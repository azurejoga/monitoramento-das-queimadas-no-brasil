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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eb4c02d-f4f7-3535-bab9-1451db3d788b | -19.49729 | -56.72665 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1ab64f4d-097f-3e4d-a229-0ab8cea57439 | -19.49482 | -56.59658 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 31d75f6d-5775-352b-87bd-8e81df7711c8 | -19.49429 | -56.60278 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 41676ee9-75df-3a6e-94f6-10b13516de45 | -19.49377 | -56.60899 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9d16b5fa-8041-3641-97e9-b6d3469a44b6 | -19.49325 | -56.61517 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bdfc4764-d888-3730-b350-349a0fbf76fa | -19.49273 | -56.62133 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9ff2498d-d752-3d2b-b5a7-c65415b3f4d7 | -19.49164 | -56.71386 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2cb46405-6770-3db5-91a9-8e6a6c5b99eb | -19.49112 | -56.71992 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 40173566-651f-3442-8696-94271b08eea7 | -19.49061 | -56.72599 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| aa7707e4-4b6f-3e53-a23a-e476afdfe182 | -19.49009 | -56.73205 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d2b8d9e6-ff0d-395c-8b3c-f0fcae530518 | -19.48957 | -56.7381 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 8939e6f2-424d-3626-86ac-13f031ec13b8 | -19.48905 | -56.74414 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7926efbc-23a3-3f5d-b60d-c94cb3287428 | -19.48704 | -56.60833 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f1c5a03-88e2-32c6-b080-48a6b5638a9d | -19.48601 | -56.62066 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4a21c175-eb44-3c03-8a89-c5584ca0d647 | -19.48444 | -56.71925 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2d3a206f-31b2-3180-92f6-32b45911b30f | -19.48392 | -56.72531 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 03942822-d94d-3ce0-82cf-54f8d1a03440 | -19.48083 | -56.60143 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fd3d027f-e731-34c1-a94e-6cef3b3099da | -19.47148 | -56.60762 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a34b8ebf-2171-3978-a078-4ca54a4e7a6a | -19.46686 | -56.60624 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 47de942c-d27c-3dba-8e12-2130987075ef | -19.46634 | -56.61243 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| af71c51b-854e-3775-8685-43a20e8bb2c8 | -19.46475 | -56.60697 | 2024-11-01 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1472d27b-1ff5-33a7-ace9-af84de952b67 | -3.0538 | -49.4895 | 2024-11-01 05:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ffb6a026-188f-3d28-a385-fb7c2f84868f | -3.0354 | -49.4688 | 2024-11-01 05:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5fa63e4f-1c20-3afc-86b6-f3abf8587da1 | -3.0353 | -49.4901 | 2024-11-01 05:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 48352d31-d053-3b47-8076-d9049fc4c3a9 | -3.0539 | -49.4683 | 2024-11-01 05:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3007c18d-326e-3044-be84-57122b77006f | -4.4054 | -43.4746 | 2024-11-01 05:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 9757ba26-4680-327e-9b0b-f31e57400606 | -3.0353 | -49.4901 | 2024-11-01 06:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 248aa5f5-1ad1-3add-85ba-25c62db9e5e6 | -3.0354 | -49.4688 | 2024-11-01 06:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 3cb780f5-fed3-303e-b596-23ccc62a1aec | -3.0538 | -49.4895 | 2024-11-01 06:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| d1762647-ce6b-3a70-8eac-86c41175a770 | -4.4054 | -43.4746 | 2024-11-01 06:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 6b7c7f76-f578-3644-8d96-63069a47c496 | -0.79503 | -63.0821 | 2024-11-01 06:10:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e458be7-23b0-333b-9344-01cf9d88c5cb | -0.79454 | -63.08532 | 2024-11-01 06:10:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aad02bd-9ce3-3eec-810b-f604bc8c4524 | 2.57548 | -60.69744 | 2024-11-01 06:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3dd89cf-6c2a-36a2-b7ab-590130d060bd | 2.56964 | -60.69842 | 2024-11-01 06:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47524179-b6b0-34bf-8c18-b37b659a9cba | -8.04589 | -71.24062 | 2024-11-01 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e1f7ca5-31ab-3461-8562-6ef0540935ed | -8.02086 | -70.7403 | 2024-11-01 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86f4f6ec-6241-3631-a2e9-3d6f64093383 | -7.90692 | -72.86871 | 2024-11-01 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fedfbab3-0fb8-321f-bc4d-e6fba5a60857 | -7.90432 | -72.33291 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a3172aa-77d3-3a45-91f4-f1e8c192dd97 | -7.90378 | -72.33648 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dccadcf-49d7-3306-bb04-b780e195c373 | -7.90211 | -72.33241 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bea14059-6f98-388b-8ab6-848b94e1e154 | -7.90155 | -72.33598 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 853b0e6d-c055-34c5-adf7-de1c020bc754 | -7.82552 | -72.78044 | 2024-11-01 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 007fda8f-5a37-3d2d-aa3e-e60ec3bcb82d | -7.81422 | -73.11496 | 2024-11-01 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a4b6e9d-043e-35eb-83b2-1478ef68d069 | -7.80537 | -72.93129 | 2024-11-01 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e689447-cc64-3040-b31d-1dfc62470014 | -7.80482 | -72.93478 | 2024-11-01 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b3b4cbd-b85e-3ae7-9a90-40275f5f24b3 | -7.75302 | -72.28387 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46aab8f4-2364-37c4-90c7-2feb6aff7d05 | -7.63387 | -72.46191 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a239ab94-70de-3bd4-a22c-c4368fc56d19 | -7.63054 | -72.4614 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7f88065-820c-3c30-a13c-4fb1f26d061f | -7.49097 | -72.83548 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93323ffb-e67f-3088-a6b7-9503ecc01239 | -7.48765 | -72.83496 | 2024-11-01 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d430462-e30e-32cb-a182-8d1965d5295a | -6.95668 | -71.79052 | 2024-11-01 06:12:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31388e96-0a20-35db-b2f9-f6928d7ac79c | -5.24836 | -60.16765 | 2024-11-01 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07d5f284-3003-350d-96ef-79f99ce6a23c | -5.24372 | -60.16763 | 2024-11-01 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a5b78fc-c184-3033-ad7f-af69896c42db | -5.2416 | -60.16677 | 2024-11-01 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de1d0e9b-361d-3116-ac8e-94b50fad7563 | -8.62718 | -69.72008 | 2024-11-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7a6b49c-2939-331a-bed1-9d1b8ad2b181 | -8.6236 | -69.71715 | 2024-11-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7cdb57dc-f7d2-3983-9b6c-919ed2f70318 | -8.6234 | -69.71951 | 2024-11-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9e0c424-973c-3526-9ed0-3b8a46b4a771 | -8.62294 | -69.72178 | 2024-11-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c5ed3339-c9e4-3e54-8103-97ab005e929f | -8.62271 | -69.72412 | 2024-11-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffdf02e0-af6d-33c2-a036-f04cc170fbc8 | -8.6117 | -69.7461 | 2024-11-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4147844b-e9f6-30ae-8416-040c9821aea5 | -8.52722 | -69.97985 | 2024-11-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f96ac1ca-c03e-351f-9492-6dd2c75427fa | -8.33439 | -72.60674 | 2024-11-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 925901e5-2a0a-3fb2-9c28-c79d9ce96ce3 | -8.33385 | -72.61029 | 2024-11-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fb3425d-f3a6-3dae-a263-6d16641f1a7f | -8.32996 | -72.61332 | 2024-11-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f023860-5ae7-391a-baa9-16328f482306 | -8.28786 | -72.66483 | 2024-11-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67a8bfd1-c88c-3832-8c4a-4d27b3d45253 | -8.28732 | -72.66837 | 2024-11-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaf263b6-0ce5-3ae1-9319-d621aa37225e | -10.85606 | -69.28763 | 2024-11-01 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f406da0e-c0b1-3913-b009-679e76aa3e0e | -10.85427 | -68.23042 | 2024-11-01 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e1da73c-c1a4-3edc-afee-2003b3ceab8c | -10.83489 | -69.35271 | 2024-11-01 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 090ffc8a-e491-3da4-8750-75a777fad26b | -10.83284 | -69.35249 | 2024-11-01 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 127a464e-5318-3b3d-b144-970aef9f4802 | -10.72695 | -68.87033 | 2024-11-01 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0316b6b-bfc7-3ec6-aaaa-6fbf92f2e90d | -10.62578 | -69.67789 | 2024-11-01 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c43ebaff-bc3c-3d5e-bf4f-d10b2e6c02c3 | -10.57559 | -69.6958 | 2024-11-01 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c47450-889f-3da2-b3ce-b130ddfca988 | -10.57499 | -69.69456 | 2024-11-01 06:14:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b34c7a6-9a90-3745-9910-4c1f40b3ce68 | -10.45324 | -69.19781 | 2024-11-01 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1955bb96-a1ad-36ce-9991-f8f4482cb66b | -10.41785 | -68.39165 | 2024-11-01 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf353ce-f3e5-34bb-bce2-d0df9ce6a5cb | -10.41729 | -68.39561 | 2024-11-01 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f1594f3-929a-33b4-bc26-a86713343001 | -10.24488 | -68.30323 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b6c080f-acb1-31c8-90d7-34ac51219cca | -10.12118 | -67.59335 | 2024-11-01 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b19f2eb-2f8a-38d9-9c1e-f1700b8a1986 | -10.12059 | -67.59778 | 2024-11-01 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb5cac2a-2324-311f-b493-f8f482ef9094 | -10.11737 | -67.59426 | 2024-11-01 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6811a19d-6765-3288-9074-72d79fda6a27 | -10.11673 | -67.59282 | 2024-11-01 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0133d09-ec06-334c-a736-69c12d863850 | -10.11614 | -67.59725 | 2024-11-01 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1580c4b1-d54b-302c-a0a3-ad82bec50d5a | -10.10069 | -68.37786 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 201fe184-c089-3e2e-9d2b-4b8318289b4c | -10.10013 | -68.38178 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 760eb0c4-94ee-381f-8ab9-2931070081d6 | -10.09957 | -68.3857 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1845fa2-8f83-39e1-bb6c-7a285ea8f5ae | -10.09816 | -68.36553 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5dd6f3d0-f329-3d0d-a34e-ff0897a4bb67 | -10.0976 | -68.36947 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2c4d610-7092-3e93-a584-cd18e6944197 | -10.09648 | -68.3773 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34a75fc2-c631-3037-894a-dd6a7ae6e66c | -10.09592 | -68.38122 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed42123e-85c3-3182-a97a-e4e5054da7c3 | -10.09283 | -68.37279 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8fed479-5b5e-37bf-8133-daf1e490c05e | -10.09227 | -68.37669 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8b382e6-7b22-3379-a715-0ea9787ecad5 | -10.09172 | -68.3806 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f35a3729-d7fc-379c-93cc-5816403bd7e8 | -10.08807 | -68.37608 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8bebc77-ba5e-399a-b9f2-045423f8b1ee | -10.0781 | -68.2942 | 2024-11-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99f7d257-ee9c-3ba6-9731-632b76cb93cc | -9.569 | -66.63258 | 2024-11-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e574d503-2f5d-3ff7-a6e9-e44cb4649f04 | -9.6991 | -66.14088 | 2024-11-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d89798f7-7123-30c4-8e9e-df81c6d7286e | -9.69839 | -66.14623 | 2024-11-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b5c2f5e-fd0b-30d5-b89a-f09d3fef6a6d | -9.67759 | -68.35518 | 2024-11-01 06:14:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64b9c201-ced1-359e-a580-df830243f9f5 | -9.56831 | -66.6376 | 2024-11-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README55.md)
