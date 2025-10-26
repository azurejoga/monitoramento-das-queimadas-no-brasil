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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4003cb85-ff5c-38b3-a317-71bee2131baa | -10.99147 | -44.86686 | 2025-10-26 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e2bd56d-16e7-30e8-97e5-ba143c8352f7 | -6.36349 | -38.3702 | 2025-10-26 03:40:00 | NPP-375D | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a1a5942-e2c3-3d76-90b2-076269bc5d8e | -5.16436 | -44.36678 | 2025-10-26 03:40:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5fdb8fb-ad39-3c0b-8578-7bb2ca4e35d4 | -6.21228 | -42.54607 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6352b58-8091-3a40-8fcc-808beea23487 | -8.15672 | -47.04523 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f44f48c0-8163-328f-b0f6-c1c1e6a28b16 | -4.80845 | -43.30761 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4737b86d-b23b-3a4c-a571-5da94f1f66f1 | -7.14623 | -44.8479 | 2025-10-26 03:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a3b0308-f752-35f9-a4b6-d8e4e2663fd1 | -8.82138 | -40.30659 | 2025-10-26 03:40:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f9eb88e-53fe-360b-a9bf-1781241fb6ec | -4.71239 | -46.43045 | 2025-10-26 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b42b88db-b7ce-38b4-81f6-25c99576e2a9 | -4.80913 | -43.30366 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fade804c-393e-31ab-a48a-32a7c8870ea8 | -6.47057 | -47.55538 | 2025-10-26 03:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05b0b47e-4abb-358f-ba8d-2dbbf30af9c0 | -8.33399 | -48.18615 | 2025-10-26 03:40:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 899382c2-99a5-3091-ba03-777d987cd109 | -5.13176 | -41.19348 | 2025-10-26 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 29259c3e-97a7-3399-a039-e65f08456cf7 | -6.50064 | -38.73804 | 2025-10-26 03:40:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 60a597ca-86ee-3761-be28-b5ec0274dc85 | -6.09009 | -47.06392 | 2025-10-26 03:40:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29b18092-846f-3293-82a6-030aa9889916 | -5.5477 | -41.39506 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ed7a31dd-b383-3d66-8ba3-6af8746c2bb8 | -10.61508 | -46.60625 | 2025-10-26 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9fcec35-1b44-367f-9398-32f6018d5f8c | -7.00523 | -41.07089 | 2025-10-26 03:40:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8060f8e0-272e-38c8-9f27-60f39f574981 | -6.44525 | -45.73934 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2687109a-f1a1-3350-9531-7189237d7b52 | -7.08904 | -39.56689 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61c0de74-1ba6-331f-89c6-ca807b1faeb2 | -4.72346 | -47.42807 | 2025-10-26 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 375661f4-8d40-35f8-bc03-20cb6f0b0082 | -6.0213 | -43.31073 | 2025-10-26 03:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6141aee3-0f1e-33d1-9266-05ac7ae1dbc4 | -8.151 | -47.03863 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 337f1416-2b89-3cfb-b90b-f7cd96c5c279 | -10.19005 | -44.90769 | 2025-10-26 03:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1511a595-2ce7-3b6d-8b4f-3adf625bac48 | -7.14537 | -44.85268 | 2025-10-26 03:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c49087c0-fcd1-32cd-86c4-995326ed9348 | -10.41583 | -44.49961 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4874875d-97c8-38f4-9666-4faace65207e | -6.73496 | -44.15343 | 2025-10-26 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 463b9271-d3b6-3af1-a6e8-48e49b3b0c11 | -10.55864 | -43.8549 | 2025-10-26 03:40:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8cb2b52-9849-3e84-a9da-3e2047710969 | -7.78839 | -45.3905 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48d94438-07e2-39fb-a262-9cdeb6453cff | -6.09133 | -47.05714 | 2025-10-26 03:40:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5893615c-f3c0-35a1-817e-7873cbd2ff78 | -5.0979 | -43.20698 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8f0a45c-0507-33e6-9531-0ef2f34722ed | -10.88223 | -48.03579 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14d1af6b-5beb-357e-87cb-e723c4fea7e3 | -7.64639 | -42.17353 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bd90020c-831c-3390-849f-103e5fa8a39b | -11.53366 | -47.09969 | 2025-10-26 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82c52017-c8a2-3395-ae7c-d2e7a1170e86 | -9.23939 | -45.58315 | 2025-10-26 03:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8d39ea8-3e96-3aa5-ba62-a1547ea26f1f | -6.43895 | -45.73734 | 2025-10-26 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdd889f2-4b51-3b43-a001-7819b6d0277a | -10.42208 | -44.49706 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5621bebd-a51b-333c-a05f-6b6cfbea9073 | -8.32674 | -48.1851 | 2025-10-26 03:40:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69c3faca-0876-3a77-98d8-c90296a5edbd | -6.52509 | -37.9831 | 2025-10-26 03:40:00 | NPP-375D | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad777f38-c07d-3364-a08a-745368545ed2 | -8.53645 | -47.20875 | 2025-10-26 03:40:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c431fe9d-12eb-3422-9c4b-539a6d2e95f5 | -8.71863 | -48.01505 | 2025-10-26 03:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80a44544-bf24-30ec-95bc-7695e2eba197 | -9.4382 | -46.33409 | 2025-10-26 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4eb8d723-29d8-322b-bf5c-c9ac7c6ca783 | -6.43261 | -42.02555 | 2025-10-26 03:40:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 454c6687-39d9-3536-ba85-fb7630639695 | -4.89595 | -43.25482 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6b524bec-c881-305f-833c-70364bbe3420 | -8.48865 | -44.72363 | 2025-10-26 03:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5848dbba-facf-35ef-a59a-720c176ef414 | -6.73626 | -44.15158 | 2025-10-26 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 285ad349-6129-3a8f-8393-0308286f9d96 | -6.50969 | -38.60738 | 2025-10-26 03:40:00 | NPP-375D | BERNARDINO BATISTA | PARAÍBA | Brasil | 2502052 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a616de3-27a5-30a1-a70c-d29016af3baa | -10.94603 | -48.07025 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca303b36-de2a-3d69-bd16-f65fc0f1b2fb | -9.51997 | -40.30951 | 2025-10-26 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2a9e0ced-0193-3f86-8a4e-ba3fd3c95a50 | -6.57697 | -41.45433 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 99473e8d-852a-3d92-a093-42281a201564 | -5.61247 | -42.6697 | 2025-10-26 03:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 630d5ecf-75af-3e27-9724-241434cd3d26 | -7.34767 | -42.44752 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4745b501-f3da-3e87-9754-37dadc38106c | -6.70332 | -42.05433 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8eec115e-eb2a-33c3-ae38-7c24681c3b6e | -6.11098 | -41.7513 | 2025-10-26 03:40:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dc09fdc8-bcdd-3315-b30f-b1f464b5c6cb | -8.33603 | -48.18406 | 2025-10-26 03:40:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d848276-ccec-3aba-9ef2-e4e1da703c71 | -8.03009 | -41.20039 | 2025-10-26 03:40:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1535440d-1db8-39d2-97a2-921df8cae7c0 | -5.8822 | -43.93554 | 2025-10-26 03:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32fcad74-1c04-3efc-a682-d48f962c6700 | -7.79969 | -43.16491 | 2025-10-26 03:40:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3882949a-f8c1-36b6-bf26-a031ddf2dc4f | -10.43163 | -44.49841 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a724ac3f-18cc-38de-a3e1-30529e4a2873 | -6.06192 | -42.1486 | 2025-10-26 03:40:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35720c87-600d-3858-921a-09750ac47a45 | -6.5712 | -41.45879 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0df74482-2b11-3d38-848c-ae02ed8d7482 | -6.78474 | -45.41519 | 2025-10-26 03:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b465b96d-1fad-3e47-95b8-c6291463ef34 | -7.7417 | -36.48008 | 2025-10-26 03:40:00 | NPP-375D | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df8478aa-3e60-33bd-9458-f2027263a439 | -7.81726 | -40.25867 | 2025-10-26 03:40:00 | NPP-375D | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b99c2d35-143e-355a-b302-98446d2326a6 | -6.6988 | -42.05047 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 459b178b-2035-3378-ab9d-78c965a9fd13 | -11.18136 | -41.05199 | 2025-10-26 03:40:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a0ee402-71fc-3f59-b98a-8b4c0e8e3a71 | -6.70538 | -42.04279 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2560f5ae-23ed-3472-ad60-96fe58653a05 | -10.77819 | -40.31575 | 2025-10-26 03:40:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8df694bb-2040-31a5-88d3-b989df559df4 | -6.4486 | -42.33457 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc9a41be-82ee-396e-86b3-a6615e478ed7 | -11.74763 | -44.46857 | 2025-10-26 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b0a1af2-5b2f-320a-a3df-97e6cf26bd27 | -7.78311 | -45.38476 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3fc2afc-bf21-3e30-b46b-192f59b0a8e5 | -8.44995 | -45.1249 | 2025-10-26 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8624c3e0-fe25-3cd8-b36a-3b53b72fcd08 | -12.02305 | -43.63347 | 2025-10-26 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f253e5a-8fb6-3644-87b6-988c761fac69 | -7.8434 | -46.43515 | 2025-10-26 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc2315c8-f4d7-3015-b3fe-56b8be9af75a | -4.90491 | -43.23685 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f40f3fce-267e-3f24-b496-f7ccfbfe0695 | -11.48094 | -43.24591 | 2025-10-26 03:40:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fcfe8056-4a33-3ea7-b4f6-6d591508ca0f | -10.41294 | -45.32631 | 2025-10-26 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b10795bc-5112-3f4f-b81b-63543db36bd8 | -7.29245 | -38.13832 | 2025-10-26 03:40:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f713f73-818c-3ec7-af8f-d6d66f5866e4 | -7.19347 | -39.40821 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 32be7623-b6bd-301e-913b-6ae27b8aa037 | -6.12714 | -41.71796 | 2025-10-26 03:40:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6684647a-f0ff-3883-822d-fc0c88b52677 | -8.14916 | -47.04179 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f5a005f-fdba-3827-be32-99df697c0bae | -10.60884 | -46.60461 | 2025-10-26 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 515bb5e9-ab82-3074-a918-efb055f87a8a | -11.67439 | -43.90468 | 2025-10-26 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ede82e7-b1b8-3b74-a650-60f91bd0879c | -7.05247 | -43.88236 | 2025-10-26 03:40:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbe7643a-4602-3000-a5ed-e354048cc9df | -6.15907 | -43.13379 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5d298355-5f13-3ef2-93d6-0610c0272664 | -7.80029 | -43.16158 | 2025-10-26 03:40:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25427bf1-cd91-3806-bda4-f705cb9c4e82 | -5.54865 | -41.38957 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0dc47753-0600-3146-8947-1e2b78f3e52a | -7.64153 | -42.31582 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cf5d10c-2c50-357b-b915-afd936d095ba | -10.77769 | -40.31659 | 2025-10-26 03:40:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d84c54aa-449a-30bd-a055-63a689655586 | -6.79833 | -45.41174 | 2025-10-26 03:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c72d748-5631-3df8-8275-498ecdec2e94 | -6.16548 | -41.55742 | 2025-10-26 03:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| af6cada7-04a5-3fdb-887d-5c58888e7423 | -7.22044 | -35.11927 | 2025-10-26 03:40:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| caa7f1e4-6b7d-31c3-aacf-a3600b29d34e | -5.89594 | -41.30909 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20c24be9-317d-38af-a2a3-5c9c6b5a6b60 | -7.64758 | -42.17099 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3354be53-39b4-36a3-9626-253c1a9b523c | -8.10789 | -44.49768 | 2025-10-26 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76b70f04-4737-3066-8c54-43394edc487d | -4.89365 | -43.23484 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7cd41994-7110-371e-838c-d61262ffe8ac | -8.15223 | -47.76279 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54255869-01e3-3180-92e3-5fbebc3009cf | -6.55077 | -41.58592 | 2025-10-26 03:40:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88530cf5-8672-34a2-ac9c-a62cc15c1700 | -7.52621 | -40.58605 | 2025-10-26 03:40:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| baef8efa-ae09-3945-90d9-d225f9b399a8 | -8.07105 | -42.0655 | 2025-10-26 03:40:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
