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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1190daa9-b997-3f30-92e0-7dbc8696197e | -6.76879 | -59.44512 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9048235a-519c-3b79-a62b-3308ba36362a | -6.69364 | -58.72554 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1be0fea-87f0-3437-8a0e-912046318997 | -6.74976 | -59.15643 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dbb31c15-24f2-3760-8d24-39c5b29d65dc | -6.14036 | -59.91187 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48edc78e-467f-35b8-8a53-aac49d05230e | -6.84351 | -52.50272 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d1c5de58-359f-39be-8ac3-6598f89048c8 | -7.68 | -63.50691 | 2026-08-24 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85caa6e4-e141-3129-b9df-ce577714bee7 | -7.68218 | -63.32274 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| ec5c1130-4398-37b2-a8f1-cc26c2e26071 | -6.96412 | -59.07332 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 247b7b68-2729-3c3b-8ff6-4cce1c468746 | -8.57849 | -55.28297 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaf3b921-bff0-3c09-a0fd-940d93051cd8 | -6.19563 | -53.52076 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6317254c-8e8c-363c-942c-1cc56394dd0a | -5.87092 | -57.56814 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54d1caa7-70ba-36d2-97cb-fe820df44a12 | -6.12775 | -57.83758 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15b80f34-f850-38ee-8da4-fe56a321aa9d | -6.95136 | -59.08434 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c15db4be-7614-3c65-8f0a-800eebf0a5af | -5.78666 | -57.57076 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c49ac38-cd5c-33a9-8514-34e88ae20eba | -6.17533 | -57.92998 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 807928d6-17dc-3cca-bf9d-497a87ac5fbf | -7.68551 | -63.32327 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 73151ca1-27fe-3b96-bd76-2d819510dea0 | -6.60737 | -58.38431 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e91ed53c-556c-35e3-8685-2b4d99f6b99f | -6.97325 | -59.06177 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 231450d5-f32b-3219-9dd5-f951ad756b01 | -6.61156 | -58.38711 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 12caba64-358d-3a00-a0a5-8984996d2592 | -6.86121 | -59.4078 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3482745e-1b45-3b7b-857b-3d4047cb8340 | -6.67264 | -58.74025 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3da5aeb-1a7e-31a3-a62f-3dd5422eede5 | -6.80147 | -59.5881 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed8f6dcf-46b0-3558-ad11-22d55514c5d2 | -6.67374 | -58.73822 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa4b6e4f-8ffd-3678-a855-fa83db9480a3 | -4.60878 | -55.744 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8e38d81-6843-326d-9554-56619b17511a | -7.76357 | -61.08693 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e241142-078c-3d18-a4ee-f6523c0cd5fc | -6.59767 | -52.45592 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f38100a-2136-312f-9beb-96bd5a152bc0 | -6.1527 | -57.95075 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 72836f1f-120a-3ed1-849b-ad87da3bf849 | -6.81203 | -58.65652 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efee7662-8983-32af-8b78-5bfb343e45ac | -8.38309 | -62.69244 | 2026-08-24 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f34ff3-d2bd-3833-895b-f2214f7e373e | -6.70536 | -58.72282 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6387737-52c1-3f81-ac05-03268b17ae8d | -6.3869 | -57.46993 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40d55c24-7050-3268-bcef-08293c866505 | -6.18873 | -53.53233 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e468cbd-fe01-39ba-98b2-6c8f7455a072 | -6.97502 | -59.07498 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c75f7ab2-c344-3003-adb1-02df5595c54a | -6.74424 | -59.65409 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a76e0ee8-4826-3615-9420-36d8ee4ecf03 | -6.60846 | -58.38195 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0c3083e-a216-355d-a829-fa1a51f0e756 | -6.33898 | -54.75311 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1225049-c604-3aa5-80b3-1f258298844a | -4.96606 | -56.2753 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f74f6415-345f-3b16-8acd-ce67fdc871ee | -6.69059 | -58.72057 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceeafb29-9f30-33aa-86b6-ad72f58e1deb | -6.79694 | -59.80986 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbb83631-0a6f-3639-bbf3-a1ba6c0160e9 | -6.59611 | -52.45733 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd057901-01eb-3363-a173-91a72f6a5df1 | -7.88295 | -61.70672 | 2026-08-24 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e06385eb-e456-3705-82c9-debb3f9015b9 | -6.81333 | -58.64764 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ff23840-875a-39a0-8ff6-1ce63bf50841 | -6.96899 | -59.06544 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a88a6b7-a82a-3c5d-9afe-ed5db38ff69a | -6.18313 | -53.53466 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe470f44-dfa9-390a-91b2-6245022fc0f7 | -5.68803 | -53.74505 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 709035c8-b132-3002-af10-e4d96b987c19 | -6.79285 | -59.81324 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d7f8dcb-9465-36ba-8b39-703c77ea312e | -6.79634 | -59.42704 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c09da2cc-e2b8-388e-bbc7-442fc6ecebc0 | -6.35178 | -54.76555 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34f9d0f2-8dfb-3055-9e28-b2871b111dc0 | -6.95925 | -59.08122 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2f667a0-cf8e-370b-b913-85ad2d80f28c | -7.26872 | -49.92134 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 088d89ae-1e69-38e6-b727-6c71bc0b6ee7 | -7.2571 | -60.61375 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41b2ca9d-b40b-3bb5-966f-c6e135c24830 | -7.77541 | -61.09987 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 344aa15a-ec40-3ef9-bc65-0b908a96ec8e | -5.94767 | -57.73471 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0266bc17-4a2d-39bf-be5b-4ae9fde801fa | -7.2559 | -49.86271 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8efc6bfd-0e48-390f-86a4-f94a78e2b56f | -6.38526 | -54.98381 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97a5499e-a363-3973-97b4-7d38d905c48a | -6.89478 | -55.69741 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2b54a22-0043-300e-a953-74a8ebbb9378 | -6.19993 | -53.52767 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18213a0f-9980-3215-8f49-29de99406ecc | -6.23817 | -55.39543 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3b86504-da40-3ca6-b636-4ba6fa5c6a58 | -6.22128 | -55.92385 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e997a428-fb5e-3e4a-a118-e21c85e5912a | -6.67328 | -58.73585 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f43f00f-49a0-341a-b9cf-364703170455 | -5.9445 | -57.72922 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13762520-ebf4-304b-beb6-77d6516c856c | -7.24746 | -49.87626 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 990cca9b-2efc-37a9-b98b-5607c2b7faa7 | -5.94586 | -57.73689 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d0c47ff-1ad5-3402-817c-dcfd228461e9 | -6.79753 | -59.80592 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbcc8de6-c01a-3957-8651-7b3f5e071791 | -4.99977 | -56.13498 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76d1d3f3-e784-3c1e-aacd-db625d5a28be | -7.76019 | -61.08641 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ae1a878-95b8-3291-8395-a3fc635cd11b | -6.94896 | -59.07536 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aab03b3f-d346-33c1-9d30-f9de1214a456 | -6.12134 | -57.74764 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc074177-12c5-320f-8bf5-bb210dffbf9f | -5.77956 | -57.56472 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d4416f0-36af-38dd-9490-442ec15ebc67 | -5.88098 | -52.10623 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f91f46b-6c53-3d46-a314-a592612cbe10 | -7.26955 | -49.91485 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1e7ffdf-cc14-3fc5-9e4c-be096c9c12ea | -6.63212 | -58.48285 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b58f2b3-4a0a-3afc-b788-fc5745aeeaf4 | -7.26433 | -49.91711 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c214b0ac-5374-319b-a3aa-cc4b3143001c | -6.34374 | -54.75384 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ea1dd89-3d67-349c-b7b6-88cae65b55ab | -7.69383 | -63.33537 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 695cee56-c608-3b81-a449-fc33a37f4ea6 | -7.94363 | -63.45458 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec4e9510-4beb-39ee-8548-529b2cccb288 | -7.23258 | -60.63337 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccadda80-56dc-307d-94a0-67e5a6a2afdb | -6.80832 | -59.68682 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca5e7238-9b20-35d5-b544-902c133e29fc | -6.82894 | -59.66958 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 272c1c43-745f-3d2f-9d14-1537c2ffcdb7 | -6.89225 | -55.69883 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dca7a774-849b-3074-99ea-f077427ea4d4 | -7.67553 | -63.32169 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 96d08a57-9ed5-3b46-9193-852cdb95dbfb | -5.86776 | -57.56258 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3354f22d-4351-3ad8-aade-a931001206c4 | -6.68995 | -58.72496 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1f791d9-4337-3475-b0d9-6b07d6e1fa85 | -6.343 | -54.759 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ceb4377-abdb-3eba-b546-0245dfdcb445 | -6.80832 | -58.65595 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09d6914b-882c-3364-a709-95ec377b2ac0 | -6.13978 | -59.91568 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08432fdc-0fd5-3b61-a965-02ecdb8bd0ca | -8.38363 | -62.68896 | 2026-08-24 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c217946-63ff-3666-8f55-d5ffbb0a6ba6 | -6.80461 | -58.65538 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a0a86fb-2617-3366-b797-97b76026206b | -7.68828 | -63.3273 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fe21811c-8164-301f-9f4a-3fc277828137 | -4.99924 | -56.14066 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bbcecde-854a-308f-a137-e6e5e309c61e | -6.80441 | -59.59266 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d274a4c2-a8c9-3721-843e-b84b3926f69f | -7.25781 | -49.86462 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cd592036-3c0c-323c-a33f-cbbd737a89f9 | -7.6783 | -63.32572 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3e7db41f-31f9-35f5-b6cc-3d1865086ccd | -7.27031 | -49.92274 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6032cbf9-c45b-334a-84cc-9527828214c1 | -6.14412 | -57.93799 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7adadb31-66d4-3088-ae2d-390287bc353a | -6.54962 | -56.17322 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f1156cb-6bce-385c-b1ee-bdb62f1838f3 | -7.78788 | -56.28343 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f05e145-00c9-3239-9129-e3fe4f0b39a3 | -6.88743 | -59.4034 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 321cad04-4236-357a-b1b3-58bdba898d38 | -7.22917 | -60.63287 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07217f70-93de-3890-bb30-d37b9bdd3231 | -6.20036 | -53.52457 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
