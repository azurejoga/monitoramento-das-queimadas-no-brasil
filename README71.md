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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0993e6ac-a674-36e4-9a13-e2f19ec4911f | -3.5921 | -42.0869 | 2024-11-23 12:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 8af13538-4abc-32ab-8d85-5342ff196985 | -4.6083 | -46.5223 | 2024-11-23 12:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 7f340c75-ff6d-337b-b1e2-b692c134ba2f | -0.9462 | -52.4214 | 2024-11-23 12:50:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 76f55b28-2d27-36f5-822a-993a51733e5d | -5.4738 | -43.2178 | 2024-11-23 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 071c24bd-3e1f-3479-bbf1-962882a2c5cd | -3.685 | -42.1771 | 2024-11-23 12:50:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 232.4 |
| fd221018-5cfc-3e27-8a47-fd79cacf535b | -4.2606 | -48.6755 | 2024-11-23 12:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 285.6 |
| 9110e5e3-4416-3088-a308-6183f67c14e2 | -5.455 | -43.2192 | 2024-11-23 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a2ec28e7-b160-301b-a9b8-ee67f037f515 | -1.7891 | -53.6495 | 2024-11-23 12:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c34fc387-a479-33af-9113-dabbc5d8b2ab | -4.242 | -48.6978 | 2024-11-23 12:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| b7cb4daa-fe46-3fe7-8331-4724db8499f5 | -1.6553 | -47.4188 | 2024-11-23 12:50:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f1805998-5a6b-3336-90c4-1ce0fa636b2c | -4.2606 | -48.6755 | 2024-11-23 13:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 251.3 |
| 6eec3373-d512-3fd3-bf7c-0cd397bf82c2 | -5.455 | -43.2192 | 2024-11-23 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c4ae29ed-29c4-351a-9c93-03cdf0e2ecd7 | -1.5493 | -54.3357 | 2024-11-23 13:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9b720672-d6f6-3608-ac6e-2c38a1928394 | -2.9434 | -44.9419 | 2024-11-23 13:00:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ce3eadb0-981a-3190-b72a-2a9ac59093db | -1.6245 | -53.3084 | 2024-11-23 13:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 33e097aa-f78a-33b2-900c-20505a7777a1 | -5.4548 | -43.2426 | 2024-11-23 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| cc5762ad-7a26-3157-9563-1a50967b2292 | -3.685 | -42.1771 | 2024-11-23 13:00:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 216.9 |
| aac5f08d-020e-35b2-ae76-0362c2b4e8ad | -5.4738 | -43.2178 | 2024-11-23 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2a1d3b60-a0ec-3b3c-b2c0-a2e0e5cbb397 | -4.242 | -48.6978 | 2024-11-23 13:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| a1a0e34d-95f5-3bcf-9ee0-4a04b4850fca | -4.55 | -42.88 | 2024-11-23 13:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b17b2561-05bd-310c-b94f-dda0d6fed6ff | -4.55 | -42.93 | 2024-11-23 13:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f408bb8b-c2bd-34e1-b2fd-6483edc402a7 | -4.52 | -42.88 | 2024-11-23 13:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 675cab47-8d09-3d21-a4bf-35e0b0cac6e0 | -4.26 | -48.68 | 2024-11-23 13:00:00 | MSG-03 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c62d13-375c-343b-a8c9-ec1cafc2df01 | -2.96 | -44.92 | 2024-11-23 13:00:00 | MSG-03 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68f62919-ee04-3e8a-bedd-79857679e41a | -4.52 | -42.92 | 2024-11-23 13:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fce7b13-f2db-3b5c-a6f0-401ee5974f70 | -4.2606 | -48.6755 | 2024-11-23 13:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 267.9 |
| 92adf05d-99d6-3f85-9bf4-5962f453f1e7 | -1.4524 | -47.1166 | 2024-11-23 13:10:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 05ce8a87-6ffc-3228-b8a5-ea7b63177a72 | -5.4548 | -43.2426 | 2024-11-23 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ea9ebcef-80e5-3cea-a7cf-08562ae6bd77 | -5.455 | -43.2192 | 2024-11-23 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 16a50467-5ed7-39e3-b730-6529430ce475 | -2.9434 | -44.9419 | 2024-11-23 13:10:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| b00470c4-5214-3484-a2f8-d3cf732121ba | -0.9891 | -47.5592 | 2024-11-23 13:10:00 | GOES-16 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 238.0 |
| 2332dfa0-f839-3b84-a4c7-cc4b9bf4f222 | -3.685 | -42.1771 | 2024-11-23 13:10:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 5fe2fb87-42f5-38fa-80b6-a1d5e9c17b43 | -1.5493 | -54.3357 | 2024-11-23 13:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 9431d45a-1d75-335e-8778-c39b9fd8adaf | -6.027 | -42.2316 | 2024-11-23 13:10:00 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 460d24de-c552-3bb0-b279-c51b8f913d87 | -0.9892 | -47.5374 | 2024-11-23 13:10:00 | GOES-16 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ee7d78a5-e906-3b41-b1f8-325d4330c824 | -1.6245 | -53.3084 | 2024-11-23 13:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| dae9e279-2808-3f97-b99b-42dcd49326ae | -5.4738 | -43.2178 | 2024-11-23 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| cd9d6574-b0fb-3ffc-91ec-3e458f885a2e | -4.242 | -48.6978 | 2024-11-23 13:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| a83c54dd-5e82-3e42-91bb-5e4d311e91e8 | -3.4612 | -42.0934 | 2024-11-23 13:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 143.2 |
| 415dc20c-6c20-3803-b6b3-9de1fde78bae | -2.9434 | -44.9419 | 2024-11-23 13:20:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 04c73064-2790-3cc5-bf39-81f959616b08 | -1.4524 | -47.1166 | 2024-11-23 13:20:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a8a5088f-ffed-324e-bb3f-edc2177e5261 | -3.4612 | -42.0934 | 2024-11-23 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 343.1 |
| 17c57d4f-da99-3395-bde8-bca0b7d54275 | -0.9522 | -47.5596 | 2024-11-23 13:20:00 | GOES-16 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 3f7326fa-b067-3d81-a8dd-f1121bff40b3 | -5.4548 | -43.2426 | 2024-11-23 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f1799001-4dcf-3bc0-9580-b6ccf82cf142 | -2.4189 | -46.036 | 2024-11-23 13:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 54085edb-13e6-301c-8230-4093a3339682 | -1.9543 | -46.3586 | 2024-11-23 13:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4e843014-181a-32fa-8444-4c844acc2b68 | -3.685 | -42.1771 | 2024-11-23 13:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 508935cb-b7c2-3008-83d8-dc1b2ce5ce0d | -3.1502 | -44.4796 | 2024-11-23 13:20:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1b7ca681-0ea7-3511-93d6-ce22bcd4680c | -3.2201 | -54.2436 | 2024-11-23 13:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6a048304-3454-3b69-a1ea-5ffdce2affc3 | -1.5493 | -54.3357 | 2024-11-23 13:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 52e7e323-f0ff-3ebc-877d-4909aeae7ad3 | -6.027 | -42.2316 | 2024-11-23 13:20:00 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 0df12237-1b11-38a4-86b4-b62518153be1 | -3.2386 | -54.223 | 2024-11-23 13:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| ab271ed4-acbf-3d15-bce9-f9f500bfb4b1 | -5.4738 | -43.2178 | 2024-11-23 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 3893e588-ea87-377e-8e6c-2a49a0f91a41 | -3.5906 | -42.3476 | 2024-11-23 13:20:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 257.2 |
| 27363029-e6a4-3729-bfba-f85a0567b584 | -3.2569 | -54.2226 | 2024-11-23 13:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 6abcb1e6-d29d-3430-8b9d-b9a7d1133784 | -5.455 | -43.2192 | 2024-11-23 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 84402df1-7e39-3e3e-b0f6-af7e0ee8ef0f | -4.2606 | -48.6755 | 2024-11-23 13:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 3db4c198-0cb5-3059-a4c6-8aee65b53daf | -4.242 | -48.6978 | 2024-11-23 13:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| c9c67da4-d6fa-302a-850d-b7a3e3dec314 | -0.9891 | -47.5592 | 2024-11-23 13:20:00 | GOES-16 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 193.5 |
| a8ea315a-1490-31d4-84bd-b40dbd90240b | -1.7472 | -47.678 | 2024-11-23 13:20:00 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 98842f47-f2bb-3d25-8763-8d649199ea94 | -3.4612 | -42.0934 | 2024-11-23 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 186.8 |
| a5039939-8577-3736-abf3-9ed7bd70ee29 | -1.5493 | -54.3357 | 2024-11-23 13:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 68ccce94-8a34-33fc-be68-be48eee67ae5 | -3.095 | -44.3448 | 2024-11-23 13:30:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 990dd640-b9d1-34d5-9028-edaec6cd5085 | -3.4975 | -53.8137 | 2024-11-23 13:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2605f36c-13b3-324c-a068-ebd509b484ac | -5.4548 | -43.2426 | 2024-11-23 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 717a6982-169d-34ea-8923-e7ec4af5e933 | -6.027 | -42.2316 | 2024-11-23 13:30:00 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| ca814fc5-b5d9-3a32-81f1-7a15fecd5c8d | -1.6245 | -53.3084 | 2024-11-23 13:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 26732522-bc81-3a47-956a-ed4b2add381f | -5.1185 | -43.1497 | 2024-11-23 13:30:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c68c943d-e591-37ce-b60f-d0fac7dbb33e | -3.2201 | -54.2436 | 2024-11-23 13:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c73af984-e19a-32ad-8ac5-cccbcc27560c | -6.1098 | -37.9207 | 2024-11-23 13:30:00 | GOES-16 | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 99.2 |
| ab4fbbcc-32ff-3d2d-98ff-fbb87790d57b | -3.4264 | -45.0585 | 2024-11-23 13:30:00 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| cf4679e9-9ad7-339d-a5f0-11f13eb19b92 | -2.6964 | -46.2497 | 2024-11-23 13:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6118614c-5e6b-3b8d-a2b9-aa21f6c886a3 | -3.2386 | -54.223 | 2024-11-23 13:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| ecd8c94d-674b-3223-88eb-1cfd9f2f177a | -4.2606 | -48.6755 | 2024-11-23 13:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 9194f2a8-1aab-33dd-a85f-b478cb0812c8 | -5.4738 | -43.2178 | 2024-11-23 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b2353d90-2381-3b44-8927-d56e7c69b758 | -3.2569 | -54.2226 | 2024-11-23 13:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| eb866791-f709-3a7e-8cc2-5e30fcb39aff | -3.0949 | -44.3677 | 2024-11-23 13:30:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a584db5d-1c11-3fd2-8439-d5397eddcc47 | -5.455 | -43.2192 | 2024-11-23 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| dcaf7bd3-2260-316b-9454-486d5ce5cb00 | -5.1185 | -43.1497 | 2024-11-23 13:40:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2c1ed31a-17cf-3f00-91b9-29688c527d16 | -4.2606 | -48.6755 | 2024-11-23 13:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 1740fc0e-964d-3785-9c17-c684c54b39e7 | -5.4546 | -43.2659 | 2024-11-23 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 372ab594-efd8-3a86-bc34-dba804835e6d | -3.2386 | -54.223 | 2024-11-23 13:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 73373599-1272-3258-b2cd-cdc2f9a96053 | -1.5352 | -51.9436 | 2024-11-23 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| eae45699-4604-3dbb-a22f-c68fc505de97 | -5.0998 | -43.151 | 2024-11-23 13:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e5074019-e795-3142-bfe9-5bbe0006b15e | -3.4612 | -42.0934 | 2024-11-23 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 36e594b5-a05b-3bbb-8df6-1097489f16d0 | -1.5493 | -54.3357 | 2024-11-23 13:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 12cfe0f1-5bc0-3f99-8e76-2e28eba9eb24 | -1.6062 | -53.3087 | 2024-11-23 13:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7f5a84d8-24ad-314e-99f6-bbb6b2832b2b | -5.4548 | -43.2426 | 2024-11-23 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 8cce259a-8dff-30d8-94e8-013b91d15d43 | -0.9462 | -52.4214 | 2024-11-23 13:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 2244d5e5-1f9a-3956-878b-3da368aaa9b8 | -3.2201 | -54.2436 | 2024-11-23 13:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d5c04ef5-ae1c-3efa-9345-ddaacbe4e74e | -3.095 | -44.3448 | 2024-11-23 13:40:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7765ee47-d3ba-3a9e-9361-22dd5aaf8370 | -1.6245 | -53.3084 | 2024-11-23 13:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 2db00c3d-ac30-35f5-a06a-91d94774311e | -4.0737 | -48.9622 | 2024-11-23 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9221b5c1-2b82-3c51-a827-6fe1964af860 | -3.0949 | -44.3677 | 2024-11-23 13:50:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 18514129-0a90-3a6c-b379-f8b0b676fea0 | -3.8776 | -47.5461 | 2024-11-23 13:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ffcfc7d3-a6df-3a18-ae48-9fb307da55dc | -4.2606 | -48.6755 | 2024-11-23 13:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| dbdc4619-9f6c-3c5f-81bc-2dcdeee1f588 | -1.5493 | -54.3357 | 2024-11-23 13:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| d4163d59-4c3e-3db9-81e2-0adda514e6a1 | -1.6245 | -53.3084 | 2024-11-23 13:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2b4cb305-fee8-3f53-986e-6a7b14be07f2 | -5.7146 | -43.5261 | 2024-11-23 13:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| e719bbfa-3a1d-32d1-9bec-802cb467287b | -3.4658 | -44.6486 | 2024-11-23 13:50:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |


[Clique aqui para ver as próximas entradas](README72.md)
