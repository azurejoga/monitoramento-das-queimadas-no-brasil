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
| 2dba0c30-669f-3b33-adb0-96ba4453c362 | -6.142 | -53.51418 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e9fea6c-0d2e-376d-95d8-8ecb28af5a97 | -9.17539 | -72.72719 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 377701f9-e2ec-304f-95fa-142b1dcf513c | -8.64163 | -70.51024 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 16239ee5-31da-3375-b3dd-87f8fa72f2d4 | -5.88087 | -61.28038 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9d50edd6-8d48-330b-8103-d6da6409dbbd | -8.61563 | -70.9445 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fcf93737-48ff-3e51-96d1-a3bf3ce64863 | -8.63293 | -66.53664 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9c56dcef-2f21-3187-95b4-3379c8dfe629 | -9.28053 | -71.91442 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 224fd5ae-6ce7-3071-9009-9c921b3aba37 | -8.2157 | -70.49644 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 72c07dda-c208-3bf5-b0c5-fea39f4e98b4 | -8.87945 | -66.9023 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a979300c-5db0-3629-830e-0d27bb174cc3 | -7.71108 | -72.0043 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27cba3dc-e6d0-3bba-8cd9-a92dcde44dd0 | -8.56971 | -64.17413 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 81dd7eb1-d978-3ecd-b701-0212e02420aa | -5.91937 | -61.39791 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6245827-3beb-3bc3-9478-3be14e1f26e9 | -6.94077 | -58.95191 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| eda58307-2a9f-3471-8ed3-ac31fb7b2e25 | -8.64029 | -66.54597 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a94ddd9e-3b4d-3440-a06f-88cea5ec56bf | -8.30404 | -70.57413 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d4863fd-1797-3737-829e-588640f1fe23 | -6.3719 | -54.95454 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c7dddda-0844-312b-af02-3edbddd370ab | -6.27779 | -53.14167 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| f2644276-9d84-378c-bcce-87afba26a9e3 | -6.60234 | -55.43005 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| caceab31-5334-30fe-83ba-5450cf4cec76 | -8.83428 | -62.31671 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4b2ab019-c971-3cee-8583-b25f8f74eca8 | -8.34612 | -70.8459 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 37.3 |
| ae0a1c2a-c773-3792-bd13-622a2f79449a | -6.17244 | -57.77727 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ac61ff07-933b-36e6-829b-7a6e0a7f8926 | -8.37926 | -70.7388 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 310811b8-72d2-3499-a0f1-03e082769617 | -8.6019 | -70.20646 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7bf69cae-29b9-380a-8991-296a9a8b1f1c | -6.029 | -61.64868 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b454e25f-9f5c-3489-ad53-51107f2edede | -4.30971 | -59.47292 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4dd291c9-2644-3ea3-948b-578a3080bf93 | -8.39962 | -71.0854 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 45c0588a-3505-32c9-a2cd-dce06b597313 | -9.09276 | -69.858 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4c191ca3-a405-3a2f-b6bf-d299eb372afd | -7.95102 | -72.38531 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.4 |
| deb6aaf1-fcc9-31b1-b058-376f23428363 | -4.31438 | -59.47716 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| af3b5050-b6d4-3ecb-9934-4678fd380f76 | -7.57923 | -61.38713 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8393c09b-77ca-302f-802c-00676d4302d7 | -8.40905 | -70.34675 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d5ed0b43-7e06-316e-b7c6-2bc80bf45d5c | -7.94771 | -72.3852 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 580ff45b-948d-3f3d-ab55-43380488f63a | -4.93086 | -55.76551 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 42cbc2b1-618f-31e2-ae1f-00b17c7afabf | -7.64195 | -55.07447 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 7b04ca02-fc99-3f00-b530-102a73654f81 | -8.81634 | -68.99053 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3114a329-46ee-372a-b692-b52781b6e86a | -6.73912 | -59.64892 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fae1401e-7567-3290-84f4-ae3f3826ad78 | -6.0121 | -57.85482 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c22cc5a9-a365-3772-b241-eb5192c6b318 | -6.83539 | -59.94144 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b8618e39-e8db-3dc9-83cd-a42d18b5ea77 | -7.47771 | -61.38861 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 9f0d5719-3ab0-356e-945a-2aecc9e8008b | -9.14981 | -65.781 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b452f7a5-95dd-3ecb-8fa4-fa1593495eb5 | -3.72897 | -60.60631 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c8bd48a5-150b-30ba-b24a-cf1cca814d33 | -6.77993 | -55.69012 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 962cea74-60fa-36da-932f-69cd8b639f02 | -5.91592 | -61.39844 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e2f6a78-93e3-3aab-a4ca-00177123b467 | -7.6052 | -61.33014 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 429e4e63-7bb5-33ab-817c-e857fc9ac5fd | -8.94621 | -72.73434 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fa3e453b-d6bb-38bc-8166-a7bad6652fce | -6.93306 | -58.95314 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8abdc1cb-8e02-3e33-8056-6380ebba4602 | -5.9867 | -57.75499 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c485c48a-bba3-37a5-ac21-7e7b3b29fd0a | -9.48383 | -71.30055 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f80ffe24-219e-30e0-b88b-cb433fa418e6 | -7.75137 | -61.10077 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 36f62864-fbcf-3440-b32f-173ce9585bbf | -8.44433 | -70.708 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b4f81f5d-9fda-365e-8d38-1c9619749b8d | -7.47829 | -61.39231 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8d21bd76-fe4a-3436-a9fa-b94bace318e5 | -7.57725 | -61.30795 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34fe5a3a-8a69-30ff-8b99-ade1a2d4392a | -7.48574 | -61.41758 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96e48dd0-f09f-39c4-a1c0-f33d572b2e02 | -6.79509 | -59.39733 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ba66f02a-a853-313e-aca2-8dc3a19f3c04 | -8.89887 | -72.70848 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 67c75ddc-f860-358a-ac84-3d215bdcabf3 | -9.14922 | -71.922 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5aa656a6-4b63-353e-a9b0-a380f1f94d54 | -7.84305 | -71.83342 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8e945eba-2e17-3b85-b422-a110243da058 | -7.89362 | -71.53487 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c2e8b247-39cb-34b9-a392-92aa226de4ad | -3.52396 | -58.59579 | 2026-08-28 17:47:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6f936f22-1d22-3fd2-9fbb-cf7a3ac78803 | -7.61106 | -61.18826 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5068f7d7-f7b2-30c5-97b4-1f3f46540531 | -8.91457 | -70.69565 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| bf063631-f35f-3788-9e4f-c4d7a0258bfc | -3.2901 | -61.32643 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 06c5b1cf-c10f-3243-b0af-3f5ed2f1ac6a | -7.60822 | -61.19255 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81a8d9fa-f1ff-3be1-afa0-c3fea2d8078c | -6.43573 | -55.63123 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 79f6226b-1b63-39c9-bedd-3674fe3d9ab3 | -8.90423 | -71.39837 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 33.1 |
| e1e56330-d887-367c-99eb-f93b38fd1b9f | -6.80907 | -59.61034 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5a3e25a4-a4ec-3a64-bf5e-7bdaf83ef679 | -9.06693 | -71.94492 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94bf38f9-09cd-3f2e-843b-4d7e0776ac64 | -4.36285 | -70.28836 | 2026-08-28 17:47:00 | NOAA-20 | ATALAIA DO NORTE | AMAZONAS | Brasil | 1300201 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 570a4962-5b3e-38fa-a53e-088b7d6663ff | -3.40488 | -61.32186 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ae5ea788-199f-30aa-82a9-64a9309d4c5d | -7.30047 | -72.8475 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bdb0e404-38e6-3536-902b-fcbff8c10dac | -8.84766 | -69.15385 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f22d92df-9ba3-3087-8523-b77781c890df | -8.37699 | -70.85285 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 36.9 |
| e0d259c2-b07d-3c7d-bd16-d557cb104ee4 | -8.7837 | -72.77298 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8e131e96-2d7b-36a7-b04c-6cf7987b3f76 | -7.91863 | -61.31797 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a007faef-f15c-3c05-95da-df6c1a64bb57 | -9.05101 | -69.61674 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb6fb058-70fa-3c36-9086-057c534d07b7 | -6.95447 | -58.95194 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a4fe51e0-67a7-3933-b5eb-c8fb71e2202b | -7.59953 | -61.33859 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e0fb23e5-3bc3-317e-b275-faf507c71ae0 | -8.82272 | -68.9727 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 85d140fb-8ade-30cf-b3c0-9584da3abec9 | -2.9888 | -59.17799 | 2026-08-28 17:47:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 574d31df-fb82-3c4f-bd2a-6c46ad5ac588 | -9.11148 | -70.95687 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b1575e4d-8455-32ff-bbec-0120cc15484f | -7.60918 | -61.3333 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01c4a64e-ee97-398d-bf5e-eb0a6da578a9 | -3.89864 | -59.72505 | 2026-08-28 17:47:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e0f534ca-42cf-3d94-883a-e318bffadc82 | -7.60352 | -61.34174 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d85278a3-77e3-32a9-997c-8c4e5c677510 | -6.38972 | -57.46861 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 07d8b5b0-fdb0-3c89-ac2a-6739abb6438b | -7.35977 | -55.1717 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 26210244-c10c-32b0-bb8a-d3801ed9b885 | -7.83582 | -72.05639 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 871f5620-4029-3bfd-835d-b2397e3a0132 | -9.61185 | -71.38137 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe2c9608-55ec-31a7-9d76-276abbfc10b1 | -8.37623 | -70.84739 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3833e07e-fc20-33d4-b908-8aee79bc2060 | -8.64201 | -70.51406 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 33.8 |
| bab08190-3e7a-37eb-92bb-e866adcff8f5 | -7.92617 | -72.28408 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 15d28edc-77c9-3d39-ad80-2cb51037992e | -6.21477 | -57.76986 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0e64268f-9a3e-316c-8d87-1e387144b7eb | -7.20459 | -72.68139 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c7a4f975-3d29-3a3f-bd06-7dd0dad15bb8 | -8.39946 | -71.08856 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5681aa3f-0d1f-33fc-bbcc-51cfef36d946 | -7.92952 | -61.36524 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| de867ec1-c09b-3a8e-ad09-53d83a101624 | -3.54679 | -54.48795 | 2026-08-28 17:47:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 46b38924-a14d-30de-898a-f83632c8fb25 | -7.64579 | -72.44055 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 224ab06f-4a8e-327f-854f-54506622d528 | -7.60467 | -61.34913 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5bde86e-0be5-3e42-bd93-1a7c40be788b | -6.98999 | -60.66497 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4c038f13-af7d-3b75-98c0-68fdc2e5c29b | -8.79111 | -62.47813 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6a7b60be-10e8-3279-951a-c6e683f528e3 | -8.38113 | -70.84676 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 58.6 |


[Clique aqui para ver as próximas entradas](README148.md)
