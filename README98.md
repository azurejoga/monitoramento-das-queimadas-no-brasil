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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c366ece-fdde-3e86-8d4a-fbd65b0bbcab | -5.85946 | -53.54843 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baead773-ded2-3254-a914-b7c1328ea7d7 | -4.37186 | -55.43441 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 022c0c66-8fcf-3115-a325-251e49c7be33 | -5.98787 | -52.20497 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad12771f-74f2-3fa1-a682-d01251f26897 | -4.49354 | -55.48207 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5da70ae-fa88-3000-8fae-06c5ba37f71a | -5.7902 | -51.863 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0f18c39-c987-32c6-9b39-1e21d8ea005f | -10.85968 | -56.18305 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88e52887-14f5-3545-9bfb-8a6f6a21e274 | -11.95004 | -55.92565 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afcc557b-9adb-3d42-81c5-6cd706bb864d | -3.69861 | -58.51833 | 2026-09-20 05:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cab7e43a-b6e2-3c9d-9523-7f8c8a6f37df | -6.80176 | -47.82034 | 2026-09-20 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8c8ba5a-9316-3b88-8f77-aa1233f00b80 | -11.23148 | -54.08688 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c9f65f6-b2bb-3f43-ac30-9e96edbc58d0 | -6.32465 | -47.63138 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9e668812-5594-3b09-90d0-b7873f17f61b | -12.01356 | -51.47363 | 2026-09-20 05:25:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 933df027-b044-3e21-8b6e-3719fbb0db04 | -7.17728 | -47.45895 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3692bab-a8c9-33a6-8b7b-fbc656c1af68 | -10.69822 | -54.17714 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf62329-fae5-3a3b-9013-5c2b56150157 | -10.88248 | -54.07195 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efa8185b-3b52-3c2f-95f3-4308f270b613 | -11.04187 | -54.15954 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d8ecf5b-38ed-3c0f-8bec-2fe164e496aa | -14.05189 | -52.08273 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 22edd189-31f1-3392-be71-082fc72c9b75 | -10.91037 | -53.97281 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b67117d-e87a-39c1-b658-2dc5750f173d | -5.87001 | -51.55794 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b31b2eb1-433f-3c25-9224-e83321b34045 | -5.76852 | -57.46184 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81289ace-0a89-3b0b-995c-56434e307ba3 | -4.36603 | -55.04943 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99bd2b8a-1bac-3a88-ba77-44fdd8721c09 | -4.39571 | -55.43804 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f1ae2b5-8967-36f7-9984-81a0891d2a51 | -11.24391 | -54.10488 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3adbc993-a495-3fa0-bcd9-6227beef9d17 | -11.22823 | -54.07998 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e3108c69-c144-3460-a4b9-24e08145092c | -11.38837 | -51.41505 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ce69418-809f-31d3-a7c5-d081b57778a6 | -3.6926 | -60.57434 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f97cc69d-f167-393a-867e-c520a1cf0095 | -5.86778 | -51.57453 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91073506-acbf-37dd-8d5d-20a4244689e4 | -3.88801 | -58.94635 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c0087be-d655-38fc-bbf1-abe281a66069 | -10.87998 | -53.97938 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9d34e8e-205f-3a63-97e7-bd00223a2196 | -14.66379 | -54.45885 | 2026-09-20 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f66ad020-376d-3cbf-9207-ee3766f6b8f2 | -11.11828 | -54.02459 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6f897890-5215-3397-bbda-d5a1c63c74ef | -11.22389 | -54.06922 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f1e9c8b-b081-3f0c-9d7d-e3928add79d1 | -11.3778 | -51.40526 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19d1c8a8-c6df-34ee-9222-c1a09a819a9c | -5.84971 | -53.5173 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d4d0037-8e98-3941-80b6-48769b4dedc4 | -11.01994 | -54.14067 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b01c101a-14f3-3048-a90d-791637744eab | -10.87785 | -53.99558 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf0518bd-f17c-3c69-8972-904d3175f99f | -7.16092 | -47.47635 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d4be0648-dbc9-3c22-b99c-efa3876801ed | -6.6691 | -50.89005 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c148fc21-59a1-3c8e-b4a8-4919fd34bc7e | -5.84372 | -53.52628 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e11fccd-7e9f-3b80-883c-a362ad3bc7c6 | -6.3178 | -47.63054 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 031f2cb7-fab0-3b2c-8155-d7c6e95cca84 | -7.16077 | -47.43191 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 67851bcf-47bb-34ce-9c23-b897e99becba | -14.92027 | -49.91435 | 2026-09-20 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b1ea0d5-131a-32f8-9ae8-56058d1fabed | -10.93226 | -53.94877 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e791df8-0cad-322f-8614-3ea90f8da636 | -14.67299 | -54.46562 | 2026-09-20 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a6ad30d-645d-3e77-803d-57b838c578cc | -5.96766 | -57.76841 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d20439a-5da6-3527-9be5-05cd689ed53e | -5.88849 | -53.6409 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 983a40a1-1ffb-315b-93db-f3c6710136d5 | -3.69663 | -60.63504 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6d79770-cf2b-3f00-98bc-561e2074394f | -3.39539 | -61.29643 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9aa0b58-0a1d-3f7a-9d06-bb89748ac7bc | -10.92741 | -53.94815 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 69100e46-1af6-339d-be71-3ae90c60ed01 | -3.58628 | -59.02613 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ee8ec4-8b02-3f27-961b-6f2daf9341d8 | -6.30408 | -47.62892 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 117db436-e086-3e66-bbfb-10d7ac874119 | -10.93334 | -53.94849 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1908b359-f930-3a26-854a-d5778be11463 | -5.84697 | -53.53667 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd1ba3bf-93ee-3e6b-b43d-c6a3643fe418 | -11.04667 | -54.16012 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7d87f488-89c7-3ffb-9664-76b5c0943521 | -4.51606 | -55.46722 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3283224-c293-3ffb-85a9-947fe851fbcb | -11.1221 | -54.02696 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d972aac3-1d99-35fb-aa4d-2a5c44af8020 | -11.9427 | -55.92654 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a3c0c8a-5eb9-327c-973d-f81ee2777ed2 | -3.68225 | -60.61868 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d66e3a4-907d-3230-9cf7-6d1800bc5467 | -3.36634 | -61.32826 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd451bb4-97e3-3953-8b7a-d5f41e4d2fd0 | -6.15642 | -57.69591 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86188d11-ba86-3327-bdb1-9ef164bc27cc | -3.6081 | -59.06186 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4e9b943-1bd6-3cdd-9ffd-f53f2c952769 | -11.07826 | -54.0298 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d0df203-2b2e-3450-acdb-a26d79e2dff3 | -13.88971 | -48.57737 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 472d9332-342b-3fed-9745-a039edeba192 | -6.12224 | -57.75319 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d6d67ff-0227-3fc3-a6a0-e954ea927e5f | -5.8509 | -53.5423 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10c74e30-91da-3db7-b26d-f8e82148aaf9 | -10.87927 | -53.98479 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 026179ac-c6aa-3fe9-bf62-33cf6dce4453 | -5.85689 | -53.53331 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bec56261-7393-3352-86db-3b16bb896f9e | -5.84354 | -53.56096 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7d3b84c1-b22a-3b2d-ad26-2b3feb38997c | -3.37808 | -61.29738 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feb3fdb7-3115-39e5-ab71-59f92a928a21 | -5.76916 | -57.45766 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0d5080a-5d33-3327-9811-20ecc14bf2ed | -7.17128 | -47.4604 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d78e2f97-f892-3a85-a548-c900cd8875a8 | -5.84749 | -53.56637 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49e73c05-a67b-3fa2-8ce1-6f7abf833be2 | -6.30446 | -47.63379 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7afcdf51-259f-3eca-bfc0-491af01e08cb | -11.7229 | -54.55907 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f51ec634-f06a-3cd4-9b56-c5b90d3502a9 | -5.85482 | -53.54788 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4666454c-f4c1-31b7-b60b-07a7ff6b7e78 | -10.9256 | -53.96939 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fff805c5-546d-3f4d-9da9-10efc762cff3 | -3.60476 | -59.06134 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82dd0a9b-c3c0-3cdd-8d4c-9162239c99f4 | -7.16014 | -47.48269 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a6c5d2af-f822-35af-9889-89bb70ae57cb | -6.07124 | -57.72879 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 311d5e7b-b750-3520-bd79-e1814495d647 | -6.09271 | -55.5654 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b8e5a49-7334-3f0e-9430-5c2399dc435d | -11.13831 | -54.02198 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eded4afa-346b-3038-8e14-c4516dc176d5 | -5.33038 | -50.09474 | 2026-09-20 05:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5fc19f6-f892-3fec-8d9f-4200d2b6c290 | -11.10309 | -54.02785 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a8298b7b-3c2c-3d85-82e4-42a2aba4af03 | -11.72824 | -54.55468 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb1c615a-8e58-35b4-842a-ab34b9764f59 | -3.69049 | -60.60935 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda4dca2-5e40-3524-818e-dad2ff8a2276 | -11.69677 | -54.55838 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b673d7d-2828-3ff1-96b4-df9a54e8722f | -11.13902 | -54.0167 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d794869-4916-342c-a772-df7911946bb1 | -5.85158 | -53.53745 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d54e66db-b09b-38ee-a6c8-dd650d225b06 | -10.92004 | -53.97415 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c38c0341-7033-3c5f-adc7-7793d615c015 | -3.95167 | -59.34755 | 2026-09-20 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 226cc8a8-734d-3933-b9bf-53801e9b69f4 | -5.89306 | -53.64178 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d5bac89-d373-3924-8fb6-dde77aa42e1b | -13.73419 | -48.78344 | 2026-09-20 05:25:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6d5d818-c0b9-37eb-922f-15f2cbf6db52 | -11.38739 | -51.42326 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 720398f7-313d-3ec0-abe9-7047e101836d | -6.32547 | -47.62538 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f8a6c74b-b9af-3357-8b51-92e1f6d74445 | -4.42524 | -55.51172 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4365effa-7f58-3e04-aef2-9ba1d38c951a | -3.854 | -58.59779 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2754438-26d1-383a-b145-f64344b7204a | -10.87008 | -54.09183 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 004b4f82-4ada-3e6f-880d-dc5637d6640f | -10.87487 | -54.09251 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8522e346-149b-3d03-aca5-47608c58cfa5 | -5.85413 | -53.55276 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c978da8f-0bb1-3d5d-b04b-0d1c37a5a525 | -6.11633 | -57.74405 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README99.md)
