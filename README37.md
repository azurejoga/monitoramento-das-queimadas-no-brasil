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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bf64143-36ce-33eb-b8b9-06205f48e2ab | -6.64714 | -59.94021 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dc1af093-19a0-3fe9-84bc-c69122c32b24 | -6.43833 | -55.04924 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 22b534c6-7e7e-3d84-b722-cac166ec52e4 | -9.56008 | -59.77382 | 2026-10-09 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b6441838-c88c-3529-9272-61057b91ace1 | -10.40072 | -54.02599 | 2026-10-09 00:35:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 984b0a73-7a08-3f14-adb6-e9025bd15133 | -9.69225 | -58.09927 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4ba790b4-e80e-31e6-a2e5-98ebee6a71ec | -7.38568 | -55.22607 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f28286c-10f0-3175-b6fb-264291d2e089 | -13.79022 | -52.79179 | 2026-10-09 00:35:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c7573a2f-2dac-339d-a18a-e55d6dd4a374 | -7.384 | -55.21463 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cfa57b60-a418-3bc8-bf3c-6411a8d39f90 | -6.72863 | -63.04595 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 04e5032d-ad23-3fa5-8bfd-cd5c2c3bd6ef | -6.48734 | -55.31322 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d1f9aeb9-e2be-383f-ae24-91915ad080ec | -6.00031 | -53.50325 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d7b47e36-3e4b-3641-af3f-3cfdb60db4fa | -7.57432 | -64.5395 | 2026-10-09 00:35:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 61894440-d8db-3079-bd05-2209e73f546b | -6.48784 | -62.85685 | 2026-10-09 00:35:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 96470e58-abbd-3dea-9b20-62e32b1ee25d | -5.71158 | -53.49839 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 49225923-26ff-3a75-a2da-6be3825a82fe | -6.10243 | -55.69575 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8a0ae729-b547-36eb-91c5-5e6d6c239fc6 | -5.70638 | -53.46451 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| eee36459-097b-3d1a-9889-bdd50b7a47b3 | -6.50755 | -55.31014 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c94ba8a5-03df-30e3-8f85-35d36f2fc50b | -6.38221 | -56.22969 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b8456675-51cc-3690-91dc-01240f920823 | -9.20971 | -57.73001 | 2026-10-09 00:35:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9de51fd9-225a-3031-bfd8-c98f9fe1d3fd | -8.25479 | -54.72844 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1548c956-a907-3ed2-9e6b-3cc1d009b610 | -6.74638 | -55.12214 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2a142e15-379c-3100-906a-a72e75b89d2a | -6.68689 | -59.96291 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5be8ecbd-f99a-3870-9d23-f40fac01c2c3 | -6.90137 | -55.55707 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec323fe8-9092-3a1f-b0f0-3f1907830e19 | -6.21729 | -60.03042 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9024ba06-34b3-3236-a031-94ed539c9cc4 | -5.8916 | -57.72767 | 2026-10-09 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 4fb50971-c623-3c3a-a834-5b996a26580c | -7.44873 | -63.56103 | 2026-10-09 00:35:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 0d20ed16-bde6-3dc7-a531-2ee106ef219b | -10.54448 | -57.45402 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c8006dd9-b9e1-3727-888a-5edc6f306aba | -13.18706 | -54.356 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 816f1d75-c639-3029-92c8-29eef49c00ef | -10.39291 | -54.02054 | 2026-10-09 00:35:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1a347aa1-d5fc-30dc-b51a-e8fcde361011 | -5.70478 | -53.50557 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 041fabb8-36ca-348f-857a-25a70216086a | -5.94964 | -55.34552 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 81730a1c-c301-3d19-926c-8743182d91ad | -5.96995 | -55.34231 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e9885c9b-cfd6-3686-9dda-8e318c98bd22 | -6.92479 | -59.26844 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d89bbec7-6b02-3ac0-af42-22172b51eb04 | -6.41977 | -55.19494 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ea7133a3-a6b7-3a0e-a07d-58b2416d51de | -6.48562 | -55.30142 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1165ae55-2a9b-3cf6-bfa6-9b3650a83eec | -12.20787 | -57.10052 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c4a687bb-147c-39b1-9d23-0dd0a79d522c | -8.23608 | -54.74368 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 12c7660e-82e5-33e9-8843-5913a2607289 | -13.15609 | -54.34945 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 143face0-3e2c-350b-8a43-232b669694cf | -13.18872 | -54.36711 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| cab0721f-a7f2-3ed5-8832-2d687bd4c4be | -6.69715 | -59.97092 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9eefe410-7387-3080-b5a5-f4096fee0f3e | -5.70404 | -49.08521 | 2026-10-09 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 7815d4bc-f268-3a93-ad7b-126464618bdb | -7.16788 | -55.13871 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d9e62b7d-a32d-385f-a924-40d3a27e68b2 | -8.17231 | -54.72168 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 24adcdb6-1c7e-365b-8b76-e13e70656250 | -5.9953 | -55.38128 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d864d900-cbf1-3fd0-8727-a4dc4cf8e0df | -6.94723 | -59.10207 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f47c38d3-2349-3ae6-a33d-e74c438ccebc | -6.50924 | -55.32192 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 075b81d8-bf44-3b0b-ab2e-39f0fdca0d8b | -13.20824 | -54.36408 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| bd105f01-63e2-3220-a939-4d9cf87a0cdc | -6.74144 | -55.1597 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| fae471e0-c2d7-3110-90b8-2d4497bf4ef1 | -7.00381 | -59.10643 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3927d180-b22d-32bd-a9bf-35dbfa62b6ea | -7.57265 | -61.54848 | 2026-10-09 00:35:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4eae01a5-e4bf-3534-bd3e-3f83d5a02889 | -5.70895 | -53.48127 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| dac77b3e-167a-3ef3-be21-57cc4ae715b4 | -11.77233 | -58.28306 | 2026-10-09 00:35:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 42bb9908-6074-3c70-ab35-4b3e0ce335e0 | -6.05291 | -59.90674 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3f95b446-1080-3316-b56d-57683961c0bd | -9.2092 | -60.86728 | 2026-10-09 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 94487c59-6957-3070-bd8a-6db1a4a07d9d | -11.99395 | -57.61794 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7d867616-2e90-3889-8aee-6e9d975f449f | -4.62969 | -49.21675 | 2026-10-09 00:35:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b4cc2dfd-1c81-35f1-acc8-a2c572f3c177 | -7.22176 | -55.08183 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 4ae955b8-0617-3188-93df-a310dba36b54 | -10.87978 | -57.08651 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4d28e864-189b-3a3f-964d-9e81cbe901b9 | -6.68172 | -63.0243 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 25619546-0bdc-313e-a138-82e3d369fbfa | -6.85676 | -59.0487 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 775e2449-7d78-3d86-9c60-f682ee1b92c5 | -14.55567 | -50.03339 | 2026-10-09 00:35:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| da3d8e83-93bf-32e5-b50c-bd1901a48fc4 | -6.99497 | -59.10767 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5793a86e-134b-3a3e-ac98-43a974e4644c | -6.50763 | -55.38213 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 04f2d887-fc0f-3452-a248-b166a441ccbe | -7.07892 | -52.68336 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 0da347b6-e2c8-3a7f-80fb-95748d672651 | -11.97507 | -57.61154 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 87ac635f-e903-3ba3-9ab4-0f6319138a92 | -8.23807 | -61.39912 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d7842750-8d1d-3acd-ad59-bccc8ef1d8df | -5.68814 | -53.4743 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| a5e6854f-9040-3163-8c5d-54093d0228ad | -6.73792 | -55.13559 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 69ae2b65-67ab-3b03-975c-4eca21e84c00 | -6.05415 | -59.91584 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4683bda4-7870-31f2-9e97-029a7778ef71 | -7.20174 | -55.15791 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| d94c5631-c887-3c4d-b462-bd08ee761bd7 | -5.70926 | -53.4534 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c80c55e6-4cb5-34e7-ae8e-def70ce91a1c | -7.57115 | -61.53728 | 2026-10-09 00:35:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 144cc2ea-1661-3034-8144-c05e137d32d8 | -7.50654 | -54.996 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f1a2744a-65fc-3bf9-81cd-e46da4c9a53d | -10.02351 | -48.05568 | 2026-10-09 00:35:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6c0f4d00-8f41-3574-9129-2911aa107737 | -6.48615 | -62.84369 | 2026-10-09 00:35:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c717b7cd-0155-314c-ac5b-c3b58de1f2ad | -13.17563 | -54.34637 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 11840d71-30d0-3f5d-8e91-c10f3c6d96e4 | -6.84975 | -59.39462 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b99d47bf-bc03-3eac-a3b2-3a5e33f72f80 | -6.22753 | -60.03836 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7770d235-4757-3237-bb38-a6694342ef68 | -11.45805 | -54.29979 | 2026-10-09 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ca72d06d-201d-390f-ae17-8d4187d96d1d | -9.85575 | -47.47845 | 2026-10-09 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 71b07467-9bf0-34b3-8680-6025800de10e | -7.44674 | -63.54561 | 2026-10-09 00:35:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 30eedc2c-ff2a-3bce-9fe4-b03ad2cf4290 | -6.92358 | -59.25951 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 154d16fc-5b7c-32ae-8546-7d33e8d94e91 | -6.61929 | -59.9409 | 2026-10-09 00:35:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d2759791-814d-3d2b-b6e2-7113e854734b | -5.98353 | -55.36481 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| a6121876-c569-35c0-aa44-90a3afc1c4ea | -5.97164 | -55.35415 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9fbb9c83-89c6-3fd1-9535-a4bc0cb6c598 | -5.96324 | -55.3679 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| dd849bed-9104-36d3-b7b8-38b935ae205e | -12.09688 | -57.16002 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0e229a9b-6bca-33ac-b989-5c46eb86a08e | -6.48774 | -55.95258 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7073f803-ef3e-3673-8372-bdc46c1a64ae | -6.77598 | -63.15277 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 804c77ad-9520-353f-a799-ec31f7f166bc | -7.18025 | -52.6366 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9e715a07-b766-3ede-8e97-674461951f8c | -7.15793 | -55.13376 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 94ac4a88-04f4-3d2e-90cf-f725907d2235 | -11.45664 | -54.29413 | 2026-10-09 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 446ab7e3-c2d4-3154-b4b0-e2189f51dabe | -6.49573 | -55.29985 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 21af8a4e-2eb6-3adf-95c3-108d75f9fddd | -6.4893 | -55.96338 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 02025169-aade-3d19-a480-8a50d5c370bd | -13.16586 | -54.34789 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| eabcfaa9-6cb4-3031-ba6e-5831f8b3bc18 | -13.1773 | -54.35755 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c72b2a1a-ad1d-3ad4-9126-61958ad663f0 | -13.19847 | -54.36557 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a92b36d5-718e-3296-8091-15a8a706e943 | -7.2304 | -55.14184 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 51d61cd5-c62b-38e8-b632-7887c63b7c80 | -5.85933 | -57.56362 | 2026-10-09 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e47ef1e4-e91c-3ef0-addb-efda75051a48 | -6.68243 | -55.10057 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README38.md)
