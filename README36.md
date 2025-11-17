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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a7b954a-3d60-3d60-9af2-724200541ba6 | -10.9253 | -48.68392 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b7aa1f1-37af-3194-9818-5ab7919d9a1a | -14.65133 | -46.54184 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1493b6e-d2ab-30c0-938a-637260081a0a | -8.67627 | -46.63044 | 2025-11-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94c96338-1815-3687-a9f3-2b6b58c22fa8 | -9.75056 | -43.96793 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e79a91f-2581-30b0-9f95-d270a22276ea | -14.8899 | -47.37279 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb9e81e8-872f-3024-9101-e9d5a288fe76 | -9.72779 | -43.97324 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 04698132-9a4f-3c36-8dbf-ed894aeef8a9 | -10.27468 | -44.79694 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebc8a33b-397c-39c3-bc9e-2cc49ef16990 | -13.5959 | -48.02269 | 2025-11-17 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58ab9bed-93be-31c0-aa08-116ee2a9f651 | -9.57639 | -46.63467 | 2025-11-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f3e2032-dcc9-393e-9d04-ba84c60c0313 | -8.73538 | -48.32446 | 2025-11-17 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 863f2b8c-f3b3-353f-851c-9f520dab0519 | -9.80553 | -48.55842 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 239c4db0-bf57-3257-bb9c-606c681560fc | -10.13282 | -49.15457 | 2025-11-17 04:40:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac29f20f-a49d-390e-8398-e98036aae330 | -9.1515 | -48.0597 | 2025-11-17 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72be3887-5adb-3e5e-8542-700a7d13a0dc | -9.35813 | -50.74225 | 2025-11-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07b0dadf-2b6d-33bb-9335-f371c70476cf | -14.66014 | -46.59515 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bcb8964-68fa-3eb2-bcd0-8399601aba9f | -11.84427 | -49.21044 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed09e38b-d4dd-3d5d-b566-9a2802da3c6d | -8.5084 | -49.41724 | 2025-11-17 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e66e236d-cdfd-32b4-b261-24c94984f402 | -9.34972 | -46.60038 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00312a17-d27d-3071-a9d8-cd5cacd99998 | -10.27828 | -44.80134 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e714000-b3f4-303d-a36e-f7c23e06483d | -11.61881 | -48.57042 | 2025-11-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7879608a-fe94-30d6-9a94-a3ec9be52619 | -10.39067 | -44.9195 | 2025-11-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1129b076-753d-3760-b228-72cfd815d303 | -13.10353 | -40.03115 | 2025-11-17 04:40:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 77874e1c-cf61-3397-9672-f8188dcd04f6 | -10.95018 | -48.70291 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40e73be2-a08c-31ba-8c62-e28d32ddd3b2 | -10.53601 | -47.91022 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5679bb39-95e2-3923-9c29-bec23423b806 | -11.80754 | -45.30511 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8cd11277-e2fa-36a8-a260-cb8c074a1297 | -12.87128 | -46.04368 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d601ba86-9671-3731-a298-e95776e914ab | -9.4282 | -44.64106 | 2025-11-17 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dbd9332-aa7f-385d-9149-283ab341b6b0 | -10.6232 | -48.08009 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73c14fe3-9049-30d3-989a-ade81d46b88a | -12.02923 | -47.01252 | 2025-11-17 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7bef6d8-13ca-318a-aebd-eb4895d95c36 | -12.85841 | -46.02079 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15d22864-553b-33c0-9dab-d16d0318f30a | -10.09982 | -44.77315 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb1843b9-77a2-3002-85b8-8f6f5af753ca | -11.82045 | -47.58103 | 2025-11-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 545f7e4a-7c72-36a1-aae6-7cfc58b4e38d | -12.00733 | -52.46132 | 2025-11-17 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfbebe5f-c467-3287-9881-1e1fbdf17a7c | -12.00016 | -49.27561 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff3a4bb8-4f0a-376a-aa2c-736aa9a90291 | -10.9833 | -45.13799 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5cccb4e-3dcf-3388-a75f-e5853e061fcb | -12.86084 | -46.0275 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de31bd81-a6a7-3e78-93e4-30f87432bc49 | -11.81627 | -47.58472 | 2025-11-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00791940-b739-350d-b25f-b7a0f5c2fb05 | -8.88454 | -44.78181 | 2025-11-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4f559a31-8fc7-3040-8b5c-244f164e1597 | -10.85849 | -44.87482 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e8a3199-c3b3-38b0-9ae6-b6e13756c6a6 | -12.98708 | -49.79955 | 2025-11-17 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f80b865d-68d1-3e94-a65c-838c4ea169de | -12.00633 | -49.28031 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56513fe6-5ea8-3ddd-81e4-48331054fc4b | -11.40837 | -43.33515 | 2025-11-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b164a407-7820-395f-82d4-de50134f07d0 | -11.96027 | -44.9413 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3187b05-dd6a-3e39-b7a2-3d1b016d95a8 | -11.81723 | -45.29494 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b80d1cbb-b3d2-37ac-8da9-bfe93281974f | -12.40516 | -47.5899 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6ccbd8d-2d2c-3300-b453-4381edbf1f66 | -9.33457 | -46.5761 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 77c6b15c-d687-3988-a5c5-d789c7d028a7 | -12.65277 | -48.82529 | 2025-11-17 04:40:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 196f54fd-c7f6-3c4a-82b6-add7686207de | -12.8577 | -46.02582 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0986e671-1a1b-3d6e-aacb-923b94d5c075 | -8.82924 | -47.3599 | 2025-11-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4f3de8a-3538-355e-90f8-7d77d8a5235c | -11.84317 | -49.2177 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fbf57180-4949-3d82-9c21-51ea44635b53 | -12.40894 | -47.53887 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8dc1f78-05a1-3f0e-a9d7-fe25c3aa1e49 | -12.16104 | -47.4226 | 2025-11-17 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fea47903-37ad-3277-acd3-b202a0c648a3 | -11.70683 | -44.44855 | 2025-11-17 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3786508c-b710-39da-8239-538907931bcc | -9.51876 | -47.47101 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ad30b48-8654-3bd8-b525-61a9596e405f | -9.71705 | -43.95492 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4633feae-d9e4-305d-bb69-cc46b3093f72 | -11.82403 | -47.58157 | 2025-11-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c449226a-f7b2-3a14-b1c6-98856667b103 | -12.69489 | -46.7927 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13c8b902-2dab-365b-a0b3-55e5cdcdde56 | -9.74567 | -43.97146 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a70971d0-d8cd-3120-94f2-06fb48f851cc | -11.84372 | -49.21407 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 42b1b310-1a62-3ca3-a254-6018fdeb5c40 | -11.80706 | -45.30861 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| da155b8d-db72-3324-81a5-93380b7ce531 | -10.55739 | -44.81963 | 2025-11-17 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9eb7aafa-e38f-326b-835b-4c4dadd5e9c0 | -9.63584 | -47.8926 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea0c07c1-b523-366d-9756-31b63ef5d342 | -12.20389 | -49.63572 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7aa22a54-06b7-3bbc-b0d1-886226865ce4 | -10.9581 | -48.69648 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5e96fae-bece-3a13-a761-7d7f90768aa2 | -10.80244 | -47.98513 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a179376d-e5a9-3d5b-8a1b-4ea936a64896 | -12.3849 | -48.12433 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ece4f8e-8b65-3fcb-9fed-e5cfcb56394e | -14.64154 | -46.55533 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87b90905-a6b8-3e26-8d1c-dc48b197533f | -9.74739 | -43.95894 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41006db5-2a87-398e-9efb-a3884b3e966b | -12.90832 | -45.10759 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59c50e0f-3a64-3bf4-80a2-67febff86c04 | -12.90361 | -45.1109 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e375e359-b379-3332-b0e1-3b7a0122061f | -12.4483 | -51.40269 | 2025-11-17 04:40:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc20fc2-aee7-3b5e-9fcc-61ae51d7348a | -9.57738 | -49.10057 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4acfc5a8-f57e-3184-a4d5-7a7c7877431f | -10.95413 | -48.69975 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15420167-b95f-36ea-9fde-20116ef4211a | -13.09756 | -40.03099 | 2025-11-17 04:40:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 779f8199-3f24-3872-9d0f-3c60d86ae746 | -10.8998 | -49.13787 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25b20c00-cb2a-3a92-acdb-ca8afb1ae145 | -10.66433 | -49.36889 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| aeef7ad1-8cab-3d82-8de9-8049a0474116 | -11.13667 | -44.93161 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b18c7b5-9e79-3a48-a014-29c2da5016b9 | -10.18532 | -44.50714 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb208376-32b9-3f40-8107-7408fa63d3ca | -9.73894 | -47.22874 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4431da2b-486a-3efb-9394-986e177cb7ac | -12.85447 | -46.02009 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cad3baa5-f2b0-39f5-aa61-ef61ba2f1a0f | -11.15862 | -49.44983 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9a42643-395c-31cb-8695-f2cb4f80327f | -10.95361 | -48.68039 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 3afcba5e-82a7-35bd-8184-00eecbc97199 | -15.86901 | -45.66459 | 2025-11-17 04:40:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e8a23b0-905e-35f0-a3e9-27207ec13340 | -11.67417 | -44.72578 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 545db644-6f27-382b-b98c-fdb3d522c610 | -11.6784 | -44.72639 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 251d157c-e1d0-3e46-b188-450b903d8934 | -12.40578 | -47.58571 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edd91b85-8ed8-3537-bd25-29002fb30f8b | -11.05685 | -45.14745 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9b14053-5e8c-34d5-b7f2-ddd40948d066 | -12.87386 | -46.05043 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6384b33-33c5-30b6-86f9-fe1754e03ace | -9.32378 | -46.57148 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5b176ad8-181c-358a-bbea-6079a48165df | -9.35337 | -46.60097 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b6dee81-4be7-33e3-a2ae-cb10d9a802fc | -9.7116 | -43.96265 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 902e5da4-52e8-3f55-b597-e5b56d2b8fc6 | -10.53543 | -47.91415 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45ede500-5381-3bda-93b5-f754bca27bfc | -12.87523 | -46.47278 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75282dc2-da0c-3d4f-a063-07623af19463 | -10.51197 | -48.00997 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a77f26c9-3cf9-3e9a-ae96-28fbf6f0b69a | -13.32193 | -47.37453 | 2025-11-17 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd5d708c-0168-3080-95e3-f5423f33f164 | -10.65671 | -48.16349 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ec9213e-2508-3e65-a139-d646f11eb297 | -11.11856 | -48.21593 | 2025-11-17 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a30a1186-e71e-30ab-b08d-1c4e70bc826b | -10.18425 | -44.51501 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ea00455-4375-394e-836a-2bc0b413e949 | -11.40499 | -43.32472 | 2025-11-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6f6eb32c-1a95-31c5-9fbb-73d594dc36f6 | -9.7246 | -43.96429 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README37.md)
