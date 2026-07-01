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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 483c4fb9-b601-31f7-ae2a-598ca20ffe44 | -10.85248 | -56.65774 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77cbb985-538d-387d-9738-9549d3b01691 | -9.60593 | -56.92146 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 66dbd342-7fea-3d18-ba1e-a423de47e3b2 | -9.33319 | -58.02059 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16791023-a1a2-3f0e-8166-e227e2a13cdd | -9.60443 | -56.93382 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a93eda6-caa1-3322-8432-66dfa3076b16 | -11.42741 | -56.05816 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 726693e6-e613-3d8a-8b87-6f1dc156175b | -10.85204 | -56.66127 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7af43f9e-f116-3c3c-8c9f-18246b4e19c4 | -13.26484 | -56.80367 | 2026-07-01 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce546ee1-c653-380f-9a06-4e50aac09a6c | -11.90632 | -57.38194 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b985b5d4-b703-34d5-81cc-7ff05179fac2 | -10.08271 | -60.49344 | 2026-07-01 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b282a3cb-1a6d-346f-ba63-5311cead418b | -9.69131 | -56.10112 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67c5da3d-5767-38ae-adb7-4f50ede65900 | -10.76743 | -53.54076 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d95b26ee-3ca7-3e4d-b5c5-37319f810964 | -11.42879 | -56.06528 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b99da64d-e919-3a0d-aea6-1e15ebc753d1 | -11.63508 | -59.01705 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ae8266a-707c-3cb5-b3c7-0394e61c3091 | -9.02017 | -59.54469 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec76f6cb-38ee-3b18-889a-41617af9673c | -12.4161 | -58.38787 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ab605bd3-4906-3dfe-9012-02f18db9e6ab | -9.08708 | -59.48784 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85b6301f-4311-39ac-a4a6-8bdaf929c5ac | -12.41739 | -58.40557 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f4da5042-9eb3-3b9a-b41e-ab35757c5454 | -11.63103 | -59.01138 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab725266-642a-343e-bd3d-7eaa4da04aec | -9.02573 | -59.53685 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 971fa1b6-ea43-36fc-b949-e8b026dc155d | -10.76449 | -53.54819 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ccbdb19-1b2b-32db-a99b-6ff8eac9cf73 | -11.04439 | -56.92104 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d627331b-59bd-3e56-a29f-fb21e0458c76 | -9.6042 | -56.93437 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc30517c-78d5-3355-9b27-26f8bd62962b | -9.69176 | -56.10301 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db721b36-dadf-3772-907f-3f9c41e2ec21 | -11.42172 | -56.05731 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 3a6b3402-41ac-315e-8e4d-d89d08d57960 | -12.80186 | -54.86145 | 2026-07-01 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe9ee319-1548-3c9f-86fa-585fed1beddd | -10.67146 | -54.52905 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 66a5fb97-6c20-3118-bad3-fadc9f814049 | -11.63038 | -59.0164 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7f5c0cb0-cc51-34d6-8d29-d07d92f91480 | -14.63348 | -54.46408 | 2026-07-01 05:44:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 675348b7-9c30-33ab-95f5-5120f20a0917 | -10.68332 | -54.53588 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 17ba5e8f-6373-3336-afef-26dce3ad8fc5 | -12.42747 | -58.41837 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac602467-de36-3efc-b7e7-438b6fbd76ca | -11.84548 | -56.95087 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a2c043c-c963-3971-aeaf-562b2a31ae40 | -10.6783 | -54.52477 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| c66168f0-4d06-3200-84f8-dff24643d433 | -11.902 | -57.41779 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b0c3502-73d9-3360-95b2-cabc3e88479b | -12.21773 | -56.56138 | 2026-07-01 05:44:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69e38ff2-3e94-325f-a354-d9e4efa29532 | -11.42221 | -56.05336 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8774c9a8-98bd-3773-a36f-a94152ddd74c | -9.63795 | -67.34963 | 2026-07-01 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4629cfd5-8784-31a8-b36e-ff0e2c0d8188 | -9.6105 | -56.92808 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d113239-3ed4-38e8-8511-085904d765b6 | -11.71723 | -59.35586 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e2955b5-9873-3f8c-955e-88b592faabb6 | -9.1765 | -58.06767 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3481b077-c6e0-3596-9981-4c0daa2a5f3d | -12.41812 | -58.39991 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c58f874a-aa30-33e6-a198-5754f9f3597c | -11.43542 | -56.05825 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a1b7d7a-8371-3cf6-8195-6c765eda57e3 | -9.60565 | -56.92412 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c64102b-e52a-3b01-bb13-7a4a14e05774 | -10.76674 | -53.54655 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| de1ff5c7-548a-3a3f-96a6-9d6755b3ddf7 | -11.62504 | -59.02076 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 52466078-5726-3139-8a8d-11c75c398642 | -9.77753 | -63.50567 | 2026-07-01 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e976579-7ec1-315e-890d-ad1132e3de7d | -11.8459 | -56.94741 | 2026-07-01 05:44:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 083ab0c2-72d4-38ef-806b-f53cafe27119 | -9.33001 | -58.01991 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10e1df6f-d326-32ba-9815-1e7e6618fc43 | -16.36607 | -56.66063 | 2026-07-01 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 8343f3ef-0679-3df2-9898-aa1cc912b571 | -16.35438 | -56.65919 | 2026-07-01 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 879ff421-ffaf-3a8f-baa8-bb54bad3ebc5 | -16.35514 | -56.65825 | 2026-07-01 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| efc61bbc-2a09-3229-b7a6-bd03a8cc1048 | -16.36022 | -56.65994 | 2026-07-01 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e40d0a23-085e-3407-b599-bc27c50112ff | -21.0977 | -57.4708 | 2026-07-01 05:46:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a939fc87-acaf-399c-9e4e-a78595ac0f92 | -16.35978 | -56.6643 | 2026-07-01 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 9fb14cd7-cc10-383d-b945-9ad9c1d337be | -16.35467 | -56.66262 | 2026-07-01 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c93cfc8a-3c0d-3d59-8255-4f9bd1173019 | -16.36067 | -56.65554 | 2026-07-01 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a61682b2-5dd6-3adb-9f52-9f7d195cafba | -21.0981 | -57.46639 | 2026-07-01 05:46:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0aa53dad-daae-3a49-95ac-61649065afe5 | -10.9209 | -43.0384 | 2026-07-01 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| c574efe5-e43c-3194-8963-f729d9876d70 | -12.8359 | -44.3422 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 258.8 |
| 23599e94-a915-37cc-abb8-278e451a7c2a | -10.6784 | -54.5356 | 2026-07-01 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 42d10b39-ea25-3cf2-97b8-7833e285c2a4 | -12.8552 | -44.3389 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| b9673391-ebd2-330a-94c4-d8d5569caae3 | -10.6787 | -54.5153 | 2026-07-01 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 50d24d2e-fb28-3b43-ae81-42bab03a4322 | -11.4338 | -56.0509 | 2026-07-01 05:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4f443235-39fc-3cfd-bc70-3b29aa96bd4f | -12.7557 | -44.4959 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| cf649add-dd03-36e9-a44d-4660bbb8654b | -12.7755 | -44.4693 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| b662eb66-8493-33c2-8488-6e96af96aee0 | -12.8548 | -44.3625 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| cfc05262-4e4f-36a1-b28c-efe2e1aa267b | -10.9205 | -43.0622 | 2026-07-01 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0d3c756a-08d0-3032-8b7f-ad2055df71fb | -12.7562 | -44.4724 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6b7b365f-71f4-38c4-8383-4382068de59f | -12.7751 | -44.4927 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 4a68df51-4ac2-3c8d-b89e-677aa2cd40e6 | -12.8354 | -44.3657 | 2026-07-01 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| e07a31fa-b830-3b53-a810-36386014d946 | -11.4336 | -56.0711 | 2026-07-01 05:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 48ee65f7-2be6-31d7-b17c-3e55ea70d92b | -10.6598 | -54.5169 | 2026-07-01 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4dd625a5-7dc7-33b5-bdac-3efd96b187c6 | -5.13091 | -37.84105 | 2026-07-01 05:50:00 | AQUA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d27d7314-c7b7-39b3-844e-a5edb517846d | -12.82933 | -44.36706 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| edbb5131-8f07-34ab-9a7d-525dae806a69 | -10.92208 | -43.05236 | 2026-07-01 05:53:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| a863de36-234a-3460-88f5-c88b0d75c5d1 | -12.76274 | -44.51084 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a40098ca-c194-3ff4-a5bc-4b3f0c3e54c9 | -12.75483 | -44.50175 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3e0e14e0-2c69-3150-bd59-a6b25978eba3 | -12.83692 | -44.32454 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| be73ff7e-c3a9-39d3-850e-c9021114f479 | -7.70472 | -45.92274 | 2026-07-01 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| c4fac56f-aa81-3477-8eda-85d08d3d227a | -12.75868 | -44.47981 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 862797b6-0972-3447-bcd9-9957006afb15 | -12.77071 | -44.46714 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| b2d38b7b-70c3-3bc3-bc01-3d6ac3efa497 | -12.84615 | -44.3481 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 233.4 |
| 655ce687-9a7d-3b5f-8a35-3e9e9ee785c7 | -10.92521 | -43.03419 | 2026-07-01 05:53:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| e24306b5-e98f-34e6-bf29-40a4d3a899ba | -12.77183 | -44.4823 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 357.7 |
| 5e83502a-5050-328a-aacb-031f5efa424b | -12.76801 | -44.50423 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 6e180206-db4f-3110-9e0d-58ccd0b586b6 | -12.76674 | -44.48891 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 583.3 |
| 501c8162-64d5-3da9-a329-322baf9e4599 | -12.83314 | -44.34576 | 2026-07-01 05:53:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 397.8 |
| 6851536c-d5dd-379c-9e20-d3b8566c8295 | -7.70997 | -45.93108 | 2026-07-01 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 3d62a2dd-be0f-31ca-b9eb-bb54c16e1847 | -12.8548 | -44.3625 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9fba9570-9489-3c69-9b31-d653decd5d4e | -12.8354 | -44.3657 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| d0eed52a-d127-3ce4-b7df-2e2cfa72ab56 | -11.4336 | -56.0711 | 2026-07-01 06:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 567b6cfa-24fb-3a41-90ee-875d90bae3c6 | -10.9209 | -43.0384 | 2026-07-01 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a390646c-0cda-3f8d-bac6-e1755fdbeb01 | -12.7751 | -44.4927 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 0a5e1c8a-1350-37b0-b8ee-c67af9b6d6c3 | -12.7755 | -44.4693 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| d2580f52-be3a-35c3-baa9-f7442b1b2ccc | -12.7562 | -44.4724 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d48c45cd-08a6-32e1-9292-274f6d7c94ba | -10.6784 | -54.5356 | 2026-07-01 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a46dcd14-6499-3eb4-a2b8-31dbdea074e8 | -12.7557 | -44.4959 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| a3a79de2-f20c-3517-8af0-7dbf0dfb5b06 | -11.4338 | -56.0509 | 2026-07-01 06:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e72a7e45-39f1-3397-8b66-4721ce56e135 | -10.6787 | -54.5153 | 2026-07-01 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b1d8483e-6309-3900-9140-441489f2e895 | -10.9205 | -43.0622 | 2026-07-01 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 9ebd6d8f-12d8-3b9f-bc85-8b168d8e655e | -12.8552 | -44.3389 | 2026-07-01 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |


[Clique aqui para ver as próximas entradas](README30.md)
