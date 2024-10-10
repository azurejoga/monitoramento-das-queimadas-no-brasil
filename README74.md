# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30c653ec-97e1-33e1-a1a1-8aade8da0db4 | -7.57903 | -46.80986 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d78438f7-6d57-3fdc-85fa-68562faf0959 | -7.44828 | -46.68857 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a21ed873-4ee8-3f75-9859-7d23ce1b2e90 | -7.44485 | -46.68798 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 812cbae1-2168-386a-8919-4f04b9f21498 | -7.39735 | -46.13852 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11442651-cb76-380a-bb8e-9e94fe6a17fe | -7.39677 | -46.14214 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 073c2602-7760-3c55-84b4-d5b01d02a1d2 | -7.39501 | -46.15299 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e7a7ea8-515a-321e-80f2-25f45d590720 | -7.39456 | -46.13436 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94bd52f9-52fb-382a-bfe0-1726d182b996 | -7.39117 | -46.13382 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a239c2bf-e737-3757-a182-bef2da338481 | -7.38825 | -46.15192 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19afb1c4-01cf-39e2-9bd5-cdc8d0930110 | -7.38603 | -46.14415 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df831dcf-600c-3ba0-b354-7b5aeb2b2b05 | -7.38601 | -46.1409 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9018879-cb87-3b0f-a83e-fe9ee5a173da | -7.38545 | -46.14776 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79990f82-52fb-34ab-b052-fdfa386f7ed7 | -7.38543 | -46.14452 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 222f9e31-28fe-30d5-9c68-6e7e5c126782 | -7.38486 | -46.15137 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29381e0c-6365-3e4f-beba-e9fff1a1cf2c | -7.38486 | -46.14813 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 532fc5c2-1969-315c-aa21-2fb8c39998b4 | -7.38205 | -46.14397 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3377fcc-fd5b-327f-8c3d-76cc077dcd46 | -7.37924 | -46.13981 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8423d895-e91b-3476-921b-a969a29d8287 | -7.37867 | -46.14344 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eff1d4a0-25a6-37ee-8070-8ef5f93af81d | -7.33962 | -46.73306 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e842373d-342d-397a-bead-57005e39f0ce | -7.33618 | -46.73249 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5a1968d-7373-3055-a4d0-30d982b4a499 | -8.70484 | -47.04209 | 2024-10-10 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8624d046-f9c5-3c3f-9853-6848ffbafc8c | -8.68344 | -47.10834 | 2024-10-10 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39a335fd-cb63-3e9a-8137-64ff14b9e4f9 | -8.62609 | -46.49092 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d262e9bd-c0b5-329e-8f29-3936c6680e60 | -8.6227 | -46.49036 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fbc4565-477d-3c1f-b211-c911dfe94a71 | -8.62212 | -46.494 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5be6091-b35a-3751-b8a0-5e234fde75fc | -8.57624 | -45.77832 | 2024-10-10 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d5db5e-b25c-388f-b7b3-985be5f5661c | -8.4768 | -46.91715 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0572388-e678-3f2f-be8f-84a77af0102a | -8.47337 | -46.91659 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6fba394-a0eb-3620-b871-bb7047250b0b | -8.40263 | -46.96645 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae351a74-20cb-322a-9597-2c00da050b7b | -8.39919 | -46.9659 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1441b729-9368-38f1-957b-04e864210a91 | -8.25452 | -46.86569 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 239972f7-2b47-38fd-8e2b-106bc3f7a26f | -8.25108 | -46.86513 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c794b70a-9a91-3de2-bcf1-79d8c0392f4f | -8.24175 | -46.27666 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7873e61-b901-3f25-af64-35bfc6f58f6c | -8.23838 | -46.27612 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 688de0cd-5f5a-3560-bcda-ce8bbb145738 | -8.13846 | -46.26791 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aec0fcbd-ae5b-37eb-ad41-63269b10aa99 | -8.13567 | -46.26375 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 752d6610-fdf9-3ba6-85b4-fbab3984ba34 | -8.13509 | -46.26736 | 2024-10-10 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e292148c-bb69-3985-9771-ecd7668d8310 | -9.24625 | -46.43769 | 2024-10-10 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a1d6be2-aab6-38df-bf6f-d95e640cd5a6 | -9.24566 | -46.44135 | 2024-10-10 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb50929e-9ffa-3f81-be45-41d2777cf172 | -9.24508 | -46.44501 | 2024-10-10 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dca762dc-b8df-3dbc-9a98-473e80666b21 | -9.14501 | -46.39201 | 2024-10-10 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 84036ac9-e293-3bf9-9efe-0e95604ba43e | -10.61503 | -47.3067 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f82314a-352b-3ee2-9def-2fddad64fc14 | -10.40917 | -47.37017 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c07c2cbd-8a98-3c7f-9d8b-253ca842012b | -10.28126 | -46.73484 | 2024-10-10 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90e7b308-abe0-310c-9f29-250056f37e64 | -10.27731 | -46.73788 | 2024-10-10 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 239db8ea-6487-3679-b34a-836ca6e9359f | -10.27393 | -46.73735 | 2024-10-10 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e33b9a88-efc8-3acc-97fd-8e817cccde04 | -10.27336 | -46.74089 | 2024-10-10 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2976fa7b-0923-3584-8c01-671395552172 | -10.27055 | -46.73682 | 2024-10-10 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f47c6240-9ede-3d8f-9117-741ee5fdac92 | -10.26997 | -46.74038 | 2024-10-10 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e884300-81a3-3f9d-a203-2a4b977188cf | -9.82608 | -46.13173 | 2024-10-10 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7841275f-9332-3a51-afe2-ba92f6af59f9 | -10.14126 | -46.32149 | 2024-10-10 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cf216d1-1cf1-3b1e-b4a3-1274539ee88c | -10.13791 | -46.32095 | 2024-10-10 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 199fb962-37d9-322b-9a08-03b228476002 | -12.28281 | -46.78413 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5949ad63-d3cb-333f-927d-8d638ed04447 | -12.24606 | -47.16032 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bdffa58-9180-3677-bb4b-22e6aab6b309 | -12.24547 | -47.16396 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48f9a73b-9111-3ada-b2c6-177c411d6065 | -12.20557 | -46.72024 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92e5c57f-690a-3192-9f68-7b95d3ac2185 | -12.205 | -46.72382 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af22eabb-c567-3cbf-b006-55be1795f523 | -12.20384 | -46.73098 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1b51225-b0bb-3d98-b16e-64dbfb059f0e | -12.20198 | -47.14978 | 2024-10-10 04:19:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebbd3aca-d103-3108-96f0-6aff1ee8fc84 | -12.20165 | -46.72326 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3930dcd7-048e-3285-8c6e-41f5a776e5a5 | -12.20107 | -46.72684 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 572c08af-0381-385c-bbcd-91022d876614 | -12.2005 | -46.73042 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12ec0b67-e578-371c-bc40-473442e46a85 | -12.19992 | -46.734 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d00fc1e4-e996-36f1-8e12-15bc53d52cba | -12.19773 | -46.72629 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff29f582-3e04-3170-8c0c-50e094fac310 | -12.19715 | -46.72987 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d32d83f-1581-3a40-b30f-6c4f6c4ab0a3 | -12.17527 | -47.57262 | 2024-10-10 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b00586b7-8a17-3c46-9f05-a379bb5e538b | -12.17186 | -47.57204 | 2024-10-10 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ac340a8-bbf9-38f2-83aa-a9ca8815bf17 | -11.79572 | -47.39266 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46034cc4-90c7-3afa-b116-bc9b3a0a11aa | -11.79352 | -47.38465 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a225cf4c-9ec9-3e0e-b97d-285d901a1f2d | -11.79292 | -47.38837 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f856c30a-0c22-3644-83b2-066dba271e94 | -11.79269 | -47.41122 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fbec065-3590-3ac1-89ca-5be85de074e5 | -11.79231 | -47.39209 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af4d727a-8f6c-3b30-91f3-d0545407dcdc | -11.78951 | -47.38781 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf7f309e-eca9-3edc-a855-68223db1c762 | -11.78891 | -47.39152 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8dfe0e8d-bd9c-3650-82f6-8853aca9eb10 | -11.67568 | -46.47559 | 2024-10-10 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c594274-7675-371c-9ebd-f707549d3cb2 | -11.42607 | -47.17262 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcc5a9a2-8f19-3182-b083-862639f7de36 | -11.42268 | -47.17207 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d36e8f3-7950-3632-83d8-bb05fd5f8362 | -11.41929 | -47.17151 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4a79739-aa9b-34c3-9109-38770069a047 | -11.39994 | -47.18348 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdc5bcd2-6d1e-3d09-9738-bc14c154d015 | -11.39715 | -47.17923 | 2024-10-10 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea51c73a-c087-3644-95b7-23900e55be84 | -13.50212 | -47.98545 | 2024-10-10 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2887e8b-282f-3f32-8ba7-4c335c724b1c | -13.49871 | -47.98482 | 2024-10-10 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ec18d23-d489-3932-ada5-15605dd04cde | -13.44247 | -46.71138 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71af05be-6b0d-3ef0-831b-ad4c869a46eb | -13.21442 | -47.99199 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e680262-7fbb-303e-bb8f-7b698fe6d431 | -13.20882 | -47.98318 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f6c080ee-bee8-3ee4-b49b-ca701993bd73 | -13.20602 | -47.97876 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0843f44e-92d7-33ef-8e43-111df19ff6af | -13.20539 | -47.98257 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 032bc766-acb9-3ce4-ae23-833627d9cc00 | -13.17644 | -47.12783 | 2024-10-10 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f0f58ef-39aa-3236-9116-cf5983db0200 | -12.52979 | -47.65107 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5e60587-5f63-3406-a445-a5dc9509a985 | -12.51858 | -47.42015 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd46e3c7-54b3-351c-9678-2bdb3cde5e9f | -12.48487 | -47.4981 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c11d4e9-e8c0-349e-80a1-78bc4d08c0f9 | -12.48426 | -47.50182 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0adc89f-3314-32ee-a918-db2a695cea36 | -12.48086 | -47.50124 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db9b0665-7d80-35d6-8539-0ec2d5364f87 | -12.48025 | -47.50495 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fe3187c-3c78-3f10-a89c-d274f9928b14 | -12.45891 | -47.31231 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cf18a5c-9d59-3c28-be96-2802e761d6d1 | -12.45612 | -47.30807 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43eeaa07-4204-3c7c-9cd5-01ed1846b1db | -12.45552 | -47.31174 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc1e86dc-2119-39da-8d83-3b8d58ee13cf | -12.45493 | -47.31541 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49c7583e-10cb-3c33-9d96-cfc565282436 | -12.39018 | -47.06899 | 2024-10-10 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d44415d4-7e01-3955-9bb0-6c55d6da3c06 | -12.3874 | -47.0648 | 2024-10-10 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README75.md)
