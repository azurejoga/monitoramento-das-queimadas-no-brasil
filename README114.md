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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e57fe19-59c9-32f4-b1ee-9b56787f9695 | -9.69276 | -46.56796 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 1189729a-83e5-34ae-abde-598d450cc4ee | -10.88274 | -50.50842 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d8788322-218b-3f21-ba3e-894e832f6ee2 | -9.8662 | -45.85376 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 622b12e8-4c46-3ac0-8c30-71f52a99a4ed | -15.35657 | -52.83569 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 806ee910-4ed7-319b-85be-7c74f1a4403b | -11.0227 | -49.6582 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 97320611-59ee-339e-8c79-34db1b65ca06 | -14.18029 | -48.76796 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0ecc5ab6-cbbf-3dfe-b5ea-a88a7a78b106 | -14.35874 | -53.11714 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e8085ab7-8865-3d21-984f-9c4caccab9bd | -9.79091 | -43.56486 | 2026-08-28 17:26:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 86756bb4-571a-3bc3-9e30-78793911d7b1 | -13.10885 | -50.05148 | 2026-08-28 17:26:00 | NPP-375 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8babb3ea-e0ea-321f-a380-dee83286e431 | -11.22285 | -53.98349 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e12d39df-5759-325f-8271-42ea248399af | -11.2936 | -54.02984 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| da8a8e02-734c-355d-ba9d-98ff4f1da38d | -11.22124 | -53.99538 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 78da0d41-5bd2-3c9d-9209-dade434f576e | -9.82871 | -45.90604 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 03cd1952-72be-3cc6-b5b4-89a4b7b645ea | -13.87582 | -54.11642 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d537e033-f9da-3c85-b82a-553614bff04f | -11.23497 | -53.99311 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 31d4aa51-c402-3b22-a701-6f0311f379ac | -11.20003 | -53.99497 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 655909b4-2334-331f-a89d-da00d189b929 | -10.77437 | -50.63055 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7372abd1-f665-3837-930b-3aef314631b3 | -9.6934 | -46.57149 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| ec829b3e-82fb-3ecf-9181-d43b47441de3 | -16.72283 | -49.10405 | 2026-08-28 17:26:00 | NPP-375 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56be729d-2ced-325c-9f94-c57d84305554 | -11.23093 | -53.98992 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 33d21728-baa8-3bec-aa51-8de0faa10280 | -14.19249 | -52.84966 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 237ef36a-6adc-372f-97f7-37a9a9704884 | -11.02723 | -49.68351 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 2879c336-80fa-3402-835c-748d3ce15891 | -13.86226 | -54.09618 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48756341-79db-3f11-bded-12633ccc2b37 | -11.76212 | -47.62907 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 1de7a7d5-4881-3011-9c1c-91865c97fe88 | -12.38515 | -48.20644 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ff598e66-6018-3101-8d6b-77a3c770f351 | -10.31959 | -49.96057 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0f8434de-2d2e-331c-aa5d-d8dbba8d4ba6 | -11.239 | -53.9963 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 9dc8e7fb-ef81-3bbe-b0fe-1238cc78c81a | -15.60785 | -56.40783 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4388a384-3f99-32df-be67-982f9be095d1 | -11.24692 | -45.05946 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 75bf7dfd-7dea-39d3-ac49-f6f028a6ec50 | -13.33204 | -46.9216 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1ec04b59-c9b7-33aa-b992-995ccca1c3f7 | -10.7627 | -50.63639 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bfa1f161-3737-3265-9d74-449bc75f842f | -10.55168 | -50.42149 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c667e259-455b-3898-ba52-24f0cfec491a | -13.66046 | -47.7463 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 6e064c64-c136-3fe0-9dc1-3124dc38d07e | -9.88939 | -46.35 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 26e4e553-dade-3630-acde-2aae8dc3198f | -11.62217 | -54.58442 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 0e106a24-278a-39be-9b4d-0a719d972c29 | -11.25279 | -45.05833 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 493d68df-d883-30ff-9557-5fa5ba8a025f | -10.92822 | -50.55066 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4ae63a7f-4c81-363f-8d20-f7e2b57a7627 | -9.86047 | -45.85476 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4ab46d67-0a94-328b-b4c8-9a28e4a7b517 | -13.86572 | -54.1181 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dec35d1c-1a9a-3feb-b070-0155c64e7be0 | -11.8218 | -47.22939 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83e8f7c4-f9bb-32df-9fc3-aa668dce31ab | -15.46291 | -53.97871 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e9db6d8-6928-3c60-aafb-f87532605fdb | -13.58371 | -45.77969 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 3e0c161a-c4fd-30bb-b704-c730021cf1c3 | -9.66883 | -45.13129 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22fe3e9e-7ca7-3482-84c6-461bdfedcdc3 | -12.3833 | -48.1965 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 38121165-1039-3d5f-82f4-3291ff7dccde | -10.0637 | -48.6699 | 2026-08-28 17:26:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d887d74e-7c81-31a5-9f08-8478f69b8345 | -11.34986 | -48.40062 | 2026-08-28 17:26:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5312e25a-344f-3675-a41a-1f363c6448a6 | -10.48394 | -49.95309 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b63df2e6-aa97-3037-a831-7fd8cce5e167 | -13.88036 | -53.24494 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3be988e7-6002-30e6-9b6b-6b76468a7df7 | -11.00942 | -49.6343 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| adda63a5-6665-3838-8821-35c796891a7b | -14.91666 | -56.32101 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| a2943fcc-73fc-3015-af2f-ec46e4981d1b | -13.88546 | -53.24018 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e29ec59c-1b0c-35d9-8e60-55acc5c441ba | -13.8629 | -43.63872 | 2026-08-28 17:26:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b7afea2-ab08-3e77-9df9-460fce7d9baf | -12.08925 | -47.18039 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 033f8ea5-1eb9-3f8f-832c-48f02347b05e | -11.48727 | -46.9413 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 248970f6-a676-3331-b015-f2e7424b6997 | -10.86022 | -44.80453 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b1cbc27e-eb80-380f-b10c-f06bf062c4eb | -10.86206 | -44.80493 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 199b1b87-f26c-3c3a-afa0-e35760a5abc2 | -10.77027 | -50.63127 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 42fd3443-cd7c-308b-984f-d66acbf240d0 | -10.06359 | -48.67188 | 2026-08-28 17:26:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35e57b0e-2e35-39ed-91a2-3dbb94779b55 | -14.42794 | -52.58884 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 58f76ef8-82f6-34ce-a9d9-b9b915203aea | -14.43097 | -42.2101 | 2026-08-28 17:26:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 39238eb8-fac4-30e9-a12a-9245754ec1c5 | -11.24759 | -45.05056 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 970f9c2a-291f-3926-802f-98caecdcdc25 | -10.64115 | -44.74252 | 2026-08-28 17:26:00 | NPP-375 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 446dba33-55f1-37d2-86f8-884005e8a804 | -10.83314 | -50.51704 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1cfc4918-ad0f-3118-a2c2-f29407905803 | -16.586 | -49.78007 | 2026-08-28 17:26:00 | NPP-375 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| b6381608-fc13-393b-bf07-ed26518c450e | -10.4679 | -46.17782 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7680518-99d1-3e51-928b-07dd6341df2f | -11.79696 | -47.67997 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c550e2c0-f010-37ea-890a-77260135edae | -12.79199 | -46.45586 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 851851e4-77f6-3c4a-9584-ad20be0408a7 | -14.18268 | -52.85537 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d73fa3b4-0675-3adb-ae76-db5736e8fe0f | -14.91558 | -56.3136 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 98a78921-3c22-3bdd-a35a-d331430d7b94 | -9.86897 | -46.33305 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d449b52-abd9-3462-83b8-e3313ef60ac5 | -12.77448 | -46.44571 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 192e3328-e4fa-3004-9091-3bf331223013 | -11.28377 | -54.01221 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 94e550f2-169f-395d-8b51-0a9289a3001c | -11.24499 | -47.05648 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31b37344-c1eb-36e7-80ea-5da5314ef015 | -14.45686 | -53.38185 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ec39bb0c-6d8f-3c34-9d3d-99c55e0cf8ad | -10.5655 | -50.50177 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 8e1a3c2a-30e1-35ae-a7e2-fa2f19da1010 | -15.89968 | -56.23594 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 79aaf5b2-4dc5-3462-9339-66f99d4e4cae | -11.48384 | -45.07806 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ed90db0f-fff3-3164-9c8e-78a9b0d6ecda | -10.47477 | -46.17765 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 352dba0b-8b18-386e-92f1-3cb4ae9db575 | -13.60599 | -45.77942 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 21c068c7-4ac3-30db-accd-d7cba952ff54 | -10.02729 | -45.82045 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6a8ce035-9540-3038-817a-ba7bb8ff5f1c | -11.48301 | -45.07386 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 008fa9ff-0e4a-3c8c-81b2-b3ecd9dc560c | -14.59728 | -53.14346 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ef1e2dcd-f9a8-3bef-a6e5-7d4f5b17df69 | -9.8575 | -45.83883 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f17b979-edd3-3e48-9b7a-20ae33761b7e | -10.00016 | -45.58299 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c866547d-6dff-3962-8101-36547b114971 | -11.29419 | -54.03358 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d8f5dedc-c29a-3bb3-825a-1583ab8da171 | -9.88221 | -46.34233 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d519d64-4922-3b4a-bd40-24707227b665 | -9.69273 | -46.56836 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 19aa89e1-6e9c-33e3-aa6d-a3e2395c7d0d | -18.10689 | -51.6153 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 77215d0a-2b82-3b2a-b73d-10149753f460 | -14.88558 | -52.60582 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 978495fa-4e4b-3bae-877e-d6da375e36b8 | -10.46291 | -46.17556 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| c86a8620-6993-31a0-9c0c-246d515ec1ae | -11.76315 | -47.63462 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| c4d24596-4f94-3b3f-a1c7-c09545398301 | -14.4228 | -51.74099 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6c1e901c-4730-3dcd-bfde-ad0d08cc6294 | -11.84649 | -47.22157 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5676780-381e-3d23-b32e-23fc3a97f524 | -12.78642 | -45.94329 | 2026-08-28 17:26:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0c196c04-6d0a-3a3d-95bb-c4034d0ba58c | -14.87704 | -52.61931 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2511f50e-8314-3753-9206-d629625d091f | -13.38102 | -50.22911 | 2026-08-28 17:26:00 | NPP-375 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 34af4a3a-6b4f-3bb0-a470-20313d9821a0 | -11.2399 | -47.05782 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4095510c-3176-38c9-b267-0663fe98759f | -10.30736 | -49.96698 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| affe3158-1a8e-3369-a9f0-c666d7e81d42 | -15.4024 | -52.85574 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8864d081-c95d-3d60-b82c-1b03ec4d3d77 | -10.53899 | -50.77995 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README115.md)
