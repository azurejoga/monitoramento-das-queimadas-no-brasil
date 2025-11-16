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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a514334-898b-3bd0-8b7e-204841bc488c | -7.30738 | -39.32844 | 2025-11-16 03:46:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9223b99-bfb8-3122-8e75-51f70d8edfc2 | -4.69897 | -46.31164 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 295343ae-84ba-3cfa-967e-a8bc2992bdb0 | -9.45465 | -44.86799 | 2025-11-16 03:46:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d367031-ac11-3fb7-a1de-13a4e3e7f61e | -5.53651 | -41.77074 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da46c84c-da08-3935-91f3-60b84ed43b00 | -3.99274 | -44.27447 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2284ee10-a58d-3a00-a5d9-a97e405e5a13 | -9.06201 | -44.74392 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 115b7a18-bba7-3911-b276-0799130c2b4e | -3.59098 | -41.6635 | 2025-11-16 03:46:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3d149876-7f4c-32ef-9d5a-c65972a69974 | -6.30446 | -43.79437 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| cbe1da7d-a498-3631-9988-38d653ea872a | -6.71213 | -42.94711 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd01f639-5bdf-390a-b635-a23df1fb5fdf | -6.70085 | -40.80565 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 81120b88-f606-38d3-9400-6a22cc853f8f | -7.19502 | -39.21501 | 2025-11-16 03:46:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d014b533-b3b9-38e1-8202-f3df968c7fca | -5.48204 | -44.83866 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8721082b-7276-372e-9d1f-6d9bdc1f2d9a | -7.41052 | -40.06984 | 2025-11-16 03:46:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5793af2d-f90e-38d0-a273-596b69b8d90d | -9.65829 | -43.90611 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0ca5199c-8711-3c2a-a03c-7d7f482be212 | -6.78131 | -43.5449 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26f258f2-c778-3e66-a28d-d3bd663dd7e3 | -7.0093 | -45.16854 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 946c39fb-45b0-3950-8f1f-b0533fca4e3e | -4.43095 | -43.41009 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2254cd00-4ea2-3d73-b0f6-feb3659ef005 | -10.16589 | -44.50628 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ca75407-1a04-37c9-9079-a4914027b0bd | -3.45211 | -46.12346 | 2025-11-16 03:46:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b99c0a7-0748-33fd-8c3d-79c2e809397c | -8.26249 | -40.97963 | 2025-11-16 03:46:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be9e9865-da1d-3454-9c21-74313acd4554 | -7.34535 | -43.34161 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48f417b9-c1a7-3eac-ae48-efbfcb17b019 | -6.31305 | -43.81373 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dbf9d5a-0da9-3e57-9fd9-166686e5ebdc | -9.73769 | -43.95214 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 129069a9-890a-3890-a0ab-0438454e1d9e | -4.73759 | -46.38446 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d556d236-ba19-3ea1-8577-4e6b6f645c8d | -7.40658 | -40.06916 | 2025-11-16 03:46:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7d69796f-cf14-3fb8-82a9-8146e08b7692 | -6.47867 | -39.77237 | 2025-11-16 03:46:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ce674ff-afe7-335c-908e-3bf49633ec4b | -6.16593 | -39.9212 | 2025-11-16 03:46:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e87283b0-d9ea-3c66-b59a-94d4bf7c1e9b | -7.19903 | -39.21317 | 2025-11-16 03:46:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| c778aa29-ad36-3d0b-9dab-a6469afd5915 | -3.66635 | -44.8215 | 2025-11-16 03:46:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fc6ba4c-1877-3f77-90d0-222abac32b94 | -6.08697 | -41.59773 | 2025-11-16 03:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c545c7e-f266-3f0e-8c2b-924243ece510 | -9.83342 | -44.18358 | 2025-11-16 03:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 545aa871-26d0-3f00-a2b3-62687f7378c4 | -7.19529 | -39.21249 | 2025-11-16 03:46:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e16c0d50-6b82-3350-b1b5-0cb26b530fd2 | -7.32469 | -39.0664 | 2025-11-16 03:46:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9dcfe25d-f5f3-32c7-adda-21715a472820 | -5.51367 | -40.97377 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e47d2cbb-4f97-3ea0-b6a5-5bb75adb0c46 | -10.18066 | -44.49886 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c38b38d4-77bb-3bb1-b605-d5bcafd7563a | -9.34896 | -46.58923 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7403a042-d106-3223-979b-6d7d26a2ec3f | -10.32671 | -44.60539 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ba28969-f2d0-38bd-953b-d486fb0567b7 | -5.48389 | -40.98225 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a51f7634-66cd-33ab-a25e-a8de3b1b1272 | -5.99075 | -41.91422 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42218033-47ad-3bf9-bbbf-732c3434d0c7 | -10.25312 | -45.06346 | 2025-11-16 03:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d18c2481-896c-37cd-9e42-b8ac9288b778 | -6.36145 | -46.1577 | 2025-11-16 03:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3edb4fe-85c0-3e22-af1b-e6907c744c44 | -7.13247 | -41.66455 | 2025-11-16 03:46:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0dc5cbf0-09d9-398d-b7d7-5d1b512ff94e | -5.46727 | -40.97545 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9df13ed1-0d3b-395b-81c5-e5249cdc1739 | -6.05211 | -46.61317 | 2025-11-16 03:46:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 556c3699-5a90-36ce-b390-81351794bdd4 | -3.82774 | -46.02586 | 2025-11-16 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c56677d-9476-3ef6-a372-2413c93242ac | -6.3546 | -46.16124 | 2025-11-16 03:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee1a608d-32c0-3768-ad53-27e723aceb64 | -2.52209 | -47.82418 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b53d5814-762c-3729-8e93-23ac32eee06c | -10.1711 | -44.49401 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06b6584b-72d3-30cf-b181-ea63a9b17f30 | -10.16388 | -44.50455 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32f540a1-d28b-3d31-a159-916160c85b19 | -4.42575 | -43.40926 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df905313-1b73-39a2-8035-f133053684a2 | -5.75062 | -42.50491 | 2025-11-16 03:46:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 87f7c530-10ab-3caa-9e54-9007eeb2fba5 | -4.89344 | -45.01835 | 2025-11-16 03:46:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b093a80e-50c3-3a73-be81-b791bbd03c23 | -9.95887 | -42.31843 | 2025-11-16 03:46:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cfc424f3-86cd-37a7-9dce-ed0ce98fb570 | -7.36881 | -43.32295 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4cd1550-2017-338c-bf00-a96c99a9eb59 | -4.80881 | -48.33786 | 2025-11-16 03:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c743e214-afa4-3d98-80b9-0fa81cfb9627 | -3.58166 | -41.66187 | 2025-11-16 03:46:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 74be47eb-0182-3863-ba14-6d8e32dcb7c4 | -10.00302 | -44.78088 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d57023aa-4ec7-3e17-8372-786e4cca03ee | -6.67929 | -40.80601 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6d813dd-70ab-3326-b14c-2cdd8366b853 | -6.08603 | -41.84966 | 2025-11-16 03:46:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6ab78fa-7bbd-35a9-b690-5f4eeaf0018d | -6.71318 | -42.12978 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5b7e5d79-f80b-38b7-ae41-c97d277cf942 | -6.00066 | -41.91122 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a891e12-1950-355f-b8cf-1e2fee45ab19 | -2.52322 | -47.81737 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9c23a8e4-50ec-3ef5-8c5c-b51e8e41ccec | -7.34033 | -43.34749 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 574db718-e055-3c68-843e-6f8c55012c13 | -5.32303 | -35.93418 | 2025-11-16 03:46:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 11.7 |
| a9baac59-2114-3b6b-aa7b-e8116733a591 | -6.5596 | -39.76829 | 2025-11-16 03:46:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba06fab6-d852-3577-9056-c3ec09f20761 | -4.81436 | -41.60601 | 2025-11-16 03:46:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5fccad76-4859-3753-8cd3-5829a49456bd | -10.00527 | -44.76845 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7495529-4037-3759-ad77-2a0b6147d20e | -6.46081 | -42.32617 | 2025-11-16 03:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e818a480-8815-38fd-a148-382a3e380b86 | -9.95466 | -44.92821 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b07b0dd2-5b8c-395c-a5e4-b5278730f411 | -3.94786 | -47.20893 | 2025-11-16 03:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73b12c96-c63c-3df9-9282-51e784513460 | -7.18857 | -39.20655 | 2025-11-16 03:46:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 600fd4e1-467b-3b7b-9be7-6429c6a5667e | -5.48636 | -44.84717 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ef211bfb-670f-3a82-9654-28f4dfe6fd1b | -4.31765 | -44.63933 | 2025-11-16 03:46:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a3d2035-30bc-30c2-9f9a-575a58ed4b8f | -9.35246 | -46.60318 | 2025-11-16 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 653e9d05-6434-3c0d-a1b4-d096843770fa | -7.71395 | -47.2961 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93398deb-8fef-3524-a95a-10feb6d307ff | -4.70137 | -46.31367 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b74b125-a73b-37c0-9ee8-62bfc99ef773 | -5.96306 | -43.75231 | 2025-11-16 03:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f327bf0e-11ac-39d0-a3fb-97868b7e34ed | -6.30504 | -43.79898 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4ed2d2fa-6306-38d4-b0a0-a2e20810306c | -2.51504 | -47.82296 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 3abca50e-e9a1-3023-b69c-c84e306efbc1 | -10.24849 | -45.05917 | 2025-11-16 03:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a3f4da6-1adf-3402-9f03-1b02ec4b970a | -6.09057 | -41.85039 | 2025-11-16 03:46:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 506c6b91-565e-31fb-8b0b-601f9ab60345 | -6.69732 | -40.80105 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ae85c78-7ab8-37bc-b0ba-fd37a26c0145 | -7.70973 | -47.29567 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b079ce16-a58b-3085-8272-53b0c9fc5c60 | -4.69428 | -46.31757 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a41a610-d678-3011-a05b-ba6bec0523a1 | -7.09126 | -42.73944 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3178a380-ba4f-34f0-afb4-8e678bacc37d | -5.47161 | -40.97601 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ebaddf6-7f4e-36e4-8a38-16e671cd0757 | -9.66419 | -43.9016 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 82076cfc-2a5d-30a9-815a-ca58540f2c7e | -9.73554 | -43.95597 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b3c1532d-2d3f-39b2-a939-7abca142f849 | -5.23792 | -44.35347 | 2025-11-16 03:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 338aaa09-e887-39f5-9572-b9e9972714d1 | -6.25898 | -47.0825 | 2025-11-16 03:46:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 508de253-f03d-39ae-a799-ffe7fbfd42bb | -5.17998 | -45.0433 | 2025-11-16 03:46:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cede352-6171-394c-91c3-fa70fd66a95a | -6.05303 | -46.60813 | 2025-11-16 03:46:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f394e89e-6f99-3989-8c1d-7e8e84bd0bc3 | -2.52562 | -47.82682 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 57521be6-97c4-3e41-95d7-419ca0863282 | -9.72583 | -43.96133 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 31ffd0e0-2e09-36ee-b27d-5a09ab30a5e7 | -7.26903 | -48.03152 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8017436a-2dd7-3c4b-90c1-a5e326256dcc | -6.28127 | -41.72445 | 2025-11-16 03:46:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b12cce56-6f08-3d21-adc2-b47eb690c7f6 | -7.01967 | -45.1617 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1139d34-0094-3188-929b-5f330fb27256 | -7.71491 | -47.29089 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a06fd2a-761d-334a-8c6d-a3568462ea4e | -5.63194 | -43.92803 | 2025-11-16 03:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70c23e72-db60-38e2-8232-b716f8ee5335 | -8.06138 | -43.10539 | 2025-11-16 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |


[Clique aqui para ver as próximas entradas](README22.md)
