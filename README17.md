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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46df967b-af0b-3dc4-afc5-6187a48a3877 | -12.16651 | -48.68185 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf9a9c01-a761-398b-bcb3-f357d87d41b0 | -9.45568 | -57.83683 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a865ae3-9590-3944-878a-6be80cba95ea | -14.02392 | -53.36449 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad4146e6-04b7-3ac1-80e1-8ce461a42850 | -10.30459 | -57.13641 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0cf168e-d209-3703-8ba3-5b3fb5b85c4e | -11.06752 | -49.61909 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57fbcaed-7f2a-3afc-b6ef-5ae4a859e648 | -14.50312 | -48.0056 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 178169ea-4044-3417-9466-c48302ac54ec | -11.94433 | -58.7459 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2066947e-b1d1-3bb3-b574-819f5185bdb1 | -9.4088 | -48.43585 | 2025-06-21 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1498897b-0742-3443-9dce-14cb5ee49159 | -12.97567 | -54.68582 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1298f9fd-5988-3a0b-a871-3505cbe65f44 | -12.5724 | -58.38601 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de6af5d4-90af-3273-876d-f44790bc7c0f | -9.24428 | -46.91342 | 2025-06-21 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 26508532-189c-359f-90fd-5da884ecc93a | -8.98295 | -49.86526 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 09e92462-eda1-3743-b167-6b3619e82e0f | -11.11684 | -53.98004 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d987b012-eafc-32d8-82ea-6ee6c9c4cc12 | -10.8868 | -56.45834 | 2025-06-21 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b41f8172-4083-34b7-bd8b-36c9ab961b3c | -10.86432 | -53.75652 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4609889f-c56d-3851-9ab1-dbd1c0b99ef1 | -9.47976 | -57.82414 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e653125b-d5cd-3feb-a9f3-cf7ce1312ab3 | -15.40114 | -47.80033 | 2025-06-21 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9219f024-7501-3829-9d44-db4935636a3b | -17.58247 | -43.80069 | 2025-06-21 04:36:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5087cfb-2716-337b-afa3-7287a5f46722 | -21.17769 | -48.69346 | 2025-06-21 04:36:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4cd7e44b-3546-3ce3-bc8a-6cb54a7c81e9 | -19.5435 | -49.6623 | 2025-06-21 04:36:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1e7773f0-9f87-3d52-9c4f-0482a1a6444f | -21.19878 | -48.69674 | 2025-06-21 04:36:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de332123-4e6d-3295-8289-93b10236159a | -15.56833 | -47.85701 | 2025-06-21 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4db38fc9-2de5-3ab2-beef-1e81f79b8b8f | -17.75096 | -42.89484 | 2025-06-21 04:36:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c93cef5e-7af2-399c-b3c7-514a4946b998 | -17.78065 | -42.80782 | 2025-06-21 04:36:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0321ec3-ef02-34a8-864e-4f4359031732 | -21.69666 | -41.25916 | 2025-06-21 04:36:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c1986ba0-9f56-30da-8414-467e4ffef29e | -15.77331 | -43.27259 | 2025-06-21 04:36:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 12fbd8b3-73e3-3b60-817a-2df8454fc04d | -15.3977 | -47.79966 | 2025-06-21 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12eebdb2-0b9e-3099-a07d-f755c3a5564c | -18.19844 | -49.84356 | 2025-06-21 04:36:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c40bb32d-a0bc-335e-873f-e1adf2bc490e | -19.37403 | -51.40458 | 2025-06-21 04:36:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc264a68-d343-387c-a97d-abd1ee64fc11 | -17.57802 | -43.8001 | 2025-06-21 04:36:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6c42641-1ac9-3d61-9ffa-cdc7e96f612d | -16.10832 | -43.63261 | 2025-06-21 04:36:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3125908e-a55d-30d2-b368-bac01db4a7f8 | -20.7943 | -41.12783 | 2025-06-21 04:36:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a8f6407a-8fdf-38ac-8ff2-5656349400e5 | -16.42763 | -44.51855 | 2025-06-21 04:36:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b447fc92-efb0-3d9c-9398-f501279b58f6 | -21.69702 | -41.25525 | 2025-06-21 04:36:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 84b729cb-f374-3118-afc3-a767e61830a3 | -17.78117 | -42.80807 | 2025-06-21 04:36:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c8c604b-eb2b-30e4-820a-f290341f70c4 | -16.6821 | -43.88363 | 2025-06-21 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9bf3112d-6855-39f1-9faf-cf9b2166e5aa | -15.39826 | -47.80099 | 2025-06-21 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9e532f4d-667f-3cde-9d97-b13a95280387 | -19.54687 | -49.66286 | 2025-06-21 04:36:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 62d5cc6f-d5a3-3a3b-a7b8-28be7732062f | -17.21757 | -44.8001 | 2025-06-21 04:36:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 029d20e9-aaf8-3fbc-945f-c502b53baac0 | -16.46486 | -45.00499 | 2025-06-21 04:36:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e0c5a08-01f5-3fa1-861c-b9b79487b7b2 | -19.37345 | -51.40823 | 2025-06-21 04:36:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0de47b1-1219-35db-9a95-bd18f9c66691 | -15.08003 | -48.94521 | 2025-06-21 04:36:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a01301f3-6eb7-39e4-a62e-c2db818f63b1 | -20.92482 | -49.09948 | 2025-06-21 04:36:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 57e373fa-bdd9-3606-8ff1-265964995e57 | -16.43181 | -44.51913 | 2025-06-21 04:36:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f5826ce-731b-3228-ab3b-65a0d5805a9f | -20.9254 | -49.09548 | 2025-06-21 04:36:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 20294b18-ae43-3e20-8225-ecd319227b90 | -15.39714 | -47.80355 | 2025-06-21 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb81919f-f72d-3f78-95b4-fb670941335b | -15.76882 | -43.27192 | 2025-06-21 04:36:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e6f67d2d-0453-3aa9-be76-2c01a86490f8 | -15.40057 | -47.80423 | 2025-06-21 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a87802cf-7e36-3fad-a488-cf65781d740a | -19.02398 | -57.62198 | 2025-06-21 04:36:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| af8f6c41-4e74-351e-bdc9-402d94e8a6d8 | -17.57695 | -43.80902 | 2025-06-21 04:36:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3d4bdc1-e42a-3e7c-af19-b3abb33c2d82 | -17.25902 | -49.63045 | 2025-06-21 04:36:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ad2ef72-30cc-33f8-9f9a-c4157705562f | -21.29017 | -48.55876 | 2025-06-21 04:38:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98e93a69-35da-3985-b775-9b09d6c61773 | -21.69517 | -49.50813 | 2025-06-21 04:38:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d6132368-35a5-331e-a009-4f731945f45f | -21.68546 | -49.50246 | 2025-06-21 04:38:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 733da39b-387b-3d75-91dd-19d8d5431de3 | -21.42945 | -48.64804 | 2025-06-21 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 575a413b-1ac3-3d4a-9c81-3640d1923be6 | -20.99704 | -51.79205 | 2025-06-21 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 89521110-fc2e-309b-8ae1-d8ed5a9fbab2 | -22.78813 | -43.75701 | 2025-06-21 04:38:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 28027ce7-041c-3241-a66c-5338891a3c5b | -22.41321 | -43.58243 | 2025-06-21 04:38:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d96408e-b2ba-328e-8164-7c8c611edfad | -22.94231 | -43.30762 | 2025-06-21 04:38:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 06f02a16-5004-3646-850a-f1b349f16140 | -27.32383 | -48.58745 | 2025-06-21 04:38:00 | NOAA-21 | GOVERNADOR CELSO RAMOS | SANTA CATARINA | Brasil | 4206009 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0f9a4789-3e6f-3b1d-b6ec-08bcc5ddd0cc | -21.6986 | -49.50869 | 2025-06-21 04:38:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cfb7a73c-db17-32b1-bd26-4e8487619b00 | -23.34033 | -46.7756 | 2025-06-21 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08f3032e-80ee-3c97-9959-3f8b47ab7f49 | -22.9437 | -43.3078 | 2025-06-21 04:38:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 1b3cc699-04d4-3932-b2bb-1b9ad4cbe68b | -23.40736 | -46.55801 | 2025-06-21 04:38:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5af1c0ec-9c4b-33f4-88b8-b1c62ff863c4 | -21.68946 | -49.49907 | 2025-06-21 04:38:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5f59f32f-34d3-31df-8fe2-c7a055c0857b | -21.98178 | -46.82785 | 2025-06-21 04:38:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a379d6d-cfba-336e-82cc-0f630e6839ef | -22.92103 | -47.13535 | 2025-06-21 04:38:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e0adfac-cebf-3246-bd5a-f3d365049fe3 | -21.80823 | -47.2488 | 2025-06-21 04:38:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 851cf8fb-efcd-34dd-8c5a-126a64f43276 | -22.53978 | -48.81266 | 2025-06-21 04:38:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 421aacfa-965a-3daa-b7b8-88e45767bc4a | -21.01818 | -52.82225 | 2025-06-21 04:38:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0811551d-d412-388d-bf85-12cf406e9692 | -21.01419 | -52.82544 | 2025-06-21 04:38:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e957b3d7-3639-31f2-8d05-08da65e09dd3 | -21.01755 | -52.82606 | 2025-06-21 04:38:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70eca077-659c-35bd-9ec8-4b78179dd9bb | -22.84144 | -43.48771 | 2025-06-21 04:38:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 86362f29-749e-3535-b165-c7bfb3eb8bc3 | -22.64998 | -47.41562 | 2025-06-21 04:38:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1bf14ee-f4a7-372e-8fe8-bd7c648cc1ff | -21.69231 | -49.5036 | 2025-06-21 04:38:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 32bb05ee-e63c-3912-a6a5-e7efc1fe3cfd | -21.68889 | -49.50304 | 2025-06-21 04:38:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3dcffac8-8ebf-378c-ad70-3b99dbb2b68d | -21.01482 | -52.82162 | 2025-06-21 04:38:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 781e1c66-7b28-3bbc-b8a1-509e5d381c14 | -22.8444 | -43.48762 | 2025-06-21 04:38:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51c6e9f4-acb5-3e32-8cfc-d111e553eb72 | -21.68603 | -49.49849 | 2025-06-21 04:38:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e90665f9-c973-39d7-827f-10d38712a18b | -11.8853 | -54.6722 | 2025-06-21 04:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b3339927-4e36-376e-9be9-9418e5399542 | -4.5429 | -48.0151 | 2025-06-21 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| ed32f2f4-895c-37db-87b4-9440eecc2159 | -11.8663 | -54.6739 | 2025-06-21 04:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 6c5bd01e-36d9-3d5c-8d8b-6e32f6ae8e2c | -11.7791 | -57.2445 | 2025-06-21 04:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 70007ed1-e164-3eb0-9654-8831b572c03c | -4.5243 | -48.016 | 2025-06-21 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| bf2b07af-0aef-3e53-8d82-5991b2de08eb | -11.798 | -57.243 | 2025-06-21 04:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 5d5b5119-cde0-312b-97c9-d9c9eba42880 | -29.8668 | -51.16309 | 2025-06-21 04:40:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 8b5552c6-60f7-3f15-b1ff-bd51dcd70929 | -11.798 | -57.243 | 2025-06-21 04:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1ca8f52e-bbb9-3cdb-89e6-d5547bd2d097 | -11.8853 | -54.6722 | 2025-06-21 04:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8108990e-cdca-31ba-8743-301b5fd7ac59 | -11.8663 | -54.6739 | 2025-06-21 04:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| cf84504e-431b-382e-bd99-6b48f07ed8f5 | -11.7791 | -57.2445 | 2025-06-21 04:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 42d8607a-359b-3119-839b-f25219bfa441 | -7.22133 | -43.05494 | 2025-06-21 04:51:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 70ab6b96-04a4-3ab5-8179-cfc5dba0b5ba | -7.22327 | -43.06308 | 2025-06-21 04:51:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 4e6744d3-ee27-36ad-9fca-36aced1d1585 | -3.96426 | -48.12917 | 2025-06-21 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ebee6a0d-f994-3dc1-898f-8df4c15d5a6b | -4.37762 | -48.07521 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 931c9269-8254-349b-86d9-bdcaea8a9fd7 | -4.53835 | -48.00407 | 2025-06-21 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31358dd5-baca-3820-966a-b80b3bdccd05 | -5.75771 | -43.05527 | 2025-06-21 04:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0649887f-0d5e-3de9-bd9a-422c3abfc99f | -3.62345 | -47.52891 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 280ab76a-4284-3459-b97f-240b904733aa | -3.04037 | -49.43875 | 2025-06-21 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a05e92aa-82a1-35e6-ad44-9e2ca76c513e | -2.53349 | -53.95764 | 2025-06-21 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da442d38-c6f1-32f5-8950-079cd635c0a9 | -3.62406 | -47.52486 | 2025-06-21 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README18.md)
