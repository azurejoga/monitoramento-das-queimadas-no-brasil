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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c62e1356-fca9-30e7-a0cf-b3424bdc763d | -10.7596 | -54.0384 | 2026-08-28 21:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| a693799e-f644-3f09-89ce-42d4ac3b4aed | -5.9079 | -57.7506 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 1f802650-dda0-3538-9b1d-8110b572943d | -6.7248 | -59.9998 | 2026-08-28 21:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 96dde196-68c5-333e-8cf8-54c5044e7362 | -9.0198 | -57.5574 | 2026-08-28 21:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 483363bc-7c75-3d2a-a9fb-fcce89105bd9 | -5.871 | -57.7715 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| b6ed3bf4-b831-3d09-9981-b520a89b7e7e | -7.5478 | -61.3056 | 2026-08-28 21:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| ec1747cd-185d-384c-804f-fdef5cbf932d | -11.7167 | -54.5244 | 2026-08-28 21:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| c11bba7d-b4f6-3190-8b86-26e567e42a10 | -12.7608 | -44.2373 | 2026-08-28 21:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 946e6df3-28ae-3124-9011-716a0debe41c | -14.9193 | -56.3237 | 2026-08-28 21:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1c7edc6e-7b6a-3b7b-8f1d-9a6a2c15a8d7 | 0.1367 | -60.393 | 2026-08-28 21:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 131.7 |
| c8e47b55-1e54-39f0-8f83-57704f0d7fcf | -5.4179 | -43.1752 | 2026-08-28 21:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| acff1482-6d85-33d5-b796-c2ad7f50f286 | -5.3992 | -43.1766 | 2026-08-28 21:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c3ef80ae-8b62-3a47-acda-3243b9079db6 | -12.7792 | -44.2812 | 2026-08-28 21:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 2039ae1c-7373-30c4-bab6-ccc8fef092f0 | -9.9288 | -60.4277 | 2026-08-28 21:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a78ca09f-3216-35d4-93d7-760c1cecbe09 | -6.1657 | -57.7793 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| f4954642-d603-3bb0-82c8-b576a0bf700f | -5.9819 | -57.6892 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| acac6663-9da7-3f55-ac44-461c58dc1492 | -6.7652 | -63.054 | 2026-08-28 21:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 1d78e7be-dbe7-3674-bcea-7319bfc2ccb4 | -8.6012 | -70.2192 | 2026-08-28 21:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b364fceb-ed13-3f7f-8cf7-9df9f0edbd28 | -14.9386 | -56.3216 | 2026-08-28 21:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c5ba135b-c703-326a-b489-b8a8ef77466f | -5.9078 | -57.77 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| eb7ecc57-0d39-3729-9bc9-21020891029c | -14.4859 | -58.4874 | 2026-08-28 21:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 288da496-1fa2-390a-8751-d73d9f85786c | 0.1549 | -60.393 | 2026-08-28 21:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 51b57fb8-af81-3fb2-9aac-9ffeb94d741e | -14.9389 | -56.3011 | 2026-08-28 21:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e8b18489-a1a3-366a-9f12-2472fc074405 | -4.1934 | -54.5755 | 2026-08-28 21:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0efcea0a-43ba-32b7-82eb-489e99dd6a0e | -5.9079 | -57.7506 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| f8958725-d48c-333a-8aa1-f01552d3b702 | -6.7513 | -55.6853 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 85669746-bb6a-3d9c-8540-619988cf444e | -8.5366 | -55.2625 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| db37c955-dea9-3621-9690-4a2703d7f4b4 | 0.1367 | -60.412 | 2026-08-28 21:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 26c5e10c-ba1e-39b2-a70b-cdefd4f180c1 | -6.7698 | -55.6844 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 7ea9969b-9910-3fcf-bed3-ccb30fd3b3fb | -6.7247 | -60.0189 | 2026-08-28 21:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| d55f61b3-86f4-3e4e-bcb9-f8341fc66a63 | -5.8894 | -57.7708 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 328.6 |
| deaaa663-17ff-3516-b160-0cb632cff233 | -14.4856 | -58.5074 | 2026-08-28 21:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 842399cb-befd-337e-94d9-e9f31f67d089 | -5.8711 | -57.752 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| d1d6b330-07ea-38aa-b7b3-cbab76570bd0 | -6.7514 | -55.6654 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 1ecdc116-6bd6-3b47-bee5-073cff82bcb2 | -5.8895 | -57.7513 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 392.1 |
| 60524b7f-8660-3ecc-9d8a-78f1dc7eb80b | -6.8757 | -59.3978 | 2026-08-28 21:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7608cf12-1744-3515-9669-ba9f5159d9b8 | -10.7596 | -54.0384 | 2026-08-28 21:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 222e1dbc-f9f7-3e88-a727-af3668f1daa5 | -5.8911 | -42.6928 | 2026-08-28 21:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| cabe6ffb-269d-3275-9d6a-0e53c20ff9da | -6.1656 | -57.7988 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 490f2755-c59b-35ec-b0db-31a0937cf4fa | -8.5969 | -54.7755 | 2026-08-28 21:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 9ccfcb1f-55c3-3a34-a250-9d263cdf29d4 | -6.7884 | -55.6635 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.7 |
| df53550c-e50c-3aa7-ade0-dc08af243e78 | -7.5662 | -61.3049 | 2026-08-28 21:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 1b25d52c-19a2-3d80-ab99-65b781935dd9 | -6.7699 | -55.6644 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 471.5 |
| a90c2222-3824-3e4d-96b5-dc46cc2650b9 | -6.8572 | -59.3986 | 2026-08-28 21:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 2d0f1087-ef20-3ba3-814e-3ba43752a82b | -7.5478 | -61.3056 | 2026-08-28 21:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 779e9d5b-e1d0-33e5-94ba-1dd80bc2ce0c | -12.7797 | -44.2576 | 2026-08-28 21:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 2bade30d-5bfc-3192-954a-ddfaf663eead | -8.5971 | -54.7553 | 2026-08-28 21:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6d81388a-fc3e-3d1d-a93c-5c97c0eb4b1d | -12.7599 | -44.2844 | 2026-08-28 21:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0bf36b1c-fb55-3df6-9e59-09f30a7835cc | -6.0004 | -57.6884 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| bc0822ac-3d49-33b4-bb46-7a991835e83a | -15.4952 | -43.7291 | 2026-08-28 21:30:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 77.8 |
| a3dd0fd1-8b6e-3cca-870a-08a2d5845e85 | -5.871 | -57.7715 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 1895099d-2aee-3a27-a2ab-ac9718d7d12d | -9.1926 | -56.9742 | 2026-08-28 21:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| ba01b153-33fd-34ed-b2f1-acd7b89d5cdd | -11.7165 | -54.5449 | 2026-08-28 21:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| ea8509e4-bd9e-30e5-b1d7-fed4c10b392b | -9.9708 | -53.9419 | 2026-08-28 21:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| dd0f6a43-c32a-3b76-a4e8-0c2aa0df804f | -6.77 | -55.6445 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 3b501048-dc70-398e-9ce5-b0d6a9acaacd | -6.7343 | -55.4671 | 2026-08-28 21:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 5a5ed58d-1f3b-35d6-bf55-8dcf73e62405 | -12.7603 | -44.2608 | 2026-08-28 21:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 93a0707c-f38b-3070-af09-f09adbd820ff | -5.6275 | -44.9115 | 2026-08-28 21:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d3aa7f21-4acb-3b18-9c82-b0019c705cbe | -6.1656 | -57.7988 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 344f097d-4820-3038-b6c7-f3e699c6e908 | -5.5962 | -44.2052 | 2026-08-28 21:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 71498efb-5ff6-33ed-8246-e56383ad43a4 | -6.3277 | -44.1028 | 2026-08-28 21:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 0bfd1da9-a46c-389b-af7b-7a4617b79de1 | -9.9475 | -60.4267 | 2026-08-28 21:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 328.2 |
| 69254116-797d-3cfc-b8e4-7f4f5d3ac3e9 | -5.9819 | -57.6892 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 51667102-97e5-3024-b79f-b52b1939f1e1 | -12.7792 | -44.2812 | 2026-08-28 21:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c772bedf-4e04-33a3-beb3-96bb58b51c03 | -9.9474 | -60.446 | 2026-08-28 21:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 234.5 |
| 4a999108-588a-392f-8f9f-8e7368a9395a | -12.7603 | -44.2608 | 2026-08-28 21:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| a0a267fc-4d72-331c-97cc-54a5f44e55d2 | -6.7652 | -63.054 | 2026-08-28 21:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9df65e81-9938-3d79-9a0b-a85886055782 | -6.3465 | -44.1013 | 2026-08-28 21:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 52c2e240-9f7f-36c9-8750-ed650c2c2d94 | -6.8757 | -59.3978 | 2026-08-28 21:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 401bfea4-56df-3b7e-baed-4dd41335711c | -6.0004 | -57.6884 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 9beb8ad9-998d-3337-9275-f2f437d558f2 | -5.8894 | -57.7708 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 369.0 |
| 15ed2b9d-87b8-3d7f-8dd0-80ecffda00e6 | -6.1657 | -57.7793 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 87686429-eac8-3c38-a204-c9a36617bf20 | -6.7698 | -55.6844 | 2026-08-28 21:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 8ce78268-c529-3107-a634-4c93ffdf12ff | -5.8895 | -57.7513 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 422.3 |
| d1413bc5-5ba7-3a36-ad08-628efc0f4e21 | -5.5964 | -44.1822 | 2026-08-28 21:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| cde70bc7-2443-36a7-a7fe-66d318bc56a3 | -7.5662 | -61.3049 | 2026-08-28 21:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 9d251829-3a83-39ef-b5d8-1568b1c0b869 | -6.3467 | -44.0782 | 2026-08-28 21:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e5dd0354-b72b-310a-a46c-fb68b89cfcaf | -5.9079 | -57.7506 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 1d28b94e-a96e-36a3-887f-bde2a01c14b1 | -11.0254 | -57.2237 | 2026-08-28 21:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 218.6 |
| af20ffa8-ddd5-3c0d-9acb-8f53a560d4d0 | -6.7344 | -55.4471 | 2026-08-28 21:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 51d09632-6c7e-3b8c-8cd0-342431d4245d | -12.4305 | -43.3944 | 2026-08-28 21:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 50f9743c-f525-3611-8eb0-c55b655c17f8 | -9.9287 | -60.447 | 2026-08-28 21:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 276.7 |
| 046df842-d877-30d9-a6aa-2c5ce1a387ed | -3.6238 | -59.7851 | 2026-08-28 21:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 82a02c94-5aa2-355a-9380-47171ccf472d | -5.6273 | -44.9343 | 2026-08-28 21:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 251.5 |
| ed2c55a4-2476-3009-9fcc-7feecda083f2 | -5.6272 | -44.957 | 2026-08-28 21:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| e98c6ff9-0864-3eb6-a293-bd445c14f0f7 | -9.1739 | -56.9754 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 35ef2569-cebc-31c5-b5cb-db268a1bb7e8 | -5.742 | -44.6528 | 2026-08-28 21:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 5654bb24-fffb-3b5c-b6ca-ccb1cbbf2944 | -5.4177 | -43.1986 | 2026-08-28 21:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ad58155a-aaa9-365b-a5d9-5582a296fb7a | -11.0256 | -57.2038 | 2026-08-28 21:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 94772133-eaf5-3251-8667-db29d8589d75 | -11.0445 | -57.2023 | 2026-08-28 21:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 164.9 |
| f109b866-096f-3a7b-964a-2d10f69716e0 | -15.4952 | -43.7291 | 2026-08-28 21:40:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 16f45fcc-86cb-394b-8c42-2fb3f4419228 | -4.5695 | -44.0427 | 2026-08-28 21:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 250213dd-6733-3a02-9d66-bd087bd8ce4a | -6.7884 | -55.6635 | 2026-08-28 21:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| e4cfc300-0051-359d-91f2-487833635319 | -6.7513 | -55.6853 | 2026-08-28 21:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 02c2a8a8-25d6-3fa1-86b0-c6b5f5777f3d | -14.4859 | -58.4874 | 2026-08-28 21:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 75fc26a8-4160-3946-8fe9-f418e569a392 | -5.3453 | -45.1576 | 2026-08-28 21:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ea8704ab-85d9-3ab5-8c6a-8b13424786b9 | -5.6086 | -44.9356 | 2026-08-28 21:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 4a2a61fa-fda1-3298-ac6b-dbf64559ede2 | -12.4494 | -43.415 | 2026-08-28 21:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 291e64e6-1858-3c83-aeac-3a7583ce2f6a | -5.8711 | -57.752 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2624e104-0909-327a-88d4-8c85464b62a2 | -12.43 | -43.4182 | 2026-08-28 21:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |


[Clique aqui para ver as próximas entradas](README188.md)
