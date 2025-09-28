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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4341682a-8855-3473-9622-d1a7108ddf88 | -5.7396 | -42.8461 | 2025-09-28 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 241.8 |
| 0f5e6a32-2415-3113-a06a-8a0e7f1f7294 | -9.6324 | -62.8534 | 2025-09-28 02:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 149c915a-355f-3a2f-8c21-559e45829f92 | -9.6512 | -62.8336 | 2025-09-28 02:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 229d0da8-41b8-33a9-a34d-aeb37d3d23f3 | -18.0458 | -51.1336 | 2025-09-28 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 436b9516-28b3-3377-82e4-d806a79f1712 | -18.0453 | -51.1556 | 2025-09-28 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 698a1c1b-5399-3d56-888d-aa8a94a551b6 | -11.3838 | -45.008 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e77415fc-9f1e-3204-a095-3a17dab05c58 | -7.7412 | -47.007 | 2025-09-28 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1e92a076-8bac-31d4-a9eb-56b9765347da | -11.3642 | -45.0339 | 2025-09-28 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 854107ad-708b-35d8-9ed2-2810528acd9b | -7.7975 | -47.0019 | 2025-09-28 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 2777064a-ff40-3435-87f5-347a62bc716a | -18.1977 | -53.3208 | 2025-09-28 02:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3bb666fc-f906-3dfb-989f-033868bc21e2 | -9.6697 | -62.8518 | 2025-09-28 02:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8f2e0901-8291-3cad-a44f-c08637b1c368 | -9.6326 | -62.8344 | 2025-09-28 02:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 954a688d-dbac-3f90-986b-2507d4a37104 | -5.8187 | -44.4413 | 2025-09-28 02:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 75eb744f-c2d2-3df2-97e5-bdb333e9de3e | -5.4742 | -41.0767 | 2025-09-28 02:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| f99b8590-3e13-3fa1-9a42-abfbc727af38 | -18.0453 | -51.1556 | 2025-09-28 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 1a48a967-943b-3480-83ce-fc4f4d36c82c | -8.2856 | -45.4545 | 2025-09-28 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 175efb98-a98c-35a4-acb9-b68204ad5d80 | -5.7393 | -42.8697 | 2025-09-28 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 861f3026-e149-3ab6-9c0f-f5a0d710b832 | -18.0254 | -51.1591 | 2025-09-28 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 55ae9113-8507-399a-a4c2-71487a60b37d | -12.6917 | -46.8708 | 2025-09-28 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1d9f1688-63eb-33dc-b23d-94e34681a06a | -9.6324 | -62.8534 | 2025-09-28 02:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 949dfe44-a2a8-3b49-8836-395a77ea868f | -18.0259 | -51.1371 | 2025-09-28 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| a0c5ae96-285e-3164-b3cd-fe64ef8330e1 | -16.9671 | -53.6763 | 2025-09-28 02:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c99e9d51-9917-36c2-9b87-47f7b8ae528b | -18.0458 | -51.1336 | 2025-09-28 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 97bd3b29-4871-3186-a200-0b628f467642 | -11.4604 | -44.997 | 2025-09-28 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| bbbf86a7-12fb-3d56-8fac-a564bcab33ce | -9.6512 | -62.8336 | 2025-09-28 02:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 08989f7d-5a81-31c8-890d-a1d8c505e475 | -16.9667 | -53.6975 | 2025-09-28 02:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| b168bf83-f218-3e13-a1e5-44cb7baa3508 | -5.8149 | -42.8167 | 2025-09-28 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| bfbd8dff-1396-3320-bb8f-deca1b149310 | -5.7585 | -42.8211 | 2025-09-28 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| aeae191a-97f7-314f-85b9-fa03d0eb423c | -9.6511 | -62.8526 | 2025-09-28 02:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 5a5b4ac8-6927-3ce3-a002-c87b9d829042 | -2.5957 | -48.4141 | 2025-09-28 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 52fcb682-0b5b-33eb-8c07-6e288d7414c2 | -11.4413 | -44.9998 | 2025-09-28 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 307.9 |
| 8540cff1-c6db-3ee0-bcf6-910aacce99e1 | -8.1614 | -46.3899 | 2025-09-28 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| f19e3bb0-52b9-3251-9f51-360e5a233991 | -8.1802 | -46.3881 | 2025-09-28 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 5e2c2df3-fafd-3d96-a8e2-e688ee80b6c4 | -6.0937 | -49.3897 | 2025-09-28 02:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7ebdf28b-cf6c-377d-9e39-6530cc492941 | -8.1799 | -46.4104 | 2025-09-28 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| fb6a0be2-3fd0-333b-a02e-5a7f7bd8ab96 | -11.0083 | -57.0658 | 2025-09-28 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f71e3080-42a7-3408-b1c0-5313256340bb | -11.4417 | -44.9767 | 2025-09-28 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 946202e8-345a-38b5-814c-5adb98dfabe1 | -2.5772 | -48.4146 | 2025-09-28 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 67fc113c-f829-380b-adcf-1f4acc68fe89 | -11.4608 | -44.9739 | 2025-09-28 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| ecf4b795-7e33-305e-ad17-977fe46f27c8 | -5.7396 | -42.8461 | 2025-09-28 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| eee82b58-e008-3379-8714-fc7040c8aa67 | -7.3847 | -47.0378 | 2025-09-28 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 7c2e4cb5-89ef-3e98-ba00-f6b49e94bd2a | -5.7398 | -42.8226 | 2025-09-28 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 956a6278-ece9-35dd-8f70-ae21f288e7ff | -5.7583 | -42.8447 | 2025-09-28 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| f03cc814-b540-3c0f-9c58-e884852c3e2b | -7.7972 | -47.0241 | 2025-09-28 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 43e57ca7-bd61-3639-9686-c3076f227e47 | -16.947 | -53.7003 | 2025-09-28 02:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| cfa07e50-4df9-3b1b-b4ef-6bcf585eebc4 | -11.9846 | -47.8865 | 2025-09-28 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d2904a1d-392d-391e-995d-ea2b7a914a60 | -11.9846 | -47.8865 | 2025-09-28 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a3ea76e6-e1b3-3c23-b0ea-55ebb04d46c2 | -2.5957 | -48.4141 | 2025-09-28 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2f6a55e4-a1ec-3968-a8de-431bb3c471ff | -9.6511 | -62.8526 | 2025-09-28 02:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 28eabe19-99fd-3da5-ab03-dff81bb997b7 | -5.7393 | -42.8697 | 2025-09-28 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| c490702a-f958-368c-9ae2-92e646abb28b | -8.1799 | -46.4104 | 2025-09-28 02:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 36764ea2-e306-3a82-b5ef-d79761ef8fad | -5.8149 | -42.8167 | 2025-09-28 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 5735cbe8-1d5b-35e2-81d1-4c05c6ad81d9 | -7.3847 | -47.0378 | 2025-09-28 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 2160deed-dd2e-3791-b967-1f908fb1312d | -5.7398 | -42.8226 | 2025-09-28 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 9db8283a-3c77-39e2-b65c-9678b3d141fe | -8.1611 | -46.4122 | 2025-09-28 02:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| f7a8031c-2cd2-372c-82b8-8d991b7ec8de | -8.1802 | -46.3881 | 2025-09-28 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 5418ce48-5574-39d7-9ae5-a4e97a8ff57d | -16.947 | -53.7003 | 2025-09-28 02:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| fd8604f3-7272-3c14-a2c5-ea9cabce7c42 | -18.0254 | -51.1591 | 2025-09-28 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6ec20789-4305-3b9f-bec0-c9e26a056c0f | -18.0458 | -51.1336 | 2025-09-28 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 60145e93-4c21-3edc-98c3-56fa1d67b9e5 | -7.7972 | -47.0241 | 2025-09-28 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 4808e9ca-0620-3279-9d98-6fbbc69f1aa3 | -18.0259 | -51.1371 | 2025-09-28 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b4689f4c-e451-3221-9e96-f040bb5815eb | -9.6326 | -62.8344 | 2025-09-28 02:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bba43c89-0eef-3cd9-aa00-1baa0c64c88c | -6.4274 | -43.5152 | 2025-09-28 02:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 17ed59ae-3410-3e3b-b070-09d632a821d4 | -16.9864 | -53.6947 | 2025-09-28 02:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1a37371a-1780-327c-a6df-c6c11b3dc191 | -7.7975 | -47.0019 | 2025-09-28 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 699d5879-baf8-3af2-892a-1079049410a6 | -7.7787 | -47.0036 | 2025-09-28 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6a4b1a7b-a728-3ca3-98eb-5c9d95e4bce7 | -7.7785 | -47.0258 | 2025-09-28 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| f40f470a-16bf-3ad6-8026-1a0e55c2c727 | -6.0937 | -49.3897 | 2025-09-28 02:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6271be00-ebb5-3aa1-b39d-669949a535d1 | -18.0453 | -51.1556 | 2025-09-28 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ffa77c3c-fdc2-3b6e-9f90-6be18bd65459 | -9.6512 | -62.8336 | 2025-09-28 02:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 5d9e8459-b065-38b4-aacd-b4f4dd6cedce | -5.8151 | -42.7931 | 2025-09-28 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 37d57117-0745-3c13-bac3-67b635e1951f | -16.9671 | -53.6763 | 2025-09-28 02:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 3a7cfec7-a3f1-304a-ba21-5038227c869b | -11.4417 | -44.9767 | 2025-09-28 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 11105880-862b-33fb-822c-1a93de599ce3 | -5.7583 | -42.8447 | 2025-09-28 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| b44a540c-efde-3275-b21b-b8506b63be10 | -5.7208 | -42.8476 | 2025-09-28 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| c4e7971f-cccf-3e2f-b000-7060072d0e8d | -12.6917 | -46.8708 | 2025-09-28 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e0563490-5b8d-3642-aa31-86b93b2fcc9a | -16.9667 | -53.6975 | 2025-09-28 02:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 59813fed-ac85-3054-89b8-85d2febc7961 | -8.1614 | -46.3899 | 2025-09-28 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| cd369026-4b27-3eb5-9bca-3b254374559e | -9.6697 | -62.8518 | 2025-09-28 02:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2fb84b23-78d8-3dec-a71c-296f43979a6a | -9.6324 | -62.8534 | 2025-09-28 02:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 607e70bd-0386-3937-a00f-ded01a02ea53 | -11.4413 | -44.9998 | 2025-09-28 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 192.5 |
| f4cbccbf-17df-3338-898d-0328820032c6 | -11.4604 | -44.997 | 2025-09-28 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9a68d9d4-8bbe-3a76-98a7-eb70c208991b | -8.2856 | -45.4545 | 2025-09-28 02:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9dc1b58b-8a25-3764-8b36-bbb21b942998 | -9.6698 | -62.8328 | 2025-09-28 02:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ffea024b-8549-3125-83ab-9288654165f8 | -5.7396 | -42.8461 | 2025-09-28 02:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 188.0 |
| 6c244d4d-81ba-36ea-a5dc-e5222b4ad287 | -5.7396 | -42.8461 | 2025-09-28 02:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| 6b4665d0-4b7f-36b3-b4ef-bbde78e28beb | -5.7583 | -42.8447 | 2025-09-28 02:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| e7e2c2c7-d672-3559-9c98-9d4f8a86ce22 | -7.8823 | -44.5594 | 2025-09-28 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b7224ef9-e2b7-3268-876c-24c23406c72f | -7.3847 | -47.0378 | 2025-09-28 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| bea2523b-d853-30db-8523-c4eaf97eea85 | -16.9667 | -53.6975 | 2025-09-28 02:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 169.0 |
| f48f56bd-b7d9-3f1c-a08e-2e42e54e6cc9 | -11.9846 | -47.8865 | 2025-09-28 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c39e0f95-649e-39c3-ad31-a4a70d9bb28c | -7.7785 | -47.0258 | 2025-09-28 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4ba8da3e-37cb-3b51-993a-396958e7a575 | -16.9671 | -53.6763 | 2025-09-28 02:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5fcd6bc9-b65e-3312-a052-2f6a78ac0dad | -7.8634 | -44.5612 | 2025-09-28 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 442a7e2d-8cd2-3742-8154-2c507f159e06 | -9.6326 | -62.8344 | 2025-09-28 02:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ba1224d9-4542-376e-81f7-20f8fff00d85 | -5.8187 | -44.4413 | 2025-09-28 02:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b91c6e00-11bb-3547-a8bd-92936220f3b3 | -18.0259 | -51.1371 | 2025-09-28 02:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3bf16a53-117d-3423-af20-dc198a291b68 | -15.0579 | -42.3424 | 2025-09-28 02:30:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 1585a0f2-aa0f-3c22-9347-123b1a79495e | -11.4413 | -44.9998 | 2025-09-28 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2375cf8d-5c8f-36f0-8590-76a5acc7f71b | -18.0453 | -51.1556 | 2025-09-28 02:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |


[Clique aqui para ver as próximas entradas](README10.md)
