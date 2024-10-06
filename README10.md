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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f080dd3-099e-333c-9bd5-86c86e906636 | -16.4944 | -57.212898 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 901de130-02b3-3884-95fa-68cc4db38cb2 | -16.497299 | -57.228401 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8dae925b-707a-34b9-925e-e7fe33ded82e | -14.6708 | -48.769901 | 2024-10-06 00:46:56 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83aa7469-52b2-3541-9647-40fab74b2aeb | -14.6561 | -48.750301 | 2024-10-06 00:46:57 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2ba526e-96a8-30de-9ab0-037f6c19908a | -14.6577 | -48.757599 | 2024-10-06 00:46:57 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f988dc5-846e-3585-9aac-412cb84b7d2a | -16.385 | -57.3311 | 2024-10-06 00:46:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52652461-9fc0-3384-bc7b-af4b08598081 | -14.5485 | -48.776001 | 2024-10-06 00:46:58 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 818e010b-723f-3dc3-8458-bf83a66d3d3c | -14.5501 | -48.783298 | 2024-10-06 00:46:58 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e77424b6-338b-3f2c-8dc9-c550a65db903 | -14.5518 | -48.7906 | 2024-10-06 00:46:58 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea7e354-dd73-3488-978e-159cd3b622f3 | -14.5534 | -48.797901 | 2024-10-06 00:46:58 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b10eecd1-d1ed-33cf-8260-4488de958691 | -14.5551 | -48.805199 | 2024-10-06 00:46:58 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 137cbe24-4593-3458-9f30-fb80903bc0ea | -14.5568 | -48.8125 | 2024-10-06 00:46:58 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2840f311-bcc6-3eaa-b527-6dc885b98320 | -14.5584 | -48.819801 | 2024-10-06 00:46:58 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2139582d-a229-30c7-aceb-1bedf2ed8648 | -15.0466 | -51.2104 | 2024-10-06 00:46:59 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ff7ed1d-155e-3df9-812c-9bf04c4ab40f | -14.547 | -48.8148 | 2024-10-06 00:46:59 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c8fc854b-b9bd-3688-82be-c82e705a4172 | -15.0482 | -51.217701 | 2024-10-06 00:46:59 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3d642fe6-a313-3987-a4cb-e0be47ec2ef7 | -15.0497 | -51.224899 | 2024-10-06 00:46:59 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45eeb393-d932-38d9-98c5-6c6e524749a8 | -14.5387 | -48.778301 | 2024-10-06 00:46:59 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c52ba07b-a1ef-3413-bc7e-c6ca39e872ac | -14.5403 | -48.785599 | 2024-10-06 00:46:59 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd3d694-992a-3666-baa5-d182bc47f785 | -14.542 | -48.7929 | 2024-10-06 00:46:59 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ada4e8dd-51d5-3368-a35b-b9597568acd7 | -14.5436 | -48.800201 | 2024-10-06 00:46:59 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d50f8267-ffd3-3243-9468-213b66f46108 | -14.5453 | -48.807499 | 2024-10-06 00:46:59 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 80edf2ec-0ea0-305e-89c7-574e7f91c0a5 | -16.396 | -58.329899 | 2024-10-06 00:47:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3719bbcb-85d4-3d34-8960-5b9817dfce87 | -16.386299 | -58.331799 | 2024-10-06 00:47:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7b70c61-1195-3614-9931-9dc83fd8da8b | -14.4737 | -49.265598 | 2024-10-06 00:47:01 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f5dbf55b-b7d9-39a7-b62a-27cf8f10358d | -14.4721 | -49.258499 | 2024-10-06 00:47:01 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13ae0c5a-87ef-382c-ba73-27e993dcfcf1 | -14.0223 | -47.258499 | 2024-10-06 00:47:01 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 013c13e3-2174-372a-bdd4-ee02c537cf12 | -14.0243 | -47.2668 | 2024-10-06 00:47:01 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9acec5eb-ce4d-3118-a0b4-9630dd2cbbc8 | -14.5128 | -49.256302 | 2024-10-06 00:47:01 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 161e217e-e6c1-3f2c-9b25-fcba5da3c56a | -14.5144 | -49.2635 | 2024-10-06 00:47:01 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab1143a6-b19a-3f87-bc8a-17b89c54ffff | -14.503 | -49.258701 | 2024-10-06 00:47:01 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5768a9b7-3a24-3c6d-911e-f904350dc6d6 | -14.5046 | -49.2659 | 2024-10-06 00:47:01 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81ddd144-697d-3b08-8652-f7e821c4e1e2 | -14.4606 | -49.253601 | 2024-10-06 00:47:02 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd9d3452-b1ff-353b-bd0d-79d9f9e6960d | -14.4623 | -49.260799 | 2024-10-06 00:47:02 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5d75ee03-3b45-370c-9cfc-5a8affb5f49b | -15.3892 | -53.723099 | 2024-10-06 00:47:02 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ff99d67-031a-3f25-90c0-919a83c5f310 | -15.3794 | -53.725201 | 2024-10-06 00:47:02 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a1435d4-e160-3519-b228-ebc50267a3c8 | -12.2241 | -41.066299 | 2024-10-06 00:47:05 | METOP-B | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 222df818-60ac-3190-b27c-cb16eb7cb0e1 | -12.2296 | -41.087299 | 2024-10-06 00:47:05 | METOP-B | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a58a5296-5c7d-34ba-b7e2-eafd38d3e8c7 | -13.0852 | -44.695801 | 2024-10-06 00:47:06 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81696bb4-e0fd-3098-b642-473504e23a56 | -22.5061 | -55.2056 | 2024-10-06 00:47:10 | GOES-16 | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| f7443c10-2d4e-3f13-8d97-f166ba75e7ec | -13.5835 | -48.123299 | 2024-10-06 00:47:12 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f52f7a1a-10d1-3424-a599-9754f97fcef7 | -13.5853 | -48.131001 | 2024-10-06 00:47:12 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee8ad133-017a-3b0a-96b8-7318680184a8 | -13.5737 | -48.125702 | 2024-10-06 00:47:12 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44c9862b-6f2c-3508-9891-dd3bdcc83f6f | -13.5755 | -48.1334 | 2024-10-06 00:47:12 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f643cdc0-5d70-30da-b922-e905fc8be8ec | -13.086 | -46.317001 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4992c387-247b-353b-a96e-4be084945d62 | -13.0883 | -46.326401 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1891e733-a2b5-31b1-be49-2555c15ac60c | -13.0906 | -46.3358 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0971a8f-bb3c-35b2-b618-b6f13d673490 | -13.0808 | -46.338299 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b2e560f-0366-3e67-8cec-76fa4de30532 | -13.0831 | -46.347698 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a592a377-0f21-3170-8bb8-73e4593c9510 | -13.0853 | -46.357101 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec5dec2c-9968-3f5f-9c6d-ddd7ee42cd59 | -13.0875 | -46.366402 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a368c622-36f1-3ef4-a15d-e38b40d60499 | -13.0898 | -46.375801 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9793be34-5349-343e-82dc-b9a440ffb13c | -13.092 | -46.385101 | 2024-10-06 00:47:13 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f61dd5a1-7e07-37a1-9b31-a638cb1465db | -13.52 | -48.609798 | 2024-10-06 00:47:14 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 96a771cb-2482-320c-96ec-2d6d9d36aa37 | -13.5103 | -48.612099 | 2024-10-06 00:47:15 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| acb1d64f-be70-321b-8873-e86a81b5b5a5 | -13.512 | -48.619499 | 2024-10-06 00:47:15 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 996a32de-5cfa-3718-afa3-d271d441e3be | -13.5137 | -48.6269 | 2024-10-06 00:47:15 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 28f32e2a-8c53-3fe5-9f8d-e4a218f4dc81 | -13.5022 | -48.621799 | 2024-10-06 00:47:15 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 56254132-ef79-3e52-9a3c-e0b95e63a36c | -13.9166 | -50.836498 | 2024-10-06 00:47:16 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f051be85-b0ed-348d-b951-84aeed6153f3 | -13.9114 | -50.860001 | 2024-10-06 00:47:16 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 664b65d3-a6d4-37a5-ad8e-745291b69798 | -12.4919 | -45.27 | 2024-10-06 00:47:18 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3592f3ec-2ee6-3994-96bc-0f4468663b41 | -12.4946 | -45.280998 | 2024-10-06 00:47:18 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3633053-4cb3-3a9c-8b25-a508cd2f4201 | -12.4973 | -45.292 | 2024-10-06 00:47:18 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7bd9358e-be7d-3ba8-88cd-b8026281661e | -13.3304 | -49.316299 | 2024-10-06 00:47:20 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72a89a90-4be3-38ef-af91-7fdcc166309d | -13.332 | -49.323502 | 2024-10-06 00:47:20 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b858c2ba-24d7-3888-aca3-5015659e1412 | -13.6734 | -51.182301 | 2024-10-06 00:47:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2cae092d-8f9b-31f3-ac4f-331de703fb71 | -13.675 | -51.1894 | 2024-10-06 00:47:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f409f49-b8e7-31f5-b911-a1c520d80f63 | -13.6765 | -51.196499 | 2024-10-06 00:47:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5bb8d7b-393d-3a21-96be-f658dc65099f | -13.6621 | -51.177399 | 2024-10-06 00:47:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af2be794-47de-3610-af44-26819936b634 | -13.6636 | -51.184502 | 2024-10-06 00:47:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0aef0c23-bbba-37ce-9efe-157c494c61e1 | -13.6652 | -51.191601 | 2024-10-06 00:47:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b9c6dea-a299-307a-9690-5f43bd68ac1d | -13.2594 | -50.609798 | 2024-10-06 00:47:26 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77b76396-212d-3778-b124-438f5f02f114 | -13.261 | -50.616798 | 2024-10-06 00:47:26 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 791e1629-3d1b-3f37-9468-eaf90d61d147 | -12.4189 | -47.0303 | 2024-10-06 00:47:26 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 875f0a07-8aa4-3492-839d-66e3e1d55cec | -12.421 | -47.039101 | 2024-10-06 00:47:26 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 908b7e9b-98e5-3c51-9c8c-79fe016f3c1b | -12.4091 | -47.0327 | 2024-10-06 00:47:26 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 993dd505-7240-37e6-8ab3-9d8ade80dc5d | -12.4112 | -47.0415 | 2024-10-06 00:47:26 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df1087e1-943f-3508-93d6-2b032dd24a81 | -12.5041 | -47.567902 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffc543b7-4e37-3dcf-820c-15a95a5ff4b1 | -12.4905 | -47.553799 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 785b051b-e365-3621-a1ad-f200970ffe55 | -12.4925 | -47.562 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2ea518f-a1be-3696-9a5e-3f4b8537eff8 | -12.4944 | -47.570301 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 438534e1-2742-3521-8715-a67281186333 | -12.4964 | -47.578602 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 493f4b06-b029-38b9-86ff-e9a86696bbe2 | -12.4769 | -47.5396 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d59bec4-0ac3-3d11-8f23-22b1f4740767 | -12.4788 | -47.547901 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a415b24-98cb-3380-86d6-e2a012350de1 | -12.4808 | -47.556198 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72b73e91-3080-3f40-95e4-2f3e66b22e3a | -12.4827 | -47.5644 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73febfc4-b86b-355a-93e4-aa759b8502df | -12.4671 | -47.541901 | 2024-10-06 00:47:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c24cdd5-ae97-33e3-b221-13d5a1595d4d | -11.7115 | -44.490101 | 2024-10-06 00:47:28 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9fd734-e171-3e7b-812d-903a23dbef7f | -12.4496 | -47.511002 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0db0fe7e-370e-3fd8-9daa-2c41bd3ca4c4 | -12.4515 | -47.519299 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a164e939-66d4-3b59-b773-1a209d49077c | -12.4535 | -47.527699 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ad0184a-2512-3dd2-8c1c-fb1bd50407c3 | -12.4554 | -47.535999 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22d4fa65-453f-3337-b88f-138c94f95cd1 | -12.4574 | -47.5443 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3794314b-a9cb-3b5f-b321-e41e8731bb8b | -12.4398 | -47.513401 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba646650-b6e9-3b5c-8dc0-e8c9d0c252e0 | -12.4417 | -47.521702 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5f3ac64-2395-30e2-9b17-0ad79f6209dd | -12.4437 | -47.530102 | 2024-10-06 00:47:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cae3ef57-cbe6-3897-8a34-b3547e654007 | -13.2588 | -51.261398 | 2024-10-06 00:47:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1cfb2017-c627-30fb-b017-297bb29b1e77 | -13.2459 | -51.249401 | 2024-10-06 00:47:28 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aad35e7a-3cba-319e-96c7-86c8d7d862fb | -13.2475 | -51.2565 | 2024-10-06 00:47:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77a70b11-57a4-3806-adbd-b480551e5c32 | -13.249 | -51.263599 | 2024-10-06 00:47:28 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
