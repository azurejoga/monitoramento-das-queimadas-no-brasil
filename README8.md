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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1c61ab1-c17b-37d1-867d-fda88c56ce96 | -14.4273 | -43.972401 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 529e0e7d-c33c-35e8-930f-cf176bbde42d | -13.6339 | -44.429699 | 2026-10-10 00:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2779cb34-35d7-315d-a65c-1f9c6442e891 | -13.4582 | -41.354599 | 2026-10-10 00:09:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1301c348-4f29-3e31-8903-213158aa8bef | -5.241 | -42.235802 | 2026-10-10 00:09:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc666a61-4852-38ad-a22b-e855c12c4ba3 | -9.9219 | -44.786301 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d325a207-cfd0-3564-89bf-c69fa947cc80 | -12.0468 | -43.427299 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a3c3a14-70aa-38aa-a0e9-94bff61c0b35 | -6.2228 | -43.854198 | 2026-10-10 00:09:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43b17638-2915-3e63-927d-708b3233b814 | -14.9659 | -41.691299 | 2026-10-10 00:09:00 | METOP-C | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0065dc30-fb72-378d-ae09-217d5dda90e8 | -6.9967 | -47.6712 | 2026-10-10 00:09:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0cd90ed-d87e-35e0-aa65-0d04b26a3212 | -7.1719 | -52.641899 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcdf69e1-f4c3-3f73-bc32-a1d3c71c86ef | -12.2471 | -44.429501 | 2026-10-10 00:09:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee161b39-86ab-3ee6-91f6-57e368021e50 | -6.0511 | -44.6521 | 2026-10-10 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9890bd1a-765d-3b41-b1bc-2cebc4a4c51d | -13.4367 | -43.6203 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea2e06e5-4b61-30b1-9a3f-ca634a7d7839 | -6.6917 | -40.461102 | 2026-10-10 00:09:00 | METOP-C | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6a8d4c53-585d-3392-b766-b6cf8977fdfe | -11.9921 | -43.458801 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 206200bb-c9c7-32ce-b762-93b2bd635378 | -18.637899 | -41.3409 | 2026-10-10 00:09:00 | METOP-C | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3e4f92d-f4f6-3b19-a530-39330a64f8f7 | -5.8342 | -44.923199 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee5b6b1f-1dab-39b9-a5b8-c42a02f18804 | -18.636101 | -41.331902 | 2026-10-10 00:09:00 | METOP-C | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 441121af-c377-33b9-a9df-822e9eebf111 | -15.0619 | -43.383301 | 2026-10-10 00:09:00 | METOP-C | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 2a08b676-6c30-3651-b9e9-ca7e5078617f | -6.9254 | -44.568802 | 2026-10-10 00:09:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5213b1cb-2bc1-3d2c-b231-2a04ad85fffd | -8.2384 | -46.4226 | 2026-10-10 00:09:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5677cdfb-c863-3810-8696-8e828443959c | -6.0308 | -46.418301 | 2026-10-10 00:09:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c94db72f-ccff-3fbb-874c-e6e555b7bb38 | -4.1491 | -43.188099 | 2026-10-10 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67231919-1f63-370a-9125-c7c4662e1a1a | -3.2121 | -49.423801 | 2026-10-10 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d51e6c0-bb2e-39ba-8d34-b28618d32d60 | -3.2023 | -49.4259 | 2026-10-10 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 798ed493-8e3f-39a5-83c5-82d9bc5379ec | -11.9688 | -43.4935 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39d0ffd0-d464-30e1-8604-bd78a2e1a2ac | -4.9328 | -45.070099 | 2026-10-10 00:09:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf4cde3e-dc7c-3f40-874a-1fcaeec6f35d | -11.9354 | -43.480801 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 018814db-be79-3ba2-9228-39a84e49bae8 | -17.101299 | -41.574501 | 2026-10-10 00:09:00 | METOP-C | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3287936f-bfa3-31a7-8bce-05b567ac4bed | -14.45 | -43.9333 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0d898fc7-382b-3600-a22b-798de3ddfbd1 | -3.73 | -50.012199 | 2026-10-10 00:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1ab30a-d9a8-312e-ac77-435de6f2c637 | -13.3727 | -43.902699 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48b6d6b5-97fb-3f3a-9517-3ad0a105ba63 | -13.363 | -43.9048 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26eb5de8-0c99-347a-a203-110c1d4a620e | -3.5586 | -51.484901 | 2026-10-10 00:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a26bc7b-da77-306a-99a5-5134cb0f0de1 | -5.3583 | -43.254799 | 2026-10-10 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 304f7c1b-e52d-3e86-a54d-89e4a1c64470 | -14.0571 | -44.810101 | 2026-10-10 00:09:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 116b2559-a0f2-3366-ab45-f34e89cbd154 | -5.4903 | -43.979698 | 2026-10-10 00:09:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7e69821-9231-357f-a272-33e307dfbfb8 | -4.1138 | -46.8685 | 2026-10-10 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87b64b6a-bf58-3824-8095-802f89f87ed9 | -16.632299 | -40.6059 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 800a9a81-0dcf-3edd-8db9-1ac6fcac66e2 | -16.9568 | -41.174 | 2026-10-10 00:09:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f9d89bc-de3e-3e25-acf2-6ca478fdb2a0 | -13.251 | -42.251801 | 2026-10-10 00:09:00 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ec96f4d1-a3c7-3486-a7b6-de2cae76cc52 | -3.6735 | -40.209099 | 2026-10-10 00:09:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 079d7a10-a67c-36df-a052-231ec21cd12a | -12.8483 | -44.1791 | 2026-10-10 00:09:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be718168-b263-327c-b2ca-0e0a74c5036e | -3.7545 | -45.950298 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6dd4317-dce6-3d97-bbc4-82e270c21eb3 | -4.0399 | -46.171001 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8c7e428-95a5-3666-bd06-ecdf3aedee05 | -17.4562 | -45.073399 | 2026-10-10 00:09:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9954e5e5-c0fc-37a3-bb35-b1737c1ab29c | -4.3115 | -41.2337 | 2026-10-10 00:09:00 | METOP-C | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b3328b7-1274-3c4d-8773-89dfcf1b4041 | -12.0527 | -43.406399 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ce371ad-326a-3d53-8c03-fcbf74b1596c | -3.3734 | -44.488499 | 2026-10-10 00:09:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2a5e71f-a4b5-34a9-b035-58dd1a59e736 | -3.7869 | -45.7747 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51a2ae61-4a6c-312b-b7ba-2bb5555017fb | -7.1221 | -41.809799 | 2026-10-10 00:09:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49dfd857-4729-3fae-8478-ad0baedd649f | -5.7435 | -43.275398 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d71af82-7a1d-3dd2-910e-c30fcca1cea3 | -7.5204 | -45.320202 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2a0e60c-e362-33fe-8980-1080c7fbdabc | -14.4379 | -43.9244 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 70f2392d-6d10-3f59-9bcd-15366dd5a5fd | -9.561 | -40.341 | 2026-10-10 00:09:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 59fe2587-41f1-3b5d-8664-ff6b47d2e7ef | -16.705099 | -41.884602 | 2026-10-10 00:09:00 | METOP-C | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7708e11a-122f-3129-8980-3addd810def2 | -5.6203 | -43.642502 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6def98b5-6621-33f9-a916-6cd7e49b4988 | -9.9227 | -44.8862 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f627d2fc-5026-3dd8-9e97-a6c1390f2c12 | -9.8435 | -48.017502 | 2026-10-10 00:09:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77c3ee6b-4f4b-36dc-8c6a-73610fbc011b | -6.065 | -44.668301 | 2026-10-10 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9036f44-e5b5-3262-b77a-aba55ebaa044 | -5.5297 | -43.056702 | 2026-10-10 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26566466-5038-360b-a4f2-e15be150f476 | -6.8735 | -45.0322 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37a3206c-36b5-3e6c-8c7b-4d4d5df39ee3 | -6.3816 | -38.938499 | 2026-10-10 00:09:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1356f243-7737-3b0e-807d-0fef86a7ae0b | 0.3813 | -50.937401 | 2026-10-10 00:09:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0626fb-e9da-36fb-b970-8911790a080b | -7.1116 | -42.5411 | 2026-10-10 00:09:00 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16b9be09-f2aa-31cb-b889-7c8d258e0ffb | -13.3749 | -43.9132 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21a01740-ce21-3d86-a80d-a58c9db6b3d9 | -13.2631 | -44.013901 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d77d533-d02b-3ea7-b129-7f7689692f8d | -4.9173 | -45.783001 | 2026-10-10 00:09:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5368a583-58de-3a93-a0cc-eaebc8da01a0 | -7.4796 | -42.8526 | 2026-10-10 00:09:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f854b8e6-95df-3c2e-a85a-abad25bba8ea | -3.2061 | -49.443001 | 2026-10-10 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5698800-820c-3f3d-8233-f868a6b902a9 | -12.8461 | -44.1684 | 2026-10-10 00:09:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9309b85b-bf3e-3450-b9ca-1e4fd61ba081 | -17.136299 | -41.348099 | 2026-10-10 00:09:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6dd8c0a9-6e9f-3039-8ea3-b74f4315c4a2 | -5.4538 | -44.782101 | 2026-10-10 00:09:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2609339-5c6a-34b5-a5fa-ac65e04c0cd0 | -13.243 | -42.262501 | 2026-10-10 00:09:00 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a897d0ab-3f16-3f66-bcf4-6698b3da37ef | -5.9212 | -44.575401 | 2026-10-10 00:09:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff1ea17-97fa-32d9-9684-38396269926c | -6.0006 | -40.955399 | 2026-10-10 00:09:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c479b109-112b-39f4-9075-da665bc06909 | -14.3257 | -44.6786 | 2026-10-10 00:09:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dff6ecfe-e7dd-3150-9ab1-deb0f13d4486 | -11.9765 | -43.481899 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce1bace4-5e18-3093-b605-6d7e21b5e4cb | -7.2311 | -44.187099 | 2026-10-10 00:09:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 966f2c9f-0d92-31dc-a722-fd45dd33de79 | -6.6101 | -44.256699 | 2026-10-10 00:09:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae519893-90c5-3eac-89cb-5dcb346bede4 | -11.5547 | -43.711899 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d038e1e4-6371-32ab-8f44-fa3acd2f340b | -6.38 | -38.931301 | 2026-10-10 00:09:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0661c946-d20b-3759-a099-01912d03fafd | -9.3058 | -47.379799 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41f11c08-ff87-33fe-a9d9-f91de3a3ac2b | -4.3813 | -41.809299 | 2026-10-10 00:09:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89e331d8-7d56-33c9-9262-f1885b2b2999 | -2.618 | -59.9747 | 2026-10-10 00:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| abfe5334-8017-3c61-a723-fb9e27c9a3f6 | -3.7945 | -45.7841 | 2026-10-10 00:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 109c85b1-e516-393b-8028-e66008aee9e6 | -7.927 | -54.7384 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| eb6d5333-cf8e-3fea-a6c5-096d120b585d | -11.6566 | -43.661 | 2026-10-10 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9834c311-46f2-3376-8ac3-855c72e86c24 | -4.4025 | -49.7774 | 2026-10-10 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 61b23f8c-7ff7-393f-bb2f-1994a4851a54 | -6.9318 | -59.2605 | 2026-10-10 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 00496373-5866-3945-8112-698c19f62b4f | -3.9009 | -58.9549 | 2026-10-10 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a250f33a-41b5-3307-a225-2cc741cd2ea4 | -13.3865 | -43.8708 | 2026-10-10 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e5ccd437-c02d-3b53-ae19-8d4ec2d31d47 | -6.9319 | -59.2412 | 2026-10-10 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 2d2d5186-3e39-3bdf-be12-5794e532229f | -12.3066 | -63.3701 | 2026-10-10 00:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 4603ad26-cafc-3f66-813e-2c4f77848ed8 | -2.618 | -59.9938 | 2026-10-10 00:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f4fbfd8d-d050-3bd7-a433-cb6aff5795f7 | -14.4731 | -43.9322 | 2026-10-10 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 151.6 |
| b62294e3-3a94-3b1c-838f-0447bb492743 | -6.4903 | -62.8554 | 2026-10-10 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 1ce24d6c-2158-3cbd-b495-8ae8a883323d | -9.2787 | -47.389 | 2026-10-10 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1452dbaa-5c7c-3189-ad15-5ecf521d4c09 | -7.0225 | -47.6829 | 2026-10-10 00:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9dcce28f-21d9-3439-94b1-05db9023025a | -5.2303 | -50.6856 | 2026-10-10 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |


[Clique aqui para ver as próximas entradas](README9.md)
