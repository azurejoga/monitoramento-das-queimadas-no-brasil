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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ed0a064-a14c-3a6f-bdde-7d67f14efca5 | -13.79244 | -47.93703 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43d25d0e-a9f5-31b8-a5e6-89c9827074e8 | -12.17536 | -43.56308 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be59917a-39a4-347b-85a9-fea42629c9f1 | -15.03592 | -46.97441 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56b397f0-f4b7-3eb2-ab5d-6c7eb66b7b25 | -14.57884 | -48.27286 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2522d0b-b114-31df-9c42-14783ba735b6 | -15.33506 | -47.91357 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd567fa2-c19d-36bd-8bd9-4188fede4583 | -15.87482 | -46.2199 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a4ce033-44c7-3058-ba6c-bf6e3baef77b | -10.71877 | -53.79892 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57b80e16-5f60-334b-b2f0-c008dfe268c3 | -15.71006 | -47.79827 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cb03087-1c40-3e46-813a-e1bc345ed76a | -13.74132 | -47.88772 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23591808-c78f-3926-b26d-3ae0678ac7d8 | -15.03032 | -46.9762 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c28f3614-cbf3-36d6-9f2f-f054a0561ba3 | -14.68074 | -48.15299 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 425a86b7-a71b-3438-92e5-ce0cf808ce55 | -16.50089 | -46.03566 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0533f64-06e5-32f1-a0cc-5c5a50e31694 | -16.5075 | -46.02853 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fabe34c0-02e5-3292-be14-696146a6f4b6 | -14.68498 | -48.15903 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb25681b-b318-3ba6-9ac8-d9464f58249a | -14.67946 | -48.16369 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 030f3ecd-6aa0-3857-a0f1-de83bf1f9e79 | -13.49563 | -47.40645 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3dece97-8afe-37a6-90a6-c9538b85236c | -12.66126 | -46.92553 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e69c05dc-2ea5-3617-bba2-acfe5838ad13 | -12.00755 | -46.62249 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bced20ac-f1ee-312d-a3c8-7b5de7fb697e | -12.99998 | -49.4425 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc131606-6800-3ebc-a5e5-05ee10a53891 | -11.99829 | -47.10899 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc26084e-0597-36ca-b36d-f6e9043c5e69 | -15.54371 | -47.87377 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40136a05-57d3-357d-b60e-38a0836bd21f | -11.93237 | -48.02951 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 14222583-1149-3cc7-bd6a-f1a383e1a3a6 | -16.27778 | -52.53989 | 2025-09-29 04:59:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7b6de33-82da-39db-9629-54b9832983f5 | -16.20607 | -52.82454 | 2025-09-29 04:59:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e08bdd23-47dd-3d4c-98e3-375b8138622a | -15.54774 | -47.88054 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79a24b13-5c0e-3d79-921a-07d9bed7fcb5 | -14.57337 | -48.27745 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb8cbbde-49c9-3a2a-9b8a-4135e6480bb4 | -12.88833 | -46.99018 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ef0f840-2050-3af0-9f92-d05b613c49c1 | -13.59095 | -47.28622 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab80044-e042-30b2-a7fb-f93f10e84fa5 | -13.583 | -48.08777 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0373e556-ddf9-3f9e-85c1-2971490d08d6 | -12.85421 | -46.90859 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5314560a-0eb3-3423-a3c2-8ff58ccfda70 | -13.59732 | -48.05778 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 85bdaffa-ed83-342b-80aa-82a34decc45c | -13.64546 | -48.05924 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1efd312c-cfc2-39e7-bf6c-33c5301f9753 | -12.00794 | -46.61935 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92353bfd-de0c-386d-8d2d-9dacd5c2d80c | -12.79721 | -47.74319 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73e65b7f-151d-3626-a8d8-8ebe37f04084 | -12.98016 | -45.22546 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7ca05ce-3f87-371a-8cbd-0e44de4ac55c | -11.80171 | -51.80138 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79ffe699-6ae4-310b-96c8-55e87015017d | -11.80089 | -51.79883 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f367d8a6-2f78-3d2a-90c2-f60f7e5eb20a | -10.79949 | -51.97887 | 2025-09-29 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70d636dc-1ff0-3a0b-af61-95b495fa9b90 | -14.56852 | -48.27695 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b13598b-9caa-38ce-9f6f-16c93711dca6 | -12.94471 | -45.17313 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 382ec282-cfe6-36e7-b60a-f824b244b84a | -13.49058 | -47.40578 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39407289-0da6-3060-9230-74419ce726ad | -14.59416 | -45.01447 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c2c0299b-9427-35cd-8cd6-868bd5747793 | -15.21559 | -50.1015 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0ae12eb8-88f9-39d6-b43e-6767c218f1dc | -12.70108 | -46.89984 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93432b55-fb7f-378a-9257-bab765b6f690 | -15.5534 | -47.8782 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a2b740b4-8553-3211-b53a-cab5bed22efb | -12.85062 | -46.97982 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f97505b5-def5-36b7-8725-9d5d2b3c6784 | -11.94357 | -46.53511 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 959b35f2-df3e-3dab-a090-5ee18b28c05a | -15.08255 | -48.33422 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c169acf8-96cf-35c6-b74e-160fde9b9050 | -13.61924 | -47.35263 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4fa96a17-288d-3b24-b7d3-612d23c783d9 | -12.35296 | -54.15398 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf717eb3-a89f-3817-98c6-89463c1aa369 | -15.9104 | -46.20805 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0da6da2-72f3-34b4-b78b-2d26b945c4be | -15.35452 | -56.95472 | 2025-09-29 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a2345fc-5a7a-3cde-a3af-d78723fc119b | -11.99514 | -47.09352 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35bde6b9-3caa-325f-9c96-7141f231d945 | -15.3353 | -47.91476 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93aab920-576d-3b21-a79d-f37ed71cf74a | -14.5247 | -48.39814 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d0ba4ca-e0bb-3d52-bf1d-9ec64c61b408 | -13.57572 | -47.29935 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c9e215c2-5900-3e75-a4a8-4cd650c80d07 | -13.60647 | -48.06321 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b9526e68-6e84-3d5b-986c-e1b851738fdc | -14.53876 | -48.4431 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 148fab22-c6b8-3c74-9414-88f6714cf264 | -13.82291 | -47.97139 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ebbffe3-ad74-3bfd-a924-2615875c1901 | -11.70788 | -44.43317 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaa70164-88c1-3964-bd18-cdac2d313f80 | -11.00089 | -57.05804 | 2025-09-29 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc08833f-6fd4-3b7d-a79e-2ce2cf3517ed | -15.28833 | -46.41697 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f55821e-e66d-3f0d-8e02-bae655d73f3a | -12.83617 | -46.88407 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d55e124-2294-3812-ab5e-51bb43067b40 | -15.99902 | -47.0359 | 2025-09-29 04:59:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 440b22b4-17b3-3875-9c44-972e9c9d53dd | -13.58114 | -48.10321 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b882701-8603-3da5-991e-cf10b6435087 | -16.49047 | -46.03595 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c7b39f5-79c3-334f-b9ef-fbd23e21ebb3 | -15.04727 | -46.96929 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78d9d4a2-2f09-3036-a6ec-6ec2b505906f | -15.28455 | -49.25563 | 2025-09-29 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24fb6ead-8bcd-3fbf-a062-55eeae8879a7 | -12.20956 | -43.74465 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c4f3e61-74dd-35b5-8b5c-fe2db9ef6d45 | -15.71391 | -53.6377 | 2025-09-29 04:59:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70d100f9-451d-376a-85b7-127cdf0c9e81 | -12.86299 | -46.96471 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26e15ff2-9e17-3ed9-804b-f6c38685f898 | -15.22471 | -50.09883 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 04258651-7012-3a81-af83-25bb20c073d9 | -13.60162 | -48.06266 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2cbeb53f-8811-3013-9e62-7b6a59d5c583 | -11.80541 | -51.80196 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65f992de-1a63-3a05-b3ac-c18e2a4944cd | -12.92039 | -47.15498 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6c73c2b1-3a9d-34fa-a7b5-a63b9ac73211 | -12.02734 | -48.34579 | 2025-09-29 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5ac3e60-5727-3470-8520-f6f589ae0a29 | -14.55278 | -48.40749 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9bc1f6d-ac22-3c8b-a9e1-e5ba687c25d9 | -12.69621 | -46.89669 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89f74acd-82a1-3a62-a899-c9255f5728dc | -15.04118 | -46.97549 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70610edd-ecbf-3a76-b362-d6ad3043f450 | -13.18015 | -47.44382 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87d04edb-223a-34e4-be9d-c364d206365a | -11.62626 | -52.84494 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a403521b-6720-3a87-8172-b6e56fb7eef3 | -15.54912 | -47.87129 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fec61d43-c3ad-3cdc-b2a7-21389b7b996c | -15.52151 | -47.93124 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96ede366-fa4f-3854-8c4f-d60a7995d4c3 | -12.00467 | -46.60279 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6173d1de-1f4e-375d-acc0-28e2a5d379a4 | -14.8434 | -48.38018 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 578ae80c-49ac-3c20-b60f-136c4545a800 | -11.71987 | -44.43479 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1add57a1-bbea-30a7-8d81-f0c1ea5269a4 | -13.62095 | -47.3384 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a4912d-8287-392d-b0c1-5c9bbaf6d1b5 | -15.27904 | -49.2589 | 2025-09-29 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dae1920-2193-34a0-a414-e6cdb4dadf49 | -15.27961 | -49.25439 | 2025-09-29 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1596c87-2f07-3cc3-a985-79f4ad99b3a0 | -15.27934 | -49.26035 | 2025-09-29 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e804f0d-8784-3878-b402-e41ca28c94f1 | -13.38425 | -48.15974 | 2025-09-29 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0af3dc04-4581-3349-b38e-813891d34d24 | -15.29447 | -49.51216 | 2025-09-29 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 0f89eea3-b166-3f0b-ab55-c353c174cd22 | -15.34641 | -47.9065 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 275dea70-2dc3-341f-a917-9b5c1a135969 | -13.22875 | -50.95932 | 2025-09-29 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 168f27e8-a682-3d4a-90b0-36c0224d5f4e | -14.8415 | -45.56949 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68b27af2-e69f-337d-aa3d-77d5a9866311 | -15.54308 | -47.87659 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2866c10-bf01-302b-a9c3-80db398f6835 | -12.69482 | -46.90818 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 963ceea1-67ae-39fd-81e0-21cab79cc6f3 | -12.79652 | -47.74881 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22e74557-c153-3318-be1f-75063e8875ac | -13.60338 | -48.04893 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3bb3960a-086b-312a-9af7-8a9e23ab4f37 | -12.85458 | -46.90562 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README68.md)
