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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6829f7db-7feb-363d-a097-cb4d68b9bc2c | -28.18047 | -49.86489 | 2026-09-07 03:47:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9cda011-b02a-38f2-9bf9-23630103eed7 | -28.67389 | -49.05146 | 2026-09-07 03:47:00 | NOAA-20 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1aaac285-de4f-3181-9c8a-311c156d0d10 | -28.182 | -49.86547 | 2026-09-07 03:47:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f190a779-3457-3dec-9310-8e4b53876532 | -8.7622 | -62.4351 | 2026-09-07 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c4eb20ac-880c-3fd1-8fd1-8b87757ea58e | -2.8839 | -50.4428 | 2026-09-07 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b392540d-12d7-3ca2-85b1-0df6a0619e39 | -2.6387 | -46.7817 | 2026-09-07 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| eb916499-4039-36eb-81f5-6ab591f7b2cb | -8.7066 | -62.4374 | 2026-09-07 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 367447e5-19ca-31d2-bd45-de6b268952a5 | -2.8655 | -50.4434 | 2026-09-07 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e48b7c06-eec5-3315-8210-b8c2c82162a0 | -3.1461 | -60.6696 | 2026-09-07 03:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0a9711d4-d73b-32f8-8ae1-c0bc3c9a2358 | -8.7437 | -62.4359 | 2026-09-07 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 93347864-e450-3fa5-a980-a12885627c40 | -6.6513 | -59.9642 | 2026-09-07 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| eba82ea7-d87f-3bf1-ba85-d87f0afa0024 | -2.6388 | -46.7597 | 2026-09-07 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 061d1126-5ff4-3ca0-806a-499888e1e0ba | -2.6387 | -46.7817 | 2026-09-07 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b277d078-9e42-3874-8247-b539ebc2ad4c | -3.1461 | -60.6696 | 2026-09-07 04:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f42f0b85-8048-33bf-a812-70a3abf9e3b7 | -8.7622 | -62.4351 | 2026-09-07 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a534be74-e41c-347c-96de-a56df0235fd0 | -8.7437 | -62.4359 | 2026-09-07 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4cfa97b4-a12a-3c2d-8806-9bc59f561933 | -3.1462 | -60.6506 | 2026-09-07 04:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| cdf589e8-beff-3b61-8684-daa5fc509692 | -13.2284 | -61.7743 | 2026-09-07 04:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c133ecc3-55ed-3ca7-8891-2d08c9b8ca70 | -2.8839 | -50.4428 | 2026-09-07 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a3f2753c-40a6-38cd-b4d9-f9a6912d849e | -8.7622 | -62.4351 | 2026-09-07 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bda91789-9cc9-34ed-9e85-21a41b840521 | -13.2284 | -61.7743 | 2026-09-07 04:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3a1779bf-70f9-3d73-ab8b-a0e51cd8adce | -2.6388 | -46.7597 | 2026-09-07 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d2016ac4-82a5-3412-8d33-4d8725131389 | -3.1461 | -60.6696 | 2026-09-07 04:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| f3d896db-32d5-3412-88a3-2913be4cda55 | -13.2477 | -61.7342 | 2026-09-07 04:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 77ea8a39-5736-30d1-a70b-8304234d670d | -3.1462 | -60.6506 | 2026-09-07 04:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a2f00162-7b07-39ba-9f4c-f07f1d3b7943 | -13.2094 | -61.7755 | 2026-09-07 04:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| efa4974d-94e2-35ca-a8c9-73507b0aea7a | -2.8839 | -50.4428 | 2026-09-07 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 45ace870-21ee-36a1-9d84-9fed77284886 | -2.6387 | -46.7817 | 2026-09-07 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c16e7eec-67f4-3322-be66-5e85ced6252a | -8.7437 | -62.4359 | 2026-09-07 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c7f1c118-6392-314c-8270-2db0748e7cca | -13.3 | -45.24 | 2026-09-07 04:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27b51e4e-c550-3043-8c20-4a602642945e | -2.6387 | -46.7817 | 2026-09-07 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5862f41c-afdf-3287-9686-45993821572c | -2.8839 | -50.4428 | 2026-09-07 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a503a74c-21fc-39dc-ac03-919ad20fcd93 | -3.1461 | -60.6696 | 2026-09-07 04:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5e87ce21-946b-3985-bde2-0bc9cb0475a7 | -3.1462 | -60.6506 | 2026-09-07 04:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 05268d14-1754-35fc-ad18-e2f29cb07664 | 1.71747 | -50.96988 | 2026-09-07 04:23:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 893d1baf-a4b6-3c8a-836f-25ac17657338 | 2.44069 | -50.77759 | 2026-09-07 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53ce32d4-9ef3-383d-9e3a-05d730f509ec | 2.44004 | -50.77328 | 2026-09-07 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e50f36f7-4d3a-3bdd-bdaa-83ab9002266d | 2.02946 | -50.91806 | 2026-09-07 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa62b88c-38d7-31af-886e-6a28f5418123 | 2.02504 | -50.9187 | 2026-09-07 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8187a60-5079-39a4-9a0f-9092e08413d9 | 1.71812 | -50.97417 | 2026-09-07 04:23:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23e74a82-c4c8-3c4b-846e-20259835d95c | -4.10473 | -49.06446 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbbdb740-2898-3c3d-9eed-686b84d9bdfd | -2.36589 | -44.57957 | 2026-09-07 04:25:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9644b197-b7a1-364e-998b-0c8c8439af42 | -2.86519 | -50.44337 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4d782da-3d00-3458-a08e-65b18f5586d8 | -2.88119 | -50.46123 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f373f837-7df1-3761-8c28-06de4ffd5de7 | -4.47378 | -55.09124 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52135d27-639d-30e2-8a91-31d99b31450c | -1.86215 | -47.98199 | 2026-09-07 04:25:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00e5db69-d167-3f35-9066-eaae4a746a15 | 1.65014 | -56.05423 | 2026-09-07 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42db31b7-1415-31df-86b9-2d09498b74e3 | -6.77833 | -41.16808 | 2026-09-07 04:25:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7239afee-af97-30c7-b6de-52b8f9198192 | -2.86738 | -50.4459 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a016cde-07e2-3ce2-b421-1dbbf1d3061b | -6.4169 | -46.60847 | 2026-09-07 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da335c4b-4434-3fcf-a010-31c547e623b0 | -5.15588 | -55.96657 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa49ded2-d504-34c4-95ca-9ca0ee5fbe62 | -2.91435 | -54.11917 | 2026-09-07 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b74db98e-bc27-37cd-add7-784b4b6a0d60 | -4.21371 | -48.56426 | 2026-09-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df1c0bef-b54c-3c94-9491-bfff2685d38f | -5.14044 | -55.95656 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74d9adc4-4963-36de-a163-177d4f95450f | -2.3021 | -48.58823 | 2026-09-07 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9965664-9349-364b-9f50-79fe857a0f8f | -4.43082 | -55.09494 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d468435-8156-3d5e-9ab7-416b97efb3d9 | -4.46849 | -55.09024 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b288405-e367-3d6e-936b-e1a2f565e113 | -2.30342 | -48.57999 | 2026-09-07 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7947e296-4338-3a46-bac8-28d36c84239d | -4.67495 | -55.62836 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b194d63-2934-3ce8-ba23-4c3675da9280 | 0.21564 | -51.28518 | 2026-09-07 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ddaf165-8f90-306c-8fd8-00529317933a | -2.82188 | -46.71146 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ac39bf0-433d-34a4-bf96-ec431b5c7fb5 | -4.35138 | -48.97511 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd6e465f-e32a-3101-94fc-629b3ceccf57 | 0.21938 | -51.28017 | 2026-09-07 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ed66aa4-c48c-3490-9ac0-2739fce1af47 | -3.78919 | -55.87757 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30f7c96a-c68d-36cf-9e61-f5bb1c26ec36 | -4.34855 | -56.28201 | 2026-09-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aec4ae2f-070a-3ba4-aafc-1c60257f5ed6 | -4.97814 | -50.63186 | 2026-09-07 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cacfa69f-30a6-378b-b336-45a1bf55a28f | -3.93369 | -48.42974 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cefad9f-f837-3733-917c-b87ddb42f7af | -3.81415 | -52.35452 | 2026-09-07 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7da17739-cb18-378e-9d11-4542060fcbeb | -4.47433 | -55.09589 | 2026-09-07 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17aa37a0-9680-3dfc-a48a-bb8c9e7cb76d | -4.02718 | -52.07548 | 2026-09-07 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 074b9629-bf9c-3536-bc71-2b381e55bbe6 | -5.14537 | -55.96114 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75d09715-40da-3300-8ba2-27e58a39c4cb | -3.88598 | -38.39367 | 2026-09-07 04:25:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c21b8b81-08f5-3c69-bb1a-07c891239d04 | -2.82216 | -49.23156 | 2026-09-07 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e2f3fd4-0cbe-3f3e-bbcb-be5bce600f80 | -5.28639 | -50.25826 | 2026-09-07 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3564f05b-6475-3ded-aede-bf8fd78d238e | -4.46172 | -49.12651 | 2026-09-07 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5e744cf-3e69-3733-ba07-860d63799bc5 | -2.4128 | -46.47893 | 2026-09-07 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32f3151f-0e76-35fc-878b-f9e38db579ba | -2.86256 | -50.45042 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a33e9058-63fb-3ea4-9fcd-94ca90773c4d | -2.63279 | -46.76896 | 2026-09-07 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6490fcaf-0b45-3bdf-9377-150c13bfd489 | -3.66152 | -45.82489 | 2026-09-07 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32123494-14ed-320a-a1ab-319e1ed11505 | -4.21786 | -48.56085 | 2026-09-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 445f78b2-65ac-390c-b553-2d389ed7de07 | -2.88013 | -50.44267 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 49796eff-e8b4-3639-9bb2-f79144fbe158 | -1.18642 | -55.70969 | 2026-09-07 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fa45dee-1be2-380b-bae8-c596e66aeb28 | -2.41613 | -46.47944 | 2026-09-07 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d30aa4b-10f7-3ae3-b2d2-498e176f2837 | -3.81039 | -52.34954 | 2026-09-07 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 790c32bd-9310-3bd8-8438-e1ebec9207bc | -5.14409 | -55.96856 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfd4fb8f-e02a-3bb4-8ecd-06648d9a05e9 | -3.9592 | -55.40173 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e09c1cb-c4d9-33a7-858d-511c86fde1be | -4.10834 | -49.06502 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cbf41640-1c9b-311b-a29f-47fe5fef9d6c | 0.2163 | -51.28949 | 2026-09-07 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c97be83-227b-36cb-b5d3-1f3e89811f20 | -6.56785 | -44.77723 | 2026-09-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54311872-f2ea-3044-a034-600d95f03587 | -1.49464 | -54.81966 | 2026-09-07 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8123a7ed-5bd4-35c5-b5b5-e39c511a524c | -4.97484 | -56.29105 | 2026-09-07 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0724df3-de81-3949-8578-633b73c3ba95 | -2.86654 | -50.45102 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 747c0d36-37bf-341e-a112-8c15644a4731 | -4.11194 | -49.06558 | 2026-09-07 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 58fba812-59bf-3e7a-a4c6-e4eeced65a43 | -4.03728 | -50.8763 | 2026-09-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6cbce64f-36b2-3723-b79a-a7569ac0da25 | -0.47155 | -51.82922 | 2026-09-07 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45ee7702-dca8-3e20-9479-1c919232d511 | -3.21041 | -42.97927 | 2026-09-07 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8163272-b078-3900-ab6e-b38528c4a7f0 | -2.03269 | -48.57885 | 2026-09-07 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed367c6-d6de-3f69-a729-2e7fb9bce6dc | -3.79421 | -55.88235 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92c7c352-d528-3043-95f0-80c641b32d89 | -2.30569 | -48.58879 | 2026-09-07 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e90d9113-4410-3cb6-a808-e68db09e4878 | -3.79229 | -55.87737 | 2026-09-07 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README12.md)
