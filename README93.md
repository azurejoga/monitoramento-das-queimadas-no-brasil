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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91371fd4-184a-3527-bae0-c38625bf8d76 | -5.678 | -41.3987 | 2025-08-24 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 137.5 |
| 5b58eb9c-156d-3a0e-8170-dd03171bab79 | -6.4357 | -44.5535 | 2025-08-24 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 462.8 |
| e16e966b-a534-38ff-86b9-862087178cb4 | -8.5272 | -48.8393 | 2025-08-24 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 91.1 |
| c4e8ca6e-42e1-3f87-a993-c73b410a4ca3 | -9.2083 | -59.6161 | 2025-08-24 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7a7f8d2e-23b8-3927-b03e-9cc302ee47b5 | -10.4587 | -46.8781 | 2025-08-24 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d6f31589-d160-31ef-8fde-ef3483a27741 | -5.5858 | -43.2562 | 2025-08-24 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 66ae1051-dc10-38dc-ae94-2c9561c1a16b | -5.4181 | -60.1784 | 2025-08-24 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 44e99d70-feae-348f-9eb9-e7544dd13541 | -15.112 | -48.6459 | 2025-08-24 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 134e423b-1e20-380c-b00a-34dfe7f1fcfd | -5.6628 | -45.1586 | 2025-08-24 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 264.5 |
| f41b784c-7f7e-308d-80c0-cfb04b23e116 | -10.4777 | -46.8758 | 2025-08-24 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| dd071aef-965c-3b36-8dfb-809a10877795 | -7.9078 | -63.0542 | 2025-08-24 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 772e4f7e-0e12-3725-ae02-a5ada1e50142 | -12.7463 | -48.1153 | 2025-08-24 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f26e5989-43ab-3828-af04-96b77d363889 | -7.9447 | -63.0528 | 2025-08-24 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 183.7 |
| aa8af073-ad65-3f7f-a59d-af8f7f2abd45 | -5.4365 | -60.1588 | 2025-08-24 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 547dfc2c-6814-3325-98db-9af3c684dc01 | -8.4833 | -49.4032 | 2025-08-24 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 0cf7e28d-8eb5-372f-92ee-5aa7a4a87600 | -9.5702 | -48.1724 | 2025-08-24 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c17c3f44-6b82-3613-aa66-db79d814f783 | -6.436 | -44.5306 | 2025-08-24 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 8a165aa2-d352-3b6b-850c-862d51f73d23 | -5.6404 | -43.4386 | 2025-08-24 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e2d3d3cf-2b87-346c-a2d5-2d06190fd876 | -8.5458 | -48.8592 | 2025-08-24 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 41ac38b2-796f-3db0-a8fd-539130acba7a | -6.3431 | -44.4465 | 2025-08-24 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 00cc3129-0b33-32ec-959a-0118e4fe0224 | -10.9145 | -50.7698 | 2025-08-24 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 310bdd5e-1121-33c3-b451-299a664fa5f1 | -8.527 | -48.8609 | 2025-08-24 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 122.3 |
| e52639e4-77fc-3173-8f2e-0b0c5a03902c | -8.7769 | -49.9763 | 2025-08-24 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6ce99d08-dcb1-3b20-9c1c-4c357afd59d3 | -5.4364 | -60.1779 | 2025-08-24 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 524811e3-6288-39f9-b414-f25a35deba1b | -10.4774 | -46.8982 | 2025-08-24 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 509ba2dc-cea6-3b1f-b2c3-d09d0f63d7f7 | -10.5937 | -44.331 | 2025-08-24 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9edc2fbb-af4a-3c23-b7bb-30b7cf1f00cb | -5.663 | -45.136 | 2025-08-24 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 329.0 |
| de8e7b88-7571-3ae1-8e22-d9fbb7c8aab1 | -11.9867 | -61.0214 | 2025-08-24 14:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2d5d0bf4-ef3f-332b-b691-5e8771bea9f3 | -11.5921 | -46.2363 | 2025-08-24 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d0fddd99-d57d-357a-9ae3-a9db542561f6 | -8.2336 | -45.0959 | 2025-08-24 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 3c25e4df-e8b7-31ca-acf3-edbca2dc953a | -10.6006 | -50.2058 | 2025-08-24 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 57dd87ae-b99d-30a0-9cc5-a85e3f2377c7 | -8.7375 | -45.4981 | 2025-08-24 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ae420122-2553-3974-9dbf-2a0aa37260ff | -11.6112 | -46.2337 | 2025-08-24 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| ddf25928-cc1b-3cd3-916a-946c5ce363be | -8.0685 | -49.6524 | 2025-08-24 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| b3db9e3d-be8d-3b37-bf42-9e5b083e50db | -7.9446 | -63.0717 | 2025-08-24 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 35a9b76e-6f2e-3fe4-ba00-39ea02b2a834 | -7.9263 | -63.0535 | 2025-08-24 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 998c3c84-9836-3549-899b-2d673800a492 | -6.1963 | -44.1134 | 2025-08-24 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9dfa17fc-36c0-3568-9eda-5e2ba40e5e1e | -8.5267 | -48.8825 | 2025-08-24 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6f7e0bb3-922e-331d-af8a-dfc365761935 | -10.3087 | -46.762 | 2025-08-24 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| d605246d-41f6-3f85-9e1a-fac68df54839 | -9.5705 | -48.1505 | 2025-08-24 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f4910226-fc19-3671-aa6b-d85fc6e79c60 | -10.8075 | -46.4308 | 2025-08-24 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 11d41b5b-d503-36c4-b488-50a1eae81ebd | -10.4584 | -46.9005 | 2025-08-24 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 6e5a5397-9aed-3177-b23f-59ffd7c03986 | -8.7378 | -45.4753 | 2025-08-24 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 24f9b0cf-718b-3dbc-a7c8-0bcd09a7dc4a | -8.7591 | -46.7547 | 2025-08-24 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 19bcd412-e6e3-377d-9b54-13035907e9aa | -7.9446 | -63.0717 | 2025-08-24 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 49c2c30b-db03-3b51-a2b6-4ca35e644d24 | -7.9078 | -63.0542 | 2025-08-24 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e26d999c-9001-3352-8995-c798d59d3947 | -10.5937 | -44.331 | 2025-08-24 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2a715543-0a92-32ec-8115-f43829c8f3e8 | -8.5267 | -48.8825 | 2025-08-24 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d308947d-a1a5-3772-9100-768da4138d13 | -11.5921 | -46.2363 | 2025-08-24 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| e800bc9b-de84-3ff7-bc48-e0bb54e280e2 | -14.1462 | -53.9802 | 2025-08-24 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 943fc621-12b9-3634-9921-2541479c5380 | -15.112 | -48.6459 | 2025-08-24 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 73aee13c-0b2c-3745-91cd-cfce725da12a | -10.6006 | -50.2058 | 2025-08-24 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b84eea07-95dd-3ce9-a1ea-0a85115559f3 | -9.1721 | -59.4823 | 2025-08-24 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 871fe00e-f06d-3996-9eb6-c80824de15a3 | -10.4777 | -46.8758 | 2025-08-24 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| bdc6dff5-2dac-32c6-89f2-689cae8b671a | -5.4364 | -60.1779 | 2025-08-24 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 60cc41ad-0ee7-3c94-af4a-c589041a3afd | -5.678 | -41.3987 | 2025-08-24 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| f6fcedff-96da-30cc-a4fe-69561a93d41a | -6.3431 | -44.4465 | 2025-08-24 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6f52375e-5c2a-347f-bf83-3a7557b931b5 | -11.5055 | -51.8705 | 2025-08-24 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 5ee33ecc-f616-30bb-ac0d-b9afd8c00d1d | -8.7375 | -45.4981 | 2025-08-24 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 5e9017ad-1a23-3d0b-b6e2-8d8b075d9780 | -11.7356 | -51.6984 | 2025-08-24 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 81b255d0-9638-3ae0-bbce-189432995997 | -7.9225 | -45.9193 | 2025-08-24 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 97005e1f-e966-3c7b-a44f-dac9ab60c193 | -15.1115 | -48.6682 | 2025-08-24 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 958a7020-0629-3b5f-876d-4f3f6c501f9d | -8.5272 | -48.8393 | 2025-08-24 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 415ecbe7-27a7-345e-aaa4-1e84abfaa673 | -8.0685 | -49.6524 | 2025-08-24 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| f10ce9e3-36f4-342c-a553-06ad6ce1eea2 | -7.9447 | -63.0528 | 2025-08-24 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| fa34369e-c6df-3434-afb4-0a9380063f58 | -7.9263 | -63.0535 | 2025-08-24 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fc8c0bd4-448f-3897-b071-8e9b41c4937d | -5.4365 | -60.1588 | 2025-08-24 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 87b06593-6c7d-36eb-8d27-0e21077b19a0 | -8.5458 | -48.8592 | 2025-08-24 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 74.2 |
| efb30dcd-fd4a-3552-8bc0-c829a1347e71 | -11.6112 | -46.2337 | 2025-08-24 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 3fe5b42d-c948-3f98-b2fb-3beb9e49ef1a | -7.6654 | -45.4018 | 2025-08-24 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| be9aa052-972b-3efa-9075-e34f1cce6f25 | -9.2083 | -59.6161 | 2025-08-24 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.2 |
| 4aed3e88-b91b-3ed0-978b-c4c710db8e3b | -10.4774 | -46.8982 | 2025-08-24 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 20d9e86b-71ee-31f1-a96a-4292dc487c46 | -11.9867 | -61.0214 | 2025-08-24 14:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| dc5ce1ff-ff79-312b-9e40-24ccb9877027 | -8.527 | -48.8609 | 2025-08-24 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 6702779a-bef4-3392-9c47-580fc9243a65 | -5.4182 | -60.1593 | 2025-08-24 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 780bf517-b411-39b6-a6d7-0272e778edd1 | -12.5418 | -45.6189 | 2025-08-24 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| bb2181cd-d5c6-3492-957f-c382df1d29b4 | -6.4547 | -44.529 | 2025-08-24 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1bf10141-5fe2-37b8-b25c-8cbe6dfffeb5 | -10.8075 | -46.4308 | 2025-08-24 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 8a3ebc16-2a78-3d29-a17c-68312dd7428d | -9.2269 | -59.615 | 2025-08-24 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| a236e49c-3952-31e3-ae88-1e21a4ba6fe2 | -8.4833 | -49.4032 | 2025-08-24 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| adc8f744-267f-3060-bb8e-c982da4ee2df | -10.9145 | -50.7698 | 2025-08-24 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 569a7fa0-09ed-3616-901c-6232a5714065 | -9.1898 | -59.5977 | 2025-08-24 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 3486d47b-4b16-3df0-8068-95a48de49f79 | -5.6628 | -45.1586 | 2025-08-24 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 271.4 |
| 172bb8fc-2b6f-3a1a-aa9b-1f0a0fa7c152 | -8.7769 | -49.9763 | 2025-08-24 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2f502b55-85e4-3d42-aa0e-43347dd1872b | -9.0232 | -65.6982 | 2025-08-24 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1449fa17-2be0-3dcc-91b4-45eca6d05471 | -8.7378 | -45.4753 | 2025-08-24 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 37962911-5009-3f7f-b85c-9a58dabb19b1 | -5.4181 | -60.1784 | 2025-08-24 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bb2c3696-e3f5-3ee2-9a08-09957bc5f1eb | -6.4357 | -44.5535 | 2025-08-24 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 435.0 |
| 6c4bd13f-2ab1-368b-9c8c-22ca48dd38db | -10.4584 | -46.9005 | 2025-08-24 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| f6b32965-8b51-3116-afcc-b310aed7f0fc | -6.6082 | -48.0412 | 2025-08-24 14:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8e963320-3713-3bbd-beee-7cd6fc76f7cf | -5.663 | -45.136 | 2025-08-24 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 336.2 |
| 014a4064-3151-37a9-9cc3-9af4143bf9d9 | -6.436 | -44.5306 | 2025-08-24 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 924a1788-aec6-3656-8f69-ca50276c47f3 | -6.3431 | -44.4465 | 2025-08-24 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 464180de-7e15-37f7-9aac-cffeb6a6794b | -5.4181 | -60.1784 | 2025-08-24 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 09bcdd22-eb41-3ebc-888b-1113c9827261 | -8.0652 | -44.9989 | 2025-08-24 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 77a0d016-c858-36ca-8463-b2414a845630 | -6.1187 | -44.3955 | 2025-08-24 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0f8a8be7-60b9-39a5-bf25-bd32d1edd8d6 | -6.6082 | -48.0412 | 2025-08-24 14:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 03b0f62d-4f29-36d8-b656-96ade5895268 | -5.6628 | -45.1586 | 2025-08-24 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 198da0cb-50bb-3569-90df-de83de5f5a30 | -11.5254 | -50.4683 | 2025-08-24 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 173.7 |
| a59cc5fa-f631-3a7d-baef-108f29d69ec6 | -10.5817 | -50.2078 | 2025-08-24 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |


[Clique aqui para ver as próximas entradas](README94.md)
