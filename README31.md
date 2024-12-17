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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa1f2c58-338b-33c2-9d4a-7df39d76201e | 4.4618 | -60.9842 | 2024-12-17 06:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 74df7bba-9922-311c-a97a-122c23f14913 | -6.9346 | -43.5168 | 2024-12-17 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8e0fcdeb-a6d4-302c-bbac-ec47d095f569 | 4.4435 | -60.9846 | 2024-12-17 06:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 9193a10d-6bac-38be-aee2-7f3475f5cf67 | -6.9346 | -43.5168 | 2024-12-17 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 816a2cf9-0a78-344c-9cb0-c4abd433de6f | 4.4618 | -60.9842 | 2024-12-17 07:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f103d573-e388-3740-b784-7aa0eba2f485 | 4.4434 | -61.0036 | 2024-12-17 07:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a3a8facd-b454-3cb2-876c-0475712f2da7 | 4.4435 | -60.9846 | 2024-12-17 07:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 131fa2a4-7587-3028-8549-3b3b167e1e6d | 4.4434 | -61.0036 | 2024-12-17 07:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 104.7 |
| cea566e5-2f76-347d-a560-811847ffc81a | 4.4435 | -60.9846 | 2024-12-17 07:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 140.7 |
| c30ecdaa-5462-3699-bd67-a01a38cd9d57 | 4.4618 | -60.9842 | 2024-12-17 07:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c93bc476-a079-3439-9e97-653149415351 | 4.4618 | -60.9842 | 2024-12-17 07:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d6e7030b-238a-3895-82fb-26ab4a77d5d2 | 4.4434 | -61.0036 | 2024-12-17 07:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f4921e3a-b277-348b-a99e-140f696bb3a0 | 4.4435 | -60.9846 | 2024-12-17 07:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 1c20fbe7-fbac-3974-a4d9-2c1259efdedd | 4.4435 | -60.9846 | 2024-12-17 07:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 92.6 |
| f032688e-a2ab-3e7f-99ce-664fa9d55e02 | 4.4434 | -61.0036 | 2024-12-17 07:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 884b4a74-f468-3f99-8813-ea5f04706248 | 4.4618 | -60.9842 | 2024-12-17 07:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1ab16371-8629-3a9f-82b2-636bd31b1cc9 | -6.9158 | -43.5185 | 2024-12-17 07:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 0b24bd6f-bedd-3544-ba30-2af6a52a1aed | 4.4434 | -61.0036 | 2024-12-17 07:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 37fd5ec5-2cda-3846-b3c4-a7359165232e | 4.4435 | -60.9846 | 2024-12-17 07:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0836afc7-e088-309b-90b9-06a15def6e0b | 4.4434 | -61.0036 | 2024-12-17 07:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 19968c2d-9770-3503-8622-e3b02045502c | 4.4435 | -60.9846 | 2024-12-17 07:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0ea17352-81e5-339f-a1ff-72e5652ac015 | 4.4434 | -61.0036 | 2024-12-17 08:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 78456d0a-3663-31fc-a8eb-cd01efffac0d | 4.4435 | -60.9846 | 2024-12-17 08:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 703f31be-fbf5-3bba-acc5-c48fa3845e6b | 4.4617 | -61.0032 | 2024-12-17 08:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 48f91185-d0ef-3533-a449-39a7f9af2568 | 4.4618 | -60.9842 | 2024-12-17 08:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fe912849-8317-3fcd-8f8d-4ace9ec6fd40 | 4.4618 | -60.9842 | 2024-12-17 08:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d3489883-5f9d-3fd1-8c8b-c20fc03e5b6b | 4.4435 | -60.9846 | 2024-12-17 08:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 34efedfe-0c8b-3fed-86db-58bcb30e1a08 | 4.4617 | -61.0032 | 2024-12-17 08:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| cbb002aa-7e5a-38db-8419-04ff711cc961 | 4.4434 | -61.0036 | 2024-12-17 08:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c7624f4a-d8cf-33e6-830a-a469478c7a22 | 4.4434 | -61.0036 | 2024-12-17 08:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6a072ccb-3168-3aec-8d16-af3803fcb6bf | 4.4435 | -60.9846 | 2024-12-17 08:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| c4305413-c79d-3039-8863-bd921aff1b84 | 4.4434 | -61.0036 | 2024-12-17 08:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 92.3 |
| f9d6c8e9-3937-3374-99b1-36b8673661e1 | 4.4435 | -60.9846 | 2024-12-17 08:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1f88451e-944d-387e-b5bf-6d51753515f4 | 4.4433 | -61.0226 | 2024-12-17 09:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a7dc2f97-6883-3355-982b-e8613889de29 | 4.4618 | -60.9842 | 2024-12-17 09:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 8bb749ed-32c2-34ae-b6bd-804239123c89 | 4.4434 | -61.0036 | 2024-12-17 09:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 199.1 |
| e90812c2-36a2-3b86-868e-2c94f41a6baa | 4.4617 | -61.0032 | 2024-12-17 09:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4a0ae0ee-4434-331a-b972-d8655657307a | 4.4435 | -60.9846 | 2024-12-17 09:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 112.3 |
| b82d2ba0-d8f0-3963-909b-5f7528480b51 | 4.4434 | -61.0036 | 2024-12-17 09:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 118.6 |
| df1f5998-d90d-3cf2-b8fe-d37f7934a87d | 4.4435 | -60.9846 | 2024-12-17 09:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2060c316-2973-3eb5-a2b7-3aa691bdfe26 | 4.4617 | -61.0032 | 2024-12-17 09:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| dca54d08-855e-3462-abb5-76d51ab37978 | 4.4433 | -61.0226 | 2024-12-17 09:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 33208ead-20c0-3695-9ae6-b74155c10a2b | 4.4434 | -61.0036 | 2024-12-17 09:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 5d3e940e-a6e8-3495-90aa-0c2f44783830 | 4.4435 | -60.9846 | 2024-12-17 09:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| e6d6783a-c76c-31d1-b05f-da2bfae535a5 | 4.4617 | -61.0032 | 2024-12-17 09:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9f5948c7-5c36-3d6c-b681-037082987687 | 4.4434 | -61.0036 | 2024-12-17 10:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 5a39b701-2402-388c-bcab-984372d10ad3 | -6.961 | -42.8344 | 2024-12-17 11:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 8a57d976-4efa-3925-b3f6-501d9a374a08 | -6.9799 | -42.8326 | 2024-12-17 11:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| f3ca9082-6086-396d-97d8-ae1ef76448fd | -6.9799 | -42.8326 | 2024-12-17 11:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| f703cc3c-681b-3825-a6d2-da3478638811 | -6.961 | -42.8344 | 2024-12-17 11:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 6be2db83-592e-3b85-b99b-061af1ab08b5 | -6.961 | -42.8344 | 2024-12-17 12:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 57b6ef92-9ca0-3428-9b8b-0ffa3b46fbff | -6.9799 | -42.8326 | 2024-12-17 12:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| e050414b-74b0-3e22-b57f-59fdeba635ae | -5.48571 | -39.41078 | 2024-12-17 12:04:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 0f26ae1c-1c23-3927-9b47-ebf1eed8c7f9 | -6.74099 | -38.58263 | 2024-12-17 12:04:00 | TERRA_M-T | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d966742f-7cbf-333c-ab46-1a4c7ebf8b3d | -7.21944 | -38.40205 | 2024-12-17 12:04:00 | TERRA_M-T | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 285a5416-c153-35ef-a91a-b23d44e5c511 | -5.87089 | -38.28077 | 2024-12-17 12:04:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 5e767aba-dabf-3693-890c-127d73afc68f | -6.95393 | -42.81313 | 2024-12-17 12:04:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| a7084c29-c4b6-3fd6-868b-4c60d2c0c776 | -5.43403 | -38.56253 | 2024-12-17 12:04:00 | TERRA_M-T | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 52c7f7a7-0e5c-3370-955c-df0b9b670d5f | -6.96463 | -42.81467 | 2024-12-17 12:04:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 7a9d8a03-9845-3e83-bb8b-1029bf2d5885 | -7.509 | -38.82834 | 2024-12-17 12:04:00 | TERRA_M-T | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 9f2b4d09-6ef8-3c34-a6d7-105f1e16c8f0 | -4.54197 | -43.30066 | 2024-12-17 12:04:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| fd051e1d-b49c-3d35-a863-107b14a48472 | -6.63331 | -37.596 | 2024-12-17 12:04:00 | TERRA_M-T | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d0c3856c-a384-3591-8d7b-dbf53a7e17c5 | -4.81201 | -38.90703 | 2024-12-17 12:04:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ba3cdd95-97ec-3fa3-b7ca-1358b1b08976 | -4.55717 | -38.49358 | 2024-12-17 12:04:00 | TERRA_M-T | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 67e41dd2-7165-3882-ab35-a283f7d5cbbd | -2.90033 | -42.19547 | 2024-12-17 12:04:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| c006ca33-e97c-391e-87f8-4f6fbdbf705b | -5.95908 | -41.59163 | 2024-12-17 12:04:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 5c56c220-5d68-3368-818b-f30195e6a7a3 | -4.95001 | -43.99632 | 2024-12-17 12:04:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 339d09e8-8f65-31ff-9bf5-eec5c97bc8eb | -4.53576 | -40.76943 | 2024-12-17 12:04:00 | TERRA_M-T | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 157f57a4-9946-3d7e-baba-a0957abc68af | -5.6194 | -40.63577 | 2024-12-17 12:04:00 | TERRA_M-T | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f31d95cc-485b-31d0-901c-b0defe7f2ed4 | -6.28608 | -38.14823 | 2024-12-17 12:04:00 | TERRA_M-T | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 63a61d89-69b0-301b-bc97-58785a71dbb1 | -7.16605 | -40.97873 | 2024-12-17 12:04:00 | TERRA_M-T | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 548dd202-30a9-3776-83cb-5c1d6900c3c0 | -2.86356 | -42.04406 | 2024-12-17 12:04:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8f695aa1-f21b-3dbc-a33a-2ec27db877ab | -6.75396 | -38.3054 | 2024-12-17 12:04:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7aefe451-f6e9-3d3f-a2a1-306e85b959c7 | -2.89625 | -42.22325 | 2024-12-17 12:04:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 2fa767ea-1251-3941-8842-3e7145807342 | -4.99163 | -38.3074 | 2024-12-17 12:04:00 | TERRA_M-T | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 32c59ceb-935f-3b04-8d78-7ac708b31ffd | -5.98412 | -41.56661 | 2024-12-17 12:04:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 9eb459d0-3afe-3c9f-9f62-c4094389d377 | -4.55844 | -38.48477 | 2024-12-17 12:04:00 | TERRA_M-T | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bd3be2c3-6c81-361b-807e-d4b5e55b4ed3 | -6.5487 | -37.60585 | 2024-12-17 12:04:00 | TERRA_M-T | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 126374c1-371f-361e-9b8c-38ec48322691 | -7.50528 | -37.17112 | 2024-12-17 12:04:00 | TERRA_M-T | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 41a897ac-834e-3be0-91f8-bfeca9875c82 | -5.01515 | -38.5801 | 2024-12-17 12:04:00 | TERRA_M-T | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 86f53480-cc36-34fc-978f-094699006785 | -2.86643 | -42.05111 | 2024-12-17 12:04:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bdbc041b-2960-3cd5-bab0-c963a1e1cafd | -7.60993 | -37.47449 | 2024-12-17 12:04:00 | TERRA_M-T | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 22.6 |
| f1246f8c-0a47-30bb-b2a9-8dfcd0b134e3 | -5.73269 | -39.1091 | 2024-12-17 12:04:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| ada53ad6-2f74-3f3d-b29c-71cc8d4ba321 | -6.78663 | -41.27576 | 2024-12-17 12:04:00 | TERRA_M-T | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| a33f0a54-0f2e-34d0-a75b-b2771050bf22 | -6.23065 | -38.03217 | 2024-12-17 12:04:00 | TERRA_M-T | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 04493046-be58-341e-a8df-e4ca269e6e71 | -5.43942 | -39.60017 | 2024-12-17 12:04:00 | TERRA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 41.4 |
| f8b3b1b4-0218-3e6a-ae58-aa2e0c319547 | -7.41068 | -38.74533 | 2024-12-17 12:04:00 | TERRA_M-T | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 03b8dd2b-b58b-34a1-8544-057ef6d1a23a | -5.87921 | -40.62023 | 2024-12-17 12:04:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 927eb52c-110a-3bdd-9cf6-1944ff84cb74 | -6.26729 | -37.57555 | 2024-12-17 12:04:00 | TERRA_M-T | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 086ccb64-5767-307a-8557-e33943e96c2f | -6.21218 | -46.2304 | 2024-12-17 12:04:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| e565fe19-53f6-318b-8a78-743d0b1df1ab | -7.4977 | -38.7036 | 2024-12-17 12:04:00 | TERRA_M-T | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 23.7 |
| a9002e21-e6d3-3a20-83d5-41b3a412a4a8 | -4.10433 | -40.07802 | 2024-12-17 12:04:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b5fc2587-a514-3ad0-8079-74ad3166849f | -5.43275 | -38.57134 | 2024-12-17 12:04:00 | TERRA_M-T | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| acb28f5d-7b8d-3a86-ba30-32fa52ea23e8 | -5.44441 | -39.50077 | 2024-12-17 12:04:00 | TERRA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 38f7f755-5b23-3fea-928f-4f6a08957868 | -5.88614 | -38.17508 | 2024-12-17 12:04:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 24.9 |
| bfdf7783-36c6-30e5-886d-d4db3c4325cb | -4.90266 | -42.0716 | 2024-12-17 12:04:00 | TERRA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 718e6245-dd22-35d1-afa4-a1c0efbd5279 | -6.22938 | -38.04102 | 2024-12-17 12:04:00 | TERRA_M-T | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 8b2508ca-d04e-3e53-b82e-d6a639603411 | -6.30708 | -37.55991 | 2024-12-17 12:04:00 | TERRA_M-T | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 0e645da4-cff2-398a-a58d-03491b53ecaf | -6.9733 | -42.82967 | 2024-12-17 12:04:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 154.7 |
| 9ed80b35-8de6-3608-b38a-895a841444ab | -6.75269 | -38.31424 | 2024-12-17 12:04:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README32.md)
