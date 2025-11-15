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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4affc9d-1271-3e13-8141-b260d4c64d3c | -6.0346 | -39.490898 | 2025-11-15 00:18:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ed0aee77-fb36-3d5e-9523-cbfd3e8619b4 | -4.6233 | -45.660198 | 2025-11-15 00:18:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 124512c1-3923-31da-a66b-9257e50793fe | -10.0385 | -44.266201 | 2025-11-15 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d700c31b-cdb4-3404-aaf2-2af0ebcb3fef | -3.9859 | -47.6754 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6e12c07-594c-39ac-8091-c55bb88990c8 | -4.6769 | -45.852699 | 2025-11-15 00:18:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5baf5318-3d67-3df4-bc82-ef3b169ad0a7 | -9.1275 | -47.117401 | 2025-11-15 00:18:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cab2412-e738-337c-9f7e-cb23175d8f2d | -10.1796 | -44.395199 | 2025-11-15 00:18:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dec063a0-63f8-3beb-aba8-b3d9c5d843ad | -3.3342 | -45.284599 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56b84ea1-7bd4-3251-a28f-448cc9f2c4c9 | -8.5613 | -46.055302 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e420d89e-a040-376d-8910-0eac9be39094 | -5.3094 | -40.939602 | 2025-11-15 00:18:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f666d5c-a637-3f09-809b-b09fa4b8bbab | -10.5518 | -44.9282 | 2025-11-15 00:18:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9d29c959-5a7f-3d5c-9b7d-0a2ae5d0fcf2 | -4.4199 | -43.397701 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0353ed59-3eb2-39f9-94af-3901e31850e5 | -10.6999 | -44.522598 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 877e0673-08a6-3e51-a924-e7e6b87f2272 | -10.3515 | -48.729301 | 2025-11-15 00:18:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6d60a09-2e69-39f6-80e7-8bab444e5240 | -12.6673 | -46.7743 | 2025-11-15 00:18:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6097b801-5670-3434-a68e-6f3d3e1b1b62 | -2.7285 | -45.2929 | 2025-11-15 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2304429b-d8b4-3304-8f27-78c034ee0110 | -17.261801 | -42.652599 | 2025-11-15 00:18:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b979aa2-1663-3e21-a934-2f8cfd2df823 | -4.4773 | -42.881802 | 2025-11-15 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50ff6d9f-7561-3cd5-9cda-e1e08d319ca3 | -5.7189 | -42.3592 | 2025-11-15 00:18:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 970da77e-51ed-3426-9acf-6959252cf445 | -3.9041 | -45.801399 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a014ada-360b-3d31-81a8-e1190bac42ca | -3.7898 | -45.978802 | 2025-11-15 00:18:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8af6546a-60ba-3026-8a1c-1d2ceae2973e | -7.4502 | -42.764198 | 2025-11-15 00:18:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7bf1d0c4-1d38-3173-9c78-70dcd7d29199 | -6.1107 | -44.221001 | 2025-11-15 00:18:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b7271e8-a8fc-3a4f-af3e-ed6525087066 | -12.145 | -46.662399 | 2025-11-15 00:18:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cf2a9bb-c391-3d48-9588-8fd8757ec559 | -4.5342 | -43.220901 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0977e4a1-8a09-3459-ba64-4044fba824a1 | -10.4207 | -44.9384 | 2025-11-15 00:18:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d54be17e-8090-3c78-990a-2d3ee50bb956 | -4.4557 | -45.646702 | 2025-11-15 00:18:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58e63691-9450-3245-bcee-c010510b81e6 | -4.6071 | -41.740398 | 2025-11-15 00:18:00 | METOP-C | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cae16ceb-cd1d-3a17-9dcf-9e179d0763cd | -7.5299 | -41.172699 | 2025-11-15 00:18:00 | METOP-C | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4fe62cb5-38f3-344f-a9a0-1542c3c7a38a | -4.5464 | -44.589699 | 2025-11-15 00:18:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad1310e9-a3f0-3700-abed-c927685c4d86 | -7.9765 | -35.205601 | 2025-11-15 00:18:00 | METOP-C | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fdc052d3-701d-3720-b2b7-e3277bb03e71 | -4.9104 | -44.787601 | 2025-11-15 00:18:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 587148e6-421b-3448-967a-ead77d913a77 | -8.2893 | -43.839802 | 2025-11-15 00:18:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3086f47-c1d1-3747-b89c-2768d0b22cd5 | -5.7315 | -42.730202 | 2025-11-15 00:18:00 | METOP-C | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c275eb9b-fcb1-3cba-855a-48448a7776ab | -10.0465 | -44.2561 | 2025-11-15 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 02b0391f-9f31-344f-8d0c-5a0aebd1ab6f | -5.0333 | -43.6022 | 2025-11-15 00:18:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f45f6e7-59c5-33cb-91cf-e6f86f581ed6 | -4.7511 | -44.948399 | 2025-11-15 00:18:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0d613f1-15b8-35bd-a5f3-af1ddcf2e9fc | -4.4187 | -47.592098 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc6a1b41-508e-37d8-bda2-3ed741c88951 | -3.9976 | -44.259201 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82b7152f-f711-361e-bd06-439e394250ee | -13.7394 | -43.6348 | 2025-11-15 00:18:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dceabc79-b23e-38e4-a637-21440b9c0488 | -4.0402 | -48.1021 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d726a48-5235-3d4c-b05e-4b87058635f4 | -5.0903 | -47.707199 | 2025-11-15 00:18:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d61276b-b26c-324e-ba82-22518ee020f1 | -4.273 | -45.520802 | 2025-11-15 00:18:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b12ed60-b1c5-37d6-88cc-c81ca5d651e3 | -7.4637 | -42.5508 | 2025-11-15 00:18:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9b857d7-d220-34a6-a1ec-faedfe870230 | -12.8299 | -46.424198 | 2025-11-15 00:18:00 | METOP-C | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 556930ed-bf12-3e89-a741-e25f2312d6ee | -6.2029 | -43.261501 | 2025-11-15 00:18:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69b39aab-7d37-3822-b52b-51a51a8c70ca | -9.1496 | -45.177399 | 2025-11-15 00:18:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1debf6bc-1d47-314a-8f20-4447e934a834 | -20.2024 | -41.8223 | 2025-11-15 00:18:00 | METOP-C | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b64d262c-8eea-3e13-9616-4d3af61be862 | -10.1061 | -40.890701 | 2025-11-15 00:18:00 | METOP-C | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 03caf06f-8ef2-3b27-967c-604f8ba9226b | -9.6742 | -37.082901 | 2025-11-15 00:18:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| ab5b287f-ee37-33b5-8b05-d9aa2d8ab66a | -6.1478 | -48.045101 | 2025-11-15 00:18:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32c868ce-8c4b-3015-a7ea-cee0b158a665 | -6.5325 | -39.063 | 2025-11-15 00:18:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6d7f2dac-a246-3073-a8e9-efcc3f67188f | -5.2248 | -44.355701 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c99e5f22-58be-3ec1-ad6a-1495aed2c2ec | -13.5442 | -43.729301 | 2025-11-15 00:18:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| abf68316-6eca-3da4-bd23-4b40353b40eb | -3.3114 | -45.6833 | 2025-11-15 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7129a3-0a22-3aec-b283-b7daee172e76 | -10.7061 | -44.503899 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4326397f-b71a-3312-a694-1df55c408ba3 | -4.4373 | -43.654701 | 2025-11-15 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08a20031-791c-3497-b9be-7bdec3d797f2 | -9.8135 | -44.223999 | 2025-11-15 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9e2194d-6a54-3cb6-8209-6d678f6556c2 | -7.9896 | -35.2169 | 2025-11-15 00:18:00 | METOP-C | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 186e727a-62f5-39c2-b3bf-b8e5753d4ec8 | -12.4348 | -47.884998 | 2025-11-15 00:18:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f825a2b-6815-3d88-b9e5-8ed9b9917de6 | -3.3593 | -49.503101 | 2025-11-15 00:18:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4cb56d3-566f-3d20-bd0b-8bc1ce72de7d | -6.309 | -41.8293 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 022c9e59-1fe1-313f-90e8-fda7540638a4 | -9.4909 | -47.2892 | 2025-11-15 00:18:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ecdf61f4-d77a-3590-a26f-a3e83bafea08 | -8.1885 | -44.8214 | 2025-11-15 00:18:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b7ff93c7-02ef-3073-b146-b03782c4d315 | -4.5455 | -43.225601 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 654d952f-bd36-3bfa-b825-6c3a0cf29eef | -8.102 | -40.879398 | 2025-11-15 00:18:00 | METOP-C | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 577929d5-9c99-34eb-abb2-5d9c9ed76548 | -5.5212 | -41.767799 | 2025-11-15 00:18:00 | METOP-C | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea9b847c-fd08-3709-b9b4-0c6734e27ec8 | -7.0547 | -48.313801 | 2025-11-15 00:18:00 | METOP-C | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e01bb16a-f8d6-387d-bda7-248a8cf770a4 | -10.4392 | -45.0714 | 2025-11-15 00:18:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4e594132-6667-3a4b-b441-2cdd115a70a2 | -7.7603 | -45.162201 | 2025-11-15 00:18:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28791b28-77b9-356f-ab82-5769f7e55e33 | -6.1009 | -44.223202 | 2025-11-15 00:18:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d99ef57-ef96-3ee1-adbc-cb8401b070e7 | -2.8584 | -45.3661 | 2025-11-15 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f2fb216-ca46-3e9c-91ef-66a923753e1b | -3.3495 | -49.505199 | 2025-11-15 00:18:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 976ebd2e-742f-3456-aab2-1481b3f7e135 | -4.4274 | -43.656898 | 2025-11-15 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b204b6e4-ec09-3961-98fe-dda06fe33683 | -5.3256 | -43.029701 | 2025-11-15 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9279aa9-6866-3caf-ad47-72e296ca2776 | -7.102 | -39.070499 | 2025-11-15 00:18:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2beca557-0200-38ea-aabe-21d93732d5d7 | -4.5857 | -44.308102 | 2025-11-15 00:18:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7119ecb9-456e-30d9-b60c-d5276f5307ba | -15.4537 | -39.238602 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ab810a9-3cb7-3e5f-a5bd-4018a7776da8 | -8.5772 | -46.081402 | 2025-11-15 00:18:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e76f8fa-919d-379c-8b69-30bae41a56cc | -5.5763 | -46.152 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c14c384-c4b9-35d3-aa1d-3f1c7bdf7ec1 | -13.8977 | -42.890999 | 2025-11-15 00:18:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 56302383-0865-35b7-b414-fe9460cf189c | -4.6517 | -46.841599 | 2025-11-15 00:18:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc39701-dc11-371b-9b47-c0261ca71477 | -11.8432 | -49.184799 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cff65f04-16a9-34bf-b268-d682a0d49ed9 | -10.4244 | -44.9557 | 2025-11-15 00:18:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bb327a40-c41a-3c9f-9bca-4ea24b99bbdb | -6.5228 | -39.0653 | 2025-11-15 00:18:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6a835234-f112-3b61-8ece-d00b42c68ac4 | -11.7016 | -48.3778 | 2025-11-15 00:18:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12ea6657-afba-3514-96e4-5f680aea6439 | -8.6269 | -39.938301 | 2025-11-15 00:18:00 | METOP-C | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7f11d87b-d697-3fb3-9c6f-728547b1bb10 | -3.6606 | -44.8162 | 2025-11-15 00:18:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a93b6035-841e-3ff9-824b-ab37a8ebe71c | -6.0095 | -41.9622 | 2025-11-15 00:18:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a49d98f4-14ec-3a7d-8bf1-f917acb38996 | -4.6401 | -44.730598 | 2025-11-15 00:18:00 | METOP-C | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 076a5f59-381f-39d0-9543-b318cf561781 | -4.5923 | -41.765701 | 2025-11-15 00:18:00 | METOP-C | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b29815ee-84d9-3c54-8ab6-bcc9a3bb9e95 | -4.0949 | -50.052898 | 2025-11-15 00:18:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a830cdcd-9f74-345d-9e18-8c17a4bdec70 | -4.9062 | -38.685001 | 2025-11-15 00:18:00 | METOP-C | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 128d5fac-a434-3466-b939-c13e2385b8c1 | -4.2116 | -45.476898 | 2025-11-15 00:18:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6458854-cb9f-3c0f-adcc-81393ce76de0 | -9.1458 | -45.160301 | 2025-11-15 00:18:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34c2a47d-546b-378c-bacc-690c860f6933 | -13.8879 | -42.8932 | 2025-11-15 00:18:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d1731d22-499d-3bbc-902d-68a1eb3d52b6 | -6.0327 | -39.4828 | 2025-11-15 00:18:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 68d55aa8-043a-3d3e-bbbd-ff3cc61c2c19 | -5.4219 | -40.6684 | 2025-11-15 00:18:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 395b9a70-afba-363b-8571-515048449d36 | -11.1663 | -48.1432 | 2025-11-15 00:18:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d188d1c-e94f-38d0-b0f7-402b5b549dac | -4.5393 | -43.1982 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
