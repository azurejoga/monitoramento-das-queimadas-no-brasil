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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e80ecdc-8cf1-3fae-831f-bd961678c869 | -3.89138 | -48.36363 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 999ac16d-2190-32c2-8945-b0fe9b38dc40 | -3.81211 | -48.97583 | 2024-10-11 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa7e65a3-61e2-3af3-98de-c5aadc3cdaea | -3.8073 | -47.79351 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46e85a8e-c775-3d13-a8e7-f252e9bb18ed | -3.80444 | -47.7892 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2971c50-85dc-3848-810e-6582503e6a46 | -3.80385 | -47.79296 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 255bc820-e956-3a22-93c7-16f8faffc30f | -4.10744 | -48.25912 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 496315b1-9d00-3fa7-b88e-587d483f95f6 | -4.10681 | -48.26307 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7612841-60e7-3c92-8765-389f2620f027 | -4.10669 | -48.48973 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d3a2f31-3374-3c66-8a71-8f080a5ff098 | -4.10645 | -48.24294 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| de245467-4e8b-3c47-895d-d5db737061bc | -4.10618 | -48.26701 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c60fead-d48a-3000-b313-90077876c524 | -4.10583 | -48.24682 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| fa1ffea0-7d5e-3629-be3b-8f20a0308d23 | -4.10554 | -48.27096 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c696dcb9-e8b7-3755-8545-31b6affad5a2 | -4.1052 | -48.25071 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2c2495b1-497b-31c5-aef3-1989c6afe8c5 | -4.10491 | -48.27489 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb5aaa63-bf7a-391e-8f3e-03da7532b12e | -4.10457 | -48.25462 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d665ef77-0983-3b02-82d0-d86841bc1878 | -4.10394 | -48.25856 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 10b536ea-8e17-3609-8340-466db6deaaec | -4.10331 | -48.26251 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52b25f83-4400-3e3e-995e-a5ffaf571e18 | -4.10315 | -48.48918 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39284a04-b79f-3f29-9bf6-fda0c1cc83bd | -4.10295 | -48.24241 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c61ee902-1757-3cdf-993c-1969a37c5eac | -4.10268 | -48.26644 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 817a4cec-8d99-3f71-8a82-72bb3f1de79e | -4.10232 | -48.24628 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| fde974b7-fc80-3555-9bc6-89b373cdbbb5 | -4.10204 | -48.27037 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 035b6026-703b-3d67-88af-daf3f26db09d | -4.1017 | -48.25018 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| af9eb7eb-e584-3793-b66c-465e2edecdf3 | -4.10142 | -48.27428 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f707eb6-95b3-331e-a9a1-c2c54fa8156d | -4.10107 | -48.25406 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d69cc68-628f-3f9a-addb-cd36548e46ac | -4.10044 | -48.25799 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a761720-1d3e-38c2-8e47-4bd3fce5d3ea | -4.09981 | -48.26192 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb89b99a-7a86-33c3-9861-34876e1334b5 | -4.09918 | -48.26584 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8bf1f4-cd62-3bc0-a39b-ccbeb588ee20 | -4.09882 | -48.24578 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 312892c2-16bc-351f-b551-75af71b65365 | -4.09855 | -48.26975 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d36dd781-2d54-33c9-87ed-52ab85398437 | -4.09819 | -48.24964 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 674230e1-b736-3cdd-ab80-b45a9f1b29f7 | -4.09792 | -48.27366 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6456075c-3b6d-3065-af4a-f662f5e14ad4 | -4.09757 | -48.25351 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d7dcdbf-5aa1-3f1c-a8a0-0f1b58571436 | -4.09694 | -48.25741 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77ae884b-31c0-3764-b9ca-5f606977df27 | -4.09631 | -48.26133 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9066bc9-c93d-3a38-8fa1-5fa727550109 | -4.09531 | -48.24525 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8903b0d4-7c89-36a8-bed6-786e4238a43e | -4.09505 | -48.26915 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dbb2cba-3a0e-3b94-9de9-895a7ea64a63 | -4.09469 | -48.2491 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c3718e1e-fb74-3c6a-85e0-e2c731f671fb | -4.09407 | -48.25295 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f424dbb5-8b86-3b8d-8d49-fa1cbdd6e2c4 | -4.09119 | -48.24856 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c00ce867-fa99-3d4a-a269-55d8ae2d5da1 | -4.08615 | -48.27979 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5682f24-9f79-3116-bbce-2bbf515a8b1f | -4.08264 | -48.27925 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c80e227-afc9-323a-825d-d6712a26861d | -4.08069 | -48.24685 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f30b1850-91df-390a-88c0-5ccf7a4c97a6 | -4.07593 | -48.25406 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 402a3d0b-2d52-3b29-8326-9d61230e5170 | -3.95578 | -47.95996 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db8b9e91-27ba-33cb-a930-d703da06b082 | -3.95231 | -47.95943 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa951889-fe00-3fb1-b7e3-07f9f9a37741 | -3.91695 | -48.33921 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1c820ee5-0b00-33de-9793-4eaa608cb641 | -3.91632 | -48.34319 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e82b4509-9fa3-351c-9b70-ef8efff0b566 | -3.91569 | -48.34717 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d354b2a0-5904-3d19-897e-8e3c9e9dd599 | -3.91506 | -48.35114 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| be6b733c-ed6c-3ba9-962b-88ac0f9cdc82 | -3.91443 | -48.35511 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 233cf981-226b-36ee-a328-66ee783b712c | -3.91343 | -48.33862 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 287b147f-2d77-3042-822e-d7b0c9b46005 | -3.9128 | -48.34261 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d03773be-6297-31fe-9d87-506f4bc90983 | -3.91217 | -48.3466 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54b0d646-a27f-3414-b70f-c7510191131a | -3.91154 | -48.35057 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 560780af-2925-3014-b895-a8caeb7e3cb2 | -3.9109 | -48.35454 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ccc49dc-6696-3ae7-8297-24e43ddbe60f | -3.90991 | -48.33805 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a0417c2-82b8-3e2e-83b7-5f79e907126f | -3.90928 | -48.34202 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8dd7e053-ecfe-363e-aaf7-a76117b29f47 | -3.90865 | -48.34599 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afc52051-3c52-3e0d-9c21-ea7488a2c1da | -3.90576 | -48.34144 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cef65ce4-4a98-3780-acd4-b3aea47b5d6b | -3.89266 | -48.35564 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a5d436a-6d7b-3f80-9533-cef00ac0efb5 | -3.89202 | -48.35963 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab25fbac-1565-35e4-bbba-31de29154384 | -3.76686 | -48.1035 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c15c324-37e7-36f4-b865-f8e3ad446449 | -3.76624 | -48.10736 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c079e502-10d8-33d1-906d-d89bae50bc44 | -5.06638 | -48.2906 | 2024-10-11 04:23:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16ff05d2-abca-39d9-bbe4-9f1f19d00e51 | -4.96241 | -49.06793 | 2024-10-11 04:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb7db42e-a292-3a12-b8fd-ead75d8f2e2d | -4.11571 | -48.25239 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c036e8db-e460-3c79-b860-c07663acfbbc | -4.92177 | -48.62465 | 2024-10-11 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22f57fd9-eaf5-3440-89ba-82fb75069188 | -4.83792 | -48.93872 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5905ad5e-bdf4-3038-b9a4-ad226af121f4 | -4.83724 | -48.94286 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 360238f0-3a1f-3bde-b536-754b1fe2551e | -4.83433 | -48.93817 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bf8c7c8-3fa8-3a0b-be54-4d8c1aa42f72 | -4.82266 | -48.22186 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f8ffc23-f40f-3245-8118-68a3ece02061 | -4.79577 | -48.89075 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10dfe68f-8faf-3066-972d-d06f7e589477 | -4.79511 | -48.89487 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c9cb30a-4e23-3c02-9891-9251fe5fea74 | -4.78662 | -48.90196 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 83f70de2-3cdf-381d-b5e8-26b2c1f68d9e | -4.77788 | -48.88773 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afd32f1b-ef5e-3d1e-bf50-f0dfe84f6c58 | -4.69388 | -48.62237 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1dd955bc-1d41-3eb3-8cbf-0234cf018d59 | -4.40585 | -48.70297 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0be7e9be-0633-3624-84d0-cbe59a9cc243 | -4.38542 | -48.62541 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b843b3f-af22-37c7-abb4-1f93b89a18ea | -4.38252 | -48.62074 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5063c702-50c5-3bb9-a2e2-97dd6a733c7b | -4.38187 | -48.62482 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cf5394a-6056-34ab-9489-1f2fbb7fac9e | -4.37832 | -48.62423 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab27b244-f0c4-3c23-bd0f-44804e4defc6 | -4.31528 | -48.63591 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 79129ba1-ff20-3cdd-b854-3ceac6521eba | -4.31464 | -48.63995 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 48d5bf23-a83e-3e4a-976e-5d7c42f86bfc | -4.25511 | -48.64708 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| da7aee0a-d199-3e21-b6c0-a0a4cd66162e | -4.25445 | -48.65113 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98492d69-4727-3091-85dd-2bf01cc74445 | -4.25089 | -48.65055 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1873fd4-38a6-38e9-b6a7-3e86983cd32c | -4.12019 | -48.26927 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92066e4b-fbed-3c94-951c-e7f48a146670 | -4.11956 | -48.2732 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 083c0162-54a7-3eba-bcbc-afcaf38e2b53 | -4.11732 | -48.26475 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1dba3c68-79fa-3b70-9f7c-0e56e0b4c9eb | -4.11695 | -48.2446 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 16b7b37b-11d4-3904-a5fd-0245f3351537 | -4.11669 | -48.2687 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7519fe1c-fae1-3c1c-9dfc-f2d807759b5f | -4.11633 | -48.24849 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d5a79874-26ac-3727-9732-044544efb8b8 | -4.11606 | -48.27264 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01e7b0ac-e26b-3fa2-8bcf-5163bc8a7002 | -4.11543 | -48.27657 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3dfa7fe7-35ae-39f6-8ba6-17c504eba13d | -4.11508 | -48.25631 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9e5e2150-fa92-320b-8393-cfa4dd3187e9 | -4.11445 | -48.26023 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 67536228-d497-3740-ad2a-ede75aa2287e | -4.11382 | -48.26417 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 322accef-dbfa-3949-b7ab-f02fcbec6bfd | -4.11345 | -48.24404 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| b813d171-febb-37d7-bdcb-d9a51f14e3e2 | -4.11319 | -48.26812 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README61.md)
