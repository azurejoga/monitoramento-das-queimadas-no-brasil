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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42ae87e3-8398-311a-8c94-d0dda3ba788c | -6.0549 | -57.8227 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 3bea5160-f087-34d7-ae71-5df615fc15b6 | -4.3137 | -49.1226 | 2026-09-22 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 478ab47e-042c-3883-a4ee-3f55e19c4eb2 | -6.1109 | -57.684 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 1a8c68af-ff70-32b6-b415-c339e8c88d13 | -9.2765 | -46.1401 | 2026-09-22 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 266.9 |
| bf039e39-e7be-34e8-aa18-7ab3f7b60a67 | -10.5908 | -53.9713 | 2026-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 94799063-b6bd-37c2-a057-c72ff7cee305 | -6.789 | -48.6779 | 2026-09-22 00:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0afbc1a6-9fb5-3f28-971b-e54fdd0861e4 | -5.7864 | -43.8684 | 2026-09-22 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| bebfcae9-61e3-3f35-96c3-0ce3ae500afc | -11.3255 | -54.0487 | 2026-09-22 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 234.3 |
| 8a3dc573-07e9-39d0-ac22-406278e33e24 | -10.6097 | -53.9697 | 2026-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| c0ae9d67-0f18-3f2a-8300-88b909110b0b | -11.4113 | -46.7798 | 2026-09-22 00:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 8a471c04-d243-3573-b623-ecaa382cebdf | -8.2388 | -55.2616 | 2026-09-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 6051e1e9-e258-3b79-82b5-ff575707b4fe | -10.5906 | -53.9918 | 2026-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 978f9c8d-0d84-327a-b898-a17f72231a7b | -8.6169 | -54.6328 | 2026-09-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 1fd5356b-76c4-336e-b12f-c5881c551992 | -8.8273 | -50.5032 | 2026-09-22 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 450a7848-5675-347f-9b72-7f558ee92184 | -8.8275 | -50.482 | 2026-09-22 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 5cea2953-e629-3529-a065-00da1c6655da | -6.467 | -59.9902 | 2026-09-22 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 62b20cc9-33c2-302a-9c0a-d30c12957557 | -8.2572 | -55.2805 | 2026-09-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 69729b44-a532-365e-89dc-76e2c438a7df | -11.3066 | -54.0505 | 2026-09-22 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 88c5060b-9706-3413-937d-b45d625ceb0c | -4.2951 | -49.1234 | 2026-09-22 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ceff0d7e-9074-3eba-b816-5d5b3e1ec786 | -6.0928 | -57.6262 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e0b6826a-c803-317a-b682-9c6d902346cb | -6.571 | -44.1516 | 2026-09-22 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9de09ddd-0c58-30ea-84c1-1155b77d90c0 | -7.5703 | -57.6962 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 64317f80-4371-3514-b7af-09dab0f8f8be | -8.6355 | -54.6316 | 2026-09-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 62b41dc5-055b-33aa-ae10-1cdbd8d76e47 | -2.8608 | -57.7994 | 2026-09-22 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 69f17910-fc89-3b51-8cd4-cfcd7f4a68c2 | -10.6094 | -53.9902 | 2026-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 39bd6b17-88dc-3fac-8510-c5d9b63e12b7 | -7.5888 | -57.6953 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 5314bc1a-c604-320c-8ddd-c2d3bc8bd444 | -6.0365 | -57.8235 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4a4b4461-0179-369d-aa2e-11c6f071507a | -18.7472 | -46.93 | 2026-09-22 00:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 8c500f45-3084-34a5-a1ce-93cac3decdd2 | -11.7675 | -50.804 | 2026-09-22 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d92d4019-d455-3dd0-bc20-d3fc6496ee09 | -7.5891 | -57.6561 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7f545e2d-a9dc-3217-a235-d7a1111e8829 | -2.4206 | -58.2712 | 2026-09-22 00:00:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e567e637-620b-30f4-ace4-6f51a262ba4a | -4.2239 | -48.6127 | 2026-09-22 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 776cf27b-6628-3eda-aebe-d473e1cfe824 | -12.5551 | -45.9376 | 2026-09-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| d1ba231c-3094-3709-b69e-61541250769d | -6.4485 | -59.9909 | 2026-09-22 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| dcb6b4f4-fe2b-326b-a91c-7f9901975ac9 | -9.2759 | -46.1852 | 2026-09-22 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| ba9cb57e-188f-3c9c-87a3-d40be9b469ff | -12.5547 | -45.9605 | 2026-09-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ee3692a2-9f0c-3e63-becc-ede32e54756b | -12.4008 | -47.0481 | 2026-09-22 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f4cd4bb6-8f72-3ed8-bde7-d31ae166a33f | -11.3444 | -54.047 | 2026-09-22 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c92e26d5-700e-364c-82f4-5f9b977c0e03 | -8.2574 | -55.2604 | 2026-09-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 6d2cfb47-c7a8-3688-a790-23f39d2a5b4d | -7.5704 | -57.6766 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 95758845-6be2-328b-942a-48c083fee2e5 | -11.3068 | -54.0299 | 2026-09-22 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 0b4b6e4b-02ae-3ac8-8282-84ec7087cc43 | -10.6283 | -53.9885 | 2026-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6fbdda06-d0c1-3844-873f-9c44593a7e75 | -9.2762 | -46.1627 | 2026-09-22 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 811.1 |
| 2c3e5a40-b66a-33c1-8f69-ab4032bae5a9 | -10.6092 | -54.0107 | 2026-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0aadce30-0e32-3c46-bdcf-64a16c2da295 | -3.0726 | -54.4076 | 2026-09-22 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0418d886-ecb0-34e9-89f1-602dcd5997fc | -9.2573 | -46.1647 | 2026-09-22 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 497.2 |
| a270a64b-2b11-3ba0-a3f9-a57287fb6de5 | -6.4671 | -59.9711 | 2026-09-22 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c0331b70-dd65-3f6e-95ae-49e4b10e0902 | -9.257 | -46.1873 | 2026-09-22 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 42ee2394-67bb-3726-a807-665dbe64d1ca | -9.2576 | -46.1422 | 2026-09-22 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 164.4 |
| ad0af6c5-76ae-379c-b7c3-bdc9d243a4e3 | -11.3257 | -54.0282 | 2026-09-22 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 170.8 |
| aa3942e9-12e9-30ae-a412-c54de39dfba2 | -8.2576 | -55.2403 | 2026-09-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| eebb1796-5613-3a8b-a60a-bc217171e1a6 | -11.6793 | -43.4684 | 2026-09-22 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 61721662-b73e-3a4c-ab7b-513c6b3f37b6 | -3.0542 | -54.4081 | 2026-09-22 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| ccab4f7a-d43c-3e2d-b144-d9df37e3b8fe | -8.2389 | -55.2415 | 2026-09-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 840a5333-f370-3eb3-8fef-8a8652e8adb6 | -7.5889 | -57.6757 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 205.4 |
| b15e9405-d87e-377f-91e7-acf4836fad36 | -6.5898 | -44.15 | 2026-09-22 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 0a96d97b-a899-341b-af08-41f5fe8f0767 | -6.0925 | -57.6847 | 2026-09-22 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| dafb19c8-e944-37b5-a7a3-8b6a60495d3b | -3.405 | -59.522 | 2026-09-22 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 85c5282e-397b-39d4-9505-b09bd1bab8cc | -11.6798 | -43.4446 | 2026-09-22 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 12729ffe-000e-3ed1-900e-ab335a45f3e0 | -3.5096 | -55.492 | 2026-09-22 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 810c18de-b325-3121-8772-67242db00697 | -12.5744 | -45.9347 | 2026-09-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 57a31ba1-627b-3316-afb1-6cfed23a5c90 | -3.0726 | -54.4076 | 2026-09-22 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c47a6d7f-8968-3f34-ab61-e24e79791afb | -6.1109 | -57.684 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6beb81ce-8951-3c19-aaca-fd8521d76654 | -4.2239 | -48.6127 | 2026-09-22 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a1aecab2-088f-3236-a969-7a746ed92b21 | -3.405 | -59.522 | 2026-09-22 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 62ce0d83-084e-3548-bfd7-0e5fe7ab410a | -5.7864 | -43.8684 | 2026-09-22 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 267.7 |
| fb236d11-b2a7-345b-9aeb-9fa73dd599bf | -10.6283 | -53.9885 | 2026-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 254df724-2b5e-31f4-affc-ee6e9d192a65 | -11.7675 | -50.804 | 2026-09-22 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| edf238d5-0127-3831-9cbf-b94eee0499dd | -7.5703 | -57.6962 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 64da012d-a411-31de-8e25-f4b7026ecc61 | -6.5898 | -44.15 | 2026-09-22 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 31147f07-a76a-3822-9be0-76ba6bfcc195 | -4.3137 | -49.1226 | 2026-09-22 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 71d489ab-b200-3125-a246-95005778b93f | -11.3257 | -54.0282 | 2026-09-22 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 99f2993e-7747-3003-a338-c2eaba24056f | -6.789 | -48.6779 | 2026-09-22 00:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d0ce9b0b-5c9d-30f6-b1e8-4f9b3fae6ad6 | -5.7569 | -45.084 | 2026-09-22 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 743.2 |
| cb773c7e-1494-3ff3-824a-c4a136388a9c | -11.3066 | -54.0505 | 2026-09-22 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 9f166576-21ad-3f39-afaa-662316043a92 | -9.2576 | -46.1422 | 2026-09-22 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 95c725a9-c08e-38b0-8489-f51446f96aae | -7.5888 | -57.6953 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 96407557-1994-38a7-981b-489719c19baa | -5.7382 | -45.0853 | 2026-09-22 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 74a0ca4b-06f3-30b9-bc5b-1e8d52c40c7a | -10.6094 | -53.9902 | 2026-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 488dbd40-d250-305d-9498-d4e605566427 | -10.5908 | -53.9713 | 2026-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 1d0a5eaa-3ca1-3a0d-9c4a-27d496fcaaae | -5.8054 | -43.8438 | 2026-09-22 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| d7241966-f030-3078-8599-474afd3d4551 | -9.2765 | -46.1401 | 2026-09-22 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 4efe66a6-0874-3cff-a78c-6cd774b2b25b | -5.7756 | -45.0826 | 2026-09-22 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 1e718d4e-4dcc-35e1-ba01-4dd48ae9b00e | -18.9835 | -47.1108 | 2026-09-22 00:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 46f5474c-1f3a-32bb-9d6c-3d26518b14cb | -10.6092 | -54.0107 | 2026-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 08992d22-db1c-3f0b-a581-d206db27fd7b | -7.6075 | -57.6747 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ea7cece2-9603-3f1e-9117-72e3c2a4c429 | -12.8059 | -54.0255 | 2026-09-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 291.8 |
| 81e7375c-43ce-3d41-87d7-a27f4790db64 | -9.5168 | -35.7636 | 2026-09-22 00:10:00 | GOES-19 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 58.2 |
| 1594663f-d53d-3dc6-b38e-b8a2aef2aca6 | -6.4671 | -59.9711 | 2026-09-22 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7ddc242f-f9ad-3818-a107-fa8647b0dedc | -8.6355 | -54.6316 | 2026-09-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 75e642df-e571-3c95-974f-6fdafd7b8322 | -6.571 | -44.1516 | 2026-09-22 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 45566e9c-6968-38e8-8a28-c3a927a99f55 | -4.2951 | -49.1234 | 2026-09-22 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 182dcc82-8a8c-314d-9b99-f8ee62db9ddf | -6.4485 | -59.9909 | 2026-09-22 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 73df046c-0d98-3aa5-abcd-2546d397c244 | -8.8273 | -50.5032 | 2026-09-22 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 19e88843-eaff-3537-9afe-8f03f15c2753 | -7.5889 | -57.6757 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| a9218018-4918-39cb-bf22-a1abce190ed3 | -11.3255 | -54.0487 | 2026-09-22 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 9d491a45-7df2-3031-8d0e-f90d91a8e395 | -5.7866 | -43.8453 | 2026-09-22 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 7db009fd-6ce0-3c98-8c67-d3325c7affab | -8.2572 | -55.2805 | 2026-09-22 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2beba3c4-492d-33e0-8cfb-05f4017ef1ad | -6.0549 | -57.8227 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 9139b01c-2734-3ff4-9aa5-6fbfe67bd37a | -5.7571 | -45.0613 | 2026-09-22 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |


[Clique aqui para ver as próximas entradas](README2.md)
