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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aff6e534-534d-3e81-a2ed-418b2db98625 | 1.49722 | -59.93232 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b841e5c-8945-3b92-9f9b-0705430d1b3c | 0.86058 | -60.4062 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c59ed5fe-1abe-3cb8-93a2-d7ba99090160 | 1.51108 | -59.93611 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07bf7d5e-d5db-376e-adee-f961130d9e30 | 0.19589 | -60.45186 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 959ce60b-4b21-32e9-bc2b-fe8da6a662da | 0.85835 | -60.40403 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87f2c2e8-4e47-362e-a7ef-fa61e5f24174 | 0.47336 | -60.40093 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dc97fc5-e95a-3122-b220-6beb5b1eaba2 | 1.08367 | -59.24779 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e67dd393-4548-3b9b-844c-b936ceecb64f | 0.89068 | -59.79087 | 2026-03-01 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1ed4501f-de69-3b5a-ace1-d43548468c43 | 1.07825 | -59.25355 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f45b0f47-0ccb-33c7-9846-61377e75d25b | 1.47058 | -59.93154 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7807902a-fb70-3e8e-85fe-b098d0d4a466 | -18.80494 | -57.63546 | 2026-03-01 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| db0cfbd9-b6a4-33be-ab8c-b7064b1fc0c5 | -18.80426 | -57.63908 | 2026-03-01 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 22a67183-3197-329d-8ff6-b5c215f23905 | -18.83961 | -53.42711 | 2026-03-01 04:44:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 202faa6f-5f25-37f9-9fae-193f7165d367 | -19.91733 | -50.83368 | 2026-03-01 04:44:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1b3ce4d8-d884-3949-afff-71cdde3e5f43 | -21.41224 | -48.73689 | 2026-03-01 04:44:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a734ba8-ad6b-3651-8ee0-d83964444c5d | -18.97839 | -52.92823 | 2026-03-01 04:44:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d6dd769-bb2a-3641-a2f2-56da4fe04125 | -18.80811 | -51.60862 | 2026-03-01 04:44:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c193972d-30a4-378e-9d82-0219cff9b10a | -18.80891 | -57.63628 | 2026-03-01 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5c5df563-f113-341e-9318-27175b4ad5e2 | -18.80824 | -57.6399 | 2026-03-01 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 15d998f0-04f2-3560-8c8e-ce851ea7065b | -21.4129 | -48.73188 | 2026-03-01 04:44:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4677b054-ca11-36f4-8369-73a1a538b3df | -18.80958 | -57.63266 | 2026-03-01 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6fe4dc58-af61-3584-98d8-239562891fb8 | -18.80755 | -51.6123 | 2026-03-01 04:44:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 001644dc-5e89-397d-80d7-fcac84ff2188 | -21.68531 | -56.31166 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62ba209d-0508-3c97-97e2-6a26c85ccfd2 | -23.46273 | -52.80771 | 2026-03-01 04:46:00 | NOAA-20 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fa09e7de-c97b-3e04-8d69-225e1e0b50f3 | -21.6975 | -56.30512 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e812a19f-560c-3271-9e6a-8d7869b2503a | -21.70663 | -56.31607 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e9969b0-12e9-3e91-9325-62a239714c56 | -23.28091 | -55.33614 | 2026-03-01 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3db360ef-7924-3d85-bcbd-8dc341579c1e | -23.27282 | -55.34266 | 2026-03-01 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2e77516-9c38-32ec-8aa5-1783c7ab831b | -25.3859 | -54.4286 | 2026-03-01 04:46:00 | NOAA-20 | SANTA TEREZINHA DE ITAIPU | PARANÁ | Brasil | 4124053 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60c73475-74cf-340a-b3db-c7c8f1c8b741 | -21.70943 | -56.32116 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7ad1453-914c-3bcc-b7ee-d5cee1a1bef2 | -21.68963 | -56.30803 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e04be356-bf40-31d8-9ada-348261920bb6 | -21.71196 | -56.32023 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b25d129-88e3-3d01-b182-9072e6f3d5fb | -21.6904 | -56.30368 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a128dcbb-3d49-328c-be3f-1afd5820d5c3 | -21.68608 | -56.30732 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db4ef7e3-53d3-3d7c-a9ca-5153a1f303db | -28.41659 | -49.20777 | 2026-03-01 04:46:00 | NOAA-20 | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6a7a744-6d17-320d-9471-0c20237cf643 | -23.28157 | -55.3322 | 2026-03-01 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1320cd1b-dcb8-3b26-b4ed-427c7a8809b0 | -21.69319 | -56.30875 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86150e77-0137-300f-b285-06c3dd7a5239 | -21.68658 | -56.32546 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9ff9f7a-7f48-3ec4-bcca-01e8f874eabf | -21.71298 | -56.32187 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22ef9678-e6d8-30bf-86c0-77f9f5a8e622 | -21.68811 | -56.31673 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47f1cbdc-eb40-3cbb-ba8f-fbaa78c002eb | -21.69953 | -56.3146 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1eb43a04-531c-35d7-9562-10933891b5ed | -23.27892 | -55.34797 | 2026-03-01 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fd4a41e3-4ca9-38d1-a0da-2e06dad03ec7 | -21.70308 | -56.31535 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79857ce1-af45-39a6-b12f-f23ce14b5437 | -21.70587 | -56.32046 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85b01f50-ef70-3373-b095-f9fe39e6044b | -21.71019 | -56.31678 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 644e7577-9137-336f-9737-523d38190a0d | -21.68734 | -56.32109 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a62f36f4-6b2b-3170-8c83-e9ada27ed88f | -21.71351 | -56.31157 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6999f37a-75aa-3a36-a122-cc6478a7c4d5 | -23.46607 | -52.80831 | 2026-03-01 04:46:00 | NOAA-20 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 27a00bfd-3d1d-3917-8fae-850e3eef18c4 | -21.7074 | -56.3117 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 451a3923-e4fe-38c4-b670-22e8e815a01f | -24.06641 | -49.78198 | 2026-03-01 04:46:00 | NOAA-20 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85acb175-19f5-3096-b778-c91723cd864f | -21.70918 | -56.31516 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7d6f68c-c144-37ae-9130-ec3024b67d58 | -21.7084 | -56.31953 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a37007a7-8c2a-3edc-970d-9762ca9d5317 | -23.28495 | -55.33289 | 2026-03-01 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eca07538-0718-391f-8656-db0dfd08a942 | -21.68887 | -56.31237 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e456e4b-45a2-321b-a276-74d60e6ee8b4 | -28.41703 | -49.20388 | 2026-03-01 04:46:00 | NOAA-20 | PEDRAS GRANDES | SANTA CATARINA | Brasil | 4212403 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0f803fa-bb44-36b7-bdc1-f74d01534f40 | -23.27216 | -55.3466 | 2026-03-01 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 51f44b4c-6028-3a5a-bef2-13af53c039da | -21.70996 | -56.31082 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9597c6a3-f639-31ba-9124-36f9b100883f | -21.71449 | -56.3132 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edbe8895-4347-3276-bf11-243ee7ab972b | -21.71374 | -56.31752 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe339018-5d1d-3ac7-bdea-c2b6d0c0d988 | -21.71628 | -56.31668 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ee501a4-1d08-3476-988a-87bd04c74008 | -21.71095 | -56.31243 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e039e78f-77af-38ee-a143-5d92fbd9981c | -21.69395 | -56.30439 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c114e39f-6cd4-3876-8bed-7df8a3ad8bd7 | -21.70384 | -56.31097 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23b8fe4e-67d0-32b9-9593-32170d76c46b | -21.71116 | -56.32463 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba8c113b-76ef-31cb-9fea-ee69d98a6d8a | -21.71274 | -56.31589 | 2026-03-01 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8e7c911-3653-369d-a403-37eef2ef6586 | -23.27958 | -55.34403 | 2026-03-01 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f0ed9a9e-2a94-30b6-a28b-173dc6296f9a | -23.51682 | -51.4295 | 2026-03-01 04:46:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 37d033ef-53c9-3ce8-898c-ff85fb663084 | -30.36259 | -54.33925 | 2026-03-01 04:48:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 3e7046e8-3be6-379a-af57-33fbd4812cac | -31.45989 | -53.66691 | 2026-03-01 04:48:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| d027b58a-34eb-3d0a-9aa7-9ce955c1c632 | -29.41122 | -52.09079 | 2026-03-01 04:48:00 | NOAA-20 | FORQUETINHA | RIO GRANDE DO SUL | Brasil | 4308433 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f89e1bc9-a6fe-3008-8000-995a7d6bf44e | 1.5047 | -59.8925 | 2026-03-01 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7fb007ce-a697-3aec-bc80-2f83a2e01022 | 1.4864 | -59.9117 | 2026-03-01 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 144.8 |
| e3c4c61f-34f4-3226-a888-ee3f72f89817 | 1.4864 | -59.9308 | 2026-03-01 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 86b4b6a2-cb00-3469-ad2b-aeccf92cd2f5 | 1.5047 | -59.9116 | 2026-03-01 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 86963575-f2eb-3ed2-a7db-ad64b814ad5a | 1.5046 | -59.9306 | 2026-03-01 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2f4c40d9-7bdc-3e5a-9ebc-43ea185de116 | 1.4682 | -59.9119 | 2026-03-01 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1e91cde3-e1b9-3b69-b564-224aeb8a9b84 | 1.4864 | -59.9117 | 2026-03-01 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.2 |
| ec754554-7acd-349b-8625-0d527f20dcaa | 1.5046 | -59.9306 | 2026-03-01 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 804debc0-6c96-3ef9-9eb3-107ab801f511 | 1.4864 | -59.9308 | 2026-03-01 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9d30b8cc-e588-3589-a060-ef1d8cb22cec | 1.5047 | -59.9116 | 2026-03-01 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.5 |
| c57bfc87-2bed-34bf-959d-bd2afc3967d5 | 1.5046 | -59.9306 | 2026-03-01 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 702ea4f1-9c79-3bf9-a80d-6cae3e9a3bca | 1.4864 | -59.9308 | 2026-03-01 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 3ffd8e35-377b-3f0b-95fd-337ded46f49c | 1.5047 | -59.9116 | 2026-03-01 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 151.8 |
| ca93bd14-46d5-343a-a70f-432cd202e34e | 1.4864 | -59.9117 | 2026-03-01 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.1 |
| d5cb5cdd-ae94-3389-a80a-53b4984fa55a | 1.5046 | -59.9306 | 2026-03-01 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.7 |
| ea890b6e-446c-38cc-8a42-f5744d4c511a | 1.4864 | -59.9117 | 2026-03-01 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 3da9b576-a83e-3f51-a37f-93f78a70c9a4 | 1.5047 | -59.9116 | 2026-03-01 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 49e9d7e0-cfde-34a0-93d2-84ecfab3db9e | 1.4864 | -59.9308 | 2026-03-01 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 439cbef3-6b62-3cb6-ac0d-858427d2a0d6 | 2.22129 | -60.7486 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 965a27f4-2130-37ad-bacb-9e64ea69efca | 3.49217 | -61.94264 | 2026-03-01 05:29:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57ceab02-d98c-3f93-85a1-c6f0249d6130 | 1.48178 | -59.92143 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed08cc2d-31f7-3e74-a2b6-1e6bf8293ee3 | 3.15464 | -59.92444 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6a61bb6-9eaa-3755-a783-a6d6bd7b1009 | 1.0666 | -59.2482 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 360e9c08-a326-376f-b95a-0ab359f13bd2 | 3.15632 | -59.91366 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8162c876-c278-3e70-a33f-97c73848059c | 1.02506 | -60.54719 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ddf095e-fcd3-32dc-9350-cf9ce77b2d57 | 1.3706 | -60.05824 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6c6c9fb-ceb4-352e-ae93-04a72d5eb00e | 0.57709 | -59.90401 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f50019bf-f950-3987-9420-5de1e4fa3108 | 1.47188 | -59.92295 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bc76fc95-d2a0-39e3-9149-08a189f3d817 | 0.19233 | -60.44382 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 392badf3-2e15-3a94-8e0d-a346c4d80f62 | 1.50044 | -59.93263 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
