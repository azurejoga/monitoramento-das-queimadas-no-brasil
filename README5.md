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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 110359ae-b78a-3780-9316-07a0c98dfe6f | -4.702 | -46.4286 | 2025-10-26 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ac176417-6fa2-3ca3-bcc6-296e96a6c10c | -3.0909 | -49.4459 | 2025-10-26 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d628d4c7-4730-3924-8529-5a8f2a460760 | -2.7569 | -45.0842 | 2025-10-26 02:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 35.5 |
| d2af6dcc-6456-3463-bec7-0d4e7fe8b63d | -3.1094 | -49.4453 | 2025-10-26 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 087a8395-7d61-387a-907e-cc5260e6eb0c | -4.8933 | -43.2349 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e82544d5-1907-3439-9d94-405cdfbc39d4 | -3.1093 | -49.4665 | 2025-10-26 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 1d4497c9-28a9-3b12-91f2-57e0279ff642 | -2.7755 | -45.0835 | 2025-10-26 02:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 0a19d6b5-a9c9-36fd-885d-0a8f725f813f | -4.7206 | -46.4276 | 2025-10-26 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 242c1485-db3c-355f-84a1-6f82f33f4e11 | -5.1183 | -43.1731 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 649a61e5-64b9-3ace-8e65-fb421a0461b4 | -5.118 | -43.2198 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| be1a8957-dac7-3b9e-9315-32efa76ee6b8 | -6.7061 | -42.0517 | 2025-10-26 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 1df01d88-79b5-37dc-9501-0c8688344e06 | -17.3365 | -43.6383 | 2025-10-26 02:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 133.7 |
| bd8b4ba5-4371-3416-9fdf-c6c8e3477837 | -17.3158 | -43.6674 | 2025-10-26 02:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 68d4e408-02ec-3352-a21d-eff49dd7462a | -5.1181 | -43.1964 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 250.0 |
| 4ae4f10f-247c-3ed3-82d6-8c638c5228a3 | -5.0994 | -43.1977 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 254.0 |
| 9e21f628-012f-3929-9bfb-f95ca026db5b | -17.3158 | -43.6674 | 2025-10-26 02:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d8be4940-31ed-3539-bbf1-68c1610608e8 | -17.3365 | -43.6383 | 2025-10-26 02:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 45181cc0-43f3-3042-a21c-d92c0edc624e | -4.8931 | -43.2582 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 26a59872-55e9-3150-86b7-6b0eb9fdeb2e | -2.3178 | -48.5932 | 2025-10-26 02:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a61a1c52-f9e9-385f-97ca-042bcb64d4b2 | -2.7755 | -45.0835 | 2025-10-26 02:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 441d8136-9e76-3d6c-89f1-69e0997fb09c | -6.7061 | -42.0517 | 2025-10-26 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 49db1445-7c29-36e0-846e-041275045da4 | -2.7754 | -45.1061 | 2025-10-26 02:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4c0c53b7-696e-300f-ad9f-2c1afec6a28f | -4.702 | -46.4286 | 2025-10-26 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 66fa9ba7-2610-3998-ac8b-8b48bf5e1f86 | -2.7569 | -45.0842 | 2025-10-26 02:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 06021a1b-3edc-3d7d-af67-37c1f0225615 | -13.5405 | -43.0077 | 2025-10-26 02:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 79.4 |
| ff9c36c5-7869-36c0-926b-064bade9c8a3 | -10.6167 | -63.4545 | 2025-10-26 02:20:00 | GOES-19 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f327d509-cf24-32b8-aba0-e0ca5d33ccd4 | -2.3178 | -48.5717 | 2025-10-26 02:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 0249d016-9fa1-3373-a973-4428539d9d16 | -4.8933 | -43.2349 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 87ea0f33-e75a-328b-b6ec-45531183adcc | -5.118 | -43.2198 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a2d5d761-2163-3a11-a709-ff780e7ab8e9 | -3.1094 | -49.4453 | 2025-10-26 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| d5672171-7a3a-3894-adf2-85b52d42efc6 | -17.3165 | -43.643 | 2025-10-26 02:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 214.0 |
| b09872f0-8362-36b9-b355-892270ee0333 | -3.7661 | -47.5727 | 2025-10-26 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2076f068-2989-3588-8c93-ab11cec48506 | -2.7568 | -45.1067 | 2025-10-26 02:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 5a6ad7ca-df9a-3e8c-b159-f7a4b6d0fb3e | -17.3359 | -43.6628 | 2025-10-26 02:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ad602094-0fdb-3a74-b7cf-58faaf1f2873 | -5.0996 | -43.1744 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 1c276bd1-bd7b-3d8c-8ca9-0c81a151101d | -3.1093 | -49.4665 | 2025-10-26 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| df8c4c6e-7007-3440-8e81-016654f3537d | -5.1183 | -43.1731 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| aeec191f-b9af-38ed-bc4a-f0df7743ef39 | -5.0992 | -43.2211 | 2025-10-26 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a2a0e9f1-6b6f-351f-a330-b78c775b9e1b | -10.6165 | -63.4735 | 2025-10-26 02:20:00 | GOES-19 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 449fe49f-7b1d-35f6-b6a5-869e37f0bcfd | -17.3359 | -43.6628 | 2025-10-26 02:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8197a92e-7bfc-31ec-87ab-f1b53d4ce4e6 | -2.7569 | -45.0842 | 2025-10-26 02:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 96361145-5a3b-3968-9c67-23424cab82cf | -2.7754 | -45.1061 | 2025-10-26 02:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c768e384-9f39-38a2-af9c-cb22d28c1bbc | -2.3178 | -48.5717 | 2025-10-26 02:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 402876b8-bcea-3bd4-9f87-331e77213a84 | -3.0908 | -49.4671 | 2025-10-26 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 4718f993-c7c8-3009-a1a6-28ce134f2736 | -3.1093 | -49.4665 | 2025-10-26 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2172ff8c-5b1e-39e7-affe-76506419026c | -10.6165 | -63.4735 | 2025-10-26 02:30:00 | GOES-19 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1222559d-83fa-3f14-aabc-67e23460d639 | -4.8931 | -43.2582 | 2025-10-26 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 039c5afb-0e9e-3794-a1c6-4578c10b2f2a | -17.3365 | -43.6383 | 2025-10-26 02:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 7b1ba99d-8262-36b5-93f4-ac9aa0f79b2c | -2.7755 | -45.0835 | 2025-10-26 02:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 39afdba5-03a8-3fac-96f5-0750b4717169 | -2.3178 | -48.5932 | 2025-10-26 02:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| d60f0257-d14b-3d8c-8f44-b16fadbc1e76 | -17.3165 | -43.643 | 2025-10-26 02:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 5a16c947-1034-3f7d-8a47-850773ccccb8 | -4.9118 | -43.257 | 2025-10-26 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 70d46fd8-176f-3aee-96f5-99830e1ce038 | -10.5979 | -63.4743 | 2025-10-26 02:30:00 | GOES-19 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| dd32b70c-61c4-3465-8a4f-e6c32fb060b3 | -3.0909 | -49.4459 | 2025-10-26 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 3516325d-a824-3838-ad0f-deb79db32fc8 | -3.7661 | -47.5727 | 2025-10-26 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 26662a30-f164-3c4d-bbb2-c753d44935cd | -17.3158 | -43.6674 | 2025-10-26 02:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ccfe636f-d59b-3188-9685-835d70eb1a90 | -4.8933 | -43.2349 | 2025-10-26 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| b1cb348c-d8b9-3049-98ef-83b84bb113f2 | -4.912 | -43.2337 | 2025-10-26 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d77ed75b-d489-3df4-95ea-fc537d2c8144 | -6.7061 | -42.0517 | 2025-10-26 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 567f0b1a-0949-3032-a8d8-a78f5af27951 | -3.7661 | -47.5727 | 2025-10-26 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 171340b0-2dbe-317d-a4ca-40d6ef1467dc | -2.3178 | -48.5932 | 2025-10-26 02:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2a9d71ee-ad76-35fc-88e1-209b04235f37 | -17.3359 | -43.6628 | 2025-10-26 02:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7adefdcc-8af9-39a5-8ff4-dda66f824ebe | -17.3165 | -43.643 | 2025-10-26 02:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 194.8 |
| e949a95a-21d4-3f15-8cc4-efdc72333ab2 | -2.7755 | -45.0835 | 2025-10-26 02:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| da705fdd-d9db-38a7-894d-0034ab51b655 | -4.8931 | -43.2582 | 2025-10-26 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 6d56e542-2caa-3642-8b20-a23404815975 | -4.8933 | -43.2349 | 2025-10-26 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f5de50ce-1390-39c4-8bc6-568a54b4f93e | -17.3365 | -43.6383 | 2025-10-26 02:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 165.2 |
| a9d9ea19-01ce-34b5-8e35-779975718a8f | -2.3178 | -48.5717 | 2025-10-26 02:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 36340740-c630-3cb5-842e-154d345aa346 | -3.1093 | -49.4665 | 2025-10-26 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2a2fe771-021e-31c3-9ea1-67af3558a5b6 | -3.1094 | -49.4453 | 2025-10-26 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 96ac7768-733d-3865-905b-547ad54ebb09 | -2.7754 | -45.1061 | 2025-10-26 02:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 497900af-4e50-302d-b47e-36f0e0aeee1c | -4.9118 | -43.257 | 2025-10-26 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 06a1a569-e3e8-3844-b0b9-6972988f9eb9 | -6.7061 | -42.0517 | 2025-10-26 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| a44b60c1-2129-3ff4-af55-a50b7f6af263 | -13.5405 | -43.0077 | 2025-10-26 02:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 8c4464c4-ac3c-314d-a52d-d8b05deab8a2 | -17.3158 | -43.6674 | 2025-10-26 02:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e961279c-8e1a-3339-95a7-22e198015fc5 | -5.0996 | -43.1744 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 8acdd786-d276-3e03-9eaf-db9eb9ee35ae | -2.3178 | -48.5932 | 2025-10-26 02:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 08fad423-565b-3df9-9b87-c2e61d5d44d8 | -13.5405 | -43.0077 | 2025-10-26 02:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 110.2 |
| a6252258-457d-395b-87ee-76630b874c12 | -5.0992 | -43.2211 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7502ca6b-6a69-301c-84fd-b2520a42304c | -5.1183 | -43.1731 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 8aaba24f-25e0-3b3a-bdaf-1d70b3373502 | -2.7754 | -45.1061 | 2025-10-26 02:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 80a6fe6a-b7bb-3663-82d3-c9f42540f201 | -4.8931 | -43.2582 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c4152835-0879-3ac5-8d20-f80c8f8152c8 | -5.0994 | -43.1977 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 21b44c41-9c29-3acd-a194-1ffd1062bb90 | -6.7061 | -42.0517 | 2025-10-26 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 71f35a77-2dd0-3d26-a171-564ab5e5d5d6 | -5.118 | -43.2198 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 349ace57-4154-3593-ad10-2a128fa46271 | -2.3178 | -48.5717 | 2025-10-26 02:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 2b20f34e-197b-318a-ab2b-8f119ae18ae7 | -4.8933 | -43.2349 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3e035414-c945-3732-a54b-69f7c7e773f8 | -3.7661 | -47.5727 | 2025-10-26 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 6476bb80-50e7-32c7-859f-bd4a1008ab74 | -5.1181 | -43.1964 | 2025-10-26 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 5cb1342c-37cc-3111-863e-bff53c8aa7b4 | -2.7755 | -45.0835 | 2025-10-26 02:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 7cabf35d-c874-31dc-ba23-50266d897d20 | -17.3365 | -43.6383 | 2025-10-26 03:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 2109d1c9-a0bc-3f94-9812-240c6a6e4c20 | -6.7061 | -42.0517 | 2025-10-26 03:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 4dd18ba9-755f-3373-8356-5c47361544bd | -4.8933 | -43.2349 | 2025-10-26 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5061c2a5-9d0b-3392-b926-a9144d45a49d | -17.3158 | -43.6674 | 2025-10-26 03:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 04fa8d3a-764b-3e0e-b14c-33db10c797d1 | -5.0994 | -43.1977 | 2025-10-26 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 202.4 |
| f41caeac-2186-3fe5-bc3c-c3b2f39a5ca7 | -17.3359 | -43.6628 | 2025-10-26 03:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 52ef97ba-4165-3d58-93ce-9eca68783ed5 | -5.118 | -43.2198 | 2025-10-26 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 264f4a5a-37e7-39e2-ad57-547b108e1ac8 | -13.5405 | -43.0077 | 2025-10-26 03:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 116.7 |
| d326e9c4-82c1-38bd-a9ab-c92485cb24b2 | -5.1181 | -43.1964 | 2025-10-26 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 241.1 |
| eb1e0120-faf5-3169-8a4c-c1c3847c9abb | -2.3178 | -48.5932 | 2025-10-26 03:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |


[Clique aqui para ver as próximas entradas](README6.md)
