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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a993c502-55da-38ca-9dc0-44a39a94555e | -18.22921 | -47.41671 | 2025-10-23 04:40:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 732fa59f-6182-3f85-8837-bee50b1a9d9f | -17.61175 | -46.59841 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67d0fd3e-cea2-3806-945d-3612a312af4e | -23.85985 | -51.43275 | 2025-10-23 04:40:00 | NPP-375D | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9227a8f6-79d6-3ba2-a20c-6ff391619272 | -17.20792 | -47.65541 | 2025-10-23 04:40:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f14fe10-a1dd-3f75-909e-ac27aebf0e6c | -21.94967 | -42.92194 | 2025-10-23 04:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0d9b7718-d2ba-3185-9610-41a1febb4740 | -23.55748 | -46.42639 | 2025-10-23 04:40:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e23b40c9-3421-39f5-9d70-96740632d1ec | -22.23731 | -56.10303 | 2025-10-23 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6813032-53e1-3cc0-95e7-fa2636fa86c2 | -18.17406 | -46.69977 | 2025-10-23 04:40:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d98b7d2e-3c66-3405-9a41-3836b3d0cfa7 | -19.47563 | -46.58425 | 2025-10-23 04:40:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 800dafb4-b01b-3976-8e8f-a23ca8ed1900 | -20.13039 | -41.80172 | 2025-10-23 04:40:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e6ef3aaa-6e0a-3638-9320-c5db2dad3843 | -18.31594 | -50.31946 | 2025-10-23 04:40:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e5275f03-f153-3b49-874f-d2212ceef084 | -19.99823 | -42.19669 | 2025-10-23 04:40:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4fe8c109-56f0-3ad5-8cfb-f61dacd69737 | -17.61667 | -46.61836 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4519c085-a10f-341a-898e-60b0e294a22e | -17.61076 | -48.57667 | 2025-10-23 04:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05be8bae-dc0e-388d-a094-927575fb999e | -19.8591 | -44.80924 | 2025-10-23 04:40:00 | NPP-375D | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffc87bff-5939-3dc6-9216-d83a44db9f0a | -17.6036 | -46.60198 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dcb0b83-b5fd-3fdd-8b05-37974fe71919 | -19.15119 | -49.13105 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2b8a13b-1839-3f93-82f3-0425ecc1132c | -20.83268 | -56.51676 | 2025-10-23 04:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81122cfc-3248-3b7d-a832-f13f3457f0e9 | -20.55644 | -54.55365 | 2025-10-23 04:40:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d2ab054-c2f5-325e-beb2-75496f4b144a | -17.55579 | -51.04036 | 2025-10-23 04:40:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0010043-07f6-301a-84cc-a3aa00688a9a | -17.60787 | -46.62665 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 151810d4-d2db-38d7-998e-e0e2ec3be1fe | -21.84354 | -43.71189 | 2025-10-23 04:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0ca82497-a9ba-3fc3-9fb4-d0551f52625d | -19.30253 | -45.45904 | 2025-10-23 04:40:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28fa0607-134a-3e5d-a981-b721c9838b77 | -22.14584 | -44.83445 | 2025-10-23 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a246d389-8f9d-340d-8487-76d05e818945 | -20.63834 | -42.71455 | 2025-10-23 04:40:00 | NPP-375D | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 385e4ae5-9b7d-3079-a696-6d59bab4d1f1 | -16.87098 | -51.52943 | 2025-10-23 04:40:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc3dc558-e9da-3c5a-a121-af1ece3e6da1 | -17.60605 | -46.612 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8895211-a993-300e-90f1-331521ced68b | -17.61111 | -46.6031 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f76a012f-c4b1-3fe0-9ee5-a2f1aed2d123 | -18.29005 | -47.69661 | 2025-10-23 04:40:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9899d741-d5ae-30d8-8242-ed79da748fa5 | -18.72045 | -46.82854 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c731033a-dd36-36bf-9d59-f24f227674b8 | -19.37269 | -45.84328 | 2025-10-23 04:40:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ee1ab3a-9333-30ca-bdcd-f5e2940da020 | -17.14972 | -53.3139 | 2025-10-23 04:40:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e730916-c134-3eab-b1c7-a7cda767c935 | -21.73651 | -45.64932 | 2025-10-23 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5bf1e31f-c1bc-332c-8cac-61339019d38b | -18.72038 | -46.83128 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 219cd0d6-3613-337f-8618-65005053779f | -23.59362 | -54.76722 | 2025-10-23 04:40:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f15325b8-420a-3e0a-9ff9-2965fd114300 | -23.86752 | -50.51028 | 2025-10-23 04:40:00 | NPP-375D | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dfdae0dd-be5b-39f5-ac4b-48c20c4eeeb8 | -17.51933 | -49.21583 | 2025-10-23 04:40:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2179b249-27f9-34b9-81dc-48534e3d3a52 | -17.62237 | -46.60479 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0658eac5-ec3c-3748-bf0f-5e60074b06d9 | -18.72414 | -46.8318 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97926c3c-56d2-37a6-8e66-68a6bfa390f0 | -17.79502 | -47.62346 | 2025-10-23 04:40:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40acf50d-7d86-3ed7-833f-5f507c9028e4 | -17.61926 | -46.59954 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf8fecf2-9b64-37f3-ae86-b17745b3f511 | -19.26422 | -49.35746 | 2025-10-23 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ea4ebd54-2489-34fa-bbfa-d8a3e426e503 | -17.60363 | -53.8472 | 2025-10-23 04:40:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae7ec3a1-7557-31db-9e91-8c59dfdaaacd | -19.76521 | -41.30036 | 2025-10-23 04:40:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd35d390-f27c-31bd-81b5-b098a6a60921 | -17.60723 | -46.63132 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c288adc-fc8d-325d-b371-693d2841ad88 | -17.61486 | -46.60365 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d373e2c5-e510-363e-b104-d3db5b633196 | -17.62418 | -46.61945 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2636aab2-f502-3846-bd3d-0a1425b548f7 | -17.61076 | -48.57668 | 2025-10-23 04:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2029b4bd-399b-331d-94d8-afeece0b8977 | -21.95367 | -42.92772 | 2025-10-23 04:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 88b1056e-6e95-3dca-bb67-5be04249d733 | -17.61732 | -46.61364 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9562c2e3-c3de-32cd-be24-377bb6074693 | -24.07892 | -49.62278 | 2025-10-23 04:40:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eb49d5e0-5e8c-3db6-8b74-25d48adb848e | -17.60412 | -46.6261 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 936bf21f-7d23-3f1f-a6ba-62b708c2cc93 | -19.99823 | -42.19668 | 2025-10-23 04:40:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6f2a68c8-a4ed-3e93-8c34-c11f4ea43399 | -19.76521 | -41.30035 | 2025-10-23 04:40:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f758345d-e00a-3917-8322-f58aa98d3649 | -18.22498 | -47.42049 | 2025-10-23 04:40:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7943e710-a8df-342f-9544-46f9fcddc14d | -23.55748 | -46.42638 | 2025-10-23 04:40:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2a4234c7-628b-31c9-ba86-763718e3d7aa | -17.61667 | -46.61837 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d045092b-c1db-3b0f-90d7-012d9bd53ac5 | -21.67811 | -49.05371 | 2025-10-23 04:40:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73405394-3ae6-3152-a9c4-52246fd97075 | -17.62483 | -46.61474 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e2bfbc6-db01-3f13-9e1d-5d10ca62e32e | -17.62302 | -46.60011 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 007a6f9c-4a6d-38b8-b83a-200fed088c6d | -17.63966 | -46.64571 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aef3b674-5b26-351c-8cd6-2d4502c9e90e | -17.60541 | -46.61671 | 2025-10-23 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87c92aa3-7384-3fee-aea2-584021fe9283 | -18.69031 | -47.05473 | 2025-10-23 04:40:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f5ec135-c9cb-3f90-b3e1-3c31386d21b8 | -18.64937 | -49.08851 | 2025-10-23 04:40:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0948d392-4c57-3ca1-ac2c-94b57173fa3c | -19.45363 | -49.32475 | 2025-10-23 04:40:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 705c2689-9abb-3420-a792-e74ab328f182 | -18.69093 | -47.05012 | 2025-10-23 04:40:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09493279-1030-3175-9120-da081bddaade | -21.7407 | -45.64996 | 2025-10-23 04:40:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bf54a53a-585f-3589-86a3-2e6c34e834be | -17.55187 | -51.0434 | 2025-10-23 04:40:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc7d43b6-759f-3fec-9935-e479833ecbf1 | -23.43857 | -47.43058 | 2025-10-23 04:40:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0ecf64f1-34f5-3b05-bc5f-7a78c6446108 | -22.24858 | -49.92109 | 2025-10-23 04:40:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10af147f-4fa7-3aad-b247-38b19ff44745 | -18.72477 | -46.8271 | 2025-10-23 04:40:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b1ed6c5-83b5-37d6-ae6c-b26ddf590978 | -18.90107 | -49.79753 | 2025-10-23 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6603019f-d0c4-390f-a940-8802da4d5da5 | -23.65075 | -51.68726 | 2025-10-23 04:40:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 159de24c-bea4-32e4-bf4d-aa33ed0f0c9a | -29.71149 | -51.77142 | 2025-10-23 04:42:00 | NPP-375D | TABAÍ | RIO GRANDE DO SUL | Brasil | 4320859 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| e2011701-e9f2-3e73-a62a-d5a2c824a441 | -25.21853 | -53.28455 | 2025-10-23 04:42:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a74bab49-bd14-3634-993b-c15ce9e5bbc2 | -29.71149 | -51.77143 | 2025-10-23 04:42:00 | NPP-375D | TABAÍ | RIO GRANDE DO SUL | Brasil | 4320859 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| b81d2418-9813-3d51-a2d0-3e9b4da0f1dd | -25.22629 | -50.90312 | 2025-10-23 04:42:00 | NPP-375D | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42d6e18b-0de8-3cb4-8140-c3a4e86483fe | -25.94667 | -49.74534 | 2025-10-23 04:42:00 | NPP-375D | CAMPO DO TENENTE | PARANÁ | Brasil | 4104105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c126beaf-1204-32f0-b458-dc3efc740eda | -25.2229 | -50.90252 | 2025-10-23 04:42:00 | NPP-375D | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 849ed529-86d9-33fe-acd5-ddb09f263fa2 | -31.56004 | -53.72189 | 2025-10-23 04:44:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 70a1897c-a492-3241-83da-1d6cd4d0faa4 | -30.62767 | -51.77714 | 2025-10-23 04:44:00 | NPP-375D | CERRO GRANDE DO SUL | RIO GRANDE DO SUL | Brasil | 4305173 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 8ba71fac-0911-3128-b8c7-20a4f379e669 | -31.56671 | -53.7233 | 2025-10-23 04:44:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 936b94f9-59ff-393b-ba08-c7b66a0ad746 | -31.83649 | -53.04469 | 2025-10-23 04:44:00 | NPP-375D | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 42e1aa57-1994-39a2-82c2-8b99952f8afe | -3.0169 | -49.4694 | 2025-10-23 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f5463367-b810-3b76-a548-df36702b520a | -12.0036 | -46.7667 | 2025-10-23 04:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 26d9bd26-5ac5-363e-9e75-fb8abf3c1ec9 | -3.0168 | -49.4906 | 2025-10-23 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 1193fd34-c282-3968-9a07-9c7338ba967f | 0.38032 | -50.93812 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04dcbcc7-4495-3e17-8cb2-f7b9739eec72 | 1.34386 | -50.68987 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad4cc624-ddd5-3243-be8a-79329ff2e1e4 | 1.65891 | -55.75171 | 2025-10-23 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56f87508-fd8d-3b6b-a695-7ad17e15fc76 | 1.55485 | -56.0161 | 2025-10-23 04:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| accb0c9a-1800-3fe8-a731-4531cbb014a6 | 1.65698 | -55.75955 | 2025-10-23 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44a5c1ad-dff8-3d32-8f35-8dd150a2e02d | 0.98725 | -51.29203 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.1 |
| c1f240bf-e761-3e83-957c-7861681417d5 | 1.65928 | -55.75033 | 2025-10-23 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffc6802f-f5c4-35d3-a0c3-1be6d85c9ede | 1.34443 | -50.69348 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10ed8cb1-79c6-37d2-95b8-7b8a716f3fab | 0.38427 | -50.9412 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed16009e-de76-3b47-9b49-6a6209fb45cc | 1.34329 | -50.68625 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1780f34-3749-39c2-bdfb-76151dc859c0 | 1.65957 | -55.75603 | 2025-10-23 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c113864-b319-3ba0-8d40-1611304e9b41 | 0.3837 | -50.93759 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 002f9dae-de8e-32fd-9924-12d0ba548f1e | 0.39046 | -50.93654 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ff8cdfa-d6c4-3b6b-9a46-3beb64310be4 | 0.98472 | -50.066 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README28.md)
