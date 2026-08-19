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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f79ad7f-2171-3435-88e7-b1a8c0d9fe68 | -6.76199 | -59.46371 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31425b8b-d73e-3e03-83c1-5866808ad1aa | -9.42533 | -60.44142 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cf8a130-2b9f-338b-be7c-856c0c27405f | -6.85739 | -59.02322 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31a08457-8bfb-3736-a252-0bad7e137b0e | -3.09569 | -61.21302 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5d469bd-b0d6-3851-9d90-4f5a40cf3331 | -8.5639 | -54.75791 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 162aacde-8d67-3226-9772-eba455d4108a | -7.10302 | -59.76302 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 851a0963-8609-334c-979b-036440b726f7 | -8.55272 | -55.31901 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2fa66f1-e75c-3f7a-9236-912f739446f4 | -9.13774 | -60.60962 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c58df56-9718-390c-9e5e-fe584ab25c57 | -7.43223 | -59.78846 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e52da6cc-f0b4-380a-94ff-6c7e030488c8 | -7.60679 | -60.94508 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6724c41f-1574-33e1-a0e3-67d156dce73c | -6.85399 | -59.02271 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f8fe813-32d9-35ea-bd10-5d7d8278bce2 | -6.8862 | -59.04572 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4842468d-4df2-3097-8b48-1eb4b44c7360 | -9.00962 | -60.44892 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d92f0b08-fb79-3759-a12a-20075d2988b8 | -8.58233 | -54.72205 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b46928b-a5c0-33fe-913f-6fde26a80f0f | -8.50437 | -54.86271 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe8308e8-6b3e-3adb-a99d-30fd364e2b12 | -6.79384 | -59.45766 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f79b10e7-5237-3a72-a196-ab2fe81e7529 | -8.58259 | -54.75326 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b02dbcd8-77c1-3020-9439-700e05117483 | -8.57829 | -54.68857 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41dd964a-7a0a-372a-aa6a-677291a0c231 | -7.91526 | -61.73196 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94356b8a-8e8e-300b-b367-e94ef442e639 | -6.87766 | -56.40966 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dc73e51-0fbc-3648-9f6c-7aa2794d6418 | -8.5038 | -54.86683 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1b6a92c1-50b7-3231-913b-135f9c5ab8a7 | -6.85511 | -59.01538 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e906c6a-1a69-3bbc-bd3c-e97a2af323e7 | -6.75711 | -59.15724 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00cbe75e-158c-346c-ae25-668328daaa93 | -8.57893 | -54.6841 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 633af9d3-a958-3d4c-a1ae-05abea36a672 | -3.15212 | -60.26678 | 2026-08-19 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6045103a-912b-3f36-8df6-bc0d112e79e9 | -9.40418 | -60.579 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c1f8db-b9c7-3c54-a412-eb052aee49bb | -7.54045 | -55.5995 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 727c65e0-86da-313c-8ef4-20fff1f55431 | -9.42703 | -60.45255 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ab5dbe6-0047-32ad-b5be-ce2338e411ca | -8.57763 | -54.69008 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35b6a226-f305-35df-b3d9-2fd88c7733d3 | -8.55258 | -54.74269 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe973401-8c6b-3d77-94cd-0b1cc4f81911 | -9.4041 | -60.55737 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ecf1807-634d-3849-aa35-4d2c14651467 | -9.2083 | -60.81405 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3abbac29-65a1-37fc-83d5-67f2862fe997 | -8.53618 | -54.73141 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 317d95e4-fc67-31fa-8fbe-7c83d860ef37 | -7.53741 | -55.59154 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb6aab0-f703-391a-a042-ea86d518ebee | -6.74421 | -59.17378 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a701e371-5662-3bef-830b-050dedbdbfd5 | -7.54363 | -55.57743 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1330b00c-71df-3187-ab74-f033ac9db231 | -8.57585 | -54.76982 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b669fe3b-4b6b-37de-bf46-be39186944f1 | -8.57145 | -54.73652 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d769463-cf90-3310-b95a-54890d10db3e | -6.60976 | -58.39715 | 2026-08-19 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 863e5b54-ced1-345c-87d8-b8c67a5ac850 | -8.57087 | -54.77343 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 62536f80-e5a5-3c3e-a9ea-c7a27a76e93e | -6.67043 | -56.15508 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5bd3a34-eaaa-3ef8-ab48-036c4e2c3d58 | -9.39583 | -60.56689 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c3d008e-d279-3063-b464-ebadc278cb79 | -9.0225 | -60.49781 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 587d43c5-6c69-32e0-b9c8-3be2ededbfbe | -6.69449 | -58.94564 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 55b3b5d2-ecef-3e42-8a74-2f91ad104928 | -6.79104 | -59.45357 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b374a3aa-69be-3391-9244-31dbf42d4f21 | -8.21617 | -55.0356 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aef0a1be-d647-3b8c-b081-53d9195203f1 | -8.54513 | -54.76361 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 78aa9c62-3c85-3086-b26b-a9b6f518beee | -8.53951 | -54.77161 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c247012a-bcb5-3e34-a474-8d2f6f927aee | -9.38747 | -60.55478 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba8b5f0d-bc85-380f-bb22-c1c15b6ea8f7 | -8.57091 | -54.77175 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 714917bf-8768-3e0e-abf7-c6987e63c69c | -7.00198 | -59.04426 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1784e1e8-6ad5-348b-bc35-0978abe691a8 | -7.46361 | -63.64821 | 2026-08-19 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15c5f8fa-8038-3156-910d-49b9f3b36212 | -6.756 | -59.16453 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64144978-56b0-34fb-ab03-a454c4443346 | -8.56173 | -54.74131 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1205d90d-c162-3947-91a3-4a953b21ab04 | -6.77793 | -59.75622 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5e5ea1f-0894-3971-8544-56d2f8fbe5b2 | -9.39915 | -60.56741 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77dabccd-6f29-3a4a-a910-78433e262d1a | -9.25915 | -56.91325 | 2026-08-19 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0904895-5630-348e-9676-ece2dec84931 | -7.43277 | -59.7849 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ebddbda-8132-3139-82bd-392c1c6a7cb7 | -8.95952 | -60.53111 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 649ed359-b6e1-3e02-97c8-a4157d7aa6ff | -8.56732 | -54.73322 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4325813f-fab4-3fc9-8074-9a48cf3a6db4 | -8.56555 | -54.74637 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e186340-06b7-32bf-ac99-372e0dfb7810 | -6.8888 | -56.44098 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dcbdbe5-fef3-362c-b8e9-f3a726586a9f | -8.58905 | -54.77177 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5f82a8b-876b-3735-b5b5-53f98ca0ed25 | -6.73997 | -59.03501 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 518842b7-9682-379d-bc87-ee7b74d9840e | -8.5745 | -54.68349 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 542d0ab6-96ec-333a-96d7-93273b5c9a2a | -9.02529 | -60.50184 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf8bab31-9f5c-3b3f-86f6-3c9c9c73dfaf | -8.59 | -54.73189 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08b6a22b-0b07-3a02-9842-4b5f8ac5a465 | -8.57767 | -54.69291 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f3eb741-4726-3528-9583-2ec9d04b46b1 | -6.74924 | -59.16345 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 998e60d5-c43c-34bd-a88a-032b645f94dd | -3.15542 | -60.2673 | 2026-08-19 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcddf8f3-7cec-3b1a-9747-9c0fdae3cb04 | -3.09794 | -61.22065 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c39c2ee9-3746-3aa3-a49e-6c0607a11602 | -6.68579 | -59.07147 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a851b35-54aa-3a0e-82fc-b81cdbadccc3 | -6.805 | -59.44439 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5933c971-e005-3d59-8871-738bf297f318 | -3.49561 | -59.63387 | 2026-08-19 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa432fbc-b5d2-3b01-9d48-22f43616913a | -8.58025 | -54.77047 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7709a875-dd7d-317a-a2de-d89d36e4b449 | -8.56765 | -54.7316 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22d2eb90-31bb-36a0-957d-260100198571 | -8.58734 | -54.71832 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49f14926-95f5-3984-aa8a-20bc18e15d63 | -9.19094 | -60.81507 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e9dad3a-c580-3315-b857-27aeb48a42b8 | -3.09905 | -61.21354 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06c07f7a-0a96-3328-a8a2-cf8a468ee823 | -7.05108 | -59.83828 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7d5b97e-1387-3ace-87e0-af16ed125a89 | -6.69734 | -58.94983 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 501daa6b-7e35-34ab-81a3-f89e6e8d53aa | -9.39026 | -60.55882 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb787af0-4d66-3956-ac3d-59844b456b21 | -8.57152 | -54.76751 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 52a7618e-0073-3979-b6b8-5d548bf858e2 | -6.74336 | -59.03552 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70466bc4-c59b-32c5-aac6-6169c12f65a9 | -8.56207 | -54.77221 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b2204b2-d2ba-3198-9ccf-533458d66f7f | -8.56447 | -54.72232 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d20a442f-36fa-3838-bb5e-1d7a18fa9359 | -8.57969 | -54.70823 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3368146f-d588-322b-ae2c-d0bca68c19f2 | -8.02353 | -54.00887 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5493cbef-14d0-397c-811a-729fb956ce3e | -7.60793 | -60.95945 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b257366-7a37-3d5a-96f9-ba2db3e942f1 | -7.90473 | -61.73389 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9583d63f-83de-33d7-ba25-b2c652cb2fab | -6.88446 | -59.03422 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae82c1e2-e08f-3eed-883b-e009e5220dcf | -6.84886 | -58.98812 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba95c321-1fbf-3152-986e-03ec81b37643 | -6.74649 | -59.18157 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd2c137d-ded3-3a49-98e2-4b13863f4dcb | -8.10291 | -51.66596 | 2026-08-19 05:23:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f1d1c9be-b749-31f5-a326-3c36ed68c859 | -9.40023 | -60.56036 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af1c99cb-0733-3061-acdc-bc213578100c | -6.86122 | -59.02692 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0d044a9-2e06-3f94-aac2-ea426f768b7f | -8.57349 | -54.72083 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a18b5235-a7a9-36eb-b52b-812da2eb6477 | -8.02777 | -54.01326 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f5b275c-7339-3591-bcaa-80afc8a1ab85 | -7.05387 | -59.84231 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb494c6a-38b3-35b5-b9bd-40bd361b29e9 | -8.54573 | -54.75935 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README52.md)
