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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f07d96ac-e5fd-335d-8e83-2ed92247ca76 | -9.7802 | -37.1077 | 2024-12-12 00:12:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 122b19e6-18f3-31ac-9b86-6d09a732265d | -4.5479 | -43.567299 | 2024-12-12 00:12:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49e7d884-0568-33fe-b1f9-596b85a43ca4 | -3.7776 | -47.0961 | 2024-12-12 00:12:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d29e4d6-15d8-3b78-ae77-9ac2881ac1ac | -7.4798 | -35.1758 | 2024-12-12 00:12:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1b82db8-e986-3194-8826-5e114207ce72 | -2.97 | -40.222 | 2024-12-12 00:12:00 | METOP-C | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cbb39b11-1d74-3483-a4a1-7c7913f9a7e0 | -10.1807 | -36.356998 | 2024-12-12 00:12:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 81fa2929-0b80-39e3-9b70-d71da97477a9 | -5.1475 | -44.3596 | 2024-12-12 00:12:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02480b8e-85ee-39ad-863c-bb769d9efccd | -3.8255 | -41.5667 | 2024-12-12 00:12:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a7dd70f6-b29a-34b3-be17-62103a624cc6 | -6.6193 | -39.179798 | 2024-12-12 00:12:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bd8ef070-8214-3b64-b2b5-d1b66ace3e3b | -5.1573 | -44.357399 | 2024-12-12 00:12:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77b1f613-27ca-3084-9d6a-d32de9805fe2 | -3.8271 | -41.573502 | 2024-12-12 00:12:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc945205-bef0-3f71-8c85-055f6fdc7bbf | -4.828 | -44.217999 | 2024-12-12 00:12:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a22ad3da-8346-3909-878c-eb087afe0b31 | -6.9613 | -42.996201 | 2024-12-12 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 30930929-d419-337b-9103-c6e5364ef64d | -4.8001 | -44.552299 | 2024-12-12 00:12:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36ba5ac3-92ce-3da7-b585-c34bad914c3a | -2.9662 | -41.822899 | 2024-12-12 00:12:00 | METOP-C | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10019b22-04ee-3711-b6d2-8f0883f99cf5 | -4.1842 | -42.416199 | 2024-12-12 00:12:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8c305779-f38a-3de9-8247-d4725c9cde7f | -7.4662 | -44.723701 | 2024-12-12 00:12:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 73b2c61a-cbb0-301f-a8f5-2d26f0063d32 | -10.8884 | -37.250401 | 2024-12-12 00:12:00 | METOP-C | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89e66a79-25a1-3afb-8847-a5b531c2a509 | -5.5967 | -39.442902 | 2024-12-12 00:12:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dbf17dd4-c4d3-3ed4-b108-2e095dc5dd9f | -5.1554 | -44.3489 | 2024-12-12 00:12:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b275eef-d76e-3389-839b-4e5ec5ac7e66 | -4.802 | -44.560902 | 2024-12-12 00:12:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fc3e58e-9e84-3e65-aa9f-a7d3f164fd74 | -6.1304 | -42.5494 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82583754-2ea8-331e-821e-881ff24cc534 | -6.9711 | -42.993999 | 2024-12-12 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a38eeaaf-33ff-3cd4-a2c2-b02178af9831 | -9.1236 | -43.1073 | 2024-12-12 00:12:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 439f43c7-f555-3c00-8643-a61eb8f25a5d | -10.0825 | -36.335201 | 2024-12-12 00:12:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| ca8f574c-946c-3db2-bdce-57d8d5597eed | -4.1776 | -42.432499 | 2024-12-12 00:12:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3154dc95-d99a-3c3e-80d6-4d0d57d9f84f | -8.3665 | -44.480301 | 2024-12-12 00:12:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c255606b-4517-3e97-83cb-502a748806ab | -6.1272 | -42.534801 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1ceacf9a-b3ad-3996-89c3-8b2ea99539ea | -11.213 | -40.005901 | 2024-12-12 00:12:00 | METOP-C | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c32b048c-61ae-3fda-98fa-c521ccdc6878 | -6.8871 | -40.117401 | 2024-12-12 00:12:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f4d3068a-24e7-3b89-bfd5-c619a51fdfab | -5.3485 | -44.2005 | 2024-12-12 00:12:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcc27cf5-f35f-30fb-bd0f-cfc88d3e62d3 | -6.9694 | -42.986301 | 2024-12-12 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0fbe38c8-d732-3964-8380-5db8d42456a7 | -10.0805 | -36.326599 | 2024-12-12 00:12:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 931ace64-881f-330c-855e-6842ff5ff36d | -6.91 | -43.5047 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f02a45a-a901-3f78-8700-b8e87cd8d36d | -6.056 | -44.054798 | 2024-12-12 00:12:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cea092eb-c024-30e1-91ca-0b401cdd3630 | -3.8173 | -44.1152 | 2024-12-12 00:12:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d0ef03c-dcac-3f19-9322-56747c9bbb79 | -5.9019 | -44.0093 | 2024-12-12 00:12:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88f6afaa-4a28-3d37-a299-cdb29fc5040e | -6.9728 | -43.001801 | 2024-12-12 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2640cc8-1285-39d0-aa3a-b9f050820a2a | -10.1766 | -36.339802 | 2024-12-12 00:12:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da104726-b279-30e0-b4d6-f972d5d0c510 | -8.9569 | -35.992599 | 2024-12-12 00:12:00 | METOP-C | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 693954a8-675f-3281-bb62-c65bc1d7b887 | -6.927 | -43.535099 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e666af0f-44d9-3345-a09c-bd43168d6ac0 | -6.9252 | -43.526901 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| febe8501-5693-3485-84f7-453bafb437a0 | -4.3899 | -42.142502 | 2024-12-12 00:12:00 | METOP-C | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53645c30-8ea6-3ee7-b54a-aa4fd67c166a | -5.0869 | -45.839298 | 2024-12-12 00:12:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb5fa82f-2625-3953-89d5-e42dc40eb659 | -4.5462 | -43.559601 | 2024-12-12 00:12:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb793c8a-aa1e-3d3f-b0d0-931765e438eb | -3.8961 | -42.554199 | 2024-12-12 00:12:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 669083de-8e12-386c-a3a5-51ada8541f40 | -5.8931 | -39.8778 | 2024-12-12 00:12:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 746c293f-5e12-3abd-a61a-6290bbf15fd0 | -7.8868 | -42.441502 | 2024-12-12 00:12:00 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06e5a873-eaf2-303a-94f0-38c9d1f07741 | -5.3466 | -44.192101 | 2024-12-12 00:12:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40ee3557-c75f-397d-bb5b-8f5c211ad0f6 | -6.4166 | -39.641701 | 2024-12-12 00:12:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d895e29b-be24-306e-8481-21daa1cfc4f4 | -5.9171 | -48.039902 | 2024-12-12 00:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c93194c-a106-373b-a4ee-3f955b417014 | -5.1592 | -44.366001 | 2024-12-12 00:12:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79ac1891-df68-3a68-b3f7-b12ef03ae850 | -5.3912 | -40.656601 | 2024-12-12 00:12:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 12c1af3a-c46c-3425-bdb3-7e789c7771f8 | -13.1765 | -43.564602 | 2024-12-12 00:12:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 196afc70-242b-3cf6-a25e-646171d48255 | -5.5983 | -39.450001 | 2024-12-12 00:12:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1431548d-2b54-37d8-8160-802cf255874a | -9.7881 | -37.097401 | 2024-12-12 00:12:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 1c9d74af-1fd1-3bfe-898d-a0f0c957cc2f | -5.9236 | -48.022999 | 2024-12-12 00:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71fc4b2b-6615-3f22-a3c5-f866271497d5 | -4.5075 | -43.616699 | 2024-12-12 00:12:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0e260f0-b830-3b18-b2eb-e28d7130558c | -3.2333 | -46.862499 | 2024-12-12 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c318ee5f-84a6-3720-a5c7-2dd348868bb7 | -5.3928 | -40.663502 | 2024-12-12 00:12:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d0409a3a-2d42-3dd8-a445-b6330d6bf75b | -5.5451 | -37.979401 | 2024-12-12 00:12:00 | METOP-C | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 94395020-d4b2-3038-9d9a-820feddad24d | -2.9716 | -40.229 | 2024-12-12 00:12:00 | METOP-C | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| be6846d0-1f56-37ad-a0ee-f78be2dc7e43 | -6.6882 | -39.254002 | 2024-12-12 00:12:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6ebefad0-5cd0-3a05-8b6d-2b4858520595 | -7.4771 | -35.165001 | 2024-12-12 00:12:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9f7515f-f4a5-3d3c-aaa4-4eb7872945ae | -4.3801 | -42.144699 | 2024-12-12 00:12:00 | METOP-C | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 016c8c25-2b3d-3367-9437-3fa9bc33b0a4 | -12.4079 | -43.799801 | 2024-12-12 00:12:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6716063b-19e7-3a84-ad39-3b94d59fcbde | -10.5885 | -44.965698 | 2024-12-12 00:12:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa2491ca-3829-37b1-8cb1-a688b14e2e59 | -3.6479 | -45.692001 | 2024-12-12 00:12:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b500989-d13f-3d4f-8f59-2645801a2904 | -5.9139 | -48.025002 | 2024-12-12 00:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba428205-c747-380a-9062-4dd5dfffe130 | -9.7783 | -37.099701 | 2024-12-12 00:12:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 6cd32da9-73a4-3dc6-8185-6b9c39f4a9dc | -13.1785 | -43.574402 | 2024-12-12 00:12:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3a9f653-7652-3037-8f24-b255f1ee81d9 | -6.9216 | -43.5107 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7095bd4b-ce97-3ba5-a51c-e50e81fcf7b1 | -3.952 | -41.4883 | 2024-12-12 00:12:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1dc91090-3577-3f81-96bd-5c174853b976 | -3.2358 | -46.873798 | 2024-12-12 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff8521e-72ae-363f-a563-4a04740ca698 | -10.8866 | -37.242699 | 2024-12-12 00:12:00 | METOP-C | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c58d0475-ab50-3e17-b00f-51435a2547ec | -6.119 | -42.5443 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60375c9c-0ad5-390c-8d39-98ebed889e5c | -2.8342 | -40.3041 | 2024-12-12 00:12:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 20ed10be-f2db-31db-bec9-9b9a2a33df77 | -5.8915 | -39.870899 | 2024-12-12 00:12:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8993d492-53b3-3ca8-8160-7e426ebd05f0 | -6.1239 | -42.520199 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| df64152f-08d6-3675-b27a-f2b24467182f | -6.0522 | -44.037998 | 2024-12-12 00:12:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b270a5d8-09fa-3df4-93c7-f3961950fc49 | -6.5838 | -38.449501 | 2024-12-12 00:12:00 | METOP-C | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| c31791c0-5ed8-30a3-b473-c8607794f7a5 | -6.4198 | -39.655701 | 2024-12-12 00:12:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3f8109fd-5ec9-3563-818c-eca142207861 | -9.79 | -37.1054 | 2024-12-12 00:12:00 | METOP-C | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| c5c9b919-f602-3ee7-8a8e-a42016a6ece6 | -5.1707 | -44.417198 | 2024-12-12 00:12:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8807bc1c-17b7-375a-b214-29d0f89bcec6 | -6.935 | -43.5247 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a498ea6a-a31c-3b2a-ac5c-a7f73ec6ec34 | -6.7142 | -39.188099 | 2024-12-12 00:12:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9dc52277-2bf7-3084-b71b-b97ca76a10f7 | -7.9877 | -35.099098 | 2024-12-12 00:12:00 | METOP-C | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cbb1112-7869-3294-ab43-08a35bd1849a | -5.0846 | -45.828899 | 2024-12-12 00:12:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4440ad79-33a2-3510-9146-7310d301523e | -9.3867 | -38.872799 | 2024-12-12 00:12:00 | METOP-C | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 474617ab-1574-3c8a-87a0-cc8a63fbbdc4 | -4.1874 | -42.430302 | 2024-12-12 00:12:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e85f6717-ff79-3466-a4cd-afd42593b677 | -10.5499 | -36.779701 | 2024-12-12 00:12:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 355c6b9b-3f08-3198-b611-fe8a3b6edb99 | -7.4704 | -44.742901 | 2024-12-12 00:12:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd6069f0-58d1-3b53-a22d-17694b30e9c7 | -3.8589 | -40.453201 | 2024-12-12 00:12:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f32b18cf-576e-3f30-8d06-1b7534763c8c | -6.9118 | -43.512798 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b62356ac-2d76-399e-ad58-4953b7ed5bad | -7.4291 | -44.741699 | 2024-12-12 00:12:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5ae7f3a-502d-34a9-bed2-3f968c263fb1 | -3.8459 | -40.4417 | 2024-12-12 00:12:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3852b8e6-7f2b-3d68-a7aa-76cb208d1a00 | -6.2871 | -43.846802 | 2024-12-12 00:12:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3055712-7f84-3fa0-81fa-91f97dc9e5ab | -5.8433 | -39.617199 | 2024-12-12 00:12:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d1485520-7dbc-34c9-b17b-5b3d3696f71c | -6.4182 | -39.648701 | 2024-12-12 00:12:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 23af309a-0766-33dc-93f3-5803a85aef9a | -6.9596 | -42.988499 | 2024-12-12 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
