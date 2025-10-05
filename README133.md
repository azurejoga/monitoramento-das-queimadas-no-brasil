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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44689e2d-7a57-3b52-9b20-56036d3094fd | -12.31698 | -55.15169 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b790827d-ab3b-3a25-bc06-46e4d1d15c21 | -13.3207 | -47.78935 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d57afb41-ece1-3ffa-91fc-d55c0b98dd3a | -11.21074 | -54.98404 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0028b3af-70ed-341a-ab6a-e645f6a831f7 | -16.34585 | -51.46596 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64b5ebb1-2ed6-39eb-a566-858aeeec65e9 | -15.99164 | -50.92202 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a24913e-bfdc-3d48-a883-73a846d376ea | -13.07819 | -47.90551 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88e94960-4148-3526-8f70-2decb0982c7f | -12.8959 | -47.31468 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8339bb5e-c1dc-3c62-99e8-e0dbb978fff9 | -11.61558 | -55.69831 | 2025-10-05 05:16:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e708a192-6544-3fa0-90d8-bfa43ef5bac7 | -13.47045 | -47.28137 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c197793-8a14-3e02-a892-7e0d46c95985 | -13.13246 | -50.88881 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e4ba27b4-bb36-3d7e-a26a-fba0368d8ac4 | -13.29003 | -47.61912 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4fe573b1-e191-3171-9571-85ad9f0ee8e5 | -14.97608 | -49.99491 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c5d4e75-fbfa-31cc-b907-0dc369637ee4 | -12.45186 | -45.53062 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f75437f-e1ed-3c49-bb2c-c74b3be260aa | -13.45685 | -47.28918 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a6468d2-8454-3807-bcb8-238cdef337ea | -17.95751 | -57.56108 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 010044f4-e401-36a1-bbac-998af690bb25 | -13.30268 | -47.78511 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7ff59a5-49a1-371b-bd49-194edae78dc3 | -12.90214 | -47.31544 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6d49517-bfe6-3678-bc55-d8bc8e62bdd8 | -15.58951 | -52.50768 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56710894-5fb7-3b0d-a88e-81a82ed67814 | -17.95527 | -57.6014 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 158202a4-4324-3d03-9b32-68eac9dd405e | -13.19983 | -48.53579 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c4bc752-3dc0-3ab9-9248-db64d0594ef1 | -18.33735 | -52.01338 | 2025-10-05 05:16:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1714acfd-32c3-3498-8e79-e5323d81fd4c | -12.27013 | -49.19752 | 2025-10-05 05:16:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 24bab2b0-725e-3321-971a-1ef9887ae5d8 | -11.93565 | -64.03187 | 2025-10-05 05:16:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2b56c9e-685b-3850-925e-0afed1368650 | -14.68924 | -48.34558 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9df0d69e-a496-3cdd-b26c-96f5d6c978fd | -17.95922 | -57.54922 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad4cb378-3727-3977-8c45-b6c6f92adacc | -14.67806 | -48.35679 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7800aadf-06f1-3e9e-98f9-6bbbd732fc17 | -15.22533 | -56.82605 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f28cb288-133b-3b94-9e81-632f7a9ed094 | -12.92429 | -47.3101 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 411206ae-7014-3eb1-9952-afa520cd9225 | -13.26291 | -47.19841 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ac6dddf-5a20-3bec-aed0-83ed39e36529 | -14.73944 | -54.62528 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c002802c-2395-3c65-9018-ec07b5eedebb | -13.3152 | -47.78349 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 461368a8-d978-3bc5-8a65-4ddc3b7b5780 | -12.59776 | -48.15116 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3410dbdb-a0e5-370e-b45b-debb846f8764 | -13.57413 | -48.15961 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76f10883-3468-3cab-9d28-c4cb366c6062 | -13.29683 | -47.62281 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 92a1cf5a-664e-3654-b6a9-8c982739cd72 | -13.37957 | -47.54477 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88a03f09-9bcc-3cab-8cf5-66977c6fa3da | -17.88154 | -57.63713 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 83450839-16be-35d4-802e-27efd2ac55ed | -13.34853 | -47.5978 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db6b6172-1d08-3e8f-bdfb-949d9c20a9fd | -15.36829 | -47.97937 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04855934-9874-3c4a-ab7e-e8b246eee174 | -15.98183 | -50.91688 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95c2c36b-23d9-33cb-a60f-f66f422b1a7b | -15.35506 | -47.974 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7c139b3-614d-3a66-818a-3fc80a96e01d | -11.20705 | -54.85189 | 2025-10-05 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebccb34c-7fc0-3dca-9bc2-cdf3d77bd907 | -14.91838 | -46.85808 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d7e42a06-ae63-3b57-afe0-bcb4dd443b5d | -14.85776 | -60.06902 | 2025-10-05 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47b0b799-6922-32dd-87e1-f425c1216fdf | -18.33203 | -45.88871 | 2025-10-05 05:16:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a69eeac2-7237-3758-b574-3c4add120e0e | -13.27923 | -47.61331 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae3064b7-79b5-3b25-8a01-1e2c4f929b18 | -15.58215 | -52.48917 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c6d9b01d-cb26-380e-8bfa-009f751ef369 | -15.28823 | -47.33028 | 2025-10-05 05:16:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42332178-75bd-39b3-a401-745b586703e8 | -13.13394 | -50.87751 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 8689ae1b-b73d-3d23-b486-77884fa6cb07 | -15.24057 | -56.77054 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d09c0511-aeff-39a9-9362-97f3ae000d03 | -15.57162 | -52.46506 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 375505af-0750-3e14-bdfe-fe4ebbde7f1f | -12.3903 | -51.0989 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ff91a49-2404-3cd1-ac00-1b9fbc5e1cce | -13.09693 | -47.84811 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3b2ca28-3239-38d6-84fa-57c026250fef | -14.9193 | -46.84933 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa1ed6bb-2b0d-3647-9201-abcdb9b796c6 | -16.00507 | -50.8542 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f248bf5f-463e-3c3c-aadb-a0fc91c3a00f | -16.03517 | -51.05865 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac7329b9-ab31-3c44-ae30-b163aaf4b346 | -12.11547 | -50.89931 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71be8881-0695-36c7-b1a3-ba4e2279ec43 | -17.85403 | -57.62904 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6bc87409-2ac5-3c08-a2eb-b7606a143eeb | -15.20828 | -56.84417 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dd3a80d-000e-36b9-94b8-d398ede685c2 | -13.29617 | -47.61997 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8de7f5e0-bfee-3101-887e-faa23954dd2b | -13.1349 | -50.87282 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d58bfcef-202d-35ca-82dd-0d451f4363b8 | -15.30124 | -46.3233 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67f25258-6f36-3502-a695-557a0337c9c9 | -12.97634 | -51.03548 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f556fda3-b972-361e-9044-60469dec8312 | -15.59804 | -52.51198 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85441d99-34b9-3415-8b65-b99a209af536 | -11.83203 | -61.20541 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b93b0e2-4ed9-33aa-a3d6-200b750f903e | -18.26236 | -53.35965 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7f17cb88-7a2c-3c63-8c6a-9022cceea1b5 | -18.17711 | -53.34653 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8dbd908-bd4a-342d-a510-f77722273f5f | -17.94004 | -57.60739 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e3d70f91-5d0b-3ca9-b65c-f7840153cfd5 | -15.98294 | -50.90763 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 817f1b82-d915-3867-bbe5-4dbaa9c36f3d | -15.59577 | -52.45934 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92c1f940-bd92-3d06-9259-d67ffd9cb239 | -14.01169 | -48.20656 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4414765e-e05c-391b-9b13-891d3b455b45 | -12.77802 | -48.82231 | 2025-10-05 05:16:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa251208-d620-3acb-8f1e-b3bced56f59d | -13.27464 | -47.59906 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c243d3c-46e3-3f4d-a3a2-c18bd01ec591 | -13.31129 | -48.08492 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2782588-2afa-3f2d-bc9a-343652b51e45 | -12.89817 | -47.31713 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fc2e348-0c52-31b5-a048-49e937dc987b | -12.59624 | -48.16445 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f9cecb2-4635-30e0-95c2-f9cbb7b56837 | -13.27023 | -47.19004 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3f2cf38-c40b-35da-94d6-ac44d1c15b62 | -15.87117 | -46.26217 | 2025-10-05 05:16:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd2ff511-2054-3cf2-baa6-b6697cece013 | -15.98219 | -50.91383 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4bd71d48-2e6e-3b19-8c77-f6b014e87739 | -12.59287 | -48.14158 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a90c590f-6350-3659-a171-24f93855d976 | -18.33673 | -52.01889 | 2025-10-05 05:16:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d22d873-0977-3e9e-a0ff-22338ea61f38 | -12.81581 | -60.82511 | 2025-10-05 05:16:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a912179-fbcc-32e4-a778-c9ac3f801768 | -14.32285 | -47.69425 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6880077-de49-3466-a8f5-978e38ee5849 | -17.96274 | -57.54981 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5136c069-c993-338b-9e89-3c699723922e | -12.3128 | -55.12837 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f760aca2-e919-3578-a49d-80cbca2c6105 | -10.82989 | -57.20113 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c02b617-1328-3acf-9215-b10cd3e6f142 | -13.30534 | -48.08398 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3311ca9-1a96-3438-8608-92047997dbf8 | -12.97488 | -57.10527 | 2025-10-05 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99a8af1d-c7c5-3803-8a9e-4050c9787ecc | -15.5975 | -52.51638 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 068acd47-2552-3809-9d5b-74b2496ae569 | -13.5088 | -47.28055 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9386838d-16e2-3445-8610-a95d4ade2e56 | -15.21181 | -56.84474 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a959608-76a0-3f26-8092-3dd1d018af8a | -15.2281 | -49.28701 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8c34be54-92d4-3213-a4f7-71dd3609b25d | -11.95823 | -51.46838 | 2025-10-05 05:16:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10310b03-03bf-370f-970e-a5ee84aa6170 | -17.8821 | -57.63329 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8565d016-aa06-3d7a-9b81-2e813cf6ce79 | -15.58216 | -52.45052 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 834c56f9-d768-3a46-ad72-6af2d69d7c58 | -13.09464 | -47.92186 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f132644e-6ce7-3209-8690-a289628c0516 | -12.32571 | -55.14394 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beb6ba90-6cda-39f4-9b43-9a66173773ac | -15.54788 | -46.84335 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e679877-0f67-3d1c-9146-f603e79f25db | -14.32634 | -47.70173 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 546fb69f-960c-3289-89cc-7d1d4cf25748 | -13.08314 | -47.91574 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6f8606e-d698-3e3e-8cae-581810376227 | -13.1335 | -50.88414 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README134.md)
