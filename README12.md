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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41ff4060-9d74-3149-ba55-860260e974ad | -7.0757 | -44.93998 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d615ef5-5a74-3f51-b87c-3e030bc6647f | -6.60959 | -43.88683 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4902b5a5-3819-3ab9-9e86-23699b958cb8 | -7.36273 | -39.17514 | 2025-08-13 03:47:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59076b76-5fa8-3f22-b093-436a25a59647 | -6.63996 | -43.21778 | 2025-08-13 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5eb189f2-6940-39d6-9419-a94743ac0a74 | -6.12408 | -44.71401 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 90879963-d5ea-39c1-9521-65d4396152ce | -8.78719 | -40.55726 | 2025-08-13 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 180562b7-1553-3931-86c1-f9cdb1474f21 | -2.90214 | -48.25155 | 2025-08-13 03:47:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9169adb9-ee65-390d-8ef2-8b1b33eb9f28 | -8.07671 | -42.55742 | 2025-08-13 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d2b0d16-c792-3436-82d1-85a6628c9891 | -7.56075 | -37.18795 | 2025-08-13 03:47:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0def6d24-14c9-33bd-89ea-88ba5f24ee56 | -6.61038 | -43.88212 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f426f67e-0f5e-30d2-8001-904cd4eb000a | -6.60892 | -43.88956 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 94bd21fa-ae01-3fa4-acd3-a0a3aeb7a916 | -7.15498 | -44.38765 | 2025-08-13 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7928678a-8640-367c-bdb3-151e0af2fc6d | -6.44782 | -44.55675 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b67bca32-e90c-3fd3-b4ed-2625e0dcddd2 | -7.06278 | -44.36095 | 2025-08-13 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96cc7a03-c44f-3123-a295-a50e07a207a8 | -7.06065 | -44.36386 | 2025-08-13 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f87a9fc4-75ea-3157-8e66-41137bf2e664 | -6.12895 | -44.71495 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b7b5b86-4c23-3615-bb62-95a3f58d9c80 | -8.47955 | -38.99126 | 2025-08-13 03:47:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd0389a6-c7d4-378b-9f53-a9aede6fea88 | -6.58578 | -44.55639 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5afe6e2-9c29-3165-bcda-b2029a7d96f0 | -6.58955 | -44.55892 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feb1e7ab-706a-3ae2-a95d-a05a965b1449 | -3.88435 | -42.55723 | 2025-08-13 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1079c2f3-38f6-3c84-9166-bfcac0ce57b5 | -6.55024 | -44.01394 | 2025-08-13 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27775d13-8cc1-31f7-9948-0fe517b7849a | -6.59054 | -44.55744 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28185140-c227-38e5-b60d-1dea5d7c12c8 | -7.07474 | -44.94563 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73318539-71e7-3911-98b0-0dccc9446192 | -6.61433 | -43.88565 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6c462a03-21da-3ac0-918f-843c6456a009 | -6.6135 | -43.89041 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 11afde1a-48f6-3c94-a7b2-56a58c412af5 | -9.33073 | -37.98163 | 2025-08-13 03:47:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30e4773b-f002-3604-bbde-be0ea6b590c1 | -7.07279 | -44.94179 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 131624ba-f965-3485-9778-9d00aad1a9d8 | -7.07078 | -44.93931 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61c49e45-34de-3785-916d-9c7e00b92f68 | -7.06533 | -44.36482 | 2025-08-13 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6602741-d6ab-387b-9078-bce6a9421169 | -7.48289 | -43.93074 | 2025-08-13 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7dac91f3-b3a8-3abf-83de-d964a9aa36e5 | -9.37087 | -40.70396 | 2025-08-13 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 75998761-32b0-3270-9a7b-9d34f6f4ad8a | -7.11009 | -41.22682 | 2025-08-13 03:47:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1c9d5b3-48a4-365d-b531-256d9e590b47 | -7.39346 | -39.68063 | 2025-08-13 03:47:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7756ebb7-b575-308a-bddc-2f73d782f654 | -11.75869 | -48.19207 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f8e4735-66d3-3349-bc20-b6169c9de75a | -4.17291 | -42.45071 | 2025-08-13 03:49:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 08258d3c-9071-3f31-b8fc-4e776e9a990a | -14.12228 | -44.31812 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 415337fb-3187-3ec4-8649-464f16a3f2a8 | -12.53803 | -46.97158 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46bd8b11-b4d6-394b-9e37-4bcb43d2ea26 | -11.75942 | -48.18837 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 99dbc5e5-f667-3b31-9411-1fa4f0ed7be6 | -13.62695 | -46.91858 | 2025-08-13 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0147a68c-c0f4-32ed-9c9b-770f959adc54 | -10.96713 | -49.57821 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3349c7de-248c-3157-a97b-2f2cf76a480e | -12.5081 | -46.96249 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2bfd921-0946-352b-84dc-61fcb4d75790 | -12.67214 | -46.96331 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 217636f6-2c67-3709-bf90-f714e54a0cc1 | -15.09088 | -51.36285 | 2025-08-13 03:49:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03a1e56a-d566-3622-b985-42c6ebbdc325 | -5.32015 | -45.21977 | 2025-08-13 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b37797-d7af-3759-ac0f-9730c6916ca9 | -16.38691 | -50.88873 | 2025-08-13 03:49:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9133d396-6d55-37bc-8f8e-63a5a82f503d | -14.11899 | -44.32104 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7dc9ea4b-6760-395a-897f-22c853d979a9 | -12.67155 | -46.96635 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07a5b622-4214-38fd-ae37-69a9aa346d57 | -15.09207 | -51.35747 | 2025-08-13 03:49:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2261f04c-02b5-34c9-bd1b-81fd7cdbc5b6 | -12.29931 | -50.00864 | 2025-08-13 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b789bc4-3037-3f66-856b-52e1e2f2bcec | -14.71684 | -42.49654 | 2025-08-13 03:49:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bed318a8-bffb-38d3-a35a-826571ffc679 | -13.63205 | -46.91888 | 2025-08-13 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ccf0961-a9d0-340c-bd5f-fde662e7c412 | -13.29557 | -39.86621 | 2025-08-13 03:49:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 603fcefa-ba0b-3c48-8958-4b3632dd36a3 | -14.27864 | -44.58728 | 2025-08-13 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5302bdd-3d0a-3aa9-ad27-364ecde691c8 | -10.37177 | -46.6347 | 2025-08-13 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25d7e8dc-f380-3dd3-82c2-ebd86dbe4185 | -11.76054 | -48.19339 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8fb9f42c-cb5a-34cc-872b-de5012aea1cb | -11.76124 | -48.18968 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3b95c274-26e9-33ac-bfc9-0fcdec20d887 | -15.09326 | -51.3521 | 2025-08-13 03:49:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f9ba02a-48b6-3d5c-9f68-d2143f9b0b9b | -6.12192 | -44.71362 | 2025-08-13 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 506131fa-b4c4-3b19-9d99-25ccb6b632cb | -4.39824 | -47.63061 | 2025-08-13 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c41a71f6-5146-38d5-997f-c9eadaf4df02 | -13.57848 | -46.95418 | 2025-08-13 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7037c06-20bf-3529-a849-7fcc4c24883f | -10.96098 | -49.57688 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b96bfa5a-5001-3739-bfb1-992f56046cc5 | -5.99302 | -40.38543 | 2025-08-13 03:49:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed139e1a-bf25-3e5b-bcaf-44edde5d0f19 | -12.14612 | -48.02088 | 2025-08-13 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75291011-1382-36e2-9614-73c3027dfbb4 | -12.49673 | -46.96679 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 074db709-b321-333e-bcfd-bd70293f2100 | -12.49164 | -46.96582 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9f2a262-8dbe-3f06-86e1-74a05a502fb5 | -12.69149 | -46.97206 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a029b457-655c-38eb-803b-c14954967e25 | -9.8416 | -47.82001 | 2025-08-13 03:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| efb31263-4299-3c41-932f-950c6245c975 | -11.765 | -48.18948 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 02164687-e046-3b1d-bde7-f5777a0bcf95 | -10.96809 | -49.57322 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d04984b4-5871-355d-a29d-78f337fb5e5f | -16.26752 | -47.88352 | 2025-08-13 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0bdb0a9-5a50-3046-a3be-b67c3ca8bf88 | -13.52897 | -47.63061 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6d2ecfd-86c7-37e7-acc2-6b6ffba7a75d | -15.09007 | -51.35979 | 2025-08-13 03:49:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b3cd2609-7b83-35e4-b8f8-ea5a8fc24ad0 | -13.76625 | -42.61937 | 2025-08-13 03:49:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5dbc81aa-96ca-3f1c-9c33-64c1bfd486f3 | -12.53745 | -46.97469 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0729f48f-f0d3-3275-9f35-7d9fab6e36cf | -9.77318 | -48.37229 | 2025-08-13 03:49:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b4b563ee-81ef-313c-8694-bbd7253d1375 | -13.54057 | -47.62671 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa9f0e6b-a721-3585-b3a5-9bad92d3b956 | -10.96538 | -49.5812 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c33b4f5-e855-3616-856c-99e54adcf201 | -11.76352 | -48.19692 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d42c947-0f7f-3e0c-9fd9-c14fced77922 | -16.39848 | -50.89385 | 2025-08-13 03:49:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a953d049-9c9e-3172-b665-65e966191a18 | -16.40049 | -50.88681 | 2025-08-13 03:49:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b48b66e9-4450-33d3-b8e4-9b3fdfe8ead3 | -13.57895 | -46.95173 | 2025-08-13 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecc960f9-9bdb-3dac-b47c-4657b95970d8 | -12.58259 | -47.05772 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16a0625d-02af-3914-811c-e6d11800f16f | -9.71369 | -49.47601 | 2025-08-13 03:49:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b218ede-5742-3371-94dc-2b9bf32b216d | -16.50594 | -47.85212 | 2025-08-13 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c41a08fa-d979-301a-845a-13a68f5955ba | -11.90598 | -52.5383 | 2025-08-13 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d21662f8-6fdb-3050-9c21-88d6c51ce6f1 | -4.22411 | -47.22036 | 2025-08-13 03:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd049fc8-4c34-3da3-9661-56c0218d2ad1 | -11.76682 | -48.19079 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e3a81f7a-9144-3bb9-943b-5430d133d8f2 | -10.34069 | -50.81595 | 2025-08-13 03:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e088069-8407-3892-985c-7e6c6cd43d13 | -5.44843 | -43.57382 | 2025-08-13 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2de7cfcf-c0d2-3ae4-a43b-d9b59f4cbb1f | -14.11882 | -44.31341 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6c5fbaa-effd-3aad-aa3e-a040daffd7f3 | -3.5835 | -47.533 | 2025-08-13 03:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ff5845-2211-335c-a4a7-84b4464961e6 | -9.7074 | -49.47499 | 2025-08-13 03:49:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93452621-9764-3da0-9945-192452bd4dd8 | -12.68698 | -46.96818 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ea5d6fa-2c91-3291-99e0-5a503d5aa92f | -12.42662 | -48.69882 | 2025-08-13 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 662224f1-22ab-3caf-bad9-0666fb488614 | -12.30447 | -50.01491 | 2025-08-13 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc3b635f-bf38-36df-9b16-023d332fc9af | -10.96194 | -49.5719 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 66af98a8-c427-3797-a498-4edf5d03b05a | -10.96905 | -49.56828 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90e67bf2-a467-3ca4-809d-668644bcbb28 | -13.53994 | -47.62991 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e02e7426-f680-3196-8a4e-e7a4cd7fa689 | -10.37124 | -46.63754 | 2025-08-13 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51a9acad-3240-389b-bcb3-6f7a0d25d14c | -12.2113 | -45.46593 | 2025-08-13 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README13.md)
