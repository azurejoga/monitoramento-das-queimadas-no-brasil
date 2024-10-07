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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2737f965-be3d-3f5f-80d6-822eae08f0af | -20.44575 | -47.68614 | 2024-10-07 01:28:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e0cf524a-7ba6-3dda-bad7-3df56e9d76f4 | -20.45476 | -47.66366 | 2024-10-07 01:28:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1190.4 |
| b057c7bb-c358-356d-ba77-8c70b4891914 | -20.45553 | -48.64452 | 2024-10-07 01:28:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 67462e9f-923c-3e4c-8679-4252aec8a1b5 | -20.45838 | -47.68374 | 2024-10-07 01:28:00 | TERRA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 794.0 |
| 95d3cc0f-a819-3c68-8665-485d51118866 | -20.46737 | -47.66102 | 2024-10-07 01:28:00 | TERRA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 367.1 |
| 5d1ed7a1-84b4-3b27-8835-cd7c0c1957fe | -20.47092 | -47.68086 | 2024-10-07 01:28:00 | TERRA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 830dac60-368d-3745-b122-cdc0168b35cb | -20.47984 | -47.65237 | 2024-10-07 01:28:00 | TERRA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 7d7f9e09-0d6a-3ed5-b978-01479d0da7b3 | -20.48 | -47.65855 | 2024-10-07 01:28:00 | TERRA_M-M | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 4064f97c-d24b-3d71-8ebb-81429af09450 | -20.59032 | -48.49651 | 2024-10-07 01:28:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 86ac1d9d-71cd-3e29-9acb-f2c56d0ed623 | -20.59906 | -48.47649 | 2024-10-07 01:28:00 | TERRA_M-M | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 136.1 |
| f38a796c-6685-3fea-9a3a-0f43872b1a5d | -20.60219 | -48.49438 | 2024-10-07 01:28:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 468.6 |
| 5a040b74-473d-31da-bf8f-eebc8b4fd2ca | -20.77324 | -54.8232 | 2024-10-07 01:28:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 811644f1-30e4-3de9-b19a-9427222afd66 | -20.78213 | -54.82177 | 2024-10-07 01:28:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 809127bb-7e16-3a9b-a178-2592e4448114 | -20.78344 | -54.8313 | 2024-10-07 01:28:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 75776be1-61e8-3837-962f-48bc2610633b | -21.06178 | -47.22709 | 2024-10-07 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 19959030-cc03-30ca-b81a-3de60d492f85 | -21.57841 | -47.74205 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 296.7 |
| b5771f46-2a2c-3473-8f19-9a3ad6bdd07b | -21.0638 | -47.23278 | 2024-10-07 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 77c8ca6e-3838-3c29-9e60-64cc06ec4956 | -21.06575 | -47.24825 | 2024-10-07 01:28:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d9495676-6be0-3bfb-a165-f427146b8876 | -21.06741 | -47.25287 | 2024-10-07 01:28:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 53.2 |
| aa2fca2d-b4ec-3fe8-866c-c513f2fc5096 | -21.0747 | -47.22465 | 2024-10-07 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a26512a1-afed-3a66-9d04-775cea25efe4 | -21.07665 | -47.23007 | 2024-10-07 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 91db7e61-83fc-31c9-97e5-b4fb8c52aed3 | -21.07849 | -47.24504 | 2024-10-07 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 3c9afe4f-07d9-3e5d-9037-953624c3a5ad | -21.08018 | -47.24976 | 2024-10-07 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a82a46ed-ecf5-3399-96e9-9d76d7e70b1e | -21.27684 | -47.39021 | 2024-10-07 01:28:00 | TERRA_M-M | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9e7b72d7-ec6c-3cfb-b5b1-0efc22d042d2 | -21.28002 | -47.40488 | 2024-10-07 01:28:00 | TERRA_M-M | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b00b352b-64dc-3bda-9ca2-ed10b2a1b6e9 | -21.2804 | -47.41008 | 2024-10-07 01:28:00 | TERRA_M-M | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b6a30f19-f526-3712-bf63-8031fe8176b9 | -21.31302 | -47.59329 | 2024-10-07 01:28:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f18ad2e9-81c0-3fcf-b15a-5086da80ce8e | -21.31645 | -47.61261 | 2024-10-07 01:28:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 49.9 |
| ff6be87c-33f6-3c0e-b53f-9024c479f865 | -21.31754 | -47.60725 | 2024-10-07 01:28:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 99451e2c-b642-363a-a832-1b0a1cd01f11 | -21.33945 | -54.65236 | 2024-10-07 01:28:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 68f13a99-c8d0-33bc-8bfd-3843058be24e | -21.34302 | -50.13706 | 2024-10-07 01:28:00 | TERRA_M-M | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 06999bd1-a7b1-35cc-a712-decece6d6339 | -21.34519 | -50.15028 | 2024-10-07 01:28:00 | TERRA_M-M | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 04b00d45-6f22-313b-843f-07a8d9f50694 | -21.35339 | -50.1351 | 2024-10-07 01:28:00 | TERRA_M-M | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 484d41ce-eb78-30a6-8b62-a97e7d60034d | -21.35555 | -50.14833 | 2024-10-07 01:28:00 | TERRA_M-M | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 15288f60-18c2-32de-8e9a-54ffd0eb2cac | -21.39628 | -57.25104 | 2024-10-07 01:28:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 428d9781-57e3-32e0-8e87-d5b154e49f12 | -21.40617 | -57.25017 | 2024-10-07 01:28:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8b2b5071-fc7d-3f09-92bf-5f52959e36e5 | -21.51146 | -47.74173 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b79ee149-b4cb-339d-9a0d-f8af9b7d9ee9 | -21.51361 | -47.73557 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d7a868c7-c6a7-3fc6-afc7-a2c259cf6573 | -21.51495 | -47.76141 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b698f089-f871-3a21-a2ff-8c622fa749e1 | -21.51725 | -47.75526 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 46.3 |
| b704ea7d-2290-3f34-a50c-4563a992e463 | -21.52722 | -47.75898 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 31.8 |
| f6517fce-de46-30ed-80d5-43e7d750d060 | -21.52953 | -47.75288 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7458f40c-7bb2-3970-9eb6-98bf5b1f0a84 | -21.53945 | -47.75634 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 09e0e1b4-bbb5-36b8-a287-62ea9c8f3960 | -21.59461 | -47.97211 | 2024-10-07 01:28:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| df34867f-4232-3039-87e6-d9dc69aeef35 | -21.54045 | -48.04646 | 2024-10-07 01:28:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 81765626-6c8c-3c68-a6ec-efbc55aa9d7f | -21.54374 | -48.065 | 2024-10-07 01:28:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b34c24d1-eca6-3059-bc60-e7f9676cd145 | -21.55046 | -47.72818 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e2a313d2-c663-3be1-a5ad-0ae6bfb4d4fb | -21.55391 | -47.74714 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8bcf03e4-500e-38de-bd80-37a247a45e33 | -21.56279 | -47.72598 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 40b389de-8fb9-3c4f-a100-26f68acb6e7f | -21.59949 | -47.71774 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 51.0 |
| afced295-ff43-3f91-8154-19b45106b67c | -21.60175 | -47.71051 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d4713169-530f-30aa-b245-242ed6755367 | -21.60285 | -47.73664 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f462a5d7-d2f1-3b24-94e0-4c8b92791fe8 | -21.60526 | -47.7295 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 506b9b60-76d1-3afd-ad5f-31ddd1cc13d5 | -21.62729 | -47.73124 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 97511457-4758-3da3-bfab-0080e87989df | -21.64205 | -47.72208 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 91af367c-0879-36d2-87dc-b002ea0b5430 | -21.65426 | -47.7193 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d4a28f37-1b88-317e-9a9e-f402540367d0 | -21.65769 | -47.73831 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 7a52f827-ac5f-3597-9b4f-b5ffd6415adb | -22.1966 | -48.16452 | 2024-10-07 01:28:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 972d7250-0d9d-3085-94b8-c6ad154095f2 | -22.19966 | -48.18172 | 2024-10-07 01:28:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c7e88405-af34-3c7d-88b7-1c312b9fe8f6 | -22.20831 | -48.16203 | 2024-10-07 01:28:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4eb5313b-1400-3bd1-8dce-f2cdde6ea000 | -22.21132 | -48.17908 | 2024-10-07 01:28:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 45.1 |
| b6c7be6d-e810-31ef-80d1-1bef3e7dc750 | -22.3761 | -48.5906 | 2024-10-07 01:28:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| 0c88ceb1-cb88-3cb9-81c3-8a24641ef582 | -22.37893 | -48.6069 | 2024-10-07 01:28:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 30b51084-d6a9-324f-8f89-cf0854b5f1ea | -22.47862 | -48.37622 | 2024-10-07 01:28:00 | TERRA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6bb3818f-d54a-3f24-a2bb-f739ecfcb7f0 | -22.48659 | -48.36831 | 2024-10-07 01:28:00 | TERRA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ca2d5e23-413a-398e-b306-6c7afc892914 | -22.71455 | -53.22912 | 2024-10-07 01:28:00 | TERRA_M-M | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 3aae273a-94f5-3ab1-a58e-0bad487db19c | -22.71593 | -53.23876 | 2024-10-07 01:28:00 | TERRA_M-M | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 05321cd3-296b-3745-ab6f-72dad01e3e75 | -22.9267 | -52.78621 | 2024-10-07 01:28:00 | TERRA_M-M | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 014653fd-9b3b-33ad-bb4c-e42fbeb921f4 | -22.92813 | -52.79599 | 2024-10-07 01:28:00 | TERRA_M-M | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b3202353-b888-3dfa-b7c4-96ee8ecc147e | -22.93953 | -48.57224 | 2024-10-07 01:28:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e12bb73b-9f1e-38be-b7bf-e216d99e3972 | -23.0417 | -49.85259 | 2024-10-07 01:28:00 | TERRA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.1 |
| 91a1cb61-4034-3391-9829-7920f50a5b03 | -21.59126 | -47.95356 | 2024-10-07 01:28:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 256.8 |
| a56d63b1-3e9c-3c2b-8b5e-9df018d6d796 | -23.10944 | -51.61259 | 2024-10-07 01:28:00 | TERRA_M-M | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| f2cc33cc-5ac4-335b-9944-ef929e0eb72b | -23.14866 | -49.81177 | 2024-10-07 01:28:00 | TERRA_M-M | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 359e867c-a362-39b0-b468-f0695eed12fe | -23.43429 | -47.04745 | 2024-10-07 01:28:00 | TERRA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 9e127f47-b4e8-3a1c-9936-c8b7d6c6eff0 | -23.43784 | -47.06706 | 2024-10-07 01:28:00 | TERRA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| e146a384-27cd-3ead-bfcc-424fe277482f | -23.4391 | -47.06125 | 2024-10-07 01:28:00 | TERRA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| b23518c9-160d-3caa-83a3-3aedf92089a7 | -23.89375 | -54.2274 | 2024-10-07 01:28:00 | TERRA_M-M | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 53b46c11-e7bc-3681-9856-c7dcba252f26 | -20.1114 | -49.06804 | 2024-10-07 01:28:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 0bdec56a-f62a-3480-b855-91e82bac4908 | -21.59064 | -47.73942 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 229.1 |
| a38d5781-c07b-3549-aa3c-c42f3cdfe731 | -21.56611 | -47.74435 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 330ff8a8-b685-3136-aa83-156d528a376b | -21.58174 | -47.7606 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5083a41c-1c4f-3123-9fc4-2e75d89c2d17 | -21.58739 | -47.72127 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 4a4d6d1a-3aa0-3553-bfac-53ad74530e6c | -21.58792 | -47.935 | 2024-10-07 01:28:00 | TERRA_M-M | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cd73f8b4-9d86-32c1-906d-d20bab2faa2f | -21.5695 | -47.76313 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 97bc2153-0940-31eb-836d-9c3de48c9492 | -21.57517 | -47.72406 | 2024-10-07 01:28:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 0e795233-7c88-39e6-9f68-6df0385011ec | -23.15512 | -45.54724 | 2024-10-07 01:28:00 | TERRA_M-M | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| 9f3f42ce-7408-3c9d-ac49-261b10c403d6 | -18.29907 | -47.14061 | 2024-10-07 01:28:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 32.2 |
| f58a99ec-22ae-34a4-b872-7771132be824 | -18.58581 | -47.31497 | 2024-10-07 01:28:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a0637bb2-1dbb-3de2-95dd-6e55c5fa75e9 | -18.59297 | -47.30719 | 2024-10-07 01:28:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| f96596bc-b3e8-3ad0-83a0-742cd3f1b7da | -18.59932 | -47.3125 | 2024-10-07 01:28:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| fd088899-abe6-348b-91cd-92e1dbc54ca7 | -19.16502 | -50.6406 | 2024-10-07 01:28:00 | TERRA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| f1d04de1-f607-3b52-8b3f-19c22097c620 | -19.39487 | -51.69131 | 2024-10-07 01:28:00 | TERRA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 96112ab3-de2e-3f50-939c-c2e695141812 | -19.42712 | -47.97264 | 2024-10-07 01:28:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 32.1 |
| d7b6dd11-ca48-3abe-9a1a-4a8ead7f45cc | -19.42717 | -47.96616 | 2024-10-07 01:28:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 50c52003-48f0-3d97-8be0-3a5d4a4e233e | -21.57586 | -47.9376 | 2024-10-07 01:28:00 | TERRA_M-M | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 21.7 |
| fb1a098a-3e1a-3f2a-a279-e1e8e9b454bc | -19.55549 | -55.06474 | 2024-10-07 01:28:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6a4234ac-5e4e-374a-97e3-f35e2b855e02 | -19.55677 | -55.07414 | 2024-10-07 01:28:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 124e44fa-783e-327e-84b1-0f3c01a264b4 | -19.65809 | -56.46597 | 2024-10-07 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d26d2717-b4ea-3a20-b2c5-e1212e13471d | -19.6594 | -56.47622 | 2024-10-07 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |


[Clique aqui para ver as próximas entradas](README26.md)
