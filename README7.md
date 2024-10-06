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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f105743-cfc6-38c0-be36-5f7cbab6b396 | -16.114201 | -50.444199 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08772bbf-76bf-33d8-a8e2-5915febeb8bf | -16.115801 | -50.451302 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70c5197d-f3e8-39f9-b20c-c093795a1e58 | -16.1173 | -50.4585 | 2024-10-06 00:46:39 | METOP-B | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bcaaf2a6-57a7-32f0-a164-4b0cc538ffca | -16.106001 | -50.453499 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 645ca9f7-b431-32c7-ad31-b2535bbe7a6d | -16.614 | -55.9214 | 2024-10-06 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 184.8 |
| 2e728011-b669-3453-8d45-c4a93f626a55 | -16.6143 | -55.9007 | 2024-10-06 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 19bd100a-d18c-3daf-9e78-89a76317f100 | -16.6398 | -55.5452 | 2024-10-06 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 144.0 |
| 2f42ec5a-d241-3e7a-89b4-23564dabf04e | -16.6402 | -55.5243 | 2024-10-06 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| c8ad13a0-dd7a-3a3d-9032-bd5102ee1a99 | -16.6594 | -55.5427 | 2024-10-06 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 63b8ad38-9c64-3258-8e7f-71ea94d609ec | -16.6871 | -57.4536 | 2024-10-06 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 33ab3dc3-5361-3929-a19d-823c101f31d1 | -16.0735 | -50.445999 | 2024-10-06 00:46:40 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b79a6135-6cd4-3ca9-9a67-b4ecfbb9d9b2 | -16.081699 | -50.436501 | 2024-10-06 00:46:40 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b165b1b-7780-3242-9c80-7bbdf6cac5cf | -16.0833 | -50.443699 | 2024-10-06 00:46:40 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a813c44-214b-3912-9423-6e1f252ab17e | -16.071899 | -50.438801 | 2024-10-06 00:46:40 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 22754ccf-d546-329e-8836-4be60963b456 | -17.0112 | -55.015301 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8940a23c-4d86-362c-b411-4a561240ae17 | -17.013399 | -55.026699 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 318112a6-6c16-3923-82de-37e45f244e7f | -17.0156 | -55.038101 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac325d8-0b18-3ba9-ada0-dfb0e4fa037c | -17.0014 | -55.0173 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 313f1568-4843-3208-8855-1d16c745a453 | -17.003599 | -55.028702 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ced68d1f-32f4-3d1d-a79a-2747b78b9410 | -17.0058 | -55.0401 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97f273fd-56d9-3203-abd4-304a179d98e8 | -17.007999 | -55.051498 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 595969c8-f41d-3d72-a321-23462588591b | -16.9939 | -55.0308 | 2024-10-06 00:46:40 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5d0297a-1f70-3309-b8d5-574406be8a22 | -16.7647 | -57.4856 | 2024-10-06 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| c2700b11-8a89-365f-ae5c-37ec2be476ab | -16.8238 | -57.4584 | 2024-10-06 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| f56dd180-22a0-3e5d-ad3b-03580aa19595 | -16.9283 | -55.8405 | 2024-10-06 00:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 034e137b-ea19-356f-8cd1-ad3083e4aa69 | -16.9287 | -55.8197 | 2024-10-06 00:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 0eba070b-d3a7-319f-b68a-66487e69a68f | -16.9348 | -56.625 | 2024-10-06 00:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 4d4da08e-c4f2-3aff-b9bd-3d7f76e02db2 | -16.9545 | -56.6226 | 2024-10-06 00:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.8 |
| b2fedbc7-a8db-320b-9512-65d975a923e3 | -15.3999 | -47.6735 | 2024-10-06 00:46:41 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8044ae1-b251-3086-9768-a2854642a1f6 | -15.4017 | -47.681198 | 2024-10-06 00:46:41 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 378676b8-e9c6-3c6a-961a-3465cbb32eb0 | -17.1518 | -56.1273 | 2024-10-06 00:46:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3991c61b-de2a-3d83-9111-196502817a61 | -17.142 | -56.129299 | 2024-10-06 00:46:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8becbd61-94f4-3c81-a135-22584b231d74 | -16.872299 | -54.822899 | 2024-10-06 00:46:41 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5e61cc-c671-33e5-b7bf-d515b5256be2 | -17.3837 | -42.6483 | 2024-10-06 00:46:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 6e215e1f-0bfc-39a7-9d2f-a2af54a0ad1d | -17.0007 | -55.0607 | 2024-10-06 00:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| c71d9872-e71f-3ed4-b42f-a85927792541 | -17.0203 | -55.0581 | 2024-10-06 00:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 18c06a8f-efb2-3fcd-88cd-c39b62b3799b | -16.862499 | -54.825001 | 2024-10-06 00:46:42 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ae1d812-25e3-31ac-a4a5-394e778de360 | -16.8647 | -54.835999 | 2024-10-06 00:46:42 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63a47edd-3317-3d19-834c-8bee3312b2b0 | -16.8668 | -54.847 | 2024-10-06 00:46:42 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06a61d68-5e33-31d3-9d00-466402d3ed06 | -17.149799 | -56.4417 | 2024-10-06 00:46:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f31654b-e209-3925-93b7-47002800992d | -17.063499 | -56.034302 | 2024-10-06 00:46:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9eb402dd-97d4-33d3-abe4-e685120a278d | -14.6865 | -45.109501 | 2024-10-06 00:46:42 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0114a57-5dc8-3da3-bcf9-054d90715e2a | -14.6891 | -45.119999 | 2024-10-06 00:46:42 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9d70d12-cbab-3892-a3ca-ddd0a83b3aa6 | -17.1375 | -57.4221 | 2024-10-06 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 91b4a5ce-9f48-3ef4-a9ea-5bd5ab70b1fb | -17.1571 | -57.4198 | 2024-10-06 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| c64dacc3-fb82-3d9b-a7d0-a3fe0191052c | -17.1518 | -56.724899 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6dfddfe7-b1d3-34f9-a442-c6bbfa64feca | -17.142 | -56.726799 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42980cba-2aac-33df-94b3-b4dc4d238042 | -17.119699 | -56.7159 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8f47e8f-ccb1-3a12-8cf2-555043fa216f | -17.122499 | -56.730598 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 982a4f1a-91c6-34d5-b57e-8ff2149583dc | -17.1252 | -56.745399 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7bcc436a-fd93-3320-8d34-381641e2e073 | -16.936399 | -55.7911 | 2024-10-06 00:46:43 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a257de79-03d6-3294-9c5f-5019feb12850 | -16.938801 | -55.803799 | 2024-10-06 00:46:43 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d79183b5-4801-378d-9f3b-2b5212f88099 | -16.941299 | -55.816502 | 2024-10-06 00:46:43 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57c5c2d5-f9e6-37ff-9403-dd7c503654f3 | -17.110001 | -56.7178 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9641ed06-71e4-3300-9ccd-289eb08deb46 | -17.1127 | -56.732498 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a930a24-9236-3848-9755-ebac84a0bb00 | -17.115499 | -56.747299 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de6c7fd9-7130-3ae5-bdd8-00ce38a52dd2 | -17.1182 | -56.762001 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77fbdcdc-d551-3708-8933-ce0bc5775e02 | -17.120899 | -56.776798 | 2024-10-06 00:46:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66e00ad2-c8d1-3718-9a2f-73575ce60c74 | -16.9266 | -55.792999 | 2024-10-06 00:46:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| faee3b42-b3d0-314b-a116-4cf26b491cf8 | -16.9291 | -55.805698 | 2024-10-06 00:46:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 197e8996-763e-313c-91bc-dd1992427c5e | -16.931499 | -55.818401 | 2024-10-06 00:46:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de994395-4cba-3b91-a1cd-871d55af2657 | -17.0867 | -56.646801 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17a66d30-7424-3735-b2c6-d7e0d95d88b5 | -17.1084 | -56.763901 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 334beafd-a8b6-3879-97d0-dbb035da3069 | -17.111099 | -56.778702 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ce53b66-7f7b-376a-a8c3-51904ae54709 | -17.113899 | -56.793598 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2855988-c669-3c7f-95b4-44072f8d6160 | -16.9193 | -55.807701 | 2024-10-06 00:46:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ef76f22-40c3-3aa0-946d-337a09468463 | -17.096001 | -56.751099 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f678a4b-b490-3a06-9a9c-35cf31edb722 | -17.0987 | -56.7658 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9267d5f0-52fb-3239-96d3-5a941f4c4368 | -17.1014 | -56.780602 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1fdbfd5-567d-34f7-8b5a-3aa19dd3dae4 | -17.1042 | -56.795502 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29442401-06b2-37c2-92e1-4e46a3fa5811 | -16.9685 | -56.122101 | 2024-10-06 00:46:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 208d4794-ab2b-3d4d-a28c-f208aa50be9b | -17.0672 | -56.6506 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a74fb9fd-5427-39aa-99c6-2ef5936e6e6d | -17.086201 | -56.752998 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69b951d7-9515-3803-814c-19f6aaa0e1a3 | -17.0889 | -56.7677 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8765a09c-f2a9-3873-9e9d-392c54701005 | -17.0916 | -56.782501 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58d16c13-0459-3454-9672-e9d98ed91152 | -17.0765 | -56.754902 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4700872-c2d2-34c4-9e37-c77bb43c9a21 | -17.079201 | -56.769699 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e6e28c8-cc84-33b4-ad21-108029decdd0 | -17.0819 | -56.7845 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ea64924-5055-3887-ab89-3a95bc421b34 | -17.0847 | -56.799301 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb108b42-6660-3543-ac20-155255626ac0 | -17.069401 | -56.771599 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e71468c3-caa8-3002-914a-b7b6b3de8291 | -17.0721 | -56.7864 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 34a8eb4a-c26b-329c-9f0b-a3fb9187106a | -17.171301 | -57.327599 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7cba68eb-128d-3cdf-a990-f431ca511c68 | -16.8827 | -55.8283 | 2024-10-06 00:46:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a1bc77b-06b2-3e5a-a507-0c1b7b66af4c | -16.885099 | -55.841 | 2024-10-06 00:46:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8e02234-5565-362b-9622-6020e2d80297 | -17.038 | -56.656399 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac3a231a-087b-3cf2-9f29-1f88bda03ef7 | -17.056999 | -56.758701 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26cde117-f435-3e96-aedb-dab40dba34f9 | -17.0597 | -56.773499 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 972a2a08-2ffd-331d-87db-b7f86fa1bf77 | -17.062401 | -56.7883 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa934718-05c3-3aaa-80e9-8970c11eed71 | -17.1616 | -57.329399 | 2024-10-06 00:46:44 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37893f36-628d-3a5b-8eb8-dd0b45359214 | -16.870501 | -55.817501 | 2024-10-06 00:46:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8671f6a-fb9c-34a2-8892-ca55a72f0dd9 | -16.8729 | -55.8302 | 2024-10-06 00:46:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7236e85-c433-3902-9058-b57e7daee92d | -16.875299 | -55.842899 | 2024-10-06 00:46:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ff71baa-6d06-3423-b687-ba56ea552334 | -17.025499 | -56.643799 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 306623ea-faea-36d1-99da-8f91e55f5a63 | -17.0282 | -56.658298 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50144341-04a8-3a3f-b244-6bf09658ab0d | -17.030899 | -56.672798 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db409c29-94cc-31dd-b981-73af10c57055 | -17.0336 | -56.687302 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a395ea54-5d44-3cd7-8e90-343ea8c125b2 | -17.036301 | -56.7019 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d527b557-0331-3960-9b54-b31af044a6ad | -17.047199 | -56.760601 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59ac62b8-5925-356d-b3ff-0871188b25ed | -17.0499 | -56.775398 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73d4d038-89dd-3928-b181-eccbc2a3ce3f | -17.052601 | -56.790199 | 2024-10-06 00:46:45 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README8.md)
