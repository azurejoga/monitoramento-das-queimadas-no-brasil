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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6458e9be-1752-3e07-9f2c-5e1f8211e81c | -5.70247 | -44.21635 | 2025-10-08 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2925f89e-b9b9-3113-9649-3fe416186a0f | -11.2578 | -47.61733 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a22afdbd-8b10-309f-96c7-e610bf2e882f | -7.23304 | -47.17464 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1611f6d8-49c5-3d3c-b634-21ccfbec787b | -8.68116 | -44.73222 | 2025-10-08 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8590a0c4-fcfb-39de-a2c9-79e1b72c10e0 | -8.78281 | -48.00524 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75debb89-3d03-3985-beb0-4fb20159d488 | -4.08044 | -48.04501 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ebd191b-c709-3723-9bf8-8c64f7a7fe63 | -4.08708 | -48.04605 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86e64a9b-d4c5-3951-abf8-339e929f758e | -10.4061 | -48.09844 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81700481-5b09-3e07-9d5c-c283341b519e | -7.77086 | -49.24332 | 2025-10-08 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927b21f7-c2d9-37ed-8c26-b61b808aa2aa | -10.88207 | -47.10064 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ce8d1e00-36da-30dc-9ff3-3929a26aeddf | -10.34592 | -50.25297 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28b62f0f-f28c-39dd-8da3-5dca6d7df6b1 | -9.4527 | -56.65237 | 2025-10-08 04:38:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3635602b-833d-3018-acdc-303bbcc30fad | -6.71797 | -42.86194 | 2025-10-08 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d214726b-294a-33fd-ba00-666c9fba117b | -7.79344 | -42.62684 | 2025-10-08 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8ccd373-67d9-318b-bf08-0d030367a0af | -7.59543 | -49.64514 | 2025-10-08 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29df658d-e33c-3634-8258-ca6027e6368b | -9.18886 | -47.79704 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5dfe1f6c-a964-3e5d-8a16-fbbb2bca03ed | -8.13881 | -54.87489 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a00b06c3-e994-35c1-ab31-903d1b8dc053 | -9.3048 | -47.81821 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3438efb3-cf45-3724-80f1-65a346b402be | -9.33146 | -48.94588 | 2025-10-08 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42fda5d2-bec2-3489-9a23-56973a8559a7 | -8.54031 | -55.01817 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7c13048-8990-3f18-a6e5-944a5478ae1f | -10.64154 | -47.79772 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62dfe015-2318-3295-b169-fdf1d5c9fd8e | -8.51537 | -46.28406 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99afdf43-1409-3537-8d45-e23f69506069 | -7.18748 | -49.10827 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 141de744-bd20-369a-bad7-e9331022c7f4 | -8.22219 | -44.20353 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de8aeb8c-9ec6-3fdd-9436-fe8b018d2074 | -5.64182 | -43.60681 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2bc6ba5-6fb3-3aaf-b2e3-aebde6500526 | -6.68564 | -58.81231 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5811e9d-4607-39ca-82b8-da3818c79e66 | -9.63586 | -55.13432 | 2025-10-08 04:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ced132a5-1d89-33de-bdeb-fbe8caa9f03d | -10.44164 | -49.3586 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e52d2ea-ef48-3bfe-ab7e-40c482367389 | -7.34369 | -43.86539 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c9082efa-7503-3ca8-9617-5e735b6304ee | -7.24024 | -43.98428 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20f34d74-1ff3-37b1-9a68-1e39f6cc10ab | -5.31516 | -44.99871 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8056f10-335f-357c-a36d-0055beafaf14 | -10.40645 | -50.66475 | 2025-10-08 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b040f6c5-032b-3b04-8362-ecc57896e347 | -10.47111 | -49.38864 | 2025-10-08 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd4aeb0d-95ec-3377-80d7-e2037622c711 | -9.25492 | -56.28844 | 2025-10-08 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfc83ce5-e5e4-39f5-a864-14d4f9ecfcb5 | -9.18943 | -47.81649 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce72a6a2-60df-388e-ac1c-25da754ce378 | -10.21981 | -48.17497 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53ecce01-b4ec-3fbd-9e4a-67fe936a7761 | -6.16065 | -51.16247 | 2025-10-08 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf68c855-734b-3ee3-b299-4ddf3b45c55d | -4.50194 | -46.35388 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a5be9ac8-cde7-327d-a02a-c01343bb273d | -7.7839 | -44.21879 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e74ef1bf-686a-3942-89d6-40becf16931a | -10.17845 | -45.55396 | 2025-10-08 04:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcf7fdae-a95c-3e66-965c-af9cb5d0c05f | -5.26886 | -49.51254 | 2025-10-08 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca9d7a02-4d72-3764-9dbb-6aab481b339f | -4.01699 | -48.96466 | 2025-10-08 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b850afd-ac66-35ac-b368-487cfcc376db | -5.85169 | -43.40949 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 341130d3-e5f6-3f3a-acf1-8cfa6d6bdfbc | -4.69068 | -46.46846 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b26ffca-c82f-3546-a39a-18446d8ad5e2 | -11.46511 | -43.48827 | 2025-10-08 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ed1e64b-6175-3976-8666-7b155ef809b6 | -9.60207 | -57.13677 | 2025-10-08 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94001ed0-525d-3b1a-9ada-e002f675b7a7 | -7.82243 | -44.18625 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68e637ff-9445-3745-b860-aa931be3a3a7 | -10.65295 | -48.9822 | 2025-10-08 04:38:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868e9e98-09dc-380b-b150-cbc1bd88d16f | -11.77005 | -45.13514 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7144c7ae-6d0d-31ca-958c-2034ca4bfee0 | -4.91558 | -48.02478 | 2025-10-08 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb4d7aa1-ca0e-3541-b75a-f80d43999979 | -3.91684 | -49.10424 | 2025-10-08 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 067a948d-e537-34b1-ab8a-b96073baca6c | -11.77265 | -45.14645 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d01a298e-9af5-38a1-9049-2e2de78cda0c | -7.82492 | -44.1864 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20524e6c-e4b9-3de2-a5e6-7b0c514310ba | -7.80533 | -44.24479 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0738a5a-8407-3406-95c0-086741220afb | -4.17659 | -49.80094 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a252b51-80a7-30df-837b-166f632ce0ac | -9.547 | -47.7687 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd95a72b-1ac9-3ab5-9615-161661ec3504 | -8.7902 | -48.00259 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9ba16bc-fa0f-380a-acb8-f5c4b37046c2 | -10.86727 | -47.98532 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e514e03-9c5e-3af4-b2bd-db7148582d6b | -7.78144 | -42.40962 | 2025-10-08 04:38:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9d977e4-5eae-368e-8da5-c0bc90818873 | -6.11739 | -43.88534 | 2025-10-08 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d47f51c9-8b1b-3d52-9cde-0a1c03ace3a7 | -6.11329 | -43.88463 | 2025-10-08 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e4c9944-41ce-320b-ac32-06ab3001c729 | -11.87599 | -44.93761 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f222ec7-d4f1-3bc7-afe3-43fc0e288e0a | -11.78105 | -45.05705 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 088f2294-b651-3a0c-abf9-148800985385 | -4.49608 | -46.36877 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7b56ee9e-530c-355f-b5a0-0365c6d0506d | -10.61184 | -48.67805 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c569d25-b96d-3683-b179-184fd85796aa | -5.63766 | -43.60619 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 245420e3-6b93-3140-a154-aec82beb4a9f | -5.3745 | -47.78056 | 2025-10-08 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afd4cdd6-41d4-3688-8b45-24e9c02c259e | -9.78243 | -48.28858 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 160cf338-515c-3ea6-952a-7b52929b6884 | -7.2595 | -44.11325 | 2025-10-08 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2aa8550-d6b6-3e86-b127-efa30200f81a | -9.1752 | -46.92626 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f2b852a-9ee2-3ccd-906b-f62735f237ed | -8.21992 | -44.16057 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa0bec56-dbf4-3c5b-99d7-16d8c10062f8 | -10.82431 | -49.95377 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf5f3cfa-9412-3f50-8f9a-4b6aa0b93348 | -6.28084 | -45.31451 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21e0c77d-00f2-34cd-8d40-e9b473e0c412 | -4.25682 | -48.56473 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1710e3f-9e96-3027-baf2-421b1946199e | -8.25464 | -50.09547 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cbb734d-f599-3cf7-bc45-83020aae9ef2 | -10.41961 | -44.49923 | 2025-10-08 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5dbaa57-3f38-3dae-8214-c7248eb7ace3 | -7.80505 | -44.2182 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 696c901d-e555-3ca8-86bd-1cd5ab84e12b | -3.50795 | -51.34657 | 2025-10-08 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eadbce24-9024-3675-ac8c-1e2cf34d28f1 | -6.66506 | -41.38848 | 2025-10-08 04:38:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 11762666-b9fe-31ec-8add-82ab2f1fcdcc | -6.37241 | -41.62392 | 2025-10-08 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7c86fd7e-be82-3f78-9ee1-b95b5bc6b3a7 | -7.78857 | -44.21568 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa8287b7-9824-32b4-9513-385e226e85ab | -4.68198 | -45.83651 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 539e1317-9bb9-3371-9148-0095d4b7a9c8 | -9.13632 | -50.06261 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fcfc6f7-93c7-352c-9b9f-4f80bd78ac2e | -9.67785 | -45.67151 | 2025-10-08 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08b3bcc3-00c7-3ac3-bdd0-c4fc4ed63035 | -11.81583 | -45.12978 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e194795c-02cd-38e5-bb7d-a0b6fe7b026f | -5.13009 | -44.96867 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e4ee3e93-bf76-39eb-b9a0-ca6381dc2f1f | -8.19685 | -44.11368 | 2025-10-08 04:38:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b528bce-59bb-381f-b0b0-f7a7ec6eb96a | -7.91447 | -47.13927 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 700f51e1-27fe-35ff-a21c-b39d357fe93d | -5.70712 | -45.68164 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d57afe23-099f-339c-9acf-230f03815241 | -7.47775 | -43.10671 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 884cf2ad-1a44-3ec3-a6f4-0f224e4e1e34 | -10.36081 | -50.2876 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed984759-4fd6-31f6-9b7f-a6e9b96cb943 | -11.7925 | -45.11623 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2531d8c9-b840-3c5d-9397-c86ab31f83cd | -8.474 | -46.28867 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe5cb40b-e491-3c30-85ea-287380606301 | -4.96499 | -48.0145 | 2025-10-08 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29836c11-32a4-3653-9436-db350d5210c2 | -10.08853 | -40.77993 | 2025-10-08 04:38:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61b8b752-be82-3adf-8d9f-f2af5a593822 | -5.75273 | -44.60498 | 2025-10-08 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f455eea5-402f-34bf-90c3-79a39df9b8e7 | -7.81472 | -44.18127 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2a8217ea-2ea9-3aba-ab4b-1c0301b5d896 | -11.86032 | -44.92783 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88ec16de-049c-321a-83a1-ea01b52f4747 | -10.63668 | -51.81278 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7e01cae-c69d-3ff4-bb0a-5a286f9a4544 | -11.14489 | -47.74473 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README72.md)
