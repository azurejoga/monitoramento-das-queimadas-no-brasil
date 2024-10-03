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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6a8eb52-13ad-376b-b0d8-e86112c9c3de | -4.931 | -43.788799 | 2024-10-03 01:05:58 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 842dabba-49fd-3ba4-b4a1-2908be1e82ac | -4.9161 | -43.770401 | 2024-10-03 01:05:58 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37d67a07-6369-30d3-ba7b-462c3ae01b9c | -4.9213 | -43.791199 | 2024-10-03 01:05:58 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 266c1168-2163-3296-878c-a45f07c4c7e8 | -3.9319 | -49.6852 | 2024-10-03 01:05:58 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e9f15a3-a8b1-3d9d-92a5-aff6e2dd2c46 | -3.9222 | -49.687401 | 2024-10-03 01:05:58 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c9adb1a-9d9d-3046-a480-66648018ca92 | -9.4574 | -40.3641 | 2024-10-03 01:05:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.7 |
| b721e39a-03d8-33c0-ade2-67c1eee1a63e | -9.1752 | -61.6749 | 2024-10-03 01:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| fce6c1fc-9f4d-3ac3-ac49-d532544d89f8 | -9.1754 | -61.6558 | 2024-10-03 01:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9d50af5c-4f8f-3dd6-8984-71d302ef4684 | -9.3839 | -61.0526 | 2024-10-03 01:06:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 9eff1931-35ee-3edd-b18e-00715607ea61 | -9.4025 | -61.0517 | 2024-10-03 01:06:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| c736b998-03e9-3c79-bfb9-fa75c2bb0b87 | -9.3833 | -68.3256 | 2024-10-03 01:06:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 257824cf-8232-3441-87de-33710d962eaa | -9.4244 | -67.2313 | 2024-10-03 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 00da0629-4368-3ed0-a2fd-f27670284a4a | -9.4368 | -64.5419 | 2024-10-03 01:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 4fdfbae6-e0e2-37fe-acfe-a84ebc3316b4 | -9.468 | -62.3857 | 2024-10-03 01:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 39f6a1c9-eae1-3f72-acb4-1980d57c86ab | -9.4865 | -62.4039 | 2024-10-03 01:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 083fe66b-c281-3925-bae9-cfe34cedc92f | -9.4866 | -62.3849 | 2024-10-03 01:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 88a80094-c11a-3f64-a4af-12c946a952ff | -9.4424 | -64.533401 | 2024-10-03 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86ff4c2e-b2b8-3556-985d-c361a23192c1 | -9.4263 | -64.5019 | 2024-10-03 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5153385-7134-3c59-9948-5b079c9f96e4 | -9.4328 | -64.535301 | 2024-10-03 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2861c3b5-4dbe-3d47-9755-cb0d8d3282ec | -9.4167 | -64.5037 | 2024-10-03 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb0a6dd-0a40-34bd-b797-1e9052d718c4 | -9.4232 | -64.537102 | 2024-10-03 01:06:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06c8958a-91dc-3c61-b29f-9e82c38b5fb0 | -4.0895 | -51.111198 | 2024-10-03 01:06:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ea9e5b-d50a-3e92-a446-5ed0c0d4dedf | -4.0913 | -51.118698 | 2024-10-03 01:06:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b16fea76-a8b6-3816-b49d-6776592c4885 | -9.4939 | -68.508 | 2024-10-03 01:06:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b714f12f-d526-33ba-b593-aab51c506458 | -9.494 | -68.4895 | 2024-10-03 01:06:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3d8a694b-e713-3f9e-ba10-e33fad68ece2 | -4.4797 | -42.875801 | 2024-10-03 01:06:01 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15c96f81-5d11-3d91-a6c4-06461c8d7178 | -3.923 | -50.661301 | 2024-10-03 01:06:01 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a476ab72-dbaf-33a4-a287-c729c11c68a4 | -9.7173 | -64.2302 | 2024-10-03 01:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 978f9a99-e5d8-3373-8236-9b6856498dc9 | -4.546 | -43.308399 | 2024-10-03 01:06:02 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43e9fcd3-03f9-3802-99c4-73029c188a3e | -4.5308 | -43.287998 | 2024-10-03 01:06:02 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b00465be-a150-3f69-808c-bb2632f27ecc | -4.5364 | -43.310799 | 2024-10-03 01:06:02 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3704b47e-f181-3add-a78a-d6a22ba545e7 | -4.542 | -43.333401 | 2024-10-03 01:06:02 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 148f24c5-f9e3-3b5f-9acc-eb3e08a4551b | -4.5267 | -43.313099 | 2024-10-03 01:06:02 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbd1aaa2-c0fa-3611-8520-7cf87759a8e3 | -5.3475 | -46.713501 | 2024-10-03 01:06:03 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b59766d1-d1c4-350a-9dcb-38e16d7c0a26 | -5.3506 | -46.726299 | 2024-10-03 01:06:03 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c30b428-c28c-3d2f-9086-ccd19497356b | -6.481 | -51.5042 | 2024-10-03 01:06:03 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cdd8016-d67d-3dc4-8836-6be873282e85 | -6.4563 | -51.442402 | 2024-10-03 01:06:03 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 593adfde-3a21-34df-8f54-038d8a9aa851 | -6.4579 | -51.449501 | 2024-10-03 01:06:03 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2ac550-530a-3a27-8103-942b126d9b83 | -6.4712 | -51.506401 | 2024-10-03 01:06:03 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ea201b-1399-3d25-9808-50f0ffb800cc | -3.944 | -51.239399 | 2024-10-03 01:06:03 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1368cda-b54c-3b7e-adef-197194e67df3 | -3.9457 | -51.246799 | 2024-10-03 01:06:03 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f05372b-b766-308b-bfe5-24ae1bfde5e9 | -10.1802 | -57.2848 | 2024-10-03 01:06:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 6f1e70f7-efea-35d9-9831-133b65a0936c | -10.1804 | -57.265 | 2024-10-03 01:06:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a7c15027-f13f-3a9a-98b1-694112864010 | -5.0902 | -46.117401 | 2024-10-03 01:06:04 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2aabb2f3-1b78-3f6e-bb09-ee1720dbc090 | -5.0804 | -46.119701 | 2024-10-03 01:06:05 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 521adc59-e126-3111-84be-b40d2432e60e | -6.597 | -52.590302 | 2024-10-03 01:06:05 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 451074f7-2f3f-3b72-b540-6aba9e3c7b3c | -10.6978 | -46.1514 | 2024-10-03 01:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ae218149-7195-318d-bfb1-bf6b4866d241 | -10.6505 | -53.6994 | 2024-10-03 01:06:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d1026f7b-e310-3175-a7e8-7ec26e641e62 | -10.9769 | -46.5443 | 2024-10-03 01:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 84b7ec1a-dba9-3637-9552-f044531629ef | -10.8942 | -63.8971 | 2024-10-03 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 39fbf4ec-be2c-3dbb-bde0-661047891f02 | -3.8595 | -52.2551 | 2024-10-03 01:06:08 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d85628c4-cdf0-3c98-b77d-223ba05d0b92 | -11.2563 | -46.9348 | 2024-10-03 01:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 85776b60-2cd6-3350-9294-bcb309562911 | -11.2567 | -46.9123 | 2024-10-03 01:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 186.3 |
| b6bb79fe-d5cb-3985-ac9d-a88287c4979b | -11.2758 | -46.9098 | 2024-10-03 01:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 35fde291-871b-30db-8573-effa608dbfda | -3.1378 | -49.418598 | 2024-10-03 01:06:09 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66295f7-e590-3995-bece-957f5fdc2552 | -3.1399 | -49.427898 | 2024-10-03 01:06:09 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2f096b-49b5-3136-8752-618a179c51c2 | -3.7729 | -52.193199 | 2024-10-03 01:06:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b34ab45e-e40e-33b1-95e7-8e45554254ed | -3.7565 | -52.256199 | 2024-10-03 01:06:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5679ee25-5a22-3275-8f11-18849a29664b | -3.7581 | -52.263199 | 2024-10-03 01:06:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45871792-c7d1-37e3-96c2-718bff123fe8 | -3.2553 | -50.141201 | 2024-10-03 01:06:10 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db448446-3a49-3968-9a9d-3ba794b8bd21 | -3.7467 | -52.2584 | 2024-10-03 01:06:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa727cb0-4d59-3cda-b0b6-1ad34ec2a20d | -3.7629 | -52.328499 | 2024-10-03 01:06:10 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e96e851d-de5f-3074-adf1-2031428df3f5 | -3.7645 | -52.335499 | 2024-10-03 01:06:10 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e76a3a26-3522-37cc-aa47-b2ea04fc4ecd | -3.7661 | -52.342499 | 2024-10-03 01:06:10 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 479edcb3-bf45-35d5-ae69-a18f7219e6d2 | -6.077 | -52.346001 | 2024-10-03 01:06:12 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09a081e-8380-3203-b245-3f23a17244ad | -2.9594 | -49.3605 | 2024-10-03 01:06:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e2ad55-331a-3146-8e15-316266cd8b68 | -2.9496 | -49.362701 | 2024-10-03 01:06:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08409964-4086-33b9-9713-3ee20ba1b3bc | -11.6742 | -65.0172 | 2024-10-03 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ace1bbcf-e2fc-3d1f-af6c-6f927f158b99 | -6.646 | -54.941898 | 2024-10-03 01:06:13 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0471fd5-b89f-312b-94ba-7ba62ca732db | -6.6477 | -54.949402 | 2024-10-03 01:06:13 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec487e82-e3c3-397a-b6a1-d46b86f1a55d | -6.6494 | -54.956902 | 2024-10-03 01:06:13 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21cab686-bb91-3b5c-8cf7-4ea0d0a7f01d | -6.2299 | -53.3293 | 2024-10-03 01:06:13 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a2f1e2-cd52-3f3a-8723-8d6a013df2db | -11.9876 | -57.1877 | 2024-10-03 01:06:14 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 5e3e6344-1410-3390-bfaf-c313df1edcd3 | -6.1879 | -53.280899 | 2024-10-03 01:06:14 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d22d3a-7cc6-3678-851d-0071feeff5cc | -6.1895 | -53.287701 | 2024-10-03 01:06:14 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4cb492-9dfc-3633-b466-1e9b9e31b246 | -6.1037 | -53.2276 | 2024-10-03 01:06:15 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 747ba42f-4b07-392c-bfac-4665576d0e56 | -6.1052 | -53.234402 | 2024-10-03 01:06:15 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74e9fb88-0b56-3ac4-aa45-9d64ef82ea0a | -12.4038 | -63.0009 | 2024-10-03 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| d86e7932-c13a-303f-937d-5559fa20b6c0 | -12.404 | -62.9817 | 2024-10-03 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 6c90049f-4bdd-3bb3-b36f-3f9cd7e90c96 | -2.5723 | -49.071201 | 2024-10-03 01:06:17 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c876af4-5c9b-3cf6-9a0a-c372d826ec73 | -12.6295 | -63.1225 | 2024-10-03 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e7125242-b6c5-36fb-9feb-2644a3184c66 | -12.6484 | -63.1214 | 2024-10-03 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.1 |
| a3aedcb8-0a0f-36c6-b001-59a714aa25be | -12.6486 | -63.1022 | 2024-10-03 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| aef6f86c-44cc-387d-98d0-a12678361f7f | -2.7934 | -50.282299 | 2024-10-03 01:06:18 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4d9db2f-9b11-36f6-9e7f-dee2e1918f43 | -2.7954 | -50.290699 | 2024-10-03 01:06:18 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8db7e434-6af7-361d-9d68-3c34a4735c77 | -12.8049 | -62.497 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 765739ae-e555-3fc9-bcdf-c77ccf521424 | -12.8802 | -62.5503 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 376e7d8d-d7a9-3fc3-ab42-a9b9d83a6fcc | -12.8803 | -62.531 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 025be7e0-ef95-3836-b73f-da7d2be5d9cb | -12.8808 | -62.4731 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5c9a1ef9-5d8a-39be-92bc-c7b74cdb1a08 | -12.881 | -62.4538 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 4c0acfcb-5603-3e8f-93a4-0d2fffe4ae92 | -12.8991 | -62.5491 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 9f1387ed-73e6-3015-805d-5fccef7c64d5 | -12.8993 | -62.5298 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c15258aa-38c6-35bc-9763-adfd2332e340 | -12.8996 | -62.4913 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 111.1 |
| df69913d-0beb-37a3-a899-e3f6447fe46c | -12.8998 | -62.472 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 14ade8a8-2cfe-3e12-986c-2cf86a37dba7 | -12.8999 | -62.4527 | 2024-10-03 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 522b5614-35d2-326c-96c4-4b38ca6185f0 | -3.6607 | -54.3088 | 2024-10-03 01:06:19 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87975582-1183-3dc1-b56c-64ac60e41480 | -3.6509 | -54.311001 | 2024-10-03 01:06:19 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4a81dc-9176-3715-bc08-f7f5d578a751 | -3.6635 | -54.366501 | 2024-10-03 01:06:19 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0e3fb6-9cd0-3ffd-b436-1ccffffc597b | -3.6651 | -54.373402 | 2024-10-03 01:06:19 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9f93db-5e0d-36e5-b09b-9188657b0433 | -12.9166 | -62.7214 | 2024-10-03 01:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |


[Clique aqui para ver as próximas entradas](README33.md)
