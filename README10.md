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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2042a118-4b17-3b5e-824e-39add5efd411 | -9.15929 | -59.50002 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 95c993fb-792c-3e88-8264-acbf4c66ea19 | -6.61445 | -48.05143 | 2025-08-24 00:50:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5573c573-1496-37e9-86d9-5c108b541037 | -14.77754 | -55.98512 | 2025-08-24 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 26641f4b-862f-3da2-805a-9569b16cd02f | -5.8604 | -52.09063 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6078b775-e85a-3485-863d-6148bd443d3f | -11.99757 | -61.03217 | 2025-08-24 00:50:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 171.1 |
| caf77baf-5f9e-3811-b94d-db879dfe13ca | -8.83859 | -49.90077 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d4187a74-3cc6-3ca4-b172-3e9f56e996ff | -7.62161 | -45.24419 | 2025-08-24 00:50:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| c66dfdf0-3b77-3788-aa79-054368009207 | -9.2036 | -60.79862 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 3b57a325-ea58-3db4-9fdd-9cd0e0b93dc1 | -8.54144 | -48.86607 | 2025-08-24 00:50:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9487cd08-1c9e-3aa1-a658-729278369570 | -9.19683 | -59.62506 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 57a9fcde-c0f9-30a5-9715-b2f578854378 | -13.47359 | -46.88485 | 2025-08-24 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6f0e9ae3-28ba-3495-bea4-facc4ec2e059 | -6.61228 | -48.03723 | 2025-08-24 00:50:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a80b5e1d-5080-337e-965a-3dc365908c57 | -6.31129 | -59.88633 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 91f27629-d8e4-3685-a276-a1128a8cfbc7 | -13.04669 | -45.22962 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 3b82c19e-ef0c-32f4-a0a5-5d83decb293b | -14.50413 | -53.09751 | 2025-08-24 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 264eeed6-f9fe-33c5-8611-90d9c6b08031 | -10.59584 | -50.18609 | 2025-08-24 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 2c84a977-a19c-3313-9da6-afabdfbfd7ce | -8.71292 | -51.1425 | 2025-08-24 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 916f62b1-b7d0-3efc-92f5-fd065d9013a3 | -5.85915 | -52.08169 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6c54974e-fab1-3b1f-be80-1836d0d78a2d | -10.61053 | -55.41305 | 2025-08-24 00:50:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 1bdf1a0d-09ca-34ed-a682-0e112b99a38b | -8.76741 | -49.97955 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| cef49265-f34c-356f-b150-5ad81b64d4c6 | -12.73462 | -48.13413 | 2025-08-24 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6bdc2aca-06b0-3f3d-ae1b-2dee36f55701 | -7.02035 | -44.64078 | 2025-08-24 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| bba92030-5bdd-377d-bfc5-832c53e9908d | -15.32347 | -56.16253 | 2025-08-24 00:50:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 97eea79d-cc18-3da2-9eb3-4a109d613a4b | -11.53887 | -51.91279 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 97aad6b5-728f-333f-8444-eaf179bf949f | -8.76595 | -49.96951 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e661859d-f5f1-301a-9ccc-f60d841d88ab | -11.53146 | -51.85881 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b8a0ff52-0a0d-3578-b126-8634385a78e1 | -8.51135 | -48.87048 | 2025-08-24 00:50:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7d74b802-e551-3ca7-81bd-dcfd93433e9d | -6.61317 | -48.0573 | 2025-08-24 00:50:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 27d2d715-423c-3185-9bd8-46a7138c4e71 | -5.7931 | -59.23128 | 2025-08-24 00:50:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a2fec73f-28e5-3125-a1a3-2bbffcf75d21 | -9.15082 | -59.48291 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 450ae1af-c5b3-34d0-be8b-9ef1f021ba3e | -9.18741 | -59.62007 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 1818f7fd-3068-3785-8105-1c6d26bf91a3 | -6.68492 | -58.85372 | 2025-08-24 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 399a18c9-2934-33ac-8b59-03b636cde889 | -6.87124 | -59.81817 | 2025-08-24 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| e5f2f449-baf5-3ca7-8fd8-610f14e4613d | -5.4226 | -60.17882 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 303.0 |
| 0a1e04ac-e594-3525-83b7-2a5d8dbac207 | -13.46714 | -47.01625 | 2025-08-24 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c5fb7f7a-4e75-3905-8303-bb872cef049e | -10.80326 | -46.40229 | 2025-08-24 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| fa550f0f-b4b3-3a8b-9149-ac6dde4d58d6 | -9.1983 | -59.47073 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 4e12f18f-89f2-35d3-a27f-1d86c1576c31 | -9.16179 | -59.45723 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 285.4 |
| f4c47201-024e-379f-8e73-78f4ba2c0d84 | -11.83137 | -55.22338 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 10f0ea21-dc5f-3eea-bd32-2807ebaf100a | -4.93665 | -55.81387 | 2025-08-24 00:50:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd2b6cbf-c19c-3624-8869-d0d9cbb483aa | -5.41507 | -45.0007 | 2025-08-24 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 1f860f8b-20f0-3f04-9971-e03b6553b09e | -3.78639 | -47.57801 | 2025-08-24 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 06221945-6193-3f8c-8e91-11758c98e534 | -9.14789 | -59.45898 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| e83f7fc7-cef3-3128-8c6a-cfa3344403c9 | -11.54773 | -51.91151 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| fe059d81-7e80-3c45-b6dc-fd8ada2e76e0 | -11.33066 | -47.8647 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 041d9485-78b7-34ce-9c09-9df7ce1477e4 | -11.54649 | -51.90251 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 69e0d323-248b-3b33-b2a1-d43d067d913f | -8.70398 | -51.14382 | 2025-08-24 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0ee66cfd-db6f-3901-a4f7-92f32da0bc0a | -13.37652 | -54.39218 | 2025-08-24 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d294765e-16a6-3ab8-97cf-923cc005a60f | -5.42823 | -60.17163 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 404.4 |
| 0e5954d7-7fd3-3479-ac52-dc347066bffe | -6.57672 | -59.8747 | 2025-08-24 00:50:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f1bc4307-326c-341d-ae6a-c92d1f70d9ce | -8.76436 | -46.75667 | 2025-08-24 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 3971114d-ee30-38ca-a413-aa52a309cb85 | -5.806 | -59.22945 | 2025-08-24 00:50:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 43df7e33-14dc-365f-9860-0585ca4062d5 | -8.89905 | -47.33033 | 2025-08-24 00:50:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 39834f03-5817-3318-9d40-03adfefe5ef3 | -6.26943 | -53.65046 | 2025-08-24 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 20f0bbcd-d5ee-3d75-9dde-1d5c6d876ea3 | -6.61111 | -48.04314 | 2025-08-24 00:50:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6b0ae968-2a58-341f-985c-91977718aac0 | -10.59448 | -50.17656 | 2025-08-24 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| c0c5fba7-6f0f-3d38-bf06-ea43bb0d6540 | -9.16207 | -59.52414 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 029e913c-721e-358c-b2eb-8898bd242e38 | -5.66637 | -45.15455 | 2025-08-24 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| da6193ac-2880-3caf-84fe-0d534bd9d7dc | -11.52385 | -51.86909 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 22808eca-16c8-38dc-b76f-bfe7ea6ce470 | -11.53126 | -51.92308 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 1578b5cf-c7db-33c1-9f12-482e0a8c421d | -12.99175 | -45.22638 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 3d3a7df4-7613-377f-a2dd-8f97a79a4db4 | -9.83023 | -47.76889 | 2025-08-24 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 566170a3-2ddf-3d64-b345-26921ec2dede | -5.43119 | -60.19529 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 99ed0628-ce2c-34a6-87cf-e89b4453de45 | -6.18261 | -45.43369 | 2025-08-24 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 1ecb8e03-626a-363d-9fa2-142c731b9f0c | -12.99489 | -45.22001 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0cbff809-fba6-3bb2-8fed-9193aa0463c4 | -8.90501 | -62.4398 | 2025-08-24 00:50:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| a00e5c5f-fabe-3ad1-9700-e380f51ca5a0 | -10.79561 | -46.4095 | 2025-08-24 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 926cdc48-af8c-39ab-a1f9-dcd82ee49b49 | -6.42529 | -53.37747 | 2025-08-24 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a70d050c-0d88-34dd-a7f6-7c3f98ecd183 | -14.32781 | -53.08208 | 2025-08-24 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8fbefdb6-05fe-36a8-bf35-5f365d614376 | -5.43648 | -60.17703 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 17c34d17-8784-30a6-b3d1-524ef890a4a4 | -14.82096 | -55.97319 | 2025-08-24 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5e8f9d58-d90b-35ed-a2e1-3076c29fd732 | -11.82975 | -55.21075 | 2025-08-24 00:50:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 1e5576f0-ac07-39fc-aa87-770adae040e5 | -14.0404 | -54.07804 | 2025-08-24 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 698df3b1-e716-31d1-adb1-b88700642397 | -8.61982 | -62.60925 | 2025-08-24 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| aed031d5-71dd-3880-8fd1-18da50f57632 | -10.40755 | -47.18368 | 2025-08-24 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3781d980-aefe-3927-bac4-f4f4885ba137 | -12.05047 | -50.36716 | 2025-08-24 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 19bb78bc-cbb6-34c4-a02f-d7c9ae92c1ce | -9.16772 | -59.50517 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 19c58c3d-8e8c-353d-a713-316046cb3c75 | -5.45035 | -60.17524 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 0e6f82dc-1cd9-34d9-a31e-462a1cc9a4a0 | -8.85937 | -52.04827 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| abca6dbc-ec2f-30c9-81e6-a2a6e31830ff | -14.55174 | -49.11356 | 2025-08-24 00:50:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| de3eb8af-2a6c-3f75-9f81-8ce212b7ca8e | -5.85154 | -52.09194 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b9692fab-e47e-3eb7-b4e8-67cfc7e13fee | -8.51309 | -48.88211 | 2025-08-24 00:50:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3e46371f-b270-3d02-b4e6-1ab840751a23 | -5.85028 | -52.08297 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 02a4f0ce-ef4c-3f0c-ad62-270232bec8ac | -4.30821 | -48.09602 | 2025-08-24 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 1fee5eba-660a-37cd-98c0-b2bcba4ad74e | -5.76022 | -53.76739 | 2025-08-24 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 03ef2386-5b99-370a-8da7-ea34f73eaa2a | -14.59543 | -54.85522 | 2025-08-24 00:50:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3204473a-0e24-3283-82b8-7a8d6c7ab1ee | -4.01886 | -49.50923 | 2025-08-24 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b16a05bf-89a3-3bd0-ae7d-4af79a419e0e | -12.99793 | -45.23816 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 99918776-d859-38db-bd67-75f2d6388307 | -9.16475 | -59.48115 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 291.1 |
| 9a7464ee-21cd-300f-94c9-27ed83ba1f55 | -4.48548 | -47.66404 | 2025-08-24 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d9195d4d-fda6-369d-9905-4d28e74a1e3d | -9.13821 | -60.77499 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 619a0377-df75-3d81-8016-38b1a71cc3e1 | -14.32916 | -53.09229 | 2025-08-24 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c8953c29-0463-3978-88f2-ace33f59fbde | -8.71164 | -51.13338 | 2025-08-24 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e13d107c-fd3b-3183-9a63-73b01f41dd0e | -5.45899 | -60.19166 | 2025-08-24 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 27a9a57c-88be-3738-bed7-3e1724472327 | -10.81215 | -46.3834 | 2025-08-24 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 54104089-d42b-3121-9692-a261b45b670e | -3.7915 | -47.57125 | 2025-08-24 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8ab14c9c-5658-3e69-a671-06412d6eef17 | -14.79689 | -59.62487 | 2025-08-24 00:50:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 99797c21-ee71-3422-ab4a-25d6363d9cfb | -5.41277 | -45.00661 | 2025-08-24 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c17d60ef-802f-38f6-ac4d-b1552263d1d9 | -3.78393 | -47.56076 | 2025-08-24 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 9ff832e8-0113-38f7-a2c7-56c0da7d5dc5 | -9.17044 | -59.47416 | 2025-08-24 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 209.2 |


[Clique aqui para ver as próximas entradas](README11.md)
