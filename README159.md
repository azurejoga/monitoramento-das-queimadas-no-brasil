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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6576e61d-1928-3a38-ad90-2191de49741d | -10.4238 | -50.7142 | 2024-10-06 10:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 778f865c-c0b6-3f46-b19c-394a2a179e5e | -17.02 | -55.0791 | 2024-10-06 10:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 704b7501-1f3c-3591-8b2e-91a25a40148e | -17.0203 | -55.0581 | 2024-10-06 10:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 2449ff46-382b-309c-908a-22651031a8d1 | -17.1185 | -57.3834 | 2024-10-06 10:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| d977ddac-d2ae-3843-806c-af5a80f47df9 | -20.4327 | -54.6762 | 2024-10-06 10:27:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 00064124-b196-3298-a3fe-a89fa8c400ca | -20.4322 | -54.6978 | 2024-10-06 10:27:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 145.3 |
| ccd66a5d-c7c4-3cd3-8608-364a507fa2d4 | -10.4427 | -50.7123 | 2024-10-06 10:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 741b2f5c-84b8-38c4-8e6d-d1a8b368c32d | -10.4241 | -50.6929 | 2024-10-06 10:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 90080793-b1a8-39ed-81f9-1868b183de10 | -10.4238 | -50.7142 | 2024-10-06 10:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 255.1 |
| 220eafe9-d7ff-3865-9dd5-5c3818ccb048 | -13.8943 | -44.6058 | 2024-10-06 10:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4cf518c0-ffcb-34a1-a6d7-1ffe9901c6ec | -17.0203 | -55.0581 | 2024-10-06 10:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 3e90f1e6-33dd-3477-be99-3d2cee24495e | -17.02 | -55.0791 | 2024-10-06 10:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| b2f23a7a-aaf0-3291-b414-eea0f2be4e69 | -17.1185 | -57.3834 | 2024-10-06 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 0aa2ff79-4ac5-3471-befc-f921f9e52762 | -20.4327 | -54.6762 | 2024-10-06 10:37:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 44cdca4c-6221-3b40-84b6-dbaa2963b66f | -20.4322 | -54.6978 | 2024-10-06 10:37:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 158.7 |
| bb5f0c4a-98df-3b76-84c7-d8be8e7f332b | -10.4238 | -50.7142 | 2024-10-06 10:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 238.8 |
| a9824b3b-cb40-33ae-82e6-c734311576f5 | -10.4241 | -50.6929 | 2024-10-06 10:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| d4081e39-053f-3e60-8db9-cd4d5d51abe3 | -10.4427 | -50.7123 | 2024-10-06 10:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| cfafe1ce-a5b0-31eb-a4f6-6aec031d8523 | -13.8943 | -44.6058 | 2024-10-06 10:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| a6235d19-2088-34cf-bf9a-b2a9220660c1 | -17.1185 | -57.3834 | 2024-10-06 10:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 4c22155a-213f-3572-ac6f-cb597029367f | -18.659 | -57.2552 | 2024-10-06 10:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 0ea71178-e359-311e-931c-575066862a56 | -10.4235 | -50.7355 | 2024-10-06 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 68441556-b4b7-376d-b965-41786b8ca00a | -10.4238 | -50.7142 | 2024-10-06 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 273.8 |
| c6297492-d744-3fd5-ad9e-e5033230df02 | -10.4241 | -50.6929 | 2024-10-06 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 03d5d658-2a98-3381-bfb6-771a28894bb1 | -10.4427 | -50.7123 | 2024-10-06 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 16e0fd68-6502-34d9-8a8f-a1f8f9b192e9 | -17.0905 | -56.6884 | 2024-10-06 10:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 5fd02599-147b-3d81-b935-79aaad86b105 | -17.1185 | -57.3834 | 2024-10-06 10:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| d779b38d-f6df-3b4b-bf69-c2ce7f594d04 | -20.4322 | -54.6978 | 2024-10-06 10:57:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 21563a2c-00ab-307c-976a-ed87a68e7e0e | -10.4241 | -50.6929 | 2024-10-06 11:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| c5f41ad6-79b2-3bdf-9c7c-af0b4ce26391 | -10.4235 | -50.7355 | 2024-10-06 11:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| fa7cb3e3-1720-37f5-b179-a223b430acec | -10.4427 | -50.7123 | 2024-10-06 11:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 8ff4018e-ba34-3b4a-bf11-14f9c727a34c | -10.4238 | -50.7142 | 2024-10-06 11:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 292.3 |
| 5b545989-d755-3772-a162-1486704766f8 | -17.1185 | -57.3834 | 2024-10-06 11:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 7aa328ee-3718-3a25-a73f-3b8ba7e07ed6 | -17.8125 | -53.7645 | 2024-10-06 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5a8e2c4c-5126-39ed-a97b-d29ab8edf1bc | -17.8319 | -53.7829 | 2024-10-06 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 5a4679a5-d449-3ccf-9dc0-cb8a3ea38e17 | -17.8323 | -53.7616 | 2024-10-06 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| afd6ca96-e880-3106-be62-7f4465c2ad85 | -17.812 | -53.7859 | 2024-10-06 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| bdee4291-e2d3-343e-bae9-ffb20ddd1759 | -10.4235 | -50.7355 | 2024-10-06 11:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| fc780378-644f-359c-a37e-2d6d40419afe | -10.4241 | -50.6929 | 2024-10-06 11:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2db06f30-67eb-39fc-884d-7467543dfbad | -10.4238 | -50.7142 | 2024-10-06 11:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 69338085-aefe-3549-9df1-bcbaf4080e9f | -10.443 | -50.691 | 2024-10-06 11:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ce544fd8-0d6b-36db-bfb9-22c73cc9b927 | -10.4427 | -50.7123 | 2024-10-06 11:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 176.6 |
| ff068f08-bb3f-33b2-86cd-1cd5ae1dfdfc | -17.1185 | -57.3834 | 2024-10-06 11:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 174.7 |
| 2d20cc33-78dd-3f74-b463-ad32920acbed | -17.8323 | -53.7616 | 2024-10-06 11:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 77cb1b63-b518-324f-9fdb-ca247ab15668 | -17.8319 | -53.7829 | 2024-10-06 11:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 4a17a667-84be-361c-b74b-da262caeafa7 | -10.443 | -50.691 | 2024-10-06 11:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 57d30004-e8b4-3a19-af5e-81880d712adc | -10.4238 | -50.7142 | 2024-10-06 11:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 288.7 |
| a8e0343d-2aa8-30dc-af6c-587ccdb76e45 | -10.4241 | -50.6929 | 2024-10-06 11:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| c892859c-1c93-3ddf-92a8-b0a1588a07e7 | -10.4427 | -50.7123 | 2024-10-06 11:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 193.6 |
| da53d457-1ee6-3e88-858e-4e5daf680b4e | -10.4235 | -50.7355 | 2024-10-06 11:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 43ea99c8-6d40-3039-9590-5eeaf3d0a53b | -10.4049 | -50.7161 | 2024-10-06 11:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| e366af9c-a913-3f7e-bc23-612adf8fc377 | -12.42 | -47.0453 | 2024-10-06 11:26:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 2188c8af-2e8c-3de8-8a6e-13690a6ebed5 | -18.659 | -57.2552 | 2024-10-06 11:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.9 |
| e0979087-6feb-3403-a60f-90bfb182cfeb | -10.443 | -50.691 | 2024-10-06 11:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 2b801e12-fe0a-3ed3-8c37-f6849c465389 | -10.4238 | -50.7142 | 2024-10-06 11:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 321.3 |
| 02e7fb39-3f21-3ded-ab03-9674c90cd5d5 | -10.4241 | -50.6929 | 2024-10-06 11:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 6bb66af2-008f-3794-b2f4-862a85bdd839 | -10.4235 | -50.7355 | 2024-10-06 11:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 0dc80382-0440-347f-9b8e-7b62042ebb3f | -12.42 | -47.0453 | 2024-10-06 11:36:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a1e453af-13a0-3a94-9408-17cd301c0282 | -17.812 | -53.7859 | 2024-10-06 11:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6e93d142-13d6-31be-9640-7bc511ab09ca | -17.8319 | -53.7829 | 2024-10-06 11:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 014462b3-13ac-3d54-812b-38c102add0fb | -17.8125 | -53.7645 | 2024-10-06 11:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e2b42212-5640-3416-8db3-d090c09bd7d7 | -18.659 | -57.2552 | 2024-10-06 11:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 4762152e-7cb5-3dd0-b227-713976da4afe | -18.33102 | -41.45574 | 2024-10-06 11:42:00 | TERRA_M-M | PESCADOR | MINAS GERAIS | Brasil | 3150000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| 9915dc23-a057-3e5a-9775-1dd01503fd95 | -18.33706 | -41.4341 | 2024-10-06 11:42:00 | TERRA_M-M | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| d6822695-4902-34ec-acdb-2bd2899d7142 | -10.4238 | -50.7142 | 2024-10-06 11:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 333.1 |
| 0a380644-543e-31da-8b1a-de4ed645f928 | -10.4241 | -50.6929 | 2024-10-06 11:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| af4ce2ee-de3d-3bf0-b09b-d6629dbd65f1 | -10.4427 | -50.7123 | 2024-10-06 11:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 0ae395e2-17bc-397f-81f4-7b17e4297f97 | -10.4235 | -50.7355 | 2024-10-06 11:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| bd9261ee-6842-3d7b-b172-d2f221941db2 | -12.2543 | -45.5937 | 2024-10-06 11:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| c1228e28-1b16-3fbf-a5c3-ee3b50dcc3dc | -12.42 | -47.0453 | 2024-10-06 11:46:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| ff9ba0ef-0880-336c-b3c2-4506d97f9269 | -12.5066 | -47.5705 | 2024-10-06 11:46:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5ba911c2-2fb9-34f3-9d7d-be7ed836c11e | -13.8943 | -44.6058 | 2024-10-06 11:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 10cbae27-a179-3d9d-8d22-6b42a02c0011 | -18.659 | -57.2552 | 2024-10-06 11:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 5c266c33-b923-3729-aff3-18f5e513568e | -10.4049 | -50.7161 | 2024-10-06 11:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 64c0ba2a-a4ab-30a8-9c6a-479735857317 | -10.4241 | -50.6929 | 2024-10-06 11:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 9dcb5dc3-7009-3e4e-b58c-4f391155169d | -10.4235 | -50.7355 | 2024-10-06 11:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 6ca6c5d8-ee17-3359-ae13-eb2e69a82263 | -10.4238 | -50.7142 | 2024-10-06 11:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 310.2 |
| a24bfc88-dd50-3b63-94e0-a0de69de4b84 | -10.443 | -50.691 | 2024-10-06 11:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| f6d1cf1c-c2ca-38dc-9503-382130704e19 | -11.2239 | -46.5796 | 2024-10-06 11:56:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e822e87a-f9d2-3d59-99fd-a7b40813142b | -11.4238 | -47.1815 | 2024-10-06 11:56:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 9cb3c270-6437-3987-8386-895f4e42c833 | -12.2735 | -45.5908 | 2024-10-06 11:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| edd9fa39-677b-3a16-a1a5-adb8f02270b2 | -12.2543 | -45.5937 | 2024-10-06 11:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 6d28e0c8-706a-3327-8a80-ca5893c6e9d8 | -12.4689 | -47.5312 | 2024-10-06 11:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7088d26e-56ff-3bc2-b77d-ee61a75e8de4 | -12.42 | -47.0453 | 2024-10-06 11:56:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 61082189-bd21-340c-8fc0-e4b84a3e1e73 | -12.5066 | -47.5705 | 2024-10-06 11:56:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 70c0bd4f-a893-3156-8ce2-34d358f8639c | -13.8943 | -44.6058 | 2024-10-06 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 62a6f5ee-ca09-3474-a5f8-88b1860a1e6c | -13.8749 | -44.6093 | 2024-10-06 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 60e47f79-0a3e-3c9c-b168-80d5996ade0f | -14.0883 | -45.5274 | 2024-10-06 11:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ba46d0b2-6aa1-30d3-993a-b529f898f6c6 | -15.1635 | -48.0336 | 2024-10-06 11:56:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 156.5 |
| ed401dcd-99cb-3d7c-8bc6-9ade4a317cac | -18.659 | -57.2552 | 2024-10-06 11:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 415771aa-7f0b-33e5-ba04-4d24724c57f8 | -10.4241 | -50.6929 | 2024-10-06 12:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 98bfa495-5371-33e9-8bce-d21d7ee109d6 | -10.4238 | -50.7142 | 2024-10-06 12:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 376.2 |
| d30ac404-e4d6-3c51-b60b-91d67f78f8e8 | -10.4235 | -50.7355 | 2024-10-06 12:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 43dd759e-026b-3f17-ace1-194af451ef45 | -11.3158 | -46.7924 | 2024-10-06 12:06:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| c538dc19-e0b2-399d-8444-798cbb9808af | -12.2543 | -45.5937 | 2024-10-06 12:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| df06d6b5-4b41-3fe8-a957-328faf53f9bb | -12.5093 | -45.3017 | 2024-10-06 12:06:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 85d5ee54-b407-3798-9f46-48764902cd60 | -12.4874 | -47.5732 | 2024-10-06 12:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 91e23299-6e71-3309-a039-642fba859277 | -12.42 | -47.0453 | 2024-10-06 12:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| b34c15cc-83d6-33f0-89ef-9a7cbc54e50d | -12.4497 | -47.5339 | 2024-10-06 12:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 08f4f26e-154c-331c-bb21-8c78e79c9f8c | -12.5066 | -47.5705 | 2024-10-06 12:06:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.5 |


[Clique aqui para ver as próximas entradas](README160.md)
