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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43529b65-ea13-3f72-894d-33fce3294ba9 | -3.69203 | -49.57525 | 2025-09-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e1fee27-59ee-3467-930e-ca4bfe1c1a6d | -3.99018 | -43.24697 | 2025-09-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c9e8af0-8a72-3bfc-92a7-a5d53d61f74b | -5.2137 | -42.88684 | 2025-09-10 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f9b96c5-7910-3d1d-8b54-2eb637255ff8 | -6.5597 | -47.48856 | 2025-09-10 04:14:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 599451f1-a685-33e4-8931-c271e99d8abe | -6.44605 | -47.02433 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74d6eb16-df36-3a9c-b4c5-62d868ac71c4 | -6.79296 | -43.45119 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ab8a6fb4-fdb3-3184-a2ea-0f2a0d012040 | -9.08689 | -47.06657 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e43057b3-faaa-3c90-9506-e8d578a9afc8 | -5.91167 | -45.79539 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cb04c09-b96a-31bb-8293-06ae930720ae | -9.31751 | -46.72692 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 208fc687-6993-3fb0-913d-cd790c54f834 | -6.3861 | -44.4547 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4008500c-a8d0-3ae9-bab1-236362387b3c | -6.25644 | -43.40149 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7279eaca-08af-3d1a-b889-8e43bbfd7058 | -7.55488 | -44.65968 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21d5ca05-8f8e-354a-8b18-f21a79415998 | -9.07329 | -45.71367 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0dffa52b-db52-3daa-a61d-545fe21757e8 | -5.92864 | -42.77721 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99eebfcc-e74c-3b23-9e59-53761881e514 | -5.65635 | -51.2686 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ecc7883-93a9-3a78-8f80-af75979887da | -5.66972 | -43.34356 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cd92c0a-3ac2-3809-aae9-8fbccaffd98d | -9.01113 | -46.0513 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ff0fc3b-3dca-3bc2-9d60-f00c19ef8fb8 | -6.05871 | -43.31689 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ee8f51d-6ce9-3639-8827-7b8e187c3c87 | -5.52108 | -42.66363 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8f8e79ea-f414-3d9a-bc2c-a2724aab1d02 | -5.86154 | -48.15947 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84c8deb5-3076-3332-b90d-6d910b1c2596 | -3.63953 | -49.20634 | 2025-09-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dc6ab07-496b-34f7-ac00-1473eec4423f | -7.27577 | -44.5713 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dcc8d92-c551-3703-845b-f83d9dfb2d9b | -8.98411 | -46.07075 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c3d91f9-69d1-3beb-a9a1-99d7425b6440 | -5.48687 | -42.66189 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b7207fd7-6061-3ece-bb42-22938174fc85 | -7.19018 | -44.94291 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbb945a-14d3-3979-900e-ac05e73eea57 | -6.05595 | -43.31294 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e9cc804f-c1b7-3c10-8be0-2d3d4c41a069 | -6.45882 | -43.5854 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fd85737-821d-34fc-8407-ee079fad4e4f | -8.18481 | -44.76439 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bef118d-d2f5-3a2d-81c2-0df4c0f449f7 | -5.57664 | -45.04111 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fbd93652-5b41-3cc8-a4eb-259151a61f84 | -9.52802 | -48.26224 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 901f946f-b685-3655-82e2-587fa50d9cf2 | -5.79549 | -43.885 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4112790-a5dd-3ed4-b822-e06efeb16c9d | -9.35537 | -46.49913 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9b4d887-777e-3928-8cdf-c22050116540 | -5.73796 | -45.28166 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e69e5fe-428c-30ab-8d0f-0e7630dbe524 | -5.6644 | -51.6346 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28b37eb7-15f5-3291-a968-a40ecf6b2f2e | -6.1989 | -43.50495 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9cdce43d-8403-3f25-852c-982eb6fe91d0 | -8.31161 | -44.82463 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc250344-64f8-34f2-97c2-f584599e3f9d | -5.68196 | -43.89227 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3979c758-c806-3d58-a2e9-3ba9e347fa0d | -6.22036 | -45.63089 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 700fd198-9b6c-3ac9-8cf9-1d6464953b9e | -8.03708 | -47.28017 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f40ad549-0c56-33bf-b026-cf1dbd7b9ae9 | -7.69822 | -47.2946 | 2025-09-10 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8068793e-3662-3df1-8b31-fd0c6b8158aa | -5.5875 | -45.03905 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 085598f9-2417-38d3-a8db-486515a159b4 | -8.03366 | -44.02133 | 2025-09-10 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2329ee4-c76e-32b5-b605-ac31935ec201 | -6.48165 | -42.41234 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 22ed5c67-4a33-3607-8257-134e5fc1b768 | -10.18087 | -44.75417 | 2025-09-10 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59acc238-44ae-30d8-9b13-a023ed0e7b74 | -6.29559 | -44.23012 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54f6f167-8da4-335a-ab23-73ec92c129da | -7.55154 | -44.65916 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bea0d8c-965d-331a-88e2-831f2b7e2612 | -8.74421 | -47.09533 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 38d8abb4-b0c6-3f0a-ad5f-3f8947e0ea5d | -7.54523 | -42.52728 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 09e99f7c-5828-302f-9b18-e0f98cac2b7d | -7.78917 | -46.107 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d714854c-4273-3a3f-9d42-4c4a29bb7000 | -3.97068 | -47.16999 | 2025-09-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d73ca0cf-9f5a-3379-a81d-a2f7a76cbf85 | -7.35894 | -44.30633 | 2025-09-10 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b834bfa1-8c2f-353d-858f-8f039b12327e | -5.91359 | -45.8281 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1919dc5d-ed4a-3158-83f6-c2ab50e2356a | -6.39558 | -42.59535 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80f9d9a8-de70-3a63-9264-816d3df817a8 | -9.80604 | -47.79512 | 2025-09-10 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 89551bc3-0306-3d55-8602-e407458a1f31 | -6.55805 | -42.92938 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b0d4c8-cc34-3a5e-a3dc-226d460c4cf2 | -7.18574 | -44.92732 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a1024d03-397f-3b01-9fc0-71c7f1a6520f | -7.58142 | -44.70391 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34b25e14-e36b-3794-9398-558c5f75172d | -5.95035 | -45.80153 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23453421-92c5-3ab7-a3a2-2ed3af652fde | -5.7385 | -45.28232 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d2b4ce5-0b73-3b0c-996d-0753fa8620ce | -6.62881 | -51.83879 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2539895d-521b-36ab-97bb-10148b23a62e | -5.7229 | -43.89152 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44361ede-018b-32be-bffc-d52ccfc63e19 | -5.66216 | -47.48884 | 2025-09-10 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb1a623c-f558-3f65-9524-b61b5e1622ed | -5.91866 | -45.75223 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c6d5cb0-b2b9-3427-8357-b8344b489ffe | -4.09479 | -41.57489 | 2025-09-10 04:14:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2bc5fe78-4128-3d48-986f-84731fd2714c | -7.2769 | -44.56425 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce9343a1-8996-35d9-ab5d-e88bb0b497ca | -6.29005 | -44.22198 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 986809d4-ad17-30d0-8218-0ec0c942c389 | -6.08905 | -44.80183 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4da12e5-0b1c-3f6d-96c3-d2e03bbf8eb7 | -9.07292 | -46.97305 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07184895-bb17-3d2e-b1be-896f509116e0 | -6.8592 | -47.92601 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d0772ff-b911-32f9-a29c-9264300401f6 | -5.12261 | -44.67229 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6f9d29e0-0d0a-3171-9956-51baed191b21 | -6.16118 | -43.37893 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36b96bc0-0edc-3156-9693-4908575e774e | -9.05638 | -50.48323 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8005a91d-08ca-3c0f-b837-e33a6a3ae003 | -9.04944 | -50.49664 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 05340c1c-4057-3ce5-89bf-6536e0dbbac1 | -7.46454 | -44.94616 | 2025-09-10 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc749922-373f-391a-92da-51add2825669 | -5.8751 | -43.98392 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71cb88d7-d78d-30a0-9ba2-ddaf62082811 | -6.85294 | -44.90004 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6839496-1192-3a47-a033-b5189f14e4c2 | -6.08907 | -43.36047 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91eabf33-604a-3490-afab-cdcc575c56c4 | -5.30043 | -43.11528 | 2025-09-10 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a659d97-eb9b-3785-91a4-ab0d94cbe7b2 | -6.30746 | -43.57206 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48b54237-f862-3dd4-8a08-bf66be5d847e | -5.87897 | -43.98093 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7495de0d-157f-3201-bddf-9a1220d034c2 | -6.68062 | -44.54909 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ce9e67c-d7e1-3692-a26b-00c3489663c8 | -5.72915 | -51.68587 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a3a9730-4999-320e-8a3d-41b937c8fa20 | -6.21178 | -45.61758 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c3f79f3-1631-39a8-8719-0dc21cda8a76 | -6.40896 | -44.48367 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50def7ca-b55f-3a08-a1b4-95d5131b29f8 | -5.88269 | -46.0865 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59a3b5ca-7f27-3751-b641-96070f1d11cb | -5.5359 | -42.65533 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| fcb0e62e-ac05-3b7e-8ef4-f66ae25c1c60 | -7.54932 | -44.65155 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60810a71-5115-3f49-9340-f35efd5c2b91 | -6.31406 | -43.5731 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d4f8ed8-78aa-3a22-a9da-341f59987ccf | -6.42135 | -44.48612 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28808b77-705d-3c0f-a9de-3b5c182c5be2 | -5.42143 | -42.8211 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35fbb584-1a6e-3654-b16f-d96f539791be | -9.21517 | -50.52857 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26581338-abd7-30fb-a2d9-7cadb0bc42c6 | -8.66747 | -36.22965 | 2025-09-10 04:14:00 | NOAA-21 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f3130b8-f0f0-3abc-bab5-534801766fbf | -5.71569 | -45.41853 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ee2991a-ef52-3e34-9abc-0af5f557ebd2 | -5.72226 | -45.39999 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf66c79d-fd06-34bb-a094-c587e0a880ef | -9.83045 | -46.05041 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6e33777-2a44-312e-8d0b-66a13380e8a9 | -7.77787 | -46.05746 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53484e1c-4feb-3989-a9b5-aa6cd9cc9173 | -3.42123 | -43.16479 | 2025-09-10 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5703a19-5c65-3e58-a59d-78160b3caf23 | -7.87353 | -46.02881 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ca6d288-1f5b-3996-9566-2a3a9b7fb7bf | -7.73791 | -50.73555 | 2025-09-10 04:14:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a4b72d8c-1a96-3265-a3b8-1c6f2e06d75c | -6.21116 | -45.62146 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README35.md)
