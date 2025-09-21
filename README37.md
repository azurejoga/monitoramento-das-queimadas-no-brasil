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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccf0b9b0-31ed-35d5-ae70-86d31580698c | -12.42125 | -45.12905 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e13929d-0f43-3463-9905-efebdd6cc8b7 | -11.29546 | -47.51235 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea495b95-5e68-3704-9ea0-18a32a79a7f9 | -10.36161 | -47.89932 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd610596-2774-3860-b331-82ab68f88a87 | -13.24841 | -44.11153 | 2025-09-21 04:57:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e24e9e6-36df-3e1a-a400-bbae8bc82b07 | -7.94228 | -44.11293 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4306391d-bd90-39c5-be98-7f07a38f4ff4 | -7.93135 | -44.10342 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 293e0ecd-f1dd-30a5-92a8-aa9b982dcede | -13.36615 | -44.28355 | 2025-09-21 04:57:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f07fea6-27a6-3d98-8f5b-a96ed0232b05 | -14.21272 | -44.66345 | 2025-09-21 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e2bd529-0ef3-3aff-9c96-98e6912aa207 | -12.34929 | -43.76289 | 2025-09-21 04:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af6efd56-a503-3914-81fa-1a18dd2dc476 | -14.45135 | -46.50391 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26e66858-3c06-3017-840f-2ac09f86039b | -9.11356 | -60.96677 | 2025-09-21 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ddd7ba4-8f61-311c-9a7c-f71b5c5457b3 | -10.57235 | -48.5921 | 2025-09-21 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c41b1f6d-a048-3e37-9f47-45b4b3ce3a19 | -11.27499 | -47.40458 | 2025-09-21 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af18ebbd-5e8c-32c0-98f4-ad599eab6a7a | -13.89518 | -50.66104 | 2025-09-21 04:57:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec99432a-a3ba-3abf-b043-52b4162a0b8f | -9.05765 | -47.01433 | 2025-09-21 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27dabdef-6848-3c3c-902f-1afdd5f06f87 | -12.07711 | -44.85119 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b44325fc-3895-316f-bd67-c240692b5abd | -10.36094 | -47.90435 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da2ceff7-8565-3503-8be9-fefb39d158d1 | -14.44147 | -47.57109 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14b9ab74-ccfb-3bd5-8168-0edfaad93b53 | -11.14285 | -54.31604 | 2025-09-21 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bcf5c0e-82e9-3db8-bbe4-f0bd11b89756 | -11.28473 | -47.40593 | 2025-09-21 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6894efda-ebef-32e0-9b87-c80416f219a9 | -7.82846 | -45.62339 | 2025-09-21 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eaade3f4-01ba-3cd4-b5c1-f1fcac511890 | -10.34952 | -45.23315 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f97c6136-d2d4-303e-9d62-0dabae27043a | -11.30648 | -47.5035 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 081147f5-16cf-3f6f-a968-8d0a115f2e8d | -11.91679 | -55.5133 | 2025-09-21 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b0129b8-711e-353c-8ae7-e21d6a3a32ec | -10.29468 | -46.09129 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cbfb603e-4c4f-348b-9b2b-2c7449630d6f | -14.318 | -47.79665 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8027b58f-090e-37c7-af55-a3854b14fe63 | -12.05937 | -48.75556 | 2025-09-21 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2d3806f-c501-39f8-bd6b-d185d0e8119d | -10.26763 | -46.05228 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e0b799eb-7934-3c18-8558-e2a990fa2a9a | -7.92965 | -44.11589 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b88ef17b-7227-388f-955e-6ba1c5614856 | -7.80981 | -46.18971 | 2025-09-21 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfcccac9-179b-3492-89d9-097c79394baa | -7.93648 | -44.11215 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7bd2c6e-d596-3620-9c0a-46546bfdd0d7 | -7.93829 | -44.09592 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e298a703-7523-35da-a64d-754cd243c0d9 | -10.22182 | -48.07143 | 2025-09-21 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a902a05-3331-36a5-aed6-9a80b6e5c4c0 | -8.59871 | -45.34745 | 2025-09-21 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 438cedd5-ec77-307f-9fc2-504befa6cc08 | -13.68033 | -43.81659 | 2025-09-21 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 612f3c55-e972-3141-ace0-cc9d00557dcc | -8.35318 | -44.71155 | 2025-09-21 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2e69984-f120-3324-b546-308021b6ba34 | -8.9834 | -65.45397 | 2025-09-21 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3716eb2b-585c-3b8d-b0bf-bf54d0147ba8 | -12.70961 | -46.84271 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f002380f-069b-374c-b122-3f5e9f4a138f | -10.10362 | -64.89077 | 2025-09-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61ec547d-ff86-3ffd-8341-1d392d9e4c81 | -11.27997 | -41.84945 | 2025-09-21 04:57:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 75c049b1-fcf2-3559-bef0-9f8f597c179e | -14.44973 | -46.51727 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b053e47f-6a30-301b-b643-a9c7679e9ebc | -12.41743 | -45.11192 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5640e5c5-1bd4-353a-b1f7-3072049fc2f3 | -7.94295 | -44.10501 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b49f86e-40af-30eb-b701-b2c5e74fcd71 | -10.10433 | -64.88707 | 2025-09-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64b99c12-c5c2-3341-a627-99bff0fe60ec | -14.62469 | -48.27365 | 2025-09-21 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c02fb1c-0905-3fb1-9d51-99ead34c319a | -10.26721 | -46.05553 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7880d319-2d5a-3589-ba72-15526a898de4 | -12.71432 | -46.84716 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d117327c-3a1e-34f5-938f-f0ee5c4c0720 | -10.35001 | -45.22941 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e30887be-2f46-39e1-8ddf-c16679bd6ca1 | -7.92436 | -44.11465 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a30eadc-eb4a-342b-b094-ad66d0f985d8 | -13.64612 | -45.69665 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dae999c4-9c21-31a3-a31e-9d6f072dbac8 | -11.30239 | -47.4972 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b71675e4-2b8d-3f58-a0fb-904e85499f33 | -13.53301 | -43.00231 | 2025-09-21 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 43188a12-8e31-3457-aa15-300957b59679 | -8.71139 | -45.26445 | 2025-09-21 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0493707-9843-3ae6-acd8-e4df2669ee9d | -10.3623 | -47.8942 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fabbe91-1836-3ddd-9b0f-da3fca1762fa | -10.03714 | -46.26483 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3e473ce-b136-391c-a283-ef725453edbe | -11.77818 | -43.76566 | 2025-09-21 04:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 366177f4-93d9-3fa1-8c32-b7d10cdaabf7 | -14.62947 | -48.27447 | 2025-09-21 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51ab3bbc-163e-3ded-aeb1-85ad1e25e9b4 | -7.81018 | -46.18697 | 2025-09-21 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbec3fa9-1e85-3454-9592-cbd0bdcebd48 | -12.41695 | -45.11597 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1507599-b1c1-35a2-8d9f-25040728f0fc | -7.93022 | -44.11176 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42001782-5ee5-3957-acc9-d500f94a5015 | -7.93285 | -44.09458 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5cea00b1-dbe2-3186-af7a-e7fb63742aac | -10.34275 | -45.23531 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3303465-de83-3c73-81cc-c22d1a3a86de | -14.43795 | -47.56393 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e67435f-3877-318e-bc44-58737ab392f0 | -7.93772 | -44.10008 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84daf543-a63f-3ddd-bbd3-e344739daf9f | -12.71223 | -46.86438 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8737a261-c157-3ca1-addc-993a4cb02c02 | -7.92596 | -44.10217 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 084ceaca-16af-3b32-8a42-5c93b7d20d35 | -12.42697 | -45.13008 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eea3ffc-a50e-3bc3-a8e4-97056a4586e6 | -11.14673 | -54.31301 | 2025-09-21 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef3fe483-14a6-3fc6-b687-8334f55c23a9 | -14.45793 | -46.51482 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4557d7ea-8ad5-3cca-bc04-e4062a819f1e | -7.92489 | -44.11051 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be738677-11cf-3f93-afa4-5012438eef6e | -12.30986 | -44.87395 | 2025-09-21 04:57:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eae3ef1-1466-3605-b951-7e59a8e94f47 | -9.17079 | -44.6249 | 2025-09-21 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4274cf0-9ae6-3c00-a89d-1075451f6fc3 | -10.96838 | -54.10552 | 2025-09-21 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6081791f-3bc2-390b-835e-f5e157236b35 | -14.43581 | -47.58098 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 849c2f03-be67-3cc3-8605-8a99fd38f809 | -12.08806 | -44.85554 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f68dc3f5-03aa-3945-8282-76d1150b7bcb | -12.07673 | -44.80561 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| deac2b94-8dfb-3d2c-982b-f5560bdcec5f | -9.4189 | -44.71151 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79fce464-2b65-30dc-8b55-31df5a884b28 | -14.45247 | -46.51466 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44337cee-6415-3cb3-a46c-455b453617c8 | -14.60448 | -49.762 | 2025-09-21 04:57:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24a3445d-7287-3f24-af8c-8bb311bbd5bb | -12.7027 | -46.84034 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee0ecb02-53cf-3206-a315-e4e85e736477 | -9.11429 | -60.96258 | 2025-09-21 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c84cca8-5bd9-372e-ba89-15e516a01e62 | -10.96558 | -54.10142 | 2025-09-21 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2701022d-482c-3c8a-a1d2-7b169654eb83 | -11.29961 | -47.51822 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54a32969-de12-3a2f-a683-299a29031b4c | -11.29755 | -47.49654 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 788f9a0c-6825-329c-9824-cd635050c4af | -11.30581 | -47.50857 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5baff46b-f7a7-3c68-931a-c7cd7d3961fe | -14.97335 | -44.41916 | 2025-09-21 04:57:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eee1d55-5f4a-33d8-a082-48748df75c01 | -14.97227 | -44.42916 | 2025-09-21 04:57:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5274a4f4-4288-3e90-9ace-1066b7dff567 | -11.52472 | -48.55159 | 2025-09-21 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 305736f0-c3a8-3a24-83fb-76846b2dc4a5 | -12.70406 | -46.84522 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e1bdbc6-5fe8-3ca9-baac-918eabad96e0 | -10.35231 | -47.8981 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92d1c909-34b2-331c-9a71-4c5a43157360 | -14.43182 | -47.57206 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2aab9e65-22d2-3b92-84ff-0adbc24ef50f | -14.45598 | -46.511 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c45db8a4-2ca2-3651-8abb-0f2951350dd4 | -9.43137 | -44.70473 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dce5d419-e8f6-3eaa-95a8-4f1c11485e58 | -13.53845 | -43.01432 | 2025-09-21 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 1ade6c87-4354-3b5a-ad4c-4a38ac82bda5 | -12.08834 | -44.85627 | 2025-09-21 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c3495bb-fdc0-357f-a4bc-b9b7eebc98cf | -14.447 | -46.5146 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f319b21-ce26-3940-af7e-e11891d2f03b | -7.93864 | -44.09547 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0c6cb2a4-7124-3132-9f57-00b3e10eee47 | -11.50092 | -43.59223 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aaaa202-6d39-3506-a194-4b6bc71115b1 | -12.71254 | -46.84541 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a829bf6d-7566-31b1-a894-2af998379523 | -12.08305 | -44.80251 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README38.md)
