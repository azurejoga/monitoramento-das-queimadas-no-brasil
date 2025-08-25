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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e661c0f-6d06-3543-850d-ae61be2d91f2 | -3.42962 | -49.04703 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5372f230-48e0-337e-bc5f-7b54ef2ebe0c | -6.19012 | -44.13664 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d576c90b-5ec0-33d0-8431-9c99265dffb9 | -2.99475 | -49.10371 | 2025-08-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6d3b4ec-5a77-3509-8915-b4dd0837d770 | -6.20345 | -44.13865 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fe90f6e-5aa9-331a-a8f9-c7ea991a6028 | -6.38138 | -43.2674 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d650b920-fd3b-3019-9429-10a92117ae20 | -7.29527 | -44.52927 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93d5cab7-7944-322c-8957-84df3901879d | -6.04913 | -44.38144 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5476e27-412f-3f88-a8b2-6479e9cb5e03 | -6.52917 | -44.42519 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8c89f7c-284b-3c69-babf-9cf9ffecdc55 | -8.12754 | -47.13145 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c68672f-fcbc-3c85-b54c-6e55efb7be69 | -7.81547 | -46.88655 | 2025-08-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 779d6ba1-c2a8-32d7-a8b0-09be5264d2e6 | -6.69967 | -44.01333 | 2025-08-25 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f3e5275-b19e-36f7-bf27-bc42c0265052 | -8.17637 | -45.06523 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a4ad010-375a-3d80-bd7a-7ff70b462631 | -7.66705 | -45.39577 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2b9fb07-9e84-3684-bab7-6f39eec041f9 | -8.06044 | -49.68421 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 9b419a6f-f0e8-3924-9d42-a56564e5c2ad | -5.55331 | -45.56407 | 2025-08-25 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a181aebb-3023-33c7-bc75-4df27f5e572b | -5.74851 | -51.70398 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 991b115f-ef35-3811-9273-e3e69a8fc702 | -6.91121 | -44.41731 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9003999c-dafb-3129-b3b9-81f02174c32f | -5.48646 | -41.40998 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 781bf66a-3030-3ea1-a88a-3789be51a1c3 | -6.12891 | -44.3976 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72e3dd3e-7acf-3e00-a756-85f3fb1e24a8 | -6.01763 | -44.15228 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b38a3d6-134e-3a1e-97cd-46aa030b5bd3 | -7.9076 | -45.88503 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7daca8c1-6472-3290-ad8f-99754405ac55 | -5.50227 | -41.41983 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a75dcc75-60d8-3549-a46f-a84b4f14fed0 | -8.13392 | -47.29819 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3be5a67a-1654-31d5-9021-3e74a2b90d6a | -6.99184 | -44.16732 | 2025-08-25 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79c866c4-c521-3dc8-b56e-0255d704b3df | -6.88968 | -47.93044 | 2025-08-25 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 824110d8-b00c-33f8-9edd-7aeb16599f9f | -6.1638 | -43.00667 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c82ddda-0e7f-3b64-b7cd-3f02c88799c3 | -6.8835 | -45.66013 | 2025-08-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac0832e4-95d9-3f88-94e3-dd76d62937e3 | -6.27176 | -43.68542 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae7ec784-9769-383d-86e1-d2a40f646afd | -7.28809 | -44.46658 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3461b5f-67e2-3618-b842-4beeac91298a | -6.90526 | -47.93301 | 2025-08-25 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a9eb08a-f732-324c-bd30-99cb176f159e | -8.12877 | -47.30643 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61eaa860-5f3a-3d2a-bb83-01a97648e9ac | -5.11436 | -43.21156 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cfce9a9d-59b1-3517-9a8e-3dfbb9cb9254 | -6.30054 | -43.76102 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3aba1bc-0b70-3e03-9327-ffeaead00332 | -6.52805 | -44.43222 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7d39d0b2-0b95-32e9-a1d1-61db2751910b | -5.85886 | -51.75144 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc3a5b31-f48c-3c90-95fa-610202eb15c2 | -9.52797 | -40.30991 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6e250e0d-936a-3876-b097-16600045db15 | -5.65692 | -45.1395 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e22954ca-6d82-357c-b769-cec7043f060a | -5.73011 | -46.15603 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4dcde29-4ce9-3ee1-b5b7-866ff49b1ac4 | -6.27507 | -43.68593 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93bc336e-8314-38cc-84c3-f6415e060170 | -14.37501 | -51.93258 | 2025-08-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de9a5bba-fb3b-3cd8-9dae-29ac2b223ccc | -16.44686 | -49.97199 | 2025-08-25 04:17:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f833ab2-7330-3cd7-a269-a7a2b0803248 | -12.99359 | -45.21946 | 2025-08-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f436e763-3075-3fd5-acaa-2b08e166fad0 | -15.65038 | -52.72751 | 2025-08-25 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16db3150-e03a-3d2c-844d-6d3e171d1bf5 | -9.47564 | -57.82536 | 2025-08-25 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e0ed1a09-7f39-33ba-9906-f59144c8fa82 | -11.17381 | -55.03375 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a811f3ab-af1d-3e94-a96e-7dc8ad805016 | -11.59566 | -46.36663 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94ef4b79-4845-3bf8-b2d3-e92be1eb0343 | -14.92722 | -45.53291 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30dcc9c8-0565-3108-bc1e-b8bf2a66a399 | -13.44088 | -46.92467 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dfc7060-5fa3-39ed-84a8-2f3d4c4faa38 | -10.61102 | -55.0548 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5209d2bb-3826-34e4-959d-74b6659c93ad | -12.02619 | -49.70793 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40b0f115-e2ea-32e9-add0-841171679700 | -20.27166 | -46.64984 | 2025-08-25 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b58d0661-73a8-3f1e-8e0f-b1167776fbd7 | -14.11005 | -53.99337 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1364533e-bd88-318d-b0e7-fee77e94aa99 | -9.8156 | -45.94915 | 2025-08-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 603ccb65-8e80-3724-8a61-39f52b2a9f80 | -11.6411 | -46.2199 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b01b553e-7028-35c4-bb20-3cf3d4b675c3 | -20.61463 | -45.02713 | 2025-08-25 04:17:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| a2f49bb2-5cd1-3994-8089-97015b5afdc2 | -11.05201 | -49.12342 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16206ac9-d4ac-38b3-8c82-12d04205522a | -13.44559 | -46.91732 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c719b95-f839-36f8-afcd-5768fbeb5ac3 | -11.91295 | -47.12386 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da072c07-aed5-3e49-843d-8487b58e8c24 | -14.72254 | -55.93645 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ae90f0a-b898-3556-ad43-728954c0752f | -20.50976 | -45.99044 | 2025-08-25 04:17:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fd266a4-70ce-3577-a45d-33f1bbd1825a | -15.09268 | -48.71364 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 195d2416-50f5-3ce9-a5eb-da708362161e | -13.51112 | -48.15942 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf740977-1762-3c01-89a0-a3478ffcee38 | -10.72655 | -47.11346 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47b5e384-df88-3706-8780-80c7a250ad60 | -10.78011 | -46.39127 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed959c43-a9e5-3841-afac-0d1781410e32 | -11.09634 | -44.78238 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c888dc9c-befa-3a9a-9662-6318da5682d7 | -10.71673 | -47.1285 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ad943a7-a66c-36ed-9a37-35d301c59067 | -15.12343 | -48.64273 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c93af05-85cf-3e22-bf1e-11e9ff4c2b25 | -10.83659 | -46.40919 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 852e7848-71bd-30a2-9c51-c569252cce78 | -9.84107 | -45.96484 | 2025-08-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b0b7620-2fc2-32d1-b6af-da8afc1f6782 | -11.14602 | -44.74722 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6dd5bac-047a-3d02-bad1-01ec0f9d774d | -22.6887 | -47.34763 | 2025-08-25 04:17:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 30bccec2-e860-3d7f-b30b-ff643235b2be | -15.03722 | -48.16181 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d19cab3-b631-35f0-a66d-209e6a9ce500 | -12.9987 | -56.89719 | 2025-08-25 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 594da8e7-10cc-3dc5-9062-23fd0e2a125b | -13.44233 | -47.02365 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cad08976-a310-3fa5-90f7-5f86a2ce56b8 | -20.7302 | -49.42208 | 2025-08-25 04:17:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58f2367f-2b9f-379b-b2ca-8e3da8ed4623 | -20.36787 | -46.77262 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35143c58-4ef3-36f9-b263-56e6bc48165e | -19.73441 | -49.01399 | 2025-08-25 04:17:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddee02b8-713b-3ff4-86f1-a8d052b9b54a | -13.44576 | -47.02429 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f9e332c-54b2-35ed-8e50-26b8a88fa48a | -13.44358 | -46.88665 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d5720fe-505a-329a-bb82-f16c94487810 | -14.92335 | -45.53592 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a7bbbfe-97b4-30ac-bce6-e702565e8561 | -11.27812 | -44.96656 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0b3f9fe-e5d0-3d85-9da8-df7202fef7a5 | -13.50612 | -46.91248 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6c49511-8861-3621-b9c1-0dcc18d8a5f1 | -19.56656 | -49.44186 | 2025-08-25 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0656b30e-b390-35ec-854a-75af379a6e8e | -15.07252 | -48.65667 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21119e9b-81ac-36fb-8303-44b4e315688a | -20.27555 | -46.64675 | 2025-08-25 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 125a9a03-78ca-32d3-8aa2-3a2c9de36399 | -11.47065 | -55.47285 | 2025-08-25 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 30836bd1-7084-3b7b-9af2-4d0f4e9c41ef | -13.40434 | -47.52381 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64662049-5949-32ce-8b6d-ba7e5bffeb00 | -12.29921 | -49.14188 | 2025-08-25 04:17:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5606c25-e3d3-385d-ba5d-89bdd401d506 | -14.11971 | -53.99854 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51454715-1e71-3b86-b37a-8d72e430b2c0 | -12.20192 | -47.21686 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b059b4de-0e9c-3d5a-89e8-39308e9ac686 | -10.61676 | -55.05648 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 590769a5-d7db-32ed-a758-193773d35321 | -16.79786 | -47.58625 | 2025-08-25 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4df46f0d-a1fe-350a-94ca-68a2af53ec52 | -13.38038 | -54.39336 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42aebdbc-c9e8-3555-8746-84c868483983 | -19.56731 | -49.43754 | 2025-08-25 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c685378b-f603-305a-9930-50d1361b7ef2 | -9.46957 | -57.83075 | 2025-08-25 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7c3daadd-35c8-314e-bf44-9eaa78f04a3b | -14.78984 | -45.38937 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7eab360f-ab20-3356-8b91-26a5497d10fc | -13.44763 | -46.8834 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c12c582-7663-3bdd-921c-7bf406023651 | -19.94878 | -47.47627 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a25e16fe-983d-31fc-8d05-f6f8451a6757 | -11.46118 | -55.47075 | 2025-08-25 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c9f913ee-8795-3a2a-a2d2-dfaec248873e | -12.40829 | -47.78823 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README28.md)
