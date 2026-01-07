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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35ceccc1-f80b-3611-beaf-2af43de5b1b1 | -2.80785 | -52.95041 | 2026-01-07 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c16e68cd-a95a-3448-934b-e20c34baa71f | -0.9437 | -47.16529 | 2026-01-07 04:31:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd2bbe20-44de-3add-836f-ecf22ad05f21 | -1.91056 | -46.95792 | 2026-01-07 04:31:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32e2fcf1-d884-3a2c-90c6-da74ecf449dc | -2.7479 | -54.93231 | 2026-01-07 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e4a6ab1-346f-374e-a7db-eab190625629 | -1.19831 | -46.5859 | 2026-01-07 04:31:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 212ead25-c23c-39dd-80ef-c83f38fa7f08 | -3.31904 | -50.52814 | 2026-01-07 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 603cf4b9-1081-34fa-9655-bb5e1e337807 | -1.19501 | -53.77005 | 2026-01-07 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41373281-1fef-35fd-9948-c07208d52487 | -1.59598 | -53.99186 | 2026-01-07 04:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ad5633c7-e450-342c-b623-ecdb243826ed | -4.2359 | -45.01342 | 2026-01-07 04:31:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90be40eb-06b9-3d1e-88ed-6ac1271f6eee | -2.99339 | -48.08055 | 2026-01-07 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64c9ee83-eac3-3dac-91b9-dc5749490d17 | -0.08551 | -51.28125 | 2026-01-07 04:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a201e04-567f-335a-aaad-b76dcf27a5cd | -3.54105 | -49.4426 | 2026-01-07 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f233d842-a06b-3b28-88c3-ef93de5a8a9b | -2.69163 | -48.98813 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e502c27-19c5-37f2-9a39-9ab6586fb1e9 | -2.92555 | -48.22771 | 2026-01-07 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a449ddb-e4c0-3d05-9aaf-367d6aece067 | -2.16425 | -51.99322 | 2026-01-07 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f39314b-6158-3957-8d91-997b17459080 | -2.1608 | -51.98909 | 2026-01-07 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df83e8f2-c22d-37a2-a909-98c8e3895058 | -1.71189 | -45.24768 | 2026-01-07 04:31:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dca725d1-2b7d-3f9b-a65c-420bffda207b | -1.02561 | -47.05469 | 2026-01-07 04:31:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4fc922f-23d4-3663-8492-8ab3d1963a83 | -3.066 | -44.94846 | 2026-01-07 04:31:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 961ea01c-3e46-3e6a-a0a2-fbb28acd6498 | -2.73642 | -54.94147 | 2026-01-07 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28e1bf6a-a4ed-3748-be54-38dd38aaa3f2 | -2.65274 | -51.82631 | 2026-01-07 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad3cf9c-aa13-33c9-9aa0-c1ad2faef46b | -4.03733 | -45.50132 | 2026-01-07 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c738e65d-2730-3737-9518-097931c77e2b | -0.52124 | -48.52567 | 2026-01-07 04:31:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99ccf8eb-be87-32be-aba1-c8cdacaa20f4 | -2.73554 | -54.9468 | 2026-01-07 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33b3a06a-1697-30f2-8f0c-84bedd4a3d28 | -2.16481 | -51.98974 | 2026-01-07 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db3d3702-b992-3ea7-a18f-6291ec76bf50 | -2.86095 | -52.81184 | 2026-01-07 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 443ccbf1-5152-3e2b-a064-4c91caa98f52 | -0.99636 | -53.21591 | 2026-01-07 04:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ca34ba48-f3f0-3398-8bbb-911cfcb545eb | -5.81985 | -44.13701 | 2026-01-07 04:33:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ae617c3-0bef-3a5e-bae2-c4a0ed45e209 | -6.34059 | -40.69678 | 2026-01-07 04:33:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0df8e487-9880-324f-9aa8-77554328928a | -6.33808 | -40.70028 | 2026-01-07 04:33:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47b54f71-bd47-39ed-b554-d12c83496c07 | -5.8492 | -43.88493 | 2026-01-07 04:33:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf7ed33a-c4b1-300d-b1f4-f2727aa4e914 | -10.6926 | -40.40305 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3d905f5-b3d6-36da-acf4-ffeecbb96703 | -3.50207 | -54.67895 | 2026-01-07 04:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a72655eb-c999-3310-a42a-58d48b82e04d | -5.51408 | -40.4186 | 2026-01-07 04:33:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fb717fd-f2b9-397d-8269-8965bc076c89 | -10.68667 | -40.40866 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 84fc83b1-d2fa-313d-8bb9-5f6a01ffa168 | -7.14135 | -45.25985 | 2026-01-07 04:33:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af5fd06e-d5c0-35e7-9afa-5c5d06c98d0b | -6.33883 | -40.69523 | 2026-01-07 04:33:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9b9754e3-2a19-3bdd-8f2d-75570c367dac | -3.03237 | -54.54476 | 2026-01-07 04:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55a5a6ca-f086-32e0-83ba-cc72f1584d0d | -5.81919 | -44.14144 | 2026-01-07 04:33:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69b632bf-9a9c-388f-8fa8-c2df68e00e36 | -5.82157 | -44.13964 | 2026-01-07 04:33:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b035d456-0b46-3aa9-8e9b-ffc819eec016 | -5.51882 | -40.41928 | 2026-01-07 04:33:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1520065-7918-368b-8c1f-0230f88acfb2 | -5.5204 | -40.41688 | 2026-01-07 04:33:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3611814e-55a1-3010-bd9e-62558e56861f | -6.16411 | -46.10475 | 2026-01-07 04:33:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d3d518a-6385-3821-87bd-34f56c969c08 | -6.96146 | -46.22496 | 2026-01-07 04:33:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08b255d8-f9df-3183-9a2a-9391db3fedef | -10.36887 | -39.06688 | 2026-01-07 04:33:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 570af06b-6870-3aff-b0b4-73298d5bd882 | -10.68701 | -40.40605 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 28c030ee-f0d6-3a1a-84fb-204541537587 | -10.68198 | -40.40465 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b015769-d614-36a6-806d-4de9b2c7d62d | -5.82225 | -44.1352 | 2026-01-07 04:33:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a055469b-6ef5-3013-8898-839d50b8601b | -5.82358 | -44.13757 | 2026-01-07 04:33:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85149432-345e-307a-9900-81ecb3c42ef4 | -10.68131 | -40.40987 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab795dab-75f1-34e7-8e5e-a945994d7458 | -5.81784 | -44.13906 | 2026-01-07 04:33:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01965925-1e9a-3ae1-a051-32008e50f81f | -5.42596 | -44.22931 | 2026-01-07 04:33:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8a98eeb-c2c8-352d-a282-79148f7e7101 | -4.90984 | -43.29334 | 2026-01-07 04:33:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18462249-7d53-38bf-90ce-fa6df87fb172 | -10.68635 | -40.41121 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3ad04400-6f1a-3583-b1ce-55b3c4060867 | -10.6922 | -40.40615 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1581d851-fec2-383f-976e-b1afeb17aee0 | -5.82424 | -44.1331 | 2026-01-07 04:33:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e50d8fe-97d6-36b5-8c2a-916a399b5295 | -10.36838 | -39.07068 | 2026-01-07 04:33:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6eb4d5f-e828-3e67-a23a-ecbb84ae568a | -3.84158 | -50.05514 | 2026-01-07 04:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07ca93bd-71ab-3059-a30e-7cc75bb19358 | -6.96203 | -46.22122 | 2026-01-07 04:33:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c13d886-3efb-3671-80f5-e5c92de90a50 | -5.38052 | -50.48311 | 2026-01-07 04:33:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4330c095-ac53-32eb-8ad9-007c2e51f22c | -3.03318 | -54.53986 | 2026-01-07 04:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 433494e0-0c48-35a2-8091-710d6aae95a5 | -5.46047 | -45.28362 | 2026-01-07 04:33:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d855a0f-8e49-319b-a910-eda3ac18fbe1 | -10.68164 | -40.40729 | 2026-01-07 04:33:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c301a595-7024-35c0-bbd6-020d88bae279 | -6.16469 | -46.10105 | 2026-01-07 04:33:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24ef23e9-e705-38b5-972b-2a29bd025a49 | -5.97353 | -44.2898 | 2026-01-07 04:33:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bc44e98-500e-3dec-b4e4-ef237ab918f2 | -3.42418 | -53.41985 | 2026-01-07 04:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94e13bc1-3d3b-31d7-b433-1e06ab3c7114 | -6.33988 | -40.70182 | 2026-01-07 04:33:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba0a01ac-5158-3a8a-9455-d5dee471a291 | -5.51566 | -40.41618 | 2026-01-07 04:33:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 21a153dc-56b3-3283-a02f-588cb609b769 | -16.3159 | -57.56167 | 2026-01-07 04:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| dde9b4b3-c16a-3424-93f9-82ffc4b57ba6 | -16.26115 | -56.88645 | 2026-01-07 04:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d75bedfb-fd3a-3be0-a60d-c14b98543cb7 | -13.37962 | -53.55464 | 2026-01-07 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 496e8e7c-8863-3da9-b9ec-96df069465bf | -16.04391 | -59.21111 | 2026-01-07 04:36:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1b0f92f-d336-3824-ad02-102cf1a736ce | -16.31132 | -57.564 | 2026-01-07 04:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 597c4c3e-5656-3e7d-b472-d1c9dc5196e2 | -16.0489 | -59.21279 | 2026-01-07 04:36:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc7f4721-cb8d-3fbd-ac54-83d337f04ed2 | -16.3159 | -57.56494 | 2026-01-07 04:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6ee46b40-ec8a-38b8-bf89-4a34df49faeb | -16.3149 | -57.56674 | 2026-01-07 04:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ef05ecd6-b990-3bef-b3d6-9039da76625c | -22.03335 | -49.46966 | 2026-01-07 04:38:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ca312a8-cc2f-3fce-9f2c-070978ada876 | -21.12556 | -53.58397 | 2026-01-07 04:38:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5f09409-537c-37ef-8bb8-b706785dcfd1 | -21.53985 | -57.53838 | 2026-01-07 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 998c78ea-aa25-3cae-a3ec-6acf4ca960f7 | -24.72922 | -51.19456 | 2026-01-07 04:38:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 22632157-a564-3c5a-8dfd-d2d435be8a5a | -20.5315 | -57.98547 | 2026-01-07 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5d89b3b4-c6c7-3e67-949c-f0f1af0b5e25 | -22.96655 | -48.6842 | 2026-01-07 04:38:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2174ee0d-42ba-383c-967f-3895b74c8f2a | -24.5554 | -51.95961 | 2026-01-07 04:38:00 | NOAA-20 | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37403d52-8922-32e3-8f11-79ad5422d57c | -21.20144 | -56.93269 | 2026-01-07 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9102874-dfb6-3c6f-ba45-f85c3d51ad38 | -21.72445 | -52.24846 | 2026-01-07 04:38:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 40726b67-cbe8-32fd-b55d-7418818d27c1 | -20.80782 | -49.82006 | 2026-01-07 04:38:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 28226a0e-c231-3d86-af0c-57dc2a9c588d | -22.04057 | -55.51745 | 2026-01-07 04:38:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da3d887-a978-355a-bd6c-f67874cf4c79 | -20.22288 | -50.79653 | 2026-01-07 04:38:00 | NOAA-20 | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8ca493d0-e326-307a-95de-21263edb4fc6 | -19.17289 | -57.54147 | 2026-01-07 04:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 788d4dd8-2a39-393c-a5e0-46a31716f1e9 | -20.81121 | -49.82063 | 2026-01-07 04:38:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 8c7a4677-58a9-3b74-9e18-91a277b2b329 | -21.53568 | -57.53756 | 2026-01-07 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ed749bd-78b2-3b38-bed2-f822b67b6be0 | -20.54105 | -57.98299 | 2026-01-07 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f5431344-875a-3eea-8cdb-4e8e024c8c1d | -20.53584 | -57.98646 | 2026-01-07 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6ec644cd-c500-3940-bfb0-03ff626f4ea8 | -22.49415 | -46.94412 | 2026-01-07 04:38:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2aab3c3-254d-3dc3-9754-b70a9951ce70 | -21.59168 | -48.6783 | 2026-01-07 04:38:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03036559-bf48-3a8b-b52b-752baf644853 | -22.73278 | -49.35321 | 2026-01-07 04:38:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1993d9a7-00a6-3e08-8bcc-1de36cc4440a | -21.25256 | -48.65499 | 2026-01-07 04:38:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a5eec90a-e100-32c1-8aa7-871c45dfb4e1 | -16.59784 | -58.21303 | 2026-01-07 04:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5afadecf-2fab-33fa-a22c-04d817ce1aa4 | -20.96527 | -48.77535 | 2026-01-07 04:38:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7840768f-526d-38c5-aee1-832bec9a2205 | -16.59682 | -58.21825 | 2026-01-07 04:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
