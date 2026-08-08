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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7c5ec02-7327-34ef-974d-5201ee582356 | -13.42062 | -57.02481 | 2026-08-08 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb58dad1-aa33-39f3-9cb8-c5446aec2e3a | -20.17805 | -43.69057 | 2026-08-08 04:46:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3c9b30ef-32a1-30f4-928e-4547bfb0439f | -15.70929 | -42.1819 | 2026-08-08 04:46:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 497f29fa-0204-37b1-bf3d-c27c52a0c6a0 | -20.38876 | -49.31202 | 2026-08-08 04:46:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b07b0922-fad6-32b0-be7c-b14790a791fb | -10.5269 | -46.61678 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b30cd7e2-da99-309b-b595-4f0d63c72258 | -14.93026 | -48.2629 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 13aa2e3d-f457-3d6e-86bf-48242e36325a | -11.73005 | -50.1371 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de49c920-39a2-3bf4-b0bb-0e418adacd64 | -19.91308 | -45.43704 | 2026-08-08 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcf50311-de98-3465-aa8f-6751fa87b748 | -14.36815 | -54.91518 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ec55e9e-a2cf-3b90-8778-69b70d5e73ef | -11.01929 | -50.53507 | 2026-08-08 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2565e20-25d5-3df4-9007-1de2a5b7d96d | -14.2792 | -45.28312 | 2026-08-08 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dd245df-9312-36ea-a2c8-cc3948d74598 | -13.836 | -53.68872 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cbcae81-394e-3ac9-991c-0dac29a616a0 | -20.38939 | -49.30752 | 2026-08-08 04:46:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 02434ab0-2214-3e3d-a4c4-78e0d9949dc7 | -14.32642 | -54.93902 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce342406-0eb3-31a3-8ad0-836465ddb867 | -15.69684 | -54.85181 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9aa38577-0ea0-3857-a412-d5ef1f3cbaf8 | -8.67853 | -62.8713 | 2026-08-08 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6808683a-54e1-3975-9259-2bcc81e888e9 | -14.33259 | -54.99007 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5d8f1e9-7249-3a41-9f39-f16dc53747e3 | -20.36089 | -53.86322 | 2026-08-08 04:46:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf96d27-3db0-30c8-9a87-371cdc49dc3b | -7.54985 | -61.16133 | 2026-08-08 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29bb39b9-c111-30f3-b5dc-6532f5378293 | -8.16566 | -55.4191 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc710b41-f197-30b9-9e31-fd48db0861f0 | -11.03425 | -44.28065 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f447b74-1e20-39b5-b301-88ce23affb66 | -8.16092 | -55.42206 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50ee506a-5ec2-34a2-9da9-b00d744ea71b | -14.36927 | -54.97417 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dae48ac1-2bde-3438-9142-a82fa3bd21aa | -15.16413 | -52.74655 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 868bd946-1df6-3d05-96b2-bda0372c3a5c | -10.25816 | -45.80511 | 2026-08-08 04:46:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d70fbb82-f634-3637-a95a-5ab91646c91e | -13.389 | -41.34912 | 2026-08-08 04:46:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71d7ac1a-2bbb-3704-a327-8367a949468e | -11.3069 | -44.85501 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ec0a1b-d075-3909-a872-9749db918dbf | -12.33677 | -53.15881 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfcf0c1a-9ae1-34f4-b317-4eb9395ce1e5 | -14.92515 | -48.25201 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06db5b3c-4517-3f98-83da-abe346d0a05f | -14.36197 | -54.97282 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67cb00d4-01d1-382e-9780-95c0f472f365 | -7.55083 | -61.16016 | 2026-08-08 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62260333-aa73-3c48-8140-593ac13fc3a0 | -11.83959 | -56.94058 | 2026-08-08 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4e89307-67b1-34cc-a4bf-bb344c2be317 | -13.42542 | -57.04592 | 2026-08-08 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 957e9228-0e49-3d06-bea0-29bcb8e5c873 | -12.53364 | -46.91866 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2377d200-00a2-36ea-a9c4-4466f02c4e8a | -15.83816 | -48.22684 | 2026-08-08 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92c663d0-f5bb-3041-a691-ef48a0801b33 | -14.32163 | -54.98798 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de0561d3-edbd-3aea-a33f-ead12568880d | -15.3796 | -53.79838 | 2026-08-08 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0a4ca07-2e0a-36fb-99e2-f24b6e3527f2 | -14.93367 | -48.24414 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a6cffe5-ed26-3f1a-aecc-1923531b9b11 | -11.03926 | -44.27692 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c13f3419-3edb-3816-a7fc-1623163ff438 | -13.3719 | -41.35088 | 2026-08-08 04:46:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 04ac5bb6-40e4-3b1e-8303-cf58dd2c1fec | -12.87451 | -52.81728 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c21c1243-d781-3610-845c-d79d268c5aa4 | -17.3023 | -42.65743 | 2026-08-08 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 15b9e897-0ecf-3236-8209-8ed1bf295202 | -14.93788 | -48.26688 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b41f25a7-8de8-3ad6-8513-c58f6ee15975 | -14.30911 | -54.99482 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5327c4e-cf9e-3b08-a0c7-b33479beadfe | -19.93308 | -45.78678 | 2026-08-08 04:46:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f468c3e-84db-35fa-b5e4-9edbefebd9b5 | -19.9096 | -45.435 | 2026-08-08 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c14687d-4ac2-3dff-9500-c14b91190857 | -17.30193 | -42.66077 | 2026-08-08 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ac4f775b-0b30-3a9a-bdf8-598da1d82dde | -12.87791 | -52.81786 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5415c2f-e244-3722-a11b-81dbcfaea9c4 | -11.72783 | -50.12947 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da43f85a-d92e-3d90-925e-fd4991bb61b1 | -15.15864 | -52.73807 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ff6452d-e3a0-3ed1-97fe-f98632368aaa | -14.36562 | -54.9735 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 630fbe98-8674-3159-8203-ecfdaaaed0d8 | -17.31071 | -42.67946 | 2026-08-08 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcbdaad8-0a15-36aa-a42e-40cd3da6c6d9 | -10.86516 | -50.34901 | 2026-08-08 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a237f030-4a9a-32c3-8ff8-56c9b24fa7d1 | -11.26882 | -55.86529 | 2026-08-08 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ad84b742-d9ac-3375-9591-61a089fae0bb | -14.32719 | -54.93464 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3e3106f-c050-3375-825f-47246d39eebe | -14.30546 | -54.99416 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aeb8656-0302-3c79-947b-4cc68068d2d6 | -14.3172 | -54.99174 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c32fb871-9415-306e-994a-77d96858813f | -20.35756 | -53.86259 | 2026-08-08 04:46:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7c7c79e-2fc8-3a37-a8de-b093887c3e5d | -14.92786 | -48.25395 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4df234d8-4d70-3377-a571-429277146e11 | -8.14381 | -55.42302 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa17157e-34b2-37ac-a902-356a69267be6 | -20.17318 | -43.68679 | 2026-08-08 04:46:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de819e79-f492-3e1d-a33a-a1cc4d2b0c58 | -14.89897 | -47.74456 | 2026-08-08 04:46:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ece1890-7e07-3709-b5e4-bef565c573d8 | -14.93001 | -48.24378 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 49c8479d-bb58-3205-a653-47a4f4eaddb1 | -15.39611 | -53.80528 | 2026-08-08 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27ac9e1c-d493-38cf-8982-ea43599f4180 | -15.10288 | -52.72846 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcd2bf10-5829-3716-94f0-0fda46a8fdfa | -16.18145 | -46.22492 | 2026-08-08 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58e8362d-883c-3c9c-b4b9-f628f4ff2c14 | -13.8375 | -53.70112 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d572b31a-63b7-3dd4-81e3-db9824c332e1 | -14.27434 | -45.28677 | 2026-08-08 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c58d3714-ed91-3745-a53f-46e1d5c4edb8 | -12.32579 | -53.16087 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 468a6ccd-e1ce-31e9-b93f-f92a13b6e28d | -10.28912 | -49.95123 | 2026-08-08 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bf2e848-cedb-39e0-bfa4-651f2366732c | -14.32894 | -54.98937 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41bcaf49-b353-362d-afec-49b0baea7575 | -20.32475 | -43.65962 | 2026-08-08 04:46:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f21f347d-2018-3b14-b3aa-5bef261eb0f1 | -11.15406 | -54.84682 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6df580cc-5d3e-3e24-b93b-031b6ae64047 | -14.92939 | -48.24823 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ac8245d-8e9f-30c9-b517-99f3af3a2aa1 | -8.78038 | -64.21813 | 2026-08-08 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 681ef315-8544-337d-8b06-cc04f680f0ea | -15.1547 | -52.74115 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf5b3d03-bfe9-310f-ac55-de19ef56fe6e | -14.22659 | -48.50531 | 2026-08-08 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8efd8fe7-8bba-342c-a30a-65f81902878d | -11.15142 | -45.93934 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b09c162-3b90-3ab5-bf79-6794ac0b0576 | -13.3886 | -41.35251 | 2026-08-08 04:46:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 08c8daf6-4fda-3b46-b056-b49eded25419 | -16.18301 | -46.22437 | 2026-08-08 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db999dfb-c6be-374c-a676-5453e50cb9b9 | -10.50625 | -46.62687 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24883e5a-1367-3d61-9b37-3bbc4942024d | -14.41383 | -45.66604 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18f9622c-e63b-32fd-a44e-b174b1e181ef | -15.71091 | -42.18619 | 2026-08-08 04:46:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51b56527-7dbf-3e47-9904-0c7a256332ae | -20.32508 | -43.6613 | 2026-08-08 04:46:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b02e045c-65fe-370c-bf53-e99b2efbad6c | -20.1728 | -43.6904 | 2026-08-08 04:46:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 376fda9d-5b27-3b69-9371-4582bbf12537 | -15.6727 | -48.26445 | 2026-08-08 04:46:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aa9def5-d835-3f48-adb2-f1c9d1dd0295 | -12.6098 | -52.46246 | 2026-08-08 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65c9e2b6-f3f4-3256-bd51-175359c6a9dc | -12.52768 | -46.96121 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db34094d-15ff-3c54-a321-d2cadcf7f31e | -8.29857 | -55.10987 | 2026-08-08 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 707f2c99-2277-314d-be52-2c0aef491659 | -8.68513 | -62.87261 | 2026-08-08 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d185f6b-f0c5-3dc1-85b9-6d1d9ebd41a2 | -15.11133 | -52.71873 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9854e5db-266c-3df0-9610-773b4b91e5dd | -15.10622 | -52.72902 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19ee305f-a01f-3c59-b950-72bfa0d91ece | -10.2685 | -45.81699 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e107fe71-796e-31d3-84de-822e1da6c7ae | -10.28967 | -49.94772 | 2026-08-08 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2aa1b531-c358-3761-ac04-7601d0a17d47 | -14.3197 | -54.95591 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bc04b1f-9ffe-32e7-93ba-2dbf323a53c3 | -11.7234 | -50.13603 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaa835ff-a79c-3dbd-8643-49289cc7698b | -15.39546 | -53.80915 | 2026-08-08 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2231694d-ac30-3c60-8fdd-12fb418d5283 | -12.32988 | -53.15763 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c0c875d-a6c4-345b-8deb-56e2daf84542 | -12.33052 | -53.15379 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f675a1c1-abe4-31e0-ad5e-29ea58c3f9fd | -14.41857 | -45.66615 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README18.md)
