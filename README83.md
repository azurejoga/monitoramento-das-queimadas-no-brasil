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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e18f7b8-1795-387c-804b-64180b993b92 | -7.74062 | -61.08699 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c4bd257-e9bc-3383-830d-1665f8ec08e1 | -9.16079 | -59.55945 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 54df982f-674e-3d6e-b7d0-7e6fca55f822 | -9.06051 | -66.06903 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bba8e0c9-7ae6-3b79-bf09-e4ad3dd914c5 | -9.14581 | -60.78596 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc87ea74-6a6d-3bdf-b97e-34ee201d122b | -8.88679 | -62.47509 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fd7d9d5-1f58-3b69-89cb-cfade52dc857 | -9.09054 | -65.72894 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 745e4682-a514-395c-a4bf-11329f21b4a2 | -7.62195 | -61.04059 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff573526-6aa7-303c-9b35-d202d1cab9c5 | -8.8619 | -62.44904 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 927a4596-1ef0-3178-a8f0-d3755aa6e3ba | -10.77108 | -60.78868 | 2025-08-27 06:08:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91ab185e-f817-3000-881c-789152af1a10 | -8.96154 | -65.97397 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d4bc729f-f67d-3107-8b30-f0d89488af4f | -8.96291 | -65.9621 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8e45cff9-953e-3d7f-8e47-550e4d36798b | -9.40052 | -60.54279 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4e75591c-9c50-36d4-b92e-7006d6e6803a | -9.08543 | -65.7328 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b3f8bd3a-fd2e-300c-82e3-b1f3d24a8cb8 | -9.15259 | -59.57042 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbb6f90c-6e81-3d33-87c8-66f651c84033 | -10.27512 | -64.49835 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9e72e17-a603-35d5-bec5-eef8c714ef75 | -10.09276 | -62.90669 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| bdafebee-6aac-38fa-9c41-dfdb762a0fd7 | -8.34684 | -62.94417 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b1c2569-7c65-3ad7-af38-ec1f0268363d | -8.65255 | -67.26737 | 2025-08-27 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f67b0763-cc70-39ae-b755-842a08aa2946 | -9.8236 | -64.28516 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16541569-3aa4-3150-9ea8-a526eebe105e | -9.15332 | -59.59283 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcde087f-19df-3f99-b523-596a882c93f7 | -7.40487 | -64.34855 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 905e0394-b1b6-3bc4-8f87-532a06936289 | -7.60306 | -61.63169 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf4af1da-f480-3203-8820-e9ea563c6c79 | -8.86092 | -62.45648 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aba1110a-25df-31ee-8f91-ea286fcc2c59 | -14.77018 | -59.73358 | 2025-08-27 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 52025727-ff40-3a47-9206-c8f816d7d6a1 | -9.17323 | -60.76943 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d780986f-b1c7-32c8-a8fe-2c14552fb8e0 | -9.28632 | -63.72086 | 2025-08-27 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6219c641-f1bc-3db6-bd0f-5b4cf2b68a10 | -8.96353 | -65.95784 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 694c4430-1267-31e0-8b7d-4a2049d1f997 | -7.54153 | -63.83997 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a4e34c3-fda5-3268-811d-d8d986b86420 | -8.34148 | -62.94349 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dfdecb9-5967-3ab0-8689-1d2505d185e1 | -9.01367 | -65.69096 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aef3dd6f-3688-3a00-a7af-3281017a98e5 | -9.8288 | -64.28761 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64e3ca60-4f81-389f-99f9-637d78fdc3cf | -8.89225 | -60.76577 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 727ad784-c7e8-3ff9-9aa8-923d6bf6040d | -8.96096 | -65.97827 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1beecb7a-4de0-3a1a-b429-10c75721f662 | -9.4202 | -60.54009 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7c10740-1bf2-3083-be08-3c6351875fa2 | -9.40115 | -62.48697 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a987db47-fc5a-38b0-97e0-b0eef46afd80 | -9.82283 | -64.29086 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd31a5f3-c033-34ab-bec3-2ac7f780a3a7 | -9.17239 | -59.54749 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f8a722-32a5-3b5f-8a4d-30ccacea8f78 | -8.92322 | -65.92583 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d3838bd-0e72-389e-8c0a-aa2d843e9efc | -9.4107 | -60.5127 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7dcda91c-b7aa-3028-a7ba-004c4c665f19 | -8.07153 | -61.53819 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9359e2eb-90ac-3b75-b97d-64b928d9eb8b | -8.33612 | -62.94276 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27825ce4-af81-3d2b-99df-2d1e62d36af9 | -8.95715 | -65.97332 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 44df7566-8d00-3095-807e-7f5031244795 | -9.18723 | -59.45885 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46f7130b-d9da-3691-a060-1f432cadcc9f | -8.89843 | -62.47284 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbfc437f-f228-3a8e-b92d-6df06fba9199 | -9.40751 | -60.53838 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42f27067-4a30-3981-b1c4-593e6ea357a9 | -8.89726 | -62.47209 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f25b0c8-929a-304c-ae06-95d0b30bc454 | -8.96105 | -65.97504 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 779df2fd-8395-3ee0-a253-94a4f5137c9d | -9.19072 | -59.5388 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c35a42f8-eb58-3898-b65d-e07a1b51b6be | -9.18814 | -60.80168 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9405cb22-0d28-334e-97b1-42f89958062c | -9.07418 | -66.06674 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59c2038d-518b-3522-b991-e05981171222 | -8.93262 | -65.92281 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1bce2966-c34d-3ce0-b3fd-dc31c3f5798d | -8.88664 | -60.77308 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b41e1756-ae83-389e-bd5e-c2d2cf59a7ec | -9.022 | -65.69678 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d89fc317-6497-3954-8ab8-6c3afbd9c865 | -8.94277 | -65.94618 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 575abad1-97bb-30d5-99d2-1b52ffe77238 | -8.10734 | -61.48689 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 088a28cc-1605-397d-8078-2f187b4335b9 | -8.96124 | -65.94325 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 354a5bf9-cf61-39ba-a10d-4b7295c54ec6 | -8.9529 | -65.96947 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| a787b635-cadf-391a-91ce-c565c3a449de | -8.96389 | -65.95673 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 57691cd2-efd4-3674-9beb-2323619eb5aa | -9.03562 | -65.73043 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9561ec73-cf0b-3e94-8361-8b6856f6731f | -9.41578 | -60.52378 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cc2eeb52-1f8c-3825-a9ba-1d12e5fb5f01 | -8.10571 | -71.25325 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7af8d36-2cc8-3018-b733-2cbcc0df2255 | -8.07037 | -61.54172 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0c60c6d-4560-3ca4-9982-246875683094 | -8.89786 | -60.77147 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b58e908a-b854-3710-abb5-6222becd301d | -9.79345 | -64.24442 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5253fcdb-0e0f-3d00-b6ba-d97f4ef336c5 | -9.4145 | -60.53406 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9207d8d4-bea5-3ad0-9e13-b6346eb8a0f0 | -9.04901 | -65.73246 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab885dc0-1725-3398-97b9-0cd161dd4eed | -8.93459 | -65.94061 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3474d8ca-9fc3-3ec6-97e5-1fc95b5d2e55 | -9.15337 | -59.56425 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00b217ff-d5c9-3be4-9083-b78bf9b13276 | -9.11608 | -67.70836 | 2025-08-27 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c09332f-5624-3220-bee8-936d486fbbf1 | -7.5457 | -63.84634 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed27dcce-29e3-3bad-8b3c-6abe78fa6c92 | -9.0704 | -66.06188 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b894bda6-3941-3c7c-9f33-2075151f525d | -9.17579 | -59.46211 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60b599b2-b18d-313d-9b39-c8b6e5229459 | -9.17297 | -59.46307 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 53d8925b-6528-3def-bf16-044aebd4dd4d | -10.09919 | -62.90031 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83f88fed-7381-37ff-9198-91eb11c31d00 | -10.27017 | -64.49765 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17f682e9-05e3-3546-90d8-404bd9ecf86c | -14.77129 | -59.72238 | 2025-08-27 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97d57f94-4ef1-39bb-ac1f-727c952441e0 | -7.54407 | -63.85767 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c58cc474-a213-3eff-bcf5-5056d10f512d | -8.92202 | -65.93434 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41b47fda-b4b1-3755-820e-4a92d43119d2 | -8.95228 | -65.97377 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 839eb401-2990-3c36-9ae3-669d9bd6582b | -8.51337 | -69.79538 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0431434e-0b79-324e-b28e-7221afe0496d | -10.27092 | -64.49194 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ffca8bef-22c6-31b7-a9f9-1d3fc641c073 | -10.03814 | -67.53564 | 2025-08-27 06:08:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bb88c54-a85c-3eee-8534-a1783546bf80 | -8.96272 | -65.96531 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ef98b1c9-d7aa-3ebd-8e28-130e82dac4b6 | -9.40372 | -60.51699 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c04c72d0-84ef-3dba-b206-9ab5e8c5e68d | -8.85583 | -62.45203 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc01008c-bfb0-319e-8295-28f638edd22b | -9.39988 | -60.54797 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6565f35-fbcc-3784-8e6b-1cfc7679842b | -7.56137 | -63.84896 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 860cb8c5-eeff-3ac3-abf6-b9abd2ff948a | -8.95774 | -65.969 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7dd1539b-4e67-3dfd-944b-692116e1239f | -8.07626 | -61.54719 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc18102e-adf1-34bc-8190-b860d58e404d | -9.0407 | -65.72665 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 850cbb02-a692-3206-acb3-2e0b39ea9db7 | -9.16928 | -59.51649 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e406ee3a-ad1f-3e23-942b-97233c104a9e | -7.54643 | -63.84687 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa7bc7b8-22d2-3d41-b5da-2108e5a89efe | -9.41834 | -60.50326 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a14bf8a4-3b1a-3e45-b75f-653aef35f8e1 | -9.06603 | -66.06121 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d669e3c1-d572-31c4-8a5d-9ddac36e2c1f | -9.16828 | -59.5542 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ee156ee-5976-3f36-b7fa-a83bfb5c8854 | -8.99415 | -65.41916 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44ec9cbb-7492-3aa1-bf01-a8b7f0a6ea34 | -9.64825 | -64.99313 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 422baf4e-a8ec-3df6-af06-e3c8e2bff7d8 | -8.94595 | -65.95538 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| e9c85dcb-68bf-37f9-9585-448aec1ce567 | -9.08606 | -65.72834 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 489af2fe-eee8-3bff-aa90-7bbb3b833648 | -9.15638 | -59.54039 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README84.md)
