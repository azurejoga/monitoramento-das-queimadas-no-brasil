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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 078b8e04-69c3-3287-a542-a1b45683972a | -8.61692 | -47.1536 | 2026-08-25 05:12:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0f6c7d2e-4e50-3f5d-9781-421347cc4ccf | -6.96549 | -59.08026 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba46655-6356-38cb-a02d-7a25498b599f | -6.80404 | -59.58559 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 581a4d3b-a633-37e0-9522-74c091f49e7a | -10.20096 | -54.95525 | 2026-08-25 05:12:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d42c39b-4a6f-31cb-be01-c033aeb634d0 | -6.63271 | -58.49809 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2639f839-0f88-31b0-9038-e37700effcd8 | -11.16309 | -53.99673 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4309b518-63eb-353e-88b5-d0c43eacde24 | -11.09549 | -46.16177 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44fb86b2-4906-30ce-b22b-4101ca087403 | -9.53177 | -49.27307 | 2026-08-25 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d518657c-db2c-345a-a6b8-132d154ed505 | -6.13604 | -57.82927 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c61f6e88-d2e9-3660-a2d2-aeff98bf00a7 | -6.63049 | -58.49052 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| da8942ba-5a82-3147-bd05-2e62dee01d10 | -6.54547 | -58.51315 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50eea2b2-469a-36e1-adac-01c091957615 | -9.9602 | -48.3237 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f67f00ec-82b1-3299-b328-947fd357f911 | -6.13776 | -57.86146 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2f5dd62-9cfe-31eb-8fb0-e8a9dd7b7f9f | -7.2173 | -60.62374 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d75f883c-a26d-3d6b-8d5b-d078e11e188a | -6.44078 | -56.05694 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fc395b3-8028-3f80-8013-429a2b27f139 | -6.71854 | -59.43855 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1027cfd7-e69b-3e06-b384-d50d4517f913 | -6.81822 | -59.60703 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5d62f79-ee6e-342a-a061-425333517d14 | -6.12465 | -57.83466 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d6e5544-9004-39cf-b95d-db1e0e425854 | -7.01076 | -59.23996 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c185b26e-e6fb-37a3-adde-cd7d68508035 | -8.2065 | -54.97405 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b6b6772-e2e8-33be-8743-78bda4e5cbab | -6.83847 | -59.45732 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbeb204e-3291-3a8b-b670-bb52c38e6cb6 | -7.21451 | -60.62429 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ef5d13c-353b-32ef-abef-ea685f4c5589 | -8.5711 | -54.85557 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e231d716-3fa5-3082-b338-48131eaa14bc | -6.72361 | -59.45074 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e874b086-d6da-363c-bfc0-a3188f7877c0 | -6.79598 | -59.59199 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c159248-f681-326f-ab1c-f05cb3e0a6e7 | -8.07388 | -44.6432 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae702150-7c7e-315f-bf0e-2367b5685087 | -9.05139 | -50.80532 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c158c9ca-d0cd-3bc2-bc33-5836cb942ce6 | -8.57167 | -54.87685 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb61d085-aa47-32e5-b3ad-db74eb030a1c | -13.36085 | -48.20881 | 2026-08-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bd6082dd-665e-3ee2-8dff-253056302230 | -6.14466 | -57.70667 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd617f06-322a-390c-9128-c0049dda10a7 | -9.69411 | -46.05683 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f66ca503-b8a5-3696-95ee-27a5b49a7ae6 | -9.03047 | -50.81903 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6a71e2a3-288f-398c-ae6c-a4937c78b33c | -8.62571 | -54.73509 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38662c7e-979b-373e-8e50-1e2d01cc7ed6 | -9.67938 | -55.09404 | 2026-08-25 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c97b5f41-c94c-33a4-8684-f8f9f96318d8 | -8.57127 | -47.43359 | 2026-08-25 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9285e837-020a-3d34-a793-da41e7a7e197 | -6.80713 | -58.66344 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5a57ea7-a4a0-3772-a939-d85c0376ba2a | -7.21289 | -60.61156 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 065d465e-6d96-39af-b05f-4a13e13e938e | -6.18313 | -57.70198 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a553dbf0-7204-3ebe-9edf-44281a29c82a | -12.10057 | -50.57545 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f871edf-8af2-3776-b8ba-392f3c63febc | -11.97909 | -45.91185 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 31d89d15-d18c-3c72-8073-29da184b334b | -6.7968 | -59.80874 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 825f5ea8-12d5-33a7-a71b-6a4faa25c10d | -6.73805 | -59.66745 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3100844a-1c1d-3501-a1c6-41a50f123042 | -7.50075 | -55.37048 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d094b22-753f-32d6-947d-12881bfbe064 | -11.09534 | -46.15852 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1584349b-a896-3472-9777-fab5171e18b9 | -6.55381 | -58.52532 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ec1fb71-31be-380f-8bd8-16e49d6c89d9 | -8.57364 | -55.28069 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3547b22a-863b-3eb0-92b7-877e811c782d | -6.6499 | -56.26889 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a01ad03-0a17-3558-9c54-9484a763adc9 | -9.9459 | -48.34614 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51113393-8ba7-3bef-a044-1d77864fc109 | -10.92353 | -51.09041 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a80ab4cb-042e-3212-9ebe-2b781bcad2ab | -9.65741 | -48.32106 | 2026-08-25 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73587c85-a41f-311a-8d66-5d79fb4526e4 | -6.15227 | -57.94186 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 981dad98-432c-36ee-96de-0dfe5b9f411e | -10.93219 | -51.06046 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b48e4388-125c-3db8-911e-34530dc40da4 | -6.83502 | -52.51272 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1df8dffb-91b9-3b43-9d1b-52d3c8cd2fff | -12.14758 | -50.61238 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b0e17a7-52ed-33f2-9ff4-eadf29112e8d | -12.86199 | -48.49578 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54848bae-e2f1-36c0-9580-008ecdc4b48e | -6.79214 | -59.8158 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 680567e5-c92c-3e92-95a0-d6513fe2a8e5 | -7.01414 | -59.24049 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6deca61-f2c0-39a0-8b75-3dec21999c40 | -7.00678 | -59.24308 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2d88197-637c-34ae-9a8d-93a0ade236e3 | -8.52007 | -55.34992 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6877fc9c-0d53-38fb-812f-10a2e2f96fbf | -6.80913 | -59.68645 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb06d840-b481-3b52-81d3-e6938c22f962 | -12.77006 | -48.36942 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91b40636-9696-32f1-9073-09536301ac7d | -7.54081 | -61.29823 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d923823e-f5e1-3677-9400-4bdeeb81b0d2 | -6.80239 | -59.66225 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a12acd8d-136c-3864-8706-dacebac58b90 | -10.36888 | -45.05841 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7c948390-72e5-3fa1-ac85-99a9c49fb654 | -7.00783 | -59.25817 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ae45058-49a4-3337-982b-506d035476bd | -13.35581 | -48.20029 | 2026-08-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29ac7e69-0f13-325b-b2e2-0a4a2b7262fd | -6.25731 | -55.39517 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 486559dc-7299-304e-ace6-45488875c6f0 | -8.80582 | -62.32837 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 632cf914-23c2-37f3-a764-ed9826352617 | -5.78168 | -59.17028 | 2026-08-25 05:12:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 666f20d4-df7b-35c2-ad80-708a3578fdd1 | -6.86394 | -59.03474 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ef2a55b-bbe0-3f9d-97c4-2ab0c9cea57b | -6.35126 | -55.86219 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80558a22-4b4b-33c0-987b-7e348df976ce | -10.37495 | -45.06719 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dc58cdee-96a3-37e3-b243-746c77e8a1ac | -7.34003 | -55.67384 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1e0ac1c-c6a0-3d31-af47-25464377942b | -6.51834 | -55.22451 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9344ef2-4631-3fb1-9579-7dabaa165a7d | -6.81374 | -59.59093 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee2ca05c-0c0d-3f35-9136-6a97adeb2989 | -6.56186 | -56.553 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb8e7ba4-1c7c-3237-9e4c-6d801100dc28 | -6.80105 | -59.6043 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ff0def4d-e181-3e14-8eb7-4ce5c54ab4e6 | -8.6222 | -54.70858 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5b87ab1-f7da-36f6-973e-ef8973111466 | -6.55006 | -55.14571 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76432449-dfc3-3e6b-a4e2-d5f9cb0b0ffd | -10.06037 | -48.45373 | 2026-08-25 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd61e415-6339-389d-a2cd-a1dbb8f6a02c | -7.54449 | -61.29883 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ac21219-a6b4-34ef-b4e3-17b0016b9f73 | -11.09619 | -46.15582 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7359fa7-6087-3c53-8442-e780203e3a26 | -6.53594 | -58.3138 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d64e5aa-7c47-3e5b-a66e-9042b7480664 | -6.12596 | -57.71791 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 412bf923-061b-31e5-970a-8f73421d2783 | -6.81047 | -58.66395 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fbc9c0c-6145-3f07-af30-dd6cb4ff32fc | -11.11749 | -49.88341 | 2026-08-25 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 661066e6-6ff6-30df-89e0-77bb869993a1 | -9.96641 | -48.31981 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da2c1096-81e8-3f45-a0de-5d6918807c69 | -7.2051 | -60.61449 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f7b827f9-6bb3-3328-ae4a-5485114798f7 | -9.53749 | -49.27297 | 2026-08-25 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 866c1523-a012-3a3c-be2a-28faab5c821c | -8.57529 | -54.85207 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e7f1645-48fa-339e-8721-148c42afe51f | -7.00339 | -59.24255 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 752aabab-def2-3908-8df6-c12849a714ea | -6.82106 | -59.41284 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c7ccc0e-fcb7-37d3-8f88-5b8402475eca | -6.12573 | -57.82774 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6dc62bc-a98c-3724-871c-edacc41d2506 | -7.01239 | -59.25143 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beedd2a6-8fb8-3c66-ac1e-4c4d87bc73c5 | -6.15336 | -57.93491 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41e1c1fc-b3e8-3561-a26a-6e994fba1c27 | -6.12188 | -57.83068 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 542a9270-11b0-357d-840f-a827db2667e6 | -13.34991 | -48.19945 | 2026-08-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e454acc-2841-32b7-a708-22331b6def75 | -6.35526 | -54.77453 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ac68631-9861-3ed2-9b04-12b35c90c127 | -10.56149 | -50.43188 | 2026-08-25 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce462645-8b7d-3d71-a9ef-00bb4d2fbfdb | -12.70742 | -48.40087 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README51.md)
