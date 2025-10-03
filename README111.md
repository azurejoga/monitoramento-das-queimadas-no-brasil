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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c65e37e7-5295-3810-87b1-bc7c75a84dc0 | -15.20934 | -47.18383 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a2c6103-e9e4-3c41-ac7d-f0a2523084b5 | -14.71693 | -48.20307 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f519b974-eb54-3e70-a77d-c857180c9a9a | -13.76255 | -48.08046 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 885aea60-0bc2-35af-ace2-cadf8753cc9e | -15.25293 | -47.91399 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8438eaa8-18d1-3b5b-b3e4-975182e45cbc | -15.35065 | -46.29355 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a623fd6f-4c53-333d-b827-4729dcd80862 | -20.11335 | -44.38971 | 2025-10-03 04:34:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ab26897d-e64e-313c-898c-666974ca64bc | -17.06278 | -46.62776 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe311a0c-2adf-3a91-a465-4349f491b26b | -14.4379 | -46.10691 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa4757f8-5e4a-39fe-9383-ea645c5590d4 | -14.20287 | -46.10743 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ebd13c55-2ed5-3819-9ef6-b3e1d1c4a256 | -13.30407 | -47.82288 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72e579d1-99be-34a4-91e6-b7bcf3229626 | -13.97014 | -48.16552 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abc44caa-43c6-3440-8b80-54868a53819b | -18.18238 | -53.28579 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 045b9ebd-746a-36f9-ba34-2ae685de0030 | -14.89134 | -46.98629 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfbbadbf-eeeb-3509-bd63-8fcb2246df46 | -11.28789 | -53.94487 | 2025-10-03 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4079621-5b7e-3a6b-8b00-fbfb00f85b28 | -16.17883 | -57.60278 | 2025-10-03 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8516dc2e-11b8-3018-933f-9552eca1b6ff | -14.66826 | -48.2635 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4696c0ef-87a9-3fe9-8af5-2720a5e00425 | -12.89874 | -46.93401 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91aba5c9-3eaa-3f25-b2dc-0c6b36ba3005 | -15.08359 | -42.12495 | 2025-10-03 04:34:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f782af9b-b708-374b-aa1f-1962180a9508 | -13.32344 | -47.20622 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78db4180-1404-3bee-a634-191494535be0 | -15.31579 | -46.38263 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13e70140-3a83-3e1f-93a5-5a0275567a77 | -15.29105 | -47.96243 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 592df72b-b489-36a4-9433-834840a34540 | -15.34271 | -46.29679 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86e9c7cd-d518-3727-ba9b-5cf107823d54 | -14.87895 | -48.30491 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0c13698d-7dff-350f-95ce-e2f29d152e7b | -14.73695 | -48.1157 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ca7d739-d322-3c4c-bc5f-180cfb1b59dd | -12.65206 | -46.87273 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21addcec-5ab8-3427-a952-5cd7e9abfdb1 | -13.50849 | -47.25365 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 031694ef-dd6c-35f7-a5c6-d29935988d4b | -14.38025 | -45.9374 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa3d9ba2-36e5-3a2f-a9be-e0fdaefcbbb9 | -13.43504 | -46.72795 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fbb7511-4d09-3969-9373-73635b1b3f04 | -13.30323 | -47.59814 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34a21281-b4fc-3422-aef4-0d30ecd11853 | -18.45011 | -43.80858 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a50b352a-ae43-3cf1-b828-b13f6e831d4a | -13.51947 | -47.25093 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f66126e-34e7-31ff-89e4-0e335bb64dcb | -12.72635 | -48.58082 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 34637e5c-0744-35ff-8769-74d838a6b695 | -12.91141 | -46.92034 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 137c7ad2-b609-33f4-b29f-e52011bc0773 | -15.3195 | -46.8971 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b166947-e3d0-3954-a659-ba2c5122abd8 | -19.90266 | -44.5079 | 2025-10-03 04:34:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9f30eb99-c05c-322c-ad53-bfe32eb4136c | -12.9114 | -47.15588 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0007cda-14a2-317a-840c-c77d3e5da3c3 | -12.83442 | -46.94803 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| acf67d31-caf1-3c6e-9db9-be5d5b716763 | -13.3388 | -48.12648 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96795726-edef-358d-b0a2-f0186c42c57c | -17.18736 | -47.01661 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca89a578-a78f-35ac-adf0-9303acdb21e1 | -14.95452 | -50.00315 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb7fdc95-ec91-3d6b-bedd-182fb9ed6b95 | -13.21659 | -48.52802 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9397528-7d10-3115-9982-11a3e968040c | -13.34437 | -48.11244 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13908f3f-86a5-35a6-99cd-a3c732fc233e | -13.7749 | -47.55404 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 93705907-77db-3b19-ad81-901f5c535c4b | -12.83096 | -46.94748 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb509fc-4482-3df5-b899-bd2b384f7880 | -14.87616 | -48.30061 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c3894b5-ba65-333e-a150-55b55b323a49 | -19.69174 | -47.63099 | 2025-10-03 04:34:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bbabb19-d201-31a8-be62-fcd7637301ee | -14.21678 | -44.95171 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1027911d-f272-307a-a847-ecdf03d96276 | -13.30851 | -47.25872 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a0488221-b5bb-3378-94f9-b2c66ae4d79c | -20.00865 | -44.18499 | 2025-10-03 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6bfc0a37-7182-35f2-8103-7cc0f988ea33 | -13.35223 | -48.12856 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7733fadc-05c0-3f7b-8b5b-2fce466cdcb7 | -11.31879 | -53.95762 | 2025-10-03 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59d66569-c30d-3de9-bf35-1cc7e735c256 | -15.27058 | -47.9128 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ca3c5ab-08c7-3abf-b17c-811cb308c5e3 | -16.06772 | -51.00512 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a7abe4b6-22fd-3db7-aa88-2b5df3db8af6 | -13.54478 | -47.29356 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f09d4469-5f35-3cba-9fbe-be13276536ff | -12.64859 | -46.87221 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d36f210-4e25-3c98-b653-1b0d4553f4e3 | -14.91437 | -48.29888 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e5473ee-de62-39ba-b666-14266a6aabae | -13.5746 | -47.27802 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 091412eb-3c68-3fb5-9ae3-f871074abd1e | -13.78112 | -47.53585 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22b5b854-fcd3-3444-a158-7d699247067c | -15.21832 | -47.9588 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeac60e7-9915-38b3-8eef-d054078082ba | -12.83499 | -46.94422 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5594a74a-8fdb-3270-b1ea-fa8e2eb0cd99 | -14.35712 | -43.85183 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 921c698a-4bf7-3ae7-914b-f798a2acbbd2 | -15.32439 | -46.2972 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e87ebed1-b977-3653-9919-a92232f05c14 | -13.53105 | -47.24424 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa05c1ad-de49-3bf8-8eb3-22859d6d10dc | -13.67819 | -48.63437 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f94c0bc-b217-3c80-9694-1ca0d8cbb8f1 | -13.265 | -47.2439 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1252def-223d-354c-862c-6d9ee0e96dd3 | -14.87213 | -48.12141 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d494922-10c9-3f27-a946-07d293d7ee27 | -14.20596 | -46.08577 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b70da321-8a47-31a7-b19e-4d73a9e1ceaf | -14.66264 | -48.25508 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1cf341d1-6d73-3243-8591-a62635c257ff | -16.35835 | -47.07171 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| daf4515c-308a-3c67-9b6b-79e26e1171c7 | -13.96396 | -48.16083 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 273ad25e-709d-3d73-9313-f5d8afc54179 | -12.80262 | -46.87607 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3011d16-3804-3614-abf4-5f5ef4a61405 | -15.16986 | -43.62456 | 2025-10-03 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 514810f4-4526-3c2d-9aa6-9e25822f9d6e | -13.35278 | -48.12494 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3453ebd2-7562-3ef7-9430-9830912b09a1 | -16.03765 | -48.06894 | 2025-10-03 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9720ee4-984f-3d3d-a2f4-2e8f55a70538 | -19.73104 | -45.88786 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36df7eab-8bf0-3735-8c26-fc6db307f074 | -12.99636 | -47.75082 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce9c189d-278a-39ec-8c17-9446ebb04058 | -14.8949 | -47.82884 | 2025-10-03 04:34:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 996be9bc-a612-333d-9c56-071d4bd334de | -18.90846 | -47.01405 | 2025-10-03 04:34:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 116c1a26-d515-3c17-8927-b5c2d9195bdb | -18.4039 | -50.7828 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2d063578-efa5-377f-abeb-fb1898055224 | -15.36572 | -43.67039 | 2025-10-03 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 866c2291-f33c-3c2b-926b-2e45677b1378 | -13.39843 | -42.65088 | 2025-10-03 04:34:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3add34a1-42a1-348a-afce-8a9ef9c9a03c | -15.9943 | -50.9136 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef906a79-1913-31ee-80a9-a481bb0e8d24 | -13.24764 | -48.50371 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3445f025-36a6-3065-bdae-85154c35ce16 | -13.75198 | -47.98149 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b047102b-b7f4-3afe-be14-c6454a77681f | -13.32579 | -47.58691 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5a9ebb3-1657-3741-95e2-79a65425cea9 | -14.29035 | -45.88998 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63e4d97b-a452-3bf3-a721-0156a94a6f92 | -12.82629 | -46.90772 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26fd394e-f780-378b-b236-6d2812af2f0b | -15.29877 | -46.2933 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6745a1bc-7da8-367b-8917-6b1d88e2b32e | -14.91213 | -48.34779 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd27b3d-bd87-37d8-9d4c-9c28e8443916 | -12.69117 | -48.5459 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad654d01-5ea7-3554-aaa6-608fcba1663c | -16.34931 | -47.1092 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a51b7abb-9d4f-3b09-811e-a49c68717802 | -12.64075 | -46.99723 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01a9fef8-7afa-3ef2-8182-18b0d321d527 | -15.3038 | -46.38784 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6be11fa-fb70-3b90-a635-05716786be71 | -12.62673 | -46.95753 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be0ba43c-20e4-3a04-a96c-c3b5562a3c98 | -12.37664 | -46.51124 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5803b81-d726-3a73-942a-20fec9372c6b | -14.07675 | -50.16095 | 2025-10-03 04:34:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b90c3189-af89-3633-b669-c5b14407439c | -10.89844 | -56.19633 | 2025-10-03 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c43c162e-2046-3fe2-ba69-560b01dc28a9 | -15.59212 | -46.93098 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bffd598a-5966-3d88-b694-a85560656e2c | -14.28578 | -45.92157 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 396fa91b-df9e-3632-863d-85c5f654b2f3 | -15.28729 | -49.3125 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README112.md)
