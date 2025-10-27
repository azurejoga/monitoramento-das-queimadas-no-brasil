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
| 8561a086-5040-3184-8565-d6b2f65f8afb | -13.42404 | -47.38469 | 2025-10-27 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 357e9a16-75a0-345f-bb47-e1f785cb950d | -17.40849 | -46.88872 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a705a64-821f-3a9f-b7de-3d0c9e1c3511 | -16.37732 | -47.41714 | 2025-10-27 05:04:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55d0925c-c222-3f24-a491-1df835dfe14a | -14.4032 | -51.54285 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a71940c8-6f0a-3d6b-b088-2b11464f99a5 | -17.23923 | -46.79871 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30b0b627-408d-394e-bb42-c955f07c0116 | -14.43935 | -46.48957 | 2025-10-27 05:04:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8953e391-016c-3c6d-9f84-14dbd02b38c4 | -15.17444 | -47.22209 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bef2c17c-33fb-3db8-a1a4-32044d2a4415 | -12.88846 | -54.72737 | 2025-10-27 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bafa3128-ad54-3b59-9660-247fda76572e | -14.25941 | -48.13064 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 318d528b-eac6-36f8-976b-9fd8ec8dcfec | -15.19477 | -47.23073 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0167132-045a-3228-b252-4f655c80eb3c | -14.25515 | -48.12502 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ac0cd9a-3f2e-37ff-9403-9026e48bafe1 | -18.26531 | -45.37045 | 2025-10-27 05:04:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25cb7795-8138-3ef5-aab5-a8e9c056936a | -15.19595 | -47.22074 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 512d8133-3aa8-3a36-aa23-9188b048eeb5 | -14.39469 | -51.54673 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50ead640-1c8b-3a34-8dc7-ca88c9fc81bd | -20.66186 | -42.73942 | 2025-10-27 05:04:00 | NPP-375D | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3be0558a-04f7-3e86-a9fe-196a5048e344 | -19.63751 | -45.39308 | 2025-10-27 05:04:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fd7d8cf-ed63-3a72-ac5c-3bf89c76ffbf | -14.8261 | -52.42333 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 27764f2a-858c-3857-a449-9dde96be28ee | -15.1512 | -47.93447 | 2025-10-27 05:04:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e78e064f-1fae-340b-b95e-fcb036f1ed8d | -12.90133 | -54.73312 | 2025-10-27 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50112af8-530f-33c9-a3cd-7cac91702e5b | -14.38043 | -51.53436 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9dd4660-cfce-3125-82b5-3898302b89d3 | -13.23461 | -47.99854 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e46363f1-d844-3ed9-9c6c-4f9b3f3feffc | -16.37712 | -47.41327 | 2025-10-27 05:04:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f183310-17b9-339a-9195-9a58eede0cdd | -13.23274 | -47.99371 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 07dc0768-c49c-3919-b35e-0cb3236d19a5 | -17.32355 | -43.64683 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc9e8964-626c-34a2-959f-a4d0f0b89be7 | -14.3687 | -51.53263 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c4ac5f8-4778-360c-b23d-8df385818676 | -13.31363 | -54.36764 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bde8dc9f-ba5f-3025-abe5-fb8f7aa2e04d | -13.85431 | -48.09648 | 2025-10-27 05:04:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd80a23e-0f93-385b-83b4-dec49db7ee64 | -13.4291 | -47.3856 | 2025-10-27 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72a3413a-036a-39be-b092-b736f9f8a288 | -13.31024 | -54.36712 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31b40043-66aa-32aa-92d7-e2a785f4ccc4 | -13.25063 | -47.9692 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90c1ace1-2c52-3edb-a932-34ebb74cb764 | -13.31011 | -54.36379 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e7d7b5c-d225-3949-a5c2-a939c65f64ea | -13.2478 | -47.97349 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50d08e49-c092-3482-aa89-df612a5ea69c | -14.62281 | -48.396 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e9bad4b-7a12-3152-802a-f956d49b956a | -17.32295 | -43.65347 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d5fc7d0-44ca-3910-a146-ef1179376ef3 | -17.77184 | -46.8675 | 2025-10-27 05:04:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68bc92ce-b71e-3b90-a6b7-7b138592b4fc | -13.19144 | -48.44167 | 2025-10-27 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b19e69aa-812a-35f2-b109-2b0939c16872 | -14.25881 | -48.13541 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4da1efc-37be-3014-91b9-98cf14cfeeba | -13.2376 | -47.99444 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 22d49184-f258-3089-b321-e199c9fb82ad | -12.41222 | -54.19458 | 2025-10-27 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07e5f186-0daa-30f5-9732-86c509ada44f | -14.82983 | -52.42391 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a79c1703-d373-3777-96ae-35391f16a05b | -13.25547 | -47.9701 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4426a05-cd2c-3b68-8356-84bca82654a1 | -17.41387 | -46.88 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60990504-a7f4-3e78-a8cf-473c942c150b | -13.31986 | -54.37238 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f4d6862-f14e-39f5-9af0-baba83fe7349 | -21.58477 | -43.50094 | 2025-10-27 05:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2b2cf233-3664-3f18-896a-def09c965245 | -21.58523 | -43.49432 | 2025-10-27 05:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5e554bd2-8d4d-3ebd-81c5-f852168330e7 | -21.57979 | -43.50965 | 2025-10-27 05:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e2c7ab5e-a48e-3f1e-95e5-7c19685bb354 | -22.12153 | -42.98397 | 2025-10-27 05:06:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7980748c-5925-32da-83fb-5289ce63dedc | -22.12108 | -42.99059 | 2025-10-27 05:06:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1df04e2d-ba74-3c74-982c-ad9b610d18b5 | -20.64971 | -47.23392 | 2025-10-27 05:06:00 | NPP-375D | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0815ea1d-50e7-35e6-b203-9b34b99055f5 | -20.97517 | -44.32888 | 2025-10-27 05:06:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fe2df120-2a09-3e73-bedf-0206490eb603 | -20.97704 | -44.33064 | 2025-10-27 05:06:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9c768056-3cea-3d00-89f9-54b7936ad5cc | -21.59236 | -43.49444 | 2025-10-27 05:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c306463f-d02d-3b40-8fa9-9af1b2cb82f0 | -20.65006 | -47.23021 | 2025-10-27 05:06:00 | NPP-375D | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32808bda-cfdd-3931-b2a1-45f077f14af2 | -21.58036 | -43.50215 | 2025-10-27 05:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4df256a9-eaf4-35c7-b3c5-b02bd95c2b5a | -21.58429 | -43.50786 | 2025-10-27 05:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e144d9fd-8885-39f0-bf77-fe09cb341c0e | -20.64659 | -47.23155 | 2025-10-27 05:06:00 | NPP-375D | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 730b217f-e499-300c-8b12-77b0f5deabc9 | -21.58794 | -43.4962 | 2025-10-27 05:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5a44bbb8-5056-347e-bb9f-94b4912b4b51 | -10.8401 | -56.959 | 2025-10-27 05:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9bb3c905-cba4-36b4-a1a1-5c0531aead6d | -9.5685 | -46.8918 | 2025-10-27 05:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c1f492ba-7938-3355-995c-939d58441aca | -7.8408 | -46.487 | 2025-10-27 05:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| ea44a75a-428a-33e6-a188-05ad2cc4a46d | -7.8411 | -46.4646 | 2025-10-27 05:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 278.1 |
| 4aa9ae27-c257-38fe-8fc4-188585dbd639 | -4.4807 | -43.4005 | 2025-10-27 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ff10c768-f144-3baa-970a-63bc8fa587a6 | -4.4805 | -43.4237 | 2025-10-27 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 21556750-97eb-3cba-8012-0a09ec9b2b93 | -7.822 | -46.4887 | 2025-10-27 05:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| f77e979c-80d2-3680-8f2a-3c0287ad9c01 | -7.8223 | -46.4664 | 2025-10-27 05:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 54b4000b-da2a-364d-91ee-0c6dca180a42 | -7.8225 | -46.444 | 2025-10-27 05:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 943cd18a-1ee9-3c60-9fdb-81cb44a3944b | -7.8413 | -46.4423 | 2025-10-27 05:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5795ddc3-011b-3e52-b396-7a990c338f6f | -9.5875 | -46.8897 | 2025-10-27 05:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 20f9a67b-205e-3754-bbfb-066bbdc58fff | -7.8408 | -46.487 | 2025-10-27 05:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 8c27010f-07a0-3598-b707-c3223d124b90 | -4.4805 | -43.4237 | 2025-10-27 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 705eca4d-63b2-3802-b88f-871cf68ed7eb | -7.822 | -46.4887 | 2025-10-27 05:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f04ad59d-36bd-3e6e-b0c7-8ec09dca2ab3 | -7.8225 | -46.444 | 2025-10-27 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 50fcf6b1-57c4-32d8-a4e4-66c7b0fabb82 | -7.8413 | -46.4423 | 2025-10-27 05:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5e102611-8467-3762-9060-6df5bb801f77 | -7.8223 | -46.4664 | 2025-10-27 05:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 974634ea-efcb-3987-bda7-187cc4028afd | -7.8411 | -46.4646 | 2025-10-27 05:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0973e78e-5244-31e2-8737-47144be00ecb | -4.3879 | -43.3129 | 2025-10-27 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 66a32c5b-fe7b-3c5a-9713-58b793afbb2c | 1.60878 | -55.73631 | 2025-10-27 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5928e739-9724-352b-919f-18e15cc94bba | -1.19123 | -53.39061 | 2025-10-27 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da411c7d-5e27-3278-a638-d6691f29b3cc | -1.34918 | -53.48534 | 2025-10-27 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1d4042c-dc19-3284-8fe8-1408fc0f80c0 | 1.1496 | -51.05527 | 2025-10-27 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e781c1fb-0ca8-3948-89d5-35bdb4a47dfc | 0.43493 | -50.83011 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 39cb359d-6d36-3f07-ad4b-064326366692 | -2.23168 | -51.99603 | 2025-10-27 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cedecee7-1ace-3122-91fd-dda6a5d72565 | 0.43764 | -50.78973 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312a1cec-5439-3b46-885d-696527519a45 | -1.40054 | -53.09731 | 2025-10-27 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec423b6d-4213-3eeb-8ba0-3f4daae09427 | 0.43266 | -50.7905 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f8469fb-efbc-3bb5-8cdf-0c5bd2b1b1fa | 0.81016 | -50.83649 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c14d2ea1-0f59-3206-ab95-680c4188bf8a | 0.43322 | -50.82666 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7b2deccc-4556-3d96-be3a-805bf6421cfb | -1.39553 | -53.10082 | 2025-10-27 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84aa9a16-7efd-36c1-87ec-7031dd7229fc | -2.18817 | -52.49422 | 2025-10-27 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09c0f0ff-be41-3534-87e4-e00dab21eade | 1.61106 | -55.72771 | 2025-10-27 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 859a8c67-9900-3928-a78e-804c47412b31 | 1.15046 | -51.06053 | 2025-10-27 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12e652a6-79e2-38d6-801a-b6997b0761e7 | 3.89993 | -59.60475 | 2025-10-27 05:21:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cfab0c0-0dc0-310e-8783-07f6f26f81f4 | 3.63955 | -51.82756 | 2025-10-27 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87085fb3-b6fc-37de-9651-1d21eb6f9467 | -1.37993 | -55.3485 | 2025-10-27 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a29b760c-6574-3579-a2b8-693a1ca04fde | 0.43434 | -50.79549 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92e2151c-19de-3d3b-a7a5-af7f5e54123f | 0.43234 | -50.82102 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 39db210b-fc51-3aa2-812e-b0f84645a92e | -1.34857 | -53.48928 | 2025-10-27 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 023076ea-9070-3928-946c-d97ada511089 | 0.43308 | -50.81887 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f1290343-3c3d-3734-9338-0ec51b2f2349 | 0.4331 | -50.79333 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b895f384-8c86-3015-b066-8bb83f71bffb | 0.43897 | -50.82373 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README67.md)
