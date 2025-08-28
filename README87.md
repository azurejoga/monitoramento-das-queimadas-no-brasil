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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05c90a7a-7eb8-3532-854e-8fb17461e878 | -11.361 | -63.278 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aade9570-dfa6-3dd4-b71e-eb28c2c9ff7c | -9.54545 | -68.57819 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f37314ea-b01d-3b60-8de7-8e1d08b7b987 | -10.84196 | -60.80952 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5341a690-7961-37ce-bb58-43696c370722 | -10.37213 | -62.56139 | 2025-08-28 05:50:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1308e088-ca78-32be-b785-cd4aafca5546 | -10.80169 | -60.76657 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9b71e134-e59c-3581-a806-c9949d985528 | -10.79639 | -60.77082 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6d970591-ba2a-3284-9a11-c7d95ffff782 | -10.80103 | -60.77147 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5229c2c1-c6ed-33c1-960a-7119a05a1726 | -11.35562 | -63.27942 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df46592d-1850-3bb7-ae20-aa254cd440a3 | -9.54212 | -68.57765 | 2025-08-28 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c25e4ecc-f3dc-34c9-bf3e-930e8c0f75be | -10.25354 | -64.49419 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b823f4b5-7cc4-3927-a8b6-5d26b98a34eb | -10.82031 | -60.76904 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a9dcd10d-f66d-3b57-a3f6-22299bcab151 | -11.35704 | -63.27742 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 141811c9-486a-3e6a-91e5-ac4dcd369a3e | -10.28329 | -64.49431 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 015be00e-ed69-34c2-a55d-83f23018bd6d | -14.3203 | -60.37292 | 2025-08-28 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7a873a9-dbb1-3ab2-b835-217025347c78 | -10.81034 | -60.77272 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2f4a680f-327a-38bd-979b-081cd1f1aab1 | -10.15509 | -64.24738 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 13acb51c-eb0f-3565-a52d-17e11553ffe7 | -10.19091 | -68.42902 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b6e4255-bd83-3642-be12-7bcf5907ee20 | -11.35959 | -63.28 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cfcb351-c2fa-35a1-b5fc-ca72ab672c58 | -10.79174 | -60.77017 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a76def1d-ce71-3902-afdf-e6e4d1ecee4d | -10.81499 | -60.77334 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9907eae-00c7-3ef0-946b-d6b513167e6e | -10.83668 | -60.81374 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b17329c3-a826-3b4c-aaad-9bbd53eaed34 | -11.71374 | -63.66255 | 2025-08-28 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d24146c6-95ee-356d-be41-24e0b64cb25e | -10.46961 | -68.15068 | 2025-08-28 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 945d1bb9-0476-346e-a5ac-ecba1fa67a75 | -10.80568 | -60.7721 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4988741b-ce33-3691-b2ef-8bac02676077 | -13.01437 | -56.89728 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 527d35f6-e0dd-3ccc-922e-972cd4911e00 | -12.22636 | -64.23104 | 2025-08-28 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3461caf0-21d8-33f1-9ef8-5c12c2512671 | -10.27965 | -64.49377 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f896830f-ddb9-3055-b70f-02c5ba3b9e9c | -10.83732 | -60.80887 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5eb9f11-f582-3c59-9da3-97bdf8ce4c5a | -10.28393 | -64.49 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60878be9-c4cb-3fd7-bc54-38f6be6da0fe | -13.01492 | -56.89227 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6e90b3-f27a-3c8d-be4c-e99078741bce | -10.811 | -60.76783 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b242c6ba-d8de-30e6-91d3-aee5350ed961 | -10.28029 | -64.48945 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ab23a06-0072-3f18-a5f4-6189c4ea9b3e | -10.83818 | -60.81135 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b6f1ae2-039f-34ef-afc4-6027847f17a4 | -10.29231 | -64.5088 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc2c960-6e68-31ab-9575-244029db7546 | -10.79239 | -60.76528 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 05262883-8603-3ad3-8cd4-48825164112a | -9.1153 | -65.8073 | 2025-08-28 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3ea8ed3f-e84f-34dd-bf88-0354d0b6ea9c | -8.3082 | -45.1566 | 2025-08-28 06:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f0536ddf-f692-3294-a304-a362bf2a94ab | -8.289 | -45.1814 | 2025-08-28 06:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 935af9fd-3154-378a-a9c0-a8047ea85d19 | -9.1155 | -65.7699 | 2025-08-28 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| d05809e7-5d91-3f0c-956e-801a4a0e1472 | -9.1154 | -65.7886 | 2025-08-28 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 248.6 |
| 76541af3-cf0b-3563-b22f-68c6275c28e5 | -9.1339 | -65.788 | 2025-08-28 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 175.3 |
| d4773654-567d-38ed-a3d0-19969b290b06 | -8.2893 | -45.1586 | 2025-08-28 06:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 30bc2918-2b96-34ec-9feb-c3cc5803e873 | -9.134 | -65.7694 | 2025-08-28 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 505c65af-9b39-3f42-a296-e051665b831c | -6.8772 | -43.6152 | 2025-08-28 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 61bf4ef0-930a-363c-884f-70bb70d572f9 | -9.1338 | -65.8067 | 2025-08-28 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 14069947-6fdc-33d6-b772-fe89ccc18968 | -14.3485 | -53.3504 | 2025-08-28 06:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b50a40e2-5c45-3a36-9685-1e724e357ab8 | -10.4738 | -57.9366 | 2025-08-28 06:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 06c0d59f-7b05-3260-8480-397c59a2a478 | -6.896 | -43.6135 | 2025-08-28 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 3af0b4db-2d72-36a5-ade2-d62aa622e70a | -9.1339 | -65.788 | 2025-08-28 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 201.7 |
| eddd1156-efb5-3807-96fb-7ff35278e965 | -9.134 | -65.7694 | 2025-08-28 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 9891694f-9f13-32b2-894b-d772b111b5d8 | -8.3082 | -45.1566 | 2025-08-28 06:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 9374b166-362b-3bc7-9ad2-ecfecc35051a | -9.1154 | -65.7886 | 2025-08-28 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 231.6 |
| 810c0d27-d045-30fe-bb78-b84a5aca773f | -14.3489 | -53.3294 | 2025-08-28 06:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2b9ee338-4e7b-3b4f-8c69-281a3c4fd0a0 | -8.3085 | -45.1338 | 2025-08-28 06:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 8fdfdbce-fe0f-35a6-83b9-236c04976c48 | -8.2893 | -45.1586 | 2025-08-28 06:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 329c431f-b40d-30f1-9768-c1f06b082eb3 | -6.8772 | -43.6152 | 2025-08-28 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c7337498-1066-3950-acf4-b7dafa9a424a | -9.1155 | -65.7699 | 2025-08-28 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 43626097-b8a6-3af0-b8cf-c948b17d0009 | -6.4355 | -44.5764 | 2025-08-28 06:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ccf34a02-2fd6-3835-b92a-c35ebe999fc5 | -10.4738 | -57.9366 | 2025-08-28 06:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| dbe9a871-0c18-31d1-b22c-7310b200f54f | -14.3485 | -53.3504 | 2025-08-28 06:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| aeb9cdf9-59bf-33b1-8253-2732297c40f8 | -6.44606 | -44.57305 | 2025-08-28 06:14:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 964f28a4-1fa4-3be4-bea5-353f9f9c1c70 | -7.23833 | -45.4255 | 2025-08-28 06:14:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| eddcf857-b7cb-3b50-9a5d-b2d30106f822 | -4.79875 | -47.25573 | 2025-08-28 06:14:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 91e4d74b-e4c0-3366-83bc-913bd957c820 | -6.4359 | -44.57869 | 2025-08-28 06:14:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1186540b-7d64-37e5-b246-366bbf8153ad | -7.22972 | -45.41719 | 2025-08-28 06:14:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a8518c68-9eff-3ddc-8de9-d25873fa0594 | -3.76654 | -54.81032 | 2025-08-28 06:14:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 3ff16c3f-f2ff-3bec-872f-512486a4aa31 | -3.75476 | -54.82058 | 2025-08-28 06:14:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9f532922-8c7d-3368-8b0f-d7a49854f79e | -7.26323 | -45.33971 | 2025-08-28 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cec095a5-3c08-30a2-adbd-4056ed504209 | -7.23544 | -45.44748 | 2025-08-28 06:14:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 36d1ef22-0a5d-3074-82fb-347a08ad92a3 | -6.88333 | -43.60565 | 2025-08-28 06:14:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 11225544-6793-3288-abe6-6d35b705cf47 | -7.22659 | -45.43978 | 2025-08-28 06:14:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 061f1cb2-bfcc-3871-8153-f644eeb1120e | -7.26033 | -45.3616 | 2025-08-28 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 66d7f1ac-3e00-391c-af71-f4fc372ec447 | -7.25219 | -45.35328 | 2025-08-28 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| afe93188-215a-3677-b760-1cbeca59840a | -5.31611 | -55.87754 | 2025-08-28 06:14:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cc2da160-6222-3ae2-bedb-c7c91b5a0f1e | -3.75657 | -54.80895 | 2025-08-28 06:14:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 31651253-6151-31e5-8e9a-bc4fc04b940f | -6.43913 | -44.55413 | 2025-08-28 06:14:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 656a8467-7514-395c-83a5-6046c57a65c3 | -6.43206 | -44.57072 | 2025-08-28 06:14:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d90333ae-1961-3c70-ae58-1e7f80b40731 | -6.86807 | -43.60333 | 2025-08-28 06:14:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| d7ead645-2875-3435-a59f-6fbcf2188d23 | -13.63053 | -48.23634 | 2025-08-28 06:16:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 49669a44-b214-3331-b054-791e0b2eb5b2 | -8.29113 | -45.17118 | 2025-08-28 06:16:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 702915d9-79c1-38a0-b036-5ad756648653 | -10.4702 | -57.94829 | 2025-08-28 06:16:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| e034b3b9-53be-3eea-81fa-4fb60e72fe17 | -8.29423 | -45.14722 | 2025-08-28 06:16:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 268.5 |
| da5f2271-0625-39bf-969e-23ea829aec11 | -11.21696 | -55.0559 | 2025-08-28 06:16:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 30ae04a4-3e57-32f2-bd82-5594e093a4c7 | -10.46769 | -57.96329 | 2025-08-28 06:16:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a4544368-1fb3-390e-903c-bb46dad587bb | -12.96401 | -44.55361 | 2025-08-28 06:16:00 | AQUA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 42d726d0-e82e-3ced-9d2b-b28d2c0e8b1d | -13.42996 | -46.95043 | 2025-08-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cd2919d7-59fb-36f4-82ed-e10d038a02c0 | -12.80371 | -48.155 | 2025-08-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5330cfb1-bb83-3d91-bcc6-c77af16ce90d | -9.40335 | -60.56923 | 2025-08-28 06:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 23ea3255-1992-36c2-976c-9b91b42270cf | -9.66276 | -48.30273 | 2025-08-28 06:16:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a6f866fa-a533-3990-9ca9-cbd0dd26a618 | -10.47268 | -57.93345 | 2025-08-28 06:16:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d45940bf-cf78-39f4-ada4-9d9150935ddf | -13.41736 | -46.839 | 2025-08-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| fbfc4828-578b-31b7-8a14-70527fd71953 | -14.28818 | -53.03841 | 2025-08-28 06:16:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| becdb5ff-2049-3d79-bcb5-4f7fac15b1a0 | -8.28759 | -45.14139 | 2025-08-28 06:16:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 3ab324d6-8717-3415-97f7-6cc81ce85f31 | -13.61893 | -48.23353 | 2025-08-28 06:16:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e5ce9a20-7660-37e2-a9a5-5ee8707ea209 | -10.49401 | -51.58649 | 2025-08-28 06:16:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ffe752bf-a14a-36c3-a089-125e6989259a | -10.47516 | -57.91862 | 2025-08-28 06:16:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 641a5183-2416-3e7a-a8f1-3e9b415d669c | -12.99742 | -56.897 | 2025-08-28 06:16:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 85a3c164-8bcc-37b1-a397-d962f7cd90c8 | -14.29087 | -53.02002 | 2025-08-28 06:16:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 656e0864-3daf-3dca-ac02-de397749d5f3 | -10.31716 | -46.77156 | 2025-08-28 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 17b3d415-085f-3730-9e77-ab1912cdaeb9 | -8.28435 | -45.16518 | 2025-08-28 06:16:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |


[Clique aqui para ver as próximas entradas](README88.md)
