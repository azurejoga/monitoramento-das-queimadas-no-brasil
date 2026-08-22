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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 516cb4b8-d6fa-3f87-8f2c-8e94d585cd91 | -6.79166 | -59.41195 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 90a865a1-9e23-3d45-8dfc-0b84566ee47a | -9.05116 | -65.45454 | 2026-08-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a96e2c3-9c89-31ec-90fe-a010387c5ccd | -9.16878 | -59.45158 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b592d50f-1295-3674-aa08-36ab5f549c46 | -6.81722 | -59.40939 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef97e0ea-6e64-3049-846b-8175c50c61b0 | -6.95097 | -59.31218 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb22f560-fc32-3279-94cf-fe471d4dc8d4 | -6.82976 | -59.67582 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0f97c37-fef6-3b2e-952d-8ee977177051 | -6.79361 | -58.64051 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bc60d1f2-439a-3e3d-a47c-c4da98b1b4ad | -6.8551 | -59.43872 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26587e05-77ca-3205-af81-ff6af77c1714 | -6.8078 | -59.39131 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaec7f2f-1e85-3686-ad8f-51e3d3c06bc3 | -6.79747 | -59.41877 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| bca24555-ad17-3892-8315-83c985b5fa7c | -7.50095 | -60.07393 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f789983-ceb4-368a-b738-32c1d956467a | -7.01799 | -71.77287 | 2026-08-22 06:08:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 234a98ab-325f-39b6-b0bb-079b9073068a | -7.60472 | -60.96203 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e91fed4-cc70-39d8-b137-31aa526ee4f1 | -6.67343 | -58.75292 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86b26ec9-db21-3e18-ac7a-d810657b21de | -6.811 | -59.66767 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2855be05-db85-3f94-8133-12a73c51a0fd | -6.26495 | -62.52301 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fe26fef-0abd-3972-bb33-f0941db9b491 | -6.37224 | -62.90726 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fdf52b3-9310-39fe-9ccb-c7aa9744755f | -8.89985 | -60.54589 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 72da8367-f34e-34cc-addc-49a233086c96 | -9.21828 | -59.77331 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c42fb95e-dd78-3f7f-b00f-6593de063c25 | -6.85379 | -59.43797 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37a8b9d0-9534-31d5-9995-2a4d901b317d | -6.80993 | -59.41413 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b012aa9b-6236-324e-8a38-b1e41d56d73b | -6.77328 | -58.68908 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1db39ffc-c6e5-339e-850a-09b9fa7ac157 | -8.90045 | -60.54089 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1a1bba31-d3dd-34bd-875a-2222e6c51973 | -6.84867 | -59.42562 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 57b12ad6-09de-3c47-b0e8-3556c52e1130 | -6.00431 | -57.81726 | 2026-08-22 06:08:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 230a2d05-1159-3eb4-9497-cc0e14ec27dd | -6.76285 | -58.66149 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e2fe01e3-e286-395e-b57d-736abde5ddbc | -6.81936 | -59.3924 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0ae0614f-b432-3071-807d-15a33bd09ad6 | -6.86399 | -59.46268 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 025910f8-d2b7-35fa-8fa0-68ab4d6e2841 | -8.38903 | -62.6805 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dae384ee-7026-3841-8be1-1368382a7bf8 | -8.39898 | -62.68939 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75c119be-43c7-3b28-82e1-6fe38cba5c43 | -7.86138 | -63.76229 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 963da159-9151-33e1-b431-18e07c0e9f92 | -7.55019 | -61.18542 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7278bc11-0820-344c-8bd9-c8503384e8d3 | -6.80451 | -59.66681 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ed1f4b7-4b94-3202-9b19-8ecaf87b9809 | -6.26937 | -62.53051 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c5c31ea-775c-328c-86da-4a7d8f8382e9 | -7.86093 | -63.76203 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ef4b640-8664-35bb-b668-a3d18bda208c | -6.79521 | -59.43592 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 455b184d-3791-3221-a9d3-55c1f78313ad | -6.79014 | -59.42352 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 07d1f475-2df6-328b-b49a-213b6c085874 | -9.16661 | -59.46991 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 272ff242-1254-369c-87ed-ee1068192044 | -6.94971 | -59.305 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd5b3749-9358-3fe2-884c-f226e176c387 | -6.82095 | -59.39339 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a34e7ffb-8a1a-3541-866b-fd11c75ef4f7 | -6.81136 | -59.41509 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb2d8836-7a80-3dad-a1f7-b65da2fbd570 | -8.89637 | -60.54603 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0891d927-3b40-3c9e-a792-cfe640c7e478 | -8.40989 | -62.69095 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c10f68b2-1d95-30f8-91b3-766dc89a0d2d | -9.21595 | -59.77411 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea9bbd9b-14ad-3155-801f-f620eaa9a545 | -9.40868 | -60.42789 | 2026-08-22 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45f1a899-f00d-332d-9182-499d38d4d6b8 | -6.92909 | -59.3078 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e270a98c-6783-3049-8532-c48f52cf4324 | -6.94094 | -59.32096 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1d8ea6b-1e76-3d0b-952b-f77b77bfd0cb | -6.85007 | -59.42642 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f30e47d6-18aa-39d3-95c4-d0bc9a46d44b | -6.27472 | -62.53129 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b6ecb65-9686-3356-b5b1-461d1a2b1c29 | -6.85587 | -59.43307 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63cff256-bb24-357c-a47c-4309fe4cb15c | -6.88157 | -59.43037 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 809244ea-f5dd-3b8f-b83f-93aae79d19e6 | -9.21236 | -59.7666 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef653396-3089-3867-9de6-f06f1e1c146d | -6.86619 | -59.44563 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 340ce1fc-ec22-3abb-8c09-91b5d14abb42 | -6.96844 | -59.04692 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d3dbaba2-4e9d-3b7d-ab72-711b9a9fa505 | -6.79448 | -59.44144 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba34d564-2aa7-3e98-b691-5a30a4cf9098 | -6.26006 | -62.51884 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 846f590c-b008-3fca-87cb-33b1696412ad | -6.8128 | -59.39124 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4bb419e1-3566-368d-87d0-71a98de2d86a | -5.91156 | -61.29785 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec89c27f-17c8-3ade-b7c7-58815b8199d2 | -6.76479 | -58.70065 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33f32291-a204-362a-9ede-8ba88171a375 | -6.81794 | -59.41603 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc498824-64bf-3f51-b370-e900d2404f20 | -6.13632 | -59.91546 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29e8363a-2252-33c7-ba9a-dc6a81791f2f | -6.9443 | -59.31147 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1ef138f-62db-33dc-a6a0-f66d3d724877 | -8.90268 | -60.54681 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe72c69d-02b4-3e1d-b2a8-0fa4e0213739 | -6.8048 | -59.41402 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 96bc30f0-83f2-3dac-944e-d5965b2761a4 | -6.80299 | -58.62241 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d2d93e7e-06eb-38d3-9e02-ba7bd51ba61d | -9.18375 | -59.44126 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6aa06cff-786d-3751-8596-9e3e5f0c5042 | -6.9102 | -58.99717 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfca2725-3e2f-3223-ae97-db3ac53732c4 | -6.80216 | -58.62879 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ebfa417-5579-3db1-990d-c5427365b988 | -6.69723 | -58.93856 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6993cb5f-84bf-3120-ae10-bb208fd2a09d | -7.60114 | -60.94294 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 400d29cb-1012-3a91-b461-e7e9c3f4a7c0 | -7.55357 | -61.18656 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3712197-b9e5-3530-8b58-e7cd7c23372d | -6.82309 | -59.41605 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fdf70ca1-17bc-3010-b341-ef5f65a69b6a | -9.1732 | -59.45298 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6d149c2c-9911-3bea-ad9d-b9c0fb58fbdf | -6.78795 | -59.4402 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 145ad2f5-b8a1-3a41-8b5e-2a4606d2dec7 | -7.67194 | -61.11839 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9b62af0-d7b8-39bb-ad1f-64297bca39de | -7.60533 | -60.95754 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 640ff6d6-a86c-31fb-b604-43deb0ff727a | -6.97134 | -59.05553 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2861283b-fe6c-37de-bb56-19e94b850a84 | -7.02429 | -59.5506 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30e1b5fc-32f4-3491-9442-9a9b72825a2d | -6.78869 | -59.43461 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d3a1d648-600c-3c7e-901b-e02f65e307ac | -6.76724 | -58.68169 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2f35732d-b587-3874-80c4-19638485a601 | -6.90267 | -59.00231 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3829595b-d543-30bd-af92-e28ee3f57fda | -9.11078 | -60.9202 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b622d6ec-714d-30fa-994c-e94220e50747 | -8.89294 | -60.55006 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e22a0ca6-71e8-3246-8091-a500162a639c | -7.87879 | -63.74368 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9ea4be9-dbcc-311d-8c49-5454230624d8 | -6.85962 | -59.44468 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fc436ec-a182-3643-bf3a-55a55396bd9b | -6.12567 | -59.89821 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9dcd4d0-a0f6-3293-bdcc-781245bea011 | -9.11751 | -61.59483 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 860b5f9c-e5e3-3fb4-9c12-e2dd7f94e5bd | -6.76371 | -58.65482 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9b9f1ab7-f143-39a5-83e6-579486e39f1e | -7.01705 | -59.55511 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 864ccc7f-bcd5-3778-8e22-ede172fcfc9d | -6.81439 | -59.39226 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7087a272-f073-3c47-b3cc-f117f1a96aa1 | -6.818 | -59.66334 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d035c6e2-c4ba-3a15-b261-9646e3886ebc | -7.59511 | -60.94192 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e51354d6-b555-30b8-8007-4c07c17f8375 | -6.96767 | -59.05312 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 55bc8fa5-2791-3716-aadd-bc2d477162f1 | -6.85452 | -59.4323 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32fe7fdc-c916-3f84-aeec-4d1e7a235840 | -6.53346 | -58.53288 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3ab7fd9b-ab7b-3f43-a2be-d28d135c9118 | -6.25959 | -62.52223 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fd46e3a-d771-302d-80bd-06f3dee016c7 | -6.37318 | -62.90363 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c895c09c-1b9b-3dec-ba67-764985986f97 | -6.36838 | -62.89967 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a97a09b-898c-3d31-a8e6-c546faad4531 | -9.21593 | -60.77079 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a1ca272-3d7b-3a6a-9066-2bb5c9eaa217 | -6.90694 | -59.00393 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README80.md)
