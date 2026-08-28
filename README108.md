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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bab74b8-7106-3fb0-ab57-839cba8176e2 | -9.88258 | -45.84635 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2009cbd4-22d0-3f7e-9b40-e8ce9af848bf | -14.43145 | -52.58821 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 16bfbc94-7a4a-3a8d-8e61-10c6dc362bd6 | -10.24425 | -48.45002 | 2026-08-28 17:26:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c95b6700-afe4-34e6-9b8a-acb78178f5b3 | -10.79124 | -53.9688 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 387ee6ad-7525-34bb-9a0f-961b5c886aff | -11.2275 | -53.99048 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 6babf931-6ed2-3aeb-ad04-ca6153d0b2e0 | -10.79245 | -53.97637 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 555ab530-f663-3a13-b7ea-0c87387fd6e5 | -10.53838 | -50.77628 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c213174c-cae2-320e-b895-a531356e9b16 | -9.86228 | -43.61576 | 2026-08-28 17:26:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e1b17fe-76f2-3cfb-ad4e-3a7a1c126feb | -17.5526 | -51.11594 | 2026-08-28 17:26:00 | NPP-375 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c536909b-efcc-3555-a13a-04cd9351f5a0 | -12.0634 | -47.15458 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de61c7ae-005d-3800-8475-32d2f1d4807a | -11.48311 | -46.94333 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2b179c0-8d7d-3e42-b51d-c0ffd2dba278 | -9.86692 | -45.85761 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c59f282d-3064-3de3-bbd3-667661778f43 | -11.22003 | -53.98783 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7a30c34f-aeba-37d6-b899-e20070a0d704 | -9.50648 | -45.65029 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2121aef9-3695-3557-b351-1a0c1f177064 | -11.19909 | -55.0928 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 083370f7-57e8-3ff6-98bf-6f408fa98001 | -11.23033 | -53.98614 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| a95ae1b6-92e9-3b31-9ab8-744d1662445e | -15.47404 | -53.96193 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1cb010f-3c0f-3308-a263-43167457e126 | -15.46512 | -53.97089 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| faaa0fc0-6aa3-38e2-81b5-2beb301340ea | -14.87354 | -52.61992 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4eab3e71-0612-3964-b048-a533fd81986d | -9.87025 | -46.33371 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78eb0082-d8dc-3b73-acaa-9ed4d8536015 | -14.60944 | -53.15319 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c3e7cc9d-f8ba-3843-afba-b82379d2ea22 | -11.24842 | -45.05489 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d80a1f63-eb88-353f-9e0c-aea601858e9e | -11.67378 | -46.72731 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7d78ed5-0129-35f9-92e7-08cd0357fe84 | -9.667 | -45.71593 | 2026-08-28 17:26:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b4eec9e-b458-3bcf-bb1f-abd2db62a068 | -11.23394 | -54.00871 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e5753d5d-606a-3534-80a6-a37eea1b1139 | -9.87003 | -45.83959 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 44e7f98c-d892-3382-94bc-e8137838216c | -10.92069 | -46.62161 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9eb098fa-2b7e-343a-9088-f96082aaa07f | -10.09304 | -46.22901 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 237b90d7-5c54-32c5-ae66-addf854ea2ba | -10.80279 | -53.97467 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 61a89773-7f8f-3023-b312-8480afc422d7 | -13.65949 | -47.74103 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 37f88966-d59d-3e99-85fc-2c59b7a8a16e | -11.17144 | -51.2363 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18aebd7e-37af-39bf-9472-4ddca85c6961 | -12.78102 | -45.94432 | 2026-08-28 17:26:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4318382f-1f2b-30d8-b376-01e17b837c16 | -10.3439 | -50.39366 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6c54436c-21a8-3504-b0e1-bc57abd59c6d | -10.44706 | -43.77077 | 2026-08-28 17:26:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c0d6016a-9a2a-35af-8a40-4003b83398d6 | -10.54618 | -50.41451 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e592ae17-9cfc-3511-9ccd-f4de6a50cfaa | -12.7925 | -46.4551 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71bb2f8d-75fa-3d34-9cec-9d0f095a5771 | -10.34323 | -50.38976 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| df488ae9-9cf4-3e1c-8c19-9885c1298d1a | -17.54536 | -51.11728 | 2026-08-28 17:26:00 | NPP-375 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| ef02294b-69ff-37c0-9c37-822b49ead63c | -11.47103 | -46.94048 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d0bb05a-345c-38e1-8516-19ffe92cf111 | -10.09079 | -46.984 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fabbe761-ce80-3755-af54-c33b5f5ad3ac | -14.51595 | -56.50887 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8154e1b7-6df0-3daa-a8e0-880d38e8bfc5 | -10.17779 | -46.85551 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2378733-0951-3542-b4d1-1bfcd642ac44 | -13.43195 | -51.86353 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 077ac137-f44a-3401-839b-374d02d07cb4 | -16.24201 | -48.3236 | 2026-08-28 17:26:00 | NPP-375 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7f13ab7c-9ef3-36e4-8c9d-a8fcdd5cf897 | -14.24116 | -51.77032 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d0c4b952-3cb3-396b-9d93-c9ec3d886d36 | -14.88248 | -52.63051 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6f3616d3-6ab6-34e2-bb27-7e88cf0b6a87 | -14.33944 | -51.70906 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7a94d7d4-2c6d-374d-88c5-a4ef78680e43 | -14.45003 | -53.383 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a915c8b1-de94-34de-a701-e1d84d23243d | -14.33745 | -47.24995 | 2026-08-28 17:26:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 34ed748d-ff91-35eb-baf1-67b5d8d0fbf8 | -12.91009 | -59.88279 | 2026-08-28 17:26:00 | NPP-375 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78e3b3d7-8a68-3f21-962e-9e9ab9bc30ca | -13.32019 | -48.19617 | 2026-08-28 17:26:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 92ef76b6-2ea0-3aff-80e5-86fd64c282af | -11.83872 | -47.20776 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3c9f660e-0f2f-369a-8273-03267f2a8b61 | -11.27706 | -54.0364 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0dcc1204-3ed2-34d9-b90f-d44719752a5f | -14.33534 | -47.2391 | 2026-08-28 17:26:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 31669558-762f-382a-9276-d759001024a3 | -11.00525 | -49.63485 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| be1613bf-6003-3805-b16c-85709ea48d71 | -13.42544 | -51.76583 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f5bf5fad-d754-3193-809e-1c032ca70f31 | -13.429 | -51.86856 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 23f6f306-3c78-35c5-b94f-daa87d2e0d3a | -14.61226 | -53.14881 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aea51010-77ff-3397-b3e6-81b6a50c6678 | -12.22488 | -50.54553 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b44f7eb0-5b09-3189-b846-62a49914102d | -11.79288 | -47.65783 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 2c1b06d4-61c5-3787-87ef-8cf284ac9550 | -14.18578 | -52.83055 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 08263c3f-83ad-3383-86ec-3e343f88dd28 | -14.56884 | -52.07249 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8032067b-c1c9-3623-8be4-b195d21251ba | -16.39528 | -48.0309 | 2026-08-28 17:26:00 | NPP-375 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dab3c677-06b2-38ab-9125-4cdc362958d8 | -11.24193 | -45.06502 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7415839b-72d8-38e7-b6d7-49e7fe11f407 | -13.65573 | -47.74714 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 46c82717-e135-37bd-8ce2-58c670bec63e | -14.15503 | -52.83977 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dbb22fca-d5f9-3f85-b063-e50a90f1360a | -15.86348 | -41.96494 | 2026-08-28 17:26:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f20abcc2-5f2a-38e9-8c82-3ccf6d2ec7b3 | -15.72816 | -51.18163 | 2026-08-28 17:26:00 | NPP-375 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2507fb2e-463e-34d0-8a1d-085981ff385a | -10.02801 | -45.82427 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f6e74f85-08b1-3b78-9bf9-fc0b877ea820 | -11.22588 | -54.00235 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| fa2616d1-facf-305e-8224-38e791a736f9 | -11.02211 | -49.68003 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7bd5142a-b6cf-3d8c-b31c-db9ef1a9a756 | -13.5844 | -45.78323 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5a4ebf03-4fd9-305d-a4f0-00b1573096c7 | -14.18965 | -52.85419 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1615cc34-f725-38c5-9c25-bb149a79c967 | -14.54526 | -53.30098 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e76ef5d2-d9c0-32cf-9af7-3baefe149b94 | -10.79306 | -53.98017 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a39e15b1-e3cd-3481-b2be-77618d6a58bc | -12.20129 | -50.55339 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a4c5f59-87ab-39ca-a893-b43d78c79b35 | -11.19686 | -55.10047 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 703c03b5-70ef-3c89-bfe5-d3de745ca708 | -13.33127 | -46.92467 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4ccf4bd5-c747-3924-b90b-10d52ce17e46 | -16.24274 | -48.32758 | 2026-08-28 17:26:00 | NPP-375 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6359e48-1854-3770-a2c3-f50b6619a4c4 | -10.75924 | -50.6408 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d4fcbd6e-0fdb-3552-8363-9f5da17cff7d | -14.29139 | -49.39003 | 2026-08-28 17:26:00 | NPP-375 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 27c6e15b-2e0f-311d-b05e-6369067fb83d | -14.87898 | -52.63108 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7cdd9205-d85f-3fa7-90d2-d7169e37b104 | -10.8034 | -53.97847 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 381c94f4-a802-33f4-886b-4dcdc4ddf75d | -10.2952 | -49.95499 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0f68cdd6-ac83-3743-a34b-fc218798aa9e | -12.27959 | -59.32986 | 2026-08-28 17:26:00 | NPP-375 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c51584cf-a4d0-322a-9398-7f0fb7d2855c | -11.85844 | -51.67327 | 2026-08-28 17:26:00 | NPP-375 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4ab911bd-fe14-3794-9254-9c7fae42ce44 | -11.6244 | -54.57662 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f4726ee5-08e0-3744-9017-cc95d9e0802f | -11.22245 | -54.00291 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f787e03b-09fb-3146-9a12-64834d061002 | -12.69 | -48.42796 | 2026-08-28 17:26:00 | NPP-375 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6096ef62-657c-329d-a4c0-a5e10ff2bf7b | -11.83239 | -50.0714 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 29e8eae5-35eb-3085-93ac-67b39c96c4fb | -15.99727 | -54.92484 | 2026-08-28 17:26:00 | NPP-375 | SÃO PEDRO DA CIPA | MATO GROSSO | Brasil | 5107404 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4154d98-0f3c-3c01-a9e5-bc3cc05137b2 | -16.58205 | -49.78081 | 2026-08-28 17:26:00 | NPP-375 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 3b942f99-3b18-30be-8a4b-187a30b789e6 | -14.17596 | -52.83626 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 3ffd65fe-9b75-3f93-af36-00cb3d99ff23 | -12.38422 | -48.20144 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| e7bf5f0f-e8df-338d-a808-74bfc6078646 | -13.5952 | -45.78132 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e14256d-f161-38cd-9bcb-00966ba7ec1b | -10.76898 | -50.62389 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| da72f343-ab83-3a17-baa4-937e97b95ae9 | -15.63734 | -45.92038 | 2026-08-28 17:26:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1ef7e8a-f7e1-38d0-9106-734cb1bcc7c2 | -14.24388 | -44.43501 | 2026-08-28 17:26:00 | NPP-375 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b0c8302b-8b3c-34de-b868-4497c309d2bf | -9.66795 | -45.12672 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d8ecc6d-7923-3871-b1cf-30ce86d91e94 | -13.83394 | -54.04831 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README109.md)
