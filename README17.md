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
| 42e382ae-04a2-391b-ae4a-c635fbacce46 | -8.87282 | -49.00985 | 2025-07-27 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34531476-474f-3ef1-96b1-abb488684c16 | -7.75398 | -51.13554 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee340429-cfa7-3727-8436-1d04d299e855 | -6.67076 | -43.97406 | 2025-07-27 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5fe012f-9fae-3994-9445-81dc09c9379f | -9.92293 | -48.90082 | 2025-07-27 04:57:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0a669e2-c02f-3a30-ba51-59f7178862e8 | -6.66097 | -58.83635 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20524d93-3426-3de4-af76-d0a60066f8aa | -7.29171 | -60.1887 | 2025-07-27 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c6b4929-1c86-34d2-a748-5a10ec07c625 | -6.67091 | -43.97279 | 2025-07-27 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dae4063-9a7d-3531-9b25-fb36e3ff1df3 | -6.01326 | -44.05097 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab32b571-889b-35ba-bfa8-2958c3e80dac | -5.18682 | -44.95777 | 2025-07-27 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1ff327d7-4e9c-3b6d-b612-567edd5afc09 | -6.39972 | -53.33903 | 2025-07-27 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b4a381c-b6d9-3b87-a37b-4dda6f90a5a5 | -4.616 | -43.32005 | 2025-07-27 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aeb25eb-760d-3469-a126-b01a0172ea54 | -6.89437 | -52.86913 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7bb1747f-af75-32c5-a9f0-22d2543275c1 | -6.63372 | -58.85686 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e9859f58-49bd-3040-b59c-b7b7d2f8bb0b | -3.39733 | -47.49278 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c30a60e-ff2e-30e5-87f0-ec48a9c16662 | -8.51577 | -47.49027 | 2025-07-27 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 497c6a04-9be2-3b66-9e34-77013d657934 | -6.66162 | -58.85642 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 27342d63-b5b3-31cc-bc14-f2ec82b910ee | -6.61765 | -58.83419 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab821104-f40f-318d-8fd7-ef3bd96e3a95 | -6.86892 | -43.68914 | 2025-07-27 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6051a0a4-b9f3-33d9-925c-d32f03df143e | -7.3735 | -43.43121 | 2025-07-27 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ad1c05b-c578-31d3-b39c-f74d83abe2df | -10.51639 | -42.55529 | 2025-07-27 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6458a954-0eda-3e10-8960-44ca54d6e73d | -3.11933 | -48.96133 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a016d212-1496-3035-90fe-f47b2a0d1556 | -4.0701 | -42.53979 | 2025-07-27 04:57:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aceb8094-53d0-3c2d-b6d9-a9b0d45c6a1d | -8.8734 | -49.00579 | 2025-07-27 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ea7c05b-ff73-36d5-9f2d-b2cb0ba3305d | -6.6687 | -58.83758 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 349be300-f3ba-3d78-8aa4-d613a2055df5 | -3.42683 | -49.4805 | 2025-07-27 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30220b06-0544-3824-bef9-c5eced42e41c | -6.6455 | -58.83386 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3acfce41-59bd-3ce1-a4a6-c6e3bbef8d4e | -8.81825 | -46.73954 | 2025-07-27 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 697638df-eaba-37e7-be4b-5124ecdcd8e9 | -6.6679 | -58.84243 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57d5dcc3-03af-3c2b-848f-95c3192ccb05 | -6.4008 | -53.33197 | 2025-07-27 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddbf1c20-9a30-370b-a40e-51d9551fd24d | -4.10634 | -47.93407 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dcaea31b-3b27-375d-969b-382517c27635 | -8.0147 | -48.17842 | 2025-07-27 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54ad5eab-3836-3da6-91dd-be8aaa0d64c0 | -2.58163 | -51.92143 | 2025-07-27 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccf15ea8-aaba-38f6-bf6e-045b9f44101e | -6.6492 | -58.85941 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f056eb2-c76f-399f-89bf-377802e61267 | -6.64146 | -58.85814 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 53d36c1a-795a-3655-8b0d-17e7060ddb26 | -6.67803 | -58.82912 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98ed161e-fbe1-302c-a227-fbaed4a9ac6b | -8.3089 | -55.10099 | 2025-07-27 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2536685-9d04-3f9c-81ef-8f50b68c81da | -8.30539 | -45.00694 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f24d09f2-a8fc-3994-bd1c-2bcf1b61fe7a | -6.63677 | -58.86241 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b7c2688e-e764-3cee-a5d6-7f7efd2ecbca | -3.12529 | -47.01431 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8363eec-8ef0-3875-a689-7868a7c9708a | -8.29376 | -45.00922 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d773975-d58d-32fb-9d4f-4733adbe7460 | -6.63618 | -58.84215 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bafc5082-be25-398b-8e11-b29349404649 | -5.67507 | -42.79948 | 2025-07-27 04:57:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 19166c68-7b17-3f47-97e3-2778e1e07fdd | -3.39609 | -47.50118 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0032056d-7848-38ab-b104-f4b717120428 | -7.75458 | -51.13146 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1bc98aca-8bcd-3f49-a1ad-162213c75ab7 | -12.67785 | -46.99374 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa7ab6bd-06b0-3f30-a164-243b2d3a42bd | -11.9655 | -46.71192 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c96946f-338d-3373-8516-99989d84cf2b | -11.11003 | -45.1191 | 2025-07-27 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 317ca2a8-5ac1-3e00-9890-0ee7546f3088 | -14.96473 | -46.97293 | 2025-07-27 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a83d58ef-0a71-3a50-8e92-a80d95d88bec | -12.68699 | -47.02049 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c59fefa-08e9-3a21-ba4c-99e2c1e0d286 | -12.71035 | -46.28854 | 2025-07-27 04:59:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c29bafd-1105-3138-9e7c-00b732c42a3a | -12.68145 | -47.02287 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3aee4fe5-16c1-308f-9d6d-c6668bc92cde | -13.49306 | -45.5026 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 101b87d8-2fae-3813-9877-09edef2f38aa | -13.12529 | -47.36262 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47b792cb-5cfc-31fa-ba1a-d67fc1d10b0c | -8.97398 | -61.5082 | 2025-07-27 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9a467a6-d3ce-3413-a53b-152bb3cf5198 | -12.68011 | -47.01755 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 428f2e0e-00af-3c36-b417-cd47c9b12031 | -15.9594 | -49.15975 | 2025-07-27 04:59:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a060a78c-31e5-32f8-b219-632d5e9ad97f | -15.99467 | -42.65055 | 2025-07-27 04:59:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 7b9ae159-d305-3735-aa79-dece725f900a | -13.71695 | -45.67072 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1d41996-cb84-3bc7-8196-916b548e97c8 | -15.27152 | -43.08083 | 2025-07-27 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7632a6cb-63c0-3d03-9883-126c008a65f3 | -12.68044 | -46.98697 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c6fbd67-d24b-39d6-a86d-1922b8f800d9 | -13.12564 | -47.35981 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c090190-9ae3-35b7-bf1f-9b71b95f2dcd | -8.66507 | -63.85409 | 2025-07-27 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3a6f588-8cc7-3d38-904f-89cccb6dee13 | -12.71406 | -47.01368 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 69f960e1-2d9b-38c4-883a-934b0d229a7a | -13.09966 | -47.36115 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae7dc31-69df-32fa-a8c5-b44cf1edbb42 | -12.68734 | -47.01753 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f839b53b-0bba-38c0-9c12-b954eba9fd76 | -8.07468 | -63.85756 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d88186b-4178-3f83-b081-782b6b39ebfd | -10.85445 | -54.04394 | 2025-07-27 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72a8baee-e94e-347d-8860-b07f403be7e0 | -8.28953 | -62.89265 | 2025-07-27 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86d514c0-1986-3dc8-93f9-fbc5626ae5b5 | -13.49392 | -45.50344 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 46ed5336-1ecb-333a-ae2f-e7bbf2bbab7e | -15.03945 | -49.25497 | 2025-07-27 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5faaa5a7-78ea-3089-b864-37867c427aca | -11.30442 | -55.12352 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8b0b54d-ff55-3b8c-8704-9bbc475c0643 | -12.1725 | -60.73845 | 2025-07-27 04:59:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7c9d539-d0ef-32d0-be80-9ff3fc9aad9c | -13.13437 | -47.33062 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 193a4773-ac10-3e03-8a22-a356526773f7 | -12.71474 | -47.00805 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07e54357-60de-3bae-93d8-55c1a54017a9 | -13.08144 | -47.34081 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 225c0364-3c4c-3a58-bfa4-98cbf9cd0750 | -15.99 | -42.64945 | 2025-07-27 04:59:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d63c410d-546e-3d19-8d08-6f79e181ac22 | -13.13399 | -47.33376 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f23145f0-c882-39a0-97d5-c0bee49fc60f | -13.11951 | -47.36769 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22313fac-edaa-3788-8def-7404cddd8885 | -12.67972 | -46.99311 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49cefed7-e71f-3126-a0ef-ae3852d4111f | -13.12498 | -47.36515 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bcc3c17-8bdb-34bc-ae13-5d13c9972e82 | -10.28148 | -64.45593 | 2025-07-27 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee063dd4-c359-319f-bf8e-632d82d01f2e | -12.00713 | -45.83709 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b42b09aa-dfb3-3fb6-97a9-504ec639c158 | -12.71508 | -47.00523 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 393f247c-2236-312b-a3d8-5ced8def059f | -12.68566 | -47.01525 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d21e3432-42f5-3a46-93d5-5c62429100f7 | -11.97184 | -46.70332 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28503356-2159-3ee3-8bcb-bcba89ed3473 | -11.3022 | -55.11597 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03b4fd1e-34b0-32b1-b468-812c08bd8bc6 | -12.67973 | -47.02057 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8d9d1044-d954-3841-947d-dc8acfbe2879 | -10.85095 | -46.6862 | 2025-07-27 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6ca0ab3-7621-34da-9ffa-fb5eb2950172 | -9.46138 | -57.84905 | 2025-07-27 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1954377-370a-3de1-a604-f97b1f7a587f | -12.71542 | -47.00244 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ffa6bc8c-ec97-33a7-bdf3-2b16b93a3b7d | -13.09206 | -47.33852 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b185a62-4085-3df9-9693-c9e3b1d897fb | -16.18595 | -48.72275 | 2025-07-27 04:59:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a1f9db9-de1d-305c-afaf-2291b59fcfae | -10.16062 | -59.49641 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63086804-022f-325c-985b-3b26742a5edd | -8.59985 | -64.03477 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da515ae8-4f43-3e42-bfb2-1e6d5960ef32 | -10.04703 | -64.98795 | 2025-07-27 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24bc34a8-8d14-36bc-b66d-7e85334320a2 | -13.53774 | -45.53016 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8feb8922-3216-316d-b760-ca818ce24429 | -11.52486 | -54.68493 | 2025-07-27 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71ca5f93-5f90-381d-93fc-3e83a640506d | -12.04032 | -45.84177 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3d4935c4-943f-3ed9-8cd8-1367d6469d4d | -12.68491 | -47.02113 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da4f88be-ba03-3398-9a1a-9f3108bd6110 | -13.72131 | -45.68364 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
