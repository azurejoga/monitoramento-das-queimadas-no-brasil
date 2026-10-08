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

## Dados Diários - Página 336

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8527297-2528-3c6d-9e96-8a2d66533d94 | -11.77172 | -45.52828 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d1e22515-ba7f-34f3-875a-d48ae80adf81 | -11.07862 | -44.0344 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| f6628076-8ee4-3a8d-aac2-2c5d32c63f1b | -12.61318 | -44.54253 | 2026-10-08 16:37:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 1f91f35f-20a9-3238-9d96-8c57d6068ae1 | -9.14831 | -49.92407 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2c617035-f806-3c6b-8c55-18c8e3ef4278 | -7.78862 | -44.57761 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3b33882e-b8c7-3ec5-a814-49598f0a2665 | -8.10858 | -47.66674 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1e35ecb2-deea-34d6-a0dd-219beced1657 | -11.58814 | -43.66516 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5d5823bd-7183-3349-a30d-6c7f894197fd | -9.75193 | -46.95728 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2496fedf-d155-3660-ba4b-825fe681b475 | -13.29428 | -41.51981 | 2026-10-08 16:37:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 2e20bf98-13f6-30f1-a3ad-c24c1cf7fc91 | -11.70585 | -47.97268 | 2026-10-08 16:37:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fbd1f4f4-ac4f-350a-b9d7-1f8d5f4266be | -9.94682 | -45.97651 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd542ecc-d80f-3f5a-b427-2f8ecdb6f3a6 | -7.25033 | -43.76278 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 68498137-0ba9-3f49-8ae4-05f8435c1b70 | -11.08805 | -44.02925 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 45f689c6-9d19-3cf4-a0a1-d782c137de38 | -9.82629 | -45.76098 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 4223fb94-d1c1-38c6-8e49-6fa2d1db0485 | -6.29826 | -37.50466 | 2026-10-08 16:37:00 | NOAA-20 | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c68fdb38-35cc-3bfd-9f99-41cf9ad8cac8 | -10.94262 | -45.38155 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| dc211e84-ea63-3e98-b681-e8a1dba33bc7 | -9.13228 | -45.83614 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| d5df6cdf-c5fe-31f6-bd97-8da34cad7473 | -10.76573 | -46.57599 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7786a38d-1a66-3284-aa21-17f0964ebe83 | -9.83353 | -47.48271 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b713788c-21e9-37ba-b733-35d6a3abb6ac | -9.70626 | -42.80791 | 2026-10-08 16:37:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 294ed170-e029-3ddd-8781-5676becd1901 | -12.33003 | -47.09091 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e34835c5-725f-372b-a5bf-aff4d9a4b97a | -7.04904 | -44.33709 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 199afbde-e386-3b57-bc30-a4729f77da12 | -8.99786 | -50.80294 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2747930f-c17a-3a6a-a196-15b61ec72a98 | -7.4651 | -42.85855 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0d1dac27-98a6-3736-8244-b519888cf5ab | -12.24398 | -44.74731 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 10edb77a-2a2e-33fc-abb5-0bb0783ac2fc | -6.31251 | -45.06074 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1b934d44-4cbf-3c75-9f04-c48966f86e46 | -9.92 | -44.79426 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4efbdf6f-1e7e-32db-a77a-b1f88407f26f | -11.6283 | -43.70294 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 1946d732-2370-3074-baa5-8ca940223022 | -7.31833 | -43.99543 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0b1a0407-2b57-33b1-b917-6bf9f2d15848 | -6.20372 | -40.80281 | 2026-10-08 16:37:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3da9307f-4e99-3c49-a883-7f09da11c519 | -6.03436 | -42.7138 | 2026-10-08 16:37:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f1c64574-7460-3be4-b320-2b730ec1d136 | -10.80725 | -47.34044 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 38761891-ecf5-34fd-8479-ed0393cd43a6 | -13.12726 | -46.36997 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 59b5a9e9-741c-3d49-b726-70d86ddcba7a | -7.29167 | -46.15962 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 15e6f540-e22c-342e-afe5-5a26d2262b3b | -7.70041 | -45.43392 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 187ae419-b293-3355-9c6a-639e6f82f9c3 | -10.96795 | -45.39201 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| df211085-7fc4-3559-9672-bcb8333c481b | -6.05841 | -44.02877 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7ca94a94-754c-32a9-9a69-a6f5af33fa83 | -11.21053 | -44.86749 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ae91a1ef-1998-3bb3-b6c1-ea560538ed99 | -9.82182 | -45.68624 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b4ac91ce-5ec4-34f7-966c-57491a3fde4c | -12.61041 | -44.54658 | 2026-10-08 16:37:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| fd67edad-caa6-3cd0-b2f2-cd65dfb632b9 | -8.96675 | -45.12744 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 501ed059-fca6-3a64-80e8-d72f5ddea272 | -7.27712 | -47.25445 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 15d333ce-cf59-3ce2-b4b1-0623db1bd138 | -8.77609 | -47.26385 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a119192a-8b2f-32a8-9ec9-011aeb457f0b | -7.18885 | -44.33728 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8059e93-346f-387b-84f7-567a132042ca | -8.61242 | -44.87676 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b5bcb626-1f59-3e42-ae70-5ae458c64eec | -11.76306 | -45.49323 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6cd16038-5eb5-3ae1-90f2-d652ba15b0f4 | -6.92998 | -45.25833 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6be3828e-3571-3a93-9b11-68eb255b1ed9 | -8.08841 | -45.62032 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22487881-2e2d-391b-9bb5-62048a138ae9 | -11.96489 | -47.76991 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 33aa8819-92cf-3d04-ac6c-ef3cd665fd5c | -9.90505 | -44.80732 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c04810a5-558d-3c33-87c1-c04b79d6fa1b | -7.16838 | -41.9913 | 2026-10-08 16:37:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f4105e3f-9d3f-3c91-b6ce-8b260ae789b0 | -8.35287 | -47.66894 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 668f24b3-14be-3612-bcef-b33088d3bfb2 | -9.02529 | -44.38457 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3384ad72-fcd4-3c43-82a5-6d545720ff48 | -6.30707 | -37.70034 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8671fa68-2016-39fc-8ec4-f5fc1c404e31 | -18.05655 | -43.80383 | 2026-10-08 16:37:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b58bef07-adb5-3554-866e-e796d4db9c31 | -6.31693 | -43.49244 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63ac5eda-610c-3d7f-9ea1-5226f3299523 | -11.84932 | -47.38787 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 253b87cf-ac94-3654-8923-24e16112dc56 | -6.52944 | -45.39047 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 71ee4d76-0beb-3c1c-896d-d7c06e8f2418 | -12.17644 | -44.81556 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| cc2e07cc-7a44-3de4-8b30-16a9c03e007f | -13.53072 | -56.59301 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 143f3fe2-321c-3b2b-954c-933e7ff59944 | -7.39553 | -44.46933 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c3317427-bda0-3b91-85e0-ed8647e123da | -11.24818 | -45.2493 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93f88ecd-de37-3a6f-831a-6b56e38a00ba | -10.86926 | -45.54815 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3ca6e550-a3be-3847-bfb0-31ae0acb8386 | -12.23682 | -44.74483 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9b3d73e3-d8dd-3d32-b2e2-7677bf64eaf3 | -7.04623 | -44.34125 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 530683a1-83a7-3142-b3bb-f0c6d0847ae9 | -11.82025 | -40.49087 | 2026-10-08 16:37:00 | NOAA-20 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 38afafe1-09a7-35d4-a93b-3c10b82900d7 | -11.25256 | -45.25579 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bdc0ad3e-6a45-3c39-9dcc-a1a3c6371380 | -11.59982 | -43.65221 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e274c267-d09a-3e37-bba6-7a4f57214938 | -9.01082 | -45.12768 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c824adb3-ef85-3302-aacb-4e380f9fc89b | -7.13486 | -41.81045 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 4871ba8d-0a7c-3757-959a-5e7d897317d7 | -18.12937 | -45.20312 | 2026-10-08 16:37:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc48ebbc-7385-3f72-bf30-1a094504cb95 | -6.6994 | -47.38737 | 2026-10-08 16:37:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 12a834f1-6f3b-3aae-8ae3-db75b98ea0d2 | -6.61705 | -44.92181 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 94f1aa13-2b6f-3356-a7a1-219d987b2d34 | -6.32866 | -43.82818 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 388723bb-446e-3468-84ab-955cc32c8a23 | -8.19199 | -46.37148 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 888fb519-54c4-3b16-bc17-4ebf53ec39c7 | -9.34762 | -45.42234 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cff61c03-d633-34b1-b0e7-fd9ddf1935df | -9.93665 | -43.5724 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 693edefd-e270-39d2-8a5e-7f30f075b068 | -9.94629 | -45.97298 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9fcb2478-e5ae-3f03-84be-bd0fa78f399e | -18.05287 | -44.60204 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8cc6a35-1d50-341e-abeb-28ed77d9cf06 | -13.12794 | -53.79266 | 2026-10-08 16:37:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0f0abc44-36ee-3670-82ee-4fa06080e291 | -11.00641 | -45.42199 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ca530fbd-0f59-3271-8c32-50cc28a76869 | -11.80609 | -47.31237 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cfdad47f-7065-3832-ba38-f0cf9e90d58a | -9.79882 | -44.77808 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 524a34d7-df84-3a63-9416-dbadcc1754a8 | -10.49967 | -47.3133 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| f93ae7c6-235c-31b7-ac09-943045160058 | -7.12857 | -44.0825 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee3ed35b-9aa2-3ac1-83bf-3e3f19d6b318 | -13.01336 | -47.77502 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0167514-6ea3-3238-9909-68c57db9835e | -6.15077 | -39.4385 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 151d6943-9214-35f8-8404-7cd838f0ccc6 | -5.82002 | -42.49989 | 2026-10-08 16:37:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2579c03a-1cec-369f-8c67-8c4e77461001 | -8.96335 | -45.14936 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b7eef7a9-b0b7-36f6-90d2-c9b13ce4b48b | -9.51098 | -46.84284 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ef10635-88ac-3a46-94a8-29359709cf9a | -6.854 | -41.75298 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 4861de7f-aab1-39d3-b93c-216d06f86b12 | -19.24047 | -40.44443 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0642bd1b-fdc8-3f4b-a525-8ceefa9b03a4 | -12.21299 | -37.80579 | 2026-10-08 16:37:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f67cd332-1f64-3950-87d7-fc58475c0bd3 | -11.20559 | -45.21399 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| bb9634d6-d819-351f-a599-5b71fa84f26d | -5.70258 | -41.73417 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e0d45c57-a541-3cc4-bd5f-fa36f4310890 | -6.45543 | -46.01625 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c28a8238-be0c-3698-b88d-5ffbd35ef928 | -11.48006 | -54.62213 | 2026-10-08 16:37:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 51329126-fc4a-31cf-9029-b4dfae407cb0 | -5.74507 | -41.72746 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| e7415fd7-7fe1-3b1c-b190-e7b4104dab43 | -10.97126 | -45.39148 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| edbcaa3e-4496-384f-afd4-9ea7bda2a65f | -14.35855 | -55.02988 | 2026-10-08 16:37:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README337.md)
