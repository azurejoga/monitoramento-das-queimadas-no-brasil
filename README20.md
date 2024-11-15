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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 438d9c1a-d283-3f4c-acb2-ba2eb6fc3d1c | -3.22815 | -54.15741 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48f8c4e2-c0f5-3974-a3ad-5999ab2885a8 | -2.14329 | -46.40459 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe623ba7-7777-34c5-8794-fb0fa631546a | -2.45618 | -53.93712 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 408abc13-eb4b-33b8-a8ce-bc2bab7d2e4e | -3.54049 | -54.32907 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 889a28d5-8e2a-334f-8b2c-7fde83fc9cd6 | -2.66318 | -46.18607 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 333bdb54-6b13-3304-b1d5-e4aac36d6ea9 | -2.65259 | -46.17981 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ba1eaf2-b947-3e25-bcf8-a3764d3100bc | -3.88817 | -42.55228 | 2024-11-15 04:44:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ed4dc5c6-3d8e-3f9a-af01-63427694f40b | -3.68972 | -54.57621 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ff779a5-07a6-3225-8932-fb42006bbc6c | -3.12347 | -45.27266 | 2024-11-15 04:44:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abf5d0e9-e2a4-3dea-9f75-4efbd4d5be1c | -1.38017 | -51.56009 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5f41729-aa45-39da-9105-bc4ed219ffd4 | -3.7139 | -41.69245 | 2024-11-15 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f6937e6a-44ab-3df1-86a9-3a72f8bf5694 | -3.2796 | -53.01184 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2871508f-ff6d-3a77-9b9d-68d4396b2309 | -3.79485 | -43.91002 | 2024-11-15 04:44:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 74e7a3b9-1054-31e3-a053-df71eb2d251e | -2.34159 | -47.21833 | 2024-11-15 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f410245-9f4e-39a1-aade-65d9a251a6d6 | -2.6474 | -46.18833 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fa46361-b35a-32fb-bf73-cd82894376e5 | -2.38295 | -54.64271 | 2024-11-15 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 182ae95c-3d9f-31e0-8616-0eb273fb2d25 | -3.12268 | -45.27292 | 2024-11-15 04:44:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aac6018a-ecf6-345c-965f-cf6040882de5 | -1.98269 | -54.16827 | 2024-11-15 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f3a7dec-ffd9-3970-acf2-a5d9b1da2b5f | -2.63303 | -46.18152 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e37800b-4767-398f-a952-0a66d3adb6ca | -1.75669 | -52.67496 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0909c331-cf4e-3580-8d73-45a9fbf5e817 | -3.53297 | -41.84177 | 2024-11-15 04:44:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60da2c29-b0ba-3aa6-b3ca-d9cce6b1cd8b | -2.64292 | -46.19229 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6149032f-3390-37bf-a835-82a63470a72c | -2.63162 | -46.19059 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6e6e754-cc49-3b59-928f-2e5ae552d69e | -2.18605 | -46.15346 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db9a5ea4-a968-32af-8993-7dcb09f01c31 | -2.38455 | -54.63266 | 2024-11-15 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2760704-9584-36a8-b348-f3cc99725783 | -2.66074 | -46.1787 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca021070-6d2a-36be-bb41-dbb344cd5d41 | -3.08419 | -53.25821 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2489519-24d4-317f-a4ad-65d2163264e0 | -2.31317 | -45.06505 | 2024-11-15 04:44:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1427648f-30be-3d3c-b4e1-8b319f921792 | -1.57839 | -53.80096 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08041a0f-9793-3835-ae6c-a0e719697f56 | -2.23323 | -46.83665 | 2024-11-15 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09b2c0cc-ef8b-366d-b5c1-34f5be59b28b | -3.42412 | -53.97109 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e824f6b6-e09b-3adc-9ff4-f8f79880aa73 | -1.70396 | -52.67199 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e813a53-8dcc-3267-95c9-137d644c9445 | -2.6533 | -46.17526 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f479a68f-0be7-3c06-a82d-651d3eb133b8 | -2.57906 | -54.22263 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bb1df20-4183-379a-a469-4dff30f827bb | -3.23423 | -53.62057 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b480da9d-1bee-3af2-92c0-ca209de0ffe0 | -4.51417 | -44.07142 | 2024-11-15 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c387f9f-b8d9-3921-8524-74e533fda138 | -2.09613 | -46.33169 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff94a57f-ab96-3c11-ab6e-e6812d1f050b | -2.66314 | -46.18836 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c88e12-dec6-3225-b0d0-ffc8430fe9fa | -6.04436 | -44.03938 | 2024-11-15 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b9dfa4c-1311-3d67-9059-a031102a80f4 | -2.90474 | -46.85352 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1990a20-a467-327a-9f36-635e84127705 | -2.61781 | -54.919 | 2024-11-15 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e07b8abd-efa3-31f8-9204-db728a8d0350 | -2.34515 | -47.21887 | 2024-11-15 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 931e4871-3aed-3123-8793-3994ca89c465 | -3.2388 | -54.16378 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5bb2063-170f-3a84-9947-564b8230eec1 | -3.70873 | -41.69165 | 2024-11-15 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 966dd6d0-8b97-3fa5-8d9f-23e0f0725a78 | -1.43219 | -55.39027 | 2024-11-15 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04a58597-3f12-39dd-b046-558ca1da855f | -2.38427 | -53.66547 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 346b2368-e2d7-3a24-b9bf-06c13c4fdc18 | -3.19257 | -53.99345 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78157cf0-3e8d-39fc-964c-6aeb502c12fe | -3.10136 | -45.97279 | 2024-11-15 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f52e6e63-bfb8-3cd6-9ef1-4e1ceb6e9773 | -1.38906 | -52.08335 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e6fc628-1e4a-34c3-be30-1c8285ed43c2 | -3.55406 | -54.57632 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00480ec1-da88-3e1b-b020-c05b3068acbd | -2.66013 | -46.18096 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31aee0ad-e97e-3fee-b346-4eb062b17768 | -4.05641 | -55.79264 | 2024-11-15 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00cf99ad-4fc9-3448-af38-fd7a9294b8cd | -2.43636 | -46.28602 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c313151f-8f72-35fd-b599-bcd04976ba5b | -3.15381 | -53.23964 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4e9981c-30b9-30c0-9652-e13e0b7877fc | -2.65629 | -46.18267 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa6f2ac7-bfa8-3661-ac2f-54f69813ac8b | -1.57595 | -53.79837 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f457975-f094-3184-a346-9abd0c87c633 | -3.25601 | -53.6725 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86f53353-77c6-3b58-9140-6f68398c249c | -3.88808 | -43.14918 | 2024-11-15 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2286f738-9e25-3669-91f4-291f8c2687d1 | -3.62637 | -54.79562 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06a46db9-06f7-3a81-9858-d9a55536eeb4 | -1.38244 | -51.56798 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1fb5f6d-dfee-3d99-afdf-8e14a5e26045 | -2.61903 | -46.82357 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4814da0f-8570-364d-8e83-318ffa9283df | -1.56341 | -51.85709 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de96e311-b32e-35ae-8706-8c46043a21d1 | -3.14362 | -45.16522 | 2024-11-15 04:44:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78ece7e1-4015-3d8a-8234-01d7994643cb | -2.65766 | -46.17355 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c944e086-37b7-3693-b051-98d3d1fde7aa | -1.8711 | -54.68323 | 2024-11-15 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5b5ce6e-eee9-300c-958d-ac9548939ba8 | -2.65493 | -46.18946 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b07b954-4b2b-334e-ac2b-f4361a568c72 | -3.81507 | -52.01722 | 2024-11-15 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf1bb97c-2adf-34d9-9c36-00f8c2a62427 | -2.60197 | -54.04251 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d8ca0ac-f49c-3d97-bc81-9a5d328d73b9 | -3.42786 | -53.97165 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 705f8e76-544b-3c4a-8cf8-e850e03b0095 | -1.55936 | -51.86031 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9e0a3d3-d0d0-3239-8d81-782e915a2fc9 | -3.27896 | -53.01588 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e13352-3009-3d02-bba5-fb451fa1a7fd | -3.96754 | -49.9933 | 2024-11-15 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f052e84a-4d18-3736-bafd-4344858c39e6 | -2.65697 | -46.17812 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3842467a-ecfc-38a8-8596-eeac23a24c1c | -1.55996 | -51.85656 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d1a0087-d6a2-36c5-b8ed-e757d83236d4 | -3.88267 | -43.1534 | 2024-11-15 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c85ec7a6-4abf-32a9-95b8-83a6a08710d8 | -3.14364 | -45.16475 | 2024-11-15 04:44:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 917bc8f6-0a98-3805-8f5a-a13022443395 | -3.12295 | -45.27614 | 2024-11-15 04:44:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54ffbd7e-de5e-3fde-b92e-b3f5496d55a8 | -3.61604 | -44.79096 | 2024-11-15 04:44:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44daf7d1-e34d-3e3b-bc59-6db0c036a04d | -3.5494 | -54.58057 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29fb0197-44da-3a77-a310-36c7fb9eb3e7 | -3.23817 | -54.16188 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b842a1c9-8ecb-3f4c-bb9f-940ea2cfedc8 | -3.53977 | -54.32649 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60805f4f-24d3-3bb5-9db8-c6dcf76dcea5 | -2.65095 | -46.16562 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14162b94-71a3-36cc-bda4-cabc120582fa | -3.88623 | -43.15238 | 2024-11-15 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 447f1a70-884a-3e29-89e7-8edbbe9e4c4c | -2.33804 | -47.21778 | 2024-11-15 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e316f1ee-8d85-3f7e-bfa3-73a8224cdf6a | -2.65024 | -46.17015 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db330552-5a7b-3d29-b53c-db0858eecc57 | -1.57524 | -53.80294 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4bffb8e-7f26-3e16-93e2-083fcccd8e4e | -2.65422 | -46.194 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8b459c9-ca0d-380e-8b01-8731add10e2a | -3.08951 | -53.22535 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3dfb09d-bae7-33c1-8f43-f6acba400332 | -3.43234 | -53.96769 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32c9eb51-3226-3a14-907e-01c8a0a65af7 | -3.23056 | -53.61995 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 206f9de6-bcd6-3d51-a26a-bc1a8210907b | -3.55483 | -54.57154 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c3a0fde-ac41-3d06-a6a1-c25c05ed319e | -2.63986 | -46.1872 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30563124-a9f5-377a-96ef-60b8ca30ca85 | -3.43161 | -53.97221 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6329fbc-f402-3316-b870-db2241959d74 | -1.98498 | -46.36376 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| abc2c75a-db2c-304b-b990-e651ba2f663c | -2.72412 | -53.19795 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfbcbe29-24ff-35d2-a5e6-26613860bbb6 | -1.3796 | -51.56376 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92a4629b-2908-3d39-b02d-f2d4a690f385 | -4.10299 | -38.74042 | 2024-11-15 04:44:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 48284823-7037-3c82-9d29-f4b9ddb095b5 | -2.70975 | -44.77658 | 2024-11-15 04:44:00 | NPP-375D | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28ac36ea-93a5-33f0-8579-8a63d623c3e4 | -2.16592 | -46.15948 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91f29fca-7c35-3d31-9e82-eea7db19fba5 | -3.31315 | -54.17912 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
