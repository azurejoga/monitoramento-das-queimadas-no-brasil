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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c06a551-ccd0-3136-9f1a-56bb82d27ef2 | -3.3347 | -49.7313 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c6070e1-58ff-31ac-93d2-5913c280d48d | -2.83269 | -50.44151 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74441c4f-206e-30bc-9463-8700f52d2178 | -3.0677 | -49.3784 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba688359-5c76-3ee3-8cc4-8a2b838b3607 | -3.59005 | -41.65851 | 2025-11-09 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 23b78fbe-3bce-388e-be05-bbabe2dd6cba | -3.28296 | -49.77712 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83e06a3e-97db-3c7d-9d88-07a2b1ab8552 | -6.40712 | -56.32091 | 2025-11-09 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d8426bc-8501-3149-8d82-eeabe5e5ce35 | -3.1313 | -49.10503 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d2b4233-ec7e-3671-9e4b-54ff630a4786 | -5.72962 | -46.46468 | 2025-11-09 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51e27c4f-904e-37cc-8a66-59aa7b55b28c | -3.15736 | -49.5425 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94d50a1a-8b72-3fee-98bd-2d11f923b9fd | -1.69999 | -54.67196 | 2025-11-09 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e853ebc7-c103-37ec-a0c7-5772a90f8a47 | -5.39911 | -47.26133 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37c7f460-3353-3ea1-99fd-d083cdffcada | -3.07998 | -49.4729 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6387ff47-b452-3d85-a964-3bc352f828ed | -2.97612 | -48.71043 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03a3429c-6f75-381c-ad1e-90ba9cd6ebf2 | -3.32108 | -50.15358 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f560c08-b171-3b0d-a53a-e5b99acae8a2 | -3.76569 | -45.87074 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb3fe2d2-5642-328b-be40-f2d9604200e6 | -3.063 | -48.72092 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45790e58-936d-3b42-833d-0ffc6699eb15 | -4.01013 | -44.78664 | 2025-11-09 04:38:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3727c5d6-5073-37cb-bf25-b17af6511a51 | -2.26175 | -47.87645 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0902e908-c20d-3d2f-8c04-4af20921f615 | -3.46969 | -39.577 | 2025-11-09 04:38:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5ad11ac2-fc33-34c6-9760-ce89d7e246c6 | -3.09002 | -50.32407 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d41b347-4189-313d-a6a3-621c76cd0427 | -3.44906 | -45.65574 | 2025-11-09 04:38:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6ae99a4a-4db6-316f-8c33-2d17fc21a849 | -3.04727 | -50.25891 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29dc0e39-7e69-361b-8526-0f22f41551f1 | -5.35225 | -45.80946 | 2025-11-09 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6094701-3926-3b5b-a865-856c4797e1e2 | -4.80277 | -45.3953 | 2025-11-09 04:38:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d86ceb38-ea74-3725-b6bc-af63e1ac6aa6 | -6.22013 | -47.02007 | 2025-11-09 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a08b385-2392-3711-beb7-0b1f73c2145f | -4.83505 | -45.4481 | 2025-11-09 04:38:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c24f987-98eb-3151-8a2d-4fe702cba9a4 | -3.13988 | -50.27259 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 339100f4-a521-36d0-9112-b047ae65ec61 | -3.32802 | -44.36805 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8f32e97-08da-3f87-9b34-09745d52400a | -3.32426 | -49.13161 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adfdf709-46f0-3144-aa5f-70e3697c05e8 | -5.1807 | -56.00063 | 2025-11-09 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9823dfdd-bce9-31ff-959c-a1bace04896e | -3.33114 | -44.37339 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aac215ce-19ab-328d-8e7a-3f8916dcfec8 | -3.31489 | -49.12661 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1f3dba-0619-3c41-8231-4a200e5c38f7 | -3.67109 | -51.16602 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e07e7ae8-f738-3066-ab4d-959bacd1f5e0 | -3.83254 | -51.99006 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0412452e-e61f-3db5-8169-903a7f0c6eb8 | -5.4031 | -47.25813 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f47cb1ff-5a9a-3f67-9fa6-3e2f1c49390a | -3.95552 | -49.03046 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1684aa19-d80c-3553-be32-d8134439e5eb | -3.4292 | -50.24429 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 988627e3-231f-3c7d-bd78-ea1c7f5af460 | -7.56206 | -45.88187 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a94792cb-a514-3263-acae-cc525ff820ac | -3.33426 | -50.07147 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79db88c8-f7b0-32cd-949b-bfa73d4be72f | -3.31651 | -50.31142 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a560f06-3c1d-3b3a-8b85-d03791d27c06 | -5.38324 | -44.73201 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e2f646e6-8354-3126-b325-5918a7c5f6fb | -3.41224 | -50.26376 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 500bd275-241c-3301-b4dd-72862a06469e | -3.8432 | -50.74562 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0e778da-dfd3-351a-a9de-87b77fff9c4c | -4.68289 | -46.40374 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a99965f5-1522-32e8-b731-0a920c434cdb | -2.7081 | -49.54647 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d1226b7-f27f-3f22-9dd8-c224485003d1 | -5.44538 | -48.08898 | 2025-11-09 04:38:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e35367bb-248d-3c6d-895f-9df08564cb72 | -4.86884 | -45.98967 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88b62f4e-fa18-3188-88c2-638a5e199048 | -3.00354 | -49.61105 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a2f11da-4740-3d03-b822-a4895ab5e4e9 | -3.53464 | -50.85354 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c277f308-d631-3e19-9d80-45c866039939 | -3.3215 | -49.12765 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c31baea-1c99-390b-9115-56daabd5e75e | -3.40771 | -50.2704 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e186d811-d6a3-3be4-8b3e-0cb6a5642f05 | -3.33776 | -50.20031 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7581ff4f-3614-3da6-97f9-b5b372154692 | -4.25252 | -48.63354 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc23f1e9-9d3a-333d-89bb-0cba08596a5b | -5.89531 | -43.96545 | 2025-11-09 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a3a85a2-426b-3b3c-a88f-aa0f835acb89 | -2.43934 | -49.22595 | 2025-11-09 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4561645-e232-39dd-a4a1-64e22650e573 | -2.8321 | -50.44516 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39316805-4ce0-3a5a-86d2-9a79440dabfc | -6.54908 | -44.46622 | 2025-11-09 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4762ed1e-f80d-39ab-88d2-bc782ff3ef44 | -4.11617 | -47.2887 | 2025-11-09 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1851f50-4762-3213-af6b-925c1a0b0213 | -3.46222 | -48.81893 | 2025-11-09 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08631d4f-c1bf-325b-b1e4-ca74917d8651 | -5.77988 | -46.56152 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1600e479-cf8f-3fd3-b24a-d34060167684 | -3.41388 | -50.27509 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51615799-b531-355f-9b6f-0f9fbbf93648 | -3.53807 | -50.8541 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 984b323e-c8d9-3c6e-975f-432f7def1254 | -3.47165 | -50.34709 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5503dbe7-0fea-3048-a537-927e532ccd2f | -6.03188 | -46.5693 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea859aa7-b6e2-35cd-8e2f-39a5fa588c5d | -2.84185 | -49.5173 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90165937-864f-3970-8ce8-e517d6da02dc | -3.03237 | -49.49395 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cd72534-1456-3df4-a0b3-bb3b66cf451c | -3.09743 | -49.68355 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 02ebf161-0c13-3a28-ae51-5997ecbc3b8a | -2.93728 | -48.80637 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 425e74d2-c396-3152-b435-d01117dcd037 | -3.97901 | -49.86884 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99500145-f15f-37e4-af05-a9b7c556a43a | -6.22071 | -47.01624 | 2025-11-09 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22a4e946-c75a-3544-8bb0-3c6fa86e6e73 | -3.61461 | -49.27342 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3adf6961-55e0-347b-a75d-a6e6e278fb59 | -3.45329 | -45.65217 | 2025-11-09 04:38:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bab04257-2a3d-3ea5-a368-4e119f22c867 | -3.56012 | -45.01569 | 2025-11-09 04:38:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0e3ade8-690f-3bc3-8322-437131065a2c | -5.77841 | -49.83626 | 2025-11-09 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baf3e83b-b8fb-3708-bc1c-7556f2cd63d0 | -5.84752 | -46.44769 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca951c6a-74b9-39e5-8739-b24ea7fc4a0e | -3.849 | -51.07976 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99b1043c-f9f9-3e41-a3a5-54f5786ca581 | -4.20287 | -50.66574 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff6cd599-f6a1-34b5-a0a4-519fd64b7a0e | -4.24461 | -48.3813 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 623f83e5-7453-38a6-8483-38d30f53aa2d | -2.62435 | -50.07428 | 2025-11-09 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27cc0d9e-533b-34e7-8923-e487dd15ab32 | -3.40944 | -50.25962 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccba86a4-5fa3-39b3-b7d3-60a46b6accb8 | -3.80537 | -45.99251 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54874cc4-9e8f-3110-a924-9be60a5e4003 | -3.08181 | -52.91973 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 501fe06c-94cb-38c4-be8d-61acf3535076 | -7.55901 | -45.87684 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7b8ea85-da1a-3ecb-8ece-f891533b0702 | -4.92357 | -48.40601 | 2025-11-09 04:38:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0849d339-4dc2-3b04-8d2f-50740241f288 | -3.43014 | -50.43347 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| caaa37cd-f6d1-34bc-a344-0312f5a79b5b | -3.49741 | -46.30213 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11ef2f08-c570-312d-bfae-01d5882fb58a | -3.74251 | -52.42977 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7bd363e-fad3-3b99-b4ee-e43269912449 | -4.74259 | -49.89634 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e793d0-ed54-3fe6-96fe-7dc53a5e95f3 | -4.72129 | -42.93124 | 2025-11-09 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ac457b-dba8-3818-ad49-ee19a4d8d264 | -3.17036 | -49.2459 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d90ed81f-6d9b-3a85-8acc-9723739dddac | -4.64826 | -48.68866 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b7fd65b-ef46-3269-b2b2-4b1ca19a2217 | -2.98457 | -52.82352 | 2025-11-09 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 387b60ad-f22a-3a0b-b350-69acb7640dac | -4.68483 | -45.84634 | 2025-11-09 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcd060c8-2907-3d93-8857-c2cff52ef928 | -4.3014 | -48.58118 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d03ba83-0b6b-3ba9-8290-568062e3e5ac | -3.52615 | -50.53445 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54152951-c5e6-39a5-8a31-a3c418da3d4d | -3.07157 | -49.37544 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c69d894-d4fb-3187-8fd5-82d97405751a | -4.86615 | -48.5994 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfd5b427-5d5e-366e-9845-28bd0b1ffc24 | -2.43115 | -48.05076 | 2025-11-09 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9771b273-370b-3908-bba8-e6d853ed43ad | -3.76976 | -44.28901 | 2025-11-09 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcfcc067-09b5-3cc9-aa07-418f2c5ee528 | -2.92157 | -40.00982 | 2025-11-09 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README28.md)
