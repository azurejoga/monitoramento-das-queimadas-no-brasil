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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33578302-30d1-39a7-adf9-29ed2aca6aa8 | -5.22027 | -56.10804 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db0af606-5fe5-3882-90f4-f314010c6327 | -7.3398 | -44.46615 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8633f460-7df4-3a24-ad79-0142e168306a | -7.3167 | -46.7556 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e07ac993-ab41-3343-8537-22e2dafa0aa8 | -9.44178 | -45.38812 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| adb26bce-f74e-3c12-8f7a-76b4fa1dc305 | -3.44022 | -50.61589 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2fa8f859-dcc8-3696-a739-2610b8ea585f | -5.81723 | -53.51701 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2680d523-b4dd-3f45-8ace-e6cd846b4db8 | -6.65909 | -50.89006 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 232909d1-e632-39cc-ac29-9af2375d1aca | -4.59051 | -45.16068 | 2026-09-21 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 249699c0-ce62-3777-90bf-4fa99d62145c | -7.42918 | -42.11619 | 2026-09-21 04:19:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b359756a-30fa-3001-87df-39f19caa974c | -8.37579 | -45.62613 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd86c53c-867d-3672-9515-5ceae759c065 | -7.58175 | -57.69639 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 179f18b0-2061-37ab-8dff-1d8154ba9313 | -9.44765 | -45.40369 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8fd13f3-dfec-3752-acf4-bd5518b77c4a | -3.33585 | -42.77033 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e447035-c25f-357c-8b1e-b35755060922 | -8.00897 | -44.81044 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ba06d7f-68c2-39f6-88f2-d33053d3eb9c | -9.26979 | -46.18822 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f35158c-8768-36d1-b4eb-988905b14a9b | -5.82869 | -53.51925 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88f1c62d-dc90-39ce-a0ee-e135c0c7cd2e | -2.88915 | -49.48521 | 2026-09-21 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8438383a-b1b0-3703-9132-861d18cb5f10 | -8.78485 | -48.74252 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8bfbd116-a0b8-3635-90ca-24275d045497 | -8.38547 | -47.18174 | 2026-09-21 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3eab63d-4353-3581-8c30-97631a1d21bf | -7.08283 | -46.28499 | 2026-09-21 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c73714e-2aea-39c6-b821-4db35d41eabe | -4.40314 | -55.24429 | 2026-09-21 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 521936cc-6401-3167-8f99-beedc96d41ec | -7.10483 | -42.08525 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4fdaa8d-f7af-31ce-ab4a-d3118436e12d | -9.44805 | -45.42239 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9189296-7550-3e0b-9c07-d317dac40eed | -6.06467 | -55.6242 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c960ce-7e9f-3771-aff9-a4d78c4363cb | -9.46152 | -45.42466 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59f3e203-09a6-3f7c-b0e2-b896a0138a2f | -6.88787 | -41.70312 | 2026-09-21 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fa52ade4-71f8-3158-a283-268b532a009c | -7.31257 | -44.19141 | 2026-09-21 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6cc3301-429c-3e1f-b286-fa8968348414 | -8.78747 | -48.751 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c91f9e7b-d6a3-38ea-918d-cbe6c12d44ce | -7.1288 | -43.10229 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d4482a89-c7b8-30de-8b72-e84ec276238f | -4.11421 | -46.38337 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39032200-cad0-3eb8-9881-5c6d0d6829c8 | -3.39108 | -50.44299 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 83ddad51-619f-39e7-86a8-46d4d36df62b | -4.33724 | -46.37116 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57fe5dd7-e0f7-3b33-83b3-58d9a3b7655c | -7.59191 | -43.43878 | 2026-09-21 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4fdaee2-d179-3a00-ad16-782a742e5c5e | -6.28537 | -41.76814 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7720fea1-99f9-3345-b9c3-6eb3afae66e8 | -5.73153 | -53.46038 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00d7ab2e-4f3c-332c-b125-98b27a1ec76f | -7.95605 | -45.23309 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c95a2033-061d-3f6a-bb99-b483da1df930 | -7.2468 | -55.60254 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f16af656-c440-3f7b-ae92-67ecfaa18da3 | -7.4217 | -44.78148 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a808012-cacd-30f9-8489-abc07c5885e2 | -9.56804 | -46.55434 | 2026-09-21 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e572465d-fd2a-3e44-acdd-9c8c2d60f494 | -6.97638 | -42.16777 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3904efdc-d9e9-369c-b8af-6d8866545e03 | -9.45537 | -45.41994 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1cce437-bec1-3395-9ad1-befc090e1d72 | -7.07929 | -46.2844 | 2026-09-21 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9dbcca2-548f-3cc3-b2f5-d57625f212f1 | -8.87927 | -49.73933 | 2026-09-21 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57d6c7e0-238d-3679-a6ee-c5db8f227d29 | -9.46846 | -45.40335 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22c6124e-540e-3904-b180-524f3c711a54 | -7.38006 | -46.0388 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 173974de-17ce-32ee-b52f-b631e1dd3ee7 | -6.83613 | -46.04181 | 2026-09-21 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdbb8aef-b0c6-317c-b09e-97c206d58465 | -5.41615 | -44.25653 | 2026-09-21 04:19:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9225c307-b4e6-3020-8ea9-826d7536cb58 | -9.47797 | -45.40863 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 510aed4c-e654-30dd-9662-72a73ce4e557 | -7.74261 | -45.35716 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64c0ea53-9b70-3d1b-bd53-a25c9f491d95 | -6.91655 | -42.94035 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ce9f2ca-46da-3445-937f-af0daf77e9ac | -4.55866 | -55.75648 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7371e658-33ac-36d1-b5ea-d4642a82399a | -7.82039 | -45.26434 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58445f3f-df1f-324d-be82-effa32cb705a | -6.91968 | -43.73616 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d23c0b2-e998-31df-bbc3-8d220ca272b3 | -8.7603 | -44.29548 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00cd6273-30ab-314e-9cda-1d722090081b | -4.54356 | -42.97538 | 2026-09-21 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c52220ca-2b0e-33f1-9a62-2b48f0e1d978 | -6.55003 | -44.13719 | 2026-09-21 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0fb567c-8635-3fed-bd13-158fb60ffe7d | -9.5387 | -45.39648 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9de18516-9178-3659-9dbb-4fe8e57cf77f | -8.77097 | -45.87012 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e1fddf3-26db-3cdd-8878-f389b077d361 | -9.47342 | -45.41534 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a1f7db8-9c33-34c6-897a-2b8b8f958674 | -7.01911 | -46.44958 | 2026-09-21 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80d09364-6aea-3f71-9a7d-43e0f24c5eae | -7.33287 | -55.61016 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f50ea9a-c347-3eb7-8269-2c69d2c86fae | -6.73449 | -55.07512 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d349421-1ba0-36cc-a462-959df5fa57e6 | -8.45185 | -46.40073 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0244321-9510-31eb-8048-273b8564f7ca | -7.42563 | -44.77845 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5e7f26a-01f1-3468-aed7-25e7efa37503 | -8.37641 | -45.62233 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78a43945-061c-39a8-a75b-d56d6a1bc0c3 | -5.19991 | -56.10415 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f9f9aaec-3e50-3f8f-8768-00c6dd7e71b6 | -4.41022 | -55.24886 | 2026-09-21 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bacf97c-bc09-328d-82cf-71f3c39d70e6 | -3.16672 | -48.61319 | 2026-09-21 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da30a90e-1351-3fcb-8bd2-1cb33853409d | -6.2718 | -41.65467 | 2026-09-21 04:19:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab8365c8-53ea-378a-9c02-08abd9d776f9 | -7.38451 | -46.03861 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15971e58-727e-3c58-8f88-5121ecbbdd7c | -9.47183 | -45.4039 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 989c073a-006d-368d-b9a4-61844112a1ea | -5.85992 | -49.80359 | 2026-09-21 04:19:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f15a64e1-9c33-3622-9d5d-46af0eaed1f4 | -3.60969 | -54.04701 | 2026-09-21 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64fc58a6-f710-3521-b245-febc7e5cdc45 | -9.53534 | -45.39594 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b18853ec-8ec4-3790-9d32-28bf04d4775b | -8.77002 | -45.85439 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77da1244-5580-3aad-a145-dc51f43d06cc | -6.91265 | -42.92192 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| de14acb3-af3e-39e7-907f-aa1a2eb86600 | -6.93228 | -43.09935 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8917538f-561a-30ef-a3ab-a683cc2f60ce | -4.35243 | -55.50369 | 2026-09-21 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c08722d-e086-36ec-af62-a8c34a7973b5 | -7.43071 | -44.76829 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf0e6914-85c1-3f8b-80cf-b42d999d631a | -6.91472 | -43.74603 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdf327d6-f1b2-3e41-a59b-536dcce07627 | -4.34371 | -55.67323 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bd8c0713-861a-3bea-afc3-8e24b64a805a | -7.05626 | -49.90741 | 2026-09-21 04:19:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d1f1f47-c924-3eae-bd65-f87ade5b06a6 | -6.55539 | -44.84516 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92ebf9a0-c2c8-31fa-bc6f-8f9ed466ff9f | -8.02687 | -49.54689 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63996fc7-de12-3cdd-b5ec-77e3e8f8ff46 | -9.46509 | -45.40279 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb9df988-9939-30dd-82e4-da94d0544f50 | -2.89917 | -54.18673 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99f443bd-cdc2-3cc8-b83d-e56fb43ed1c2 | -9.26854 | -46.19583 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22614b7b-8494-325d-a4ce-e99b2e3cbbb4 | -9.44607 | -45.39223 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a4775449-ff90-372b-bf0d-3c43bb032d97 | -3.9471 | -40.96671 | 2026-09-21 04:19:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8bf636e-761b-30dc-bc40-70fdd87ea50d | -9.44825 | -45.40005 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 5331ce69-5d0b-3575-87cf-43ffb4948009 | -5.19666 | -56.116 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98c5d0f4-af50-3ded-bb20-b0478a9251b7 | -9.25531 | -46.18983 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6078856-692f-35ce-b294-2c819326a876 | -9.4534 | -45.38971 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3a8acf4a-54b8-3725-8c03-48fd7049f645 | -3.1725 | -51.35555 | 2026-09-21 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d9c346c-0a3b-391a-a5aa-059046e947e8 | -3.45282 | -50.60097 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9e48c8f-d2f2-3dd3-8617-70ef0411a70c | -5.9952 | -41.04504 | 2026-09-21 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 50269885-b9b1-3862-921b-6832afab8fdb | -6.91527 | -43.72124 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbeda184-4996-3e02-ab3c-2c723d7eb495 | -9.45063 | -45.38553 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4891afef-7546-3e2e-8782-bb51f0cc4163 | -9.46132 | -45.38357 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9dc78460-cfdf-3c5a-987b-e10c542778b4 | -7.13402 | -42.07503 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
