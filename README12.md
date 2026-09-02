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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b00b600-59b2-312b-89d1-9fa918c9b44e | -8.4298 | -54.706 | 2026-09-02 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 6f04d50c-fc5f-37d4-9b7f-cef9d3b6dcc9 | -8.4669 | -54.7237 | 2026-09-02 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 684588cf-14fd-3b57-9a2f-1af501fe8d73 | -13.9855 | -58.672 | 2026-09-02 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f2c7fc82-9cff-3700-9d72-a6c45984088d | -12.1504 | -47.1283 | 2026-09-02 02:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| e4c661e8-a554-34f7-8223-6111f6007a8a | -12.1512 | -47.0833 | 2026-09-02 02:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 9dc36162-0a85-342e-9bfe-74da6f4fd463 | -6.6948 | -58.7678 | 2026-09-02 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 850b81f4-2c82-3a92-ac59-11b130915461 | -11.3331 | -50.6394 | 2026-09-02 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e0a3424c-5bb0-37cc-a631-59ca8a903ce2 | -14.0044 | -58.6902 | 2026-09-02 02:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 1cf869de-6ae0-373b-ae28-017822cc3230 | -11.3524 | -50.6159 | 2026-09-02 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 7c245c78-2749-30ea-9eb7-d434c0fcfb04 | -11.3579 | -45.4027 | 2026-09-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a22d50c1-b6f4-3ebc-a961-6d10322a1a20 | -12.1312 | -47.1309 | 2026-09-02 02:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9e557b40-86e2-35f0-81e3-1b22eecc07b5 | -8.4296 | -54.7262 | 2026-09-02 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1adce0eb-bbbf-3b2f-bedc-f4acc6624ff1 | -10.6971 | -46.1967 | 2026-09-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f2cfe38d-d651-3153-8e8b-dffd3b11d5f0 | -14.0047 | -58.6703 | 2026-09-02 02:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 6dd5ce07-e9b6-3254-aa5a-dbd6761dfd69 | -10.7962 | -44.7669 | 2026-09-02 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 072eb6c6-8de1-310a-967f-5b3933602e30 | -10.3956 | -49.9918 | 2026-09-02 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 72c90fdc-d527-3ec6-b469-215ea908fded | -8.4483 | -54.725 | 2026-09-02 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6e64de63-efaf-3888-b3b9-933db747fddc | -8.5728 | -63.1807 | 2026-09-02 02:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9b555380-e748-3cc8-8cd8-5d18d70a58ab | -11.791 | -50.5021 | 2026-09-02 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7cec0a8d-383d-3d89-b74c-bba2b9051d2b | -12.1324 | -47.0635 | 2026-09-02 02:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 3ea5d588-056f-3b0d-a0a2-80ccae6ed253 | -10.92 | -45.3483 | 2026-09-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| b91f6ccd-47c4-3bb8-88f4-d9aa1dec1489 | -13.9853 | -58.6919 | 2026-09-02 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| b6472309-978e-3e4a-880f-a35b20b5ccc4 | -10.7774 | -44.7463 | 2026-09-02 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a47e4749-38e2-3d7f-9c58-a19c02aae55b | -10.6967 | -46.2193 | 2026-09-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e325eb56-aa0f-3a26-93a1-1dde4acba919 | -11.7716 | -50.5258 | 2026-09-02 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 6d33097a-1a0a-3926-84dc-62d595a2db6c | -10.7158 | -46.2169 | 2026-09-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 21d93100-546a-3d0a-b179-784a9684f5c9 | -7.2006 | -60.6706 | 2026-09-02 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| eefb69af-7158-3c9f-a1e2-531d64d3ca0e | -10.9009 | -45.3509 | 2026-09-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 281.7 |
| f4445f2f-5dcf-3982-8aaa-648e7d76d3bc | -12.1516 | -47.0608 | 2026-09-02 02:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| f4e6ab42-6a0a-3c38-af62-bf5842769432 | -11.7906 | -50.5236 | 2026-09-02 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 389c3f21-5d86-3d34-b098-4d9b6210a645 | -10.777 | -44.7695 | 2026-09-02 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 475f881b-8f90-3fd5-a99e-b0575d416b1b | -11.3521 | -50.6373 | 2026-09-02 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| bcb23a0c-a88e-3764-9906-f4c1055614a3 | -11.3337 | -50.5966 | 2026-09-02 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e8257022-2eb8-3c61-b362-adbee92fdd34 | -10.7161 | -46.1942 | 2026-09-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b3e06d3f-4a38-3c3a-9e18-534e01399a03 | -10.9204 | -45.3253 | 2026-09-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1f7dd960-1904-3526-b7bd-0a73508673d5 | -12.132 | -47.086 | 2026-09-02 02:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b264fd32-6a5f-344c-baed-e406e0fc9041 | -10.9013 | -45.3279 | 2026-09-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 368.0 |
| 15351b9a-bb16-35dc-8b47-448d51bd609a | -12.8843 | -45.8183 | 2026-09-02 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 72c407f9-a3cf-3b01-a099-18271328ab19 | -6.6949 | -58.7485 | 2026-09-02 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| fee5ea8c-f140-32cf-b3d0-40b4d458ae5e | -11.3334 | -50.618 | 2026-09-02 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| b5280a1e-cbdc-3a11-93ef-b8704e1c27da | -8.5542 | -63.1814 | 2026-09-02 02:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5fa8a36a-890b-379f-b336-c5e0dd3d945b | -8.4671 | -54.7035 | 2026-09-02 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 8ce4bc55-986f-3503-97d9-d6630e76d215 | -8.5727 | -63.1996 | 2026-09-02 02:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3dc101eb-94d8-306e-962d-5730f91006fe | -10.6164 | -55.0284 | 2026-09-02 02:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5cc3ff5a-595a-33eb-a255-f8d36037162a | -10.3956 | -49.9918 | 2026-09-02 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 5c455232-31e3-3caf-ba63-dd39e4e2b906 | -10.9009 | -45.3509 | 2026-09-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 3fb1a52a-8df5-3d20-bd3e-32dc5e5a9882 | -10.7962 | -44.7669 | 2026-09-02 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b846fa57-c5b6-3522-babc-e57aaa51d877 | -11.3334 | -50.618 | 2026-09-02 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 290.5 |
| 5ac496da-0ec3-3242-a8bb-617f12b48d1e | -12.8843 | -45.8183 | 2026-09-02 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 42863576-f0ad-3dc0-9437-f0194414e394 | -11.3048 | -45.1575 | 2026-09-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| e18d013e-76f9-32a9-975e-23f9788d661a | -8.4669 | -54.7237 | 2026-09-02 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 348b384e-eacd-3b33-9794-c4127bddbfd7 | -12.1516 | -47.0608 | 2026-09-02 02:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| a4ef8766-5aa1-3f46-8896-0b50f84932f6 | -10.9204 | -45.3253 | 2026-09-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 03f3ca60-7c03-3a3e-93aa-1720bbdd6e44 | -10.6971 | -46.1967 | 2026-09-02 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 9c90dfe4-e0d4-3ad8-b9b9-b96403f66453 | -11.7719 | -50.5043 | 2026-09-02 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 0ffd9ee5-4d27-3099-bf88-32b8a3644ea8 | -10.6967 | -46.2193 | 2026-09-02 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e14936d9-e7f6-386a-bc4f-84216a7eb3c2 | -10.92 | -45.3483 | 2026-09-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 85f3b056-e2d2-38be-b353-cbd4269d00bd | -13.9853 | -58.6919 | 2026-09-02 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8f6e34a9-dd72-303f-a885-a210f7fb0fad | -11.7716 | -50.5258 | 2026-09-02 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 1c11003a-0edc-3374-b59b-681e78b8cfd9 | -8.4483 | -54.725 | 2026-09-02 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 2d2ba17e-a047-3450-817f-3b4e63f99fc5 | -12.1312 | -47.1309 | 2026-09-02 02:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2945ff4e-9882-3319-a49b-60e1271d5aae | -13.9855 | -58.672 | 2026-09-02 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 8ea2276e-3c99-30a9-a1bc-926de1434836 | -11.7906 | -50.5236 | 2026-09-02 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 241.5 |
| daa872b0-b040-3da3-b88f-7f99a8fab338 | -11.3144 | -50.6201 | 2026-09-02 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4ff49967-8516-3797-9772-97e3e9978991 | -8.4298 | -54.706 | 2026-09-02 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 8e712dcb-c78e-3b58-ae6f-d1af09b1c0a8 | -8.4485 | -54.7048 | 2026-09-02 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| c2e60198-d94e-387c-b160-83441510be3f | -11.3331 | -50.6394 | 2026-09-02 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f838304c-0430-3bba-a4c1-5bbcbb1b1107 | -11.3524 | -50.6159 | 2026-09-02 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 2b76131c-9637-3a81-bc2e-45b709d07880 | -8.4671 | -54.7035 | 2026-09-02 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b8328441-6cc2-304d-801b-4fa545796300 | -10.8822 | -45.3305 | 2026-09-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| cc897287-6b58-3912-9ed6-4e2ccda96c29 | -11.791 | -50.5021 | 2026-09-02 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 195.8 |
| c5fcdd6a-6267-32b2-96d4-a3f9d53b3fac | -17.0878 | -56.8534 | 2026-09-02 02:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 6643d745-5f5f-3c1d-8c33-1cca484061be | -10.7161 | -46.1942 | 2026-09-02 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3f32c69f-3a85-32a2-8f21-959de0aaa4e0 | -11.3337 | -50.5966 | 2026-09-02 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 13dbb79f-0cc7-35e9-a9f4-c4f52d44fd54 | -11.3147 | -50.5987 | 2026-09-02 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| c60e45ee-a00f-300f-9b73-847639702b92 | -7.2006 | -60.6706 | 2026-09-02 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 4103fa08-5ee3-3768-97d9-cd5e0d9aafdd | -12.1504 | -47.1283 | 2026-09-02 02:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 826fd932-a2c8-308a-8f98-38c9a67854bc | -12.1512 | -47.0833 | 2026-09-02 02:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 63360f9f-a48c-3381-918a-8dcc1c676c01 | -12.1324 | -47.0635 | 2026-09-02 02:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 457e8850-eac3-31bc-8ea2-1b5c115c08da | -10.9013 | -45.3279 | 2026-09-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| d5877f8d-c4c1-3d4c-b98d-856f1bfba549 | -8.4483 | -54.725 | 2026-09-02 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0404b169-2e43-3e20-ab6f-f2210cd070b2 | -8.1036 | -58.2749 | 2026-09-02 02:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e4c5a1e8-905e-3e75-a233-ab7fb13f1424 | -12.1324 | -47.0635 | 2026-09-02 02:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2a37d821-fd6a-3e49-82d5-7fa4e09fb55d | -11.3337 | -50.5966 | 2026-09-02 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 281.3 |
| cb14ace6-1b50-30f5-9b88-ec71d698b655 | -17.0878 | -56.8534 | 2026-09-02 02:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 7236338a-a876-37a6-8e7d-108795997642 | -13.9853 | -58.6919 | 2026-09-02 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e39e5318-e187-3e8d-9706-574364b96a25 | -11.3579 | -45.4027 | 2026-09-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| d9aebfb1-05de-3b0c-a9e4-36268837c95c | -8.4485 | -54.7048 | 2026-09-02 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| c2518d54-7183-38ef-aca3-52900dece47e | -12.1504 | -47.1283 | 2026-09-02 02:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1d6ea80c-92a5-34ea-b28a-825a15d06139 | -11.3334 | -50.618 | 2026-09-02 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 343.1 |
| 7e68b034-7ea8-3806-a5b4-a68e9d6d534c | -10.6967 | -46.2193 | 2026-09-02 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e97e25b7-427a-3dab-b7ed-7a1880f7dbae | -10.6971 | -46.1967 | 2026-09-02 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 48fda887-f6e0-357f-8c3d-e21204bfcc8a | -8.4298 | -54.706 | 2026-09-02 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 1d195d7f-9105-3017-a179-eaf84045461c | -10.92 | -45.3483 | 2026-09-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| cb6ff35a-8107-3ed1-9f69-0a800ef818e4 | -10.9013 | -45.3279 | 2026-09-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 2e20704d-bc1e-3d9f-9103-da07a8301591 | -11.3527 | -50.5945 | 2026-09-02 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 62577999-e399-3dd3-a659-76ae05d33529 | -11.3144 | -50.6201 | 2026-09-02 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b47ebf39-9550-3d13-98b4-139238b9294c | -10.7774 | -44.7463 | 2026-09-02 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 517e0002-0a79-3e93-a945-6c7559696879 | -8.4671 | -54.7035 | 2026-09-02 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| b12290ae-1b95-30a4-9e74-45b0388be5c0 | -12.1512 | -47.0833 | 2026-09-02 02:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |


[Clique aqui para ver as próximas entradas](README13.md)
