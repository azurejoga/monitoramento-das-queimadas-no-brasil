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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e26be4d6-4cdf-37ea-bb8c-48dba7574da1 | -9.191 | -59.4425 | 2026-08-23 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ea4cf8d5-422c-3679-bc3f-3a1e3fe48e6c | -6.9513 | -59.0859 | 2026-08-23 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 79995fa5-b62e-3ebf-9181-cd25c858c331 | -10.8361 | -50.9691 | 2026-08-23 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| e59d2109-11ba-36bf-8eb7-5ff0619ba30c | -3.0005 | -48.9592 | 2026-08-23 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 212.2 |
| e9a70a64-65ff-3196-8df6-cfc921606d29 | -7.5669 | -61.1906 | 2026-08-23 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5122979c-ef7f-3886-a780-51160c46ad57 | -6.8061 | -58.6663 | 2026-08-23 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ffa6770f-e1e1-3b8c-84d2-2901f633e30b | -10.8358 | -50.9903 | 2026-08-23 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 59772b96-f6e8-3c43-9add-da34dcb44fc8 | -6.1285 | -57.8393 | 2026-08-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| eaf9ba38-ab23-33b7-bcb1-26f562e2cc2b | -6.8062 | -58.6469 | 2026-08-23 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 0d30a9a7-a6c0-350e-8c43-05b97f661a6a | -6.9514 | -59.0666 | 2026-08-23 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a1db8d0c-9d50-3d09-9fec-bb9ee0a5d1a2 | -21.4532 | -46.1613 | 2026-08-23 01:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 72851104-7089-33d1-8ebc-096cfd5ebd31 | -6.1925 | -53.5231 | 2026-08-23 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0e8e6511-f153-3065-9149-bc86f0504d18 | -21.4748 | -46.1316 | 2026-08-23 01:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 6651a715-0340-3fad-adf5-51f78bccce60 | -9.191 | -59.4425 | 2026-08-23 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f9f1801f-7bdd-3e57-b87f-aa0e67be542c | -6.9698 | -59.0852 | 2026-08-23 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 23e7c707-984c-3f72-8282-3893056aef8e | -6.8061 | -58.6663 | 2026-08-23 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9dc69515-55c4-3f6c-a435-635332ff4d1d | -6.8008 | -59.5934 | 2026-08-23 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 79311a33-cd98-3f40-8c91-8e71c57d8915 | -6.9699 | -59.0658 | 2026-08-23 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 4d0430da-4f2c-39e1-a776-ee5c79972d4e | -6.5487 | -58.522 | 2026-08-23 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5e710372-f02e-3d07-a154-52b7bee748e5 | -2.982 | -48.9598 | 2026-08-23 01:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 2201cdad-3dc0-3f5b-a70c-e5655113d126 | -6.8026 | -62.9212 | 2026-08-23 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9246b4a9-fb84-350d-9c2e-d46165d79f6f | -8.5359 | -55.3428 | 2026-08-23 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e9cd917e-cc44-3bdb-9a97-32a384dbf0aa | -9.1909 | -59.4619 | 2026-08-23 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 8cc4a51a-319a-34c0-b7c5-8ef0f6a8919e | -21.454 | -46.1371 | 2026-08-23 01:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| e66fc461-a70a-3f52-b018-3285c2372ef6 | -3.0005 | -48.9592 | 2026-08-23 01:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 5d0974d5-b725-3027-866e-370c6c9b7d0b | -6.9513 | -59.0859 | 2026-08-23 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1b718604-25af-3392-8b2d-4e2e16b1bece | -6.8062 | -58.6469 | 2026-08-23 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e59caa8d-389f-3e08-9e94-abaec2636381 | -6.8027 | -62.9024 | 2026-08-23 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 833fc9ac-d6b8-3eea-9ea1-4aa9d90213cd | -6.8188 | -59.6696 | 2026-08-23 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 3a25bf27-978b-335b-bccb-bd302a507b50 | -6.1285 | -57.8393 | 2026-08-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f345d844-b8aa-3ffa-98fa-1199d1bd6e29 | -2.9819 | -48.9811 | 2026-08-23 01:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6bec9087-6cb5-3f59-9188-0c9ea316246e | -2.9819 | -48.9811 | 2026-08-23 01:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e3403ad2-96d0-337f-9268-564700ac8a76 | -2.982 | -48.9598 | 2026-08-23 01:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 3d210135-2520-38fa-9503-bd484e701b65 | -6.9699 | -59.0658 | 2026-08-23 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| a7d97d51-586b-3934-a33d-2c53f668534d | -6.1285 | -57.8393 | 2026-08-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 90c80ac0-5009-3eab-a567-e192a501bc98 | -21.4748 | -46.1316 | 2026-08-23 01:50:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| d286f816-fd9a-3506-bb58-40772b97f82e | -10.8172 | -50.9711 | 2026-08-23 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 74a0ff4c-f177-35fb-884d-979d512f7e20 | -6.1925 | -53.5231 | 2026-08-23 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8f0db7a8-9e0e-3285-9ff3-822a410b6769 | -6.1286 | -57.8198 | 2026-08-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 2e2e8d9e-2338-388e-9818-5cf4c67c654d | -21.454 | -46.1371 | 2026-08-23 01:50:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.7 |
| 81972b0f-1f90-38cb-86c3-09838520dd00 | -10.8361 | -50.9691 | 2026-08-23 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 071bc874-8fc4-3597-ad55-f3e1fe107ad3 | -6.8062 | -58.6469 | 2026-08-23 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e1e5f237-62bc-3c47-b7e1-32c76f9278ae | -6.5487 | -58.522 | 2026-08-23 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6e7d4e72-1031-367f-bc0d-e16915d6fb66 | -6.8061 | -58.6663 | 2026-08-23 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 16421d7f-1efc-3c8d-80a0-d30da5d77d33 | -6.9513 | -59.0859 | 2026-08-23 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 42f1e1f8-8647-3663-a445-5f766df20fd0 | -6.9514 | -59.0666 | 2026-08-23 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c338cafb-7e1c-380c-af81-dc8ec75c183d | -13.1889 | -51.4234 | 2026-08-23 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cd0e3ed3-3dfa-3274-9f48-a1c8c30c8b56 | -6.9698 | -59.0852 | 2026-08-23 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fbafc52b-07f7-3ce7-869e-d9ebbe212efc | -3.0005 | -48.9592 | 2026-08-23 01:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| d6ef29ee-eaf5-33a1-b6bf-5069b968f066 | -9.1909 | -59.4619 | 2026-08-23 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 09af4fff-df71-369b-a763-20c7d40f7e41 | -6.8027 | -62.9024 | 2026-08-23 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ac475bc6-5227-3a5e-a731-5c445dc3e273 | -6.8188 | -59.6696 | 2026-08-23 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ff61bb4e-a544-3d8d-bcf5-9879b33f26c6 | -6.8062 | -58.6469 | 2026-08-23 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 7f731ce8-31dd-30c6-913d-34a2ace29f5f | -6.1925 | -53.5231 | 2026-08-23 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 83a0b578-3c6b-3626-8890-83c34e8f2636 | -6.9698 | -59.0852 | 2026-08-23 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1a2a8d0d-d26b-365e-8b23-b6f20469a418 | -3.0005 | -48.9592 | 2026-08-23 02:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 002230c7-3dc2-370c-99ee-81e683564ddf | -6.8188 | -59.6696 | 2026-08-23 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e55c0f67-d8ab-340e-b87d-c84e4abf30d6 | -9.191 | -59.4425 | 2026-08-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| ccda6cdb-af1c-3541-88bc-84464026358e | -13.1886 | -51.4447 | 2026-08-23 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c147f3d9-931f-3b4b-a1f9-e25e8a9ef0ac | -6.1285 | -57.8393 | 2026-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 728e3a63-1b9d-3254-afea-0490cf3ca371 | -3.0005 | -48.9378 | 2026-08-23 02:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8bc257b1-3e64-3fb8-86af-cdbac4e66383 | -13.1697 | -51.4258 | 2026-08-23 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 904d0368-8600-36d7-a018-11310cb5d00e | -21.4748 | -46.1316 | 2026-08-23 02:00:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| 459dbbc3-8723-3334-88f6-a3d58f6df134 | -6.9699 | -59.0658 | 2026-08-23 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 80e7fdad-5194-3469-a88e-bf4893f34d1e | -10.8361 | -50.9691 | 2026-08-23 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 5c8ac521-2fda-3d94-bf0b-d5753aab80d9 | -6.1469 | -57.8385 | 2026-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 4cfa0d34-8648-3dc5-8eb7-7955104f76c5 | -10.0667 | -46.4544 | 2026-08-23 02:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| b364f8f4-20a7-34fb-98f3-e6194d9cd63d | -6.1286 | -57.8198 | 2026-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c6741751-bcb7-3b56-aae6-d84272cb1dd1 | -6.5487 | -58.522 | 2026-08-23 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 7762466b-ec84-3016-9792-ffe1cf8d3237 | -13.1889 | -51.4234 | 2026-08-23 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ccf289ec-d6b5-3039-b4f1-3474b574ee0b | -6.8061 | -58.6663 | 2026-08-23 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 62b2977b-2834-360f-b8d8-41b27c09abeb | -6.1101 | -57.84 | 2026-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 77194c99-8eab-3e14-afae-28c372ecf626 | -6.8027 | -62.9024 | 2026-08-23 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| dae242a6-c2e5-379d-a92c-1a74b6fa2898 | -21.454 | -46.1371 | 2026-08-23 02:00:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| f664ca99-5aee-3e62-b3a2-51341a81960c | -13.2078 | -51.4423 | 2026-08-23 02:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| d269f3f5-0d3f-3acd-aa5e-0f384dff666d | -6.8008 | -59.5934 | 2026-08-23 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ca191782-348a-3f23-948d-e48469bdf1e9 | -10.0671 | -46.4319 | 2026-08-23 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1860d905-c557-35ba-accb-73d5ca588852 | -5.7799 | -57.58 | 2026-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 31203d1c-04b3-3c16-b930-4884df0f4a72 | -6.9513 | -59.0859 | 2026-08-23 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1bc543e9-7e43-35be-bde9-6e7e1c6a724e | -10.8358 | -50.9903 | 2026-08-23 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9724e81f-2eea-339a-baa8-4aae97613707 | -6.9514 | -59.0666 | 2026-08-23 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 4470642c-86bd-3633-b505-4e102509bd00 | -2.982 | -48.9598 | 2026-08-23 02:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| ce999459-33f3-3d85-8019-f0ed98f3e51b | -6.8188 | -59.6696 | 2026-08-23 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| bda972c2-441f-3ad7-bb46-9aa38dbab37b | -6.8373 | -59.6689 | 2026-08-23 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b22433a2-bd3c-3a15-82a9-e897de1cebb4 | -12.075 | -50.5974 | 2026-08-23 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 17a9508e-3703-352c-8caa-80bc403d58ff | -13.1697 | -51.4258 | 2026-08-23 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6a2d40e4-db31-37b8-9d79-1307f5f68445 | -20.2758 | -48.6518 | 2026-08-23 02:10:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 52.3 |
| ca421f7a-f5ee-385a-8a98-077a6bc80038 | -13.2078 | -51.4423 | 2026-08-23 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f35d8bdb-8f8a-36c2-9fd3-855f6fe2475f | -6.1101 | -57.84 | 2026-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e8d11d38-4701-3430-a9e2-ac080433bf8c | -21.454 | -46.1371 | 2026-08-23 02:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| adbe1a0c-2a3c-381a-af72-6ced65d16f46 | -5.7799 | -57.58 | 2026-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 8cf20b72-b60d-336c-8d3f-eb1dfef62cc8 | -6.5487 | -58.522 | 2026-08-23 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 417d1118-5f75-3909-bca1-5b055a057c3f | -6.1285 | -57.8393 | 2026-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| a67c3516-7b12-3c9f-8d8d-f9d49d477d6d | -21.4748 | -46.1316 | 2026-08-23 02:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| ee5ff6b9-1524-3f5c-8971-39642941c8cb | -6.1925 | -53.5231 | 2026-08-23 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 62e30ea0-8ad6-3da2-aa2b-e5f25a69b325 | -6.8061 | -58.6663 | 2026-08-23 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 748b5c18-31dc-3a97-a687-eb2756af36c3 | -16.0706 | -50.4332 | 2026-08-23 02:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 7d1973e9-dd85-3b5d-8b52-de4127ef766d | -6.8027 | -62.9024 | 2026-08-23 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 10e58f3c-276d-3e50-90f7-19c02e5b143f | -6.8062 | -58.6469 | 2026-08-23 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| c5173fd7-ed56-3343-acf6-e0d3fc3ec9f4 | -3.0005 | -48.9592 | 2026-08-23 02:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |


[Clique aqui para ver as próximas entradas](README7.md)
