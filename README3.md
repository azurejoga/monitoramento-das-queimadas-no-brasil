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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b6b54d3-8868-37d3-9926-a705566ec1cb | -13.95546 | -47.54316 | 2026-05-07 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75564b0f-0d0a-3b81-97a2-a967a4c41c71 | -21.35636 | -45.13856 | 2026-05-07 03:47:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7eb053ce-edd3-3d76-a7c7-1d9b33891aef | -10.55644 | -42.43376 | 2026-05-07 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4a8701c3-ce27-3c62-aae2-286850ed4410 | -14.12116 | -45.35045 | 2026-05-07 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdb6676a-2dd3-355f-818a-02b6a7ca0a08 | -20.2257 | -46.84821 | 2026-05-07 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bd59216-1737-3a96-8d2e-72a482137a37 | -22.74322 | -48.21034 | 2026-05-07 03:49:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7e1ab60-260d-3aec-9ea6-6147d73c5fab | -23.32695 | -48.86488 | 2026-05-07 03:49:00 | NOAA-20 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad64e900-8fd2-3a12-abda-aee3470b49e6 | -21.70417 | -48.41977 | 2026-05-07 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f281458-7235-3533-bed3-f45c44443f47 | -22.74252 | -48.2136 | 2026-05-07 03:49:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a41d4a5-91d7-335e-8a3d-864368858fda | -22.97234 | -52.69195 | 2026-05-07 03:49:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1c697d7a-88b7-3ff2-9625-0aabf47eac91 | -22.70018 | -43.35996 | 2026-05-07 03:49:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d14e8a63-3fb5-3692-96a4-6c58d29f355a | -22.74181 | -48.21689 | 2026-05-07 03:49:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 46f82bf9-352d-3a46-a546-34910f3ff587 | -22.00775 | -48.42873 | 2026-05-07 03:49:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25e2d953-b8b6-33d9-a9d8-a61e6a2695eb | -21.69968 | -48.41515 | 2026-05-07 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a11660b8-e312-3c53-b330-6fe8eabf2379 | -21.70345 | -48.42307 | 2026-05-07 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bad3bad4-d7ab-3ee3-92f1-65c2ce67f160 | -22.0085 | -48.42532 | 2026-05-07 03:49:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b89b7a6-9d8e-3b98-baba-9bb2c394bd1c | -21.69897 | -48.41843 | 2026-05-07 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 47318aac-f160-3edb-9111-d501987f6faa | -22.60975 | -47.22766 | 2026-05-07 03:49:00 | NOAA-20 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dffd045-584b-3e99-ac3b-20d13b6da191 | -22.97091 | -52.69767 | 2026-05-07 03:49:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| adaf6657-7d68-3500-b565-a4efca41a0aa | -21.70489 | -48.41648 | 2026-05-07 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 369f532e-4a8d-393f-9388-c831b2b56a93 | -10.55907 | -42.43599 | 2026-05-07 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 156d3c32-c013-3900-8c72-bc4ca6c50913 | -5.78161 | -45.12179 | 2026-05-07 04:34:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7d42a78-e6d2-3bb6-a5af-9a548bbc3eb7 | -6.31885 | -44.6344 | 2026-05-07 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e0a48a1-ef06-3421-92c0-9f8f4cc1d76f | -10.23898 | -52.2313 | 2026-05-07 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06590acc-9710-30f9-aab8-ddb25a036f11 | -11.61264 | -48.05483 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f73ad8c-0f0f-393a-9f1b-1f98067ce7c8 | -12.34441 | -50.01355 | 2026-05-07 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e596f04e-f8c4-339c-a0a7-af8a89a28528 | -5.77812 | -45.12123 | 2026-05-07 04:34:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa70400-e59b-3a99-8160-e91f9b141123 | -9.46986 | -47.80118 | 2026-05-07 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad5ea1e5-7368-32a9-a5da-a0ee246c8b7e | -8.30709 | -45.39395 | 2026-05-07 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 522ac14f-f6d6-380b-abd3-446a3d77ebea | -12.35156 | -50.03306 | 2026-05-07 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d449ad3f-1f63-33e6-a011-3baa0a555ae9 | -11.60931 | -48.05431 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e9b2eb6-ec09-3ebd-8c22-9db0561c23e3 | -8.31414 | -45.39523 | 2026-05-07 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 981c8815-86a9-3a75-bfc1-eef7c9b86fec | -7.15418 | -48.23856 | 2026-05-07 04:34:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2e9b42-da38-3ef2-a754-b891daecef09 | -8.6284 | -49.5413 | 2026-05-07 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beefe741-25c5-3691-b3c5-aa79bbf67f3e | -10.2353 | -52.2307 | 2026-05-07 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f7c1ec9-38a2-3051-bb27-bf0cfdaa4a8f | -10.24266 | -52.23194 | 2026-05-07 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb12bddd-0293-3c55-bc78-d6d45cace958 | -11.6193 | -48.0559 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf9f3342-732f-3172-90bc-79ceec490712 | -10.92349 | -55.14318 | 2026-05-07 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94311cae-8541-36cc-8d1d-4623f64f5450 | -8.68021 | -49.09034 | 2026-05-07 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90e597ea-9880-3b8d-89d9-91a4c9021217 | -8.74795 | -50.23496 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| becc0041-0f84-3d48-bd68-6da7fc334c18 | -7.27637 | -46.79286 | 2026-05-07 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a7b35cf-8db9-3fa7-909a-939517d98e98 | -8.31002 | -45.39862 | 2026-05-07 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49c47510-6f5f-3ba6-a777-442085d10069 | -12.27671 | -43.55266 | 2026-05-07 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bc1f99f-7f80-38eb-a654-efe35ba838dd | -11.61984 | -48.05234 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6c5ddc6-2634-3413-85e9-4085d1ca3c3c | -12.34774 | -50.01409 | 2026-05-07 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7001aa59-74f9-3d4a-b5c4-bae6b6c3786b | -7.15364 | -48.24203 | 2026-05-07 04:34:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c27d08c-c11f-3c93-9338-14532e76e8bf | -6.33383 | -44.63258 | 2026-05-07 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47acee25-7924-363c-9830-4cf1f8c79410 | -11.60544 | -48.05733 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d422a66d-41d3-36e7-98d7-0205f761b746 | -11.94637 | -43.38247 | 2026-05-07 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3330b23-208b-35c5-bed2-7e8683df14f7 | -8.81226 | -49.94561 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd2d961c-5771-3320-ada7-97da3345877c | -8.63118 | -49.54542 | 2026-05-07 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19bad0bb-bfd3-318c-875f-0e270954b9a7 | -10.55373 | -42.43332 | 2026-05-07 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69bb7841-49f7-3789-86ce-d0350b21c23f | -9.40528 | -50.68996 | 2026-05-07 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb10cfa9-b579-3860-a4f8-8acbb1a2b048 | -11.43896 | -55.10147 | 2026-05-07 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d36549d-a6a6-30ab-84b8-e508401d289c | -12.86351 | -43.75151 | 2026-05-07 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa554049-4913-3e55-8fe0-1e3d1b43b61c | -11.60598 | -48.05377 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11bbd564-4a6d-3aba-b77d-db8c16651aff | -10.4848 | -49.36025 | 2026-05-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c4406a1-af28-3b81-817c-92154daefc43 | -10.63801 | -48.00705 | 2026-05-07 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 203d28b2-b195-3cfa-aa22-78f872966108 | -11.61597 | -48.05536 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1df4236-2943-3005-9dbb-b42504a9b0e2 | -12.75658 | -46.96581 | 2026-05-07 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 354c609d-c0ce-395d-a515-93c654d6f687 | -8.81167 | -49.94927 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 54f78bfb-a300-3a50-b42f-6826698911ae | -8.84337 | -36.55631 | 2026-05-07 04:34:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9b521258-c9ba-3b70-aa5c-9e39df5db043 | -12.75714 | -46.96197 | 2026-05-07 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2b1da2b-162a-3bc7-adb3-c5ad4fae2f41 | -9.46655 | -47.80066 | 2026-05-07 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 172718b1-fd81-39bc-a851-e49b5f32ec69 | -6.32306 | -44.63089 | 2026-05-07 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbc47158-c7a2-3e40-8c15-5b3456ff04b3 | -6.4341 | -44.21682 | 2026-05-07 04:34:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 576de9df-416f-349d-8229-4e627404e083 | -6.1066 | -44.74623 | 2026-05-07 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59813818-7ea8-3182-9be0-1321bb5aeb7c | -9.40402 | -48.42307 | 2026-05-07 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c705ec75-4545-3bce-bfdb-426315747e08 | -9.25946 | -49.25595 | 2026-05-07 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e6bacf3-1103-3dc3-a1d8-0c1b2dc60863 | -11.61651 | -48.05181 | 2026-05-07 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ef71f20-2bcc-3ec3-80cc-07445cabf7c3 | -12.4155 | -49.67165 | 2026-05-07 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 108fbb31-2a33-344c-9789-4985e23b7b6d | -10.02534 | -50.74233 | 2026-05-07 04:34:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a381db08-c8e5-3a50-a851-18f610c664c1 | -8.69296 | -49.09596 | 2026-05-07 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d95c0a8-b2dd-3936-b501-2b558b212f70 | -10.55528 | -42.43108 | 2026-05-07 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d98d57e4-6a69-3229-abef-85a6b58449f6 | -5.78044 | -45.12954 | 2026-05-07 04:34:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e4dd025-af9b-34fc-93c9-0cad340d8fa2 | -9.40652 | -50.68228 | 2026-05-07 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60daf643-2722-312b-9189-b639a1e42613 | -11.57726 | -54.56402 | 2026-05-07 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4b7370e-0e9c-3ef4-8f1c-31cb0006e566 | -8.72867 | -47.97749 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba548d03-9d26-35fb-92a5-0d95951c79d9 | -12.85427 | -43.75789 | 2026-05-07 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bc49f2b-cbbe-3646-8f31-c5db8da38110 | -6.10592 | -44.74541 | 2026-05-07 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c3e70fd-1a91-3445-9f3a-e993181376bd | -12.41219 | -49.67111 | 2026-05-07 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b2de316-d322-30bf-95fd-c7b6dd7f217c | -8.17035 | -46.88267 | 2026-05-07 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a52b5b1-f705-3fc9-8635-86b47e15df4a | -8.72814 | -47.98097 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e65bd7e-82cb-3fc0-b713-8dc9e45c1778 | -12.86301 | -43.75531 | 2026-05-07 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dad988c3-2574-3e8a-887b-c50af94fc3ea | -12.34717 | -50.01767 | 2026-05-07 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56de1416-a89b-380e-8423-6aef0b3040b4 | -12.35213 | -50.02949 | 2026-05-07 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4928641b-4c4a-367e-b918-1d194c335ed7 | -8.80888 | -49.94506 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e5a863d-70c7-37d0-a7d1-9d216f630e15 | -8.72483 | -47.98045 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ce28ffb-2d0d-3f26-96b9-b1bc51d54be5 | -10.48812 | -49.36078 | 2026-05-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9e720d1-99e7-389b-b197-f51a83536f85 | -8.7276 | -47.98444 | 2026-05-07 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39d993ed-b63f-36e1-93ab-f00458c270f8 | -11.94687 | -43.37869 | 2026-05-07 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25cbd618-03d7-317a-867c-cb84634141bd | -8.5372 | -39.56805 | 2026-05-07 04:34:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a77ad714-93f4-300a-b280-40f9cb4e497d | -12.85839 | -43.7585 | 2026-05-07 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 634c7f4e-3f9a-3735-9d5c-ab86788a76fa | -6.45601 | -47.85194 | 2026-05-07 04:34:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61e75b11-83a9-3d9b-a1db-f96420e3e7b8 | -5.77753 | -45.1251 | 2026-05-07 04:34:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 935ceab4-c9f7-3437-bb17-e89e698d5e22 | -11.48148 | -52.91944 | 2026-05-07 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecc26cde-4973-393e-b58f-ab24955716ac | -8.63175 | -49.54184 | 2026-05-07 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6facaed7-3bc5-31e3-ba65-80be135a118f | -8.68354 | -49.09087 | 2026-05-07 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64a37a44-912c-3e12-803b-9483fd014224 | -12.28085 | -43.55325 | 2026-05-07 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5dc0388-768f-37e1-8852-0542bb7ac724 | -8.98125 | -48.0817 | 2026-05-07 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
