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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6197040a-d3be-3515-8b1a-7e0d9f5e148d | -3.30659 | -42.53381 | 2025-12-14 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3c42796-250e-312d-93f7-fb617669d9b8 | -1.1459 | -46.75642 | 2025-12-14 04:31:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78d31e05-8015-3e60-b42d-ee9767c3833d | -2.18509 | -53.67007 | 2025-12-14 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 948ea81d-8016-34ed-8ec6-a1428cc4b590 | -3.21116 | -41.8536 | 2025-12-14 04:31:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b3062c-4acb-3e9b-8405-20d2ceca862d | -1.59373 | -45.41276 | 2025-12-14 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 259e8e38-3ce1-3c5d-97ef-e58be2809167 | -3.5241 | -47.20768 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2cfb3bc-1cea-3fa8-b942-21f54177ade1 | -2.48094 | -45.43777 | 2025-12-14 04:31:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25394c8b-1c3d-3bc2-b633-a106c73aba31 | -4.4368 | -45.83942 | 2025-12-14 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 291560bd-8e9c-36c8-8210-b3bbf8e0e6e7 | -3.14459 | -45.3671 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa10eda0-ac6d-3af5-bc42-934a6931a3dd | -3.77447 | -42.09812 | 2025-12-14 04:31:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7083616e-8c1d-3dc2-95f2-f2304abef74d | -5.9407 | -44.45628 | 2025-12-14 04:31:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ea63a141-460e-3d9e-8229-f01024578a04 | -4.69443 | -43.25352 | 2025-12-14 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27e6a566-bc0c-3ca7-b806-dc5d361d9b33 | -6.1673 | -46.1013 | 2025-12-14 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a816a690-a6c0-3e76-bdf0-a262a16a0988 | -1.53644 | -45.58237 | 2025-12-14 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 69689e96-c516-354c-9ec6-bd3a16030f21 | -3.43599 | -41.64533 | 2025-12-14 04:31:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4acc032c-06fe-3ab2-b9ff-3abf3a41ab96 | -2.21363 | -45.69049 | 2025-12-14 04:31:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ad3c2a4-ad82-33a5-b19a-fbe2674bd416 | -2.04192 | -45.59473 | 2025-12-14 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5bbb01c-405f-37dd-9fc5-a1c1770752e3 | -1.62572 | -45.4287 | 2025-12-14 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9008a7c-351c-35e7-8173-cba28f343e21 | -5.81946 | -43.00962 | 2025-12-14 04:31:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8bf7a05a-ce6d-3e82-b00e-dd0e725706ab | -2.85125 | -45.40133 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 820c33c2-b997-3268-9fcd-5b8425564595 | -6.33268 | -46.32814 | 2025-12-14 04:31:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49a2be1b-1806-3498-ad33-9e98d74f3cff | -3.30962 | -42.53669 | 2025-12-14 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87d0af91-87b0-32c9-a73b-082670aaf381 | -3.63976 | -42.21649 | 2025-12-14 04:31:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fdc7b9d4-8168-3885-8009-c0de87b15c7f | -3.49948 | -41.98592 | 2025-12-14 04:31:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f5e084b3-743a-30e0-a6f7-38cc1fa6bc34 | -2.78874 | -45.06042 | 2025-12-14 04:31:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db5bc0ce-a0de-3701-b6a1-3956f94e0bf9 | -3.44071 | -41.64968 | 2025-12-14 04:31:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 77dac9e9-af2b-3200-af06-15e3fb473247 | -2.11487 | -54.21681 | 2025-12-14 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2993b3e7-603d-3827-bd02-853dcf1cb8a2 | -3.40666 | -52.20005 | 2025-12-14 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6821d5a3-9e8e-3b8e-aae5-eb4169469160 | -3.42669 | -52.92263 | 2025-12-14 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 748ad861-2b16-3973-bf5a-85a2936f7d4c | -5.3494 | -40.68299 | 2025-12-14 04:31:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d4534091-3dde-379e-bad3-49d4c93a3a4e | -1.78676 | -54.15085 | 2025-12-14 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1b7f499-4dbf-3fda-a3b3-97203f373c03 | -4.35692 | -46.14359 | 2025-12-14 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3ca754b-8fcb-30b0-bbe1-7c92238dd4a6 | -2.88739 | -44.96744 | 2025-12-14 04:31:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d46fa8bf-e279-3027-9460-6b43b18170a1 | -4.45618 | -43.65037 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbaf93d2-3076-3812-b65d-a83031ccc8dd | -1.93049 | -46.43603 | 2025-12-14 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49d8fb6f-0fa4-3537-9676-90535ebc90cf | -1.97453 | -46.48227 | 2025-12-14 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3fbfe54-c372-34a3-afa0-56a1c2110599 | -3.14516 | -45.36343 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 182c2401-46e2-3d11-8ea7-a7d8aac3001c | -2.83324 | -46.73278 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c30bf902-08c2-3905-89fc-99632d2a0616 | -5.94004 | -44.45747 | 2025-12-14 04:31:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 53345356-46be-37e0-b721-54d516f0e5d1 | -4.3418 | -43.6392 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8eab3825-45f9-31bb-8db7-49ae22e56bf5 | -3.88208 | -42.52039 | 2025-12-14 04:31:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 691e50e8-5704-391b-86bf-6a9d5c8691e7 | -1.87108 | -47.98693 | 2025-12-14 04:31:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7278b94f-8100-3964-8692-478fa61ccd68 | -2.44148 | -46.91092 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed27ddc3-2817-32a4-8613-8112fcf6b312 | -1.92772 | -46.43208 | 2025-12-14 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa806abf-7f36-39e2-b3b7-40cb8e93a3ac | -1.52889 | -45.67523 | 2025-12-14 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c03e6b7-9ec4-3270-8124-851a8afdd4be | -4.93304 | -43.9622 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0a40bd6-8439-3f14-9151-9633a4d1252c | -5.67485 | -39.26489 | 2025-12-14 04:31:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90af8ad9-67af-3ea4-8dc5-bfef8ffb116f | -2.66807 | -46.89746 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3187605-e81d-3c62-a9cf-5a2061fac35d | -1.92718 | -46.43552 | 2025-12-14 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51b1d28d-6b85-3ba9-95f7-7e9a529f2cfc | -4.86627 | -50.82232 | 2025-12-14 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2796a58-377f-3ee8-ba6c-58eb0ea3fade | -3.46153 | -52.59073 | 2025-12-14 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 011a38d4-124c-3e72-9f3c-48113345f5eb | -3.15251 | -54.6018 | 2025-12-14 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f17cf77a-ecdd-3bc1-9c73-70fee2a96913 | -6.40651 | -41.08727 | 2025-12-14 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74d36edc-55e6-3a0b-8c8c-0068534e0458 | -5.13338 | -37.91133 | 2025-12-14 04:31:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 995be2bc-c58a-30d7-932c-a384b7645cf9 | -2.34839 | -53.9151 | 2025-12-14 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3afacc09-99bb-3881-87b6-2b3720751dc5 | -3.14743 | -45.37129 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cea7ce2-3a21-326e-8853-058038ad5789 | -1.14206 | -46.75934 | 2025-12-14 04:31:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8534d2e4-c12c-3c4a-affd-a7290b546baa | -5.39875 | -44.6752 | 2025-12-14 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 398383a0-679c-34fb-ae9f-14ecebc0625e | -2.83655 | -46.73329 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d2ffe25-8e2b-31fa-8c32-396f9cd46e3e | -3.15758 | -44.36878 | 2025-12-14 04:31:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3275bd2-bdbc-3364-9027-b92038fcc30d | -2.78531 | -45.05989 | 2025-12-14 04:31:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d54fcaab-adea-32b4-a721-1261e01be561 | -3.51741 | -52.18633 | 2025-12-14 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ee3a959-69d7-3e14-bf23-041578c49b48 | -1.52445 | -45.68176 | 2025-12-14 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 882fa051-ac12-3c7d-8a3d-dec0b502bb4a | -2.6686 | -46.89402 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b53f2f2-4f5a-31c4-8f71-02b11b015bf7 | -2.2852 | -45.58488 | 2025-12-14 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bd22455-4ad9-318c-945e-2a421c5868d2 | -3.36412 | -39.81444 | 2025-12-14 04:31:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd60cb64-6a4f-3033-8ee0-31279d435398 | -2.09025 | -45.28588 | 2025-12-14 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 296ecf55-1113-3b1b-a9a2-c2e212f6f52c | -3.43708 | -41.64522 | 2025-12-14 04:31:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d61f609f-5cbc-3a61-9b06-caff1967e8a8 | -2.9721 | -60.06981 | 2025-12-14 04:31:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 00206f3c-2420-365e-bc19-2242a9d8e96b | -2.62931 | -47.29593 | 2025-12-14 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13780b8a-57f4-3b76-bcf7-2eadd2a007b8 | -5.48337 | -46.44079 | 2025-12-14 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae2361cb-05a1-3800-9453-dfce55e58a74 | -2.63261 | -47.29644 | 2025-12-14 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92fb3bd-949a-3a98-8aeb-034a35a350dd | -3.52026 | -47.21061 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e785bbdc-3b87-31d8-8517-5ee83ea34d33 | -3.16199 | -53.03052 | 2025-12-14 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef92ddb6-e04b-3e68-818c-860f90f0a2b3 | -5.67314 | -39.27696 | 2025-12-14 04:31:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f432c27-448c-30e4-be68-603b374a5217 | -4.03808 | -48.8946 | 2025-12-14 04:31:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75ba40f4-348f-3dd3-8cce-815b8096ae75 | -2.48433 | -45.43829 | 2025-12-14 04:31:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bca8685d-471d-31fc-b3b9-92ad34c2cf8c | -3.40723 | -52.19651 | 2025-12-14 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f227fe8-2381-399c-9e66-83e89f17c58a | -2.37981 | -45.52206 | 2025-12-14 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e3faf02-8147-32d4-b949-285a73dc680f | -3.88657 | -42.51758 | 2025-12-14 04:31:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2eafb7cf-e1a6-3887-95a8-a92cf8712b75 | -3.95506 | -42.70239 | 2025-12-14 04:31:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e9f43294-a244-3ed0-9f74-ccf599648178 | -1.52725 | -45.6858 | 2025-12-14 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f88a843e-00bf-306e-b915-737100d6b87f | -5.0038 | -42.77897 | 2025-12-14 04:31:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8fbb07b-b379-3b8e-a57f-3f51febb12cb | -1.50739 | -53.99198 | 2025-12-14 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f02cd5e-2881-368e-bb48-b7b3f1a13ef4 | -2.77603 | -54.52666 | 2025-12-14 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b05e2be-20e5-3b41-a3f3-ea8df12e4dd8 | -2.04247 | -45.59117 | 2025-12-14 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6b7d73d-ebbc-30a1-9957-8e516cd220e3 | -6.58807 | -39.56794 | 2025-12-14 04:31:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d2d560f-571d-3827-9d3f-25f55c5230d2 | -3.17437 | -52.87151 | 2025-12-14 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b62c91-ca7d-3bee-8a8e-3e8c0e6c9f75 | -2.28464 | -45.58845 | 2025-12-14 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b07b7c2-e52f-3f6a-87a5-2d1356fbb1e1 | -2.37644 | -45.52153 | 2025-12-14 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb063c80-f047-350c-b082-80c28df784ed | -2.88453 | -44.96315 | 2025-12-14 04:31:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1e0e632-8e91-32d3-ad69-a8cb1f664e05 | -6.29418 | -47.00036 | 2025-12-14 04:31:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6094a53e-9fc0-342c-b292-ef777d271dcf | -3.70264 | -50.94675 | 2025-12-14 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 006e1ab0-5249-3d68-939f-5ba5175f24c9 | -1.1426 | -46.75591 | 2025-12-14 04:31:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd67e51d-6945-309c-a657-a12f3fefb976 | -5.84268 | -44.92501 | 2025-12-14 04:31:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc45cd17-ffd3-315c-b362-c5e32c9d7b6e | -3.49734 | -46.96756 | 2025-12-14 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec9eb662-7b36-3b6c-99df-27195a5c779f | -2.8404 | -46.73036 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da3f2eb7-28ad-3d6b-8499-005ec7c755b9 | -2.5879 | -44.95364 | 2025-12-14 04:31:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 147a2583-dd06-3119-ae46-be4812d4f6a7 | -4.43341 | -45.83889 | 2025-12-14 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72cfacd0-af09-3074-a247-ea7279385a89 | -2.1896 | -53.67079 | 2025-12-14 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
