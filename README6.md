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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06804de7-d482-3fb0-ab04-02c74ff17776 | -18.83076 | -41.98198 | 2025-07-24 03:25:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b13529d-4761-3e8d-abbf-1a1a475db63e | -18.85016 | -47.95984 | 2025-07-24 03:25:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d7af0320-bb59-3ab7-b018-9fd27fc42503 | -19.67125 | -43.23256 | 2025-07-24 03:25:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb834050-c4c6-3177-9eab-f3f670571bb7 | -20.03936 | -45.6504 | 2025-07-24 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84f34426-fdb9-3e86-b1d6-a71e4558e473 | -15.27971 | -47.13587 | 2025-07-24 03:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dc299ce-50fb-394d-a200-881ebc403335 | -20.0383 | -45.64926 | 2025-07-24 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deb0b575-cd6d-3645-8849-bfdab90b6e41 | -20.04309 | -45.65609 | 2025-07-24 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 811ee163-f34b-3082-9738-b7f0f25606ab | -15.26744 | -42.25595 | 2025-07-24 03:25:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5e3d1d7-22fb-389c-b1f7-317ea19bebff | -15.28084 | -47.13098 | 2025-07-24 03:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff95d098-cbb4-3a51-b8d7-34143029be8a | -15.27227 | -47.13567 | 2025-07-24 03:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71872cbb-9bde-3b96-943f-445ec40992f2 | -14.78993 | -42.44134 | 2025-07-24 03:25:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe27cba3-631d-3861-a44f-6e703a44ceb8 | -13.70669 | -45.69489 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9822541d-7a83-3939-a2fa-f17edc0c3e7d | -15.27274 | -42.25737 | 2025-07-24 03:25:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 214ab234-c014-385b-9a5a-e7092ae7ed9a | -18.11188 | -44.63613 | 2025-07-24 03:25:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4f50ce0-8a89-3442-a2f8-cfab4e2eb02a | -19.67055 | -43.23586 | 2025-07-24 03:25:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ec7eea7-a9de-38c5-9b75-30ee87e5675d | -13.70267 | -45.68074 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0cf5c4b6-5e12-3521-865e-22781d6ca1f6 | -13.70538 | -45.66819 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d099e49e-0fe4-3e33-a6dd-6adbac2be8aa | -14.78916 | -42.44515 | 2025-07-24 03:25:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 033a5eb2-9f3d-317a-9fb3-c7edd5e2237a | -18.84837 | -47.96717 | 2025-07-24 03:25:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bb165df4-3833-3738-b6b9-fe1d19ea1d11 | -13.69995 | -45.69333 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f5b8f9d8-9037-3dc1-8a15-8f137adac2cd | -13.70131 | -45.68703 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 70284cee-891b-3c9c-938d-a33d35c033cb | -20.03717 | -45.65429 | 2025-07-24 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e24dc036-c00b-3fca-a177-3a4bbdcd3a97 | -20.03821 | -45.65539 | 2025-07-24 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41f609f7-8c56-355e-985a-8883a7419e04 | -18.85093 | -47.96607 | 2025-07-24 03:25:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e30a0528-af14-3fe7-8786-33949e97d5de | -13.70402 | -45.67446 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6861e004-fe9d-33bf-a45e-5b0ed142751a | -13.70805 | -45.68857 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12220bc4-d554-38fc-8ca9-234588565088 | -20.0442 | -45.65117 | 2025-07-24 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42ba0eb4-f3cd-37f1-a9d8-a75b2db7cb04 | -13.69728 | -45.67294 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb05b017-71fd-3da2-b9fb-068d83e3633d | -15.27682 | -47.13661 | 2025-07-24 03:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 035caab0-5f72-3d7d-8f49-09dedfd328c8 | -15.42471 | -39.80675 | 2025-07-24 03:25:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0635d6dc-40a2-38d2-811f-fed877cb59aa | -13.64268 | -45.72374 | 2025-07-24 03:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56503b6c-138e-3be2-bffd-339aa7b53d70 | -23.29539 | -46.12562 | 2025-07-24 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 44615bb2-9181-3d6b-8774-73a47585de31 | -23.29396 | -46.12737 | 2025-07-24 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d424c9a1-5e60-3b38-ad9b-bbe4c5e2340f | -21.79083 | -44.70348 | 2025-07-24 03:28:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d47017a-69e1-3637-bea7-c5ee0fc6fac9 | -22.86649 | -47.10038 | 2025-07-24 03:28:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5fc212fe-3606-337d-bc30-8d26bfbcda4c | -22.8146 | -47.15293 | 2025-07-24 03:28:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 996d9fcc-d902-3e74-9635-089e483e07cb | -23.0561 | -45.53588 | 2025-07-24 03:28:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ced1de1a-4e9f-3b00-869d-c5c3563037dc | -21.78591 | -44.70221 | 2025-07-24 03:28:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d50b5a7-e9ae-3014-8e7e-3f274979d723 | -23.29436 | -46.13004 | 2025-07-24 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e0c45fb4-598f-3aaf-b655-399da84cc537 | -23.36073 | -47.1786 | 2025-07-24 03:28:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5cf45580-cfcf-3e93-b644-6ae96a50207c | -23.35943 | -47.18399 | 2025-07-24 03:28:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2ac09e4a-d74f-3202-8665-f2c6a1efe717 | -23.30111 | -46.12735 | 2025-07-24 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4d18ca3f-1f0a-3205-8676-fde98f651193 | -23.91631 | -49.10472 | 2025-07-24 03:28:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 403b7e92-dba4-399a-b304-4f6ae7dce62e | -23.05513 | -45.54004 | 2025-07-24 03:28:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 14d944cf-4c75-3929-912f-c2e6dda34c68 | -21.31189 | -48.57073 | 2025-07-24 03:28:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 502e4d40-4e1a-364b-bec9-36a917612fe3 | -23.29968 | -46.12909 | 2025-07-24 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bc8799cf-87d0-36ac-8d8b-d1ecd2e5d097 | -23.30009 | -46.13174 | 2025-07-24 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 102e750e-44a7-35fb-a905-156d83ff7e5b | -3.1648 | -49.4648 | 2025-07-24 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 9f54ef83-ade9-3daa-a5de-fd4922d46ad8 | -7.2597 | -43.0645 | 2025-07-24 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 170.7 |
| 26b3b6c4-a14c-322f-8077-7cf5ba38b448 | -4.0569 | -42.5118 | 2025-07-24 03:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| b1013c34-eced-37da-abab-da38566d768b | -7.2408 | -43.0664 | 2025-07-24 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 2ace63d4-ace7-3e43-b752-d9a3c0874bdd | -3.1649 | -49.4435 | 2025-07-24 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c510d6e7-26f3-3637-8acd-d5400cab7b3a | -3.1833 | -49.4429 | 2025-07-24 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 66fb2377-feff-36f6-b432-01fb09ddcd17 | -3.1832 | -49.4642 | 2025-07-24 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 04ab3e48-11d5-32d2-9da1-59bad411870a | -7.2594 | -43.0881 | 2025-07-24 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| d03148aa-2c9f-3cad-9048-3b34b367a474 | -7.2408 | -43.0664 | 2025-07-24 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 57df7641-f1fe-36df-af6b-3b302fcb2e20 | -3.1832 | -49.4642 | 2025-07-24 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 0449af70-cea3-3703-8cb9-9a2376b79171 | -7.2594 | -43.0881 | 2025-07-24 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 359e0ccf-8dcb-3f86-946a-2e4bbc1ed9c7 | -3.1648 | -49.4648 | 2025-07-24 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| b4d33b3b-d5fc-3bdc-b5de-6d3b64486b37 | -3.1649 | -49.4435 | 2025-07-24 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0a50ba09-1668-3857-ba84-7c20acb32b3b | -7.2597 | -43.0645 | 2025-07-24 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.3 |
| 27dfdf04-e286-307d-b221-d09f8257b3a6 | -3.1833 | -49.4429 | 2025-07-24 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 6615ec58-81bb-38fa-9b71-badde8983eac | -3.1833 | -49.4429 | 2025-07-24 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 38e23e57-0655-321f-937c-effeca994e7a | -7.2597 | -43.0645 | 2025-07-24 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| 09b95df5-bd60-37ea-9aec-fade631646c4 | -3.1649 | -49.4435 | 2025-07-24 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| f8ac112c-2011-30f5-ad63-36cb6143eb75 | -7.2594 | -43.0881 | 2025-07-24 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 99fa326a-2ecb-3453-b29f-d93d6bced5e3 | -7.2408 | -43.0664 | 2025-07-24 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 47442be1-3e4f-3234-b0ad-a83236fbd554 | -4.0569 | -42.5118 | 2025-07-24 03:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 02af8c1e-0f86-3a1f-821f-d2135f062652 | -7.5444 | -44.4777 | 2025-07-24 03:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 07ccbca8-c676-36a9-8763-8297bc4ffb25 | -3.1832 | -49.4642 | 2025-07-24 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 096aff2a-ee30-38e2-9918-8d9b4959ea46 | -3.1648 | -49.4648 | 2025-07-24 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| adddc75e-96f7-3cba-ad6d-08b4011a6a1c | -7.2594 | -43.0881 | 2025-07-24 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 85393e62-59fc-37a8-b36a-43735ce2f993 | -4.0569 | -42.5118 | 2025-07-24 04:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| f17caa65-aeb3-3ddb-96bd-a1cfa3d2f833 | -3.1649 | -49.4435 | 2025-07-24 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8bc407df-1436-3b24-9b50-e56a5328070d | -3.1832 | -49.4642 | 2025-07-24 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 368a5a15-dd29-3026-bf28-ca408b98dbf7 | -7.2408 | -43.0664 | 2025-07-24 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 0193f8e4-50ca-33c6-91dd-df13f3b74e82 | -3.1833 | -49.4429 | 2025-07-24 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 11a73244-48df-3b3f-83fc-2f7996d1122a | -7.2597 | -43.0645 | 2025-07-24 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 8ea605a0-5b73-319e-a66d-413bb84f1a20 | -3.1648 | -49.4648 | 2025-07-24 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d54882f0-0b99-39bc-bf9e-af051884e702 | -7.2597 | -43.0645 | 2025-07-24 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 848f20e8-ba81-3005-89d5-251a193cae0f | -3.1649 | -49.4435 | 2025-07-24 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 43113258-07a3-35b9-8083-73148513f611 | -3.1832 | -49.4642 | 2025-07-24 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| ee63ba8d-6251-38f5-b569-5164b33e8709 | -3.1648 | -49.4648 | 2025-07-24 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 84c43df0-a93e-3ab4-a6d2-bac5241f1b78 | -7.2594 | -43.0881 | 2025-07-24 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 003dc1a1-94ad-38e9-9a72-a02a59969043 | -3.1833 | -49.4429 | 2025-07-24 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| e7fd71aa-b349-3eb0-9e99-bf5ca77f3e07 | -7.2408 | -43.0664 | 2025-07-24 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| af9d166a-2534-32a9-a864-c4dd96756158 | -4.0569 | -42.5118 | 2025-07-24 04:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 105aec83-517a-3c0b-8ceb-10d4c384a91b | -0.74839 | -47.75473 | 2025-07-24 04:12:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a68981-9eef-3c2d-9041-f1ca8ac4a214 | -4.17521 | -42.02758 | 2025-07-24 04:14:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 44179b02-c70c-3c11-a20b-4c22118b8bee | -7.25181 | -43.08175 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59b89d58-72d6-3e40-8919-82aa174c3ba1 | -9.58656 | -46.32175 | 2025-07-24 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3dc6a1e-bef6-309e-88ed-92d103450ddd | -4.30089 | -48.04654 | 2025-07-24 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf2f9923-3170-3067-a464-04a4e406e041 | -7.35678 | -43.43501 | 2025-07-24 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eb0c44e-0e35-39ae-afe3-f23765e2d0c6 | -4.30043 | -48.04736 | 2025-07-24 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a109966-f0cd-3f15-a4cf-48367d9afe5f | -4.82134 | -45.09423 | 2025-07-24 04:14:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 488ef1e1-e4d5-39ce-a40e-5939a96dc421 | -7.2485 | -43.08123 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fad57675-09d8-346d-abda-9525a2bb83c8 | -5.65332 | -42.58196 | 2025-07-24 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 93eb91ec-bc63-31b9-8190-c2821bdcd25a | -4.05991 | -42.52635 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6dca0b9d-30cd-399f-89bb-a449480e9458 | -4.05053 | -42.52138 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e06454d4-cdf6-3b40-b643-b7cd367ec6b5 | -6.96974 | -44.37916 | 2025-07-24 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
