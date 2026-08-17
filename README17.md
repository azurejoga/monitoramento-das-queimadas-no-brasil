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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59c5687a-603a-3aa7-b7ef-a85c1ea95f92 | -11.49574 | -46.61266 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e89c8a38-4d12-3093-8f59-3ad99cfe1149 | -7.38374 | -55.48893 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0798d0c-3678-3968-b17a-c5d81d94fcc0 | -12.66975 | -48.4808 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aec56ac4-7413-3f0d-b9a1-135fc769e605 | -10.47408 | -45.14322 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef3bcbb4-c589-37b4-951e-6ec49dec6260 | -9.34691 | -50.33334 | 2026-08-17 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| faa1d983-8a71-3bd0-8c5f-e340671973ff | -11.46922 | -46.58661 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 531892eb-b52a-3797-898a-a87e0b951361 | -14.30025 | -47.20301 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d30136f-ae0a-3c1c-9617-e1122975e1f9 | -8.63042 | -54.71993 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cfbd962-f4f1-33d5-a7e6-ecfc0cf8c4a5 | -11.23894 | -54.02017 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58911be7-4ca2-3c4e-8537-db313a3bdff6 | -11.81385 | -51.77232 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 044dedcf-80ee-3f08-babe-8c92b6a93b87 | -12.69165 | -48.52052 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4614fa19-0864-38d9-b746-ab566eb3ea50 | -14.45831 | -53.07902 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d326993-e6ec-391a-894b-43d9d0733e3f | -13.50724 | -46.23235 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f7cfa83-7a7b-3871-9f82-d3acb6b20278 | -13.52708 | -46.23558 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1401494-773d-3eca-93fb-eb71c8e090f0 | -14.88202 | -46.63838 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 634c01cb-4306-3005-a249-856d6005511b | -12.54217 | -47.8684 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdc9802f-f945-395f-9489-86ea208c4d57 | -15.12506 | -50.05538 | 2026-08-17 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71675076-65ae-3128-9e46-888c97bdafb2 | -11.70441 | -54.62252 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5da3998f-0cd5-305a-93f1-61db5ef9c2df | -12.67157 | -48.51281 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 28e234cc-c0c1-33d3-91ee-9edeb3fea1b9 | -7.37351 | -55.51269 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbf32e01-af2a-3ef6-bb6f-648da8527dad | -13.51663 | -46.25919 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d8cca7a-55c1-3ca5-8316-a4151bd82f94 | -12.67847 | -48.51414 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d8abdf35-b51a-3c13-8ee0-5e4b181506f2 | -13.28102 | -48.69386 | 2026-08-17 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d6a0fa0-98b4-3e1f-8cb0-0eb41754a7c2 | -12.02658 | -46.4391 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2e04798-efd3-3717-80a8-69b217243496 | -14.1904 | -53.05727 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a83340f3-d22e-311e-a9af-a346994f9645 | -11.31587 | -45.87381 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86ae9aa0-09c8-3a3f-8cc1-c073d98f9399 | -12.0481 | -46.45336 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5cc1c87-8d07-35a1-a63c-118fc3bb3e86 | -11.22533 | -54.01154 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f303fa9-acfc-33e7-bc94-ae7be84fec2c | -8.52518 | -54.88649 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a975ac33-f28a-3bd7-9e42-684cf9a70ebc | -15.0307 | -47.0355 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68b4e0a7-2842-3dde-b500-5c45ffd59012 | -11.10857 | -47.24315 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0b7859c-7234-3cf2-86aa-bc0220266580 | -12.25966 | -45.88222 | 2026-08-17 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 723656d1-df66-30cc-8fa1-299e2f543679 | -12.00111 | -46.47124 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a3fee1f-a08a-3802-83ce-072c06d987d9 | -10.47736 | -50.36824 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3738f27e-a1ac-3287-a8f6-89773ac275b0 | -11.71572 | -54.59042 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7992d8d0-3454-3f31-b097-038ff5e0c411 | -11.88065 | -50.22328 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24a2a3d3-171a-34de-a98f-70f8c94c00e4 | -11.88526 | -50.2192 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3da8f35e-4641-31b1-a466-d1e67147d8bf | -7.37065 | -55.49537 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad1c6bde-1da4-39fa-9776-3db9626c7459 | -12.66397 | -48.5157 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a65845a6-f135-3dea-9be4-6b0248c986b0 | -11.49302 | -46.58677 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 073f22b6-e991-37e2-8ae2-06f227b5dfc5 | -12.25641 | -45.92493 | 2026-08-17 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2e5c7fc-8ae2-315b-a872-fff2c1dad5e4 | -14.46067 | -51.84097 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56189a34-efe3-35a1-b459-a646c207f071 | -12.24846 | -43.14321 | 2026-08-17 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ed742126-8f75-3f8f-aa50-2a6ccd9c7259 | -12.71346 | -48.49611 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b7d3dce-72c7-37cc-a450-b6006f5756eb | -8.5645 | -45.33274 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d61058e2-04f8-3001-9cf3-fc1688a56a99 | -7.38078 | -55.50543 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1dfeb77-05f1-3a5a-b595-69eae14ce78b | -11.718 | -54.60614 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c470a34c-4d5c-3742-859e-25896d270c32 | -11.61509 | -47.7996 | 2026-08-17 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ea124fa-96d7-3bff-aeec-cb09e6106794 | -14.3064 | -47.18573 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83b2c160-c626-3b8b-acc2-0c40769d7353 | -12.5699 | -47.86924 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dffafac8-dfe1-3064-8017-96cdc1aa80f3 | -12.65617 | -48.49834 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ee418a29-e775-36aa-88f6-f0c170fb2850 | -14.48924 | -51.98751 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5babe8e-e345-3a68-8293-1e18a2c7cb4e | -12.76216 | -48.43169 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a5efeb6-264a-3bdc-a16e-700c7a38a18c | -10.18795 | -46.40717 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f06777c3-19df-3bc1-9aca-c26ad20d9e80 | -13.4666 | -51.80296 | 2026-08-17 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0caec76b-355d-3a50-b038-032c7ddb3836 | -11.32076 | -46.21213 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afff2e6d-f03e-308c-b65e-ecee82e3ebd5 | -11.23511 | -54.01355 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c841d658-2ef4-363c-abc3-b094e69de414 | -11.21694 | -54.01972 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 711f7e78-a4c4-3579-b818-e1c153f24e9e | -11.82223 | -51.7738 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff2432da-53b4-3f11-964b-713cf3be505b | -11.09571 | -47.3011 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca9209e6-a471-3f64-bdbc-2d7bbb22c87d | -11.49241 | -46.61214 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25866618-2e2e-3d55-a350-674d13a65593 | -6.87523 | -56.41833 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c122a66a-8833-30a5-99e4-1763eafaeab8 | -15.09095 | -47.01979 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6d47681-cd9a-394a-861d-203ada78852c | -13.44068 | -43.83979 | 2026-08-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6c02192b-ff40-3268-9714-15153216b285 | -14.14453 | -52.88431 | 2026-08-17 04:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7816a02a-976f-328a-953b-987a18054da7 | -14.88147 | -46.64194 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8e7dedf-f6f8-3038-a1ce-5013fdc6b31f | -11.70843 | -54.60126 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64ccc589-2802-35af-b653-9629a27cdcc0 | -15.16627 | -48.6665 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ccd2f1a-6ebe-3d0b-9829-2b9c0759c08f | -11.72193 | -54.61311 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75c4b349-da1c-382c-b73b-563ddeaabad4 | -12.68819 | -48.51991 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8eac2bc6-8e8f-3917-af08-013b6045007b | -7.38286 | -55.49598 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bfdf1fa-e0f3-31f1-859f-52c901dc12af | -12.54799 | -47.8541 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87700c43-c993-331b-8bf4-55f3e7cfac5c | -8.51155 | -54.89929 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df188f6f-89d4-3c4d-ab01-0c16fd27dacd | -9.30593 | -49.09842 | 2026-08-17 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03846026-cbe3-3f71-9a54-ace51d71e025 | -10.46837 | -50.37395 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a093ae14-a017-3012-826e-76174100d1ce | -12.7068 | -48.51501 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2ca5b58-89d4-3f10-8338-a9c589d7c298 | -14.87321 | -46.65145 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15cbdf18-9682-31a7-90c2-951d2ad622b7 | -7.39171 | -55.4777 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6eb020b-3f90-3aeb-a0c4-f91b31c79e60 | -11.71342 | -54.63047 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 351d0ada-9ac2-3b44-9d1a-5baa90dab8d1 | -11.3213 | -47.0044 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cfcabd9-e02c-37cd-9dc6-487b4625be47 | -15.04232 | -47.02645 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d2e5862-fe72-3b55-a5b8-5f294b8fb692 | -14.4864 | -45.67716 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84131116-52d0-3c94-b4f4-da40d71908d3 | -12.5647 | -47.87979 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c21217b7-443b-3cd8-890e-ba6546fa9f33 | -10.3912 | -48.2673 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdf93af9-bbe2-3fd3-bcc6-8f76bd325e23 | -13.50725 | -46.25404 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d47a00-a0b2-3835-814f-9b71ba4a716c | -7.37424 | -55.50861 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50c2ab01-ba3a-3e26-8862-3efa6ca100d8 | -10.27659 | -48.28483 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b42bf33-b4e2-3e5c-887e-5f74a98bde60 | -12.46291 | -46.66964 | 2026-08-17 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55854827-5fb5-34b7-a8ba-258e084e9128 | -14.97482 | -46.58783 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcd76a38-7414-3653-ae6c-c58e150581cf | -11.11748 | -47.25211 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92ca4e75-4317-335b-889b-e6a39c0ba88c | -9.1212 | -46.01181 | 2026-08-17 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da3b4cbe-968c-37da-9a2f-5ae467e6e5a3 | -11.97729 | -46.44878 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9eee8fb7-ae98-39f9-8072-be9b59828722 | -11.13603 | -46.52136 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d76a49e5-92e6-35f1-b43f-2b23d59d71c0 | -12.53974 | -47.88322 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20295320-61e2-34fc-845e-163749910559 | -8.52324 | -54.89709 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1012ca54-c7e0-3958-8d13-e14bb9e2e1e4 | -14.28583 | -47.20795 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c07105b1-bf07-37ee-a6dd-3bc924bf2daa | -14.29749 | -47.19889 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cfb31fe-c2e3-35f7-bbff-b5dc66e33bf8 | -12.32877 | -47.25493 | 2026-08-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 405c84c0-5df9-3d18-a865-c638f7c1dbc4 | -10.27936 | -48.28607 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef5ab29b-feed-3de7-8f36-62a5dbea913e | -8.93462 | -47.60718 | 2026-08-17 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
