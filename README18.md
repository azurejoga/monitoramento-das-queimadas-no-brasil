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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5db1d3ea-2289-3fb9-a02c-5e11ffb09247 | -3.08875 | -49.21381 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1bc6fe6-c4fd-3192-b522-bc4889d6af85 | -2.1783 | -46.3838 | 2024-11-26 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59206dd5-554f-3c7a-9aab-fa40f5cda1a7 | -2.40522 | -53.68279 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3ea61e6-6314-3bdc-a38d-d4ccda528544 | -1.82877 | -46.28841 | 2024-11-26 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 732f47a1-4ad9-3395-a287-840be5f3cabe | -3.76004 | -41.028 | 2024-11-26 04:14:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 91436bee-d47e-3ca7-b6be-943271fb7144 | -2.93223 | -48.01421 | 2024-11-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2abb416c-317f-3a51-9c88-bee8b93e5064 | -3.97834 | -48.0736 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 345ed285-b030-321c-b68b-8adc63b229f9 | -3.23238 | -50.31625 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a306286d-32a8-34b0-8dd3-d9713409f6ba | -3.96844 | -48.05708 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1e83e57-dbf3-3284-b07f-6de6d9886201 | -3.45793 | -50.83325 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84e7b339-13df-37aa-80ee-213717b9b1de | -1.04509 | -51.74082 | 2024-11-26 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 875ea953-da9a-39b7-a521-408ad2b7981c | -4.25921 | -48.6674 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07bbafb3-fba7-30cb-b64a-9c61916730a0 | -3.97019 | -48.04639 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adbf53e4-eda5-3859-9d13-d34f6bde9722 | -6.19277 | -44.4309 | 2024-11-26 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de45c5f5-f3e8-3a59-b459-70add4a22be3 | -5.94581 | -43.7964 | 2024-11-26 04:16:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32df5918-683d-3f7c-bb5b-ddc0f89e1f5d | -6.18929 | -43.41341 | 2024-11-26 04:16:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ec961cce-f4c6-3471-bfb9-f17be58d8296 | -6.69676 | -43.06165 | 2024-11-26 04:16:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86d5c084-f7e5-3f6b-8c8d-0a4abae858e7 | -6.08522 | -48.03527 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e1fd3bb-408c-3880-8797-90f3580e7525 | -6.11896 | -41.93407 | 2024-11-26 04:16:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 30e4dd0a-d03f-317e-b353-0583a07f2d4b | -8.05109 | -47.08427 | 2024-11-26 04:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0be8c593-9c9e-3a07-b0f7-cd5e12730567 | -5.95618 | -44.46326 | 2024-11-26 04:16:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fbcf461-b21e-3986-8ec9-49313d259744 | -6.07649 | -48.03901 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 338465f8-b40e-362f-bc89-87549aeeae19 | -5.76667 | -47.81578 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0fbf208a-f19a-37a5-a0ce-777061a4c457 | -5.47954 | -51.17337 | 2024-11-26 04:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99f66d2b-239e-322f-8203-a89c1f6ca917 | -5.47677 | -51.17021 | 2024-11-26 04:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 330fb516-32d8-3ebb-844c-6d51974c20b7 | -6.15907 | -46.81319 | 2024-11-26 04:16:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 301094fc-48f9-3b3d-95be-8c7d61191436 | -7.71558 | -37.43346 | 2024-11-26 04:16:00 | NOAA-21 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 111e0df7-c1b2-30b7-aef1-8527edf1ee1f | -6.37392 | -47.35713 | 2024-11-26 04:16:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a58e3d2c-8000-3461-b6e9-ec2a72bd0c41 | -6.18544 | -43.41635 | 2024-11-26 04:16:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31f98223-2746-33ae-9ac2-5396b162b23b | -6.44965 | -52.43887 | 2024-11-26 04:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0e87bba-fada-3952-8890-8bd8a65e0bea | -5.50408 | -47.16537 | 2024-11-26 04:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01b4ee7c-7d0a-343c-932c-8df73cf6102d | -5.75863 | -46.2555 | 2024-11-26 04:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d347b68d-cc14-3f96-8f0d-1a4eb20f1e90 | -5.85141 | -43.87757 | 2024-11-26 04:16:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad2eaeaa-59e6-317e-845d-3232e7d94f97 | -8.26494 | -49.54197 | 2024-11-26 04:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55175bd0-0dd4-37de-9a9f-dbc529239ef1 | -6.14724 | -43.70408 | 2024-11-26 04:16:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50c93abf-650b-3386-9668-21529c6957b4 | -5.98162 | -43.76289 | 2024-11-26 04:16:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37bdc8a9-fa56-3a51-b7e5-ecf48d3f9cba | -6.11037 | -46.92645 | 2024-11-26 04:16:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 865bfd3c-d10b-31ca-867a-702947c207fe | -5.48172 | -51.17097 | 2024-11-26 04:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b99e8d3-fa31-3c1a-9893-c008e7e002e3 | -7.19626 | -48.59896 | 2024-11-26 04:16:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61462b26-c431-30fb-b4a3-349e3962190b | -9.81052 | -41.52926 | 2024-11-26 04:16:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f0211466-70df-3742-896b-20e62ffd6ef5 | -5.76561 | -46.30307 | 2024-11-26 04:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f2b4e1f-6107-39fb-b75c-fb8ecb755706 | -5.94912 | -43.79691 | 2024-11-26 04:16:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6ff4d36-f7a4-3fb1-ba90-0d3a4b5bd438 | -9.42124 | -43.27202 | 2024-11-26 04:16:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aace48c3-28bf-3703-8de9-7da118092981 | -6.44858 | -52.43944 | 2024-11-26 04:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8561a445-6e73-307f-bc1a-d6590686c5c3 | -5.95283 | -44.46273 | 2024-11-26 04:16:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7446134-a082-3c76-a253-c5a53658b307 | -5.76356 | -47.81019 | 2024-11-26 04:16:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8846d7e2-d36a-3d1e-b6e7-88902578335d | -7.09316 | -45.45896 | 2024-11-26 04:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eaccea7-e3f3-3621-a927-3bfd59b4faa3 | -6.2593 | -46.91334 | 2024-11-26 04:16:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad1f457d-32f5-3320-8bf2-6a0275dec63c | -10.42118 | -49.24271 | 2024-11-26 04:16:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7aea9e0-aeec-317b-a919-9944a3375e0a | -8.26426 | -49.54591 | 2024-11-26 04:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a44f20f-9036-3297-8e40-94cb80084e64 | -6.08128 | -48.03455 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c7e2b969-0726-314f-81a7-c57a8e02b9dc | -5.12638 | -47.74347 | 2024-11-26 04:16:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 921f500b-0bcb-31d1-84e3-bbc7a4318809 | -6.07421 | -48.02811 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a8dbaeba-fa4a-3034-9674-5424f9375c81 | -6.12732 | -46.91562 | 2024-11-26 04:16:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eabb7c1-f894-3910-bd4a-49969609021f | -6.00638 | -46.54969 | 2024-11-26 04:16:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5a7a6c4-2968-3e12-a032-95ab4618fafc | -7.8587 | -46.9078 | 2024-11-26 04:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3a56fbe-4635-31e7-9640-e4a746c6a2fb | -6.14393 | -43.70356 | 2024-11-26 04:16:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7a2e18b-bfb5-38d0-9e1a-414f8b90716c | -5.73871 | -46.51374 | 2024-11-26 04:16:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98c039cc-bf42-30c8-b149-6ef9dad5fbb5 | -9.86503 | -44.11486 | 2024-11-26 04:16:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34253f7a-1bb4-3be3-9e4d-64f710d1df6a | -5.48046 | -51.1678 | 2024-11-26 04:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5462ee3a-7f07-3b04-b308-b9309c903c73 | -6.92131 | -37.10799 | 2024-11-26 04:16:00 | NOAA-21 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 826e84cf-73ff-3f18-95b8-5de5d7903f36 | -6.08439 | -48.04036 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c482d00f-5023-3817-8bb7-f9f01a86dc27 | -6.19333 | -44.42736 | 2024-11-26 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 565793de-29c7-3613-938c-eb30489d68ca | -9.19364 | -43.16039 | 2024-11-26 04:16:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3b0454de-43aa-3f80-ae3f-8707c6ef90c5 | -5.94635 | -43.79293 | 2024-11-26 04:16:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 125f6145-7a31-3477-abca-5a597882660d | -5.49767 | -47.66293 | 2024-11-26 04:16:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3050222d-c1cd-3b67-aa5e-33f3ef5c9bbb | -9.35013 | -44.644 | 2024-11-26 04:16:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 109e7481-97b3-35df-9471-e563916e40a4 | -5.23828 | -48.06107 | 2024-11-26 04:16:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0edfdf5-09e4-3249-8ef1-680f2a2fe46c | -5.65355 | -46.64584 | 2024-11-26 04:16:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e9ab446-aada-3c61-9a0e-db67bc82fee7 | -6.1266 | -46.92001 | 2024-11-26 04:16:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27f8dcbd-5d0c-329d-884b-70a919c3f270 | -5.76275 | -47.81516 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bfd1b1e3-c31e-3d05-9e72-fb44bc9f8496 | -9.44428 | -43.21063 | 2024-11-26 04:16:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20c25d4b-d775-3083-aebb-9fc275f4c6d7 | -6.07338 | -48.03322 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0ae02c4d-620f-39b5-b2fd-7cbdd3c2ab96 | -6.68688 | -48.874 | 2024-11-26 04:16:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21c13b62-5507-3586-8ef1-c3d9da3e5920 | -6.07026 | -48.02747 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2345b34c-baaf-302b-a887-8b2287d893db | -6.94334 | -42.83023 | 2024-11-26 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26f15175-2c8b-3a80-b1af-765cb9078ff3 | -9.44096 | -43.21012 | 2024-11-26 04:16:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5eaa61a1-ce1a-3ee7-adc0-b54efeb7c115 | -5.66242 | -46.24595 | 2024-11-26 04:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d83cf848-35f0-32a1-919d-7433e44ebc15 | -6.94002 | -42.82972 | 2024-11-26 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7229d487-a2ca-33d0-a2ce-4748c4441395 | -6.19612 | -44.43143 | 2024-11-26 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da1ca040-219a-31f4-aed4-e607871aaa8e | -6.94665 | -42.83074 | 2024-11-26 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2b05ef3a-7e5b-30b7-be79-0b164692f1e4 | -6.06942 | -48.03258 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2266c53c-2e4d-3946-92cb-14256d01e468 | -6.08044 | -48.03968 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 6d2d8476-b123-3570-8cab-b44be0586344 | -6.07733 | -48.03387 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 988e77a5-a920-36d0-b1ad-f9844161f18d | -5.44461 | -46.52208 | 2024-11-26 04:16:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b46c7559-b255-31ca-97b5-41f420a243d5 | -6.6392 | -47.34915 | 2024-11-26 04:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 73c52aeb-61cc-3a0a-876a-4f78696618ac | -6.63995 | -47.34456 | 2024-11-26 04:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c0ed26d9-42fa-3df5-ae61-10264be635b7 | -5.93696 | -43.7879 | 2024-11-26 04:16:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eff77213-1e2d-3e67-9e4d-67ca40ecad03 | -6.6437 | -47.34523 | 2024-11-26 04:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 34c96d23-b3ff-3883-850c-2df3251421ed | -5.79776 | -47.0774 | 2024-11-26 04:16:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c39786c-4b81-329f-b3b9-9a50734e8124 | -8.05473 | -47.08482 | 2024-11-26 04:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d67b586-edee-3dfe-8ee7-e6b9737b3b35 | -6.37014 | -47.35649 | 2024-11-26 04:16:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 18155eb9-d31d-32df-812f-3180637b0bd1 | -4.91592 | -50.59823 | 2024-11-26 04:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e77b6594-9458-3574-8054-cff265833bd5 | -9.44761 | -43.21115 | 2024-11-26 04:16:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2aa429b5-07b5-31d9-9a09-7a2a4310c03d | -5.75371 | -46.2631 | 2024-11-26 04:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c93216d8-1502-3126-a330-aba5876ae30e | -6.18598 | -43.4129 | 2024-11-26 04:16:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c2a9f6f6-341c-358f-8aef-8db3c474bfc1 | -5.76748 | -47.81081 | 2024-11-26 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2885d84a-f38c-3720-87ec-00313081d6a1 | -4.91633 | -50.59512 | 2024-11-26 04:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc55f7af-c402-3c54-9bd8-c2cf443672c0 | -18.70662 | -49.35477 | 2024-11-26 04:18:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 06cb2d89-c12b-3171-ac0d-76f1fcdd5b30 | -18.1149 | -51.16823 | 2024-11-26 04:18:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README19.md)
