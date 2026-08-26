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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f60bccd-4954-381c-b741-d323fc03e0a6 | -6.7833 | -59.4208 | 2026-08-26 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 778ba690-4baf-3a9e-82ed-0a99f2fc438c | -6.5138 | -55.2387 | 2026-08-26 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d5beef1d-109b-3e5f-ab29-eba983eedd91 | -10.9216 | -50.2571 | 2026-08-26 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 37a136ca-4dbe-3d36-868f-664d38f1c5e6 | -7.0058 | -59.2382 | 2026-08-26 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a2be0f34-9a93-3487-b2de-998c366ddac7 | -7.0242 | -59.2374 | 2026-08-26 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f064883d-16b4-3212-b2c1-d63df38d01a8 | -10.9405 | -50.255 | 2026-08-26 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 6e07a677-c1a6-3781-9480-41b21ce99d8a | -3.2178 | -61.2362 | 2026-08-26 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 153.0 |
| cf3c6c9b-fcc4-371d-a920-5f03180c05a7 | -6.1743 | -53.4834 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0dcea19e-e06b-35b2-9673-a479bc1766ca | -6.8246 | -58.6655 | 2026-08-26 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ce162888-8b71-3b74-9ad6-92fe94be0697 | -11.1939 | -53.9993 | 2026-08-26 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 082dd5d9-9b9d-3dec-ab9e-846368437422 | -13.6817 | -51.7872 | 2026-08-26 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 12183001-5dc6-3c71-8a7b-5cf709e64d1f | -13.6337 | -49.0051 | 2026-08-26 14:50:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 11f196ba-f293-31a3-bc5d-593f952ad86b | -6.1741 | -53.5037 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| a45d7209-3b2b-3b91-9118-a5bb8f4bb832 | -11.8356 | -47.6621 | 2026-08-26 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| a3b2b928-f993-3018-8431-9512cb262ae3 | -8.5361 | -55.3228 | 2026-08-26 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5ecccdaf-06d1-3d7a-ba85-1bc777f7ca5e | -9.6024 | -55.1078 | 2026-08-26 14:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 465.1 |
| 15aa729e-75a5-380f-a8db-36e7db101d17 | -8.616 | -54.7339 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 2392d80c-f768-3bd4-a276-75458f0c3b7c | -9.1899 | -49.9818 | 2026-08-26 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0453d160-e234-30b8-8e96-643c6244f7f5 | -12.1704 | -50.5861 | 2026-08-26 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1786fff7-e9f0-3885-a20b-8283c79a8207 | -9.7249 | -49.3296 | 2026-08-26 14:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d0ab4101-5ebb-3f06-b34a-c780bc3c2704 | -8.7584 | -49.9566 | 2026-08-26 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 218.8 |
| 83537097-de4c-3fa4-942b-1b27c23576d2 | -3.2179 | -61.2174 | 2026-08-26 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ca85471e-d2ca-3fb8-85c6-e56f396d9b61 | -8.9418 | -45.748 | 2026-08-26 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| e05ccc53-d634-3b42-b817-49dccb739aed | -4.8002 | -43.1709 | 2026-08-26 14:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 970f03e1-6e05-39e3-9e65-49eaf2e9a431 | -9.659 | -55.0632 | 2026-08-26 14:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 57195e63-5606-3470-add6-0ceb3f5b9ad6 | -3.1083 | -61.2191 | 2026-08-26 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 93d42d02-5c02-30d0-81c3-fc6aae61511b | -6.8062 | -58.6469 | 2026-08-26 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6344a00c-e253-3d63-986d-edd5c9676615 | -11.7973 | -47.6672 | 2026-08-26 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 9018a87b-fbca-3aeb-9493-a41d3ea41f06 | -10.95 | -49.5877 | 2026-08-26 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 18f44e67-bb9b-3644-9b29-a7cdae86e246 | -9.1713 | -49.9622 | 2026-08-26 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 0ac08e9d-6d93-3cf5-ad1b-ae97727cc0c3 | -10.5596 | -50.4449 | 2026-08-26 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 662a3b82-6dfe-30a6-85aa-b86d55dd22ce | -7.5015 | -44.9397 | 2026-08-26 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 195c6319-60f1-359a-a76f-ca6feb6ca909 | -8.7772 | -49.955 | 2026-08-26 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 42459225-ae74-3351-b191-4ae0b55f8db1 | -6.1656 | -57.7988 | 2026-08-26 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3168c4ed-99a4-329f-af43-63ea1f544e74 | -8.7582 | -49.978 | 2026-08-26 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 316.4 |
| 94dadfe2-4aa1-3a1f-a204-d44b898aa37e | -9.6022 | -55.128 | 2026-08-26 14:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 45f713a5-c9a9-32b9-b370-945906e1d76b | -6.6917 | -45.1932 | 2026-08-26 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 47ac3758-b753-3d3a-8a2a-542cf8db7e90 | -6.8018 | -59.4201 | 2026-08-26 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ac7f8134-1c16-3d46-b77b-c4b16e80063f | -8.6344 | -54.7528 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 75f87cc3-c602-3e31-93e2-84c7117fd40e | -12.1229 | -43.3738 | 2026-08-26 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 2ae88cb3-244a-3cd9-82d1-04410dde8060 | -5.9794 | -52.2252 | 2026-08-26 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4fcfbbd3-ff10-3d24-a526-142c1575937b | -5.6035 | -45.5465 | 2026-08-26 14:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 84090577-9d5d-31f0-b6e2-0d8d2d3f5c17 | -8.5177 | -55.3039 | 2026-08-26 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 05e10507-37c1-3938-af0c-3386ab89e11e | -7.1309 | -42.7945 | 2026-08-26 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 596d2c52-477f-37f9-a1f6-6aa9203bb8ff | -8.1482 | -47.5218 | 2026-08-26 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 26a69be2-178b-3e68-9674-70627a27a3fb | -9.4435 | -60.5307 | 2026-08-26 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c5d2ce70-1817-3a5c-933d-1c161c0582e6 | -7.0815 | -42.1824 | 2026-08-26 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 87ddd214-b807-3c80-b701-3c6e01b84b85 | -6.0353 | -58.0376 | 2026-08-26 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| a1ce142b-35f6-310c-935f-6104b004b0f2 | -7.6461 | -47.1258 | 2026-08-26 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 916.5 |
| 4671f63a-ce56-3c05-ba99-0c6a1f26074b | -8.6415 | -50.3495 | 2026-08-26 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| e96636db-b3ee-3ebe-b19e-1bf5ffb5748d | -10.4686 | -46.2254 | 2026-08-26 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 6d35e026-411b-34c8-8865-e48f3ee1dac3 | -6.1286 | -57.8198 | 2026-08-26 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ca1fb9af-7aaa-38ff-b313-bb0f44cf9e0b | -9.6588 | -55.0834 | 2026-08-26 14:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| b0d34b6c-20c4-3e8f-b5b4-a3ad4848f21c | -9.1896 | -50.0032 | 2026-08-26 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| d84a231a-80d2-305d-b545-71f1f5a0cba6 | -6.3322 | -54.7473 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| bd91ca4f-bf85-3ecd-a53d-86e5d93a1445 | -8.5363 | -55.3027 | 2026-08-26 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| aea750d5-eded-3ec1-990b-3065c3171f51 | -8.1484 | -47.4998 | 2026-08-26 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 561f1571-6023-3090-abd0-326f8712a284 | -8.7769 | -49.9763 | 2026-08-26 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 218.6 |
| c340e6ad-e346-3ff4-b88d-f387e73dbc0d | -8.1857 | -54.9435 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| fca060b6-f6c2-39a7-8c61-186bc2e5bf27 | -13.3788 | -48.2022 | 2026-08-26 14:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5b3247e7-6e3c-3c36-a61b-1897d55321e8 | -6.5139 | -55.2187 | 2026-08-26 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e2caf9b9-fbe0-3f2c-ba02-7d98f23bab2c | -11.6025 | -46.7542 | 2026-08-26 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 88a54325-4616-36e6-81e2-42c16e91c41f | -9.9708 | -53.9419 | 2026-08-26 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4483c86f-524a-350a-aea1-2ba30a1e81c9 | -6.235 | -55.4715 | 2026-08-26 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8e3b09a8-f285-311b-bc43-fb73ac0eac7e | -8.5175 | -55.324 | 2026-08-26 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 1646f0e5-c7cc-3944-a3c3-823a874a0a93 | -6.9693 | -42.098 | 2026-08-26 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 70ff5642-ad61-3662-a709-c8752eeaa5ea | -10.4689 | -46.2028 | 2026-08-26 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| a3b240df-008e-37de-abfe-5048cfded647 | -6.3323 | -54.7272 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b59b9302-96a5-367f-80e1-a9a284aa4f90 | -6.5829 | -58.9851 | 2026-08-26 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e4eef29c-1fe7-3af5-8d38-9b289a9a81da | -9.1711 | -49.9835 | 2026-08-26 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| db5ae313-ca07-329b-95ce-6399cf92d557 | -6.8247 | -58.6461 | 2026-08-26 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 606bb401-00e2-34f9-a3f0-6b0eb6bf2ddc | -6.6226 | -58.4995 | 2026-08-26 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 5325039e-15d6-36bd-8c93-e446a06a9632 | -12.5968 | -47.892 | 2026-08-26 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3821059c-02c5-3386-b54f-f540ea47550e | -9.7246 | -49.3512 | 2026-08-26 14:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 130f1893-ae3c-32bf-8026-0f69c24cdc6f | -12.1422 | -43.3707 | 2026-08-26 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 8654a35c-b43c-394f-bf61-bd6cc3521d81 | -12.6836 | -48.4116 | 2026-08-26 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d4095a02-59c6-3928-8fb5-35a90955eaab | -6.5261 | -44.8887 | 2026-08-26 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 2143d236-dea6-3487-948e-a1650484d9c6 | -9.6024 | -55.1078 | 2026-08-26 15:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 442.0 |
| 4bdfba17-d73c-3692-8d22-a9bbbb324e2c | -12.1704 | -50.5861 | 2026-08-26 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 2cb59314-83ef-34bb-8c24-48c0cd763c1d | -11.1939 | -53.9993 | 2026-08-26 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 5c211aa2-3b91-3dc9-90fb-235d81e22861 | -6.1741 | -53.5037 | 2026-08-26 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| de1e09d5-64d2-32e6-9e42-6c7d69748afa | -9.1713 | -49.9622 | 2026-08-26 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9092e034-9213-3fe0-b68f-c78ae45fa6c2 | -8.7582 | -49.978 | 2026-08-26 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 527.2 |
| caab7f0b-aa9e-3c8b-be70-ab1149b35684 | -6.7999 | -59.7473 | 2026-08-26 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a4842f6b-5425-3eef-ba4d-912038e38553 | -3.1267 | -61.1811 | 2026-08-26 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b35568da-6b1d-3c22-9c65-3e6b2d9d365a | -8.8189 | -49.5879 | 2026-08-26 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 900fb0fe-a3d0-39cf-86fa-4991ff096b4c | -7.1312 | -42.7708 | 2026-08-26 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| c2c5076a-2b63-3a6b-b906-f20007b19df9 | -9.6588 | -55.0834 | 2026-08-26 15:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 9b842330-e321-395a-8252-b717c5fcce9b | -6.5829 | -58.9851 | 2026-08-26 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| aa119b4d-5c7b-328d-bfb5-417bdd409125 | -13.2661 | -51.3925 | 2026-08-26 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1fd18b02-a9c8-3833-bd8e-46fa78e0d011 | -6.1544 | -53.6874 | 2026-08-26 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 91101286-88da-3d71-8d4a-e4afb602f168 | -6.7692 | -58.6679 | 2026-08-26 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 836aa6b4-71c1-3785-9525-563edc6ad3dd | -3.2178 | -61.2551 | 2026-08-26 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| cfab530e-1882-3d6b-bdd3-7d231166fc5a | -7.5015 | -44.9397 | 2026-08-26 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 2893d451-0aa2-3a5b-a4af-30e915845715 | -9.1711 | -49.9835 | 2026-08-26 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 32588d94-2adc-3dbd-b69a-bdeff97075d3 | -6.8246 | -58.6655 | 2026-08-26 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 06b61783-3517-3889-9fd0-383d353661b5 | -8.1484 | -47.4998 | 2026-08-26 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 5b9614f7-d89e-3fd2-b83e-a15f91ab0930 | -10.5596 | -50.4449 | 2026-08-26 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| be5c0287-9bcf-33b5-80c9-6e00538f68e5 | -8.1482 | -47.5218 | 2026-08-26 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 1d9297e9-7025-324c-9c19-7acdf92cb726 | -11.7354 | -54.5431 | 2026-08-26 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |


[Clique aqui para ver as próximas entradas](README87.md)
