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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebc83a62-2267-3c69-9b56-884e9ecc2e23 | -11.28836 | -43.54049 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| db46c064-8b24-3cc7-b154-f7cbf1c96a8d | -16.06829 | -47.92382 | 2026-09-28 17:07:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 067b57d9-2682-3c94-bcac-6a859f11c4ea | -13.47816 | -48.63335 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dc6b459d-a514-3137-a455-42e937a38ed3 | -14.31577 | -44.81684 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 784b8a7f-a183-3987-9ffa-883300489106 | -12.44914 | -48.21815 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a532e3fe-6b0d-363a-a3b9-2f0fbc778c10 | -15.74181 | -46.02443 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 21ad8a6c-5e42-384a-8e30-a8e2e0306669 | -14.62921 | -52.10897 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b7003841-cea0-3871-9294-d4e6736dda1d | -12.63974 | -47.28918 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3f5ddecc-b1d9-325b-bc1d-e179d8a8e060 | -11.39725 | -43.41996 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 2d6f7ee0-4ecf-3c7f-ab20-7a6acd6cfa30 | -12.82183 | -49.67204 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d951ee2c-6fab-3eb0-ae34-292add31e910 | -14.32269 | -44.81103 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 577d2b16-ff09-3a35-a469-4800837a810e | -16.4345 | -43.49388 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75ea94b7-de00-341e-b788-1fdd9fa39ea1 | -14.445 | -40.75423 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 74.6 |
| fba2b261-eb8e-3ff6-a85a-037d0608e9f4 | -15.18345 | -46.1754 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1164018c-2b63-37a1-ae48-6561bf7dfd60 | -16.15393 | -42.85835 | 2026-09-28 17:07:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e0e502a9-c5d8-369c-bc8a-52da926a564f | -15.47122 | -46.1448 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 76defcd9-871d-3a05-bae2-3fd23beedede | -12.623 | -47.27337 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5160ff1b-6946-3355-a648-b5b8b63aace4 | -11.38725 | -43.43128 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 3d58ab25-9246-3f68-a16d-a52c3a4a1aa5 | -11.38783 | -42.55644 | 2026-09-28 17:07:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1f9b02e6-3d8a-3ea5-8314-fb86cfaea111 | -18.11667 | -44.3859 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 6410c5d3-b280-31d8-bf27-fdbd217b2377 | -13.32346 | -43.95163 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1b8bb291-5d72-39d8-967b-5cbbf6990476 | -13.69548 | -48.82196 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5f3f3b0d-4463-3df8-8879-331969e9a219 | -14.31213 | -40.32111 | 2026-09-28 17:07:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 13ceed7c-de3c-38b9-8660-e61d4747ad2c | -15.15729 | -43.60509 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1513f5fb-3d03-38e9-86c1-32335c21d331 | -15.08348 | -54.60167 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 404ebd42-3d03-3c05-8813-229767c1b69b | -13.47727 | -48.60394 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bbca3b98-5832-3edc-8e3e-b286389414fa | -15.17633 | -46.13729 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b9ced06f-46af-3d1c-8312-0db44128aaf6 | -14.31883 | -44.81833 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0b1bd2e5-acd1-3fc0-81d3-280446c004f3 | -13.92174 | -47.85426 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 712d100d-4fb6-3b28-9a16-11c22af17989 | -15.12502 | -40.9933 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 6020b55c-69a2-3d97-be3e-bee2143f8426 | -14.45033 | -40.80574 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| fdd09442-0e44-3198-a0b8-0055ff46b29f | -12.6133 | -45.07843 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e6106d9d-ad42-37f2-ae45-9d14bbd2a583 | -14.53577 | -48.30815 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3ed1e517-9930-3421-8113-7468939ed1a6 | -18.21315 | -43.16057 | 2026-09-28 17:07:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f3b43ccc-5fb5-381a-aab2-e2a8706511bc | -12.72289 | -47.27516 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 03d1d29f-a9ec-3685-94b6-e53e3aa001d6 | -15.86405 | -41.26956 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| c25d414d-e1cb-312d-8924-7b367912058e | -15.15269 | -43.61721 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 28.3 |
| f430fd94-6996-30da-9d9c-8cbc17907a39 | -13.37209 | -44.0259 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fde0d295-9685-3898-8b0a-35b63bf72113 | -15.75875 | -43.275 | 2026-09-28 17:07:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a4bf9a1e-ff05-300f-93d2-98c9257c04ee | -15.26641 | -47.62955 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a36f1a1e-e60a-3e1c-9c79-480e176d15ec | -13.47754 | -48.62972 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9661f441-42b9-31b4-a8fa-49521b44a78e | -13.97002 | -54.0139 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b25879fa-9b1e-3873-87f0-3b6bac03f1a9 | -14.53044 | -48.30174 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 68edb9fe-1ece-3b84-b974-96c20771f1b2 | -13.58451 | -51.44796 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d4866e74-5124-3b0b-b9a9-39443d23cadb | -14.86938 | -41.02738 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 512e6cad-9615-3c8c-a50d-2e3ab135a68a | -13.08819 | -47.43679 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e0fb2d77-c237-32a8-9f17-d209b60de3db | -15.68873 | -47.60326 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 74a37a48-4c46-38df-b922-626d2b6a09cf | -15.40729 | -47.90593 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30de14e5-ab2f-3c41-8361-31558efdb6ce | -15.07804 | -41.20467 | 2026-09-28 17:07:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 2d70a368-1047-3f2b-91bf-a52687135005 | -15.58404 | -47.91178 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.2 |
| bbbd5539-cb87-3738-aaa4-e43fde7d43b4 | -14.54413 | -40.74353 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 5e43cc42-1653-3759-aa8c-8668a8025b06 | -17.32681 | -53.95954 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d0b60d6b-4068-3aa9-a831-21bda69a015c | -16.35033 | -42.57527 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| f11c7348-ddd4-3f1f-8c02-3ae088b04122 | -14.49357 | -45.23353 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5bca6859-e19f-361b-ab64-fb1aeb3eacb4 | -18.74262 | -48.23055 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7c32d42d-c30d-3fdc-856d-0b7174b7dd99 | -14.09054 | -44.29007 | 2026-09-28 17:07:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1866e772-d1ee-37a5-b234-450722452677 | -11.36096 | -43.35919 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 492f0812-7a7f-383f-bc4e-47eac06b08c3 | -15.21672 | -46.17519 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b8784455-8364-33b6-ab9a-7d702c459fde | -15.06676 | -54.6042 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 21cb7b45-fc60-34f1-8931-472dca0d0b9e | -14.82246 | -41.60922 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cad331fd-a18d-36fd-99b3-d072699f1fcb | -17.19684 | -46.64766 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e87de16d-ca28-361f-b32e-ec2d89256ff4 | -12.61972 | -42.75748 | 2026-09-28 17:07:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 38.9 |
| 31cc8986-9950-39ae-9c09-750b7a77413c | -11.37968 | -43.4237 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 550be053-8b8d-368d-96f7-3b3a219ab8f2 | -15.40376 | -47.93364 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b0feb890-bb7b-381c-b2bb-2e0901d8635e | -12.9731 | -51.08392 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| e839e8e7-f70b-3584-bf69-632daaf88eba | -12.90927 | -52.0751 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 01675c40-c6e8-3341-a3ae-f4de19cb15a0 | -14.48335 | -53.636 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 682c6e6f-314d-3db6-9e74-04f4765e99ae | -11.64391 | -43.27369 | 2026-09-28 17:07:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e6b88bd1-74c3-32e7-bb06-d5167a14c2b6 | -15.13783 | -43.62767 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 7acf77cf-bad2-3cfc-8e61-f707bc03e68c | -12.4381 | -44.14975 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d6a9162b-9cfd-3219-a531-ef23f350d47a | -11.69987 | -43.49535 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d83c239a-e6f8-3978-bb81-8e7ee8f2a517 | -14.19469 | -40.21196 | 2026-09-28 17:07:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| bfc67968-ee81-3871-9b98-fe1134c4b5ec | -16.88763 | -46.90325 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b546c983-f864-3eb6-ba67-ccdf48a85f9f | -15.20461 | -50.24492 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 30ab1aba-fc74-360b-b28d-51a09da26901 | -16.54468 | -41.46122 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cea4ba8e-db26-3c1d-a599-25b7a6579bfd | -12.88123 | -44.7727 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4c6d2d3d-f2e1-3faa-b76f-d993d1d04587 | -14.08815 | -46.31786 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| dbf526b5-898b-3f8c-8dc7-5476938baf7f | -14.21303 | -53.26957 | 2026-09-28 17:07:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e240cba1-aeb0-3f5f-bfd8-6073b08a6423 | -15.17794 | -46.1714 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ffc699a-9663-3167-b5ea-caff93333a49 | -15.02838 | -49.58184 | 2026-09-28 17:07:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 868fc135-1537-36dc-bf6f-729f491f9025 | -10.81338 | -41.32742 | 2026-09-28 17:07:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 3d9f494b-00a6-307f-8e23-c933ad43a313 | -14.32208 | -44.80791 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| cb7476b5-8b08-3c44-8a53-bb056abdce6f | -15.15337 | -43.6135 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 220a374f-7892-3402-840c-3df72831d5ee | -13.49106 | -48.02651 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5c2b9f74-ddea-3d80-beee-23723b0849ac | -14.15988 | -40.73671 | 2026-09-28 17:07:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c1f9b48e-6462-3e68-914c-9d8d810d7739 | -20.83259 | -57.69666 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b5cf406c-b855-3007-accf-8879e0c5ad6e | -13.51478 | -46.90479 | 2026-09-28 17:07:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 9da5a1d7-b6c6-38d6-9c39-560af3be0115 | -14.75441 | -45.65491 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6d8e7e39-9f61-34c6-ba85-6ac67492ed46 | -15.73927 | -46.03252 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 485a3e41-45cb-3256-a7ff-8cf755fc982c | -15.05953 | -54.60157 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 53b2d208-026a-3c8b-8f4c-880a2a68fceb | -13.36733 | -44.03059 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4737d3b2-1d6f-3ff2-849f-194e6c7082d2 | -14.51669 | -52.48993 | 2026-09-28 17:07:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| bd12dfe8-c3e4-3c69-a85e-edaa45368589 | -19.00482 | -47.25162 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e6330745-da22-3c68-bdb0-f80647fa6863 | -12.87706 | -44.80824 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7ee566ce-5ad9-3a3f-b469-df04379d1f71 | -11.37371 | -43.3931 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1cba8e37-9105-3c77-a729-3000df35b58e | -12.64431 | -47.33982 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 09174737-c61e-300b-8f92-bb1effecdd49 | -11.26832 | -43.53103 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cfb38dbf-c51e-32da-b05a-fa78eb24b4ae | -19.14902 | -46.53433 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1ae2a866-6941-3fdf-8b18-48e12bf27022 | -18.06233 | -41.42835 | 2026-09-28 17:07:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| a9a74e35-12f8-348d-8bb7-e90bf28b52b5 | -17.3419 | -53.17314 | 2026-09-28 17:07:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README133.md)
