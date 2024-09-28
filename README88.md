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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fe69a71-2dd2-3129-b3f9-d4451970cf24 | -7.59787 | -60.58368 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8011ec7-cb7d-36e9-8ba0-eedbe281654d | -7.59719 | -60.5878 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f0fcfe1-2e7f-3283-8303-7b5448fd65ba | -7.5965 | -60.59199 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a550198-b6ad-35d4-abff-f9369ee756a5 | -7.59565 | -60.57476 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87545e18-1849-3db7-9fcb-1c10712eafbe | -7.59496 | -60.57899 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4757c4d0-de51-368d-8af3-20a96dad1124 | -7.59427 | -60.58311 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f47c4906-07e8-30d8-aeee-3e686e2c4707 | -7.59359 | -60.58724 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bab4bfc3-db11-3ae8-9671-58ce1fad04aa | -7.59291 | -60.59142 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b891a9f6-915a-37eb-8a1d-e73095fd4f5a | -7.59222 | -60.59559 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06e22fbe-9704-369c-b7de-f3cf3ac65b79 | -7.59137 | -60.57838 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfd1a58c-9c83-3353-a9ab-68d1983391c9 | -7.59068 | -60.58253 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b7008dc-9b95-3a64-a542-561c18d7d09c | -7.59 | -60.58667 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ca44a87-ad93-39f6-97b6-f5186481b07d | -7.58931 | -60.59083 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58827be6-3a61-335b-b6c1-3a59bdfec6e9 | -7.58862 | -60.595 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e7d728b-0f63-3bd7-9172-d0c612350ca9 | -7.58641 | -60.58609 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 369e4277-ba7c-3ffc-8f49-9c97c6ccd4eb | -7.58281 | -60.58551 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d562cd6-9c8d-3f2b-9011-ee6d58b48d13 | -7.58212 | -60.58966 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd10fe9c-8b22-38d3-badd-dd2ccd82472f | -7.56928 | -60.60033 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5e6e6dc-071f-3526-932c-c22237eeaf57 | -7.56859 | -60.60448 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cefd6432-af00-31e0-86ad-8cc21013027b | -7.45932 | -60.41593 | 2024-09-28 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3f20590-9191-3d1e-b259-8c678ffe5883 | -9.25801 | -60.71635 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 216bbd74-9dfc-3fe4-93de-ac4c8bd7ee22 | -9.25578 | -60.70774 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3139be34-8ec2-357a-8aed-a8de31c87394 | -9.24971 | -60.32735 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ce6b951-1d2b-3c9a-bfb7-d37f4897d052 | -9.24695 | -60.49647 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d8c75f9-a795-3cdc-884c-3589daddcdc6 | -9.24629 | -60.50042 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e09573-82ee-36b7-a5d1-955f517b9a3f | -9.2447 | -60.66428 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6762b88-8198-3cc9-8ea3-cf4b991c0c2f | -9.24271 | -60.67636 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f53c9c4e-0c20-3f0e-94d0-eb74bf52724c | -9.2405 | -60.66771 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a060dbb8-07ac-3e2e-bdae-2736ab478a38 | -9.23993 | -60.49528 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1af54a0c-17bc-3e6c-9f39-2ec0482b8294 | -9.23917 | -60.67577 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24d0840d-3074-3ebb-8f8b-780647ca827b | -9.23851 | -60.6798 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0c719fc-8fff-315e-9c95-44ff7c1d2941 | -9.23785 | -60.68385 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd4df2aa-c74e-33e6-8967-147c79ef9c32 | -9.23641 | -60.49469 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eaec748-4b1d-3a9d-8896-55b79b694bb4 | -9.23576 | -60.49865 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c974619f-9d0f-3187-abf1-c6fd6d1f6a79 | -9.22789 | -60.67801 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371d283d-2bcd-3d45-9e9e-5e0319e16c30 | -9.22502 | -60.67338 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8e8ec47-2c52-3cb7-86da-b0733c450148 | -9.22368 | -60.68145 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e2c1a2-1a20-3b67-a24f-0cea8fc9d3a4 | -9.22302 | -60.6855 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c46dbd8-8c22-3692-a82c-85fb3aac1672 | -9.22148 | -60.67278 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d180516-4627-31e6-bf1f-4dee09f064b0 | -9.21794 | -60.67218 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05824eef-ef6c-39ef-b5e6-ecae54713e17 | -9.21727 | -60.67621 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5151365d-0b5f-30fb-a393-fb7a6756462f | -9.18094 | -60.91771 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16f6fb31-0150-393f-b7b1-6a153d1cbd89 | -8.751 | -61.04467 | 2024-09-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02a407d4-2895-3d83-bc3f-ab89c0805ddd | -8.61783 | -60.55336 | 2024-09-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a849689-c989-3ef3-9ca5-42eeac2ac892 | -9.31505 | -59.67239 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d22dfef-652c-3a7a-964e-a4071e91f194 | -9.31445 | -59.67607 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb86895d-3986-3700-b994-168ed1d6e22b | -9.20897 | -59.80774 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0987ff0b-66fc-3ed6-9e68-7f43366172b4 | -9.20888 | -59.8086 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7c25b44-56d5-3662-b470-9b75e4370d98 | -9.9493 | -60.23738 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b24268de-b130-3c15-b54f-795e3f05b807 | -9.94867 | -60.24121 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c81ff7c3-cd45-3723-b49f-575701ccdb56 | -9.94585 | -60.23679 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35a6697b-9a84-39df-a8b7-5ebce296a45a | -9.915 | -60.75433 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb6c1d8f-fd5d-34bc-ae19-a41af307f43b | -9.91434 | -60.75833 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c6d82ab-e764-3518-9c6d-a814cde5c2cb | -9.91186 | -60.72915 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 101ef735-191f-348f-a565-46d3c1d29bfc | -9.90768 | -60.73255 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad28c4a9-de97-39dd-9a65-f46184478aab | -9.8557 | -60.6747 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 890ba2c9-b3cf-35be-8f21-cb4a7da00989 | -9.81891 | -60.47876 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f243809b-d939-30de-82e9-b2cb665fb5d6 | -9.81542 | -60.47818 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1923496c-bfd5-3342-979a-80326e18f688 | -9.77346 | -60.40693 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3322e97a-974d-3474-b6ac-c1b46ffc42f6 | -9.77063 | -60.40246 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2064864-c20d-396d-8b31-0ef1fdeb8033 | -9.75318 | -60.41203 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbcb5b46-b842-3148-9fa3-e1fc8c12e3b6 | -9.7497 | -60.41142 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08e2bdf7-8fa4-39c9-b2aa-da593d5d007c | -9.70844 | -60.75442 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ac3de12-534f-3334-a9c1-20564920862a | -9.70843 | -60.75367 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c04a9091-551a-3501-9421-cc7d57ab8247 | -9.70778 | -60.75847 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b1d056-2ddc-3700-86b5-a73880e99c19 | -9.70775 | -60.75771 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2720ce5e-3c1f-35ba-8cbe-95fd7197c0e0 | -10.03537 | -60.44158 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ed6d7de-7336-37d4-be55-c46dab0f0db3 | -10.03189 | -60.44101 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c06928ec-f7bd-34e7-8c76-1c59ed4455d2 | -9.92447 | -59.9387 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2ce01d83-253f-3a62-a8c3-6d40216c63ba | -9.92188 | -59.91139 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b0a778f-3814-30c8-a2fe-bb42ab3dc615 | -9.91907 | -59.90708 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 72a800f3-22a4-3d80-a057-d68fb32dde3c | -9.91846 | -59.91082 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f882cd65-318f-3492-9ee0-8e85add1bd3d | -9.57782 | -59.78304 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be41c3a7-06b7-3bfb-a26f-8cafe9c2fb1f | -9.56979 | -59.78939 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ea34da-e131-365e-bc10-83105c31b890 | -9.56699 | -59.78512 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bc3e13c-9cba-36bf-acc0-09b4ea84b6f4 | -9.56638 | -59.78883 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e55599d0-8c7c-381b-9485-467f6fd089a3 | -9.56419 | -59.78083 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c959bdc6-f5c7-3d25-8f72-ae61e996440d | -9.56297 | -59.78827 | 2024-09-28 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 333b79c0-5172-3c29-ab7f-4b482300ea89 | -11.93172 | -60.38811 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3cef289-53c6-3620-8839-f6e3cb6c6061 | -11.93112 | -60.39185 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15e3ab37-e7a5-3949-9263-19ee2f5f21a2 | -11.93051 | -60.39561 | 2024-09-28 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64495bd3-c6c1-3098-995f-1928e47bb28c | -11.81617 | -60.25804 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a00d67f-6186-34fe-97a8-8555935c752d | -11.67585 | -60.21527 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c7f171c-3db0-3768-acc2-8197e408c75d | -11.67463 | -60.22271 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6bcc5b7-ea54-385f-9107-2862b42f021f | -11.67402 | -60.22643 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df514a5c-f94a-3cc1-b0ed-8c5f8774f46f | -11.66325 | -60.27074 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecfc5e12-8439-3bd5-aa29-92cd676c0309 | -11.66263 | -60.27449 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e36090ab-ec71-3dd2-a673-96c9d949e0e4 | -11.66201 | -60.27824 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e08e9c6-d3f3-33eb-ab23-1f1f6cbe8478 | -11.65737 | -60.28517 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b64807b6-8bcd-3dc4-b8f5-176739743636 | -11.65056 | -60.28401 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b36eeb8-1d74-3b04-b87c-82e6f8e02e3e | -11.64563 | -60.31393 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e193b02-c31e-3c1a-a7dc-dcb51046a6a1 | -11.64284 | -60.30958 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 689fc418-b664-3c4f-9f8d-b1456adbbc12 | -11.63849 | -60.29345 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f24d704-1afa-37df-ad8c-2e5fd62b126f | -11.6354 | -60.31212 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5298e3a3-64e7-376a-9e08-cbc05075ea70 | -11.63106 | -60.29599 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6047abf6-ef2e-3b1c-a278-908c664f5015 | -11.63092 | -60.29651 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6d005ce-ead9-3dfa-bcee-8a2f6c7b04ac | -11.62471 | -60.29161 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a362975e-6909-3811-a65f-4d76a1354862 | -11.6241 | -60.29535 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbdb82d4-8429-3c37-acf9-94234b743cc7 | -11.6213 | -60.29104 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0f38300-6aef-374c-af4c-e5bf8687f4d4 | -11.61496 | -60.3518 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README89.md)
