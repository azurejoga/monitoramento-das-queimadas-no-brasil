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
| d9f928ea-3624-365b-a167-9bb0bb72272d | -8.6311 | -66.5101 | 2026-09-11 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a7030131-8b9f-302b-9c53-345ee5845685 | -5.9815 | -57.7672 | 2026-09-11 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 81e32d01-9b71-3dbb-ba51-05c990040d65 | -8.6311 | -66.5287 | 2026-09-11 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a5778c48-faa4-3232-9886-d622bcb0f644 | -13.3053 | -61.6721 | 2026-09-11 14:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| dc335991-6c97-3327-825d-fa52e7f1fff8 | -10.5286 | -51.3597 | 2026-09-11 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| e61e6f10-4dff-3374-b269-910a127628bd | -9.209 | -65.5803 | 2026-09-11 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e24eb16b-f525-3aa1-a238-9572c81ec94e | -9.0982 | -65.4904 | 2026-09-11 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7adf5ddf-4613-3820-8a8a-1b2a5a9c209d | -6.7075 | -45.4861 | 2026-09-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| de5ac2da-ccc2-3842-9cba-97ebe8d49dd1 | -10.5478 | -51.3367 | 2026-09-11 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 352.7 |
| 99f8c2b4-fa80-360d-aa2b-146484d91c87 | -9.6947 | -43.4217 | 2026-09-11 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 121.3 |
| 0554de9e-d913-31f8-9054-0ea4192c7f09 | -8.0934 | -54.8488 | 2026-09-11 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 51a1eab9-51f1-3666-8791-2059398c0733 | -9.9041 | -45.91 | 2026-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 317.6 |
| 7c58bbbd-3e03-3026-b19b-a1c77b5ee4a1 | -10.5475 | -51.3578 | 2026-09-11 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 476.8 |
| c6431e26-469c-34d2-8ab5-032ba39f9249 | -13.2682 | -61.5775 | 2026-09-11 14:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| a276eee4-4e30-3371-9aa3-404ebc67d44c | -9.8072 | -43.5246 | 2026-09-11 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 18765fbb-2265-34ab-b1e2-a0060f0ca2c0 | -1.7683 | -54.9513 | 2026-09-11 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6f083dc2-2a86-3884-af45-543a5100a34a | -10.2182 | -45.2111 | 2026-09-11 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| c1b2d17d-67bc-3b11-b317-fe46ec9a7fc7 | -6.4045 | -54.9842 | 2026-09-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 71ff150d-1455-3cac-9b0d-962607cbcd7e | -7.9645 | -43.9971 | 2026-09-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 579d52c5-bae8-3399-9b9b-2c9da2e11eae | -7.9834 | -43.9951 | 2026-09-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 7db6e034-aa15-3d48-8a41-38d2487c1163 | -12.169 | -64.1404 | 2026-09-11 14:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| bd044d44-341c-30f4-b349-3ef510118877 | -8.8361 | -62.489 | 2026-09-11 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c7749a36-1098-3f1f-a197-52fd87823c3a | -11.4026 | -43.935 | 2026-09-11 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| cacdb8c0-8c1b-3bb6-b764-3b893ec104d3 | -11.4021 | -43.9585 | 2026-09-11 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 6d20519f-fbf9-3433-abc2-514516d317c5 | -9.3663 | -49.3865 | 2026-09-11 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| b2f4becf-8450-3b73-98a6-793b030cbdd4 | -11.3513 | -45.7922 | 2026-09-11 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| fb4d0a52-4708-37e3-ab1e-51f6bd35b161 | -11.9547 | -49.7512 | 2026-09-11 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 42f9827c-d44a-376c-b0f3-4b0401d63188 | -6.2427 | -51.7146 | 2026-09-11 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8f22c077-06ee-3e1d-be26-85f63761f89e | -7.9831 | -44.0183 | 2026-09-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 4396f067-751d-3141-ab8d-79e5029006ef | -5.6313 | -51.6651 | 2026-09-11 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f416ba35-deab-3408-81ee-231851e69c8a | -6.1993 | -55.2739 | 2026-09-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 58a96422-9f20-38b3-beee-5a5ef0b2440e | -9.0982 | -65.4904 | 2026-09-11 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0e0c2f5b-8a0f-3f04-9b8f-1ab1e77ea43e | -9.8079 | -43.4775 | 2026-09-11 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 85cffeef-b753-35b0-99be-3286c36d19bb | -8.6496 | -66.5096 | 2026-09-11 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 671e9acb-f0ed-3539-afb5-b2d7eaf2e542 | -8.6311 | -66.5287 | 2026-09-11 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3e97c783-410c-368d-8715-f9582c4a8f25 | -15.038 | -48.4573 | 2026-09-11 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7ca558aa-5568-39a9-ba78-9cb938b7fa20 | -11.0434 | -49.6851 | 2026-09-11 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 32abab84-a97c-3663-b7ef-b4c314b7c624 | -13.2682 | -61.5775 | 2026-09-11 14:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f8d59177-c6b6-3081-94b3-e328c6bbeb95 | -9.209 | -65.5803 | 2026-09-11 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1bd3f2c7-7cb2-3cf1-98a3-c784a3b359b8 | -8.6311 | -66.5101 | 2026-09-11 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 24241b20-161a-3b6b-9bb3-4b8635fe5b27 | -9.9041 | -45.91 | 2026-09-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 253.9 |
| be9ebe25-a83a-30f1-9562-c78209011d8e | -9.3852 | -49.3847 | 2026-09-11 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 647c428d-4ea4-3975-907d-323fd3ebe8fb | -7.12 | -42.107 | 2026-09-11 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 131.7 |
| b6ade883-bec1-3eec-a0bb-ab26ea9f4c9e | -6.9182 | -55.637 | 2026-09-11 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 566d5b14-e70c-3f30-9531-1440d93e0007 | -9.3666 | -49.3649 | 2026-09-11 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 005326a8-7202-3244-8ac0-a961fb5a8fb3 | -10.5475 | -51.3578 | 2026-09-11 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 170.8 |
| e662a257-6f60-39a9-b64d-e03285c368fa | -8.0934 | -54.8488 | 2026-09-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| d342adce-dc31-3876-8d5a-2e46efe337de | -6.7263 | -45.4846 | 2026-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| b55b7aea-d3a9-33be-9222-977cf48bd34d | -14.5836 | -48.8409 | 2026-09-11 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 96854cf0-a5f4-312e-aa75-af14e4b1639e | -7.0242 | -59.2374 | 2026-09-11 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b641dfb3-4442-3c66-a51b-a409acb1a3d9 | -10.4722 | -51.3442 | 2026-09-11 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 10eda22d-7cb2-3a3f-9150-21f78569ad38 | -6.2707 | -52.9483 | 2026-09-11 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| da2516d6-2f57-3fc3-95b6-053455857d82 | -9.6947 | -43.4217 | 2026-09-11 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 153.8 |
| 18ec6faa-3c4c-36b7-b73e-010dbb2b6ef2 | -9.8075 | -43.5011 | 2026-09-11 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 618.8 |
| 53b96295-c714-344f-a464-c383c871ff32 | -8.0936 | -54.8286 | 2026-09-11 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 647f64bd-c7f3-38fc-bc34-85d6d19b32c7 | -6.2429 | -51.6939 | 2026-09-11 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d1e939de-0685-3b97-8c89-6fd8e9dbba84 | -5.6314 | -51.6444 | 2026-09-11 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f1e193fb-f138-3625-97c8-6267f41095f2 | -10.5478 | -51.3367 | 2026-09-11 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| e06605cf-35d3-3d4a-9072-7cb34d366cbf | -9.2276 | -65.5797 | 2026-09-11 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| bcbd16e0-bc3a-3de0-ad06-eb9da684eae6 | -13.249 | -61.5983 | 2026-09-11 14:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fbb0ac1b-33b0-3259-811c-53783b03804a | -6.7075 | -45.4861 | 2026-09-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 83f2cfcb-ae95-3259-bf74-c013388fc830 | -11.4606 | -47.266 | 2026-09-11 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| f32330bc-27b9-3773-854f-3be45a9a06ac | -11.417 | -51.416 | 2026-09-11 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| b05f863f-075e-363a-aa1c-494f935d2901 | -8.7254 | -62.3987 | 2026-09-11 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9f609948-a1af-3782-8ee9-359368162655 | -6.5004 | -47.5909 | 2026-09-11 14:50:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 272d85bd-7a74-39cd-994f-07b8f0ca8b52 | -9.1799 | -68.2194 | 2026-09-11 14:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 55e7d5cc-78c9-3d33-b475-ebcd7b053312 | -9.0982 | -65.4904 | 2026-09-11 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| df76cb57-8b2a-3d28-98a4-bca49f5b6730 | -10.2929 | -45.2932 | 2026-09-11 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 46401205-c228-31d3-b581-d23eb8753dd0 | -6.4045 | -54.9842 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| fd2469ad-0d3b-3614-a8a9-ec058dee8459 | -13.4198 | -51.3731 | 2026-09-11 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 2400d85d-4601-303b-ab89-2cbe8db8c5db | -8.9412 | -44.3995 | 2026-09-11 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| f6e794d7-b4ff-3ad4-a090-ae90f3951590 | -6.1993 | -55.2739 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 35e4ee10-f011-3e17-b840-c5d0e70dad2f | -11.3513 | -45.7922 | 2026-09-11 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 29f82012-5e96-3667-ac5f-acd4e562afe8 | -8.0748 | -54.8499 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 880e818c-ae4f-3ffe-b1ca-491bb5647d9f | -22.2645 | -55.8532 | 2026-09-11 14:50:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 511ed12e-cd39-33c6-b13c-14c209b3f103 | -6.2707 | -52.9483 | 2026-09-11 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ef664144-27ee-3611-831b-16655d74faff | -7.9645 | -43.9971 | 2026-09-11 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| f77da90b-20a3-3866-a0b7-d7e84ca2c8c8 | -6.1306 | -45.1244 | 2026-09-11 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| aaeeb952-3a3b-35e7-936b-9d11814c46c1 | -8.075 | -54.8298 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| dcd10f9d-d477-305d-a5d9-f0f9287d339b | -6.1308 | -45.1017 | 2026-09-11 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7d42d8ac-1772-311d-be0e-cdc2db44baa7 | -6.7263 | -45.4846 | 2026-09-11 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d7753706-fbf5-37b2-8e51-59ea8aefcf6e | -10.4722 | -51.3442 | 2026-09-11 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b9a99863-b9fe-3f1c-9cf9-3d86ca423587 | -9.8075 | -43.5011 | 2026-09-11 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 265.8 |
| bfa05c04-bca6-3292-a9e0-bb4c0d5a5900 | -8.8361 | -62.489 | 2026-09-11 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f3e4af35-c12f-3c8f-a75f-7875de89817e | -6.7648 | -59.4408 | 2026-09-11 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1dd2e250-26da-3eed-bc81-9f4f2e11bd1f | -9.0981 | -65.5091 | 2026-09-11 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0d7312e4-9fde-3b0b-b7ca-cd966e399118 | -8.6495 | -66.5282 | 2026-09-11 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fbc83cfd-824f-3f83-ab77-6934be18d292 | -12.1501 | -64.1414 | 2026-09-11 14:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8c3bc4fe-255c-32c9-bc8a-d7c567946e67 | -7.5553 | -45.1624 | 2026-09-11 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| cc90e8d6-bda6-3fd9-913b-9f4659d23576 | -8.0023 | -43.9931 | 2026-09-11 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 167a58ce-3ce8-3eaf-8625-6dbbcb96f1f5 | -13.2848 | -61.8287 | 2026-09-11 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 57dca540-9a38-3929-8662-aab487f23d3d | -6.2429 | -51.6939 | 2026-09-11 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 95d199e0-3dce-389a-b35d-a4e562bd7e7c | -5.3462 | -56.0256 | 2026-09-11 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 071c84c8-bcec-37fd-b444-77cccf3164d2 | -8.6496 | -66.5096 | 2026-09-11 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 479d2484-1be9-3121-8804-ab36ced82861 | -5.3646 | -56.0249 | 2026-09-11 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 799873e8-9326-3a8e-86fc-56992c25742c | -22.2649 | -55.8315 | 2026-09-11 14:50:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 154.5 |
| acb0ca02-a11e-3c50-8223-7c49566e4f80 | -1.7683 | -54.9513 | 2026-09-11 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2d887639-3fde-34ca-a691-ed5c31864f9f | -6.7075 | -45.4861 | 2026-09-11 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 9341dd43-9582-3a38-9d51-bd39c7537259 | -5.6594 | -45.5652 | 2026-09-11 14:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 10e28765-0f1c-37fd-af74-ff672c51cd89 | -6.1994 | -55.254 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |


[Clique aqui para ver as próximas entradas](README42.md)
