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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adb93f38-277c-3848-a3fa-0a053744e9cd | -10.6571 | -54.14167 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c87d7501-4c7f-3f6e-ab90-c6b8c5ca9df3 | -10.6688 | -54.14312 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 324.9 |
| fb3aac56-f8f5-3779-b5b9-fe4271009689 | -6.59047 | -58.857 | 2026-09-14 07:31:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a02fc08c-a307-3800-8fc6-b310615d38e7 | -10.66067 | -54.13692 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 3bb1c92e-e39b-3f38-bb4e-cda58a8a242b | -10.64898 | -54.13536 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 249dd943-1c36-3e31-bd22-4d4d08ab0789 | -6.33026 | -60.01099 | 2026-09-14 07:31:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6357c83-e6eb-35fd-a30f-b38fd8b399a9 | -10.67012 | -54.15474 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 356.4 |
| f8ef148e-a13f-3653-9cf6-13d527d08bde | -6.79424 | -58.79231 | 2026-09-14 07:31:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b01b6694-6e73-3f3e-94c3-69b4c6486eef | -8.53722 | -54.70222 | 2026-09-14 07:31:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e12e6f88-799e-3363-a6fe-e2029bf92f70 | -10.6805 | -54.14459 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 172.6 |
| 41cb696b-db09-3521-9440-bd2dc1f76826 | -10.67238 | -54.13834 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 275.3 |
| a632e900-0ceb-3435-beb9-59b09a9047a3 | -10.65842 | -54.15336 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4bb428e1-675c-343b-8836-0da688cc6af6 | -10.67835 | -54.16107 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 5a5fcae0-d2b1-3c20-a2a4-91a72b35261b | -10.66786 | -54.1711 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| d8b92c8a-37ad-3035-b620-0423a3a52139 | -10.66667 | -54.15957 | 2026-09-14 07:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.5 |
| a3e2f35c-43d5-3fae-839c-0e8c761792a9 | -6.28605 | -59.93226 | 2026-09-14 07:31:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c8e9f72e-80fd-3fe2-9995-bf981f37e02a | -9.44085 | -50.12519 | 2026-09-14 07:31:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 93015ff9-13ce-3afe-b591-6c44026532e0 | -6.31659 | -59.98045 | 2026-09-14 07:31:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a3a1e0cb-b65d-39a3-b522-5940e2abfc81 | -6.31803 | -59.97123 | 2026-09-14 07:31:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3aebc06d-8494-37cc-8d13-86ac6c4a1031 | -10.6832 | -54.127 | 2026-09-14 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 86791ab2-3e2f-3bd0-a973-c70813a9afb7 | -10.6641 | -54.1491 | 2026-09-14 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 212.0 |
| 9d73d250-992a-38ed-a8ea-afada98765d6 | -10.6643 | -54.1286 | 2026-09-14 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 204f6391-4578-3665-afdb-5eeda179443e | -10.6638 | -54.1696 | 2026-09-14 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| f97f1d30-e4d4-3044-ab77-6c2a73939d58 | -10.6829 | -54.1475 | 2026-09-14 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 284.3 |
| e8a56cff-6887-3cd3-9f1d-59a0b428e168 | -10.6827 | -54.1679 | 2026-09-14 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 84e8f52a-cdce-3c91-ba0b-24b0516f333f | -10.6829 | -54.1475 | 2026-09-14 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.4 |
| c955231b-0ffb-321a-9617-db09139e6027 | -10.6643 | -54.1286 | 2026-09-14 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| dca75441-2d67-3c97-941e-24e279b687a8 | -10.6827 | -54.1679 | 2026-09-14 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 9d9306fb-2e8b-34ac-b71b-fc13774bf04b | -10.6641 | -54.1491 | 2026-09-14 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 240.7 |
| 1a984584-ca0b-3a96-b280-2dc1775836a3 | -10.6832 | -54.127 | 2026-09-14 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 60a87af0-939e-32a1-a3be-c802a1d3b7b5 | -10.6638 | -54.1696 | 2026-09-14 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 935a4216-4b9a-3eca-8732-c7afc3a05c8f | -14.2055 | -47.3813 | 2026-09-14 08:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e1b14ac1-cd17-38a2-9d14-3c8892a53d65 | -10.6827 | -54.1679 | 2026-09-14 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 9218380a-b1aa-3e71-939d-d8e4073a16a4 | -10.6641 | -54.1491 | 2026-09-14 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 220.9 |
| 2b0d001a-3c92-3d8f-b7c4-9896d9dc0e7f | -10.6829 | -54.1475 | 2026-09-14 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 194.9 |
| 101b2c75-667a-3c83-8af8-8867e1ee99a0 | -10.6643 | -54.1286 | 2026-09-14 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7b0029cf-bb85-3e3f-a63e-1181b8560bb6 | -14.2059 | -47.3587 | 2026-09-14 08:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| bb54fab6-1923-35ab-a66b-bbd5dfc49e1d | -14.1861 | -47.3844 | 2026-09-14 08:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2d8e3411-29eb-3d72-b07f-fcca31349af5 | -14.1856 | -47.407 | 2026-09-14 08:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 6053b85b-7ee3-3f9a-8727-12850ae5da36 | -4.1333 | -60.6882 | 2026-09-14 08:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f28157d7-6027-3563-9b4b-41a3f7184554 | -10.6638 | -54.1696 | 2026-09-14 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 240ac704-0135-386d-8445-e255ff45ba11 | -10.6832 | -54.127 | 2026-09-14 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d19975d5-f114-3ab4-bcf3-d48eb3d06588 | -10.6829 | -54.1475 | 2026-09-14 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 204.0 |
| d0f11d9c-f8f4-302a-9cce-a4e3fcf56f22 | -14.2055 | -47.3813 | 2026-09-14 08:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2df62003-c993-3e9f-9dd2-1700c4d84b75 | -4.1333 | -60.6882 | 2026-09-14 08:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 7ccf2a85-eaf6-3a34-9cd1-1a0e47ebdd4a | -10.6827 | -54.1679 | 2026-09-14 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| b9cd928d-730a-3cc2-b2b2-b7f8a718c01b | -10.6643 | -54.1286 | 2026-09-14 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 47783f6f-c347-393d-917b-3bbec2cefb3c | -14.1861 | -47.3844 | 2026-09-14 08:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a8ce6d47-53e8-3d18-979c-6b0f649698bf | -9.4328 | -50.1086 | 2026-09-14 08:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 68b4a5e6-1dce-3890-b7d5-20a738709e8d | -10.6641 | -54.1491 | 2026-09-14 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 279a177b-f8a2-3106-bb3a-c00a630a2684 | -10.6638 | -54.1696 | 2026-09-14 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 367c8cf2-7b1d-33c3-8928-70cea3da3785 | -2.91 | -50.45 | 2026-09-14 08:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d80be6b-3d8d-39f3-9091-2dfe32092f33 | -2.91 | -50.4 | 2026-09-14 08:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ec448b8-d439-3f42-a9fa-2c5231fa2b30 | -2.94 | -50.4 | 2026-09-14 08:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 534f84d9-0741-3e66-a21c-e8c53c43e8cd | -10.6643 | -54.1286 | 2026-09-14 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ded2d6fe-7609-3301-8d95-845112c790ff | -10.6638 | -54.1696 | 2026-09-14 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 2634bc09-5a5a-37ca-8428-d7bd387a9a2e | -10.6641 | -54.1491 | 2026-09-14 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.9 |
| a46db5c0-517f-3a92-bf70-77defd7b2ca4 | -4.1333 | -60.6882 | 2026-09-14 08:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d871cb6b-2866-330f-b91c-2da8e43f91de | -9.4328 | -50.1086 | 2026-09-14 08:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6ede3f3d-37ce-3997-bfb4-1087ac672247 | -10.6827 | -54.1679 | 2026-09-14 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| dade2a46-6544-3386-868a-85bd5f129b06 | -14.1861 | -47.3844 | 2026-09-14 08:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 26ce98b9-0757-3c20-ab3f-309e8a002b1c | -10.6832 | -54.127 | 2026-09-14 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a44108f9-56a0-3967-bc60-5be5944b30bb | -10.6829 | -54.1475 | 2026-09-14 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 206.4 |
| a16714cd-3737-3711-a477-bfa13536cb4b | -10.6643 | -54.1286 | 2026-09-14 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ccf199f7-a657-31eb-877e-2b297fb2895b | -9.4328 | -50.1086 | 2026-09-14 08:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4780a7f7-9753-3cbf-b452-e036bcac3e22 | -4.115 | -60.6886 | 2026-09-14 08:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 71781bac-009b-3c29-a51c-d0bfbd17a009 | -10.6827 | -54.1679 | 2026-09-14 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 7acde966-2176-3b05-992d-e30eaec6b785 | -10.6829 | -54.1475 | 2026-09-14 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 41695382-77f9-3e5b-9817-cdf8a7ea9a62 | -10.6638 | -54.1696 | 2026-09-14 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| e7dcb378-9282-3fe4-a370-0b7399ec5653 | -10.6641 | -54.1491 | 2026-09-14 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 182.3 |
| c189a412-0b0a-3c72-a867-d3edeec0dcad | -10.6827 | -54.1679 | 2026-09-14 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 31bfc3ce-178f-35dd-9802-cb08d4fb667b | -10.6643 | -54.1286 | 2026-09-14 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 18b0cb1d-d37d-3bef-854a-f0202a364b6d | -4.115 | -60.6886 | 2026-09-14 08:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 0114364c-ecf3-3c0d-87e7-5a85a42c290d | -10.6829 | -54.1475 | 2026-09-14 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 116dc718-1a63-3d5d-8ffb-928164380cf9 | -10.6641 | -54.1491 | 2026-09-14 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 177.3 |
| 46872f77-2e26-31b0-a48a-e1b8125c4e75 | -10.6638 | -54.1696 | 2026-09-14 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| be3c6d15-8a6a-3e2d-be0b-7fcba3c84e8d | -10.6827 | -54.1679 | 2026-09-14 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 6fce755a-c82d-3813-93c3-7c729c22d837 | -10.6643 | -54.1286 | 2026-09-14 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d56a7378-0374-332a-a593-bf3a76abb85f | -10.6829 | -54.1475 | 2026-09-14 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 059c3be8-280e-3092-9330-30364807f8b5 | -10.6638 | -54.1696 | 2026-09-14 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e76cc26f-85cc-3b1d-acea-055fda69f7c1 | -10.6641 | -54.1491 | 2026-09-14 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 5510443f-840a-31b1-887d-50d630c054f8 | -4.115 | -60.6886 | 2026-09-14 08:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 93f73933-f30c-392d-af08-4a9370b024e1 | -4.115 | -60.6886 | 2026-09-14 09:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| da3a2ce7-89c9-35c8-9f29-1bd8f25aabda | -4.1333 | -60.6882 | 2026-09-14 09:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1a4b9f88-6899-39fa-88ec-552329a92627 | -2.91 | -50.4 | 2026-09-14 09:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0130b56-39d5-3cbe-af3e-3866b775f416 | -2.91 | -50.45 | 2026-09-14 09:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd2cf6c-d1d2-3e06-9169-64410623d0a8 | -2.88 | -50.4 | 2026-09-14 09:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe4deae4-28cd-38aa-bb95-360e51b9702a | -4.1333 | -60.6882 | 2026-09-14 09:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| bf46bec4-a7fe-3ce0-bb31-886a573078d1 | -10.6829 | -54.1475 | 2026-09-14 09:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| ffdee6e1-4d8f-3377-9c0d-2f91ca3b06ef | -10.6641 | -54.1491 | 2026-09-14 09:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 720b0b09-3064-380c-aeba-4e66887449e4 | -10.6641 | -54.1491 | 2026-09-14 09:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| d4c69351-a1c8-339a-970b-52a3c904efca | -10.6829 | -54.1475 | 2026-09-14 09:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| bbfb82f2-897a-3921-b2cb-5fc27e5f983e | -10.6641 | -54.1491 | 2026-09-14 10:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 11cc4941-051a-3be7-afbc-a5599c41f3cd | -10.6829 | -54.1475 | 2026-09-14 10:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| d3b87018-1e43-3f04-b366-56ac1132dda7 | -10.6641 | -54.1491 | 2026-09-14 10:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 616d9506-038a-3db0-b5e6-515f13b43fe3 | -10.6829 | -54.1475 | 2026-09-14 10:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 79e5116f-e54d-3ad4-a574-6ba5d371efa7 | -2.91 | -50.4 | 2026-09-14 10:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589bb57c-71aa-3f55-9e3e-74a05119ffd1 | -10.6829 | -54.1475 | 2026-09-14 10:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 42a69d85-5e56-364f-b6b8-a3adef65dce6 | -10.6641 | -54.1491 | 2026-09-14 10:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 0b886083-950c-3291-b999-d5d9cc9ed882 | -10.6829 | -54.1475 | 2026-09-14 10:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |


[Clique aqui para ver as próximas entradas](README65.md)
