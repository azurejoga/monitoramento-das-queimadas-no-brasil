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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd72c5fc-ad6a-3cea-ad9d-8f95daea43b4 | -16.34769 | -43.6947 | 2025-02-12 03:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca33d79e-5295-3212-90a6-f6387f705097 | -20.20738 | -46.43018 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93e5cd4f-578b-36ae-acd3-cb68eaab98d5 | -19.83839 | -40.08123 | 2025-02-12 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3cb6dcfa-ea9a-315b-a6af-b5019ebb5d6d | -20.21537 | -46.4416 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aff94535-6dae-331e-899a-32fb7c1558d2 | -19.22486 | -40.16249 | 2025-02-12 03:40:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90793084-a8c9-3d2b-8b8d-a635671d23ef | -16.35211 | -39.25649 | 2025-02-12 03:40:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79b245d0-5724-319d-86dc-c5ffd4e93e67 | -22.67754 | -42.85607 | 2025-02-12 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b6931967-c478-369f-9091-de3e3deb3ccd | -20.21978 | -46.4491 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 460ef503-26e4-3397-bbe6-70767d102132 | -20.21677 | -46.43517 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0aae09db-7e34-3af4-99d8-30c90ca75a80 | -20.21219 | -46.43106 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b448652-186b-3e5c-b232-8d192190ed62 | -22.85475 | -42.98144 | 2025-02-12 03:40:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 99915c58-5d20-30d8-ace7-40921bed4fd6 | -20.21923 | -46.44902 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e835613c-bd52-3ad1-af55-1454de2cbb9c | -22.84227 | -42.78555 | 2025-02-12 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 32f468a6-4536-3e2a-90e9-43c4039aa724 | -20.41728 | -43.5538 | 2025-02-12 03:40:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 847a3fd6-13ec-3312-83e6-641b8aa1c637 | -20.21197 | -46.43428 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01aedac2-46a7-3bf4-b263-ef1a39c067fc | -20.20668 | -46.43346 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92f61d21-a6ef-3d0c-8a4f-003a11385a26 | -17.95498 | -42.58364 | 2025-02-12 03:40:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e59776b4-9719-38cb-8f8d-c8261c177a27 | -22.67805 | -42.85855 | 2025-02-12 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 19fbba55-6099-3c2b-af4d-94a748328fa6 | -18.56265 | -39.92583 | 2025-02-12 03:40:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51fc1381-e28b-392f-969e-a440c46266c6 | -20.21656 | -46.43842 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb6866ad-094b-3296-ba76-18fd4e98af99 | -20.21589 | -46.44164 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0483ee1-60e1-38b2-8206-e35a07c531b3 | -17.95316 | -42.58285 | 2025-02-12 03:40:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8a1b6880-37e6-35e3-9e64-17505ded3f60 | -19.22122 | -40.16171 | 2025-02-12 03:40:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 83034273-0ecc-3c06-bca3-318ab2d2377e | -20.20619 | -46.43348 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48d4b563-199e-335d-a713-052c3e8650e9 | -20.21992 | -46.4458 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4898a1f3-6f8b-3b85-815e-6b83de23d42d | -22.67406 | -42.85764 | 2025-02-12 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fb59ac28-c7ff-3079-92cc-3c668b494f45 | -20.21724 | -46.43518 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f299a39f-f39a-36c7-b917-7704d6f8174e | -20.22062 | -46.44258 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 086bcacd-54e4-3a55-b9f1-bd59086a26dc | -17.7633 | -39.76838 | 2025-02-12 03:40:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99cf6351-7751-3097-a5fd-0d4fcdc70158 | -20.21606 | -46.4384 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54c2b077-992d-3056-a5dc-8a26ea63d9d8 | -20.22046 | -46.44587 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13f7912d-ecf0-3325-8ef5-f5cd2e3fe1b5 | -20.21265 | -46.43105 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5f8f4de-ee08-334c-b4a5-830b85047208 | -20.22114 | -46.44264 | 2025-02-12 03:40:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e77d9c86-e55f-3fe6-94db-8ab792063305 | -22.86868 | -43.23566 | 2025-02-12 03:40:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c55a5d8e-2108-35bb-ae54-678e4fae267e | -17.95074 | -42.58265 | 2025-02-12 03:40:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 69d8b74d-91a8-3d80-9a6e-3d6030231f00 | -20.71218 | -41.88601 | 2025-02-12 03:40:00 | NPP-375D | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2d0b143e-b4e8-3b2c-aaee-6a03e12d0b16 | -22.56303 | -47.32097 | 2025-02-12 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d2e9d29-5075-3ca8-8a78-f76274108bee | -22.53846 | -48.81408 | 2025-02-12 03:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ee6f776-428b-3e07-a1e7-794d0dcf6820 | -3.43915 | -39.62177 | 2025-02-12 03:57:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4de02d48-a59e-322a-b881-29aa037f65a1 | -5.21947 | -40.35249 | 2025-02-12 03:57:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e4ff013-f9ad-3d64-b119-c89ca238f8e2 | -5.00287 | -42.93459 | 2025-02-12 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00071d9a-b715-3f89-8954-1be3147bb070 | -5.97414 | -39.68229 | 2025-02-12 03:57:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ffa9e70a-ec74-3c07-bbe1-1fdc40753b5e | -6.15917 | -35.18835 | 2025-02-12 03:57:00 | NOAA-20 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 83ed904f-32bd-3171-a984-efb8c51e8317 | -6.15862 | -35.185 | 2025-02-12 03:57:00 | NOAA-20 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 81854722-93fd-3333-8a93-2231b4730dfa | -4.31359 | -39.91462 | 2025-02-12 03:57:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c7abbe97-17ec-3b04-bf46-7cf359c15aa9 | -5.97744 | -39.68281 | 2025-02-12 03:57:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 17c9920a-092b-3954-863b-0c7990fdf7d5 | -6.7271 | -43.02494 | 2025-02-12 03:59:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc550a51-bebb-34af-8331-eae6207433ac | -10.53482 | -44.67891 | 2025-02-12 03:59:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f605aa4-edff-3fd8-ae39-42595697e270 | -12.86062 | -38.36744 | 2025-02-12 03:59:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 655fc78f-61be-3b87-ac46-6a783bfcd0f4 | -6.59847 | -39.38298 | 2025-02-12 03:59:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66a980ec-09c8-35f7-ba46-d5a5e3eb7bb2 | -6.53993 | -39.14847 | 2025-02-12 03:59:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f1be1661-6534-3689-92f2-b4a9576e870d | -11.93781 | -39.99384 | 2025-02-12 03:59:00 | NOAA-20 | PINTADAS | BAHIA | Brasil | 2924652 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 76a0a330-0aac-3ba7-ab0f-00f11a961aac | -9.10216 | -39.96533 | 2025-02-12 03:59:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f8408d76-cfc8-3fbc-91f3-c57f3a74ebd1 | -6.97799 | -42.81964 | 2025-02-12 03:59:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d6bc945-d036-3055-a02e-324f0acc12d2 | -10.65428 | -44.48878 | 2025-02-12 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 87d78bae-e0a1-3ec1-9804-e4ea1370b3f7 | -7.0181 | -38.82093 | 2025-02-12 03:59:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9329e6f2-94de-329b-b032-c0b25f51a963 | -8.35189 | -45.19381 | 2025-02-12 03:59:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1ad8135-7a52-3afc-bbd1-505308768361 | -10.65356 | -44.49314 | 2025-02-12 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cd8d0e06-e7a3-32b8-83df-ac0f758871d5 | -9.87554 | -41.80017 | 2025-02-12 03:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1771a46-9e6f-33d2-9000-6ff9ab1318e4 | -11.01302 | -45.06209 | 2025-02-12 03:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4006a4b-0b76-3b19-89a9-29c5750c070d | -11.11094 | -45.12455 | 2025-02-12 03:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5955ff52-76c5-30de-9854-2d6701203198 | -8.34794 | -45.19318 | 2025-02-12 03:59:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69cde49f-e624-3650-9fbc-2891ad8acab4 | -10.53559 | -44.67442 | 2025-02-12 03:59:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9bbcf25c-a09b-3017-84e8-c2a75d4c6ddc | -9.85349 | -37.27919 | 2025-02-12 03:59:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd5769ff-5b48-359c-b831-83496a61b1cc | -9.09885 | -39.96481 | 2025-02-12 03:59:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c313f5e6-841f-34f5-86f4-aca811544653 | -10.65795 | -44.48942 | 2025-02-12 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ec6077d-a818-3a30-8f41-a03277b3657c | -10.59389 | -44.78227 | 2025-02-12 03:59:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97f7069f-7d6a-353c-8f51-dc7fd2b6e003 | -9.15458 | -43.12332 | 2025-02-12 03:59:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d28afada-a6bf-356b-ac1b-dbf3c87894cf | -6.34211 | -41.91624 | 2025-02-12 03:59:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 460247cb-f292-3cf2-90d9-2fb786edcbad | -6.97511 | -42.81507 | 2025-02-12 03:59:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fecf958f-9bad-3f7f-9cf3-2268e9e13813 | -7.57995 | -37.49532 | 2025-02-12 03:59:00 | NOAA-20 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 849bc5d9-e300-3983-b6ae-c73753b73405 | -7.7258 | -37.48787 | 2025-02-12 03:59:00 | NOAA-20 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6b2d5b94-46d7-3057-aa91-e936b8f15b15 | -11.93726 | -39.99746 | 2025-02-12 03:59:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93329d12-6843-3b2f-897f-aaf38c5f2a53 | -6.49754 | -39.59481 | 2025-02-12 03:59:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 56cc0ef9-07e6-36aa-8677-cf394fff5e15 | -12.15046 | -40.3367 | 2025-02-12 03:59:00 | NOAA-20 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d73e1ac8-f11f-3b5a-aedf-6f10dec25ef1 | -11.01383 | -45.05743 | 2025-02-12 03:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1086776-841a-3a18-a8b2-67f27d127180 | -10.79067 | -38.35355 | 2025-02-12 03:59:00 | NOAA-20 | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| efceed01-6633-3517-aaf2-9d83feee06e5 | -6.97864 | -42.81565 | 2025-02-12 03:59:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 51d7b72a-6d94-3517-a34b-871c32a9431e | -7.05403 | -37.24316 | 2025-02-12 03:59:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c9157bb-30ef-3521-9aea-69b9b918995a | -10.66 | -44.40917 | 2025-02-12 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43dae814-bcba-36d3-af9a-0014c15ea86b | -6.68295 | -42.95928 | 2025-02-12 03:59:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1220a42-d2d4-3419-8279-12516b0cd49c | -6.97446 | -42.81906 | 2025-02-12 03:59:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 602881e9-546c-3f26-93a5-6ce139af245a | -6.60179 | -39.3835 | 2025-02-12 03:59:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68bd0218-5516-33a5-bed7-c3f803af7f1b | -13.03346 | -40.3321 | 2025-02-12 04:01:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 10c72e17-6384-3ce3-bfcf-2c34c280b9f8 | -17.74356 | -41.63345 | 2025-02-12 04:01:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 75a363fe-6304-3a81-b032-60b4f9c3d219 | -17.77759 | -42.81027 | 2025-02-12 04:01:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd57fb86-969a-3df0-95c7-702930627dc0 | -16.34719 | -43.69703 | 2025-02-12 04:01:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b3e4ccd-cbbe-305f-98ea-394875ff59cf | -14.13278 | -41.69209 | 2025-02-12 04:01:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74323569-9ca7-3b1d-8896-7cb0fe41dd96 | -16.34867 | -43.69678 | 2025-02-12 04:01:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e40c708-d378-3291-a5c3-5b5a648c3560 | -14.1179 | -41.67873 | 2025-02-12 04:01:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a0a4ac2a-0398-33f1-a2c4-0696515bf0ed | -13.03681 | -40.33263 | 2025-02-12 04:01:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 968002ea-ed9f-31c1-b5ed-5abe784afb13 | -15.64978 | -39.192 | 2025-02-12 04:01:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| babe7d46-d826-304d-832b-4dbbaea0506c | -19.22311 | -40.16107 | 2025-02-12 04:01:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 34062b91-bd12-3890-a3d9-e65bd7a87462 | -15.6536 | -40.99089 | 2025-02-12 04:01:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 59a569a5-e626-318f-85b4-3bf1a1285647 | -17.95305 | -42.58079 | 2025-02-12 04:01:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0a128ba-68f3-349c-8827-aea16c21282f | -17.77816 | -42.80666 | 2025-02-12 04:01:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db4e6991-52cd-3908-b423-612dc2408c89 | -17.76401 | -39.77027 | 2025-02-12 04:01:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e97af8ec-acf4-31ef-bd3a-f3607d5e21fa | -22.85635 | -42.98204 | 2025-02-12 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 85e2854b-9746-3444-857e-86ad8a887f95 | -22.69839 | -43.34892 | 2025-02-12 04:04:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 418d656c-79c6-3f08-9526-b6f3e3774a69 | -22.89993 | -43.75308 | 2025-02-12 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
