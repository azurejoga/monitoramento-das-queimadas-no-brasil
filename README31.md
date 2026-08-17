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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbef2fb7-5f2f-3586-9a15-51f24c60b475 | -8.89958 | -60.59055 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a901776-3301-305f-8e99-49b7fdf2dee4 | -8.60185 | -54.70445 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfb62a07-9a28-3140-90fc-5bcaa65ba821 | -11.21978 | -54.02249 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0936890c-5e40-34c5-bbb5-1fe4b8434d1c | -11.23463 | -54.01739 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57dc67d7-22cf-3513-a86c-a14a0d427e65 | -11.81069 | -44.80954 | 2026-08-17 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 88f59e95-f1ba-3396-8c9f-995bb98b021d | -11.49224 | -46.58106 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99366d62-7745-3469-9b88-e14367ce39cd | -14.46808 | -52.07779 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a6716d6-7041-3527-8348-c6985c4b1597 | -14.4929 | -53.27438 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00ec6cb0-ef22-3607-a3c4-d72545c08b14 | -11.8162 | -51.77206 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84334a26-870b-37d2-b4ea-e09bbf161a84 | -11.71972 | -54.59148 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b443d30-5e8d-355d-bcaf-e2ffce245dbb | -11.71151 | -54.59797 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c390dd-4994-315a-b400-9643116590ad | -10.0557 | -62.45991 | 2026-08-17 04:57:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5f13045-96a8-344d-a92e-a81c8f080c3c | -9.17664 | -59.66791 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d44570c-3c9a-3ad5-a79a-54105e351204 | -6.68909 | -59.0612 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e12cf27d-8227-3a57-8de5-942bc2b1c85d | -6.9829 | -59.04406 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f694fe-90af-3db4-a504-1d991b89190c | -14.19174 | -53.05984 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8118015b-15bd-3488-8e8f-aa4ede7f5f9c | -8.58304 | -54.68425 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18b2528a-b761-3181-9113-4dbc59a0ff42 | -6.62373 | -59.07604 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a72dc4f-9391-3dde-83db-f8464a15cf1e | -9.47435 | -51.60727 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3de15a7-7f8b-31db-afba-ab2a07237dc0 | -7.90613 | -48.5261 | 2026-08-17 04:57:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7c07b19-3bf3-3c6e-9e3a-d01281bfbdeb | -12.04354 | -46.48024 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 912dea64-718e-3d64-8e9c-9e6a27846ba0 | -8.95387 | -60.52884 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c0e61ad-0d58-363d-8e60-fb95a4f21a6d | -6.70462 | -58.95657 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 931e6db6-de32-302a-9642-43a32f613265 | -6.96353 | -59.04056 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09193b4e-ed71-3183-9158-f39fbbab08a5 | -14.18672 | -53.06989 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b468f05-3cb7-3302-8916-2730fe3ae990 | -6.62757 | -59.05416 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71d1ed20-61ee-3b4e-923c-fc6f48c65bcf | -12.7076 | -48.5268 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b411aac0-d22a-3eb9-ad25-45e0d8d91810 | -13.51771 | -46.28048 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a75d0ed-2833-3c8d-98a7-47d6bc6c837a | -6.83502 | -58.97065 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aef2770b-3348-3b6a-a30c-45c460ee07d8 | -12.46395 | -46.65475 | 2026-08-17 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66105031-ef17-3a97-a62a-e7456cd6e085 | -6.60893 | -58.97568 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 047cdc16-0e9e-3867-a754-eab4d783b14c | -12.32749 | -47.24693 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92b8adc7-696f-3c45-86a4-37041270c7a7 | -12.26093 | -45.89927 | 2026-08-17 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4cdb5db-1a07-3560-9065-3207f03132c5 | -11.9074 | -47.35479 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0679de90-1019-3035-bc1b-f8ec6cf1f155 | -13.63685 | -56.98936 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c5eeff2-ea39-34f9-a1f9-9165f66b4ef9 | -8.95671 | -60.57174 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d24fc5af-d639-3af5-ab00-223c1068a7d5 | -13.46474 | -51.80312 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b41bff2d-8ebf-354d-95a2-3e54159569a3 | -15.04307 | -47.02541 | 2026-08-17 04:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7a7ccfd-35aa-38be-a06b-d5cc439bb453 | -13.82141 | -53.84627 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36959b9f-f260-3cce-97db-241aa1d0d2c0 | -8.90301 | -60.57171 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9c84baa-632f-357c-b08a-208d9028da4d | -6.77376 | -59.77338 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6038ca1a-d1d7-3f11-a76c-8a8f21cb4168 | -12.68609 | -48.51426 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 197f5b3e-55ba-3c18-8c08-cfc6e08becfb | -11.50601 | -46.60536 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70427d7e-e82f-3189-911f-5bf0ef5ab9d6 | -10.50521 | -50.40226 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d17cd3d-1f80-3e5d-bcf6-7c47cbf8a47c | -10.46551 | -46.30391 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3481ecb4-ba4a-310f-b7e0-a5f391c53542 | -13.50727 | -46.25652 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15d7f0e7-f1cd-3942-95b0-da118860317f | -8.95906 | -60.52976 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bce43b9-8be0-3942-95fe-8c6e030e2d43 | -12.69999 | -48.52565 | 2026-08-17 04:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a398fc75-8c50-382e-a9ac-5fad568a7734 | -11.50552 | -46.60896 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 595591cb-e539-302b-be9e-c422d6fd1240 | -14.37931 | -53.13485 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bae42f1b-dc88-37e7-8573-5bbb8f861de8 | -8.58594 | -54.68899 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 8f4745cc-8472-3f18-8aef-7985b7731c04 | -12.89897 | -52.82455 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69c7c74e-f79f-3f11-8d21-9ae2990089db | -10.46868 | -46.31244 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5865ff04-635c-37de-9999-380da02a3e75 | -13.51656 | -46.28928 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 600959f0-d21a-3ec5-904a-a3b0cce08966 | -12.70201 | -48.51161 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 657430d8-4b00-340b-9ad4-6f83fbc6ddfa | -7.61224 | -60.95626 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d66544ae-8a0d-392e-a8da-fd7d1b81ad8f | -8.52443 | -54.90174 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f620f3c-44f7-38b4-a5a9-1a8de83a87e0 | -11.70611 | -54.60894 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95496d36-de14-3b74-987e-92f46bde41f7 | -14.45031 | -51.83621 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31f39827-4789-35f0-a7a2-a970ee217b26 | -11.23524 | -54.01366 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc898060-7535-34aa-8e09-70322e05392e | -10.49975 | -50.02465 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 573060df-6d0f-3933-9e99-618d7587044d | -11.3964 | -46.40886 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cedfce54-bd67-3dbf-929c-eec68eed8cbc | -12.0609 | -58.04278 | 2026-08-17 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6f7bc43-2c0c-39a4-b8c5-07fe3982fa93 | -11.48435 | -46.57584 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b79c25e8-4097-3091-bec8-f38bd75bbc2b | -11.81953 | -51.7726 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5d5cb72-fd17-3ea4-8eaf-2ac06b68a967 | -11.49636 | -46.61279 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0487a8e7-9d80-3967-9c97-899f02a3f018 | -8.95043 | -60.51847 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae6de8b-e7a7-3d2c-b125-0376f20ce5a1 | -9.4799 | -51.6368 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91b1c347-e8d5-3ccb-9d28-ca6f96962289 | -6.61377 | -56.27302 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6ec8abe-3947-3f1a-83c2-06f36e75b3fe | -6.96319 | -59.30643 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d61b8248-b307-3bfd-85ef-8d683bd9c582 | -7.34813 | -59.59555 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb7d5609-3591-3578-b72d-3d54635f0a30 | -14.36691 | -51.89797 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27b2a11a-ee17-395f-b252-c20fe492d1c5 | -8.94584 | -60.51439 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5704221-ab2b-3390-8911-c5b324dd9d21 | -8.54664 | -54.59352 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63036b36-1416-30b7-8127-230845c502bd | -9.34729 | -50.33429 | 2026-08-17 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feecdc95-0849-3e45-9bb5-a3fb8acb690f | -6.62765 | -59.0824 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6fa23a7-88b1-3642-9361-c4532edefff4 | -9.46937 | -51.61722 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9df3f8cf-4887-3b97-98a1-affe93d1820f | -6.61561 | -58.96575 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6803501-1df3-380d-bd1a-75c5cd07809d | -11.70958 | -54.60952 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24389c2c-e228-3db9-8d36-63bb4b78c0c8 | -7.46073 | -60.00185 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e384705-5a36-3851-b90c-b19d69af2e6b | -11.13586 | -46.5193 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8181436-f30f-3a5c-839f-d5225f27d9f6 | -11.40438 | -46.41404 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85751938-748e-3416-a78e-45d55906d368 | -14.87296 | -46.65559 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 478d674a-0ac7-3586-a6ef-bd46c93662cc | -8.94985 | -60.52162 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfa6153d-ce18-3008-a25f-6ea6d98f1af5 | -7.61893 | -60.95036 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ebf408a-a64e-364e-a4b4-a9dbcd466021 | -10.46921 | -46.30851 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f75a353-8eb1-311f-a951-294c2be6496b | -11.46904 | -46.59279 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9adda93-2345-3c3e-af9a-211c6c998187 | -13.52832 | -46.23437 | 2026-08-17 04:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d841476-a76e-3558-b500-d8437a1f7262 | -14.39653 | -51.87238 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1f3c6ee-4717-366c-84eb-4f5295329389 | -11.10338 | -47.27987 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16bb2c24-7150-3363-bd6d-0b878a8e28df | -8.97919 | -60.53672 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e177eb8-5991-33ab-a3f9-5642de8132d6 | -6.87645 | -56.41589 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22170ce8-1ed1-321f-a104-af902e5bd11d | -10.47019 | -46.306 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b32a6fa4-76fe-3e6f-9ced-ddb2f67bddea | -8.09457 | -46.90031 | 2026-08-17 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d5581f-df4b-3f0e-b947-2823497ee97d | -14.31823 | -53.43192 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5da1876d-917c-36c6-ba43-ed4762752cb2 | -7.38548 | -55.48725 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b71505cf-8b2f-3c2b-a981-8a8b202e875e | -9.99853 | -51.48252 | 2026-08-17 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eeb96f10-6f1f-3f26-83c8-a32faf956c8b | -8.94467 | -60.52069 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b4bb941-43c2-396b-bdae-7c65465054af | -6.96837 | -59.04147 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b20a68f2-fe0b-32cd-ba2b-361b0f66d0ff | -8.5128 | -54.90427 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
