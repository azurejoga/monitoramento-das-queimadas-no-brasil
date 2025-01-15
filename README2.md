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
| e018f139-105b-36c8-b243-c62c6e0972db | 1.3217 | -60.4452 | 2025-01-15 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 00b9bfa4-0466-3388-bddc-8bfdd6df7a62 | 2.1039 | -61.8166 | 2025-01-15 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| f15d7701-95a9-3778-862f-36125a70fc32 | 2.2889 | -60.2076 | 2025-01-15 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 22f6a1c5-a264-3508-8db4-958c9234038a | 1.3217 | -60.4262 | 2025-01-15 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.7 |
| fb5f2d2d-ee3f-3b32-af0a-ce834288af48 | 2.0856 | -61.8356 | 2025-01-15 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 92f504ff-3fff-3510-a5a7-740aa9d56859 | 2.0856 | -61.8168 | 2025-01-15 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a9c3c612-2f46-30c0-8a1e-90bd7e571169 | 2.2889 | -60.2076 | 2025-01-15 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6999cbcf-aa86-3e56-a86f-ecbb8bdbfbef | 2.1038 | -61.8354 | 2025-01-15 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 80de6a91-49d0-316f-8292-2532090f5d84 | 1.3217 | -60.4452 | 2025-01-15 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.0 |
| e803eb12-afa6-34f0-bc77-0dc4c955d728 | 1.3217 | -60.4262 | 2025-01-15 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 485bf62e-1444-38ff-8201-91ba2d1c1a3d | 2.0856 | -61.8168 | 2025-01-15 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8e24bb0c-60eb-34b2-b57e-9935c2b075eb | 2.1039 | -61.8166 | 2025-01-15 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 3903bcdf-bf9a-3813-9999-791333461cd1 | 2.1039 | -61.7978 | 2025-01-15 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c1d34cf8-bcb0-3626-8cfa-2c542838cbc1 | 2.1039 | -61.8166 | 2025-01-15 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e96ac5b7-f727-3f95-b58e-8e23b3503d2b | 2.1038 | -61.8354 | 2025-01-15 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0d91e894-4de5-3214-9461-7bee5255326f | -2.5104 | -51.9258 | 2025-01-15 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 705a21b4-7799-3f10-bc21-a0c1269fc51c | 2.2889 | -60.2076 | 2025-01-15 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 6fe5f034-8a6b-398f-adca-eeef2d8a62e2 | 2.1038 | -61.8354 | 2025-01-15 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e97ea546-b85f-349d-b99e-5f2d5ee773a7 | 2.1039 | -61.8166 | 2025-01-15 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 9e3e7e88-5922-35d5-ad3d-6f683630c88f | 2.0856 | -61.8168 | 2025-01-15 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 821cb586-9099-3e8b-81be-42616efb7ca1 | 2.1039 | -61.8166 | 2025-01-15 01:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 90.0 |
| be3f30df-b1b0-301e-a194-cbd47b082002 | 2.1038 | -61.8354 | 2025-01-15 01:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 4c0bac2a-6f32-3c44-9f49-53423f459a46 | 1.3217 | -60.4262 | 2025-01-15 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 74aac122-c202-3724-9a89-78499c594db8 | 2.2889 | -60.2267 | 2025-01-15 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.0 |
| db589c9b-6e50-3faf-9202-74de5879ae0c | 2.2889 | -60.2076 | 2025-01-15 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| b43b081c-cf4b-360f-bf25-c6d63cf0867a | 1.3217 | -60.4262 | 2025-01-15 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 6b27bd5c-62a3-3172-9826-b5a995a60ff0 | 2.1038 | -61.8354 | 2025-01-15 02:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ee0df8c9-77cd-35a1-99f7-a745d1d68bab | 1.3217 | -60.4452 | 2025-01-15 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 7a9644f1-3fc7-34ae-9a57-2959472fde28 | 2.1039 | -61.8166 | 2025-01-15 02:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 5da355ef-392d-32c6-9806-29c006bab615 | -9.259 | -60.309 | 2025-01-15 02:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 03ec4c7d-67bd-3f4c-9839-94b24c79f350 | 1.3217 | -60.4262 | 2025-01-15 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 3f36e989-652a-394a-8ac1-37bf530b0de0 | 2.1039 | -61.8166 | 2025-01-15 02:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 251e195a-8693-3c2b-8c1d-44026baa684f | 2.1038 | -61.8354 | 2025-01-15 02:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 48d7d2a0-a06c-3cf6-9506-d1dae9831dd4 | 2.2889 | -60.2267 | 2025-01-15 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| a3675c6d-237c-3e4e-adce-a21468bf6617 | 1.3217 | -60.4452 | 2025-01-15 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 1956a701-1e3f-3a63-88e5-67ad53e5c8e4 | 2.2889 | -60.2076 | 2025-01-15 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 587eedcf-1f8b-3459-9df2-378887a3f494 | 2.1039 | -61.8166 | 2025-01-15 02:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1a5e9648-59ee-32c2-8c9a-ea4b13b17e1b | 1.3217 | -60.4262 | 2025-01-15 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d1b1864f-8b57-3cd1-b694-0a5e21f3ae03 | 2.1038 | -61.8354 | 2025-01-15 02:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cf93447c-f1b1-35ec-b979-94c621f1f68f | 1.3217 | -60.4452 | 2025-01-15 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 1459725d-876f-3f80-ad9a-f1cdffaccc8e | 1.3217 | -60.4262 | 2025-01-15 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| cd0008a6-ad8b-3aa7-858f-19a984d2e38b | 2.1039 | -61.8166 | 2025-01-15 02:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2d82f3f5-76e2-31a7-8584-4a99ec7fcf73 | 2.2889 | -60.2267 | 2025-01-15 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 0cfa5eee-1148-32c3-9b60-c5d7f04679f6 | 2.2889 | -60.2076 | 2025-01-15 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 06705e42-101b-374c-b278-bd8d34b38471 | 1.3217 | -60.4452 | 2025-01-15 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| ad985e87-6b73-32c7-903d-b324ce74bee3 | 1.3217 | -60.4262 | 2025-01-15 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7aaed14d-32be-3afa-b3f4-2de6893eef19 | 2.2889 | -60.2267 | 2025-01-15 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e711a7ed-67d8-32e0-bf7e-be48ae269949 | 1.3217 | -60.4452 | 2025-01-15 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a2d736f3-dc18-370f-b399-4ebc20a894af | -9.259 | -60.309 | 2025-01-15 02:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7fcab954-e881-301b-9479-3168415650c4 | 2.2889 | -60.2076 | 2025-01-15 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c1888b4e-78b8-322a-9789-f4cd9c5b0eff | 1.3217 | -60.4262 | 2025-01-15 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| bb951c13-278b-3299-8580-87da6c2895f9 | 2.2889 | -60.2267 | 2025-01-15 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| e67cfc2d-d713-3538-8d1b-6f5e9962d72e | 1.3217 | -60.4452 | 2025-01-15 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| eebf4ec4-70b8-3e04-b11f-6745ae80a61b | 2.2889 | -60.2076 | 2025-01-15 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ae50b42f-2f73-36f7-84af-0cf5ab96954e | 1.3217 | -60.4262 | 2025-01-15 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 22ba0812-eeb5-3d59-85f4-d75ffefc12a8 | 1.3217 | -60.4452 | 2025-01-15 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 66224448-f4a5-3688-ba46-b69b613a7eac | 2.2889 | -60.2267 | 2025-01-15 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 6d75ae86-eeaa-3279-a5f6-c5255f4cc42b | 2.2889 | -60.2076 | 2025-01-15 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 59f82c67-107c-33ea-b0a5-a010b69c6529 | 2.1039 | -61.8166 | 2025-01-15 03:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 665aafc5-afc8-3c86-b311-0d20ea1a0178 | 2.2889 | -60.2267 | 2025-01-15 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8efd2be2-23dc-31ba-8673-d9e9106a0cb8 | 2.2889 | -60.2076 | 2025-01-15 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 95cd5742-1dc6-375f-b70a-6c02d4a05c21 | 2.2889 | -60.2076 | 2025-01-15 03:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 35628d9f-543d-3242-9d76-38a9de412c7f | 1.3217 | -60.4452 | 2025-01-15 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 7e3059cd-6017-3f50-aa09-f043ac53ded8 | 2.2889 | -60.2267 | 2025-01-15 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 32a4808f-f963-36ee-8d10-3d72e005ad28 | -12.12923 | -38.16988 | 2025-01-15 03:38:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 413457dd-021a-3ffd-bcec-ee0f6260a1e4 | 1.3217 | -60.4262 | 2025-01-15 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 5602272d-68de-3e4c-a2d3-c3a5cc8a3088 | 2.1039 | -61.8166 | 2025-01-15 03:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 44376566-50ba-3d5a-9a26-ba4e53c25247 | 2.2889 | -60.2076 | 2025-01-15 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 29.3 |
| fbdab072-8c98-30b9-8188-acd80cd5494a | -21.44393 | -48.60781 | 2025-01-15 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b43e2a5a-25ec-3e41-9fdb-7769873fb2c6 | -22.10794 | -49.62822 | 2025-01-15 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c71eb273-eb82-3d26-a455-e5e8993cc7c5 | -21.44975 | -48.60912 | 2025-01-15 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a656720d-8de1-3b2d-9722-30f53f4d8f47 | -21.45079 | -48.60449 | 2025-01-15 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 8aac510f-a848-3f93-8900-f20426df970e | -22.10711 | -49.63105 | 2025-01-15 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4237f35d-c97c-3a3a-b490-066da76d6683 | -21.44875 | -48.60957 | 2025-01-15 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 90133905-5fd3-37b5-bf2b-299baa37e101 | -21.44984 | -48.60494 | 2025-01-15 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 3aa81ecb-0787-3f14-bf33-a892f03218a6 | -22.53865 | -48.81234 | 2025-01-15 03:40:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f873f6f-1f6a-314a-b413-d77594e2d81e | -23.85481 | -48.10441 | 2025-01-15 03:42:00 | NOAA-21 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e579db8a-f4b0-3469-ba6c-7a55727e0877 | -25.18892 | -49.32697 | 2025-01-15 03:42:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dc7698a0-f4ea-3f31-adc7-a976f0ff9796 | 2.1039 | -61.8166 | 2025-01-15 03:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 89528e3c-41cf-3ec9-8729-ff23d16b22a5 | 2.2889 | -60.2076 | 2025-01-15 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5adfa4f9-239a-3341-a128-15426a8b262e | 2.2889 | -60.2267 | 2025-01-15 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 767ef2f4-52d9-37f0-9227-23671cf6462b | 1.3217 | -60.4262 | 2025-01-15 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c3a0911f-5004-3240-a5ec-66e8a8dd7003 | 2.2889 | -60.2267 | 2025-01-15 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 65176d1c-5b22-3ed0-a8a1-600446aef48d | -9.259 | -60.309 | 2025-01-15 04:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6a16904c-c7c4-39ff-9c88-15f4d5ba7019 | 2.2889 | -60.2076 | 2025-01-15 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 71d9aef6-1c1d-39e0-9ce1-4d41f066ea98 | 1.3217 | -60.4452 | 2025-01-15 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ec6cb883-18a1-3c0c-8822-2ddc7ef03917 | 2.1039 | -61.8166 | 2025-01-15 04:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c85d2339-ceb1-3c94-b22d-c60efa203532 | -19.80126 | -53.792 | 2025-01-15 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6b5bc4f-c5f0-39d1-bb69-72d252c39ac2 | -23.85282 | -48.10131 | 2025-01-15 04:06:00 | NPP-375D | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 094a1f89-c07b-37f9-8501-5d74737bc97e | -23.41341 | -49.64227 | 2025-01-15 04:06:00 | NPP-375D | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bba67d68-d2a9-3f86-baa0-965ec357fb4f | -23.41992 | -54.8281 | 2025-01-15 04:06:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6f1b2df1-5f79-326d-8112-f68b283b79bf | -21.44913 | -48.60344 | 2025-01-15 04:06:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4508f909-d99d-3b43-a23f-c44e8a5a03a3 | -21.4481 | -48.60886 | 2025-01-15 04:06:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 86880d0f-40f1-30b9-bdd5-857e2190b059 | -22.5417 | -48.81361 | 2025-01-15 04:06:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b6434a9-dd06-38ac-b438-29073ff2db98 | -22.10988 | -49.62879 | 2025-01-15 04:06:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e38f0735-93c5-3a3c-b3a9-c9df4bf2d2c6 | -23.27646 | -47.09616 | 2025-01-15 04:06:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 95a84b21-3d67-3fef-a3cc-800cd5c929d5 | -23.8565 | -48.10215 | 2025-01-15 04:06:00 | NPP-375D | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a5a1cc28-d05e-343f-a08b-d56692103ea8 | -19.79564 | -53.79091 | 2025-01-15 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ae5ae1d-b4df-34df-b94b-bef16787dcaa | -23.41744 | -49.6432 | 2025-01-15 04:06:00 | NPP-375D | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5b93c716-2cd1-3937-a0cc-68623e8db834 | -21.19121 | -52.02631 | 2025-01-15 04:06:00 | NPP-375D | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
