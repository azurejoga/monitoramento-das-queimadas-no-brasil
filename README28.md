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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5efbc1d3-e71d-351c-a80f-e154243f75e6 | -6.32559 | -43.45476 | 2024-10-30 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd915902-19d9-3dc0-92d5-b8dedd23ae73 | -6.32527 | -43.45143 | 2024-10-30 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 678c50cc-7a08-3e9b-a742-df8252ac3a22 | -6.3244 | -43.45618 | 2024-10-30 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72fb7688-3531-38c7-9f9d-05963970294f | -4.25496 | -43.44628 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3feb0791-d80f-3e13-a65d-8e9045e90b99 | -6.31949 | -43.45334 | 2024-10-30 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d10be3a8-c5cb-3efd-995e-c6425f58f44f | -5.83344 | -43.65223 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e792cdd-8a46-3b8e-877f-368e4e9368b5 | -5.83053 | -43.65011 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c93888d-22d3-3942-8906-e1344fbed547 | -5.82964 | -43.65513 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 624a67ea-3a73-3a07-9277-bbc71d5ba751 | -5.69679 | -43.68982 | 2024-10-30 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a15fe0df-1640-34c2-bb88-ef90da017aa4 | -5.60745 | -41.72637 | 2024-10-30 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 434b87f4-90cd-3d15-8c40-84f8dbacf474 | -5.60185 | -41.72545 | 2024-10-30 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6b2c79bc-8014-30a6-93a0-472cad47e623 | -5.57255 | -43.71368 | 2024-10-30 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f370f3ce-7fac-3400-a8e3-9a30345081e1 | -5.56129 | -37.34658 | 2024-10-30 03:28:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a2a8a096-10c5-35bd-a32c-5178882e8db7 | -5.47387 | -39.64658 | 2024-10-30 03:28:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df36264d-a3f8-34bf-addf-05b6397435fb | -5.46821 | -40.88539 | 2024-10-30 03:28:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 333e2c0f-648a-3610-a9df-0f5d925c67d9 | -5.27575 | -41.0269 | 2024-10-30 03:28:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4b8df5de-2938-3eae-8285-8f102ecafa23 | -5.27514 | -41.03043 | 2024-10-30 03:28:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3b261e36-5feb-38a4-80de-20a4d565886a | -4.93523 | -43.18758 | 2024-10-30 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b14559ab-8154-3875-acd2-03b4ba25ca44 | -4.93439 | -43.19241 | 2024-10-30 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29facd17-fa12-3bdf-bec5-7552fea920b4 | -4.92821 | -43.19122 | 2024-10-30 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57fa47e1-f1bd-3e44-9646-071003af565d | -4.92738 | -43.19599 | 2024-10-30 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b0be52e-4c7c-325a-b4b0-3acd60ae531f | -4.85061 | -42.47566 | 2024-10-30 03:28:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 70e14770-e43c-3b11-a85b-cbfaf5a1ffc9 | -4.84987 | -42.47997 | 2024-10-30 03:28:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 75c158e4-eee3-32c4-b7d7-816c30d89c15 | -4.52283 | -42.05866 | 2024-10-30 03:28:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c75c6f45-f5df-3a72-ba5c-7e46d6596720 | -4.52282 | -42.05822 | 2024-10-30 03:28:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0d9f3abf-b3c5-37b3-9d36-73e29fd51b52 | -4.52213 | -42.0628 | 2024-10-30 03:28:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f9a0919a-86c1-3bac-ab05-b77b733265fd | -4.52209 | -42.06234 | 2024-10-30 03:28:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f36381a4-5a21-32b5-affa-0c416f5e6efd | -4.35032 | -43.78395 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 290d35f4-6cab-3b3f-9735-1aa51aefa571 | -4.34998 | -43.785 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea07a91a-bd6e-3535-a2ab-150e9afee1ae | -4.34935 | -43.78968 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b094f289-3f27-3268-bf46-a2b4444f1c38 | -4.34896 | -43.79074 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6334caa7-4709-3595-a15d-afbf01c8960e | -4.34386 | -43.78269 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3f604e0-8912-3a2d-a304-83036e34f2b2 | -4.34353 | -43.78373 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef2b4625-2f95-3ad6-94b8-736a344d40e2 | -4.34293 | -43.78814 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fe98e7c-2a7c-36e8-a5d1-461618816040 | -4.34254 | -43.78926 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6664dc05-5cf8-3dc2-bf1e-560b658fd08a | -4.33702 | -43.78275 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 786a6b4b-89c9-3ea1-a664-c53dfe144908 | -4.33647 | -43.78688 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe84c3ab-5cc3-375b-8182-eb5004e4d6fc | -4.33609 | -43.78797 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae1277d5-e11b-38a4-8633-d5676e7b4ae4 | -4.33548 | -43.79272 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c362a292-3aaf-3e4e-9149-09bc1b01a6af | -4.32958 | -43.78702 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ad9fcb4-22be-3bea-ba22-97f94f772a09 | -4.2693 | -43.45216 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f556dc2-246d-341d-a3d2-00bb3aa8d037 | -4.26859 | -43.44322 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2d60f4f-a388-320e-8ce4-1d21bb1a55b5 | -4.26835 | -43.45744 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdaf128c-b409-3e02-980b-bbc7691a18e5 | -4.26765 | -43.44865 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2d3a06af-6632-3f55-89fb-9ce4f1f59b94 | -4.26671 | -43.45416 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 57a4aea5-8fa2-3a6f-ae55-794f5dbf8247 | -4.26582 | -43.45938 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45c34ff3-2f4c-39e7-902f-b6678e07d209 | -4.26394 | -43.44548 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 86160115-7d50-3006-b19c-7d326643fde4 | -4.26297 | -43.45091 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bd1fd833-b117-304f-afcc-03d546217309 | -4.26223 | -43.44211 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d2b9b52e-6d09-325a-a553-5a799a796a5f | -4.262 | -43.4563 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0326eb80-cb7a-3003-ae51-6b9d904da7bf | -4.26131 | -43.44746 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df3b3574-984a-3707-975a-99d9c83417b8 | -4.26105 | -43.46159 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 024d1316-8fd1-3634-82d2-c0dce7ff8407 | -4.26038 | -43.45286 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e77198b7-f571-3ce1-9d0d-906ea0997f7e | -4.25946 | -43.45822 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6ed2f79e-c15d-31fc-b326-49cc4354f5be | -4.25758 | -43.44439 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 57a45d69-043e-3a56-b2db-9fff023a4799 | -4.25664 | -43.44964 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 808bcedf-04f2-370f-a30a-1f318c094546 | -4.25568 | -43.45497 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 167e32db-90c2-3249-afb2-e8439bc0e1ab | -4.25406 | -43.45156 | 2024-10-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c0e1d052-1bc4-326e-a80f-554e242c2d5e | -3.95852 | -41.47863 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f0986cf-c4de-38f8-bc01-8fb06863d360 | -3.95288 | -41.47766 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6fa115d-4818-32c8-874e-5a616acb43ab | -3.95222 | -41.48156 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8753bdbe-5c31-383f-90ed-cf47c13553a0 | -3.94658 | -41.48063 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 693f897c-54ab-397d-b8f6-d3c056c4a361 | -3.94593 | -41.48449 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08b2406a-7a62-3397-88d7-662af2e5e11f | -3.94332 | -41.5 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ed45ffa-6fa7-3b19-922a-1cf04b579fdb | -3.94267 | -41.50386 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eef14ea8-9696-34e4-aef5-082201cbbd2b | -3.93963 | -41.48738 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fdb64616-9cf9-3071-ae1d-cdcc4f70ba62 | -3.93768 | -41.49897 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 853d9dd2-05b1-3d66-97fc-d1f2ab34dff4 | -3.93703 | -41.50282 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 622d4560-ad0e-363c-8e58-da08295bfe93 | -3.93638 | -41.50669 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca02cb1b-f695-3cdb-98d1-2b08c5d1a371 | -3.93399 | -41.4864 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4a5901da-f8d5-35e0-90f7-942324c4518c | -3.93334 | -41.49026 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2266d369-c003-3678-bd74-55317bb33ab8 | -3.93269 | -41.49411 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c894ce9f-7fe7-3c13-bebd-93f19b869c49 | -3.93204 | -41.49796 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1b22fef9-7597-30d3-b37f-5bedc2a02f9f | -3.85025 | -40.70582 | 2024-10-30 03:28:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 285389ef-0770-3be4-9bf6-5aad5b0492a0 | -3.84968 | -40.70918 | 2024-10-30 03:28:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f1dfed0-2ceb-3152-9297-c69e364ef64d | -3.79398 | -41.61061 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69bfdbce-de54-36fc-bc4c-ce51ae79f0a8 | -3.7883 | -41.60951 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d7f1d64-f6ec-33cb-8e27-558dfd45f9bd | -3.78261 | -41.60845 | 2024-10-30 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d70c67d2-87bd-39e8-abd6-e86a24e294cd | -3.46623 | -42.00153 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d878b7f-4f96-3b62-9104-9f0a3ef88fe7 | -3.46487 | -42.00049 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 438d8cd0-e28d-3501-8618-352013b0441b | -3.46036 | -42.00046 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1accf679-fedf-329a-9b9d-fbb616d6463f | -3.45901 | -41.99943 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d32d6a7e-034a-3d3a-a33a-6dbec7fa3ef3 | -3.44718 | -42.00697 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ab69a8f6-50f3-3a63-ae00-d17f2e8fea40 | -3.44647 | -42.01123 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bc0deb68-2fca-33ab-a7e2-a07cd15da7e2 | -3.44576 | -42.00598 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 52234eaa-ecf2-316d-8a61-e6e4609d2308 | -3.44503 | -42.01021 | 2024-10-30 03:28:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2c070a85-328b-3692-8f8a-b29b0828d5d3 | -3.40299 | -41.63258 | 2024-10-30 03:28:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 74d0b82d-cd48-3963-b208-0ce56e4fabb2 | -3.4023 | -41.6366 | 2024-10-30 03:28:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b8f893bc-728b-330e-9b18-b5e93ad00e0b | -3.40196 | -41.63391 | 2024-10-30 03:28:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 536cede8-d9da-3100-9c47-1b054b255738 | -3.39723 | -41.6317 | 2024-10-30 03:28:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1f9dc81a-0971-3fab-9685-09228719d5e5 | -3.3962 | -41.63301 | 2024-10-30 03:28:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0cd238f9-ec3a-3c42-b2c1-db76622c73fc | -11.14079 | -37.42975 | 2024-10-30 03:28:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bb25f60c-d962-3841-bd7d-6b90492fe9f2 | -10.69611 | -37.05199 | 2024-10-30 03:28:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6df98bd-f8ae-39d0-acb8-c19755ecabc6 | -10.13985 | -36.24553 | 2024-10-30 03:28:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 90adff39-4341-3a25-8846-d28776bcacde | -10.13913 | -36.24983 | 2024-10-30 03:28:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e7ef2c4c-fe76-3a85-a634-109df6a06ae4 | -10.1362 | -36.24497 | 2024-10-30 03:28:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6a6e4335-6f2a-35b6-b7f5-8eed74b80ad7 | -10.13548 | -36.24927 | 2024-10-30 03:28:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7b82bc2d-2ff2-3aa8-a741-2874bccfef17 | -7.54924 | -46.12947 | 2024-10-30 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49dac923-bd76-3930-9a57-eb95fa8f7232 | -7.54789 | -46.1367 | 2024-10-30 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acd3027a-ded0-3d0a-add9-e15acb1a30fe | -7.23361 | -45.53387 | 2024-10-30 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README29.md)
