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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e127373-ef90-36c6-a0d4-145331b09509 | -13.88647 | -45.55904 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3aa00e3d-cf80-3b8a-ba1e-efaa7b01dcd1 | -13.41711 | -45.88908 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 707587ac-7d43-3120-a9d8-311bd8f17a71 | -14.17204 | -45.3603 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ade02a77-0d90-3ad1-b148-e1e918f79aae | -6.86225 | -42.80222 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 551.2 |
| 556d8381-9257-37ee-af01-1f6b4796f129 | -13.32416 | -45.23239 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 5b8ccce1-3b15-3ac9-bca8-222bbc1e38d0 | -6.95756 | -42.98601 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| bed52cb7-6015-3c23-b16c-4d20bfd2d138 | -5.60401 | -43.2387 | 2025-08-15 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c04bf817-8f06-3fc9-a226-d81561811a7e | -15.20943 | -43.79258 | 2025-08-15 12:14:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 55b7d90b-d450-34da-9e26-639beb3ff7ab | -5.70905 | -43.67273 | 2025-08-15 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d562d7cf-dcb0-31d2-99ab-82951f36554b | -7.29314 | -41.58091 | 2025-08-15 12:14:00 | TERRA_M-T | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 871886dc-b0b8-39be-b2d1-ae764f72d602 | -12.05055 | -43.35978 | 2025-08-15 12:14:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d72a0ea5-a524-300a-bfe1-6e7746d9bb9c | -15.14457 | -45.65351 | 2025-08-15 12:14:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 45.0 |
| f9ae7eb3-fa86-33d2-b5ba-cdd349878f91 | -8.32347 | -44.93927 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 31da9e8e-a515-3da5-89ce-925488ce2455 | -13.87751 | -45.55779 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bc439272-50f5-3964-a098-a8def6bff246 | -13.51613 | -42.38699 | 2025-08-15 12:14:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c3a6a806-ccaa-33bc-a636-98056992c966 | -7.91813 | -46.84028 | 2025-08-15 12:14:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2283a9a9-cba2-34a1-aeb4-4e42a05dcdd4 | -11.40571 | -47.59895 | 2025-08-15 12:14:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ab5bb3e1-fd6b-3472-bda2-ea185e187b6d | -11.17799 | -45.74338 | 2025-08-15 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 7c627906-fd33-3ba4-af35-f691422cd570 | -14.51915 | -46.63068 | 2025-08-15 12:14:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 70d8bc6e-1e3f-3156-a59c-9d7dee484c2c | -12.48953 | -47.00602 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4b931d72-7a00-3e3c-9762-9d12854eb2d7 | -12.4882 | -47.01512 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 8a256de9-0527-390f-8ab4-2659e8e7c5df | -13.87881 | -45.54845 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 5e07f9a5-5d0c-39ac-9548-20f0aff308b2 | -6.32974 | -42.79565 | 2025-08-15 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 73b7d4b2-0add-333f-83af-686d738da514 | -11.9287 | -43.4374 | 2025-08-15 12:14:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| aa42f9f6-b904-322d-b794-40a63e2c5d34 | -12.58964 | -46.95255 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a022e8b6-e19b-30bc-8919-f50e7b84e905 | -12.5821 | -46.94214 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 3ea831b6-ff06-3b1e-bb77-0258ec5a9bf5 | -6.34934 | -43.38066 | 2025-08-15 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 02608d58-fa24-35ad-94dc-c5893218b24f | -12.83281 | -44.45264 | 2025-08-15 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9c075579-9aa6-3f3f-9cbe-e45263bef33a | -9.18968 | -45.33244 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| ba8d02ce-9737-3e67-8d1d-739281645d71 | -6.42379 | -44.61476 | 2025-08-15 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 20e9fde1-bc02-3ff1-89e4-b5a3f6d5c6ad | -9.88276 | -47.40819 | 2025-08-15 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e5286d76-efe0-3559-a35e-a426d35271d6 | -8.32474 | -44.93036 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b6ef7389-0ad1-3342-8e81-5a1d80207d4b | -10.79375 | -46.10029 | 2025-08-15 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5effd79a-d058-3dee-aaf0-12c5cde8b52f | -7.40135 | -44.87434 | 2025-08-15 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1f4031ec-7266-3895-9e45-9d9602b69de3 | -6.48287 | -42.95085 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d3a08452-af67-315d-8248-e777805bf932 | -13.32545 | -45.22298 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2682ffa5-6208-392f-83f0-3e6aef234fab | -10.65429 | -48.93931 | 2025-08-15 12:14:00 | TERRA_M-T | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0fd9c769-e1e3-382d-83a6-0a7198c7a215 | -9.5957 | -42.93058 | 2025-08-15 12:14:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 05e7e2ba-974a-3732-be74-5da9d3de7513 | -6.91046 | -45.2062 | 2025-08-15 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8b7a9299-5fc6-3e5e-9714-daa5b4137d80 | -11.19459 | -40.40202 | 2025-08-15 12:14:00 | TERRA_M-T | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 854ed59e-e300-3845-9826-6b719694b381 | -9.85325 | -44.68258 | 2025-08-15 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e4fe1ae1-344f-340e-a024-9614d74203e9 | -6.22599 | -43.33808 | 2025-08-15 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d6fa62aa-a5d8-36ec-8a5b-9edcd54d9e31 | -13.31435 | -45.23452 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 308.8 |
| 100c310c-0c14-3f21-b86c-460beaa4ed30 | -13.42597 | -45.89036 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 62e2bbe2-63e8-3701-819f-997d62e8ffd3 | -7.156 | -43.41074 | 2025-08-15 12:14:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| dd275c58-7813-39a3-a8aa-5e7efbccda14 | -13.31567 | -45.22513 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 31a53efa-8c4d-3a93-8f72-9545fac1a779 | -10.86539 | -48.48969 | 2025-08-15 12:14:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5c713069-2355-3029-86ba-ec9852ad84e4 | -12.68962 | -44.9588 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 8f466490-c66f-3311-a380-aba6eec04af4 | -6.19536 | -44.52839 | 2025-08-15 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 253ff1e8-825f-33c5-827f-706757be053a | -5.90991 | -43.49004 | 2025-08-15 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f174159d-a2a7-3251-b686-18ce294c9661 | -8.72836 | -44.0292 | 2025-08-15 12:14:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| db27fcd5-e426-34ef-b2a1-9d3194f5fe2b | -13.88777 | -45.54972 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 1fbe9956-9f9e-3d0a-9ebd-8a90e390ad57 | -10.68088 | -42.67605 | 2025-08-15 12:14:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| cf1984ae-0282-3291-8c29-1e3343847782 | -12.59096 | -46.94347 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d210971b-0430-3925-a9d9-25e457a19e25 | -10.53442 | -42.54951 | 2025-08-15 12:14:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 56abae9b-b282-33fb-a2dc-1b5670cf71ca | -15.61274 | -41.83307 | 2025-08-15 12:14:00 | TERRA_M-T | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 2ea5cc06-a87b-3175-8f89-07c199a39f3c | -12.58342 | -46.93316 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 67886298-8ccb-37d2-878f-4c7bc94d3beb | -14.06659 | -46.30506 | 2025-08-15 12:14:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 684fa67c-fbe4-3107-b122-2bb65bffdbf6 | -6.42505 | -44.60591 | 2025-08-15 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 3abc1f29-90ea-397d-bd76-298d3e476688 | -7.40388 | -44.8566 | 2025-08-15 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8bf0eb3d-5de2-3566-b6f9-2c4cba72ee24 | -12.69093 | -44.94936 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aa33509e-9b52-3db5-917b-9900c8ebe3f0 | -13.33187 | -45.24305 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d123fb3f-b74e-31dc-b5ec-d76e3df81fa8 | -5.2689 | -43.59012 | 2025-08-15 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4e2cb032-2f4b-36d2-953a-cbd5154647a8 | -6.48149 | -42.9608 | 2025-08-15 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 389596db-c337-32e9-8928-8654a5217b63 | -13.32674 | -45.21357 | 2025-08-15 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4672e729-fd3e-3278-9efe-4044598a4555 | -9.21616 | -45.33618 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d4597ff6-7b64-3d95-b7ac-b95e007a8deb | -9.84106 | -47.81038 | 2025-08-15 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b745bf60-871f-3c7b-b5bc-46cd685445fc | -6.10961 | -44.60899 | 2025-08-15 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0ba26251-b94d-3805-84ea-726a9c816bfe | -9.60538 | -42.93188 | 2025-08-15 12:14:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 35.9 |
| b3a822c6-3525-380b-a9cd-e985ecff82af | -7.07576 | -44.94811 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0cd68eb7-ba67-3430-978d-d9869222a782 | -9.60395 | -42.94257 | 2025-08-15 12:14:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d2b8fdef-e829-3668-9a04-6a9c5de5049a | -6.33773 | -42.80686 | 2025-08-15 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e9bfd1d7-69e9-376d-a169-9e8d22c23b85 | -12.31655 | -44.58928 | 2025-08-15 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 43d40552-1e14-3fde-9d0c-f2324e281fdf | -6.54508 | -43.49747 | 2025-08-15 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 48258824-58e3-3862-8cc5-dcaf78945591 | -12.64917 | -45.18274 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 63a339bf-e614-3612-9e92-0df1d79c5855 | -7.39126 | -44.88198 | 2025-08-15 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4d398fa7-7a13-32ed-b00a-628656227557 | -5.71034 | -43.66356 | 2025-08-15 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 80f2754f-edc4-3b52-bc6a-ba6831a96d2a | -7.04174 | -43.83095 | 2025-08-15 12:14:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b13ef0b1-4641-3f83-8579-01c8c67e9795 | -7.02082 | -44.308 | 2025-08-15 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6f67058e-1278-3ac5-b1ac-28bfcd3f5cb4 | -6.97436 | -42.86537 | 2025-08-15 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 51a019f6-90d5-3093-9fa8-914800043198 | -7.23738 | -44.79383 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 8a4455d5-2ae1-3cef-b57c-e9859386ed8b | -7.59408 | -45.19337 | 2025-08-15 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9e8e24f5-6f76-3a7a-aa6f-e8a06c930a91 | -7.74025 | -43.97721 | 2025-08-15 12:14:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ffcf987c-be8f-3e42-819f-6f327717798d | -9.54709 | -47.24582 | 2025-08-15 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 67ee9c75-d50b-30c1-ac5c-53b3ebd094e8 | -9.85815 | -47.82317 | 2025-08-15 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1620f1d9-f640-3577-9b18-02899c185dfa | -9.18213 | -45.3223 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 87a040c0-89c2-3f1b-9bb3-a72bb9a4b2cf | -11.17927 | -45.73444 | 2025-08-15 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4344b3bc-c577-32a9-8425-6d3b0de582c1 | -13.03201 | -45.07995 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae394fa2-fa4c-3d43-9ec5-38e74149416d | -8.31331 | -45.01054 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 32fe6af2-5d3b-3683-aad4-3dda52110559 | -14.16302 | -45.35903 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| de607a7f-5448-3f31-a0ab-34213fa0b85e | -6.95864 | -43.83193 | 2025-08-15 12:14:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 56badbc7-d2b4-3248-9ef3-c0c80bbe8c27 | -7.00553 | -45.63788 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3a96e05d-4b68-3b54-b484-32d16a98892b | -12.48687 | -47.02422 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 651e4eac-3367-3316-bdd2-61d10d431d6a | -14.17335 | -45.35082 | 2025-08-15 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f4988b47-ad4f-3b8d-a885-0d451d7f70ea | -7.1001 | -46.3153 | 2025-08-15 12:14:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4ffaf229-0e71-3353-a796-f4a1fe2527eb | -12.59717 | -46.96302 | 2025-08-15 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fedae918-ce46-348c-877b-6e11763fb3ed | -5.6901 | -43.67315 | 2025-08-15 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1c8ec5d3-8f89-3fc5-83ba-fe9ade248b10 | -8.31204 | -45.01944 | 2025-08-15 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4b95cd8-1fa2-365f-9a9d-48fc175b432c | -6.94742 | -44.55643 | 2025-08-15 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a7144148-1cc5-3b84-b3b5-dd242f38a929 | -7.01077 | -43.85497 | 2025-08-15 12:14:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README74.md)
