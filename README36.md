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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de058ec5-937a-3c6e-a8c1-33bc3db3674a | -13.97137 | -48.16992 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 61068bea-0240-3421-81b4-b0a45575852c | -11.92548 | -46.27867 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10a2965e-5f1b-3eb8-a33f-8bd413c557b3 | -15.94939 | -46.21631 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f89497e8-3aac-379d-82cc-6c417282181c | -11.09314 | -47.86354 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 245cb2a8-6c22-3f11-9964-47998b4bb4dd | -12.6135 | -46.96416 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f4dbd65a-f666-38f6-9787-946b01ec8ce6 | -13.96932 | -48.1798 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4ad1d836-1765-3225-9a6e-0329d2807624 | -13.19721 | -47.80824 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8b19d0d-9990-3588-bfa6-29078053b136 | -13.82604 | -43.2373 | 2025-10-03 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02072783-1c7e-3552-ab9b-3d4bad0badad | -15.84719 | -46.23571 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcf86208-1122-3a46-8b13-7fe7f92bfb1a | -14.97292 | -46.85541 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55eb1f63-5d69-3fb3-a6bd-afe92eb791e9 | -11.48787 | -45.11475 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66503d89-1c8a-302e-9b86-8f61e656e64f | -13.95622 | -48.09488 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7316216-f084-316a-a798-04152525728f | -11.47655 | -44.97814 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e79d9ce-339b-3eec-9e05-99812eed54e5 | -12.63136 | -46.96249 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1d30d2a-be2d-39f2-97a4-6b5bbb6fc244 | -12.64782 | -46.99799 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb997303-345f-3bf2-9213-2837e148bd7b | -10.89288 | -46.72109 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a41e9a12-d5e4-3758-a9bc-c0ea72246f7a | -11.80932 | -45.02469 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29020e50-c35d-32d4-afcd-03c71ca31159 | -10.83802 | -41.27335 | 2025-10-03 03:45:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2a92122e-f3a8-362f-9906-2d70ba744347 | -10.68076 | -47.34601 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41b5ef7e-8566-3901-899d-a0b1d15d8823 | -15.52164 | -46.80699 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fa54d74-801b-3a05-83d0-5a3846a78c1f | -8.55737 | -47.64664 | 2025-10-03 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 461d9643-5a76-3280-8bbc-9b9c190e8b4c | -14.90872 | -48.32553 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5762e458-86c3-3175-b7cc-568a5d0f7a94 | -13.33278 | -47.223 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cfc5f79-903d-39c4-909a-8cb359c59ce0 | -9.94936 | -43.75497 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7716c41c-effe-388c-b521-98652c824556 | -8.64579 | -47.71308 | 2025-10-03 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 97db9ee7-eef2-3f32-a6c5-10c5e6280314 | -11.07344 | -48.3664 | 2025-10-03 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a9d2b2f-f849-33cf-9d89-ce7cc6a08bf1 | -14.90279 | -48.29554 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 291e2ae1-1970-343a-88e1-6d902c93867c | -14.29371 | -45.89239 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fbdba66-620f-3889-a5eb-9b54cc710161 | -14.46839 | -48.41498 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 288f6c10-9284-3f2b-957a-24dc5fa00612 | -14.93353 | -46.89939 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| aa8362dd-abeb-30c1-baec-b083d7a6b438 | -15.35205 | -47.06414 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4fea99e-d369-3215-9e73-71610c8d35d4 | -13.57765 | -43.35184 | 2025-10-03 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f272754f-75f7-3ba2-9510-0640ac066b13 | -13.50859 | -47.25219 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c29e5df-e93d-3a8b-80c8-9d93677cad51 | -13.7607 | -48.06233 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b5ba906d-de1a-3439-bd29-63baf065379a | -13.13295 | -47.88287 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 66954f7b-2015-3c2b-92f6-c4622bba9b5e | -13.15095 | -47.83404 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb1c182b-49ce-3bf5-9c25-ce382798108c | -12.90886 | -46.36571 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ee4a2b3-49c2-3bc4-b0cb-f5923a8bb365 | -13.26942 | -47.24576 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1cdedb76-31e6-3319-ae8d-8844c2cefb68 | -12.40034 | -45.01748 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd65ac6f-a6c1-3232-962e-dbd294d433f8 | -13.25812 | -47.26039 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ba450a4-f52a-3fd2-bd4c-0a3684b4ac4a | -10.85682 | -47.21675 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f6319ef-5e96-3b1e-88dc-86d6ba1ed1a0 | -14.88255 | -48.30445 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85789a1e-56d8-33f1-ae0f-9df28b80da4c | -11.61265 | -45.02753 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85170f2a-020b-3cb8-a4a3-767f18639d69 | -9.9198 | -43.72771 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| da93bf1e-5099-35df-8ec0-d56287de2906 | -14.35667 | -46.13692 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78a479d9-e6ea-31e1-90b5-a516e38f9409 | -9.95606 | -43.71801 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0129c91-29da-34c6-bf4b-146ebef9184d | -12.60616 | -46.97174 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a702efd-7946-3456-91b5-70aae8a78a02 | -13.34853 | -47.33142 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09750b29-de94-3eca-8f34-d98a22534eab | -13.2675 | -47.24253 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ce5ff21-48e5-3529-a4a2-e597134c0080 | -11.86001 | -44.97264 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b3fc32d-f03a-3cb0-89df-acebfeca93e9 | -14.20414 | -46.10753 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 940bc257-66c8-3006-880b-f3827789584a | -11.9044 | -46.27058 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed755672-ee0d-3005-a32b-f1d67a019bbb | -13.67018 | -47.30845 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dfb6436-3f6f-3093-89e4-280b4be35511 | -14.56989 | -48.33058 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1af77138-e246-398d-9ade-ebea1ba6ae03 | -14.91595 | -48.34944 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64448481-57e0-342d-a073-5f8147de9ec6 | -13.30982 | -47.81651 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81c78c04-7b88-32b2-ab40-0c49778504c1 | -12.29234 | -45.37057 | 2025-10-03 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf700c49-02c6-3337-9db0-2ed7c3423705 | -14.29838 | -45.88293 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1658e240-7548-309a-99e9-3e1c3c0290ff | -11.1432 | -43.40076 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 71ddfe21-8eb7-3e8e-b5f1-0dc1a101f68f | -11.59815 | -47.65665 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e340f364-8b51-372d-8ec7-076496b6e3e8 | -8.59093 | -44.78294 | 2025-10-03 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22ad104a-8457-3a25-8486-6304122ea907 | -11.90892 | -46.30614 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52e3e58d-152b-3219-a487-d6a82a5c66b6 | -14.87748 | -48.3283 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b13a5c7-ceef-32a7-aa33-0b2e3ccd6ca5 | -12.37442 | -46.5258 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c9b44a3-d4bc-3d18-b7c9-6a0363f098b2 | -13.57409 | -47.27654 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83c002d5-2068-31b9-9393-0e5ff1777c78 | -14.94607 | -47.52262 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5086b708-57b3-3d28-9ea6-0bb3b21f872f | -9.91601 | -43.7215 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 458f936c-3db6-337d-ae64-6e283b6e8fd8 | -13.12771 | -47.88928 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 40ac2789-cd4c-3525-9c5c-298be1d40b2c | -15.35336 | -46.26422 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebe74f77-7d17-3050-a5e3-c096c2eca142 | -11.87795 | -45.01486 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 303b0113-cf4e-3c98-b89f-8fcefa12c0b6 | -12.90725 | -46.89751 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2556b6c7-81d4-37ab-86d2-e46985c57927 | -15.22672 | -47.95841 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e39ef36e-56e0-31c5-9685-6f339cf4a68a | -14.20745 | -46.09058 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ad45095-ce56-3e11-9a61-1600b484eaac | -14.94315 | -46.87905 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfa16da4-fb8c-38af-9c32-e91e2b440a49 | -14.6677 | -48.26464 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f7588b48-8ffa-31d8-9561-ad0ffe5b2cb8 | -15.32576 | -46.29565 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fd718c1-f143-3e77-9bcb-e0e19627ece8 | -9.06864 | -46.65102 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 87839072-cc98-3c73-8f1c-604bf4c1b654 | -11.85114 | -44.96475 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bea06927-10d8-331f-b40d-94569930eab8 | -11.14168 | -47.20081 | 2025-10-03 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d90c300f-c789-3f66-b2a8-4ca751a21090 | -15.35271 | -47.06083 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd179a71-9bb7-36a2-807e-f78a5840bf47 | -11.85301 | -44.95732 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bba2a8de-4532-3ba9-a18a-3ba4e4fd4f62 | -11.67944 | -47.49492 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3a4b1393-9376-3479-81a0-4b7e77cd9281 | -14.42806 | -46.35008 | 2025-10-03 03:45:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 745196b9-9aa8-32d9-b35d-571c4d972f3e | -9.06455 | -46.64745 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 858163bd-c961-3900-9d62-3b71ea120a97 | -12.93425 | -48.44127 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a30a06e4-987b-3cec-a71a-66390c348816 | -12.37289 | -46.53368 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee149b69-95b6-3057-890a-ef68c9597faa | -11.45289 | -45.13251 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c4d20e8-00d3-3a30-a77d-7706fa155c37 | -13.30618 | -47.59662 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4945bfcc-be89-3b2d-8ae1-a851c7ea8213 | -12.5363 | -43.18718 | 2025-10-03 03:45:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 535fcd3e-8c26-31d1-a5bc-19dd4e217ad2 | -12.90517 | -46.89999 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c27afd67-b26f-3a8e-8082-c3f1f73ba233 | -15.22103 | -47.95715 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7080ca3a-dad9-3a08-a0f8-0fa270ef8df6 | -14.86063 | -48.36016 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 781481c3-b1bd-397c-a312-cc435d90203a | -14.8782 | -48.30447 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b9f817fb-abf2-34ac-9c1c-dddc9f6c14d5 | -11.84073 | -45.04594 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f2bad6f-e4f8-34d2-ad8b-a52f0f301a1e | -12.913 | -46.91877 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d269c416-b12e-341b-9d6d-8b45b925e4ac | -11.627 | -45.03482 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b69f48bb-e8bd-3de5-b752-bdba1b03920e | -14.36123 | -46.14103 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eba2d69c-b853-3f4f-ad29-d41904768f66 | -11.14308 | -43.37505 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48842d2f-4780-36af-b14f-55794df77b7c | -8.07971 | -48.22097 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55a82a63-7746-397e-b239-86882d319894 | -13.66658 | -47.31188 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
