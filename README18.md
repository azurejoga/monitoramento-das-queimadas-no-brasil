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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7162a09a-5736-3331-876a-15e8ef9a05b8 | -4.93877 | -41.54189 | 2025-10-18 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 03e4c652-b7e5-3ecb-80ef-766cea3ac8e1 | -6.74044 | -43.81465 | 2025-10-18 04:00:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 945743ab-1d6a-33c8-bf8b-60cc8499f885 | -3.83415 | -47.40364 | 2025-10-18 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2bcb4d49-895c-32e8-bb3d-958cd68c3458 | -3.2831 | -40.88559 | 2025-10-18 04:00:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9db6309b-fa00-3ac1-a4bf-e820d07c293b | -5.8865 | -43.92482 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e793af4d-2d28-31ff-b8e9-81ce9d81de84 | -4.2473 | -48.36876 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83e69eb0-5828-3ae0-810a-0eb0faf3278b | -4.40559 | -44.36635 | 2025-10-18 04:00:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4173ab81-2958-38f1-b716-ede6365f4689 | -5.06727 | -38.03448 | 2025-10-18 04:00:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d9f8c82-e7d4-3485-a0b4-1e7ccf9bc917 | -4.68982 | -48.62662 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18aeddb4-7fde-3b87-92ae-4379f959ae46 | -4.54226 | -48.41208 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e8f0c5a-da1f-33c4-829c-d9ddeab911bf | -3.4698 | -50.023 | 2025-10-18 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0af11ba8-350b-3aa9-9447-ad20295dea16 | -6.29986 | -44.72153 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e3d17a1-063c-300a-9476-c235ac617b64 | -3.8148 | -51.69875 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4d46bdb-c194-30da-9b11-eb1a78f98593 | -5.83638 | -40.8218 | 2025-10-18 04:00:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54c8173b-9bc9-386c-b9a5-e7eb01ed5221 | -5.3722 | -45.95386 | 2025-10-18 04:00:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19ca169c-3414-375a-9bbd-87af546f114e | -5.53645 | -44.09519 | 2025-10-18 04:00:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34b8e01b-46f8-39b6-9608-1577f95b2cb2 | -3.2917 | -50.00851 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a1ab38-81ed-37c8-8a3d-438e1c4f187d | -5.34695 | -41.20459 | 2025-10-18 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 53b097b0-87af-382d-b42a-440d4bd03875 | -3.84978 | -41.58512 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f587ad14-6425-327e-a08e-f1b2cd02c84f | -4.17136 | -42.20822 | 2025-10-18 04:00:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7904209b-ba9c-389c-ae4f-7b1e876a9ae1 | -5.5165 | -45.90632 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00cdd26e-7930-3e91-bd05-19e79a2f4414 | -3.69688 | -49.56317 | 2025-10-18 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41a8a9a2-dfb8-35fd-b87b-8762ba51fa9b | -2.74482 | -49.39285 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d037c692-8d79-385f-8982-9b26ad418642 | -6.14463 | -44.29348 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f7711adc-f350-31dc-9d4a-3e58ed79ae40 | -2.57157 | -49.11757 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c81eac3a-4f9d-3b12-8cfc-23b90edb5ab5 | -4.94042 | -49.76425 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cf51728-d838-3fa2-a93d-b29cba01e67d | -5.45888 | -41.01233 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 226fb6ad-21be-39d7-a6ba-32e5f1f7b90a | -6.23043 | -44.14624 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c244b4d3-5eda-3477-b594-9f3611534a37 | -6.52716 | -41.49151 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0ec8f831-eb11-3a23-8eb0-e05ab5da9015 | -6.26162 | -44.34083 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec76a2de-3751-3e17-bcce-a4bfdf3df592 | -5.728 | -41.30914 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 08f00419-c0f9-3605-ab35-5d7ec4e9afef | -2.22612 | -48.36802 | 2025-10-18 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33ea21e9-79f2-3e10-80f6-6d05467930d0 | -4.97706 | -48.36626 | 2025-10-18 04:00:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d18f0a69-c6bf-3dc5-987c-a5a80921a8a6 | -6.30042 | -44.71813 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 34cebd50-f7b5-3c60-838d-8f5fed22bbb1 | -4.45614 | -43.23428 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 2f38056f-8778-373a-9323-d42be0ce306e | -3.32299 | -42.79081 | 2025-10-18 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a683a71-70fa-364d-99ce-25e50eedcccb | -6.30439 | -44.71875 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16b3a237-568a-37c1-8783-a5c7f09c8015 | -4.00444 | -45.50269 | 2025-10-18 04:00:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9d114788-aed7-37e7-9e34-154f91f86e3b | -5.16752 | -45.21857 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90f3402c-9028-386d-b21a-006cdb011303 | -2.87892 | -50.72263 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c12be25e-794a-3466-be69-5f65434ef7c7 | -0.89965 | -47.54263 | 2025-10-18 04:00:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69f34dd0-e1d7-31e3-9168-36be343ae4a9 | -6.10425 | -45.85051 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4be4c9b8-7e73-3cc4-be42-a636566d0ec7 | -3.93915 | -48.08624 | 2025-10-18 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f1214c4-335c-3a97-8270-e3e5fe576a28 | -5.5318 | -44.09942 | 2025-10-18 04:00:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09b929ab-9107-3a0a-91e6-8eb6a6a28c7d | -4.93699 | -41.55305 | 2025-10-18 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 50361c88-28a1-3785-8741-13e46d040560 | -4.29204 | -48.26313 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b668223-a210-3083-a802-085ceaafe3bc | -4.71617 | -44.36079 | 2025-10-18 04:00:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| ca812e9f-6e33-3fe1-8670-170e9f7b7338 | -5.16804 | -48.60477 | 2025-10-18 04:00:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cba52aa7-faa8-302c-ae8b-dc89fe1c253f | -4.45542 | -43.23874 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| f9f4a1f7-2137-3693-a12a-9a516b0c2606 | -6.63968 | -40.97184 | 2025-10-18 04:00:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 823c2def-f8ac-3890-96e3-0f3820cae6ed | -5.30503 | -44.84909 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c1b8b7a-c9dc-3cb7-8187-1d56400aeddd | -6.23811 | -44.14744 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d0f7ab7a-c10d-3522-b7e9-7796d05c4c71 | -3.45145 | -50.09592 | 2025-10-18 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c09809ce-d2dd-33a2-9746-6f40408191df | -4.42129 | -40.16871 | 2025-10-18 04:00:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| de5744fd-e5a8-3efe-8447-ece8d58556a2 | -4.96208 | -45.08371 | 2025-10-18 04:00:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7f4b0aa-163f-3325-966e-f93706f17286 | -4.82433 | -45.23823 | 2025-10-18 04:00:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf2aac13-6e42-3694-a4e7-74db41f86e22 | -4.4517 | -43.23815 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ad123b9b-26e5-333b-90a9-0dd2568205f2 | -4.28124 | -44.6188 | 2025-10-18 04:00:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d10ecb3-4eb3-30fb-93e4-f499ecfb8aa6 | -2.92491 | -49.17857 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 09623e1a-7096-3de8-b788-43471f76ec17 | -3.51556 | -45.98743 | 2025-10-18 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4149c25f-f46e-3a4f-adc7-6a8b6b536af2 | -6.74638 | -44.36278 | 2025-10-18 04:00:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb6ea4b4-a8cc-34d2-9904-7cc2aea52b8d | -6.84247 | -42.41779 | 2025-10-18 04:00:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ee094c74-376b-3505-8c6e-526316b80f55 | -3.49892 | -42.72332 | 2025-10-18 04:00:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b55d946-9bab-3096-be4f-689fa1d79122 | -3.59319 | -43.04599 | 2025-10-18 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 365889fc-dd7a-375e-813d-2633daeb6887 | -2.87014 | -50.73642 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba9ad58f-b5e1-3104-950d-a87b14ea48bf | -7.22175 | -41.16663 | 2025-10-18 04:00:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5236aa03-83d4-31f2-8c19-5ecef6c5d653 | -6.23165 | -44.64822 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 321ec4ce-0353-3d53-97d2-689c88a5ef02 | -2.87267 | -50.72161 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6a91c56-464a-3cef-967d-69074b169bbe | -5.89783 | -43.90308 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b25d012f-fcd3-30dd-a1e4-13d46f9e7bd8 | -4.11818 | -42.91146 | 2025-10-18 04:00:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a454f053-b21d-3290-8901-72244ed8e4c6 | -3.8522 | -41.5699 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 956f59a6-c814-3b11-8b85-3a03bd6105dd | -3.82136 | -51.69978 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a8fdf5c-96a4-3734-86ad-fed8a326c97f | -6.35441 | -45.75763 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09de7002-ed9f-3729-b2f7-56de9272e42b | -3.06022 | -43.21731 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e1a48be-f407-374a-a75f-dc306445f540 | -0.9049 | -47.54337 | 2025-10-18 04:00:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3295ebf-305f-3ebd-bc50-b139a982aaa2 | -6.84429 | -41.71341 | 2025-10-18 04:00:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0ebfca3d-4561-3ce1-9ec2-a82726a39c3c | -6.23122 | -44.14156 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc5f28ce-f9a5-37ca-8dc6-7cf3e8340e04 | -5.1256 | -45.12554 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6cdc3c04-89bd-3a46-a069-d1a81c2861bd | -4.70057 | -45.19904 | 2025-10-18 04:00:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a250e0e1-5adf-31cb-ab2e-477ed17ca0de | -6.54846 | -43.91598 | 2025-10-18 04:00:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a79f15ec-22ef-3d02-8aa4-9a1945c080a8 | -2.8764 | -50.73747 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1df10847-982a-379b-a96e-6c736820ab0d | -3.14804 | -50.25443 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e048f3d5-9046-38d3-9336-fac84caf7873 | -4.78272 | -45.3078 | 2025-10-18 04:00:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8ce14ea-3577-39ca-8489-0aba4309b42c | -6.17646 | -44.86111 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d26305-bc70-3982-b699-f4cdbaddac16 | -6.21072 | -44.67692 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b95070c6-7ac7-3cbf-8fe5-68f6268e5e54 | -4.45014 | -43.2242 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 57e723b9-82f6-3ccd-b227-ac77acb3f5c2 | -5.59964 | -46.38304 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5fbe89f-562c-31c8-a763-9bd8d447d378 | -4.93403 | -49.76734 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb2d4645-e705-340b-8457-f7d272163fca | -4.97175 | -44.61485 | 2025-10-18 04:00:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62f4bc0a-c322-3943-aa57-5898fec296d9 | -6.05717 | -43.4043 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4fcdc18-6ae6-3837-a3b1-66eaf7986ffa | -2.74073 | -49.38889 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 349aa8cb-9f44-3b1c-b333-8548006209b1 | -6.60269 | -44.44497 | 2025-10-18 04:00:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c321fd3d-b46a-3dc1-943d-1d09043cf9cf | -3.51764 | -45.98576 | 2025-10-18 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7880efd3-f514-3a70-81da-a5e09e60d0f6 | -5.35753 | -45.03719 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36052920-a6e7-387c-889f-e177c4974c7c | -2.71136 | -49.41645 | 2025-10-18 04:00:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40e8837a-f888-32c7-a381-af0e99be1968 | -3.14098 | -50.25017 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9988335f-d58c-3a2d-982d-6377e23b8fb1 | -12.75181 | -48.62979 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2cf23ed-9d41-38b3-a1d1-4ebc1ed10097 | -10.70583 | -44.56691 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f67c0df7-e302-36d1-841e-ee90e07acef3 | -9.24631 | -43.76661 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b5e027c6-271d-3429-a7b5-e9b40695fa4c | -13.43027 | -47.98185 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README19.md)
