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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faf07a8d-fac4-38e0-9b95-3e729d4995e7 | -14.15928 | -46.15947 | 2024-10-29 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ef91307-9162-37d6-ac66-ae4adf135d66 | -7.21795 | -45.52866 | 2024-10-29 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90b57f32-b220-3680-bf52-93920c71644a | -7.95656 | -45.68965 | 2024-10-29 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d0cbede-d216-3e6b-955d-77d44a6d6bc4 | -7.95604 | -45.69258 | 2024-10-29 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caddb083-d87e-3b78-b683-0926f40eb412 | -7.86125 | -46.26204 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fbbdc75-de85-3364-b6cb-67f3276d828e | -7.85712 | -46.25446 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f3094e3-2236-3367-9de7-b4c65fc55e96 | -7.85654 | -46.25776 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61ec6266-b29a-3565-a577-6d79d4be402a | -7.85595 | -46.26106 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ece39233-bc37-3c82-b196-02a906f8a829 | -7.72539 | -45.71571 | 2024-10-29 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd98ea6c-3642-3b31-818f-477a268fdf58 | -7.72485 | -45.71875 | 2024-10-29 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98e119b9-ce04-3e9f-9df6-9af3dc45356a | -7.60493 | -46.87478 | 2024-10-29 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d66d82b-f0e1-3bab-855e-0f4775c1307f | -7.60427 | -46.87845 | 2024-10-29 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66edc071-9177-3b82-b385-f2b1f83a6556 | -7.59809 | -46.88099 | 2024-10-29 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7ba428-4488-3f31-8b9f-ef310c291b4a | -7.56857 | -46.44628 | 2024-10-29 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6169d72-2515-38d9-9c60-e161f1919ef1 | -7.56795 | -46.44973 | 2024-10-29 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 158665ae-61bd-3d60-8be3-49c205c26238 | -7.39042 | -45.6869 | 2024-10-29 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b840bab6-e654-33cf-9348-1779c8ce5b54 | -7.38988 | -45.68995 | 2024-10-29 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a91fef0-1c0d-38c1-9eb3-10632c524ed7 | -7.2571 | -46.07832 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34ce8b62-3093-32d1-bdfb-08a7bef83bf9 | -7.25652 | -46.08167 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d362a08d-52c3-3015-b467-ad616132d5df | -7.25618 | -46.07654 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d6b56f5-c1a9-3560-92dd-a26535ba03fa | -7.25557 | -46.0799 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9835d58-e678-3dc7-83f9-b14710b8005a | -7.25183 | -46.07727 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03cdd069-b9a0-3e85-bba9-8d335eadc4d2 | -7.17477 | -46.32812 | 2024-10-29 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d17b78a-4027-3103-9b9a-06b1b5361bd9 | -7.17416 | -46.33161 | 2024-10-29 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b4da1f7-3fa4-3fee-b305-09586c9fd0a4 | -6.9501 | -46.31599 | 2024-10-29 03:49:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2c2d3cb-b685-3191-9773-937cd73cb875 | -8.99486 | -46.76259 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f4a56d3-a3c5-3d8f-bad7-8b467a267d27 | -8.99011 | -46.75824 | 2024-10-29 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5f85f37-762e-3981-8d29-2037c064ffcc | -8.23219 | -45.84435 | 2024-10-29 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5099743-0689-32aa-94f8-bad73cfe33b0 | -7.46998 | -47.18834 | 2024-10-29 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cafc57c5-8be3-309a-8caa-713971a65bff | -7.46503 | -47.18331 | 2024-10-29 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ea54be8-2884-3b84-9dd9-c23d2834809e | -6.98685 | -47.08907 | 2024-10-29 03:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4afda6aa-e606-3e39-b7d4-191d66791fbc | -6.98189 | -47.0841 | 2024-10-29 03:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce2603ee-b308-3529-b39c-4fe7915a2a95 | -6.98118 | -47.08802 | 2024-10-29 03:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50337e8c-14f5-3142-94a1-d0ae20aea365 | -9.10213 | -47.65892 | 2024-10-29 03:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 750e4315-3b96-3c8b-9070-bfd1e1f49d26 | -8.663 | -47.86657 | 2024-10-29 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 146f4586-cb3c-34bb-802e-d5e9d1eb71b3 | -8.66297 | -47.86473 | 2024-10-29 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddfd4a14-0a1a-3e08-8d41-3e6bec6ebcb3 | -8.66225 | -47.87069 | 2024-10-29 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51304997-84c6-3697-8ec4-dbc4989ce524 | -8.66219 | -47.86887 | 2024-10-29 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 513b06da-9f21-34a2-b725-e6d69b73d968 | -8.46971 | -47.80998 | 2024-10-29 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c603ddd-0cb5-3545-8b07-5b6f5c551115 | -8.46895 | -47.81402 | 2024-10-29 03:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea6e6446-8b0e-3501-919b-b4ff72be991d | -8.74372 | -49.7891 | 2024-10-29 03:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6d7214a-566a-35c6-8cc3-d64f04a9bec8 | -12.09515 | -52.48785 | 2024-10-29 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf54134d-448c-35f7-ae76-eaaa0b443e5a | -12.08801 | -52.48621 | 2024-10-29 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ac40f86-b63d-3bea-a712-8ade88deb769 | -27.59509 | -51.31374 | 2024-10-29 03:51:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 46fa69f3-0701-3938-9458-7b42d37ee232 | -24.00366 | -54.13341 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 725f1b75-f30c-3efb-ad21-5784c68631c4 | -23.3734 | -51.10789 | 2024-10-29 03:51:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6f98e7fd-fe10-37d2-b212-6ce412efcaf1 | -23.2359 | -51.28563 | 2024-10-29 03:51:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 68e57bed-b841-3f5a-bb9c-ff938032fef7 | -23.23569 | -51.28543 | 2024-10-29 03:51:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 305202e6-5ff4-3c53-9417-72752f4849dd | -23.235 | -51.28951 | 2024-10-29 03:51:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b8c3759a-321a-3093-984d-a6b025fc5fb7 | -23.23482 | -51.28931 | 2024-10-29 03:51:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99a31c50-b493-3a3c-9540-71daa4fbbab6 | -24.00333 | -54.12653 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5789ae7f-a5ef-3ce8-9878-e379c2a031d2 | -24.86735 | -53.48288 | 2024-10-29 03:51:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 26400e70-e008-30ad-9ace-2587f99968d7 | -21.80514 | -53.49495 | 2024-10-29 03:51:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82b6fbc8-1753-3945-8191-f226d64fa622 | -21.80384 | -53.50034 | 2024-10-29 03:51:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d3e79b4-743f-3820-865c-64e11ee441de | -24.00505 | -54.12788 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0569b2f4-8cd7-3cc8-9e5d-f1cdb2db9b0d | -24.00198 | -54.13207 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| db3a2051-2de4-3984-9a07-369a1b66971c | -23.99883 | -54.12599 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 24b28f10-e002-3b35-8351-7f2a735b6c4f | -23.99846 | -54.11907 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 54098e17-0a9b-36ca-9739-d04f38b2d05f | -23.99744 | -54.13151 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 0d9d9308-a6a4-3835-adc2-9ab20ba47ec3 | -23.99711 | -54.1246 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 5c5460ca-07cf-3658-b2bb-d7775b54bd5b | -23.99575 | -54.13014 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| e90137e0-67c2-33b9-bac4-15860b51c4ee | -23.99399 | -54.11858 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| a9e44e4b-062b-3bce-a1f5-28b104b9e9d1 | -23.9926 | -54.1241 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 37c7dacd-6a0d-3c35-95df-bca773fa64de | -23.99089 | -54.12268 | 2024-10-29 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| f9a9594d-af56-3c89-821e-f437f1194bfc | -29.81472 | -51.17778 | 2024-10-29 03:53:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| a3222553-c593-3cd0-bf26-7224626e7a74 | -2.6481 | -49.2678 | 2024-10-29 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 367e444f-0377-3352-b74f-8573594cc66a | -2.6482 | -49.2465 | 2024-10-29 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 780931ae-5f57-3a2c-ae20-e0c28b925442 | -2.6666 | -49.2673 | 2024-10-29 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 978c6c56-15e1-302a-94b8-747c777b37eb | -2.6667 | -49.246 | 2024-10-29 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| a7911bc4-4a37-3eb6-ba49-74b9fc2adab1 | -2.8555 | -53.3459 | 2024-10-29 03:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 643d56f9-d7e3-3c91-8b55-b5eac230116e | -3.0501 | -50.4171 | 2024-10-29 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1c37c3cb-08ac-32dd-845f-e136d6654b13 | -3.0913 | -54.287 | 2024-10-29 03:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3f76af50-2143-3e2b-964b-f03b665a2d3c | -3.1097 | -54.2865 | 2024-10-29 03:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 71fdaa07-64a5-3f5c-8e78-b6b4d34edf96 | -3.1098 | -54.2665 | 2024-10-29 03:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ac6529b0-cfad-3d67-a1a2-56025d4d2cac | -3.1794 | -50.3922 | 2024-10-29 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d7eb5659-6888-3ecb-8455-c2277936797a | -3.2503 | -46.8709 | 2024-10-29 03:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 89f98a3b-e00e-3f7b-ba3e-4f896066e946 | -4.3473 | -43.779 | 2024-10-29 03:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 906adbee-672b-31c6-95d6-0b2981c9a38e | -4.3475 | -43.7559 | 2024-10-29 03:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| c15b2062-9396-377e-bcba-48003e08b26d | -4.2762 | -46.0956 | 2024-10-29 03:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 5e3135b3-17ef-3624-bc1a-3d425e71115f | -12.3331 | -49.9424 | 2024-10-29 03:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| df66f5b3-5ea5-35b0-9fcf-9d5897ad4b3d | -12.3334 | -49.9208 | 2024-10-29 03:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| bb7e11ce-bad2-3c37-8f65-c27525f29a36 | -12.3522 | -49.94 | 2024-10-29 03:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 3267474d-e3dc-3108-97b4-f062a323d9fc | -12.3526 | -49.9184 | 2024-10-29 03:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 337566a6-fbc9-3f5e-b661-35b80cfabbe1 | -2.6481 | -49.2678 | 2024-10-29 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 16852089-cc64-3608-bb9f-f92bc50e134a | -2.6482 | -49.2465 | 2024-10-29 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| a474c345-ecb3-3231-bf52-104890fafc83 | -2.6666 | -49.2673 | 2024-10-29 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 318313fa-14d3-3ba3-acb6-5936773546c2 | -2.6667 | -49.246 | 2024-10-29 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| edc2617a-2c16-3119-b16c-a15cc011b8c7 | -3.0501 | -50.4171 | 2024-10-29 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 640eb181-bc0a-3761-a375-51b1700e6b12 | -3.1097 | -54.2865 | 2024-10-29 04:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 8ffec348-d40f-35e9-93af-63d82028093d | -3.1098 | -54.2665 | 2024-10-29 04:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ca3e635f-a4b0-38c4-b644-c639ff4dff0d | -3.2503 | -46.8709 | 2024-10-29 04:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 4557b8ab-4e4e-3140-a58a-da92dc1d0686 | -3.1794 | -50.3922 | 2024-10-29 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f0e0c0fe-fea4-36b0-ba88-eb5e39aed5b0 | -4.2761 | -46.1178 | 2024-10-29 04:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 9d3c8274-13d1-3b14-95f9-aea5931b707e | -4.2762 | -46.0956 | 2024-10-29 04:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0407542e-527b-399f-8374-627ab337c9e3 | -4.3473 | -43.779 | 2024-10-29 04:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 883c34cf-bf1c-3e78-80aa-ed6b96353cb7 | -12.3526 | -49.9184 | 2024-10-29 04:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 85e9cfae-7a1c-31bf-91a6-5b3ec733cb5e | -12.3334 | -49.9208 | 2024-10-29 04:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0866eafa-49bd-3a98-971e-f91d01b68ce5 | -12.3522 | -49.94 | 2024-10-29 04:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 5f0b906d-ee7c-3082-964e-a04759e75d37 | -2.6667 | -49.246 | 2024-10-29 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 86434210-7a7a-3899-a85e-5fc8f7e88cfe | -2.6481 | -49.2678 | 2024-10-29 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |


[Clique aqui para ver as próximas entradas](README34.md)
