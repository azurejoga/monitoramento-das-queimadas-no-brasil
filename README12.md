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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15f35d16-6b67-3561-8dc9-856e6090ad81 | 0.43803 | -51.06028 | 2026-10-05 04:00:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3d32978-f2e4-37d7-b76c-50941b07227b | -2.47576 | -48.04101 | 2026-10-05 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 300a423d-0323-38d9-8935-8a40a8887fa6 | -3.24486 | -44.36985 | 2026-10-05 04:00:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26f0ef83-ed98-370e-ad2b-3ec4df1c4838 | -2.75726 | -45.54965 | 2026-10-05 04:00:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 891ec4e2-4ad3-3ddb-b6cf-424704003a54 | -3.11901 | -45.19145 | 2026-10-05 04:00:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7658223-8140-361a-adb6-3992ce74db3a | -3.71072 | -40.34492 | 2026-10-05 04:00:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6002fff4-c657-32c3-976e-3ef3713cc141 | -3.94845 | -40.93218 | 2026-10-05 04:00:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e876196-5a59-392f-895b-d400e0263672 | -1.87266 | -50.60512 | 2026-10-05 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f3f028f-a4f0-3c6f-9dee-ff9ce7ce7521 | -1.86757 | -50.60656 | 2026-10-05 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 89fe64bd-54d3-3257-8b73-a7188da11426 | -1.1792 | -49.2593 | 2026-10-05 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f469f9be-b46e-3137-9406-df7fd7188ac0 | -2.75794 | -45.54544 | 2026-10-05 04:00:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2926ec-bcf8-3b6d-ac3d-747127696e44 | -2.59312 | -48.95235 | 2026-10-05 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5746247-ff3a-3a99-8f04-dc3a72292ded | -3.16891 | -41.40033 | 2026-10-05 04:00:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73cee4ca-ff5c-3a2c-9d98-6aee590eaf34 | -2.67612 | -49.03268 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 76463248-0db8-3b6d-8609-ee4e70ffe6bf | -4.11455 | -49.07731 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b1012ad-07e0-36ab-9b4c-f87860af12fe | -2.85002 | -51.29481 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05517f6d-c051-3462-ae68-d96e5dae9519 | -3.80454 | -47.4877 | 2026-10-05 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6769cdd6-7465-3015-8b79-39414ea38471 | -4.07709 | -48.95703 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3e5a4de-852c-3253-8242-b44791078cf3 | -3.47501 | -50.09372 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a1f6b15-0ea4-307a-9449-e9e28d4e7e75 | -3.84361 | -50.30798 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6cee9f10-3358-3ae9-b297-97e19c1a36a2 | -5.99516 | -53.64089 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7f199b4-f556-3591-b458-b4c42d112f3f | -4.28755 | -48.56712 | 2026-10-05 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4edfcb53-9234-36ac-9e0c-1b12cee63935 | -3.27957 | -50.01485 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccf94cde-6a3d-3643-9d09-06f3862b6404 | -3.84212 | -50.31649 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 97cc2433-3318-36f7-bc49-6f985e43a0c9 | -7.18239 | -42.00467 | 2026-10-05 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1edeb97c-8385-36c3-bd36-ff377b04b83f | -7.32864 | -44.366 | 2026-10-05 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ca90dd7-fb32-3f4c-9cbe-c794d988aa1c | -3.06734 | -49.53952 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3711a3be-a151-32e7-9167-4b863325e11f | -11.32663 | -42.52361 | 2026-10-05 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 838e5978-644c-3649-8f90-a7d88731f683 | -6.60729 | -37.89563 | 2026-10-05 04:02:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1caf99c-051d-3889-bfcd-f368e3878ad0 | -3.8429 | -50.31204 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7bc8979f-8f9e-388e-b216-24a7b1b6e6cd | -6.85815 | -41.64076 | 2026-10-05 04:02:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f4377509-3bef-3037-b7a0-e3474b1bd761 | -5.95776 | -41.31139 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| fc7b5edd-91c8-3764-8abc-a08ab7fcf5d5 | -6.92664 | -43.67826 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7f7ad8a8-3282-3f23-bac1-ed75f8cf6c1f | -5.11139 | -37.44521 | 2026-10-05 04:02:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae21494a-5c7f-3b77-84df-2d576d11404a | -6.61451 | -41.56517 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fa002403-f0fb-3852-9b8b-145385159b70 | -3.47006 | -50.09416 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5c3c254-f269-3193-bced-8f4fd71ae2a9 | -7.17842 | -42.00782 | 2026-10-05 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 43dd9a9f-ff18-37af-9916-1c82ac76c7b0 | -3.84732 | -50.32155 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6f67280-42d5-393a-900d-ead5d7872e1e | -6.91004 | -43.66379 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85bf9072-bb69-3bb2-8d3f-6a5f55c0496b | -6.90867 | -43.67228 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bb0aefc-7030-3e91-96e0-3fb175e75789 | -9.79814 | -44.78994 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a08f7bed-dd75-392f-814f-d05cb5ab956e | -6.06507 | -42.91428 | 2026-10-05 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4ca200b0-7042-3e68-9ad2-5ed3abb37fd0 | -7.72618 | -45.46379 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b715a77e-c662-3cb0-a913-3e318db0f0b7 | -2.59731 | -51.8507 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ee187ec-2c87-3ef6-b5f7-9b5cda07c458 | -3.7084 | -50.64331 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56c8bb7e-ae51-3e62-aa4c-ef934ea11d86 | -3.70532 | -50.66106 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0680e1a1-265e-3a13-a800-617c0033d024 | -6.91733 | -43.66502 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e81a25c4-85bb-300c-b3fd-5bfab1874485 | -2.68193 | -49.03413 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c90e5629-5230-36de-bc7b-b440d102510a | -3.6992 | -50.66037 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac6eb6e7-9a56-396e-a09c-0c1aab482054 | -3.84887 | -50.31274 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 551b9bb0-6ecc-3bc4-84bb-28d49c9631bd | -2.85738 | -51.30064 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bf1e713a-eafc-3e26-94b6-b944340512fe | -3.07744 | -49.54918 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54acb9fd-8a14-3493-8a41-7aa7ed5bae4d | -7.88576 | -44.19344 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33241d7c-fcb2-3561-84b0-3d975f050cbf | -6.89339 | -43.67415 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57f3d544-c5dc-3320-85a7-67d1d9fbb6cb | -6.90572 | -43.66741 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2dac1a2f-284d-3d9f-b064-f9738efc4654 | -5.9965 | -53.63369 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27f35f39-7751-3f5b-8248-78aff3fd5e62 | -3.84576 | -50.33046 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a1926a26-03fe-3c10-b67a-281f2c0dfcd2 | -7.71877 | -45.45893 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a79cb2da-d418-3eae-8100-6d8c5ebf3194 | -4.28565 | -50.27555 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4668cb4d-63cc-335c-b7d8-c89a830e34af | -2.84916 | -51.30006 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6e506760-eaec-3787-94e5-908e4f94c0fd | -2.58121 | -51.86539 | 2026-10-05 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80887c74-f0ec-37a4-9348-99b5789a7a0b | -6.89565 | -43.68333 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 003e4fcb-c00e-32f6-8cd6-c332b637532f | -3.46936 | -50.0984 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98a6ef2d-99e2-39fc-9f12-54aeed496630 | -7.88947 | -44.19402 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2f8c975-4108-3742-9457-65b9f1ead9e0 | -3.70498 | -50.65423 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f95ac112-8aba-385e-b695-e0d0564773ee | -3.47522 | -50.09942 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab09f89d-4366-37dc-af4c-6576a1201e5b | -4.07939 | -48.9579 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6477e25c-a7c8-3880-be62-eaaebef8a132 | -3.79443 | -50.8019 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd1f1774-8743-391b-896d-26397bc58f40 | -6.15681 | -43.63454 | 2026-10-05 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82d8caf3-0608-35c4-8308-041a94e9a537 | -7.88503 | -44.1979 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7de9ac8-92e9-3e6f-a1dc-9836ef879aee | -4.11395 | -49.08083 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85760f29-b72b-3baa-ae82-c8ccd0b82c6f | -6.91665 | -43.66927 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeba4fff-86ea-3548-9b57-ebff3020c69a | -6.17453 | -52.93116 | 2026-10-05 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d838a314-010b-37b9-83b0-dcec80ce91d7 | -6.89861 | -43.68823 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46a68b0c-2656-3c53-999c-f16ed4a0f91c | -6.89931 | -43.68392 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 93f000a6-088c-39ef-bba3-22c566035e5d | -4.30911 | -50.78638 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ff5b9131-f321-3e1f-9ab2-8712973e5abb | -7.89318 | -44.1946 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6faf083-3543-327d-b350-029d725427ba | -4.84478 | -40.40602 | 2026-10-05 04:02:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c6e2073-d18a-318d-9ad9-3f4721afb4b9 | -6.91391 | -43.68628 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0208f74f-3389-34c4-9880-29e2d288ad08 | -8.22595 | -50.21783 | 2026-10-05 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1dd8fc4-1429-3c1b-8739-912d2e3380db | -3.71029 | -50.65976 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c92aeac1-4c7f-3494-9fdc-a320ccf679a7 | -10.96244 | -45.42619 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f8e16be-58ef-382d-afc6-88bf29ed0974 | -6.9455 | -42.67503 | 2026-10-05 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87fa3fd2-7d85-3605-b136-49ae66028d9e | -6.20887 | -45.40413 | 2026-10-05 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ce0db51-c8e7-3112-92e9-384813fb9234 | -5.95385 | -41.31442 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af3f3783-9359-3626-b5a5-4e58aa3e6962 | -7.11165 | -37.60308 | 2026-10-05 04:02:00 | NOAA-21 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 12d3db2d-60fe-3bab-bbaf-40934c2f316c | -6.43126 | -43.72322 | 2026-10-05 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fdeced94-ad80-3bb2-876b-10a18d3ffaea | -4.11513 | -49.07386 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74cb17ba-9869-3b27-9927-16e603e72eef | -9.43685 | -40.50094 | 2026-10-05 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7764d348-e731-3130-9543-82baecd50b7d | -3.71252 | -50.64632 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7dedc47e-5f5d-371c-a5e4-bf7448e1ec06 | -7.71816 | -45.46249 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80a2983b-d297-35ba-8d59-dc66cc900ed9 | -4.28711 | -50.26728 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5496ebc0-c979-30a5-8c5b-69914fec43bd | -2.68105 | -49.0372 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c88dd484-a937-3892-8e06-3db9e9b8f7ee | -5.94993 | -41.31746 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0caeed25-4867-3644-b2d9-a6a1dd7fc72e | -6.65254 | -43.77069 | 2026-10-05 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 040e88ab-2978-3ead-a215-23335642402f | -6.42757 | -43.72267 | 2026-10-05 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7433f170-a45d-34c0-901f-a23d6532cdc8 | -6.89409 | -43.66987 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94c4ec72-587d-31a7-b7fd-18c61aee976f | -6.90799 | -43.67652 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26ae8b85-455c-3995-808d-87d369d5ea79 | -6.92553 | -43.68385 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ae10e95-e631-3ecf-bb93-2e11ffc38d37 | -6.87879 | -43.67187 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README13.md)
