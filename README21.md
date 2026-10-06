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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29d1bbf2-3474-37d6-a85b-268bfc051f69 | -7.37764 | -46.22543 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9e1c32fd-cd55-3005-9314-e0faa740902a | -11.27761 | -45.50553 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| bc368140-4fe5-3554-88fe-6f2591c1f07f | -11.27456 | -45.49767 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ca20a6df-1d8b-3765-94fb-659d702d3666 | -10.49688 | -44.4176 | 2026-10-06 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac375d49-a5f9-3b49-ac6a-7f178573145a | -11.28044 | -45.51942 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1a8022ed-1491-3707-bda2-f9cdd6799c8b | -11.26842 | -45.49707 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6f1d2e0a-57e4-38f3-88ee-ff005b67ebe5 | -11.23185 | -45.26503 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c5185db-9711-39e6-b928-276fa9da63b9 | -8.70407 | -45.22249 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a1e536b-b422-3340-9b2d-0ecb233d71c4 | -12.76195 | -44.88671 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d871d413-76e5-3b0b-839c-7253d0e3660d | -10.97014 | -45.41491 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5beb434e-550e-31cd-b1f5-00e08fd05170 | -7.28601 | -47.26928 | 2026-10-06 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b46f26e0-10e6-381e-aba3-fa9a8e4a9e5c | -6.00465 | -47.39245 | 2026-10-06 03:45:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 55c72a71-469a-37ec-9ee9-36b727b4f65a | -11.28063 | -45.52214 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c30a4b3-2530-3613-99ca-a9264a69f7ec | -8.47343 | -36.5315 | 2026-10-06 03:45:00 | NOAA-21 | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fe2b7458-d2d8-3321-b787-321775d0cd13 | -7.01827 | -43.44916 | 2026-10-06 03:45:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ae7b5f2b-1805-3e38-94d3-c89b057c7352 | -12.86569 | -39.92339 | 2026-10-06 03:45:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 441ece9a-bff9-3b6e-97b3-edcaeb97cc65 | -13.87987 | -43.79569 | 2026-10-06 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fee8a2c-cdd2-3f33-85af-b40ff3a44866 | -11.76597 | -44.92942 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b09607ae-7818-3982-a171-0484ad0b003b | -14.23022 | -42.94082 | 2026-10-06 03:45:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 74b57bee-df9e-3b40-8708-4b4732275c46 | -11.53476 | -44.89488 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 46679703-070b-33db-99e6-e0cc73428787 | -7.4663 | -42.99818 | 2026-10-06 03:45:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e4cbd499-a3cd-3fc0-93b0-d1707658e2f8 | -11.28827 | -45.51038 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 4ddb8db8-14d9-37f0-bd27-22450c62187e | -6.92326 | -44.56387 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5688229-c76f-3851-ba2a-c9e87b4f113e | -11.69116 | -43.66914 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eadf9ce6-b0e5-3206-acf1-b4f709fbc29c | -11.66898 | -43.63545 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fe77eaf-f4bc-3f53-956a-042bc4c2ed88 | -11.26202 | -45.50255 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 79ee8142-eb36-3afc-b29b-c3dbf0d7806a | -7.47099 | -42.99899 | 2026-10-06 03:45:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1824474c-3ce0-3030-b489-cfd862fcbefd | -8.69467 | -45.21353 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9794dfb2-a25d-3193-ab8e-2bc3bd02f67e | -11.28337 | -45.50345 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6a1dde3b-e6af-3698-b468-35770f983966 | -8.70185 | -45.20429 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c98dd9f-8faa-376c-ab0e-919b196d1aa2 | -14.05595 | -44.29111 | 2026-10-06 03:45:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fbd56f0-1a3e-361b-a200-0c6c5175adf5 | -11.67748 | -43.66645 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80944f59-f94c-3208-b137-446039b61ce9 | -11.63647 | -43.65845 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b40495fe-3495-380c-a751-7fa96cc13b4f | -6.85682 | -41.80229 | 2026-10-06 03:45:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 661f5cc7-6420-3943-94e4-5e5416dbe165 | -10.36226 | -45.03329 | 2026-10-06 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ae965c4-d0a5-3067-b073-8962fe9611a7 | -10.54665 | -46.40297 | 2026-10-06 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6d49d308-26b3-3a6a-b96a-c255d12ca160 | -11.27394 | -45.50087 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 787e3374-64d4-3649-9310-55e834b2eb14 | -11.64106 | -43.65913 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abacc6bc-5ee3-3051-8a3e-43fe3dcf7eed | -13.87992 | -43.80119 | 2026-10-06 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0741802b-000c-365a-a1ac-8d7211a9e522 | -11.28162 | -45.51298 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 5f711daa-1262-38d0-ab96-b81273eef22e | -11.29795 | -45.51609 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c0fddbbb-ec1b-3145-b39d-28ccec08580b | -8.70123 | -45.20771 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f40f0e9c-e9aa-3c9a-a68a-541b2b47ab9b | -11.26142 | -45.50581 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a291a487-496f-36de-999a-90d183f71dd0 | -6.66887 | -43.8223 | 2026-10-06 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 628d2a56-47bc-3953-8d0f-018c62dbeec9 | -9.80169 | -44.78981 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 702f5ca0-e783-3cbb-bb15-b815ef10c189 | -8.58516 | -45.65949 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b64354a-3651-3ff0-98d0-87016d2b24cd | -11.694 | -43.67952 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1bc4d1f1-ca26-3652-915d-1e889c847fb5 | -11.29164 | -45.52093 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 76259cb4-55a1-3ab5-99b3-3c680967bf51 | -9.86066 | -44.81251 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebc967df-3ea5-302e-ab63-14d48ba24804 | -11.68447 | -43.62794 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58ad6bb2-9f6b-393e-b71d-6611b263ce21 | -11.63903 | -43.64457 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e15b68e-c0d7-3b2a-b4b1-2e5ddefda745 | -8.58586 | -45.65566 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcc5bd05-f990-3879-ab7a-097e682b88c2 | -11.2874 | -45.51081 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 85a32d0b-6bb9-3a62-9b77-77a9180f2354 | -8.70532 | -45.21558 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c14b15d-eb64-3a89-90ff-4cc3ede97ad2 | -6.88841 | -43.68661 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b26f3b5-3961-3352-b84c-481994edb8de | -11.67356 | -43.63618 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fb8acf0-71cd-34a9-8678-8036e892a2b8 | -11.76652 | -44.92651 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab0ceef-05fb-3e0c-9a9a-3e3a4361f8aa | -11.2782 | -45.50232 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| d3ca06bb-ac28-351b-8fa4-3ffe8e337063 | -7.4818 | -42.79735 | 2026-10-06 03:45:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4398fafa-d6ed-3318-9635-e532a72dad48 | -11.82408 | -43.53551 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b12368f-8439-315f-8bd9-fb97d79a5d4d | -11.28886 | -45.50733 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 60ce862f-aadc-33b0-806a-23a9202763fe | -7.29038 | -47.27006 | 2026-10-06 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57d016b0-b976-3221-8fd0-b462364e6e5c | -6.88442 | -43.68015 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5428e2f1-9b4e-32df-8a3b-b889c387da10 | -8.69876 | -45.22139 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55283053-a3aa-3242-a61b-59c58c3dc0d2 | -13.49381 | -44.35978 | 2026-10-06 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e14b2d0-4090-3ff1-b827-cb7f611328c0 | -7.37839 | -46.22124 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a11a8807-1865-3e37-9c73-c5f6ed168650 | -11.26722 | -45.50353 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f0867211-4f9e-3092-b304-80c402c6053e | -7.48391 | -42.81273 | 2026-10-06 03:45:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f45aabc-4ef9-30b6-96a7-3d011eae7833 | -11.29396 | -45.50879 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 61f9e28b-98b6-374f-9f1c-0f31b1d5b813 | -6.67339 | -43.82612 | 2026-10-06 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7e7f6e46-8859-344a-b38c-3dfd917734ad | -11.27604 | -45.51796 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| dc747955-2f3f-3c00-ba0d-966fc67126e1 | -10.35315 | -45.02522 | 2026-10-06 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60088c57-a662-37e8-8f4d-da52dadcca8c | -13.00027 | -40.14487 | 2026-10-06 03:45:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cd06d95-3d5e-3884-9265-5cf4a2f7de6e | -11.28221 | -45.50977 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 981f9fa0-97e0-3152-878e-8b474360429a | -10.96961 | -45.41243 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74380b5d-96d0-3e9c-867b-f43d7eb6b85d | -7.82543 | -45.30018 | 2026-10-06 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fb47caf-f651-3514-8ce1-8ee79eda7325 | -6.92564 | -43.6785 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 806c92de-4975-3abd-ab43-df518d6b1a21 | -6.89986 | -43.67965 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3109bace-7780-3a70-ba86-6e7980bbdc01 | -11.67293 | -43.66555 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4bd3c9e0-4058-3f57-bcf4-b2ae0ac168da | -10.97471 | -45.41918 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f79a2b9-1d10-31ad-b6b6-07aecf901f09 | -6.00368 | -47.39777 | 2026-10-06 03:45:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 39d5a4a7-f6f1-334d-82f3-6723297683a9 | -8.70061 | -45.21112 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bf38617-ddfe-3035-9f0d-dfb112297bde | -11.6866 | -43.66825 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be41fca4-f725-3206-a500-fbcc2bd78771 | -7.01924 | -43.44365 | 2026-10-06 03:45:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bc3dd183-4cae-3154-880d-f5ab96cc0c12 | -9.88363 | -44.80178 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76e05e91-a33d-36f6-9d48-f3dd54fdef28 | -8.7 | -45.21453 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 571ab05d-31aa-313f-ad18-97fe24372d3f | -11.28645 | -45.51991 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d8451d5-7c19-3e50-acbb-ebeb41b0ce3c | -7.47929 | -42.81183 | 2026-10-06 03:45:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5e4af58e-d2a8-35c1-bf60-735948379416 | -6.92515 | -43.68133 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35dca7a0-1b89-30bf-a0a9-650a83e76aae | -11.69201 | -43.66439 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1e97172-ca08-365c-8123-d91c07e864f5 | -6.89936 | -43.68254 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67c90b95-cade-3fc7-8892-0a82dc926602 | -13.02897 | -43.1208 | 2026-10-06 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4fbcc342-7579-303f-a0c1-7c1ed51c3055 | -8.87106 | -45.37206 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb02c82b-419c-37f3-a7a6-027235f3f4f2 | -11.71995 | -43.64003 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8a61cb14-dd03-3199-9424-28a25acd908c | -11.2828 | -45.50659 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6a90243f-1f17-334c-ac18-741441ea0043 | -8.70593 | -45.21219 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13883ac1-557e-37cf-ba45-ebab3de6142e | -7.76428 | -44.58307 | 2026-10-06 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5618b0e-5658-344b-8353-7d3fc5b105b8 | -12.86498 | -39.92758 | 2026-10-06 03:45:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b512ce62-d57a-369f-b850-ca74ee68ecdb | -10.50181 | -44.41836 | 2026-10-06 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4dc82d59-6bf2-3269-8d3d-98f526ef785e | -9.82211 | -44.79317 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
