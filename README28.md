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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1d2abf7-4d35-3199-804e-658404a0242a | -5.39975 | -42.33457 | 2025-09-01 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ee13749-4480-3b97-88a4-753844fae685 | -6.57483 | -43.7099 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c946482-8522-39c6-a365-7df3085e0ad1 | -6.81719 | -43.33564 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 243650f6-f217-34f1-b716-2816688d0929 | -10.04231 | -48.08625 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab05f9d-baea-3363-9b93-bcd6ebe1361b | -7.67307 | -42.65989 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 065d8340-efb8-31ee-93bd-f2dc1c6670f7 | -7.11084 | -44.56063 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4ead907-d373-3a88-bf7d-e14cf574ed50 | -5.76071 | -53.40958 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf184624-ac81-3fc3-ba24-9d933568ac77 | -5.62549 | -42.62365 | 2025-09-01 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7cb6c09-b8dd-3e8c-afaf-c48de28e9b59 | -10.0445 | -48.12317 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e53b48b-7ba1-3851-95a7-ca0c42ca2f66 | -10.04661 | -48.11129 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8643564-a409-3382-9455-33c3189d1a8c | -8.84315 | -47.79833 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b13fcab-8495-344c-8cd8-e486b9aa624a | -11.05018 | -45.14751 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| c5860894-98ec-37cb-a564-503fde7240ae | -8.88911 | -45.12003 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f761d657-3ab7-3115-a2ed-b926acd977d5 | -6.57668 | -43.69852 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99f3dfd7-7f39-378e-af9a-3fd2e6fe4afb | -8.84383 | -47.7944 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bb1a04f-bf2f-312c-8aa7-51f7d2391679 | -6.35386 | -43.56196 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21419520-d764-32d3-b103-dc086a577ae9 | -6.42571 | -43.96103 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| add651e6-813c-3f9e-a872-7f8d9634c013 | -11.90576 | -45.03881 | 2025-09-01 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b9d3e07-bf46-3eb3-a207-3dc8ee1e8346 | -8.87784 | -47.96568 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc2b137c-6612-3bf8-a962-12fd8c557c90 | -9.93027 | -51.6246 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8185887-6f0e-3da6-a1e0-bb5d1e97ef05 | -12.09772 | -44.72495 | 2025-09-01 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c150a22a-2343-3d7d-af9a-673785d1a096 | -8.19827 | -46.7759 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| cc1e7509-4bba-3b55-9f7a-ca9bf66c3346 | -6.27171 | -43.53371 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceaef6d9-a300-3652-a4ec-22b6cf9f2aa1 | -5.56948 | -47.4136 | 2025-09-01 04:10:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3299a3f7-ae9f-30a8-b891-0ebc6561f368 | -9.13797 | -45.19655 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cfa5dbb-5ebe-3bba-839b-40db96192350 | -6.54399 | -43.51844 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b200a18d-9287-3206-8cfc-3d981581be2e | -6.92928 | -45.5672 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 393c8832-36bc-30ee-8d1e-d868ef81dfa8 | -9.64019 | -47.81368 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b6d5b68-7522-30ce-978d-2d3f5e2e3ea7 | -9.67332 | -47.0373 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0affe6c-bcc1-34df-9042-731865b9ed36 | -6.15757 | -43.33863 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16ba7073-fad7-3c99-b76a-8d865dbdcf81 | -8.82778 | -47.83652 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e573cc61-465d-3edc-8f41-a195b4947045 | -7.10897 | -45.34723 | 2025-09-01 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f64ae1d2-d2cd-3a30-9949-d20ff7753999 | -6.03007 | -43.7758 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 438d0904-3d6b-3143-a603-6ba2cfea50dd | -6.14949 | -43.34502 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40afea5f-b5a3-319b-8017-530b17b59e7a | -12.14185 | -44.9654 | 2025-09-01 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66dd7c38-d39d-3208-8a08-f61889947814 | -6.09613 | -43.19515 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9348a9a7-bf51-3e57-bcaf-08630993dec2 | -6.8058 | -52.81797 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85fadda3-b3a5-36ab-ab9e-bad182013a8b | -9.22795 | -47.10771 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36d23496-56c8-3963-a545-873ba58e7b22 | -8.16749 | -45.03736 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 267a14f0-7286-3d8e-83af-3908dbf9defd | -8.17113 | -45.03793 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9befcc4b-529e-381e-b1d2-03e4fa11c814 | -6.15189 | -43.32999 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75f4758b-ff7b-35e0-ab9b-459b5e92bbf8 | -6.84177 | -43.33576 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c9854f51-ca13-3f5e-8b20-ca5c718ab8b3 | -7.94299 | -46.44912 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1cd048ea-71f2-34f9-8373-08a788220e4a | -9.64246 | -47.82574 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6af2f9ab-0c31-36ad-a77a-ca3e2cdbf90e | -7.70297 | -50.27948 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 108354c9-6b36-3d35-9d4c-27782f12ad17 | -7.46133 | -44.81373 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0140a9dd-ca5b-32ff-b4f1-0aa8663733e4 | -6.74583 | -43.79222 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2caa8f5e-cfa4-3d80-babc-5dcf2837c088 | -6.43388 | -55.61327 | 2025-09-01 04:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ddde780-b476-3d8e-8d02-ce789f817209 | -8.47068 | -45.1684 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da5072b4-7c10-39c1-9b83-5cbeede6ea63 | -6.81193 | -52.81904 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04e8fe83-2b6f-34c1-802d-6f88b1a82741 | -11.01762 | -46.94462 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d0352eb-9895-3525-8b2a-7a5c13e6b72d | -6.02511 | -44.88248 | 2025-09-01 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4623656a-f67f-3d7a-b4e8-230a28015496 | -10.7723 | -48.84062 | 2025-09-01 04:10:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b4e1837-6ecc-3992-8242-ec928519e81a | -6.26339 | -42.6102 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 589e3058-e029-3ae2-a32a-a2f1539f0ac4 | -9.28217 | -47.1063 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 144b4e7c-7b58-3216-a4a1-b2e1a7a977b9 | -6.2888 | -43.55981 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b41315b4-605a-3488-ab3d-27faa6a830e9 | -6.44617 | -43.96843 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bda8487d-3f82-3585-b950-04b999c7e4f6 | -6.26353 | -43.54026 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee058d1-b1f2-3751-ac49-0c9f5bc44335 | -8.44112 | -47.3719 | 2025-09-01 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b51898db-72d3-3d21-ab9c-a38dfe2d6715 | -7.08362 | -44.35687 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6326f6f2-8a1b-3ec5-8f06-6dad664b3fa1 | -7.66245 | -49.85015 | 2025-09-01 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c092f98-a9ab-3a2e-8c89-bf680a77b706 | -11.03465 | -47.05525 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d65fa06-440f-3296-b563-29255662120c | -7.06493 | -44.337 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8fd589c4-8647-3aaa-bd81-79b718b6c316 | -12.09146 | -44.71998 | 2025-09-01 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f412339f-87a8-392e-9944-385c7df7894e | -7.70092 | -50.27827 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c312730a-b284-3128-9836-b9fe6ed954c4 | -7.46062 | -44.81799 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 929c83b1-6946-36d5-970b-9805661a93d5 | -6.46403 | -41.74823 | 2025-09-01 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f11d075-605b-38e3-92a2-de1b3d6cc48d | -6.83544 | -52.82878 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 519d13ec-0ef9-3819-bce2-52793109760f | -6.49384 | -44.07216 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 039fc6e6-079c-349e-9819-8f205fbc1e47 | -6.37832 | -43.54277 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 555848e1-9f10-37cb-8eab-6be498ea5ea6 | -5.58396 | -46.32567 | 2025-09-01 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7118e32f-19f7-3d47-8bf1-6d73959713d6 | -6.27278 | -44.77631 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8efde9d5-d31b-3ce7-9c78-bb8070964a5b | -6.9422 | -44.3348 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 758eed75-5649-3f9b-b8df-d7588f860fd6 | -9.63995 | -47.81668 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6f7493c-c964-3f5a-b7d9-00faba6993a2 | -6.46155 | -43.96262 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e5f9385d-39cf-33d3-a7d2-b6108d397650 | -9.60885 | -47.81994 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4614644c-1aa5-332b-a1d6-99bcad701831 | -7.72713 | -50.26262 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e40866a-1fda-39f3-b02b-a2435deff7cf | -10.04732 | -48.10728 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5bdc995-8931-34f9-a76f-08fbbecfd0a6 | -9.63859 | -47.8243 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93265917-3641-3867-ae38-46a5093dcee5 | -9.6431 | -47.82196 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbc76b2f-9598-336c-a658-30f60cee0e3c | -12.32951 | -45.72185 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12735e26-0931-3dbf-8f13-c96bbf369ce6 | -11.02452 | -46.95103 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 1e35cd7f-9d73-39b9-bac5-803a0f218be1 | -6.74324 | -43.78104 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a565796c-7ba6-3601-bd43-acff202d4256 | -7.95629 | -46.34803 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2992fd97-cbd3-325d-9b00-8a3836b21e5a | -6.78317 | -44.62475 | 2025-09-01 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20ce7206-1f97-339e-ae9c-0986f1f4663d | -6.43926 | -42.39051 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 957f5ad0-9d5e-3c31-a20f-40a75f5d094d | -6.50316 | -45.40959 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e672aaa1-2e06-398e-9fb6-59f478a92e69 | -7.4898 | -46.71214 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46260711-21b1-38e9-8f6d-e3369fd63155 | -10.92632 | -50.84833 | 2025-09-01 04:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12b2d9cc-8241-305a-8980-ebfc5da0501b | -11.32231 | -43.67524 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d96ae2f9-bb20-3166-a5ac-7a2d1e91f315 | -10.76111 | -48.83143 | 2025-09-01 04:10:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfed291d-40f1-3d94-9d41-92d2dbb9d59a | -7.09969 | -44.44961 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c8f081c-c158-35fa-8b54-a1ff4a3f1541 | -6.58115 | -43.71492 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 054dab25-bb5d-3b99-adee-53d2199594a5 | -6.07509 | -43.43318 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f13a4c35-617b-3aca-ac17-1aba97febe2f | -7.97575 | -46.42355 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d76f5ebf-0801-3fd6-b52f-9e449252f848 | -6.11095 | -43.27751 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 050b1f52-ad88-336f-9897-b5928e132443 | -10.75508 | -46.35968 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09c3cf94-b8db-3d7d-89d4-c8f02d7b9ea6 | -7.45849 | -44.83074 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a2cbd94-be06-3166-a603-052107a70aba | -6.57893 | -43.70667 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f9d1ce3-c803-3fc6-a101-fca94032f3c7 | -4.04367 | -48.93826 | 2025-09-01 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README29.md)
