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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc655ae6-098e-33f7-8cf4-04b5fd121572 | -7.17778 | -43.61549 | 2026-09-11 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37fcdff5-fdfb-3b87-b2a1-e086dab0d33f | -10.97326 | -47.88009 | 2026-09-11 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a8cb2dd-e331-3c36-b1b1-641d0566f466 | -9.90247 | -45.90163 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bf6c089-5140-3e6b-b014-857ddbecda12 | -10.60618 | -45.22619 | 2026-09-11 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12b596cc-8724-3d90-a6c6-f6523fd8f7e9 | -8.73091 | -50.59747 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a257fd66-efb4-3f0c-bd8e-0a53c510bdba | -8.73024 | -50.60117 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ecf22b8-b567-353b-ac31-9bca873730ab | -9.78328 | -43.4495 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99a06869-4ba6-3f96-998f-1de44d798f9f | -8.62248 | -47.40597 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e12273c-2e1f-3af4-96f1-e81c4d01a417 | -9.32536 | -45.64576 | 2026-09-11 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ab6e882-efa5-39f0-ade7-f1ab6ce9e512 | -7.35252 | -44.19257 | 2026-09-11 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f83dab25-4ddf-3471-912f-31c4dd24124d | -6.1228 | -42.56588 | 2026-09-11 04:08:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4402a97a-c056-3c64-aa09-424eb9f0e707 | -10.7703 | -45.93214 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78f8aeda-eb6c-31c5-9eb2-26c2366a8d3f | -9.17659 | -49.94973 | 2026-09-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07846481-1056-393a-a60c-ec71966d2c65 | -8.3851 | -46.30082 | 2026-09-11 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f2af695-90f1-32fa-92c3-78a5c87ae0ac | -9.53476 | -45.45961 | 2026-09-11 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 30f8d0ab-fb21-3ceb-bf2d-6d70e6b887e5 | -8.50646 | -50.15237 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 109f19fb-9c99-344d-9830-0843b7b94e32 | -9.15552 | -49.98255 | 2026-09-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d638730-1fd8-348d-94dd-4c0134d2615c | -6.78793 | -48.66676 | 2026-09-11 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 548baec9-4e93-3bb3-b671-f5b07e675dae | -8.8361 | -62.489 | 2026-09-11 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 49cc7cae-9ab4-3bfa-8aa4-26a9be804319 | -9.1799 | -68.2194 | 2026-09-11 04:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 26fcc4f8-ad6e-3575-8b87-7246b21c7f0a | -13.34264 | -43.74839 | 2026-09-11 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ca79a6c-e4f5-3aee-9ca0-2d75f9ecb051 | -14.58652 | -48.86012 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63f67ea2-d856-322c-ad4d-80691935fbec | -13.86085 | -43.62975 | 2026-09-11 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df446743-7e26-379b-8511-efc3453c6d50 | -14.06769 | -45.63328 | 2026-09-11 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3522b81b-2217-3857-9a56-bf25198a59f4 | -13.77034 | -43.64584 | 2026-09-11 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c270aa8-740f-3849-8678-0acc44cfd8e1 | -14.90103 | -44.67882 | 2026-09-11 04:10:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a121ed1-0d09-3165-b1bc-e6563f88c9b3 | -17.93276 | -42.67591 | 2026-09-11 04:10:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5422d502-eced-34aa-bb2b-814859ceb07f | -14.89445 | -41.70159 | 2026-09-11 04:10:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ff656397-6915-3620-87eb-58393132081a | -14.61678 | -48.84729 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2822b517-a1be-3150-8ca8-483d1acc5e44 | -14.85592 | -48.15715 | 2026-09-11 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f502ca4-e289-3e5c-8b9e-ad32ad9a8e9a | -13.48395 | -48.55791 | 2026-09-11 04:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3015e9a1-8ef2-3456-9739-187868ec4998 | -15.43415 | -56.07224 | 2026-09-11 04:10:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e2ffb1b-6536-3be5-9c04-28fce2c3e18b | -18.08191 | -46.85134 | 2026-09-11 04:10:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2722cae-6547-3e8c-836d-3f7b52f9053b | -14.5964 | -48.85699 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8c7067c-2e14-3e20-9d32-022fdd68473b | -13.77436 | -43.64267 | 2026-09-11 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32884b58-55fe-3ee7-bbbe-042e1ca441a0 | -14.61153 | -48.85054 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2118d424-597c-369e-8de5-67c59283f71c | -14.59832 | -48.85934 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1214f9fe-2a09-395d-a58b-be73db103a25 | -14.91449 | -44.66814 | 2026-09-11 04:10:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b68372d9-84b8-327e-b3ca-0661f1688b9c | -12.34973 | -48.20238 | 2026-09-11 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f1e0286-87d8-3ff8-a9ae-a8f86da07fe0 | -14.60531 | -48.85887 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a240cd9-2fe5-30c0-b444-a17c0243f2ed | -14.65701 | -44.12106 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46358327-90b7-3a36-a3a9-3bbc74379012 | -14.58747 | -48.8552 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44839abe-e783-336b-b51a-4ca7ac42f196 | -14.59545 | -48.86193 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 757ec93f-0765-3342-a53d-c663d246b376 | -19.06726 | -43.08183 | 2026-09-11 04:10:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 379e255d-f73a-3897-93bb-3563c5697edf | -19.0114 | -49.48287 | 2026-09-11 04:10:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1186c81-ebf5-30bb-a274-f02b4988c9fe | -13.50302 | -44.06814 | 2026-09-11 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71d04c31-a599-3190-a939-1c87de4c2139 | -14.58042 | -48.85595 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 41c3ee9e-906f-3e83-9d0f-fdf6214d7b0f | -14.59991 | -48.86285 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9f8f1ff-d47e-39a6-8d46-d85df00a11a5 | -13.00461 | -44.11446 | 2026-09-11 04:10:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f87b314-04bf-3c02-aa7f-8f89c91ece71 | -13.77158 | -43.63831 | 2026-09-11 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ef6f586-5549-39b4-ae8e-5fb34010220d | -14.90962 | -44.67551 | 2026-09-11 04:10:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e0e9990-11e9-3315-a729-4145af90e9aa | -18.63299 | -43.22752 | 2026-09-11 04:10:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9742e4e6-f437-3557-b2ea-25fd3db4f42f | -17.59602 | -44.6216 | 2026-09-11 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f678d6e5-10b9-3242-ae9d-8cba4ffb5926 | -14.91311 | -44.67614 | 2026-09-11 04:10:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2618ab0-5281-3b08-bbf2-349434a50a08 | -13.86023 | -43.6335 | 2026-09-11 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c2313a8-050e-335b-9b41-4a6ab23d38f1 | -14.60367 | -48.85538 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d9da2a-172b-35c8-bfea-9767776f76aa | -13.77096 | -43.64207 | 2026-09-11 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1240d52d-0d93-34f0-b913-4df54edb0da1 | -12.44791 | -47.16666 | 2026-09-11 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c01221f-d0f9-3519-b17a-2f6b2dcae48b | -13.00113 | -44.11385 | 2026-09-11 04:10:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6709c900-52ab-387a-b120-598f248d8093 | -12.99764 | -44.11324 | 2026-09-11 04:10:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73bc0f4f-fd14-3901-b1a9-ae4627af21c0 | -13.48838 | -48.559 | 2026-09-11 04:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b577f768-0ca5-346d-a3c7-45288cb7805f | -14.95348 | -47.52352 | 2026-09-11 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80a7a540-4423-3dd7-91ce-55d045d7d335 | -13.73171 | -48.97445 | 2026-09-11 04:10:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 452618b1-09d0-3733-ade2-cb97f431d1d8 | -14.59194 | -48.85607 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d51ba65-5cac-36db-8159-b92029875168 | -13.5538 | -44.16973 | 2026-09-11 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15bce936-5209-3554-8227-20c365ace97a | -12.88365 | -47.42678 | 2026-09-11 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd8782c0-8099-3790-87f3-f52c1d3b9bb3 | -13.85295 | -42.4447 | 2026-09-11 04:10:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10903b4f-9e61-3975-9d7f-0ffc1e95e3b7 | -14.60189 | -48.8651 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cffadbd-3369-3127-91a6-c4403796b126 | -14.58491 | -48.85667 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2b2d5f7d-9e55-3748-a35a-bed07672a08d | -14.66884 | -44.13504 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2aa3b6c0-efa5-3612-b6d7-a1595f555371 | -18.03821 | -43.01707 | 2026-09-11 04:10:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a9ef0763-af61-300d-b222-5d29b28de4e4 | -12.87945 | -47.42599 | 2026-09-11 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 333999a6-5109-3ef8-a462-6222c671fb13 | -14.95679 | -47.52366 | 2026-09-11 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 861e4b69-7ec1-34d1-b2aa-80b18647d520 | -13.4804 | -48.55215 | 2026-09-11 04:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5235eaa-838c-372f-9c85-07945b74d9fd | -14.07368 | -45.62059 | 2026-09-11 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 835e2377-badf-331a-a3a5-3893b1008e85 | -14.59743 | -48.86422 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7200a05-f18e-3b05-89db-a5b8e61ead1c | -14.9138 | -44.67214 | 2026-09-11 04:10:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b8d4254-9298-39b1-a9bc-9fd9311df611 | -14.06846 | -45.62882 | 2026-09-11 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee94b482-d7b3-3aca-a68a-83c1f5cfe575 | -14.58402 | -48.86153 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f0166205-110c-3756-b761-3a432dee0a0c | -14.67151 | -44.13472 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 11ef32e5-5b5b-38f3-afae-f4051cf02ce2 | -14.65637 | -44.1249 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af3bf37e-9a23-3289-97c1-ef81100afa7f | -14.60712 | -48.84936 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fece3dd-89cc-353d-a5d9-6beb1008a3a5 | -14.6738 | -42.85104 | 2026-09-11 04:10:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e3e1eed4-7882-32ad-a4c5-85e4539245af | -18.07905 | -46.84572 | 2026-09-11 04:10:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05f5032a-d0d2-3625-9fd4-17284ee59559 | -14.60456 | -48.85053 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7d11513-44dc-39d1-a980-0c309f04d68e | -14.13108 | -44.01179 | 2026-09-11 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8adf3e57-859a-3102-9329-b19cb4342d11 | -13.34328 | -43.74458 | 2026-09-11 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9a333434-366c-355f-a08d-9e8532abb86f | -18.14614 | -45.37996 | 2026-09-11 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 038f3231-a7b8-3457-93fc-ad7f84e6d5e6 | -14.60103 | -48.86982 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 541168dd-2113-33df-ab9a-da8f3275b308 | -14.5894 | -48.85748 | 2026-09-11 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d96c260-6b84-3271-a26b-8c2bfdb93029 | -13.50648 | -44.06872 | 2026-09-11 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47ec517f-e027-39be-bf92-46eea9498258 | -17.71969 | -42.27991 | 2026-09-11 04:10:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 347f4198-edaf-3fe6-8c5d-0255138c818d | -14.07445 | -45.61613 | 2026-09-11 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7645e457-5816-37da-a08a-cb0857391881 | -14.67713 | -42.8516 | 2026-09-11 04:10:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fb6723f4-27e4-36e7-909f-f89b507caeeb | -18.70181 | -44.47594 | 2026-09-11 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 680726c9-408a-3a90-89a8-938a6a8cbfd5 | -14.66947 | -44.1312 | 2026-09-11 04:10:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 848515fe-19a1-3670-875a-c96eff057b95 | -15.43559 | -56.06585 | 2026-09-11 04:10:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e756d25-63a5-38a3-a51b-0721f0b94310 | -13.4795 | -48.55694 | 2026-09-11 04:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0640378-37ab-36c1-bab6-531124443b0a | -16.58989 | -43.63421 | 2026-09-11 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5769efd5-4e9d-33f4-9c3b-56c967866d9c | -14.06923 | -45.62435 | 2026-09-11 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
