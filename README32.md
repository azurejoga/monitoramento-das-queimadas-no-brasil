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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5790c198-ddd0-385f-b15a-64908a847436 | -14.4871 | -44.79264 | 2025-08-26 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 505f7406-05b3-37d4-b924-8083716e97c1 | -18.84156 | -47.01067 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff17c893-e3df-323e-821b-dfd84af071d6 | -14.34455 | -51.94398 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e83f862c-3412-372e-b64c-36bc33784c8e | -14.25475 | -48.03076 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a18e1b22-dc7b-37ae-8d0a-042784f5c4fe | -15.06798 | -48.54033 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a6c5b50-c065-3604-a125-ab56bdc9c0cb | -16.76387 | -49.33225 | 2025-08-26 03:57:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75c83892-2567-3240-a443-623e611839e2 | -14.36349 | -51.91413 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe3ae242-2298-36a6-80f9-70b94dc182d9 | -15.11528 | -48.67527 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8d03549-7cc8-32fb-a933-451f23eb72a8 | -19.03587 | -46.91573 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f08e4c47-a7f6-3ffc-bf71-42fa9fdde118 | -20.04997 | -44.4703 | 2025-08-26 03:57:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b92a9a73-2691-3b98-a5d2-a36bc39eb74e | -15.08762 | -48.5684 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 905c9371-44f5-3437-bc90-ab803ee0c647 | -15.02727 | -48.16056 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c2bc334-0bf0-3ec2-8b7c-494ed0dc19de | -20.98402 | -42.99347 | 2025-08-26 03:57:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9008c90-b441-3eb9-8637-53856e6cd9d7 | -17.81561 | -42.83071 | 2025-08-26 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4f22b54-e06d-3408-a620-8acde01ba76f | -13.41703 | -46.88028 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f4845f1-90c1-341f-bffe-9d19793dc012 | -13.41784 | -46.87588 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2debc48d-9cb6-338d-8a94-4f02c9af1821 | -13.44471 | -47.00703 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d784412-a3a5-3520-a634-9dbc82e2d33e | -17.60781 | -46.69178 | 2025-08-26 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e333c762-881e-344e-a934-1a53e81e2944 | -15.63177 | -52.72156 | 2025-08-26 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b537faa-db4e-3697-af65-ed51db810381 | -12.4414 | -48.71351 | 2025-08-26 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf26c840-ec04-3a4e-92a3-0d27253b04a5 | -13.77649 | -42.70304 | 2025-08-26 03:57:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 91540c95-3438-327b-95bb-93102f56b7b9 | -11.5475 | -52.13652 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e625988a-71b6-31e1-be0a-a583875f6509 | -17.5661 | -49.75686 | 2025-08-26 03:57:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1bfe2b8-ea4f-3e77-bca1-01e596e80717 | -11.50784 | -52.134 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7826ad77-677a-3515-9304-26cc6d6d6e2a | -14.39574 | -51.94093 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65b12254-ba2f-30c8-ac42-684ff3cb3669 | -14.80318 | -48.96928 | 2025-08-26 03:57:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2778644-feec-34b5-b050-17380cf1195a | -12.93191 | -46.31321 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edee36fe-4ba6-3cf6-9eaa-7020b47a7df1 | -18.89221 | -44.70023 | 2025-08-26 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f9b9fbf-90dd-3d06-8c01-c8e018bf0fe6 | -19.45465 | -45.30576 | 2025-08-26 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 929de276-f757-3afb-afa4-47005d3b0af4 | -20.20617 | -47.01221 | 2025-08-26 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| da9de83a-af6a-3ab7-a86d-65d9fa821e8f | -13.83645 | -46.696 | 2025-08-26 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26c3d7dd-85aa-3331-bcd9-4ac3d1665d58 | -14.71841 | -45.38608 | 2025-08-26 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4691e60-f092-3586-a62a-a7427163073b | -13.44654 | -47.02256 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44f34e2f-8638-39c6-99c8-ebd378a46de7 | -15.02623 | -48.16595 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64f991c3-b25e-3bd9-a88c-c552683f6941 | -17.6071 | -46.69565 | 2025-08-26 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd55c096-eda9-3594-ae23-4a3abd0f2e60 | -12.93282 | -46.3083 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5df5d26c-cd60-3a24-a3df-8518e579c21d | -14.71933 | -45.38084 | 2025-08-26 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9b842af-6bd9-3fa7-817e-4ae65e2a3fce | -13.41179 | -46.88369 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 84a9b0c5-85ab-3a6b-9f02-5bcd41a976c7 | -20.20222 | -47.01121 | 2025-08-26 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3ad6bb8-21e7-30c4-9cdb-ac02e4d2813b | -11.55725 | -52.12142 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76715e1c-b3c9-3be6-88ca-97248cac76f4 | -12.73249 | -48.16063 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d8cbd65-d7bc-303f-89be-cf61c3a9b136 | -14.30005 | -43.91175 | 2025-08-26 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d475360-ef61-3f0d-8b77-5cfac6bc93ab | -15.086 | -48.55076 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2e021c8-6abd-36e3-8064-6a4bb4a96cb7 | -14.77401 | -47.92844 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5731dab4-4ea6-3e74-8ecf-e7a046f06a7c | -15.95196 | -46.89283 | 2025-08-26 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83214951-a1e7-3065-a962-2556babf2037 | -18.85376 | -47.01338 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3497fd18-abec-3a9b-aac3-b41caf301631 | -18.7346 | -46.90833 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91ddf358-9cdd-37ff-a3b5-9603c8e3a72c | -18.89052 | -44.7015 | 2025-08-26 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b963c84-d904-33e5-8fd2-3b28d806a99a | -19.98594 | -42.21579 | 2025-08-26 03:57:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f0440feb-efe6-3a23-934d-ca8c27112506 | -20.25441 | -41.85253 | 2025-08-26 03:57:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3fe2e205-abe8-33cc-b9b4-bd34ceffd131 | -18.75627 | -45.36579 | 2025-08-26 03:57:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 440eca50-9060-3e4c-a577-c7c83367631f | -13.1649 | -45.28888 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f3e3accf-4dbc-3d09-af1d-2cbed5cc2c7b | -17.68569 | -46.31349 | 2025-08-26 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 82675db1-2d36-3200-b894-d4a4541c2363 | -14.11878 | -53.98373 | 2025-08-26 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdd8af0d-7f30-382a-bbf0-524bd921f92f | -12.94585 | -46.33466 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f81aba93-f390-3933-b2bb-ce04bd938830 | -19.48708 | -46.12134 | 2025-08-26 03:57:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d252e5e9-9089-3f89-a3f3-704cf642b280 | -14.34918 | -51.94777 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b0682943-2ab9-3967-b669-feb66ec56bf8 | -18.84234 | -47.00654 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 937c1c16-0e93-35b0-a980-4852a47973e3 | -12.75997 | -48.14969 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac316202-d530-3b28-b1cf-0f44c9e3eaa0 | -13.82769 | -46.69447 | 2025-08-26 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95e36a9b-e092-3d1d-9cc8-ca4a6357226f | -13.16894 | -45.28959 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a1c70ab1-6d3f-3f4c-8150-ea138108d95b | -14.24225 | -53.05179 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30242fdb-618c-32b1-ab7a-24426b23b645 | -17.20847 | -47.21995 | 2025-08-26 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f2e4191-2ebc-3afd-9960-c06bf1fbee7c | -13.45179 | -46.99356 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2448052c-4ccd-36f2-8c8d-301773e3a918 | -11.54863 | -52.13094 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2362eb71-8109-3d8c-87e8-3ae6c8fe928d | -13.59171 | -48.18994 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9fef88f1-b12a-3638-bbd2-571523e95236 | -17.35233 | -47.85506 | 2025-08-26 03:57:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9c81176-980e-35af-8dc3-30686cdfbdd4 | -12.93105 | -46.30959 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f79e425e-d777-34de-8cb3-a1920532d92b | -17.65631 | -46.97144 | 2025-08-26 03:57:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6f3e755-3134-392f-b4ee-c929e57d6ed4 | -15.06398 | -48.69146 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78f35264-bc03-3360-ae92-d6fb8add42ca | -13.59064 | -48.19549 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4216a55c-34f3-3f13-b47d-1ef8679e4cbb | -13.44729 | -46.99283 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76718672-9674-3382-aa0d-584d8efabfd0 | -12.6556 | -47.86034 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b3eae62-e714-3b1f-b9dd-e74053d3d97f | -18.8094 | -47.59332 | 2025-08-26 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52b2b759-6bc4-3844-a0a9-ccbfe470ca86 | -18.52654 | -46.28955 | 2025-08-26 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19b7a42a-2025-3668-864d-c0d964a1be72 | -13.4515 | -47.00629 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f699d12-38f1-3923-8310-1537ceb26ba7 | -16.74275 | -47.59659 | 2025-08-26 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12410af5-f3ef-3934-8fbd-425f99620812 | -13.48665 | -46.86861 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c421d1d0-63a6-3441-8a46-2906cda57d5e | -14.11078 | -53.98483 | 2025-08-26 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d11dbc6-4177-3f4a-918c-4f13fd131678 | -13.51979 | -46.91325 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe4248ba-a02b-398d-a403-2a55066873d9 | -18.09978 | -42.5762 | 2025-08-26 03:57:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 08a72de6-1418-36ac-83ea-608037536628 | -16.05043 | -45.75027 | 2025-08-26 03:57:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dba81b4-c5a7-3b47-874a-360d127bf265 | -19.1275 | -46.45193 | 2025-08-26 03:57:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c3c9bed-8cb7-31c1-8839-fa14a3e0f0c7 | -13.06114 | -46.32475 | 2025-08-26 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7b02bd9-6b28-3e84-8daf-5957cac93ec5 | -14.84682 | -47.1512 | 2025-08-26 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e04fd3a-59cb-33b6-94b8-d2c75571072c | -12.75104 | -48.17011 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e64f4f96-bd9a-362c-bc0c-50b6087f02e5 | -19.4909 | -46.12216 | 2025-08-26 03:57:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4a533e4f-380e-34a5-8287-2cc841efd85a | -15.02639 | -48.50233 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a5f1637-0c72-358c-9da5-b69847121778 | -13.51624 | -46.90753 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2950eb4-0d48-3eda-bb22-08eeb9ff7d24 | -13.8201 | -45.8897 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 20733c1d-e64c-3298-adb4-07aca50455c9 | -13.52514 | -46.90924 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90c0c8f6-cc03-3b89-b8e4-4ec7eda41dd9 | -11.53688 | -52.12292 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da75e9db-a471-3c9e-bf83-312944237128 | -13.83646 | -46.69878 | 2025-08-26 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1973191d-03ba-3263-a7ae-044869062db3 | -13.44613 | -47.01007 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 921e5751-4fa1-3d48-a103-83dc56da31ea | -13.47887 | -47.00894 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 375fb81e-55de-3b3b-a1c4-be255465fd4e | -20.42072 | -42.93839 | 2025-08-26 03:57:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0b07c46-c637-3807-99b5-621ab9ed3ead | -17.20771 | -47.22404 | 2025-08-26 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77a365dc-2bbb-352a-b7d6-78e0e009ccfa | -14.64204 | -49.07829 | 2025-08-26 03:57:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfc660f3-d8e7-37b3-8884-859ac30dbbe5 | -13.52248 | -46.89869 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0661dbb0-b1ce-309b-80e0-0d40fd540f8e | -12.93623 | -46.30556 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README33.md)
