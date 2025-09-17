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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77b936a5-8369-365f-8938-8e78e67ab8f6 | -9.52252 | -66.59698 | 2025-09-17 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 207dec7b-8bd9-3689-93ef-92bb65069b30 | -9.5627 | -67.46 | 2025-09-17 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0bacfba-313b-3713-b6fe-bc43ace212a1 | -7.50218 | -63.50548 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdc79353-6d16-3eda-b08f-583e022cbb72 | -7.50523 | -63.51047 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bff25d0c-f5e5-34d5-bd84-24a1a13bd132 | -7.49799 | -63.7217 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d38360d0-926c-3f1e-ba88-136a6c855580 | -10.0515 | -68.45033 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9138c5f-85a8-3387-8c4c-24900754f22e | -7.50903 | -63.72336 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f55c955-3724-3dbb-80ac-8a1f8a5954b9 | -7.9418 | -67.27315 | 2025-09-17 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0a8c305-c287-3bf2-9143-375973388dcf | -7.56885 | -67.38207 | 2025-09-17 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0852c56-0e09-391d-9e7e-485b9f39bc6d | -10.05485 | -68.45087 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d771bc20-167c-3908-83d5-0db2eb1da442 | -9.38094 | -68.77404 | 2025-09-17 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ceccd4ad-62b1-3041-a8a5-c165c21af0e8 | -10.48057 | -69.53349 | 2025-09-17 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90cee1ae-968a-3736-9f2f-13c2954c3185 | -7.53751 | -63.60773 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a0482c33-06cc-3e20-a53d-b99c216bd1ee | -10.17018 | -68.42941 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9adf8043-b229-3588-b210-7100ad2b47b3 | -8.71435 | -62.4412 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f3ee89c-3e68-3093-be5f-dae285243227 | -8.7759 | -62.83699 | 2025-09-17 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3333a5a0-bf24-3c0f-9f64-5a8f7bb1927a | -7.56829 | -67.38555 | 2025-09-17 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ae2de35-5258-3f71-8007-b333894c9ff5 | -8.02435 | -67.26165 | 2025-09-17 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdfe1c16-121b-3119-91a0-1568684e82dd | -10.21313 | -69.05005 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1bc5647-33de-3d8a-b1d6-355378d85895 | -10.74788 | -69.09254 | 2025-09-17 05:53:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4de3ee5-7e5d-3d56-84e3-dcc8d7a94edb | -7.53677 | -63.37844 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c7a345c-6538-3c3c-967b-14092a100176 | -7.52946 | -63.61099 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31a7d9a2-5824-3eac-9257-8a7c617008f0 | -7.53381 | -63.60717 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0fc0891-1790-38d9-89c4-f436d62cf088 | -8.71838 | -62.4418 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab4dbc73-112c-340c-bc28-86286b6fd3e8 | -11.79646 | -62.73997 | 2025-09-17 05:53:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bf651e9-6893-3c61-a10e-29ab6a43c3ce | -8.71787 | -62.44531 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d9e5920-942f-33fa-b821-00938c34db93 | -11.79232 | -62.73939 | 2025-09-17 05:53:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b678df40-9583-3e1f-977a-01f54478eab3 | -8.33198 | -67.31042 | 2025-09-17 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea995d35-f6fe-3d49-b37a-454964dd01e5 | -11.84348 | -63.22756 | 2025-09-17 05:53:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a37ecb71-058d-31a1-86c8-ef7d6457bec8 | -10.05094 | -68.45387 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c3903fd-cb2f-302e-8a63-54f387214e73 | -7.8443 | -72.8509 | 2025-09-17 05:53:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c381d5c0-b6b0-3084-a04b-79f0364e0cf7 | -7.5059 | -63.50605 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2851f215-530b-3eb1-82db-1a8ebfab90f6 | -9.62459 | -67.40871 | 2025-09-17 05:53:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2daa17e5-004a-3598-8e5b-f80a1aaae5bc | -7.50839 | -63.72766 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4db74a73-3e12-37e5-aed0-a72f209bd2fc | -10.17352 | -68.42995 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad90314-f233-34a6-9da1-7a1407c2a1ef | -8.71941 | -62.43476 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b64b227b-551a-3326-a127-024558fabc3a | -7.53316 | -63.61154 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6e9c42d-65e4-362f-9180-30d82c75bd9d | -7.53668 | -63.38078 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cd8973a-d10d-3d7f-a393-3bd6082c3c38 | -8.65229 | -62.67165 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f4653b3-aa6c-3ffb-92fd-d7ff042ddc94 | -10.8034 | -68.68196 | 2025-09-17 05:53:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3931c4bd-b972-356f-8937-efe6699e8dad | -8.71486 | -62.43769 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f0b19a5-4c39-39a7-af6f-835db1f74788 | -10.21254 | -69.05367 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db60b334-18cd-3396-95a4-ddb4aeca0a5b | -10.89226 | -68.21011 | 2025-09-17 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07953480-8fb1-39a1-af9e-42ef8f8661cb | -7.50167 | -63.72226 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 345b26da-36e8-30b4-9727-d1a0f183913f | -12.59519 | -62.95975 | 2025-09-17 05:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5322c4c5-db1b-3dd4-a2f4-88136faa381d | -6.9156 | -63.02939 | 2025-09-17 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 236ccbe7-775e-3986-9ba2-8247a5cda2e6 | -10.05428 | -68.45441 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f279f190-d1b9-3960-9cf5-ed3bdfdcedb5 | -8.72293 | -62.4389 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b34ade4-872a-32cf-9b5a-d91c10860d35 | -10.88723 | -68.24181 | 2025-09-17 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67b2a001-58e9-3dda-8c2a-9d0e06931168 | -7.56667 | -67.38141 | 2025-09-17 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 785e5ad9-e528-3c88-a904-ce5f65e1fa96 | -8.65626 | -62.67224 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017f41f1-b2f5-3e59-945b-2bc0635cf95b | -7.53609 | -63.38296 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cc669d9-1ec7-3bc1-8884-72eb18f2fdad | -7.53011 | -63.6066 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea1fdccc-f05a-3d87-b1cb-b580a969b268 | -9.56215 | -67.4635 | 2025-09-17 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d33616e2-314d-38f8-a7c1-62e52dab8aab | -8.77983 | -62.83758 | 2025-09-17 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf92b4a-18cc-36b6-9c76-5aae4a6f6862 | -8.11334 | -63.69375 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffc8e822-55b6-367a-ad25-fb306d75e569 | -10.60565 | -69.25906 | 2025-09-17 05:53:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b03879-faf6-3621-a65f-4f28cafffee9 | -7.50535 | -63.7228 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d5803d9-b946-367b-a468-7ba515f3886c | -8.7189 | -62.43828 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b0beb46-9f8b-3e5e-9ae5-21ce59c540d1 | -10.06425 | -68.47787 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163cfb89-cf30-3700-8229-1c6528d256b2 | -14.78497 | -60.22797 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a80e07c1-c691-38a4-acf4-2b77e3c22db7 | -14.78463 | -60.23077 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3706738a-eb9e-3491-9bef-4626503a7324 | -14.77339 | -60.23795 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b26307d-13ea-34be-a828-b00b729eab81 | -14.78757 | -60.20662 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf0fc1e0-db70-34e8-b887-1ae81f166cd6 | -14.78719 | -60.20976 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae160f9a-ea32-3599-ad0d-db60ad1a65bc | -14.78126 | -60.21584 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82650989-fc94-357a-8def-671075447dd7 | -14.77303 | -60.24096 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6d7fef9-b043-37da-98f9-9fec1b284aab | -14.78088 | -60.21893 | 2025-09-17 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c32911d8-14f0-3d64-92d2-cab91b18864a | -18.0303 | -50.9385 | 2025-09-17 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| ab211162-353d-317e-8009-3aaad6539ef0 | -6.87461 | -43.95939 | 2025-09-17 06:03:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9a8b827d-ce52-3e9c-8872-e0dc9dee7b5f | -7.82485 | -46.15135 | 2025-09-17 06:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e2148280-33c0-39ae-95df-c6aad6b391af | -7.58269 | -44.57623 | 2025-09-17 06:03:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e96be839-b8ec-3c7b-9ee5-018d57d604e4 | -7.26707 | -46.58731 | 2025-09-17 06:03:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a7c86389-53e2-3be2-b1d3-b93388e0285e | -2.9194 | -48.30113 | 2025-09-17 06:03:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| cb147a82-8199-3041-9631-5be7957156b2 | -6.20817 | -45.12656 | 2025-09-17 06:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 20001cde-1c29-3abc-bff6-37e046cecf77 | -6.1902 | -45.11722 | 2025-09-17 06:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 90e234c9-0694-3c44-a864-772905152451 | -6.39544 | -43.35523 | 2025-09-17 06:03:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5326cd62-e4ca-3101-b680-1777ac870ef9 | -7.57822 | -44.5826 | 2025-09-17 06:03:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ce22be90-4b9e-32eb-8662-56b799c07c56 | -7.58082 | -44.58987 | 2025-09-17 06:03:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 248e8984-929f-3877-82e8-9e59437f358c | -7.26854 | -46.57724 | 2025-09-17 06:03:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81793ee3-c88c-3a84-8ca0-3c156bb0f501 | -8.15717 | -46.74507 | 2025-09-17 06:03:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e6b6a87-7ab0-3e62-8143-c03645f9c55a | -7.88423 | -48.15478 | 2025-09-17 06:03:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4c006b3c-a191-350b-861a-735fff97cb26 | -8.14779 | -46.74373 | 2025-09-17 06:03:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 13586850-ff06-3153-948a-5f2f79340311 | -8.56506 | -46.33806 | 2025-09-17 06:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c74ff2fd-9fda-39cd-9484-34115b124c00 | -7.41393 | -49.98871 | 2025-09-17 06:03:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 11edb1dd-d404-3274-a485-52ad17137c31 | -2.91807 | -48.30989 | 2025-09-17 06:03:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8b3bb00c-ac7d-3bdf-bbf2-ab5302258e41 | -3.23831 | -46.78764 | 2025-09-17 06:03:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70de1f1f-1f3f-3917-aec4-232f68ad07aa | -7.76815 | -44.72413 | 2025-09-17 06:03:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a9511461-15ad-3dca-a84a-1632ecf16f0d | -4.05627 | -47.49852 | 2025-09-17 06:03:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 48009fc1-19de-3e63-a2db-8f6e68904882 | -5.81416 | -46.36101 | 2025-09-17 06:03:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 123fb165-ba5d-3a32-a7f4-843615876093 | -9.06799 | -44.9491 | 2025-09-17 06:03:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7ffdc751-f125-34e8-9761-9f5c38cebe21 | -5.76928 | -45.90106 | 2025-09-17 06:03:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1e8b2ef4-b433-31f7-b85a-84434b0b2191 | -7.82332 | -46.16219 | 2025-09-17 06:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90278917-dea7-3dc1-af8b-4d3ed608d4cf | -6.60585 | -45.57816 | 2025-09-17 06:03:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d32bbe87-eb17-3aca-8923-6cf6b15e1157 | -6.20029 | -45.11882 | 2025-09-17 06:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c679b73b-4e9d-3c64-a5cb-75a13b82e004 | -6.67178 | -46.30365 | 2025-09-17 06:03:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c356e32b-c31b-3a89-a6a8-0b071931ada7 | -9.05899 | -47.0186 | 2025-09-17 06:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dedbdcf4-1a39-3574-81c6-603f56a3fd58 | -6.19858 | -45.13052 | 2025-09-17 06:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7e36b8a2-bdb9-3512-9dc8-e6ecc9f910f4 | -2.8307 | -48.64864 | 2025-09-17 06:03:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e46fcc55-8017-32c9-8a51-206c4f6bee37 | -2.92072 | -48.29236 | 2025-09-17 06:03:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README55.md)
