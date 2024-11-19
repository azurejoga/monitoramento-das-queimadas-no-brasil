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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0489024-a3e6-3143-aeb1-24750bcc1755 | -23.97067 | -54.13469 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 743197fe-db79-3755-af43-dd2275db5d9b | -22.30714 | -49.76392 | 2024-11-19 05:14:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d3967634-d6eb-3caa-87ab-d37e94a78131 | -23.96907 | -54.14955 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 09a7d674-6834-3120-ae51-bc425d965e99 | -22.30677 | -49.7682 | 2024-11-19 05:14:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0704da5f-3b1a-3d74-a6df-17c94ab2b06e | -23.97415 | -54.1452 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 54f37798-7674-3dac-9d5b-da837883e354 | -23.97468 | -54.14025 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 50d26a8e-c632-3212-b07a-435bb0f4ce53 | -23.95403 | -54.11739 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 45499ef8-dba6-30d6-9756-946dac078eea | -23.96664 | -54.12913 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9d0eddfc-efef-3324-83d5-e0da567d47a7 | -23.96262 | -54.12356 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 81e1ed54-2b5f-3174-8e42-b6862be8c260 | -5.9788 | -45.3621 | 2024-11-19 05:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 43417953-5c73-35ff-be82-9f568361ddbc | -5.9788 | -45.3621 | 2024-11-19 05:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 95823447-30c9-3cbc-8d43-477b9c503cf3 | -4.5429 | -48.0151 | 2024-11-19 05:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| d78efbb1-5546-32a4-8551-e6329551e633 | -4.5614 | -48.0141 | 2024-11-19 05:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 7dc09c1d-c4a6-3268-8db0-6da7fa4cc1a4 | -1.51945 | -60.32965 | 2024-11-19 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2097c7de-7773-33f6-8f03-148c0379330f | -2.76405 | -52.60601 | 2024-11-19 05:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70522994-242e-3156-b796-4229af66035c | -3.04371 | -54.40186 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 101aeecf-74a9-3a7d-9eb4-8f3781ea3dbf | 1.18804 | -60.22195 | 2024-11-19 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb3a4135-c910-325d-a0ee-9247cee50793 | -3.18773 | -53.24308 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d75881a-e369-3c41-aa2c-49432212981b | -2.84981 | -54.0112 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03e9a518-4d05-3ba7-98f7-5895cdea24a6 | -1.70472 | -52.15069 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 320582dc-3d1e-3f44-a775-fd961026105a | -2.85028 | -54.00799 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ec81760-8338-33a2-a505-33f749e00aa2 | -2.60854 | -54.54053 | 2024-11-19 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecbf31db-915e-3042-acfd-d940cc6a0f7e | -2.58795 | -51.72056 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f62a007-c17d-3b7e-892c-dbf6b33ddc66 | -1.20427 | -51.77387 | 2024-11-19 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d1060a0-f89e-3ec4-8b50-25b69ee4e492 | -3.66325 | -50.44822 | 2024-11-19 05:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b850688c-a303-3da7-83da-0e902c38a637 | -1.14281 | -51.6974 | 2024-11-19 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d3b61c5-17b0-3e92-8078-d3cbbd3faaa4 | -0.85416 | -48.75188 | 2024-11-19 05:31:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 424313b2-f99e-3b1a-9e49-6fe4964494a5 | -1.24942 | -52.05775 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc858e88-ac0a-3e11-9494-a5b26f7336c6 | -3.36507 | -50.82726 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29cba684-e37f-397e-8f40-0675a0e1cd5b | -2.90014 | -53.0534 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cf63cba-c0d9-3f29-b76b-1b3a0bb885bf | -1.37605 | -52.08396 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35859db9-80b8-3b5c-9b1e-e31c19fc1078 | -0.94333 | -51.7253 | 2024-11-19 05:31:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99b2b9ca-13c4-3d16-a2b6-a2ec2f8322de | -3.20339 | -52.44324 | 2024-11-19 05:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4182ab6c-ff1e-3fd5-ac39-3a5cfd22103c | -2.68722 | -51.81009 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b511ea54-67ca-3e88-b807-17b286c7c5f7 | -3.06932 | -53.28127 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82645ab0-e13f-336e-b4ec-0be7144add40 | -1.20562 | -51.76514 | 2024-11-19 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46d9133e-79de-3e34-a158-7f199d489a82 | -3.04089 | -49.47652 | 2024-11-19 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36c8e166-499b-3c4c-a62b-056330382ac9 | -0.93257 | -52.49965 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03d673a4-6731-36e3-9083-84ed441c4719 | -2.61358 | -54.54135 | 2024-11-19 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b6b38ef-e8f7-3c0b-af27-320d2f27098f | -2.76986 | -52.60656 | 2024-11-19 05:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53547ef9-78b3-3e8a-bdf7-a7b073633197 | -1.59209 | -53.80951 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5046a5b-05f1-38d5-9f98-c4e7d7c17bfa | -3.51527 | -53.80059 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34c47f0b-8b96-3f9f-a9e9-10f596391ade | -2.42729 | -54.62009 | 2024-11-19 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e06a919-e99a-3530-a3c6-764dcf97dfbe | -0.94927 | -51.72622 | 2024-11-19 05:31:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e431b73-bbd6-3dba-8688-8d2a0478235f | -1.58217 | -53.80015 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c411cf0f-7d48-3282-af07-168c53cc96b0 | -1.29933 | -52.23291 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e4c1e26-d400-3720-be00-aa31336b4e82 | -3.71607 | -51.84743 | 2024-11-19 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f95e5b39-1106-3b91-8f19-060c520a1a59 | -2.86608 | -51.79068 | 2024-11-19 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 138cf5d4-2996-311b-b726-8f1df31138d8 | -2.77048 | -52.60238 | 2024-11-19 05:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| effdaa19-4fbc-31eb-b3cf-d588b2c20265 | 1.18464 | -60.22248 | 2024-11-19 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f98924f-511c-36ec-b97f-bdb32367bb63 | -3.1088 | -53.74439 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9666f6ca-cd25-3496-8a0b-d2e3fb72c03e | -3.51576 | -53.79737 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef58d139-2ff9-315d-bbfb-282ef125cf15 | 1.18861 | -60.2256 | 2024-11-19 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf4d0a24-c4a9-3f4e-8ee1-d31e86ced314 | -3.3142 | -54.17096 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2899713-39b3-38e9-9d49-5ef36bd0d384 | -3.98408 | -49.91691 | 2024-11-19 05:31:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e21b4eab-0def-3570-9de1-69b46086bc36 | -3.36719 | -54.10439 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f131308-c0a2-392a-b74b-4d4a37be2804 | -2.787 | -54.07086 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aa783c0-e679-3d9a-bb80-8bad1f04e351 | -3.65999 | -50.447 | 2024-11-19 05:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1715100d-205f-3546-a58f-0027c83c242f | -1.20359 | -51.77823 | 2024-11-19 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd15c2ff-2017-353e-9fc8-c8f4a0c0e335 | -3.59818 | -53.99792 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7def0df7-53a4-3b75-9c73-6d01f48bbf97 | -0.95521 | -51.72713 | 2024-11-19 05:31:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 89ac0201-df4b-35d5-944f-17607647adf9 | -3.71061 | -51.8418 | 2024-11-19 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d86e1f7-9622-324b-9aa9-3edda972b948 | -1.64018 | -52.67776 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ba40330-33a2-3c7e-bdfb-e53907f4bded | -1.07486 | -53.36845 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93227797-1499-3a4d-97d3-1b544923242d | -3.55499 | -51.53244 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05672984-3771-3b0d-a515-cbc7c3dd0ff7 | -1.62508 | -55.1467 | 2024-11-19 05:31:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9d786ce-13c3-37fe-a0ee-0478899560f5 | -3.06823 | -53.28873 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f9ae13-70a4-32e7-9af3-6e0154eeae4c | -3.04838 | -54.40572 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| effbfdb4-b332-3b68-bce4-32a78f119d04 | -2.21728 | -53.7934 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f0befd7-de92-391c-b7d5-752387c3e4d7 | -3.34089 | -53.31367 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a49931e3-3fea-3f14-ad9c-510035e2644e | -2.6637 | -51.71751 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 353bf7f1-18b8-3cd8-a347-1b2e647e1786 | -2.36759 | -53.68113 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54d3889f-b4db-3433-a0fb-5ab8b9d55c35 | -3.06424 | -53.28111 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdadc580-140e-3d35-969c-4c2e00b7e21d | -3.10293 | -53.74696 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0b6c62c-0c48-3635-bdc6-58f7b9692535 | -1.25006 | -52.0536 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ee5692c0-adbe-3820-ae42-6db550eb4529 | -1.58165 | -53.80342 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b5c5d43-23ee-3596-a80c-cb152be1bba0 | -3.36588 | -50.82168 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20b74541-48ea-37b2-997e-1fc2aba5b768 | -1.58782 | -53.80233 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24e0fe4d-757d-3178-8bf1-d55bfc6264ed | -2.77633 | -52.60265 | 2024-11-19 05:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2edeef10-5d35-39bb-925d-c85bd1927f5e | -1.42259 | -52.43777 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 87588c73-ff83-3a44-9a33-d0a4d3afbc45 | -1.33721 | -56.03582 | 2024-11-19 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7646047b-8c8f-3206-8ad9-04d18980da9e | -3.1078 | -53.75117 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0a425d7-c7a2-3f2f-b464-3aa2949cadc7 | -1.39518 | -52.42592 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a579c2d-529e-3ac7-a0bc-aa99dddc05d6 | -3.18103 | -53.25007 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 607e5fe9-0cad-34c5-b797-b3d98fcce03d | -1.24485 | -52.04856 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10d65f6f-aea9-39d7-a99e-d804654774ad | -3.59867 | -53.99468 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b57309e-c4f7-3ce3-98ea-a069518556a8 | -3.06367 | -53.28484 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0323eeaa-4c98-3249-a537-413d993e051c | -3.05812 | -54.41064 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0094a48c-c130-3d02-9760-1f0afe0634e2 | -1.9501 | -54.45791 | 2024-11-19 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78619331-53eb-32d7-8296-c2fd8f28dba7 | -1.43289 | -53.3838 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b82efe-d358-30ea-af4c-0a7d6fdd5e61 | -3.09921 | -51.31975 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d6dc260-31a6-3ff5-b86e-6366750d2758 | -1.92421 | -54.05832 | 2024-11-19 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 512cb8d6-f173-3249-95f3-cdbe03ccf59e | -1.5869 | -53.8041 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e232e088-2960-3d37-9b66-3de184b51362 | -1.70534 | -52.14664 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ada289-74a4-30fb-a55f-2d4075ee00e5 | -1.58685 | -53.8088 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 043a9e4e-4991-33fb-a029-dcf3be9f15dd | -1.63765 | -52.67648 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c2b0909-6d34-3df4-bddc-651cb53a2856 | -1.53615 | -60.33612 | 2024-11-19 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea40c2e9-66bd-3516-afd8-8daf3ab0d6db | -2.58726 | -51.72515 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 628569a4-acda-301a-a064-1b70e249063c | -3.04884 | -54.40265 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d38f1581-fcd5-3085-abc1-3a69cd4a00ee | -2.95894 | -51.41684 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README47.md)
