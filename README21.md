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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60d3e5b5-5508-354f-aead-5b39bcb7cf40 | -10.65169 | -49.45018 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1beeeae9-d282-3b7e-a65b-03b99a5f47db | -12.53059 | -57.20832 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e81d1cda-81ad-3043-a1c5-fbb303f44cf4 | -9.45905 | -57.8507 | 2025-06-19 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6dfda327-9ca5-3942-8ea4-76140ff37e3b | -10.83909 | -54.01097 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60bb680d-691c-381b-ac98-3ae55d402ed0 | -12.20615 | -49.6296 | 2025-06-19 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82c4a54f-cea8-37d4-aa2b-3106ed265f5d | -9.79125 | -47.18402 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac812d17-4fd0-3321-8d6a-20090bd8a704 | -11.96464 | -58.73601 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8e71cd3-2d85-39d7-9ba6-5639ba51718b | -11.9619 | -58.75353 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9be58409-d9b8-3064-bbcf-c627a1b66b04 | -14.4392 | -48.90826 | 2025-06-19 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9166e361-94dd-377e-9ffe-c2e6df33c925 | -12.0241 | -57.10067 | 2025-06-19 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3ff088f-5d5f-3da5-93b7-91e801a7b33f | -9.49085 | -56.08708 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 53bdb21c-a318-384d-8d92-d95e3116b0dc | -11.62515 | -58.29351 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 569b5b2d-86c4-346a-b7a5-b534d4aa9f66 | -11.95698 | -58.73832 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ceafee7-1c36-3f9a-8e71-6ba6944e6bd2 | -9.37795 | -47.63809 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4908fbc1-0b53-38ba-ad7c-f72ceb8b2591 | -12.47206 | -58.46863 | 2025-06-19 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48dfffdd-6400-386c-8df1-cd3d527dbb87 | -11.99179 | -57.20126 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b5ae413-dbf5-36ac-8bd7-54d1ea91c11a | -13.96198 | -56.79004 | 2025-06-19 05:12:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2128f8a1-7513-3ed9-936e-16f4d8ad0bf8 | -10.64603 | -49.45265 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53db966b-4379-3c92-827c-1b74b9b86ba8 | -11.11797 | -53.98946 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b3b15fa-1867-3ca4-b203-365a61175e63 | -10.85321 | -53.76532 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ec5ea26-a22c-37ee-8781-94880bb54072 | -10.64561 | -49.45589 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a499e90a-38b6-3aa3-a673-b3df75e4db98 | -11.95753 | -58.73482 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78075549-410e-3ffb-b7c1-8961ed42a3fb | -10.64478 | -49.46236 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea297d18-2f28-3db4-96a4-3a443f588f8c | -12.46875 | -58.46811 | 2025-06-19 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2aad440a-45ca-3d21-b403-eb320cece6b5 | -12.79527 | -48.73078 | 2025-06-19 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ca8b427-d802-3613-b52f-462c33c88326 | -10.63995 | -49.45841 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a502551-649c-3a1f-9968-97252a552d7c | -11.66087 | -58.25964 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 10d59d83-6c57-3c10-8a4c-2aa045cc6b74 | -13.5097 | -55.65397 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b9b66b7-26d2-3906-bc9e-7be560fbe0d9 | -9.49714 | -56.09192 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62779bea-6b5f-3ebe-b652-cbd316d139f8 | -9.49771 | -56.08814 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 96fdb5f4-8bd1-353a-bd9b-52eae97bf49b | -13.7944 | -54.29869 | 2025-06-19 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71a84ced-b658-376d-9488-267a6d437792 | -11.25946 | -52.47132 | 2025-06-19 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 322a657e-b4b7-3ce9-be20-5973ee1ebc71 | -10.30309 | -57.13911 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a258320b-2b30-3203-8683-97d37f97e43d | -9.8963 | -48.02502 | 2025-06-19 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 719de9b8-bba0-3ade-8019-950f6e05a90b | -11.96029 | -58.73885 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 98ef08bb-1034-3bc9-822b-39fef8ef11a4 | -10.23572 | -52.23109 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58c8fa76-b222-3c3c-8516-9163df656569 | -10.84461 | -53.76925 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc66218d-0390-3786-85e8-739f851de771 | -10.84676 | -53.78183 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30fb5410-2dd6-3be9-bb24-789b550e550a | -11.9471 | -58.75827 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd34448b-ea00-3d37-bed8-c70c7b95462c | -11.07132 | -55.03997 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a6d7fef-a61c-32f5-bf67-4216eac5d453 | -14.21542 | -45.51931 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0604be4-c2d7-3547-b5f7-cfc5b8eae07d | -11.93665 | -48.42693 | 2025-06-19 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1af07275-1c30-3c84-a6c0-88b073144c42 | -12.42713 | -54.87394 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5af8c816-836e-3563-8402-239570dadfab | -12.90444 | -56.97717 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b0faf9e-a91c-35ac-9d16-2bd329afb627 | -10.85462 | -53.78298 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4befffd-64d5-3c68-bf82-598440bd8eaf | -10.85715 | -53.76586 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 616b6ff1-5b8a-37e4-b557-9aaa44baed25 | -11.9504 | -58.7588 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed043890-b342-38bf-bfcd-428ceac892e8 | -11.32933 | -45.21173 | 2025-06-19 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aaf01b4-722d-309d-b623-59d2f8dee171 | -11.33625 | -45.21253 | 2025-06-19 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47349fdb-86a6-35df-a0e8-47f916a37f91 | -10.08785 | -52.74126 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c9e6d1a-a439-3182-a6fa-7c00cd2b5176 | -10.51095 | -53.57879 | 2025-06-19 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85c904ca-53b9-363e-bf4a-481c5047d372 | -9.46289 | -57.84775 | 2025-06-19 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aaed4177-b028-3f1b-9158-2c701b74e3e0 | -9.40015 | -63.13517 | 2025-06-19 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb4489ce-9827-35d5-b98c-e28a98cdb72b | -9.0025 | -61.52505 | 2025-06-19 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ec06cc4-ed9d-3945-ba1c-70b856102780 | -11.9537 | -58.75934 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 22652d3f-7d8c-3e4a-8d6a-5e88d793f2b3 | -12.52436 | -57.20356 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9be5e2b5-ccf0-3cdb-b4b0-48c24b2035c8 | -11.13683 | -53.94093 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94e69417-8356-3e63-abf5-efb969d2d3a1 | -11.95314 | -58.74129 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cda411e-62f2-349a-9657-f7dbaa19d551 | -12.02749 | -57.10121 | 2025-06-19 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe4563c-7131-3627-bf50-98c4a54f69cf | -10.9748 | -59.16414 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cc1df5b-9f62-31fd-8248-6488dd144005 | -10.66884 | -56.55431 | 2025-06-19 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef1d6ea2-c496-3e4b-910c-d55e3229f90b | -14.04299 | -56.05532 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b75fb61b-d097-3c1f-8e59-96417dece395 | -11.95534 | -58.74883 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f519bf7c-2fb5-341d-aa14-04cb69c4d6e1 | -11.52773 | -56.99565 | 2025-06-19 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45e6c24e-2162-3528-9297-e2dbee71239d | -11.12902 | -53.93973 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1339d043-8a8d-3a5d-8a09-2fa889569449 | -8.70906 | -50.04737 | 2025-06-19 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3ceeffc-9819-3949-ac87-a5a1d04ca2ed | -14.20996 | -45.51726 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b1673aa-d513-3d57-bb20-1ce4e4561a09 | -11.14609 | -53.93432 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 786a1063-aa97-38ac-9a0c-c71d9b7c15eb | -9.89682 | -48.02098 | 2025-06-19 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d4c17ce5-66f5-34a5-9bd5-deb797bb4ec8 | -9.49485 | -56.08384 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 122ec5a2-822a-3f00-b120-6c5c17a67c29 | -10.08182 | -60.49939 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d137a9f-3e91-348e-9d0f-0ffb1da19b34 | -13.95793 | -56.79343 | 2025-06-19 05:12:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fb8dde8-e25b-3b5d-9d07-8df8e7f9c479 | -11.94325 | -58.76125 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c58d8ed3-c2d3-3054-a944-93256afb29e1 | -12.53004 | -57.21202 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce738554-91e4-3ab5-be07-45724ee7f4ec | -10.85031 | -53.78548 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29652453-2b51-3697-bd89-fedc4c6a1631 | -9.50115 | -56.08867 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd06069f-8494-3299-a9d5-e832f061779e | -8.71921 | -50.26543 | 2025-06-19 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a10e0f29-341a-3c36-8abb-36a1f6abef14 | -10.66202 | -59.29037 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8653608-d6e6-376c-a899-f8c09efa5985 | -8.96196 | -47.98027 | 2025-06-19 05:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ac58989-f7c7-30af-aa6a-d9c99bfe6f4c | -10.27912 | -60.53922 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1cf8fcf-1684-3e39-a6c0-6484e6ed58dd | -12.80047 | -48.73569 | 2025-06-19 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85933d03-6c86-3f78-ac9c-c4e91251d35e | -9.01536 | -49.59124 | 2025-06-19 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b2cb9da-20b1-3ef4-a14b-15e43158b4d3 | -9.15607 | -49.64015 | 2025-06-19 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bb5daf9-4d04-3000-8b4e-9004f2b05c7b | -12.53589 | -57.72137 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4be29a2b-3bb4-3fd2-b5d8-1e0e1a9dc187 | -13.50981 | -55.65174 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a0f4aa8-3d69-3e5d-a9ee-f6ee65117bef | -11.62184 | -58.29299 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 275a72a0-80fa-3248-9346-a5a2df042f30 | -12.49243 | -58.4683 | 2025-06-19 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee470729-38ae-35b1-8c9f-2c6e182e30b9 | -13.58233 | -59.20173 | 2025-06-19 05:12:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03705d1c-3136-398c-953b-6427fc64d3e7 | -11.52434 | -56.99512 | 2025-06-19 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5da2bda7-7c9e-3672-ba8e-935a45782663 | -9.49371 | -56.09138 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e07c9ff-b23f-3e28-a6a5-0aafafcdca74 | -11.77122 | -54.36465 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa7a1882-c3e1-3fbc-8a5d-5474095c0886 | -10.8442 | -53.77117 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2aae90ad-0734-33d6-8c00-63e6a5f58a1c | -11.95425 | -58.75584 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 88962848-438e-301c-a38e-418d5dbd0fac | -9.2531 | -50.03179 | 2025-06-19 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 436355a5-dbd6-36b6-a647-8f7ab3f6f6ec | -11.62569 | -58.29 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a5506da-cc0d-3753-a782-0786301092d0 | -12.42777 | -54.86928 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b31d1869-3b76-32a8-8acb-ff471c41f831 | -10.65128 | -49.45335 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0eabf414-de17-34ad-8ff5-b17fa52eb710 | -11.52884 | -56.98829 | 2025-06-19 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 054c7f6e-d864-3a6c-9668-0ab822ae9ddc | -12.37721 | -57.40307 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41caa5d9-ad0f-32fb-8f33-10192fc3c10f | -11.61854 | -58.29246 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README22.md)
