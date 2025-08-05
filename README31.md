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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a8357bd-4989-307b-8439-9fb29f6a90b3 | -6.96699 | -42.86367 | 2025-08-05 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 56c0c255-d814-31af-835c-723708442ce7 | -4.44303 | -39.08511 | 2025-08-05 12:12:00 | TERRA_M-T | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| e4ea9ac1-1993-3b43-9331-37d1f1433a9d | -8.73319 | -46.43683 | 2025-08-05 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| de792889-9e7b-317f-b1ce-d55fef423744 | -7.99939 | -43.13245 | 2025-08-05 12:12:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 89032fbc-1f3c-345c-8673-7445e705adf8 | -6.98592 | -43.38997 | 2025-08-05 12:12:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e519f580-62f6-39b1-b849-4e931fd14f80 | -6.24177 | -45.86337 | 2025-08-05 12:12:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 69176796-cd74-374a-8385-d093e8c0e7c0 | -7.54094 | -44.86641 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2886218a-6010-3789-b988-7e1f14fa9ca2 | -7.56736 | -44.87014 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 174726c2-ccb9-3495-bf10-0fb7b0b29e82 | -4.66159 | -41.96129 | 2025-08-05 12:12:00 | TERRA_M-T | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7a6c73fc-e0f2-33c4-871e-4110286b3603 | -7.83969 | -45.1049 | 2025-08-05 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a3a20aa9-1b79-3269-99ac-301fa224885d | -5.92746 | -45.10988 | 2025-08-05 12:12:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 028a621f-3504-372d-99d9-a806c733b68e | -7.84098 | -45.09605 | 2025-08-05 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| e5178244-4293-3c77-9bf3-53a6f0e230ac | -4.9929 | -43.07187 | 2025-08-05 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 98395b0d-94f3-38e9-8af2-a0d2739121d4 | -8.0069 | -43.21133 | 2025-08-05 12:12:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b057e120-95df-3b2e-afa0-ee9f6b7da19f | -6.95641 | -42.81656 | 2025-08-05 12:12:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d803b6c9-4208-38fa-b27b-33573b3e8aa5 | -5.48224 | -42.15976 | 2025-08-05 12:12:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e3016f1a-bd96-3d98-bfac-089925c77f2c | -8.38745 | -44.81737 | 2025-08-05 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6b4820a3-d4fc-3b88-b183-678f5775f6e7 | -7.59674 | -45.30508 | 2025-08-05 12:12:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 249577b7-d8ce-3ecf-a77f-cb9e199ad553 | -6.96565 | -42.87333 | 2025-08-05 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 16ce5f58-32d7-37a1-9e60-580eb852e3a3 | -3.40517 | -43.0077 | 2025-08-05 12:12:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 85449a22-5ddd-3766-ad90-9abe39a5a232 | -7.58416 | -44.44035 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 862be0bf-f0f3-371e-a432-b48347d1468a | -7.37348 | -44.16636 | 2025-08-05 12:12:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| db3aed1c-ee22-3487-bf3f-552cd23710f5 | -7.41785 | -48.12242 | 2025-08-05 12:12:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| f2115a15-4dbc-3db8-9783-2ca53d675198 | -6.50107 | -45.54569 | 2025-08-05 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2b693364-d1e9-3f13-95d1-6c2eaac0d602 | -3.4804 | -43.25158 | 2025-08-05 12:12:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cddd2295-6ce4-35e0-a3f3-36d93eb031fc | -6.3496 | -43.3898 | 2025-08-05 12:12:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 662b539e-5a75-37c1-824a-af42d9cf2af1 | -6.76272 | -44.31454 | 2025-08-05 12:12:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 63b52930-beb0-30db-a61f-d81701aceba9 | -8.84069 | -44.55944 | 2025-08-05 12:12:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 857600e4-e844-3050-8f97-9baa27452bb4 | -8.71649 | -46.42489 | 2025-08-05 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b1c63e1b-47f6-3e7a-90f4-1367295cf306 | -4.67096 | -41.96261 | 2025-08-05 12:12:00 | TERRA_M-T | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c55e5086-409d-31c3-b38e-7150994cce4f | -7.77618 | -45.21626 | 2025-08-05 12:12:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8fb878ae-78ba-3874-8d42-126e20b242bb | -7.60558 | -45.3063 | 2025-08-05 12:12:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f18099b3-2c1c-34f1-85d4-ff1bd65cb0f5 | -5.89364 | -43.73597 | 2025-08-05 12:12:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b31595c2-fa7f-33ad-af59-523366909f2e | -5.44435 | -43.5882 | 2025-08-05 12:12:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6d7eed84-117b-318f-a7bd-2489884ee503 | -6.27403 | -45.26571 | 2025-08-05 12:12:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| ea1fbb23-f46c-3a6d-8ffa-18d96ebf8ebd | -5.1509 | -42.86547 | 2025-08-05 12:12:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b2863ca-c9fa-3fd2-a7cd-75c6634e8d11 | -7.21823 | -44.48123 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 50c749e1-95ab-3d34-bf5b-12d1467822d7 | -6.23275 | -45.86208 | 2025-08-05 12:12:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| bcec106d-9e1d-342b-a23a-431ec07cf677 | -3.00136 | -40.02414 | 2025-08-05 12:12:00 | TERRA_M-T | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| bb813b9d-81fa-375f-b929-1d51a69ff64a | -7.42006 | -45.31269 | 2025-08-05 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0871ca28-aa01-30d5-8e0a-59643972e8f5 | -12.99576 | -47.45088 | 2025-08-05 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8497204a-5dbc-3457-85cf-6f886a8bdba1 | -8.85967 | -47.61857 | 2025-08-05 12:14:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ef4e0aa6-a8b3-314c-8cf0-bbf84887a997 | -14.91536 | -48.6131 | 2025-08-05 12:14:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c8cdcf2b-4fbe-31f9-999d-fc2c61fb629a | -12.39257 | -40.89221 | 2025-08-05 12:14:00 | TERRA_M-T | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 30.8 |
| db1eb390-537c-3f3c-a011-92ce08bf4079 | -12.35183 | -46.05808 | 2025-08-05 12:14:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 62411683-2c82-3f4d-9ebe-770ada4d7af0 | -8.94735 | -46.73742 | 2025-08-05 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 205fd369-9815-3700-bf14-53788c43b7d3 | -10.9276 | -48.37369 | 2025-08-05 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 61385806-99c7-3a4a-96d1-18bd2b8aada5 | -11.4991 | -44.26978 | 2025-08-05 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4a352692-7cca-3344-ba43-6d3ede1cd7bc | -8.84937 | -47.46151 | 2025-08-05 12:14:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6a082ad3-a0da-33ed-8015-7349aae25368 | -12.69021 | -48.12706 | 2025-08-05 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 60e10c50-81c4-3f2a-aaf9-3e52db34e668 | -11.76185 | -44.96106 | 2025-08-05 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 775aa2ab-b78d-3042-9c75-25eeca13341c | -11.76387 | -47.53706 | 2025-08-05 12:14:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 63c0c22e-7c6e-3fe7-acf9-d01f387f3f24 | -15.3401 | -43.84317 | 2025-08-05 12:14:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b75f2f6-1ab2-319e-b878-afa7dc5c9a5c | -9.61357 | -43.31712 | 2025-08-05 12:14:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8e50bc98-84e5-34c4-9d9a-d23fb70ed9e3 | -12.39067 | -40.9076 | 2025-08-05 12:14:00 | TERRA_M-T | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 32d494f6-a62f-3dfc-a224-78fa3110dbde | -16.47196 | -45.00737 | 2025-08-05 12:14:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3dca5c7c-eb96-3c4e-ac7d-0d57b650ec15 | -16.47063 | -45.01716 | 2025-08-05 12:14:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 93dd123a-281d-3e56-8f6d-ccf6d91fd4c3 | -9.61493 | -43.30732 | 2025-08-05 12:14:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| adfce631-0e21-3eb7-b505-3b9a4b8a5856 | -14.26732 | -51.964 | 2025-08-05 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| bd4ed007-6574-303b-94b7-3233b793b31b | -12.68238 | -48.1156 | 2025-08-05 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4cd5c11d-ec32-31f0-820a-e3b2571f7de6 | -8.95647 | -46.73878 | 2025-08-05 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| ebd43e9d-658a-3eb3-882d-481e089b6079 | -10.78895 | -46.64548 | 2025-08-05 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 95659b19-ab5e-33cc-81ed-e9f8f428affe | -16.78007 | -49.10013 | 2025-08-05 12:14:00 | TERRA_M-T | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9ac42566-ea10-3097-bc3e-0c84cb8e74d7 | -8.93823 | -46.73608 | 2025-08-05 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a804101f-9ca2-35e2-b620-41ecaf977ff8 | -11.65709 | -50.15208 | 2025-08-05 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1377932f-9743-38a9-9700-f18bdd0d042c | -11.75471 | -47.53544 | 2025-08-05 12:14:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 7ebd759a-55db-338b-9b49-e2000ad702cc | -12.84574 | -43.85242 | 2025-08-05 12:14:00 | TERRA_M-T | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 504e3ada-5b76-329b-858c-79ef0287c0ec | -11.74661 | -45.00497 | 2025-08-05 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 179b6257-03d1-38f5-9b46-b467dfa42ff8 | -14.25949 | -51.97349 | 2025-08-05 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 9fd99864-54a9-3503-bd53-6fb662b3efd3 | -11.36358 | -41.40333 | 2025-08-05 12:14:00 | TERRA_M-T | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 97cf7995-254b-3248-9294-e7d97740fcf6 | -11.66797 | -50.15384 | 2025-08-05 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ecd8ad42-334a-3b2e-b367-e231332301be | -10.29842 | -46.52618 | 2025-08-05 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fac3ffac-7d9b-36b9-a804-240d0a1fa194 | -10.81829 | -46.50858 | 2025-08-05 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 749c6960-374e-3a8d-8524-b15eacc8832b | -8.85174 | -47.60669 | 2025-08-05 12:14:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1795107a-0970-3a5e-9c3c-f8292297139f | -8.93682 | -46.74558 | 2025-08-05 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 82b9c70b-b3f5-3346-987c-13858bd45516 | -11.79219 | -45.00231 | 2025-08-05 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3687e65e-376a-3085-a7ff-336b34f02724 | -10.80935 | -46.50735 | 2025-08-05 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1f938d23-944b-33d3-ae54-4b432e81bca7 | -11.76238 | -47.54694 | 2025-08-05 12:14:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 31a61695-460f-3b1a-abe3-4f4fa84bbb9b | -12.69174 | -48.11708 | 2025-08-05 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| aa5fbf02-56b6-3ebb-8212-3f071508dd7e | -12.99434 | -47.46043 | 2025-08-05 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bf80da4d-eda8-3327-b9a3-3144f03ccf94 | -12.73714 | -46.39455 | 2025-08-05 12:14:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac307bb7-b240-3235-aaa3-10b0832f5e1b | -10.79655 | -46.65611 | 2025-08-05 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b3dd8dcd-fac5-36d1-b95d-639de121511d | -13.24966 | -46.98417 | 2025-08-05 12:14:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 321ff115-6154-3f10-bf28-2dde4f012c7e | -10.81693 | -46.51783 | 2025-08-05 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 40d1b796-dfe1-3f31-8946-40143f038469 | -12.39152 | -47.04522 | 2025-08-05 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e505f834-b8cb-3dd5-9ebd-c7f3b1bcc760 | -12.52521 | -42.42266 | 2025-08-05 12:14:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a4d45566-9a80-3960-b96b-d5efa806b321 | -12.70731 | -48.07769 | 2025-08-05 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f7c14c1d-ba32-3658-9534-dc2d37e9df58 | -14.26435 | -51.98142 | 2025-08-05 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a1552643-d6b9-3c0a-97c7-12ea7d6199af | -10.7795 | -45.50764 | 2025-08-05 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5903a78a-af1c-3951-977c-3ed8006affc8 | -11.79347 | -44.99331 | 2025-08-05 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c859ff4-0057-3544-ac2d-731e475645aa | -14.26233 | -51.95607 | 2025-08-05 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 6dbc60d5-21cf-32c2-a01f-f31c4c40e894 | -14.25539 | -51.96193 | 2025-08-05 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 258.2 |
| e6ac909b-6ca4-33c5-9287-6de95f3ebcaf | -10.57613 | -50.49683 | 2025-08-05 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 12b5a0b0-6f96-368d-bc0d-a9a3277ea5a9 | -13.25084 | -46.85263 | 2025-08-05 12:14:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6e62682-0486-3888-94b1-d32a244c43b7 | -11.74788 | -44.99594 | 2025-08-05 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cf39011f-9cc1-368f-b6ee-d6fde8b0accd | -10.79792 | -46.64683 | 2025-08-05 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| bbf4af08-bdd1-3291-aaba-4ffd41227280 | -32.37008 | -53.56999 | 2025-08-05 12:19:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 20.4 |
| b62f0173-cca4-31ce-804b-a9c077bb4ff2 | -32.368 | -53.58239 | 2025-08-05 12:19:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 13.1 |
| 3e4ad56d-0448-3c64-b74a-b26ff4b9619e | -8.012 | -43.2219 | 2025-08-05 12:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 4a8f1184-776c-3392-aabf-dcb1587f01e0 | -6.236 | -45.8607 | 2025-08-05 12:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |


[Clique aqui para ver as próximas entradas](README32.md)
