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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a37fb310-97bd-3600-8907-3fc7778e0ffa | -3.73761 | -52.04263 | 2024-11-18 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3861b5fa-919b-305b-95b8-c72ccd0937be | -4.71948 | -49.61947 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07ccd969-16bc-3b55-bdf6-59c144edf94e | -5.58659 | -45.20713 | 2024-11-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 858340b1-aea2-333c-97ac-beb4dba7ce5f | -4.10453 | -46.87017 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9763e30a-528a-3aff-808a-13547fb9f1e5 | -2.84683 | -54.01334 | 2024-11-18 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81664ff6-af28-3ff0-9660-cc6d2065d571 | -3.89572 | -50.08635 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bca59946-cc4a-3c75-9dce-ebce57c9f258 | -4.99515 | -46.80275 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 341af4c3-4c27-3071-a4b2-66e6c8b9b96c | -5.95769 | -42.16483 | 2024-11-18 04:12:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 00c8e1d3-f2dc-3c22-ab5a-e2daf276f44c | -4.53619 | -48.49588 | 2024-11-18 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cca80819-4107-3b53-8070-2df560651194 | -4.96756 | -44.07138 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7dfb63cc-3af0-35b1-bbe8-9998fc2e353b | -3.18754 | -53.23835 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd1b11db-3c02-3fb8-be77-1017994e437f | -3.40862 | -53.30714 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fdbb621-7470-3703-885a-440a1f65d310 | -4.9971 | -44.33024 | 2024-11-18 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d6f6449-ff2a-355a-9538-b64de98e83a0 | -3.18462 | -53.25541 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6d9f54a-18a5-37dd-ad8c-3e0174d153d3 | -7.00172 | -37.89748 | 2024-11-18 04:12:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e72e69dd-97e9-38cb-adb1-d17085c9b789 | -11.85275 | -46.93223 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a98232e-86cc-3733-81ca-cb5a3ec4cc1d | -11.48726 | -42.94859 | 2024-11-18 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee37db6b-b92d-319a-aa06-f33b149d47d2 | -11.37297 | -49.79827 | 2024-11-18 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bded13e-fe2c-3dee-9f74-9938c853dabd | -13.21798 | -54.16199 | 2024-11-18 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a5be171-c929-3173-a8e1-31132e745596 | -11.11963 | -45.2919 | 2024-11-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eda6a0e9-90b4-3e3a-8d41-228545a4a5ad | -11.77168 | -40.90592 | 2024-11-18 04:14:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8ae0e7b8-aa24-3349-8fe2-73e3f6efe734 | -12.71968 | -46.7291 | 2024-11-18 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 37b8a7eb-0f74-3ea7-8396-8a87042a0643 | -11.83349 | -47.09003 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 489ac4f1-2051-3d44-9fff-7e3b9ec072bf | -11.81858 | -47.07075 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab08787b-081a-3635-b1ba-ee6ae9ffc24a | -11.11905 | -45.29549 | 2024-11-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d983fdba-5073-38f0-9d34-885325451012 | -11.93454 | -44.55383 | 2024-11-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4148828-ecdb-3e1b-894e-a690eb497369 | -13.43461 | -43.03019 | 2024-11-18 04:14:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f5ac3fd8-f98f-3166-a898-72f2be99d626 | -11.11718 | -45.29197 | 2024-11-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c89fabb5-8b1e-3895-aec4-987d40d5d456 | -10.12786 | -49.15184 | 2024-11-18 04:14:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e3c353a-325f-3801-8e0c-f74dded9b014 | -11.20371 | -49.96848 | 2024-11-18 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51c100db-b900-3ad1-b94a-9e5f05669a2c | -10.8742 | -43.36562 | 2024-11-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7bde52e9-8fe3-377d-ab73-aac38465a5bd | -12.82684 | -43.88528 | 2024-11-18 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf367a3d-3d27-3164-89d0-da91d785309b | -12.82761 | -43.19702 | 2024-11-18 04:14:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6d86eef2-c20b-34c5-b154-be3694156838 | -11.16025 | -45.10422 | 2024-11-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 972fec98-7fa9-32e3-bdf9-8ee3fd490445 | -10.52617 | -44.94669 | 2024-11-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd927326-d465-35ce-b730-72838e3528d1 | -11.48672 | -42.95221 | 2024-11-18 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d45bfd4-8df9-32c1-9fe2-d359fd363516 | -11.14552 | -45.34408 | 2024-11-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4104c77-d412-370d-b67a-a5c037bdaaa8 | -10.52674 | -44.94314 | 2024-11-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7cd3254-77ba-3d2b-9815-d034aef43e1c | -11.85209 | -46.93621 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a643ee7-e0a7-3f06-a1cc-ae5ee6fa6cf4 | -10.86415 | -47.69552 | 2024-11-18 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17870e2a-69c9-3eb8-b77b-0e785e5cacf8 | -12.55503 | -57.82238 | 2024-11-18 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dc91a8d-2c5e-3cf8-a413-ca32a452eb2a | -10.12848 | -49.14822 | 2024-11-18 04:14:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05a89861-6bdd-31af-99ae-3689e8938b06 | -13.22332 | -54.16314 | 2024-11-18 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d7b477-c3d9-344b-97ed-cc5b12f05280 | -11.85559 | -46.93679 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5810ddeb-13e4-3fe7-b12c-59c25445feb4 | -13.01554 | -56.46647 | 2024-11-18 04:14:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69c6745f-645d-381c-bacd-12976b5f2d28 | -12.79548 | -46.41576 | 2024-11-18 04:14:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be4db1f5-e2df-334e-8740-7e5a0bcd2684 | -11.82211 | -47.07138 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37912408-0708-315d-9cd4-290dd10ff56f | -11.52975 | -45.00466 | 2024-11-18 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c0a1b3f-63ee-3b29-a18b-18b1acb4a49d | -11.96553 | -44.22777 | 2024-11-18 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c81c00-1b52-3d5f-89bc-f229597521a3 | -11.83281 | -47.09408 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e30f250c-005a-3c23-8305-77f6b39a9fee | -13.01655 | -56.46143 | 2024-11-18 04:14:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a59303c9-9d6e-321d-ad3a-eb44e312f787 | -10.86047 | -47.6949 | 2024-11-18 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c8f6a3-e9f1-354f-812c-37a350ce69b8 | -11.83633 | -47.09472 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73ddc665-011b-321b-a22d-1030393f03b9 | -10.52284 | -44.94613 | 2024-11-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de865a0-7ade-34f7-ae48-0e72d1d37b65 | -12.68964 | -44.48206 | 2024-11-18 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dabb271b-5611-3fc3-b05b-f202a981a74a | -13.17641 | -46.95545 | 2024-11-18 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3773da73-569a-3376-befe-6c33663a67f6 | -11.83701 | -47.09066 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b289834c-32d7-3c7e-9c6f-1326742fb48f | -11.36883 | -49.79749 | 2024-11-18 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 353de6d8-3e54-3906-bd79-cbc522b6a438 | -12.54828 | -57.82099 | 2024-11-18 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 775b85c9-e307-36d9-90f4-4853701bd7e1 | -11.81506 | -47.07012 | 2024-11-18 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d0b328e9-91ba-3f5f-997a-1d7310484a87 | -10.52629 | -44.90646 | 2024-11-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1d760d1-fcd8-30b7-a103-f0b031b6cb69 | -12.72043 | -43.95921 | 2024-11-18 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a025c3-67ee-3e97-8750-85f1e63248d0 | -12.51732 | -44.08587 | 2024-11-18 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8e7b995-42e4-3145-aafa-6203be133d66 | -11.53598 | -51.27793 | 2024-11-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd33b6f0-1cc5-3d9f-947d-b7c8e6e2187a | -10.85541 | -47.65801 | 2024-11-18 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3dcd086-094b-3dcb-8120-a93919a2c93d | -10.44087 | -44.88522 | 2024-11-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0724e339-0f52-3ae8-a6f6-3aa8840e8c89 | -12.54692 | -57.82743 | 2024-11-18 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28dfa5cc-f5f6-3d39-8c77-09b7b0488828 | -12.82629 | -43.88883 | 2024-11-18 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e50454-eb04-3544-8366-fce00fc031f1 | -10.52798 | -44.89581 | 2024-11-18 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7299b39-0430-3411-84bf-6d6db7ae799d | -10.57715 | -45.11954 | 2024-11-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac3414ce-1d2b-309e-87b4-c20d23d2acaf | -10.87365 | -43.36917 | 2024-11-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e95404d-983f-3fdc-92cc-775e72c5b6d2 | -11.46342 | -48.00977 | 2024-11-18 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29f47827-d9fa-3474-978d-bd9e035a40f4 | -13.22868 | -54.16415 | 2024-11-18 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4765e3a-5043-3972-abc3-21ecb3a0be19 | -11.67637 | -46.41431 | 2024-11-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82971c11-3c95-37b4-8c61-d2b949f9e785 | -10.85616 | -47.65364 | 2024-11-18 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9414fbb3-31fc-371d-8454-23ea14f8d94a | -22.67571 | -42.85556 | 2024-11-18 04:16:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 33f6c5ce-a2e3-3e49-8bb0-485f892de969 | -17.60931 | -57.56796 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 05328265-c6c2-38a4-9359-7502ff545b15 | -17.60999 | -57.62129 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ba501c67-9e4b-394e-84dc-745fdd2d6e4d | -23.63019 | -50.56118 | 2024-11-18 04:16:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d63e704-6366-3be5-b3c6-94fdf8d90a79 | -25.19162 | -49.3293 | 2024-11-18 04:16:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4c5cc619-4c44-30b8-89c5-d16e9ff9bb27 | -17.69988 | -54.09197 | 2024-11-18 04:16:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6b1f1fa-5bc2-388a-9807-fba1471afb2b | -17.6143 | -57.57432 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| cd315a89-b277-31dd-a503-d2792bd1feeb | -20.99482 | -51.79531 | 2024-11-18 04:16:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e712ecae-0f1b-3e91-9923-1c9ee2c5bfbb | -25.03783 | -50.05561 | 2024-11-18 04:16:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 474150d9-d938-3d68-b932-fde848f24875 | -17.60882 | -57.56975 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d833a9f3-374f-3274-beb0-e720c2d05702 | -25.03709 | -50.05981 | 2024-11-18 04:16:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f2490a97-c373-33d4-a57b-dbdbc1df368b | -23.63001 | -46.42521 | 2024-11-18 04:16:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 78acd749-886c-3b71-9836-48e2fcedcb46 | -17.60664 | -57.57942 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 32b6f999-a0b8-3b5c-aa5a-f9bcaab845c5 | -22.90194 | -43.75581 | 2024-11-18 04:16:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 34daa251-cb11-3781-be23-bd4d34d0efa4 | -22.29261 | -49.05426 | 2024-11-18 04:16:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce9473a7-44ad-3c74-9ecb-3583f9c4f6e5 | -23.3389 | -46.77263 | 2024-11-18 04:16:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 84a0197b-09e9-3424-8d20-f008d4b7c75c | -17.60721 | -57.6052 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ca8d5b4e-8053-3991-9d5f-fedf1554c60a | -18.00866 | -52.37243 | 2024-11-18 04:16:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54feaa5e-1aa1-3b48-8e08-27f5267db4bc | -17.69864 | -54.09056 | 2024-11-18 04:16:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbd83778-1390-3bf4-96cb-6d23e2775418 | -17.61536 | -57.56948 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 7db5a156-87d3-31db-b505-540e7598c404 | -17.61765 | -57.58727 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 02711d0c-fbcf-32b8-ac2b-e75f47511dbf | -17.61112 | -57.58891 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 74bb7688-b203-3846-801d-5e5a7eb029d3 | -17.61983 | -57.57757 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 4aecd7a8-b05c-3ee7-ae27-05436d14217b | -17.61823 | -57.58556 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| daa88ead-d535-3310-85ce-f5b18bebcd75 | -17.60719 | -57.57766 | 2024-11-18 04:16:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |


[Clique aqui para ver as próximas entradas](README27.md)
