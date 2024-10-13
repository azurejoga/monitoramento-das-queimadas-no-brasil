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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b09910e1-db53-3b1f-b7c0-4d343a51489e | -1.19569 | -53.38495 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6d0cdfa-eed8-3d8a-afd8-b23dba7d0f14 | -1.19511 | -53.38859 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e191893-5364-33c4-8bd6-afb2d279ea48 | -1.16642 | -54.19696 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1402fe19-88f8-3268-ab19-2a61762f7709 | -1.1633 | -53.40566 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce9db419-930d-3ce4-ad1f-94654c84c178 | -1.14709 | -54.09977 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14a98f48-f1f0-304c-8051-bd2a8ada01de | -1.14645 | -54.10371 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06b12094-0f95-3622-9fe6-1af5ad8945d5 | -1.14348 | -54.09515 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78f78423-8de8-3225-bb51-09b2e61613b1 | -1.14284 | -54.0991 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ec43938-9bd5-37fb-ab84-4427bdb2dc10 | -1.12221 | -54.17865 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c46f005f-bd14-30d3-8bc4-cbcf2ed8b0ee | -1.09294 | -54.16978 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16e0b008-2fb5-3c2a-b4af-4fd0a89bf17f | -1.02377 | -53.73105 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c128753c-546a-3ef8-916a-d426a35d393f | -1.01965 | -53.73022 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad09c3a2-5a6e-3628-b408-27ff040192eb | -2.25286 | -53.48593 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a677ab09-e09b-38f4-9bf8-ff4e812a10ee | -2.22142 | -53.68086 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71874cf5-9d05-320e-a93e-f11ded391c2e | -1.89168 | -54.62814 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1acd960-45e9-3195-9d35-d14cae52e4d8 | -1.72885 | -54.17815 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 121ea5f5-c9ef-3c89-8b1c-172cd5698e50 | -1.72822 | -54.18208 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 74b3c02a-63eb-37e9-98c0-021691fcf3f6 | -1.62961 | -54.77193 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e04221ab-3a74-34b5-b8b9-79d068c644d6 | -1.59858 | -53.34875 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f936922-9ce1-3c54-b3d1-f2eb3c087bab | -1.59457 | -53.34811 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 043d262a-d49f-383d-b019-95d0cc5d01a5 | -2.79004 | -54.01011 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e40ff6b-e234-3192-b95e-254188126502 | -2.78943 | -54.01382 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5fa374c-d55f-3fca-9677-0c1461fe917a | -3.06941 | -53.88629 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 57433580-649a-3cac-8382-987887a076ab | -3.29981 | -53.85641 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b16433c7-9e86-3ba9-a597-de279fcabd22 | -3.29634 | -53.85222 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05ea0e77-f6ef-3d76-bad6-6821397d9286 | -3.29576 | -53.85579 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75bb74ff-2b9c-3c97-aab5-42ce73bc7fce | -3.29287 | -53.84803 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b974c6fd-739e-3fab-acaf-1d18d755cee1 | -3.06588 | -53.88227 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d283a43-f0d2-3f48-8ec5-db715ea2487c | -3.06533 | -53.88571 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 771c1e56-63e4-338b-aa66-0adf09c65e8c | -3.00702 | -54.03719 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e9c4a6d-e34e-3ec9-9924-93fa15184670 | -3.00281 | -53.91176 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd623df-1149-3dfc-bd4a-f53253a107f0 | -3.00223 | -53.91542 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07bcba5b-13cb-373d-bfa0-7a3debc8340e | -3.00165 | -53.91908 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78578440-1534-3425-92a5-31d72339831c | -2.99873 | -53.91112 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e69aec-ccf1-3d0f-b105-62ed6c0c83ba | -2.99815 | -53.91477 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa6698b1-fcb6-3fff-a24d-67b90f6d9bca | -2.99757 | -53.91842 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7c1e88c-a08a-37d1-b48e-9830fad9ddab | -2.95703 | -54.1202 | 2024-10-13 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c47f460-3b24-36c2-95db-e90e9b15a847 | -1.23727 | -55.90352 | 2024-10-13 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8111706-df56-3018-91d4-395d29e664b2 | -1.94707 | -56.45488 | 2024-10-13 04:38:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9e9f8c2-486d-3fa7-9f04-9adc575606a4 | -1.94496 | -56.45861 | 2024-10-13 04:38:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c592d09c-aeaf-33c8-bd16-13ff21a34020 | -1.71707 | -55.14363 | 2024-10-13 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22161953-45af-3d1a-9ffd-0284a179ab53 | -1.68031 | -55.1904 | 2024-10-13 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8061ac17-1d89-312c-995c-ce6330d9fb8d | -1.67576 | -55.18969 | 2024-10-13 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d896f72-4160-3d2e-8548-0584119b282f | -1.655 | -55.08804 | 2024-10-13 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee145f13-9f2c-3b45-97a8-6858555053ea | -1.65426 | -55.09256 | 2024-10-13 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e269c753-e4bf-37b2-a21a-513fe68c3986 | -1.56249 | -55.89741 | 2024-10-13 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef546843-7d7a-3c2b-b134-e9412f21d86c | 1.13152 | -59.52727 | 2024-10-13 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65dc8388-9ac9-3001-9ba0-75eb09736b6f | 1.13075 | -59.52218 | 2024-10-13 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5235c30e-7895-3919-97e1-cb78bd8c91d5 | 1.12825 | -59.52468 | 2024-10-13 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bd932b04-e927-3bd5-af2b-57f36d279e4e | 1.12441 | -59.52313 | 2024-10-13 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a886a8d5-7c0b-3731-88b3-3c29be95ea5b | 1.12364 | -59.51805 | 2024-10-13 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de0ea595-5e33-3481-a56c-258375ae9be2 | 1.12111 | -59.52055 | 2024-10-13 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 63c31aec-dc9e-3967-9d30-179a0edb48bf | -5.32146 | -43.07527 | 2024-10-13 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 746e1a25-5f15-3052-a657-8405352acc0f | -5.1391 | -43.87731 | 2024-10-13 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46063b35-8632-3827-a4c4-f0645279d88b | -4.09135 | -43.91987 | 2024-10-13 04:38:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f08bf25-56bd-32ba-b886-b50406843b3b | -4.09081 | -43.9234 | 2024-10-13 04:38:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb0939aa-b734-3b7e-8159-94f9b96f99a7 | -3.05649 | -43.10759 | 2024-10-13 04:38:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e98d1cf-639c-3784-9e01-168d5b86b6a6 | -3.43688 | -43.0592 | 2024-10-13 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df97538d-25ac-34bf-806c-5711f4b1d98a | -3.40722 | -43.34302 | 2024-10-13 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45b64485-296e-3c5b-a7e5-49cc26f9b1d0 | -3.40666 | -43.34676 | 2024-10-13 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcb76def-1a36-3267-aa7d-90f2463276fc | -4.87602 | -43.33449 | 2024-10-13 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a0ee9a1-9c00-32c4-a1f8-e077a38490f6 | -5.51002 | -39.56455 | 2024-10-13 04:38:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a507de0f-61dc-38ea-87a0-a142640f24fd | -3.72014 | -40.71495 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3673f164-8e7e-35c9-a395-ce693a315dab | -3.71972 | -40.71775 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bdbeaac0-b7bc-3565-82d2-ccada2945830 | -3.71931 | -40.72056 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0734b070-df0e-3775-829e-c2afc1d4e105 | -3.71888 | -40.7234 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d4fb8f0f-f0e7-3df8-bd7e-ec052e317c76 | -3.71517 | -40.71417 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| feb99d96-2761-39f7-bc95-7dd39e09f6c5 | -3.71476 | -40.71695 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a776f19-a588-3564-ac2f-5ab8cba7be05 | -3.71435 | -40.71973 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eb2320f8-89e4-3d8d-825a-596295a7127c | -3.71393 | -40.72253 | 2024-10-13 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c7994b5-e81c-35a6-8352-e16f9d1ed5a2 | -5.12452 | -41.68831 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2ac9813c-175e-3360-9f4c-4d4d3577fc20 | -5.12381 | -41.68709 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 434dbca5-3f71-3517-bc2d-4a530598d0ff | -5.1238 | -41.69344 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f5fc24a4-d870-32e2-8c62-9eba4696ff7d | -5.12305 | -41.69221 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| fb4e7b40-436b-3eb8-89ff-1beae84e0642 | -5.12048 | -41.68256 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a01d2a6-3f91-3e6b-a8b9-98eabbde1373 | -5.11981 | -41.68135 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 77fffdf0-d4c8-33bd-81e4-c1043e4bd9f2 | -5.11976 | -41.6877 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5079baea-ca7f-3887-b187-f57d14d17064 | -5.11904 | -41.69279 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe606f68-bc19-3b3c-9c67-43ecd3509a55 | -5.11829 | -41.69156 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ec2172e9-a0ed-3131-8a2a-cfe98e7f1411 | -5.11754 | -41.69662 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e439bdec-18c4-3221-af4a-ae9d8ddf9ae6 | -5.11572 | -41.68188 | 2024-10-13 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4bdd8fb-1e8d-3fb4-a310-c6482e53c97b | -4.95744 | -41.821 | 2024-10-13 04:38:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 09c99549-4d05-36ff-8c23-302f6eebf39b | -4.95274 | -41.82032 | 2024-10-13 04:38:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 36bff7a1-b4b1-391a-835d-ca9e6623ad0c | -4.82626 | -44.07645 | 2024-10-13 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3b95b89f-9d52-3227-8c91-d6b66b707cee | -4.82224 | -44.07587 | 2024-10-13 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2fdb34d-3a8f-33d0-a5d4-53566149b884 | -4.82118 | -44.35303 | 2024-10-13 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b84e4b4-121c-385b-8356-e91f14d5b19c | -4.79307 | -44.62488 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ca38bd4-d788-3880-865c-b8436f26270e | -4.79129 | -44.62716 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0a479b9-334f-3f9d-a6ec-444c6bcd04f0 | -4.78918 | -44.62433 | 2024-10-13 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce72c468-2b56-323a-b82a-4c2a34a12a0a | -4.40513 | -44.47762 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88067927-7d46-3566-b313-0a774a30aff2 | -4.4044 | -44.48251 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64b47d4a-1979-37ca-a35f-43654b1b28da | -4.40124 | -44.47702 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2fce80fe-6b98-35b0-973d-70e1b2b0c30f | -4.40051 | -44.48191 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| fd0a2a4b-f333-382e-970e-b6c732312946 | -4.39735 | -44.47642 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 69301586-d71a-309d-869a-97b19c57fee4 | -4.39662 | -44.48132 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| c6b39c4b-aa45-3423-bbdf-98567942a969 | -4.39346 | -44.4758 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48e7f852-6d85-3cdc-8f64-bb41f9330704 | -4.39274 | -44.48069 | 2024-10-13 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1db3e72-b278-398e-a131-08e791468729 | -3.10449 | -44.50014 | 2024-10-13 04:38:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec93d47-ec2f-316f-a8b0-71dcd32a693a | -3.10138 | -44.49485 | 2024-10-13 04:38:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de591465-4736-37e0-8419-b71adb746523 | -3.10067 | -44.49956 | 2024-10-13 04:38:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
