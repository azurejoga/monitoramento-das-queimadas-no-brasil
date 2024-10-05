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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45fba5cb-bdab-34d9-b9e9-2f252e5573eb | -17.1178 | -57.4244 | 2024-10-05 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.0 |
| cf783f25-4e58-3d17-b0d3-69a60126d2da | -18.4853 | -52.8659 | 2024-10-05 07:36:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b2219005-af7e-3962-8be9-bdb022307516 | -18.5053 | -52.8626 | 2024-10-05 07:36:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d3361f34-e73d-33cf-a858-47627118459c | -18.6785 | -57.2734 | 2024-10-05 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 9b8c9941-35de-3788-8903-464aba63d648 | -18.6586 | -57.2759 | 2024-10-05 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.4 |
| ce62718f-6b72-39a1-8c6f-7b06a3e4b7b5 | -18.6582 | -57.2967 | 2024-10-05 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 923f053e-d6f9-3047-b3d0-5bea93821045 | -18.6387 | -57.2785 | 2024-10-05 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| a06740de-277d-3117-bb46-1cc4fae9ea26 | -20.629 | -51.4722 | 2024-10-05 07:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.4 |
| 39fd9d90-a4be-398d-a863-28325638f67a | -20.6284 | -51.4945 | 2024-10-05 07:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 58fe5de7-81c1-347e-ad14-40b6d8da15fd | -12.6089 | -53.1338 | 2024-10-05 07:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 4f51859f-2ddb-3740-a502-99326840b742 | -12.6092 | -53.1129 | 2024-10-05 07:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 64655925-33aa-364c-9995-96093ba88747 | -12.628 | -53.1317 | 2024-10-05 07:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 750453dd-b922-300d-abce-a0e2d83fc3ed | -12.6283 | -53.1108 | 2024-10-05 07:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| af5c4e90-a47a-3242-9d55-c703924861c8 | -12.6723 | -54.0395 | 2024-10-05 07:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ab2be224-6ecf-37ce-ad53-38422aef401f | -16.554 | -57.2237 | 2024-10-05 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| f4af77e2-912a-3d9e-bf14-42669905a31e | -16.7647 | -57.4856 | 2024-10-05 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 1139b6ab-7716-3efa-96a6-3bbe12fc740e | -16.7843 | -57.4834 | 2024-10-05 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 7afc37be-d090-37ff-a189-94dbf0efcd27 | -17.012 | -56.698 | 2024-10-05 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 07429b32-876d-3b80-9c0b-5cf3ad6274c8 | -17.0316 | -56.6956 | 2024-10-05 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.2 |
| 44fc0210-8a11-33d5-a16e-0ad86d4374b5 | -17.0319 | -56.6749 | 2024-10-05 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 4848ae33-d74a-34ad-916e-2c743ddc0b87 | -17.1178 | -57.4244 | 2024-10-05 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.0 |
| a7bdcbe4-c6e2-3781-a909-5312e57e2535 | -17.1182 | -57.4039 | 2024-10-05 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.0 |
| 8548076a-d821-3912-9151-ff4f73caa966 | -17.1375 | -57.4221 | 2024-10-05 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.8 |
| f8ab8e45-2aac-3ec4-9986-1b338b6e75b5 | -17.1378 | -57.4016 | 2024-10-05 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.5 |
| 378356a4-4222-3451-8f10-9a7da1c78d20 | -18.4849 | -52.8876 | 2024-10-05 07:46:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8d62f859-3c7f-3143-b4a1-35cc6fbe0ac2 | -18.4853 | -52.8659 | 2024-10-05 07:46:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 9a7f59a6-6d68-3b84-992e-f1ba051d13f6 | -18.5053 | -52.8626 | 2024-10-05 07:46:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 9b918a4a-10ec-3791-82f7-5d4a0b8573a7 | -18.5058 | -52.841 | 2024-10-05 07:46:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| bedde0be-0e3e-3f64-9413-3d9c0c313513 | -18.6582 | -57.2967 | 2024-10-05 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 39ee4a27-b4bc-35f3-a905-ea5a5ee9904d | -18.6586 | -57.2759 | 2024-10-05 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.9 |
| ff02446f-2282-3952-ac06-a66867d7a2b5 | -18.6785 | -57.2734 | 2024-10-05 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 7c1dc061-5a23-312d-a02d-53670c2e9566 | -20.6284 | -51.4945 | 2024-10-05 07:47:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| fee59775-103e-3350-8e89-884c58e0193a | -20.629 | -51.4722 | 2024-10-05 07:47:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.5 |
| ef9f51c1-1035-34f9-aa18-b2189fff6db8 | -12.6089 | -53.1338 | 2024-10-05 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 4ffc71c2-518a-3e87-ba17-8f83bf700267 | -12.6092 | -53.1129 | 2024-10-05 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 2ee1273e-1eca-36db-b545-9c92b44cee73 | -12.628 | -53.1317 | 2024-10-05 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b8289ab2-019e-3614-a1f8-c115cfc3f2d3 | -12.6283 | -53.1108 | 2024-10-05 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| c4daf385-0fe2-3eb5-ae9b-54a3a6b76561 | -12.6532 | -54.0415 | 2024-10-05 07:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 748e74df-1d4d-3016-bac9-d36544f4c707 | -12.6723 | -54.0395 | 2024-10-05 07:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bacf19c0-c09d-3096-8409-17b42459a9bb | -16.554 | -57.2237 | 2024-10-05 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 854c2101-2b68-3bba-bc58-ef476838aa89 | -16.6594 | -55.5427 | 2024-10-05 07:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| cc7ec67c-152a-32f9-8315-9e2b69fe9a81 | -16.7647 | -57.4856 | 2024-10-05 07:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 2ec4ce5d-2b55-34a1-b50d-2a467add623d | -16.7843 | -57.4834 | 2024-10-05 07:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 970424b8-2172-3ad7-bb80-5f6ebc2d1f13 | -17.012 | -56.698 | 2024-10-05 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 5dd11bb2-1220-3a27-b674-54c286c5314d | -17.0316 | -56.6956 | 2024-10-05 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 03da1fbe-3ee6-3dce-8c24-a27e9e440058 | -17.1178 | -57.4244 | 2024-10-05 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 151.8 |
| d964055d-eaac-31f5-903e-cdd0f89a4f26 | -17.1182 | -57.4039 | 2024-10-05 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.6 |
| d834a44a-d0cd-3067-aeab-8941441ec12b | -17.1375 | -57.4221 | 2024-10-05 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.5 |
| 3749886b-be3a-3833-ba39-9137dabcd6ee | -17.1378 | -57.4016 | 2024-10-05 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.5 |
| bc8e4d01-6f01-349f-9dc5-dbe2e82e57a2 | -18.4849 | -52.8876 | 2024-10-05 07:56:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 14963771-0bfa-3ef7-9111-75eeb1785305 | -18.4853 | -52.8659 | 2024-10-05 07:56:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 86f21c0e-0c3b-3d7e-aa49-5f0e0cd2e3b3 | -18.5053 | -52.8626 | 2024-10-05 07:56:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 213.0 |
| aa652d98-c58c-3dee-9f1d-4f416ce967a3 | -18.5058 | -52.841 | 2024-10-05 07:56:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b89dab50-9144-346e-99c1-048e05ff7b53 | -18.6586 | -57.2759 | 2024-10-05 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.1 |
| d342965a-9922-337d-9edd-a057d7d6012e | -18.6785 | -57.2734 | 2024-10-05 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 85f00e71-4aa1-3fc2-b9e9-2d3c54837e1c | -20.629 | -51.4722 | 2024-10-05 07:57:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 70ee109b-7276-30ea-875e-a2505b43a332 | -12.6723 | -54.0395 | 2024-10-05 08:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 7c7f5406-bd08-3e96-b8a2-6181458da3ba | -12.6474 | -53.1088 | 2024-10-05 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 2b1c07da-debd-3a7e-9035-ae09ddc1a1b1 | -12.6283 | -53.1108 | 2024-10-05 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 010ab568-0814-3a31-ac6f-9eea4a30874d | -12.628 | -53.1317 | 2024-10-05 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4e157425-071d-3a23-959c-3494e214f425 | -12.6092 | -53.1129 | 2024-10-05 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9de533cc-4432-34d9-a9bc-17488ce7b7b8 | -12.6089 | -53.1338 | 2024-10-05 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| ed2f7986-5f0e-3236-a049-409925796c63 | -16.5345 | -57.2259 | 2024-10-05 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 943cf77c-47fd-36cb-bf0f-876c6a782e97 | -16.554 | -57.2237 | 2024-10-05 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 6fc2ef78-f7b4-3e17-8ee0-5999b1943c6c | -16.7843 | -57.4834 | 2024-10-05 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 854b51f2-8a33-3fe9-8b91-156ea6d0b5f4 | -16.7647 | -57.4856 | 2024-10-05 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 113a50cf-2aa2-388e-882d-856e4901e295 | -17.012 | -56.698 | 2024-10-05 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| c103872d-058f-3c4e-a6a5-3eb2439b00f1 | -17.0316 | -56.6956 | 2024-10-05 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 634b289b-95c4-3073-a51f-35a39222d3fe | -17.1178 | -57.4244 | 2024-10-05 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.8 |
| 700153bd-54bf-383a-ba56-9bae8c33088c | -17.1182 | -57.4039 | 2024-10-05 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.9 |
| bfcfe4ef-e1c2-30aa-8074-effff654e714 | -17.1378 | -57.4016 | 2024-10-05 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.1 |
| af901e77-fdba-3022-a7aa-24fdd19f74e1 | -17.1375 | -57.4221 | 2024-10-05 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.7 |
| f36ecb23-d55c-3a1a-91fe-46225ee8dde5 | -18.4853 | -52.8659 | 2024-10-05 08:06:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8e35ef74-82bf-37f4-a2ac-d7f83cb77555 | -18.5053 | -52.8626 | 2024-10-05 08:06:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e39769fd-b5d3-3c7e-8614-8043ad8b6c64 | -18.6785 | -57.2734 | 2024-10-05 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| d6ffb66a-1481-3501-8470-0652e9417f80 | -18.6586 | -57.2759 | 2024-10-05 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| c4f47456-75b7-3eb8-bf43-b23a3295b9ee | -12.6532 | -54.0415 | 2024-10-05 08:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6b5680fa-9c6f-38ec-9772-172ce081a7fa | -12.6474 | -53.1088 | 2024-10-05 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6b33a80c-3823-30b8-8d36-81fb29ad4ade | -12.6092 | -53.1129 | 2024-10-05 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9205a61b-f6ca-3e79-8c96-c2d69ee3b66b | -12.6089 | -53.1338 | 2024-10-05 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c1db445f-95e9-3cc0-8bbd-1d2c6249fdb4 | -12.6283 | -53.1108 | 2024-10-05 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 5459bf92-f4fb-33a5-945b-2400d9760548 | -12.628 | -53.1317 | 2024-10-05 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 8a07d129-6633-3d01-b8fc-74fdf4e7f2d9 | -16.5345 | -57.2259 | 2024-10-05 08:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 215140f8-a366-300d-b344-b7e05779bfaf | -16.554 | -57.2237 | 2024-10-05 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 047088d5-576a-318e-ba85-e972ff37419c | -16.7843 | -57.4834 | 2024-10-05 08:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 145ed70f-bcdf-33c6-b544-78c56f2eb930 | -16.7647 | -57.4856 | 2024-10-05 08:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 09171c3b-4ce6-3ec6-8d9c-fd414e924889 | -17.1378 | -57.4016 | 2024-10-05 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.7 |
| 29713572-ed51-3592-8b29-d427f5659556 | -17.1375 | -57.4221 | 2024-10-05 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| 641339cc-a681-3d84-a675-ce5d4e436c6e | -17.1182 | -57.4039 | 2024-10-05 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.8 |
| c1569438-3bfb-3add-b0f3-4b3348bcea55 | -17.1178 | -57.4244 | 2024-10-05 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 157.2 |
| 00696a1e-2c70-39b8-ab23-15de2ffd033b | -18.4853 | -52.8659 | 2024-10-05 08:16:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 2c6dd482-3b5b-3824-882b-99e8062b89b8 | -18.4849 | -52.8876 | 2024-10-05 08:16:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1082599f-6b79-3b1b-94d4-ccb2e428e8bb | -18.5053 | -52.8626 | 2024-10-05 08:16:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 80ef4907-10a6-3af6-b4a4-205cecc304d1 | -18.5048 | -52.8843 | 2024-10-05 08:16:50 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 898d2811-a73a-3737-9f98-14e070456043 | -18.6785 | -57.2734 | 2024-10-05 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 599449ae-4983-35ea-8121-7f07929b5b02 | -18.6586 | -57.2759 | 2024-10-05 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 68f6a777-4d74-3e4e-8a3e-13594c245f88 | -20.6494 | -51.4681 | 2024-10-05 08:17:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| be559a4f-dfeb-3b69-a512-fd594941c1d5 | -20.629 | -51.4722 | 2024-10-05 08:17:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| e3901d07-450a-3c0e-a8dc-93b288e2396c | -20.6284 | -51.4945 | 2024-10-05 08:17:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 3cd2753f-774a-3b10-88d4-bbba2614a6c9 | -12.6283 | -53.1108 | 2024-10-05 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |


[Clique aqui para ver as próximas entradas](README155.md)
