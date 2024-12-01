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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0ae2924-805a-3bea-ae90-1faf17e44036 | -2.84086 | -54.03255 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fac8719-5c83-3f07-bfae-29e10dd59e83 | -3.4946 | -53.83382 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 589f4508-c292-3108-bb12-9aebcc5c733b | -4.52865 | -45.70207 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e06ebcf0-78b6-3562-a821-adaeb23a9904 | -2.98936 | -53.35435 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9943682a-feda-3b39-b65f-e29111cb84b4 | -2.78472 | -51.66789 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2254aaf-aebd-3693-91b9-83a14c7fb8d7 | -3.51333 | -53.78345 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8266c741-dcb3-300a-9c43-8ffa3de95d07 | -3.09656 | -54.04531 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5a2bfee-d3f6-30dd-bd67-b3c0283f3226 | -3.32075 | -50.03478 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a15065-6286-3057-b3e4-2166cfb21526 | -2.98151 | -53.28469 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b733ff8-bef8-3fde-a70d-63285442231b | -3.25544 | -53.62283 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 368d8f44-ba8a-374e-9592-debfcaf95f4b | -4.15762 | -60.88816 | 2024-12-01 05:08:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65ede06b-d600-3c97-b86d-7cb066f609e4 | -2.74418 | -54.08077 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7363ded9-70b1-3b35-87b6-e54e3c3a6fc6 | -3.74298 | -53.39102 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa20446d-187c-3eaa-9606-1d6edf560e02 | -2.91467 | -54.11736 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd6a6e86-6c17-3cd8-9fca-fce48eae9338 | -1.44907 | -54.52317 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28752ac1-2199-32fd-a4c2-7449e2df1161 | -1.39568 | -53.64988 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3739d8b1-8d6a-3c98-99d4-44294befbe7f | -2.87291 | -46.80007 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a328582-16ad-383a-a9f9-4501ac9c88b7 | -3.44087 | -50.12499 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0e6a8c1-d2c0-351d-8a2f-9924c9123b0b | -3.49414 | -53.81342 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d46b9189-63db-3103-9c92-d70f84e59a5f | -1.59281 | -52.53751 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9eedd106-9cda-3bae-8d42-9600704bb007 | -3.11172 | -53.75806 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd6dc9f2-4f11-301c-a6c5-fdcbdd2093ab | -2.36138 | -53.86286 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e0cb887-4a5f-34a2-a70f-f090502c837f | -2.97124 | -54.4509 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1031e9c3-14a9-31a3-8be4-16510c930153 | -3.24968 | -53.92009 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8ecfc8e-60a6-3dc6-a877-3ad2520ad3b3 | -1.56129 | -53.51418 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d074b3-e191-3350-915b-e39f4364d1e8 | -2.86208 | -54.04234 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d38a885-a249-3d97-80a5-3feeb1f4c005 | -0.18417 | -60.67762 | 2024-12-01 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0618955-d34d-3feb-9033-00a8ce109f2a | -2.75975 | -54.1184 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7354a1e3-c012-345e-9611-a93f798e1a66 | -3.24555 | -53.92344 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 259f6d06-5b7f-3f94-8dd1-30840abd001c | -2.85788 | -54.0929 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdff200c-4378-3354-b840-f63e68e77078 | -2.52787 | -54.07568 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb3696f3-c0fc-3fab-9721-5a447a8fcd25 | -2.21538 | -50.4463 | 2024-12-01 05:08:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37c2013a-d52b-3bf2-a9b6-cff616e8c23d | -4.0627 | -51.06692 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6057779f-9c14-3ad7-abb6-28aadc16f1d6 | -3.18205 | -45.35372 | 2024-12-01 05:08:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1261518a-fdf6-3f24-8989-bb589c907d0d | -2.88908 | -55.23013 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 945363a9-57e1-3b61-aa6d-fc3f3233e24f | -2.91175 | -53.99849 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f373128-58e1-30b9-bf23-956220eeb2d5 | -4.5347 | -45.70048 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccf2bc22-dc3a-3a15-a812-e757770ff211 | -1.42325 | -54.31041 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61c6acfd-4631-3498-8c5d-5ffe67feca85 | -1.64609 | -53.87204 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99cf97e-a0ad-3fd7-9935-d087f54e55fc | -2.02743 | -52.08113 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2cee664e-0647-3915-8fe5-009c667573e1 | -3.03047 | -54.1857 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eec043b7-1e3d-330c-aece-025a8f8968b5 | -3.9103 | -52.3395 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db518d56-3743-322f-99ce-2a454de74e79 | -2.77161 | -55.3317 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b24968f-99e9-3f62-8e6a-33b84c6adbef | -1.24927 | -54.55142 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e692eb5-7501-3140-a01f-afb8c8149380 | -2.83299 | -54.0826 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c23b1c-7a02-321e-8b7b-56acbbc89197 | -2.78646 | -51.6671 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b858fc0-49ab-356f-ad26-8c22caf04ab0 | -2.86979 | -53.99204 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f49c4f25-bedc-342f-9fc5-f3f14a8850ca | -3.09559 | -53.297 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8b0c0aa-a093-3633-91fa-5e5bcf41fc6d | -2.96504 | -53.72501 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 652fc8b5-9dec-3b53-8799-e6dd2b2612a7 | -3.71 | -51.67873 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 885f8aee-b862-3c2a-89ab-b484a87bcb45 | -3.49243 | -53.80096 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 711dd0da-c7d8-3078-baa2-c6aa61cb0bef | -4.0366 | -46.932 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d6381e3d-9281-39fc-ba77-fcd64d067933 | -2.65378 | -51.87341 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c8bc1925-4b7f-3103-b7b2-6d93d686cbed | -3.96375 | -49.90928 | 2024-12-01 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55681c64-218f-32ce-a77f-22c47d407834 | -2.04642 | -54.67266 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7efadfe-0012-36df-8f65-753c938e9905 | -2.60129 | -54.2807 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6d27ff4-e6a0-30b8-bc82-5c995794b675 | -3.09385 | -53.1367 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1ab0dca-112b-31af-8768-eca13193a6e3 | -2.80007 | -54.04213 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cd284e1-66ef-3482-9281-6a22b75fae0c | -3.0332 | -50.23883 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f506f35-9cc7-35dd-98c8-bb4326b3eebd | -2.57703 | -54.21593 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b82474b-5b5a-3c6b-9edf-97127e4952a1 | -4.76007 | -50.99469 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ebced82-8194-345f-affe-c5f7552a56eb | -4.00409 | -44.75761 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dc34c679-e7ff-3569-a5c5-bdefa7a65b0b | -2.5813 | -54.02946 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d13719f-835a-3363-be4c-b8cbd5e0234a | -2.44493 | -54.02419 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fc66102-d445-3689-b147-185020427ecd | -2.19318 | -53.7785 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072f9301-0d0b-3ce7-886f-751382ac3fe1 | -2.36396 | -53.6586 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cd2217c-9a71-3767-bf5d-8145e4dfeb2b | -3.21239 | -50.27345 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00414bbe-503e-30db-825c-0f9a81d01e97 | -3.51039 | -62.75718 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d505cceb-f863-34a1-b0ce-875dcbf2d6ef | -3.09374 | -51.40866 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683198e1-a380-38e4-8ea5-fe43aad0b652 | -3.29967 | -53.83096 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cf0de25-1f1d-3409-b2f7-9640b78d98b4 | -3.18914 | -54.33336 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a58c4950-a6d4-3824-bf95-86a53d951820 | -3.10938 | -53.10821 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 601a7eec-35fa-3ced-b8b9-74f3c50edb56 | -4.44425 | -45.36465 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4646f116-2baf-31c7-bd4c-a40cffeccf5d | -1.48272 | -55.38684 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63f7c133-1e6f-3bdc-acfb-ecd11612d1d8 | -3.39101 | -53.27039 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08c2cc1a-271a-3d17-96aa-cb375f7dead1 | -2.89608 | -51.58008 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 642bd922-29ee-31e4-ba6b-1f97dca94ea1 | -2.98384 | -53.29372 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10b396ee-a040-3356-824d-51b8a8f14b19 | -1.6251 | -53.89255 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb037146-c05f-3c6e-bff2-93eae7ff43ed | -1.64261 | -53.87153 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb1a71d-ba20-336a-a314-66db4a437aa9 | -3.09042 | -53.71085 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c064bcb2-9d22-3526-8e5f-5922d4319140 | -3.11671 | -51.31292 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33bc2bd2-3eb8-347f-8feb-1718a1200a86 | -4.54698 | -43.29446 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4637c22c-6c83-3a85-9a73-fdf9696b2ba9 | -4.07664 | -50.03115 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14062565-e688-3539-9aea-a79616d1f820 | -1.82288 | -50.89941 | 2024-12-01 05:08:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 67574d54-b9de-3f56-b4f2-dd8a31ff7c00 | -4.18957 | -50.68359 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 788ff125-5e41-3b64-8bdf-69440092aafe | -1.49247 | -54.45119 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c159dcf8-8b14-3048-8bd1-391ee120a9d6 | -3.9984 | -44.75138 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 41b6d432-7afe-3b5d-a818-f9731bf9b909 | -3.52271 | -62.85267 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68abf372-d81b-310d-8875-d83e09890f51 | -3.47874 | -59.4631 | 2024-12-01 05:08:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d84e820-9c34-336e-88dc-92bdb25e7b3f | -2.97456 | -53.87226 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 485be9f9-7e99-3075-a7c5-17571aebdcfb | -3.18389 | -53.25456 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bcd5762-f8f1-338b-a84e-78a94211b9e8 | -3.29499 | -53.67432 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c94f474c-3112-3886-8a92-14f2f605e836 | -3.25591 | -53.6437 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ef82e2a-8409-36ec-b1b0-fc34188aac71 | -4.07223 | -48.80465 | 2024-12-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ea59bcb-f247-375b-8781-5ea51db5e58d | -2.44126 | -53.88554 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e200b70-6a73-3546-91de-7aa5731ed2fd | -3.78783 | -52.40658 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0669a517-ab6f-3c6d-a015-e57696d34f4d | -1.60975 | -53.83129 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6e1d2d4-5c2b-38aa-8947-4e33cd1e5e36 | -2.86221 | -53.99483 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d465705-7717-35d6-b89d-30abb766c8a3 | -2.07123 | -55.01026 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 425160fd-d8b1-3922-92d4-8e8ebdf25203 | -2.80765 | -54.03933 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README91.md)
