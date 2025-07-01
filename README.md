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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5156e3a6-cd91-320d-8ae0-ccb2ba1a32b2 | -6.2945 | -43.6659 | 2025-07-01 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 38f2138b-2612-3127-bae0-36c017e8dab7 | -10.1205 | -52.3618 | 2025-07-01 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 9c11893d-af70-3e40-8e07-36f34845bb84 | -9.9658 | -48.2398 | 2025-07-01 00:00:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7cb6e338-7d07-3ab2-a0b3-5676d6d0bd4b | -6.2226 | -43.3459 | 2025-07-01 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c05e47db-daef-3efe-b197-4ff82eb8ae1b | -6.4814 | -43.743 | 2025-07-01 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 1ec48987-97dd-31fd-a5c1-dc037bfdc0f9 | -6.4816 | -43.7198 | 2025-07-01 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 331e83c4-ef90-3bc1-8842-a1f17ecb4b51 | -10.8832 | -56.4367 | 2025-07-01 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 0e7f7650-6811-380c-92d5-f309e490a84f | -9.7041 | -56.1843 | 2025-07-01 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f7449cd0-30ea-3cf1-93b6-1a11124822a0 | -10.0972 | -52.7376 | 2025-07-01 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8e04ef48-6417-3526-9ab6-6dee347981fb | -10.1207 | -52.3409 | 2025-07-01 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 297.7 |
| ede72a1b-83ba-3a96-bb15-cb66fa3e34fc | -10.1393 | -52.3601 | 2025-07-01 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 172.5 |
| a55b58a7-b80e-3543-ae46-84d0dee38e0b | -4.3197 | -48.0908 | 2025-07-01 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 297eff05-a53a-33dd-8d91-6102b65ceaa9 | -10.883 | -56.4567 | 2025-07-01 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 128.2 |
| fb7ec25c-f3ea-3a4d-a9f2-657c6fbe3c98 | -6.2943 | -43.6891 | 2025-07-01 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 39512183-5b35-38ca-aad3-e8c97a5a6d66 | -9.6507 | -50.7469 | 2025-07-01 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2e3ee52d-0323-3b72-9e8c-f077cce3bb1e | -6.5771 | -47.3661 | 2025-07-01 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8093aa85-1bc3-3b4b-8f4e-f891e7816d44 | -10.1395 | -52.3392 | 2025-07-01 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 278.6 |
| 944446b1-758c-3aa4-b6a4-be3cf8eb13a2 | -10.0784 | -52.7393 | 2025-07-01 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 7de21ca6-de13-3dbe-8707-4af8e77251d7 | -7.6239 | -45.7447 | 2025-07-01 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 109bc7b5-e6ef-3bee-ae29-ca1dc487f00c | -9.9847 | -48.2378 | 2025-07-01 00:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 0fed0e0a-17f1-30ef-b0e4-09b8ddc98802 | -7.2217 | -43.0917 | 2025-07-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 29a088f9-e436-3172-a8ab-40ec9690b0e7 | -7.2028 | -43.0936 | 2025-07-01 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 12bc1279-56e4-3cdc-8b32-ccc624f7e6a3 | -10.1395 | -52.3392 | 2025-07-01 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 5ebba958-fdb4-363c-95a6-1f5c357a651d | -6.4816 | -43.7198 | 2025-07-01 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c06f13d5-e9dd-3955-ad67-f858ffcd4887 | -6.2943 | -43.6891 | 2025-07-01 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 27dde8fc-e448-3a00-94fd-c79cb99f98e9 | -10.1393 | -52.3601 | 2025-07-01 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 1800a0d4-a8bc-3d4b-95ae-3718f6d3d104 | -6.2945 | -43.6659 | 2025-07-01 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 00b58a48-fd3a-3866-b5df-bd7b056f576f | -12.6319 | -54.2087 | 2025-07-01 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ff248471-edb7-341e-89a7-9e055f4256e1 | -6.4626 | -43.7446 | 2025-07-01 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b292e9ad-0f01-30fa-9e60-7c372850a2e5 | -6.2755 | -43.6907 | 2025-07-01 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| aa18ea0d-e775-33e1-b4ce-a6e82108fe23 | -9.9847 | -48.2378 | 2025-07-01 00:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 790c90ee-7de1-31de-808c-ed4bced94b9f | -10.1205 | -52.3618 | 2025-07-01 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 41c796a3-e263-38f5-8bdf-fb13e2535100 | -10.8644 | -56.4381 | 2025-07-01 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e2919702-400b-3d52-9eee-a5d494a5d5f3 | -10.6483 | -44.4861 | 2025-07-01 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e850bc0e-3158-31de-b6e8-c567bdb460e0 | -10.1207 | -52.3409 | 2025-07-01 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 202.1 |
| 9ca5ed69-393c-3681-8748-4ec3841f134d | -10.883 | -56.4567 | 2025-07-01 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 8383e261-c274-3ce8-9d40-6aa1e06b9803 | -6.4814 | -43.743 | 2025-07-01 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 51f636a8-f621-397a-b0f7-988ca9af5b47 | -10.0784 | -52.7393 | 2025-07-01 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| effda44e-37a9-3fbc-af5c-718d61787459 | -9.2522 | -58.7584 | 2025-07-01 00:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 06aea9b8-35b1-301c-9184-c00aed35c944 | -6.5771 | -47.3661 | 2025-07-01 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7fe962ff-5134-3b69-97b2-3b3a1c59069c | -6.2226 | -43.3459 | 2025-07-01 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 144786bd-d67a-3319-8899-b310c2de2b83 | -10.8832 | -56.4367 | 2025-07-01 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 3fd56e1f-4b33-3ed7-9567-30ac15b18024 | -9.9847 | -48.2378 | 2025-07-01 00:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8b101b88-1da2-3fc3-940e-f8437de9cc51 | -10.0784 | -52.7393 | 2025-07-01 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b5306c1b-d2bf-364a-912c-0ee4d0be83fc | -4.3197 | -48.0908 | 2025-07-01 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d10c63d1-2e66-3eaf-a351-0311ae203b1c | -10.1207 | -52.3409 | 2025-07-01 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 55715709-bbaf-305d-8263-33df39732e64 | -9.9658 | -48.2398 | 2025-07-01 00:20:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4f58f447-9f00-31d2-a2d4-5a4ea29f72f4 | -6.2943 | -43.6891 | 2025-07-01 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 63dbb545-6560-3372-89b6-88f4ca467366 | -7.2214 | -43.1153 | 2025-07-01 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 3baad466-5c68-371f-bbe2-bdbbf031f720 | -10.8832 | -56.4367 | 2025-07-01 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 156.0 |
| f9256e63-712a-3ef5-8ff3-8763f975379c | -7.6239 | -45.7447 | 2025-07-01 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 221d6bfd-b6e4-3ff9-8b17-151f3f9246c8 | -9.7041 | -56.1843 | 2025-07-01 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 35d4b95c-4962-3d68-aa73-1e3ba6b865ae | -7.2028 | -43.0936 | 2025-07-01 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| dba9c991-c266-3f2e-8951-c3ecc7751ca3 | -6.2226 | -43.3459 | 2025-07-01 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4c85187a-b0c3-3956-8c5c-75b4780632a1 | -10.1205 | -52.3618 | 2025-07-01 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6d6fa9ea-60e4-34cc-b79b-98bea93afa78 | -7.2217 | -43.0917 | 2025-07-01 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 49966ba5-2fb8-3f8e-9006-2e1f6efbc51f | -10.1393 | -52.3601 | 2025-07-01 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 279660ff-65a9-3245-aee5-c63a9ec6f0da | -7.7758 | -44.0164 | 2025-07-01 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ab9a6755-f9a8-33ce-a405-3b926c3a1f75 | -10.883 | -56.4567 | 2025-07-01 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| b0034d3c-e986-3180-87af-9353b4f6d58f | -6.4814 | -43.743 | 2025-07-01 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 0c402f35-6a95-3cbe-bde4-babfe8cbe3b8 | -10.1395 | -52.3392 | 2025-07-01 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 180.7 |
| b17bf7ee-e382-36dd-9ec5-f7149a6543c1 | -6.4816 | -43.7198 | 2025-07-01 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 310e6e81-83e7-35e2-8071-061f705f8ce4 | -6.2945 | -43.6659 | 2025-07-01 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 58a8df80-ea7c-38e8-9a1c-d31b183ef5f9 | -9.6507 | -50.7469 | 2025-07-01 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fa0a1960-be3e-348c-9941-ea190b57f87b | -10.883 | -56.4567 | 2025-07-01 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 82b43ded-9ed9-3be9-9564-b7800b3e7ab4 | -7.6051 | -45.7464 | 2025-07-01 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5ed7df0d-65dd-3010-97cc-d12ce15f8acd | -6.2943 | -43.6891 | 2025-07-01 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| d39be37d-0973-3401-99c8-9d5b21959ee9 | -9.9847 | -48.2378 | 2025-07-01 00:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 34c04e49-9984-3c95-bcdc-57bca52d52d8 | -12.6319 | -54.2087 | 2025-07-01 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 870238b2-20bd-3b1f-a7e7-86f945770748 | -6.2945 | -43.6659 | 2025-07-01 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| cbd37c8e-dee0-3aa6-9bc3-342816cfe902 | -10.1205 | -52.3618 | 2025-07-01 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 43b3ff7a-53a5-3d5a-9b08-fdb728e59dd0 | -10.1393 | -52.3601 | 2025-07-01 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3e9e51a2-c054-322c-a533-3ef02a858861 | -4.3197 | -48.0908 | 2025-07-01 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 37050b87-4e5e-3d03-8455-21c6ab157a52 | -6.2755 | -43.6907 | 2025-07-01 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 87c185bc-f8c0-391f-90fb-ccefb883c13b | -10.1207 | -52.3409 | 2025-07-01 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 8bac24d5-6c11-30d8-bfe3-dbfa098ea21a | -10.0784 | -52.7393 | 2025-07-01 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7beb68ea-34da-3d82-a19e-d4b688432f11 | -7.6239 | -45.7447 | 2025-07-01 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 826489dc-1e40-36d9-a2c4-825ba3217a50 | -6.4814 | -43.743 | 2025-07-01 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| abdaa2be-7807-3032-bb89-97b63b47949b | -10.8832 | -56.4367 | 2025-07-01 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 54946916-0988-3991-a3cf-70890f78e9b4 | -7.2217 | -43.0917 | 2025-07-01 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 1a2baf85-1aa0-31ae-9efd-c60cf147eef2 | -10.1395 | -52.3392 | 2025-07-01 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 078e8022-140d-3d1d-8f3b-da5adeec23fb | -6.4626 | -43.7446 | 2025-07-01 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c7e66b18-cad3-3018-979f-8339eed1575a | -6.2945 | -43.6659 | 2025-07-01 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0d4b8b4f-a6b0-30c1-91a6-9843cd212f4f | -7.2217 | -43.0917 | 2025-07-01 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| b49fb5db-bdf9-35ed-a805-008eca62f525 | -10.0784 | -52.7393 | 2025-07-01 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b40aea91-72bc-3451-b5b3-09d61aac268f | -7.7758 | -44.0164 | 2025-07-01 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9e7adf25-af64-379f-9b79-1ee22348ec2a | -10.8644 | -56.4381 | 2025-07-01 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0fb305b6-2f2d-30ea-9ea2-eceb893b322a | -7.6239 | -45.7447 | 2025-07-01 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f58d863e-2e12-3504-ae3b-baa0a299fc0d | -10.1395 | -52.3392 | 2025-07-01 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 911cb7f0-03fb-370f-8f75-2e446217e82b | -10.1205 | -52.3618 | 2025-07-01 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 239cd485-ded2-31c1-86c5-d4406bdc050b | -7.6051 | -45.7464 | 2025-07-01 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 46d455b1-6efd-3442-bae6-2e3be3e2e14c | -6.2224 | -43.3693 | 2025-07-01 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d7efb6f8-a5ff-36b6-b205-ef4c67176c81 | -9.9847 | -48.2378 | 2025-07-01 00:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e2802b02-078a-300f-abde-125f24cda228 | -7.2028 | -43.0936 | 2025-07-01 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 66283926-e566-3d9a-842e-1ae2963b869e | -10.883 | -56.4567 | 2025-07-01 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 60c2ff11-7848-3eda-b772-910b8e3b571b | -10.8642 | -56.4582 | 2025-07-01 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7ef1b6db-97b7-389e-8012-f670b8684238 | -10.8832 | -56.4367 | 2025-07-01 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| f7a60440-c7a2-3380-9c94-d95b634a95cb | -6.2226 | -43.3459 | 2025-07-01 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 071b404b-7313-38e4-8e9d-df9d90a7fcf7 | -6.2943 | -43.6891 | 2025-07-01 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| a3fd4d50-4c9c-3765-a6d6-90d18cd206a2 | -6.4814 | -43.743 | 2025-07-01 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |


[Clique aqui para ver as próximas entradas](README2.md)
