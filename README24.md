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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bebce8b-7bf5-3565-ae2a-596b97da0aa4 | -2.56037 | -47.28299 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 511b409e-e122-345e-8099-8adda0467f17 | -2.55981 | -47.2783 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab64bd1b-12fa-3044-986c-4d9c24d68f64 | -2.55918 | -47.282 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 291deee6-f86f-3aef-88b9-c05f5e789f13 | -2.52991 | -47.22487 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f53b282-8d0c-3045-b84c-1a7289ecd0af | -2.25459 | -46.8701 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7331cbc0-fa67-36e5-a606-4e51db5be822 | -2.25401 | -46.87364 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf758e09-d58d-3ad5-b4d2-39a598dff129 | -2.08102 | -47.13359 | 2024-11-03 03:53:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbf5d26e-98cd-3de1-a86c-2efd0d1e219c | -4.50792 | -46.62396 | 2024-11-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12931009-e47d-33bc-9a93-3e6b10e9fb4f | -4.50743 | -46.62691 | 2024-11-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d8a87fa-e930-3176-b470-f91bb8f32d64 | -4.26713 | -47.06304 | 2024-11-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92f01bc0-c701-3b4b-a7f2-e8f3a90fa1c2 | -4.26653 | -47.06654 | 2024-11-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09c0859d-7ed9-31d5-a06b-1160317dc365 | -4.111 | -46.16571 | 2024-11-03 03:53:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d02d290e-42a0-3702-a192-cf011db88595 | -4.11051 | -46.16862 | 2024-11-03 03:53:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e247834b-bd2c-39f9-9445-8d4b333e22ca | -4.05092 | -46.93877 | 2024-11-03 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e712cd0a-5f2e-3695-ab35-9dd53fdbed7e | -4.03815 | -47.14289 | 2024-11-03 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d214bd36-2e40-3ac3-be75-03bed0988b1a | -4.03756 | -47.14631 | 2024-11-03 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c23d82eb-929b-35a4-81e7-21944417370e | -4.03275 | -47.14202 | 2024-11-03 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3744d2e-cd04-31d7-95ad-c0df9d1aa1dd | -3.61724 | -47.52604 | 2024-11-03 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57cfa099-b77f-3c14-abb8-3a9441d7d371 | -3.61662 | -47.52982 | 2024-11-03 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e1a18f6-3a90-3d1a-bc53-5636168a51f6 | -5.2942 | -47.38856 | 2024-11-03 03:53:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f7e73c9-6847-3c04-af2c-7f29bd3f0934 | -5.22479 | -47.45546 | 2024-11-03 03:53:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62e083d7-a11d-3539-9d00-892a31f13703 | -5.22213 | -47.45212 | 2024-11-03 03:53:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d51dd7e7-c717-336e-baeb-45dc829a9c3a | -5.22155 | -47.45539 | 2024-11-03 03:53:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4263403e-c283-3908-87c7-02b267a010ba | -5.21947 | -47.45403 | 2024-11-03 03:53:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b499f85-7d86-30b8-8f1b-5c4c29a917db | -5.2189 | -47.45737 | 2024-11-03 03:53:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d47023c3-a898-3bc0-b8d0-d14cf3a44488 | -9.33358 | -47.83438 | 2024-11-03 03:53:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 495d0ccb-694a-36d1-bf55-eba903c7706e | -9.33302 | -47.83744 | 2024-11-03 03:53:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e731e99-02e3-3dd2-8b2d-5a24e292ed0c | -8.83857 | -47.72955 | 2024-11-03 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1974ab97-d8b2-3b4f-9467-cf3c924f9829 | -8.83799 | -47.73278 | 2024-11-03 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4654dcb5-dfb4-33d8-80ed-eece7f09c4b7 | -8.64868 | -47.8266 | 2024-11-03 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f1766a6-3b42-34ef-96e2-7c4a5383a0f2 | -8.64809 | -47.82982 | 2024-11-03 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 225b30ea-e2dd-3e1b-8652-ea25cb156bec | -8.6475 | -47.83304 | 2024-11-03 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12cde474-c39d-3c06-bd35-7a888cbd2ac8 | -11.81697 | -48.76453 | 2024-11-03 03:53:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 267597f4-9c8d-3d6f-abde-3fd51f08ac37 | -11.81633 | -48.76785 | 2024-11-03 03:53:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bdbce3f-f112-3d89-aab7-6649f21312c3 | -11.81565 | -48.07384 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b08af269-705f-3fe8-8799-9ffe6d3ae575 | -11.81502 | -48.07393 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fd31408-12f3-3394-a697-629e3d3c1e6c | -11.81445 | -48.07691 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70acab57-295c-3405-b9fd-2fa588edde14 | -11.81009 | -48.07584 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93a69ea6-1a3e-3431-a9db-a7112aead3f4 | -11.80954 | -48.07883 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16cadc74-5530-3e3e-bb1b-ee854b0f89b3 | -11.80898 | -48.08184 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b02a566-cb1c-3cad-8998-b945012a575c | -11.80452 | -48.07787 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67bb84fc-0092-3ef6-8ded-4b5262e18295 | -11.80397 | -48.08086 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f857aa94-d78e-3046-ad11-d68e4053c4b1 | -11.80341 | -48.08385 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2859e418-4e76-3b13-affb-04c3275c66e3 | -11.7995 | -48.07693 | 2024-11-03 03:53:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 478fe5e0-3e9f-33f2-8cf5-3f1052a0d5ed | -0.63235 | -47.68319 | 2024-11-03 03:53:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb9a21b8-5436-3455-be88-c5c1444b4504 | -0.63167 | -47.68744 | 2024-11-03 03:53:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2df99f6c-57f6-3ce3-9cd5-5a9f00eb25bc | -2.08284 | -48.29819 | 2024-11-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f0acfaed-096d-3e13-a992-48d0609d5f16 | -2.08022 | -48.29872 | 2024-11-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2e65bfb9-017f-397a-9957-b1e315e80a06 | -2.07685 | -48.29721 | 2024-11-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 33fc4031-c84f-332c-84e9-566a97632222 | -1.98875 | -48.12762 | 2024-11-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aa34772c-8b27-31c0-b034-54267535c3b8 | -1.98645 | -48.12505 | 2024-11-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bf608538-ba33-3f09-8d05-0f23beccb737 | -1.54482 | -47.7423 | 2024-11-03 03:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0d8de0-4219-3c18-b26d-c9991e82d8bb | -1.53936 | -47.74192 | 2024-11-03 03:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 477c3789-5907-39c8-a7aa-cd5f9219bd1e | -1.53898 | -47.74139 | 2024-11-03 03:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac15a65-417a-3058-a61f-f142c6ae54bb | -1.27833 | -48.13263 | 2024-11-03 03:53:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41f54604-5199-313e-9afe-f26790cdc549 | -1.48556 | -47.2229 | 2024-11-03 03:53:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68cf4406-ee6a-3200-8f15-a578de1020f3 | -3.45739 | -47.66904 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbc97005-6f40-37aa-bff2-006d0f61d9a5 | -3.45674 | -47.67297 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48c3326b-e6cb-3f86-bb96-75bca0670095 | -3.45107 | -47.67226 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 005110b4-222e-340d-95af-fc242bdc3bb3 | -3.07177 | -47.57915 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 729833d3-4145-395d-b5aa-7323a975583e | -3.07115 | -47.58299 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ceb49d2-a36c-393b-8b6a-91ccab5c108f | -3.06868 | -47.58264 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93d58eb9-2816-3e58-9844-c1e9ce73034c | -3.06549 | -47.58218 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df99040c-23bb-390f-af63-3c46d09f58dc | -2.47111 | -48.04615 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fab66d08-5548-3a51-ba12-79a477ce08c7 | -2.4704 | -48.05035 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b533f57-e5a2-36ce-83ab-6a71041f5f68 | -2.46969 | -48.05455 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a1ad524-7165-3b41-ae1a-b0e462e29ca0 | -2.46452 | -48.04949 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7064895-e096-35e0-baaf-df1723452cb8 | -2.46381 | -48.05368 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d99c9648-24b2-3bf0-8a68-3880e7cb908a | -2.45936 | -48.4957 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39d2c846-f9e1-3a7f-9757-d1d13d5d558a | -2.45744 | -48.49633 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 480446ba-2e57-3152-a0d2-4ef99fc45b71 | -2.41483 | -48.86621 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61042a18-755f-3e55-8edf-ccc2c8924a55 | -2.41006 | -48.86201 | 2024-11-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3743d88d-1021-3c66-a82c-41949fc055d6 | -2.40928 | -48.86678 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6effce37-c6b5-3fe6-85ec-21cdddff7303 | -2.40866 | -48.86514 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae1e7145-6022-3e24-9fd8-db2634f46664 | -2.40611 | -48.58114 | 2024-11-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5a30efd-4b27-3a6a-99f1-e4f29a3bbe63 | -2.28733 | -48.80481 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0f84a704-bc71-38e5-954f-196477c19f45 | -2.28654 | -48.80962 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8b03eff1-8917-3321-813d-486882ea7229 | -2.2569 | -48.26434 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb59b01c-3568-3e77-9ed0-86d3f408a837 | -2.25619 | -48.26858 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 275b196e-ea03-380d-9343-267b3c1e6949 | -2.21197 | -48.1675 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 993df02f-69e6-3c1f-920d-22e09abae461 | -2.21122 | -48.17194 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d11f9ef-d625-3647-b0e6-0edd20cdae27 | -2.20865 | -48.16682 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 08270040-8e31-3ec1-a107-cbb0bafed39a | -2.20792 | -48.1713 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aea20173-6c15-3b47-8b0e-0bd4052aedbb | -2.20722 | -48.17562 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 585e0743-036d-3b0a-8f1a-757b5b0f7b9f | -2.20681 | -48.16196 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f6e19bd-5212-3b00-93ef-377f78022915 | -2.20606 | -48.16642 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76848503-7cdd-3713-9968-64e9cf52592b | -2.2053 | -48.17093 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 674bfc80-c3fe-30a7-9bf1-014b4b2238ad | -2.20456 | -48.17523 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| faa25422-5001-3cf4-b987-0debfbf89ac5 | -3.15152 | -48.56948 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d7887929-d4dd-3c61-b603-1b78f0b0a80d | -3.15076 | -48.57394 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1c456199-e884-3ed5-8e81-34639877b2ba | -3.14552 | -48.56848 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b5d3523e-165a-3e4c-90c9-ddc96dc5c5ca | -3.14477 | -48.5729 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| efa494b6-386e-37ca-a943-03ae3ebf2156 | -3.06293 | -48.00057 | 2024-11-03 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f3c53c4-fa13-3cea-94bd-f96d0fc7c72c | -3.06225 | -48.00463 | 2024-11-03 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9f8865f0-1457-3fc6-b7db-5ab58bd091dc | -3.03255 | -48.07529 | 2024-11-03 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cc0cfcd-408a-3e12-848f-818290c26de7 | -3.03188 | -48.0793 | 2024-11-03 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 288ac164-a8da-3e28-81e9-90893cf3caf1 | -2.92308 | -48.61677 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c9288c7-d89a-356c-8523-c6b6dc340621 | -2.90421 | -48.61824 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f49f1d3-481c-3b69-9903-23cca8636f76 | -2.90342 | -48.62291 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ad5588-34d7-3a6c-a2cb-61586461c8c0 | -2.90262 | -48.62759 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
