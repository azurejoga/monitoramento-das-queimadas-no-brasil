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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ac865ec-98f2-30cb-a85f-82eb32d6b63e | -2.87611 | -52.61653 | 2025-11-23 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 347aff16-7b5f-31eb-b12b-f98ed93a602c | -1.41715 | -52.59296 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d62fc9fb-ebba-36ca-bd48-69020f813210 | -1.86397 | -54.07183 | 2025-11-23 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fa68fff-c14b-3ada-8dec-72f0d6913d64 | -2.63084 | -47.30046 | 2025-11-23 04:53:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c4218b8-0eaa-3662-bfc2-8d8a5d0c0121 | -3.4611 | -52.2361 | 2025-11-23 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c281fcbb-63e2-3eec-be35-9db69ecd9af9 | -1.6698 | -52.0465 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e04f257-9aed-3d85-b6c8-e6674332ef5c | -2.88356 | -45.28543 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6eff96a1-6721-3266-b384-7dde41a61398 | -4.04136 | -42.51962 | 2025-11-23 04:53:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bf297551-e622-37f3-848f-1fd27efb6c54 | -5.98152 | -40.38463 | 2025-11-23 04:53:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 1a25be91-6391-36f4-8d9c-bc9c62979032 | -4.83353 | -44.06437 | 2025-11-23 04:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9e6daef6-e7d1-3498-9eef-7702e72ee138 | -2.47902 | -50.47313 | 2025-11-23 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da4f3108-518f-3e15-9f0c-7159c2c8bcb2 | -3.8659 | -40.64001 | 2025-11-23 04:53:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd6ced1c-0d10-3d20-b6c4-92092015f613 | -2.64241 | -47.38403 | 2025-11-23 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be0532de-5bc2-391b-8511-e95741f69849 | -2.9855 | -44.41964 | 2025-11-23 04:53:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 799279a2-28f2-3f00-a633-44a96111532b | -2.02729 | -47.14712 | 2025-11-23 04:53:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ac354db-2b2f-38bc-940d-07b7e3213a83 | -4.04635 | -42.52403 | 2025-11-23 04:53:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 17ddd288-623b-3308-be63-3b60c7ea8340 | -2.29963 | -50.47799 | 2025-11-23 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64909064-34d3-31fd-be91-c9654ccc9e7b | -2.2273 | -53.6483 | 2025-11-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24fff5e9-f670-3179-8e54-4f3deda1df12 | -2.70265 | -49.51548 | 2025-11-23 04:53:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ddafff06-e338-3536-baf2-83aee0277ba5 | -2.8671 | -45.4532 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24e8caaf-623f-3f79-9c30-2fd8c8bb893c | -4.71555 | -46.46186 | 2025-11-23 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 642d049e-499c-3e6a-93c9-57b292ad0cb1 | -1.7463 | -52.03359 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c318152c-4936-3138-ba12-06a869a2f6f9 | -4.64091 | -45.47088 | 2025-11-23 04:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de5742aa-4c38-3f47-8545-c4950cb9673d | -4.83309 | -44.06332 | 2025-11-23 04:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 71ce9743-6790-389e-92f1-2fb32a82ec04 | -1.65081 | -55.5604 | 2025-11-23 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ac8a321-ef69-3bfd-8bdd-996b7ed5ab88 | -1.82555 | -45.57298 | 2025-11-23 04:53:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb8826ac-9da1-3e7e-85af-a4722227f84e | -2.50198 | -47.10151 | 2025-11-23 04:53:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad9a58d-e5c0-3785-9ac5-b736a1f12203 | -2.98875 | -44.43058 | 2025-11-23 04:53:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a3c6887-7175-3df7-9ca8-cd36ead4615e | -1.32619 | -53.14382 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a816a09-2c46-397e-b563-729966864452 | -2.08806 | -52.03385 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6de1f815-0654-33cc-b473-047dbf2645f6 | -1.88707 | -50.9707 | 2025-11-23 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0ac912a-5b16-392b-8ac4-a49424be5a30 | -2.8391 | -53.01443 | 2025-11-23 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5302ec76-6aae-3c04-9b8b-f020770265a9 | -3.4756 | -53.3374 | 2025-11-23 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d979fd59-a50b-3f78-ba2e-c1599e0b1b72 | -2.95524 | -45.43382 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c637e5d9-34cf-3ee7-89f6-757a01ac6f1c | -2.95081 | -45.43309 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff39e07e-3026-3cba-8ee5-a20839b4b897 | -1.73465 | -52.02114 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a770d700-a747-3a7b-8c85-723160915842 | -1.98024 | -50.24675 | 2025-11-23 04:53:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98292498-aae9-3855-b9a0-dc6b592f0109 | -2.87907 | -45.28477 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bda003d1-9587-3f6a-a3e3-78315286db5a | -4.71612 | -46.45799 | 2025-11-23 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1c305093-4558-3ec6-8d89-583dc45cd94c | -4.56212 | -45.49553 | 2025-11-23 04:53:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13f5f12b-b0e5-396b-890d-8ca0d5b5b66a | -2.88424 | -45.28098 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1e1d01df-7345-30d5-976f-651af724d21e | -2.87945 | -52.61705 | 2025-11-23 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c204713-352e-3a9c-8840-198220f7da51 | -1.33319 | -55.40095 | 2025-11-23 04:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81748ee7-b38d-3e94-8e02-a4e4f148b76e | -2.04438 | -52.05179 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 335a00a3-74fd-3cba-8b95-0685ec7dd81e | -1.74184 | -52.01873 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71fb7fa5-7208-38e9-ae2f-ebca9fdf3e81 | -3.8647 | -51.13962 | 2025-11-23 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93f173a2-1ac0-367b-89c2-dcab9656b2bf | -4.17255 | -44.2178 | 2025-11-23 04:53:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b10d9fbb-798c-3ef1-91ec-cba4d882bdaf | -2.6963 | -49.51059 | 2025-11-23 04:53:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc2569c4-72df-3310-b3f6-a7fa2d50216a | -2.46811 | -45.42586 | 2025-11-23 04:53:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e03662a9-d396-3d41-8354-1f6bfd367646 | -2.63757 | -45.48829 | 2025-11-23 04:53:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a53966db-d3de-364d-8f4e-f454c62459cb | -3.45624 | -47.62949 | 2025-11-23 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dafbe707-d972-32e7-a985-88372a28c85b | -1.32959 | -53.14435 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f613476-d0b4-3e4d-9c0e-08631216e626 | -2.87975 | -45.28031 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4cd7c8a7-68fb-35fd-8e1a-763b544b530d | 1.93523 | -50.86937 | 2025-11-23 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d06f28f1-539c-3980-bebc-89c2a66967a4 | -1.31538 | -53.1459 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e5bfdbb-dd02-39c0-bd55-329a4846fb5f | -2.63552 | -47.29619 | 2025-11-23 04:53:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 797ba0d8-f70c-33b0-881c-c60816e55549 | -4.30432 | -47.54287 | 2025-11-23 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4cf6a2d2-39e7-3d93-9418-49ae95a0c746 | -2.88021 | -52.77853 | 2025-11-23 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27155597-2d82-33bf-88c3-65a65a65b116 | -3.70072 | -47.67555 | 2025-11-23 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2186714b-da47-3aa0-8dd7-f6eae226e5c9 | -3.46606 | -52.22626 | 2025-11-23 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 702b94d1-ce6c-37c1-b34b-171b400fdcf4 | -1.74297 | -52.03307 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fee67757-4a9d-3649-85bf-46f56eb7fc33 | -5.97423 | -40.38936 | 2025-11-23 04:53:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 14caa910-4051-3f69-9d82-26d26ea007fd | -1.74407 | -52.02616 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2a94c5f-0d23-3314-8043-86e71bb6387e | -2.63159 | -47.29764 | 2025-11-23 04:53:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5713cbff-413b-3d00-a0da-b90986cba2c1 | -3.46012 | -47.63006 | 2025-11-23 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d0f5066-0fcc-3379-8d46-c6f726cf3f29 | -1.73688 | -52.02857 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 446bb9d6-d259-3130-b9ab-63febb6a5276 | -2.47252 | -45.42653 | 2025-11-23 04:53:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 28ba913f-9eba-3341-b30e-df6c41e27273 | -3.86081 | -51.1426 | 2025-11-23 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c33ce44d-877e-3c7c-8e0b-292c3bc9d198 | -2.88872 | -45.28165 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e21b17b2-64d4-3165-816b-21f79d07ad69 | -1.86106 | -54.06749 | 2025-11-23 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 115648e8-9fe4-36e2-8f9c-46dc4a5ee262 | -1.31422 | -53.15321 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeb076f3-d571-300c-917d-f911db87e08e | -2.69978 | -49.51113 | 2025-11-23 04:53:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a750bf51-b0da-3f11-aa76-957740cd5562 | -1.48553 | -54.20386 | 2025-11-23 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28a48315-fa84-3c28-8588-b39b7aa5bd1d | -2.95903 | -45.43887 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d71f1c6-0695-314b-aa63-8bc03ea790ff | -0.85759 | -52.70582 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aac11ba0-3461-3ec6-b42d-bc391eca3462 | -1.30857 | -53.14485 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d74eda89-470c-32b8-bfb1-61b80bfefe77 | -3.16671 | -51.1629 | 2025-11-23 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93ad95f0-4025-39c2-8dcb-dbac06faf9db | 0.64268 | -59.73246 | 2025-11-23 04:53:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 170aff8c-c152-37b4-92f1-a7593f4d600e | -1.73797 | -52.02166 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c65dae8b-680b-3bc7-a44c-a13306c3f4c6 | -4.71129 | -46.46124 | 2025-11-23 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 419fc646-45a1-3529-8848-7158d3f8fbac | -2.95585 | -53.28567 | 2025-11-23 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4d6e07f-2b82-3009-afe7-c223c8417b85 | -3.79902 | -51.1437 | 2025-11-23 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98cfd5eb-efcd-3ea7-a2f8-fae945bb8195 | -1.67273 | -46.45498 | 2025-11-23 04:53:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72e1a286-84dc-3c23-93fa-35ad449953eb | -4.54845 | -45.49387 | 2025-11-23 04:53:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76b569fd-593c-3b58-8297-abab0ed71e2c | -4.04188 | -42.51604 | 2025-11-23 04:53:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 19f8dc25-12bd-3325-b50d-4eb95a20aab0 | -4.83268 | -44.06621 | 2025-11-23 04:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52852dac-debd-3cac-8242-7408393967b1 | -2.89322 | -45.28229 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 77186a5a-b51a-355b-a3f0-aed8a0ec52bb | -1.8225 | -45.57523 | 2025-11-23 04:53:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7cc903e-cd39-30e6-9c0a-df94d17034fd | -1.7402 | -52.02909 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29b2d796-69a2-3d94-b9d8-36ac079dfade | -2.87219 | -45.44957 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 13081997-2a48-3e12-9e7c-20d85460a1b0 | -4.04133 | -50.48415 | 2025-11-23 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89084d02-d6ad-3486-ac6b-09e24a88e2f8 | -2.88805 | -45.28608 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bf6f7192-1b7b-32d4-a5e1-815f8679dbc9 | -3.79815 | -46.04802 | 2025-11-23 04:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9106aba-4d84-3f74-8dcf-bdfafc23fb76 | -3.90749 | -46.13667 | 2025-11-23 04:53:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0bdc1f7-9b8f-32de-9c44-03590116bff7 | -2.95699 | -53.27848 | 2025-11-23 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c9848b9-9d0f-3421-8e59-67de0abbfc34 | -2.27117 | -46.44518 | 2025-11-23 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7e82927-79ec-3458-82e5-838fd67d907c | -4.56145 | -45.50005 | 2025-11-23 04:53:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f16475db-8ab3-3e4a-950b-a98a832d7139 | -4.55618 | -48.48466 | 2025-11-23 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee886cf7-499c-3a4e-a683-2f392722e4d2 | -1.3148 | -53.14956 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9a35c68-f9e6-3ccf-b427-ebf628b21caf | -1.74352 | -52.02961 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README9.md)
