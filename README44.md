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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85180b27-ec5a-3f54-aec6-59e35a59bcb0 | -9.53582 | -47.78127 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c77c0ce-a339-3d0f-8036-8a93a766b7db | -9.53531 | -47.78497 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 242f5691-a674-3bc9-b5b8-52fe93db3f59 | -9.53335 | -47.78147 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 340a3ae0-5aa5-3aac-b77e-a28e045f4cd3 | -9.53282 | -47.78515 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e20029e4-8171-37be-8d7a-a7fc6ea659c9 | -9.53119 | -47.78433 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33d63334-5fb1-3da5-af63-704cb222f382 | -9.5287 | -47.78453 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f270c015-040c-3388-a9ed-21620d079025 | -9.52816 | -47.78823 | 2024-09-29 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85f019fc-dbc9-34ba-844a-99a07b732508 | -9.50309 | -48.53648 | 2024-09-29 04:49:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 150157e2-acf9-32eb-8777-c5f593e792f0 | -9.49916 | -48.53593 | 2024-09-29 04:49:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5b604e04-4a42-35cd-8f0f-6dac769fd23a | -10.23972 | -47.76593 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bf33174-e968-37ed-a967-eb7f5eb03ad9 | -10.23921 | -47.76955 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21a3a9fa-afc5-3a0a-8da6-14e6ce1c9bde | -10.75357 | -48.74349 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0562f962-044f-3966-bb5f-cde14739ea8a | -10.74962 | -48.74295 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2814686b-3f97-3d16-8594-f10530ae7982 | -10.745 | -48.74719 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cc67a65-cc77-3a1f-8e9d-3617fcccac8b | -10.74106 | -48.74657 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05585553-f6f0-397d-a052-19f2a29268b3 | -10.73712 | -48.74598 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98a8f6c8-89ab-347a-b7ad-b335b70cb819 | -10.73648 | -48.75053 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 186db391-b5f6-38c7-bed0-d3b5860bf63c | -10.73252 | -48.75002 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03401a2d-8453-3043-9b4d-5fec5555db07 | -10.72857 | -48.7495 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3752ece-2154-3da6-b4c5-bd1b335e6a0c | -10.72792 | -48.75416 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a75b914-1f31-30c7-8b35-eb6a8147fbeb | -10.7221 | -48.73822 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89d19a7d-09a8-380b-b127-f76666021217 | -10.72141 | -48.74319 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37746b56-5daa-30d6-8354-7c0b69b78fa5 | -10.7175 | -48.74239 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f97ad7e3-8905-3acd-ac37-52de0707ef2b | -10.55216 | -48.05552 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07178df0-4b13-3ccf-8dac-54d2e642af91 | -10.54907 | -48.04774 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa76142d-bba0-3846-aeb1-f1a0630d3196 | -10.54851 | -48.05165 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 139553c2-e1e1-3435-b55e-29c875eeb172 | -10.53608 | -48.02069 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0497d5e-b282-3d5a-ae93-2fb07cd691fb | -10.53396 | -48.03579 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab5cbba3-e552-3888-88ba-c2a4b7f62bf9 | -10.53343 | -48.03954 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5116f38c-1b2d-3706-8896-2dce3b654196 | -10.53195 | -48.02017 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c72eb2a-2c42-3933-8982-b8f1b9ff8d6d | -10.53139 | -48.02414 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f471d4d3-4f19-393c-93d1-297ad90ef63e | -10.53083 | -48.0281 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 072d9f5d-be04-3be7-b4b5-14223ed06fe7 | -10.5303 | -48.03189 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 89e1e3c8-8b3c-3f26-9516-5ed8b977a91d | -10.52978 | -48.03561 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2dd87e0-c2d4-3a79-bd2d-0e72d36d14a0 | -10.52565 | -48.03511 | 2024-09-29 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 867e9131-c768-3e4a-9a7c-736a86d21fd5 | -10.44023 | -48.19965 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 983c4186-89b0-3273-ac2e-27c9a4b1293f | -10.43573 | -48.20212 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d57eeb02-ff65-3eb0-96db-36d577c58793 | -10.43169 | -48.20135 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdced3fa-02f1-34fa-a6d9-7800049f5999 | -10.42507 | -48.18959 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f65a6eec-b704-3572-8e92-fd0c45b05a78 | -10.42256 | -48.17801 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4932a398-3083-3eb2-ac67-085af305cadc | -10.42205 | -48.18161 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac746bd8-7115-36ac-a8d5-372319831c2f | -10.42156 | -48.18503 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fad4426-6447-372c-8bd0-4c20a320f7e9 | -10.42108 | -48.18844 | 2024-09-29 04:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e161193-a0d2-3baa-b78a-c98b2423513b | -11.19924 | -47.71532 | 2024-09-29 04:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f878fae3-d99e-3297-8475-7f0f3cd38597 | -4.91928 | -48.61219 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9aebf8ff-7879-38d6-88bd-f6cddf258b52 | -4.91862 | -48.61653 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 828ec31a-db8f-3b67-9c59-58221226d636 | -4.91797 | -48.62085 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de286136-ab7d-3a70-bad3-ce3524a662e4 | -4.91559 | -48.61167 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8b5e7c1-a63e-3d25-b66b-d463f87526cf | -4.91493 | -48.616 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 110efb26-7ae0-3555-8eb9-394e6049310a | -4.91428 | -48.62031 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20643b39-d885-37aa-adb1-0b53d55129d4 | -4.9119 | -48.61114 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9608854b-cb3b-3bf2-b6f3-b0bf1ede042d | -4.91125 | -48.61547 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c39736b9-1a4a-3cd1-8e3b-ac49a7270365 | -4.82597 | -48.53824 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e50cc14-bd53-35e1-bde9-dda34aac6f20 | -4.82284 | -48.09791 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a3216f-d31b-335d-950a-f54594e4b8f6 | -4.63249 | -48.53398 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79cae24f-9f53-3fc9-9f48-582075d0a905 | -4.63184 | -48.53829 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30ed02b9-c35c-30bf-b9bc-d5eace3cf9ca | -4.5776 | -48.00529 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 804522f2-afdc-33af-afea-00db3e385a9e | -4.49179 | -48.11226 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 070fdfb5-2167-31ca-b989-998d1519fb6e | -4.49039 | -48.12136 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d754a65f-640b-309e-80d1-220fa9f2f982 | -4.48663 | -48.12078 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1caa9fc6-8c01-37de-a492-b680ecf32865 | -4.40381 | -48.63561 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef4fa7ab-e791-3f81-bd82-dbb5535e70ef | -4.73128 | -48.84407 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e39e5d8-dcea-3705-8bbf-f0ff8771274a | -4.73028 | -48.84505 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc68c313-c1ce-30ce-a2ba-7a9baa3ec9de | -4.72766 | -48.84346 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ddbbecf-2ac5-3def-b3aa-4e8cc6c94f76 | -4.72732 | -48.84021 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b105af9b-0236-30c9-b4a4-69ad15928593 | -4.72342 | -48.84697 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3c65ff1-6f65-367b-a309-d51f0c986eba | -4.72241 | -48.84789 | 2024-09-29 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 119b45a4-dae5-3521-bcaf-bdc2e1f70964 | -4.35428 | -49.09952 | 2024-09-29 04:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87d8065c-0e5e-3e82-8d08-71b53344dcd5 | -5.57803 | -49.02791 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12039131-a07c-3844-94ac-c50584320667 | -5.57629 | -49.01464 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9dd996c-0666-33f2-a21f-54aaedf721c5 | -5.57265 | -49.01409 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ab85b18-18b6-338a-a577-6468f3ef8da6 | -5.57203 | -49.01832 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff0e4fc1-9120-3f4d-b146-5e42324320e6 | -5.57179 | -49.01511 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41a46105-7f71-3345-a7f8-876c34c2fe20 | -5.57114 | -49.01933 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c296b73d-87c5-3445-9276-ed1d63bf793e | -5.56902 | -49.01354 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f44e7b22-3aa1-3ce7-959c-d0b76e18b669 | -5.56881 | -49.01034 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 732319e3-f9a8-372c-a287-d86b7c180bdc | -5.56816 | -49.01456 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 617ccd15-c13f-3439-90ba-f934c0f3b513 | -5.56601 | -49.00875 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79f65c92-3905-3b61-9cf1-276f1c9dd1e9 | -5.56538 | -49.01299 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f33b2bd-0c36-38ee-b412-12c8e2d8cd8d | -5.56517 | -49.00979 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54e09a61-c1f6-30ec-9e1d-147c2b2098da | -5.55596 | -49.02134 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b17ae1b0-c93c-390c-8841-212ab0276a9c | -5.55532 | -49.02555 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2318291c-3c16-3952-820c-5242b944d757 | -5.52177 | -48.97732 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edb21b36-2208-3447-8cba-f69c0f309754 | -5.41283 | -49.07913 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f523fb39-10c7-3d4f-8511-53d8962049ea | -5.40922 | -49.07859 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfd2a390-82a2-3303-848e-c30038e14908 | -5.27027 | -48.88641 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73496a81-f324-3eb3-a034-a8a3a1ce2ef1 | -5.26726 | -48.8816 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 045faba8-0576-32a9-8550-f46b508550b8 | -5.26689 | -48.88313 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9f83f14-f7ee-33fe-b482-5a8147d3387b | -5.26663 | -48.88586 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0ae48f2-9b0d-3154-abdc-ec8e4d383efe | -5.26623 | -48.88738 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1820f76-7e98-3e77-be18-9c1e381a83af | -5.266 | -48.89011 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2c446a3-876c-3b9e-b244-dcf2d36be799 | -5.26298 | -48.88531 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 367a114a-0698-3699-911e-8caa73a7a5b6 | -5.26259 | -48.88684 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d8af838-f699-38ec-8827-d508a128512f | -5.25807 | -48.89326 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9147b2f4-73a8-37fc-bb78-ea62b97b0c0f | -5.25763 | -48.89477 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6960fb1e-f420-377b-b0cc-5df16fbbc640 | -5.25034 | -48.8937 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a54454f9-faf4-3ec5-b63e-c56e6b9776e9 | -5.24605 | -48.8974 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75cca187-7644-32ff-8805-b6ea75f8bf71 | -5.21196 | -48.97426 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 716824cf-dea2-3d4a-98fa-8149d62a1b9c | -5.21132 | -48.97847 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d73051b6-1cba-3b9f-b86d-50174379a037 | -5.20769 | -48.97793 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README45.md)
