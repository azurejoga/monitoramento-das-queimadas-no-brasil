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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d7f383f-11a8-3b15-9384-ad44c90a6ba1 | -13.02518 | -46.76085 | 2026-09-12 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e8610a5-a82f-36ae-8c79-a82f16019c31 | -6.61294 | -44.20546 | 2026-09-12 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4843969-fbb9-3a85-8eb9-7c876e5d0ee4 | -5.26007 | -50.97427 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ace3339-c9b9-35db-a759-5a991d3d553b | -5.81013 | -53.81527 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f78081de-508c-31d3-89ca-6377921ce8ba | -10.22161 | -45.19624 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88f57bbc-127f-3049-ad39-f1a270683978 | -7.18621 | -45.92221 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 139c5309-e2b1-3e06-b6f9-2aa8a84e8b3a | -6.19974 | -55.26601 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d07de83-2b76-3a91-8cba-2140f661904d | -7.15904 | -45.86748 | 2026-09-12 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1e531fa-0784-32f5-abfe-b9c3953db114 | -9.52185 | -40.33293 | 2026-09-12 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3027f19a-03e1-3980-910a-6435531706d4 | -8.9527 | -49.52694 | 2026-09-12 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9cbfd69-7c32-3f84-9fc5-ef973cdbda4a | -5.81299 | -47.22656 | 2026-09-12 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb473d29-8c9c-339b-91e0-6e418a1bc7d9 | -7.05453 | -42.72453 | 2026-09-12 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 56922ae5-964c-3822-95bd-9c7c54e4342d | -6.34301 | -55.30155 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 060887b4-6b98-3487-986d-cde374314c7f | -7.03364 | -49.20513 | 2026-09-12 04:34:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2533a43d-70df-3de4-ae56-c57f2ca7adca | -6.41064 | -47.38409 | 2026-09-12 04:34:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 246bdb8a-9193-3f7b-894e-3a0f93348cc2 | -6.66699 | -50.91082 | 2026-09-12 04:34:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b2d8f14-b595-3309-8b08-02fe947757d8 | -12.13054 | -48.95723 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c539566-e4ce-3b89-8fed-c5c568c5ed3b | -12.20469 | -49.39755 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9a3a3361-fa1e-3e87-ba43-105e0eda043c | -11.37862 | -46.83985 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b48fbf53-fff7-364f-b1e3-4c6c356be993 | -10.49887 | -51.36774 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eefd26b-6a11-3485-a06a-5ec68eefaa00 | -6.61443 | -58.84224 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4c4bcaa-1abb-3c98-8b49-bc11f5f9ca4e | -6.07942 | -53.49805 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 201847c7-1062-3a8c-8dd5-ba60440c5d0f | -8.82078 | -46.91014 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5414a10c-cae3-38ff-bce6-21f36d98f312 | -6.34214 | -55.30653 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17cc58b8-7b8d-325a-859c-f115ca165f2d | -6.84308 | -55.25078 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 71a75154-d451-3e23-9c60-35a3e8f02402 | -10.82616 | -50.5863 | 2026-09-12 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 052d4526-004c-36dc-80d1-4bcbd732a0d4 | -9.3042 | -44.34323 | 2026-09-12 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4d2dd72b-49aa-3d0e-b8d8-253ea253746d | -6.24559 | -51.69791 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a6d90ea1-223e-3754-923b-f00a2dd8aa18 | -11.25338 | -54.13505 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c948125-ad1d-307d-82ed-7bb02e1df5ec | -7.40823 | -44.55261 | 2026-09-12 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3c99a87-a841-32cb-b102-5e48ef3661c8 | -6.10981 | -55.64958 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76496e5f-a9e3-3bd2-85cf-5e77e9a76aa6 | -5.85643 | -53.87289 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81837a4b-7d8c-33c7-8622-406847c39d02 | -10.63955 | -46.11504 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c824efef-322a-3307-b5c5-22accdfda856 | -12.11843 | -48.96966 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ee27157-fda6-34d8-9440-cf29c024503b | -6.12215 | -55.63531 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90edd984-36b8-35c5-bfa3-906ea7db49be | -6.33032 | -43.36086 | 2026-09-12 04:34:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d162c9a-d769-30b6-811c-64790d8c8fe7 | -11.37109 | -46.79499 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b452cf3f-d583-3a0a-b54b-a944d24fceb6 | -6.16728 | -47.08864 | 2026-09-12 04:34:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf07576b-159d-3741-9d93-deb834e5e88a | -10.55223 | -45.21127 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 062f909d-e364-3106-8160-5d58b62c6a8c | -10.54412 | -51.37494 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ae0fc09-793f-3d79-b4e8-9d07ae51a9ff | -6.17581 | -57.7164 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8bc5c603-4e68-3a5b-b280-abe6b8ed8259 | -10.14538 | -36.20607 | 2026-09-12 04:34:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0e9eb8d4-f355-3ee4-9e6a-b780792f04fc | -11.37341 | -46.8272 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f996d394-ba8b-38df-bb7c-f2d50f5cea1a | -5.81571 | -53.80799 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 017072d5-ef38-331d-a935-a2f5efd1fb36 | -7.18967 | -45.92273 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb7d2737-b97b-3688-bd3f-87f8a3d50879 | -8.12024 | -54.79113 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d3d3340-79b3-392e-86cc-8e0870e0dd50 | -5.81771 | -53.79588 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc13a321-f296-3e63-8248-e154b72d4937 | -9.7019 | -43.46146 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdc8e0e6-224a-3993-b60f-4440af51ae97 | -6.51078 | -47.61709 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 198a226e-aabc-3d7e-84f7-fd5300ff5d1e | -6.84391 | -55.24594 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 06324e94-41c9-30df-897f-69738dbe111e | -9.91214 | -46.24043 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| b4fcdb33-5f59-3c05-aaae-fafdbe487578 | -11.24604 | -54.13002 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c7767ea-bd41-3c1d-82a6-cc38f0abe949 | -11.39079 | -43.98389 | 2026-09-12 04:34:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbf6d9ce-ff07-3352-9561-1cf245738ba1 | -10.73059 | -50.61957 | 2026-09-12 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d4fb903-1af0-3c3a-835f-82de59914cba | -12.13444 | -48.97583 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5b4bdb4-e347-3bf7-804b-2348854be907 | -8.50837 | -50.15147 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc3f22b1-2f56-3cd5-a0d5-20b258b3ebb8 | -7.18335 | -45.89437 | 2026-09-12 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ae59777-bf8e-30c0-809c-41c36a43c2c9 | -6.33622 | -55.85367 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68a5946a-4cd3-363d-b070-711263eca6ca | -10.55552 | -51.34888 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 556863ff-2f89-3002-8647-0b9e2f95b918 | -6.23664 | -51.68275 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c64dbcfd-aabe-3649-9c1e-32bb8d8a9bbb | -6.40415 | -54.9772 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 712256ff-5d47-31c8-bff2-b5b70c6a2c52 | -6.20442 | -55.26684 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac7ca8e5-5917-3948-8f2d-e45920f61341 | -6.11847 | -55.65678 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a55e45e-0e50-3ccc-8e18-4b9377f824ad | -6.28767 | -56.02037 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd987a93-3398-3c29-b740-2d65cf88cae6 | -11.2004 | -46.33358 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bcc03a4-1c36-30b2-8175-544a00f126a0 | -6.52231 | -47.60824 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e75a9646-c247-362b-8e6f-3b3a6b3297ba | -11.23494 | -54.14637 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 716032d3-3abb-38b4-b715-b1bf67694a80 | -9.92561 | -48.52963 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2642511d-b61a-3cd5-9414-18f2a5cf3cef | -6.8464 | -55.80426 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ccce7d6-0fee-3aae-ad07-c906b1cea775 | -8.39021 | -46.30085 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 508db333-c909-3d0c-a392-fbee72815b10 | -7.42108 | -46.15026 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15437217-0796-3d00-befe-93320b6f5816 | -8.57839 | -54.57642 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 699b9ca8-6d86-3606-b90a-2cedcfc30dab | -10.45942 | -48.66135 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32469261-cf67-3889-9faa-d988f3704e61 | -11.28028 | -47.5644 | 2026-09-12 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aa712cf-cc0d-314d-bc4f-62f1a211075e | -10.50922 | -51.30523 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b53e6037-9ea6-33d1-9820-59f9728e2d6d | -8.81686 | -46.91314 | 2026-09-12 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 676345d2-4ab4-39e0-928c-8107c1075fbb | -8.49644 | -54.65299 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b703cc9-1dae-3179-beca-9475e71ae9ef | -6.61285 | -58.85094 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2ebe5607-6671-34bc-a204-903515efbab1 | -6.43176 | -56.108 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0219fa50-fe69-3c74-ab0e-39bcfd76cca0 | -10.54851 | -45.2107 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d5c9d72-f411-375c-b4ce-d489c9036d08 | -8.57479 | -54.57169 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f523e350-5b21-3e8f-a4fc-d613b216e19f | -5.80028 | -53.82183 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2d3c778-994d-3260-9a6f-39103b195613 | -12.12944 | -48.96429 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7e5a739-c3c1-3f6f-af47-f0b665b8db8e | -11.06014 | -49.51776 | 2026-09-12 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11d17a5e-c526-3d3f-9388-365625a017eb | -5.96297 | -45.9647 | 2026-09-12 04:34:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8b9fce0-fa9c-3c4b-a1ab-fd2658202b2d | -8.45866 | -51.54234 | 2026-09-12 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 523a0a6f-0fc9-38f8-a756-ca3323c8eb86 | -12.64399 | -47.09101 | 2026-09-12 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8476bc0b-2ada-3a6e-a46e-c3f6b8734cad | -7.12009 | -42.10442 | 2026-09-12 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9e810ae-1452-374b-9755-46852b34882b | -8.034 | -43.85854 | 2026-09-12 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e3b97a22-aa7e-39cd-8b45-3a8e11641a81 | -6.10885 | -55.65514 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f893258-bff3-3fec-9ba9-36bb841f3b44 | -5.98025 | -57.76402 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55d8d932-7f4e-3332-9f4a-354e7c117122 | -10.22322 | -50.36802 | 2026-09-12 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c947e4b-0160-33e9-9f12-a8142c1f1f5f | -11.24479 | -54.13712 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 674da873-6b05-3204-8914-ee21ce6312d8 | -11.2732 | -43.25113 | 2026-09-12 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 827caf95-07bf-3ffb-a1ee-a6a78cb8af56 | -10.55025 | -45.22478 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2e1e485c-01b3-3d57-ba3a-87fc3cec2fe2 | -6.83597 | -43.19802 | 2026-09-12 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7cac666-276d-377a-9dc9-e03bce10e5e8 | -12.12614 | -48.96375 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89820c57-5a51-3e29-91f3-8d9d6c3b2e42 | -10.63063 | -46.12623 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7732da3b-b0ce-3f94-a5f4-51d54765225d | -10.60477 | -50.58764 | 2026-09-12 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c160a017-83b7-38b5-a201-c3ca755f7bc1 | -6.85769 | -47.43945 | 2026-09-12 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
