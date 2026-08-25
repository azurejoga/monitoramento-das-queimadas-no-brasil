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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c4bd631-99ec-3c00-850e-52fb4f30e9d0 | -6.60033 | -52.45521 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a7d7121-7d20-303d-88d8-adccc01d280f | -6.63478 | -38.73552 | 2026-08-25 04:25:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 94e200d7-7d81-3462-b694-73a9d38f4dc5 | -6.40309 | -51.70771 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 17edd3b8-ba67-32b3-8be1-7eea4e34b950 | -6.17017 | -53.69998 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c34221af-6743-3d61-9066-d354f532523d | -9.04779 | -50.79565 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c68e970-eca6-3edd-8d87-5b37004a3905 | -3.52911 | -48.18716 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 67f7ea66-866e-307e-95aa-082b092a9bfe | -6.62784 | -58.49431 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 368b8b07-45b1-346c-aba9-374c7ed7848e | -7.1885 | -42.74026 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3467f2b6-e8e6-34b8-bcf4-94a0528e9146 | -6.16727 | -53.50191 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5165ae19-70f5-3c52-9780-cb3b65dd6555 | -8.09875 | -47.46878 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 681686a3-8e89-3d60-bf26-acbab0682df4 | -7.16175 | -42.79896 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7080ddc7-7247-3173-ab0a-c98039068556 | -6.83798 | -52.50207 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e15910f4-8c9e-3e38-a00a-cb399c0d0571 | -8.07273 | -44.65222 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0ce3f3e-7c3f-358a-9ae6-6ec548865a90 | -7.19655 | -42.75727 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d71cad8-09d8-3c52-9e0c-7c7ad5cbac25 | -6.29848 | -43.7986 | 2026-08-25 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 158af3e6-b2d0-32c4-91e1-094f67f29aff | -9.94258 | -48.34243 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 124b8070-f4b2-3db5-bbb7-43d182d4bbd6 | -9.03117 | -50.81886 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a39d6777-48ee-31fb-a31b-fc314646a9fc | -6.80165 | -42.66427 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 054c6708-cbb9-3703-b62a-ef0841ad06a2 | -6.18182 | -53.47933 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fe3ed1d-aa26-33ab-8dea-11c261cecf48 | -6.92099 | -41.52601 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22b72d8c-3b26-35d8-a38e-a5157d970025 | -5.77711 | -57.55331 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b84df3f9-14de-3758-959b-7f32b7421fae | -6.63973 | -45.16721 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c07718f7-c4e9-3be5-a158-07a38d521bd5 | -5.91833 | -43.64204 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6d83b37c-51e1-3bb1-a299-2c3b138b4046 | -5.9498 | -53.60295 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72c99b3d-0bd3-33d2-8429-f799e3e0ba19 | -9.9795 | -48.31609 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 036b8a78-d531-3750-a928-070326a2ba78 | -2.89271 | -48.80198 | 2026-08-25 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1824553b-3b47-3377-9d55-a42ab44b65b9 | -7.30243 | -43.00246 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc87fe8d-79d0-31a5-879b-0415003d561a | -8.21225 | -54.99074 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df43de58-c411-3b51-8b41-ae36b36c946e | -7.29514 | -45.36094 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dbb21865-02c4-3da8-96ff-316e1f57b9b5 | -6.34518 | -54.77188 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af32debf-2f99-3183-a407-2d56fccbf66c | -7.0641 | -44.99722 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71adaa67-7ebb-3077-9f6a-5a106a738f47 | -8.10851 | -47.47422 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f48702b3-3234-3a82-89f3-77013fd2f5c3 | -8.20391 | -54.97379 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cfc048c-0e27-3811-866f-6b1ca13868cd | -7.15886 | -42.79462 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 80b8d286-f5ae-3913-884a-94fbb32c7f55 | -9.93906 | -48.34185 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64b572ad-2d83-3ec3-8322-3c5a215452f4 | -10.30612 | -48.20646 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d6500e0-cbe9-3a50-ba7d-0ccb981ca4f6 | -6.12593 | -57.82711 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 88695570-4687-325f-a7b0-25b91f9bfa72 | -6.17631 | -55.44383 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 149e2019-134d-386b-a5c2-dcedf1ba587a | -9.974 | -48.3274 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71c1b590-30da-3527-985a-4ef2af1ca6aa | -8.57378 | -54.85207 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1a7600b0-7eb3-33ce-b3a2-adbf4d71eaf7 | -6.80623 | -42.68054 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 026c97cd-a73c-3673-863c-50f7a843a4a6 | -7.24432 | -43.12781 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 117c6a9c-e0bd-31e9-862b-7a384dfff3a8 | -6.45306 | -41.55748 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0025357-8c08-3f48-8b52-ce7ccd32f640 | -6.35764 | -54.76661 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf84eed4-6975-3410-8d0c-601226fe236c | -6.01698 | -44.85186 | 2026-08-25 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 495ab06a-b2dd-39ae-9d01-8eb860a31f23 | -6.34595 | -44.07996 | 2026-08-25 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21f4ae42-9000-3b1c-a78a-d78cd302fa09 | -5.93716 | -57.7312 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f41924-a3cf-3102-b147-49a8edff3a47 | -10.03968 | -46.40879 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad5b5271-2d0f-344a-bb15-e9cf63cfa781 | -6.73183 | -47.43391 | 2026-08-25 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d415b9c-b7e3-392e-bdb2-a23c763b0cc8 | -8.59565 | -54.73533 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f34254b-814b-3887-bccc-738fb9406cf5 | -10.3144 | -50.40123 | 2026-08-25 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f1d89f9-9ba2-3da5-a8e2-93864aedebd0 | -10.36824 | -45.06136 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e664a26d-1cae-3cb2-9ec8-760ade9821aa | -7.44459 | -43.12297 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ef09f62-df99-3d93-b552-5cf2734b8ea0 | -6.96878 | -59.08678 | 2026-08-25 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8c18797-db27-3eac-b4fc-139d85bf70d9 | -6.14727 | -57.93907 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94e22858-2818-3470-a1ec-14499fe6fb28 | -7.18155 | -42.73919 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c55c740e-9833-37c1-8837-379438c1451a | -10.02576 | -46.43175 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60025d0f-cf27-397f-9ced-b8592dd1cb8b | -10.05061 | -48.45449 | 2026-08-25 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4203f912-b6cd-3a49-b141-2d22238f96b3 | -7.29679 | -42.9707 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1e0a4e1-1bdc-35af-ba41-fd28046dc455 | -6.20536 | -53.49626 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 692efec7-52df-35b9-825f-c81979a98fd0 | -7.88663 | -46.33538 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| affef27e-5d5e-3e6d-9566-b91bdc97ed79 | -8.56689 | -47.43441 | 2026-08-25 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 553baac4-195a-3a30-bef7-80d1f405abbf | -6.83925 | -52.498 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65f6c321-8170-3dc0-a5cf-4647e8fbd7fe | -6.18128 | -53.48241 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26acee09-036b-3496-9243-842b2213c9ac | -6.32556 | -54.75304 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96d9df8f-e828-3cc6-ac2a-5451a7540f62 | -8.57356 | -55.2811 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23cd0f47-dfad-34a9-8ee9-6cd403b29b3d | -6.45734 | -41.55377 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5e22c64-2037-3828-9b08-5cc1fd2e6996 | -6.61139 | -58.3889 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70d30957-20f2-3b76-a924-d1f0bd5f375a | -6.14719 | -57.94547 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ea7b6fe5-6951-39fd-95af-b4843d6fd750 | -8.08315 | -47.5212 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbd0c2de-5e12-353d-b9b5-fe8b5e62f0b9 | -7.2786 | -45.3583 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5dfa1d17-2596-36f0-b1ff-bbfe09eaabaf | -7.76363 | -46.15263 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d4c81f3-bdba-312b-85be-37b48d95ac3b | -3.53288 | -48.18776 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 0bcfe475-df58-302a-97d1-0c31842194c8 | -7.48396 | -44.46618 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b61a995c-2f0d-3262-876b-68a49be3e11c | -6.33045 | -54.75779 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4abb492-ebc2-39b7-a595-ad588b71f0df | -4.12729 | -49.4514 | 2026-08-25 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78a38013-692d-392f-a8b4-43b4778791f3 | -7.48063 | -44.46566 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 173e0d31-ba2d-3f18-a9f5-a2b551b605f8 | -6.34295 | -54.75237 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4d8b824-fbc2-3ef5-836d-e1c41a7e7af7 | -5.77219 | -45.79401 | 2026-08-25 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 446a2ee2-63b3-3d1c-b14c-722af830c8c2 | -8.02686 | -51.79307 | 2026-08-25 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e3ffa6-9c2a-32bf-aa0f-44b7a20d8b21 | -8.61801 | -54.70449 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 553fda4c-7814-3f7f-a7c5-4f9c470134c7 | -6.32624 | -54.74932 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4beefc7a-a920-3da2-925e-398f20a80abe | -6.43587 | -54.96328 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72deb867-e1ae-3c46-9021-2297062ba4ed | -6.12359 | -57.83967 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7433489a-b90d-34dd-8956-9c6ab1e41d0e | -4.48162 | -43.90472 | 2026-08-25 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21b8fa13-321a-37c7-ad0a-3dfbf332a8a2 | -7.89588 | -46.38441 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca4f573d-b325-32cb-beff-6d20d0d91024 | -6.79464 | -42.68655 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1a7afacd-3875-3124-9127-c3ea9a58fe22 | -10.33488 | -48.22745 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8034803-e266-3c3c-ba31-989ff617f7bb | -8.07769 | -44.64225 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88151b8f-8208-37d7-b796-a605d75d262d | -6.60457 | -58.38319 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40f5a935-1a3e-3380-b321-79b630e95f24 | -7.42859 | -43.08981 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af56e520-ad04-31ec-a2cd-3bd1b7b8edba | -7.18548 | -42.783 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b4b2c35f-2065-34e5-b437-4f0e63f8e689 | -5.95555 | -53.60066 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85a59234-5258-3f97-b4c5-f74f2cc1d123 | -7.26646 | -45.37058 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c0af1a0-46d1-3b4e-8211-198736f04e6e | -7.30712 | -42.97232 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9d93e0d7-a8e4-3470-a135-cdb0cae7ba59 | -7.3077 | -42.96856 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d9ad108-b29c-321f-9764-f66032ce6712 | -8.32155 | -45.70016 | 2026-08-25 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3394f427-3ce9-39f2-8f67-44b015b42beb | -9.03393 | -50.77844 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73afe16d-da0b-3a9d-bd3f-0ea423514594 | -9.38157 | -45.4212 | 2026-08-25 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a076d2d-0d57-34df-a862-0baccdc6d699 | -9.70274 | -46.0519 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README29.md)
