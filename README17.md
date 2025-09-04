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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f05d7e45-6694-3f24-a6fe-f3f2970b2a1b | -6.25734 | -45.09856 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 196e0162-fae9-3915-9553-45bf68001f9b | -11.97006 | -45.78934 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcfdf32f-2128-3165-a206-eb4975a7fcfc | -6.26812 | -44.51245 | 2025-09-04 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e1be4a8-bc45-3b9d-aaa0-6a83291c5694 | -11.59525 | -47.78721 | 2025-09-04 03:36:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 465db841-fc86-3329-8fda-dd6d7d5d44b1 | -7.93435 | -44.93819 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35076051-cf31-37ae-abcb-df25f691b060 | -7.36306 | -44.32853 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9b565bc-9365-3e61-9a3c-d1015ade99f2 | -9.53221 | -40.32323 | 2025-09-04 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b188fb98-64a9-34ad-833e-13f1635bbfe9 | -6.54243 | -42.94725 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4edfb84d-2b51-30aa-8ca4-44bbe1d3a69b | -7.04269 | -43.27069 | 2025-09-04 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e9a5f132-b631-3fe3-b84e-55567fab85ea | -8.38601 | -36.70547 | 2025-09-04 03:36:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d763ac46-c4ba-3b2c-80c4-bd4b0786fd49 | -6.27711 | -43.85146 | 2025-09-04 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6775397a-fa2e-3e69-95fa-9a64cac05a40 | -6.77908 | -44.08625 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9632d1a3-093b-30c6-a4d1-5a0b0359d988 | -11.24101 | -44.9601 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e899d9e-89bd-3944-abc8-74ff0853f9e2 | -9.60024 | -47.03492 | 2025-09-04 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10510496-fe75-3088-928a-0e8a601abf54 | -8.05113 | -44.14121 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dae30a05-2030-38b7-b665-15314e229130 | -11.23783 | -44.96273 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98ba2d1f-448d-3e54-815a-ac7b33aa1620 | -6.54152 | -43.91319 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55ff27a6-9ad3-35f4-a58e-0ab81f416d7a | -6.27289 | -43.84964 | 2025-09-04 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b116388e-7463-3d1b-a730-efcb30f20bf1 | -8.06886 | -45.34725 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78b98237-9c20-379d-8b6f-0a7233fede76 | -8.89319 | -45.80161 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f081c56-c1b9-3533-81ff-6ad85358e5eb | -8.02721 | -44.06565 | 2025-09-04 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65788d38-6a38-3435-b2ea-6d2daed12259 | -7.76184 | -43.97192 | 2025-09-04 03:36:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59f7febd-fced-3e74-8ecf-6aa4c91e86d4 | -6.49784 | -43.07518 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc284422-ca92-338c-bd8e-08c6df46f60d | -11.04128 | -45.14652 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 095239fd-3a96-369f-a345-cdde67d7f218 | -8.08587 | -47.58768 | 2025-09-04 03:36:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b23755e-652a-3fdb-886f-3d118caca1b2 | -11.24022 | -44.96412 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f749528-5485-3b90-86e5-052c5ba7cd4d | -6.2721 | -43.85398 | 2025-09-04 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1d5ed6-a48f-35dc-b994-ca93746a6e1b | -8.04854 | -44.14056 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 762bb470-00c9-360c-a39e-76aca2e6731b | -9.46447 | -47.60748 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a60b994-cd11-3aea-858f-97bb05e4d540 | -7.92916 | -44.93286 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f75e699-f429-37d4-addf-88fd847d9e13 | -10.03294 | -46.09 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de5e1e37-56a9-36dd-8ca3-cc6a1074d1e7 | -11.95511 | -45.77286 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d72d13c-ba75-351d-b945-12c3c3fa9546 | -6.26435 | -45.09525 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6ff67eaa-9d7b-30d6-87d6-c8ca116f0951 | -6.79189 | -44.44963 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 288822d7-7716-32d5-bf73-97d078f08c74 | -9.59911 | -47.04061 | 2025-09-04 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d628213b-02c4-35de-bcaf-27ac3881af65 | -6.54441 | -42.95201 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c3a21e8-df63-3b7e-bd5c-369d4ac92226 | -6.87976 | -45.56057 | 2025-09-04 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 044bd487-9ade-3937-85b3-db7e91dad63a | -8.06779 | -45.35127 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8cf7e4c-8644-3880-b1fb-da2dffe6a58c | -7.41353 | -42.04544 | 2025-09-04 03:36:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d54835c2-4ecb-375c-814d-d25d4227e4a3 | -12.15313 | -43.70672 | 2025-09-04 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac7a1de4-b74d-3cfd-82dd-b6eb257d58de | -11.0519 | -45.15294 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a3df78c7-cf70-36cd-b367-c57cfffc7d9c | -10.02582 | -46.0937 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ee59195-a097-38fc-9966-caeeef068744 | -6.59132 | -44.0699 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 165d22d5-d50a-3b8d-8e15-28382079d588 | -6.59428 | -44.31931 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96866a0c-4f36-3aca-b7c4-9c49b802e16c | -7.55155 | -45.72313 | 2025-09-04 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f067906a-e844-3b8c-ade0-95508e142d7a | -6.25904 | -45.09697 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 19d6acf5-595c-38cd-aa4b-ed7c9b1d115d | -8.05552 | -44.1343 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5dacfbe-4a2b-39db-9b5d-3c48866af4c4 | -6.79139 | -44.08821 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4c09920c-47a2-312f-a19e-a4b329f74245 | -8.8687 | -37.02905 | 2025-09-04 03:36:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| deb92a60-f343-3217-a5c5-d86d0d9b611a | -6.80563 | -44.46297 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0252dbe5-3d6e-36b5-a9a4-969aaf194a92 | -7.75983 | -43.9686 | 2025-09-04 03:36:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62520a0f-73d8-356c-913e-34f70399a1cb | -7.97135 | -46.3493 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73154000-8c5b-3b3a-8434-d3ca8a168143 | -8.02231 | -44.12426 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86020aa2-b166-3099-90aa-906ee4a1119c | -9.61451 | -47.03178 | 2025-09-04 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2aae7f0-9430-3f47-8ab9-2f09229cfbc7 | -8.61041 | -40.31424 | 2025-09-04 03:36:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e8603bc2-d09e-33c5-b7b6-4b523613b51f | -7.93557 | -44.94706 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc94f893-2f12-3961-beb3-4e10719fb2a0 | -8.03022 | -44.14496 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e9264ea-cd99-3d27-931a-29ae676861e1 | -9.81637 | -47.81378 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0820043-8095-3951-bc7c-c8e2bec945a4 | -7.93178 | -44.9524 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f03f3234-d26c-30cb-b452-553558129e46 | -11.9091 | -46.66165 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e3f38438-0a4f-38d5-ae5a-8deab96971c5 | -7.54527 | -45.7219 | 2025-09-04 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09129ff9-0c84-3c11-a96e-1a4a5b646fbd | -9.61997 | -47.03869 | 2025-09-04 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2724e4a-87af-3a03-b6b4-7a2797d1e919 | -8.43207 | -45.05415 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3a192fe-e281-399c-a788-813ed20b5525 | -7.76252 | -43.96815 | 2025-09-04 03:36:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6a4309-c469-3220-a30a-9f2dfcb870d1 | -6.8844 | -44.8853 | 2025-09-04 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b99a2fc-c2c6-3845-a593-a743fa31d032 | -11.05346 | -45.14494 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9c217f77-bbd6-3b0c-8dd3-9eb4dcaa4b3e | -11.05544 | -45.4108 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c8c162-fab0-3d30-8258-97c47a05caf3 | -6.53881 | -43.10608 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8de1618c-cba3-3239-8ba3-c0f95fe11fd9 | -11.12857 | -44.63731 | 2025-09-04 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab43b105-1f7c-3efa-8dc9-f74e31f86427 | -9.03547 | -47.02066 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06ae837e-ae1f-341b-9de0-af0ddac0086a | -6.3355 | -45.67943 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 474d4e1d-007d-3654-9afe-60cdde8d4c38 | -8.43803 | -45.05525 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e72dc8f8-1f3c-32d3-8e54-3db97f166ffb | -11.03154 | -45.13556 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 43e15962-0cae-3396-9620-d16d47120708 | -10.98323 | -46.82846 | 2025-09-04 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2690f8de-a0f1-3abf-a7b7-c788475cbf34 | -6.78349 | -44.09889 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 461c44a2-770d-3f74-9614-5c2be0259cb8 | -6.7829 | -44.46581 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b23ab1e3-8b85-3a07-b336-30e66e8bca85 | -11.24347 | -44.96381 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d6215c7-b920-33e8-bd1e-a97b053a1024 | -7.04818 | -43.26474 | 2025-09-04 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc261b9f-591c-331d-9a9e-7f5d3e88823d | -6.87084 | -45.57354 | 2025-09-04 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e9775c81-267a-34e0-bb2b-8249d9372322 | -8.02923 | -44.0546 | 2025-09-04 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8e393f0-dc84-3ab0-aa71-b013ebb81723 | -8.89413 | -45.79665 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b43f12be-441c-3216-86f5-6842aaa9e80d | -11.95637 | -45.77509 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8e6793a-2e67-30f4-82e7-0e2973f1bb20 | -7.97242 | -46.34356 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40830078-507b-3278-a45a-513105fea6ac | -6.78367 | -44.46156 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a08bcdf-3bfa-36ce-b837-79ecf2b0c69b | -8.91464 | -45.88101 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b198c8d4-29fe-375c-b0ce-aba7bc6f8c76 | -6.78017 | -44.44719 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc569357-a69a-3401-9bf1-a688c602948e | -12.15254 | -43.70979 | 2025-09-04 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d22515a-53ea-3772-b011-ecaffbed9364 | -9.07221 | -46.99438 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3c5f16e-6f8a-37f7-99dc-9ee6b26f34b5 | -7.46216 | -37.3868 | 2025-09-04 03:36:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dd02be6-3a3f-3bee-8535-c39316b6cc8b | -7.15481 | -45.23354 | 2025-09-04 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20b2ccdf-2c84-3937-a6aa-5a4573d98833 | -6.27869 | -43.85022 | 2025-09-04 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb82e445-777a-318a-9e67-4ad88daa2fbd | -9.48438 | -47.61807 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6b6ef10-0e07-3d39-98d6-da0b10d0b4b6 | -10.97807 | -46.83179 | 2025-09-04 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2db8b24f-f6de-3297-9d12-ecfd8b7731e3 | -11.0511 | -45.1571 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 075e2cdd-100e-30c3-8f8e-a71d455f907b | -6.54082 | -43.91711 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 379c9e8c-8b93-3d96-beb5-510d94dce1a0 | -11.0454 | -45.15582 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0cf0a97b-7203-3161-b654-e0a4a5c0356c | -9.42994 | -48.09734 | 2025-09-04 03:36:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6934b558-e183-3792-80f7-ee6e0bd2972c | -6.54423 | -43.10701 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39fc7917-04d0-343a-b727-5ae034a3ca85 | -11.04474 | -45.40389 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdcec337-d0c6-3e4a-8a36-d836f32aa812 | -6.17214 | -47.28764 | 2025-09-04 03:36:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README18.md)
