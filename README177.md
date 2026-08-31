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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02d12281-0778-3677-b125-27510235a0a5 | -10.4794 | -64.5012 | 2026-08-31 17:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b80d9608-36e3-3210-a264-ddd20734f874 | -9.0057 | -65.456 | 2026-08-31 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| fb1fbb5e-dc59-36d1-bd88-c12234027395 | -6.8019 | -59.4008 | 2026-08-31 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 55e63af6-0f95-3970-941e-65dd211d917b | -8.574 | -66.9569 | 2026-08-31 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 83505f47-dd02-3ea8-bc25-99d65d0f66bd | -9.4345 | -45.6477 | 2026-08-31 17:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 797950ef-2060-3e1f-afa3-68ed34556906 | -10.7856 | -50.5066 | 2026-08-31 17:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c3e162e6-cfd2-34f9-bb61-19b52ed36f2e | -8.5555 | -66.9574 | 2026-08-31 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 471059d8-809f-3e23-b06a-b93400273375 | -3.3819 | -61.3657 | 2026-08-31 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 0f15c820-7871-30ac-9c0f-8118b293890f | -11.1542 | -51.2324 | 2026-08-31 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 96f34da0-8178-3040-925b-9ff7eeb3dcfd | -3.1266 | -61.2 | 2026-08-31 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e251caf4-5e1f-3f10-a88b-e66db270feaf | -8.739 | -45.3844 | 2026-08-31 17:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 517ba991-bc45-3505-b166-8dbf73b1d409 | -3.1998 | -61.161 | 2026-08-31 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 531d09f7-aef4-3ed0-830b-bd70f2159020 | -3.1267 | -61.1811 | 2026-08-31 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 957644a8-6821-3e90-8f04-ffb49e0599fb | -11.1995 | -55.1008 | 2026-08-31 17:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| cca5dfa6-40e3-3ad9-8486-02d8f784dccb | -5.9636 | -57.6704 | 2026-08-31 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| c2681d33-5805-332a-bea5-aed3eaba231a | -8.9428 | -63.2797 | 2026-08-31 17:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 93f30f07-9fc4-375f-8e94-51e2f608965d | -3.4185 | -61.3273 | 2026-08-31 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 89874ee2-563b-370b-a465-339b3f43d5cf | -9.4156 | -45.6499 | 2026-08-31 17:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f6d8775a-ab16-3682-a540-a6190a60e4b1 | -10.1528 | -45.7665 | 2026-08-31 17:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 4ed32ddb-943f-392c-943d-cd2fa7eeb81b | -6.1295 | -57.6637 | 2026-08-31 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3ef02456-9ccb-351f-9314-e3912ac8589b | -9.6939 | -65.1145 | 2026-08-31 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 4a7c258e-693a-3e2e-a734-5c7c89d46307 | -10.1531 | -45.7438 | 2026-08-31 17:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 7f21f4bc-931c-3991-85ee-96a815b5bc95 | -19.11 | -57.41 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 14024d15-fe27-3e4c-a4ce-e1edc6d2cb7c | -10.31 | -50.0 | 2026-08-31 17:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44f5b85e-8079-30e9-bbd9-d1cd9d667d46 | -19.14 | -57.43 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7bfecd7d-4eac-3316-9487-d7b525af05f4 | -19.2 | -57.4 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4fc47d3c-96f8-32ff-9052-06d731810b80 | -8.01 | -44.32 | 2026-08-31 17:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64b9179e-bf09-32ce-8682-1f86dccd6706 | -17.88 | -50.51 | 2026-08-31 17:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47524b12-2b31-32cc-babf-1df9a3a95474 | -19.2 | -57.33 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| be12f920-9766-3819-8638-ef06329fa117 | -19.17 | -57.38 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2bbf527c-8d7a-3e90-b68a-08b67fcff898 | -17.89 | -52.09 | 2026-08-31 17:15:00 | MSG-03 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4054c2d3-6f67-3492-a469-01e3bb4ecba1 | -19.23 | -57.35 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4a505642-bed2-3eaa-9a62-c0cf8fcd23fa | -7.98 | -44.32 | 2026-08-31 17:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 941ad724-f78f-32d9-8ca2-2f02170c56d4 | -17.85 | -50.49 | 2026-08-31 17:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eced755c-e73d-3503-a7c1-beac5cf48e0c | -7.92 | -44.26 | 2026-08-31 17:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9f7712-a6c9-38e3-a8d6-62aef4ed5ec6 | -10.14 | -50.34 | 2026-08-31 17:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0e18cd-4b73-3432-8801-fdfcc9401e0e | -10.11 | -50.33 | 2026-08-31 17:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa9aa0e2-3b75-3f72-9f07-01ba10a4c98c | -19.14 | -57.35 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 982d6d27-d4cb-3bc9-afcd-52845687d952 | -19.1 | -57.33 | 2026-08-31 17:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4c35348b-72ff-3bc7-b231-35400771258b | -17.92 | -52.1 | 2026-08-31 17:15:00 | MSG-03 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7013cb08-a5ae-399e-a766-074cb438a1a9 | -9.1709 | -59.6374 | 2026-08-31 17:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f79e0951-9d5c-396c-8ebd-49ad5d65a8b4 | -5.9636 | -57.6704 | 2026-08-31 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ce26dde5-3a90-36b0-bab8-54d69877840c | -10.8046 | -50.5046 | 2026-08-31 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a3f1e687-46db-3b7e-abd9-845e364054a7 | -7.4736 | -61.3656 | 2026-08-31 17:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f7917e78-b8e3-3740-9a66-a5df5039a1f6 | -3.4002 | -61.3465 | 2026-08-31 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 46abad0f-005f-3251-b164-e5fc4ce0c24d | -10.8212 | -50.6732 | 2026-08-31 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5f43a0ae-5562-352c-8f05-2dfb5a44a6f9 | -12.1905 | -50.5194 | 2026-08-31 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 54896f50-eb5d-366e-aa18-4d34604ab54c | -8.7628 | -46.4642 | 2026-08-31 17:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 0412dfb7-337d-3e60-b166-df53aadd463a | -8.3717 | -62.716 | 2026-08-31 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8c78f14b-0044-316c-b499-3b713f57d4a7 | -10.5793 | -50.3789 | 2026-08-31 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 1598ae87-db75-3d99-b5d6-9433840174e2 | -11.0244 | -49.6872 | 2026-08-31 17:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c2893fcf-a879-3cd5-a36a-23b1531e8e2a | -10.8614 | -50.4985 | 2026-08-31 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7f7cbbb5-2c39-333b-80df-230bc70fe4f5 | -8.631 | -66.5473 | 2026-08-31 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8d3031e3-b682-30df-b8ce-ed4a9c71ed5e | -9.1523 | -59.6384 | 2026-08-31 17:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d54671da-01ea-3937-b090-9b1f2f5307fc | -10.746 | -50.6386 | 2026-08-31 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 885798fc-49db-3506-be08-9ddb8320410b | -9.6939 | -65.1145 | 2026-08-31 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 242.8 |
| a51124f3-e9d9-3876-9f67-b5075b7a154b | -12.0925 | -47.1587 | 2026-08-31 17:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c61233a3-e673-30ad-a1b1-a5059df1688a | -10.1531 | -45.7438 | 2026-08-31 17:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 5df685c7-1f4c-3518-b44e-8469f7cc63bd | -3.4185 | -61.3273 | 2026-08-31 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 7730969b-ac88-31ca-a69f-cfdc565d3a7b | -12.1902 | -50.5409 | 2026-08-31 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a0fa9d07-80ed-3024-8dc4-1e191282cb43 | -10.7081 | -50.6425 | 2026-08-31 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| fe1724e0-b62a-3cd9-a7d2-f6b5dda57d5a | -9.12 | -61.6011 | 2026-08-31 17:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e9a08a0e-ecfe-3815-b1f1-97423f7e7439 | -9.1895 | -59.6364 | 2026-08-31 17:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1555337f-00df-3fbe-b402-fec10dcce0b7 | -10.7827 | -50.7198 | 2026-08-31 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 128d6369-6dda-3017-8703-4a3fb3a2e3c0 | -11.1995 | -55.1008 | 2026-08-31 17:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| db6ee730-0735-3a04-be2d-136b7a80034f | -6.1295 | -57.6637 | 2026-08-31 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6e29ebd6-b606-3a34-b0eb-2f1d61b3a11f | -3.1267 | -61.1811 | 2026-08-31 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 773b2a8d-6829-38d3-8a1e-c5d08d8240e0 | -9.1708 | -59.6568 | 2026-08-31 17:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6b4cb309-2772-384d-9e35-371e9877abea | -8.6852 | -62.9496 | 2026-08-31 17:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 6a8d6d0d-eb01-3766-894c-948426d2f798 | -3.4002 | -61.3276 | 2026-08-31 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f06f69b6-53b6-3f31-bc31-c49db21042e0 | -13.4194 | -51.3945 | 2026-08-31 17:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 641d6f36-a393-3055-b75d-d7583ff30e46 | -9.0057 | -65.456 | 2026-08-31 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0c2b980e-03bf-3534-8ea6-ecf60c53803b | -9.6941 | -65.077 | 2026-08-31 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 337a18ac-d933-343f-bab6-e675849bb98e | -13.471 | -57.0373 | 2026-08-31 17:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 198.5 |
| bdd97821-0c3a-311f-8aeb-dd1989d13d81 | -10.8215 | -50.6519 | 2026-08-31 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| e0c1debb-0a3a-3c06-8666-0b17a517f78c | -10.7271 | -50.6405 | 2026-08-31 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 1f1c76c6-239f-3dae-972f-6e73f1e6b7cb | -3.9707 | -60.0258 | 2026-08-31 17:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1b555347-6aa6-351e-a830-78326edf4e23 | -10.8617 | -50.4772 | 2026-08-31 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 267123e2-08fe-320b-bbfa-5364f55518db | -10.1538 | -45.6982 | 2026-08-31 17:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 4b445ed9-debf-30e7-b023-9aac174bbd6f | -9.7126 | -65.0951 | 2026-08-31 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 110.8 |
| d50c6e3a-0bcb-39cd-bdf7-8a5238b4786f | -10.1528 | -45.7665 | 2026-08-31 17:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2ec2483b-ebe0-377c-bfe7-822e67544f4e | -10.7428 | -50.8727 | 2026-08-31 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f1a90446-b172-3f0e-a760-d0d4b2489ada | -7.685 | -63.3255 | 2026-08-31 17:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4f0a67bb-fc36-3a80-9679-35ecfbcdd792 | -8.9428 | -63.2797 | 2026-08-31 17:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9b030976-0e2c-3ecb-82df-222648462c5e | -9.694 | -65.0958 | 2026-08-31 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 165.4 |
| b0e5d630-7995-39a0-a7a8-51a41cf898ec | -9.4342 | -45.6704 | 2026-08-31 17:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 7491b9de-be31-3a4e-83fb-d5595f2cc656 | -12.1714 | -50.5217 | 2026-08-31 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 63722e37-3ed9-3ae3-891f-07f910979372 | -6.8387 | -59.4186 | 2026-08-31 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c761d427-0791-359e-88fc-3938da551d4a | -8.948 | -62.3894 | 2026-08-31 17:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8bab2f4d-afca-3a35-b276-08e5b3b93d05 | -8.7579 | -45.3823 | 2026-08-31 17:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b873d050-502e-3619-8482-c56bb2df8c12 | -7.36681 | -35.58227 | 2026-08-31 17:26:00 | AQUA_M-T | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 27f89283-de22-3770-9e2b-5205050a9682 | -6.64416 | -35.07694 | 2026-08-31 17:26:00 | AQUA_M-T | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 44.5 |
| 492daa7c-75c8-372c-8d6a-7c7f831d2499 | -11.1824 | -50.5706 | 2026-08-31 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| ecb483c2-9944-324b-b16f-96a680c3b3e1 | -15.2669 | -53.8851 | 2026-08-31 17:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 463.7 |
| 14ff0015-bc3b-305f-a941-ff2ebd72932a | -9.6676 | -47.9429 | 2026-08-31 17:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7c71652b-e6ab-3e17-b06d-a03cd02e261b | -11.0247 | -49.6656 | 2026-08-31 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ea9da303-b7f8-3475-952b-47293afa8d33 | -6.7123 | -58.9412 | 2026-08-31 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b3e39243-bc2d-3d75-8fdd-33484bc03ac9 | -8.3944 | -72.5825 | 2026-08-31 17:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 405e550f-fe09-3467-a8f4-b8aac90e3dc5 | -8.9002 | -68.8899 | 2026-08-31 17:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 8ec3a3b1-b1a0-30e5-9636-e4b0f9a02b16 | -5.9636 | -57.6704 | 2026-08-31 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |


[Clique aqui para ver as próximas entradas](README178.md)
