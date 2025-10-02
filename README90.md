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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43c1f782-c34b-3c82-9713-eebc4c005467 | -13.18227 | -47.79171 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 367a1334-0068-3489-9897-e95c195ee4b6 | -12.42671 | -44.09313 | 2025-10-02 04:32:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 533af18e-0311-34b0-8d17-692a5a1264d3 | -12.70452 | -48.57849 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 294e9bfd-59be-3804-b4df-46a302d5d0d4 | -13.65659 | -47.3062 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74b7de39-d460-31f3-8c04-1db37ae60048 | -14.19104 | -46.12862 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4226f2ed-b614-3dbc-a3fe-3bdfb278d448 | -16.28985 | -46.26426 | 2025-10-02 04:32:00 | NPP-375D | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5287fd6f-9a8f-3df7-933a-e95e0d2441d2 | -12.05466 | -48.77068 | 2025-10-02 04:32:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15ee665c-add2-3879-87a3-664c37198549 | -13.29862 | -47.20142 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24f15f67-50b0-348f-a049-75f1ec847b6b | -13.43331 | -44.22743 | 2025-10-02 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24be7ed2-6909-300b-834e-bb5aa7be5597 | -15.25777 | -49.30907 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edfa9964-13d9-3b80-814c-44bda054fc66 | -13.94151 | -48.09803 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53f94f9d-af1d-304c-a090-99de4ad7a665 | -19.45954 | -43.65366 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9dd0a186-681b-31e9-8cda-177a0212ca36 | -12.69182 | -48.5507 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4294f780-496c-3e77-9cc4-99b9f7100a30 | -12.84914 | -46.93481 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e3268a5-29cb-3f66-85b8-bda20565ce53 | -11.90631 | -47.88542 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67602f5a-939e-3182-aca6-e56b88687238 | -13.76386 | -48.00356 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b4d408b-7601-37d6-b5ee-636554c8baeb | -14.87702 | -48.13145 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b521989d-0546-3fcc-a590-3356b0ddb397 | -14.36508 | -45.94931 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4437b8a3-c0ad-3efc-9c32-9a9c8badfcf2 | -15.26283 | -49.30961 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1592d43f-16f6-31e3-b560-deccfd2b63d0 | -14.98886 | -46.89429 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 737779ec-0bac-317e-8b16-679eb8e1b70a | -15.35218 | -46.28238 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfbaba04-b435-3d62-bc5c-cacf1ab7ed20 | -11.94496 | -47.05446 | 2025-10-02 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa5dbea9-db8b-3372-a790-f1b8c181f6c4 | -13.56982 | -47.27758 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca430e8f-7ea0-3a75-b43a-e1bfb172cdce | -12.67437 | -48.5736 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97521334-50f9-3d9d-929d-cda7d4ba3fc7 | -19.45907 | -43.65746 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d56ebef-ee13-3174-8940-bf6f13ebf9e2 | -16.01037 | -50.9086 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6600db29-c99f-39b6-b98e-213151aaea30 | -11.58331 | -50.16666 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97db724a-c0c1-376a-8b6a-4041c303b3e8 | -12.86375 | -47.01777 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97d786a6-3705-3d9c-8e89-2169a34665f5 | -14.1835 | -46.66583 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a38d6dcd-7a3d-334e-b5f2-ca5b45424320 | -15.20861 | -47.99862 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5eb6d4fa-31c0-3bc9-8ebf-ffed0cd8b738 | -14.89976 | -47.1777 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18dd19dd-819e-3dda-9067-f2d64142cf91 | -16.02299 | -50.91893 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f154f45-811d-3834-b012-9523501a0136 | -14.32978 | -45.87596 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f285a06a-2835-3c91-b200-b102ca214e83 | -15.70128 | -46.25416 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1eaa3663-5346-3091-8d03-dddcc8ab6500 | -16.02232 | -50.9229 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5ff0e6c-5daa-358f-aa7f-9f115b2c038d | -13.2475 | -47.30999 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6d11907-467b-362a-a83b-60e7d29ad940 | -14.89149 | -48.10454 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d9c3283-f7f9-3b3f-858f-addfc78ed938 | -12.49557 | -50.26305 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c60e05d-9e05-33c3-8f5d-539383217e07 | -15.76393 | -43.66957 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d82b360e-4c9b-3bbe-a6a2-678c2e6c378a | -14.42822 | -46.10469 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ecfcc25-bd03-33e7-be4a-6b9b0e139bc0 | -12.26086 | -47.81982 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 985bfd66-c7b4-3fca-9735-9f1f3a56593e | -14.36564 | -45.96921 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ce65ea4-424c-3392-acb0-355a7a57a21f | -13.74886 | -48.01203 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 56be8aff-1e84-36dc-877d-9c711d8cb882 | -15.29684 | -45.08063 | 2025-10-02 04:32:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0270eb51-3c38-3c3d-b719-39ea2b603ed5 | -14.65006 | -48.26274 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 001cd868-4a31-3023-a805-b7fa3774bf5e | -12.68442 | -48.57524 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8aaaeacb-5490-3f89-b49f-f13b419b892e | -16.02714 | -50.91563 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b6f0a944-a212-3092-b057-ab6988dd4bc6 | -16.36773 | -47.05941 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56136e0c-45ed-3035-b5f9-ab4319023d1e | -14.68169 | -49.61141 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb2faf6e-eade-37e4-80bb-57c7de49a70b | -15.92546 | -43.33368 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a71d89d6-b603-354b-86f7-5ef076231d3c | -15.02887 | -48.06416 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c8e84897-c9c1-3b19-8d4b-cc1780481f8c | -12.64502 | -44.22988 | 2025-10-02 04:32:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0b3842e-1f2f-3431-8cf4-b13ec4476c60 | -13.80087 | -47.53437 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 2d7cab6d-371f-3033-8230-73092068a4e2 | -14.33933 | -47.15252 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27744977-1fc4-3003-bc8f-c59636003783 | -14.33865 | -43.83803 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8080cb26-82be-3fb7-aef9-0645cb99ce59 | -13.32367 | -47.22763 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee548afd-20c3-328d-88d7-970cd63152ea | -14.47342 | -48.43443 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2df563de-e674-36eb-9d0e-2f1e082edacf | -14.2293 | -44.9361 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfa971e9-7116-300c-87b7-0cb5a2f66937 | -13.74441 | -48.69527 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14d13a82-b18e-3c99-b257-b762520aaf3a | -12.14632 | -46.67286 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b5787f5-00ef-3075-a1f2-b035bb0d7820 | -13.15835 | -47.83507 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3808e2ed-adeb-3923-acfc-1fcceb6af864 | -14.96941 | -46.92585 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f94c59f3-cea7-3060-b8bf-8e9ab75de0f1 | -12.90674 | -47.1716 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bf84330-3e9c-388e-8ab9-93947504ee77 | -14.96968 | -49.96362 | 2025-10-02 04:32:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b658e9d-8d2b-33b4-8aee-c665bdeea641 | -13.16949 | -47.80778 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc8fec71-8ac0-369c-a796-8d5f12f89ae2 | -18.17484 | -53.28228 | 2025-10-02 04:32:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 348789a6-fcc5-34e8-9f95-baf848cda520 | -14.70119 | -48.21229 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68d73675-af24-3068-a469-f64f1665c082 | -13.79764 | -48.04931 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 91fd7e9b-6fc0-309d-982f-d641050c8f5f | -12.76482 | -50.55564 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fc76efc-3aa2-3ae5-bcd1-6577553b25cf | -15.94121 | -43.33974 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 03c59dc2-7696-32ee-99ad-efc98310aad1 | -14.90154 | -48.31475 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81bd6b2a-94d1-3dae-9070-6da6074b010a | -15.14028 | -48.02037 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e6b20ab-57c7-3c17-b59a-0ed1218e3c44 | -14.0205 | -47.98696 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aadc5dbd-b05d-3b83-a342-637a6b2a23a3 | -13.79487 | -48.0452 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc4bff00-6d5f-30b5-852b-db2ae0aab8c1 | -13.3632 | -48.12381 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47c57bf7-b158-39c9-badb-48aa02b4b27e | -14.4752 | -48.40174 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b065f04a-4b15-3926-aa07-02763cda455a | -12.65976 | -46.87173 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e76f0b89-35ef-3194-8693-f8a40f28c5d1 | -14.41553 | -46.11864 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12753ad1-f070-37f6-a0a3-f6d318263270 | -14.69588 | -48.11617 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4ca46ba-891f-3d71-a16a-3c1f503a5b74 | -13.21624 | -48.49424 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94a7241b-cbc9-3a10-81ac-9076bffedc80 | -13.77986 | -48.05367 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18f668b5-0c4e-3106-a27b-fefcb4cebfee | -12.70887 | -46.8872 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46d1132a-acec-38d5-8cb1-6f73b7bd144d | -15.28277 | -46.39346 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f19007c2-3f5e-3aff-ab80-575a9e9e99a4 | -14.3365 | -47.12607 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 713d0129-072a-30f9-b5d6-ed072d2b2ad2 | -16.36666 | -47.02052 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a152a74-71b0-3342-b3b2-f8b255601a16 | -19.01982 | -49.74826 | 2025-10-02 04:32:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 895e171f-bcce-3f07-a151-8782a65318fa | -12.50474 | -50.25132 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91a8cc21-b96d-3deb-904b-f092d9630e02 | -16.04427 | -50.87794 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1af37509-c3ae-3078-977d-6a81352737fd | -12.40821 | -54.36472 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57bf99f9-d402-3eb3-aee1-8a82c2e674b8 | -15.24483 | -48.72818 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da5d1c8b-3289-37da-9651-d6e815674f3d | -13.75118 | -47.95401 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67374457-6534-33dd-898e-87d87f7e27fc | -15.15238 | -46.41071 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e6305f2-5b23-3a9f-a5ab-31e74d632e28 | -13.75269 | -48.7077 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3e65a45-1373-3ab4-af7f-2a32bb61223f | -14.41726 | -46.08338 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2e3ac87-4f30-31e8-aa2c-779fbe8a0e91 | -16.3672 | -47.03996 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a353c16-72f8-3b85-8388-f07033d916c3 | -13.04636 | -47.05823 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7fd9764-b854-3859-be51-2147abc5e9c6 | -16.175 | -57.5981 | 2025-10-02 04:32:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a2984670-8c26-304c-bfd3-d98cf6c9bbda | -15.12944 | -46.44627 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33736865-9fc9-3118-972f-cf64e4d3a173 | -13.47676 | -47.24831 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5528f939-7fac-3628-8424-024c873d0151 | -13.75662 | -48.70465 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README91.md)
