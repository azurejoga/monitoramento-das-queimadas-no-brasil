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
| eeff8331-6469-35c5-86bf-3bd958611c61 | -7.04242 | -59.21581 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77cba232-e4dd-3669-b0c6-6cc33b877561 | -6.37142 | -54.95134 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4067108-690b-3bbf-8991-8d6f4f1a5047 | -8.13438 | -54.94139 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b16c1a84-6302-32fb-b20c-9c9075dabc84 | -6.23992 | -55.39734 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea02b93-60d8-3d14-9097-a44f7a75c67b | -7.08396 | -56.51482 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0d192aad-24c6-33c9-a364-c6c9fdf42e4a | -5.24915 | -55.91286 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdda7f17-d303-34fb-9838-f2a3d6a30772 | -9.01983 | -65.44611 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95aa041b-3a01-3588-b11e-ff68e4d761db | -6.25109 | -55.48448 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69041c84-4f58-38d4-9134-f6d5eb5d1bea | -5.97424 | -53.58789 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5a136c8-431c-349d-9240-1fe2d666b965 | -7.05152 | -59.21967 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e49d3c1-7b66-3eea-b6e5-cc4b1fab9f5a | -3.1218 | -61.2251 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f001d17-257b-3c4e-ac28-4658f997dd5b | -8.43006 | -54.73792 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 957d8568-8e8b-380d-b444-4b1ce818a915 | -6.4873 | -53.6091 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2557bac-c44c-37b2-8b34-ea03263fa014 | -10.31835 | -49.94772 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21428a6f-7970-30be-8ee9-e777f6fece16 | -7.19906 | -60.66265 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d23845a2-fd52-3f59-abab-28ab80469af2 | -10.89138 | -45.31186 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61c98462-c4a3-34c1-89ee-273c47fbca1d | -10.32142 | -49.95278 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 878978d7-ad34-37a0-a3ae-6c6121b5b93c | -10.34006 | -49.95555 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d249fef3-bb97-369e-9809-ab2cd8775e85 | -5.20881 | -60.03228 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 88fce7db-642a-30c1-96a3-a1a027fd2259 | -7.04677 | -59.21662 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f5ed0be-57e0-390a-8912-0528bfdf555b | -6.64736 | -59.44146 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fbf77782-b386-3cca-ac88-5290bb1b3e7b | -5.9748 | -53.58439 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6c2f6d2-6253-3960-b01c-ef97431ba3aa | -9.62674 | -54.30987 | 2026-09-03 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33e0fb51-019f-306b-84c0-ba117fdeeba1 | -6.25204 | -55.41159 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d07668c-3539-3baf-8cd5-410d4d353e05 | -6.6437 | -59.43601 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03ae110e-b3cb-3a43-9043-a42cd5edd29c | -6.1154 | -59.96312 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 001bafd4-1a35-3258-b5fa-664eea6eb2d9 | -8.49026 | -44.74571 | 2026-09-03 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dc297a8-380e-31af-899b-9a46bb7f8885 | -8.45471 | -54.64928 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f8bd19e-c1ec-33f6-9b01-d752d3e54ab7 | -8.45297 | -54.66007 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ecc1fb-bff0-3666-8967-17d04db8c321 | -8.07184 | -50.9617 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7976a25a-080e-3731-a1fa-acb9824c676d | -10.18159 | -50.27101 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebb80178-029b-3f97-9bc7-262debca08c0 | -7.455 | -61.37429 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad73b670-4fa4-3234-92e9-c579908e0664 | -7.54889 | -61.31159 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1f68536-c6f2-3b03-a8b9-f7ec0af45a19 | -5.82699 | -47.03719 | 2026-09-03 04:57:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fcf1cb6-fb74-3280-acc2-7f1a4b43a03d | -7.03879 | -59.21077 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bfc3466-2151-3e7e-858b-128c33a83d9e | -7.34337 | -55.20993 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7592f06b-b909-32bf-b5cb-9ddd7ad7a0eb | -5.56213 | -60.17784 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72da3023-bb7b-32b5-b4e2-00d5eaf74d65 | -6.76071 | -56.33751 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86885624-b866-39d9-9e6a-181bc03fbd26 | -12.09401 | -47.06704 | 2026-09-03 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a09f18e4-f790-3758-95c5-ce197e049f5f | -6.06685 | -53.66789 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c8d3a7c-503f-3b1b-a1bd-9057c0a9a536 | -6.0454 | -53.80169 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e59e6d34-4cac-3b7d-9705-d1e71bd0a8b4 | -10.56909 | -47.71684 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da97008e-225b-389e-923c-8c1c8ba3e8fc | -11.33943 | -50.5457 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| dfd0f02c-9cc2-3445-a204-4ce48f4ddaef | -7.08336 | -56.51326 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2db73396-2e3e-3bf6-9026-d2e6684d4ee9 | -6.48786 | -53.6056 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39c8237e-9445-35e3-920b-866a1a40d7ae | -11.33641 | -50.54082 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f60be8dc-d54b-37dd-8aa1-926881ae5856 | -8.47096 | -54.65559 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b6cc2f6-02aa-3950-9026-7d555b12b8a1 | -11.29809 | -50.52178 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 832930ee-4427-311d-81af-78ff7940d13e | -6.31953 | -54.75479 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2fff29c-da87-3f64-b14b-25af5a5449f7 | -11.29312 | -45.14721 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c12ae09d-fbd6-348b-a4a1-bcd2e530b5fc | -3.75542 | -59.31909 | 2026-09-03 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0140ac8-da1e-3954-900e-b416d6671d40 | -4.97077 | -55.85014 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ce33153-e8e7-3d85-8ad1-505383aa87cf | -4.47075 | -55.40295 | 2026-09-03 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27874f1f-a650-3167-8aee-2215b19db6e4 | -6.04931 | -53.79872 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bbc7e26-a4c4-398a-8f5d-80cbed139cf4 | -6.32342 | -56.05751 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fb17feac-6bcb-31a7-9612-0691e2944099 | -9.63007 | -54.31041 | 2026-09-03 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d46e4f16-1999-37a2-9e68-69d3b23c9dc0 | -6.32014 | -54.75106 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36e2631f-1d7a-3ee7-aaa8-ed5564bb7907 | -5.45982 | -60.05786 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8bf1f5e1-bf76-3027-bda4-17c51f2de451 | -7.27391 | -61.11591 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9ed6647-475f-3d49-b521-37aba934bebb | -11.29351 | -45.14412 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd0e8263-4431-37d7-b69e-40caea9ac6d6 | -6.6227 | -55.24613 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3172917e-6e0b-33ef-bba1-b28782dd2090 | -8.7021 | -52.36191 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c68a5764-0388-3209-9f41-4152c1e368c4 | -6.63153 | -55.23568 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c94b8677-bb13-3590-ac20-6887a844ba2c | -5.5884 | -61.477 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ea17675-45ef-3a55-aa55-4c2d610f9131 | -11.31164 | -45.12609 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6aadd6b-3294-381a-b041-b816fd3eac33 | -9.09106 | -53.04206 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed1b1b4c-2b5f-3225-b5e1-3eb90488b434 | -9.83004 | -59.47537 | 2026-09-03 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7e1dc97-fa82-3690-bfbb-43eac432ee25 | -11.31637 | -50.52454 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| de938885-88e2-35fe-acac-219374aeac71 | -3.54919 | -58.68496 | 2026-09-03 04:57:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56e482bc-5fa9-3e3e-8888-2c7f0b9c0c07 | -8.47265 | -54.65597 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2df17e21-d8a6-3a28-9acb-32c740a74c30 | -10.98264 | -50.48402 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cb60f3b-e650-3336-b754-0ab3ff10c3d6 | -3.38003 | -59.4253 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cde5c4a6-6303-373e-947a-eeb673f51621 | -5.98287 | -55.7085 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81c9b9bb-dcfa-3039-a894-04fcc23d5764 | -6.87483 | -56.505 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2be779a4-f506-3199-9cf8-8aaac55d75b7 | -7.2924 | -60.71991 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4e3d8799-91d1-379a-8f50-d65700547cdc | -7.11914 | -42.22741 | 2026-09-03 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bb99f5cb-7288-3efd-a4e7-309fb9d2b00a | -7.50855 | -60.77787 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad4f270-0f23-391b-bc14-b226c6a3836a | -6.31465 | -56.04303 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ddb3487c-a1f5-3f6d-a5e3-0b1c65fe53b8 | -7.28712 | -52.35569 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc4d34e-056d-3f70-80f8-f31ef3233a51 | -4.09784 | -60.66281 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48a41d16-185f-3f27-92b9-d691a74637db | -5.55245 | -60.23492 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dea42aaa-6fbb-3b6c-913d-7bb5fe07943b | -6.06629 | -53.67141 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa8f0250-6edf-3954-8a62-a8379e650b47 | -6.62805 | -55.2351 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57095f77-0dc3-3a20-9671-ad9c0e17160b | -3.12069 | -61.23175 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df98d448-cfbe-3a58-9b6c-f7cc7b4d4384 | -8.08897 | -50.95582 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a44807de-db38-3a77-b7f0-08cbcc856ab8 | -6.3205 | -56.05267 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c2507393-71ff-3861-a6df-347d30a5313e | -6.31687 | -56.05207 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b2a42f89-5e6a-3e5d-895b-217e1252556a | -10.87564 | -45.31316 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d83ab795-ea4f-342d-b380-394a4f0aa7da | -8.70599 | -52.35889 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4e1d392-7009-3b49-8b0d-a66e3cef9036 | -6.75508 | -59.44455 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b922920f-32e0-3dd3-b142-25265f7afaa3 | -6.13189 | -55.63946 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a23191ba-53ae-3127-b8e5-2da40ee60a55 | -8.45807 | -54.64983 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 23426082-e632-3582-b0a8-69196e27beb9 | -8.71877 | -52.36462 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbc5da9f-a881-3abf-86c1-20b000206dad | -6.75659 | -59.43572 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 794d6cde-be89-3d57-8e94-adc1de9780a7 | -3.63351 | -60.54927 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4cb668d-3e86-3275-b7e6-dfa7bf1f0f17 | -6.64213 | -59.44521 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6f1ecf06-3cac-3e71-84f7-687618a1bee0 | -6.25396 | -55.39973 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b727b1d1-e320-35c7-89e0-b97f7031f3c0 | -7.35543 | -60.61261 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12df188b-d1a1-3b07-bf82-7a93e1046636 | -10.89403 | -45.33103 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c25a8ac-8198-3264-9b76-c506d4ce424e | -7.28381 | -52.35514 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README37.md)
