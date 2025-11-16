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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14197ace-21bc-3502-9ada-bfb33c1b1ba2 | -14.05768 | -43.12376 | 2025-11-16 04:10:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a195be74-5235-3569-8833-907546d3dbdd | -14.67752 | -46.54554 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fb41393-dadc-3418-8923-4c5b7a14338c | -13.55456 | -44.1039 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34c17a9a-6090-383a-b61e-501b30c65d7f | -12.85709 | -46.45292 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a28b1051-dd0c-3a04-992d-6187923591d8 | -12.67866 | -47.17215 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 17a2aa66-1b98-3f1f-89da-8fd5ddbd3164 | -12.80146 | -46.44844 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40f6dcda-2953-3763-bde6-551bc9cb58f9 | -14.58239 | -45.22033 | 2025-11-16 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 381b9425-f7b9-36a7-9a16-3b8da1e79ae3 | -14.20478 | -41.84629 | 2025-11-16 04:10:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99e043ec-17bb-304c-8b21-6e0daaed6754 | -17.3408 | -44.90763 | 2025-11-16 04:10:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a8cb44e-0219-3364-813c-ac8603cd6e28 | -12.67784 | -47.17691 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f812c7fe-48cf-378e-8a3a-3dae96829845 | -16.565 | -47.6137 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 124fa1d9-2b63-312f-a25a-7ef22c80cc49 | -14.64381 | -46.55959 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39da4e9f-0c34-3672-966b-9fec061d9832 | -13.46405 | -44.03374 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42d8df86-877c-3189-aa4d-d276571ddb53 | -14.64597 | -46.56871 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7e2a6bb-d0fb-3932-a4b1-f7a81b9637d8 | -18.35339 | -47.25682 | 2025-11-16 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82a6f1b4-fe7e-3746-b592-f7ac1ed872c5 | -12.80941 | -46.44585 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a2b87de-2efc-3eaa-846e-e062428f6426 | -14.65755 | -46.55443 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 052950c2-a1f4-391c-8fbc-78790907ce65 | -13.70826 | -48.19722 | 2025-11-16 04:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fd8b17a-813b-3ec7-b712-9311379c126e | -14.64293 | -46.57474 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6aa03906-e46c-3d5c-bf18-b318756510c6 | -15.52599 | -44.38079 | 2025-11-16 04:10:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b551eaae-440c-347d-9c5d-0ebe4ac3a245 | -13.87095 | -46.84431 | 2025-11-16 04:10:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 358755c5-9bdb-3ff6-bf05-58b02f6a2dc3 | -15.45744 | -39.23935 | 2025-11-16 04:10:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 40f35bf6-154a-399b-8ad9-6687eb0c4486 | -12.87761 | -46.4426 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d67ac77-8071-3df8-9bbc-a0d79ee558bd | -14.66259 | -46.5466 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e748057-7e62-3436-9a75-3aec62c64671 | -14.58177 | -45.22408 | 2025-11-16 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f157a6cd-d3ab-3159-b852-871a5ea16862 | -13.55069 | -47.38607 | 2025-11-16 04:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4032a925-c697-3609-b35b-78557a30f36f | -14.64508 | -46.58362 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00021a17-56a1-3a84-9777-4b715e00f455 | -13.7576 | -42.89273 | 2025-11-16 04:10:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4ef05b7-a349-3d7e-9f9a-2aeed2ec4dd0 | -12.84407 | -46.41961 | 2025-11-16 04:10:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13765578-923d-3e1c-8175-ee27b94b4657 | -13.3636 | -44.77625 | 2025-11-16 04:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 945f63c1-1336-3f3f-bf31-aab5467722b2 | -15.52931 | -44.38136 | 2025-11-16 04:10:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77d1962e-13ef-3278-bd62-89fa9f51e695 | -14.65082 | -46.59315 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f6f440a3-f153-30ee-8fd8-38a3377f89e7 | -16.56949 | -47.60981 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c4348cc2-6f71-3717-a9fb-1cf0ecc0c4b8 | -18.32278 | -47.18327 | 2025-11-16 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16600cf7-e51b-3c46-9382-4d17fc0b2ae1 | -13.36824 | -44.05872 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 860ed998-42b7-329d-9e00-bf1b3edc4379 | -12.87097 | -46.45955 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ced50294-0d3b-3e91-a97e-53901f9322d7 | -15.37547 | -45.64489 | 2025-11-16 04:10:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4231cac-11e0-3f76-b4d6-5bd205b4e2c0 | -12.63512 | -48.50779 | 2025-11-16 04:10:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09ec7011-7f39-35d7-8cde-e805e6422454 | -13.97783 | -47.05307 | 2025-11-16 04:10:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6b2416c-e040-37b5-8e7c-aa7bdf1266d9 | -12.41298 | -48.60683 | 2025-11-16 04:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a278170-064e-379b-bc2d-1d6bdbbd87cc | -15.07242 | -43.25739 | 2025-11-16 04:10:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1aec6b50-137b-3929-8b79-3c70f8ab8c5d | -12.68215 | -47.1706 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1820bd0-8962-3b88-9911-ef962083788e | -13.58849 | -42.99606 | 2025-11-16 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ea17d10-ce7c-3b19-91f8-f4fe1830c2df | -13.97474 | -48.78306 | 2025-11-16 04:10:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef5de3cb-68f7-3aa6-a81a-7ab3914677e7 | -14.66029 | -46.58119 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8365aa15-0bfe-312a-8439-1942a5632516 | -12.85429 | -46.42559 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1d5a6be-fd13-3549-a6b2-8e73b7aa61f4 | -13.35752 | -43.63982 | 2025-11-16 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6bd971b-7e4c-3b2e-9b68-ac666483c7da | -13.81973 | -43.18969 | 2025-11-16 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2a423a5-a474-39d0-9e48-6d8986baa70e | -13.05552 | -53.95387 | 2025-11-16 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 61d9927e-e0c6-331b-ae72-95d0da3a6e07 | -13.65029 | -48.74751 | 2025-11-16 04:10:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f744739-72be-3ad4-aa8d-d596108c35c8 | -12.86384 | -46.7796 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b9d8c92-520f-3ca2-af13-9c72c58b3387 | -14.64653 | -46.57529 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4aa624f8-2bba-3891-af74-94ff046c7760 | -14.6458 | -46.5795 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fac25e5d-b625-305e-9ccb-d2892869aa2b | -13.55372 | -44.27801 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc91d964-d3d4-312f-915e-b28212236775 | -18.7105 | -43.00492 | 2025-11-16 04:10:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ffe8e7a5-60ff-3dbe-8088-8cf4271a98b0 | -13.75728 | -48.52644 | 2025-11-16 04:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f744eaad-7feb-33c7-b5d8-464fcbb929c9 | -16.04821 | -44.82734 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 043421c7-a4aa-3b7e-9609-a22f50a44983 | -17.34413 | -44.90821 | 2025-11-16 04:10:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 167e91b3-6c94-3fa6-b47a-e8b51b218782 | -17.78325 | -43.85795 | 2025-11-16 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cecda706-2684-3899-bfa4-437136aeaa10 | -14.39002 | -43.87745 | 2025-11-16 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3e75e4a-e866-3637-90a6-eba144832035 | -14.35835 | -47.87994 | 2025-11-16 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35e94a6c-765c-3a4d-98e6-0db8da027ff5 | -12.86 | -46.45786 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd5ae378-227a-30b8-953a-c2d23d07d687 | -14.49047 | -46.62514 | 2025-11-16 04:10:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c1b25e0-9ceb-349a-9859-3a00cad70b89 | -14.89493 | -47.37179 | 2025-11-16 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9571754d-fa0e-30e6-85d1-d2ececef4de6 | -12.86366 | -46.45841 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 978f0a79-f671-3b07-9234-d6d307e32f69 | -15.68552 | -42.58702 | 2025-11-16 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73a1ec7c-1a93-30a2-9906-581c7d8ee244 | -13.82248 | -43.19378 | 2025-11-16 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 477c9435-cc7d-3972-a6ed-c59bf7259999 | -18.31925 | -47.18259 | 2025-11-16 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3233e8eb-e60d-3670-b8fd-a13c300b9a0a | -13.98026 | -48.77604 | 2025-11-16 04:10:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84a32803-05fa-3abd-a00f-41cba5aefec3 | -17.77938 | -43.86099 | 2025-11-16 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5841b2cc-16e0-3f85-9636-fdc90e48bc7c | -17.14639 | -47.32194 | 2025-11-16 04:10:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4406c4a-c33d-395e-8f7d-02eb8e8cadda | -14.07265 | -41.26472 | 2025-11-16 04:10:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2996df4b-81d7-3b6d-899d-6cfdab4e2b60 | -15.95346 | -44.97326 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f0b07a8-b8d1-32c6-aff2-82c75809bbfd | -12.86731 | -46.45897 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 418cf3ce-e663-3df2-ab2e-b6273943667b | -14.49119 | -46.62088 | 2025-11-16 04:10:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 830998f2-06d3-3435-96b2-714dab0fe345 | -15.45952 | -39.23722 | 2025-11-16 04:10:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 313b67ee-b846-38f1-acb1-5abe6dda168d | -12.67405 | -47.1762 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a0c63bdf-1e37-306f-b489-9684ce221916 | -12.79784 | -46.44761 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cd65674-5084-3ea8-88bb-6ec1310aca3f | -12.85932 | -46.78363 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0065c526-4bae-3a67-ac04-16e390584bef | -13.97705 | -47.05758 | 2025-11-16 04:10:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7680b813-7a04-39e8-8317-9c922e2f3b43 | -14.9493 | -47.52855 | 2025-11-16 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5ba8d7a9-e229-33b8-a0ae-9347891628ce | -12.80976 | -46.44452 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b78fd4a-9e69-3bc5-bdc3-8058c8910e53 | -14.20421 | -41.84999 | 2025-11-16 04:10:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a4bab766-a4c9-32a2-8c03-0759fd5b89b3 | -16.04487 | -44.82676 | 2025-11-16 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9d35c591-61f1-37ae-be06-3f4724372c9d | -12.80867 | -46.45021 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b61f08c5-2da8-3b1b-9bfb-32c21829d0e5 | -14.64435 | -46.58781 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c360b619-dcc8-309e-bb91-3aa360b4c5a7 | -13.55359 | -47.39187 | 2025-11-16 04:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c974fa5c-145b-3ea9-858d-aa05f67cc069 | -12.86375 | -46.43593 | 2025-11-16 04:10:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c44949c-55bf-38f8-9cdb-9d68610b7e5c | -16.04254 | -50.20916 | 2025-11-16 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88baaf3e-ff8a-302c-87f3-356c24dfd0cf | -13.78978 | -46.9028 | 2025-11-16 04:10:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56bb5425-50c6-31a9-9805-2c67c8e34681 | -13.78899 | -46.90739 | 2025-11-16 04:10:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e1f0793-d88d-3166-a34a-8aa49b676b1d | -12.80824 | -46.45323 | 2025-11-16 04:10:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83fd0e4b-4f33-3bd6-8d1f-fae5d69679f3 | -13.75709 | -48.52734 | 2025-11-16 04:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 317a0bd7-43ad-34ce-95ef-22d858baa47a | -13.81739 | -44.4528 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57c00f2f-a03c-332d-a76c-06267cee1b7d | -13.3843 | -44.37619 | 2025-11-16 04:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f47e492-1cc8-3f6d-bd97-ee4f7c4f3a25 | -13.5498 | -47.39114 | 2025-11-16 04:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a00313c-e03c-3e92-91e9-09457ac42a30 | -13.5545 | -47.38667 | 2025-11-16 04:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0137486d-fe40-3259-af81-9b647dd189d7 | -13.75569 | -43.14265 | 2025-11-16 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32c4a43e-4d14-372d-bc68-c1d2b11cec84 | -18.69986 | -40.10972 | 2025-11-16 04:10:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 85571ff3-6a66-3273-801d-8d937e78d3b6 | -13.36028 | -48.49899 | 2025-11-16 04:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README46.md)
