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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8b19b63-9219-3633-b47d-f3f73e6fb2fc | -10.37099 | -62.56101 | 2025-08-28 05:25:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 159e05b8-45f4-3fd3-bdb7-989cac1d1a33 | -10.81219 | -60.76877 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6db9d8ac-5796-31ef-94f9-b70451b02c03 | -8.95276 | -65.95052 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf334b21-1da9-3deb-9684-4e3958cc97af | -10.84513 | -54.02748 | 2025-08-28 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa68146d-2bdf-3a29-bf2a-e2781ce217e1 | -8.34889 | -62.93522 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a2128c8-e2ff-31c5-a289-2cfbdc4e864e | -10.80551 | -60.7677 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| fe45e1fe-31f6-35a3-a746-c66b7a5d0bf3 | -9.16835 | -59.55411 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a4bcb93-e36c-3456-860c-863fdae7a8b4 | -9.19343 | -59.64416 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63d03c2c-d10c-33ff-b68e-917f6b02c957 | -9.01866 | -65.70988 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0e8cf06-c526-3f53-bc1b-8edc8618b232 | -8.34669 | -62.92709 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b3ff468-e203-3d8f-8488-a5b375ad8e11 | -6.0072 | -57.85236 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21536530-829a-3107-b5f3-4280537de2c1 | -9.54025 | -62.40385 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 581a800c-962c-3c8c-ac83-6a4280c07549 | -8.95294 | -63.36545 | 2025-08-28 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 937a803a-fced-37ba-ba69-07ed9a591a42 | -8.10053 | -71.24236 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa84664-716e-3a39-979d-a8d52f49fd18 | -7.35914 | -57.62187 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3833a85-5e26-3183-ae99-ec04a1984fc2 | -10.79605 | -60.76256 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5313133-0cfb-3b58-9d14-320dc6832a9d | -9.41144 | -60.51147 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8020a27-e78c-395a-b7d5-ebdde26f0d98 | -13.00508 | -56.90077 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 985f7dcc-eb51-3fcc-adcc-b082b6ee2a8f | -9.53966 | -62.40746 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d13c334-4802-32cf-a221-c8f80e816597 | -10.47085 | -57.95589 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bea34c3c-e706-398f-8627-2218aa9a357b | -12.80852 | -48.14941 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0477757-e2ec-37af-9fdd-675ba03f0c66 | -8.09924 | -71.24919 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 442b054a-1f5a-385b-9f7b-c054fcb29214 | -9.1404 | -65.77505 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f523f019-23d6-307c-818d-7691f78ffede | -10.8406 | -60.80596 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ec664a7-8a57-304f-9171-12e4134af42e | -5.99682 | -57.84767 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e441b5ec-de0d-33ef-8e35-19456913a4dd | -6.00324 | -57.85268 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a80416e8-3500-3f7e-988b-dcaa95db4d3b | -9.01472 | -65.70918 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8e43b15-c8ea-37b2-9fd8-490369d86b45 | -9.11716 | -65.79198 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14ee0943-de0f-3e24-900f-29d367ab3d1f | -9.40316 | -60.54263 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22c69a1b-97fc-37a3-a7f4-d94e7248f87d | -7.4452 | -63.15938 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| addd0239-8d43-35f1-b115-36d2badc6870 | -10.08825 | -68.46429 | 2025-08-28 05:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a61ad68-8032-35ee-a0c2-66d6860029bf | -5.99972 | -57.85213 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff38add8-0c1f-3553-aa33-221d12fcc2fa | -9.469 | -57.84161 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1243a70f-78b8-39ae-8f35-b6789f207fa7 | -11.36376 | -63.26459 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb1767ec-b66a-3802-a026-4b0a35ed31c6 | -8.87475 | -60.76807 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f845a8d-61c0-3e25-bd60-1c283e0dd0f5 | -9.1095 | -60.3236 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48139f23-fb37-3946-bbe1-a8157cd23181 | -9.12903 | -65.79405 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f66d9ed4-0571-36ce-809a-74379ea4da5a | -9.46391 | -60.30619 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54daaf16-320d-3f3e-b818-040dfb5bfb24 | -9.14605 | -62.35505 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cd1c2c6-e1cd-3fb4-97e2-2c03d8d27bba | -8.23391 | -61.46077 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72513fc0-59f4-3567-b319-a8bd575173d7 | -10.47239 | -68.15192 | 2025-08-28 05:25:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d182f78-ecef-3b20-b58f-25d39e01eb5f | -9.13866 | -65.78532 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e989dd7-e8af-3685-a15e-e47559b8a282 | -11.22964 | -55.06222 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 911ad0e9-f6d1-312e-86c9-79f7eb2643f2 | -9.12973 | -65.28912 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe3a9248-926c-3d88-bc9b-422b4f238802 | -9.46781 | -60.30318 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87bf74fb-df33-38f1-9d58-dbcb555b4b27 | -7.35235 | -59.66204 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69336862-debd-3b2f-b2f3-5a5af8b701f2 | -9.02347 | -65.70547 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20e5ba85-2480-357e-a3c6-70bbc3ee0373 | -10.15364 | -64.24982 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 27d9011f-6f94-3c7e-90ab-30630f16043b | -9.22963 | -59.67948 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72c294d2-c363-3450-b82b-4cb63575bc30 | -8.62863 | -62.61587 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b8251c-2bd4-3f09-aaf4-89f1aec91e46 | -7.54184 | -63.85582 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84a20e29-efdc-37a5-a765-e9c03b84bf67 | -6.23899 | -60.01658 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb5a6db-cb04-3503-a0cf-1e6fb006d1d9 | -12.22637 | -64.2285 | 2025-08-28 05:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ecd2ee4b-c418-3431-90bb-a71c2a53321b | -14.34396 | -53.35258 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd437c4c-c666-34b3-8738-8728fe6326e5 | -15.60876 | -52.72369 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b50543d-aa92-349d-a4df-03891c2c6e8e | -14.29194 | -53.04556 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0b62924a-000d-34e2-a884-0c0f4bb8489f | -14.4377 | -53.19441 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e5a99b7-3ec5-3547-b859-bd02180eaed0 | -14.3347 | -53.3415 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5078f304-5d64-3f16-a532-528d2646e04f | -15.62661 | -52.75437 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8dfb736-0260-389f-b227-e77d91eef092 | -14.28885 | -53.05119 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 62db1b93-4564-3ad0-a546-cde0562500eb | -14.34982 | -53.3519 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6af9a488-6217-3c08-906d-39a64ed42062 | -14.28623 | -53.04803 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a58bfe3e-7d4d-3f9d-b34b-7e0b7ad30f9b | -14.28963 | -53.04448 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 55539db5-9da2-373c-b026-ba5e4ffaf19d | -15.68151 | -52.76429 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d7caa01-b686-3de1-95a3-0f83367892ef | -14.30936 | -60.38269 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68e15413-85d5-3c8b-8f59-668810273e41 | -15.61611 | -56.1202 | 2025-08-28 05:27:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9028020-b501-350a-80ee-b4e862626aa2 | -14.3128 | -60.38317 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c141b657-95a0-3fad-b497-a8443f61d1b9 | -14.60383 | -54.7979 | 2025-08-28 05:27:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ad5b4ae-8840-3aa0-8a38-6c83c3d21a65 | -14.33286 | -53.26912 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08993ebd-b6c2-3071-b40a-c618014e5acf | -14.26863 | -53.05938 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24a020e6-4e3e-305b-83ff-7d2b0d262af7 | -15.60774 | -52.72233 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cf37433-84c7-37af-8b37-807208995c03 | -14.30997 | -60.355 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e90e9f-3ae5-3ca0-a8e3-4fcd111b00ca | -14.77892 | -59.71119 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d48cfc5f-6627-35d3-81b4-15516845264d | -14.36245 | -52.08171 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0c06bb9d-689b-3328-aa5a-98121deb40fb | -14.3134 | -60.35564 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb93907c-9482-318d-ab4b-f51e00e598b8 | -14.33004 | -51.90847 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8122ce1d-efa3-3032-81ef-f76fe1766c13 | -14.78541 | -59.71619 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26638b3c-8f66-396e-8c81-4b9cded6cf4d | -14.28664 | -53.04469 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc00509c-df21-3797-b24f-c669e844bded | -14.26737 | -53.06973 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7d953a2-24aa-37d8-a314-98cc3d3bfc41 | -15.68193 | -52.76069 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b57d34df-3bae-3f31-a1f4-5113cb54d7cc | -14.76721 | -59.74167 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba3274f3-65ab-3172-806f-f50ed535610b | -14.29236 | -53.04216 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4900a4ec-ce27-3b5c-9127-9acbff6ccd7f | -16.01254 | -59.92677 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a604485-469d-34c4-91f3-572bd99118ed | -14.32763 | -53.2683 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32a50780-d075-3672-9b4a-ca5a05664405 | -14.36198 | -52.08572 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 129b0dfe-d7fd-3f56-ab9b-613cd8df9e3c | -17.77757 | -48.49826 | 2025-08-28 05:27:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f75717d-5f04-361c-baf7-8f203e4d5599 | -14.3305 | -51.90434 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7c1dccf-e7e6-31cd-b3cd-0b91cc9377d3 | -14.26821 | -53.06283 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd401780-9a57-32b7-9622-ae3d99cef2fb | -14.31681 | -60.35631 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5a09f3c-af8c-3e57-ae79-a65c7287acc3 | -14.28924 | -53.04784 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 25f50386-caf8-34da-a6e6-cf4be4aeb16f | -14.31906 | -60.3648 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef651d91-73bb-3e68-ad88-2b0a868f11fc | -14.32029 | -53.05968 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a68e72f-ad0c-328c-a39f-c37636d903d5 | -14.33531 | -51.91345 | 2025-08-28 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3109726-f1f5-39c8-a587-a2f9379f97c4 | -15.62701 | -52.75082 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c79dc11d-13d7-3030-9201-d0e1d7a8ee27 | -14.28582 | -53.05138 | 2025-08-28 05:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 84edac84-709b-33f8-9301-89a0dae0667f | -14.78187 | -59.71574 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a466fbc-c5d5-3d86-9b85-d26b01e45667 | -15.66735 | -52.7411 | 2025-08-28 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11a7fe82-f14f-3be5-a800-fce899c3e16b | -14.77133 | -59.73824 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07a750e5-bcd2-3138-a930-b82d0b6fad44 | -14.31055 | -60.35115 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f13f1ec5-c2f9-3c82-86ad-0f741eff9837 | -14.76366 | -59.74126 | 2025-08-28 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README79.md)
