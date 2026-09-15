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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5889b4ca-cc0b-3b74-90d0-8b142a7e1279 | -7.21721 | -46.14098 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74fd8f5a-b095-31ba-aaaa-309bee001ed1 | -8.0985 | -43.77734 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f4333e6e-21cb-3e99-b59e-f512aae79571 | -6.95539 | -44.54438 | 2026-09-15 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f5cbc84-1d19-3ad3-9652-84ea342a24a3 | -7.29193 | -46.74768 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eae948d4-659d-31c6-b107-32e48f1868d6 | -9.45715 | -48.90767 | 2026-09-15 04:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3b134b1-6cd8-3b94-8302-83627b307941 | -7.07931 | -42.11214 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 156ec004-95e7-3e07-98bb-f3637acce1d8 | -6.26005 | -41.97487 | 2026-09-15 04:14:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49f14e86-7a8a-31da-ba5f-793a65c8b5f2 | -7.17264 | -43.5908 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc46dd46-89f3-3dba-8ed9-9396931abfe8 | -8.10661 | -45.62656 | 2026-09-15 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17e0e63d-b3e4-3eb9-a806-16f68937b4f1 | -9.67949 | -47.89426 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a835d2df-0d65-37ec-91ac-7e50dba6e3c3 | -12.7289 | -40.27823 | 2026-09-15 04:14:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a411f08-838d-389b-8c38-7f73ed1a84c9 | -10.43652 | -42.74065 | 2026-09-15 04:14:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 14b5f2f8-787d-3f00-97df-d32e56dc3e8f | -6.61207 | -44.20592 | 2026-09-15 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06b6b801-5056-334d-92e6-ea18066adcd9 | -13.31117 | -43.7158 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96f82d68-3b8d-3a30-833f-68d02f1f52e9 | -8.08528 | -50.97226 | 2026-09-15 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25bb277e-2077-315d-b2aa-b6aaf0d39e58 | -7.19778 | -45.9226 | 2026-09-15 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa5d358b-88ce-3de1-9bdc-adb215abf268 | -7.08806 | -42.10197 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc94ba5f-50ef-3576-bf4f-568bf2a74f2e | -6.85921 | -38.22418 | 2026-09-15 04:14:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 043430bd-1c91-3450-8113-18da2c1b250f | -9.88127 | -47.79865 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc3b7399-94a2-369b-918f-7141d6dbe3f5 | -7.07869 | -42.11591 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dd20ba7a-33e7-38ce-8af0-fd63cc54917e | -9.36512 | -50.10264 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39b8369f-035c-3f85-9057-c1fca977cf71 | -9.3544 | -50.13631 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61e1736d-0ca7-3c5f-a32e-58520f278d18 | -7.08375 | -41.83001 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4c370a67-dbda-38f0-ac3c-d6cd471880fe | -7.17709 | -43.60938 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa804877-4847-3c3a-b94c-6dc3e58ebc2a | -7.24682 | -46.17554 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7e11e8f5-ce80-307a-8269-507e0cc520b5 | -11.26664 | -54.13046 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eba5a5ff-dade-37d7-8429-79a752e32a07 | -8.80127 | -50.48964 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dff447cf-3a6d-37c3-b099-84444bea19ae | -9.35685 | -50.08657 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae5576d3-4690-371f-9ef5-d7957be91698 | -7.2289 | -46.17647 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c0d2fa0-b272-30d5-a633-7b89336ccbe3 | -9.3578 | -50.11203 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 16e89a76-6d86-3d8d-8a7c-caa0e2e3dd85 | -7.16971 | -43.6082 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6da4fa38-2bd4-301d-9647-412c96fe3332 | -10.03458 | -52.10233 | 2026-09-15 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b420e14-b22f-33ba-85e9-87618dfeb103 | -8.80686 | -50.49079 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5c94d1c-709d-33e6-b4a0-303a5a6efa41 | -9.35927 | -50.16996 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b05c2adc-e94b-3ebb-9e56-bf33a8127027 | -7.01889 | -44.6174 | 2026-09-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77289d59-7300-3f60-9af1-e4f559d93b11 | -7.56647 | -46.31207 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43d87277-0e86-3c76-97cf-119882d67f6b | -8.09336 | -43.77914 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8eae314b-d427-371e-80e3-826cabdd1885 | -11.19074 | -42.82495 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3dc0d53e-eda7-3104-9a4e-ddcf71be8da7 | -8.58297 | -44.49213 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5eca4a5-bf8f-3258-adc1-5df9fffad6ef | -6.61487 | -44.20421 | 2026-09-15 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db92e1ef-5c18-33cf-ad61-3a65b544de07 | -5.92053 | -47.38237 | 2026-09-15 04:14:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ddb22b7-7daf-3713-b6da-0b94ca1b4987 | -8.503 | -50.14995 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abe844ae-857f-3481-abbd-828bb24403ee | -7.1698 | -43.52572 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 102a14e6-62f7-3c33-8065-0b78573578ef | -9.87545 | -47.77787 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1963ac65-9622-3228-aeaa-1febd097ddff | -13.31014 | -43.99781 | 2026-09-15 04:14:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 086479d9-80cb-3fe3-b7b9-9e7393c0a6b2 | -9.35727 | -50.18051 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba069452-42bc-31c9-a7bc-c2634ef8b2fc | -13.55876 | -43.53294 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa3752f-7331-3f2a-8476-61ad43b3eb9a | -7.24028 | -46.16174 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38302f46-f2b9-3285-a3b2-56fcbaf049d2 | -6.80486 | -43.17777 | 2026-09-15 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd374a92-21ab-3e65-8d02-e0fee9dec661 | -7.09919 | -41.82119 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4ec4653c-45e8-39ea-9659-4864c854de70 | -7.21292 | -46.14017 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19287c3e-3138-3cf0-ba89-e04b45d27ab8 | -8.5945 | -44.46998 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b7ed5f6-30cf-31fc-af70-0a86c57e402f | -7.09654 | -45.04207 | 2026-09-15 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 527eb667-8e47-38fc-8dd0-50aeed565fee | -9.88819 | -47.77847 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 893830fa-573e-3826-b6ca-cc3ae29dfe4d | -9.67622 | -47.14617 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 236bc063-9b82-3684-9986-b92c971109f9 | -9.3587 | -50.20271 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48403117-9518-38ed-b36e-ada5b5e3be1a | -10.98813 | -48.34174 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c74f6f6-95ab-34cb-b9bd-a3beb8aa2ff1 | -10.67201 | -54.14886 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1af2ce19-7581-3aaf-8f34-53316bbe6e96 | -6.94968 | -42.56723 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 389679f5-5b04-37dc-ad45-b579e884406c | -10.86068 | -46.30614 | 2026-09-15 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7cd20766-434b-3e4a-8ee4-ebe6bf685ebe | -11.12812 | -40.48375 | 2026-09-15 04:14:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1dcb892b-5c3e-35c1-958b-97ad51a0de9f | -9.45604 | -40.38935 | 2026-09-15 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 534825c2-7336-381e-bc87-08c116dcd3e3 | -10.89833 | -51.54765 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3ffe5e0-b5fc-374f-96c9-309c1952e911 | -7.29568 | -42.35221 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 144c1bcb-c7c7-387f-a6c4-8e5cacb1b0af | -8.59134 | -44.48879 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95e65069-9a8c-36dd-9b8b-189a2a6ce4b7 | -10.69782 | -47.50669 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f251723-18b4-3f58-b010-ea1df8ee53bd | -9.87921 | -47.8014 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ac64811-ece4-3ce6-83d7-1587f28724f3 | -7.16324 | -42.11818 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b03b0cf8-f014-3356-8a82-08bb5fcaa1e6 | -9.42184 | -50.10595 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 47e4353d-e2d8-31c9-8aa3-5222ad6720aa | -7.11402 | -42.09464 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11a58360-21d3-3ffe-a7c7-9d30131b7827 | -7.16683 | -43.52083 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2aa5c420-b334-39c9-8212-186913cf7f83 | -9.16094 | -49.99192 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be431e84-37c4-3759-96ac-ce19cbb173d8 | -11.80173 | -46.59098 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 835e87f7-0bdd-3b0b-9256-48c24708934a | -12.8548 | -44.38744 | 2026-09-15 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 84421a91-bcb8-3999-a68b-07e76c01d72b | -7.09828 | -47.48402 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| eb370aab-619f-379a-afe7-bbf83d6dd92c | -9.42854 | -50.10003 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36914e38-1038-3d81-b8b4-654807411457 | -11.14559 | -42.1183 | 2026-09-15 04:14:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4b9b82fe-5b7c-3a8b-b7cd-3dd3cb140931 | -9.35844 | -50.10854 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 80eb753e-67fd-331b-9ac3-da4373a84eb3 | -9.35397 | -50.13303 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce31a37d-8243-3067-abbb-897b02b0d5f8 | -5.29091 | -49.09145 | 2026-09-15 04:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85a0afef-7e55-33e3-8175-46f54cee18e3 | -10.70604 | -47.50172 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 369dd25d-9f9c-3cee-983a-e76bef63d37b | -7.46346 | -46.14555 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 012c1e33-8571-385f-9d60-98c2c8b9261e | -8.61043 | -44.46795 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e657a11e-3179-3d0c-b9ea-1ca3748a4ada | -7.5622 | -44.91697 | 2026-09-15 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08321214-f585-34a2-ba74-81ec8bbe3ecb | -7.19958 | -45.92043 | 2026-09-15 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63166258-8b22-340c-a245-21051963a512 | -7.25181 | -46.17225 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e81e232-1772-33ff-89c4-d3a060336c24 | -7.54589 | -44.89305 | 2026-09-15 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee2f4b3e-b0f8-3fb6-a876-78f617215da8 | -12.47486 | -41.40686 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c7d3ade-695f-3d21-97e2-2a34db045dc4 | -10.98641 | -48.32503 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52fe3176-58cf-3da8-9f60-ad0fd599ff33 | -9.45492 | -48.55996 | 2026-09-15 04:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04a6a9b8-3791-356d-9384-a554b897a79c | -11.88321 | -43.82244 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 867fd4f3-32b7-3d50-a1fe-c15ab22d6a08 | -9.36003 | -50.19566 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf580376-a4ce-3db4-a370-0b0bb66003c1 | -11.24913 | -43.44751 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1216f3cf-03a4-327c-9120-bf11f59b85c9 | -10.50004 | -53.57063 | 2026-09-15 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9821b8df-462c-39e9-89b8-8c5ed8b0861e | -7.47134 | -46.15117 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f74da4a0-9f3c-3500-a243-d55af6e99c1b | -10.675 | -54.16888 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3038f21-5341-3255-b233-843bab8ec2bf | -9.88446 | -47.77294 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0f79517-b045-3841-98c9-a508dd139587 | -8.49074 | -44.58542 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc59aef7-cd87-34b0-b332-ab59ebd3c404 | -8.64674 | -48.59635 | 2026-09-15 04:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9608b59-2f51-30fe-ba9b-db25b11c0d93 | -8.79567 | -50.48854 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README28.md)
