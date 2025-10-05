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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e847324-f355-37ca-9e55-6a870ae477ca | -19.01457 | -50.60052 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 1024f875-f5a4-3480-8a22-18b323623a70 | -17.11264 | -48.92865 | 2025-10-05 05:16:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 584b6927-1873-31ba-b635-f801ba4aa48f | -13.09736 | -47.84435 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2ad7db8-abba-38e6-92a0-c9820d7a20de | -12.3207 | -55.15224 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a44e048e-4abd-30e6-a302-fb4d01b06cf6 | -16.04884 | -50.94271 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dca6fc59-f144-3654-9c33-540c14ba031c | -13.27825 | -47.62183 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4f6220c-ebb7-3b30-bc7f-38f0fc497b0c | -16.01572 | -50.95894 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eec822b9-1620-3548-9631-36b85bc8f249 | -15.98504 | -50.90829 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e08304f0-32a5-3bfc-ac38-dd50dcc6c98f | -14.68724 | -48.27018 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcb7201d-8c73-3dd7-9aea-4acd3ee11e81 | -10.83833 | -57.19132 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e94da080-998a-302e-9914-c63c6c697406 | -16.88179 | -49.39398 | 2025-10-05 05:16:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cc417c6-d5c6-30a8-890c-095d2e8328bc | -19.00911 | -50.59991 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 2a77e57b-cd91-34ab-b6ac-ec6a16e02b10 | -15.38887 | -47.94892 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d3fe091-2482-3861-98c1-769a2174abc8 | -13.14286 | -47.97868 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aab77c6-cd69-343c-884f-5811ebd998cf | -18.17079 | -53.36112 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5966da02-c853-37e6-abe1-79b7063a9fd8 | -15.78258 | -49.09814 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99218ffd-9eaa-308a-a0ee-faf07e5ab58f | -14.69783 | -48.34163 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78428f05-ae5b-390e-93f4-1a8ae6698fb2 | -13.49046 | -47.27349 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c59233f-42b4-32a5-ba18-0241ac14b017 | -16.07871 | -50.91064 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 369d2d16-f080-3f9a-a82f-e7ddcdb43d25 | -15.98872 | -50.92185 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 67889cf7-dc68-3ec2-ae6a-12e324a1d914 | -12.78368 | -48.82304 | 2025-10-05 05:16:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcb5e0c8-e6a1-3dc6-8f1d-19e4bfae8929 | -12.84421 | -58.76286 | 2025-10-05 05:16:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98248a8d-49fd-3099-a808-ac4635f77a5a | -15.38324 | -47.94297 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c19e6e4-1dd2-38c0-870c-51be507cd111 | -14.69048 | -48.29692 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 198591d8-a733-3946-804f-2cf38fbfe2b4 | -13.29573 | -47.62397 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5de06c7-5b9e-3c73-8bed-315684444e7b | -12.56874 | -48.16431 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d8536c-156b-3655-bff6-1cb86e04fa37 | -14.70062 | -48.35187 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d22eac0-81ab-38d2-87ca-8f0148b5eb29 | -15.9837 | -50.85773 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6980da8-8b85-337a-8b2d-04ff88fdca3a | -13.37848 | -47.55427 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db8ac049-226a-3537-bb78-aac7ba6c0826 | -13.28528 | -47.60554 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c31dac33-0fe4-3cd9-9305-3328ffa7e32f | -15.54177 | -46.8376 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74c1f5ae-d7a5-307d-a653-c793eead3857 | -14.32809 | -47.70345 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1402926d-2538-3776-b6f6-5d5c3fe8f3cd | -16.0326 | -50.94799 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4b4cb64-7fed-3e89-a460-9ccdc5c21972 | -16.00714 | -50.85162 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d1b85d7-300b-395f-85a6-f94d52ceda92 | -13.32122 | -47.78478 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d3a4278-89ca-33a9-a2f3-e068780a707d | -16.01228 | -50.85255 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c89506a-bc29-33f3-8324-82b471d5c86f | -13.35677 | -47.58019 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91e7bc0c-19ce-330f-b9a8-3948d040e3ec | -13.26801 | -47.60254 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a94bbc0-b723-3cf8-bb0a-a6bb7c10fee8 | -15.34533 | -47.96097 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5db1b11a-df41-3f77-a024-3b975745dd83 | -15.42463 | -50.20245 | 2025-10-05 05:16:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec0ded97-c048-36b4-85b1-18436c2b0b83 | -13.1587 | -47.96888 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56443ef1-0369-329c-9387-35e43c7dccc5 | -14.69277 | -48.27526 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40bfa959-38c1-3173-ab78-e2319c9bb95e | -15.35603 | -47.97738 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a76d697b-4847-3749-8aae-99ec29de205f | -13.2725 | -47.61765 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19d5b259-b0e9-3c48-98f6-459c745ed5d6 | -13.35017 | -48.06347 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5ac9a89-36e0-3c24-bac2-723a89cd8365 | -12.27003 | -55.13541 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb0688da-f281-372f-89ec-bde024f2cb42 | -12.91571 | -47.30702 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71e6c195-f7eb-3c5f-8f50-3cc9eb64c99f | -16.91333 | -52.04765 | 2025-10-05 05:16:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fa1f68d-eac6-3050-a25e-583c58b5e21d | -13.12498 | -47.97545 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b10d2bba-848d-340c-9e78-b74402d877ab | -13.35317 | -47.24725 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a42d2f54-b3db-3a4e-9b79-44a0890e2fdf | -15.35462 | -47.97837 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 794ef850-9b5f-3353-a23d-efd13e86a8da | -15.68923 | -46.27236 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44dc6eee-9cdd-306d-8901-ce41cfc5764f | -13.46355 | -47.28626 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cc7dabd-dca8-354f-8a6b-234cd16f9ed4 | -12.97075 | -51.04029 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c4858cf-c8c9-3591-8c2c-970dd3caed2c | -14.32901 | -47.67633 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1956ed80-a63a-3c03-9be3-bcb841c2c665 | -13.09098 | -47.8465 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b50e111-6544-36a0-8437-aa28387531b2 | -17.96172 | -57.58174 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2adc7c2d-b9a2-328e-8e14-88431db8dd3c | -13.30022 | -47.80413 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e3d479c-da34-360d-b778-d53b5ec3b5dd | -12.92487 | -47.30519 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72cda909-ce3c-3cec-8b6c-fd154f7f7b39 | -13.45982 | -47.28683 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08ce0333-e147-392f-8e36-7b193eeaa76b | -12.31215 | -55.13285 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc8887fc-1fe4-38f9-880b-76c3adfe1a56 | -14.93848 | -46.84455 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7771331f-7d46-322f-a801-821933f72838 | -13.43858 | -47.28145 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e577103c-3c6a-3e71-8eca-453b4579e640 | -18.3314 | -45.89624 | 2025-10-05 05:16:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 3615e6e0-d87c-3087-9ac6-9157d5a73d8c | -13.31827 | -48.07697 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c4e1349-22f1-3598-b971-9614dc984223 | -14.87237 | -48.15557 | 2025-10-05 05:16:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c9d9b4a-4353-3387-9970-299bdd03cc53 | -13.09188 | -47.94594 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 663587f9-82c5-3602-96a8-26b27d68c0ed | -16.03224 | -50.95105 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f60a3eb-2ce5-3f7d-a4c2-011cc8e9449f | -10.80463 | -69.04048 | 2025-10-05 05:16:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a749ce63-7555-3e36-95df-6f6f3b99b877 | -13.47628 | -47.28631 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2a4902e-fba4-31f6-9e9c-18dbcc2c3a41 | -18.25455 | -53.36485 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d1843f59-cc62-36d7-9a4d-f53ded29b2ce | -18.24896 | -53.33467 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7982c37d-95f0-3cb6-98e3-0078774c44ae | -12.31569 | -55.16053 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dc53598-dc62-3b19-8f35-9d33218f9ca6 | -14.92668 | -46.84228 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3f7aa7b6-baec-322f-ae87-187a00ab5711 | -14.22034 | -56.57103 | 2025-10-05 05:16:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bb3accc-1b8d-3894-8d07-3c752656f2fd | -17.8775 | -57.59114 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 40ac8300-0ed7-3d2d-bdb6-d73eac3ff6d9 | -10.03521 | -62.4592 | 2025-10-05 05:16:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7324fa1d-2dc7-3f4f-bad9-e7ca8213a73f | -18.14374 | -53.3471 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3296ffb-c4ad-3a99-930d-21f6dc594f9a | -12.30407 | -55.13618 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 987103dc-3271-3931-9d06-80a8c4d83d0f | -15.56028 | -46.97149 | 2025-10-05 05:16:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e26e7a4-8363-3450-af6b-b04c4b810d10 | -14.85442 | -60.06845 | 2025-10-05 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 962024ea-5b19-313a-82a5-0e6548daedcf | -12.31587 | -55.1334 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6bb227a-be5e-3293-b47c-6b25e51b78bf | -12.60759 | -48.11745 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85409e50-9173-3a8f-aa80-9e61e47a467a | -14.32848 | -47.69998 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02692cb4-8aeb-3db4-b485-1a7e61791a1c | -14.99382 | -49.98355 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 647c4034-a3e5-3b2b-a678-23c816558871 | -15.58948 | -52.5057 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f1a0127-da74-3a16-a390-dfdb76e2c7d7 | -13.28431 | -47.61446 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c860db8-6ad6-3f37-b949-c2e707075191 | -13.54641 | -47.23045 | 2025-10-05 05:16:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c7c9845-f877-38a0-9e73-7ebf775876f1 | -16.1537 | -57.5758 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 268ea2e1-ef41-364f-a0c5-64546ad30c7e | -16.35008 | -51.47272 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 847970d4-0577-3829-acce-3ec7118d5388 | -12.59509 | -54.76466 | 2025-10-05 05:16:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 122f486f-4152-3a9e-9c36-af5a8dc2a593 | -12.46016 | -45.51001 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 880bb1b4-4a3d-35a2-92f5-9d72e7e71abc | -15.38379 | -47.93761 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de59e550-8403-3e7c-9ed5-5db730e26aa2 | -12.60712 | -48.12156 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0faf22f-77b8-3ddc-b30c-1d6c48ab0259 | -11.82996 | -60.48693 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32a7b9ec-e95b-3e2e-9797-9ebfe59df352 | -15.90661 | -48.82683 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 508a646f-1096-36c1-901a-ac477b6e37a4 | -14.01393 | -44.92772 | 2025-10-05 05:16:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7d29476-0162-3d65-9019-e0525cc76e6d | -13.72675 | -48.08747 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61b0501a-af02-3e22-8ada-c1d68e8032da | -16.01134 | -50.95186 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b69b2e95-0a33-33fb-b7ab-b2e551aa8036 | -12.10982 | -50.94273 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README128.md)
