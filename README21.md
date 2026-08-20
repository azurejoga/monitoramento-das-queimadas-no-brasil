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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f2767b7-035b-331b-872d-fc0667d72a33 | -7.3603 | -45.8136 | 2026-08-20 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 405fbb2e-a317-3467-975a-3129e9e303fd | -9.2258 | -59.77 | 2026-08-20 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4f1b1cac-6632-38be-b54d-86354c0c5e71 | -7.36 | -45.8361 | 2026-08-20 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| dcd6ee00-3414-3eff-a4db-a1efeab5eff6 | -11.8377 | -58.8445 | 2026-08-20 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c518d591-b29c-3540-8146-03d70cef3601 | -6.6938 | -58.942 | 2026-08-20 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3a49bfbf-88c8-3c3a-ac58-4edac46e6a45 | -9.4256 | -60.4353 | 2026-08-20 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| b1baebb7-fcf7-3bb4-8016-6372a49f4985 | -7.9751 | -44.6648 | 2026-08-20 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| fe153e63-8ace-3ebd-8eec-e6cde99690d8 | -17.3372 | -43.6139 | 2026-08-20 02:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 5dc26b95-8caa-3467-b6a5-32bbf1f35643 | -9.2071 | -59.771 | 2026-08-20 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| bcefb691-9e64-3714-bb50-3f8dd4d7b9e8 | -7.36 | -45.8361 | 2026-08-20 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6bf35e81-1fa6-3780-b47f-df386b112547 | -11.8377 | -58.8445 | 2026-08-20 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 57a6703c-8257-3846-a410-14a3e1c0a5b2 | -6.6938 | -58.942 | 2026-08-20 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f8cc54c8-016d-3281-901b-61039c0e268c | -18.0285 | -44.6113 | 2026-08-20 03:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7e484c58-bb08-3506-b146-3f0f1714ab15 | -9.4257 | -60.416 | 2026-08-20 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 39bb2217-068a-31d4-bc9a-aa40893d7d1f | -7.3413 | -45.8377 | 2026-08-20 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 2fbd88bc-ee93-3d33-b0b5-691aa0cac053 | -14.3339 | -51.9157 | 2026-08-20 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 5500a4db-bcab-38fd-b77f-d6f6428e9932 | -9.12 | -61.6011 | 2026-08-20 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6816d5a4-119e-3251-be30-527ae34959ee | -14.3146 | -51.9183 | 2026-08-20 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 208e2d95-8d58-37fd-a8c4-c13c561d2438 | -11.2189 | -55.0585 | 2026-08-20 03:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e4219f33-a5ea-39c9-ae0e-a3876ca740a0 | -11.2 | -55.0601 | 2026-08-20 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| cf1a5fb5-61a0-3b5d-82ea-62cf091adb77 | -8.654 | -54.6505 | 2026-08-20 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e26177be-4672-3469-9dff-a3bb20d00745 | -15.3636 | -52.7767 | 2026-08-20 03:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 373b0c64-3bca-32cf-99a8-f5c23c422532 | -9.4256 | -60.4353 | 2026-08-20 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7a3c1ca9-bc77-34d9-a91a-cc436dcbc039 | -11.1936 | -54.0199 | 2026-08-20 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f4438be9-6ad4-3710-a934-dee5dbe5e9c5 | -17.3365 | -43.6383 | 2026-08-20 03:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ebefb893-6c7b-3036-9f4f-5880d45e786b | -8.6727 | -54.6492 | 2026-08-20 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 15937f18-8965-301a-a168-51783c5d0abb | -7.3603 | -45.8136 | 2026-08-20 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 07512326-d9fa-3489-92ed-0e562ad9cef1 | -17.3372 | -43.6139 | 2026-08-20 03:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 168.9 |
| d637d044-3831-3dfd-923b-58ec1c4eb35e | -7.3415 | -45.8152 | 2026-08-20 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 739a726e-25ce-3a1c-b547-1c033edf20fc | -9.2258 | -59.77 | 2026-08-20 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 24ddbb26-fb71-392f-b14e-4c2d4006bbd1 | -9.2071 | -59.771 | 2026-08-20 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 1c155463-3ca5-3aad-9261-951506306a25 | -8.654 | -54.6505 | 2026-08-20 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0728c285-d9d6-38f7-b6b9-8c3481710a82 | -8.6727 | -54.6492 | 2026-08-20 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 110b7b4f-4201-3359-aa76-b979c1b63b12 | -17.3372 | -43.6139 | 2026-08-20 03:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 7e9d0619-2175-3a0b-af2b-bd2011a86f58 | -11.2189 | -55.0585 | 2026-08-20 03:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a69e021e-7330-3126-bba7-9d0a2a6b89c2 | -15.3636 | -52.7767 | 2026-08-20 03:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 0082c65e-7c9b-3f40-b45e-21ea9d777ca8 | -11.2 | -55.0601 | 2026-08-20 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 44f1d944-1b9a-3eb9-9c68-4daa777f2700 | -6.6938 | -58.942 | 2026-08-20 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3c5fdd22-78be-351e-8af2-bf087d216f0c | -17.3365 | -43.6383 | 2026-08-20 03:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 71cd686f-7678-33db-8d6a-8c429460b549 | -7.3413 | -45.8377 | 2026-08-20 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 217f7677-d81f-3056-adb8-a7d0f0ef22e9 | -18.0487 | -44.6066 | 2026-08-20 03:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0c79dc53-fe22-34e9-8244-923d165b8652 | -10.3897 | -61.2118 | 2026-08-20 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9c6a4cdd-d6ec-3756-81a9-d456c63b8a3f | -7.3415 | -45.8152 | 2026-08-20 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ae2f1d93-6aa1-3421-ab7d-5c2ae08be7f9 | -9.4257 | -60.416 | 2026-08-20 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| eabbf42f-b8d1-3ba2-b54d-c0985ed7f32d | -7.3603 | -45.8136 | 2026-08-20 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 60584029-2fa0-3b41-bd93-667533451f84 | -11.1936 | -54.0199 | 2026-08-20 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c9fd38f3-f616-36ad-ac37-4b7f48b7b98c | -18.0285 | -44.6113 | 2026-08-20 03:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9ea09f76-6d3c-3aa0-943c-66b4d9183ac0 | -7.36 | -45.8361 | 2026-08-20 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 72c990b3-2ed4-3368-ba4b-6812e8523e04 | -9.4256 | -60.4353 | 2026-08-20 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 85b3afe0-82a9-35fa-97cf-5e63343f552d | -7.6118 | -45.1571 | 2026-08-20 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 74a808d2-417b-39cf-b20c-c8220e7cd4e6 | -9.12 | -61.6011 | 2026-08-20 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ff559df3-a19d-36e7-bc3c-9ecc8f59b173 | -15.3636 | -52.7767 | 2026-08-20 03:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6e9359b3-6526-3ba6-b47f-e014c0e04ab0 | -7.6115 | -45.1799 | 2026-08-20 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ba8ad678-b3e5-319d-ae81-f6a711eb7d76 | -7.9751 | -44.6648 | 2026-08-20 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 50f37f96-7931-34ea-b2de-a28182e4164f | -9.4257 | -60.416 | 2026-08-20 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8585ae27-3d7d-3bb2-b2b8-879b4b751f2d | -7.36 | -45.8361 | 2026-08-20 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 481fb088-4d39-3c37-89d0-f307b00d95e6 | -9.2258 | -59.77 | 2026-08-20 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| baacc8a0-6977-33b5-9226-4f2e01ed67ea | -17.3372 | -43.6139 | 2026-08-20 03:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 3f0a3917-7843-3856-9235-3a735563cacf | -9.4256 | -60.4353 | 2026-08-20 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d6d8ba55-1feb-3863-b6c1-c9cc4cc16a75 | -18.0487 | -44.6066 | 2026-08-20 03:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 808f4b96-2aea-368d-b1fb-09d3924ec8af | -11.2189 | -55.0585 | 2026-08-20 03:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d4dcced0-751e-31c4-8247-c525b6178459 | -17.3172 | -43.6186 | 2026-08-20 03:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 7e03e297-75eb-3577-81a9-67845d0fd988 | -17.3365 | -43.6383 | 2026-08-20 03:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 5d2adf6d-50d2-3c5b-9c71-f4f4e6ef2de5 | -7.3603 | -45.8136 | 2026-08-20 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 79b2108f-43b8-3a56-8337-c62718228051 | -8.6727 | -54.6492 | 2026-08-20 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 16db3a0a-b571-3051-81e6-6396637ba411 | -7.3413 | -45.8377 | 2026-08-20 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 09da5d3a-8d19-3c06-90dc-4cc1f033dded | -7.3415 | -45.8152 | 2026-08-20 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a675e9f9-807b-319c-a63c-999f4785ee27 | -11.2191 | -55.0382 | 2026-08-20 03:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| cd4e4495-6a69-38f8-aed6-e0afd22e9afe | -11.8377 | -58.8445 | 2026-08-20 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2b92b9be-142a-3619-b2d8-34b1478372ac | -18.0285 | -44.6113 | 2026-08-20 03:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9037a1a4-6b76-3beb-85b1-c8e5ce7833aa | -4.05612 | -38.2888 | 2026-08-20 03:21:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3570d26c-abf9-3348-82f4-c78855ce95b1 | -4.05622 | -38.29182 | 2026-08-20 03:21:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| b3f9029e-a8aa-33bb-a5b2-dfe6c61670a6 | -4.05563 | -38.29169 | 2026-08-20 03:21:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 5bb80e9f-bf3d-3b36-b3cf-1531adc10d1c | -4.0567 | -38.28893 | 2026-08-20 03:21:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ffdf2988-c361-3af6-801d-b0ecd8023e18 | -6.17289 | -39.38514 | 2026-08-20 03:23:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c6d6952d-aa82-3614-9d49-9d074f266586 | -7.96607 | -44.66142 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 40b88911-a702-39a9-8eb2-c9fcae912ece | -3.97464 | -43.11131 | 2026-08-20 03:23:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b5e2f34-7d7b-3111-857b-afdf57c26d2f | -3.56141 | -43.20379 | 2026-08-20 03:23:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a429d50e-88d1-35ba-a6c8-39cc28cdb7bc | -3.5617 | -43.2005 | 2026-08-20 03:23:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c23151c0-f38f-34f7-9c57-f7ace338279a | -5.42481 | -43.43928 | 2026-08-20 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9cd412f-faad-3352-bdd7-00fdb22ab9b2 | -6.42871 | -43.07213 | 2026-08-20 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56ac0607-7740-3a02-889f-268e11d94961 | -6.29175 | -43.64023 | 2026-08-20 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a64122a-71b9-373f-b5c7-7f3f8b331788 | -6.2906 | -43.64643 | 2026-08-20 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e325959d-052a-369a-bbef-efcb775ad963 | -6.33734 | -44.08656 | 2026-08-20 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b5a8565d-d52d-3327-9fe2-a6ef058036a1 | -7.96238 | -44.66791 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a63f136d-38a2-35aa-9f9b-b0d87aa0a415 | -8.80868 | -44.21444 | 2026-08-20 03:23:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0406867-c24b-33e5-927d-cdd9242395a6 | -3.96174 | -43.11033 | 2026-08-20 03:23:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b7e8591f-033b-327e-a399-4763883120af | -7.97438 | -44.65598 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1620c1f7-2660-3cd1-9e66-6a02b997ef80 | -5.42595 | -43.43308 | 2026-08-20 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 895e6916-0543-38ba-862a-a063a87ef536 | -3.56056 | -43.20699 | 2026-08-20 03:23:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 35c242ec-7da3-3821-b46b-7581188ef8dd | -6.78534 | -42.88809 | 2026-08-20 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7e4ac339-3c6a-315b-ad1b-ae64f7193262 | -5.84039 | -42.63412 | 2026-08-20 03:23:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c0614b89-21fa-3280-a662-ba28d56cac8a | -5.74115 | -43.2747 | 2026-08-20 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c465ce29-0193-3719-8496-aaeb4347451c | -7.96364 | -44.6615 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b8043f63-d90d-37de-8b64-df6c37f0f6b2 | -3.96857 | -43.1115 | 2026-08-20 03:23:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6063b370-1a2c-3e19-b0e4-95b98a4ee007 | -3.96673 | -43.11632 | 2026-08-20 03:23:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e98779a2-282d-35ea-a5e1-6db18a3935ef | -6.34554 | -44.08123 | 2026-08-20 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a418ceb6-1f33-30ba-beec-97db81c3d684 | -10.45535 | -37.14283 | 2026-08-20 03:23:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 70d50f74-74f1-310d-bc26-362eaa859927 | -6.26546 | -43.27719 | 2026-08-20 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c9fee38c-c279-3b7d-a037-2dada4843e84 | -7.96108 | -44.67451 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README22.md)
