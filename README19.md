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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80481708-276f-3630-9114-85ae194223bd | -9.87078 | -44.68867 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4765a47-a781-3c43-8f5c-6387dcbcafe3 | -6.40982 | -42.50506 | 2025-08-18 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9ddebddf-c392-3c9f-b60b-320000eabfe0 | -5.9923 | -44.13232 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b798df0f-6523-3df0-923a-6e88fb5bac3b | -9.51856 | -60.5405 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 85a17d40-a097-3a1e-83d6-d98dc91cdd14 | -8.79366 | -52.08264 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4feb42-22a8-36ea-b74b-b2366796ffc7 | -8.82309 | -52.04813 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f33b02a0-8d02-3d67-a9c2-986ad293f384 | -9.4006 | -48.28794 | 2025-08-18 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5491e76-5237-3285-a898-aa40f35bec0b | -9.97381 | -48.3322 | 2025-08-18 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d98fb60-e87a-3c9f-81a9-9f7488b9ec37 | -6.43162 | -44.77491 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c01c0f1e-cc47-3262-ab30-b130dab312ed | -6.55615 | -44.47901 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5df72df2-705f-3256-9746-06d2f41749eb | -6.67759 | -43.67277 | 2025-08-18 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b8734b5-a158-3cd6-bf31-9733d2fc8ca4 | -9.86475 | -44.69785 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2e4bb37-3de0-3afe-bc4c-3d0b11412d76 | -6.56328 | -44.47227 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e38e3ef1-d992-3191-9363-41eca214324d | -8.78032 | -49.99736 | 2025-08-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7c90e78-b0a9-3882-83d2-b5d8a15f6c69 | -6.05876 | -44.12753 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0de994a6-30a0-3d67-abc5-2598f2b741a4 | -6.5001 | -53.37626 | 2025-08-18 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 711e580b-633f-38d8-92a5-b9e37db8beb8 | -8.82089 | -52.04064 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0699d532-f028-3fe8-a16b-c17da64efb56 | -6.57324 | -51.51494 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e458dacf-c12c-3c50-828f-a6bef5c91fe4 | -9.51731 | -60.51826 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04d2b88f-a3ba-3871-861c-9a186bd4c57a | -10.67667 | -51.56487 | 2025-08-18 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7124e9f-db0f-31ce-9ee1-08b857436a00 | -6.1463 | -57.93448 | 2025-08-18 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cdaccd31-a9ed-397d-be03-4e9bf0272e95 | -6.32803 | -44.71294 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f35e286-5ccf-3296-b560-78efcd91338d | -5.99694 | -44.13274 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6e2ef03e-4f38-3f60-b4d4-cb21ba5082cb | -7.56656 | -45.42608 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8aa5173a-ffee-3f64-af21-db27d679df9c | -8.79721 | -52.0833 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77c1ebd9-66d4-30ed-ab56-00d9270b0197 | -6.15092 | -42.70453 | 2025-08-18 04:46:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 10ea4777-a050-3ccd-a5bb-4d73600f50f8 | -6.42659 | -44.77853 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 119ae7b4-6600-3220-9094-c69b68cff434 | -7.56967 | -45.4351 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c57a5d35-0e27-3178-b5ce-bbbe44c2625f | -8.82035 | -52.06556 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9905381-9b56-35c4-ae11-6dd126bb864c | -6.15646 | -42.70212 | 2025-08-18 04:46:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 930be53e-8852-3da9-98a6-6c4b57843464 | -9.51223 | -60.51733 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1136d26e-0988-330a-b444-b45e17115820 | -7.02055 | -44.27737 | 2025-08-18 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b957bdf4-af3e-388c-aca8-91baa5fe098e | -6.98403 | -41.63158 | 2025-08-18 04:46:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 31889936-4b27-318e-adf6-a4614f6d65fd | -7.55073 | -45.44485 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fac04452-fa54-3603-b1c8-eda835c1e772 | -6.3529 | -44.5351 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ed56e3b-cea5-3186-9b7a-c63fd09e6f0a | -11.8068 | -44.94014 | 2025-08-18 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96bab30d-44ad-3e60-97fc-87a272548f1e | -6.41021 | -42.50235 | 2025-08-18 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9eddacf-8f37-324f-88e2-bd1c09c4355c | -5.50531 | -49.21882 | 2025-08-18 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4a0e542-d1a1-3b60-8d11-95853016f7d7 | -7.80678 | -45.15788 | 2025-08-18 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1726edb0-7a49-3af1-bff5-f7b3a97dab04 | -8.06423 | -49.63618 | 2025-08-18 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 701480cd-2aee-3e2b-a561-d5abd9d021e2 | -8.23823 | -47.86127 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dbdc3ec-c73f-389a-a56b-3568d1893b3f | -5.9802 | -44.11948 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| de75a798-8b2c-32ac-bc2d-30ecdf9b72c5 | -8.78089 | -49.99367 | 2025-08-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 897664f6-d90c-30b8-987b-e2574ebc2a13 | -10.99825 | -45.65312 | 2025-08-18 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aec39426-d56a-3575-92ed-88ae81c16cc5 | -6.56783 | -44.47277 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aaf5a503-33c3-3c94-9e39-25ac87920a81 | -6.57113 | -44.47144 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 37652f43-0e7d-35d3-80fc-c2531e1ad591 | -6.96089 | -44.23707 | 2025-08-18 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8512417f-9e53-3322-b7aa-612e8875d3b4 | -6.98497 | -41.62447 | 2025-08-18 04:46:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 53402378-61c4-333c-b4cc-3c8d2d02c9be | -6.52574 | -43.42841 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5222a497-f538-3cbd-81a1-7945c0e85f50 | -6.03667 | -44.3428 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed76696b-a5fb-3ede-9df6-8b297f19cef2 | -6.95625 | -44.23647 | 2025-08-18 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e15e28d1-cb24-3857-897b-fe7db2dc70d0 | -6.56234 | -43.01323 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7ef2b95-145b-3305-9e40-a272556925e2 | -8.23597 | -47.86362 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5b7ab34-a1fa-328e-ad8d-caa9e3c2a984 | -7.19886 | -43.9688 | 2025-08-18 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 066f2524-f80f-3c07-9fc2-cd86af4b28f5 | -5.03172 | -49.60222 | 2025-08-18 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4b274a7-4911-30b1-8fb8-7cba83cc7abe | -5.49364 | -51.15646 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edfa329e-c2bf-3405-b02d-eecd2ac59224 | -12.18871 | -47.23346 | 2025-08-18 04:46:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52f1b176-4607-349d-b8f2-b8acc44b53c2 | -7.56716 | -45.42186 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54c4b88f-5afc-3bd8-95ad-fd5399168263 | -7.91492 | -51.37356 | 2025-08-18 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b810fb6-3e24-379b-9ec3-9bcff7179c2a | -9.51457 | -60.53347 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52d3938a-ad3e-33a0-ac00-03912f6abce9 | -6.87944 | -43.12446 | 2025-08-18 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6130746-065e-329f-9c27-ec4a12f218aa | -7.14088 | -44.38972 | 2025-08-18 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb24b99a-b484-3d5b-8d75-efb1fa6c22c6 | -5.99825 | -44.12342 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0172d49e-8b53-3934-8417-f3c6286fa96c | -11.00332 | -45.64927 | 2025-08-18 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 830439be-21f6-399d-978a-9d81c0f4b61e | -6.79813 | -44.72753 | 2025-08-18 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b21681-1e23-3130-9fef-781785fb16fc | -9.87225 | -44.69505 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae7f43bf-653f-3da2-8653-6710149ca476 | -8.80983 | -52.02468 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6030ba2-adc1-329e-8c9f-232a852bc480 | -7.5476 | -45.4359 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62da8416-9275-3ffb-9eac-5e1f31cf8eb1 | -8.20324 | -47.33196 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ee9a65f-429f-3241-b015-11f1b0fac762 | -5.92104 | -50.00422 | 2025-08-18 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90f90521-3b06-31c5-9a8b-5a8aa080b3e8 | -7.53602 | -50.52863 | 2025-08-18 04:46:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 493b72e2-a68c-3aa0-8359-21bf2538ef7d | -7.01024 | -44.28867 | 2025-08-18 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c0573aa-cca8-3a4e-b0cf-d8b3ce08fb47 | -5.98767 | -44.1319 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4fb6a6b-7a0e-3562-b06f-04965f6be522 | -9.29328 | -50.27364 | 2025-08-18 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774f12f4-2fba-3403-bc35-4c9999ef5604 | -8.2195 | -47.30032 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc55797c-6b8a-3620-a6f3-e69eef47af0d | -6.11623 | -46.67152 | 2025-08-18 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 864e527a-f346-3cbb-9ff4-08ad8f18f4ee | -5.98832 | -44.12728 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8c3b5a0f-c131-314c-ab47-b2541c3f24b3 | -11.66804 | -46.88099 | 2025-08-18 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c42a1150-8b2c-3cd8-9f75-19bb6780da5f | -9.86693 | -44.69931 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ffc0219-d291-3f57-9575-b4e66ad52534 | -6.19256 | -53.51541 | 2025-08-18 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c63f95a3-9122-374b-8149-bf9abae0a2b8 | -10.96702 | -49.57005 | 2025-08-18 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73400f30-5eac-3895-ae2b-78b0784c070b | -7.55502 | -45.44554 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93b68714-bd0d-3889-bddf-cb39ace2dc1e | -6.9845 | -41.62804 | 2025-08-18 04:46:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8c2730a7-b703-3e91-b22d-1efa5cd2f56e | -8.19983 | -47.33941 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 354e139c-0d72-3e19-a443-5048158b6bc5 | -16.74397 | -44.99644 | 2025-08-18 04:49:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 778caaca-7758-3543-a3de-4fb0ac6f574f | -11.31112 | -55.21811 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0cb68a5-d4a2-30e9-b4f4-dc5f95e40a5a | -11.31535 | -55.21462 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6850bccd-7071-3ba9-84fe-d83b6ecd1020 | -15.25468 | -49.5224 | 2025-08-18 04:49:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 833d4d83-0a2c-36a2-b917-a70d10029b4d | -13.0214 | -56.84864 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bff9d41-b15a-3c1d-832e-9f0194b3b7c6 | -15.11926 | -48.73256 | 2025-08-18 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37ec76ab-357e-3150-9ccb-82794b55c379 | -13.4506 | -45.88685 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f14395ea-ed51-3c67-b24f-cf4ffcdb5a2e | -16.73856 | -44.99885 | 2025-08-18 04:49:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eed49c64-4c2d-3d37-944e-08512b6d3781 | -13.23326 | -50.7489 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3c6c4074-4393-3ee6-8ae6-e44e5460297e | -13.57523 | -47.00052 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 718c5f43-ffc0-3e6a-b4f4-67cebd98484c | -13.00629 | -56.84592 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 790d0429-cf49-3680-b1e1-ec0932ed4eba | -14.18429 | -45.3374 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85e40f96-54cb-31a4-9fe3-a3ebb5e27a66 | -14.98966 | -54.79166 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9ef725b-1bab-3244-bc4c-b82caaeadaf8 | -17.09396 | -49.87463 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bc342c4-6f8f-38b1-8ea4-14b607e9a2c8 | -14.63464 | -54.90126 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97c3aac2-c4d0-3045-8000-9a959be93b95 | -15.86784 | -50.2126 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
