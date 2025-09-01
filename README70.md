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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db256fe7-0308-3fe6-890a-26466fc7ccaa | -12.78681 | -48.08666 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b22ce3be-7a35-35f1-91f5-c1220b02705d | -12.80137 | -48.08141 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b24d12b-3668-350a-9c09-2edc581a318e | -15.58824 | -48.3246 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 81c58cb1-370d-35bd-9224-32676aa28916 | -14.78932 | -46.72596 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d1030efb-deb1-3c2c-ba15-22c4246628bd | -12.06773 | -46.66067 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4a1f3fa-cf0b-3c69-a4cd-b3baf5a9be2c | -11.68249 | -47.5679 | 2025-09-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e3c55cc-18c1-3243-a599-b2385d0cca02 | -12.95436 | -48.10523 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 863a7cce-c6bb-3ab2-9218-e7f56286116a | -12.78737 | -48.08292 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a88d0267-3832-3ba1-8b5c-b93a99bb5a32 | -11.42487 | -46.88555 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c1c2005-3677-3076-9c60-3e1e9c4c6a79 | -11.59766 | -51.94791 | 2025-09-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11c9efd6-38f0-3331-988a-c5a27818e95e | -16.07748 | -43.61991 | 2025-09-01 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34331612-c71a-35af-92dd-efdddbebb250 | -12.86912 | -48.07703 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75ad69be-55d8-39e5-8868-354ba6e6f4a7 | -15.69277 | -48.93216 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d5efc98-5461-34b8-bb83-57c7c7fe96f9 | -12.80415 | -48.08577 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c38dadf-ec9b-3874-bcf2-41a79e275e6f | -15.16532 | -52.3472 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aca53150-a307-321d-8825-07000b1ef229 | -11.42666 | -46.92097 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb5c844c-5153-303b-a1e6-27558b890034 | -11.91553 | -46.44681 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c5a3b52-3984-39d3-95f9-48e055970b85 | -10.88025 | -55.7585 | 2025-09-01 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15cf318c-1e92-35d8-8ff9-71898c095cc0 | -12.30431 | -45.71683 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4880688c-4dbe-36d0-95c9-cee36d76ae57 | -11.79982 | -46.42346 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 18591ec9-f7f4-340d-8e74-0e552cad7a87 | -13.70091 | -46.89935 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7324680f-741e-31c2-adb2-d9519805a8af | -12.87716 | -48.15994 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5459ff4-270d-3ea4-ba09-8e8af000cc0f | -11.9304 | -50.62604 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31793f71-3451-35bc-9799-33217908f220 | -11.07531 | -52.0593 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eef98deb-1e48-3152-ac45-1158b9909d61 | -17.20488 | -46.06795 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 796658e8-cf57-30be-a395-7d350974f7e1 | -15.32642 | -46.10698 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28205f6a-ddce-3a5f-b642-38659348e301 | -15.16252 | -52.34256 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81c48f7f-874a-3c02-8cd6-b272b896f03c | -13.34761 | -47.0466 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56c260ed-331d-3fd5-a6bc-5b64134675dc | -14.77173 | -46.75971 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27b3a57b-7ad5-39c4-b163-5f4d5ced4757 | -14.7496 | -46.76073 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c1a5bd13-007c-3e2e-953a-8cc0f2d398b5 | -16.97448 | -49.31349 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eec6ed6-fdef-3908-9909-6c282f29d44d | -10.77024 | -48.83636 | 2025-09-01 04:34:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92ec6cea-9887-3841-908d-6b9a42e467f3 | -14.73775 | -46.74126 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b647b8d7-a3d8-3c18-971f-af43d7ea4000 | -11.8366 | -51.47276 | 2025-09-01 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ef9fe13-a717-31b9-9192-40cf6fba0b8d | -14.56128 | -52.99086 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5b54c88-51ee-319b-98b5-e1e535eea66c | -11.51332 | -54.47173 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eddf6013-2e66-3bb1-b3e5-64a4afcb2684 | -17.14455 | -46.09026 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef732a64-d324-3c91-8601-e90f19576a53 | -14.6427 | -43.96204 | 2025-09-01 04:34:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6be7536e-9421-32f8-9bc5-73036db89b5d | -11.3763 | -43.62749 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab184be3-f609-3160-869d-ec95f9b150ce | -14.6017 | -54.48615 | 2025-09-01 04:34:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e70db382-1ae2-3e25-ad70-1ada7204e863 | -13.47536 | -46.93682 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dacd92a2-8a30-3d36-a5da-77eb4f76c16d | -15.59452 | -48.35223 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4aad341c-211d-3f45-832c-dbccf68831b9 | -11.79094 | -46.4345 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26eb8444-fdbd-3d4f-abac-3bc6d4b1b8e5 | -17.83121 | -44.32906 | 2025-09-01 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7be7fad7-705c-3588-ad25-e0daa4bf270f | -17.14369 | -46.08774 | 2025-09-01 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa50f50-7456-3730-bf55-cd1469fd8b61 | -15.22109 | -53.79159 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6654a5a-a5ad-3460-9e51-16f86439519f | -15.6989 | -45.42048 | 2025-09-01 04:34:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61fb31e2-be83-37ae-bf97-b9f903a63188 | -13.68758 | -46.91673 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8661f7dc-21ed-3268-bf94-5dfa383b0800 | -15.72738 | -48.99747 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 25b68ebc-f95f-334c-8a8c-623f992b7f35 | -10.23808 | -51.12101 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4feca3d-b08f-3c6c-b714-2f5cc6be0cc9 | -10.67884 | -51.56795 | 2025-09-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf0b4e6c-a029-3a36-861e-8683c1c15c45 | -13.49017 | -46.98271 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e62218b-1231-366c-866a-a7d95246dd1a | -11.02423 | -46.9473 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49bccae2-f430-3b4f-a153-690e6ae6de0f | -12.56842 | -48.20774 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 316e0464-1bf1-3962-a137-aa0b46aa4f51 | -13.1668 | -45.27835 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3d18d079-44f3-3345-93c6-29e107afa763 | -17.16345 | -46.08574 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80c654f4-ff9a-3a8a-83fc-5c8504b3969d | -13.40232 | -46.9417 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f39468e5-2798-3ce7-a703-6b6fce1c0868 | -13.17208 | -47.20134 | 2025-09-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b73a5f9-0d3e-3b07-93ac-6a2663c6faa2 | -11.00762 | -46.94096 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12a40d4d-d9ee-3aca-b8c0-da8e29bc5e3a | -10.48043 | -51.62671 | 2025-09-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e552936-0433-385c-917f-b22c3c8b473c | -11.52348 | -54.46211 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bb335e0-1461-3d8c-9815-c2fbe83a54c1 | -11.03509 | -47.0377 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f761e8d-3e9b-3f50-bfae-90a83c978e16 | -8.75854 | -61.42793 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a1d4d414-4fcd-3833-a910-f748a1cec75f | -11.90412 | -45.0396 | 2025-09-01 04:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 437e20dc-37d4-3235-969e-10999490259c | -12.60024 | -48.22392 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a67c2062-3f0d-3686-a731-c5400c5bca97 | -15.22852 | -53.79299 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69ddb9a0-a38c-39f8-8de1-adac7124af9b | -11.03737 | -47.04574 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f6a4809-98cb-3b7a-915a-d5210c54934c | -14.7407 | -46.74622 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70131137-2f0b-38ac-a339-c318457ed443 | -15.58657 | -48.33569 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41e037b8-1d18-3c26-86d4-4ad69e0ed4ce | -12.7801 | -48.08551 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91a9a4da-b6d9-3dd4-ac10-fff401224690 | -11.37119 | -43.57269 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b8d195c-7d22-3499-a59f-be6f70703d78 | -11.45704 | -46.81197 | 2025-09-01 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bec4a4ed-58d0-34d0-8656-394d40a0b069 | -11.84653 | -46.78521 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67403b4f-dc07-3017-9a30-0450ebc0e222 | -17.20105 | -46.06736 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 253e5f91-834a-3ad7-a667-1c383b15dc11 | -12.32938 | -45.72508 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f66779e-bbe6-327f-b753-d15718e093a7 | -16.23821 | -52.6952 | 2025-09-01 04:34:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80380119-478d-31c5-a0ab-b4a2f4359a0e | -13.3766 | -46.94598 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c44527fd-e1b0-3fea-bea6-0eb8fc035bd3 | -12.96862 | -48.11419 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1dfa6251-ead8-38b7-973f-c119571b6ce3 | -12.97254 | -48.11105 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d84e905a-52cd-3f55-8d57-8a8c79d7379c | -11.94917 | -49.17744 | 2025-09-01 04:34:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b974430a-80f0-33a6-a720-2e7aee9bbc58 | -13.50185 | -46.82867 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b1efa6b-a490-377c-bad7-1f6ff9ca1466 | -15.59902 | -48.34541 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8d2886c-ebb2-3670-a336-50a6a4ac5e83 | -11.01854 | -47.05441 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02c2463f-96c6-3292-baae-76a75396897e | -11.68193 | -47.57157 | 2025-09-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c3da012-6597-3e2b-9970-b96d7ea31d4d | -8.62799 | -62.59544 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83b2ab25-c2a3-3b7a-b8bd-444f96b467d3 | -14.53569 | -51.95387 | 2025-09-01 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66060931-8b53-38f5-a039-5ae0da42719a | -8.75611 | -61.44013 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6d071c5-e2d4-3680-ae2f-530711153000 | -8.72519 | -62.40055 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58b64072-86b9-383e-a153-35b82a20ae57 | -8.76524 | -61.42927 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45246898-efad-325d-b6e4-394b10208187 | -11.80402 | -46.4189 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bfa8ef58-4625-3d46-b717-cc2176702137 | -14.48988 | -52.98822 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 461453dc-52c9-3d75-a7fb-d3f6e4074cdb | -12.0584 | -46.65117 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef42bb16-7da7-3318-b226-6eb3ba01928a | -12.9759 | -48.11156 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0ce9c4dd-d930-3028-8cef-404817b9fcc3 | -14.74304 | -46.75537 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ebc77e8-465a-3829-8c93-772a2504ada0 | -10.5044 | -51.79033 | 2025-09-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c6ce110-66dd-3c0a-9bc1-a4c6872bb60f | -12.85849 | -48.0682 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 750f9b5f-46ac-3d56-99ba-c7e2f4d154e7 | -13.65246 | -46.93369 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d550fdc2-ff50-37b5-a044-0196c2428ac8 | -14.04684 | -44.55904 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50b7d3ab-d154-305e-a8a8-da8bdf67e1ff | -13.33481 | -46.85913 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e015c4a4-8bed-3c04-958f-4e4f0763505d | -13.37719 | -46.94192 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README71.md)
