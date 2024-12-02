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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5349872-cca2-37ab-b060-ed06b7e927f5 | -4.43466 | -41.77222 | 2024-12-02 04:25:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b69c4c36-c425-30c7-beb9-72d9e0ca2ee4 | -3.40443 | -50.23109 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36f43745-bf99-3a18-b0a2-8c49bc39daa7 | -2.75149 | -51.75553 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce9f30b5-760f-318c-9e2a-c15c564c8bc5 | -3.4616 | -50.26804 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e5746e8-581e-3d78-8887-c60fccacc747 | -3.7888 | -46.70268 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9043b789-1720-3807-b733-aae02b85bf66 | -6.45906 | -47.54311 | 2024-12-02 04:25:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3a725ed-c454-35c8-a9e3-50b6cd021ce5 | -10.65516 | -44.49724 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 056c89dd-b19a-3fb4-a468-a4bb2b28799f | -3.8804 | -46.57993 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad5b80a6-c84d-3f76-8bc0-cd3647543050 | -3.45591 | -51.41909 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a6ebe2a-4bcf-3565-9463-334fd6bb1849 | -4.56274 | -45.47183 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f199068-365a-3c33-9236-3b56eaec4cea | -3.54075 | -51.02604 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2e5b695-bcad-3e6a-8bf9-3953a122393a | -3.65791 | -50.4397 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4359e4b-a105-3fc3-a3de-f00a5a09d841 | -4.90044 | -41.34347 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 65c503c6-e6e1-3b84-a952-f583bf70d6fa | -3.74125 | -51.69062 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 646798cc-48eb-3ef4-90f9-675dc7584107 | -3.86139 | -50.89477 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f4efde1-77a2-3a69-a857-6c87e70f561f | -3.07107 | -50.99155 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 699cb029-db1c-3410-88c9-fb2d5c7dc7ad | 1.93918 | -55.70839 | 2024-12-02 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cbb0442-2088-3cdb-8f8a-aafab98c345f | -7.61276 | -47.0954 | 2024-12-02 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1d55a94-01aa-39aa-a8eb-e13259be6ae6 | -2.89405 | -54.16101 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c3d5133-7004-33be-9e98-98cf23b84686 | -6.14741 | -52.04499 | 2024-12-02 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9ec2167-1191-3e13-8e8f-1f9dd3f49af2 | -2.41204 | -53.85907 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30ea8451-b8b6-360e-b572-d1831549b1db | -4.32611 | -45.92361 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe3c2b37-ebe0-3acc-b2a9-32baecdd17ad | -4.67871 | -46.36945 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ac601c-7aeb-3019-a156-cf8c46a0cfde | -3.2515 | -53.92339 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d28d3414-c2e7-33e0-a8bf-bfc3b18962bf | -3.78955 | -52.40635 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b272b9a7-2d96-300d-840d-deb60e2325f2 | -3.78824 | -46.70623 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f46738-4c7d-3722-a748-a9cdbb19e9e8 | -5.58046 | -45.14799 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 31caee96-903c-392c-8f64-b22c4916bce3 | -4.10977 | -50.49448 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a7951df-c635-3bed-9bd3-cfde0557a3ad | -4.14024 | -48.21992 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc14d010-c746-3db0-9b67-732046500ed2 | -4.25529 | -50.85162 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2822da5-6f8f-3b28-b621-68d7ed0414fe | -3.16493 | -49.02278 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0ef0884-1d7e-377c-9742-b173d18c5dcc | -2.82685 | -51.81447 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db863b32-30ec-3f33-8dbb-64db400d9390 | -5.12731 | -43.20173 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1711b4c-fabc-3610-8d0c-a942aed8a689 | -3.90766 | -49.73888 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02e016b1-c226-32d6-8476-385352a6238c | -3.98577 | -49.8747 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d3dd82d-d76e-3540-8c67-5f22307a6058 | -3.82071 | -46.58865 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08951104-4075-3226-8d32-c17883b8fb59 | -10.70002 | -44.96963 | 2024-12-02 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a27fddd1-14f5-354a-8cef-4160ade80cea | -5.12193 | -43.21317 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2cc7458-7361-3f32-b14a-8224e5890dee | -3.97732 | -46.71831 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58c6abcd-42f1-3233-8019-cdce51f78d74 | -3.04705 | -51.3471 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3739b2c2-5ade-3f42-b12a-64d96892d92b | -3.43208 | -53.89391 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca735b74-d35f-30a9-b63c-2f2e55d42ea3 | -6.08425 | -48.0523 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 827b8d4e-309a-3306-8bf2-3d7c3e722338 | -3.04269 | -49.37728 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81af210b-02ea-3dba-a442-108a115f4842 | -4.05198 | -46.99546 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 829cac3c-a1b3-3452-998e-e0eeb2aa036b | -2.74775 | -51.7505 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4489918-e225-3195-b415-b21145da02ab | -4.16799 | -46.55721 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c61b908-6263-3312-8761-64bfd6d9596a | -4.32666 | -45.92016 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9514c54f-c7b8-3870-9763-0e538140172d | -3.25634 | -53.62646 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eb53a94d-3d82-3a6e-afb9-dc63a929ca50 | -3.8408 | -46.57015 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f82d3a18-aa56-3d40-b28c-47a5cf9fea01 | -10.65222 | -44.49266 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2285997-6432-3939-ad07-40a125bdacbd | -3.53164 | -53.51158 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c481d612-0ee2-3353-bc00-9d45567bc8df | -3.21376 | -54.17392 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32bc5494-c423-387b-920d-04f4b95e7f47 | -2.63547 | -54.20111 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5539ffa-bea1-3290-824b-6318fc9aa8f0 | -4.906 | -41.33335 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 90657cbd-5be4-3208-a2d1-0d1c83a652a5 | -4.14376 | -48.22046 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52044949-0e07-3ae0-af6b-978e2d7f6b16 | -3.7088 | -52.18673 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30fc1fe3-cf7e-3639-bcd7-1fbf20c2a393 | -4.01656 | -47.00087 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e28f60b-5aee-34f1-8d24-a2c4be93d6d2 | -2.79556 | -51.89527 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc99a59e-914e-3103-95a1-e3707c335bcf | -4.66595 | -46.87313 | 2024-12-02 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 272e1ba7-e301-39ec-b3c5-57e28fd2ba4c | -4.77041 | -46.43001 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1208ddb-bf88-35c5-a483-d707861df356 | -4.20797 | -50.6838 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6f5260e-3eaa-310d-9f44-87fb6ffe18fc | -3.42346 | -50.65475 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d6c5388-7e61-39ce-b17f-65b20e857db2 | -3.95325 | -46.5022 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c02dce4-c4c6-3c28-94b9-bd3c0af274ac | -4.07106 | -46.67868 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed12c3d0-3369-3c67-b008-56329469e2d9 | -3.06774 | -53.68734 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa71d674-487b-319f-8220-c3105479a8cd | -3.73945 | -51.83576 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1157ec0-945b-3cae-8b75-5009e9ca7508 | -3.74743 | -52.26172 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a86fcc6d-e3cd-3bf9-adea-09c7ea583e9d | -4.16855 | -46.5537 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1df49516-43a8-39e3-bb88-8e024ea242fc | -2.79413 | -51.90409 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06fa7a6d-d509-372f-8ca7-8d9be8bdaf0a | -3.07181 | -53.80848 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d4a649e-11b3-387d-8d58-7a4f6615104b | -3.18168 | -54.33306 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe33807c-2ab7-32fc-ba65-bd0f7c1cf05f | -3.93654 | -46.49959 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744224ab-c03a-3f9b-9757-67e05e67f454 | -3.746 | -52.27058 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2dad776-a882-3860-8adc-4962bdef57d6 | -3.95661 | -46.91499 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e40cd8ee-700b-351a-90c5-3af079ad3d6d | -2.86776 | -51.2585 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1daa1c8f-e649-318b-b3a2-16b45d7be4ac | -2.80759 | -53.05543 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 820b1722-5aad-3084-9f70-e48769bd7f15 | -4.14829 | -48.23721 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13272b6d-6070-3190-8549-9be2fee5502c | -5.01022 | -44.16899 | 2024-12-02 04:25:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9db0b9f-dc9a-3002-8f3c-9a4221180922 | -5.61136 | -43.47328 | 2024-12-02 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86daf4cc-a46e-310c-bc40-752a38eaed4c | -3.90544 | -47.72216 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de178370-bf95-3386-9304-9a37b03392be | -4.04861 | -46.99492 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a44ab6de-6f05-3208-ba49-79c226fdb9a6 | -3.25359 | -53.92839 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abe5ddf1-2968-3558-b0ce-0a99f7e4d847 | -7.4912 | -46.76838 | 2024-12-02 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 389d316f-49e7-3a4a-adda-24817ed0d12a | -3.25499 | -53.93367 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ed5dfc0-8f91-33c5-8c12-1dec2d43cb56 | -3.40305 | -47.14914 | 2024-12-02 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89fb1bd1-ae3d-3169-8750-c755ecd748f1 | -5.91478 | -46.25224 | 2024-12-02 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a49dec7e-c93c-3d6a-8072-59a6dbe9892a | -3.54384 | -51.50089 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 114787f3-1428-32c2-9dd7-ebeaeb4033e5 | -4.31859 | -48.21114 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2315e04-21b7-3e60-8f59-741346eee5df | -3.25353 | -50.57571 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2621e42-a0c3-3d37-b661-bfc36713a6fd | -4.14766 | -48.24112 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f2a26d0-e382-3740-b09d-a2cb30d84fbd | -4.53031 | -45.74304 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ceab7ad-62df-3258-802d-17fc10788d14 | -5.5866 | -45.15254 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c11796f8-30a1-350b-bd16-7b5a2d1da880 | -3.33132 | -53.54377 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4819ac5-07c7-31a2-995c-872f6b3ec811 | -7.29258 | -45.11308 | 2024-12-02 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 374921fd-7ec0-3a62-b002-9cdc8c813fe5 | -3.25682 | -49.9029 | 2024-12-02 04:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0738435c-2204-37ef-a8a4-861ef2c7719f | -3.69667 | -47.1464 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 858a4513-6542-3ab5-a98c-61c771c643db | -11.27855 | -41.73084 | 2024-12-02 04:25:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5de72fa1-dc2c-3053-95a4-c66abe4a68ac | -4.90284 | -41.32769 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9da10d00-15da-3df6-9b8b-00d700984d4e | -3.54148 | -51.5017 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8795e366-cc91-36e3-85a2-faae9743f463 | -3.85028 | -46.53206 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README37.md)
