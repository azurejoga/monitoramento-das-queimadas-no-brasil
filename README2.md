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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ba2b55d-5d75-329a-9801-772b46768dc3 | -13.2974 | -54.390202 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5505cf5a-e1af-310c-a156-71d5d7e365f5 | -5.7874 | -43.782902 | 2026-07-08 00:27:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a83bafa1-6d83-3eee-8254-ba798e0f155b | -13.2991 | -54.397999 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca91d8ac-8e86-318c-99d7-cef4add2f445 | -9.7397 | -49.033401 | 2026-07-08 00:27:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e91a4b0-f298-366b-8b5b-43700b4c4bfb | -13.3431 | -54.3638 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47dddb23-a37b-3228-b5bc-f1eda3cc5f57 | -16.7213 | -50.702702 | 2026-07-08 00:27:00 | METOP-B | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a74e8041-2014-3d14-b3c5-8cd5616536cf | -7.4055 | -49.772202 | 2026-07-08 00:27:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9e41d7-1b57-361c-96ef-5006ae42f809 | -11.9159 | -55.8997 | 2026-07-08 00:27:00 | METOP-B | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85a74b63-f229-3d74-90ae-5e2934814330 | -6.8439 | -50.639099 | 2026-07-08 00:27:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38f5de16-cd47-3554-9443-4850b20af207 | -9.2335 | -50.132301 | 2026-07-08 00:27:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71455f1d-1de6-3d3f-9a1e-343a0f5ebe4f | -6.4329 | -55.792 | 2026-07-08 00:27:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd412a5-7579-3529-be13-c87cb1417895 | -8.5928 | -47.987598 | 2026-07-08 00:27:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6a06b86-4bf5-38a4-bfaf-38d8cfa9a579 | -17.2799 | -50.020699 | 2026-07-08 00:27:00 | METOP-B | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5bfb50d-6fab-3e38-bc04-a1679e0ccd93 | -6.4908 | -42.219799 | 2026-07-08 00:27:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ff06ab45-6370-3a82-b15c-3f44138165ec | -13.5406 | -49.295502 | 2026-07-08 00:27:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2cd249-f355-3a4d-bdb3-aff5b7bf4d5f | -17.115101 | -49.9762 | 2026-07-08 00:27:00 | METOP-B | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b80f205a-ff28-3f79-92ea-994d56919335 | -12.4975 | -48.2481 | 2026-07-08 00:27:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82918de3-8ef1-38da-b3b4-06e07ee31a3f | -7.4034 | -49.7635 | 2026-07-08 00:27:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86cf1794-d8c3-3e64-b6b0-6ed5533a1a63 | -13.2689 | -45.1521 | 2026-07-08 00:27:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9699fb6-62cb-332c-9201-0e523ab22ac2 | -21.0543 | -47.2472 | 2026-07-08 00:27:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 25e36c0f-e3ee-3e25-aad7-d5f1a3af7ebb | -6.4837 | -42.1917 | 2026-07-08 00:27:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2142e0ce-c095-3537-b0ea-bd1863280024 | -5.3266 | -44.7015 | 2026-07-08 00:27:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94548756-2f87-3e5c-a06f-fa603855c369 | -13.335 | -54.373699 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 838973ed-60d9-3577-8962-9924409706d5 | -8.0708 | -45.582901 | 2026-07-08 00:27:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a79b2752-8bc0-373c-92c2-1ef402720006 | -13.5397 | -52.942001 | 2026-07-08 00:27:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8600f12b-c68b-3667-bb4e-7db3d226ddee | -21.3671 | -49.155201 | 2026-07-08 00:27:00 | METOP-B | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb38955a-76a3-3f04-9e5c-cd468569d5ee | -14.5995 | -52.051201 | 2026-07-08 00:27:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5893095d-effb-329c-838d-9f8f2aee5d8e | -21.0641 | -47.244598 | 2026-07-08 00:27:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bb5a1897-492b-3457-b49a-ef50d463e78e | -13.4749 | -49.902 | 2026-07-08 00:27:00 | METOP-B | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7799d42e-d25e-3291-a792-10029a6b91d4 | -12.359 | -47.413799 | 2026-07-08 00:27:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2784814-fe10-3758-aba8-639154a5545c | -15.086 | -49.455101 | 2026-07-08 00:27:00 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d96d1e26-504d-3753-8946-54dc2d533936 | -12.1263 | -48.252102 | 2026-07-08 00:27:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a7c9343-ff47-3f7f-8334-bb82754cd051 | -13.9477 | -45.217602 | 2026-07-08 00:27:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f827019c-bc97-326c-97dc-2c288152778d | -19.659 | -50.855 | 2026-07-08 00:27:00 | METOP-B | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 034c6b94-a10e-3d3e-98ec-120b2f74240a | -9.3117 | -51.906601 | 2026-07-08 00:27:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81fa18f0-8042-34c7-80b2-960aada42713 | -10.4887 | -54.790798 | 2026-07-08 00:27:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 931f04e1-3c0b-333a-ad5a-31083a7d0ded | -14.1433 | -52.880501 | 2026-07-08 00:27:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0cb8754-4be2-3bf8-8a39-59f7a7df6bd8 | -21.066099 | -47.252998 | 2026-07-08 00:27:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c12ac9ba-3325-36d9-bed9-c30827fdb7da | -12.7432 | -44.465401 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a37e6c8-c1a6-30a8-a769-c79999b05524 | -13.3333 | -54.365898 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9c0dc24-1291-3e47-8eda-5885153c1ec2 | -12.7449 | -44.431702 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51bf1078-47f8-39d2-b304-96b488b51a4e | -12.1285 | -48.261299 | 2026-07-08 00:27:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e99e66f-d39f-36c6-ac4d-54576adcd792 | -14.1531 | -52.878201 | 2026-07-08 00:27:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96bff1e6-1c91-3c48-9636-062a567621ef | -21.8004 | -56.262798 | 2026-07-08 00:27:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 782ed2b7-8c66-320c-b367-58acddc74a81 | -9.2175 | -48.572399 | 2026-07-08 00:27:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e1bdead-2ac6-3bcb-83f4-5a4aff243f9e | -13.9444 | -45.2043 | 2026-07-08 00:27:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be8254e6-4152-3045-a93c-4e74008baf51 | -9.3019 | -51.908901 | 2026-07-08 00:27:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f93f8ba-5f73-33f8-b3f4-9961771e4633 | -22.287001 | -46.852501 | 2026-07-08 00:27:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3df92c82-a0a4-3db4-9ad3-3495b8e92b28 | -12.7392 | -44.449902 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 038c3c04-e98a-3e6a-942b-3d8031dfa9dc | -21.412399 | -47.052502 | 2026-07-08 00:27:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0dfaca28-dcc6-3fe7-b6bb-2df2c7ba6c01 | -21.795799 | -56.237099 | 2026-07-08 00:27:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5200b4f1-0e61-30a1-bec5-6b103a642c8d | -18.0839 | -54.0107 | 2026-07-08 00:27:00 | METOP-B | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9491b207-f99b-37a8-96bc-11ada14ec208 | -12.1383 | -48.2589 | 2026-07-08 00:27:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38c98ec2-dfdf-38a8-a03c-c84e95fda96e | -5.6484 | -44.299801 | 2026-07-08 00:27:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afd61c8b-1ee9-3b23-babc-cc11ff2c6ab0 | -9.3708 | -44.721298 | 2026-07-08 00:27:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c7c839f5-c637-352e-91f4-c6e39ee3c84c | -8.3744 | -48.239201 | 2026-07-08 00:27:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d873eb65-f081-3a55-b70f-fd9b7fded023 | -9.2272 | -48.57 | 2026-07-08 00:27:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 797b24da-74e5-3956-be53-399222872cce | -18.2404 | -54.584599 | 2026-07-08 00:27:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 32005b28-4eb6-3fd8-a6c3-bcdd14657c0c | -5.793 | -43.805401 | 2026-07-08 00:27:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc2536a3-592f-3ff6-a9e5-3249ab790b4a | -9.3133 | -51.9137 | 2026-07-08 00:27:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1747529-f14c-3fee-8454-76f2127d1a0b | -13.2876 | -54.3923 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc01c66c-2853-3489-a8a9-1a9c4262d7a8 | -14.1417 | -52.873299 | 2026-07-08 00:27:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2922e379-a624-33e6-9f2a-0fe92e4f3426 | -16.570101 | -49.396599 | 2026-07-08 00:27:00 | METOP-B | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1037daef-d39d-3785-b01c-303dcd409ba9 | -9.3636 | -48.7967 | 2026-07-08 00:27:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4698b864-975e-354b-811d-913e250df725 | -19.619699 | -47.572701 | 2026-07-08 00:27:00 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e4a99dbf-555d-3874-a1bf-35df24003059 | -5.6535 | -44.320599 | 2026-07-08 00:27:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54471ce8-a431-3476-b0f7-801e06ae200e | -21.7981 | -56.25 | 2026-07-08 00:27:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 62b312d6-aa91-37e8-af49-d66ade29cf4e | -9.2198 | -48.582001 | 2026-07-08 00:27:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5862d06a-2a0d-32a7-be0e-bf67593b2e4e | -12.7489 | -44.4473 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0739664c-5560-3756-aae6-db0deb94692c | -20.962099 | -48.638699 | 2026-07-08 00:27:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4273a0e-86ba-3198-a62e-e2ee285aded4 | -12.3492 | -47.416199 | 2026-07-08 00:27:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa955a6a-dd8d-329c-9f55-1275916fb990 | -20.9603 | -48.6311 | 2026-07-08 00:27:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95dfe1f5-56a2-3b8a-b743-b571e6df679d | -9.2353 | -50.140202 | 2026-07-08 00:27:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8412534c-8893-3047-8572-88b5bcfd68dd | -8.3719 | -48.228802 | 2026-07-08 00:27:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4651f785-9a90-32f1-9a20-079743149924 | -6.937 | -43.7076 | 2026-07-08 00:27:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c8bc503-4153-3bad-90ff-6673a010b9eb | -12.8474 | -44.387699 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5aec03d1-444a-3960-b273-dde626d39162 | -9.7355 | -49.015499 | 2026-07-08 00:27:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a1f8bf9-4490-3cf4-8738-d97aa673e7df | -14.1515 | -52.870998 | 2026-07-08 00:27:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b98821c5-a57a-342a-9eb4-3b95fcc871ce | -8.5979 | -48.008701 | 2026-07-08 00:27:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46df400c-5a23-38be-bb32-3a5312a30dc3 | -8.067 | -45.567299 | 2026-07-08 00:27:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4a6c81a-c14e-30c7-85ec-a672184e3f4f | -8.1122 | -47.875801 | 2026-07-08 00:27:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c1981a6-cceb-370b-8c4d-91aed00915cd | -7.6355 | -50.006302 | 2026-07-08 00:27:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a48358d6-86fc-3eb5-910c-34e799e277f2 | -21.808399 | -52.703499 | 2026-07-08 00:27:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 66d3fc33-6952-391f-bea1-6c460c52021b | -6.9026 | -43.6931 | 2026-07-08 00:27:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 758f698b-eafe-35d1-9a5d-d46a4b8bbdaa | -9.2295 | -48.579601 | 2026-07-08 00:27:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1917ae63-093a-3636-a7f0-85141963b7bf | -15.0824 | -49.439701 | 2026-07-08 00:27:00 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e51bf843-cd6c-35df-bc70-af0628aa6c4e | -6.9081 | -43.714901 | 2026-07-08 00:27:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01f7e558-ac35-35f0-8d47-56750afd1d65 | -12.7529 | -44.462898 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fd960cc-1029-35d3-94ce-8391873f9ad1 | -7.2933 | -46.234798 | 2026-07-08 00:27:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c59b5a2-d2ac-3c53-a460-1bb959a4d95c | -12.1361 | -48.249699 | 2026-07-08 00:27:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44da809b-85a8-3ff3-a003-83657b797f76 | -9.7376 | -49.024502 | 2026-07-08 00:27:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 122baac6-2044-3bba-8369-164909f81995 | -17.278299 | -50.013401 | 2026-07-08 00:27:00 | METOP-B | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 483825be-d40e-3929-ad27-4f8eb0848151 | -12.7353 | -44.434299 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b2d2610-87f7-3866-b763-795f8c2b3085 | -16.5718 | -49.404202 | 2026-07-08 00:27:00 | METOP-B | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c58df567-0fe4-3709-9dfc-48b96189848e | -13.5283 | -52.937099 | 2026-07-08 00:27:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7623ef15-fe7e-37ee-b9d1-c6adb5e969b9 | -12.3467 | -47.405899 | 2026-07-08 00:27:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7dd8a19-7b82-387d-adcc-073367229488 | -5.6632 | -44.318199 | 2026-07-08 00:27:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 755d9a2a-751d-3ae4-9eb0-d9ca042291e4 | -9.2152 | -48.562801 | 2026-07-08 00:27:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0c4636-04bb-3d70-855f-24eaeaf82422 | -6.9177 | -43.712502 | 2026-07-08 00:27:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 42f451b0-b95b-3691-bafc-b7ec19de3883 | -6.8457 | -50.647099 | 2026-07-08 00:27:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
