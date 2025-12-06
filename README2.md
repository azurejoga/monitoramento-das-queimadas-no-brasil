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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df63453b-0a30-3817-b203-44facca60d21 | -19.6647 | -56.8073 | 2025-12-06 01:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| b06d6077-7f2b-35ad-b4da-c7bd4fc1c85f | -19.6643 | -56.8283 | 2025-12-06 01:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 163.7 |
| e1538c37-7837-3aab-8988-25f9dbed924f | -19.6643 | -56.8283 | 2025-12-06 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 196.2 |
| 32145fc1-8e18-31e0-b475-9d57c726b635 | -19.6639 | -56.8492 | 2025-12-06 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| cd6c3ee0-caf9-3872-9b0d-f65847801716 | -19.6647 | -56.8073 | 2025-12-06 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 3c5f6c46-2414-3b57-8154-11bc85ffc72b | 0.4325 | -50.9203 | 2025-12-06 01:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4b97ef96-a65f-3388-9ec6-1894e94675bb | -19.6844 | -56.8254 | 2025-12-06 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| c184a9d9-7265-32bb-9495-ddf0386c56ab | -19.6647 | -56.8073 | 2025-12-06 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 701cee0d-ec29-3c7c-a112-a9f6a5e3f899 | -19.6643 | -56.8283 | 2025-12-06 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 213.6 |
| 55389c56-da74-3431-b979-3f52b8e7ec20 | -19.6844 | -56.8254 | 2025-12-06 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| a64ba305-1f1d-30d9-baff-debc42a6471d | -19.6643 | -56.8283 | 2025-12-06 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 188.7 |
| b926baec-4cad-3a5f-9eb4-b13f988ce580 | -19.6647 | -56.8073 | 2025-12-06 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 21d2a3bf-a69b-3c59-a777-00d58c951a77 | -10.0235 | -36.4589 | 2025-12-06 01:40:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| 6ecc3dcf-1b7c-3176-ad40-31884716352d | -19.66724 | -56.85329 | 2025-12-06 01:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 3379e550-46b9-3471-9fc0-315c2653d589 | -19.65945 | -56.81476 | 2025-12-06 01:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 147.5 |
| d9b2f1b4-007e-3bae-a46b-9d3ab35eedcc | -19.65549 | -56.82266 | 2025-12-06 01:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| f413a6db-6d0c-3317-8561-728c0c933c12 | -19.6643 | -56.8283 | 2025-12-06 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 160.7 |
| 2e63a926-ae97-33f1-bcec-2c7a47959f1a | -19.6844 | -56.8254 | 2025-12-06 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 52775592-c741-307f-b38b-a82236d88c56 | -19.6844 | -56.8254 | 2025-12-06 02:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 2316c3ba-b39f-3e2b-85ca-53025ecd0b75 | -19.6643 | -56.8283 | 2025-12-06 02:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.7 |
| ed79c4b4-5395-3495-9d61-03d7cdeea627 | -19.6643 | -56.8283 | 2025-12-06 02:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| c4699df0-fcec-34f6-b648-b0857d4d0ecf | -19.6643 | -56.8283 | 2025-12-06 02:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| c53b9aa9-5cf0-3174-91a1-81e275f99356 | -3.87704 | -41.58834 | 2025-12-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ba2871a-0704-3b4b-b5ea-871220e032d6 | -3.54951 | -43.37692 | 2025-12-06 03:42:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e5bad08-41b9-363d-86c6-a4a9aea9900e | -3.4704 | -43.88734 | 2025-12-06 03:42:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 396529aa-3e25-34bb-b2ce-90daf0c5ea34 | -3.87865 | -41.57888 | 2025-12-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e85802ae-5b56-353e-9525-dde6b1273d89 | -6.64024 | -39.71551 | 2025-12-06 03:42:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5e46af40-7aa5-3f93-9718-ef7b158d8627 | -1.72018 | -45.77428 | 2025-12-06 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6511099-2ea4-39db-8bea-db929c7b061e | -3.66506 | -43.55579 | 2025-12-06 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4945d3a2-0d41-33ad-8841-845677f1ade0 | -3.6652 | -43.55818 | 2025-12-06 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47dea6d0-086c-3d19-ab64-223b53c72ef7 | -1.48026 | -45.58373 | 2025-12-06 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ff7150f-9eeb-3e2f-ba4d-9df6a18deb47 | -3.47581 | -43.88821 | 2025-12-06 03:42:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a952f0e-9759-3388-b87d-0e6aa734931c | -3.66451 | -43.55899 | 2025-12-06 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bceea7b1-5bab-3f27-974b-f68c232e841c | -2.16996 | -47.87207 | 2025-12-06 03:42:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0d964ca-9683-38a8-8fab-4e251aad0c32 | -2.58889 | -45.54702 | 2025-12-06 03:42:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1c9bd04-3b22-3fac-b140-135fdffdf1c4 | -5.90374 | -37.82924 | 2025-12-06 03:42:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 785f6028-b825-3263-93bb-0d779b0b2dce | -2.29168 | -45.78433 | 2025-12-06 03:42:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c11003d-ba7b-37be-b701-e8abff6331e2 | -3.65994 | -43.55727 | 2025-12-06 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2813d34e-7d47-3640-8ecb-ac01bc350b33 | -2.29789 | -45.78539 | 2025-12-06 03:42:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4d18fae-3848-3166-9cfa-a41fdfb6c7c5 | -6.39504 | -38.28578 | 2025-12-06 03:42:00 | NOAA-21 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c24b4e95-4f54-320e-844c-01bff8af842d | -1.48108 | -45.57883 | 2025-12-06 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23d86e6c-3ce8-3ea1-a354-c811e44a9902 | -6.42597 | -39.57593 | 2025-12-06 03:42:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 346d4c5e-a44d-3e53-bd03-28dfcd177d37 | -2.33825 | -47.47452 | 2025-12-06 03:42:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee721b99-88c6-3f0f-8dba-a5538a70a25a | -5.5762 | -43.74794 | 2025-12-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd94dae4-79ef-3784-a331-a924169a9e9b | -4.47536 | -44.15267 | 2025-12-06 03:42:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd26b73f-ab44-3dcf-a039-66c313a681d8 | -6.63637 | -39.71481 | 2025-12-06 03:42:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 68ff0e2c-9e1d-3135-913e-48fe9c3d7502 | -3.47098 | -43.88386 | 2025-12-06 03:42:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44437b1a-422b-3796-b426-1ab85c9c18a1 | -2.5891 | -45.54928 | 2025-12-06 03:42:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25adad4e-9e23-3dff-bfbc-06716d5db187 | -6.75768 | -39.80744 | 2025-12-06 03:42:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea14baa2-9668-3874-b42e-b0e3917a6d1b | -2.16641 | -47.8646 | 2025-12-06 03:42:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c649f21-0ce4-3b30-90cf-49fea8243b32 | -5.58189 | -43.74586 | 2025-12-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59c90665-6b4b-3c9b-8b09-84d0a027e939 | -5.78555 | -35.56646 | 2025-12-06 03:42:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 34b2d43d-85ee-3c67-bf5a-27c452c15a1b | -5.58135 | -43.74894 | 2025-12-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdef3838-f075-3e93-923b-f1e90b69c517 | -3.66572 | -43.555 | 2025-12-06 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9195ed4f-b32c-3ed0-9ad0-4e2a4f17cb9b | -5.53357 | -37.73968 | 2025-12-06 03:42:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca9f4e11-2764-37f3-8a4e-d0beb4cc0f33 | -3.87752 | -41.58591 | 2025-12-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 76b1ffad-4320-3bd1-bd3f-801efe4ea63a | -2.34509 | -47.47583 | 2025-12-06 03:42:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44d665a9-f7b1-309a-8e73-86f7565bfebf | -3.54898 | -43.38009 | 2025-12-06 03:42:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22903760-02b6-38a0-bff2-7d2e8a2d3def | -1.85431 | -47.48258 | 2025-12-06 03:42:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 07a3e5a0-cb75-3b33-b504-df8ed4f79244 | -3.47638 | -43.88477 | 2025-12-06 03:42:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 656dca36-9546-3bdf-bf8c-ecfb7bac24bc | -5.40945 | -37.65561 | 2025-12-06 03:42:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8fadcdea-90d2-32e9-b11b-8c8e22f2a605 | -5.90386 | -37.82841 | 2025-12-06 03:42:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2ed9a49e-e0c5-3cf0-a2be-d1e08ea13064 | -2.16528 | -47.8714 | 2025-12-06 03:42:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc0cb01c-e193-36bf-880c-a7791e4e341b | -2.17113 | -47.86529 | 2025-12-06 03:42:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| afa5d5fa-5c7d-3158-89e7-e5608d5c90f0 | -5.10221 | -39.22216 | 2025-12-06 03:42:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b150bbca-02c9-3aa4-be32-64b933394ec5 | -5.85392 | -39.94339 | 2025-12-06 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a873c8ce-b462-3257-a682-abc5e35e5c79 | -2.17347 | -47.86572 | 2025-12-06 03:42:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7a6eba7-9bb6-31c9-905c-1564f074ee61 | -5.53004 | -37.73912 | 2025-12-06 03:42:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4e6b3b8d-e1be-34ac-a4ce-600c8683b23e | -6.63556 | -39.7197 | 2025-12-06 03:42:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ba11aaf6-b5ae-3938-80ae-c818bd3aceb6 | -6.63943 | -39.72041 | 2025-12-06 03:42:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d1fca491-b537-3462-860e-9a24b914043b | -2.70466 | -45.68554 | 2025-12-06 03:42:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34bb28f5-ecc8-33b8-be48-c8623d9d32a8 | -5.61151 | -35.63463 | 2025-12-06 03:42:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca257e5c-3fbf-3860-8b6a-b49c7b3ac526 | -5.90438 | -37.82523 | 2025-12-06 03:42:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a92ea55-06b1-3fc6-ad09-4f9ce58fc6bf | -6.39572 | -38.28169 | 2025-12-06 03:42:00 | NOAA-21 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 907797d1-09ab-3337-a5a0-a85e5f96d3e1 | -1.48202 | -45.58188 | 2025-12-06 03:42:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 913a9961-64b4-386c-8d01-8d9e1028992e | -4.46997 | -44.1516 | 2025-12-06 03:42:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70309750-8f7a-3c83-b4f2-3d196e10aa17 | -5.60819 | -35.63411 | 2025-12-06 03:42:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 054a3379-eb41-32ec-acfd-fe3fa188ac6b | -5.54058 | -38.01404 | 2025-12-06 03:42:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee2082ae-8895-37cc-8148-7cd4e34dcbf6 | -5.85788 | -39.94417 | 2025-12-06 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f44a561f-21fe-32e2-b116-c66013427d3e | -5.58081 | -43.752 | 2025-12-06 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1151ba4b-d63a-3884-bf72-fa5ff307c1f6 | -4.16411 | -39.25183 | 2025-12-06 03:42:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 541d1f03-c20b-3e38-9a17-bd2f0e0c3e3d | -2.16412 | -47.87832 | 2025-12-06 03:42:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f9894aa4-4b64-3d2d-97ff-4b2e62a5df5d | -3.87785 | -41.5836 | 2025-12-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 415dbd48-e5a5-32d1-98ae-48438e2faeee | -6.53104 | -39.76628 | 2025-12-06 03:42:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ccef856-9e83-392c-9d42-6fab8bec9594 | -5.14631 | -35.54311 | 2025-12-06 03:42:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8119ae8-3ad0-3eb6-9397-6a3a0c323a7f | -5.36543 | -36.84256 | 2025-12-06 03:42:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb6c3a88-cdfe-3411-805f-1914174202c2 | -5.3292 | -36.80654 | 2025-12-06 03:42:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84263c42-e7bb-36eb-b257-dd91c6fa2585 | -6.57817 | -39.67338 | 2025-12-06 03:42:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e265fe90-15d6-31ea-9d00-44eee15c0219 | -3.87829 | -41.58116 | 2025-12-06 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 44400d47-0dc8-3c7a-b48a-e593dc7042d9 | -2.23411 | -45.59725 | 2025-12-06 03:42:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54ad0482-8a50-3967-b035-555eb230acb7 | -2.16168 | -47.87794 | 2025-12-06 03:42:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56fdcf18-13e3-3ce5-8383-31eecf3726fc | -6.60298 | -38.75583 | 2025-12-06 03:42:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 63d6049a-3aeb-32f9-bea4-3e581daf9666 | -2.23491 | -45.59253 | 2025-12-06 03:42:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b05ed39-ee95-399e-ae3e-49dffbaf40fa | -4.54401 | -38.33523 | 2025-12-06 03:42:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e311a9ba-df70-3ff9-aec5-c6bdd5e721cd | -1.85796 | -45.5879 | 2025-12-06 03:42:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93783131-85e0-39d0-a2fd-d1cd98714c13 | -5.7861 | -35.563 | 2025-12-06 03:42:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c2ff59bf-052d-3d4f-8028-8a387bdbefb3 | -10.07273 | -36.55105 | 2025-12-06 03:44:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d485c78f-ebdc-3146-947b-0bff5ce30fcd | -9.33937 | -36.96789 | 2025-12-06 03:44:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9212df95-c685-39ce-8f85-ce18edd788ed | -10.26318 | -37.85975 | 2025-12-06 03:44:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ac16a5e3-bc57-326f-a64d-155b0a2a83e8 | -10.19009 | -36.34739 | 2025-12-06 03:44:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
