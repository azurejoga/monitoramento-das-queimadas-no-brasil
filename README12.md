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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2f90182-75df-316d-8439-f2ff2daf178b | -2.7522 | -54.109699 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36b97893-4a0d-31aa-9826-fd1ca634592a | -1.4561 | -55.4454 | 2024-11-23 00:45:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e06d2d6-33a6-31fc-86a7-895d9642b1e8 | -0.2648 | -51.585999 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e642c9e2-286c-3734-8d07-1395a71d6396 | -3.5096 | -53.812698 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082e427f-f03d-3b87-85e6-a9298965e357 | -3.2249 | -54.240799 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 180f0f78-9e65-36a9-89e3-d52729a5e620 | -2.5669 | -54.064899 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f31ede-340e-3aab-b7f9-b92314560712 | -1.817 | -52.163799 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec87213f-122d-3722-93ad-0a27217a8207 | -1.6357 | -53.318802 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f149a8f-e6f7-3c03-ae95-625d651899c3 | -2.1496 | -50.909698 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4ded291-57f0-3f97-a99b-b8c1151c9b08 | -2.6109 | -45.628799 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e25a73ad-6a6b-3a32-ba21-01647be89465 | -2.7036 | -46.2845 | 2024-11-23 00:45:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10c3dbdd-1a7e-3123-ad57-360554c8d252 | -1.2078 | -51.7491 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fab9b91-5348-3ad7-936b-a7888569cbd9 | -1.7639 | -52.701698 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c15a4e51-316b-32d7-964d-77bc99da78c1 | -3.0051 | -51.544102 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 407a23dc-ff6d-3e28-ba48-fa6fe774b2e0 | -2.8123 | -54.010399 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c4f74a-c838-3cc3-847b-45651d060261 | -3.7098 | -51.786701 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a06e58-10b1-377b-a6a5-c4055c5f4f28 | -4.5333 | -45.871601 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ebf9c169-ada5-345e-ad46-4edfb5846c81 | -3.1783 | -54.308399 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0645cbc-a237-3f78-b830-f9c10d1c96f7 | -1.5197 | -52.079201 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c55c97c0-5a29-3307-a233-f1569264e2d2 | -1.2687 | -52.062901 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18281aaf-f84b-3d68-ab46-8703d8518c88 | -1.6976 | -55.145802 | 2024-11-23 00:45:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb1c75f-bc36-3386-a19a-2814f158834d | -1.5588 | -53.5257 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f0e3f32-89b4-347f-8245-dc14d8658ebb | -2.6777 | -45.651798 | 2024-11-23 00:45:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5edc668-a571-3077-acb6-bb71f91fab00 | -2.7627 | -54.0644 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ad6d68-7655-3d15-bcb0-f125b90a90ea | -1.1387 | -53.399799 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b06c4eba-20ff-3515-af46-79c471b0ce4d | -0.9461 | -51.639599 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deb4a71b-4328-3702-906e-40c77283f77a | -3.2891 | -53.840199 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74c60e99-9651-3f26-aa6e-cd1fec561d8c | -4.6041 | -46.513199 | 2024-11-23 00:45:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17aedbc0-53d8-36c8-a1aa-5cb6d589b10d | -2.9674 | -53.875801 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c164d6ed-8847-3314-bccd-aa1bbdfb1225 | -0.9723 | -51.709702 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| eb711b86-6ccc-351b-9c2f-7c160264fdf6 | -1.6231 | -52.580601 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 980cccca-1f68-38c8-ae2f-a6c0453d9865 | -3.2504 | -53.2584 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a4d5f08-5de0-3fad-a30b-a2a0af675a42 | -3.1146 | -53.113899 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8e2753a-be7f-39b2-a780-e8616b0991b4 | -1.6428 | -52.622101 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df06c59c-2709-3b28-8b31-c15de51c4b78 | -1.6175 | -52.4198 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83e5c3ac-1239-3a2c-800f-7f347997dff3 | -4.0994 | -51.056999 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02c68351-c9d3-3ef0-ac88-1f8fd820bd96 | -1.7263 | -52.717602 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 738f38d5-f6e4-3125-acb9-cbb4d95a7340 | -2.802 | -52.462299 | 2024-11-23 00:45:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccdf6f69-3980-3ee3-819a-fd0ec88c96ad | -1.2238 | -51.728802 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aef3a7e-c2e0-3a33-b6de-d9776f6a1f9e | -1.2431 | -46.740898 | 2024-11-23 00:45:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c54c09f8-bb55-3256-a303-6d403ea40796 | -0.8139 | -51.601101 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8150077e-b82e-396c-b546-69fbbdb3614b | -5.7549 | -46.254902 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e83f34f-e0ed-3dbd-8028-5c8f1bf4f845 | -3.746 | -50.012798 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d4149aa-7ade-3f7b-a869-39375b75508f | -6.1527 | -46.669998 | 2024-11-23 00:45:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40769ab5-b62f-3373-9d87-c339535bef33 | -2.8635 | -53.963299 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 553ceb92-dfd3-36d4-a938-5491c0424148 | -1.6397 | -52.699001 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07a1ffaa-f6f8-361a-becf-1a5bae32f3de | -3.7195 | -46.0294 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 166210c5-8d16-3c78-ba93-011f57dec9fc | -1.1837 | -51.9603 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acaf74da-3939-3434-b24a-0f83050c9d45 | -3.4811 | -50.4282 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 502c9c7e-30bc-3c1a-b976-9a1278e5ee28 | -3.2649 | -53.8241 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f9b599-196d-3c50-b8f4-f3a12e59e12b | -1.7345 | -52.708302 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e61ea503-90b5-370c-888d-e80bf766b4c1 | -3.1112 | -51.196301 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fad26e1-7e0a-314a-9b3c-082b20b995a3 | -1.6412 | -52.614799 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b55bc7-a1d4-3270-9bde-683b5a7ecf16 | -3.2464 | -50.662102 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd709284-2768-30e0-91de-1b5671f384cc | -2.8433 | -54.0107 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5d6aac-46cc-3ad3-b28a-415712ec03a3 | -1.6281 | -52.602501 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5f02aee-de4a-38d9-ba22-79d1af3d0058 | -1.7515 | -52.374401 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2552ebec-9a99-3477-b5d7-75bf95ff4664 | -2.6917 | -45.667702 | 2024-11-23 00:45:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8b25536-6498-3bd5-9577-2cd733e07aeb | -3.2482 | -54.207001 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2f5681-8440-31c5-8f40-c06216bc153d | -1.615 | -52.59 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29327de6-b19c-30ba-8c92-0d29bea5a779 | -3.6983 | -51.781399 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed16700c-ae6d-3540-8cde-f811b1c37f59 | -2.6213 | -54.260201 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0871d843-89ce-3b47-8f3c-535252d50612 | -2.3249 | -47.076199 | 2024-11-23 00:45:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3207cf9-c21b-36c7-9a82-8b22ca516014 | -3.3378 | -53.325901 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c94f00f-9944-37e9-b332-25cb20cbec0f | -3.2983 | -50.349899 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e282ccbc-eac7-3b17-9356-fed3a40c7759 | -1.4254 | -52.662899 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba157a6e-1cea-39c1-927d-dd44cc38786f | -2.5387 | -53.985298 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e91ec8-bf72-34d8-8394-e58c8a34fd36 | -4.4053 | -44.103802 | 2024-11-23 00:45:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57d315e7-4267-360e-a992-8ca945df3175 | -1.638 | -52.6917 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90b43af-ad9b-3122-8070-849604bfcc6f | -3.9516 | -47.973801 | 2024-11-23 00:45:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcf2377-50c1-3474-925e-9dc92cae0e67 | -2.2074 | -53.750401 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4c27296-cf89-3d33-bee4-d742e32948da | -3.3155 | -53.2729 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8d01a51-031d-3bf2-b309-90b74054d307 | -3.8885 | -46.0933 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 960fb82c-3e45-361c-aac4-a87858d7c55b | -1.1819 | -51.952499 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc3855d4-272a-33d4-8527-b14f7f79cb9e | -3.2145 | -51.4231 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1103e0-b10f-3099-af2f-741749321e28 | -3.755 | -52.392601 | 2024-11-23 00:45:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b47d37ba-2d64-3c8d-88f6-3b905a39ff21 | -3.2446 | -54.236401 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22006ba0-de41-3bc1-9c65-ed0ab3eede0d | -2.8924 | -53.999802 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc7b2947-a90f-3f71-9227-13f4e3d87d2f | -3.2127 | -51.415298 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1f6f121-c9f3-3833-bfe9-beb693b46b78 | -2.8221 | -54.008301 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a704a25-7bfa-36be-965c-b457a172c8e6 | -1.7827 | -53.650002 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f55a58f6-1c9d-375b-bf43-9e46d5c14487 | -3.6767 | -50.114201 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59a9299b-d2d2-3005-af08-c48deb4b1025 | -2.8932 | -53.046101 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3da754cd-3e56-3208-80d9-b282daba6de8 | -1.2354 | -51.734501 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd224b4b-50f0-31ee-ab80-a734ec9a80cc | -1.6806 | -53.198502 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbf7afab-502e-3ff6-b168-dd4a106bc38d | -3.8017 | -51.331799 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b81da2f8-f9ce-3cfe-a2db-94061ba3f07f | -0.9625 | -51.711899 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1d778908-d717-34b9-8f31-347b465e94f5 | -2.7792 | -54.046398 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7461fe6-9f8c-3ea2-9d3d-1543b5458a53 | -1.4342 | -55.0742 | 2024-11-23 00:45:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0c9d258-5dec-3adf-a41e-91202bd9e028 | -4.2537 | -48.694099 | 2024-11-23 00:45:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 002f9329-dcf9-35fd-987c-36b2cab8eee8 | -3.2264 | -54.2477 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cddb9c85-22a2-3be9-97d7-b3076583aeff | -3.0707 | -53.283901 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21d80143-dfc9-38f4-b47a-fe96c6039cf1 | -4.6103 | -46.496101 | 2024-11-23 00:45:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cbd3a68e-ad4c-39e6-8def-3dd1f8245d10 | -3.5102 | -54.730801 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a62c288f-2c5e-3021-993a-a06dc21e076c | -3.3187 | -53.286701 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80bb8baa-5487-3538-9736-1e162f931119 | -1.454 | -53.3811 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b1ec4b-bdc1-38f8-b27f-7cfc8a69c252 | -3.0675 | -53.2701 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 546f2aab-31c2-30b2-9cfb-f94e33d78765 | -0.9248 | -53.091801 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a30845d-fba3-33f1-8b59-2c39558714f0 | -1.2922 | -52.257198 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35caf018-d3b9-35d7-9e6b-7a77586d1dee | -2.0926 | -53.334202 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
