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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91bcf33-6d1f-388a-a4c5-872e406fb17b | -8.0575 | -43.114399 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0fddc7b1-2d65-3662-a1b1-34fb05eff12d | -9.4056 | -45.504799 | 2025-08-01 00:11:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 647e754c-a175-3021-baa5-4478ac41497d | -7.5869 | -44.803501 | 2025-08-01 00:11:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03b8c778-e13a-390f-86cf-7231ebb1b235 | -10.727 | -50.451801 | 2025-08-01 00:11:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4eaf020c-6ce4-39c1-8f5c-2b7792e9fcf7 | -12.5493 | -44.7271 | 2025-08-01 00:11:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a139157a-5670-3fc6-89d3-ff6ab56ce7e8 | -23.517599 | -47.852699 | 2025-08-01 00:11:00 | METOP-C | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69f14bd2-66b5-3368-ba45-ddbb72fe9812 | -3.6952 | -43.434601 | 2025-08-01 00:11:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ebd8c57-d109-3f62-8f28-2306d6c1e331 | -11.7593 | -45.0 | 2025-08-01 00:11:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9fd5feb-fd65-37cf-8c20-4ea74c8999af | -6.5723 | -41.537701 | 2025-08-01 00:11:00 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ecca3df-d784-34f3-bf4e-cf244ff351eb | -8.0397 | -43.126801 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 882c53ca-7e96-3014-b672-cd19c4a713b1 | -8.5111 | -43.308601 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a24df39a-dff1-3046-89c7-c775aba0b208 | -11.7569 | -44.9884 | 2025-08-01 00:11:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bac7996e-13c6-3548-ac1d-fd7d4ee006b9 | -9.3958 | -45.506901 | 2025-08-01 00:11:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a9612b00-3479-3552-ade8-cc59edee6821 | -7.2441 | -43.385799 | 2025-08-01 00:11:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e427f2da-41f1-36e8-ac08-db426c9f2a09 | -14.2023 | -42.847401 | 2025-08-01 00:11:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 56745846-f54b-3d09-a4fa-05cd5c48ae74 | -8.0361 | -43.1106 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d886d02d-456e-3b0e-9109-f7c0a982d98d | -15.686 | -43.209202 | 2025-08-01 00:11:00 | METOP-C | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| af7182dc-274c-32d9-857e-abc4c9703ffb | -11.7666 | -44.9986 | 2025-08-01 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| f5f367ad-777c-3940-b952-c308abd22400 | -9.4178 | -45.4906 | 2025-08-01 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 238b3475-9e71-3e2f-aa5d-e1d4a6a0c95c | -9.3989 | -45.4928 | 2025-08-01 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 83373735-09e9-3ca3-bd27-df8fb277cb9c | -18.6908 | -52.5722 | 2025-08-01 00:20:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 4e569184-3e6d-30ee-b64b-3a75712b2a9e | -18.6704 | -52.5973 | 2025-08-01 00:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a2ba0cb2-f994-3736-ab94-b805f3045c41 | -18.6904 | -52.594 | 2025-08-01 00:20:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 463216dc-41eb-3d71-81e4-cd46cc0c60ba | -23.5446 | -47.8293 | 2025-08-01 00:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| ed98419a-2ee4-38e4-bf2a-872f24d56587 | -18.6708 | -52.5756 | 2025-08-01 00:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 49d86666-7cf1-3272-a535-37bdd549a213 | -8.051 | -43.1237 | 2025-08-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 198.8 |
| c706111f-5e8d-3f26-b50d-b9bd9cc777a7 | -6.5258 | -56.2121 | 2025-08-01 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 893781a3-0d6c-3e42-ba4d-9f38d0b80c85 | -23.5234 | -47.835 | 2025-08-01 00:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 462.5 |
| 34ccfd3d-547d-3304-8f3c-a63d25be9bd6 | -23.5022 | -47.8407 | 2025-08-01 00:20:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.3 |
| b941af41-0140-3e16-aebd-537bbb43fd13 | -6.5074 | -56.213 | 2025-08-01 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 8a49dfbe-f857-3542-a444-beb14167e569 | -23.5242 | -47.8109 | 2025-08-01 00:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.2 |
| 9d01f5a1-31d1-3e58-8212-fc79e545c3c9 | -8.0321 | -43.1257 | 2025-08-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.6 |
| 1337243e-7dc4-398f-88c1-c10b6b048224 | -8.0324 | -43.1022 | 2025-08-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.6 |
| b86ff79d-dd89-356f-af0c-973aae9ceda0 | -8.0513 | -43.1001 | 2025-08-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 194.8 |
| f6815228-e17c-3271-8fd8-550b5d3e4e59 | -20.5347 | -46.10288 | 2025-08-01 00:24:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fe8a7fec-1fa9-3fbc-bb73-c56caa2a230f | -14.20724 | -42.85066 | 2025-08-01 00:24:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 365c3f13-6d7f-300f-b940-5130ecc89951 | -20.35146 | -45.99049 | 2025-08-01 00:24:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 444a81d6-2dc6-30c3-8ac9-548c341ed969 | -21.3844 | -43.76014 | 2025-08-01 00:24:00 | TERRA_M-M | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| da53091d-8a5e-3a72-8bf5-25de313a4944 | -20.70032 | -44.27657 | 2025-08-01 00:24:00 | TERRA_M-M | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 0a5e9caa-e49e-3364-828c-05595862bf37 | -20.7016 | -44.28616 | 2025-08-01 00:24:00 | TERRA_M-M | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 92bd5bbc-a841-3d0d-97e1-39915e418022 | -19.52564 | -45.33547 | 2025-08-01 00:24:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4c486f54-f1ed-3f4c-b7d4-78566983eae2 | -23.50934 | -47.83171 | 2025-08-01 00:24:00 | TERRA_M-M | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| d7315214-6148-30cb-8dc5-2ae5374baceb | -23.52048 | -47.82993 | 2025-08-01 00:24:00 | TERRA_M-M | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 561.4 |
| 191a37bd-29a2-3afc-9649-2294d5917560 | -14.76226 | -47.11726 | 2025-08-01 00:24:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e772df5-9f83-3931-ad0d-972152c692d5 | -21.17086 | -48.6451 | 2025-08-01 00:24:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| f90e1051-236e-3221-a27f-af41ed939a27 | -14.20573 | -42.84053 | 2025-08-01 00:24:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0b221462-60cb-3919-acc4-e935431b5d9d | -20.44445 | -46.42819 | 2025-08-01 00:24:00 | TERRA_M-M | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f07e7b32-35d1-3aa2-9af3-0f143fb2e917 | -22.51921 | -47.21851 | 2025-08-01 00:24:00 | TERRA_M-M | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 122859cb-aaf0-3073-9f90-7217ed1c04f3 | -18.67382 | -52.59989 | 2025-08-01 00:24:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 164.1 |
| d8393322-f96c-3d09-bb2e-0d1140e1c7d3 | -21.09763 | -42.76139 | 2025-08-01 00:24:00 | TERRA_M-M | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a669288a-9567-3f95-8f76-34abf32c9e08 | -23.04456 | -46.65148 | 2025-08-01 00:24:00 | TERRA_M-M | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 50e0d5a8-18ec-3d49-a189-2bd2f8553230 | -23.52217 | -47.84576 | 2025-08-01 00:24:00 | TERRA_M-M | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 166.9 |
| 3c0ce5d2-e097-39fd-a603-ae646990c785 | -18.67125 | -52.57138 | 2025-08-01 00:24:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 82026080-b684-3c15-8f4b-51455e900dd5 | -20.01095 | -47.38567 | 2025-08-01 00:24:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3d311e3f-76a4-331b-909d-70eb24c0b9a3 | -15.6897 | -43.20836 | 2025-08-01 00:24:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 9.1 |
| c41bece1-9810-394c-9d92-e56273560946 | -19.70533 | -46.79767 | 2025-08-01 00:24:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4f29e96b-a990-303b-ae26-8a6d610465b3 | -21.24167 | -48.5641 | 2025-08-01 00:24:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a5461fba-361a-3686-85da-ad55dda8dd1c | -18.675 | -52.60597 | 2025-08-01 00:24:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 6a77c885-c662-3b5e-ba09-5a5ba313ee4e | -18.67224 | -52.5775 | 2025-08-01 00:24:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d6984059-bd40-3e39-9dcc-84192886ac5c | -19.70748 | -46.80292 | 2025-08-01 00:24:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1131b0a2-277f-33f4-a041-7cbf28623bf0 | -16.12788 | -46.87772 | 2025-08-01 00:24:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| db955b11-e7cf-34ac-b264-346e69056ed3 | -12.09301 | -49.19469 | 2025-08-01 00:26:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a0e568de-5433-3591-aeb0-fb7a32dffa0c | -7.7393 | -45.08339 | 2025-08-01 00:26:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b2a98b1c-ab3d-39c9-aead-e1279bd2644b | -11.77515 | -45.02036 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e190ca26-dd9d-3c34-976a-e5350cecefef | -9.7403 | -48.67079 | 2025-08-01 00:26:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a89a9905-1975-35bd-9630-b4dbdc9cccf7 | -8.43271 | -47.4972 | 2025-08-01 00:26:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 93fe3745-c8b2-3994-8fe9-e66bc5e895fe | -7.59041 | -44.81596 | 2025-08-01 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c4ccc009-51b0-30cc-b907-7cc280b0f95c | -7.24851 | -43.39149 | 2025-08-01 00:26:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| ad4f668e-c1ff-33c9-83cb-62090bab966c | -8.59159 | -45.51364 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ed0efbbb-ae4a-3aa7-ad80-69301d48c95f | -10.44499 | -47.27465 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 711388b4-6632-31a6-b4e1-340fb9acc848 | -8.51747 | -43.31829 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 57a0054e-54c6-3abb-8932-8f1aac6021b1 | -11.97443 | -46.67639 | 2025-08-01 00:26:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d9078ac9-73b9-3452-9b35-e885f6059522 | -11.52854 | -44.32186 | 2025-08-01 00:26:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e96a72ea-6dff-35b7-bcbb-a852fbd30b53 | -8.05712 | -43.11159 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 7a14fe01-9c84-3bac-a7a8-b511bac341cc | -8.33786 | -50.5668 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d7cd3e7-3138-3e63-92b7-1510e274aac9 | -9.39881 | -45.48813 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b2fd79fd-fcec-3ef5-b20c-215fe4236af9 | -7.35058 | -44.16698 | 2025-08-01 00:26:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3522ad4b-8911-3401-a9e6-8da14f2a14f2 | -7.58904 | -44.80647 | 2025-08-01 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 487bdfe0-4467-3143-8e93-3ada664ae12f | -8.03729 | -43.1146 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 303.5 |
| 7575630f-1a4a-38bc-b27f-1e7f55afeb14 | -11.94985 | -46.69909 | 2025-08-01 00:26:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a9bbe484-126f-31d5-b881-a0b050e389a9 | -12.43615 | -44.75006 | 2025-08-01 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f98f63c0-241c-3dd3-9ff2-179369a030c1 | -10.79359 | -47.26977 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b736fee-1a53-336e-806b-7d39fb419d80 | -8.0472 | -43.1131 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 149.7 |
| 921f01a6-8f0a-3aaf-9741-592ab75a03e2 | -6.54395 | -43.61455 | 2025-08-01 00:26:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7e7ae865-5f00-390c-a414-5c5719bf4959 | -9.40768 | -45.48683 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d380d86d-af7e-369c-9915-fc02272fdc2c | -12.80868 | -45.44158 | 2025-08-01 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e97cffa8-7bfa-3def-8149-2e4e5e48b1a0 | -9.81138 | -47.75623 | 2025-08-01 00:26:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e33999d5-fd82-3967-8831-056e8f8d5b9a | -8.32876 | -50.58207 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f6189233-51b8-3673-8fec-87d1886a40a6 | -11.77606 | -47.39071 | 2025-08-01 00:26:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c14a38d-2009-3c01-b458-582c648b2f35 | -13.22562 | -47.23405 | 2025-08-01 00:26:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 735aabd9-d16f-305a-b2ea-c7e3bf284faa | -10.60394 | -45.27251 | 2025-08-01 00:26:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 66f30fe1-2b11-3f52-9653-dfed0071000d | -9.40131 | -45.50604 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a5245730-1143-3cec-979c-25e6f4663ac0 | -12.64504 | -48.08737 | 2025-08-01 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| acf0e4c2-3bb2-3344-a6d7-83aad6cb1bc8 | -10.43458 | -47.26635 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 33485d42-75ba-365c-868b-178b6b661355 | -11.76376 | -45.00369 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 2ed9ca76-053d-396b-a196-01ef991f4642 | -8.03894 | -43.12594 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 214.5 |
| afca3cf7-982c-3fc0-8560-d3616ab8e431 | -12.70956 | -47.79761 | 2025-08-01 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 22c4ae4d-cd90-3c8d-bed0-c81c08e74ef3 | -7.34582 | -44.64596 | 2025-08-01 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 273a7391-72cb-33cf-acbc-81b043c404f2 | -8.24865 | -49.58676 | 2025-08-01 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e22e01fa-04d7-3b46-8c18-14b08f85b801 | -10.73341 | -50.48805 | 2025-08-01 00:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README3.md)
