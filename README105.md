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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec648e8-a3cd-3508-aabc-e4947a68d4dc | -6.12415 | -50.95318 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b694e8b-6da0-37ff-bfe2-f08f3563e548 | -6.12139 | -50.94921 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04a03985-afd4-3cc3-8666-cbc9f683d53d | -6.11374 | -50.9763 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6c4db60-9bff-3bc0-8e15-a1dc876905de | -6.10137 | -51.09801 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a0a027c-550f-3664-a11a-13dc7b7621ad | -6.09916 | -51.09058 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8980890d-b4e7-37db-ab96-fc350d92066f | -6.09861 | -51.09404 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52603c9e-9651-3771-873d-f64b9822f683 | -6.09806 | -51.0975 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9010c021-0780-32d5-b0dc-01de6599e605 | -5.99352 | -51.04886 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e159a46-9f64-3190-b2a8-0b18a246633a | -5.99322 | -49.67736 | 2024-10-10 04:44:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e24dac02-f947-31e8-9468-9db7462c9eef | -5.99268 | -49.68085 | 2024-10-10 04:44:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e2ef4a5-5fe2-3d82-87e3-9e6835cc4082 | -5.9913 | -49.77855 | 2024-10-10 04:44:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6295ba0-f17e-3769-8da3-4c53cdf531ae | -5.99076 | -49.78199 | 2024-10-10 04:44:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4c90c88-13b2-37f7-a943-bddf26a75ed5 | -5.34264 | -50.82299 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5af01d2e-c439-33a0-b560-f636c46f5711 | -5.06491 | -50.75433 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03b39681-daae-3e9e-a0f5-58d2acc8ba1d | -5.06246 | -50.66222 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d29fdc9-427c-3809-a938-085b83e9c916 | -5.0616 | -50.75381 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48120ece-07f6-3548-8913-db4374bddbea | -5.85416 | -49.94111 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d4ea58e-a739-3f11-b4ce-b05b2c92007d | -5.79689 | -50.20036 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 945514a1-c0ca-31c2-92e2-19b25fe9848c | -5.79553 | -49.8382 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 229bb354-40bb-3aa3-b9fe-c40af1e90a38 | -5.76986 | -50.22081 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75194c17-966e-3905-8f1c-0caafa9251ae | -5.75025 | -51.03894 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd780be2-488e-38bf-ad51-73d3c1fa3f74 | -5.71491 | -50.13747 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 209fa9e9-34c8-3278-9cc0-0cf3bca99ac4 | -5.7144 | -49.98737 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d4bcda7-68be-39f4-b2fe-a7c8b9d06358 | -5.5555 | -51.02574 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe03e270-67af-3050-acdc-1537cad017d4 | -5.55424 | -49.94851 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad94fcfe-316a-3f49-bca7-dd8c6d38b8c7 | -5.55091 | -49.94799 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fccfdda5-fd8c-3a1e-9ddb-4994caf80f6d | -5.53547 | -50.37271 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5d15cf7-a6f0-3a7a-a11a-c51d129fff04 | -5.53216 | -50.3722 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49e8a2ad-dd23-3a14-868c-058613b38dc2 | -5.5123 | -51.01889 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc1fed1-72f2-3510-951c-02006b5f0179 | -5.50899 | -51.01836 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec37dc6a-0446-30ea-8f6f-35f92743c9ca | -5.49973 | -50.40608 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 608a88cf-560b-3aec-bcdf-a075d753573d | -5.28404 | -49.54633 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 754b2e8a-2ddb-3bc8-b65f-ac7d71f15b84 | -5.20036 | -49.99696 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 895523ee-f621-3e87-9ad3-9d7fc789445f | -5.15197 | -49.84979 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 739713bd-dc59-3d1d-9d46-7d6341268ecf | -7.19388 | -51.21436 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9fc1160-c600-340e-bb37-4faeeab7785f | -7.19334 | -51.21782 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9487e5e8-01c7-39d9-83e0-376c1fe7b7d6 | -7.19062 | -51.23511 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 977ad97d-0366-30b4-8649-68a6adaaeedf | -7.19057 | -51.21384 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3a9b53-1e35-36c2-a0ec-6858d5c82cd0 | -7.18727 | -51.21331 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4035fcde-cc6a-3b23-946a-01aec4876626 | -7.10357 | -51.11826 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b3f2266-c965-31ea-8cf6-18d8c4deb83a | -7.09835 | -51.25911 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81e94c6e-5e9e-3cbf-a899-0274d7a8b7cd | -7.09781 | -51.26257 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a4cd0f2-e04b-3760-9e1e-1bec46d886c7 | -7.09505 | -51.25859 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b5dfc2b-24c5-3a20-b440-4c7dd3861584 | -7.03887 | -50.31514 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57e69e7d-be4d-31fd-ac68-937c9afd8374 | -7.03833 | -50.31865 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c717799-3b75-3730-8adf-af3ab5c72b88 | -6.86109 | -51.08377 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1438d34a-8e08-3de3-b268-5f7953be5fb9 | -6.85778 | -51.08325 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 530fa539-a0ee-36b1-9637-b2ff37720ce3 | -6.81206 | -50.94148 | 2024-10-10 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ef9afc-70ab-393f-8377-766aa9f15a2b | -6.80074 | -49.94252 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e6a011b-a8d8-305e-a4db-5e56f18f3a3c | -6.8002 | -49.94606 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7733184c-c2e0-3216-8ec7-6c2f412a3c67 | -9.3813 | -50.75486 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e471599d-3725-318b-9893-b5dfdb040930 | -9.353 | -50.76134 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab66877-f2c2-3e57-b8f2-3353ac9963d1 | -9.25104 | -50.36272 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96db0114-f245-397d-8434-d99ffd2a7ea1 | -9.17739 | -51.51844 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38e2efb2-2647-3a5b-acb6-0928e919d590 | -9.14292 | -51.4346 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65c210d9-9d0c-3b8c-b706-404acbd646fc | -9.10671 | -51.51432 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afc5ed36-cb15-3afd-85ca-10fd0fb55bee | -9.08128 | -51.46045 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 755760fd-4608-38d4-9fb2-e05c21bfa2ee | -9.03189 | -51.47067 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34f55bbd-aa6b-3349-af09-718615f2a0d1 | -9.03135 | -51.47415 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd45904a-e091-339f-88fd-041872e217a6 | -9.02859 | -51.47015 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 898b10c6-9384-3446-a9d3-56677e941f1c | -8.8569 | -50.7851 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c29a806-2105-3b3f-a2b6-fed85fdce750 | -8.8105 | -50.66968 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80ecdff0-d94c-3351-a8b2-545e8f4237a8 | -8.7713 | -50.72484 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31615ce4-b1ec-3f45-82b3-2e03a7133823 | -9.18067 | -51.49764 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d7ee0e6-2036-3252-9a90-32279b472818 | -9.17794 | -51.51497 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebe33347-886e-3999-aceb-a367ed45a100 | -9.17463 | -51.51444 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 598970b2-f86b-306e-abda-1c93692099c3 | -9.13974 | -51.49818 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2f1fecf-f934-3b31-baff-0506b7166516 | -9.1392 | -51.50166 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c0258b5-8ba3-33a5-8fa3-6acb07c191b4 | -9.13589 | -51.50114 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4525af4e-cdbf-31dd-be6b-69dd79310871 | -9.03411 | -51.47816 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9037426c-1163-39c2-8884-26c1c84efb22 | -8.57636 | -50.53608 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6cdf887-6628-3a42-b95e-a8e5959265b9 | -8.57303 | -50.53556 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0096cc90-d3fe-33a9-bb3a-ef6c16720f58 | -8.56357 | -50.53047 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b47061b-b448-3b71-bcf8-7da0bd93025e | -8.56079 | -50.52641 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c18de5-a147-35d0-bfca-8cfae47957df | -8.56024 | -50.52995 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 039c30cc-76d6-3ae1-a48d-2f2b4992702a | -8.53206 | -50.91032 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8dda9313-e26b-3cf9-bb4e-9bc0f01c86a2 | -8.5075 | -50.80593 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 266ec5ae-a3ce-32fa-9aa6-c1b6876241a4 | -8.50696 | -50.80943 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 330feb33-a923-37cc-9dfc-89886f7bc8d9 | -8.50687 | -50.98501 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf51fb77-2306-35c8-bc1e-cdb29f328669 | -8.50418 | -50.80543 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 628745ce-a375-3ca6-a768-7370dabc7bf1 | -8.50356 | -50.98449 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec76cef2-5d78-332b-876f-6a128370bb62 | -8.50086 | -50.80491 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bca114eb-0860-33ec-b6df-9a72b0e1eeb3 | -8.46871 | -50.77126 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f01cca5b-a3eb-3331-904d-5b97341d8b5c | -8.36795 | -51.65295 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab1070cb-a0be-38be-8ee0-49b377ec5662 | -8.36519 | -51.64896 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9407f39-6fac-374b-a0ab-e4206c7e1412 | -8.35237 | -50.82118 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5da0dceb-6db0-3f11-917a-dc450a7e1d1c | -8.34905 | -50.82069 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95e62085-3c4e-3092-b1e8-36411b5cb4b6 | -8.31643 | -50.26295 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bac4d8a0-7449-3138-90eb-c954cf6dde2a | -8.31282 | -50.90082 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebd0c50c-e3eb-3697-8159-d1672182ec9f | -8.22245 | -51.0004 | 2024-10-10 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94bb313a-475c-3d43-a750-53e5865318c6 | -9.37797 | -50.75433 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ce52253-c5ca-302b-8ac1-e5a6c61ebc55 | -9.37518 | -50.75028 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e3a8ac0-2eb8-3037-9a81-4f259508c9e4 | -9.2505 | -50.36631 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19c640ff-d095-3f26-9d79-62ae57f6a95b | -9.15993 | -50.58295 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c6aa92-0760-33ca-bef5-f3387227e350 | -9.15156 | -50.57073 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a8fc66f-9360-3d2b-aede-6560c4d11cfa | -8.86185 | -50.77511 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cafe86f-8427-3760-b5dc-f958c26589ed | -8.86022 | -50.78564 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 137bc79e-ec82-3f8b-a9a4-a9d964106375 | -8.77462 | -50.72536 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57277856-eb14-3d35-aa89-775c6cc27177 | -10.32318 | -52.03065 | 2024-10-10 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79aab0e7-4b8f-385b-8656-8d1266e6e0ec | -10.32263 | -52.03415 | 2024-10-10 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README106.md)
