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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b80f9e35-0c52-3061-bca9-8daced10d950 | -6.65829 | -41.39728 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eba69511-6bd6-3598-8161-0c7f77fb3b36 | -5.85585 | -45.94479 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77278fb9-caf3-3209-8048-aa0118ce40ae | -6.39745 | -42.89383 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f4231c2f-3423-3e83-8ad1-231a1020a1ee | -6.69554 | -44.55481 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da79c8c4-40a4-3c9f-8128-5d7eacc3025b | -6.50665 | -44.24856 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bffbd52-558c-3a3a-ac42-20867144c084 | -4.90207 | -43.46523 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a5ea1e38-7199-33f1-82ff-e7ae4d3914f2 | -6.25358 | -43.63036 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 868769aa-4000-3001-a3ee-ecb87f3204e5 | -6.07616 | -42.61705 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 83b5910f-bb60-324f-b95a-0a5856cbb8c7 | -4.398 | -44.08846 | 2025-09-30 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56f52d8a-3229-31ca-a767-8e25b95a5152 | -5.52546 | -43.87327 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a8c6316c-abef-3d0c-ae81-b3d8afd2ca3c | -4.67742 | -43.2577 | 2025-09-30 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b53c466c-8a77-320c-807f-5c5a8dff2c05 | -5.74585 | -42.68306 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 56178ce9-df1d-3dcc-a5b6-eea38fb28093 | -6.50038 | -44.26324 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1436fd78-5026-3fba-8947-8871dce722d3 | -6.37537 | -45.62913 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9badd5c-3752-3fba-b3fe-97c754117d26 | -4.87205 | -48.88272 | 2025-09-30 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c7753c83-3770-3262-8693-d4a3833effb0 | -2.55401 | -48.40607 | 2025-09-30 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11e2db57-c9d0-3208-bc79-ee9ac634c747 | -6.25702 | -43.63363 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5492baa4-06ad-3dfe-9319-5100804587ec | -0.0973 | -51.27575 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9099a525-9b30-3e52-b7c9-48b1ef2d0c45 | -6.43089 | -43.07163 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb4d86ac-1436-3ced-9cc7-ef707e28b754 | -2.3058 | -48.142 | 2025-09-30 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 892bc561-5a9b-3794-aa74-7332df4c8a53 | -5.91317 | -43.70663 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e1ee330-1c41-340e-af6c-a61cc6a39ca2 | -3.27937 | -50.03144 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9983c021-186a-3f77-bdff-f13feb04c9d7 | -6.79267 | -44.08645 | 2025-09-30 04:38:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3d9ba8f-b44c-3107-806f-ba0233e50592 | -3.60634 | -41.37713 | 2025-09-30 04:38:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ce7a32a5-f0f7-3091-b4a9-8f4305aa88f1 | -5.98428 | -43.60756 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6ec7748-307d-3137-b84c-d2190f3fa588 | -3.80378 | -51.1348 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 548f7b27-d7f1-3b0c-8940-031c57fc314d | -4.48445 | -47.67513 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb9c2e6c-a9a0-3f15-b082-57343f31e17a | -6.83964 | -44.83626 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c3b6a955-3323-3c2b-a041-0046866aa763 | -4.38291 | -48.06858 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1228152a-9363-3c3f-8245-dd628ae83da9 | -3.05465 | -48.70892 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 498d2cc5-7990-32ff-99e2-0876b5f31fe6 | -1.29007 | -54.17691 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ee0895-5a5a-3456-ba52-09a7ec98ca7c | -4.40505 | -44.39066 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 519f1685-c922-37fd-be66-eaeb0091d1a5 | -5.08815 | -48.45625 | 2025-09-30 04:38:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a614684a-e2a8-37be-968d-a089e007c13c | -3.85435 | -48.9721 | 2025-09-30 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 763049c6-d8dc-3ceb-b9a1-b017cf3079cd | -6.83952 | -44.83236 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3e89c3e8-4259-3848-9ff3-e75b308208e7 | -5.97073 | -44.12621 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff365583-c476-3b6c-b409-ffbd70e08b2e | -5.27861 | -43.16555 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 885a8449-7989-3bee-91d7-8b53ce9f13f1 | -6.68743 | -42.79387 | 2025-09-30 04:38:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b009d387-635e-3b72-8207-b4dc394cc5e7 | -5.09308 | -47.47981 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 450505b1-e8e8-3a7d-87a8-208b99090b67 | -5.73425 | -42.68281 | 2025-09-30 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3070779b-f0fe-3f8e-9e9f-49fdba3d892b | -5.81663 | -42.86531 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fba19a78-85ce-3abd-9699-6b4849c84ae9 | -6.16989 | -44.15853 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0edc3a26-d8d8-3bfa-8d4e-f7b395e673ed | -5.77227 | -43.398 | 2025-09-30 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff057f13-63b9-3306-a68b-622cb7258d63 | -4.64824 | -47.95837 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75ca3594-1d0c-355e-a40f-cd4177d8933e | -5.181 | -41.24397 | 2025-09-30 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9cbac67d-0b96-3309-9904-b8f9b6029c2b | -4.24043 | -48.1538 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 193709fd-54cb-3ca0-bd0b-ec5cfeb9bd97 | -6.25759 | -43.62957 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4070c9a-39c8-38a3-ab73-aeee926953b9 | -5.02503 | -42.98706 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f40695f7-9732-3745-b994-57d232d1a864 | -5.50342 | -42.73718 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8c9c69eb-9e5e-3af4-b651-f0d15f49939f | -2.07091 | -56.87466 | 2025-09-30 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54211279-fb34-3ffd-9210-c5af062a1797 | -3.81363 | -47.56837 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdc9e50c-29b4-3374-b2e9-07b3537add51 | -4.40375 | -44.39805 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04109bca-c2c4-3baf-85f4-7f2553d6d937 | -6.43025 | -43.07332 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a642f6d4-20e3-3862-bfe4-391d6e03d87f | -6.37095 | -45.6331 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c2fc9b4-da0b-3b93-bd0d-b21c9ccafc35 | -6.50562 | -44.11759 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 656e325e-4cc9-320e-a9b0-24e91fac3054 | -6.51964 | -45.23412 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df2a4f18-0041-3e7d-a026-e6dd89ffa401 | -5.52436 | -43.88075 | 2025-09-30 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| d5777541-0ba7-31f5-a808-2064d3520b9c | -3.88399 | -42.51229 | 2025-09-30 04:38:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91ffda7f-ed8f-3ea9-b69a-8f5a321e9d93 | -3.81308 | -47.57193 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dbaea1f3-3e8f-32b9-a7ef-3a2167f9e130 | -4.39588 | -44.39688 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb9c9c4b-3fd7-3fe9-accd-aa1a1149b66e | -4.40055 | -44.39246 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e74b2e-89e3-3a14-a596-92be58dda88c | -3.10156 | -47.01088 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f87c889c-4550-3519-88fd-962d9cf46258 | -2.25421 | -47.88702 | 2025-09-30 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8a0d34f-8fbd-3882-a96a-44aef14cdb42 | -4.63305 | -50.78584 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79d9a8e1-0681-3f2e-b332-89bce46361be | -5.71255 | -42.86994 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5c2e976b-c894-3216-b3a6-bcc6383e958a | -5.24916 | -43.74589 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6ef87f22-c7d7-3883-b7ce-ae36c9e455bb | -3.09817 | -47.01036 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7c4e0ff8-f370-366a-9f19-accbacc50d2e | -5.23279 | -56.01458 | 2025-09-30 04:38:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16118b4c-ac74-32cd-a17f-368f8547420d | -3.35461 | -49.7913 | 2025-09-30 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6978f95c-4d2a-3dea-973e-859d398c7cb5 | -6.05421 | -43.21718 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 227e45f5-edc5-3f07-85f8-a0538274e82c | -5.92849 | -42.90813 | 2025-09-30 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2492ff0e-37c7-34c4-bac9-743bd14f395e | -6.07945 | -44.06417 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e69ad0a-97f2-3fe6-9d9c-fdc8ece9e360 | -6.31056 | -43.47187 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f60f3626-f107-3a81-a623-1b4ae7317615 | -6.43467 | -43.07665 | 2025-09-30 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df27ce47-75da-3e07-85d7-cc0ed40e3d08 | -3.36776 | -49.75051 | 2025-09-30 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 209d4369-3949-328e-b76c-0a1c3cad9497 | -6.11144 | -43.44516 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c90aa46-c1dd-3384-b10c-5b60cd32c12f | -4.89786 | -43.46459 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 56ae14ce-0e54-3f09-9c50-a499dd492b29 | -4.25646 | -48.55345 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3d6796d-c399-348d-9a1b-2a2f1138d916 | -5.51832 | -43.86435 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66910cd4-2039-3ae4-af1e-53d374ca9d2f | -6.15775 | -43.90193 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3a06422-c822-31e0-8bce-43c959abf436 | -5.15084 | -46.41787 | 2025-09-30 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d01ecab6-996c-33c5-9304-3c2ec2408cd9 | -6.36958 | -45.64215 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc5b14a4-0520-34dd-98b3-d5231b534a7e | -7.04176 | -43.23336 | 2025-09-30 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f8eeb655-d25e-37d8-a6e1-a64c44bf2bd6 | -6.47071 | -44.21126 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 180e8021-0d90-3026-bad9-86d6b0a67d00 | -5.5073 | -42.73037 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 89105133-da68-3cec-a7ba-011b05c2e909 | -2.96269 | -48.59995 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4cb4780-7c0d-394d-a856-f2e51c234493 | -6.08259 | -42.47012 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2d4919d4-78b5-3ce8-a98b-c9022e01ca02 | -2.99241 | -49.27911 | 2025-09-30 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dae56b1-f276-33d5-9314-cce5913e7f79 | -2.49081 | -49.26765 | 2025-09-30 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e27022-3066-35db-9390-0d6ffe34690d | -6.1572 | -43.9057 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae9013dc-3ab1-3138-87dc-85427fd4a172 | -4.40011 | -44.07434 | 2025-09-30 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01070172-e64e-38cb-a14a-7fe910c9c547 | -5.91029 | -49.42334 | 2025-09-30 04:38:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf07540-5bc2-3342-be76-b2f7c28b7f5b | -5.04001 | -43.61114 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c24259f0-6f9e-3f7e-ab26-7802b616a826 | -6.70006 | -44.55194 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26d4c5f4-d57a-336e-a3b9-5a84fb9a9c5c | -5.51364 | -43.86745 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd204152-f7f1-3f8f-b452-2c6a69202d35 | -6.15357 | -43.90137 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bbf5407-ae22-30e0-a10b-656b9b837cc4 | -6.56074 | -43.41843 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 57a94666-4985-3f4d-b1fa-c76bed818250 | -6.90357 | -44.52721 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28cbf2ab-9c45-331a-8db0-007f7076f23e | -3.54888 | -50.32864 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e924db5c-c81d-32a7-b94f-16d61ecfbc78 | -6.27518 | -44.06945 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README49.md)
