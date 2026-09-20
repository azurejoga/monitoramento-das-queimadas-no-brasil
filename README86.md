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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4056ebe-9373-3b04-a189-538f68d0fa94 | -8.77702 | -48.72972 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 43b0185a-bd0b-3e71-b65d-ab636a248c73 | -8.24582 | -61.36996 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 393338c1-7d64-3d25-941f-21cab52ddd41 | -3.38924 | -59.5726 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51d74d56-5498-3a82-a765-a139e189878f | -6.37061 | -58.31334 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3400e050-c8eb-3734-90ba-24d1523b4900 | -8.61235 | -54.60149 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d128bf70-e369-3e5d-aebf-8ec989733443 | -9.67606 | -54.31922 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c83b6dda-f315-35ca-b9d3-edec960762d0 | -3.33462 | -59.81431 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57bdcb4d-573f-34f6-a6d2-0bbe807edee5 | -8.14789 | -54.8112 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bda7cf4b-549f-35a0-8e5e-a2479b996c16 | -2.97106 | -54.76802 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d84cf09-e3d5-32bc-a471-301d0c000d07 | -3.36255 | -50.44897 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a99c6fd-ee47-309e-ab62-2b449840019c | -6.13101 | -59.9431 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed56ddb-4703-30a8-9567-8eca868415c0 | -2.90158 | -60.04182 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf969a4a-a420-3aec-9241-849c0e48f8f4 | -8.18642 | -54.75976 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fd0d337-1ae1-310f-8832-bba52b2bcf1b | -8.17201 | -54.76647 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b50c027d-def4-3d31-b713-a4b66a03cff7 | -9.27935 | -48.24808 | 2026-09-20 05:23:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83db48d0-4b07-3cad-b2e7-3e61a14cc6d6 | -3.32091 | -59.44545 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7056daa-144e-3b49-8296-4d69cb6d57f7 | -8.80034 | -60.8004 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1a4d1731-0f9a-3324-b224-376c7c4fbdbe | -10.32028 | -50.21164 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 74e030c4-f867-3edc-9668-17c9f916bed6 | -9.19831 | -60.75568 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0123749-5171-3b4e-a878-819621d75548 | -8.29532 | -50.92258 | 2026-09-20 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d99bd7cd-4390-3cba-b9f6-908d11420838 | -8.18581 | -54.7641 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21c4012a-6145-35e5-b919-1f1bcff9eaaf | -8.15868 | -54.83002 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7678224-1756-310c-9365-26219806d5b8 | -8.46455 | -57.62552 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ba59af0-53a7-36c1-be72-cc4d529c91d3 | -10.41434 | -48.33416 | 2026-09-20 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2060e6cb-1c22-374a-89d0-d403df942397 | -8.54249 | -54.68945 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70d96c56-1258-3a80-a128-dc29805ec2d9 | -10.60928 | -50.2485 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c569da4d-c3ae-378e-b1b0-1eab5ae899ef | -9.20163 | -60.75619 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 639d0fbb-14d0-39d9-9636-18bce99f7c8e | -6.44535 | -59.97773 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcc84328-0037-3043-8fa3-60fc2d3240a8 | -8.85794 | -62.36224 | 2026-09-20 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c6e4cd2-b5e2-3262-8d02-0f2b983c3262 | -3.44745 | -50.60585 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2228a8f-9e57-3dc2-98db-9430bcba13f3 | -2.99373 | -59.36261 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d397b9-dd09-3d60-a8b7-1d963a4c2498 | -3.35599 | -59.8773 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d3f5042-cf6b-3b87-802c-59cd11647747 | -8.76965 | -48.73502 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 642e3567-d284-30cd-84f5-b3b9ba35b5fc | -10.72129 | -50.24964 | 2026-09-20 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f1552f1c-f513-3688-85d2-28e3acea02ec | -8.42453 | -54.72848 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a00e7948-9328-3393-8666-285f5ccee3fc | -3.4085 | -50.40369 | 2026-09-20 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 488705c5-379e-33f3-8ef7-d801bdd97b3c | -4.18087 | -49.40772 | 2026-09-20 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8708059-01e8-3a67-809d-e8429bc85a8c | -6.45423 | -59.98627 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b20aa298-d11c-3eaf-beac-cdb9bd8f5035 | -3.29198 | -59.43336 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e21119d1-c2af-3998-8fbf-6ec7a858c13e | -10.96165 | -49.742 | 2026-09-20 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 647679bd-9e92-34ac-a73f-dff17dd5586e | -2.21374 | -60.17657 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 731adc07-7942-3dd1-bf88-9924c49f719c | -8.77083 | -48.67122 | 2026-09-20 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ccc88758-2eb0-3308-9d4e-3e6ce40f3c3a | 1.10888 | -59.6422 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baf143cf-e4c2-3e4b-ac9a-aa0dede4fec4 | -3.16507 | -48.61516 | 2026-09-20 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2081b4a0-d678-3c79-87df-a16f2e94f45a | -3.01275 | -54.17124 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f4d5136-da15-3668-99e3-fc3956b97062 | -8.24197 | -61.37291 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee938d9a-d8fe-3f08-8f14-9861f26c2d80 | -6.45199 | -59.97877 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 15928b2a-916c-35c2-a929-209f941864ec | -3.36312 | -59.87489 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c1379c2-246c-337d-bfb7-71e411e7a53d | -2.24219 | -58.10902 | 2026-09-20 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3118b73-4ee2-3d74-8e55-0f0bb82ce5cd | -2.17343 | -48.32464 | 2026-09-20 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5450467-3494-398e-b3f9-864ff33a0663 | -3.361 | -50.45985 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79858997-fa73-38a4-9ffb-1f97e0de4239 | -8.07802 | -55.34452 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a38c16d0-edfa-3c22-a574-e2a930852ded | -10.30994 | -50.24427 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0913536d-3975-3527-8529-4dd3891d1c0d | -10.78517 | -50.87312 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5bfd5a21-35d1-3dd6-802a-56443ed63dad | -6.35438 | -58.30294 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b99d0bdc-2024-3d31-9656-3faf9ac14bca | -10.72094 | -50.24952 | 2026-09-20 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ee56bee4-9777-3b88-ad74-a3fac374b82a | -10.84402 | -50.93438 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93fa1cdd-2108-364f-aa5e-2237872acfe5 | -3.34631 | -59.84775 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 419c9c63-4175-3c54-bef8-d0eea527ae60 | -2.21704 | -60.17708 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f78593e-3847-3d53-90bf-37a75138260f | -8.23666 | -50.64975 | 2026-09-20 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ded0872-75e6-38f8-be38-2a8b05fcd3e7 | -3.45739 | -59.52999 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16ae19ff-5eaf-3364-b33a-38336dd94b12 | -3.14594 | -57.88981 | 2026-09-20 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fd70a3cd-8c58-31f9-ae7e-d65bdce9c09a | -3.17194 | -48.61142 | 2026-09-20 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 088a1a38-ce14-371b-ad64-925009b64dc9 | -2.64845 | -59.3718 | 2026-09-20 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb56862-5087-345f-a80a-c8e4926f5bd4 | -6.64569 | -62.88015 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecd0d22d-fd14-3510-96d8-0c00f65f5591 | -3.4535 | -58.19415 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 74ecca63-3b69-3af8-ad18-36c32fdf70e1 | -7.48793 | -55.60948 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07205a75-21e0-3827-9557-4194486ae8ca | -2.82839 | -46.71234 | 2026-09-20 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06abd1b3-b089-3829-9a82-cc8e0833a620 | -9.18334 | -60.76408 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d8d50bc-e952-3ed0-bff2-015292b9f681 | -6.87929 | -59.63024 | 2026-09-20 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1648598-a8ca-36e8-9268-76cf59e699ca | -6.3712 | -58.30947 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44d04914-7604-3b67-8098-7c3620016a68 | -3.14823 | -61.396 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04969c20-c0ad-37dc-ba95-1500691a2cff | -3.33899 | -59.80795 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2573066-9863-3182-91c8-aa68f165290a | -10.31023 | -50.24422 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 70c31a79-7250-3c23-8fa2-cf0f209b11af | -7.05157 | -62.95527 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a930995d-a1d0-3fe3-86d6-d07967a82453 | -1.74148 | -54.93697 | 2026-09-20 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51374696-4339-350f-8106-a4545d9ef499 | -9.68646 | -54.33865 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f6e7daa-b694-3980-bab8-6c25c65ff6cb | -10.32084 | -50.20687 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4934bc33-c14b-36f6-b8b5-df1e0ea17c90 | 1.22791 | -50.98802 | 2026-09-20 05:23:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c127164-9da5-349b-80ac-a0c2f6a9b45b | -6.35379 | -58.30681 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1531b157-11f0-3a28-b75e-3304ee0b59ac | -10.27869 | -50.24492 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 057846b9-6b2f-33fe-86fe-4fb882226bb7 | -1.63685 | -55.14832 | 2026-09-20 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1df1d890-d50b-3b04-9254-a277794ccf7a | -8.20225 | -62.85268 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2054248-349b-36da-b1e6-20fcbd5e08be | -8.79426 | -60.79587 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0ad8491b-4444-3c1e-bcf3-c2c320e7bd46 | -3.72993 | -54.64729 | 2026-09-20 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 216230d3-23b6-3a9c-8c56-074a20bb5f1a | -9.06343 | -61.42604 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 288b944e-7e63-3d35-981c-11d5c555d8dc | -3.90283 | -49.06749 | 2026-09-20 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7fc59be6-1d4d-375b-967d-c90fe31fb98f | -3.35099 | -59.86599 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d636037b-2962-309a-ae30-4b291bf62e50 | -6.45159 | -57.87387 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52174ef4-a4c5-332e-9c4a-544be5dc083a | -8.17822 | -54.7542 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f483ff07-274f-3da7-a632-6b0e48a24494 | -3.45395 | -50.59933 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 037df44e-eb7f-37e2-9603-1f23af718cd4 | -7.59405 | -55.71144 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52914d8e-c47e-3645-a351-eb3b2d2b9d74 | -8.15228 | -54.8118 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8abcac36-8bed-3611-8735-94c56faff515 | -7.59309 | -55.68878 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79cfad44-1db3-3aa7-a6e4-3603c1d6c4f5 | -8.80088 | -60.79691 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6529b16-2cf6-3ab1-a964-6195ab007df6 | -9.65684 | -54.32159 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef20fb9f-d2d6-3911-aa46-ecd2c131322f | -3.55459 | -50.29299 | 2026-09-20 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 231c2eca-aa18-346e-b317-b28a98c8d437 | -8.18064 | -54.73682 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 088f63a1-3c3b-3621-a0ca-ed519d965616 | -3.36036 | -59.87095 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 253fc493-2524-3271-95f7-8ae8096c33f2 | -3.30967 | -59.51797 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README87.md)
