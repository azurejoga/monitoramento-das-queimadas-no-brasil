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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c7e2799-2c7d-3a99-89d9-75833dc74929 | -10.3824 | -45.40871 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2883e119-345d-3f3b-8566-61d2d83924ed | -6.71431 | -42.85049 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4c5c052-c5e6-345e-ab84-cd3d0f771902 | -5.7602 | -43.39259 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af331264-35f2-3289-9c3b-eace836c4cc4 | -6.72675 | -42.82272 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f535f5f1-86f9-32fe-95ce-fdb96508f92a | -6.28292 | -42.94002 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 181bee7e-532c-30a7-bc4e-583f81c6573b | -6.51992 | -43.57194 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68c42715-28d6-399a-8395-f19be1dd7569 | -5.33921 | -43.37981 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae4aae65-ff9b-3280-a2f7-284fcd42b7e2 | -7.02203 | -42.78357 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1e200c26-3738-3fc8-9a1e-5f71691f663c | -7.8904 | -47.8147 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff69f634-ed58-3efc-9d42-2ca406c4e3f2 | -6.45723 | -42.79505 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 238487e0-afb1-3d16-9c04-077f50050ad0 | -5.74263 | -44.98845 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b48bcc60-9c4b-3aa6-99d2-aa23ad3d6eb9 | -5.53496 | -50.06131 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0ed54fb-a8ce-36ba-af4c-0cff24f7120c | -8.56609 | -46.23985 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc92d412-3401-32d5-a02d-56039b0c8e34 | -5.76265 | -45.74809 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36eb6b0d-3552-3cfc-b13f-8d10c35de3f2 | -10.16188 | -45.42367 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c0ee22f-21e8-3f41-9c01-15cbb8ab328b | -7.6759 | -50.20845 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14a32c6b-24b7-311b-a147-ead2cfbc1206 | -9.48463 | -49.82279 | 2025-10-07 04:36:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ba4534d-456c-3fff-bf0b-9d4523039f4c | -5.70726 | -44.82657 | 2025-10-07 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c14fbd-0f6d-37b4-be5d-d5cd9f06d95c | -7.28848 | -41.98319 | 2025-10-07 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a03804ab-725a-3ae1-9c0b-02a107dbf279 | -5.76147 | -45.75565 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87e710bc-633c-3b5c-b8fc-79a66403e45a | -7.68646 | -42.4097 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9ee4a496-87b8-34e2-b981-d5c6bef8ae16 | -7.88706 | -47.81417 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 173a5736-1657-3a60-a3d7-0d4802bde04b | -9.00777 | -49.2197 | 2025-10-07 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34bd7ede-cb97-3548-bc4f-cf93d2a5efbb | -8.19885 | -44.20225 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d5842db-3d60-3be7-9ae9-a6a5315a70f6 | -6.67518 | -41.39134 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d677bb8-8917-3c04-8766-12253e0e18cb | -8.34515 | -49.65417 | 2025-10-07 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 389050b7-ed4d-3e8c-81ce-c0aa1a0674ad | -8.85268 | -46.10437 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 696b79c0-9376-391d-9a48-1ff2ace5f79a | -6.81477 | -42.787 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0295822-b8d1-31b5-8622-c7b4b7dd6c3b | -5.85193 | -42.85836 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 33bfab87-f289-3b81-951a-f1b525ad5298 | -8.1833 | -50.30787 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10993b99-f75f-32a4-9fbb-eb4b61fb2a08 | -7.06589 | -42.77125 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8a5db83-72bd-3321-99f1-c8a5f4237f21 | -8.10577 | -55.08239 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4363d45c-de31-3a99-b9f9-78c82e77117c | -10.41429 | -45.3959 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 107f0f78-9c0e-33f6-805b-526894a6e26c | -5.47567 | -42.8896 | 2025-10-07 04:36:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a22f7732-3b28-3a25-a75f-9f960b3b2cc0 | -5.48903 | -43.07397 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 66a288e4-d87b-3f2d-8db4-cfaa56da5d2e | -7.69496 | -42.41101 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 98e2f7a9-32fe-33a5-8713-bcc4b7e3bf73 | -7.25457 | -46.97206 | 2025-10-07 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af3bb1e9-ae36-3b9a-ad8f-8da8742bb3b6 | -5.92849 | -50.21715 | 2025-10-07 04:36:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ac8fc04-aed1-382a-9fdd-bfa786e145a7 | -10.02997 | -48.29726 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26e9113c-03ee-3a61-bc0f-5cf074f6784d | -6.45671 | -42.79862 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f54af60-e055-39cc-8ae0-7999283ed120 | -7.01954 | -42.2936 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| afe9aa92-6d1f-37de-9260-5c71074da605 | -8.62154 | -44.93143 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e05dcd85-c59c-3302-a8f5-b39b3c0464a9 | -9.73608 | -48.08089 | 2025-10-07 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cb380a7-f7ab-3b2c-aa5a-03657cb819c1 | -7.52384 | -49.91199 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4faeab90-02d9-33ad-b865-d716595b36cb | -6.85185 | -51.06107 | 2025-10-07 04:36:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12d5d6d1-d672-310d-867d-08707ab690d2 | -6.31721 | -41.61567 | 2025-10-07 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b0cd344-3828-3415-9faa-ed180211656b | -10.20984 | -48.93712 | 2025-10-07 04:36:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ab8629c-65f1-3b2c-b20b-848a62966ec6 | -8.7493 | -50.66771 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d418a862-9fca-3c44-ba02-881faac18084 | -6.21994 | -44.32949 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8b331ec-2c71-3af5-8aaf-12330bf831fc | -8.49455 | -46.32715 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d9e0c78-55f2-3b6f-aafd-1377dfbc54ed | -10.22061 | -48.17915 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67bc376b-8edb-3080-a877-42548d58f94e | -5.7462 | -44.98897 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1afb2d9-2c92-3d1d-9d74-2df8a8a99bcc | -7.70213 | -42.39206 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81c9b721-a1aa-3db4-8b93-cccc5299ab97 | -6.72622 | -42.82631 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f4762315-22a9-367f-b416-037f1289f7a3 | -8.61483 | -44.92596 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05bc0e3c-d521-316d-8d10-2e6010bff238 | -8.95396 | -48.75019 | 2025-10-07 04:36:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b90d8899-3b6e-32fa-b832-21416248c5b2 | -8.61389 | -44.92386 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c00d77dc-e420-3af3-9036-7669651c26e9 | -8.62175 | -54.9705 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18c5c63-530d-36e5-b4ff-3f7df20b2d9b | -6.58756 | -44.62587 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b9b947eb-e14d-3ba6-a08a-5069feccddf4 | -5.42709 | -45.99751 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 758c400f-ca52-33bf-b505-b9df35b75f18 | -7.80173 | -44.13279 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b885683e-c3c2-31ff-b146-77900f3cd3be | -5.09396 | -44.87474 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f25d74cf-6f23-320d-826a-f7eadb0162c6 | -5.254 | -46.48477 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4751ae38-16be-3ca4-930c-e30409a9cda1 | -7.6936 | -42.41339 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 754266cb-b227-360b-a297-3bb267c546f3 | -7.51824 | -49.90797 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22dcd6c3-23aa-366a-b381-43ab3d634210 | -10.38626 | -45.38187 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6a9e81c-1b9d-322a-87aa-ecf86d46f49d | -8.22186 | -49.14003 | 2025-10-07 04:36:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cb2a330-6875-3dc2-87c0-caf042e7fc38 | -7.79075 | -42.6063 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ad87b88-b551-30ab-b418-1cfe330935ab | -5.8479 | -42.85782 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d50f7585-4308-370a-ace9-cd2b6c6a751a | -9.33698 | -54.52413 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7e2b411-7d12-3484-96db-a7562ee74597 | -6.70505 | -42.85686 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 91ca3e0f-34c8-3472-9b1e-59ac6f6e3021 | -6.2565 | -43.27878 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 942e6919-b0ea-3cd0-ab36-58cdd19db92b | -6.24151 | -43.27128 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b158ec63-e1a3-3ab7-9c47-0dd8a255ae2a | -9.01736 | -50.68982 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db0909c1-36d6-3702-8088-7ebf11a88696 | -3.66292 | -51.94994 | 2025-10-07 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a1f9d3f-7a91-318c-b400-14f629a0f038 | -5.25908 | -46.49648 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 611edf0c-7e8d-3fa8-a430-f9ce29b0c697 | -8.19135 | -44.1185 | 2025-10-07 04:36:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a518fd71-6597-3fb5-a9f7-d622c76870cc | -7.03454 | -42.7553 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3cd98721-43fc-3882-9d66-b0d4ce6a8ad8 | -5.16968 | -50.64478 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9aae43c-4e18-3b09-b471-a529f01ba029 | -6.98501 | -42.87092 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| c07f681b-6139-3659-9b47-8b70a3b72bbd | -7.64871 | -43.89627 | 2025-10-07 04:36:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b7b8311-ed48-326f-8143-302b5689497c | -5.79395 | -45.4771 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b04118d-906e-3709-9e7a-ead68bf4a329 | -5.54766 | -42.68039 | 2025-10-07 04:36:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c9aa0fa8-fedb-3a00-9263-d80fc8218474 | -5.55119 | -42.68452 | 2025-10-07 04:36:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5ad55588-c06d-326e-88e5-4150514f7223 | -5.46006 | -42.90038 | 2025-10-07 04:36:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 435d392f-a325-3c89-85be-7a3d1d1182ae | -5.77762 | -45.74271 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76178ba3-53ae-35b7-bdd1-74f6e1bdfd69 | -9.6705 | -45.67348 | 2025-10-07 04:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 174b274e-cf7c-3dcf-8c47-454ebcba65e7 | -5.23081 | -43.79482 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3066e03c-1aea-37c7-aecb-9abefa41bb74 | -8.86687 | -46.78411 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a43a446d-0113-34dc-adfc-e4dd4d9b752e | -8.49112 | -46.30339 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 144dbc0b-e578-3a14-84fc-90cf7b1c0200 | -3.46555 | -53.45436 | 2025-10-07 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87b870c2-f128-351b-929b-3b1e298ad4d4 | -6.7166 | -42.80654 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 78e1045f-9185-32e3-8aa1-1e20d4db9d38 | -9.02085 | -50.69032 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49bb6c39-542e-3abe-9203-807caa1cfe26 | -9.04859 | -50.69503 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1fdce15-9d4f-3c76-a932-e7917d2c97b6 | -6.98092 | -42.87029 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 1fc900cb-ea27-3d86-92b3-a4daabc4646e | -6.65416 | -41.97287 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90d6dd5c-7572-3978-8ebd-c4a4786e8d9d | -8.74902 | -48.8712 | 2025-10-07 04:36:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18922514-37a0-352a-91e9-c7fa0b5e0f0e | -6.6455 | -42.75949 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 25880453-f09c-3205-b090-4984db8f49c0 | -3.87009 | -54.35265 | 2025-10-07 04:36:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48694826-e1cb-3572-9381-a94f78a19931 | -9.00834 | -49.21616 | 2025-10-07 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README58.md)
