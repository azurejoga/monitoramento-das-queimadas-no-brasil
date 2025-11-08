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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db603721-7b9f-3fed-87f0-a99f127c8b4b | -3.40795 | -45.43998 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a7e0cadc-cba6-33e7-abbb-774da46f5228 | -3.60387 | -43.51942 | 2025-11-08 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c69d002-504e-358e-9d9d-ab96196600c2 | -3.12923 | -49.10309 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04fd0929-e06c-3ff4-9a99-b4d86a7d3ab2 | -4.7276 | -42.92445 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5991709c-9ce5-371b-a19f-674eead89318 | -4.64986 | -46.87573 | 2025-11-08 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41929214-64f5-32ee-af00-c6e07449f360 | -3.14424 | -50.29248 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04579e1d-ed27-3e2b-8020-93b3c1cd658d | -3.00535 | -49.60975 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1975f8cb-6983-3682-901c-ffb9f389b17b | -3.38865 | -52.65403 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da99319b-9ef7-3732-9202-b48946bd0b91 | -3.51837 | -49.26378 | 2025-11-08 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da8fa71f-786b-39e4-bebb-21209309e900 | -2.82611 | -49.8333 | 2025-11-08 04:55:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43b7563e-394c-3c94-94a0-de0794eebf28 | -5.84345 | -43.41739 | 2025-11-08 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae19fa65-aceb-3077-a0b4-90298bce39cf | -3.09444 | -49.2531 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c63e8eb-a124-3a7a-9c7a-0105b3e9e9b9 | -3.34432 | -50.17969 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f3fd820-32e9-36ae-a0cc-490d616d6664 | -1.32098 | -50.64215 | 2025-11-08 04:55:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a063840-792f-3dd2-9b87-8f306c0bc63c | -4.53206 | -45.62245 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1b68fd76-d030-3621-8652-78e12c6fe5b4 | -3.53273 | -47.54186 | 2025-11-08 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d30ee3d-ca28-3f6d-aac9-7ad5a54ac97c | -3.40877 | -45.43431 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9ccd9768-1bdb-37c4-8514-f59b6eecb953 | -3.39188 | -52.65425 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eabbf9b9-6a62-3973-9114-62fd222a6c25 | -4.46337 | -45.32458 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c801b8d0-2a22-32d2-9a2d-27748d5572b5 | -5.91045 | -44.53001 | 2025-11-08 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e1b4640-7bb7-35de-ad05-0b6ef1e0b3f3 | -4.83697 | -48.54878 | 2025-11-08 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9689267f-0b73-32aa-a1b8-1e82a90fa212 | -3.85623 | -47.40425 | 2025-11-08 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71fbae69-3f51-396b-88e1-cf6ab288f978 | -2.69973 | -48.97475 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99127c51-02bc-3464-8d7d-f383ed16c3b0 | -4.64526 | -46.87517 | 2025-11-08 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bb76d33-3780-30ef-9f56-ec26d9f943a0 | -3.39885 | -45.43282 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c7ab7f4-f10d-38ce-9ef0-eee4b0355f29 | -3.36033 | -49.51338 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ac2ea0c4-3d7b-3c88-93de-251da7d5d718 | -3.43541 | -50.24424 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eb03eb3-f104-3058-b080-a9ce1ba4969a | -3.95326 | -45.45266 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| becf8260-bb92-3d30-a607-8e19b2b4f7c4 | -2.97719 | -48.70865 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f8a5cfa-af6d-3ce8-8167-0a128746051b | -3.33476 | -50.19864 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 333f3029-bc45-31e2-85af-7176058c30fe | -4.64156 | -47.95079 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6f0c16e3-dc79-3f70-b7d9-302078800213 | -2.98845 | -52.82232 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02d97d2e-c90c-32a2-acea-c820e56d3da8 | -2.989 | -52.81886 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdcb2419-7805-370c-9d62-a31033a1b915 | -4.90347 | -45.10659 | 2025-11-08 04:55:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9f537f6-082b-302c-a85c-ed8b1abac55d | -4.53292 | -45.61669 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7d6305c1-04d7-3d2e-a2bf-664b1514c21f | -2.61427 | -49.2277 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84ef4c94-1b3f-3508-b2de-0bf07c1876b1 | -3.04778 | -50.26157 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9064d38-b8d4-383e-8628-5f3928e3c8e5 | -3.51426 | -53.53963 | 2025-11-08 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9d6b135-dde1-31fb-a2f3-77081400ac8d | -3.82944 | -49.83113 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a83e21f-b7fd-3678-af3e-21dea90a1d73 | -3.43669 | -43.17362 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b298c36-6f63-3cff-a61f-0e1d7f68060e | -3.65507 | -50.2753 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe153e79-80f0-3d4b-83dd-1978e6643497 | -2.98114 | -48.70924 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e24d730-ddd5-375c-a35e-343edcb15213 | -3.6137 | -52.12517 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b7f12e1-4fd0-3dea-8405-c72561d2dba5 | -2.10023 | -48.04854 | 2025-11-08 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec0e28e7-04d5-364b-a521-20d5a8df995e | -3.42909 | -50.1179 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2bed21e-a54b-3725-a6c7-4b907704760b | -3.32099 | -49.13708 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926f2c10-fa54-33fb-ac5e-05aae451032c | -3.15378 | -50.30242 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0df1489d-b505-3794-94e2-cacc570c686c | -3.3221 | -53.35781 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f209a32-3032-3b14-bc45-69f99eda4c79 | -3.43717 | -43.1723 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a6c6e88-bab1-3998-b4e2-96501b65110b | -3.11789 | -50.14425 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0243ce0c-8690-33c9-8dff-7f2ebabad341 | -3.83723 | -49.81632 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80674925-3ffc-3c1c-a2ac-2ee148c068a9 | -2.09616 | -48.04791 | 2025-11-08 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10271177-cc85-30a3-8d69-2990ce6b0fef | -3.15696 | -45.50118 | 2025-11-08 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6f27f39-5409-3e75-b552-3884d683b355 | -4.8282 | -48.55141 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 967402b4-f10a-3267-aa14-b604e33ecb0c | -3.31287 | -50.11879 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af4a0200-2033-3938-a761-3ca6e82aef22 | -3.40283 | -45.43284 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c00c796f-caf9-3629-a5fa-3fb29941fa34 | -3.35036 | -53.22148 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 040db74c-cf47-3948-87ea-34ce14423582 | -3.83595 | -49.81392 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b058e6e8-7ceb-3dfb-a030-84a7a4dae952 | -3.03145 | -50.27174 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0acab9e-529f-3bfa-92d8-9c585126a031 | -3.4343 | -51.52097 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c4c9a2a-bf29-31a8-b4bb-5c27939126cf | -3.83153 | -49.81779 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11524050-4bca-370b-9f8f-0ac9b035a337 | -1.42918 | -52.60255 | 2025-11-08 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22586385-fd5a-3668-b978-80212aa4fdb4 | -4.04553 | -48.98808 | 2025-11-08 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78095d80-948d-3731-8bff-c37608f988d3 | -3.06075 | -49.37177 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab3acaa-0a0a-322f-a98e-86a0d7ed24b9 | -3.0934 | -50.32368 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cab65b42-79c4-3104-907b-f1c0d4f09f1c | -3.7118 | -42.72836 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61bd1512-b3db-3fbb-a93a-08004d5b4f01 | -3.24555 | -48.76071 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e75be30-5289-3f9e-92e6-132142acd073 | -3.516 | -49.94017 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97a15482-0839-33f7-908d-21dbf7695064 | -3.35705 | -45.29663 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c3c294-b2e0-3580-8076-f6f4a25dba56 | -3.0957 | -50.33245 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd229c74-d0e0-38c8-a87a-eefa0e938904 | -2.52221 | -49.44931 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec3d99ec-7f8b-320b-b2f7-6dee4ede3056 | -3.65296 | -50.26921 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 89a89f8b-65a0-3761-bc7f-bda85da4eee1 | -3.83149 | -49.82909 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29d4ad6d-a7cd-3f92-bb94-b29424d38a09 | -3.33967 | -50.20921 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d7375e8-4af9-3455-8966-b27aa5de3874 | -3.60649 | -43.51886 | 2025-11-08 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43fb0cf5-da83-31a1-bf56-565eef321c7f | -3.31786 | -49.13168 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e07ea3dc-7b75-3082-a11c-53149beaf5f2 | -3.01489 | -49.44187 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0eecd8d8-3c07-3463-afb7-ff51af3b6061 | -3.15081 | -50.29772 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9387a52-8692-362f-a0fa-afdcb6ca697d | -3.30815 | -50.05274 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b85793d5-fc07-3981-8632-ef5134499d14 | -4.10481 | -47.27628 | 2025-11-08 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdd705f5-0e71-3709-a347-9dd43076e03b | -3.64206 | -45.88531 | 2025-11-08 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89fc2715-c3a8-3515-835c-f43bbe6bdf0a | -3.83961 | -49.82582 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15601255-4078-3aad-b2c2-6c9144fbaed0 | -3.41374 | -45.43505 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 70bd44a0-8aa2-31fa-bd8f-cb4498fe5ea0 | -4.73087 | -42.92704 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c93d1382-da55-3310-a53f-6288e33379bd | -3.59096 | -51.23654 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 053591c9-2e7a-324b-bde0-d359bd73c2fe | -4.82913 | -47.79078 | 2025-11-08 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deba1878-9902-3b52-b1e4-a9cc8e1aaba9 | -1.18538 | -49.05409 | 2025-11-08 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f675fb0a-3d8e-3d07-a411-a80a74f9f5ba | -5.84402 | -43.41317 | 2025-11-08 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de875da6-8079-3a3a-9472-cf0bfc985242 | -2.98129 | -52.82473 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1072d5e3-a803-3631-b5d6-055d40484c37 | -4.58878 | -45.99775 | 2025-11-08 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a98606ab-3a94-3254-bdba-ff1771f447af | -4.41081 | -54.98074 | 2025-11-08 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 751f52c2-1d59-38e9-8b3a-6b8a803ab785 | -4.47264 | -45.33215 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9a0718f2-211f-3ecb-af22-3658a32c0596 | -4.36403 | -45.61835 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3798185e-ec3c-3581-9390-4b2c80fa7f24 | -3.33839 | -50.19923 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d822e6b-c78c-318e-9440-a8a86244ffa3 | -2.61877 | -49.22364 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f3379b3-1372-3ded-bd2a-657588c72723 | -4.72699 | -42.92887 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7efda23e-7ee9-38cb-8656-37947b3e38b0 | -3.87209 | -49.91258 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cad91364-1fd2-3184-9acd-ecb812141843 | 0.85228 | -51.31673 | 2025-11-08 04:55:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12913b12-4dc6-3fd6-a9b3-88f885f65acd | -4.11351 | -48.01443 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9264f0d6-5ad2-3bc9-b0fa-f9b971c5087b | -1.50372 | -47.15202 | 2025-11-08 04:55:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README33.md)
