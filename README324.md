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

## Dados Diários - Página 324

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b0fcbb9-1567-3266-9a8a-7af68bacbfe3 | -7.25062 | -39.40555 | 2026-10-08 16:37:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 389bb56c-d7b9-3c1e-95fb-b9c1bac9da63 | -14.36181 | -55.02333 | 2026-10-08 16:37:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05c81423-2432-3957-a684-61798a01d123 | -12.19512 | -44.82703 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| ec0d18bf-3402-35cd-abba-dd5dd902d86c | -10.0752 | -45.99624 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 9c810f25-e3bd-3547-994d-e32e790d2a20 | -12.19751 | -48.41825 | 2026-10-08 16:37:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 630beb9e-22a4-3708-908a-ad8cdf8ed81a | -10.36019 | -42.48471 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 0edf0e8a-9320-3780-a6f5-32e3fbaedcb1 | -8.89072 | -45.38521 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 93f5721d-1005-3122-8e34-ea71a9572ebe | -10.76278 | -46.60286 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 592b8d4e-fd22-3b9b-be3d-0db71769a198 | -9.14064 | -45.82413 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 557143d8-5f9d-3c7f-a705-3a5b391fea2d | -6.40784 | -44.95156 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5ceea2ae-c5a1-3579-9329-b62b1ab4d8fc | -11.08473 | -44.00794 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e2d94f79-a4de-319f-a0db-c34472d69f8f | -7.48392 | -42.79313 | 2026-10-08 16:37:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 63145449-a217-3e9e-9874-50af908b2a8f | -7.70618 | -44.74635 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8ca3a11c-25c6-3188-a576-51ab239a0aaa | -7.79251 | -44.58065 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 25e9ce68-6680-3350-80a0-577fb069066d | -10.31434 | -48.00264 | 2026-10-08 16:37:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 305f0e76-e77a-3b39-aca1-2428917bbea6 | -7.53817 | -42.09826 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 72e631f7-5d7f-3509-afcf-9da3f1d27ff6 | -8.73912 | -37.33715 | 2026-10-08 16:37:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 5785236e-3803-3b6d-8a33-85766baf56b6 | -12.31149 | -47.06133 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 512223c1-7be7-3758-b3b0-20993ee9a4e0 | -7.40282 | -44.44983 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 822556a8-4923-3749-905a-03bb29023de4 | -12.19128 | -44.82403 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d5c23b96-6e36-330e-9274-3adb594e6735 | -8.28745 | -45.72367 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 5b48f249-96e3-3852-a8c6-e10fbf01f335 | -11.8245 | -44.68858 | 2026-10-08 16:37:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ce33ff0-cf25-3530-b964-4ba79ca7e095 | -7.18616 | -46.51538 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4996bad7-66ee-3c89-a60e-5a657d20c629 | -10.86594 | -45.54865 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 04d2d73b-86c0-3ad6-837f-9b997972f41e | -8.89787 | -45.38766 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 03079452-cc2d-374b-bc7b-53f42fd1cefa | -7.53746 | -42.09388 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 9b019d21-f1ea-340e-8875-0b170d301990 | -12.24621 | -44.73976 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| df69b1c8-6f2c-3c55-9638-3d516546f620 | -10.17648 | -48.05095 | 2026-10-08 16:37:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9771132c-2fb1-3eb8-abe2-bc083a666468 | -6.33406 | -44.87244 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc9a46ad-af86-3611-82c2-888764b158d0 | -18.13175 | -42.78405 | 2026-10-08 16:37:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 77300b9b-0b10-372b-8e46-db0dda565f28 | -11.75936 | -47.74276 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 050e5dff-777d-3671-9b75-6d3079928090 | -6.21612 | -45.18406 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9270fb2-60d0-334e-be74-54e7f86f289f | -9.53121 | -45.62574 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bf4da9f1-04a4-34d7-8da5-fe16cb2a15ea | -7.63626 | -44.38649 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d2a6f29-79ae-30e0-8dcf-b5f838b1cb32 | -6.6748 | -45.36418 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0eb884c1-f256-35c2-bcd7-90525558820a | -7.04999 | -45.44204 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 730d6d7e-dfbc-312d-a2c7-cfb26c23261a | -10.7466 | -48.54819 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ba0f8159-6fc2-38a3-97ef-4742737bc6f1 | -11.58258 | -43.67342 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2d4fee0e-25f1-3a08-8829-60e9051140d0 | -12.98664 | -47.06481 | 2026-10-08 16:37:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 83f02e1f-7d23-3454-847f-c4248ce49189 | -6.55221 | -45.36208 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 40b34f26-e38e-3cb4-83b4-b0f4ba415b86 | -6.95134 | -43.73321 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 51a88494-a30a-3ff0-b90d-e201bdff1525 | -5.75804 | -42.07273 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 78edb75e-1f6e-3d53-9a24-3c5bb6da4c29 | -8.353 | -47.64561 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3c66e554-cbed-31e8-94fe-5cacb4ce92d7 | -9.13388 | -45.84667 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 62347e1d-76b7-391c-8178-f7b25bdb511a | -7.0962 | -44.03121 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7c159d14-a476-30ed-ab13-4f13bfc9312a | -12.22904 | -44.76047 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| df809d5e-bb60-38e0-8f14-cc45f6f08acb | -14.00769 | -48.75387 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 1c50a8a0-4152-30c7-84e7-3de5b4d01ebf | -8.3694 | -36.81894 | 2026-10-08 16:37:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0343d92-cfd9-37a1-9800-4a1556c9b58a | -8.59117 | -39.54992 | 2026-10-08 16:37:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 408966b2-0ec3-3bc5-8ebb-29e0924aa46a | -7.59987 | -42.38802 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| f6092e1b-f64a-3afb-99eb-d142703032b5 | -5.72509 | -41.77495 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 01dd1854-c075-3112-8672-ac3e9e1a160d | -8.62188 | -48.35331 | 2026-10-08 16:37:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 28e107ad-945f-34a3-a147-4c36aef1bfb9 | -8.3969 | -46.92368 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57469320-5530-3a21-a50b-662ad2b3b738 | -8.31157 | -50.37643 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfa2bc05-8c90-3933-834d-3eb34facc2d0 | -8.30558 | -45.73157 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 900761b2-fa76-3013-9bb2-2895975e5180 | -10.67946 | -47.83458 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fb7727a8-e02b-3f8b-b876-89ef53a23582 | -7.12321 | -43.91327 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b324647d-e571-37b9-8007-bbcb49a8d52a | -6.03503 | -42.71803 | 2026-10-08 16:37:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 168967aa-6909-3f9a-b581-c25470a1299b | -6.67373 | -45.35722 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5333a5a1-9107-3eb1-8598-4e224498eb01 | -8.19556 | -45.7882 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 14f74d0e-226b-309a-87e5-fad73f4ea483 | -6.45648 | -46.02316 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bfb45901-fb4b-3f59-a6be-5162c2369424 | -18.14297 | -41.62836 | 2026-10-08 16:37:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 851941a4-9145-33bf-b7a7-6372dfaa7b94 | -7.11507 | -40.68832 | 2026-10-08 16:37:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 5003b120-ae84-3e7d-bffd-45e6f6bf19d0 | -8.78689 | -47.26603 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 36c37b44-e63a-30cb-80fd-a0ad587b7074 | -9.83399 | -45.76698 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 908ab89a-8fc8-3abf-a6c7-3a9b58d728a4 | -7.84325 | -45.50346 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6a278150-24e3-30b4-a177-3a69e1c21bf7 | -10.47804 | -47.8636 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| dc7e1bfc-6dcd-3959-b38e-81f6a03707ff | -7.87977 | -54.98449 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9962634c-86a7-3b2b-a5ad-93a2d4c964e6 | -9.85286 | -47.85764 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 02e66c9e-2385-311e-a459-9b6e484a693f | -7.14621 | -45.00926 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1c3c0ad4-df1e-3fbf-923f-c0c77711c180 | -11.09028 | -43.99978 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| be456b45-3f28-346d-ada8-b1cd466c0449 | -11.97159 | -57.58579 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 336fa44f-691e-364f-b4f3-7312e83cc524 | -6.79405 | -45.05893 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a8a7ca56-d47a-3a4c-86ad-f572d32c52c8 | -12.21022 | -57.10149 | 2026-10-08 16:37:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 62413bf3-629b-3b99-9864-3c90077aa63c | -11.77357 | -45.58615 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f4d6e51f-f45e-3e37-ac25-52c9847f0482 | -9.14439 | -49.92463 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 657ca8f6-78b1-3db2-8476-b267cb18dc32 | -6.42889 | -44.8282 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a38cf5b3-4f5e-398f-8964-5d12816c7c76 | -9.40663 | -46.44369 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9135d60e-d7b3-3c96-8f40-61414c70c9e7 | -9.88663 | -44.86386 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 2cc603e1-657c-3706-aeaa-e305d1aafbc2 | -9.94167 | -43.56032 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| b9296db4-af5e-32e7-b0ca-47057eb9263e | -10.47752 | -47.23375 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b397e87f-8806-3715-91bd-877b8f0b8fe2 | -11.78339 | -46.78963 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b9b06391-156f-3cc3-9fde-decf50de30be | -7.39889 | -44.46882 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5758e4ef-f6bb-3c8e-ae66-4ab6414fad78 | -5.74891 | -41.67747 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 60b3f7f1-857f-33be-81e5-59c6a57a27b0 | -12.31093 | -47.05738 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 573a51b4-f76f-3c8e-bf38-ddf1961b2ed0 | -8.84401 | -45.45717 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1c0c7679-fbe7-3a1b-a443-db8303a01042 | -11.62496 | -43.70351 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 7b7f2fac-36eb-3366-88ca-dfaadd545707 | -9.53015 | -45.61874 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 99148762-5159-3197-885c-70b3b835cc89 | -11.7841 | -45.5882 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e4062812-96e2-3f60-89d0-2553775e1950 | -4.90764 | -37.29585 | 2026-10-08 16:37:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cb01e84b-f6d6-33e3-8c51-8b053d1b2024 | -11.58705 | -43.68009 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 1df8cd51-b694-360a-9f14-b407c615e152 | -11.39162 | -47.56775 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ecc55e9d-9ed8-31a4-a66a-c0ef4c5441a1 | -9.74225 | -42.24566 | 2026-10-08 16:37:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 534202fa-5f91-3615-bdd1-8b23758e1571 | -8.95513 | -45.13995 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1c114590-66b8-35cc-942d-5f6939db1253 | -6.45979 | -46.02266 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f8743db2-e119-3f4f-b03d-8396f434ca8f | -8.17728 | -54.72507 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a5e0d23d-7db2-3a68-870e-d7d09bab4d50 | -6.15004 | -39.43409 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 47a7b5bc-e465-328c-b8f1-50216688fa60 | -5.11876 | -36.86696 | 2026-10-08 16:37:00 | NOAA-20 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 158081a8-f0fc-3d4a-8900-18c09f326e72 | -8.30572 | -45.71021 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7f0e74a-b1d4-3eca-baae-b2da9066583b | -6.40395 | -44.94853 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |


[Clique aqui para ver as próximas entradas](README325.md)
