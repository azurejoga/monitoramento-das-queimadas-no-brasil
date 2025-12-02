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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4c3c841-621d-38b5-83b6-79492fc69364 | -3.4901 | -43.592 | 2025-12-02 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8bfb4ded-c1a7-3249-9fc4-a29ea6762dc7 | -11.1379 | -53.9429 | 2025-12-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 6a23de5e-e885-3ec4-98e5-044771861a30 | -4.3892 | -43.1263 | 2025-12-02 01:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 597a5624-07ba-3afc-9ddc-6e4d1466c7e9 | -12.5213 | -56.9022 | 2025-12-02 01:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 73166ec1-e8dd-3142-aebd-f88c6bdd8659 | -11.1193 | -53.9241 | 2025-12-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 638981b7-acba-3d4d-a9a2-a728205915bc | -17.5335 | -57.2107 | 2025-12-02 01:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 5a9e5950-d759-3552-86ae-d5849312c4df | -17.5141 | -57.1925 | 2025-12-02 01:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| f99c25f4-b4b5-39b1-8d78-4b353697f896 | -17.5138 | -57.2131 | 2025-12-02 01:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| af34be11-82e6-30c4-a908-d698478f9f2a | -3.0172 | -45.0748 | 2025-12-02 01:20:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e3c57d59-9680-3158-8e46-97463155edc7 | -8.0513 | -43.1001 | 2025-12-02 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 223.3 |
| cfa7a3cb-1c4e-3bdd-861a-63737df59a28 | -3.4903 | -43.5689 | 2025-12-02 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 97866fe4-4ec2-3821-a689-0d9e26d3f504 | -4.389 | -43.1497 | 2025-12-02 01:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 485018dc-1aa6-3385-bbfb-d99882490c7e | -1.4737 | -45.7907 | 2025-12-02 01:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 6ee69365-02b6-3d39-9ccb-9e31af17182a | -3.0358 | -45.0741 | 2025-12-02 01:20:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 624103fb-64c6-3fb3-b1cf-b1db4e17ddb4 | -8.0703 | -43.0981 | 2025-12-02 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 18c41bc6-07f1-320a-8ba2-e13529a80274 | -19.7672 | -56.688 | 2025-12-02 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 144.1 |
| f7735f84-4144-3c59-a32b-df1d54f4aa64 | -19.7873 | -56.6851 | 2025-12-02 01:30:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 131.2 |
| 52055226-a7b6-3eeb-83c4-f0dc0dcdb561 | -8.0513 | -43.1001 | 2025-12-02 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 267.8 |
| e26d82f0-d0af-3c0f-8330-9586bd16d3cc | -1.4737 | -45.7907 | 2025-12-02 01:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 98b41e4d-4f8f-3263-9c48-477728051648 | -11.1382 | -53.9223 | 2025-12-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f966b593-49e7-39da-8d73-0df1aa2b18d1 | -1.4923 | -45.7903 | 2025-12-02 01:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9edf62e9-0c81-3277-962c-decb5d6ff890 | -8.0324 | -43.1022 | 2025-12-02 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 1d12071f-f4a8-36a1-b91e-8bd0adcc4805 | -4.3892 | -43.1263 | 2025-12-02 01:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| fc6a63c1-9923-39d9-b189-2bd866321194 | -19.7877 | -56.6641 | 2025-12-02 01:30:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| ea0e2e80-66e7-3ce5-9e62-b93ae6330feb | -11.1379 | -53.9429 | 2025-12-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d20d0d70-64cc-333b-9b53-dba9a41724ea | -11.119 | -53.9446 | 2025-12-02 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 53f18475-33ea-33c9-b748-4dfd9f7a0b1e | -21.7552 | -48.4496 | 2025-12-02 01:30:00 | GOES-19 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3c3bd25b-f5f4-3092-bd95-24049ef199a1 | -8.0516 | -43.0765 | 2025-12-02 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 7187aaa6-8ae5-3c69-981e-b160a726584c | -17.5138 | -57.2131 | 2025-12-02 01:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| dbecc0f9-b989-3c4d-bb7b-1c1b03745f71 | -17.5141 | -57.1925 | 2025-12-02 01:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 81dc21be-a0ba-389c-ab11-72fcc87dc5d9 | -3.4901 | -43.592 | 2025-12-02 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 65e044b0-394b-39ce-94ce-7815bed4b715 | -21.7545 | -48.4731 | 2025-12-02 01:30:00 | GOES-19 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c3e85907-1012-3ed2-97cd-667dc2581769 | -4.3703 | -43.1508 | 2025-12-02 01:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d4c1aa13-a10f-3dcd-b946-a2e437b65869 | -8.051 | -43.1237 | 2025-12-02 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 235235bb-aa6f-3f14-982f-d6198c563128 | -17.5335 | -57.2107 | 2025-12-02 01:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 96bcea69-17b8-34ac-94ec-90cd3bd3a6c7 | -4.389 | -43.1497 | 2025-12-02 01:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 60c4bb44-83f5-37be-8b35-b73238f4e589 | -3.4901 | -43.592 | 2025-12-02 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 095b12de-2438-3cc7-b963-699fd1e6e855 | -4.3703 | -43.1508 | 2025-12-02 01:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 72c60fac-4d6b-38a7-b4c2-59020398b97a | -19.7873 | -56.6851 | 2025-12-02 01:40:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 16d4ac1a-df00-3d19-af44-c3187f70ccbf | -17.5141 | -57.1925 | 2025-12-02 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 4916d792-2a08-3084-874e-a4e3004aa063 | -11.119 | -53.9446 | 2025-12-02 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 50efa26c-a804-3db6-bf34-05b618170ea2 | -4.389 | -43.1497 | 2025-12-02 01:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 2d73746b-156b-314d-9d41-1796d5917c16 | -8.0516 | -43.0765 | 2025-12-02 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| ec02ec51-5844-3891-9c8b-7549287b9bc6 | -21.7552 | -48.4496 | 2025-12-02 01:40:00 | GOES-19 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 3b1f2369-1c1e-311b-8dbd-1d687469b904 | -17.5335 | -57.2107 | 2025-12-02 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 01f9a8cf-9ce1-38e1-8098-d2ed680b9c97 | -17.5138 | -57.2131 | 2025-12-02 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 3abb287e-3220-3867-b855-b5ac0efab0fb | -1.4737 | -45.7907 | 2025-12-02 01:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 81b57ef8-d040-3a78-9cd5-c2e81f346e6a | -11.1379 | -53.9429 | 2025-12-02 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 3b2d76ba-e003-3b0c-b8d6-1710616e6a8b | -8.0324 | -43.1022 | 2025-12-02 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 0d4476e5-a5ef-32fe-9024-c6c9271e3236 | -8.0513 | -43.1001 | 2025-12-02 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 325.1 |
| 80753e62-56d8-30c7-b1ed-0ee41395dbde | -11.1382 | -53.9223 | 2025-12-02 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b1acbe0b-5751-3505-ba31-920b87aa5c7a | -8.0703 | -43.0981 | 2025-12-02 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| bf7af0dc-8d59-37ca-9459-d3d93863da3d | -8.051 | -43.1237 | 2025-12-02 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| c1457265-10d3-36cd-8220-adc3d29bf076 | -1.4923 | -45.7903 | 2025-12-02 01:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e7a88980-faea-3fd1-8798-f966b8d16e9f | -17.5138 | -57.2131 | 2025-12-02 01:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 547cfa8f-a243-365f-a1db-82d3902ad445 | -8.0703 | -43.0981 | 2025-12-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| cb18aef2-48cd-3a75-8139-4d03b992791d | -8.0516 | -43.0765 | 2025-12-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 84f6a61d-44c8-3ae3-87d5-b3ac645823ed | -2.9044 | -45.3494 | 2025-12-02 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e6edff99-9699-3713-829e-48b495ecc1f3 | -4.3703 | -43.1508 | 2025-12-02 01:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a3e6cb43-52c6-31e6-bbe9-2a3baf8eccaa | -14.0755 | -56.1683 | 2025-12-02 01:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 59cbb107-349e-301c-a804-ba1ee7a155fd | -8.0324 | -43.1022 | 2025-12-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 32f6ac13-4430-3e2e-942d-ca28bf5d8b69 | -11.1379 | -53.9429 | 2025-12-02 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 17e52ccc-2319-301b-849b-7515475286b7 | -1.4737 | -45.7907 | 2025-12-02 01:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 507be864-a7bc-3ca6-9334-33a8bf1b1127 | -4.389 | -43.1497 | 2025-12-02 01:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| f3eae24e-887a-3dc7-bc15-a1fb81b323fb | -17.5141 | -57.1925 | 2025-12-02 01:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| a82a8eec-93e1-39d0-aa56-7ad089a6ccb5 | -17.5335 | -57.2107 | 2025-12-02 01:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 55e300b6-ef99-3f99-8184-9b97ba780e83 | -21.7552 | -48.4496 | 2025-12-02 01:50:00 | GOES-19 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 1ec29279-ccf3-33f8-b067-906726f7403f | -1.4923 | -45.7903 | 2025-12-02 01:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 42bb67ea-1076-3463-a0cc-da86b648792d | -8.051 | -43.1237 | 2025-12-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 54ab6395-66c4-392a-a03f-22e2c00ec4ff | -8.0513 | -43.1001 | 2025-12-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 259.9 |
| af8cd74d-a7db-3074-979c-eab5db62aeb4 | -8.0513 | -43.1001 | 2025-12-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 337.9 |
| 4f6e8fb2-74ed-361c-815c-42d7ba683ceb | -12.5213 | -56.9022 | 2025-12-02 02:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| eb65f595-fd58-337d-b451-efd9b94be708 | -1.4737 | -45.7907 | 2025-12-02 02:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b8ed02ec-c687-3c75-a63f-b6f0403680c8 | -19.7873 | -56.6851 | 2025-12-02 02:00:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| aa433b00-b3ea-3452-8903-c2745cc62d8a | -17.5138 | -57.2131 | 2025-12-02 02:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 5d9da632-bf56-3739-96e9-8936ad525257 | -17.8383 | -40.1059 | 2025-12-02 02:00:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 48.0 |
| a6232b06-0249-3afa-b3f5-819ea1d8d92c | -8.0703 | -43.0981 | 2025-12-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| bd58387b-5c67-3a3a-854c-a3741a328ad1 | -8.051 | -43.1237 | 2025-12-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 70341a15-0984-382f-aee7-09db731d33d2 | -11.1379 | -53.9429 | 2025-12-02 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b8067572-639d-3b61-acea-3d4fd6d1aa08 | -17.5141 | -57.1925 | 2025-12-02 02:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 5f99beeb-b7df-3502-a6ea-3cd38066d0da | -8.0324 | -43.1022 | 2025-12-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| b4531b36-c735-3c3a-aa7d-b97ecb815ad1 | -4.389 | -43.1497 | 2025-12-02 02:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8a809f4a-24a3-3c9f-8e32-9e2dba89eda6 | -19.7672 | -56.688 | 2025-12-02 02:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| ec52f572-9053-33c8-90dd-e42870a74feb | -17.5335 | -57.2107 | 2025-12-02 02:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.1 |
| 12e352cc-809b-3c99-bc0b-ec5b27a1c6e2 | -17.5338 | -57.1901 | 2025-12-02 02:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 76ba3d4e-4181-3e31-8ca2-2724620b50a5 | -8.0516 | -43.0765 | 2025-12-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 330d33e3-6516-3310-82e6-c27b57b1b1ef | -4.389 | -43.1497 | 2025-12-02 02:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1aa70dd9-eb0e-356c-9df0-09c0de4af682 | -8.0324 | -43.1022 | 2025-12-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 690c0120-31f2-31aa-9389-48b77eb9fcbb | -1.4737 | -45.7907 | 2025-12-02 02:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ff0091c2-0fdf-3b6a-939e-69991f98a526 | -19.7873 | -56.6851 | 2025-12-02 02:10:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 8b74aade-1438-3a07-9d33-2b13e429616d | -17.5141 | -57.1925 | 2025-12-02 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 77af927b-e991-3703-8a8a-de1b69f3d99f | -11.1379 | -53.9429 | 2025-12-02 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 305ed443-af80-3035-8b28-7d2cc2d77d3d | -8.0703 | -43.0981 | 2025-12-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| e31d5bcb-60ca-31ee-ae37-3e94a4c9f2ad | -8.0513 | -43.1001 | 2025-12-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 377.7 |
| 3ee92874-100a-3507-9b57-31407560a9d5 | -8.051 | -43.1237 | 2025-12-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 6c032419-a480-35ef-bc83-bafa9069f448 | -17.5338 | -57.1901 | 2025-12-02 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| a63b49de-ab55-3456-a158-cafbe139bae7 | -11.1382 | -53.9223 | 2025-12-02 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 099c9f73-17db-3ef0-a453-46bfc33220f5 | -14.0755 | -56.1683 | 2025-12-02 02:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ba297ce4-f161-3b3b-87b1-37a41364e9bd | -19.7672 | -56.688 | 2025-12-02 02:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 8c5751df-eb14-3c6a-b65f-c4a939dc7da1 | -1.4923 | -45.7903 | 2025-12-02 02:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README5.md)
