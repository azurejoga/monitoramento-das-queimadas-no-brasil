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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ace232d0-9073-3dcd-b9f6-7588ef86b72d | -16.48113 | -47.95536 | 2026-09-01 05:18:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| cb2f5f82-b70b-3b28-b43a-d511792b4ebe | -14.40636 | -52.50405 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22d7c648-b86f-30df-8dcc-93b0d7d89665 | -14.41909 | -52.50206 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 094e932b-fabf-3125-84d3-f86a66f9cce0 | -14.71728 | -53.56796 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6f746da-e823-3ae1-9574-0457faf06adf | -8.51219 | -67.13757 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b5935a4-401b-3e67-9ff3-3794373b5e36 | -9.08442 | -65.4993 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d58195f2-1e19-3d14-92da-30c3dd815f97 | -14.39266 | -52.51328 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 910bf1c1-1ac0-3205-9307-91e507e1f961 | -8.86925 | -66.77198 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f67453fe-ee68-34b4-ba86-4531979dc5dc | -11.92363 | -45.08902 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98a1c785-3b6f-3e9d-8b1b-46642fc0130c | -10.49936 | -59.61395 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79e14f6c-f36a-38db-83ac-6bfaffa0f987 | -15.65934 | -48.7102 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d90c97-1630-3fa9-bd5d-a8ae49a32e22 | -11.18875 | -55.1117 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f710cfe-f8dd-3589-8bf1-95f5779e675d | -14.50601 | -52.2347 | 2026-09-01 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4eede726-0455-3f85-9372-4d0c92817b20 | -15.02664 | -52.76885 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c87c37ca-6f9c-3c59-8280-fa007fe8efac | -14.4471 | -52.5099 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 168c2313-1d42-3765-9929-e4b7a0c0a0cd | -10.41708 | -57.22736 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff5ce629-9714-3bfa-9023-1fdc6110c940 | -16.05534 | -54.3868 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2abbac5c-4be4-35dc-b00d-af2c2e7a99dd | -14.71592 | -53.57765 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e393869-9e81-342d-96d4-0720cb77a74e | -10.50224 | -59.61862 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3961efad-22ba-3e37-9852-09bf3e5175cc | -14.45579 | -52.50714 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d71ce12-2d9f-35a5-9534-caf1580cc236 | -15.48878 | -56.00786 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92785d99-871a-318a-94e1-503a5e06b37d | -14.39623 | -52.5176 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc12203-416b-3659-ab62-a3e569fc8a46 | -12.95743 | -45.95951 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc67028d-561f-3f28-a1ef-bbf60f6770e9 | -14.57106 | -52.10481 | 2026-09-01 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bdfd3e2-3f6d-3d86-bb4b-f87b324acc45 | -11.9048 | -45.07224 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18b8275e-b741-387d-8960-d32319229f59 | -11.30248 | -50.57312 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 39706993-c395-39f8-9618-1beec026b0d7 | -10.41928 | -57.23494 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9637fc08-dcb9-3bce-ac8d-69bffc5b4cfe | -9.8903 | -60.2728 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 175976f7-7686-32b6-93e6-42cd7e88e671 | -13.9563 | -54.39824 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ae6ce3a-20b1-3a12-84e3-ecfe43d85505 | -14.46345 | -52.51188 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 252c0b81-5fc5-318a-bf6d-02d7cf0b6358 | -15.87078 | -56.48333 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da66c929-17b9-3ee1-8592-d926d6290f51 | -14.44763 | -52.50608 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1af96358-69f5-3d7c-97ec-1a2e74ff0ee8 | -10.76817 | -54.04466 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1e623ba-1568-3dd3-910f-2179a2af96d8 | -8.77317 | -69.33713 | 2026-09-01 05:18:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1db44a36-6172-3c2e-9f38-f0a8843d6dc0 | -15.65067 | -50.10336 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78d9d1e9-38a6-3c47-92d4-c1dae4e97a38 | -11.6676 | -47.59708 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da1b881b-4079-33c7-9ea1-66947166b0f5 | -14.58049 | -54.077 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d82714dd-802e-3961-9b4f-c16a9429b49f | -14.39723 | -52.51019 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ca339c9c-f697-304a-8691-fb28aa07a576 | -15.65972 | -48.7069 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d5c75a3-12dc-3f43-beb8-3d661f0dac4c | -9.89253 | -60.28225 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 079103db-c35a-3c12-89cf-15aaad8d91ba | -9.02799 | -65.45182 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db3aca9e-0401-32db-ac35-a0ddefbda716 | -13.46904 | -57.03583 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 051a2ade-0c12-34de-9c47-950c09ffed66 | -15.42942 | -52.68743 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97d39e89-de83-35d0-97f1-96a578f30f4c | -9.79433 | -60.17612 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50ecfa1b-8837-3b58-9048-083f7177c9fc | -14.72982 | -53.58985 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af2f0d1b-a15d-3e60-8d55-b3a2b68bcf69 | -11.26836 | -50.56934 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18a62c65-7d2a-3b79-b1bf-c66b0c93ec7f | -11.66539 | -47.61437 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59b56ce4-6b6a-3049-b046-bd85a3ee2247 | -11.91054 | -45.0787 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66fd1506-9662-361b-b205-53b30e24beac | -12.95622 | -45.96009 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a525e3bb-18f5-344a-8602-8045c7eacecd | -9.62289 | -68.59857 | 2026-09-01 05:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14d4c4a5-965e-34b5-8335-981f39589c4c | -14.66951 | -53.54586 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 04c5ed36-4f14-3bcf-b696-8e6c906d6ae2 | -14.3821 | -52.53022 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f5eb330-f082-3cfa-a9e0-e6cb99dcf730 | -11.19961 | -55.10954 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08521785-f0d8-30ec-ba17-904087a9a9ce | -15.63157 | -56.38473 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45a37596-aefc-3c2d-a536-93d0c62b6d0c | -11.30691 | -50.57375 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9eb49bfc-9ddb-3d2b-b42f-c6bd86a31929 | -15.39727 | -52.71379 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 719ddc74-60c9-3cf0-9be9-19b4bb035060 | -14.12813 | -52.7926 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 310be290-329f-3ede-9514-11e00e65c217 | -10.74383 | -54.03669 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dc2a018-c661-31ff-8ea3-2fba12938d6d | -13.45016 | -57.04734 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 543cc238-979d-3cd3-8265-1f960f9b98f6 | -15.83576 | -47.68944 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 502050e0-0435-38f0-b096-b7affb6faa8d | -11.09954 | -51.56733 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fe1020d-e82c-3086-9e4d-8e27c7075e03 | -10.57308 | -57.48086 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7dea570-f2cc-301a-9ec6-5b8763c33031 | -15.21817 | -56.35079 | 2026-09-01 05:18:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98ddc0ae-01e3-3029-88b7-033c4d682191 | -12.95003 | -45.95953 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21d3106f-06dc-3598-920c-b56668f889a2 | -14.43032 | -52.51109 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 330d1838-f201-3beb-95d2-423054711816 | -10.7753 | -54.04569 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 989ea645-8eed-3025-a5af-4cc0b781770a | -10.94537 | -61.65858 | 2026-09-01 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c2ed6db-522c-341a-bb11-9dd433e37226 | -13.95142 | -54.40623 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7fea5ec-4010-3862-9bb7-e98a7f76a7d6 | -9.03817 | -65.39721 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fcf2205-cd7f-3b34-8192-4a4a5e7d1b8a | -9.61653 | -68.59746 | 2026-09-01 05:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d1fe5b-7d20-3543-8aa5-14cde612b06c | -15.01455 | -52.7669 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edc65ff1-a92b-3840-ba4e-52fcdb5ec4fd | -15.83617 | -47.68562 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 951defe5-b20a-3fbe-9c6a-abfb54c10af8 | -10.74565 | -54.02447 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 051e9061-638c-307b-ab86-63160fed61c3 | -15.66425 | -48.71453 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3694dbfb-ffaa-3617-a966-2895432b4452 | -12.09449 | -45.03145 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57f3d176-3e65-3d1d-b444-a335cf51ccd6 | -10.41868 | -64.45734 | 2026-09-01 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e17af179-18ae-331c-be09-e5ef550cc3a8 | -15.24653 | -53.84814 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f87ce135-289c-3e79-a5b1-3c20de89206c | -15.17299 | -46.2408 | 2026-09-01 05:18:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2b0dd19-e396-3e55-9f7c-59385dea9b2a | -15.24585 | -53.85289 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19c5ed90-4da9-3899-9e12-d9abb92fbbc9 | -15.40292 | -52.73305 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fbb4cf6-f43e-30d3-bba0-eefe416072db | -11.09902 | -51.57109 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9350744-bda3-3807-b9a8-6208818c6e0d | -11.68985 | -54.54652 | 2026-09-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8535b4f3-933f-31a2-abc9-99b54b70fbb0 | -10.74027 | -54.03613 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78cb5517-1479-38c6-b3c6-01f5443cebee | -10.74679 | -54.04133 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4af07e33-db1f-37d8-81a3-57c5a0498db4 | -15.42989 | -52.68387 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da4698e4-2a9a-339d-ad4e-587b985ed31d | -14.39021 | -52.53157 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4a1eba4-0431-382c-9c06-894ba1372eff | -14.47025 | -52.51562 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e86fc40f-735b-33c8-a929-7a75a6d55888 | -11.1767 | -55.10221 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8621f9f-3a23-3516-bfcd-aceb5697368d | -14.40985 | -52.4782 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9580ef3f-fac7-3367-a2bc-dcb5f4615b9f | -10.758 | -54.0639 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c8af9aa-e7a0-39d2-af12-d744fc347520 | -11.29448 | -50.6086 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c92b0a6-03c0-3537-96e4-ca106b7d232d | -14.97323 | -48.14159 | 2026-09-01 05:18:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fcfdc33-ccaa-38fb-b75a-244a522a9cbd | -8.86772 | -66.77994 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fecef41d-fd5f-3ed2-9c58-bc5f6578fd90 | -10.75087 | -54.06284 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eef83c71-f008-3214-b9da-d4b1a4827036 | -14.39773 | -52.50647 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62a4894f-21dd-35cc-b84f-5257f9b4da81 | -10.74444 | -54.0326 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09adbf18-b758-329f-ab3b-cb767cad7792 | -9.79359 | -60.18048 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e7d679a-f541-3716-bd21-6f7cc18e7b64 | -14.72354 | -53.57903 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b08bdc34-d0fa-3d0b-8eb7-94bbba4eeb96 | -9.00534 | -67.8031 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cdde04b1-adbe-376f-9e09-b9837df108f9 | -11.91249 | -45.06258 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README68.md)
