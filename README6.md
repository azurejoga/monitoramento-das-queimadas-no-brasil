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
| 1312fce9-3fcb-3958-a25f-d5894ab8a1a6 | -6.7127 | -58.528999 | 2025-08-27 00:22:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e44a209a-04b4-3ce5-84ad-965c786c0410 | -16.930401 | -49.425098 | 2025-08-27 00:22:00 | METOP-B | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 768aa346-2663-3aa2-bdb7-75da5c61fba4 | -13.3995 | -46.871799 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20132499-988a-382e-a184-8bac11c12a04 | -9.0734 | -49.555599 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1175002-4a4d-35db-96b9-69622e3cae1a | 0.7786 | -51.322701 | 2025-08-27 00:22:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6f557cc5-1deb-308d-8e38-cc74b64dbaf5 | -9.1076 | -49.57 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5d6fccc-1a5c-3ae1-b9a9-348b0ecd9183 | -9.0718 | -49.5485 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6862e404-bcd2-3336-b5b9-7af585f91344 | -15.6279 | -52.703201 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0dd8bd42-ad76-390c-a66b-fd92d26e7d4a | -12.752 | -48.1842 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db698e96-898b-3d8f-b2d6-2b1647b2eed8 | -11.0322 | -45.115101 | 2025-08-27 00:22:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 287ff896-8f81-3258-9dd6-53bfc7b5d9ea | -12.7828 | -48.138401 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a47668d9-fd71-32cb-be9d-7013ebd08fc7 | -15.6548 | -52.735001 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d78f1724-c93e-359d-9d6f-bfa8e5a21291 | -12.7274 | -48.166901 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea3e3d5e-97ce-3276-b35d-b9db2e170e9c | -10.3203 | -46.770302 | 2025-08-27 00:22:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f33d3f1-61d4-334c-905a-95c31ccec4f3 | -13.6189 | -48.187199 | 2025-08-27 00:22:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7e12f34-9d3f-3dc2-8294-8a72623d2896 | -9.0716 | -49.592999 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3011bc1d-162c-374e-bd7b-9e13d31c8c53 | -15.7863 | -43.329201 | 2025-08-27 00:22:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7d856dce-b7b1-3ef8-a032-8f341c47d8a2 | -13.4153 | -46.851002 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3387aeff-f1e8-308c-b7b5-7ff7c3ac90db | -16.5403 | -42.327999 | 2025-08-27 00:22:00 | METOP-B | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 682beb8e-40e5-36a5-ab21-8ddc1aadcae0 | -12.7618 | -48.1819 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c29af1e1-a46e-32e3-9730-c03c663d4997 | -7.2758 | -46.984299 | 2025-08-27 00:22:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3305842a-a590-3a22-8f69-067e5e98396a | -6.5751 | -47.3839 | 2025-08-27 00:22:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8ace7b5-840a-3068-a6e4-79f9c29328d2 | -9.1879 | -59.422699 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 824323aa-4c7f-3698-b6f2-291bd6297cb2 | -9.0946 | -49.558102 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7065f639-10aa-375d-87bb-a1294a25d3a5 | -20.985399 | -44.308998 | 2025-08-27 00:22:00 | METOP-B | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70edf13e-17ad-397f-8e06-47a651cf01bb | -7.2877 | -46.9911 | 2025-08-27 00:22:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b6db9fa-ba9f-3085-8c9d-44f7ada3a6a5 | -12.7405 | -48.179199 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78a3f6fd-5e16-3faf-8611-21f0c439b921 | -6.8285 | -58.935902 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2984a8c9-1d09-3c57-bf46-019c0f0a34ba | -13.4032 | -46.887798 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 062ab3ea-56d1-3e9b-acd2-4c0bc33d207d | -8.9018 | -60.7206 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9df4adba-d8b1-34cf-84eb-18ff0210dc95 | -7.5808 | -47.4972 | 2025-08-27 00:22:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b14e917-f562-3243-9013-44e15e4e091b | -10.4922 | -51.584999 | 2025-08-27 00:22:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c71b54b9-cd5d-393f-b73d-f1693342c215 | -7.7515 | -50.2728 | 2025-08-27 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e329bb62-9d84-3ea2-9590-1aa0865bfd11 | -6.2544 | -59.976002 | 2025-08-27 00:22:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 915d276a-181d-3708-9d05-8f49c4ac7ff3 | -6.6926 | -48.382999 | 2025-08-27 00:22:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7b936a44-67df-3d94-9533-773496f33d6b | -9.0782 | -49.576698 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53291eec-7429-31b7-8c64-62c1613aab0f | -11.5754 | -44.627399 | 2025-08-27 00:22:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df1fdcf7-b5d2-396f-9c8b-6a03ab4272f0 | -9.1526 | -40.570301 | 2025-08-27 00:22:00 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7d1be64c-949b-3f40-bd96-06c02adee50d | -3.735 | -48.922298 | 2025-08-27 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef2b486-5f6b-3622-a082-88cd3071550e | -13.069 | -46.297199 | 2025-08-27 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 074b689a-0f15-3c41-af47-3c0b466e5503 | -6.571 | -47.366199 | 2025-08-27 00:22:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 257c9929-c56d-346a-832f-97c86cfe442d | -12.9262 | -46.305 | 2025-08-27 00:22:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d9156c9-1ece-3911-863b-79efcd000ae0 | -9.1743 | -59.506401 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fff2af37-13f8-35b8-b354-1b0a901e63e5 | -7.5651 | -47.4739 | 2025-08-27 00:22:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7977983e-1fc5-3893-a982-9e632ba17c52 | -13.4014 | -46.879799 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c82e036f-b665-3897-83f4-6fbcad7f1f1c | -8.8096 | -52.069401 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3b08b0-9eae-34f0-b801-4e366a475bc0 | -5.7674 | -53.754501 | 2025-08-27 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b9af2a-2e5f-37c1-9c69-f762a5e37ae4 | -8.1335 | -55.352402 | 2025-08-27 00:22:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5f9bd84-dec7-351f-b6fe-3e50dfb92eed | -3.7368 | -48.930302 | 2025-08-27 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 249c059d-9170-3d4a-97f7-f3efc78e9640 | -9.4118 | -60.4991 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef64d5f-da1c-3b12-acee-18cc563fd70b | -5.1227 | -43.199001 | 2025-08-27 00:22:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5dec11b-a91d-3e13-8b6e-67d57a0d6297 | -9.5858 | -40.335999 | 2025-08-27 00:22:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dae10664-f512-361e-ae24-ddff1780f3d2 | -11.5781 | -44.638401 | 2025-08-27 00:22:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a508b05c-d109-3b33-8ab7-4b1fa16957ea | -12.8757 | -48.093399 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f63d960c-4e1f-371b-aee8-399e4f6f6cf7 | -9.1919 | -60.762501 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67c005da-bbf5-38fe-8c82-15c5865dda35 | -5.5507 | -44.257801 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbec5673-a937-3929-9f8e-8ee43c068a16 | -12.7845 | -48.145699 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 207f24d4-eedd-304f-8fc5-42527ec6cc6b | -12.7079 | -48.171501 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbc93363-12b8-35d7-acb3-c2411c582fb6 | -19.266399 | -44.3946 | 2025-08-27 00:22:00 | METOP-B | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 980dc20f-f9d8-3ec9-9796-787793bbf62a | -15.6316 | -52.7211 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a3ee0e1-f081-33d0-886a-c26a2778da41 | -6.7715 | -59.635899 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b58808d8-a19b-3d51-93c2-8828a2a91bd5 | -6.624 | -53.304001 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83e46e3f-6427-3cd9-94b6-ed7736eecafe | -12.7634 | -48.189201 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82373cba-a2aa-3d93-b7ee-6d6e3f18cc65 | -8.6937 | -47.182899 | 2025-08-27 00:22:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c536b81-8c8e-3960-bff4-d697417e883f | -21.588499 | -47.468899 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0607cb02-f146-3ae0-908e-c43052897d4b | -6.8413 | -58.9552 | 2025-08-27 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 30e87045-ff70-3249-aa06-5c35489236e1 | -13.1837 | -45.2865 | 2025-08-27 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 6579574a-1bdf-3799-9053-a3c21b66c487 | -10.2743 | -64.4907 | 2025-08-27 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 5f0e76d0-9865-36df-bc01-c979165553dd | -13.1648 | -45.2665 | 2025-08-27 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 9575061b-c156-3bf9-a603-f3b54a6335d0 | -9.8102 | -64.2454 | 2025-08-27 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 282d8212-411e-3367-bb6f-661b1910de57 | -9.4249 | -60.5316 | 2025-08-27 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 547f4f9e-5321-30ba-beed-36aaaf7f060a | -10.2742 | -64.5096 | 2025-08-27 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 8d78e8de-854f-3d39-a61e-73f911412818 | -9.181 | -60.8131 | 2025-08-27 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 0107ffba-4c2e-3b0c-9ccc-65d55456db6b | -6.8412 | -58.9746 | 2025-08-27 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 925b313b-2d45-3da2-b828-477c1f6acd68 | -9.4065 | -60.4941 | 2025-08-27 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 3aa472c8-b9f2-3f26-a1cd-465431f3b8d0 | -9.6104 | -40.342 | 2025-08-27 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 5e795b51-c3ec-3f46-875e-27287bb934d4 | -5.1181 | -43.1964 | 2025-08-27 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 1b759933-8ac9-34f9-9990-2c82022e3562 | -9.4064 | -60.5133 | 2025-08-27 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 282.1 |
| 4d9eeba7-43e7-3d3a-b747-b671702d4007 | -10.0977 | -62.9085 | 2025-08-27 00:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 778faf1c-6720-378e-8507-81808632fb7f | -9.7915 | -64.265 | 2025-08-27 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e2cb8af0-6135-33c5-bfcf-11ac3cded9b9 | -19.5767 | -47.5367 | 2025-08-27 00:30:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a707d164-a535-3247-b596-9e4bf3f7e3a2 | -9.5998 | -55.3699 | 2025-08-27 00:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 94a03035-6b1c-3c1f-bbbb-2cf6796bd01f | -21.5776 | -47.4852 | 2025-08-27 00:30:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 101.5 |
| fe98ac75-f6dd-3c18-8f76-e24d28ff6c5c | -8.9028 | -60.7498 | 2025-08-27 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4b07364d-e359-342a-bc7d-b729792a95aa | -9.1009 | -49.5621 | 2025-08-27 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| fb8396c1-6f84-3b3f-8304-2578fd3ca211 | -9.4062 | -60.5326 | 2025-08-27 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 191.9 |
| b1bf48b8-f245-3a52-85c3-53dfe063ac87 | -9.7916 | -64.2461 | 2025-08-27 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e7b2bfa0-1e43-3784-8adb-6f68fb5dd59e | -9.0821 | -49.5638 | 2025-08-27 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| a713fad4-370f-397e-b48a-b9915daa1846 | -5.118 | -43.2198 | 2025-08-27 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2f84785c-1fa2-3d55-b15d-16fb3bd61d73 | -8.9026 | -60.769 | 2025-08-27 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 90383c2b-ecf7-3ecb-b6de-9f1220dc0806 | -9.8101 | -64.2642 | 2025-08-27 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 32de013d-bbca-398b-a8a9-1ae82df2945e | -9.0771 | -66.0695 | 2025-08-27 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 4b92d2ec-e126-3fcb-8072-147ab99ef435 | -9.1529 | -59.5609 | 2025-08-27 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 09d65ab2-a37a-37f7-865a-eda6106b8363 | -9.0819 | -49.5853 | 2025-08-27 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 43b62555-a4df-3141-aa93-6f9b5e7ea71d | -5.5584 | -44.2539 | 2025-08-27 00:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 669c78c3-1716-3b67-87e7-4b1e7b4ed790 | -21.5769 | -47.5089 | 2025-08-27 00:30:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 81.9 |
| dcd476bf-2063-38f5-b317-a5cfe2ef6737 | -8.8842 | -60.7507 | 2025-08-27 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 5d9c5cba-6648-3d1a-947a-a12b9750c5e8 | -13.1644 | -45.2897 | 2025-08-27 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| e0b23506-f6ee-3b39-a34e-40fad7ff93dd | -6.8229 | -58.956 | 2025-08-27 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fbc2d8f3-0914-3d0f-84e0-72cd74223988 | -5.5582 | -44.2769 | 2025-08-27 00:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |


[Clique aqui para ver as próximas entradas](README7.md)
