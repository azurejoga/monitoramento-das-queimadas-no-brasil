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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14e99a39-92a3-36d9-b521-dc13bfee89d8 | -4.43287 | -46.58783 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82d5391f-056d-3866-a606-608653b596c3 | -3.59978 | -51.56363 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2bff37f-e7ec-3e27-bbc9-5382fb502103 | -3.10096 | -53.7445 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6758977a-be5e-3c58-83f0-e7056452d0e6 | -5.10899 | -43.16565 | 2024-11-22 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 114b2e35-b2a0-39c6-bba1-d44ba850f9da | -2.8413 | -54.01354 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95e6f899-9501-365e-818b-d55b0c35d716 | -2.22659 | -50.39289 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bfad826-9cd9-3672-a18e-a97ea264d452 | -2.71884 | -46.09301 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2eafd325-f400-3ebb-a7ba-0cbfe4a89637 | -2.35593 | -49.09095 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46e8bdb6-8155-3f65-a95b-2330c8f8d850 | -2.69728 | -46.09367 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 955dd06b-8f4e-32ff-a119-53d54276e5be | -2.08019 | -48.87805 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d100e76-7fca-3914-9b1b-53acf3200204 | -2.83161 | -46.67739 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a03dcab-9925-34f7-8d0f-481fe74a1776 | -2.15608 | -50.46213 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feb5b48b-bd70-33d7-85b0-ee3a2bbc7d26 | -2.56303 | -54.00066 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 249c5ace-a733-3d74-bb88-9aa83b7b3686 | -2.07603 | -50.32499 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 119145d2-b8e0-3dbb-9f1f-2aa8d6450155 | -1.50198 | -51.56472 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0830d8b4-6321-3a4c-b2f0-3c06f9702370 | -1.40058 | -52.96249 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eefd49e-5692-3aba-93d2-845b53dca352 | -3.86575 | -49.89913 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b9323b6-dd50-3a21-8f0c-e06050dc66a8 | -3.60042 | -51.55964 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917385a2-ae62-3cd8-a46f-f7152d3bd06d | -2.55877 | -48.16804 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aa7ba8d-6075-3649-80c5-e8544416f2c8 | -1.49103 | -49.68137 | 2024-11-22 04:36:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f063c01-0f73-3965-a1c2-e61b90d1e948 | -2.52417 | -46.4034 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fff6f1fe-f353-37ac-ad4d-6f86a94da0ea | -3.90313 | -40.98028 | 2024-11-22 04:36:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 66890362-d765-362d-998c-2539dbfbc617 | -5.19793 | -44.22342 | 2024-11-22 04:36:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fecbe587-4bbe-3d0c-925f-5a3a0f1b9ed2 | -1.84889 | -53.69947 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71db03d2-0712-3f75-85b6-a156a76530c5 | -2.31374 | -52.49358 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be281065-57b6-3fdf-af45-246a3a9acb78 | -5.95228 | -48.05826 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c063343-3459-3f4a-8fb4-db95a68c9daf | -3.10024 | -54.29469 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8dd5f87-92cf-386f-8bac-5278256613f7 | -2.64911 | -46.14238 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 952a86d9-7a25-3013-bbd7-ea7d3adfd062 | -2.19821 | -53.65264 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a460a0d9-d6ea-34bd-bc8f-7d9b83a31ca9 | -3.64585 | -51.45684 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70b4f669-d31a-3e82-b0f7-01d8ad86c8b9 | -4.06669 | -50.0032 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58b0d50e-9b6c-3596-bef6-f5c432dbc75d | -2.22377 | -50.38865 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0156a57a-7e2b-3f2a-a474-33357182bd69 | -2.55483 | -47.32673 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec912729-daba-3f7a-bbfd-ee0d44ec7ae2 | -3.52324 | -54.64977 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75a2300c-4708-3f8a-b84b-a9dd9f646139 | -2.22373 | -50.38913 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e8192a0-53c7-38fc-ba22-f7b4a4f5c669 | -0.92376 | -51.73516 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67eecbdd-c24b-341c-a919-a8d7c1ee90e8 | -3.85173 | -52.35022 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae589592-3d48-3005-8c87-781eafc40c85 | -2.61634 | -54.01319 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 698b0865-a39a-3f9c-9f2b-c6c5b613c444 | -1.22181 | -51.79671 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93e2c064-dd8d-3c11-b4b9-2ea740aeaa18 | -3.32703 | -54.09853 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 39fc89a7-cec3-3520-8688-bdd934f60db3 | -3.03473 | -54.8491 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bba0a259-a6d0-358a-a814-311055c336e7 | -3.46678 | -45.91038 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5c9b2b2-4857-3969-92fe-3e0bbd59a00b | -1.87657 | -54.36436 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e44b16-37d0-395d-9f3c-47bfa67ae7f1 | -0.92458 | -51.73716 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdf301b4-c30d-3120-ac5a-c1538f5e75c8 | -1.76773 | -52.70498 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f764026b-4f18-30d1-bd40-b8c1545b7bc9 | -2.57673 | -48.20616 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 428fc7f1-05bc-3ae5-a918-8d98ab0c646e | -3.40468 | -46.24038 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18a9b54-cdb7-3e53-a470-b13c01fba5bc | -3.43194 | -54.60003 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1d064e3-1e30-3f03-be4f-0f992dbee162 | -1.19477 | -51.94542 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2a10460d-0e37-35fa-8fe3-5af3fe998ae1 | -4.13673 | -54.66399 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1337433-f4f3-3f16-820e-9a5b70289ce4 | -1.61916 | -52.42528 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1865cf5-06dc-3376-97c3-9dd40f9df8a8 | -3.33837 | -53.32948 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 00555efa-871c-3379-8b0e-c6ef35ba6f4a | -3.96302 | -43.00358 | 2024-11-22 04:36:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5925d1d4-7733-33be-8289-e639d3c232ad | -2.24321 | -48.5553 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95fefa24-8aed-3f61-a614-b49d278ff5de | -2.92119 | -48.32746 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cceea02d-3f85-3dde-a411-cc0684bc666e | -2.83788 | -46.68215 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58258a76-9dda-351d-88d9-3dcefdd5905d | -4.71023 | -48.68122 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ced90877-5f7b-365a-b9ff-76d7177e2b47 | -2.74689 | -51.87962 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c6d53675-61f3-36bf-b5b0-41a8ebd89d3e | -2.57988 | -49.22204 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 062ac66b-bab0-3907-a20e-12f88b4e017c | -3.03249 | -53.72782 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0c06030-eb8d-363e-9499-c5a340a72268 | -2.73513 | -47.54157 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b91373e7-dd84-31c3-a78e-9a58de36aab3 | -4.1409 | -54.66505 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f26400b-76ff-3d41-99c6-fb1d203cef43 | -2.38603 | -46.81668 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff19d713-4db2-3f78-903f-11255e648351 | -1.33208 | -52.42937 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dea283f-940c-3e7f-bc98-28f63e3e636e | -3.54715 | -51.53172 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07ff0b8f-f34b-360b-ae50-ca339a786752 | -2.58597 | -54.04351 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7cba7059-4414-3a89-bb0f-c1c18d0f478c | -2.29607 | -50.66 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc73fb01-257c-357c-ad71-a7882d361cfe | -0.63749 | -52.35865 | 2024-11-22 04:36:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e8dbfff-c1a4-3fae-b6e2-a82aeda10d97 | -3.59315 | -43.63599 | 2024-11-22 04:36:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64d7c42c-7b87-3de4-81cc-cfb1cda2831b | -2.08749 | -46.32685 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57a745c4-b729-383c-a84f-f78dc4ec18c6 | -4.35986 | -50.8697 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6258efb6-8814-33e9-9748-d482dccca192 | -3.10666 | -53.99042 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e643da-f4a2-3c1d-b37f-077f3a758304 | -1.9016 | -50.92265 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37e41f4b-5f27-3661-8cf4-fde7eeb67060 | -2.26534 | -50.8069 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da459cdf-49a3-3aba-bb09-656e4671488f | -1.14883 | -54.17802 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ba0a64c-aa05-3ac6-b0c7-1527cc99bd43 | -2.09697 | -50.36993 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90379829-f238-3994-883c-46afdfe80c63 | -4.07869 | -46.8381 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 013c4adc-f0a2-3ccd-b60d-5c1dc45fcd3f | -3.853 | -51.40779 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80ba1ee7-cf00-3918-b6c6-e546aed0bdad | -2.35524 | -48.55526 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e539c72e-c6ad-3a94-b1b1-439c5aa856e1 | -1.94364 | -49.52656 | 2024-11-22 04:36:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39207999-e62c-33b5-82c9-ccdb8cea2d8f | -2.31446 | -52.48896 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3f0f826-5c3c-3d0f-8fb3-cb552642b565 | -1.20678 | -51.77211 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95d20bfa-8a8c-3ed4-a1c0-482bf823bdee | -1.47588 | -51.09609 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a89f410-fe6e-3f82-8d4f-d18de6e259ec | -2.81413 | -54.02438 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88084e2a-8a8c-3243-a6a4-914a0f2bf407 | -2.4116 | -50.35389 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b900be3-6689-3ba7-b055-5bec4d62a9a0 | -1.08896 | -53.13285 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e371608-e5d6-34ca-8f02-777f2314ca5a | -4.40696 | -44.12322 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18e2a6b4-6ee1-3a95-bebd-8a331c7e1337 | -2.15147 | -50.46904 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a784c716-551f-33b7-b466-ea1ab813e21e | -3.18347 | -54.31618 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b8588fa0-bf13-3464-891b-65308cd1feb6 | -3.87129 | -52.36381 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8716963e-36f8-3e29-8101-5633d996eadf | -1.19942 | -51.77094 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a4ae566-a8fb-393d-b2f2-9b7917239375 | -1.19408 | -51.94984 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2e55f532-c7b7-374a-a652-dadd8c130d48 | -4.08351 | -46.84965 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7405436-64a8-379c-a9b8-516c8557395b | -2.2184 | -50.6868 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f488fc7-1811-3673-b388-0e8faca31bac | -4.43995 | -48.45538 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bc0d1e1-69a7-3d54-89bf-2ad5ef0f227a | -3.00417 | -51.55391 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d696375-403d-3f27-9c50-9ade58b759f9 | -3.53786 | -52.78867 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 442d9650-37fa-36a7-b462-4e949db55c89 | -3.33364 | -53.33385 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74774354-4c3d-3e26-a690-cdced04233b3 | -2.70263 | -46.24393 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb4f30ea-54b5-3edb-8573-defa373bdaff | -0.90795 | -51.65023 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README31.md)
