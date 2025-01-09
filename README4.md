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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd851132-b908-3546-8d9e-ada1faabd305 | -3.04872 | -40.08423 | 2025-01-09 04:14:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 687c26ff-c316-3305-a603-ddf2f6db1133 | -10.45882 | -36.87486 | 2025-01-09 04:14:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d8515226-963d-35ea-8704-e33770fb79f9 | -2.99412 | -40.38861 | 2025-01-09 04:14:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 347063ac-7213-317c-807b-ec556bfea6e4 | -5.00538 | -37.60293 | 2025-01-09 04:14:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2d05aac1-95f4-329f-b59c-a7f91a445a16 | -9.87027 | -36.27435 | 2025-01-09 04:14:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9ffdd5be-51de-37fb-beec-04aae51bd24b | -15.35555 | -39.12803 | 2025-01-09 04:16:00 | NPP-375D | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fe582566-70eb-30e9-a91d-d18416789983 | -15.355 | -39.13226 | 2025-01-09 04:16:00 | NPP-375D | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d245aa0-2392-375c-a6a2-3968c641221d | -11.48368 | -37.79981 | 2025-01-09 04:16:00 | NPP-375D | CRISTINÁPOLIS | SERGIPE | Brasil | 2801702 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 78a4c09e-8947-39b7-9ad4-14463a5b62da | -15.43886 | -39.79772 | 2025-01-09 04:16:00 | NPP-375D | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fa52f7a9-e5f1-370f-89b2-40ea3dd5a658 | -11.12884 | -38.17082 | 2025-01-09 04:16:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb2515ca-dcef-343c-a40d-e8f431afdca0 | -19.83515 | -53.92226 | 2025-01-09 04:18:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4663d5ee-e7b9-337e-8c31-2dc121c694f1 | -22.95494 | -47.08152 | 2025-01-09 04:18:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c7f77742-ecd1-3b61-ae0f-2e5ffff947ea | -20.76495 | -46.76831 | 2025-01-09 04:18:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e161fbd8-14e4-363a-8f8d-ce40d9691b04 | -22.25452 | -50.0393 | 2025-01-09 04:18:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c419320-4462-33af-a526-3372f4000f57 | -22.54071 | -48.81376 | 2025-01-09 04:18:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9764b7c7-9747-37e3-b9eb-2de641a869c6 | -21.10718 | -51.2006 | 2025-01-09 04:18:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed7b3caa-5471-3a82-a9c4-f3e77694f329 | -22.02005 | -49.11525 | 2025-01-09 04:18:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1dbd6734-c5cb-32e2-9db1-7084193118a0 | -19.83974 | -53.92339 | 2025-01-09 04:18:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52f9ac20-ce4d-38b9-bcac-116666196e22 | -22.84919 | -49.38358 | 2025-01-09 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aee7c5f-bf49-3bfd-924a-d4cedcbafbd0 | -18.75965 | -55.96136 | 2025-01-09 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 41bd7e07-3da6-3706-a4b9-ad0ff6ab55a6 | -19.56295 | -54.12061 | 2025-01-09 04:18:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1910f918-2d56-39ee-bc48-b175599db659 | -21.11102 | -51.20137 | 2025-01-09 04:18:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d240a1e3-57f6-370d-ad8e-98095ae07884 | -20.30992 | -45.58347 | 2025-01-09 04:18:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb2e55f9-cc10-3ab3-b48e-b064a47d12b1 | -19.3052 | -53.7443 | 2025-01-09 04:20:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 707620d3-19ad-3a46-a1d3-0af5d32894d2 | -30.10612 | -51.61903 | 2025-01-09 04:21:00 | NPP-375D | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| f72777c5-b498-3ed9-8fca-8d2f61e6c289 | -29.49732 | -51.98364 | 2025-01-09 04:21:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 073ea805-1e34-37dd-a81c-e36cac2ed1a0 | -23.98527 | -48.9186 | 2025-01-09 04:21:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1edab9f0-94e6-3883-be29-33c7f2f8629e | -26.87462 | -52.33837 | 2025-01-09 04:21:00 | NPP-375D | XANXERÊ | SANTA CATARINA | Brasil | 4219507 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a20e9b6b-845d-3c6e-afc5-1293cdc63f06 | -23.98189 | -48.91793 | 2025-01-09 04:21:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 721d2ae7-0476-3b5a-b375-0b7630b7e0df | -29.80991 | -51.22593 | 2025-01-09 04:21:00 | NPP-375D | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 917cc577-0866-392b-9e18-1229a1e80e7d | -29.95437 | -51.61778 | 2025-01-09 04:21:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 80df4a2f-54a1-3773-a2f8-a8ebe6edfc97 | -23.32821 | -50.12716 | 2025-01-09 04:21:00 | NPP-375D | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c4e44b16-a975-336c-8ca7-f7b2336b1956 | -21.8833 | -56.11172 | 2025-01-09 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff5581f9-39d4-3966-a7d8-bd495425d9f4 | -27.08864 | -50.50624 | 2025-01-09 04:21:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6b67b021-e92f-38e5-9945-f1c155d4389e | -30.52786 | -53.96129 | 2025-01-09 04:23:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 19c24157-fd68-3c0a-9fcf-d37dcfe62782 | -19.3052 | -53.7443 | 2025-01-09 04:30:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 092d89e4-3944-3c36-a70a-b7b8f7c981c9 | -19.3057 | -53.7227 | 2025-01-09 04:30:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b473127c-c67d-39b6-82ef-9c28dab91caa | 4.52306 | -60.8159 | 2025-01-09 04:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fb25703-85c0-3009-9417-8fb533988af5 | 4.52216 | -60.8092 | 2025-01-09 04:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fe71446-bd77-37e6-be7a-4f294088d8f4 | 2.92779 | -61.11688 | 2025-01-09 04:33:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e51dce41-1b10-3e8f-bccd-8f91f8dc3b28 | 4.51917 | -60.80854 | 2025-01-09 04:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59ae8897-89f6-3620-b0f0-52b35d62922f | 4.52419 | -60.82433 | 2025-01-09 04:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a76f391-3d3f-3053-af0c-0fc15dcf5f6d | 2.92171 | -61.12499 | 2025-01-09 04:33:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb7415f8-83f7-3ee8-a8b3-a7ee8ee5227b | 4.52004 | -60.81469 | 2025-01-09 04:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8ae522c-2bfb-302c-a9b0-5046a4b5efb4 | 4.5212 | -60.82296 | 2025-01-09 04:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cd711a1-cd09-3d12-b1df-2e94bd2eacb9 | -1.32863 | -53.21581 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daa2dc7b-8dab-363c-b4b9-08ca18c5e83e | -1.32751 | -53.22272 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47acb27f-e99d-3d22-9923-4230ce777b7d | -4.33311 | -39.36471 | 2025-01-09 04:36:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49f5213c-fa7b-336e-a962-4091862f2ae6 | -5.42527 | -40.68147 | 2025-01-09 04:36:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4876562-204f-3a35-a41f-c2c537471ff4 | -4.15909 | -42.01685 | 2025-01-09 04:36:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 06d1113b-5d97-3082-9d10-ef756f219529 | -4.163 | -42.02216 | 2025-01-09 04:36:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 611a6051-98d8-3dff-a1c5-4d2f98c2027d | -5.4257 | -40.67839 | 2025-01-09 04:36:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5402dad1-fa35-3167-ae1a-3437fa6924ce | -3.85007 | -41.11864 | 2025-01-09 04:36:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 13f33fbe-f629-372c-b38b-2cefdf1f39ed | -4.84648 | -40.0488 | 2025-01-09 04:36:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 817e552e-d9eb-39fe-930a-44ae80f4faf1 | -3.84732 | -41.1166 | 2025-01-09 04:36:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a93cfa70-1500-3c65-90c4-b852fba6cc81 | -1.3332 | -53.21296 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1d766ca-bdc6-35fe-b834-17bf6b8a9e70 | -4.1584 | -42.02153 | 2025-01-09 04:36:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7eea7a73-a33e-34ef-8337-9d052d3de55a | -1.32807 | -53.21925 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c8315b-39d7-3722-bb96-29dab4d29a6f | -1.33264 | -53.21642 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ad2f898-c3ad-32dc-9847-0726886449ba | -3.85088 | -41.11308 | 2025-01-09 04:36:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 57a112bb-a441-375a-936a-596759d385f3 | -1.33152 | -53.22336 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16deef72-8900-3dff-8c02-0325188b4287 | -1.33208 | -53.21988 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d1317bd-5f66-34cf-b785-1d303733cbea | -1.28935 | -53.09101 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb1f97af-800f-35fd-9f3c-047599867c59 | -1.32919 | -53.21235 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eecdb33c-fcd7-339a-aaec-fa71c13f3f17 | -4.33362 | -39.3611 | 2025-01-09 04:36:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd120995-f4ae-3a74-a70f-aaf9132b7449 | -0.96208 | -47.95293 | 2025-01-09 04:36:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8c15b49-8034-363f-83db-342bb1e1b320 | -1.28855 | -53.09611 | 2025-01-09 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d481aaec-1d10-3ca9-b1b7-363f6fbe0f4e | -10.45704 | -36.87345 | 2025-01-09 04:38:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| f47f4143-7dc0-3aec-ae5a-4059e949ea8d | -7.56411 | -39.01223 | 2025-01-09 04:38:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae5ba3c4-6846-3745-8f83-d686f3af6048 | -7.56807 | -39.01095 | 2025-01-09 04:38:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6f26ce92-a13b-323a-acc5-4fa53b690de7 | -7.5706 | -39.00885 | 2025-01-09 04:38:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 650b127c-c84f-3d43-9628-fd1ac13e4c09 | -7.57005 | -39.01289 | 2025-01-09 04:38:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a8cb25cc-0e7e-32af-b6e8-41106865dcbc | -10.45576 | -36.87469 | 2025-01-09 04:38:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 33edb808-621b-3b37-94e6-30d2e5806ad3 | -7.5686 | -39.00691 | 2025-01-09 04:38:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2f4b67e8-1099-3191-8bb8-914ee6c0d37e | -7.56467 | -39.00817 | 2025-01-09 04:38:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff6c4258-e8fb-35a2-a4ca-bc120511223f | -19.3052 | -53.7443 | 2025-01-09 04:40:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3c3ccbd2-7d11-3724-ac9d-dda717c3b353 | -19.29404 | -53.73484 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 539c45fe-09cf-3a2b-8462-950fa9a7ceeb | -20.23622 | -54.2118 | 2025-01-09 04:40:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55bc2ae2-b6ed-337b-8e3d-6a1f44a91c50 | -19.30349 | -53.74049 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2175ef5b-d4f4-36af-a141-620df1f9fc97 | -19.83519 | -53.92085 | 2025-01-09 04:40:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efe1accc-07ee-37b9-9d07-252c98ea847d | -19.02258 | -57.62432 | 2025-01-09 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e5f94989-b0a0-33e1-b77f-adb247cff752 | -19.02325 | -57.62075 | 2025-01-09 04:40:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5b7bb84b-2b80-36e3-9909-dd0dd01f6dd9 | -19.0215 | -57.62472 | 2025-01-09 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0a57fcce-37c6-3a68-8569-05b6a1d746c7 | -19.30411 | -53.73672 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0ebae629-e3b0-3fb2-8c77-fc6ed6f2ecf6 | -19.56328 | -54.12233 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76891b0a-f2b1-3755-8297-92605d042dcb | -19.29342 | -53.7386 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a007d56a-56fb-35f8-bea4-0e6a76abf69e | -19.29889 | -53.74739 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 735c74f7-e400-3bfb-ba44-11742548f2aa | -19.34451 | -54.17062 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c243014c-10b7-34ae-a776-3036c165bfb4 | -20.47639 | -53.67633 | 2025-01-09 04:40:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02eae1e7-867c-3df1-b0d2-99910bb0f48e | -19.30224 | -53.74802 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df9034fa-eacf-3ec7-b84b-1c94d3287877 | -19.30684 | -53.74112 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7fbc6b8-278d-3a44-9dbe-2c4142c0e161 | -20.76181 | -46.77009 | 2025-01-09 04:40:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0f9808ce-a91c-33d0-9f74-7147a5861e58 | -19.62101 | -54.15259 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac9f3a93-af1b-3951-998a-7b550af58b05 | -19.29678 | -53.73923 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f05893e7-86bb-3d46-af6b-490a2fef0e89 | -19.02216 | -57.62109 | 2025-01-09 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fd44fd76-9443-3e46-ae40-6c7558b91a29 | -20.06095 | -54.89645 | 2025-01-09 04:40:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9257e3ff-574e-3253-8993-b97b31165ae3 | -18.76193 | -55.96108 | 2025-01-09 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 06f8db11-95fa-3f78-870b-cee9db098212 | -19.2974 | -53.73546 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| edccf701-492e-3ef7-a7c6-bf69b2e0be32 | -19.30622 | -53.74489 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adce5786-b93b-3d0f-bc2a-c0aec8397377 | -19.29951 | -53.74362 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |


[Clique aqui para ver as próximas entradas](README5.md)
