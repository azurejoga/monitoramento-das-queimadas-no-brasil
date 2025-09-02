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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26d2af0e-ef77-3173-9a5d-d5c2793348e2 | -5.31796 | -55.99753 | 2025-09-02 05:31:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f07367ff-2f6c-388c-aab8-96a9e010ef8f | -7.56139 | -63.07309 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d15e432-f0cc-3891-a22b-eadedaf92d63 | -8.6577 | -62.60616 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3849371d-8e38-3d82-ba9c-2be976593b6a | -11.66034 | -52.19793 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d5d2a7c1-0fac-36f4-8edc-7adb6ac87e1e | -11.65932 | -52.19205 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f95aee15-a151-3b15-8ac1-43cf0d1ab33f | -6.78708 | -52.81336 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3bc307e3-b91e-359a-b5cb-93592a807a43 | -7.5479 | -61.33592 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c2a15179-1c0f-326f-94d0-e4d7bc76e968 | -7.70652 | -61.10104 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c83e297-8f6e-3be9-8cc1-7e4c4be3544f | -8.69017 | -62.40026 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c17ce6d9-0aef-37c5-aa0b-955542f344b5 | -9.54532 | -65.94944 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 394a545e-d8c4-3365-9754-d330c40884a4 | -9.45128 | -60.57314 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40512584-3f57-31b5-9a2c-8718dd0d1273 | -11.6769 | -52.19886 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 14b19d2f-d6db-36ac-94f3-7da8752acc41 | -11.66689 | -52.19434 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8205b711-ee38-38b0-aa62-44658138ac67 | -11.67688 | -52.21384 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| fbbb68e1-042b-33f9-8783-8d5976adc0a7 | -9.20182 | -60.25107 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9693349e-a5b6-3b9c-b17f-438f4f2c2c97 | -6.81375 | -52.82059 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41e1cdbc-260c-3424-bad2-6365a1623a9b | -10.39183 | -59.41447 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e39f3168-d651-3426-a338-52511eacdb43 | -11.42482 | -55.18492 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e30a53cd-13c3-33cd-bce7-9baa7ab973a7 | -8.61709 | -69.49885 | 2025-09-02 05:31:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ec3d7fc-2d52-3134-89b5-cab018028241 | -11.66137 | -52.189 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5a4ac8b1-f32e-319b-bc6c-837871484180 | -8.6584 | -62.925 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31e3c0f1-b533-3a9d-ab3d-7d90ac49486d | -6.82953 | -59.68143 | 2025-09-02 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6de0be6f-125e-3722-9c01-d9f11f4691cd | -6.33896 | -58.17673 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf791859-6605-3b67-9a89-8bcfb54e3836 | -7.27942 | -60.65796 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09ace0bd-92f4-3c6d-bcbb-bace00aa769f | -11.6588 | -52.21125 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 93bcfb0d-c8a8-3083-8a14-635fa9dafff6 | -6.83059 | -52.8191 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b883b26-3e0d-365c-8197-788299bae454 | -6.33588 | -58.17163 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b644503-4d45-30a5-bc72-d72149cb943d | -7.66604 | -61.09472 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43c49b86-2316-34ac-aa86-893ea02f759a | -9.26281 | -59.75761 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5de984ac-fc16-3494-bda1-c9ed5bd80d3f | -6.83112 | -52.82175 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bd701d2-47cc-354b-8091-fa4ad94782de | -6.83298 | -52.808 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dba32d7-96bd-316e-8c33-9019c33e972c | -11.67746 | -52.19433 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a167953c-a5c7-318d-89e7-3a25ba64aa0c | -7.11073 | -63.01899 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bda4b771-9ea6-3397-b75e-f49dec9eb486 | -7.70033 | -61.09639 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db446ead-2e07-3d63-829e-444d602fc307 | -8.44578 | -70.13845 | 2025-09-02 05:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 473eebf2-e7d6-3401-b9dd-caaf9905da19 | -6.82522 | -52.82444 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2645f94b-0a2f-30e9-8a65-17e572ef0892 | -8.6179 | -69.49417 | 2025-09-02 05:31:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30db3546-be55-34b8-a3fc-134277905761 | -9.68069 | -56.73796 | 2025-09-02 05:31:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcf0c3a0-a45c-3762-be22-218223455d9f | -11.65769 | -52.20536 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 083e6942-e679-38a5-a8e0-b08cbc5f22d7 | -6.19473 | -53.76155 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1355bd5-6a3f-3abe-9b9f-1cc2ea3a6588 | -11.66929 | -52.2264 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 207b0147-8c95-3640-a911-303fb8320297 | -6.79701 | -52.8215 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f69cb413-ff2c-369f-9e7b-0b7c4eb82ec5 | -11.67412 | -52.22127 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 32eefb1a-c1ec-390d-b720-33e91ccc2ef9 | -11.67196 | -52.18915 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e32915e5-12eb-3e93-a3b1-3e693c00d958 | -11.65878 | -52.1965 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 650e5e45-3810-3935-a7cf-86a139268bf5 | -9.26342 | -59.75356 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a1f0b8c-5809-3bbe-a8aa-4e933f1be7fc | -6.82336 | -52.83817 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c9b34a3-4435-31a7-b48b-3c5afdb196c3 | -7.69676 | -50.27015 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8eaf0a0b-3e1d-3404-b21f-e7668d39044f | -7.50805 | -63.49011 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e511a9d2-7649-3dc5-82a9-f3a632d5cc43 | -9.20742 | -59.53649 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1753430-4f42-38b8-8037-30f5c9b7ec6b | -7.5462 | -61.32475 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 984eecb7-d1af-39e7-a42c-3fcf5350b7c2 | -8.50892 | -63.91243 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 488d5db7-6d2e-36fc-86ae-d4e1e070d417 | -8.71457 | -62.41846 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35f168c5-0f1d-3241-9229-cd55537c8c11 | -8.68684 | -62.39973 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 128c75ab-2fe8-3d15-80ce-4ca03c511e0a | -6.54048 | -56.20254 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55c3c73d-9887-3be0-bf6c-ecdd6ba964f4 | -9.74013 | -48.97 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2082caab-a726-38af-aec4-67e05e967d56 | -6.22615 | -53.57606 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39484328-3463-33e7-9738-036d8795cb36 | -7.28056 | -60.65063 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1e10657-3608-3242-929e-89b2012c8b07 | -10.89527 | -50.8379 | 2025-09-02 05:31:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21bfcd41-7013-393b-9714-23b57b887ba0 | -7.67279 | -61.09578 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cf1031f-e282-3a44-89f8-e197aa9383d2 | -8.7057 | -62.40989 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 793cf6e3-e997-363e-aff2-56e0755242f9 | -8.6667 | -62.851 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3614612-3e0d-3798-a6a0-8bfd7f3f59ca | -7.69303 | -61.09893 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f87647e-2e30-3f5b-9f79-ae3a8357cc5e | -7.53862 | -63.83961 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca31b92e-971d-3f65-8233-dda1d27b3882 | -7.54174 | -61.33133 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d63b3318-c002-3b62-84b6-bf2d06b842be | -8.65437 | -62.60563 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee678cfa-45f4-3458-9c97-100cd8b0ed62 | -11.66042 | -52.18311 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d60ea0bc-aafd-3c98-a381-f8acd7014474 | -11.67033 | -52.21751 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2ba10d66-4de2-3f2f-8e35-dd16ff467da3 | -11.67505 | -52.17689 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 31c0d631-f53e-38fe-81f8-951ba4d406eb | -6.85702 | -52.79448 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cc22ee5-5c86-33e8-8a18-a17e96957343 | -7.78966 | -61.5689 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ea4f44c-9c2d-3628-aa61-f705073364eb | -9.54965 | -65.94582 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 816293bf-6ef3-3472-b64e-a3c4c07374f8 | -11.81787 | -51.54669 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80972cfd-1e20-3a76-9eb3-5080079acb03 | -8.72843 | -62.41708 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41abb136-6dd7-3165-97f7-dbcdcac244aa | -6.80291 | -52.81892 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afe017b5-2e88-3d99-b3b8-87297f25f3f0 | -3.72747 | -58.84084 | 2025-09-02 05:31:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4669eba9-a2d9-321c-bca2-28c232a7b83d | -9.27683 | -59.74556 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f77c547a-90c9-346e-b939-b1e498ee42c7 | -11.67532 | -52.22722 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 8403555d-27f5-31e2-82c8-1e66a737cd44 | -8.96765 | -65.96399 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f22f9051-9169-3d25-9dd2-ca299069fc8f | -8.66173 | -62.92554 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba3b0bf-2e9b-3c2e-93b4-f94e1c8c0726 | -11.65432 | -52.19696 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 79bbae82-ecb9-3bbd-82bc-357977219d83 | -6.85517 | -52.80796 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96e0de4f-52bd-3a3d-abcf-5d1d256aaaab | -6.78212 | -52.8092 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0491b5a7-ef75-37d2-868d-4194a5e6bde5 | -8.97058 | -65.96886 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5456aff1-02ac-3a26-8030-fc103a4edca0 | -8.68074 | -62.39518 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76fb9d72-d17e-3780-be5b-3cb4b6b92a3e | -8.67354 | -62.39762 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bc14f56-b998-37f3-8e9a-d22079143e24 | -8.65715 | -62.60965 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce9d7580-9ae1-30f2-9c23-082ba0049f33 | -7.70214 | -50.28278 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fee6cb55-c00d-3c7f-899b-73b6336c950b | -9.73399 | -48.98838 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc661a32-c7fd-33dc-ae78-ffe5b5c86fa1 | -8.66004 | -62.82847 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3b1f31a-007f-328e-9948-00d8bbbf2658 | -9.44028 | -60.57539 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 979f996b-58f2-3185-9e31-025946ad3b2f | -7.54734 | -61.33946 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 972bd657-ced7-3de6-b22a-3b6262d53d65 | -6.34246 | -53.43143 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a544519-d6ed-3acd-85f1-bd08abd88e12 | -7.50748 | -63.49369 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d94a9af4-58a2-394f-b54e-ba1f84e12009 | -6.43735 | -55.61925 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebaaf0eb-f770-35c1-a327-80a0f7245809 | -6.82069 | -52.81697 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 609e474c-7e03-3533-b4a1-9c4d99efa369 | -8.72675 | -62.40608 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44f5fce1-350f-3f97-8fc5-e9e514fb9263 | -11.65605 | -52.16856 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37d8adf0-271e-37ba-91cd-6f0f09201763 | -6.35249 | -55.55989 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16cbc71b-b80e-3817-974e-4b498be6bf65 | -8.7179 | -62.41899 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README80.md)
