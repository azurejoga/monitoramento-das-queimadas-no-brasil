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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d60668f1-e91b-34b8-8ae3-38720f4acd2a | -13.16941 | -54.92678 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa0da7f6-dcd8-3f08-8d4b-f452de8b9c6b | -8.36836 | -70.13832 | 2025-08-19 05:18:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25763971-d2e9-3999-b9de-3a58ec294d56 | -13.16105 | -54.92558 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebaeadd0-335b-38d9-9f8a-86bb5f11d073 | -16.81855 | -49.36781 | 2025-08-19 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54deb6cc-8415-358c-89de-c85c845c793c | -16.62857 | -51.36421 | 2025-08-19 05:18:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9769becf-8073-372c-a8fb-746e71c4c697 | -15.0828 | -55.42523 | 2025-08-19 05:18:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 329c764a-9d95-309f-8d1a-c161760c22c9 | -9.51662 | -60.51585 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ee068aa-9080-3145-8d13-a00beff4e228 | -11.86499 | -51.57942 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fac76eb-6fb0-31fe-8d3e-e725b570ffd6 | -15.02047 | -54.81813 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c4286dc-9c92-3ee8-841d-997f53810a16 | -13.17623 | -54.93951 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 675b6c28-91ad-3770-8aca-31be47e8bdaa | -11.6182 | -58.4244 | 2025-08-19 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ab2edd8-a10c-3004-b1dc-6007abdf1398 | -13.00066 | -56.84976 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b02e65c-3a85-3ce0-80bc-a19ed008f28e | -13.015 | -56.82879 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 530b7a24-b5d5-30c4-951a-b200af434819 | -13.17519 | -54.94725 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c46c35bd-7c90-3df3-a6ae-bae762f1f934 | -13.59265 | -46.99105 | 2025-08-19 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a380a950-2a8c-3b85-806e-47ac9ae565b7 | -12.98022 | -56.86054 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fa5fd63-4678-3d39-ae15-9f51280872e0 | -9.28421 | -60.77961 | 2025-08-19 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0432f6-54a2-37bd-9e6b-bbf0d693e240 | -16.79434 | -50.09576 | 2025-08-19 05:18:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4f16332-e01e-379e-bbd2-db45b0e50aa1 | -11.74885 | -51.94017 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1278a7e-be4c-3bff-b980-43678c2a01b8 | -9.48042 | -63.50998 | 2025-08-19 05:18:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 378008b3-4d38-3d16-8e1f-11a3d5a7b7fb | -14.61915 | -54.89965 | 2025-08-19 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ef19507-ec48-3e65-a13c-090ac407a0d6 | -10.92085 | -68.43197 | 2025-08-19 05:18:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7b279af-2e2a-32f6-bf66-176b7aa31edf | -12.99822 | -56.84023 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06862c4e-55a4-3d0f-96b9-0a41ef8ff6df | -14.8461 | -48.06466 | 2025-08-19 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3f80e81-505d-3f73-88bc-a6fb5b8acc04 | -10.03955 | -59.35552 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 095ca509-2df3-37f3-b149-86267507d3f3 | -13.15951 | -54.93715 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 98d4a1b8-1c94-3b67-8ee1-bfe18bc553f2 | -13.19241 | -54.94582 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da247770-b50d-3dc5-9141-36ca9d3eb1d2 | -14.98112 | -54.81615 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8839b6c3-072a-3c74-ba5f-b4f6e12c6571 | -15.0419 | -54.82251 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd39d3e0-9c18-3463-a470-eea79626d821 | -15.15446 | -48.77989 | 2025-08-19 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8d11af1-0ed6-3347-983d-85ee04b93047 | -11.85429 | -51.58121 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea26104f-19c8-3360-a531-afcc69a93e31 | -13.18771 | -54.94907 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8f6338f-3862-3e4a-9e2d-1e5a73337dc7 | -14.97541 | -54.81281 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f55459e7-c1af-3a97-94fd-d68d0d6c56cd | -14.97614 | -54.78582 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ccff829-f67f-3bd5-b1d0-01f4ab58fac6 | -15.02199 | -54.80636 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00868a98-9f18-3fe4-bd56-69bd3d0628db | -13.30907 | -50.80624 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01b7e072-95fc-3c60-a16e-baab4c61f5b4 | -9.92562 | -60.46614 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60ebfb54-6234-3f1c-ab9c-bc841de6022a | -12.98518 | -56.85214 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb917e6a-7a8d-3fbd-bf95-8f9b858339bd | -13.13306 | -57.15258 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5adbbb82-8db3-3cfa-bf96-ca2d20ecdb01 | -11.8587 | -51.58792 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81a327f7-8fcc-3085-a884-f93098ffa8ab | -13.58411 | -47.005 | 2025-08-19 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71e2565b-3a74-3c0d-b123-17968accbdb0 | -12.99387 | -56.84421 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f758d83-8b29-3f9b-a4e3-35175e764415 | -14.29841 | -57.76488 | 2025-08-19 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83725bb4-de89-39a0-b8d5-01d285e4e0cf | -11.85744 | -51.58025 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bdca18d-bc7b-3314-9378-e87811efb167 | -13.16054 | -54.92944 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fedb3e4-6261-3ca5-af2f-d7dd298828f7 | -13.1642 | -54.93391 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4876fd43-777a-3644-9c50-41cf106802ea | -9.516 | -60.54108 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 577946e3-36f6-3356-a7c7-512fc551774a | -13.00872 | -56.84631 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f4215a6-0b31-3f89-9051-d13e18154b2d | -13.01372 | -56.83783 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f6bb778-6768-3478-a530-5f1a6341a0f6 | -14.98571 | -54.80164 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 398ece6e-85f8-3a32-93b7-917a0cbe7930 | -13.00629 | -56.83677 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd74111c-20c7-39ee-91a6-4d6a3914fe41 | -13.14037 | -57.15365 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69f3cc50-66d2-3062-a9cf-b1d755f83be9 | -15.02954 | -54.81601 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 462b2cbe-0110-373a-804a-67a64d5183b2 | -13.44037 | -56.851 | 2025-08-19 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da99cde9-2497-375d-a9ed-6e3a356d3291 | -8.36902 | -70.14035 | 2025-08-19 05:18:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5eec3032-3a62-3ff1-a497-d662c6ed0f80 | -13.01064 | -56.83278 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80464a84-aaed-3d5c-bc01-ee0659d8e8b9 | -13.14285 | -57.16107 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af583e6a-cefd-3c69-a396-4e1e2df98460 | -11.85785 | -51.57719 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caf06398-2fcf-3599-bc7a-ccb5b941f513 | -13.13243 | -57.1569 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42ade22e-9ad3-339f-bfa1-01ec6179c275 | -14.9768 | -54.81552 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 571ce90f-d44c-3037-890a-e074b56af7d3 | -10.0401 | -59.35202 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba94156c-4970-36af-aab0-9bf95de397ea | -10.039 | -59.35903 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5d5c40b-5a03-37fc-83b3-8c537e84c258 | -14.96467 | -54.79425 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18feb019-4fe5-3a54-8afd-ae6d6fc12722 | -11.85945 | -51.58183 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92c9600c-fc33-3d35-ba35-a982621b1d99 | -15.02905 | -54.81985 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| beca6604-ca56-3edd-b3d6-a6b12108f199 | -12.5058 | -57.78136 | 2025-08-19 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3f1905b-3bd7-3a18-8009-d0d9c4416447 | -10.03569 | -59.35851 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2a23ecb-2188-3c8a-99b3-7cf21ea75827 | -10.42828 | -60.29597 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acfb5f2a-f1b1-37cd-a49a-52f04450c228 | -13.17049 | -54.95056 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79fc7522-9dfe-3659-b354-4109bee026e8 | -15.74762 | -56.02566 | 2025-08-19 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7e16ad0b-0ed1-309d-8716-10a70be7a1f3 | -13.00437 | -56.85028 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e490bea-d5a0-3dfe-82f5-8431e4804b2e | -13.14769 | -57.15469 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a47da454-f81f-3ffc-b56e-5bb04dac1230 | -15.07915 | -55.4209 | 2025-08-19 05:18:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fbbf727-2b63-3ab7-8674-67c678cd5acc | -9.52045 | -60.53456 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03152d19-8101-33b9-b9c7-a55170002926 | -13.16208 | -54.91784 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c47d850-a220-357d-91c4-2dfbbebc2d1a | -14.96843 | -54.7991 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f085ba36-88b6-3d95-ba8f-0a0606f4f448 | -10.43215 | -60.29301 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc1bc72-36af-37df-bf58-70c3a2740461 | -13.0013 | -56.84527 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ab2433d-25b4-321d-b9b7-77e07c979097 | -9.51437 | -60.52996 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 969ca4a9-076c-3b42-9ad3-2e0c1c65843e | -9.52158 | -60.52752 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b77e4e2-b20c-3ff8-9062-3050e3daec77 | -13.37537 | -54.41684 | 2025-08-19 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 445118d2-72eb-3e96-a716-72b0f452ad5e | -14.84725 | -48.05344 | 2025-08-19 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90a209f4-c7e3-371a-9678-9f9fb9d59b0b | -9.71618 | -62.40053 | 2025-08-19 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b6ed63c-5d18-3bc5-9fe1-4afb943eef3c | -13.15739 | -54.92107 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee261dc8-dc1f-3c72-b9f7-d22ce78a4bb0 | -15.03812 | -54.81777 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc4bc2e0-c317-36fb-9498-38763a07331c | -15.01718 | -54.80946 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8061afa5-3466-3a7e-8819-2312430a4928 | -13.01128 | -56.82826 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e789ec46-3cab-3a59-a6f5-fff7db1c5f79 | -15.55563 | -58.70063 | 2025-08-19 05:18:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf74fa39-2121-3101-b5a3-0c1c5b81600d | -11.8531 | -51.57341 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c88b2d2d-c6c8-3f9a-8f33-f8b4dfb2b8cb | -13.25373 | -50.79929 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31bc00c4-6237-3424-b1de-99f389dc8538 | -16.62397 | -51.3547 | 2025-08-19 05:18:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fbd5b85-1759-3fce-a6c6-550c109db4dc | -9.5347 | -63.57505 | 2025-08-19 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7554c77c-6f2a-3cf5-86b6-269719d3ac46 | -12.29521 | -50.01313 | 2025-08-19 05:18:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1785767f-9be7-3ee8-a9d7-c4e4256e9b76 | -9.51769 | -60.5305 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccdf53a3-71f4-3d81-94ba-67a5305e9f36 | -11.09161 | -58.93989 | 2025-08-19 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a561c5-4d6d-31b3-bf0c-a88674499c69 | -13.14101 | -57.1493 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adca7688-d9f1-3a28-a3d3-ca2ac8b66710 | -13.1579 | -54.9172 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ebcc047-0f79-392f-9011-d587372cbd44 | -11.94983 | -58.75604 | 2025-08-19 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7deeda62-f7d7-3a6e-9e22-0886f31d8815 | -13.30997 | -50.79883 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff91a072-b7fd-31a3-8f3e-426c49c89e56 | -13.16002 | -54.9333 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |


[Clique aqui para ver as próximas entradas](README52.md)
