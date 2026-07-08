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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62b5f766-db4e-35e7-bbf6-d32e93183988 | -5.3054 | -47.23968 | 2026-07-08 04:23:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0b877b7-d4ef-377d-8fc8-918e27718ca2 | -5.47241 | -45.42535 | 2026-07-08 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ef4b362-60eb-3e42-a557-87f462418c20 | -6.94067 | -43.69732 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed674697-9263-31c7-a259-ff6e20f08b55 | -6.92506 | -43.70951 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5532ae87-4a99-3e12-9002-74967ffcdca5 | -5.30893 | -47.24023 | 2026-07-08 04:23:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 500df42a-7d8d-31f1-a49f-864ecc363365 | -5.83056 | -43.48219 | 2026-07-08 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cebd919-b637-3b63-8cb4-8795e76dc2ff | -4.5426 | -47.80225 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d12cc728-2549-38e7-998b-714d3a1dc13b | -7.63983 | -50.02328 | 2026-07-08 04:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c25ffc64-9104-3818-87a3-2063e3ff6385 | -5.48183 | -44.10186 | 2026-07-08 04:23:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a65fb66-bc50-36ad-8e38-17d37f05f301 | -7.01224 | -42.77887 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 607e313b-3846-3e8e-aa24-dc64711035a9 | -6.93621 | -43.70395 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0927b6ba-77fc-30e5-a93c-a232935b3dbc | -5.79672 | -43.63256 | 2026-07-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb3da1ac-9ce6-3169-be7f-0c1f80a753cc | -7.29848 | -46.24575 | 2026-07-08 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86f779cb-8cc3-3c86-8b59-cf2eaab1dd09 | -6.95857 | -42.06454 | 2026-07-08 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9726a01a-74c2-36e8-ae8b-9250c928d949 | -5.30469 | -43.06093 | 2026-07-08 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b5b528c-7e98-3a13-94c6-6739c97d9165 | -8.12831 | -47.09868 | 2026-07-08 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7df4a122-86e7-34e7-aa00-e45af0818ff1 | -7.30241 | -46.24274 | 2026-07-08 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa2fc257-f299-3fe9-b6cf-b7aef70f719d | -7.75848 | -48.41899 | 2026-07-08 04:23:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 876a6249-1c90-39a0-adfd-b9c24c429c49 | -6.91391 | -43.71507 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec41dcda-50ef-3676-ae34-98da54c785c8 | -7.27266 | -46.81375 | 2026-07-08 04:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbc7654e-19bf-3c7d-81b0-de7da6682802 | -6.93677 | -43.70037 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe02255-e9e4-331b-9b67-84b0e76a380d | -3.4947 | -48.03527 | 2026-07-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 142bfa65-3fb7-3c25-b9f9-1b3999e6e35d | -4.2843 | -48.3574 | 2026-07-08 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53e246a7-0547-39b4-be52-fb3c8eda6379 | -6.91671 | -43.71915 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63f41a38-20d0-3c42-865b-31634d576b8e | -6.92616 | -43.70238 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35164742-fa2a-3d8a-b4df-543d4540c240 | -6.94737 | -43.69836 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac96f4b0-66ac-31c2-820d-cc5759a45e03 | -8.10938 | -47.10716 | 2026-07-08 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92349d92-2f80-3fd1-9324-62ea57ea0606 | -8.12709 | -47.10612 | 2026-07-08 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6b7b202-e1e7-3172-ac1d-b5d2d57e23b6 | -7.25666 | -45.10574 | 2026-07-08 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fef55a6-8217-314b-9e8f-18af2a083343 | -6.94236 | -43.70855 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc668230-4e74-351b-bc44-227bfb19b796 | -6.93286 | -43.70342 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3a5e98d-31ad-3557-86d3-cbf7c33093fd | -2.43072 | -47.02795 | 2026-07-08 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52054467-e315-3e5a-9aa7-f01f081ca335 | -7.29906 | -46.2422 | 2026-07-08 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3d69b68-8679-373e-8731-7427c8f6505e | -5.33769 | -44.71142 | 2026-07-08 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a746a678-21f7-353b-ac83-c739c86c1289 | -6.94292 | -43.70498 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a007fe28-13a0-3eed-86a9-a5ec3c175888 | -4.18346 | -47.84296 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 985b1d1a-7be1-33d6-9f48-b6accc2784d9 | -6.94012 | -43.70089 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b8ab3410-b21d-3746-8885-dd587327ddf5 | -4.94231 | -48.24707 | 2026-07-08 04:23:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a4a2568-8c94-30f5-a26e-1ea9faf131a1 | -6.90614 | -43.70675 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbbc94cc-705c-3aac-98fa-76fd7c7d6e8b | -6.93956 | -43.70446 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e15f8a5e-4c0d-31ff-a526-69c888492b30 | -5.6646 | -44.3004 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 396195fa-1a39-371e-b64b-b2b701d01466 | -7.00651 | -42.77025 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 571ebc50-dc7d-3c87-b9b9-1ac33e4be678 | -5.80189 | -43.79521 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd2f251-14bd-3427-947b-e54ae5173e20 | -6.90223 | -43.70978 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe43c0e2-b459-36c7-aa43-bbe82f9cc22b | -5.43915 | -46.28576 | 2026-07-08 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bfd427b3-cc2c-3179-a971-8cc310d9748c | -6.94347 | -43.70141 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04282063-bbb5-33c2-b628-719562fece4c | -6.41271 | -51.23308 | 2026-07-08 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5069a96-91d7-39f1-ab54-d120dd398e44 | -4.34627 | -47.76531 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fa52de94-4899-3477-b815-038e01a573d4 | -4.41375 | -47.60247 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98307c3f-7d42-3785-b8e9-b59a71daee6a | -3.49397 | -48.03984 | 2026-07-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f4ac6cb-f8e9-37bc-adac-514b6da59ffb | -6.84563 | -50.64629 | 2026-07-08 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c9e2f2b-4e80-38dd-80ea-c05fa8744e67 | -4.18402 | -47.8444 | 2026-07-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cdcb867-0af7-37f5-9ee5-ed2e8eb6a8ad | -13.47586 | -49.91281 | 2026-07-08 04:25:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ded1cc0b-ad44-3068-bed3-71dfa4932612 | -14.14186 | -52.88234 | 2026-07-08 04:25:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f2cb1a67-8b57-39dd-a122-4d99354dd01f | -13.95264 | -45.21885 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 99886498-8083-3b6f-8326-64cfecf4a6db | -13.32747 | -54.38723 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a69368ec-2725-39b2-a50d-99eeceab9027 | -11.32153 | -54.47897 | 2026-07-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 528636b0-98c7-3915-979a-3e941a450171 | -13.28459 | -45.16996 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77bf0341-fca2-34af-86dd-e4a10a47b405 | -12.35064 | -47.42067 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 890ede66-0762-3578-b7c1-2b786f6f0336 | -11.69504 | -44.14026 | 2026-07-08 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 997603e7-7b2a-3cf9-8c74-cc92fc8f18b8 | -12.7521 | -44.46225 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8a4ed47b-83c4-3ad8-8dee-03dd85c11950 | -9.22078 | -48.58055 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 67eaacad-8589-3595-ae28-510064e6208e | -12.75966 | -44.53197 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c603eb0a-713a-32e4-aece-2ac3763b2921 | -12.78503 | -44.45566 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f88781f8-a896-36c5-8621-ff6408bbf86e | -10.76729 | -45.02936 | 2026-07-08 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99766850-22e1-3b87-8d24-ce2bacff27a4 | -11.99339 | -45.13575 | 2026-07-08 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1f06808-cdee-3a71-ad96-f17f9c998289 | -10.49551 | -50.25376 | 2026-07-08 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0cadd84-ad3f-3fdc-aa33-1b19a92c9efd | -12.13218 | -48.25836 | 2026-07-08 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79e7af93-ad44-3b45-b53c-9c1e72f57862 | -13.28682 | -45.17775 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cfdb730-5f56-39de-9c1e-f6a42fd6f2a5 | -14.73386 | -47.14571 | 2026-07-08 04:25:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13346dc6-41da-35a0-a92b-36bcf72f2d4d | -9.22437 | -48.58122 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3abb1376-4bce-3373-a395-a20bcd0df9e9 | -9.3032 | -51.92039 | 2026-07-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 131e1ac8-265f-3dac-9d83-e1738d828d50 | -12.13499 | -48.26279 | 2026-07-08 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bab6fe0d-ef8a-386b-ae26-ff482b02c585 | -13.29324 | -54.40876 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33fc188c-de8a-3d43-84f0-73ce28853018 | -12.49797 | -48.25204 | 2026-07-08 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0846e31a-a2c6-388e-aa51-ad8a46c76a01 | -12.35005 | -47.42429 | 2026-07-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d961bd6-28ab-333a-a690-9fc7452433ef | -12.13562 | -48.25896 | 2026-07-08 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f137ed3-a339-3df2-9aa1-6048bef2e569 | -11.90753 | -55.90966 | 2026-07-08 04:25:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 748ce2b9-de68-32c6-a746-e39031b29ad8 | -12.54241 | -43.16044 | 2026-07-08 04:25:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df0d86f5-54ed-37ae-871d-6d19d736ad40 | -9.23418 | -50.14213 | 2026-07-08 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03b92cdb-429e-3777-9a86-ac98320e10f7 | -13.47876 | -49.91786 | 2026-07-08 04:25:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7ba9c27-00e0-3774-a460-17e735a94357 | -13.28571 | -45.18499 | 2026-07-08 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78fab4f6-036d-3172-8744-f9771f8e13e0 | -13.27871 | -54.40586 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 31bedb20-4306-39a3-b80b-2ee1edbf6b91 | -14.47539 | -51.82936 | 2026-07-08 04:25:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d085598-1141-311c-b849-da544bfcc171 | -13.95401 | -45.22276 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4bd8b7e1-c082-3aa8-9210-08ed71e9ab92 | -13.33334 | -54.38268 | 2026-07-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbb63143-d3d3-31b3-8752-9d03f1f3a821 | -13.53721 | -52.94247 | 2026-07-08 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5792dd9a-1168-3eec-9011-c6aef30642a2 | -10.94435 | -43.05373 | 2026-07-08 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9e05b12-855b-3f9b-93f6-dbee14d6d210 | -13.95207 | -45.22252 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cd1860cb-c683-339c-bf2f-e878a67ec91c | -12.63349 | -44.64901 | 2026-07-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c8adea4-97f1-3e75-abc7-922aae2811a8 | -12.78162 | -44.45513 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 54a509e6-8251-31b4-90e2-9d1730977de9 | -13.95848 | -45.21599 | 2026-07-08 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b31387a6-73d6-395b-ab21-1301125d1304 | -9.22367 | -48.58537 | 2026-07-08 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2073e818-454d-36c2-9718-6646d68ae73b | -12.76249 | -44.53623 | 2026-07-08 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d58a2348-c251-3fcc-b141-b39a26b143be | -13.9129 | -47.34802 | 2026-07-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cc3cec6-b0b6-3ed5-8f41-265a060f4cc1 | -13.47221 | -49.91215 | 2026-07-08 04:25:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 541f4401-f8a6-32b0-9d64-d2e472a1bcfc | -13.91897 | -47.3527 | 2026-07-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da9b5503-0952-38cf-9015-e9edd2c5fdbc | -14.73055 | -47.14515 | 2026-07-08 04:25:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76444923-1255-341d-bd8a-ec6cdb774bbc | -13.91074 | -47.3403 | 2026-07-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68bc7bca-331e-33d8-925f-684f8a975d25 | -15.57974 | -48.23859 | 2026-07-08 04:25:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
