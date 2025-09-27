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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ee26cd0-0055-36db-8452-c8d0f988761c | -22.50158 | -52.98576 | 2025-09-27 05:40:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| be3f8043-38a9-381a-96b3-a395aafa765e | -20.73354 | -57.78492 | 2025-09-27 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cb6887e5-653d-3d44-9c22-2175cea38f57 | -22.21583 | -56.19722 | 2025-09-27 05:40:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 983e49ca-9eba-3b3c-860e-0158885f8a1c | -20.73455 | -57.7747 | 2025-09-27 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| f48d7936-9b51-32b5-bb11-87e4d51c749b | -20.72896 | -57.77746 | 2025-09-27 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| d8855dc9-9d18-3431-8635-a3266f6ab72b | -20.73912 | -57.78217 | 2025-09-27 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3bb0f001-4451-340a-bb0e-ff5db7d48b3b | -20.88537 | -56.61241 | 2025-09-27 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 79e33351-5bb2-3ccf-a742-5430cf60019d | -20.88575 | -56.60836 | 2025-09-27 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 29.3 |
| b0c2682b-4909-358a-9d11-224dc88298fa | -20.73878 | -57.78558 | 2025-09-27 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ce839a98-3d9b-358d-8d79-59e0815f11e4 | -20.89179 | -56.60509 | 2025-09-27 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65ac05a9-07a2-3b7c-8ac3-2da5381999e7 | -6.7008 | -44.58087 | 2025-09-27 05:57:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 69586aff-be43-39cf-bf03-aba247e70d39 | -5.79256 | -42.83389 | 2025-09-27 05:57:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 78b05cf4-b1b6-3664-8bce-580a21cded5b | -5.46983 | -43.08179 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 0a13524e-eb99-32fc-8328-e73ea7e01dd1 | -6.52831 | -43.8323 | 2025-09-27 05:57:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| cc5d716b-4c9a-3ce6-9e29-5bb3afa33960 | -5.47998 | -43.08323 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| d75e9024-64ff-3350-80d7-0ece2ed0ff27 | -6.69486 | -44.58343 | 2025-09-27 05:57:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f85e7d56-bb5c-3eee-9798-ccfb73307c0f | -5.46138 | -43.06841 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b19de8ac-f36d-308f-86fc-e532ff39dba6 | -6.99383 | -42.38428 | 2025-09-27 05:57:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 3724e2cd-9dcb-3c27-b408-8aa701aaa474 | -5.48344 | -43.05918 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 296e6aaa-4b8a-3e95-a3a6-e9b074972022 | -6.69636 | -44.57334 | 2025-09-27 05:57:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2fe10374-0155-3203-9c35-ea45913dec90 | -5.07516 | -44.8524 | 2025-09-27 05:57:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 2dd33fe6-b2af-3218-b6c8-0ef6459f2058 | -4.79045 | -42.8256 | 2025-09-27 05:57:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8953654f-073d-3013-b44d-1414275133ca | -5.8083 | -42.79806 | 2025-09-27 05:57:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 848020ae-b6f9-3a05-aad3-d9456fcc59c2 | -5.47326 | -43.05778 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 33292265-1045-3d4f-9e0a-5f1be151dd8f | -5.49186 | -43.07274 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9d0572c6-d2a1-375b-b60d-9743f47a777d | -5.50949 | -43.86176 | 2025-09-27 05:57:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 54808a76-29cd-3316-9e97-367b71f8b761 | -6.42264 | -43.08026 | 2025-09-27 05:57:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3540fa7e-c728-3f9b-a4cb-d5a88165fe44 | -6.31912 | -43.44371 | 2025-09-27 05:57:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5be5924c-d4d9-30ac-886e-21626fd4b708 | -6.53022 | -43.83827 | 2025-09-27 05:57:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f848a559-5117-34ef-936b-3704cb7b78b0 | -5.79431 | -42.82162 | 2025-09-27 05:57:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 818e2021-d259-314e-b6a8-917024478f21 | -3.32627 | -50.2479 | 2025-09-27 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c7d3f953-4db3-3e17-a594-7009f4429060 | -4.80066 | -42.82718 | 2025-09-27 05:57:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1890ea63-bcfc-3d79-9165-c6dc3134afd7 | -6.42443 | -43.06786 | 2025-09-27 05:57:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6599eb74-6eaa-30ef-a198-e4fa587045ff | -4.00011 | -46.96779 | 2025-09-27 05:57:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a9a99f7e-14a5-3860-9a23-caf9ef480a69 | -6.70362 | -42.74808 | 2025-09-27 05:57:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| c80422a9-2a54-3075-909b-8f3ec672baed | -5.4817 | -43.07128 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e6983ef6-f999-3e31-b281-87e2996da71a | -5.50791 | -43.87243 | 2025-09-27 05:57:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4fac116f-eaf7-3114-82ea-5354e9aee354 | -5.73943 | -44.97861 | 2025-09-27 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 490de7a6-ef5a-33eb-9776-d8d14b6757c5 | -4.80242 | -42.81511 | 2025-09-27 05:57:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 2ac550d0-8476-3dea-ac9c-3d7e07dfcb8c | -6.53177 | -43.82728 | 2025-09-27 05:57:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 0e68ceb0-31a1-38e8-85ae-86c66d645daf | -6.8097 | -44.46746 | 2025-09-27 05:57:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 90bf74cc-19be-38c5-a5cb-105266c6c99f | -5.07374 | -44.86186 | 2025-09-27 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 85aa0ec2-416d-3aea-82a6-b588264f0f9f | -5.52127 | -43.87031 | 2025-09-27 05:57:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 057deb97-61dc-3e62-a29a-6cf67e290ea8 | -5.49014 | -43.08463 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 45b27ddd-bf4e-3a58-8f8c-1ccbe1deeb1e | -5.08425 | -44.85374 | 2025-09-27 05:57:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9cf49d03-aeea-355a-9cc3-1c3e784bae60 | -6.70548 | -42.73475 | 2025-09-27 05:57:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c232e4c4-3b00-3ab6-a00c-f6a0d31bdf1e | -6.31749 | -43.45528 | 2025-09-27 05:57:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2750d854-a4e5-3f9c-9dac-f7074c98f23a | -3.44573 | -44.1232 | 2025-09-27 05:57:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b820db3-7136-331a-939a-f7cf48534bfd | -6.69303 | -42.74646 | 2025-09-27 05:57:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5d5bde95-8f5b-30e9-8644-91718b2faa85 | -5.46309 | -43.05637 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 049eca5b-f16d-34b4-ba58-0768d134d98f | -5.47154 | -43.06986 | 2025-09-27 05:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 253.3 |
| 2310aae5-c55a-3b8f-a1c3-98af32549be2 | -5.80652 | -42.81046 | 2025-09-27 05:57:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 3949c1a1-3701-3a44-94b1-5de5c3aceb30 | -6.22151 | -47.32545 | 2025-09-27 05:57:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02f9c53e-cfac-33e4-9cd2-9a0c3422b76b | -4.7922 | -42.81354 | 2025-09-27 05:57:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| fabcd4c4-1bd9-3025-af57-d7e18f896537 | -5.51012 | -43.87954 | 2025-09-27 05:57:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6a0ad5f7-bd34-3369-9c91-4023b59b2bce | -4.59331 | -50.65681 | 2025-09-27 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 16fc585d-e5ba-3213-99e6-f8f829610161 | -5.51164 | -43.86886 | 2025-09-27 05:57:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| c8cd651d-903d-3248-a5f5-62969888385b | -4.00145 | -46.95889 | 2025-09-27 05:57:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 828f76fd-68f4-3e87-8fc1-4fc75921293e | -6.26942 | -44.07074 | 2025-09-27 05:57:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1c7e0604-bf11-3eea-b839-4c4f5fa6c430 | -14.06266 | -48.8157 | 2025-09-27 05:59:00 | AQUA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 859401e4-9bae-3157-95df-1a9cf0747582 | -15.19693 | -48.46643 | 2025-09-27 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 52864fca-850b-3ce5-872c-dedb5a64c5cd | -15.4277 | -48.21666 | 2025-09-27 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9bbf9c88-b53a-350c-b5ef-c2d77eacaade | -15.88948 | -46.19553 | 2025-09-27 05:59:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 83e136b6-55b1-3f45-8daf-a3b9fff9107a | -13.70431 | -47.88975 | 2025-09-27 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eab23ae1-27cb-3ed5-9262-03b69326e5cb | -15.25786 | -51.47125 | 2025-09-27 05:59:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7d57fda6-da2a-3bd8-85ae-f23c9b908ebc | -15.01941 | -46.96713 | 2025-09-27 05:59:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d8528bc-e0c0-31e6-83ac-367e97ea9b3d | -13.78405 | -48.33268 | 2025-09-27 05:59:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 45fa71f2-13f9-343d-8e71-f3806699c268 | -15.26172 | -51.46751 | 2025-09-27 05:59:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3d9a5f15-51ab-3274-98e3-f2c1f25c657d | -15.25992 | -51.47837 | 2025-09-27 05:59:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c13cb49a-d539-3c2e-8d26-eeaad4df53ed | -13.76128 | -47.8707 | 2025-09-27 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 157b1bd1-da08-3d26-9eaa-c39e74404403 | -15.19829 | -48.45737 | 2025-09-27 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2371064f-304a-3385-b84f-3674cdcd203b | -14.06129 | -48.82472 | 2025-09-27 05:59:00 | AQUA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9786e4d1-ba37-34ad-a2f4-896d959e1495 | -15.03927 | -46.94719 | 2025-09-27 05:59:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f1aa6f71-4f5e-3636-8b65-be511023abe0 | -14.6316 | -48.28845 | 2025-09-27 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c4ac490a-3172-37f8-bd3f-a57d7c16c273 | -14.81996 | -45.63507 | 2025-09-27 05:59:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6c1070e0-faf9-301d-8138-ab5f1e8e2d24 | -13.62887 | -48.07551 | 2025-09-27 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 19fb16f0-3c29-3ddf-a3ad-6c85f97ab5f7 | -15.2802 | -46.43285 | 2025-09-27 05:59:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9785861f-63b1-3495-a72d-acf57c3aa7b2 | -15.03788 | -46.95704 | 2025-09-27 05:59:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5cf49c87-d4be-38f3-8f49-5631c9201e56 | -12.29798 | -47.20979 | 2025-09-27 05:59:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9aa40054-f122-37ad-bbda-a55be7bcdfa6 | -12.94844 | -48.9092 | 2025-09-27 05:59:00 | AQUA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9e8952b0-353d-3a8c-8200-ab125921dd37 | -12.64637 | -51.66676 | 2025-09-27 05:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4b01fec5-6270-3e44-84a2-cdfd0ae0d140 | -13.51624 | -47.4047 | 2025-09-27 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| d8f8c8e0-1a97-31d5-bce7-74219fad6db8 | -13.50733 | -47.40345 | 2025-09-27 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b9846d04-bbc8-3d00-b7e0-c9a5e310584a | -7.72155 | -47.30557 | 2025-09-27 05:59:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f5aa380-b2ff-328c-8f95-790736d35400 | -11.34604 | -45.03336 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cd0ea5b1-0c33-3777-a1b7-a15ec9d2aa4a | -11.34754 | -45.02251 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 63ef1533-4747-3c54-904f-bd824c0e0fc2 | -11.9651 | -47.90205 | 2025-09-27 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b9cba159-9747-3829-a885-c888a954a879 | -9.7507 | -46.14531 | 2025-09-27 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 24eb991a-b1af-361f-ba86-32422af379f9 | -11.9739 | -47.90339 | 2025-09-27 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 23c789e1-77c2-35a9-8f57-2ac41944018c | -11.98269 | -47.90474 | 2025-09-27 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 12a8a0de-23ea-3c7f-bf56-e10750be03ff | -11.68876 | -44.40119 | 2025-09-27 05:59:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5e2b8bec-54b7-38c4-bcf4-27cd676b22ca | -9.75208 | -46.13592 | 2025-09-27 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f55af9aa-3e80-31d7-89d5-a4e7a82b500a | -12.64437 | -51.67873 | 2025-09-27 05:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 60ea9635-af8f-38f6-81c9-329c22936a99 | -11.35424 | -45.04539 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9da20d56-e6f1-3e10-b5d0-276a442073c5 | -10.1155 | -45.33581 | 2025-09-27 05:59:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2c381d6-f070-3819-8aee-86a06ace0762 | -13.59699 | -47.30013 | 2025-09-27 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 38a6a7b8-e4d3-3c4d-a0f4-50bb17103869 | -8.8186 | -46.26726 | 2025-09-27 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a90814d6-8d7c-3656-b189-035f5053abff | -11.60739 | -45.41677 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 47086be9-c84f-39a2-b92c-837c08973244 | -12.03488 | -47.05816 | 2025-09-27 05:59:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 46e1c877-1ab1-3f04-bad4-5bf8fda00f58 | -7.81023 | -46.89561 | 2025-09-27 05:59:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README59.md)
