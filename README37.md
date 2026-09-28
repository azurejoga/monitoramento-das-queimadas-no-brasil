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
| 93e2ccc3-236e-35d8-a998-345106c363bb | -12.70703 | -46.99043 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55ad3d74-4142-36ab-9f3a-deeb761c6a4b | -11.90626 | -47.00496 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48881ea2-dcad-3ebd-bc21-7b62df7c17e2 | -6.00238 | -47.39073 | 2026-09-28 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2b1d7e23-b088-3744-bddf-7ae04bbad50b | -12.09561 | -50.29794 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8112f550-5923-3e6d-85c6-580e0d8ebd94 | -8.25505 | -45.40691 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cd28b49d-e5a3-3754-af8c-9f98a1c3c53c | -11.72359 | -50.66534 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dadbe021-10a3-30fa-9797-3ec70d66d934 | -11.37759 | -47.42723 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03a957e5-916e-3ec0-9a61-ab6dcaffaf59 | -9.97402 | -45.33809 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b90af92-647c-38d1-80bc-d60bdd6ed6a7 | -13.33366 | -46.80946 | 2026-09-28 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 469e3c8d-4a5c-3894-b83a-3848b3311e2a | -12.14709 | -50.35764 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6b2c9043-d39f-3945-940d-7dec8d940406 | -8.22813 | -45.44089 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09b56e09-8935-3a1f-bb44-d7cca9304298 | -8.4477 | -44.67023 | 2026-09-28 04:34:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75e0f7bd-0cc4-3693-978a-8b221e82fa79 | -8.23232 | -45.41217 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba301305-8c8b-3b3e-9a0b-2288b2393af4 | -7.82036 | -55.13882 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9813a86-952a-3d8f-96d0-be5b9972a861 | -10.22618 | -49.98444 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52737209-8df8-3c5f-ba09-ab1350e1d32d | -11.72023 | -50.66479 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6bbf2d7-1b24-32f8-9145-60f91db942a2 | -13.10611 | -47.42173 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bda66d2a-b0d8-3a72-8dbc-762530aef79a | -11.63199 | -46.77492 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42058f3f-f944-3a5a-b41d-482e4c439233 | -12.65856 | -47.32053 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf1340aa-40ed-352a-880e-551f48a73edf | -10.22392 | -49.99869 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa61c9c0-4db2-3226-8065-5c6a96b6fe1a | -10.14274 | -43.90627 | 2026-09-28 04:34:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfdeb58f-43e5-3431-b812-13064a855022 | -5.74378 | -47.38919 | 2026-09-28 04:34:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53e49704-dc0f-30b2-bafe-c51eb8ac08f9 | -7.82114 | -55.13424 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e51d230-aab0-3f42-b58d-432651b4cd85 | -10.89108 | -50.68223 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94110ba1-2e0f-3329-94ca-b33760d0bf4d | -10.92237 | -50.69087 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70dd2e43-ee06-3129-95cb-0bed732fd38a | -11.17359 | -45.13515 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31c2e336-03f5-3b82-91df-5d231ef75767 | -6.65171 | -55.10363 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ffd69ee-54e8-302c-9471-1abc05030bc3 | -6.76593 | -45.3721 | 2026-09-28 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d487b61-62f0-39fd-8dbd-523501d30ed2 | -11.71093 | -44.51738 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06dcc326-f982-369a-8db1-5db541989acf | -11.4418 | -44.93103 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d74cc9d3-c95a-3eb7-b688-e736a4afbf12 | -11.62678 | -46.7862 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26d55798-8c67-3c6c-b8b5-9e78b6a12f97 | -8.65566 | -45.42057 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03aff155-f67e-3814-859c-abb2d795f111 | -10.21334 | -50.00064 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6091e76e-0538-36d8-bfa0-670f836ddfe3 | -9.98703 | -50.16206 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4891a9dd-5aef-31af-b853-dcc2d9f05b3e | -11.13618 | -50.0601 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be84b25d-3b99-3370-aa4c-3bdca0713b77 | -7.71134 | -54.77156 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffebb055-7476-3944-b1a9-04173182f23b | -13.08316 | -47.43409 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f6853d9-abca-3774-bc93-b8f05fa27273 | -11.17051 | -45.12985 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c6f3bfd-a4cf-3533-a151-49810ae70704 | -9.07288 | -49.87103 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96cc8f74-81e3-305b-b81a-c116998562da | -10.40988 | -53.81697 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbe90960-2c12-38e8-9a99-6903a7f46faf | -7.93939 | -45.4631 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab042a70-9bc6-3fe8-8619-24600371b365 | -6.65972 | -55.11245 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d463374c-57dc-3eab-ad0c-e6745803a3dd | -10.88391 | -43.68909 | 2026-09-28 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2cc626c1-6e10-3848-9be3-f3f6955e0edd | -9.98425 | -50.15792 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 328f3ca4-dc06-351d-b2e4-d53b53d7c192 | -11.49304 | -47.38285 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c976479f-9624-3b82-90c5-d2c6de44ea9e | -11.37934 | -43.40736 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b0665a-16d7-3dac-a1bb-3d0d36994690 | -8.23711 | -45.47926 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa2d916f-977a-3d50-867f-e930cb8ff1b7 | -9.08846 | -49.88086 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 136af3e3-4601-3606-8aaf-80bf74b907a5 | -8.35479 | -45.44119 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 909532a2-0762-35c9-8c4d-6f567d9cc68f | -10.21448 | -49.99351 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f3b8d54-be59-3e48-9aca-6f66af57544c | -9.65776 | -49.14569 | 2026-09-28 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1988f05b-1769-30e2-87c7-dce7df7256f3 | -10.20894 | -49.98531 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 266492f1-a7c2-38cf-9efb-97f240dea0b1 | -8.25205 | -45.40244 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1055653-cbd5-3a05-abc1-7835bf3598bc | -12.31145 | -46.40681 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31f2882b-be88-36ab-a5fc-94e5fb8eaa3e | -6.94916 | -41.60819 | 2026-09-28 04:34:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45b3c0ea-2a2b-30f9-ba5f-5cfff1b282c1 | -8.45013 | -44.67995 | 2026-09-28 04:34:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dcf570a6-340e-3039-b545-5b48c042a4dc | -10.21284 | -49.98228 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06a7603d-f152-3f91-8f11-ac963568a658 | -6.59868 | -47.16251 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 366afe48-e20c-3d63-99c7-eb7b7b71681a | -13.07901 | -47.41461 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de2d4b8b-8b24-35ad-b9c5-1856328c96bf | -9.32912 | -45.37767 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61120806-9580-3633-9c92-c2ebc2413340 | -9.08014 | -49.86854 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52dcc7b0-47f7-3970-ab7f-8ceeeb534a54 | -8.96624 | -44.15011 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8bc5803-d80b-389c-ac6c-778bff13e585 | -10.2061 | -50.00313 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80a6f18b-b6b5-33ab-9fa5-71fd2e9328fe | -12.7211 | -47.27916 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e47e187a-2648-3250-82c8-4445e7d6dbfd | -11.13675 | -50.05655 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8336a316-75d1-39b4-b615-c00718e0519c | -6.60146 | -47.16653 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c519890c-fa4e-3189-b65c-c3fb19080990 | -7.2832 | -44.31435 | 2026-09-28 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08c23d04-fdda-3457-b494-ce2ee9425818 | -12.71051 | -46.99106 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e320153-6e17-37e0-b9dd-6e065b930d5a | -12.63791 | -47.31732 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b19f309-4fa9-38df-b685-390e913125f3 | -8.27849 | -54.71315 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4deee0ba-3a45-30ab-adfe-c2ebceeaf91f | -10.82012 | -57.22645 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d89f28f4-7024-3f80-9743-04eeef80b1e9 | -6.41882 | -45.85828 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea04ec45-cfc1-3fd0-bb89-1b1ea0e75da0 | -12.69539 | -46.9724 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f722ad3a-e4fb-39c6-9685-93e1c0c9cf98 | -10.42086 | -53.82416 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f82dde7c-b173-3098-9c72-7dde6846368a | -11.10847 | -51.34111 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1dfed2a5-26d4-3185-a98a-f1b5a105372c | -9.85193 | -44.93918 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d360eb64-b23f-306c-a076-7ca75d606bca | -9.32368 | -45.36383 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3213213f-570b-322c-9012-915279e2e6d4 | -9.98653 | -50.14353 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19fe4e6d-b224-3e55-a909-37efcb4078af | -9.9764 | -50.16403 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6312e3f0-2a98-3971-a3c7-d8b4b08a412a | -13.56348 | -46.36636 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 19051d65-f693-343d-9ba0-46c38e3a8030 | -12.875 | -44.78273 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74a6967d-eb23-30a2-9209-b5558aba9d69 | -11.38945 | -45.3903 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fb66361-cc64-30dd-b1f4-b2ac3ca9be3d | -7.71581 | -54.77093 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f94c7b6-75c3-39d9-8526-625120d1ee02 | -10.22115 | -49.99459 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aaafdbf-c225-30ef-9e51-9c015f9e3e92 | -12.71363 | -47.28193 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e1bf022-30f1-3383-8670-98caabc79b69 | -9.15558 | -46.75107 | 2026-09-28 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9facfc0-597a-336c-a1c4-d6f23b746c17 | -7.37909 | -42.12771 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0a03d9d9-b906-3c23-a776-256d846a3b7c | -9.17155 | -61.40372 | 2026-09-28 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 94d55668-6b13-3e2a-b8d6-5f57c740dddd | -11.18598 | -44.80361 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 7794dbe7-363e-3783-9ed2-2cda09c07b2d | -7.56114 | -47.00264 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33f15635-8e22-31e8-a3a0-d89ee9bfb602 | -11.7105 | -44.54856 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 007c0ec9-4d5c-3514-b4df-635d5ddf5a05 | -7.10353 | -45.65084 | 2026-09-28 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dc17224-950c-3680-8195-430e08b25311 | -9.85439 | -44.94868 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a849db70-488a-3c6b-bb67-4d1dedbedc08 | -8.36129 | -45.4468 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12d949e6-65ba-3e56-b978-c9938728f81e | -7.3931 | -42.63117 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34d4f405-8502-31b4-842b-824c94f2d31b | -11.8652 | -47.09765 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8f7a434-68f1-38be-bafc-a1f414f69245 | -10.11982 | -43.95293 | 2026-09-28 04:34:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c7229f9-5e72-32d9-830e-92a3a02311e1 | -11.38668 | -43.41647 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b3557e5-e6f4-3394-be19-656307855421 | -6.6471 | -55.10301 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fdd97488-f6b4-3e48-8eb8-9c07dfd61eb8 | -12.83732 | -43.39642 | 2026-09-28 04:34:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README38.md)
