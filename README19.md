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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60817589-ffb3-3ff9-b00a-41bbba2ca0fc | -15.6324 | -47.80095 | 2025-08-04 04:36:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6087de18-d14a-3e4b-8899-d4c23f8f6853 | -13.0707 | -56.91983 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 21e5bd29-0733-30e8-8f5b-a34f939543a9 | -13.24713 | -46.97269 | 2025-08-04 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e06bbe7-0e51-3923-aaae-59931a852382 | -13.05947 | -56.90152 | 2025-08-04 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7880ccf8-34e8-38d8-ba4d-13625e66d4c3 | -13.25062 | -46.97322 | 2025-08-04 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01a57695-1801-327a-8f46-a1daff11ec76 | -10.25111 | -50.1642 | 2025-08-04 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db500d99-42ce-3f92-9081-8cc7d8b3ceb8 | -12.12954 | -45.02743 | 2025-08-04 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5d8a44f-ebef-3229-bece-fa8d52e8ab92 | -12.14241 | -43.37446 | 2025-08-04 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b9cf1b2-6868-32b2-a49d-bf6d02338d78 | -11.22069 | -51.52879 | 2025-08-04 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95e61583-5622-368e-a1b3-16ebdbc8f43e | -12.48506 | -51.76779 | 2025-08-04 04:36:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c07c0be-f566-38e2-945e-0ead408c4355 | -11.92511 | -44.97849 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7066576e-9471-34f9-8d00-c5d967a9cfb4 | -11.92698 | -44.96531 | 2025-08-04 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 282cc3e3-e353-3d86-b3cc-4f0e98706304 | -22.5646 | -42.16826 | 2025-08-04 04:38:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6354941b-7f30-38a2-b6b4-4db09fcb205a | -18.97989 | -44.52749 | 2025-08-04 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e328df7f-4630-3dae-a468-f12cca013810 | -19.80624 | -42.39516 | 2025-08-04 04:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 224a83d3-eeb1-3141-9c03-d59f08723c7f | -19.57776 | -46.95089 | 2025-08-04 04:38:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a91a75d5-d928-3c80-b939-259ab2c506c3 | -21.93303 | -46.20081 | 2025-08-04 04:38:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 185ff8c9-8cf3-38c4-84c3-ebc617c80a9e | -17.36852 | -46.08478 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e4b0e66-dc30-38fb-8902-df484abb5019 | -21.9246 | -46.06656 | 2025-08-04 04:38:00 | NPP-375D | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a1cf9f77-cf79-36ef-ba20-111919f1a55d | -18.37061 | -49.27108 | 2025-08-04 04:38:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ef9301c-df06-35ee-b80f-c35270c14ef5 | -15.70348 | -48.99197 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e24a46c8-55f5-3f8d-a9a5-378251b973b3 | -15.69568 | -48.99805 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6e84495-ac3f-343d-b9fc-13eb0fbfb69e | -16.92259 | -49.45755 | 2025-08-04 04:38:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d2c1208-d0b8-3e1c-a3bf-caba542ed9fd | -22.56494 | -42.16483 | 2025-08-04 04:38:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 71533814-051a-36a2-99e9-993aeae9b5b7 | -16.17863 | -46.96014 | 2025-08-04 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb61a2bf-cc1d-3eec-96aa-b99d6c867a6a | -16.14288 | -50.24609 | 2025-08-04 04:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5ee1851-5fa0-3284-865a-b20b8c75f097 | -19.3316 | -44.15893 | 2025-08-04 04:38:00 | NPP-375D | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fc125f2-162d-3ffc-8197-b0288a1effbd | -19.09619 | -43.60289 | 2025-08-04 04:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7be6a76e-4c58-360b-8467-0385d3f7274c | -19.57773 | -46.9491 | 2025-08-04 04:38:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1216783-c401-3fc3-8487-2e14de35a824 | -16.42937 | -43.72327 | 2025-08-04 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7d8a999-abfc-3cf7-a81c-beced66b5384 | -22.55968 | -42.16421 | 2025-08-04 04:38:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5655cdf8-8a02-323f-8729-e2d56582a9a4 | -21.25271 | -43.97677 | 2025-08-04 04:38:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 757e8c5a-7574-3135-b500-e36aa7bde965 | -17.3615 | -46.079 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66dfad16-c790-363a-bb9b-87bec9a90fd1 | -19.80822 | -47.93034 | 2025-08-04 04:38:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b3fd19f-a627-3e69-ab6b-1ed5e4e73b88 | -18.98418 | -44.52816 | 2025-08-04 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 376c7eb2-b0c2-3c99-b6fd-c484aa61ae5d | -22.46652 | -43.83995 | 2025-08-04 04:38:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 408f83ba-7614-3501-8545-3011391b4928 | -23.25307 | -46.03044 | 2025-08-04 04:38:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| daf87924-897f-367e-b4cb-f1008fa6d867 | -20.08634 | -44.0151 | 2025-08-04 04:38:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 778399bf-8324-3ffe-8606-5f050b5e21b7 | -21.92054 | -46.06603 | 2025-08-04 04:38:00 | NPP-375D | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 49bcc940-3c3f-3a9a-af4f-443e74286279 | -15.70182 | -49.00275 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 88c13ad2-2325-3895-9153-14bde8a4f879 | -17.99771 | -44.33271 | 2025-08-04 04:38:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1c4a4cb-7464-3e81-8143-d3d3d245e278 | -19.99347 | -44.42759 | 2025-08-04 04:38:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46c37e4e-fb7d-3299-9a04-d61cd5d9a191 | -16.92537 | -49.46173 | 2025-08-04 04:38:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79a6ea49-543e-3b10-b91b-5549c80d5816 | -17.37171 | -46.08995 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8dcca3a-1208-3a9e-9e38-7605dafc0a36 | -21.93646 | -46.19938 | 2025-08-04 04:38:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3bac06ca-3b74-31ae-8ce0-f94b1783e360 | -15.69958 | -48.995 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36e208c6-0dec-3674-9bce-1c0a1f76e458 | -15.70293 | -48.99556 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc009aa0-87ee-380d-9463-cc479844da18 | -19.806 | -42.39551 | 2025-08-04 04:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b73d06c1-e3bc-322e-b605-4d31887dfcbb | -21.93174 | -46.20427 | 2025-08-04 04:38:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1b8162e0-1f69-336a-a8da-3264d815ce81 | -21.93348 | -46.19717 | 2025-08-04 04:38:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8dff8da0-41f6-3763-a006-2bac0ee027c9 | -17.37109 | -46.09453 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84e98ed9-8750-3ae5-b11a-bf659fbf28de | -21.93244 | -46.19876 | 2025-08-04 04:38:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0d4a5a02-14d9-363c-9656-d253618d316e | -20.00457 | -45.39571 | 2025-08-04 04:38:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 839f0023-d335-35e5-a01e-22e900b45829 | -16.42499 | -43.72265 | 2025-08-04 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91e964fe-bc63-3e0a-8217-c3818b5af6e1 | -21.87862 | -46.13761 | 2025-08-04 04:38:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 168f4c57-b9bf-3412-bc54-e3327ae24eff | -17.37234 | -46.08532 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89c81ceb-b336-38d1-91c1-f75e7e06ef09 | -17.6101 | -46.70779 | 2025-08-04 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11807347-c6ed-39a4-ab6d-78533ca48424 | -16.92315 | -49.45391 | 2025-08-04 04:38:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd9f7304-8e2e-3054-8cdb-a9c813802cb7 | -22.92052 | -43.70524 | 2025-08-04 04:38:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c9c4b54e-f56c-3fdc-897b-a6745a12c9bc | -17.96694 | -52.56567 | 2025-08-04 04:38:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a12da543-1075-37f3-a55f-8b09525df7c8 | -21.25676 | -43.98231 | 2025-08-04 04:38:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 49f882a9-963e-30db-9d1a-89dd1838149b | -16.42992 | -43.71894 | 2025-08-04 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92f4e5ed-5167-3a54-adeb-466ec5e48754 | -21.93247 | -46.20543 | 2025-08-04 04:38:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2bc8644-3ab1-386d-8ff1-5e8f0b25c412 | -16.89315 | -46.68781 | 2025-08-04 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8d416e-e4d3-375a-ac14-bb2dae33bf5c | -22.56036 | -42.15735 | 2025-08-04 04:38:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a893da0d-40a8-349f-a06a-aada5d28c03b | -22.56002 | -42.16078 | 2025-08-04 04:38:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a7e37ab3-1fae-3f52-a34d-de823eef9363 | -21.25216 | -43.98173 | 2025-08-04 04:38:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5eefcc25-6032-3d16-a882-08475820535a | -16.13406 | -46.88122 | 2025-08-04 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbf2df9f-cdc4-399c-8092-fc1cc8631926 | -19.52298 | -46.90228 | 2025-08-04 04:38:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2349d359-70cd-3748-902f-eb6b637552bb | -15.70238 | -48.99916 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 619f3bdd-a71a-3007-9ef0-21915a18e915 | -21.91959 | -46.07355 | 2025-08-04 04:38:00 | NPP-375D | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 92321d90-507e-3eb9-bd36-bbf278f1a5a8 | -20.72106 | -47.28974 | 2025-08-04 04:38:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e809fb60-c2d5-3a2f-b659-533afa351ef4 | -17.36597 | -46.07477 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db71e105-310e-3449-b12b-9efc2bc46575 | -15.69847 | -49.00221 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b0a45fe-4fef-3f68-acaf-c2de821f7846 | -17.46594 | -47.10181 | 2025-08-04 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 539cec60-68e8-30e0-96c2-03a8c4c28a74 | -16.92593 | -49.4581 | 2025-08-04 04:38:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 047faf25-110d-37ac-b416-d37aed8ca01b | -20.09144 | -44.01063 | 2025-08-04 04:38:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 23c651f6-7d1f-3c5c-b653-076a86981282 | -16.42555 | -43.71832 | 2025-08-04 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1681d4e0-96e7-330f-8d44-fe4c7efecf2a | -17.99722 | -44.33669 | 2025-08-04 04:38:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7d83345-3a0b-34fb-9c30-4d5b0050106a | -17.71606 | -48.64106 | 2025-08-04 04:38:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62ec43c9-79af-3f49-9808-78d5c0248f72 | -17.67463 | -44.12794 | 2025-08-04 04:38:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37340575-126f-32f1-b58d-2d80eb00a178 | -20.72203 | -47.29193 | 2025-08-04 04:38:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ed91f24-14ce-3d89-93c4-cd5fe103fb9d | -19.10076 | -43.6036 | 2025-08-04 04:38:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d183d6b5-272e-3e74-bb78-aa7f4eb93f20 | -18.21919 | -48.95745 | 2025-08-04 04:38:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4ec26a9c-d354-3cf9-bd2e-1b3597ea5db9 | -16.17503 | -46.95959 | 2025-08-04 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 109d1867-1e6d-3967-accd-6e975590d3a9 | -17.36914 | -46.08014 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ce18fc8-e4f0-3896-9fd7-60ea962c46a2 | -16.13767 | -46.8818 | 2025-08-04 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 661c251d-2463-3071-8e25-71010c303422 | -19.33106 | -44.16345 | 2025-08-04 04:38:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6af72cd9-a255-3c1a-b7f2-a6f70363ae08 | -20.00236 | -45.39407 | 2025-08-04 04:38:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75a82428-ae54-3c55-9521-01970f3b77a4 | -17.35769 | -46.0784 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e4cdb73-ffa4-3611-b93a-667af19d72f9 | -18.0 | -44.33514 | 2025-08-04 04:38:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0de7f90e-0497-362d-b3bd-7440315fa535 | -18.98039 | -44.52341 | 2025-08-04 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af71f492-83cb-3d4d-b66e-7836e94993c3 | -17.3609 | -46.0835 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8d53aa0-6f0f-3056-96e6-85b2a3e595c9 | -19.52234 | -46.90701 | 2025-08-04 04:38:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b486dce1-ec77-39ef-80ab-c1fefbf63574 | -21.87909 | -46.13383 | 2025-08-04 04:38:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cb3a1db1-0c7b-3b0e-be6b-cb68eabc1bb7 | -20.0019 | -45.39785 | 2025-08-04 04:38:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7990a00f-372d-39d4-a668-6e55032ddb67 | -17.96929 | -52.56504 | 2025-08-04 04:38:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7671974-a717-368b-8d85-01b29ad0f8f7 | -17.3698 | -46.07526 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d4467b2-24d7-3f7d-a8d1-ecb3d349fc93 | -15.70014 | -48.99141 | 2025-08-04 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d44573c-8223-38b0-a7bc-6cfa3747a783 | -18.2198 | -48.95388 | 2025-08-04 04:38:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
