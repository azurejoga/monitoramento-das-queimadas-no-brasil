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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47934ae7-bc2c-3295-8d36-6f87c7115ea4 | 1.73447 | -55.60633 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0952cebf-77d2-348f-b65a-fb93dbedbcfd | -2.81095 | -52.08426 | 2026-10-07 05:40:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 480153dd-2034-36bf-b9f2-323df6b28cd7 | -3.09369 | -54.29434 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fe3e7a49-ce15-39a1-a596-f78441350cb8 | -3.03282 | -53.92541 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0959c261-c2a6-337d-b7a9-205cf94daae3 | -3.73393 | -55.98437 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 586678fc-0303-35af-a3ba-ec3b247020ac | -3.54556 | -59.4793 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2878ef7-6bd9-36f8-99ea-06280cd7c1b6 | -3.69093 | -55.95448 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6950f944-1f1c-38fd-a8e8-83cd5f4f8247 | -3.59385 | -54.56309 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f66bc600-2b99-3185-a77c-6f90fc381c3b | -2.77916 | -54.08652 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9517edac-cf0d-39b1-a610-6659fef78728 | -3.07095 | -54.25642 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50bef0df-ea74-3b28-a557-45146b3cfc77 | -3.37939 | -58.1918 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a3f488-71e2-3357-8dbc-838991333694 | -2.78461 | -51.66774 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2708607d-0c1e-3499-aaad-65a5546349f8 | -3.77812 | -58.52232 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42de63e9-9300-30a1-89f5-2658fd6cbf48 | -3.51454 | -54.65528 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55a48964-41d4-36e5-96da-0427d0284ffb | -3.50932 | -54.65912 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74ef879d-8cdf-342b-89c2-13800e05bf5d | -4.15304 | -55.1535 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f30a76b6-6da4-32e9-8f44-fc70f88a88eb | -2.9506 | -54.15086 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bfb27a0-64be-3f13-877e-f4a657fa604e | -3.06777 | -54.24598 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1db2961a-957f-3029-b6b7-aad6cccdc0ca | -3.54548 | -50.09158 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3215e539-c127-384b-91d7-0c266c56ae1c | -4.15499 | -55.14064 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4559c3b7-7ae5-37b6-a0e5-479d1a6e73ef | -3.11547 | -53.7705 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a0cfaee-e929-397c-bc59-73b7ae68651b | -3.04535 | -53.87523 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df07bc6a-951b-3768-8002-ff500e423398 | -3.49256 | -54.61676 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59e21f5b-94b2-36e1-a1cf-544fe651fbbc | -3.0827 | -54.27298 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f4f3fa58-8a39-3db3-86cc-2c88ee3ac237 | -3.21992 | -53.88013 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 181a7d24-1516-3850-93d8-c055908d2ca6 | -4.14213 | -54.92161 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 585912a6-37ea-3c51-9143-e92c261a0d52 | -3.08832 | -54.2984 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c3f39c6-eba5-3bdb-baad-e2c4399b242f | 3.14197 | -60.59565 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52631f3-8139-3f1f-9ddb-fc582e7a3855 | -3.48192 | -55.43803 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fef6c8bd-f29e-3aba-a4cb-67f0cac3b084 | 3.1442 | -60.58816 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2621b73a-ceb3-3ee5-ab51-680a737d9914 | -4.1154 | -54.01921 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc788cc-81fa-33b1-a230-09a6e11742e6 | 2.43447 | -50.84651 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b7b39fc-80cd-3913-b517-24c482df0710 | -3.55816 | -59.48887 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae8ccda4-72e3-33ca-bb86-9c04cc406f82 | -3.73811 | -55.98094 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e3daee9-51b3-3140-b8e0-fc7793b71e44 | -2.81042 | -52.0877 | 2026-10-07 05:40:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e00cebf-20d8-349b-900c-495b7b0f0302 | -3.24122 | -56.8019 | 2026-10-07 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcf0873e-f1ad-3985-9673-d84932dc1af7 | 3.98309 | -59.67198 | 2026-10-07 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a70785b2-777e-3269-85d4-67319e740109 | -2.94033 | -54.11296 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4999dd48-5229-3f8c-82b0-2edc8500cb72 | -3.70439 | -59.64785 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 440d09bc-bc40-3147-9a15-45a31faf0c45 | -3.88613 | -55.83046 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d53b88ba-2e49-35cb-80fa-c1f5e70c4367 | -3.28945 | -54.03743 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 703154b8-da7c-3dc3-83c4-b1be83bcad7f | -3.26973 | -54.03279 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 01e3c921-6e67-3fe6-ac07-9017dbdd53e8 | -3.58547 | -54.30464 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9cbe7d26-7df7-3835-a3d2-c0fec115aeef | -3.98233 | -56.21448 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06e387c0-5d95-3834-8e0f-e1615058041f | -3.77899 | -59.19893 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 129e7c52-696b-3848-afff-76dfea081ace | -3.26814 | -50.41497 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc5d6cb5-e2b2-3386-9639-3ca0eafa2759 | -3.29446 | -54.06886 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c0c49c1e-9253-3850-8545-a7fe8daca9b9 | -3.07373 | -54.14285 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1241f52-ce0e-308e-8429-92333a005b14 | -3.53482 | -54.64419 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 424e073b-4261-3ade-88c2-7cc8f6846673 | -3.5507 | -59.49153 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7886cb37-9360-3b2e-80c1-1ab6d945648a | -3.09564 | -53.73299 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbd919e6-76ff-311c-9990-761f357076db | -3.50429 | -54.63 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b8c4a64-9132-3f0e-90e7-035b515ae697 | -3.43622 | -56.93597 | 2026-10-07 05:40:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9579af2-d139-3135-8f2e-d18f7cbf85b8 | -2.01706 | -56.89134 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5992113-fc71-3957-bb1f-1850e6b54f1e | -3.03774 | -54.25597 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bc7586b-713c-3324-b659-ff6c9039f6c7 | -3.67814 | -59.63623 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38e87a72-3677-3fc4-af3e-64828dc18ed1 | -3.27746 | -54.02024 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3bdc19b-5a0b-369a-bb8e-68fc04ca440e | -4.25153 | -50.73117 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eaab44e-97c6-3fc2-b5b4-3fe7a304dcb2 | -2.22092 | -58.11288 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43cb3ba3-3611-398b-9c21-786d59659ffc | -4.45367 | -54.96367 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc01ccf1-a81e-39ab-a339-026ac7f53fa8 | -3.50361 | -54.63461 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eddae8c3-0f57-31c6-9a57-631d1e443fe1 | -1.32449 | -56.40962 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2baff7bc-5d33-36e3-85b1-04609fc1d5f9 | -3.49086 | -59.58503 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1b403b7-02cf-3073-b28c-14f51c1c4de8 | -3.289 | -54.07303 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 38d61947-a962-3187-bade-f6a10a9cc751 | -4.14824 | -54.02929 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f35f49e-53f0-3017-9a94-5201569d69f3 | -2.98234 | -54.13075 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f70e2a60-f2ea-3e5d-b84a-eddffba7fe2f | -3.5394 | -54.64477 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f398dfd6-2515-3fd9-834d-1f109fa9a752 | -2.76585 | -54.07954 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2efef047-8cd3-34fc-88e8-6ea7bb6b96cf | -4.30648 | -50.78624 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381aaa9b-631f-3871-b11f-4b433dd36972 | -2.84165 | -54.06778 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 343c2f73-cde6-3f35-95ea-2f2d223327e7 | -3.10042 | -54.15649 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 434de6ac-698d-36b9-9b57-3572787bcad1 | -2.94134 | -54.16776 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fade180e-a00c-3686-a6c7-111b165e3086 | -3.2812 | -59.56488 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1994444a-3979-352b-8d15-0d7bfba9a7f5 | -3.2761 | -54.0542 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37eff43f-7b15-30fa-b341-7e61c993f530 | -3.28843 | -54.01158 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76a9170d-b7e0-3a2c-88ef-3a36288d3eb6 | -3.5068 | -54.64459 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd816bf7-d1d5-3dbe-9952-664bfdef4045 | -2.12935 | -54.79506 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 10656907-7ad7-3587-8381-3e2a12af5c6d | -2.98308 | -54.12587 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b07a6e8-5e7f-3936-9da3-55afb523af22 | -3.1714 | -50.43885 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72f04c23-ce22-35fe-96bb-bcd37a39d44b | -2.76438 | -54.08924 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a7c7dd4d-1d9c-3ef1-9a56-dc09ede8b241 | -3.7686 | -59.32116 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42cc6ef5-0755-303a-927a-da935ad84c12 | -2.60642 | -48.25982 | 2026-10-07 05:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7edae394-67f0-344e-9082-94899b13d6ac | -3.6557 | -59.16063 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bdc8804-c669-39bb-8bbc-f2c11036759f | -2.86868 | -54.20605 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57638da0-cb46-34e4-bb23-414484933ef6 | -2.95863 | -51.04716 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a5fb831-9112-33fb-85ec-e83b2ab7c21f | 0.70133 | -51.431 | 2026-10-07 05:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d0d3b85-8e83-3d31-8c79-679868b722c6 | 0.94218 | -50.20175 | 2026-10-07 05:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50b505eb-5356-331e-bba8-21144f01d63b | -3.27198 | -54.02455 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96c90ac7-e65f-3d8e-8b72-d4f1164594de | -3.66318 | -57.09469 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 156a400a-fe89-342f-b218-a15c03e6ea17 | -3.32926 | -54.18913 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7048d6d1-00ae-3969-8259-895b213a7a0b | -2.94304 | -54.16957 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fde9dec3-bc90-372e-b6eb-4a220800c1ad | -3.2806 | -59.20982 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0324706-6d84-3ca0-9569-0b32128700bc | -2.302 | -58.09898 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51525b89-7ded-3576-af63-17851b489303 | -3.49814 | -54.64108 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 369d140f-2787-3fff-8f66-0e8053d40875 | -2.9816 | -54.13563 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebfc3cf4-f4e1-34a5-86f8-b482daaf2b36 | -3.54038 | -59.48992 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f849da48-0d75-3c54-8c2a-92f94232397f | -3.51386 | -54.6599 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f9d28af4-4fc8-3775-8780-f8572008ce5b | -2.97694 | -54.13478 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e189064d-0a1b-37b0-ac32-43f8ceec8ec2 | -2.77374 | -54.09068 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d271faff-90a9-396c-96b2-8e8ee21e03e4 | -1.10571 | -54.15645 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README103.md)
