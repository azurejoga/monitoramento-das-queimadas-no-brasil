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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47e764b5-59b6-3e58-a304-58f645a0a890 | -13.35717 | -51.73862 | 2025-09-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad774a13-c786-357d-b5e1-32a8f0cac70d | -14.59714 | -48.06246 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d8093dc3-0251-308c-b6d9-ce1f1eb5841a | -14.73384 | -46.75203 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75f968a0-418b-3d3c-9b02-0a5ae53a8a9f | -15.1258 | -48.1092 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae25b532-4dce-3508-bc47-5ba477c8e928 | -12.9252 | -56.96115 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1be77d1f-586d-3002-a46d-e8a718402d2f | -15.57008 | -48.37273 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa0ab5cf-ac32-3f12-8c34-6ce023e1b464 | -14.99402 | -48.3193 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7621d20e-17b1-3c26-99b2-6179afcba5e7 | -14.60748 | -48.03614 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa781c97-240e-36e7-9b78-d82c77effcef | -14.22662 | -51.66311 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0323766c-7409-35f5-872e-30127c48e4cd | -12.928 | -56.95467 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 260bb20b-98b0-329c-94cd-3e67a84587f0 | -14.78324 | -48.1838 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb1e450b-c2b7-3c41-b668-0ef40353a1f1 | -14.22018 | -48.05594 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 826f1017-b7b9-3376-8ba1-77f55dee7b39 | -18.16286 | -47.91488 | 2025-09-02 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ab53d92-9063-3a92-a665-5c7cec56b72f | -16.07792 | -43.62144 | 2025-09-02 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1435e225-8542-372c-b951-3d4a7823dbc6 | -14.60958 | -48.04521 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ec018a4-337b-3e16-9b97-78a7a6f3e791 | -14.57979 | -54.54122 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a05f309-cc32-37b2-ba90-445d9ec83db3 | -13.89624 | -48.08497 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da4ca7ac-abab-3142-8069-ff6d50b87f7f | -12.92206 | -56.94399 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 720b92b2-1c0a-3ad4-a734-0b32aeb56319 | -14.59642 | -48.06676 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77ecd88a-8088-3809-8efd-f900373e5afb | -16.42728 | -49.89645 | 2025-09-02 04:17:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fd282c9-01ae-389e-8618-02f5aabe95de | -20.62385 | -47.19701 | 2025-09-02 04:17:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dfcf54b7-2723-3547-af8e-c0e4aaaa2c7c | -14.58218 | -48.06393 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31088a5b-fe51-31a9-8dfd-057856950986 | -14.48615 | -45.94301 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c5c4a25-ad82-3bf9-948b-b4be0dcaf37b | -18.08712 | -50.47641 | 2025-09-02 04:17:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 19583152-a3cf-3996-bcf0-090dbd1138ff | -14.59732 | -48.07358 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eed1c27-29b2-393c-ae37-7fcc8df45e9a | -14.2636 | -45.25229 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d721ba6d-c537-3658-9808-41b4c1f4fb73 | -12.9205 | -56.95878 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61b4119b-d70e-3d16-b78f-4e4ec2912394 | -20.69444 | -46.30775 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fdd4cea-4ca8-3138-8a8f-28a184ead6c4 | -15.13151 | -48.11282 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a02c060b-faf5-3174-8104-d5be3d1cea3d | -14.58275 | -54.54268 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 031e4a6f-05a8-374b-bed8-258639ac26b2 | -12.92407 | -56.96668 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ae6ccd5-54d0-3fdd-9171-c798705467c3 | -14.71789 | -49.44413 | 2025-09-02 04:17:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c6898f-e09e-324f-9656-1521aa62bb35 | -18.04505 | -47.73837 | 2025-09-02 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8001d70e-daea-300c-8306-8d9f74b62bf2 | -23.78439 | -51.07949 | 2025-09-02 04:17:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 964763d7-0fa6-3ea1-bb53-5ec62f77c1de | -14.64385 | -48.03818 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 680c40a6-5b02-3511-8ab5-244e4f105d66 | -14.5829 | -48.05967 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f5e15e-1833-3c51-b08f-179555850415 | -20.69559 | -46.3004 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19a48d1a-7386-31a1-90fe-8e4f8f404df8 | -23.93475 | -48.8462 | 2025-09-02 04:17:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f22cde5f-f13f-3a5b-9d44-6360be6c2fba | -14.75094 | -48.1568 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc22b39e-21a5-3f5b-8626-511be28b63b2 | -14.58373 | -54.54937 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e8f964-1cdb-30dc-afcf-2ff3cca8f564 | -14.58302 | -54.55298 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11f3eb58-a025-34c8-81bb-5eed8de2a530 | -14.79764 | -46.72468 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93d5682d-d132-38c3-a11a-34264d8a8cde | -15.56008 | -48.34513 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9335a796-7298-34f3-a7ff-9181a2d67fb7 | -15.58362 | -48.37984 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a7907d7-1146-34c2-b051-198e2d8bdbe4 | -19.41344 | -43.79151 | 2025-09-02 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf0f4e64-9cb0-3e99-ae23-a1dff763f292 | -14.74874 | -48.14808 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c230a432-313f-31f2-946b-0ca1533d3d3c | -15.091 | -48.1199 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37a06d32-50d2-3dc7-bb30-6f2b3ff0b8f1 | -14.27467 | -45.24684 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11f07ef3-c2fe-34de-9e57-1df0cf367737 | -23.9341 | -48.85012 | 2025-09-02 04:17:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c387dc5-319a-3137-ac0a-d9accb2eded5 | -14.59145 | -48.05252 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 489a3518-4794-341a-8d59-26a254045952 | -12.91742 | -56.99941 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50077b42-bb30-3161-bb40-374d24a5fc31 | -14.79326 | -48.19005 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d8d47c0-faac-3be7-895c-12a54e5787eb | -13.825 | -49.38184 | 2025-09-02 04:17:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2664b0ee-8941-3060-a867-90bd004ba9dd | -12.93044 | -56.96799 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ae72fcb-c522-3365-bdaa-4a72e7f5e6b0 | -14.59779 | -48.03667 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e268567-a81e-33bf-a1c1-6279cfde729a | -14.62921 | -48.95318 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b5864af-f229-3b25-92e8-b3ead83a4466 | -14.59881 | -48.06501 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44a56012-68ee-3727-9335-388fbac94e8e | -20.70164 | -46.30523 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c204b59-0000-3c8a-9a17-f0a4046dcdc8 | -13.6971 | -51.94289 | 2025-09-02 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 836bdf78-8a3e-3221-8779-933dcc25000e | -14.76672 | -48.15068 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91ed4cb4-91bf-3251-add6-099ec5bc7103 | -18.54762 | -47.46207 | 2025-09-02 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c04509-b908-3054-810e-0486d7447c35 | -14.2741 | -45.25039 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7bb47f43-464d-36fb-a5b4-544af01b582e | -14.73508 | -46.74456 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2cd71e2-6647-3da1-b315-0bb9b7c5b981 | -15.08816 | -48.11504 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e68a68-5669-3614-b465-d3cd54acd9ce | -14.77246 | -48.16032 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc840d97-5220-3143-a791-ff88bebb0f1d | -14.20081 | -51.65345 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 245b7116-c8c0-3669-81ce-162e70d82fa4 | -20.68534 | -50.15957 | 2025-09-02 04:17:00 | NOAA-20 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be1a7a31-1862-3161-bf73-2fabd438454d | -12.9249 | -56.99529 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de45c1ef-d350-3df9-be2f-27e99efbfb85 | -12.92185 | -56.97764 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 65be5333-d7b6-3375-acf2-18c3d70611fb | -14.5588 | -48.95897 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 304b36fd-05bb-3c0c-85cc-87a1f1d7667a | -18.04781 | -47.74286 | 2025-09-02 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37e59c1c-9bc7-39d4-af73-68ce05b5a04c | -12.91936 | -56.96422 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cfe7a5d-916a-3017-b0e2-8fe2ff1b9555 | -15.55791 | -48.35769 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c69376f-55a5-32b5-8f5a-3886044786e8 | -15.11564 | -48.18308 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb7c1dee-39e6-3a79-8789-0ac7812c9489 | -17.89243 | -47.17301 | 2025-09-02 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c15dfaea-497e-3963-97cc-4aefd4b80e9e | -14.22749 | -51.65844 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b483973e-0aef-3dd0-8ada-6bf4f4b8644d | -14.26966 | -45.25695 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a6dd231-4d09-3749-b9b7-757aeb807e70 | -14.77967 | -48.18309 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ecb982-4223-38b6-b39b-6b59c80c7c0e | -15.55872 | -48.33162 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9dbc6fa9-8f92-3239-8a0e-b14b18d5b7f4 | -16.59157 | -48.97889 | 2025-09-02 04:17:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 25263a13-bc7f-3d4c-a76b-592fc660bbac | -12.92295 | -56.97224 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e13bf7b5-ffe1-3df1-bf68-147eb9a9198e | -17.28468 | -49.20283 | 2025-09-02 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6100a517-477a-3d45-8579-81b1256f5ff0 | -14.5996 | -48.03919 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ead2362-7185-3b66-996f-f20b64fe7c75 | -18.75434 | -47.61176 | 2025-09-02 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4a3ba5b-1ecb-312a-8057-7911e1b1b5d4 | -18.04845 | -47.73902 | 2025-09-02 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eacbbe18-0903-3e94-9e8a-829f5dbeafb9 | -15.72338 | -49.02971 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cc17496-c441-3134-8f68-4acc41904988 | -14.78333 | -48.20509 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4212d918-4b9c-3ddc-af69-66f7d7ddc8b0 | -20.39019 | -54.66578 | 2025-09-02 04:19:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204be3a8-3e24-3451-8efb-29e6da987f0c | -22.52673 | -46.80992 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e102e478-7e13-33d8-a9fc-c655bb82c15a | -22.79247 | -46.25647 | 2025-09-02 04:19:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f9eb60bc-0769-3758-a7ef-95ca3462f52e | -23.66711 | -47.48046 | 2025-09-02 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1295589-b593-3254-bf2f-296c93d7d1c9 | -22.39682 | -47.1813 | 2025-09-02 04:19:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f75ad3c7-c9b7-3317-bbcd-82a8a9382287 | -22.10795 | -46.96942 | 2025-09-02 04:19:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dca4f38e-184e-3e3c-9f5a-af329c6871c7 | -23.31728 | -46.03341 | 2025-09-02 04:19:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7f25082b-47bf-340b-bf8c-c7dad3822e6a | -22.52789 | -46.80246 | 2025-09-02 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2634b66-9a12-367d-ae68-e2b65709127c | -23.04906 | -49.87191 | 2025-09-02 04:19:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fce22ae0-9d99-3c44-a977-03439c6edcdf | -22.94246 | -46.26983 | 2025-09-02 04:19:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c2eb5edb-a62f-3771-b4c4-86c8f78a447f | -23.23751 | -49.51915 | 2025-09-02 04:19:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88f44331-a2f1-3170-816a-14788334a6ea | -23.65408 | -47.41216 | 2025-09-02 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| a95309b8-a06b-31f7-9c3d-3960690caa39 | -23.65077 | -47.41154 | 2025-09-02 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |


[Clique aqui para ver as próximas entradas](README52.md)
