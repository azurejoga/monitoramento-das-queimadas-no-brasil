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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa5d632-94bd-3133-aba6-f6fd748ace36 | -21.66545 | -43.9655 | 2024-10-02 03:34:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e2b182b9-1729-3b42-bf33-10f222baaed7 | -21.56211 | -43.96227 | 2024-10-02 03:34:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c3cf27eb-fd2f-3985-9932-26ff6bd5b32a | -21.5573 | -43.9609 | 2024-10-02 03:34:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 04ae91c1-94ec-37c2-aa47-40dad4b6541b | -21.47758 | -44.58462 | 2024-10-02 03:34:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b3df2bb7-c448-3ffc-8997-3f72388d7da7 | -21.46835 | -44.57796 | 2024-10-02 03:34:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c16483f6-bb34-34bc-bd12-4d23f4d04d99 | -21.46768 | -44.58113 | 2024-10-02 03:34:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29537acc-bd07-3f59-8f38-c3c2a8f7f49f | -21.46269 | -44.57959 | 2024-10-02 03:34:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 207c7432-ddbb-3457-9543-7fa10c18b798 | -21.46199 | -44.58289 | 2024-10-02 03:34:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 48bbcde4-868d-339d-a1c9-4e845d294cf0 | -21.29049 | -47.62124 | 2024-10-02 03:34:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 18416b92-e4cf-327b-8b29-2e5d25095d5c | -21.28909 | -47.62719 | 2024-10-02 03:34:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e7367b7d-6a71-34ea-b699-9662b9218f74 | -21.28474 | -47.61826 | 2024-10-02 03:34:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 66f37755-847e-36b6-b807-64d0734b7f59 | -21.28335 | -47.6242 | 2024-10-02 03:34:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fb56ffb-a908-3130-a297-24fdbc3232c5 | -3.2136 | -46.7843 | 2024-10-02 03:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ef72dca5-5bbb-398f-acfd-c4ba11a00cdb | -3.1465 | -49.4229 | 2024-10-02 03:35:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| dc702fbe-2979-3cae-b838-1a6b9f2d31e4 | -9.9553 | -64.9172 | 2024-10-02 03:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 194944e1-93c3-32dd-922e-5b05e32a290f | -9.9368 | -64.8991 | 2024-10-02 03:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 50c08499-41e4-31ec-a91d-396904213c9d | -9.9367 | -64.9179 | 2024-10-02 03:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 648e2256-fb45-3d09-8f0c-0af0619a1c52 | -11.6743 | -64.9983 | 2024-10-02 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a5104111-5b41-3fea-ad79-795fc9d76a7c | -11.6742 | -65.0172 | 2024-10-02 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1455bf96-df26-3585-a88b-bb97abcf2dfe | -12.7054 | -63.0798 | 2024-10-02 03:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 68b9dd1b-1c43-3919-b63f-79495aa62776 | -12.6484 | -63.1214 | 2024-10-02 03:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 0d10e97f-1e61-35e0-8333-5f82725e1b7b | -12.8803 | -62.531 | 2024-10-02 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0f700f88-b4df-3a45-baf3-e84e44ff20d0 | -12.8614 | -62.5321 | 2024-10-02 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 121.1 |
| efbdffe5-7b5d-3d22-b606-538439263a00 | -12.8612 | -62.5514 | 2024-10-02 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 228a65b7-545d-3fd1-90ea-f2964a69f525 | -12.8424 | -62.5333 | 2024-10-02 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 119.3 |
| fce259e0-1c7f-324f-af18-7a716b549aac | -12.8423 | -62.5526 | 2024-10-02 03:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 903868ec-71f0-3b6c-b4ad-920cb6c3f500 | -13.2173 | -48.624 | 2024-10-02 03:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 306fc0d6-1d71-37a8-a4df-c32ebf5df6bb | -13.198 | -48.6267 | 2024-10-02 03:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 9a4f5a33-f4b6-3605-976d-912debfd9cd4 | -14.5699 | -44.8351 | 2024-10-02 03:36:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 63494a73-c276-37ea-92a4-e029f85a35e9 | -16.109 | -53.5215 | 2024-10-02 03:36:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 681f683b-cdc6-3c87-9836-4b29c4b22056 | -16.0895 | -53.5242 | 2024-10-02 03:36:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 9978cba6-9056-3ceb-9340-09dcd33fae9f | -15.8936 | -57.155 | 2024-10-02 03:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 2f488cca-03af-30cf-956e-08fb8a04bbe6 | -15.8933 | -57.1754 | 2024-10-02 03:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c8f8c86d-32d4-303e-aa23-2050ac5f328a | -16.6127 | -57.217 | 2024-10-02 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 51a15418-aff9-30c5-84c0-03dce768a672 | -16.6124 | -57.2375 | 2024-10-02 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| ac433904-77ba-3071-8837-7a58527b1bdc | -16.514 | -57.2896 | 2024-10-02 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 22ada621-d68e-31c4-9387-44ae4272caa4 | -16.5137 | -57.31 | 2024-10-02 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| f34fb4eb-6342-3f82-91aa-18a408da5373 | -16.4945 | -57.2918 | 2024-10-02 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| fb0acf14-dcee-3693-aa4e-48d64ba22c52 | -16.4942 | -57.3122 | 2024-10-02 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 4901be1b-7acb-35d3-acd7-6eef7b94569a | -16.475 | -57.294 | 2024-10-02 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 5f616cd5-afe1-3839-bcfb-37aaadab4dac | -16.4746 | -57.3144 | 2024-10-02 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| 2369dcf3-6a41-34b8-b940-7156353b94df | -16.7647 | -57.4856 | 2024-10-02 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.8 |
| cfdb73e6-b711-3aec-b4bb-5baaa5218686 | -16.7461 | -57.4265 | 2024-10-02 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| e3a01e20-7c48-32f6-b816-dbb23a6a0e38 | -16.7455 | -57.4674 | 2024-10-02 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 53b8952d-b3ea-31c4-a285-31b4714a64fa | -16.7452 | -57.4878 | 2024-10-02 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 7ad46549-eb96-3f2f-8a08-355c451c9699 | -16.7262 | -57.4492 | 2024-10-02 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| d2b79111-8bb4-3740-adab-0879fa924953 | -16.7063 | -57.4718 | 2024-10-02 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| a1e35690-ceb9-3ea5-b4af-51176051ab53 | -16.6518 | -57.2125 | 2024-10-02 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 5b073d04-fe33-396e-a8ac-8da0e54075d2 | -16.6322 | -57.2147 | 2024-10-02 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| d2ab4c8d-2284-3aa1-9ecc-88f40c49b556 | -16.6319 | -57.2352 | 2024-10-02 03:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| ae86c879-d1a9-30b9-a2c7-d2b3770ed2d2 | -16.7265 | -57.4287 | 2024-10-02 03:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.5 |
| 4949eace-166e-3e97-bd9d-87e32bca3d7b | -16.8891 | -55.8455 | 2024-10-02 03:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| a4aef4db-63ae-37a4-9f7d-41d5dfe5befb | -16.8698 | -55.8272 | 2024-10-02 03:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 55604a46-0812-31ff-a4f9-c7d5e3b8d1f5 | -16.8695 | -55.848 | 2024-10-02 03:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 138.0 |
| accf6f6d-8c18-3a0c-83f0-a2d912883754 | -16.8386 | -57.7628 | 2024-10-02 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.6 |
| 255dcf4e-b9d8-3e12-a2c5-f721a62d99df | -17.1581 | -56.1637 | 2024-10-02 03:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 692d68b3-b3c1-36dc-9da3-ff4db9ae3872 | -17.1577 | -56.1844 | 2024-10-02 03:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 7203aeb5-ae72-3301-aff0-ea06bc54388c | -17.1288 | -56.7455 | 2024-10-02 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| a19de393-8b54-34bf-8d1c-1ed625986aff | -17.1091 | -56.7479 | 2024-10-02 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| fa90da17-c132-3133-a336-3c246430ecb2 | -17.1088 | -56.7685 | 2024-10-02 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| afd8cedb-0959-3ad5-8e7d-83c39a27e21d | -17.0895 | -56.7503 | 2024-10-02 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 8a968324-bf6b-3c1f-a60e-4b764cfa72bf | -17.0892 | -56.7709 | 2024-10-02 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 200.1 |
| ff394fd5-b9b8-3c98-942d-df94394c572e | -17.0695 | -56.7733 | 2024-10-02 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 6ba5546c-6946-3d2d-a7d6-e4a49f6e32c6 | -17.1974 | -56.1587 | 2024-10-02 03:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| b9193340-31bf-3974-a13d-3a051c1be2f0 | -17.1971 | -56.1795 | 2024-10-02 03:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 3e6a53ad-209d-3209-b17c-81dad65ddb51 | -21.3661 | -55.6807 | 2024-10-02 03:37:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 67ad759a-877c-3c41-a513-ee49f9562b91 | -21.3456 | -55.6841 | 2024-10-02 03:37:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5d3f81c4-db2d-3252-b8c2-69c4e9d11f3b | -21.3451 | -55.7056 | 2024-10-02 03:37:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 85e97e52-88a0-3749-b1a7-0eb634a5a415 | -3.128 | -49.4235 | 2024-10-02 03:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8855f0ea-af47-3812-bc7b-2a321500bc2d | -4.8593 | -42.7923 | 2024-10-02 03:45:33 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3fef08ca-33c8-3db3-8b86-3359732352eb | -8.4643 | -62.7124 | 2024-10-02 03:45:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.9 |
| e5ff3f14-7844-37d1-b359-7a0a42c72d71 | -9.9367 | -64.9179 | 2024-10-02 03:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 530153dc-2d5a-317b-aa9d-76568a816a82 | -9.9368 | -64.8991 | 2024-10-02 03:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 57b78052-8616-311c-a788-33a91588824a | -9.9553 | -64.9172 | 2024-10-02 03:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 13dc71ac-33a8-3c20-b746-51299d8d5c2a | -11.6742 | -65.0172 | 2024-10-02 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 65e8ee21-bfb5-33fd-9adb-504ea2a9526d | -11.6743 | -64.9983 | 2024-10-02 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f9c84d85-db24-3552-8d72-5ff19a3c9bec | -12.6484 | -63.1214 | 2024-10-02 03:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| a277adee-fa11-339c-b46f-fa4f8bb5a8d3 | -12.8423 | -62.5526 | 2024-10-02 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 508d9b3f-53a7-3443-88e8-0073e6b1c6bb | -12.8424 | -62.5333 | 2024-10-02 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 111.8 |
| bc87ae2b-0519-376c-8f18-c3f33b29c542 | -12.8612 | -62.5514 | 2024-10-02 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| f5ad2ac9-4103-321d-80a1-345ba3e7ad91 | -12.8614 | -62.5321 | 2024-10-02 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 132.3 |
| cbe974da-5246-3acd-a5cd-072310e6ad6e | -12.8803 | -62.531 | 2024-10-02 03:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 45333c63-2ad9-3254-b1e5-18e125a9c6e9 | -13.198 | -48.6267 | 2024-10-02 03:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e70fb09c-59fa-363f-a062-23652fc608a6 | -13.2173 | -48.624 | 2024-10-02 03:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2b46a3f5-1d89-357e-9f03-3b8d7d1407dd | -13.055 | -51.4186 | 2024-10-02 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| fcd09949-9093-37f3-bd2b-4f1f2f079a7b | -13.1122 | -51.4329 | 2024-10-02 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5bbd62e8-dedf-3f29-919f-3bcb9f37ecf8 | -15.3708 | -55.8431 | 2024-10-02 03:46:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 9fe0c6de-0dcc-37e3-aa20-cad3988779e6 | -15.8933 | -57.1754 | 2024-10-02 03:46:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 1142b56f-495b-3cee-a25f-abad53b3bb7a | -15.8936 | -57.155 | 2024-10-02 03:46:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| a1eacb63-ef62-348c-9d69-c4a6bfb19f12 | -16.109 | -53.5215 | 2024-10-02 03:46:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 06f4c803-2a96-3572-9a1d-72b72aefb40b | -16.4746 | -57.3144 | 2024-10-02 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| bb2b85e2-12bc-35f3-b1a2-b500bedd5d0c | -16.475 | -57.294 | 2024-10-02 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 3abd6fe2-cfa4-3c8a-83da-75f7a741b83b | -16.4942 | -57.3122 | 2024-10-02 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| c43a85d3-8ecf-3709-b39a-17789fcc4522 | -16.4945 | -57.2918 | 2024-10-02 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| d9f84e84-f552-3640-a1b8-2660fda7f9dc | -16.5137 | -57.31 | 2024-10-02 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 7ca55d23-8f3d-32ba-97c6-dfd9f35eb5c1 | -16.514 | -57.2896 | 2024-10-02 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 71679be0-c264-33dc-b453-41844f2d1b9a | -16.6124 | -57.2375 | 2024-10-02 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 791cb527-63fa-3221-8edf-7895e0b14480 | -16.6887 | -57.3513 | 2024-10-02 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| e0064caa-db01-38e8-8530-964cd85231b2 | -16.6912 | -57.1875 | 2024-10-02 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 6313543e-72a1-331a-9c07-40733fe92394 | -16.6916 | -57.167 | 2024-10-02 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |


[Clique aqui para ver as próximas entradas](README59.md)
