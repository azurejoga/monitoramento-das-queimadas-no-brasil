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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0932e5e6-b3eb-31a5-a903-536dec110cb7 | -9.7246 | -49.3512 | 2026-08-26 15:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| e261876f-0149-3858-ae5d-928e0fe48b55 | -9.1708 | -50.0049 | 2026-08-26 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| e65f2c4f-4cb0-32b5-8097-6a77ad7267c6 | -9.3873 | -60.5721 | 2026-08-26 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| f8f75b08-622e-3825-a443-0dcade2f1b0b | -6.5138 | -55.2387 | 2026-08-26 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 477f2aeb-0b87-315e-bf6b-b0f770a04ef1 | -6.5261 | -44.8887 | 2026-08-26 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| afc5fdad-2c39-3822-834b-55bbc8f74325 | -7.6461 | -47.1258 | 2026-08-26 15:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 685.6 |
| a1b2d2cb-658a-30f2-9155-f41c1fe836b8 | -6.6917 | -45.1932 | 2026-08-26 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 1b3736af-301b-32f9-a4df-de6e86aa1e83 | -8.8187 | -49.6093 | 2026-08-26 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 259.2 |
| 107669ee-4646-34e2-86d6-7a4ddcec80c3 | -6.7833 | -59.4208 | 2026-08-26 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| e0184b49-ea36-3052-92e1-9fbe15de49a5 | -13.3226 | -51.4493 | 2026-08-26 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a8b71299-482c-346f-a92c-df049643e4c6 | -13.5848 | -51.8419 | 2026-08-26 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8aa036ee-6588-3f24-b0dd-2958da078343 | -9.1896 | -50.0032 | 2026-08-26 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 0e593f12-5a89-339c-a579-d8d432a5a041 | -6.695 | -58.7291 | 2026-08-26 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4d777b59-c88a-3a6c-9484-fc957e3c0fa4 | -8.6415 | -50.3495 | 2026-08-26 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b6654cff-cf5c-3ff4-904c-223a26f5e873 | -7.385 | -55.1523 | 2026-08-26 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| dc133fb1-53a4-3ff1-a7bc-f1f27f99f7aa | -8.7772 | -49.955 | 2026-08-26 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 8b93d328-8ded-3a7f-830b-7aae64cbcbc8 | -9.7249 | -49.3296 | 2026-08-26 15:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| e30fe6a3-1018-3e9f-93bb-3be081ffd171 | -3.1083 | -61.2191 | 2026-08-26 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9583e0a9-6c0b-3200-afcb-46a57d0f6122 | -11.7736 | -54.5191 | 2026-08-26 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 408.9 |
| b9839dca-813c-3a1d-b2fc-666c7ef50c67 | -12.1701 | -50.6075 | 2026-08-26 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| c3da5363-1724-36b3-9720-1bb0678e1149 | -13.3038 | -51.4304 | 2026-08-26 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0bb5b3e5-805c-3fff-a570-fb92f1db897a | -4.8002 | -43.1709 | 2026-08-26 15:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 7f479293-1acc-30c1-a459-e07ca5f688c6 | -14.374 | -51.8252 | 2026-08-26 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 273.0 |
| e47b2f7c-8674-3271-a446-abecb6d4865d | -8.1294 | -47.5235 | 2026-08-26 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 0d36869d-1384-3c6a-8851-0bc149926fbd | -11.7357 | -54.5227 | 2026-08-26 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 139.5 |
| cb973d99-5a60-37f1-8219-837107f5d20b | -9.406 | -60.5711 | 2026-08-26 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f1882f2c-5c9e-3f6e-9159-edda55cf913d | -3.2178 | -61.2362 | 2026-08-26 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 196.1 |
| a44cb57a-bb9f-3ced-b612-bc60f8d87348 | -11.7544 | -54.5414 | 2026-08-26 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 436.7 |
| 73c59692-6daa-348e-9186-5aed296f9568 | -11.8165 | -47.6647 | 2026-08-26 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 211.8 |
| bfd6cec6-d8c9-3a7a-8506-ff38aa36b62f | -13.6337 | -49.0051 | 2026-08-26 15:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 7707bd77-514a-37e0-a7b4-4e1dcffd66e8 | -9.6022 | -55.128 | 2026-08-26 15:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 8f1c9e1b-a9aa-3a2d-82d2-7c8e3e89b80f | -8.1669 | -54.9648 | 2026-08-26 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ad8aa3d7-d543-3595-a20c-3d2a09081592 | -6.7691 | -58.6873 | 2026-08-26 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| dd95daed-14c9-321d-b0e0-32dfaec5e17f | -8.5177 | -55.3039 | 2026-08-26 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 269.2 |
| fdb89f57-87bb-3eae-8045-284df8a1adbd | -11.7733 | -54.5396 | 2026-08-26 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 336.0 |
| b8ad4752-5ebd-3c70-8b7e-f329680ca24a | -8.167 | -47.5201 | 2026-08-26 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| f1d989dd-b142-3d78-9549-11cf69dc3c0f | -12.6836 | -48.4116 | 2026-08-26 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 20379048-151b-3c16-bb7e-d29b9c435e2f | -6.8062 | -58.6469 | 2026-08-26 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b4d89832-570b-3b5d-8701-ede8a79d6c66 | -9.9708 | -53.9419 | 2026-08-26 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 80cba143-fd0f-39e5-99d2-1fd5e9132980 | -11.1561 | -54.0028 | 2026-08-26 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7d30f3cc-d857-3182-a473-93b58e010bbe | -7.5256 | -44.4795 | 2026-08-26 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 90541331-efa7-371b-a17e-de274519abd6 | -6.1656 | -57.7988 | 2026-08-26 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 14e5d329-7904-3fc1-9938-4f32e234eea5 | -13.6817 | -51.7872 | 2026-08-26 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 589670c0-0b20-32a4-9c28-eabb326c7047 | -6.0353 | -58.0376 | 2026-08-26 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 006bbc09-3951-3dfc-8cd1-7b887bcc3680 | -7.0242 | -59.2374 | 2026-08-26 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e87a3c31-fd1e-318d-bc16-a0dae6232bb0 | -11.6025 | -46.7542 | 2026-08-26 15:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 34b9d105-538d-3b8e-adf8-b73dd583e8e8 | -6.3504 | -54.7865 | 2026-08-26 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 68e81ab1-60c2-3cdb-8165-791c9bee8925 | -8.7769 | -49.9763 | 2026-08-26 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 420.3 |
| 98fff0f6-fdc6-31b5-a6a3-3af70fd69684 | -6.8247 | -58.6461 | 2026-08-26 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| a5363489-4272-34d7-948d-c2044d4b31ce | -8.7584 | -49.9566 | 2026-08-26 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 208.2 |
| 0afa25c9-4c95-3c78-a653-1f9f429fc40c | -11.175 | -54.001 | 2026-08-26 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 180329d2-7a49-3d5d-84c6-8cc8222195c5 | -8.5365 | -55.2826 | 2026-08-26 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d32a0a40-a6ac-3a6f-88ca-1196fe063267 | -7.0058 | -59.2382 | 2026-08-26 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ed2bbcf9-34bc-3d59-a211-55a6f8b3d1fc | -6.8019 | -59.4008 | 2026-08-26 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4c840793-3fa7-359c-b4ee-31d801678ab8 | -9.1096 | -60.3937 | 2026-08-26 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9dbc00d8-2a16-3027-a92c-98a9c140df09 | -13.6044 | -51.8182 | 2026-08-26 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 32a84a57-15b2-3a73-9c23-370e9ec7a31f | -11.7546 | -54.5209 | 2026-08-26 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 440.7 |
| 5a166b3b-c26c-3d0e-aabf-c689591f3dc9 | -10.4689 | -46.2028 | 2026-08-26 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| b6edb530-726b-3939-9765-5a2f52188962 | -9.1899 | -49.9818 | 2026-08-26 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 0e66c3df-4bad-3e07-b077-3015116dee84 | -10.4686 | -46.2254 | 2026-08-26 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| cd6eb74d-469a-3e73-bf61-201fbca0b5a4 | -6.6226 | -58.4995 | 2026-08-26 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 870c547b-5a85-342d-b9dd-a2635bf81455 | -14.3737 | -51.8466 | 2026-08-26 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 1064e852-c9c7-34ab-b81b-84eae88aa60f | -6.3323 | -54.7272 | 2026-08-26 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| af504abc-41dd-3e9e-8e80-402fb143ee2d | -5.9196 | -43.6497 | 2026-08-26 15:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 383d6dcf-e1a8-31b0-a607-f4eb13d159a1 | -7.6649 | -47.1242 | 2026-08-26 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 395.4 |
| 7328e511-67c7-3bc1-af9f-a46224c79f4b | -7.1309 | -42.7945 | 2026-08-26 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 3f135097-37ba-3410-86db-214b0e96ec9f | -3.2179 | -61.2174 | 2026-08-26 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 49cb52e9-b495-3ff9-a511-b981d2b55646 | -6.8018 | -59.4201 | 2026-08-26 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 2c616b1b-b5e1-37a2-b9e9-320cb803f6b9 | -11.3702 | -50.6993 | 2026-08-26 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 235f4155-5971-3520-ad35-1bed6010bca6 | -12.6836 | -48.4116 | 2026-08-26 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 5da22466-1030-3688-892c-7081c3ad0daa | -10.4689 | -46.2028 | 2026-08-26 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 7441005d-395f-30fa-bf07-405e0c0265d0 | -15.7878 | -56.452 | 2026-08-26 15:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 97fc8bc8-1193-363c-9b12-c44c4f11d96f | -3.2178 | -61.2362 | 2026-08-26 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 2c275347-a454-3bab-bb43-72183fab6331 | -5.8469 | -39.5443 | 2026-08-26 15:10:00 | GOES-19 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 81.7 |
| e2c69bef-3651-3bb1-8c41-0677db060367 | -8.6415 | -50.3495 | 2026-08-26 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 3a1bec2e-ba63-33ee-b152-8b2687d355e5 | -8.1667 | -54.985 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 61ea7cc9-1304-3730-970f-0b88d45f9aa5 | -11.7354 | -54.5431 | 2026-08-26 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 6389fce9-272c-3e55-ac20-36fdd85c9943 | -8.8187 | -49.6093 | 2026-08-26 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 255.9 |
| af6f4bed-8112-3803-b500-8c8945ee468b | -6.7692 | -58.6679 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| dd0bc539-b128-35bb-aa4a-8faf0987391d | -6.8247 | -58.6461 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.8 |
| c67792b0-9bbb-37f3-922d-15616355d60a | -11.3702 | -50.6993 | 2026-08-26 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 3841d133-8c75-307e-9292-3c921127ef40 | -7.1309 | -42.7945 | 2026-08-26 15:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 3ec011e1-0a93-3987-ab0d-f0f5848d3e17 | -8.1484 | -47.4998 | 2026-08-26 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3b489a4b-4759-34bc-b595-625f6bde9baa | -3.1083 | -61.238 | 2026-08-26 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1107fbe4-c8d6-3291-bffe-fb60d7409377 | -12.6452 | -48.4168 | 2026-08-26 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| dd821397-1fea-3525-a80b-b268031e23e9 | -9.9708 | -53.9419 | 2026-08-26 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| d109993a-d04e-3c0e-8813-4fc4f45691b6 | -6.8246 | -58.6655 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| b732fd38-4475-358f-824c-4ef7b3f7f080 | -8.7772 | -49.955 | 2026-08-26 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| e3d389c5-c471-36e8-b429-ed8cc45a676f | -6.7661 | -45.2551 | 2026-08-26 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 86e37032-0945-3ffa-92fc-5c7059dc8f67 | -6.7105 | -45.1917 | 2026-08-26 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 57004659-e7ad-3a96-b730-dbee813009ab | -6.1743 | -53.4834 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 20284793-dd66-38f5-8a77-21682c2025fa | -8.5365 | -55.2826 | 2026-08-26 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| bdfeec1e-97fa-3769-b96e-c83ccb8ffd5e | -8.6344 | -54.7528 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 1b576b9b-ef0b-32b1-b9a8-a0ccbf20bc81 | -6.8061 | -58.6663 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| df4738f1-f8a6-3359-848a-e2baa32093b9 | -7.4769 | -55.2672 | 2026-08-26 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 03ed1e7d-9323-35e8-857f-18b7745817df | -7.6461 | -47.1258 | 2026-08-26 15:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 635.8 |
| b69e335e-b5fc-3d4c-97a9-8c1929bf809c | -9.1899 | -49.9818 | 2026-08-26 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 92b367ee-7127-3606-b850-155f1d753fc4 | -10.5596 | -50.4449 | 2026-08-26 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| bf2acb26-08ed-3369-aae4-1c779b98a503 | -11.8356 | -47.6621 | 2026-08-26 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a936e177-bbf6-3c3a-9399-44456fa0b9f5 | -8.5973 | -54.7352 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |


[Clique aqui para ver as próximas entradas](README88.md)
