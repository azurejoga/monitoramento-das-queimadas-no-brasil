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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6711a5f-d8c7-31ca-b8e5-30df94a0abf0 | -12.84562 | -62.70011 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55d412b4-2e49-37fe-8d33-b1c591676a31 | -12.83735 | -62.69895 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21724bff-7599-3b9a-98f8-08d52015f4aa | -12.83321 | -62.69836 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee68cf61-a626-389f-9ecd-3bf1e5a2872e | -12.82907 | -62.69778 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fac33002-3d4c-3eb9-ad5c-dfe407512b66 | -12.82441 | -62.701 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4b276d7b-536a-378c-91fc-15647eb7f03e | -12.80121 | -63.01952 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 576beb7b-6a7a-34ee-ae4c-90d792a38541 | -12.34633 | -62.32249 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cecf7c-1ae1-371a-824c-c9987fe30a95 | -12.34208 | -62.32219 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b976bf17-f425-33d3-bd09-14b140812520 | -12.84615 | -62.69631 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cd29eae8-ffad-34e5-b0f0-1abf744b8b49 | -12.84201 | -62.69573 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c18c0855-3917-3ebd-8745-c0c830e6067e | -12.84149 | -62.69953 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37ef4cbe-717f-3d2c-9ee7-056bf4cd705c | -12.83787 | -62.69514 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b6c5d09-8310-3e6a-b3c8-4ed9054adf25 | -12.82959 | -62.69397 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d50d3bf9-8032-3f6a-be48-ffe6a54dfd04 | -12.82493 | -62.6972 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| caf47f8d-f478-36b9-91c3-052432ad236e | -12.80526 | -63.02009 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df70555c-09a7-3251-96c5-9ed12265dcbb | -12.58781 | -62.57654 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7b4f980-3cce-3b11-b947-162105d58075 | -12.13634 | -64.74624 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9b02fd3-9af5-31e3-a5da-85b3f147981e | -12.13208 | -64.74996 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd04c379-97c0-34cc-912e-70d21c407901 | -11.77012 | -64.26662 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78d2022a-56c4-3b8a-b0f3-ef9caac325e0 | -11.7697 | -64.24357 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b833ec0-f84f-3c3a-844e-91854988817d | -11.76946 | -64.27112 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a32d35b-f313-328b-8a6b-d7796fc0c156 | -11.76905 | -64.24803 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f584fb5-f4ac-39f8-84c3-3ef502391cc7 | -11.76707 | -64.2616 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a14b11b-f135-309a-9a63-812d2f8dc16a | -11.76573 | -64.27074 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8409f7b-c9c6-330f-a869-e7f85a6cf36d | -11.76509 | -64.27511 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99a41786-b049-346f-b4fd-1646a7f0db77 | -11.76137 | -64.27466 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fea3f476-23bf-3a68-9aff-6fc7e4463396 | -11.76119 | -64.22393 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6987dee8-efca-34a0-9f38-0660cd850a5d | -11.75747 | -64.22343 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 606f4c92-a7dd-3823-89bb-76e5846d70fe | -11.75022 | -64.27322 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 493fc568-eade-3137-bc4d-c5646bb082ee | -11.74959 | -64.27759 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c397566c-8039-3582-bf59-e8e6ff765a0c | -11.7493 | -64.22737 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4193d4a9-20a1-3380-bade-e0569f28b507 | -11.74586 | -64.2772 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b34f4999-da2d-3d49-a145-673be849b700 | -11.74216 | -64.27661 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57c59467-aa19-3a9d-ba6a-e6c007ca0c80 | -11.74154 | -64.28088 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41ebdb0b-e2e3-3a8a-baeb-b12a1ca203b2 | -11.73785 | -64.28024 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e34273ae-4592-3beb-a321-23c0ef4f109a | -11.73416 | -64.27963 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9712d132-6295-3951-81f3-8729a58fdc4a | -11.73108 | -64.27477 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c1a3b68-62db-36f6-81fc-61e65c288c7a | -11.73032 | -64.09439 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47147c54-0828-375a-ad2b-4aba4646bc8e | -11.72968 | -64.09895 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74d619cd-625a-3399-8ef4-7f76afbb1da1 | -11.72739 | -64.27415 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe314700-b396-322a-8d37-b681390875f7 | -11.7237 | -64.27349 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9db8916a-d46e-3cab-9e6b-1f39834be4e2 | -11.72065 | -64.26837 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a225a48-0429-375c-9f56-3931f670e466 | -11.71695 | -64.26778 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68352a7b-3400-3f83-a670-aabe23ff6a9b | -11.71523 | -64.12006 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d42ca1-cb36-3aca-97af-5bae412badd8 | -11.71389 | -64.26274 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b459c3a-e064-3e67-b94b-1559091764bd | -11.71019 | -64.26218 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10959a8d-aff7-3cc5-910a-b294c770b0da | -11.70712 | -64.25719 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1756de7a-67c5-3d96-85c4-ffe202c366d7 | -11.70648 | -64.26163 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a2d61ea-f9dc-3592-9da2-8dff467b33a4 | -11.70584 | -64.26608 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5a951b9-75b1-3d14-b572-9746c48630ba | -11.70341 | -64.25664 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 909afea5-1781-3188-b6c7-a44c11b49a11 | -11.70277 | -64.2611 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c5fa630-f9b7-3e8b-a167-eb7cde57acc2 | -11.6997 | -64.25608 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 718ad560-cf3b-3136-8e9c-6245e028b362 | -11.68978 | -64.07684 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85959115-28cb-3378-b599-583d282acc74 | -11.68614 | -64.24493 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6529866-6948-3ed4-855f-66dc16013e15 | -11.68361 | -64.06672 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b1828f7-8544-3ff2-9cbd-83fcecc41712 | -11.67254 | -64.19466 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 887d1d0c-b6e2-3b1b-8ad9-f7ef80638ab3 | -11.67188 | -64.19915 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70999bf4-d692-3462-ae66-ac9846cb4f20 | -11.67163 | -64.07018 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4c10179-22e2-3f81-9de9-5376f441c29f | -11.67037 | -64.07888 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e6e0c916-1e5a-36a0-8719-76bb60de82f0 | -11.66817 | -64.19858 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30f8391b-b565-39c6-8b10-1aa346004152 | -11.66249 | -64.2115 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7901a492-f475-32e4-b583-56fafc3d4882 | -11.66221 | -64.08246 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fea700bd-87e5-332c-9bcc-455f3b5c08d2 | -11.66159 | -64.08671 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3150a05d-93a6-3188-8e5a-ea21f59ec1a4 | -11.66094 | -64.09121 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e9c1eb-c364-34cf-be6f-c4b052476cc5 | -11.6572 | -64.09067 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7675074-87f6-3997-8014-0f168594e49b | -11.65654 | -64.09528 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb2dfc19-a362-332e-8da8-a8fac72b445f | -11.64214 | -64.00896 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7747745f-32d6-3287-89f8-8ac09e79776b | -11.56193 | -63.94733 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac4e9a01-e2cb-3782-bb23-527155126a22 | -11.55817 | -63.94678 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b08dfdad-f71b-3384-9a61-f130bd7f7165 | -11.5575 | -63.95142 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccc25313-b35b-30a3-a68f-d0590037790b | -12.5089 | -63.90991 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08e574fa-a623-3b78-8c09-3791b3e38671 | -12.50575 | -63.90456 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 95ad60d2-dedc-35d5-b007-1b904484a69f | -12.49842 | -63.95704 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6068b9da-b51a-3318-9900-181ff9b68c22 | -12.49776 | -63.9618 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d24184de-9ca0-35d7-9579-961532d9d6d0 | -12.49709 | -63.96655 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0972f36b-6726-36cf-8b96-df9e09a119b7 | -12.49395 | -63.96125 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 927f7b9b-a677-39cb-9f2b-0ce4736d05f9 | -12.49229 | -64.02859 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12341f47-eea3-304d-b29c-5919d5d0b33c | -12.4885 | -64.02803 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b965f18-d1a8-31f7-9d41-5672390df90e | -12.48784 | -64.03273 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ffa7a13-649e-373d-90fd-f02a25007e56 | -12.48339 | -64.03687 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b254e79-8c43-32e9-85b3-fa832a3276cf | -12.48273 | -64.04156 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5a18108-0511-3090-87c7-6686f092b51e | -12.4796 | -64.03632 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f86b0bf-1727-3151-827e-176e00659f33 | -12.47894 | -64.04102 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6806377e-8860-348f-9bd5-8af6fc79416d | -12.47646 | -64.03107 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2cc5f58-13d8-391e-b076-e0a8de5d2c06 | -12.47581 | -64.03577 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15ce12be-b6c8-31de-a046-7a9f2e4bb2cb | -12.4745 | -64.04517 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d91d26-68f4-3ca2-835c-04fa523e91b7 | -12.47071 | -64.04462 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 309dea85-9bf3-332b-99ac-c38e28206a5a | -12.47005 | -64.04932 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b37ad9a3-2a34-3c8e-9cd8-3847316c8d9e | -12.46692 | -64.04407 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5805f2dd-0271-3f71-bcf0-f3d951987749 | -12.46626 | -64.04877 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2820924a-7a63-3ba8-a37d-3b2dee6839d3 | -12.44348 | -64.40155 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8d35ae4-7f14-325c-a54e-e453aa9b5a47 | -12.44284 | -64.40604 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00696e56-666f-3259-bcb6-4797cee7311c | -12.30739 | -64.34493 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6a14b6f-c6ff-34c2-b7da-b189cebe3b9e | -12.30506 | -64.34703 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dba9e34-9a6b-347c-a1b9-c698b899e7be | -12.30303 | -64.34882 | 2024-09-26 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc34366-24fb-34a7-b1c7-3487cd98c150 | -11.96789 | -64.95527 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f07423a-1683-35c1-9f91-c766e5a8dfe9 | -11.96728 | -64.95943 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ee37ddc-fb51-3a60-b881-5b6d9cc3cfdd | -11.94929 | -64.9822 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6122b546-4ca5-3ea6-a59c-1f40c07f8b76 | -11.94571 | -64.98166 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d928ddd-d020-3207-8471-21bb2dc41225 | -11.94511 | -64.98581 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README164.md)
