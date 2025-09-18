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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b0d9372-21ca-3c1f-88ca-30636bf5eed4 | -7.8512 | -45.5879 | 2025-09-18 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 73b02cf4-0eec-3ac4-b097-13b33d20c1fa | -6.2055 | -45.1187 | 2025-09-18 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 01e1f352-00b2-3ca2-b9cd-7365ec5f9717 | -8.4134 | -45.7809 | 2025-09-18 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 32492e2c-281d-3f18-a04b-9f686f38fde4 | -6.259 | -43.4595 | 2025-09-18 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 8b7e1553-0e97-3375-afd1-62e61e62ba12 | -7.5412 | -44.7532 | 2025-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 70cf485c-d408-3179-b01a-9c0209231261 | -6.9024 | -44.7656 | 2025-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 80a5eca7-a7cd-3490-9caa-eda3f2e545f2 | -9.0671 | -44.8685 | 2025-09-18 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| b7d65676-a6eb-3fd0-ac4e-3b64e3be4f85 | -8.8801 | -46.138 | 2025-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9cd6573c-4b05-34c3-a9e3-1af19b8f0db7 | -5.6233 | -45.41 | 2025-09-18 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b874ae88-d85e-3b12-8e9e-88df84d4742d | -5.8809 | -45.8641 | 2025-09-18 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 21cc8daf-2f50-3182-bf59-f09e08037e3c | -5.8807 | -45.8865 | 2025-09-18 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 637570c4-d8cc-3a37-b845-97cef8e5033b | -6.2136 | -44.2732 | 2025-09-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e89bc99d-6151-37b4-b3f0-c10c56cfbb83 | -3.8658 | -43.1787 | 2025-09-18 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 071bfd1c-d561-3fde-8018-e34abfab3213 | -6.4779 | -45.9991 | 2025-09-18 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e3fdfea8-491d-33a7-9c9c-f1d7b91863c2 | -10.0371 | -47.1952 | 2025-09-18 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 897d21d4-21e6-3ec2-9f99-5ca3baa42186 | -5.79 | -43.4738 | 2025-09-18 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 363ddf4e-8404-3596-a4ca-2177648c96cb | -9.1709 | -46.9792 | 2025-09-18 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d1e913e9-7511-35a5-920b-6319b29cc3f7 | -6.0786 | -44.6733 | 2025-09-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0bc7693b-476c-3a1a-9ab5-73a72bf804fb | -6.5774 | -45.3837 | 2025-09-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e7988819-a8f9-369d-b01d-18c2737b6b32 | -8.3523 | -44.6487 | 2025-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 6fac388d-8223-3f85-85d1-cf3f530e6373 | -5.786 | -43.9147 | 2025-09-18 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b54027b3-efd9-3e92-afd6-44b80c9c0504 | -8.6504 | -46.4086 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c38f1e44-a757-3b8f-bdcf-ee35b674d1fb | -8.9516 | -45.019 | 2025-09-18 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 286258be-15e9-34e1-99c1-c5c323e7c454 | -7.8512 | -45.5879 | 2025-09-18 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9743c26e-f128-3d8f-9dc9-1441606b9479 | -7.2923 | -45.1639 | 2025-09-18 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 1ca97b07-2600-3f87-8a09-27e6b7d2939e | -5.8397 | -44.1872 | 2025-09-18 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 23b436cf-0266-3e36-8e29-3fe214b962c8 | -6.1878 | -41.2097 | 2025-09-18 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 9c68715f-2859-34d8-98a4-10616a366cbb | -5.2143 | -45.1888 | 2025-09-18 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 72befc3c-1b17-3f11-81c4-cdf3eb4dede1 | -8.6502 | -46.431 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 2355b427-2366-3d05-a80f-0cf2647da730 | -6.6319 | -45.56 | 2025-09-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d7706f5c-c4e3-3837-bf31-9754beeb1baa | -8.9722 | -46.3079 | 2025-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f13549df-291a-3b8c-9798-c7732cc1e828 | -8.7076 | -46.3579 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 53481fb5-b632-3126-9ca1-af9dd1c1e401 | -3.8756 | -41.6188 | 2025-09-18 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| ec86497d-b639-3b46-b16f-b64aa7a31641 | -6.921 | -44.7869 | 2025-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1b8ff0f1-6105-3906-b4c2-21e4eea1f518 | -5.8058 | -45.9142 | 2025-09-18 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 783a96e6-6ad3-39a1-bd7d-0aed8c4ad970 | -6.1196 | -46.3385 | 2025-09-18 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ad5d97fa-004a-3a16-8651-4176d8acf006 | -19.5869 | -57.7765 | 2025-09-18 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.1 |
| d0a9bde9-2365-3414-8c06-4ed837a4b39c | -6.9022 | -44.7885 | 2025-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f27e970e-7dc8-3ffd-9626-6f0821f6f8aa | -6.3967 | -42.8388 | 2025-09-18 14:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 4c2a0942-a35d-3bd3-8914-e86ba743ab4a | -4.7486 | -42.5877 | 2025-09-18 14:40:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 144.2 |
| 88b4e288-7628-3d3d-9bdf-a123e4c4bd8b | -7.5164 | -45.2796 | 2025-09-18 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6d66b83f-0ff5-3de6-80c0-45686a04ffe4 | -8.899 | -46.136 | 2025-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 32a93065-14ce-300c-8400-443063e0c740 | -5.642 | -45.4087 | 2025-09-18 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 82d72961-5809-34c9-b009-7c779991a3ea | -3.1562 | -43.2587 | 2025-09-18 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| e9f17407-c121-320a-bb3a-368342bdf854 | -8.6693 | -46.4067 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 5fc27ae9-2d11-38e0-85da-f1909d20cf56 | -6.0071 | -44.3124 | 2025-09-18 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d67779e1-7bb0-3bdc-96e3-c83e97e1bece | -3.8659 | -43.1554 | 2025-09-18 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 182.6 |
| ee71213e-28a9-3c78-a17b-8e8f8c588de3 | -6.6883 | -45.5328 | 2025-09-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| daa68dd5-99bf-3da7-b213-38bed2b0db3d | -8.6887 | -46.3599 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ec69a437-4430-39af-8c9e-207ae87797bc | -8.8054 | -46.0784 | 2025-09-18 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 6cb9a316-8e5f-328b-b32d-9dbc92a58690 | -8.0092 | -44.9589 | 2025-09-18 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1e74edc9-5640-36c4-abcd-fb9a75e2d162 | -3.2691 | -43.0674 | 2025-09-18 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 534338f1-7fc8-3640-9e41-887da637904e | -17.732 | -46.7756 | 2025-09-18 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 24d86d56-e87e-3aec-bef4-6dd3a946bacc | -5.7871 | -45.9155 | 2025-09-18 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f2f998a0-b9e4-319a-b937-2ddb70b1d982 | -8.3334 | -44.6507 | 2025-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c4b7c8b4-b540-3d61-9ef5-69ae547fc92c | -5.7858 | -43.9378 | 2025-09-18 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e6a040de-544e-3873-a103-3134c7bc24fb | -6.9212 | -44.764 | 2025-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d30e09ef-621f-3376-b2d2-60601442c3dc | -5.806 | -45.8918 | 2025-09-18 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3f6cc8c9-c073-36be-8807-86537b9c178e | -3.8566 | -41.6677 | 2025-09-18 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 6bd7f9cc-4f7e-37bb-af6b-2b8a22ea16c2 | -8.669 | -46.4291 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 336a6aec-2086-3390-97e8-1328bdca7b92 | -8.7866 | -46.0804 | 2025-09-18 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| e5720fcd-81a4-3081-8778-fe948383b360 | -8.6885 | -46.3823 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 2e84cda3-5f9a-30f6-bb7b-07313f5ffd9a | -8.5421 | -47.573 | 2025-09-18 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 20f1eb60-c8cf-3960-a592-6e1b66e5666a | -19.5865 | -57.7973 | 2025-09-18 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 143256a4-4336-35de-8515-c31184efc603 | -8.4145 | -47.2324 | 2025-09-18 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 0c6faf9a-7277-39cc-b3d5-8610674d95a9 | -5.8056 | -45.9366 | 2025-09-18 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 943452ba-af8b-318f-af52-f49b33fdbec2 | -6.0599 | -44.6747 | 2025-09-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d91f940e-2a9b-30d6-9871-34bfec1e51c4 | -8.9911 | -46.3059 | 2025-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 4e99239a-7618-3d74-9245-5f30536640ee | -19.5872 | -57.7557 | 2025-09-18 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.4 |
| a3da357e-e6fb-30e7-886b-04e74f88d8f0 | -3.2692 | -43.0441 | 2025-09-18 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 656b2a5b-19aa-3677-a07a-4198f75061f5 | -9.1901 | -46.9549 | 2025-09-18 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 91815060-a339-327a-b050-d86167540ebb | -8.5609 | -47.5712 | 2025-09-18 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c5e02c0d-4a1c-30ca-a948-f1581c1d777a | -8.5759 | -46.349 | 2025-09-18 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 522b8f87-6504-3443-bb66-2707ced3b3a7 | -4.7484 | -42.6113 | 2025-09-18 14:40:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| 355a3b7c-c16f-3109-a95e-a74446ad7873 | -3.7655 | -44.3383 | 2025-09-18 14:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 87512632-c564-3f8d-8140-a84e7100e35b | -6.9978 | -44.62 | 2025-09-18 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 88108e56-206f-3ab0-a1d1-fa3180ae392a | -7.3235 | -44.0608 | 2025-09-18 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7abb8326-61e9-3313-83f5-3105368e57c4 | -7.5084 | -44.3431 | 2025-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 19445753-b0cd-3b65-aa1c-9705e3bb201c | -3.8101 | -43.1116 | 2025-09-18 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 271.0 |


