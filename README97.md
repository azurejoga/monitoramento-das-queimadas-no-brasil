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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 876c18d4-1f3b-3de2-a155-d5753da3da3e | -14.40871 | -51.69773 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83d2ca3f-8d52-39d8-a477-63a70074dab8 | -9.61635 | -55.37597 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c4889a7-b115-3756-91ca-39a8cd448bac | -10.12703 | -47.44266 | 2025-09-03 05:14:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 031bbcc9-0ca3-30f3-9c9d-fd94cebf6e29 | -15.0198 | -50.06865 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4fd68d3-8f46-3683-b2d4-06256bab1319 | -11.59075 | -46.76698 | 2025-09-03 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b963f27e-ead3-37de-9794-f4fa0ccd4118 | -13.8186 | -56.60726 | 2025-09-03 05:14:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b76f58a-1de7-3121-b011-8109e6e61815 | -13.48917 | -46.82365 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c068d8c-e0f1-3099-b18e-9f801dc29a93 | -14.99568 | -50.06407 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc4b772a-13ad-3f98-93a5-a38741600f2d | -11.42013 | -55.17894 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 792c8b9b-07b9-3e92-8ef8-4f46ae4ee4ca | -9.63583 | -47.03562 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef071653-03ae-3e93-b36e-8651576704d9 | -8.81424 | -47.80388 | 2025-09-03 05:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38167e11-337f-3547-9580-3c5622322e3a | -9.63419 | -47.85973 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f68973a-3322-386f-b2d8-301b133ac96f | -12.63282 | -56.99714 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 801b7a11-b8bb-3314-bff3-5bdc5733dede | -11.60739 | -52.11329 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e068892b-5ca2-3d6d-a66f-7f65397023ca | -12.89174 | -48.04721 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49bb2086-e2c1-3a25-8cfe-85759750eaf7 | -11.42251 | -55.18795 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87640af-b155-33da-bfd5-be6d4b7255fe | -10.14932 | -46.27383 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba3559f-dc16-30aa-8215-befb7222db5e | -14.40367 | -51.66088 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7d23b59-4112-3937-b052-479ef373df14 | -14.57174 | -54.54148 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cc59db9-a870-3786-aa5e-ec15f62bde88 | -8.36386 | -52.54047 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e8b586c-b413-3119-a848-d928d3cad3c0 | -7.08817 | -63.07014 | 2025-09-03 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 127b1cb9-974e-3fe4-bfad-23e8cc91c83a | -14.76958 | -48.14413 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a5cfd3c-a114-3b5a-8cfe-a8470be5b123 | -12.60776 | -57.0009 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7de779ce-d997-371a-9595-1fd5a5d4615e | -10.4633 | -53.6264 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 397c1263-a6fd-3ec6-9c86-502ae83c51b7 | -14.59435 | -54.58084 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00e8ad61-a10c-3deb-ad3f-7f3dcdbf2064 | -14.51715 | -53.15224 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cca0a792-73ec-35f0-87d6-dfd5f5462b19 | -7.96663 | -55.29055 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5e99d73-1866-3f1c-bb58-3d67caa3d593 | -14.97223 | -50.20218 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 407f49fe-57a9-3ea1-bea2-8ac6ba18f9b4 | -9.13196 | -49.65311 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e233727-db7c-3ae1-bb69-6c323658dbea | -7.34627 | -57.62585 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee28c326-df45-353b-adf1-71dd4d926d66 | -10.91471 | -50.83804 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b3ff4c2-d961-3aa5-9315-9786f392dd8b | -11.5906 | -52.13745 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| fbc8c55c-9bb9-382d-827d-23d65c8dad42 | -9.33005 | -55.22486 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18d50447-6071-3a64-b94b-662ede955f7e | -12.8841 | -48.03764 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e0711af-6317-3c43-90bd-4cfc7cbd61ed | -15.00997 | -50.06025 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2a3d768-2d26-311a-9575-952b1046122b | -13.77383 | -47.45386 | 2025-09-03 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa22b8f7-5f18-32fc-8745-7eb39d66becc | -11.61383 | -52.13191 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53dfa6b3-ed59-3a26-8062-9ffac8bfe9e9 | -11.65794 | -57.35588 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d1e194a-9575-3f29-b22c-8aef9c26b2fc | -11.11965 | -44.64543 | 2025-09-03 05:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 931e4fc3-f86e-3641-9cd8-633a44e3c592 | -11.58296 | -52.12755 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d86465f-8992-3170-a5ae-b5a4cdb2342d | -13.31848 | -51.76698 | 2025-09-03 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44a96d66-6f7b-3051-a75b-83490b0c75c4 | -12.94242 | -56.95557 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fe886d1f-90cb-36b3-a26f-df979b1ac512 | -9.39846 | -48.05016 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 249a22d3-a723-3517-b9a2-ceb699cf82e2 | -10.09014 | -54.76292 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a3cbf73-8444-3eb2-923e-e392cccd4840 | -8.86914 | -52.03032 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9e682e3-191b-333b-a1c0-147fcd945d82 | -13.01307 | -48.09777 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b38e26e-f1f7-359e-a09e-6394a6c7b64b | -8.06148 | -52.34784 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb098a19-675d-3364-a50b-4b5d16baab2e | -9.63402 | -46.11603 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c364063a-a4f3-3947-948d-8f40af9fc256 | -12.94015 | -56.97063 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a0ad1b7-39b3-387f-8488-57d31808843c | -9.96446 | -51.62851 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec21a1c0-0b61-3d4e-b54b-fd40e3c7802d | -12.94185 | -56.95934 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1ae6dd09-6162-3674-9043-85711dafb239 | -11.66578 | -57.34972 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bb04a11-eac5-31f1-889e-a0dd03931af0 | -9.05393 | -54.95375 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b74a5313-46b5-3a2a-ba69-44cf191ffd50 | -8.08834 | -47.59386 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26b08bd8-af59-3939-9739-bb47f15e0af0 | -9.63254 | -47.0624 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b5c27e4-aa59-34a4-aa67-7da7b9eecf7c | -14.57598 | -53.0041 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7883d01f-7426-3f4f-b299-1fdbcf033512 | -12.94299 | -56.95178 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 54c59cfb-4e50-3bc6-8902-661ff035a647 | -9.60686 | -55.39099 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92370dfd-67c9-3b8e-a5b5-f4679c167d3e | -12.94128 | -56.96311 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0284b37-cb99-3132-8c65-ab561dd6aa81 | -11.21219 | -55.07699 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be9c9019-b24f-31dd-8e07-5144843f4594 | -14.77435 | -47.5181 | 2025-09-03 05:14:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| da627d5b-5a09-3f12-a663-342d7ed7fa61 | -10.12756 | -47.43831 | 2025-09-03 05:14:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14c3f22a-5d9f-382d-b75c-66d102d987d1 | -9.63861 | -47.85963 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de1099b0-8319-3208-a333-9b43ca041e56 | -11.61205 | -52.14486 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a2f653d8-0f23-3ec0-a2d9-ff6939e59c98 | -9.64118 | -47.03482 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0d4acc5-c306-3369-88ba-9d0c5805f091 | -12.9396 | -56.99752 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b0cf47f-2513-3bec-8d14-cc7271965a52 | -9.62897 | -47.85482 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d17006c6-3b42-3bba-9a89-26baa62bfc15 | -7.76539 | -61.19918 | 2025-09-03 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18fdc43-8263-3955-b4a4-3f3b965379e0 | -12.96364 | -48.07522 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff721eeb-6a9c-37f9-af29-feac8e71d26e | -6.79854 | -59.87661 | 2025-09-03 05:14:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10b25eb1-538a-3c53-bb4f-161e0faa33be | -9.42739 | -48.35549 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38515e09-3031-3a33-80ee-39578e029211 | -12.92247 | -56.99483 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d127e870-c35b-3483-b0c5-d092ea7748b8 | -7.76 | -61.20057 | 2025-09-03 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5aa4e1b7-c9bc-387d-9a70-a76aa8fe574f | -12.99892 | -48.11703 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6b4deab-4d18-3f73-9994-8998e950aa0a | -12.93218 | -57.00021 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86c22a7c-93c3-38af-8a2b-5015bc55765f | -10.14356 | -46.2678 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5a51df2-e946-3fe4-98e3-a4b0acdfd2f9 | -12.97827 | -54.76483 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87c5ef9c-1cc2-3168-aa79-01a23c268d61 | -13.00068 | -48.11572 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78b46e6c-65af-38d4-aed7-ef49a8a349c5 | -14.77972 | -48.1495 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfa52979-e9c3-33d2-989a-c3da9e5c5e79 | -12.89296 | -48.08677 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ddcde47-3a54-3710-a96b-cae9e42e7312 | -13.90268 | -48.12251 | 2025-09-03 05:14:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 274c5919-5ada-3114-8dfa-635a76ed9593 | -11.59796 | -52.11644 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be448ba2-728a-3b61-8a2e-df76c39b0834 | -10.48571 | -50.35512 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a915163a-3239-3d73-aa79-6dde2763b745 | -12.63909 | -57.00196 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76d01d8f-1ee0-3d0f-a766-e5efd8b302c8 | -12.97171 | -48.1081 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85376956-d58f-327c-8886-283311a6e78c | -12.59824 | -53.99017 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64f86f4e-220f-3b2b-afc5-8312325c9bcf | -13.00757 | -48.10822 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17b00e54-f98a-336f-836e-c7b8cacdcb21 | -12.91438 | -56.93174 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2a23678-cad9-3647-927f-2496c274ea04 | -11.80244 | -48.35726 | 2025-09-03 05:14:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18fbf5a4-c23a-3c6d-9460-c1bc363a676c | -11.64042 | -52.06237 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af0737a9-db1a-3671-9e47-658177047bdb | -10.05848 | -48.08996 | 2025-09-03 05:14:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3440905-5129-398c-ad0a-ed8a49ec2bce | -12.89412 | -48.05494 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fb49a21-7bc3-3ba4-b9f0-f7cf38600788 | -15.00137 | -50.06172 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9eabcc4-85f8-373e-8ba8-5336be1374f9 | -12.98138 | -54.77013 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1652518d-3ce8-32bf-adb1-41c1bb9a2599 | -8.43484 | -45.08068 | 2025-09-03 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ebe8a3a-137b-3f75-85cb-cf0a18533098 | -10.13844 | -46.25624 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecab7a59-f2f7-3d3e-8a62-2614fbe2408c | -7.7144 | -50.25281 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5475109b-c65b-32d6-85fd-81fd91539e13 | -10.0069 | -46.89899 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5905855b-5bec-3190-9e94-a6945eb4a11a | -6.43861 | -58.14006 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a5901e2-aac5-32fc-8756-c7630de50378 | -10.14243 | -46.26734 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README98.md)
