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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e1f1f4-c12b-36b6-95c1-e329f1a3d106 | -9.11828 | -45.82328 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bc285e2-3c3a-3f77-b99f-1b71a5107882 | -11.76274 | -45.45892 | 2026-10-10 05:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 68039ff4-d6bb-3bd2-90da-04b755eb0f86 | -10.89826 | -57.08589 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c0edd4b-82c3-35f2-b5a5-8752b7759493 | -8.48924 | -54.60572 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1548cb9-cf0a-31d0-83a9-ebd23d1d26ac | -13.91359 | -48.91592 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb4f0ae6-bde5-3a95-a2fc-d718ca0a2cc2 | -12.45168 | -51.39403 | 2026-10-10 05:06:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45ec190b-adab-305d-9ea3-52777893df9f | -11.09704 | -47.63923 | 2026-10-10 05:06:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 799d2b8a-93c4-31a1-a6f7-4a33ee397cee | -7.914 | -54.71999 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0520445f-6754-3b9e-a365-d94e81927892 | -12.25216 | -44.42779 | 2026-10-10 05:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c2c4b7b-f2c4-34af-9191-8ebfb3754348 | -11.82879 | -55.52662 | 2026-10-10 05:06:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8df4a89-05cb-316d-8427-04b3607794f1 | -11.83852 | -43.6148 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ea2c43-3796-3c78-aed3-143d28ca906c | -12.01797 | -43.44001 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55327a04-f778-34b3-8b20-d1899e270c5b | -9.08839 | -61.04833 | 2026-10-10 05:06:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 180ffc95-a5f0-3037-b2f3-68296c267206 | -11.42877 | -62.07839 | 2026-10-10 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad3a39b-7e21-34a8-82d1-d402a1e659ff | -8.75465 | -49.61113 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 794f7944-6725-32e0-ae1c-0d4898420dd6 | -13.39094 | -43.88628 | 2026-10-10 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6965d334-3d27-3111-8e51-e1ccddc0aa36 | -12.36824 | -46.61114 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d93fffc7-b191-3fd8-8601-649635543616 | -11.1952 | -44.87923 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32625a9c-26e6-3cf9-b8bb-af8c705962a8 | -14.45302 | -43.93555 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4475bcf0-92a0-3992-8928-ffc17037b770 | -8.28604 | -53.91116 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 590c575c-6abd-3527-ac21-dd965e1b1399 | -11.96042 | -43.47874 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41949540-c00e-3d2c-9a4d-dcf3066865b6 | -13.50618 | -48.59811 | 2026-10-10 05:06:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a2d7c38-7c49-36b1-90f4-6233ff3906e8 | -7.90905 | -54.72986 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8b5f7ee-9237-3391-86e1-c70c1ba16546 | -9.75384 | -53.87738 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66e91f30-53c4-3676-b344-3b2ace63d53e | -11.3851 | -55.15264 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26a89c5c-4cc3-3f35-a8d1-a5e7043363c6 | -9.1772 | -51.38115 | 2026-10-10 05:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03dcc036-6f69-3955-8e5c-22898e585bee | -12.22777 | -57.12921 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3e35abf-0cb8-3b16-9796-d5990947c7f2 | -8.00361 | -62.03119 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee72b4c6-0455-385d-84fc-79f25072ba42 | -9.30444 | -47.37634 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c2a835f-6b94-310d-a20e-df47a612e633 | -11.05122 | -49.56173 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ab9a2be-c602-3ec3-ba61-f526a5a5a8d8 | -13.91885 | -47.85163 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3563efee-8597-3609-b705-b1e0838ec3ba | -10.61125 | -60.47635 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f5f9e4cb-788c-3ada-9e62-3ce1ed8863d9 | -7.22643 | -59.6501 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fbf319e-543e-35ed-8c63-8ccfa4a26489 | -11.46356 | -43.38009 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3363d82a-69a6-3015-b73b-bd10f1b656ca | -8.30435 | -54.70109 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c576515d-b4da-34df-a2cb-0eac2c027a9b | -11.01865 | -49.11583 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a00d2e97-9665-3096-b04a-3db04ff36f9b | -10.89253 | -44.79904 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ac3bb9b-a8f6-36f1-95fe-2d4b1d6535f2 | -12.38374 | -46.61641 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 117805ef-e37a-34a1-88ed-bb4a7ba40136 | -11.39102 | -47.58473 | 2026-10-10 05:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3446eab-b321-3e75-9df0-3f5ca0354aa6 | -11.84148 | -46.81148 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e28b7b-1952-3274-83cb-4e845c96f957 | -11.77967 | -45.50893 | 2026-10-10 05:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a863d50d-3f4b-3728-a2d8-39af9bd7c67d | -7.90518 | -54.71148 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8e9e89c-259f-32e9-9712-9e93dc586bdc | -12.49511 | -51.29186 | 2026-10-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf169181-86fb-3114-85eb-1055bbc959ba | -7.46022 | -63.64458 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e792cc6-aa9c-3eb4-babd-2f7567747682 | -13.16482 | -54.30723 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b7d6f70-b164-3d2a-a44c-00ba83338d7d | -8.17693 | -54.71282 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4421f93b-fb11-3f24-a0aa-a58b188b2319 | -10.60064 | -60.48929 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b376df03-f60c-309d-b1d7-c85f5ecb52a0 | -9.31784 | -60.075 | 2026-10-10 05:06:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 048f6302-47a9-3096-a89f-20c4b8c13bd1 | -9.29269 | -47.3906 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 39c11fc7-95b2-3f32-918f-31efb2f4aeb5 | -10.89578 | -44.821 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d8442a85-aa90-3033-b8d4-cd19e462a80d | -8.94773 | -47.37932 | 2026-10-10 05:06:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93e9e973-b65a-3223-ae02-24f4a8e1418b | -9.91145 | -48.12889 | 2026-10-10 05:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8dce72f3-eba3-3167-96f7-21f14ed3fd54 | -11.08145 | -44.11066 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bfaf83f-3768-38b9-b7b3-7e4391798c3e | -9.2501 | -62.30785 | 2026-10-10 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41ee64b7-ca98-3e70-a1cf-5de5392546fa | -8.8716 | -50.18951 | 2026-10-10 05:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70808121-b3ef-311c-bb32-3e673c296244 | -9.21239 | -57.72444 | 2026-10-10 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 993abf11-cc4e-3a4b-a978-b0bba870211f | -10.60255 | -60.47853 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e45adff2-7b5b-3148-8828-a994fbed7d1a | -7.91235 | -54.73039 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e9b1b58-c5dc-37bf-9112-b906f3d9bd46 | -14.46061 | -43.93197 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab59fd87-8571-3b43-9c78-d5e532235225 | -9.75664 | -53.88152 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23460daa-5e41-3dda-874b-a989b9520d96 | -12.92746 | -47.4386 | 2026-10-10 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f1eaa3a-aaf9-3067-a4e3-9d71057bf5c9 | -14.89479 | -47.23191 | 2026-10-10 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b47a4c8a-a0c3-3338-a5ab-95dbbbc4e146 | -13.03282 | -48.52074 | 2026-10-10 05:06:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34408fd4-3bed-30c9-8fa0-322e4d8e3ea1 | -14.03047 | -48.76546 | 2026-10-10 05:06:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7a3bd6e-3f9f-325c-a56e-9608625148d4 | -10.24884 | -49.66164 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0ba43f9-203d-3725-811a-6ed3cb92579b | -11.60434 | -43.75172 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 220a6f77-bfa5-38ef-a1b5-6e6ebc7b1c6b | -9.28789 | -47.38993 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| da4fa588-27ca-3f77-826b-7f59dab54ec1 | -8.79704 | -47.57964 | 2026-10-10 05:06:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 844a7cc9-299c-3a00-8cb0-c4e587bc17b3 | -10.88177 | -44.79438 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 633d83ee-ff72-3e86-b57a-2d3fbdeda734 | -10.67707 | -58.73508 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 310ac360-5956-3689-8b55-815d3ae17fda | -13.90899 | -48.91512 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17d03f8f-04ee-3983-8d56-1bbb63ab1376 | -7.89801 | -54.71389 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63c97724-73d6-3486-8a62-8da7423c86f4 | -11.85895 | -43.55211 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7de4a219-7c30-39bb-8426-df1568d98e68 | -11.08992 | -43.99345 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36084df5-fe64-302a-ada4-3d27eb030d4c | -13.38396 | -43.89081 | 2026-10-10 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9151a8ef-4923-3c92-895a-182033bacabe | -7.88961 | -63.77952 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2b52d75-cf66-3710-8b35-6f7177ef437e | -11.38124 | -55.15562 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c5b98ae-cafe-34a7-968c-979154e3bc2b | -11.83978 | -43.60427 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78c88b43-b498-37b1-b90f-34bc9abda8e7 | -9.79392 | -60.48949 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f325da4-3a03-392b-9628-a4e35331474e | -7.91511 | -54.73438 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89b1c442-30b3-3dca-ab1a-7ad1851990d8 | -8.07904 | -55.30629 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b18dd2d-f660-3bca-9fb5-00e93f7f81aa | -14.44545 | -43.9525 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f1be654-772c-3380-8ed9-1e203b391077 | -13.15582 | -54.36655 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22b27d05-c904-384e-9d7b-368e9e7aad90 | -11.97263 | -57.61629 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d83bf422-32ae-338c-8f4c-073648d39a9c | -12.28975 | -63.37706 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1db0da0f-a413-321d-a541-d505a221b643 | -13.9084 | -48.91971 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 774991cd-d8a3-359a-8a7c-3bb25b059c3c | -10.59724 | -60.48501 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7cb267b2-2fe1-3fde-8002-e07768b3a678 | -12.37926 | -46.6091 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f42ef67-1883-3aaf-b604-53aa55ce5ea4 | -8.77157 | -49.60985 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68b8fd2c-46ec-3eee-829c-962a9ecb54de | -8.22738 | -61.1837 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 343e8f18-f238-31d3-9caa-4326587d4bd0 | -13.77026 | -48.13412 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2103da5e-c8ae-3d2e-93f1-dc561c5b5055 | -9.95643 | -55.33731 | 2026-10-10 05:06:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 270c40a5-4113-362c-afa6-dfb4708ff2b4 | -8.58082 | -53.10201 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a29d455f-cd1d-316c-9f7c-cea3267c8a64 | -9.11166 | -45.832 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 506eb7cc-3a8e-347b-a9bb-4792a3964317 | -12.73032 | -47.01031 | 2026-10-10 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c378be9-048d-3911-a60d-87f27ed900b5 | -13.24819 | -42.25822 | 2026-10-10 05:06:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 250dca2b-8c19-3e39-a353-2f7d83b58b0e | -9.94247 | -44.88735 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e943c4e-9450-3f53-a28b-fc30a1424769 | -11.50899 | -49.89979 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dce58e3-40ec-3707-9743-571c4159c6f0 | -13.52538 | -47.42442 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d68aa2d6-084e-3af7-988a-1d92bf3b1f70 | -7.5744 | -61.54647 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README135.md)
