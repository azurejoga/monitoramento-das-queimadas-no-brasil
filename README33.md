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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 895d88eb-6bf3-38e5-b165-09d65d6e96c0 | -12.9167 | -62.7022 | 2024-10-03 01:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| c4f70b70-bf76-35ce-b25f-5a60e1d5016a | -12.9187 | -62.4708 | 2024-10-03 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 074bb98a-391c-3486-8caf-b81eab6532cb | -12.9741 | -62.6409 | 2024-10-03 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 1c2c2b18-fead-3942-af06-5bacb0bc0ce9 | -4.566 | -48.007 | 2024-10-03 01:06:20 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef72de7-73a0-32d4-a479-80b3a14d91fd | -4.5686 | -48.017899 | 2024-10-03 01:06:20 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87d9379-fcc7-3896-a0b5-5e2c4a62a134 | -3.5031 | -54.025501 | 2024-10-03 01:06:21 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd1b5877-a1f4-3c74-9276-62eb5b72c8e4 | -3.5047 | -54.032299 | 2024-10-03 01:06:21 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ecccff3-88f6-3628-ba15-29b65b4f7735 | -3.4611 | -53.9772 | 2024-10-03 01:06:21 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1bd25b-d2fe-36f0-b615-b099de7f2e1a | -3.4627 | -53.9841 | 2024-10-03 01:06:21 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89529b7c-d43f-364f-9a0d-5b09916fff7a | -3.4513 | -53.979401 | 2024-10-03 01:06:21 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a884ecb-b051-3c48-ad4c-06716ea78b1c | -3.4529 | -53.986301 | 2024-10-03 01:06:21 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83e466c6-5de9-3deb-99f8-1469602d9ccb | -2.8799 | -51.675999 | 2024-10-03 01:06:22 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a12676-be52-32e5-be02-fbb0551f67ca | -2.8045 | -51.394798 | 2024-10-03 01:06:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a03ab25b-c9e9-3e85-b2ba-92f3ed46aaeb | -3.3279 | -53.755501 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5e2027-6b37-3f18-9bcf-f7ba78fc6e9f | -3.3295 | -53.762402 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeed5722-810d-3ec2-951a-bf406ed8def9 | -3.3311 | -53.769199 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93919fe5-c7c2-36d1-90ea-c5e5122ee15b | -3.3181 | -53.757702 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc6ed37-9fbe-37ea-ae4e-b797a2bd2ebe | -3.3197 | -53.764599 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78994ec5-45b9-3966-bd01-3bf0f8a95298 | -3.3213 | -53.7714 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 460d6216-5466-331e-ae1f-45de9e756b30 | -3.2942 | -53.698502 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93c07875-335e-394e-97d7-51500b11823f | -3.3752 | -54.097301 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20243cd0-4639-3611-85dd-8485fa76766f | -3.3768 | -54.104198 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d688e81d-654a-35e2-9235-3744455b3ec5 | -3.3784 | -54.111 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec08ce0b-ef13-3e48-aff6-151109adf437 | -3.3799 | -54.117901 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4a84fef-3b5d-38f3-ad07-6f379722ebcb | -3.367 | -54.1064 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cbf92fb-fc0f-36cb-a5a6-6a92058b55c6 | -3.3686 | -54.113201 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57efdfe0-77ae-368c-ae8c-33a4f2ea91c4 | -3.3701 | -54.120098 | 2024-10-03 01:06:23 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c391c6-99c9-36ee-b7ba-0dcc47e3ebfb | -4.1436 | -48.3974 | 2024-10-03 01:06:29 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e1816a-a423-38ad-b300-58abd5d50cc6 | -3.6969 | -47.598701 | 2024-10-03 01:06:33 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3080b3-5b35-39ba-b946-a23f537197e1 | -3.6997 | -47.6106 | 2024-10-03 01:06:33 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0537a9c6-1a31-3137-8cbf-44e278c290c6 | -4.3272 | -50.493599 | 2024-10-03 01:06:34 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab40266-90a0-3f2e-bfdc-6e81f631f29c | -3.4657 | -47.665199 | 2024-10-03 01:06:37 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d878a2a-8a6f-3655-9e21-233d52d021f3 | -16.779 | -57.8306 | 2024-10-03 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| a4c8b9bd-5471-3f66-9888-ba601efe05e5 | -16.7793 | -57.8102 | 2024-10-03 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 1c1a477d-f4fa-397a-a65e-89b2213da8bd | -16.7985 | -57.8284 | 2024-10-03 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| c3d9296e-9dbf-3c99-9106-41507475e3c2 | -3.95 | -50.998901 | 2024-10-03 01:06:42 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2447a3b1-7544-3aa7-bcca-e62a47802bc9 | -3.9517 | -51.0065 | 2024-10-03 01:06:42 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c8de97-8986-3a1a-9d4a-cbaea36667b2 | -3.2269 | -48.920898 | 2024-10-03 01:06:45 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca487b5a-d23c-31d9-a36e-8d71ff78e266 | -3.2292 | -48.930901 | 2024-10-03 01:06:45 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1889e53c-e4de-3c0c-8de7-13471059a95a | -3.2171 | -48.9231 | 2024-10-03 01:06:46 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c7e1be-0b1d-39ed-9a09-297d0078d374 | -3.2195 | -48.933102 | 2024-10-03 01:06:46 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49f67b88-c4da-3942-88e9-6e7aefdcaf34 | -3.1138 | -49.4044 | 2024-10-03 01:06:49 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e02e836f-da73-3aa7-a41f-d56363285bbb | -3.2434 | -50.134899 | 2024-10-03 01:06:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 161a17cc-22b4-3c2c-ad5c-c51973af9c30 | -3.2454 | -50.143501 | 2024-10-03 01:06:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1f70bff-fedc-317a-ac73-d7657ffddf25 | -2.5385 | -47.2229 | 2024-10-03 01:06:50 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5301e43f-94d4-3ff0-867a-bd770e308719 | -2.5288 | -47.225201 | 2024-10-03 01:06:50 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a8f8c9-ad36-37a8-9443-bbc1a530ca4c | -19.0344 | -43.1944 | 2024-10-03 01:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.5 |
| e0e030c1-65a9-352d-b1cf-6d8b533461ae | -1.7538 | -54.444401 | 2024-10-03 01:06:51 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3268ef82-2ddf-3080-ab68-18f938732d5d | -1.7554 | -54.451302 | 2024-10-03 01:06:51 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e5737c-ecb2-3892-82a8-9610421bde7e | -19.2801 | -43.7703 | 2024-10-03 01:06:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 37fd0b81-6c3a-3b5f-9e2e-c4448096f6a5 | -1.1337 | -53.629601 | 2024-10-03 01:06:58 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbe89b9a-9c96-3d2c-ace3-1cce197e4917 | -1.1353 | -53.636501 | 2024-10-03 01:06:58 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9abc51-b106-3cd5-ac7c-4cd19ce19bed | -1.1368 | -53.643299 | 2024-10-03 01:06:58 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92bfe16-34fd-34e0-9dd3-7f4be3cba1f3 | -1.0451 | -53.512798 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c299b9b-f9b6-3048-9186-ced67b50a182 | -1.0466 | -53.519699 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c18c0a1-30fd-3cfe-948b-47bcf6abbf8b | -1.0482 | -53.526501 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c77c65f-9b55-322f-8488-f3ac32b27f31 | -1.0498 | -53.533298 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8d9b003-2c53-32b7-8a0d-16a6a4cfb6e7 | -1.0337 | -53.508202 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08c64f95-59cc-32ea-b146-c808b8636671 | -1.0353 | -53.514999 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 208f80c8-e182-31f9-984e-ce0e998ad6f3 | -1.0368 | -53.5219 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f487fffc-6905-3dc3-8119-8a0b4cea28ef | -1.0384 | -53.528702 | 2024-10-03 01:06:59 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bddc6e82-9250-3d1b-8f45-74ebf4c51e66 | -21.346 | -55.6626 | 2024-10-03 01:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 119.1 |
| e5f08ae6-289a-302a-8f8c-6dad5b1767aa | -21.8813 | -48.3725 | 2024-10-03 01:07:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 0fc24a2d-8e4a-33eb-8c82-8867e7d86828 | -21.9014 | -48.391 | 2024-10-03 01:07:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c4ece3d5-bb32-313c-a5f7-734c88da8d3a | -21.9021 | -48.3674 | 2024-10-03 01:07:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 7bcc1958-ad29-31ce-9bc9-da2508b69f04 | -21.9028 | -48.3439 | 2024-10-03 01:07:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 468d52cf-9067-3c5a-974b-44a963bcc865 | -21.9215 | -48.4094 | 2024-10-03 01:07:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 69.3 |
| bd5f0fe5-0cbf-39f1-a3e4-84fa20738e03 | -22.2307 | -48.4507 | 2024-10-03 01:07:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a6225ed7-689a-307e-9cf9-7d4b1b80ff5e | -22.2508 | -48.4691 | 2024-10-03 01:07:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 157d8715-c285-35c2-9e85-ef5ae68ab683 | -22.2515 | -48.4456 | 2024-10-03 01:07:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 8f37cf83-3fc2-3459-b270-a84f8822772c | -22.3495 | -47.9515 | 2024-10-03 01:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 093cb50f-3549-325a-bf6b-3ad4a97709cc | -22.3502 | -47.9278 | 2024-10-03 01:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 98a21bfc-d913-3639-aba0-848ac6277166 | -22.3704 | -47.9462 | 2024-10-03 01:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 263ae1f4-62aa-30f1-94e2-e0cb1705cece | -22.3711 | -47.9225 | 2024-10-03 01:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 930a90de-e95b-3304-aee2-1804205a56cd | -22.3719 | -47.8987 | 2024-10-03 01:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2368ee67-8b7d-3693-acdf-072dd54cd4f3 | -2.9549 | -54.6483 | 2024-10-03 01:07:11 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df9d6129-2b42-3df4-aec9-3969e187dd74 | -2.9565 | -54.655201 | 2024-10-03 01:07:11 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0d544a5-f784-3ee0-a6bd-8607a54a39b3 | -2.958 | -54.662201 | 2024-10-03 01:07:11 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34259519-6b85-314a-849e-5f103c416cd5 | -2.4123 | -53.809601 | 2024-10-03 01:07:17 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c12422-4d33-3a24-b126-8006bdaaaca8 | -2.1383 | -53.6488 | 2024-10-03 01:07:21 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20b2b36e-0d7f-3e8b-bf71-0812407d110c | -2.1398 | -53.655602 | 2024-10-03 01:07:21 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7589673a-6c02-36bb-b7e7-362c3698c0c8 | -3.3854 | -42.2866 | 2024-10-03 01:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9cc50ad2-1bc6-36ae-845d-339d06628051 | -3.3855 | -42.263 | 2024-10-03 01:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| fbb29177-fee8-3508-9356-14bb57dc94d8 | -3.404 | -42.2858 | 2024-10-03 01:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c91608e4-30a2-34d4-a1d0-619e8a6ba032 | -3.4042 | -42.2621 | 2024-10-03 01:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ea06ef7e-4e6c-3047-b24c-de9a97fa2c6c | -3.4229 | -42.2612 | 2024-10-03 01:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 1fe7494f-e885-3ce7-becb-9c2406bc3db3 | -4.0949 | -48.4894 | 2024-10-03 01:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 29262cdd-ab22-34b6-8f2c-c4653be611c5 | -4.095 | -48.4679 | 2024-10-03 01:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d9c4eaa6-3545-3c43-a2dd-b85cfed75a40 | -4.1134 | -48.4886 | 2024-10-03 01:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 576c0ede-b050-3b1d-bd50-aa01ab727b1f | -4.5373 | -43.3273 | 2024-10-03 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c43e902b-d5d9-3764-b9ad-345095957529 | -4.5375 | -43.304 | 2024-10-03 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 0f354de2-d4b7-3ce4-9dbd-f358a63cea4b | -4.9264 | -43.79 | 2024-10-03 01:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3de7e85d-1112-38fe-909f-2bfa7b44ec85 | -4.9265 | -43.7669 | 2024-10-03 01:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 81e62f5c-2ef2-3692-86f7-e62324738bc0 | -5.2441 | -43.8151 | 2024-10-03 01:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a5082be6-0b73-3d41-aaa0-3440543c4d59 | -5.2443 | -43.792 | 2024-10-03 01:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 2292b7b5-ab98-3d4e-8936-c63b1a6798f2 | -6.7112 | -59.1345 | 2024-10-03 01:15:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 75a3195f-f155-3e76-9d30-4f9284b4c930 | -6.8777 | -59.0504 | 2024-10-03 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bb458eea-62b0-3584-b5c8-282ed096d34e | -6.8778 | -59.031 | 2024-10-03 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 62f0ee10-4a11-320c-8c04-c4e7c95c4366 | -7.2056 | -59.7886 | 2024-10-03 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4db0ae52-3a1d-3fd0-a253-72e22898eab3 | -8.8506 | -45.5086 | 2024-10-03 01:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |


[Clique aqui para ver as próximas entradas](README34.md)
