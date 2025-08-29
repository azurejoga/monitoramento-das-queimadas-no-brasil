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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 688d8528-56e0-3a2e-9856-1040dfe82bee | -6.7074 | -49.4561 | 2025-08-29 02:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c2ee61cb-e90a-34e1-a85c-70027de3d977 | -12.0976 | -44.717 | 2025-08-29 02:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5663c675-e5e5-398c-9937-d357fc7cfab9 | -9.4433 | -60.5499 | 2025-08-29 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b7fc6ad3-836f-3ef2-979e-ee1f5a7876a4 | -9.7728 | -64.2657 | 2025-08-29 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e4a8c9ad-e136-3977-9c07-21c85034ca6a | -9.9328 | -59.9247 | 2025-08-29 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1470637e-08de-31e4-aaa0-92e772ff8ff3 | -9.773 | -64.2469 | 2025-08-29 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 2501ac0d-307f-3660-90c6-5d746de73a32 | -24.1648 | -49.5569 | 2025-08-29 02:50:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1d65e0d3-09f0-34bd-a554-4c551172e593 | -9.1154 | -65.7886 | 2025-08-29 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| e6cb6843-079c-3e21-9e67-6719a70d88c5 | -13.2031 | -45.2834 | 2025-08-29 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 6782d34a-fcd6-3578-afdc-575867073a63 | -8.1758 | -61.3755 | 2025-08-29 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 200f513f-2616-343f-96ec-c15ef360cbd0 | -10.3624 | -57.8258 | 2025-08-29 02:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 6f83554c-6c95-3078-99c3-26e5f9bf4960 | -9.1155 | -65.7699 | 2025-08-29 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 6a786179-6ad7-38b5-a7b0-3b8b71a54d91 | -13.5386 | -46.8775 | 2025-08-29 02:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a8760390-ffa5-32e9-b0cf-72756d83805e | -9.1156 | -65.7513 | 2025-08-29 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0fd46a7e-259d-327b-b6b0-4513f812e7d7 | -5.6081 | -45.0038 | 2025-08-29 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 21a02bf7-5289-39dc-8ef3-a52bbf286af0 | -9.462 | -60.549 | 2025-08-29 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8fd17b2b-0c63-3d47-bc8a-65971c29356c | -10.3812 | -57.8245 | 2025-08-29 02:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 79f6fbff-2709-3fea-9ff8-be625818766b | -13.1837 | -45.2865 | 2025-08-29 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 4d674645-e254-3cf0-8f0f-c8e348a17e63 | -12.4345 | -63.9173 | 2025-08-29 02:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 5e4802d8-36c0-3ab0-9ddb-b684015db08c | -9.1525 | -65.7874 | 2025-08-29 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9a6a5511-79d8-3644-8b66-e1cc550528cd | -5.6268 | -45.0025 | 2025-08-29 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| a119bb20-ff2e-3d36-8a83-309a95b7de78 | -9.0969 | -65.7705 | 2025-08-29 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 74246d90-cc4f-37b6-b85a-9d84f2620b9d | -9.4432 | -60.5692 | 2025-08-29 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4bc52953-9723-39ad-997d-45ba19573dcb | -10.3626 | -57.8061 | 2025-08-29 02:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f550fa15-7685-354a-9175-1b80c1f3c2f2 | -9.134 | -65.7694 | 2025-08-29 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1f38712b-6318-398d-b6cc-99091fb4e555 | -6.5358 | -43.9237 | 2025-08-29 02:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 770bfbb6-ea80-3dbb-b152-3a4ca1b0e50f | -9.4618 | -60.5682 | 2025-08-29 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b48e8c96-e34e-32c9-ab1b-2286a699500f | -9.7916 | -64.2461 | 2025-08-29 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 57759f39-7cb6-3b50-bc17-558b5bbaaa66 | -6.5546 | -43.9221 | 2025-08-29 02:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1e16b226-4e3f-38d5-9504-5e6a12e9e71f | -3.4254 | -49.0517 | 2025-08-29 02:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| aefcbba9-42dc-3382-8f5a-d7e43b82cd9d | -7.56407 | -37.18722 | 2025-08-29 02:58:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6cb7d05a-6966-3fe2-88c5-d878c11896fb | -6.5546 | -43.9221 | 2025-08-29 03:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 53b74982-8834-321a-81ce-9e937c43dcdd | -13.2031 | -45.2834 | 2025-08-29 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 26875ef4-9f3b-3427-bd56-45816d9979bb | -13.5008 | -46.8382 | 2025-08-29 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a2bab135-f75e-33f3-8cc0-bd2a92f7bf85 | -10.3812 | -57.8245 | 2025-08-29 03:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a7e4d897-e8c0-336c-94f2-d3d0fe0c0f13 | -8.1758 | -61.3755 | 2025-08-29 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 0de56f67-de7b-3681-9f12-7311e9022cff | -9.134 | -65.7694 | 2025-08-29 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1d38ef68-d422-3d2c-a98e-d4f5a652b752 | -12.0976 | -44.717 | 2025-08-29 03:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 10948629-8e79-3c37-91fb-0347b832c12b | -9.462 | -60.549 | 2025-08-29 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 65af5686-916c-3c12-9881-17eab912d990 | -6.5358 | -43.9237 | 2025-08-29 03:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 110f0a04-3de2-37ab-bccf-7a482c2a79ec | -9.773 | -64.2469 | 2025-08-29 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 599e9ef6-f0dc-3f11-bfe2-f7376908af51 | -10.3624 | -57.8258 | 2025-08-29 03:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ad11bf28-fdc8-3b09-a829-4808faaf4805 | -9.1155 | -65.7699 | 2025-08-29 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 420c1af4-68ec-3138-bb46-9a368654d2d2 | -5.6081 | -45.0038 | 2025-08-29 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 47f7a08a-6e72-37cf-95ac-db4f99dd9980 | -9.7728 | -64.2657 | 2025-08-29 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6129fcaf-890d-371c-a5bb-b3ee48ceab7a | -6.1672 | -47.2858 | 2025-08-29 03:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f6285a7e-0e29-3746-ba07-83ca96f3d35c | -3.4254 | -49.0517 | 2025-08-29 03:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 53619528-7a73-3f4c-a74c-76badd887e50 | -10.3626 | -57.8061 | 2025-08-29 03:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9aaced2a-ba73-307c-af0f-81cf4edd9f97 | -9.1156 | -65.7513 | 2025-08-29 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4b62e5fa-065c-3a18-b705-639896e06f7c | -10.8608 | -60.7998 | 2025-08-29 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ba0a5838-5f34-3af5-a0e3-0ea908b407ed | -13.5386 | -46.8775 | 2025-08-29 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5887be1a-b0b1-32d6-99d6-2f912dd8415c | -12.4345 | -63.9173 | 2025-08-29 03:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d972bcae-bcac-3a1d-adda-7558a071c7cd | -9.7916 | -64.2461 | 2025-08-29 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 25ed9ee6-edfc-35c3-8ab4-7089542989d4 | -9.1154 | -65.7886 | 2025-08-29 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e5af98e0-6659-35b0-89c4-bd5ad74f3b18 | -9.7322 | -64.9067 | 2025-08-29 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d10bd9b5-79ae-33c0-8062-ff85864f0dd0 | -9.4433 | -60.5499 | 2025-08-29 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0730f43c-b49f-3e99-9ea0-44e27e9326b4 | -5.6268 | -45.0025 | 2025-08-29 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fe2fe448-8d8b-3055-adc5-9620c4024e89 | -9.1525 | -65.7874 | 2025-08-29 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0ec50ac6-ac58-369c-91ce-52dcf745a5d9 | -13.1837 | -45.2865 | 2025-08-29 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| f46c56f9-9617-3cbe-b6d2-4c3849c1feaa | -9.4618 | -60.5682 | 2025-08-29 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| f58962f9-e924-3334-a244-fb545b794b3f | -20.28038 | -41.3045 | 2025-08-29 03:02:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| dbdd7a1d-38f5-35d4-8449-9ba574a6df0f | -20.28328 | -41.30539 | 2025-08-29 03:02:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| bc43e184-477c-3e02-98c3-1fa2b3d66568 | -16.3669 | -39.26514 | 2025-08-29 03:02:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d230cf59-8aac-30b1-9f27-b7d959211b56 | -16.3681 | -39.25966 | 2025-08-29 03:02:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bcba7c2e-f5f2-3975-8d25-4267f8cbeb4f | -20.28825 | -41.31394 | 2025-08-29 03:02:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 290f2be9-56ff-399f-a5f7-ae6bc795d23d | -9.9328 | -59.9247 | 2025-08-29 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 441e381e-0088-314c-a115-70aaa3afdacd | -13.5567 | -46.9426 | 2025-08-29 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| fcf74a59-5827-3700-8dd7-cc593b614f19 | -9.1525 | -65.7874 | 2025-08-29 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4274bcc3-3c9e-3e05-85cd-f8bd9bd61c51 | -6.9683 | -59.3362 | 2025-08-29 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 1c1de7c7-e82d-3f89-ae6d-c639529da67e | -9.134 | -65.7694 | 2025-08-29 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 510faada-0dae-344f-82cf-8bd494af3612 | -9.7728 | -64.2657 | 2025-08-29 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 874ae60f-71a6-3bfb-a77c-42615b948ebd | -8.1758 | -61.3755 | 2025-08-29 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 73635494-1c53-3a12-aa02-9ff0f15a1a91 | -13.5386 | -46.8775 | 2025-08-29 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 5d176c1a-bde7-3287-b5fa-7de3c9644fc5 | -6.5358 | -43.9237 | 2025-08-29 03:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b5daf811-275e-3748-a244-f3c9a91ace5e | -6.5546 | -43.9221 | 2025-08-29 03:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 3a24d88b-7c60-3c3e-b5d4-711d922a43de | -9.462 | -60.549 | 2025-08-29 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 185044f0-598e-3122-a2bc-164e4d19b169 | -9.4618 | -60.5682 | 2025-08-29 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 34d722ee-acad-395a-8eaa-fbc0e2e57dfb | -6.1672 | -47.2858 | 2025-08-29 03:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4e303615-325e-38f6-b666-60c7a5989734 | -13.5391 | -46.8548 | 2025-08-29 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 5d6c6e22-b3b9-3a00-8b27-58818f8a025e | -9.0969 | -65.7705 | 2025-08-29 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5d690529-4c0b-3f68-824c-ca1e933e5705 | -5.6081 | -45.0038 | 2025-08-29 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4d7dbca1-5b95-3a07-822f-5cb74525a8bd | -5.6268 | -45.0025 | 2025-08-29 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| abe29e5f-227b-3427-bf0c-365cca3e9592 | -9.1156 | -65.7513 | 2025-08-29 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| d70b5cce-aead-30a8-a36c-21c01271cf42 | -9.1154 | -65.7886 | 2025-08-29 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 989c4969-1b8c-3400-ab82-e053a9e99318 | -9.4432 | -60.5692 | 2025-08-29 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2ee0f803-01f6-33d7-aba1-bd5295e95568 | -9.4433 | -60.5499 | 2025-08-29 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 05a75157-2d0b-3876-93c8-4064cb14bea5 | -12.4345 | -63.9173 | 2025-08-29 03:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 735f7177-66bf-3111-b86a-ffb9b17d4a64 | -10.3624 | -57.8258 | 2025-08-29 03:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ab2fb3b6-d6ad-387a-87e3-bb61de602ba9 | -9.1155 | -65.7699 | 2025-08-29 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 72600860-b156-387b-bf9c-1a35fcf9b890 | -9.773 | -64.2469 | 2025-08-29 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 3253cca0-7603-3a91-868f-74af7f0a2ac7 | -13.0151 | -56.9184 | 2025-08-29 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a3e49658-88ee-353a-bb6e-017998d2cec2 | -6.9867 | -59.3354 | 2025-08-29 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d4bca7a0-b35d-3c18-aade-f50e7d40c530 | -9.7916 | -64.2461 | 2025-08-29 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c28e959f-ef12-3827-9a54-63bdeddc5872 | -12.0976 | -44.717 | 2025-08-29 03:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| bbcc55d5-c701-3155-b6ac-9708d29cb6f1 | -9.7322 | -64.9067 | 2025-08-29 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 1cda7036-4427-30a9-b91c-1e303701a26a | -10.3812 | -57.8245 | 2025-08-29 03:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f72f34c0-4bb5-3704-ac01-3529598493fc | -5.6268 | -45.0025 | 2025-08-29 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 76b388d4-ee3f-39cf-8aa7-21b521ac3554 | -6.5358 | -43.9237 | 2025-08-29 03:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 052b50cd-b338-3b08-aa53-db011007ac16 | -9.7916 | -64.2461 | 2025-08-29 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ec243e6b-1377-3372-9c31-d87a6f3af49d | -9.773 | -64.2469 | 2025-08-29 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.0 |


[Clique aqui para ver as próximas entradas](README21.md)
