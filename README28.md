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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e68d8b7-8e20-3241-8bf4-f161c53a92c2 | -2.72071 | -46.25212 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1514769-f934-3790-a370-2f787c1ffb36 | -6.07923 | -48.04403 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51a94749-518d-30de-a699-ccc57ee900da | -1.69808 | -47.90295 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b80f94-7e13-3e17-8b3c-07d92bf82ca5 | -2.57799 | -47.02374 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a16031cc-363f-3826-8406-f3a0623988e5 | -2.02297 | -51.16571 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aac1410-5312-3068-a145-3d56768cce0d | -2.72362 | -46.25659 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95aa50bb-e213-31c4-ad68-9e557c1dfd98 | -3.2901 | -54.12988 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6065576-bfd3-3eff-a319-96d4351ce435 | -3.8231 | -46.54836 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8806e17e-dada-3a41-9ef1-051d4342cc6d | -3.2194 | -54.18084 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20493c86-d9cb-3455-89e8-f66361824c7e | -4.87781 | -41.30741 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f0a11a71-f963-3b26-9ebb-29b3cbb04a75 | -2.637 | -46.95771 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8430c90-7dbf-398d-92a6-03a1b702507c | -2.59198 | -46.56864 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c852364-d503-3ad6-b3c0-81cbc7bfd4a8 | -4.47718 | -48.1141 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31fd00de-66b6-3a29-b310-4e12260e81a7 | -2.14783 | -46.49075 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86db28fb-0368-3bb5-b833-599321eff302 | -1.07749 | -53.63733 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bddf06e3-7c7b-3c92-a8c0-c49990343646 | -2.97569 | -53.29354 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0110032-c9fc-3d63-bea9-6692a3f31b70 | -4.64693 | -47.13856 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dc23c03-9412-3578-b771-ea64d526e395 | -1.29169 | -51.37045 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a422b8f7-714c-37c2-8201-b5972e0a0ab3 | -3.24742 | -53.6356 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3346ad4-ce0c-3f16-ba9c-3e8f3a791297 | -3.28847 | -53.27634 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f200de92-71be-3fa2-b3fd-829282f32ad8 | -3.03055 | -49.52116 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3dc2cb9-4c5c-3420-a8b5-5b3bf4d61dfd | -3.49893 | -53.79616 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7d2f8327-fe6d-36e6-b4d4-2672c4478f58 | -3.8431 | -46.51836 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ecfb751-2714-3694-9170-ecb3440457e2 | -3.66594 | -53.50987 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 066aade7-35cf-37f0-aba2-0dd365d34c29 | -2.43029 | -46.5441 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3856062-5ef4-3663-9ec4-9e62b5147bff | -3.94218 | -49.7603 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e53a39a8-0c30-3744-8586-e9074f881899 | -1.32458 | -54.63634 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 20a06c50-984a-33bd-a7a8-ec460f7ba76c | -2.95998 | -53.72041 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7e81a5a-674a-3133-a0f2-601fc3c6e05b | -2.08479 | -48.54173 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee023c9d-0b95-32e2-831b-99a6ce5b6ea0 | -2.73941 | -47.98614 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80c87df6-99b1-3427-982a-5352906caad9 | -1.50303 | -51.93546 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2424a7df-ffbe-3d63-852b-d39b13a61172 | -1.65215 | -52.73243 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a386021-8cae-3e8d-adb9-66051f8ce7ad | -3.49861 | -52.91067 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2318b880-0779-39df-80e1-7f1a225e5ff9 | -2.08686 | -50.64178 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b36acc0a-4b9f-37d8-9713-a1df4abe8033 | -4.17846 | -48.61826 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69b2e055-e493-3449-9b50-3e188c4a89cb | -3.71251 | -47.14884 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6671844-4081-39ae-af81-7c266e780f69 | -3.25538 | -53.28596 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f75c2f8d-e094-3730-b967-31fb73946226 | -2.98067 | -53.89798 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca171604-b541-3028-a004-5dec2f45d183 | -2.50293 | -52.15371 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7da73a1-6d61-3dc8-ab9b-0753bc731924 | -2.00205 | -52.0983 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa363556-a546-34f5-87da-02bf9d252ba0 | -3.14209 | -46.61819 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06255747-8e58-3045-bd9b-fd3d53b42102 | -2.88795 | -54.16516 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 961e9b98-ce63-3912-962a-954282982f07 | -2.66132 | -46.57068 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb9ebc4f-6738-34fb-a75d-875741078cd9 | -5.73504 | -46.6219 | 2024-11-30 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47701253-1622-340b-b4b5-c3864609c8e7 | -2.88436 | -54.21325 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c38ecbe1-a939-35d6-8e2c-2602639a04a9 | -2.46718 | -46.5575 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1733739b-bd0c-3d56-b75a-979fc90d8166 | -3.11137 | -53.8091 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4201e436-3e01-3f60-a1f9-e89d6b9a7739 | -4.21012 | -50.69358 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d1a4087-8268-302f-a8d7-058e22363f7c | -2.27879 | -48.49854 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82a1a1a5-df08-38f9-929b-e261f8061bd9 | -3.27923 | -50.64874 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72d7b457-cb09-3ee3-affe-194916b774ad | -2.92008 | -48.33409 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 348621af-3ba7-3781-b73e-aef82cd4a295 | -2.24486 | -46.45098 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1f1fe85-db94-3e50-9df9-1e0645951a6e | -2.99876 | -50.50945 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72863338-aa3f-31a5-bf2a-a58cdbccf22f | -3.62301 | -42.73464 | 2024-11-30 04:40:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3dd2a825-956b-3c12-bea5-2c3024ec040e | -6.14009 | -43.95375 | 2024-11-30 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 895b0f85-50d8-3b02-b66b-4e9c790400e7 | -2.89831 | -54.7685 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d97af41-da7b-3b45-a663-325a23cd5f54 | -3.09643 | -54.29614 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 128eb011-1963-3c72-9d25-1a697b8002eb | -3.61095 | -49.98624 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b303d046-7ef2-3ac7-bd46-3af1efbfdf0d | -3.07946 | -48.66574 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16da7d32-94fd-3103-b322-880c2e134e9c | -3.53896 | -50.18373 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81e430f9-adc8-3f27-9c71-33f06def7a34 | -1.57972 | -53.83929 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc13a4d4-79cf-3d2d-b987-19286f3f4b7f | -1.83258 | -46.30383 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 68fe7f48-d4f7-3973-a7a5-6084ac7cfe91 | -3.47272 | -54.16307 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c1ac100-f64a-354b-a4cd-774365f56e34 | -3.26385 | -51.62702 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f034d0b7-e23b-3f07-8acf-46b5b9c83182 | -3.78229 | -46.69688 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5bd5333a-6fb0-3440-8021-c296516c33cd | -1.91147 | -52.90593 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20f66af4-514f-306d-bf18-efeebfffb480 | -2.86662 | -53.98486 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c5a8286-de0b-370f-a8b5-bad52ce6a9f0 | -3.9557 | -46.91352 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b83f99c-6cae-33ed-8dd1-e4ebead72316 | -2.56347 | -54.31541 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 90efad55-69fa-3541-86ca-725896f8f4df | -2.75993 | -49.22771 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c96a550d-cba3-3368-a281-560ccc3ceae6 | -3.82636 | -46.59666 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c118d3e4-50a6-3948-b235-3f0be050606c | -2.76758 | -54.05732 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3d3ca7b-a537-3494-8549-0c898e51cd7f | -2.46198 | -46.56834 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc298758-3748-3c07-a722-ca852e459e8f | -1.89417 | -54.54264 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4315070d-98ad-3125-a214-79680a06dcb2 | -3.30139 | -50.37551 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 340c8a6a-cc45-3f0c-8aeb-b4dffe10870e | -3.27757 | -50.61504 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a463ca7-7c46-321f-b402-690a66a83772 | -1.61894 | -53.33003 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 241162aa-fd6e-3e0b-996d-87175b387788 | -3.02578 | -52.38112 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f48dda87-0efb-3519-9199-19d321b0962c | -3.79798 | -46.68753 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5ff73ff-b8c0-3209-8d68-e50315f2eab1 | -3.07313 | -50.33305 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 68921c32-3acd-3d71-b748-ed2261ead8a4 | -3.16308 | -46.29585 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa6c7912-2dca-3326-b8e9-c33abad9633f | -3.1915 | -54.32689 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05ef351a-c14c-32f3-ad72-5067c4296988 | -2.71786 | -48.62675 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2e1a142-4c83-356b-a570-97c18dca1198 | -3.19696 | -46.57534 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85999923-8bc1-3093-8602-c5ae0a193311 | -3.8101 | -46.58609 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71c66a25-bffd-3e91-902d-fcc31c57d39f | -4.06526 | -49.05957 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3eb248aa-9705-31a1-96bd-30937dd5d840 | -2.68026 | -46.28194 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55309dcb-11a7-3494-a8a6-b828ad565381 | -3.59375 | -49.98715 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eac18c21-c8da-3251-a01f-99940978ad59 | -3.26354 | -48.76873 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ad9492e-5a6f-3448-a86e-49dbb68aaf5a | -3.16247 | -46.29979 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ed423e8-868c-358e-8140-13082a54be6c | -3.86106 | -50.54 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfa70634-be08-36b2-ba2e-df2480dc04d4 | -3.67768 | -54.44912 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 419fe61e-de0a-3d6e-a0e6-7fe5b15d1ce9 | -3.06696 | -50.32845 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ff49389f-e295-387a-b3ce-c86bff4df4c3 | -3.73259 | -49.96937 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bee460af-3398-3efa-9a26-91f8c1af12a3 | -3.84096 | -59.57843 | 2024-11-30 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| baf7b041-785e-3440-afc6-0588242c1477 | -3.24584 | -53.64557 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b79e14f-9ca0-3fdf-9637-4ee943082d3a | -3.01459 | -49.53641 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60d80c4e-cac7-3579-9b3c-465fb4da9536 | -4.51933 | -45.723 | 2024-11-30 04:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a9e4ae9-18aa-35a5-937d-45fcf5bea53a | -3.24657 | -50.59167 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aa30d0d-a738-3f7c-82b6-303133ae6d37 | -1.97262 | -52.89114 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README29.md)
