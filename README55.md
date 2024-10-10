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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c2cd19b-fe28-3efe-813f-dba2c3bc6af5 | -7.0971 | -59.408 | 2024-10-10 04:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 10be0594-c96a-3810-bc1e-452b73209e69 | -7.0785 | -59.428 | 2024-10-10 04:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 17c1024e-eef6-3c8a-b862-3d02aff7b566 | -7.0416 | -59.4296 | 2024-10-10 04:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d79ed37c-5927-3c4f-8bc8-93f47f009fc7 | -7.0417 | -59.4103 | 2024-10-10 04:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| fa5cd81f-d111-30a5-a16b-1b997590b372 | -7.0601 | -59.4095 | 2024-10-10 04:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b8a2c1c0-3ba5-3985-9f04-3a9b9747a7ca | -9.1035 | -61.2769 | 2024-10-10 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8d0c7420-81df-353f-98cd-5e13c70fdc01 | -9.122 | -61.2951 | 2024-10-10 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9906a243-a660-307d-8dfd-027504ed77d2 | -9.1221 | -61.276 | 2024-10-10 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 1a1da10b-4902-3ede-9002-176444a746b6 | -11.0254 | -57.2237 | 2024-10-10 04:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 51999964-887b-3987-bebe-9df5834918e1 | -11.0256 | -57.2038 | 2024-10-10 04:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 40e0f202-54c2-361a-be20-e8f4d1603faf | -11.0443 | -57.2222 | 2024-10-10 04:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d01f6c75-0b22-3b3b-bac2-77200642e0ed | -11.0445 | -57.2023 | 2024-10-10 04:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7fd3ef67-b0ab-39e7-b4da-b05f9ec955d9 | -13.8379 | -44.522 | 2024-10-10 04:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a3096909-53aa-3673-8bf3-f19508b20ee1 | -13.8574 | -44.5185 | 2024-10-10 04:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| e22d5194-74ea-3b53-b5de-29d3d325a460 | -13.8579 | -44.4949 | 2024-10-10 04:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6424c00a-43a3-34d6-9a9f-6aecfe47ed72 | -5.51853 | -42.78745 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57803348-11b3-3fbd-8661-908bb6729440 | -5.2607 | -46.21601 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c38923-df38-3998-8ac1-653748dad43e | -6.37531 | -42.97935 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31a864ca-702f-36f0-93aa-588e07a178d4 | -6.35162 | -43.81449 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7e0feeb-e8e0-3ad3-81c3-aa43011944dc | -6.34774 | -43.81749 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1014acf-73f6-3695-a319-e1970117c0dc | -6.34719 | -43.821 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fef90ef-959b-3161-8073-c64ea5a96d2d | -6.34524 | -43.81722 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7781461d-9bdb-3f24-af7d-5ba0fde19813 | -6.34469 | -43.82073 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff857f41-851d-3db4-b302-5911d387e1ab | -6.326 | -43.45697 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 107ddaaf-f871-38c9-a417-afdd4f7aa853 | -6.26805 | -43.42294 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6649a06-65fc-3826-8b54-db23d6978e3e | -6.2675 | -43.42648 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53aafbb2-382f-3a4c-af58-7cde88bc6138 | -6.26695 | -43.43003 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaeb4cc1-8a58-3a5d-811f-d61743110f20 | -6.26415 | -43.42595 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61a9a7fa-157f-32e7-8f89-6c52266803d4 | -6.26359 | -43.4295 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d0c7697-7026-3f81-b6e2-4f8b58c9484b | -6.24587 | -43.52122 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31aaacb4-ca9f-3a11-8b24-9062a83e9d93 | -6.28689 | -43.81886 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0886c218-4dd3-3f81-864b-174c7fe3a7d3 | -5.85302 | -43.73695 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02993bcc-48a7-35df-8045-d0d2196f961e | -5.85028 | -43.57864 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88c2d2c7-cc7b-3424-8f9c-6ac89fef3faf | -5.84859 | -43.74343 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed8fa0f1-46a1-3235-8a4a-84d4eca1b538 | -6.17281 | -43.70444 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23a8bc9e-a71e-3525-bdd5-fcfbaf444b21 | -6.17227 | -43.70795 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc6d90ca-42f7-3b00-b6b0-e4824359569b | -6.16947 | -43.70392 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 507927a4-7c90-3e21-9656-b6ccb31746ea | -6.16893 | -43.70743 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 045c7e5e-7bdf-36ad-be3e-675f96b46ae8 | -6.16838 | -43.71094 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c9731c9-03e0-39ed-b4bf-4a72f5ff96b4 | -5.84973 | -43.58215 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae4e678c-4836-3908-81b3-fb9226c2c556 | -5.50317 | -43.46747 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cf858c2-92f5-389d-a56a-d98fa3c1d0b8 | -5.56562 | -43.69584 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31dcc2d5-8731-3409-9379-33b6b2496b32 | -5.38691 | -43.62917 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bd4518c-6ae2-3bf7-a104-a2e5066bcf74 | -5.32277 | -43.73351 | 2024-10-10 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 696e0d81-f74f-3f54-ba06-c928b30af755 | -5.12009 | -43.08283 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c84da7cf-a72b-32bb-9bd3-e8539293ab62 | -5.11783 | -43.07522 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bef3ed3-cfd6-3cb3-83d9-875a1451855a | -5.09539 | -42.70444 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d7e2f9f-77ac-3ef7-bbd8-241b9dea225d | -5.09483 | -42.70803 | 2024-10-10 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46a8896b-9ad2-35a7-a3d8-603cc8070dc2 | -5.07208 | -43.14805 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab2c92e6-a7b4-32b3-999d-a3c58aa72e6c | -5.06873 | -43.14753 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 138d4124-c808-3855-a939-52de5bca823e | -5.81241 | -43.23653 | 2024-10-10 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6129041e-e09d-3e92-b541-bf77d55cf310 | -5.58274 | -43.25555 | 2024-10-10 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5e7ad85-0df8-3303-94c6-9862cdb65827 | -5.79984 | -43.94653 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec22d2f8-307e-34c4-913f-5e8bce15af61 | -5.89801 | -43.96893 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f76890-99cb-3696-8d54-150989f500fa | -5.85247 | -43.74045 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50becbae-dda4-392f-a9a8-9f544081f792 | -5.85193 | -43.74395 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da0568db-99c3-35d1-8854-b53c8f48042f | -5.68971 | -43.6367 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 827672c7-c39c-3694-ba63-aede9ec6a589 | -6.72235 | -43.55792 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 610d4f3e-01b5-33db-a8e0-98800c6e2a25 | -6.719 | -43.5574 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee217c87-91bd-371c-8cf4-73a8af90e45d | -6.68895 | -43.45479 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9d7355c5-db43-36ca-a988-c75c8ad0efdf | -6.65437 | -43.52239 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74463a18-5921-3397-ae90-6f323d39ceae | -6.66778 | -43.91041 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6397d9f7-e270-32dd-8e28-aa01aef429c9 | -6.64796 | -43.87164 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1abc24b1-f469-3c2c-a541-c81e3618cfb2 | -6.64558 | -43.79934 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fad6a8f4-e479-3c7f-bac1-b9c3b55732c6 | -6.64503 | -43.80286 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da9a92e0-8390-358c-b78c-8df541f24a62 | -6.64462 | -43.87113 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fecf5d09-5f41-3c44-8cb1-90d4da9a219e | -6.44266 | -42.92622 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d418b675-dad2-357d-8748-4cbee8ea6be3 | -6.44209 | -42.92989 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d129ce4b-e434-3f14-a212-69d7e9e08d6e | -6.47469 | -43.33055 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 236ee356-0e42-368b-b85b-fed6da1f0533 | -6.47132 | -43.33006 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 161be765-6775-31ec-b3d6-a5a3d8fa6a55 | -6.47077 | -43.33361 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81ae9eee-79aa-3308-85a7-9d3ff1b745a4 | -6.4674 | -43.33307 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09a4b7f3-afea-38c2-80f5-95d4b9e62097 | -6.46685 | -43.33661 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8eba275a-9685-3b36-af1d-0a19661234d0 | -6.43104 | -43.78752 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97b90c81-d09e-3b67-bf45-f8933b4af235 | -3.53814 | -43.93988 | 2024-10-10 04:17:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0556ef10-d979-35df-bd5d-b81615528c1e | -3.41532 | -43.19069 | 2024-10-10 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53d4f0ef-55a6-3af3-ab57-7e0133f373c1 | -3.30112 | -43.51051 | 2024-10-10 04:17:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a913b78-bd49-3e51-a184-84ac51d64366 | -3.2978 | -43.50999 | 2024-10-10 04:17:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c531a931-d9b0-3a18-94a3-1b7851633ff7 | -4.44347 | -42.90611 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6d2f67a-1a09-3aaf-9fab-b591864cb3fc | -4.49802 | -43.84235 | 2024-10-10 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c60ee6a6-88ae-34f5-8901-cebf36e7533d | -4.49748 | -43.84581 | 2024-10-10 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80ea5bb2-c2bb-34d6-9735-0492e9811471 | -4.4947 | -43.84183 | 2024-10-10 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 785b7375-ebaf-39c5-971f-50804685c491 | -4.49416 | -43.84529 | 2024-10-10 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eeaa2e7-2f09-37f3-a315-dd0e45daf189 | -4.40565 | -43.52257 | 2024-10-10 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b860eb1-3cd9-379f-9ab7-19cc0fb4c0d6 | -4.40232 | -43.52206 | 2024-10-10 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f340617-b7d2-3603-a50b-6418c5f68f7b | -4.39511 | -43.5245 | 2024-10-10 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23532a02-59b9-3fbe-be67-85a5c3a0b9be | -4.39178 | -43.52398 | 2024-10-10 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73575600-568b-39eb-b268-55e2c3efb47a | -4.36467 | -43.54462 | 2024-10-10 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc3f8db0-4b60-35a7-83d0-31d551f52246 | -4.36419 | -43.56946 | 2024-10-10 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d02cbd0-ec10-3c36-946d-348bdb087c94 | -4.3608 | -43.54758 | 2024-10-10 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d376ba75-19b6-399a-8adb-5a1f450feb08 | -4.02786 | -43.23538 | 2024-10-10 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfd63e46-8a5b-3b4a-b4a3-86d8a819d826 | -4.02659 | -43.39581 | 2024-10-10 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b900e509-3242-3557-ba57-6dec527a1e04 | -4.02452 | -43.23486 | 2024-10-10 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b51c7a4-d8c2-3276-8bec-1f613e48d7aa | -6.90874 | -43.54306 | 2024-10-10 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19c7c69d-ca78-3924-ac8a-1ab4d2b5cf0d | -6.93332 | -44.05551 | 2024-10-10 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24bcfff9-2d2c-30b8-b90e-3f0a081c92ea | -6.92999 | -44.05499 | 2024-10-10 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a63a9d4-16b7-3b1a-a7aa-5217f0708d3f | -6.92944 | -44.05848 | 2024-10-10 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb2a5888-efc4-3f12-846b-46a4494745f5 | -6.89485 | -43.81952 | 2024-10-10 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86e7d750-46bd-3385-abd3-c7005a84fa62 | -6.83473 | -43.6877 | 2024-10-10 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e86e30a-dea2-31aa-857f-751f4a5829d7 | -4.58443 | -37.80751 | 2024-10-10 04:17:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README56.md)
