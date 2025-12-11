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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edd6d0c0-f9b8-357a-8375-b14b6b5738b2 | -2.44477 | -49.02744 | 2025-12-11 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f92d125-f476-37f3-b334-17616ef392c3 | -2.65549 | -51.64719 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a2c87f2-8443-3107-80f7-b99e093c3b94 | -2.88037 | -52.72433 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea9a54d-4de7-3fab-8005-4475b66bca0d | -3.51258 | -52.74765 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19d02a32-7bc5-310c-88fd-a6e1a2a196a0 | -3.27551 | -49.95601 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3aa9323c-889f-3af8-afc1-c2be37845256 | -2.47124 | -52.15031 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a4615a9-eb0f-3fb1-bc44-0a149bef7986 | -2.07818 | -52.05284 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18e6d804-3358-341a-a68e-b107efe977cb | -1.68897 | -45.7962 | 2025-12-11 04:38:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97f9195d-4923-3980-ad05-54884b698f74 | -4.23458 | -42.51027 | 2025-12-11 04:38:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ff55229-7359-3ef5-aa3f-b99a8defd73a | -4.49614 | -43.42458 | 2025-12-11 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee62d710-8612-31a9-802a-e15221f61fb6 | -2.89816 | -50.23234 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab5d774-3cc6-3b5c-bb23-7a78fffb2da9 | -4.0655 | -47.65866 | 2025-12-11 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90bf3deb-87ae-3a9e-9f1d-fa18f425f614 | -2.67041 | -49.16854 | 2025-12-11 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b568512c-0dd8-38cf-a19c-61102c289b5c | -3.23174 | -47.47603 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e196bbe2-b189-384b-9dea-7e9ffdac1b33 | -3.08717 | -44.89711 | 2025-12-11 04:38:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e55b9fb-ead4-305c-88b0-e1455b6c6658 | -3.01111 | -52.68275 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a9dddf5-f5e0-36fc-a6c2-94a638eb885f | -3.825 | -48.87117 | 2025-12-11 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cceb371-1e3b-3058-8e9d-ea6c42782135 | -0.64229 | -52.39657 | 2025-12-11 04:38:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75a8161d-f24b-30e7-8c3c-1423c68ea2ba | -3.27494 | -49.95952 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 219b8571-576a-394f-a6f7-cfaefdeb0a5b | -2.4661 | -45.3228 | 2025-12-11 04:38:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 89c9d5ec-6b78-34b4-a7fd-f87692cc4c67 | -2.41002 | -56.01661 | 2025-12-11 04:38:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5fb953b-1538-3cec-9ae2-a936e411c54c | -2.55167 | -45.32574 | 2025-12-11 04:38:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5540e424-6a64-3549-a550-a311bc6291ac | -3.51421 | -52.18364 | 2025-12-11 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb7749df-89b3-303b-b9c6-920583e0f1ea | -1.16729 | -48.85429 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bf668c9e-de2b-385a-a696-4457cf065d05 | -5.17775 | -44.80699 | 2025-12-11 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4bf335b-8403-3ffc-af83-d46d30834134 | -3.14813 | -53.75262 | 2025-12-11 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 865b0366-5e73-3e60-9eb1-d3d22c8b07ce | -2.69449 | -51.64845 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7814b44d-9c3b-3d38-81f5-f073b3d28ecb | -1.09609 | -46.62913 | 2025-12-11 04:38:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5ccd625-52d9-37eb-821a-eb2c2a2c2183 | -2.05445 | -50.66063 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d111c5-98b0-3ca3-8755-8b3f5b458950 | -1.93586 | -45.43968 | 2025-12-11 04:38:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f6785f-802b-3444-b267-892584d7bbb7 | -2.65256 | -51.64256 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 457cc7d1-6e6b-33c9-b3f9-8afa369ce176 | -2.47491 | -52.15086 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c34a0d7e-20fd-39bc-a284-338b0a527fb0 | -3.73659 | -48.89218 | 2025-12-11 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91896e07-bf43-321a-8ca7-558ba078bc81 | 0.59772 | -51.58146 | 2025-12-11 04:38:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4b09407-c643-35dd-9588-f3f76bb5f4b3 | -3.57826 | -52.10817 | 2025-12-11 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8a3c9a5-e169-3afd-a846-7397bd80100d | -1.01444 | -53.72669 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19451186-b35b-3467-868c-aa8a90d582a3 | -2.20911 | -51.89304 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 550ea964-2774-3bf6-afa7-85eb560fe8d1 | -2.90798 | -45.22589 | 2025-12-11 04:38:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cd159d2-0f84-32b5-ad6e-f4fecfbe9db2 | -2.31352 | -46.48329 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f86c0d8c-92f1-3af7-a8ec-151233bb0a35 | -2.21205 | -51.89783 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c432ced8-5932-38fe-9031-c6167dd9df36 | -2.90631 | -46.72959 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da5b4caa-a73a-3807-b326-5f45486ae758 | -3.48753 | -51.53815 | 2025-12-11 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc8d3ee6-893c-3194-9c0e-060ad521e19a | -3.7589 | -45.4944 | 2025-12-11 04:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 0b4e4513-ce2b-3893-b508-811640448c8d | -2.2906 | -45.5933 | 2025-12-11 04:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3056ca3c-0384-32a7-9101-b52a76495fca | -5.77159 | -53.44889 | 2025-12-11 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7290cf0-c93e-3ff1-91b8-c3a785b89b89 | -6.37234 | -44.03053 | 2025-12-11 04:40:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 326fef86-b6aa-3222-a544-f72e24e21c49 | -9.82145 | -47.93097 | 2025-12-11 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 703a40c1-82b7-30eb-9090-b518c1c0fd3f | -5.37361 | -50.62848 | 2025-12-11 04:40:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1deb824b-095a-37aa-9759-066b6bf8a9e4 | -9.30302 | -48.55686 | 2025-12-11 04:40:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8634e922-2e3e-3db1-8e3c-98e33304c89c | -10.47946 | -50.65904 | 2025-12-11 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d509ef8d-14f7-3c1a-86e7-09b51dcb7369 | -8.43935 | -49.4215 | 2025-12-11 04:40:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ca0f3cc-ee10-389e-91bf-be190ce737c1 | -6.03083 | -43.70682 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 7b2ea9fa-dc39-3755-9437-8db3c280a438 | -5.98609 | -44.59793 | 2025-12-11 04:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1ddb229-ec76-3d03-8054-1604f562cbea | -5.06437 | -49.88415 | 2025-12-11 04:40:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d30b2f6a-5027-3067-8e24-3f78e39dadb6 | -6.50254 | -41.48949 | 2025-12-11 04:40:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9887b084-95ab-35e3-aa46-5c5d4be5f0fe | -10.9819 | -53.9966 | 2025-12-11 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1dd7633-cd05-3a08-a9e0-7d172157a6de | -10.23857 | -52.218 | 2025-12-11 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a34ae0-f49f-3f6a-bfb2-0e0d5b1a9540 | -6.02975 | -44.33075 | 2025-12-11 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2cd69ce-ee18-3e6f-ae0f-4d1b4f2e8e8f | -11.48311 | -41.47333 | 2025-12-11 04:40:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| cc2a2240-2edc-39a2-8dbd-3ef6bf91669d | -5.9866 | -44.59447 | 2025-12-11 04:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f193050f-e7fa-3ced-ae59-254f3a2adb09 | -12.67592 | -46.77867 | 2025-12-11 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccc88537-ed61-318b-b717-24d67638418d | -10.47615 | -50.65851 | 2025-12-11 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a3cf8cb-cfa4-3327-93f5-c2b63dea984c | -7.86152 | -38.72897 | 2025-12-11 04:40:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a46183da-1d0e-3fc7-b3e2-d2eb87f0c7b8 | -10.48001 | -50.65555 | 2025-12-11 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 862d509f-ce6d-3322-8ff3-2a2a994212a1 | -10.98917 | -53.99788 | 2025-12-11 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f64ceb6-6564-3ec0-8dc1-1dbf1a543479 | -6.26805 | -43.6801 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa92e286-586b-3ddd-8c35-308f8c2f26b2 | -6.02659 | -43.70619 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 19a7580b-49e9-33ec-a0fd-073df7de1d24 | -5.9826 | -44.59391 | 2025-12-11 04:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0662a0dd-45c9-32c9-b224-9e27c569817b | -6.06058 | -43.73924 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ae6b3f-822f-3441-b5f4-b60e95807305 | -6.02179 | -43.70944 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5feab2b-74af-39cc-ab6a-12e70dd1381b | -10.66609 | -49.28663 | 2025-12-11 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17325eea-5aff-3927-aae2-91f1c66b3230 | -10.98513 | -53.9985 | 2025-12-11 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42c5fb96-e969-316c-8a50-e376ee69d563 | -10.98554 | -53.99724 | 2025-12-11 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa4eab1d-5af6-31b9-a4ec-169ed4e4b33e | -11.66557 | -47.12549 | 2025-12-11 04:40:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a89b4db1-9bfa-3496-9b20-1323d3f20ce5 | -6.03029 | -44.3271 | 2025-12-11 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12ebab68-dfe5-30ae-b019-6117e65ee0b1 | -7.86001 | -38.73236 | 2025-12-11 04:40:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cf77047d-d52b-3730-957e-b468278abab0 | -6.37289 | -44.02672 | 2025-12-11 04:40:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0076d896-d475-3db9-8aa9-8b096af5937f | -8.71978 | -50.22923 | 2025-12-11 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6305a99-d3cf-387d-9288-0460733e96ca | -8.09822 | -55.01168 | 2025-12-11 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e13c3c17-adf8-3f11-8716-f44a5dab794e | -7.86062 | -38.72789 | 2025-12-11 04:40:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9c4c11ba-9ab3-33f4-b533-580cddd3f051 | -9.30641 | -48.55738 | 2025-12-11 04:40:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2273f55-2b17-3c63-9f65-3baa6cb4d453 | -5.98209 | -44.59738 | 2025-12-11 04:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4d8a940-dc6b-3a3c-9f80-dc926eab6530 | -10.23797 | -52.2217 | 2025-12-11 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad27350d-ef8e-3142-aa85-c6e01163c993 | -6.02236 | -43.70557 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6523bd34-6178-3cf4-b7c8-b557b393a77e | -12.67526 | -46.78344 | 2025-12-11 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27aa1738-e575-39ce-8675-b3636b3b1b56 | -5.14513 | -49.93223 | 2025-12-11 04:40:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92831da4-86d1-3756-8b40-5532d0e37f89 | -10.4767 | -50.65501 | 2025-12-11 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1fc019b-65d5-39f5-ab92-4e03d7e76928 | -10.23456 | -52.22114 | 2025-12-11 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3246bfbf-cbd5-31d1-adea-103e8104d4ce | -5.9781 | -44.59681 | 2025-12-11 04:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 057277d0-cac2-3771-9c2a-c9470dab7a69 | -6.03026 | -43.71068 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 598e1f72-8dac-31ed-82a6-fa7bbe0de7aa | -5.06492 | -49.88068 | 2025-12-11 04:40:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2946a7ff-e363-30bb-a38f-45c249cee932 | -5.51779 | -50.38638 | 2025-12-11 04:40:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac95da09-d3fd-3813-9245-9047d9a2012e | -11.48355 | -41.46988 | 2025-12-11 04:40:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 1a02062c-df06-3a13-83eb-a614c9f0cfd9 | -7.56966 | -49.40172 | 2025-12-11 04:40:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49feeab1-67fd-3b4c-b608-0f3c469fd0e7 | -6.02602 | -43.71006 | 2025-12-11 04:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa541b34-2a40-38fb-8d1c-ebc25d582260 | -14.07577 | -56.168 | 2025-12-11 04:42:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 552fddb1-742a-3b8e-9f5d-b6eadfa0272f | -16.70202 | -44.96581 | 2025-12-11 04:42:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03c7aede-afbb-3dd4-b8cb-90fe62a23fbf | -12.44472 | -63.63739 | 2025-12-11 04:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06694c6b-cba0-3f8e-9136-29061e898229 | -16.30851 | -53.82578 | 2025-12-11 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd29ed4b-4d11-3ff8-b190-8831328c692e | -16.30787 | -53.82959 | 2025-12-11 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
