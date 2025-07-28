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
| 9e27e5eb-ed20-3562-912d-afa35d041d7f | -19.08571 | -43.6363 | 2025-07-28 04:42:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 891578e7-5360-3cc9-a6b0-20ec249e19f9 | -12.0772 | -63.55181 | 2025-07-28 04:42:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0438f18a-d3ff-3428-a4c2-85249c9ba75d | -14.4924 | -48.64836 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 147ca0e9-383e-31e9-a26f-7b218312301a | -14.31522 | -54.15134 | 2025-07-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3a729bd8-27b8-39a3-b8dd-6feb4c7e1a5c | -12.0761 | -63.5555 | 2025-07-28 04:42:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5732074b-0f0e-3807-8c2e-c1465e623262 | -15.53971 | -47.38557 | 2025-07-28 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8e55d96-60f8-33b8-8ebd-f2bea174f2bb | -17.3632 | -42.63705 | 2025-07-28 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c53ba406-7236-394b-beb4-fdbc9108665f | -15.9568 | -49.16927 | 2025-07-28 04:42:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5499e137-b145-351b-bd70-9c6c7d7c0ebc | -19.0809 | -43.63273 | 2025-07-28 04:42:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d31c4518-3522-3803-b78e-7019fff4718a | -16.60362 | -47.82315 | 2025-07-28 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6a8d3f8-6be0-38d7-8ed7-ea8258a6fc8f | -14.49283 | -46.54317 | 2025-07-28 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ff6a558-0486-38bb-b994-b0ad83ca4c9d | -13.52298 | -46.29082 | 2025-07-28 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63cde0ba-91c0-327e-ae00-a30cff6f0bf4 | -14.48956 | -46.53727 | 2025-07-28 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 894a285d-8380-38e1-a1f9-325f8d63d612 | -17.36205 | -42.64751 | 2025-07-28 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| db0d408c-2722-3f0f-9f39-cfc46376e338 | -14.98023 | -46.96259 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eab43b71-9640-31cc-9626-49c95b5e01c6 | -13.52744 | -46.2879 | 2025-07-28 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 836697a1-419f-3638-bf8c-c53224b44a95 | -14.98354 | -46.96746 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e82fa56-600c-352b-aa93-1472ad3cbfce | -17.35746 | -42.63978 | 2025-07-28 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e25f25af-9251-3889-b81d-93f16c0ec447 | -16.60673 | -47.82868 | 2025-07-28 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| df45111c-1469-31a0-9b1c-272b76bb0e5b | -19.08339 | -43.63237 | 2025-07-28 04:42:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1b80f2d-49f0-37bf-ac1d-aa49dbf104e1 | -14.87435 | -48.40018 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba9ae6cd-bf4f-3847-8261-9ad14f19e5f3 | -14.99016 | -46.97718 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59395ae7-bdc0-3dc7-a086-550e9721fe63 | -14.49537 | -48.65295 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 495aa3f5-7b4c-3d51-9f49-b193dd6c82fd | -14.4968 | -46.5438 | 2025-07-28 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea07209d-4401-368e-b3f2-ee7894307274 | -14.57793 | -52.8777 | 2025-07-28 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0253c2ce-8646-325d-a372-89944baeec48 | -14.4816 | -46.5361 | 2025-07-28 04:42:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4effb032-907e-34fc-9c7e-e2631cadb446 | -14.49948 | -48.64948 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fdeb438-3da5-33d1-825c-7da939e0ee15 | -14.51544 | -48.66442 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6de637dc-e6d7-3efb-83ee-fb6145394fc0 | -17.21409 | -44.85286 | 2025-07-28 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50c134f2-2687-30cf-811b-7458fa7719b9 | -16.02775 | -48.02432 | 2025-07-28 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c6b9534-a384-3a87-839e-a7b0036a3c74 | -14.31942 | -54.1479 | 2025-07-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e59e6451-d0c4-33b7-817d-c104c4809c03 | -14.50598 | -48.65464 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b69cc601-5b66-3172-a9d1-329e02c5d4f4 | -14.31239 | -54.14661 | 2025-07-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a15edae3-df2f-314e-92a7-3e8b2b14daf7 | -14.5119 | -48.66389 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c401e1c2-e0b9-3675-bdd2-bcaa087ea384 | -14.99079 | -46.97254 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b012dd1-fb7f-360b-b97f-25522881a567 | -16.96907 | -50.19934 | 2025-07-28 04:42:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d70cfd1b-76fd-386b-8314-a3e8fa90fc16 | -14.49891 | -48.65351 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaba6858-1ada-3ce9-a750-2a0c9fd999c9 | -17.35172 | -42.64263 | 2025-07-28 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0518831f-7075-3eb8-aa4f-d717bc0861c2 | -17.53824 | -43.92381 | 2025-07-28 04:42:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd10e9c1-8ca3-3ae7-a765-3db288265d43 | -15.14969 | -53.51183 | 2025-07-28 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71f5fd7b-cece-3f09-80bc-f82d44b71f1d | -13.52521 | -46.30455 | 2025-07-28 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe11c719-3b25-39e5-a759-9a5ede4c4b60 | -14.49652 | -48.64488 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 196f2809-e47a-3619-a3ca-6d39eba38fe9 | -14.98685 | -46.97229 | 2025-07-28 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2637e566-a214-3bad-8dda-92d2b788b236 | -13.52989 | -46.29996 | 2025-07-28 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e3e1a37-7796-3e60-a67f-6b73c9e493f8 | -14.48558 | -46.53667 | 2025-07-28 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82317334-fb22-3d94-9014-5a7041effc56 | -14.51306 | -48.65574 | 2025-07-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 377b11dd-e350-30fb-80a6-62ce887b5ad9 | -20.47899 | -54.74285 | 2025-07-28 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f62618c-dd95-3552-97b6-56ac5c736d01 | -23.32664 | -46.88725 | 2025-07-28 04:44:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| afc791c1-e7a3-3867-a2da-450156ef95a3 | -18.39912 | -54.89026 | 2025-07-28 04:44:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 192080c4-7bc8-3853-83ce-aa2be1f56524 | -22.03843 | -47.57138 | 2025-07-28 04:44:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a15bdc60-dc86-31c8-a8d6-a81a977e480d | -23.32692 | -46.8886 | 2025-07-28 04:44:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| aff3eeb1-e21a-3d87-b8de-844a4ab3361a | -23.33104 | -46.88773 | 2025-07-28 04:44:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 84775744-0b03-3898-8638-e336da4e1965 | -20.47701 | -54.67042 | 2025-07-28 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5eac2a06-7b6a-3a99-86bd-647934a36e96 | -20.47935 | -53.67449 | 2025-07-28 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a51178c9-0b8c-3d29-8e4f-e18285eaacde | -20.48627 | -54.57245 | 2025-07-28 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07f178e3-d690-3eed-990d-e53fbd614780 | -22.03794 | -47.57538 | 2025-07-28 04:44:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62ed85b1-b740-3a21-91df-edd51cf37b0a | -19.50968 | -48.47459 | 2025-07-28 04:44:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a10b0735-fc29-3200-a008-179ec360ba6c | -19.96717 | -44.1626 | 2025-07-28 04:44:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7cca8465-155a-3ff0-967d-a24b1d1709b4 | -23.33131 | -46.88912 | 2025-07-28 04:44:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e022a2d2-469a-3058-b3ed-c20576d2f562 | -20.49351 | -54.6975 | 2025-07-28 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62d1aa0f-3d74-3b84-93a7-5790e9941389 | -22.03892 | -47.56739 | 2025-07-28 04:44:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b83d377e-e46d-3501-80ac-e6774b41d456 | -18.40259 | -54.89095 | 2025-07-28 04:44:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| afd72d20-d2db-3c8a-ab68-372ed4bb02d2 | -20.14296 | -52.83673 | 2025-07-28 04:44:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb73f49a-3f0e-3850-8217-1aff06bc257b | -19.50904 | -48.47953 | 2025-07-28 04:44:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15a4486c-0264-3284-bd68-01740acbd0cc | -19.97118 | -48.4245 | 2025-07-28 04:44:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3810eb7-5ad6-3ff8-8b34-69f780c83dd3 | -23.32742 | -46.88398 | 2025-07-28 04:44:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 16bf3e5b-0109-35a2-aae4-9e99cdcd960c | -4.1603 | -46.8101 | 2025-07-28 04:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c4477ecf-9481-3c80-89b3-53edd257d1f0 | -6.4889 | -56.2139 | 2025-07-28 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| bc855ec1-7edc-375d-afaf-c1b2dc9a1687 | -6.5074 | -56.213 | 2025-07-28 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 788171b3-2e1d-3fbf-b31b-b34dffa4f8a3 | -4.10711 | -47.93597 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44e72f56-9499-3045-9c4e-5bef0f77039e | -4.16348 | -46.81982 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4a74de3f-358a-3a21-97ec-169721d00cdb | -3.4024 | -47.49939 | 2025-07-28 05:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ee198e4-8b94-3901-86b3-457a44ed5dcc | -4.15422 | -46.812 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fcac463-90c3-326b-9632-b9654031af34 | -4.11259 | -47.93175 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3fe0a245-3ee7-3404-ae05-f67f27467ce3 | -4.16302 | -46.82289 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a169679d-bc97-3cf9-af81-b0f40fc5419a | -3.80091 | -47.50602 | 2025-07-28 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1d40cfda-83e7-3b39-b0ad-8c09e9f9e657 | -4.07587 | -47.95123 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87ea395e-a9f2-3df0-8f32-ccb7d1b56e7f | -4.15837 | -46.8191 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f42b4ae-99e0-3e0b-87d8-54214ba5efa6 | -4.1138 | -47.92811 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ce0b665-a424-3301-985c-adfa5a6bb6ec | -2.94468 | -48.0507 | 2025-07-28 05:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45a883f6-cec0-3f27-b55a-aac2939aff13 | -4.16769 | -46.82653 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b6a326c1-2828-3f58-b347-e6e0910adcba | -4.16442 | -46.81356 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab4590c4-7915-3b7d-9923-1d3589ac1a5f | -3.39757 | -47.49877 | 2025-07-28 05:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 635ed14d-0526-3b59-a1ad-0b16a7d20bf4 | -4.11395 | -48.12457 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26a5d8bf-a165-3c73-a90c-9dedeca8f517 | -4.11182 | -47.93677 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7c2fcf5-6b8f-3473-8cc9-939c7a8c1786 | -4.16626 | -46.82067 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8d82ec7c-be99-3963-8a53-af00754c082a | -4.16672 | -46.81748 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 37bd14ff-55d8-3b6f-a6d1-24401bb4a6a8 | -4.11457 | -47.92277 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01412d95-0b85-3c0e-abae-423bdea29daa | -4.17095 | -46.8243 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 52531455-1988-3a4d-b93b-deeddc8d2277 | -4.15883 | -46.81602 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cdc0dad-4a9c-3aee-b895-7fba59938187 | -4.1593 | -46.81292 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a4ae90b-67ba-3061-b0da-d781d5567458 | -3.50609 | -49.05294 | 2025-07-28 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 365011d5-04e4-3ce5-bbbb-c4526c4988a6 | -4.11306 | -47.93323 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a94ac6d9-87e9-3e56-92a8-ad30e3f6a447 | -3.21959 | -48.8142 | 2025-07-28 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 79ae9020-c62b-3892-9e42-d86c69fe7411 | -4.10762 | -47.93748 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54114457-74c1-38cf-b7ef-7955faccc5f9 | -4.10928 | -48.12394 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 308cf139-56be-3cda-b576-ad291ad39016 | -4.16582 | -46.82377 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 51ada258-16d2-3f39-aef8-29f3e2a0a20f | -4.10789 | -47.93086 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 164f6885-fb17-3184-b7f1-df7cab082f6d | -4.16816 | -46.82342 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1671ec17-1b82-3ec2-91aa-7834f76a3488 | -4.1091 | -47.92723 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README15.md)
