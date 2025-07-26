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
| 0fceb7db-4cd3-3df3-99e2-a9f63e9786a5 | -12.02441 | -57.09679 | 2025-07-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecbba3cd-5aa6-3d98-b186-814f6364be36 | -14.79103 | -59.5663 | 2025-07-26 05:21:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a28c0404-d0f0-369b-aded-34c422843dd6 | -14.94574 | -46.9486 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 30fe3241-6b4c-3348-999d-01c42215629f | -13.23472 | -51.1511 | 2025-07-26 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 188072e4-5f55-3c46-a04f-372737be1f2d | -12.02536 | -57.09507 | 2025-07-26 05:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2acf653-410f-3535-acf8-a1676610dd44 | -13.24086 | -51.13188 | 2025-07-26 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3349d9c5-904a-3702-92cf-b84f52da0828 | -17.54043 | -53.7136 | 2025-07-26 05:21:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e7d9caf-9628-359d-a1b7-c4cceecd413d | -12.46295 | -57.87791 | 2025-07-26 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2df9d8d-c32b-3cdd-b184-5907f3ab8b7e | -12.50977 | -57.77826 | 2025-07-26 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 748d75e4-ab6b-3dcd-a405-beba08a46cab | -11.9484 | -58.75888 | 2025-07-26 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f51d9146-5904-36c0-abf6-28d0cbda7354 | -19.97591 | -48.43117 | 2025-07-26 05:21:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8e54c15-1034-3cb8-86e0-a6dde8fbac7a | -14.94448 | -46.96242 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b7911e6a-8f0c-357d-9bc7-c4eca2eb9bea | -11.7319 | -62.32943 | 2025-07-26 05:21:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c84ca45-aa06-3138-a6af-5311e4fd31e0 | -16.30004 | -52.92479 | 2025-07-26 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abe378ea-aa62-3f50-b9d8-175b03dc0c2e | -13.24598 | -51.14902 | 2025-07-26 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cd5fcb4-e04c-373a-b688-8f4187f2f972 | -14.37639 | -50.33095 | 2025-07-26 05:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ecf9d0e-fb04-323e-9335-a215eb2b4dc7 | -14.94186 | -46.95599 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| abbe9933-3a9d-31fb-9458-5c8ad3fe30ff | -14.93569 | -46.94502 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73c7a37b-e5f5-3387-a15b-9761682f9dbc | -19.01897 | -54.65551 | 2025-07-26 05:21:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca69e470-7334-3a95-bb75-3fe8166e3964 | -14.93832 | -46.95045 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c837c94e-8312-3b22-97f4-e3ec44aea8ce | -16.2684 | -50.14239 | 2025-07-26 05:21:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0da08a67-dca3-3881-a762-8c8065b33e05 | -11.00764 | -68.49989 | 2025-07-26 05:21:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab51334-3029-382f-ae25-2d66fcd85578 | -14.94933 | -46.95368 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f91f866d-e7fd-352c-8c23-6dbf90d6bce9 | -17.53978 | -53.70946 | 2025-07-26 05:21:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5172fd5-e3f3-36bb-8a98-fe44de407ccd | -13.24639 | -51.14547 | 2025-07-26 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cd9072c-6828-3db2-a6d1-eb8d4120916f | -14.9451 | -46.95557 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 48dbe8c3-bbca-3799-9096-32a08d0133e0 | -19.01987 | -54.65976 | 2025-07-26 05:21:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 869e999e-c99e-3da5-8e4b-cc148b6af841 | -13.24015 | -51.15183 | 2025-07-26 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0266e384-cea2-3398-b6bc-3dbb41f2c85d | -13.24043 | -51.13543 | 2025-07-26 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04b75930-3b55-3866-9312-8f8ab1cfbb24 | -14.93501 | -46.95203 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84c25960-6970-3379-919c-aca2a28b3942 | -14.95552 | -46.9643 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6840eb8-d5da-317f-af19-c7eb58f4d373 | -18.22675 | -54.54641 | 2025-07-26 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1da034c2-91d4-31c6-96e4-cbfc28a5ebc3 | -14.94863 | -46.96087 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 194b9da6-f728-36eb-ab12-ca51cda45383 | -14.9412 | -46.96278 | 2025-07-26 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4f68e36a-416e-3954-9a00-f1d30bc18603 | -13.00664 | -54.87801 | 2025-07-26 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c63cd942-4bdb-32a7-a111-4c39e92d5e9b | -22.00147 | -55.53154 | 2025-07-26 05:23:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b01f900b-22bf-30de-98ab-1fe766cf71f5 | -20.23043 | -56.29081 | 2025-07-26 05:23:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1e90a41-567a-3fa5-9a02-8e9500a84f68 | -21.34579 | -56.45025 | 2025-07-26 05:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3f08ed2-5d68-3487-bb57-fe7a26ecb90d | -20.23101 | -56.28796 | 2025-07-26 05:23:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 282222ab-40cf-37b3-8240-fad6c87bf4cc | -21.3004 | -56.11188 | 2025-07-26 05:23:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0770394b-5855-3379-ba53-9c3e450da181 | -20.62417 | -54.83814 | 2025-07-26 05:23:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 17e85ecd-5284-32f3-a38c-867930129b88 | -21.99364 | -57.61199 | 2025-07-26 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f358fe07-f2c7-32b5-a390-53dbd929947a | -21.99537 | -57.61383 | 2025-07-26 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c0806895-275e-3abc-b165-6168180f3997 | -21.99763 | -57.61259 | 2025-07-26 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9ae3b747-dec8-3335-9c7e-1668465fa023 | -21.30805 | -56.12186 | 2025-07-26 05:23:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c208694-a01b-3cd8-8d59-45720d2680cd | -22.00604 | -55.53204 | 2025-07-26 05:23:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ef19999-3bc0-3db4-bcf8-ac7148a4eca2 | -20.62189 | -54.83844 | 2025-07-26 05:23:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c2cf263-5e54-3b6a-9099-76b62a714675 | -21.99936 | -57.61446 | 2025-07-26 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| af9a907a-de76-38a8-b6d6-ec36a53407c0 | -6.55921 | -56.24616 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 177034e2-f020-30dc-b1a9-b9c768cd7baf | -6.55435 | -56.242 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25938e3c-2dc1-3dfd-91fa-fb014892e01d | -6.61949 | -58.83523 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| df447fca-3102-37bb-a236-8d026b4ead2e | -6.62652 | -58.8497 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| f3801a61-8925-3f38-bda1-bb07949bb260 | -7.49775 | -63.82197 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bf87098-98d2-378d-abe7-7f16f8cee058 | -6.68767 | -58.83623 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2dfc9f5c-8229-34ba-a4ac-5ae91b16c0ba | -6.64563 | -58.84342 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ebab680b-83f3-3fd0-aeae-d13cd6ffbe97 | -6.65899 | -58.84542 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| d12e7d3b-7f7f-3141-be34-53752db68660 | -6.62269 | -58.84466 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7653d42c-3647-3461-b9be-3f2a3f343562 | -6.68321 | -58.83558 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 79a833bb-b9df-37f7-8d94-5ad9e656b9a8 | -6.53654 | -56.2531 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d691c422-41f6-37eb-8b50-320a385ff523 | -6.65454 | -58.84476 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b7300778-a69c-3938-ba18-302c0fa1f095 | -6.56014 | -56.23941 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78bfe211-a32f-302c-9d63-498275215f4b | -6.54374 | -56.25652 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 889aba78-99c6-33c2-8d7d-8c474d7fa14d | -9.0743 | -64.41228 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99634087-2127-3579-907c-91adf4e74191 | -6.64627 | -58.83898 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b4b6c075-aaa6-361d-98b9-b8b3ea97b8e2 | -6.69086 | -58.84554 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec66148a-6da3-37e7-8586-8246ccaddb51 | -6.69338 | -58.84809 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e59a2eb-af6c-3ffd-a76f-d99e62d889f6 | -9.63024 | -61.45707 | 2025-07-26 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c9b6297-1da7-3650-bfa3-0ba146f5db02 | -6.55829 | -56.25281 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c45c26b-6b8d-324e-8df1-1d58290ccf8a | -6.61886 | -58.83961 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf7e9648-8b68-37d0-8878-2c0c69155a22 | -6.67365 | -58.83862 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cf24baf4-fd57-3788-b8b7-ca49079ebee4 | -6.5389 | -56.25243 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10f44236-ed2d-34a3-bec2-362dbdd96b95 | -6.63733 | -58.83783 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b3d0b9bc-3d8b-3048-932f-0d5cb5a0c1c6 | -6.63286 | -58.83721 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 893c9f1d-4c3a-3487-8882-1e25c0f7ef67 | -6.62714 | -58.84538 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c2e898ee-11cf-3a96-a0cc-f02bb63a1518 | -6.66219 | -58.8234 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5f836021-e00f-364a-ae28-1b3d4a0e2924 | -6.66855 | -58.84233 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d3c54285-fd95-34d3-8236-77608970e8b3 | -7.6581 | -69.9303 | 2025-07-26 05:44:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4332e066-152d-33b4-82c5-0a5f67cfa4a2 | -6.63478 | -58.82379 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 58f31e2e-a4b0-3d9b-ac12-8d25d654f9c2 | -6.65709 | -58.82711 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 8880db5c-3e05-34cb-a8d8-2341ad224de1 | -6.666 | -58.85982 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 64657ac3-b411-3857-84f5-616767da29af | -6.5481 | -56.24794 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0431786b-5d79-3963-9fb8-6003b995f395 | -6.65646 | -58.83152 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| aeaaa8ee-1320-34e2-a08c-018ae43195b6 | -6.53608 | -56.25647 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74689085-cb65-32ca-b146-88770377e4e7 | -7.66197 | -69.93096 | 2025-07-26 05:44:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 806a9975-c573-30b7-9644-0308cdebf522 | -6.5447 | -56.24984 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9413190c-9b60-33a0-bcc6-5507a45b0253 | -6.67811 | -58.83928 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 88e4e44d-6adf-3755-ade4-ada0065795f5 | -7.94261 | -61.56741 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17eb499f-058d-3c21-a521-0997b3028c44 | -6.65773 | -58.85413 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| e5acf383-c584-3e84-839b-dab1b4b0ab28 | -6.53744 | -56.2625 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 138ec3b5-9cb4-3855-94ed-0cef772d7001 | -10.85223 | -54.03818 | 2025-07-26 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56c6e900-3de9-379d-b2d2-08d81b504685 | -6.66473 | -58.83726 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e01d8054-f8d5-3d6b-970d-8f7411b37802 | -6.53793 | -56.25916 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0bc94ea-e2c0-3452-90c2-6ac73c2b58eb | -6.63544 | -58.85097 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 61f3ade1-0753-3ef9-a6c5-cf0505e19714 | -8.21181 | -70.50255 | 2025-07-26 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4059a520-af61-3ccc-ac05-c7a7557aa709 | -6.6813 | -58.84861 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 9a2741f7-4d5c-313e-903d-72b6c07a452e | -7.56705 | -61.40158 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3659b740-d257-39aa-85f8-cfe7077f225b | -6.6539 | -58.84913 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0932e928-c72d-3937-a0f1-f1cbae9079f1 | -8.66464 | -63.8522 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82f36c1d-af88-3962-8504-db654fa31fda | -6.64945 | -58.84846 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| cbd05e12-e6a5-3fd8-ac86-df7c87422877 | -8.09858 | -61.40018 | 2025-07-26 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
