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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1e23b37-7d2b-3870-9bcf-d5766f799207 | -7.82858 | -45.81367 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c0c323a6-fec9-3073-8f86-8db86779ea90 | -1.04474 | -53.5634 | 2026-09-29 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ccebf86f-24c3-36f9-9c4f-addecbb43f8d | -3.15562 | -54.09317 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94778ea0-358f-38a1-bd7f-8091a4750d8e | -6.70321 | -45.69212 | 2026-09-29 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5921a46-d94c-3e77-8408-dc1e34e48d7f | -4.31905 | -48.63041 | 2026-09-29 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 639c8a82-4f58-3271-893a-e96e7900ec57 | -7.84497 | -45.82452 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 50b197ad-19ee-3282-aaf0-79fa99295bd5 | -4.81948 | -45.63859 | 2026-09-29 05:10:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4126154-1453-3db7-8438-0ce916f4a459 | -3.01997 | -53.87247 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 23d164c2-bc76-3277-a369-21b8a98d994e | -6.68064 | -55.10611 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72e2c6fa-c7fc-3e51-8a55-910d0f3884b8 | -4.50389 | -42.55737 | 2026-09-29 05:10:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b1d0c18-8784-3021-b676-bb9fbd1443c5 | -2.95484 | -54.09096 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eefedd8b-12f9-3e72-8246-0be0f24e7fc4 | -2.29224 | -48.58232 | 2026-09-29 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c7a2fdb-4ef3-3752-8a27-97980a6ecbdc | -7.25868 | -45.3398 | 2026-09-29 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca49a7b2-c883-3b6c-a1d5-df86fa90ca4c | -3.83009 | -55.90545 | 2026-09-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 43a6d31b-01af-38fa-ad46-ac9cbd6750f3 | -7.26462 | -45.34089 | 2026-09-29 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18bcb107-f41b-31a2-8ae7-c0b4014144d5 | -3.41661 | -48.33553 | 2026-09-29 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a7b58d5-8bb9-38be-8b85-2758f68c62e0 | -6.67899 | -55.11666 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a3f747c-ac0e-3e15-b241-81ad6788b315 | -6.13494 | -44.13935 | 2026-09-29 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0212d04c-b6d3-3b06-b5a9-90a52eedb0f1 | -5.73964 | -43.27963 | 2026-09-29 05:10:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9c017ad-5917-389f-a51e-721fefd80592 | -2.98055 | -54.14537 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b46112b5-0ccb-384e-aaa9-76f82327fb79 | -6.30733 | -56.02967 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4baa4f0-1c22-3af6-a684-bc6155ff15ea | -2.66027 | -51.7344 | 2026-09-29 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f1acfb1-5e15-360c-9c6e-a5751ad5722c | -3.88572 | -49.50344 | 2026-09-29 05:10:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 515998cd-5541-3284-b8d9-7ae46a4221f6 | -1.05812 | -53.58721 | 2026-09-29 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3384e5ed-7746-3987-8751-b30145f86f8c | -4.1326 | -51.06219 | 2026-09-29 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd25c81-6877-3a2e-b5c6-66886a015622 | -6.31534 | -52.62065 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d996e595-424f-3fc5-b6da-aafa723aa0b7 | -4.49973 | -49.64137 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f102bae-28e0-372f-8fa9-f0429ccf04da | -2.89833 | -54.08548 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e35036-43e4-322f-9a51-4637321b397e | -3.88512 | -49.50748 | 2026-09-29 05:10:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f55cbbf0-503a-3264-be03-7953071ac83a | -6.67565 | -55.11613 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 436f039b-cfda-3502-9efb-27c1ce84c51c | -6.88553 | -52.47761 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e65470c6-3ba7-33ba-9510-c3c8f5c1eaff | -7.83932 | -45.82402 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 33cd6f90-e844-346e-92f0-d33727fe89d9 | -8.21487 | -45.46077 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2612027a-05b2-3cb9-8e5e-6b6c94957233 | -2.66004 | -51.73561 | 2026-09-29 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d4d62bd-67e9-3f52-8822-fd06b2431232 | -6.74165 | -55.08352 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d180b7ee-b15b-3a01-bafe-eda0068f04bf | -3.2657 | -53.99816 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d056809-46c7-32cc-8471-6ba902552ede | -5.12365 | -47.762 | 2026-09-29 05:10:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b63967-f9f7-3ed7-8886-73ef63b8a18e | -7.43316 | -46.88445 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79336d23-4124-3304-9ce1-5999a0e7110f | -4.71356 | -50.63987 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e07882bc-80cf-3886-a571-9565ee586526 | -5.30946 | -55.83237 | 2026-09-29 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed27319-d2f2-30a4-bfa3-af7b5c2bae19 | -4.04962 | -54.92628 | 2026-09-29 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 46a56ced-eb04-3fe2-9d1d-0df2d1cc0641 | -3.70788 | -54.22594 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 064c591c-9160-3fd7-a0f5-4650dc869db1 | -2.94706 | -54.09695 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed36ef75-8bae-3048-b647-44010542bd20 | -4.04908 | -54.92974 | 2026-09-29 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 51a102cb-98d7-36a3-95f8-6a3aa57b0774 | -3.82346 | -55.90441 | 2026-09-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4bfcc142-725e-3f5e-b01d-f544a638c1cd | -6.28869 | -43.65635 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 91a10d81-0dc7-3f29-b852-ec77ca4158eb | -8.73462 | -44.93209 | 2026-09-29 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abe04092-963f-344a-b481-56c0c6aa2644 | -3.6039 | -49.4551 | 2026-09-29 05:10:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45d0469c-2d36-3f7d-89d4-39f90f7987e2 | -2.91228 | -54.1273 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e465d6e9-d5ec-303b-acea-25b363ffc86e | -6.31859 | -52.6227 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42f31640-177a-3fc1-84c7-b99fff7a6d5c | -6.37761 | -55.13043 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 147dfa7e-3525-3e7e-ba68-fe0a71a79733 | -8.72415 | -44.91462 | 2026-09-29 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b52ffa05-207b-365b-9ebd-afd26ea24a4c | -5.73184 | -45.05448 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b7a8964-761d-3719-b2ae-4eef77a097a5 | -3.3585 | -54.74321 | 2026-09-29 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14078cf3-8f2f-3c9f-b83b-eecb11c59d51 | -4.49487 | -49.6447 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5af38bd-5525-384a-ad98-a1aa9525eb72 | -6.72342 | -45.58718 | 2026-09-29 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57281e73-ef88-30a3-b74f-f12005acc759 | -3.95732 | -49.05069 | 2026-09-29 05:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46b93a03-8f44-387c-b451-df4a56c94b10 | -2.86495 | -54.12354 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe559bc-e682-3311-886c-1e492110a3d5 | -6.71854 | -45.62295 | 2026-09-29 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0cadfcd-debb-3763-8a75-c1ece0de5132 | -7.47945 | -45.81629 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf411520-69dc-3f3f-a424-d49029052299 | -5.73553 | -45.02795 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b723d65-0798-37ca-8a2d-0290c043fbc0 | -6.67232 | -55.11561 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 870f1fab-e2d3-3595-a728-e3e58e2e8d22 | -7.24746 | -45.26543 | 2026-09-29 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01643745-1d45-3aae-948c-8c37e8ef0699 | -5.72561 | -53.46089 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7962d145-075d-3e33-8756-fc1f387ac13d | -6.67621 | -55.11261 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81f06a3e-26b2-3357-a97f-1362fb74ba30 | -3.70898 | -54.21889 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3717f2d6-1664-32ea-862d-2d896f1a9d96 | -2.95429 | -54.09447 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c9fec588-5364-3c86-b938-0397f69b04a8 | -7.51467 | -47.33799 | 2026-09-29 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c208337e-4b0f-3b3b-b102-06496070888b | -2.90503 | -54.10816 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0900bd0-1202-30a9-9aa0-c9bf08c14b53 | -6.30293 | -56.03606 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7e166fb-7b2f-3b58-912a-1dd1666d0bb4 | -6.70901 | -45.6928 | 2026-09-29 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 130e142a-3ef1-3bfc-8140-c6515dd8e5b9 | -6.31238 | -43.62086 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18aaf8ba-07c4-3071-ba7d-2dfc94c87492 | -7.82879 | -45.81428 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0ad8cf70-1a74-3692-ac23-47e448a974ca | -3.23176 | -52.22905 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14aa0601-6d3b-3f76-9376-da48206dc1d4 | -7.99773 | -43.25848 | 2026-09-29 05:10:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a6496b98-e6e0-3ef4-8bc4-efd0d43009fd | -3.96175 | -49.05127 | 2026-09-29 05:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af67cc58-04ad-33ad-9c1c-7a191a53ad3a | -3.01232 | -54.22586 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45bd95ac-824c-3406-8f0f-8aa0487e268e | -6.28944 | -43.65086 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e40468dc-d5fd-3975-bf16-a7c0a8985684 | -3.48268 | -54.73076 | 2026-09-29 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69074c8f-5243-3172-867c-f77a3f2e4ac2 | -7.46367 | -45.80186 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa119c99-12dd-34c2-80d3-ac5c81215686 | -1.05755 | -53.59075 | 2026-09-29 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e262cd58-1fa7-3507-883b-8d98a62d16e0 | -6.75112 | -55.08859 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9083a62-4268-386c-8181-31b7070f63bf | -7.83387 | -45.81865 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 66be2126-eae0-3f1f-b0ab-ff843f679b84 | -8.72907 | -44.92585 | 2026-09-29 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a5a6d1e2-0615-309b-98af-efd73899e273 | -2.86606 | -54.11651 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0d8fb22-a7d8-3d61-b1cb-a6ea88de0087 | -5.02926 | -43.56816 | 2026-09-29 05:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 93f3f57e-9bc3-3045-b1d7-978f35e927f5 | -2.89445 | -54.11013 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b198862b-faa7-3df9-9f35-286c65ad9fe2 | -7.69174 | -48.86332 | 2026-09-29 05:10:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83b24083-e0c2-3b89-9671-fe88bad24e32 | -4.49641 | -49.64253 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c48e195f-9c0f-3ff6-91ba-387f8edc98bd | -7.67303 | -44.89335 | 2026-09-29 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc6cd942-1493-39bb-93db-848c3425a500 | -7.51448 | -47.33841 | 2026-09-29 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e9eaca9-faff-38df-91e9-6ab78e5476c0 | -5.02851 | -43.57341 | 2026-09-29 05:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| db26372a-f41d-3b70-9627-4cc197250289 | -3.1573 | -54.08257 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8eb4b7d8-1484-3e57-96af-6a59cbff03bf | -5.73429 | -45.03688 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23d53e2b-265c-3ebc-a307-62ebd3de419f | -3.59318 | -50.6813 | 2026-09-29 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cb8064db-5a7c-3701-a370-34a5cba1413b | -5.48349 | -45.30735 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e746754-635b-39bc-a7de-95044eca37fe | -3.14669 | -54.08456 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b1e92b0-dcec-31e2-9e3f-178f8535d7b9 | -3.48323 | -54.7273 | 2026-09-29 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc62f7e5-481c-3754-ab6c-24751954fcee | -7.82824 | -45.81828 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8a60bf9b-bd1a-3d47-a56f-30380f53691a | -6.28445 | -43.6387 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |


[Clique aqui para ver as próximas entradas](README57.md)
