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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55ddd93b-2e99-305b-8675-727ff74479fe | -8.5211 | -43.3063 | 2025-08-14 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2e3344cc-9246-3385-93ba-5798f6021a6d | -9.1522 | -59.6578 | 2025-08-14 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 77b43952-3305-3f1b-8884-d082a2255572 | -7.8775 | -61.8063 | 2025-08-14 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 9d65548f-5d6d-30c6-bf79-908de8e4e599 | -6.0991 | -59.9459 | 2025-08-14 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 63b82d43-f243-3427-a5b1-5bf29e1ddb9b | -6.8956 | -59.1462 | 2025-08-14 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 208.1 |
| e779f49b-4c00-3f4f-a078-2dd28c73b8eb | -6.8771 | -59.147 | 2025-08-14 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 001d0add-7b9f-3c67-a264-76f487b4dea8 | -6.9139 | -59.1648 | 2025-08-14 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f67e33f1-ac47-35e8-99ee-01b36bfdeaaa | -7.8775 | -61.8063 | 2025-08-14 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9639a398-05e5-3c69-b177-8a838c87b84c | -6.914 | -59.1455 | 2025-08-14 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 27dfee8c-165c-3501-b3ea-f68a0a5d7765 | -22.6774 | -47.4407 | 2025-08-14 02:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 93855bb2-3a99-3ce8-8775-2e9507a66044 | -17.0629 | -51.7984 | 2025-08-14 02:40:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| fedf2d7c-45b1-3268-9953-9ac33103eb51 | -9.1522 | -59.6578 | 2025-08-14 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6dbebc86-9ccc-3683-acef-4cddb56ab7b9 | -6.877 | -59.1663 | 2025-08-14 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 5c1cedb5-3754-3318-b849-f4ec03af8593 | -8.5211 | -43.3063 | 2025-08-14 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| aa3f6c14-09cd-3b34-a5c4-3f7b87e56f06 | -6.0991 | -59.9459 | 2025-08-14 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ba80d539-eca0-385f-b875-27cd278bf408 | -6.0807 | -59.9465 | 2025-08-14 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 95b081c7-3378-3711-a890-6103b1b58518 | -6.8955 | -59.1655 | 2025-08-14 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.5 |
| ef8216e1-e0c3-3729-b531-a408bc00612a | -8.5208 | -43.3298 | 2025-08-14 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 58151cbf-8b2b-3107-a4cb-f73539561e22 | -7.8774 | -61.8253 | 2025-08-14 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 19675a8b-1635-34d7-86da-001a86633d77 | -7.6103 | -63.516 | 2025-08-14 02:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 580632cc-1751-3d20-9f46-8665d40b61f0 | -2.9106 | -48.2971 | 2025-08-14 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 18574ea1-f913-3d57-bfc8-3db2412abffc | -22.6767 | -47.4647 | 2025-08-14 02:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 8da8405d-8071-3ccf-b5e1-c49ffc6b991e | -16.3153 | -52.9201 | 2025-08-14 02:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 12fe7ae1-0c2a-3847-b32c-fa78265d5df7 | -16.3153 | -52.9201 | 2025-08-14 02:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 51d8121b-a116-32b5-8399-fae96a0aa583 | -7.8774 | -61.8253 | 2025-08-14 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4fc03474-6106-3519-9fb1-b610b4a593c4 | -6.0991 | -59.9459 | 2025-08-14 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a7cccb97-5cdd-3df8-b513-716ccc2f9620 | -22.6774 | -47.4407 | 2025-08-14 02:50:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 44.1 |
| a40419bb-b237-3450-a2ab-d45a7aad1e70 | -17.0629 | -51.7984 | 2025-08-14 02:50:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 709630fa-8683-363e-a021-a6c9b4c26938 | -8.5208 | -43.3298 | 2025-08-14 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| ee638a0e-1534-3ace-a334-c37ca09de1e8 | -6.0807 | -59.9465 | 2025-08-14 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 60d29669-8a74-35bb-854f-cf055b943cab | -8.5211 | -43.3063 | 2025-08-14 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 4019e595-6d83-3a22-9e17-16e5fd20ffa6 | -9.1522 | -59.6578 | 2025-08-14 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 323d1c86-6b6e-3056-b70b-00098e43e3af | -7.8775 | -61.8063 | 2025-08-14 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d5251181-701f-385f-90f8-9c99535869bd | -9.553 | -40.3503 | 2025-08-14 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 118.6 |
| 7bbdfd25-40ae-3b21-8a47-bc314666461e | -22.6767 | -47.4647 | 2025-08-14 03:00:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 49.5 |
| e41d2cde-32ff-380a-9a26-839d2e846db4 | -23.5558 | -51.619 | 2025-08-14 03:00:00 | GOES-19 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| b7cb221b-1861-3f20-86bc-e81a4c6fc4c5 | -6.0807 | -59.9465 | 2025-08-14 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 85ca9512-d102-30d3-a3e6-11ca1217c3bc | -17.0432 | -51.8016 | 2025-08-14 03:00:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 22b69b06-bc0c-30a3-9159-025fd521d0de | -9.5721 | -40.3475 | 2025-08-14 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 10825870-2f9e-3ea2-8fbf-ca760d38ed6c | -9.1336 | -59.6588 | 2025-08-14 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 85d37279-52d6-33e8-b0f5-263218316998 | -22.6774 | -47.4407 | 2025-08-14 03:00:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 26e67102-8c49-302d-b1ee-af2cf59a9ecd | -6.0991 | -59.9459 | 2025-08-14 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 4ac2fa5f-b57c-35b5-8f2c-ed2cbdc885c6 | -7.6103 | -63.516 | 2025-08-14 03:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| d5437f57-f872-3ec6-b530-a1fa1256aef7 | -7.8774 | -61.8253 | 2025-08-14 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d1022667-ed82-3cb8-8507-9497a484e56b | -9.1522 | -59.6578 | 2025-08-14 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 344dcb07-5ab9-3087-8f4a-7a2d4259db1f | -5.374 | -36.8531 | 2025-08-14 03:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fdd3730a-6468-3214-a93d-bdfb6dd05de1 | -5.47218 | -36.79115 | 2025-08-14 03:06:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 91b5770e-bbf7-3a21-92e7-32fd0b504cdf | -5.37818 | -36.84969 | 2025-08-14 03:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d32caf5a-d314-3cd6-a659-e642b5e23fb3 | -5.47304 | -36.78632 | 2025-08-14 03:06:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2b7069d4-49f9-33dd-ab07-6dc058b824ba | -5.37195 | -36.84855 | 2025-08-14 03:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 36d364b1-33db-3111-ba9e-d6f6ec7b4a21 | -5.37486 | -36.84823 | 2025-08-14 03:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0bd982ae-3fee-30f9-aaf5-6b62805cd80e | -5.37728 | -36.85458 | 2025-08-14 03:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9180d68f-fe49-3388-9c6b-89dc7ef7ebb0 | -9.32909 | -37.98411 | 2025-08-14 03:08:00 | NPP-375D | PARICONHA | ALAGOAS | Brasil | 2706422 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f5fec045-c26c-3099-ae14-5eb2ac78592e | -9.55842 | -40.34361 | 2025-08-14 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.3 |
| b3a919dd-8e13-330b-b560-deb02ba2d88d | -9.56409 | -40.3523 | 2025-08-14 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 6bcf19b6-e016-3d61-a814-be7dc32c3a85 | -9.55549 | -40.35799 | 2025-08-14 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| f3df16fa-82da-3e8b-af83-ba5669c93ba9 | -9.55696 | -40.35079 | 2025-08-14 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 79bffc23-85f0-35ea-9fe8-3d14949fb7f6 | -9.56555 | -40.34512 | 2025-08-14 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 60904ba4-04e9-3cd9-b3e8-9a016e9bfad8 | -7.8775 | -61.8063 | 2025-08-14 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 46fcb5c4-f392-3f77-b755-09912065af83 | -9.1336 | -59.6588 | 2025-08-14 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| fe02e121-7378-3bfe-ba7a-48bd8a541d7b | -7.8774 | -61.8253 | 2025-08-14 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f0abe37d-b479-36cf-a443-0b44efe7b078 | -6.0991 | -59.9459 | 2025-08-14 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5f084424-57b7-31e7-b47a-516aa0ee7b03 | -6.0807 | -59.9465 | 2025-08-14 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1485bd1e-53bb-31b0-a476-fad58de4cf49 | -9.1337 | -59.6394 | 2025-08-14 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 44724976-68b1-36c8-8a82-8a9c2e52bcdd | -9.1522 | -59.6578 | 2025-08-14 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 859ec82b-f2b7-39c0-b776-7a7cee0f5ecb | -8.5211 | -43.3063 | 2025-08-14 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| e9f1ca63-e1ff-3433-9e30-1e13076e3cf1 | -21.22778 | -42.5723 | 2025-08-14 03:10:00 | NPP-375D | SANTANA DE CATAGUASES | MINAS GERAIS | Brasil | 3158409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ac4aa816-0a2c-38b7-86f7-3f6bdc9b2681 | -21.22912 | -42.56677 | 2025-08-14 03:10:00 | NPP-375D | SANTANA DE CATAGUASES | MINAS GERAIS | Brasil | 3158409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9793b80c-e5b3-3191-8cbe-7c9f15c82dbe | -18.72666 | -39.8713 | 2025-08-14 03:10:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9a5f9160-5adf-3ecb-b3c8-3bcbfaa09f40 | -19.06511 | -42.93081 | 2025-08-14 03:10:00 | NPP-375D | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0be91414-7fad-3fe2-812f-bd7e643fcbd3 | -6.8771 | -59.147 | 2025-08-14 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 42a2b9fb-2916-39a5-bc87-290fdc93c50c | -9.1336 | -59.6588 | 2025-08-14 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 0f097783-68a0-328a-b288-4e424d3265fa | -9.553 | -40.3503 | 2025-08-14 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 646e3033-f31f-3cbf-a365-304604bf255a | -6.914 | -59.1455 | 2025-08-14 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 47564caf-7345-3331-8bef-bc8d3cc56ffe | -9.1522 | -59.6578 | 2025-08-14 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cd476a19-79be-3546-8e90-ad070ba00287 | -6.8956 | -59.1462 | 2025-08-14 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 71d45b34-bd12-3601-a418-e04fcdeff6e4 | -21.2308 | -48.805 | 2025-08-14 03:20:00 | GOES-19 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.0 |
| 276cc21e-a318-39f7-9391-ee86024d91dd | -7.8774 | -61.8253 | 2025-08-14 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a52e38c4-cba8-399b-96e8-2232f51ada67 | -6.877 | -59.1663 | 2025-08-14 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| fa29dc1f-ce3a-378b-894f-54b480cdb2f1 | -6.0991 | -59.9459 | 2025-08-14 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| bb7e1fc4-082f-30e1-9c04-8e2a16c514a3 | -6.9139 | -59.1648 | 2025-08-14 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6b99daab-c3a9-38c7-b9d7-5b9a54d77a95 | -6.0807 | -59.9465 | 2025-08-14 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a5a3bdb9-9dff-392e-b6c6-a08c7d818f0e | -6.8955 | -59.1655 | 2025-08-14 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| ae3293cd-23bb-3c71-8c88-4585a639803f | -9.1337 | -59.6394 | 2025-08-14 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f7bc19e8-5c95-3fb5-9c86-7e718565bcf7 | -9.5721 | -40.3475 | 2025-08-14 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.4 |
| f832f025-c17b-302d-b979-375025a0286f | -5.78788 | -43.61617 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e11853cb-dfca-30c2-9d98-73a164e36ab2 | -3.8192 | -41.57734 | 2025-08-14 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef76fb10-ea50-3c47-8e65-35b050b9cbf3 | -5.68035 | -43.65367 | 2025-08-14 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17225c79-843f-3a25-ba8a-6b3eb4f2a51b | -6.18332 | -43.31783 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bca40dd0-9077-338c-8c05-4a051dfaab58 | -7.07148 | -39.46724 | 2025-08-14 03:28:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33c2eac4-7f51-3b63-befe-1a8f05d5e011 | -6.61466 | -43.89037 | 2025-08-14 03:28:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 85f10d61-22c4-3fae-838f-cd787113861d | -5.7834 | -43.60545 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6840e9e0-c8e4-3e7a-aad7-965af092ea69 | -6.18942 | -43.31884 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ace1b414-2c17-3ff9-a590-223c94b87ee6 | -4.4508 | -38.44657 | 2025-08-14 03:28:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89998711-e597-3322-b701-9627bddf8e7d | -5.88368 | -43.92762 | 2025-08-14 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dbdc2ad-407a-3cca-b003-3ff49e7ec264 | -5.37503 | -36.84436 | 2025-08-14 03:28:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c7ade00-bd45-3802-a878-effa335659c0 | -4.17022 | -42.45622 | 2025-08-14 03:28:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf258f85-ce48-3463-8b49-d2691093f0ce | -6.61653 | -43.88029 | 2025-08-14 03:28:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dd3bd4c9-ae48-3dbc-8496-438e600e51e2 | -4.58887 | -43.31328 | 2025-08-14 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b35d957-5621-356c-8009-e948eeae62f9 | -6.17877 | -43.31107 | 2025-08-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README9.md)
