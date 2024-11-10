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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dde05378-4d2b-3c44-9d4d-fde831b7f127 | -18.87873 | -53.052 | 2024-11-10 04:18:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2097afee-b7cd-34c0-b0e0-38af1753aae8 | -17.29453 | -57.48285 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| d12e50fc-afac-373e-a144-4548b7f5dd25 | -17.6126 | -57.51865 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| aad2d952-15fe-330d-889c-a92786fb98e8 | -17.29142 | -57.497 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 3c1be51b-8eee-3939-bf17-9963fccf0043 | -17.2794 | -57.49421 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 273bab25-9aca-3041-a5d1-5356909c0428 | -17.61754 | -57.52474 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 82b2420d-4956-3bac-befc-fa819695f347 | -17.60558 | -57.52194 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 84784f63-08e0-39b2-a78f-c0d7d475ef6b | -17.60661 | -57.51726 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| e19e47b4-d6f1-3ed0-aad8-0a4514848edd | -17.29038 | -57.50172 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| a0d1f60d-123f-32a0-b96e-506812b5ccf3 | -17.30447 | -57.49507 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2685783d-ee72-3bea-9cef-c795e1261a39 | -17.60765 | -57.51258 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 69f3ef72-979d-3709-bd43-74b35d2f005c | -17.61053 | -57.52805 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.2 |
| 9072ce3b-371e-3af0-aaab-53f516f00990 | -17.62559 | -57.51678 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 8da1c689-d006-347d-a9fc-9f46723851f5 | -17.60247 | -57.53601 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 3dd8db75-7bb7-35d5-ba30-ed90c7e9a1a2 | -15.27139 | -57.68414 | 2024-11-10 04:18:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09edf725-ad4f-3a98-a8d4-31e4dd22b25a | -17.63053 | -57.52286 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| 679da3a3-d72a-3d00-b339-ab795428de02 | -17.28645 | -57.49088 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 35e80819-9e27-3428-aa82-66fd7a3fb9cb | -15.26876 | -57.68466 | 2024-11-10 04:18:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec1815b6-4199-3906-a7a7-75def73a2cec | -17.24702 | -57.49175 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7e53c990-49bc-3f83-a7e8-97f0dc5b5d85 | -17.29743 | -57.49839 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 60e36d6f-8afa-30c4-8d38-2e5494a36613 | -17.61569 | -57.50464 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 21af1b52-7086-3402-b997-d1dfb4db0182 | -15.26509 | -57.68269 | 2024-11-10 04:18:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 660fa423-5eb2-3433-b34e-06493b667f7c | -17.28541 | -57.4956 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 65998a34-00b2-366a-954d-0d5c671cd104 | -17.23998 | -57.49509 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b4d77680-5d49-3624-bb9d-79ebb59d6ada | -17.24203 | -57.4856 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0ab6f54c-fefa-34ae-be87-637565157d02 | -17.60454 | -57.52663 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 01d4371a-0923-3ae0-a654-d28929854142 | -17.24122 | -57.49534 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 2551ee1c-e6ae-35c9-863c-f56e071333cc | -17.23895 | -57.49983 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4ddd91aa-2860-3c7b-93ed-3e6fb006cc1c | -15.26989 | -57.67935 | 2024-11-10 04:18:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c9960699-0a0f-30e1-9955-1ec86c996094 | -17.77604 | -54.93312 | 2024-11-10 04:18:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7f781cb-a7f8-32f7-a1c7-b27156292280 | -17.30344 | -57.49978 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e2cb985e-e722-35ef-b86c-e052f2ebc625 | -17.29846 | -57.49367 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| a2cf1cce-bf82-3a75-8766-fbdeeb12ca7f | -17.63259 | -57.5135 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| e9d1f0bc-db84-3052-89a8-bf4660d03843 | -17.62353 | -57.52614 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| db0bf4b8-6634-381d-bc45-fc9821a0f754 | -17.62456 | -57.52146 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| 67732ca0-9f19-3a45-bd92-556d5ecbb305 | -17.29246 | -57.49228 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 955e9b8d-9646-35d3-a563-5e8b5dcfcd70 | -17.61156 | -57.52334 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 1d3848c2-c626-318f-930b-ab9775fab9e7 | -17.24101 | -57.49035 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 1f252f54-1808-3d14-8ddb-0c932cd3947a | -17.61858 | -57.52005 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 5bafc0ca-f706-3084-ae21-cf188ad2f48e | -17.26137 | -57.49005 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fd459dfe-d5af-3482-b549-b4184bd20f7b | -17.24804 | -57.487 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 15fd79a4-f828-3044-bfd8-e8febb0659c5 | -17.62969 | -57.49812 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1580cda9-6000-3856-bcf8-789aa1a8022f | -17.28437 | -57.50032 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 21427222-710f-3333-a774-f9e3d82b9526 | -17.24439 | -57.48116 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7e2cbdde-9441-3baa-9b62-f5add56ce7b8 | -17.24228 | -57.4906 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 28381738-0382-3fb8-9b69-562e5425ca51 | -16.27574 | -55.32887 | 2024-11-10 04:18:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba516df5-c6e0-3729-a2bf-1bd28dbdefba | -17.77159 | -54.92883 | 2024-11-10 04:18:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06b217e2-f3a4-3040-b8b2-71afc7d113a0 | -17.25904 | -57.49456 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3f6ab780-525c-3936-aa8e-d3af077b62e4 | -17.60846 | -57.53742 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 7806cd2f-848d-3e53-90a0-5dd12178162d | -17.61608 | -57.44609 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 71b0f600-a44b-3ad4-bc42-06c4383aeabc | -17.60868 | -57.50791 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| a81766cb-c177-3293-983e-8b7d7f913923 | -17.62474 | -57.49205 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 09dec9da-1bad-3dc6-bffb-47e3c2b16b9f | -17.60351 | -57.53133 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 77c7ad5a-2216-3ad8-8c34-89adb08c0c70 | -17.61466 | -57.50931 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| ab897370-4496-3920-85a2-adb9dacb3a99 | -8.3781 | -44.1154 | 2024-11-10 04:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 61349db9-9b31-347e-9316-c9b6c232dd3f | -1.5347 | -52.2104 | 2024-11-10 04:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 209209ba-1ee9-3f27-9d70-70b0e926fa42 | -8.3778 | -44.1386 | 2024-11-10 04:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 04f51755-e282-380a-91bc-9f0ca74ee95a | -3.1239 | -50.4358 | 2024-11-10 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 733dc08f-b505-3687-8d1f-2838659fad78 | -3.1238 | -50.4568 | 2024-11-10 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 77875f7b-09c0-36ac-801a-618a1b337d52 | -17.6266 | -57.5281 | 2024-11-10 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 219.7 |
| a6287e05-83a4-3b89-b926-1e6cc766ab84 | -8.3967 | -44.1365 | 2024-11-10 04:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f08da10c-1e49-3fe4-9a86-e94cd8bb70d6 | -17.2933 | -57.4857 | 2024-11-10 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 96270acc-41fa-3660-8aea-c514c2bee845 | -3.525 | -44.0286 | 2024-11-10 04:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 5fe1de72-7ee2-304a-abc9-0a838e50af9e | -12.414 | -64.1472 | 2024-11-10 04:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0a6f70b4-a0d7-34bc-8bfe-26cfeed4daa2 | -2.8803 | -51.4628 | 2024-11-10 04:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| aaefec88-25ff-31b2-8f02-dcece51df160 | -2.9171 | -51.4825 | 2024-11-10 04:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8ee86f74-ac1f-379f-abe7-e3f7c3e6f1fa | -2.0953 | -48.8338 | 2024-11-10 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f3a4aff8-78da-35ee-9732-7858b7f1c18b | -2.9355 | -51.482 | 2024-11-10 04:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 915e665e-7643-3e03-8fb6-aec864eebd64 | -17.627 | -57.5075 | 2024-11-10 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 209.5 |
| d8cc8036-fee6-38c7-bc69-db9647540f29 | -17.6069 | -57.5304 | 2024-11-10 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 308.7 |
| c47323ac-1604-38a6-bc77-9acda1e5d01f | -3.9483 | -48.1724 | 2024-11-10 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 91c830cc-1fe4-3afa-a26a-623b827e5ed9 | -3.9668 | -48.1932 | 2024-11-10 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 12f56887-5c9e-3f67-8724-bdce0bc5f1dc | -2.8802 | -51.4835 | 2024-11-10 04:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5d8e9cb2-45b6-3076-a6d0-756de586cdb5 | -2.931 | -52.7753 | 2024-11-10 04:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| fe89f46a-5295-3625-a478-8bbffdf6dd3c | -2.418 | -46.3024 | 2024-11-10 04:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| b4fbd8d4-6821-3a5a-acc8-5be23fd74375 | -3.1608 | -50.4347 | 2024-11-10 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e1bf8a97-3e05-3845-8bf4-7a4395643cab | -3.9485 | -48.1508 | 2024-11-10 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d4565fc4-2468-39ec-b665-9a5def51da58 | -1.2751 | -53.7164 | 2024-11-10 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 68aac991-de04-34f0-825a-e2127f449de3 | -3.5064 | -44.0294 | 2024-11-10 04:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f008da13-4c83-3491-ad70-f6e9d8e18ee3 | -17.6073 | -57.5099 | 2024-11-10 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 286.9 |
| a0906515-eb6c-3337-a3b7-28af6e16c958 | -12.4141 | -64.1281 | 2024-11-10 04:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6c664758-66ab-3699-ac67-c0be03059ba5 | -8.397 | -44.1133 | 2024-11-10 04:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a17f3077-5efb-3ae7-83d0-1343065429ac | -3.9669 | -48.1716 | 2024-11-10 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| c34a6bef-f92e-300a-8fb9-57f580367ece | -3.1422 | -50.4562 | 2024-11-10 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 555b9ba7-3c25-315e-954d-47fec9530edf | -3.1423 | -50.4352 | 2024-11-10 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 292.9 |
| b07887b8-4e79-393f-8d27-466e3305b900 | -23.90904 | -54.06839 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 87073ac4-5591-315d-80df-8276f5f50eba | -23.4066 | -46.55478 | 2024-11-10 04:21:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d9ac345b-abca-35e5-944e-ae0efea99cf4 | -23.91602 | -54.05607 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 0d9d9676-d6f7-3c77-8c3a-b28b700edcc0 | -23.90294 | -54.07628 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 56886b16-9425-3376-8922-b32811eef3a6 | -21.58871 | -57.16302 | 2024-11-10 04:21:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb516b37-f3e5-3045-99d3-043f4fb55dc6 | -21.75001 | -52.64199 | 2024-11-10 04:21:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6eb5f76-fd03-3e55-b6fa-74ad0d3ead47 | -20.76328 | -46.77053 | 2024-11-10 04:21:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8465e30c-a37b-3278-8c33-e3641f3eb05c | -21.58954 | -57.15932 | 2024-11-10 04:21:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55a87c87-96c3-34a7-a306-f40ea13dc11b | -23.91691 | -54.05163 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9444c094-4c02-3509-ae83-176baacd65da | -23.86493 | -54.05518 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1f89b082-3744-3137-b89b-4f59761e7155 | -23.3396 | -46.77126 | 2024-11-10 04:21:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c1e01bd-8379-3a99-870e-e9fb4d4451ac | -23.89865 | -54.07527 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 59215afb-0dbb-30ec-a4c0-8855b0af9d12 | -22.54128 | -48.81164 | 2024-11-10 04:21:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fca7a44c-6e9a-3faf-be80-5370d5c31481 | -23.91263 | -54.05063 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ccafa5cb-f2dd-3425-8637-47069e55046e | -23.8701 | -54.05173 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |


[Clique aqui para ver as próximas entradas](README55.md)
