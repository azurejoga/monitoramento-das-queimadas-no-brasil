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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 366f03c8-3c02-3c8d-8f97-a7945cf21e6c | -5.20599 | -45.61996 | 2024-12-24 04:14:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d91dcf1-80f2-3631-866e-3c817684fcab | -3.83488 | -41.56286 | 2024-12-24 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb8f1562-deaa-3bd6-b8e5-486eaaf1c5d8 | -5.98566 | -45.39582 | 2024-12-24 04:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6468b0e5-8071-3614-980f-444c42ce06e9 | -6.23204 | -55.62867 | 2024-12-24 04:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acf326da-56a4-3655-ba63-491edd018a0c | -6.96866 | -43.55237 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3c504aa2-59d1-3d40-8523-dff737a4ee51 | -2.86462 | -51.65492 | 2024-12-24 04:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8a793a-8543-3b94-b5d4-68b7cda579e4 | -6.91709 | -43.53352 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0813a336-fea0-30ae-93c4-5614bb540332 | -9.15876 | -40.96647 | 2024-12-24 04:14:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d8d209c3-5701-3b25-b9ac-3e543c538c65 | -6.957 | -43.53983 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5cd95d3-34d0-3a63-a021-9f28b013e987 | -6.9859 | -43.27012 | 2024-12-24 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 419ad2c6-6ee8-34f1-9adb-a1aef95b133d | -4.43152 | -46.13604 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fda8667-5543-37b6-9736-20f6a4373a16 | -4.51087 | -42.06269 | 2024-12-24 04:14:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fc42c8b2-a5e9-3e10-821a-7498aeaa7dd0 | -3.18237 | -45.97305 | 2024-12-24 04:14:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 471ebfcf-40de-3f7e-8f1f-a73aa6c6282c | -2.79335 | -51.77062 | 2024-12-24 04:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4890d72f-6a27-3844-affc-4c60f9140008 | -3.0248 | -53.89728 | 2024-12-24 04:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3f209e7-9e0b-3906-9285-2d62cee88540 | -6.11909 | -43.01596 | 2024-12-24 04:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0884ae60-4c67-36ce-8de5-44ad061991dd | -2.86803 | -51.6555 | 2024-12-24 04:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 745abb8c-89f7-371e-906e-123eb0dbb763 | -3.13307 | -52.13018 | 2024-12-24 04:14:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a3a4fa-b35a-38f6-9651-5fd88bcc63d3 | -6.94757 | -43.53477 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8db9c6de-a5ef-374a-b77d-66e7dcf5cb92 | -8.47363 | -40.66635 | 2024-12-24 04:14:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9072013b-b2b0-3171-9dd9-ee54b4fb5fb1 | -5.38896 | -42.95071 | 2024-12-24 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d7040cc0-4426-363a-9a9d-4519cd544895 | -6.95645 | -43.5433 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beaa9b29-be32-35a7-abc1-42a0d7fc4e54 | -5.39228 | -42.95123 | 2024-12-24 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2e842334-063c-354c-a01c-2f01b9c120a3 | -6.99642 | -43.26822 | 2024-12-24 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21076769-50fc-3251-bbb4-058e4f379cb4 | -3.02564 | -53.89247 | 2024-12-24 04:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3c7c16d-9ecb-3c52-bbf4-c180659ea856 | -10.59836 | -38.40882 | 2024-12-24 04:14:00 | NPP-375D | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 027ab275-06c6-331d-bb8e-82c7d7e30fae | -4.43214 | -46.13696 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1777b36-7b61-3bba-a103-6e82673072c5 | -5.92045 | -38.12267 | 2024-12-24 04:14:00 | NPP-375D | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 91be9088-bb71-3f30-8c22-fbb8f60c968b | -6.19509 | -42.63968 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5b748d8d-9e98-38c9-9fbb-1000e199ab01 | -6.20563 | -42.63774 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4e126bc3-0632-3c11-9bf2-16f9e9f11aae | -1.71402 | -54.49004 | 2024-12-24 04:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3667865-fff4-35f5-8208-c97038b7580a | -6.20006 | -42.62975 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49edcf55-be2b-3ce5-9c03-6eab9af40332 | -5.25229 | -40.40412 | 2024-12-24 04:14:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1e923a43-3602-3dc6-be7d-5ddbfc27e8f2 | -6.9437 | -43.53772 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3d58c62-54f0-3f80-ac8e-9048c1aa7b5d | -5.98629 | -45.39194 | 2024-12-24 04:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e8658db-f979-32c0-87f1-473a6a67ac14 | -7.23711 | -37.43389 | 2024-12-24 04:14:00 | NPP-375D | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2cda9f4-0069-31b5-8bb0-d4d3c1ab9f2c | -6.69018 | -39.12062 | 2024-12-24 04:14:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3273af44-6f8b-30d6-a2c3-40eddf4e39d4 | -3.80604 | -51.03564 | 2024-12-24 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4856c88-1a73-394c-b34a-00cde465146c | -6.31227 | -43.46639 | 2024-12-24 04:14:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25781f24-50b6-3bc0-9253-6b847117dc58 | -4.51142 | -42.0592 | 2024-12-24 04:14:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 202e1d87-55b2-3a99-992d-a7bef16f9fe1 | -6.07132 | -42.63124 | 2024-12-24 04:14:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 13e97f44-14bf-32df-bcfc-d4726af3dc56 | -5.89246 | -42.33122 | 2024-12-24 04:14:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b197fc12-391a-345a-b4b8-0a1c827cd072 | -5.8958 | -42.33175 | 2024-12-24 04:14:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b211e126-10be-3c15-b08f-d6cef569ea75 | -4.52288 | -45.82807 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82172fde-9a9d-389a-86d6-8982583aee85 | -6.69402 | -39.12113 | 2024-12-24 04:14:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f0d878ca-6f3a-357f-b3c3-40b7869e8abd | -5.39119 | -42.95816 | 2024-12-24 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fdeb0384-be79-3142-bcb3-4c6f6c3d437e | -2.54838 | -54.76544 | 2024-12-24 04:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08fd82e8-9620-3331-bbbd-ac727f363b2b | -3.83544 | -41.55932 | 2024-12-24 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8fd4a95a-15be-3ffe-8a89-9579a551f910 | -6.98922 | -43.27064 | 2024-12-24 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a82477df-f549-3ae2-bce9-4acf2caf7dd5 | -4.5301 | -45.82921 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bf00e55-23ed-3f26-bd62-b674fa38b3bf | -5.83927 | -40.68887 | 2024-12-24 04:14:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee82f5d1-c1e3-3de1-a9bf-19961090cbd2 | -6.11668 | -43.01575 | 2024-12-24 04:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6590f328-0db9-3f33-b226-6682b78b8cab | -3.17938 | -45.96814 | 2024-12-24 04:14:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d42980b3-b336-364f-84b0-78e811a1c5b8 | -2.58347 | -54.2523 | 2024-12-24 04:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 394f627c-b858-3481-bbd7-54c1e2fea8a3 | -4.33134 | -40.18722 | 2024-12-24 04:14:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cf2e9d43-d39f-3698-a8db-e68f61d6b180 | -6.20896 | -42.63828 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a1966bd0-56c8-3950-9541-d2dcd4b93f50 | -4.51366 | -42.06671 | 2024-12-24 04:14:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 25be6925-9273-39a4-abe8-451f291ee407 | -2.5503 | -54.7677 | 2024-12-24 04:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 837d2976-862f-3c33-8132-6ff8b2ef8395 | -2.92136 | -51.58121 | 2024-12-24 04:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2dcca7d-889d-38c5-934d-338bcab2e58d | -5.53276 | -42.853 | 2024-12-24 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 44de64b8-ccf6-3487-a917-9024c1d7c4c2 | -4.14917 | -43.64721 | 2024-12-24 04:14:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6d03ac0-ae87-3ce5-8d8f-934cb61b4b0e | -7.38168 | -37.46278 | 2024-12-24 04:14:00 | NPP-375D | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc0a31b3-2750-3e5b-becd-6c702f1e0ee2 | -6.99309 | -43.26769 | 2024-12-24 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb1fe1a6-bd2e-3edd-bbad-33ed18c26498 | -2.93563 | -49.44183 | 2024-12-24 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b393a399-f46d-30dd-ad2b-8e8f4a364f49 | -5.9904 | -45.38866 | 2024-12-24 04:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 523f7063-28d2-336d-83db-f071c5da4d75 | -4.51421 | -42.06321 | 2024-12-24 04:14:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6b98bc30-7bf3-339c-8999-52e6dde2f223 | -9.37208 | -43.27785 | 2024-12-24 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4aaf72f-3f7b-38b9-8652-23f5059f872b | -6.2123 | -42.63882 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91eebec1-b9c9-3052-848a-5568f9794033 | -3.2942 | -45.85694 | 2024-12-24 04:14:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e97362d-eb47-3470-ba91-4c331e4f5b92 | -5.98977 | -45.39253 | 2024-12-24 04:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8d2651d-8cd0-3539-a980-4ead676fe87c | -6.22544 | -55.62757 | 2024-12-24 04:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29d8eded-5473-3352-903c-29e5025eed90 | -6.95312 | -43.54278 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 599ba714-c5d4-30fc-b702-51de837d67af | -6.97253 | -43.54942 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f033ebec-b152-3ae7-a027-b08080123223 | -3.21824 | -45.44615 | 2024-12-24 04:14:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2be4be7-632e-3250-8295-ba9b62e41b5b | -4.3017 | -40.70076 | 2024-12-24 04:14:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 28663d14-cc0c-3c18-a502-9b889feeb1f1 | -3.83824 | -41.56338 | 2024-12-24 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4a99f92-3c82-38fa-bad2-701db568cb21 | -3.18906 | -45.97854 | 2024-12-24 04:14:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa500ca-3837-39f5-8890-8ea374e03693 | -6.9724 | -42.99384 | 2024-12-24 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 67801c45-fcc7-3b7d-80be-7509e5d136f1 | -12.71321 | -40.20919 | 2024-12-24 04:16:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f8bb35ed-6b0d-37a5-b8d3-b4aaf01fb60d | -12.30018 | -37.86084 | 2024-12-24 04:16:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f638858-f379-3a5a-ade7-7b747d785118 | -12.81339 | -38.26677 | 2024-12-24 04:16:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6b10b6c-4cf1-361f-a901-d65593e5ec80 | -11.87806 | -40.95205 | 2024-12-24 04:16:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 35dd9b52-c6c2-3591-a177-fdc94da60925 | -13.39629 | -40.44587 | 2024-12-24 04:16:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c944499d-195b-3f8d-9f15-1d872c4aef88 | -12.18369 | -41.3555 | 2024-12-24 04:16:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 542733cb-6ce0-3d04-b3e1-03694c161d53 | -22.54039 | -48.81335 | 2024-12-24 04:18:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3af23d0-cd64-3e45-b017-0a038c5b4b42 | -23.23832 | -51.2874 | 2024-12-24 04:18:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59c11f5c-61c9-347f-a0a3-b24bb75667a4 | -23.23919 | -51.2826 | 2024-12-24 04:18:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff046948-5ea1-350e-9825-1dc8d1fe5980 | -23.23545 | -51.28182 | 2024-12-24 04:18:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a32dcdb9-9bb2-3424-bfc5-f9da8259c1df | -23.23458 | -51.2866 | 2024-12-24 04:18:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c1df4ae4-0bd9-3570-8072-2d7c62c75315 | -30.55634 | -52.8897 | 2024-12-24 04:21:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d35d9c75-847f-398f-b83b-495187c59a7e | -5.73316 | -44.11066 | 2024-12-24 04:36:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52ce0584-aaa9-31c2-90d2-df649ab5f0c2 | -4.44186 | -45.61921 | 2024-12-24 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ad98bb7-6e74-3124-9c0c-6fb7536214d3 | -3.77331 | -51.97408 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37d152ce-b3b5-3c0b-992d-0ad15a3080a6 | -5.9914 | -45.39292 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f62a04ef-b909-394f-acc8-761ed0c84265 | -2.21352 | -45.44664 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a64c89a-c475-3854-b0ce-b10f88573115 | -2.9953 | -40.39797 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9f5d93e0-9d02-3dde-9f96-0b8089ac9f86 | -3.58622 | -59.61563 | 2024-12-24 04:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4b581d2-a120-3764-9bda-2d7703e2dac2 | -2.35714 | -54.61468 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7a629f7-1afc-39a3-9b02-57404b7a6a62 | -1.6403 | -45.8539 | 2024-12-24 04:36:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37f678f4-04de-3c74-bbab-1133007eba66 | -6.2003 | -42.62992 | 2024-12-24 04:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
