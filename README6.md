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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe96059e-5ad1-3e66-bfd2-04160afdaf57 | -10.6784 | -54.5356 | 2026-07-01 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 38d2143e-a777-3db3-a009-f1cfdb87c522 | -11.4338 | -56.0509 | 2026-07-01 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 336.9 |
| 55e5b36e-15ab-3617-9b55-ca71c1b92990 | -10.1237 | -52.0905 | 2026-07-01 02:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2f16d481-6920-374d-b1c5-1a01cfe0d335 | -10.9205 | -43.0622 | 2026-07-01 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 955b240a-f2aa-3d47-a1c6-c7e7a362f90c | -11.4147 | -56.0726 | 2026-07-01 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 9bfb070f-7392-3225-b2bd-46d478cdac21 | -11.4149 | -56.0525 | 2026-07-01 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 7f631297-5755-3584-b886-362950ed65af | -12.8548 | -44.3625 | 2026-07-01 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| e8574072-87b1-3ed0-8772-8945cd875a6c | -12.8363 | -44.3186 | 2026-07-01 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| dafa5b4b-af39-3440-bd3d-99a87be6ab24 | -8.5933 | -48.0069 | 2026-07-01 02:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 36419eaa-ef9f-3fa9-b762-b3fcc7177324 | -12.4096 | -58.3865 | 2026-07-01 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0b265a1b-1507-3731-877a-c800e2cac904 | -11.4336 | -56.0711 | 2026-07-01 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 509.7 |
| 97b8bb0f-6055-3a48-86aa-f84f3254bf77 | -12.8165 | -44.3454 | 2026-07-01 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 87c594af-1b18-3518-a992-74d0ec2125df | -12.8354 | -44.3657 | 2026-07-01 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 249.0 |
| 32251d20-1357-3719-80a6-d3d80f73bc3f | -12.8359 | -44.3422 | 2026-07-01 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 765.0 |
| 87759947-4c5e-33a9-8d5a-514b6b1da44b | -8.6121 | -48.0051 | 2026-07-01 02:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 73fb6e8d-dd50-380a-a2da-0005f11d8b34 | -12.8552 | -44.3389 | 2026-07-01 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 426.9 |
| 72fb3a06-b1b9-3068-9d59-c5a3608fb6cc | -11.5528 | -47.4546 | 2026-07-01 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e103fe5d-e6cc-3424-8617-8ff881cf09cc | -10.6596 | -54.5372 | 2026-07-01 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7fd05f6d-e5ce-3ab9-bce3-d7b53dbe2b16 | -11.5528 | -47.4546 | 2026-07-01 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 22f18bcf-ec9a-324d-88ef-490413b82f13 | -12.4096 | -58.3865 | 2026-07-01 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| cb955f1f-4946-3a52-98b1-ed3f1e2e9329 | -10.9205 | -43.0622 | 2026-07-01 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b7d07aef-d9ec-3cde-921c-09b0dc12c63e | -11.4338 | -56.0509 | 2026-07-01 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 330.7 |
| 030d083a-f6ba-3a22-a0c1-4b75a1a52b27 | -8.6121 | -48.0051 | 2026-07-01 02:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c8703a9e-cd0d-3031-b4af-89549899abc0 | -11.4525 | -56.0695 | 2026-07-01 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 54be7901-9a60-3e2b-9d5c-75848ea720a2 | -10.6784 | -54.5356 | 2026-07-01 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| ebe5917f-3a39-3613-8ec3-bcaa023304bf | -10.6596 | -54.5372 | 2026-07-01 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4388a681-ad63-3117-806a-8517985b803c | -8.5933 | -48.0069 | 2026-07-01 02:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 81fdf923-3f52-37a7-9b9f-783349a9bb68 | -11.4527 | -56.0493 | 2026-07-01 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3b524b54-5792-3849-a3cd-1dc96788ab71 | -11.6286 | -59.0169 | 2026-07-01 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7da0f5a6-9f70-34be-be1f-6ac16e1701e3 | -11.4336 | -56.0711 | 2026-07-01 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 420.8 |
| bff9773e-4a42-34a6-b87c-c3342a953c5a | -11.4149 | -56.0525 | 2026-07-01 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| a26def98-7872-32fd-8f3b-3d97e344cb67 | -10.9397 | -43.0593 | 2026-07-01 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c59744a9-eadf-36bd-bbb1-d43e33a3747e | -10.1237 | -52.0905 | 2026-07-01 02:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d9841892-c93b-3802-956a-af812c680a07 | -11.4147 | -56.0726 | 2026-07-01 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 198.9 |
| 4ed828a1-e742-3b6f-ad62-99f2f9edeec5 | -10.6787 | -54.5153 | 2026-07-01 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a3a42710-f9dc-3b95-9801-8968bf316655 | -11.6286 | -59.0169 | 2026-07-01 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| cf639f9e-f75b-30f0-aec5-63a0e1e71403 | -10.9209 | -43.0384 | 2026-07-01 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 188869ea-d060-32cd-a864-7ed6abc11a3e | -12.8359 | -44.3422 | 2026-07-01 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 648.2 |
| 499b8424-8467-3e9c-9e4d-a5f8d773dffc | -12.8548 | -44.3625 | 2026-07-01 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 17a30b96-2856-3357-94eb-fb191cf7f800 | -12.8354 | -44.3657 | 2026-07-01 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 310.7 |
| 0c524c65-67b6-3336-aa05-2bcfe2974928 | -11.4149 | -56.0525 | 2026-07-01 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 8b1ca166-26fa-378a-ac16-29609f6d240a | -10.9205 | -43.0622 | 2026-07-01 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0341cc47-8868-3e5c-b6ea-e3829fb8d2f0 | -12.4096 | -58.3865 | 2026-07-01 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4f8b6d83-d90c-30d4-8404-467a8ff3c24e | -12.8552 | -44.3389 | 2026-07-01 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 348.0 |
| fa775fb3-05b0-3043-8f7b-78ceaadc7e14 | -12.8165 | -44.3454 | 2026-07-01 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 46a9fbb2-5371-3def-a41e-4faece96f6d4 | -10.6787 | -54.5153 | 2026-07-01 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 92c0d63c-5fe8-313d-a140-7439306689d7 | -8.5933 | -48.0069 | 2026-07-01 02:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 7f025de5-b8a3-3280-a899-3678996de7ad | -10.6784 | -54.5356 | 2026-07-01 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| dbc400ad-bba9-3a48-92c0-fcc6f7e58f62 | -11.4336 | -56.0711 | 2026-07-01 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 416.7 |
| 7b401af1-494a-3f6c-9a5e-d7395c0f77bc | -11.4147 | -56.0726 | 2026-07-01 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| b6bd6047-7893-343b-b8cd-aed8b96bfb05 | -12.8363 | -44.3186 | 2026-07-01 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 61b3d90f-43e8-355a-8010-d0e8acc1edf9 | -8.6121 | -48.0051 | 2026-07-01 02:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| d385b5e3-6a00-3903-87ef-98a894f322e6 | -10.1237 | -52.0905 | 2026-07-01 02:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cf896058-4481-3020-8137-029fe7b4d1f1 | -11.5528 | -47.4546 | 2026-07-01 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0b3ae7a1-22de-368c-9585-8a20e74e8846 | -11.4338 | -56.0509 | 2026-07-01 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 380.4 |
| 222733e2-a18b-3d54-aa79-22064a760b80 | -12.4285 | -58.385 | 2026-07-01 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 53ec5e98-dfc9-3d45-97fa-0cba2b7d9610 | -11.4147 | -56.0726 | 2026-07-01 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 196.2 |
| 1655e1e9-6c0a-31c9-b648-7b7f0a188399 | -11.5528 | -47.4546 | 2026-07-01 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e8da2f9f-7e9a-3c15-97cf-aa68533371a6 | -10.6787 | -54.5153 | 2026-07-01 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7e8dabfc-3a87-3eb1-afe7-4a928c1fa2f0 | -12.8359 | -44.3422 | 2026-07-01 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 680.5 |
| 0ca6ae68-cff2-317e-9494-4be5952af025 | -11.6286 | -59.0169 | 2026-07-01 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 9e02e12d-8e6f-3128-827f-1a809d530935 | -11.5337 | -47.4571 | 2026-07-01 02:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 079b68a1-533d-3b50-8b85-324d4bfd4681 | -12.8552 | -44.3389 | 2026-07-01 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 392.2 |
| a8255bb8-ebf8-344a-bfce-045bd698ed9c | -11.4525 | -56.0695 | 2026-07-01 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 67efda66-47a2-37bb-938e-be0423cbe7e3 | -10.6784 | -54.5356 | 2026-07-01 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 529ef15e-dc2e-3a33-8009-9e7599aa5e93 | -12.8354 | -44.3657 | 2026-07-01 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 29cde545-7832-3033-ad76-566e156a5bd4 | -11.4149 | -56.0525 | 2026-07-01 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| f7216751-6744-39bd-8c6f-3289e922c5d1 | -12.8363 | -44.3186 | 2026-07-01 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8762c889-23d8-318b-9e6f-d5c1e4a9c019 | -10.9205 | -43.0622 | 2026-07-01 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 8452e8b1-26ca-3900-b50d-f6467e9f376f | -8.5933 | -48.0069 | 2026-07-01 02:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 41679f83-a53d-376e-9347-aad6d8cea662 | -10.1237 | -52.0905 | 2026-07-01 02:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7ccff839-c3ab-3a02-a087-270012e614b4 | -11.4338 | -56.0509 | 2026-07-01 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 228.2 |
| 14f35bee-1ee6-3d5c-8430-1d690346376b | -11.4336 | -56.0711 | 2026-07-01 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 322.4 |
| 999bea2d-02fb-30ad-939a-f8350cfeb9df | -10.9209 | -43.0384 | 2026-07-01 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| cd460488-15a1-3182-8ce4-e393d57050b9 | -12.8165 | -44.3454 | 2026-07-01 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5bdee31e-8188-3dbc-a4a9-460c3fdcb15d | -12.8548 | -44.3625 | 2026-07-01 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| ce6f5820-5110-3e1a-b83b-00ff8c6338d1 | -10.9209 | -43.0384 | 2026-07-01 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 4c798fe4-c4fa-3808-b9ea-c160312d1b7a | -10.6787 | -54.5153 | 2026-07-01 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| e8116104-ecca-3663-b1d2-250dab497a2b | -10.6784 | -54.5356 | 2026-07-01 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 219614d4-c7c1-3376-bdfb-09a87a25e2b9 | -10.9397 | -43.0593 | 2026-07-01 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 04a74cd7-5a68-348a-bd82-d791e52cd465 | -10.1237 | -52.0905 | 2026-07-01 02:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 27041370-faee-3bd4-af30-f67a4735f871 | -11.4147 | -56.0726 | 2026-07-01 02:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 321ba5d8-450f-31b8-9b3d-605a7d0486a8 | -8.5933 | -48.0069 | 2026-07-01 02:40:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| c1205e23-a9ab-34f9-8272-f4101d5053e9 | -11.6286 | -59.0169 | 2026-07-01 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| b91217bd-7244-3706-935b-6dd896729a01 | -12.8548 | -44.3625 | 2026-07-01 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 9269d363-11e3-35b7-ab1f-3bec9ccc22d0 | -11.4336 | -56.0711 | 2026-07-01 02:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 330.2 |
| 25d74b22-0531-3d30-abd2-abbd5cad7d42 | -10.9205 | -43.0622 | 2026-07-01 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| f209c498-c19a-3264-a6d1-72082e7e71b7 | -11.5528 | -47.4546 | 2026-07-01 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8bcefda9-0098-385d-916c-bb457499c960 | -12.8552 | -44.3389 | 2026-07-01 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 298.4 |
| 9a6d7597-4182-330c-96a1-6c95f2170ef8 | -12.8354 | -44.3657 | 2026-07-01 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 300.7 |
| 6ca0933b-8bb1-310d-8daf-9c94033b547e | -12.8363 | -44.3186 | 2026-07-01 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4045f06e-fdde-3c36-a5e2-2308d721e324 | -11.4149 | -56.0525 | 2026-07-01 02:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| b953e47e-47bb-361a-80b6-11fd92490aa7 | -11.4338 | -56.0509 | 2026-07-01 02:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 330.8 |
| 964f115a-e548-3485-b565-c6bdb6a6653c | -12.8165 | -44.3454 | 2026-07-01 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 193f1830-b68f-306c-83d0-a56739fffd96 | -12.8359 | -44.3422 | 2026-07-01 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 659.4 |
| 9782444c-a709-342f-879f-35d7562e25eb | -12.8552 | -44.3389 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 282.7 |
| 3a6ed6fe-57f7-360e-8ca1-82096411355c | -10.6784 | -54.5356 | 2026-07-01 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c6a9a315-7b90-3292-acc8-b9b5f3f817fb | -11.4149 | -56.0525 | 2026-07-01 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 2e8c4678-6c86-303d-b1bc-fe5eaa17083f | -12.8165 | -44.3454 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 91898a5e-a0c1-3e60-acaf-2132092dfd3b | -12.7746 | -44.5162 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |


[Clique aqui para ver as próximas entradas](README7.md)
