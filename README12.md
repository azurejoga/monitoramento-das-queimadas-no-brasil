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
| 5a5690bd-c174-3fd4-99cd-e8de2241181d | -16.1638 | -58.6053 | 2026-08-28 03:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.7 |
| c486e577-166f-3efd-bb0f-4d788dc50167 | -6.1656 | -57.7988 | 2026-08-28 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 21b5d763-53a4-37b8-9f70-725e08d28c7b | -11.8243 | -47.1954 | 2026-08-28 03:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fdf71c78-5c20-3097-943f-889c1678dc56 | -7.8828 | -46.1028 | 2026-08-28 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a330a7c0-f723-31b8-8b1c-7194c85d1653 | -14.9019 | -52.5842 | 2026-08-28 03:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 310065ce-0a66-3d6c-97de-f00c9254a6ad | -7.2659 | -45.8668 | 2026-08-28 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 7b503a85-9d98-392e-91c9-d35db7122c20 | -9.9708 | -53.9419 | 2026-08-28 03:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2899b060-5659-37bb-a125-c8fa66bb2c8c | -16.1444 | -58.6073 | 2026-08-28 03:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 075bafef-90e9-3385-a00b-efafa213a31c | -15.5403 | -41.9175 | 2026-08-28 03:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| d9b11d66-868f-3cb9-8c9d-4939f808def4 | -9.6212 | -55.1064 | 2026-08-28 03:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 0107402a-d452-3a10-af6d-55970cb997a9 | -9.621 | -55.1266 | 2026-08-28 03:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| d7b5fa1a-df12-32c8-8f20-9208becbb344 | -11.8239 | -47.2178 | 2026-08-28 03:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| bdd66a1e-b012-3f51-81af-054301fe24f7 | -14.8821 | -52.608 | 2026-08-28 03:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8a6fcddb-6060-3ab5-b613-8d5188fcf106 | -10.3895 | -61.231 | 2026-08-28 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 595a64ae-266f-3d1a-b1a7-e1772b9799d1 | -10.7596 | -54.0384 | 2026-08-28 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 39ae00db-77bb-30fd-bab5-9c61fcc15fb4 | -4.8583 | -45.3915 | 2026-08-28 03:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 31772814-e56b-397b-b324-dd22cf8b3e43 | -7.8828 | -46.1028 | 2026-08-28 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 21a56098-4994-3156-a7ff-d90cc8f6caab | -16.1641 | -58.5851 | 2026-08-28 03:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 478.5 |
| 3179c0b3-d79f-35f9-bd8f-6ae69928edee | -7.2471 | -45.8685 | 2026-08-28 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 91860afc-a3b9-3cd0-b076-d5d2c23b2282 | -12.2656 | -50.5961 | 2026-08-28 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 1c9f0181-56f8-3566-95ee-ae461dcc62ba | -11.2879 | -54.0317 | 2026-08-28 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| da928283-ac17-3049-a7f5-6691ee053a23 | -16.1638 | -58.6053 | 2026-08-28 03:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.8 |
| e79fd89a-000f-3566-9d1b-bff70701e37a | -11.8239 | -47.2178 | 2026-08-28 03:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| f214097d-51c7-3d4f-a818-7b39cbe6bbd3 | -7.2474 | -45.846 | 2026-08-28 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4c4f12cc-93f6-3a35-8ac3-74f655af45a0 | -7.8831 | -46.0804 | 2026-08-28 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 684a187b-4d26-33fd-9f9d-bb83e2d77f86 | -11.8243 | -47.1954 | 2026-08-28 03:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 79f04a77-f907-3e7a-8bb0-41233c22f67f | -11.5659 | -45.5338 | 2026-08-28 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 47c40490-8d82-36a3-b7d8-5fda32bb4239 | -6.1304 | -47.2224 | 2026-08-28 03:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 470fcd8e-07f6-30ed-ab79-55ca0a49fb28 | -14.8821 | -52.608 | 2026-08-28 03:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3087a10e-424f-3f1b-9a0c-e8210a88599a | -11.585 | -45.5311 | 2026-08-28 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 337e1d19-ead3-31bf-beb5-5eac81dfb4fa | -6.1656 | -57.7988 | 2026-08-28 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0f0dae56-fcf3-363e-b9c2-b9f73d8deb5e | -16.1447 | -58.5871 | 2026-08-28 03:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 227.6 |
| e9ac83ff-34e9-3fda-9882-2cacd7e59848 | -12.43 | -43.4182 | 2026-08-28 03:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| bcb5560f-016f-3e48-aa79-08698b1b16e0 | -16.1444 | -58.6073 | 2026-08-28 03:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.0 |
| 521dbc91-35ab-3640-b01e-5e0244d04fc7 | -12.2847 | -50.5938 | 2026-08-28 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 0a393126-dfcd-3d5c-ba4a-6d9d5a4b5991 | -16.1644 | -58.565 | 2026-08-28 03:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.3 |
| 7b3ac5df-f32f-30b4-83c4-bb0f51290e95 | -8.5969 | -54.7755 | 2026-08-28 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| eb00a544-d2e4-35a0-9340-6f131456ba18 | -12.4305 | -43.3944 | 2026-08-28 03:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 293ddc53-56cb-3a68-be3e-95aff2433ec2 | -7.2661 | -45.8443 | 2026-08-28 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d15c1423-aa12-3a87-b6ca-3ad7a5afafac | -10.4981 | -64.5005 | 2026-08-28 03:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 08e5bbf0-2606-3699-bf56-18d31807fdd5 | -10.3894 | -61.2502 | 2026-08-28 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fef0fcd5-3386-3812-91ab-db7495a774c9 | -7.2659 | -45.8668 | 2026-08-28 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| ff08440c-9cee-34cf-bdb1-100d4ccc64ae | -15.5403 | -41.9175 | 2026-08-28 03:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| a65bd249-bdcf-3c55-b0e7-fda597df8cc2 | -16.1836 | -58.5831 | 2026-08-28 03:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.5 |
| 933fd442-9b29-39dd-a236-f3bf26ca998c | -14.8825 | -52.5868 | 2026-08-28 03:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 501eeba6-54f6-3ee5-ae05-fb05bd10bede | -4.8397 | -45.3926 | 2026-08-28 03:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| b389ed40-1752-3202-8e8a-58c1014ceaa3 | -6.1657 | -57.7793 | 2026-08-28 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9280c3f1-d9f1-3e74-870f-77bade82e97d | -12.2659 | -50.5747 | 2026-08-28 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 484f8ae0-d4c2-31f1-8cff-8a174be5ff23 | -7.25 | -45.88 | 2026-08-28 03:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 536b96f5-caeb-3e27-8c5b-858a861d8c4e | -16.1447 | -58.5871 | 2026-08-28 03:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.6 |
| e8e07415-976b-39cd-8350-a88234fa6192 | -12.2656 | -50.5961 | 2026-08-28 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 78f7eacf-23e3-31f3-ab6c-3be1b259a580 | -10.4981 | -64.5005 | 2026-08-28 03:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 6fd45342-c82e-352e-85b2-061095e6c076 | -16.1641 | -58.5851 | 2026-08-28 03:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 290.7 |
| 813e7e88-c411-344c-8db3-57e0fa0f1300 | -16.1638 | -58.6053 | 2026-08-28 03:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.0 |
| 65d37ebd-678a-3b58-999b-8f6fe05693c1 | -7.2471 | -45.8685 | 2026-08-28 03:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| e0bfbcaf-0813-3a8c-8365-f916d4aec065 | -12.2659 | -50.5747 | 2026-08-28 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 161b61c4-19ca-3331-ba80-ee9b7aac421a | -16.1644 | -58.565 | 2026-08-28 03:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 34bea7de-2ece-30a2-a16f-9e878c8e4b05 | -4.8583 | -45.3915 | 2026-08-28 03:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e9a29290-bdb6-3fc1-8142-b97c533bd88c | -6.1656 | -57.7988 | 2026-08-28 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1de0240e-c4ee-3519-8ce1-e275e48c8b92 | -11.2879 | -54.0317 | 2026-08-28 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c047997e-cbf6-3eed-bba1-833d1dcdf703 | -7.8831 | -46.0804 | 2026-08-28 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 73d04aed-3643-35f5-9977-047a8881b13b | -4.8397 | -45.3926 | 2026-08-28 03:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7699cf19-01b0-3a6c-8abd-e8bb3eb8f623 | -14.8821 | -52.608 | 2026-08-28 03:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 48595ce0-3116-33eb-a38b-a02a6a18de91 | -12.2468 | -50.577 | 2026-08-28 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 597081c9-dbc6-3116-b0d5-e80c187e89a9 | -7.2659 | -45.8668 | 2026-08-28 03:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 7592f92c-9415-3ea5-9b72-c201b6333d9f | -12.2847 | -50.5938 | 2026-08-28 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 74f105bb-716c-3457-a87c-2fa6161b863f | -16.1444 | -58.6073 | 2026-08-28 03:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 151fa2bf-88b1-3cfd-b456-efd63f2712b8 | -7.2661 | -45.8443 | 2026-08-28 03:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6d339325-9015-349f-a1a6-f24383e7b01f | -10.7596 | -54.0384 | 2026-08-28 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 2da51271-0d8e-31b7-99b1-f899fa919b8e | -14.8825 | -52.5868 | 2026-08-28 03:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 59062a1b-e9cb-314d-b1af-8b62ec2a1fa3 | -11.8239 | -47.2178 | 2026-08-28 03:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 275374e5-6eac-39bf-8b16-f532064f7f66 | -7.8828 | -46.1028 | 2026-08-28 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a79dff07-5d8c-3611-9217-6233df737c6d | -7.2474 | -45.846 | 2026-08-28 03:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 545faf4f-4125-376f-9a7f-4bb9f7518c1f | -5.11671 | -37.56717 | 2026-08-28 03:28:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af075ecd-a8c8-3194-b8cc-6b1923533fae | -5.33806 | -37.04023 | 2026-08-28 03:28:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3b6d862e-ce8c-3d26-b679-8385c355bb28 | -5.33356 | -37.0395 | 2026-08-28 03:28:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de30e046-ca17-332c-a3d1-0599bcdd086b | -7.8828 | -46.1028 | 2026-08-28 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f88ca5a8-305c-3b42-96b7-8cbea9794a54 | -14.8821 | -52.608 | 2026-08-28 03:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b67ca7d6-d4d4-3659-9b15-11ada2ddc0cf | -16.1638 | -58.6053 | 2026-08-28 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.6 |
| 1aad150a-36f8-3215-9601-24ccc7026ff0 | -7.2661 | -45.8443 | 2026-08-28 03:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8c283974-a110-3186-9380-34b185fc9128 | -11.2879 | -54.0317 | 2026-08-28 03:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1b10437c-c8c9-3802-8a8c-9b34d3a5da83 | -16.1447 | -58.5871 | 2026-08-28 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 212.8 |
| 8c9b3c1b-fb19-3429-a52a-47ed0810c644 | -16.1644 | -58.565 | 2026-08-28 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 143e6d54-850d-3d79-923d-6971cc700c68 | -4.8397 | -45.3926 | 2026-08-28 03:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b61857b4-8e5c-32c8-ba3f-4f2fcadf31bb | -14.8825 | -52.5868 | 2026-08-28 03:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 560867af-6c4b-3bd7-9f8f-123af46f73af | -6.1656 | -57.7988 | 2026-08-28 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 77635b92-2c1c-32cf-b739-97a26464b9bc | -7.2659 | -45.8668 | 2026-08-28 03:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 39550bb3-138b-3e82-8de2-3233401f3044 | -7.2471 | -45.8685 | 2026-08-28 03:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 91ced963-98e1-3f3f-852f-2fd516b4fb17 | -12.2468 | -50.577 | 2026-08-28 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 61784c3a-69e4-3e25-8e4e-df2caef8da64 | -6.1657 | -57.7793 | 2026-08-28 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| ed648842-a099-3fca-b6d5-b53f8b68bec1 | -12.2656 | -50.5961 | 2026-08-28 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 10028e71-65b3-3f7f-ba11-6221b3b349d5 | -10.7596 | -54.0384 | 2026-08-28 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9fdafe7f-1233-3faa-88ac-915f1d5d067b | -7.2474 | -45.846 | 2026-08-28 03:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 4759a764-3a82-3b34-bf63-3367cbb41f09 | -10.4981 | -64.5005 | 2026-08-28 03:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c8e59904-bcf9-3fa3-97bb-85b4b8cb6547 | -16.1641 | -58.5851 | 2026-08-28 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 279.0 |
| 81ea6cdc-481b-3ac1-80b5-92b32898a8ec | -7.8831 | -46.0804 | 2026-08-28 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1875d5ee-52eb-3eae-919d-9d2fa9035edd | -16.1444 | -58.6073 | 2026-08-28 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 19074554-12a3-3b35-9a07-c56c142d20de | -12.2847 | -50.5938 | 2026-08-28 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7de46c86-3a49-337d-8c06-6a9162c53a5b | -12.2659 | -50.5747 | 2026-08-28 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c77abb39-f3bf-320c-befb-b41cc10f610d | -11.57427 | -45.52505 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |


[Clique aqui para ver as próximas entradas](README13.md)
