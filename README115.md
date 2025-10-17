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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c3e8221-71bd-3519-b6c6-909758713e9c | -6.13354 | -44.29279 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a35c854-372b-33b6-bf6b-0402544717a3 | -11.09335 | -45.87594 | 2025-10-17 05:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 017a70e4-9f93-38b0-a748-b19033fc354c | -10.11598 | -44.60894 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9097c7d8-7078-349b-b89a-6f072d498f61 | -6.94445 | -47.71656 | 2025-10-17 05:44:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 28ce7139-9020-3c25-8625-c56c3f731abc | -11.47696 | -45.07993 | 2025-10-17 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6f4541f3-7979-30b4-ad20-cbc429cab513 | -2.8697 | -50.71757 | 2025-10-17 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 4248707e-63e6-306e-a362-afee54c06c05 | -6.58416 | -47.07015 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f5681228-b3ce-3251-97c5-e0b6e0f2c8e8 | -4.41204 | -43.40174 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 29d9fc6c-e9fd-329d-9442-a0523aaaa087 | -10.15495 | -44.5375 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9b86b707-b42b-3494-baa6-10b0229f18f2 | -8.46462 | -44.16934 | 2025-10-17 05:44:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6b544788-0ba9-3678-9417-4254e6e6e6ab | -5.79563 | -42.50251 | 2025-10-17 05:44:00 | AQUA_M-M | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a317be9b-4f2d-3277-b2b6-65fa04504118 | -6.21526 | -44.427 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bca3d510-8231-3a04-92e8-3f93d0af0b1c | -6.22437 | -44.42851 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 29659081-ec22-3059-b659-e0c92144e07e | -6.42327 | -42.56728 | 2025-10-17 05:44:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5991cb82-5fd6-31ff-8bc4-4ccc2876412e | -12.28852 | -45.62724 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0df5abc7-b253-33a6-9d3b-083fce36a8c1 | -6.14507 | -44.21804 | 2025-10-17 05:44:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 02c09645-b250-3e83-8562-8487bff83c39 | -10.10427 | -44.62587 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e23758a2-535a-3bf8-b183-85e658484210 | -5.89185 | -43.88609 | 2025-10-17 05:44:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba91133b-c6e3-3b0d-b167-d2ab2e6ecc76 | -6.94419 | -47.71108 | 2025-10-17 05:44:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| db913495-c092-30c9-a7c5-988501163136 | -11.74775 | -51.1669 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c3412365-897e-3686-9c89-912a193d3ffd | -11.75178 | -51.14426 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 22cf6b8d-6dda-3435-a47d-5e25318486d9 | -5.85555 | -43.87474 | 2025-10-17 05:44:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0f89013-3ba3-3be6-89fa-ea2b0ed05b59 | -10.14607 | -44.53607 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 33a4c4e1-a0e3-33bb-a23d-67e20a529ce0 | -9.7097 | -44.54949 | 2025-10-17 05:44:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a22d3e88-26e7-30f6-a0c8-e822c3d8c6b6 | -11.57721 | -44.05268 | 2025-10-17 05:44:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c46a8b93-7b3f-3871-bcc7-633a15f80a1e | -7.18327 | -42.36835 | 2025-10-17 05:44:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3891f702-de8d-3983-af5f-d119194dc26c | -8.73098 | -43.87313 | 2025-10-17 05:44:00 | AQUA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eb5bf975-c26b-3c4b-a10f-53620962a576 | -5.51485 | -43.86483 | 2025-10-17 05:44:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 910718af-4c22-33cc-96d6-edb2f839e929 | -8.8229 | -47.29971 | 2025-10-17 05:44:00 | AQUA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a567fc24-8453-3280-916d-dfb55470332a | -6.22112 | -44.14887 | 2025-10-17 05:44:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ca36d66-d93f-329a-b19b-b2d9d0cc5220 | -3.23681 | -45.96797 | 2025-10-17 05:44:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| f399bfdb-7205-3837-977a-23e3bc315fe6 | -6.99605 | -39.23004 | 2025-10-17 05:44:00 | AQUA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 0b1a1d2e-ffb0-38f1-9370-30ca89d9a57a | -4.38702 | -43.38215 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe5e8e1e-da4a-3a2c-a87b-291f528520c1 | -6.08993 | -42.38546 | 2025-10-17 05:44:00 | AQUA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 569a22e0-1941-39af-886e-31071b140999 | -10.25724 | -44.04664 | 2025-10-17 05:44:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f5d5102c-0f11-34dc-b6c6-4788cd6d76bb | -4.41343 | -43.3927 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e805b77d-5e24-3934-a57d-5bdd8acd3439 | -8.30918 | -43.42506 | 2025-10-17 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 87000a79-0680-383a-97ad-dea45bacd8b0 | -6.0332 | -41.90985 | 2025-10-17 05:44:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 60bf4034-257a-3993-b53a-934d16d6cf28 | -10.52839 | -49.5451 | 2025-10-17 05:44:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 66be525b-33bd-3f76-8d71-d49efdd04cd5 | -4.8137 | -43.19274 | 2025-10-17 05:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 807e9fe6-246f-3eea-aef5-0fcc392b977a | -10.01113 | -45.64033 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 18cf6a7f-f76c-3f56-a169-6d75466ac531 | -5.33728 | -44.47571 | 2025-10-17 05:44:00 | AQUA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f8efd24f-ec80-3ca0-af7a-5e64a13ad778 | -6.32041 | -43.62271 | 2025-10-17 05:44:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e9ec91e-f97f-3186-9682-b1f841f4ffab | -11.59557 | -44.07026 | 2025-10-17 05:44:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9b05115-b393-3bca-97c0-4a17c6ce831b | -7.46418 | -42.66049 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 360823b3-4e9c-3ef3-98c3-dd8b5892e79d | -10.06009 | -43.83136 | 2025-10-17 05:44:00 | AQUA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 59f8078e-6fc3-3aba-ac20-6136ad724cdd | -3.24727 | -45.96956 | 2025-10-17 05:44:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 01f903fd-79a0-3361-a409-036f3ea59fa7 | -6.94187 | -47.72579 | 2025-10-17 05:44:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a401a0a7-7082-3fbc-bc5d-2ec0e1463f12 | -12.1115 | -45.8736 | 2025-10-17 05:44:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 606543f8-92aa-32e7-834c-8f8384dd0753 | -11.96113 | -45.35608 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ea07e724-2e04-32c1-9e01-dc573e312399 | -11.36405 | -45.26685 | 2025-10-17 05:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c083fd35-30e8-359f-aef3-f60f2df35162 | -8.39637 | -46.2448 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c2aec1ab-9d99-3900-8f7d-b5b8a5647e77 | -9.71595 | -48.91191 | 2025-10-17 05:44:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c9cbb705-df76-320c-a9b1-9e3ebca678a9 | -11.47162 | -44.20325 | 2025-10-17 05:44:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ca1043d-3b26-3ce9-943d-672f346c2d00 | -8.52243 | -44.56945 | 2025-10-17 05:44:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5113f1a-b4e2-39e7-a835-95254469fd08 | -6.75973 | -42.35602 | 2025-10-17 05:44:00 | AQUA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 22cf439a-b0d4-39dd-9fda-40e1af135a64 | -8.31052 | -43.41624 | 2025-10-17 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| b5d62844-4d37-38fa-b9e3-18ce4738b0d5 | -4.40036 | -43.41848 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 811e1436-0a31-3344-b666-440fd88fe63c | -10.61773 | -42.31434 | 2025-10-17 05:44:00 | AQUA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b7a19d3e-deae-3c56-bb01-caea80b3034b | -18.09256 | -42.44352 | 2025-10-17 05:46:00 | AQUA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| da781e73-7fb7-3d77-b59f-100602b1cf6b | -13.43212 | -47.95542 | 2025-10-17 05:46:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 86042588-1816-3c00-9c00-78c3ea76d2f4 | -16.40189 | -41.95767 | 2025-10-17 05:46:00 | AQUA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 736d6fe8-2bbb-3d94-ae27-15246ace9293 | -13.49158 | -47.96096 | 2025-10-17 05:46:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7866b28e-c017-3d97-b363-2f9c8d601d13 | -12.42196 | -51.29412 | 2025-10-17 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 65b18b48-d008-33d9-bf00-83217a76cf23 | -18.09524 | -42.44971 | 2025-10-17 05:46:00 | AQUA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| da03e8cf-b3ee-3878-8be5-d410ae48adb9 | -14.87152 | -52.42644 | 2025-10-17 05:46:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 39fa24c1-2996-3e10-abbe-171181ea307b | -13.4195 | -48.58378 | 2025-10-17 05:46:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e162a322-b4c6-3367-a967-a352dd2a8a60 | -17.20025 | -46.96984 | 2025-10-17 05:46:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc531bdf-35c5-354a-b362-801f014498ba | 1.82149 | -55.71278 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 515c696a-f4de-3da9-bea7-08d9db4a890d | 1.8271 | -55.70591 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1d67ca5d-464f-3ccf-8663-b921efdf3972 | 1.74013 | -55.77732 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85aad151-4e40-391a-b91c-220aa82caaff | 1.7441 | -55.76644 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9a4ddc80-fe66-3e80-a01d-7edea1044607 | 1.74316 | -55.76074 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9b86b3e7-c9ed-32b4-b480-70277ade0b5b | 1.82296 | -55.71194 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16a46c8e-77ac-32c8-8d55-a9dc0f6bbfc6 | 1.73446 | -55.78402 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e64496f0-b661-3703-bcbd-e8d64a536dfc | 1.86087 | -55.66466 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83b0289f-5e7d-381f-b0d5-b2720312ada1 | 1.77944 | -55.89879 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4184a65-3704-3194-8807-ab3e46b4df23 | 1.87091 | -55.84766 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7c9fa27-fc10-3e11-a191-411128b7d46c | 1.82861 | -55.70506 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c6f7489-adb5-3dbb-aa93-6403fa4b2493 | 1.75068 | -55.76542 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 275c8b61-5ff6-3f4e-ab0b-9d37ca74ceae | 1.78296 | -55.92015 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 25ddf8fa-2a9e-3df5-ade3-c043768cab5b | 1.97895 | -55.93461 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 020c530a-724b-3ad3-86ed-d6155485c9d7 | 1.72789 | -55.78506 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 212661d2-7c90-352f-8b52-f94b4f46831f | 1.73356 | -55.77837 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b624a159-3a12-3478-855f-6d00acedc932 | 1.84862 | -55.67255 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5e02ffc7-2cc5-30dd-ade0-9908f2fdccfe | 1.84392 | -55.68505 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5d2683e-ce05-3f2c-ac7a-a5433e6d510a | 1.98543 | -55.93354 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11700d47-bab5-36a5-9235-a5f745e269d8 | 1.72253 | -55.79874 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcba32e1-2c4b-3ed5-8a21-6cb4f7221c0f | 1.82205 | -55.70627 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ce74f52-9c38-3cea-916c-891626ea5869 | 1.78977 | -55.88028 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8ecba167-9ff4-34e9-b8d8-0a148c6c3c27 | 4.5246 | -60.86099 | 2025-10-17 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 624ba3b0-53c1-3ddb-b541-0ced864c169a | 1.81911 | -55.72998 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bad479a-2265-3f33-9c6b-284ad5a0b550 | 4.52379 | -60.85611 | 2025-10-17 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac7678c5-448c-3528-8c7b-fe37f00b2cff | 1.74504 | -55.77207 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8ce8f69d-894c-34cd-9222-fa51d3ce6a2c | 1.73283 | -55.77972 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e6c781d9-6d54-3f3c-8a92-7a239c9503b9 | 1.8173 | -55.71875 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2b7dda7-01ce-33dc-81a4-b3e667e87087 | 1.82243 | -55.71839 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c44bdd04-4439-3d3f-8c84-8b8518f89dfb | 1.8327 | -55.69893 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5acbfc1-9b6c-3190-b02f-d340af894b9f | 1.82386 | -55.71757 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcb56602-fd56-3bb3-883b-af88cdba93e5 | 1.77736 | -55.92664 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README116.md)
