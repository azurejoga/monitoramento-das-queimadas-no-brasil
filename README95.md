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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcbfb1fe-4a1a-3506-b1fe-18295378452d | -7.34332 | -42.07355 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a0dec797-13bd-3e3f-ba2b-12d5c47e1c04 | -7.0795 | -41.74998 | 2026-09-29 15:48:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b88c3f3c-4755-340c-b552-f75eb40889c3 | -3.40142 | -44.11979 | 2026-09-29 15:48:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93bb27b4-0453-30e2-a2b5-5dd251cadc57 | -8.02366 | -42.86591 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 5a2c9c0f-35fc-34a0-be20-c810d7884aa6 | -6.02743 | -42.58409 | 2026-09-29 15:48:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b4fdc796-210d-3948-be78-63b85d3392fa | -3.53593 | -39.95693 | 2026-09-29 15:48:00 | NPP-375 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b8a168de-64fb-3d46-adf7-895fec9416f9 | -7.05729 | -42.0786 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c44bd747-e9a2-3f04-8eec-d15f0df10895 | -7.39294 | -42.64207 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b82119ae-4c84-3036-ac82-58cf7b5924d8 | -4.30034 | -41.76635 | 2026-09-29 15:48:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 24891ba0-ec57-3ef2-a0a5-2ad3984dc7b6 | -6.87992 | -43.69921 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e2909038-9314-3c11-9570-c063bac0d727 | -6.87632 | -43.77432 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bc6056fc-443e-37c6-aa30-ebffb0ab2bf2 | -4.95158 | -37.44319 | 2026-09-29 15:48:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 56433262-2e5b-3ef6-b021-ad38c89f257c | -7.16406 | -35.7221 | 2026-09-29 15:48:00 | NPP-375 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c19be2b6-4d91-39e6-8277-587d2758d38e | -6.95498 | -42.86307 | 2026-09-29 15:48:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 72eb6ad0-16bd-3690-b95e-af4fd9bc91ad | -3.28332 | -42.66881 | 2026-09-29 15:48:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 505e8251-8319-35ab-8181-4dd2b5a58913 | -7.01464 | -45.30427 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 366e8286-d821-3321-b0ab-67c55250cbf7 | -3.28099 | -42.88867 | 2026-09-29 15:48:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 629a2bf7-72e0-3c71-8e4a-4bd92c0b4ed1 | -8.03708 | -42.86967 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 69140021-1a6a-33f4-8a49-d5b8f226967d | -5.51922 | -44.12503 | 2026-09-29 15:48:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 505cf6c2-b83d-35b5-9050-751d0ce15cc3 | -8.55027 | -44.04743 | 2026-09-29 15:48:00 | NPP-375 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| aefa928b-cc93-386f-ae79-a7253e3cc4a1 | -5.73817 | -45.19975 | 2026-09-29 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3780347e-2762-3e36-a0dc-5b91625cc371 | -5.95417 | -35.52153 | 2026-09-29 15:48:00 | NPP-375 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| df088a21-1349-3266-ac27-bd654a2cb48c | -7.42039 | -42.62807 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 69cc405e-5a5d-3032-a253-49f025a63576 | -6.76471 | -39.11338 | 2026-09-29 15:48:00 | NPP-375 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5747fedb-f29e-3346-8ca8-2275c8b22099 | -6.02806 | -42.58862 | 2026-09-29 15:48:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 87b638f1-5741-3723-a05b-08b0c8397fbf | -4.97426 | -37.39247 | 2026-09-29 15:48:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b8b50640-182e-3575-9cec-55a87a54688b | -6.94038 | -41.59756 | 2026-09-29 15:48:00 | NPP-375 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f5ac1b16-1d4c-39e1-ac90-002d5df091b5 | -5.98865 | -40.9104 | 2026-09-29 15:48:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| a83d201e-1be9-3e10-b7ac-b22e10bbdd8a | -6.87337 | -43.70045 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 62b3ddbc-803b-3a05-bc04-11c26cff1d4b | -7.05617 | -42.07005 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a390b37e-c8fe-36ca-a1fd-c176cf21a724 | -8.74014 | -44.90173 | 2026-09-29 15:48:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cccbd932-7d3d-3077-a1ca-d26576a6964f | -7.0621 | -42.31303 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f3ae41b2-4753-3eaa-92de-4ce94c983e3d | -7.28472 | -45.33022 | 2026-09-29 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b4db543e-5529-3d0f-94f9-c3d96b97c7da | -8.02304 | -42.86106 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| d89da6cc-d331-31e9-b426-0cc8c4798658 | -7.55315 | -40.4678 | 2026-09-29 15:48:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6e93634a-7590-3082-a567-0be25a96fbcb | -7.06327 | -42.07783 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ca90b4ea-398c-3b7d-9554-d5bd4213cedc | -5.70417 | -45.24731 | 2026-09-29 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b0f893a7-106f-3299-bf7d-392744695739 | -7.41978 | -42.62334 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 2073cfb3-7e2b-329d-bb70-956fc2020283 | -7.07363 | -41.75064 | 2026-09-29 15:48:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f7b0a8eb-55df-3be4-b362-56825672eaa2 | -5.25615 | -44.93473 | 2026-09-29 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df8e7e79-bd18-3da5-a348-559b3d737671 | -7.14535 | -36.11222 | 2026-09-29 15:48:00 | NPP-375 | POCINHOS | PARAÍBA | Brasil | 2512002 | 25 | 33 | nan | nan | nan | Caatinga | 17.2 |
| b8aa35bf-3189-3afd-87a9-0e33a2dce8aa | -7.02192 | -45.30349 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a1150f92-0d16-3ccb-bd59-fe17e56433f0 | -8.55026 | -44.05175 | 2026-09-29 15:48:00 | NPP-375 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 67c713a3-a9ee-38c7-a1e5-1776a975aaeb | -2.9194 | -42.86744 | 2026-09-29 15:48:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4be6c683-5d19-30d6-9ca6-47120c913f54 | -7.34277 | -42.06926 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 64f9467b-0bef-345e-8263-b3ac5d21a52e | -7.5512 | -39.62802 | 2026-09-29 15:48:00 | NPP-375 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cf91ab1d-ec72-37d0-9da3-96ae58c1c3cc | -7.04445 | -42.84072 | 2026-09-29 15:48:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7acc11e9-b63e-3bf7-a99f-a0ea2fbd3bf9 | -6.06472 | -35.35865 | 2026-09-29 15:48:00 | NPP-375 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 5f3a6355-f728-3633-a4e3-6ffbb3fa284e | -7.38544 | -42.63322 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 05f85406-7cbc-310c-866f-42bf70f8cb4f | -8.45416 | -44.66309 | 2026-09-29 15:48:00 | NPP-375 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8eddf9f2-6e0a-309d-99dd-b788e0f69755 | -4.0349 | -42.06106 | 2026-09-29 15:48:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7c70b9ac-ed37-3944-9397-831df49c098d | -4.72304 | -44.34248 | 2026-09-29 15:48:00 | NPP-375 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bbdb8269-6ddf-34e3-b97a-5284a3b85039 | -7.4159 | -42.62444 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bdbb71f3-57bd-317a-86c6-4f96bb679445 | -6.94181 | -42.85992 | 2026-09-29 15:48:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6b5c693a-67f3-3516-91e6-f7621c919a52 | -8.02179 | -42.85126 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| a59ad59b-fc81-3bcd-a883-dd2b8144b140 | -7.06385 | -42.08218 | 2026-09-29 15:48:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4e0bcb14-22d1-3e34-afb7-692630c7b47e | -3.6409 | -42.8339 | 2026-09-29 15:48:00 | NPP-375 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7618cde0-ca43-3f95-94a5-9ecaea56989c | -6.02007 | -42.57568 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 8388cd40-092e-31b6-b31b-05fbdc8c71eb | -8.01668 | -42.8619 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| bcc5c139-7e9c-3a8e-b7d2-4319df413008 | -7.03026 | -44.63262 | 2026-09-29 15:48:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| eea600a0-6881-3e60-98e1-4ba3e26109ff | -7.39168 | -42.63255 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 198b160f-c6e6-3df9-af14-f64b74b02dae | -7.33042 | -42.08097 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f21661cf-500b-3ab8-b0e5-6bbd6093f989 | -7.39228 | -42.12111 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c137252e-9014-36de-8c35-af3ac6bf6346 | -7.42278 | -42.62852 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5371a06f-1313-3f25-8f5f-b0f4a3dfcb1b | -3.12325 | -40.51002 | 2026-09-29 15:48:00 | NPP-375 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 33a51a91-af37-3e96-83bc-e1bc37abb92d | -7.02717 | -44.62477 | 2026-09-29 15:48:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 272b00a3-a509-3ef5-8fd7-9143d55eb483 | -7.4591 | -40.2179 | 2026-09-29 15:48:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| aa49eaf1-e363-34d9-9d89-fbdb35d5e448 | -4.50171 | -42.55601 | 2026-09-29 15:48:00 | NPP-375 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 2cd59328-d818-3d47-a3da-bcd6fff391b0 | -4.77708 | -43.27606 | 2026-09-29 15:48:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27df9c47-f46e-3eeb-ab3e-2157a7d8ff43 | -7.24418 | -43.36404 | 2026-09-29 15:48:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 760d8b1b-09f2-311e-9757-509d393df6b1 | 1.9425 | -50.8199 | 2026-09-29 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9849afb0-7bbe-33cc-87a9-bcf56bc473bb | -12.0369 | -50.6019 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e84460ec-dba7-3d14-bf8d-dc3624b43576 | -12.0997 | -50.2297 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4921b9f5-da65-39cf-b597-cff805872a6d | -15.3998 | -47.9261 | 2026-09-29 15:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a4f94436-2208-3478-ac3b-15668ac6a829 | -9.9582 | -50.2499 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 96128c09-1a08-38d9-8624-45bf78284668 | -9.9959 | -50.2462 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| edb1d603-a5b9-332b-925b-a45ec2cb5ecd | -11.7129 | -50.6394 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4dfcb3fb-40b6-3631-83b8-afe607b16927 | -10.8777 | -50.6886 | 2026-09-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| cc16d2d5-7aac-30f9-b80b-dd16ebd8aa44 | -10.9722 | -50.6998 | 2026-09-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 33bc8bbf-32f1-3f1a-a82c-c7709e74af10 | -20.9159 | -57.8246 | 2026-09-29 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 133.4 |
| af606550-2934-33d2-a1b4-78b2708c0cd3 | -12.0806 | -50.232 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9b5edf91-ec96-38a9-a277-4935f68a10ed | -10.9912 | -50.6978 | 2026-09-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 59eabec4-4dc2-3d0a-ad63-941ade112f05 | -11.7828 | -51.0578 | 2026-09-29 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 6c337e90-0318-37dc-afb4-a7dc348277ea | -10.6683 | -50.7955 | 2026-09-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8aa0bd06-00d3-350c-883b-7cc31f683605 | -12.0317 | -50.9442 | 2026-09-29 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| a544fdb1-95b6-3ce9-bd0e-520500e9f979 | -12.1185 | -50.2489 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| fe0f2e9a-e3ab-3d59-9fcc-6e6b1ab59db9 | -10.7056 | -50.8341 | 2026-09-29 15:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 404ada64-bc9a-3d63-88c0-535b198cac7d | 1.9241 | -50.8202 | 2026-09-29 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9eac37ba-06ca-33fc-9af4-dc08ddd8ca8a | -10.651 | -50.6697 | 2026-09-29 15:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 2fb32634-8403-3372-8d08-b5b6fdb3c96f | -10.1095 | -50.2135 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 99b442b6-f3fb-3dd5-8dee-e25e51aa26da | -9.9956 | -50.2675 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0f51a1c4-2842-306b-9350-f07f72acfd0b | -11.7887 | -50.6521 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 47d93898-bd23-34bd-bd83-fc8b772d7f8c | -9.977 | -50.248 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| f8603903-0ff7-3056-b8ec-1d8ea41e4cb4 | -12.2894 | -50.2927 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9b6aeafe-f9e8-306a-9417-e587cf838210 | -12.0314 | -50.9656 | 2026-09-29 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| a4ad1d8d-4091-3546-b545-e80b4cd7d1d7 | -9.9598 | -50.1217 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 21497225-6fef-3082-8619-365444af88cd | -12.0559 | -50.5996 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| eafee030-9fbb-3f54-b9dc-667bec2840e3 | -12.1737 | -50.3712 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| af2ded66-398e-3a14-9804-eb49d5ef46af | 1.8587 | -55.5648 | 2026-09-29 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 2803516f-bb3f-3ac2-9608-3dfd187b1b1d | -12.0612 | -50.2558 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |


[Clique aqui para ver as próximas entradas](README96.md)
