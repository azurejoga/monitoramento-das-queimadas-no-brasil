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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c2a7c67-022e-39dc-a5ac-5896a553dd1c | 2.6685 | -61.17258 | 2026-04-12 06:12:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f45bbd-1712-30cc-bf8e-c1096f0cbafe | 2.53521 | -60.35006 | 2026-04-12 06:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33b9b4dc-8e54-378d-bfc3-6d8a8b7d2677 | 1.21609 | -60.44864 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab663400-f783-3a3c-a2f8-73c84e5fcdaa | 1.36895 | -60.66034 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b7c5b0b-58ca-3a82-a585-34e820692dd7 | 0.42698 | -60.50696 | 2026-04-12 06:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0d51c5f-3073-340a-984d-9b24f7135cc3 | 0.42755 | -60.51062 | 2026-04-12 06:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5ea3ff5-9be9-351f-9ede-6e05bd1f688b | 2.02092 | -61.0948 | 2026-04-12 07:26:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c6ebe7a8-d9d2-3075-a465-8860697d4a61 | 2.01959 | -61.08603 | 2026-04-12 07:26:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01c8e19b-f111-3301-9399-e1a01c06fb60 | 2.53766 | -60.34966 | 2026-04-12 07:26:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4dd50e1e-f0a0-380c-abdb-fbad9c4bab03 | 2.6717 | -61.17012 | 2026-04-12 07:26:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10dd6b28-0505-391b-b9a5-b1118e290bac | 1.35677 | -60.68408 | 2026-04-12 07:26:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4b5f3ad2-a392-3fec-b21c-07f3cea40c23 | 2.02969 | -61.0935 | 2026-04-12 07:26:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ecc682c2-5d2e-3984-bd43-652fe1d18438 | -11.79977 | -43.63206 | 2026-04-12 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 1ecd5e35-bf80-3a7a-9748-252f5d24640b | -13.44316 | -44.04539 | 2026-04-12 12:04:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 60ee5e06-741f-3bec-a7c7-72fb1965bf1a | -11.80408 | -43.62669 | 2026-04-12 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 1e9e0822-fc68-3b69-befb-30a3a2320cf1 | -11.80177 | -43.61546 | 2026-04-12 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 21ac09d5-8c39-36eb-b2e1-ddb6dfc44139 | -19.77438 | -49.76215 | 2026-04-12 12:06:00 | TERRA_M-T | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5f70efe-cfdd-30f5-936d-13dd1f178619 | -21.37807 | -49.11048 | 2026-04-12 12:06:00 | TERRA_M-T | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c0f873a7-18e2-3521-bef2-d49896148ac3 | -23.74711 | -52.46491 | 2026-04-12 12:08:00 | TERRA_M-T | TERRA BOA | PARANÁ | Brasil | 4127205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 51a243ee-fa25-3e8b-b09b-6c7b789d89d7 | -11.811 | -43.6133 | 2026-04-12 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| df12bc40-c4ed-3d0d-8f28-743c181386f3 | -11.8105 | -43.637 | 2026-04-12 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 65274888-03ec-31ea-9718-34c452c5b5bb | -11.7913 | -43.64 | 2026-04-12 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 20306967-1742-35d9-a66f-396f012f5a66 | -11.7917 | -43.6163 | 2026-04-12 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c72cc62c-fac8-3bb9-9acd-ff27ff120bc0 | -11.811 | -43.6133 | 2026-04-12 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 956fd7ff-c557-3798-9ca9-1eb6cd9c41fa | -11.8105 | -43.637 | 2026-04-12 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 3b8a90b6-1f8b-3079-ba38-a00b063bb442 | -11.7917 | -43.6163 | 2026-04-12 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 76e184b4-e292-3481-8bb9-5e03b163df38 | -11.7913 | -43.64 | 2026-04-12 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| c812d0a9-d560-3e85-bdcb-e084334e965c | -11.811 | -43.6133 | 2026-04-12 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 84e5e0ba-6b2c-35a0-a98c-2949be8a4d51 | -11.7913 | -43.64 | 2026-04-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| cc89e798-fdda-360d-a9d0-894aa4b54785 | -11.8105 | -43.637 | 2026-04-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 49ada36a-877a-3afd-a000-8e95410cd3c7 | -11.811 | -43.6133 | 2026-04-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 255b8119-45d0-3f71-99f0-a32b6f4558d9 | -11.7917 | -43.6163 | 2026-04-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 716b81cf-05a6-35de-beb9-e62cb61e28bc | -11.811 | -43.6133 | 2026-04-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| fb497fc4-647e-3b86-9ca7-5aff1977c719 | -11.8105 | -43.637 | 2026-04-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 7322c9dc-a88d-3ceb-8a80-ced7b0798ac3 | -11.7913 | -43.64 | 2026-04-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 05ac8390-5d9d-3232-a361-dd7f2f9140de | -11.7917 | -43.6163 | 2026-04-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b55255ef-fa30-34f8-8bba-509b8b2b6187 | -11.7917 | -43.6163 | 2026-04-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9cccb35f-acb0-3c3f-84da-cb058fa014f1 | -11.811 | -43.6133 | 2026-04-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f325b970-1815-32eb-a56a-3146fb7c4b75 | -11.7913 | -43.64 | 2026-04-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 1ee518df-8df0-35ba-b004-32f121f10d9f | -11.8105 | -43.637 | 2026-04-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 9acaa009-1618-3dc9-825c-5ad7dd83dd69 | -11.7917 | -43.6163 | 2026-04-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 802feaa6-1745-3513-8b97-e713fb0cb39e | -11.7913 | -43.64 | 2026-04-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 290fc694-ec84-3f50-bb4c-c55f331edf3d | -11.811 | -43.6133 | 2026-04-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c77c7381-d319-320a-8a51-2d6d6a43a269 | -11.7917 | -43.6163 | 2026-04-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f6dba6c5-30d9-3060-89a6-7202f2cfb48a | -11.811 | -43.6133 | 2026-04-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| cb53da9c-cfa9-30b9-b2c8-38651997d3f9 | -11.8105 | -43.637 | 2026-04-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| b370f0eb-3540-35df-8bba-48cf9941dc4e | -11.7913 | -43.64 | 2026-04-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |


