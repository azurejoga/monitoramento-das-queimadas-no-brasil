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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d65fe04-a88c-36c9-81ee-942b353ca31c | -11.4248 | -55.91962 | 2024-12-12 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61562ca3-8812-397a-a7de-1d9c55f699c8 | -13.37545 | -54.24672 | 2024-12-12 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35f5b526-73a3-3309-8d99-3a13396f7e0b | -11.20276 | -53.83578 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e1d4802b-dfd5-34a4-99e8-0a13d14f55e5 | -10.54535 | -44.6806 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 208a4aa4-f769-3d46-ba2a-90cbc2d045cb | -12.41571 | -43.80324 | 2024-12-12 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a42564c4-9152-3660-8210-ea3a0ab988c4 | -12.70779 | -47.63058 | 2024-12-12 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97e06202-a76b-32ae-b6f5-012cc931906b | -11.42277 | -55.91619 | 2024-12-12 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e92c2eda-b480-396a-b899-254a60dcc9e0 | -7.56969 | -49.40185 | 2024-12-12 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50682166-c231-31d6-a930-1d8c628468bd | -13.68931 | -54.76637 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f069422a-e274-39b9-b480-0a6003a69127 | -10.29528 | -53.70112 | 2024-12-12 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8acf5e4-b755-39a2-a518-62b8c36d8602 | -11.42953 | -55.91671 | 2024-12-12 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88c947bc-546a-3f7e-b6ed-481811470d8a | -14.74244 | -52.63703 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16c37bf7-bb82-3f02-bcff-118e39a7a347 | -12.41463 | -43.79966 | 2024-12-12 04:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a81dfb3-4dba-3e6e-a0be-45e5d7c231f9 | -12.04022 | -49.87686 | 2024-12-12 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 248a2988-65a3-3337-8e1c-70babba0aad7 | -12.92643 | -55.05536 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 641c13b8-4180-3336-8eb1-82d08a0784ec | -11.74559 | -43.77067 | 2024-12-12 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b676fe08-c821-3ecd-a2ae-23936acd0445 | -8.73296 | -49.73491 | 2024-12-12 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c87666b-d059-3952-ac8e-a9806f3f8018 | -14.74641 | -52.63393 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9159326e-ee62-3ae2-ac51-bf0c4a7371d0 | -8.36339 | -44.48516 | 2024-12-12 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8905b50c-413a-3900-ba8b-e8ce231bee3c | -11.42686 | -55.91694 | 2024-12-12 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7ea83d6-d1ee-3055-95ae-f2a787a781b6 | -11.42214 | -55.91985 | 2024-12-12 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7def49ae-a283-3991-8424-e959331cc1c3 | -12.75064 | -48.34338 | 2024-12-12 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a8d8cbe-ca47-300a-bbd6-c9e8617661a4 | -10.88121 | -54.32229 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 741201aa-de3c-3bd4-a8a1-6b073f851ce5 | -10.20101 | -36.22231 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 8f9bb0f7-892b-37b2-bbfc-fdf497c51017 | -11.12069 | -45.29254 | 2024-12-12 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4d849d9-dd85-3dca-b891-3216713613de | -12.55422 | -58.35799 | 2024-12-12 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 732741ba-5a1f-323d-b1ea-706a33c18b9c | -11.11777 | -54.65775 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ddaa296-f88f-3348-a558-59217dc1ec6a | -11.21217 | -53.82425 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48bc5f15-cd2e-3ac4-8ece-dccea048e7d3 | -14.75353 | -52.65403 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a558693b-2919-3dae-bcc3-dfcd548e3354 | -14.74956 | -52.65713 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 088a4516-cdec-3f9b-8c13-a36307ec3010 | -21.44504 | -46.6462 | 2024-12-12 04:42:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 57b50bf0-612d-31ed-bcf1-36a0c1f82ce1 | -15.08333 | -59.63047 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af4b84e9-a176-3e59-8c72-1c3790575ba2 | -15.49415 | -50.95371 | 2024-12-12 04:42:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed7e3b0d-f3cc-3713-880b-760e312bb69b | -21.28872 | -49.18079 | 2024-12-12 04:42:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 154fa58d-9311-3c39-889f-a07a9405f91a | -18.05219 | -52.97559 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e57f281b-43ef-3ccd-ba1f-9734c9008f0a | -20.99448 | -51.79362 | 2024-12-12 04:42:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b16b5b7-542b-3643-8434-12701d370c87 | -15.08812 | -59.63811 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34873d14-9b54-3793-aecf-6dbba64ec7c0 | -14.75869 | -52.64359 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cebcc088-60cf-3539-8422-e28e61ae04e7 | -14.74858 | -52.64185 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cfe6fab6-bd5f-3cf1-952c-f2088dd17957 | -15.08225 | -59.63615 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4b08d79-bb1e-3eee-a997-fd80727de169 | -15.08057 | -59.62486 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53fd1ad3-99c5-3e97-b284-a6457f007d90 | -15.08438 | -59.62489 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a1282c4-1e32-373d-9080-229c0f86e045 | -19.02394 | -57.6232 | 2024-12-12 04:42:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2313a211-f6e8-3b77-945f-e0409a89a44e | -18.94101 | -53.69698 | 2024-12-12 04:42:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 187c3729-e12c-340c-9d31-5a6a95ac30b7 | -15.02948 | -57.61422 | 2024-12-12 04:42:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0c8dac8-e65c-3771-9ed0-44619004debf | -15.08324 | -59.63708 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88cae87e-c771-337a-ac7c-fa55db13313f | -14.74918 | -52.63818 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea4f03d9-4599-39e3-a848-69e6862ac2fa | -15.069 | -59.65762 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88f56bff-7378-3fb9-b1d2-4be9ed744ab8 | -14.75195 | -52.64243 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 859a5651-fdf3-376f-8fdd-e679e17fa675 | -14.75413 | -52.65035 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5198e1f2-f108-3e68-aa54-eb6287fe2c95 | -18.04982 | -52.99028 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75fca82f-fbe6-31e4-bdd7-9cc99bd021de | -15.1548 | -51.88007 | 2024-12-12 04:42:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49ee2ed9-4624-3448-95ff-175433e1a6a4 | -15.02342 | -57.61485 | 2024-12-12 04:42:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16e9907d-1767-3ce7-89b9-965bd6eb32b0 | -16.47189 | -54.4646 | 2024-12-12 04:42:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dae14c88-1ee3-3711-a731-e278d43bda47 | -15.09188 | -59.64484 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1dc1830-2b74-382c-aed3-5aab5c5f192e | -14.75293 | -52.65771 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d3061c23-5cbf-3210-bbf3-c7419f8fd65b | -14.74739 | -52.6492 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9acc7d0-6494-37e5-9324-27f029ee78c3 | -14.7557 | -52.66199 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c078d647-0382-35c5-a6cb-b14d969637d6 | -14.74619 | -52.65655 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3ff4571-42b0-385c-b959-2839b3a89a85 | -15.08546 | -59.62582 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a57c2980-7e81-3d8c-bf0c-ef4eae5874e7 | -14.75136 | -52.6461 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acf624ee-33a1-3185-bffc-c426321c5362 | -15.06327 | -59.65575 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae10257f-ae2a-3b8d-ac6d-e2d816cfa886 | -14.75233 | -52.6614 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 24249b89-8f10-3640-852c-7012269fa26e | -15.07736 | -59.63516 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c270dea-60ba-33dd-a8a0-5f9210a5cb5f | -15.06925 | -59.65105 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b634a6-64da-36ef-bea6-8a8e017fe9fd | -18.04432 | -52.98175 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b1aa4eb-d689-3bf3-98b7-bd81e2226d98 | -15.08924 | -59.63245 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae5a25a0-5a93-31c7-bf93-fc750ef03b60 | -15.08436 | -59.63141 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f6e5a78-8728-38b3-83e3-8aa1d609e17b | -15.02673 | -57.60519 | 2024-12-12 04:42:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e7acf2d-93cd-3d3f-abf0-64940f781b31 | -14.75315 | -52.6351 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdb051bd-4c5d-3e19-b2eb-1ea7603d9df6 | -18.53259 | -56.1708 | 2024-12-12 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b79b0a4b-0dda-3202-8425-e405fd835272 | -14.91676 | -52.8749 | 2024-12-12 04:42:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7f20d2d-4926-3b08-a8e6-1f2a961f0d04 | -15.07843 | -59.6295 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fcd07ed-235b-3f77-ac95-82c27791b575 | -18.05041 | -52.98661 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec45f6b1-2ab7-39e6-8d6a-4c251ab2223d | -15.92595 | -59.80959 | 2024-12-12 04:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15316672-a107-30ea-b559-22ad3871678c | -14.74559 | -52.66022 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d667e285-1031-3656-9c0b-a1da1b9cf2b0 | -15.07501 | -59.65297 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb381814-2893-338a-b8cb-050c58882239 | -14.74799 | -52.64551 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b93df6eb-7aca-3cf4-a5c4-f6ee5b78e9ee | -18.04766 | -52.98234 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84622b08-a72c-33aa-9249-f164e84674f3 | -20.72999 | -54.42461 | 2024-12-12 04:42:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f07fdc7-5cfd-310c-828f-ff4957c0c307 | -14.7569 | -52.65459 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3dd7b43-cf62-3d41-bc0a-55d941992213 | -15.08543 | -59.61935 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e9ae1dd-2ce6-351c-bb5f-a97f64ed3482 | -15.06409 | -59.65665 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 506de24b-e0cf-3b9d-ade9-5ee20ba89e51 | -15.07724 | -59.64172 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a04bf3ba-33c1-3596-9727-89106a4374af | -14.74978 | -52.63452 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6437e30b-f967-3d3c-870c-b41a467daf06 | -15.07946 | -59.63043 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f45e21fd-edb3-3cba-830e-2715e45e0f99 | -15.96742 | -57.16128 | 2024-12-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bb75326-427b-3ee9-b648-a1d809865e20 | -14.91615 | -52.87863 | 2024-12-12 04:42:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34472d7e-1f9b-377b-a25d-f5a6d2b0f391 | -14.7575 | -52.65091 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91618ac7-f51f-30ca-82d1-bb37b89d3fc2 | -14.75532 | -52.64301 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 044c5ba9-842c-30d6-b0b8-11f2c8681423 | -15.96813 | -57.16829 | 2024-12-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1693c36-8f20-3c5d-9255-13b70479b832 | -14.74679 | -52.65287 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dabe29c8-c091-3084-ad71-eeac10fe2fb2 | -15.02596 | -57.60929 | 2024-12-12 04:42:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5527515-6c16-3d78-906d-4effc71c927d | -14.74896 | -52.66081 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 354b6ce8-93ec-3e50-9f05-f53ada69fb6b | -17.29572 | -53.77443 | 2024-12-12 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f91dac5-8b8f-37ec-9269-0f1dec182d9f | -17.297 | -53.76674 | 2024-12-12 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aecf6104-871d-36fe-a5c3-8ce3c3a914a9 | -18.04826 | -52.97866 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44f8f716-0337-37e3-b254-0489218e9257 | -17.29914 | -53.77502 | 2024-12-12 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11c5206c-e0c1-3b32-a470-5df77bb97de9 | -17.74503 | -56.32489 | 2024-12-12 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10f8fc77-e587-3452-bb57-e9f96ab4f9fe | -15.0941 | -59.63355 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README27.md)
