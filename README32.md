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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c5abfe-f014-35a1-b384-e5bde61f4f07 | -13.22694 | -51.65564 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9350fbbd-6d5e-3f01-a5e0-87ab7f1f7172 | -15.58198 | -48.82187 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89864dd0-007c-3922-9d99-8384faca8596 | -15.26937 | -42.78027 | 2026-09-15 04:17:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a3112893-775d-3c56-bf70-0704f7bc595f | -15.16482 | -43.84024 | 2026-09-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 254d9cfc-626a-3f8d-859e-d8a237a87fb3 | -15.58741 | -48.79341 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5717de5-b7c7-3cb5-abb8-6697103ed57f | -16.04839 | -52.27797 | 2026-09-15 04:17:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a504bc00-5a8c-3bd1-8f43-c6afcd96cf32 | -16.70333 | -41.30295 | 2026-09-15 04:17:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 07592e9f-2aba-331e-91a7-4e517fb211a3 | -13.2726 | -51.28167 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 444992f2-e57b-3eb9-8501-a107d565d962 | -13.56886 | -47.90427 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27a53e5f-f31b-3ca0-a366-ccd81f07d2fc | -15.53892 | -48.81997 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b70a758-66d0-3a68-a9f3-efbf91a4ce83 | -13.59578 | -47.90462 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3af0d61c-001d-32f5-aa28-f08d3bd132e6 | -15.44994 | -44.84457 | 2026-09-15 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8a1385-20a0-37de-814a-12d25469d0bb | -15.54307 | -48.79772 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a14dbb62-1207-3895-ba7b-039936f25c59 | -15.5793 | -48.78762 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d37f549-76de-3f4c-ac0b-bed621a1c0ca | -17.98125 | -44.33585 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c6b8f9-74ef-302d-bec3-7a2601f22641 | -15.53854 | -48.79728 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92dd9df1-6ac4-39e2-b3d7-3ce88a37870c | -14.76776 | -42.94611 | 2026-09-15 04:17:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4efce37d-05cd-3873-beb1-5846c8b21be4 | -18.86902 | -42.00343 | 2026-09-15 04:17:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e0a684bd-4df4-3f81-8c01-3ec9f18f6b12 | -15.25147 | -40.99134 | 2026-09-15 04:17:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fc7b6c50-eed1-3fc6-88b1-13a60fcef224 | -17.9819 | -44.33199 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25bd2225-d444-3bdb-9371-ce266e7745bf | -14.85807 | -49.94774 | 2026-09-15 04:17:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 477d9402-fb7e-317d-9678-7607353aa826 | -14.16124 | -47.39697 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a90bf1dc-0ffd-3270-aba4-7e7e5b15e625 | -14.85249 | -48.13932 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55efcabf-2f11-3661-a51e-0d16d94b14d8 | -15.9827 | -43.0137 | 2026-09-15 04:17:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 969f3c89-06f1-3e45-a82f-2a542d99f01a | -14.22675 | -47.42109 | 2026-09-15 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f0a83d5-fd41-382b-a97d-c9cf20a2d5dd | -15.28547 | -42.78681 | 2026-09-15 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 145b4e89-a955-35ef-a96b-3113477b56c4 | -15.53412 | -48.79626 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 181732ac-3a8b-39c5-872d-2d53373339b5 | -15.55147 | -48.82698 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23ee334a-2e6e-3f1d-879a-3be990b138be | -14.95756 | -47.52582 | 2026-09-15 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46fdc4f7-3a12-3d1e-aabd-cf3a02f2f02c | -17.47354 | -43.6674 | 2026-09-15 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e669916-e554-3338-8e7a-32326be7e11a | -16.56469 | -51.6254 | 2026-09-15 04:17:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| def486a5-b54f-384c-9592-052b0d1e6c7a | -14.20875 | -47.42526 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bcdc9632-244b-3920-a51e-370378419e98 | -13.261 | -51.28293 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d2e9ec7-1e72-3c3e-b78d-a9ee7a5b1f90 | -18.17271 | -51.76183 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5bfb275-6338-315b-b3f7-48ed98818f2c | -13.56965 | -47.90005 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1983b2df-beba-380c-8bee-26ab22d91538 | -15.04467 | -48.55731 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40388322-6785-3aeb-902e-4d895bb15760 | -14.85676 | -48.1404 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 30a71238-d1ad-3fe3-9cd7-1cf7f7a94d13 | -15.54927 | -48.82379 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| de245961-f4db-39fd-bd6e-d12f7f987845 | -14.66952 | -48.00525 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 170a17d0-6759-3b93-9a85-8ee39852aa83 | -18.8718 | -42.00769 | 2026-09-15 04:17:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9da3c554-a095-30d5-9b5f-41d7a1d4846b | -15.03307 | -48.52805 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03e57e81-efcb-37a3-a163-24d22b07f1f3 | -16.50547 | -47.81802 | 2026-09-15 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40e8b972-6901-3ddd-a25b-5c351e4d20ba | -16.97034 | -43.36741 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d6eddb6-f0a5-3f98-a3e5-c19fcd72792f | -14.99875 | -48.51604 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 751fa334-7470-35c2-8d09-d0e190b7f9fd | -15.50165 | -48.55627 | 2026-09-15 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb9df6cd-5fbe-347d-ba42-a130525690ad | -15.16825 | -43.84084 | 2026-09-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c16e49bf-0b4b-3600-a28c-34aa41eb8964 | -16.79928 | -47.61042 | 2026-09-15 04:17:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a9cae4-fb95-3060-9ee5-bf317ec6a3c7 | -16.48257 | -43.41988 | 2026-09-15 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39365c69-d443-3c3c-8060-8a5cdb8c4987 | -17.66166 | -43.09256 | 2026-09-15 04:17:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b1d99b8-8703-3528-91b9-6b11d34fb04f | -15.57846 | -48.81614 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e058716-0416-3be8-8e32-d3ececb7604d | -17.98531 | -44.33257 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b786ac89-7811-390d-b930-debbd5cef5a1 | -14.68234 | -48.00798 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1624c73-40fb-3f72-95e3-5dc4ba7f4cbf | -15.53335 | -41.78167 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c2b7929f-6c19-3085-a845-67c84c1ac14b | -18.16498 | -51.7733 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51c18ca6-2ddb-33e7-beee-9de1c6de1bea | -15.04511 | -48.58669 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 493fd55d-7061-30d2-83b5-d48cbb63e439 | -15.04999 | -48.55351 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41951555-ec06-37e7-8be2-62f975ad9b88 | -18.1714 | -51.76818 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4abc31f-9cac-3f4b-aa89-2462f3384ec6 | -16.97094 | -43.3637 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82943df4-22ee-3ecb-8eb0-95bcee1dcf7e | -15.58006 | -48.78369 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63db0ce5-ea18-30f7-99f9-b71786e099a6 | -13.69994 | -51.81027 | 2026-09-15 04:17:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76cbaec2-26eb-3f08-9e6b-ef319808ca8c | -15.0492 | -48.58146 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1207456-bf9e-3275-9f03-d05a7a5a388f | -15.36152 | -53.00058 | 2026-09-15 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f696fdf4-b33a-31c1-99a6-0f18141af7fe | -15.57753 | -48.82098 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36d5e478-021d-3ccd-8b76-b319c5f26bb4 | -14.21104 | -47.38948 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3519e8da-8f59-3d33-851e-224bab653ed1 | -16.9676 | -43.36308 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76114a67-b240-3e6f-b678-1c390395e33b | -14.84188 | -42.40519 | 2026-09-15 04:17:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8e5e0597-cd8f-32b1-934b-b36819f7a8ce | -13.34984 | -51.71239 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c096b367-88d4-3a4e-a706-da3d8e1e0676 | -14.20394 | -47.42794 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d7c0b379-3742-3258-b372-730eb1e0f79b | -14.22608 | -47.42474 | 2026-09-15 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bab65ccb-7f80-3a8a-904e-4877ccedf916 | -14.19497 | -47.42986 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14d4e731-e767-34ba-b0b9-4aae74010a4a | -14.6943 | -48.01544 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49992a0c-0ea6-3535-b6f1-6f7355f10746 | -14.17504 | -47.416 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1662a1e6-3587-39bb-84dc-30a58d8ac6ac | -13.62525 | -47.91553 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6af0a6c-e312-39ca-9352-597da25de3fc | -13.60009 | -47.90562 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb8e20a7-cbd3-3ebd-a5fc-2d185dd2738b | -15.04936 | -48.56361 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4706bec-1606-3839-8c4d-db8282b45370 | -18.82813 | -44.51881 | 2026-09-15 04:17:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a4be6b2-b0c5-35e4-965a-d0136761bed8 | -14.19981 | -47.42696 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| be7b8837-f1f8-3abf-82d6-cdd3cfd9e544 | -15.17103 | -43.84526 | 2026-09-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e19c6551-a03d-3ea6-8850-a33c460c70c6 | -15.25761 | -40.99612 | 2026-09-15 04:17:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b28c03db-bb83-3597-9b3f-c34bf8cb6c47 | -13.70072 | -51.80643 | 2026-09-15 04:17:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b883836-6dbf-31ae-a897-92b0c73f6d5e | -13.30383 | -51.29578 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d0df119c-4885-3e77-bdc6-99d8a86370d4 | -15.03394 | -48.5234 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02462187-86aa-3da1-be2e-6be6386148cb | -17.31734 | -46.91185 | 2026-09-15 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4523a0fb-1084-3a96-91b0-2893816f96e6 | -15.53928 | -48.80378 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecc5b6f2-f673-32d3-8e2f-b99b6ea627a5 | -13.29435 | -51.28633 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36ebf925-28b3-30d2-a71f-b31f7dfe1359 | -17.98937 | -44.32931 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 447db7cb-d60d-39d6-b966-52881720c1d9 | -16.97155 | -43.36 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93c0ea79-9c61-3efe-b236-e512381f694e | -14.20466 | -47.42408 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 91a3b510-c769-38f5-9472-212f751f32f9 | -15.98938 | -43.27847 | 2026-09-15 04:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b818d31-37b0-345e-8bcf-7cddedb53125 | -13.58019 | -47.91592 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a31aa69-03ab-3a3f-839d-9e0b310e766f | -15.35169 | -48.09707 | 2026-09-15 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b9c5c1c-9fbe-354e-80d2-3c27b8c888b6 | -15.54703 | -48.82603 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeb2c886-d3e4-3622-880f-de5ea801f06a | -17.31073 | -49.23272 | 2026-09-15 04:17:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05f1cfa2-db90-3ce7-8bf0-645d301d7279 | -18.76546 | -43.21595 | 2026-09-15 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 97eae8d9-4f99-32ab-98f3-7fd448b721f9 | -14.2226 | -47.42021 | 2026-09-15 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11669b89-76ba-3bf4-8c45-15d0ced2a536 | -13.23174 | -51.66074 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2736a2d3-ac93-3c12-a9d3-06835b23b1b5 | -13.56533 | -47.89908 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86831c8a-046a-30c8-a88f-a45dd6016706 | -15.04829 | -48.58621 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b26071f8-3374-3ac3-a934-ea5cd2b169c9 | -15.54119 | -48.81775 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a931e70-b66d-3248-8e20-42c83030d40c | -18.82473 | -44.51817 | 2026-09-15 04:17:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README33.md)
