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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 163329e2-faaa-3996-af26-1661faaa751e | 0.14194 | -60.40078 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8079aa8-25d3-36b8-b8fa-b54186f4f06e | -6.79228 | -58.99364 | 2026-08-31 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0f80dbc-4fab-3068-9371-f87322d459ed | -6.41855 | -58.2275 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5d39f4f-54e2-35a7-b39c-6f42ac9c9140 | -4.92577 | -55.76946 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745bf8e4-65c7-3383-b90f-2edcdbe0e7b6 | -6.25079 | -55.43454 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8dbf4f9-249c-3ae3-a278-ef752219e70b | -3.79838 | -59.61065 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e891fccf-e525-3cf8-8125-a18e8f981151 | -4.15368 | -60.69883 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19b6e582-39db-31df-9ce2-ea21168e716f | -3.87244 | -49.10927 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 054a342f-2548-3106-9b37-068e057213d3 | -1.59605 | -54.40668 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a29e60b5-aa56-3ab4-8e8e-33ec3abcc95d | 0.13801 | -60.39775 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 505fb2aa-baa5-394c-aac5-73f0183f96b2 | -7.05612 | -52.71925 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 736de01a-f775-3c0d-b8db-c1a6479c8786 | -5.88068 | -57.76815 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a86fac4-4781-3484-8595-65a17646f010 | -3.11136 | -61.22617 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60dc982f-ef8e-362d-9873-990ac8ef170a | -6.61309 | -58.5973 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8a54115-7971-3813-98db-ff65dd916d0f | -6.12814 | -57.67472 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 96b8411c-f583-3197-85d7-f796857c5ce7 | -1.59667 | -55.04849 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6cd5bdb-117f-3ec3-850a-e8630ce07f82 | -6.59868 | -58.59891 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3e9ad7d-5f2d-3565-90e3-bf1d21056ce5 | -6.93224 | -55.64382 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e15b79f-0ffa-3f17-8b31-16bd86b2fe1d | -5.88546 | -57.76082 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d08595dd-318b-323f-8159-3899432ce622 | -4.85318 | -55.82642 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9ad8812-dc28-32fe-8bdb-f912d0774bb2 | -6.26568 | -55.41829 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21318cae-af49-35a0-9096-a4360b795cde | -4.29011 | -59.94751 | 2026-08-31 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aec23d6-7169-3cf3-b7af-2d123f48c1b1 | -3.63261 | -60.54799 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e12923b-9f17-36ce-b2ce-73e5b78e955f | -5.9427 | -57.69001 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c11120e9-3788-3036-9281-1368b8d7b06f | -6.12053 | -57.68675 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94f61975-62fd-39b2-b84c-cd9195e91d2f | -6.74048 | -56.33796 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2e0d477-fee7-30fe-bd2c-7d426afdaf5f | -6.15882 | -55.96112 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 188cee98-127f-3f49-acf7-6d0a0d48d7b7 | -6.25408 | -55.41674 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22c8dbc3-e716-360c-a1fd-46f1fe4c2a6a | -3.40709 | -50.12612 | 2026-08-31 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 372deeaa-89b3-3c09-b545-f75d8b19e8c3 | -6.61191 | -58.60485 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 01ab60db-87f4-3ded-83cd-a45f843bcefa | -4.85949 | -55.83741 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1858d485-1a49-3934-b839-53e138020267 | -4.15256 | -60.70578 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0268587d-ea83-3118-ab69-b72487f3c709 | -1.24875 | -55.70104 | 2026-08-31 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69d2fd1b-37c7-38ce-86c5-3ec73053fdcf | -5.89674 | -57.75848 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ae860c2-7f51-31ef-bbac-4f42fa80b6c2 | -4.95687 | -55.85516 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7559b8a2-91cb-38fe-b2f8-46c95041af10 | -6.60904 | -58.60053 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6b44c045-1236-3a88-87f9-f74a4c779cdf | -6.25186 | -55.43136 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 238aea92-80be-3509-acf4-ee0aca1cf281 | -7.29396 | -52.36919 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4c67ee4-7f82-3f30-a1c4-3d4fac5b30dd | -5.85823 | -57.55773 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 21452384-ddc2-38b2-9df2-90dc7fbdb685 | -4.14702 | -60.69778 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32577a71-9c9c-3fb8-9d8d-6013a89d955f | -4.15146 | -60.69135 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f7cf383-74c1-36ae-b093-8dfaf79531ba | -4.14923 | -60.70525 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50ba1683-5bf2-32ea-b34b-f998c2c5f0ea | -3.62985 | -60.56535 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 608b4afb-5970-329a-8a23-493123e57145 | -5.94332 | -57.68599 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90e954d0-d276-3bf1-85af-0b3d206ae034 | -5.4854 | -57.14474 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72821fb3-5434-3eb6-af6f-a854efd1db4b | 0.19403 | -60.50237 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e4d72cc-0857-3ba0-b72d-8170a76a1589 | -5.89025 | -57.7534 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42bf7786-44da-37ce-872f-175f8f03bd34 | -3.61016 | -59.07124 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 256bacbc-299e-3cf9-bd7a-4bb946189fde | -5.48969 | -57.14108 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 162850bf-d98d-34bf-b3e2-89536c166c77 | -4.14979 | -60.70177 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73fc08c3-6aaf-3986-af55-16d21e706faf | -3.38764 | -61.35798 | 2026-08-31 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac03d335-9df2-3738-9a5f-b482da79ce38 | -6.68085 | -58.74564 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6073112-a00e-3686-8466-abb11ede1bf3 | -6.25132 | -55.43085 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55a9a330-0dd9-39bc-b684-c3bb56d58c00 | -4.15811 | -60.69241 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a305ce3-34d9-3e26-972f-6ffe919a389d | -6.77425 | -55.67472 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be33d46a-877a-3eb1-b550-45ca408b9b70 | -5.48905 | -57.14529 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed6a4e37-4afc-341d-8da3-e803da70a0ad | -6.26622 | -55.41454 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55b7917-2976-3754-a505-00a7bdcccc3a | -3.19188 | -61.15477 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87a8a6ad-6b8d-300b-948e-5cfbfd424035 | -4.95837 | -55.84536 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc2390aa-ef85-34df-ab70-b37bc6f26236 | -4.96153 | -55.85081 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e90757d-fcc5-3969-88ed-9aa79d2f00b1 | -7.05655 | -52.7199 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 684d11cb-f733-3062-982f-a1e26d25238b | -5.25402 | -55.89512 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a409f5d6-fe99-3704-8aaa-efdb7038b916 | -4.8517 | -55.83617 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c43d023-fa17-3311-b6d9-06a1382a91a2 | -6.15035 | -57.88831 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4df198a-4d65-35f3-a490-bbd5a53b2c9e | -4.15201 | -60.70926 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05b5e16f-d6ad-3339-83a5-44ab50b594f1 | -7.29001 | -52.36009 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 924f7b9f-8c54-318f-af94-59a6c495df83 | -4.15756 | -60.71726 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49670f25-4754-3595-8952-567a72a35850 | -7.28963 | -52.36284 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 803dd12f-3638-3c51-9b3b-e60e3738e7b4 | -5.9576 | -57.68812 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b54eb15-70d4-3990-af61-503841189ee2 | -5.48777 | -57.15374 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe7f5bcd-286f-3876-add6-7d39f4a75da3 | -6.25344 | -55.41619 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2894cd0-0953-3b5e-8012-d7272efa6272 | -5.94565 | -57.69461 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 25c167fc-1690-3533-a18e-463d2c3fca7f | 0.01035 | -60.60093 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59ea9a90-85b1-35fb-bdf2-694b79c2dc78 | -4.36976 | -55.43691 | 2026-08-31 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 574dcba9-7645-366f-a732-41f270891eb1 | -5.88814 | -59.98198 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eccba236-aee5-35d2-b3b0-d735a8096352 | -5.87172 | -57.77906 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1b434bc-d213-3837-b143-921ce7d36c4e | -5.48411 | -57.15321 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 697efe17-3678-3232-9235-01919d2dc1dc | -4.96469 | -55.85627 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a3d44f1-95e9-308f-a54c-c8b220db59f3 | -1.39593 | -60.33153 | 2026-08-31 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8c4c79e-3027-3865-9306-162eb43fb9a8 | -3.6304 | -60.56187 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d2174e7-00c9-3c49-8e83-475667ac10e8 | -5.24695 | -55.88899 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0b3e1582-a418-3f74-9b18-de1dd00d20e5 | -3.96996 | -60.02412 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f86108af-639d-3b8b-a2db-1d5600188fe2 | -7.00476 | -55.87824 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69b5d997-ae52-32df-9d43-79b504db06a8 | -3.62929 | -60.54747 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1ce3780-01be-353f-a86d-54726418a04e | -3.92024 | -61.32084 | 2026-08-31 05:33:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89dc7502-1f88-3279-9385-8bfb0adf7077 | -3.88675 | -59.39675 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03fabdcf-0787-396b-a403-d76c3c1b2cdd | -6.7778 | -55.67881 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0944d535-032f-33c2-a9ab-824b336db45a | -6.11317 | -57.71057 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 140cc5a4-b18a-372d-9fff-7a0bf2a90064 | -1.44152 | -60.26007 | 2026-08-31 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b093d13f-74c3-3096-8f6d-e5df99d25a67 | -4.96544 | -55.85137 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b14e13a-0ca0-3171-ab0f-cd778fcbabef | -4.15312 | -60.7023 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 846814e7-c149-36d9-a943-0ea6793895c7 | -3.62208 | -60.54989 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57ed33e4-8395-3e53-8d70-85ad3c2c8f3c | -5.89318 | -57.75795 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a58cbc5c-1cf2-3a93-b02b-b7b8a4010aaf | -6.17465 | -55.44542 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d657c59-3858-3262-b1da-ade7754fdfaf | -5.5787 | -60.23199 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cff46e1c-005c-3fa3-8727-d4ae98c5efb6 | -6.79172 | -58.99733 | 2026-08-31 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4c899d5-3d59-3132-8a5c-afe50b06accc | -6.07803 | -57.88997 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b056334c-5d54-366f-b4d5-c582d1c36602 | -6.26106 | -55.42132 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 426ea393-bbc6-3d2b-a705-07d551e23603 | -6.28065 | -53.33548 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 305f8706-cf3a-361f-99d6-c6a58a02315e | -5.25106 | -55.91484 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |


[Clique aqui para ver as próximas entradas](README58.md)
