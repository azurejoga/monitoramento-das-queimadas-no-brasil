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
| cdee9d04-5401-3365-8ac4-f0842bff4b6a | -5.9746 | -39.681 | 2025-02-13 00:08:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5f4d0905-517d-354c-88a1-ab74affcd538 | -9.9731 | -36.188702 | 2025-02-13 00:08:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4baf9733-5111-338d-96f6-564c1b99afe5 | -9.9615 | -36.183102 | 2025-02-13 00:08:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33add681-cd79-3def-9fed-a9aa3f43f469 | -11.4574 | -40.620499 | 2025-02-13 00:08:00 | METOP-C | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e7d522ff-f962-34d8-9d5e-d821128b43c6 | -6.3482 | -41.921001 | 2025-02-13 00:08:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b90ec308-77a0-3cbc-80e1-8c2187f39726 | -7.7249 | -35.157902 | 2025-02-13 00:08:00 | METOP-C | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fdd0e256-a625-3dc8-b8d3-66b9d0e9ccc0 | -9.9633 | -36.191002 | 2025-02-13 00:08:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80530394-7323-34cf-b11e-aa60dc9883f4 | -6.5971 | -39.382099 | 2025-02-13 00:08:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2af64a2f-67d6-347c-a357-f45c68fc9228 | -6.761 | -35.182999 | 2025-02-13 00:08:00 | METOP-C | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1a1f6a7-3c9d-3601-a9a2-4a132b730e92 | -8.1143 | -38.893398 | 2025-02-13 00:08:00 | METOP-C | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ded22954-0a01-313f-b50e-403b2f0fe2c7 | -11.4557 | -40.612999 | 2025-02-13 00:08:00 | METOP-C | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 087e6e7d-6afb-3784-b145-19552377452c | -8.9587 | -40.575199 | 2025-02-13 00:08:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1d2d9b98-b3cb-331b-a0c8-16564698c96f | -9.3523 | -35.574001 | 2025-02-13 00:08:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbee6440-c951-369d-b4d8-63c09be09bae | -5.9762 | -39.687801 | 2025-02-13 00:08:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f2a28501-1d97-3b14-ae3c-cec91484d11d | -5.973 | -39.674099 | 2025-02-13 00:08:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 46c1aafe-d837-39f8-af7f-95fb520c627b | -9.2412 | -40.549999 | 2025-02-13 00:08:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 8c31c606-c8bc-33ea-86d5-a3ded22a5726 | -5.7807 | -42.601898 | 2025-02-13 00:08:00 | METOP-C | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| adf92077-db9b-30e6-9e04-6c5802498eb0 | -6.5986 | -39.388901 | 2025-02-13 00:08:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a07c3642-2144-3d47-b6b6-03e6cb8a69f8 | -6.0853 | -42.676899 | 2025-02-13 00:08:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 030b7b78-bc97-36ee-94a9-ee5a03d77cbb | -8.9603 | -40.582401 | 2025-02-13 00:08:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 49140acc-d866-3193-a48d-9929fe4ed4b0 | -8.9489 | -40.577301 | 2025-02-13 00:08:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9f2cf2ae-b7d4-31d3-9651-0116bdb84f24 | -20.94983 | -43.17318 | 2025-02-13 00:24:00 | TERRA_M-M | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| b0f821cd-07a7-301f-94fd-2ec64f85871b | -22.56208 | -42.04335 | 2025-02-13 00:24:00 | TERRA_M-M | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 085a7066-1475-3c9c-9bc2-9052538c2b46 | -22.84724 | -42.0467 | 2025-02-13 00:24:00 | TERRA_M-M | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8b6045a2-3a3e-3678-8238-dc1cd22fa5f8 | -11.45276 | -40.61074 | 2025-02-13 00:26:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 079b92ba-fdf9-3479-86ea-c8a1ef93d04d | -12.64583 | -43.80968 | 2025-02-13 00:26:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ef443600-cd68-343f-b9e2-ea1f588aa30c | -14.96072 | -42.88857 | 2025-02-13 00:26:00 | TERRA_M-M | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7881d1c0-48f1-33e9-8a1b-a39b5c8d57f4 | -11.59599 | -44.85769 | 2025-02-13 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8ba6aa33-7cc0-327b-9c05-5d547b6036e3 | -6.7717 | -35.18595 | 2025-02-13 00:28:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 7bcf52bf-464e-3ca2-9cdc-1d52cd718c47 | -6.60019 | -39.37793 | 2025-02-13 00:28:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| df0549c8-293d-35c1-a877-80c9b9005933 | -8.96009 | -40.58633 | 2025-02-13 00:28:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5d6a1940-be65-3289-9477-09e8574b118c | -8.72411 | -44.01377 | 2025-02-13 00:28:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9105418a-460a-320d-86c6-016d764ba694 | -7.72635 | -35.13735 | 2025-02-13 00:28:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| 8b32fc2c-f7ab-3e3b-85de-10814d85dc52 | -7.779 | -35.18451 | 2025-02-13 00:28:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| e4248b3d-4f81-31e5-b6c2-a6f947cbe01d | -5.97835 | -39.67618 | 2025-02-13 00:28:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 24.6 |
| c6531c12-a360-341f-872c-0b16efaf75d3 | -5.85343 | -44.24883 | 2025-02-13 00:28:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8edc0f32-51fe-33cc-bc72-4a764aac4dff | -8.72288 | -44.00467 | 2025-02-13 00:28:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c30791c9-8bb6-37c2-a3a2-ec64616352df | -7.66868 | -44.58587 | 2025-02-13 00:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48012ccf-057f-395e-8119-eabbd08aff36 | -6.34753 | -41.92015 | 2025-02-13 00:28:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a150bc17-c365-34b4-9ab2-018a87c35f04 | -7.25054 | -45.71138 | 2025-02-13 00:28:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b36e955e-6f69-33ea-9771-d0abf44ea7fb | -7.64595 | -45.23155 | 2025-02-13 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 555e8ff3-3705-3ec0-839e-f83cc34d1b91 | -6.60221 | -39.39131 | 2025-02-13 00:28:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 27d6c55a-6b9b-3482-acdb-ff1abb85fdf9 | -8.95859 | -40.57588 | 2025-02-13 00:28:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 29def3c8-7f6e-30bb-9302-4888396e3520 | -5.78123 | -42.60685 | 2025-02-13 00:28:00 | TERRA_M-M | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 40056b96-9454-3141-b3bf-01a8b5a0d1c7 | -10.65636 | -44.48715 | 2025-02-13 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c246c77d-2d7d-39f9-a591-567a88e27b5d | -5.97359 | -39.68325 | 2025-02-13 00:28:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 26.5 |
| fb561f74-04d3-3af0-9285-bcfca16c4cfa | -6.8809 | -43.87673 | 2025-02-13 00:28:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 172a92c7-6b72-37ec-881a-bb8527a122e1 | -7.64727 | -45.24133 | 2025-02-13 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 415934e1-cad9-3696-9cf2-47168893a6f4 | -7.77967 | -35.17896 | 2025-02-13 00:28:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| c9a6d419-48fd-3571-a919-16affbcb3f6e | -7.14562 | -45.28216 | 2025-02-13 00:28:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6dfc0437-9c10-33f9-a8e3-a8e81e0f5f05 | -10.5352 | -44.67639 | 2025-02-13 00:28:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7ff9c43a-2c4d-342f-98ea-c2634cae6b3b | -5.77993 | -42.59773 | 2025-02-13 00:28:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2b7bf40b-8bfc-3ee7-acd4-66293ead61ed | -7.22594 | -44.7163 | 2025-02-13 00:28:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bbc39379-74a2-3891-a7dd-1e38b13a1fb9 | -7.24917 | -45.70122 | 2025-02-13 00:28:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 36bd67e5-bcce-3fff-864f-63f4eeb71faf | -9.24209 | -40.55743 | 2025-02-13 00:28:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fc7fe4ff-69e7-3907-874e-98f812f0fa4c | -7.13763 | -45.27979 | 2025-02-13 00:28:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c00e2f66-cb31-37ba-8ce5-a5256aca9ce2 | -5.97174 | -39.67042 | 2025-02-13 00:28:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 5b021a1b-0bd6-34db-be53-a51cf0eebef0 | -7.73071 | -35.16447 | 2025-02-13 00:28:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 46.1 |
| b74407ec-752d-38e5-94f3-34d72ea47a8e | -6.42386 | -43.77356 | 2025-02-13 00:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79d6994b-4ca4-387a-9770-9b6e74f597cf | -9.24059 | -40.54699 | 2025-02-13 00:28:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 26ce6cdd-f7e4-3afc-b26f-36aa1a7fdcd1 | -8.94907 | -40.57731 | 2025-02-13 00:28:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 591af342-c546-3a59-99ea-90b3eefe84d2 | -21.885599 | -56.252602 | 2025-02-13 00:52:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 541753a5-5d5f-3eec-b367-b84fbc16d4ca | -21.8874 | -56.261902 | 2025-02-13 00:52:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ea072d37-872c-33f4-a881-986a8b8de204 | -21.972 | -57.5746 | 2025-02-13 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8b08d849-b251-34b9-b5dd-9848ec667b53 | -21.0844 | -56.379002 | 2025-02-13 00:52:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d7edd03b-a45d-3552-9a61-264fda700f10 | -17.328501 | -53.7281 | 2025-02-13 00:52:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 39b73386-9c3b-3da7-aeee-4d3bed639154 | -12.402 | -43.787899 | 2025-02-13 00:52:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3f9b18d-f726-3257-9689-d97e7940b4bd | -21.884501 | -56.264198 | 2025-02-13 01:45:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6165ade1-6109-3bde-8726-297760fa111e | -10.32344 | -37.08377 | 2025-02-13 03:17:00 | NPP-375D | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f01a1c53-f456-37fe-b796-3c9ae9fccf23 | -11.15515 | -38.05088 | 2025-02-13 03:17:00 | NPP-375D | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 785fdcda-d452-3153-ac02-12090e85adf3 | -8.95779 | -40.58072 | 2025-02-13 03:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e988e890-8216-3456-b0d4-5ddde213d116 | -9.45557 | -35.58045 | 2025-02-13 03:17:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2c973182-299c-35e7-9678-0eb0e623ddc0 | -10.82514 | -37.16548 | 2025-02-13 03:17:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a3ad8bb6-ad73-3be0-a0c2-b22fa25f3b21 | -8.95384 | -40.57673 | 2025-02-13 03:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9714a073-a51c-3be3-8639-22316dc49a5f | -9.4513 | -35.57965 | 2025-02-13 03:17:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 7d485072-f526-355e-910b-85e4d40d7afa | -10.69518 | -37.04851 | 2025-02-13 03:17:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ece83e55-cb41-323b-9dcf-85afde9a5fab | -8.5183 | -36.06443 | 2025-02-13 03:17:00 | NPP-375D | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b2aaa38-c344-33c9-afe1-0edc52c18dcf | -8.9518 | -40.57956 | 2025-02-13 03:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6366f763-135d-371b-b9d0-86fc791f599d | -9.45202 | -35.57564 | 2025-02-13 03:17:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 0498822d-f9f0-351f-9b7d-4e2e4cec2eb6 | -10.78861 | -37.25985 | 2025-02-13 03:17:00 | NPP-375D | AREIA BRANCA | SERGIPE | Brasil | 2800506 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9864cf12-cf90-3641-be27-50554c30bc36 | -8.11421 | -38.89489 | 2025-02-13 03:17:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a6aedf7c-8f4a-3677-b2c9-cf0367829313 | -9.45628 | -35.57642 | 2025-02-13 03:17:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 782f9ae0-b7a5-3f61-9942-8a9422e4637f | -8.10874 | -38.89396 | 2025-02-13 03:17:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2b783a7-603c-38cc-9d08-bb3018b55723 | -10.78774 | -37.26458 | 2025-02-13 03:17:00 | NPP-375D | AREIA BRANCA | SERGIPE | Brasil | 2800506 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 8150ccb4-d48a-3904-8383-4be4809e2577 | -9.44978 | -35.57571 | 2025-02-13 03:17:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c1ba16ae-ddb8-3b93-b96e-9eafcea8045d | -6.59869 | -39.38185 | 2025-02-13 03:19:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f4f0cd4-f188-32d4-ad83-d9fc85df9459 | -7.38996 | -35.25476 | 2025-02-13 03:19:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| cc6f8c31-ce64-338b-91b8-943880ae6c71 | -6.59795 | -39.38588 | 2025-02-13 03:19:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c1fe1f9-2ea2-3cb8-b83a-e267d0c7973e | -7.38564 | -35.25402 | 2025-02-13 03:19:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 65f32861-befb-3b43-9f5a-deb8bc6770cd | -6.9914 | -34.98163 | 2025-02-13 03:19:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 9a71b818-48de-3130-a6cd-9ec8d4fe8bba | -7.38492 | -35.25819 | 2025-02-13 03:19:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0d1d8527-4f70-3d13-a061-e174b067a192 | -12.41786 | -43.80464 | 2025-02-13 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7d491a5-b411-3358-ab93-23b7d11acacf | -12.41797 | -43.80564 | 2025-02-13 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf56ad42-a177-3b2c-aa0e-8bd3ab47f7e6 | -12.76601 | -39.8093 | 2025-02-13 03:19:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ca348cc-b794-3346-b460-0ed8010aa4b6 | -6.33945 | -41.91906 | 2025-02-13 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 821a4677-f65b-3361-af50-f3df3f9b950f | -5.00038 | -42.93558 | 2025-02-13 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45a43cf0-3fd8-36e2-a615-09f08e0436db | -7.38971 | -35.25287 | 2025-02-13 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 782917f9-ce90-379b-a132-dcf75e6d574a | -7.38256 | -35.25529 | 2025-02-13 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 42f383b3-f09b-3eee-ad70-1a50758ce113 | -8.95293 | -40.57766 | 2025-02-13 03:40:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2891eba-262a-3424-aad0-0e6979621e5b | -7.5033 | -37.46122 | 2025-02-13 03:40:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README2.md)
