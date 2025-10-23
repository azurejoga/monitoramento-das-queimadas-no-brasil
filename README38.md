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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1bfd2ae-fec6-3f0a-898a-691f5564bdc4 | -17.6555 | -46.6523 | 2025-10-23 11:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 3ac85ecd-2d3f-3fbf-a137-1456755e49f3 | -17.6173 | -46.5906 | 2025-10-23 11:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 0c5abd43-29c6-3fb5-9e70-167c1c0f15bb | -17.5967 | -46.6182 | 2025-10-23 11:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 6ac4f985-3053-32e0-851f-a046f1a5f4a0 | -17.6167 | -46.614 | 2025-10-23 11:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 259.8 |
| c921a48a-e7b5-38e6-bdc6-785698b5277f | -4.20525 | -38.7743 | 2025-10-23 11:36:00 | TERRA_M-M | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 7d036be5-9b15-3bc3-b83e-3702c776caea | -4.20389 | -38.78355 | 2025-10-23 11:36:00 | TERRA_M-M | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 6ae27e1e-eb3a-3dca-a986-90dcef02c625 | -6.55292 | -35.58636 | 2025-10-23 11:38:00 | TERRA_M-M | DONA INÊS | PARAÍBA | Brasil | 2505709 | 25 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a57f4302-db0b-39c0-9602-b9f35867f943 | -8.58394 | -39.56863 | 2025-10-23 11:38:00 | TERRA_M-M | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 21b6f28d-592f-375f-9072-6ebd9c90896a | -8.81667 | -37.37917 | 2025-10-23 11:38:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a8a41696-2eec-3ac1-9daa-5548e68c3e85 | -5.06542 | -38.57496 | 2025-10-23 11:38:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| f0e00e48-f0e9-32cb-8382-bf28c1a8228c | -6.74935 | -37.97145 | 2025-10-23 11:38:00 | TERRA_M-M | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c5725a2f-a5a0-3059-890f-ebc8a2d90b55 | -7.95562 | -37.59462 | 2025-10-23 11:38:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ded7eacc-494d-3f3e-b54c-acf45143e831 | -5.18897 | -37.664 | 2025-10-23 11:38:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 2b541add-1a97-3119-b3c4-ea5a23656f71 | -6.77858 | -37.70596 | 2025-10-23 11:38:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e2df104c-bfb4-38f9-9c9f-fcb94e847dea | -7.63019 | -42.19363 | 2025-10-23 11:38:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 337fafdc-61b2-3e70-b37d-3cfc314e54a9 | -5.6707 | -38.66109 | 2025-10-23 11:38:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 71554c57-49df-3a21-816e-3144680656e6 | -10.23082 | -44.61767 | 2025-10-23 11:38:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 025ef409-684f-38ca-b226-17d6c628fcd7 | -6.25628 | -38.4404 | 2025-10-23 11:38:00 | TERRA_M-M | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5b1bfa4f-ea32-3d26-bfa0-7ffa77c16a60 | -5.18771 | -37.67279 | 2025-10-23 11:38:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 91352efa-4e14-3410-9a78-bbe0ccaf082b | -6.2227 | -38.60956 | 2025-10-23 11:38:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 24.4 |
| db4b0519-a311-3692-bf79-6b75dac3be13 | -7.39045 | -37.48723 | 2025-10-23 11:38:00 | TERRA_M-M | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 5441f891-2846-3b43-9a2e-955a7d1521b9 | -8.03656 | -38.51813 | 2025-10-23 11:38:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 71848cdf-1ce3-3e39-b8d5-ab287fbd5121 | -5.67973 | -37.31824 | 2025-10-23 11:38:00 | TERRA_M-M | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 177ba2c8-2de7-3a3c-851e-d40806f4758c | -7.14892 | -38.78328 | 2025-10-23 11:38:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 24e9c504-40ad-3ca8-a9c6-e165f8dbd004 | -6.77984 | -37.69715 | 2025-10-23 11:38:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 1a6db7cf-0631-3748-b771-7272f9fc3cff | -6.17394 | -42.6101 | 2025-10-23 11:38:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| a1165d75-020c-36ac-a5c3-265db76229ee | -7.95435 | -37.60349 | 2025-10-23 11:38:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6faed95d-a584-3145-9d20-5be6e9870db2 | -8.0454 | -38.51939 | 2025-10-23 11:38:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 4d46e834-0b13-3515-be54-b3a2105e8aa2 | -5.66431 | -37.87888 | 2025-10-23 11:38:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 54f89206-d548-3027-a222-55b0273932a7 | -5.96605 | -37.76899 | 2025-10-23 11:38:00 | TERRA_M-M | OLHO D'ÁGUA DO BORGES | RIO GRANDE DO NORTE | Brasil | 2408409 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f01e9c18-2925-3b7c-ba4b-ccb59a563e45 | -7.42552 | -38.78611 | 2025-10-23 11:38:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| bd6763bc-663b-3cb1-bf38-e22ff6e5f608 | -10.61642 | -42.29268 | 2025-10-23 11:38:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 6c11fbd3-753a-3edc-b85a-4d1b92225b28 | -6.34735 | -38.58456 | 2025-10-23 11:38:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d193872e-cfbf-3c9e-9c53-bca7eae56a2e | -6.43332 | -38.30512 | 2025-10-23 11:38:00 | TERRA_M-M | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 18.1 |
| c57a4d7f-a0c2-3bdc-ab19-d4bad05dfc16 | -6.43461 | -38.29623 | 2025-10-23 11:38:00 | TERRA_M-M | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 24.9 |
| ec94c072-0a41-3036-a6f8-161d3a916d30 | -8.33709 | -36.92975 | 2025-10-23 11:38:00 | TERRA_M-M | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ab278da0-c192-32dc-a101-fbce4677c066 | -7.15025 | -38.77424 | 2025-10-23 11:38:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 6a88780b-8fb7-3db6-9909-2bf9a4a4845b | -7.02041 | -38.83565 | 2025-10-23 11:38:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 58fdb829-7ba7-3e96-9f39-3bc831ec79fe | -7.16453 | -37.77613 | 2025-10-23 11:38:00 | TERRA_M-M | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 7.0 |
| bbd6f478-8ed0-330d-b820-168c5072dad7 | -6.17162 | -42.62542 | 2025-10-23 11:38:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| b1d84516-9b90-3de7-bd48-f94184d84758 | -7.38919 | -37.49607 | 2025-10-23 11:38:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 38.5 |
| af7464bf-ce08-3085-be9d-7f7b850896f5 | -17.6555 | -46.6523 | 2025-10-23 11:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 37d9a50a-89f2-3dc2-8e92-8288368c8e45 | -17.5973 | -46.5948 | 2025-10-23 11:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 148.3 |
| b7e2b884-5978-3776-ae92-378c28380a98 | -17.5967 | -46.6182 | 2025-10-23 11:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 193.5 |
| c06d6b39-1c0f-3067-8909-f282f0987ee3 | -17.6167 | -46.614 | 2025-10-23 11:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 9201790a-3b7b-3657-a6d8-f1fce3d0ee5b | -13.87872 | -44.32636 | 2025-10-23 11:40:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a7a6cecd-3c84-385f-bf71-e803db3cd34a | -14.85162 | -42.6363 | 2025-10-23 11:40:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f446698c-d376-3ee7-b33d-0902432beacc | -14.77414 | -43.444 | 2025-10-23 11:40:00 | TERRA_M-M | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 28c0364e-8508-3450-9f66-4a6fe4fae296 | -17.6125 | -46.63671 | 2025-10-23 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 130.2 |
| e15c433a-8695-35a1-8576-777116c825be | -17.46098 | -43.97314 | 2025-10-23 11:42:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ff1105f9-499e-3999-9a4b-33c716a215d6 | -21.39208 | -48.08426 | 2025-10-23 11:42:00 | TERRA_M-M | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 8aa07157-8cad-32f1-8b30-73c8f0430f2b | -20.13711 | -41.46703 | 2025-10-23 11:42:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| ee1be1fe-1a8c-3da2-9bfe-b4d030443beb | -17.61608 | -46.61702 | 2025-10-23 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 8c1335c6-8e92-3aab-b5d5-4fd45f6e0fb8 | -19.43932 | -44.18881 | 2025-10-23 11:42:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 44298e74-c597-3f48-9ec3-597d57bd25e1 | -15.14206 | -43.7896 | 2025-10-23 11:42:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3e93b9df-f766-3891-bcdc-aee925daa135 | -21.95528 | -42.9292 | 2025-10-23 11:42:00 | TERRA_M-M | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ed6a71ab-339e-3281-be61-f32bd213af8c | -17.612 | -46.63045 | 2025-10-23 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 702e2d45-8dad-358d-9c56-c54d2499dfd9 | -18.70765 | -44.45868 | 2025-10-23 11:42:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 38c04760-e0ce-3d5f-8dee-62f6f0e7debf | -16.0401 | -43.81371 | 2025-10-23 11:42:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fc557d28-89c0-3501-a481-8d0e065162f9 | -15.96593 | -43.83512 | 2025-10-23 11:42:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0e9acb85-4378-3910-a596-ab387eeb78a3 | -20.1357 | -41.4765 | 2025-10-23 11:42:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 71aaf3f9-7262-3d14-b632-03935adfa9a5 | -17.6029 | -46.60832 | 2025-10-23 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 289.2 |
| 92b8619b-c8f2-3e1f-803f-78efdf2d9ddb | -15.97296 | -43.82914 | 2025-10-23 11:42:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 17.5 |
| c11ba067-5ea9-3dc6-9435-f4c153db855f | -15.60059 | -45.90554 | 2025-10-23 11:42:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2b994cb2-f493-3fab-80eb-d6cfcd34fc06 | -20.54501 | -42.49001 | 2025-10-23 11:42:00 | TERRA_M-M | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ba9c56a4-29cc-372c-8418-6ace9064b7f9 | -17.61543 | -46.61079 | 2025-10-23 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 5de07cdf-e7ab-35ae-b82d-86dcb5ac93ca | -17.5967 | -46.6182 | 2025-10-23 11:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 162.5 |
| ba43bfd6-9010-34ce-87b7-bda86b444177 | -17.5973 | -46.5948 | 2025-10-23 11:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 2dde6864-3e08-3df1-8c6b-42872234a7e6 | -10.9234 | -50.1284 | 2025-10-23 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e91000fa-d3c3-390b-9706-74a3a5fe603e | -10.9047 | -50.109 | 2025-10-23 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 3481d1e6-6a1e-3b08-a1c9-42dc837b98e8 | -10.9041 | -50.1519 | 2025-10-23 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 3286d60f-b0b9-3da5-83b0-6e94c1c6b181 | -17.6555 | -46.6523 | 2025-10-23 11:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0712d12a-81f4-3ad8-9f5f-7b02ad1255a1 | -17.6167 | -46.614 | 2025-10-23 11:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 81b6e381-9158-39d2-8c05-46b2324f69b6 | -17.6173 | -46.5906 | 2025-10-23 11:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 9314629c-d693-3162-999f-4e81b2c68a87 | -17.5973 | -46.5948 | 2025-10-23 12:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 177a499d-18f2-3031-b1f6-c2b4e5d65dc0 | -10.9047 | -50.109 | 2025-10-23 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 7d3a1675-03d1-3a6b-9f94-b9083242af69 | -10.9041 | -50.1519 | 2025-10-23 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 42dcad47-d5cc-3e8f-a76e-fd66ed85fff8 | -10.9234 | -50.1284 | 2025-10-23 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d704cb70-2f9d-3409-abf0-eff731ea12f2 | -17.6555 | -46.6523 | 2025-10-23 12:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3679c2e2-6758-3c27-a1a5-0035b1c099ee | -17.5967 | -46.6182 | 2025-10-23 12:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 254.5 |
| 23514348-9104-313e-87a8-ed29cfe2f9b7 | -10.9237 | -50.1069 | 2025-10-23 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 0c6983ef-54a2-3e43-b79b-5dd99671512b | -17.6173 | -46.5906 | 2025-10-23 12:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 220.2 |
| c1d5ad0c-e2f4-30b1-9953-70c7188abf93 | -17.6167 | -46.614 | 2025-10-23 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 179.6 |
| b2ec9b6f-4449-3633-abe0-062926248fb1 | -17.6561 | -46.629 | 2025-10-23 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1bbd021d-cfe9-3591-93e2-d98fd96fa5bf | -17.5973 | -46.5948 | 2025-10-23 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 587fef3b-2380-3a9f-9411-f7750a73bccc | -17.5967 | -46.6182 | 2025-10-23 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 5ce3274f-3b98-38c8-a7c3-d964fe5f24bc | -13.3697 | -46.632 | 2025-10-23 12:10:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2fa5f8be-d309-3442-a17e-847db01f1e13 | -17.6555 | -46.6523 | 2025-10-23 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 9a240146-5a1b-323a-882a-eb24fd6d9985 | -17.6173 | -46.5906 | 2025-10-23 12:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 58cf193d-5dbd-3c74-a8e1-68399cdbb2d4 | -17.6555 | -46.6523 | 2025-10-23 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 133.9 |
| ca261381-440f-3b56-b3e8-df283045156a | -17.5967 | -46.6182 | 2025-10-23 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 266.2 |
| 3592a5b4-f6b5-3aea-920d-bc76a32fc481 | -17.5973 | -46.5948 | 2025-10-23 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 82b68ba8-6927-31e4-9836-73460e57aec5 | -17.6167 | -46.614 | 2025-10-23 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 183.8 |
| ea9c5af1-1624-33c7-81fc-df42645715aa | -13.3697 | -46.632 | 2025-10-23 12:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 70e0c99d-6631-3a39-941a-b30622466334 | -17.6173 | -46.5906 | 2025-10-23 12:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| efef7c40-58c7-35cd-b25f-db84724f5ce3 | -17.5973 | -46.5948 | 2025-10-23 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 07078336-5e36-370f-ae27-5f83cdac114e | -17.6173 | -46.5906 | 2025-10-23 12:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 115.6 |
| be5f7520-259f-3426-a8c8-27e8a3afede2 | -17.5967 | -46.6182 | 2025-10-23 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 339.3 |
| dc39bd45-faa2-3af7-b57b-330953429011 | -17.6555 | -46.6523 | 2025-10-23 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ecf04357-3763-388e-8126-ba20273a860d | -17.6561 | -46.629 | 2025-10-23 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 86.9 |


[Clique aqui para ver as próximas entradas](README39.md)
