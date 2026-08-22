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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9e5ab25-62f2-3167-95af-0b0d6639bc3b | -5.58969 | -44.00326 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4b315d42-bae8-3c40-8e4e-bea78f108471 | -4.90447 | -45.24845 | 2026-08-22 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0df7a816-f4d6-320d-9952-6671fe1541d1 | -5.52832 | -46.61385 | 2026-08-22 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8051442-d2c1-313f-851b-87ce2606014e | -7.08202 | -44.99452 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e4f26e6-7bd9-32c6-9750-6fda94d71270 | -2.45218 | -48.56657 | 2026-08-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 089c7f4d-5ba8-3623-87b2-ad247d54f6aa | -5.60345 | -44.02864 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddb28416-47c3-36c9-bf17-b64e83d536bc | -5.64737 | -45.19132 | 2026-08-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cde06385-4de1-3d73-82c6-9396a5b24774 | -5.60799 | -44.01685 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98a7858f-b3b8-3d0b-94f3-82e2d10ff6b4 | -5.81371 | -43.79662 | 2026-08-22 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4687ce55-5097-340c-94a9-09de508ec2a1 | -6.26838 | -43.27335 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2638feba-0870-30cc-8a91-4c5c4e0878ab | -4.71932 | -42.77021 | 2026-08-22 04:25:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f117467-b9ab-3c53-8f70-5ed90f6e7b6b | -5.85941 | -47.75198 | 2026-08-22 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 489620cf-beb6-3ae6-a5d0-cc4497787ba0 | -3.54204 | -48.18246 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86090fa4-d429-3b03-ba52-097b3cf8e94c | -4.5283 | -54.86202 | 2026-08-22 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 002e805b-c469-35f7-aaa8-30631bf0922c | -5.82777 | -43.48895 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3105617e-000a-3b8e-89e0-9b4efd154673 | -5.60463 | -44.02104 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a763ad20-1684-340a-89a0-ee2f269cfa1d | -7.17535 | -44.29407 | 2026-08-22 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f52ac67c-591c-3999-899e-d518828370fb | -1.98254 | -56.46351 | 2026-08-22 04:25:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e352bba8-8fa9-3ae1-b0ec-ace8da7a60c6 | -6.02631 | -43.10925 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2d26451-fe9d-32ef-a787-62601f7ff857 | -5.80109 | -43.64289 | 2026-08-22 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f579d724-747b-383a-8710-1d9ee2137efd | -5.55513 | -44.11373 | 2026-08-22 04:25:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bdf423b-e8d7-3eec-8ca9-f91df274bc2e | -5.22265 | -47.43102 | 2026-08-22 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d00433c-de85-31be-b852-b17f3cd3e27d | -6.17137 | -43.77683 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae3ea629-cf04-3206-83a9-9b491f3d3309 | -5.60454 | -44.01631 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db2919a2-e47a-35c2-a562-6370ec5c11fa | -5.43405 | -44.87947 | 2026-08-22 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a7a6e47-53e0-31f4-99f0-c5ce136c47b1 | -6.7223 | -48.11516 | 2026-08-22 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9fd70eb0-ac19-3a4b-b299-1111c0ddb4ee | -4.93625 | -41.98192 | 2026-08-22 04:25:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 30e15538-35b3-3940-ae3a-49cfce3c40ac | -3.18445 | -48.0178 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e5e84a7-ecaa-3b71-bea8-dda9e0df73e9 | -2.56958 | -47.24297 | 2026-08-22 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a173d734-39e5-320e-82e5-db718298ec1e | -3.01589 | -51.05835 | 2026-08-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5648d4ee-e926-3920-89fa-5294f5250256 | -5.86294 | -45.14142 | 2026-08-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bd0771f-88b9-34c3-b658-28376adb6dd5 | -6.77927 | -42.87461 | 2026-08-22 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| de58d10e-1d75-3e8a-bd01-63978f9498fe | -3.03855 | -48.41253 | 2026-08-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8c523c25-1aaf-35f4-9aa7-042ddf3f286d | -6.4006 | -49.81167 | 2026-08-22 04:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5356bb77-cb8b-304c-97c8-2bcdea632d0f | -4.69336 | -42.54199 | 2026-08-22 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5fff0127-a651-3884-b852-c7e17557eebc | -5.59198 | -44.01135 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57f68820-9afe-312f-9183-6a0ec144547b | -4.65773 | -43.13466 | 2026-08-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f47412fe-feb2-3609-93ea-0863c5acde51 | -6.78979 | -42.67212 | 2026-08-22 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 96539596-86df-32f1-826f-f8b411ebe2a2 | -5.86518 | -45.14902 | 2026-08-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4278ca62-9c28-39b8-aec1-27b16b1b2271 | -2.56221 | -47.24556 | 2026-08-22 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6cdec4b-f7cb-300b-b557-c5619a438e55 | -5.61093 | -45.71455 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14bc041d-1372-3c13-8777-61c3799660f9 | -5.58701 | -45.67184 | 2026-08-22 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f691df47-4efc-367e-926e-536892c72e79 | -5.01737 | -47.07548 | 2026-08-22 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f3f364d-cba7-3065-aa1b-77116d69baf8 | -6.88164 | -43.74899 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 07fba8f0-1d95-38b1-91b1-c9c340250d72 | -9.26997 | -45.64909 | 2026-08-22 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 008bb8c0-ef11-3436-9739-023c163fa888 | -12.27641 | -43.17213 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6bf55511-b3b9-3509-8636-366821e1ea18 | -11.59564 | -45.20564 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daf6629c-16d1-36b9-a9c4-d33805109ee6 | -6.80004 | -59.43009 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 2497b793-deab-3530-8215-bbb504966e86 | -6.78965 | -58.64786 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5730ca9a-4466-39c0-9a28-69e0dcd26b63 | -6.75214 | -58.66697 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 11bdab53-40d3-3500-808a-e7f6441173d9 | -8.02721 | -51.7995 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06ceea64-86cf-392a-8d6c-67db2a404812 | -6.43066 | -54.95763 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa260d53-2e99-3270-acd8-6cd364c988b2 | -6.76438 | -58.67658 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| de915cf4-2c1d-3831-a6f2-546d89ef0121 | -6.95353 | -59.3099 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7f088e7-1c04-3536-932c-a89e0461b864 | -6.89234 | -56.43879 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f95472cf-19dd-3ca9-85b4-e53eedeb3579 | -6.43915 | -54.95189 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63c4b964-7a4b-3b9d-8d9a-f0cde1701c68 | -9.44149 | -51.6055 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 024bf0a9-23e9-38bf-9b95-c722ecb4c7af | -8.51566 | -55.32597 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47fd7f0f-550f-3f63-bdbe-3d7c410741fb | -10.80628 | -50.97549 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 174324df-3aa6-373f-960b-cec5573e81d3 | -8.95517 | -50.72953 | 2026-08-22 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09f60332-af00-3859-b5dc-c901815363f2 | -6.76784 | -58.69378 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ffba77b-653e-3e2c-af94-3dd8e00e9bf2 | -8.63046 | -54.72972 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ace00df5-279d-3371-a1ce-6d937c36c72c | -9.44629 | -51.64797 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28220d14-502c-364c-93ba-1c4bea184744 | -8.34096 | -46.48074 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14e3d5b4-4b66-32b5-bcea-f82f26d13697 | -10.29307 | -48.21239 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca1aa609-3507-3815-a4d9-6179c70ff480 | -8.11754 | -47.17108 | 2026-08-22 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0847cca2-01a5-3f58-8de7-2ad605f25519 | -8.52242 | -54.81518 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af0530e9-38a4-3bd6-a62e-f11c20cae983 | -9.44703 | -51.59643 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8625e6c6-d769-36b4-9f54-5ca72f7fca2e | -8.10279 | -51.65531 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f90075ee-8dbd-39b8-b25c-553e46da78d0 | -9.1013 | -60.9197 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bd03ef3-1a39-3d71-8683-1de160594585 | -11.10475 | -49.89225 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10929abb-3711-328d-8195-97f0879aacf1 | -8.10306 | -50.04685 | 2026-08-22 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e59e6221-6942-313f-b8a5-a47b6acbc7d5 | -12.77334 | -48.40357 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a739309-c3c8-3550-a37a-8c9ecf8a6754 | -9.43973 | -51.61583 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5daabff-d0e0-3f4c-a833-1a96725f586a | -7.54957 | -55.56283 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ee665ad-58df-37e3-a5b8-aace02725c5a | -11.5936 | -46.56726 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1b5eb11-18cc-30db-a008-c2fedf90165d | -8.53187 | -55.32268 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3d8725f-a378-31ec-a65f-f695331046e0 | -6.75447 | -58.65841 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d0aaae2b-de02-3b9b-bfc1-4ec8c46ff337 | -6.81786 | -59.40873 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b7355961-ae04-3a89-b56e-873b89709a80 | -8.61493 | -54.73286 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7f490f3-eacc-3c80-b00b-b793c7b1f6f2 | -6.11884 | -59.91874 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f1e4ddc8-cfae-375e-92a5-06fd4695c0af | -12.76893 | -48.38838 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07166d0d-4b17-3af7-b5ed-ec3e2082c57a | -6.43966 | -54.9489 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98357dd7-34e7-33fa-8546-fd60a835790f | -6.7961 | -59.42783 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 99cb2775-5cb2-32a1-9595-076758a73a8a | -6.4363 | -54.95552 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84694fc3-78c6-3f90-841d-a5961ed4dea5 | -12.25554 | -43.17952 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8b720402-887f-30ee-9fd0-3c31cc1253d1 | -6.76038 | -58.69809 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b39d263-08d8-39f7-aecf-9791b71b2c02 | -7.25808 | -49.9137 | 2026-08-22 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8c6be7b-c2db-3c15-ac16-4c7f0cb9cec8 | -6.78426 | -59.44025 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c236346-28bb-39f5-b2ac-aefd3ad3c653 | -10.3074 | -48.22964 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bcf690e-1640-31af-93ea-9df6555c3543 | -9.10439 | -60.91968 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e61fa6b-c5f4-360c-bfe3-ba30b4c8ea70 | -8.5531 | -54.85529 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2dde95cd-2d02-3587-a37f-a663bdfc86bd | -10.51712 | -50.7715 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bde567c9-8e62-3261-ac79-b4de0586861b | -10.30579 | -48.21834 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c86ee14-546b-3c08-b7f8-2e37b47d87d1 | -7.3519 | -55.67151 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f997e73-8cfa-3e19-8b5f-510d9a1a0785 | -6.10817 | -59.9473 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b26f7946-6cad-3c58-8f19-86b822465545 | -10.0439 | -59.46019 | 2026-08-22 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b73348ad-8447-3d9c-b0aa-9f7d2da59321 | -8.8053 | -48.54496 | 2026-08-22 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d22618b-a9f0-3c84-85f8-9540c64d150a | -6.86896 | -59.44711 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6b2f8ca-8162-36a9-9098-90323c8bb6bc | -8.99605 | -50.73656 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README20.md)
