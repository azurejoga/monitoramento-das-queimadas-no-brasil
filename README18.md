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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd6e9df2-2517-3169-9d56-f5cc86dc5cb0 | -14.23115 | -51.80355 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bf46af9-0c66-3cbb-973d-572b0d103603 | -16.09427 | -57.28027 | 2025-10-20 05:06:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e21ce56c-dec1-3638-b1b3-f1e319def5b0 | -15.30396 | -59.23684 | 2025-10-20 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa4642e5-4f54-37a4-b5a5-6de4ad867828 | -14.23319 | -51.7877 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c78284e-216e-352e-bcf2-7eea04a92435 | -9.64101 | -65.25227 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4da39ad-2644-3647-8b45-3db66dd489aa | -14.23268 | -51.79165 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcd9fbad-520c-3cc5-8335-d8d73343e119 | -16.90626 | -53.01886 | 2025-10-20 05:06:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eee6ed1b-fab4-35a3-9af8-cbdf86d8f714 | -9.90054 | -64.17159 | 2025-10-20 05:06:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43c6763a-f716-3107-8136-1a45b5ae540b | -9.89275 | -63.58832 | 2025-10-20 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0b7c1c6-7042-3b29-ac36-008ebf55cafd | -15.30199 | -59.2369 | 2025-10-20 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5af03ec9-9496-3664-9abb-984554e7b202 | -12.36982 | -63.88081 | 2025-10-20 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d078c811-0151-3c6e-a5d7-b3a19f019d2e | -9.63977 | -64.74642 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7662a3e5-a713-3dcf-83e7-9e048e48b55d | -9.69166 | -63.30684 | 2025-10-20 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f226607-8687-3bb2-a13b-6b0f7188453a | -9.89733 | -63.5891 | 2025-10-20 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c56f970-0fc4-399a-9ea3-bc2a0ef0a9a3 | -15.30457 | -59.23313 | 2025-10-20 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96346ca7-6f79-3343-b508-22984a63816e | -9.73228 | -64.94704 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66cc0bda-f894-339c-a057-7d824352a7dd | -12.70188 | -62.18854 | 2025-10-20 05:06:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 217cc0f3-0908-3c98-85c2-ced8a40b931f | -9.11676 | -65.36633 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 682f8521-8ad9-3976-92a2-3f6f42773132 | -9.64677 | -64.73598 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ca79bad-0408-31e4-9765-dd63d535e05d | -14.23166 | -51.79958 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc2b08e0-64b1-3f4c-aa70-01366baa4fbf | -9.64576 | -64.74165 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e86c8c4d-183a-3591-b128-8bcdac05ce56 | -15.30335 | -59.24055 | 2025-10-20 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f54854f-f7db-32ba-a2ab-14c1b7c89a9d | -9.64727 | -64.7332 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ae4c449-6ed0-35ea-9887-223759add752 | -14.21821 | -51.43652 | 2025-10-20 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd6be79-595f-347e-9cdb-edde2737d964 | -14.23079 | -51.79626 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56911862-63ee-3649-983c-dd6f184af580 | -12.36452 | -63.88451 | 2025-10-20 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 955bbb43-108d-3d2b-9571-60ec030acab0 | -9.11734 | -65.36311 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed1f351a-9009-3775-846a-d547acfaa28f | -15.29923 | -59.23262 | 2025-10-20 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3506896-da72-33eb-aa52-339a4dbf153c | -9.64614 | -65.25322 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee02323d-739e-37eb-b22f-da5d6ea32770 | -9.72112 | -65.87643 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e25d9de6-76b3-30fc-a577-640c9b7648b4 | -9.6408 | -64.74068 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75cb7844-89b9-3c89-b1b3-5ccfde59ed4a | -9.11217 | -65.36295 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fd43d2f-4720-378a-be5a-088912ea2d8b | -9.11799 | -65.36072 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d51b5316-5ab9-3da6-b34b-ad816bd4b421 | -10.59331 | -63.47669 | 2025-10-20 05:06:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1b6dbad-673e-3269-a520-65473d692538 | -14.24003 | -51.80077 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3737ce1-e551-358e-aa3e-e79fb08bd05e | -12.36899 | -63.88535 | 2025-10-20 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6cb1f3d3-93e8-3f07-a365-a4ee8ad831b8 | -9.62704 | -64.15434 | 2025-10-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fbe7e73-b3fe-30fe-8fd4-24d8f654edf3 | -9.11739 | -65.36392 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7a28f7b8-9eba-3b83-93b9-e135addeff3c | -14.23585 | -51.80017 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8888f5af-bdb9-34ab-bfc2-3282daae34d1 | -9.11157 | -65.36617 | 2025-10-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 407c1765-30bd-3f8e-8e24-c7efa4fc25b2 | -15.30671 | -59.24113 | 2025-10-20 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ba9fd5d-b6f4-31d2-bcd1-3f33af375c6c | -11.75716 | -61.07496 | 2025-10-20 05:06:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 709412b9-afdd-31fe-b31f-04ce37c639f8 | -14.24054 | -51.79682 | 2025-10-20 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2d081d9-aa90-3a24-87ea-facc096fd283 | -22.30383 | -51.50909 | 2025-10-20 05:08:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 038187bb-4916-3e77-9995-1017c367ad4e | -23.35642 | -54.34293 | 2025-10-20 05:08:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6b3065ba-1f4d-31ad-8d0a-1fb407a36d48 | -22.3043 | -51.50956 | 2025-10-20 05:08:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d9749988-e698-3b97-886c-3e5821d15ca5 | -17.68518 | -52.24303 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e31a0d9-be61-35f9-8d19-751c93a42e54 | -17.68039 | -52.24661 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74fcdafa-ef67-326c-918b-ed3faf4494b1 | -21.64535 | -48.39734 | 2025-10-20 05:08:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc956e4e-c370-38c6-8bf1-80e9bd473769 | -17.68943 | -52.24372 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9eb52b0-f0fc-3ae2-ab01-7fb6ee7ed518 | -19.04361 | -49.70009 | 2025-10-20 05:08:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ce64f3a-44ac-33e4-b910-0cb534c920f0 | -17.68466 | -52.24713 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5c119d2-e141-3a7d-bafb-1828507f7d1e | -19.03885 | -49.69587 | 2025-10-20 05:08:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 828f45da-e1a1-30f3-bbed-3a2c31c3a868 | -18.26107 | -52.89611 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a31d0c5-b492-3239-9f0d-d235ea595d62 | -17.68142 | -52.23845 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d298930-dd71-359c-bddd-87096f250d9c | -18.01775 | -52.68411 | 2025-10-20 05:08:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03a0b5e7-e772-31c5-a4e4-53c84e5a2d55 | -18.26157 | -52.89222 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c3cd5c0-f042-3354-8c69-f34eb00ea1df | -21.18815 | -56.47807 | 2025-10-20 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a349618f-6844-38ab-9134-cbcd8d6450e8 | -17.68091 | -52.2425 | 2025-10-20 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2ced64f-1ac1-3d70-a13c-8dea1d5b9b66 | -19.0385 | -49.69916 | 2025-10-20 05:08:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 235d6c53-6981-31e7-82d3-cb4ec8d5857c | -19.03814 | -49.70246 | 2025-10-20 05:08:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2448424c-141c-3c15-9876-99e1756e2f62 | -2.2527 | -51.9108 | 2025-10-20 05:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3233f6e8-4327-3efd-a1e9-e6dcb3284f8b | -2.2527 | -51.9108 | 2025-10-20 05:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ba622cf6-d63f-30be-a3df-73a544eb63f5 | 2.04237 | -55.72076 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 967e7275-c9fc-3658-9087-4ecb64757c0f | 1.72047 | -55.75436 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3153de7-4bc5-32af-be0c-8002dbfa097e | 1.84915 | -55.66349 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46ffc1c0-8793-3cde-94d8-785327e77298 | 1.76534 | -55.71489 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8a1194c-c285-38d9-9020-f6a81d2c4854 | 1.70393 | -55.77744 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| ac9cad51-9088-358d-be5c-2cac884f3d97 | 0.97667 | -51.14758 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba08d95d-d2cc-39cb-b63c-767f13fa7a26 | 1.81751 | -55.66841 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0f8ad74-434d-3b8f-9773-590249d3f147 | 1.79846 | -55.69421 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 529b3261-e1c7-39ed-92d5-3ab38a9aa5ce | 0.98104 | -51.14258 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f795987e-21d4-3db3-88c5-dd249ef2c3a3 | 1.71416 | -55.76559 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fec8d585-8248-3468-acf8-e6e26a0074e7 | 0.97181 | -51.15491 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c08322c-2b7e-33a7-92c4-7a659ec12f38 | 2.06674 | -55.72203 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744ce65c-c7de-3ff4-895e-bcf5b4135e4b | 1.74256 | -55.92091 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5feeea23-dc04-37b7-bad8-046c9a843e5b | 1.72573 | -55.94035 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e8a0ecbf-dee8-30bc-ac70-05ed47286c8d | 1.78347 | -55.70175 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2465c99f-8917-3cc3-8ad5-04c953d3991c | 1.73977 | -55.92817 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0e471146-81b4-3107-9dde-386031a8aa8c | 1.82855 | -55.66155 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afeca1fd-deed-3275-ab1d-b9c5b4813d10 | 0.96637 | -51.15584 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc917523-413f-3477-b3d2-68a49fd789f4 | 1.73901 | -55.92332 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 66f029b4-f82a-3d53-a5d7-c23bd6a09fbd | 1.78428 | -55.70679 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a0608cc-eb58-3ada-9932-6306030da1df | 0.85982 | -51.12564 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dde0ba83-696a-31c1-92a4-730611afe804 | 1.74177 | -55.91608 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fe58780f-400d-3eb9-bb70-242ab104b017 | 1.81819 | -55.66516 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba739eb9-cdaf-38d3-b06c-83be5be1c232 | 1.72997 | -55.74605 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44ee3977-6dd9-34c7-809b-f765bea4179c | 0.97615 | -51.14703 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f77a7dc4-8dc9-3d31-af03-086568c67bd8 | 1.71949 | -55.95129 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f9d701c-d0e4-3759-8b6b-9fba361b0027 | 1.82531 | -55.65889 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bfa4d1f-6c43-3904-9492-b9bee645135e | 1.74643 | -55.72301 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5d4903f-acd2-3694-9479-5918487af1e4 | 1.00216 | -51.13252 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad15d375-8cd1-3552-9026-eb2e89a7ab6c | 0.97238 | -51.15545 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cd52f06-c863-36c1-a759-aeb460d471e6 | 1.70786 | -55.77681 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e3a77ef1-4991-3b21-866e-7be7b447287c | 2.04102 | -55.76148 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac4bc7e3-51a1-3a0d-ab9e-4af1eaa63b88 | 0.99671 | -51.13347 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d303b58-aec0-3d6a-aeb9-219ed359b541 | 1.81898 | -55.6702 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22852ff0-9130-3888-8516-79777ce09f5c | 1.81521 | -55.67912 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f189c9e1-6c8e-3b7e-9203-586803339083 | 1.71731 | -55.75997 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55e0d893-fc81-3a89-b1b8-341ecf2f24f9 | 1.8246 | -55.66217 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
