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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7273da31-79d1-3682-a536-253c0839383c | -14.9396 | -46.95802 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 932c1a35-088c-318a-a7ee-be64e7d22739 | -16.09427 | -42.27998 | 2025-07-26 04:27:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 732229ee-2c14-34ab-8977-98bfcd693774 | -14.1358 | -45.28635 | 2025-07-26 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 472f3f19-6e7f-3ab6-b25e-e59ed2a419e5 | -12.7042 | -47.00405 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcf43c67-1d20-3927-b6d3-53af88c06429 | -14.95871 | -46.99118 | 2025-07-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2c76a68-cccf-3923-894b-60d8ffeb9656 | -13.23575 | -51.14902 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e2dc0bef-45f7-3b60-adb4-85f80b51fb59 | -18.25657 | -44.77938 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 25b12402-1630-332b-8d8a-c0b92f0486ee | -16.09864 | -42.28051 | 2025-07-26 04:27:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 619017eb-b88e-36ca-a2eb-299ce90f893e | -14.94071 | -46.95069 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| df466960-33b1-3bfe-81a6-47c2d4500068 | -13.11033 | -47.3604 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2a81d89-5e9a-3257-a45a-d5b51cf2ccf0 | -14.2185 | -43.95972 | 2025-07-26 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db1aca2c-d7b1-352a-8599-d87ad1b8fa6d | -13.1291 | -47.32695 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1386ed69-971d-3ab0-8cc6-44bf7066ef21 | -13.09984 | -47.36229 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b68349dc-9bdc-3e6b-95ad-9a07a1ee4c0b | -15.02775 | -52.77641 | 2025-07-26 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f069db13-0140-3d9f-8180-badf96c77707 | -12.71859 | -46.2721 | 2025-07-26 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34f7fd9d-e6a3-39e7-8cec-05d323a7e309 | -11.73794 | -48.18103 | 2025-07-26 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d166bce3-2951-3e1c-9204-22ed767b5daf | -13.72612 | -45.69205 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81c40eb7-60c7-38ef-8944-836f4226c276 | -13.6902 | -45.69459 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88417ce7-ceda-3a94-a227-6f916bff9d3d | -12.69254 | -46.99125 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fc7464e-2a12-3f26-b3f6-c11970f6a17c | -14.30693 | -43.78997 | 2025-07-26 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0f9ded1-e713-30fd-9585-782d4ea0cebe | -13.11088 | -47.35688 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 428ceb29-a080-33f2-86fa-b3bde5bf4712 | -14.13701 | -45.27808 | 2025-07-26 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 563f4ce7-2216-3e71-a557-1d7f9faba145 | -13.11252 | -47.34629 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c101d07-b842-3af3-b862-46ccd72cea69 | -12.83761 | -47.08309 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea0d7042-e97f-3540-9f65-e801995d256a | -13.12579 | -47.32643 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2f8deaa-a5bb-3a48-adc2-4d9474a24b74 | -10.29665 | -57.05078 | 2025-07-26 04:27:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db3030c8-1ca9-3595-a1dd-80c8ee1a31c6 | -12.71411 | -46.27878 | 2025-07-26 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0004fb6b-6c66-3975-b6a0-459c479f4811 | -15.7867 | -41.32693 | 2025-07-26 04:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b8316fb4-da97-3a59-876c-a2feb641827d | -14.94184 | -46.96603 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc863463-1329-31dc-b963-d9a10b472ba5 | -15.37327 | -44.27962 | 2025-07-26 04:27:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ba1aa02-f6b3-35dd-84d3-77433fc5029b | -18.24827 | -44.78312 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc29c49a-f2e3-3e52-b027-74b8f98a9183 | -12.71987 | -46.27218 | 2025-07-26 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79a93c9d-1f4c-3b17-9790-07cbca406215 | -14.9671 | -46.98134 | 2025-07-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe1d131-dac0-3020-9a2c-bc5a17953e9c | -13.11859 | -47.32899 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 902785b8-942a-3582-8d15-06048334c3dd | -13.64081 | -45.7035 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eda5480-8fc1-3998-93c7-fcd3e75524a0 | -12.70981 | -47.7947 | 2025-07-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27f94f86-8dab-3cdb-a7f3-2675b03d4afc | -13.11527 | -47.32849 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb874026-147f-30aa-9f49-c968415d79ea | -14.95297 | -46.96076 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc5f9225-4d90-3a8a-b698-ff27f7957576 | -12.68169 | -44.96134 | 2025-07-26 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4668b503-7321-3b5f-b137-2e235834306c | -14.93511 | -46.94205 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dd13f100-0b9f-3f38-bcff-06917106a8f9 | -13.12523 | -47.33002 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2e51c4f-3ec6-34e2-98a3-2e1e690e4609 | -14.95633 | -46.96135 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d19bd1da-dab7-332f-a7f1-d90d2de70aba | -14.13346 | -45.27755 | 2025-07-26 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb19fed5-0014-38df-afe7-9548c2744bbe | -13.10422 | -47.33405 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d32a870-56ef-3484-8301-6ddddc310701 | -13.10863 | -47.32748 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acb5bc67-8a54-3ba1-9005-f67174b55903 | -13.12191 | -47.32951 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 577e26b7-1066-305b-b5fd-f4784cbcc187 | -18.25593 | -44.78428 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 573ea615-cbf4-3200-93a5-4f2e85775a38 | -18.24893 | -44.77814 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4becbc2-9927-3081-9e86-aec0227e5e72 | -13.69831 | -45.6878 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c6eb518-938b-3354-a8cf-23282fee5f19 | -16.66218 | -43.76327 | 2025-07-26 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91aa70f1-abf6-3531-9d36-1b8625483384 | -13.69773 | -45.69173 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb2488ca-001a-33fb-a2f0-c11cc2f550ed | -13.68888 | -47.52671 | 2025-07-26 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a444395d-8457-3f52-ad65-fe244833f8b1 | -16.70326 | -50.58261 | 2025-07-26 04:27:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0be69561-0a79-3824-8aea-2d43a999705b | -13.72554 | -45.696 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 901f3696-f96d-30dd-b426-80219501900d | -15.87101 | -43.28882 | 2025-07-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d63c56d8-d043-3c71-9914-63fdc18e3730 | -16.30107 | -52.92566 | 2025-07-26 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f74a149f-2476-35ae-9428-8b8b9e7c9566 | -13.24364 | -51.14608 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f36a7a3-c8dd-3be3-9a54-bb33d935b2f3 | -13.69598 | -45.6794 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2abcf69-769a-31b5-86cf-e810ed9bdbbc | -15.76174 | -47.7726 | 2025-07-26 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eda61ce8-f99f-3646-a98d-dfe1b64aa8fd | -13.67601 | -44.22548 | 2025-07-26 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f72f5fd5-17f8-3de1-bac7-b67867b14495 | -13.18081 | -42.32561 | 2025-07-26 04:27:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3dd71569-12dc-3a17-808c-4534f71ff21b | -13.71916 | -45.69104 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfa79a43-b5de-3d5e-851e-85e8244af7f9 | -17.70383 | -44.30862 | 2025-07-26 04:27:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d45a533-1faa-3be2-a876-0c36e1dfa19a | -14.96144 | -46.97316 | 2025-07-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4329a2cb-dc9c-3940-8dcb-fdcb7466880f | -17.51277 | -47.99251 | 2025-07-26 04:27:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 991d3511-6dc7-33a6-a42f-a83d6122fd69 | -13.09172 | -47.35025 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ed22b8a-4272-3869-bd62-9a0eaa1e157f | -14.1299 | -45.27702 | 2025-07-26 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eacaad1-d276-3aea-bb44-d58fd3590db9 | -19.01101 | -46.12793 | 2025-07-26 04:27:00 | NOAA-20 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e80e43fd-6d9e-39e9-afe8-6cbf2b45c178 | -13.72206 | -45.6955 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 717f4363-c6fb-3ecc-ba54-3958952595e5 | -12.71805 | -46.27565 | 2025-07-26 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f5ec9c6a-1fd9-3dfd-9c60-44ed3ef5c77c | -13.7012 | -45.69227 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61b0ba50-458e-3b80-b6bf-46fbf8317ce5 | -16.30218 | -52.92363 | 2025-07-26 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9a7de050-c982-30f2-a31d-16145e8ceb43 | -12.77456 | -48.81547 | 2025-07-26 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f6b2f5d-72f7-3f81-88ed-b525984146dc | -13.1781 | -42.32431 | 2025-07-26 04:27:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45003fa6-cbb3-3486-98cf-1fe707fb8a6b | -15.16282 | -49.57944 | 2025-07-26 04:27:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cc6c10d-edbf-3d02-b8ac-28c14825e1bd | -17.04527 | -43.77266 | 2025-07-26 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5e01d8e-a4b9-363d-bb3b-4c635f3d34f0 | -11.92187 | -44.55048 | 2025-07-26 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f682c64-143c-311e-b35c-b222ab499cbd | -13.24035 | -51.13131 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55408679-0360-36fc-b13a-a151cd5e70e8 | -13.10808 | -47.33104 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f546d000-5108-34ce-a1b6-9f6ba4f9c622 | -13.11474 | -47.35391 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9e90242-8102-30d6-8ff3-3d4490cf7f1b | -12.68811 | -46.99783 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb103836-2607-3231-848f-8520cf0bf7cc | -12.70365 | -47.00758 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 581b6144-9777-3bf7-84c5-c05f47acbd25 | -15.83597 | -43.30359 | 2025-07-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b83f531-ec81-3b29-a3f0-24acc13856b1 | -18.17872 | -44.03643 | 2025-07-26 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d12fa3b9-a555-3ca6-be53-dbf80216390c | -13.09548 | -52.13664 | 2025-07-26 04:27:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5e16299-926a-35b1-9659-bb75dd0de00e | -12.70311 | -47.0111 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f51ae4ba-fc33-366f-b5d1-1c6956bd4405 | -14.2965 | -42.82439 | 2025-07-26 04:27:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eca215ea-c14b-34ed-8dde-f4929f6230e1 | -14.21918 | -43.95491 | 2025-07-26 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d2c653-ddb6-3847-a5ca-c7fd02e66394 | -14.94405 | -46.95139 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2eb86c4b-322d-3014-84ed-b837c469ecd7 | -13.54526 | -43.56732 | 2025-07-26 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47276792-b4bb-373c-be0b-aad3bc735265 | -14.29723 | -42.8247 | 2025-07-26 04:27:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a77a56f9-5e0c-3638-9a58-67c64176cb1d | -10.22324 | -59.40683 | 2025-07-26 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7afb8c8-aa54-3c07-8da0-a169c9d245cc | -13.11362 | -47.3392 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 282d694a-ec27-3462-a272-aa85db89c767 | -16.51068 | -50.85345 | 2025-07-26 04:27:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10d0bea4-4e87-385b-81c6-1b69aa59a53e | -13.64804 | -46.82002 | 2025-07-26 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c0688b7-ad16-306a-ad43-02e5a4e7f2f9 | -16.30131 | -52.92861 | 2025-07-26 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d25efe-093a-3cf3-8189-3b5ee84d44de | -13.11417 | -47.33565 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 926d1816-5f7f-3306-b68f-4857ef5ba2a2 | -13.6925 | -45.67885 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c37852dd-daf7-3e43-9436-3725e21fd21b | -18.24378 | -44.78759 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 2790be8b-8a41-3975-b79f-61e8a7f439c5 | -15.78731 | -41.32189 | 2025-07-26 04:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
