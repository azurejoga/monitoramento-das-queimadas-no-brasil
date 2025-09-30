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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b395beec-c100-373f-a016-93971adee13e | -11.20432 | -47.7396 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75b906d1-b3c8-3283-aada-8911ea886cd4 | -12.75489 | -46.87672 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a775f37b-29cd-3b51-833c-b1a65bb37d53 | -10.9556 | -46.49332 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3bb69a8-adbc-3b2a-8071-f535fb746b0b | -12.85813 | -46.9922 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cad47d81-1567-3fa2-886a-c703ca3496dd | -6.94408 | -45.39643 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9eb2b9e-8cd5-3130-b48f-eef2201af545 | -8.00397 | -47.04918 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddfaeaa2-66c8-3077-b497-125e24909742 | -12.79301 | -46.89928 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81b250ed-892f-3766-9fed-24ae8ed17fe8 | -13.35047 | -47.81044 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e54a1018-3e00-3785-9189-b321a38878dc | -12.77424 | -46.86233 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 461e8e49-9d58-3e42-9365-88e0c1b5831c | -10.42919 | -46.14766 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5da78efa-fd8b-332a-9edb-26c273d690f6 | -12.83749 | -47.01852 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e566949-338b-344c-8b79-4a8a3c3c3289 | -7.926 | -44.62923 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 844746a7-40e8-33e7-81b3-b4bd3ec0b493 | -8.83483 | -46.18763 | 2025-09-30 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2169651-d985-371c-80c4-304f00a50dfd | -12.84411 | -47.01182 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b17fac7-ac1e-3f27-b0fa-8dbcc7a3d610 | -11.39476 | -55.08499 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be9184e5-b1e7-38d5-badf-85d75f552ef5 | -12.961 | -46.87213 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74d0bcb4-dc3c-3e38-a6dd-73d20b5e475d | -9.39702 | -54.7012 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 994a25b2-8735-3fbe-b7b0-194684640ccf | -11.4337 | -55.03694 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36d5b31f-8821-36d3-9320-c4b341187e49 | -10.96141 | -46.49392 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3cebd71a-3391-368f-b372-e7ab254b9c71 | -11.16053 | -54.12542 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 506f5dbd-4aa0-3575-a2fa-d93ef9c645c0 | -8.71375 | -47.98045 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d053173a-363d-349a-8dc4-ac718e4c5fda | -13.56521 | -48.19983 | 2025-09-30 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bc3a2cb-5f65-3ce8-b669-ac42130ddc28 | -10.64737 | -48.5933 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80403483-5aa9-3f06-9eda-2997067513d5 | -11.43641 | -43.50506 | 2025-09-30 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10b5772a-d94b-351f-9f39-fc58cee88899 | -9.40218 | -54.71341 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab5591e2-e627-351c-887a-8578de4ee374 | -9.37024 | -47.58465 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01ec1e90-284f-36d0-907c-81a8ce33e2e7 | -12.23494 | -47.79828 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86369985-6d9c-32ab-8605-c69d48f60bf7 | -12.84139 | -46.98575 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 297f441b-b7f1-32df-973d-4669d038a7a3 | -9.41074 | -54.7033 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1f1e193-792e-3091-9a67-d9be4298fd5a | -7.11131 | -45.54751 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f802c160-f76b-3b92-8dd3-d4b54a9bab2b | -10.88844 | -53.75439 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 433ed376-de8a-3964-81dd-5da0920e27de | -7.7082 | -55.44935 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fccc75bd-fc75-3d96-99f5-b864c241a940 | -11.19446 | -47.2325 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91c55347-c195-3ba3-a63a-0939852b90b1 | -10.80741 | -45.3587 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e026ab-1300-39b1-ab72-2eaf768e07bc | -7.78674 | -54.92397 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 802f297a-2c0b-3bf2-8a30-2b2a0cf3ee17 | -5.9845 | -51.90739 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2193771c-42cd-3582-8f90-777f026ebe5b | -9.39816 | -54.69372 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e30bf9dd-5b9b-3544-bd66-2c85e38575ea | -11.76093 | -44.74599 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad02f9df-201d-33a1-a5b1-9337b502cd6b | -6.36905 | -45.63107 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 845f68bb-e82c-3f43-968b-896a4b83da1b | -11.88909 | -48.05265 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4d8b2c2-9deb-315b-b769-6860b8c15687 | -11.12602 | -48.35588 | 2025-09-30 05:08:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd407917-497c-3355-a115-5d38fd885a44 | -8.32304 | -50.88301 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b08ededc-c646-306a-807d-f7fa94815ae1 | -9.50947 | -47.6983 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14b4b2f3-33dc-3118-b792-b22166b725d4 | -7.75919 | -45.76941 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66478695-bfa8-3267-959b-f725805210e5 | -10.18416 | -44.89178 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66c6e345-e0f4-343e-932c-9b225d870aad | -9.40561 | -54.71393 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2dff79d-7f54-3e3b-8823-b8456e323109 | -12.84367 | -47.01557 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30146fac-ef29-37a0-a843-dccf8e6786e5 | -7.76831 | -45.74714 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 726c0460-6c51-3bf9-a578-85af62d58a0e | -7.85227 | -46.75688 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff861f9a-3824-3194-b1d1-46df641b3c06 | -13.35275 | -46.38275 | 2025-09-30 05:08:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 934db09c-f80d-3ecf-be93-d2d6e010a199 | -12.89109 | -46.76648 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 64eda21b-0214-32f9-9bf5-64e2c7c320ca | -9.93589 | -47.45676 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3255bb35-8dec-3c3b-b863-d0a0001b1f1d | -11.26105 | -47.22925 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f38c6fc3-23e3-3a67-b879-67cbb870b9b5 | -13.39035 | -48.07368 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7ee2d8d-3a92-3c12-8c85-e46ffb620261 | -9.40275 | -54.70969 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 344b3973-64ce-399c-bb95-9f5b0d5d0eca | -7.51947 | -46.687 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a8d1262-ae41-332c-b0df-472f550858b2 | -13.39378 | -48.06382 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46af141f-1729-30c1-a1af-6a447488918c | -11.84561 | -46.61801 | 2025-09-30 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65127237-7ea4-3e36-b6b3-9d93e2369e90 | -11.03389 | -49.81368 | 2025-09-30 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86e4ace6-6514-3b77-99c4-183a5033dd15 | -13.23753 | -48.44771 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 514595a7-f916-3b46-ba68-372409fe02de | -7.01414 | -44.47632 | 2025-09-30 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5d2332f-7a2d-3cf0-9c4c-52e621609a66 | -7.68475 | -61.06078 | 2025-09-30 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b637d045-14e3-364b-a91c-f41a143f7468 | -11.63496 | -46.84451 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28ae3e53-c4a3-3d2b-9901-b89dd992f04c | -8.71294 | -47.98634 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb3aa7db-3442-3047-9c36-234ab07ac67c | -9.39759 | -54.69747 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 102ed970-66cb-36c0-942d-7a65c3081f2c | -13.23647 | -48.45141 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98f45937-ac2d-3fd2-bbd0-4268b1aa8070 | -10.18481 | -44.88663 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3d8b3bc-8314-3957-abc2-15b9cbf0d69b | -11.22233 | -54.84168 | 2025-09-30 05:08:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e90eea2b-499e-3185-a35a-8480b009dd2a | -13.39341 | -48.06701 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27710394-5751-3eef-9606-0b95965adb80 | -7.47969 | -47.26778 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a63a16b-4ee3-339d-b2d4-ae664be14880 | -10.4094 | -48.17508 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85402bb1-4529-31ca-a990-468ef4019695 | -11.44071 | -44.959 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1cf65588-034f-3b19-a0c5-58b218736851 | -12.80003 | -46.88929 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f521568-f9ee-32b6-9bcb-fc8d8b837335 | -13.04199 | -47.0781 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a61c51d-6d75-3357-9953-b3b3aeb7348e | -10.10554 | -47.78287 | 2025-09-30 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad5b0c83-1430-399b-bb60-4f18c554a574 | -8.82848 | -46.19142 | 2025-09-30 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82f30a10-ffa4-3312-956d-86a75af33c4b | -11.76159 | -44.74038 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15ba6218-2dba-31cc-a5fb-a7853c01a934 | -13.35877 | -46.38341 | 2025-09-30 05:08:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d27bf25a-4a9c-32ae-b367-508d2024a7ac | -14.54273 | -48.48704 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94c77597-b51b-3a35-a72d-5c0a528b1061 | -17.73356 | -46.67871 | 2025-09-30 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a66a43d8-a1d5-3e83-a233-45f2f0040901 | -14.51558 | -48.44095 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4c0b8bc7-8bc7-3565-be3f-0e8455576474 | -19.79752 | -46.5212 | 2025-09-30 05:10:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff2624c2-16db-3554-ba22-95d7dc926662 | -15.2763 | -48.02248 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 420c0103-7fe5-3f0b-b845-eb2c7e7bf4d0 | -14.53232 | -48.24573 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6cdf6628-040e-3341-a8f4-2ad627c207d6 | -14.52782 | -48.47572 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47bbe70e-872b-3d86-8c02-83e1bfb13dc3 | -14.56688 | -48.23178 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b38be197-c2b6-3d99-857b-2c06d7f4cdfb | -14.56785 | -48.45749 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b36bb55c-186e-37c5-84b6-88780fcf4a08 | -14.66615 | -48.14766 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcb0ad12-0742-32f6-bb7e-4b42ab8cc452 | -15.46934 | -47.93762 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db52ab45-52ca-3ca2-b35f-b3fb639b73d9 | -14.52225 | -48.38254 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d1e7f72-82d6-35e3-bf90-25083e07bf3c | -13.80441 | -47.88421 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 640d99dc-f19c-301a-95d2-02f0d874ba05 | -14.51085 | -48.45749 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cef99a2b-2d66-3e8f-aa73-8faf81759935 | -15.90667 | -46.22637 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9891b93-14fb-3587-a707-2215be15e0f7 | -19.86075 | -44.56371 | 2025-09-30 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e0068f29-a582-3228-a5d6-0a03b426970d | -14.55159 | -48.25735 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3913ddd0-3520-3c34-b0b6-3270db56513f | -14.53849 | -48.23974 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4977c659-4131-3ae9-a504-8ba4d2f1c662 | -13.7345 | -48.67829 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52d5d20e-ff8a-3196-bb62-a3fec3390edb | -15.27957 | -47.89541 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50ba0807-4ce6-3803-866b-634ef2d1500a | -13.65087 | -48.05437 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e680969-ab77-3e35-86fe-d04e13654ab4 | -16.16377 | -51.94249 | 2025-09-30 05:10:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README95.md)
