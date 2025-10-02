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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d28e41-869c-338b-90de-eef481e719ac | -10.0717 | -50.2173 | 2025-10-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e6eb9394-3511-3106-a2aa-a1a323bd3de8 | -7.5934 | -46.7984 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e41234e8-2a73-33bc-a383-29a29c409d21 | -10.222 | -50.2662 | 2025-10-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0b632aab-aaa5-38a0-b86d-b886332a7723 | -7.7944 | -42.5132 | 2025-10-02 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 222.6 |
| 81500700-863c-3424-a5e8-0feb618edd8b | -9.0803 | -46.6992 | 2025-10-02 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4a80f66b-e147-364a-beab-013fe2bb9420 | -9.3199 | -45.7288 | 2025-10-02 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 42310e6a-3657-3f95-9b8c-fdf38fc68202 | -9.9567 | -43.6927 | 2025-10-02 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 197.3 |
| c10711fd-5f4a-3567-8aa3-5712a72eb0c9 | -13.7864 | -48.0524 | 2025-10-02 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 73927a0b-8f6e-391b-a5b3-ebab854228da | -16.0426 | -50.8522 | 2025-10-02 13:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4bb85773-a96d-310e-9cd7-725d902e8cef | -6.7814 | -45.5929 | 2025-10-02 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 1cbc2641-669f-3d67-ba51-07254fea1993 | -9.4086 | -47.5521 | 2025-10-02 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| c375a0d3-8e4c-31a9-8730-3add2aaac125 | -11.9085 | -47.8745 | 2025-10-02 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9b074b81-5515-3b33-baed-5667258e4895 | -12.902 | -46.9299 | 2025-10-02 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2ca8a4c6-b6b4-3dc2-b709-14d4cb5e6da6 | -8.1513 | -44.1397 | 2025-10-02 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 9fb1c7e4-568e-3846-b784-eaaec32518a9 | -12.6536 | -46.8539 | 2025-10-02 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c53053d8-8648-38d1-a585-3dbcac861906 | -11.8238 | -45.0132 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 97fc2bfc-a535-3082-85cd-4f2b6f851ea4 | -14.3114 | -45.9967 | 2025-10-02 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9f217461-a896-3750-8ad8-4c8c6546637a | -14.4757 | -48.4137 | 2025-10-02 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| efe5b3b0-2787-3c63-b6a2-d4064524f8ab | -8.6534 | -47.6943 | 2025-10-02 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 515114d6-f7e2-3a90-b79f-8b2e329bab59 | -7.7941 | -42.5369 | 2025-10-02 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 246.7 |
| 2bde55a3-c3ce-35aa-a346-74cb74437546 | -12.9024 | -46.9073 | 2025-10-02 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7fede2de-29e7-3c9d-9931-fbd3435d456b | -11.2799 | -47.8445 | 2025-10-02 13:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 0432997d-1e7a-3668-9643-9ebd697d7e32 | -7.5661 | -42.656 | 2025-10-02 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| b0c6390c-c7b5-3484-a6a5-5e0561db8eb9 | -8.6722 | -47.6924 | 2025-10-02 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 90b3c572-039e-3bc9-a046-ac2abbf216b0 | -8.6911 | -47.6906 | 2025-10-02 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c5594fff-f0cb-3f3e-85c0-772d92a4bd37 | -14.1921 | -46.1321 | 2025-10-02 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 140.8 |
| e9498c50-3159-3038-9e8b-2fe556dccd4e | -9.3389 | -45.7266 | 2025-10-02 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 157.9 |
| cb9a618c-226a-3751-9f1c-41028544a558 | -15.2738 | -49.3073 | 2025-10-02 13:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 84e675bb-e265-3943-8bda-cb7dbcac207b | -9.9372 | -43.7187 | 2025-10-02 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 284.3 |
| 79946a5f-66ee-3b8c-843b-f6b5ff229c1f | -9.336 | -45.9305 | 2025-10-02 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| eb6b0d4f-e4e5-393e-b890-44f84f1fb439 | -9.9563 | -43.7162 | 2025-10-02 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 319.6 |
| 0d4aef56-b64e-3ac2-9014-620c43dfa4bd | -13.1743 | -47.8093 | 2025-10-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| f4e3518e-656b-3d81-adf3-1eb47fe4d18b | -6.7816 | -45.5703 | 2025-10-02 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fcd5ec90-e79a-3aad-bf3a-b381a17051ca | -10.0906 | -50.2154 | 2025-10-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 49b891b3-3d63-30e1-8f9a-7324db693128 | -9.9182 | -43.7212 | 2025-10-02 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| 8a04df2e-224f-3d4b-bba8-852baba68d0a | -9.4272 | -47.5722 | 2025-10-02 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| cfff4b2d-73a7-3047-83c5-354aec1c713c | -6.6978 | -42.8118 | 2025-10-02 13:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 2e7c5af8-2d82-334a-988d-f95504bab196 | -11.9276 | -47.8719 | 2025-10-02 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 658c261a-3577-3a14-9409-b034076ed0ef | -6.679 | -42.8136 | 2025-10-02 13:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 101bce5f-f292-3325-b669-43079d72ec55 | -11.8242 | -44.9901 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| d67f5c20-9462-3064-ba2a-9e8c11f6f49e | -15.3072 | -45.0477 | 2025-10-02 13:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 95558d20-0f59-3211-8ad1-65f8c3699c2b | -16.0417 | -50.8959 | 2025-10-02 13:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 99f26b4d-3ed1-3edc-84bf-a54754f3f0ce | -13.1735 | -47.854 | 2025-10-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| fe859736-eed2-3f4f-ae34-9502b2febca5 | -7.5746 | -46.8 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 319.7 |
| c6ae2d79-75d6-3dec-9b46-be6c8b6b8aa0 | -12.5001 | -50.2453 | 2025-10-02 13:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 235.9 |
| f360b6ea-1892-3b2f-9809-3d9df45bac7e | -7.8882 | -47.281 | 2025-10-02 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 0f6125a1-ee48-3291-b0ca-622a227f0fc3 | -11.8234 | -45.0364 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 87b6f127-f851-34e6-8624-879a81ad1623 | -12.6729 | -46.851 | 2025-10-02 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 814f8daf-738c-3b93-a486-ea3ab6334022 | -7.7947 | -42.4894 | 2025-10-02 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| ca273ce8-fa8c-3feb-a310-09184085f626 | -7.7755 | -42.5152 | 2025-10-02 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 203.1 |
| 241e2ede-b358-3c0e-93c1-66540ef6f045 | -11.4796 | -44.9943 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 62e2ba6e-9cdb-3817-a536-2d21017501a4 | -7.7752 | -42.539 | 2025-10-02 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 298.7 |
| e5ec8e1b-4e41-31dd-84a2-19b0a05564dc | -14.1917 | -46.1552 | 2025-10-02 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 4e9c3491-598a-3370-aa87-c31eb0a096bc | -7.5744 | -46.8222 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 420.6 |
| ad720cd7-a72e-37f2-83f8-140dc71ed570 | -7.7311 | -46.2289 | 2025-10-02 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4fa0271e-db16-3f5f-b912-d02a59170294 | -14.2924 | -45.977 | 2025-10-02 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| fa111bc3-398d-301c-916c-a93be9832b52 | -10.8625 | -46.5589 | 2025-10-02 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9da95e41-5a34-3e1a-889d-b5100bd41c71 | -12.9024 | -46.9073 | 2025-10-02 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 655ecccc-2fbb-3683-9cac-6e5c8b1bdc9d | -11.8442 | -44.9408 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 9df9bad6-95e1-3501-8d73-e4e260afc293 | -10.1845 | -50.2487 | 2025-10-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| aed68f94-f876-3ee8-ad65-7c25c757598c | -6.6978 | -42.8118 | 2025-10-02 13:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| e5df99d4-5d10-3b2e-81aa-0c9045d5e8d6 | -7.7755 | -42.5152 | 2025-10-02 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 203.2 |
| 7bcca19c-1635-33e6-93e3-29dbc8200847 | -8.5599 | -44.6494 | 2025-10-02 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 3097867c-71a3-35a5-95f0-00b8c3b379a2 | -8.672 | -47.7144 | 2025-10-02 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4ea60232-80eb-38f4-b596-ab1b8b520c28 | -12.6536 | -46.8539 | 2025-10-02 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 54d4158e-c345-3f5a-8ff4-fe94b7a2dbba | -7.7944 | -42.5132 | 2025-10-02 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 221.6 |
| 40cdc1f9-01dc-36ec-986e-6236c9bb6930 | -9.9182 | -43.7212 | 2025-10-02 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 96741176-dde2-3bce-bc69-937a90b76d96 | -15.3072 | -45.0477 | 2025-10-02 13:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 7ca47ca5-5f2b-30cc-924d-64d77a3e0ba9 | -14.4753 | -48.436 | 2025-10-02 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 20a4b5a6-cb49-3894-bc77-71d861a887b2 | -12.7627 | -50.5567 | 2025-10-02 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4250d3c4-41e7-33d2-a385-b75ced09e606 | -9.4272 | -47.5722 | 2025-10-02 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 0c41dc8a-a364-35bf-926f-3f04012057e0 | -16.023 | -50.8553 | 2025-10-02 13:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9c15ba4f-7dc8-3bd5-a7a5-4553599c4350 | -14.7043 | -49.616 | 2025-10-02 13:20:00 | GOES-19 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 39f144e8-16c1-3afd-b00c-2ffe2eff5ea8 | -8.5596 | -44.6724 | 2025-10-02 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a2652aa0-e14a-392a-8d32-973cdadb6883 | -10.937 | -46.6618 | 2025-10-02 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 7bd89b7e-63d0-3501-b9cb-e31d5babd42f | -11.9276 | -47.8719 | 2025-10-02 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 228.7 |
| c22096db-b128-3ffb-ab63-dbc8b8b75c16 | -13.1735 | -47.854 | 2025-10-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a0045c78-6476-30ca-a362-6a2800877676 | -14.425 | -46.1381 | 2025-10-02 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 3f3eee20-9ca6-3d4a-b5c6-5ea9fc8d63b7 | -11.1746 | -47.2805 | 2025-10-02 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| ab59e8c6-ac2d-3790-bdda-e68be86ac257 | -6.2411 | -45.3198 | 2025-10-02 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9a7bb9a9-707f-3153-8d7e-b11c52e6bb31 | -9.3389 | -45.7266 | 2025-10-02 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 22487f64-ac99-3b36-a9c8-bad97cc11874 | -11.4792 | -45.0174 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a83571ec-3657-3829-ae9b-386da513b7a1 | -11.9272 | -47.8941 | 2025-10-02 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 78406ca6-d671-3a0c-ac41-d1145210e642 | -10.2217 | -50.2876 | 2025-10-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b94c1d28-d998-33a4-a59c-fd21e6fd007b | -16.0417 | -50.8959 | 2025-10-02 13:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a4ab3fc0-a768-39b3-9734-9906fc0ca281 | -9.9567 | -43.6927 | 2025-10-02 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 60342fe6-cb8d-365b-b83c-8782582dc708 | -11.8426 | -45.0336 | 2025-10-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 572712ce-64c3-3d4d-b182-b868ee699540 | -8.5204 | -47.8167 | 2025-10-02 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 42d8641e-7cb6-311b-a5e2-d2403f6700fe | -14.4947 | -48.4329 | 2025-10-02 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c11ee4bc-a25c-324d-851c-aa3f0a4d16ab | -7.7947 | -42.4894 | 2025-10-02 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 5d7b89a2-52f9-3979-90b4-b9cddd21e9c5 | -13.1542 | -47.8568 | 2025-10-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| aafb0082-7fc8-3d6a-b7b2-6ee50a9787b1 | -14.5937 | -48.3281 | 2025-10-02 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a0922c46-e5db-3671-912a-ec94162906e4 | -7.5661 | -42.656 | 2025-10-02 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 2a38c101-8883-3bb1-b61f-ce8dbd626b05 | -13.7859 | -48.0748 | 2025-10-02 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ecd5bd00-f123-3cd7-a224-0059b4c1ab24 | -8.6911 | -47.6906 | 2025-10-02 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 701692f3-16b7-3454-ab88-4738d7b0ccb9 | -18.2171 | -53.3392 | 2025-10-02 13:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f5323aee-a007-3170-b54c-b247a343258f | -9.3364 | -45.9079 | 2025-10-02 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 71d2bd49-7204-3a53-b9df-11896014644f | -15.2738 | -49.3073 | 2025-10-02 13:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2160b27c-43ed-3ca1-934b-51578ea45ce1 | -9.9372 | -43.7187 | 2025-10-02 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 262.8 |
| 2a65a388-1c48-3f6e-b05b-b7183124b2a5 | -13.3131 | -47.5876 | 2025-10-02 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |


[Clique aqui para ver as próximas entradas](README154.md)
