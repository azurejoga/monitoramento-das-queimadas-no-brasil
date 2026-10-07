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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ec53aa7-1766-33dc-89b5-f1d9a3a63efa | -14.90343 | -40.33407 | 2026-10-07 15:58:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 8bfd8ba1-4b7c-3dd4-80d5-3d9444ba895c | -14.3873 | -41.26889 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 52389e04-3fc8-360e-bcf1-cf07f14e3829 | -15.39669 | -41.70616 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 4e160f95-2310-3346-8c92-ef793211d980 | -18.38971 | -40.31659 | 2026-10-07 15:58:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| b911302d-b1b3-3d82-8029-be19ee668c4c | -17.74893 | -45.40245 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4de06260-f989-3728-87de-b47f32bde720 | -14.35176 | -41.27785 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 316.1 |
| 68d64515-b491-394c-9b59-775898207941 | -15.89024 | -40.72665 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 80f8209c-28cc-3a92-8c23-7ab7dc51b3ea | -16.05179 | -39.86077 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 49eb22d5-96b2-3b4d-863d-fd3627148cff | -15.3388 | -41.69733 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| f96ecfd0-20bf-3e92-9e7c-11e5f4d4efab | -16.16057 | -43.63063 | 2026-10-07 15:58:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb38e74b-762c-3a42-8850-373e67cb6e6e | -15.72071 | -42.62678 | 2026-10-07 15:58:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 0501b6d4-0fbf-3b9d-9efc-ff13fede350a | -14.1569 | -42.18478 | 2026-10-07 15:58:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 486a3d9f-ab78-3cf2-a999-816f57223eaa | -8.1035 | -70.1349 | 2026-10-07 16:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 4031938a-6308-3dd3-b0b4-55f95a405f21 | -1.4301 | -49.0382 | 2026-10-07 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| dd95ac2a-9669-35dd-a2a9-48c717de2cde | -6.1976 | -52.809 | 2026-10-07 16:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 30dc87e4-c93d-3f4e-b48d-797eb0cb422d | -8.5912 | -67.3084 | 2026-10-07 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d0be7022-6b6e-345f-a2fe-6f45a9cac598 | -9.6572 | -65.022 | 2026-10-07 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| fed65ac5-df96-3c42-9590-e6c560c17f0f | -9.5176 | -67.1173 | 2026-10-07 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 15aaaaf2-7dc5-3a4f-8192-b88887b4301f | -1.5118 | -54.8153 | 2026-10-07 16:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| b3678b0f-8434-378d-beaa-206f996deb4f | -8.868 | -67.4497 | 2026-10-07 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a2ee3e5e-9a78-3f6a-85be-203c30b03baa | -9.1408 | -64.3836 | 2026-10-07 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 376e8566-9b61-3141-b172-4a4f7868dba9 | -2.998 | -54.7492 | 2026-10-07 16:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d6e1369d-3085-319f-b175-ecd147a2b59c | -2.8899 | -54.0912 | 2026-10-07 16:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7e78d6fb-9632-3f1d-90bb-eb2b488034b6 | -11.0867 | -45.6459 | 2026-10-07 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| e0b73c8a-b7e2-31af-8c66-7f886d1f76a9 | -9.0889 | -67.759 | 2026-10-07 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 90250677-aa32-31a7-b908-f310fd338b49 | -1.3927 | -49.2727 | 2026-10-07 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 02de2011-3acd-3368-a690-8d26fa7f6345 | -11.1051 | -45.689 | 2026-10-07 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 23f0f1a5-21e7-3ec7-8daf-8bd6dc904742 | -0.3768 | -51.9947 | 2026-10-07 16:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 03a4e6ab-aeaf-3fc3-9b5c-9ca6486119eb | -11.0863 | -45.6688 | 2026-10-07 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 8011b97c-9541-3eb3-a0e3-d36ae93e2fb5 | 1.9134 | -55.7024 | 2026-10-07 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 30d1ce09-8b69-3be2-bebc-dce6144715d9 | -9.1253 | -67.9432 | 2026-10-07 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d5a41c1d-76db-3de2-8c85-b53e1fe7d185 | -7.9008 | -70.1928 | 2026-10-07 16:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 16db04bf-c4dc-3b99-a62f-ce559d5a47d4 | -12.1746 | -44.7051 | 2026-10-07 16:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 890d239d-12fc-3f1c-a500-b9dbecc3410b | 3.3971 | -51.3027 | 2026-10-07 16:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ceefd765-57de-33ae-a527-04568e7abf2a | -12.2132 | -44.6991 | 2026-10-07 16:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 265.1 |
| b3546ec3-c2b7-3225-8695-098a5996e4ea | -8.5918 | -67.1418 | 2026-10-07 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9c4d2326-fc1e-3797-840b-b597e147f0b0 | -9.6757 | -65.0401 | 2026-10-07 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1512a0e5-df6d-3264-9d52-9bf0516bc70c | -9.6419 | -68.6156 | 2026-10-07 16:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c4a37f06-0d7c-35c0-b543-964e99ac5350 | 1.8768 | -55.7227 | 2026-10-07 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 40259126-1d8b-3f87-833b-983cee4de857 | 1.8767 | -55.7424 | 2026-10-07 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 777d10e9-5b5f-324f-8c31-657d84a82722 | -12.1742 | -44.7284 | 2026-10-07 16:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| e5f8ddcc-fecf-3512-8696-d1c906823c40 | -3.8567 | -55.9769 | 2026-10-07 16:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 242.8 |
| d62be786-13bf-3867-ad12-0c5bfbd7eae6 | -1.5118 | -54.8352 | 2026-10-07 16:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 483a1bee-27b6-3856-8cc2-3949abc88186 | -11.14223 | -46.16992 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 875a4f3c-73b6-3bc4-a5fe-f94a0296568c | -8.76842 | -44.16232 | 2026-10-07 16:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 26c59d73-8891-34df-afee-053c011c1917 | -8.59039 | -44.86864 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 44be5434-1b5e-3c65-8caa-9fb0fd8fa5d7 | -12.2124 | -40.55849 | 2026-10-07 16:01:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 883626a4-7c36-3ac1-bc36-e982f7a313b0 | -11.06482 | -45.81153 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8c31d6ef-525b-379d-8a87-3fbc5349f652 | -11.23019 | -45.28136 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 87a83aed-17fa-382a-805f-ba7c3593397c | -11.64281 | -43.67176 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 44599d8c-c316-330c-a164-96f64c06bf3b | -11.23357 | -46.24887 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0c236aa9-3dd4-310d-8f62-205414c97466 | -8.39142 | -36.72847 | 2026-10-07 16:01:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e5f56a70-9566-336e-8335-f96e19313079 | -10.81041 | -46.58262 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f6202948-a1da-3b05-9782-f21a0ff4990c | -13.39254 | -43.87371 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ac5703da-17be-3dba-8987-58aaf56e3fcc | -12.81452 | -39.03083 | 2026-10-07 16:01:00 | NOAA-21 | MARAGOGIPE | BAHIA | Brasil | 2920601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f4240335-85cf-3952-8db7-433675d1ceb6 | -9.74041 | -48.18866 | 2026-10-07 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7e95fdf8-e547-3854-abff-a916cd5628e5 | -9.86634 | -46.30777 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6381f277-8888-39a9-a214-4f23ec646e4e | -11.70635 | -43.66491 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 759b98cc-2cd4-301f-951d-72a399e6b97d | -9.44198 | -45.81223 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8bc3a325-7d8e-34e9-83a8-51d40c61ceae | -14.58162 | -47.53308 | 2026-10-07 16:01:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8158ebff-50a6-37a2-a70e-39b0d3c61e59 | -11.73352 | -43.66148 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4220a3e3-6e76-35fc-b380-3d77051cbc73 | -10.77731 | -46.53905 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b28f1ef0-76de-35ac-87a2-e9b8282a282e | -8.29246 | -45.47244 | 2026-10-07 16:01:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c01cc46b-27c6-3f2e-b120-378af5f5b23d | -8.43105 | -35.75425 | 2026-10-07 16:01:00 | NOAA-21 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c5760a6f-1cc5-3a99-859f-caf6ffb783aa | -12.17286 | -44.74781 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 555.4 |
| ba0f516d-b0d9-3169-ad20-c833d5e11664 | -10.85723 | -50.65417 | 2026-10-07 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 11572ec6-3292-3671-9328-6842e7f0dc65 | -9.93612 | -45.72923 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ac68d562-47bc-3a5d-af45-e93d094b2ba8 | -12.21939 | -44.70158 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 5c77f143-e111-3816-8e0f-73dbbacd2f45 | -11.76441 | -45.50789 | 2026-10-07 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 254be4b4-9e05-32b0-932e-22571f3343dc | -9.96426 | -43.48491 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 5e96d9ef-eb0d-3808-930c-3e067f0ab939 | -8.11883 | -35.26254 | 2026-10-07 16:01:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 18a432a8-3e03-3a66-951f-544e452cffc4 | -9.87234 | -44.80278 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 06b9ac58-a1ab-30b6-bd00-1638293028a6 | -8.33777 | -44.73855 | 2026-10-07 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5080ecb4-cff0-333b-a667-ce0f87623bb0 | -8.70761 | -36.13395 | 2026-10-07 16:01:00 | NOAA-21 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9ebe348f-2ad9-3aa2-a2ca-1e92b284a871 | -9.81879 | -38.40498 | 2026-10-07 16:01:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 944bc042-35b4-3e25-9660-07b284a015d8 | -10.9955 | -45.47778 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 85c1344b-a981-34c4-9afe-8a36e967e701 | -10.99199 | -45.49056 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13d40c82-2b38-30c5-b3de-c5011640112b | -11.83458 | -47.34677 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 26c903ba-f6af-33d5-9d71-d659c9a4fa1e | -12.16304 | -44.70954 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a86e69d8-7017-33c6-aead-5b88553ce15a | -12.88065 | -47.65416 | 2026-10-07 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc3e203b-2e7f-362c-87b5-1f8d8ef055b2 | -10.87858 | -46.67348 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 702e47fa-c231-3bb9-96aa-b9716212af77 | -9.40637 | -45.89539 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0ebadd7e-9a60-3fbb-ab4e-4eed047fcb40 | -11.91436 | -50.65393 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| af2f149b-5bc8-3e93-926e-db797c8d1b4b | -8.45726 | -46.42116 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65ed1c28-5f8b-3729-899b-e80456deeefe | -11.73291 | -43.65689 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 61ea0748-8935-388a-afe9-cd059d0ebdd1 | -11.44056 | -45.56717 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8c303829-9351-37d9-9c9b-00d1e1d7ee89 | -9.44161 | -45.80944 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 65c5eefc-a67f-3e7f-8928-70876cacc237 | -12.16137 | -42.34847 | 2026-10-07 16:01:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| fa160b37-a41a-3dad-81bc-0ab35f32cb65 | -13.44515 | -43.45156 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ae2741bf-933b-3e2a-a8a3-6c4058043ec7 | -8.76394 | -44.16293 | 2026-10-07 16:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7a359aab-b35f-3c72-8dab-d5d393b04caa | -12.18972 | -44.76272 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 12dd3d7c-4734-3158-8339-54131f9e12c5 | -9.38029 | -45.93475 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d0a8362d-d243-3774-9e51-68c2a9b010eb | -11.32698 | -46.66957 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8f485cfb-4778-3b40-bcbd-93edb35ce005 | -11.80667 | -47.36325 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d843009-d9f8-3bbf-85dc-fe7c7462009e | -10.23212 | -46.66808 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dd0a7439-b66d-35bb-94e2-2004f5c7e90a | -10.88436 | -47.60172 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| d583c9ca-2c6d-3982-a9b8-e49216e34f4c | -13.33232 | -38.98448 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 123792b2-31be-32e1-acae-cd4163e2d3d5 | -14.75564 | -49.2596 | 2026-10-07 16:01:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| afb25068-7c37-3b53-a79d-95ac4eac3ac5 | -8.95262 | -45.1172 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 41db8575-f438-311a-be6a-379be2a7112f | -10.99221 | -45.41273 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README148.md)
