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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f57a114-d21c-38e7-ba90-e6320cfafc65 | -9.51197 | -60.53671 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 72f63579-d294-3730-8c7f-6b8ffc9f17e5 | -8.9896 | -60.50539 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8405941c-1b02-3a11-8940-92c3468cee5d | -7.92946 | -61.73673 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 092348dd-bb79-38b4-a984-1cbad7cbd644 | -8.98549 | -60.50317 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 58eed11e-dd67-35b4-8266-509baac48ab7 | -9.50347 | -60.55787 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b67c79e2-2e40-3372-bcfb-72fbb4043c3a | -7.90718 | -61.74478 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9d6fce4-cc6c-3057-829b-64288b4b3407 | -8.46728 | -64.06558 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2883613a-0f8c-3598-9fde-540b9a78bff4 | -9.15685 | -59.62911 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 671d8a78-75f2-3539-8a41-96a753b886ac | -7.94384 | -63.22113 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad8d818-2535-3b29-b7dc-15fab25c6d84 | -7.52648 | -61.37533 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a837ea3-1769-33ef-bb07-ad29044fcc74 | -7.59491 | -63.50101 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88739bf4-3340-31a6-92c3-1a2b4d731243 | -6.93537 | -59.55137 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4dcff292-7286-3be3-ac15-97e093ce73d2 | -9.18304 | -59.65498 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 985e3cc6-c000-3f17-94cb-ef3bae834d4d | -7.95207 | -63.2177 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eb07c22-d35f-360f-b3a8-1160d6eee132 | -9.16246 | -59.62433 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| be4ca211-b7e3-335f-af72-4e09e0f36fa8 | -8.99982 | -60.50051 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43f42e00-e547-30bd-8dcd-817be1f5d024 | -7.91023 | -61.75277 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c606d8c-0b6d-356d-8271-5afd6f044ce9 | -7.07865 | -59.23053 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7f25349-72a4-32a7-badf-eb5bbc6765f5 | -9.21874 | -59.66603 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae08a74-9547-3f93-9836-531d43804819 | -8.985 | -60.54113 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9704ea56-fbe9-3333-bf6f-402072eb0c62 | -9.50994 | -60.54442 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c96871c-b313-37dc-b22f-2fd4aebce0e5 | -6.95031 | -59.54831 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 579eefab-0e5a-3b1e-b89d-cc1760181e4a | -7.56651 | -61.42457 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0650133-e863-3bdb-be8d-b72f732ff5fa | -7.52478 | -61.32759 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd28f4c1-df27-38ad-af40-e5b642711dbc | -9.5112 | -60.53497 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3284d62f-7ee0-3506-9632-b6398b52aeea | -7.82101 | -61.33062 | 2025-08-16 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36bf6677-70c9-3d06-853c-b34db6262a77 | -7.9584 | -61.75631 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50be8ad0-2da4-30d2-a70a-e8df06bf66fd | -8.98233 | -60.52652 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 60169718-c2de-3697-a6a6-bad24338f6e8 | -7.61463 | -63.33492 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f8e51b9-b5d7-37b5-bfcb-44350c75189a | -9.22087 | -59.65002 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b049e109-710e-3497-b007-536304df1968 | -8.5598 | -63.92276 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dab783a-d9a9-3610-b2bd-1b320c5bdf57 | -8.96587 | -61.6783 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a60befbe-c438-3ab8-be3c-e5c27a12ec3c | -8.59787 | -63.89347 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1530659-aa17-32a1-b7f9-2b2bf25f6d1d | -6.66246 | -58.81896 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69fe680f-45b3-3637-8e9c-04f948b6f1d7 | -7.43771 | -60.0182 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f02cfda0-88a5-35eb-bded-40cc6d9b7f7c | -7.49954 | -61.38327 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2796a6fd-82eb-3bec-b9c3-7d3137e741c9 | -7.67883 | -63.31934 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4567d213-0d9e-304e-aaf4-fadc5db5d1e1 | -9.21448 | -59.64275 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8629b7c8-636a-3600-9940-5acea08808b4 | -9.18228 | -59.66043 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c9adaf8-9150-3abf-9043-31c0ca380f46 | -9.16998 | -59.64188 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6900fd43-1379-3cb6-8ea0-7c55a6a7e70e | -7.91598 | -61.74227 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c02843e5-921d-382b-a55a-fc829331ef0e | -7.6727 | -63.30927 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0bf5083a-6342-344f-8083-a1a6993ee3c6 | -6.94082 | -59.54704 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8852bdf6-19a5-31b2-a3bf-7559f9da2dea | -8.98626 | -60.53186 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 91bd6c4a-4248-36e7-974e-e6551b7ab04a | -6.87526 | -59.83849 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16b8ac95-418f-3525-931c-2c991cb3260a | -8.9825 | -60.5596 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c52d027-ddb3-3cb0-a662-afd2ec0144bf | -7.68017 | -63.31039 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3546653f-31a4-36b2-bbec-b0aed3853a2b | -8.98893 | -60.5464 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87fdb959-7cfd-34ac-a0f1-57272fb67ea3 | -9.00046 | -60.49586 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e64fd03-ff20-39ff-8c45-7ddb9bfb50cb | -7.49447 | -63.82922 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fca82f6-d849-3189-a040-bc90ce9c374e | -6.9539 | -59.52334 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b392901-dbfa-3b93-b2c9-b4971d59ef88 | -7.83457 | -62.99973 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c495a192-149b-31c7-854f-e820fcb49f4a | -8.99791 | -60.5146 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5b0433b-9975-3886-9548-65f18efe3a18 | -7.04199 | -59.6246 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 983b836e-0f8f-3f57-90ce-ec1ef15c973b | -9.17072 | -59.63646 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27cdc7d5-2218-3748-9407-4a3e512344ca | -7.94906 | -61.74707 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb7b0a5e-50f6-32bc-9032-58faf1675768 | -8.98942 | -60.50851 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7278b9a-884f-33e3-8043-b9d7426c384a | -7.94706 | -61.747 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e80640a6-d7b3-36ea-9d43-7485fca4af52 | -8.98485 | -60.50787 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b87c4bf7-6813-387d-bb65-f588e2e62b4e | -6.94845 | -59.52765 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 429bc8e5-9f1d-3454-a949-5c62a2068245 | -9.20697 | -59.64273 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4bc978a-8a91-3dde-b83d-cb12009861c9 | -9.50868 | -60.55382 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ce0e101-c10c-332f-b595-61f9840214ba | -7.43469 | -60.02901 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 722ddd5a-95bb-3c38-82b6-5822a4a64ab1 | -8.06024 | -70.58695 | 2025-08-16 05:50:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b886481-f515-32e1-985e-4ac36a22bb16 | -7.67203 | -63.31374 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bef8d04e-8f3e-3fe8-91ca-d7b93a64f6d8 | -8.78671 | -63.69534 | 2025-08-16 05:50:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30838f6a-99d5-35f6-8a83-62a8eaf18d82 | -8.99411 | -60.54248 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 362f29ab-eb6c-33ea-8e57-26161ac5a334 | -7.13022 | -59.65345 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85239edb-09cd-36a3-abcb-f28e36040be6 | -9.50804 | -60.53137 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 045d430a-c1ac-3d59-a35f-22bb3920dd16 | -6.95791 | -59.52916 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5abbc362-ec39-3af4-91f2-02edc31b2f88 | -7.62391 | -63.32934 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16c4480-f8e0-3803-813f-e3e5e49416a2 | -6.94225 | -59.5371 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd0dbd00-e409-3f96-ae24-d8d7ad5d22ca | -9.50723 | -60.52962 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 268c31c8-a76c-355a-8e5a-d84af3266521 | -7.64486 | -67.01291 | 2025-08-16 05:50:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adc0a419-572f-3106-a7f6-dcf1bdcbf9f6 | -7.94878 | -63.21487 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f20f3146-5194-3f59-88fb-3712537c18d2 | -8.99335 | -60.5139 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f754048-4e7b-39b7-a0f3-da5d3778512f | -7.88104 | -61.80887 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1bcc68d-5b88-3230-a6b1-521432cb269a | -9.50145 | -60.54491 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30fd6a6b-762b-316b-8318-4265c5e3aab3 | -7.91804 | -70.22485 | 2025-08-16 05:50:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c0c1870-75fb-3248-b476-70a3c72e1b84 | -7.43567 | -60.03221 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 568a0045-0abe-3129-9173-1b067d72a6b1 | -8.98956 | -60.5418 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 494139ba-8ed7-34c3-9ebc-0933a0ec1f7f | -6.94154 | -59.54208 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 988ad5c7-861e-322a-a905-c5ae54911bc3 | -7.07791 | -59.23576 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a64f7707-9f0b-3167-9edc-9ef0b26ee303 | -7.61579 | -63.33268 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecd425e2-4237-35d4-bb85-946cc330ec1a | -7.91077 | -61.74906 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49556b13-ea7c-3f88-ad91-63284191a656 | -9.50476 | -60.52133 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a677942-39c6-3cb4-84d9-dc31c75da5dd | -9.00055 | -60.52934 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6bd38716-2f46-3aa0-a257-3c0f1eb6fd32 | -7.94435 | -63.21887 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7068297c-7c79-31f9-a63f-b04da122f809 | -8.03521 | -61.51612 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbbb3737-d029-3cc3-bcbf-246dd72ab550 | -7.9212 | -61.73548 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5f03990f-b751-3f2b-abcd-20574b1ad79c | -8.46194 | -64.05192 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b62e758-6903-3b6e-8180-2fb66e90dd58 | -9.50937 | -60.52192 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a2289a30-93fc-3538-a98d-01c5ee548234 | -8.03576 | -61.51229 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fdaf773-404a-36b6-bf08-23dc735155ec | -7.57573 | -65.00509 | 2025-08-16 05:50:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 011e7c32-a429-3743-be1b-34734934741b | -7.49874 | -63.82558 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60df8d2c-ee80-378b-a8ce-db81371ef44c | -9.1909 | -59.68961 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d1169e2-56d4-3d85-8375-453db010d5c6 | -8.96532 | -61.68219 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6efeaabf-d8a7-35ac-be07-5e4ac6513c19 | -7.56665 | -61.42744 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2054113b-da11-37f9-b193-0fe238e03654 | -8.98559 | -60.53334 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| edd0fde5-f729-3d60-a4e1-845260f6b017 | -7.95255 | -63.21544 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README67.md)
