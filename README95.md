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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13990023-f538-3045-99fb-0b3a9197cd54 | -8.5367 | -67.0505 | 2026-10-06 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c984ecf6-2b4c-3042-b23a-d2a74291042f | -11.6579 | -43.5899 | 2026-10-06 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 4dc9ec62-109d-304e-9d11-a98fe4278a78 | -7.0164 | -71.609 | 2026-10-06 17:30:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 27598eed-962c-3ed0-aba9-b0e84e56bd80 | -11.4503 | -43.4091 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 629fd3a5-cb54-3b04-9b9c-6b77ca2f7006 | -7.8167 | -45.3193 | 2026-10-06 17:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 403.9 |
| a39e3d8e-aab1-3852-8a57-29624157b5aa | 1.8221 | -55.5456 | 2026-10-06 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0bb99be5-f013-3f91-aff1-8c246e625074 | -9.4633 | -66.7842 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 024f1023-dad4-3bbf-a439-6f3c4e05c5c2 | -7.817 | -45.2966 | 2026-10-06 17:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 14809ee3-43cd-3dbb-a421-11f073411160 | -9.7881 | -44.7828 | 2026-10-06 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 59c17b21-b2c1-37d2-9452-2bd75a049734 | -9.1076 | -67.703 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| deacc5a8-7853-31ca-8817-4db356b6fa0b | -11.0485 | -45.6511 | 2026-10-06 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 81bd17fe-1839-3dc8-912f-5b0404ed3a42 | -9.0889 | -67.759 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 109f4e63-acf1-3f39-9a40-8298929f1eee | -8.901 | -68.6502 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| c356f66b-2df9-3bc7-9933-d169ae8a4994 | -9.1055 | -68.3135 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 51e6750a-0251-3b91-b8ee-f6e418870395 | -11.47 | -43.3824 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| ba556ede-4855-3513-9527-368fb6948a53 | -9.5468 | -64.8196 | 2026-10-06 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 257.7 |
| e3dbc717-957b-3499-b426-c766d09a0d72 | 1.4922 | -55.688 | 2026-10-06 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 3cf77716-7781-36fe-96f2-70adb9a9a57f | -9.0045 | -65.7174 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| ee6e0f8b-0f32-3a3b-8b2d-e1941a9d243c | -7.5332 | -70.0148 | 2026-10-06 17:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| f987ef34-b779-3edb-af29-065989af4836 | -11.6387 | -43.5929 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| f91387be-c1af-3a47-96d5-da691bed6d5c | -9.2366 | -67.885 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| f1b672c0-fe06-3843-a69b-cd976b420e32 | -10.1783 | -69.3249 | 2026-10-06 17:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e6a567b1-03ea-3e58-9c0e-75d80410e097 | 1.7304 | -55.6259 | 2026-10-06 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ce523a39-d214-37c2-b3f0-63d2b9766703 | -9.4421 | -67.435 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c7ff0ff3-585d-3b9f-879a-3fa2f3384430 | -11.6382 | -43.6166 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 296.8 |
| 1b85da60-d4f6-3253-8c2e-dad5c7fdc526 | -11.2267 | -45.2604 | 2026-10-06 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1976f795-261d-3481-a4cf-42cafd82464e | -10.1793 | -69.0104 | 2026-10-06 17:40:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 88.3 |
| cc62e56b-4117-3d6b-b494-21d8e025b781 | -8.5367 | -67.0505 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| de6dbfce-2280-39ee-b794-c660bbf83cb7 | -9.1068 | -67.9437 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 492c1d9e-8b66-38fe-bdb6-b5b06313c220 | -8.5367 | -67.032 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ba52af9b-3ce6-3e02-a4ac-7b27c2d34a13 | -11.6575 | -43.6136 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 420.5 |
| 0acffb76-9b35-341a-835b-94176ea9cf00 | -8.845 | -68.7989 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| d9850a25-17ac-3c7d-a260-67a0083c3112 | -11.3558 | -46.6748 | 2026-10-06 17:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| bc84720d-46af-3ad9-b421-7ac9a1a826b5 | 1.7854 | -55.5856 | 2026-10-06 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c9c2726c-60f6-3724-97ed-e2a6d4b11d64 | -7.5332 | -70.0331 | 2026-10-06 17:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 97ac16e5-884b-33c2-a1d7-bcbcb747ceee | -9.1253 | -67.9432 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3cf9d7f7-5475-323a-a21c-08e4ccad9534 | -7.9913 | -70.9967 | 2026-10-06 17:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 278fe9d6-c592-3f02-8374-6ac1befb0703 | -8.6109 | -66.956 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| af1c7968-c70a-3acd-a319-f8aeba5c3faf | -9.8638 | -44.7964 | 2026-10-06 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6c2068fa-8feb-32f6-83ce-d8fa30af2f0d | -9.1261 | -67.7026 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 48b2ea8c-b06c-3afb-9f07-2431dc4cd230 | -5.7321 | -41.6349 | 2026-10-06 17:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| aa014225-aa92-3987-8c02-9b7fa4c96cd4 | -9.1441 | -67.8502 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 717205b1-e189-31d0-bad7-282eac4542bd | -11.4507 | -43.3854 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 3e0f351c-11b8-35c9-bb02-efa487d40906 | 2.0713 | -50.8799 | 2026-10-06 17:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 5d1c9df4-d0f5-3b74-85c0-fe29a0026caf | -11.657 | -43.6373 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 03298814-0e91-3295-8b03-44e8717a10c3 | -9.1256 | -67.8507 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 4a435783-2076-3a58-ad27-a5a8c7773d25 | -11.6378 | -43.6403 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| ea2f5e8f-695b-399c-b48a-db27de0f81a2 | -9.1259 | -67.7766 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a603c2d7-9ffc-3eb1-bfb6-3a29b3712e22 | -6.5425 | -69.8085 | 2026-10-06 17:40:00 | GOES-19 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| f76a7025-3602-39a2-a253-e3da148205f5 | -11.6579 | -43.5899 | 2026-10-06 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 8aa54d48-b2f2-3bbe-b462-c79c31f9b784 | -9.7317 | -65.0006 | 2026-10-06 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 2a287845-0b2e-3aa6-b847-1938a27e9cb4 | 3.5263 | -51.2778 | 2026-10-06 17:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2f0c7a1c-8da1-3324-a2c7-73d326fce3c1 | -9.4819 | -66.7836 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 370da705-c141-36ba-86b0-ba47415cbe9b | -8.6664 | -66.9545 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| da31300e-cda8-323f-a1cd-98516e41e0c5 | -8.573 | -67.2163 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 6382eab3-02cb-32a7-a856-b84641ccd8d8 | -8.7816 | -72.7807 | 2026-10-06 17:40:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 66.0 |
| af7f18eb-ab7e-3a63-98fb-bea8857986ae | -8.8709 | -66.6707 | 2026-10-06 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| db843cfe-88dd-3a72-b0db-14e56854e0cb | -9.1072 | -67.8326 | 2026-10-06 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| cf84773c-8cce-3b16-947f-53d469cc8b30 | 2.4585 | -50.8299 | 2026-10-06 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 0a5dccee-ef77-3b99-b651-efecf0d3a981 | -7.8496 | -44.1478 | 2026-10-06 17:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 0b01e9eb-43af-3fe3-a1dc-09d4107a820f | -9.1442 | -67.8317 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 435a5c97-aafe-3241-a8a1-080ec72374d5 | -9.4435 | -67.1008 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.8 |
| c8a6d9e7-d9bc-33c7-9d8e-1165375fb3be | -9.1068 | -67.9437 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 76ac79c5-c7c1-3d99-8e1d-73b656899cd6 | 2.4585 | -50.8299 | 2026-10-06 17:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 03bff651-7a95-3002-86da-17c9b034c5c8 | -9.5468 | -64.8196 | 2026-10-06 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 208.2 |
| 238300b0-d502-3271-bb2a-c560f41de50c | -9.1259 | -67.7766 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 30983c04-72df-39c5-8838-5f143e5f1bfb | -11.6382 | -43.6166 | 2026-10-06 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 77ce9b36-30d2-3c10-a30b-dbdeec993868 | -9.1256 | -67.8507 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 9b82d131-aaed-3ec6-882e-3af46aea4f90 | -8.9188 | -68.8711 | 2026-10-06 17:50:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 864dee71-db06-38ec-af69-5bcd3db4f38b | -9.4622 | -67.0631 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e18a52c1-0c53-3e83-a6fd-7a5d03d3bef8 | 1.8038 | -55.5458 | 2026-10-06 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0d0808ba-ae12-3a62-b966-05aaec6af025 | -8.5367 | -67.0505 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 4f5d1f10-7a53-3120-a495-57389e2d53c3 | -9.9175 | -65.0313 | 2026-10-06 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.3 |
| f38e19c5-bf77-38b4-9318-8f13d3aa11ac | -11.8216 | -47.3521 | 2026-10-06 17:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| d752fca2-beb3-3a5d-be40-c26355fef3e4 | -4.1761 | -44.2716 | 2026-10-06 17:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| f0d0b8bc-13da-3556-a17c-8b9fc699fc47 | -9.7881 | -44.7828 | 2026-10-06 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| cec8e0b2-f920-3417-a451-d2cfcccc1d61 | -9.1072 | -67.8326 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| fec746ec-78b9-36ff-82ff-22b548349ccd | -11.6575 | -43.6136 | 2026-10-06 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 53cd0366-531d-3310-90b2-e56b6e83fc30 | -9.1895 | -65.7863 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8c426bc0-7501-3fc9-a916-e0cbc8c37297 | -8.9964 | -67.7613 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 73b9c513-da86-39dd-ad5d-8c4e6a0ac3d2 | -5.7321 | -41.6349 | 2026-10-06 17:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 150.7 |
| 3deb69fa-682f-38fc-843d-4eb7f2932251 | 2.0713 | -50.8799 | 2026-10-06 17:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c4a9714b-b0c2-33a7-a90e-ee927fba4d1e | -8.7324 | -69.4271 | 2026-10-06 17:50:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a3dab75f-6cbf-341c-8c94-562563d70eae | -9.5006 | -66.7459 | 2026-10-06 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 83b5b09d-4b9e-3aa5-b206-99ab33254e1d | -8.845 | -68.8173 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 31848bdc-a356-3035-84e4-afe9a606b154 | -6.0266 | -42.2792 | 2026-10-06 17:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| 845e603f-ab3e-31a8-a522-ad34147f35ad | -6.3862 | -45.8044 | 2026-10-06 17:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ea38f25d-4fc5-38d1-8ba4-5654d7cb3119 | 3.5263 | -51.2778 | 2026-10-06 17:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 614d88e8-e214-3e48-9799-2000bd0f4e97 | 1.7304 | -55.6259 | 2026-10-06 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9b71dd4a-bc67-3978-ac42-9cb7f60d3315 | -7.8356 | -45.3175 | 2026-10-06 17:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 204.6 |
| fe87c3df-f905-3eca-be33-26950aa3b91d | -11.47 | -43.3824 | 2026-10-06 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 0d4c1f64-5bc6-3170-845e-e4085be18c3d | -8.2675 | -71.0849 | 2026-10-06 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1fd57064-8232-3b27-93fb-1dc529dc582b | -7.5332 | -70.0148 | 2026-10-06 17:50:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 13d2bef2-47df-3da5-9736-f50e471e3394 | -9.8824 | -44.8171 | 2026-10-06 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| bcb85301-cbca-3b62-ad1f-7f38898934d4 | -8.2495 | -70.8289 | 2026-10-06 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 169.3 |
| ae9c6d49-7727-3051-912e-aacb128ea79a | -11.6378 | -43.6403 | 2026-10-06 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2e9a48cf-9e5b-3113-89c4-f5f020a70a4f | -9.1257 | -67.8322 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 8489e7a7-8e31-392d-b0c8-1c564e679f0f | -9.2365 | -67.9035 | 2026-10-06 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 4d16ecae-28f5-385d-8773-eb9ec1a95a4b | -6.5425 | -69.8085 | 2026-10-06 17:50:00 | GOES-19 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 9b686218-da02-3374-9188-b753ff6d477a | 3.5079 | -51.2784 | 2026-10-06 17:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 66.1 |


[Clique aqui para ver as próximas entradas](README96.md)
