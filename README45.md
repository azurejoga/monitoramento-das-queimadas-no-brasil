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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5ff4d73-8dae-3856-9736-a1e0cf89dd2e | -3.58247 | -41.95927 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8ebdbdc0-ba43-3413-9060-fa75453a4ff6 | -1.66676 | -52.714 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b020d8a8-fded-3629-8800-234b65fee66e | -4.66729 | -43.45977 | 2024-11-27 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2887af46-ef64-3fd5-8a91-e5e1f7669c5f | 0.97762 | -50.12236 | 2024-11-27 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c277765-3a4e-31f5-b183-e4dd5d5725c7 | -3.0848 | -47.82063 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30e0506e-3bc5-3d26-b835-0d3026dbb111 | -2.3208 | -46.12497 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23e2ce60-4d22-3e26-9157-4887e7ee77a3 | -1.65386 | -55.2363 | 2024-11-27 04:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8841fd8c-7092-3d85-b574-8739c6761d88 | -1.71467 | -45.37548 | 2024-11-27 04:18:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1adf707a-be27-3acd-bd10-47bb23f9ed52 | -3.50976 | -50.30678 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 60600ed0-c12b-3b22-a1a3-9ced8fa62526 | -2.22951 | -53.68554 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cff8e6df-5ee5-3280-ac50-d0803582435a | -4.64637 | -45.93697 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a90a298-7aac-3370-bf31-a527ff3a4d5f | -2.78993 | -48.60282 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84bce75b-f649-3bd8-9d32-cf02c2620367 | -3.9106 | -50.60045 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17a507c2-711d-35ea-b8de-c0f4998b3d35 | -3.29046 | -50.75467 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| babf3204-d66e-3cb8-8b97-87ef1dc1cef3 | -2.18597 | -53.77133 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4186e8a1-8a02-3503-9f39-959393b7e487 | -3.29313 | -50.62225 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67a8074e-00bf-3a75-977d-e1b399970c17 | -3.72307 | -50.18644 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62c6c2db-bb40-31e0-8e76-ff387597e207 | -4.40527 | -43.79309 | 2024-11-27 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd57c156-6846-3d55-bbdf-84c749f5db05 | -3.66915 | -53.65797 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41172bda-40ff-36c9-bd10-52bb06167cd6 | -2.47791 | -47.96536 | 2024-11-27 04:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8154b1c7-3e52-3385-9695-77c43c91f67d | -1.66568 | -52.72077 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57bedbb2-175d-35af-beb7-22818b46e1d1 | -3.0577 | -51.05456 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 814fbfdd-fb18-39d0-b100-ade9d0666052 | -3.94773 | -46.91098 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3822628f-23ba-3957-8b15-5da93eb6883a | -3.01855 | -48.60181 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4187e09-fafb-33c3-877e-501d9d90f57f | -2.10034 | -46.55907 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f718c260-717a-3c8a-ab1f-65e181ca7cef | -4.26922 | -42.43598 | 2024-11-27 04:18:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 53f0cef6-2fe5-3463-8959-997b76f8efd1 | -1.78151 | -52.73658 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4873c5f2-45b2-3412-8e8e-5f7ef032ab29 | -1.31502 | -51.74541 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a597012-a522-311e-b368-529394516f8a | -2.56918 | -49.09446 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f421a2de-68b1-36cd-8760-e57c52d80ce7 | -3.96485 | -48.08382 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc9fd492-4d1b-339c-9d08-27b2f9aecde1 | -4.22069 | -48.66838 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 03866351-0d10-31e0-8ea0-6338277e6ae8 | -5.58753 | -43.15719 | 2024-11-27 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2bfed326-8a5a-3889-b79b-dc77ebc2860e | -4.29799 | -48.19645 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0507b864-e291-391b-b5c4-7c275b4ba0fb | -3.58485 | -50.37696 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f793ace-e167-3e20-a8bc-64d8367d9ad4 | -3.16973 | -48.43638 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 8f20a256-fc22-3e01-adfd-4487ee179948 | -3.58446 | -53.26112 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f59dd65e-6065-30c6-b8df-88cff7eec8d8 | -3.10779 | -53.28041 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 303dc945-a2af-3a87-be58-70c27f2f1d83 | -5.38827 | -42.95826 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c6bb4d52-7d9f-33cc-a944-1ea7bfc53d84 | -3.99954 | -47.92006 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11e8bd17-8de4-3eec-bfb3-e507e8a768ef | -3.34494 | -50.51234 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 522a7ee4-037f-378c-a095-5c35ad82a38a | -1.60571 | -52.74929 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 403b6ce3-c51c-3691-a7bd-4055e41aa4c6 | -1.35807 | -54.63543 | 2024-11-27 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d780818b-02b5-31d9-8a38-f4bf84b2cf06 | -2.89632 | -54.17229 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d3323a1-91b1-3658-a9af-5b539fdcdfbb | -2.80108 | -48.68517 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3b54820-0c59-34f6-93dc-68b736ce92e3 | -3.32706 | -50.05368 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71176b6a-ad1f-3750-890c-e97b4bb4c1d6 | -1.20599 | -51.75742 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3418a31c-aa3e-3baa-8641-ea893b43285d | -1.94151 | -46.59808 | 2024-11-27 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d66d4f83-20ea-35c1-b7d3-c1ea75658161 | -3.95108 | -46.69125 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5429cbc6-39e6-3d48-a28c-8813ef492927 | -4.47591 | -46.65821 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ae35e55-9ee2-370c-b2db-dc53f7c67274 | -2.01995 | -46.38224 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84afcc1e-ef20-3547-9e0c-6f8f4930611f | -2.79638 | -52.91185 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c64e682d-7604-3154-a019-6a1ce4e98f0c | -2.82382 | -46.81654 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb9dd09-d335-3436-a9b4-5010c5ec1937 | -3.71799 | -50.18991 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ef75644-7fc1-3c36-95d8-547e34ddad60 | -0.98917 | -51.71844 | 2024-11-27 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c2108da-a94c-3d8b-8ca2-5840259d1563 | -4.04795 | -48.33083 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f933601c-e57c-3618-b4ff-e49fc087b6c2 | 0.48342 | -50.77805 | 2024-11-27 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96a73227-747d-39da-9619-b1c829d6d02a | -3.38877 | -44.16441 | 2024-11-27 04:18:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ce89a71-5f2f-3133-8ce2-bee0e1d1e64a | 0.94548 | -50.73221 | 2024-11-27 04:18:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1818ff4-35b3-3210-ae37-27c15184045c | -3.09198 | -53.27436 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f292b4f5-8082-3f03-9b6e-4811200f2949 | -1.71772 | -46.21941 | 2024-11-27 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7342d36b-9107-387c-ba40-3f1f1d37c15e | -2.57332 | -49.09512 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1682b9e-f507-374d-9042-ced436079af9 | -2.81957 | -46.82006 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb3f7be2-4bf7-3d64-bb20-9dafeeb645de | -4.17256 | -46.07967 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 16bc97a9-19bd-3f7c-94b4-d1fea1f59074 | -2.11324 | -47.88892 | 2024-11-27 04:18:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c539fdb8-1e41-3f16-a12f-8262b98bb78d | -3.50075 | -44.79047 | 2024-11-27 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a6f7e1a-4e03-3822-971f-8e2f262543a9 | -2.10699 | -52.77669 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f49cffd-0532-37d1-a988-5798248b2977 | -2.69582 | -51.99704 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cd5d97f-9e89-37d4-b5c6-3f6469deabf0 | -4.72728 | -46.57392 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d98adf3-0f31-39a3-a41c-eaf26ebb328a | -4.27547 | -42.44068 | 2024-11-27 04:18:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85f43d4e-74a3-3a09-af54-aa69372afd10 | -3.10793 | -53.27492 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef8361f-c6a5-3882-8a88-6c2016aae821 | -3.89491 | -46.09526 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c778577c-d3cd-377a-aa61-0250ee0e1149 | -3.29008 | -50.61237 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca98d3d6-0a20-356f-ab7e-1c098ceb788c | -3.77517 | -46.68454 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 858683c6-6b22-3c70-92a8-d4a27b5d1a84 | -3.077 | -50.96744 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae9c2ae4-f71c-3467-aae1-b016f70c4cd0 | -4.21478 | -47.21913 | 2024-11-27 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bbb85be-0ba4-3884-9fe7-1532a174f741 | -3.25074 | -50.62477 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a80bf300-1508-35b4-8243-def988044b7b | -3.89665 | -45.62278 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21f501c6-a41c-3fa4-a95b-624fd677dcde | -2.24466 | -53.62893 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f326601f-0009-3611-ba3f-cff2c6989f7c | -4.73826 | -48.12698 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a884122-6880-3e35-9e5e-308ade07cc67 | -3.11019 | -53.2663 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58589705-7371-3a1b-a118-cb0896c7d0af | -3.382 | -50.10169 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cfd7086-ab1b-30a9-ac19-419fd0ff304f | -4.1877 | -50.68676 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36ef22d6-5565-3866-82bf-ff15aa7874a4 | -3.23006 | -50.77834 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcd4de34-3e9e-3f79-8212-b33357b3c7a3 | -2.7064 | -53.1854 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0a2779d-441d-36a1-a83a-a86171e71d8f | -3.00043 | -45.461 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87add2e9-dd5e-3cab-90b4-faf769510e71 | -4.31813 | -45.8938 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aab8006b-e310-3aa3-b5c6-ef679ae2261b | -3.59068 | -44.92721 | 2024-11-27 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6febbf2-3b3e-3836-92f3-e835071014c3 | -3.97248 | -48.08495 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c109f8bd-cab1-3762-adea-01bcae240ede | -3.49711 | -50.49387 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2c7e0bbe-47a2-3b76-afdf-56e3ae3287e4 | -4.04918 | -46.8392 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eb158ad-91ae-3b59-ab85-ffa88f7ecba6 | -3.09032 | -44.4296 | 2024-11-27 04:18:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9aaaecb9-0028-3de4-ac60-d7d65d51eaac | -3.25371 | -51.14151 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3dfa5de0-1e41-3ad3-9566-623916802b4d | -3.60966 | -49.89046 | 2024-11-27 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 142c6610-617d-3b82-902a-121e959c377b | -2.55975 | -48.19941 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec946ae1-0620-383c-a77d-4be361be2e66 | -1.98666 | -51.52063 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b94f8868-785a-3a29-9b37-752bf711a482 | -3.84968 | -51.3821 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f100626f-da0d-3c98-9c50-64ecb087238a | -2.8347 | -54.1125 | 2024-11-27 04:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 5eb9a000-0e1a-3a28-945f-345ac7b1f101 | -3.0393 | -48.5082 | 2024-11-27 04:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b6dff76b-abf8-3db4-9ee1-ed93f8859591 | -2.1928 | -53.7839 | 2024-11-27 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 52d40b08-3122-3d4a-815a-1fbb4fec1b1b | -3.1692 | -48.4179 | 2024-11-27 04:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |


[Clique aqui para ver as próximas entradas](README46.md)
