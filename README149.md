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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 507492d7-17e8-360a-a22d-a67fb2f48275 | -14.84639 | -45.18627 | 2024-10-07 12:19:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 351eaece-2c73-3d42-a7f6-b90a939e6373 | -14.68949 | -45.13702 | 2024-10-07 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1beb900f-18d3-3ff2-8b6f-b5a92707349e | -13.85595 | -44.62716 | 2024-10-07 12:19:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 8fc1d3ef-65ba-37bf-ae7f-88e96fb8c819 | -13.82892 | -44.61184 | 2024-10-07 12:19:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 80056e04-857f-34c9-b575-e63edc87be2f | -13.82725 | -44.62257 | 2024-10-07 12:19:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 733f76f1-27eb-3ba9-8395-04425cb130a7 | -7.66651 | -45.23231 | 2024-10-07 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| dea6cd57-e1c4-3e96-b369-09cd049dfc69 | -11.97788 | -45.16778 | 2024-10-07 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c5e9fe71-3667-3c41-b029-3d1f4abc5583 | -11.96772 | -45.16617 | 2024-10-07 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e21ff85e-9318-31d6-b391-2a86ab2d47cc | -11.9658 | -45.17822 | 2024-10-07 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 081ebd4c-d35b-30f5-80c4-842145728611 | -13.2453 | -45.58548 | 2024-10-07 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f45ddb87-de3a-3ca9-a382-8bf31e4f21ae | -13.23505 | -45.58386 | 2024-10-07 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3a926027-5c4b-3da6-a9e0-3ccd0d095150 | -14.13474 | -45.53347 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 6ac5be7f-4fda-3974-ba5c-280e07bb17d4 | -14.13339 | -45.6065 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 200f6cb1-f0db-3f33-9388-5d6e24e5fa5d | -14.13285 | -45.54528 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 08972a20-16a3-38e8-9b65-c0e0550b4fcb | -14.12713 | -45.58088 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 355bf0d1-bdb6-3bbd-992c-ee08e0058903 | -14.12659 | -45.51997 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 43fc9783-a078-3dc5-be2e-cdd4ffc97665 | -14.1252 | -45.5929 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 7e0c42c0-7b05-3e62-abf5-9118c8599ca0 | -14.12469 | -45.53174 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 0e3fb34d-4f20-37b5-84c3-1c5e0af2d838 | -14.11798 | -45.51239 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3fb12ceb-b08b-31eb-bd70-87562da0587c | -14.11702 | -45.57932 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 53a4e981-e88f-373d-81da-c76dfc391804 | -14.11654 | -45.51824 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 65f7af4c-e88c-3919-ba35-796fa835b57c | -14.11615 | -45.52414 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 59f8e9f7-a79a-39ab-8562-066694ce13bc | -14.11507 | -45.59139 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| bf3ecf93-baee-3b31-8084-48fd89810c33 | -14.10795 | -45.51059 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d071e5da-4bd3-3fc0-a437-08d8f8ee6de7 | -14.08523 | -45.45847 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| cc924ff7-16a9-310b-b4d8-2a912e46667b | -14.0834 | -45.47011 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| ab16cba3-f352-3ac3-9897-9b395afbc4fa | -14.07524 | -45.45665 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| c15b588f-385b-399c-b7c3-72a8ab568dcc | -14.07339 | -45.46828 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 433d10f2-eb92-37f4-aa15-46148d024163 | -14.06581 | -45.51603 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 06c236e6-6527-39fe-a070-da953fb0e718 | -14.06391 | -45.52798 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 557266d4-d1b8-33a3-9d14-b2f9726eab64 | -14.05384 | -45.52628 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 19d46718-2395-34b9-b175-93a4c26aa9c8 | -12.34198 | -46.41273 | 2024-10-07 12:19:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4ea3b945-e01b-3ba2-a5d0-dbbd2d94975f | -10.14862 | -46.36383 | 2024-10-07 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a4f7938a-2388-34b4-87a0-e8b95cab7836 | -18.59249 | -46.58332 | 2024-10-07 12:21:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 41782acd-8408-3274-81cd-4383a51ccd27 | -17.89327 | -43.98088 | 2024-10-07 12:21:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d6ab5adb-e264-34f9-be6f-60730ec0676c | -17.89183 | -43.99045 | 2024-10-07 12:21:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 9b548b61-efb8-378f-a735-32e126c79be9 | -17.57535 | -43.70148 | 2024-10-07 12:21:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a13b17ed-0168-36a7-9ac0-59c270f2ef31 | -17.57396 | -43.71083 | 2024-10-07 12:21:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f4e0bdff-52a9-3394-822c-6a2d026c2a48 | -17.54766 | -43.76432 | 2024-10-07 12:21:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 050cb752-e684-30d3-992a-a470f2ca5755 | -17.54011 | -43.75354 | 2024-10-07 12:21:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4f09cb4b-6e77-38b3-af87-83e5dfcc6d15 | -17.5387 | -43.76293 | 2024-10-07 12:21:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 93a86237-135e-30a7-81de-2d48553692c3 | -19.25592 | -44.36371 | 2024-10-07 12:21:00 | TERRA_M-T | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ab7172af-6676-3026-8f34-8c2ff90ea0db | -19.2469 | -44.36234 | 2024-10-07 12:21:00 | TERRA_M-T | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2e78b552-7142-396e-88d1-bc2d9fab2d40 | -20.69087 | -44.57238 | 2024-10-07 12:21:00 | TERRA_M-T | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 408f70ef-89ef-31f2-a124-79e0dc768910 | -20.41749 | -43.74255 | 2024-10-07 12:21:00 | TERRA_M-T | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9fb2940a-0782-3f92-a255-aced433945d8 | -20.41612 | -43.75195 | 2024-10-07 12:21:00 | TERRA_M-T | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| bb37e76e-4017-3d0d-b7f4-71a496d48efe | -20.38792 | -43.88257 | 2024-10-07 12:21:00 | TERRA_M-T | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 81ffbb46-7e65-3228-be78-de8e98eef93d | -20.38653 | -43.892 | 2024-10-07 12:21:00 | TERRA_M-T | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1dac25cb-bfd9-32c6-80c8-9ca6620c1f3c | -20.3609 | -44.00417 | 2024-10-07 12:21:00 | TERRA_M-T | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| eaf96c2e-eb21-398b-9aef-642b1040d6e5 | -21.96372 | -45.36566 | 2024-10-07 12:21:00 | TERRA_M-T | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| b26b3448-259d-300d-b901-4960af9a8627 | -21.96222 | -45.37541 | 2024-10-07 12:21:00 | TERRA_M-T | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 4a0c79a4-3f84-3aa5-a868-09159e46899e | -21.71193 | -45.20127 | 2024-10-07 12:21:00 | TERRA_M-T | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| aa03ffba-e303-32d2-ad76-810376ffafc4 | -21.71042 | -45.21122 | 2024-10-07 12:21:00 | TERRA_M-T | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 59e91d72-741f-3a4d-9bf2-9507d36cca87 | -21.67964 | -43.99529 | 2024-10-07 12:21:00 | TERRA_M-T | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 93661d4f-62f1-3725-84a7-c0b260798055 | -21.67826 | -44.00479 | 2024-10-07 12:21:00 | TERRA_M-T | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| bce3eebc-8c85-3e35-a440-c29f531c5f3b | -21.66799 | -44.01285 | 2024-10-07 12:21:00 | TERRA_M-T | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| b86e82d2-6920-321b-a96a-16b9905479d8 | -19.01974 | -45.52914 | 2024-10-07 12:21:00 | TERRA_M-T | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 28436cca-6734-3fa4-bc7c-788eb83de482 | -18.08087 | -45.62479 | 2024-10-07 12:21:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 28d6f280-2ef9-3008-aa8e-c4f8af2cb0ee | -20.83544 | -45.56382 | 2024-10-07 12:21:00 | TERRA_M-T | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 98d3eab4-251a-3be5-a73d-22db9719d96b | -20.53489 | -45.87511 | 2024-10-07 12:21:00 | TERRA_M-T | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0c51507b-2b05-3370-9535-eda52d69d3c0 | -19.70934 | -46.27089 | 2024-10-07 12:21:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 12b0bc63-a991-3b66-9f84-05c5281cae9b | -21.81408 | -45.6768 | 2024-10-07 12:21:00 | TERRA_M-T | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 9d1748c2-9ec9-3ce3-9571-52790eec7368 | -21.00148 | -46.08812 | 2024-10-07 12:21:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 6b4b4463-31cc-31ea-8f62-642474249990 | -20.98256 | -46.08488 | 2024-10-07 12:21:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| f0860faf-1751-38ec-b676-9f49f4d87528 | -20.98084 | -46.0957 | 2024-10-07 12:21:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 919261c1-2602-38d9-a563-d391663f6d25 | -19.19871 | -46.57887 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a2f2320c-c360-3a94-8d3f-8927eac88ad7 | -17.18145 | -47.29121 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 81e1679a-df68-34c9-8043-1c2a10febaa0 | -17.17061 | -47.28946 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| df01b814-e423-3599-9d1f-f32ab12c9bdb | -16.91871 | -47.13905 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 93a052d1-f030-382f-a6f0-30bc5d2afc5e | -16.91633 | -47.15319 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 98db5f6e-3b24-3d1f-8490-4f918fc94ccb | -16.90557 | -47.1514 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1644f25c-5afc-3bb0-aad8-d0277894124d | -16.90294 | -47.14418 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 19d8d8c9-e582-3ec2-8b8f-926462abf503 | -19.20068 | -46.56658 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3c9ded46-c5e0-38b0-bb62-428b71f75b97 | -16.90084 | -47.17939 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| cd558348-0040-3eed-8469-38e3d2a6360d | -16.90066 | -47.15827 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 31.5 |
| bfb3df09-c5d2-364b-a289-5a7e73964d5e | -16.89845 | -47.19347 | 2024-10-07 12:21:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9b7c1b0f-87d0-31eb-ae55-81e414900f35 | -16.89612 | -47.18623 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d8ae1b98-a9f1-3eb8-9947-31bf74dc37b9 | -16.8948 | -47.14963 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1e2edc10-0e69-314e-ab97-1866f22a56de | -16.89012 | -47.17716 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| df24a319-eeed-3d09-8084-e42e33994513 | -16.88992 | -47.15623 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f734d3f9-e391-3448-9140-ecae02b0fb3d | -16.8877 | -47.19136 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 011608ca-02d0-3532-825e-5f359dd18aab | -16.88539 | -47.18399 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 5053ba5c-1f6d-32b8-b859-204c0893d2ff | -16.87918 | -47.15418 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e30b6950-cbb6-3968-bd60-59b60072f3cb | -16.87693 | -47.16792 | 2024-10-07 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 98e6b68a-97e4-36c4-8417-c8b572de42a1 | -17.71845 | -46.40564 | 2024-10-07 12:21:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ea8b117b-0093-3414-b0ba-d1b2a7843db5 | -17.24825 | -46.39336 | 2024-10-07 12:21:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1d582daa-e4b4-3f3a-92b7-629e19a7f14d | -18.31631 | -47.13492 | 2024-10-07 12:21:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5620e074-6f0a-3cfa-95f7-3321e027cca6 | -18.31418 | -47.14768 | 2024-10-07 12:21:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ec783150-6da9-33fb-af88-0b144db06774 | -18.30587 | -47.13287 | 2024-10-07 12:21:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 10423ecf-4854-3b13-9a63-d91b8cf8554a | -18.30373 | -47.1456 | 2024-10-07 12:21:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5086dcc5-5614-3962-b174-88b56d32e371 | -19.21173 | -46.56273 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ea1c38ec-e8e2-3c5a-b641-4241d5b55777 | -19.21065 | -46.56818 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| efb6418a-a2d8-38fb-9508-da421392db31 | -19.20973 | -46.5748 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 941c740d-f69c-38ce-9197-2aca75f89153 | -21.17199 | -46.94031 | 2024-10-07 12:21:00 | TERRA_M-T | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5678d73b-777d-3c18-947e-c21ad92a1483 | -21.31555 | -47.62823 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 842e9380-0f73-3852-97ed-037ad3a9dce1 | -21.31776 | -47.61493 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 24a1f82c-035b-3b39-b466-781c6275b5fe | -21.31998 | -47.60158 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2dd47b92-9a46-3feb-a7a6-a0079184f16a | -21.57273 | -47.74938 | 2024-10-07 12:21:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2f507176-3e05-3dc3-9e76-a7d814aa493b | -21.58084 | -47.76466 | 2024-10-07 12:21:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1c3114f7-8773-31f0-9bf0-ae47b87f845c | -21.58306 | -47.75132 | 2024-10-07 12:21:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 64.2 |


[Clique aqui para ver as próximas entradas](README150.md)
