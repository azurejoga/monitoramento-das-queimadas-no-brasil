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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb4b4a2f-e7aa-3e28-885a-d3faad8ad7c2 | -8.53786 | -54.82575 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e593b3b7-560a-3bcd-a342-6adcbc9179a0 | -6.80076 | -59.59938 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0fbfabc-5d0e-3a1e-8dcb-84316794c311 | -6.76835 | -58.68499 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb4d8605-a971-37c4-82fa-94680281d31d | -6.68526 | -58.73576 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3df7f76f-f3bf-3d2e-ab55-d7aacae0e0de | -7.60298 | -60.95216 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 185f470e-8528-36f1-8206-26193aa26d8e | -6.79977 | -58.64404 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3be315d-ea55-36ad-bc1c-2d068e1d15a5 | -6.67517 | -58.73431 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc933224-6c82-3932-b6b4-79fd8a5bd46b | -6.76248 | -58.69016 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd492f1b-ea13-31c0-98d4-ca337b1b392f | -6.69654 | -58.72861 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c3f8600-c399-309c-a7d8-f70b36e94c17 | -6.851 | -59.41575 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2fc9589-6d13-3f5e-9c7b-91bbb1d11d84 | -6.7854 | -59.42746 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b378b705-f902-3395-81ef-e047247e7ce4 | -7.56892 | -61.19125 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88afa70d-1f00-3552-813b-dff5698ae15f | -6.67981 | -58.738 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| dca212ed-0d09-39cd-ba64-afa6abe3b07b | -6.89577 | -55.70074 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 436389f8-6c1c-3453-ba5e-53cd30c0c733 | -6.67052 | -58.73063 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 65a5c85e-153d-3226-82f2-72f480885644 | -6.80407 | -58.65054 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3757174e-b28f-31d7-aac6-6dd8724ed4b5 | -6.71127 | -58.73383 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f48ec92-1891-3f76-9f42-49305f22a771 | -6.94444 | -59.08401 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9149b013-da58-3a19-a561-b26e8a2e1ba9 | -6.55183 | -58.52352 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc7e921-4016-3dd1-bc9f-4a937bc150b5 | -6.81341 | -58.6581 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ff89f654-004d-34d4-90be-a9545bba9fc3 | -7.60872 | -60.97475 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd1a1ff5-5ae3-3ee4-b037-0e78ccf275f3 | -6.93828 | -60.08765 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b57836ad-d550-3ff2-8dee-2ee8a8925369 | -9.1738 | -58.33405 | 2026-08-23 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c70ee745-5815-3436-89f2-0e6f4a0b9a92 | -7.59438 | -61.22851 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccc26ae3-4e27-3d29-8f67-fdd37f919b9e | -7.43832 | -59.79504 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7159273-9157-3026-9990-b9764734afc2 | -6.78638 | -58.66635 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 459b4cdc-370b-366a-8fe9-e08091d6222e | -6.78848 | -59.40979 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef16b7c8-535e-394f-b5c0-9ee2fb8b6b31 | -7.02056 | -59.56593 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 801f722f-c6d4-3396-a346-b8e2e9d4b4e2 | -6.86943 | -59.03257 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b5f892-6106-3d96-a07c-2098fa767d8b | -6.76169 | -58.66882 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f39a4ef-058a-32be-b3a7-55289451a7e1 | -8.90554 | -60.54911 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db9de2de-33b7-36a5-843c-571db9341ede | -6.67092 | -58.72766 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1e08357-ea37-3602-b8a6-b85c5ea42178 | -6.79736 | -58.66176 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9d7b302-1e4b-3ef3-b7aa-b23d36a04b9d | -6.76211 | -58.66582 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 229079a3-6fec-35e1-859e-eb7c1957ce9f | -6.79898 | -58.6499 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b2ed463-53ad-362a-b2a2-330bcfa3ae54 | -6.79587 | -59.80558 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a943afd-c5db-35e2-aca3-14cccb282926 | -6.6689 | -58.74253 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2d35e67a-e88c-30d0-8836-5cdc7849b68a | -6.79858 | -58.65278 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7dc47ef-5ff9-307e-b828-aef4fa559ddd | -7.59378 | -61.23259 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79b67de5-dd86-3298-a087-f5e9cc992320 | -6.78757 | -59.41154 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d563612-bff2-3700-910a-809c4ac5d6e0 | -6.95165 | -59.06804 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3d0adb5-bbbe-3667-ac53-c75ab42312ab | -6.67637 | -58.72546 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8deabace-ccb6-39b4-85f3-bc68bb1846ab | -6.66136 | -58.79811 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a0c2273-79fc-3907-9559-d1721fe948e0 | -9.1181 | -61.59028 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02611e4a-2f28-3bdd-b058-d06108ff51b3 | -6.70704 | -58.7272 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4501cbb-abd7-3a0d-8941-6c77d6c94df4 | -7.24589 | -59.45572 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37792986-5bf0-36b5-abb4-9a8b44496c33 | -7.78958 | -61.43173 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8818cad3-47b2-3ea1-8d03-58073c128b17 | -9.59062 | -60.49917 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d04a92-a951-3c9b-88ee-bdef39e7e5fc | -10.06809 | -60.50195 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f92c7fcc-82e1-3bb2-bb93-ad12410ec426 | -6.81465 | -58.64903 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd3a0da9-93f4-357d-a57e-02bdc40e33f8 | -7.60042 | -60.93863 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3af44089-843e-3dbe-9be6-3ef0d3cd17f2 | -6.66426 | -58.73885 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceea19b1-789d-3173-ade9-522f7eb99751 | -6.83506 | -59.95321 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 908ef663-9247-3633-b1f8-c64f4691addb | -6.96004 | -59.0806 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 341a7714-1d33-3ac1-9c62-6350519cb751 | -7.66647 | -63.3428 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a9b1a0d-c50e-39e8-8a16-fa8d63d679c0 | -6.85 | -58.98948 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bed01a4-03fc-3204-9cec-5fcc6a14d8a6 | -9.14408 | -65.95747 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6518f1d-1349-3b3c-8009-7548cc34b2c4 | -6.68021 | -58.73503 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb5d1635-0396-38c6-82c7-e3a523195b91 | -6.80897 | -59.67898 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 782eb6a2-7fea-3060-9696-6956fab59bac | -9.53759 | -63.56511 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98a82209-e1ec-3cfd-a4c5-d57acfb2bb34 | -6.76487 | -58.67234 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a2bbcb0-ef89-308a-ade9-8e1ec06c353c | -6.82137 | -59.65977 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e584db5b-2786-36cb-9190-47022fc5dac7 | -7.62188 | -60.97657 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d30c3cf9-1425-3464-ab4c-653fb8cc8e86 | -6.7924 | -59.41225 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a0c471f-855b-3cc3-92f7-b966eb102526 | -9.05143 | -65.45421 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 779b2384-421e-376c-8ba0-ebdd45aeccaf | -6.9007 | -55.71111 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f5aef68-7012-3714-9261-6314b381f50f | -6.8254 | -59.42272 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30769bec-a6b2-3f03-b7fb-cde2ec7bbfc8 | -9.1833 | -59.4562 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5c00ebff-2030-3370-bbe9-4bd4a5f4d097 | -6.90471 | -58.99728 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99e3bd39-e4f8-3a9a-9793-1decbb043dd8 | -6.6915 | -58.7278 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8f2e2da-f99a-32ab-91b8-8f0e735d5946 | -6.96232 | -59.06389 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17c6252b-a8e4-3897-802b-4ca6a554cedd | -6.7962 | -59.66665 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3220ff57-d1d4-3717-909c-03fc96db5ffb | -6.67858 | -58.74705 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| dc05f905-8540-3b0a-8feb-ec6bbb02f69a | -9.1041 | -61.59641 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aec076b5-11fc-34a3-8042-5f4e86ebc070 | -8.69663 | -62.87292 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d00d80e9-91d6-3c50-a0b8-af6eda4da2ef | -9.66038 | -63.83853 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6aa9d10f-5cf1-3922-b3fc-4a0923d7342b | -7.68598 | -63.34104 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b1d71daa-57f9-3a9d-9b9a-50ebc865d720 | -6.84505 | -59.45792 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a0c8e8e-fb54-3272-bea0-0ba8e90f0fcb | -6.77909 | -59.44074 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 43bf18ad-6cab-32f2-b79f-35077d88daa0 | -9.09981 | -61.59574 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ec579e7-56ac-3a4b-9746-e5ef7ea36e29 | -6.76795 | -58.68796 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eece955c-eeab-3ecf-b1d9-b16ceee57e8c | -8.70555 | -62.89476 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a307e17c-f211-3aa2-a2db-7bdbff438fbc | -6.80451 | -58.98115 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 395c3d16-e9fb-357e-8814-da3ff59b681d | -9.18254 | -59.46195 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4502c571-2a09-3abf-ab7a-332540e71c0c | -9.17757 | -59.46122 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 848e6b61-22a8-319d-803f-cfddb4bab3cc | -8.20054 | -54.9827 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08c2601c-ec32-3cc5-8b30-17abce924b93 | -9.21139 | -59.79041 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a645526-0557-3f1a-9670-8408100af73e | -6.80465 | -59.4305 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccfc4218-d865-3f33-a972-dd6f20cff4c7 | -6.85657 | -59.41119 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81b70478-cbc2-3a3f-b753-e4501d4df00f | -7.59809 | -61.23323 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aef48f5f-a3cf-3bd7-b010-8c1dcfc9b130 | -8.94892 | -60.57491 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad4749b8-8c05-3cd0-a137-132b207f807f | -6.55225 | -58.52052 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6811c0e-8764-373d-bd5f-bba898c5603e | -9.17338 | -58.33739 | 2026-08-23 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40980ba4-3be3-397f-b82e-8b12bdf7ce19 | -7.36429 | -72.65833 | 2026-08-23 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74e02099-a37e-3cf6-8b4f-ca9584925e0d | -7.78535 | -61.42606 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac773858-65de-3e86-97f8-6fb62a5147bf | -7.78108 | -61.42543 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a827ed3-a5b6-3f0a-87c3-25985224ac4a | -6.96386 | -59.05264 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86026c8f-8b78-3978-ae50-0c4a3cb7b84d | -6.78338 | -59.75805 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 350ebb62-b254-3ced-af9e-52cd0776aa5d | -7.60299 | -61.61841 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19d66737-72f7-3747-801d-ebe513ffed12 | -8.6927 | -62.87234 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README66.md)
