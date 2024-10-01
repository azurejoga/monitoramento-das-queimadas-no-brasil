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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c7f87e8-e387-3945-b557-38c70001bc1d | -22.37 | -49.3477 | 2024-10-01 12:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.4 |
| 44db3fe8-e44d-329d-a215-c8c4ae37f2e7 | -10.6787 | -46.1538 | 2024-10-01 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 2215553b-e386-33eb-8466-612ad8f12ad4 | -10.6978 | -46.1514 | 2024-10-01 12:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 2b0029be-aeca-3617-9525-f9773481e23d | -10.5746 | -48.0178 | 2024-10-01 12:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 10c43582-27cd-3f87-8eb4-c0a6b8286264 | -10.5743 | -48.0399 | 2024-10-01 12:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f4264285-56da-377d-8c14-15cc415d5159 | -10.5553 | -48.0421 | 2024-10-01 12:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| bd052619-5cd2-393c-a64f-84b59fd2de9f | -10.996 | -46.5418 | 2024-10-01 12:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 25a29311-b3fd-3419-934f-ef4e2b0653b8 | -11.258 | -45.6682 | 2024-10-01 12:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5fe1bf54-94c1-3b5d-bec7-0aba931f5599 | -12.1402 | -50.074 | 2024-10-01 12:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8f7bbc1b-cf05-3151-9a79-1fe0f9bbac6b | -12.1406 | -50.0524 | 2024-10-01 12:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4c5019fd-1b5c-3c9e-81bf-00e4cda73c66 | -12.4125 | -50.9635 | 2024-10-01 12:26:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 62902f3d-e622-3e13-a44a-8a237a3c18d4 | -12.9205 | -51.4563 | 2024-10-01 12:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b3070507-529b-305c-b341-76c2cdc1cb5a | -12.9803 | -51.3 | 2024-10-01 12:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 0ea566e8-351f-3be5-a5b2-9a535ee97e9a | -13.0396 | -51.186 | 2024-10-01 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 87227c43-1511-3622-80c5-f6f4a6b76709 | -13.2116 | -51.2073 | 2024-10-01 12:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| e32b77a0-5348-3733-8c71-03f30b278d74 | -13.5765 | -51.1821 | 2024-10-01 12:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 686b3209-39a0-362e-8df0-f7f8f9e3aa6d | -16.4939 | -57.3327 | 2024-10-01 12:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| c789e37c-bb36-39c2-ad91-18f6b2400fae | -16.5134 | -57.3305 | 2024-10-01 12:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 212a5c5f-2d79-3898-aace-d9a54ef3656f | -16.474 | -57.3553 | 2024-10-01 12:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 23ff5642-b94f-3a8e-8f4c-851e99658b37 | -16.4935 | -57.3531 | 2024-10-01 12:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 3724ccee-183d-3ddd-975d-b69f3385c2f2 | -16.4536 | -57.4188 | 2024-10-01 12:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.7 |
| a61aff1d-66b1-3cd4-94aa-a30ba92a103a | -16.7461 | -57.4265 | 2024-10-01 12:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| b060ba81-e97d-3c61-9ad9-b8e50c369c3a | -16.7728 | -55.7773 | 2024-10-01 12:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| cebc2a88-da34-3197-b4af-41233ab1af3a | -16.7471 | -57.3651 | 2024-10-01 12:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.7 |
| b0f6588d-94f4-3f6b-ac64-ef23a678a0c2 | -16.7724 | -55.798 | 2024-10-01 12:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| a92f32ac-5111-30de-bf00-1c0e214ecbf6 | -16.6455 | -55.2117 | 2024-10-01 12:26:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 2802dba3-7640-3fae-ac6f-e380deda813b | -16.6108 | -57.3398 | 2024-10-01 12:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 2d46f5f5-461c-32da-a115-72c60b6d344e | -16.8787 | -57.6971 | 2024-10-01 12:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.6 |
| 9650e039-8cfc-3405-a670-7b6795a3d7d0 | -16.8784 | -57.7175 | 2024-10-01 12:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 9e7ec585-1f11-3423-b9a0-b576b7da0843 | -16.8983 | -57.6949 | 2024-10-01 12:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 9ce6e96e-7797-30d1-8cd8-bdb8fc2bedad | -17.0895 | -56.7503 | 2024-10-01 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| c61490e3-3965-395c-9ee1-79445d8994cf | -17.0699 | -56.7527 | 2024-10-01 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 46eb01dd-fa75-3eb5-9f57-71b6ab76a089 | -17.0898 | -56.7297 | 2024-10-01 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 2b95ef4a-be8d-3e3d-89a4-c32812f1af7d | -17.705 | -53.2046 | 2024-10-01 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0dcc26da-2c89-3953-898d-e97a56b01187 | -18.1127 | -49.0983 | 2024-10-01 12:26:47 | GOES-16 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e41590a1-06e3-31c7-8026-6f0e6c44fb8a | -18.6973 | -57.333 | 2024-10-01 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 8df71486-dd14-329d-a671-c2d746f42fef | -18.6977 | -57.3123 | 2024-10-01 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 9a43aa0d-f52a-39a3-a6a4-71d55e6d3356 | -18.7176 | -57.3097 | 2024-10-01 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| f6932176-12b6-34bc-80eb-b52afbda7ac6 | -18.8895 | -49.1942 | 2024-10-01 12:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.4 |
| 47f32e8f-b4c5-39bc-ae92-cc05d11f583f | -18.9096 | -49.1902 | 2024-10-01 12:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 256.6 |
| 33a86451-1edb-3228-805e-d80bccc0b2c7 | -18.9091 | -49.2129 | 2024-10-01 12:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.2 |
| 38219ced-7f1f-33fe-9199-da1215f8e1cb | -21.3834 | -48.4915 | 2024-10-01 12:27:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 809c0ee9-100a-3b0d-8d62-91767f9be7ee | -21.3841 | -48.4681 | 2024-10-01 12:27:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 136.1 |
| c0b6a356-3da1-322a-b905-e9fc786e0c5a | -21.5892 | -47.7882 | 2024-10-01 12:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 353.1 |
| 4e75bb61-5a4e-37df-9ae4-34c6868a4986 | -21.6099 | -47.7831 | 2024-10-01 12:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 370.1 |
| 8a595455-5f5c-388b-a121-05b36df314ef | -21.5864 | -47.8827 | 2024-10-01 12:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 279.3 |
| 494dbbd4-0b26-33b5-86c8-400d20b9bce2 | -22.3707 | -49.3244 | 2024-10-01 12:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 247.8 |
| 1c6248f3-b09b-31e5-a592-8ed89a0d1be2 | -22.3498 | -49.3293 | 2024-10-01 12:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.2 |
| 2d769a6f-e9c9-3f67-a840-6bce270d7943 | -22.37 | -49.3477 | 2024-10-01 12:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.2 |
| 3b787e20-c0f7-39dd-a466-2b5ed0b66496 | -22.3713 | -49.3011 | 2024-10-01 12:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 242.9 |
| 4ea798fb-6499-37a2-b1fe-dbcf7742c428 | -7.844 | -43.0753 | 2024-10-01 12:35:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| ff6ef10b-333b-337e-8ec0-419d673fb69c | -10.5743 | -48.0399 | 2024-10-01 12:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c56a0720-d38d-3066-b215-cc68f407eafb | -10.6787 | -46.1538 | 2024-10-01 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 5e6f551a-c9a0-3609-be9c-880e54ed57f8 | -10.6978 | -46.1514 | 2024-10-01 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| d10569ff-295a-32c9-bd8a-e73105917882 | -10.5746 | -48.0178 | 2024-10-01 12:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| de24febc-2fbd-3df0-bc74-09561f337a5b | -10.6791 | -46.1311 | 2024-10-01 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d9c84e97-2368-326a-b631-06cacd09e8cb | -10.9463 | -47.2869 | 2024-10-01 12:36:08 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| faf9bcb3-27f2-3bd4-9154-5373dae40eda | -10.9459 | -47.3092 | 2024-10-01 12:36:08 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c16e3a91-9524-39b5-8d71-5340eca76952 | -10.996 | -46.5418 | 2024-10-01 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| b9ecc9e8-138e-3644-9496-523ec5b5051d | -10.9964 | -46.5192 | 2024-10-01 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0357edeb-0412-3c19-8380-6214f1df93ee | -11.258 | -45.6682 | 2024-10-01 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| ae601e4a-4bc6-33ff-ae8d-c969cde18927 | -12.1593 | -50.0717 | 2024-10-01 12:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7cdb9c79-7902-33aa-8810-82ca799b8ed6 | -12.1406 | -50.0524 | 2024-10-01 12:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| da616f2e-9683-37ef-9e2d-2b104e5de0ae | -12.1402 | -50.074 | 2024-10-01 12:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fbb487b7-50ee-302b-bafc-3b2c687d8c46 | -12.4125 | -50.9635 | 2024-10-01 12:36:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 4750b797-bacb-3ade-8aca-3d5f3c40cb1e | -12.9608 | -51.3237 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3c16dd4a-9a5b-31e6-b383-30e8c83b1860 | -12.9995 | -51.2976 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a03441a2-921b-3c8d-b4e5-57e46841fdd4 | -12.9625 | -51.2169 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 7f1e7672-39b3-3f6d-80c9-50671bf6c2d7 | -12.9998 | -51.2763 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| fa0a8f00-a4b9-390d-bd82-3482b59c1029 | -12.9803 | -51.3 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 21211a53-3210-36cf-abbb-2536ad222740 | -12.98 | -51.3213 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 36db23d7-2b4a-3f07-9d36-7081ac5e0f69 | -12.9205 | -51.4563 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e1eed5b4-6ad0-3fb2-b62f-ffd6dd1fe088 | -12.9807 | -51.2786 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 3f3300b7-b40f-3584-919b-79791242d21b | -12.94 | -51.4327 | 2024-10-01 12:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b6872b06-3e68-3eb5-b3c8-26c78be9fc45 | -13.0396 | -51.186 | 2024-10-01 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| b4324248-a691-38c2-a70d-7ac31120ccd6 | -13.218 | -48.5797 | 2024-10-01 12:36:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 531e8c99-8d11-3091-9d0f-f310e3cd25dc | -13.0587 | -51.1837 | 2024-10-01 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| db2899fc-a588-3e73-b4b2-03104ea24ed8 | -13.2116 | -51.2073 | 2024-10-01 12:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 64a9d3f1-517a-3cad-9229-b43cb62435c6 | -13.5765 | -51.1821 | 2024-10-01 12:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 71facd58-730b-3423-8337-298c3583637e | -13.5768 | -51.1607 | 2024-10-01 12:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0c7a658d-bae5-3317-bbaa-01672da1c748 | -14.7596 | -48.769 | 2024-10-01 12:36:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 807cdcf9-a1df-3183-92d3-10077038f611 | -16.5134 | -57.3305 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 1de7ef7e-b480-3b41-82c3-e15ff5b618a0 | -16.5131 | -57.3509 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| b6e7268f-df96-35d6-b466-340f6585790a | -16.4539 | -57.3984 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| bafc37c5-1990-3695-a6e9-6113637148f0 | -16.4939 | -57.3327 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| e3688eef-880d-3733-8747-8359258dea80 | -16.474 | -57.3553 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 7aa44a52-1171-3c9f-b12b-62b620043971 | -16.4935 | -57.3531 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 102c6cde-2b80-3fdd-88dd-e10121f9488e | -16.4536 | -57.4188 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.2 |
| 5279ac47-ea68-3a4b-ae53-f772dd2a5de1 | -16.4743 | -57.3349 | 2024-10-01 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 21dfd689-67bc-3513-8756-7dd9f607edbb | -16.7461 | -57.4265 | 2024-10-01 12:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 2f61d758-4a8e-3893-bac7-838a3edd5b24 | -16.7532 | -55.7797 | 2024-10-01 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 58f6118a-e422-3747-b51c-c1c9699567f6 | -16.6525 | -55.958 | 2024-10-01 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| f291e958-2829-3899-8da1-7ff3dd2bb62d | -16.6459 | -55.1908 | 2024-10-01 12:36:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 2bbdb9d9-ffe4-30a8-a575-1c5648e3125e | -16.6528 | -55.9373 | 2024-10-01 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 17fc8649-e160-36b5-9afd-8178a9751694 | -16.7471 | -57.3651 | 2024-10-01 12:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 227.3 |
| f4d83b41-a3dd-3d4f-92d1-7bab07eea696 | -16.7275 | -57.3673 | 2024-10-01 12:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 4468b208-4689-339d-8cdc-cdbc74b3cff6 | -16.7724 | -55.798 | 2024-10-01 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| fb4fb1a6-7ad4-3b62-8aee-6956e9776e09 | -16.7528 | -55.8005 | 2024-10-01 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| c7c0ce51-e475-3050-b553-8bffd508549a | -16.6455 | -55.2117 | 2024-10-01 12:36:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 475c6806-f265-3923-803e-14b5e01cb9fe | -16.7728 | -55.7773 | 2024-10-01 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |


[Clique aqui para ver as próximas entradas](README164.md)
