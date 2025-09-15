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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24537eb8-ca58-3618-8cc5-99117ec949a7 | -5.47133 | -44.68885 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55470dd9-252a-3723-8f26-510afe1eb9e2 | -8.43116 | -45.73422 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74bdbfb1-f2d9-3fa8-aa26-9a9d291454bb | -8.89075 | -45.4526 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11f01bb3-af65-3a96-b373-5c04a78bb7e8 | -7.71278 | -44.82487 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba8bba20-32b9-3ec7-a393-b7335b58e8cd | -8.14517 | -43.65302 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a12f16a3-541f-3625-819b-7706b823b3a5 | -8.89406 | -45.45312 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3457b325-e74c-30c9-8664-77f58edddfd8 | -7.84863 | -43.8549 | 2025-09-15 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2a20960-5796-34be-a32e-6c6813104b04 | -12.00244 | -46.6726 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 360d17b5-f16f-3c88-8ed7-982f8e72140a | -15.89976 | -49.99334 | 2025-09-15 04:21:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91d29756-25d1-3934-a540-5dd71bb947e9 | -16.64753 | -44.94044 | 2025-09-15 04:21:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09016a31-190e-3b62-a3a4-4956eea904fe | -14.50092 | -47.33444 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 366e6173-c435-3e67-a4d2-d96f71881241 | -16.28602 | -45.68287 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a51775b-f4b5-3c75-b1d9-c7811dcc5469 | -11.8148 | -44.70559 | 2025-09-15 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 322049c7-7eef-30e0-a942-1d2d404421dd | -14.12931 | -45.41184 | 2025-09-15 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1077dac-db3a-3702-acaa-fc7a3337855c | -15.78612 | -52.20575 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de20d6c9-9df0-30cd-9706-f28c600af878 | -10.30268 | -45.38276 | 2025-09-15 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 972b81a3-6156-35fa-87dd-048c3d247610 | -11.5054 | -43.64181 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8717ea5f-d85b-3630-abe9-63c8c8e7b620 | -12.64761 | -47.94904 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3e83659-5ca5-343b-b20b-16d5d7593955 | -14.51468 | -47.35479 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27d7742b-3921-3884-9143-f3c74ed859eb | -13.18752 | -47.28753 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c1971a0-29f2-34e3-9ece-42cdde85ab9c | -15.76679 | -52.22084 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 634fd82f-478e-36fc-af4d-21254dcd7183 | -10.76089 | -50.64806 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9c985c8b-118e-360b-8688-60986ad4b082 | -10.66797 | -46.24539 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08a68f97-0c04-3771-b854-55600d61a402 | -9.87505 | -46.45914 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d124b61-f338-3a1c-8c24-31698a5e4cb4 | -14.49987 | -47.31966 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80ceaaf6-af4a-3e2b-8f4c-15411fa15ea9 | -14.82933 | -51.63497 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 26581b1a-7aa5-3728-9106-8d7ad2c5b534 | -10.16957 | -45.32176 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 038248a5-c5d2-3f12-a077-b69d76d9c2f3 | -14.59427 | -46.5924 | 2025-09-15 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d741ab8b-cdb4-3ce9-831b-86463c37ca8f | -12.16296 | -47.58065 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb24cb12-268b-3a07-904d-bce273ad6aa5 | -13.88143 | -48.13947 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b91b6ba-99ef-30b1-8114-33d6dac01597 | -12.56597 | -45.63667 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb317857-e011-35a2-bd4c-20603340e5d6 | -15.78886 | -52.21361 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dfc244fe-2c24-3027-be34-c86e6866a5b5 | -14.94908 | -46.5634 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 035cc275-6716-3243-a29f-b7ac3ba76da8 | -11.47006 | -43.59282 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d93c3a1-2286-3b14-b708-c44f8a85b254 | -10.86891 | -45.46249 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6399adef-c5f6-3d3d-9bca-9276165a79d0 | -15.89621 | -49.99272 | 2025-09-15 04:21:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59593be5-64b9-3d63-91d5-83a2d6330072 | -14.2502 | -44.3852 | 2025-09-15 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd7b0c43-76b5-3416-88a6-08b381cbf209 | -12.98186 | -47.96895 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9f7fa19-ebc2-3137-ae2f-05871f1dffcd | -13.01467 | -46.74841 | 2025-09-15 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08b25d9b-a953-3186-8417-12027b955a0d | -10.75755 | -50.63892 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ff4ccd74-b445-3759-a52a-d41cc1db2281 | -14.94633 | -46.55931 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e6c44fd-6555-30c7-8614-09b93f0f2763 | -9.84346 | -43.1575 | 2025-09-15 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d97699e0-bd01-3a4b-88ff-2d5434999d4a | -12.60585 | -45.72988 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41aa2c8f-1285-36bf-8083-727ba466e731 | -10.88207 | -45.44308 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a75ef189-9558-3797-bc89-47441b6426a8 | -14.59702 | -46.59648 | 2025-09-15 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b22cead2-973f-3b7d-be96-0cca7fc93383 | -11.81144 | -44.70506 | 2025-09-15 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e84b0b3-f90e-3862-b4c7-cae10c050632 | -12.09618 | -44.86427 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2ba56f8-1bda-3cde-89a1-319c24ebbbb9 | -12.56543 | -45.64019 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a70eeeb-0098-30b7-ae17-8ee6a6b1e222 | -14.14236 | -46.26092 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff5a61c6-a6ab-339b-a22e-3c481a6f5184 | -10.17605 | -46.14804 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ff45d3a-f785-3d2b-a930-2bfc3aaa1f9c | -12.7878 | -47.97149 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9239e7d1-4b05-34e5-94f1-c021d090651e | -11.48167 | -43.61047 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59fc175e-e04d-3b69-9dab-18ee6e4e4609 | -10.75781 | -50.64221 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e2c7cb46-4f48-3339-9ca7-0b991c3cf6ca | -12.03855 | -46.53027 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 485074bf-b3c5-3997-b454-c202a4a5ac5c | -12.602 | -45.73288 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d6ff606-9b3c-3a8f-9c94-ada650fd6e57 | -11.50252 | -43.66126 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1960727-c815-3237-a5b3-cf0e3e30feac | -14.51525 | -47.35124 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56ecad54-6e7c-3a1a-a7a2-eca509e6f632 | -8.92756 | -54.44582 | 2025-09-15 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d341f609-f38e-3167-9727-7b4179a95269 | -16.35077 | -46.84278 | 2025-09-15 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23ec0752-0085-3360-b636-4d361e69d243 | -10.93723 | -45.50195 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d5a227-e63c-3063-bee7-e75fb4e4b0e6 | -13.89848 | -44.86802 | 2025-09-15 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db060501-637f-3e05-867c-e8e306e1a810 | -15.10354 | -52.4819 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a951343-edff-344a-82d0-d79ff28297a3 | -14.84663 | -45.50247 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbf6b661-2d35-3b06-8dee-a5c2cd66698e | -12.64666 | -47.93361 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c61847e-ef9e-31bd-b0fd-afb223f5e7a8 | -10.7233 | -44.77518 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d0e363c-929b-3c1e-8a7f-cadbd23e5275 | -10.17011 | -45.31828 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 644e1a30-a33b-393c-94fe-ea7aa04abe4d | -9.13748 | -46.96325 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcf8750c-cb5a-3bbd-8688-0c1833dec844 | -11.131 | -45.30637 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f7646ce-f528-3933-8d2b-d8c3d910834f | -12.17042 | -44.09331 | 2025-09-15 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f897898-2080-3cd1-948b-b5953cba1199 | -10.93778 | -45.49846 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b105bbb-97c8-3ea7-a656-484d0ef5b568 | -14.42978 | -53.36693 | 2025-09-15 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 505ebb55-6fd1-3030-a230-0063e2d14b6d | -17.34617 | -42.64193 | 2025-09-15 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bca3a643-af01-370b-9a36-fac2a42ed959 | -12.05285 | -46.54705 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4098f4cf-c6fa-3fe8-8883-b8738a05d623 | -12.63712 | -47.92821 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf715044-5c7b-31d9-9f34-536e0db89ad6 | -10.03353 | -45.30028 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcfb7d53-413c-3816-817b-83bd704809a8 | -14.13266 | -45.41237 | 2025-09-15 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9649f06a-df27-37e1-bd2b-c40ae938fb7a | -14.80186 | -51.61074 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d6928f90-ff56-30d2-a7e6-8f74318c3ff8 | -10.74445 | -44.76755 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14253e4c-0467-39d0-a4b1-89e352efb8e9 | -10.62719 | -46.24608 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fde2d24-c47c-33fa-96b3-14f0570a1e19 | -12.01461 | -46.66008 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 473bca9e-56be-3bed-ba05-c91849571421 | -17.3377 | -42.64587 | 2025-09-15 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a188c736-35ee-3863-9f47-eb3806766306 | -11.46598 | -43.57218 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8600a2e3-93d2-37ff-aeef-3a59a93ab888 | -11.08158 | -49.73475 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87d7e20d-4c15-324a-87a5-39343024bd11 | -14.20804 | -48.76548 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae502724-140d-39b2-b42c-c6515e7acf14 | -13.90247 | -48.31551 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4a5ed086-226a-3812-99b8-20682875e1fc | -9.45137 | -47.30359 | 2025-09-15 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a41c8ae-4497-3b39-84c5-5df80979345b | -11.48224 | -43.60656 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5de7eb6f-7895-3599-b395-ed271a07732b | -14.28252 | -46.12357 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3d8054d-4647-31d9-99b9-a63bdcdffa56 | -11.04151 | -41.90409 | 2025-09-15 04:21:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c7793985-87ec-330a-befd-1dd8ac08a16b | -10.15236 | -46.14785 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9918d0d-3edf-3d21-a500-e1067fd6cb54 | -12.42071 | -47.80476 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19c6a7ba-9c1a-369f-bd41-454d3cd1a070 | -10.88537 | -45.44361 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cf66666-43eb-3230-8270-afcd1bb11d67 | -13.1842 | -47.28698 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ec6ef3f-d73a-3c59-9e44-9443d3333731 | -14.80579 | -51.61147 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| da8562ac-09bb-3da6-9d26-32b084dc7175 | -10.63105 | -46.2431 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c892f2d-129e-30c2-a037-49d66abf566a | -10.68613 | -46.25914 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2971888-6ed1-30a9-9d55-3e749aa89419 | -11.0749 | -49.72895 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d440024-bf18-3c93-bebc-b36d6148fd19 | -9.1498 | -46.97272 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d9b603b-4dbb-3226-9824-8bb505648d44 | -12.64944 | -47.93788 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d972b256-cb50-320c-81b1-29d55fed8fe1 | -12.43542 | -46.88203 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
