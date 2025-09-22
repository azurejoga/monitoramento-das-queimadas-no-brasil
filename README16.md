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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36937426-dccb-31d2-9906-a8ea4d5b96ea | -6.05141 | -46.39637 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d06e1dc0-aa78-3260-9640-fca327400b2f | -14.2658 | -44.68055 | 2025-09-22 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad0119cc-b680-3e43-adee-92325a0420db | -14.32822 | -47.79751 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cec197f-dd4d-3616-8b68-ca4d5706fbd5 | -5.64321 | -45.94756 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2b85b84-46a8-39f2-8431-ac87f5bd6266 | -11.65973 | -47.48969 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cc71bb0-76aa-3cc3-a593-609d9e0acee4 | -11.96043 | -46.9284 | 2025-09-22 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 404991df-c470-3ffe-8c09-5db22c5f98b3 | -15.09666 | -43.83484 | 2025-09-22 04:17:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff55912e-5f50-3843-b4e4-ed5742bee5c2 | -14.34818 | -47.78796 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecccb397-7069-3abd-bb5a-e7f1edcb8d87 | -11.95796 | -44.90384 | 2025-09-22 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dfb6773-eae4-383d-a79f-1a3c2093e6a3 | -12.08314 | -44.79676 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e569aac2-850a-3329-acc5-c5fcd8ce553c | -11.27105 | -49.22889 | 2025-09-22 04:17:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 309373df-fecc-3631-82fb-2056a3c9e808 | -11.31733 | -54.34611 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8d0a799-05a2-3643-b5a2-5b6f4de1a384 | -11.3285 | -54.34867 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf8a6fe7-fc9c-33e6-83f7-d21e36259fee | -3.68304 | -45.38203 | 2025-09-22 04:17:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8756c11-2d11-3ed0-b827-0253ee70dec6 | -10.34214 | -52.5239 | 2025-09-22 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc3ff358-8770-3e7f-ac28-6425ad76c4d3 | -8.80275 | -43.06355 | 2025-09-22 04:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 36456b66-230a-36ea-9908-b93662da8de3 | -13.07923 | -47.01937 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89dd09b9-c8af-33ce-802b-8f752665aaf1 | -5.63827 | -45.95515 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4b449fc-f9e8-379e-914a-c9eeffe5ff7d | -7.47352 | -44.39286 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9db4c15-ec9b-384f-b522-f557f2261ae7 | -7.23201 | -43.76254 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d761af72-fda4-319b-ad96-d8ac8b1793d5 | -1.34289 | -47.74946 | 2025-09-22 04:17:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00987f73-6d8d-346d-9a00-c5160746c3ae | -13.06046 | -47.02412 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9516c7f5-34a6-30ce-9ab7-997bc5e128a5 | -7.23145 | -43.76602 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2091f7f2-1dfe-32a7-8cd6-068fbc3625b1 | -4.77446 | -43.72156 | 2025-09-22 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78afe346-fbb3-3197-b1d3-988d25cbfb6a | -12.09093 | -44.79076 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ace6f092-724a-3f3c-bfdb-5ee331f0ba00 | -7.28717 | -46.1166 | 2025-09-22 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3f515f6-bad5-3585-8324-cdf18286967f | -10.96444 | -49.57266 | 2025-09-22 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfac3319-9fe0-3038-9bdf-3298a98ac48d | -13.07573 | -47.01876 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8f87524-0330-3523-8fa0-009df83c532d | -6.61656 | -44.60228 | 2025-09-22 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a807d496-7cc6-3c18-8e22-77497b3a3a48 | -8.18574 | -42.3825 | 2025-09-22 04:17:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3b3c157c-9eaa-3349-be78-f46eb26bbe62 | -5.83674 | -49.0273 | 2025-09-22 04:17:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae962764-8d33-3a1f-92ab-1aa3e86d0440 | -3.51309 | -49.94313 | 2025-09-22 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 112467f9-6e1b-3691-a84e-b482963d4a2d | -14.64358 | -48.26947 | 2025-09-22 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 438965a8-9cb5-3fbd-977a-a2fb060c8201 | -7.95867 | -43.89246 | 2025-09-22 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a0530c3-530e-31cd-b249-4780e168780f | -8.01211 | -45.71705 | 2025-09-22 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 776b0402-62c7-3089-942a-a154e000b97f | -11.74614 | -54.72678 | 2025-09-22 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ce9abea-842d-3cb5-a900-030d129d5fe4 | -12.71558 | -47.69669 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e0439bea-ad3b-3ef1-8d30-9082ccf23f4a | -5.58876 | -46.25677 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77bce7f6-f739-3e76-a447-34c2e0cfd335 | -3.948 | -53.38754 | 2025-09-22 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9578da30-6058-3d09-9919-d50aa0b56691 | -7.94138 | -44.10884 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c6383df-89bd-3a4b-8f44-8fe61dc9f5fb | -12.9674 | -46.38482 | 2025-09-22 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e128a9a-7dce-3ee7-8630-3b3648630aac | -14.44028 | -46.52325 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90afce07-e899-3c4f-ba53-f30dbb29c9c0 | -3.32635 | -50.09353 | 2025-09-22 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3105eedf-51f7-3a6b-bd65-a0f399c7db0a | -5.56677 | -42.13283 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 77f98ee3-beca-3d15-b2a4-aac1843541d2 | -0.94459 | -47.35262 | 2025-09-22 04:17:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f1b87ae-3f50-3d5c-b516-0b68d9e31c3b | -14.23079 | -44.32294 | 2025-09-22 04:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aebaa764-f39f-357f-8e09-1e1fa02f5dd2 | -12.42938 | -45.1345 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde0c920-3ec1-30f6-a4ed-fb0e6ee26600 | -12.73003 | -47.72113 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d552dd32-0c08-37ee-86b5-5852b920f43d | -11.31248 | -54.34102 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c91962db-99ca-31c8-b34b-7443147f0dd3 | -5.11199 | -46.16471 | 2025-09-22 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 326e4ab1-3cf1-310f-9d7e-8a054fa6acde | -14.84302 | -45.13762 | 2025-09-22 04:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eb75b06-3787-3b30-8c98-3f3c40af8ee1 | -7.3647 | -44.55481 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 518e7e1b-a8f6-34a4-ad4a-76b85a4784c5 | -11.21889 | -49.59853 | 2025-09-22 04:17:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 368e2d76-af2e-319a-9786-9bd2fcfa0124 | -14.97405 | -44.43152 | 2025-09-22 04:17:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51d5ac91-22b6-3123-bd60-680e72310670 | -8.8033 | -43.06003 | 2025-09-22 04:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c17c4edd-7315-3d4c-9aea-4865739a5243 | -11.73448 | -47.79877 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ffeb598-93b2-3d3a-ad8c-ea0d8ee038c1 | -13.61903 | -47.41838 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c05045f1-86a3-350d-9219-ee86528620db | -14.11735 | -44.01311 | 2025-09-22 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5af945a-8db3-3528-a698-a4fbe3aeca9c | -14.98074 | -44.41043 | 2025-09-22 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b3b7b76-9673-37c2-be08-78eeaa758367 | -12.72481 | -46.83134 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfaf7167-2b8e-3ea3-b7e3-ac62dfc7de06 | -8.80719 | -43.05704 | 2025-09-22 04:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 36c995a5-2b05-31df-a932-2dd539e9a9c8 | -5.64918 | -51.46418 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef06d78-3765-3d96-b106-4da0e7093a77 | -6.45589 | -45.68034 | 2025-09-22 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6723ecd5-0df8-3dea-8408-6054803eedc4 | -7.35516 | -44.54963 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ce881a4-5861-346e-a027-8c8e93b17a88 | -7.96747 | -43.64339 | 2025-09-22 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4476597f-8e3c-3da1-84a7-332adf316596 | -2.9143 | -40.39043 | 2025-09-22 04:17:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d212c717-39f6-3562-a380-617524da9f09 | -3.05248 | -46.92725 | 2025-09-22 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d9cd658-6763-38e7-adf7-d9d515828f55 | -7.36586 | -44.54765 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 736d6d6d-2871-3666-ac55-e56ff332ce40 | -11.72094 | -47.45782 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b48c2b9-14e2-355a-81da-6763cc4dd258 | -7.6133 | -44.48475 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 63e31ec4-2be3-3aae-b93a-20f977761b74 | -11.64194 | -44.31954 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 948fab38-7565-3d52-92e9-a23d7c9afd41 | -7.35259 | -44.60834 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 152ee297-3fc9-3df4-98ef-7105d8d7b074 | -12.69024 | -46.83831 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 047b389c-72f7-36c0-ae39-58638b279cee | -7.62741 | -46.82333 | 2025-09-22 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c20aa834-35d2-3686-9a12-c5b43b4876db | -7.93248 | -44.1002 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2916f103-ea66-34b0-ac89-e14813b4fc16 | -11.28532 | -47.51745 | 2025-09-22 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c5b27b1-21a4-3910-b7e4-e3384fe4b83f | -13.74855 | -47.84304 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6827ab7-ffc8-3641-a71c-c087f7d93a81 | -8.30044 | -43.67888 | 2025-09-22 04:17:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 507f8038-1215-3244-9276-684ffadf9e54 | -12.96226 | -46.943 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21b68f1b-291d-3e9a-9658-1b9c67c97aff | -11.78071 | -43.76227 | 2025-09-22 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 174544c5-9cf1-3b84-a847-7682bf0b2d51 | -6.09357 | -41.00315 | 2025-09-22 04:17:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0c72a33-6880-379c-a7ca-1f4b35090a73 | -11.22102 | -46.16544 | 2025-09-22 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 553232cc-bc76-38f0-a4cd-523856860659 | -12.72829 | -46.83193 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 112e5f39-ce33-314d-9ddd-a98468be3faa | -7.16673 | -44.43907 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb80229f-54dc-3f21-a35b-8d6448b32057 | -7.51364 | -43.68907 | 2025-09-22 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2ac7d4e9-1803-3e34-b490-673ef3fd2ad2 | -7.50976 | -43.69203 | 2025-09-22 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd23a0ad-b2ff-3ddf-bfcf-a3f0c3d82652 | -7.36354 | -44.56203 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 591959b1-cb16-39c2-8003-68ab7f22691c | -11.31807 | -54.34226 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f70780f4-0838-3080-a39d-6f86d15030e7 | -0.94877 | -47.35329 | 2025-09-22 04:17:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 700e5dcc-edcf-3273-8dce-df7fec40aa51 | -12.71197 | -47.69604 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9b56f35-1f51-3de3-9de9-d6b4c33feacb | -5.64187 | -45.95576 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 573d6914-0b5e-3fb2-a9c8-cee327dccbc5 | -2.26388 | -47.84669 | 2025-09-22 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a574e6f-320d-3888-b8dc-bc7745ed9c13 | -13.07857 | -47.0233 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 925e6d1d-f77b-32fd-8065-4a1071eb95c7 | -15.09329 | -43.8343 | 2025-09-22 04:17:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fc83b84-b329-377e-918b-963ecbaa24de | -5.64806 | -44.06242 | 2025-09-22 04:17:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b02454bf-b4df-3dc2-92f1-bcaff0cfa56b | -14.39885 | -48.55868 | 2025-09-22 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 361845ad-dc29-3025-87a8-df76e3c46128 | -7.35458 | -44.55323 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4ea0f56-de6d-38dc-9d88-9030e144c03a | -5.4209 | -51.45064 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebd8a075-8b4f-367b-8129-7c80dd0bac7b | -14.44089 | -46.51954 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ca3bc15-2fa3-34a1-8a48-58d35751ae78 | -11.46441 | -46.93859 | 2025-09-22 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
