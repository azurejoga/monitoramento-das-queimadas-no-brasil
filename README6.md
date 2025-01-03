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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 424f90e3-244a-30c3-81b3-ecbb02feea7f | -30.85881 | -55.52112 | 2025-01-03 04:33:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| dd8e67c2-e094-3fdc-a8df-8cd9e769a622 | -30.93044 | -52.62475 | 2025-01-03 04:33:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| eb72ff58-2810-329c-ba8e-e7c8c918e967 | -31.74832 | -53.33614 | 2025-01-03 04:33:00 | NPP-375D | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 5476bf8b-f4ab-3e4f-b6ac-8f6d28055b7a | -4.25822 | -42.60749 | 2025-01-03 04:48:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f904754c-3c38-3ded-b76a-04248e0119de | -1.25564 | -53.86341 | 2025-01-03 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a3c93e9-0ec3-3ee0-bda1-b68275598d4c | -1.64555 | -46.12957 | 2025-01-03 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2c01432-d299-34fa-97d7-6ce1972f0ad4 | -2.57504 | -51.90647 | 2025-01-03 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1647c066-41f3-3ad7-89fb-d61438ea2c03 | -2.57281 | -51.89907 | 2025-01-03 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfaf4ee6-e1d0-342a-9f97-508c62944bed | -1.72539 | -53.23856 | 2025-01-03 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 607a6b2e-3ac3-3e55-8178-56416060d177 | -4.16033 | -42.0284 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| bd9d9299-0b26-3026-b7c9-809d39096f77 | -1.81301 | -45.91078 | 2025-01-03 04:48:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c50e701b-cc38-3709-bcb9-d40032777762 | -3.9093 | -47.05356 | 2025-01-03 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ace492f2-abe9-301c-aab7-e56eeb35863d | -2.57612 | -51.89959 | 2025-01-03 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cb395f4-e6b0-31d4-8074-a6c7eb3dda46 | -4.16381 | -42.02984 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 531ea26d-a47e-3cd9-976b-d4dcefe6718a | -3.01463 | -41.12881 | 2025-01-03 04:48:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4890a1c7-a300-3afc-a381-3f12f3d6b104 | -2.57319 | -51.83219 | 2025-01-03 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c10fe821-0a28-34de-acd9-6efb7679a1c6 | -1.67035 | -53.96589 | 2025-01-03 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66391019-ac6b-3534-bb19-e5769011a966 | -2.58197 | -53.97769 | 2025-01-03 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62535529-0b62-3305-9dd5-31f411cd7e12 | -1.37519 | -45.86169 | 2025-01-03 04:48:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6b5ff10-920d-3d53-9bc2-453fb922e313 | -3.90615 | -47.20878 | 2025-01-03 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a852bc62-7358-3d55-bd2c-f69bc896362f | -2.29754 | -46.41134 | 2025-01-03 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ced2863-281e-3d84-afe5-73e26c693db3 | -2.57835 | -51.90699 | 2025-01-03 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54405748-8eae-3984-82a5-d219b3a7fb5e | -0.84214 | -53.07945 | 2025-01-03 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eab362c-ef88-3051-9886-532e4c305970 | -3.85809 | -40.45577 | 2025-01-03 04:48:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ad220836-7005-3c2b-b363-306dbbb2a3c3 | -2.30107 | -46.41559 | 2025-01-03 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e088cb8d-4679-3a62-9a09-82c3435e9331 | -2.29697 | -46.41499 | 2025-01-03 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d268ca37-135a-323c-a484-32d83e12d9a9 | -1.71256 | -46.23428 | 2025-01-03 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31ba5ba5-c131-37cf-8f0e-9099526303a9 | -2.35303 | -51.91423 | 2025-01-03 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d0d2551-373d-3bca-940c-c0b2f0869007 | -4.79872 | -43.30619 | 2025-01-03 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 229a6918-c074-3ae5-b64f-b4365c8d6bf4 | -2.22366 | -53.65404 | 2025-01-03 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 147ac55a-b993-3f15-8730-ede950ef8121 | -2.29344 | -46.4107 | 2025-01-03 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a403a92-2e27-3812-9a3f-17abdaa2c8ff | -3.32338 | -46.82911 | 2025-01-03 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53a9fc8c-cbad-3626-b7f5-4ec971061fee | -1.72257 | -53.23439 | 2025-01-03 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd1e8fd2-889c-321a-ad38-6c48477e073f | -1.32891 | -46.65063 | 2025-01-03 04:48:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32d06d5e-c611-3fe7-a3ba-d979f26dd4ee | -1.71801 | -53.24113 | 2025-01-03 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0ff6270-bc36-3aff-be95-973dc2b44e0f | -4.804 | -43.30688 | 2025-01-03 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23ec8fec-9dcf-341b-b400-98033505a7cc | -2.25129 | -53.61278 | 2025-01-03 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ddff07-be35-377d-ab75-966518b72b30 | -4.15979 | -42.03223 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 8defa6e5-c826-3dae-a92b-481e94ddb7cb | -1.61666 | -46.20844 | 2025-01-03 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e702976c-9e46-33e0-a8b8-48bc6ab461d7 | -1.87007 | -54.12304 | 2025-01-03 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 214e8845-2ad9-3b9e-983f-9feaf3821bca | -1.90338 | -53.28419 | 2025-01-03 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c2d600c-1edb-3088-ad07-f8b33ef33922 | -2.30164 | -46.41195 | 2025-01-03 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4a602d7-98f4-3350-af60-717febd5ffc7 | -4.16603 | -42.02916 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a747afa0-82b0-3f71-a3b0-5b21556b6e95 | -2.58165 | -51.9075 | 2025-01-03 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0431c72-07a2-38dc-8e50-a45362dd52d5 | -3.90528 | -47.05295 | 2025-01-03 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1bd1ce6-a11b-3347-b9e2-208094d87c01 | 2.85169 | -60.08255 | 2025-01-03 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4d69882-860c-3fc2-9c6a-91dbcc9f719d | -3.00555 | -46.70501 | 2025-01-03 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c11fb1-70a1-3cc8-89ac-932613f94cb6 | -2.21924 | -53.83803 | 2025-01-03 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd348cc4-a340-3254-b4ac-10eff2762c79 | -1.6365 | -54.27427 | 2025-01-03 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb1b132c-948f-3ed2-980f-5c0c428b3bcc | -1.15798 | -53.77024 | 2025-01-03 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2522baaf-0c9b-318f-871a-38d7fd40cfb4 | -3.86434 | -40.45673 | 2025-01-03 04:48:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e438254-ee11-36e8-9277-f96c5a59bfa8 | -4.09644 | -46.6152 | 2025-01-03 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31bf64ab-7e1d-3132-a666-c1e9556f7359 | -4.40277 | -43.37642 | 2025-01-03 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 327a1f38-5cf3-39f8-a463-99af2743412a | -3.01525 | -41.12451 | 2025-01-03 04:48:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 845a76b0-620f-3f78-99f8-64f01a7f13bb | -1.64498 | -46.13329 | 2025-01-03 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74d3d05-bb01-3409-8c00-b6f495922578 | -2.51467 | -51.92189 | 2025-01-03 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f04788f-21ec-31b0-8e2e-370393e383a5 | -3.86243 | -40.45448 | 2025-01-03 04:48:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 39f0fbe9-996d-3b9a-acb4-f9a47ab39a5d | -3.005 | -46.7086 | 2025-01-03 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e43d8dab-799d-39ee-8f3d-3861902d43d7 | -4.15811 | -42.02911 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5afdc83a-2a98-34f8-85fd-f3e32be6b2db | -1.90803 | -53.30362 | 2025-01-03 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56c7f62b-4a09-3a2b-827b-b27c8174d6a1 | -1.7306 | -46.10072 | 2025-01-03 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6132467d-927c-3d59-ae70-6278ca59f8d7 | -1.71723 | -46.23122 | 2025-01-03 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddab42c2-a6b2-360b-9e2c-2b449b1d616c | -1.72467 | -46.08449 | 2025-01-03 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38f33784-b435-3068-9f4b-d336de291aa4 | -1.72665 | -46.08468 | 2025-01-03 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90ac0651-8ad0-3209-bc2b-3ee2e771825a | -4.16087 | -42.02456 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f042db63-b380-3ecb-a16c-1e6960a01404 | -4.40232 | -43.37954 | 2025-01-03 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54a95500-ee61-3184-8a92-6038ccd96914 | -4.16439 | -42.02601 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 846b9eb7-8b73-35b2-9cbf-d620e0dcd692 | -1.86945 | -54.12695 | 2025-01-03 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7154f319-80d1-3296-ba0e-fdf8c4400860 | -4.4071 | -43.38334 | 2025-01-03 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15ab67de-9470-3d5c-b223-a01d8c6741a3 | -2.51413 | -51.92533 | 2025-01-03 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bdee940-4ac9-3ad4-80b3-8533a9476515 | -4.16324 | -42.03367 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 9971400c-5e50-3547-ab47-fe5a20fe027a | -2.57264 | -51.83563 | 2025-01-03 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac09e841-301b-377b-bc4f-41816fc30b2f | -4.16548 | -42.033 | 2025-01-03 04:48:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 170544b4-78aa-3130-a016-8e4faa7ebc4b | -1.72597 | -53.23492 | 2025-01-03 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dbeab50-8535-3343-aa13-3dc5fa39208f | -4.80446 | -43.30371 | 2025-01-03 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3600421-4680-3bdd-8179-9707568733d7 | -6.12957 | -42.54924 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f03c039-da8a-3827-b4cd-472bc09a7be0 | -6.12393 | -42.54836 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 480f39d2-ebf4-350b-b8a4-166a633661a2 | -3.49166 | -54.74187 | 2025-01-03 04:50:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86fccd46-085d-37b1-b1f6-512cdb286a8d | -5.04788 | -43.62135 | 2025-01-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f92bcd77-05f9-3f65-9cf7-a7932d71d085 | -5.96835 | -44.29424 | 2025-01-03 04:50:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 861347b6-6c5c-391d-80e8-b9381998fa93 | -5.67808 | -45.21491 | 2025-01-03 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff42fdc1-10bc-315e-9187-1de392c315e1 | -6.11884 | -42.54367 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 488ff27f-3b4f-36fd-8a75-dca259652bc3 | -6.12448 | -42.54457 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0fcd109-facf-370f-b2b6-53975f7b3ce4 | -5.92394 | -43.78689 | 2025-01-03 04:50:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cf9fbda-b32e-352b-b4e2-8cd7b9e1708b | -5.62544 | -44.83405 | 2025-01-03 04:50:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8960f22f-d5c3-311c-b436-dda949da5b58 | -6.11829 | -42.54746 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41696b78-5188-3658-9cc2-caafc4e0f7b4 | -6.12134 | -42.54789 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 844f8431-b554-3242-8ab4-9b41b39876ca | -5.0427 | -43.62057 | 2025-01-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25a27502-5225-3c33-afa6-a92e351142e0 | -5.67738 | -45.2198 | 2025-01-03 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4891cf91-5616-37c9-a285-2467622c2d72 | -9.23736 | -60.33881 | 2025-01-03 04:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dc4d727-68b8-341a-8e82-cf8216cd30db | -5.67197 | -45.22419 | 2025-01-03 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7da6015-cdf3-39a6-999b-5c8597ceafc0 | -6.1275 | -42.545 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 660012fe-79a0-3879-8ebc-0841a3dcc0b1 | -9.92447 | -59.9065 | 2025-01-03 04:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de875b83-0a2d-3058-99a4-906f863c4bf7 | -5.62948 | -44.8401 | 2025-01-03 04:50:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 01545a4c-48aa-3f44-ab7e-f670b36b8b44 | -5.63427 | -44.84086 | 2025-01-03 04:50:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31bfb89b-0221-3262-b415-2ee8efb66aa6 | -6.12186 | -42.54409 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ac25f7ad-66ab-3bf7-b5d3-fb1f483865c8 | -5.63503 | -44.83559 | 2025-01-03 04:50:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4f277923-e4a0-37d3-8770-8e02da250307 | -6.13012 | -42.54546 | 2025-01-03 04:50:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 936b5cd6-d172-316d-9ca3-e17cfc62750a | -5.6694 | -45.20877 | 2025-01-03 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bc3b832-95ef-33b6-abef-0ffefaae269c | -5.70461 | -44.96257 | 2025-01-03 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README7.md)
