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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7527ffca-ff7a-382c-ae76-59ac55b39034 | -21.73332 | -52.25533 | 2025-07-24 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 127a03d2-6b96-3178-acc7-05091a56a36d | -14.18141 | -45.34962 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 869380ca-5005-38df-b34b-56b72dfc24d2 | -21.36954 | -48.52814 | 2025-07-24 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1212e93f-ab2d-398b-a7c6-5deb99066edd | -10.71029 | -48.86047 | 2025-07-24 04:17:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf13393a-30ff-3942-aec2-d0d1c407ec80 | -23.29737 | -46.12477 | 2025-07-24 04:17:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 130faa92-3112-32ab-9618-556688fd00aa | -13.70145 | -45.67447 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 987f1644-ef42-38a1-9d32-afd982a5e280 | -10.71839 | -49.48545 | 2025-07-24 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44d88754-cf45-3e6f-8482-337552ec7e59 | -13.70534 | -45.67146 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e302acd4-7648-37a8-8949-80f8ae0354e9 | -8.29916 | -55.10335 | 2025-07-24 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0abe1d8f-02df-328b-9274-ce9ee220ba1d | -13.0972 | -45.06499 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f0a1fdd-9504-3057-afe2-19818b2deb0e | -11.77648 | -47.4048 | 2025-07-24 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf68634e-0fac-3e39-a68e-1f6f0c8d1420 | -22.40078 | -49.79508 | 2025-07-24 04:17:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c158b6a0-dcdd-3529-940f-f93adc6be65a | -20.04189 | -45.64827 | 2025-07-24 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0852ff7f-cbfe-3f81-b8e4-24ae6f0ac0d5 | -16.74516 | -49.17846 | 2025-07-24 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90135a56-dfa8-388e-a19f-ece4415a9c5d | -23.28197 | -46.58583 | 2025-07-24 04:17:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| de309b29-de62-3139-a121-2ff2cdd44a97 | -22.81779 | -47.15122 | 2025-07-24 04:17:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 34fdb9e3-9907-3da0-8b3f-8df35f858c56 | -11.46521 | -48.16227 | 2025-07-24 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1cd4e4b-b4d6-3511-b8de-491a4085fd67 | -10.62514 | -45.22992 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f8fcd112-903b-3647-8d57-4420d68aaa70 | -13.7042 | -45.67859 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dcbbd7a-ee9b-36fb-9d51-1d4672ea559c | -12.66226 | -45.04081 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd435f54-58c4-3478-aba4-2d4de9b8a0ad | -13.2165 | -51.0864 | 2025-07-24 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03476074-1900-3970-b2a0-ad6110f56ed9 | -9.66749 | -48.52302 | 2025-07-24 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21d9af9c-1e82-3cd1-b6ba-a69349eba5d6 | -10.06661 | -46.85467 | 2025-07-24 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83ca5868-0df9-3eb0-9a28-0a6987a7d088 | -22.87002 | -47.09875 | 2025-07-24 04:17:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e3a07394-d835-3325-b471-489d564ce54d | -20.04133 | -45.65197 | 2025-07-24 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3f9c9ca5-fcd1-33c8-a6bf-c30675901cd6 | -10.62735 | -45.23759 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 764f70ab-4598-3fea-9712-1d29c61cf5ba | -10.66593 | -47.78244 | 2025-07-24 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8da3fbc-c5c2-3063-8e18-d606697afe52 | -20.29437 | -54.07682 | 2025-07-24 04:17:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfa34d11-2a86-3b95-a5c0-3314b34ca95e | -17.0451 | -43.77274 | 2025-07-24 04:17:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23cd1e0a-82c4-3165-a90c-c84c6f23c951 | -14.4826 | -46.35754 | 2025-07-24 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fd7a2b4-5584-388e-bd74-8ac01290fe94 | -15.73792 | -46.86585 | 2025-07-24 04:17:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7819e332-0ad4-3073-9d20-ca0ebc6da301 | -11.9949 | -45.15202 | 2025-07-24 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dde741cf-646d-3bd6-88a1-91fad5244a60 | -15.73516 | -46.86157 | 2025-07-24 04:17:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5190ae0a-a982-3633-85c2-b4bb0596f942 | -13.69975 | -45.68518 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e8cddcf-3707-347a-8956-0dd3e05132ed | -21.76314 | -52.75587 | 2025-07-24 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| defc1fa8-785e-37e2-93c8-57a69fe1dc38 | -13.70477 | -45.67503 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7af8c34e-7ab4-3747-95ac-c9c5ca244e2b | -15.27501 | -47.13672 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06bdb1b0-18eb-3f0c-96f8-7897a21831ee | -20.60952 | -46.35751 | 2025-07-24 04:17:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 593c8c3f-6424-380f-a9ca-269e82f205ff | -13.71311 | -45.66542 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1b0d923-2fda-3050-ae17-010b070ab6a1 | -13.70752 | -45.67915 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfae3230-0535-3d3e-b7b9-fbfd1549a70e | -19.07418 | -53.45725 | 2025-07-24 04:17:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d21bbd95-89f9-359e-bf29-5f069cfe3f7f | -10.00379 | -48.12739 | 2025-07-24 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 970d4f9c-67fc-3032-a763-ff0fe6282519 | -22.91735 | -47.25329 | 2025-07-24 04:17:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 44c17906-ea38-3934-846a-b423408c2744 | -12.42773 | -45.38299 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ea56c88-8d74-396d-a4f9-acd366733438 | -21.25674 | -45.99302 | 2025-07-24 04:17:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 14560fc9-9ac2-3630-b5bd-af1c3fbfc6dd | -14.30494 | -43.80144 | 2025-07-24 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dee32b86-553c-30de-ab14-5ce691511991 | -10.66517 | -47.78691 | 2025-07-24 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0faac885-0240-3f0e-948f-5e26d3837464 | -21.36551 | -48.53136 | 2025-07-24 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b090a9e-a3d0-38c1-8bab-768d50849ed8 | -9.66664 | -48.52792 | 2025-07-24 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d2788e4-92e3-3ffd-8dd9-a480d436a857 | -21.31016 | -48.56922 | 2025-07-24 04:17:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6107e65f-196a-3bb6-9c5c-c7186e33ea62 | -16.74439 | -49.18287 | 2025-07-24 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b27bd440-8f21-3044-93a1-9f339f1e1299 | -13.70202 | -45.67091 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3b1d92b-5ac1-37dd-acf7-792bb897c6e5 | -15.27039 | -42.25751 | 2025-07-24 04:17:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1d19c92a-7236-337e-a4d4-86671b3eda1a | -11.81389 | -44.26867 | 2025-07-24 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c73237d5-9242-326c-9ac3-a951a9151389 | -13.70971 | -45.68684 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9308b109-4dce-3100-b812-d0ffc4955381 | -15.28524 | -47.13835 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ead0383-6f80-31b1-b317-0b2cd1a5a92e | -16.69513 | -48.07197 | 2025-07-24 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c4f99a7-d722-3d2d-bb11-8473d48680e2 | -13.68139 | -47.74094 | 2025-07-24 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a287538a-ac1b-308f-953c-973682d61931 | -11.71979 | -47.76869 | 2025-07-24 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 675e5f78-8436-3e42-92a9-141a371d9154 | -21.79058 | -44.70449 | 2025-07-24 04:17:00 | NOAA-21 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aace5860-e8ac-358f-a4b9-cda95abc3af3 | -13.70866 | -45.672 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c5123a4-9a47-3d71-b651-1316e7462683 | -16.68071 | -49.09459 | 2025-07-24 04:17:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 395a56f5-9d9d-3ae1-8e72-027de31e9ede | -12.66282 | -45.03729 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d32e70d6-869c-375b-b151-e94818e41ebe | -13.01468 | -45.06978 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6a9459d-c73e-38d0-bff7-8d491c23bcf5 | -13.65029 | -45.71732 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2392c38-44a5-36df-9d07-52b158ec4cce | -14.2165 | -43.95528 | 2025-07-24 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ac2d154-e52c-385e-a459-489bd6efa2e6 | -14.87364 | -48.34026 | 2025-07-24 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b79d1e5-6608-3ee6-98b6-088e3040d2f6 | -21.19645 | -49.29507 | 2025-07-24 04:17:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 39c33422-98eb-3ae2-b46f-399fc58214d9 | -21.56708 | -48.50477 | 2025-07-24 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2afeea96-0c81-323c-bbb5-5310b805bbf8 | -11.733 | -48.18262 | 2025-07-24 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 142f31e9-1a03-3ae9-963d-a9682c6630a2 | -13.65362 | -45.71787 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa487bf3-afe1-30fe-9e27-553d6257960d | -20.28949 | -55.49542 | 2025-07-24 04:17:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64242327-51dd-3104-9103-39c9406b4b9e | -10.67101 | -47.79696 | 2025-07-24 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac34849e-960f-3db4-ab0a-ea5d945b657d | -21.47825 | -57.10682 | 2025-07-24 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d18bcf7b-3199-3cf4-ba27-a69c5bf2e1fd | -10.06862 | -46.84261 | 2025-07-24 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 914bbb52-facd-34a9-a730-3fb247aa02db | -15.76026 | -43.36884 | 2025-07-24 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8df5e681-0feb-35fd-90c5-c8baab77a4fe | -20.40279 | -54.63448 | 2025-07-24 04:17:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f27b298d-0200-3165-a815-728d185ee001 | -16.21897 | -45.97248 | 2025-07-24 04:17:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d55fd331-d1f6-350c-a576-52a13d3a6ac9 | -21.75569 | -52.75008 | 2025-07-24 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18af6a61-4270-3f0b-9f05-3bb9aadce383 | -9.73352 | -48.02231 | 2025-07-24 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e5b5c07-8937-32f1-82bf-a5957fd7b9ba | -10.96749 | -42.18243 | 2025-07-24 04:17:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1b18e0b-cc82-39e2-96fc-50cef2762863 | -16.4281 | -43.46986 | 2025-07-24 04:17:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5b23a19-e666-344a-ab8d-0b06d68e9b9c | -10.62791 | -45.23403 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72767a38-8c44-32d6-852b-594fa0b332c9 | -21.80916 | -47.25042 | 2025-07-24 04:17:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 42d80c5f-26fd-3161-a779-19dbe824b527 | -11.87447 | -48.63184 | 2025-07-24 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 156a691f-d605-3cff-8598-7b575ee558e8 | -22.86944 | -47.10249 | 2025-07-24 04:17:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4749ad13-4f6d-354c-bd2b-9e3a56892884 | -14.21316 | -43.95475 | 2025-07-24 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56611377-d72b-3f7c-b9c9-b7561049b1b3 | -23.30072 | -46.12535 | 2025-07-24 04:17:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2fff62a5-c07f-358a-821f-fd8088d35550 | -13.74694 | -45.92155 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dce39c8-8dbd-351a-bf92-75500ecb195d | -10.63237 | -45.22746 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 997273ee-679b-3593-b75e-d579cda3055c | -10.65953 | -47.26266 | 2025-07-24 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6f72812-0ff9-327e-aa86-ea0590205b08 | -9.73442 | -48.02026 | 2025-07-24 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68874dd8-f58f-32c1-8e7f-38bc92faa8a3 | -20.84806 | -45.28213 | 2025-07-24 04:17:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5fed7175-f8f4-3c49-8938-8c19605347e1 | -22.92559 | -45.49078 | 2025-07-24 04:17:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8ad118c4-9cbf-3f58-9b6c-de3bb317af98 | -12.42886 | -45.37589 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71d72f20-a238-3162-b580-3a8e044dc545 | -21.56643 | -48.50864 | 2025-07-24 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75684185-8326-39cc-8541-5f8d58c81344 | -21.76807 | -52.75262 | 2025-07-24 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bb6350c-d5fe-3ff1-b488-e0f45817b28e | -11.81003 | -44.27165 | 2025-07-24 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8fa5ab7-2a9c-300a-8ba7-454415e5c8d9 | -12.25395 | -44.78288 | 2025-07-24 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbe0e88f-a898-37d6-9fc3-0b7bc96c6922 | -20.35654 | -50.19168 | 2025-07-24 04:17:00 | NOAA-21 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
