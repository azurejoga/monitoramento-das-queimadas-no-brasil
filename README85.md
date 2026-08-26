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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34f989b3-0c69-3783-894a-824fa6618c7f | -9.1711 | -49.9835 | 2026-08-26 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 490d97fe-1a74-3e04-ae7a-e36f9e741d64 | -6.8062 | -58.6469 | 2026-08-26 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e41fb9a4-1574-30ba-af94-82926978bd69 | -12.1422 | -43.3707 | 2026-08-26 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ed117178-081b-3813-8ece-edceb7369956 | -13.3402 | -48.2079 | 2026-08-26 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 92d2b075-d1a3-3a46-b0ca-b569ac0f0931 | -12.1701 | -50.6075 | 2026-08-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.3 |
| b7a23b93-9dea-3758-bf7c-adbe85266292 | -10.5596 | -50.4449 | 2026-08-26 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| b077d534-0808-3541-b366-dea158aa5907 | -6.5261 | -44.8887 | 2026-08-26 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d1708489-49ce-3709-8afd-c63a7fa7ada2 | -8.5973 | -54.7352 | 2026-08-26 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 6142119a-df78-39dd-a18f-723baead2eb2 | -10.9405 | -50.255 | 2026-08-26 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2ed27822-35b3-377d-a77c-dac9641f5dbc | -10.95 | -49.5877 | 2026-08-26 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| af177446-a929-3ffa-bbf4-64d68c8c92a0 | -8.6344 | -54.7528 | 2026-08-26 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e9a85d79-07e2-3f6a-8e9c-5f56b2e2d280 | -6.1169 | -53.7501 | 2026-08-26 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| adbabc22-17cf-3ef9-a37d-ce5c2e18a37b | -11.7357 | -54.5227 | 2026-08-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 8c2a1347-1e98-32a3-b47a-644ab5a0f1cf | -6.0353 | -58.0376 | 2026-08-26 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 25b1ecf8-441c-30a9-9be6-89c30539b987 | -7.385 | -55.1523 | 2026-08-26 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 49da73ce-ad4e-35de-9967-39076a1358cc | -6.1286 | -57.8198 | 2026-08-26 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 664fa05a-e6c5-3d10-9f59-b5a0374ff9bb | -6.6409 | -58.5181 | 2026-08-26 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ae754982-f0dc-3274-a3cb-b7ac3c6a3c98 | -12.757 | -46.4538 | 2026-08-26 14:40:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5712ed15-a779-3433-b024-7c10974b16a4 | -11.8165 | -47.6647 | 2026-08-26 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 6ac74cdb-30a7-31ba-80ca-95216204e325 | -11.0037 | -51.1635 | 2026-08-26 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 907f184b-8b73-39b4-92dc-adab4dc284c6 | -10.4689 | -46.2028 | 2026-08-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 8405a0db-1806-3d25-9abb-9f3c5bb773c4 | -14.3941 | -51.7799 | 2026-08-26 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ec7b5237-e010-3ce0-be9a-d731c640aef6 | -7.1309 | -42.7945 | 2026-08-26 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| c2e6740e-1b29-3aea-a222-a97ed64abbd2 | -13.681 | -51.8298 | 2026-08-26 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| eea66338-4a61-3fde-852c-d041a916a03b | -8.9418 | -45.748 | 2026-08-26 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 383.7 |
| 4d8e7d68-3372-3351-9b69-31b4367ac0ac | -11.3702 | -50.6993 | 2026-08-26 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0d491d13-e385-3c6a-9285-08f4d7b7f24c | -9.6024 | -55.1078 | 2026-08-26 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 266.0 |
| 5f09a0a4-885c-3b0e-a0ce-9474495c945e | -7.6649 | -47.1242 | 2026-08-26 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 249.9 |
| a018fe67-b59e-3812-87ea-aa94c1b2b7c3 | -6.1285 | -57.8393 | 2026-08-26 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d6df770c-6046-37f0-8c39-6e71aafa9990 | -9.7249 | -49.3296 | 2026-08-26 14:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| c4b642c8-22a8-3f56-b5ef-d206e43010ee | -3.2178 | -61.2362 | 2026-08-26 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| f9924c00-e704-30e4-a67b-770116046af9 | -8.8187 | -49.6093 | 2026-08-26 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 199.9 |
| 8f52f8d6-d89c-39c8-a7f4-c43d273d9f02 | -8.5175 | -55.324 | 2026-08-26 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 05f66ce1-e54d-3647-8d9d-e151e7f6a133 | -8.7769 | -49.9763 | 2026-08-26 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 8c45be9e-8d12-3f50-a4b0-316a69629c8a | -11.7544 | -54.5414 | 2026-08-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 189.0 |
| e856dcd7-37f6-34cb-b677-4d9c40e61cac | -7.5104 | -61.3832 | 2026-08-26 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6b52b8fd-3000-360b-8732-2225f68f8834 | -12.1704 | -50.5861 | 2026-08-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| fac63d76-ee51-3234-b220-cce0fe8bbc77 | -8.5363 | -55.3027 | 2026-08-26 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 188.9 |
| c97a0218-60e2-33dd-a9e1-106156ba5c32 | -9.7246 | -49.3512 | 2026-08-26 14:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| fdccd5f5-d204-3cf7-bc16-6c61c90fe2c2 | -7.0242 | -59.2374 | 2026-08-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 267dab13-1b85-3836-a8ea-2ec76bd9ad3b | -11.7736 | -54.5191 | 2026-08-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 330.9 |
| a7a9f9ca-3d65-36bb-b4a5-7ac13b41bb5e | -8.1482 | -47.5218 | 2026-08-26 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| ef2a1557-ce0e-37c0-9d97-4c1490ca937a | -14.3945 | -51.7585 | 2026-08-26 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 220.4 |
| df2ce819-475d-3b47-b342-5133430d1e62 | -13.6617 | -51.8323 | 2026-08-26 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3b23720a-b5c0-3ca5-88e2-1545c1678bd6 | -11.7354 | -54.5431 | 2026-08-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 6cfa0494-51f1-3ff3-9538-45f1ccfa1f0c | -6.8247 | -58.6461 | 2026-08-26 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5ae8a2ed-a072-308b-8183-de71bc29fb06 | -8.5177 | -55.3039 | 2026-08-26 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0e8473f5-0e7e-32a4-8b29-4b60ff3816a6 | -6.1743 | -53.4834 | 2026-08-26 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 63641966-614d-3de6-8d6e-c0127abb51fe | -8.5361 | -55.3228 | 2026-08-26 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 48ec6428-f7a0-3a6a-b105-431481d101b4 | -9.1899 | -49.9818 | 2026-08-26 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 6f332019-0a71-3944-989b-2186d4711eab | -6.695 | -58.7291 | 2026-08-26 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fd84a32d-2536-31dc-be5a-75258a1c3fe3 | -8.7582 | -49.978 | 2026-08-26 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| fa98ce4e-ba7e-32e4-b570-948a2de8273f | -3.1449 | -61.1808 | 2026-08-26 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ef45def7-7a87-3402-aeca-489630444ecb | -9.5997 | -46.0135 | 2026-08-26 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a468ad7d-69b2-3b94-8018-90334dabe0b4 | -15.5734 | -47.1254 | 2026-08-26 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| ed0be1b6-5514-31b2-8e5a-b0157a3a6ab0 | -10.4686 | -46.2254 | 2026-08-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 5f85859a-37f8-3bf5-bd05-592cd911b147 | -11.7546 | -54.5209 | 2026-08-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 330.6 |
| 36c98ef0-d665-3a4e-8e7d-4f1500b5f329 | -8.7584 | -49.9566 | 2026-08-26 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| e76085d3-d249-3be7-bd55-4273a9eb0cc7 | -13.6614 | -51.8535 | 2026-08-26 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0e0848c4-8afb-33cf-9781-23172c79330b | -11.1561 | -54.0028 | 2026-08-26 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 087c064a-77d7-36b7-8ceb-9a599a52b68f | -9.6022 | -55.128 | 2026-08-26 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| dcf39389-5acc-3339-83f7-76f8e7699bec | -6.8193 | -59.5734 | 2026-08-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| eaee7fb8-1d42-36cd-8a26-3e4cc2f72c9c | -6.5138 | -55.2387 | 2026-08-26 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 23ca79bc-490f-3758-aa10-b745874d6357 | -13.3595 | -48.2051 | 2026-08-26 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 9e4d6d57-f14f-3137-aaef-6d917030f84f | -8.1484 | -47.4998 | 2026-08-26 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1da4114a-b549-3bd6-9a4e-419c31b576f7 | -5.8469 | -39.5443 | 2026-08-26 14:40:00 | GOES-19 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 68e6087f-cbad-3f80-b3de-94240ddd8e19 | -6.7648 | -59.4408 | 2026-08-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b56e9577-daeb-3700-80df-71f0cb03f43f | -9.659 | -55.0632 | 2026-08-26 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 648f35d5-298d-38ed-bd0e-abdd66ca01b2 | -7.6461 | -47.1258 | 2026-08-26 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 526.9 |
| 0b0915cc-6563-34b1-91f0-a71e70276bef | -11.7973 | -47.6672 | 2026-08-26 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 200.6 |
| fd69fc64-2d82-3106-840e-6cc14c8e5bef | -4.8002 | -43.1709 | 2026-08-26 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 1da0f042-4c0f-3689-895c-e9a58e375a54 | -11.7977 | -47.6449 | 2026-08-26 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3dfbf8fc-20e1-3bae-824d-2144ea3251f4 | -12.6836 | -48.4116 | 2026-08-26 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 89215c1a-b28a-3e03-9160-2607fb1c3b5c | -11.7733 | -54.5396 | 2026-08-26 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 67453318-aab1-3961-b957-0d6ecec5fda2 | -6.6226 | -58.4995 | 2026-08-26 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| affd14de-4e84-3420-b29e-72fa64fc46a8 | -11.1939 | -53.9993 | 2026-08-26 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 53b2e04a-5a28-3d5e-a07d-804a96ba4f4b | -6.7833 | -59.4208 | 2026-08-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| de462b43-10dd-3057-a96a-d530bb95b8cb | -7.0058 | -59.2382 | 2026-08-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 641a20ee-6709-3c0f-aab0-67874f21a8e4 | -8.9421 | -45.7253 | 2026-08-26 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| b020ad50-eb08-33c6-a9a5-54713cbd92f9 | -3.2179 | -61.2174 | 2026-08-26 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7a249272-5d20-3f58-a857-5756e125bae1 | -6.1656 | -57.7988 | 2026-08-26 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 899b7d91-c9d6-375d-8491-ba14be3107e6 | -13.6817 | -51.7872 | 2026-08-26 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 04d8682b-33ed-3241-aca1-6b1f703777fd | -6.8019 | -59.4008 | 2026-08-26 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b2b90708-2658-3c93-8aea-5e01e856826a | -3.2178 | -61.2551 | 2026-08-26 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 47bb155f-f19c-3e7d-8238-e0661f2a77e0 | -13.6813 | -51.8085 | 2026-08-26 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a64017f4-d0ff-34ea-88a9-19be29e98e0f | -6.695 | -58.7291 | 2026-08-26 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b86228ab-7b2f-3c41-b822-9ae32be21aac | -6.6409 | -58.5181 | 2026-08-26 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c9beae79-fad2-3d45-be81-9229ee3fcff2 | -8.8187 | -49.6093 | 2026-08-26 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 300.6 |
| 16542cc9-5855-3998-9e19-453d4047f0db | -11.1561 | -54.0028 | 2026-08-26 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8f864468-c34a-398b-8fbe-90239c4c84eb | -13.3402 | -48.2079 | 2026-08-26 14:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1d84d8d8-e2ff-38d0-b19f-3e30d2aab13b | -3.1267 | -61.1811 | 2026-08-26 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d4484b1e-f868-3191-b672-7d944b6833c6 | -9.1315 | -57.5703 | 2026-08-26 14:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 939b2325-a16c-3699-b6b6-ee663214faed | -8.5973 | -54.7352 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 36ca7b2d-7c6b-3507-8fa0-72679495e9dc | -8.5975 | -54.715 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 22f44080-cefd-3b4d-ad72-9aa854a9544c | -8.6161 | -54.7137 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 38122ebe-a6a9-38b3-98b2-1ac7a16fa7d4 | -7.6649 | -47.1242 | 2026-08-26 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 363.5 |
| eb97e1a4-1238-35f0-a3cb-0622a6ed863e | -12.1701 | -50.6075 | 2026-08-26 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 8178031d-8deb-34b5-8227-7d987ef4c637 | -6.7692 | -58.6679 | 2026-08-26 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0e2170be-9fb2-3902-9fa9-fef77590e3af | -8.1671 | -54.9447 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 84abdafa-45d4-3195-8f2c-2d92d32623cd | -7.3663 | -55.1734 | 2026-08-26 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |


[Clique aqui para ver as próximas entradas](README86.md)
