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
| f84566b9-c4d0-3dee-a3d0-596493f137b1 | -7.57435 | -46.4852 | 2026-01-06 04:31:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 87ceeddf-7e40-322a-9a2d-aaa0c2fce662 | -3.70469 | -46.97128 | 2026-01-06 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6f07eac-de09-352d-acb2-a010028f012b | -3.18264 | -51.0841 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cead2657-9bb1-3bf8-b59b-4df5023da477 | -7.29244 | -35.17945 | 2026-01-06 04:31:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d55d1c86-e2b7-3ff6-8932-398b15bed0e8 | -5.6629 | -46.22872 | 2026-01-06 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bbd7a28-f9c2-3f95-b2b6-84a2e17371ea | -5.66235 | -46.23219 | 2026-01-06 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 500e3a2e-cb46-318d-bcb7-4e23fda2b44f | -10.14335 | -36.41721 | 2026-01-06 04:31:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2cbb3c97-f6e0-341f-97dd-2b1e8b27f5ef | -6.95931 | -46.22347 | 2026-01-06 04:31:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15ed4ab9-334e-30c1-bfc9-7ae77c975443 | -5.48416 | -45.43444 | 2026-01-06 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbb85e02-9463-3363-82dc-dd6ca6c30b8e | -8.43548 | -35.57708 | 2026-01-06 04:31:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 57218c3c-8d4a-3c97-bd79-c48a8ffabb90 | -4.39618 | -43.5733 | 2026-01-06 04:31:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5ebe174-4864-3010-8226-690093126c0e | -4.12459 | -43.88717 | 2026-01-06 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 381abd52-d035-3758-8d2f-09a0205632c6 | -3.18202 | -51.08783 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba2aa2e-0e78-3c0d-854e-9c43f38c3154 | -10.93152 | -38.81789 | 2026-01-06 04:31:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b66e8bdb-1fb4-35a3-9e4d-3ae3830b47cb | -14.92288 | -59.90538 | 2026-01-06 04:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1f3ce11-1e6a-3824-a6dc-6c39abf97dd6 | -16.59933 | -58.21778 | 2026-01-06 04:33:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8289afcf-666d-30a0-a411-25f2dae50a30 | -15.61912 | -57.33783 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3567f8ee-7379-3b30-b976-bdb0af6ac3ed | -16.04119 | -59.21868 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b9034c-e62c-33c8-8c0c-2064fe3c0194 | -16.07167 | -56.58918 | 2026-01-06 04:33:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8174f41e-1d81-3ce8-ba13-b5720c1db00d | -16.04474 | -59.22625 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 435f1c7a-7c33-3b03-8fe7-3e0329a508f5 | -16.59475 | -58.21328 | 2026-01-06 04:33:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8aab2b2e-360d-36a5-895f-e780926458cc | -16.04569 | -59.22159 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c493231-5ea8-3265-99fc-fe86d3ece687 | -16.00739 | -54.78368 | 2026-01-06 04:33:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b98e078a-3fc6-368f-b46a-318b8e63a413 | -16.04588 | -59.2246 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffb769c8-9ff2-330e-a90a-2dfe7638a2a4 | -16.60002 | -58.21446 | 2026-01-06 04:33:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 61dcc59e-2a15-3212-a6cf-c99040f53842 | -16.06161 | -60.07066 | 2026-01-06 04:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eb7043b-db9f-32c4-b42a-a854bab48aad | -15.62417 | -57.3391 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb6cf924-711a-3d58-a1f6-2a4da91a6138 | -15.68433 | -59.66068 | 2026-01-06 04:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40bab77b-01a7-353c-8105-f8463485f385 | -15.62478 | -57.33601 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 985e1a94-e7ca-3fdc-95af-14efc409e995 | -16.04089 | -59.21609 | 2026-01-06 04:33:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c04f4f2-d6d0-3931-87e5-72781f22474f | -14.92389 | -59.90067 | 2026-01-06 04:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca5f39f4-8f63-3faf-ad77-53383cfe1ade | -20.51233 | -58.01519 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c2613ee9-f07f-36df-bcff-b495b116bc09 | -20.51947 | -57.99184 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7172e423-6b0f-3cf4-8750-f88c3badc6cb | -22.91276 | -47.07939 | 2026-01-06 04:36:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9d754604-fdb5-39d0-8c55-c053081d94ad | -20.52317 | -58.01184 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f40f9f54-8274-3728-b5d8-1cb46266505f | -20.50984 | -57.98955 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 6f6d3070-5b9d-3975-944b-cfc3e88cf20d | -21.53645 | -57.53667 | 2026-01-06 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4cc4147e-8962-3c50-b7b2-efac7a7cc458 | -20.51834 | -58.0107 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0275a82c-72dc-300e-9a16-ace626f80fb0 | -20.51708 | -57.99268 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a3f45bfc-00d2-3cb6-afbd-7db75ec1ed85 | -21.53742 | -57.53193 | 2026-01-06 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 187cb0bc-c146-3549-afb1-aa30f0ef1d54 | -20.53517 | -58.00288 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 04e4f940-f5e7-3fce-9e10-19f088de1453 | -17.65141 | -56.4464 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 476b135d-c6d0-3056-8fb6-3bf896439d5e | -20.52568 | -58.01106 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| eae4392b-f1ea-3c71-849f-0a6a11146f81 | -17.64946 | -56.45641 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 24f70607-822f-341b-8548-cb40a59d0f0f | -20.51488 | -58.0144 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d76d18c0-7740-32db-8cbb-bf8f01b76e46 | -22.8634 | -52.28039 | 2026-01-06 04:36:00 | NPP-375D | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6103a420-e7f2-30e9-9c4b-79789927e623 | -20.53635 | -57.99725 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 322f6ceb-7419-3b33-8496-8311431a61d4 | -22.49392 | -46.94335 | 2026-01-06 04:36:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20769cc3-6f69-3181-b1b7-2d3bd83680f4 | -22.03243 | -56.30365 | 2026-01-06 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 933f817d-5d96-307e-8969-30efed64f68f | -20.52799 | -58.01299 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a964efee-4374-3965-bbd3-2ff877c7d590 | -22.49816 | -46.93946 | 2026-01-06 04:36:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb341f49-111b-3d17-a890-aff8126b0ea1 | -20.52086 | -58.0099 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c208efc6-8c2a-3b6b-b7de-44819a901f51 | -21.54107 | -57.53759 | 2026-01-06 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bd5324c-a159-34a2-8fbd-9c0ebc745f46 | -20.98912 | -54.4766 | 2026-01-06 04:36:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06343248-ef9b-3cb1-bf24-7a93c26127b1 | -20.98911 | -54.47938 | 2026-01-06 04:36:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30abae7e-657e-393b-a569-9b39e48d0d49 | -20.52917 | -58.00735 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 939e266f-7bae-3353-80ea-4360b4d1297d | -21.54204 | -57.53289 | 2026-01-06 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 060f8605-a15f-3408-ba5d-ae8ae4170892 | -20.51465 | -57.9907 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 706716b0-3196-314e-9635-2f6d6209f94e | -22.03651 | -55.51892 | 2026-01-06 04:36:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af6f7edd-e0dc-329a-825e-a57ae1ed8b56 | -17.65506 | -56.45239 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c1290d7a-c91a-35c9-91a6-00d0d62aa42c | -20.51226 | -57.99155 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0abe0ec6-be1d-363d-93b9-c404d2d5c711 | -20.5087 | -58.00842 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| deea98ec-c8ee-34de-90ab-7ea20dc6d052 | -22.02823 | -56.30262 | 2026-01-06 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a33e8b9a-49c2-3d23-a748-0addbe24829f | -18.54791 | -55.43461 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ba25a25b-97f0-3fa7-9412-3394d209e550 | -18.5471 | -55.43879 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f038549c-8fd9-39e3-aa88-c499a2c18fbe | -20.53399 | -58.0085 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2cf00038-1fe5-3fd8-8b1a-1e6d23ad35be | -22.49453 | -46.9389 | 2026-01-06 04:36:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f2adda4-4545-3094-bcc8-dab4e9d70436 | -17.65044 | -56.4514 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 55c97f2d-5012-3116-bd85-8eded653fbcd | -20.52429 | -57.99299 | 2026-01-06 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0ccdace0-ecf5-3dde-8e08-d003ff82e2fc | -25.4252 | -49.36801 | 2026-01-06 04:38:00 | NPP-375D | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 556a8ae3-94c9-33ca-896b-ee6c2196631c | -31.75401 | -52.98495 | 2026-01-06 04:38:00 | NPP-375D | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 42f4f9bf-a62b-3bc9-9008-c376ff6c54c3 | -26.20181 | -53.14949 | 2026-01-06 04:38:00 | NPP-375D | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ca094d1-f071-3fcc-b522-8b6c3aa9052c | -29.5466 | -55.47556 | 2026-01-06 04:38:00 | NPP-375D | MANOEL VIANA | RIO GRANDE DO SUL | Brasil | 4311759 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| baca1dcf-f1e9-3b2d-b8c7-4b753e1c3f53 | -25.4286 | -49.36863 | 2026-01-06 04:38:00 | NPP-375D | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be4f383d-b1c3-32aa-a5e2-bb1f9a7883d1 | -32.03408 | -53.54691 | 2026-01-06 04:38:00 | NPP-375D | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5f458276-6635-33d0-8dc8-d74a39c6f497 | -26.19838 | -53.14877 | 2026-01-06 04:38:00 | NPP-375D | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d7d38eb4-593e-348d-9163-4946f7dc2010 | -27.51408 | -53.68571 | 2026-01-06 04:38:00 | NPP-375D | MIRAGUAÍ | RIO GRANDE DO SUL | Brasil | 4312302 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f10d9294-2b8b-30e1-bfc4-08817bb36cb0 | -27.51065 | -53.68495 | 2026-01-06 04:38:00 | NPP-375D | MIRAGUAÍ | RIO GRANDE DO SUL | Brasil | 4312302 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf6e9291-c3da-34bc-b5cb-f3e7e18c7788 | -26.10287 | -50.17418 | 2026-01-06 04:38:00 | NPP-375D | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 16dc5a90-075a-3c76-8a89-417adee87d28 | -3.6962 | -43.4432 | 2026-01-06 04:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| cad0ec96-6776-31d9-b29d-23bd5e0ead00 | -3.6962 | -43.4432 | 2026-01-06 04:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 72403250-1032-3241-8aa0-d9fcd2741112 | -0.43868 | -48.59098 | 2026-01-06 04:50:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2010c8d0-2d28-37ec-9640-829d76232c1b | -0.43512 | -48.59043 | 2026-01-06 04:50:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e7bc714-e958-3da8-89a0-85f9c6dbbfae | 3.62147 | -60.79612 | 2026-01-06 04:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3a83667-4183-3ee6-b881-4601f0737fe4 | -0.36386 | -48.44456 | 2026-01-06 04:50:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a03da23-a492-30b2-ac42-6f049dd58316 | -0.08759 | -51.27933 | 2026-01-06 04:50:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6092eaf-94fb-3ee7-817b-4bc0709153d3 | 2.54548 | -60.5712 | 2026-01-06 04:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25ef8a60-a242-3553-be31-e41c2fa8f6b8 | 2.54608 | -60.57501 | 2026-01-06 04:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acdba7e5-039a-348e-b342-1029b385b547 | 2.54409 | -60.57318 | 2026-01-06 04:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e12bcfde-3eac-327c-84dd-c03de1254d89 | 2.83992 | -61.32621 | 2026-01-06 04:50:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d020c94-25d3-32e2-8bf0-d00c150acb8b | -0.09089 | -51.27985 | 2026-01-06 04:50:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7d524eee-1a7f-3446-a65e-8fb34b57f1c7 | 3.62205 | -60.80019 | 2026-01-06 04:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ffdcb66-5f0d-3773-86a5-c848ccc23433 | -0.36807 | -48.44106 | 2026-01-06 04:50:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d60eb8a9-fe05-39ff-a6ad-cbf87f99828b | 2.54969 | -60.57231 | 2026-01-06 04:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 875b1ab8-0501-3f87-9407-a3dcb9970ef4 | 0.11962 | -51.04308 | 2026-01-06 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 053ba44b-2c2e-37eb-b264-7ee6948bfb48 | -0.36449 | -48.44051 | 2026-01-06 04:50:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12fa0db3-d36b-300f-ad4a-52b4ad0dc257 | -1.03854 | -47.22917 | 2026-01-06 04:50:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff0c9968-60b7-377c-8a53-ffa0dc732f92 | -3.18335 | -51.09796 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f5c6139-2bac-39ed-a3ba-bf2994465634 | -1.97552 | -53.36379 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9637a82c-6b53-369b-9052-b6dbf49b0d26 | -1.45883 | -49.07998 | 2026-01-06 04:53:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
