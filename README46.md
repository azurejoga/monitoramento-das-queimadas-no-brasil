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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69445cc3-4c15-3eef-a09a-4c15dc8f7e79 | -5.58003 | -49.74953 | 2026-10-05 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bfd8a3b-5034-3c7b-b324-c4c7718d7d9f | -3.10735 | -53.74815 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4c379cd-263f-3de2-9d79-2def595b932d | -3.12218 | -53.72063 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 667e8d5d-5da7-38a0-a775-1d72138037a7 | -3.11995 | -53.71282 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3986eb64-c3fd-35f3-b51e-d93b92940f67 | -3.28427 | -54.17751 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 729b12a4-cb76-36b1-b2b6-3c0ce08ac66c | -1.62708 | -55.13302 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9936d23a-ca88-372a-95f4-5edceb0bcffa | -3.68502 | -51.15402 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59fe152f-c05b-3b64-b83e-ce11940ed5ff | -4.11662 | -49.07771 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fd56d42-b6c3-3271-a402-221a62c1a146 | -3.9031 | -49.7141 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba7a6227-f56c-384e-bc66-93f07f8b2154 | -3.11869 | -53.74248 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8b142d6-1b72-3516-94ce-2a866e566779 | -5.97845 | -55.38186 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e97a362-a601-3f3a-afae-be2fc8bf9a58 | -3.28142 | -54.17324 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9358f8e-239a-3662-9c12-9f6ee8651f04 | -2.99336 | -57.7883 | 2026-10-05 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 831f1ec0-220f-3e9e-80fa-9db622af029e | -5.99037 | -53.63285 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76f30d15-f930-336a-bd12-549148f8ecef | -3.84106 | -55.96322 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc277f02-28cc-3fed-891f-eeda0acf2a24 | -2.94211 | -54.12413 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4587c786-6b8e-3071-8c05-9708376f5dc4 | -3.27666 | -50.40008 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a63c50a7-b20d-39ec-afc5-9b0d8a85c55c | -3.84354 | -50.31329 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a892a729-e67b-3b6e-be90-5503ded626d1 | -3.76031 | -49.56443 | 2026-10-05 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e4eb1d-d3ce-3749-810d-8f676b8a685c | -6.90104 | -43.67304 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9041f609-bb63-3357-bbc2-e9bd4bb606dd | -2.79171 | -54.09718 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b615f53-6b3e-3b2a-acbf-4058615aa384 | -2.78928 | -54.11222 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cd3e264-4cf8-30ba-ab0b-042ea444ebeb | -7.50104 | -54.9961 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5162a79b-97da-3fcb-bfa9-c36e50790600 | -7.44584 | -63.56247 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b4c0dcb-8eef-30ad-9fea-43b94acf3df4 | -3.83962 | -55.97211 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a13c9a65-b9cc-3cee-a33e-edff422fbad4 | -3.80649 | -47.49061 | 2026-10-05 04:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8de5464e-be7d-35a6-935c-197e19e872a1 | -3.42392 | -54.55298 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05108261-ac83-3bad-aaaf-fdeb036a7c22 | -3.12035 | -53.75394 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a125e503-7153-3293-b714-32bf24727773 | -3.22093 | -53.87108 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36bb78aa-536c-3f1e-a319-966ce9f6689a | -4.25464 | -55.04158 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 994c3f41-f93e-3bb9-81f1-27e28a32cf63 | -1.98873 | -54.10227 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a302fe4-d09e-38aa-bf3f-5b0baaaa2ef4 | -6.19123 | -53.2887 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2a6b1d9-8878-3ff4-bfaf-20e7ff24662e | -3.93568 | -55.51722 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58412ff0-4d93-3a02-80af-41e1d37cf82d | -2.8594 | -53.91703 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6697c294-2aac-3ada-9528-316cd0924ae5 | -2.89268 | -54.12392 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e89b2874-660a-3d0c-a6dd-df234f0b85f2 | -3.11355 | -53.75286 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d3a37ae-2778-3376-949a-36948e849275 | -3.13177 | -53.72589 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c575945a-3096-36c7-a83a-19bc09b47f05 | -6.25232 | -52.8409 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb8fdd95-5ea6-3001-8363-ae03991c3065 | -3.85653 | -55.82105 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96ed721d-6b88-31ce-aae3-da8643327520 | -4.28417 | -50.27275 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d4f899d-f4e6-38fb-bd2c-35850a1cef4c | -1.94867 | -54.0415 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cb121f8-0935-3077-b4a7-10537fc696fe | -2.78198 | -54.0918 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 78f24f70-79a6-3f86-83fe-f9def64008c9 | -3.84118 | -55.84536 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1304e4ad-625b-3dfd-8fc6-4c8e89c31b6d | -6.25122 | -52.84781 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e580d5ab-f453-38da-bede-8e416d9dc4d8 | -3.32659 | -53.39201 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c85b38e-47a2-3d58-928a-a4e02fd58ce3 | -4.30325 | -50.7832 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bca99598-6fe9-3702-a2f4-3962a1237a4c | -2.89613 | -54.12448 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abb905ef-099e-3263-96a6-a113ffb84ce2 | -3.06995 | -49.53902 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08453e08-8594-35e1-a879-ccc906ea41fb | -7.19321 | -44.30867 | 2026-10-05 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cdc707a-14c5-3f7f-93bd-43263d2c2c5b | -6.9074 | -43.66678 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f30c8e86-7404-3961-8575-07c8343992ba | -4.30269 | -50.78682 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6fa7ff30-fe43-3166-9735-b9891cf3a1e9 | -4.10939 | -49.06908 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b2b12ce-73c5-3def-b26f-ca76f22c31ca | -2.9466 | -54.14026 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20d04314-ecd1-36a4-824e-eea5eeb43c70 | -2.85079 | -51.29882 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 943146f6-0095-3194-86fc-9c9d7cffa41a | -2.81298 | -54.09671 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d430f3ff-b94d-3286-8ddc-8357bff4530f | -3.46025 | -54.59459 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b5fb5336-d097-3a2d-828d-3c164aabb73e | -4.28474 | -48.56994 | 2026-10-05 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 953f0308-066e-3275-941e-62cbc4744280 | -3.07433 | -54.17537 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 930ce844-7fc2-317a-a3ff-b85199796e26 | -3.5501 | -56.86174 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2665540-ed44-3cce-8191-9e77a57b7310 | -4.46506 | -54.9712 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be8e2cb-a6d5-33fb-9e03-714f933f93c6 | -2.81504 | -54.12788 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03559220-a566-3ce1-ac87-fa39c291803c | -2.68182 | -49.03386 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 73cc3f0b-8970-3d9f-aa20-023a56ba62cd | -4.78442 | -55.71161 | 2026-10-05 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb5131c-c81d-3f9d-999a-d3aeede9ad41 | -3.01305 | -57.74737 | 2026-10-05 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0abcaa28-ce5a-3036-94f3-5a16f02fe2f1 | -2.80386 | -54.08756 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18d7e2ea-f480-3d37-a3a8-f51a9d1b62db | -3.11539 | -53.71955 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42f79664-67f2-3f52-b60c-18ff976a5ca6 | -6.92699 | -43.68338 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6cdb765-45de-3eb6-9496-2f8982b0261e | -5.80288 | -53.42329 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5a9749f8-83df-3201-b2b8-467446f9f322 | -7.32945 | -44.36364 | 2026-10-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d396154-f71b-31d6-8637-804119efa625 | -6.01766 | -53.52577 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bb77758-7892-3651-93f6-a9abbd3a5314 | -3.26483 | -54.25513 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa9d971b-62e6-30ee-853d-58f3f74a0135 | -6.00823 | -53.52069 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9b6d4c5-66ad-3f99-9a91-212d84fdf349 | -6.89916 | -43.6866 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a811e84a-a9f3-30d6-b9e0-1fb541008167 | -2.85688 | -51.30332 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcf5546a-a2d3-3d5e-8ef6-5b521b2aca96 | -3.64948 | -55.3169 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35d37e60-9418-30a2-b55f-b0cd6f262312 | -2.26774 | -55.83846 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 577e31ad-1d68-3145-9d33-b935ec38064c | -3.70498 | -50.66201 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 328e7357-ffe5-3864-b6fc-3799bb9c5cf8 | -2.96684 | -54.21321 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e3026b4-e840-3aff-a54b-f3ebb37df79f | -8.6553 | -54.55989 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29bedf84-23fe-38d6-bf1c-99d9571138f6 | -3.37829 | -54.11548 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c183fa1-7913-30ee-bd83-f78e9d2b709e | -3.96701 | -53.46748 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02fedaac-f957-33e7-9d70-6c69888e6076 | -5.83131 | -53.47827 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04883e39-d95a-3126-97c1-12274b03ee83 | -3.60886 | -55.47764 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fcea298a-fe97-3783-a531-28a8de272a08 | -6.00379 | -53.52716 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04d05577-d57d-364a-9a4d-4f3c4fdbe6cf | -3.65687 | -55.5055 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b377ec3-fcd6-339b-bab1-6aeb0150238c | -3.11472 | -53.74558 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b7640c2-3ef3-32c9-9529-ed37f94cbf62 | -5.99591 | -53.641 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbbbf50a-af32-320d-adc6-1d08ec27fd50 | -3.48934 | -59.72739 | 2026-10-05 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e1e37ce-f5ce-35d1-a158-46a1a04a2600 | -6.26059 | -52.85283 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de9d4c8b-7f41-35ea-b547-e425fff62947 | -4.25473 | -55.0409 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffe832f5-4623-3f3e-8126-82a9989a1874 | -3.84582 | -50.3212 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4a1ed9de-d2b9-3e2a-91c3-3e2f226a2840 | -3.1057 | -53.73668 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91f476d2-d2a8-372a-9d96-9d9efa1c1612 | -3.06234 | -54.1619 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| de9b9ecd-5632-3781-9433-4f6808e4f3dc | -5.61513 | -57.23552 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6deafcd1-4a1f-3c2d-8ced-cf43617c1ff1 | -3.91341 | -49.69938 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e92dd259-6142-3a18-8255-fdae784da062 | -6.20689 | -52.82716 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c832bed6-8618-3407-8eb1-9b5bf572b5b3 | -3.87343 | -55.81032 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 766084be-c649-3cf3-b1f2-8b2ccfe5a202 | -6.26776 | -52.85043 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bcd18d4-e49c-3774-8a07-53cef42d37a1 | -2.82599 | -54.12576 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b886f1-443d-3333-bb49-cbb1e6dc9a3e | -6.93283 | -43.68083 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README47.md)
