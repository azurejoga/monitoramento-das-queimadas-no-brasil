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
| 3ef50b0a-4b89-3dde-9974-4faa5acc4f78 | -11.698 | -50.3629 | 2026-07-23 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e7cbb4a2-6181-341b-a9ae-72532bef35fb | -11.9451 | -50.377 | 2026-07-23 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 87b25dda-f336-321c-a103-ec76ad81c3a3 | -11.6789 | -50.3651 | 2026-07-23 05:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 3e9391d7-4407-3bc0-8e34-aaa0b476c85f | -11.7875 | -47.1108 | 2026-07-23 05:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 20372ca1-293f-3c94-a44c-e19ce8844ba1 | -11.9645 | -50.3532 | 2026-07-23 05:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| b6653d3c-2b98-30d4-acbe-119cafb0f765 | -11.9641 | -50.3747 | 2026-07-23 05:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| cf779435-e734-3926-95cf-0babbfb1fe36 | -11.7875 | -47.1108 | 2026-07-23 05:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 50b895e7-0ef3-3d6a-b1a9-58b94ba6a824 | -0.09127 | -51.2798 | 2026-07-23 05:27:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20f30c61-d80e-364e-af81-5b51949bbc2f | -3.09829 | -54.51555 | 2026-07-23 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 131712d8-0b79-397e-ad70-ea0d513af33d | -1.78564 | -55.52575 | 2026-07-23 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd96716-95a9-36a5-83b2-e7c030d07456 | -2.4147 | -60.0117 | 2026-07-23 05:27:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7768af76-0f4a-3df9-8db2-9028cc01c637 | -2.8536 | -54.48933 | 2026-07-23 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6f6a6cc-ec27-35ca-83c2-48bc19acb721 | -2.8437 | -54.67915 | 2026-07-23 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cdbaa2f-8bc1-3c28-8de4-1b2525ec644b | -1.78379 | -55.52694 | 2026-07-23 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b89c28b-7685-34ac-8dfa-3e08230f03a2 | -2.84304 | -54.68346 | 2026-07-23 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8306b289-a286-3770-af02-5a5681cb01ef | -9.12651 | -61.05794 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d934e39a-4fd4-3714-91b4-99af018f2e57 | -9.1254 | -61.06527 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02111d5-ca6c-3603-923d-fc9d443dd397 | -8.44651 | -63.83765 | 2026-07-23 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68c90129-09f7-3857-8ebb-dbe6c8a5c783 | -8.82815 | -63.90261 | 2026-07-23 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2f79a4a-ef81-3e48-bf90-bb7ac710a5b1 | -9.1243 | -61.07261 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c229ceba-c0c9-33ad-b8cd-0a08a8ea5da1 | -9.23769 | -60.38496 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e716191c-2435-3597-838e-4da775a13e11 | -9.12706 | -61.05427 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 762bba53-036b-3b34-96b3-bec30843d3e9 | -9.12879 | -61.06579 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fa17378-7796-300a-8669-190b683648a5 | -9.18493 | -58.06595 | 2026-07-23 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11c620d6-5ef8-305e-8cfc-970e8aa82e27 | -9.12547 | -61.08781 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92a0256b-2793-3b56-bfb4-79fbcefa6ecd | -6.21132 | -49.43177 | 2026-07-23 05:29:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0962406f-333c-3d19-bd39-a262a57c794c | -9.12485 | -61.06895 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b84d020-74de-36f6-a12e-f0392d3446e9 | -6.20888 | -49.42764 | 2026-07-23 05:29:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d901e38f-feaf-3971-9f49-42a87930b454 | -9.12319 | -61.07994 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a863e22-a2d5-30d4-ad70-2130a7d25225 | -7.32607 | -64.70179 | 2026-07-23 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a48e60da-be80-3b8d-8b75-842508e74669 | -8.44316 | -63.83712 | 2026-07-23 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa46bdea-1a9d-3294-bede-17989a0f70fa | -9.12367 | -61.05375 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48fe5964-9bd0-321c-894a-3016495c1888 | -8.82759 | -63.90617 | 2026-07-23 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 83e6b24c-7303-3cd5-afa4-5ffd994df50f | -9.12374 | -61.07627 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 333eff5d-eba8-3bc9-a9b6-ab8eba8f5353 | -9.12153 | -61.09095 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf8314c2-c7d6-360e-8a06-f5a48452cfc7 | -9.17285 | -58.31304 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9036d1c2-29fd-3f72-8c3a-0242e624e3fd | -9.13163 | -61.06998 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db599fb3-6ea0-3db8-a375-b2940c4ce9a8 | -7.6126 | -55.26708 | 2026-07-23 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e5cebcd-84aa-36fa-91b6-8812175f4d91 | -9.16196 | -58.30637 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7694a44-9999-38e8-af77-efbf2f84a2da | -9.12492 | -61.09147 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27074674-2061-37db-879b-09be83b35b6b | -7.71112 | -62.33291 | 2026-07-23 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9803a1ea-5119-3674-89db-60979e0e609f | -9.17019 | -58.31496 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fc0c49f-96f2-3b04-8b62-9084e0fecbd8 | -9.16898 | -58.31247 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d320a0b-eb42-3a94-93f7-caed52943f37 | -9.16314 | -58.30885 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0f224ec-3fb6-3e28-bf4e-8b17544075cf | -5.76592 | -49.08773 | 2026-07-23 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1516cdaf-14fc-318e-bf6f-60f8a733fd42 | -5.75914 | -49.08679 | 2026-07-23 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59870670-fa94-342d-bad6-5ce0c115cf9f | -9.16511 | -58.31188 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d26ac8b-f91d-3f64-98b5-a708bc700ade | -9.12595 | -61.0616 | 2026-07-23 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c74b97-e9c7-39f4-9a3f-916b90856711 | -9.17407 | -58.31553 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eb03bc5-d17e-3d66-9a44-a3a6b4e95661 | -9.17088 | -58.31004 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b32f3707-769f-3a95-80b6-1f3b6b0c6b68 | -9.16701 | -58.30946 | 2026-07-23 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0562a1a0-4785-32f4-8d06-0d4f100ae936 | -11.698 | -50.3629 | 2026-07-23 05:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7bcc448a-5a4d-3e70-bb1c-cd865ffca559 | -11.6789 | -50.3651 | 2026-07-23 05:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 26fc0ae4-53f3-3177-ad27-89bd0471f96d | -11.6792 | -50.3437 | 2026-07-23 05:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 6f95c5fc-06df-3d23-a851-f83b5f98a95b | -17.79517 | -50.53022 | 2026-07-23 05:31:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16283dfa-e27e-3e9f-bbb8-4123494ed629 | -12.39586 | -50.39003 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07b76e29-f6f9-3770-ac3a-05a2065a5900 | -11.95584 | -50.35854 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f72aa613-0b20-329f-89ca-8aa0a63b775c | -11.66752 | -50.35509 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 451c4684-dab3-3b9a-8257-210ec9fb38f4 | -9.82757 | -62.27868 | 2026-07-23 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1468c4ad-7715-3404-9c5c-5bac4a076880 | -13.37558 | -54.3028 | 2026-07-23 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1660a51c-dd67-3837-b246-2ee95980a0dc | -11.69017 | -50.36169 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 97195909-1299-3683-9102-30a101d98c3d | -9.82806 | -67.88597 | 2026-07-23 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3192f96-40d0-362c-a715-00dafa334137 | -11.85254 | -60.70771 | 2026-07-23 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34778265-6cc6-3dd2-8a4b-23ea9eb276ea | -9.55435 | -66.19061 | 2026-07-23 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae1276ce-987f-33bf-bd05-6233fa63308e | -11.68408 | -50.3547 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4666059b-3ade-3f04-bd21-49e64bff5b1d | -11.67668 | -50.35994 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e83837c3-33b3-3d8c-a0f7-6bd6f9d9b737 | -11.93354 | -50.37438 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbc0ef70-4e3a-3df1-a995-e4243f12c888 | -11.00435 | -54.31297 | 2026-07-23 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45217669-f094-3970-9d60-d4909f4261d1 | -11.33836 | -62.22234 | 2026-07-23 05:31:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcb088a7-0f91-3520-bf94-68b039e220dd | -12.88346 | -58.28649 | 2026-07-23 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f93b0065-0877-33a5-926f-72c73eb9bf69 | -11.80608 | -50.388 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d17d4d63-cc4d-3537-b157-c93e1228d499 | -11.68032 | -50.3629 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3bf3be42-90cb-32ed-96b7-fb254a33c289 | -11.96125 | -50.3717 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7a520bf0-3ca1-3703-b63c-737703c2d6e7 | -11.70658 | -50.3724 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4ac5ef9-a96a-3687-85f0-508b813178ae | -11.968 | -50.37257 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c3113a66-fd99-3982-b4d9-e4ea3e662956 | -14.30594 | -52.0908 | 2026-07-23 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 92f68146-339f-39bb-9b00-b391649262ec | -14.31275 | -52.08652 | 2026-07-23 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 31136de1-6cda-32af-ac02-99564f8e1b1d | -11.70232 | -50.37567 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d1f7457-5a1c-3717-9b90-b519fba7bcbf | -11.68342 | -50.36081 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b500383a-1ad9-3941-830c-ebf18dfcaef7 | -11.6931 | -50.3707 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d63d785a-3842-3df1-8cb9-e3d158ac3b5f | -11.68706 | -50.36375 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a979f063-c25d-36c5-9f30-6d96e02d647b | -11.33781 | -62.22591 | 2026-07-23 05:31:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 944c0789-1d82-3076-b11f-3cfb3939d209 | -13.37021 | -54.30203 | 2026-07-23 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b39df4f-4c88-3e4b-82b4-df0abbe34350 | -11.96193 | -50.36555 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4fc0d4db-38ab-3a9a-bea0-424893e2c471 | -11.70906 | -50.37656 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ec630c8-f053-3cec-9a93-0f0efaa8f2df | -11.97041 | -50.37099 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa1cad36-1b9c-3cbc-849d-a5417602eceb | -14.38172 | -58.33945 | 2026-07-23 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac9e2a6f-e529-3149-96da-4151115df147 | -13.37599 | -54.29925 | 2026-07-23 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609af466-ecbe-3358-b644-a0c9cc2c36df | -13.31514 | -54.32601 | 2026-07-23 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d412d99-102c-3079-bf1d-fa0215a3a210 | -11.68101 | -50.3568 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a11efaf-6a1f-3534-aeca-1cba92d7ac5b | -14.31221 | -52.09161 | 2026-07-23 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0a7eb373-5a6c-3c8e-9693-1b2f141d80f5 | -11.95516 | -50.3647 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2e73ed0a-4ee5-3d4f-b46c-8e44e94849bb | -11.9403 | -50.37525 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b096ba66-faeb-3be9-b989-cf3b41b01079 | -14.30649 | -52.08574 | 2026-07-23 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 45b61aa3-4fe0-327e-b309-1301cc16cc93 | -11.80342 | -50.38858 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ae10f629-f1ee-34cf-9aa8-ba389f026a16 | -11.68171 | -50.35069 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 52ebb1a9-91f6-3a66-9eb3-57cebf5a21e7 | -11.69984 | -50.37155 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0573fc0a-17ba-33ee-b7ee-df52118733bc | -11.95652 | -50.35238 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fac2a06c-c340-3125-8a89-665287114da6 | -11.69559 | -50.37479 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd813416-0a15-3206-957a-e5acb33f81b6 | -11.67357 | -50.36206 | 2026-07-23 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README18.md)
