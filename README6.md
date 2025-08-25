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
| fa2e98ac-633f-3a96-b6aa-fb250a1e6475 | -8.2403 | -61.421001 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db1190e0-2224-311b-a6cd-b96234027741 | -8.5972 | -62.616001 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b3fb0b3e-c3bf-3046-b662-4ed41fb5acdc | -18.058901 | -51.371899 | 2025-08-25 01:03:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1d4914-3eab-3fcd-b0cb-e410c1c2cd9f | -6.3606 | -57.9631 | 2025-08-25 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16e50de3-2791-3342-80d2-b192bb71772c | -9.8219 | -64.245102 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dbd3cdf6-c686-3fe5-9b22-d9fe3f1fe61f | -7.5529 | -63.8545 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d566d15-3d9f-36d8-a507-048775c70233 | -9.4701 | -57.810101 | 2025-08-25 01:03:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39bd5f81-8f66-3b82-8e01-740b3eff3b74 | -10.2533 | -59.106201 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e95c3202-0640-3e0d-812a-3c0031db90ef | -9.0379 | -65.713898 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d02b886-16bb-374c-a0cf-c395f8b4f105 | -7.561 | -63.844601 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8c792bf-9938-3428-9ce8-3966f68ca88e | -7.3531 | -57.620998 | 2025-08-25 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84246307-6f75-3fe5-9252-186058a2a32f | -7.664 | -63.516701 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cc568f9-9a13-30e1-b6b8-680765d09eae | -9.104 | -61.416801 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf93f619-0129-3a76-9e14-9f7f46aa8b43 | -8.2464 | -61.448502 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01f0ddd0-31f5-33b9-8a38-d95311cab019 | -9.1892 | -59.458599 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b88e33c2-cfd8-3bdf-a31d-c9cd90c926b3 | -8.8857 | -64.180702 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eccec6bc-24d3-34a4-85a1-6ed9f9584211 | -8.9218 | -62.408699 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc8cfb12-b4cb-36c7-af6c-238d67c47984 | -9.1549 | -59.4436 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbd0444-06e2-337d-a1c1-7a474794fca5 | -9.2212 | -60.9258 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9ae771b-9529-3094-9ddd-152b43e50385 | -8.5906 | -62.632599 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2166483b-c443-3d2c-bf96-06c05f4ca218 | -9.6496 | -59.624699 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45ede5d3-074b-3575-8ccf-607534e906b6 | -8.5189 | -63.859501 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e1511ca-e510-3195-bae5-3a7b5bc06206 | -14.3073 | -49.072498 | 2025-08-25 01:03:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e28b2beb-942f-32c1-9324-18e22c4a2b68 | -7.7886 | -61.565102 | 2025-08-25 01:03:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54e2a4aa-dcd5-36c2-8a9f-17493246951b | -8.9003 | -62.451199 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5728374e-e50e-3ee5-9b10-f6b6eebcfb93 | -10.8907 | -55.782001 | 2025-08-25 01:03:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3fb4b8f-a101-3b20-89b5-607f910a68e3 | -13.0009 | -56.885799 | 2025-08-25 01:03:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27fd26cb-e4b1-3e4a-bf03-40f5b4ff3461 | -6.2476 | -60.029999 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3626ec-89c8-32f1-a5fa-4c0233b14858 | -9.2267 | -59.668999 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7fd575c-c0f9-38c8-87a2-f5f76114b7ca | -9.0694 | -65.717796 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a672689-a6c9-32b9-8a83-28bc933d9de1 | -14.2341 | -58.6106 | 2025-08-25 01:03:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9357ddd-42d0-337f-a6ce-6169039eafc1 | -8.7342 | -64.143898 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f3ea1a1-0c63-3824-9953-928dc3de3f20 | -8.8971 | -62.436798 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3400528-8847-3d70-894f-aec5ffe15492 | -20.3393 | -46.6991 | 2025-08-25 01:03:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c3339f27-b566-3bbe-be82-6d473b70faf1 | -15.6211 | -52.696602 | 2025-08-25 01:03:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3af42de-13ed-330a-a9dc-066e5b78ea9d | -18.0686 | -51.369099 | 2025-08-25 01:03:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4e0edabf-0107-36de-8927-07f494097c1f | -9.2611 | -59.638599 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20990e73-2085-35a0-9ad4-2bab9e16ad8e | -6.2917 | -59.997299 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86f885b5-0d90-3b10-bde9-44d2b897b2e2 | -7.9224 | -63.0541 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5e41ec3-b90c-30c9-afbf-6760ad4f00cf | -8.2289 | -61.416302 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d4efd76-1001-35c4-9a41-92c6f47525d1 | -6.8219 | -59.429199 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cda77c9e-8a23-3767-9134-49badf32cad3 | -9.15 | -59.467602 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b51aac4a-f189-3e08-9434-8f87b92c9636 | -9.2082 | -60.9142 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d928c61-d59c-3240-9ebf-c5d50f52a083 | -8.2295 | -61.3727 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88fdaa4c-fabd-3e7f-a851-5e9677235636 | -9.8059 | -61.194302 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05e0b4bb-bddc-3e51-914a-c3bfa39f0449 | -9.0199 | -65.386597 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f06d071-a2e5-3062-b8f7-b4f25beb8488 | -9.1876 | -59.451401 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5c7386f-9ce3-324d-a01b-acf186d8f499 | -8.6282 | -62.616798 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b08eb64-bb1c-3c7f-82af-3d16de8a990f | -7.5312 | -63.8022 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d601bf34-c611-31df-85a9-46a82ad4c586 | -9.1598 | -59.465302 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0f513a-c30c-3cb7-9ee7-197930624060 | -9.1761 | -59.446301 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4df9dc-6a6d-3e24-9da1-d526001b257c | -9.8139 | -64.255798 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0db30fe2-b750-35a9-a0db-72a7cf7e284e | -9.1663 | -59.448601 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad041f99-e599-3fe3-b33b-3b062e8b2dbd | -8.9101 | -62.449001 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85d22ad4-f9e8-38be-8da1-3fc15a5d92ba | -10.422 | -64.419098 | 2025-08-25 01:03:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b59d6fb-c8cb-3f3d-85b2-752a3ea9bf99 | -9.1418 | -60.755001 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7199c4c-0a9c-36d6-a96f-ae59530ad5fb | -9.2098 | -60.921101 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7ba4133-1256-3a16-93ae-2c58cb0ba4f8 | -9.2114 | -60.7901 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f381029a-6053-363e-b1d8-ae0219a3eea5 | -7.1027 | -59.214802 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2455504-0052-3db8-a01e-3ff9df7d877e | -7.0448 | -59.818901 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6effbd27-8207-34ce-a031-0b899da8c7bd | -8.8987 | -62.444 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eefc9206-01a8-3ed4-950b-25a7ba624b6c | -8.8665 | -62.3909 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 479dc826-43e6-3cfb-9a0d-f0f868cd1868 | -8.9926 | -65.402496 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f74df9c5-49b8-3f61-a402-0620abad5096 | -8.6118 | -62.635502 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7bb1b7b-20bf-377b-b00e-6083099bf7fb | -8.589 | -62.625401 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e56d3c4-170b-361d-ad4b-ff2ae7a4da19 | -9.1743 | -60.762199 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26e41bc0-c367-3325-b4cd-b0c6cc13f5e9 | -8.8905 | -62.4533 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21a09028-6b66-3a8b-940f-5ad97f0c9173 | -9.1433 | -60.762001 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4aaf7b0-d619-3ca5-9a2d-4a36f13896dd | -8.633 | -62.6385 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a7bc3883-6143-3722-9869-b51c8977ff37 | -6.8202 | -59.4217 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bae5a33-3778-395e-9969-7c1e14b4dc03 | -9.204 | -59.478001 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 135f5139-e332-3c8d-aafb-7c9bcdc8011a | -10.2435 | -59.652901 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87fabc22-0986-375b-8cdc-277af303b306 | -9.1924 | -59.427399 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac0a005b-d803-351e-bd50-ef3f83561cac | -9.4018 | -60.536301 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 774fe5ea-92ae-31ca-99f6-e896b18c0890 | -3.8368 | -55.967499 | 2025-08-25 01:03:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4497dd0-4dd9-3418-9e76-026d3a69f866 | -9.2072 | -59.492401 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b286ccac-f477-3305-a67c-8fdd90f0857a | -9.0217 | -65.685699 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e86fc721-39ab-39cc-9e25-5b65406916a1 | -8.8857 | -62.431702 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac4a399-1f44-35bd-86c1-09c5c26b0fbb | -8.231 | -61.379601 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6264f316-9593-3e17-b9c6-088f0e0521e0 | -9.1984 | -60.9165 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc6f0f1-44c7-3b1b-a415-dd22cdb59889 | -14.2259 | -58.620201 | 2025-08-25 01:03:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce7ef59-699b-3bff-a940-202f387f75b4 | -11.0497 | -51.991798 | 2025-08-25 01:03:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53df5291-dac9-373f-82ce-2c2dd859c713 | -11.1719 | -55.020199 | 2025-08-25 01:03:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 690f99c0-12b8-39ce-a9a4-29fbef95f281 | -9.1242 | -60.722698 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb8e3197-2eb8-382d-88be-19e556c15ef8 | -8.8955 | -64.178596 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d06dca7-fb1b-3f67-a223-25c8b41119e0 | -9.0081 | -65.378899 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be13495a-7b60-3cff-83bb-2748c471e214 | -14.2357 | -58.617802 | 2025-08-25 01:03:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e75a1d22-1149-3a19-934f-e93ddde7d318 | -9.2464 | -59.6194 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a327bc42-f807-3e95-afdf-53a28905cda7 | -9.2595 | -59.6315 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23317fa6-3e00-31bc-a527-f71e33d2c811 | -8.8889 | -62.446098 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ebd0d1e-f8f4-3d75-a3c5-8d5a9631e062 | -8.6907 | -62.855 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad665deb-5b8e-3964-a6ea-28268a473f73 | -7.4414 | -60.614399 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee73e4a-1177-3224-a717-197148d51281 | -6.2574 | -60.027802 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b6dd112-3b88-3c18-8a2d-63a2e72f4f09 | -11.6985 | -60.167999 | 2025-08-25 01:03:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8c7ae44-ce25-39b8-a87d-1074afdc8866 | -22.716299 | -52.152901 | 2025-08-25 01:03:00 | METOP-B | PARANAPOEMA | PARANÁ | Brasil | 4118303 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd5fa97f-5a4a-39f5-b9c5-ef617d5f9739 | -9.1942 | -59.480301 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43794066-483c-3f0c-bc0f-83c09ac58881 | -14.2161 | -58.622501 | 2025-08-25 01:03:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2742b772-129f-315f-94dc-f6535e82f340 | -9.1909 | -59.465801 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b787cb1d-b021-3eab-9686-ca547ca86c40 | -3.8339 | -55.954899 | 2025-08-25 01:03:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0436141d-b31a-3007-82a9-c148c2c8570b | -8.6121 | -62.590099 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
