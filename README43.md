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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b96cff3-bf8f-3596-bdb1-19254a2026c8 | -5.87907 | -48.11555 | 2025-08-21 04:38:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f3ceb08-02a2-3db7-94b3-9369c9b02b82 | -2.62183 | -46.84766 | 2025-08-21 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffd89235-350a-359e-a410-f9f98e99bf99 | -6.21169 | -43.33388 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e01cef6-14bc-32fa-9f0a-2eac48b6015c | -6.26358 | -43.72219 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60fd310d-4995-3f9b-82bb-44a41e519953 | -6.49954 | -43.44638 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0f7a9e5-c1f3-3a8b-b3d6-3c751bbb8468 | -6.77385 | -44.33202 | 2025-08-21 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75db0fea-d56c-3884-869a-4dcda5e5e8a8 | -8.14083 | -47.34268 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9edb8b09-b243-310d-a168-fe56c0aa4f70 | -6.42428 | -44.66476 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e517d5-4ba2-3553-bc38-117aae89d307 | -8.14374 | -47.34717 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6e30d3b-53e8-3cda-95be-3b484ec274bd | -3.04141 | -49.44279 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2551deb-003e-3e5b-b908-b8d353e0f960 | -7.2708 | -43.68052 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9651b15-2613-36e7-8077-5b8c90e25595 | -7.26159 | -43.68336 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f20cf9fd-d3e6-38f5-a74a-abaf496bd03d | -5.96734 | -44.13257 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e68c28c1-0712-362b-8ec8-383d655ae473 | -6.08713 | -44.42234 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72a3e28e-fcf2-3023-8d6e-c9cbd4eb3a66 | -5.96668 | -44.14391 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3dd9b87-92a2-3977-921a-c6a4b808b56b | -6.10554 | -45.41311 | 2025-08-21 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09ac0684-ea0e-318a-984f-396dcffa3187 | -7.63111 | -45.24752 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abe2d748-82b8-3b42-a9b1-103851c70a71 | -3.03809 | -49.44227 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddf1d747-3321-38c1-a651-8f0d7e69bd6e | -9.48072 | -47.32479 | 2025-08-21 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18c4d5cb-9492-3f09-be72-e5de7dde00de | -2.90628 | -48.25362 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d8e9120-0867-3335-bf81-3f0e77752a6a | -7.63042 | -45.25232 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2139e99a-b425-3665-9463-3e5aa4c8b829 | -6.20061 | -43.56303 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6023b917-6be0-31d1-a68b-7a4f9ceea483 | -7.01501 | -44.6129 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e28b2b81-007b-3e75-be1f-f092bad106a3 | -6.31574 | -43.74985 | 2025-08-21 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06808da5-6fcf-3f2d-9669-419c0df8d9f9 | -8.21687 | -44.42525 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d3192a-6e37-3009-bf4f-af2246dcc89d | -6.27266 | -43.71926 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 671d39ee-4080-3a85-8e8d-fd96363a8c4c | -6.61537 | -43.88555 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0a993fe-0909-35ea-99e9-c4a8dc420f2f | -2.64856 | -48.81208 | 2025-08-21 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6503e85-eff2-3ebd-a8f6-06a49f4d5101 | -6.02451 | -44.36567 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeb3b9b5-a916-3846-84c4-599c5ba14517 | -7.7049 | -44.01866 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 01c0a602-799f-3c9a-a541-e42f143e9be1 | -8.02773 | -47.01223 | 2025-08-21 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32f2f42d-c311-3f0f-87bd-d466cae29546 | -3.96982 | -47.88365 | 2025-08-21 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 917a0f1b-eeab-3cae-981f-05181940813a | -2.25674 | -47.84724 | 2025-08-21 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c4a002-5e20-3e16-a3a7-4ecd5cd24823 | -4.95073 | -55.79119 | 2025-08-21 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c627bd29-6a30-39f0-b657-e240f6ba6d09 | -6.3645 | -43.32912 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9147581d-9fd1-3f4e-bf3d-260061b72aa8 | -7.261 | -43.68745 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8acbceb-0bae-31dd-ae6f-ad5c31e581df | -5.98088 | -42.84736 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 53ddbd64-7122-35e8-91e3-622559a882f1 | -6.31995 | -43.75064 | 2025-08-21 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1cf2ff5-7521-3f2d-bf75-c2de9576816a | -6.01243 | -44.3636 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be5a5c61-007c-3ee5-8e7f-48f2eaebd782 | -6.95645 | -42.86781 | 2025-08-21 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b5935490-6d26-3406-a983-5c1a96ae3692 | -7.64893 | -46.26352 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc023aaa-860c-3748-8951-d275a962148b | -7.57313 | -44.40023 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84dcaeb0-11f7-3ccb-ad0c-e6daa3821835 | -6.70875 | -44.31941 | 2025-08-21 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73442c3d-0eb3-3685-af9a-2eed4cf1a67a | -6.21688 | -44.13244 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fdc4025-e103-3077-92fd-913133f0d0b0 | -5.12218 | -43.21301 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dbfe06e-04ae-380e-92de-077e2cf2a3f4 | -2.55384 | -47.70807 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca96f00-d160-3920-b66f-442ecdf21b71 | -7.14358 | -44.17842 | 2025-08-21 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2bd43a5-c569-3f0a-890c-8a26cf04fa46 | -5.78425 | -43.60681 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 838907e4-d847-3fc7-a65a-eec64256b5dd | -4.86768 | -42.54296 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bea86b65-eb18-3f0b-815e-13010bfbfc17 | -8.83086 | -52.03722 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9df455e-6b4f-33cc-aaec-078a918382da | -6.57551 | -44.46516 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9d34c2c-69f0-34fc-bd48-fa9c1f910636 | -7.30589 | -43.68142 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dcd8937-f79d-3c98-bd5a-6b7fb79a3f1e | -6.53947 | -45.5098 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eadfb7ce-bf0f-3174-9bda-adaa66d529c0 | -9.48724 | -47.32988 | 2025-08-21 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64a35a9b-324a-3a59-8053-4583da26f967 | -6.41923 | -44.67124 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 08e4137b-687a-3dc5-8b5c-5fff79a71d56 | -5.13642 | -56.96834 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40006efe-4ee4-30d0-ba63-c2d502bd44cb | -8.02883 | -47.0098 | 2025-08-21 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d86a201e-1836-3173-b949-5d8105d16189 | -4.28876 | -48.27382 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8480043-ac25-31d0-aff5-09cb02ec8405 | -5.95794 | -44.14629 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4147b1a3-aa76-3862-95c5-2ba8b6a6cc48 | -8.38663 | -44.60117 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c9cd010-d1d8-3546-9776-a9492f9df1a4 | -7.39316 | -44.26838 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a79d2535-2611-37f8-9e51-0bc5f57fe104 | -4.94247 | -48.39347 | 2025-08-21 04:38:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 720baa46-d7f4-31b1-8d2f-5062556101e6 | -7.15118 | -44.64677 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3fd6044-0f6d-3307-947b-093af66c6155 | -9.8566 | -44.68929 | 2025-08-21 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 584b4b4e-925c-3b5f-86f0-fe5fd1213faa | -2.98495 | -49.30616 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bde2e99d-e5d3-31e1-80f4-bcdb80d9beee | -6.29732 | -43.87416 | 2025-08-21 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cf24508-a514-3fd4-b1ad-b99bcb899c8e | -5.78365 | -43.61085 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 339851f2-1d44-3b13-969f-5888dd208355 | -7.28129 | -49.39736 | 2025-08-21 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d5753f5-94ab-3a65-80e5-3717feda6b7e | -4.31211 | -48.08061 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95f54642-5fc3-34c8-9f9c-a51e1c7a3f04 | -7.53474 | -50.52297 | 2025-08-21 04:38:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c29009e-e22b-36c1-a2df-15f918a31726 | -6.10484 | -45.90208 | 2025-08-21 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e1aba43-c4c2-3233-bb5f-f9d812f6a7e2 | -6.45343 | -53.37834 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 451c27bd-574d-3458-a7ae-e823f01c62f2 | -5.47669 | -44.701 | 2025-08-21 04:38:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43c7c5b6-57c1-319b-8b98-eb2659b870b9 | -6.25934 | -43.72159 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2069d90-407a-3370-8cd8-34e0454e6616 | -4.94111 | -47.45969 | 2025-08-21 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dfdb428-c849-3bd7-a10b-f2aabb82f984 | -6.28362 | -43.87991 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58c0bb8c-f484-33e6-93be-4d3acde0046c | -6.74986 | -43.94278 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ebf67d3-0823-35e7-827b-eeaed3cba497 | -8.15248 | -47.36056 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70255958-c453-31bd-bc42-4ebf4c627f39 | -7.02504 | -44.62887 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 04ca7cf4-9406-38e0-8f6c-9fcd7206ee07 | -6.56843 | -43.00163 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ef8f2d7-ea5b-3016-ad7e-23a0059f1987 | -6.07047 | -44.14402 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e420fc75-cadc-3eb0-a973-0c29e59d2b52 | -6.94739 | -42.86641 | 2025-08-21 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a3eea481-0cc2-36a8-bab9-cd8859f8723c | -3.01678 | -49.21208 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3deb16d-8f12-374b-9008-f64799b116b0 | -5.79319 | -45.075 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13c68767-7532-32bd-b696-c2e5aeacb00b | -5.95491 | -44.13863 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07eab767-6d8e-367c-9641-45ad0556a792 | -7.42003 | -46.87379 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06ecd004-cb73-3d86-97e6-f03230a5b800 | -8.8553 | -62.3743 | 2025-08-21 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| f897eb23-1490-34e4-9ced-34e1b5492cc7 | -7.0354 | -44.6167 | 2025-08-21 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 8a74b0e9-c403-3847-9fc0-b84407e6da99 | -14.6519 | -54.875 | 2025-08-21 04:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 44ed1898-2991-360b-8dfc-e3228422c24e | -8.8739 | -62.3735 | 2025-08-21 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8f109a03-23f5-3948-a2ad-14a94d68004f | -8.8737 | -62.3925 | 2025-08-21 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 150034ca-8276-3aa1-a22a-4b2a2a792621 | -8.8552 | -62.3933 | 2025-08-21 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 31d5098b-755b-344c-8636-3bc479222e95 | -7.0352 | -44.6396 | 2025-08-21 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a27ceaea-a090-3f0e-8319-07cfaa34e2f1 | -7.0166 | -44.6184 | 2025-08-21 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 294.5 |
| 08d9b9f5-b8de-3559-b97d-22bb7ffa1f11 | -7.0164 | -44.6413 | 2025-08-21 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| a69d0577-dc0b-338b-96eb-5d0980eec501 | -8.8551 | -62.4123 | 2025-08-21 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.0 |
| e37b2348-7ed3-3a2c-8824-717145d0669f | -8.8736 | -62.4115 | 2025-08-21 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 121.4 |
| b8e9af51-a945-3508-9925-80598d3ffffa | -7.0169 | -44.5954 | 2025-08-21 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a1e342ca-8263-3634-a1d2-fcf046557e8a | -14.6523 | -54.8543 | 2025-08-21 04:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| de48779c-4013-3749-9081-5882729e6cca | -9.66317 | -48.37937 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README44.md)
