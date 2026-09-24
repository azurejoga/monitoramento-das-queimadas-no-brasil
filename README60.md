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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7942ea9-3542-3036-a6f1-8b66a5e517b2 | -17.57631 | -43.75564 | 2026-09-24 04:49:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99eb2f54-3463-3e30-a0e6-ed2973a32fde | 1.57286 | -55.93201 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48db77c6-2c05-3082-9c68-d45040d17e21 | -0.50597 | -49.151 | 2026-09-24 05:01:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38da80aa-ba53-34b5-a57c-3873cc8bb399 | -1.03003 | -53.74133 | 2026-09-24 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45b015c9-a5c6-3372-9c4b-5c3fcb326503 | -0.93526 | -47.55352 | 2026-09-24 05:01:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5e6d88d1-544a-38f8-b511-e32d41b724a2 | 1.29551 | -50.85676 | 2026-09-24 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 254b8613-b827-346d-ba78-0b416c7df1f9 | 1.99578 | -50.87525 | 2026-09-24 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 734d4031-1eae-35b4-9d30-818b36ae2d4d | 1.99695 | -50.87496 | 2026-09-24 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e918a083-12dc-35ba-b0bb-2e0d904bfd4b | -1.02376 | -53.73697 | 2026-09-24 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6711be9-249c-38cd-80c8-887d258d94ff | -1.60586 | -49.81661 | 2026-09-24 05:01:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80cd7f6c-972f-3beb-8cff-1627340eeb70 | -1.7215 | -49.98569 | 2026-09-24 05:01:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760cd70c-3289-3308-b688-756a40bed839 | 2.01004 | -61.08627 | 2026-09-24 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c22fb55b-ea2a-3b70-941a-c09449c061dd | -1.60151 | -49.82035 | 2026-09-24 05:01:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aaf226e-0e6b-39fb-856b-9168c3b51a03 | -1.71785 | -49.98514 | 2026-09-24 05:01:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7814c3b8-d029-3cba-b3aa-128bc134bb7f | -0.2756 | -50.47301 | 2026-09-24 05:01:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01741cf0-5990-31d9-93d6-d0c21eb3568d | 2.13069 | -50.7277 | 2026-09-24 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44ae815b-8af8-36a7-a88c-b6803b11b652 | 1.49661 | -55.84901 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 381fec46-d166-3f5f-b471-40276c0f3888 | 2.34046 | -50.76641 | 2026-09-24 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9152822b-e411-3415-8268-027967cd8c31 | -1.02431 | -53.73354 | 2026-09-24 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b128b273-051b-3e09-83fc-86b243f5c324 | 1.50788 | -56.01857 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0912f3b1-3755-3078-9fd0-a0a453b52494 | 1.61465 | -55.9357 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 422b5ab5-5b07-3d58-b2cc-de9e2be14320 | -1.39473 | -47.94438 | 2026-09-24 05:01:00 | NOAA-20 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ded51042-5cef-3a28-9034-d36db2ace774 | 1.87319 | -50.67398 | 2026-09-24 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6453bedf-e567-3548-b7a0-5aacd200cdac | 1.29609 | -50.86043 | 2026-09-24 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aafbba04-7237-3d71-a7c3-8576f0f390c7 | 2.00582 | -61.09317 | 2026-09-24 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9603d354-c971-371f-b4e2-f2e150ba0587 | 1.29493 | -50.8531 | 2026-09-24 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc972f69-a8ac-380a-8092-7f2c111491e1 | -1.33233 | -47.78416 | 2026-09-24 05:01:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846a41a9-55b5-33d1-96aa-05041d862e7e | 2.16012 | -50.89032 | 2026-09-24 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfd4695e-3427-34eb-b6f8-73f07c28011b | 2.00536 | -61.09014 | 2026-09-24 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d2ff27a-392f-37c5-869f-9f292d818d3b | 1.58349 | -55.85416 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cebd6fb-b309-368f-8091-144c6160b13e | 1.30066 | -50.86721 | 2026-09-24 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 308faefb-3798-3eb4-8a16-547c95f97560 | 1.27897 | -50.84056 | 2026-09-24 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ec094f9-357b-3b8f-b153-6e566757ee5b | 3.83445 | -51.80142 | 2026-09-24 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 458b90ef-4248-3d5b-9fbb-bea3f9852489 | 1.5072 | -56.0143 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 09e27809-b960-38ce-9dac-884e221d7167 | 1.50747 | -56.01628 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1275934c-b795-3825-b064-1dc1a24c803b | 1.58627 | -55.85219 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92f572b4-3dda-3158-8e1c-902451ecdbc3 | 1.51113 | -56.01572 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b776b92a-d8aa-3dfd-a9ef-d92fb96a6e88 | -1.78676 | -47.83604 | 2026-09-24 05:01:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1154a244-8e92-36b9-97c5-9a40a78eea06 | 1.57353 | -55.93624 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0be46ebe-a019-32d9-9883-1f97222f10c0 | 1.56989 | -55.93681 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1a87ede-b536-3e85-b330-50fc76621277 | 1.50672 | -56.06025 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc83ec60-71ae-3c83-8882-3736a22e26b3 | 2.13011 | -50.72405 | 2026-09-24 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dcfcad9-df27-3d13-9a62-bb791b3cbf86 | 1.49428 | -55.85796 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa7dffb3-3c2b-3ca0-91ba-14dc97da5a2e | 1.30008 | -50.86355 | 2026-09-24 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb486d5-f0e4-3517-a186-f82e3dff15dd | 4.00096 | -51.69357 | 2026-09-24 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37ab4bb6-fc9f-3bbc-ae27-4a9b65a9b636 | 2.0105 | -61.08929 | 2026-09-24 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 220284ed-b9c6-3e13-90a0-32a8078820a8 | 2.01143 | -61.09541 | 2026-09-24 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e03baf3-159b-3d88-b298-c7d283368805 | 2.01097 | -61.09235 | 2026-09-24 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cb9280c4-8027-379b-b704-341beca1a81b | 1.57634 | -55.83651 | 2026-09-24 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| caf2851a-a9c3-344d-9d91-94f643ab7e61 | -1.39417 | -47.94806 | 2026-09-24 05:01:00 | NOAA-20 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d85d18cc-55e7-3e82-bc42-48df1a2b7968 | 2.15954 | -50.88671 | 2026-09-24 05:01:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf6e350b-8d82-390c-9153-b43671379a94 | -1.72218 | -49.98146 | 2026-09-24 05:01:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f17486f0-c8c9-34ca-be45-53dcccf62447 | 2.42313 | -50.8719 | 2026-09-24 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca4a220-cf94-35b5-8d60-b9c05b07c91c | -1.39177 | -47.9453 | 2026-09-24 05:01:00 | NOAA-20 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84cd74a7-6713-3f5c-8818-00a054596d93 | -2.83163 | -60.23338 | 2026-09-24 05:04:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53b09599-b3e2-34f4-b423-3f6f201a334d | -3.45668 | -50.07812 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 503f8138-c060-3933-8a6a-b60e104ce04a | -5.82092 | -57.73896 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49cd17ec-4dbc-3cfb-9fda-5c62aafbed92 | -3.60196 | -60.57568 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23f1fb86-10f0-3fc7-af39-fa121f3db980 | -8.60178 | -54.60255 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23383199-25fa-3fe2-b26a-3c95dd92695f | -6.04004 | -57.77105 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d469e5e-ee46-34d1-987b-ed1875d4871a | -3.73326 | -59.42252 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80f11e13-ea3a-36a8-960f-d30ad2645447 | -6.08239 | -57.62931 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e42d914-e7fc-3f28-ae42-5332c6780afc | -2.95578 | -54.08832 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c21eee6a-3429-3014-9ef7-699b58aceb4f | -2.91277 | -54.18747 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34aeeb0f-7b8f-3b6c-b92f-9a0a2ba63b82 | -9.24797 | -47.34785 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d1f0b5f-fbe6-34e6-a88f-39344940f009 | -6.92308 | -62.91484 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1c0ca40-bc4e-30ee-8a2f-caddf18aeecc | -3.68198 | -60.63363 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2cdd22a-bd17-3cd7-8655-2079fef35d23 | -7.19258 | -47.47461 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a248dfd-df43-3434-b125-4552556f1752 | -3.75162 | -59.31187 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f48cefa7-d371-3954-a7bd-cd7e7d3e9e9c | -6.46361 | -54.99711 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3cb1f51-ff27-35e0-a492-f72165798668 | -4.95318 | -45.14654 | 2026-09-24 05:04:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25d19af5-13b3-3a54-bf01-d4cdde8e010f | -4.5585 | -54.90445 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e69e65c-18ed-3ef8-98c8-1ef4709d8b34 | -8.17351 | -54.79781 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa928d35-2133-3cd2-9e4b-57c40306bdbe | -5.10237 | -56.12254 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 393a27a7-5e67-39b6-bd0b-02c48a742748 | -2.3871 | -48.52487 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a0c0c9b-647f-3ab0-bbf2-1ff9268c035d | -8.1222 | -54.82163 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0419480-bcd7-3d91-87e2-360bfe60d00d | -6.33463 | -49.86363 | 2026-09-24 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e805130-7197-34bb-9f28-bb05c941b75f | -2.47963 | -56.55811 | 2026-09-24 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1476b8c7-014a-399e-b92e-d786abc0e812 | -6.30827 | -59.9452 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fcb6f97-8036-30f5-9de3-d25583ad0893 | -3.4558 | -50.07084 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad4f9ab7-be94-346d-8e7d-94767cdd3631 | -3.17054 | -60.65435 | 2026-09-24 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c391340-d4bc-3dad-ad3b-3f9500b8e396 | -6.88923 | -55.56546 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fe92010-34ba-3dea-b99f-76da45cea66a | -8.59186 | -54.62237 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b55044c7-9396-3a8c-8753-ae664cdda442 | -8.52979 | -47.39539 | 2026-09-24 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c49c89e-31bb-359f-a5c8-f8cdc2fc4350 | -3.19785 | -51.01766 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c437b0d-88bd-368f-94a2-dedf8499d4ab | -6.65126 | -55.05592 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e122fe0c-8542-386e-b8f6-29c2ac9ace48 | -10.0798 | -46.05204 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 25cf8fe3-c55e-32b7-90ce-d1becec3f5f7 | -7.31069 | -50.06133 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07c0ffbf-19e8-39aa-bcc6-e5e9c2a01ba0 | -6.45531 | -55.0065 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9361267c-bc5e-3f2d-952e-74d2ce87136d | -5.42426 | -60.24869 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b22d023f-8992-3b65-a55c-76338ff2e388 | -6.40182 | -46.20216 | 2026-09-24 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0bc7a55-cb39-3773-b910-364228e467a6 | -8.59847 | -54.60202 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e986c37-e9eb-3c90-8f7c-54c732a7e01e | -3.08351 | -51.28708 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6537098-78c5-3d29-b979-59e1ee646a64 | -5.59873 | -60.19737 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c1ee5e9-a5d2-3d0b-9b20-f211ae011523 | -8.29064 | -55.10881 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba1addec-086d-3d34-9c39-886e66bff540 | -1.63912 | -54.90887 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ff3926d-ac4a-39d1-8c8c-29fac1718c1e | -5.14593 | -60.36879 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c16db99-bdba-3f58-ae16-8f6d8efefa8b | -8.30683 | -56.36636 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ace370a8-c965-302f-b67d-2338e36e7380 | -1.19348 | -54.14446 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af9fb618-d282-31b4-8321-ac6af1049853 | -6.57161 | -51.48967 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README61.md)
