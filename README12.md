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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cefac12e-988e-38a7-befb-4bf62e2ac205 | -3.42538 | -48.94012 | 2026-08-23 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20cb784e-5728-34be-b5f8-93234a4b9734 | -6.19266 | -44.85864 | 2026-08-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbc00ad0-6d23-3b76-ac38-4bf9b3d33c56 | -7.03812 | -48.02212 | 2026-08-23 04:08:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9ab9266-3a53-3868-9a00-aa23d729a499 | -6.89247 | -55.70263 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c5a2ab4-1ee8-3b6f-bf01-4dd19a5000c3 | -1.98589 | -47.96816 | 2026-08-23 04:08:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c181a52-72f4-3849-8c1d-705f2dd93d48 | -3.51399 | -42.10671 | 2026-08-23 04:08:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c2bac2dd-bfc6-36ec-ae4f-6c1ba7faccb9 | -8.47792 | -46.99409 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90857d40-2021-33c3-8660-68df5c9afc04 | -4.30637 | -46.41848 | 2026-08-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85ab3907-f8a5-3d55-abf3-28fdf6e5d2a6 | -4.17547 | -42.44632 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 521c3571-d7de-33ef-83c2-aa295cb99f82 | -5.96108 | -53.62667 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6439ef4d-c5fa-31d0-b65e-074275b79ef0 | -8.38121 | -47.39188 | 2026-08-23 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a164eff5-fad1-3a11-8212-a97bbebc9067 | -8.45749 | -46.99382 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3695634d-0d9e-3346-9d76-acf0a31fcd19 | -8.98364 | -50.76164 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6029ef11-4383-3fbd-a17a-afb8e3c6310d | -3.7044 | -53.69267 | 2026-08-23 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edc588fd-0813-3d6a-a28c-7e59d83ce188 | -9.01204 | -50.76913 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 88e7d40c-1536-3f95-b07a-61e03454dfa5 | -6.79852 | -42.6754 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d7863eb-a508-3069-ad3b-dc00bb5e6604 | -9.72689 | -45.28425 | 2026-08-23 04:08:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aed146e8-8319-39e9-a497-cf380be6422b | -7.18438 | -42.7511 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 818884ac-c5d8-3a11-a615-5caf51286b33 | -7.07285 | -45.00531 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32577aea-7e9d-398e-8514-deb1cbd98a8a | -5.29884 | -47.50033 | 2026-08-23 04:08:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2257cf9b-556a-3908-bc61-6a4db9b06d3f | -8.08496 | -47.26249 | 2026-08-23 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5e18798-5d6d-35c5-950f-b70c6800d454 | -8.58253 | -45.54776 | 2026-08-23 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff1fc1f4-66ed-376b-bcb1-c7ecea106eae | -7.68821 | -50.75099 | 2026-08-23 04:08:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e489cb55-0432-3175-aa78-2dabcc833005 | -6.37931 | -54.97548 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71843448-5f8c-314a-a320-72f1e7054b46 | -4.65299 | -38.12971 | 2026-08-23 04:08:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9abe508b-6123-3912-84fb-e7842389de26 | -7.17549 | -42.74607 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 942eb088-6429-30d1-adcd-b20a67a9834a | -8.17642 | -44.44526 | 2026-08-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3344034f-42a1-36d5-98a6-0276e5b23da9 | -8.16237 | -46.71671 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37621232-90a1-33f6-a4be-5bf0a75b3461 | -7.39665 | -45.98769 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30372d61-bce3-3a58-99fe-680a4c788e1b | -3.01312 | -51.05531 | 2026-08-23 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98398844-ba3c-3a98-b41d-a16e29f53b5f | -7.18771 | -42.75163 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f18258a9-6509-31a0-9da6-74fbc7d29158 | -7.15049 | -42.79632 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ebcf6825-4596-38b9-bec9-a54eb133906e | -8.97955 | -50.75515 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 38c2b4bc-509b-351e-bd3f-0585e8befc1b | -7.30697 | -42.98846 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 87d036f1-13f7-3b41-aa21-6dc507d68144 | -2.50065 | -48.13696 | 2026-08-23 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fef36d31-b2e8-3c68-8521-66e1888f7461 | -7.26341 | -49.874 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1318de33-9977-3e55-9c4e-dee006bd512f | -8.97779 | -50.75587 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb0a5380-99f4-30d4-9bb9-e776f837131d | -6.95538 | -42.69642 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3d4b008-23ae-3375-af85-70917da56b61 | -7.42657 | -44.68417 | 2026-08-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0874aa27-f0d7-31fb-be1f-b4842397e4af | -2.55819 | -47.24791 | 2026-08-23 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2e1002a5-b8cd-38ca-8ca3-f3905d6c0ed6 | -5.01396 | -47.06634 | 2026-08-23 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28873335-6a5c-3b15-807f-d99ac479dd7f | -4.16594 | -42.44119 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5f18ac8-8fea-3965-9003-0ba046474b96 | -9.79892 | -46.61204 | 2026-08-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59ccc01b-16aa-3fad-8e76-faad1f0f1e82 | -7.2538 | -49.87091 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3e397502-40ba-3eb2-9be8-15ab74706d22 | -9.57105 | -44.57215 | 2026-08-23 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9488fb68-68f8-31cd-996a-b387d680c384 | -8.99137 | -50.76752 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ac12411-696b-38fb-a734-c46051e30a25 | -3.69114 | -50.93217 | 2026-08-23 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed5fd44d-0905-33b5-81ff-e8b8386e233d | -7.18715 | -42.75515 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 635561ee-45b7-310d-ba8e-2645e7ed7b34 | -9.79969 | -46.6074 | 2026-08-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f138a70e-637b-36af-8f70-b0982e6c6a62 | -2.56264 | -47.24858 | 2026-08-23 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8c0aa943-b66c-362c-8320-26a132d937b7 | -5.16662 | -45.05814 | 2026-08-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a42e56e-fbe3-30cb-8ba4-71a72c5fdc88 | -7.48361 | -46.09727 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b872189-cc35-39fe-adad-76de6b7697ce | -7.1563 | -43.09959 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf0d262f-9b67-3ccd-8a99-9aead976ed59 | -6.8989 | -51.56642 | 2026-08-23 04:08:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 707c3d83-1211-3eec-9487-d7d6d771e345 | -5.61843 | -45.70491 | 2026-08-23 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b4a2978-18fa-3889-aee3-7f14c26df10f | -8.93051 | -48.54156 | 2026-08-23 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a77e707d-f6cc-3285-b283-8953ff523971 | -7.28797 | -43.00006 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57670577-d091-38ac-8a1e-61ac6e2be0b3 | -2.35343 | -48.82962 | 2026-08-23 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc938a2e-3a1c-3c77-a490-22d5e8bcffda | -6.55515 | -55.10324 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2a88bf1d-f167-3445-9c1d-6e44a7cef185 | -8.48189 | -46.9948 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce65660-b8d9-3f90-82b1-d8fc5550f3f4 | -8.47454 | -46.98991 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19a4d71-3637-3385-8b72-93647b5a8272 | -6.94393 | -41.75018 | 2026-08-23 04:08:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7a611e26-8c73-355a-acc7-d2ea262b7bc3 | -6.96204 | -42.69749 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d30b93a9-90f2-3794-8f37-c386feaf6108 | -7.64744 | -42.72794 | 2026-08-23 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51818979-6680-34fe-9b32-5b8d23ddbb83 | -6.37489 | -54.96127 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2efca388-a230-3adf-8e80-a978b80ead73 | -7.14715 | -42.79579 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ab7dd8ba-e82e-3763-98d3-20d83df5f60d | -2.91387 | -48.86773 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 593dd6d1-5b42-3018-8faf-a601eb7918a6 | -6.02512 | -43.009 | 2026-08-23 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| acc50677-c996-322c-a905-fe8a28d9ad7a | -8.08965 | -47.25963 | 2026-08-23 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3508ad6b-82de-333e-97b1-d840c72b131c | -5.65348 | -47.08521 | 2026-08-23 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79ea2267-263a-3c3c-891e-2c86a5154fe8 | -8.98877 | -39.93649 | 2026-08-23 04:08:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de3cfe45-5ca1-3603-a3aa-22f98a11640c | -7.14103 | -42.7912 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40cf3319-35b2-3b62-9fdd-0f74ab9de345 | -7.26361 | -49.9021 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 70a2d7e2-4666-324f-8b0d-14cd136ca500 | -8.92543 | -48.54493 | 2026-08-23 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e76ae6e5-8670-3cda-ba6e-0afc67e01f4a | -6.78184 | -42.67279 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e49d9307-afbf-311a-856c-8e96d423c53e | -3.05989 | -50.34171 | 2026-08-23 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b499cfe-a4c6-330f-97ae-102e6bafce4a | -8.17294 | -44.44471 | 2026-08-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1e107e60-a6f8-37b9-942c-e4b0480410fb | -3.51733 | -42.10723 | 2026-08-23 04:08:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 055603e9-56f7-398a-ba61-7bc17673535d | -6.79908 | -42.67185 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f507ca64-8c73-3c70-abec-0131e6d100ea | -7.14659 | -42.79932 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 40382966-b419-3da2-a7ef-552c9d659727 | -8.99081 | -50.77055 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74458f09-9070-3593-a817-f7813b0e9b3a | -6.47343 | -42.47246 | 2026-08-23 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66948208-f44e-3799-8f5d-64938a51b8ec | -2.99506 | -48.96123 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 18cf0dbd-17dd-3d14-a362-5dfe7e200a78 | -6.89954 | -55.70424 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09fd3974-4c6e-3eee-874f-2f33eac47e06 | -7.99277 | -38.32998 | 2026-08-23 04:08:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cca1c31c-5137-3a8c-a68a-b49722273caa | -8.98183 | -50.7624 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 74cb58fb-45b4-3758-87f4-dbca71016863 | -7.17882 | -42.74659 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae612dbf-6cf4-3465-877e-92b60d06de8f | -7.4259 | -44.68822 | 2026-08-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c45600d1-2150-320f-afb1-3a36a488eea9 | -2.98513 | -48.95959 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4975a39d-bb8a-3cf0-b9ef-a35040b2bd00 | -7.48438 | -46.09253 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8323d4f-44cb-35c9-84af-ac2b1ad4a22c | -6.55443 | -55.10403 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec235477-80d7-378f-9102-96166213b785 | -3.37219 | -39.50232 | 2026-08-23 04:08:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ac21ece-7a2b-3c2f-9fa7-9b429a4d8816 | -9.01811 | -40.99567 | 2026-08-23 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3273ce16-2ff0-3252-b842-59387e971006 | -7.12943 | -44.54807 | 2026-08-23 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b57288d-f0cd-3412-b418-65636757307f | -9.02258 | -50.73997 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7191693-2a47-3136-9c32-b014a00bc5b9 | -6.95482 | -42.69993 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70e620bd-5634-3da3-a726-8b83ac5f35a2 | -6.80242 | -42.67237 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 883531af-950b-3fe4-8f1e-ebfa76db0031 | -5.05207 | -39.18055 | 2026-08-23 04:08:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 342df596-4be2-3e60-8330-ce386c7d8b6b | -10.74942 | -40.26764 | 2026-08-23 04:08:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b1f618b-30a5-39d6-b46b-5ab029fe107d | -2.99102 | -48.95475 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README13.md)
