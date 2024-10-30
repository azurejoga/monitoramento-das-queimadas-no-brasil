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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10784db3-9277-34ab-8060-53f7242f4429 | -6.14691 | -47.2398 | 2024-10-30 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52ef29b1-ebbc-366c-a2bb-96a7b6621f9a | -6.134 | -46.86787 | 2024-10-30 04:19:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09f484d1-888a-3e1e-9135-b81cec05f003 | -6.05007 | -46.60238 | 2024-10-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb09589b-405a-3cd3-bced-c55eae2fdb52 | -6.04665 | -46.60181 | 2024-10-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b715e1e6-5c94-31bd-b5ca-55fce728c982 | -5.78499 | -46.61126 | 2024-10-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c1cd54-aa64-3133-8cac-2826a9b3248c | -5.75233 | -46.50978 | 2024-10-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cf97cc7-94af-3ae9-bec9-6bc67225e89e | -5.73261 | -47.04253 | 2024-10-30 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dfb4d91-7060-365b-a210-9eb42514bac1 | -5.58781 | -47.26299 | 2024-10-30 04:19:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 984edbb3-fa83-3e62-9d3c-2139720da803 | -5.53771 | -46.53392 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9600f0be-0271-328c-8288-d7d49dc40bfd | -5.53427 | -46.53337 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38c05722-340d-3eed-a9bc-2e4702f75083 | -5.50919 | -47.16547 | 2024-10-30 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fcb02acf-7a69-3788-8072-8790b8096568 | -6.36314 | -47.91545 | 2024-10-30 04:19:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb67aae0-bab7-3e73-bd2d-560bdf4a0f4e | -6.36246 | -47.91959 | 2024-10-30 04:19:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c00a9e3-ea5d-3de6-bf16-2f0cf004d11b | -6.03674 | -47.93621 | 2024-10-30 04:19:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2e9a0af-a4a1-3705-a3aa-677d2a7c600b | -5.07033 | -47.80915 | 2024-10-30 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf639462-431e-3098-a948-c26564f0384e | -5.39053 | -47.15917 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ade74fe-bcea-3f66-8210-deed76c0441f | -5.37651 | -46.57359 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 546ad415-ac1f-3258-b7ce-c0161c96c540 | -5.3759 | -46.57737 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db302c11-7707-395c-b83d-eed8fdf39678 | -5.14514 | -46.85613 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e97b34c3-858f-3962-96bf-eb0dc1e817f0 | -7.04274 | -47.62345 | 2024-10-30 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a16689dc-b3b0-31c4-9ec4-b39cc22428c7 | -6.88336 | -46.83798 | 2024-10-30 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 50c2cf2d-7257-37b5-bcbd-85568f0917ba | -6.88054 | -46.83368 | 2024-10-30 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db897c6e-2ce4-30c9-b4d0-ba4e15276e32 | -6.87993 | -46.83743 | 2024-10-30 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfd1cd10-b370-394b-9310-56efd1888672 | -6.82158 | -46.78601 | 2024-10-30 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17d62ffe-c292-31ee-8a8f-171799f15764 | -6.81815 | -46.78545 | 2024-10-30 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e8260de-56fb-3339-a781-947958a9df50 | -6.66363 | -47.09238 | 2024-10-30 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3b3d6f1-6853-3e38-a64c-c14995007217 | -6.66301 | -47.09623 | 2024-10-30 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a8d7db2-71b0-3aeb-b80e-2187a0418be0 | -7.43661 | -46.93768 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9bd04dc-f47f-3441-b85d-3a08e1f6e72a | -7.3645 | -47.23064 | 2024-10-30 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20c12d99-efa2-354c-9c52-069255b9d4e9 | -1.6049 | -47.24594 | 2024-10-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89c367b5-469d-395d-aeaa-1bd6d61a74a6 | -1.47874 | -47.33256 | 2024-10-30 04:19:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87814f5a-0487-354e-93b2-c059d90850c5 | -2.07452 | -48.21893 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc5c42fa-d51a-3367-a7d0-2e661e1b38b6 | -2.03004 | -48.19698 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a51a20c-f373-394c-8be2-442d8dbb13e7 | -1.98378 | -48.75641 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2cce398-91bc-3293-a62a-647329372253 | -1.87245 | -48.55844 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 387a4602-7746-3bcf-b74c-8c607ed8de48 | -1.8671 | -47.82272 | 2024-10-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454c3e84-431b-3705-ae7e-b87a5fd95abf | -1.34972 | -47.75083 | 2024-10-30 04:19:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e845353-153f-3812-8c59-c5680edb2330 | -1.0572 | -47.63913 | 2024-10-30 04:19:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 478ce7a5-34fd-3bb2-b296-b6a240bb29a8 | -1.05338 | -47.63853 | 2024-10-30 04:19:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7337cda3-a32d-3697-8766-d3bc038cd1b5 | -2.42631 | -48.8865 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 532e08a9-0a8f-3176-989f-bf373f51b96c | -2.19032 | -48.82265 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77f53b0a-9ad3-34d3-a989-7757b0f35eef | -2.14059 | -48.79273 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1997c1b1-b74c-32fb-a520-9859b438c880 | -2.97766 | -48.78346 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 312f7e8c-4d49-3ddc-97f1-4979acc5e04c | -3.28146 | -48.81908 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cf7a454-0c04-3665-9706-3a58d9adfbf3 | -3.00065 | -48.94886 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72d2525f-6221-321f-b93e-1b41b209c768 | -2.93363 | -48.02292 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 429f99fe-12e4-3859-96c1-780411de698d | -2.93288 | -48.02763 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71145469-1248-3702-a88d-20b7cfaecbe5 | -2.93242 | -48.02544 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f7851df-330b-35cd-a3ef-26950d700ade | -2.90803 | -48.61681 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 237cd08e-361d-37b1-a751-793750b6c2de | -2.85647 | -48.46177 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e76189da-07f7-3f24-b10f-aaf886d1c5d3 | -2.80308 | -48.67053 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87746cc0-98c0-38d3-a34d-fba936778109 | -2.72642 | -48.73982 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61978672-99ee-3dc0-aad0-2b7af34f5cd9 | -2.72198 | -47.74222 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65b2469d-4810-3675-8cee-72637e06d216 | -2.69947 | -48.6389 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1cfc062-a421-3306-b7f7-c2d02cfd01c4 | -2.69604 | -48.63485 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89c8ac04-9fc7-3f81-acf1-8427acce1495 | -2.69495 | -48.64172 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63f10efe-cebd-34c3-a159-dba8b7efc10a | -2.65999 | -48.53088 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5b722c7-4856-3501-82b3-62baa960b1c6 | -2.63553 | -47.96538 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66f28afa-d8f3-3a2d-8f80-9dc259337718 | -2.61659 | -48.3271 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be231ed0-ada2-3fad-8fa9-bd20149efbc0 | -2.61023 | -48.36669 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d484671-f06a-38c7-bc17-6feabe25640a | -2.60816 | -48.25551 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3c65a49f-73ae-3aab-86c3-b0cf15f9eed0 | -2.60218 | -47.93377 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a26d2e51-ba6c-3508-bab0-b66dc59077a9 | -2.58456 | -48.14505 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f3ec8c-968f-3023-ae4b-f8ffb5829e64 | -2.58112 | -48.39773 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76ad04f5-3d21-3c92-8cb0-43b7bf122183 | -2.57719 | -48.39712 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fa6338f-bb4b-30db-a505-e15894847ffc | -2.51119 | -48.1336 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5d236a2-4e3e-3fb0-bc2c-9368f07332e6 | -2.4512 | -48.47826 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34a67631-7c02-361b-8b86-d9de58cdc0d3 | -2.44956 | -48.48835 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edfb508c-6c76-3162-9303-0066ce9a7ffa | -2.44566 | -48.61266 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51b3bbb5-198a-3e2a-bc1d-e72c64748cd7 | -2.4433 | -48.47702 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 076aaea6-a07d-3d72-86a4-a76a69c8e650 | -2.4375 | -48.51255 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17bb4175-ebca-315d-9933-12a4dd6e1d7a | -2.40844 | -48.54925 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e831afc-c0e0-369d-925b-d404ad5527ba | -2.39166 | -48.57817 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0115f380-4901-36e0-8b38-e99b316c956e | -2.39111 | -48.58162 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fd8889e-b113-36c3-a1b8-321b588f3ff1 | -2.38768 | -48.57755 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acfba5cb-d6d4-3925-b926-a71bc283f416 | -2.31547 | -48.56983 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8befef27-a63b-33d3-aadf-af2f510fd61c | -2.30344 | -48.57809 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143ddb8e-e48f-34a7-982b-74cfec1b55fb | -2.30289 | -48.58156 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68812c69-b629-3eaa-8555-4adb34f5f103 | -2.30185 | -48.5782 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49ae80d2-12bd-3263-8560-b51b3bb38994 | -2.29131 | -48.49996 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ad4d507-556d-3b14-be43-3ebb96c343f7 | -2.28735 | -48.49931 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0b15ff9-39d4-3411-958b-b39d85efe57e | -2.27092 | -48.06788 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8040e241-b87b-3141-8fa3-7b66353baf75 | -2.26842 | -48.07011 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25eb7115-35e9-3062-9ebd-6190a2335934 | -2.21997 | -48.23964 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eed0aebd-b121-3118-845c-3ec503001e79 | -2.188 | -48.81132 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e01c19e-2ce4-33f8-932f-fe1af8997195 | -2.16393 | -48.38923 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51eff96a-d4d4-3a3f-bc5d-5a2cf056d280 | -2.12925 | -48.37868 | 2024-10-30 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cf9552d-d7e0-31fc-bf16-624cf5d34feb | -2.58875 | -47.47631 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9db5edaa-b8e3-3808-922e-2879b9446650 | -2.58659 | -47.47966 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a3b0e1f-20f5-3bf7-9223-ce29b66b13ae | -2.54087 | -47.51429 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ba0b403-061c-3fdc-aa66-084076b3a0b1 | -2.53715 | -47.51368 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b9889f9-bb98-3bb7-812a-a2cb175eac63 | -2.51739 | -47.44692 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9cbd13a-8ca0-308a-8be1-135a8bcd401d | -2.51368 | -47.44636 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68464f04-e65e-32c8-9481-7631b20986fa | -2.51297 | -47.45077 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd029244-9be5-3371-a78d-03e4d27c0fcd | -2.32069 | -47.48318 | 2024-10-30 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 096067ea-e1fc-32fd-8234-58aa3c63c18d | -3.00009 | -48.95242 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb2dca1c-04a2-3190-bd4a-3ec532b5bf72 | -2.93623 | -48.02605 | 2024-10-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1335c1f-7d6b-3df3-bf22-9798036e6777 | -2.84941 | -48.45555 | 2024-10-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16ebbbd5-22e8-380b-9029-ce29c3c9474b | -2.80362 | -48.6671 | 2024-10-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d554f4e-819f-3224-a3e8-407b714a0af5 | -4.48714 | -48.11756 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README41.md)
