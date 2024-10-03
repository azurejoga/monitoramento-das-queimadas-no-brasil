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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c4a81dd-abbd-3656-af5a-ef89b369a03b | -10.42377 | -48.1639 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec89ea07-af29-329a-8021-e4d5560f2ab3 | -10.42319 | -48.16754 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7670d1bd-62f6-3a2e-9db2-f11976e34805 | -10.42159 | -48.15617 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c7701b6-26f3-33cf-a59b-5e7b65df9592 | -10.41883 | -48.15205 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 895b3aa5-45f2-3dbd-8b5b-a31425c6a267 | -10.41493 | -48.15508 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d95957a2-bf55-3775-85d7-7f78f2fc7993 | -10.41161 | -48.15453 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56c5579b-07f5-3b87-8407-5e99242d56f9 | -10.07963 | -48.16586 | 2024-10-03 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8f26762-114e-304b-b7af-da3d60c6c218 | -10.0338 | -48.21685 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a8897ea-2079-3dd6-b515-213d4a0eeb34 | -10.03266 | -48.22397 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b3a842-91ac-35a5-92d2-adc7bebd46f9 | -10.03047 | -48.21632 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6063bdfc-1e04-3d71-879e-395f204b03ee | -10.0299 | -48.21986 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2098cc1b-6473-3450-a333-fb91394d9a28 | -10.02932 | -48.22343 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dd79f85-a228-3341-8a80-39633eb91725 | -10.01112 | -48.8502 | 2024-10-03 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5e01691-0567-3784-a5a2-b919d6ce2f34 | -10.00772 | -48.84966 | 2024-10-03 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 569e4741-4a43-3f3c-b0bc-c21ced6803cc | -10.72883 | -47.63644 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9d54feb-d17a-3633-a83e-f4d8b7bb943c | -10.74966 | -47.70068 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0c4fbea-ce8d-3324-933e-7d85e0e1d473 | -10.7491 | -47.70417 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e966e43-3601-3d52-8c1a-d1656349ef68 | -10.74855 | -47.70768 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89b72b79-2ac5-3258-add4-24688cd0ff11 | -10.74799 | -47.71118 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f21e30f-a85d-311e-b859-43bed5dbfa39 | -10.74743 | -47.71469 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf8d84d5-4a82-371f-9177-0946f9adbb39 | -10.74697 | -47.6932 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6077bcd4-5e68-3552-b5e4-e65334f40ebb | -10.74531 | -47.70368 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 433d95f8-0eeb-34a2-8f01-861e92e274c3 | -10.74476 | -47.70718 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 675c80b3-c199-3ec1-ae61-e6d612cac240 | -10.74367 | -47.69266 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64995592-df4a-3052-a09b-3c8e1029ea27 | -10.74256 | -47.69965 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac993f1b-801e-30f5-983d-a5d72456d00e | -10.74201 | -47.70314 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01670f48-d0d5-3f56-924b-95800305957c | -10.74147 | -47.68513 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9b9a851-dd2c-320e-8e80-5c1475dca29d | -10.74036 | -47.69212 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be4b5654-186f-3576-ac6f-4acaf7550fd2 | -10.73926 | -47.6991 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f18f9a95-5a5b-37c3-b62f-27ecf725a9f8 | -10.7387 | -47.7026 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59b71046-73dc-3e07-9cbb-65cc714127c9 | -10.73816 | -47.68459 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05f799ef-3816-348c-b669-6e09762d7329 | -10.73596 | -47.67705 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7022c000-7160-31ee-bb69-0ba7a264594d | -10.73541 | -47.68055 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23a76ed2-36d7-36d5-92b2-45f102f1db7e | -10.73431 | -47.68755 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 787914fa-d772-3301-ba4a-53b238a1526d | -10.73154 | -47.70504 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4383a358-db6a-3f77-a5de-44519cdbf04d | -10.73103 | -47.64397 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eeb0d50-3135-3241-9f99-951d4b014339 | -10.731 | -47.687 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d79e18a-0143-38d1-9207-e8ee30ec5b23 | -10.73098 | -47.70855 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7781ed5c-1834-3dbd-8435-8e1ba29382e9 | -13.75562 | -48.31792 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3137b3a2-dba7-388c-8488-55f784d0c17a | -10.72823 | -47.70451 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| feeef846-c9de-3b27-b7e6-66c81263f467 | -10.72552 | -47.63591 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e999c30-76fd-36e6-8b4d-ef7e8f5ae986 | -10.72493 | -47.70398 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51e840b2-090f-357f-be69-3580910d77cf | -10.72439 | -47.68593 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c4b2ceb-08c3-3aa0-b8f2-bcf20c9649a6 | -10.72384 | -47.68943 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7022037d-c04d-39bf-b1b5-db6e1970d68d | -10.72329 | -47.69292 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4d16e034-4d20-326b-a766-1553760f0c42 | -10.72218 | -47.69994 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 926530a5-920a-32d5-8783-410756777e18 | -10.72164 | -47.6819 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3fa225e-e54b-3d9a-93ae-73a31b4a2403 | -10.72162 | -47.70345 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 169fdce7-349a-3225-9113-dcbbeaa26a81 | -10.72107 | -47.70695 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e446d1f3-05ec-392d-b750-864784ac3f6b | -10.72053 | -47.68889 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e29d31cc-6685-3e8a-b6fb-898eed312278 | -10.71998 | -47.69239 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b284744-f6f7-3ac9-8341-185ad6b10701 | -10.71887 | -47.69941 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 877ffb44-500e-3ffa-86f2-e341f8bd96cb | -10.71832 | -47.70292 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 478123df-06cf-357e-adb4-fbe31c4f9046 | -10.71778 | -47.68486 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 940bee41-1379-394c-aed0-1609f9773a38 | -10.71667 | -47.69186 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5e015dc-1c90-367d-8925-d0a2a1e7b6a7 | -10.71557 | -47.69888 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b164f0ca-c3b8-3f53-9199-0e707a877adf | -10.71503 | -47.68082 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d52dec71-1fee-3222-a2a1-699b127bdd00 | -10.71448 | -47.68432 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 697a2385-d363-3c12-8eca-5ec93cf9e051 | -10.24954 | -47.67635 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f98d64b-f769-3dcf-8a24-442bd50e564a | -10.24623 | -47.67582 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c32d3d4f-9787-3787-b747-33fc1c8d2de1 | -10.24568 | -47.67931 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2f07581-6ebf-33ff-b51d-52ef22bc6c57 | -10.23848 | -47.70329 | 2024-10-03 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17dad64a-7d15-3ca2-b862-415ed7be82c2 | -11.89804 | -48.31157 | 2024-10-03 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acf6ff2a-ec1f-3386-afe0-fdc15d9f3cae | -11.68112 | -47.81296 | 2024-10-03 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28059fe4-dc42-36f6-a77d-6cb2aa5c8f9b | -11.67726 | -47.81593 | 2024-10-03 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54aa48f8-26ea-3d70-b489-e7648e86d65a | -11.67396 | -47.81539 | 2024-10-03 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ad8e607-7e72-3b9c-975e-85907963896d | -11.48805 | -47.76371 | 2024-10-03 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab0768bb-5f1d-3dbd-aa06-10a7f71d4cc6 | -13.74845 | -48.32039 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d06a5cc-112c-3ad3-bbf9-18817f26d36b | -13.74522 | -48.29804 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47d1bc44-a26e-3ab2-90fc-f4a1600a17b3 | -13.74465 | -48.30159 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5f60334-e0db-35b9-a514-3bb0ff845e45 | -13.7391 | -48.31521 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 859b835e-49ef-3222-b506-a9de81be8282 | -13.7358 | -48.31466 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ba5a279-2559-3edc-8900-a97c93c6dea3 | -13.73524 | -48.31819 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17db7c6d-f261-3f3d-aee8-2097d5f83564 | -13.73307 | -48.31056 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6778300-4cfa-3936-99ed-25cacaeee5ec | -13.73194 | -48.31763 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c13e19ff-fdf9-34f9-a67d-8a484d2519b7 | -13.72977 | -48.31 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dd448d0-74a7-3b8c-84d4-ccd533e9bf81 | -13.7292 | -48.31354 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2edf9cf8-280b-3fa0-8b12-8a13c3985a48 | -13.72864 | -48.31708 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 08900133-6de8-3c57-8c93-edeb8c99ebe7 | -13.72703 | -48.3059 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd2e25aa-6f66-308c-ae4b-e0dee9d05058 | -13.72647 | -48.30944 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e202d990-fa0c-3a36-9a74-b4644cf1ba4d | -13.72534 | -48.31652 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 052d693d-2473-37c8-b8a0-6d0d2bc7a5d7 | -13.50748 | -48.61513 | 2024-10-03 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 498afb06-3a70-3e02-89c0-05d3d07eac3b | -13.50473 | -48.61104 | 2024-10-03 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10c263e7-487a-3ac3-9b24-bcb7f3a41f06 | -13.50417 | -48.6146 | 2024-10-03 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0857dbe4-5a7b-3664-9de1-0606da8ca3e5 | -13.50142 | -48.6105 | 2024-10-03 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6bc5351-a328-3ca8-abac-99c519c0f1da | -13.50085 | -48.61406 | 2024-10-03 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaf2a164-0de7-3633-863b-a662a44d4201 | -13.4981 | -48.60995 | 2024-10-03 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33432b25-2d18-3c25-8a32-b7b7911d6459 | -13.49478 | -48.60941 | 2024-10-03 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 899dd707-cdc1-3ea6-af85-2c5e18f34261 | -13.22968 | -48.6277 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a26efc8c-5929-3b3f-90d0-651f5ea3eec1 | -13.22579 | -48.6307 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 204a81b8-34f8-36fc-9dd2-0283e63f3580 | -13.22247 | -48.63012 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b02a6def-011b-3595-a1de-4c1c0a517e0f | -13.2219 | -48.6337 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6e2fb44-86d9-3ddc-99b4-b0346e79238c | -13.22132 | -48.63728 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1db4771-08cf-3d18-ac88-a300797bdec7 | -13.21743 | -48.6403 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d86e96ce-aa0f-3749-9f08-53634fb6e432 | -13.21353 | -48.64333 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 425f1b5e-55be-3bde-821e-712a3f18ca19 | -13.21181 | -48.54748 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1347de9-4a58-32a5-98e6-8bf67d4745eb | -13.21029 | -48.64249 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 373350dc-c9c9-3d4a-88fa-2408e4f0c8a8 | -13.20972 | -48.64608 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb2cb6d2-a900-316b-bd5b-950d4b7cbb3c | -13.2064 | -48.64551 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db7000da-7a6f-3c0b-962f-af6e3e6e9683 | -13.20583 | -48.52094 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README92.md)
