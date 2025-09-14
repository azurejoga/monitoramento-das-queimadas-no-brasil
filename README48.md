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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 603a7ed8-f44f-34ad-9f3f-1fd5e1701dae | -15.1794 | -52.31988 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5655917d-dfc2-38d6-94b0-b27c9563dd1b | -14.62269 | -52.03238 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d39ae8c5-73ef-3c0d-be39-143b7f2fb14e | -18.37733 | -48.34046 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 05c0ee8b-d71f-3398-9d9e-40703c3d1304 | -18.01653 | -46.96748 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc03ecb7-81fd-3c68-9c11-bbb4d905ed97 | -16.10652 | -49.94438 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf2bdafd-ed6d-3dfb-909a-4564cb0edb52 | -16.65874 | -49.78746 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c5394c0-f06f-34ff-875e-ced223502452 | -15.91711 | -49.97364 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cad05a6f-9c89-35e4-8aef-536b02653b4d | -15.7134 | -54.36674 | 2025-09-14 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32462e66-58e3-3757-889e-420de0718d4d | -12.96916 | -54.74333 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 077486d2-5483-36be-94f1-7187eb6f89d5 | -13.18229 | -55.62358 | 2025-09-14 04:42:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 987e16b5-da19-3c73-b058-e9e124a38c64 | -12.68103 | -54.6928 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ad1e0cc2-63ed-3e14-a7d0-875977e1acab | -14.75199 | -60.21694 | 2025-09-14 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6b233f1-a553-309d-a2e1-99a4caad6a87 | -14.45975 | -47.30696 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb44bdd9-1baa-36e2-998f-bbe2eb4b124b | -12.94686 | -54.74581 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f15235a-9cd2-36cc-8610-4ab853c4e367 | -17.14312 | -53.89211 | 2025-09-14 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f66d746a-5d15-3336-a549-4e861938eee6 | -12.6649 | -54.67625 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e62d2aa6-f109-36f8-bef0-7c2bca05d2f3 | -13.90521 | -48.30671 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b39b90f-fdd2-3c0a-9cbd-4987dc9ce6bb | -15.15195 | -52.47048 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 072825f6-587d-3c7c-9cac-8a3498f9ba19 | -12.70302 | -54.7197 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6a7693dc-b259-381f-a107-c08a1787f0c9 | -15.55305 | -54.80181 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fd5420b-814f-310e-8057-fda38006230f | -18.00568 | -46.92388 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 814dfd1f-9055-3278-a9b5-8f4aae69970d | -14.43845 | -43.20108 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d25a134-f067-393e-912c-de5367fcb94c | -17.36267 | -52.90733 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5a11af5-2649-3ebd-b346-1217a305bf2a | -15.42554 | -58.77439 | 2025-09-14 04:42:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e85f013d-e6d1-34d8-9f20-f789238b1391 | -12.70897 | -54.70699 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8c7039f-ac8e-384d-9074-172a08579987 | -16.56996 | -49.20765 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e308e52-34e7-3ea5-bd92-3c12aa2ad96c | -16.90835 | -47.69997 | 2025-09-14 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d6e57d8-477a-317d-8280-a5b3d8a13ae5 | -16.58239 | -49.34653 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6740528-c823-3e37-afe3-93e247431c90 | -12.69274 | -54.7132 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bcada1a0-49e3-3bcb-982a-ad53b8c6dfc6 | -14.17854 | -46.15417 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2667bd9b-70f2-3507-a49f-86afafe80d46 | -17.99371 | -46.95271 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76a06141-d90a-382b-bc16-365ce02d5e8d | -17.17402 | -49.3819 | 2025-09-14 04:42:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3907da0-d258-35d1-a022-50982ebe05db | -12.94392 | -54.7407 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc98c8ad-14b0-3c53-a99c-e1629aadb5b1 | -12.68396 | -54.69785 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 99a98e31-b0c5-30cc-83e3-a746cdfe274f | -15.93468 | -49.97234 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cb621ea-8f77-31c7-a0f9-51370da877c6 | -17.14376 | -53.88831 | 2025-09-14 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70abdc14-a650-33d8-bcb3-bcc84d509741 | -18.46557 | -49.57048 | 2025-09-14 04:42:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 23b2da9b-4bbd-35a4-9a71-42740df68bab | -18.85994 | -46.88486 | 2025-09-14 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f877ec10-16fb-3328-b1e3-6d796daa88c8 | -16.49547 | -55.1508 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4630afa2-4fb4-3b05-a4cc-486251b06f69 | -12.6883 | -54.71695 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c14002d9-6326-3a6d-9b9a-b61fa7f61abb | -12.66274 | -54.66678 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83f21682-56f9-3e7b-bb7e-5920833cc089 | -12.67442 | -54.68708 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cf79c183-becf-3154-a3c7-a3874338eb9f | -14.4335 | -43.20043 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 11dac5f0-a977-3ff3-93ad-4b32b4af03ca | -18.98912 | -44.23194 | 2025-09-14 04:42:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02a7022b-7c38-3260-81d4-7050fa609c37 | -15.76296 | -52.22373 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63d227ce-01d3-34a3-95f4-c52537ed6bde | -13.87435 | -48.29315 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c3d5198-af5a-31e7-ab81-5114ed486aaa | -17.38747 | -52.92285 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ce2a61e-c94a-334e-bb1f-3bd720a9ea6a | -17.99869 | -46.94607 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70ede8d6-74d8-32a4-844c-cfc01292f279 | -12.67735 | -54.69215 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5bf79c5f-4f41-3521-aef5-3a912b012eab | -15.85993 | -51.84773 | 2025-09-14 04:42:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abff0dec-e3a3-3c7c-8117-4da86fdcee14 | -12.69726 | -54.68657 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 094ff6a3-dfae-319c-b17c-3cbe7d485c1d | -14.39992 | -52.909 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c6de68a-b0cb-32f2-a8ca-cb977caaaaa9 | -17.56516 | -46.50478 | 2025-09-14 04:42:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39d0b0f9-ab10-3347-bff5-226a39373a91 | -15.11698 | -52.47561 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2bc9964-b359-38b7-b879-42e2b200bb38 | -18.58852 | -47.19719 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fad8f50e-9c39-342d-a07b-40ab9b494b7b | -14.20489 | -46.17287 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5a50fad0-4a69-3f9b-bc6b-30180420d643 | -14.99345 | -50.1208 | 2025-09-14 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a76c5fe-185d-3798-9682-bb1bb2417391 | -17.26936 | -46.11135 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c483411f-373b-3705-921c-70d1a2e28b2c | -15.28467 | -53.77295 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbba1b88-e932-3f29-b2eb-45ed1e1692f2 | -12.66566 | -54.67184 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a803cf7e-34df-3d3e-ad82-2dbae988c9c5 | -19.14918 | -44.84332 | 2025-09-14 04:42:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dda1c344-49c5-3046-a68a-c3a835494a8d | -17.39022 | -42.62925 | 2025-09-14 04:42:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b51d03d4-781f-3039-beab-bcd825dd9067 | -17.833 | -50.42331 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec07a424-3002-3199-aabf-2d624219e04b | -17.26018 | -47.24623 | 2025-09-14 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b39cb0dc-fac5-360e-a250-d90bcd62120e | -18.20638 | -42.5746 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0a5da035-2491-3210-8fd1-cd210972beb0 | -15.43153 | -52.91373 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8413d31c-e4ce-3970-a875-035215e77ffa | -14.39649 | -47.34514 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4ed074a-29f6-37db-bc7b-5abb19b70f89 | -12.67074 | -54.68641 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 07eb05a7-6c9b-3a48-87e4-8b4d91ea2608 | -13.8791 | -48.28542 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ef568f6-775f-376e-bb40-5ebbc3542ff7 | -17.94281 | -45.26022 | 2025-09-14 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d30bbd9-e0e2-3d64-859f-39d9969d7501 | -16.36769 | -51.77532 | 2025-09-14 04:42:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7f645f9-204a-39bc-a3f3-c6ddb02f985c | -14.48076 | -47.35052 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5484ae0-83ee-3bc6-b65a-4337e42a2ab3 | -14.19018 | -46.1596 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6938c85-7703-3cc9-8cab-00598dcd17ae | -18.00847 | -46.96611 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8586e67e-17d2-3277-afea-01ff7aee8680 | -12.66923 | -54.69524 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3ca8be88-175e-3b1f-9e67-05290b88eba5 | -15.20576 | -52.49465 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3abb947-7366-38f7-ac29-78ee0f76e824 | -14.76281 | -60.21519 | 2025-09-14 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93ac6602-07bf-3556-bd4b-184b26c848d1 | -13.70491 | -50.8129 | 2025-09-14 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0db47370-14fa-33a3-88c8-d499f5be95f3 | -14.44047 | -43.19688 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59f664ff-1878-3f67-be11-22ab1af28ade | -18.71781 | -51.79286 | 2025-09-14 04:42:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b2b14e8-a8dd-3a83-befc-679550515ad9 | -16.1447 | -49.94975 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2672cb9-fa0a-35b3-a29c-0a557617513b | -17.29452 | -46.11673 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11a7f480-0f15-3312-9589-934bed212db6 | -15.84531 | -47.23463 | 2025-09-14 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebf0b7b4-6773-3a37-9bf2-61efddd5df4f | -16.49268 | -55.12426 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 37ed0e3e-a445-3bee-9bfe-d470e23db65b | -15.19535 | -52.47445 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fd43986-5d03-3315-aa1f-974d28f2d71f | -15.11744 | -52.49404 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e036d51-44f1-3179-a901-63dbe6d72342 | -15.585 | -54.73727 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d48d80d-e6ab-3d62-bf5b-2e56b5d095db | -14.63144 | -46.36457 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 261bad90-f263-3110-b442-d0a0cffd507a | -18.16428 | -49.19946 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7d28cca5-0d96-3688-a332-d3c406d39b93 | -14.61529 | -46.33231 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d30606b-b357-389e-9196-88242cfefd4f | -19.72008 | -45.44299 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3d886b7-f2ec-32df-bcd5-9f555aada9ce | -16.33168 | -51.52711 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86a4fb40-7654-30bf-a439-3540bd7752ad | -14.3874 | -52.9221 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16377b02-722f-3c1d-804b-6f62c97ab9a3 | -14.20134 | -46.16863 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d88084d-26a8-3824-be13-e3987920f2a7 | -15.1981 | -52.47858 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25881b4f-27a8-3731-a60d-67a2cf865c17 | -14.41121 | -52.90339 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a15e24b-f061-30b2-96d3-b76f1a027548 | -12.97207 | -54.74842 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f0cb7ae-1578-3044-975d-714e23a521a4 | -14.60927 | -52.07399 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61de6ea3-0088-302f-a074-8f2cf41bf795 | -14.43552 | -43.19627 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fad22fdf-b875-37b8-8bc4-fb27f74eac8b | -18.64201 | -51.79943 | 2025-09-14 04:42:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README49.md)
