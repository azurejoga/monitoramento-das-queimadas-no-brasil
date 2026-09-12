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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d270b086-f058-3817-9dca-1f8c53d0b441 | -8.1202 | -54.781898 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20da8bee-6e86-36df-a853-df14ccb22d72 | -9.1787 | -68.209099 | 2026-09-12 01:26:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff554de9-ec33-3e82-b4de-706c34530d5c | -6.8845 | -55.648201 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2579d003-41bc-3722-9091-73265492a0c8 | -6.6189 | -58.853802 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da14a35b-caae-3452-b16f-c737024f929c | -6.8481 | -55.797298 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f3a2c8-fd69-3213-9fe4-28551cbe3bee | -6.882 | -55.637798 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0143e057-53c4-395c-bbcf-ca09b1f3abde | -5.7892 | -53.802502 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77486915-fbce-3871-a9bd-380448f546f2 | -6.187 | -57.710701 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 560c7270-e3eb-3a19-b1e5-48ba276a1438 | -3.7386 | -61.759602 | 2026-09-12 01:26:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45169d76-e6dd-33f2-9ea1-4dabda3b8217 | -6.1848 | -57.745399 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d4c646-595a-3b35-a687-94c1326a9af4 | -6.1908 | -57.727001 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e647f0e3-c519-3fe4-b757-a66ddce43ee4 | -3.7355 | -61.745899 | 2026-09-12 01:26:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17995e00-116e-3ec2-bb83-1cd5be4573d5 | -5.9814 | -57.758301 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81de3720-3193-39f8-b338-f2d51a7f410e | -8.1229 | -54.793098 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddb83946-50a9-3aab-a363-d302772a97d9 | -5.8218 | -53.809601 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9e0641-6c22-3e6c-9648-770de304ea56 | -2.9621 | -50.367298 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db77396-ac1b-3c63-9bff-7f795f42dacb | -14.5959 | -52.666698 | 2026-09-12 01:26:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3173add-f967-3d71-b3c3-972bae3648f2 | -9.1689 | -68.211098 | 2026-09-12 01:26:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14aae506-b5bd-3b3d-8ccb-63fcdee25541 | -6.1889 | -57.7188 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aebfb6bd-b35b-3188-9408-20abaa3613cb | -9.707 | -54.345402 | 2026-09-12 01:26:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29f33cc6-3a25-3b07-bba7-57a73b43e6a5 | -9.7127 | -64.970703 | 2026-09-12 01:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3964bfcc-7d81-346a-946f-47166f3e3ea8 | -10.5499 | -51.326 | 2026-09-12 01:26:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed2d64c-ddd2-3d90-8ec1-b0341d5f552e | -6.1171 | -55.6311 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f503035-7da6-3da7-a02c-982e67ca1534 | -5.7926 | -53.816601 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604427c4-1d3b-37b5-9a8a-ee2deb600f87 | -3.3713 | -57.712299 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8256263-8ff2-36aa-be72-7e25aa7d779b | -6.2119 | -57.773201 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c21b4e18-1e2a-3308-97fc-fb1255b9284b | -4.8681 | -56.013802 | 2026-09-12 01:26:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae56a0ab-d941-30e0-af89-6f52c9b2ddb1 | -2.7207 | -57.618801 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6358f8-9725-33a7-b90f-24b3be28ca29 | -18.884501 | -46.987801 | 2026-09-12 01:26:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8150fa57-878f-3d72-9c43-10e08f60bd11 | -12.1534 | -64.138901 | 2026-09-12 01:26:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ead6dad-a43f-3da3-bfe5-2996a7177bf8 | -8.1104 | -54.784199 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c5e7865-bbec-3188-be38-8f3cccf4c9ce | -6.3331 | -55.844101 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92d3746c-07e5-3f3f-80e5-de5077024d7a | -8.535 | -54.7048 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3661306e-2507-377b-aeb6-a72808eec32c | -8.3233 | -54.768101 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49b8ebf6-be3a-3b16-a0e5-0b5ef8d92322 | -12.1374 | -48.963799 | 2026-09-12 01:26:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| effe0c40-9922-3403-966c-432dd3f35867 | -6.6172 | -58.8465 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d36a9f03-4de4-33f7-9531-3cff86fe11f2 | -6.1927 | -57.7351 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2773d3b3-d247-3f28-a25f-c148885ef0ed | -9.1566 | -68.249397 | 2026-09-12 01:26:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4773c6f-92e2-38cb-afb1-e2456def58c4 | -2.7367 | -57.643299 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9a31f1c-ed32-3b96-9fec-f58538e86998 | -4.5331 | -54.953999 | 2026-09-12 01:26:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e59ea60-22b3-3b47-a796-16bf26bd531c | -2.9591 | -50.396702 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e328de-f54a-3ea3-acc4-dac1e8f8db10 | -6.6091 | -58.856098 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba5ae47-15eb-3392-accc-f4a514214684 | -6.5068 | -58.283298 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ca4f67-b076-33bc-9e3c-b8d733c41352 | -6.2427 | -51.677299 | 2026-09-12 01:26:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b13aa2c-9152-3e3b-8ea7-b95c109ed3f2 | -6.1099 | -55.6441 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9653d785-1eb7-3f30-b618-4ca2f7e90950 | -4.8196 | -55.766602 | 2026-09-12 01:26:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7152172-6fe9-332b-9f44-091ba1338eca | -10.6823 | -54.1511 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a87f364-4b3a-3706-bb51-49c0a762fad3 | -17.174299 | -55.9286 | 2026-09-12 01:26:00 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 378c009c-4fca-3150-958e-5f74c16899e8 | -6.3944 | -55.1968 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b8db9e-1cb7-3921-9a20-f93d27e2e16a | -6.0731 | -53.489601 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25e1c3cd-0461-38cb-a04b-6b56d2d6e19c | -9.7006 | -64.962196 | 2026-09-12 01:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8156d005-84de-35b9-ac36-cb40361f0063 | -6.1001 | -55.6464 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8300a4-cc19-366b-a358-3d343935fbad | -6.2475 | -51.696701 | 2026-09-12 01:26:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb1db36-d2f4-342a-b888-3f0fd72793e0 | -6.7726 | -59.428501 | 2026-09-12 01:26:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1130e132-5e33-3880-ac9a-994ef1805164 | -6.2814 | -56.016499 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dfff913-3726-3064-b9ed-dcd74dbc2f3b | -6.181 | -57.729198 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6565c2e2-457e-36b0-b29f-57cfcae143de | -13.2492 | -49.603401 | 2026-09-12 01:26:00 | METOP-C | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 981d7f9e-1def-3a06-9d03-c98ebf13cc91 | -3.7469 | -61.750599 | 2026-09-12 01:26:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad48cd3c-c2c7-396d-900d-64bac8058953 | -6.2778 | -59.922699 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c676f132-9b87-32a2-be72-cb66de5895ca | -4.3553 | -54.769699 | 2026-09-12 01:26:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6728dc5b-69ce-3b01-84e6-0295f2f1f4cf | -2.9495 | -50.399101 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05475b33-d3d1-31b9-9260-19b9d536ca78 | -4.8632 | -55.992901 | 2026-09-12 01:26:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f18335c1-8d93-367c-9787-35d39fdf135a | -14.584 | -48.836601 | 2026-09-12 01:26:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0511530d-37cf-340b-a029-96ffb67b1c13 | -6.8635 | -55.2603 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 394e3fa0-c5a9-36ff-9d2a-691650085c9b | -18.877501 | -46.963402 | 2026-09-12 01:26:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 778966f3-06a8-39a1-b1c5-a97458141d2f | -6.0695 | -53.4748 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b348ad3f-b08e-34cf-93c4-f30621c65366 | -6.8485 | -55.2407 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac71727-7864-3ff5-ab7d-548cd36c1867 | -10.2176 | -50.360699 | 2026-09-12 01:26:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1caf4b8-a1da-3f2f-9763-c371be6b8deb | -10.5544 | -51.343498 | 2026-09-12 01:26:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5ea9373-8a21-348d-96e7-f091ac244eab | -6.3355 | -55.854301 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7614d3cd-f44a-37fb-9f2f-f27efed49e7a | -6.0967 | -59.898102 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e512df9-f678-3581-ab23-78889ef96bf5 | -6.3839 | -58.287498 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 404bb6de-34be-3f94-b376-82cb69937f6d | -10.692 | -54.148602 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2c4e569-3ddb-3711-9e6e-0012efbed0ee | -2.729 | -57.654598 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac991d93-e6b6-30a2-9f4d-869a48b5d134 | -14.5862 | -52.6693 | 2026-09-12 01:26:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1df3f8b2-12dc-397f-90b6-6e14a1404d20 | -6.8511 | -55.251701 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef452178-c922-32d7-9184-424e9c511c62 | -8.2234 | -55.2505 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce30af64-4409-39a3-8a21-1b238f5ccb76 | -6.2911 | -56.014198 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36da9d28-fd86-33e0-b690-003fb1ce2b37 | -6.2935 | -56.024101 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24c8e314-59bb-38d7-ab30-888cb45e0e66 | -6.1074 | -55.633499 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18a194c1-6c03-387c-908f-4b3210962ddc | -2.9561 | -50.426102 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 641231a6-c803-3524-99b2-efc2becce7da | -3.895 | -55.820202 | 2026-09-12 01:26:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d8ee043-645e-3c88-86bc-50ecb6749457 | -6.1162 | -52.243198 | 2026-09-12 01:26:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abc85221-4a1e-3a26-9298-34d5c19a72b0 | -9.1884 | -68.2071 | 2026-09-12 01:26:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eea4863a-744e-3613-9762-a72ca4320e12 | -10.6879 | -54.173698 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 267fa1e5-ec94-3de1-b3da-120db09dbf95 | -6.3378 | -55.304298 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e7adb39-5233-3b17-ab32-42f20d15e942 | -6.2145 | -55.263199 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec373f61-22d7-31f7-813f-c94c5ccfcd55 | -3.349 | -59.436298 | 2026-09-12 01:26:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0803233-05f2-317e-bd09-4ab252662f2c | -6.233 | -51.679699 | 2026-09-12 01:26:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89dfc83a-d988-3a64-ab72-9931f550d0e2 | -9.1627 | -68.230301 | 2026-09-12 01:26:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aff47083-d76b-3036-af13-91f0630d7b2d | -6.5488 | -62.8881 | 2026-09-12 01:26:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42877fc2-2d7c-3574-94f1-32bd8774dec1 | -6.1791 | -57.7211 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91eb8d63-df04-37d8-a721-dc0cce205318 | -18.867901 | -46.9664 | 2026-09-12 01:26:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d46eac3c-0490-35e9-8e06-0a3de6591799 | -3.3571 | -59.426701 | 2026-09-12 01:26:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb049cd-f33f-378a-8178-73bf1edf0c10 | -10.2325 | -56.260601 | 2026-09-12 01:26:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8653f4-9248-3069-ab92-0dfc9fce558a | -11.2455 | -54.1292 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf9829f-cb55-3ee8-b85e-ebbb02d69658 | -15.9873 | -52.716999 | 2026-09-12 01:26:00 | METOP-C | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41fa95a4-fd9f-30bc-9733-3d5cad610b1e | -5.9833 | -57.766399 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec6e1c3-9e46-3b3b-8a8e-e79fc8fda4fa | -9.1663 | -68.247498 | 2026-09-12 01:26:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba1c7bc9-d3a1-3da3-8424-b9954dc876ed | -16.0338 | -52.654598 | 2026-09-12 01:26:00 | METOP-C | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
