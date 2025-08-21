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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83839852-a459-3e7c-9146-5da3ade906b8 | -5.4073 | -42.36295 | 2025-08-21 03:47:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ae08af94-3976-3f92-9025-8c861b5cd65d | -3.87333 | -40.45769 | 2025-08-21 03:47:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8a164270-4224-35b8-ad8c-da0f76321caa | -3.7035 | -40.3547 | 2025-08-21 03:47:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 74eeece9-d437-3070-a0d1-948fd866643f | -3.98691 | -42.50904 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e2ce0a1-c751-38b8-af24-4757cc879481 | -4.86665 | -42.53959 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b04d3661-3f68-362c-bbf0-97ffdd03f525 | -2.91212 | -48.30362 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fb316daa-d5e3-3725-aaf4-40a4daccbf6c | -5.24293 | -37.69563 | 2025-08-21 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ceaae9d-20bd-3de3-a13b-b4b8a404ad46 | -6.01251 | -42.8191 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f649a454-037f-3b5f-9938-efa5c0fb9b5d | -3.0409 | -49.43964 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 989c92a5-244f-3fff-b7fd-184eb2203ffb | -5.87756 | -42.41198 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 21456a02-7529-32e9-bf5e-5e0d332e15a5 | -3.81841 | -41.55864 | 2025-08-21 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5df432f8-84ac-3116-bbc9-717de9a2f536 | -5.98326 | -42.8455 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0873ebe-2428-371a-af8f-e8ebe5f6e583 | -6.16471 | -42.71807 | 2025-08-21 03:47:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9a97584-4b85-385c-8a62-c3fd2f89695a | -2.90726 | -48.25344 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7107db05-fb93-3ac9-98bd-aea4a595392b | -3.81783 | -41.56225 | 2025-08-21 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 23b072c0-16ba-309b-a126-647e47528a11 | -6.01767 | -44.35369 | 2025-08-21 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1716dfa7-36f5-3026-b158-72c8a392510c | -6.07266 | -44.1446 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0527878d-960f-3768-b455-ec02fbe77b47 | -4.39222 | -41.90741 | 2025-08-21 03:47:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd8554fb-97d2-391f-bbc9-782d6ab4caf1 | -5.2278 | -37.31739 | 2025-08-21 03:47:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 48fce315-8b3e-395c-97bf-6b01e2d0d22c | -6.26744 | -43.71671 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eab6783-81b8-30b4-a52f-34500f6c5440 | -6.46378 | -35.16701 | 2025-08-21 03:47:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ad08392-89c7-3834-a319-5a77fefeb708 | -4.6503 | -43.12365 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed06180c-d1fa-33ad-84e3-8dac32a14c00 | -5.6449 | -43.7204 | 2025-08-21 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c69844a9-be5d-31ec-a625-272030253dde | -3.98055 | -43.24851 | 2025-08-21 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3adbf59e-b283-36f4-9c3f-145a0ea9eaab | -4.65358 | -41.40758 | 2025-08-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 18cb895d-4d87-38c1-8d53-5d3a6ecd8977 | -5.98396 | -42.8413 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 14641efe-e17b-39ee-856e-96b369be2a80 | -4.17293 | -42.02752 | 2025-08-21 03:47:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d2d2afd4-a21e-32c8-9896-d114c9974e2a | -4.7831 | -44.91927 | 2025-08-21 03:47:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cab619db-cada-3ca2-9f5f-cee180c3ab23 | -5.99734 | -42.81355 | 2025-08-21 03:47:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11049101-81d4-34c3-ba2d-88b88a27af71 | -5.99369 | -42.80903 | 2025-08-21 03:47:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d88a389c-b227-3316-8699-dca6a18c32f2 | -4.87395 | -42.54091 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9dcf87b7-6812-323f-8106-ed0e683dc04c | -2.44452 | -47.33038 | 2025-08-21 03:47:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a731852-4ea0-38a1-b33b-f191587bd311 | -4.72346 | -38.39846 | 2025-08-21 03:47:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e133d1d-d422-3085-b667-c01e48089096 | -5.40666 | -42.36688 | 2025-08-21 03:47:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 675d4514-dfbb-3299-a71a-3dbad78337d3 | -6.26583 | -43.72627 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8563c75-33ed-3d00-b11a-f91264647052 | -3.98624 | -42.51317 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43ede535-985a-3a17-8c08-a07d4995d0a5 | -6.00748 | -42.84844 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e0fa21a8-b8f9-3609-80be-1916003bfefc | -4.64583 | -43.12292 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20e9dff6-0aa6-30f7-b387-91fd71ecc636 | -3.35489 | -42.87226 | 2025-08-21 03:47:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82c219ea-6dce-324e-8b14-bbafc2c04377 | -3.81898 | -41.55505 | 2025-08-21 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cca98432-db49-3a49-8de2-192e9d97ad55 | -3.03513 | -49.43208 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6902c5f2-4aea-35de-b85a-3d05a052895f | -3.99557 | -42.51044 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4c297880-8900-39ee-850f-647480c25bf6 | -5.83888 | -38.35997 | 2025-08-21 03:47:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d4e8067c-ef70-3a23-9f4a-ca16a6e1088d | -5.44135 | -45.0999 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4bdeba1e-97c3-374e-b6bf-0f6bae197d98 | -2.9186 | -48.30464 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8570611e-a177-34c5-99a9-04050009218d | -6.20303 | -43.56371 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31544351-cbe2-3ee0-a325-815b1d0b7cc5 | -4.86968 | -42.54015 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 712a2102-3f37-36b2-ad7c-3ff715505a3d | -5.79078 | -45.0755 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a246ef44-5d38-365b-9b6f-cbb8ce25a903 | -5.99305 | -42.81289 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b61a98a-1dd6-39a0-ae7b-45d31e74dc66 | -3.83178 | -47.73451 | 2025-08-21 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c88379b2-0334-38a3-b1aa-0cc3130483cd | -5.67178 | -43.51064 | 2025-08-21 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4556364c-d4c1-3c95-9d3d-8fedb5e16125 | -5.77703 | -43.61102 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 095198de-a065-3e93-b6f6-db0cbc62c667 | -6.06375 | -44.11211 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d893d6a-beb9-3f03-a792-1adc8c88713b | -5.74647 | -42.75262 | 2025-08-21 03:47:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18fae487-d379-3056-95fd-f8735ca3cba1 | -3.98511 | -43.24924 | 2025-08-21 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ea9ee1d-1b49-342e-a53e-d23e8e25296e | -6.2175 | -43.33945 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd7c4d65-87d4-3e71-94ec-705b2677a160 | -2.39058 | -47.66044 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb64ec10-ceb1-3d8d-9ce6-4c935491d98b | -6.46662 | -35.1712 | 2025-08-21 03:47:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fdb97ff3-50e2-34a9-93e7-3599b5b25272 | -5.98809 | -42.81627 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5bce8e4f-09f4-3ea6-ace1-1520b0833755 | -4.01612 | -49.50423 | 2025-08-21 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bafacbfd-d6e5-3e14-98d5-2c9598018360 | -4.64958 | -43.12809 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 04278d71-f7d0-3c1f-90a0-313e1dfffed6 | -6.00161 | -42.81434 | 2025-08-21 03:47:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1660671f-43fc-35e6-82d1-e744747bf0a1 | -5.95802 | -44.15393 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9d80b1f-a556-36b8-92a3-eb6f88656c52 | -7.04933 | -35.05313 | 2025-08-21 03:47:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a53c8e91-3c44-3240-9c44-4fe10bade61c | -6.00903 | -42.84964 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4c42a85a-4c6d-3ed0-acce-6b666d4d4ac5 | -3.04027 | -49.44279 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb21816e-2440-3f47-bf5d-8bf1b400e085 | -5.95973 | -44.14382 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fcce54e-ef4f-3189-8cc9-242310f3be8b | -3.73899 | -48.9329 | 2025-08-21 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2300ed1b-86b8-3a7f-a1d4-48a1df0ab59e | -4.311 | -48.09923 | 2025-08-21 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bde8e723-256d-303b-9b83-1b50d623dd9e | -4.86112 | -42.53875 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4adab70c-a84d-3b17-bd7f-cc5ea4c3f4b0 | -6.0168 | -44.35875 | 2025-08-21 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8f60061-ead8-3b9f-a96d-123533ac60a4 | -6.21823 | -43.33514 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2d95b50-bdf9-3b7e-b0a9-77236fa65fa2 | -5.41087 | -42.36749 | 2025-08-21 03:47:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a02d439-71ba-3ebb-834e-c8eaddb541e7 | -3.67248 | -40.35446 | 2025-08-21 03:47:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 28019446-98fe-3595-b521-a2902c999ef8 | -4.71372 | -47.22102 | 2025-08-21 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b01e2a8-b937-399f-b051-ee87fea94fdb | -3.99124 | -42.50975 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0009adeb-ac31-31a9-a684-167ae368e168 | -6.02036 | -42.82468 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eec38356-daa4-3e47-b4f1-aeb7330ad4eb | -6.07315 | -44.11334 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa38298b-73de-35a4-a747-688f01534bf3 | -6.02393 | -42.82958 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 22858325-c97c-32a6-9547-31311dcefc7b | -2.91948 | -48.29932 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ef9e76e9-2b09-3f5f-a22b-ebab95733b0e | -4.2931 | -48.2776 | 2025-08-21 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c862db-a3a3-31f6-9585-769cbe1d3391 | -6.26134 | -43.72529 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64afa1a9-faa7-3b19-8d4e-bca609528955 | -6.21013 | -43.32926 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cec3afc-1e23-399d-962d-6c78f22d1b20 | -5.16437 | -37.98116 | 2025-08-21 03:47:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 56c6f1cd-12c7-37b2-8e86-f56c7bef001b | -4.86471 | -42.54352 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa22b216-9efa-3391-bd86-533a04a0c64e | -3.81726 | -41.56586 | 2025-08-21 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5b099905-2dfc-3565-8c4d-ef298f5594d5 | -3.98257 | -42.50836 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 060ea23b-adcd-3030-b5e6-0a59b0585a54 | -4.866 | -42.54367 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aae17f32-a3d2-35e2-bd87-ffaf52a616cd | -3.94071 | -40.89566 | 2025-08-21 03:47:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66d18850-f241-3cd6-9bd6-a31ea83cd5c2 | -5.12239 | -43.21243 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f037eb29-d805-394f-8892-5d4de82fbb06 | -6.27193 | -43.71768 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ff7cd57-12ea-3373-b698-5112b3e50cb6 | -3.94554 | -41.82819 | 2025-08-21 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b76caaf0-7a88-3572-bb89-b3ba3d3043be | -6.82009 | -39.89234 | 2025-08-21 03:47:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c2dd4223-ffb2-3903-b40a-ccdcf5cd192c | -4.64117 | -41.40851 | 2025-08-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a9eb35db-f2a4-314f-ae1b-626371d9a44a | -2.91268 | -48.30303 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 050e0780-cec9-35a6-8a4a-eb0fb911933a | -5.10829 | -43.16027 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c01e3c57-aa58-3213-8ebf-c3adf8aaa948 | -5.68196 | -43.86376 | 2025-08-21 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4868751-6667-3392-9783-29150123a33c | -6.0168 | -42.81976 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1a63212-05e0-33ce-8a52-07bfd6308eb3 | -3.94043 | -40.89312 | 2025-08-21 03:47:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bee40c4-7950-3e88-bd0b-a8f50ffe02a4 | -3.51753 | -39.29927 | 2025-08-21 03:47:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README12.md)
