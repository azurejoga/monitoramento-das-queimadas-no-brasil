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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a093f176-10eb-3df1-90c7-a05b41e28223 | -11.20187 | -48.99646 | 2025-07-04 04:40:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acaa30ed-4317-3cf5-8ece-88c7adc30bdd | -11.92607 | -45.38155 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65057ad0-10bc-3ac6-849d-c536580cfab6 | -10.05603 | -59.10674 | 2025-07-04 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d864b835-b8bd-34f9-abf1-a800b7e63c0f | -15.35431 | -49.2321 | 2025-07-04 04:40:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e5f0a79-e22f-3631-a85b-2d951ec09b3c | -11.92038 | -45.39223 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1479b7e2-760b-3118-8dea-770ace4e7fdc | -18.03561 | -46.05043 | 2025-07-04 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a44c28bf-6259-360b-bd1a-8deeb73bb1a0 | -10.34223 | -47.29149 | 2025-07-04 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0d7fe02-5a1a-3bd6-b740-38c0f46a6c66 | -11.93019 | -45.38211 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f38b6401-2254-3e52-a378-46a633f95176 | -11.92449 | -45.39287 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bad86db-5c47-30a2-bea7-1e773b3de4a6 | -11.51223 | -48.45345 | 2025-07-04 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e1bb4ba-2a9d-3380-8c1c-d493d7a69d7c | -10.9821 | -45.10193 | 2025-07-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 830cb548-186f-3359-908b-2177fbc531bb | -11.92808 | -45.39722 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95b967e5-fac1-37c6-82d5-5483ac1b2c85 | -11.5468 | -47.86329 | 2025-07-04 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05c283f4-d95c-353c-ac0b-7fc18125fd62 | -11.44953 | -45.11643 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bb427aeb-b0d7-3da6-9523-a80afd47ad2c | -13.24064 | -49.83862 | 2025-07-04 04:40:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fba0eaa-b8d6-3ed4-8964-6a8660b18002 | -11.54619 | -47.86738 | 2025-07-04 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dd8a786-5119-3fa6-b335-681956aadd3e | -10.89425 | -56.45366 | 2025-07-04 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77758daa-7072-370d-8dc6-94873fa56298 | -12.57962 | -56.97574 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a528f881-6123-3a88-931d-4919ce94e918 | -11.87419 | -58.7333 | 2025-07-04 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09a78fc9-e670-30b1-b529-9bf7889af641 | -11.48454 | -48.44921 | 2025-07-04 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e702b144-f2c9-3b95-b654-273a81d1bc52 | -12.57346 | -48.88467 | 2025-07-04 04:40:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c317770-298f-345f-a848-422bdfde03e5 | -11.01653 | -56.25609 | 2025-07-04 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c0dceaf-0704-3c43-991b-fe9686d7798f | -11.54265 | -47.86682 | 2025-07-04 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3a984f2-0276-3571-bc66-b675aacdbf2a | -12.10276 | -54.5887 | 2025-07-04 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0138a23-9666-3fae-b5b3-ab71e3198cf7 | -13.38832 | -47.83286 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61880693-f72d-34b3-9d67-3203810eefde | -12.16256 | -45.52743 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27880478-4297-3b59-a5e9-d7a9fb69f677 | -11.91578 | -45.39517 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36d5feb4-a096-37eb-8280-06ecce9faf0f | -13.23668 | -48.03109 | 2025-07-04 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ae8a81-1131-38af-aa90-d619412f7573 | -11.46481 | -47.30091 | 2025-07-04 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e87f0b4a-2171-3f89-b2c1-44ad78591b5a | -10.25721 | -48.14465 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e96336b8-3088-3025-8981-cb8150bd6511 | -11.44899 | -45.12026 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 71e223e3-e4bd-3ff7-9e03-ee4a6b2725e3 | -11.92502 | -45.38911 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 654452e1-441c-3ed5-9bc5-81349f05c844 | -10.5554 | -49.13313 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 709f9cce-3389-364d-9437-b71450580493 | -11.44591 | -45.11201 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bde619e7-3b27-36cb-8c8a-b4a503f9665a | -16.39727 | -51.54935 | 2025-07-04 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a523b3b-5a45-388a-b8e0-7e8ccab8e9cf | -10.24539 | -47.67543 | 2025-07-04 04:40:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e71f0b5b-3fc7-3845-b121-05df7e98eb1e | -10.25951 | -48.14456 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c24d2dcf-5997-3c68-90b7-19cd56e70bef | -11.02072 | -56.25672 | 2025-07-04 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8622dda2-5928-361c-b648-67b669b03b9a | -10.9603 | -48.37659 | 2025-07-04 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 898e3738-7264-3d6f-85ac-b2ae35b6afec | -13.38892 | -47.82868 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3683e81e-e1d7-3525-92bf-c4f079c97d0c | -10.98729 | -45.09505 | 2025-07-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e043a9c3-0bbd-328f-b3d9-85dc3f91d43c | -13.45697 | -46.72278 | 2025-07-04 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c740fa6-6e9f-3c35-9216-8da6adce2dce | -10.56213 | -49.13417 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c871e4d0-372e-3211-9474-1d1e54cdbc63 | -11.9163 | -45.39141 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4318b9eb-43d0-3599-bf00-a32e8198e706 | -11.93326 | -45.39022 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc6c5bc7-433d-336c-9ca9-1229495e395c | -12.5789 | -56.97978 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8b3de19-4a23-3951-bcc3-103ccee4b0a1 | -11.92554 | -45.38534 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1853327c-2ce4-303e-997b-400417743e15 | -16.60941 | -49.36703 | 2025-07-04 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fa80cd0-7a6b-3d2d-a521-810ca073dc86 | -11.93073 | -45.37826 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c19669f-e2d4-329c-80bf-3537e11c965f | -10.05284 | -59.10672 | 2025-07-04 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9591e45b-ea45-3255-bc6c-969a639a8c5f | -11.86959 | -44.85596 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dce0576a-9c2d-3a55-9821-8ed8b2c01bff | -11.77212 | -47.39531 | 2025-07-04 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5946d18-f6c2-374f-bef1-ccd20a578073 | -12.42747 | -43.72217 | 2025-07-04 04:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8c9e3be-2e3e-39cc-97f6-e45b5297ce76 | -11.49353 | -48.07772 | 2025-07-04 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c2fff09-e351-3851-a9f1-2ce926fec0e1 | -11.92143 | -45.38473 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2a8845f-962c-357b-89c0-aae5c67ba5a2 | -12.10646 | -54.58934 | 2025-07-04 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0b9d190-5860-3009-a113-773c9583d397 | -12.58034 | -56.97171 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a57ae303-78fc-37df-ab08-a8932ebdbe92 | -14.47925 | -46.35516 | 2025-07-04 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe0e5bc2-c356-3b6f-b2b0-4e9e9105d664 | -11.24455 | -44.889 | 2025-07-04 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23b3b342-9ddf-3be3-a20a-a27a968d28da | -10.24914 | -48.15116 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd07ba58-eab9-3fb2-add2-cb84512a5094 | -10.76199 | -48.2534 | 2025-07-04 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d15cc42-95fc-379d-bb25-16bd8f51b917 | -12.9397 | -47.13372 | 2025-07-04 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1702ef1-72b7-3d40-91a5-fb12e865f7e9 | -14.31326 | -54.65552 | 2025-07-04 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89b16632-56ef-30a4-a20e-3e46b548cd52 | -11.91882 | -45.40342 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f53c0a7b-4755-3a00-a12b-7a1423beb278 | -13.16323 | -53.25556 | 2025-07-04 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d3a897c-05af-3898-9d90-8712eb822466 | -11.24821 | -44.89357 | 2025-07-04 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 158056df-8c62-3296-b273-534947cb5ba8 | -10.26009 | -48.14903 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 031e82c6-23a6-3a5c-a2c0-6842e6335442 | -10.30545 | -57.13427 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cbe005e-a264-389d-ad9c-cb546862614d | -10.32682 | -49.93439 | 2025-07-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94a01ae8-ba92-3168-b737-b59134f24aa8 | -10.98106 | -45.10941 | 2025-07-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d31d852-2adc-322d-803e-a0659c61b017 | -11.52694 | -48.95536 | 2025-07-04 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a496591e-beb3-3fd7-810c-3a259f40513b | -11.93167 | -45.40155 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51269e25-0463-3386-ba66-fd0f6cccabbf | -11.54974 | -47.86793 | 2025-07-04 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d38c08a3-63ea-3312-80c3-db974fd7d188 | -10.59115 | -49.45872 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee7dd2fe-c2d6-305b-9d1c-bf6b0602b333 | -9.6333 | -63.50675 | 2025-07-04 04:40:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 388b2bb1-4da5-36a5-a875-04b90371544a | -14.87557 | -48.35763 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ab6fe0b-0087-33cb-8e8b-06f3730a6f31 | -10.98624 | -45.10255 | 2025-07-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 961814c8-cafe-37e4-9a49-d0a8c3537716 | -11.92716 | -45.37374 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7367368-aa26-3070-8a19-40b4f564be7a | -13.69547 | -47.74529 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a98cb471-e271-35bc-9019-aa088f9e79c0 | -17.86289 | -44.57263 | 2025-07-04 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6d4e503-653b-37fe-9e55-9e1658b7ba34 | -10.05034 | -59.1089 | 2025-07-04 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3db9b888-6308-3a14-a020-52ba34bd02b2 | -14.60854 | -48.24954 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49b59732-0307-3a15-abf4-f52f8dd56f44 | -10.24892 | -47.67594 | 2025-07-04 04:40:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5007dd78-7976-36eb-ae24-625f979a55fd | -11.46524 | -47.2996 | 2025-07-04 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1c7904c-d7e2-3d67-9c3b-da4a38d4ac07 | -14.37012 | -50.32864 | 2025-07-04 04:40:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 410317d6-dfc3-3cdc-9c26-8c6c697b092b | -11.86416 | -44.86395 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e16e8ccd-b177-3bdd-9a17-a7cfb1212544 | -11.48858 | -48.44588 | 2025-07-04 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e344042a-df12-3eec-90cf-6f108259e9c7 | -13.44956 | -47.81971 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cef5f34e-1cd1-32f8-af6a-b22247cbfffb | -11.46846 | -47.30145 | 2025-07-04 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f81b771-201c-33c3-b357-4f415b5a3209 | -13.43261 | -47.80866 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41722ee7-2cee-3352-9f57-6d324c38435b | -10.25259 | -48.15176 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b494f3c0-a930-3cfa-a22e-0d4fd9c3c95a | -11.473 | -47.92391 | 2025-07-04 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f27d43f8-9c5a-3c46-b0fd-29c04ce3d95f | -11.86361 | -44.86798 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b00c6e96-f6c4-3ed4-b428-0d1992ae4137 | -13.39922 | -47.83432 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1c54241-0be7-3b21-8336-aca715245678 | -11.488 | -48.44974 | 2025-07-04 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a966b97-86c6-39ce-99b5-d9c1b5ff8ee2 | -13.40226 | -47.83891 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a464aa11-938f-38a8-85fc-f84cb2dc5dd0 | -13.43625 | -47.80917 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0cecb6ec-544a-3fa4-825d-746c174329b5 | -11.93273 | -45.39398 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e683edb-0ada-3542-9f05-98ab5aa87b9c | -12.10723 | -54.58484 | 2025-07-04 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac63ec83-60ff-34d1-92fd-1ee87ff38c6b | -9.90732 | -55.52826 | 2025-07-04 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
