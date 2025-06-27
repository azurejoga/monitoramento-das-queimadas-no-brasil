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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 560f7ef6-58a5-3f12-b839-6770514a3364 | -10.82624 | -53.74554 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52585f9b-f1f7-3b5b-9c74-8cf3c6b03f3c | -7.0175 | -49.18242 | 2025-06-27 05:10:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6471f54d-4f6e-3a5b-b819-4b87c0e46544 | -11.77636 | -55.0331 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79765ca4-3585-3037-ae05-94076a9d38b6 | -9.07583 | -49.43249 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51624a10-38fb-3b03-bf67-291dae1b1db5 | -10.8309 | -53.741 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b875ee63-b3f3-3ed2-92be-f3ad5e802c50 | -8.61905 | -51.57428 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d368f0e-0575-3ec4-b812-75e2591439fd | -9.12075 | -49.44805 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d4b1e71-b684-3640-b572-8a509955487f | -10.83033 | -54.05016 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad6aa69b-b3ff-358f-80d2-af8b791ce5bd | -12.02163 | -57.08242 | 2025-06-27 05:10:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f98694b-9c67-3e0e-8a94-d55ca6be2d8f | -9.75757 | -48.04582 | 2025-06-27 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0e1534-34e3-3a29-8af6-18961a3622df | -9.55035 | -63.5229 | 2025-06-27 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bbf41cd-b8a4-3827-9cd7-4b5124123ad8 | -11.6845 | -46.72713 | 2025-06-27 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e504a1e3-42eb-32e2-9878-c64bd7009b80 | -8.5461 | -55.03753 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69eb53ee-2d1f-3f9e-86ab-ae6ab891f1f3 | -8.47865 | -48.26381 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0233d924-731b-37ed-8df4-4ab5a89f5800 | -11.17887 | -55.91945 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 413346b2-871f-377b-bf0f-28912e082709 | -10.71198 | -59.13838 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a3dc8b4-2c81-3127-a054-3c085a351eb5 | -8.84495 | -49.8588 | 2025-06-27 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49035436-568c-370b-935b-65ae2f750541 | -9.75238 | -48.04109 | 2025-06-27 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dd99735-4de6-3c00-acf6-1f91fecf0bc1 | -6.17942 | -48.08585 | 2025-06-27 05:10:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 80385c4e-565e-3f29-872f-e8b879b80e2c | -12.02445 | -57.08664 | 2025-06-27 05:10:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8adaa162-e8cd-3585-a712-8944bc125d10 | -9.07194 | -49.42247 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b908ccd-4fbc-35e2-b235-5c5b08437ddc | -9.11905 | -49.43924 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 786bd2ce-22eb-3642-a4cb-36689a62387e | -11.57882 | -52.12429 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed13c1e4-bb70-32b6-a28d-f03c5ee883c9 | -10.6495 | -44.49205 | 2025-06-27 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73f4d248-db96-3fbc-b527-a2f87d95185a | -11.18649 | -55.91653 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a93a735e-ee77-34a3-86d0-60b6be056091 | -10.86065 | -54.0417 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bde1aed7-b65c-3bfd-8693-e30b31b0d25c | -7.53844 | -45.82554 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9cbe4e1-95ec-3621-b0f9-40d04b86c906 | -11.13508 | -58.61278 | 2025-06-27 05:10:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 611ccdae-44a6-3087-97bb-7cb57a1756d9 | -7.54477 | -45.82661 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d3e6624d-df23-39c0-89ad-937bbfa4b846 | -10.4193 | -47.51326 | 2025-06-27 05:10:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50fab47a-f9f5-3e4e-9eca-c77683d63cd0 | -10.71254 | -59.13484 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 346bdd21-e646-390f-bb50-8a3e7a8110e3 | -12.01171 | -47.16109 | 2025-06-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 207dbc6c-9ce8-3552-a434-cf0c54aa8f39 | -10.85427 | -54.03094 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86c30923-94fe-34db-b85f-a806c971ad6d | -9.0775 | -49.42007 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27c58c00-e5af-3df1-8da4-f4d2d042c319 | -11.06121 | -55.37503 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8e0499f9-8662-32a9-8c8e-cb7ea92a322b | -11.77702 | -55.02866 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16fc3dd1-5b34-315a-9f5e-c14f59b14431 | -10.63975 | -46.7055 | 2025-06-27 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daaff5ac-5491-35e0-951b-8010f2e94413 | -11.18708 | -55.91254 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f38c77d-f0d3-3e1a-b20a-c23775641358 | -11.07138 | -55.38083 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62110d8b-661f-35ed-b36d-427cbcb7e099 | -10.82552 | -53.75064 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 994a2ead-dd1e-3a37-85ad-8949804dd032 | -9.11826 | -49.44534 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bfe3156-f58e-3c80-a488-8480f6af15b9 | -11.06419 | -55.37976 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 46f13fed-aa3a-3548-9186-3f6d1aef6a78 | -11.17947 | -55.91545 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ef03bc2-cf5e-3424-b8fa-d393d3c53eda | -11.80967 | -57.35295 | 2025-06-27 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bfa0e7c-7749-32d8-b9b2-1409c420de6f | -11.05465 | -55.36974 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b8f562d-5606-35b2-ba03-9ff76f043c00 | -11.17596 | -55.91489 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667865df-a449-3e32-90cf-f6c8f9b4c4ab | -11.43233 | -54.47913 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf5e8023-d55c-3fe5-bf06-471d303ef87c | -11.44129 | -54.47085 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f068ed0-c6e0-3159-a8da-416670aafc44 | -11.05403 | -55.37392 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b5cec25-3a59-3463-a308-fe2b60715e49 | -12.0061 | -47.15533 | 2025-06-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81877962-491b-352b-9092-8faa61dd924d | -11.75753 | -54.22924 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9f0fbdb-d9df-355e-9a8e-50993f3976a9 | -13.05464 | -48.82325 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69d8435c-38f8-3aac-8d44-9bb04a9859f2 | -11.50586 | -61.82159 | 2025-06-27 05:10:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcb2cdd8-ab5f-353d-9ef8-3041decb4409 | -11.06928 | -55.06797 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fff75d2b-9aea-308f-8263-2139ac5e1b87 | -11.38551 | -56.54665 | 2025-06-27 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e93e010f-83de-3e30-8ae5-86ec50ffa444 | -11.44567 | -54.46404 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fec46879-f312-34f7-9377-9c21537283f4 | -10.16897 | -51.65208 | 2025-06-27 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d32a3171-cd46-3bab-ae13-d1a17ceefea2 | -10.85634 | -54.03409 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5c6c4b6-811b-3b1d-9264-87342f33ba13 | -12.02839 | -57.09093 | 2025-06-27 05:10:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0fd7570-e190-3bb3-bf28-d0c757d9a7f2 | -9.36685 | -47.63024 | 2025-06-27 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b28b72-b76a-3dab-ac83-2ecdd5bb8b9f | -10.70646 | -59.13025 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df5553cd-b0bb-3a4e-87d7-007f95ebbe83 | -11.82393 | -57.76717 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7f1d29b-20a5-32ea-8225-4043bd010954 | -9.11647 | -49.44122 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 838e1b21-2f73-37a7-a629-416f43c5616c | -11.17186 | -55.91832 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a8b94e7-890e-33c7-877e-c2d500880b11 | -11.18589 | -55.92052 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79bea7fe-6042-32c7-ba0b-b2bce29237b3 | -12.05125 | -48.07566 | 2025-06-27 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c70ecf9-648b-3a05-aad6-33329b94bedb | -8.62417 | -51.56886 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5cc0acf-562f-3d18-9812-df2cde89c02f | -12.02694 | -47.7788 | 2025-06-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 277d4f1a-cb92-3dd0-b27b-925b04b3bdba | -10.83339 | -53.75174 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 715197e8-9e5e-3f7d-9fa7-0d280b4ac0ea | -12.04485 | -48.07944 | 2025-06-27 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d221f7-0d6c-33ef-b587-1723ad1b5745 | -13.04593 | -48.82301 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cfb535d-7acf-3357-97d1-23b27dc4df80 | -8.48463 | -48.26102 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe4ea7cd-8776-344c-9876-6eae07b0e7b0 | -11.36052 | -48.71404 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd4bb0fa-cd1a-35c3-9eb4-f08b2fc7525b | -10.88234 | -53.77407 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4bb01d4-850f-3ba3-80de-fce2622b9867 | -11.82274 | -47.53911 | 2025-06-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dfcff07-c770-3985-837e-7a50c9510da5 | -10.85678 | -54.04115 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df7d56b4-3f75-370b-a4bf-ee3305d49297 | -8.84439 | -49.85759 | 2025-06-27 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d9b553e-4a42-3f3f-8181-e00b5ced4ad8 | -11.43164 | -54.48124 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efe2ad25-9c9f-3b8c-9f37-46fc945d2adf | -11.57229 | -52.10553 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c464d57f-dc4d-3a05-a913-a477b8de693b | -12.05005 | -48.07816 | 2025-06-27 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f00d431-4fe5-35d6-9871-d172336db6c3 | -6.17896 | -48.0891 | 2025-06-27 05:10:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8f038fa8-863a-3e6b-9595-885ffe500fb1 | -8.48416 | -48.26455 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3913a1aa-1b0d-3c40-ab3e-2f643b2043f8 | -10.85879 | -54.04427 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 011b28b0-558e-318b-ad08-1acc6eff2b40 | -9.50416 | -56.09724 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4487ea2-49f2-3d5c-95d9-7df944bad280 | -11.81792 | -47.54544 | 2025-06-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a32ca6e0-2682-394c-9f38-e5503440a5c5 | -11.36141 | -48.70671 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eaf36c3-dfbe-3232-a8f5-6733f19f5729 | -9.82144 | -48.38326 | 2025-06-27 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54bc372a-cc8d-3178-b064-9ce77749a3d1 | -11.18529 | -55.92451 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18559703-95d4-36c7-a44e-8e57fb1d5458 | -11.44121 | -54.46822 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 027904c5-cd6c-32d9-abb0-40b99a88f439 | -11.445 | -54.46878 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a301d79-4d57-3272-9aa8-a7c146a77415 | -10.70703 | -59.12672 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12b90e87-152e-3cd5-8da3-e9c94f85de85 | -9.32754 | -57.84008 | 2025-06-27 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb59bc17-c8ea-3183-b4df-6d64182d5b3b | -11.36239 | -48.70761 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a91a9f00-3290-3088-9594-75dfcb70b5da | -11.06841 | -55.3761 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4efccd1d-f7b1-31ca-9756-25e69cb8824a | -12.10878 | -54.66117 | 2025-06-27 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96378dd5-41ff-3841-9a02-abc1ba10b814 | -11.80631 | -57.35243 | 2025-06-27 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ebf4382-29d7-352c-b21d-fcf4b3201c1d | -10.82946 | -53.75118 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99002918-014d-3ef1-9a1c-aa73219684fe | -8.67766 | -49.95868 | 2025-06-27 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5049680a-e79a-36a9-a466-c90b57642625 | -12.65525 | -54.10514 | 2025-06-27 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c770e9d5-8e80-3f56-816e-fc8bdd7335bb | -6.17452 | -48.08159 | 2025-06-27 05:10:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README28.md)
