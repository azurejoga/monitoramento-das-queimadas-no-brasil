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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef60f263-020b-333f-a6fc-148ffd9de1bc | -13.4767 | -48.581501 | 2024-09-28 01:07:21 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 034a2627-5abb-3642-83bd-8862c4920ee2 | -13.467 | -48.5839 | 2024-09-28 01:07:22 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1208d4d5-6b58-3784-b987-fd3998927696 | -13.4551 | -48.577599 | 2024-09-28 01:07:22 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6293d5ee-2c66-3838-a503-c66e38cd676b | -13.4572 | -48.5863 | 2024-09-28 01:07:22 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c8a8915-23ce-3c23-8270-e145a743ff3b | -13.1696 | -48.508598 | 2024-09-28 01:07:26 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e139ae4-fc8a-36e5-bec7-f49f5fabcd83 | -13.1599 | -48.511101 | 2024-09-28 01:07:26 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3c561737-7e62-3c64-a25a-ef0da39d19b3 | -13.6947 | -51.088902 | 2024-09-28 01:07:27 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32e87ab6-cda8-3d7e-8f96-9e48947328cb | -13.6358 | -51.462502 | 2024-09-28 01:07:30 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c002deac-d55b-3cfc-b14a-326571cef33d | -13.6375 | -51.469601 | 2024-09-28 01:07:30 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84beb5e8-bfe1-3d61-9454-a713ad60e9ba | -13.6391 | -51.476601 | 2024-09-28 01:07:30 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b89a0130-1399-38fc-bcbc-a094b0f7a7f1 | -13.6277 | -51.471901 | 2024-09-28 01:07:30 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 597b04eb-4584-30c2-af54-897d3422896d | -13.6293 | -51.478901 | 2024-09-28 01:07:30 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 903ba34e-17c6-3c22-aa42-bd7bdce5b450 | -14.8916 | -57.971802 | 2024-09-28 01:07:32 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c302eb6-fc1c-31af-b9eb-cf4d880fc876 | -13.2267 | -51.2523 | 2024-09-28 01:07:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 038e5942-0676-3bae-9545-9cc99000a7c9 | -13.2283 | -51.259399 | 2024-09-28 01:07:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3617e704-c7d4-3138-88cc-fd6073c187a3 | -13.968 | -54.588001 | 2024-09-28 01:07:36 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9a2dcb-d4c5-3adb-bc54-b812e130d9bf | -13.9697 | -54.596001 | 2024-09-28 01:07:36 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29b0f7f7-eb0d-3c08-a022-61b7cb6d36b8 | -12.1704 | -47.969898 | 2024-09-28 01:07:40 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14ff3002-7d34-3b75-91a2-276565bc6d9c | -12.1727 | -47.979698 | 2024-09-28 01:07:40 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8867ab6-cdbc-3a0f-b2c6-d0507713749f | -12.534 | -50.622299 | 2024-09-28 01:07:44 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbff94bc-0e0f-3355-8afc-2b4b2678e05f | -12.5357 | -50.6297 | 2024-09-28 01:07:44 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dab6e414-6923-3a51-b7fd-aa40993c28e1 | -10.987 | -44.407902 | 2024-09-28 01:07:45 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f39c9be-df0a-3e99-bd87-abf4655ff97d | -10.9914 | -44.425098 | 2024-09-28 01:07:45 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c220407c-bc17-3449-9251-063835a16c0e | -10.9958 | -44.442101 | 2024-09-28 01:07:45 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef7e7231-50e1-3101-9646-17ce138ad02b | -12.526 | -50.632 | 2024-09-28 01:07:45 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b110839-ddaf-34da-b460-9749dd12e7a9 | -12.5277 | -50.6394 | 2024-09-28 01:07:45 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 051a07cc-a5b5-371a-bfe8-1abed8eb35d5 | -12.3813 | -50.454601 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 253fe5f6-2dff-3316-9225-cdfc97e67815 | -12.3831 | -50.462101 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6785654-6a28-3fdb-a72f-276581cf5071 | -12.3848 | -50.469601 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1d71982-0158-3331-9d12-dafed950319d | -12.3866 | -50.4771 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40b77791-43ad-3e54-8402-3b1a943b3f51 | -12.3883 | -50.484501 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59d4f4e4-773d-30da-9a09-f3be7754b296 | -12.3715 | -50.457001 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4eda00-067a-3d89-a9f5-8ad1477431bf | -12.3733 | -50.4645 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53d3c27a-60ab-30bd-b19a-7cc83ef61eae | -12.375 | -50.472 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea42668d-2562-3dd2-bc3c-650059bba965 | -12.3768 | -50.479401 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebfb8108-749f-3898-a26f-a9abcb4abd4f | -12.3785 | -50.4869 | 2024-09-28 01:07:46 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87ac7aaf-cbd5-304a-9389-4ece3ccc8e4a | -12.36 | -50.451801 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 454260b6-1039-32f8-b364-86c5155d79c9 | -12.3617 | -50.459301 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b38570d5-a309-3ef1-921f-aef8e7f84c54 | -12.3635 | -50.466801 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a36a4e36-04b3-36cb-bd90-38dd80be1b70 | -12.367 | -50.4818 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b02285b-dd53-35ca-82a5-40470fc1c797 | -12.3687 | -50.489201 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5508dd7c-c480-3237-b78a-b50ad05ef6b3 | -12.3449 | -50.431599 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 053e1d4f-3b95-322d-8cca-f611c828f986 | -12.3467 | -50.439098 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e864fba6-5807-3c0d-8f97-f0a17d4847a4 | -12.3484 | -50.446602 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d4e1bb3-97e2-3c3b-a9f2-1f89d00e2b56 | -12.3502 | -50.454102 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb38372a-b8a7-30f6-91a8-1d4dc23ae6b8 | -12.3351 | -50.433998 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd13e99-1fc1-3d07-81fe-d8707bca48ab | -12.3369 | -50.441502 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e45f41d-aafb-3859-bf1d-bd3e2af83da0 | -12.3386 | -50.449001 | 2024-09-28 01:07:47 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84d7836d-c95c-3d72-aaa0-426583dce2aa | -12.3907 | -50.672001 | 2024-09-28 01:07:47 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0680e159-409a-3ef0-92fb-0956c676a3ee | -12.3924 | -50.679401 | 2024-09-28 01:07:47 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83175958-bb12-36b9-a0ea-64ea0ac622db | -12.3941 | -50.686798 | 2024-09-28 01:07:47 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 649629c5-c981-3a2c-8d00-5fcbf3478419 | -11.1096 | -45.575001 | 2024-09-28 01:07:48 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17758661-4213-3079-9d0d-e52ddaf9c7f1 | -11.0474 | -45.696499 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5740842-12eb-3c81-845c-da90686a2748 | -11.051 | -45.710499 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebd1a23-afff-30cd-b792-25b11af22080 | -11.0377 | -45.699001 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9eda9b4a-4747-3164-8e4a-dc7932c341e6 | -11.0413 | -45.713001 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ca9b62b-0d3d-3967-ad3d-b0edfa6c4252 | -11.0448 | -45.727001 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0ed6d24-4b5b-37b5-aef4-3deebd5ea969 | -11.0245 | -45.6875 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57717043-0bf0-3847-8463-0eee6d0e1d83 | -11.028 | -45.7015 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b90d051d-1ff2-3d09-aea8-7ce560fc9f9b | -11.0316 | -45.7155 | 2024-09-28 01:07:49 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be7fc14a-50af-30fd-ad7f-70af304c06de | -12.2417 | -50.652901 | 2024-09-28 01:07:49 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7019c676-38d1-38c2-b55a-4c5d07ffa529 | -12.2435 | -50.660301 | 2024-09-28 01:07:49 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87fd2005-187b-3f7a-a5f7-f5fda888aa1a | -11.0148 | -45.689999 | 2024-09-28 01:07:50 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72fd11ea-f798-3b5a-8bcf-73f841e501c2 | -11.0183 | -45.703999 | 2024-09-28 01:07:50 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb8bda5-391b-3985-ae99-4f9f76ce230b | -10.877 | -45.512501 | 2024-09-28 01:07:51 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d6441d9-4d4d-38d7-bf53-1dfd4f02a851 | -10.8673 | -45.514999 | 2024-09-28 01:07:51 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e3515d9-64c2-3550-a91c-177f997b5365 | -12.866 | -54.004101 | 2024-09-28 01:07:51 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee0a290c-0bf5-381e-a2dc-0efeeb388dc9 | -12.8676 | -54.011501 | 2024-09-28 01:07:51 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38d7c025-e7cf-3571-a607-13a0b18ce74e | -10.8552 | -45.548901 | 2024-09-28 01:07:52 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a71b59db-f39e-3c10-91cf-0db91fc0263f | -12.8546 | -53.998901 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09a241ec-e6fb-374c-9710-ba270be1012e | -12.8562 | -54.006302 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc7c8797-2b64-3fe8-bcb5-afa863bec611 | -12.8578 | -54.013699 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af86708a-ac51-3deb-981c-985066dc61ef | -12.8595 | -54.021099 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00a83263-ee94-338d-83f5-83000df6f74f | -12.8448 | -54.001099 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54346da4-6340-3634-b32e-c700d957c739 | -12.8464 | -54.008499 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23800c40-1561-3860-b5da-86d1b4e36926 | -11.8328 | -49.617199 | 2024-09-28 01:07:52 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97d5f577-37f1-3d2e-a9d6-d93fed2392d9 | -11.8347 | -49.625301 | 2024-09-28 01:07:52 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f43646d-41f3-37fa-b31b-fd9e9ae83446 | -12.8351 | -54.0033 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c412b533-3afb-356d-abd1-63017087eb33 | -12.8367 | -54.0107 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fac77c1-a760-3e43-b2a5-ce24a78edc7a | -11.8249 | -49.627701 | 2024-09-28 01:07:52 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af95dc97-feac-36cf-bd1e-03fda20a3931 | -12.8236 | -53.998001 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 131204c4-dcd9-3800-bd17-805ed2dc2aed | -12.8253 | -54.005501 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb7342c5-af1e-34a5-9cfe-a271976bb9d7 | -12.8269 | -54.012901 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b0cb879-bbde-38b7-84d7-3e663c3612f8 | -12.8106 | -53.985401 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0d1cacb-a609-37da-8c44-8641751f4149 | -12.8122 | -53.992802 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 075ada03-4840-3944-8eaa-3b1dc1d31727 | -12.8138 | -54.000198 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| faa948a6-1765-3db1-ab66-875199ae4b39 | -12.8155 | -54.007702 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cbb33ef-4117-30d3-bab2-42266fc735af | -12.8171 | -54.015099 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad600a1-41e7-33be-b962-6a65a790ccab | -12.8008 | -53.987598 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5752e086-0d56-3174-af18-badbee0dcea3 | -12.8024 | -53.994999 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4497cf12-f318-36ae-85e0-4769faacbfe3 | -12.804 | -54.002399 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b95d6681-15a4-329d-8263-76e19d6ae80d | -12.8057 | -54.009899 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 552735c2-d550-3db6-b9b6-abed92693fc7 | -12.8073 | -54.0173 | 2024-09-28 01:07:52 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3adbf9e3-1070-3db1-94c0-5c9cdb236115 | -13.4925 | -57.242001 | 2024-09-28 01:07:52 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfd1a81e-45e9-338d-9171-91930fd1cdf6 | -13.4947 | -57.2528 | 2024-09-28 01:07:52 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f32020ca-f9fc-3cbd-ae08-d5d6468fe4da | -10.2737 | -43.566002 | 2024-09-28 01:07:53 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de23bf18-9ebe-3d1b-a4d7-1a14e94da516 | -10.2641 | -43.5686 | 2024-09-28 01:07:53 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66e49f7b-38df-3054-85a0-30ea042aa243 | -12.791 | -53.989799 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e212b561-9f21-318c-b2d6-38128d3e3b01 | -12.7926 | -53.9972 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22f6f3f6-8afe-3ec2-a2b5-dc6d4f42aa10 | -12.7942 | -54.004601 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
