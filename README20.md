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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7acfa989-adb0-3c96-adf4-617c0d3f4936 | -9.09321 | -59.40999 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9224f9de-2e85-3f74-a5bb-4a4b9c1a3835 | -12.22844 | -56.55297 | 2026-06-28 05:33:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3d9c6c7-706b-3c9e-9a07-f5f70e7ba361 | -10.93808 | -56.85678 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c208149-c502-39ca-b82d-8f5635b96eb3 | -10.93859 | -56.85332 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6cd479f-9c52-32d6-87d4-742188f63f18 | -12.19491 | -52.91233 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 280c06cd-2c2d-3eb5-93d4-1aa47dbeb21f | -12.09068 | -52.00591 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dce3a949-09b6-3e0c-9a3f-84bfe04b1198 | -9.09264 | -59.39055 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b03ed317-7f3c-3974-be6c-fc8232ae2367 | -12.19704 | -52.89556 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4157a74-ceac-3cc2-82d3-f28c2db5ba6e | -12.19619 | -52.90228 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d4ecb0a-c49e-330e-bf9f-1e7b133c2540 | -12.20006 | -52.87175 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b28cc9fe-26df-3bf6-8960-d2b26e9f805b | -10.29573 | -57.13015 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f6640ad1-035b-3c19-bcbc-072c1ab25601 | -12.18229 | -52.88313 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b34fdf5-7d0d-3354-9824-ab09ad9b56b5 | -10.63058 | -50.53962 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2380f6a-c530-3e2d-b307-218fa6088c7d | -12.19747 | -52.89218 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd4843cb-2434-3e6e-a70e-d32cc3ad59f6 | -9.08862 | -59.3938 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b75919bd-2221-305f-9675-6f73cd6c3972 | -11.72177 | -59.35466 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c4dc46c-0189-31d6-b15a-f931e08fa77f | -12.0836 | -52.01672 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ffc4643-bffc-3a13-83cd-7d1b25e7579e | -10.93456 | -56.8528 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2dc4a3f-65f3-38b6-b4fb-03ba42baa5e9 | -12.08313 | -52.02052 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5df6ead5-211e-3dab-b91f-2971654300d0 | -12.18423 | -52.91095 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 608897a2-6f12-3f23-a922-a6c1b60e04d0 | -12.1855 | -52.90086 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 476cd7b7-e17e-3a01-b40f-6258cc57befb | -10.0581 | -60.5033 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a1fe55f-c4b2-390a-a506-e41270f7d12e | -11.90449 | -57.1309 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a4a7b8a-3992-3ab0-80c6-304682a8ea42 | -11.2142 | -53.82718 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a0c91f4c-3be9-3fc8-902c-02e996b3f5d5 | -12.18144 | -52.88994 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57bc5d1a-8eed-378d-84d0-eb9a35ba8154 | -10.30605 | -57.14186 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45de1b97-e8c9-3c1b-8066-1d89ebf6e0b5 | -12.17929 | -57.14154 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6a9333c-49d2-3c0e-b63b-18e90454138e | -9.08288 | -59.40838 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa250b5e-d269-393b-8545-0729a9dd6544 | -10.53784 | -53.71502 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6260f367-61a6-3e96-a263-d15ef2ca84f0 | -12.19427 | -52.87443 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0ff1b39-cc48-3d75-85a5-eceb764b3116 | -10.35668 | -50.18587 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31a1e115-1b15-3b5a-820f-76d10c295b85 | -12.19127 | -52.89821 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3683bb10-ba00-3341-bde3-e808d6bee8e2 | -9.0892 | -59.41323 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2a7c894-6bb9-34c7-917d-f93aa3923f7c | -12.08407 | -52.01291 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69fa28cc-c8f8-3c67-bfa4-4abab467eff0 | -9.09436 | -59.40244 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fc6592a-de40-343b-be97-2ffc27c8addc | -10.36349 | -50.18177 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea16fefe-a75c-35d4-82eb-05ea166ae45d | -12.19576 | -52.90563 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdbb0d8e-aadf-3abb-8ff8-86020938f5b8 | -12.20541 | -52.87249 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 53b94689-2447-31b9-b9d6-f5ef0413d672 | -11.8495 | -56.84021 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6244a193-413e-3674-8a61-2d70188f5b24 | -12.09493 | -52.01808 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aba27106-c181-3431-ac4a-77ee8654521b | -12.18058 | -52.89675 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0df7d7e9-9537-3152-93f4-829ec38e4737 | -12.08926 | -52.01746 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21ae8c65-d1e8-349a-9fad-c0ffc523747f | -9.08977 | -59.38623 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9ee426b-6f46-3a76-a120-ac210311c121 | -11.92215 | -57.40725 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 20c237c2-77ab-355b-9da4-e0b782d38f17 | -12.18272 | -52.87973 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00a30e18-92a4-389f-9b59-cde1c6cf2b02 | -11.93318 | -58.63054 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ba2de8-fc00-347e-ad8e-7b0803ed76b2 | -11.93015 | -58.62561 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66f252e3-5bbd-3b3d-8f3f-080a39a7076b | -12.18105 | -57.15795 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccfbb5b0-0654-3b80-a8c2-fd52171c427f | -11.92202 | -58.65565 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26a585c0-b237-3d83-9b32-a2eca8c65775 | -11.91428 | -57.4061 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25d09f67-bef8-36b5-89b5-570f23e07907 | -9.16765 | -58.06935 | 2026-06-28 05:33:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcec090b-e7d7-3efd-a939-2f6ab07cc7a0 | -11.90195 | -57.11972 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33af054b-9fcd-3e83-a1b0-beaa2697666a | -10.29965 | -57.13075 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d9c9c3c2-2c7e-31aa-b9d3-a64b3aec71b3 | -12.17931 | -52.90689 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 352bff2b-bf00-3d3d-93b5-ed655be7ac1a | -12.16801 | -57.13443 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 638b2685-cc69-3d81-a21f-fa64291dd897 | -11.92809 | -58.66537 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b539ac76-2aad-3819-92af-22a48afb50e0 | -11.90268 | -57.11448 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b221a96b-fdd7-3050-b1e2-65a110e13761 | -11.92143 | -57.41227 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6d09f83-047f-33bf-9e1d-6d72a47bc61d | -12.1917 | -52.89484 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33fdd085-68d5-3d1d-8ad3-6239759ad9de | -12.17528 | -57.14092 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 739a255f-5c63-33b7-92bf-855ed3e72e9c | -12.09541 | -52.01424 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d32322-6635-3b95-a761-d7a751a209be | -12.19298 | -52.88467 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84febbb4-c74d-3037-ac2e-28f4510551f5 | -10.05616 | -59.11119 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a752babd-bc68-3d02-90d0-3685f3323019 | -12.19341 | -52.88127 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8954ffa9-02f3-373f-9a4f-43ae640dbb1a | -10.05676 | -59.10727 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 398ac58a-5f63-3222-b0fa-5403009d96a0 | -11.9085 | -57.13145 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94105251-0a1c-3b6f-928b-f04f27fbe121 | -10.06257 | -60.49665 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3349a11f-131a-383f-b41f-9a0a9c038356 | -12.18506 | -57.15854 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c66a573c-2ace-37c7-8d7d-91cdb6655350 | -11.21283 | -54.313 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86b1e227-814e-36af-a99e-858fa0575f21 | -11.72237 | -59.35065 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48112b81-02e5-3a89-b9d1-4ab9031b82c7 | -9.09034 | -59.40568 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0de79ca2-34e1-37f6-ac5f-d575738f159b | -10.35727 | -50.18095 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbb15dbd-8305-390f-afc1-4d658c40fc29 | -9.09207 | -59.39433 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f05a10b1-de68-37c9-b04d-21e1b67b7a23 | -12.18696 | -57.15029 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf92eca1-9d73-3581-83c7-5991e4058988 | -12.18465 | -52.9076 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70021367-a878-3dfd-862f-f927436b63f9 | -12.19557 | -52.8642 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6738687-3f97-36d5-9d69-d0f8689f70c2 | -11.86324 | -57.81539 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0224d9dd-d397-38a0-835d-ba209d950fc8 | -9.03052 | -61.33806 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afd5891d-61c5-3024-b71f-3d91bcaeb6f8 | -11.87232 | -57.80684 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ada5c3f8-35c1-3718-b14b-ebb8759ca188 | -12.18187 | -52.88654 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73285c3a-fa3c-3cdf-8453-a344c8e1d808 | -10.53861 | -53.70942 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0789d9c8-91ef-3131-87b3-5064e3720389 | -9.18656 | -58.06787 | 2026-06-28 05:33:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a77d3b4a-088e-3b68-918a-2800c4cce045 | -9.03108 | -61.33456 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08a0818e-793b-328a-92ae-d7a925031305 | -12.17603 | -57.13564 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77de5be2-d345-368e-a3a0-0256d6691c59 | -10.30428 | -57.12631 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b49a07e-fd6d-3e84-bae2-d0d742252202 | -10.30036 | -57.12574 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 01a3585a-5a6e-3ebf-acc1-396e326cb53f | -11.92442 | -58.66486 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1db5831a-03c4-3810-821f-c5fbbce069b7 | -9.19022 | -58.06842 | 2026-06-28 05:33:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad5a7112-d320-3aa3-bb3c-e0f93fcc992a | -12.16073 | -57.12791 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b52c610b-2c10-33ca-859f-df98aa862b01 | -10.35786 | -50.17605 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 493cc346-90d3-3432-bd9d-33341c30514c | -11.9504 | -58.61541 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb6644c0-1340-362b-945b-05cac46e90aa | -12.18101 | -52.89335 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e6f205b-07ed-3d9d-a948-0c67eb689c54 | -11.92569 | -58.65616 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 330223db-b957-3d4f-a2b2-8fd4660a0c44 | -10.77813 | -54.10818 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 016964ca-b543-3ba7-9013-0bcc4685b9a3 | -12.1818 | -57.1527 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7434dbd4-f08a-3631-8fe7-e8f00634cf3d | -11.88468 | -57.11564 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4514e22-59df-37c6-9e0c-db981b4524c0 | -12.18255 | -57.14745 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e5ecbe4-76c0-30a5-8246-b14900e30acf | -9.03329 | -61.34209 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5af250a-bbe0-32bc-ab42-56b1f316a14e | -9.19213 | -58.05553 | 2026-06-28 05:33:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7959bc24-6874-3cd8-91d6-983828d833c6 | -10.93958 | -56.84641 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
