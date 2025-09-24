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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71b6e5cb-b9dd-3a9e-adc2-277a16f8b96c | -10.57708 | -44.07779 | 2025-09-24 04:51:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80b64f1f-8b90-3a62-9e26-2449c4c31300 | -6.42426 | -43.09735 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c092c0f7-b47d-3bb5-bce8-fa37c3a56c1c | -10.58346 | -44.07132 | 2025-09-24 04:51:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3ebdcad-b8e1-300d-8556-8adea0171e03 | -11.6341 | -44.34105 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef868407-c9be-30f4-b8ca-fa012619fa08 | -4.58009 | -47.707 | 2025-09-24 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6d40a01-1e44-31b7-babf-eaaf1e1318b8 | -7.82371 | -47.85975 | 2025-09-24 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf21886d-16bb-3026-84b7-5501859b85fd | -5.24813 | -43.72347 | 2025-09-24 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9606bc9d-1459-32e4-8122-666441fd1d94 | -5.63457 | -45.73376 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3c1a27ee-7b72-3bab-abb6-8997acb718fb | -6.43075 | -43.09102 | 2025-09-24 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d005e027-dc2f-35f1-ad0e-13200924cc25 | -6.42474 | -43.09386 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 33268b17-0203-37f4-bce9-b616bd00e385 | -9.20989 | -43.1283 | 2025-09-24 04:51:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f344efe9-0cfa-311a-8e6a-7e07c525d672 | -9.13776 | -65.31015 | 2025-09-24 04:51:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42b0f511-dc3d-3b67-999c-0578781263fe | -9.58798 | -47.59159 | 2025-09-24 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f296b662-cf22-33a3-8e64-4196dc82c4d1 | -9.20937 | -43.13228 | 2025-09-24 04:51:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d6d78a07-2a87-3c08-9d6f-b4312d36f18e | -5.65046 | -43.61032 | 2025-09-24 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e87c00c0-a7cd-3a4c-894e-3fee73ed864a | -3.9321 | -52.03169 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d2bfd47-c79f-380c-a132-6998f4e45b41 | -4.29065 | -48.26217 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37143f23-346d-335d-806c-7f96daf0e70a | -11.42463 | -44.94112 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bdfde9d4-915d-3ed5-8b2d-d165c78671fa | -5.64045 | -43.60619 | 2025-09-24 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63d4cd3c-53b8-3072-89fb-784657920735 | -5.02967 | -43.60004 | 2025-09-24 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 962e44dc-e25f-3104-a5ec-4285ac85275e | -6.53764 | -44.22139 | 2025-09-24 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9883f271-05d0-35c1-b34a-82ab82674926 | -4.31291 | -48.09064 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| e71145c7-6b69-3cc5-8ad7-1fe0912e8e4c | -11.52476 | -43.66721 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8de86287-04e2-3ca3-8570-21032ae50c86 | -9.89265 | -64.84238 | 2025-09-24 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56126e0c-e4c8-3187-a9df-ae6d70a34ce3 | -15.93052 | -59.35777 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a18b6f62-a9b9-3f1a-8e11-020553b14d6a | -15.36016 | -59.17168 | 2025-09-24 04:53:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26f16f74-e995-31c8-a91f-2e3ff2116bc8 | -15.83863 | -59.59329 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2823f224-429f-3087-b4a5-5a50d9c39db9 | -15.36399 | -59.17235 | 2025-09-24 04:53:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4a0ee47-8525-3453-a8a4-cb9561884d95 | -15.83475 | -59.59256 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d523da4-c2c1-3c68-ba98-4fcc60325f97 | -15.27816 | -59.42506 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78c74eb9-14b2-3537-b1eb-bdf747713e10 | -15.81344 | -59.48847 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54ed1679-83d4-3378-b3db-17e2c2e53b72 | -15.96549 | -59.49437 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 194e534e-f9af-33d3-940d-2301f50c8963 | -15.2656 | -59.42813 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecefbff4-2960-3f36-a979-507b0897f147 | -15.82994 | -59.59695 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3eeac100-64ee-3fcd-bd66-a784f523cf41 | -15.97415 | -59.49046 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a16837cf-0d8c-3cd3-9011-392ba477fea2 | -15.78084 | -59.48529 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4df9fd57-e02a-32c2-8d24-faef19e64e18 | -12.89338 | -44.65097 | 2025-09-24 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0834ed0-083e-3fb6-b952-3863781ee3b7 | -15.2668 | -59.42615 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c197c5fe-bb6a-39b6-95dd-295a981445e8 | -15.924 | -59.35838 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 428003ae-f3d0-3f0a-a31b-d5cd62defdfa | -15.78175 | -59.48011 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| addc75fc-271a-3879-a0e3-4db31f886b94 | -15.78471 | -59.48596 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d24ebf8f-1cec-34a7-bc83-e6a1da13985b | -11.15528 | -54.12719 | 2025-09-24 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c12ff41-cf85-3043-ac18-3463cc2bedba | -15.97225 | -59.47878 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7f16bc7-1d9e-35ec-8166-6ded16ec381e | -15.26167 | -59.42769 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d8afc3e-0654-3528-978d-e6e57b3f57b1 | -13.616 | -43.97961 | 2025-09-24 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fab87713-aa21-32d1-9537-9dc187fe0acc | -15.35579 | -59.19632 | 2025-09-24 04:53:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10d4cf94-dad7-35e4-b23e-e8de75b58337 | -15.83955 | -59.58818 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbc92c0b-d19f-3265-b645-ca450c4dfa65 | -15.95119 | -59.50742 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b2049ad-a231-3c62-bf9f-36c85b4544d1 | -15.92018 | -59.3576 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd62e1c-0e55-3be2-892a-25c19838b84f | -15.96642 | -59.48912 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f87d0705-e6c0-30b3-8e25-c6bb5a37a275 | -15.91257 | -59.35596 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a5783b-e144-3da1-8d99-67ff39319a8c | -15.92481 | -59.35375 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62d64fd8-a764-3627-b3ad-aac3b247d91c | -15.77995 | -59.49035 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62192e26-0648-3984-a25d-0e84c0b0ae88 | -12.18178 | -47.75398 | 2025-09-24 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 463e4ed4-eb99-3637-b89f-04ba71615df2 | -15.93247 | -59.35514 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7f14abf-bacd-38c8-8102-c9c322461ae1 | -15.83383 | -59.59767 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d6584d85-5e8e-394c-bbad-e3a16d92902b | -15.91637 | -59.35678 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6240eea3-14da-3bce-81fc-57a957c4f856 | -15.35928 | -59.17663 | 2025-09-24 04:53:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1ff5672-3eda-3aca-8ecc-b524e9af125e | -15.90876 | -59.35514 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65fa5504-0fa7-3cfd-b9cb-98ea3f82e7cc | -15.27154 | -59.42211 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b71efe26-b68b-380e-a9a8-bd516343450f | -15.35667 | -59.19138 | 2025-09-24 04:53:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b5057e8-e9bb-3022-ab44-a9638bd5f1e7 | -15.89641 | -59.35788 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbd42292-5be7-35b4-9a18-bf588d35653b | -13.61961 | -43.9812 | 2025-09-24 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27c80771-d566-3836-9ed3-6410c218e532 | -15.90495 | -59.3543 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 243d268f-23ec-3677-8a5f-b3d20964d647 | -12.89561 | -44.64952 | 2025-09-24 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5037cdf-6197-35e7-b454-01a990339b51 | -15.28329 | -59.42368 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244077ca-e5c6-3434-96c1-2af373bec533 | -15.262 | -59.43045 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a53d7d6d-301a-331d-ad9f-d119dbfe2db2 | -13.81625 | -43.22799 | 2025-09-24 04:53:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 49c39c64-3604-35d1-8a3f-75ce3b3aed9c | -11.14813 | -54.12962 | 2025-09-24 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 606f1e64-8797-3a6c-90fd-835584e00a41 | -15.27034 | -59.42398 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca56edf-71f8-3d38-9cbe-accf9b882b93 | -12.89295 | -44.65446 | 2025-09-24 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7e92d57-dc04-3d0a-87ed-f56067806f00 | -15.78273 | -59.47452 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b8cda9f-727d-3520-a343-0b5c6f2f7308 | -12.88978 | -44.65224 | 2025-09-24 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18e7857a-59c5-3bd5-ad0d-be21a8b675c8 | -12.18326 | -47.75194 | 2025-09-24 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15c5510b-a104-38ca-ae84-2c7504074536 | -15.90025 | -59.35854 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 809b7240-77bf-3026-a9fc-9eccee6c5b1a | -15.27937 | -59.42315 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4efe5e4-62fa-391a-bd74-861ac4abf8e4 | -12.1827 | -47.75626 | 2025-09-24 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2302cb44-aa79-3a54-99cd-8e2065c090cb | -15.96754 | -59.50519 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd92b0c8-7ecb-31b0-8963-ae579a50114f | -15.93164 | -59.35987 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0692529-46ed-33c4-883a-7501613de230 | -13.81425 | -43.22702 | 2025-09-24 04:53:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1aac18ca-4a5c-3b63-b9a7-afcdfce1d277 | -15.96844 | -59.50013 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bebe0dd9-bf80-30a8-a85a-4929c464e9b3 | -12.8988 | -44.65173 | 2025-09-24 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49b412bd-ede8-36c3-9e66-8d6e722fdbd4 | -15.96369 | -59.50446 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 891b42bb-9d17-318c-adcd-4a3e11a2c70b | -15.89933 | -59.36378 | 2025-09-24 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 962223e1-fa70-3344-bb44-e95908ff2246 | -16.46105 | -55.138 | 2025-09-24 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d307953b-67ce-3a46-8500-20bdd86bbf2d | -14.45063 | -55.93325 | 2025-09-24 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3b39000-0e64-38ae-8e8e-8ea4920012da | -19.70895 | -43.92342 | 2025-09-24 04:55:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e6c830d-26ab-326c-a54f-f093772a75eb | -22.37743 | -49.49162 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7a2d994-8b54-3dd9-9b9a-4240ddfe5d3b | -21.00425 | -47.38069 | 2025-09-24 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 21cdee1d-366e-3850-b807-60cf916bcf6c | -20.90267 | -55.26162 | 2025-09-24 04:55:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e32c2d9-5954-3dc3-b5f4-5fca603f6bde | -22.60988 | -49.01465 | 2025-09-24 04:55:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a5cb6793-93b8-397a-bb02-999cd6ceb6b1 | -22.38081 | -49.47564 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfabdc74-202b-33d3-a495-f1fd8ab2fc97 | -17.95131 | -55.87162 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 58faf669-6684-395d-861b-4c45ea67df51 | -17.95692 | -55.85771 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 03222d56-5ae4-3417-a20c-7eefa7b7b469 | -17.95073 | -55.87524 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| aa22d5d7-ebdf-37b3-a396-b3a0c50eeb9c | -21.26895 | -54.15342 | 2025-09-24 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c448564a-2c9a-3c00-a31f-8a0c8636abac | -22.20198 | -49.66875 | 2025-09-24 04:55:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 63f4a667-fd11-347b-811c-f24bfb506690 | -22.36401 | -49.46384 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f17ab35e-adaa-3847-b7a9-77c10a9e8369 | -21.00461 | -47.38299 | 2025-09-24 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0bf7905f-6827-318f-96b7-537e847f653c | -22.37975 | -49.48483 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
