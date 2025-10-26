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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7bb3b8c-28c5-33cc-91fa-3a7e9da2532b | -4.82978 | -49.35074 | 2025-10-26 04:49:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48b53e36-5dfd-304a-9502-aa24bdeeda7d | -3.78732 | -43.40735 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0389927-9cea-38a9-8ce8-2ce15c4e344c | -6.3932 | -45.77512 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6678dad2-5329-3943-8508-ed777a9123dc | -4.83386 | -50.92895 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68e46e32-96ab-3113-aa9b-2c7250723a95 | -2.32136 | -49.1664 | 2025-10-26 04:49:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b32bcdc2-4edc-39c7-8233-d521740bdddb | -3.25975 | -50.04549 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25f2aa12-b370-3246-8770-0f966464acc5 | -0.16564 | -50.40785 | 2025-10-26 04:49:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f6bae11-757d-3cc2-8d4f-9073e3c08268 | -7.34744 | -42.44522 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 95347874-042d-37d9-a637-9a65f1849da7 | -3.41361 | -52.83268 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 601e528b-7018-3b82-90bf-8b0654a31649 | -6.43222 | -42.02668 | 2025-10-26 04:49:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 43d5a71c-cad3-39d7-a7bb-72f8c63f5f3a | -3.45961 | -52.03979 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f52bea0d-630d-3a25-8e49-3a37527a8215 | -2.65442 | -48.51029 | 2025-10-26 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d5ae3333-6e75-3b5a-8215-396a74b87c5d | -4.68345 | -42.7264 | 2025-10-26 04:49:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf2e3f43-9792-37f5-9e51-5ee076d2c9f4 | -4.17699 | -47.78383 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19b01088-841b-3eab-aed6-5467f96a8738 | -6.55201 | -43.23599 | 2025-10-26 04:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ddd6b985-c8b7-36a3-ad30-4def7ef6ef75 | -4.89899 | -43.24813 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b9e64042-ab91-361e-86d6-4a3f25e61479 | -3.85171 | -51.384 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b92c3d2-f718-31e7-a6c1-cdae4f222f8c | -3.75614 | -52.25906 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81062a63-c5d8-3a77-84c9-f724ab3ff033 | -4.60505 | -48.78719 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c894e37e-2652-3a93-8d35-65fb3d93b6aa | -1.75059 | -55.74332 | 2025-10-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cc4428d-ca22-393d-acb5-c30f2519b7c0 | -3.92706 | -52.25116 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b0a0dcd-a33a-3635-b8e9-311d9319538a | -3.83891 | -50.20003 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38037813-5e26-3df6-af1b-b33bac417999 | -4.03568 | -46.06999 | 2025-10-26 04:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c383457c-1803-389b-8d40-d5ae0cc49518 | -6.08336 | -52.26083 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48ec803f-f22d-398e-a50a-be11d01693f1 | -5.70932 | -49.30902 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a1fe8a7-b748-326d-9c2a-f65da559418f | -5.71014 | -49.27959 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1447a7d-91eb-3a40-932e-4c675f5691cc | -4.74067 | -50.8714 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b7f5f6-930f-3c0d-9602-0d83b75e7d09 | -2.87169 | -52.79464 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20c57760-7c2b-3ed0-a91e-f929d93abaef | -4.58196 | -49.40797 | 2025-10-26 04:49:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa473760-24a1-328e-a6e3-7a18d1853020 | -6.44121 | -45.7299 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79e43041-9927-3357-bc67-b1e48a09f145 | -3.12016 | -49.1089 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d57518-81dd-3de3-a306-80a9d7ff1ecb | -5.9149 | -45.41246 | 2025-10-26 04:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef76db73-5208-3943-9a79-50a687ab1ebc | -4.15643 | -47.65892 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4abc444b-e971-3570-bc60-0d2d5b79dd25 | -3.67593 | -52.04949 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56ae7d85-adb4-3bcf-963a-570749af6d9a | -6.18027 | -49.23997 | 2025-10-26 04:49:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cd354c1-1eb7-3c6c-9c06-9ed8896483ab | -4.70966 | -46.4259 | 2025-10-26 04:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 441a91f0-49fd-3030-a991-239b76ab6a78 | -5.61243 | -42.77895 | 2025-10-26 04:49:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bca0ceb4-eb80-35a7-ae1c-7f1602607065 | -3.76274 | -52.26009 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4379d55-5437-362e-9c23-b9453a729e2a | -3.84894 | -51.38004 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b561f154-2816-32a1-a308-28ea03298148 | -2.76944 | -45.09062 | 2025-10-26 04:49:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d501165-197e-35c5-ae4e-e28dc971eeee | -6.69954 | -44.31245 | 2025-10-26 04:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d2663f1-c867-3573-a24c-d60559f97e0f | -4.73787 | -50.86732 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcc36d14-7902-385a-b9c2-2434bf4a9ec8 | -3.41578 | -45.46147 | 2025-10-26 04:49:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9f5dd08a-57fc-30a5-ae7a-1ffb110f9d0f | -3.24198 | -50.64749 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 979b3ab8-5eff-318f-bb53-5bfcd6cc0a66 | -3.10637 | -49.46608 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1901cb46-1cd0-3929-8514-2619e0486f32 | -3.23864 | -50.64698 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dd628f9a-8cd9-365a-a281-3fe05b6d4b71 | -3.26653 | -50.04652 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2d86d74-f6d1-3815-97c1-bca8a50d3327 | -5.82879 | -40.80976 | 2025-10-26 04:49:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5fcec49d-ba6c-3d92-910c-cd2854bdf81e | -4.89325 | -43.25067 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6a840afc-c2d6-3c54-9b68-49afea141253 | -3.09396 | -49.46117 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76f7c823-05f1-3a38-a585-47882e22eb90 | 1.60882 | -55.75935 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4806b4f-20da-3d15-987b-7c03c60a1727 | -3.69397 | -49.54947 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc3344b8-74c5-3bc4-b5c5-a6bf33d1514a | -3.08567 | -49.51424 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| faf70e6c-58c4-3362-851d-7a0ff0bd1970 | -3.45441 | -49.69207 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4b4ff9b-13fa-369e-9968-21b75831b15e | -2.76877 | -45.09506 | 2025-10-26 04:49:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd48527f-2031-3c76-b8f5-9924d167c2a7 | -1.28285 | -55.77755 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c48e0d-01ce-34e4-8132-907828b418c5 | -5.11203 | -43.18703 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b4c2df6-c23b-3eb5-8b37-3c06c903a9db | -5.1181 | -43.1964 | 2025-10-26 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 9d540e24-b45a-300e-9a16-816a316ecddd | -17.3165 | -43.643 | 2025-10-26 04:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 96956164-a2fa-307b-a788-3224c8b87d5f | -5.0994 | -43.1977 | 2025-10-26 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d2668da4-0e69-3ca4-8133-0e360620276b | -6.3864 | -45.7819 | 2025-10-26 04:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 7ca0c021-10a2-3023-a4c1-1919bf720afc | -17.3365 | -43.6383 | 2025-10-26 04:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 68b7bde5-30a1-3d6c-867e-9c24f73da9c5 | -13.25432 | -47.98553 | 2025-10-26 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d982335-5f90-3629-80b1-6d8a4e253a3c | -10.51416 | -43.25595 | 2025-10-26 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba2521d6-4e6d-3366-bdd8-5ab4a34067dd | -9.26137 | -45.59111 | 2025-10-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1bf0882-bb43-3a2b-a5bc-d5c6af20b589 | -9.44505 | -56.64551 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 937bca1e-4dd3-382c-afa7-56814e836557 | -14.58369 | -44.14119 | 2025-10-26 04:51:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 02806d3d-ebb0-3280-b84f-5d63179ffd39 | -7.80316 | -45.39298 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a38cdc3c-45e7-3480-b4c9-ecde3454f043 | -8.15806 | -47.74667 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 295c0dbb-f3eb-310c-af53-b0ca6d0e7ad0 | -11.11571 | -43.22906 | 2025-10-26 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 414111f3-45d7-3a74-b0d0-be79ac6eda61 | -10.89578 | -48.02721 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd99845b-dfcc-306c-ae42-a2d49dcc7e4f | -9.57203 | -46.92359 | 2025-10-26 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 427ad4de-0a32-36b6-a75b-0b6cd87b875c | -6.53793 | -54.97067 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dc7ea52-2cd6-3afb-bf92-09b28c47a945 | -10.51367 | -43.25987 | 2025-10-26 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47cd2b8f-0601-3ba0-9b64-f5e495d483c4 | -7.65111 | -42.17033 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b089ea60-3029-3be3-88b8-440a181885ac | -7.93585 | -55.01812 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41a88aff-c3da-3acf-ab16-02ee81744dca | -11.53724 | -47.09957 | 2025-10-26 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51379d42-ebf1-31d2-8164-4f8c7e1f0a6a | -9.15028 | -51.30802 | 2025-10-26 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c1edddb-9796-3548-94ac-f728cafc8750 | -12.59247 | -52.85334 | 2025-10-26 04:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1028467d-6e54-3dd6-8d79-a57f92bb681e | -9.46181 | -47.72673 | 2025-10-26 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3113f5e9-174a-3f6f-b9f0-c6b682ee0d89 | -11.48605 | -54.02302 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36106bc6-f35f-3a60-b1ca-da0c6b7f728d | -7.84241 | -46.43237 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 287da2c7-f341-3eaa-9a32-6c339a4d6909 | -13.53806 | -49.54306 | 2025-10-26 04:51:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24ee2cc0-be74-3be6-a911-34d9f0701a17 | -8.08334 | -46.95661 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c1a3792-f7d3-325a-ab44-2473108a0746 | -7.78364 | -45.38383 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc14a39b-8362-3c22-8bf1-a6b5da435f74 | -13.19692 | -48.44286 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce78b424-2bdc-30fb-9de1-51a30e338562 | -9.44434 | -56.64983 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8da5ff8-80c7-3141-91c5-76e2fd2da0a6 | -8.96272 | -50.32917 | 2025-10-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e1f069f-4e10-3872-aa4a-c6c8c9f364a2 | -10.39819 | -57.32446 | 2025-10-26 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d999a377-b3b5-3241-afce-67152c8a3311 | -8.60975 | -54.65741 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0121ebb9-9652-3555-a594-9df01c1212fa | -11.21288 | -54.83949 | 2025-10-26 04:51:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08889929-d46a-3444-8065-03bc30aea595 | -11.54143 | -49.43209 | 2025-10-26 04:51:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c38baa3-875c-3136-8ec6-e03ab38e1884 | -12.86471 | -48.65383 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42e4f050-ae34-3bae-9bc1-8be70465ccaa | -13.92773 | -48.40063 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bee3e020-30ea-372e-a7f6-27e0110165df | -10.88297 | -48.02822 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4760ec43-be3f-3619-b338-f8e0dfed5613 | -7.78294 | -45.38882 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 810349ba-3cd3-3a75-98c8-467d0fcf4e1c | -11.14338 | -49.93949 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f2bd0d8-366f-3278-9632-0f47744a7758 | -11.02259 | -47.86421 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5cce1d42-2fb9-3d93-a0d7-cf6f68e9af82 | -10.75682 | -49.78779 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8431ce3-1b04-3966-89e5-289929d737fc | -11.45924 | -54.29967 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
