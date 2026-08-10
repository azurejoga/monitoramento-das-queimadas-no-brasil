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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e4d9719-3f78-31ff-a8fd-b6a1b8374912 | 2.35727 | -60.1427 | 2026-08-10 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4be7d8e-1428-343c-b09c-a1de8b415895 | -3.93047 | -59.1327 | 2026-08-10 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80316dc5-ceca-301e-a045-8bd2a21317e9 | -2.90659 | -54.15345 | 2026-08-10 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffabaacc-63dc-3973-b036-073bf60fa087 | -4.30315 | -59.47022 | 2026-08-10 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4859fed6-f330-3e72-bc81-24a9d3543b47 | -2.90827 | -54.15096 | 2026-08-10 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5a58814-7c23-30e2-8400-cd3022ebbed5 | 2.3609 | -60.14204 | 2026-08-10 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f71909a3-535a-3a2a-88cf-5dabc848a7ae | -2.90721 | -54.14925 | 2026-08-10 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4cc830e-3aa5-3328-9082-f24a8981b321 | -3.93167 | -59.12479 | 2026-08-10 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ec1029f-6852-3e37-bb33-dce2a7653ebb | 2.67815 | -60.06283 | 2026-08-10 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc1e5f1-3300-326a-a129-cd69fa44b1fd | -4.40322 | -54.78701 | 2026-08-10 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64b12eb7-ebde-3e63-b8db-64a35fffd044 | -2.35858 | -67.21498 | 2026-08-10 05:46:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f99cf29-8876-311c-8ad8-9aaf4977608a | -4.39692 | -54.78989 | 2026-08-10 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34f2e233-2e21-38cb-9755-1fa3372bfa7b | -4.86422 | -55.82104 | 2026-08-10 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db8dec9d-59e7-368b-8f16-31d85c4c563d | -4.61749 | -61.24522 | 2026-08-10 05:46:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4683ddc4-ceb0-39af-bfe8-9109129b6082 | -4.39751 | -54.78588 | 2026-08-10 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e2f7ac7-b673-3ae8-bcdb-0490b23a06bf | -4.30259 | -59.474 | 2026-08-10 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 803a845f-bb3e-37e4-b24a-46cfed41dc41 | -2.61859 | -59.9024 | 2026-08-10 05:46:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 700fb652-b5d9-3aec-adce-3d71f5cca03d | -3.93531 | -59.12939 | 2026-08-10 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec88ebe5-6390-3dfe-9d77-23dc3b6fc13c | -2.3621 | -67.21555 | 2026-08-10 05:46:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 912c4009-b0d2-341f-ae14-3d08c8349173 | -2.90891 | -54.14677 | 2026-08-10 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 037a5093-154c-33e9-a9fc-2e05fe7dbdec | -7.14922 | -59.62328 | 2026-08-10 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 016bcb0f-92ab-3ec7-b1c6-cd0e4e0025d6 | -6.13963 | -57.71819 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1055c735-de85-3794-8a7f-5d010da3bc09 | -7.94025 | -63.45244 | 2026-08-10 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2475c9ab-0b2e-3924-83c0-e7a58e8e2c5b | -8.17059 | -61.51673 | 2026-08-10 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 003e3c10-0221-37bc-80d8-abb7fc6bd7f6 | -6.16412 | -57.9171 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38066fd0-f469-3e25-8318-09b00cf367a6 | -8.9458 | -60.52794 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 281ae731-1cab-3224-b372-1bd02f421f57 | -8.91089 | -63.97028 | 2026-08-10 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e58752f-da14-3520-a241-a8777b5bed48 | -6.87837 | -56.63524 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d4233fd-a05a-3de3-b985-069183e30f4f | -6.14312 | -57.72084 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c7710d70-8d36-3dce-a308-714af77439ed | -6.83639 | -56.40591 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28e8adbd-ae39-3222-992a-9a244fd49bee | -8.94331 | -60.51589 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9d9c71a-4c52-3bba-8bb3-ebb34b4e8967 | -8.94469 | -60.53554 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 024dfb29-3893-3c93-b95a-86151c23f630 | -6.85059 | -56.4048 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5835cd4f-2b94-3054-965b-95abf1230e85 | -6.81068 | -56.43343 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88ebc5c1-f90c-3b06-944f-4e84ccb977c9 | -6.84294 | -56.42101 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09300a4e-cf22-3df9-b93d-f611364a5d70 | -6.85194 | -56.41167 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d9a6b9b-4563-3e36-922d-75c38f64e4bc | -6.84076 | -56.41355 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd0bbc3a-92f3-368a-904f-adc0435cdce3 | -6.13826 | -57.72025 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7214e13d-8278-3137-97d7-c734eae66528 | -11.216 | -54.03475 | 2026-08-10 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 126a19c6-ecf5-325b-a9a3-c507b1c3c7dd | -6.84341 | -56.41755 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4211d2c4-8670-3acc-9b85-554ce2b6f7fe | -6.82911 | -56.41872 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb0a5b6-564b-35bb-a6dd-ba3ff6626b3c | -8.96102 | -60.55321 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6e0012bb-f6bb-3d0c-924f-5f402d8a2e07 | -8.68292 | -62.87023 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c3821d4-ed57-313a-8c6d-749afcb317ff | -8.16414 | -61.51834 | 2026-08-10 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68bc2689-70c3-3e1f-abda-fab7c44b7b47 | -8.67509 | -62.8733 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3f71c56-aa36-30a5-9f8d-1f6583cd9b9a | -6.83631 | -58.93483 | 2026-08-10 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ec52cad-8abe-3456-a2be-75814e0991a4 | -6.84269 | -56.40004 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d26b7cc-8a44-352e-b409-aa7dc98dbe76 | -11.21671 | -54.02892 | 2026-08-10 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b94752d2-ed94-3557-93b3-baaaafd2f46d | -6.15934 | -57.91645 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6e4c076-1834-38ac-bb72-ecfa2b2ab1ad | -7.69127 | -55.16529 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58296618-c0e2-3a29-b8dd-e8f68dcdf398 | -6.13978 | -57.70947 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9f097e7d-d3c9-303c-9dd0-f49ae39ac8a5 | -8.95995 | -60.56087 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83e9012f-795f-3826-825b-37fe59c5e255 | -6.16489 | -57.91181 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbf4aaa7-8db4-3718-993a-531e6051809a | -6.84706 | -56.40763 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ae8e4ab-e720-31f0-b458-9744871ffa73 | -10.93239 | -57.11667 | 2026-08-10 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51a00a1a-49a7-3b48-97a2-6635b40c0d37 | -7.69658 | -55.17035 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a5dcefc-1dc3-3b6b-b15e-49d358f60fde | -8.67869 | -62.87384 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfbc6f44-653d-3f15-9606-c6639c043c17 | -6.81115 | -56.4301 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163da950-7c89-370f-b2ed-fbb8e40ff98e | -7.69183 | -55.16104 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28f06155-3bd9-3c72-a00f-ba1c753af673 | -8.9589 | -60.5684 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41c3f3b7-c23a-3be2-8d13-75172d7145ec | -8.95606 | -60.5449 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99dcf41a-2f2e-34b1-97e6-15de11d29cf8 | -6.84124 | -56.41014 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51b02d90-8d13-32d8-bb0f-5d42f1bd5ec6 | -11.20939 | -54.0341 | 2026-08-10 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b684202b-4b8f-3024-a2ad-91dd2cd3f859 | -6.85097 | -56.41842 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1491eca4-15a0-3dd1-ae06-758613e4cf42 | -6.83542 | -56.41275 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47dd87b4-045b-3123-b334-6dfb0b188b04 | -8.95633 | -60.55643 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 58f17a19-ef57-3f34-80b8-cb4b5c2ecaeb | -6.13558 | -57.71218 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4116b606-d542-3368-aea5-8016a3577875 | -6.85339 | -56.40155 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4050a64c-d4e6-3dfb-8ab9-13b935aa357a | -8.95687 | -60.55259 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 431ceaf7-f287-35d7-93bc-4b30bc1e3af8 | -8.166 | -61.521 | 2026-08-10 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f25d1353-aec5-31f8-bea3-2b6ce683cb33 | -8.62973 | -66.53687 | 2026-08-10 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bdb1cbe-f424-3351-bcff-970396fdfd8b | -6.84172 | -56.40678 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e1caa64-9852-3d34-9923-5dc2d242d5ea | -6.84561 | -56.41772 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15fc07be-82c8-3553-b2f4-b097ffb7a068 | -6.83805 | -56.41682 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb7081ab-a986-3fe8-ad05-dd30eff16fc6 | -8.89714 | -60.57109 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7cb24f3e-1e23-3698-9fe2-1023ad3d05e3 | -8.51114 | -63.35929 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e725ea89-0385-3cd1-b043-48aa82d4ee0f | -6.83759 | -56.42028 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c9c259-567a-3617-a69e-adb08b7e0a5e | -7.54202 | -55.57396 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8039b5e4-3ea8-39c5-b0c0-b74b71b13fa9 | -8.96732 | -60.53857 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8dfa872-9964-3c33-834b-29ecdcb6968e | -8.89082 | -60.58563 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95cb1545-f8a6-3a82-a74a-32727e5795f0 | -9.9034 | -67.00924 | 2026-08-10 05:48:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3fe2b8c-bfc5-3901-8067-a7bed94f04c1 | -8.95015 | -60.53989 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b92ea864-4b20-3ce3-bcb3-cc1e5c7e0c7b | -6.84434 | -56.41068 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff4220fd-3f7f-3371-8888-7a7fd1f3ada0 | -8.16673 | -61.51616 | 2026-08-10 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4ed86d7-37ae-3579-8778-de2a6091809e | -8.9483 | -60.53992 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| aeb8a295-5663-3f11-91f3-dc04c31f3f6c | -8.89245 | -60.57428 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d03a5b5f-813f-3d60-9a3f-80699111742c | -8.95414 | -60.60234 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9afe08f2-6327-3b1f-8c96-32c105ab1c64 | -8.95467 | -60.59856 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f52ce4e-834b-301a-aace-80ba0a8e6c6b | -8.89551 | -60.58245 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0bbe583c-54ac-3809-8eac-d1f6ea9655ea | -10.93871 | -57.11008 | 2026-08-10 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0b17acb-5a89-3aa1-bf37-ff77302d7225 | -11.22137 | -54.03016 | 2026-08-10 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 379a1ac9-6966-3fc1-a593-1a8e375e2c4b | -6.84802 | -56.40089 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad79f9fd-f15f-3de4-844b-e1fb916fc064 | -7.54826 | -55.57092 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f0c7233-858d-3b54-bb1e-eb494207c7ea | -8.89443 | -60.58998 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac7f2536-a9cc-3743-be56-71fb2c10093c | -8.02308 | -55.1162 | 2026-08-10 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cd5eb8e-ab36-36b9-936c-216c31a4c314 | -6.83714 | -56.4236 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22e2c572-93f4-3de3-baa6-8da7f8398388 | -6.87746 | -56.64171 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7ba6b5e-9c86-3f28-b4ee-1b31dcb33d62 | -8.95828 | -60.60298 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 984280a9-464b-3639-b6ff-ed586c217507 | -8.8919 | -60.57808 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca0615c8-e507-3c2c-83bb-afcaeea91dda | -6.85106 | -56.40136 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README20.md)
