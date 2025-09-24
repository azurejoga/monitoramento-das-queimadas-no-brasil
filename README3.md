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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d40643f-31b2-3906-b477-c24153d5ff24 | -6.4319 | -43.0707 | 2025-09-24 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9595beb4-9464-38e4-a227-cb53d3cd6ee1 | -6.4317 | -43.0942 | 2025-09-24 01:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| ba984b77-50f6-3cca-956e-f67d8c0caa90 | -6.4129 | -43.0958 | 2025-09-24 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 93f436e5-7d94-3964-857c-96975764698a | -6.4131 | -43.0724 | 2025-09-24 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 06a9fa7f-3c48-3846-b29e-ecfa03dbf942 | -5.6207 | -45.7252 | 2025-09-24 01:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 77ce3516-6a67-3004-ab6c-03c6be3f4c16 | -14.3067 | -41.8364 | 2025-09-24 01:30:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 158.2 |
| ebc2f751-ccf0-37fc-8bf3-3b8357ea0444 | -14.2871 | -41.8405 | 2025-09-24 01:30:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 153.5 |
| 85e5856d-163d-3b7c-8970-49f08099941f | -5.6361 | -43.9258 | 2025-09-24 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c68cd702-cbf6-3c7d-bcc4-5f837cb2c700 | -4.3197 | -48.0908 | 2025-09-24 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f08e087a-7529-3d5d-9654-b50aaf0b8bfb | -9.76156 | -64.99265 | 2025-09-24 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 864d5894-44c9-3191-bd95-e2e1bca568c4 | -9.14078 | -65.3131 | 2025-09-24 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 36b37240-b40f-36ca-b5db-0fb3e0ed7a2e | -7.96351 | -63.55621 | 2025-09-24 01:32:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2b89996d-1b2a-3c3e-a5e1-5fafd363995e | -9.76286 | -65.00249 | 2025-09-24 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 39705cee-2301-355c-ac01-f891f2929891 | -10.62717 | -64.99094 | 2025-09-24 01:32:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc7df5ed-6714-3d93-9379-7f578da83543 | -9.81866 | -67.02888 | 2025-09-24 01:32:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11855edb-e39d-3933-9162-784f26180737 | -9.13947 | -65.30307 | 2025-09-24 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e966f73c-59ea-3127-9f31-1d235896817c | -9.68178 | -63.17025 | 2025-09-24 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3266a59d-46f0-388f-87b3-e8586ad6b947 | -9.54274 | -63.58089 | 2025-09-24 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 0686aab4-0508-3c75-b3ec-63f7651f8797 | -9.88946 | -64.83954 | 2025-09-24 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7f46e7b2-894d-39f5-940d-0e7603ad770c | -9.00168 | -63.66729 | 2025-09-24 01:32:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfaa7854-c1c2-3dc4-883c-e87f0296864a | -9.96242 | -66.77088 | 2025-09-24 01:32:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dff4b073-3ff7-3ca3-9b80-10f9cd27033e | -9.5339 | -63.58215 | 2025-09-24 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a9327f4e-9801-3ea4-9f70-4c2a1d59c5b2 | -7.6145 | -67.24024 | 2025-09-24 01:32:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c9a2e34f-b74a-3b31-9e7e-a3e9a1deac80 | -9.13389 | -65.30966 | 2025-09-24 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cff3f4c9-399e-34e6-9071-f84a36af23c5 | -14.3067 | -41.8364 | 2025-09-24 01:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 6a093c85-4f00-33f3-9a9f-5b7055b740c0 | -6.4131 | -43.0724 | 2025-09-24 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 87d3a974-562b-3ae9-a365-7e0969d3ec1a | -14.2871 | -41.8405 | 2025-09-24 01:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 180a2d71-6815-3074-8605-8b20b80e14bd | -4.3197 | -48.0908 | 2025-09-24 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1eb14c13-32d6-30be-8e34-c59cd49b21bc | -6.4129 | -43.0958 | 2025-09-24 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| c58442a0-a0ac-3db3-9506-e9aaa8c66c13 | -6.4319 | -43.0707 | 2025-09-24 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3f475067-fa1b-3460-9b5a-e1b92314b79b | -5.6361 | -43.9258 | 2025-09-24 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 47243b96-8796-3788-95cd-5ff8d35c952b | -5.6363 | -43.9027 | 2025-09-24 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| b6121df9-cc00-37b5-8b46-23895b5d279e | -5.6393 | -45.7239 | 2025-09-24 01:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e7020f0d-e34f-33b2-9605-6285e554cc94 | -5.6207 | -45.7252 | 2025-09-24 01:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 607a8c19-3103-36e0-9cca-651b79370bd1 | -5.6392 | -45.7463 | 2025-09-24 01:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| e4121de5-2c16-3f37-a01c-62db120d63a1 | -6.4317 | -43.0942 | 2025-09-24 01:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 5c062528-12fd-38c9-9618-dcc445c886e9 | -6.4317 | -43.0942 | 2025-09-24 01:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a75ed58c-1363-3be0-9001-a4ad88932b24 | -6.4131 | -43.0724 | 2025-09-24 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| e67a6dde-d93d-3ead-ba93-72ab950d9ace | -5.6207 | -45.7252 | 2025-09-24 01:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 40ea7cea-4640-398d-92d1-884d2167a183 | -5.6392 | -45.7463 | 2025-09-24 01:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ef01b29e-3578-396a-b816-a3681fc37feb | -14.3067 | -41.8364 | 2025-09-24 01:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 8de115e8-bf52-343a-a36e-3dfab9f6d018 | -6.4129 | -43.0958 | 2025-09-24 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| cf899b28-f930-36fe-aed9-56963540f0eb | -5.6361 | -43.9258 | 2025-09-24 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 66800123-5233-37d1-b5ca-e16800fc21e1 | -14.2871 | -41.8405 | 2025-09-24 01:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 96.1 |
| bde37a03-fe4b-3f3d-a27b-9d1594045c84 | -5.6363 | -43.9027 | 2025-09-24 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 401abe8e-a438-3199-860d-9ce5f615ce72 | -4.3197 | -48.0908 | 2025-09-24 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| fbd6b9a5-f15a-38ac-8490-d55fdf7e0eae | -5.6393 | -45.7239 | 2025-09-24 01:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 89f572f4-9d09-3306-9e8f-0f1a38b19aea | -5.6361 | -43.9258 | 2025-09-24 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 259c2484-cf6c-37f1-82ce-3a84a7c4774c | -5.6363 | -43.9027 | 2025-09-24 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 048d7882-0b7f-3d06-b14a-6e2741a6b0f9 | -5.3882 | -42.2826 | 2025-09-24 02:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| e270cd6a-7653-36ce-9a1c-4808f97ea98f | -4.3197 | -48.0908 | 2025-09-24 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| fadfaad7-c830-34fe-ac95-4bad872a0629 | -6.4131 | -43.0724 | 2025-09-24 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f7812924-8c8f-3399-9abe-dc3a28b88e88 | -14.3067 | -41.8364 | 2025-09-24 02:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 100.4 |
| c55a47c1-10cd-3f85-99bd-34f13f365a8d | -6.4319 | -43.0707 | 2025-09-24 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 943b553a-38d2-33b5-a849-2ef005035609 | -5.6207 | -45.7252 | 2025-09-24 02:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d7c1e4f9-4e57-317a-8bbd-90e6416be0f8 | -6.4317 | -43.0942 | 2025-09-24 02:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b335770f-f3c0-379a-acb0-a9f5a877de3d | -5.3884 | -42.2588 | 2025-09-24 02:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 7ec70356-283f-3926-8e2f-6c87bd28034b | -5.6393 | -45.7239 | 2025-09-24 02:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 700c9723-8217-324a-b5ff-b63d26eeefac | -4.3012 | -48.0917 | 2025-09-24 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a4ca8bc8-c4da-3351-92d6-f11f6138d55b | -6.4129 | -43.0958 | 2025-09-24 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| eb6c8dbf-38d1-386b-b425-bbf97fcf1694 | -4.3197 | -48.0908 | 2025-09-24 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 74eba821-56b6-340d-99b1-e20a7bd80136 | -5.6393 | -45.7239 | 2025-09-24 02:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 53aadd09-ad6c-3f15-b3b1-53a43bdd2a15 | -7.3659 | -47.0394 | 2025-09-24 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 1bd0811a-e913-3abf-ad44-072d052b217a | -4.3012 | -48.0917 | 2025-09-24 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 416e100d-b442-3cf1-91a2-c14eb24addaf | -6.4131 | -43.0724 | 2025-09-24 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| d4ec71f6-3a8d-3b49-814f-3169ea3a7c7a | -6.4129 | -43.0958 | 2025-09-24 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e2a4e145-8e73-3066-99e0-1e25e5825ede | -14.3067 | -41.8364 | 2025-09-24 02:10:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 74a163d5-abbd-3a77-bf47-de6416990fe9 | -5.6361 | -43.9258 | 2025-09-24 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4abbd067-cdaf-350a-8df1-4ed8bf4cb49d | -6.4317 | -43.0942 | 2025-09-24 02:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| af92da9a-a896-3b34-97a4-2c003a0364c8 | -5.6363 | -43.9027 | 2025-09-24 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0754c6e6-ec38-36cf-84ef-1160b5d373dd | -7.7689 | -46.2031 | 2025-09-24 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c8f74192-0890-3328-b8fb-00f7244735ae | -7.7877 | -46.2013 | 2025-09-24 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 6490cc7d-0c84-3fdf-8aa4-2a0797b0c2a2 | -5.2448 | -43.7225 | 2025-09-24 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3dceff35-5bee-3139-8390-d1c2135d9d51 | -6.4129 | -43.0958 | 2025-09-24 02:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| d3685d19-b91d-392b-adc4-062f780cf681 | -7.7877 | -46.2013 | 2025-09-24 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ec47a0f8-9127-3402-a532-5bb9639ee334 | -4.3197 | -48.0908 | 2025-09-24 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c345f2b6-4979-3c77-a5c9-97d1fffaaede | -22.6084 | -49.0117 | 2025-09-24 02:20:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d9b9af8b-e0d1-3eb5-95cb-3098e9cce7b0 | -5.6363 | -43.9027 | 2025-09-24 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 63531898-44f5-3689-9a7f-55b975cd1ed9 | -6.4317 | -43.0942 | 2025-09-24 02:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 5c4b9b88-b87d-3f74-81e5-a87084fc05a0 | -7.7689 | -46.2031 | 2025-09-24 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1c99750a-16d1-3be5-baea-e2dda839a22d | -5.6361 | -43.9258 | 2025-09-24 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 25616067-b55f-318c-a79b-f84946841645 | -14.3067 | -41.8364 | 2025-09-24 02:20:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 589357c8-2fd8-3243-bd5c-b3d8f6e0dd7b | -4.3012 | -48.0917 | 2025-09-24 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 993386a7-b0d1-335b-b872-b9016ad30461 | -5.6393 | -45.7239 | 2025-09-24 02:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| fbb3e8a9-e5ba-3dcc-b950-253a7f0927d7 | -22.6084 | -49.0117 | 2025-09-24 02:30:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 34c8d334-d86d-30d8-b3d9-fd21b6e70e82 | -14.3067 | -41.8364 | 2025-09-24 02:30:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 9224da37-7da4-3460-ba9b-ed1d3ae8e816 | -6.4317 | -43.0942 | 2025-09-24 02:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 567fc654-7093-3af8-b6cf-fbf0a3c97d6e | -6.4129 | -43.0958 | 2025-09-24 02:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 4a429ead-07de-3b7d-947f-5b336afa4826 | -4.3197 | -48.0908 | 2025-09-24 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 314d7467-795f-38c8-a5c5-b3a880bf9118 | -4.3012 | -48.0917 | 2025-09-24 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e391a63b-d020-3b7b-b49d-23b4fd12d8a7 | -4.3012 | -48.0917 | 2025-09-24 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8b7f668f-48eb-35e5-923b-df27c7b09ba6 | -15.7835 | -59.4853 | 2025-09-24 02:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 85c3ec5c-261c-396d-b83c-126011197252 | -5.7607 | -42.5852 | 2025-09-24 02:40:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| dd6f9e75-3627-3b62-a1f6-f0116fc52713 | -5.6361 | -43.9258 | 2025-09-24 02:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| d6da7117-1cd8-3647-a8d7-e5262cbda9b3 | -5.6363 | -43.9027 | 2025-09-24 02:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5d47c6a5-f0a2-322b-a400-5f6e3df5f335 | -22.6084 | -49.0117 | 2025-09-24 02:40:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6c6f20c3-45ce-3db8-8e82-ce85d6efd447 | -14.3067 | -41.8364 | 2025-09-24 02:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 00a88a25-3562-3dbd-aff5-2d108bbe28c2 | -5.761 | -42.5616 | 2025-09-24 02:40:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 1ad4a31d-dde4-3cb9-ab62-b199f44a42c3 | -5.2448 | -43.7225 | 2025-09-24 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7734ea82-d5af-360d-90ae-2e8732ff6e8f | -5.7605 | -42.6088 | 2025-09-24 02:40:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |


[Clique aqui para ver as próximas entradas](README4.md)
