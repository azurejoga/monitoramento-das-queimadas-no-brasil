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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8b30f29-9888-3b7f-89fd-44638725d9e2 | -22.8926 | -45.08577 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ba0a5d2f-40fc-3efd-8708-c371c61858ba | -22.89228 | -45.08928 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 2389057a-e44d-3b2c-8a5e-c3f46107fe0a | -22.89197 | -45.09258 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| a38f93b5-c15e-3ce4-8a0c-c1e062a114fc | -22.8911 | -45.1018 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| db2a6226-af73-3bb6-8a46-56a93b9e4ced | -22.89082 | -45.10481 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82a62782-5b76-3213-93b9-1d992c3f3569 | -22.88696 | -45.08821 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 5434a1fa-3609-3998-9fda-8b469c042e38 | -22.88466 | -45.11276 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1af061c8-1b11-3b4e-ad77-a3cf31625860 | -22.78715 | -45.19433 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| eb3a59fb-4f3e-3c06-8530-1613108a166f | -22.77024 | -44.65452 | 2024-10-02 04:51:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2175a560-4b9d-3e5e-bb7b-087a40c88f5a | -22.76982 | -44.65895 | 2024-10-02 04:51:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 345c8ee3-5eab-3af5-be20-fd91c943b957 | -22.76474 | -44.65395 | 2024-10-02 04:51:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f001ac60-d7ad-382c-8ccf-8c73fa2cb38e | -19.39384 | -46.39981 | 2024-10-02 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a538e0ad-ba38-3f35-a259-742dad3a3eab | -18.92049 | -46.07842 | 2024-10-02 04:51:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5a5cda6-a58f-3fa4-a0ff-94f9ad9e56a1 | -20.5226 | -46.26714 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 92087619-23f5-3228-b3c4-18fc13aa9499 | -20.51182 | -46.32214 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8be1bc7a-8b24-3d93-ae32-601b7eb31a04 | -20.5038 | -46.30717 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9521263-aa2b-34b3-a005-4f51d7268973 | -19.66109 | -46.23883 | 2024-10-02 04:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 662b846c-2bee-3549-8585-b38df86956e2 | -20.53219 | -46.26884 | 2024-10-02 04:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 4b2e776f-e883-3d1e-a2c3-fc365b9b15dd | -20.53159 | -46.27439 | 2024-10-02 04:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6d9e4c5e-79da-381c-93f6-ae388b0c442a | -20.52622 | -46.2789 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c90ab2bb-473f-3b22-9fcb-f53f756e5b32 | -20.52563 | -46.28432 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 97c51265-d0fb-3d37-9356-08ee6deb6fc6 | -20.52265 | -46.31195 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5ed5dabb-d9c6-326b-9fca-f5804e731d35 | -20.52086 | -46.28329 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1fd97742-74e5-3c8d-b65a-eaeb0c62f43b | -20.50353 | -46.30854 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f05f6d1-1d5b-3dcb-ad1d-ffcf16b3462f | -20.34504 | -46.37958 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c281f2b9-77ab-3370-9dbf-3c49aebdbabd | -20.86738 | -45.25434 | 2024-10-02 04:51:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d1869186-1f5b-3401-a067-dd443d373980 | -20.86706 | -45.25748 | 2024-10-02 04:51:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9c5c42a1-4510-3513-9d38-7325fa2858a9 | -20.86255 | -45.25033 | 2024-10-02 04:51:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e9a71134-0a74-3f64-a6a2-a91f142ad054 | -20.86222 | -45.2536 | 2024-10-02 04:51:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c8b046b3-17b4-38f7-9ab1-5dab2ca00332 | -20.52736 | -46.26831 | 2024-10-02 04:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b3f1311f-9d44-3a19-96bd-b73d0c44f6fb | -20.52678 | -46.27369 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 18e0efdb-88ea-3f8d-b6d8-3114d9d60b04 | -20.52196 | -46.31835 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2022556a-7b03-31ad-b492-2b87fc98a46a | -20.52144 | -46.27792 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f34f8eaf-a326-3c0a-b1b6-177ce90db089 | -20.51656 | -46.32328 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df4843b2-2640-32d7-b027-98a605e32751 | -20.51596 | -46.32883 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cad9a3e3-534b-3b69-8d31-1367608b1cf6 | -20.51535 | -46.33446 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c46fa94c-48ca-371d-a657-d0be766cee47 | -20.51245 | -46.31621 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 229aed6e-09ea-3ced-aed8-7f5d34cd06d3 | -20.50832 | -46.30935 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 38aac023-b020-382a-a6e8-78f5a880ccb2 | -20.50414 | -46.30289 | 2024-10-02 04:51:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b89e8d6e-bd7b-3c4b-99bb-3a8e9dbd60a4 | -22.20606 | -46.00101 | 2024-10-02 04:51:00 | NOAA-21 | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f24f5f88-23d7-3cce-ba47-9f3c1859e85c | -23.6643 | -47.39892 | 2024-10-02 04:51:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 451650ba-792f-3799-b680-ac25e357dc8f | -23.50964 | -47.22194 | 2024-10-02 04:51:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 45941ed9-f014-3d76-847c-0fdc86910c49 | -23.50911 | -47.22704 | 2024-10-02 04:51:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bcb7cc77-dc9d-390e-bfba-998831cb7684 | -23.50858 | -47.23222 | 2024-10-02 04:51:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a93f42be-0887-33b7-a545-4ae9edb5fbbe | -23.50442 | -47.22638 | 2024-10-02 04:51:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9aeb88af-e497-3c02-a025-981563048c44 | -23.50079 | -47.2153 | 2024-10-02 04:51:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 2cc490d1-5945-305c-abd0-42e053ce1dd0 | -23.49901 | -47.21444 | 2024-10-02 04:51:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1ef6e5cd-9ba4-3232-84aa-e1d95d41a1c0 | -23.49843 | -47.21966 | 2024-10-02 04:51:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4420e865-e26b-3c3e-9203-2a939ed260e3 | -23.35564 | -47.01718 | 2024-10-02 04:51:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 8c311619-9d6c-3331-9477-ab8674a86b05 | -23.35091 | -47.0163 | 2024-10-02 04:51:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6c52e5bf-2085-3765-b797-d4a6417b28fe | -23.2807 | -46.66459 | 2024-10-02 04:51:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 337db40d-27a7-3135-acab-5049158bdebf | -23.25267 | -46.64962 | 2024-10-02 04:51:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 983ca4d7-825a-378c-863d-166cafa80958 | -23.23967 | -46.64778 | 2024-10-02 04:51:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e20bae26-2b7a-383b-aa49-01f38ac51722 | -23.22378 | -46.46905 | 2024-10-02 04:51:00 | NOAA-21 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd3cdb9a-c5f2-322e-b8ef-4b20b5354fe4 | -23.21887 | -46.46839 | 2024-10-02 04:51:00 | NOAA-21 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ed5902e4-d7c2-3f08-a7d2-0b3fedbfb203 | -23.15818 | -46.325 | 2024-10-02 04:51:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| a67da5c0-2927-3421-9c9e-b5bd3d7e430e | -23.15737 | -46.32358 | 2024-10-02 04:51:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| f3856e23-041a-332d-930a-78af4f38c384 | -23.09162 | -46.378 | 2024-10-02 04:51:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 31d10877-70f2-3f6b-9930-60e6a77e83e0 | -23.09109 | -46.38327 | 2024-10-02 04:51:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 083b84e2-039c-309b-94da-fa81f51890e6 | -23.03962 | -46.88467 | 2024-10-02 04:51:00 | NOAA-21 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 683f1578-00d8-3419-b2c2-ce327c4d98da | -23.03481 | -46.88438 | 2024-10-02 04:51:00 | NOAA-21 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| aed32d01-d7bb-3942-8c6b-48abd24cd5bb | -23.03001 | -46.88391 | 2024-10-02 04:51:00 | NOAA-21 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 32685c94-7c53-3338-a128-a9490ffa4afc | -22.77909 | -46.82158 | 2024-10-02 04:51:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ebed0d64-8fa0-3723-853e-b1a2d79e9d63 | -22.72076 | -46.68287 | 2024-10-02 04:51:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 258eb781-2e9e-3594-af61-165710df8e6e | -22.71593 | -46.68227 | 2024-10-02 04:51:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 44a1e115-6bce-3a32-8f1d-c7e26930d576 | -22.71543 | -46.68711 | 2024-10-02 04:51:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| ae35fbfb-897a-348e-aa57-15dcfcbd2721 | -23.66557 | -46.114 | 2024-10-02 04:51:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| febe6e2e-6ccb-3e65-9763-d4a516e9901f | -23.06795 | -45.90693 | 2024-10-02 04:51:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7621672-a8b0-37cd-bd5c-6e7fe99ecbb5 | -19.47714 | -46.88449 | 2024-10-02 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aa3c7f2-1484-3246-86b3-d3bac7d1d3c5 | -19.47661 | -46.88921 | 2024-10-02 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06fd39cb-f363-3e0a-8dbc-41acb38e1026 | -19.47257 | -46.88401 | 2024-10-02 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d91587da-b22f-3c3e-b7fe-a7cf7f546e56 | -19.47222 | -46.88165 | 2024-10-02 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2209b0a7-009b-312a-8aca-903e950576da | -19.47203 | -46.88877 | 2024-10-02 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71680183-5339-3adf-8808-8e90b2c9c922 | -19.47165 | -46.88636 | 2024-10-02 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09dac036-12b2-32da-ae49-09fec74a7ed0 | -19.23692 | -46.86174 | 2024-10-02 04:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f8646d47-e89d-3574-a30b-1c37a9da3392 | -19.23634 | -46.86659 | 2024-10-02 04:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| af35df6a-22ea-39a1-ad01-830d5ed88d14 | -19.23576 | -46.87141 | 2024-10-02 04:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bbca66e-c4da-35f2-8f6a-72dccf9675a2 | -19.23238 | -46.86106 | 2024-10-02 04:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 849cade7-6da2-33fa-a2ee-c4c8b147c2de | -19.03126 | -47.52393 | 2024-10-02 04:51:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39f06cd2-7482-375c-8ec6-6fbbabeb59e2 | -18.98293 | -47.29558 | 2024-10-02 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad3493ea-c090-3abf-80f3-3c4c0d19e6e6 | -18.98275 | -47.2985 | 2024-10-02 04:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fcfe55c-af9c-375f-afa0-2153c65b92d1 | -18.78443 | -46.62866 | 2024-10-02 04:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be0aeb85-6095-3267-a20e-130e67a64797 | -20.96348 | -46.88221 | 2024-10-02 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cdd24484-36ba-38ef-9b95-719def4dcbd7 | -20.96178 | -46.88287 | 2024-10-02 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc2391f5-e0ff-344d-a505-cd184579553c | -20.64693 | -47.04115 | 2024-10-02 04:51:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53350139-42a8-33d4-84a1-1fcb01797375 | -20.64637 | -47.04615 | 2024-10-02 04:51:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 828a0701-6f0f-3e07-b1f8-ce04df9d94e7 | -20.63079 | -46.77496 | 2024-10-02 04:51:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0225fd6e-949e-3ac6-85e5-6b83b4e6e65e | -20.6302 | -46.78014 | 2024-10-02 04:51:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e65aac5e-9ea5-3794-9374-aec140dad61e | -20.01262 | -47.36409 | 2024-10-02 04:51:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5eaa5dd-a06c-346e-91a4-0e62ac267716 | -19.9348 | -46.91427 | 2024-10-02 04:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f5d72bcd-5804-3208-888f-e8f14ff32aa8 | -19.93424 | -46.91916 | 2024-10-02 04:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2fd252ba-da67-3fe3-93d8-c6ff5bc3944b | -19.9302 | -46.91392 | 2024-10-02 04:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9225e6ce-a0e5-3d2f-8306-97372d198769 | -19.92964 | -46.91883 | 2024-10-02 04:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e805ebb3-c4de-35aa-af29-535adcf9636b | -19.76516 | -46.64764 | 2024-10-02 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 311be49f-5965-3aa7-a7d7-a6f6dfcd520b | -19.76461 | -46.61105 | 2024-10-02 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 999867d4-188c-3b70-ad15-fd0a8483e73e | -19.7605 | -46.64712 | 2024-10-02 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fac2439-53fb-3c12-9c67-fe6932bf7cc6 | -22.11098 | -48.46117 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c99a885-9cc8-370f-84b3-173479b12a69 | -22.102 | -48.46391 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 218872b4-5ded-3249-8f24-30ec929df5d6 | -22.09775 | -48.46317 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c98a699-4a49-35fc-bae1-7ead3bc5dd0b | -22.09724 | -48.46758 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README120.md)
