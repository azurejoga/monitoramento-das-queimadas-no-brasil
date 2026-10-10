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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74aab83b-c98a-3bab-aace-5bb3ed3918b4 | -8.77056 | -49.61007 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00a53301-d92b-3ef4-8b6b-3405a60e5afb | -3.58395 | -54.70956 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7135584-2791-3f36-b5fd-d049773c9847 | -5.53663 | -43.84734 | 2026-10-10 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8326c733-87d1-3687-a25f-f3ed42d354be | -2.205 | -50.82451 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7655c71f-b484-34a7-aa21-266a7290e7dd | -7.00783 | -47.71507 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc6aa914-f8e6-3f8d-9f91-9479bed4f603 | -6.42486 | -51.9558 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d7c0159-7644-3ff5-a702-1fc67c6cd3f3 | -7.0865 | -43.47734 | 2026-10-10 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fbbe1cd-7a31-37fe-8ebc-0cbc9a83bc43 | -2.57387 | -48.24938 | 2026-10-10 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82d00250-c309-3705-b50c-abb8f2f58f69 | -5.59298 | -47.28814 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0988535f-9a62-3315-8543-66feee056d56 | -5.6931 | -53.46658 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0bae3012-3a1e-37fd-9bb5-1fc74c295fa5 | -2.38015 | -47.6092 | 2026-10-10 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 789223b7-2c59-3d5d-91ba-5fd2c8eb88d1 | -10.05532 | -44.35178 | 2026-10-10 04:08:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9cf4ac6d-e1c0-36ec-9c63-7f27b95687b5 | -6.65031 | -55.33029 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fc94b32-f13d-3ce9-8d08-6766fb46c940 | -7.39628 | -44.7611 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7849abbd-62fa-3287-9785-d1252d8b4acb | -7.24 | -44.17977 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa84754e-0229-3a32-87e5-91a4921f9454 | -7.24062 | -44.17591 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b47116db-700d-3a7e-955b-562f8a99aea6 | -3.23204 | -49.45297 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ced82599-dcf7-3e15-a8d3-437b71e7622b | -4.63805 | -50.95615 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b442bef-305e-30fb-8233-64fb37d204bb | -7.10045 | -41.75502 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8abe4132-ec96-3453-800e-21657b92d5e4 | -3.59741 | -54.60009 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 208a294a-ebc7-3204-89bd-ae64790cb1b4 | -9.3064 | -47.37988 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d173aa5c-8bed-3915-8546-f920fa294025 | -8.93062 | -45.41737 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eaebbe2f-e1d2-3fa7-b95e-425d1497c484 | -8.9244 | -45.14273 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c908da87-c250-3e92-b6d2-a8f1b7fd8c20 | -4.12468 | -46.8662 | 2026-10-10 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b4a62b6b-e320-3ff7-83b6-dbd6ba8d7bb6 | -7.59351 | -43.07698 | 2026-10-10 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 13517025-ad91-3873-8ebf-0ca134dd596f | -3.19742 | -53.85852 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 081e0783-95f1-39d6-865e-2b0ed4c5d914 | -3.03882 | -50.33767 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eafea221-5c3b-3822-8257-7ae51b90e249 | -3.18512 | -50.58924 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a39ae0a-a593-3f00-82b1-db8d78b972d6 | -4.40148 | -43.12217 | 2026-10-10 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69f15588-f2d2-32d7-95bf-726ab212988a | -3.99177 | -54.4528 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95840d9a-cbb0-3231-b38b-1099626f3eba | -5.59554 | -47.27235 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74d6b45b-e1d1-30e3-bd23-51cdd19f391e | -8.76887 | -49.60685 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d50fd86b-e4b8-38e4-8909-95fdfbab2fda | -7.51813 | -45.30788 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0a2b3015-0ff2-33b3-92ab-9c96f5e06aa9 | -4.12233 | -54.04211 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2ffe440-a331-35e1-adeb-5e7a496c7ce4 | -3.74455 | -50.00765 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd9ad417-a2df-3998-a166-2a42d713c891 | -7.56416 | -45.6469 | 2026-10-10 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef39584e-95de-3298-ab00-15aaa21dcd8e | -3.76228 | -45.96064 | 2026-10-10 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d83e6f0d-df0c-3405-a392-a36850740f3e | -9.93498 | -44.78798 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e840f9e-a097-334f-a8ff-594da81a1869 | -7.07355 | -41.60246 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec5052b6-9169-3c4c-8ce5-a15a82ed51f8 | -7.00163 | -47.72607 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b40dfc87-b0c4-396a-9c32-2b924c75635f | -2.3994 | -45.57707 | 2026-10-10 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28e108df-c49a-3d4d-87db-be53ab6c6184 | -8.2464 | -46.43235 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be103506-f111-3b66-9fd3-27612c2302b2 | -3.50158 | -49.94167 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7afc4d46-cfa1-328b-923d-998548c248d4 | -7.91204 | -54.72733 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6227ceed-e41e-3fad-a31f-7598b42bb29e | -7.03264 | -47.67067 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53925758-2e7f-35cd-8480-2190b598546b | -3.45603 | -39.14763 | 2026-10-10 04:08:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0f6a9d25-91f9-3f87-b4a4-51ee477ad790 | -7.2186 | -55.15244 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12ca182b-11ac-39e5-b9a2-c71ccf0a1019 | -4.31614 | -44.99062 | 2026-10-10 04:08:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ed58f1c-979a-30d4-8620-e2adcdef62af | -4.13265 | -50.82248 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 300fe529-ddb3-3591-99b1-f328c5260b5d | -7.08898 | -52.68485 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cf28a7e-9f30-379b-9a51-f47aac3bd261 | -3.22339 | -49.44224 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5a1d7e6-291b-31c5-b68e-111c7f111b4f | -7.52245 | -45.3042 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a129503-871e-359b-9f76-01428f06f3b5 | -8.18187 | -54.71498 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 68306d46-9b63-3a8e-8398-ac9eecaebd21 | -3.89367 | -52.19489 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86775a20-d26b-39cf-95fd-f6531fc0468a | -9.76089 | -44.7799 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d31b28ce-a564-30f0-be1f-811d46b8f216 | -5.10075 | -46.22561 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6808606e-34f2-321e-94cc-3c0785ed5ab6 | -6.06738 | -44.67317 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 022df6d5-a115-3bed-a710-244c1a7460a4 | -3.34443 | -50.41071 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fe1dfa3-996e-3270-9a95-30c6fdfaec2e | -9.94464 | -44.88036 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5013ae7f-0c3b-3b15-8b43-ad89380384a8 | -9.94054 | -44.88366 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b7dab8ee-b26c-32e2-b6f4-971177f044de | -6.45042 | -55.28961 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f0ca58a-984c-3f73-b182-5213fcace1a3 | -5.9582 | -40.91702 | 2026-10-10 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70dbaf3e-910a-303f-bf18-bfb2f5350ff9 | -6.36689 | -55.16567 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44f22316-1d50-39cd-ae11-e0aff0def644 | -9.12091 | -45.81527 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e1f0569d-d3cc-3533-9e8f-7722eb98f6ea | -6.93414 | -45.59903 | 2026-10-10 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fac50498-a839-31ed-a3bf-acd16dcf1907 | -7.12113 | -42.53412 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3b85ab96-a18c-3bb7-bc7a-b732e4e9f326 | -9.01186 | -44.37158 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3fc6e32-06f6-359c-b58b-de87ac487fb7 | -7.91424 | -54.71568 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8039484e-edad-3e28-8b55-31e45a6f07bf | -9.93217 | -44.78353 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 76b9b0ea-5927-39be-86a7-9acc3708c11f | -6.18416 | -44.85223 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7748c3d-a776-37ed-9c12-88611df3aade | -5.13062 | -45.79448 | 2026-10-10 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d658f57-0a71-351b-8009-499df1bfab10 | -6.9479 | -46.13334 | 2026-10-10 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 291aeff7-ae28-37a6-bf71-b15058de44ea | -8.94605 | -45.12153 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49c7a7c1-712e-335b-9a6f-b77be63c52c8 | -6.70078 | -40.4664 | 2026-10-10 04:08:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 810dda71-dfa6-3d77-bdef-45109d803145 | -9.27295 | -47.40667 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d85136c-ec6c-3dde-be85-a8ebec3e38a9 | -5.08491 | -46.2231 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7a978d6-d61d-3173-b534-8b131fab1b44 | -3.17963 | -50.58836 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e43d5554-8ba6-37ba-8a6d-fe1687f9ff34 | -5.73069 | -44.03897 | 2026-10-10 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c650f49f-e5e4-3dc1-a21c-a5abb7377834 | -5.87726 | -50.09739 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7a37d1b7-8b1d-3111-8a47-3c71578899d0 | -3.20927 | -50.55108 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d8c0524-f872-3217-88bb-89e3e070fb24 | -3.88769 | -52.19364 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8d9ee3bd-a539-3696-94f6-bc41c141190a | -7.18801 | -55.15956 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb5041c4-0ada-3705-8147-891f23e3bf77 | -7.19357 | -52.63574 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 828570c3-3fac-3b39-b633-8ee9a1e5e061 | -7.18847 | -52.63049 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 24fd8f62-5c87-3062-bfc9-a19c7d7930a0 | -6.58684 | -41.5572 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae1e8b65-101c-3db8-9fc6-f203a56ab450 | -8.404 | -46.90361 | 2026-10-10 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0423ad94-c109-3eaa-ba40-b92f32bb5aa8 | -5.98339 | -43.93265 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69fd3acd-5148-3d11-bbff-40a91e8fa68e | -9.60452 | -45.97941 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5d044c3-75e4-37e1-a0c6-3334bae79bcc | -5.51934 | -43.04776 | 2026-10-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7fa277b-a704-3b0d-bd00-6816cb88e677 | -4.23146 | -40.77484 | 2026-10-10 04:08:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| beb07f14-3143-3c0d-bddd-13bb971f1953 | -3.25988 | -54.69308 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6067b23-2b53-3a1a-8677-e63871035254 | -6.43302 | -55.27214 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fa62463-68d0-3f16-91cb-13950fa05616 | -6.47617 | -42.6969 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 72003ade-cf64-31ad-bcd4-539b098c0414 | -8.25487 | -46.42881 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e11d7b6a-9bf6-3d56-ab07-1b2b31c274eb | -7.03036 | -47.65826 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 861e5a58-87b5-3907-b362-e6115f0a64ed | -7.18538 | -41.99457 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65082229-5989-3395-9a92-0f4d87f27b1b | -5.74282 | -45.07698 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98732115-854c-357b-980b-716168f6a7e9 | -5.87857 | -43.55706 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b61ea23-9052-3564-9857-d7898120b176 | -9.46294 | -44.60264 | 2026-10-10 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df7db5d6-56f3-384a-b9bf-0cfd2307cec7 | -9.7411 | -44.79242 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README40.md)
