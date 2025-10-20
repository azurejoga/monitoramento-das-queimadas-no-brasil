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
| ff5c22aa-9ddb-3c26-8c2b-28b2d6885882 | -4.49838 | -43.66445 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ccba3c03-125e-3775-a36c-7ce405237a53 | -9.5674 | -40.33131 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4d2e40fc-fa94-38d2-98cd-a8b82aa9e59e | -5.54635 | -43.03689 | 2025-10-20 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b8aaa1a-1e6f-32e1-b46a-b2063e2c1573 | -4.39734 | -43.31428 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7a73c21f-86f0-3a70-b872-a06b4011b456 | -6.39867 | -38.28175 | 2025-10-20 03:51:00 | NPP-375D | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1d14cd8d-6281-3371-8c19-fab404c602b8 | -8.07113 | -48.02576 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ed480e1-92ce-31cd-a9cf-d21d4e225771 | -8.07594 | -48.01627 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0d1406d-b643-3e85-b427-2da97af412cc | -6.85644 | -46.29801 | 2025-10-20 03:51:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 661a08c7-1c4c-3f54-8327-26f30f51af50 | -6.88051 | -43.60116 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e37352bb-f26e-3ce4-a44f-ab60090ce950 | -5.61895 | -43.65249 | 2025-10-20 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e97ebff3-8452-3be4-8706-3358bfc8f495 | -3.58385 | -41.65698 | 2025-10-20 03:51:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 188ca636-1870-354f-9c75-7f4777d91837 | -4.47919 | -45.30149 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7ae2a5b-eab4-3abe-ac3f-a99ce1d64c23 | -9.5696 | -40.34 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 743ec6c9-9c89-39e9-9e2c-161db6e2a982 | -4.4576 | -37.97266 | 2025-10-20 03:51:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 133801cd-9c35-37db-985c-ced4e7506cd4 | -6.5098 | -39.71781 | 2025-10-20 03:51:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bf8899b-baf2-33e6-b553-d31457ec1205 | -9.76215 | -41.92159 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b450a6df-84c4-39a3-a8e7-74c189c6bb49 | -7.50691 | -38.82086 | 2025-10-20 03:51:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6138b8b7-77bc-38fb-8a6f-60012c5c1fae | -6.49838 | -39.72021 | 2025-10-20 03:51:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5782c54-172f-3d6d-9f79-1415d4319250 | -6.11504 | -41.7905 | 2025-10-20 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5887c0cf-c0ee-333c-992e-91f09d5b4219 | -7.1305 | -44.25191 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6338c011-6415-34ba-a6ff-729358d988b7 | -6.11038 | -41.79347 | 2025-10-20 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 36a2115e-b9a6-3f95-9ab7-4594a3b17204 | -6.10113 | -44.02833 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77848ae0-647b-3730-bf08-4063a9df062b | -4.47862 | -45.30473 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dc6a79a-5834-3b87-adbe-9095e9337f61 | -4.8423 | -43.03395 | 2025-10-20 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 48498929-3e69-339c-8e94-61e90d9cbb43 | -6.95999 | -39.63782 | 2025-10-20 03:51:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24f92dee-14f0-3c51-9d7b-c2e66f055dc5 | -8.15923 | -38.62874 | 2025-10-20 03:51:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ec171e95-d6a3-303e-9466-8e5c93a6faf1 | -4.55099 | -43.55132 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f5d346e-f5a7-3994-848f-23bc733c7230 | -8.07003 | -48.01509 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a417beb8-16ce-30da-b6f8-9fc81039c03f | -7.14473 | -46.5209 | 2025-10-20 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0e1bb9e-4795-328f-ab33-7f314057385c | -6.11097 | -41.78991 | 2025-10-20 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 14a6babe-e1d3-3d54-9b04-0834ee25a07c | -6.87974 | -43.60567 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c84bb841-0af8-358a-84c3-4e76983387fb | -4.80764 | -41.12795 | 2025-10-20 03:51:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6a6922a2-df2d-351b-b4f7-af994be718fa | -7.05766 | -41.82591 | 2025-10-20 03:51:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f570b1d9-586e-351a-8fc1-5483da744ea5 | -7.1263 | -44.25412 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88ea5b22-138e-371d-a415-974a8357aeb4 | -8.16203 | -38.6329 | 2025-10-20 03:51:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 8d92d4eb-3625-3f74-8bfa-bf5f4fef67dc | -7.21056 | -45.41707 | 2025-10-20 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e48e91ff-b3ca-34f0-94cb-f19ca526526d | -6.88205 | -43.59216 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 809b2ce2-dd13-37c6-9bf6-7b2147f86919 | -4.48019 | -45.30132 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b57b0cd-6e5c-3e8d-a276-8463562ff800 | -8.15864 | -38.63236 | 2025-10-20 03:51:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 17.7 |
| de8e7891-9090-3a66-82b9-f789ed5b670a | -7.46519 | -44.76975 | 2025-10-20 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c07645d6-e34b-352b-9656-407cf5339ac0 | -7.53189 | -46.09263 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecfaaba0-7277-367b-8e05-0d9a92a03c58 | -3.5939 | -41.65413 | 2025-10-20 03:51:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 92ccfb0f-069a-3a6f-ad10-d0e2f8175f4b | -6.87522 | -43.60493 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92b82c22-c7b5-372c-b8be-bfc00576f50b | -5.54456 | -41.34216 | 2025-10-20 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 054576be-ad05-3d14-ba91-05b85d6afb01 | -6.88283 | -43.58762 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d882d01b-0534-32e2-badf-a534fc39dc00 | -4.48545 | -45.30231 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8721a25-ec13-3ceb-bbf8-4bda0920999b | -8.15526 | -38.63182 | 2025-10-20 03:51:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d04537cc-1a0b-3ab6-8eee-ce2f870a9831 | -7.53131 | -46.09591 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6925999-b28b-3348-9475-cabca79c8ed2 | -6.46838 | -43.73325 | 2025-10-20 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a38c542-a49c-35f4-b2f2-27a96d5d5662 | -6.21167 | -40.96911 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a5823f2b-ccbe-35cb-8d80-d8b1e81d6630 | -7.13299 | -44.23732 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecb432ac-ec40-3c22-b077-dfa0d64774bc | -4.40114 | -43.31979 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5a0fadeb-2aaa-3d13-94b4-803c82a76723 | -5.47008 | -36.65131 | 2025-10-20 03:51:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac059fb8-a876-38ad-b8aa-d4579ee63262 | -9.47133 | -41.03719 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ad10e48b-7e46-336a-ae81-73a88870f087 | -3.59807 | -41.65484 | 2025-10-20 03:51:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 911663e3-9c5a-3208-b351-bc693864293a | -5.54191 | -43.03616 | 2025-10-20 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 775dd048-5254-3cf7-90b0-5161868d789b | -6.87894 | -43.6103 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3462db56-079b-3f53-8933-2d60c56b4280 | -8.07784 | -48.02263 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7e6919b-e2aa-35b6-acdc-e5451fd838ff | -10.52324 | -43.35514 | 2025-10-20 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc7bdda-274a-3e31-a48a-4175f6df1339 | -4.40195 | -43.31503 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f1d0af3f-cd79-3fc1-b32d-5e75d21a303a | -4.49368 | -43.66359 | 2025-10-20 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f9f37b2-2871-3ccd-9941-b2923a292544 | -7.21563 | -45.41801 | 2025-10-20 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b75ccd0-1286-3446-b970-03b55e8f5844 | -6.34198 | -41.55405 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1acb3d5-d18f-3f58-b1d8-009192050088 | -6.10261 | -44.02519 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40208d9c-085e-3e9b-9db0-0e0801a91991 | -7.13364 | -44.2401 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a6523998-dbfd-3d60-b903-1487797cb7ba | -6.2007 | -41.53373 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 62559a2a-aded-395c-a3df-e8549533710b | -5.36718 | -45.51187 | 2025-10-20 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 295045f9-b28b-3b43-9fa4-3636022b366c | -4.85405 | -45.12092 | 2025-10-20 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b94c182b-842b-385e-bdbd-4a8fb61dc815 | -4.94463 | -41.55646 | 2025-10-20 03:51:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07f362ca-4f5c-3616-8a91-ca18a0e18735 | -6.88735 | -43.58833 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e6c5b1e-d8ea-3b22-9763-59a8381255ee | -7.50409 | -38.8166 | 2025-10-20 03:51:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd522f40-41a9-37ec-bf0f-7dbec95dbf65 | -6.88503 | -43.60189 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 795c7042-2eed-327f-98f5-c21793221df4 | -4.42393 | -40.16859 | 2025-10-20 03:51:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49caf34a-d28c-3f55-adc4-ae7eba094a7f | -7.12966 | -44.25685 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a708b2d-2407-37f0-b00c-1a7566a7863b | -7.53718 | -46.09353 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 492cff15-a754-3e50-92e1-93a9643da4db | -7.54247 | -46.09442 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cad745a1-4106-3a0f-aca6-5cdd2547d29f | -4.83062 | -42.74897 | 2025-10-20 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c66b1ad9-d3f3-395c-b557-d340790be608 | -6.85166 | -46.29346 | 2025-10-20 03:51:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5543bca1-b313-38df-ad8f-0d2eefa1306b | -5.62597 | -43.64691 | 2025-10-20 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a162d3e-10ba-32d8-8bff-fd9e8787be91 | -6.14524 | -41.8091 | 2025-10-20 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| dcef00c8-3f71-31c2-bef7-17a60a18a761 | -8.07512 | -48.02057 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c690b67-6a80-3149-a600-9f5e9a288dc2 | -8.23599 | -46.24704 | 2025-10-20 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c502071-8d50-3632-be9c-02e33c54fdb4 | -7.13608 | -44.24753 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c673c456-5b56-3c80-9ff8-2f57d0cadafd | -4.48389 | -45.3057 | 2025-10-20 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 13504a1d-9faa-3f94-b592-5ac95881f805 | -4.17829 | -42.19077 | 2025-10-20 03:51:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1d3ca0d7-9b67-33be-844e-533e49cab5cb | -8.07271 | -48.01711 | 2025-10-20 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae315caf-2b0b-3444-b869-65ac762538f0 | -6.20216 | -41.53667 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15c4f8b8-62b9-3262-9a0c-ccc0ba2cd7e9 | -6.09803 | -44.01791 | 2025-10-20 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e7567be-d4ea-31c0-bdae-bf4ea371a9cb | -6.5526 | -41.661 | 2025-10-20 03:51:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| cbc699ff-c0dc-3cd0-a7f8-fa700001d435 | -7.13135 | -44.24692 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 60ff6e79-7bcf-31ed-b292-93b3c5b54480 | -7.41512 | -40.06866 | 2025-10-20 03:51:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 457d1ab0-899c-31d6-8a35-383e872db619 | -10.15775 | -42.212 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5daa296b-efcc-3217-a2a6-4f0f2aaa1c07 | -7.1416 | -44.24349 | 2025-10-20 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0418dd32-194e-3696-8ebe-7e945f5bb105 | -10.49434 | -43.3727 | 2025-10-20 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3940078-71b2-3c7c-8f80-7eee0116435b | -6.21551 | -40.96974 | 2025-10-20 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 08050807-6ac1-384e-be4f-8c720841c6a2 | -6.89031 | -43.59815 | 2025-10-20 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 26b4ba91-d985-3468-a7b4-23f3db0f5ae9 | -4.18258 | -42.19151 | 2025-10-20 03:51:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e7d097d9-96e8-3617-bc89-08909275290f | -7.21 | -45.42028 | 2025-10-20 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f7107a3-0c29-3ace-b8e5-f07f4f7f7346 | -5.36252 | -45.50743 | 2025-10-20 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 309a269e-b168-3a18-92be-6473ace2965e | -9.76298 | -41.91671 | 2025-10-20 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README8.md)
