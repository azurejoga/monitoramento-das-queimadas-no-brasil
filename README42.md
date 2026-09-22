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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf8eb412-66f0-37e6-bc87-3eb3e2e74c17 | -18.91559 | -46.84948 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b96d0b39-2af9-36f0-a320-1360883e09a0 | -11.31692 | -54.03765 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b6ff4183-2d4c-309f-816b-8acb58d54b2c | -13.27969 | -51.79242 | 2026-09-22 04:04:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02dded66-756d-3b46-8ffb-a6c7b0990627 | -14.61172 | -41.02924 | 2026-09-22 04:04:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8e0b5f48-6fb7-372b-9e49-37d62b8808a7 | -15.75443 | -43.37531 | 2026-09-22 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ac8b679-282f-330f-a67e-80d069a4a3cd | -13.46328 | -46.90878 | 2026-09-22 04:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67833bda-d09d-3a43-abf5-962f2ad82368 | -19.87062 | -42.63987 | 2026-09-22 04:04:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 870a8112-6340-38aa-8719-bd80fb0571f8 | -11.75234 | -50.81681 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a81a7fc2-d84a-30d6-89d6-dfb7224efd08 | -14.68905 | -45.68174 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b54e805a-6633-3b6a-b3f3-256cdab1d651 | -13.62791 | -42.47844 | 2026-09-22 04:04:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b1a8f2ea-a6db-38aa-8a59-fce03c3e2dbe | -14.7567 | -48.44148 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40e32780-9d00-3e04-a507-8c7fcae18e87 | -15.26279 | -47.60375 | 2026-09-22 04:04:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9ecdb11-3754-3e77-8edc-120e0e4b31f3 | -14.0312 | -40.94296 | 2026-09-22 04:04:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1ef37f0c-69af-37fe-a5c4-831a79e304a0 | -13.92035 | -48.56781 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0f2f361-d09f-3078-84a3-559b68797d17 | -15.44747 | -43.81644 | 2026-09-22 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 955688d4-4d73-38da-818b-567c5b6235fb | -19.40887 | -46.40689 | 2026-09-22 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4059b57-feab-3204-84fb-371d108ae031 | -11.32409 | -54.03916 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a42bf980-bca2-3241-8a35-eac596513d28 | -17.61471 | -42.10833 | 2026-09-22 04:04:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5aa21f8f-d236-3b2b-8bb5-8306b63900ee | -14.17432 | -47.87685 | 2026-09-22 04:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5ef49ca-dec9-32d8-bf05-785f53bced97 | -18.03817 | -50.92664 | 2026-09-22 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0dab60b-34e8-3270-88d2-51faf3323a1d | -13.71671 | -48.78861 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6aa5eec-1516-3435-9df3-184cb34ecc4d | -18.13139 | -39.86125 | 2026-09-22 04:04:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 50700b1f-b24e-3953-bf22-c360cc45904c | -17.09152 | -46.17091 | 2026-09-22 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdbf3ceb-1219-3ab7-919c-d88a612e4998 | -14.67632 | -45.68068 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0fd544e-2008-3735-a159-4f65783f9cb9 | -15.44258 | -48.47287 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9ece182-34a7-3504-8a1e-e573a837df62 | -14.63203 | -45.67203 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b79903c0-7871-3756-9b53-9f235604a4c0 | -15.20316 | -46.33444 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c5a9edd-7eec-30aa-bfac-12db6cb0680e | -14.76535 | -48.44843 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3824c53-485f-359b-9f5f-dd080a9133ad | -14.63138 | -45.67566 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44b569bd-cdc0-3aee-af1a-7f20e30c0b9b | -20.15226 | -41.51727 | 2026-09-22 04:04:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7aab8ee6-785e-3916-b091-0d7a54869825 | -15.60224 | -48.30842 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 736ac0b2-6980-3596-834f-0c3368923419 | -18.76606 | -45.11926 | 2026-09-22 04:04:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff89151a-3742-3d35-af35-d8189fa311ea | -15.62529 | -48.32313 | 2026-09-22 04:04:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5da7d79-8841-390d-8499-09d01bc67ed0 | -16.97458 | -44.88446 | 2026-09-22 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb8a18be-d266-3471-b7f5-5b27d6639619 | -15.60319 | -48.31129 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4345005-e471-30e9-87af-d637913cbe6f | -11.74966 | -50.81415 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f45c2af3-af5a-349b-9d6c-dd90b08da027 | -13.89895 | -48.56744 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ffedd7c-f812-3234-82d0-c3159cc3df87 | -15.4498 | -48.48687 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c18d8b8-88e5-3e21-b81a-cb544369ee47 | -12.79072 | -54.04318 | 2026-09-22 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 760e6c81-f7bb-38cd-bc59-b85d9592c373 | -12.31211 | -50.18657 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c7faa9e-bdeb-3d9e-abb0-006d2c09136d | -15.86046 | -49.89116 | 2026-09-22 04:04:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ccf0993-eaef-3e34-b857-dee371c63f01 | -11.76593 | -50.81049 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a14eaa1d-09fc-333e-82df-9cc864b56a59 | -15.44285 | -48.44578 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9033250-e7f9-38e6-9607-be0f1ed05e9f | -14.6723 | -45.6799 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c05a64a-b94a-3c0c-8971-b9c811d49435 | -18.76973 | -45.11994 | 2026-09-22 04:04:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ade7c855-7e91-31d7-864e-56c1f5b44967 | -19.41172 | -46.41335 | 2026-09-22 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89b46afd-6143-38b7-a294-51ef6012c3b5 | -13.71603 | -48.79212 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0413c05-d204-385c-9542-67f87352e7c8 | -14.13335 | -44.01293 | 2026-09-22 04:04:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4485a675-8bdc-3ef2-acd0-06b90cc4f62f | -18.88807 | -46.83992 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed74cab0-1e21-33da-a19e-9d2a68e01c93 | -13.93013 | -48.57013 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae307ab3-697f-3c94-9bc4-f420e4ab4715 | -15.35667 | -48.10058 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36183b7a-6557-321b-957a-ac6246874ecd | -15.71804 | -42.24372 | 2026-09-22 04:04:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69b73f20-ddad-34cd-9e57-11b3a5b454fd | -19.4156 | -46.41426 | 2026-09-22 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57f0e8e1-0fd3-3c88-90e6-ad2a28594f6d | -13.21374 | -46.93337 | 2026-09-22 04:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88b4b8af-43da-39c3-b9ea-bb7e0f38761d | -12.78923 | -54.05017 | 2026-09-22 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9508063c-7c15-34b9-9606-84b0bc405a01 | -15.74028 | -41.89033 | 2026-09-22 04:04:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb78a179-a9c8-3f54-b779-a9123e40e6b9 | -20.26135 | -41.75028 | 2026-09-22 04:04:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b951f54b-c00e-3200-9a39-f6ca88bd8616 | -13.02176 | -50.60019 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faf9afd5-2413-3dc1-8d4a-7b6068d5c42b | -13.92682 | -47.84748 | 2026-09-22 04:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d63cc8e-8aef-30e4-be4a-ab7788395229 | -13.21289 | -46.93795 | 2026-09-22 04:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 327f204d-9d31-30e0-937f-7ca80a687a37 | -14.68167 | -45.67655 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2bf31f2-bebc-3b26-8772-75bedf307375 | -13.32589 | -51.29174 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6771e68c-7bff-30f4-abd7-f26f7639c327 | -15.35933 | -48.11185 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4985ca80-7a97-338f-987a-c0b8a435998d | -15.44492 | -48.43498 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 517f0f05-f9e6-355a-9c72-d8b75235a35e | -15.62161 | -48.31694 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15d3b97b-70f2-3714-950f-7e8d1949006a | -14.66892 | -45.67545 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 363306a7-35b5-3945-8f45-fd4910e6cc80 | -21.60031 | -41.2151 | 2026-09-22 04:06:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f471251f-28ba-36be-8c94-96ff550bbcaa | -21.60089 | -41.21134 | 2026-09-22 04:06:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d38c6acf-2bf7-3f1c-b147-833accb387d4 | -21.59122 | -41.25211 | 2026-09-22 04:06:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f09a920a-ea2f-3e97-aa77-bb37a17a2da3 | -20.85195 | -49.06954 | 2026-09-22 04:06:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 121ff27e-dce4-3be0-973b-75abff4e2a8e | -10.6094 | -53.9902 | 2026-09-22 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 220.3 |
| 94823b94-2e8f-3758-a949-0dda32dd7be3 | -6.467 | -59.9902 | 2026-09-22 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0fc61448-f33b-338b-9ab1-355969a3afe1 | -11.156 | -51.1051 | 2026-09-22 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 0972e87f-6418-3549-9bb1-bcd1af884af2 | -7.5889 | -57.6757 | 2026-09-22 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7decec6a-77da-38de-ac2c-c55346719737 | -6.633 | -59.9457 | 2026-09-22 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d30ac09c-d9b3-341b-9670-381b7f609a1e | -10.5906 | -53.9918 | 2026-09-22 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 792a5444-ad85-3a70-ad3d-bbc986e22e76 | -10.6283 | -53.9885 | 2026-09-22 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7536640c-6480-3561-961c-3188bc33a914 | -11.1747 | -51.1243 | 2026-09-22 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| b67ae592-912f-3ad3-be6d-36917006767a | -6.6515 | -59.9258 | 2026-09-22 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 275.3 |
| 929b23fa-62ce-3863-a92b-8ee99e136849 | -6.6331 | -59.9265 | 2026-09-22 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 226.9 |
| 56f02f79-9feb-31aa-b23b-a5241c9f9fde | -11.1557 | -51.1263 | 2026-09-22 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fafd72ed-2f9c-3460-adb6-0849c926a83e | -6.6146 | -59.9272 | 2026-09-22 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 146.0 |
| e0b2ab17-cadb-3af9-8a6a-75056aa0ee97 | -10.6097 | -53.9697 | 2026-09-22 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| b5d58918-a67e-32fa-9915-19e4f81c5bc4 | -10.5908 | -53.9713 | 2026-09-22 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d203c0a9-4e5b-3b4d-9cad-807832693407 | -11.175 | -51.1031 | 2026-09-22 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b06e8b44-1662-35d5-90f9-5abb6de01a0f | -6.6148 | -59.908 | 2026-09-22 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 20114e5b-006f-3629-bbbb-401c29c33007 | -6.6514 | -59.945 | 2026-09-22 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 546694d6-2362-3c32-aff1-719d86af8551 | -9.5594 | -66.0359 | 2026-09-22 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 18bbe921-11d5-3442-bfef-c80421ea9461 | -6.6331 | -59.9265 | 2026-09-22 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 244.5 |
| 8d33d579-cfdb-3702-9560-161e992dbd1e | -6.6515 | -59.9258 | 2026-09-22 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 214.0 |
| 50996b11-fd7c-3100-af77-fff868ea1888 | -6.6146 | -59.9272 | 2026-09-22 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ce120193-4485-324d-935e-579126715c24 | -6.6148 | -59.908 | 2026-09-22 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d5fc86b8-a00c-336f-91ee-da969ca3f3ae | -7.5889 | -57.6757 | 2026-09-22 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 639f4685-4e59-3dc3-a95c-e0657d4718b9 | -6.6516 | -59.9066 | 2026-09-22 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 4b41e5e9-542b-3f9c-b0f3-3dba9faee367 | -6.6332 | -59.9073 | 2026-09-22 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 8bd99d60-f518-3aba-94d7-561be1a2ebfd | -9.5594 | -66.0359 | 2026-09-22 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 56c4f8ab-0108-384c-9dc7-293c426d43f4 | -2.53994 | -48.15906 | 2026-09-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ab64641-d031-36ee-a4af-401365d9d526 | 0.16919 | -60.49249 | 2026-09-22 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cd89002c-bb04-3fe6-b8fc-e624300d51cd | -2.32524 | -49.20296 | 2026-09-22 04:44:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 096466a2-e917-3d7c-998e-3d98ba8522ae | -1.41555 | -55.16071 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README43.md)
