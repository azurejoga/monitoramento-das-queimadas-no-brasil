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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57c9e2bc-ed70-3e4a-b955-fc42e033a295 | -6.17228 | -43.70579 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bdd3884-16d7-34d9-9c69-8d18d71106b2 | -6.1612 | -43.70807 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95f7529a-3de9-3a80-8a1e-bd1af92ad045 | -5.97005 | -43.89927 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15dee68a-b08f-3005-bc71-5bf3afc83278 | -5.9666 | -43.89874 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 557257ac-740e-325e-a5b6-311135c574eb | -5.96256 | -43.90203 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7f1bff3-1ca3-3955-937e-4604e101ba74 | -5.95692 | -43.69452 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9d02f29-56d5-3b2c-b948-9eded65cc487 | -5.80137 | -43.92951 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4e853a4-2b07-3838-bbf4-6d2e826558e5 | -5.69059 | -43.64352 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eeaebaa-42d3-3114-9cb4-55836258cf40 | -5.6877 | -43.63911 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b31e9e-9b46-30cb-978f-22d292840b5c | -5.66371 | -43.91286 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fbcd8fe-525f-3f6e-8193-f82e7e6fa800 | -5.30708 | -43.61563 | 2024-10-11 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db24f096-6274-32aa-a120-b3e6a2903fad | -6.17108 | -43.71358 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2995e0a9-0d85-34c8-81c0-ea418149e796 | -5.69815 | -43.64073 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1953cca9-c662-32ce-9fda-a81435bca574 | -5.37949 | -43.64176 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3c54371-a478-3fee-ace8-6ce8b1c76b67 | -5.25205 | -43.55615 | 2024-10-11 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19c4f400-da60-34a4-aa58-2b26cad8fdcf | -6.17168 | -43.70968 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26838733-6570-30cd-aa82-cb055b180500 | -6.16529 | -43.70473 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb77dd19-d384-364e-aeec-a1ce8adda7ca | -5.69526 | -43.63631 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81ce38f3-3919-3e4b-a7c8-72c2c01f7ca3 | -5.69118 | -43.63965 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b4e995-fc8d-3048-a86a-270f70eab37e | -5.96708 | -44.12641 | 2024-10-11 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca3c6b94-9325-3e6b-a0ba-eca1a58051b2 | -5.90905 | -44.07262 | 2024-10-11 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c64934f-a638-3e96-bf20-074a0577e23d | -5.81354 | -44.12304 | 2024-10-11 04:23:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd2bb03-bcf3-3a16-a3af-9f8a666f6bc8 | -5.81012 | -44.12249 | 2024-10-11 04:23:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87faffcb-243a-38a3-96c6-b072efa9a5c3 | -5.7455 | -44.33601 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b961769-aa46-3dbd-92bb-1e17eea7a3c8 | -5.74211 | -44.33548 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbea45e2-c2d4-3544-8027-210d5132a56e | -5.73927 | -44.33132 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b11ab72b-de55-35d9-8d5e-65e7d7cf3ec1 | -5.73871 | -44.33495 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ace33f1-d77d-3156-a32a-51b104285aab | -5.63611 | -44.07004 | 2024-10-11 04:23:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9250982a-0e74-3252-aa81-f128f88b8f5e | -5.63268 | -44.06953 | 2024-10-11 04:23:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9aaece2-f387-354d-8f40-4ae706f12c4f | -5.62182 | -44.07172 | 2024-10-11 04:23:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b066e3c1-c382-3fa2-8ce3-3f8dfe800b6a | -5.42724 | -44.42905 | 2024-10-11 04:23:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8cb7332-3d2b-34af-b009-4a7427e78cd2 | -5.34215 | -44.45696 | 2024-10-11 04:23:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 095b22cb-7e8e-35e9-a99d-a6897847f51b | -5.3416 | -44.46057 | 2024-10-11 04:23:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f53a447b-f0cf-34a0-8a11-c3f1d8c11efe | -5.33974 | -44.1511 | 2024-10-11 04:23:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 002182e3-127c-3ffa-8576-92e5767f8e44 | -6.41244 | -44.69366 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eae10cd7-ea94-3953-b477-af61a2081d73 | -6.41189 | -44.69728 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 96f49b79-ae1e-356d-8c5e-bb4c0e177ca4 | -6.28895 | -44.7674 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 841c7326-2d98-3eda-931a-a1d2015328bf | -6.25876 | -44.8068 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e91f091-a998-3b6d-81e8-3967f3acb661 | -6.25595 | -44.8027 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e42e999-9c51-3fb4-95d8-6c6d49c1b186 | -6.2554 | -44.80628 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc108e40-23d2-3285-9450-2a99edc71523 | -6.25203 | -44.80575 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 901c49f4-1ce5-3ed4-b606-3715e69905ea | -6.25149 | -44.80933 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76e36f52-2a2d-33ae-851d-94f894e9ebd6 | -6.24812 | -44.8088 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6ac528f-3a15-3b6b-8c9d-88edce129a6b | -6.07151 | -44.6342 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da5aa77a-ac66-3599-9349-ac81e2a09682 | -6.07096 | -44.6378 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7417a021-e576-3d4d-9faa-f0b55fcb3787 | -6.07041 | -44.6414 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2f03d40c-83c5-3d0b-b0d1-043bf59ae8bd | -6.06986 | -44.64499 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7a340cf6-f815-3946-8ab8-b2a7bcd954e1 | -6.06703 | -44.64088 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c722a364-591e-37fa-ba09-67ac0352ec9e | -6.06648 | -44.64447 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9b7b3deb-a824-38f0-ab9a-3a4bab5c5204 | -6.0631 | -44.64396 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6a97120-bdd0-337a-bd60-f224eefab9e7 | -5.20075 | -44.75792 | 2024-10-11 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06df8f4f-710d-3dd1-b021-c38d953780cf | -5.19741 | -44.7574 | 2024-10-11 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f286055-e644-3eba-a17e-ccdeb20cc200 | -6.51408 | -44.00677 | 2024-10-11 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6a51cdc6-529f-3573-b11a-d90edfa6ea27 | -6.45397 | -44.37769 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fedd9b5-08b5-3e20-8a29-c15477a52282 | -6.44999 | -44.38088 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20e72189-22c1-3eb7-8da4-ba43bd6f8b72 | -6.44695 | -44.26305 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fb481e7-2b05-33aa-a166-d0748b62246e | -6.44639 | -44.26678 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25965d48-1cfc-3e26-82f7-70b4289dba07 | -6.44582 | -44.27049 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 192d9641-6404-3afb-913b-0b850d88e705 | -6.44527 | -44.27414 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b775bf6b-119b-3ffb-b0fb-8d53165bd22e | -6.44472 | -44.27777 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83b0256c-df31-38e4-bc65-e33b94269863 | -6.44353 | -44.26253 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8cf7097-9f42-310f-b5b3-893259abab65 | -6.44297 | -44.26623 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 391da47a-8c9e-3285-b268-8250769394ec | -6.44241 | -44.26991 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 960778d9-06f5-3e95-b5ba-a82fb43adb93 | -6.44073 | -44.28094 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2935cf40-4cca-3b85-adcc-8a28005f2917 | -6.435 | -44.27253 | 2024-10-11 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca576c02-8c6e-356c-9142-e956cc717c4e | -6.39604 | -44.36578 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aae37b39-9d17-34a1-b1ae-dfc82a30711c | -6.26658 | -44.18336 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4468bb6f-e3b4-3531-9ee5-f9c58c0662ea | -6.26258 | -44.1866 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7218c246-c7ad-3fd7-b045-65d653ce8082 | -6.23346 | -44.19353 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ceb6ee4-a9ea-3c53-ab67-a6d5431885d4 | -6.2014 | -44.38161 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa185e8d-d0cd-3b36-85e3-e23cdd58da12 | -6.19855 | -44.37739 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8952571c-1a97-397e-b53c-71c9b960d208 | -6.19799 | -44.38111 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b83743af-2ec2-370a-a12e-5426cccbe6a7 | -6.19751 | -44.1997 | 2024-10-11 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9c25764-b654-3b68-9f55-670843cc638f | -6.19742 | -44.38484 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f4fb5ab-b13c-3089-9be7-19735ca2ab40 | -6.19515 | -44.37688 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da5f55bb-25c7-3054-be51-2f2dba1510fc | -6.19458 | -44.3806 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ce18ae8-217c-3707-b0c6-537013a8afd7 | -6.19455 | -44.37683 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3214ee7-c782-3d04-aba8-988446290f0f | -6.19409 | -44.19916 | 2024-10-11 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 609a2a2e-7a3a-3fef-86a9-56943e97a56d | -6.19402 | -44.38433 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 619a31e4-989e-3d96-a76c-fd90f11e239e | -6.19397 | -44.38055 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cce12284-9c5f-300b-a464-e81048191121 | -6.19339 | -44.38428 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 209463c5-7e13-339e-b55f-68edbe4e1959 | -6.18998 | -44.38376 | 2024-10-11 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4af9929b-6d54-3e13-8d67-66c553dd2958 | -6.85226 | -44.8604 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcbf9f1e-89fd-3863-8c13-f3361b4addf6 | -6.94095 | -44.05397 | 2024-10-11 04:23:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b23dda6b-5ed6-3f7a-9c15-e2bffc0c70d6 | -6.95509 | -44.28482 | 2024-10-11 04:23:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b817c45b-bdf4-3231-bf5f-09c5805fecd6 | -6.95451 | -44.28858 | 2024-10-11 04:23:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3eb4ada-c368-3208-9623-d5b46f282f18 | -6.95165 | -44.28429 | 2024-10-11 04:23:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddd23d0e-3581-3ab1-a55d-413b9718119f | -6.81487 | -44.46637 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed5c58f0-408f-3356-8785-bca211c2767a | -6.57922 | -44.17539 | 2024-10-11 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 219034fa-e17a-33a2-a912-2b22e3b4cc3c | -6.57865 | -44.17916 | 2024-10-11 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d6aa0a7-d227-3d48-92e9-2fc7222fc381 | -6.57578 | -44.17489 | 2024-10-11 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 952b49c8-ad22-3c13-9fa1-5a4017ac2b10 | -7.66563 | -45.21979 | 2024-10-11 04:23:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a35d4ffa-f5c8-3e6e-b20d-0e810ff4c20b | -7.58469 | -44.76934 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8cc42391-ab13-308a-a72b-652cf7677eb4 | -7.58413 | -44.77303 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2eb063a-152d-3cc8-9ed3-2b809c4430da | -7.5813 | -44.76881 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0f1b8735-d427-30bf-b1b2-aecc1edcbeff | -7.58073 | -44.7725 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 52de6ca8-087b-32d8-8116-16c1c29621f5 | -7.57733 | -44.772 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f6b782d-b0ca-3e87-95f7-47bc96fba13b | -7.57676 | -44.77573 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c4e7bb6-2428-3a55-b8a9-78eb63024080 | -7.5762 | -44.77946 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44897fac-6b14-33bd-96fb-eb02ebdb135f | -7.57507 | -44.78687 | 2024-10-11 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README55.md)
