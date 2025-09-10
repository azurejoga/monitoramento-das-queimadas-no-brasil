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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f26cd85a-b571-3b30-be74-fecbda931fc0 | -5.81955 | -44.11895 | 2025-09-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62f1c61c-21ea-3a1a-9c89-e1d034d0448c | -8.3985 | -47.29924 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee92beaa-1d1a-3f53-939b-d1dc6642bdfd | -5.67089 | -43.8977 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01f06aa8-0827-3805-8041-9cea5ec25493 | -5.22762 | -43.68775 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5121d35c-d121-383c-a0f2-f5170b202d50 | -5.9361 | -45.95836 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9f6e94a-80f0-34bf-b47d-132754c704c0 | -7.1983 | -44.00906 | 2025-09-10 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 007fa504-77d0-3912-805a-2d4f760bed53 | -9.9336 | -46.06382 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ac60e6b-b96b-32e6-97a2-3d491c001e7d | -5.66588 | -43.34649 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4296c64d-c892-3fcb-a6f6-3b4ee34eb4c6 | -8.72177 | -50.03806 | 2025-09-10 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9af86bc1-e13e-3238-b24f-c5a43500e78f | -9.06928 | -45.71684 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4db9250e-62b9-3868-8187-6a9614d8b878 | -9.0745 | -45.70623 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c8b01a66-8a67-3cef-b855-d3aa7b8bba98 | -9.78525 | -46.00433 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45c6fea9-107e-3347-935f-d9495b4f9e6a | -1.96639 | -48.43521 | 2025-09-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b4b92d9-0399-37db-a3e9-7d1684e629e5 | -8.47988 | -47.30603 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d1a6f1a6-9aae-34f1-9616-c31694ca75ef | -6.26196 | -43.40941 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e5db296-836a-33ac-a127-24a4ffa550c8 | -7.73943 | -50.72671 | 2025-09-10 04:14:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d5a4533-94a2-3d26-8690-739056badd53 | -6.43346 | -44.04723 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cf9ceae-b256-36a5-9c83-91c5bc3394cb | -6.88622 | -47.88411 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 395922bd-bdf6-35ba-a872-4b4a785f5aae | -9.69734 | -46.75759 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cca43865-2642-3c15-bdba-264317befebc | -9.07131 | -50.47659 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2194aed7-d5c8-3770-8d91-04ed4d4b87f2 | -5.73735 | -45.28545 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 081f1fca-a0a9-3fcd-b3bf-3ffce2a5f2a6 | -5.42322 | -45.87608 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c86fabd6-4863-32b3-b88a-62a2851d53e5 | -5.4147 | -43.45147 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c693784c-d31f-3422-a1bf-0942915de5d5 | -5.84742 | -43.8574 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4363104-2ace-3517-920d-eec25340412e | -5.68173 | -45.46108 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3093799-b6f3-3d67-a921-c6559eb535fc | -9.69314 | -46.76107 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 666e7f2b-4ec5-3e43-8b3f-ccbb0e4daae0 | -6.25197 | -43.40371 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a39d4ab-237d-3048-b52f-5b78d5a4dc89 | -8.10544 | -44.85371 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36e48c76-4dff-3bd5-87b7-922b47494c79 | -5.58126 | -45.03421 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 9c3d53d6-374f-33f5-bcf4-7e8b184d782a | -8.05098 | -48.6972 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 941b09cb-1e9b-3f93-b200-f1b8ed1b297f | -6.85142 | -47.92461 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0f752e92-8d87-3c3a-9e3e-baa715eb08cc | -6.55198 | -42.9249 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cec33642-cbd0-3fef-bb22-a2528a9529ca | -9.01562 | -49.54186 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a22e7f8-c3b5-3732-8313-4c39200066f1 | -7.70882 | -45.14861 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efe991e6-c828-3f6a-bab1-0d7db4f736a4 | -5.4254 | -45.88365 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 755f0510-7713-36ee-9aed-a589cbb002fa | -6.16861 | -42.65552 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86c62f5e-ec70-309c-84d4-7fbc7e741946 | -6.18461 | -42.66156 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e22ad7e9-fc73-3cb1-b028-9d34105b9bd7 | -5.69811 | -44.28368 | 2025-09-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9bc9850-c748-3b91-9dd7-22b898eba27d | -6.9714 | -44.79702 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4227e3ac-4b9d-383e-8669-84a527362208 | -7.99923 | -46.3299 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ea2f3e5-8775-3e58-89cb-7156250b4c64 | -4.49614 | -47.82251 | 2025-09-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a8a1607-0b15-3234-a12d-855f251b1400 | -8.44996 | -47.28508 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f437e2d0-5160-33af-a9b7-ff4b897f5ea3 | -9.14931 | -45.56665 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 689eeeed-007c-3c5a-b0c6-b4869fef43bb | -7.78981 | -46.1031 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d28538f-1dca-3312-9523-f06d71554cbf | -9.56287 | -48.01159 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adf42c58-7f34-3b25-b379-2f50c231986c | -9.13516 | -45.56816 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28162602-5c6a-30c4-9701-2b77ed6b490e | -6.17469 | -42.66001 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1d17db3-5fd9-34e7-b6ff-aa661c7693fd | -7.76141 | -50.76568 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3dd62ab1-8ebc-383e-9731-34465eebc1a3 | -7.54728 | -48.24281 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2a26abd-beac-3912-9066-39e9d8124513 | -5.42022 | -43.45941 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da43468-d968-3273-b455-c8ea3f1e4479 | -5.50955 | -42.67245 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05baccad-afea-3c13-8b24-190646cbc540 | -8.69608 | -48.88854 | 2025-09-10 04:14:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9924a69b-0ea5-3efa-a452-1369de4f1633 | -7.71683 | -35.13243 | 2025-09-10 04:14:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b454fcba-42bd-3023-b3ae-eeb762db8782 | -7.98091 | -46.33129 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7104f0d-d277-36f0-be5f-0e440ed81083 | -7.19751 | -44.94023 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6616a0e7-7315-3e9c-a562-bdf9f6f61f03 | -7.70472 | -44.74221 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15e0dda8-adf8-35da-8c0c-8ec8f8ac4996 | -6.44232 | -44.05576 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba608d80-7d06-3226-bfa7-625308ef31d9 | -5.7391 | -45.27853 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a3a259c-8fcb-33eb-9767-3b47c7580aef | -8.75077 | -47.10067 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f77f6ab1-17bb-3a73-a6cc-9f370ea0659b | -9.75993 | -45.40417 | 2025-09-10 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1ed2f6d2-693f-3bbc-9950-8c15da301048 | -5.80329 | -44.85014 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c43914b5-0c7e-3714-82b7-f2a7fece867b | -5.40754 | -43.4539 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 585983aa-a046-36c6-b1cb-f9f306d6c52e | -9.03007 | -49.78398 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18d5d470-0a8b-3318-acd5-befd67d5f334 | -6.17245 | -42.65257 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2cadc97b-1bf0-37a8-94d3-85faf3665aa0 | -6.20162 | -43.29348 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a8bccfe-d060-32f5-97c6-3e33a9d1c991 | -5.82956 | -44.09897 | 2025-09-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cf91d78-1672-317d-bb6b-99b0dbc5b20e | -6.45828 | -43.58885 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0676d88-1264-323d-a046-a2a950bd42a7 | -7.54738 | -48.24587 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f768a94c-5e70-3b16-ac4c-dde4dbecb146 | -9.83325 | -46.05479 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 904e3b42-9ee3-3503-b0cc-dfc04d4182f8 | -5.74165 | -45.25898 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba1cfe53-1778-3473-8eb4-425889f0e0ff | -7.60723 | -44.6497 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c15183-7e58-3604-926e-65e75dd26765 | -8.4806 | -47.30174 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aceea204-ca3e-36ae-afbc-df544d65fca8 | -5.22544 | -43.70164 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 526952d4-03a2-3d2b-84be-00935ec670a1 | -8.04698 | -48.69642 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a82b6a9f-5374-3ad6-bf56-bcdd424dcca2 | -9.06588 | -45.71626 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9aebdc19-7437-3b46-aaff-f52dc30f0597 | -6.18899 | -43.50341 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da43dd86-9c48-3d6c-a0ac-37de19c32885 | -6.30172 | -44.92098 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 011efa59-910a-35da-a4ea-926375253dbb | -6.03469 | -43.66331 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77461626-8591-3958-985d-7b69c4711a95 | -8.21721 | -43.04136 | 2025-09-10 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d051f6b7-4002-30d2-ba46-e5910c22305e | -6.20085 | -43.40628 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e39120f-b7be-3241-a2df-e6fe13165120 | -5.9869 | -43.70553 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 239fe6af-2438-3b23-a9e5-f7de21344850 | -7.56659 | -44.65065 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e599a839-d1c6-355e-a4cc-4d04b744a183 | -5.67258 | -45.31855 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abafb666-3af6-37f9-a9e3-a9e8e9c93d96 | -6.86004 | -47.92102 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c850cd8e-1209-33af-bd98-b3c1530431af | -8.34307 | -44.83737 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| afc09b03-fac8-31cb-a20d-8a5999a4399c | -7.71199 | -44.73966 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f38cfa65-1c3f-305f-97d6-604ebfd2377f | -6.18608 | -45.80114 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ad44e7e-1ee6-302a-871a-c3d4aa7fa0a5 | -8.37426 | -45.02919 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b0c9a2e-15db-38df-a3d1-c5287d4f8d1e | -5.44046 | -45.1005 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e49c8c1-642f-3b17-9514-d46d79901e69 | -6.19493 | -42.48546 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 197f2c84-6898-3690-979b-e6d788e7e861 | -6.64519 | -51.98597 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa4727be-2b13-3271-828c-5f21eee6d4f8 | -5.73276 | -45.59934 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 673c0a2a-4e51-36ea-8e95-4ff63f627bf1 | -6.2571 | -43.72005 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0a311ff-6e31-3e0a-80f5-02a347801818 | -5.42195 | -45.88404 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 849de7d0-9157-357c-9099-803f255ba7b9 | -5.71693 | -45.41089 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e28be29a-b4ec-3842-8119-c8d1cc4d8de7 | -5.73152 | -45.60705 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e3efc1e-20f0-3dbd-b4af-e9a3b19566f2 | -8.00208 | -46.33456 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5997a53d-91bc-3ba5-9db8-300446e9a4cc | -5.4202 | -51.53549 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afb38e5c-8f27-3edd-8039-d2ed512116b7 | -6.05541 | -43.31638 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a053359b-912f-3d5e-82a7-307d1b6101c9 | -6.56762 | -43.15009 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README34.md)
