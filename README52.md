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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de732bf8-8fce-3582-859a-0e330f321725 | -10.10953 | -45.34789 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 082ab0ae-244d-3a09-b883-28adac9f4873 | -15.03751 | -46.95155 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc478f62-1479-33cf-b2f1-7349eb4494cf | -15.19873 | -56.02249 | 2025-09-27 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e713e9ae-395f-30c2-bcf0-7c05cd3bce07 | -12.0624 | -46.63044 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a321f72f-c9bc-3303-a072-a414bdce8b31 | -11.44662 | -51.49281 | 2025-09-27 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8a7bc9e-a9f3-3232-9f49-9cbbf38b8be1 | -15.2087 | -50.16172 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bcb347c-7f94-3c61-bbb7-f03ce7c13be2 | -10.16606 | -51.56197 | 2025-09-27 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd0eed63-1b88-3e5d-9ad9-40149c1274ed | -11.42771 | -45.01461 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20fd6e46-5913-3bf5-b083-d0d718882df5 | -9.41645 | -54.69394 | 2025-09-27 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76d14937-63a9-3ec1-836f-31b1f728f18e | -11.37554 | -44.9828 | 2025-09-27 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cabe396-a1eb-3556-93c6-2386ea616b24 | -16.12346 | -47.3942 | 2025-09-27 04:46:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3c41eca-1243-3c5a-86a4-96eb8e206956 | -13.07208 | -49.69191 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6214f047-f0e2-3727-a55d-ee5079ae78dc | -15.92808 | -57.49029 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2811beaa-261c-3176-af63-a21abf050e5c | -14.59828 | -48.24561 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe2ca1c9-0351-340c-b041-92383f885b12 | -11.69732 | -44.42146 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75efd442-53fa-3154-9abf-014b0cdcc4c3 | -13.50525 | -47.40886 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a3ce1b1-deac-38ef-9d98-24e9990f8a85 | -11.04955 | -47.65807 | 2025-09-27 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c67f31b-e1da-31f8-94d6-41fb94dacdd0 | -15.69612 | -56.16733 | 2025-09-27 04:46:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77af80c4-a6bb-38e2-83fa-bb463a5eeddb | -10.59805 | -46.28119 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2990eaa1-1b83-3bb1-8eda-c6dc9487c357 | -12.64509 | -48.15276 | 2025-09-27 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79f2771d-7294-31ba-bea6-b489c8a1fbb5 | -15.42531 | -48.20964 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a02c7b89-8033-3990-ba98-253849068003 | -9.41065 | -54.68447 | 2025-09-27 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f74a387e-6c80-3509-b47f-48dc6e7941e6 | -12.2696 | -44.05689 | 2025-09-27 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81d3a824-2cb5-3358-ad48-3f8e3a81d327 | -12.03225 | -46.50758 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66fbb001-b87d-3483-8f0d-bd86fafc3454 | -11.3514 | -45.02372 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 064306b0-592d-33f6-9d8d-94c33b9317e7 | -11.04116 | -45.87819 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05b843ce-2e04-3eae-8499-c5c89839b9b9 | -12.03559 | -47.06051 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a671b382-7e66-377a-ba30-6401dd5602a2 | -12.26462 | -44.05615 | 2025-09-27 04:46:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2592147c-5569-3054-b04d-317cdbc9fbf4 | -13.76241 | -47.87168 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26a6485d-7068-3798-a79f-bdf895957e3c | -15.90514 | -57.49423 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b41e4343-e51c-36c1-903b-48d54311d4c1 | -12.07183 | -45.0506 | 2025-09-27 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c20edf5-b192-378b-82f1-4cad26f7debe | -15.5314 | -44.33149 | 2025-09-27 04:46:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 08d5323b-ed97-3e78-9b66-36805d22dd09 | -10.59386 | -46.28061 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f6436f6-e5ed-31fd-9c77-966baca98e9d | -12.04777 | -47.06223 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e64f2172-9569-323b-9cb3-20b886ca4e9e | -15.94122 | -57.49079 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d45e41e0-3487-3d6b-beee-05b972e5a417 | -15.27114 | -51.46464 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0981c214-40ab-3c56-9656-2a1e5b4086d6 | -12.88071 | -47.09753 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05100f1b-e6fc-3c1a-8829-cc63735c3244 | -11.35537 | -45.02917 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 96aace1f-7172-334f-a702-ecb15a6a415b | -9.8918 | -49.12188 | 2025-09-27 04:46:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3cc5152e-ea5c-3edd-af1c-56106ce1290c | -15.2649 | -56.8201 | 2025-09-27 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06b098e4-ba34-3305-97a9-59281e9113c0 | -13.37745 | -47.82602 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95d30572-5dd0-3803-918e-e1422def847e | -11.97176 | -46.59837 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba703ea0-646d-3a53-9302-c082da70dcd0 | -10.12466 | -45.33669 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d0117de-da81-354f-8017-95e889db82db | -12.83557 | -44.69241 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9af13d0f-70a1-347e-8e87-941649bc8cef | -11.94392 | -47.87272 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0cdf7ee7-9edb-33d5-881c-1a3ab52c8bd5 | -15.29557 | -49.28671 | 2025-09-27 04:46:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48c020c2-8128-3398-a291-7dae2828da26 | -15.19625 | -50.09709 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37283ab8-5e32-34f5-b9e3-142350bf6232 | -15.19921 | -50.10174 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be1ea81b-46da-37ae-9ca5-1811d22ad32e | -10.52319 | -49.56541 | 2025-09-27 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30efa915-c276-34f5-af37-b78256c5c5a5 | -11.29952 | -47.81979 | 2025-09-27 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7ec9a62-46d9-3f62-b289-95800af701a0 | -11.60742 | -45.42276 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05f4af82-8ac9-3379-94c9-4773ac8f1433 | -13.50423 | -47.41649 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 857a7075-a025-3b18-b01c-66c91e5784fb | -15.0122 | -54.99514 | 2025-09-27 04:46:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 684687d0-e2cd-3b32-b472-56fd92e2abab | -12.00857 | -47.888 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ff93c8e-486c-3c57-8efe-7a29bd88e8bc | -12.03055 | -47.06719 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c14d16ee-42cf-3fa6-a6e0-2d051ebda0fa | -10.25953 | -50.24206 | 2025-09-27 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6155520-608f-30d9-a5a6-516ade9fe2ea | -16.15985 | -48.09506 | 2025-09-27 04:46:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68f1d314-026a-383d-b423-77140537c474 | -14.09882 | -51.14276 | 2025-09-27 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28d01301-adf8-3cfa-9040-e3cc79e26f0e | -12.06719 | -45.04997 | 2025-09-27 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cdbd7b3-87e5-363e-be2c-b3c4de824549 | -15.42496 | -48.21808 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a60e6253-5856-35f9-a822-976b9acd7aa1 | -15.91187 | -57.50082 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7e7b39e-b934-308e-8843-d14a55928c94 | -13.61751 | -47.3134 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1c8e5c1a-c9c6-3f42-a1c6-cde368ebda22 | -11.67248 | -44.46153 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f81adb3-bc30-3390-9c2b-8f55ad76ef93 | -15.25873 | -51.47791 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3b8393d2-46dc-3fc8-bbc5-44063e1c3d24 | -14.02181 | -56.10501 | 2025-09-27 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cb860a2-fddc-3ab9-8a38-3278c410857b | -12.27957 | -44.0582 | 2025-09-27 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2138f9d-f41c-33b1-b241-ac5e9a4dee27 | -11.35851 | -45.00515 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9911723-9597-3c99-ab98-1f838441b7c6 | -10.62535 | -53.89029 | 2025-09-27 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d426e6c5-fe0d-3f46-a271-2e06ce983565 | -15.21034 | -56.00986 | 2025-09-27 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63c60265-c297-3a78-a965-6b55fc245e6c | -11.65889 | -45.34567 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 456fe655-0844-38e9-b568-b6026c4fa13f | -14.83774 | -45.61221 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 498fbe89-1e69-3bf0-adb2-c1f568742dac | -11.9706 | -47.90629 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9af57893-c5be-33ca-a673-8c5a9606718f | -13.6389 | -48.07438 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec817a02-2917-3781-a029-74c8b42c9d54 | -11.98281 | -47.90327 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0e95172e-f2a8-3313-9fa7-a60d379cf3d4 | -11.98882 | -46.60828 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f010a04-210c-34e2-830e-eef8882a0ebe | -11.78591 | -44.87041 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2698d3c2-7592-390a-b499-a3126e227cdd | -11.61213 | -48.58258 | 2025-09-27 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0208f0e-d300-3b83-9614-6165a454244b | -11.40335 | -44.91497 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc368eb7-d0f7-300f-bfa5-d8d15965c8ae | -15.29494 | -49.29124 | 2025-09-27 04:46:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 607aa547-fc1f-37fa-94a3-8674acbbc005 | -12.36529 | -44.14655 | 2025-09-27 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7effc18d-d286-351f-8b50-87fadcb1d84b | -11.356 | -45.02439 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f512a8d9-1382-3086-985f-3b1d2297be4d | -11.82474 | -52.39384 | 2025-09-27 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2859ca74-207f-3fde-9c1a-f592096fd1e7 | -14.63552 | -48.29245 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2230cf36-21ce-3c0a-833f-1ce0a9db3e43 | -15.11064 | -46.46463 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a76ca4dd-04f0-3fab-93a5-a0009d8aa3c0 | -10.86296 | -52.05376 | 2025-09-27 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7758b124-f7e3-34d0-a7ad-ffb65e66dedf | -15.42394 | -48.21999 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0cefd3f0-296b-3448-931c-63909f6a56cc | -14.84303 | -45.6077 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d69969c3-740c-344b-add3-058432df7f4a | -11.37823 | -44.96233 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 877c88c6-2ad0-33b5-bd0a-9df5bb3eda29 | -15.57252 | -51.71325 | 2025-09-27 04:46:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7225df0b-fac6-3a6d-a81a-a5133d7bf469 | -11.98349 | -47.89847 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 04dee0df-9dcb-3d83-9526-dec61f22f3d3 | -14.77597 | -60.18358 | 2025-09-27 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aacb3df8-6b18-36d3-98ed-9e8017c3ad6e | -12.05074 | -47.65276 | 2025-09-27 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 834f3454-ef90-31a7-aeb0-07a11d559787 | -13.07022 | -48.71912 | 2025-09-27 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7907845-82f4-35b9-bc94-2eebd84e0652 | -11.68906 | -44.40949 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4514c24-5560-3c3e-a6a8-0f3f81cca9a9 | -15.57308 | -51.70956 | 2025-09-27 04:46:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e8c95ee-e178-3a95-a51d-13f079022f6e | -15.42329 | -48.22496 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54beeb9b-fe81-3515-8826-736fefdf9710 | -10.10902 | -45.34595 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37b14ab0-b00e-3ce9-88b5-11382486e455 | -14.83122 | -45.62667 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de9ca551-7d87-34ad-b859-8ad20ef0ba55 | -12.29398 | -45.65708 | 2025-09-27 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a5fd460-e2d9-3914-b5d4-3e7773aaec57 | -11.44256 | -44.93985 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README53.md)
