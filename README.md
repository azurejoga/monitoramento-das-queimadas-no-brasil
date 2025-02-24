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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6b19005-12a7-30ed-b451-c2d600c89d53 | -10.292 | -36.5181 | 2025-02-24 00:00:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| 0e71aa78-cd33-3bc6-903c-0564b93f8383 | -18.0024 | -42.6929 | 2025-02-24 00:30:00 | GOES-16 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| adeac9f2-6ce8-334a-a493-48580c623cad | -21.30188 | -48.61946 | 2025-02-24 01:09:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 46cf80e2-a4f4-3af6-9ac8-0d289fa7fb40 | -20.72206 | -49.42856 | 2025-02-24 01:09:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4946c0ee-5791-3839-8180-8713cb821cfc | -21.08299 | -54.19287 | 2025-02-24 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7d3d1d43-7379-30f0-a4c1-75d70ee2984b | -20.72367 | -49.43903 | 2025-02-24 01:09:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 62da9ee4-4b05-3701-9acd-82684df9a383 | -21.09257 | -54.19156 | 2025-02-24 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1097590b-263e-3fdf-b42f-eb38914f3d84 | -18.63804 | -48.25072 | 2025-02-24 01:09:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2507951c-210e-35e8-892b-c4f8f1b06032 | -11.36694 | -49.61476 | 2025-02-24 01:11:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1c23801a-b443-33ad-b549-3931f88879de | -12.10107 | -51.23683 | 2025-02-24 01:11:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98fc8bf4-b8b4-31b9-8fdc-efe807c690c3 | -8.07069 | -34.9799 | 2025-02-24 02:47:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| a18cc20f-9b32-3c90-8275-95652fc43651 | -12.1679 | -38.47326 | 2025-02-24 03:12:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb8336a5-9dc4-33cb-b87a-c62d40d31d20 | -12.1686 | -38.4697 | 2025-02-24 03:12:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7882299c-4e3e-37f4-91c2-dd7afb1ec603 | -9.86354 | -37.11057 | 2025-02-24 03:12:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 088245b0-93c6-340a-9423-eff34266d673 | -9.86294 | -37.11378 | 2025-02-24 03:12:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e524b962-e895-3a02-9b93-0e9e7a594e22 | -7.98209 | -34.93253 | 2025-02-24 03:12:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 67682d52-eb5e-35eb-97e4-9ec363716ec4 | -8.37018 | -36.19259 | 2025-02-24 03:12:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13cbeb56-2eb7-3f7a-894c-eaaaad9223fc | -8.37252 | -36.19622 | 2025-02-24 03:12:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ab55a7a-8a44-3651-a002-721283a12283 | -7.53225 | -35.20531 | 2025-02-24 03:12:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 497293fc-672d-302e-b7cc-702c084275a3 | -7.53317 | -35.20002 | 2025-02-24 03:12:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 58a1cf46-753a-35b6-84ad-467435083ffd | -8.36968 | -36.19545 | 2025-02-24 03:12:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99201325-e801-3514-866e-9a940e1dc56d | -8.37304 | -36.19336 | 2025-02-24 03:12:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3f84bcf-3a98-35e5-acc2-e28e4cb34802 | -22.67885 | -42.85705 | 2025-02-24 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bbbd3a24-f151-33a3-bf5c-5a9cf674f555 | -22.67196 | -42.85991 | 2025-02-24 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3fd3148b-2ed2-396f-8ff6-6c53ecb4c8bc | -22.67305 | -42.85535 | 2025-02-24 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3d932f7-04e6-322f-89be-176a373c6449 | -22.67449 | -42.8605 | 2025-02-24 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 70bf1533-8793-388c-afad-3fb877bc645c | -22.67777 | -42.8616 | 2025-02-24 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ae881b0-d580-32bd-b80e-4f98584f479f | -22.67555 | -42.85592 | 2025-02-24 03:17:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ae63880d-dcc3-30cf-8698-4a0b69ca9088 | -5.97819 | -39.68244 | 2025-02-24 03:34:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f613ec96-0987-3781-8db3-355a8d4861b1 | -8.29768 | -35.35947 | 2025-02-24 03:34:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cdada55-e8c0-37b1-acc7-6d38fc3ac19b | -7.53172 | -35.20433 | 2025-02-24 03:34:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6ac91b5f-599f-3f13-a78f-1127f587500c | -7.53508 | -35.20488 | 2025-02-24 03:34:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53139287-0073-3318-a01c-a6d9e8315ca7 | -8.0709 | -34.97631 | 2025-02-24 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 55931686-c0bd-3f82-ad1b-b818ccfde76d | -6.95475 | -43.00716 | 2025-02-24 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b8bc0cf-08e7-3ff8-9b89-c3831563e565 | -10.6954 | -37.05081 | 2025-02-24 03:34:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eb6a6469-54ba-3698-be13-63d20a754959 | -7.65248 | -34.82972 | 2025-02-24 03:34:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 26d40980-54ea-399d-9f9e-67c811b7c3cc | -9.86241 | -37.11121 | 2025-02-24 03:34:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b04a66e9-76fa-35d1-b42f-3e6acb1e90f8 | -8.2958 | -35.35938 | 2025-02-24 03:34:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a994a31-d4c8-3227-8400-6d6cce00513c | -7.6767 | -37.54911 | 2025-02-24 03:34:00 | NOAA-20 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 683a9e3a-a4e9-3762-98dc-720031055901 | -9.86198 | -37.11258 | 2025-02-24 03:34:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8984ae4a-29c9-312c-89a1-62cacdfcfc77 | -7.53566 | -35.20128 | 2025-02-24 03:34:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6f42db7d-68f8-356f-b383-389e376cebe6 | -8.06756 | -34.97576 | 2025-02-24 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 681ab80b-951c-3745-8669-7af3dc564a33 | -6.94939 | -43.00626 | 2025-02-24 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc74f556-bcfc-3204-8f75-388893f309c4 | -7.98259 | -34.93341 | 2025-02-24 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c0d0ac0c-5b6a-3953-a77e-f78ef06a84d2 | -12.13213 | -38.31112 | 2025-02-24 03:36:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f589ad40-e072-3fe4-9056-d9db5dd31cc0 | -12.16911 | -38.46807 | 2025-02-24 03:36:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f2bc1c11-eda9-3fca-ad55-c50989da83f9 | -11.28097 | -38.19736 | 2025-02-24 03:36:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05ccbadd-91dd-34cd-8b25-549154c65555 | -12.1314 | -38.31542 | 2025-02-24 03:36:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3900429a-2fb0-3cbc-ad6a-1b5135018a85 | -13.99278 | -42.48149 | 2025-02-24 03:36:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c43ee506-02b8-3e77-a22b-0e317dfa6a34 | -20.30366 | -46.47808 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6bf67cd-7357-3768-9039-94ce0a50a5f5 | -21.29408 | -48.61929 | 2025-02-24 03:38:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ad9e4dc4-0c61-3bbc-9376-47e850a2626a | -22.78538 | -43.75838 | 2025-02-24 03:38:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b241756c-e2a2-34d4-a588-0cabe287ca3d | -20.76419 | -46.77195 | 2025-02-24 03:38:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de092373-16d2-33ec-9bd0-a0b700094d04 | -18.81597 | -43.21354 | 2025-02-24 03:38:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4aab742e-cdd5-3f23-a64a-9914214774b6 | -20.30294 | -46.47886 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57c19734-a59a-35da-9b82-e4e366b966ce | -20.30372 | -46.4753 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67fb239c-9691-3e93-bb06-7d697c472e2e | -19.82401 | -40.09717 | 2025-02-24 03:38:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4c9fb4cb-e4d6-3ef5-8907-1f3a3f780533 | -19.71792 | -40.35476 | 2025-02-24 03:38:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cae053a1-6970-3b5f-9a89-c7dcafe0d74a | -16.6809 | -43.88637 | 2025-02-24 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da9fd4e4-c40e-33ea-82d1-5e0db900461a | -20.73077 | -41.00484 | 2025-02-24 03:38:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1ad1d135-18c1-3bcc-9b97-a869b9d8ee59 | -22.68412 | -46.8806 | 2025-02-24 03:38:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85a8d409-2673-3340-8114-4b3f9f74eeb8 | -20.30441 | -46.47455 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 64b2f04d-fc58-3896-98ea-9b07fec9e235 | -22.67409 | -42.85863 | 2025-02-24 03:38:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2d3cf3de-353b-3879-b84c-f9e926a261b7 | -19.83794 | -40.08173 | 2025-02-24 03:38:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cc0d88af-b748-3811-89c2-e9a3912c5956 | -21.2999 | -48.62074 | 2025-02-24 03:38:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f66fdb77-06de-362a-9b29-0b9febdd9d4c | -20.30946 | -46.47413 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02bd2bbc-e20f-317e-ab05-c35ee6709098 | -18.77678 | -39.87363 | 2025-02-24 03:38:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c021de33-f4a7-3a6a-8178-a206f82e31b5 | -20.29775 | -46.48008 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f70caf79-4ca2-3ea9-9c30-63ca12057a90 | -22.6834 | -46.88391 | 2025-02-24 03:38:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| effdda1a-c292-347d-b3b8-742aa1ac62df | -16.34651 | -43.69963 | 2025-02-24 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8da8ea0-3d1d-30f4-9c88-6bb8008ea4bb | -21.18061 | -44.2771 | 2025-02-24 03:38:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2161e567-a4aa-303f-b49b-30717efd8bf6 | -20.34836 | -40.36174 | 2025-02-24 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5b7d1bce-0083-3260-83d3-c6fc287cce80 | -20.29851 | -46.47651 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6a8f177-87da-38bd-b96c-54107144663f | -20.29779 | -46.47731 | 2025-02-24 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a930e137-ad50-3a4a-968d-fb62940a8e0f | -17.87292 | -39.8624 | 2025-02-24 03:38:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 96f0768d-a499-3323-a5c0-60a7dd68a9e9 | -19.76819 | -41.99289 | 2025-02-24 03:38:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 84a2bc00-79b7-37bc-b31e-1b862875ecf9 | -22.8569 | -42.98037 | 2025-02-24 03:38:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 12c972e0-d991-3482-88f5-4a1f1779881c | -21.18954 | -41.77903 | 2025-02-24 03:38:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f9db0c7f-ceee-3360-9db8-f4b96e9fda6b | -18.03802 | -39.92688 | 2025-02-24 03:38:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 87d757f9-e17b-30b7-8f35-55bbc9442e45 | -22.6748 | -42.85486 | 2025-02-24 03:38:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bfc543d7-1c5a-3da0-8742-9877400ead82 | -20.73139 | -41.00795 | 2025-02-24 03:38:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c636e8a9-f812-3e72-96c3-708301ed655c | -28.58268 | -49.44139 | 2025-02-24 03:40:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 097f2859-33a7-3861-8123-a156315072cc | -6.95645 | -43.00557 | 2025-02-24 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b699ba9b-de61-326f-9528-569278c96fdf | -9.86451 | -37.11385 | 2025-02-24 04:25:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66286535-44de-3c0e-8ee8-9bb3f98a8903 | -6.9528 | -43.00499 | 2025-02-24 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6a2a22dc-f888-37c4-9d4d-0fa9d95079d6 | -8.11455 | -43.14333 | 2025-02-24 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9beec9d4-56d7-3b7f-aab3-1f482db55db3 | -8.11519 | -43.13898 | 2025-02-24 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 87b76648-cf1c-3949-8a24-09d9aec62be6 | -8.07248 | -34.97518 | 2025-02-24 04:25:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 717b2af9-a2ab-39a4-9cc7-a1da7d543300 | -8.11822 | -43.14388 | 2025-02-24 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6fed49cb-54f9-321e-9af4-7544c52e4a77 | -13.99595 | -42.48027 | 2025-02-24 04:27:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ab7ee62a-afe2-3564-8688-5842e3eb274e | -16.68056 | -43.88192 | 2025-02-24 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 555166e0-25a8-3948-bfa7-6e652d9df90f | -15.57069 | -47.8553 | 2025-02-24 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55b5f39c-b611-3a89-9f74-ed16402202ff | -16.34929 | -43.69619 | 2025-02-24 04:27:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebc52c75-1fec-3bee-8c24-a537a8916b2f | -16.84888 | -40.70647 | 2025-02-24 04:27:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2f669f16-2365-3516-9286-c96abb67c575 | -10.59964 | -52.85122 | 2025-02-24 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c65f2708-498a-33ab-81d9-76e9133fc04c | -15.75628 | -47.70905 | 2025-02-24 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52faf47e-864b-3870-8848-7329271c4758 | -13.9944 | -42.47881 | 2025-02-24 04:27:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 30b7fb6d-4276-35b9-8872-9fff9021c6a5 | -13.54666 | -44.40331 | 2025-02-24 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af5ef524-28d8-3f11-a6b7-33ef47fe58f5 | -20.30364 | -46.47461 | 2025-02-24 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d65e534-6ba9-39fc-9641-094dc6d7c8c9 | -21.18295 | -44.27314 | 2025-02-24 04:29:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
