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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7cc5f34-ab94-31cf-8c8d-d6c16c4330dd | -4.7204 | -46.4497 | 2025-11-13 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 86c36625-6e97-36c6-99cb-e4b0285cb818 | -18.7578 | -50.4972 | 2025-11-13 01:50:00 | GOES-19 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| 1c2bd863-0978-37c2-9903-ba4e166fffcf | -9.4387 | -40.3419 | 2025-11-13 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.2 |
| cba8a9c0-6ef6-351b-8a31-89ed936661a6 | -3.0731 | -49.2765 | 2025-11-13 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 83a4ff18-96f6-3843-906e-643f72217f22 | -9.4383 | -40.3668 | 2025-11-13 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 126.2 |
| fbe9edef-6268-30d7-a1ea-b147d0833af9 | -18.7583 | -50.4749 | 2025-11-13 01:50:00 | GOES-19 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| a3bee34d-98c0-3046-959f-60fefb091698 | -3.7981 | -45.1548 | 2025-11-13 01:50:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 582fb4dc-f59f-345a-8432-eb893e4e2f38 | -4.702 | -46.4286 | 2025-11-13 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a2c8a500-d9aa-399b-90f1-2c19cbb93538 | -4.7018 | -46.4508 | 2025-11-13 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9b638d6a-e85d-356f-9e18-f02f27e18940 | -3.0916 | -49.2759 | 2025-11-13 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| c009a427-cf17-3c17-bb5c-5be701b3b5da | -9.4192 | -40.3695 | 2025-11-13 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 188.3 |
| 0cac2f99-835a-35dc-bc9f-3d252483a1e0 | -4.7206 | -46.4276 | 2025-11-13 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c12139d8-ed51-33c7-ae7d-3c03655736d4 | -3.8659 | -49.7786 | 2025-11-13 01:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| cd62c82b-f428-3368-a8dc-a5de6017d9f2 | -12.6364 | -46.7435 | 2025-11-13 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c51f4904-3b54-3568-a5b5-22be6a3f09c8 | -9.4196 | -40.3447 | 2025-11-13 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 6d8fe488-dcd4-3f98-ab0e-d8bd157d7ee4 | -5.3262 | -45.2041 | 2025-11-13 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a742fdb3-0e8c-394f-89e8-52c5d3718262 | -4.7204 | -46.4497 | 2025-11-13 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 114.8 |
| e04b7577-83e0-3f01-bd52-e80d7da65470 | -3.0916 | -49.2759 | 2025-11-13 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| a800b37c-ebe2-37ed-8f2a-7ff019ff8760 | -3.8658 | -49.7998 | 2025-11-13 02:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 24089d4e-fbf7-3f46-affd-16e4dc880737 | -3.2378 | -45.5839 | 2025-11-13 02:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 254a04c8-acf4-3f81-a0b0-6e12a7383c94 | -4.7018 | -46.4508 | 2025-11-13 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 810ea3dc-9c5e-3317-95c7-0ff52ce8d4cf | -9.4192 | -40.3695 | 2025-11-13 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 4f7b2b92-2cb6-3b61-b0f6-a66652eddc24 | -12.6557 | -46.7407 | 2025-11-13 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| dbac0fb1-35db-3789-a8bf-f9f509188a1a | -4.7206 | -46.4276 | 2025-11-13 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| db1da5b2-2848-3512-8e01-d6fa93caef13 | -3.2378 | -45.5839 | 2025-11-13 02:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 70b9f7df-d48c-3c66-a5dc-e3bd5ab1a7d4 | -4.702 | -46.4286 | 2025-11-13 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 824dd423-74f9-3586-a132-325aeee9d18e | -4.5344 | -46.4376 | 2025-11-13 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 11b6d113-5ef9-3791-a79a-70c6b5458198 | -6.9226 | -35.1441 | 2025-11-13 02:10:00 | GOES-19 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| e9deafe1-09a1-3918-811a-0f41065b14c7 | -4.7204 | -46.4497 | 2025-11-13 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 5996cc65-0cba-3f52-a368-a4b142c51b07 | -3.0916 | -49.2759 | 2025-11-13 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 098323e0-5415-3f42-aa7d-43438b647e57 | -4.7018 | -46.4508 | 2025-11-13 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 527dbd5f-e40e-3ab6-a6f3-cbb193ee24f1 | -3.8659 | -49.7786 | 2025-11-13 02:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| f7714e21-15c9-3041-9444-395406c22719 | -4.7206 | -46.4276 | 2025-11-13 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 5484add5-f29c-3564-8679-e2a6ae980e7f | -3.8658 | -49.7998 | 2025-11-13 02:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ca57018b-f34b-3174-a546-b8476fe1f41e | -3.2192 | -45.5846 | 2025-11-13 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 594d43fb-f3a9-3083-a5a4-9afda2556704 | -12.6557 | -46.7407 | 2025-11-13 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 790c22a9-b360-3ebb-bda5-9720e2414c4a | -9.4192 | -40.3695 | 2025-11-13 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 160.8 |
| 7af493bb-5b4d-34b3-87a4-e2276c23a781 | -9.4196 | -40.3447 | 2025-11-13 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 158.1 |
| dcc04181-c208-30ae-9036-bac9d082b9e2 | -3.2192 | -45.5846 | 2025-11-13 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a98b0e9d-6239-34e0-96e8-9e3276e45edd | -4.5344 | -46.4376 | 2025-11-13 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6a64f92e-181f-32a4-8969-e96da36b84cc | -4.7206 | -46.4276 | 2025-11-13 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2eee610c-d1c9-3958-bb67-3cf0d4e07303 | -3.0916 | -49.2759 | 2025-11-13 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ca57301b-b33f-3fc5-840f-93606aa307c7 | -4.7204 | -46.4497 | 2025-11-13 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 101.1 |
| c217c841-c8d6-3249-ac2f-69cdc0fae977 | -9.4387 | -40.3419 | 2025-11-13 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 50daee63-2e12-3c14-b4ce-1eb5638989b6 | -9.4383 | -40.3668 | 2025-11-13 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 577bcd4e-5ef6-377a-b4ad-0af3c1c114c6 | -4.7018 | -46.4508 | 2025-11-13 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| fab55220-f9bf-3caa-b74e-333b55023666 | -3.2192 | -45.5846 | 2025-11-13 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 79d339bd-09d7-3256-9001-a43cd474b7dc | -3.2378 | -45.5839 | 2025-11-13 02:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7467d8a2-5994-31eb-8253-c2de5190a723 | -12.6557 | -46.7407 | 2025-11-13 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a89baea4-14a8-3e4d-a3e3-f22eaf0f945f | -3.0916 | -49.2759 | 2025-11-13 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 24991ac2-f09e-32c8-bca7-377a463e299f | -4.7204 | -46.4497 | 2025-11-13 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 1e4e2492-c320-3e3d-b73d-d4236e1c7844 | -12.6364 | -46.7435 | 2025-11-13 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 95a3e84a-6483-3834-9158-e8c436b4cfa2 | -4.7206 | -46.4276 | 2025-11-13 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 046684b9-3d5c-3f9c-99ba-0b035994ad9a | -4.5344 | -46.4376 | 2025-11-13 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| b08d8771-3b28-3a9c-b2eb-324f6cd8c499 | -3.0916 | -49.2759 | 2025-11-13 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fe000aec-6373-3c81-856a-d6227a0515dc | -12.6364 | -46.7435 | 2025-11-13 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| dfedfb01-ba11-3616-892b-7071dd50ef16 | -4.7204 | -46.4497 | 2025-11-13 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 63cf7013-d939-371c-a2c1-85c02c66b80c | -3.2378 | -45.5839 | 2025-11-13 02:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 08257e6b-018e-3370-9c27-c71b22b12328 | -4.7018 | -46.4508 | 2025-11-13 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b4ef3da8-0602-3216-aac3-bc8c382ddad2 | -4.7206 | -46.4276 | 2025-11-13 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4bc64049-1429-3e6c-a8a9-51739fa8616b | -3.2192 | -45.5846 | 2025-11-13 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 22a5b6b9-febe-3f96-a9b0-c00921a3ca5a | -4.5344 | -46.4376 | 2025-11-13 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f1fcf950-c22e-3897-8a57-cbcffa2f49ac | -21.8957 | -56.7489 | 2025-11-13 02:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c49ecf81-8b09-31a3-9b6b-79592071dd0d | -12.6557 | -46.7407 | 2025-11-13 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8ed1bb40-8ea6-324f-9142-1cd1105ed5f9 | -4.7204 | -46.4497 | 2025-11-13 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 5a865192-0c48-3ede-8c14-49eeaeb5ee39 | -4.5344 | -46.4376 | 2025-11-13 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d41c9538-57c1-33bf-9afa-0bb69c116824 | -12.6557 | -46.7407 | 2025-11-13 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7ad67e70-9d33-37a0-8f56-c2d944ad7d9a | -4.7018 | -46.4508 | 2025-11-13 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 45774eec-678a-317e-bb36-41f9796ecf24 | -3.2378 | -45.5839 | 2025-11-13 02:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 729da555-6fa1-3297-bbcd-664442e664ae | -4.7206 | -46.4276 | 2025-11-13 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 36b3d07f-fb4a-32b7-b964-4f98c7136ce1 | -3.0916 | -49.2759 | 2025-11-13 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 07c0162e-55e4-3360-a6b1-d98cf194daa8 | -3.2192 | -45.5846 | 2025-11-13 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c7de6370-5f5d-3cbc-a91c-3cfbb69b8f38 | -6.4845 | -35.1164 | 2025-11-13 03:00:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 108.4 |
| 26fe0fa9-cd29-3c3d-9284-0d68434274e2 | -4.7018 | -46.4508 | 2025-11-13 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0f3ed594-a72a-372e-a1fe-8e50c6c9dc54 | -4.7204 | -46.4497 | 2025-11-13 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 1ea6ce7c-cb62-3615-b353-bd9cf531813c | -4.5344 | -46.4376 | 2025-11-13 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 09d944ad-ce92-30f2-89d2-1200162b5bde | -4.7206 | -46.4276 | 2025-11-13 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6226a74e-6539-3a87-b857-511e90f7251d | -12.6557 | -46.7407 | 2025-11-13 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3926ad38-c549-3c75-b2ff-35f2b3b4e9e1 | -6.5036 | -35.1141 | 2025-11-13 03:00:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| 7bdd3853-9a89-384c-9a5c-12acfa0ee5df | -3.0916 | -49.2759 | 2025-11-13 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f498b489-204c-34f8-9956-e48ce91dfa4f | -3.2378 | -45.5839 | 2025-11-13 03:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6aae0037-e173-37d2-9ab6-770d5887bd4d | -5.60629 | -37.945 | 2025-11-13 03:02:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb7a2027-ad79-3a5c-b59c-d6224eb35342 | -9.9774 | -36.36419 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| 31c4a358-24ea-33aa-97f1-e110e887e7a0 | -5.61199 | -37.94826 | 2025-11-13 03:02:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b2faf581-aca6-337b-9c29-30773c86ed28 | -9.97699 | -36.36019 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 28e1e111-0342-3bd5-b877-622ae2ecb1ed | -5.6135 | -37.94632 | 2025-11-13 03:02:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8d87f02-30e3-3a4d-aa09-5f3fe513a3cb | -6.488 | -35.11905 | 2025-11-13 03:02:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| d0e3f5fe-0872-3200-aa2f-20037cea11c0 | -6.48881 | -35.11464 | 2025-11-13 03:02:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 39.1 |
| 314039d1-a27f-32b1-8d42-341c9a06c054 | -9.98311 | -36.36145 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 90102b66-b99d-3eab-b006-8799ce2893f1 | -6.48717 | -35.12356 | 2025-11-13 03:02:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 521375a3-5148-36b0-81b3-d32570492186 | -6.72661 | -35.05267 | 2025-11-13 03:02:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 25f57bad-7c9a-3207-ab51-df33a09b271d | -6.48198 | -35.11797 | 2025-11-13 03:02:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 279255b5-340e-3308-876f-25981a4a8a4b | -9.9862 | -36.35138 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| c9250c0b-100a-3d4e-8108-2d8d39644e8f | -6.49398 | -35.12034 | 2025-11-13 03:02:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b8a184b4-8091-3d60-b344-ddf68aa95aa3 | -9.9783 | -36.35944 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| 67adb0ce-3d6a-3d9a-9898-aedeeaf7178b | -6.91942 | -35.13623 | 2025-11-13 03:02:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 271b71b7-e435-3070-a6a3-c54ad399c261 | -9.98004 | -36.35036 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| 056c522d-3c3f-3cfe-8091-abf7a333591c | -6.71974 | -35.0565 | 2025-11-13 03:02:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 415e05e4-f6b6-37b6-b415-cde25403e68c | -9.98404 | -36.35674 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 774cf09f-79b1-3e28-a425-a425790795d3 | -9.98495 | -36.35212 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |


[Clique aqui para ver as próximas entradas](README10.md)
