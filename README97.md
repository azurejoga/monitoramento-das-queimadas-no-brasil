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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b96bd9b0-6d57-33e0-91eb-1f720487d1a8 | -11.65649 | -43.60144 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f1809d1b-450f-32ee-bcb1-e729c3fe2dd9 | -11.31693 | -44.26206 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| fa04092f-2e94-35c6-9274-3e2f34182912 | -11.806 | -43.57439 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9be119b6-2f64-3b82-9703-83837d5823cd | -11.81098 | -43.57294 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 18007449-1224-3561-ba4d-9bf8ae361f7f | -11.26753 | -43.51688 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 949669fb-01dc-33f2-81e0-8b7986ab20dc | -11.71197 | -43.51481 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| df4c120b-8311-3836-8ae5-ac7e0142d594 | -11.27425 | -43.56797 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8e0abbb6-8cdc-3bd5-ab30-ec43daef9bc9 | -11.65685 | -43.60431 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 781a774e-a969-367f-9324-a9cef728cc0f | -12.89708 | -44.72993 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 1014ce15-017e-3496-80fa-d1a838f5d4ed | -11.61937 | -38.04787 | 2026-10-02 15:54:00 | NOAA-21 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab847ed9-424a-37ed-bbbe-cc83b45902c7 | -10.92696 | -43.84288 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8ac2a4ef-5170-3c47-8867-63ab6f5c492a | -11.4987 | -43.52238 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 492.7 |
| 32fa8f4c-c808-36ad-8da8-fa870896d0f1 | -11.72474 | -43.45472 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bb68765b-3c3e-3aed-a71f-dd9acc2c4bf9 | -11.39199 | -43.36426 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 23465adc-6043-3b21-97a6-19aee27e8813 | -11.79343 | -43.55601 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 29c8574d-768f-394a-9c55-0b19ed576158 | -7.07907 | -35.12832 | 2026-10-02 15:54:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 09da9e73-2e43-358d-a991-b263330e9d61 | -12.5367 | -43.09326 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| b37a9c20-fed1-398a-9d07-a3a1e00e9c99 | -11.72124 | -43.50777 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8219ceeb-057b-3ca5-b0be-ee2140b9fd54 | -11.65828 | -43.61556 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a3e8c55d-7565-35ce-925b-ee1e8cfa7baa | -12.4898 | -44.15295 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 351.5 |
| 227287b1-ed10-3c9a-996c-15f4d294f7c4 | -12.78887 | -45.14523 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| abd2c687-b8da-3013-9a58-0a1ac6f89dd1 | -11.40187 | -43.40276 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| cfa41c02-e03c-355c-9955-8952fd827743 | -11.80347 | -43.55485 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 36b23a14-b497-3997-be2f-87af03688238 | -12.77353 | -43.27695 | 2026-10-02 15:54:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 75dc95ec-112b-3071-9299-eff44d91b8a5 | -12.54578 | -43.08611 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 363.0 |
| 19e04a9a-6e33-38fd-8fd0-7f1381189cb3 | -11.15721 | -44.60599 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0ff3ac4b-7c6c-37e2-9518-bfe4d2a720c8 | -12.50439 | -44.14117 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 5246d683-12bd-3799-b0f4-e7eb51bb87ae | -11.72666 | -43.59247 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5573ca39-5245-3eb0-88e0-81b15f9d1e8f | -11.79626 | -43.57803 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c9712892-eef7-3b8d-be54-425efb32767c | -10.00112 | -43.43103 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bd4ebcb7-633b-3a41-8e75-a6eed6bbf4b1 | -7.11612 | -43.15247 | 2026-10-02 15:54:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| f6d97cbd-7072-3a50-8aed-59d8d3d8be8f | -11.1387 | -44.58798 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 15d56b6f-9297-3a04-8d72-84cf2b370358 | -11.74542 | -43.53867 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 00eca03f-a158-327d-affe-18baebcabe84 | -7.36684 | -44.64481 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a577db4f-366d-3ef4-9b1f-ac1671e2e020 | -11.41193 | -43.52221 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1cc233fe-8197-3ff9-9c1d-e130156a8209 | -11.85633 | -44.74903 | 2026-10-02 15:54:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4b04c99d-bec3-3c71-9329-91588346b959 | -8.56494 | -44.13376 | 2026-10-02 15:54:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 24ed3e17-a1d8-35fb-9a5b-099c8c21a33e | -8.79259 | -45.81143 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 928d4009-ba6c-32f4-a501-1e19b0979c8d | -12.78189 | -45.13446 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| fffc0357-f540-3358-a75e-2ce161172efd | -12.17978 | -40.57751 | 2026-10-02 15:54:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| da39b3cb-8618-32c8-99ab-9afee727219d | -12.48454 | -44.15362 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 351.5 |
| 342ec5c0-115b-3d20-9fa7-3c045b4ed924 | -10.90561 | -43.83634 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bfdd4637-35a5-33ed-a3af-685d51edcbfc | -8.16893 | -39.67052 | 2026-10-02 15:54:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 23ea43d7-7aad-3b9b-b085-36d193418f42 | -11.4725 | -43.4056 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 005ed26f-526e-3874-a132-2d0ac321a342 | -11.73678 | -43.42997 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a3ac80c8-d5b0-3dae-a4a3-bd03f5bd3019 | -11.66828 | -43.61391 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 5ddde84d-0713-36eb-b7bd-551c44caa4ea | -11.80991 | -43.56422 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1da705db-a0a4-3fd7-9b13-83796e26092b | -11.70135 | -43.59404 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 20911e53-9cc3-3826-b0c4-fed1c64c0a38 | -11.29481 | -44.25491 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b03ea550-f2db-39fe-94fe-033c55700a91 | -11.11735 | -44.59036 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f321b59-3d82-33e4-a80d-33cdae5ba5b9 | -13.36115 | -43.84714 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 0d84cf24-7647-3018-93e1-c834a3094034 | -12.78019 | -41.83427 | 2026-10-02 15:54:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e2628399-38f8-3ce2-90da-af72c1771b41 | -11.66758 | -43.60844 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 653c89f8-625b-310b-bae0-9776532d6800 | -8.5691 | -44.12723 | 2026-10-02 15:54:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| c52a2cb4-4cbf-3716-a9e8-3fc0097c5148 | -11.598 | -43.54563 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1164d57f-183d-3c45-be4f-1295476324b8 | -11.72416 | -43.61359 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7c3ca988-cae2-3b8d-a5e0-7879baf4456c | -7.61461 | -40.31652 | 2026-10-02 15:54:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 02c82499-7c24-3c92-9cf4-e194563c1e8e | -11.3121 | -44.2659 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 2cc14bce-4b00-37fa-89eb-8e6230c84058 | -12.32394 | -46.36988 | 2026-10-02 15:54:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70bbe002-7ba8-3497-aed8-c1ee9a4a91f9 | -12.51564 | -44.14586 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 2b99e70c-1428-3120-92d2-32df138734f0 | -12.17691 | -44.66103 | 2026-10-02 15:54:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 3570dc0b-73a2-350c-a998-4f827f9267a3 | -9.94101 | -43.45202 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d86bb077-4c21-3828-9a28-54634d247698 | -13.34993 | -43.8419 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 923df592-0902-3e64-ba46-8d43f04bc879 | -11.4683 | -43.41183 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 50debebe-81e2-3b62-b2be-aeffba7f9c19 | -11.15187 | -44.60659 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05ed5a59-9f56-3cf4-a617-3f86caf85ac1 | -12.78931 | -45.14899 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d495eb56-ad6d-324d-81de-68902061796b | -11.914 | -41.57624 | 2026-10-02 15:54:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| e0760b00-c61f-38fc-ac7b-e54609324444 | -12.50562 | -44.15104 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| fc84a1ef-5480-3cae-af83-abd43f876318 | -9.58592 | -35.66758 | 2026-10-02 15:54:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3180c33d-17cb-3f08-86cf-3efb8a2c2db0 | -11.28958 | -44.25555 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f78c34cb-6aec-3b2d-80d2-1ff4078f5a69 | -13.10555 | -43.49411 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a0e3cd88-26a3-3f07-a559-99bc3f775260 | -11.65576 | -43.59563 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ff5bc0b9-c772-3433-b4a9-71ab38bfa099 | -13.1081 | -43.51537 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1520f526-ec23-388f-aa67-c89f185b4531 | -11.80521 | -43.56834 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 69f54435-590a-36cb-980d-f4685b03b3c6 | -12.51575 | -44.1465 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 7d69e802-eea1-35c5-b757-d1e4077006fb | -13.35592 | -43.84775 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 1eb8d4a0-031d-39c8-b2d1-0107e6c059c9 | -9.71605 | -38.13648 | 2026-10-02 15:54:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| caf40782-0f89-3adc-ae4d-9ec727a5f7ba | -12.42123 | -40.64631 | 2026-10-02 15:54:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8906999b-6d40-31e0-b34f-3fa6653afd62 | -11.65465 | -43.5869 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bef12f8a-c8ee-3e06-bd39-5e18a719814b | -12.52615 | -43.08863 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 41.2 |
| ebfcb7e9-7eee-325c-886b-384a5aee9555 | -11.71068 | -43.58698 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f3e2eb68-b01c-351f-99b3-da9c98b779c7 | -11.67763 | -43.60718 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e3140eb-c19f-3ca7-b92d-ceec733a65a9 | -13.34546 | -43.84898 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 7653522c-7dfe-39eb-a412-e0183ae8ac33 | -11.47967 | -43.42188 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| d110bf07-73a3-3979-86f6-5c9ed57e07f6 | -8.1222 | -44.8 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8887849b-7ad8-36e1-99ce-f9f26548e522 | -11.8035 | -43.55344 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b92f9bf1-67f7-39b5-a3b1-2d2757b41f34 | -11.46755 | -43.40618 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| dd1c687c-0eca-3542-8709-fd98ee9f1579 | -11.48462 | -43.42125 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| f43d0a0f-f776-349c-bf80-617acb9bcd91 | -11.70914 | -43.61604 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7d079802-e730-3ed4-8996-16c6a5170f19 | -13.36268 | -43.86021 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ab6d2a34-2c5d-37ee-8082-aee77a56f870 | -11.71465 | -43.57779 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d889c0bc-ed1f-33aa-b264-d8caaa2f1e13 | -12.50398 | -44.13788 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| bfbb8f1b-5060-34c2-a5bb-c271b6f91521 | -13.34061 | -43.8529 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e2bb3406-913c-31b9-af38-5c7acddb60e7 | -11.3117 | -44.26268 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 574141a8-fd96-3e16-9157-82b171d32761 | -11.72696 | -43.59495 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bdf4e672-72b7-3190-bdb5-5a8ba5009804 | -11.69629 | -43.59356 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 77605f74-0413-3bba-a4ea-9890fb39f878 | -11.72684 | -43.4312 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| f963e865-8dc6-3c97-b2b3-69c8fec202fa | -11.80449 | -43.5615 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| ad0b6b07-099c-3c18-a336-febd0a115817 | -10.30795 | -44.65349 | 2026-10-02 15:54:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0183afca-2c6d-3198-8f6a-3a4daa044733 | -11.69736 | -43.60182 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README98.md)
