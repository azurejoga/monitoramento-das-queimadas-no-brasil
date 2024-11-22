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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f11c0e09-556a-3d36-8481-0289ad35cc93 | -0.06411 | -51.24369 | 2024-11-22 01:06:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a58e6d5b-bce1-372f-8a87-8cf45451c311 | -3.10719 | -53.98304 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 37726986-6d8c-3a5f-aaa0-2ab28342c7b6 | -3.51628 | -53.81738 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4a807038-a0ce-3a49-bba2-c5c50ad88248 | -1.29577 | -52.22247 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d755c85f-40ec-3dd8-af75-a2198e0e2b69 | -3.40062 | -46.2408 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| fdd905d8-cbf8-386b-8f4c-dccc581526d4 | -3.02843 | -45.65484 | 2024-11-22 01:06:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8cb2bc87-2a41-316e-bc03-4ccc95304a23 | -0.04716 | -51.25567 | 2024-11-22 01:06:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 101e9e3d-91f9-3d66-8198-77fcfe06e066 | -3.63851 | -54.31625 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c9f58f50-3f53-346d-a248-18e8185d1b78 | -1.26541 | -51.60336 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ec9ae5fc-34b4-3b68-aec1-638f755c652c | -3.33882 | -53.33186 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| eef28094-b851-3ce1-ab4a-14e9af13fcc5 | -3.58293 | -54.68422 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a326ecb9-c0f4-3d75-b756-34f8c14ef089 | -2.58979 | -54.04682 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b369184c-6ccd-3b33-86dc-feecc7fa8fc7 | -3.32422 | -54.1039 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 97517c1d-5536-3783-a580-aa0dcb14adea | -1.1289 | -53.39946 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e6cb64ee-8004-3933-9820-8b714511559d | -3.28604 | -53.82254 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f14ab484-1f32-31cd-8920-84d563cbe58c | -3.11068 | -54.28238 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b88d2773-7320-345d-a384-593636afc1a2 | -2.68602 | -46.88409 | 2024-11-22 01:06:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3b4e4465-a828-3ca0-849c-6cb454541a37 | -0.76917 | -51.74688 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e92c36bd-32a0-3a2e-9b21-0f89fc159e4f | -4.70547 | -48.29787 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8beea1e5-bb18-3422-b97a-6bac47919703 | -1.71048 | -52.48972 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a25ef50a-e047-3c91-bd00-7f232cc2e5f6 | -1.73353 | -52.71991 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 241bc48e-dace-31b7-9ff6-7c44ac24f930 | -1.23807 | -51.74184 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b8dc9269-b544-3d38-9bf9-b1088155a81d | -4.18241 | -53.57859 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d0372793-af2c-3062-9f41-d31a4342f8cb | -1.80311 | -48.46748 | 2024-11-22 01:06:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 856e9403-80f7-353c-b0f5-78c6ff61a71a | -1.81243 | -52.15793 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8e0a00db-19a5-3c20-aa29-715578d582a0 | -4.40415 | -48.83884 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c7da39df-6c0d-3db1-bafb-12332a6e3ae1 | -1.55374 | -52.28445 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 014b3ca6-61e4-3f78-acc5-6847e3b13bda | -1.81366 | -52.16675 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bf3374ab-158f-3ae5-b4c4-0e3d25eea23c | -0.67558 | -52.33459 | 2024-11-22 01:06:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 521103a8-8e6a-35c0-9a3b-829d09071e5f | -3.58075 | -54.49774 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 043d125c-a412-32bf-a800-5b95cc96e95f | -0.87213 | -51.89085 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7c56bc6c-e265-3b9c-95c3-e4b99cf46520 | -1.24343 | -54.02636 | 2024-11-22 01:06:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ec2b3b7-4687-37a6-83fb-c044ac2d6cc5 | -3.18022 | -54.32841 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| e20ab11c-567f-33ac-b5b3-50517581ed34 | -0.22224 | -51.19002 | 2024-11-22 01:06:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2188e73-4941-3e98-89c8-adc66c9c1813 | -1.27766 | -51.82107 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| be86ddd7-34b8-3843-81ad-6b16d38e9d11 | -2.46015 | -53.70424 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2987e685-cda4-3843-9b9a-602e5efdfeb3 | -1.20489 | -53.68338 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e449cdcb-e174-391c-ab56-b51609aeaa3c | -3.83199 | -51.7048 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 131ca437-860f-33ab-a259-1a15ea359dae | -1.24213 | -54.01699 | 2024-11-22 01:06:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3a09904a-afaf-39f7-8a87-bc6383df9d31 | -3.28064 | -53.83893 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 44cbb598-577c-312d-b306-e432cdabc33a | -2.0159 | -51.17367 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5fd4f656-b40b-3ff7-a9f2-411d72bc2640 | -0.19111 | -51.36594 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 46ecedb2-22d3-322c-9a40-1fc9acc6626b | -2.89472 | -53.05431 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0004dfcd-4d74-36b4-b41c-e7c042d4ec49 | -1.51846 | -47.06588 | 2024-11-22 01:06:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 4391e98f-d53d-3db4-a074-42dd5a8b0a7a | -3.7486 | -46.10861 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 8efc1ac5-8200-396b-a158-a6ad5afe23d3 | -3.3511 | -50.51228 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 65bb97c8-bc1f-3dd8-9ab0-fa04f627a495 | -2.75055 | -51.87709 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 778e5162-b02c-3455-962e-f0598519bd05 | -1.63507 | -52.40168 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2cb156db-3142-3ac6-a600-c7480e318441 | -3.53734 | -50.27296 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8219f4c0-7f7f-3fec-879a-02dca9ba39fb | -1.2113 | -51.74562 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1dcc5d0e-8aff-3bda-8a7d-126e11481b5e | -1.11998 | -53.40072 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 9f57d612-6b82-3e2b-a736-ab7963d8170c | -3.51361 | -53.79802 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3046c10a-9d52-3d4a-afba-2d3c7a71ae62 | -3.31837 | -52.85445 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bf591955-dae6-30b4-b512-a44935397374 | -4.25064 | -48.6945 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a6ea125f-57b1-3081-af2d-3a247d29f7b0 | -1.60099 | -53.22088 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2bef59ae-fdf7-364c-9d9e-60a7cc60ff20 | -1.12638 | -48.34608 | 2024-11-22 01:06:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7ade97da-4e85-30f5-86a9-9f3bcbda8fdc | -1.74477 | -52.39784 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6cf2701e-ebc0-32f7-96a2-2c1188522ac9 | -3.42624 | -50.98376 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3a4a664-d5d9-3bc6-8996-c91f30abc139 | -2.70531 | -45.22569 | 2024-11-22 01:06:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 96bf5495-fc0d-37ed-90e5-e8a02824fb24 | -1.78256 | -53.59778 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 57197203-1a05-31db-bcb6-0dacb87a6815 | -3.71989 | -52.09259 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 9ab8a865-167b-340b-a9d5-b239e12b079b | -3.08722 | -45.44497 | 2024-11-22 01:06:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c56042a0-5cba-3517-bca4-320a5aaf2e24 | -2.49448 | -49.00108 | 2024-11-22 01:06:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5cd9ffbb-6632-38b4-a17c-7230f2f8a865 | -2.51221 | -54.15229 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| d2dc93f8-38c5-343b-b67b-61a5b6899689 | -3.96403 | -51.13825 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5a394696-c9a6-3baf-8741-a84d680252a2 | -1.13146 | -48.35259 | 2024-11-22 01:06:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 96c3aef6-fd40-352b-a54a-ea7b484d6de1 | -3.29125 | -53.86081 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| f8a89055-fbed-3b5a-9105-efae264dd8e9 | -2.85033 | -54.00166 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d40931b-7e94-3cdf-aad8-423833881c71 | -3.3978 | -50.2561 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 18410079-42e5-304f-a109-b887cab65fcd | -3.66494 | -51.56917 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 00cab72c-1301-31a2-9cf7-3e05a3fdc591 | -1.63421 | -52.66784 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9916e549-97bc-361a-a8e9-29f3295d6d97 | -3.29296 | -50.36533 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5be290c4-d8fe-3a8a-8142-556e410f0e75 | -1.62317 | -52.58862 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd173f9f-a853-3211-890b-8b262e39479e | -0.97759 | -51.71764 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9be2db12-cf66-3e82-ba46-19a60e3cef94 | -3.03965 | -52.43523 | 2024-11-22 01:06:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 10142b45-ea3f-3c47-953c-0105e40dcd34 | -3.4599 | -45.92445 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 38.2 |
| b4372750-dbfa-314a-98df-ca74e30f29a8 | -1.24981 | -51.75211 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e0c47ebe-ba6b-3e45-8de1-90aebab3e4e3 | -4.10986 | -51.0594 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9c3fab4e-3a18-35a7-b0a8-8f3fa20c0e15 | -3.28734 | -53.83207 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4dc50604-ba8d-37e9-936c-18880189ccdb | -0.81255 | -51.78976 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 6db5d317-4a4d-3de9-bced-61b1317faa5f | -3.05847 | -45.68566 | 2024-11-22 01:06:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ac7fb9d7-5b09-315a-8f75-8d1d23f542a3 | -3.23634 | -54.24915 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 228.5 |
| 54582e1a-7a60-3d64-9870-a675bc4b0a95 | -3.5457 | -50.52023 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| adbbf38b-5e6b-37df-856a-ee061c07895e | -1.6357 | -52.61378 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7c435e6c-bda5-3409-8861-36b49089e620 | -3.28977 | -50.54019 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 197f185f-382d-356c-9713-526b501a9221 | -1.61983 | -52.42177 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f92cac0d-cc54-3785-bb6f-03dd5b6e2d3b | -3.94988 | -51.23178 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 024c8e3c-92c2-3cd2-a8c9-336fdcd39bb0 | -4.43962 | -48.02257 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 603bf897-b040-317f-9845-2036943d7a88 | -1.64677 | -52.61535 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2963b5b1-7ae3-3549-9124-2f1ecdb96d7a | -1.13783 | -53.39818 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d68e40e4-1054-358a-9626-a51cc9a62f99 | -2.70286 | -45.24203 | 2024-11-22 01:06:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| dd346416-ae33-3bd9-bf6a-2182c771d9cc | -3.2333 | -53.63314 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d3decada-2b38-3d74-bd2e-2cd01b129f7c | -3.18963 | -54.32707 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 2f194ffa-5535-366c-a490-bafced2d58ff | -4.07992 | -49.28804 | 2024-11-22 01:06:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3c721c48-068a-3644-81f0-887120082f73 | -4.19158 | -53.5773 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4fc72efd-8cd1-390c-83ec-1165290f467d | -1.73108 | -52.70228 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1ca8c305-d1de-33c8-a44b-98ad036f8361 | -1.65411 | -52.66819 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 96608958-4b22-3383-9d9c-8d595b809a8f | -2.69837 | -46.08765 | 2024-11-22 01:06:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 96468cd2-bfcc-3728-8200-d9507d3de475 | -3.20821 | -54.2531 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| aea324e4-8c1c-3871-bb4e-6302401f0433 | -4.41032 | -44.13808 | 2024-11-22 01:06:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |


[Clique aqui para ver as próximas entradas](README9.md)
