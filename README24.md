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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f80a8cf9-206c-3f36-86ae-db4a4975bb69 | -3.83179 | -41.56148 | 2024-12-13 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d733ba5-6521-325b-9d6e-6b42079e950a | -2.58818 | -53.9682 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae1c2110-1ec7-3c37-bf83-f3d95d45bff2 | -2.46821 | -53.64563 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae4aa846-6f83-3a93-8c86-97c525bdbbcb | -4.88132 | -44.40322 | 2024-12-13 04:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dac0b2a-eb33-3ab3-88c3-8922e0e84d62 | -2.23193 | -53.72851 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd3f7ac5-aec7-32cf-ae5e-255bd1d5329f | -3.10712 | -48.28604 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b558e523-9f46-36ef-9172-829becc2375e | -2.96174 | -48.61333 | 2024-12-13 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d03587-f21a-3271-82e2-1e785f4b94c7 | -2.5174 | -51.78983 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f96f33-fe08-37cd-a8fa-bd029f520405 | -2.51341 | -51.79296 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83db28f0-c2f9-30ff-b4de-af40b2a0d26e | -3.83043 | -41.57079 | 2024-12-13 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 600c9f08-b2de-388e-9257-c6558c2e8cf3 | -7.36095 | -46.23331 | 2024-12-13 04:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a972332-18c1-3bfd-82bf-14b40fdac38c | -4.77925 | -48.50267 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f00663c-4af7-3b9a-b73f-cd61293b0cb8 | -2.49862 | -51.79815 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a62fc285-e7a5-3842-a8d2-6ec0a14ce770 | -1.73763 | -52.02522 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41a07602-a1bb-3430-9254-39ded89f2556 | -6.12769 | -42.53763 | 2024-12-13 04:42:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0ed429f3-8251-38d4-b0b5-65a434ebbb3f | -3.1822 | -45.6178 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b0ba0e-ac07-3d0c-9bdc-e689e26c7a6c | -3.14524 | -53.29142 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aca6b9be-5c2c-36c4-b68f-9683b3ee3047 | -7.36032 | -46.23764 | 2024-12-13 04:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d491656-9379-3017-82af-343ef7179394 | -2.2348 | -53.43758 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 769ed82c-cde8-3cb2-8e3e-c66c4ee61136 | -1.46034 | -46.81372 | 2024-12-13 04:42:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1962594f-ed70-3c0f-b425-376bbd51a054 | -6.05995 | -44.04797 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d345f54a-d0fe-346c-a5ab-5d762859a46c | -3.1454 | -45.59722 | 2024-12-13 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42219d77-72ee-305c-b844-7b2440da95ec | -6.90901 | -43.54725 | 2024-12-13 04:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bb8feaba-b004-39dd-a6aa-719f1c83cbab | -3.13507 | -53.28556 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fa73dfc-2750-3a36-a9d6-7fe98632eb86 | -3.18297 | -45.61287 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ac28c7e-69bc-375a-bd5f-1804701c17f0 | -2.55061 | -53.42935 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a1e1011-5d6d-3ee0-b672-61920a7380d9 | -5.94088 | -43.76933 | 2024-12-13 04:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d5aa77c-475b-3628-a2f1-42bf9e396cdf | -3.30154 | -43.53411 | 2024-12-13 04:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd902766-a286-332d-93e2-e36def0b0cc1 | -6.76395 | -44.82553 | 2024-12-13 04:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f0e2c48-93ba-3070-bfdf-1c9a404eb59e | -6.92145 | -43.52819 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 91aa3536-6489-3f6b-8a83-d86157cd0434 | -2.4815 | -53.71778 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6ebd57c-958b-3fdc-b5e4-01298a6e93f4 | -2.44665 | -53.71013 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f00f77b-c550-32de-b46f-151f96be924e | -2.47063 | -53.64379 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf39dc74-2e29-35e4-9170-b6ac623881ab | -3.77339 | -50.69609 | 2024-12-13 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb69ebea-3e3f-30b6-8231-6a8cbd9dd9f2 | -6.20908 | -43.28253 | 2024-12-13 04:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff942983-ca65-3b81-9121-b67b71c6038d | -2.91472 | -48.0142 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1daaf95-4f0e-3495-bbbd-a01501e46935 | -2.50086 | -51.80603 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec135aaf-f1ef-3fa1-954f-9bb48b1a3201 | -6.11518 | -43.95581 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae458031-c712-3461-8387-8ee59bc1ebf6 | -1.57432 | -46.04229 | 2024-12-13 04:42:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee122cfd-a383-3c6c-8fa6-af9287e52794 | -3.14107 | -48.60423 | 2024-12-13 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e231dc50-b5dc-3424-8bc7-d4ccb090829b | -3.13769 | -48.60371 | 2024-12-13 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb86346e-f30b-369d-8015-ca34a091a4ec | -4.55053 | -43.57758 | 2024-12-13 04:42:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a80859c-edf6-3982-83f2-d99a1851affe | -2.19321 | -53.65087 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9635b71e-ee01-3bb3-9876-522e22f069c6 | -1.9952 | -54.51468 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed63cd8e-f533-306f-ac88-b1da9e1e05c8 | -4.47709 | -47.98376 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3280780e-e631-3484-9d7c-b8d5448fa539 | -2.06722 | -51.19897 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d088425-8a12-3f36-b7bb-0ae51773b769 | -6.92547 | -43.53395 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 9540a699-0f09-327c-9fce-04849d60aa0e | -2.45723 | -53.98787 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 595b486e-3aab-3c88-a240-754ae667212c | -2.4645 | -53.64499 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d03e2b2-0a87-3da4-83a2-de29f1e3c441 | -4.7821 | -48.50693 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45a91018-98d6-3183-b5ff-fdb49155298f | -2.91187 | -48.00993 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19327f34-6497-3334-a9c1-1d2820fa0dfb | -1.24827 | -52.1708 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f0f20d5-e4d4-3268-a0bf-55f623c29279 | -2.3635 | -53.91918 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05357182-72ec-3828-9c03-e20165d2e779 | -5.21921 | -43.29893 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 379e0f0f-4dbf-31be-8717-126620fc12c8 | -6.28436 | -49.64463 | 2024-12-13 04:42:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c107a9a0-96e8-357b-bc66-4851e276b9e0 | -5.94105 | -43.77147 | 2024-12-13 04:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a08f4fc8-8b7a-3372-9f1d-55720fee56e6 | -3.83225 | -41.55833 | 2024-12-13 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63e670fc-564d-3a75-a034-3592821a4c9d | -1.99362 | -46.54146 | 2024-12-13 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ef6f4cd-1b97-3f83-ae6e-54155f0862f2 | -2.46516 | -53.7243 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95655055-4978-308c-af40-79f95a0955a1 | -2.41452 | -53.69606 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36e2c7d9-d7fe-3957-96d4-d35fe5790e61 | -3.4754 | -49.67525 | 2024-12-13 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36f041d9-1c5d-3e09-a26a-6b5c073ea639 | -2.48664 | -51.80756 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6587731c-547b-3ba6-a8dd-714b92889eda | -2.73608 | -52.97116 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b154a63f-cf84-3513-95c5-18cef3d58eee | -3.13825 | -48.60012 | 2024-12-13 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca39a510-0de2-3324-a463-951f6210940c | -6.05541 | -44.04738 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4819584-ffbc-340a-8dac-14de0297bc57 | -3.28979 | -45.59726 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4997f453-0dd5-3cbc-93fe-911f280d51da | -1.75632 | -54.17554 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 494a6c08-d842-3521-950b-51d88f9cf3f6 | -1.51151 | -54.15118 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ad44c57-1f3a-3397-ae27-ae3d71f1a453 | -2.49005 | -51.80809 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 461b0d99-81d9-31c5-a743-b66e62d706f3 | -2.73672 | -52.96717 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ef9be28-1cb0-3445-8aa1-04b24c84558b | -4.67445 | -48.15868 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd5d1781-9471-30fb-a3b9-aff31f777715 | -2.52023 | -51.79403 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138f63c3-47ea-329e-b940-1ad495a16f62 | -1.25587 | -52.16802 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cec10b33-164a-3db0-af0d-e534f7fcd517 | -3.14692 | -45.58732 | 2024-12-13 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62ca02d6-0996-3e75-b353-c59dd581d09b | -4.44786 | -44.65611 | 2024-12-13 04:42:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d59b6da0-4dc1-339c-a7ba-c8fb91c6b498 | -2.30699 | -54.00465 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1f59a95-9aad-3947-aaa8-f02b6a270ea3 | -3.03735 | -47.94824 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d345c8c5-396d-3602-85ed-eb937e3588d7 | -6.91449 | -43.54287 | 2024-12-13 04:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fec4c12e-3403-3460-bba5-63334b8b2c5c | -2.45242 | -53.70866 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8518b417-e158-3e22-8d7d-0b7cb46cb4f6 | -2.95837 | -48.6128 | 2024-12-13 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07388e57-47dc-30fd-bf3c-c2f774c15525 | -6.76061 | -44.82757 | 2024-12-13 04:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8811b5a-a40e-3067-9f16-864a45dad3e0 | -3.28661 | -45.59167 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 144b83c2-a3c7-3f6e-ab5a-0fbd476c7491 | -6.91193 | -43.52686 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 795f5d48-3c37-3fc2-9733-f5bfc288f1bb | -4.42952 | -44.14233 | 2024-12-13 04:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4e53fd6-53aa-3e78-9267-e60438249009 | -6.08589 | -43.53502 | 2024-12-13 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c7ece4f-23c2-34e2-ac7c-022f975b48f9 | -3.04051 | -44.47724 | 2024-12-13 04:42:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c089a3b4-fa4a-36c0-99ab-e51be53d9800 | -2.71506 | -47.56086 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f7db2f-f1eb-32a3-be37-053108c3e5ac | -2.18949 | -53.65025 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07476ec1-1a4e-329d-9bc2-a144bc8106b3 | -2.48149 | -47.80359 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cacbb9a1-94f7-3a49-b426-855b43e4980b | -2.4992 | -51.79448 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebb6cbe4-cc29-3464-bd0f-99e755fa7f30 | -2.51624 | -51.79716 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b82abc6d-4d07-34ae-9940-945676c64838 | -1.74049 | -52.02955 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11d6ab5b-50f4-3a50-abda-4e1225ff7712 | -2.45344 | -53.98729 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17b277bc-0548-352a-9d22-ac99c50548e9 | -2.00218 | -54.51782 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e7257e-2f57-30ba-8024-7a0476f1b009 | -2.48221 | -53.71335 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45b45443-4653-3ec0-a45b-fc8d4e3334eb | -2.50144 | -51.80236 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9679da4-3754-33eb-9a2f-8bf6cc38ab09 | -3.63515 | -50.23651 | 2024-12-13 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53d40c8e-1ea4-310f-8a65-97f7aa08a354 | -4.02401 | -46.88292 | 2024-12-13 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9fc39249-11ef-37f6-8bc3-45c5eb550857 | -3.35982 | -42.3064 | 2024-12-13 04:42:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1f071429-fe28-3511-8ca7-ab45901fa205 | -1.61928 | -46.66772 | 2024-12-13 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README25.md)
