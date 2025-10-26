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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64a7a103-0954-3cc4-9ad4-e5d0410f8004 | -11.66169 | -41.44555 | 2025-10-26 03:40:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c1eb999f-485c-3c3d-be09-54a35dee0d35 | -6.38993 | -45.78696 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78953f5c-ce0c-3ba0-9d87-66555390a596 | -6.57605 | -41.45975 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cd3be409-3075-3868-ab43-c076d8c019a8 | -11.4815 | -43.24294 | 2025-10-26 03:40:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 333cc576-e7c4-3697-8ca8-56312a1a2143 | -8.04428 | -41.1175 | 2025-10-26 03:40:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1452a0ac-3afd-391a-b9fd-a8f82e5cb15d | -5.15672 | -44.37479 | 2025-10-26 03:40:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f0f4015-5127-3b3c-8a7c-f1979843e982 | -11.75306 | -44.46961 | 2025-10-26 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d871eab8-8c35-3aa4-8d9c-a9bdf02f1a46 | -5.46581 | -40.87682 | 2025-10-26 03:40:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 64a853d4-dc5a-3a55-9ff1-efd1c6fc2c95 | -9.43182 | -46.33304 | 2025-10-26 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b09a0b4-bed2-3180-abcc-deab917bed77 | -11.5326 | -47.10501 | 2025-10-26 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a14cf420-7999-39b0-b465-c4d0fdfcc257 | -5.10346 | -43.20825 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1f01a9c-c408-38e1-aaa0-52b5ff0323c6 | -11.46918 | -46.11967 | 2025-10-26 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d1d832c-79d8-312d-8997-af9fe9440d0b | -6.43994 | -45.73188 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12e360fd-f4cb-3cbd-8957-a8fc946f12d1 | -6.07732 | -42.15141 | 2025-10-26 03:40:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e797811-3ed8-335d-8fa5-4072d7225e0a | -8.0493 | -46.74828 | 2025-10-26 03:40:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4d02016-4056-350a-b0b6-25767cf58b00 | -8.45076 | -45.12061 | 2025-10-26 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ef933941-90e4-34ee-9a47-cfd56db943cc | -7.10793 | -47.94832 | 2025-10-26 03:40:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4270378a-d221-3aa0-a6b6-4ac419cf09fc | -10.83128 | -47.62312 | 2025-10-26 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf641185-4eb2-3e44-83cd-d2a4d2f98e30 | -6.46915 | -47.56283 | 2025-10-26 03:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cb5c142-69d5-3bf3-826a-5539ef35980d | -7.79025 | -45.38972 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14417616-2b6d-3bf0-8f62-b2eb81601ec0 | -17.38577 | -45.51701 | 2025-10-26 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95642894-f230-3839-9558-623e8ba6a9f5 | -13.53354 | -43.01502 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| aedbfe30-81f9-318a-86ab-067cc4ff0f12 | -15.58801 | -43.21 | 2025-10-26 03:42:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5081449a-1dec-3f33-9477-cae8ffb0ae40 | -12.56762 | -43.97407 | 2025-10-26 03:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1443399d-d985-3740-9bc6-a5f034ce2534 | -12.13637 | -47.00757 | 2025-10-26 03:42:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f84ca7b-00c3-3ec1-b06d-1b1a2a4c7df4 | -15.04612 | -46.20704 | 2025-10-26 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6b4031f7-bec3-3319-95a7-72511d8d9069 | -14.43658 | -49.9557 | 2025-10-26 03:42:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d2164bd-65ee-3cc2-b051-c8dc470e35fd | -14.58217 | -44.13968 | 2025-10-26 03:42:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bacf4b76-0db5-3fb9-a5da-71d5dd3e2f0d | -17.31976 | -43.65958 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07b7670b-627d-3b36-ad30-144fa4faf11e | -13.53442 | -43.01354 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c6f0b075-88ba-3df8-bef1-62b64099947b | -14.76849 | -44.97149 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02717589-e1bb-3a18-9060-f270b84cc4bc | -13.09028 | -43.05174 | 2025-10-26 03:42:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 347693a3-4779-3ea7-99ef-f25e603e22ff | -15.35107 | -42.87691 | 2025-10-26 03:42:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 416116ac-1f33-3d65-803c-32e587a46f06 | -14.1592 | -44.76099 | 2025-10-26 03:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 747b503e-e649-379e-9811-12195f7dcee9 | -13.00822 | -44.01537 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed6fa633-2a82-328e-b332-efd54515b171 | -14.7678 | -44.97488 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0819308-3999-3f69-a203-d6a723980e37 | -18.20045 | -42.17033 | 2025-10-26 03:42:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c917a88e-966e-3024-a5e5-f23254fb9a99 | -12.17457 | -47.02296 | 2025-10-26 03:42:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7d1a004a-cc05-36b5-9b9e-0cd81c07d961 | -17.42155 | -46.87649 | 2025-10-26 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23630996-8bc9-3ff5-9bc1-6a6d07bc4535 | -12.17294 | -47.02163 | 2025-10-26 03:42:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c5405e11-392b-3177-b06e-d49f5fbaaa03 | -12.50503 | -44.33128 | 2025-10-26 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e6d5159-acd5-335f-abcd-00181e25fe1d | -14.43256 | -49.96305 | 2025-10-26 03:42:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db6cb1c3-efb6-32c9-8d61-10c05f33187d | -13.55025 | -44.00955 | 2025-10-26 03:42:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ac9350-135a-3148-bac4-2ee951e63e5a | -17.31606 | -43.65382 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5821020c-625c-3de4-922c-ad46cf81a497 | -15.3357 | -42.8082 | 2025-10-26 03:42:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f7483af-92a4-3bd2-88d8-e9d49681fbbe | -13.54967 | -44.0125 | 2025-10-26 03:42:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8aa53ab-b6ec-361c-916d-ec0b934a46cd | -17.38053 | -45.51593 | 2025-10-26 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e2b0f9f-397f-36e6-818c-b46cf5c41624 | -15.58703 | -43.21511 | 2025-10-26 03:42:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0424cb4b-483a-3560-8674-c05738b2e36c | -12.12979 | -47.00758 | 2025-10-26 03:42:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4846b6b8-1340-3b82-b643-2b03f9b8db62 | -14.77242 | -44.97938 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a800a6a4-f821-381b-bb4b-2ba6cf65c4b2 | -15.21809 | -47.93819 | 2025-10-26 03:42:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25468781-ea4b-3a61-986e-b7ade4eecc33 | -16.61299 | -44.57921 | 2025-10-26 03:42:00 | NPP-375D | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e7a81f0-9a0c-3bd2-8d89-73d9126e3455 | -15.12294 | -43.29764 | 2025-10-26 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71578600-b440-3ef2-a924-75d151e9d225 | -12.84356 | -48.64332 | 2025-10-26 03:42:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 686730dc-1d86-3b91-a7d7-b7eae74c8bf1 | -14.77451 | -44.98238 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57702324-dd78-3221-85b3-74c5d29bec18 | -15.60228 | -46.78945 | 2025-10-26 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 166d352c-6a07-3b4b-9632-aeb1b767e92f | -16.61802 | -44.58008 | 2025-10-26 03:42:00 | NPP-375D | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed4331e-de23-31ef-89a7-61bd2e054039 | -12.49972 | -44.33024 | 2025-10-26 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fd20a4f-d0d4-3a0c-9e08-d90e6fa9ff72 | -18.58155 | -44.03642 | 2025-10-26 03:42:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39e2a856-4bb0-30a7-95a9-3cabb4c6fd55 | -13.55302 | -44.01071 | 2025-10-26 03:42:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cb16770-b8dd-3331-8e85-b492c94d17ce | -13.40084 | -43.01849 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3000f517-9d91-38f3-9033-f1691362c775 | -17.85057 | -44.11357 | 2025-10-26 03:42:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43e1acdb-6002-32d9-90cb-72bf6388d752 | -12.85026 | -48.64548 | 2025-10-26 03:42:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ec5fe2d-85e2-3d6b-a65c-cc01c29f505e | -14.92636 | -43.45012 | 2025-10-26 03:42:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b272bf97-23cd-30ea-8d58-d6b43c970a4e | -14.77771 | -44.98055 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1fbe777-3910-3ba2-83a2-69cc66ff34fb | -14.43482 | -49.96336 | 2025-10-26 03:42:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49692840-ef25-3070-af1b-6eb61102f938 | -13.84732 | -44.36303 | 2025-10-26 03:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c9db5ab-337e-3a9d-9c84-7c1b12490b1f | -17.32075 | -43.65458 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f6ae7383-7f42-38fe-874a-b2bd50707ac7 | -14.16363 | -44.68193 | 2025-10-26 03:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 746b10d6-e94e-339b-81cc-70147a13688c | -14.7731 | -44.976 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f15b922c-4eab-3e07-b0d4-f84d4547a97b | -13.54036 | -43.00535 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 6b7dd140-c435-3647-a3f2-0331ba125bce | -15.10937 | -43.2653 | 2025-10-26 03:42:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b806dc7-bf33-3ad2-9da7-2386a40a55d1 | -14.17196 | -44.33624 | 2025-10-26 03:42:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4313e094-fdc3-380b-9005-4c1fe5c23606 | -15.33386 | -42.81784 | 2025-10-26 03:42:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee63e015-d773-36a7-9f3f-ff5954e77f7b | -14.77055 | -44.97441 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c36e5ef3-e5c5-3e47-92ff-ad8996b140cc | -12.17437 | -47.01453 | 2025-10-26 03:42:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9e5d10d0-068c-3de6-ad2a-01416212cbc6 | -14.44137 | -49.95718 | 2025-10-26 03:42:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2afbaa3b-79e6-3ffd-b682-96fa2ed9a100 | -15.20827 | -47.93092 | 2025-10-26 03:42:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2434cd72-784c-373f-896b-38cff8d2f115 | -18.47785 | -44.42958 | 2025-10-26 03:42:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 558bbb50-d71c-31cf-807d-4454a7babd86 | -14.51058 | -43.00291 | 2025-10-26 03:42:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 5188221d-69df-3985-af8a-6136c8a0d148 | -13.5364 | -43.00281 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 79942d3a-fb72-345b-8493-f2dad9c7bc0b | -12.00696 | -46.78042 | 2025-10-26 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6750de03-55f7-3d24-bc21-955c5569ea2e | -13.9452 | -41.43758 | 2025-10-26 03:42:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f6b0e79-ec5b-39fa-830e-5dadcda40c9a | -13.00596 | -43.85602 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b61200be-18c6-30d4-9f4e-3a927da120fd | -17.37601 | -45.5114 | 2025-10-26 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecded22f-94d3-3ff7-84f0-2afd528af879 | -13.00724 | -44.01688 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f6d8399-0abc-3407-993b-7bf015892c38 | -14.58718 | -44.14087 | 2025-10-26 03:42:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 054b62a7-02cd-3fab-bb3b-19ebef14ff98 | -17.31706 | -43.6488 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b477c04-ce51-36e4-816b-fec88813e32c | -13.40412 | -43.02028 | 2025-10-26 03:42:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5b8269cb-7724-3945-b628-818b138095de | -14.77518 | -44.97898 | 2025-10-26 03:42:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da01ba0b-63e6-33a4-9bea-8687448c84aa | -15.21417 | -47.92566 | 2025-10-26 03:42:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f6598d2-056b-3164-805a-296789511f14 | -17.43135 | -46.8863 | 2025-10-26 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c21309bc-af28-305f-8f98-6da669647368 | -14.50888 | -43.00676 | 2025-10-26 03:42:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| f772cb5a-f5e3-33b7-a8b0-cfb636e5d6ae | -12.84326 | -48.64505 | 2025-10-26 03:42:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 435d1f37-6a97-37e9-948b-ee11cd1e6d06 | -15.83023 | -49.08073 | 2025-10-26 03:42:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4b3c139-e413-31c9-a2ef-d088d6811577 | -17.37672 | -45.50801 | 2025-10-26 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2747c1fb-9adb-314a-afb4-341753cf7853 | -12.99835 | -43.813 | 2025-10-26 03:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96b02c5b-aa0c-3bde-8c4f-cca8786d2eab | -14.44196 | -49.96503 | 2025-10-26 03:42:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 994be2e7-221b-3f70-8a15-76dfb34eaac7 | -13.53156 | -49.55051 | 2025-10-26 03:42:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5a8f494-98cb-3e4f-b806-68ce99acfeaf | -17.31421 | -43.65167 | 2025-10-26 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README12.md)
