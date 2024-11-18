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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 694a6a18-be09-3a01-883f-23533a19c423 | -6.522 | -35.1666 | 2024-11-18 01:00:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 5c335198-4f40-3e9c-b46f-5de3afcf3fdb | -2.8791 | -51.7932 | 2024-11-18 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| b0bff0a8-3717-3402-a717-3136fbbf34ef | -3.5678 | -50.2534 | 2024-11-18 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| cbab4be2-c6d3-3bee-b7b2-1f3566cf4f1c | -14.286 | -57.624 | 2024-11-18 01:00:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 760dfa9c-668b-33a0-bda4-012e0480b0fd | -2.8607 | -51.7937 | 2024-11-18 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 3c7e759b-807a-3f8e-83a8-63b04e1f4889 | -1.2964 | -51.7616 | 2024-11-18 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 1751fa57-03c9-3340-9237-6c3923fb122c | -2.5846 | -51.7387 | 2024-11-18 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 241b82f4-d6ad-336b-926b-d56868c358a2 | -1.7147 | -45.8307 | 2024-11-18 01:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 119.3 |
| ee8321b7-cc6f-35a3-8b90-ba3a27dd9943 | -14.2857 | -57.6442 | 2024-11-18 01:00:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7a59e57c-75c9-3587-af3b-68eb6c853376 | -1.7324 | -46.1862 | 2024-11-18 01:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a30fb928-166a-388f-b110-d5b6e5daea09 | -3.775 | -45.9413 | 2024-11-18 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 139.4 |
| fa4de846-cfc0-3e06-b324-a1007c3fdfc2 | -1.3148 | -51.7408 | 2024-11-18 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 321.3 |
| 1d6eb65f-5d9c-34ae-89e7-e6a241451f2a | -1.6962 | -45.8311 | 2024-11-18 01:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 167.3 |
| c66260ff-bd41-3193-bc48-3d430b9ec49b | -2.5073 | -47.2461 | 2024-11-18 01:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| f1f59f89-869b-34d6-ad91-c2e2be9d244e | -1.3148 | -51.7202 | 2024-11-18 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| d8a9be38-0667-3b49-a127-b7a4a9ead8c6 | -2.5846 | -51.7387 | 2024-11-18 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7d4710a1-dceb-35f5-b266-2af1714b0892 | -6.5407 | -35.1917 | 2024-11-18 01:10:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| a3dcee10-676e-3b99-9ed5-3bc04214e53b | -2.5847 | -51.7181 | 2024-11-18 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| cd6a955c-e18a-3bd5-84d8-44bb613e8800 | -1.7138 | -46.1866 | 2024-11-18 01:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ef3d2a82-7bce-3062-9309-dc42e3d97ed0 | -3.3267 | -50.4923 | 2024-11-18 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 603faa41-6b86-3304-b690-127964f78730 | -1.3148 | -51.7614 | 2024-11-18 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 36907428-d907-3469-ab5d-1bf195752896 | -2.8792 | -51.7726 | 2024-11-18 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 883a8ede-6bb2-3bd6-9c06-40ae240b039e | -3.7564 | -45.9422 | 2024-11-18 01:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ec21a407-a81b-3010-9bb8-e17f7b33d71d | -3.6593 | -50.439 | 2024-11-18 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 682e991d-b9aa-3ca3-a7aa-5f9a100e2317 | -1.6962 | -45.8087 | 2024-11-18 01:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| fbd50799-f7ed-32a5-a934-368a42e5cd9b | -3.775 | -45.9413 | 2024-11-18 01:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 04125ea3-20a1-3597-909b-05ca021b1dac | -2.8607 | -51.7937 | 2024-11-18 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| d60ffe50-d699-37a7-8b14-95d61bb3c28a | -2.5074 | -47.2242 | 2024-11-18 01:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1173bd4d-cd03-328d-af8e-c158df53406a | -1.2964 | -51.7616 | 2024-11-18 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 42d1703c-822b-3f6d-ab74-2bc9bb41642b | -3.6778 | -50.4384 | 2024-11-18 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 0afa13ad-0cb5-3fc2-8a26-d0f827395f26 | -2.7659 | -52.6163 | 2024-11-18 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 039dbef5-f286-3cf5-8b1f-5016cfe31518 | -2.8608 | -51.7731 | 2024-11-18 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 2a3d7f58-a443-3d5f-bbeb-3ef24912b360 | -3.5678 | -50.2534 | 2024-11-18 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 27a67510-f3f4-3bc9-971c-c04b26a19772 | -3.3452 | -50.4917 | 2024-11-18 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4d7967e5-9c94-3fc4-ab27-fef2222bef56 | -1.7147 | -45.8307 | 2024-11-18 01:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 09ff930f-b540-38be-83e8-b0428522c6c0 | -1.2964 | -51.7204 | 2024-11-18 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 3674a7de-1d6e-3406-b75b-d0eedf8cc1f0 | -3.0542 | -54.4081 | 2024-11-18 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a5f0b60f-d5dd-3c44-ab63-81809baf40ba | -14.286 | -57.624 | 2024-11-18 01:10:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 67a6d440-272b-3cfa-9b5d-bbefe9bf1ef2 | -6.5216 | -35.194 | 2024-11-18 01:10:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| 8b0e5f8c-8959-36d8-b143-4e5f325feb94 | -3.0764 | -53.2796 | 2024-11-18 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ba99ffbb-db80-3535-a46f-de6f18643122 | -1.2964 | -51.741 | 2024-11-18 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 370.4 |
| 82eb6997-eacc-32d2-b9db-eb4efa72909d | -14.2857 | -57.6442 | 2024-11-18 01:10:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6b4bab40-f8c5-331d-aa8e-ab7ffee4b69e | -2.8791 | -51.7932 | 2024-11-18 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 6a9dac64-efff-3ff7-b02d-665b50c28c32 | -2.5847 | -51.7181 | 2024-11-18 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| cbc33e75-034d-3806-b9f8-e06de3899546 | -6.5407 | -35.1917 | 2024-11-18 01:20:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| cbb0c498-56f7-3a94-bb88-e55ab3faa60c | -1.3148 | -51.7408 | 2024-11-18 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 367.5 |
| f1cb5730-137d-3797-b795-28d829860c69 | -1.2964 | -51.741 | 2024-11-18 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 319.0 |
| b74034c2-7ab8-3272-a736-4f2ed7c072c4 | -2.8792 | -51.7726 | 2024-11-18 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c1f80f92-6289-35c5-8641-662f5cc01e0a | -5.5292 | -43.3071 | 2024-11-18 01:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 35a39182-e9cf-3e7f-8d41-e40b90bcb6a2 | -2.8607 | -51.7937 | 2024-11-18 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 3495ca9e-1236-32bd-92e3-76905e78c99b | -3.6593 | -50.439 | 2024-11-18 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6070bad5-42a0-3cd5-92db-60f807ba97c1 | -3.3452 | -50.4917 | 2024-11-18 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3989dfc8-08e2-329f-bc9f-10568da411da | -3.5678 | -50.2534 | 2024-11-18 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 5550bd35-5747-3336-a881-73e0615ba107 | -14.2857 | -57.6442 | 2024-11-18 01:20:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 34a9c8d1-757c-3047-a972-0c84e5bc40ce | -5.5479 | -43.3057 | 2024-11-18 01:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 91693287-e625-3930-ae8e-0b8d4c028040 | -1.3148 | -51.7614 | 2024-11-18 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| fc2cd142-b3cd-39b4-aa32-c840a5cfc510 | -2.5074 | -47.2242 | 2024-11-18 01:20:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| ad74a9db-3ea8-3279-9074-e7b4fc3f587c | -1.7147 | -45.8307 | 2024-11-18 01:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 136.4 |
| eb7e6aa0-690d-3e7d-b44a-beac5c388439 | -3.775 | -45.9413 | 2024-11-18 01:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| aa34cd1e-edd0-3986-8994-e76743ea5206 | -1.6962 | -45.8311 | 2024-11-18 01:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 5d7b53e5-fac8-3c4b-a2ef-82a89dc70077 | -3.0542 | -54.4081 | 2024-11-18 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| abf6de06-ea29-3e78-88d0-10de32c014ab | -14.286 | -57.624 | 2024-11-18 01:20:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e9552153-67e7-3df8-815e-0152e0a3c9e0 | -3.3267 | -50.4923 | 2024-11-18 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7b0e1c79-38b5-37e8-87b5-615f82d9be95 | -1.2964 | -51.7616 | 2024-11-18 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 32c14486-b113-3d0c-8f04-499081abd4f3 | 0.966 | -51.1452 | 2024-11-18 01:20:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 61.5 |
| fd302beb-72d9-3e63-a84f-295d00742cf6 | -2.7659 | -52.6163 | 2024-11-18 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 98c984b1-ce51-3273-862e-dd74a631104b | -6.5216 | -35.194 | 2024-11-18 01:20:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 607b836a-1de6-3a5b-b43d-9aa464737850 | -1.2964 | -51.7204 | 2024-11-18 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 0d610f6c-5428-34bb-9fbd-3477f93904ac | -2.8608 | -51.7731 | 2024-11-18 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 19f9dc2f-4a38-3921-a141-b21da438d0af | -2.5073 | -47.2461 | 2024-11-18 01:20:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 100f628a-5622-321b-819b-cfdb9e42c667 | -1.6962 | -45.8087 | 2024-11-18 01:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6baebd1d-8a05-3597-acec-5030cb5c4d9c | -5.5481 | -43.2824 | 2024-11-18 01:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1ff576ce-2e55-37f9-8820-8e7d6d456454 | -2.8791 | -51.7932 | 2024-11-18 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 19f22dd0-61de-38d9-9baf-7438c1cdf951 | -1.3148 | -51.7202 | 2024-11-18 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 7907f10c-8b1e-33e6-9bab-a3169e1b5c13 | -6.5407 | -35.1917 | 2024-11-18 01:30:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| 2613ea16-1cb2-360b-8022-759ab0f1d48e | -2.8791 | -51.7932 | 2024-11-18 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 840f499b-8688-340e-b8eb-b893238f5c47 | -2.8792 | -51.7726 | 2024-11-18 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 881d51b6-14ea-3c42-8cd0-33901ff52684 | -2.5258 | -47.2455 | 2024-11-18 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 907a0836-b013-310b-b034-a1a5f86cfb84 | -10.0799 | -36.5294 | 2024-11-18 01:30:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 919cecfd-dcaf-3cc2-8851-f2b316efdbae | -6.522 | -35.1666 | 2024-11-18 01:30:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 131.9 |
| b812dcbf-a943-30b3-92d8-7d80f17b321b | -2.5072 | -47.2679 | 2024-11-18 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| b8a2d9a7-30bc-30e4-b75e-04f507be58a4 | -2.4889 | -47.2247 | 2024-11-18 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e40400a9-146f-3825-a4f1-9cf5a617bfaa | -2.5847 | -51.7181 | 2024-11-18 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d799a702-b828-34a1-9617-1ceb291ac74b | 0.966 | -51.1452 | 2024-11-18 01:30:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ad6115a5-6743-354a-9189-2084ce82c103 | -6.5411 | -35.1643 | 2024-11-18 01:30:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| f7de4b8c-72e5-3d73-b211-07a4bb8a0c9d | -1.2964 | -51.741 | 2024-11-18 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 271.5 |
| 0c4fb6ce-d2f3-3e26-b1d7-3926c1fd636a | -2.8608 | -51.7731 | 2024-11-18 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 07d3dcd6-1268-382b-9e69-0b789b7d153b | -1.3148 | -51.7614 | 2024-11-18 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 51e3c69f-882d-3dbe-9e29-f7f061d93ec8 | -1.2964 | -51.7616 | 2024-11-18 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 51dba49f-e020-3ad5-9917-6b590b240f46 | -3.3452 | -50.4917 | 2024-11-18 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3588fd86-38d4-302e-abda-7d30eec4fcff | -2.5073 | -47.2461 | 2024-11-18 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 478.8 |
| 6a0f12f4-48af-37a7-8baa-169248d9ce8d | -3.0542 | -54.4081 | 2024-11-18 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 752ff1c0-21a5-3d0d-8464-b2e95753878b | -2.8607 | -51.7937 | 2024-11-18 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 6f08aca6-748f-3b29-9c62-e9f293af95c7 | -2.4888 | -47.2466 | 2024-11-18 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| e4635855-a49f-3be5-956e-409b9e395bf7 | -14.286 | -57.624 | 2024-11-18 01:30:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c75d4f2e-9e58-3048-9683-6f9b5161c25e | -1.3148 | -51.7408 | 2024-11-18 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 293.6 |
| 0fedd991-527c-3d4c-a87f-bf59070cd618 | -2.5074 | -47.2242 | 2024-11-18 01:30:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 235.1 |
| 5a2065e0-fe54-37da-838b-c3b359354d57 | -3.6593 | -50.439 | 2024-11-18 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c074f258-ec83-3da3-93f5-f92c1a05db45 | -14.2857 | -57.6442 | 2024-11-18 01:30:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5d1770d3-c5df-3fe9-b8c2-0cce76927b9e | -1.2964 | -51.7204 | 2024-11-18 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |


[Clique aqui para ver as próximas entradas](README11.md)
