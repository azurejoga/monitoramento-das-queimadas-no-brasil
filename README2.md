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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83acd85c-d555-3d00-9916-e6e27c7c7744 | -9.29596 | -45.48212 | 2026-05-23 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 23b55266-8f47-3dd5-95d1-0146f29f7a1a | -9.97337 | -49.09652 | 2026-05-23 00:11:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1578cdc9-1352-31ed-9504-cfec73755eac | -11.18916 | -55.9221 | 2026-05-23 00:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 140.3 |
| eb65df1e-123e-3c72-95b3-9141f2d42fc7 | -11.18211 | -55.90302 | 2026-05-23 00:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b11e5660-a89e-39b7-9cc1-c9058616eb43 | -11.175 | -55.92393 | 2026-05-23 00:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 600dac62-99d8-35f7-8111-aab90ec4cc49 | -8.71446 | -47.92364 | 2026-05-23 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13254662-d0f2-34fa-a4f2-03b56f245f7d | -6.21809 | -46.88534 | 2026-05-23 00:11:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 00385094-a630-3e9c-b3a1-baa09a6e6f61 | -5.78042 | -45.13465 | 2026-05-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 236e2e87-4638-312a-bdba-7927f7528b30 | -9.2861 | -45.48368 | 2026-05-23 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 09d86824-cc7a-338d-96b1-614c17d1711b | -9.29763 | -45.49346 | 2026-05-23 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 6601f93c-cd81-38f6-a7ee-1cf526d90632 | -11.4534 | -52.9212 | 2026-05-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fd50b42c-7f4f-311b-ad35-78f77a813d56 | -9.2855 | -45.483 | 2026-05-23 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 54afa09b-6649-3872-a161-b8c573326cc0 | -11.1712 | -55.9319 | 2026-05-23 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e22a0547-ace6-34fa-8977-fd9ee5385375 | -9.3041 | -45.5036 | 2026-05-23 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 891db00b-c8aa-3537-8892-4679a592a701 | -9.3045 | -45.4809 | 2026-05-23 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| cdab6fb2-ece5-3440-b726-4bd22ee9f3c8 | -11.1903 | -55.9101 | 2026-05-23 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| e6724873-462d-32ac-aca2-066ec842390f | -11.19 | -55.9303 | 2026-05-23 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 840d8070-e907-32dd-b501-c7d24c60d700 | -9.2852 | -45.5058 | 2026-05-23 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 04daf8d1-e978-38c4-b18b-a1fb3ff7de7c | -11.1714 | -55.9117 | 2026-05-23 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| b940adc5-3502-3cb0-ae90-ff9a064c81a9 | -11.1714 | -55.9117 | 2026-05-23 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 9524077d-a40d-3073-a8e6-08bd936f25db | -11.4534 | -52.9212 | 2026-05-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 64d7ac17-9b39-336b-b568-0185f9454a22 | -11.0108 | -46.8095 | 2026-05-23 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 22c37013-edb4-3c40-975f-32b5d6536735 | -11.1903 | -55.9101 | 2026-05-23 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| ea76c3f9-dd6b-3b13-9c64-a139219aabc2 | -9.3045 | -45.4809 | 2026-05-23 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 18e5371e-4194-3ff8-b1ae-fe6e5b45e70c | -9.3041 | -45.5036 | 2026-05-23 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| cf806c67-355f-30d0-9a25-2ddaa873661b | -11.4534 | -52.9212 | 2026-05-23 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 2c3b8114-6f12-3108-a6a6-211593e2f678 | -11.1714 | -55.9117 | 2026-05-23 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 69739aa9-bdeb-3406-a7b9-7abfc6043117 | -9.3045 | -45.4809 | 2026-05-23 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 8238edaf-6d43-39aa-a60a-bd56985634df | -9.3041 | -45.5036 | 2026-05-23 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ac9cfcf9-c181-39ae-beb1-c48518d39597 | -11.1903 | -55.9101 | 2026-05-23 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| e336c276-413b-3266-92f7-1e49eab3dde1 | -9.2855 | -45.483 | 2026-05-23 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| bb8da88f-cb6d-3c99-80f8-1ed88c23abf9 | -11.1714 | -55.9117 | 2026-05-23 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| be68c62d-b5ad-3e55-8e81-bcff981b882e | -9.2855 | -45.483 | 2026-05-23 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 099f08c2-7645-3061-b8a3-92280891e047 | -9.3045 | -45.4809 | 2026-05-23 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b346c666-9b84-3133-a52e-ac122cd97684 | -11.4534 | -52.9212 | 2026-05-23 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 86c30d51-2053-3c01-b7bd-c5895b76d23d | -9.3041 | -45.5036 | 2026-05-23 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2e4cceef-a96f-37a6-aeb0-ba205fdbdf74 | -11.1903 | -55.9101 | 2026-05-23 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 3140d546-a42c-390b-b08f-0c14985d3b9e | -11.1903 | -55.9101 | 2026-05-23 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 6531ea44-18a1-33a6-b449-42c9aed1b43e | -9.3045 | -45.4809 | 2026-05-23 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6ff60c12-6418-3f19-86ce-1ab37d5a4a26 | -11.1714 | -55.9117 | 2026-05-23 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 06251112-7b46-3561-b111-bac6dea820d5 | -11.4534 | -52.9212 | 2026-05-23 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7d9f699a-15f1-3018-a9bd-351f72559a3e | -11.1903 | -55.9101 | 2026-05-23 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| ec4119a7-8f35-3421-8520-44e1d2e22be3 | -11.1714 | -55.9117 | 2026-05-23 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e6d50f6f-7bd6-32b2-9ca2-e5f35fe02795 | -11.4534 | -52.9212 | 2026-05-23 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| efeb5b92-671f-35cd-aa09-7c5eedac45b1 | -9.3045 | -45.4809 | 2026-05-23 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| bb953d5c-3dcb-373c-8981-119dbec822b4 | -11.1756 | -55.8909 | 2026-05-23 01:16:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad04189c-ce59-35ca-a729-7e9cb4077255 | -11.1707 | -55.9119 | 2026-05-23 01:16:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d72e7c27-a8f0-3e96-a5a7-e97cf3c16c07 | -11.4408 | -52.907902 | 2026-05-23 01:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cabe402-f371-35d5-970f-ef57bc412aa9 | -11.1803 | -55.909302 | 2026-05-23 01:16:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0061549-fe18-3c89-8e84-608631491e86 | -11.4534 | -52.9212 | 2026-05-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d26c74ba-e59f-3512-ab57-abcd605eb029 | -11.1714 | -55.9117 | 2026-05-23 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 7045e540-a1ec-383a-b538-816f3a0c0265 | -11.1903 | -55.9101 | 2026-05-23 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 40c99360-51b2-321f-85e0-88ebb9cb90c5 | -11.4534 | -52.9212 | 2026-05-23 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9ad616b2-ca08-330a-badf-af5e3bec506a | -11.1903 | -55.9101 | 2026-05-23 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| bb4a0abe-42b3-3e90-9f1a-855b99eb9571 | -11.1903 | -55.9101 | 2026-05-23 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 473786d4-7e2f-3775-9874-46b8aa489670 | -11.0698 | -46.6897 | 2026-05-23 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cea9b443-37c0-3c96-a900-008acb209ff5 | -11.1714 | -55.9117 | 2026-05-23 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 635fcdb8-df87-3cf4-9a05-cbaa5814770b | -11.185 | -55.924999 | 2026-05-23 01:43:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06ad75e7-29ba-39cb-b868-c1cc4f8b3a75 | -11.1903 | -55.905899 | 2026-05-23 01:43:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7229af-183a-3d9d-9752-fad36c5dc6f8 | -11.1861 | -55.889198 | 2026-05-23 01:43:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8fd5c1a-a54c-3bc9-a0b5-5d90fb001616 | -11.1946 | -55.922501 | 2026-05-23 01:43:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2adad6f4-f8eb-31b8-ae61-79c4a42a22b3 | -11.1807 | -55.908401 | 2026-05-23 01:43:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb3881c9-5740-36f3-bbc6-ecd56a402827 | -11.1714 | -55.9117 | 2026-05-23 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 44cc5e7e-b34d-39b7-8f6e-c85dc7409607 | -11.1903 | -55.9101 | 2026-05-23 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2cb1a7ba-aeef-39eb-9303-188aaa98df79 | -11.4534 | -52.9212 | 2026-05-23 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 28713718-d82d-30c4-a196-c8382d3ec79f | -11.1714 | -55.9117 | 2026-05-23 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0f373d48-62ea-3ba1-9df5-6df74c917cb0 | -11.1903 | -55.9101 | 2026-05-23 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 1944d29f-fb25-37c7-bb38-802c262da79a | -11.1903 | -55.9101 | 2026-05-23 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 44101675-1f0b-32e2-810f-1ada3f4b5e40 | -11.1714 | -55.9117 | 2026-05-23 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2830c215-bcb9-373c-a64e-ebd3262c61a8 | -11.1903 | -55.9101 | 2026-05-23 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fb13bab7-162d-3c8d-aa8a-b0d7902de5a0 | -11.1714 | -55.9117 | 2026-05-23 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 47444362-c14a-3ada-ba1d-b91279083d64 | -11.1903 | -55.9101 | 2026-05-23 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d1f03f03-0987-3e5e-8f96-503d385516c1 | -11.1903 | -55.9101 | 2026-05-23 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b94aa36d-6a62-34fd-aa4a-8b8263d9a5e7 | -11.1714 | -55.9117 | 2026-05-23 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f976932f-4cee-3448-ad01-34be2c6ac4aa | -11.1903 | -55.9101 | 2026-05-23 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 485b5134-947e-3656-973e-f0fcb3c4f0ae | -11.1714 | -55.9117 | 2026-05-23 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ab72f5db-2dd0-3436-9c77-9dc895c8f162 | -11.1903 | -55.9101 | 2026-05-23 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b26378db-e2cb-33db-b524-73baff66bf37 | -11.1714 | -55.9117 | 2026-05-23 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1c61255b-d816-3280-a2fd-899f644022d4 | -11.1903 | -55.9101 | 2026-05-23 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e8c1a105-724b-316f-acfc-088dc5d9eede | -12.8859 | -58.1891 | 2026-05-23 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 7a9d3329-81e8-3615-87f2-3b5c4bf575d0 | -11.1903 | -55.9101 | 2026-05-23 03:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 356e9347-2ff7-3f61-bf42-3b2ebef4f26b | -4.47497 | -37.81544 | 2026-05-23 03:25:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cec5ef1f-c66d-3d9a-b88e-e64af6893854 | -4.47555 | -37.81207 | 2026-05-23 03:25:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6af84148-4e4f-3860-abc4-7e49b3e5b9e1 | -4.47438 | -37.81882 | 2026-05-23 03:25:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 05fafcd5-ba9b-3471-bf8d-291760178a3d | -8.58136 | -36.99704 | 2026-05-23 03:25:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36846453-6cfe-32d8-8f89-55dfdb5cbe9e | -5.1816 | -35.86114 | 2026-05-23 03:25:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| abb3ae1f-28ee-3aab-b2ae-1739d6a5a38b | -4.47613 | -37.80871 | 2026-05-23 03:25:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b6659d1-dd5a-3cce-8ea7-3eab753aa4b5 | -10.48014 | -42.41358 | 2026-05-23 03:28:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8bc4acfd-0c5d-3beb-b680-29a665c24aa2 | -10.47904 | -42.41908 | 2026-05-23 03:28:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 108fcf3b-e870-3f9b-b023-5215e734786d | -10.48126 | -42.40807 | 2026-05-23 03:28:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f40c0eb3-874e-3d83-9f78-b8418d0179ff | -11.1903 | -55.9101 | 2026-05-23 03:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| cc8b1358-11ee-36a9-8586-16028b740c15 | -11.1903 | -55.9101 | 2026-05-23 03:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b0976f99-b71d-3f00-9aa1-e0ff9bda6714 | -6.63935 | -43.91796 | 2026-05-23 03:45:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7276dfa-fbf5-33d4-b4cc-cc6961e125d9 | -4.47698 | -37.80931 | 2026-05-23 03:45:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9502d314-889f-3058-b13b-23fe75569596 | -4.36934 | -37.89621 | 2026-05-23 03:45:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cdaa10f9-fc73-37d7-9242-f125879dcc87 | -6.38887 | -44.17168 | 2026-05-23 03:45:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 64d1b25c-212d-3bfb-ad38-be71b87b6428 | -6.38945 | -44.16841 | 2026-05-23 03:45:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae01907f-6463-35b5-9d91-3b77ff75f343 | -6.39473 | -44.16935 | 2026-05-23 03:45:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 80e6a09f-2a4a-3b6b-98f2-a0e95c48a632 | -4.47564 | -37.8176 | 2026-05-23 03:45:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 98da7667-6a5b-3669-bade-9097512496b9 | -5.18011 | -35.85697 | 2026-05-23 03:45:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
