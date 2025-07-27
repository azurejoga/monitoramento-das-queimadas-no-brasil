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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed88f723-4852-393f-8718-c11c6b0ef0fd | -7.49592 | -63.82015 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aac0454b-df40-361b-ac5d-93f529ce570c | -6.67159 | -58.85439 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cecf1c9-65c6-3162-b3fb-00b943f45fd8 | -6.54901 | -56.18687 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d92a7c44-d30d-3866-96e2-31c1e15d0e7e | -6.53804 | -56.25894 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc0dbcef-0b7f-3726-8fba-ae3363de7e67 | -6.53494 | -56.26115 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f32b5f8-c91a-3f45-bf5b-01c3c5c50604 | -6.66193 | -58.84915 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f058eedf-0f8c-30e4-9eb5-1f7ef008b704 | -9.43255 | -51.75505 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aebadb6e-bb5c-35e3-aa03-f1c16239c432 | -6.49579 | -56.19873 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efb093e5-96bf-3c1e-bacf-4d27c49050a5 | -6.65796 | -58.85228 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 901ae7d9-5faa-30d1-9dfd-7057483ab45c | -6.68239 | -58.85229 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df0c9ec2-0641-3313-9647-72fa0a40b0cf | -6.53205 | -56.19429 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dbc0cb5-839e-3263-841f-48def02d23e9 | -6.6841 | -58.84131 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 242a7246-8905-3dbd-b746-e4e83729390d | -6.63011 | -58.8292 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f763c0ca-4ba1-30e0-9a49-bdf3c47e0775 | -6.49192 | -56.19814 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4befb734-81fb-3785-a769-53929d854fc9 | -6.6466 | -58.85803 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9c72fccc-38e5-38a9-925b-0a8315313960 | -6.4965 | -56.19392 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e253319a-5abf-3663-99a9-7fcd244b8545 | -9.43112 | -51.75549 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aa5f952-909e-33a3-9405-0d11681c61b8 | -10.28155 | -64.45854 | 2025-07-27 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fde20cd5-21fa-3d80-a087-f0f4bde757e0 | -10.04706 | -64.98221 | 2025-07-27 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5683db78-bd5d-3b2a-a577-bb51ec1f0dbb | -11.29856 | -55.12001 | 2025-07-27 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0343a0fa-5038-3ca6-92af-9fc7590e4eea | -6.55528 | -56.19767 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cc30cd0-dd4e-363d-969b-c171ad8aee36 | -6.68998 | -58.84931 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42c64b02-2a67-32b5-a650-dff53d983455 | -6.64773 | -58.8507 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9553c2c8-79f7-32f3-8a4e-e705ae389aea | -6.65682 | -58.83708 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f519956-eb9f-3083-96cc-6fc52824a38e | -6.67728 | -58.84026 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab795073-4bcc-356f-9b9e-bd3f33a8f4f2 | -6.54365 | -56.19603 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e6e1cc1-8d86-3d0e-8406-46ec42171e89 | -10.05001 | -64.9873 | 2025-07-27 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5eedb297-556d-369b-a958-b41ab262253c | -6.65341 | -58.83655 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6aaad37b-a9c7-370e-a8f7-59d21316723d | -2.58367 | -51.92218 | 2025-07-27 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21c052f9-ca0e-32ca-9007-df3e5a0fbc00 | -6.62784 | -58.84393 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aaf720f-79db-3287-b2c9-2815d089d3cb | -6.65285 | -58.84023 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b94b911a-e922-387e-9939-7d04536a1caf | -6.69035 | -58.84601 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0aa62ced-eee7-3d44-aaf6-08bdb1caa982 | -6.55245 | -56.19499 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 869d5a0a-a4cd-3db5-8f25-e7168e27c7ae | -6.64376 | -58.85384 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 63603cce-72e1-357d-87b6-a5aa3e806340 | -6.54439 | -56.19117 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4a6caad-8cea-331e-8df2-ba0f2c188af3 | -2.90759 | -48.24765 | 2025-07-27 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17189e29-2798-3e9f-9711-a7ee873b1906 | -2.74785 | -48.68447 | 2025-07-27 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6bca113-7e34-3030-abcc-ea8185a4513c | -3.11761 | -48.96222 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34f4faee-e5da-3649-b18a-ea87cb661d89 | -13.19837 | -53.30649 | 2025-07-27 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 433d7d71-88a8-35af-813b-90b191d84cdf | -6.63864 | -58.84182 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53e32df9-7845-3524-b33e-a5f413f1debf | -6.66876 | -58.82764 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ea9134-f56c-31a9-a89a-1ca1722a7ea7 | -6.66989 | -58.84286 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7529a2ea-9cd7-31d4-85cc-e3417866539b | -6.53277 | -56.18947 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da2c242c-3ace-32d6-83fb-9480a9607d70 | -7.60367 | -61.21521 | 2025-07-27 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ddc23737-5ec9-381d-acef-a6cfd16d3805 | -8.30923 | -55.10162 | 2025-07-27 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acfdb065-1990-3030-8b2d-8dd0df27378c | -11.93891 | -63.85144 | 2025-07-27 05:25:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e16466bc-5e39-350c-8a50-f7e71d2ac3eb | -7.55985 | -61.40533 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcc0d82b-83fb-37e9-a2f8-db18e6e5da29 | -6.63182 | -58.84078 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0d9e10b-5792-38f3-9a38-e059768588aa | -9.43242 | -51.74586 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20a50275-5e53-3632-be3c-6b87a371810d | -9.43214 | -51.75822 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e48144-3b57-3655-8ba6-b2bf98fd30ae | -7.29465 | -60.18991 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b5554da-b872-32be-9ed8-676d7586de45 | -8.49655 | -64.02934 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de3f61ba-967a-3b98-8ece-6a0231f72fe3 | -7.57096 | -61.39993 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab2b3b72-8db7-35e4-81fc-7da02f5c90d3 | -7.5593 | -61.40883 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6fce010-b298-37f6-bcc8-6ea7ce35dc3d | -6.68524 | -58.83397 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db2aa80a-31bf-3045-a7c7-c246362e42f5 | -7.56763 | -61.39938 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cbe1d9e-010f-3324-9180-4844aca8049a | -6.53738 | -56.18523 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4773dc25-910f-326a-9c98-8798ecb37696 | -6.63295 | -58.83341 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbd082ba-d341-3c09-bef5-c6722d8caf3a | -6.5454 | -56.189 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8aa0dc72-193d-3ecd-92fd-d1cbf926b013 | -7.56207 | -61.41287 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 515b4e1d-d7af-31d1-9351-1d8359245677 | -6.66932 | -58.84653 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fdd8474-e236-3e06-98ed-7fd8a1e6aeac | -13.09246 | -52.13647 | 2025-07-27 05:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 562ca9dc-b668-3f93-918c-ab5d1f173e2b | -6.68694 | -58.84549 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1131d7d3-36e8-31ab-ae65-63bf93c4c130 | -6.62272 | -58.83185 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eebad547-205f-3fe4-9ac6-24985a60de6a | -6.61875 | -58.83499 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3440bb9-0c18-3452-8bec-911bc4e949e8 | -10.04018 | -59.10513 | 2025-07-27 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 127c2fad-5bc9-3dd0-8b30-c2741e15ae65 | -9.02283 | -59.76273 | 2025-07-27 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c455a3dc-ec5a-350f-afd7-aba01bc029f9 | -6.65001 | -58.83601 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84724766-7ef1-3ff1-9c16-20ea28b72131 | -2.90136 | -48.24666 | 2025-07-27 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17fd5484-0c3f-38f1-ba89-4c40b6342ced | -6.89585 | -52.87124 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fa7bdb7-a910-3f29-9ad8-f23f8ed29231 | -6.62897 | -58.83658 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b0b77ff-9a22-3327-819f-cfc212badf4a | -7.3717 | -62.27808 | 2025-07-27 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 231ad58d-d55b-3925-9cc9-4d83a28e258b | -7.17254 | -59.82663 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73d5be27-c8ab-315a-9bb6-c077cb4e6ddb | -13.20355 | -53.30714 | 2025-07-27 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16fad875-70cf-363c-bc30-8dec42d7cfad | -11.30361 | -55.1163 | 2025-07-27 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8a88c0a-c035-34c1-b68b-f22751ceeea7 | -6.67671 | -58.84391 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f88d330a-d9ef-3e56-906e-f273a7e56612 | -3.39833 | -47.4919 | 2025-07-27 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d23250e-29dc-371a-90d1-465f98ddf70d | -11.29917 | -55.11559 | 2025-07-27 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ceb251e-b08e-347b-9b40-22a622230265 | -10.04076 | -59.10128 | 2025-07-27 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92c7d759-0b2d-3b20-aa3d-5a72e8638d92 | -7.28854 | -60.18537 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a1b0dc-52d7-358c-bd33-6ae107705c67 | -6.53419 | -56.25835 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f8a2ca6-0a91-352d-bb0e-8272a6c42e41 | -6.64205 | -58.84233 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63b90e53-77a0-385c-91ff-2c814ed5695a | -7.904 | -63.52832 | 2025-07-27 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 196750bb-b5bd-3244-b255-8f6dbc924d2e | -9.46019 | -57.85027 | 2025-07-27 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 222f1230-e548-381b-a16d-7e79a90e693b | -8.06969 | -63.85685 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01c2d749-2cd6-3e0a-b8c8-b8454ea69fc5 | -8.97529 | -61.5104 | 2025-07-27 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a0ac31e-1f68-3d63-bc4a-83f1e66a8b95 | -9.92209 | -48.90415 | 2025-07-27 05:25:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37c836c4-7378-32b5-add7-71dc63764fa7 | -7.29132 | -60.18939 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91d4568f-0b24-3d99-ac8f-b86b0518ce45 | -9.4384 | -51.75269 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99eeb9b0-f077-3e73-bc5e-b0b36258f04d | -6.66137 | -58.83027 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8c13b79-5ac8-3efc-b68b-faa71b727ade | -6.65739 | -58.85594 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c6cf08a1-813c-3be6-a2eb-87290dbbfc07 | -8.68837 | -64.22255 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ebaec38-9653-31c5-9bb6-36b633a942f8 | -2.58023 | -51.92532 | 2025-07-27 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b8ea157-4cc1-30dd-9dcd-da05d85cac70 | -6.62841 | -58.84026 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5867db93-ff23-340e-a6fc-d7a7924f8533 | -6.62557 | -58.83605 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d71afc43-6671-37b5-a8a0-fe02d903bec6 | -12.17363 | -60.73777 | 2025-07-27 05:25:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d1f1a7f-109a-308c-9cee-38a832dbefa6 | -6.63466 | -58.84498 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1321e0a5-76e3-386e-80db-a607a3b38c10 | -6.6483 | -58.82446 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d0ceec6-0583-3b76-8adc-8196a8408974 | -6.66023 | -58.8376 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bfcb747-f6b8-3c27-b5dd-18bbd7341446 | -7.56263 | -61.40936 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
