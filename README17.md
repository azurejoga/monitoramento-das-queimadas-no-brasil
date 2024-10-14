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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00bcee38-0cf1-320e-ab90-b346b57e585b | -17.9445 | -57.3661 | 2024-10-14 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 634e5dfc-ceae-3324-b92b-88d412e0ed7b | -17.9449 | -57.3455 | 2024-10-14 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 6a1335bb-256d-37ce-88e3-95f1084bd21c | -17.9636 | -57.4049 | 2024-10-14 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 796ee143-42a1-39f3-b795-6bf002baf66b | -17.964 | -57.3843 | 2024-10-14 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 735e332b-1db5-37b4-9fa0-2332ce49be90 | -17.9643 | -57.3637 | 2024-10-14 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 512ec0c4-d737-3d95-a820-b49112dc358a | -18.0035 | -57.3794 | 2024-10-14 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 2a78b758-5db2-36ba-8fb6-f2974654fbb8 | -18.0039 | -57.3588 | 2024-10-14 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| d38cf1d9-e147-3775-bf3c-1a0ccfaae71c | -17.14428 | -56.86349 | 2024-10-14 01:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 6e72dca3-d56e-3250-b50c-77597758023c | -17.13279 | -56.86494 | 2024-10-14 01:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 11d8e5c0-f367-3efc-9b41-3a71ad9381b9 | -17.12131 | -56.86638 | 2024-10-14 01:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 49079e99-b027-3064-88ca-6deb9b2ff6ba | -17.08086 | -56.01724 | 2024-10-14 01:17:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 75fa2caa-a106-398d-a180-705e0f82d216 | -17.07924 | -56.00331 | 2024-10-14 01:17:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| 9ac12be3-d871-3213-b04a-eace5c0338f5 | -17.07579 | -56.01007 | 2024-10-14 01:17:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| db41c6aa-4a55-3b7d-98f5-63086d1f9032 | -17.07408 | -55.99621 | 2024-10-14 01:17:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| f44520d6-d0f2-339d-a5c6-fc35a95cb1fd | -17.06849 | -56.00471 | 2024-10-14 01:17:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 6bd121d5-4f75-34ef-95fc-5bc8c1ddd436 | -12.8865 | -53.54407 | 2024-10-14 01:17:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 67b68d53-3a4f-3bd3-ac01-21a0c88ef7e1 | -12.88524 | -53.53482 | 2024-10-14 01:17:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6c679675-d92a-37d1-a01f-89d9448ad195 | -12.87756 | -53.54537 | 2024-10-14 01:17:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| ac664e22-dc75-39e7-8bbd-2330c152efde | -12.8763 | -53.53613 | 2024-10-14 01:17:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 1d5ceabc-dc2e-33fc-9c59-e7069c635ff4 | -12.87504 | -53.52689 | 2024-10-14 01:17:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9b0e2e6c-205b-324d-9104-8ab27381f375 | -12.59777 | -48.57751 | 2024-10-14 01:17:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 6a8c900a-ca65-30c4-a4e0-91cea16f0e4b | -12.59574 | -48.56441 | 2024-10-14 01:17:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7d5c2707-48cc-33cb-8292-cff620e2134c | -12.50501 | -49.17228 | 2024-10-14 01:17:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 00f44aae-a17b-3fa9-9c8b-e3616b13802d | -12.33668 | -50.24538 | 2024-10-14 01:17:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98096636-498c-3bf3-8256-57608af1ff1c | -12.31768 | -50.24839 | 2024-10-14 01:17:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 74b9bbe8-1e77-3665-b607-dcb17dc594c6 | -12.31613 | -50.23788 | 2024-10-14 01:17:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 6ec8984c-5f18-3782-98e2-45355b28653b | -12.30662 | -50.23939 | 2024-10-14 01:17:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 45569bd9-2b35-3d61-9ee7-ea28011efb23 | -12.16067 | -50.6946 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 442c0f21-a5d2-316d-98a2-0c67edca3163 | -12.13426 | -50.70897 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 55e8098a-97f7-3c64-ae0f-bf56dfb7cfd7 | -12.13277 | -50.69895 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e0007d09-137e-3f0f-a87b-776dc1b539db | -12.12858 | -50.71615 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 62d7f2a2-5a41-3bea-8bff-2204b1517f35 | -12.12713 | -50.70613 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b78e0b16-c4c4-3c52-a9d4-0ef021007023 | -12.12567 | -50.69609 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ce7c5783-1585-3891-9489-b49313e4d81e | -12.09776 | -50.70045 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 020e0954-4f56-343b-bf4e-503fb61d6165 | -12.09628 | -50.69041 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 41.4 |
| c90d2492-faaa-30e5-99de-bef51d514592 | -12.08845 | -50.7019 | 2024-10-14 01:17:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 19854a32-9b99-38a7-83bd-49f5061b79ff | -12.04336 | -51.0876 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2dcbe837-3a96-3223-ab1a-8bcef1e84229 | -11.66402 | -52.63238 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0e2db642-67c9-391e-8a6a-7c2578db7e86 | -11.66276 | -52.6234 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a3cc507d-b27b-3996-87eb-022a474f7f28 | -11.55833 | -53.86368 | 2024-10-14 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 24412a7b-7609-3d67-89fd-9d8d1aefa156 | -11.55707 | -53.85446 | 2024-10-14 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 36c8cccb-80b0-3986-bff1-1e333236845e | -11.54686 | -53.84657 | 2024-10-14 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 474ef95c-74a2-3dc6-a383-1c19dfb7a2cc | -11.51024 | -51.80162 | 2024-10-14 01:17:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d00decb-4e1f-3a33-a32e-59bfe28bd191 | -11.40115 | -51.23931 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 285d8ee4-459c-3d21-8eff-b32f72b9b5fd | -11.35321 | -55.20546 | 2024-10-14 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3e1f1140-0c61-39fe-a3fe-096718a0aa71 | -11.27349 | -51.4375 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ce1d7b7-cc80-3221-87d0-756f11f9e0e8 | -11.2674 | -51.33096 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1c9e1e9f-fa52-396e-8621-c090ad7846b5 | -11.2644 | -51.43888 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2af2e564-841a-32a4-a86e-ba3da3725eab | -11.25828 | -51.33235 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f9c08647-1fd5-3594-a0c7-bfd95e9fb2e7 | -11.25689 | -51.32275 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 127c8344-76c6-3318-b45f-e7ddfa0beb63 | -11.24915 | -51.33375 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ede681ca-29c7-3908-8c9c-3978800d825f | -11.19646 | -53.97745 | 2024-10-14 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5eaf56f9-db44-3c13-b52a-22d79e1bc449 | -11.07696 | -54.79716 | 2024-10-14 01:17:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bdfa16b0-7102-3651-ac20-5f910d3f92af | -10.95403 | -47.78688 | 2024-10-14 01:17:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1f494d07-1f5c-35d2-9849-2c325bd0a863 | -10.88779 | -52.3548 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1332f566-d454-3043-9d9d-01cb8740b105 | -10.88018 | -52.36517 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eb729e48-0efe-3a14-bfcb-a27121905020 | -10.8713 | -52.36649 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 714e9f06-86c9-3523-b6ef-9e9db7f2c6c8 | -10.8637 | -52.37689 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e9800fd-0fd3-3aa1-8ca6-53aa6743ed0e | -10.85993 | -52.41438 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4337e246-8c19-30f0-b268-ab4c511482ff | -10.85737 | -52.39627 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4f3f50e8-9a36-3464-bdea-d9240b2b771e | -10.85609 | -52.38723 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7821b68-6482-3da5-a427-4ea31a7bccaa | -10.85208 | -47.8748 | 2024-10-14 01:17:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6875efc6-1626-3b1f-acd1-66e8e15569ab | -10.69501 | -53.01551 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 07769f22-47eb-3c37-b27c-2bf584f6ab6a | -10.62975 | -54.61547 | 2024-10-14 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7f597b93-5dff-3c9b-b799-e9607d09bcbb | -10.62847 | -54.60603 | 2024-10-14 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e5ad42bf-6ab8-3ea6-98ac-917fa799c378 | -10.62065 | -54.61687 | 2024-10-14 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a1edf51-53d3-3af0-a8f3-4d1fa4824083 | -10.61937 | -54.60735 | 2024-10-14 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e7f066b-699b-3c10-9876-cd9436742429 | -10.55031 | -50.83716 | 2024-10-14 01:17:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3e87e841-2b94-3683-86dc-1f4839dd3e22 | -10.52925 | -49.79351 | 2024-10-14 01:17:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7a47a88d-a7f6-33fc-ade7-d6e36cb52ee1 | -10.52747 | -49.78183 | 2024-10-14 01:17:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cf75243c-ade2-3dcc-9ef1-d94d5ea9d0af | -10.52003 | -49.80119 | 2024-10-14 01:17:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 48ad59c3-bf71-3800-8d74-34d0eb0d1aa7 | -10.51925 | -49.79509 | 2024-10-14 01:17:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 54fb6a2e-9f42-3ed8-827d-d0987dcff7d3 | -10.51831 | -49.78951 | 2024-10-14 01:17:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8366acac-8718-3824-b584-284d44dff395 | -10.51745 | -49.78342 | 2024-10-14 01:17:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| c2b42021-d914-302f-8067-2c2b5c7f4d58 | -10.51659 | -49.7778 | 2024-10-14 01:17:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f3f4e79d-917f-3241-a92e-f1bc9f358738 | -10.4701 | -47.86374 | 2024-10-14 01:17:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7f79edd7-4a96-37c5-84e1-06fe0178feee | -10.22636 | -52.68842 | 2024-10-14 01:17:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d1ad390-403d-3a95-b55a-1fc3e347ccce | -10.20314 | -52.33227 | 2024-10-14 01:17:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 93be83d8-83d8-356d-a32a-d1e5582eee51 | -10.0403 | -54.34329 | 2024-10-14 01:17:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 15a355d6-cbcc-3e1a-8fb7-148906d4a1bf | -10.03155 | -47.33595 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 69556caa-7c87-37b8-88f5-d44d0fd89e9a | -10.02876 | -47.3181 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 8bc34471-697d-3fec-a218-2b61ff8650c4 | -10.01941 | -47.33818 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| bfdaaf5c-b0ec-3acb-9a64-cac12b6f7f99 | -10.01658 | -47.32019 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e1d1c245-aad1-39b3-865b-de0f5d9c8246 | -10.00726 | -47.34027 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| d393bc3f-746d-30fe-add1-7911bad21860 | -10.00441 | -47.32227 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| e04ae074-2750-3c61-aba1-7e0315297044 | -9.26904 | -45.23368 | 2024-10-14 01:17:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 55d3b350-f0fa-3be8-a140-53fa1a6ca15b | -9.2684 | -45.24053 | 2024-10-14 01:17:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a79780cb-d8c5-394f-8cd6-1412127b2030 | -9.26404 | -45.21321 | 2024-10-14 01:17:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d0f8674a-ed65-3eb0-abbc-85325e1f8fb9 | -17.72657 | -56.27737 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 5cf53fec-398d-3f41-b894-badf6ef085ed | -17.68989 | -56.25194 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| d8168653-802b-3bed-b224-5a4e4baf4efb | -17.6857 | -56.31286 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| abc05619-f310-38f1-9593-60eb2a0dbe41 | -17.6524 | -56.31712 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 894c9469-3840-3527-b7d3-a2a6fbf485ea | -17.65072 | -56.3022 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 45d97b22-ea9a-3935-ada3-fb4162003d17 | -17.65005 | -56.30873 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| ba076139-08c6-3c43-af2d-e9b4c79af629 | -17.64826 | -56.29386 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.2 |
| 4e9e08b1-22ad-306b-850e-57b028b83399 | -17.63896 | -56.31016 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 57d7775c-53bb-32b2-ab5b-8b88972ecf88 | -17.63719 | -56.29528 | 2024-10-14 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 1f0be77c-43b8-35d9-a9f2-41ab6f6aceb3 | -11.89114 | -43.90068 | 2024-10-14 01:17:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 1364f3df-da83-3153-9d2b-d5d9a0972612 | -11.11219 | -43.33789 | 2024-10-14 01:17:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 04a6630d-e65b-3790-b30f-7021bd5a6698 | -11.10541 | -43.34621 | 2024-10-14 01:17:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 82.7 |


[Clique aqui para ver as próximas entradas](README18.md)
