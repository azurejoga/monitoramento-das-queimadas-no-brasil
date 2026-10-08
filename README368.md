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

## Dados Diários - Página 368

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4efec266-1cc6-3768-bbbb-d75a5d112a25 | -3.01653 | -54.03956 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 9af56285-e39a-36f9-beca-9f1cd398e097 | -1.43515 | -55.25875 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| f11ec650-b0dc-3406-a2d8-61c1dd11d680 | -5.24698 | -50.90445 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d432b15e-8fcd-3af7-a142-49c3a79bdda2 | -3.03649 | -54.10111 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b6a99303-a2ab-3f59-9713-526f100b58d1 | -3.32941 | -58.15143 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 13c50fe5-e550-36f4-aa8e-6fa3d4ca5c59 | -7.19032 | -52.62283 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 2abf1e88-70a2-3f41-9a08-22f5b3ed1a0b | -2.82643 | -58.35088 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| cd414368-989e-3265-b123-32cd4f0e0bfe | -6.74186 | -55.13686 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 069459d7-db9c-3940-9d51-eac98d0cec7a | -3.30776 | -53.71202 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 8d41d03b-bc33-37bc-a39a-3da8874e6eeb | -4.35671 | -55.22232 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 11686aec-6cc5-30e1-beb1-4ec25a726fae | -2.99494 | -43.28105 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8fd92ae3-fd52-3d7b-8c37-7ba0266e2270 | -2.98876 | -54.07961 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1ac4b0e4-53a2-3d74-b5ee-64765cda8ce7 | -2.57873 | -56.17203 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 494c4bfb-78c5-38d8-b27a-8d2997c6230d | -3.25063 | -50.40189 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 331677cd-5557-32c2-94ba-5470f731428b | -4.58629 | -40.28698 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee16eff7-0c68-339f-ad82-93c654a223fe | -6.7383 | -55.15123 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 859f7486-9825-3baa-82d7-22628dd7fa39 | -3.01839 | -57.7818 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d79d4435-96ea-3c6f-b9f4-8d75b997f8af | -2.41284 | -56.52995 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cf869977-88f2-3ad7-8aa5-d2b8fc970b1c | -5.3759 | -44.18918 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 85b6e2c5-9bc1-30f2-9244-4459379476ea | -1.93469 | -56.97561 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f1f685e7-361d-38c1-80d8-a681ee0691f1 | -5.38845 | -44.17956 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ea7ab687-4782-3b96-9d36-8e3dd26da6f7 | -5.97715 | -51.53294 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7361bda9-6fc6-342c-9cfa-42a052f04cc8 | -4.07126 | -59.83543 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 375adb64-3071-3342-bcf5-713cb2cb5abc | -1.46185 | -54.7629 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fc42b822-d970-348c-88dc-0c4a5c00a449 | -2.83342 | -58.35485 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fcc6876-929d-3ae4-9c73-d6432f3de97b | -2.50393 | -56.11649 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 32ed2cf1-bc6b-3cf7-a190-0726596fa828 | -3.91378 | -55.74474 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9752d019-7e2c-3761-8346-406b6e94e26a | -3.06304 | -45.31782 | 2026-10-08 16:39:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ded0f871-7edc-3bde-a573-305d4f7b46ad | -2.15802 | -59.22103 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 42e74904-f137-3a86-a1f8-12cf66fe7c71 | -6.11739 | -52.71231 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5c046080-981c-3fad-96ab-a51e18399877 | -2.43855 | -55.97024 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 233ba822-a8ba-3704-a1f6-85384b61b1cf | -3.38429 | -50.21669 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 410fa785-7ee2-34d0-a41e-88b6a0ec1da6 | -3.98737 | -42.85725 | 2026-10-08 16:39:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c224e32b-c39c-3e64-b9ea-6a2e1d319cd8 | -3.46621 | -60.25195 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| adc49c1b-26d4-350c-ba74-0e2e6e1862ac | -3.11443 | -54.16798 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4dafa0eb-096b-3b9f-a01e-de0805d924e6 | -6.24897 | -52.67427 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| abf756f9-2514-36a2-91b9-40c7eb72e684 | -2.74645 | -54.12603 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 6bccb453-c8db-3a70-ae1f-df030491b989 | -3.00984 | -54.08426 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 156b1ef4-a158-3fd3-a2da-58f1087cf525 | -0.58438 | -49.41366 | 2026-10-08 16:39:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0aab8715-9077-3501-86b1-215bf27e25a6 | -6.20657 | -52.84287 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e2f25f66-cfc9-38d3-884a-0f29a8e57e3c | -3.0095 | -54.04826 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| ea6bf646-bba3-32ca-80e1-33ffc61db748 | -0.60736 | -49.4256 | 2026-10-08 16:39:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 2ccd6e19-dfa1-3f33-a61a-1e67241cfaf2 | -5.74421 | -53.44991 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ab6d61c6-ded1-3650-a631-3dbd5237c070 | -3.00784 | -54.04594 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| caf85b01-0a80-37aa-922e-3a30a8b0b28b | -3.0633 | -53.92323 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2fc14412-d484-3b3b-88a4-0efc405e91d7 | -4.09059 | -44.09856 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 80d5f771-4d2a-3f6f-99ef-b1b3793b30b6 | -2.8893 | -56.55083 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0e92a936-44a9-3721-807d-e7b502d09c8e | -6.45445 | -52.64828 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7f0c237a-d500-3bc0-b5ba-b44c5bf107ec | -5.96252 | -53.54462 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cadb5c60-1b72-3cb3-a150-0f1878960cca | -1.7002 | -54.9808 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7109fc90-c6dc-3b1a-8770-a291581d3371 | -3.25743 | -50.39637 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8db79054-d2c1-3593-8b8e-479a4ae481e0 | -6.86511 | -59.34165 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 69b365be-8ae1-36c6-bef3-64e2ef8cd6ca | -5.39354 | -45.90556 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d31859b8-f785-3d0c-aa9d-9e75bcfdd72b | -1.48304 | -54.54964 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b220234e-5ede-300c-ba86-7582c0d1a5e1 | -2.15545 | -56.61668 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 36d8a014-ea31-31a2-a135-1558adf07dae | -2.15706 | -59.22081 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| aa45ee44-c423-3b6d-9f6a-7be4ada8e3c2 | -1.38999 | -55.46357 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 676602b7-71ef-368d-997f-37de7b2b4be9 | -2.88658 | -54.14961 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 935a7b1d-e5a4-3127-8542-cc99d0b31c13 | -3.32062 | -58.2687 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4c046618-90b6-352f-9e14-96a09484a229 | -3.73345 | -43.33772 | 2026-10-08 16:39:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 376db1fb-387b-3c75-b131-815b4262eeb2 | -3.89304 | -41.59843 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 0c18ba6b-b780-3425-8210-09151acabec4 | -2.61733 | -57.00323 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e40b230d-11ca-3d59-9054-de810393de25 | -7.21177 | -55.16576 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 76d71062-de2c-394c-b927-b7983e6cf131 | -3.10139 | -53.95319 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 304c9f74-474a-3429-a106-ce9a59af9f93 | -1.7197 | -55.44057 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2f3c1d4c-ce63-35ec-afc3-77f0f365c92d | -6.72954 | -59.4356 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7c658fc8-ebc0-3c82-b106-69c352beed24 | -3.69862 | -58.27859 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 956a67b3-f659-31a3-babc-7e46352be9c8 | -1.47893 | -53.61042 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c20caf27-2241-3b01-9437-be4bffceead2 | -3.16435 | -54.7382 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| db42b2e5-50a3-3746-8139-14e3f3cefb02 | -5.38108 | -44.19987 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2bdf2682-f131-3aeb-b435-7ec0cc0d8df1 | -3.23922 | -42.23699 | 2026-10-08 16:39:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cde23c0f-1da2-3236-b733-3c6c41997b6f | -3.00811 | -58.96022 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0e55df1d-ad1e-3812-9e63-56087d9ddf42 | -4.35667 | -55.22574 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fc095c46-c318-35cd-8acc-e0be74c1d5f0 | -2.9114 | -58.56042 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 258fb63a-7b49-3c72-8a9d-0bdbee4674b0 | -3.74208 | -51.20811 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 762d81a4-8d41-38b0-9658-c6fea84443d7 | -5.27966 | -55.95549 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 54fa8932-29f7-3ee0-ae73-25b4c12b2e19 | -2.73874 | -54.10655 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 13ac38fa-d191-3f1e-bb64-212be8f010e4 | -2.22391 | -60.07521 | 2026-10-08 16:39:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8ace6e70-a900-3d2d-bd7c-cc1bf0e3c417 | -5.36638 | -42.84447 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7c0f049e-2512-3d3a-a6f4-1b496b2345d5 | -5.9258 | -51.83196 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| b5d62ea1-ccea-36d8-9d98-1ee7b7409f8a | -5.3274 | -48.98634 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ea6b9760-4a04-364b-98d9-7ccf67405f40 | -3.81762 | -44.62252 | 2026-10-08 16:39:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 42d4624f-e5cb-3680-8436-82fa39ed9d84 | -6.85899 | -59.34934 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 86110d5d-4dff-3c9b-add2-32dd6e62f9f8 | -6.2176 | -53.28017 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20c60814-feeb-3578-955e-16739e4a60a8 | -3.30837 | -54.67575 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7b465fef-f534-3fef-beaa-3d0ac1c003b4 | -4.33604 | -42.74933 | 2026-10-08 16:39:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8f158388-553c-3abd-9c42-3648f24b6eff | -4.74847 | -40.50409 | 2026-10-08 16:39:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 7bc3d42e-a449-38d9-a138-dca5fd69a2f2 | -3.43086 | -45.04263 | 2026-10-08 16:39:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 901551bb-2446-398a-8a92-bd92c05af210 | -4.47296 | -55.89889 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 987ce785-9416-38d2-b840-8d53d8756533 | -6.2202 | -52.77476 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 18365d65-74cf-36f7-9c4f-3e399a8cf7ba | -3.57113 | -51.993 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c78e3e4a-2dff-37a4-9162-f5a618be813f | -5.9819 | -51.59425 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e1dc1576-f1cb-32f0-8830-96c281734e7f | -5.71729 | -49.83028 | 2026-10-08 16:39:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a13dea7-39f9-3557-a952-941e6b57a296 | -3.91436 | -44.38635 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a347380a-e434-31f4-a751-b7b011977811 | -2.97876 | -54.04517 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| cd695486-32c4-3f2e-908c-001043dc5a84 | -3.6669 | -45.40811 | 2026-10-08 16:39:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b52245a-586d-379f-8c79-c2f6d9dac2de | -1.80177 | -57.11271 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5f639b38-2d07-3dd0-8009-982217d2a804 | 0.53612 | -50.76896 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 41170fb0-22f4-3002-a201-4a755b7ce684 | -3.44318 | -45.09986 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4abbb9c0-721e-3ce1-bbc8-ef86178f1ddb | -3.01567 | -54.05762 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |


[Clique aqui para ver as próximas entradas](README369.md)
