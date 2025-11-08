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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ee20d69-dbc8-36b5-b451-bdbdad7a528e | -4.2042 | -46.39711 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1881bc9f-c0b8-3b30-83ce-279764485d9f | -4.82575 | -48.06697 | 2025-11-08 04:36:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4d1edfb-747a-31b7-a7ee-bdd8197c77fd | -3.67372 | -50.45179 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40a701d0-f1f5-33f6-8a01-7d435f430db9 | -8.06747 | -47.12141 | 2025-11-08 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 102752ee-55dd-3c13-853d-1c2e6ebd0c30 | -7.38533 | -43.53565 | 2025-11-08 04:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e239b1dc-2ad9-3d00-b9f9-65c49cdebac3 | -6.46849 | -43.22868 | 2025-11-08 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa556cbb-dc15-3fb0-ab6a-3dac6bfcd05d | -5.86414 | -44.70277 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afa60fcb-d898-399d-bc6d-ad7258cd87b7 | -1.69884 | -54.67451 | 2025-11-08 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fe7a004-7895-359b-b4e7-174194070baa | -4.57068 | -45.75216 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3c150d1-ed72-344a-bf8d-dd40ebf016d8 | -3.31682 | -49.13427 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee38c1ea-c8ad-393b-896e-003e6d4730d1 | -3.44195 | -43.15181 | 2025-11-08 04:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ad2ecc2-11b7-3554-bcad-3f78d15d8f51 | -1.57916 | -53.78955 | 2025-11-08 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9e2313-c4ef-344e-930b-f8a0e33402f7 | -4.53261 | -45.61806 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 39e18ce8-5a80-34e3-ab37-e14528cf24b7 | -2.9964 | -48.92875 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75c2fab3-5c92-33e4-9a12-62bb1b428be3 | -7.03489 | -46.98343 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3883c5bb-69ae-30cd-9ea8-68601ef72506 | -4.26019 | -48.58551 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62671d5f-6a29-35a9-9f2a-a003c38bee18 | -5.93514 | -38.17906 | 2025-11-08 04:36:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d306feab-7cad-32ad-9983-9781eeea269c | -3.77951 | -45.76952 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 215a206f-6df0-38e7-8540-c8dc6f59dd0c | -4.53436 | -45.80648 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9948d9e7-3f08-3967-9162-61afa470d628 | -3.42995 | -50.11564 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc23e28b-db3d-3d25-8e5c-3c8dd8e70a34 | -4.3824 | -45.36624 | 2025-11-08 04:36:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 903ef4d8-da77-384a-a3a9-ed9115d7b23a | -5.44268 | -44.65638 | 2025-11-08 04:36:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0aee78e4-258a-3ba9-9d46-683c6ecba0bb | -4.11169 | -48.00684 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 422ca02a-4ec3-35a8-bf13-4ac044e4bc37 | -3.64476 | -45.88949 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b1a1233-d201-3ac8-9424-7e2ea0efe881 | -4.95091 | -48.56395 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4473f8a2-3081-37fe-996c-13c894924624 | -4.03166 | -49.27139 | 2025-11-08 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c173b000-b91f-3066-b6af-55fc4aa809cb | -4.2366 | -48.60367 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd4de27f-8b86-3ab5-a25a-d735c414401b | -4.4064 | -44.78759 | 2025-11-08 04:36:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c2ffaad-5ae9-356d-9765-dfd987059c4d | -5.83041 | -43.27895 | 2025-11-08 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a95c930b-acd0-3d2a-87ba-ee1f7d09b9e7 | -3.15285 | -50.30288 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb829f48-db64-348b-ae86-e41eff491d76 | -3.41427 | -52.19103 | 2025-11-08 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8d407f3-5e61-3cbb-8fbc-e10ad5dbb2ff | -4.24486 | -48.37988 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f61497fe-16df-395d-9369-8c6c3108166c | -4.46652 | -43.21386 | 2025-11-08 04:36:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daa82df1-3567-3f8a-b5a0-104a8135ab3b | -3.24477 | -50.15056 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acbc7509-07a3-3d5f-b2c5-cd8c1d75f7c9 | -4.91569 | -45.91298 | 2025-11-08 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09b07a42-433c-33a1-bb6b-656ad280d414 | -2.71098 | -49.54029 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0f19cd9-05fc-3c5f-90b4-08c75ec24ec5 | -4.47233 | -45.33387 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dc1b6bf-bc45-3465-893c-6929854f691d | -3.63802 | -44.23353 | 2025-11-08 04:36:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed7a7aeb-d4a2-3779-ae0a-6f6da8191495 | -4.29435 | -45.69139 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86e4e1ef-90d7-3c13-8eba-479dfcd7bd61 | -8.06692 | -47.125 | 2025-11-08 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ede5fb-94b6-3a07-baa3-8b9d48d14291 | -5.37544 | -43.61683 | 2025-11-08 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd4191e5-d407-33f4-ad32-0e6d10545a53 | -3.43766 | -45.58755 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76a30544-e324-3c04-876d-69f52d80b2ef | -4.60725 | -45.56147 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 520949df-b643-397d-a09a-52d16378fb2d | -5.65152 | -43.00784 | 2025-11-08 04:36:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5f04160c-3b33-3b03-964a-b752a650a219 | -3.09478 | -49.25788 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4019e4c5-7573-33ee-b323-34c34af44adb | -7.79305 | -46.64713 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 519a5cbc-3f47-3858-bf22-77839e7b061f | -6.82694 | -46.77627 | 2025-11-08 04:36:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6585d151-e203-33ce-b59e-4be596bf426d | -6.52375 | -55.034 | 2025-11-08 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa1379b5-d0a9-32dc-bb68-08a900bfef96 | -3.44295 | -43.17095 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5fd556e5-757c-3d61-86ef-2c8c113881b7 | -6.46968 | -43.27522 | 2025-11-08 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbd165d1-007e-3e6c-bd76-eef1131813dd | -5.78066 | -53.44876 | 2025-11-08 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aac4fc2e-9ef4-3d74-8dc1-869efcb2229b | -6.2067 | -42.04939 | 2025-11-08 04:36:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 78cb4b05-6f10-3f8c-9625-6ec0a8fd109c | -7.79645 | -46.64765 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c39a3a55-b234-34c6-bc5b-b2230af56931 | -3.25457 | -50.13536 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99278a9f-7602-310d-8e5c-81531d2b2073 | -6.22582 | -47.3286 | 2025-11-08 04:36:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 838689a1-8b26-3fb6-a2b8-2008dda4490f | -5.25967 | -47.16645 | 2025-11-08 04:36:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d081f86d-9c0c-37d2-b805-d0001997543e | -6.36699 | -41.7487 | 2025-11-08 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3b99d9fc-c376-3dac-ac7b-b781f620d5c6 | -3.67439 | -50.44759 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e71e9f-e75f-3ce8-857d-c727cb3482c9 | -5.37271 | -44.72926 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b04ef7d-3eae-306b-a7b9-94cbd7d9d8b1 | -3.20902 | -51.68755 | 2025-11-08 04:36:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d362336-df7e-348d-bd78-f27a2f7d80d9 | -8.20837 | -46.97844 | 2025-11-08 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86b96c92-5e6f-3f0f-8666-04f3d1c624ab | -5.3921 | -44.2379 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac20587f-a0b1-33ff-b618-6f9480c71b85 | -3.16207 | -45.49695 | 2025-11-08 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0aeb26da-75e5-3634-a8e9-be081f5cb357 | -3.67801 | -50.4482 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a6986f0-70e7-3c1a-9d28-67149959976b | -3.44436 | -43.16167 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f23a18c2-313f-3385-a454-e7b0aad09f10 | -3.83805 | -49.82637 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c8d4e9-0c08-3a68-9e9a-545fb0c4dbcf | -3.44281 | -50.21804 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5aeec3d-9091-32aa-91b8-f50d92aebfa3 | -3.36124 | -45.29413 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a08a3640-a9d1-3b9b-896e-09cbb514f7c1 | -3.64607 | -45.88563 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b139c67d-9759-3d78-ab75-7a33c38aafc1 | -6.22267 | -41.72207 | 2025-11-08 04:36:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1ea45df-3fa0-397b-bc73-1eba93a19242 | -3.01519 | -49.44417 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfe6dbfd-2f8f-3a86-a5d3-b7dc001fdf95 | -3.44037 | -46.19199 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95b784a4-57a2-3d29-86c2-48807c353f2c | -2.56716 | -50.64557 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dae0f83-4fa7-34ba-bac7-335a83201c2d | -3.55244 | -45.36435 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d40d1832-812b-3be0-9158-ed50bbfcaee6 | -9.0936 | -44.31807 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8787996-f1ef-3589-b23c-5f799d4c70e3 | -3.50529 | -50.05732 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d9a868-eb80-3b2d-8531-c711df147923 | -4.9692 | -48.01838 | 2025-11-08 04:36:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0466c75-029a-3288-bfe7-8fac55ede17c | -3.65102 | -50.26953 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a1a2db-cb86-32e1-a1fe-872f79d08a78 | -3.44647 | -43.14775 | 2025-11-08 04:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca6e17cc-b9de-326a-9515-3b3bddf7f0ef | -3.44604 | -50.24384 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90138607-a937-349e-9692-ddde9df4ed71 | -6.22331 | -41.72026 | 2025-11-08 04:36:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 01829d56-c231-30bc-abff-baca8ad76187 | -3.46013 | -50.22503 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4a6b97e-0d18-385c-b006-635feb8aec1b | -7.55374 | -47.24525 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a62980d8-ce29-3298-b7a0-dfed611533fa | -3.44106 | -45.58808 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713f92eb-a01e-36dc-a876-cb4d4d822b47 | -3.50365 | -50.04464 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ca10100-9bbd-3ee5-97fb-81255557a367 | -5.63081 | -43.9147 | 2025-11-08 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ab44708-04e2-3760-9430-6338d0fc42d4 | -4.2166 | -48.35021 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f0526db-9d08-33a0-96eb-0a2099d69e9f | -3.73468 | -49.68338 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5f00438-77ff-3484-b6e4-a692ed52df00 | -4.36457 | -45.61898 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 125d566b-132b-3268-84ae-2e6584d7d544 | -3.51345 | -53.5401 | 2025-11-08 04:36:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65019c7c-783f-3bed-9a27-ddd4b3c782a1 | -3.83859 | -52.14037 | 2025-11-08 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9818d88a-249b-3724-a279-3dccc4827455 | -3.42683 | -50.0448 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78d0deb1-a04d-318a-91ac-99c3ee50a890 | -3.87386 | -40.98525 | 2025-11-08 04:36:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d90b4e23-642e-30da-8b23-7ec198a9eebd | -4.39449 | -45.35658 | 2025-11-08 04:36:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c88b28fe-33ca-3ba8-8770-7c677ef7a204 | -4.69417 | -45.85689 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75f03990-364f-3c39-98b0-f51e4f8591f3 | -3.73118 | -49.68282 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0f68676-47cd-3c50-b53c-d18a89291685 | -2.93827 | -48.76968 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e486cda-8965-356b-8d1f-08dea0a5ba22 | -3.34732 | -50.20867 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74c4ebf4-f871-35b8-aff7-70690ff8718c | -3.34079 | -50.2034 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc6608c6-3ede-381a-a04f-8b0082bab11b | -4.10944 | -47.27258 | 2025-11-08 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
