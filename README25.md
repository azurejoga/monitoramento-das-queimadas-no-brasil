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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8417f3a7-eb1a-3dd1-872b-81b4d2a5ca1f | -9.58309 | -60.51719 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a478e8c7-cb25-3d90-a66b-8ba40c2fc7ee | -6.31194 | -57.75156 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2357af1-cc49-3ead-b20f-c43f392debd9 | -10.04825 | -53.75984 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fa7b6a6-d9ab-3270-9a4c-6bc21b195b4c | -11.18141 | -51.36594 | 2026-09-25 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91b8d40d-dba8-3d97-9ea2-69c001e59091 | -12.23633 | -50.77655 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2420903b-1fed-3060-b404-15900a870b53 | -5.34797 | -49.03745 | 2026-09-25 04:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c02352-96ff-38aa-9446-8e41a1829d21 | -12.2242 | -50.74568 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fc4b868-df01-3349-9997-50f55fbb6b04 | -12.21754 | -50.78794 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a553ccf1-e165-329a-8634-af41012e779d | -9.40938 | -44.53198 | 2026-09-25 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf73c7fe-d997-363d-9253-d68afd6e2957 | -9.87798 | -48.31731 | 2026-09-25 04:46:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ce1dbdb-36b8-31bf-a911-6411ba2dcfcd | -9.00451 | -49.62619 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3f54449-a390-361f-89cd-a75a3ebdfc9b | -10.56203 | -59.49132 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61b73593-1452-3295-b29e-cc9649d00713 | -12.21921 | -50.77738 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e888dbff-f45c-3339-80b6-9c7feed22e6a | -12.21976 | -50.77386 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6860c8e8-64b3-36b9-9021-f3c4607f8b3a | -12.20375 | -50.76764 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 947a0a66-48eb-3c39-9a9b-7cdb83abf87a | -12.20651 | -50.7717 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5030dec4-bef0-3a2e-88c9-815d5d63e85a | -6.67731 | -55.08738 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0577bea-1dc5-3aa8-b9e1-d532308e03f3 | -10.05187 | -53.76048 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05475e62-385c-3713-a845-48f26f8f8209 | -12.2358 | -50.73673 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd12992e-f49b-3c39-be0b-2f8360a16758 | -9.19993 | -60.86808 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53aff60b-945d-35c7-a544-ce4b87a24732 | -10.89801 | -53.9477 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07264ea6-7d8e-381f-8f1c-08b40b95772d | -12.20156 | -50.73838 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02ed22ee-76ed-31ca-86d7-18e39f1e9f28 | -12.22751 | -50.74622 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58411bd7-41d0-332f-8e2e-3f93d67316eb | -12.19603 | -50.75193 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5382b306-e8b2-3625-ad9b-1500ca8c8536 | -9.00841 | -49.64476 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 274d51d6-d55b-3283-9181-f63a20ff4161 | -12.2148 | -50.76221 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 404c3de5-a78b-3684-872e-0a0d3a157f17 | -12.21535 | -50.75869 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a1698408-70ce-30ba-a029-0490f8e55717 | -7.12528 | -41.72623 | 2026-09-25 04:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a26057e7-b809-3f1a-bb52-e0db52e9dd33 | -12.23355 | -50.79416 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ce37293-1e1f-3633-aee8-bae785366efe | -12.19822 | -50.78118 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 770959eb-4779-346c-a50b-4b896a5cdaa2 | -10.28681 | -49.95884 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8795dd7-e418-3388-b8f6-28c249efda25 | -10.89802 | -53.92593 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59ec5671-3c4c-3e6f-aa0e-414b4d9a035a | -10.55738 | -59.49337 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c422bba-507b-33ff-a860-feafa3128d17 | -12.19324 | -50.7912 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 25d096c6-bb83-334f-ba78-d55fe8ed5304 | -10.42674 | -53.78161 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79a99540-49fa-3146-a935-344d6215baf4 | -9.14913 | -59.47878 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 550ffbd5-6861-3263-9cff-8b7513741c63 | -9.63065 | -43.95964 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 92d7698d-ffab-3e00-a757-3eb5e2f63a49 | -7.16563 | -45.04124 | 2026-09-25 04:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40d343d1-19f0-3d29-ade5-57facfe01a6a | -12.21092 | -50.78686 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee429952-57db-39a1-bb78-c9aa158d79db | -12.20597 | -50.75355 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25465059-9005-3bd6-a5fd-f8cb9ce64efa | -11.28811 | -51.29285 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a1d3d51-cf0c-3f5a-a30c-2aeff753816b | -12.17833 | -50.7996 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 90508990-6819-3edd-bb31-3561701a243c | -12.20652 | -50.75003 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb76ba50-2bad-393f-8d9c-35306d47596a | -5.83712 | -47.75398 | 2026-09-25 04:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06d78f6b-260e-3ebb-82d5-35c60075cc44 | -9.01173 | -49.64529 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 910b6ddf-b652-370e-a874-751501cd7ac9 | -12.217 | -50.7698 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c6999bfd-584a-3862-ac9c-5c85c9ace8aa | -11.27865 | -51.30939 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 280f5809-5a99-30e7-94f0-00fd550495cb | -12.22033 | -50.74866 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 95591e0d-54ea-3caf-934c-6c9eb0159409 | -6.68147 | -55.04693 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd3bab07-2ca2-3291-8ec0-49d7811305de | -10.94515 | -43.8812 | 2026-09-25 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a1d7fd6-b8ca-3947-993c-11d3ff7f07c0 | -8.32354 | -44.13068 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcc3d288-85d3-30a9-88c2-6de13dff5c36 | -10.90017 | -53.95683 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cd595f6-9892-3b55-b78f-858c8021f752 | -10.29345 | -49.95989 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f744c1f-513d-3065-8e83-3265221d7ae7 | -9.15928 | -59.47371 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 544ac1a9-a7cc-3ab3-b0ef-5027e1355a27 | -10.9038 | -53.95743 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aaab083-dd17-3e4d-8985-2180ea590fa4 | -11.29087 | -51.29692 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9c34ce-a3f0-322a-89c1-36c03fc45ef9 | -12.2225 | -50.79958 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 431e44ba-c6bc-3160-8bf3-ebc0c491ae3d | -12.22475 | -50.74215 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f4babeb-bb9f-3746-9c06-c9da9fb4b0d9 | -11.71108 | -50.55451 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| acd6ab55-95ca-371c-9a7f-53da8c297f83 | -6.67894 | -55.0535 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8ac1be6-30f0-3e80-896b-7580f29d237c | -12.21093 | -50.7652 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5283c5fe-bd8e-3b6d-ab83-4c0d39156dd6 | -11.18417 | -51.37002 | 2026-09-25 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2ad3e5f-8bac-3e45-9a4a-9a7493efd494 | -12.22307 | -50.77439 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 07cb3053-6e9a-3417-9d53-62a2d755f301 | -10.90309 | -53.93982 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 419d5b73-2081-323b-a4f8-1a83ac2239d1 | -11.15903 | -50.65224 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fd1792c-9d0a-3120-87c3-1d560e80e2df | -7.16167 | -45.04063 | 2026-09-25 04:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69fb2c94-cfee-3302-9505-3283dd00f1a6 | -12.22143 | -50.76329 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 535a9656-a266-3ecd-8475-890d8fd768f2 | -12.22805 | -50.76437 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb11edbb-0c4d-3dc7-89bf-9ec8b5dc2446 | -12.21423 | -50.7874 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5723991f-a00c-3f0b-88ef-07b657d9d119 | -12.19934 | -50.75248 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fc33348-e38a-3813-b434-92cd5174d05c | -12.21865 | -50.7809 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6d2f790c-947d-3261-8717-6d7d3a3815e9 | -9.29359 | -45.92255 | 2026-09-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17a4fd93-3ebe-32a7-9b27-3a566b4550bb | -12.23525 | -50.74025 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a58f6fec-ef27-317c-ad71-f234130616ac | -8.60731 | -55.21247 | 2026-09-25 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee50b7d8-f726-376d-92c9-7f5bd15cf06b | -10.90019 | -53.93498 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d76f7c70-7624-3aeb-96e2-aae12ec22094 | -12.20763 | -50.74298 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2602f010-38b1-319c-a128-2ccaa3846014 | -9.63005 | -43.964 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 6fca550a-9191-3e5f-91a9-d049aae37970 | -10.28459 | -49.95127 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4115bdda-6e81-3b00-9106-625c8cfcbab6 | -12.20266 | -50.75301 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7876ff89-c8d4-3833-aacc-148da8540fb7 | -10.61068 | -54.00305 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4431707b-204b-3c94-a10b-648d5e705f73 | -10.28791 | -49.9518 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15433935-9dc5-34c4-a85a-72b196546c8a | -12.21038 | -50.76872 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eca24638-4a1d-37b9-9bdd-3072659e5d0f | -11.28148 | -51.29176 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 709d4c8a-2133-3315-9546-06aadf012dd1 | -10.41163 | -53.80503 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf29a5b0-c8ad-3c5b-ae95-807d37730cf9 | -12.18554 | -50.75384 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5cf7b048-74c9-3c31-a5af-2944ac8d8475 | -12.22859 | -50.78252 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 365b7a48-8a85-3e26-87f6-0ad22b04b674 | -11.29039 | -54.04177 | 2026-09-25 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe563138-e34f-3950-8f7d-4d8b25cea150 | -9.17863 | -58.06909 | 2026-09-25 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80bfe165-eda9-3e9b-b226-eaa23c402bf2 | -11.28868 | -51.28933 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d64a6f12-ff7d-34bc-bb79-b69d0588b7a4 | -9.25959 | -46.25753 | 2026-09-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0226d387-c628-3827-8c6a-8c304edfa740 | -12.22581 | -50.80012 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c68a8d9-a234-3649-91c1-843dcc62bea8 | -12.21039 | -50.74704 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4f5f4cc-8d13-3fc9-8a92-837c7965e339 | -10.23655 | -44.62783 | 2026-09-25 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efa3813c-4013-350f-9666-67c4065028d1 | -8.32921 | -44.15223 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a7758932-0331-32e3-91ce-c75ea5236c20 | -10.90452 | -53.95319 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 134f97f3-099c-3d0b-8a93-03249b106337 | -9.14974 | -59.4754 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d99b3e21-64b8-3a6a-bb70-1671fd246a81 | -9.62623 | -43.95904 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 5dbf4a3b-cfc6-3ee2-8eea-0461911ea59b | -6.65063 | -55.07986 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89988be1-6af8-3f15-a34b-7bf0d3537b5e | -10.61942 | -53.99569 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8d0b635-d9bf-38cb-86c6-2b4d6dfdd317 | -12.20431 | -50.76412 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README26.md)
