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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70208ace-71d4-372a-b749-c96d50b39fb8 | -11.55534 | -46.33558 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 420edff6-09ed-3349-9a6d-ea9ce85bb9db | -13.48606 | -46.85254 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a914fe3b-fbe2-31ca-827e-1e815021ec9c | -13.44405 | -46.96422 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9220b234-3983-325e-a6c5-cf77c3b34d48 | -9.05246 | -54.95063 | 2025-08-28 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d59f5fd6-8f6d-3f77-a3f7-8f1ea1b4ce78 | -13.38026 | -51.7561 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbfd02cd-34cf-3e5a-b84b-5e15051825ec | -8.28624 | -45.17026 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d5d56f72-5c8b-313e-8b04-d5dd69e9ee6f | -12.81035 | -48.12605 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab3fd965-615c-3e07-9c57-a123fb16d35b | -11.60952 | -47.3 | 2025-08-28 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a93a65f-fcab-3497-8fdd-4b6f4f99fb4f | -13.44774 | -46.96499 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa260d6d-3702-36c9-b937-ebd2faec4d2e | -10.32608 | -46.77611 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 3f651634-068e-3cef-bc05-1d24f6038a68 | -13.98111 | -46.34796 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24ce18e2-be4e-3b39-8e78-c86f38d8d6c9 | -11.32518 | -43.53145 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69a77c2a-7314-32d7-b466-e5d0073dcb3c | -10.53008 | -46.69385 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 6bfe60b7-46cb-384a-9e06-60da14e08848 | -11.65277 | -44.86781 | 2025-08-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d37844-953d-305f-8363-b5c3ee676c5d | -11.22262 | -55.06847 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f14d1c4f-5dc5-3930-845d-3ae7b8356651 | -11.55609 | -46.3312 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 776ea2a1-0028-3eab-bf78-3c7bddd75e4c | -7.24097 | -45.43486 | 2025-08-28 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 433fbeea-5dc8-3dd9-aad8-43ea99009f0c | -7.66917 | -44.75821 | 2025-08-28 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f7cf2cb-cf20-396b-a49c-5266561a9c16 | -8.45483 | -43.65192 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab956ee9-440a-3ffb-bb2d-8c23785e4a05 | -11.34013 | -43.54485 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5914961-c869-3cc7-8ad5-79671f0290e1 | -8.08403 | -44.98962 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71e6b0b2-54d4-37fd-9012-2fbbddcd53c9 | -8.43719 | -41.45208 | 2025-08-28 04:08:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| a346f841-59f6-3d9c-8dd5-3bdf6c6191d6 | -12.78656 | -48.16687 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c07db6f-3def-30fb-83fb-2bf527f465e3 | -13.60322 | -48.14686 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be0be241-80aa-3c5b-b5c5-239c035d5761 | -8.29773 | -45.16795 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83141c00-137f-30c2-8ab6-bcd71ad89388 | -13.44031 | -46.85355 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f582e1a2-00ff-3c9e-bf09-f6068ced6b5a | -11.33517 | -43.5331 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a8036cf-00b4-34ce-a89b-b2d285cff57a | -11.54786 | -46.35703 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f546e5d5-3c62-306c-b1ae-e338b9dd6ddf | -13.63491 | -48.22132 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3756da9-8f37-3965-bed0-43c0cb80da45 | -11.3329 | -43.5473 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bccb401-1653-3913-8b08-38cb8e2d8f85 | -9.44556 | -49.45225 | 2025-08-28 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c77212ba-6c9c-3a41-86b7-ef34e98d4238 | -9.67694 | -47.06833 | 2025-08-28 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a8bd5bd0-634f-36fe-93ef-9a55970b6ab5 | -10.53711 | -46.67568 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74f5d712-e10b-30af-b25b-7452b145f4a9 | -8.44628 | -43.6618 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a9f77a7-bd68-3c79-84b1-6e7b01d354e0 | -11.33184 | -43.53255 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08bd5afd-194d-3346-ac9e-36076e86c13b | -12.78257 | -48.16595 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88843c82-c898-3b39-9901-83bfd1ecbabd | -12.95481 | -46.33959 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a5a4b9a-2340-3870-b9d3-e13ec098727b | -13.59681 | -48.21722 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a18a477-e278-30b6-bda8-18f9c0326de7 | -11.23763 | -55.0605 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 316f1c4d-2ec8-36e7-93ed-77a7f319a023 | -11.32072 | -43.538 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c44fc74-1a8e-3ca6-b33c-865b82c43a85 | -7.94259 | -42.62859 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97cf637e-da29-3b57-9994-1f856efeb206 | -8.29038 | -45.14533 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a91e36a8-3ad9-32ac-9845-cd8ff2a56286 | -8.48031 | -43.64475 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 042fe0ff-47e2-3660-92a4-6a8bc8cfe8c2 | -13.97326 | -46.35086 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28e4fc0b-6b09-35d4-9db2-926d9304e96a | -11.33956 | -43.5484 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a580f83c-5589-35a2-a5e8-cfe65c6e4b70 | -13.18377 | -45.28577 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e0379124-fdc0-33b2-84d2-27859d3f7cea | -13.38951 | -51.75549 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96d2809b-25b8-3d8e-9e60-985385250c48 | -12.68931 | -44.4067 | 2025-08-28 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a7a6d28-ba8d-3c01-ba39-2c00ce9079ad | -10.52682 | -46.71283 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ffbaab6-6417-3bd1-9231-595587fa3d62 | -8.46897 | -43.65044 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ad29241-9849-3918-bf15-f785c9880447 | -13.42758 | -46.97104 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fccc782a-3e43-3d72-a4ae-7fc1f5525fdb | -13.48239 | -46.85179 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce8831cf-8dab-306b-9c42-8cfc4b4f6d5f | -14.1366 | -45.40174 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a99c24ed-30c1-39e6-902a-fe7d5c47ae35 | -12.0635 | -46.63361 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b5afaab-c50f-3c7d-a14c-583bca856b4c | -7.2336 | -45.43336 | 2025-08-28 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18b98ee2-70a8-3ad0-abe5-4d5ead5af38d | -11.79368 | -46.80159 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad6cb7ad-e4ae-3295-bbb6-bb8a4cb5a4d6 | -13.39869 | -46.87406 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c85eac6a-0f3e-3eeb-a4cc-091cc4ce7100 | -13.59619 | -48.22076 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fa447a2-4cc1-3cc0-b3bc-5ac5c946701b | -13.52051 | -46.93138 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2a609bc-8fd7-32a5-bb1d-ca439082592e | -13.5988 | -48.21646 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 495cbf1b-29dd-336e-a908-9e7810f55b19 | -8.2991 | -45.15969 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4506c418-d0b7-3c35-baa0-039ae4f4bd13 | -10.52463 | -46.70273 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96130d94-cb9c-3e24-8eaf-9efa981cf8f0 | -14.12783 | -45.41203 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34f2db90-136a-35df-ba35-e4ffccd1621f | -8.27112 | -45.17199 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e0c1584b-5fc0-3a71-9086-48a5c94cec7e | -7.76395 | -44.06521 | 2025-08-28 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe7eb98f-0e6c-39a6-b32d-eba133f25eb2 | -13.49707 | -46.85478 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ac4508f-0445-32cb-b386-9df136537142 | -11.80626 | -46.81839 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1b65b7d-1c80-350e-8103-4116d11cdebf | -12.71986 | -48.18819 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4797e65d-6496-3422-aa36-71eba7d660a1 | -8.24217 | -45.07019 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1fc903d4-7468-3c38-b19c-2d6a9ec9f7c7 | -12.02929 | -47.20772 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43f5633f-8dba-3b03-bf67-35187d676b66 | -11.15021 | -44.80464 | 2025-08-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3429884-2030-3e08-b9d4-2a4d48c0a14e | -7.73966 | -50.2734 | 2025-08-28 04:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9928052-e3b9-37f7-ac81-d7ee6b11f8d9 | -11.3445 | -43.53447 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1bb3307e-7e8b-377e-af91-69ce96e3e8e2 | -13.46766 | -46.84909 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce69d16f-dc75-3622-8cc1-2c5885910f07 | -12.92766 | -46.31816 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61978594-c435-3a82-8662-a529f35f22c9 | -7.23198 | -45.43011 | 2025-08-28 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72aac959-cd16-39ff-bea9-7478cdfbda7d | -7.93927 | -42.62806 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5720d81-a143-3352-b190-f14be79d5d23 | -10.60504 | -55.40619 | 2025-08-28 04:08:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ead5a59-406a-3dea-9cc5-f8d042bd3822 | -11.65437 | -46.39305 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a80f776-535f-37c7-bd99-52be61a209e4 | -9.45194 | -51.95092 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d1f0c156-b955-30fd-bcf4-e425d2f76911 | -9.66982 | -48.31868 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9af05962-132b-3917-980f-a221652f4063 | -11.34507 | -43.53092 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 94a59648-66fb-3436-8df5-33848cb98ec6 | -11.22566 | -55.05116 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e5f8a22b-cba5-3521-8a4f-342e270f2cea | -12.40978 | -47.79063 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b63fda95-06af-3611-be2e-d9dcc6d24d38 | -8.20128 | -45.07207 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d414aee-16af-3923-afca-16f3e5e838a6 | -9.50072 | -46.70349 | 2025-08-28 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65e846b3-d91a-37d4-9b36-ff53c432f5f9 | -8.28772 | -47.21403 | 2025-08-28 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f2342d1-1c69-3f79-88e7-561c03edefb5 | -11.57017 | -47.61676 | 2025-08-28 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d15e40c-11c5-34ac-adb6-40338aa3bd57 | -7.68055 | -45.00023 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e0ab801-e27c-3526-97c7-c3e2d107b15b | -12.95967 | -44.57947 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a626c9d3-dfb3-316b-9256-0e328da3444a | -12.81578 | -48.14225 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7304a6bc-a3e4-33d2-bdfe-80c70d1bc598 | -12.78196 | -48.16938 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62326dfb-4f06-37cc-b25f-cee238f61588 | -11.33574 | -43.52954 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 423a8d0e-eaf2-3bb6-ac7c-1eaeedccf675 | -12.67284 | -48.1718 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 483972bc-296d-3829-9e4d-7af0e2cc8756 | -12.72248 | -48.17314 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 23c862c3-36a1-3557-a1ac-09ea12d6c713 | -13.9861 | -46.34021 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9421a2de-ec85-3344-b9d8-d2bb08a1a348 | -11.33567 | -43.5514 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbfb7446-1186-3174-9b22-64f3e4cb43af | -12.6837 | -48.18092 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 103c5c76-15cb-3ef7-af0d-495c9dabc820 | -11.23017 | -55.06427 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a272e124-f76e-3cd0-b502-0f288616e0df | -14.54494 | -48.18317 | 2025-08-28 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
