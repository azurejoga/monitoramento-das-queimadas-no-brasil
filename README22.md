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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87616855-0914-3f0c-a448-2192a44688b9 | -14.96263 | -46.98806 | 2025-07-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5f5a0d3-9cf8-37c8-829c-cd4fe0d0f443 | -12.68534 | -46.99371 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a711f1d-1699-3d2c-a34b-0dd3ffba81b5 | -12.77731 | -48.81961 | 2025-07-26 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 088fd589-4eed-3ad4-9410-51930bcf884e | -15.02907 | -52.7797 | 2025-07-26 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 505266ef-e96d-346e-a2e7-230b989fba94 | -13.10316 | -47.36282 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cb3ea90-b628-3f3f-97d6-06878e9ade70 | -14.93456 | -46.94574 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4fc61d3c-c9b3-3781-bdfd-99909ede0a2c | -11.92607 | -44.54684 | 2025-07-26 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1ad430b-a89e-355a-94a1-074061077fda | -15.7821 | -41.32611 | 2025-07-26 04:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 508d30d7-a569-3bd0-b26e-b04172853f66 | -12.1228 | -47.91888 | 2025-07-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23d3de04-c6ca-3347-8cc2-c875cdb6cb29 | -19.14387 | -46.14579 | 2025-07-26 04:27:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8d8a218-9381-3453-8527-b0d827f6c634 | -13.12966 | -47.32336 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 909d0f70-2ced-3925-bc2e-d6e43f002343 | -13.72264 | -45.69156 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f8dcd5b-f83e-3cd1-bbd7-86eabc65b2ca | -10.85224 | -54.03717 | 2025-07-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62794911-0895-39db-980a-542777ff5720 | -14.85864 | -48.12453 | 2025-07-26 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb360e38-98fa-32dc-8fc3-13d4c739eff9 | -14.94684 | -46.95575 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ea4e5c2-deb1-3d7d-9bfe-fcd455c7b6ea | -13.69713 | -45.67152 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e009b19-d70a-35d8-b5ba-6ecbc8af17a5 | -13.10866 | -47.34927 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 024b14d6-dca5-391a-8906-b9f4236de656 | -10.22213 | -59.41242 | 2025-07-26 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65700d03-0ba2-364a-a5e3-826391c85f24 | -13.24146 | -51.13698 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0cab83b-4ddf-35b1-b9ce-60ea8fc128b1 | -16.64344 | -49.2104 | 2025-07-26 04:27:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97c47ec6-39c5-3321-a41f-e158af25f59c | -13.69946 | -45.67994 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d628184-cba6-3cb1-9989-b786eec95f2c | -14.29265 | -47.41842 | 2025-07-26 04:27:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39ecc82f-23d0-3ff4-97dc-f35b1a9ac595 | -18.24444 | -44.78254 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b3e30bb-80df-3414-98f9-d06743ae800e | -15.26269 | -47.13379 | 2025-07-26 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f05a0b97-2f85-3a42-bd5a-4adad99ad69e | -13.54245 | -43.56929 | 2025-07-26 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08a41fcc-f0c2-3e6b-9ee7-aa38378cdf18 | -19.24695 | -46.95358 | 2025-07-26 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9625165b-79e7-3a1c-b458-b0b29cd781b5 | -13.23647 | -40.59898 | 2025-07-26 04:27:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c29af5f7-87fc-3fb2-8532-f5e228a3035e | -11.32085 | -55.21365 | 2025-07-26 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5000e919-47aa-3532-a389-ad097a201543 | -15.05237 | -46.5089 | 2025-07-26 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a62a57f-983f-3208-8521-787959cce90d | -13.54633 | -43.56985 | 2025-07-26 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f2d83f5-a5d6-3c03-bce0-defb18603e57 | -12.77789 | -48.81602 | 2025-07-26 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 773e77f3-e30c-3075-9bf7-74260e9c1657 | -14.94294 | -46.95872 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c7b9d63b-c611-3b77-bf37-930a0cc2c579 | -14.9474 | -46.95206 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d05de37e-81fd-381d-89ba-3e942cc03ef7 | -13.69483 | -45.68726 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c86b663c-5177-3c52-8ed6-fbac54be74cb | -13.09339 | -47.3396 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c625d8e-f295-3f4d-9886-c4fdb8d3aded | -13.09725 | -47.33662 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60de522d-a0d6-3ebc-b19a-c9fd4fb2f63e | -13.22496 | -51.14709 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbcdabd6-e624-32ed-908f-77f469a01c6b | -13.10647 | -47.36337 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cbd04de-2191-34df-94e3-e2fe5ea9935e | -13.11419 | -47.35744 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31794b2-e42f-3888-b1f2-ae3749f02ee3 | -15.26212 | -47.13754 | 2025-07-26 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24888c88-7764-344e-9506-8ae159b53ba0 | -12.68921 | -46.99072 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f1bc4e7-60b7-3a9a-94d9-4c82f6fb6c12 | -18.51718 | -56.41865 | 2025-07-26 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c62e8799-3d38-3c66-b2b8-aace26364dda | -21.3446 | -56.45208 | 2025-07-26 04:29:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64870bd1-d257-3a43-a3a3-bf6d65e5c37a | -20.22794 | -50.90258 | 2025-07-26 04:29:00 | NOAA-20 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0e5143ae-3980-39a6-9c5f-de78a1e75f67 | -21.99707 | -57.61606 | 2025-07-26 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04bbac08-f97b-3f98-b1da-1bf5696cfa07 | -19.97301 | -48.43065 | 2025-07-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a9dd2dc-b511-3542-a8fa-e82feb18aee1 | -21.74135 | -52.08447 | 2025-07-26 04:29:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 59321981-4c19-363c-a6b3-954064163b39 | -18.22819 | -54.54542 | 2025-07-26 04:29:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed77bd9b-bacc-3945-842c-c18a54d11b5f | -19.01675 | -54.65731 | 2025-07-26 04:29:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1593fa3e-c426-3359-9566-0a9fab2dcc1d | -18.22749 | -54.54916 | 2025-07-26 04:29:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 339f678c-fb28-3d14-baeb-b8ae4b29030f | -21.99805 | -57.61131 | 2025-07-26 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 904f4b1c-af1b-36a6-b589-b511f6ab4c68 | -21.60609 | -57.5783 | 2025-07-26 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b2af275-febd-3881-85d5-8096a2e34555 | -22.04007 | -47.93281 | 2025-07-26 04:29:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c61591dd-14bc-3b1b-a485-4508bc9f51b2 | -22.00447 | -55.53005 | 2025-07-26 04:29:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16b58c12-d15d-35cb-b944-afff4edf70de | -20.21674 | -41.45414 | 2025-07-26 04:29:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9c35c86-c8ad-30c0-98b7-9db2c6fd49b0 | -20.32359 | -55.00681 | 2025-07-26 04:29:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c18b3ae-c388-3754-829a-a6e08afe260a | -21.57778 | -48.39494 | 2025-07-26 04:29:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4d9c008-dd9c-3abd-a025-9f24a08eb888 | -21.77601 | -52.74808 | 2025-07-26 04:29:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 605068b9-6e11-3dcc-8119-2cbb1e56b91d | -18.22344 | -54.54839 | 2025-07-26 04:29:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9adf8c03-b09e-39e4-9cfd-24bc383255a0 | -22.00047 | -55.5291 | 2025-07-26 04:29:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3bd513e-cf42-3eae-9dbe-e85ed7620968 | -23.89219 | -52.35453 | 2025-07-26 04:29:00 | NOAA-20 | PEABIRU | PARANÁ | Brasil | 4118808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2ab3153-a38b-357b-9a1e-4a4b65a2d0a0 | -20.62287 | -54.83949 | 2025-07-26 04:29:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abc25675-f201-34da-b40c-46b785bd75dd | -18.22415 | -54.54459 | 2025-07-26 04:29:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52efd863-abe5-30d6-8691-a68541537fdc | -21.63489 | -49.84274 | 2025-07-26 04:29:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df7ee4d3-3d36-3539-96dd-0d313d7346a5 | -23.38532 | -50.76032 | 2025-07-26 04:29:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4f3aef27-68b9-338a-b0d8-e05ade434b25 | -23.35099 | -51.78733 | 2025-07-26 04:29:00 | NOAA-20 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 55b7aa88-b09a-3a11-862b-515bb449cdbd | -20.62389 | -54.834 | 2025-07-26 04:29:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e827b1e-10f9-3a91-9cd8-335067b9a3e1 | -19.97023 | -48.42635 | 2025-07-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3972096-d21e-370e-9bc5-d6f7e2884a65 | -21.04939 | -46.37308 | 2025-07-26 04:29:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e06f7593-7c00-3db4-a674-2fe7bc552247 | -21.38972 | -48.67413 | 2025-07-26 04:29:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4aba1fdb-6cf4-3e87-82f5-ce64eadf6be8 | -19.97358 | -48.42691 | 2025-07-26 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f1232e7-9959-38f3-babb-c5fd039b45c2 | -20.0073 | -48.9387 | 2025-07-26 04:29:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be546514-892f-3536-948b-4170e6b5ad39 | -21.99252 | -57.61495 | 2025-07-26 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 92d9630b-feb0-35a7-8797-6875ef9958e4 | -20.64138 | -42.90634 | 2025-07-26 04:29:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90a1ca99-c547-3893-8a6a-e70bd890e02b | -21.99348 | -57.61029 | 2025-07-26 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 445001be-cc32-3cbd-b4a5-7de327b299e7 | -19.01073 | -55.77815 | 2025-07-26 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2bc286de-e12f-33bf-b57e-57d2df8b91a6 | -14.9333 | -46.9422 | 2025-07-26 04:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a44fc75b-a6f0-3478-8b41-df5db2216efc | -29.95099 | -51.61695 | 2025-07-26 04:32:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 5a89e9fe-8a7c-3588-be15-419f1e14273c | -29.00096 | -52.4317 | 2025-07-26 04:32:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 39d48be7-8c10-3224-af99-a0e37799ee49 | -30.12097 | -52.07719 | 2025-07-26 04:32:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| edbfe7d4-5212-35d7-91de-d6a4e58f2005 | -26.02237 | -48.97152 | 2025-07-26 04:32:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f04d4aa5-6e44-376e-a551-2c442d2a5b78 | -26.02122 | -48.9796 | 2025-07-26 04:32:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e400d331-ff49-34b3-9524-379dbd09fe39 | -9.363 | -40.3031 | 2025-07-26 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 07aef9fd-e199-3957-a826-5e543bd5e535 | -9.3626 | -40.328 | 2025-07-26 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.8 |
| ce1fbe96-4563-3339-b5c8-d21b1dcdd7da | -4.0382 | -42.5129 | 2025-07-26 04:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 53.2 |
| f0884a87-7f9b-39f5-8e7b-61ba602f1642 | -18.2442 | -44.7767 | 2025-07-26 04:50:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 771a184c-970d-3830-bc92-03312f0c61b3 | -9.363 | -40.3031 | 2025-07-26 04:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.2 |
| e40f7013-2efe-367d-bbd7-8b8d80445c18 | -18.2435 | -44.8008 | 2025-07-26 05:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 848f585b-9324-3249-ab58-b02cff82b6cf | -18.2442 | -44.7767 | 2025-07-26 05:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ea332094-290f-3792-91ee-d62d47945431 | -9.363 | -40.3031 | 2025-07-26 05:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 54c07e4f-79af-352c-b403-65fce01a5df5 | -18.2435 | -44.8008 | 2025-07-26 05:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 9151bfa0-c8c2-3c7f-bf9f-3030594576c9 | -18.2442 | -44.7767 | 2025-07-26 05:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| ba753006-b8d4-3e95-bd8c-2e753efe413e | -3.6589 | -48.44621 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cbdac59-f320-3b33-99e3-db09ab93eb57 | -3.05027 | -47.38453 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93f1452d-be15-3a85-911d-b4be83e24b22 | -4.07743 | -46.9019 | 2025-07-26 05:16:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce63244d-fc65-3e1c-9284-78ef840d207f | -2.99052 | -49.31964 | 2025-07-26 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e90bb74-c3f6-37a5-931c-db2f920a9990 | -3.12439 | -47.01293 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 941b7eab-fc40-370f-9c0e-3c55a42ed27e | -3.58349 | -47.52785 | 2025-07-26 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc1893d5-2055-3a23-9dd6-98a47a91e339 | -3.31423 | -48.71661 | 2025-07-26 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8378b89b-4958-3bc0-a6c8-c65ba0d13f76 | -6.57185 | -49.50019 | 2025-07-26 05:16:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
