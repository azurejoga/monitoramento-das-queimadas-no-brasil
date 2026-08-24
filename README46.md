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
| 6b03b44c-f661-31e3-85cf-1d8ca2fcd74a | -14.9392 | -52.664 | 2026-08-24 05:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 1c69815a-c77e-300c-b610-4b4be7097808 | -7.6849 | -63.3443 | 2026-08-24 05:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| fc761534-1ebe-3468-a0b1-f5cd5406ca5e | -15.4106 | -55.7769 | 2026-08-24 05:50:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d6c269d0-19a0-31a5-a234-e08cb5c1fc4d | -7.685 | -63.3255 | 2026-08-24 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e9ee81f4-9b96-3d66-ac39-2a8214cc69d5 | -15.2652 | -52.8535 | 2026-08-24 06:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d93d27e9-0df9-36e3-8cd4-6519e9624703 | -7.6665 | -63.3261 | 2026-08-24 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| a5ca1f77-7104-34b5-ac73-40022e17b273 | -7.6849 | -63.3443 | 2026-08-24 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1a71a5a6-76ca-3508-b7d9-aa4ccf23b6f8 | -7.7034 | -63.3249 | 2026-08-24 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 6815cd15-5d26-377e-a930-78d8b08cc151 | -7.78377 | -56.2877 | 2026-08-24 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf42cbf6-befd-3f41-a999-49d5c93b5186 | -7.68981 | -63.32951 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e94b7a8-d92b-30d6-80fc-49943a8adda6 | -6.85792 | -59.41237 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 779be538-c84a-35f4-9b11-fa321087ddd7 | -6.85969 | -59.40862 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a43537a2-d3d5-36d8-9317-57ba052d4fba | -6.69132 | -58.72399 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1843a3a-a017-33f3-a86a-b29ef6b82e3f | -5.79123 | -57.56377 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a95b013a-f8c0-3ac7-b0ca-0d5fd1f62991 | -7.59632 | -61.23035 | 2026-08-24 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96871317-e0fa-3cfe-91d4-ee9cdb1bf866 | -6.69696 | -58.72486 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae5189e2-0ed2-35da-8e83-9105f61a2717 | -7.68934 | -63.32653 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 7792b4cb-8482-3b3a-8eb7-8ae5edac20a2 | -6.56267 | -58.58946 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95b5b935-58a8-3bae-ac43-f20ad192271f | -6.1444 | -57.94356 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43c88de7-91c0-3ef8-8a6e-5a62c27b04f9 | -5.94039 | -57.73105 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1027b12-8333-3daf-a02b-e1d73541f705 | -6.35002 | -54.76228 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4140ed5-2199-377d-9940-707a1d3aca5d | -7.57094 | -61.19989 | 2026-08-24 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65336ff4-a3ad-3835-8808-f86d555c7f70 | -6.33568 | -54.7601 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d65a836-8d8e-335c-ba68-cf377342385e | -5.78457 | -57.56747 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6c23f3e-3987-398f-afc0-181d8c0aad5f | -6.56099 | -58.59101 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 508c64aa-c805-3368-9294-6e84b99ea6d4 | -7.22107 | -60.63293 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d60fc111-adc0-3729-b7e0-27b6601d7b07 | -4.99344 | -56.13817 | 2026-08-24 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0757f58-a8e3-3caf-956e-02c8a4727d33 | -6.12953 | -57.83194 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fc96fdf-d02b-30ba-a1b5-37c949b22f2e | -6.34592 | -54.77043 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54e4c874-40f4-3d6b-b4a9-af24392af5d4 | -6.12593 | -57.83333 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77c86623-34c9-31a9-8d67-0b72a285d107 | -7.68515 | -63.32592 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 666679ac-84f1-34b6-9e86-93ca2094e8dc | -7.57772 | -61.22235 | 2026-08-24 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43dd7889-b81a-3c8d-9d28-cd35bf144c9a | -6.77066 | -59.44521 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f51489c-3904-361e-ba06-23311a1a75d2 | -7.57699 | -61.22762 | 2026-08-24 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82dd37ac-d2a4-307b-9b61-24fb32c56bd2 | -7.69239 | -63.33482 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ef0e4b8-4aca-3c74-bb20-ad05493d288f | -7.22687 | -60.62789 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5498d881-5783-3a03-847b-20addd453657 | -5.7798 | -57.55766 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d9f691e-1055-3caf-8896-7f5b734853d0 | -5.77854 | -57.56675 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46922769-4539-3c97-bb53-fa69fe5c994e | -7.6882 | -63.3342 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 408f8066-67f5-37e0-acb8-2ff61eda4ca5 | -7.68872 | -63.33717 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f66c1393-0dc5-3455-8ea9-849410921fb8 | -6.34191 | -54.76839 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16814319-5dde-30fc-b5d1-6ca0b570446b | -7.68153 | -63.32147 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0eb43854-d514-3a70-a03a-07a6997c2c17 | -6.34155 | -55.87183 | 2026-08-24 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d45432e9-c2dd-37ba-a16a-e5e9e1e45f6c | -7.68458 | -63.32976 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 204015ee-13e6-30ef-80be-20035c1de6a5 | -7.69345 | -63.33395 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37ad18d4-b1f4-371a-8d28-1c86c8aa611c | -6.97236 | -59.07674 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d839c110-d7b2-3ddd-9cd0-9f46c6c2665c | -6.74117 | -59.65908 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8031a38-a8d6-3348-9b6d-fac11cf4a789 | -6.67172 | -58.74075 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2abbc31-08ff-3a43-a67c-7d46250eb086 | -6.34909 | -54.76936 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35b1de46-8d97-37d8-86e1-5ecfedb6bbce | -7.68572 | -63.32207 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 209c9b75-cea1-37f9-bb2a-31a179b32b67 | -5.94381 | -57.72877 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 176b6efe-3f36-320f-8233-016069a0f51a | -6.79387 | -59.81327 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71de2b50-fc90-31fe-a18d-9b4bd2457778 | -6.15088 | -57.94022 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f451d46-3582-34be-8574-4b540f6b8597 | -6.79913 | -59.81407 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e03aa2-f65f-3d18-995d-c446d2684b50 | -5.78519 | -57.56306 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 640bcff6-3416-39ff-a398-b742d3e1cdb9 | -7.23125 | -60.6333 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9d50355-f395-3353-8845-69d93a5d3b67 | -6.74072 | -59.66235 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ba7ba68-48a4-30ae-a545-3e0b397b4864 | -6.3469 | -54.7633 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69c0ad56-4074-3861-9b3c-21e5014e2b4f | -6.2224 | -55.61917 | 2026-08-24 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20bfcf9c-45b1-3c91-a75e-fa3926aeec24 | -5.79061 | -57.56816 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cbf3087-000f-32fe-b18e-c4f8bdb4d1aa | -5.94917 | -57.73401 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8b98d57-1e28-3441-bf99-f1f78347cada | -6.79589 | -59.80683 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1626f900-6fd3-378a-9183-c30112be24df | -7.67259 | -63.32408 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 218d3eb7-feec-3dae-b98c-ccb53fecc9b4 | -7.67621 | -63.32852 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f096456b-6d56-3153-954d-2949e855728f | -5.87185 | -57.56721 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bca2e5e3-f9cb-3ef3-9bf1-88e1facfc26c | -6.12246 | -57.83937 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a59fc5fe-8f98-3ae7-924f-20be51e359b4 | -7.25935 | -60.61478 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 864ea906-b4e6-33cb-9da0-39caf6c9236a | -6.145 | -57.93923 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7249b5a9-d8d6-3272-8806-ef382996d9b8 | -6.80029 | -59.58608 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 44b48d83-93d3-388c-b448-acbc71557ce8 | -6.96027 | -59.08236 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e47a9e-3fe3-3507-aa2c-189775e98f04 | -6.85842 | -59.40891 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44ddc6e5-68fb-34cc-abeb-9833a1e27482 | -6.1236 | -57.83097 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2092598d-452c-332b-9e05-59482d176221 | -7.68991 | -63.3227 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6d92a9f5-122b-3f49-ad56-ecb35d4abc94 | -6.15029 | -57.9445 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 055116e1-9182-39c1-969a-09c33746f865 | -6.77607 | -59.44587 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8acdce5f-c802-3e20-b71d-a699da98c770 | -6.79982 | -59.58942 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cff87dc4-3630-351f-a8a6-de69dda075bf | -5.93785 | -57.72783 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f34dca80-359c-34c9-a778-1e71b2c67db8 | -6.69078 | -58.72784 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c45aeed9-503c-393a-921a-777118fa17f7 | -6.3438 | -54.75399 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07c3b055-b30c-39f9-af46-9d514b5d3d7b | -7.23112 | -60.63409 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1ec7fcd-b83d-3ae2-9b56-f80f0e954f1d | -6.95473 | -59.08157 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7dc2437-b28b-3858-a2b6-3f9986221005 | -5.94318 | -57.73335 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a09129c-2f64-3150-b590-69cde5c3d882 | -5.00638 | -56.14054 | 2026-08-24 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5af51028-bf6a-322a-b028-cb91d722e175 | -6.96077 | -59.07875 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10ab426b-7d52-3aa8-9038-dc5e7efe7f92 | -6.34908 | -55.86688 | 2026-08-24 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ffb098c-d296-3619-9c29-3bd542448218 | -6.33973 | -54.76227 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16d9b16b-f0c2-338d-9dc8-047c8f962b54 | -4.99989 | -56.13951 | 2026-08-24 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54e847cb-31e2-3d29-ab60-d65b9fa93ec9 | -7.2261 | -60.63351 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 443ce5c6-e72d-3a1a-8284-5b2ffbfd17e5 | -6.33663 | -54.75289 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db3461a8-2558-3611-81ce-9db97cb5b57c | -6.68567 | -58.72315 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d83c494-1ffb-39a3-a0a3-664c2b94bfe1 | -7.22622 | -60.63274 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c2977f8-ec48-3e31-9fb2-5a699737d208 | -6.55584 | -58.58644 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed21f783-2d80-3747-a513-09304ffe9ebe | -6.22923 | -55.62007 | 2026-08-24 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 791de779-ae9f-3929-bc56-f01636f998ec | -7.68097 | -63.32531 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6ea7e983-fc7a-3958-a1e1-8db37d932944 | -6.55528 | -58.59028 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c212c1dc-18cd-3944-8f64-01fed6a65f97 | -7.79048 | -56.28844 | 2026-08-24 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee3aba0c-b6bc-3039-b492-778da67ef18f | -7.22119 | -60.63217 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5f86c2a-be81-3457-ab53-796a1676b48a | -6.95523 | -59.07796 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbc3649b-39e4-37d0-a7ad-32aca190b99c | -7.21685 | -60.62646 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 998202ec-935a-3d83-a76a-5e1def2d8998 | -6.79477 | -59.80668 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README47.md)
