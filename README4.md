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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afd8e79a-efe6-343d-b1ba-8a470c541047 | -6.43141 | -55.79663 | 2026-07-05 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65125cde-9824-3c27-8692-c4e987a10251 | -3.21453 | -53.02824 | 2026-07-05 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cadb0683-38fb-3f6c-a96f-b1974ef40376 | -6.81189 | -44.93644 | 2026-07-05 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f0fe97f-77ee-363e-b1aa-157c6a4f67f0 | -7.9209 | -45.44195 | 2026-07-05 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9d478a1-ed57-3cab-b584-a60f84d97ac5 | -3.41889 | -41.70993 | 2026-07-05 04:25:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 134a6297-1f60-3455-b067-b0f6091c5c7e | -7.29145 | -44.52916 | 2026-07-05 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 466c979e-fbb7-3292-b7b4-b2155e1d1df8 | -6.42594 | -55.79569 | 2026-07-05 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff328141-c95c-3e6f-a96a-6ddd3324aecf | -6.5926 | -51.69979 | 2026-07-05 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8b4884b-a448-3be8-8177-d7717499a8da | -7.28271 | -44.09867 | 2026-07-05 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1524f579-a869-3737-be61-cbd1f10eab9f | -6.89939 | -43.71065 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eff445a7-e786-3bf4-977d-7d8ad668f121 | -6.15556 | -47.12094 | 2026-07-05 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6cb01307-4a37-3dca-bf16-46c8a8175f79 | -7.91757 | -45.44139 | 2026-07-05 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c89b1c-6455-3aa8-8300-8d5fec14bc11 | -2.96683 | -52.64959 | 2026-07-05 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cca82d6-4f94-32ef-ad3d-681b327aa0e9 | -5.79511 | -43.63866 | 2026-07-05 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bfc27ff-c899-35ed-b908-d59fb586709e | -7.10093 | -46.71469 | 2026-07-05 04:25:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8de92b0c-9c97-3800-b1a8-feece51c16c5 | -6.86394 | -44.99942 | 2026-07-05 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f565e681-6b1e-3c5c-820c-7b4b98ec756a | -5.86869 | -51.7364 | 2026-07-05 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72602676-1560-3e68-abfe-53028b3e6e9f | -7.1899 | -43.56093 | 2026-07-05 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48e756d4-14e0-36eb-8071-3146aa441b02 | -7.40611 | -46.83073 | 2026-07-05 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccc8e5c4-832d-3520-809d-0c072a4b528d | -6.13381 | -47.61971 | 2026-07-05 04:25:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53a701e9-2a60-3fed-bc4b-440b413e74bc | -6.80464 | -43.52246 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16382485-4cdc-3f8b-a002-2b21bf1df9b6 | -7.21844 | -43.78074 | 2026-07-05 04:25:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f468edbb-2aa2-3dae-a5f7-0afac0b4f7a1 | -5.98487 | -45.09569 | 2026-07-05 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8bd02c8-5f5f-3f39-8c0b-642783801703 | -3.21538 | -53.02314 | 2026-07-05 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 618295ae-82a6-3f87-a002-f12703d8a8bb | -3.42194 | -41.71494 | 2026-07-05 04:25:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3fdf01d7-1e44-32e3-9f48-10c77e7521c4 | -7.19049 | -43.55689 | 2026-07-05 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1127623c-0aa5-3586-ab6b-2119009aa6e8 | -3.26305 | -51.09798 | 2026-07-05 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d8c1b2-d574-3c48-b337-018de00fa76c | -3.42263 | -41.71048 | 2026-07-05 04:25:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3277156c-0e9a-3afc-b331-8cd4ca5dc0bf | -6.90289 | -43.7112 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c83cb78f-c20f-3088-83b8-590ff06a3129 | -7.91585 | -45.43029 | 2026-07-05 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4104d6ab-68b1-32b5-a79d-9ae7a85581c8 | -6.89471 | -43.71795 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcf29b00-cd64-30b8-93b5-e0cb7a24e9a0 | -6.8953 | -43.71402 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| df607911-a319-39a0-b376-1b0fc7eccf95 | -6.45671 | -47.02509 | 2026-07-05 04:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b9a9695-4df9-3b7a-aca6-60da247a1dc5 | -4.50118 | -50.92603 | 2026-07-05 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7701f20-1e2a-3e46-b8cb-a5fbccda27aa | -6.10463 | -49.34345 | 2026-07-05 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3688ef9e-8c60-3ab7-8fb8-fd75d2545058 | -7.40665 | -46.82727 | 2026-07-05 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7aecdc1-43ee-36ab-a869-14475829e129 | -7.91918 | -45.43085 | 2026-07-05 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55ae8d6e-4524-322b-9b5e-12c1295924ec | -5.86805 | -51.74025 | 2026-07-05 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 612a4ed5-ffb8-336d-b446-fa49cee2d3ba | -6.92295 | -42.85146 | 2026-07-05 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac3efaae-0ac5-3d09-8db3-38f9ea6ad7c8 | -3.81804 | -50.63363 | 2026-07-05 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf80714-1d40-37dc-94de-266b26723719 | -5.79917 | -43.63534 | 2026-07-05 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bf81646-58d0-37d8-bbcf-9484d2e7f463 | -7.98025 | -45.87502 | 2026-07-05 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1aa64fee-5bb7-31cc-b0b2-1de5a3220a6f | -3.26243 | -51.10181 | 2026-07-05 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 194fb4b4-6642-3b3e-b413-b77477351820 | -1.69695 | -53.67766 | 2026-07-05 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac9ef46-ed7b-31cb-97ba-0769dd446f93 | -4.40616 | -47.50123 | 2026-07-05 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11b39d55-6115-31bc-8b37-304c420926a2 | -6.93501 | -43.71206 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9691bfa8-4f3b-330b-a575-0def5854f5d1 | -7.28328 | -44.09489 | 2026-07-05 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2d51c62-ff6b-3a08-adbf-9d4781d63f3a | -5.75356 | -43.26394 | 2026-07-05 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea9e7ba4-69f3-35ce-8c56-319a3ab6bb42 | -6.93732 | -43.72045 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d99df00f-ea28-327a-96c2-848aab8d9739 | -7.19028 | -43.55748 | 2026-07-05 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3ab9385-5cc0-3674-ac17-bb1a28cc0a74 | -6.93792 | -43.71652 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4429fa1a-3fe7-3e67-9386-2d3a06495754 | -7.24681 | -47.10765 | 2026-07-05 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ed70043-500c-33b7-b4d0-d1985f7d5a2c | -6.9023 | -43.71512 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93ccc5a4-b4ac-3ce4-93b7-27e8b1a26cb7 | -11.66403 | -46.7502 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46f86353-4e36-3bbf-b277-f4de58fda646 | -11.43468 | -46.58382 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eaafdb8-2edf-3feb-8732-d95c41843e1e | -11.43746 | -46.58786 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 015fa93f-0232-3fea-a9b7-159b6c42e6fa | -11.43915 | -46.59894 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a21510dd-63e4-3148-bd4c-a51af5944f86 | -11.54677 | -48.26123 | 2026-07-05 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62253564-351e-34ea-974b-af4f020f2377 | -10.89965 | -56.85 | 2026-07-05 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 900029d8-af01-3416-82dd-e3beec686ab7 | -13.23962 | -54.32663 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ca412934-3070-3b0e-8279-780fe0609c6c | -11.52557 | -46.47858 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a694a87-7b77-3f58-9549-ed4d7413042a | -13.24042 | -54.3222 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a47347c6-449c-3064-9141-dd44a210c4ba | -11.32113 | -54.47514 | 2026-07-05 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a0ffc0e-2d3d-3195-bb73-90957458e958 | -11.49266 | -47.37229 | 2026-07-05 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1199cc03-ae64-30ff-94ea-3d26d1709120 | -10.94144 | -43.03977 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 71f3e1e4-9ccf-304c-838d-ea722822cb09 | -10.94008 | -43.04922 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 67301fe3-2835-322c-a60c-c1bc0a1f5a7b | -11.84376 | -49.19219 | 2026-07-05 04:27:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97299f2c-a766-358f-92cc-432f747f5af1 | -10.93316 | -43.04339 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e734d556-434f-3bd5-b6c3-c275ec600671 | -13.23602 | -54.32141 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 689a1d1c-e445-3f58-b14a-175a734ae38d | -13.22559 | -54.32869 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15bf7fcd-70b4-3b22-91e7-b6846e9b951d | -8.90121 | -47.77326 | 2026-07-05 04:27:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9f70e89-9116-3dd2-91c4-c400073b5810 | -12.14086 | -44.75668 | 2026-07-05 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5804c34-71f0-39c7-a9c3-02bdeb4c3939 | -12.1706 | -54.53784 | 2026-07-05 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6881697-7ed8-365b-bb54-55c0c1e7c24a | -13.44502 | -43.85175 | 2026-07-05 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd732e24-7430-3a14-be9a-4183f1b08d24 | -13.24483 | -54.32298 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 494b0bf0-c133-3053-867a-476f45f4bc44 | -11.92495 | -43.38424 | 2026-07-05 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 588bd546-163e-33bd-b298-d0e2541947a5 | -10.8334 | -48.76527 | 2026-07-05 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eea83c9-99ac-3329-a182-148b4656c269 | -10.97169 | -48.13066 | 2026-07-05 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93979b8e-83df-3265-b482-9740b8212470 | -13.4435 | -43.85348 | 2026-07-05 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 651844b8-a157-37ca-8102-7e1c20658cec | -8.05623 | -46.70034 | 2026-07-05 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41f9b1e5-f1ec-39ea-bb02-746ff83bd561 | -8.94685 | -44.21173 | 2026-07-05 04:27:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf238b5a-257d-35a7-af4a-8ce677c06cd5 | -10.97226 | -48.12712 | 2026-07-05 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e21b4b16-4afe-3655-89ec-4049ed671a8d | -11.43136 | -46.5833 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aadb78c5-497e-3c8a-9d1d-ef2aefeca9ed | -8.89844 | -47.7692 | 2026-07-05 04:27:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa9a95a5-8e88-383e-b6aa-4628a5b444df | -11.52503 | -46.48211 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff39b6d6-da22-3834-a33d-17eecd31b7c1 | -11.43083 | -46.58682 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bf2a755-4123-32e4-802c-3ade683ac141 | -10.12502 | -52.08758 | 2026-07-05 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89550bb4-9ed8-3bbe-8701-42d01f8aeaa4 | -10.93248 | -43.0481 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6326f516-5ac9-3886-ae81-9c83f20b47e1 | -9.83505 | -45.32953 | 2026-07-05 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edc383d6-1494-3ecb-9282-79fa4ee85341 | -8.32512 | -45.38066 | 2026-07-05 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c57fc262-f718-36dc-953d-aa620d212883 | -11.92118 | -43.3837 | 2026-07-05 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7beea3fa-14a6-3882-a020-b9ff329ff558 | -13.19879 | -54.30119 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88483a56-b9d7-3ba8-940f-3a1e3e03cfca | -10.65417 | -49.72079 | 2026-07-05 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feed92db-64ea-39ad-a795-5ab06208bd0a | -8.45351 | -48.29426 | 2026-07-05 04:27:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6599b331-02b2-3299-89ff-e2160d7ba627 | -11.9174 | -43.38319 | 2026-07-05 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c51d15ae-93f5-346f-a428-a37d35fd5a0c | -11.45666 | -46.55111 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e10ede2-f2df-3b57-bcc7-8741344f3139 | -11.5462 | -48.26479 | 2026-07-05 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8d4460-5f9c-3ffd-a056-0f6d58abd113 | -10.93696 | -43.04395 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 329a382d-1ec0-3b51-bcb3-5a59ba2f4446 | -10.07532 | -48.30718 | 2026-07-05 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd982d86-492d-3db8-b411-7641cfecd0c2 | -8.11253 | -47.12125 | 2026-07-05 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
