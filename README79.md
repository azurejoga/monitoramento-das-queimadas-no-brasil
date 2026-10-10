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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d878e2-8154-31e4-bad2-4b4ac37733fd | -6.9918 | -47.70307 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4adfaf60-5f3f-3d65-b4e2-6805eb878961 | -8.17752 | -54.71032 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cafdfe4f-5427-3c61-a406-05b151d6eebf | -13.5217 | -47.42333 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce787e7b-38f9-3875-8a98-f6407b38f955 | -14.05791 | -43.83105 | 2026-10-10 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6841257e-31a7-3b73-b1a2-b207830912f6 | -12.03524 | -43.37907 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd41bc04-e168-34f9-be29-a1ef06bbe18b | -6.53387 | -54.91874 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 690b780b-2762-3954-8f21-e3c0b4806a15 | -7.47102 | -55.70211 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dc0b8dd-6eeb-3a65-9277-cc18fa6aebf0 | -9.94115 | -44.87937 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23bf8d5c-f357-3f08-af4d-a43d18ad1e07 | -14.24779 | -47.30249 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8321cbd0-f584-3ee7-9b75-36c0b81a586f | -11.59803 | -43.74791 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07f1d37f-3f18-3079-b176-5f461a023535 | -11.313 | -46.64744 | 2026-10-10 04:46:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8cbb4b51-dfa7-3510-a557-426bcacda3d8 | -6.42699 | -55.2604 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ece49c6-989a-35d1-9f9d-8e45ff30fe2e | -11.33443 | -47.80276 | 2026-10-10 04:46:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0cbb8c0-3cae-3aea-855c-57d0e533c0c2 | -7.00624 | -47.71962 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92f0d3e7-21f3-3b5c-9f7e-4c387cac79f3 | -11.60205 | -43.71914 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c80f093-5d08-340a-8186-bff23bc27327 | -12.73072 | -47.0098 | 2026-10-10 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 499e9a2f-5cae-3b2e-bb51-62fd62e9e661 | -13.10583 | -46.35261 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 661ca481-d858-3566-a604-a135d307269b | -6.43535 | -55.04347 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d9884d6-5296-34a2-9271-c079da8017a7 | -8.2413 | -46.42818 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a6ecf13-aeba-319a-acec-065b65c94b2f | -11.66769 | -46.78186 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8248d1a2-bf52-367f-84b6-45a238a7f595 | -7.08826 | -55.7383 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7d640ed-9a35-341b-8fae-7fb613bb2996 | -6.47107 | -55.5137 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db2897cf-3425-3b20-8a92-4282d2b0577c | -6.12663 | -55.69376 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3effeda2-8bc0-318f-a3f2-cf31997491cd | -15.37123 | -41.9266 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cea68f6-b6d3-3b45-a83d-594501d6096d | -6.70583 | -58.7159 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ba6146d-3608-3c7d-a167-36303e03b301 | -6.43971 | -55.21513 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18c50fce-011a-34c7-8ac7-fbb88d619213 | -8.95522 | -47.3757 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f12c3ab-089c-320c-97f7-8e2b790208fc | -6.48346 | -55.96745 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e0eb4ef-f7fa-370a-9d31-8480f7a1b4fc | -11.37453 | -54.02657 | 2026-10-10 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8464744f-f377-35e4-a9de-334e82b11a6e | -14.4426 | -47.05814 | 2026-10-10 04:46:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18f58179-c876-355d-8305-95621dabdb7b | -7.23052 | -55.14601 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2071e67d-8de3-340f-86eb-b46c23203b5f | -11.76604 | -43.5235 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c8aad2f-3d81-3c78-8e71-fa68f5bc4351 | -6.46656 | -55.05917 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04a0dcb8-7a00-35ed-80b3-9a22baa5cbc4 | -6.2454 | -52.8636 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e3ac32d-6499-3d4a-9048-b826def2e1da | -14.46283 | -43.94466 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d403894a-d7d8-31ea-9c79-fc27c39c3620 | -6.43921 | -55.04917 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9632ee40-914a-369d-a8ee-8c69e8d5217e | -11.12335 | -45.95312 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36f879cd-f3c4-30cb-93d9-a6d207519f3c | -7.90549 | -54.71534 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e41c04dc-3703-3de7-85d0-41ad107e8ad0 | -11.5699 | -43.71009 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23203ad9-e371-3810-9243-7d1b102590ee | -5.96321 | -55.33703 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ce31669-dfaf-348f-8344-b8f03c00a42d | -6.94348 | -59.10954 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa7c212e-bfcd-3817-b67a-bef8dfef9cfe | -14.45967 | -43.9362 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91e449ef-7c39-355b-a73b-5fc85ae0fea7 | -11.83112 | -43.5242 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c73da68-39cb-331b-9777-8c3d3a17c46c | -5.96561 | -55.38079 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6a94c6b-1b17-36c2-9e78-c160b283bda4 | -11.96117 | -43.4804 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1670d953-4083-385a-9693-8e9f8e527912 | -7.9039 | -54.72441 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0f52be2-1cb4-3759-81e8-f16466a386ec | -11.90142 | -46.56527 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55df6d82-df23-3512-842c-54d0db2882ff | -6.53676 | -54.91656 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29411557-efc6-3e94-9d0c-b0ad7381fa54 | -11.97687 | -43.45942 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30eaaa7d-7098-34c5-af1b-fcc385b8ab60 | -11.59691 | -43.7261 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b942cd8b-0e2e-3bad-8f2f-b85c56aab580 | -5.18526 | -60.31295 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e15848fa-8741-399a-96e9-d0a289707565 | -7.82415 | -44.1775 | 2026-10-10 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d009b61e-4de7-39a5-93b4-8e35faa9b0e0 | -12.58449 | -44.13902 | 2026-10-10 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30117a87-1b9c-3f18-9864-215baab25f89 | -5.98463 | -55.35732 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 206dbc65-955f-3694-b594-210603a8e3a3 | -11.19955 | -45.29536 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba28cca7-0307-3635-b191-64c2ad055921 | -12.77512 | -44.88551 | 2026-10-10 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64bc00ab-7d26-3b77-ad2b-2e7ed2809b05 | -13.52633 | -47.41597 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 256c29fc-c2b3-38a3-af6e-490d185fa173 | -5.86912 | -55.70251 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 869dad9b-07c9-37a3-a760-706723cfedbd | -6.4426 | -52.70451 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6af35424-c4c8-3cc5-987d-99791e62dce6 | -11.02218 | -47.56939 | 2026-10-10 04:46:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 428a26f2-2535-3e14-a3e9-ccebb7ef0a05 | -9.95496 | -55.10797 | 2026-10-10 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6866ef38-f584-3343-844a-78e2a7482708 | -13.69289 | -49.08144 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d46d94c2-9855-39fb-bf63-889ccbdc394f | -13.50719 | -48.61148 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0b068a4-ab79-395e-9a26-bd95c8ab3378 | -8.1857 | -54.7163 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b15a4197-9530-30d7-8fba-c8e780311fff | -11.92832 | -46.76817 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2668a7c-5dd4-3862-be68-00d4a759a7fd | -13.80798 | -42.65754 | 2026-10-10 04:46:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f01160ba-3e32-3b20-9179-28414c035fca | -8.17677 | -54.71471 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a58a96a9-9cbf-3510-bf81-2de226462f2b | -6.13458 | -53.10193 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b9c3700-354e-35f2-a919-938f35f6d90f | -9.28687 | -47.39474 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52e3c699-4cf7-3a7b-97c9-8302962b0e10 | -11.67116 | -46.78238 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c32f637-d437-3fd3-97ab-28b206df092f | -11.76135 | -43.52668 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db642d80-bcb1-3709-9ec6-2fa18d37726a | -6.36185 | -55.15715 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31b1e84d-0e6d-3774-845f-705c476bdf3d | -6.70902 | -58.71192 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11daa0f5-f424-3f81-ab54-bddccc56d1d3 | -13.7684 | -48.11996 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f00f583d-1028-3d86-bc07-ad5edeb59bb0 | -11.29036 | -45.20226 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4277abf2-b788-31af-b756-3f76d61260b6 | -14.9736 | -41.69344 | 2026-10-10 04:46:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 762e98ff-041b-3095-ac99-b42ff25bdd84 | -11.38325 | -55.16256 | 2026-10-10 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8633e05b-a852-399c-ba2e-6b6d42558b9b | -11.84366 | -46.8039 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d962e774-e707-3de1-b6ce-582d553dd31b | -11.03237 | -45.44098 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e97ad771-d9dd-3181-8d85-4cf75b5066fe | -13.39015 | -43.88708 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ca2de00-6ea2-39bf-b8dc-da57b08ae9f4 | -7.00181 | -47.72605 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0192928-f8bf-34ff-b8a7-578b0e341e55 | -12.02493 | -43.48174 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ace6479a-98ed-3cb6-91a5-585a82faa3ce | -9.75584 | -53.87847 | 2026-10-10 04:46:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d7e59a7-894e-3929-9609-6e976ba5d79c | -6.45228 | -55.28292 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c752b647-4ab1-3613-8e9e-c27b394f46d2 | -6.92961 | -59.25566 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e805db5-eadd-385e-a56d-67711a715afc | -11.7776 | -45.50547 | 2026-10-10 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1550958-f055-3ad7-b6a0-517d718d652a | -7.78149 | -42.31242 | 2026-10-10 04:46:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7fbcd62e-c337-3a83-84d1-30f3cd5db72a | -6.48119 | -53.60596 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fce3b5ad-05a8-3ec4-9d44-346682fce2f5 | -12.37575 | -46.56756 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3d8c198-1d3e-304a-b9c7-c8311ad2d88a | -6.45715 | -55.05752 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee0b8134-734d-38ff-b7c1-556150350fd3 | -13.25901 | -44.00422 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2399d030-27fd-3730-8bd3-b853b1540347 | -9.21141 | -45.6529 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 613897b6-4ca1-3006-8b52-325705421ce7 | -12.99812 | -43.33905 | 2026-10-10 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e0ae82c-8044-395f-9244-5efbcadceef5 | -14.01389 | -48.76268 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f2a2fab-fdc9-36fe-935f-e9fc1c2b40c9 | -12.35927 | -46.58142 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b217d64-a6f5-3b9c-b562-1c5189d50caf | -11.77331 | -45.50901 | 2026-10-10 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4a4404b-984c-3d19-9e55-b55a02733449 | -8.50436 | -54.61023 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a5baf132-5d52-301d-9add-28901100fb04 | -13.74295 | -40.83757 | 2026-10-10 04:46:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3a9175e8-4c38-31a0-9aa5-2fe39dc21e68 | -7.17795 | -52.61382 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77731bc5-bcaa-3f69-8e22-cdbca61eac2e | -7.2297 | -55.15075 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README80.md)
