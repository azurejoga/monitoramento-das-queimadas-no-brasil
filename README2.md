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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21c0a7cf-1138-351b-b4ab-7855ef446a32 | -12.32184 | -46.07655 | 2026-06-12 00:07:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 132d119f-8c8b-33f4-89fe-68fbc08d1bcb | -3.98486 | -47.93658 | 2026-06-12 00:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cd259790-4876-3a06-97fc-cf281d200a0f | -3.50149 | -48.04155 | 2026-06-12 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| a06ee273-5b57-3faa-8afd-3d212ec6c5ee | -3.50922 | -48.03117 | 2026-06-12 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88d88f82-387d-3758-97a9-aa6c2c1c21dc | -3.51049 | -48.04031 | 2026-06-12 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e79b069e-36b4-3edc-b4b8-ea518537406b | -3.50022 | -48.0324 | 2026-06-12 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b3a26a9f-3ca4-3dd1-9677-dbf8b0557df8 | -7.3474 | -47.0188 | 2026-06-12 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 5287865e-7c34-37bf-917a-11ebe2b0c717 | -12.8548 | -44.3625 | 2026-06-12 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 11a24dc6-0f50-3051-81d7-ce7f748e7127 | -6.5721 | -47.9132 | 2026-06-12 00:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| f4379f67-be7f-3461-85cc-e93936da4e91 | -12.4274 | -58.484 | 2026-06-12 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| bd820c6d-cef4-3b5a-b9ca-9afd91397212 | -12.4274 | -58.484 | 2026-06-12 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 1a1f0b71-f587-33c0-89e4-32b308628c19 | -7.3474 | -47.0188 | 2026-06-12 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 9cbe7c81-0f84-35fb-949f-16d067ff73e1 | -12.8548 | -44.3625 | 2026-06-12 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 823c5430-2a72-3ccb-82a1-269ccca78bb6 | -12.8548 | -44.3625 | 2026-06-12 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5469e12a-c532-34e5-af53-a3881161ba1d | -12.8741 | -44.3593 | 2026-06-12 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| da0dbd1d-6520-38d7-b433-f87a455bde98 | -7.3474 | -47.0188 | 2026-06-12 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0b71b4e1-1511-32bf-9adb-bb4b1b989b7d | -12.4277 | -58.4642 | 2026-06-12 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 53d15658-73ed-3e7c-94b4-cafce79e3b4a | -12.4274 | -58.484 | 2026-06-12 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1773e8e8-2a48-3ca3-9858-89b91987e650 | -12.4277 | -58.4642 | 2026-06-12 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 19842229-d493-34bb-8252-3a713339b043 | -12.4274 | -58.484 | 2026-06-12 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c1f29267-58f6-3db8-ad02-fd6c40b04977 | -12.8548 | -44.3625 | 2026-06-12 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ac617675-c0af-36a8-b0ea-c407a9c5cf7a | -12.4274 | -58.484 | 2026-06-12 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a2c1dda6-be0b-3c3a-8f62-8d96cd0f16f6 | -12.8548 | -44.3625 | 2026-06-12 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a9698b7b-c3a1-3443-8ef0-84088b444c99 | -12.8548 | -44.3625 | 2026-06-12 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| aaf7af5c-71e1-3291-a2e3-c9291966b44e | -10.8189 | -58.0042 | 2026-06-12 01:03:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97a066fb-72e5-34a1-a520-a7f52b6eed74 | -11.0466 | -56.923302 | 2026-06-12 01:03:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 761f69ba-1dbf-3446-b21b-9c9504dcf8bf | -16.595699 | -58.223801 | 2026-06-12 01:03:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8dab013-58ea-3083-bcb4-47a061a9e3f6 | -12.4287 | -58.478802 | 2026-06-12 01:03:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d534676-e8e6-3898-8bd3-c7e5b07d0270 | -10.8209 | -58.0131 | 2026-06-12 01:03:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0853086-2b0b-3d6f-9bf0-670c7bcd0ce2 | -16.605499 | -58.221298 | 2026-06-12 01:03:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a28ef6aa-dfa7-3d66-b8cc-53ca22d4b0a9 | -12.4268 | -58.470699 | 2026-06-12 01:03:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5498711b-4819-3b75-ae8d-04c259604ae8 | -12.425 | -58.462601 | 2026-06-12 01:03:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3634aa1a-3d0c-3135-8c71-5e0c176bbef3 | -12.8548 | -44.3625 | 2026-06-12 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4ff29287-90b6-34bf-97fa-f350d201206e | -12.8548 | -44.3625 | 2026-06-12 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 5daac0c4-cd6e-3a75-ad42-1f7235465719 | -12.4274 | -58.484 | 2026-06-12 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 084a447a-ebfa-3a1c-bf20-7da82508aa49 | -7.3284 | -47.0425 | 2026-06-12 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 7d9eb97f-13e4-358d-971a-d02b27663c3e | -12.4274 | -58.484 | 2026-06-12 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b20fdc76-2f64-3277-918a-fd1a8b113d37 | -12.4274 | -58.484 | 2026-06-12 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 3d18047f-7c56-3919-9b57-69336f6de4e3 | -12.8741 | -44.3593 | 2026-06-12 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| daa6e918-8308-3abd-b3b5-4dfb6fbdaba5 | -12.8548 | -44.3625 | 2026-06-12 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f7a90a70-cd67-3d25-93bf-ada031e57c65 | -12.4274 | -58.484 | 2026-06-12 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a3604e36-1157-31f1-9a2d-9fa4bdafe453 | -12.4274 | -58.484 | 2026-06-12 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8f72b9f4-22f2-3e70-872e-a537d80a7af3 | -12.8548 | -44.3625 | 2026-06-12 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 33b3c63e-497d-309e-8a29-972090ceb21f | -12.8548 | -44.3625 | 2026-06-12 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| f7279a80-deed-3dec-a195-c3a44f1454ed | -12.8548 | -44.3625 | 2026-06-12 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 691c0eaa-f20a-3c14-9312-b72689753645 | -12.8741 | -44.3593 | 2026-06-12 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 59033066-6452-38d7-8d10-8ae4df3ce362 | -12.8548 | -44.3625 | 2026-06-12 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| fe2955c0-e99c-3c41-b87c-c4aa7b177a09 | -9.5156 | -40.3061 | 2026-06-12 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 497a39ec-b086-397b-a7c9-0c7c1cc2856c | -12.8548 | -44.3625 | 2026-06-12 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 0ec170b0-4ece-3d67-975d-cf0a003a8583 | -12.4274 | -58.484 | 2026-06-12 03:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e5bf5503-c88d-3b97-bc7d-a7f6d62eec07 | -12.4274 | -58.484 | 2026-06-12 03:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 106af8e8-17e1-36d2-bb95-35178967c048 | -12.8548 | -44.3625 | 2026-06-12 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9f7b2d9f-20af-36b8-becd-6e060cb63e39 | -8.4495 | -36.23175 | 2026-06-12 03:17:00 | NOAA-21 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ebb4a320-4099-32ff-8fb0-ca1195986eaf | -8.44932 | -36.23305 | 2026-06-12 03:17:00 | NOAA-21 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a52ecbba-1f40-311d-a0af-586b2f41d784 | -15.84177 | -41.90063 | 2026-06-12 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c510791c-8cca-36b9-8ac1-4f302f649897 | -15.83915 | -41.99868 | 2026-06-12 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca79e2a6-3e66-3b44-978a-bda3877aba05 | -15.84192 | -41.90225 | 2026-06-12 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62137073-1a0d-39df-9d2c-0ff4131a566c | -19.46105 | -39.83892 | 2026-06-12 03:19:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e78e00f3-202b-376a-8d85-c31c4ffd6947 | -12.85544 | -44.36976 | 2026-06-12 03:19:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 18d2cd06-75d0-36b0-9cc3-ab37eb6674ff | -14.07851 | -39.50062 | 2026-06-12 03:19:00 | NOAA-21 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c3a8b3d-efa2-3979-a1a1-fbe9da68d218 | -15.06975 | -41.98421 | 2026-06-12 03:19:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8c883b53-cec1-351a-8f0d-a84b665b050c | -15.83607 | -41.89893 | 2026-06-12 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 963860ec-2fa4-3f7c-999d-a3cc76e1302e | -13.84664 | -41.41034 | 2026-06-12 03:19:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 956d4f9b-9541-3d50-afef-ed9878cbc0ee | -15.07073 | -41.97958 | 2026-06-12 03:19:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 89f45020-da04-32b6-a055-30dbb4e9900e | -15.83824 | -42.00299 | 2026-06-12 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f2512674-a16c-3b71-ada6-c36333b37456 | -15.84849 | -39.03242 | 2026-06-12 03:19:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a2ea1aa-5431-34e4-8f79-9657b182dfc9 | -15.07353 | -41.97963 | 2026-06-12 03:19:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b1532363-3a92-3227-a061-93f92c7aa53a | -15.84959 | -39.0267 | 2026-06-12 03:19:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 02826fbc-c65a-33b8-b1f3-952b9aa47700 | -15.84278 | -41.89809 | 2026-06-12 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 302647ef-7d0b-3beb-b58e-f028586180b8 | -12.86401 | -44.36427 | 2026-06-12 03:19:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2ded977f-dc2a-35bd-8d05-a43c15efffd6 | -12.86248 | -44.37132 | 2026-06-12 03:19:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| f709d179-e67b-3525-8bb7-9f58fb98bf05 | -14.07274 | -39.5027 | 2026-06-12 03:19:00 | NOAA-21 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 840d842e-b293-3cab-82a0-1917a08a8532 | -15.07259 | -41.98425 | 2026-06-12 03:19:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 82c36158-b1c9-35d7-9bb9-721b624710d5 | -12.85698 | -44.36268 | 2026-06-12 03:19:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e2b67503-8ebb-3d7e-bad4-22efb9403852 | -15.83621 | -41.90054 | 2026-06-12 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ca7ab52-f9e0-3935-af75-63aa362caec6 | -12.4274 | -58.484 | 2026-06-12 03:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 7e9d1d9f-8f5b-3226-9d83-13ffa0a39a6a | -12.8548 | -44.3625 | 2026-06-12 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| a5d7488b-a899-3d9f-9eed-3e2ec9b43245 | -19.88975 | -40.46236 | 2026-06-12 03:21:00 | NOAA-21 | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1889e3e7-0613-3292-b57d-df4739054aae | -12.8548 | -44.3625 | 2026-06-12 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0b096460-4458-3d6c-98da-952352587093 | -12.8548 | -44.3625 | 2026-06-12 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3b660755-d58a-3d9f-baad-9a1ba588536c | -12.8548 | -44.3625 | 2026-06-12 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 22cd98f3-b171-33af-994f-436bf9ab2657 | -7.35218 | -47.01833 | 2026-06-12 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6da87cf0-c251-38d3-88af-0fd6c866bc7a | -9.20639 | -47.91972 | 2026-06-12 03:51:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59b8b41a-0e62-3399-8e03-00edb2112a67 | -6.56575 | -47.91474 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cf05132-963e-3419-be0f-99e1dd47138c | -5.80004 | -45.1066 | 2026-06-12 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c132e3f5-1506-3d81-b955-5bff7470f7b5 | -10.30215 | -40.72071 | 2026-06-12 03:51:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b53c2e0d-4607-3bcf-8248-dd149448e9b6 | -5.7994 | -45.11025 | 2026-06-12 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a73673a-0a26-3570-9230-e6c05c7ba9f5 | -6.39095 | -44.17778 | 2026-06-12 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ecffa71-f7e0-3e15-84f9-f1e4dceb9181 | -6.39151 | -44.17461 | 2026-06-12 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87850483-f012-30c8-95af-50a0603d02ec | -5.58403 | -43.51105 | 2026-06-12 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d520cf4-a69d-3c07-ab24-196056de848f | -6.72642 | -44.37698 | 2026-06-12 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e20db4f-27bf-304c-8c11-28617453ca14 | -6.1862 | -44.86391 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8a29280-a6b9-3a67-9e71-427c9db4c6bf | -6.44458 | -44.56496 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f8a848c-e521-3f65-b21b-54bc0060363c | -7.64499 | -45.30024 | 2026-06-12 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 311165cb-36ab-3786-82a4-7a1fa36ddc6d | -6.39671 | -44.17554 | 2026-06-12 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8aa5116-e772-3f20-9265-994b659f4396 | -8.45037 | -36.23365 | 2026-06-12 03:51:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d578b79-b9e4-3d30-8b57-9445ba3d21d1 | -9.21824 | -48.5822 | 2026-06-12 03:51:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6994facd-6c3d-3eeb-ac67-cb5c985c05d6 | -6.18682 | -44.8603 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3f06004-8e0d-3ad0-b852-c8038479d402 | -6.44259 | -44.55915 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2da08978-39e2-30d2-a187-6fadd4979726 | -9.75 | -36.86598 | 2026-06-12 03:51:00 | NPP-375D | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
