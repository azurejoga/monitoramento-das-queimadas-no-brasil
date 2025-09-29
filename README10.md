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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa5fd216-413c-3066-89df-f2a9259a9654 | -2.55038 | -45.15638 | 2025-09-29 03:45:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1492745-e7cd-3e95-8188-f574cd1419da | -4.14363 | -40.01442 | 2025-09-29 03:45:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 931e53e6-0c9a-3b22-be28-b764b098728b | -5.22144 | -43.76985 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ff1941e-809a-3e6e-b25f-b43712bc24a1 | -5.19152 | -43.75737 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2e71a032-d0a3-3357-bf57-2aaede51c794 | -5.38242 | -42.3009 | 2025-09-29 03:45:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5e8430d2-e5f9-3fc0-877b-a1f0e1f02b8f | -8.86666 | -46.62088 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b554a799-ae44-3a06-9ab1-db6e6dfb84bb | -6.4933 | -44.25908 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e762b6f2-62b7-30ca-9d7e-0ad7e7c2585f | -11.45055 | -44.97988 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 786c03eb-465f-366a-b124-0e323016ff29 | -15.52802 | -48.51764 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8e05f0e-f606-3c0a-b250-9fc9c4610fc8 | -7.86933 | -44.59312 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61352729-82f6-32b3-ac03-429c937b2c50 | -20.05463 | -41.33604 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 0b29315d-b734-383a-b91f-02d8176c0888 | -16.52925 | -46.95411 | 2025-09-29 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4e00954-2387-39f4-853f-ad89610b054f | -9.64073 | -48.12267 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d0bc5c0-e0cf-3850-a7c1-03e2d2a578ec | -6.82049 | -44.9208 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4c482f5-c229-373a-b5ab-174a80ab791e | -7.22197 | -44.79097 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2e2bea0a-7792-34ce-9c91-585366582ad6 | -18.11637 | -42.19096 | 2025-09-29 03:47:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d63155f8-5164-3be5-a268-9e8ba59afe1a | -11.95591 | -47.11276 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d183dd-f6c2-3221-938c-66e3295d16c6 | -15.90985 | -46.21048 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57ed8bd3-ea16-36ad-8cd5-4b7cf1f30684 | -12.64875 | -46.93226 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa4b101b-a0f7-321f-8d04-cae88a7818c4 | -15.53527 | -47.39106 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be92d19-a904-36a2-a817-c348a02be3d5 | -12.5861 | -41.29446 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| cdad7a4e-30cf-347d-a4ec-3962e1479dca | -15.28187 | -49.51514 | 2025-09-29 03:47:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3269b43c-6465-3066-bed5-83a8e7eefbfc | -6.46438 | -43.94401 | 2025-09-29 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d2be976-1b6e-3d39-ac07-0726defb9e50 | -16.4715 | -43.49471 | 2025-09-29 03:47:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b64bab-bc9d-3360-aeed-17bcd0b71e46 | -8.7114 | -47.98802 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3b5da19-8f88-3dcf-8184-b083072ae9ae | -8.29789 | -45.46579 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f8061f4-40e1-30ff-961a-413f2080976b | -7.2489 | -43.00086 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cb7e369f-021d-39c8-8a81-311c287a8bcb | -7.70543 | -41.28526 | 2025-09-29 03:47:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e76bf7a9-cc88-3782-928d-983c3f88a528 | -15.55337 | -47.88023 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b11def84-375c-3c4e-8fd7-9d8eb2e4ef37 | -11.36884 | -44.97969 | 2025-09-29 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43c8b990-0d31-331a-8a9c-127d37e076bb | -11.434 | -45.03876 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9013287c-6e42-3e98-a4f9-200064180eb5 | -7.54781 | -46.10974 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e171b95a-21eb-39d7-ac87-ef89e5387532 | -8.29406 | -45.4868 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc9ce8ab-b44d-3d16-ad3b-6e913932da1b | -7.85874 | -44.59123 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89c29e6c-e0ee-39b7-ade7-7b51dd45083b | -15.87528 | -46.84156 | 2025-09-29 03:47:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dad32b9f-4fe7-3768-b1e1-5d1e175ac724 | -6.91655 | -43.99999 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 575ee12a-3728-39cd-8542-0fc5af95fe1d | -6.25837 | -43.64099 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cef13fab-3a17-38dc-84cf-82b97610a655 | -16.41225 | -47.0243 | 2025-09-29 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3845635-104d-3c23-8e8e-dc949df5ed02 | -12.87993 | -44.68903 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3fbc3a4-cc6b-3c61-a1b1-5d6745fa686a | -6.5809 | -45.09845 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff58e1ec-8d5a-3cac-ba5f-f39c698609d2 | -6.9103 | -44.00512 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 518c63d0-748d-38d2-b806-6fdb482b36c0 | -6.0789 | -42.46672 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e28e1b2-643b-3e8d-9218-9dd248ff1321 | -12.58912 | -41.30033 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91e136f8-2248-3b20-9361-3d2c771c1e6b | -17.396 | -47.1279 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d50b73f8-500a-3914-820c-de6d8d987089 | -15.07249 | -48.33994 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d73b0bf6-de28-3cbc-bc33-8ba827d323a2 | -16.25274 | -42.21326 | 2025-09-29 03:47:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 146bea6d-f91a-3204-93bf-eeb01d9e4cba | -5.79515 | -42.85756 | 2025-09-29 03:47:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| e872f1a2-bd89-3f3a-add5-3f41964ded73 | -15.82851 | -46.93473 | 2025-09-29 03:47:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3306b8cb-4983-3c41-b1ec-57d7e31ec5ad | -7.76397 | -45.74968 | 2025-09-29 03:47:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bf82d58-b83e-370a-8b95-17197314dde6 | -9.0814 | -45.87637 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d44e71e9-5eab-3506-9d20-8ca39b1b586f | -10.00174 | -46.69333 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dae98231-6ebc-3276-80cd-fbce2b07ac58 | -11.80221 | -44.91407 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0e9f871-aa78-3bdf-9b56-b3410e348d49 | -12.94512 | -45.17886 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85f81e4b-b93d-396f-be44-dc584152fcb6 | -11.68957 | -44.31398 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d13ec19-bd95-38a1-9bd5-3db2bba7956f | -6.74759 | -44.75483 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 94786a7c-d106-334a-b516-122cc92c288c | -11.66392 | -45.32904 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 920130b9-5f73-3256-8eaf-e13b5788c986 | -11.94278 | -48.00573 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bb97e84-424c-3795-804d-907bde83a6fc | -15.87005 | -46.8401 | 2025-09-29 03:47:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fe4251b-c935-3a3e-a35a-d1904771a681 | -7.8154 | -46.99596 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc81e174-16dd-3298-ba73-fa9d1f55f14e | -7.8137 | -46.99796 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 11e1113d-3823-36d1-a7a7-1ae23ef1552e | -16.6053 | -45.13218 | 2025-09-29 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 004785fe-0147-341b-9a17-9e063b57cfcd | -12.17358 | -43.56175 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93dacda8-d893-3913-8919-579582c53405 | -7.69852 | -46.81117 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63acb6ee-b48f-37cd-9110-a57403179d1b | -15.47008 | -47.93542 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00c5f760-19a2-3e7a-bbd8-c14e08aabe6e | -11.36105 | -45.07727 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f1755f61-fe75-3896-b6fb-c3cd59a64918 | -15.33899 | -47.90221 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd330a48-e140-3277-8d47-9855735da4aa | -11.93115 | -48.03577 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 57bb9441-66bd-3845-828e-c077b4c48044 | -17.39668 | -47.12463 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3922dd09-5026-35de-b8e4-9207047a5e67 | -12.65805 | -46.92397 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 024be4bc-967f-3109-b242-f5afbb1ef308 | -17.7542 | -48.77058 | 2025-09-29 03:47:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26c46fe8-8b1b-358b-9a8c-bd8a9b55fb08 | -8.91145 | -46.08788 | 2025-09-29 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02c7447f-c0f0-36fb-9580-3dfd7dd8b8fe | -15.42368 | -48.24875 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e9f1ed2-7d77-3cfd-9216-a22279bf93f6 | -6.74938 | -44.74453 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 536c2d77-160f-36a8-8e2f-d545e4736173 | -17.49772 | -43.48221 | 2025-09-29 03:47:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d489ee8c-b38d-3932-ba99-3b3837b0ec38 | -8.14469 | -46.40257 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ded60e92-e9c7-3d1f-9bb6-91cbf199a1c6 | -6.05651 | -42.48335 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b7ebbc9c-68a8-3d41-b5f2-850b4ce0ab07 | -11.45014 | -45.00975 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28e500a3-1894-3b65-b2c4-239b7170380f | -7.11177 | -45.53545 | 2025-09-29 03:47:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00ebfae5-fda3-3933-bcd4-6df4f143af0b | -6.62027 | -44.96187 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f54c8eba-4ae5-376c-95d8-925ab0e854a6 | -6.15231 | -43.88274 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d8efe004-80c8-3d39-829d-eb841990c688 | -11.44956 | -44.98507 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4fe3f57-0afd-3321-b27c-c6cd5a4ad6f2 | -12.2113 | -43.74693 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8339392-f256-39cf-a99f-543e61cac6f4 | -6.26249 | -43.6476 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62f1fdc0-e9ca-31a2-ac33-7811795e6358 | -18.96737 | -43.19304 | 2025-09-29 03:47:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 01027620-8136-3e49-9b9f-2c7534f38a80 | -6.46398 | -44.00643 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d5e6d2a1-b2cb-3a97-bff9-799879798cb9 | -9.05253 | -46.71956 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 039b463c-4d08-3fc4-8f5d-e752768f82f3 | -9.63971 | -48.12781 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55b3c509-f967-3897-af4b-3ac9ae567aae | -6.07975 | -42.46186 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54a19224-14a0-3122-a6da-2ad0fdc504df | -6.43784 | -42.82277 | 2025-09-29 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd7d5aca-d811-3125-baeb-e2095615dc56 | -19.85143 | -42.60382 | 2025-09-29 03:47:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| db6cd061-0ffa-3234-bcc5-04e49592429b | -6.21492 | -44.19777 | 2025-09-29 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf8b083b-9462-3131-89bd-f29eeed388e9 | -11.3468 | -45.06818 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92addbd6-2907-3054-ae54-490588692766 | -6.89598 | -44.53171 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f5703c4-2c57-343a-bda0-f31207281517 | -9.79829 | -46.94115 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5decaf46-4553-3846-9f9b-8925a3bbf2bb | -7.24795 | -43.00614 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a48f003c-9e87-33d3-aff5-bb1c8ae7bbf8 | -7.8899 | -44.6002 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e6fbf1-c57e-312f-a081-403f7e1a11c0 | -15.91042 | -46.20761 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc788186-eda2-31d9-a212-bf9b1c23a76e | -6.82541 | -44.8274 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c22f3140-a46d-3a90-8756-aba8b46f374c | -10.83167 | -45.39413 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae5694e-d1c5-38f9-939d-0f456bf9822c | -6.48665 | -44.51036 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
