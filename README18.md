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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e98300d-73d6-34e8-8275-188d9c4dc18b | -8.53397 | -54.85296 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdd5bd32-554d-3c84-bc8c-b8a6de171046 | -11.01053 | -41.05162 | 2026-08-23 04:10:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 629e34aa-0315-3637-99b3-52cc314c59e9 | -13.6381 | -47.76899 | 2026-08-23 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dc4a1ad-2fc2-30be-b93b-66dbc7e4afd0 | -12.07208 | -50.60028 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 286db512-e3ba-3e03-9556-1cc9cb982949 | -14.15212 | -48.06511 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 071c50c9-d3a1-359f-a151-5b647d528eb5 | -14.14827 | -48.06419 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6dd1771-b28e-3f55-8576-1f3e290f506c | -12.73562 | -48.39048 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1003dab7-6e62-3eda-b2be-21ab388206b3 | -10.05152 | -46.42482 | 2026-08-23 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d73353d-e1cc-3ac5-905d-9606698e1f56 | -12.2174 | -43.16635 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 45f8375c-6ad2-3eb2-9f0b-c280f141fc1d | -11.27536 | -50.73918 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe55ebff-d66d-34d5-95e0-978ad9712287 | -10.30823 | -48.21315 | 2026-08-23 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8c4b4d8-e0ba-3559-b638-f69946245585 | -10.84053 | -50.98917 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 283a1704-c474-3499-a68b-0f0384381d41 | -15.31716 | -53.7966 | 2026-08-23 04:10:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc87677a-ccac-3c5e-9139-90956315310a | -12.74905 | -48.38559 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8adc8fb7-c008-3215-a65f-bfc83bd96289 | -11.61627 | -50.554 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| bea5a91b-3346-3021-a733-9d34b6aad41f | -12.28163 | -43.14828 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21ff79b7-7a66-3c32-ba20-8db9028e7818 | -13.52909 | -40.64285 | 2026-08-23 04:10:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d95195fb-d6bf-3e78-8ec9-acc3d888905b | -12.72979 | -48.39978 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 350555cd-514a-3a78-8d58-b9a68ce64ef8 | -11.84796 | -51.67305 | 2026-08-23 04:10:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 835cc06f-8d3b-3e7b-b4d6-e1a2a192e8c4 | -12.24523 | -43.18568 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19dd7945-c4ef-33e0-b445-fdc065d8a53a | -17.7161 | -43.4988 | 2026-08-23 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38b310a7-5040-3281-b62b-92a03f777613 | -15.04456 | -48.69721 | 2026-08-23 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ed9a932-939a-3280-a519-30a71340e20e | -11.58586 | -46.94116 | 2026-08-23 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70ed7467-fa96-3a72-99dd-f874244412e0 | -8.53912 | -54.84952 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a312cee-fbc9-3595-b87f-6372d5405476 | -11.93951 | -45.51525 | 2026-08-23 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbe36065-b158-33a7-b5bd-7a6d223cf8a9 | -17.92539 | -44.38801 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4920f083-1c0c-3801-be0c-00a3d29637b2 | -10.84552 | -50.9901 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57d3722a-cd60-3760-9bcc-9eb74e8d087d | -10.70975 | -47.73761 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b6b560e-9b3e-381d-a677-f3bc3fcd7674 | -13.2544 | -51.59639 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 805af21a-ef03-35e1-947d-cf64f8b67987 | -16.05385 | -50.44144 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4e915d46-2897-34d8-8d33-3863ae276c16 | -14.575 | -53.02465 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bd21e7b-7bc9-3606-93f5-72f8067f68f6 | -10.71378 | -47.74323 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f854b55e-5baa-39ce-adfa-0b218f1eacc1 | -17.35676 | -42.65808 | 2026-08-23 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70523025-232d-300f-9006-da2e96ccaf03 | -14.5616 | -53.03627 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03f4043c-f3f0-3647-8c56-617245502b3e | -16.11629 | -43.62808 | 2026-08-23 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9463c5da-1dd2-3ef7-b5c8-b1ef70d7d1dd | -13.18967 | -51.44405 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 476fa15c-5bf3-35f5-a91a-99fa5ebd058b | -17.60212 | -44.62643 | 2026-08-23 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c1f2db5-c4f8-3872-9370-465b130abdd1 | -14.13836 | -48.04965 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70c81844-3491-3ef9-ae69-25d1b38292d4 | -15.9422 | -44.04639 | 2026-08-23 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| feefaafe-10de-32ff-a595-fa4a86132538 | -12.73797 | -48.40096 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 28c37144-1d85-370e-bd07-46134bb8078c | -10.79782 | -50.96924 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5708161b-4687-3d2e-b278-9e351e94e762 | -13.20012 | -51.42393 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7fdd122f-5341-3c17-9245-2f7c1663129d | -12.65179 | -47.64421 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ac52fc3-130a-3cda-a8cf-4fa9f8a179e9 | -13.45126 | -43.84064 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f963c7e2-c73d-321e-978a-3a980726a9a3 | -12.26674 | -43.17834 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d62eb6f-5525-35b1-b4e3-b59da7d29b01 | -12.26655 | -45.0802 | 2026-08-23 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b76d4baa-7bf1-3ac1-b781-b4fe1c3d944b | -9.43188 | -51.66979 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2704a574-fff3-32bb-b993-3398987b852d | -10.68754 | -45.04951 | 2026-08-23 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b908c49-cdb4-344d-bafe-c58fd87f1498 | -12.74326 | -48.39473 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 78f846b2-ca71-37cf-92c3-becf480f0832 | -11.60289 | -46.77135 | 2026-08-23 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61a40142-4854-3c65-9d5d-739ffd1c02a4 | -13.16118 | -51.43259 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f6fede21-ecdc-3865-8061-f5a10740b270 | -14.14229 | -48.05264 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd579e3e-a79f-35b0-b642-f70c26c698c9 | -14.31154 | -53.22894 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d692cc58-1af6-3d51-984c-79e05ae8d240 | -14.95437 | -52.64719 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 89298c1a-2ab6-31b3-8652-c0f5397b2ce6 | -12.75374 | -48.38272 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b76753ce-f80d-35cf-b3cb-af294394c3f5 | -13.18426 | -51.42673 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d284d3cb-0d18-3ec9-9e06-8da4dd91053e | -16.01449 | -51.4002 | 2026-08-23 04:10:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b5bebe-d5ba-3774-b703-2457966873e2 | -17.36069 | -42.65489 | 2026-08-23 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfb6cde8-eb6d-3a1f-8645-ed78c5617af0 | -12.22402 | -43.14576 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cd6b7044-9034-34fc-8980-3bf1fb0e9336 | -12.75722 | -48.38681 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14ca2ba9-6160-39dd-a151-76653dd132c1 | -16.40423 | -51.84588 | 2026-08-23 04:10:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c33c9aec-b6ae-3935-a394-fbb78f8d04b3 | -13.19902 | -51.42959 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b914bb22-6729-31f3-837e-6b9836851bd4 | -13.88505 | -54.0027 | 2026-08-23 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8418ffbb-f740-37bd-98d6-5fd2d9e3e5df | -10.84643 | -44.74208 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a855f334-ecf2-30bf-b905-2919c4d8a0aa | -13.21051 | -51.44947 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c78834d4-04f4-3e89-bc6d-a2f663e7ab77 | -8.53267 | -54.81277 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fbae1acf-499a-354c-a6e4-39d3af8c0cce | -17.91924 | -44.40551 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec67e0e3-c238-35c9-b0e2-ba8380e77120 | -17.36176 | -42.62428 | 2026-08-23 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 830b567b-a262-3bd4-8430-b499521e3f2b | -16.04951 | -50.4404 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 24f4dfbf-b7c9-3011-9f0b-ac80dc55b521 | -17.35731 | -42.65434 | 2026-08-23 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f82c1a4-98fc-311e-a287-f2b0575cdd1c | -13.24998 | -51.59249 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cbff0db-5619-3304-bcb7-3898b5da1be6 | -9.52799 | -51.64584 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b5e7353-6018-3974-878a-db2536a45dec | -10.84926 | -44.74643 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27d5d5bd-029f-309c-ba8d-f3cfff34a9b1 | -13.88942 | -54.0061 | 2026-08-23 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40d4b8a8-18af-3941-9188-ed3cea07130f | -13.34776 | -44.14956 | 2026-08-23 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21ffa932-3ede-30d2-9085-c0415f522547 | -14.35381 | -51.77576 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7cf706d-403a-309b-9008-ecfc5faae1ca | -11.9382 | -45.52322 | 2026-08-23 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c245cc7-5cc3-3a1e-9cbd-251d61062239 | -14.30546 | -53.23114 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70518266-fa65-3bcb-8b33-db1def8926eb | -8.53943 | -54.82418 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aad52512-9fb2-322a-899e-1b7b9863bb79 | -16.05906 | -50.43785 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 652739b0-8f57-30df-9cdf-6f096a057caf | -17.07146 | -39.42431 | 2026-08-23 04:10:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a1174166-86bd-3cd7-8b44-e41c9f94c989 | -17.60543 | -44.627 | 2026-08-23 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 799b0450-ace7-3732-89dc-066a2c941912 | -11.44142 | -44.53869 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5c17aa-2e7e-3424-909c-b8d390b73d11 | -17.93151 | -44.50041 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 502f0912-a7d2-3e07-91dc-507dbfff1f4c | -12.27336 | -43.13614 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0ebe318-d1c0-3681-8a4d-cd0aeed9cc72 | -8.52625 | -54.82162 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| acdacf98-366f-35a9-b71b-f31ce16fb13c | -12.75819 | -48.40529 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d75d66c-e351-3b08-9fe2-3752d4798508 | -11.44202 | -44.53498 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67cae45b-e09c-3db4-8a74-ed974de29433 | -16.84322 | -46.34821 | 2026-08-23 04:10:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c98a90c-e310-373e-b17a-977ec6ecfe97 | -14.35874 | -51.77673 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd0aa385-ddb1-330c-a402-1212edc92be0 | -14.79853 | -48.783 | 2026-08-23 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38ab4b38-aad1-3aae-89a3-374c03528b6c | -12.26785 | -43.14965 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da8ee470-ed9a-3358-a3cd-d6e98f653dad | -14.95757 | -52.65811 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7736e755-f408-3a43-8231-8240d6434511 | -17.9287 | -44.38857 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1009749-7c7f-3ec7-8006-d7f679df854c | -12.24854 | -43.18622 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a8c23d8-d2cf-31e3-bdd8-c3844e1d6461 | -12.40517 | -42.90162 | 2026-08-23 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f6be2f73-b7f9-3078-b044-6963c7e5b89d | -13.66635 | -51.85288 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b982712-04e9-3dfb-979c-9264382dbc6b | -10.82987 | -50.9632 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e846f00-7d76-3cf8-a48c-b01d58f46c0d | -13.15733 | -51.42594 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 7102d05d-c3b0-348e-a365-b0904de5d0bb | -13.15625 | -51.43163 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |


[Clique aqui para ver as próximas entradas](README19.md)
