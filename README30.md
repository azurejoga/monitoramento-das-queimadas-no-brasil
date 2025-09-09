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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c677c9f2-2309-3ef7-92fc-3da7aea855af | -4.11774 | -47.13365 | 2025-09-09 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e6ee196-7bb3-3522-b77b-ca26bdf2238c | -6.24222 | -45.64915 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbc934d4-5515-3f84-b1b8-573d17e7488d | -5.9653 | -45.79097 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fbb954c-cf3d-3363-a441-fd7cdf58ad49 | -6.37458 | -42.58079 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0390147-852c-3722-9ac4-31c52a01f356 | -6.28384 | -45.60865 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71630459-0dbc-38f8-aaab-43f9460c6f90 | -6.20957 | -45.56998 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d2219b3-83cf-3854-93a0-c85af658cec0 | -6.525 | -42.92522 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c4dac79-ea04-3cad-a6d7-b9c6a9cbcafd | -5.69441 | -45.97882 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 09b579dc-4688-3316-a051-7508d805a015 | -5.81368 | -45.65583 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33722a8c-b992-38cd-ab21-b63310b10bdf | -6.2194 | -45.57548 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 097cd228-4683-3058-b64b-97d755632734 | -6.06209 | -43.1155 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d2c9a048-ee01-37b3-9928-4bde2be71850 | -5.80651 | -44.83451 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5b7b4cea-126f-39e8-80e2-2bf88cafcdd5 | -6.43209 | -44.05143 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11ff97da-0f9b-3378-9424-8db736fd8b0b | -5.86275 | -44.17901 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87b5a84a-b428-3264-b2af-fe3fe47deee0 | -5.78087 | -45.46011 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d7b3eab-e7af-377f-82fa-084f5c33d13f | -6.40392 | -44.43964 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6c15bcb-c533-3759-9768-82aee8f847e2 | -5.93951 | -44.89109 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbab26bd-5532-3d11-99fd-39a1e1b9a073 | -5.79315 | -45.42645 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d3c8ee8-095a-3ed7-98bc-fb7971ab445e | -6.29644 | -43.81582 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bea9c39c-7421-3cd9-942c-d5a39dd89f25 | -5.71112 | -45.4148 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e526737-d7ee-32c2-9638-8eadbbd0e5b4 | -5.68637 | -45.10639 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe6b5896-35da-30bb-9680-f744446ec7e4 | -5.8811 | -43.98009 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3cf4066-e0bc-350f-92da-a1749f7901aa | -5.69978 | -43.89619 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22a2ff06-dbe3-3fb8-bd28-243c36d8dc86 | -6.03653 | -45.01727 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd5c55d4-2c7e-3b5f-bf17-2b2a3dec31fb | -5.91601 | -45.76799 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7678fba1-cd80-3c75-a8e2-d1c15b190cb9 | -6.19464 | -41.0338 | 2025-09-09 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb8dc1cb-6c37-34db-a92c-71d3000227b1 | -5.92347 | -45.76525 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9ca4838-6cd7-3d66-94c9-e70c1e00605d | -5.6548 | -45.43375 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d8371c6-86ca-3647-95e5-95a52f9878cd | -5.93481 | -42.77487 | 2025-09-09 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a696111e-3658-300f-8e5e-71e1102af2c7 | -4.97847 | -43.64371 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d46a758-679f-39b8-9b0a-97ad911624b3 | -6.96125 | -44.7899 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 314a8d08-69fa-333b-9072-b7111abf438c | -5.96587 | -45.78721 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 177eae22-6e43-3796-b49d-539c05b97fa9 | -5.81736 | -43.97007 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1cf312d7-223c-3670-ac17-2f49efaf41dc | -7.29993 | -44.15367 | 2025-09-09 04:32:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3286956-f884-3274-ad2d-b7d7654638b5 | -5.70355 | -43.89677 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7d354b4-967c-302b-ad1f-2afba449c2f5 | -6.4076 | -44.44019 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88f46561-83b2-3937-8a08-65f5153572c7 | -6.2077 | -45.03274 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84250480-b623-3158-a0fa-cb8702447452 | -7.02451 | -44.94395 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60848f8b-4089-343b-b5f9-992c1be930ab | -5.16312 | -42.95084 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 167575b5-7488-3168-b1b0-f6d22f965d0e | -5.42202 | -45.87788 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d185a17-5678-31b5-bb84-98b31e469514 | -5.80161 | -45.66555 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5126f61c-cf9e-3f84-9688-896b590be317 | -5.16465 | -42.94057 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0be7c814-e7ca-3b12-bb45-eee0bd4a5097 | -5.91013 | -52.47071 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5512d472-0490-3343-960c-3b4a25609f2b | -3.69248 | -49.57188 | 2025-09-09 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a66b6f45-9a2d-3b6b-ad32-0dd08e4de8bb | -5.68433 | -45.4501 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd4f2a2-c9ea-3313-b3e9-0ab2e6b084b7 | -6.08354 | -43.34748 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a9fcb64-b74e-3e1e-bda1-a84c66877eb4 | -6.35491 | -43.03107 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aff7fdfd-92b7-31c1-8605-a6e256f27131 | -4.73544 | -44.45338 | 2025-09-09 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 913fa332-26be-3c4b-a45e-8e831e97a7ed | -5.82244 | -44.11797 | 2025-09-09 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e094a92-db50-30bf-a4ac-fc20658e1c65 | -5.94354 | -45.72603 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a349cf5f-ad4d-349f-9251-e23895050343 | -5.45395 | -43.42115 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db041709-383b-3041-8479-9098690936d5 | -5.94184 | -45.66762 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09dcdfe8-74b2-3b55-bc2c-abab92849c13 | -6.41268 | -44.4262 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01f0f596-7f0f-3231-bbd2-6a1d681c34f5 | -5.11423 | -44.67495 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3177ca60-1468-30c5-8f98-6235927a6077 | -6.55104 | -45.9273 | 2025-09-09 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25d3517b-d9a4-3f2e-a696-e79873179fbd | -5.51654 | -46.40527 | 2025-09-09 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5db80f0d-6492-318c-b6b3-6cd6cdb80dd0 | -5.82813 | -43.96875 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58479b0e-15c3-326f-bcd5-4c75c6e72858 | -4.97917 | -43.6391 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09de5bfc-27e2-3349-b447-c2eb0255bfd7 | -5.63812 | -43.63805 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6dfb69b-fc13-3025-9208-a255cbd37f9d | -5.93939 | -42.77182 | 2025-09-09 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 115858e9-d482-340e-a070-186f3bfd5774 | -2.51252 | -51.90749 | 2025-09-09 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48f33191-e016-3636-8faa-2c2196747176 | -6.43958 | -44.05283 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fad79438-c01a-3ee6-8203-b424d36cac85 | -5.67561 | -45.46059 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40f2d885-bd5c-3212-ad64-edcd9ad96bfe | -6.6416 | -44.79868 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0f94aeb-c2f7-36df-9adf-06c26985bdbe | -6.95934 | -44.80265 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c09f3ec-d69f-331d-ae3e-5f6f27890afe | -4.40397 | -48.9468 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4e9af72-4dd4-36b6-9fb3-66414a639e56 | -5.69725 | -45.98303 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 787fe123-3495-306d-8644-ccebf983a0af | -5.42848 | -42.81538 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d61c50d3-9afa-3636-bbe4-52c44afe2eb4 | -5.45468 | -43.41631 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8147efc8-501d-3a03-8fd8-04abdc46eb19 | -5.68645 | -43.90812 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee8f549f-b353-33c0-931d-6540185764b1 | -3.48765 | -40.67251 | 2025-09-09 04:32:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e5e63200-5483-3e8a-a299-57333d8296d3 | -1.95613 | -48.11687 | 2025-09-09 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6cc4349-36ee-3ce4-83ea-4b17dedd1a96 | -6.64586 | -44.79501 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e350b8c3-fc19-3ba3-b150-dffa35102d06 | -6.37565 | -42.57334 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a05501c6-7645-3b44-a4e8-c613eca13809 | -5.5397 | -42.65821 | 2025-09-09 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 79a46ebf-13d2-36dc-b759-852fd48ddaec | -6.21696 | -43.50871 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a151aea-e9b0-37af-be77-7a709ee6f164 | -5.81244 | -44.84393 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b39b48d5-9813-3f83-8ded-b0390e4c119c | -5.26731 | -44.45452 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba115ef4-eb86-3edf-8520-2ab0b67b125d | -7.21169 | -44.74167 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78fdeb34-9759-3f0b-8e63-446491991b70 | -5.71068 | -43.92582 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b061cc97-aa0f-3ca3-980b-64f557489ff5 | -6.8875 | -46.36901 | 2025-09-09 04:32:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1882875-4bb3-342c-b191-a255c34fde36 | -6.06123 | -43.30866 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd0486f7-bea8-3aab-9634-a6733c5a1021 | -3.31933 | -48.71065 | 2025-09-09 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d0afae7-6b46-3c22-857b-a011325f8b34 | -5.67518 | -45.39347 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0fc44e4-d9a9-32fe-b410-a2f35588f632 | -5.87758 | -46.08929 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b73ba01-6838-3b6c-8d02-68990aec7a8d | -6.79707 | -44.78909 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e7e6a29-c7c6-3a81-a83a-1b0b682df4c9 | -5.35571 | -42.63396 | 2025-09-09 04:32:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 56b5d765-8a6f-30d2-9e30-35b926a3cd7e | -6.16987 | -43.38792 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fa0d3fd-dba4-311f-a3ac-89bae53b63fb | -5.93202 | -45.93894 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6040efb-a116-3747-bbfb-c32bf35ec189 | -5.3807 | -45.32718 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fe83f69-6b34-3db6-a242-4d9a4d060512 | -6.86401 | -45.60168 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0e21056-314d-3809-b289-7f899c745589 | -6.20802 | -45.03437 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 720de64e-b278-3d2a-927e-642a2536e2c4 | -5.92404 | -45.76148 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfb6b1ee-3747-3b7f-a9d7-86c1bb320ed9 | -5.94126 | -45.67141 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08151bfc-5f8a-3ff0-920a-21dc83e42bc8 | -5.93938 | -44.41624 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8f6f566-3daf-3d2a-bc54-9298e569ac6c | -5.01549 | -48.46179 | 2025-09-09 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0104479d-7c24-3b40-bcf9-c10e6ecff739 | -4.27539 | -48.19159 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| da81a052-4035-3053-8559-8df6d2674e88 | -5.17603 | -45.17418 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4090a29-1d9d-3085-a395-b93f2b1f2668 | -5.36698 | -44.80247 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aed8c882-9e3f-3f5e-b2b2-547ddf34f2b8 | -5.6885 | -43.89448 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README31.md)
