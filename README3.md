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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9213321f-ab60-3255-b2ec-6e384d81c645 | -5.03572 | -43.62087 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ced1e707-0e6f-306f-aac6-1bbbf2616109 | -5.74956 | -43.39705 | 2025-11-04 00:34:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9c526007-0d8f-3c4e-bc2d-f871720e8ab2 | -4.46805 | -43.22807 | 2025-11-04 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 611f3203-b2f2-3eb3-8e69-3bf40f3d4b46 | -7.96435 | -44.50897 | 2025-11-04 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a285b8c9-8843-315e-862a-45c51a479592 | -5.24211 | -44.20919 | 2025-11-04 00:34:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| b6712c1b-752d-38ef-9fc8-08add24ede0a | -3.43823 | -42.54403 | 2025-11-04 00:34:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1664102d-0784-363a-9baf-89a2edc90215 | -3.9178 | -47.70171 | 2025-11-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| ac66df76-dd51-3f7b-953c-ce9a8445c3c6 | -5.32324 | -45.38445 | 2025-11-04 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9fcf5971-4061-35ff-bc04-18b288679c4b | -5.93198 | -41.3285 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 2c0763f0-38da-3185-bb4b-aef744cb7a9c | -4.87787 | -47.53982 | 2025-11-04 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 85f3eac9-3a03-3aef-a017-86754f93a264 | -4.25121 | -45.67837 | 2025-11-04 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cbe7c710-8e16-35b7-ba21-6f2667b59037 | -5.06479 | -45.90572 | 2025-11-04 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 34.1 |
| a96e8ba2-e6d7-3f51-bf50-233a0c2a1855 | -3.48732 | -50.02676 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72d383cd-361d-3db4-abe9-82162cf8188f | -3.77552 | -52.31899 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a09ca16c-8c3b-3227-9152-5d4e3e06da9e | -4.86814 | -47.54125 | 2025-11-04 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a4931084-d86e-391d-9b66-409310a802d9 | -3.0164 | -51.08828 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2517706b-707a-39ca-a755-5cebf2dbf763 | -2.59981 | -47.35529 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4691b233-5cea-3675-904e-8eecb455fa8f | -3.46485 | -50.3341 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0fd96488-a850-3c3e-bcd7-4c41b8538081 | -2.31692 | -48.588 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f13662c6-471e-331a-9052-97f9aac62718 | -3.04407 | -50.28281 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b9363b97-48b9-398e-b554-bed84a291912 | -3.43572 | -51.52087 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 674b0370-98dc-342e-8de2-b23fb6b0cb7b | -3.2434 | -50.79576 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 74eca677-e966-372c-a231-ac5396eb01ab | -2.20161 | -48.35837 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 30d13792-9c7d-3a73-bea9-451cf4cfc2f9 | -2.90359 | -51.46167 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9e6c3df7-732a-3643-8f83-b218f0d3afd3 | -1.14283 | -49.20464 | 2025-11-04 00:34:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d8ccddb4-8528-3ea0-87d2-6b66ce915d6f | -3.44256 | -50.23824 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 4b95cd12-76bd-38d5-b332-c6daec62577f | -3.45507 | -51.05901 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 33806745-cb42-3ad4-aba0-4b97810a6245 | -3.49076 | -50.4562 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 32ff5ac5-df31-3226-8a63-78f6018396e7 | -1.22817 | -49.15687 | 2025-11-04 00:34:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7de0214b-a4f7-37b5-93f1-496825691174 | -3.40741 | -50.18005 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f1913b1e-987c-3a86-a84e-0a67f8c83347 | -3.04383 | -50.34593 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d6dfcf94-b9b9-32af-8ccd-03259747e410 | -3.02129 | -51.38497 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8aba1ba2-dbb2-3c0c-92d2-ea6e001e870a | -3.02252 | -51.39387 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d9dcfb04-78fb-3ddc-b35f-769f76c7c244 | -3.00506 | -49.47469 | 2025-11-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3098bedc-51b9-3dc0-ba8d-f9cafb7963b8 | -3.24977 | -52.91197 | 2025-11-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3c8a4356-8434-36aa-9fa6-613813497928 | -2.29378 | -47.86472 | 2025-11-04 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d38bca8c-a0e5-3e6b-ab3d-1afb89592362 | -3.24461 | -50.80455 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f491eb03-7ceb-3d04-a9ce-093ba9c23c8a | -3.23579 | -50.80579 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 89b5f53b-520a-318e-b043-b9622916299c | -2.31548 | -48.57787 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c88cb248-2aee-3605-bd6d-de0e5a35a88d | -1.9699 | -52.11382 | 2025-11-04 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4c43d14d-396e-3aa1-83e3-b8bff25c2226 | -3.43371 | -50.23949 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| eecbc8d3-ce78-3113-89a8-3c2404328f25 | -2.71949 | -48.34937 | 2025-11-04 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f301efab-1f74-3ec8-b1d4-b2fca3fd7c07 | -2.3775 | -47.73193 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 71f7341e-9c5c-3454-bfcb-d73cc5f839c3 | -1.32292 | -46.75 | 2025-11-04 00:34:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| dca00ae9-c7b5-3b47-8eee-12754951100d | -2.96167 | -52.49643 | 2025-11-04 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a1b3eac0-c333-33d4-86a6-6d08a69b3e15 | -2.9882 | -48.70506 | 2025-11-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 61c3d651-7bc3-38f2-a358-a1d964c9b22f | -3.23457 | -50.797 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 84f1d7c7-9b57-3618-9948-10f65e997190 | -3.01364 | -51.39511 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6d32a24e-0a15-3758-9506-259f8e6683ee | -2.8438 | -49.84114 | 2025-11-04 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b2976eb-c695-3840-9234-a2289a873c51 | -3.46337 | -52.87391 | 2025-11-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 77ddf94e-6bc1-3aa2-aaa4-ac54d7c00440 | -3.34938 | -50.23029 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 080bd69d-ae2b-3df6-8977-bf393dfe6f7d | -3.44896 | -50.21931 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f37836ff-72b6-3353-bbde-b35f72b846aa | -1.98126 | -54.17081 | 2025-11-04 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a5b4e9c6-f112-3faf-a28c-688a89d16d96 | -3.1066 | -51.20419 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e5824ba-1950-37ec-9ad2-3154beaf5a63 | -3.10782 | -51.21302 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da96dbe0-37b6-3cda-9954-43bf027283a8 | -3.66514 | -51.71571 | 2025-11-04 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd35808f-b238-3acd-92e7-ca01f1f451b6 | -3.49198 | -50.46499 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 2199930f-b79a-30af-b65c-bffa1cae65ab | -3.45385 | -51.05019 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ec55eccd-1bc0-37b3-b851-4ee8e4a2fbe9 | -3.43448 | -51.5119 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b0c84746-8ec4-30e8-9ffa-fde1193ec9d4 | -2.31107 | -48.58479 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dcd06ef8-3b1b-3050-8cfe-148a4a9bf07e | -2.97888 | -48.70642 | 2025-11-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ad672de-aacc-34d3-851f-383a2d401a68 | -3.44244 | -53.25925 | 2025-11-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 84a6e9a2-16bf-32fa-ad12-d7f1e3d270ad | -3.44734 | -51.47361 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| c91ea5bc-a47b-3038-b926-472ab97b8140 | -3.01592 | -48.0466 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a0889227-d6ff-3516-b910-07f1da68fb76 | -3.45838 | -52.88122 | 2025-11-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ca22882-f182-356f-817a-144e622b8774 | -2.82112 | -48.24821 | 2025-11-04 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 585ef7e4-e999-33e5-b9ec-36fd6d50d137 | -2.32782 | -48.59679 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| caae8d57-9a3d-3fb7-ad8c-f5b258e8fd13 | -2.32638 | -48.58666 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ed4f524a-fb1f-3cb8-95eb-172af6b40a06 | -2.84255 | -49.83212 | 2025-11-04 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 612bcc08-3165-3b09-8898-f4ff2185cc5d | -3.45697 | -52.87111 | 2025-11-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 49b8d4a3-07d8-3755-bfe5-3ae5b88b1e62 | -3.59588 | -55.44111 | 2025-11-04 00:34:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 770739c9-0ab7-3d1f-b8eb-f8d9a03229fa | -2.37593 | -47.72058 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e99b642b-bbb6-359e-b055-aad458678ba8 | -3.29133 | -50.20237 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c12de021-af62-39af-a425-edf57c35b2c5 | -1.76354 | -53.55342 | 2025-11-04 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0d5364c9-0a23-3050-b89a-cfe1f241a131 | -3.14791 | -50.1715 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 86aa1000-fd8b-3949-b3af-6556471336fb | -2.36753 | -47.73331 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cfa6a1af-4650-3a03-b83e-0106438cb6ba | -1.96864 | -52.10472 | 2025-11-04 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 98d3b859-7909-31fd-aab2-cb96bb6ec9a0 | -2.31386 | -48.60503 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fc812c3e-0f9a-3e6e-8a5f-3270cbbdd939 | -3.4461 | -51.46468 | 2025-11-04 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 02bd53c7-cfea-3437-8611-b8b60259882d | -3.3506 | -50.23913 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4a210840-9352-3fc4-99d0-2e817f202d0e | -1.98249 | -54.17591 | 2025-11-04 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 19474676-4e8f-339f-9937-4349a4edc0b5 | -2.31837 | -48.59811 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 067eb158-06bd-334b-82df-b1d91c0a8154 | -2.60217 | -47.36066 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 297e0cd0-89a4-34b1-9180-4876ebb55f34 | -2.37724 | -47.72565 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 1039e8e2-3237-3b43-8e6e-b77cca2987c6 | -2.31246 | -48.59489 | 2025-11-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 08e05fd3-c711-3326-8d40-58a352f68ffc | -2.62062 | -49.23044 | 2025-11-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 5bcc2088-5185-33b6-be91-ead1a9554066 | -2.50093 | -45.97445 | 2025-11-04 00:34:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8fe90277-7346-36ea-8a21-aeb4d03b97bb | -2.37561 | -47.71433 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 2eca98e4-5079-37b2-9520-2f31aa39a100 | -2.36596 | -47.72199 | 2025-11-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ab973ef0-3c65-3cf2-ac7e-a0ef663f2a7d | -3.01762 | -51.09711 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6f8224dd-95e7-3f45-82eb-140a446e7245 | -2.30604 | -50.47147 | 2025-11-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 119e135e-ce2d-309c-a3ea-cae142462eb9 | 0.98275 | -51.21199 | 2025-11-04 00:37:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bd2a8b58-f75a-31cd-ae5f-3aac3052a78d | 2.61071 | -51.6458 | 2025-11-04 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bbb3032c-5f22-34c5-b814-005918413e40 | 0.97025 | -51.23717 | 2025-11-04 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76988aea-f602-36be-aff3-46ebdd169f26 | 0.73214 | -51.49599 | 2025-11-04 00:37:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4baace0-1384-3bb5-9ea5-c5822b571c52 | 0.98153 | -51.2208 | 2025-11-04 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 358fad0d-e1b7-37dc-a5be-4c1a61028dcb | 0.9602 | -51.24474 | 2025-11-04 00:37:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 98d0956d-b276-36c6-9709-cb3e68582c7e | 0.97269 | -51.21957 | 2025-11-04 00:37:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 5e64b5d7-c2df-3217-8ea0-df6aa39a067f | 0.96903 | -51.24598 | 2025-11-04 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 33f8e9aa-cb0f-32cf-a333-27ad7bd043b1 | 0.97147 | -51.22837 | 2025-11-04 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 21.2 |


[Clique aqui para ver as próximas entradas](README4.md)
