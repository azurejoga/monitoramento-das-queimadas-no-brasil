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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1a570f4-98a2-3c33-acda-9ba21368c26f | -11.2148 | -53.833 | 2024-12-12 06:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9051deff-de59-3f6c-94ff-865b8d23d826 | -11.1959 | -53.8348 | 2024-12-12 06:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b64ea17b-f307-36e7-a999-7871b9bdffe8 | -6.9344 | -43.5401 | 2024-12-12 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9b57e779-cc30-32d7-bcee-40897ed72341 | -6.9346 | -43.5168 | 2024-12-12 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 3b4e04b4-0ac2-307d-90e8-48263c64e719 | -6.9349 | -43.4934 | 2024-12-12 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| dbb57f9c-a973-3411-b440-515a0860359b | -14.74947 | -52.64826 | 2024-12-12 06:12:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| afe520bf-5641-37da-aef4-4d0aa58e4bdb | -15.02773 | -57.60771 | 2024-12-12 06:12:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c3cfc60b-3fbb-3885-aaa5-f79cfd55fb2a | -14.75269 | -52.6361 | 2024-12-12 06:12:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f267ec19-9bdc-3359-947b-ff2d9f545505 | -14.75042 | -52.65546 | 2024-12-12 06:12:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1157d828-6e78-35d8-b122-ab57c39b1d47 | -15.08646 | -59.63924 | 2024-12-12 06:12:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c8343345-8cdb-300a-ad4d-3def5b694c72 | -16.08131 | -60.0829 | 2024-12-12 06:12:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cae23118-137a-3785-a6b6-c5e1c5bcd662 | -16.07987 | -60.09222 | 2024-12-12 06:12:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 64283030-8313-3286-a4b1-92284c3593e6 | -6.9344 | -43.5401 | 2024-12-12 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 195322c9-e2e3-3718-a060-0b21742b5ffe | -6.9349 | -43.4934 | 2024-12-12 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 7c6885d4-eb83-3ecf-a54f-c4d361aa2dee | -6.9158 | -43.5185 | 2024-12-12 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e1df666b-15b1-3750-82a1-21484a9fcb98 | -6.9346 | -43.5168 | 2024-12-12 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 342f6d96-32cd-39a1-a518-97d1e52a7f66 | -6.9346 | -43.5168 | 2024-12-12 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 98ba5e5d-a192-3e77-b9de-44a08842e4d5 | -6.9346 | -43.5168 | 2024-12-12 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 5380e4ac-9589-30c1-86d5-e047c807e07a | -6.9344 | -43.5401 | 2024-12-12 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 323238fc-4129-33a2-a51d-89e0c4cc2e00 | -6.9158 | -43.5185 | 2024-12-12 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 794d9324-9a47-3c89-aec2-1ad16ab85369 | -6.9346 | -43.5168 | 2024-12-12 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| e02cb58f-2aee-3e3e-a512-2c8977572f15 | -6.9158 | -43.5185 | 2024-12-12 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3076a952-e958-3739-9348-96a9fa0eab1a | -6.9344 | -43.5401 | 2024-12-12 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d0b827c7-ffe6-3d03-ab70-46871261b90c | -6.9158 | -43.5185 | 2024-12-12 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0ec5c809-df23-33ff-9977-03560b226c23 | -6.9346 | -43.5168 | 2024-12-12 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f58e8734-eddd-37a1-91d4-9581f8ca3b41 | -6.9158 | -43.5185 | 2024-12-12 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 7b700c13-4da9-3b7d-be2d-d494375bf78b | -6.9346 | -43.5168 | 2024-12-12 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 91490eaa-fabe-3364-bdbe-8e1a3047cb40 | -6.9158 | -43.5185 | 2024-12-12 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 0a0e5ae0-eb74-3ddb-bfaf-b314c54061ba | -6.9346 | -43.5168 | 2024-12-12 07:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 66a8c337-c439-364e-96e0-df0fa38a635b | -6.9158 | -43.5185 | 2024-12-12 07:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4919d992-abe2-38a7-bc97-dd22cc8568ac | -6.9346 | -43.5168 | 2024-12-12 07:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a5ca8e53-78fa-3762-aa2f-cfbd15a62554 | -6.9346 | -43.5168 | 2024-12-12 07:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| c59834ff-f447-3159-8f8b-1c778cfe9685 | -6.9158 | -43.5185 | 2024-12-12 07:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| be30e4cc-6ec9-314c-a1e9-0c8be0f4dec2 | -15.9905 | -57.1647 | 2024-12-12 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| e2bbc1e8-ceea-3918-b3b6-fb41d1bcb42e | -7.55767 | -35.41889 | 2024-12-12 12:01:00 | TERRA_M-T | MACAPARANA | PERNAMBUCO | Brasil | 2609006 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| fc6797b9-d982-336d-a73b-0e946113972e | -6.10137 | -37.58173 | 2024-12-12 12:01:00 | TERRA_M-T | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1bcbd937-9c72-38c4-82e1-60b8458a2dbf | -7.2148 | -38.05373 | 2024-12-12 12:01:00 | TERRA_M-T | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 69f37684-9908-3a39-811d-1565534a0a8b | -5.9349 | -38.66403 | 2024-12-12 12:01:00 | TERRA_M-T | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| fdb62e1e-1e82-38ab-a9ca-20d8866ab08a | -7.03976 | -37.86344 | 2024-12-12 12:01:00 | TERRA_M-T | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 6031670b-cca6-3765-a365-721800746940 | -6.06237 | -38.17631 | 2024-12-12 12:01:00 | TERRA_M-T | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 11.0 |
| d5f8d5c0-0a76-3866-b8bb-a22cf13fae51 | -3.6056 | -41.68303 | 2024-12-12 12:01:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| ed6ec280-2b82-37c4-ae14-536720dafc58 | -6.13503 | -42.55315 | 2024-12-12 12:01:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| e531c329-8bc5-3b50-b0bd-1cc0524a8568 | -2.96495 | -41.8187 | 2024-12-12 12:01:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ea0e1e53-f8d9-37f7-976f-5760861d5b91 | -6.27063 | -38.57294 | 2024-12-12 12:01:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 59373a5d-e4a2-3742-9538-7f11e4e04366 | -5.77705 | -39.04741 | 2024-12-12 12:01:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 2081db1d-3398-31c4-a091-7ccc57f2519e | -3.28922 | -41.24887 | 2024-12-12 12:01:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 25708544-b3f7-3f3d-8521-3d8160858d04 | -5.69973 | -40.18748 | 2024-12-12 12:01:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4a4617cd-b3cf-36a9-8048-9eb4a5a55b52 | -3.29281 | -41.25634 | 2024-12-12 12:01:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 1447acea-e371-3b47-a432-77594645553c | -6.21658 | -35.27046 | 2024-12-12 12:01:00 | TERRA_M-T | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| f8462f8e-38da-3712-b141-3e7844b372dd | -2.8577 | -42.07552 | 2024-12-12 12:01:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6797fb4a-ff5d-3c00-978b-1a2fe74b7650 | -6.90465 | -37.89482 | 2024-12-12 12:01:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 25.7 |
| e9388214-a545-3fb4-aea6-5b876d409bad | -3.29484 | -41.24303 | 2024-12-12 12:01:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 19.8 |
| c8abf984-8686-3d34-8a32-64029332e0f0 | -6.90593 | -37.886 | 2024-12-12 12:01:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 35fbfd9e-6d95-38db-8a38-4472cb7004f1 | -2.91228 | -41.94238 | 2024-12-12 12:01:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 20f7abc4-250c-309a-9f64-161529009078 | -3.67897 | -42.41941 | 2024-12-12 12:01:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 8e25a23c-80cf-3ffe-9229-f376a7ac6b2d | -4.85091 | -39.00507 | 2024-12-12 12:01:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b7842b63-a44c-38d3-8d41-9beb69184e8d | -6.21801 | -35.26011 | 2024-12-12 12:01:00 | TERRA_M-T | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 4f733607-8044-357d-bbba-92a214c4525f | -3.44322 | -41.53259 | 2024-12-12 12:01:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 18847cd1-bdbc-3f18-9bfa-f926e879cdb6 | -3.59768 | -41.67414 | 2024-12-12 12:01:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 896fa245-7b24-3766-8e55-16767688b22c | -5.42255 | -40.66885 | 2024-12-12 12:01:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2dfea7a1-3440-3a82-a938-ba87920f245d | -4.59993 | -40.47484 | 2024-12-12 12:01:00 | TERRA_M-T | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| d6f73cce-3178-32ee-86ab-10b4aafaab85 | -6.85673 | -37.91504 | 2024-12-12 12:01:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 18.7 |
| b2e31352-a36d-3be2-a34a-0c87772f33a9 | -8.85043 | -40.42509 | 2024-12-12 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b445061a-ab4b-3d8e-baef-dd882dd12780 | -7.62144 | -37.79393 | 2024-12-12 12:04:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 5731a5dd-6eea-34ec-94b7-a9f9c6ff61e7 | -7.79278 | -40.26031 | 2024-12-12 12:04:00 | TERRA_M-T | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 0b41b561-8d6d-373e-b9ae-4ebc6176b2ee | -11.52408 | -41.4149 | 2024-12-12 12:04:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 68489eb2-57ed-36da-8b6a-b14ecb01141a | -9.20018 | -37.13354 | 2024-12-12 12:04:00 | TERRA_M-T | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| d377ae7b-04d3-3d75-adf1-4cbf291aea90 | -12.43913 | -38.60258 | 2024-12-12 12:04:00 | TERRA_M-T | TERRA NOVA | BAHIA | Brasil | 2931707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 027b935b-ccb5-3825-9073-a08fe69de0ad | -9.15945 | -37.73903 | 2024-12-12 12:04:00 | TERRA_M-T | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3cae5102-b32f-3897-b706-a78311afd252 | -7.34965 | -39.0872 | 2024-12-12 12:04:00 | TERRA_M-T | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2bed5a70-9cf3-3ea4-bc2b-b241fba58390 | -7.4883 | -37.24594 | 2024-12-12 12:04:00 | TERRA_M-T | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7f4341d2-f1bf-340e-a9be-a9a70b109898 | -11.60804 | -41.53269 | 2024-12-12 12:04:00 | TERRA_M-T | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e442bd87-f43e-378b-b8a7-72818ab95709 | -10.60662 | -37.29031 | 2024-12-12 12:04:00 | TERRA_M-T | SANTA ROSA DE LIMA | SERGIPE | Brasil | 2806503 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 11722f05-6b27-3295-915a-86b4f7f6187a | -7.58342 | -37.79162 | 2024-12-12 12:04:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b8f0698c-ed23-3fe3-99db-fa5ec333aef8 | -8.38503 | -35.32899 | 2024-12-12 12:04:00 | TERRA_M-T | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 52a5a3c3-6cf9-3aa4-b5de-2995fedcb29b | -9.62876 | -36.97057 | 2024-12-12 12:04:00 | TERRA_M-T | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 303f2fb2-7f1b-3f90-b5e6-09a4d99dcc0c | -10.43135 | -38.01257 | 2024-12-12 12:04:00 | TERRA_M-T | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 21b7f153-2206-3ddd-b96c-73ead1d6492f | -8.6605 | -36.90819 | 2024-12-12 12:04:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 33.8 |
| d0a7a5e2-4a93-3e87-ab9d-9f5b25a77499 | -9.11082 | -35.78778 | 2024-12-12 12:04:00 | TERRA_M-T | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 510fe4a8-51de-3a51-b76b-56eebdb48357 | -8.30745 | -36.79696 | 2024-12-12 12:04:00 | TERRA_M-T | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| cb93e110-6931-34b4-9c26-bfbddb0bad30 | -9.19888 | -37.14278 | 2024-12-12 12:04:00 | TERRA_M-T | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4c07561a-ce61-30c3-bceb-7aa229445ecd | -7.58469 | -37.78279 | 2024-12-12 12:04:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 57c14b1e-d151-3c64-97f7-8db18749a967 | -11.19642 | -38.32753 | 2024-12-12 12:04:00 | TERRA_M-T | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 25a054f9-ef84-3c14-b554-8ebfd45cefa6 | -8.64722 | -40.90627 | 2024-12-12 12:04:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8dd9c20c-d8b5-35fa-aee5-55ccd41abef3 | -7.54275 | -37.30832 | 2024-12-12 12:04:00 | TERRA_M-T | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2f722dad-af52-3435-aeb8-c57e5e53c03b | -8.37874 | -36.87971 | 2024-12-12 12:04:00 | TERRA_M-T | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 057bb997-337e-3ab9-876e-5fcb1901fda3 | -9.40184 | -37.47 | 2024-12-12 12:04:00 | TERRA_M-T | SENADOR RUI PALMEIRA | ALAGOAS | Brasil | 2708956 | 27 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 3e128679-88eb-3fe2-8380-ad2594347c3c | -8.65148 | -36.90694 | 2024-12-12 12:04:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e878c9b4-d77c-3e1c-9a78-a205a55f80d1 | -8.46305 | -40.29118 | 2024-12-12 12:04:00 | TERRA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f37a6cd3-9e7f-3ec6-a259-a219036e8865 | -7.40445 | -38.90036 | 2024-12-12 12:04:00 | TERRA_M-T | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 6aee657b-6a52-315b-8276-30e7dfd98d2c | -7.62534 | -37.70425 | 2024-12-12 12:04:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 3a883041-96e8-3884-892b-f4e054011c60 | -10.43263 | -38.00357 | 2024-12-12 12:04:00 | TERRA_M-T | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| aa74ef33-83b0-31c5-99ca-9607d03601b5 | -11.20196 | -40.74729 | 2024-12-12 12:04:00 | TERRA_M-T | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| d3f12179-e129-3fef-bde8-8e812a209820 | -9.92615 | -36.27535 | 2024-12-12 12:04:00 | TERRA_M-T | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 7564c746-6a8e-3fa6-90e6-6277b72de7f1 | -7.72098 | -37.80539 | 2024-12-12 12:04:00 | TERRA_M-T | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 9b9cdf3e-eeea-3d13-96e9-98075e41e1c0 | -8.53582 | -36.29119 | 2024-12-12 12:04:00 | TERRA_M-T | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1ac51076-408a-3ab0-9871-fa4e26dc3c9f | -7.62287 | -37.65873 | 2024-12-12 12:04:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 3b998439-ad4e-3646-b263-b679cb3d5ba5 | -9.27652 | -37.76785 | 2024-12-12 12:04:00 | TERRA_M-T | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 99ba8171-4789-32c8-bf05-53f8450bef6a | -7.83696 | -37.89101 | 2024-12-12 12:04:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 35904902-210a-38fe-863f-5fc06b685ea4 | -7.35096 | -39.07825 | 2024-12-12 12:04:00 | TERRA_M-T | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |


[Clique aqui para ver as próximas entradas](README35.md)
