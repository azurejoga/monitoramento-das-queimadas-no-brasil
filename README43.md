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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c5e4027-952a-345a-a8bc-64e8e9ca6bb9 | -4.30281 | -49.10326 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c73b563-df65-35c7-a806-576fda800429 | -5.75481 | -57.59118 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ea3d623c-82c5-30f9-9f80-94086a121053 | -6.14898 | -52.74403 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e72441f-e90a-338f-90ac-4dfcdb3fcca6 | -2.10522 | -52.05118 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 806115b4-a933-343b-97d9-29db6b49e0cb | -4.53747 | -55.62216 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0352ebd4-2ee1-3400-954b-314c442a85d4 | -3.42692 | -58.22972 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 372d0823-4ee5-3aad-85ce-a14a586f3331 | -6.34454 | -62.68838 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b2a944be-e046-39d3-9f62-2b10b04d983f | -5.49234 | -60.16773 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 524e67bd-fb40-3214-8c6a-f9098b52e765 | -6.10531 | -57.6268 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8265f8e1-99a3-3f70-98b8-762ae20732d1 | -8.79717 | -46.90433 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61339ede-fa30-3a2a-9be4-6e7993884801 | -3.12269 | -61.25577 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 748bc793-0c0a-3a35-8670-97e602652958 | -6.19071 | -44.02985 | 2026-09-16 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c558b8ef-8f31-3929-b470-41a9991f18fa | -5.119 | -55.94202 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d06b8b8-ca10-383a-9854-f921fe9cf6f0 | -3.74219 | -55.94603 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36a72931-0ed9-399a-bc73-e4dfada59a31 | -4.43084 | -55.78551 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 96aa45dc-0246-3930-ad66-0100b6fc92b1 | -6.32881 | -59.99769 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3d9adee7-85c5-33b8-87a9-2ed0d1693104 | -6.34853 | -62.69506 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5c7bf422-5fc0-3380-9e9b-b99799d6a5aa | -4.52754 | -54.97264 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba0a2fe0-17d9-38b9-9182-0cde079d8686 | -6.77422 | -48.11098 | 2026-09-16 04:57:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0b09468-5ec6-37da-9841-9d486aee4df0 | -3.55414 | -54.47649 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24b5615b-8177-300a-afcb-3827dd3d6160 | -9.34189 | -44.3866 | 2026-09-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 43346713-5d74-3857-9be7-85ff72f11975 | -2.91696 | -50.4143 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1cfebe5-3664-35ab-8367-f33c45d81930 | -6.79887 | -58.78958 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aa5723e-7b83-346c-ae3c-389f55b15c7e | -3.76153 | -51.14877 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed19a0e-a204-3751-8a4a-968bed4430d9 | -6.34248 | -62.70003 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e29bbe34-3392-3c5c-8169-e0c10421073c | -5.2406 | -59.98786 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3ac5499-a416-35a8-a8df-c22cfcc19735 | -5.8377 | -52.11668 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9177d6a3-26a7-3cbb-86fc-d716b9952652 | -4.49444 | -55.50018 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f848d3b-3028-33f4-a447-c29e770c9a29 | -2.91461 | -50.40544 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c68c406-5146-3727-99e6-122baa806d17 | -3.08451 | -50.5721 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b9ec7fd-fe17-3a87-a6c2-c19812201a96 | -3.32387 | -59.44777 | 2026-09-16 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5de85798-9816-382d-8359-3c57d544e1a1 | -6.44756 | -60.01367 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ae85d16-cd46-3887-bf9e-a8800d308d9f | -4.43425 | -55.78605 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac3255d0-a9fa-327d-9f90-ca29c1b4dbf7 | -2.46076 | -54.76537 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3f41060-4432-3cb5-9609-00c32bf2653c | -5.31901 | -55.85646 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfb0230e-0bff-3f91-9f1d-af57f779bcf4 | -3.07444 | -51.20431 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc94b03f-589d-344e-9aa4-134a8edeab07 | -4.46621 | -55.25313 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c735fd-0f6f-325f-a73b-0d2145b94343 | -5.63396 | -51.67452 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20a325ba-9b05-3a59-82ba-25eca190c706 | -6.02437 | -51.7915 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6babc5e-40b2-3d59-b1f2-71cb06fec4d3 | -7.07858 | -45.24363 | 2026-09-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4488fbb0-6be5-3bce-95de-d70f0d6a6968 | -4.72371 | -55.73322 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ec7126-818d-33a8-8757-dfc83d2ef9eb | -6.66257 | -50.91898 | 2026-09-16 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e685085a-b6c8-3d9c-a92a-9a27a3aebfca | -5.10558 | -47.61397 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 85170b93-3508-34ce-9633-31c853d0a92a | -3.52493 | -49.39229 | 2026-09-16 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18dc27c0-712f-343a-8ce9-1962d2402503 | -6.34351 | -62.69422 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 98cd442d-aca9-35be-9ffc-0dd690a2cf7f | -6.36253 | -55.82728 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0895f8db-09e9-386d-b211-34c8786e6ac1 | -3.43002 | -58.23524 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb4e380a-7461-3358-bfec-359391a8adb7 | -3.47765 | -54.68239 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 267f57d2-1ee1-35c0-ba75-5157dff5423f | -3.45786 | -60.51847 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2aafbe1b-aee2-38fc-8e62-5856202ab60b | -3.73529 | -55.94496 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ab790b0-0a67-3fd2-aa00-b9b1942a0199 | -6.31948 | -59.97626 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8eeac502-5ef4-34cd-ab35-fb0ef9d0822f | -4.08822 | -54.43275 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13619770-642b-33ce-ae32-f32a0968fe28 | -4.43833 | -55.517 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67cafcc3-716c-39da-bd03-aea3091e7aa8 | -6.09454 | -57.69442 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e61e9d2f-d3bb-3026-a1ed-f9e5ae7fe48e | -6.33927 | -62.69193 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 312a1529-91d9-3a57-afca-7d211ff2404f | -2.97463 | -54.15895 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e26a431-9e1c-31f1-89e5-cd1cbf32696b | -3.48153 | -54.67941 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 347b1fa2-cbfc-3a27-afaf-a8f4c15cd6c0 | -9.48919 | -45.44791 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e2bd948-0df2-3394-b90a-33398fc239f3 | -6.15699 | -55.70671 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eb517e2-dbb6-3746-838b-89362d7c0509 | -3.53695 | -55.53397 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 106deb72-b9f5-3066-81eb-0db3ed1f846d | -2.72917 | -54.98211 | 2026-09-16 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31adc154-ecfd-3546-8d67-92d228ca7448 | -7.08779 | -47.49289 | 2026-09-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0bd92a9e-2089-31fc-aa3d-529c80d899de | -6.15756 | -55.70311 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19ec1f74-74a5-3452-94c9-98eb926fefd7 | -5.83426 | -52.11613 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f434cea9-b236-3178-b493-85db901f4f41 | -3.07853 | -51.20099 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e3a86b7-4237-3f9d-8843-960a91181708 | -3.73243 | -55.9407 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45faafc3-de06-3655-b210-f735dfa5b202 | -1.74116 | -55.25386 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa197ec5-548a-3d63-b3c8-3825335fe152 | -6.10463 | -57.63103 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1bbdfc2a-14df-358e-8bf6-678a5955c676 | -6.23245 | -56.04866 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da032f80-cb42-3bf3-8f4f-747ecde4755a | -5.22327 | -49.31348 | 2026-09-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ecc2bb3-5c3c-34e9-aa7f-c4362801f239 | -9.35855 | -50.08781 | 2026-09-16 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55e22dbb-9caa-354a-8afd-d58a79c4117e | -11.26869 | -54.12816 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 143ea7be-6ba7-364a-9b86-d8e2eca0fa86 | -12.32835 | -57.01346 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dc791c0-1f05-3f2c-b6f0-cc4d9a162662 | -10.83407 | -46.20318 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc8c1952-8b42-3739-8853-b7d746522b99 | -11.31063 | -47.24237 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a93a1d5-8ac2-3b46-bad6-6bc7594c9bc2 | -9.7038 | -55.13303 | 2026-09-16 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22d13fd2-183e-3e00-8b72-caf0ab2242a9 | -13.44158 | -54.57871 | 2026-09-16 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 657041c4-520d-3c4c-913d-412ba27aa368 | -12.12477 | -57.18159 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e2c883f-1ee7-3144-a91d-cdc00a147c3c | -9.57542 | -46.60818 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| decfb3a1-6d6e-35e7-bb18-ba7fa90d8e5f | -7.57335 | -63.29049 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f310147-51f6-3fc0-a971-0f92f8a27a0f | -7.61422 | -67.24683 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 75f4877a-971a-35df-8425-61af4c57ad88 | -10.93891 | -54.08486 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de98ea72-99b4-32d6-b9fe-b5c6853e84c9 | -9.12792 | -65.84843 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d3fc568-8598-3719-89c8-40ba05a8fe67 | -10.79244 | -46.20147 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cb84424-0e0f-3874-9b3b-565a33cfe949 | -9.02295 | -61.01977 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 429a7d54-7e71-31db-8d06-13d7a149e45f | -10.40819 | -48.6552 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d6b1d1d-2203-3eed-9bf3-a073f7d46506 | -10.90221 | -46.29932 | 2026-09-16 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51d03436-b468-35ba-a89f-41d9f82e1c97 | -11.19182 | -55.0307 | 2026-09-16 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca3c94c8-1541-3302-8c93-bc3229d38ab9 | -10.82218 | -46.18072 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 734842c0-ea56-37c0-919c-d00f67523547 | -9.81653 | -48.91177 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dda3e227-19c2-338b-a254-2decf2365dde | -14.66713 | -48.01798 | 2026-09-16 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| da5c1571-fb4d-3dc6-a15d-f30e9fbe263a | -11.19445 | -54.12812 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bfd7ad7-1619-3b68-9bf2-c3a4cd98aac3 | -11.195 | -54.1245 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fff00aa7-7518-37c2-b8a9-d45d75dbf83e | -9.25747 | -60.2787 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfdd2053-3161-30a2-8d6a-bb95f331402f | -9.7134 | -64.91599 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4036da3b-f1e6-3571-b3fc-add365d02afc | -9.81244 | -48.91749 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6f79c57-b5b6-3877-82f3-12dbf76b7a59 | -15.04035 | -48.56677 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8ffd3c5-a4be-364c-a8be-1f95f54fc640 | -9.71272 | -64.91971 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b823007-ae48-37c7-9140-73794ffc17ea | -13.30423 | -51.75632 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22d35ed9-8104-3792-8e80-9fd29c683cb0 | -9.12664 | -65.84639 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
