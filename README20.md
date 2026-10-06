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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98d4e73f-ee49-3e70-a06c-29c87e9a8826 | -4.35789 | -47.77571 | 2026-10-06 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b8899ce1-273c-30e3-8dba-0ae75738ebb5 | -5.83081 | -45.01472 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 52f601d6-23a7-3e65-8079-c4d376b66eef | -5.46934 | -41.22823 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a5a9a29-e82f-350b-9247-868c2e69ab35 | -5.96779 | -41.3614 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31672328-6525-3d52-8948-cbc8176a79e3 | -3.39799 | -44.48268 | 2026-10-06 03:42:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca38eb01-f7bf-32db-a4e8-755a69b1be80 | -3.93655 | -42.98941 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b95c416-3a4f-3c9a-b7e4-f940e19ece5c | -6.36544 | -42.54598 | 2026-10-06 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a6ac0b26-34eb-3d41-ac28-e2f469cbaff7 | -5.84171 | -45.01594 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 54356d54-cc73-34e0-88de-6b2f564849a2 | -6.8184 | -39.30136 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9f0c022a-05c1-31f7-93b4-37d86e9098bf | -3.07357 | -44.45626 | 2026-10-06 03:42:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32a09a2c-60ba-331e-88f1-568a0412c688 | -5.84191 | -45.01638 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| da80ad49-9ac3-35d7-adce-0e602211f36c | -5.44098 | -43.44394 | 2026-10-06 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc1f7ea2-ccd6-3d4a-bd0f-ded8de72032b | -4.72191 | -44.08227 | 2026-10-06 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed2369e9-58c4-3dad-8594-cba67305a1a0 | -3.94179 | -42.99199 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7033ffcc-d6a7-37bf-82ba-6e871e0398bc | -5.74833 | -46.6829 | 2026-10-06 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 74435cae-e8da-3db5-b480-ae4cae2c3db7 | -6.31905 | -43.34061 | 2026-10-06 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bf027f26-2862-362c-9d4a-911bfb861e60 | -6.82018 | -39.30355 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4080ea14-d115-3f38-8e0b-37052ccf585d | -3.93609 | -42.99225 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6fc1e90c-4409-3f5e-ad8e-3117d49ae928 | -3.94131 | -42.99482 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aaa934b0-4795-37f8-b56a-b123d0b2e62f | -6.42051 | -43.46936 | 2026-10-06 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9f52b98-d4b3-3c6e-a90d-4ad4f457dee0 | -5.32012 | -40.89748 | 2026-10-06 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 484e7e86-1e13-3416-95be-9db144048e2c | -6.61973 | -41.56955 | 2026-10-06 03:42:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 091acf94-f6af-3cd9-a936-0742284a5840 | -4.3646 | -47.7769 | 2026-10-06 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b53e15ff-5da5-318c-bb94-8d9f379c1568 | -4.72135 | -44.08546 | 2026-10-06 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1143078f-8fcd-329c-8e44-9a7254cf0479 | -5.8521 | -45.02158 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6337193b-eb10-37e7-a5c6-b498d5138b5c | -5.64472 | -44.11927 | 2026-10-06 03:42:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f287f4d0-ec3c-3763-80d9-79a413e3545a | -4.50829 | -43.69063 | 2026-10-06 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 003b641a-76bd-335e-b15b-bba0d3a22c32 | -5.46727 | -41.24067 | 2026-10-06 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a49f1eff-04de-31fb-83ad-64aab515eae1 | -3.93562 | -42.99511 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6da93b8-3358-3931-9cda-72da6d21d539 | -6.60874 | -37.88266 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d6474b7-e3fa-3519-b2d2-242f57d692e6 | -5.41116 | -44.35035 | 2026-10-06 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3be14a7c-ef97-38f6-8df6-f64e83a543c0 | -6.36079 | -42.54523 | 2026-10-06 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c7526880-4c20-366b-a0bc-f7c9b7700e3e | -6.61564 | -37.89503 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 10d24e52-3e92-3a89-bcde-10dea6164fbb | -4.50901 | -42.0699 | 2026-10-06 03:42:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c2cb96d-2e31-39ea-80f3-5fcfb5d6673b | -5.4106 | -44.35363 | 2026-10-06 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 553468bb-0e79-38c4-a362-7b6464842777 | -6.82515 | -39.30685 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| fcbe3b73-9cf9-3b69-97db-6918c8f32509 | -6.31807 | -43.34635 | 2026-10-06 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e75f4f27-bc34-30f5-a49b-ebde8030dade | -5.84104 | -45.0197 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 68df2a35-31f1-38c8-adab-f5ee7f7b753d | -6.61745 | -37.88389 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3964b08b-b95c-3900-9b85-79e4c9dadd6c | -4.19498 | -44.26432 | 2026-10-06 03:42:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a3e8f879-e05e-3307-9fde-e464a7474ab5 | -5.75494 | -46.67912 | 2026-10-06 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4cfd6c56-7e91-3742-ad4a-7c141bfe0401 | -5.61664 | -44.84214 | 2026-10-06 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b1affa1-0119-3d1e-ade7-281095fb00b2 | -6.34527 | -42.55233 | 2026-10-06 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 95f36dfa-3350-33cb-a4a2-fc11f262fb63 | -6.61921 | -37.88422 | 2026-10-06 03:42:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a7ec0531-081c-38a9-b7f6-338c5424e90d | -6.45182 | -43.82645 | 2026-10-06 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 875416a1-8488-3cee-b3f9-aec6e7146b32 | -5.83146 | -45.01093 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9da2cccc-7344-3a6c-a0c4-6ef02fbbb5d2 | -5.46251 | -45.5215 | 2026-10-06 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ee82a85-c8ac-3334-b00a-221899aa4ee0 | -3.93729 | -42.98833 | 2026-10-06 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 191101a4-cd9d-30c3-86cd-0d8f9ea80c8e | -6.81342 | -39.29799 | 2026-10-06 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9ef13551-f7d9-3f50-a856-5ecaf4e50cd2 | -5.67459 | -42.5876 | 2026-10-06 03:42:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 796c461a-9aa3-3e81-864b-eaca69964ab7 | -5.4355 | -43.44587 | 2026-10-06 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f432a38-4be6-3221-b2f5-8e109c6eb0ea | -5.60642 | -44.03075 | 2026-10-06 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16a4924e-2771-3803-a9c9-328e7aaa505a | -13.87544 | -43.79486 | 2026-10-06 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2803c361-8839-3ca5-afc0-00587526170b | -7.88269 | -44.19043 | 2026-10-06 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e611b77a-cad7-33af-a454-0b516d4ace42 | -8.5836 | -45.66793 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5224600-d50c-35b6-82b8-c8d071242422 | -12.64188 | -42.86047 | 2026-10-06 03:45:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 064560d4-0f82-3c43-b6a2-a74824547a9e | -11.27879 | -45.49915 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f669bfba-142f-34ba-a43c-58280da67270 | -8.69405 | -45.21695 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4991e942-8fce-3f0c-9b5d-6e80c5fe4ec5 | -11.66811 | -43.64021 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d47d4b9-03bb-3011-a995-eada4598532e | -11.27728 | -45.51152 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| d22599ae-fce6-30ed-8c50-97811bd815af | -11.29224 | -45.5178 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e7b1e45e-3cd6-3fa0-8a8d-1c63e2252244 | -8.60226 | -45.65925 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 432a87b8-064a-33c1-afe1-c6ac8e50f8c4 | -13.00204 | -40.14371 | 2026-10-06 03:45:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bb4d0b82-876a-3015-a2d5-b50d199de83f | -11.69486 | -43.67477 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6952f17d-540f-382b-b290-95b0144853bf | -6.93159 | -43.67361 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60776122-8cef-3576-8665-b277ebf81145 | -6.01008 | -47.39894 | 2026-10-06 03:45:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cbc87372-0857-37a5-a73f-1d92a5f5a8e8 | -11.28125 | -45.51892 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41625354-fd9a-399c-8b8c-5d1fb3cfa1be | -11.27702 | -45.50875 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b7306115-22aa-3655-bf4e-72ee1666cca0 | -10.36794 | -45.03118 | 2026-10-06 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c15aeb9-11d9-350e-ac78-e04468247169 | -7.01339 | -43.44834 | 2026-10-06 03:45:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5b444ec-3723-3009-a2bc-d47407caef0a | -13.87631 | -43.79583 | 2026-10-06 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 42d97717-1081-394e-93ea-a8f7e0a6f0ba | -6.72451 | -44.27844 | 2026-10-06 03:45:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 489be212-8fb2-3429-b839-dee8a1e404cc | -14.07219 | -44.4852 | 2026-10-06 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c5200db-477f-3d8b-8570-9d66bfa49618 | -11.28706 | -45.51671 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5f2e0942-cc8a-3c71-b4f1-be11fe85b135 | -11.5353 | -44.89199 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86cd7ea4-4fdb-3ffc-947e-8ffa1cde197e | -13.0262 | -43.12471 | 2026-10-06 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 803916cf-b94d-324a-b981-100fbcba5bc7 | -7.37669 | -46.22845 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1873ddb9-ff26-39a4-9342-fd4800433fef | -11.27642 | -45.51198 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 284a0183-5967-3d5f-9b49-e62945d587b1 | -8.69343 | -45.22038 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 965d0738-0440-3015-8699-8493ff0e6f33 | -7.29133 | -47.27543 | 2026-10-06 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aad126b-e615-37c7-a5a6-2b6a898dfebd | -12.20252 | -44.65843 | 2026-10-06 03:45:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b8a1cf4-1c5d-33e3-9a8d-fb07ed603af2 | -8.45475 | -39.56013 | 2026-10-06 03:45:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9649c7b3-c644-37bc-abc4-a96c13d94e95 | -11.82541 | -44.69188 | 2026-10-06 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d7f58997-f6b1-3ca9-92bf-44414cebf2c3 | -12.76402 | -44.87566 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8ce80ad-8ed6-3bed-995c-84a33b352d10 | -11.28853 | -45.50468 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1e188fe1-fdd5-3d23-9328-57ca31a57c0b | -11.26081 | -45.50908 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| d2766a61-94e7-353f-afdb-1b51beebd26f | -6.88891 | -43.68378 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf30cc6d-0bec-3211-85fc-bad6b6b838e1 | -11.27973 | -45.49876 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8e74f533-e31c-36d1-9b7d-0a69df517c41 | -10.97533 | -45.4159 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 775735f6-afd4-332f-aac4-6d35d336dab0 | -11.68574 | -43.673 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a39a1992-de33-30ac-98d7-64c6c45f7be4 | -11.28623 | -45.5172 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fc66ac2b-c544-3a13-9946-8488d1bf3974 | -9.08903 | -47.0705 | 2026-10-06 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52d94ec9-3107-3d39-bcfd-16ac954206fe | -10.97421 | -45.41671 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 500fcd07-2a89-3094-aff2-17bfc42300e1 | -11.72449 | -43.64093 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e96d0f29-e623-3bcf-a01c-e4b08cef2b76 | -11.68534 | -43.62314 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e1e14e0-9b62-39ea-a991-2ae240e463b4 | -6.71547 | -45.97854 | 2026-10-06 03:45:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8e15961-503f-3842-8c05-f5eaa728d85b | -11.27208 | -45.51055 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 8326cb0f-da76-3ebf-ad95-da1652735a05 | -11.28767 | -45.51352 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 597ca570-72b2-3dd3-9c93-ed44246c8599 | -6.87944 | -43.67935 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e23d3e84-c3be-3238-948e-fe32f298b73b | -6.91802 | -44.56279 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
