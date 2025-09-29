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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21d2bf99-903e-37e9-b20d-4826e3ad6294 | -12.887 | -44.6846 | 2025-09-29 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 33cefbc5-0b74-36b7-b88b-2afb50e374f9 | -11.9247 | -48.0495 | 2025-09-29 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 77de3608-995d-3dbc-951a-3061710291d1 | -7.2999 | -42.8486 | 2025-09-29 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 84979f8f-e905-38f2-ac55-3b643131fe6d | -7.3653 | -42.1058 | 2025-09-29 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 145.6 |
| 25119554-8ec0-33ce-b057-57dacacf925e | -8.5413 | -44.6284 | 2025-09-29 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 188a2cd4-fe90-378e-92ef-56118ddaf1d7 | -5.3645 | -42.851 | 2025-09-29 14:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 23aeae30-7047-39d8-a0a6-378266711946 | -9.7864 | -46.1949 | 2025-09-29 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 09cc0fac-0587-3bb9-bfc9-0cbf9bbf0815 | -8.2474 | -45.5037 | 2025-09-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0edd4bb5-0257-356b-addf-e05a3991d157 | -6.2979 | -45.2475 | 2025-09-29 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b4c30f91-e5b7-3002-beeb-83e59134ce49 | -9.3705 | -47.5781 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c9757122-5d04-325f-9d4a-aa199d0b63d8 | -7.2416 | -42.9957 | 2025-09-29 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 7a823cd9-c6ef-3d8e-9062-ecb9fb36cfab | -11.9782 | -47.1296 | 2025-09-29 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 4cd335a9-96ae-364b-82a4-7e633761171e | -7.2216 | -44.7601 | 2025-09-29 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 60e5b091-6f55-36e8-8eac-19edf9523e4d | -7.6277 | -45.4053 | 2025-09-29 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| cff5c56b-d8fb-30f7-be1d-7b040d34eb87 | -6.4131 | -43.0724 | 2025-09-29 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a03094d4-0e51-3e71-9a64-7e73b6cbf71e | -11.4866 | -43.5219 | 2025-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d2d08f9e-dcf2-3731-8eb2-fba2b1866f00 | -7.4676 | -46.2974 | 2025-09-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 32366823-1b12-3277-9dc8-a234091da640 | -11.4405 | -45.0461 | 2025-09-29 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 4ad6bb8b-7d9d-3213-8db2-2a3c47e2fa4a | -9.4744 | -45.5068 | 2025-09-29 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 973d8121-db13-3982-8332-534f32281175 | -9.301 | -45.7309 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 50026ba6-d8a9-3101-8f2c-317e27e87ef0 | -7.6062 | -47.3498 | 2025-09-29 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| eb20099d-bfbe-30c0-9910-0b3b9081853f | -11.3447 | -45.0597 | 2025-09-29 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 6c649670-01e9-354c-b4c5-f0915e4c5b52 | -10.3257 | -48.2001 | 2025-09-29 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e2b95584-77de-3f04-844c-f6cf80475cdc | -10.4022 | -48.1476 | 2025-09-29 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 293dde8a-7d96-3608-91ff-3bdf5ec25065 | -6.3154 | -43.4548 | 2025-09-29 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a4fdc321-2181-36fe-9b18-66ce37157f52 | -5.7294 | -43.9651 | 2025-09-29 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 83c51abc-fbd1-334e-a353-0e8f155ac523 | -6.2977 | -45.2702 | 2025-09-29 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 7ba4966a-2e79-3019-a797-166a6c41f30d | -13.2346 | -50.9691 | 2025-09-29 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 57d9b76f-be8b-3443-a770-ba095a518d57 | -8.2662 | -45.5018 | 2025-09-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2f5e36f6-a1b8-3e44-b442-0e0469db6a9a | -6.0797 | -42.6064 | 2025-09-29 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 7048029d-5091-37c9-b1f5-ea0e18f9b03b | -5.207 | -43.7714 | 2025-09-29 14:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| caab0f70-c969-3adf-8922-7dbffa8c52af | -7.2605 | -42.9939 | 2025-09-29 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 7fbcfe8a-4479-3cd2-9531-e1b8e317bd7f | -11.46 | -45.0202 | 2025-09-29 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 850af6d2-5b1c-321b-8960-952261d97593 | -15.072 | -45.0693 | 2025-09-29 14:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 0829111d-84a8-3356-995d-221d38389f50 | -13.3796 | -48.1577 | 2025-09-29 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 383.8 |
| 85a496bf-3009-351a-afde-f8b75676e5c1 | -7.6064 | -47.3278 | 2025-09-29 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 758ce5ab-a259-3fdb-b203-e0a1c84de943 | -8.88 | -47.6282 | 2025-09-29 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| daa617e1-36c6-3796-9b88-4a1aa888d00e | -7.8165 | -46.9781 | 2025-09-29 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 717ea79b-0d47-3944-a228-d851f1ea6dbd | -12.9547 | -45.1618 | 2025-09-29 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 3d2ac5c0-5b91-31af-9451-ca3371df96dc | -4.5798 | -37.8505 | 2025-09-29 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 3d0669d7-3bbb-3820-8892-2772ff9d6abf | -9.7643 | -47.7786 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4d3e8a22-bdf4-318e-9cf8-27c4497a4c56 | -7.9816 | -47.3168 | 2025-09-29 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c09d09c7-7b05-3f16-af15-5740954a87f8 | -5.6275 | -44.9115 | 2025-09-29 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 597f6265-755e-3e60-a1bc-6d46cacef852 | -9.9581 | -43.5987 | 2025-09-29 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 8a066e8a-5494-3615-918d-37b4267c515f | -7.5447 | -46.1115 | 2025-09-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8714a4a5-5b23-3632-8e8a-3b30d7f73abd | -4.1491 | -39.998 | 2025-09-29 14:00:00 | GOES-19 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 911bf064-7389-3f20-b3f1-97b88f74d625 | -9.8852 | -45.9122 | 2025-09-29 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 1a2b7aa2-df4c-33d8-a115-2a3cf6e3d6de | -7.3001 | -42.825 | 2025-09-29 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 524af3d8-08bd-384d-b5e9-5e6fe6a3e088 | -9.0721 | -45.892 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 93394a59-aff1-3816-bb3f-c51081630f06 | -9.091 | -45.8899 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f390477b-e6ee-36ee-9f62-4203d71dd4f7 | -6.7782 | -44.0876 | 2025-09-29 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| dec346cd-042a-3f64-8abd-92a92e60d938 | -9.4007 | -54.6984 | 2025-09-29 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 4c850010-a70b-3960-b9de-d6903c817091 | -9.0874 | -47.6074 | 2025-09-29 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 19f84988-321b-3138-a9c4-d4891cea3eb0 | -11.5246 | -43.5397 | 2025-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 1b7f62c8-9952-3a8b-9db3-176e90383ec1 | -6.4317 | -43.0942 | 2025-09-29 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2f353d68-954d-3b44-98eb-73b7e709b3fe | -7.1574 | -45.4932 | 2025-09-29 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 25fb5a91-ffd9-3b87-91a6-53462624bb2e | -9.1105 | -45.8426 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ff2052a9-3662-3a3e-bdde-9ff198f81a01 | -9.9585 | -43.5752 | 2025-09-29 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 24affb9a-0d3d-33c5-b4ef-f4d80bfd12b3 | -9.0724 | -45.8694 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f88aefa3-a120-3872-ba56-8784084a7c45 | -11.5054 | -43.5426 | 2025-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 462.0 |
| 13cf47a2-19e4-3bd8-af15-740e6f4d13f8 | -8.71 | -54.6467 | 2025-09-29 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d31a6b40-ce2e-3d3a-b7d7-97063fa98369 | -14.9097 | -51.065 | 2025-09-29 14:00:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c4442c97-8ce4-37a5-b7cf-51e0581b6413 | -9.764 | -47.8006 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c78fb473-4051-3d3b-a722-3d1d16e07b7f | -8.1614 | -46.3899 | 2025-09-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a99e0cd0-898f-37cf-88cc-75920cf67d50 | -18.4667 | -43.9996 | 2025-09-29 14:00:00 | GOES-19 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 6f79f6b9-7579-3d07-a701-180623bb9751 | -9.7451 | -47.8027 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 9ff2e75a-3d73-3e65-ac5f-eec0d84f2226 | -9.2821 | -45.733 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1298a177-6ac0-3f95-9888-d9f421055268 | -22.6286 | -49.03 | 2025-09-29 14:00:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 221.7 |
| ad24665d-8aea-3215-99ef-ef4b75f19061 | -7.8566 | -46.7527 | 2025-09-29 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 9a78e871-940e-3eda-9c87-5b911a0c2643 | -9.0913 | -45.8673 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2a65df53-20eb-3ca4-b1cf-ea5c48a15f3b | -9.4458 | -47.5923 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f80f3970-d18b-3833-8b51-7c174cad2715 | -7.8378 | -46.7544 | 2025-09-29 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 93aef212-74a3-3e15-a7b4-23806d8265b3 | -7.8163 | -47.0003 | 2025-09-29 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 75a2fbaa-effc-3438-b7b1-d9d313554e60 | -7.5089 | -44.297 | 2025-09-29 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 95176129-bc37-3404-abe3-6f3b3b60c5a0 | -8.9185 | -46.0889 | 2025-09-29 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fd669c24-82d6-3c9a-847e-9ab61370806c | -7.8375 | -46.7766 | 2025-09-29 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 20a57f71-077d-385c-85dd-cc21f4bd036f | -15.0524 | -45.073 | 2025-09-29 14:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| bc0512be-ee6a-3f29-81a7-1040afb745f2 | -13.011 | -49.4423 | 2025-09-29 14:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 26d6b855-431a-393b-b05c-a387b19ac089 | -5.6462 | -44.9102 | 2025-09-29 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| cac45b1e-efd1-3f9c-8412-697893ac8a12 | -8.5221 | -44.6535 | 2025-09-29 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| d2f67b99-9aed-3d1c-bd09-c8ac93caacc0 | -13.3989 | -48.1549 | 2025-09-29 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 37a34ee1-9f15-3aa1-9845-d22cefdb63bd | -7.4488 | -46.299 | 2025-09-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 80932f1e-e0ba-3230-bd7d-0b4565fd8120 | -9.1102 | -45.8653 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a9cd57ba-146c-39fc-9448-4407706bed75 | -7.2813 | -42.8269 | 2025-09-29 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 4f54a86f-aadd-327a-9b89-7ae148c9033d | -9.0685 | -47.6093 | 2025-09-29 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 8b896104-a59f-3e9a-9878-afd331bdd10d | -14.6975 | -45.2327 | 2025-09-29 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| e96917f9-088f-3b12-9fbc-55767f68b182 | -8.2665 | -45.4791 | 2025-09-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4e6b712d-2d23-3ccb-8cc1-c6a4256fa979 | -9.4455 | -47.6144 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c5c024aa-cc0a-3bd3-935a-063f7a80e437 | -9.7454 | -47.7806 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| a7ef2008-1872-3f61-adec-80f572f4c09b | -12.9435 | -46.7655 | 2025-09-29 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| eeefd83b-c141-370b-a3b9-808da1d8e1da | -5.7679 | -43.8467 | 2025-09-29 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 5357d30d-6048-3e63-960c-189cecbb5a1d | -11.3642 | -45.0339 | 2025-09-29 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 6dcb597a-65ac-357c-8267-0b55e5c1ca1b | -13.2346 | -50.9691 | 2025-09-29 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 189.8 |
| e2133028-25e4-334b-8654-cf827f7a4145 | -5.207 | -43.7714 | 2025-09-29 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8bde2967-2dbb-3859-bbe2-b077a033aa3d | -9.3708 | -47.556 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 133d22b4-d2b6-3c53-80d0-29a1b56ea7f5 | -11.3447 | -45.0597 | 2025-09-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 0d5908c6-7bc3-3c17-8f5a-13044b9f6b27 | -7.6277 | -45.4053 | 2025-09-29 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9e59f35a-8c28-3160-9686-c7af79beeef0 | -12.8865 | -44.708 | 2025-09-29 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| beb7f31f-e28a-3378-bfb2-935994983532 | -9.0016 | -51.6875 | 2025-09-29 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 23960c27-1c39-3a43-8bed-114600d7a483 | -9.1105 | -45.8426 | 2025-09-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |


[Clique aqui para ver as próximas entradas](README96.md)
