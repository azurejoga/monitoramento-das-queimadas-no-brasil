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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f3bd3a3-ae99-382f-b6fa-05ae472d5efa | -1.50032 | -51.97635 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03c914e9-da64-315c-bed6-00da569791fe | -2.68299 | -52.06897 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab3f33b7-77fe-3c83-9e0b-8d7dfa9f6100 | -2.56536 | -46.55587 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ba36516-aae4-3a54-b203-8204dade24ba | -3.47273 | -47.68479 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfb0ffd7-fa13-35e4-b8d8-6eb9597f0ae0 | -1.62909 | -53.31363 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15ed7e1d-d7da-364d-944f-edce4ddcac73 | 0.87273 | -54.63567 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41a44994-2277-324b-8c45-9e1137162638 | -1.61169 | -52.60254 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0573b255-c9c8-36a4-9e39-bfd8546ceca0 | -2.61362 | -54.26844 | 2024-11-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 518bed05-4a90-367d-90bc-ee8c76c7471e | -1.18245 | -51.95812 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9337744a-8ca9-3ef9-86fc-182fba2d3377 | 1.79021 | -50.42778 | 2024-11-23 05:10:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35062929-fe33-3cba-92b9-61dbcbb97188 | -1.95233 | -53.01078 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22446efe-05d7-33c0-aa74-2f5b531f884f | -3.07566 | -51.66543 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88a462f1-4f2e-3360-b11f-195fb0f4f8b1 | -2.40316 | -53.84725 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9489eb8-667f-3d42-b757-5b0c80c2eb27 | -2.16162 | -50.46061 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c42080e-6880-392b-8cf5-049d0ec4fa55 | -2.68708 | -52.07307 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4df8b05f-3ae4-3fa7-bdd8-95ef2cdd6818 | -1.7349 | -52.71369 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c13ed908-dcb9-313c-82e9-ab0c8e8d8e79 | -0.94113 | -51.72233 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df74fcf7-9f8a-30d8-8ef7-cf9439f30a9b | 0.95686 | -52.10899 | 2024-11-23 05:10:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92541860-ebcb-349a-bdb8-57059b99d36d | -1.3076 | -51.7436 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 281503dd-1784-3c7e-be19-a6d063ef076c | -2.20706 | -53.75728 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9d2d608-8f93-37b8-8e33-9b5a4aa2e022 | -1.23209 | -51.78851 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e51c8cf9-8f57-38d4-b610-ddab5d793be4 | -1.20907 | -51.75409 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85c38b05-36df-3d5d-8dad-b8906dc0a705 | -2.06048 | -53.23262 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8ced10e-ca7f-3b1b-ad51-f5b117a83905 | -3.66995 | -47.13593 | 2024-11-23 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d7e6a11-d458-31e3-954d-f23f383c9444 | -1.41909 | -52.37022 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70b00081-942b-3b83-9667-ea9c43772cff | -2.7423 | -54.1151 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccb9f37a-ae19-35c0-833d-328bfee8d52b | -1.93882 | -49.52924 | 2024-11-23 05:10:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6e4c3bd-c9b5-3aec-90ba-dea3d9db569d | -0.36594 | -51.57127 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc1146c-4ea5-31ee-9531-1c1af5e27dbe | -0.99095 | -51.76323 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a492dd1-3f9b-34a2-88f5-e9cba7e17970 | -2.46172 | -53.69779 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11bf3894-0a5e-3fa0-838f-c235fd34f522 | -2.45208 | -49.08612 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| f15f3bc4-063a-33e7-8864-529a2dd193c4 | -1.62721 | -52.60694 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c30ef01d-5b21-3a60-b553-a3afc85180e6 | -0.92433 | -53.096 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2826a41-b48a-34a5-9502-931113fb3d1e | 0.09311 | -51.20986 | 2024-11-23 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22316c5a-01e2-34a0-8722-c48792a3124f | -1.28864 | -51.73546 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8309ca6-8753-3215-bc38-ae855fa18694 | -1.62345 | -52.60636 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f3981fb-2cf8-37ef-93cb-481de922d210 | -1.60629 | -52.58775 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e504b0c-00d7-3106-9967-5a922ea5385b | -1.1958 | -51.97517 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d94ee1d3-28f6-302f-b8cd-b46e51484867 | -2.56503 | -54.06513 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8553903-84d0-308d-85e5-1a886dab0335 | -1.95936 | -52.07735 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3b4bac6-8c76-3783-887c-9ec25799203f | -1.74586 | -52.38902 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccb12ccc-6a53-3916-8749-51c704c80240 | -2.89789 | -53.04352 | 2024-11-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9abbb10f-56c3-31b0-8699-98905fd04410 | -1.40398 | -54.9255 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2da394f9-2a08-3c26-8721-de1adc95ee40 | -1.63337 | -52.6172 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca52daa2-4e27-3b30-b4a0-f3bf7ac74d9c | -1.44848 | -54.97276 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60b085e0-49c4-3b85-af25-5fe1474d14cb | -1.30144 | -52.27824 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8dc0ece-f879-30da-8516-d30c661a2311 | -1.64703 | -52.62861 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d147b2ab-1761-335b-848c-054203fbc8d0 | -2.19581 | -50.6841 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8909e7e0-7b39-3c67-ba62-f9f962fcaa0b | -1.22897 | -53.68323 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfdd7340-6414-357a-8139-0c2f986c35b5 | -2.52647 | -54.01059 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89f4f7e9-f134-3f81-aace-fea52581bbc8 | -0.92006 | -53.09962 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 875075a9-5dbc-3c7d-890a-afce5e5baab9 | -0.30603 | -51.54132 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5370907-a6aa-3895-9997-ece8144364a0 | -1.42406 | -52.66762 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f887603a-d509-38f7-82c0-8e37a07ad4e9 | -1.26776 | -52.12486 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26ab58fe-07f2-3086-a0d6-7733a2243064 | -2.24167 | -53.61977 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b761e5c-19e1-3c22-9ef2-e55f9dfaf3a4 | -2.28996 | -48.42774 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f858ac3-ad47-3372-829f-3fb6aff8f4ad | -1.23996 | -51.78973 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 579fb525-ac82-33b8-9ff6-bfeba0b5a48f | -1.07441 | -53.36698 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f48e308-5ccd-37aa-b91e-48a43d1ad8f7 | -1.77999 | -53.61356 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93a751b2-d830-371c-838b-a9c0a48f871e | 0.61344 | -51.77185 | 2024-11-23 05:10:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b04d69b-40d8-3a59-88fa-599943ff0061 | -2.77073 | -54.071 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 404bb980-bc83-33bf-8e6f-529c93d9efcf | -0.26826 | -51.5509 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1210aed3-c544-3b6c-bfae-d1a356072aee | -3.00497 | -51.55224 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e60471d3-8efe-3a66-a69d-3e42b477f175 | -1.78126 | -53.60545 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 96cc635d-c9c3-391f-97e1-77e68d001a0a | -2.21107 | -53.70825 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ca15841-169a-3813-aa55-20cd96b9d4bf | -0.6687 | -51.66518 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b120c8c-1518-3289-9742-70a61f5f16b1 | -1.11849 | -53.39055 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 46aceca4-15d0-3895-b7bd-22cab8d78769 | -1.35756 | -52.81419 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c703f6c1-b8fa-3743-a635-0ede0d5e8df4 | -1.07557 | -53.36808 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f0c00af-222b-32c1-a54e-7f7993220c1e | -0.362 | -51.57064 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15a667f1-000b-330a-a2bc-7cb7b4082495 | -1.65852 | -52.70432 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3cf11f51-2173-3890-bebe-38686f7acfe8 | -2.74677 | -45.97997 | 2024-11-23 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 556ecae7-0da4-3990-a518-d012e60452e6 | -2.41804 | -48.98331 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| def248a0-1c22-305b-a48a-043c5463a69f | -3.15905 | -45.19909 | 2024-11-23 05:10:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 86329661-b43c-3042-ad23-cb997c9ee64d | -1.20907 | -51.75763 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 271c3da1-1f11-38fe-9755-53372025b69a | -1.15238 | -53.66362 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4ac1b58-edfa-371c-98f0-78ce78bb66cd | -0.9046 | -51.64835 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e82529b-a344-3190-ad88-deead77726e4 | -1.76692 | -52.70481 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8e1918a-ce62-39c9-b3ef-19f51d28949e | -2.73638 | -54.13031 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c34ad21-36ca-3da9-be32-6fbc52f94d40 | -1.1208 | -53.39933 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c82dfc7-5fa9-3060-be04-b90fb5d7e68c | -1.20117 | -51.96599 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 864235d8-6b7a-3c2b-8839-9c990522dbc5 | -3.2491 | -50.11793 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa5edeb6-e538-3827-a4d6-1b19f089de92 | -1.62978 | -52.60997 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a64208e-3cb0-3165-aa9f-2007b9e284ae | -1.45458 | -53.39621 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e224d29a-9e6c-3b6c-b6df-e134e1934ec3 | -2.37159 | -50.38581 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c809b4-664c-353c-9250-3e12be6492b8 | -2.16297 | -50.45953 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88ac750d-7f6d-39e5-be87-33740d32c07d | -0.26102 | -51.57315 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 45143ecd-2017-3c2e-9225-ffe8cbd73239 | -1.48234 | -51.96352 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a8a17a1-b2d0-300e-9120-8f055083d33a | 0.76496 | -50.80582 | 2024-11-23 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dc670bc3-5cf2-3521-b94d-85ab979ee4c3 | -1.11427 | -53.39413 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cb9a0456-b66d-3350-9de6-5aebf910b6c1 | -3.16853 | -45.72818 | 2024-11-23 05:10:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 434e4c01-e8cc-38b3-b4fb-def215986118 | -2.76185 | -54.08177 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8d6afca-8cec-3078-95c5-6d34f82afd23 | -3.70838 | -47.61432 | 2024-11-23 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8df21dd2-2fcf-3f3c-aff0-c253600d6a03 | -2.46007 | -49.03336 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b8f44e4-0b8c-3cf7-998f-09a3cdcdc29a | -2.19427 | -53.65159 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6844386f-4ec9-30d5-8fc2-8a23663f109d | -1.63713 | -52.61778 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| baa5b1d9-8e08-385a-8974-f542cde484c0 | -1.13055 | -54.17572 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75438d5f-7770-304f-9f60-0767c9127bc6 | -1.19319 | -51.9397 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21cc6ad5-6f04-306c-88d7-71ec901a08c3 | -1.41432 | -52.04308 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3493e365-374d-3429-b5c5-03be65b8f416 | -2.74502 | -54.02635 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README49.md)
