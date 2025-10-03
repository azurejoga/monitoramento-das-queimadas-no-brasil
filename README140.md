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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb5fdedf-d735-3ece-94df-2cab900896d9 | -12.62338 | -46.95111 | 2025-10-03 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| dfde388e-9909-339e-b0db-ea9d236154c5 | -10.00701 | -50.19835 | 2025-10-03 06:33:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| fde1bdab-d00b-3870-b30d-a25013732144 | -14.66087 | -48.10081 | 2025-10-03 06:35:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 94c56237-46ab-3a94-9635-57f24168814b | -14.57182 | -52.45968 | 2025-10-03 06:35:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ef88a759-3021-3538-9f3e-7a0e93b932ae | -13.15367 | -47.90182 | 2025-10-03 06:35:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 3c9ff15d-e9fa-310b-b79c-10001c1d64fe | -13.14373 | -47.89412 | 2025-10-03 06:35:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 9f4374d7-693b-39d8-a6f4-77f9a1e276e3 | -13.32699 | -47.59241 | 2025-10-03 06:35:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| bc3dcdeb-8739-383f-8429-1ee735fd80f4 | -12.75958 | -50.55025 | 2025-10-03 06:35:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 020d5efd-2e43-388f-a04c-947b5cb7e3b8 | -13.76566 | -47.56342 | 2025-10-03 06:35:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 9fb838b4-836c-3b39-8d9d-050f48bf3b59 | -14.67451 | -48.0788 | 2025-10-03 06:35:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 34947b88-e959-3b86-9ba3-1bfb29a27e79 | -15.59013 | -52.46322 | 2025-10-03 06:35:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| aab3ea11-b465-32f7-a8a9-ea731d50c701 | -13.12827 | -47.89057 | 2025-10-03 06:35:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a1819ba3-fccc-3e81-b52c-7fc5738fedd2 | -13.33683 | -50.93151 | 2025-10-03 06:35:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fb1d5f8c-b7e1-3572-8a7d-228441c24172 | -14.74997 | -48.11937 | 2025-10-03 06:35:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 1e40f2b2-6e9d-363d-83a2-e00083e9522d | -13.21222 | -50.89153 | 2025-10-03 06:35:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5ae2cdfe-c743-33b9-8cd3-b4cb3f9fb067 | -13.76899 | -47.53258 | 2025-10-03 06:35:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 074e016b-59f6-3424-965f-df2cd68add56 | -14.67967 | -48.07531 | 2025-10-03 06:35:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 526fa500-18ec-3fd6-a2de-5c3180afcabc | -14.9373 | -46.88744 | 2025-10-03 06:35:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 505756d6-5a53-3ec3-b718-3ecd197c47fe | -14.93596 | -46.87967 | 2025-10-03 06:35:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c0ba7cd6-ec26-365f-b5d0-dc3745ed6aad | -14.66406 | -48.07198 | 2025-10-03 06:35:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 83adf6cb-ddbf-34df-9795-2a3e8afab5fb | -13.77481 | -47.55759 | 2025-10-03 06:35:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 0cf42178-27c4-3691-9f72-fbf74589501b | -18.24309 | -53.30971 | 2025-10-03 06:37:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2cdc247b-57a1-3f66-bcc8-f361995ecb3d | -16.17114 | -57.59057 | 2025-10-03 06:37:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cdecdb45-e206-3760-89a6-5bdebcf7bd92 | -18.22664 | -53.35162 | 2025-10-03 06:37:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b7f8ff87-99cb-3442-a9dd-ec6f916997be | -13.2168 | -50.8856 | 2025-10-03 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2b6952cc-6105-3b6d-b61e-dd2c58275fbc | -14.5755 | -52.4576 | 2025-10-03 07:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ef196b5c-b9a3-3786-94fc-7fcef8d3d9e3 | -18.1574 | -53.3485 | 2025-10-03 07:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 30dd0313-827a-36ee-b24e-b8a114a76d90 | -14.9342 | -46.8965 | 2025-10-03 07:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1d3c7e07-6f1f-3e88-979e-019cb6f626fa | -14.6761 | -48.0915 | 2025-10-03 07:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4facdcb3-b3b7-3a5c-a0db-46b547085292 | -14.5755 | -52.4576 | 2025-10-03 07:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| a5d73290-9eef-37ce-8bff-121665426c65 | -14.9347 | -46.8736 | 2025-10-03 07:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 66178aa8-fbd2-3b4d-b0b1-a31bb7ebf881 | -18.1574 | -53.3485 | 2025-10-03 07:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9cf50faf-eea4-3b7e-b961-d8ca0395d7fd | -14.7341 | -48.1045 | 2025-10-03 08:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bddf8514-c833-3543-834c-ab9709696b1b | -14.9347 | -46.8736 | 2025-10-03 08:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f26304c8-b2cb-3570-b0be-225883849fad | -14.6761 | -48.0915 | 2025-10-03 08:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 969dd074-827d-3183-b3b8-c62125e413d7 | -18.1574 | -53.3485 | 2025-10-03 08:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4b011860-e5eb-3aa7-9353-625474d7edb1 | -14.9342 | -46.8965 | 2025-10-03 08:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 3e607223-6fa7-3c63-9320-4c4689d6a542 | -18.1773 | -53.3454 | 2025-10-03 08:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f4295425-9d52-3407-91d8-f7cb6df4ac9f | -14.9347 | -46.8736 | 2025-10-03 08:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ecdf863d-18c4-3b4c-92a3-412524f641de | -14.9342 | -46.8965 | 2025-10-03 08:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f3e75ee6-8b4f-319c-ac2e-5cfd22672307 | -14.7341 | -48.1045 | 2025-10-03 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 10f48df1-23bc-3757-9d77-1b599dfa0e2f | -14.6756 | -48.114 | 2025-10-03 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 90157e9a-f40f-33f1-9392-4bca2a284adf | -14.6761 | -48.0915 | 2025-10-03 08:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| c5c421a3-8af9-3869-85f5-a98058f06b9a | -15.7289 | -49.9397 | 2025-10-03 08:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b85a0d1c-160d-310a-a1f0-a9b679b9ecf2 | -13.2168 | -50.8856 | 2025-10-03 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b4c33dfe-d6b4-35c1-ba7c-cd96ed81a37e | -18.1773 | -53.3454 | 2025-10-03 08:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e56b5d00-fcf0-38df-ab34-2b4c20374f08 | -15.7284 | -49.9617 | 2025-10-03 08:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 2855a441-7139-3d00-ac67-2f551e7e066b | -15.7676 | -49.9555 | 2025-10-03 08:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| fc83c51f-ff9f-3458-89f9-9b6bbcfda38c | -15.748 | -49.9586 | 2025-10-03 08:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 141.3 |
| aa43da5f-9e9a-315a-9a97-235736a09485 | -15.768 | -49.9334 | 2025-10-03 08:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 3788b3f2-77b5-3f59-8243-e6c6501d5eaa | -10.967 | -51.0826 | 2025-10-03 08:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e613ade3-9f63-307b-bb5a-8ac919bda36b | -15.7484 | -49.9365 | 2025-10-03 08:20:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 01e3bfc3-5e2b-305e-b60c-b550a4f0f209 | -18.1773 | -53.3454 | 2025-10-03 08:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 30da7feb-8ad2-3f42-9ba0-4247b9797577 | -10.9673 | -51.0614 | 2025-10-03 08:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| e85195c4-99ed-3f6f-8b30-c712bc72bcd9 | -10.967 | -51.0826 | 2025-10-03 08:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bcb25d68-f8c0-3def-bf95-7b8f6852a10f | -18.2728 | -45.9343 | 2025-10-03 08:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 7680873f-091a-3fee-94fa-63d8a8457c02 | -12.6131 | -46.9725 | 2025-10-03 09:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| eaace66b-f2ee-3ca1-9bae-f706211ec327 | -12.6127 | -46.9951 | 2025-10-03 09:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 9a5c162a-ad34-37fc-9c65-3d9cf2277c92 | -12.6319 | -46.9923 | 2025-10-03 09:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 62cb9468-89a3-36d9-b8f2-a7f54c728bc4 | -12.6319 | -46.9923 | 2025-10-03 09:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 553a520c-1297-30e5-ad29-088f216856de | -10.967 | -51.0826 | 2025-10-03 09:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| db594beb-13b4-372e-b0e3-4b3f9815e4d2 | -14.6761 | -48.0915 | 2025-10-03 09:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 1138a387-af77-32a7-924d-39d158592218 | -11.9159 | -46.3044 | 2025-10-03 09:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 508c9bfa-2317-363c-9fe5-bdfc5ca5187a | -20.0728 | -45.7711 | 2025-10-03 09:10:00 | GOES-19 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 162.6 |
| bbd8edbb-a6b8-3292-96b2-09e4fcca8fb3 | -11.9155 | -46.3272 | 2025-10-03 09:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 206.2 |
| fc8ebc47-2088-364a-b984-bfe933567025 | -12.6131 | -46.9725 | 2025-10-03 09:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 6227ecc2-60e0-312d-bcab-034ca0c7b7aa | -12.6127 | -46.9951 | 2025-10-03 09:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 7584de15-eaff-3de9-839d-339a98a541f0 | -12.6127 | -46.9951 | 2025-10-03 09:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| d44acc7b-9487-3c3d-910d-be2d1b3beacd | -14.6761 | -48.0915 | 2025-10-03 09:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 43288cde-76f1-32cb-ae86-531a50671c15 | -11.9155 | -46.3272 | 2025-10-03 09:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 0e9c9fb5-a2bb-34ba-8664-a0795f6ecfd7 | -12.6131 | -46.9725 | 2025-10-03 09:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 977ad033-2027-3331-b74e-e0e11973ea3c | -14.6761 | -48.0915 | 2025-10-03 09:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| af436d3a-0732-3029-a4ed-4972290c0abd | -12.6131 | -46.9725 | 2025-10-03 09:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 8c1c8a1a-1f24-32f7-88d0-75ec890025c6 | -11.9155 | -46.3272 | 2025-10-03 09:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 1faa218c-604d-3379-b9b1-418469661a27 | -14.5755 | -52.4576 | 2025-10-03 09:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| ad25f3f7-f92a-3ef8-8f12-46caba79cc5e | -11.9155 | -46.3272 | 2025-10-03 09:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 623715b1-8377-3e75-964f-0e2536c2ed9e | -12.6131 | -46.9725 | 2025-10-03 10:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 7eca45b3-de32-376e-9a06-14dd7020a183 | -11.8963 | -46.3299 | 2025-10-03 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| de44e367-4500-3c9b-b927-3303ec4adb06 | -12.6127 | -46.9951 | 2025-10-03 10:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ab5c3b1d-4829-37df-93cb-9aa78b90667c | -11.9155 | -46.3272 | 2025-10-03 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 7e633257-5ee5-34ce-8942-90f4fd629d70 | -11.9155 | -46.3272 | 2025-10-03 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 216f5016-6416-361e-8994-6721486a3e96 | -10.9673 | -51.0614 | 2025-10-03 10:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 053f45d8-7e54-3874-9d22-1fb6cf63e239 | -11.9155 | -46.3272 | 2025-10-03 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| bae1c914-f226-306e-870e-9c07d4d369d6 | -10.9673 | -51.0614 | 2025-10-03 10:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c046efd3-7f13-3b55-a70e-0a0c50f2fd1d | -9.9182 | -43.7212 | 2025-10-03 10:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 88916f28-d68f-3eaf-89f8-f11e7de8286c | -10.9673 | -51.0614 | 2025-10-03 10:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 1e609f26-02f4-3bf9-bf0d-ce55ad68d532 | -12.372 | -46.5108 | 2025-10-03 10:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 86223cb9-0c6e-3d16-b7a8-2a1ed88103ba | -10.8216 | -46.7438 | 2025-10-03 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| cfbfee98-c046-3980-a0a6-50dfb0873275 | -11.9159 | -46.3044 | 2025-10-03 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 09c6ebcf-592d-370e-9eaa-5983077b8a2c | -11.9155 | -46.3272 | 2025-10-03 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 8e250827-59e8-3d60-9296-16b98f21f0ec | -11.1278 | -47.8413 | 2025-10-03 10:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a4c5bf7c-1091-36f5-83d5-14ae3d08bcd2 | -9.9182 | -43.7212 | 2025-10-03 10:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 0e639773-ed22-380c-bffb-5232531b4df8 | -10.9673 | -51.0614 | 2025-10-03 10:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 438360b5-aa1e-3df5-85ce-93d0834fd375 | -9.9965 | -50.2034 | 2025-10-03 10:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| da29aa12-e320-3aef-926d-4715ef8e9712 | -8.8343 | -46.7694 | 2025-10-03 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 56238cda-40ad-3bcd-adcb-d7e8fe251d43 | -12.6131 | -46.9725 | 2025-10-03 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 853f6c47-8596-3292-b1f1-429b548567a7 | -11.9155 | -46.3272 | 2025-10-03 10:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 0332e931-a5f3-3d0f-bad9-b1c726172c7b | -8.834 | -46.7917 | 2025-10-03 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5b2f4559-090c-30b4-9b69-c97d4f5dcacb | -11.1275 | -47.8634 | 2025-10-03 10:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 03792699-1e13-3b6e-9a8b-096e38f5e2fd | -9.9182 | -43.7212 | 2025-10-03 11:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |


[Clique aqui para ver as próximas entradas](README141.md)
