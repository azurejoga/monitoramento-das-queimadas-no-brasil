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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fabfddc5-5363-34b5-9ad6-b319f989724f | -9.55901 | -57.5492 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35b73e6b-412b-3c65-84a3-e9a190600bc6 | -9.6952 | -57.20268 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bf34d4a-0d85-32ab-a667-bc5d7bf0f87f | -9.6936 | -57.21508 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e56f4967-c9d3-3f51-badf-e978248679bc | -9.64994 | -56.95589 | 2024-09-26 05:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bca7f5bc-1048-337d-aa9a-a646c57b375c | -9.64412 | -56.95507 | 2024-09-26 05:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a645d5e4-d912-37fd-8f24-644de7a4d545 | -9.61693 | -57.76084 | 2024-09-26 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2883543c-7b37-3b09-80e4-430db55cc5a6 | -9.61595 | -57.76833 | 2024-09-26 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 174ee918-4364-35e1-8805-62941c831be4 | -9.61546 | -57.77203 | 2024-09-26 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da1f543a-55e1-37da-8c18-8722885f735f | -9.61042 | -57.7676 | 2024-09-26 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 946ab9f7-4006-3c5f-9c03-99709fe4317f | -9.56508 | -57.54622 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dbcaa13-bb1d-3e4e-a34f-b40bf4d55d2c | -9.56123 | -57.54659 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| acdad293-285d-3e33-addb-8d439d957a90 | -2.72195 | -57.51432 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a13ec854-e2b1-38b0-975d-4702bca43c9c | -2.71882 | -57.5129 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7809085-2e07-34b9-82bb-48aa8ee8e3a3 | -2.71837 | -57.51587 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a6ba54-7694-33f3-a082-41a01d936b6c | -2.70087 | -57.5284 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91cf8626-0785-35b7-9fe8-88d8beb40269 | -2.70041 | -57.53137 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1c5fda3-2b21-3f89-ae49-d95494b97dff | -2.69624 | -57.52469 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 039afe73-d3e6-3fb0-a202-ea632c216f50 | -2.69579 | -57.52766 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baec6ade-484e-3f32-b9a9-680d9fd98578 | -2.69116 | -57.52394 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c19fb327-ab0a-31a5-b96d-02e4a46da787 | -2.68609 | -57.52319 | 2024-09-26 05:46:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f77e05a2-2daf-38f7-8841-ef091a1386f5 | -3.753 | -57.20808 | 2024-09-26 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96235a1f-7023-33c9-b6d4-9bde38cf1e8b | -3.75254 | -57.21127 | 2024-09-26 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc128371-65cd-3c80-9cff-c610076fa263 | -3.74775 | -57.2093 | 2024-09-26 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d100aa40-28f2-381d-aad6-f985bd4b392a | -3.72715 | -57.20305 | 2024-09-26 05:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2652a7e-cd96-3fe8-baf5-dbd1970dbc98 | -6.82346 | -59.04285 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3408010e-bdfa-341f-afc2-d6a6b62749d8 | -6.70513 | -58.92455 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f189640c-65f0-3f07-ba73-90f390cf5809 | -6.70322 | -58.92081 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da574864-430e-38bf-bd9b-192443d52bd5 | -6.70246 | -58.92631 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5718f9c5-5280-323e-80ed-1e6d56f60652 | -6.7002 | -58.92412 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bc11d28-e6a4-3ff1-ba83-a4865d0866a0 | -8.80898 | -58.21863 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 562a6967-5a58-390d-bc9d-bad8d98aaecf | -8.80802 | -58.22574 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 863cd923-2b43-3a82-b4dd-4bbee05de965 | -8.80368 | -58.21792 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 275a1e78-21a3-309a-b389-fb00acc9a9b9 | -8.79625 | -58.19271 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db4a9ae-4b5d-3a9c-b1c2-ae0993788cf8 | -8.79094 | -58.192 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64122198-4154-3187-8c38-5f5865170aa2 | -8.75398 | -58.18534 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dc5cce8-6ed8-3f76-8eef-db72a756e828 | -8.09054 | -58.03599 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98f438c2-d5ec-3812-8e13-b96f9ffd64cb | -9.01062 | -58.98758 | 2024-09-26 05:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36c25e2a-58b0-3b15-ad30-e7dba635cd9a | -8.8138 | -58.22295 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bf9d9d5-175c-3ee7-8421-2e87910ba0f7 | -8.81331 | -58.22655 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e3e992-42b2-3b74-9ace-2ec75d947c6a | -8.80851 | -58.22212 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b9a5c1c8-6a84-3993-b3f4-7b63168eca8c | -8.77713 | -58.17377 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69bc9187-feb1-3bfa-8163-c938c5acc3f1 | -8.77709 | -58.21498 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fcd36ac-5d96-3182-a2f4-7ee0a7980677 | -8.77223 | -58.21094 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae0d5671-42a0-3086-96da-454e4ac8c485 | -8.77178 | -58.1733 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a4f34de-1719-3739-a25b-e99fd78de616 | -8.75444 | -58.18185 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29c0e606-efb4-38eb-9685-f8595452c126 | -8.09145 | -58.02932 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe1efe1-f0ac-3b49-8117-6567db777779 | -8.09099 | -58.03266 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c131c24-cd2e-3a1d-9ced-4017142760b9 | -3.51859 | -58.75414 | 2024-09-26 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 788869be-a5f9-3d53-8e1d-015c8dec2283 | -3.51661 | -58.75635 | 2024-09-26 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f0310f1-2f81-3289-86c4-52f963355d24 | -4.28875 | -59.69577 | 2024-09-26 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fea5ab0-3cef-3bee-b8eb-e61d27941133 | -4.25354 | -59.71767 | 2024-09-26 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3222c23c-441d-3a74-b80d-1f74a50f40b6 | -4.22673 | -59.86993 | 2024-09-26 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33e50566-5408-3cea-930e-ded826563601 | -4.2261 | -59.87423 | 2024-09-26 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2642e4d8-0777-3a30-b221-d87304a9c8db | -4.22547 | -59.87855 | 2024-09-26 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ff09551-e52f-3238-9271-ef519264e550 | -4.22232 | -59.86927 | 2024-09-26 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7f6875d-1442-3bbc-a53d-47a593ebfbfe | -4.22169 | -59.87355 | 2024-09-26 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d0f88af-f4dc-3db4-b394-9a67fff49efd | -6.40152 | -59.98509 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35dc146e-3b9f-31d9-a39c-927a98a5c5f4 | -6.39697 | -59.98456 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b91120a5-6a3d-3962-b775-780f56ad2081 | -6.36852 | -59.95693 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3b4d6ab-be2c-3910-a3f3-138b940f6f91 | -6.36399 | -59.95616 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a06d71c5-ad76-3ec8-aeb0-b1fd1e482c76 | -6.30663 | -59.99145 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a71eea60-beff-38a5-91ec-20de53199969 | -6.22985 | -60.01274 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9c1e03-dff4-3a5e-abcd-feaaba7da982 | -6.22921 | -60.01729 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fed4b9d5-d813-3231-b468-790fa7da7a8b | -6.22789 | -60.01467 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a2e32b0-53dc-3836-ba53-735fb84a213a | -5.52576 | -60.20367 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 109ea819-7241-36a4-a1ef-42831e365e34 | -5.50497 | -60.13021 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e383502-28cd-31c8-9759-3446da7cb994 | -5.50054 | -60.12955 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acc0243e-fa14-3a23-bc9c-596f015ff977 | -5.29344 | -60.13315 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a0dd4ff-d3b5-35b0-a6d0-82b3669e86aa | -5.28903 | -60.1325 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0dbca080-d646-36bd-af36-e321cfa83596 | -7.2742 | -59.49074 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b28a2a1f-9de6-3962-8666-337abf012614 | -7.27268 | -59.49442 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b050a9e4-186f-31e1-bb70-8639ef835712 | -7.26944 | -59.49015 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a44bb2c0-e452-3c5e-832d-c97219df1409 | -7.26876 | -59.49513 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bef428c-215a-3c98-86ef-db3674cac59b | -7.26864 | -59.48882 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d5171b7-d5c3-3907-a813-33bb91b9095e | -7.26793 | -59.49377 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87e1824f-6f40-369c-8ac6-33967bede04f | -7.2647 | -59.48937 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 137492b1-4dfc-3525-b397-d0fefa629e25 | -7.26391 | -59.48803 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d6f17f6-a7cc-3ce5-88f1-be861a7d2290 | -7.12301 | -59.45132 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff6da2a4-0a0a-3ee2-a1cd-e1842e0c4c0f | -7.1223 | -59.45641 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cd6aa17-405c-3344-b657-152ec12d5242 | -7.11827 | -59.45062 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1fba5d51-a4ec-3418-98bc-834dca2bd913 | -7.11755 | -59.4557 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0355ee2f-f251-3502-8c2b-322f65add5de | -7.09461 | -59.23846 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 933983e1-f12f-3439-95aa-6dcca89ca678 | -7.0944 | -59.23525 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2de00c2b-29ab-38ae-b570-970a75953572 | -7.09385 | -59.24366 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d46dd348-2c00-3693-ab9f-a0eb618e2feb | -7.09369 | -59.24052 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0f33f4c-5544-3fe6-94e1-7ad9051cf428 | -7.0931 | -59.24889 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d827e13f-4c44-3181-901f-bbe65ba95323 | -7.09297 | -59.24573 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6eb40a4-9c3c-3be6-8660-b52885550017 | -7.09055 | -59.2325 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d3ea8a5-c74d-3e3b-a45d-53992f953e0e | -7.0903 | -59.22927 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24334d97-2459-328c-8f20-bf4f28150eb1 | -7.08979 | -59.23778 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5304de32-5e9f-36d5-ae10-bc33fb8bf950 | -7.08958 | -59.23458 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2db6aa8a-ff21-33e2-a0aa-c2f2233ad4d0 | -7.08904 | -59.24296 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f565888e-1e45-328d-bdc1-563cd1285fb9 | -7.08887 | -59.23983 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2aa3862-e357-367f-837d-251a96d654e0 | -7.08829 | -59.24816 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b85c38-b64d-3dcc-9d88-6813329c6f93 | -7.08816 | -59.245 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75e25bdd-1a56-3fa4-9601-2ea74fb1038a | -7.08572 | -59.23182 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6aecfc28-bed4-3c39-bc35-a71ce9d022ff | -7.08497 | -59.23708 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abb2d460-73dc-3cd9-afab-621376be7c19 | -7.08476 | -59.23387 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dc6ca96-881a-322e-9313-d9216ef63eb5 | -7.08405 | -59.23911 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57f4b593-d088-3afd-ab1c-4df12261f3fe | -6.80174 | -59.30458 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README159.md)
