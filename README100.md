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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f17e18d-5a4b-358f-9cd6-c10afed1642e | 0.67772 | -51.42437 | 2024-11-30 05:01:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52f0bf69-6d55-3870-a00d-d6d9e1985271 | -2.91514 | -53.07107 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02466ef4-95cd-3ad2-933f-4d88e0464db3 | -3.25231 | -53.63605 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48f3196b-6651-3b73-b339-8fd5a891ff59 | -1.89157 | -48.64737 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2637785-b54a-392b-9092-6d96048784c9 | -4.17582 | -48.61928 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 797c1395-0488-38dd-9d78-3324cdf6a76f | -1.29475 | -51.72717 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70c26ee2-1977-36e8-b3d6-f81a4e37688e | -1.09271 | -53.64413 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c12554c6-2d9c-30ee-bf83-09297fa470ec | -2.81887 | -51.9559 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef1d4a65-02dd-3c5c-a0d0-483956d3db13 | -1.16819 | -53.67709 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8a90c16-bf8c-3c6e-8c62-8be21eeb0708 | -0.95091 | -53.21422 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cb8eace-eebe-31e9-907d-dd8460856b76 | -3.84549 | -46.51867 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7519c33e-0b99-3dd5-b491-923237103f27 | -1.45667 | -54.48811 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 945f06cf-a153-3f79-ac5f-4c1f96b4e0ff | -1.09296 | -53.35924 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad2edbb6-4eb0-367a-aa0d-f5d14248f2c6 | -3.22923 | -53.62879 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f8bc988-f8db-3176-824a-f852491a1fec | -3.29543 | -53.67524 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 540ec0f9-29ba-34c5-823d-b3a575fea8b2 | -2.85699 | -46.69358 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a161cb8-2cae-385c-80ad-7a6ae2c332f9 | -4.30616 | -48.2334 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b9e217a-e6f8-3a5a-adb1-d23101a05edc | -2.57516 | -53.97689 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 938268b6-c4a8-357c-8312-eecefffc9d1f | -1.56254 | -51.26088 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2688ad2-8a77-39bb-8d66-43e5443fd803 | -3.46717 | -48.93118 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 176b90aa-3576-30b5-9952-d19f35e8bbf8 | -4.31209 | -48.20835 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ead7384c-e006-3374-baaa-0911a9e70a5f | -3.19965 | -53.41336 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac0aa998-3da4-33d4-86fb-c4d97696c308 | -1.35889 | -54.63869 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebc5de10-2a7e-30a1-89f3-ed9333317d11 | -2.97621 | -53.88443 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5852b8ac-2add-3079-ab92-010f2e71173a | -1.24837 | -51.78981 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f663b9ef-81df-3f17-b28c-f7e8b644ca0b | -3.464 | -50.53343 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0169f87-4374-3892-8557-8418374d4fe8 | -3.19905 | -53.421 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33a91752-c8b7-3032-a5f2-ea4c97559933 | -4.87861 | -41.29405 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9f75f128-4c5f-34da-a045-c681b4eb79f8 | -2.90316 | -53.05785 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62ae1106-812b-3d90-a243-d7df492a275f | -3.26487 | -53.82744 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3df7560-50e7-33bd-b91d-6fb2db6e6046 | -2.61028 | -54.21096 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af645c4-93ce-3868-8fa7-94a5ad47bc17 | -2.81048 | -53.0473 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e60e681a-bd8c-3f81-863e-0640dfbcc340 | -2.96969 | -48.0335 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f83b237b-c4f4-36bf-a601-7bcc40a81797 | -3.30325 | -51.1092 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 877564a4-0f54-3863-aac2-1f010dad9419 | -3.16401 | -53.23983 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01e8f97b-1ba6-3641-bc0a-a05135954baa | -2.82552 | -54.08776 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30a84e03-5f7b-3d98-b5a1-ed2de9ebb51a | -3.77786 | -53.42236 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07472589-e931-353a-910d-b9b1275808c1 | -3.27167 | -50.02132 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78988d21-b2d8-33f4-b752-3a12c905b61f | -3.54246 | -50.17712 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5801504-1d6e-3cce-9778-5d18f4007830 | -1.48586 | -54.45382 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46549eb9-b4f2-3dbe-a658-0531470eb612 | -0.97122 | -53.68279 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3240d48-1305-35da-b0f9-e7d67319db00 | -2.38305 | -54.47376 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55c2d6b6-f453-3f09-93ed-868bb8bf08ce | -3.1146 | -54.01064 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b306b8d8-c424-39b4-8c95-fc376ad8f40b | -3.2655 | -45.3736 | 2024-11-30 05:01:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83845f75-c873-32e7-9009-442fce5dae4d | -3.29858 | -50.75504 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 658d5a7c-f4e3-3300-a691-649037efa5ad | -2.43024 | -54.02257 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d36e80a3-f543-329a-bac5-c5f412ca0639 | -2.86762 | -53.97228 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e77a6f0-c1ef-38f1-b25b-3409eb5e4264 | -1.1144 | -53.5936 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d532e492-a9cb-39a0-9028-0800d53caa22 | -3.25458 | -53.42195 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b10d95ff-b6f2-37a5-80bf-eb1b39a260f9 | -1.09381 | -53.61553 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca7872c8-d92a-3f15-bff1-6f15d46c88e0 | -1.45273 | -54.96391 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f801c249-5fdb-3fee-ba4d-f22ac8e2dbaf | -3.41672 | -50.15811 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2735aa3f-56ea-3f2a-b529-04605f368769 | -3.14522 | -53.24821 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5ae8c57-c639-378c-a516-ec89a4ed0c4e | -1.47425 | -56.10072 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea82131-1dd8-3f9d-801b-a880cda74211 | -2.73021 | -54.11603 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fceb466c-a893-327a-9a9e-4e8e538bcebc | -3.72848 | -50.20899 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f80ee4b3-beac-3709-8c4d-39a6d765fbd3 | -3.2508 | -50.62256 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02fbc95d-7af4-3f2d-ada4-24472ee1153e | -3.61888 | -50.19186 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8cd2799-8541-36a1-b1dc-960f2b2ef9b0 | -1.2035 | -53.88235 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8ef22f1-471c-3236-8715-f46cfc354f8d | -1.07213 | -53.64447 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19987e4c-ebd1-380e-bbe6-f7a384e37eb2 | -2.85114 | -54.09888 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb661269-3735-39c2-b966-61929debc70f | -2.69577 | -56.90076 | 2024-11-30 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3876c86-985d-3026-a60f-74f75859979c | -3.38736 | -54.28576 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c78cc6e5-e217-341a-a7b3-6d700e5a0729 | -1.14704 | -53.68105 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f54b13a-a3a3-3ca5-b496-a8f0e5b4a632 | -3.78411 | -52.40357 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a487ab7-e0ce-3551-bbb7-dc12b6fce49e | -3.08068 | -53.28377 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f0947cd-c383-34b7-8e2d-7d224a3f4523 | -3.21573 | -53.62661 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a279406e-984e-3525-a546-bde204f27d31 | -3.73898 | -51.83547 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87ccd2fb-2987-310d-95c2-d28e1e693e5f | -3.18783 | -50.30065 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea8ffeb5-7120-3d39-97c7-6bb9dbee3102 | -2.80513 | -51.58507 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d6dbe68-3eb9-3aa6-a5a2-9a22adb9c5f8 | -1.68054 | -47.8501 | 2024-11-30 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35be9a45-428b-3a78-b1a7-3a3d08b12ad8 | -2.84209 | -54.02579 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83d52e5a-47c6-30e5-bd21-eb59a157afa1 | -3.07786 | -53.25713 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e469a27b-9d5e-3e1e-b1b4-fd84417f02be | -1.23611 | -51.61035 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89a46a66-0060-3af2-9cf2-a2b8083fcaad | -2.72354 | -54.11498 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc00f81d-e6b6-398b-a701-607e0e1d21b6 | -0.94442 | -51.65994 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44430d07-0834-3101-87ff-7a8a9d9a957b | -3.89407 | -50.07143 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 969c59cf-0e48-3a23-8e98-6e73cc4979c0 | -2.88328 | -54.00347 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 041fa128-75f5-38e1-9a2e-ea85ed664cb2 | -2.60067 | -54.35874 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1888c57-b153-3747-9da7-97581fb3bc10 | -2.06088 | -51.19216 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3547ae32-2141-3752-ab4c-5acd87ef68c0 | -3.20297 | -46.5626 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90a03c74-152b-38d7-b641-9ec77c5db05e | -3.05921 | -53.84619 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58312e37-bc4a-3a8d-9153-9fde612e34cd | -1.49233 | -52.44097 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 699f0d8d-6ba9-358f-a29c-f395ef9687e8 | -3.09505 | -54.55002 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d8f937e-c06a-335e-8ee1-dfbd53736d9a | -3.13299 | -53.68304 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3eb86da4-cf25-3639-acb2-daf46d28e3a1 | -1.38583 | -55.02417 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33ed50aa-f64b-3a44-b3d6-f963a9a342e8 | -1.51424 | -52.62877 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a845d5e8-d317-3df4-adc8-8a3e0601b4cf | -2.8478 | -54.09837 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 147c4b89-36c7-31d6-a8a1-7b3f3a77ef37 | -0.04472 | -51.73953 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01285f81-4f50-3d6e-b10b-97ef15f67a9f | -3.22867 | -53.63239 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1409f0cd-d317-3dcc-b622-5e3399fa445d | -0.76287 | -52.45522 | 2024-11-30 05:01:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5edfabf7-9494-32aa-a094-d84f8ca0a0ba | -3.03454 | -54.04811 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ee22dd5-9057-3768-be5e-98f1dfde5804 | -2.6053 | -54.00307 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47b086d5-f150-3092-a193-00240136b2dd | -4.02063 | -46.99483 | 2024-11-30 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39f5de00-cd9e-3d44-a04f-300eaf070941 | -1.5279 | -52.03226 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9566f5f1-f065-3c84-83ca-b0b1cff13b5a | -1.62147 | -53.86881 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d565b8d4-c3ac-3a0b-aa9f-6ee4f92c9ae5 | -4.88565 | -41.29721 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 15f123f0-aa90-3ebb-8bf4-d4bc0c4d2694 | -3.01246 | -53.22823 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fabdfd6-a7ab-3aa7-a0f2-2b59ab1c187f | -2.59903 | -54.36914 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5deb442-6b00-3c2b-92ca-4b3b42b61ce9 | -3.11009 | -53.80695 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README101.md)
