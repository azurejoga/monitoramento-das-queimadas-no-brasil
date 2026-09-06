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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6a2ee0f-eb66-3be1-9c9b-a51c7e0737f4 | 4.19794 | -59.9617 | 2026-09-06 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58621649-34df-39da-8e53-9379ff32b905 | -2.86228 | -50.46527 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bffda1e8-430a-3b15-a851-14edfe418e09 | -2.76721 | -48.57396 | 2026-09-06 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 99cee5a6-1f77-317d-94c3-36eb8df75413 | -1.49391 | -54.82738 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 638172de-6836-3ba3-8f20-a88b0e6a8a6f | -2.29773 | -48.58864 | 2026-09-06 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 239f3a5c-7639-3a7d-a5bb-c861ee2be81d | -3.85415 | -44.05173 | 2026-09-06 04:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ebec327-fff6-3df4-9cc6-e3565ca67d4e | -1.39186 | -55.17872 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52a005b7-e31c-396b-9cd9-c8ccd5e79a90 | 0.02906 | -51.64927 | 2026-09-06 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0977ebc4-8eb9-331c-8220-3babb042d3b4 | -2.73361 | -48.56161 | 2026-09-06 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4869cfe5-d529-3779-a3c2-268e1b844b24 | -3.97578 | -43.10806 | 2026-09-06 04:44:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 053f7009-e31b-3b23-adce-6605bc86c3b4 | -2.85898 | -50.46477 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dcdff09-393e-3d72-a32d-d1ddaccc61c6 | -1.49077 | -54.82167 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1840ebff-439f-3528-a6c1-ef2fd0a68927 | -2.26353 | -47.00491 | 2026-09-06 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5108539-5db8-3264-8f1e-8cfe8920b834 | 4.19831 | -59.95887 | 2026-09-06 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f22e6b26-8dcc-352d-9c41-0b4bac2b9295 | -2.91393 | -48.1 | 2026-09-06 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85360b42-97d2-3532-be2f-1ef2cf28ab94 | -2.9555 | -51.28326 | 2026-09-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 921638f5-e652-3011-b650-9398dace64f5 | -2.02646 | -52.10592 | 2026-09-06 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2343ff53-be6e-3a54-a8df-2197127bb134 | -1.49472 | -54.82229 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23c8432c-2306-3f5c-9470-9aafa66b945e | -2.87273 | -50.46337 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| badbeaf2-7417-3237-a2ce-3d4660cc537b | -1.86967 | -47.98061 | 2026-09-06 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c04c6b9c-665f-3ff7-9f6e-e34ba2bbccc5 | -1.86277 | -47.97956 | 2026-09-06 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00bea898-8934-3d2b-9b6c-d0e432b32a68 | 4.36393 | -59.75209 | 2026-09-06 04:44:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 721c88b8-e362-3c71-8cc4-1ad13999f7dc | -2.54062 | -48.245 | 2026-09-06 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75ff5afd-af5c-3dd1-90d9-402218ad3c6a | -2.29377 | -48.59174 | 2026-09-06 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83cc34d4-3b1f-304b-8f42-4a0d00856108 | -2.58576 | -49.49001 | 2026-09-06 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa16da03-2bd7-33b9-b38a-3dac7b823737 | -1.49787 | -54.82803 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c51116a-17f4-3453-a495-4765da119995 | -1.39646 | -55.17579 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7def3962-02a3-30f8-846d-03746065d445 | -2.98018 | -50.51524 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f011f22-7582-3a66-a030-693fa0cbe037 | -2.87934 | -50.46439 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f9ca92-b7d8-3283-9a8d-d3c8e2c454a2 | -2.86836 | -50.46973 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aefed444-fc23-3299-85dd-a87e92019ae6 | -1.86911 | -47.97974 | 2026-09-06 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1fef6f4b-7c22-37fa-b074-a1e9ba169a24 | -1.39752 | -55.17233 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 91fcc4e2-2c6b-3aa4-8a62-2b042964b911 | -1.39347 | -55.1717 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb80b82c-e83d-35b2-b8c2-9da035b6b162 | -1.48996 | -54.82673 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07fa9d77-daab-3a86-885b-d351d263c8bb | -1.39296 | -55.1716 | 2026-09-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b97d0192-bb86-312b-8055-3364c553e0bf | 2.30729 | -51.66261 | 2026-09-06 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0bce814-a26b-3f90-8d1a-85ea340fdd9a | -2.86889 | -50.46629 | 2026-09-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cabaa213-2052-39f5-a4c7-61b542703b1c | -2.58908 | -49.49052 | 2026-09-06 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6073534e-d111-37dc-ae20-5f112d81c4e1 | -1.20174 | -47.76133 | 2026-09-06 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0d3c8bf-1294-3860-8987-99c9f9316e20 | -1.18369 | -53.82603 | 2026-09-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb816fd9-7033-34ed-b75d-2b6d02555799 | -5.36382 | -56.02391 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d40e62bb-1165-36bc-a0de-1de98dff9f96 | -5.14904 | -55.9581 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a7579a8-1bda-38bc-b51b-0a6706b30527 | -3.22784 | -58.88993 | 2026-09-06 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4621590-8a03-3c86-a68a-2bac8ddc91c6 | -5.9272 | -45.51773 | 2026-09-06 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a10854bc-9c86-3ec1-bedb-8e725323ec80 | -5.84672 | -60.2557 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ec359c9-d5fc-3d1d-accb-83b18df11f78 | -11.28369 | -45.71255 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce7e919e-4399-31ab-9b7d-036fcfe7300c | -3.76966 | -61.76123 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f8ac4d0-b6ee-30f3-8e4c-a94e2e885ca9 | -11.28937 | -45.70418 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c431b47-4a6a-3154-8cf1-3772c43cf4ef | -3.22564 | -50.29366 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea359e7-1e07-3056-b3cc-c5b88ffbb8cd | -11.28814 | -45.71323 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71312387-786c-34ef-8d25-ccac21d3cdeb | -3.81018 | -55.8966 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61298b63-699a-30c6-9a71-34c6fc63139c | -3.54941 | -48.18589 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 45c2e6b0-3ee5-3886-ba72-87788c3b980e | -5.37246 | -56.02171 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c7d4c1f-ce35-3504-97c1-13cadc0314ed | -5.30378 | -55.86282 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee9a57b8-1459-3e82-b3a5-16738d9ff684 | -3.76508 | -61.75801 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87d2d23b-f4b2-3188-a3c8-583774f8025e | -4.47791 | -55.08706 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2da48ab-df51-3839-bef3-75131ea3504f | -6.05668 | -57.79362 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f0080a1-a268-393f-aa06-694e02a79fa1 | -4.36531 | -47.78035 | 2026-09-06 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| cbbf2be1-ea4c-34e7-bda2-8cc92ff7f551 | -10.03863 | -48.21769 | 2026-09-06 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9e909a6-0671-3a6a-b719-5bad1ef57c64 | -6.51652 | -58.29676 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40f9bf3c-7013-3f74-b7a5-a25847ce560a | -7.97128 | -54.90413 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee118207-f0b1-379e-81f5-31cf6b2103ac | -5.15768 | -55.95584 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b67f70a7-f9d5-38af-85da-f92671ca3059 | -4.77688 | -56.11541 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c8667de-a028-3355-b6d1-ebea37b960d3 | -3.76428 | -61.7626 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42166f71-4e0e-3dff-b828-04d59948aa2e | -2.45453 | -57.91663 | 2026-09-06 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0780847e-1f97-3927-8a29-1ae1c8027f30 | -4.67785 | -55.64077 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73a6153f-6f33-3b7c-a3ff-adc48ee85ea8 | -3.16288 | -50.82597 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c6012a1-b777-396a-a974-c701ab890a18 | -4.63704 | -48.63705 | 2026-09-06 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2df1203c-e9e4-35f6-b809-1ef7d06d335b | -4.1368 | -56.34165 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42d813c3-ac3a-3a86-8972-d5619124d815 | -4.47632 | -55.09677 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6428b7f7-4429-3a53-98be-9847b6eace00 | -5.35979 | -56.02324 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ede3d9b-8a64-3670-9b60-fc70cee12f35 | -3.14018 | -60.6397 | 2026-09-06 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16843e50-cba7-3e0f-970d-39fae7292cde | -7.37735 | -47.7595 | 2026-09-06 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 166054d7-4a67-391a-992a-3c626d889584 | -7.2817 | -55.14415 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 204854c7-4f07-3345-90a1-73fddb7dc74f | -5.77184 | -45.06944 | 2026-09-06 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b876e1-4e63-3e23-b697-9ac373fdd5da | -4.67954 | -55.63019 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 856bec4b-7aed-3a94-97b7-c9c8758cd38a | -5.14731 | -55.96872 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bd83fc77-0430-3c69-9874-8c53c52639c2 | -5.847 | -52.0394 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77950f38-806a-3bae-89f9-6dec3dd1b47c | -3.94135 | -48.44142 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ae696d-736f-3c3c-a5ff-50241fcef1c0 | -4.47248 | -55.09609 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eacd6f58-f7cf-3614-b771-59c8c1ccf9e7 | -5.65385 | -60.23806 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da4041e1-270e-33c9-b818-c264e6d9dd1b | -5.27792 | -56.11628 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32489fa1-22cd-390f-947a-7ee7c040f057 | -8.50031 | -54.6514 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c199cd0-9f12-3ad8-b84c-9bc614ef5d1c | -3.94538 | -48.4382 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8595201d-820b-306f-8e65-312a892d95bd | -4.45441 | -46.13324 | 2026-09-06 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e1dd291e-c71f-3154-b887-3a9aa0d242d8 | -5.17474 | -56.05896 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0753e4ca-b53e-39a2-87f4-3fbc35566fc7 | -3.93561 | -48.43281 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a00d7fc-3f8f-333d-b76d-2731005366e5 | -3.94193 | -48.43766 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e19aced-a2c6-3c97-b8af-f01b3abd45f4 | -4.45832 | -46.13395 | 2026-09-06 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 97ca038a-30ff-390c-97f8-28d562abed81 | -9.32857 | -48.44929 | 2026-09-06 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3e16971-9243-3be3-b848-1e9f753df58e | -3.79149 | -55.8824 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94230bf5-643d-3652-83a2-725a02d646be | -5.34999 | -56.03252 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8049f7ab-b9e7-33f7-95ae-40c812623252 | -5.3523 | -56.01835 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9ca6003-e24d-34b5-a642-f37ae3d3ee04 | -6.09376 | -55.59084 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dfe436e-06a4-3142-8093-369acbe2754f | -3.23348 | -50.5727 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9e2dc48-5e83-3daa-8fd8-5a76684b83a3 | -4.4505 | -46.13258 | 2026-09-06 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a47b957-9234-3332-96fd-1fa6710c14a6 | -4.11726 | -49.07933 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e80397a4-4c01-3cdb-8768-03e46ac4cc6a | -6.87876 | -41.04461 | 2026-09-06 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07ebd7a1-2413-36c1-80f0-51e5ffdeb305 | -5.13886 | -56.27344 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b6cdf0b1-f012-3636-9f17-5a2bcdf485b7 | -6.87419 | -41.04588 | 2026-09-06 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
