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
| 05c53f94-a2f6-3de9-bfb7-74ec505e9586 | -3.38032 | -47.49454 | 2025-07-15 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f07ef222-5326-3107-8310-b414623adaa5 | -5.53498 | -43.8913 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bf74c5e6-d2fb-3e20-a5af-06c2f7409d0d | -4.03404 | -48.06897 | 2025-07-15 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4f46bf3-e8ae-39ae-8273-3fdc20892f68 | -7.09171 | -43.69439 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a7540951-11d9-3042-a2ff-e7ae4fe5ce96 | -4.23526 | -38.04155 | 2025-07-15 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec14b406-885f-37ee-a64a-ecc426d41add | -6.38672 | -43.7202 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b56ceb3-d9c5-3e80-a081-68cea357d727 | -7.29197 | -43.04082 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 084a8f9e-886d-3845-9d89-0b3af6b04895 | -5.78811 | -45.09705 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 576b8bef-1532-34bc-9d92-85f11faef070 | -6.7329 | -44.33783 | 2025-07-15 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d821374b-6da7-3e97-a2ad-6aef1f8805a0 | -5.53606 | -43.88487 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8fa7da0d-b2e6-3c98-a94b-d20f60908dd4 | -7.45313 | -37.231 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73808cca-f9c6-3797-9e9b-d4765db84c85 | -6.46446 | -45.35424 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4afcc13-2199-3892-9254-c7381c1d1039 | -5.78184 | -45.09994 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c3bc2a0-3300-3841-8ec5-7ad1680588f0 | -6.38116 | -43.72229 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 53768b8b-57a7-3549-ba46-a2f80fbf7276 | -6.37257 | -44.75069 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14e49fa7-dc83-31e0-b21c-a9dfe122ba95 | -3.96517 | -40.43906 | 2025-07-15 03:42:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b034352c-018d-3253-99e2-fca4563a561a | -5.5369 | -43.88942 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 8e300224-03b6-3d94-865d-f4c968dd8712 | -3.38347 | -47.47619 | 2025-07-15 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 38dc01aa-6d24-3253-82bd-f4080bdefe27 | -5.77889 | -45.0923 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32788ea9-f347-3671-8174-c36f4b2b7ae7 | -4.26943 | -48.18577 | 2025-07-15 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56363e52-7457-3725-ae7d-103f9ee2a80a | -7.20244 | -43.10478 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 50caaffc-37bf-35b8-ac5d-c9a3f577116f | -3.4246 | -43.34773 | 2025-07-15 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fe6c046-f1e1-3886-8bf9-f878c6422e71 | -3.38706 | -47.49556 | 2025-07-15 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 469e131b-4774-35a6-9573-de83095bf892 | -7.75826 | -40.63188 | 2025-07-15 03:42:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9fdda56c-ef57-3071-b6c1-4ae7d8eb4a1c | -7.28476 | -44.0334 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0da1dac9-8aed-3c28-b740-0cd9d3d6cb2e | -7.28319 | -44.04228 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e333edc1-19a8-346d-90d2-a68c8436b68b | -5.33668 | -43.75513 | 2025-07-15 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30a39cf2-13aa-39a6-b7ca-d727a8c27c04 | -4.27053 | -48.17936 | 2025-07-15 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03643200-6a68-34ea-8a5c-ccaa46993140 | -6.46946 | -45.35877 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b44e47f3-94ea-3586-9683-107fa5262588 | -7.09239 | -44.38505 | 2025-07-15 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24124a35-a7ec-3028-8174-9e12a2d59cc9 | -4.27019 | -48.17992 | 2025-07-15 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6965bbae-7460-3651-91f4-fe14fba89ab8 | -5.3372 | -43.75206 | 2025-07-15 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2cb21f7-8699-3aea-91c6-afa9075568e7 | -3.58116 | -47.52671 | 2025-07-15 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 945928b2-b719-3541-bbb7-257d9c931c9b | -3.37778 | -47.46907 | 2025-07-15 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93c6bb11-ab38-3619-9301-5f40c8c82bd9 | -5.98282 | -43.76721 | 2025-07-15 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb153567-ff97-3770-9316-0f8d569c29ad | -5.70089 | -44.25013 | 2025-07-15 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a981af78-be82-38ca-abb7-06c713c99c0a | -7.28372 | -44.03929 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cb852443-918e-36b8-a4b8-98fb972c15f1 | -5.78319 | -45.09234 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4565ff23-dd8e-3dc5-8700-d4b4392c5a99 | -6.70788 | -44.32701 | 2025-07-15 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a594598d-3b7f-3493-834f-74cf8e50f8c5 | -5.23462 | -40.87513 | 2025-07-15 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a6bc7491-876b-3160-906c-29f6df16a602 | -7.10293 | -43.51048 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 597e3abc-818d-3258-92b4-d5b9d6199ef5 | -4.22368 | -47.76722 | 2025-07-15 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 127117bc-e272-3b75-8a8d-99afd1bdb2e0 | -7.15376 | -43.15732 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96347839-b02c-3db2-bc54-e8a36b1d6694 | -7.16885 | -42.98461 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 939009df-b167-338f-8432-8115250fe070 | -5.78116 | -45.10375 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ca93e13-caf0-3e1b-ba0b-1d879d84de32 | -6.38723 | -43.71723 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb4e3e6b-df8c-3de5-98f5-3e2b63937938 | -5.79589 | -45.11808 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f505506-be40-3b3e-b0ef-00769f83b480 | -4.23674 | -38.04057 | 2025-07-15 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 782b336a-4d0c-3178-84b3-3c384ffbe03a | -4.00463 | -43.23269 | 2025-07-15 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42874084-6ca9-31ab-9614-1c380c5dbf3f | -5.69617 | -44.2459 | 2025-07-15 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9067f6a1-5efd-3ef0-a38b-00568399f703 | -7.16709 | -42.99479 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb35ab58-aef1-3e0b-a971-dac55f5cf61e | -7.28424 | -44.03632 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 80795112-5f1f-321a-82ad-7e0689ada5c6 | -7.19675 | -43.10916 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f41f721c-dbb2-377d-a15f-4afe7f975c8f | -8.54482 | -36.51066 | 2025-07-15 03:42:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a65994d5-f86f-3c72-b50d-525aeffce800 | -4.26904 | -48.18631 | 2025-07-15 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6400ded2-3bb3-3716-beda-a6768bbae9b2 | -5.36839 | -43.922 | 2025-07-15 03:42:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ba90aa5-601e-3efe-b540-3d588d928b90 | -7.08673 | -43.69353 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36cb04e3-cddd-3cb2-9347-19ecf8e1af4f | -6.71833 | -44.32878 | 2025-07-15 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c44bb00a-fb7b-3336-bcbd-eb969ca7a728 | -6.38271 | -43.71338 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 583043b0-1769-3f64-8ac9-1c12ba2f91f4 | -3.58219 | -47.52077 | 2025-07-15 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6170e5c2-033a-3295-a0f4-c8d9920d0822 | -3.75845 | -47.1193 | 2025-07-15 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3df282ae-7cef-37f1-9a7c-abcefeb84f4c | -7.50468 | -37.37109 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 772c1cd9-12dd-3ec8-9236-538383a0744b | -7.15944 | -43.15293 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39204d25-9159-3fcb-88d7-faaa630848f8 | -5.70036 | -44.24871 | 2025-07-15 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05f25617-501a-364d-9d0b-c819fabdac4f | -6.71777 | -44.33198 | 2025-07-15 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0edefbdd-c480-3fb6-ab02-8461a470616e | -6.17871 | -44.38862 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ffeb597e-eb6f-3c93-b7d8-5d0dd275eee1 | -5.78469 | -45.11623 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8b5e1a3-8b0d-3132-a3d2-ae32c237bae1 | -6.8036 | -42.85159 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ba024c71-a33d-3dd7-892b-6787e78dfd2e | -6.37612 | -44.75063 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49eca201-bfc2-3e74-b12e-29d1510ee108 | -4.03574 | -48.0601 | 2025-07-15 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cf28bc35-96ec-3084-bf07-43392d5fc5e8 | -7.08623 | -43.69647 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc038a1a-3160-387e-88fc-ccb61c0b6f28 | -3.42408 | -43.35086 | 2025-07-15 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79bca1ce-0ee6-3dc9-9525-c3ab9efa9e90 | -6.72822 | -44.33378 | 2025-07-15 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 149822f6-a9e2-3e5f-a8c4-5b05ef10f0d8 | -2.91872 | -48.23856 | 2025-07-15 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b453cf16-c08b-3b2d-b17f-b8c52ad10735 | -7.08688 | -43.69651 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17f88e9b-f89d-3a87-91da-8b51d36426da | -3.93035 | -43.15403 | 2025-07-15 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9e4326e-b706-3b6c-9b9f-207e0961e89a | -6.81846 | -41.73232 | 2025-07-15 03:42:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e8a9c07e-aee9-3530-9ade-70413c850186 | -7.16145 | -42.99916 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f4ea63ff-f186-3197-9af8-8c79a4cb0080 | -2.91753 | -48.24547 | 2025-07-15 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| f6c17100-82c4-3904-b894-fd29eec9d877 | -5.78744 | -45.10081 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26278bab-cd6d-3f1a-8d30-76e242b84f74 | -7.1929 | -43.10318 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1f743a16-54a6-3617-8305-074a3264c121 | -4.0346 | -48.06641 | 2025-07-15 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3b326505-f170-3679-b758-7b0af4cf2b83 | -8.34577 | -37.26977 | 2025-07-15 03:42:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 634193fa-932d-3928-9a6e-49de40112b61 | -6.95923 | -45.2478 | 2025-07-15 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 340e1122-ca0f-3e83-99c4-b4cd6b3b48af | -2.91046 | -48.2443 | 2025-07-15 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a782908-9090-332e-8de7-090a12676dba | -5.78251 | -45.09614 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6ba710e8-a11d-3a16-9711-3ceb6e64d72c | -6.3707 | -44.74974 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6fccc7b-39c5-3245-84f2-6f6c8f4a4eb6 | -6.29672 | -44.2372 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59d37cea-cf1a-3f0b-9abc-3c4531799929 | -5.33153 | -43.7543 | 2025-07-15 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c233627-499d-3571-9aae-420cd12c2b35 | -7.13213 | -43.44384 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91c67299-f787-3dd7-b7c1-b80ffb4af653 | -7.197 | -43.10593 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2c23e818-5830-3a71-b805-47457b70a86d | -4.03517 | -48.06253 | 2025-07-15 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f915490-1a27-36cc-adc1-d827d43d8848 | -2.9258 | -48.23967 | 2025-07-15 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e340d622-1213-3883-ba39-f22286553d9e | -7.28265 | -44.04529 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2d7be9c-bb85-300a-8915-698b5e1ab90b | -6.63647 | -44.57654 | 2025-07-15 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6807056-f345-35dd-8cf5-21eab362b098 | -5.36784 | -43.92523 | 2025-07-15 03:42:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 46223f10-aa80-31d8-b335-22beacf5c5f9 | -5.53552 | -43.88808 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 96b21f31-1da8-373a-85b8-6fd5be0082b9 | -7.75887 | -40.62833 | 2025-07-15 03:42:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0fd0ace6-7637-367c-a8d7-380171a20568 | -6.85313 | -39.75772 | 2025-07-15 03:42:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 05e08dd8-b286-30bf-b150-8bc6ca8c4e5b | -5.78878 | -45.09328 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README6.md)
