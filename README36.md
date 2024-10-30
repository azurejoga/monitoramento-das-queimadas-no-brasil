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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94d48964-e6d3-3469-9bcc-3c643519fe24 | -6.54695 | -43.91453 | 2024-10-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ba2706e-0b8c-3b76-b0fb-bda2c41f5fe3 | -6.5158 | -43.65456 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5627e133-bc74-35e2-98d3-a94494642b55 | -6.51301 | -43.65052 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3533d5d2-e78a-367a-b0ca-ec6fe9c778a5 | -6.51247 | -43.65404 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2c01b2e-6e52-3f27-934d-443ee4c8c343 | -6.51192 | -43.65754 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 681c1885-33ed-3a46-8615-5a25cf9f0b33 | -6.40403 | -43.63003 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39591ebd-2483-3a9f-8382-b76e0ca30047 | -6.13939 | -43.51685 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88097887-2217-37b6-878b-21d1d9810e0c | -6.13118 | -43.56955 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e638b8c7-94dd-38ba-9ed8-959de7743d3a | -6.12785 | -43.56903 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33346b5b-da05-3f6f-8afd-3c1b264ddd0c | -6.09006 | -43.54878 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ed3ec72-1080-3579-a1e3-5a4aa41f9dbb | -6.08951 | -43.5523 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1458798-2df1-37d9-bace-ff44442bf440 | -6.08673 | -43.54826 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6285a2f5-4531-356f-8207-22556f6e932a | -6.06145 | -43.6234 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9a4dfdd1-0a11-3c3c-80db-5d1cb0846bb2 | -6.0489 | -43.68245 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbae7845-98e2-3d1a-821f-a6dfd22193ae | -6.03437 | -43.5583 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa0f6ad9-646b-39bb-9aae-79ad79eaba6c | -6.03382 | -43.56182 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99c2897d-ae1b-3b3f-9511-9fe12e2a62e0 | -6.48962 | -44.23983 | 2024-10-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 377d9174-0333-3180-b873-a430b0c931d9 | -6.43998 | -44.18554 | 2024-10-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b272fb05-ae9a-3ca2-bccd-754e784f421d | -6.30704 | -44.8821 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01c6107f-385c-3225-b1ae-722288c0f5df | -6.3065 | -44.88555 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90bc583a-b205-338c-8539-e294f96fa0a7 | -6.3032 | -44.88504 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a8c8b3e-ed0b-354c-8418-418977bff7a9 | -6.27473 | -44.48137 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1364fc43-516f-351d-b807-b5cbf87d1b3a | -6.24114 | -44.12965 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fa94fed-4a24-371c-86cd-9d95b5579dc7 | -6.21369 | -44.6978 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfdabb50-b75b-3c35-ad2d-ae69690c68de | -6.19971 | -44.0913 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 897dae50-6d2d-33c2-8c01-aec6b442ad81 | -6.19182 | -44.20696 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85927a20-8a68-3ad0-9258-4f34ecb933e2 | -6.19129 | -44.21039 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8da29a26-9e88-32ee-a4b1-f6569a365942 | -6.18906 | -44.20301 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9c40246-4b94-3c36-9689-6da36fda21ad | -6.18852 | -44.20644 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d57c2649-440f-3c5b-9bd1-400707aadc42 | -6.14645 | -44.06099 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a280dfcb-07b9-39ba-b98c-333dfec5dc11 | -6.11336 | -44.42357 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 932a2908-6293-3ad4-8f66-735bec0f2088 | -6.10952 | -44.4265 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25f36e7b-6188-396e-8fd1-bc0371602375 | -6.07155 | -44.62529 | 2024-10-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b213badd-06de-3b19-9523-431f7ad4ab9e | -6.04442 | -44.77636 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 08f16198-c3ba-3112-ba11-1a5325ea4d42 | -6.04058 | -44.77929 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f6a4db9-2b58-38f8-809a-a598e559d5e7 | -6.03895 | -44.78962 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63cb39ea-8b17-3371-968b-7c88828b53ee | -6.03511 | -44.79255 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f54c0900-9fe0-31e8-80c5-1a5c001c30c6 | -6.03013 | -44.78118 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6b9e60b-7280-3226-ba60-bdfbb3705cad | -6.02737 | -44.77722 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b6e3bc8-3c7e-363d-a190-b661a09d7fe7 | -5.93997 | -43.68348 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 714e53c3-d8da-32e5-b01d-3795eb3afa0b | -5.93664 | -43.68297 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6c3a362-9fe4-3748-890e-819a4a79a4a3 | -5.93386 | -43.67895 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b582becf-3ca6-3d79-9ffc-1dbd273b486a | -5.93332 | -43.68245 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9127116-8240-358c-adea-b6dfbddba08c | -5.93054 | -43.67843 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c5eb2f-9791-384d-b881-8796754a5c13 | -5.93 | -43.68193 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be1cb794-d75c-3a29-9e1d-29f952d8a8c1 | -5.92722 | -43.67791 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d2ca430-97a7-357d-bf05-ee052b215329 | -5.92668 | -43.6814 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b18ef9b4-3ef1-39b6-9b62-044946afc8b2 | -5.92266 | -43.6414 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 473bf224-a715-3237-aacb-eb9a8f19003a | -5.83308 | -43.64858 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17665ad8-30ba-3b2f-acec-d5fb9dd348b3 | -5.83254 | -43.65208 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e2bbaee-6f73-33fe-8f34-a47af369b329 | -5.81721 | -43.86019 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 187e73ce-d7d8-37fb-b62d-d766519bd5eb | -5.7044 | -43.68937 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 368a9eb0-53b6-35ed-8db1-306a4919b275 | -5.70162 | -43.68538 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4e8625a-9d0c-34e3-8749-923cff689d75 | -5.70108 | -43.68887 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92f5a52d-aab0-3eb2-afc6-690ee968c873 | -5.69776 | -43.68835 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5817b6ac-5cae-3682-a3cd-ceb70c24618f | -5.68211 | -43.94201 | 2024-10-30 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2fa0d97-89ba-351f-a41b-d01abd59df07 | -5.68157 | -43.94548 | 2024-10-30 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4d79c16-96b2-3d3e-81aa-626194d15504 | -5.67826 | -43.94497 | 2024-10-30 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e03f5c2c-ce6b-33e9-a091-d7dea320a9c8 | -5.67265 | -43.91572 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe44f249-fa62-3508-aeba-36526ce1ae29 | -5.63323 | -43.79601 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b4dc4a9-29f8-30b5-8db6-62ea75107abc | -5.62992 | -43.79549 | 2024-10-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6d0caa8-0401-383e-862a-adac5dae6fc6 | -5.57499 | -43.71159 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8659edee-a6ce-31b1-8c0d-10100e3288d3 | -5.57167 | -43.71109 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b4abf7f3-93c3-325b-a26c-26a66a5f7146 | -5.54737 | -43.71445 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7737778-ed9e-30da-9997-1a1fec7e10f4 | -5.53098 | -43.77596 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6ef423d-d4f5-3b21-85f7-0d746bfdb981 | -5.52307 | -43.71782 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea31f51-cd57-36f7-a1b0-90d04113f662 | -5.52253 | -43.72129 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06aee7ec-8ff7-308d-8cc7-6083133a989a | -5.48806 | -43.65896 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed499124-1c87-34cc-ac90-d077e2afbb5c | -5.28253 | -43.9077 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ebfb3dec-44d5-39ee-959d-e6a22997ce85 | -5.28199 | -43.91116 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1863e706-1e35-35ab-89a9-1d44e1be17e6 | -5.27869 | -43.91064 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24ad3432-54b2-3619-9c1d-df7e89043330 | -5.92483 | -44.52124 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5853eb64-4b1f-3ee8-8cd0-4b6962a45ecb | -5.92375 | -44.52813 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 952a28a3-2b05-3841-b078-a4b7bce1c9d8 | -5.92153 | -44.52072 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b06e808-6b94-3641-b8af-3ded4bd93861 | -5.92045 | -44.52761 | 2024-10-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbfab981-0fc0-3f5c-8a66-46e9608fc443 | -5.87143 | -44.31878 | 2024-10-30 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e7fd39dc-4b58-37b8-b659-9d926d511028 | -5.86813 | -44.31827 | 2024-10-30 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d63b4b5-86d1-3409-a272-0fddde004c90 | -5.83639 | -44.36972 | 2024-10-30 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa4f11e2-3093-303b-a0ec-b0ce5f1578dc | -5.81515 | -44.28473 | 2024-10-30 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35ede857-fb91-3855-bb91-d50ebea00c86 | -5.81252 | -44.12886 | 2024-10-30 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea139fc9-bca2-3915-bda9-2d24cfc4f908 | -5.81198 | -44.13231 | 2024-10-30 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feab3f6e-abff-314e-9485-5f3a0b0fef17 | -5.80303 | -44.27579 | 2024-10-30 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5136d10b-42ed-3ea2-8e7b-0804900e0542 | -5.75845 | -44.45221 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1afb2d30-d7b2-3d72-aa74-ebf5924a7f62 | -5.55718 | -44.32536 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7196facf-0771-3f5a-b9ae-c0b1bb2127ce | -5.55664 | -44.3288 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a841c05a-bcf1-3621-a361-8e525ecc097d | -5.55442 | -44.32141 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d420fd35-73ec-3370-a452-d9ccc7d9d16e | -5.55388 | -44.32485 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 297fa00d-3229-36bc-aee1-442a1a26a732 | -5.55334 | -44.32829 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4da6a543-2530-3694-8d56-6835d3e3f26b | -5.55112 | -44.32089 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e9cf612-6bf1-3c32-adf4-4557a3669a67 | -5.55058 | -44.32433 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9813c7e-710f-3855-8548-41fea181ae33 | -5.55004 | -44.32778 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4081ddb8-f2e4-3b24-89a6-9c0ea903ae62 | -5.34056 | -44.18872 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0d5d0b6-9eb6-3ac1-a1d7-cb786d7b5ab7 | -5.34002 | -44.19216 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ad699a-a1ea-3e91-ac31-e40ff319861f | -5.33726 | -44.1882 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b9adbb4-899d-3772-9d2c-f5efecec8f07 | -5.33672 | -44.19165 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92e7b131-69be-3cac-bd2a-c20ecbafaf39 | -5.06339 | -44.21867 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8339d3e4-2e47-35ae-9438-b156be134410 | -5.05901 | -44.22504 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a27260c8-fb42-3aac-84c3-52871e5416c2 | -5.05571 | -44.22452 | 2024-10-30 04:19:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f88b95f-4f7c-3200-86f7-2e5832d40c2c | -5.96245 | -44.75997 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44fa0e2d-7755-344b-beac-fa72d9f846e9 | -5.95732 | -44.76625 | 2024-10-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README37.md)
