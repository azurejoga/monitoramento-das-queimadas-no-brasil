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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91e55b2-a4bc-393f-bca8-bcb43b2c1fd7 | -4.1423 | -54.0242 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a331bc9c-1677-3068-a3c4-0754769cda02 | -4.3159 | -50.775902 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12659d95-130c-3de9-a38f-6edbefc84def | -3.0062 | -54.060799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3811428e-565c-31a4-b171-51e46cce3603 | -2.9825 | -54.138699 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d8f5e56-e6ad-3ec8-b89c-3471b1313b3d | -2.9516 | -54.138401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27e12f69-82ef-3bb9-b504-6401799bcc2e | -2.4878 | -56.146801 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb18158-61f1-3b70-8da2-107cbf706823 | -2.0465 | -56.2006 | 2026-10-08 00:26:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad1e93a-ef15-3468-a08e-fa34d25f2678 | -3.1079 | -53.782501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b85a49b9-35bb-3997-af5a-72e8efacaaa5 | -8.7176 | -45.163101 | 2026-10-08 00:26:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb3efdb-582f-31d0-9eff-ec739fe10a28 | -3.2679 | -53.987801 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7360b912-b264-3d50-a96b-94678d3f181b | -3.1493 | -54.101398 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eed7c95-25b3-3f16-bc53-d5b33990a230 | -5.972 | -55.376499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa32d465-4479-326f-a8fa-e55c7022a6ef | -3.2903 | -54.040901 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2dc7a5-4d12-31e6-9834-e4b0e944f320 | -1.3251 | -55.424999 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a86baef2-b4f2-3694-a787-4b82f65fefb9 | -3.2924 | -51.566101 | 2026-10-08 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a20a259-378e-33bd-8b3e-c1e904ff9b3b | -1.8545 | -57.040501 | 2026-10-08 00:26:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de1a092d-b8ab-3408-ba85-a0bdc21d4456 | -3.1738 | -50.559799 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c60bb1d-c7eb-3ed3-bd9e-23b78c43d30d | -11.6305 | -43.693802 | 2026-10-08 00:26:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08510f05-a384-3a7f-a43d-e4ff9d22d63a | 1.7723 | -55.540901 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 069a8d47-3f48-3790-81f6-8bdea6e7e4d1 | -5.8594 | -53.4575 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f56d589-d8e8-3fb1-aea1-a86d1e55bbfa | -3.2906 | -60.991001 | 2026-10-08 00:26:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5865cec-3cbe-3d7c-8562-1483121330ad | -2.7517 | -54.030399 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903626b3-e0d1-361c-9492-fac10b4c8f2b | -10.2444 | -49.656502 | 2026-10-08 00:26:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a7216e9-74b8-343e-9e5b-e27fc6cc18a3 | -3.1003 | -53.930599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fce8031-fdeb-3e79-9a57-83ffdf7dcc0d | -3.5765 | -54.667702 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4606479a-2f74-305e-87c1-3bf2b87314de | -3.0079 | -54.751301 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0011a9e1-d953-3617-a2c7-d546921c1224 | -3.4717 | -59.5844 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17eedabb-79de-3474-af39-29d71cb4b42b | -6.747 | -55.065399 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b13b8b-afc1-39bb-a211-0dd47252f13a | -5.9973 | -55.674599 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84300520-78cf-3b27-af2c-50685d0beb53 | -10.4593 | -47.240101 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e149fc6-c421-3a0a-8668-e53dd5d27180 | -2.4851 | -56.089001 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fabcce17-d728-3df3-a486-94040ad3464e | 0.791 | -59.188599 | 2026-10-08 00:26:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 234c15e5-9c3e-3251-856c-e26685b6ac81 | -2.9426 | -54.053299 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35331069-d249-3da5-ae95-9f91fc717c72 | -3.2727 | -54.008598 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c54b3e85-89ee-3fc4-b081-286782aa0e52 | -3.3032 | -54.052601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cddb825-a564-3ab5-b85e-562a4efc2a71 | -3.1082 | -54.146801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3daa1855-536a-31b4-84b5-511ba5fa6271 | -4.2703 | -54.863899 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ce7051-3208-375f-bf36-4087ec8dc5af | -6.2198 | -53.273899 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e76658-5e05-3a96-8c78-3e0ce6b5f04b | -3.5363 | -54.626499 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8b124f-5409-33ab-8ab4-0e62cdcc2fe7 | -3.4919 | -59.2589 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 604be0e7-6b49-316c-9494-e1ecc0e0a5e4 | -2.6027 | -57.575298 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3aff1e61-014e-3974-b579-79d047986749 | -1.5275 | -54.5424 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e3fca8-7014-31a9-9ce4-9e56d5457fde | -2.8514 | -54.196899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e528b414-bc79-3b11-9b46-f6059c50586f | -2.5028 | -56.121498 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b8fbcc-8452-363f-87b6-7bc787f4509b | -3.9946 | -56.250801 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4990aa0f-2f44-3ffc-81e4-2fb0a8abc287 | -2.8746 | -54.1628 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc79754-06cd-3d7d-9888-de4f46d75c61 | -3.0984 | -53.740601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96beb842-e908-37e6-82b0-9eafd5d26449 | -4.1197 | -55.0191 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3fa1d6d-d1e7-37d1-a685-96f9bae9904b | -2.9716 | -54.090401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f68707-b0d1-32bd-9658-97ed7e56de09 | 1.7739 | -55.5341 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48078163-ee24-3c9c-b019-317366ae581b | -1.4836 | -54.530499 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2149c89-4d6f-360d-bc0c-0526a5d4d691 | -3.1018 | -53.7103 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e07101a7-5884-3330-9393-1dfdcdfc27e8 | -6.4803 | -55.3008 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e332e84e-fe2f-3b7f-aab3-006fd2f56028 | -3.4381 | -56.938702 | 2026-10-08 00:26:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3843ccc-c618-39e1-90a3-04499cc54945 | -6.3429 | -55.3312 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0971f76d-35c3-3bda-94d8-a080834aa6e0 | -2.3218 | -57.974998 | 2026-10-08 00:26:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd64d25e-73f9-3e28-82b1-15df10c29895 | -5.8596 | -57.562199 | 2026-10-08 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28993b1c-f292-3734-8ec6-9d5d575ed107 | -3.4759 | -54.632801 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6402a2a-1da2-3ecb-8880-364a0cc69f80 | -4.2806 | -49.077301 | 2026-10-08 00:26:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef111f03-51b0-3561-a1f7-d02a6786558c | -1.2838 | -56.9767 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f2ce122-c4ab-3c81-a291-5300aa3df3f7 | -6.2169 | -52.8531 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072dc02f-55fe-35d3-afac-423992a7d7a1 | -2.9928 | -54.092899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ec0b635-2b30-3163-9279-4e9db81f4058 | -14.9174 | -48.097099 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 247043df-c5fa-3c59-800e-ddff2d8cab9a | -6.0908 | -49.4161 | 2026-10-08 00:26:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b849df4a-cac4-3ec4-a456-793538ea9d98 | -3.26 | -50.3979 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8352c4ee-e90c-36a2-8ccb-10e0c5d424e9 | -3.0505 | -54.029202 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9a8aec0-ff22-30a7-9b14-78b2ed3d1ccc | -6.5137 | -55.4044 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8d5ecde-f94f-3e0a-8879-b38ee530156e | -3.0207 | -54.079399 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4843836-81b3-38ce-a878-849a77979eba | -6.1827 | -53.428299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d57768-2514-3d58-8206-58bd07eb1587 | -6.1296 | -53.0588 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c22d01a6-be00-3507-ab38-9cf4dafd79ac | -13.7897 | -52.790901 | 2026-10-08 00:26:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab8242e8-f051-3302-9f2d-6788bacf81e1 | -3.2223 | -53.3787 | 2026-10-08 00:26:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244ae1af-4e0e-349f-9acf-4e0990f8ed4f | -3.0161 | -54.742298 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cad9c51-d0a8-3467-bc7a-39dab9de4f7b | -2.8612 | -54.194801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 306f075f-a251-30cf-8598-d01004f6f0d5 | -3.5474 | -59.4627 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98d0b27b-675e-3434-8c88-e782ec421822 | -3.2102 | -53.869499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748b03b8-7a18-3d61-bc8e-9abcc1e16263 | -2.95 | -54.1315 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57b92929-f41f-3563-a677-7c8dbd30cccd | -6.2429 | -52.877102 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c77bbb88-e134-3421-ab3c-eee2038faa9b | -2.6578 | -52.575699 | 2026-10-08 00:26:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58316c59-beb9-32b6-adeb-f97c786dce26 | -6.1081 | -55.7099 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ffd5324-0b5d-3349-a0b3-107cc21efa41 | -2.5008 | -56.1586 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6178de7-a9d8-36cb-97ab-72ca8d845781 | -3.0182 | -54.159698 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7ec3b8-1de0-39cc-8ef6-f1b8c4ee4cac | -3.7354 | -57.117599 | 2026-10-08 00:26:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2e84f6b-cdfe-3c85-9296-f42e4c4c0b70 | -2.9912 | -54.085999 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfd67490-e73b-3455-a4b5-1e9db5a21067 | -6.623 | -43.7323 | 2026-10-08 00:26:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12d288a1-61a1-3b84-bd40-4b7e9b126e3e | -2.9999 | -54.033199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e873368a-8b5b-3041-9b3a-0c13bc6f499e | -3.0006 | -54.127399 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70b7ad4a-b97e-3b86-828a-03bb272f2d31 | -1.4677 | -54.6423 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cdf87ba-e19a-32bf-ac3d-18dc2c5033b6 | -2.9328 | -54.0555 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0bab265-8768-35cc-8a1e-f9b0f563cc03 | -7.2327 | -55.119499 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd2555bd-13fe-3378-a5f3-9f761f9f0084 | -3.5778 | -54.308899 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa3f2dc1-e632-3ecb-945b-ad35eda75ba1 | -3.4842 | -59.455601 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aac2b8e9-14e4-3b91-ae8d-55039b231ebc | -2.8739 | -54.888302 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c473289d-1657-3b12-8fb2-789bb101c2fc | -6.3137 | -43.3563 | 2026-10-08 00:26:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 679fceda-cc79-3acd-ad23-8bbb119fc21c | -3.5864 | -54.665501 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b75225f-3db7-39b2-8482-1c4eb00676e3 | -2.8036 | -54.077 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf1e5c8-de5b-36f8-bd72-3a15576851d0 | -6.0884 | -49.405899 | 2026-10-08 00:26:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbd46f60-94ec-3127-aa05-924997c10802 | -3.0484 | -53.883801 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18adbc8a-c9d1-3191-b9df-e9fe5767d1d6 | -9.285 | -50.319599 | 2026-10-08 00:26:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f839a5b-66b4-313c-b288-ae55be375fb1 | -2.8829 | -54.153702 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
