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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d0e0960-c01d-3001-8a09-2b6c29d80f53 | -13.40168 | -47.84293 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab467656-c01d-3ca8-89e2-236401bee788 | -10.98676 | -45.09881 | 2025-07-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3ae8f3a-64a4-31f1-ba68-148382614c3c | -12.5817 | -56.98874 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 224086d2-1124-38cd-9709-0e439679073c | -10.62062 | -48.42322 | 2025-07-04 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e70b671-5eec-39ed-9c09-a393942e27c4 | -10.55485 | -49.13675 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb4d904b-225f-3f33-a66f-eefe1fdc829e | -13.39862 | -47.8385 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69862f57-6e1c-3ff7-9751-0cc24375b787 | -10.30194 | -57.13979 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6034bbe1-afe9-3bb4-b7dd-6a55067c8931 | -11.20469 | -49.00069 | 2025-07-04 04:40:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b8da96c-4c9b-3ffb-8ceb-8a87301c328d | -11.24399 | -44.89303 | 2025-07-04 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62bd33a1-93d9-3da4-a1f6-b9062457995b | -11.9209 | -45.38849 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3402ad40-adac-383d-8432-40b2cfab20fb | -10.30272 | -57.1353 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c862bea5-a987-3e61-acb9-37545810ffb4 | -10.30464 | -57.13876 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a67c894-ad8d-322f-ad3e-af8212b5bf0e | -10.61952 | -48.07668 | 2025-07-04 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cf93afa-89b9-3e72-9f9c-cba0080c9a10 | -10.5906 | -49.46229 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 156da8a6-cd4f-3ae4-8277-738daf2abca4 | -11.86845 | -44.86432 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcd4832b-fa72-392b-b380-266f5d751a93 | -9.70339 | -56.1849 | 2025-07-04 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4ac7622-b078-33b8-8dc2-4bbc46c38031 | -10.34944 | -47.29261 | 2025-07-04 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 660439d5-4ba8-331c-ab49-7926c82a8812 | -11.85937 | -44.8673 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fa9726c-af3e-34b7-b225-183b9b222177 | -10.34584 | -47.29205 | 2025-07-04 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e0b812a-f808-3f15-9b71-e3d187adfd6c | -11.93114 | -45.4053 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56152a2c-a0ed-3ce2-b150-8907e56e0675 | -12.58315 | -56.98061 | 2025-07-04 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ad25996-1f4c-34a1-922c-9e18c3d2c619 | -11.45063 | -45.11966 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b9e9cb12-3c2a-3fa5-a5a6-2f96fceb0e42 | -16.03601 | -51.16523 | 2025-07-04 04:40:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 599a760b-5ed5-374c-82f9-44871777bdd8 | -11.93379 | -45.38642 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84f6986c-287d-3e90-902a-f75f43fd2a0b | -9.90389 | -55.52393 | 2025-07-04 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 617e0cfc-0d85-33c7-a913-38afcb5954bc | -11.32943 | -55.21805 | 2025-07-04 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dd9601c-8658-371f-89cf-93e94a83d7fa | -10.22689 | -56.76732 | 2025-07-04 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c3386ce-229c-30df-87b7-cebd5dbd195b | -11.92755 | -45.40097 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef83f74f-9ec9-3fb2-afee-d8a9e30468d8 | -11.45115 | -45.11582 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c8eebf44-c5f3-3a50-99c8-653dfdfa6980 | -9.89985 | -55.52322 | 2025-07-04 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22f7d7e3-103d-336d-b543-e11a24d8b5a3 | -10.34557 | -49.923 | 2025-07-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cf54e99-c43a-3c87-b6c3-a46661703060 | -13.43989 | -47.80968 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13a6aa3d-46d5-328a-8579-fc8fcd24bb45 | -10.66314 | -49.45158 | 2025-07-04 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2a524d7-64fe-32fc-b79f-987b2c4d9a86 | -11.46889 | -47.30014 | 2025-07-04 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ba1342e-d000-3112-aef9-71807f5f8355 | -17.65602 | -46.83127 | 2025-07-04 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9721f6ce-9788-32f6-a908-aa09475fd724 | -19.74698 | -53.99642 | 2025-07-04 04:42:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83c7a9ff-7f62-3ff8-9953-0955ef619ceb | -21.19482 | -44.93755 | 2025-07-04 04:42:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 42cd6a26-3919-3ec2-bb5c-138d9857a4ad | -22.67297 | -47.45789 | 2025-07-04 04:42:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4af14743-4967-3549-9a2d-42534d7ced3b | -18.29158 | -52.44075 | 2025-07-04 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b44453d-8878-32cb-8f7e-c5ac85dc7c50 | -19.86588 | -48.32614 | 2025-07-04 04:42:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f930f820-adb1-3307-9f3e-46e311c8a607 | -19.44574 | -48.53475 | 2025-07-04 04:42:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 775ae902-4727-3e52-9b5e-4785ef3a13c2 | -18.49611 | -45.90368 | 2025-07-04 04:42:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47916145-f8ff-3dbb-9692-44de4bd7ef7b | -20.54192 | -48.74821 | 2025-07-04 04:42:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea8011e1-a1d9-3d7c-94f8-7a4eac891114 | -19.86525 | -48.33103 | 2025-07-04 04:42:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f45e8144-4e3c-3e70-9b9b-368a00fc9f40 | -18.41273 | -55.58784 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 21bfa445-e6bc-3a65-b372-e0b4e39be869 | -22.6683 | -47.46153 | 2025-07-04 04:42:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45cfc996-c984-3f64-8008-e0e0016e9bed | -18.45456 | -51.2375 | 2025-07-04 04:42:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 761fcca8-b182-3456-8195-b5710c8468f3 | -18.14066 | -53.29791 | 2025-07-04 04:42:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e8aac1e1-3bd8-38fe-9334-ea039ce8b885 | -18.44126 | -54.66706 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 156f3b5a-21bc-3870-a214-2c4e5af2b85d | -20.44896 | -47.41088 | 2025-07-04 04:42:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc2c2f6c-6070-3b57-a756-257751c307fd | -19.44887 | -48.53991 | 2025-07-04 04:42:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cd0fa48-04f7-300b-9704-be60a3e34589 | -18.65693 | -55.73455 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a9a6d1a1-1923-3f0d-a3a1-a7fa66859653 | -18.08141 | -54.27905 | 2025-07-04 04:42:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29f07c57-8dd6-315e-addc-bf572156abaa | -18.44472 | -54.66769 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e304bcf1-dbc4-36c7-8376-8cb34c7b41ce | -19.8149 | -54.41312 | 2025-07-04 04:42:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c8e99db-ae8e-3421-82c1-12067b78e318 | -18.66697 | -55.74104 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fa2d33ac-6cca-3a37-a233-7aca23a2a4a0 | -18.44751 | -54.67228 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ae27fa7e-a387-3a13-9c22-c6f4617019d4 | -21.95418 | -57.58862 | 2025-07-04 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 134b0f07-6b39-3aa5-b094-b0c0de12e936 | -18.44338 | -54.67561 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82b55008-4c79-3697-8161-858b2f34e3ed | -19.4495 | -48.53525 | 2025-07-04 04:42:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d6022f5-cd7c-3e71-9dbf-9cd9c4bc2113 | -20.70443 | -54.89157 | 2025-07-04 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f937c531-7c59-35fb-8a8f-4caba326f56a | -21.12798 | -57.51865 | 2025-07-04 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 53caee9c-a368-3420-8575-05b5d0998e41 | -21.03808 | -56.00089 | 2025-07-04 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79c6e34a-baba-30b7-9fc0-8eb9bc583f34 | -18.65977 | -55.73963 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8b3d756e-3e67-32da-86bd-2e90d87c4ddf | -19.74239 | -54.00331 | 2025-07-04 04:42:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 544ef028-3be0-3297-be6e-85edd198e390 | -21.1291 | -57.5218 | 2025-07-04 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| faa88063-e815-3a96-9f29-c5609ff4d524 | -20.76418 | -46.76771 | 2025-07-04 04:42:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e380f7ac-ab81-32f8-b370-5284787feac9 | -18.90751 | -47.01054 | 2025-07-04 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f87c389-9a63-3600-a2a2-012da17bb612 | -20.72347 | -56.65616 | 2025-07-04 04:42:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a184c933-8cf3-3f9e-b381-2464800fdab6 | -21.8643 | -54.0227 | 2025-07-04 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 86b05917-226f-3dbc-a17b-94850a3548ee | -21.20554 | -55.70504 | 2025-07-04 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfac46c8-d190-3b7c-ae67-8c375aa9a9a0 | -18.41183 | -55.58454 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6de0c45f-ecc4-33ec-8544-3d7c6ee780f6 | -19.44511 | -48.53942 | 2025-07-04 04:42:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cefb87eb-1228-375e-85db-7e83a968269d | -18.41108 | -55.58887 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2160cdfa-6471-3bc5-92ff-83e92ad5f1fb | -22.67249 | -47.46201 | 2025-07-04 04:42:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01815aeb-09c2-3297-a7e6-2c04be4c6e97 | -21.12226 | -57.52799 | 2025-07-04 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 440a790f-d34d-3dfd-a278-2b19c64eea90 | -21.25589 | -53.26364 | 2025-07-04 04:42:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7eb87a16-a675-3412-a58a-2abed6ebe28d | -21.03956 | -55.99239 | 2025-07-04 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b06455d4-5241-329e-ad05-edea65265283 | -18.44684 | -54.67625 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb0853e6-58e2-309c-b0cc-9fff92031a15 | -19.72459 | -44.89125 | 2025-07-04 04:42:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff713f16-6c57-3d27-b775-affa1b5d5f3d | -19.74301 | -53.99956 | 2025-07-04 04:42:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 869bbd54-5e78-3059-849a-cf841c5a5f15 | -19.62836 | -48.94715 | 2025-07-04 04:42:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b960876-759a-3100-b745-49535db5411c | -22.66459 | -47.45694 | 2025-07-04 04:42:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92672f1c-7623-33d7-ab3e-cd741d5b34db | -18.91159 | -47.01117 | 2025-07-04 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5705a42-123a-3a44-984c-a2c521b1b3f6 | -18.14185 | -53.29053 | 2025-07-04 04:42:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c42440a-5903-366e-a656-65d11df9c73f | -20.72794 | -56.65232 | 2025-07-04 04:42:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb233861-a946-395f-820c-77246f0faa49 | -19.86681 | -48.32938 | 2025-07-04 04:42:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbb6b7cd-da71-3a17-8916-55e484d68228 | -18.53104 | -48.42707 | 2025-07-04 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 862eeda6-c4a1-36cc-a969-03ec147419e7 | -19.71986 | -44.89053 | 2025-07-04 04:42:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f691569-c1f1-3d34-9506-a9e6363aee2e | -19.14699 | -54.39652 | 2025-07-04 04:42:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4f6df87-8eda-3a50-b33b-c1a20b12aebf | -21.85421 | -56.74632 | 2025-07-04 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aed40cc7-bee0-3df6-9800-f0b2c8c8c97f | -18.66544 | -55.74979 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 68abcfd2-3b61-35d6-a02b-6d72919d00f2 | -18.66053 | -55.73526 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f64bb6d3-d81e-3faa-9bf0-1e9909d5156d | -18.6662 | -55.74541 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e65a7d98-c758-34aa-be9a-2d20ffeea87f | -18.44059 | -54.67101 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d9fc4b5-d572-35cf-88fe-6731db384589 | -21.04162 | -56.00159 | 2025-07-04 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 569a75d2-dc0f-390d-8d1f-56678b3e38cd | -19.81563 | -54.41179 | 2025-07-04 04:42:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42b88a5d-c1e8-3060-9394-5eafca8f853a | -23.59307 | -47.43816 | 2025-07-04 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8c52b11c-b6de-371d-ac0f-11e29f71e4b4 | -20.79085 | -55.79182 | 2025-07-04 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6540cf8-ea12-3bdf-ae4a-9bbfc75102c2 | -19.79372 | -46.30279 | 2025-07-04 04:42:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
