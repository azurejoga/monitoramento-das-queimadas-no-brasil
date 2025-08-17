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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c80023f-9a18-3a6e-be59-c69a7f35c7a3 | -7.02113 | -44.28107 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15e9d6d5-f0a5-37ce-9d54-9ea6bb426702 | -10.31069 | -54.15773 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 62a807a6-3b04-3ba9-a925-a174331374dd | -6.61603 | -43.87887 | 2025-08-17 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e9c45d8-6193-3e99-b209-1328eef5b55b | -8.70516 | -49.40958 | 2025-08-17 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31464eed-7b9e-342f-a69d-c7ed9271af4f | -12.619 | -46.90729 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b19b173-0d6c-38f0-b66f-66d2110c3984 | -9.61469 | -40.34628 | 2025-08-17 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b0508116-c9d3-36a2-b9d0-b224b2be192b | -8.79704 | -52.07238 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f38c6140-4e30-3eb6-a24a-3b70b15f2a6b | -12.55742 | -46.9454 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef2e0816-a73d-35e4-a2fa-14666e242191 | -10.31427 | -54.15865 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8bd89d87-985b-383f-b16e-2c570677adfa | -13.10363 | -49.2015 | 2025-08-17 04:14:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b12110e-a213-33fe-aa67-b2ae12ffe49b | -9.277 | -44.55701 | 2025-08-17 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 620df325-7e50-3132-ac47-3344d1dc8a03 | -12.55456 | -46.94117 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3aff507f-52f2-3af9-a633-5643c0331a7d | -12.86184 | -46.05521 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ff13e05-17d9-327a-b4c9-2c8f5aa9c911 | -10.83846 | -45.33129 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 381f46e7-8d71-3b6f-b132-f6695b8dc7eb | -10.96773 | -49.5694 | 2025-08-17 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c091a38-1d64-3ecb-ac26-b429c2d30182 | -7.12304 | -41.3979 | 2025-08-17 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6e66793-e43b-3f17-b1d8-d539d895c1b4 | -11.36062 | -55.39313 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ab162898-3d93-3428-9c3e-610f540ca13e | -9.86524 | -48.31701 | 2025-08-17 04:14:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd5f9efe-f961-335d-b967-2a0791df99ee | -7.41835 | -42.03008 | 2025-08-17 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2d86f85-7424-31e3-959c-0311f3770ecf | -12.19437 | -47.23274 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb29d1b4-2eb5-3253-83d9-fb528df68dee | -10.30513 | -52.56078 | 2025-08-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d904c6d8-8be2-35d1-a40c-82d580c4b47d | -8.51135 | -44.73385 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 061e7f15-b8f1-3e17-bda2-888a2c06793c | -12.14048 | -47.9173 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c179105b-f639-39d3-a161-ee75ae0a005a | -12.55395 | -46.94484 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c954d39-a067-334d-b070-ff7660f080d7 | -12.82529 | -45.99287 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff930205-a07b-3abe-a6d0-e239354ad476 | -6.19042 | -45.44531 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deaae41f-7942-3098-a4dc-fb9c3be8fe24 | -10.85069 | -45.34069 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1c6a4ca-a2b1-3e93-b5cb-93e4486ce1da | -8.3063 | -55.09949 | 2025-08-17 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65818fc0-811d-3d89-8fb6-c27cde6cafd6 | -9.10338 | -44.70941 | 2025-08-17 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e97e3f7-d019-3a89-b196-887c09928adc | -12.44996 | -46.98042 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 420ee121-55c1-32bd-886e-4f040f387de5 | -11.42342 | -52.21994 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 723db4e3-64c2-3018-91d5-a9a94f85a668 | -8.79598 | -52.07823 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 45ec7c04-25e2-39dd-9fad-4578fcee8f5f | -7.42227 | -42.02702 | 2025-08-17 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 233182ee-bd57-3234-a7af-23490d31a0a9 | -6.54356 | -43.026 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8cd5bbbc-3cab-396d-bed4-8baff32252db | -10.84213 | -45.37249 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37f1c88f-f536-3e56-aaa9-06e8a2310028 | -13.60666 | -47.74309 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 725c892e-5c55-3185-88ae-7d999e194043 | -13.60747 | -47.78176 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77088b34-04d8-3610-a099-81a5ade07354 | -19.93584 | -47.08105 | 2025-08-17 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16f8dce7-d014-3f86-9de0-aef0ee92054e | -15.14851 | -48.75962 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f66c9073-5724-3dd1-88ff-7b45870cb147 | -19.30011 | -46.21011 | 2025-08-17 04:17:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09a78f70-578f-38f5-9525-1c32535e5029 | -14.54497 | -52.03666 | 2025-08-17 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31841d4e-1bc7-3bd7-a5f6-74a5477e1ea0 | -13.58225 | -46.98396 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 271b464b-5b69-3af5-9675-635cda66c273 | -15.17406 | -48.76464 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6db81fe7-bee4-34b0-abe4-a934e84dc8ff | -18.62411 | -40.00576 | 2025-08-17 04:17:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 94cf5c71-2c41-303c-8a92-958f1d75b84b | -15.5248 | -42.33279 | 2025-08-17 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28c3da91-da81-394f-a17c-c6163b607f48 | -15.6233 | -47.63324 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13ff2c3f-4adf-366f-b658-87b57a9093a9 | -14.68567 | -49.0041 | 2025-08-17 04:17:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10502079-5b7f-3643-9556-70194a2ff106 | -14.96091 | -54.76236 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a60058b-ab12-3252-8d83-48d71da77b96 | -13.65905 | -53.70393 | 2025-08-17 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2bef26a-1c61-3a7a-9256-331f92d38154 | -14.95303 | -54.75988 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52c4c31e-5185-39fa-9253-6c1fa130c05e | -13.63007 | -46.909 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55096a5e-f642-3ef1-8841-c616452b89a9 | -21.65143 | -44.078 | 2025-08-17 04:17:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d864f258-f9fc-3912-9e41-dc5850e42e13 | -14.95839 | -54.76091 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5215820-81f1-3540-9e34-510cddf118e6 | -16.62661 | -51.36707 | 2025-08-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c41f5efe-b391-3dda-833f-a2b48f266fd3 | -14.19568 | -45.32936 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4f2b01b-cfad-37f3-8182-313ef76496a4 | -19.72361 | -46.47432 | 2025-08-17 04:17:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7eb94804-5a2c-30ce-94ee-d74693233568 | -14.96168 | -54.75859 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcd97a15-f9f4-3691-9cbd-2ac82dc0e8a8 | -24.15916 | -52.90166 | 2025-08-17 04:17:00 | NOAA-20 | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a75daeb4-c271-3fb6-b102-f5689f4241c8 | -14.18356 | -45.32006 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c8df880-a295-3e23-be6c-b27ada078461 | -13.87576 | -45.54698 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1968b227-8106-364b-bb52-2290a4fc5015 | -16.03685 | -52.34984 | 2025-08-17 04:17:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 416a3d1a-ca18-3203-bb31-3cb988a0c5b0 | -14.18518 | -45.33126 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ca6aa32-477e-3590-b2bf-9e5a25c56c85 | -15.11559 | -48.75359 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a90f3de-887f-3332-80d9-94b554135b53 | -13.87908 | -45.54754 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b11c2bd-700f-35f4-bcba-4b706fb7f841 | -14.97129 | -54.75186 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4f81965-bbe6-312f-b38f-599e0196790a | -16.64225 | -49.15392 | 2025-08-17 04:17:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ef41c0f-7643-39b2-b2cf-32aa555eb716 | -14.1918 | -45.33237 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de83b521-c7c0-3e53-bb18-5d510cd2e01c | -19.60951 | -47.03865 | 2025-08-17 04:17:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f34e88ed-cf02-312e-91e7-da9b6cdc178b | -14.18413 | -45.31652 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61d2838e-8f02-3f28-a2b6-403ee0c985be | -15.17482 | -48.76024 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f9dd707-6ea8-3050-a214-0172b39e100e | -13.59045 | -46.97725 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 771ab33e-a322-3adb-90a6-6e530df82215 | -17.48888 | -45.85272 | 2025-08-17 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a09ad0d-bcb5-36c4-813a-1416b7485c58 | -21.57192 | -45.09281 | 2025-08-17 04:17:00 | NOAA-20 | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b3057575-7169-3258-839d-f34625713686 | -15.64457 | -48.13618 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f512ebc-5149-3419-bbdd-3d4bb1238765 | -17.97077 | -42.98399 | 2025-08-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e683cdb9-f35f-378f-9ac6-7cae234acef3 | -14.93258 | -47.05581 | 2025-08-17 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43d7097f-0ab9-3939-a03a-91febc4013b2 | -17.41322 | -48.11031 | 2025-08-17 04:17:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14718962-a6c1-324b-a168-96b8fd34b6d4 | -17.50191 | -44.19845 | 2025-08-17 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5a881a2-af99-3f92-92bd-0348c48da889 | -17.40769 | -48.12174 | 2025-08-17 04:17:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6bc0eb0-2407-3010-a154-969256d334b9 | -13.61873 | -47.75829 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cd6683b-4e8e-3d46-bd31-07bf3dfff8d8 | -17.97019 | -42.98807 | 2025-08-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f689b8b1-f016-3068-b834-55775a08ba75 | -14.98023 | -54.74951 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c79b7f10-9414-3eb7-a85b-236ccb6c3c48 | -14.59015 | -47.95333 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f640022-9800-3c1e-9205-ff9e8710bbb3 | -13.15849 | -55.71698 | 2025-08-17 04:17:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eee2f4ba-c4f8-3d44-b298-6b4b2e99d1ad | -13.59904 | -46.90458 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 11e2efae-6f5b-3e71-93b7-cb55abb737ac | -15.63682 | -48.13902 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb333589-3850-37fa-aed4-2d945acb60c5 | -15.14928 | -48.75516 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f581b64-0f59-3e58-88f1-fce43a266279 | -15.85761 | -50.19839 | 2025-08-17 04:17:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6bdba004-1e0b-36a7-8d13-dc18cd51b82e | -13.42253 | -57.03288 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84317f2f-7b7d-37e2-9790-44cfc4263790 | -19.3668 | -42.92539 | 2025-08-17 04:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 460f654a-d355-324a-ba3f-07559efcd954 | -20.28891 | -46.05253 | 2025-08-17 04:17:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8afa9c00-0eef-3da2-a6e2-dcf9009d421d | -13.57882 | -46.98333 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95384a77-409d-3295-bec9-f2449ccbd796 | -14.93878 | -47.06082 | 2025-08-17 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60cfd8a2-0868-3cdf-abe8-cb6ff0d0d4ef | -14.96374 | -54.762 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8fda87e-d21f-3a00-9a3e-48defceead80 | -19.16348 | -46.5797 | 2025-08-17 04:17:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 831685ec-598b-3439-9272-f9cb08e916a3 | -15.7826 | -48.26223 | 2025-08-17 04:17:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85bbd764-0500-358c-907c-0fbfb56a6975 | -16.04132 | -52.3508 | 2025-08-17 04:17:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3735d593-8727-3537-9e88-398ff956c35c | -15.64388 | -48.14032 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 988a2960-00c1-3e63-946e-df5bae6a3cc5 | -14.97933 | -54.75395 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59929e6f-aa2c-3402-bd1a-2b05f3787a5f | -13.60659 | -46.90164 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README21.md)
