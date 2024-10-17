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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33beb210-04f3-35c9-9cdd-696d223b1bb8 | -3.57634 | -50.57486 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ebc1bc9-5eb0-30f9-83d0-da737ae20d75 | -3.57576 | -50.57431 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1534977a-8096-36d5-b3c2-6173364a6dd2 | -3.57329 | -50.56275 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59b62ead-bd4b-3e87-856e-902db5a40bcf | -3.57139 | -50.57391 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d2f1e12-1e58-36df-94f9-da15f95a5d88 | -5.3241 | -50.8486 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6b9b085-0e75-3e72-a333-92fa22e75521 | -3.50197 | -51.58936 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb520ab-ac7f-35b6-9f11-499690e8580b | -3.50143 | -51.5927 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9068e46b-db76-377f-a92b-f78041882678 | -2.89283 | -51.68502 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3120d9ca-7fc4-385b-be0f-90f209028f92 | -2.89225 | -51.6885 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e7671859-0f94-31ef-ab73-c0420e268ddd | -2.89166 | -51.69204 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c69138af-0ffb-3f39-abe5-6502cf71c739 | -2.88683 | -51.68757 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86f0e0c4-a3c1-3cfa-a0af-3171ba122731 | -2.88625 | -51.69106 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5ff1deb2-2033-35c7-8db5-42863f96a9d9 | -2.88198 | -51.68325 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 052b2db5-647d-391b-9e53-f5e16fdc5118 | -2.8814 | -51.68672 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3380ead3-8755-34e1-8dfc-97ccc0aa9aad | -2.88082 | -51.69021 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e24d69f-8fc0-36ea-85df-2e75cab2d6d5 | -2.80478 | -51.60173 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b8c517-18aa-3912-adb8-8c63a314283f | -2.79883 | -51.60417 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edaef3f9-8fcc-3633-a997-43d82ac9e041 | -3.67071 | -51.02468 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27aee9d9-3e77-3fe9-bcc8-a7a246d8b667 | -3.59677 | -51.01176 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99d01f4a-5607-30d9-b1e9-78ec6d450e7d | -3.08498 | -51.21148 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28ce0f33-0d5d-3354-adcd-f9e3fcdd3d5e | -3.08445 | -51.21462 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e58aaf7-95d7-3924-95de-9561df31ae46 | -3.08393 | -51.21775 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9441c5e-b5d5-3183-8942-3e2be82054f6 | -3.06356 | -51.0522 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46c4be56-d326-3f9f-82ae-20c9744841a5 | -3.06244 | -51.05069 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd81cec0-b4b7-34df-91cf-9c1e13326f8f | -3.05944 | -51.04508 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff935947-178e-3631-bfb8-895581100c20 | -3.05829 | -51.0435 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e914e407-3aa7-3310-b4c2-653ec8c22495 | -3.05778 | -51.04661 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616c3314-76e0-3192-82f7-459725e17abf | -3.04075 | -51.15502 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f11bb9e2-d9cb-3e38-8678-a9f5eb9dc672 | -3.03401 | -51.22629 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8345a78-d8f0-34e5-9aef-3865d42ac2b0 | -3.03367 | -51.22839 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 861e60c6-5cd6-3efa-bc30-363fb7b93709 | -3.03347 | -51.22948 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9563923a-ae68-3c82-b4b7-52daa066fb81 | -3.02843 | -51.22747 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e6959c9-7c62-31be-9e6f-77d08e853f13 | -3.02823 | -51.22858 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64cee18f-5742-384c-b52a-7a040f3993f5 | -3.02791 | -51.23068 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb1ca55a-62d6-3414-8114-c239ab8163d8 | -3.02769 | -51.23176 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06a3cde7-7fb1-3348-9e5b-15399488efd8 | -3.01417 | -51.34876 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a6f4a1a-7ec3-387e-ad21-86810b111238 | -3.00888 | -51.34786 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53bcae52-ca68-3fb6-aa1c-892a5d9c156a | -2.99512 | -51.00732 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ed45d1b2-6a3c-3866-b784-c19acfccf65b | -2.99461 | -51.0104 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ea2fc1f-9ec1-33d4-874c-61fb51b5f74b | -2.98995 | -51.00644 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b21fd201-e4b2-3304-aa22-9f48ddc9d99b | -2.98944 | -51.00953 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c5aeab7-46d4-3100-8fd7-031dfa91392b | -2.98892 | -51.01263 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53757e7e-800a-35f9-94fa-e9052f597aae | -2.82136 | -51.33784 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e479e961-4054-311d-8f39-c6f55317bbe5 | -2.82025 | -51.34441 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47d027fb-b988-36df-b998-f632541af3e4 | -2.8197 | -51.34772 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bd41e91-b662-30eb-9af4-3e971d7a8fbe | -2.81495 | -51.34354 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4e1d360-157d-30f8-8808-dc0302708d0d | -3.50691 | -51.10696 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a82fd05f-0216-389b-8d3c-a435fe0db12f | -3.50637 | -51.1101 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8a2e5ff0-68db-3118-b620-2816aab57181 | -3.50584 | -51.11325 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dbdf880b-5894-3562-8730-3077e2dbfccc | -3.50174 | -51.10609 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c4555aed-831c-359d-9590-003bcb48ffb7 | -3.50121 | -51.10921 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4a7f6809-f1c1-300c-a7ad-e0561b267c83 | -3.50068 | -51.11234 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a3ae9642-4989-3206-a0f6-722d16fc028e | -3.49711 | -51.10214 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fd79443-6a0d-3a68-82fc-d7ab0f19a86a | -3.49657 | -51.10527 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 384331d4-7b37-334a-aff8-58af8165b192 | -3.49605 | -51.10836 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe78a6e0-b254-30e2-9e98-a258f8e21069 | -3.28034 | -50.93757 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7677a879-bc15-3cb6-9d03-56d42e1d885d | -3.27984 | -50.94059 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50c03034-39a5-3b5f-b90b-a417edb97e13 | -3.27338 | -50.66388 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f5012aa-ffe8-342a-94f5-8d9a9f80da12 | -3.26835 | -50.66306 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64dd9c4f-50ef-308d-a8fd-4ed2ba15e0cb | -3.23716 | -50.84945 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be995162-5f64-371a-ae1e-a513bbc6d840 | -3.23665 | -50.85247 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ec056c8-9248-3115-9576-c95968ade96a | -3.16039 | -51.30729 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65b6bbce-7e78-305e-8041-63c8c6cc34bb | -3.15927 | -51.05259 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 961904a5-a4e1-380f-82df-c2d7b5bf0962 | -3.15876 | -51.05569 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 372e3769-4945-3bb9-8ae3-d972d3931efa | -3.15513 | -51.30642 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a14e0326-52fc-306d-af55-44a263ce6567 | -3.88087 | -51.8336 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07a96963-630e-335c-bef9-e71ef77ca657 | -3.83574 | -51.90388 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f933ca5-9472-3cc3-9bc8-ceff66f8218d | -3.83458 | -51.91078 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2778923-9226-3b61-9667-6b75618901eb | -3.83399 | -51.91426 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba63402f-5618-349e-8977-96ac6781395e | -3.80849 | -51.29839 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b12d36d3-f789-36a0-94c2-373e1bb40e62 | -3.80794 | -51.30162 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8c67849-4a8b-3b6d-a2dc-9389047ff09d | -3.8074 | -51.30483 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b96d91c6-53bb-3900-b0b9-1d9f9225f8c8 | -3.80686 | -51.30801 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a9df701-8d3b-3777-b8d3-f06f2f9b73db | -3.80325 | -51.29775 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c377cb87-e953-3436-bead-48963e81de74 | -3.80271 | -51.30093 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47de2455-b14d-3827-9a87-207211693bbd | -3.80217 | -51.30408 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 850fdcd5-d035-3795-a28f-094ef3f7998f | -3.79811 | -51.39143 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afdd4c8a-6ec1-3da1-ad81-92b04aa19c5a | -3.79755 | -51.3947 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9f5dc8f-1008-3ec8-8a61-fe3524db7868 | -3.79397 | -51.6097 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 289bc6fe-2137-347f-89dc-cd69ecf908ff | -3.79342 | -51.61296 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dca0e99d-3727-37e3-9825-32af7efa8290 | -3.79288 | -51.61623 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5ed411c-4e22-3cb4-9d9d-837e375bfa6e | -3.77791 | -51.35201 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47276ecf-4509-36bc-9f97-2fd03c6e4d54 | -3.77781 | -51.35168 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e961428-7fc4-3152-878b-fa477c5bd05f | -3.77737 | -51.35513 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17b407c2-c0c4-3939-aa36-b5010a677670 | -3.7773 | -51.3548 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7260ef21-3179-308c-92b2-b9da7ea4c13c | -3.77679 | -51.3579 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4a28330-4bb6-390f-8678-e0c60bdf31e2 | -3.77322 | -51.34798 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e00bcfca-1fb0-301e-befe-4c7f231f19ce | -3.7731 | -51.34762 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c1844d7-f283-3e47-8d50-6fb8a38aa5ed | -3.77268 | -51.35115 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd65fcd-3d26-31bf-8d11-fac159d37dd2 | -3.77258 | -51.3508 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd29bb06-fdea-3c9f-8346-7d1091468f1d | -3.77213 | -51.35434 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dcdbda2-58cf-3c32-9eb0-2a359087b6d3 | -3.77205 | -51.354 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcd95c62-08e3-38c1-bff5-416de1aa55b5 | -3.75798 | -52.06057 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b19e5f70-4346-3dfa-aa4f-f9a42b3ded4c | -3.75741 | -52.06408 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41916a69-0e10-3ee6-8e90-54d7bb8f3272 | -3.75068 | -51.93533 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81edbb7d-1324-3948-9eb7-965c0120436d | -3.75008 | -51.9389 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45e4f1fd-fb07-3a05-baf7-94aea5504ca5 | -3.74462 | -51.93809 | 2024-10-17 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1888a55-7f28-3d3d-a13b-93770117548f | -3.68827 | -51.2775 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 053e0cca-f2e1-39c6-b6da-1f63d17a66fa | -3.68357 | -51.27365 | 2024-10-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ac03138-fa5c-3129-84b9-c5535e49ecff | -4.35767 | -50.97195 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
