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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc726a82-80ef-33ba-a6f5-8718f07b0a35 | 1.8221 | -55.5456 | 2026-10-06 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e824f65b-dd6b-30de-8388-fc999961723b | -5.7321 | -41.6349 | 2026-10-06 17:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 171.4 |
| cfee1576-2ea7-3917-9135-4d25e68094e8 | -7.364 | -72.6079 | 2026-10-06 17:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 043e4281-ff49-3afe-8da1-52312d23efab | -9.1055 | -68.3135 | 2026-10-06 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 5e172376-0e8f-3233-9a3c-16e10ddb4b37 | -9.4115 | -65.9099 | 2026-10-06 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 889af17b-334d-3b34-87a1-89e4318eae81 | -9.2366 | -67.885 | 2026-10-06 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a6e30eca-fae1-3926-8c87-f5e10fd844d6 | 0.3221 | -51.0038 | 2026-10-06 17:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 73429715-297e-3d92-a003-1970e7fd6e0c | -9.1072 | -67.8326 | 2026-10-06 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7f00344f-bcf5-3f33-ba57-c8ba384deb43 | -9.1221 | -64.4031 | 2026-10-06 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| ff5a4497-b1d8-3095-a001-dc00d76d3bdf | -8.5733 | -67.1422 | 2026-10-06 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9abfaa04-db8d-32d6-b44a-995de44840a6 | 1.9132 | -55.8011 | 2026-10-06 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 978ddf2f-60a8-3609-99fb-85d77d6526d7 | -11.6579 | -43.5899 | 2026-10-06 17:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 4ff64e2d-6036-3a39-8f36-74bc04fc7b32 | -7.2718 | -73.0089 | 2026-10-06 17:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ccb7ab0d-093f-3a73-bc78-d22571fa38f8 | 1.8221 | -55.5456 | 2026-10-06 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1c6b73f3-f82a-3220-8ccb-3e09cae1d3a8 | -9.1253 | -67.9432 | 2026-10-06 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 56f0cf69-eeeb-341b-a1a2-cffbaaed5146 | -9.1076 | -67.7215 | 2026-10-06 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| abf1fe89-2bd0-3c85-9b02-728532583aa7 | -8.5554 | -66.9945 | 2026-10-06 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 289264cd-7472-3960-86db-dc1e5bc46ed2 | -9.95 | -43.56 | 2026-10-06 17:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23c3da38-08f7-353b-9dcc-28b4916f75e6 | -5.76 | -45.19 | 2026-10-06 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e27ceb59-7356-3959-b5e1-326a650c3043 | -3.2 | -50.53 | 2026-10-06 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e19e7a40-6656-3c02-ad37-889799780dd9 | -12.19 | -44.73 | 2026-10-06 17:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 810d9a56-bba6-3e48-9d89-778f42f4ab93 | -9.95 | -43.65 | 2026-10-06 17:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a78eff4-10e9-3f91-9196-7d85636fd0ac | -3.96 | -44.03 | 2026-10-06 17:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 940b9b04-e9aa-31d8-843c-2687d31d647a | -5.76 | -45.14 | 2026-10-06 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa138afb-3005-389b-90f7-38727d6e0933 | -3.42 | -44.49 | 2026-10-06 17:15:00 | MSG-03 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89b52c57-2c6a-3394-88d4-afee075c44b4 | -3.2 | -50.59 | 2026-10-06 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbe0e68e-eee2-3421-9099-a50220007c63 | -7.86 | -44.21 | 2026-10-06 17:15:00 | MSG-03 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a1fd7b33-c750-3f82-81ab-3125519d2353 | -7.86 | -44.16 | 2026-10-06 17:15:00 | MSG-03 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0b0627-8d8d-38ed-80e6-70c6f8cadfc9 | -6.73 | -45.79 | 2026-10-06 17:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afac9899-c719-3438-b51d-2c0b0f9102db | -15.61 | -41.68 | 2026-10-06 17:15:00 | MSG-03 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1ef06f9-d352-37f4-8609-a956b298aedc | -3.29 | -54.01 | 2026-10-06 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18917d5f-7c11-36e4-91b4-9a31846f6475 | -9.95 | -43.6 | 2026-10-06 17:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74e37f3e-4996-39f1-b689-dfdb3f8a7223 | -5.73 | -45.18 | 2026-10-06 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4338aa73-c42e-3f15-9a56-207ed8bd8b15 | -5.72 | -41.66 | 2026-10-06 17:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 145152f1-8a6a-38e5-84bd-972ff78587fc | -5.73 | -45.14 | 2026-10-06 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b24394f9-6e89-3c96-b116-826fc88dd71b | -3.08 | -54.24 | 2026-10-06 17:15:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2dc61b2-f0d7-38de-ab23-f0f3c02f5bbd | -3.5 | -54.6 | 2026-10-06 17:15:00 | MSG-03 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc801a6b-bd63-3774-8b09-8f941afd696a | -3.42 | -44.44 | 2026-10-06 17:15:00 | MSG-03 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5372de83-bedd-3e0a-bf03-4f5115242923 | -3.17 | -50.53 | 2026-10-06 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07684195-6605-36e7-b248-9da739914df6 | -9.95 | -43.69 | 2026-10-06 17:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a0a9aa8-fa4b-388f-a265-b411589828ca | -3.11 | -53.75 | 2026-10-06 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d423f53-a278-3c42-8d19-6d2a02ca9f05 | 2.4584 | -50.8507 | 2026-10-06 17:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 51125ffa-45f5-38a5-ba1a-ec220bcc36e3 | -9.4819 | -66.7836 | 2026-10-06 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ad7396b4-aa91-335e-850d-438234f2010e | -11.6382 | -43.6166 | 2026-10-06 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 544c01ed-30f0-323f-a848-88d3005d0056 | -8.5367 | -67.0505 | 2026-10-06 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a99ca72a-7875-3ad2-a90e-916d58bfc9c1 | -9.1256 | -67.8507 | 2026-10-06 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 95a08ac2-805b-38f6-b20b-d834237d17f7 | -9.1261 | -67.7211 | 2026-10-06 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 10d4fecf-70e4-3f5f-a609-30a87ba911d8 | 0.3221 | -51.0038 | 2026-10-06 17:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1bd3002a-c865-3062-9a7e-f66035a1eef0 | -8.6292 | -67.0111 | 2026-10-06 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 263b4295-78ab-3d0a-a7b8-e6f0894556b4 | -11.657 | -43.6373 | 2026-10-06 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.7 |
| 782255f0-5b2a-3320-8d2a-647406860ba1 | -11.6378 | -43.6403 | 2026-10-06 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 1f831a23-d94d-3e79-a838-5a4358c1bc15 | -9.2366 | -67.885 | 2026-10-06 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 312831d0-6f4e-35d4-baf8-e6c8425b4d9f | -7.2718 | -73.0089 | 2026-10-06 17:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b816cd5a-e74f-3c4f-b5d1-51e9ee904d66 | -9.1072 | -67.8326 | 2026-10-06 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 40fb4f84-3fa4-3cd7-b1e7-34d7666decab | 1.8038 | -55.5458 | 2026-10-06 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0ce6a424-8e06-3529-8749-6e8e63887c22 | -9.5006 | -66.7459 | 2026-10-06 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 3db8f643-7b25-3f34-b937-1776a4b4468e | -9.1055 | -68.3135 | 2026-10-06 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 2b2026e7-699a-3f21-8f2f-cdc853ac3ef7 | -6.7066 | -45.5765 | 2026-10-06 17:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 443.3 |
| c503412a-e609-38dc-9a99-fac832be8b58 | -7.364 | -72.6079 | 2026-10-06 17:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 38b8bfd1-a9f8-38e2-95e8-15fb26f3cd17 | -8.8371 | -72.7437 | 2026-10-06 17:20:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 9e2a12b7-81f6-34c9-94b8-e6994c75353b | -9.2365 | -67.9035 | 2026-10-06 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 21b08004-493b-3652-b396-fcf694bd9faa | -9.1072 | -67.8326 | 2026-10-06 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 071c4104-7e1c-3a9f-8a4f-18c5470d70a6 | -7.6949 | -72.4235 | 2026-10-06 17:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 4c555995-6664-3ca1-98f5-b2892bf3ada1 | -5.7321 | -41.6349 | 2026-10-06 17:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 199.8 |
| 1b7ae334-5a58-3d9b-b8c3-f49843998e07 | 1.8038 | -55.5458 | 2026-10-06 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ad761284-83fc-35ae-b813-1df46a061527 | -9.5468 | -64.8196 | 2026-10-06 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 289.5 |
| e05fe262-c33b-3b34-afdf-aca9b78c25ae | -7.2721 | -72.6995 | 2026-10-06 17:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5556f381-d209-31d0-b4f3-f975548470cd | -8.6159 | -72.3798 | 2026-10-06 17:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9267e90e-1037-3c51-aa40-abe25d6bfb32 | 1.8221 | -55.5456 | 2026-10-06 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 26e86593-bcc6-31ad-a688-817ac15d5fdb | -11.6758 | -43.658 | 2026-10-06 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a13237d1-0d1a-375e-bc31-990ddfaca8e7 | -9.7881 | -44.7828 | 2026-10-06 17:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 3bef8a0c-73be-3157-afed-4549089a51e0 | -8.5554 | -66.9945 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 1b4c6249-1d20-35eb-a297-8d41a3066546 | -9.1256 | -67.8507 | 2026-10-06 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 40d5627b-1e13-32cc-9238-935b38d0ec3d | -8.537 | -66.9764 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| a882ef30-bdb9-35e4-8519-8bf4c60267df | 2.4585 | -50.8299 | 2026-10-06 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 0f8e9b20-774a-3fe2-ab9e-3fe8a4072188 | -9.5467 | -64.8384 | 2026-10-06 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 53faea01-2199-3505-85dd-40d625731019 | -9.0045 | -65.7174 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 4e66060c-77a2-3b5e-848e-42baded0f356 | -11.4695 | -43.4062 | 2026-10-06 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 0a0f1158-018b-3c01-a9b4-76a9212877af | -11.0856 | -45.7145 | 2026-10-06 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 749043a8-1dd3-35a9-a3d7-c60e08977d5a | -7.364 | -72.6079 | 2026-10-06 17:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3201bcdd-860c-32f0-b08a-638d15a66e01 | -11.3367 | -46.6773 | 2026-10-06 17:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b3a44529-847f-33ff-9667-5e4eb98570fb | -7.8606 | -72.3311 | 2026-10-06 17:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 37358a35-b588-3931-8113-9a30bf094446 | -9.3447 | -68.7884 | 2026-10-06 17:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 47517481-4bb0-349e-9603-288a15d04389 | -9.1441 | -67.8502 | 2026-10-06 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| c77c3916-32c3-35af-9f4f-ca50e8a6290d | 1.6202 | -55.7852 | 2026-10-06 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0e5a4071-f57d-3150-b0b5-2d2741d08a6c | -7.2718 | -73.0089 | 2026-10-06 17:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 94f7b30e-f5d9-304e-b719-c277012c0518 | -8.7324 | -69.4271 | 2026-10-06 17:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 73.1 |
| dda11e33-edf8-34c3-850b-93669747a313 | -11.6382 | -43.6166 | 2026-10-06 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 7735aa94-8294-3c0f-b557-c23ccf599f3e | -9.1334 | -65.9 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 8cc44542-ab2a-3f59-bc31-baf170c31c47 | -9.0889 | -67.759 | 2026-10-06 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d5c44510-fee4-3603-90f9-978867765e3d | 1.7304 | -55.6259 | 2026-10-06 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 138f578c-2989-3c68-87e4-aff7c49cb6f6 | -8.5554 | -66.9759 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| ddaa6833-6116-3677-845f-eef9719ecc9d | -9.1333 | -65.9186 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 690f76ae-1c08-38bd-ad63-9fc2737549d3 | -7.6765 | -72.4236 | 2026-10-06 17:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3233012a-73b7-3215-90f7-0797256159de | -9.2366 | -67.885 | 2026-10-06 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| fdf5b10d-a2e5-3e7a-a3d0-9bba7434387b | -8.5368 | -67.0135 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b9d68775-48e6-3d12-9644-5f368d3357aa | -9.1257 | -67.8137 | 2026-10-06 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1ead6525-b4d9-39cf-9acc-970e19ef4096 | -11.4503 | -43.4091 | 2026-10-06 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 7f0d91b5-c0b4-32aa-9d15-1f3e872e6f53 | -6.5608 | -69.8266 | 2026-10-06 17:30:00 | GOES-19 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7b9d3ec2-8b8c-39b4-a6e5-79a464e749b5 | -11.657 | -43.6373 | 2026-10-06 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 384.6 |


[Clique aqui para ver as próximas entradas](README95.md)
