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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9038c651-bd5d-35c1-b0bc-2bd52ecbaeaa | -3.46071 | -51.21586 | 2025-09-20 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bb249d29-068d-3f0e-85ba-1dd377622fd2 | -7.3318 | -44.5588 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 463c44a3-5a12-3e73-9eec-ff08e60d6114 | -5.75953 | -42.77414 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85678159-f5f0-3914-af43-4cdc352c59d2 | -9.14201 | -40.10923 | 2025-09-20 04:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f8422078-ec50-37cc-ad18-82ff0f0dd8b5 | -1.18131 | -47.79263 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12ee21a4-5d06-37b4-8abc-f1f287dd355d | -7.256 | -45.49404 | 2025-09-20 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15c2d9bc-b8cf-3dc5-9899-9dd1942be189 | -7.44182 | -42.62192 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d2272b6-fe98-3b66-b46e-322302f054fc | -7.38523 | -47.04428 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a5ef1088-7432-37e4-b5b5-bdb98bff4cb6 | -3.80593 | -52.35817 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd0c5261-2a8b-39f9-9b63-3a1a7e9e0cf2 | -6.22501 | -44.66122 | 2025-09-20 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ced12709-daa5-3ef2-b6cf-ff2305cb1fc6 | -5.52312 | -43.85819 | 2025-09-20 04:25:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db649017-b195-323e-8862-25b58cd4eb60 | -5.05149 | -47.89773 | 2025-09-20 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31de0f5d-ad3d-3d18-9897-983efbf51f74 | -7.17396 | -44.41969 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4145550-2f58-3078-ab44-41d7488f2237 | -4.31253 | -48.10285 | 2025-09-20 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77fc84e9-86ab-3953-b8ac-761a196caa56 | -5.16565 | -45.42017 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 894130c9-6a77-3ab1-80cf-39eb22ca4c0f | -5.36492 | -43.00777 | 2025-09-20 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 547bbb0e-62f4-305b-8c26-af755e802b17 | -4.99024 | -45.1466 | 2025-09-20 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4bd26f8-c6f0-36a8-ae9f-40b511972b7b | -7.23517 | -46.61273 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5797c84-f0b1-3293-889f-01a14f1f2fbe | -6.33412 | -42.38432 | 2025-09-20 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c289b016-db2b-3dbf-b7d7-4f2527c3dec6 | -6.23998 | -47.31484 | 2025-09-20 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d956820-6637-33d9-b8ce-6c599f6ed7ac | -7.5255 | -46.71553 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e1afaaf-ba41-3cf8-aa45-9b17ba1901bc | -7.0843 | -47.33474 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 536bc29e-005d-3de5-9077-6ff65ea78196 | -7.1104 | -47.85604 | 2025-09-20 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cec82215-0dc9-302f-9a73-0d5ce00d2e71 | -6.37801 | -43.34686 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0387a278-3a38-396b-8d37-31dcd77e5767 | -8.26902 | -45.62907 | 2025-09-20 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47c24379-1b81-38df-ba96-cafbe83948f9 | -2.79757 | -47.15524 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14c61c23-2cd5-392c-8106-6b111b2da2de | -8.00178 | -43.93924 | 2025-09-20 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4633ff90-4be7-3843-9461-ef1b5f256aa2 | -5.19239 | -45.48824 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a560d79-b457-3cd3-af52-ec93d939f3b3 | -5.56749 | -43.43949 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 127a6d8d-9973-334a-8aef-223d6a13a9fd | -3.68655 | -43.06701 | 2025-09-20 04:25:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d3dcba3-ca9e-367e-b57f-7b3f2be96162 | -6.32968 | -42.38826 | 2025-09-20 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd12faa7-5840-38ab-ba80-42a0a474c964 | -4.09392 | -40.49218 | 2025-09-20 04:25:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a14ef82f-0e59-3c57-9566-817d00d85b70 | -6.47877 | -45.98719 | 2025-09-20 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 040c1159-af7a-326b-9e91-19df76b8c376 | -8.05504 | -44.09019 | 2025-09-20 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0939605-5557-31a2-9664-c2967fe2fba6 | -7.11433 | -47.85299 | 2025-09-20 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 988569dc-affb-352e-8d94-8b1d0c78ae0b | -7.08596 | -47.34572 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d716ad06-7e27-3c53-80e8-39b1c15b4567 | -8.1476 | -43.63432 | 2025-09-20 04:25:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9050f3a-80cd-3411-b443-bf93f6b73570 | -7.13909 | -47.74053 | 2025-09-20 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ee83c06-2819-3452-ab52-31a3e53a5284 | -6.20035 | -41.22866 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| babb979c-70ae-3bf6-802d-021976516c09 | -8.61524 | -41.16561 | 2025-09-20 04:25:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 922e38e7-b300-393d-bb19-1a1b142ceca5 | -4.9376 | -45.48719 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb30cf08-f4fc-395c-9826-cf1664af772a | -5.3571 | -43.01085 | 2025-09-20 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f1fac143-a35e-326d-a0e1-b539ac58f7b2 | -7.30266 | -44.13039 | 2025-09-20 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f03ca07b-c937-3e1b-8e12-383881b91fbd | -1.1807 | -47.79653 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8412be9-91af-38e7-808d-2639e12d4407 | -5.56189 | -42.16039 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4197a507-e16e-3d49-958e-5494e01f207e | -5.76555 | -53.41487 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb764be8-7837-352f-9e9f-e3c1f7be395c | -4.4074 | -47.59875 | 2025-09-20 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8918b6ff-8a44-315b-9f62-9df2c0fa079b | -5.84597 | -46.29356 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4a1cd10-9e56-3a11-95a2-d0ebb9bb9da8 | -5.76759 | -45.94648 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a3e5f21-ec89-3b85-bba9-e900ab3608f3 | -6.48675 | -39.69512 | 2025-09-20 04:25:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ae17311e-5d76-3bac-8a08-2308591e1866 | -6.44864 | -41.74554 | 2025-09-20 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b4e6bdc9-d0af-30e8-8ada-0b5e265a715c | -3.02254 | -41.73104 | 2025-09-20 04:25:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ddb494c2-c9f0-3011-adfa-6f893c2207b5 | -2.7987 | -47.14804 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d213a37e-f3fb-302f-9f52-7edf8b81cf5a | -8.37825 | -44.68709 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6428d31-a751-3850-9e5c-a3f51eb63786 | -7.05167 | -46.65807 | 2025-09-20 04:25:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a08bc59-9f21-30f0-8580-0785f4bc6e68 | -6.10997 | -47.85176 | 2025-09-20 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef9046e1-14f2-3a14-ab78-42074b9ebf2c | -5.21972 | -45.4214 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfaaeb16-cff7-37bf-aba2-f1eacdb42c7b | -4.29942 | -48.27222 | 2025-09-20 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c746bb34-3eb8-3a20-901d-ed684ddd4424 | -7.68009 | -45.43212 | 2025-09-20 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 409182b0-2570-3c40-b256-2e743b32e860 | -5.5968 | -44.09007 | 2025-09-20 04:25:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58c4e638-4ff1-3e96-b38e-ab7827b55287 | -5.55122 | -42.15203 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 30d56200-575f-3cec-85e2-46a01b13c297 | -5.23541 | -37.67481 | 2025-09-20 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f0eb960-c03b-3c9b-a22f-4727e3a934f1 | -5.55743 | -42.16442 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6a709fe5-c7b0-39eb-adb3-9e994cb7d8df | -7.24944 | -46.60789 | 2025-09-20 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a26bddc5-d23d-3230-beee-d2b5c68751c9 | -8.89524 | -40.4354 | 2025-09-20 04:25:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71532854-e3d7-3b2d-95be-fb4f29019b58 | -7.44559 | -42.62249 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7151ddfc-5ed6-3f98-84fe-3ca2f9821e85 | -8.34799 | -44.77127 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b723a36a-8201-3494-91e7-92b18d92182a | -6.09598 | -42.82673 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bced051c-ad1a-3bfb-96b7-a56420bca7a9 | -5.57041 | -43.44402 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e08caab-9110-36d1-aa1b-bda18dbee657 | -5.11405 | -43.20603 | 2025-09-20 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 086cba48-b188-30bc-bb0f-728de007c683 | -3.4542 | -47.62646 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59273bc6-2a25-3fb8-b63f-4a626e94d44a | -2.14546 | -53.64856 | 2025-09-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8952b39-ab1b-3d4e-b840-5124bfdb40b5 | -7.11098 | -47.85245 | 2025-09-20 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b4e7160-17d3-33ae-9699-77e682aed510 | -1.24212 | -46.02678 | 2025-09-20 04:25:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cad7945b-82ba-323b-9b39-105c04afac1f | -4.0714 | -40.47349 | 2025-09-20 04:25:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c02e7f5e-17d3-33be-bf49-755323546d94 | -3.65659 | -41.114 | 2025-09-20 04:25:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e49cf7e1-baae-3258-bdb3-4af36eb61f68 | -2.91179 | -48.30092 | 2025-09-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5eadbc6-618e-3d36-8ef3-eae5e479719e | -5.69573 | -43.33351 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51905292-c454-38d3-935a-1a367629d3cf | -6.37209 | -43.33744 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0bc9c24-2ea9-3717-80e3-2e14fafe0d7d | -6.95745 | -42.43829 | 2025-09-20 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 82367f1e-7bac-3ba7-83c2-a17242ea825f | -5.03987 | -45.57372 | 2025-09-20 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc4cd620-b6d5-3f21-8648-9883f3363c6a | -2.79814 | -47.15164 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fc0c487-ec07-3a4f-9b91-03e50eb2d605 | -5.82726 | -46.28359 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5886ca80-98b7-36e2-b991-02dd73ce98b6 | -5.80868 | -53.4423 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 048045b0-31bc-3e3a-bea7-1976c05e18f7 | -5.30348 | -45.58332 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb704ecc-0409-3fd6-8077-42ea1168e429 | -5.62867 | -45.00031 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b60e71f-4d56-35e6-b1e5-e8eda9515d64 | -5.20716 | -45.1732 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 382f3b79-d23f-3857-bf31-d57478c05cf7 | -5.54981 | -42.16129 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d7472463-6f60-3a75-981e-d7bb801e3f06 | -2.30442 | -48.14957 | 2025-09-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db9dc492-0378-3c77-9ca7-d9fdfc04241c | -4.94139 | -42.71375 | 2025-09-20 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac2578a8-9730-33d3-9344-4892c04f6e1f | -5.97626 | -44.93007 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b19c7bb6-be1e-3d82-a024-e47b7a5555ae | -2.83335 | -48.65565 | 2025-09-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dce6b367-8860-3c6e-803b-8ccc329bf39f | -2.43532 | -49.34032 | 2025-09-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6601421c-38b8-3903-8091-07b61921ecc3 | -6.69038 | -44.09176 | 2025-09-20 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdd65217-4cbf-3a61-af76-d7c4344fe79e | -5.82396 | -46.28308 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6566858-406e-366e-b247-a40513a1b7ca | -5.55578 | -42.20206 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 97620630-aba4-3990-a159-c6d9c0e0a0e7 | -5.62812 | -45.00387 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a83ffee4-0d54-34cb-9d4d-c9a447c25e26 | -2.79138 | -47.15062 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cee177f7-17aa-3f84-8128-7475a2522107 | -8.36104 | -44.68452 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b5be8ef-0aa4-3ff1-8aab-da3babdf0015 | -6.55827 | -43.47243 | 2025-09-20 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README14.md)
