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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1228b676-fdbb-3f9d-8d7c-81483d5de94c | -12.23408 | -44.79496 | 2026-10-10 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6db360d9-80e2-3008-b9a0-749503b3b8d5 | -6.11448 | -53.09469 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32a62f0a-daf2-3fdb-a69b-f00ed227f36d | -6.70821 | -58.71625 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5205ba21-e9b3-3627-9387-589997f8eb1e | -11.7655 | -43.52728 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07ffc756-a73e-3a55-ba71-5f45c6142bc7 | -12.3833 | -46.61359 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62e99573-24b2-3575-8292-beb3fa2b71af | -13.17863 | -48.12481 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c86d78d8-b611-307f-948f-0a51db7a3186 | -5.21884 | -60.05321 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31571fb3-27da-3570-bb81-6158fe378037 | -13.51053 | -48.61203 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ea9aeaa-afc6-3ace-b5c5-924d8900d296 | -12.29107 | -47.03868 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72c3e83e-d71f-3972-a07d-9c299ef406c8 | -12.37041 | -46.60347 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bb6ca17-4658-397e-b860-d9e603284728 | -7.25531 | -47.46997 | 2026-10-10 04:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bce69019-4cc6-362c-b1ec-2c66f9ea647a | -8.35639 | -48.14537 | 2026-10-10 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe62fc3-c35a-341c-86d1-bde0c5ad4a4a | -8.58038 | -53.10288 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93006b41-1439-3dfc-a525-2e61238cd92e | -11.84307 | -46.80776 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5427069a-f0be-3e65-8e64-bb94f81f671f | -6.45745 | -55.50579 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f39f9a5d-0bf6-3bda-b7c8-01d0b8cf6d5b | -9.92134 | -44.77971 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea37c82e-0ab1-3429-bfc0-742bb8478512 | -13.15156 | -54.36747 | 2026-10-10 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f75f3d8-bbb9-32da-8ce8-91694ae4eea6 | -5.08037 | -60.21646 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c486527-7860-31d2-962f-c275af37f352 | -11.99681 | -43.43896 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a779748-bc2b-3005-b3e5-95d3e7068069 | -9.88126 | -50.48917 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9770fe6c-5e32-36e6-9eb5-75ee8c27d777 | -11.04939 | -49.56173 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4e00b96-d63c-3af9-aa93-c55edfc075c5 | -12.77829 | -44.89091 | 2026-10-10 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29e6fe28-cc1a-3177-a1ba-3c90a32ac4b1 | -8.26352 | -46.41572 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 641c8d39-1801-35a1-ac73-947d5f9cf274 | -6.95148 | -59.36949 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f225ec7-d9c0-3783-9d62-85d71b03acd2 | -14.05686 | -43.83891 | 2026-10-10 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f82ae3c0-43a2-34bb-8e98-b5a7aadb1a40 | -7.49962 | -54.99238 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1585e955-397c-3dc1-9334-04902e55f647 | -11.01709 | -45.41732 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99143270-d0d8-3a2c-9d8c-29bd397821c8 | -6.49552 | -55.31723 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ea7815b-b2d6-3b44-8139-2b97bbd576de | -14.32782 | -44.67363 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ed1e212-4205-3b8c-b44a-7a0c61325448 | -14.44864 | -43.92252 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e36eb3ba-07eb-3395-be16-87a9e96c0d01 | -6.42522 | -55.27069 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3e538c4-c805-36b6-b6f0-97809b9b461d | -10.89705 | -44.81178 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d7fa8db-ea70-385d-beb3-58914c6f1fb3 | -9.21434 | -45.65751 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8f273cb-9351-3d71-868a-bd73ef666f2f | -9.92508 | -44.78031 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79c6280e-b89d-3b8d-8bd4-7efa2b0a06d2 | -9.21729 | -45.66201 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f8f3532-3497-39e5-bbf7-e3b932d37a74 | -10.39216 | -53.81345 | 2026-10-10 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f24e0fea-f5b7-36ba-bb7f-b383fdc30c6b | -12.22335 | -44.64844 | 2026-10-10 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a9a573a-1e1e-3c60-a217-1d825a6eaf58 | -11.08556 | -44.10455 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5562ef99-9d5f-3bc6-a381-94b716322cd3 | -11.73834 | -44.95035 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f947bed7-f2d8-3f44-8ead-52872d9f51a4 | -6.44178 | -55.03437 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cc1e46dd-2dc7-34dc-87b3-3f8728987073 | -14.44811 | -43.9265 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 178a4636-a6ec-3d9e-abf7-fe268ce37ecf | -13.4479 | -43.61776 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 378ea382-8c96-3db5-a869-c2083aa6672d | -8.24701 | -46.43204 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f8f00ca-93c2-3d98-a97b-1a6d249bfb1c | -6.45887 | -55.04754 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69db6fc9-e00d-33c4-b5ab-55c2b34ae92c | -11.95749 | -43.47615 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11f6b09c-2d90-37d3-88d0-d8f4253d7bde | -13.26724 | -44.00533 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d912b308-fd23-33ae-89fc-15adc176fea7 | -7.22106 | -55.14502 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1c1f0bf-6691-37fa-9ab9-d8a826f429a5 | -6.46272 | -55.05332 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e123c41-e26f-3774-a041-3d793c2b2540 | -6.98958 | -47.69559 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 318e537b-e0c8-3f3d-979d-3cd4a77f0867 | -10.45589 | -47.84434 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5db69064-fcc4-357c-b094-ae7dd20d0f13 | -11.08416 | -44.09665 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1b53a81-e3b3-3c6c-8fef-8327d043edcc | -5.08188 | -60.21922 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e34f022-2438-3b8c-8855-d2423180f6c8 | -7.10433 | -46.71577 | 2026-10-10 04:46:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3269476f-6d2b-3559-b07c-6f2591a8a8a7 | -12.07969 | -47.37852 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5427fdca-a8e7-329e-829b-c54afbff97c8 | -10.89437 | -44.83041 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 82474828-02ac-3bfe-a0fc-132facb2314b | -6.98625 | -47.69506 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e146fb7-34db-3321-8479-513ab8dbc618 | -9.95628 | -55.33104 | 2026-10-10 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb40d821-dde8-344c-8729-3263616c7bd7 | -8.77473 | -49.61003 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f5ec78e-9a0e-3eec-bbfd-7b9c09741ba6 | -14.53374 | -48.03778 | 2026-10-10 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75ecf2d8-81b6-320f-adec-6f45ee9769f9 | -13.91282 | -48.91599 | 2026-10-10 04:46:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94ea2b90-7bcd-3b3c-bf96-53c96eb1e211 | -11.77525 | -46.80957 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fe2d797-a5c5-3629-b392-5750d3ea25fa | -10.89772 | -44.80714 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e2ce9735-9065-3c8c-a201-b90ecd172caa | -12.49758 | -51.29894 | 2026-10-10 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 323700f3-e43f-32fe-8b53-d625670f8296 | -6.46743 | -55.05412 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0eb434bf-2951-3c5d-ab5b-0f4231e7e814 | -6.37463 | -55.16712 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35cbad05-762a-3747-a5ad-e415f4bbdd6a | -9.21915 | -45.64989 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b019921b-984e-300b-bb2d-d7126d1b0c6f | -10.60281 | -60.48482 | 2026-10-10 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bce928a8-1f5e-3bba-b18d-a0ca01e896f7 | -8.35307 | -48.14484 | 2026-10-10 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 149901ec-776f-3601-ac0c-dba1074ae38c | -11.76019 | -46.79143 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40263cef-1ebc-3d54-b2f4-323d7cb69b0a | -13.37719 | -43.88907 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27756e5b-8a38-3e26-8b1f-6f6979bc3fe2 | -12.9097 | -46.96535 | 2026-10-10 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b610f9f-fef6-3280-ac72-373e3bc5da18 | -5.24232 | -60.18921 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7ce8b99-8deb-3e3a-a19a-1ac962993136 | -12.58498 | -44.13543 | 2026-10-10 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3836437b-1262-33d4-99fe-8087c115ac6a | -7.02503 | -47.66553 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f9ea06e-7f64-35c2-969a-a8fd8bc7c753 | -9.27567 | -47.4003 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e030d6bb-e5c0-36eb-b32b-0d1b8e7cff47 | -7.02615 | -47.67998 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c443aefd-ab74-396a-9490-b6de5e8ea08c | -8.982 | -47.5432 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b06d88d-db9c-3b53-baa3-cac2d93a206c | -6.43107 | -55.20843 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90651dde-7a87-3c60-9418-47e1cbe11a48 | -7.22429 | -55.07066 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 128631f3-4979-3bcc-9e9a-b2492641788a | -6.76789 | -48.66576 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1a24624-2de2-3e1f-9aa0-2eabbb565740 | -14.24431 | -47.30196 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce17fd25-aa14-3313-a540-1a768ce2770e | -8.48962 | -54.61655 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc0351ae-c99b-30b8-a65c-89a0e45ce4e3 | -10.24776 | -49.66166 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1d43f76-9514-3ddb-a8b8-cae5975b1ec0 | -6.4521 | -55.28619 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9939abb2-7194-3a01-b5dc-4e1bf90f2357 | -9.11282 | -45.82571 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14d87899-9e9d-38cb-a6da-12937fe66e5c | -11.01723 | -49.11007 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 124dfb9f-2f33-311a-bbc5-9c593c132b4d | -6.77124 | -48.66629 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3e3d281-591a-3be9-ac7a-3415f5f1eb5a | -13.90948 | -48.91544 | 2026-10-10 04:46:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 294fd3b2-e980-3280-b203-7b8dbba389fb | -13.00647 | -48.52037 | 2026-10-10 04:46:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 291a1938-9084-3c49-977c-3eabb491fb3e | -8.49995 | -54.60945 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 388b4215-66f6-36a8-a929-eb242e3560ee | -6.48846 | -55.96838 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b5391e-2f31-33df-b8eb-8f7f0bba02d1 | -13.52797 | -48.43375 | 2026-10-10 04:46:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b583e55a-ca0a-3bd6-ba45-33e3463fe879 | -13.14711 | -46.33255 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0abdb121-b144-3cd3-b965-b4a008452a0e | -12.29684 | -47.04741 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ca67c46-724f-3ff9-899c-4ca889aa83a1 | -11.98581 | -43.45652 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef879095-0bd6-3227-b4d7-177d104f250c | -7.91365 | -54.72155 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7055d4da-3c25-3736-acf7-098a4392cf94 | -7.93527 | -49.74487 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0380fa8-c08c-3792-b334-cf4907d7f849 | -9.12516 | -45.81564 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3b0b476-1f23-3b30-9f23-7dd9bbc1d99f | -12.03979 | -43.37863 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f42740d-1145-3007-8920-92cd5984687b | -7.77116 | -43.79166 | 2026-10-10 04:46:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |


[Clique aqui para ver as próximas entradas](README83.md)
