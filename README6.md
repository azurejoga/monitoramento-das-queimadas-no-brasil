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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69308f10-7f6b-3a33-930b-7519fc68ec03 | -12.06856 | -48.47154 | 2025-05-30 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce97b4b4-064d-3cde-8177-e814bd948514 | -13.00274 | -42.67091 | 2025-05-30 03:55:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| db82ebea-7bf3-3953-81ee-1fd01a0cbc11 | -12.82609 | -47.39557 | 2025-05-30 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a50294d3-96dd-3ba9-be05-745690471f59 | -12.39598 | -50.00251 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 545b598f-9f5e-3bd4-8b67-4dabae5e70e2 | -16.03052 | -43.67907 | 2025-05-30 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f0259b9-92be-3b09-b73e-5db868ed9f62 | -12.01155 | -49.52142 | 2025-05-30 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b20183d6-a460-3f0e-87f2-30503f0ac291 | -14.83954 | -48.10057 | 2025-05-30 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4353c96-6597-3a57-a49e-e639375f8cea | -16.52056 | -43.06229 | 2025-05-30 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e0aa770-07e8-3705-8c56-7ab4794257fb | -12.39093 | -49.96858 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce645f14-0914-3079-b79a-fc40ecfebf7f | -19.94095 | -44.10099 | 2025-05-30 03:55:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 893d1185-6acd-3314-966a-0918eca3462b | -13.63426 | -47.42643 | 2025-05-30 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d1273a3-816b-3322-8a75-0b3d7f99523a | -12.82465 | -47.39814 | 2025-05-30 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b6c354a-a134-39b7-badd-6ad0c72bfc70 | -12.29711 | -50.08513 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8b0d4f3-1991-31b7-84d4-a57a1d20f339 | -15.36897 | -45.67252 | 2025-05-30 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aac543c8-c990-3b60-b7a1-00b90ea4da0f | -13.22533 | -49.83669 | 2025-05-30 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1529aec-047d-3947-9c55-ffd3d6da774f | -18.38283 | -44.51453 | 2025-05-30 03:55:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 820b4ba0-b3db-31f2-aae2-380e156487ba | -13.09965 | -52.29573 | 2025-05-30 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 296ada3c-6603-3c16-a65d-dc834c6600d9 | -12.06342 | -48.47054 | 2025-05-30 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33a65244-1d2d-399a-a15d-6404b8c5ce8f | -13.09173 | -52.04984 | 2025-05-30 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e38b044-19e6-3eb0-b287-72b6dd37877f | -13.22607 | -49.83461 | 2025-05-30 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32635266-983b-3d4b-9ce8-052ffbac00eb | -12.01083 | -49.52507 | 2025-05-30 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b6f6442a-848f-3b3e-8e2c-bc09f46edc67 | -14.85216 | -48.08625 | 2025-05-30 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb2ec760-e709-3219-84e4-fe3107567dd0 | -12.01705 | -49.52258 | 2025-05-30 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3884155a-52bd-3103-9079-53a04913458d | -16.58732 | -45.87917 | 2025-05-30 03:55:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e514a7e9-62c8-3878-9435-91dfc2915033 | -15.24401 | -47.46284 | 2025-05-30 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f130350e-7fcf-3cc7-943e-333bb9377947 | -15.07965 | -48.94671 | 2025-05-30 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efbecc3a-7228-3ebb-8865-e89b8e62a3a3 | -18.37921 | -44.51384 | 2025-05-30 03:55:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78166fa2-4321-3e9d-ac7a-ef3d51e5b60c | -14.84331 | -48.10678 | 2025-05-30 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e97b32b6-30a6-33f2-be4a-4cd588e6b4f6 | -12.30198 | -50.09029 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb0d4138-eb9d-35c1-a8c2-450c2d2c6fb9 | -15.36229 | -48.00435 | 2025-05-30 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ab0c69-0e9f-324d-b58f-af1545c978f7 | -12.2963 | -50.08912 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8593f552-e175-3c96-8745-7aa856585c6b | -12.29448 | -50.08883 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6ed4a73-b330-3eee-81b3-754257b7844b | -13.08975 | -52.04793 | 2025-05-30 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 982f4464-6834-39b9-a78d-793c398a2b74 | -13.09599 | -52.04959 | 2025-05-30 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43fd1d3d-b5d3-3cb6-8416-336d00b24721 | -16.58832 | -45.87948 | 2025-05-30 03:55:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38c83059-5147-3bca-a9e4-03ec378e1d02 | -14.86047 | -48.09464 | 2025-05-30 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02be22cb-e232-3227-8480-15cddc1872d0 | -17.09432 | -43.80502 | 2025-05-30 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82488a79-1695-3267-afec-297d3ac3d5b2 | -17.75616 | -42.89484 | 2025-05-30 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d09c4f9-a677-3a0d-a28b-71994483b0b5 | -16.37591 | -43.0407 | 2025-05-30 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25c0e29f-a6a0-326c-a5d0-8710b548b5af | -16.68201 | -43.88298 | 2025-05-30 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6deb0313-328a-3e96-b2eb-79c89fe4fbfb | -13.53389 | -43.67747 | 2025-05-30 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8773ee7-c558-3ffe-ac1a-4d52d28d0f95 | -14.86149 | -48.08922 | 2025-05-30 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e620038-7a3c-3219-a4a0-84288681c664 | -13.00342 | -42.66687 | 2025-05-30 03:55:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7893af74-e2cd-388c-b81c-bbc56efe5288 | -15.57014 | -47.85542 | 2025-05-30 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9536de66-059b-328e-a054-10341834bf4c | -16.51989 | -43.0663 | 2025-05-30 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4723820-d3db-3e00-9c0a-db676af040b7 | -17.47754 | -43.32414 | 2025-05-30 03:55:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14ea66de-8e7c-3b6e-ad5d-5d4e5909ae6e | -13.53019 | -43.6768 | 2025-05-30 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31ca1471-683a-32a1-9849-c81e5d040ee9 | -13.62867 | -47.43044 | 2025-05-30 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88848fd4-142e-30c5-ae18-c680af073c10 | -12.81994 | -47.39715 | 2025-05-30 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a3c971e-65cb-3b78-bb3e-2137e59d5720 | -19.45409 | -44.314 | 2025-05-30 03:55:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77ccd520-0985-3658-82ee-16d780f39b92 | -12.30015 | -50.09001 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61cc0ae8-bc58-3ca8-a11f-fafb24eedbf4 | -12.02325 | -49.52012 | 2025-05-30 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c7668d8-be6f-3688-9300-478d1892b196 | -12.82138 | -47.39456 | 2025-05-30 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5df29c4-6aa1-37e9-8a38-0d1650ebe8ca | -16.04288 | -43.80056 | 2025-05-30 03:55:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cc83caf-6511-35aa-8fba-83b4bf53e8fd | -12.06282 | -48.47371 | 2025-05-30 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd8ff238-a10b-3c91-b42f-b84374b72dd9 | -14.85992 | -48.09689 | 2025-05-30 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd717d98-83f2-34db-8c47-dccb35546b05 | -17.95775 | -44.41064 | 2025-05-30 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ec4c2e4-6684-3fd2-847c-5b97a3003cc3 | -14.85117 | -48.09146 | 2025-05-30 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8f14209-648f-3caf-9205-a310f60d0308 | -12.8204 | -47.39967 | 2025-05-30 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 822df2a9-ce6e-3efd-b021-680e5954b2d4 | -12.40159 | -50.00379 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 278d51a6-2bbd-318c-9a76-8732c469e05b | -13.53311 | -43.68196 | 2025-05-30 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e300e04f-8627-3434-aed5-31bc4f61d0f0 | -16.02978 | -43.68336 | 2025-05-30 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7758f6-9a8e-3db8-be16-3d879d599a24 | -13.53681 | -43.68262 | 2025-05-30 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 2d2cdee9-4ddb-34f9-9678-1638d2b125b7 | -14.86098 | -48.09154 | 2025-05-30 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a698931-7080-32fb-991a-10deff97fce7 | -13.22058 | -49.83345 | 2025-05-30 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0c750ab-4d6c-3e9a-b123-1c8658095f7b | -12.597 | -48.37272 | 2025-05-30 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 506f7c97-6d2b-378d-9d77-482c67df6871 | -13.63337 | -47.43119 | 2025-05-30 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b895c550-3f80-3a90-baec-b54c7da978af | -14.84533 | -48.09614 | 2025-05-30 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a37279cc-dac4-3eba-882e-a0bd653ed0f1 | -14.85947 | -48.09992 | 2025-05-30 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6c8ab71-e49d-3169-aa7a-d5ee0e050329 | -13.52941 | -43.68129 | 2025-05-30 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee880ebe-02a4-3e34-9dfb-a21038291c2b | -14.0838 | -41.6719 | 2025-05-30 03:55:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8b56671f-08bc-308b-a14f-c9f7d1c15a48 | -16.51642 | -43.06566 | 2025-05-30 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 683a8547-d15a-3ea6-a995-171124c2ea2c | -13.10079 | -52.29029 | 2025-05-30 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57c15187-6e06-32f1-a84e-a498a080b9d5 | -15.3252 | -43.07309 | 2025-05-30 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7393566d-95eb-39ff-9531-ffc297b72ae7 | -17.47911 | -43.32368 | 2025-05-30 03:55:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af0be40a-55e3-35cb-936c-de3b027c9548 | -13.10192 | -52.28485 | 2025-05-30 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c4be662-6fc6-3258-a037-19ea392d7263 | -14.83851 | -48.10598 | 2025-05-30 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f59e66bf-fc0e-37d3-8ca0-31be52ab02e3 | -13.22607 | -49.83303 | 2025-05-30 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbe80b54-5388-3804-a71d-041242c17663 | -13.22058 | -49.83189 | 2025-05-30 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49d4565c-67e9-381b-99f3-e62c9ab7b798 | -15.37233 | -45.67699 | 2025-05-30 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4305fd03-ed96-3ae2-ab15-42a8cc0015cd | -12.39016 | -49.97248 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ebc706d-d601-3f84-9f0e-3a458a9f5e92 | -15.90984 | -43.45623 | 2025-05-30 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5f2970a-c312-37a9-9120-d44456dcb6a2 | -13.09797 | -52.05148 | 2025-05-30 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 352bee80-166e-33af-8d83-7e918e90848a | -12.30093 | -50.08602 | 2025-05-30 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd7c8e2e-f488-3c96-8ba0-635c065a17cb | -15.90914 | -43.46041 | 2025-05-30 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 384ea54b-d66c-379d-bed9-48fb05930d04 | -15.36333 | -47.99899 | 2025-05-30 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 684918ea-ad79-3ee6-b19b-294801489775 | -20.41646 | -43.55313 | 2025-05-30 03:55:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 20a8fe27-4dc0-367d-a509-81037b2c8d88 | -22.87447 | -48.64548 | 2025-05-30 03:57:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0502186f-2ae9-3ae5-a548-10a95f8bf006 | -23.40533 | -46.55375 | 2025-05-30 03:57:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a76dc0f-e607-3b2b-b168-4f52ff08207f | -23.64095 | -48.08543 | 2025-05-30 03:57:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba5b2d1d-dab0-3a4a-ae1c-c3baa58edaa3 | -22.46097 | -48.05891 | 2025-05-30 03:57:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb144cf5-6560-379b-9c71-af17e31906ce | -22.91961 | -45.41365 | 2025-05-30 03:57:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b9af978b-b3ef-3d7b-bd8f-2bb252104674 | -22.53997 | -48.81338 | 2025-05-30 03:57:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1577b93-0073-3bd0-9221-0333f3fa005d | -23.36894 | -46.03095 | 2025-05-30 03:57:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 352646b3-c30c-3e62-a183-da25e2211770 | -22.22892 | -50.86072 | 2025-05-30 03:57:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 74714fef-1b07-3056-8a64-8a9569b106b9 | -20.99554 | -51.79377 | 2025-05-30 03:57:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f368e16a-f67b-37bf-9a91-d6cf38bb5e09 | -23.28373 | -50.8959 | 2025-05-30 03:57:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 538a228a-18e8-385b-9a5d-58a5dc9808d2 | -25.19275 | -49.32756 | 2025-05-30 03:57:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 82efab38-f3ae-3da8-a765-ae1581dfc1c8 | -23.98301 | -48.91784 | 2025-05-30 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a6e1ec2-4350-37cf-b9ee-f50291b0fb8d | -13.5261 | -43.6797 | 2025-05-30 04:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |


[Clique aqui para ver as próximas entradas](README7.md)
