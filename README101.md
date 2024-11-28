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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dd0f986-b5f0-3fc7-971e-f4f77a1ad092 | -6.16743 | -42.62011 | 2024-11-28 12:33:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 6bc12d1e-906a-33ed-a026-88d36fe1e71a | -7.42428 | -42.31796 | 2024-11-28 12:33:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 9abc1019-5580-3895-b343-3f59fa9c17c8 | -4.15825 | -43.81536 | 2024-11-28 12:33:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 728d04d7-bd37-346d-90aa-7637986fd277 | -7.63193 | -47.15591 | 2024-11-28 12:33:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 84bbd682-d739-319c-8085-d3b9d1cb1e9c | -6.18455 | -42.04054 | 2024-11-28 12:33:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 4a528a91-5b20-30f7-901f-5104f264d795 | -4.1544 | -43.8425 | 2024-11-28 12:33:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 308361bf-f165-33c1-aa72-99d76cc50262 | -3.51551 | -41.66693 | 2024-11-28 12:33:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 40a78fc3-e818-3993-94e3-da6a17653cb3 | -8.13125 | -44.47271 | 2024-11-28 12:33:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| de626089-26b5-3d4b-9095-fdf585cd3c91 | -3.55786 | -40.72209 | 2024-11-28 12:33:00 | TERRA_M-T | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 5374dd0e-3f65-363d-82ea-1e9bf1063544 | -2.41094 | -45.24236 | 2024-11-28 12:33:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 223f6dfd-ce54-3c0a-af5d-823eafe33b38 | -3.30588 | -41.98189 | 2024-11-28 12:33:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 3d979cfd-0bb6-3250-8a1f-e351aec310f0 | -3.33047 | -45.51575 | 2024-11-28 12:33:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| c9f25703-e978-3713-906f-cb2ad26c7f01 | -3.23935 | -54.23962 | 2024-11-28 12:33:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| a06d7974-45c4-35ea-9186-cbd5eec1bea2 | -6.16466 | -42.61373 | 2024-11-28 12:33:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 91bd5844-0050-3d27-bda8-881e53e397b7 | -3.42102 | -42.05325 | 2024-11-28 12:33:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 3597eeb3-fcba-375a-a2b5-69d2ac8643c1 | -3.5283 | -45.11326 | 2024-11-28 12:33:00 | TERRA_M-T | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 8ef6d0cd-4178-37d1-bf47-344aebd8cf62 | -4.43423 | -46.42877 | 2024-11-28 12:33:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 2750ec8d-38df-3271-9cf0-499ad6477865 | -7.77131 | -37.94054 | 2024-11-28 12:33:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 31.5 |
| e0d64c5e-f103-38c1-900c-18beab6ab3c1 | -4.94578 | -44.68182 | 2024-11-28 12:33:00 | TERRA_M-T | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 40478e2a-16d0-3d59-9dc3-b79cb58619dc | -3.34996 | -50.51617 | 2024-11-28 12:33:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ac603f3c-9f46-351f-a943-56e5bcbb2115 | -5.00426 | -43.83075 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 02f761ee-1e87-3363-9051-f5a5eb9b434f | -6.17852 | -42.61084 | 2024-11-28 12:33:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 5dbb7bf6-c38f-390e-9f36-69c659d9f6c0 | -5.97601 | -45.35635 | 2024-11-28 12:33:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 2483c022-65c8-34e1-a36e-7952b67c75b9 | -7.91968 | -38.09511 | 2024-11-28 12:33:00 | TERRA_M-T | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 38.9 |
| 27fa75f1-30c5-3df1-b0af-130ab9851220 | -4.43284 | -46.43813 | 2024-11-28 12:33:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9c1c8b1b-0107-32e6-8921-4cfe479b0142 | -3.96079 | -48.08611 | 2024-11-28 12:33:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 105ec714-d37b-305a-b030-2d16860b4c21 | -2.53318 | -47.3335 | 2024-11-28 12:33:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 084b936b-51ea-3d30-ac6d-a7cb1d4ca931 | -4.41531 | -46.11813 | 2024-11-28 12:33:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a8bcdb8b-33de-3e7e-a73f-da3797ac7169 | -6.48565 | -42.81114 | 2024-11-28 12:33:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 0d0a5987-c25f-322a-b545-c8f5c5463a17 | -6.16888 | -42.60944 | 2024-11-28 12:33:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 4dc5fc69-48b7-3a74-bb62-49b60e5137ed | -5.35475 | -43.96027 | 2024-11-28 12:33:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ab18105a-07d2-3b8e-b518-84c03bf16a3b | -6.67472 | -44.66121 | 2024-11-28 12:33:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1157fb46-36ac-3994-bcad-28703fd03daa | -3.84276 | -42.78223 | 2024-11-28 12:33:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac00ad5e-3528-3a6a-ad1a-e2ed9ae001e3 | -7.80381 | -40.49682 | 2024-11-28 12:33:00 | TERRA_M-T | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 37.5 |
| a9007818-cb5d-3b8f-b316-b66e3938e814 | -6.83233 | -44.39524 | 2024-11-28 12:33:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db895343-e283-33a3-9d5e-c88e05cb09cc | -7.9228 | -38.07043 | 2024-11-28 12:33:00 | TERRA_M-T | CALUMBI | PERNAMBUCO | Brasil | 2603405 | 26 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 469f1672-3f1c-3feb-a583-bd1aa62157cc | -6.2786 | -48.13775 | 2024-11-28 12:33:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f60be7e8-808b-3a18-aa9e-24a63fecad40 | -3.45433 | -44.59791 | 2024-11-28 12:33:00 | TERRA_M-T | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c02ab1a3-ff25-354d-b93a-5f7ec36ae0ae | -6.21632 | -43.27935 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 87bbc515-b438-332b-a6e5-7da650b0ec3a | -2.35318 | -46.1435 | 2024-11-28 12:33:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| da8dab62-d3d3-3ff6-a13b-fb0be57b4af8 | -6.31847 | -43.40955 | 2024-11-28 12:33:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fc6eb98f-1c01-359c-a75b-abfaa212c60d | -6.50368 | -41.48725 | 2024-11-28 12:33:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 05aac42d-4a59-3215-8222-2ec79d4a1c31 | -9.18605 | -43.39739 | 2024-11-28 12:36:00 | TERRA_M-T | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 00cfd81f-65a0-372f-b527-2e9a59af0613 | -9.1739 | -44.72438 | 2024-11-28 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 53e2a26b-1ed4-334d-bd4e-d8b499d57beb | -8.29373 | -49.05824 | 2024-11-28 12:36:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 4a66cf07-0d30-3733-892a-43abd19acb99 | -10.26959 | -43.58095 | 2024-11-28 12:36:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0ba94767-93e6-32fd-baa0-14020e9fb9c2 | -9.19112 | -43.39308 | 2024-11-28 12:36:00 | TERRA_M-T | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 19fac4c2-a1e0-345c-bc3c-39cff3616418 | -8.91985 | -44.56614 | 2024-11-28 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7788c973-a0d6-31c1-97b4-27ee03ca81c7 | -8.29552 | -49.04667 | 2024-11-28 12:36:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 9d6ad150-fedc-33e0-9b6a-24b4bbcc063b | -9.17259 | -44.73359 | 2024-11-28 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 846fafc0-5add-359d-a7c4-3edb4ff71d5c | -10.57102 | -36.8718 | 2024-11-28 12:36:00 | TERRA_M-T | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 45.2 |
| e35e4575-9ecf-3c8f-8299-14a8c13f2cd6 | -9.18289 | -44.72565 | 2024-11-28 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| cf5d3da8-4ca4-381c-8025-967d340c4725 | -8.47464 | -47.81163 | 2024-11-28 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 26b212d7-7106-38e4-8c66-6651ce0b4851 | -9.18157 | -44.73488 | 2024-11-28 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| f8a3005c-6833-3a3e-8f62-3f4fd187c8d8 | -17.25679 | -43.65135 | 2024-11-28 12:38:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a24c2494-b028-366d-971a-491589bf8e96 | -17.64519 | -44.46276 | 2024-11-28 12:38:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 629e8a4d-8317-3a0e-a44b-7c685ece7985 | -13.92752 | -45.85411 | 2024-11-28 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| aa03c352-2860-3d09-8457-cf886ad81541 | -18.51293 | -51.35241 | 2024-11-28 12:38:00 | TERRA_M-T | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d3fd90cf-00cb-3289-92f3-67d7343167f2 | -19.79232 | -42.13637 | 2024-11-28 12:38:00 | TERRA_M-T | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 61c2ed04-120c-303a-a9a9-c7e11d42378f | -19.33203 | -46.31603 | 2024-11-28 12:38:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| db26f46b-aba8-33cd-834d-23bff171610d | -20.00694 | -47.5668 | 2024-11-28 12:38:00 | TERRA_M-T | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a51d182d-fb57-3db2-ad63-665c697e552a | -18.01523 | -51.38158 | 2024-11-28 12:38:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 28ccf599-53a5-3e15-b509-53ec3ef356f1 | -19.33067 | -46.32618 | 2024-11-28 12:38:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5b840ce8-9356-37c1-bbb2-db6f7b395e31 | -20.25801 | -46.40896 | 2024-11-28 12:38:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5aad31df-74fb-3890-b892-4a16c4611f0b | -14.91273 | -46.18738 | 2024-11-28 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e11c372d-e746-3538-8598-3159541b3ac5 | -14.59011 | -43.15683 | 2024-11-28 12:38:00 | TERRA_M-T | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5938ef57-7960-3162-b9a9-4f70b66d1ff5 | -16.68151 | -47.2385 | 2024-11-28 12:38:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8f7618d3-1ca7-344f-bcbe-792951c03f05 | -19.83865 | -43.18001 | 2024-11-28 12:38:00 | TERRA_M-T | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 08f1d3ec-e4c1-3522-b6dd-3d841e80e85f | -16.04324 | -51.13134 | 2024-11-28 12:38:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e9312f49-6604-31ba-95b4-471af37854d7 | -20.51116 | -40.82867 | 2024-11-28 12:38:00 | TERRA_M-T | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| fe553f89-7bbf-34b8-9c76-c9b6d9dc6f63 | -15.89865 | -43.60382 | 2024-11-28 12:38:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6611f2de-9129-35f9-a46c-87791f2cb802 | -20.3932 | -44.48007 | 2024-11-28 12:38:00 | TERRA_M-T | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| df7bce39-1334-313f-99e5-78c24f0f683f | -19.6196 | -51.18034 | 2024-11-28 12:38:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 49a2faca-b8d8-3ecc-84fe-0141f7961993 | -18.01323 | -51.39386 | 2024-11-28 12:38:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6ee13918-a129-3ec6-9f20-2c2b9efe82cc | -16.70502 | -46.07961 | 2024-11-28 12:38:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9389683e-b605-33e2-a1dd-b70da6d7aa3a | -17.65516 | -44.46418 | 2024-11-28 12:38:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 42154b03-4c5d-3875-8e58-6d8376263d39 | -19.89207 | -43.80709 | 2024-11-28 12:38:00 | TERRA_M-T | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| b32702a5-52c8-32c7-a182-e990ab271571 | -6.1039 | -43.9824 | 2024-11-28 12:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| dce02e6f-5560-3b34-b094-7d9317e830f4 | -4.4845 | -42.8631 | 2024-11-28 12:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8c64b90f-6ffe-3a65-9663-8f9f6daec84e | -2.8609 | -46.8626 | 2024-11-28 12:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 8080e453-a33d-3944-945b-f5ec7b90cc3f | -5.4546 | -43.2659 | 2024-11-28 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a3573272-ca11-344f-8424-a8109910f33a | -5.4548 | -43.2426 | 2024-11-28 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d505cb30-c614-3a5b-838b-25c609fc71a5 | -6.0853 | -43.9608 | 2024-11-28 12:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c3cbcd5c-0430-3832-a8af-cbbd68bb45bd | -4.6565 | -42.3811 | 2024-11-28 12:40:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 5a8ef328-48a8-3e54-986d-259fb0641d69 | -4.6753 | -42.3799 | 2024-11-28 12:40:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| a2abdd3c-5019-3ec3-93d2-1f32f8414eac | -3.1802 | -42.225 | 2024-11-28 12:40:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 03fd1887-0d87-3e29-b531-67fad7abf2e4 | -21.12146 | -42.93331 | 2024-11-28 12:40:00 | TERRA_M-T | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| bb875dde-03a5-3e70-be58-94b4b058499a | -23.36944 | -47.06293 | 2024-11-28 12:40:00 | TERRA_M-T | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 730bfac7-206e-32a7-a64d-1d293afe134d | -23.65317 | -47.14567 | 2024-11-28 12:40:00 | TERRA_M-T | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 9e52336d-0303-3dc0-bb09-aaeab9b70a97 | -22.63386 | -47.54473 | 2024-11-28 12:40:00 | TERRA_M-T | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.2 |
| 46cb731b-9f5e-3607-8f2f-120ebed6c020 | -23.63784 | -46.24859 | 2024-11-28 12:40:00 | TERRA_M-T | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 2581724f-36c2-3273-b095-f23a4f14d84a | -22.64425 | -47.53616 | 2024-11-28 12:40:00 | TERRA_M-T | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| b2b012ac-845b-3a15-94b2-405139a36225 | -22.69363 | -47.30719 | 2024-11-28 12:40:00 | TERRA_M-T | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 06113c08-00eb-37ef-adac-e7bd533fa9c5 | -23.7856 | -48.86254 | 2024-11-28 12:40:00 | TERRA_M-T | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 81d2b909-11c9-3850-a26a-5d58bc398667 | -22.63251 | -47.5547 | 2024-11-28 12:40:00 | TERRA_M-T | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 267b2df1-fb2a-3030-b5cb-272b07bd03ce | -22.6429 | -47.54616 | 2024-11-28 12:40:00 | TERRA_M-T | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 305.9 |
| 74343dce-2de5-3d30-97fe-b6080dcbf844 | -21.73198 | -45.59402 | 2024-11-28 12:40:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| b2ae1042-d5ce-300e-86f5-dfbb2ef8d88c | -23.71111 | -50.55528 | 2024-11-28 12:40:00 | TERRA_M-T | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 85cd0124-49a1-30f0-bfe0-0bc5c8d13ba2 | -20.95511 | -43.79074 | 2024-11-28 12:40:00 | TERRA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 5cf6c302-c61d-3127-98a5-858e868138b7 | -23.78124 | -47.83412 | 2024-11-28 12:40:00 | TERRA_M-T | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |


[Clique aqui para ver as próximas entradas](README102.md)
