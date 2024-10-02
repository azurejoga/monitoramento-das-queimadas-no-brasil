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
| d7f93b1c-ea9d-366a-9bcb-fa5cdc801f9f | -12.9385 | -62.6716 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5db77213-c4e4-3428-9ebb-086773fbfdf8 | -12.941 | -62.683998 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d87ae2f-5f09-3515-aacb-ed413e5439dd | -12.9435 | -62.6964 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8f042fd-6ec0-3fd1-a6ff-de187709ce88 | -12.9287 | -62.673599 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91f0a5ad-1d88-3c27-b91f-569fcff88255 | -12.9312 | -62.686001 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e393c8c3-5635-3364-8169-22ebd9ff473d | -12.9337 | -62.698399 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 94226a08-c0f4-3eca-93a1-803ca1af1de3 | -12.9215 | -62.688 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c74e7c1-1930-393b-98b4-26620fdc95d5 | -12.924 | -62.700401 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba993476-7ec8-3e51-8035-b8e11c28f9cb | -12.9117 | -62.689999 | 2024-10-02 01:25:20 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 96c1e9ae-8d50-3091-8905-555d86c62955 | -12.8549 | -62.510899 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f134657c-2afc-3eea-b014-3cb887677544 | -12.8573 | -62.522999 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6d6506f-1c6a-3267-9242-be3230389f2d | -12.8598 | -62.535099 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f925a97b-3a9c-3317-8163-34a93eee614f | -12.8451 | -62.512901 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2c8f95-f8a2-32ff-8bfb-d1a9337a0e97 | -12.8475 | -62.525002 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c877659e-f339-3241-a890-06c421a87ca2 | -12.85 | -62.537102 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0bc22047-1eaf-3094-a33c-739230482c3b | -12.8353 | -62.514999 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be025900-d8b8-32e3-a08d-9fe5b71ec77d | -12.8377 | -62.527 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5d9924e-62ef-33ae-8778-25f5cf0c77c1 | -12.8402 | -62.539101 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a519075d-1f52-328a-907e-8622458cc07e | -12.8427 | -62.551201 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e6fbb5e-50f6-36bd-84ca-e8aeb1c48293 | -12.8256 | -62.516998 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7aea33-b32f-389a-bd2b-1403c19508a9 | -12.828 | -62.528999 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5459ae5-7fed-3646-ad11-2c4c423d56d0 | -12.8305 | -62.5411 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2575611-4726-3c34-a99d-6d90dac3997c | -12.8755 | -62.762299 | 2024-10-02 01:25:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d6b7b7aa-3da7-324c-83be-c08231836845 | -12.8781 | -62.774799 | 2024-10-02 01:25:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 645b0e97-8d5d-3da8-b82a-b7f8ac40464b | -12.8207 | -62.543098 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 755f3009-7959-311f-991b-1c102341b9de | -12.8232 | -62.555199 | 2024-10-02 01:25:21 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6accf4bf-7c1b-3b15-a5f5-1137b0f7197e | -12.8657 | -62.764301 | 2024-10-02 01:25:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8a115fb-4225-3fb1-9753-08614e390c30 | -12.8683 | -62.776798 | 2024-10-02 01:25:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b666dd2-be3a-389d-8592-6ad8dc6190f7 | -12.806 | -62.521 | 2024-10-02 01:25:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3a878bb-3bce-35ea-add9-23fbb00fa5ce | -12.8084 | -62.533001 | 2024-10-02 01:25:22 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c80989da-8604-38ac-8569-7de964c15483 | -12.8109 | -62.545101 | 2024-10-02 01:25:22 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1ca83e8-6f0b-315e-80b9-4a3665f74298 | -12.8134 | -62.557201 | 2024-10-02 01:25:22 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0a1d474-a28b-39d8-bc53-87a011e77740 | -12.8585 | -62.778801 | 2024-10-02 01:25:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58554ddc-185b-348a-a97b-d21cb4049e24 | -12.8488 | -62.780899 | 2024-10-02 01:25:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc777a8d-ac99-3fb0-b613-40c7c11ea45d | -12.8513 | -62.793499 | 2024-10-02 01:25:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3bc0ce-2205-3224-b482-4a10292d7435 | -12.839 | -62.782902 | 2024-10-02 01:25:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee67247-a130-3f2b-9aff-a368a7e57865 | -12.8415 | -62.795502 | 2024-10-02 01:25:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 79a8a759-9359-37c1-8309-a5e945484bb7 | -12.7747 | -62.666801 | 2024-10-02 01:25:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9319358d-c18b-350d-bc0d-8efa267c1948 | -11.4841 | -56.7789 | 2024-10-02 01:25:23 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7ddbcc-f88c-31e9-9f67-c834216a4510 | -11.4857 | -56.7859 | 2024-10-02 01:25:23 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f75ac3a0-7eac-3030-9ad4-e8302e627b73 | -11.4873 | -56.792801 | 2024-10-02 01:25:23 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c29a2298-ab26-3956-9ba2-049d599164b7 | -12.1268 | -59.7724 | 2024-10-02 01:25:23 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57a47d59-ece4-37ba-b531-c0600fd7d93e | -11.3287 | -56.233601 | 2024-10-02 01:25:23 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66d7c2f1-f73c-34c7-9411-c6418b3ca338 | -11.3303 | -56.2407 | 2024-10-02 01:25:23 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b174ff8e-cbc6-3bda-86cd-6a2b119a900d | -12.1188 | -59.782902 | 2024-10-02 01:25:23 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4aa88e-fb90-3c09-a4d1-206698dcae3e | -12.1402 | -59.882301 | 2024-10-02 01:25:23 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56fefeb1-1e3b-366f-84ca-0ba48434492d | -12.1419 | -59.890598 | 2024-10-02 01:25:23 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc7e610f-434d-3382-a36f-096f0ca6d168 | -3.2136 | -46.7843 | 2024-10-02 01:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 35e4df51-fbf6-35a5-831d-258dbdf48838 | -12.7495 | -62.8932 | 2024-10-02 01:25:24 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1bdafd4-c1df-3469-a066-628ee8ef115f | -12.7521 | -62.905998 | 2024-10-02 01:25:24 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de1be556-ace2-3ff7-b6df-e4dac1612709 | -12.7547 | -62.918701 | 2024-10-02 01:25:24 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc6bc26c-26d2-3de6-bb35-35e073fcb0a9 | -12.7053 | -63.0765 | 2024-10-02 01:25:25 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3c15775-708b-3ba5-835a-77971894fcdd | -12.6468 | -63.0886 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7bddf862-20c6-3711-a9b4-a632c194e788 | -12.6494 | -63.101601 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce62ee6-2124-391e-81bd-9b7fbab1ce04 | -12.6521 | -63.1147 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2847fc16-79ec-398f-8407-ede31125aae1 | -12.6396 | -63.1036 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6f298e17-e304-3c8a-8e49-e50ee5ca55ec | -12.6423 | -63.116699 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a59b417a-6a10-3ffe-845f-88c979305241 | -12.6449 | -63.129799 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 856ee24f-b53c-3975-acde-e0f22898de78 | -12.6326 | -63.118698 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4de3365-46d3-3a3a-abf7-95cc8ec28a8b | -12.6352 | -63.131802 | 2024-10-02 01:25:26 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 108d6bfa-4dd2-36db-a93b-ae48fd534cab | -10.6144 | -54.060299 | 2024-10-02 01:25:27 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5abfd85a-13b6-3bfb-bcac-46c06c58b850 | -9.5961 | -50.191002 | 2024-10-02 01:25:28 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfe63a6e-e2ac-3560-8fb8-e21c3cd0fc39 | -9.5864 | -50.193401 | 2024-10-02 01:25:28 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec3d61a0-b020-33ed-b2c8-ea63db16f749 | -9.5901 | -50.207901 | 2024-10-02 01:25:28 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00ab86ca-3bad-33d1-b534-b1708361517e | -9.5597 | -50.169201 | 2024-10-02 01:25:28 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 269e4f62-7a4d-3259-8caa-d9df71d3e9eb | -9.5634 | -50.1838 | 2024-10-02 01:25:28 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e72baa9-97a5-3551-a4a1-120197b64293 | -12.2647 | -62.315201 | 2024-10-02 01:25:30 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d223da6-70e4-33c3-8a0f-68f52330cba6 | -4.4657 | -42.8877 | 2024-10-02 01:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 54a67a16-e9e1-323d-affb-332fbe5ccb9d | -8.4791 | -46.836102 | 2024-10-02 01:25:32 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d63e81c-2fb2-3405-92db-8520b0bf024b | -8.4857 | -46.861599 | 2024-10-02 01:25:32 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7142e6b-8927-3ee1-aa78-7aac98446d12 | -8.4695 | -46.838699 | 2024-10-02 01:25:32 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cae0381e-87ba-39f6-b892-1ab2e535d431 | -8.4761 | -46.864201 | 2024-10-02 01:25:32 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 024e1f22-0a61-3f65-9cc6-4659467c6a4b | -10.6269 | -55.874298 | 2024-10-02 01:25:33 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f45153e-b5d9-303f-b4cb-a38e89ab5c9f | -10.6285 | -55.8815 | 2024-10-02 01:25:33 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7dd8b7e-8ba1-34bb-aa94-d4bbb29b4bf7 | -10.6171 | -55.876598 | 2024-10-02 01:25:34 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecfe7586-d489-37ae-994f-2464c497b3ac | -10.6187 | -55.883801 | 2024-10-02 01:25:34 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d84a28e-9167-37c8-a87a-e0bcf3843dc3 | -10.6204 | -55.890999 | 2024-10-02 01:25:34 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab40bc9f-8c92-33fe-b2f9-6bfdef45cee4 | -12.3148 | -63.707802 | 2024-10-02 01:25:34 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17e504bc-0fb2-3f9e-9474-905c32f74072 | -11.2414 | -60.468498 | 2024-10-02 01:25:40 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9117369-ac74-34e0-8b9d-a92508e39b33 | -11.2433 | -60.4772 | 2024-10-02 01:25:40 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d96e9a87-c44d-359e-b989-74a94913f1a5 | -11.2696 | -60.599499 | 2024-10-02 01:25:40 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63e6a03c-060d-3338-b160-a60062171bf6 | -11.2715 | -60.608398 | 2024-10-02 01:25:40 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f86c2ec1-b406-3b4d-8ade-cbae605f23ca | -11.2579 | -60.5928 | 2024-10-02 01:25:40 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88babf03-eda1-3bbd-9613-9967ba27abdc | -11.2598 | -60.601601 | 2024-10-02 01:25:40 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8545d044-0ecb-38f6-a668-9b7c02919b08 | -11.2481 | -60.594898 | 2024-10-02 01:25:40 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c679ba7-1506-3966-99df-7ff8c61842b2 | -11.25 | -60.603699 | 2024-10-02 01:25:40 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9c71b6-0059-3d8b-b727-8b62f30191ac | -10.7222 | -58.5187 | 2024-10-02 01:25:42 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd29f953-2579-32a4-b285-eba1594bf6af | -10.7238 | -58.525902 | 2024-10-02 01:25:42 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83f3ccb7-45fe-333d-844a-d6da61f556cb | -10.7124 | -58.520901 | 2024-10-02 01:25:42 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bda89a7-7028-337c-8e77-0481d5a6edb6 | -10.714 | -58.528099 | 2024-10-02 01:25:42 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75f19d08-79a9-3d9c-aec6-5a09ed4b2131 | -10.3296 | -57.503601 | 2024-10-02 01:25:44 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5ace2e-a63d-3fca-a4c2-ef9746067bd1 | -10.3311 | -57.510502 | 2024-10-02 01:25:44 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1efca40-554d-3544-93e4-1f5051123fb1 | -10.1296 | -56.761101 | 2024-10-02 01:25:45 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31457999-73d8-3da2-8913-3079b9fb3eb2 | -11.6641 | -64.003998 | 2024-10-02 01:25:45 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03434f9b-c339-3ca8-b845-8ff571eb0cc1 | -7.1794 | -46.9665 | 2024-10-02 01:25:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 892602db-81e9-39d2-9f0f-c413f2e34ab8 | -7.1796 | -46.9444 | 2024-10-02 01:25:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f223d7e5-e675-3149-ad92-e9ba92a62b04 | -11.6134 | -63.9543 | 2024-10-02 01:25:46 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8e352eb-7a4b-3463-ba03-45a48033a677 | -11.6251 | -64.012001 | 2024-10-02 01:25:46 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 331be9ac-6453-33ac-8d24-61d2455c4052 | -11.628 | -64.026497 | 2024-10-02 01:25:46 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2aab3a1-b6df-350e-87f9-1383561527cd | -11.5662 | -63.772499 | 2024-10-02 01:25:46 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README32.md)
