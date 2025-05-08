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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85c42620-6e4e-3e92-ba1d-bbd5714ecf2b | -8.0889 | -43.1196 | 2025-05-08 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| df2c469f-8332-378b-9b5a-058f6d42feb1 | -13.4901 | -52.9715 | 2025-05-08 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e3f154f5-4ae9-3b63-a2fc-63a97da66c39 | -13.5093 | -52.9692 | 2025-05-08 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 3ee6ad77-cc48-3f77-a0f6-851602e8f665 | -14.6414 | -45.1263 | 2025-05-08 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 76a65491-8ff2-3109-a5b4-40b852220483 | -8.07 | -43.1216 | 2025-05-08 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| ecf7ba7d-9297-3a1e-81fc-05dbc3a62f8d | -15.8208 | -46.5763 | 2025-05-08 00:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 3d9cdc04-d9b9-32da-bc1e-a6b6f3afb046 | -14.0964 | -44.2397 | 2025-05-08 00:00:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3aff5dd0-2367-31e8-bf4e-8bc82c9aa634 | -15.8405 | -46.5726 | 2025-05-08 00:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 7a0da144-0360-3b08-88ca-25624c1fbcdb | -20.75114 | -43.65414 | 2025-05-08 00:09:00 | TERRA_M-M | ITAVERAVA | MINAS GERAIS | Brasil | 3133907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| f1749b60-20d1-3727-b104-167c3ef24157 | -20.7529 | -43.67016 | 2025-05-08 00:09:00 | TERRA_M-M | SANTANA DOS MONTES | MINAS GERAIS | Brasil | 3159100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 1af3915a-f240-3ec0-97c0-430879114142 | -8.0889 | -43.1196 | 2025-05-08 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 78c37051-5cfe-3b76-97c5-53ccfab6b766 | -14.0964 | -44.2397 | 2025-05-08 00:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 36707df4-0adc-376c-8a5d-105689c23c69 | -13.5093 | -52.9692 | 2025-05-08 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 15b3f71a-dfa7-3093-aff5-9bcd834e9c54 | -14.6414 | -45.1263 | 2025-05-08 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 1cd9dca1-ec99-37ed-b3b1-53a06e0255d9 | -15.8208 | -46.5763 | 2025-05-08 00:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 19da3030-cf0a-356f-9d7a-bcecec0b9836 | -15.8405 | -46.5726 | 2025-05-08 00:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 093bce89-2f9f-3e9e-a520-ca05bae8aeb4 | -13.4901 | -52.9715 | 2025-05-08 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| bdbff20b-5837-3859-972b-3ad5743b97db | -8.07 | -43.1216 | 2025-05-08 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 16fad24c-cf48-3b05-8b5e-9deac7aab401 | -15.82716 | -46.56897 | 2025-05-08 00:11:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 2343bd15-208f-3f06-a30d-f599b38e571d | -14.09892 | -44.23487 | 2025-05-08 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f0b14e79-6176-3ea0-bfc5-4f5866910220 | -14.1038 | -44.24206 | 2025-05-08 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f58b1b38-18be-3965-9fd6-ae88f4598127 | -14.10215 | -44.22816 | 2025-05-08 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 97d0d18c-82ff-3c1a-85bc-dc3c91977f52 | -14.09299 | -44.24331 | 2025-05-08 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6728e338-cdaf-3966-b4e7-f479b77528d9 | -15.82551 | -46.58508 | 2025-05-08 00:11:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| d6e7a3da-62b7-368b-bfeb-d4daec9b8e62 | -14.10066 | -44.24868 | 2025-05-08 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 76a03dd5-5cee-37d1-ab2e-58283a31c6ac | -15.51287 | -41.67268 | 2025-05-08 00:11:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 2f3f8466-e9bc-308a-abcf-6bf7db5e1f94 | -15.82318 | -46.56282 | 2025-05-08 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 47.2 |
| e3d4ab6c-aaed-3fdc-88bf-58db690aa340 | -15.83889 | -46.58387 | 2025-05-08 00:11:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| dd6dea15-df4b-3e0d-a244-955afbf822e1 | -14.63149 | -45.12498 | 2025-05-08 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| ec7cbd3c-82d7-3944-b42c-76a59bfa30dc | -14.6451 | -45.13993 | 2025-05-08 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| db53367e-1ea5-3468-9c4d-30dbdddaaa06 | -14.64313 | -45.12352 | 2025-05-08 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| b15f7bf9-3666-381c-a78d-72b9b79b685f | -15.82967 | -46.59134 | 2025-05-08 00:11:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 01bbec9d-7321-35ea-a91e-e4c746691f60 | -14.63344 | -45.1414 | 2025-05-08 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5bfdb2c1-9a91-32b1-a9f9-3627a8c88598 | -10.67174 | -44.38534 | 2025-05-08 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 408e361a-972a-36f8-9d75-884ede999dcb | -10.7145 | -42.3143 | 2025-05-08 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 33a1ec60-80cd-3891-803c-3c4e82b12037 | -8.07955 | -43.12277 | 2025-05-08 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 90f3aed2-07ee-3237-a2c3-87d649002bed | -6.97899 | -42.80445 | 2025-05-08 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| baa804ea-e744-36e0-9428-d10d86c19e42 | -9.6114 | -37.04097 | 2025-05-08 00:13:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 983df89d-179e-3052-b636-b4cf68fc1b71 | -6.97773 | -42.79517 | 2025-05-08 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 79af41ee-1bfa-3fb8-9f81-9e1b96a414cf | -9.60907 | -37.0478 | 2025-05-08 00:13:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6761a9b2-4bf2-35cd-9c5d-2d5fc242fa82 | -7.07036 | -44.38822 | 2025-05-08 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3bb550bf-559b-35c6-beb8-cf6290979e25 | -6.83915 | -42.79229 | 2025-05-08 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5394daf9-65c9-3ad8-bfc5-12aae36cb6fa | -8.07198 | -43.12011 | 2025-05-08 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 7b883404-1810-3072-bab7-984e389220ef | -10.7158 | -42.32393 | 2025-05-08 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 2f34ae5b-6b30-3b62-a99c-421e8a6c7fb1 | -6.70266 | -42.13168 | 2025-05-08 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 086ae81b-bc27-3455-80be-082b2f2b8f37 | -8.08085 | -43.13258 | 2025-05-08 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| e97ba4eb-ba08-3c84-97ab-a4210e5e6142 | -6.70389 | -42.14062 | 2025-05-08 00:13:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 76fd26bf-bc06-303b-abb0-1ad25e6e0121 | -10.72496 | -42.32266 | 2025-05-08 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 48.7 |
| b074667e-2107-3bd3-9c95-00e914e1ef43 | -5.79124 | -43.61724 | 2025-05-08 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d8629be5-d934-374a-9574-0c56b493b6bf | -5.06764 | -37.67326 | 2025-05-08 00:13:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 3fec5edb-d356-3a3b-ab28-5c09dae743a2 | -6.95995 | -47.92455 | 2025-05-08 00:13:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 65560374-f7df-3db1-bf5d-8ef7984e745e | -10.98769 | -44.45561 | 2025-05-08 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c9c2583b-cb49-38e4-9d7d-75c43d2e4261 | -10.98604 | -44.44284 | 2025-05-08 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b9f36ba5-1b8a-301b-9866-cad462c30e9f | -4.89869 | -37.52511 | 2025-05-08 00:13:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3d1d7dc8-a8c8-3bb0-a3d1-44653851ec53 | -8.07332 | -43.12992 | 2025-05-08 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| af4259d2-eaca-3057-91ca-581ac4c44417 | -8.07826 | -43.11298 | 2025-05-08 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 7378ab55-1e5f-38a3-833e-08875aab5dec | -6.69379 | -42.13293 | 2025-05-08 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 7983cfe5-68f5-32db-89fc-afefad292316 | -6.69502 | -42.14186 | 2025-05-08 00:13:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 68f8d2e7-bc54-3caf-a35a-4ddcd513c0f5 | -6.9587 | -47.91909 | 2025-05-08 00:13:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8be03cad-de59-303d-b37a-76c297e80cfd | -5.16334 | -45.10393 | 2025-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 79458a6b-ca9c-3d62-8d79-42076ec35776 | -4.00056 | -43.25119 | 2025-05-08 00:16:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5dad340d-3522-3b3e-be1b-d0657f854686 | -5.17338 | -45.1026 | 2025-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ed22e1ff-bc86-32f6-bd47-5ce8b94e01dd | -5.1649 | -45.11559 | 2025-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8143e149-1d95-34ed-a16a-382f44b4e49f | -4.89625 | -37.53196 | 2025-05-08 00:16:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 635dc1c0-910f-3464-9676-18862cf54190 | -8.0755 | -43.133301 | 2025-05-08 00:17:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f946a802-e23e-3c59-836a-73b95963282a | -13.0463 | -53.694 | 2025-05-08 00:17:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 862f05d1-0436-3dc2-83db-8277fb3a7aa8 | -14.1015 | -44.225399 | 2025-05-08 00:17:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e77615e6-1260-30f9-a14d-debbf2e627a5 | -10.9943 | -44.447498 | 2025-05-08 00:17:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4c9d729-35da-3363-95ed-f7d044a492a6 | -8.0829 | -43.120899 | 2025-05-08 00:17:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d642767a-f4c1-3c47-b121-6d7f3ce51d0a | -10.7319 | -42.329102 | 2025-05-08 00:17:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 01c858bd-d61e-3a98-834a-00a91b5c2d36 | -13.5028 | -52.968498 | 2025-05-08 00:17:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb40f3e2-d0b2-3fe5-b44b-7f4527fbf47f | -11.3909 | -52.9333 | 2025-05-08 00:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7450dd47-7b9c-3e98-954e-bd0f07be2f2e | -8.0731 | -43.123199 | 2025-05-08 00:17:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 90f15f5a-75b3-36bc-b903-447a71f160ad | -9.3231 | -49.483299 | 2025-05-08 00:17:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b51ed876-3714-3429-b84c-782b3c4cf5d0 | -20.761101 | -43.647202 | 2025-05-08 00:17:00 | METOP-B | ITAVERAVA | MINAS GERAIS | Brasil | 3133907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b069de77-3025-314e-93a8-9809a4c0db5c | -11.3884 | -52.921398 | 2025-05-08 00:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e90e861-c3b3-3717-8fdf-2b63eb687fb1 | -10.7294 | -42.318699 | 2025-05-08 00:17:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7fc59568-3ad6-3363-be72-6b8337499e9f | -6.6939 | -42.132 | 2025-05-08 00:17:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d5f7063-18da-3192-b1ac-2caf28ee614b | -13.3669 | -54.250702 | 2025-05-08 00:17:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67bfaaee-8b33-34eb-8c58-afbd9d25a8de | -6.6968 | -42.144199 | 2025-05-08 00:17:00 | METOP-B | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5edaf940-b7dc-3f0c-b00d-e29270d09982 | -5.1665 | -45.1124 | 2025-05-08 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18f9aeb0-77b1-3cd3-a4d2-5a36ecabab50 | -9.3215 | -49.475899 | 2025-05-08 00:17:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea1842d8-085e-3096-aa9d-99232ec4de0f | -20.070801 | -49.353802 | 2025-05-08 00:17:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bada9e86-03b3-3067-98b6-a75a37d60cb9 | -13.5003 | -52.955502 | 2025-05-08 00:17:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 410e050d-10f1-32b4-ace3-9b686b71d849 | -8.0853 | -43.131001 | 2025-05-08 00:17:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2f2789a2-431f-38bf-be30-ed5c3b722419 | -10.9925 | -44.439499 | 2025-05-08 00:17:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84aa0d83-83db-36f3-bd9f-741d39955007 | -14.6396 | -45.135399 | 2025-05-08 00:17:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd9e88a5-0766-372f-bc16-37cecb2cc9c8 | -14.6379 | -45.128101 | 2025-05-08 00:17:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8311211-ba47-30da-80b1-ecaae1479c7a | -13.0491 | -53.708199 | 2025-05-08 00:17:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 697346ce-dd6c-3aee-8f64-6c2febf9fe49 | -6.968 | -47.908501 | 2025-05-08 00:17:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf56c39f-47b5-3fbe-99c4-0d6d83df5378 | -10.6691 | -44.380299 | 2025-05-08 00:17:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12cb3e30-08a3-3399-9895-150d75429829 | -18.4196 | -54.6833 | 2025-05-08 00:17:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bb759043-fa78-3acd-a181-882cbd1bdf6a | -5.1743 | -45.1017 | 2025-05-08 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 851d4bdb-d467-3eb3-b1ac-3a6222d2ad5b | -14.6493 | -45.133099 | 2025-05-08 00:17:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3600f8ab-1828-319b-bea7-a98d0fb5091c | -13.3766 | -54.248699 | 2025-05-08 00:17:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39731667-d975-3d92-ae07-50175dad328d | -8.0707 | -43.113098 | 2025-05-08 00:17:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bf475893-58a4-38b7-a2d7-a5e7dd6e86cf | -13.488 | -52.944599 | 2025-05-08 00:17:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f5cfd4a-5d83-3f59-9f5f-8d426d8d7f8c | -14.1033 | -44.233101 | 2025-05-08 00:17:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0b39997-184f-3305-b5fa-1d4e2cc17888 | -8.1714 | -46.710999 | 2025-05-08 00:17:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48ba0bbd-63dd-3702-a7c5-5f054d40789a | -14.6363 | -45.1208 | 2025-05-08 00:17:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
