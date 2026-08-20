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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ad65090-ed97-31fd-89fb-dac40a27e401 | -8.5725 | -54.7477 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abc2f625-c19f-3d34-9e41-c7d5b6646b9c | -7.3796 | -55.534698 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c42b04-1a67-32c4-8372-c164eaeba3f8 | -11.1953 | -53.996498 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc625600-d775-3e9f-9c0c-397b49caa23f | -7.5344 | -55.582001 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e639812b-6270-364c-8727-52b8cbbdc601 | -8.899 | -60.536098 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44be3245-484e-3803-9d2a-3049ce3afeec | -7.338 | -55.6702 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0d408d1-bf24-3477-9ef2-8b8658732888 | -17.778099 | -49.1311 | 2026-08-20 01:02:00 | METOP-C | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db6a7c5f-f375-30a1-af4e-bd2879bdebb3 | -3.5307 | -48.166199 | 2026-08-20 01:02:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7481239-cad4-3258-9528-ea35a229dded | -8.5571 | -54.816799 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca75f6a1-a17c-38e8-a961-067629694075 | -10.7859 | -50.300301 | 2026-08-20 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8d9da0d-c05b-3feb-8c1f-c1564239bedf | -6.3592 | -54.8951 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60004649-e4e9-3ef2-883f-db3f4d6ddba7 | -8.5045 | -54.8578 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4d42574-4b44-3c95-86dd-c293935910ad | -12.4719 | -54.740002 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4179a358-e14e-32bf-b8de-da70678df240 | -6.6898 | -59.1003 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78066e6c-2894-3012-9614-5c1e9aa3248d | -11.8238 | -44.817501 | 2026-08-20 01:02:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 237e7535-1ac4-3269-b35a-935fecae09f3 | -8.5304 | -54.881199 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2ff3558-7e6f-32b7-87fe-c35985e7b10a | -6.7927 | -59.571999 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9accf24-bd90-3adc-8690-dfc09819858b | -12.7609 | -48.455101 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a7ed8c8-512e-3519-a187-8b3b0bdbfa58 | -7.6067 | -45.1726 | 2026-08-20 01:02:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5b6ebbc-8c81-312a-a9be-1dc4bde726f0 | -8.5807 | -54.738499 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 243eaa42-da2e-3708-a005-9c0ecea82d77 | -8.1027 | -51.668701 | 2026-08-20 01:02:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e6a92b-5089-3557-9075-3a1fbaccc6a5 | -18.848801 | -47.133999 | 2026-08-20 01:02:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6250e435-6f47-33a8-a665-e9ab559836c8 | -8.6699 | -54.631199 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 412110fa-1126-3089-9787-2e84fc679bf0 | -10.7879 | -50.3088 | 2026-08-20 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffe025b7-5cfd-3e82-b142-7d3810ddeccb | -12.4801 | -54.730499 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09cd48db-5b50-355f-8aa7-5f31aea147f6 | -23.068399 | -49.151699 | 2026-08-20 01:02:00 | METOP-C | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec06392e-a48d-3dab-9342-acf08e2eb4b5 | -6.5891 | -58.967999 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6904d30a-74df-3ac7-918c-d65ec051df94 | -6.3608 | -54.902 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1809680e-b98c-31bd-8510-2b744152adb8 | -1.8429 | -54.4911 | 2026-08-20 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3830c3fd-aa39-3bc9-ad0c-cef5fc3a9274 | -7.3522 | -45.837799 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b897c102-4f15-318d-b136-a6ae5ceca733 | -14.3542 | -51.916901 | 2026-08-20 01:02:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 552ba269-2123-34d8-82dd-03f12dd41dd6 | -8.662 | -54.5965 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff9ba32c-9366-3234-a7d4-dbe1a22efc77 | -8.5838 | -54.752399 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3798dd86-805f-3963-b64b-8819331c0ffa | -9.4193 | -60.442101 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 529eeaf8-146b-30ea-ad66-eff5b11e9396 | -2.1653 | -47.471199 | 2026-08-20 01:02:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4fb1c1-ef1e-3c10-8aaf-247fc4f79860 | -9.4096 | -60.444099 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6133d4a-1d2d-3abc-b89c-1959b4c9d247 | -4.3858 | -55.4646 | 2026-08-20 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd6e5ff-a99a-307e-b275-2d44c8c5081a | -10.3338 | -57.567501 | 2026-08-20 01:02:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd1faeb7-3c14-34a5-8051-556520f1dc1e | -6.5772 | -58.960499 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80ba2f67-ac29-37c2-be1d-574a86172fff | -14.4403 | -45.6129 | 2026-08-20 01:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1bd785-6ef9-33ed-88e8-263683201d8d | -6.4446 | -52.748699 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91a3c70c-6f2e-387e-b274-1c7cf6bfc1d7 | -9.1216 | -61.603001 | 2026-08-20 01:02:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3080d9d3-1517-32ef-be9e-e6bd761e783e | -8.673 | -54.645 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0719ca47-058f-319e-9f88-26ad80e5d59f | -10.5196 | -50.790901 | 2026-08-20 01:02:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e714f50-8d2c-31f0-b0ba-0a09f9df4c2e | -12.4947 | -54.750198 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abdc7c95-b13c-38d4-a79e-932fdea09ccd | -12.7707 | -48.452599 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb7cefa1-c966-30d3-a80a-13995f23b351 | -17.330299 | -43.623402 | 2026-08-20 01:02:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 88cac317-996f-33b9-88d7-43be0697fd1b | -7.3529 | -45.799301 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fee4f662-3931-3703-8895-0e3119a71543 | -15.5444 | -50.273602 | 2026-08-20 01:02:00 | METOP-C | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be3b93b2-623c-3b8d-94df-6479ef426dba | -6.3898 | -54.938702 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 227906c2-6e84-3e32-be99-436e98aedc42 | -8.5622 | -54.7938 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 046d482f-44e7-3aaa-b389-a13cdf320f61 | -11.1902 | -54.019699 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79217a91-b760-32c5-8fd2-665355f1b802 | -6.4297 | -52.729 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc2e61e-0d09-3644-b0a2-8116afee343b | -8.5642 | -54.756802 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47cf3598-5b3d-3664-86d7-15281eafd627 | -9.1165 | -51.148602 | 2026-08-20 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02d22930-dd77-3ba7-84ea-9fcc5f194392 | -21.7141 | -47.139702 | 2026-08-20 01:02:00 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 03297f21-5a45-380a-947b-49e81c00e19c | -6.587 | -58.958302 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb539065-d167-3208-a8e9-4be40b9fccda | -11.2359 | -54.826 | 2026-08-20 01:02:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb62a1dd-10d7-3a07-a7ca-8cb682af41b3 | -9.411 | -60.402401 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa84ddc0-1569-3338-a56d-4784aa8be8f9 | -8.5402 | -54.879002 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f17f9fc-165c-3a4e-80f7-ac635a9b2709 | -7.6114 | -45.150398 | 2026-08-20 01:02:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca2567c-7808-3e84-afec-960f6fde02e6 | -9.4208 | -60.400398 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a99fe2b-8407-3730-a6fa-f8c4d5cf0607 | -12.795 | -48.425098 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92a37e93-2222-3d96-855c-2f2d483bf20e | -8.5493 | -54.782001 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9b1c3ee-1da1-3664-9468-35a75538e6e7 | -6.3815 | -54.9478 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4810a9a-33dd-369b-a6b7-fc1706f4fae3 | -8.7114 | -49.6166 | 2026-08-20 01:02:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 111d7c03-4890-35e7-8202-28e762d4dc29 | -8.6812 | -54.635899 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b11aca-ff8c-3c8c-b395-83f55b254644 | -8.0991 | -51.653099 | 2026-08-20 01:02:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2275632a-69a7-38cc-8d0f-b96d8297b56e | -8.4978 | -54.873901 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0453f0cf-8e64-3a7f-85ef-3ca76f79f198 | -7.338 | -45.822201 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 758419ca-cb62-3451-8304-b63e950442f4 | -7.7553 | -49.203899 | 2026-08-20 01:02:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9a179e-9512-3663-b6ac-c7912ad9723f | -7.3425 | -45.840199 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd8e1b6-0331-3c28-a7f3-e0a31a313977 | -14.1784 | -53.0569 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc6b23b2-29b1-35a5-954f-fa802b755ab5 | -8.5787 | -54.775501 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 995c245a-d666-3a87-8da1-3aff435d6f27 | -1.8331 | -54.493301 | 2026-08-20 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6261b8a8-2dc3-3d12-a13b-2d11f20a62a9 | -9.206 | -59.766201 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69d003ae-61be-33a7-ab7f-c0dff0d0f0f0 | -15.4507 | -48.5774 | 2026-08-20 01:02:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09802b0a-c881-3f03-b13d-ac2a40993b16 | -11.2121 | -55.0439 | 2026-08-20 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1d8a774-3249-3430-aa6f-ad03e3fbadb2 | -9.1021 | -60.9221 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9904390-e4d3-389c-b902-c1a8edffa206 | -4.5067 | -55.452099 | 2026-08-20 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5c1c682-a3b1-3201-9a91-4c1af1e3bb20 | -7.5493 | -55.5564 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db6ba71-9b83-32c1-a58d-57b8a883a4ef | -6.8953 | -55.716301 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3368d365-c1cd-38d7-b819-679b7074f9f8 | -5.7965 | -55.7313 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c08639-82ba-3e6a-8965-03829408e7a4 | -6.8693 | -59.0308 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eff21b3f-8b83-308f-8466-0aa515912cff | -5.7933 | -55.7173 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 734184ce-d54d-34fa-937a-aa489038de80 | -6.5836 | -58.989601 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3d55cb9-f276-3a32-93cc-a6d9c7c36dc4 | -4.5051 | -55.445301 | 2026-08-20 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26c1c5aa-efe8-31a2-b8db-d354f1e642f1 | -7.5442 | -55.5798 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62275b60-c45c-3558-9c53-30681f01d91c | -6.38 | -54.940899 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0a7a296-e51c-30ef-8bcd-18ac6d85cb5a | -6.8332 | -56.449902 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f0a455d-2e74-3dce-b6bf-4cdd77930b2c | -14.4537 | -45.624599 | 2026-08-20 01:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eddb7ca7-1dc5-352e-a62c-c4e03ba753db | -12.4931 | -54.742901 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36c69112-7454-3e51-bd67-f66e22bd6454 | -12.4915 | -54.7356 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94ac4558-036e-36ab-92b9-152414575dc8 | -11.8171 | -56.598598 | 2026-08-20 01:02:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9c1ac22-9630-3604-8d01-a5ff49c4b3da | -13.4086 | -54.369499 | 2026-08-20 01:02:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 122ec332-3c5c-35d1-bdd5-cd9e3d8897f8 | -4.9505 | -56.2729 | 2026-08-20 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab25aa40-f033-31ba-927c-e644191d6562 | -7.7677 | -49.2122 | 2026-08-20 01:02:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90bd3762-3681-3438-819b-d0edfb813fcd | -5.7901 | -55.7034 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4aeca70-13b0-34b3-8a57-850ef3f3f804 | -6.2464 | -55.397598 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463ed66b-03e3-3218-95a7-86a065325145 | -4.4561 | -55.4562 | 2026-08-20 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
