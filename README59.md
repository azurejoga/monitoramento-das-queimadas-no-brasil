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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05a90298-bbf8-3edb-89b1-13b2aded91b3 | -5.87818 | -57.78426 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c0e5518-5a5a-35fa-8653-474f783d8c67 | -6.92513 | -55.71951 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d4f0a5b-e49b-3025-992b-c9713920db55 | -6.77084 | -55.64116 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41d1c96-2621-3e5b-aae8-c44c780888ac | -5.95046 | -57.68703 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1221db70-441a-3d43-a6c9-62cc2ae5caa9 | -5.57023 | -56.18195 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19f6513b-22c6-382b-a4a9-df313a62124c | -3.61626 | -55.47862 | 2026-08-31 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aed768cd-5436-3186-9d76-f8ba2b0b9550 | -6.61022 | -58.59298 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f85f927d-1436-343d-9b62-ea7008bb59f7 | -6.93684 | -55.64083 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a02d0c7-ad3e-3f8e-85be-334e311ac164 | -3.63484 | -60.55546 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd5ee09d-0a25-3e1f-aec5-318e113180b1 | -1.60591 | -54.39703 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74cbb429-285b-3478-aa83-5ba3da0fa1a2 | -7.28378 | -52.36728 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e99adc5-59c5-3a71-b67f-69dd337e94a3 | -6.25129 | -55.43504 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 822a15a9-f0bb-3a1d-a2ac-72b5a24ec9f7 | -6.17874 | -55.44596 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28401049-20ce-3633-b29c-78da0c2857ed | -6.42352 | -55.52837 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f92286-1840-3072-851b-0ee17df28040 | -7.54758 | -47.32117 | 2026-08-31 05:33:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d8a232a-e034-326e-b8ba-1d562156f273 | -4.96619 | -55.84644 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39c795ee-6052-34ce-89aa-4f14fd715be8 | -6.12347 | -57.69137 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 141ff0bf-2ae7-3f82-9439-79f32ba0a644 | -1.60015 | -54.40722 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ded64489-ed28-3d8b-b042-485be4f63900 | -5.90635 | -56.93051 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8158095f-db3f-3783-9c72-bfcff9b36f84 | -6.0891 | -57.91195 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25d1022d-398d-3746-a3e1-b6400abd6309 | -5.5726 | -60.22747 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f75d787e-0f1f-3780-b57c-1cf3bb6e4b8d | -4.95911 | -55.84048 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f340f265-91db-332c-a07b-9325979959b3 | -4.1509 | -60.69483 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a945e212-841d-3afd-bbea-d16484ae2194 | -3.86904 | -49.09081 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3d8c602-779e-319b-8620-df128ba3d1eb | -3.61422 | -60.54177 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a6ffd7-4a0b-319b-8e29-a86cb7302f4c | -6.12507 | -57.69516 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f473fb6-157b-3b8b-99a4-6604e457b220 | -2.84481 | -61.97867 | 2026-08-31 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 829d86ca-16e4-33c7-92a6-bd289b7c0a09 | -5.2423 | -55.89331 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8f835880-ac30-3d07-bc41-fc9a29d9ad21 | -3.62818 | -60.55441 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3614dcb8-91bf-37e3-849a-4887a59d304d | -5.25794 | -55.89568 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2903d4fe-f53f-302e-b395-8600f6459d46 | -2.66932 | -59.37002 | 2026-08-31 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95129b5b-423a-39ae-ba73-727035fc0534 | -1.60832 | -54.40838 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c7bdb35-571f-3a63-ad11-37d95865eeb6 | -3.6243 | -60.55736 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3cecebc-d909-3ccc-9959-55a015fde885 | -7.05732 | -52.71424 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f385151-6251-3901-a240-a96a1cfa11b3 | -6.93791 | -55.63361 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f93fe90b-2864-3182-8b1e-2ab82467a8e1 | -4.95762 | -55.85027 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 687a520d-9d66-30eb-8954-755202666599 | -5.94209 | -57.69405 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a817f332-7d37-3bf1-b8d7-894c3e5ca569 | -6.93438 | -55.62941 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1640885b-50e5-3b1d-a815-b987a5c406dd | -5.49334 | -57.14165 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6b830b0-9b08-3b6c-9838-3e69a82ba10a | -6.07742 | -57.89391 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17ad5c02-9eb0-3644-9209-5979a19e23e8 | -6.60963 | -58.59677 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1038169f-f8b9-3759-b49c-5413122e91a5 | -4.96228 | -55.84588 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46d18327-7434-3498-aa3e-fa8da846813c | -4.84465 | -55.83 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| faa92759-f2a7-38e8-9cbd-31fdf778cdc5 | -6.61537 | -58.60537 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 140fc2b8-4d18-37d6-b7ea-1dfc9a7e6f03 | -1.59197 | -54.4061 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4842c8fd-3522-3988-b1c1-7328ec041bfe | -4.3574 | -55.02757 | 2026-08-31 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51e1754b-e804-398b-99fd-f68f753f650c | -6.76099 | -56.33849 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9c23416-7840-3afb-bda0-e0a5d3891a72 | -1.48154 | -57.77621 | 2026-08-31 05:33:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d57aedf0-4f60-3bb4-b8d2-ae8a8520b479 | -1.39586 | -55.74418 | 2026-08-31 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a2b48ec-bf94-3db4-8d67-46d7235e7e2f | -6.11885 | -57.674 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 6f63d9c6-3ee1-3800-9773-56ede33b366b | -7.28527 | -52.54062 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b9a3887-ab72-356b-900c-91c515d6669c | -7.00073 | -55.87776 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab52fa97-0dba-38ee-9772-b3396875a25e | -6.24777 | -55.42657 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60e7f039-842c-37d7-b25a-c4f5e94b2f57 | 0.19741 | -60.50183 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7d9fbb4-c56d-328c-994a-1a7378856522 | -6.77476 | -55.67125 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d009d6-1a81-3f20-8095-f9ac8bb71b3a | -6.37203 | -54.95285 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f579022-f2c3-3595-b3aa-eed7ec689ec5 | -3.76452 | -59.33506 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bcc7247-ccbb-395d-aa99-315b8d87e9eb | -6.25699 | -55.42058 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb64f7e1-80b8-3f8a-916b-625d8539ef76 | -6.78587 | -55.6802 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3250134-a678-3e55-82ff-f6bf8ca3a8c8 | -6.26923 | -55.42257 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae9813f5-eb69-3e42-8444-01f72415183e | -6.12537 | -57.67917 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d71b2b2-ee06-32d1-97fc-0f9b9c379e32 | -5.48604 | -57.14053 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb9b8a46-24e1-32ee-a107-b4f5374781b3 | -6.72425 | -56.34035 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3538b9c5-6278-3d5e-8543-7ef49a2ba17c | -4.15423 | -60.71674 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5da250b-74e0-3357-8a59-967a298dcfa5 | -6.08987 | -57.71944 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c75c3933-3f50-35e6-a9fb-785cde7b5fbf | -7.54676 | -47.32753 | 2026-08-31 05:33:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33485fce-2860-3be7-9eec-40fb4ccd2c73 | -6.77375 | -55.6782 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caffe40b-557c-3fa2-82b1-51717cee84fc | -5.31598 | -55.85524 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 235efc6d-157d-3f83-9b23-69ee6c813ea7 | -6.93738 | -55.63722 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24949305-2184-3700-869f-e16d0c98c6d9 | -5.95822 | -57.68407 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c71761ba-0bb0-3298-aa60-d49512bd597a | -7.06229 | -52.71504 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b069adfc-8ccf-36db-9317-3f7c6b5d89e6 | -7.29033 | -52.54134 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05907428-9351-3fc1-9e34-8b3cb3c13cee | -3.63206 | -60.55146 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bfe3d80-e055-3b4b-bf5b-df9c94f182bd | -3.86836 | -49.09533 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ffd50ed-698b-31d0-ab73-ccd644988212 | -5.87883 | -52.15513 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20fa84bb-a927-3f18-94fb-15c4002da887 | -6.92405 | -55.72675 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de09b9f-3823-3f46-872b-b17cabafdaa6 | 0.01316 | -60.59681 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a00beca-d8b1-3fee-b363-ee3697c9ca52 | -6.15562 | -57.78262 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8480cfac-55e6-3bcc-a92b-83c98212c1e3 | -1.60126 | -54.40004 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff4b4273-7079-3614-8dbb-22e8feb88273 | -6.92303 | -56.63314 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b83f4fb4-2f44-3a7e-be84-54464bb8ebd6 | -4.8967 | -55.91084 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcfbcb5c-ae96-35b9-b84d-559fffa3982a | -6.07694 | -55.54829 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 723846a5-37a2-377b-92c6-e3cb8a58ae7f | -6.92459 | -55.72311 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1edaacd9-1f4d-3346-a7a2-2051b0101d64 | -4.64503 | -55.85532 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32454dff-4a5f-3132-ac77-abab21f3021c | -3.86574 | -49.1127 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e979ee7-b46e-3152-bc35-4e4f6d195b4a | -5.87943 | -57.7762 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a342630c-a113-356a-bed7-8f4805d2ef19 | -6.27593 | -53.33481 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7728466e-cf8d-38d5-aedb-4e9863394652 | -6.41795 | -58.23139 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7616145-cca3-3938-a82b-993dee5f1c89 | -6.6125 | -58.60107 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7efa0afe-03a4-3b4d-aa76-d933c2e78714 | -2.74831 | -60.23793 | 2026-08-31 05:33:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f9465fd-c202-304b-b43c-96077c1ad12d | -3.62263 | -60.56777 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a8e2e52-9b22-3912-929d-ad1f00320678 | -5.85886 | -57.55359 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 57bfcf46-fd1c-3e4e-a06b-3afd75a83c54 | -5.31644 | -55.85355 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e5c40b3-7daa-3729-8354-d354ba013148 | -3.94071 | -59.33068 | 2026-08-31 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 218d5869-f066-3d2b-8ee3-108e2780c059 | -5.3196 | -55.85906 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20614e56-b0c2-3a14-a634-3b338887b150 | -1.60424 | -54.40778 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ceeac7ca-6a1d-341c-993c-246597a90f00 | -5.31251 | -55.85299 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f35f8894-23cd-3dfc-a3ad-000e9572c7e5 | -6.15919 | -57.78313 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23d67abc-63a7-3d12-936d-83f55abe23b5 | -6.02953 | -58.03991 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d37793e9-513a-35c7-a427-f7fd6f6f4ac1 | -4.95985 | -55.83558 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README60.md)
