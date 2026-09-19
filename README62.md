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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc7ad6de-88d9-3a82-be9a-e8a02cd985b3 | -8.42519 | -54.72736 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1da36987-7fdd-3557-a07b-e43fda743569 | -9.79027 | -48.33937 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc11a88e-1824-315d-95fa-a91d1d4b7645 | -11.14363 | -54.02439 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7e03f6f2-2009-3a07-9f16-55af71166677 | -13.6252 | -48.31713 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f53c6762-fd8c-3cfa-9e6a-e4c4045e624c | -11.17941 | -45.387 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3579a096-66d4-3891-8448-a0f078184f2c | -10.80474 | -50.8946 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e3c9e2e-62bd-349f-bb94-e5cff980bc04 | -12.15646 | -46.97128 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daf5493c-9dda-35b4-a5f2-e81646aa29a0 | -10.16968 | -48.45739 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4990db1-fcaa-3895-a073-85d1a7ef9435 | -11.67334 | -54.44254 | 2026-09-19 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 535d951f-59fb-3b5e-bed6-a46045c5f64c | -13.61283 | -46.93472 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bada1b33-f2f1-3465-bf83-c1c50f17ecbe | -14.92703 | -49.91758 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 22041bc2-6c98-35b5-8630-229323e7de4b | -11.00217 | -48.32011 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6c3d7e0f-0b5e-3529-b849-24d7019c1ea4 | -14.69033 | -46.66311 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d013747b-5c27-34be-b5b7-6c6c004886ca | -10.48085 | -46.30103 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f874b5c0-baec-3e31-aa59-a3d1bea0a772 | -12.14032 | -46.98692 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77c34384-3c74-3d04-8f21-ffd571bd3ff7 | -9.79856 | -46.09507 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 960e7880-65dc-371f-89ba-2b5458918dbd | -12.58127 | -49.09546 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6d7e4f9-9abc-38ef-b26c-d69dae153165 | -11.48937 | -45.73412 | 2026-09-19 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b871a329-4f89-3c80-881b-165b1843e3f5 | -12.13702 | -45.14005 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a1ccb11-7cab-32de-a078-728dc572ca1f | -15.02321 | -48.56147 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e3e7478-60c2-3ba3-86dc-c99afe4f780f | -10.53747 | -46.75304 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88e59da1-ad35-3df1-a52c-77d8a7990781 | -9.82358 | -49.24186 | 2026-09-19 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65dc8fcd-eb7f-34cf-9e73-b2a5d593da7c | -7.57935 | -57.69558 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56c180f0-0b5d-3982-b574-ed3c06609cb1 | -12.14477 | -46.98032 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4166751-5fba-33ab-80a2-15f9887f4aef | -9.93788 | -46.52372 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 181267dd-4cda-3078-9302-3e7ddbb0dfaf | -12.28395 | -49.15933 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33a8a26f-7c2a-3117-b558-bc4911cead31 | -11.07922 | -48.29927 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7fdec6ea-0735-31cf-8d5f-af0344ac6103 | -11.32322 | -45.54461 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50c64ff1-dee1-3e38-a9d3-05fe4b057958 | -11.43565 | -51.45902 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 107578cf-928f-3d37-a922-6e00acd9e78b | -10.36685 | -48.89675 | 2026-09-19 04:40:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1604f362-dc83-3049-98f8-e7d3c7b74697 | -9.73538 | -48.13861 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb85938d-31df-39b2-8192-22eb5db984e7 | -14.16703 | -47.0334 | 2026-09-19 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc56e40b-8577-3b1b-b37e-1c4afc7196e2 | -10.88907 | -54.04967 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eafda7e-35fe-3131-b785-8fa63a519bf7 | -10.5806 | -46.54285 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ee22779-6c7a-3e16-9e6c-9c9bef2b8952 | -11.06762 | -48.26463 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bec9aca2-5113-3483-bd7c-a77d36e709f7 | -9.57126 | -46.55916 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e5ac4d6-a6b0-3343-b0d7-55996c32787f | -12.58804 | -49.09662 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d5b6d3a-f0eb-335e-bad1-538f2d5f0552 | -9.79144 | -48.33217 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bce04072-7bf8-3ee6-be5a-a396857acea2 | -10.83448 | -50.17851 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 268860cb-0af3-3245-b725-31d90a452d93 | -10.17252 | -48.52501 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b0aa4b6-4cd5-3938-a6d6-a83800e17b14 | -12.5496 | -49.09761 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 036348f1-733e-3a84-9fef-67c6f8db27c6 | -8.6091 | -54.58785 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6634a2c6-4180-32e4-bc52-9941da1e5c83 | -8.77764 | -48.68052 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 538bbe38-ee41-3cd5-9021-cb5850a5513c | -11.07701 | -48.29163 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 60971aa1-9cfa-38fb-8732-b6061972eaed | -11.32536 | -43.99158 | 2026-09-19 04:40:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f880238d-ffed-3bb7-84fe-e2af95e7e7a5 | -13.62471 | -48.29874 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ee06397-07d9-3dff-b2a3-3e95b98416b8 | -11.12195 | -45.28469 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f7575c7-9dca-38e7-a88a-f268a8036011 | -11.32866 | -47.67782 | 2026-09-19 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7c92b0f-fee8-3bc2-a833-4941d3cf71e7 | -13.62691 | -48.30642 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccc79536-17db-3fde-b256-fc5e98384d9c | -11.52307 | -39.09006 | 2026-09-19 04:40:00 | NPP-375D | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae06c5fc-040b-32e3-98f8-f1be82ffb89e | -10.51346 | -46.71621 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87342cb7-1b60-3d39-aba8-94b19d00713c | -12.37479 | -47.00215 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0101cd3d-8b45-3e6f-a726-38029d54fac5 | -11.28008 | -54.12418 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39d6834f-b46b-3e00-835c-862ff45db324 | -14.68579 | -46.64708 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd1fea0f-d013-3398-b08b-469cec8f6963 | -9.90709 | -46.52974 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6161dbe-b34e-39a0-bc07-2e8d296158f4 | -10.70489 | -50.2637 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5db6c242-e555-3838-ab2d-a865d023c0a3 | -14.1535 | -45.21412 | 2026-09-19 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 003e7a88-a1a8-38c1-b392-9c3c818c820c | -11.24671 | -54.10363 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 499ed538-a3f8-3529-95a2-6df343a82489 | -12.1242 | -47.00249 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c829a009-fadf-3845-bcc9-d431174383b2 | -14.95808 | -47.53556 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62312a00-462b-33ee-8964-7410086f1423 | -11.82053 | -48.83341 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbf9ab73-5846-39bd-9ead-66e1e8b53cf3 | -14.66709 | -46.65554 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6dc092fb-c283-3e28-bbe0-d8399851e4fd | -13.51409 | -48.94353 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8d3884d-e85b-3eae-9542-ee229cbcc9be | -9.04111 | -48.75383 | 2026-09-19 04:40:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8442a402-6247-3353-a0fe-e14860e0649d | -12.99948 | -46.98163 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c44949e9-1504-3080-9385-3a5d30a3d6b7 | -9.94976 | -45.27194 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92ec9627-30fe-3b55-bdd3-21fa0f709a61 | -10.62633 | -48.71898 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c583f40e-c79c-3240-9c7d-bae460f710ac | -9.41168 | -50.20479 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 167dabdf-cf63-3059-8703-46ad63d26751 | -14.67674 | -46.68385 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a50ca257-a7f8-370d-a33a-43450087a53a | -12.13421 | -47.00419 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f48f0ece-5b7d-380d-a1c6-4a3bc656d98d | -11.07873 | -48.28102 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b00d3337-b9f7-3c07-b9fd-edd2962b6c5c | -9.8049 | -48.33469 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4150ea6d-5d25-3d91-8190-49fd500cf5a5 | -10.81139 | -46.15075 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0b85a6e-1596-389f-857b-2ad4e3627cf3 | -11.42429 | -51.45699 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 019cec79-6b7f-3a0c-b669-25f1553a40cd | -7.57416 | -57.68987 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0feb96a0-f863-3b55-b77f-7e4a766076d9 | -10.91442 | -50.86238 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38cf6db0-05be-32a3-8b02-c9b376e3de1a | -13.00894 | -46.96488 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7507f911-bdf9-32b7-a8f7-81a0e28de5ad | -9.73028 | -48.14881 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c2120ed-4fcd-37eb-b4b3-83405501ad15 | -14.17276 | -47.84546 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 168e5a2d-7801-38e1-b55b-9c3e829533ce | -9.71426 | -54.81617 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a512f21f-702d-331e-a005-83b08793b66e | -13.00283 | -46.98215 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2f8fecfc-ca23-3967-a1c6-3866732fdb46 | -9.90043 | -46.55032 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b12dbff0-8b19-3fb1-8b01-bf7536af70b0 | -13.52081 | -48.94468 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fdcda0a-8092-3a48-ab67-28be84a19d61 | -12.58081 | -47.09031 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac022bf7-595d-3c24-9f40-93c2f302c411 | -8.84322 | -50.44768 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a8f02b2-76db-314e-b0c4-28ea7de19d62 | -12.12474 | -46.97705 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1af3c49a-8164-38f7-b374-92c566447ad4 | -10.89277 | -54.055 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcba5aa3-80f8-371e-b4c8-4b71722a4f76 | -8.77325 | -48.66422 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| afc3b57b-45a1-330a-ad3f-3a16bd2726a0 | -9.72798 | -47.12316 | 2026-09-19 04:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 211aff3e-6fa3-30bb-ba68-dc87d6340bb2 | -12.86154 | -46.33487 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1f9f752-b831-3c3b-82cf-20c6aca3b1a3 | -11.43944 | -51.45968 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d289d75-0a78-31b7-8785-ffdccfe3f71e | -13.60947 | -46.93416 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf7fc0f8-824f-3fde-9f35-545d6981f3c1 | -13.00783 | -46.97201 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 843386dc-bdc6-3d03-bb58-f63dcde24421 | -12.41437 | -45.03717 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07467586-942f-3ba2-ad33-e1a2ec686430 | -11.07806 | -48.30642 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f47f0bbf-1b39-3de9-9a05-66435b85dfb5 | -10.57615 | -46.54942 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1bdc09c-fef1-34d4-91ad-503f77508b18 | -9.91097 | -46.52678 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91559705-46a9-3a89-94c2-12b3aadb1075 | -13.74123 | -48.79234 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fec1956-7959-3ff1-97cc-487bc17de940 | -14.79595 | -48.58561 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c11333d0-51cd-35e3-83d1-eae1d38ec545 | -14.79895 | -48.54563 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README63.md)
