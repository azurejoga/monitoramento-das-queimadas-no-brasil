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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f0a4e23-f63c-3266-9605-2c21603b9d59 | -12.70735 | -54.08038 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91358aeb-8aeb-3eca-a15f-e888ccc701fe | -12.70344 | -54.07982 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06ce23ac-d815-31b1-a127-17c86868ec96 | -12.69769 | -54.06359 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8cec46b-4f68-361e-a123-42f88865ae14 | -12.69563 | -54.07868 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20101bba-c0f2-3700-b5a5-8950e1fb5378 | -12.69309 | -54.06805 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab824451-1e8c-31d6-a8bd-1bd4c85becc1 | -12.69241 | -54.07308 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d85524b3-acff-3d6c-bce6-1e1c19348907 | -12.69232 | -54.07062 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65b00f46-704c-3e09-be6a-26fe527e6fd5 | -12.69172 | -54.07811 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3193f456-95bf-353c-ae97-2cd324d0aa13 | -12.6916 | -54.07565 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83d0b55e-4268-3e03-a3ae-96e5093ebd36 | -12.69088 | -54.08065 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fc0b081-beca-3d74-8768-6c3f66adb906 | -12.68954 | -54.03422 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0d8b21-c2e1-3f1b-b383-2fcc1a739794 | -12.68882 | -54.03928 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1452d324-4284-36ef-b493-1d26ce3f35a5 | -12.68528 | -54.06692 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 52fd70c9-9c09-3c48-8f34-d7f429cb8917 | -12.68522 | -54.06448 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 952aae62-f6fe-35d4-8cae-498a1d32b5de | -12.68459 | -54.07193 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f80cd026-e556-300a-a66f-ee33e943fad2 | -12.68451 | -54.06949 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a8c743a8-1283-30c9-875f-05f13309f71e | -12.68137 | -54.06634 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 832eb0c6-4895-3704-8d41-e4855b8abf43 | -12.68069 | -54.07136 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f9a2743c-b514-3f72-9dbc-f51f2934bffc | -12.6806 | -54.06892 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1ee317f4-4e8d-3999-9234-b098c1a87548 | -12.65191 | -53.21049 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab3b6a0f-846b-3e1b-ae65-a76395e348d7 | -12.60464 | -53.28056 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc9a4abb-d9b0-3ab0-aedd-3707f344031b | -12.59552 | -53.16019 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 886eb505-de55-398a-8b3e-3479636920b4 | -12.59362 | -53.15631 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a6efc89-688c-3082-b304-1113a438dbee | -12.59309 | -53.1601 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3ea7010-3426-3ff0-84bd-f8a339adbeb5 | -12.59189 | -53.1558 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf4a8fa1-9816-3e54-9ca7-7b396cea98af | -12.59139 | -53.15961 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2659d420-2705-3c20-9e82-10f839c9c08c | -12.58949 | -53.15573 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd03ae10-b460-33a3-95a3-dd4ca4a87ff5 | -12.58535 | -53.15516 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63957803-22e5-3b5b-a99e-fb876983e9b0 | -12.58482 | -53.15895 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff23712a-a1e8-3853-afb5-e46739ccaf4a | -12.58068 | -53.15837 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54de2ffa-9344-3868-a49e-eb1c81584c12 | -12.57655 | -53.15778 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be90302d-2bc2-3a1b-85c1-1004116458c1 | -12.56224 | -53.50266 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a8aea80-2837-3007-83ad-30bfd2e23d08 | -12.5582 | -53.50209 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0313105c-26cf-3ed5-be42-cde5bbd9a2a2 | -12.55771 | -53.5057 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b229d71-a3dd-32af-879e-6f445387a4ac | -12.55059 | -53.49734 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a90b0248-6e4f-3b1d-a29e-1100e8588c2a | -12.5499 | -53.49711 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c51a50f1-07ee-332e-9fce-e5443596ea7e | -12.54586 | -53.49654 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff81f745-3cda-3963-8efe-042f347836fb | -12.53468 | -53.15571 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54840cd-87e0-341e-a102-fe56beac184b | -12.52539 | -53.16211 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1fd1169-6175-3f99-ac73-a3fd780ca2d8 | -12.52386 | -53.17342 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cc553b7-3bf6-352b-a78e-37e333e1f9a3 | -12.52075 | -53.16529 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef39c5b7-939b-308e-9337-564c5db249c2 | -12.52024 | -53.16906 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e177047-9e75-3b94-8e1f-624aaf594b09 | -12.51973 | -53.17283 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83f9778c-7d2d-3826-b049-a89ee94a50fb | -12.51906 | -53.4817 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98cc357c-a392-3882-9c74-2666b6c88f2e | -12.51509 | -53.17602 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ca76f2-4ed3-36f9-adc7-95ab9efd5072 | -12.46693 | -53.47071 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec10e1c4-f536-3c2a-8d5c-3a82049287c1 | -12.86151 | -54.00536 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2874ea15-3a3f-3796-8e84-ffff5213b9ad | -12.82934 | -54.00597 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f4bf9d3-9173-3db0-8c7a-7c002876e52f | -12.82612 | -54.00025 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc455d23-d2ef-35df-8dd7-234497885d5a | -12.82541 | -54.00542 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a8342d1-f99d-3c81-b86a-0e57263be8ad | -12.82218 | -53.99969 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad1b3bf4-a519-36c1-9b8b-d080add267c8 | -12.82148 | -54.00486 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9434b22a-7e5a-38f0-aac7-61b80b3cafa5 | -12.81825 | -53.99913 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be4a7c43-2d4c-3b29-83b4-fbef6f310d07 | -12.81755 | -54.00429 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e42873cf-c7c2-39ed-bd87-b012348db7e4 | -12.81432 | -53.99856 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 66e19480-598e-34a4-89b0-c76127da9209 | -12.81361 | -54.00372 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f5c86b06-0a44-3949-9093-ee83d679550f | -12.81292 | -54.00884 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 711ae6c7-5769-3da2-900b-9c41d70cf4e8 | -12.81098 | -53.99712 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 63f4d69b-702c-37c1-a8d8-bfdf9ee488ea | -12.81038 | -53.99798 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f993dd18-e2b0-337d-9ef3-e3084ea65f08 | -12.81025 | -54.00225 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 235376cf-86c2-35e9-9aa4-67247ffbcc47 | -12.80969 | -54.00312 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6a148214-dd20-39a3-9c64-f5adea720297 | -12.80951 | -54.00737 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31edf9c9-9427-3ee9-a4c1-ca4e60351aee | -12.80899 | -54.00825 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1c963ae-bfad-3224-b464-11cadf066899 | -12.80646 | -53.99738 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1a16d641-c3aa-3948-ba34-d9edbf17bb36 | -12.80632 | -54.00166 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 139ebc20-f396-3d13-817e-4a82f48808d3 | -12.80576 | -54.00252 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 657132c7-9e65-3348-b03f-0e0e0d2cfb8d | -12.80559 | -54.00678 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 49020e6d-2077-3268-b6fb-ae7659f8c071 | -12.80506 | -54.00764 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5c2a13f5-d8ea-34c1-b74e-e4d07f91a53d | -12.80239 | -54.00108 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8110b018-6e86-356b-afb7-370d343e9bce | -12.80166 | -54.00621 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 30178e36-c09c-3a5b-9380-abd3239e6f9a | -12.80113 | -54.00708 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ba59776c-1010-3182-82ca-bbe6af6458cd | -12.79773 | -54.00566 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a517a64-7d2f-3d62-bccd-3579212d8b38 | -12.7972 | -54.00652 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 0a647402-09d7-3fc6-8f57-761868c435a1 | -12.79397 | -54.00081 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 4b730dfb-a8bf-35ff-9765-b991c00bc2a7 | -12.7938 | -54.0051 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 13b94d96-6b52-310b-b260-1e9637e09491 | -12.79327 | -54.00596 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 55609356-3826-3954-915a-600acaa41e69 | -12.78987 | -54.00454 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 51897a5b-5e2f-3e5d-81cc-6d2f3fd3c286 | -12.78915 | -54.00967 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3205fa8a-d3eb-3e84-93d1-f3199b6c5038 | -12.78594 | -54.00398 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4aa64f9b-3af7-36aa-a7eb-859adeccc1bc | -12.78522 | -54.00911 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 81ee1cad-8755-3d90-9210-67947ddd1a50 | -12.78201 | -54.00343 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 81701bda-e65d-3b90-8fe1-72c5ad2a71ad | -12.78129 | -54.00856 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 96e58a6e-240d-3f96-97dc-819c6fa4cf68 | -12.77808 | -54.00288 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5907cf4c-7e24-3611-b96d-b4c7e2455bbf | -12.77736 | -54.008 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c05a7e08-521d-3573-a7b4-6d1d82337d2b | -12.77487 | -53.99717 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e54be66a-2182-3b9b-bb27-20634a33f96f | -12.77415 | -54.00231 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e7552bae-9c3c-3015-8e96-abbc223211d6 | -12.77343 | -54.00743 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 340cb43d-dc73-3165-98b0-6d765c2a3b3e | -12.77095 | -53.9966 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71b6e5e4-6648-35a3-94d4-3660f64c8050 | -12.76951 | -54.00685 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b97e845-22c7-3567-a75d-f514605a3b5d | -14.77916 | -53.87051 | 2024-09-28 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a150027-dae1-399b-9162-b4d7103d51e4 | -14.77869 | -53.87414 | 2024-09-28 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0d2fe6d-a824-3e31-8074-20ef0e97b570 | -14.77747 | -53.8518 | 2024-09-28 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6a84f86-23ef-3968-8b3c-a66f1ea51773 | -14.77699 | -53.85543 | 2024-09-28 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af2c37ce-43d5-3e5f-a5ed-63fb5f2f5aaf | -14.77652 | -53.85903 | 2024-09-28 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31362926-8afc-3a8d-917e-9cf2d8643935 | -14.4285 | -53.16345 | 2024-09-28 05:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31f91f2f-a16d-3c04-adab-7d5b0c39129f | -14.42808 | -53.16207 | 2024-09-28 05:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4080fb5-1f99-3a8f-9f45-b4eeb6557b3d | -14.28756 | -53.38631 | 2024-09-28 05:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2da8a7b3-f849-3749-8ff1-6b5d3d5b7f18 | -14.28605 | -53.38648 | 2024-09-28 05:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acb2a64a-2992-3288-a316-314f85f22aca | -15.68065 | -53.91261 | 2024-09-28 05:10:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1bebffe-fcbe-36de-9a84-6f19a763d408 | -15.68014 | -53.9165 | 2024-09-28 05:10:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README81.md)
