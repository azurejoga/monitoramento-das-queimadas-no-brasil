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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 446bc07c-978d-31aa-9861-86a95abdce40 | -3.041 | -50.37371 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83ade1d0-af12-3c6a-a4cd-490ab11eace7 | -3.47455 | -50.80458 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e97fb19-971f-3c91-b36b-d6cf8d928dd4 | -0.39402 | -51.94634 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81c2d732-2372-3387-a66e-cd6a2cc0b94e | -5.20214 | -44.91943 | 2024-11-09 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb5655bd-1d59-37fe-b314-b008c5c23a0a | -3.95781 | -48.15953 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53b04b1a-fdb7-3e38-80f6-ef066f8d4393 | -1.50835 | -52.15499 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76e7d58d-d373-385f-b99d-1edaab0d1672 | -4.20653 | -48.54823 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c04d6723-082b-3b53-b57c-0f0af56deba6 | -5.43509 | -46.94443 | 2024-11-09 04:55:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dffca7a-b5c1-38ea-b9a1-2b1593130e0f | -3.66479 | -49.95229 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71321006-3e88-3915-ad98-9a838b9e1a03 | -3.25483 | -52.23769 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28707316-bede-3344-b9dc-668976719497 | -2.72499 | -54.9128 | 2024-11-09 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5e6a972-62e8-3b06-a4a9-3294de253bd7 | -2.23741 | -53.67072 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fe9cc61-7d08-3ee3-a1bc-06808ad285f3 | -3.91544 | -52.40811 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acac56d5-c0ca-3c80-aedd-d66e45310b6a | -3.98661 | -46.41755 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fc9d348-0e70-3a80-8d46-17b81f467d1c | -4.05066 | -47.38454 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5031f5af-413b-39d5-9c94-2bf5bc69caf7 | -2.19061 | -53.26038 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31927b93-dd4e-32a3-8125-cd51e31cb2aa | -4.01577 | -48.29646 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 117ef867-d49c-3952-ac5a-83fbf2319dfd | -2.23139 | -50.52387 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5a09cad-e379-391b-9e44-9be2baa43306 | -2.85013 | -49.22661 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98cae318-1c17-3d2f-bcca-31ba22709a0f | -3.68585 | -51.30445 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d9706c9-21b7-3df1-8b1e-fa307b8d4195 | -1.56565 | -51.29578 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2edfa3fd-bed3-3e1b-8cb6-03e0d9cc34ec | -3.02984 | -51.53174 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 462ca266-64c5-3971-ae5c-e76290f38be5 | -5.63595 | -44.83194 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be18fce7-0608-355e-8285-ff46c6d2d7b6 | -3.74321 | -50.17358 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 891198a3-8dc7-32ed-ac15-1d5c7996b931 | -2.32676 | -51.98557 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd5181cb-5f57-3366-ac5a-a3e86f77e9cb | -2.29171 | -50.64437 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c905cd4-de2f-3e76-bf2b-f084ddae2738 | -2.47843 | -54.05084 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccbdac8a-0649-3bda-a5ba-c05ee85cec1e | -1.1593 | -53.66181 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff91c8dc-21f7-32f9-8afb-a6b18d04ed73 | -3.95257 | -48.16622 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3cab09b1-76aa-327e-bd4c-2cf9badad28f | -1.23877 | -51.75678 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d78d86f7-775a-3b9c-ad0d-eb2e8d0f54f9 | -4.21587 | -48.67931 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76939fff-89d3-390c-a543-0f86298c8b57 | -3.97573 | -46.41429 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 516a7ec9-e60d-3005-882d-7ded67dc9889 | -2.19644 | -49.28988 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bca7765-5a56-33ce-9400-c9250df771fa | -3.08282 | -50.56565 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5bc18213-73d8-3e8c-b2bd-6699134890e0 | -3.82208 | -49.85337 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6b100257-24a9-3026-a08f-396e7d2c4404 | -4.20601 | -48.5518 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c43797bb-3299-311d-ad93-ad203bd8f9eb | -2.8123 | -52.96548 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e0a14f6-9938-3e62-bf9a-f4d2a1b8e3e3 | -3.53733 | -51.256 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6084731a-de62-37fd-873c-83fb3ea713df | -2.88846 | -51.7458 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 66fb717e-0db9-3aca-80ee-04ab596f5038 | -2.30977 | -50.66711 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d63a2a5b-d3e6-3fd0-bd7b-e320c0cb3646 | -3.04753 | -50.37887 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2c93949-df6a-3856-98b2-9f0233611ad2 | -3.76561 | -51.76217 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1ec475e-40f6-3367-a4d0-b564d05761b7 | -1.45212 | -55.2759 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95a6932f-3b50-33e2-b50f-ba258c49308f | -1.34549 | -51.42935 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 717fa899-5add-3e2c-8676-3b4592e3245d | -1.15711 | -52.00397 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8122a010-dab6-30ac-8391-153fbea4efe5 | -3.20121 | -51.03458 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a14d59e-3225-3f6e-86e1-8082b937d92d | -3.50398 | -51.40147 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b462a054-87aa-3896-a8ce-532a93b61536 | -1.39665 | -52.06609 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8f3db1d-92d6-3bf1-a021-11f4bb68c090 | -3.04407 | -50.36526 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66c899ae-1cd2-359b-b17b-6246f3ff57d9 | -3.95008 | -48.15445 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3775d67-9cce-37d0-9323-7cd69285a9ea | -2.86076 | -48.45412 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62b46907-7b75-3424-a169-b9179300b23d | -4.80663 | -44.7769 | 2024-11-09 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c774a7c-ad78-3021-8cfb-1aa01c148c4e | -2.94764 | -54.45188 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f5728c-dbd2-39ef-9bb1-bfa9606f74df | -2.27755 | -50.66615 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f52c3aa-aa13-3b29-a2a1-4f651f9a7962 | -4.20248 | -48.5476 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b1d461b8-e558-300d-bbc7-b5e9518aad7d | -3.59939 | -47.34697 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| de7447a1-5a32-3068-a818-af163334deb4 | -3.37564 | -52.35371 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ba0e4b1-1378-3f55-852f-2a3a1f16c298 | -2.87223 | -50.41164 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37272d8b-14ef-3425-bcca-a4e8c62d1fde | -3.21019 | -54.05072 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbb17092-6e47-3619-a47b-959bc40cacdc | -1.56769 | -51.66549 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d79bf43-0c69-332e-b47f-d057d688811c | -2.26813 | -50.68059 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fceb3b83-3502-38a7-9dc9-f2b29d2fa485 | -2.56842 | -54.16499 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b67853b-bff0-3f4a-9aa0-3be27f183b1d | -3.24067 | -50.45626 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f361416-845a-36e5-910b-688486bfde86 | -4.49305 | -48.48962 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d149d82-baf5-3a1c-b2a3-21d1bb33eb01 | -3.30639 | -50.08442 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e0faa2b-2835-3a3c-941e-484fc7a0c787 | -4.43713 | -48.06241 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d905f787-f82f-3ebe-9bdd-7f959e9578d7 | -0.22507 | -51.64418 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e3a092fb-1472-3650-999d-f213bdf48c11 | -2.72135 | -46.66903 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 074e3b79-633e-37d6-bea0-743a137fd7e0 | -2.12436 | -50.13898 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16e30cc9-2519-3ddf-9924-0c65a514d358 | -1.53808 | -52.00897 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f3d22c7-9ee3-346f-9c20-c76b938cba39 | -3.50115 | -51.1452 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14754659-3409-3b13-8035-b1c70471ffb5 | -3.95644 | -48.14025 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b63267-dde8-3dde-8ae8-fb9594bfb50d | -1.27318 | -52.18612 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360f083d-23d2-38bd-b8f8-dfe89b52e176 | -1.51228 | -52.17348 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b86adcbf-c8bf-3367-9cbb-6f819c31084f | -4.31449 | -48.6556 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 737e5868-4ece-37ed-8781-65710aef131f | -2.87042 | -50.32816 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d99346a-89f1-3dc5-a595-2a40ce4a3585 | -3.01566 | -51.04328 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d0d4691-6a21-3983-87b1-7faeeca86444 | -2.07849 | -50.34296 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 266bf5ff-38f6-3d2c-a016-218ea7f34f1d | -3.03236 | -53.26526 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b55bd5a-e4af-3b7c-bbb0-2061b53c8746 | -3.69468 | -54.61886 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e236d6ff-90e9-3fcd-b2a9-22d7f0851add | -3.0854 | -51.22012 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d092fdc-2a90-3883-9dab-046cc044e2c9 | -2.97165 | -47.92389 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0d08f97-4f39-3dd1-b88d-0796f8fc5868 | -3.98192 | -46.41692 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8ef90aba-37a6-37ee-a33d-1b30b7f8ea63 | -3.63408 | -50.18011 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e9b65a84-caf5-3d5b-ac79-4e756dd21ece | -2.86115 | -51.24793 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebc3ed86-2a03-3e76-a364-c979f55eb007 | -1.37274 | -52.26245 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 618e62bf-e47a-3e58-a39f-8189e8b0c9c9 | -0.89729 | -51.77708 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b76e06ff-bd42-3cb9-8a4b-2d2623a1d304 | -5.50064 | -47.17085 | 2024-11-09 04:55:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96703c9c-cdd3-3b53-a96f-ca310251dfd3 | -1.38655 | -51.57163 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c185d682-e876-3de1-9ec0-9c7fa4562099 | -3.95587 | -48.14407 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 372e63b4-3ac5-370b-9479-0dd9e9c6892e | -3.07415 | -53.87982 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dd07c4a-1f53-317b-ab1a-9fb77b943db8 | -2.31257 | -48.43503 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b7f5a2a-a2b7-3a7a-b31d-72a637d104a6 | -2.88951 | -48.29358 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| edba14a6-6bf7-39e5-8da5-504d1f6a72cc | -1.32259 | -54.63972 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e32d112a-e401-39f7-9c74-20e9481199fc | -2.15911 | -53.69765 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7662c83d-c47d-390c-99a6-af387963c2f7 | -4.09641 | -48.31939 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d158de5-9538-3881-bdbb-2ae4253c5c60 | -3.14508 | -45.16455 | 2024-11-09 04:55:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28c0fe6a-709d-3641-9a5b-f69683b26f17 | -2.56837 | -47.34897 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce43a75d-e7da-3365-9598-ed2574659853 | -2.54348 | -54.00722 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc3f0894-01d1-38ae-b11c-dadfe83f8439 | -2.96029 | -48.02448 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README70.md)
