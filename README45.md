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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5f167d0-b20b-3eb7-85f3-a388e5c2e1bf | -15.42032 | -46.15606 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48714241-713e-3695-afcb-8b0715589b7d | -18.19667 | -44.53704 | 2025-09-17 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ed18e17-d442-3df0-990f-2f339efb4027 | -18.21361 | -48.49274 | 2025-09-17 04:34:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 384c9812-1917-3509-b170-539fc06b8975 | -12.70243 | -47.97298 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5967c9f3-82b9-3371-94dd-a57be6217c52 | -13.18121 | -44.48144 | 2025-09-17 04:34:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e6bbb7c-8feb-3395-af10-04a4a42ffd75 | -18.35558 | -43.32035 | 2025-09-17 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 33125b5f-5580-3287-8b8d-9c815d9d0f16 | -12.09504 | -51.22351 | 2025-09-17 04:34:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf6bef40-9b0c-32d6-9b3d-ab73aac6162f | -14.97717 | -53.41181 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4da0635-2d13-3209-b3b9-8013dcd983c1 | -13.91713 | -44.96756 | 2025-09-17 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee7b57e0-38c1-3565-b0bc-617b6b98e9b9 | -12.71007 | -47.74147 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86384fde-66f5-3605-8984-288c1d0af9c3 | -12.69907 | -47.97245 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dea402a8-6428-3b57-b64d-bf16f287089b | -14.90046 | -51.70108 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef3c5ea5-f8ab-3d41-b2ea-ccab0fc72f38 | -15.39503 | -46.14708 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecfdbdd4-1f0a-32f8-a3a3-7c497bbf9ff3 | -12.38016 | -51.40871 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59d2aa40-28fc-3bc8-aef5-2dc4fa14f8aa | -14.93749 | -51.66845 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9736e374-08c7-37b1-adee-d1f0c3f20d39 | -16.61568 | -43.37516 | 2025-09-17 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d5dad50-56c7-3e69-824b-87438ed753ec | -14.91601 | -51.69206 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ebaa09b0-26c8-3a9a-a1b6-73d5da0d7ba5 | -18.52261 | -48.14839 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e72bcc52-1524-31cf-942c-36e079198f5d | -13.22293 | -47.28497 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae616ab9-1f6a-39b8-8357-3a23942e54cc | -17.33731 | -46.8102 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30767f52-a0ca-3770-b6f4-cb3252ab7f1e | -15.4086 | -46.15859 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df506c77-838e-3ce5-b824-191930dfe0b3 | -14.91134 | -51.69907 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51710b99-ff8e-39d6-b0d5-0d94d089e0a1 | -18.36324 | -43.33495 | 2025-09-17 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e8fb28b1-8dbf-3453-8149-076e956eb93f | -14.81458 | -51.69055 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49042fea-971e-381b-b183-0e24bfe9118f | -12.98826 | -47.98529 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ad1342d-22e7-35f9-90d0-121ed8126266 | -14.82977 | -51.705 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20f334cd-36b6-3d40-806e-581ac86d4c95 | -14.89767 | -51.69667 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e51c2ae-9c9e-314e-88b9-ccb08d5e61ef | -13.18346 | -47.31351 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a144b758-14e0-3e74-9712-733591f72999 | -18.3637 | -43.33106 | 2025-09-17 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3e508a42-59bd-3e28-88f1-a9877f030e03 | -10.81315 | -50.65299 | 2025-09-17 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e876353-922b-376e-b774-23622add55af | -15.00295 | -49.24752 | 2025-09-17 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef2fc19c-4453-3225-88c4-bad08c026eac | -17.33 | -46.80895 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c789c095-5990-3d54-bed8-219cf1285f03 | -12.70019 | -45.81101 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6ea2e81-fcfd-3614-8fd3-13092062d6ce | -13.03427 | -47.95489 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 465eaf1a-0eb4-3dd4-98b6-587935e05529 | -12.24587 | -46.7603 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe668bb-a624-321a-b1dc-a29102b48970 | -12.27965 | -43.83038 | 2025-09-17 04:34:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e87a358c-99c6-3bf3-af22-b4e98d60de92 | -12.06427 | -46.54946 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b7cf583-32c6-3948-9f89-95a4c9aa121c | -13.15094 | -51.62327 | 2025-09-17 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c246d7a5-6797-3637-853c-eef5777026a3 | -12.38362 | -51.40931 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75200eb5-a596-3e9e-a8cd-4a8b76b2b751 | -12.72822 | -48.00688 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34470db3-b9c5-311b-93ec-0cbdaf07ff90 | -14.80457 | -48.12119 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 282aebbe-2fbb-3bd5-b777-e87a467fbf4c | -12.06891 | -46.56643 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cef4bf3-37f3-33a4-bfb2-eba1a5ddeab5 | -16.94395 | -42.87271 | 2025-09-17 04:34:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5cf04b8-5baa-3175-a6a5-487d6325694f | -14.83571 | -51.69035 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 390c74b5-70ec-36d9-bec0-356ab0922ff9 | -15.63623 | -47.3004 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 180bc4bd-a54a-3cc4-bc5f-c1666b7c3131 | -18.17412 | -45.18494 | 2025-09-17 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 744ba09b-979b-3099-9177-44c9e726f6d7 | -14.81394 | -51.69437 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c49bc20e-c1f6-304d-9d6b-f12c4e74623c | -13.26042 | -54.19972 | 2025-09-17 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6f0aeeec-a56c-3e68-94e5-0260be3f7cd2 | -16.70464 | -54.94136 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7960dbf8-a015-32e9-948a-278260667001 | -12.74732 | -47.96151 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c77bb448-c6d9-318a-b526-4ebfbcc49769 | -18.52203 | -48.15244 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6280d8a0-85cb-38a8-bcea-d72919e61de4 | -14.78298 | -60.23378 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09f24854-66f8-373c-b816-af16ebf80948 | -12.70672 | -47.76358 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f769a24-abd2-3861-8484-c5aa3f9a0b53 | -14.0696 | -50.14878 | 2025-09-17 04:34:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94d9f9f8-54f1-30db-a2e9-49674a1dc25e | -15.02078 | -49.45867 | 2025-09-17 04:34:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f979890-f0b0-3af7-9502-f1ec623608c1 | -16.88899 | -45.78868 | 2025-09-17 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f49bb1a7-d589-3d28-8444-184763a0faa6 | -12.86393 | -47.13356 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8434d3cd-8888-30ba-91e9-9f5e8153d0f5 | -14.70329 | -50.24353 | 2025-09-17 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c9f334ae-5313-37bf-8ab0-7283cca16e25 | -12.38644 | -51.41376 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17b86df7-68e5-33eb-8c4c-920387e06586 | -16.42618 | -45.67155 | 2025-09-17 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c3ac08d-a990-317e-9b98-51bd3a637c66 | -14.78168 | -60.21113 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5b4e0d8-a844-3822-a091-d51f4f7b2f34 | -14.9764 | -53.41625 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 839d499e-abf7-3356-8bce-936f35dbae6a | -12.70521 | -47.95483 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2f8a6ca0-c446-3376-93f2-bfe6eb8f5843 | -16.69378 | -49.76705 | 2025-09-17 04:34:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc6eef3c-699a-3640-b382-fff1d88f9870 | -13.17658 | -47.31242 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c551f73-c5cd-3530-a2f8-5e52e4cdab71 | -15.42466 | -46.15212 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16fb37bf-f564-3a1c-a15c-d9867d975084 | -15.98437 | -46.44195 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98b41561-9b07-3714-8061-bd2e91baf44d | -13.22357 | -47.30429 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07aebcc7-e424-3d23-965b-d24dd9111fb1 | -12.85803 | -47.13282 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f82ac048-5c37-3a53-8962-2520fc668404 | -17.57007 | -49.0653 | 2025-09-17 04:34:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abcac2e5-b3ec-3453-aa12-72cc24de2458 | -16.50116 | -54.65765 | 2025-09-17 04:34:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74fba3df-fa55-3843-9b24-4141bc02b683 | -12.43819 | -49.72918 | 2025-09-17 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c80bb37-4ce2-34ba-8980-380fc96627c6 | -13.1356 | -49.20605 | 2025-09-17 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85276cf1-0e01-3c7f-aaa0-377814e844e3 | -13.01597 | -46.75604 | 2025-09-17 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f106ce48-d149-3269-bb93-9a4fb5d5d720 | -13.22007 | -47.28049 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f45079-1fa3-39d2-b4e3-0b69efb1ba90 | -14.75156 | -51.71117 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65fafda1-1fe2-313c-9e28-5fd95870dc4d | -12.86915 | -47.14606 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c10a544-862e-36af-bc7a-c0a8e57daea4 | -14.84174 | -46.7109 | 2025-09-17 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7cda9e7-e898-38e0-accd-244a9110ca38 | -12.70616 | -47.76726 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77208184-4b11-3b44-b866-5fc00c3d664d | -12.70278 | -47.76672 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7205a0a2-4015-3b27-a702-4611119cd8de | -14.46019 | -47.29246 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb103b62-7f3c-3023-a32b-436d5188c7e4 | -14.83098 | -46.70927 | 2025-09-17 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 821f9209-454d-3609-af03-192ad46ce98a | -12.29267 | -50.12502 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cb3cd16-e057-3436-9c5e-8d97fa870e42 | -16.61239 | -43.3652 | 2025-09-17 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70088aa4-bc75-366c-80b4-56249962ec27 | -12.39052 | -51.4105 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fed8ae53-587f-3ee0-b79a-4af005950311 | -13.03656 | -47.98502 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e68cdcb8-96eb-3847-8ebf-4e59af260acd | -14.97271 | -53.4157 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2006993b-bc7e-3d18-a8af-31ceb2de8e1b | -12.09625 | -44.83234 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efa316a3-dfe0-3eee-a144-207113d1cd31 | -14.91412 | -51.70348 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90e14785-0b08-330a-9419-b555893a5b82 | -12.8668 | -47.13805 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 086c0404-91b1-32a1-8fbc-e44b8c048189 | -18.16355 | -49.20567 | 2025-09-17 04:34:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a9ddf258-3738-3a10-98cc-b83326b09540 | -13.25583 | -54.2254 | 2025-09-17 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f0c458e3-2cb3-3a44-8131-da03fef6167f | -14.61078 | -46.37461 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 656669c5-8288-3dd5-8585-391b973f4cc2 | -14.82431 | -48.10536 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30db0019-a289-3ec3-b1d7-a31b51cea93f | -15.39626 | -46.13814 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdc12376-ab8b-3a36-a447-fd138f201db1 | -12.27359 | -45.29374 | 2025-09-17 04:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7c44c53-3ca2-35a5-b18c-ca28cc04ed5a | -12.59298 | -62.96523 | 2025-09-17 04:34:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 62fcde04-6078-33e7-81e2-02257a2dc6bc | -14.59902 | -46.32528 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3df37f3d-7cd8-362e-a02c-2263693b7b89 | -13.64839 | -48.70253 | 2025-09-17 04:34:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 962cec32-fb7a-3df1-af55-e42ac348a84b | -12.99107 | -47.94402 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README46.md)
