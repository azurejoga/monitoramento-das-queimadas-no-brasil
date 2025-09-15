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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9763a48d-7917-3c3b-b11c-97aa6c140c34 | -7.8417 | -46.11357 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4e04dbf2-0917-3274-80b9-6dc02d914ece | -7.98704 | -45.67321 | 2025-09-15 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e2f0216c-00c0-3e0d-a441-99e424e9535b | -8.91409 | -45.50518 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 179c686b-dfe4-3927-a008-ce67210d35dd | -8.42366 | -47.22744 | 2025-09-15 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| aa388c62-4677-3f38-9118-e39c077be8c8 | -7.7061 | -44.67398 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3cc2129f-3d52-331a-a008-73cc46e1eed8 | -10.93661 | -45.52444 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f1cab13f-8eb5-3db8-953e-eb35b085f2fa | -11.79035 | -46.65326 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7c496d9c-beaa-380d-af50-d072c734529f | -10.92689 | -45.58767 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 717f9e0c-d62c-3a22-8d51-f849363d27fb | -10.63887 | -44.21648 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5a5d7388-ea9a-3803-8bda-e55fd7bd87a9 | -7.70225 | -48.862 | 2025-09-15 00:33:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 54a9a7bd-e490-30cb-aba9-b5368a9e38db | -8.60389 | -46.35349 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a8491bbe-d1ee-3c46-a898-318f9d543519 | -11.46526 | -43.59008 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ec1deec5-337b-3941-9b0a-3cdb28243ccb | -6.40776 | -46.93075 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 36c5384b-edff-340e-a505-206565e74eb1 | -5.69264 | -49.2046 | 2025-09-15 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d0f5d2b9-8b95-377d-b3ae-5cf180c3f28f | -12.67299 | -54.72075 | 2025-09-15 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8ecfd3bd-abf8-3e1a-9f83-d36fa7f39eaa | -10.78211 | -45.97919 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9dc2a56b-8e45-3958-8e9e-d35bb39b683a | -6.98297 | -44.55048 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e6dd8ebe-2d33-3cac-95da-3b017dd2e45d | -7.50547 | -44.3761 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0e4eb3a6-a1db-384e-93b1-9cbc98a6deb8 | -10.92583 | -45.51586 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d06d5fd1-c4e9-31b0-bca7-c1efa0b650ee | -8.07278 | -44.51762 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2f08da21-03f6-3f23-b1da-22e7222973b6 | -7.86812 | -43.58815 | 2025-09-15 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 398.9 |
| f8d8e4c1-657c-3502-9316-98efa91f2f6e | -11.66753 | -46.50012 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6576986b-3715-314f-b648-93cc640c3467 | -7.85476 | -43.57528 | 2025-09-15 00:33:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 9fb06b4c-4d9c-335c-a809-396bd85ad7ba | -11.34745 | -43.49464 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a44700fd-4411-3d57-a68e-e76cb036e954 | -7.40182 | -49.9763 | 2025-09-15 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 47e39be3-9ee8-38ab-9755-30e6107c1421 | -11.12753 | -45.30669 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 864f5739-0ab8-36f5-a006-b23d30699121 | -11.33899 | -43.50949 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0561d310-45c2-3780-985e-372a23af2470 | -9.01822 | -47.06084 | 2025-09-15 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 32086466-4f3f-3d11-84b9-07b650c94608 | -10.72397 | -44.77896 | 2025-09-15 00:33:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 39cc497a-4035-3543-8a88-943c5d380e1d | -6.69172 | -45.5106 | 2025-09-15 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 505abb99-714f-39cb-bcc5-fff9f6398a55 | -8.59609 | -46.36449 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6f9f369b-78e9-388b-9aa7-c50bfbfa3363 | -8.97798 | -45.81197 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3ad7204f-4dc4-360f-95a6-c6802e7a21e5 | -6.40912 | -46.94025 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| b199abee-2fae-3f56-a664-916fbcfcfebb | -5.11257 | -46.13217 | 2025-09-15 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3acd81d4-4d64-3d5d-b7a9-45f19268598f | -9.01512 | -48.03206 | 2025-09-15 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5af934b1-a96d-3f18-9212-5d9c731e9e46 | -5.75372 | -43.92314 | 2025-09-15 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 95f90ede-46f9-3111-af98-0bae2915384e | -12.0043 | -46.65829 | 2025-09-15 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| f6e25300-6ffa-32fb-a2ce-6b4adbb7315c | -6.91784 | -46.16708 | 2025-09-15 00:33:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fa0907d8-4e00-3307-ae29-026023c1baf5 | -6.16757 | -48.10526 | 2025-09-15 00:33:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84a2d9cd-ea62-3d9d-b65b-dbd2a279f4e8 | -8.97174 | -46.21479 | 2025-09-15 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14cb17c5-ce67-3d7a-b326-b69be2751480 | -10.66334 | -46.2467 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bc64f0a4-140a-3fcc-ab1e-5f7b23c951d5 | -9.47054 | -40.3585 | 2025-09-15 00:33:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 8274f4a9-c919-3e57-9f76-a9e0161f156d | -7.85462 | -43.58165 | 2025-09-15 00:33:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 266.1 |
| bb5424d6-4dac-3389-950a-7ac42eadb74e | -11.43626 | -43.54165 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| afd4af71-5c9b-3a8e-a1dd-f0324b69ac6d | -7.99733 | -44.84566 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a00c7fb1-8d32-38a7-8067-de5209f640ac | -9.05006 | -47.0285 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07484f3d-20c2-3266-88c2-a384c358b6f1 | -8.6407 | -47.00053 | 2025-09-15 00:33:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 55356868-4381-3355-97e8-f287ea8912c6 | -9.55179 | -45.95465 | 2025-09-15 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 57c256f8-f97e-3a75-8012-0e0a2a3255e2 | -5.70024 | -49.19453 | 2025-09-15 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 992b4e53-e495-377d-b5ed-698224311e12 | -6.10402 | -43.72325 | 2025-09-15 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 90e55d4c-a999-3d95-9456-c44881dac92f | -11.33397 | -43.51675 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 25b168fa-f965-317c-9c92-bb6265e56810 | -7.40309 | -49.98573 | 2025-09-15 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 78c0d133-ec60-378a-9907-65a121998022 | -11.7711 | -47.56173 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 2350bf53-799b-3ac2-aae1-5c72d9d203f0 | -5.93049 | -44.86793 | 2025-09-15 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d3fbc2b5-02d4-3c98-826c-1bd0da849489 | -9.0577 | -47.01804 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 462399d2-e454-3935-9396-cb0206506052 | -8.10813 | -50.15823 | 2025-09-15 00:33:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 96a5cd62-3522-31ea-b492-c627c547715f | -12.05102 | -46.53967 | 2025-09-15 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3891884c-9ac0-36e5-b19b-fed78e1493ae | -12.16917 | -47.57977 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 55145307-62a1-3786-8d51-ce8820c33819 | -8.61864 | -45.74384 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e3d90c7c-398d-3367-88a6-526479e8b028 | -10.65292 | -46.23859 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4a58dc8a-99c0-3d79-8088-b3ce03a00ef7 | -8.97007 | -45.82354 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a4d78d54-fae0-339e-8dfb-1cf344eb8eb3 | -9.54539 | -45.97584 | 2025-09-15 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 161df789-68de-3898-bd5f-b12b2e71dc9f | -10.74709 | -46.51095 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 34148ec3-3532-3601-9f61-48fcbee27a39 | -8.7909 | -46.05721 | 2025-09-15 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 477cef18-3095-3b03-b2db-ea9178b0f5f6 | -5.28337 | -45.26541 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f83826b3-5f3e-3d96-a48b-98a576e4408b | -8.64256 | -46.37098 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 70e24671-0069-30c9-9ab2-a5b078948e16 | -12.17041 | -47.58875 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 44d93543-e8ed-38de-9cff-d7203a61ca7b | -6.9193 | -46.17733 | 2025-09-15 00:33:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3d06afa8-a4ac-3270-8266-e76250adc4fb | -5.39527 | -42.82767 | 2025-09-15 00:33:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f2ca004e-b2ef-3665-9306-2b115451fa43 | -9.5468 | -45.98567 | 2025-09-15 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| dd36b205-98d3-367d-b9a8-7d3976f4d354 | -7.90455 | -46.24014 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5db41636-5c84-3fe6-b576-84534923a371 | -8.41475 | -47.22873 | 2025-09-15 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0de21a99-3cf4-3c90-850f-ba1d28c4109e | -7.39272 | -49.97754 | 2025-09-15 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7e363063-8adb-366a-ab43-dcd19b221483 | -11.76241 | -46.64805 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 80aa94d4-064c-3596-b5ad-a1ddb5999850 | -11.12903 | -45.31705 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ad4d3702-fa34-3962-807e-0bbddc15ded8 | -10.73419 | -46.48458 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 42dc84f9-cbee-316b-8fad-bd9cecf8b824 | -7.6441 | -49.72374 | 2025-09-15 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 831db2db-54ee-36ce-ac26-78d721ca26a7 | -4.10986 | -51.09283 | 2025-09-15 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3d5dcad2-bdaa-34be-b718-3da2dd6c7782 | -4.46548 | -48.8501 | 2025-09-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 110b1a80-20ec-3c95-9a2a-83cb4ef20e5b | -2.92218 | -49.56123 | 2025-09-15 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dece4ed3-3683-3322-81e4-d301c0b95f63 | -3.90973 | -47.7167 | 2025-09-15 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ee7b40f-c14b-3d94-af62-4bda6d5880e1 | -3.83475 | -50.77168 | 2025-09-15 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd195d24-1d08-3da7-8c4a-c92fc4becbe9 | -4.03581 | -51.03361 | 2025-09-15 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a914c9ea-c34e-3064-959a-6f092be5d431 | -2.92732 | -51.93905 | 2025-09-15 00:35:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f1a83e4-53e1-3efa-a91a-6b6b68045720 | -4.13765 | -48.82227 | 2025-09-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 28123102-4b34-3be9-9ebb-1f6949c8539d | -3.42411 | -47.60685 | 2025-09-15 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c8077d4b-a194-3258-a9c8-2c9dd5b2dc12 | -4.17783 | -48.57689 | 2025-09-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 53a1a06f-515a-39e7-9e69-632c1bb9b244 | -1.95584 | -48.11905 | 2025-09-15 00:35:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9029a6ef-c76a-3517-83f1-7e05c7d8b538 | -3.59658 | -47.52181 | 2025-09-15 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05d049f9-d1e4-3a21-965e-216c3632e910 | -3.52667 | -52.86946 | 2025-09-15 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 41743f75-9522-3fd2-8367-cca718ecf396 | -3.64522 | -54.06002 | 2025-09-15 00:35:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a84781a9-a8db-3f52-b7f0-1f553abe6541 | 0.75593 | -50.77183 | 2025-09-15 00:35:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d33da0d0-4857-38b4-82a1-38e5d7dd09ef | -2.95534 | -51.28619 | 2025-09-15 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e6dae420-4df3-379a-ba6b-870edd38795e | -3.07856 | -48.82338 | 2025-09-15 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 857a8545-92ce-3f89-b47d-8d62dfd2a8aa | -4.13643 | -48.81348 | 2025-09-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 566303b3-ed9f-3895-8d57-70f43526bf77 | -4.1766 | -48.56805 | 2025-09-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b335b59f-d818-3245-a450-f0002a16d8bb | -3.51947 | -52.75365 | 2025-09-15 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6687113f-ecc0-32a1-b7b5-31cd57ad8a0d | -3.32211 | -49.05461 | 2025-09-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5c5bfa17-c66e-396e-b8b4-06b6c0cce961 | -3.3898 | -50.14754 | 2025-09-15 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 176f8c23-d98a-3be6-89b2-95236d1fd238 | -3.48757 | -52.813 | 2025-09-15 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README6.md)
