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
| a43a1bf2-985d-39c3-864f-576d57ee420c | -3.50658 | -43.3551 | 2026-09-20 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45fb83e5-b5d2-3649-81cf-ef5cf8a7d476 | -4.84669 | -40.52258 | 2026-09-20 03:42:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9db6bb5-35bd-3369-b1e4-e0e93ab45a63 | -5.66815 | -45.30227 | 2026-09-20 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11569a87-f808-3a2a-881e-bf0a1bb31e7a | -5.79079 | -47.3682 | 2026-09-20 03:42:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f1696a0-dd66-37a5-8993-b60a1e18fc75 | -5.1026 | -47.51136 | 2026-09-20 03:42:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ffd92bd-9194-3597-bc76-3991615c64b2 | -4.68805 | -46.40042 | 2026-09-20 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 925deba2-52c2-37b7-a241-83437c08c648 | -5.45508 | -44.31504 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2fe1b56d-52d2-3601-b292-f05171f4e376 | -5.64761 | -43.37259 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 670cfa71-8672-38da-a7b8-e28cf918a33e | -5.41348 | -44.28005 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf1072ab-057a-39ae-be7d-a991c8c9deab | -5.3486 | -44.83233 | 2026-09-20 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26fcf905-2a78-31a4-a3e6-37c9e9cff89c | -4.84727 | -42.83748 | 2026-09-20 03:42:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c90eac22-3b97-3a5c-b16f-99021cafe81b | -5.40648 | -44.28913 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 546595f0-90b3-30a7-96b6-f9d5486924d9 | -5.40394 | -44.2718 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fb6bef5-3bea-347c-8ce0-c797474dacbd | -3.71134 | -39.43642 | 2026-09-20 03:42:00 | NOAA-21 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f2b14732-7f62-390f-9145-c715f8414eff | -4.77628 | -37.74528 | 2026-09-20 03:42:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 617c809a-ef48-34d9-b0c2-141167587b2c | -5.4598 | -44.31947 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 255b6469-7037-3b57-a7d6-a775c0648572 | -5.66711 | -43.41125 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2180bbda-7dad-3da0-b47f-5ab114c097ef | -5.23579 | -47.58441 | 2026-09-20 03:42:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b0ea6519-01b5-352c-8f69-5c1ed5a57f16 | -5.22623 | -37.65589 | 2026-09-20 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 408ea658-b554-3cda-862a-5b37eaf41b17 | -5.41241 | -44.27713 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61106b63-508d-30ea-8606-937d3a924610 | -6.41605 | -43.87823 | 2026-09-20 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc7b020a-0844-33a8-9c94-baf1678704bb | -3.71067 | -39.43839 | 2026-09-20 03:42:00 | NOAA-21 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 406b6092-8123-35d5-b0b0-ed8835ab0106 | -4.80654 | -45.7721 | 2026-09-20 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1fa1070-3d86-370b-bdda-d041819c39f9 | -6.22555 | -44.69136 | 2026-09-20 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c4319b5b-a480-3453-8ade-fe9901004634 | -5.11242 | -37.68684 | 2026-09-20 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d4d8dcf-c3d5-3118-8ed5-40f6bdc12e0a | -5.40451 | -44.26842 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8e82fff-40b0-32a5-842d-23e8ea935c6f | -6.21476 | -43.76066 | 2026-09-20 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5e5830c-e025-3d2b-a1a5-5921244d8127 | -6.22493 | -44.69486 | 2026-09-20 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8530df18-681f-329a-a5f1-1bb779f1ffc8 | -5.10539 | -37.68573 | 2026-09-20 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 85583a82-d9e0-3e8d-b6ba-aff064df9301 | -5.75723 | -43.69357 | 2026-09-20 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1a378e4c-8d65-3fcc-8507-76822f7dcb8a | -5.67154 | -45.3012 | 2026-09-20 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d39913b-8728-327e-a343-094fd7deb93c | -4.84829 | -40.52632 | 2026-09-20 03:42:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2fe8335-59a9-3d87-a37a-2c2585e6011d | -5.55279 | -45.54516 | 2026-09-20 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c78f12de-51df-3d53-935c-576df12c0913 | -3.58845 | -47.35627 | 2026-09-20 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e6a9250-bc93-3152-a1a0-e954bc291087 | -5.46039 | -44.31602 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d2eb7b5d-f530-36f9-81cf-26c1ca3dc8e8 | -5.40649 | -44.27967 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e94825dc-7997-32ea-b384-9f4b71b9e5dc | -5.40268 | -42.94915 | 2026-09-20 03:42:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 060ea738-b49c-388d-a1a6-0463e8ebb54b | -5.93151 | -35.62169 | 2026-09-20 03:42:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6774874a-fa95-3d20-b8a0-9cfa3c40e137 | -5.79176 | -47.36279 | 2026-09-20 03:42:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 68cfea62-99a9-3523-993f-69cab19fd0ab | -5.35416 | -44.83307 | 2026-09-20 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d99887f-939c-3b0b-be45-cf6c8ed6014d | -6.28563 | -41.77294 | 2026-09-20 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a5de83b-9277-3719-afa5-9516290e8936 | -5.24761 | -38.17308 | 2026-09-20 03:42:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 507251f6-3589-373e-8383-96db096ddcf3 | -5.34988 | -44.825 | 2026-09-20 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e175cbe-275b-3e14-8d59-30fd46423d4b | -6.25863 | -42.72803 | 2026-09-20 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5439641f-d177-3896-af18-c14d4c36e3a2 | -5.64213 | -43.37465 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01a1fe7f-616c-3796-9c3b-70d639bab627 | -4.7283 | -46.13132 | 2026-09-20 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64b79c7c-7f2c-3e32-9453-c55dd698c942 | -5.82683 | -44.13234 | 2026-09-20 03:42:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d06a210a-a5c3-35fe-b22f-6eb1e06ab949 | -6.41089 | -42.81251 | 2026-09-20 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dbcef6cd-172d-37b9-af7e-051ad71d9d55 | -5.41067 | -44.28705 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73a2a264-e898-36d7-8bf8-6177ad5cd127 | -6.35956 | -43.37055 | 2026-09-20 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 92d0c512-5459-3fda-8173-bf8c44f04a7d | -3.68539 | -38.81595 | 2026-09-20 03:42:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 529fa0f6-246a-3070-a4de-24288177ace1 | -5.66314 | -43.40462 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b16db10-e1ec-3bc9-a703-44851f9b2d34 | -6.15396 | -43.83977 | 2026-09-20 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3103aa6-dfaa-378f-94bf-1c6d5d756db6 | -5.31676 | -45.2484 | 2026-09-20 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a06e0ea0-d31c-3d60-ae6e-3c5c30582ed3 | -6.41158 | -42.8162 | 2026-09-20 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d98208de-bf5a-3544-a929-c456c274234d | -3.59211 | -47.35882 | 2026-09-20 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a2e73eda-8594-3a4e-9e0e-ffbd53be78f7 | -3.04643 | -46.92687 | 2026-09-20 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3082496c-def1-3088-8506-28140971756e | -4.1013 | -39.07309 | 2026-09-20 03:42:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25c9c788-cea6-3e1c-931b-70eaa10a5155 | -4.31742 | -38.49085 | 2026-09-20 03:42:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bda25e72-1d18-3654-83f2-a5dc877a9924 | -3.56739 | -43.48084 | 2026-09-20 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af7f2892-c815-3988-b9a9-dec1086bf470 | -3.38251 | -39.20367 | 2026-09-20 03:42:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d9562955-b2ea-3d15-949b-b54b34955241 | -3.50854 | -43.3564 | 2026-09-20 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd26f077-2612-3a4e-bb85-487dd376d350 | -6.28488 | -41.77731 | 2026-09-20 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19d71095-d98c-3697-bc08-701f23de9c2b | -6.69467 | -35.52733 | 2026-09-20 03:42:00 | NOAA-21 | BELÉM | PARAÍBA | Brasil | 2501906 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 574fdc12-5fa0-3d38-8db5-32b62d8b481d | -5.40759 | -44.28253 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e7e2fb-7e47-302a-a0c0-8bb9eec4d97d | -5.66762 | -43.40835 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43d68e0c-1603-3a28-a3c3-4e37d8dfe025 | -5.31613 | -45.25205 | 2026-09-20 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e0961a2-ea2b-348b-aae9-b19a62e2cd34 | -5.40927 | -44.27256 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bd22ccc-5ec5-32d7-898c-988e0caeaf8f | -3.56843 | -43.47455 | 2026-09-20 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a949448-6436-3ad3-bb94-7a82b279d796 | -6.31069 | -41.75902 | 2026-09-20 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 279521e0-a80c-3838-b4b2-02a78e904825 | -6.19254 | -41.41024 | 2026-09-20 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41643065-d5e1-30f7-9e9a-e7df8d2440cc | -6.36054 | -43.36491 | 2026-09-20 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a6f37c1-893c-3c17-bfa1-72e79af63bd7 | -5.93205 | -35.61823 | 2026-09-20 03:42:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ad2439c7-07ea-3eca-8012-2d4e9a3397d4 | -5.4146 | -44.2734 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f67e9e6d-beeb-32a3-a718-b0d144d483d1 | -6.36063 | -43.39366 | 2026-09-20 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d255487-81e1-35aa-b0cc-1e128225bc6d | -3.34559 | -42.76609 | 2026-09-20 03:42:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb7b4a62-17de-35c5-812a-54ea0555810c | -5.66757 | -43.37568 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce56b2bf-a716-3494-9014-1d2bfd7917e3 | -5.66772 | -43.40546 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 397e64da-e267-306f-b0bc-d6d998edf1e2 | -5.413 | -44.27379 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6090450f-060b-3e88-b35e-52d7b923790a | -3.34964 | -42.77248 | 2026-09-20 03:42:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 22155c58-388f-3d06-b6d2-43812075aa56 | -4.81417 | -45.77513 | 2026-09-20 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2eda9e0b-780c-3ede-b089-1c7fe51f48e4 | -4.81163 | -45.77773 | 2026-09-20 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69e152be-7355-33d3-95c9-0e5f3c0e4514 | -5.40766 | -44.27302 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 481e6fb0-4134-3781-a906-1aba6dde1d48 | -4.56773 | -42.97289 | 2026-09-20 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48bb5ae9-046b-308a-ace5-ea907cbc2867 | -3.68466 | -38.82057 | 2026-09-20 03:42:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f27d5eb2-6da7-3763-8574-0c79282cd483 | -5.66675 | -43.41127 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97d3e528-51da-3590-9cbc-42ff08a6d2fb | -5.66813 | -43.40543 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4cd78de-9b74-31cf-a237-636aeebb54f4 | -5.93482 | -35.6222 | 2026-09-20 03:42:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3e489a6-a08c-3743-ac01-92df988d6cc2 | -4.02018 | -44.06775 | 2026-09-20 03:42:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 090c1a7b-bd4a-305f-9c7f-1c83ae80bb30 | -2.82273 | -46.71075 | 2026-09-20 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 920dae3f-8a94-31ae-9719-6149b816b4b0 | -5.67088 | -45.30505 | 2026-09-20 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45a1183e-8374-3386-892a-974011762812 | -2.82919 | -46.71185 | 2026-09-20 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a16e91f8-c5ed-35f3-ad82-94d1ac7d35c0 | -5.41183 | -44.28044 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8faf3b-b46a-3eb7-8ed1-eb469ba82620 | -4.76622 | -39.58139 | 2026-09-20 03:42:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 147b2a52-377b-3dfe-afac-27203df8ff92 | -5.41772 | -44.27804 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64e5ab68-dd0d-3228-9265-6ff148dbb553 | -4.84414 | -40.52562 | 2026-09-20 03:42:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb9464c7-4fd7-3c51-be21-80d7fd78b0e5 | -3.59502 | -47.35786 | 2026-09-20 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7a2c130-642b-3e48-8e07-b68f3a76c6e0 | -5.22398 | -47.58309 | 2026-09-20 03:42:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca26d06a-68c9-3554-812f-dac5ded19cd7 | -5.40983 | -44.26923 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b0a4d97-4893-3cda-b1ec-47f37b2ad2e6 | -3.41371 | -39.28463 | 2026-09-20 03:42:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README12.md)
