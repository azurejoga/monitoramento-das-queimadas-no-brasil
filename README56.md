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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f2f6b3d-6823-3ea3-8f4a-41228b4319c9 | -1.14278 | -51.67409 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f81f6b3d-7583-304d-a2c8-0f0e159265ac | -6.24347 | -39.85803 | 2024-11-30 04:40:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57af715a-389d-35b7-916c-fdc09af248f5 | -3.35108 | -46.29865 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb47e648-31c3-3743-b980-6dc9e9aa251f | -4.47862 | -48.19368 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b60706b8-593f-31eb-970a-0e495af57650 | -3.20384 | -48.58693 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3dd774-c1f2-3555-9ea6-57dcc75f82ef | -0.95418 | -51.65524 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5efc5d86-91d1-39ee-abfd-cd26d6656f86 | -2.01954 | -50.77987 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3eece002-1f79-352d-8eca-032350024a80 | -3.43328 | -50.40385 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02847725-9f61-352b-bf2d-1c340817a574 | -1.20801 | -51.73832 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b7f7ec9-38d2-39e5-a32c-7c1f8821d3df | -2.98835 | -53.7467 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c59b4b7f-b39a-3a83-86a4-88894bc48ef6 | -1.56698 | -52.00496 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec3e8119-5176-38a0-a0ac-42adc8f17b8d | -3.11193 | -53.8056 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de6d31c1-2b36-3b27-8caa-aa9d9b8bdad3 | -3.03196 | -48.51037 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1734b4fd-9603-3c7d-a639-4d99581f0811 | -1.98413 | -48.66676 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d910e62-6a68-34dc-9ba3-af7baf60aa8f | -3.25272 | -50.61862 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3da7d749-bbd9-31b7-b7a8-242762965c35 | -1.27641 | -51.82902 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d89b5a9-a93d-3ba8-8b54-d241fb7bde77 | -2.31269 | -47.90897 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da6374ab-afae-373a-8a13-72f467b0a9c2 | -2.62145 | -46.07255 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baf602aa-44e8-3046-a085-f5c6a96aee2b | -3.45657 | -54.56826 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| be991c63-e685-36ae-8215-cd7543d88018 | -3.85752 | -50.14725 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 639a9322-4759-35d6-adb7-f5ce9e8ed6ef | -3.40155 | -53.02878 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 11e1a46b-2ced-3dcb-b778-e4e3a4e21037 | -3.73804 | -53.73594 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 946422d3-0d60-3357-9d57-7831af06467a | -2.37063 | -50.40455 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dc6c72f-273d-3fe8-b069-93b74dd8fc30 | -1.72651 | -52.48411 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd42e544-5360-3627-b91d-1a8229733b8c | -6.13951 | -43.95769 | 2024-11-30 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 087cb3af-8725-3836-9f1b-a24d36c1f9d9 | -3.67718 | -47.12816 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 23866899-4385-3abd-993c-a6469676335b | -3.79439 | -49.94373 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2dd1a8a-4a42-3f33-9e46-e3da98423f26 | -3.58482 | -50.34319 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b985eca5-e709-309b-81b6-3d48286d73d4 | -1.0953 | -53.36444 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26253aca-d053-3003-b9b6-56b251510da2 | -1.97249 | -48.67191 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37fcf476-f180-3727-b5dd-dfbe54483754 | -4.1713 | -48.62069 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fa416f5-e78e-3e32-be24-28b56856a517 | -3.19142 | -48.57727 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1822de88-1c49-3330-bbb8-0d980f2aee7c | -3.29574 | -53.83537 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c59f822-0990-363e-922f-1c71e17cc014 | -3.2776 | -50.59277 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c36aa8c-a402-3b0c-b923-5dc0e569cdad | -3.29684 | -53.82851 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad191555-0ba3-30ab-94ed-d4f09c132e5d | -3.09949 | -50.36275 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6728127-e910-329b-a247-0b88f75edb56 | -2.72055 | -46.30011 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c56c225-0cb8-3d27-af83-9bfafbc6ad8f | -3.39009 | -53.27068 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3fdd7c2-da9f-36d3-a8dd-935cee3cb8f4 | -1.08978 | -53.64008 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f35d4f3f-8aa2-330b-909a-c2e09052af2f | -3.96478 | -46.99202 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c17cde8d-889a-387a-9aeb-e741065debe6 | -4.8828 | -41.30785 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e4f1c67f-c572-36cd-b772-e7e08d7e0beb | -2.01938 | -52.08354 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7b2c89a-0586-30a6-88e1-763131b276f4 | -1.69182 | -46.7851 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 8d32ae19-9847-355a-8e6a-c2fcd62f9dd7 | -3.37336 | -50.17931 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 453bc2ea-4878-3759-b9b7-1dba09ec75a7 | -3.68273 | -49.57047 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9207d3af-16ee-3097-9e6b-f72ac39569a8 | -3.20647 | -53.8427 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f4c257-9393-385b-97a2-e81e1da7a6b5 | -3.90059 | -46.49477 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e29f2a9d-ee14-390d-9fcc-0442bce9e79a | -2.91252 | -54.11681 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae0b7d91-cbe9-3b0f-965b-174217f7c38e | -4.15699 | -44.2715 | 2024-11-30 04:40:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 111b8071-cf04-38c2-885c-61712adf7798 | -3.83719 | -46.60508 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4925c361-4f76-3d46-8e0f-b9c0eb65b099 | -2.26178 | -53.46008 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16bd254e-56f2-32e8-b414-9680942bf8b9 | -5.98278 | -39.95449 | 2024-11-30 04:40:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef26f4e5-5693-31f9-ba26-2fc15a873fe2 | -4.04373 | -46.84058 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e92a53cf-95cb-33c9-8d8e-76b9836bac1f | -1.36111 | -55.17713 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcee7f12-4678-3ee6-883e-db62a6604e28 | -2.53356 | -47.33595 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08c2cca8-fdfc-35c4-9e1a-7e904dfaf2b7 | -3.31603 | -46.17285 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0558a18e-bc63-321e-b68f-3c6edbe5d0f7 | -3.96442 | -48.08905 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36103b6d-98b5-3efc-a4ce-d2d4b6eadd89 | -1.40643 | -51.58999 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f654f433-cf43-3df1-97c3-d349a23ea734 | -3.48056 | -53.80918 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92a73971-0312-35f7-bae3-adf66f817bea | -2.66243 | -48.78696 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2d91c01-4aa3-39d0-ac37-8c9707910801 | -2.39529 | -50.49013 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 026e288f-65b4-3fc8-8abb-d4fc81096b56 | -3.2643 | -50.43575 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbd12157-2ae8-30d4-b9d7-e8273069bae1 | -2.61392 | -46.56422 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4be8443d-d6ae-3d99-927d-702a61a10467 | -1.94349 | -48.70607 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5716d0b7-f051-32a1-9bf9-b9580cd0fdaf | -3.83773 | -46.64883 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e13c2c6e-a3e8-3d99-ad17-bdab5dc8c852 | -3.27001 | -46.44811 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6de7e22-6883-3824-b2a1-827a26b90f0b | -2.02166 | -51.19723 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e772780c-6e68-3641-aed0-856f0f1e72ee | -1.00419 | -49.93145 | 2024-11-30 04:40:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7142516-91d1-39cb-acb5-77ec44014e37 | -1.83147 | -54.52496 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 662ed0a9-2304-333c-8428-7688ee07aa7d | -2.11877 | -50.59729 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e213418-a0b1-35e6-ab85-7f43e985a6ef | -3.04132 | -50.97796 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b392d85-71c8-38b9-91a1-b08eb690f4fa | -1.27125 | -54.55497 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f2a6d820-70c4-395f-814c-68160ca50af6 | -3.35765 | -49.75718 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 02b80fa1-d5b3-36b0-9af7-3f6198f0495a | -2.87476 | -48.09945 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 597712fd-0989-3472-b09e-0b81e588e067 | -2.42874 | -50.43206 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d35676d-9bd7-3e0f-983f-f6cfd1ca8a47 | -2.92799 | -49.48048 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 659b9792-1b28-39bf-88cd-b6e99075e4ad | -3.14771 | -53.82673 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aedac1de-4c48-35d7-8829-733a3d41d5bf | -4.06696 | -49.07038 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0defa2ba-a8c3-393d-8941-8ee1d84faac0 | -1.44644 | -54.52258 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 206d0729-4d2d-329f-a467-56f94a01e9c5 | -2.66797 | -48.79485 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e833cf97-5973-3acc-a28a-3e3d9491a367 | -2.42698 | -48.54958 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e62a46-1072-3695-8f03-9d3ef70d6b78 | -2.41646 | -50.31186 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7338a56c-24c5-39ca-9f70-b7e5528dcbe8 | -3.59599 | -49.99467 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e44c85c7-940c-3677-8c90-c73c7b0d2794 | -4.03549 | -51.02071 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d34b130e-b0c3-361b-89d6-28d8e9f4bd66 | -3.73286 | -54.23415 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8b4333c-426a-3f15-8bea-69c607e7734d | -3.13331 | -51.04201 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8089b28a-f99f-3fdd-948a-1c9630afda37 | -3.39129 | -50.32065 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf806fa1-0beb-384b-bd0a-61096f635e38 | -1.61114 | -48.02365 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7122f917-9728-3dff-8c10-54b0c06dac62 | -4.05359 | -46.82251 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58703ac7-dc7f-3ca8-a22b-02ba8c0b96b5 | -3.33721 | -46.69379 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 840847e6-ba61-3c8f-8295-a1e8bd5c91d5 | -2.23102 | -46.40199 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b248ffc-42db-341a-a3b7-b636b765aa11 | -2.69449 | -51.98886 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e4918be-9925-3451-a29a-bb3df64d0c0e | -1.31052 | -51.73145 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 732ccf34-cc6a-336b-84dc-7c6936a58c94 | -2.02013 | -50.77613 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fb0e8ef7-b938-3fd8-b567-f44f3651f921 | -2.83689 | -54.12006 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ea3334f-8ccf-35dd-92e7-da8441dee4d1 | -3.28456 | -54.16587 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbe51a84-c37d-3c38-8477-dcd3afa68a9e | -2.83388 | -49.60427 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 879c5e0f-fd9e-3007-a709-f80ddda33d0a | -3.93334 | -46.71088 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bdb90cb-9d9c-38d3-aa64-0491421a1d9f | -3.2821 | -50.60831 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d87c0082-67af-355d-8cca-531b431da51e | -3.60063 | -54.42908 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README57.md)
