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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9920a7e-7a5d-3052-acec-289970e8404b | -9.76812 | -46.61622 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb783451-7519-3330-87e9-4592aef20840 | -7.09231 | -41.84173 | 2026-09-17 05:16:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9578187e-6b9a-3143-8b31-455684f428ec | -4.3609 | -47.77995 | 2026-09-17 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c281962-ad3e-36d5-b6c6-ef9ee9f70bda | -4.13482 | -54.42109 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae6233b5-4f36-38df-8730-77e8db06dfe7 | -6.798 | -59.18182 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dc4e3c6-bdd7-3f78-92dc-911d1e8f384b | -6.75926 | -55.83994 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3474a0ad-464b-3c1d-92b6-948d95729ed5 | -6.70326 | -44.14226 | 2026-09-17 05:16:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 005ec553-b1b3-3cd1-8ec9-c7dfb9135f55 | -6.89845 | -59.02514 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 592990d0-f5f6-38dc-99a2-a2dd6f8d769d | -2.90141 | -54.17893 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62ec084a-ca9e-39ac-a074-a92bb0c9cef1 | -7.58088 | -46.33684 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a266bd5-9038-3de4-990c-3ca070029d7d | -9.62615 | -45.36516 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 782b77ab-173b-34fa-a390-22524944d014 | -6.71059 | -58.80524 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3206428c-ce79-33d3-adc9-bfcc6a90c457 | -9.62502 | -45.37411 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7cbcc535-9ce6-3288-9af2-476bf9ffa4e4 | -4.53046 | -55.66392 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2efb09d1-1d8f-3dcd-bc64-e5fe4e39355a | -9.94631 | -45.28959 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c908232-af33-3ec8-b7f8-45ae564c2200 | -8.86389 | -46.98769 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb96c554-3658-3d86-bc5c-4a36acaa26c5 | -4.45518 | -55.43579 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a74d4ca-dc76-3c96-a6d3-26485ea4916e | -7.07827 | -47.49187 | 2026-09-17 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7637285-8569-380b-97d8-e7a8fdb4b948 | -4.24197 | -54.88112 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56760e95-0729-379f-afab-9c5f765f9a90 | -5.90557 | -52.09387 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22fade14-7932-37fc-97fa-41eae5c9a975 | -9.90448 | -46.51062 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd546ec5-9f39-37d1-beb2-a2961c46a34f | -6.50243 | -58.37836 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6e56bfb-f400-32aa-9e54-d3b9dceebff1 | -6.10173 | -57.62992 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32620254-b48c-38e1-a6b8-a4158db9ac69 | -8.09238 | -61.81898 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 789796b5-43cd-3596-a9ba-9617191b2355 | -10.14654 | -45.67512 | 2026-09-17 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12b85c2b-941d-3882-8bff-3a0d48e58647 | -5.76975 | -45.09421 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dcceea19-b95f-3aa5-9f05-2d1f6808be82 | -6.80449 | -59.18649 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13c3a99e-c447-3a50-82c2-41c83e43c4ed | -10.14711 | -45.67062 | 2026-09-17 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4844a21-b9b2-3362-92c5-eb82e8079edb | -9.61618 | -45.34916 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6e1761f-1110-3663-b47f-964e1539bbae | -3.23454 | -54.32009 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 369b666c-c88a-3411-ba67-3da7754b142c | -8.85546 | -46.97893 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4ac61a0-53e8-3f16-b069-fec290904220 | -6.43982 | -58.14453 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab4e97e1-951b-315c-954b-d09608663822 | -4.37639 | -55.03355 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7a43d8a-d9d7-332e-808e-0a456ccdc516 | -8.78685 | -46.90005 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c6904e-3862-3799-905f-4246bf29f699 | -8.60833 | -44.4924 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80317199-63f6-326c-a60f-bd01a7d346fd | -3.42826 | -58.19913 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44201498-b326-32a5-abda-3e304be844bf | -5.19621 | -49.32899 | 2026-09-17 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40118885-2e69-35c7-91bc-e1a75a27a5fa | -6.71126 | -58.80115 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42f84460-8135-36c8-ab82-8dee4eac62a6 | -4.4324 | -55.78709 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 696ef121-ced0-37c2-b57f-c050a052ee57 | -7.94259 | -44.83326 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ffa9c18d-d33a-332a-9d8b-c958983af140 | -2.82084 | -51.34079 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63b7c6ee-5f79-3048-82f3-4f918cb51e94 | -2.46989 | -54.68026 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ddf221f7-7222-3998-993f-0969c6b30def | -4.52412 | -54.91456 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d104ef0-310a-3d49-b5ad-ad68efc8eb13 | -3.02758 | -51.22734 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a6f1263-2499-339a-94d4-6a3b899f5073 | -4.54701 | -42.94931 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aebf7e39-3a9c-3791-86c5-13aee292fc96 | -3.84589 | -51.76661 | 2026-09-17 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 645c33e1-e7a9-331c-9916-f581dd27913a | -9.61739 | -45.33996 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95f9991e-1ad3-3ee8-b816-332ae859fb07 | -8.55947 | -44.54979 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 71d082af-e015-3d29-bba7-6f0c15729729 | -5.30675 | -56.1005 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af202858-9f32-3636-ae8f-e00ec13f7d0a | -4.53579 | -54.92707 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e250a995-ac25-3db9-ad66-73f5173c74e5 | -5.14814 | -55.92929 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5201ddbb-4bc9-37e7-ab35-a2d7ebdb2352 | -5.92402 | -51.64499 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c0265ce-e104-3684-bd2e-610592b9b6b4 | -3.33329 | -59.82859 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9755e021-7fb0-3fef-b297-5af0453e7f58 | -9.87836 | -48.3849 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 14f9f6cd-f2a0-311d-919a-55aac8ec66c1 | -7.64816 | -44.32411 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 204f81a9-abd8-3dae-adb9-73daeeb667d2 | -10.39422 | -46.63004 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1cf8ce5-f1c8-3dfa-aa1c-1c0657dcd7df | -5.89869 | -59.93748 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35cb5982-632a-3f52-b96f-c52a11c03ce3 | -3.47822 | -54.70421 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f6f8836-01ad-34d1-a6f8-7fc8e311473c | -3.39145 | -50.44889 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de72787f-988e-397f-983b-f2ec643830d4 | -5.85546 | -52.06554 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c7d7817-57b7-3da5-b86b-e98697984c2b | -8.33341 | -51.31099 | 2026-09-17 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0952c08a-26fa-3901-b2db-66a8987255b9 | -4.18096 | -49.40506 | 2026-09-17 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc56eb7c-bc99-3bea-8207-79e6f6b44787 | -4.45131 | -55.43873 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ca9381-6e16-3148-afe7-1dd63906a348 | -5.80356 | -47.24299 | 2026-09-17 05:16:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 215c846c-40d2-36db-aee0-7aa869b58be8 | -8.85979 | -46.97721 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f833bcfa-a327-3010-887f-945e78a3dc69 | -5.14981 | -55.94023 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d61d5c57-abb4-3946-bfe8-ffa9ee6092a2 | -2.79847 | -52.08062 | 2026-09-17 05:16:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d3f80df-9fa7-389d-b1af-6201ff3f9508 | -9.10057 | -45.72432 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 5233438a-efd2-3faa-ad61-c57314d04351 | -6.83571 | -55.75938 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e81ecd86-cee8-3c69-9b00-41d4fc4aed4a | -5.15092 | -55.93328 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba5f5d78-5c9b-35b3-bfe3-985a27a20981 | -5.81832 | -52.10961 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcb77d36-a31c-3ab0-b185-c61349ee644e | -3.82366 | -55.78684 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b3b2196-9c68-3703-813c-05aadf3566b3 | -5.22541 | -49.30972 | 2026-09-17 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b6f7d29-a917-38d9-940f-d608aba17665 | -3.04757 | -51.2719 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b320cc0-1858-3789-be0e-ec28ce24d131 | -6.75871 | -55.84341 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aceb8552-72f2-3ab3-8c57-1dfeb478ec26 | -3.48656 | -54.71616 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6a275379-9b10-3938-8565-6daafc87e737 | -4.53023 | -54.91909 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40db1380-e49d-310b-a0ae-840a6dfc256f | -3.80884 | -58.89497 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d387e8c-2489-360a-b4d9-a550fe290fa1 | -1.77108 | -55.84449 | 2026-09-17 05:16:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0de9cdf3-12ea-31e8-833d-b42082d017e7 | -8.85805 | -45.86443 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86f53a7b-a44b-326f-8c0e-9bd026451c4b | -2.8749 | -51.61493 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3002aa03-5d23-3bdf-af5d-ab5a8b64002b | -7.37747 | -44.48592 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ede1cba-6982-3fe3-afb2-8e6ec7fd0f5d | -5.92977 | -51.64774 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b37a1428-55cb-34f2-b581-6ab04e9d3117 | -5.64176 | -44.80096 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e980d563-f122-3767-be0e-43278bf127ad | -6.65706 | -50.91803 | 2026-09-17 05:16:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc00061-5fdb-34d6-8a40-3177d4ccd7f5 | -6.90275 | -59.02159 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48269df7-d6ad-3a8e-a97d-ba925195c278 | -3.17417 | -48.58088 | 2026-09-17 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7fbfa279-cfa6-3cb2-95a3-f085ac8b0c53 | -9.61121 | -45.33961 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b7ca33c-bf29-30d6-8ed4-987bdc0ddfaa | -6.89777 | -59.02932 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 683b393e-25bc-3810-b689-bd92f22b3cb1 | -3.27003 | -54.26164 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7730062-5241-3528-9912-ede2f5aa683a | -8.00043 | -61.37247 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bf010e1-58d2-3a0f-b8d3-e9f7711887de | -8.43259 | -47.74955 | 2026-09-17 05:16:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dc35a8b-f796-321b-a975-4410271a9948 | -9.55869 | -46.59573 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b0437fe-de45-3291-bf64-44ea44059ca8 | -5.79888 | -47.23926 | 2026-09-17 05:16:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92910df0-13ce-32a6-96d7-024722d92117 | -9.61679 | -45.34454 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62ff279e-6f73-3fcd-8817-47fa8ea62b03 | -3.17568 | -48.58301 | 2026-09-17 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0c39764a-f285-3b8f-bd46-9250170ea991 | -4.56572 | -54.91039 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb7a133e-c374-3843-8df8-2a265b0822e7 | -6.79648 | -59.18952 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d8b6a08-c90f-376c-8344-78678b34b5bb | -5.91026 | -59.93934 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2abdb5e-aadf-35d0-884e-7e4a0b5ce889 | -8.09725 | -61.81583 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README61.md)
