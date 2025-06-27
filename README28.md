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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3ce5f2e-7909-3425-b021-2b81d27345ac | -10.45819 | -58.68228 | 2025-06-27 05:10:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ec0b5f5f-2717-390e-8ab0-50ff6efbc4d5 | -13.15943 | -45.23192 | 2025-06-27 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e1375aa-f5cb-349b-ac61-5c2c7e483055 | -10.71367 | -59.12778 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e042679-8a31-3ff9-9bb8-6d84531afcea | -10.27373 | -47.60563 | 2025-06-27 05:10:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28a35fec-782b-3ae2-8889-d3e18aac6444 | -9.17078 | -61.40596 | 2025-06-27 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f50fc05-e0c1-3db1-ab9f-304f0412cd12 | -11.60287 | -55.5477 | 2025-06-27 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19e9398e-27ec-310b-bc1f-0f0211e9ecbe | -11.57672 | -52.10618 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c21467bf-77ae-3f93-816c-1f9c22540e5d | -12.05055 | -48.07375 | 2025-06-27 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 621d6622-b9af-3c02-a360-6cc058495968 | -11.44054 | -54.47296 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e210be0-0619-354c-97f7-72ad4cd7809b | -12.13527 | -54.6651 | 2025-06-27 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c6604c0-82b6-37fb-ae34-78e45104a113 | -11.05824 | -55.37029 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d721a352-56c8-35e8-be31-82d7cc5cb26b | -10.83411 | -53.74663 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19248e40-58ad-30f8-b5b8-b0e87ebaa9a0 | -12.03428 | -48.7502 | 2025-06-27 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cc3f6cd-cf1a-3b30-bda2-3aacf520c8d0 | -6.17404 | -48.08502 | 2025-06-27 05:10:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5a78053b-6542-3279-bd01-2baf3031ea11 | -11.61476 | -58.28414 | 2025-06-27 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ed3bc26-365c-3611-a69d-2c708fd62578 | -11.50513 | -61.82585 | 2025-06-27 05:10:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6080a76-5480-3470-a08f-abad9d442ec9 | -7.53772 | -45.83097 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f17c007-82e4-392d-98e7-7ceecf4163f0 | -9.51332 | -56.10635 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b2633f4-cd82-315b-b5af-2637b9fa449b | -11.57998 | -52.11559 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 5b8b647e-7ff2-3800-ae48-3598d195e348 | -7.54972 | -45.83797 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0732ec8e-fd96-3e59-bc50-277f9e9a81db | -7.0179 | -49.17947 | 2025-06-27 05:10:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b5f9a53-1d32-35bb-b272-7ada9dd8ab35 | -10.8223 | -53.74501 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42f9d27f-9f6f-3be1-819e-b570f7ffea14 | -8.61778 | -51.583 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 948c3b82-7c7f-3341-87fd-86dc9210390b | -9.3436 | -58.85415 | 2025-06-27 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e528231d-7d58-3b95-a6de-8cb33a95e5ac | -10.52281 | -53.628 | 2025-06-27 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eaef854-f88d-3236-ba98-d6977cccc739 | -11.58056 | -52.11122 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c9ee90e1-2b52-3f40-917e-f76cc92d7285 | -11.67056 | -46.7362 | 2025-06-27 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cffad3be-f1e9-3f27-aa19-6606c37b5096 | -12.05072 | -48.08001 | 2025-06-27 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11f009d3-77f5-316d-8892-a76f41d148ad | -10.85746 | -54.03633 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfb28dc1-2ac6-302d-a1a4-781b7f23d28a | -7.54339 | -45.83694 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 54609566-6869-3fd2-9c17-5278e4d2ad7c | -10.87794 | -56.45587 | 2025-06-27 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a891d3c9-51ef-3632-adab-d55402dda260 | -7.01884 | -49.18316 | 2025-06-27 05:10:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b4187b-b84b-342f-b9dc-daa08c552331 | -8.67273 | -49.95802 | 2025-06-27 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63927cee-b7bb-311b-8bda-a7f67b6cbd6b | -11.18119 | -55.92796 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a255540a-a797-3813-b5a6-07e61becca3f | -8.54374 | -55.03426 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34d15bcf-89b6-3869-a850-35516710b3ab | -11.67385 | -46.73411 | 2025-06-27 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca13b4a4-c014-39d4-8fe5-07e65494f70c | -11.57498 | -52.11929 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ab9c1615-c447-3e69-a84d-3742be2e58c1 | -8.37466 | -51.07045 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b842173-2c5c-37ab-ac1f-d8e151ee8e78 | -11.60569 | -55.54282 | 2025-06-27 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff9eda67-a92f-33e0-bfdf-5f15e573a87e | -9.49787 | -56.0924 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fc1f5bb-0d6e-37c1-9f57-832a609195de | -10.85493 | -54.04373 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84a8c3b3-3816-35a4-85d6-a35e8dec4120 | -12.02783 | -57.08718 | 2025-06-27 05:10:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cc5c26b-a4f1-37b1-8636-e1b1c38542b3 | -11.36698 | -48.70735 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9b2bbb3-8b26-3f55-abdc-d8dbfa5cfb7c | -11.77398 | -55.02368 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c8c7fdd-42d9-3133-a2e5-bb8a85b16151 | -8.48967 | -48.26527 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b075d3a6-3bbe-3d93-9a80-871167e928d0 | -6.77586 | -55.48457 | 2025-06-27 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb70cd4e-0f98-3eae-a9ab-8d448f3570ed | -11.44578 | -54.46667 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc93154d-ff0e-383f-833b-5639afe5852e | -13.04901 | -48.82246 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85c064e9-dc44-3095-9875-40408bbcd826 | -9.37264 | -47.63253 | 2025-06-27 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 695e49fc-4f51-314c-8545-eeb0ae1f1243 | -10.83018 | -53.74607 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 053a4c07-e646-3c28-9996-2df797a08b20 | -9.37266 | -47.6311 | 2025-06-27 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7070fd64-eb95-3909-92e7-257894632c02 | -11.44187 | -54.46347 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343d259a-c51e-31f6-b536-be5ba939faa7 | -11.36191 | -48.71127 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 590727f0-afd6-32c5-a7bc-048afd952386 | -13.06136 | -51.64083 | 2025-06-27 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 015d96ff-8cb5-3f10-83e8-bd9c3ad9fca0 | -10.80432 | -57.75491 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4e3a62c-2abe-389f-ab03-c78a08d8104b | -12.03006 | -57.07984 | 2025-06-27 05:10:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf25cb70-f1fa-36bd-9239-c627faff8450 | -10.28926 | -59.44074 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28da913b-0a77-318d-a046-860dd41bffe9 | -11.5744 | -52.12363 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 98015165-2545-399a-bad7-564d712426f1 | -19.5804 | -49.11065 | 2025-06-27 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d06ffc9b-f475-3a68-9b9e-9ca46f3bd9a9 | -14.38002 | -50.32526 | 2025-06-27 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 334b8bdd-0735-38b7-9247-b218cb7cd872 | -12.60385 | -57.88333 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3f3e807-7371-3654-8f63-07763e0cfef3 | -12.5826 | -57.3792 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67a4f4ae-4915-3d7f-ae24-98f976148071 | -12.5899 | -57.37661 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52812326-99c3-3a97-829e-fae6d113f628 | -13.94363 | -54.4987 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b11d633-ed72-3485-8850-a7e97d3d7a12 | -19.57851 | -49.10606 | 2025-06-27 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46152193-728b-342d-b754-25b6a31bd62d | -14.44095 | -48.87138 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed404693-15d1-3cfd-9c2b-92fb0c972d4b | -11.85845 | -63.11257 | 2025-06-27 05:12:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5122a7f-3866-3b16-8486-8af220f9e19d | -14.20186 | -57.411 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ca7f738-f02e-3caa-ad4f-8cb1f24ae531 | -13.29217 | -57.08397 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f27017f8-a190-3945-9822-fdaf02f82e31 | -18.65592 | -55.74659 | 2025-06-27 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f5f818cb-6b12-310d-9d4c-e627c3aca11e | -13.29446 | -57.09204 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c94851bd-e7e8-3a4b-9e1d-16bbf357d73b | -14.40482 | -47.89231 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c80dbd63-8eae-365e-be2f-ce0cb573a5ac | -12.2875 | -63.7467 | 2025-06-27 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e0ef13c-ea6e-3f90-a5b1-74f4a9e6d7e8 | -12.5014 | -58.3477 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc23641f-98a9-385d-ae75-0dfad6d39fce | -12.58653 | -57.37607 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48343014-f104-3897-b1c3-e6279c09718e | -12.59494 | -57.87457 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee25bf5d-9e97-3022-b110-378ea0007c06 | -13.94499 | -54.48869 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af96361a-3848-3429-95d9-9e8b108f652d | -14.37965 | -50.3284 | 2025-06-27 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5c88f72-e5fd-3e8c-930d-584d123de055 | -19.58083 | -49.10594 | 2025-06-27 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dce0c09-2685-34da-afda-858babe71fec | -12.60106 | -57.87922 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18788025-e042-3930-9e43-ed2abc004661 | -12.59439 | -57.87815 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4a11e26-92f3-3c24-afec-453c0f5ec8a2 | -13.14202 | -56.80382 | 2025-06-27 05:12:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaaef39e-404a-3d87-91b6-609cdcf9622d | -14.23352 | -45.50352 | 2025-06-27 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 400e6b4c-4337-32bc-9cbb-9177e725c317 | -14.41101 | -47.89211 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5e81e82-55be-3077-a867-6588ccaeb74d | -13.29502 | -57.08827 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b84d05d-73fb-3cdd-a8f5-21c900ab749c | -13.9358 | -54.49762 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dac826a-3018-3f56-bc9e-8079e2ffda96 | -14.4352 | -48.87086 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62143d8e-3054-3d1b-9371-b75aa2a1d294 | -18.42595 | -54.56066 | 2025-06-27 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5df85d3-8677-3ac4-9cc5-e7cbbb1e80bc | -14.02044 | -54.49094 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15f98736-7fd4-37c0-ac58-565e376218e2 | -13.93716 | -54.48759 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7991f36-39d8-3af7-b892-cbec050c0024 | -12.73861 | -58.15298 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcfb2eb9-9710-3409-b6b4-6c4423c942a5 | -12.57923 | -57.37867 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abb748bc-efce-3fe8-906c-90219e267728 | -12.31046 | -63.73287 | 2025-06-27 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd6c700-044d-399c-aeb9-b66d6f987e35 | -18.65911 | -55.7522 | 2025-06-27 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 868a7eab-ce41-34af-a07c-337c15f1b7bc | -14.20622 | -45.51143 | 2025-06-27 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9f1bfc5-23ca-36cc-a26d-b14be0fa509e | -14.23498 | -45.50743 | 2025-06-27 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffb1e037-13c0-3a60-b3da-48a350e1fbe6 | -18.66298 | -55.75276 | 2025-06-27 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ab39edf0-8844-3de2-969a-aaaa229ec063 | -13.93647 | -54.49261 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44942299-3e9f-35d5-a3ab-cfadc76502f8 | -13.93121 | -54.50201 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d26e778c-182d-3066-bbc1-0f1d57daf160 | -16.70697 | -49.35618 | 2025-06-27 05:12:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README29.md)
