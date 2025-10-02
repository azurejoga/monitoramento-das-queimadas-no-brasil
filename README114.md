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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74045bd9-d538-3f33-873f-f78a5cb46b5f | -13.14647 | -47.84849 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8ccff736-fb17-38c8-bb31-a024024609e8 | -11.46106 | -45.02232 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ae1aaa1-a1fc-36f6-9f6c-7bef18dd145a | -14.70299 | -48.20563 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7437101-4c39-3ffa-985f-1358c5df190d | -12.81942 | -47.02187 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f48df66-f69e-3608-93b8-5552c4bc14db | -12.71019 | -46.89011 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd2b97aa-b7da-3864-adb6-ee24e89ee817 | -13.40141 | -47.78029 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6b458bb3-f1ea-3df8-836c-c1940b920a1f | -12.27666 | -44.12814 | 2025-10-02 04:51:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cd46bdf-4def-3436-83cc-f4384e434907 | -11.81159 | -44.90726 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc4177c7-64f5-3d28-bc70-1da14c204c6c | -11.47293 | -45.01092 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 760182e5-1f0c-36b6-a858-0914b5c848c4 | -11.08467 | -47.85179 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43fb6212-6e61-3c31-b549-b533f2566c1a | -11.7865 | -47.56255 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4d66424-361f-37d3-83d4-732e4c5360ef | -14.42564 | -46.10362 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ede61788-0bb8-3067-ae6f-bca05722d83f | -16.03573 | -50.91538 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bec0c817-c18c-36a3-974f-4ee49d034e2c | -12.93738 | -46.4353 | 2025-10-02 04:51:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f323bbf-b15d-360e-90d4-cb14c19bdb5b | -10.86942 | -47.81625 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 127eb36d-e2ad-30eb-95f1-ce518014be5b | -13.31388 | -47.19717 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81e8797c-fc36-3651-8433-868929f9af70 | -10.81981 | -46.60695 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dcce001-d7f7-3012-895c-ac74e98250f6 | -14.90614 | -48.3314 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5ee6e61-1644-3d87-aa45-ebb8a8242d9d | -13.06253 | -49.17162 | 2025-10-02 04:51:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31cf55c0-0a2f-3597-8417-4ec5a6bbad9d | -11.6757 | -44.2793 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 011ad15e-1e50-3788-8a48-066b9a8745b1 | -15.22887 | -50.1181 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 071d4ad5-f198-36ac-8bb6-97a008902a89 | -10.89829 | -55.45811 | 2025-10-02 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2411138-0d78-3f39-8a7a-415e29092a00 | -11.032 | -47.82695 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e2cc254-02ec-31fb-940c-9a7cbf37e4ec | -13.21042 | -48.49779 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7144dd8c-0a0a-3c0c-9b73-c7834444ee95 | -15.18796 | -46.40792 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ce40f7b-9328-338b-aaab-ec98fd8b7e2e | -13.75427 | -47.9508 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6d2fb6c-5c85-3020-952f-7b4c9efe79ff | -15.9999 | -50.89994 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 14b8beda-17f7-3a74-b641-42fee29e7e6d | -12.27754 | -45.37101 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1037d48d-20e9-3464-81e7-32f2080428a9 | -10.86034 | -46.58513 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33898ae3-1ba7-31f6-9fb1-42ca6653b28c | -9.94103 | -43.74942 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7993cd34-5809-32db-b6cf-3927e9257f02 | -13.31852 | -47.20424 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffb0187c-948a-34b2-985f-947f7e7d5529 | -12.70067 | -48.58421 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0bd98b18-d924-30d8-b614-78f8a90e6b68 | -12.89098 | -46.93745 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9a9cf87-cfb9-3b48-9372-ae4641866da2 | -10.95795 | -46.65938 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 65d06976-d371-3c08-98e6-bffb99eaa8e6 | -11.56825 | -47.01875 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2070499-2597-3485-8c9d-7d61d104d73e | -11.84001 | -45.01616 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6460e65-4ba7-32e8-a204-ca4f969bb7ff | -11.46115 | -44.96408 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ab66f0c-01b3-3a7b-9079-4c9656952df3 | -9.92585 | -43.64867 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81c7a1aa-5f20-36e2-9203-e346ee32384e | -15.35076 | -46.28047 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc63f2fb-b9d6-3b55-8e12-9c03b3444057 | -11.09042 | -47.84102 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| febee77c-3258-39cc-b76c-aebb807d6c4d | -11.58569 | -50.171 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 12717350-84ed-3c53-ab41-258787bbb303 | -11.06063 | -47.80654 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 587fa1b4-3a3d-3382-bc85-272d1c0b7b66 | -14.5882 | -48.33217 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 80d5c0ae-f913-3943-a8bd-c5e7e544e3b9 | -13.53648 | -47.24982 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73131187-1f1d-3bec-973c-b31136a96355 | -11.85409 | -48.02161 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fb0d020-4694-3c2e-9759-eea04ce6e9f3 | -12.86335 | -46.93428 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfe957aa-b58e-33b1-89db-4ca36796164f | -14.99208 | -46.89752 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87300293-9130-3e36-af84-1a032de794bf | -14.57755 | -48.31321 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2d9e963-6a9b-3bb9-a754-d335eefd61a8 | -13.79054 | -48.0562 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9af8dae9-2bba-3d9f-9d68-273dbf336134 | -12.26002 | -47.82699 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3672b24-aa1e-3bdc-a034-f47cbc336f32 | -11.59551 | -47.21802 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be1f69c3-955a-3903-8828-be9682f9588b | -14.02332 | -47.98806 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14d8adec-ec7a-3a16-b5e3-7f12e14696ef | -12.4603 | -54.32253 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd92cb64-ef2b-3d6d-858e-e94da07ad4ef | -12.8035 | -46.85723 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25ed8684-3db3-3f38-a0f2-76f42cc96c2e | -14.79293 | -49.26401 | 2025-10-02 04:51:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbf55ecd-f2af-3da3-a295-c19cb5262319 | -11.46641 | -45.00352 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 855224fa-1fe6-3b95-9876-1edcc1b73dce | -13.31462 | -47.82372 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3cb17835-c36c-39c2-b823-c7cb37e1a9f7 | -9.93323 | -43.72316 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cafdf991-419e-36ad-93b2-6c0efe9de7cd | -11.59101 | -47.64486 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 554e4091-a37f-3473-9274-e80ee95e58f9 | -14.3269 | -45.87794 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5228d3ed-a8ac-33f7-bc41-4219ab7e0876 | -10.26669 | -50.32784 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4bf5e65e-1c68-35b2-bafb-720a5356e82a | -15.26543 | -47.90359 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 162d7253-747d-3278-bc77-91181583f737 | -13.24698 | -47.32043 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dac9246-398a-3c16-b383-d8ac4996f5cb | -14.21662 | -46.11575 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ed66641d-4e60-39c0-ae8d-365511f89876 | -13.343 | -47.33619 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c7ea7de5-8806-30a9-a873-2be85c5a1ef6 | -14.48558 | -48.42735 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6b5d7af-564f-33ec-81fd-9fc15b2e27af | -15.79599 | -43.73243 | 2025-10-02 04:51:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b33539af-d555-3e89-9119-b875bd11f7ff | -12.89923 | -46.9104 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93fdb702-94ff-397c-8641-84607dd614fd | -10.70516 | -48.00295 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93fd4ff7-58a1-3349-8f22-1314de9aaf1b | -13.74642 | -48.7029 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73fef250-146c-3727-ba91-6ee195d5535a | -15.86236 | -48.12889 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9da21f98-2976-3ec2-be72-6b9a1c6fd80a | -10.22093 | -48.22763 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a97046d3-4a67-3c00-92b6-ce3851209843 | -14.88787 | -48.33735 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68619dbf-f91c-3c20-b225-0fc1982bd2b8 | -15.36263 | -56.97894 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05232c36-46dd-3b62-a824-a3b1c5847a52 | -11.58201 | -50.17045 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 236299ce-76c4-36bb-a6d5-b6d46e13259c | -14.8781 | -48.12746 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8ab503d-ef0e-3c04-999e-597f2b9f99ed | -11.82759 | -45.03143 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a00219c7-d1ee-3436-8f29-17fe88dac9b7 | -10.8217 | -47.97213 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e764137-862a-3186-a469-2bed6280bd09 | -13.94527 | -48.12893 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68e1e85b-21ad-3ad8-be9e-280cbee94b49 | -11.00712 | -49.58259 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4592abd-b1f3-3231-b7c9-f824e6326828 | -11.92508 | -47.88184 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a8b7f04-acae-3864-a4db-f1749449065e | -11.14518 | -47.19935 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4ea0e2d-2595-303b-8128-21e5533c24a9 | -10.64318 | -47.46017 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10a94b0e-9c20-37d2-8c11-7e4e20d34129 | -12.84331 | -46.94467 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49aa5051-f084-3528-8fa7-8896069311ba | -15.25183 | -49.301 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8370ac0f-80c2-3a26-8fe6-0405ccb9efeb | -9.937 | -43.78095 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 93d1cc15-6802-39c1-8f12-afa4c81db8cb | -13.15623 | -47.84139 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94ef7f65-c554-3cee-9032-10f619ec079d | -10.8008 | -44.23795 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 707f3f95-6cee-3bf9-bff1-7f573bfe74bd | -13.42034 | -47.80518 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ded252b2-f56f-3928-bb96-001e0fd7143d | -13.7642 | -47.98827 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cea2e8e-48a2-347a-855d-bf552d369f13 | -14.70218 | -49.61843 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 11c08aaf-95c7-37fc-ac86-3c1a749fc3c4 | -13.75914 | -47.94746 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29da8354-74d1-3971-9e28-825bb9fd7bd8 | -9.39907 | -47.56888 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6faca2a4-664e-380d-a2e2-8501a2326bfa | -15.32388 | -46.29392 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20fd9333-9680-38e2-9f63-902e62271e13 | -9.794 | -45.94548 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9906be52-bae4-3450-ad20-a9f0330417d4 | -9.94011 | -43.75658 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6c854f2-ddd0-3f68-8637-38b34af1f05a | -15.46452 | -45.88239 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 305b0ffb-4300-3ead-96b9-7a5429c8c76b | -13.24817 | -47.31133 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2701047f-919a-3d1c-a4dd-f3757685bfc7 | -12.7016 | -48.57728 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 99a0698f-9d2a-327b-8662-c2e77c6e521d | -11.06009 | -47.81041 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README115.md)
