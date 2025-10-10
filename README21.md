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
| 1f5a3e18-92af-3d99-95dc-9be605066bec | -5.24943 | -42.99768 | 2025-10-10 04:00:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 383039e6-29fd-3454-92e2-4b1b08933de9 | -6.82494 | -42.78543 | 2025-10-10 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 22e58ec6-83be-35a3-9740-1082c6d20ff9 | -7.67875 | -42.39523 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d34d3b0b-a808-3edb-9581-54b2df74e650 | -5.99146 | -42.47482 | 2025-10-10 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 347ec854-4fd4-3e20-b282-6a7236526937 | -7.03288 | -42.28948 | 2025-10-10 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1539715e-dd8c-3e62-8d29-29ade52244a5 | -8.83146 | -44.4214 | 2025-10-10 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 174b8fae-0de9-397c-baca-e968f65b4eeb | -9.16138 | -41.0587 | 2025-10-10 04:00:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f6c7f3d-bb03-39ad-aecf-cae3fcb4759e | -7.56986 | -44.28463 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93420a6e-233f-3e14-ac2d-0bdff06bedb4 | -8.20473 | -43.37785 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54b9f666-4409-3db2-8f7f-80ebe59f5929 | -7.31747 | -42.94044 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3e6fa66b-2f92-35db-b7bc-481efc761f42 | -7.77232 | -44.04914 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e2e4d5c-d7b3-38b0-9749-0ce5da549962 | -4.47826 | -42.85985 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97d12d36-bb68-37dd-a55d-f88631497839 | -7.77311 | -44.04448 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a166dbc-c6a0-3207-861b-14b5d0579066 | -4.95228 | -42.82265 | 2025-10-10 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 851ec98e-0b4f-3841-80af-675c6a4c52b7 | -7.29198 | -41.96772 | 2025-10-10 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9e7b92a3-3fc9-3923-bb69-e71649ec6f6a | -6.25412 | -39.74569 | 2025-10-10 04:00:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d6a0b0b-d0f1-3be2-8984-ed8aa9dadd26 | -7.61551 | -43.06555 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ad71f1a5-3b8f-32dd-96a3-9618a11438ba | -7.79922 | -42.41016 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27a13c9b-5e40-3c38-886c-660107206c02 | -7.53432 | -44.30842 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6baeae77-9fa8-34ef-98e1-d3c3199fd733 | -7.77314 | -42.26468 | 2025-10-10 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db9eeab8-5d34-397f-88a8-994913e7f269 | -5.98324 | -45.92205 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9696daa4-6895-3fe5-b2a8-90a41e9cb033 | -7.03636 | -42.29005 | 2025-10-10 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3d9e00e4-580b-3b06-b14b-ccda7780fd2c | -7.6624 | -42.58419 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e5c6ebb-c8ec-3d99-9a63-9fe3db0d8769 | -8.84114 | -46.05817 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb3ad626-b7dc-3279-b423-6973cae6b213 | -7.26608 | -44.10443 | 2025-10-10 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 298975ab-064b-3d99-92b1-4b69e778065d | -5.84922 | -42.30266 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7441dced-de5d-360f-a083-502f67bb7a06 | -4.48631 | -42.85672 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da142a7f-3a4b-3135-ac2f-f85662a01a04 | -5.39559 | -40.97876 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 218cd287-59f5-3803-9a65-bb368c28b9bf | -8.57617 | -41.23136 | 2025-10-10 04:00:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d96290ed-5c55-3b3d-bda3-bede0dd5dc8d | -8.20534 | -43.34522 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6131cf32-3bfb-36fc-bf30-08eeb726bdb0 | -6.7467 | -42.82396 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2beeb5e8-a6e0-389a-8132-9b297596b100 | -8.18216 | -43.32843 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c76bf5fd-2d1c-38d5-94a6-325c40d50ede | -8.18645 | -43.32486 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 05ed1be1-d90a-3391-ad8e-910e124e39bd | -9.66072 | -43.84203 | 2025-10-10 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9c80c9f6-daf0-3bdd-9e18-8608b6672720 | -10.15183 | -45.17645 | 2025-10-10 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63d9c4f1-d9c7-33be-a8ea-b705667ee71a | -4.95298 | -42.81836 | 2025-10-10 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b0d1ff2-464f-3ede-962e-039ac50ff612 | -10.16423 | -44.59975 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c7e5b696-2c22-30f9-bc67-105e4eb0092c | -6.58481 | -44.62251 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 24ec9fb8-b256-3894-905c-bfb51714fb87 | -6.5725 | -44.16459 | 2025-10-10 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4175d6e7-6cda-33ca-8c20-8a368856457c | -8.89259 | -46.01128 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee61e397-ba88-31a4-94db-3dee19e42a94 | -7.49726 | -42.75254 | 2025-10-10 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ef08307e-679d-373c-b155-c9bd5f536a7a | -8.98666 | -40.57531 | 2025-10-10 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c66a333f-8eba-330c-b33d-0054fb6fe9cf | -9.3267 | -46.11222 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed54900c-00c0-3991-90fd-afcc846fd18c | -8.00342 | -44.45591 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3c2dee8-5e30-332c-9e0f-a9730bacd647 | -6.7035 | -41.55085 | 2025-10-10 04:00:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15e7f58c-b1b5-35e2-a7ac-725c4c6eb881 | -7.26373 | -44.91251 | 2025-10-10 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee752109-c3e9-34f9-8c4e-54db64e1150c | -6.742 | -42.85287 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07959c56-f4e7-3a4b-840a-46551d2591e8 | -8.1995 | -43.33564 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9fa6ca79-21e0-3b4b-a3c8-f67c4c7ed349 | -6.48396 | -39.81724 | 2025-10-10 04:00:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ed9c54a1-6810-39c4-8f86-0474a25e71b2 | -8.52182 | -46.17015 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fde2ecd6-0e18-3ced-a6cf-c17f87df6b69 | -7.63253 | -43.05173 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7cbea4b4-5827-3485-b0f8-3eaf896d59b3 | -7.11016 | -44.08883 | 2025-10-10 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccdb5882-3ad2-38ef-929f-0b7acd9af310 | -7.32104 | -42.94102 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cb134f4a-414f-3173-869f-a364815e8a5c | -5.39954 | -40.97567 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d1bad4f1-d9fb-3be5-8dd1-74d5b8772d44 | -7.80047 | -42.4025 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8da2b4ed-1741-3986-9390-1266d33308c9 | -8.51329 | -46.14383 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79f1d846-d367-3f03-8414-220bb764216a | -5.20567 | -44.35797 | 2025-10-10 04:00:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4df9b2a1-1afa-33e8-a5eb-82d922df6f8a | -7.83988 | -44.54622 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ace6a171-4583-3484-aea8-1c7d1d3af7b0 | -8.83526 | -44.42205 | 2025-10-10 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f3404f7-3e25-36d0-98a9-82e2b65c6b1d | -4.65284 | -43.19748 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8042a5ce-a78b-3a2b-a995-abade6a1a601 | -9.28247 | -45.78904 | 2025-10-10 04:00:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4608f91e-0919-384c-b4be-b6c272822015 | -8.18577 | -43.32903 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 76592ace-bea0-304a-924b-5cf3e1b7bb38 | -8.00643 | -44.46165 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2822303d-46a8-3f89-9d7c-609b4f4991d6 | -5.31742 | -46.06906 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bab5786e-2e04-39cb-840e-c474c373a1f5 | -7.86107 | -44.82392 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7b475fd-e0da-394f-bb2a-15e187015cf9 | -8.15696 | -43.32405 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4eb4b6b1-d25e-33ee-8bf7-f53697a560ec | -8.53104 | -46.16756 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d098ee4d-f55f-3d15-a0c2-76b6a5682baf | -8.50755 | -46.17645 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6ac16f5-c950-3c14-ab71-d176ae1fc3d0 | -7.78065 | -44.0457 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bb0a33b-8746-32e2-b609-cf48bd8f2584 | -7.79347 | -42.60088 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b28f2b4-081a-3ac5-98e5-ae4d3e4588c5 | -7.20245 | -45.49038 | 2025-10-10 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a48d359b-316c-3698-9001-2d8d660ce753 | -6.74492 | -42.85757 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 09f0484f-9b8b-3924-a5bc-bd662861ad1e | -4.4926 | -45.87697 | 2025-10-10 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d55a53cc-3072-3922-b995-a7c58fde2145 | -7.89891 | -37.06283 | 2025-10-10 04:00:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 666b04fc-83a9-3477-b857-7fbe749898e1 | -7.54525 | -44.29043 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18a737a0-c883-3e96-9985-b72d0d83f863 | -5.36958 | -45.00684 | 2025-10-10 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de583f46-b76d-3463-93ed-ff57dd119523 | -7.38128 | -46.94396 | 2025-10-10 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3b1d78f-2814-3f83-b59f-df7e62b0381e | -6.8187 | -42.80113 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a955b743-1120-3fd3-aa41-586e28468a24 | -7.28108 | -41.96977 | 2025-10-10 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a359273-8be9-3fe2-94f2-642f59e70241 | -6.55448 | -39.99513 | 2025-10-10 04:00:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 014f5ade-f48d-3c19-8beb-c67f158e0684 | -6.7438 | -42.81923 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f4e5bac3-f5a8-382a-8813-ae750b044760 | -7.21577 | -34.90749 | 2025-10-10 04:00:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c383a024-6a2e-3f89-a7b8-26d250dcb177 | -8.19657 | -43.33088 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f166f196-dfe0-3e27-99ca-48336a7106f2 | -4.85864 | -42.54187 | 2025-10-10 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 17347599-7d31-39f8-8ebd-afb5b41be5dd | -8.51607 | -46.17794 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daedf163-f029-3b9d-9e91-1f603efe1728 | -6.58536 | -44.63447 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f41ecdd8-a43b-3716-84ca-a90f0593aef8 | -7.7717 | -44.05097 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 359e0871-673b-39aa-bd5a-90c0247fce85 | -5.95981 | -45.68055 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6998051c-7c73-3ffa-b678-65985a1f710e | -6.75542 | -42.8381 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ab8002b2-e128-30b7-a47e-d79fa1fe2bc9 | -7.53513 | -44.30362 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69c97442-1eb9-3adc-8fb2-39074e941252 | -5.68573 | -41.72649 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea4b66e0-7fe6-3233-933d-4353b922d1a0 | -5.6429 | -42.7016 | 2025-10-10 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 30334c89-bb37-3385-aa16-e9a21c0c1eb9 | -7.42016 | -42.97643 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 85589034-a0e3-3c67-8d69-a6d5a68314b1 | -8.51681 | -46.1737 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6df0339-cc50-3a85-b120-69f7ad4fa370 | -5.84932 | -50.07726 | 2025-10-10 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| accd5054-082d-3bce-8aec-ae1afcfcc200 | -5.84906 | -50.0776 | 2025-10-10 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdf8e974-f0d4-34e9-ab3c-d350ac22d8c9 | -7.49372 | -42.75196 | 2025-10-10 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 15c5a4a7-d7eb-3f61-bc5b-142f29a6e947 | -6.07388 | -42.59105 | 2025-10-10 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8ec6ef7d-8853-332a-89ed-aef60c179e04 | -8.00253 | -43.75849 | 2025-10-10 04:00:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25beb4e1-7db9-3719-8806-2a6f7d2feee7 | -6.75609 | -42.83396 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README22.md)
