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

## Dados Diários - Página 244

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b61bd447-3537-38e5-bc42-2a5985564f73 | -7.82781 | -45.48006 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8933a831-9689-3876-8770-974d34f082ea | -6.90128 | -44.91867 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| efef2e57-036f-369b-8ca5-3a20692e1ffc | -10.97926 | -45.39774 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2e4768df-5235-388f-b038-f4aa305304f6 | -7.26103 | -45.35009 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e19797c1-cedf-3e21-b3e2-1923f0971294 | -10.59984 | -43.84648 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3d2a55e1-458a-3649-8bcd-bb6e8d4f587d | -10.87136 | -45.55218 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e2ed658b-df75-3efd-8009-6b4109fe7b41 | -10.3061 | -42.38307 | 2026-10-08 15:41:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| c98a9a9d-49a1-3260-9023-29dab3a997e8 | -9.36688 | -45.95014 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 4bc92fd8-4584-32b9-a4ef-ee87da1b7227 | -5.74861 | -41.68689 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 27020200-6448-3063-8d93-c993188f6edf | -8.94334 | -45.1528 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ac53631b-11aa-3167-b2ab-272bb121d123 | -5.31939 | -40.89316 | 2026-10-08 15:41:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 01cf8cf3-7d66-3f91-a4c0-19b166142901 | -9.52221 | -45.61237 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 55709912-f775-312f-b1c5-9e40a3cf32ac | -11.08836 | -44.02586 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d9a616b6-42cf-3c9a-befc-0b5a5ec325e4 | -8.80904 | -45.80434 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bfe8d75e-0996-3c6f-ad2f-68d2666bb2ea | -7.05156 | -44.34087 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 878275ad-58c6-3ff5-bb88-80c2fae74f77 | -6.93051 | -45.25799 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| f3fe024b-af1a-37ab-82be-e5cb0d28d088 | -8.8938 | -45.3838 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 59144a79-625d-3218-873d-fb416c44789f | -7.37305 | -44.03033 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bb7820ac-5afb-393f-ba2b-a6070c4cccb5 | -6.88358 | -43.68936 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0ee335b0-4d2c-32e6-b5f4-0f0964f1a908 | -8.19493 | -46.35832 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0b806ab2-4d00-3cd7-a9e4-1be5aa775a67 | -7.5364 | -42.09563 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 67205270-02f8-3d29-88f1-905aed5e37dd | -10.90562 | -45.54311 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 915957b6-96f5-31fa-88d9-3711f7642749 | -5.39438 | -45.90479 | 2026-10-08 15:41:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ed1680d5-e2ac-3a6e-85d4-3e29edd7408b | -8.93134 | -45.17383 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 340.0 |
| 742a9bcc-9db1-303e-bd13-89f3dd86decc | -9.1351 | -45.8386 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 11eb637a-2481-34fd-9c65-9b94868009f0 | -10.94986 | -45.38292 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 77cdc690-5583-3abb-bda5-b5cb549aa13c | -7.54126 | -42.09164 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 367d237d-04f8-3bcb-9d11-de5adbc577e9 | -5.77344 | -43.33329 | 2026-10-08 15:41:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| ba661d75-c5a3-38e5-b7ef-5cb5b8c86ea4 | -5.33018 | -35.55929 | 2026-10-08 15:41:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 76681280-c2c2-31a4-bc4e-9b34526deafb | -7.46961 | -42.85506 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| eccd83ce-ee77-3985-aeb6-22e7e89b6eb5 | -6.88413 | -43.69352 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ca840f34-da05-3b8b-868c-35c753e2d98f | -6.82086 | -39.3114 | 2026-10-08 15:41:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 23cb2077-70a6-332c-9825-36d6290ce5a7 | -5.98372 | -41.36382 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| f04d211a-bcdc-3aca-9807-8d83ce8c43da | -7.53474 | -45.87263 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 6c5a8672-ecb9-3b7c-8646-16c8dc78e3e1 | -6.6666 | -45.36763 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| bb8a7159-fa2b-316f-8163-54affbde4949 | -9.89916 | -45.18844 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5a5d90d8-54b5-3df7-967a-7da329c3da4f | -7.4707 | -45.77602 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 665615a8-ad62-3618-884a-1cad275fc99c | -6.4131 | -44.95138 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a8a6ba5a-f56e-39b0-b86f-499fb2dc53ff | -7.53685 | -42.09893 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| b9a65930-5c44-3b58-8fea-93f2a393a1fb | -7.48938 | -42.79549 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 659e31ed-34d4-3813-8a09-77bc37d86291 | -4.49694 | -38.73223 | 2026-10-08 15:41:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| fe324714-dc11-31dc-b54b-a920e141cc04 | -5.74686 | -41.71115 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 2814d444-7a62-3b7a-b0d9-ee696e9d5b27 | -9.94081 | -43.57682 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 73c0f988-bfe8-352e-b8ae-a96e8bbb0142 | -8.9631 | -45.15076 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 92dd19ba-1087-3e55-bd71-2397b640909c | -8.29819 | -44.16934 | 2026-10-08 15:41:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cb63e993-c764-33bc-b649-82a3fbb46efa | -5.84008 | -35.40682 | 2026-10-08 15:41:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 475e0181-8643-3cd4-b58e-05e6b660f073 | -11.01095 | -45.4314 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4ced12af-3049-3849-9c71-ead44bc8ca15 | -5.77149 | -42.05589 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7b250250-578d-39ef-9cc0-252039eae1f0 | -6.53071 | -45.38455 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 92a290b1-30a4-3edf-a9a9-d9672f12358a | -4.84075 | -40.39819 | 2026-10-08 15:41:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b790ff5b-169c-3e19-acf5-f19fe9bfbfab | -7.18862 | -46.51183 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d2e0696a-3d96-3cfd-bf08-ddf900b63b79 | -8.96684 | -45.12796 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 90ac0bbd-e77e-30b8-b5b5-71da3ee87a76 | -5.71402 | -41.72999 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 962dae60-929d-3abf-a07e-5f13f381841b | -8.95491 | -45.14788 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2a822ad5-3a63-3ec9-9a5b-3105da859d27 | -6.14839 | -39.44751 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 58b6381b-fbb8-3919-a1e6-7fef64e58fec | -5.72694 | -45.23343 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d6348f8b-aad9-3223-861e-2750be1fc729 | -10.74936 | -44.79743 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ad0ae40-8b4a-3eed-b249-6dce1a606a99 | -5.71525 | -41.66769 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a11e0a5f-be15-3748-a9cd-a82b796e87e6 | -6.57148 | -41.61247 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 590a19c4-b4e7-37c5-ae74-55dbcf6f2651 | -6.45425 | -46.01036 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| cf8acb64-d290-3519-921d-70635ade21c7 | -8.60981 | -45.64046 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d951afdb-f019-3621-ae15-b2672a6f8651 | -9.517 | -45.60909 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f78a1511-2481-325b-8c83-7f7d102df538 | -5.71753 | -41.64702 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| 3f8283b2-9fea-3c42-8818-621427a73f29 | -6.95631 | -44.89776 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 89eadbf3-f3ae-3519-b309-f0884180f401 | -7.05546 | -44.33082 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f55642ce-8168-380e-8457-532aca20601f | -7.47012 | -42.8588 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 44ec0ee8-c80b-3060-92b3-928f8c8cc797 | -6.99584 | -44.0534 | 2026-10-08 15:41:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97067f51-06f2-3b1c-bb06-10c955cb5202 | -7.48384 | -42.79386 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1ecba8a8-0ff3-3db6-a952-7d823d6ea719 | -6.45456 | -42.80009 | 2026-10-08 15:41:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 475efc53-291e-3db1-a444-ce602bd15b55 | -6.1473 | -43.38436 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bee7eb05-f62f-359c-9641-aed571f2f0f8 | -6.77177 | -44.12955 | 2026-10-08 15:41:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0d631d6f-65cd-317a-9db3-ac422554c2c3 | -5.48642 | -43.96241 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1af60d24-0265-3f62-9cf0-c9b7c7c1f2c6 | -8.55556 | -40.28307 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 549b20bf-0223-3249-82e5-a46e38769cfb | -6.3182 | -35.13498 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| d420354c-ca6d-32aa-b1f9-ef4fcac8074d | -8.95649 | -45.15126 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| d9c033ae-53e6-384b-93c9-34bab77e702f | -6.36277 | -42.91198 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0da70926-b665-3a33-8660-b665a6cb279d | -7.34445 | -44.47638 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f9b8bde4-3cbf-37af-b1db-18a67302800f | -8.93964 | -45.17627 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 326.3 |
| 5b0608bc-dd16-3b9a-bb92-0de1ad651e10 | -9.01262 | -45.12903 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 324fe636-e544-3670-b63d-7d1c35ed6e42 | -5.26135 | -45.4101 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fccb29ac-b518-3f19-adba-27190eee0da1 | -6.49845 | -41.82663 | 2026-10-08 15:41:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ecf18f74-04a9-3a54-8fba-80c9d79fb606 | -8.10049 | -39.88902 | 2026-10-08 15:41:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f50b8252-1455-3f7d-8bd8-51e743de4184 | -5.71815 | -41.6525 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ca0d197d-57e2-3962-a8a4-6bc75621d352 | -9.36541 | -45.93661 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| bfa38eee-8ec9-3615-a58b-d08368caaa78 | -4.26276 | -38.72398 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9fb176a1-203f-38cb-86bc-7d9925a289d6 | -7.48434 | -42.7975 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2966a66a-d0b3-3010-808f-5e12e85d3ab8 | -6.15611 | -39.4244 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c83f1928-9edc-3cdd-b77c-56e356f62428 | -10.89746 | -45.53682 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9830234f-5dd0-3c8e-996c-fda19921fe44 | -6.86343 | -41.799 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ebac81ac-60fd-3c0a-a2c7-deff727cbb19 | -7.45842 | -43.1985 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7c6b5394-e851-3731-b680-e1382fc70eff | -10.16025 | -44.67785 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| dff9725a-2783-3e05-a6fc-4110e6af9265 | -9.94024 | -43.57235 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| d56e329e-29c4-3113-b9ba-89fd4867b190 | -5.76722 | -42.06272 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 84054a02-c579-3cb5-b1de-09c94e635155 | -6.67284 | -45.36018 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 8e6f4c26-f184-34e5-9d77-8577ba77ed9b | -7.04393 | -44.33723 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a6c08e58-4c15-3269-9d7b-75b027726804 | -6.23731 | -43.73066 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fe78fe9f-341e-307c-9b24-ec289100951c | -5.38231 | -44.19194 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 20f061aa-add7-3fb3-a5ff-00814f1d96c6 | -9.43616 | -44.60766 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d20f4d80-e302-3007-9806-caac29f8740d | -8.88426 | -45.60714 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b6928e46-6da9-3b99-9745-2e1f979e76b1 | -5.76985 | -42.06642 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |


[Clique aqui para ver as próximas entradas](README245.md)
