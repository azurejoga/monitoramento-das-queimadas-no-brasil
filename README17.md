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
| 0a90b8e5-0989-3d8b-9792-e71e7a4d3bfd | -10.07244 | -46.67924 | 2025-07-17 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef5d8c97-1f48-3377-bf21-84f6ea51a4f9 | -11.45842 | -48.1608 | 2025-07-17 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c9dd849-b9da-3517-b710-ba17a150ad05 | -11.94455 | -48.43045 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ceb515b-7a1a-33f1-b233-8a089648299b | -11.94625 | -48.42134 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b36c8e29-447c-36c2-820c-fd8c7a02be6d | -12.70655 | -46.81049 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab4fc959-2781-354f-b434-dd17ff6e5ae4 | -12.37289 | -50.37593 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 465bb379-720a-3c55-b24e-041988aae4ea | -10.56559 | -49.13917 | 2025-07-17 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f610a151-045f-3028-b690-3917f5a3ee68 | -10.54551 | -46.5139 | 2025-07-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac7630f1-6740-3818-89f0-f1fa1b53a6f2 | -10.95991 | -49.25041 | 2025-07-17 03:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d26aaa6c-f544-3be5-b4cb-f994b47b2bf2 | -14.02232 | -51.22813 | 2025-07-17 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1b9bdd26-a490-3197-ba53-6c059a2ed90d | -9.24173 | -48.55883 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 61ff120f-9fae-3868-ad90-47ede612d632 | -14.51562 | -47.67121 | 2025-07-17 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6197d427-7975-3627-8a27-278c49add3ea | -10.80768 | -50.46915 | 2025-07-17 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd358474-28bf-3018-8d2d-4764fc6a899a | -12.40495 | -50.48486 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| af8480b1-2f79-3ab4-8dab-334e9d568844 | -15.2139 | -44.74135 | 2025-07-17 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb4cf62e-c486-3d7f-8a9f-33581146f17b | -12.40949 | -50.04638 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42e9ad7a-fa47-3dec-b95e-7cafa2c65b1f | -12.49022 | -46.93 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dffbd0e-8393-3c89-8ee2-8609d3fed1ab | -13.01919 | -45.06418 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfd4d5c4-eb67-3e39-b2b4-04f8a1db4b1d | -10.20821 | -47.32247 | 2025-07-17 03:55:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9924218-d57a-389c-818f-3aa11fdce845 | -12.37209 | -50.37998 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 61674bf1-5cfd-3eec-bdd1-a79c19bc8b84 | -10.96695 | -46.47935 | 2025-07-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cece5c56-7dcd-31e7-a881-e29070c5f2b1 | -14.50531 | -47.675 | 2025-07-17 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a11be6bf-46a2-3aec-b85c-9386281fe002 | -12.71105 | -46.81133 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 753b33fc-3471-3411-9bdc-61249de4be71 | -12.41027 | -50.04251 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c05e27e3-f268-3b53-bb93-3a6f46d701ab | -13.0152 | -45.06343 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8db0fb27-c917-3b9c-ae2c-3c2037c01e40 | -12.47567 | -46.93215 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5434735-bf14-301d-9de7-1c983a352a06 | -10.9695 | -46.46526 | 2025-07-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f21a1920-2863-3ec2-b826-e819b73b502b | -12.47855 | -44.50252 | 2025-07-17 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a871b19-ebfd-35d5-a80b-9ac11db9ad30 | -12.03 | -47.78065 | 2025-07-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 011c6948-c6ee-3003-b1b1-de224b1f4530 | -9.24367 | -48.56643 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5586ed56-ea08-3c96-9e1c-51ace7628e95 | -9.41623 | -48.41106 | 2025-07-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| beb1e970-541e-3c99-9748-c56a95e58c9f | -11.66204 | -43.77148 | 2025-07-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8112b9e4-80ce-3f05-bfd3-e5796b29b6b5 | -8.91366 | -47.3576 | 2025-07-17 03:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6f8294f-e0aa-3eb6-963e-e643d7c49ea7 | -9.23831 | -48.56531 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dd66f7eb-219e-36af-b51f-29eb2f0dca21 | -10.20335 | -47.32151 | 2025-07-17 03:55:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed6adbae-98dc-3b2e-88e4-772c86506db1 | -11.58142 | -47.30203 | 2025-07-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67baf3ef-c9c5-39d5-bf88-9a3d01e0d7d7 | -11.46089 | -45.09686 | 2025-07-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed818bf9-d5fe-3a68-b7b8-d77a7178c971 | -13.01751 | -45.06452 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e24a58ce-cab1-3874-9851-0c0e86c156f2 | -12.70696 | -46.79921 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a45d813b-d01f-3620-ac4f-f54028cfa805 | -14.02989 | -51.22078 | 2025-07-17 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07d10692-40a6-3144-bb1b-92c73e3cfc24 | -12.97077 | -38.51338 | 2025-07-17 03:55:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| aacf7391-191e-3d93-bc59-675a02373b70 | -12.41235 | -50.04404 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fac1ce1a-575d-3d6b-927a-fcadf3bc2dc7 | -12.42624 | -50.04992 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2975cc54-a2c9-31d9-bb03-8ff6be07b7ac | -12.09687 | -48.19532 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f0a2740-a859-3dc2-913b-41b7c529f16f | -8.88025 | -50.1518 | 2025-07-17 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95995ee5-465d-3bf7-8734-bd602595b17d | -12.70292 | -46.80501 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e83741f9-6bee-3935-bb93-ceaaad759928 | -13.00485 | -44.87867 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff90f83b-401b-360e-b908-4741d25ac3f7 | -12.97133 | -38.50973 | 2025-07-17 03:55:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4a64da92-03c8-3e2e-96f9-f9014fb7167b | -22.99643 | -47.12351 | 2025-07-17 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c132e3c-4878-3a19-86d0-6106c894f900 | -19.5389 | -49.68094 | 2025-07-17 03:57:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 586cac50-cd45-3ec5-8033-e73f6c2f27f7 | -21.27587 | -44.50844 | 2025-07-17 03:57:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e070be04-aea9-3b04-85a3-bb125e848023 | -19.96206 | -48.9866 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67209ae3-46d3-3a75-a06c-0fcfbc1e8d6f | -20.01131 | -49.04921 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 81e2d44b-de8d-3e7e-ae8c-7a793847f98a | -19.44448 | -48.54089 | 2025-07-17 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c847f0f6-b5be-3fa2-9e0f-ee1d0a27b3db | -20.98869 | -49.77444 | 2025-07-17 03:57:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 74fa47fd-d442-3433-8a78-8a2cdccb865c | -19.62982 | -44.94783 | 2025-07-17 03:57:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81ac29a8-bf3f-3b3b-b34e-ebf08e889c35 | -19.95752 | -48.98558 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fdef4a3-4080-3386-9577-2bcca850340b | -22.55325 | -44.12628 | 2025-07-17 03:57:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eea8aced-d163-350e-8a92-2abb94bc5e0c | -19.74412 | -40.69308 | 2025-07-17 03:57:00 | NOAA-20 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7fb24abd-efe1-3449-b8c7-d1d79b5f0ba9 | -18.91838 | -47.00924 | 2025-07-17 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b0a6ee1-ea8f-3cec-8339-d3a15744a648 | -22.95827 | -46.73467 | 2025-07-17 03:57:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76df0f77-d69f-3e36-9bb4-d1e55216db86 | -20.99087 | -49.76386 | 2025-07-17 03:57:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e7372347-2f1a-34ee-8eaf-9ea37f197417 | -21.8023 | -49.63042 | 2025-07-17 03:57:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9f93e025-a9a8-3d2f-9ed3-02bdf58eee75 | -22.39629 | -49.79244 | 2025-07-17 03:57:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eb7b1842-962c-341f-a9da-0f19058a4dc7 | -23.1552 | -46.24443 | 2025-07-17 03:57:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 21b3188b-775e-3ca4-ba53-cb2e20201d45 | -22.14003 | -44.83054 | 2025-07-17 03:57:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bcfa8c26-2293-3f6d-b47c-fd925d535b27 | -23.22926 | -46.40265 | 2025-07-17 03:57:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f7990cbd-9a18-376b-9edd-65fa2443bf9a | -18.98174 | -48.31007 | 2025-07-17 03:57:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 611910ec-b4d8-35a9-b266-f5bee5793956 | -19.4534 | -45.30568 | 2025-07-17 03:57:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25598a65-7d88-35ba-8e03-f3d959bdac1f | -19.8573 | -48.96425 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a1db93d-3f68-3812-a428-e430a574125b | -21.22912 | -43.72566 | 2025-07-17 03:57:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ae2e9291-c995-3f72-b1df-971c78e1cc02 | -22.99447 | -47.11936 | 2025-07-17 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 299cd86e-df0c-356f-ba09-ecccd4498118 | -22.54568 | -44.94364 | 2025-07-17 03:57:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cb88814d-21d2-3dc9-b3a8-b6b3530b7abf | -22.69799 | -47.37995 | 2025-07-17 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9214042d-51b6-38ab-b566-fcbbc7cf1672 | -23.51824 | -47.01786 | 2025-07-17 03:57:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9ae2db46-f5ad-337f-bb8e-f5bb8f7e6731 | -23.25215 | -45.5794 | 2025-07-17 03:57:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f0ee8f50-2e84-32b5-95d0-cf495e5021c2 | -23.06056 | -51.51971 | 2025-07-17 03:57:00 | NOAA-20 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 14fbcf9a-c94b-381a-a936-d625a7018a3f | -22.55392 | -44.12232 | 2025-07-17 03:57:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fa14a27a-113f-3455-8c68-29ab06804766 | -22.87261 | -46.79639 | 2025-07-17 03:57:00 | NOAA-20 | MORUNGABA | SÃO PAULO | Brasil | 3532009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c71c9b19-39c2-3bdd-809f-bec967d6b7e5 | -19.44547 | -48.536 | 2025-07-17 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb613aea-8ec3-3a5e-bca7-476e13c1c0ca | -23.08322 | -49.73522 | 2025-07-17 03:57:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1d5bdf26-00ff-3836-b909-c93a5e074fac | -19.4472 | -48.5393 | 2025-07-17 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4c8d32c8-9b35-3fbb-8cdd-d838d3595522 | -19.53636 | -49.6724 | 2025-07-17 03:57:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 63479ff0-4818-3872-90cf-0806ce1a2644 | -21.74668 | -48.13194 | 2025-07-17 03:57:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b10e9244-d323-37b1-a2dd-fc24aec26b83 | -23.22556 | -46.4019 | 2025-07-17 03:57:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 90ae8ce7-478a-37a8-8e3e-b30585eff5cc | -22.10501 | -45.13405 | 2025-07-17 03:57:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b3fe3fd5-b480-3dcc-b8c8-212d345e30c4 | -19.47903 | -49.2922 | 2025-07-17 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7bb6a7d9-fca5-3b3d-b1e8-182ddf085271 | -23.25569 | -45.58017 | 2025-07-17 03:57:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 78fbeba4-6a9c-32fa-87a9-f89d59a82c8a | -22.5422 | -44.94291 | 2025-07-17 03:57:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d876a0b3-1aea-3021-92d9-4fe3156b9566 | -17.83652 | -44.35355 | 2025-07-17 03:57:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa55f11b-37a6-375f-9498-cee3f5c51d11 | -20.99335 | -49.77557 | 2025-07-17 03:57:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 57435315-128f-3c3e-923c-bec6a7ec276c | -20.00716 | -49.04512 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fae8288-b9ec-3fa5-865c-f501e149cf1e | -19.54001 | -49.67908 | 2025-07-17 03:57:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 45f28cf9-8a88-330d-99d6-68dbd87a8c49 | -20.0107 | -49.05104 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7436bb59-f369-3f7d-bb63-4f6228d57b33 | -19.44888 | -48.54208 | 2025-07-17 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0c9700d-0534-3449-916e-0b4226fdc202 | -20.00676 | -49.04822 | 2025-07-17 03:57:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fe650012-f3c6-3426-8621-c85a7aaf5677 | -21.64782 | -44.26358 | 2025-07-17 03:57:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e9528fd8-0557-3fd1-899f-1ea1a996bbac | -19.47438 | -49.29112 | 2025-07-17 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3f7f9762-f5a1-32af-81e7-309d9f1b8c1f | -20.98979 | -49.76912 | 2025-07-17 03:57:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 0bcc9bc7-c79f-39b5-a0bb-f0d4c4eb0f75 | -22.10429 | -45.13817 | 2025-07-17 03:57:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
