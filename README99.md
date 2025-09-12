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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865826e0-0a9a-3130-b54d-a704932b03ae | -4.53361 | -55.68298 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b5120d1-d965-3f90-aec4-1a5400e69e3c | -6.1003 | -45.94352 | 2025-09-12 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3921278a-54c4-3441-a88d-b9d1c1142571 | -6.86996 | -51.96952 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1ae3882-e188-39e7-96d5-173400822687 | -6.63224 | -49.78168 | 2025-09-12 05:16:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64690588-0b64-322e-9313-509c57bd19e6 | -4.94502 | -49.92267 | 2025-09-12 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d13a15-311e-3283-8aaf-ff70f71a6fd5 | -5.7611 | -52.37476 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd32dc9f-b8d1-3852-83ba-101d70f59f59 | -3.6944 | -49.10188 | 2025-09-12 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 020848f5-c206-3a3a-ba4b-87e9f789b77a | -3.59006 | -58.53796 | 2025-09-12 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aaedabb-1239-3927-acb0-8fbfe900e2c1 | -6.46894 | -53.41342 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de624b50-a950-3d1e-985a-6a924a638cb1 | -6.10902 | -45.93923 | 2025-09-12 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b17e3c7a-6a26-39fb-a92d-cf25c5ae9c71 | -4.9456 | -49.92357 | 2025-09-12 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb0f30f7-34e1-34be-86d0-fed5425e4753 | -3.6733 | -47.4906 | 2025-09-12 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5046ac11-0999-35de-a371-a2f085e6f0b5 | -6.17391 | -47.28083 | 2025-09-12 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ced2c03f-8e8d-3291-be16-5dbb56b5468b | -3.04463 | -59.19426 | 2025-09-12 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31ee6be1-7ea7-3887-9444-b3b4de4d9f69 | -5.292 | -48.126 | 2025-09-12 05:16:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7c4acac6-792b-3afe-a847-e2e5c2cb07f4 | -2.99114 | -49.2965 | 2025-09-12 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23dd7f4-3c44-3b9a-b2e1-8cb3b68c5d4a | -4.93509 | -55.78636 | 2025-09-12 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee350cdc-2c83-3ca2-a441-533f5ba495af | -4.48229 | -48.11332 | 2025-09-12 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 49e9fccd-7150-3c19-9578-2237378d6151 | -9.74721 | -48.34565 | 2025-09-12 05:18:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bda20313-1503-32cc-ae53-5f61a43b81dc | -9.77692 | -47.85813 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ed09350f-7f65-3fb0-baa5-28c283cf987c | -11.80565 | -50.57051 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 407c0082-7870-30f5-a088-59cb13a62f90 | -10.08583 | -47.16578 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 858657d0-e889-368d-82db-0543d646135b | -11.18729 | -55.07775 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bc152b1-ce37-3095-9108-b3526af57fa4 | -10.53549 | -51.53172 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5cdd9859-6a81-3d34-a78b-a6f9238b350a | -7.72747 | -50.74097 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f49f88a-b86b-37be-bd53-fb5f1e0e0717 | -13.16636 | -50.08652 | 2025-09-12 05:18:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6817a12-92b4-3750-83d9-c5b622422170 | -10.8507 | -48.16209 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2dd31c0b-1ad6-32f2-9561-f65ca1e9e454 | -9.70673 | -64.92725 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ae26f7-0be8-3053-aad3-dfe57b9bdc02 | -10.70566 | -48.62782 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 843890cb-293c-3218-86a8-aaecece468e5 | -8.08178 | -54.74406 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 664dbc68-6e82-3922-afdf-43aef4163cfa | -7.2246 | -55.05727 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6ffb210-3622-332e-ba11-8d064f0fec58 | -11.31917 | -50.78082 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec29be94-64ff-3f0c-9d63-3f2ae4959437 | -9.48854 | -55.99088 | 2025-09-12 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96fd34f2-e9ba-3a62-94ea-f3769bb8d18c | -8.87448 | -49.5396 | 2025-09-12 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb603b26-3d2d-3a83-9633-d7b99c96619e | -10.4355 | -50.61881 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b09dbe6e-5792-3dfe-8093-486184d1722e | -11.94882 | -51.17611 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cc11d147-d4b2-3e22-b35a-d2b869d69d88 | -11.95944 | -51.17753 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9e4e9a3f-7144-3409-b5f4-832b97d77777 | -6.83757 | -52.79759 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf82e83c-3a75-309e-86fe-4d4f823e4dfb | -9.71404 | -46.88083 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46f31a61-4352-355d-a05b-3deecacd13c7 | -11.81116 | -50.57125 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96f28519-e50d-3b26-8cd5-769698d9a386 | -8.46084 | -47.26526 | 2025-09-12 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b28966c0-f174-3824-864d-82e541a2f12b | -11.65201 | -50.58715 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68919428-b6b5-3ff2-8be5-6e82f4fce444 | -9.98278 | -51.70446 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a3d278c-d4b6-318e-a755-300a092f10f3 | -11.18376 | -55.07355 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fde6056-22b4-3335-af44-961943427021 | -9.0406 | -47.05426 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f6b31df4-87b1-3525-a682-2dda05004867 | -11.16052 | -57.18124 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 849ebf18-2cc5-3574-aed0-7c69390b2c40 | -11.22418 | -54.99104 | 2025-09-12 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9ba72f7-fcef-3bf1-a0b6-66846de25a0c | -8.48665 | -47.27039 | 2025-09-12 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3019178e-ad37-3b68-a5e0-ea0c3b4ca8ef | -12.24442 | -46.75417 | 2025-09-12 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47dac738-b406-3331-b364-bbe471c590ec | -10.38165 | -50.50272 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b4a6b8-2d05-3ac8-95b9-d273d0a25dd1 | -7.42199 | -50.65908 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 514e0a68-21f7-3925-b688-c4bc1cec0a70 | -9.3381 | -65.46211 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f742dbef-ca7a-3e87-b281-95b89a894940 | -9.9957 | -51.72223 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1bc0883-096b-39a1-af6a-86308c97e5c6 | -11.19082 | -55.08187 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87b1fbcd-3eff-3083-9763-c54ad319a681 | -11.92566 | -50.69424 | 2025-09-12 05:18:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6287ad7-51ce-3af9-b722-0326d90410f3 | -11.48476 | -49.27073 | 2025-09-12 05:18:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcbb3743-fb55-32d6-ae5d-7121a8a4bb02 | -9.73003 | -51.00387 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1132470-2b00-3a35-b9a3-d22c23c44439 | -11.87041 | -58.82547 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc15fcf1-a243-3eaf-904d-5ec597ded917 | -11.88276 | -58.8236 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11cb6778-c178-3fc4-9664-ab7fefb13a99 | -11.94351 | -51.17545 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e142c989-827c-33f9-925d-2b92717b1d92 | -10.6716 | -48.5978 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ddfcb81-9c15-35e3-b443-6adc16929325 | -9.78397 | -47.8536 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2cb5ccb2-6c79-3520-9d4d-ef870c109afa | -11.87488 | -47.52751 | 2025-09-12 05:18:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8f0b1bc-0182-389b-bd79-5cfe844a5315 | -7.38625 | -59.69376 | 2025-09-12 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e80105f-0b73-302b-a6d2-c269f581f614 | -9.66811 | -47.5577 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 033a51f7-c02a-3bf3-abbf-eb1f9529dbff | -10.42538 | -60.81439 | 2025-09-12 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cff10577-dde2-3fc8-9e29-4d1e4513fb35 | -11.19536 | -55.07886 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b935a4b7-b6d8-3ff1-b8d7-f9e79304b620 | -10.5284 | -51.50572 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fc2774e-44fc-37b9-a895-a0fff0e964da | -10.08656 | -47.15971 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abab6738-9840-3f1c-9aa4-029696b9be95 | -11.71837 | -58.1839 | 2025-09-12 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c412066b-fb51-36b3-b8d5-17338258dcff | -13.17217 | -50.08717 | 2025-09-12 05:18:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa7abe4-78f8-308e-b9dd-7de4a6de6652 | -8.89655 | -49.93833 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 72730612-535f-3513-ac92-733ebc27530a | -11.95855 | -51.17482 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c8894f64-8338-3b2d-864e-ee228e19d8c3 | -9.9718 | -51.70592 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8d3a4279-6da7-3bf4-827f-8af68ea601a4 | -12.08523 | -47.59307 | 2025-09-12 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 13f45038-107f-32ed-819e-ec65ca3662b2 | -7.81486 | -55.22632 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77807c2f-e248-3af7-b902-dde1cecd0090 | -8.95037 | -46.72748 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| d7b00ba6-32a4-3307-8451-da9d2a0bb359 | -9.34012 | -48.94909 | 2025-09-12 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd9cda46-a942-34b1-b076-489060335dfa | -10.70617 | -48.62349 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40f54b90-3daf-3399-a561-334af45de51b | -9.05812 | -47.0421 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9d349c8a-dd8c-36f7-b2e7-824ac13c269f | -9.25335 | -57.06622 | 2025-09-12 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6584721e-0b7c-3567-b532-c40c19da2c3c | -9.077 | -50.50443 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 348b3094-709e-3571-af16-3c7a8ce4d96d | -11.9484 | -51.17946 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2feff61e-02cc-3fc7-ad90-5f854b067094 | -9.72094 | -64.94063 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12c77557-0240-3294-99fb-a0dd58cbc968 | -6.82811 | -52.80082 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b5dc0fe-db2b-3eb4-84de-1f70d984037e | -11.52925 | -50.39558 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f2d1c980-4f97-3419-8b5c-a6ce2323d9f2 | -10.71243 | -48.62352 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e911f48c-521d-3a95-b248-39b40cb623e0 | -11.43528 | -48.56771 | 2025-09-12 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33ab3983-088d-3117-9a1c-600418e3e552 | -10.67227 | -48.59547 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90c37b30-5137-3857-8f2b-77471064fef9 | -11.18686 | -48.62293 | 2025-09-12 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab825f8b-4b40-3b38-bbc6-0c5e88bcb118 | -11.95975 | -51.16471 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b82947fb-ef53-3bde-ba86-df938f2fb312 | -11.87938 | -58.81185 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ae1d3b9-c4ce-39f6-b73c-4a278ecd9eeb | -11.80538 | -50.57256 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0f12676-225f-350e-b963-2ff106704924 | -7.49458 | -54.95222 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43e2de23-d47f-3bfa-8d82-68167b27e0d0 | -11.96957 | -51.17294 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bb5da5db-d062-3d99-8216-385aed0c8ea4 | -11.18679 | -55.08131 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 438a8276-3804-36f4-9c16-f06f47b2e1c5 | -11.53382 | -50.59111 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3de89bb2-004c-3166-b122-09fa7af3f620 | -7.49073 | -54.95156 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f504678b-8814-3eea-be3c-7133fbe15b75 | -9.74833 | -48.34511 | 2025-09-12 05:18:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac3d8f6d-477e-3f49-9904-acb0a561d764 | -10.68276 | -48.66232 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README100.md)
