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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae294958-347f-3d2c-bb22-d33b54ef711f | -6.60789 | -39.40293 | 2025-11-19 03:59:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3edbd406-5c6b-3380-bbec-5622350fcc4b | -3.59665 | -40.96661 | 2025-11-19 03:59:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bef12325-8146-373c-b0f0-cbb99b138706 | -6.81943 | -39.15779 | 2025-11-19 03:59:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| baed2eb6-1011-341c-8cbb-c4bc0dee4314 | -5.47731 | -44.69184 | 2025-11-19 03:59:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bab9d01-1954-317f-8247-b3125a8b7f77 | -6.75103 | -44.21301 | 2025-11-19 03:59:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4677714d-d7d4-3ef2-a466-7e1fec504c9d | -2.21986 | -44.81681 | 2025-11-19 03:59:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 027da447-368b-31f3-9f6f-653f96b870c4 | -4.75497 | -45.90215 | 2025-11-19 03:59:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44f0737f-aacc-31b0-a7da-e641b80cf6f5 | -4.58541 | -40.62523 | 2025-11-19 03:59:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38b7d116-6b0c-33d5-92c7-57ad4bba2bb1 | -7.75754 | -35.1111 | 2025-11-19 03:59:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5fe13908-25b6-3d51-addc-78152a3fbf61 | -5.75894 | -40.45538 | 2025-11-19 03:59:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 38e3f47b-4db0-32e5-926a-e77e9d5f617b | -4.35337 | -45.70767 | 2025-11-19 03:59:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e2075f5-9913-3a49-8715-08efe22189d6 | -3.35628 | -43.50167 | 2025-11-19 03:59:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3905e0d-1041-301d-9449-cd5d6f25a9c3 | -3.59323 | -40.96621 | 2025-11-19 03:59:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e6a4fb15-fadf-3bbe-b01b-8fd8bf1c9716 | -3.02283 | -44.45605 | 2025-11-19 03:59:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc071bbd-965a-3ffb-a619-5847e7202a94 | -2.97263 | -41.75648 | 2025-11-19 03:59:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 94ec861d-41ca-3680-8e5a-a5f2504f7342 | -6.18497 | -41.84979 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e319caf3-95e1-354d-b41a-91b2a02481bd | -4.58518 | -44.06509 | 2025-11-19 03:59:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 645248b5-d1c3-39e3-b3ef-08d20e065779 | -4.58126 | -44.06446 | 2025-11-19 03:59:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f99e4b57-dd1a-30b5-a15d-b6d102237a23 | -6.43705 | -39.27628 | 2025-11-19 03:59:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb088556-2b9c-37db-a9f4-ac428b202e23 | -3.42215 | -43.02142 | 2025-11-19 03:59:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38f4a868-81c9-3844-ad65-2873a20eb084 | -3.25005 | -43.29276 | 2025-11-19 03:59:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d1acabf-9ba5-3f91-a478-3d0d7a1286b4 | -3.5995 | -40.97059 | 2025-11-19 03:59:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6a029d5-c9e4-37e8-8ce3-ed4acf3c8c65 | -6.18373 | -42.03162 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f77939a7-f48f-3922-bb14-df112d42a8bc | -6.01078 | -36.30738 | 2025-11-19 03:59:00 | NOAA-21 | CERRO CORÁ | RIO GRANDE DO NORTE | Brasil | 2402709 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 212d202a-4bac-3903-8fa7-acb4fb576d62 | -6.1831 | -42.03546 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d18a180d-160e-3cbc-abe4-25c6b6a925f7 | -6.21638 | -39.6033 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ba67b14b-7446-397b-b62c-fded7b5a9bbb | -6.20356 | -39.39968 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| a924fd4e-610f-3688-8490-261452d3edb1 | -6.20302 | -39.40313 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0d781661-ff68-32ad-a5b0-d653b7093c2c | -6.6911 | -38.06463 | 2025-11-19 03:59:00 | NOAA-21 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ddc6fe9-4a96-3d26-b723-dfd3a8ebc25f | -2.972 | -41.76043 | 2025-11-19 03:59:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ad28688-c0f5-3e42-a0d8-e66be0aa36c3 | -6.19063 | -42.03276 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 238e3e2e-8d5a-3b0d-b847-23a657ea32fd | -2.29043 | -45.74326 | 2025-11-19 03:59:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 898ee487-61ed-3e8a-be6b-983bce482c69 | -7.75934 | -35.10781 | 2025-11-19 03:59:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 08121295-935e-3561-86fd-4da6168fd489 | -3.60046 | -40.97094 | 2025-11-19 03:59:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc6fd310-e5f7-33a0-9d00-167f54aca6d6 | -7.3404 | -40.02531 | 2025-11-19 03:59:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30113c46-4e21-3ea9-99e6-e5cdf17e30a2 | -4.69385 | -45.88753 | 2025-11-19 03:59:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3ac2a08-9969-3f81-af73-087554f74498 | -6.18718 | -42.03219 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90134ead-65f4-3d6c-bd95-a427b5e90e34 | -6.00204 | -39.5128 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5537f798-99b4-3095-b961-57e891803e60 | -2.98194 | -41.76602 | 2025-11-19 03:59:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ce2c959e-83e6-3656-9c4b-357587f360e1 | -6.21914 | -39.60727 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 708c1fae-da4f-3193-a11b-1a7e6950f632 | -4.16384 | -46.84393 | 2025-11-19 03:59:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca5f93ab-1407-358f-a166-504bbf626179 | -6.86045 | -44.84563 | 2025-11-19 03:59:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 434cbc67-1fe0-3b25-a131-c52f3612cdd4 | -3.02165 | -44.46346 | 2025-11-19 03:59:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fb503a7-58de-3ed5-b8a3-e37524b8be0b | -3.79995 | -38.45481 | 2025-11-19 03:59:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4f049a4-180f-3446-8136-13e94e42db95 | -5.61919 | -37.80489 | 2025-11-19 03:59:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ef964b76-db06-32fe-b4c2-df2e7ed20f3c | -6.66375 | -39.28367 | 2025-11-19 03:59:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20cfe5f8-e0a3-3de4-ba4d-db688914ac1e | -3.73796 | -45.60275 | 2025-11-19 03:59:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1c33eb0-d5e9-3335-aced-378e397dd00c | -7.75806 | -35.10759 | 2025-11-19 03:59:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e551712e-02d1-36ee-8f59-9234cbb7dade | -7.69444 | -38.68381 | 2025-11-19 03:59:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4f51853-83b5-309f-a285-f26e54357216 | -4.98671 | -44.75475 | 2025-11-19 03:59:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 668c5090-dc5b-31b9-b2a6-bb7ab20e27da | -7.16905 | -40.66212 | 2025-11-19 03:59:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3a5d800-c81b-3545-9d67-f83fdea2658f | -5.86612 | -44.67014 | 2025-11-19 03:59:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d85090d-9ddf-3b85-9665-b8c6962621a1 | -2.22477 | -44.81345 | 2025-11-19 03:59:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e0484e4c-8a4b-3cf8-acf6-0dadc8f6e6a3 | -6.47595 | -39.7681 | 2025-11-19 03:59:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| da4b2002-a0da-31a0-930f-757f8d159eed | -7.57997 | -37.75516 | 2025-11-19 03:59:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29e8331d-7e5d-3252-96a2-0516bb79f789 | -7.32798 | -40.17273 | 2025-11-19 03:59:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 41fe16bd-382e-3738-837b-a0c62113c3bf | -7.65762 | -39.7816 | 2025-11-19 03:59:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94356953-70c1-3784-99cd-3d0c31c0a90c | -6.39654 | -39.70929 | 2025-11-19 03:59:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6813b8b8-da30-3a60-9f71-a740e7f69317 | -6.72018 | -39.99105 | 2025-11-19 03:59:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 848cd752-7293-3917-9887-a17fed545cc7 | -4.48869 | -44.33089 | 2025-11-19 03:59:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48432ac6-1dc1-3284-bfff-7b217e1fc473 | -2.22414 | -44.81744 | 2025-11-19 03:59:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 707c5f66-c46a-321b-89b5-5f10343f6740 | -2.29159 | -45.74146 | 2025-11-19 03:59:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 567ed940-2f4d-3311-9dbd-8f2b5b344090 | -5.68567 | -38.59708 | 2025-11-19 03:59:00 | NOAA-21 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 866e4995-5e44-3ace-8f0a-5076b9634b59 | -4.99078 | -44.75542 | 2025-11-19 03:59:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d847d62-2b08-3adf-9d51-d071a27bc042 | -5.77331 | -42.50295 | 2025-11-19 03:59:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e541554-8f7e-3970-a903-929a360f1953 | -1.37947 | -45.79397 | 2025-11-19 03:59:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cd43c30-e5a1-31c2-95e2-d922c308614f | -3.02106 | -44.46716 | 2025-11-19 03:59:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aadfce7f-d490-3a00-a6d9-437295d52f03 | -6.89438 | -40.09257 | 2025-11-19 03:59:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9572995e-4c4f-3281-ad9d-707f6b10bd07 | -3.73724 | -45.60704 | 2025-11-19 03:59:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3249f4f1-063e-3cef-bacd-b039b64864ce | -3.56662 | -43.47204 | 2025-11-19 03:59:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a2e4bd7c-e419-3081-bb58-f4aaf0b0188a | -6.2041 | -39.39622 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 256abf19-64ca-3576-8ffb-3c3f2d38fcad | -6.17099 | -39.7163 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ea14ae0-6e20-31d9-ae31-d0134338d49a | -3.45423 | -40.5236 | 2025-11-19 03:59:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5e36af67-4154-3f3a-8cbf-187e0baa2e28 | -6.49799 | -39.77861 | 2025-11-19 03:59:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e0449ba-c3eb-3f32-b5b5-68d1850cd367 | -2.22359 | -44.81356 | 2025-11-19 03:59:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4ea525c2-6953-315e-a580-6c9488639cd0 | -4.16421 | -46.84601 | 2025-11-19 03:59:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02052f8f-49ae-3d6e-9d96-73ef6b448a31 | -3.41841 | -43.02081 | 2025-11-19 03:59:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5f2bb54-6149-30da-bb7f-ff10b742b67a | -5.83074 | -40.00142 | 2025-11-19 03:59:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e63639ca-0e2d-3fb7-9d63-bfc5a5148d0b | -6.44036 | -39.27679 | 2025-11-19 03:59:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 56537c26-668d-3a3f-b21d-1958278fbb49 | -6.15835 | -41.84195 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cb8db32-0e26-342f-8bb7-a5a76e12b03c | -4.98957 | -44.76273 | 2025-11-19 03:59:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3b838f9-4248-329c-92a0-27c23dd78161 | -4.99138 | -44.7518 | 2025-11-19 03:59:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ea90172-845e-3317-94d4-542780fcf8fd | -5.13497 | -39.48846 | 2025-11-19 03:59:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3ee06a84-ed36-35f2-b360-7ae7a7434984 | -5.75215 | -45.10616 | 2025-11-19 03:59:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7078b289-7f68-31d1-bb3d-73263c374719 | -1.38336 | -45.79945 | 2025-11-19 03:59:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 606d2160-04d5-3b74-b1d8-1b4a375b110c | -6.20633 | -39.40364 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fd9f33ff-97e4-3daa-80d4-e2914fd54356 | -1.37871 | -45.79876 | 2025-11-19 03:59:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21d34e11-f858-377f-8aa3-fc8e4fb2eedd | -5.83404 | -40.00194 | 2025-11-19 03:59:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8742b845-a69a-347f-9e7d-5203a785932c | -4.32839 | -40.40041 | 2025-11-19 03:59:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 56a35d7d-fb83-3518-83af-722bb817cfaf | -3.35321 | -43.49624 | 2025-11-19 03:59:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbecaa58-b890-3338-8f32-98bbaab630e5 | -6.64928 | -39.24572 | 2025-11-19 03:59:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 64d749e0-0b27-3d57-b837-9a9174e901ad | -3.46147 | -40.52129 | 2025-11-19 03:59:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aebcaf86-523f-3486-9bd9-685d8845c6f7 | -6.69507 | -38.06146 | 2025-11-19 03:59:00 | NOAA-21 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4592d61f-d6c7-3841-8445-d830fe152dc8 | -4.9861 | -44.7584 | 2025-11-19 03:59:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7094fa09-c29e-31c3-9fed-30be50f86160 | -4.58437 | -44.07009 | 2025-11-19 03:59:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e4eb9fcc-0784-3982-965f-02a5d9f0ed51 | -6.89384 | -40.09602 | 2025-11-19 03:59:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8772e2ba-2315-310c-bf03-6bdbd6c98528 | -4.58044 | -44.06946 | 2025-11-19 03:59:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90c1c892-e652-3cbf-ae39-aafadf799c93 | -7.31391 | -39.03738 | 2025-11-19 03:59:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fcf124de-aac0-33d0-b5b5-58360382fa2b | -4.58633 | -48.5369 | 2025-11-19 03:59:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa9d619f-8482-31e1-abb1-4d0abe85bcad | -6.94317 | -39.62965 | 2025-11-19 03:59:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
