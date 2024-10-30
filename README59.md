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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d5cc189-e327-3fbd-a89f-7a8a98de5e99 | -2.51441 | -49.19678 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc37e651-7969-3ec0-9ec0-fe7736a2f721 | -2.51162 | -49.19276 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13fda088-83d1-3529-8de0-431efdc75b29 | -2.51158 | -49.17124 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0e6e4b4-0251-37b2-9e07-5975f9786ac1 | -2.50933 | -49.16372 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2597b556-94c5-3d46-b72f-8f42cd3fc025 | -2.50599 | -49.1632 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55f4a59f-1aa7-3e94-9b2b-3af1bea1733c | -2.49461 | -49.30099 | 2024-10-30 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25eac5b6-7210-3684-85f6-094959b9ba55 | -2.48752 | -49.12803 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e1ed82d-5a7b-39f1-9586-45a71c173f2b | -2.48078 | -49.68652 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212f9324-8786-35f5-934b-4e9d311896c1 | -2.47038 | -49.38995 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42b04bca-548f-3482-9e91-2d00a1758149 | -2.41333 | -50.41788 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd62d6d6-d11d-3931-b2bf-fab9b0d4e816 | -2.41278 | -50.42134 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dd0f692-4d96-3071-832d-3d124c93a785 | -2.40614 | -50.4203 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5c84638-c37b-3adc-ade6-0b4a6d834ea3 | -2.36383 | -50.32174 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8d12f91-7880-35fc-8904-8a659845e781 | -2.36329 | -50.32519 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e915f372-631d-3ab6-8601-2cca6d5443c0 | -2.36083 | -50.32432 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33cd2477-1938-3c7b-9146-203d1aa2e6b3 | -2.36028 | -50.32777 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd772f2f-b778-3513-a9d9-351cb046ebd1 | -2.3575 | -50.3238 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b58f722e-b99f-3057-9aec-63a42004f2a2 | -2.35696 | -50.32725 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c149fd3b-0c86-397b-b178-3f3b694a1768 | -2.2118 | -50.32224 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a32ed49-9166-3019-ac07-8f3bdea256c4 | -3.4006 | -50.318 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56ba0bfc-8ecc-36ee-bf29-3946600bccb5 | -3.40006 | -50.32145 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1c8638e-2d39-3047-889b-d7bda5890c0c | -3.37966 | -50.34301 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92f5e529-be3c-3a48-b167-e28172ba65a5 | -3.35788 | -50.26542 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f8ff558-45c3-3f97-bfaa-df13f5c5b94e | -3.35734 | -50.26886 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3a3ce40-b386-3c45-a444-1d79e4672247 | -3.35456 | -50.2649 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fae32be-ed3c-3c34-aae6-b5dcb998d0cd | -3.35402 | -50.26834 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 581f73ba-0acc-32c2-878b-b1b83db0046d | -3.32186 | -50.30155 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1fbe024-32b3-30ff-b578-5fe2e5f21c1b | -3.32131 | -50.305 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a224227-3783-3c0f-ba55-8294a3c349a3 | -3.32113 | -50.24139 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32d7c548-38d9-3413-b504-3fa7b57903d8 | -3.31854 | -50.30103 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da83a504-385e-3197-a893-e5880173bdba | -3.31799 | -50.30448 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b51220b1-5631-3753-968d-242614ea41fb | -3.31781 | -50.24087 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3deebbf-9881-3918-b6f9-26b24e55bd8f | -3.31576 | -50.29707 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c069753-e7c5-31f5-803f-2ddce66fb05b | -3.31522 | -50.30051 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdc5baa4-34cc-369d-954c-55716e8218ab | -3.2918 | -50.23328 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fda4957-69e8-3e03-8a95-29e20d21730c | -3.29126 | -50.23673 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f935d427-45e8-371b-9844-6aafc7eca3b8 | -3.28848 | -50.23277 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb94165-276e-34aa-9abc-dce11f4fa13a | -3.28794 | -50.23621 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46401f99-865d-3356-af6a-ee4eb01c5251 | -3.28517 | -50.23225 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f94783d-02a1-3904-b727-1921ac634fe4 | -3.28462 | -50.23569 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04631713-eeca-38f0-8f8d-c74ce0d5befe | -3.27872 | -50.29483 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05c4f282-2c61-3905-83e9-f5d9ecc0c6d5 | -3.27335 | -50.35051 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85dc1b40-f88f-327e-bd4d-24369a0f3686 | -3.27057 | -50.34654 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a475dfa-fda7-3f37-8bec-f0f8bcbecaad | -3.27003 | -50.34999 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 2fe1fade-c5fe-3d05-9f06-23af5a904fa3 | -3.26948 | -50.35345 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 42be5a49-c19a-3343-9920-e4260dfa51dc | -3.26894 | -50.3569 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d51da8-d832-353f-8b0b-36bed6bc8599 | -3.2678 | -50.34258 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a92741c-98f4-3793-9c5f-aa533d1372a5 | -3.26725 | -50.34603 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7880610-7acf-3797-95dd-7a731afa9282 | -3.26671 | -50.34948 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 5242938e-af71-3c5b-90ad-968313649e39 | -3.26617 | -50.35293 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| a6603b01-538b-3266-930e-95be2ed45b54 | -3.26562 | -50.35638 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e275578b-9efb-3f94-8ebc-8f0da5eb34de | -3.26448 | -50.34206 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c954d71-5751-3e5d-8389-277445a6de63 | -3.26393 | -50.34551 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 376bd372-e784-3cb5-aebc-41c7a74b410d | -3.26285 | -50.35241 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7f43d0fd-5222-3dfa-b540-c3e06f6eb239 | -3.2623 | -50.35586 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a4de2a7-2250-323e-8536-ce5c1e5d6d96 | -3.26116 | -50.34154 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 082e6ec9-f37d-3ace-931b-3abb0d41be6c | -3.26061 | -50.34499 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57e644dc-2b9a-34e8-a56c-c05294f92086 | -3.26007 | -50.34844 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 5a92b5db-6265-335f-bff0-6cb1544a88c3 | -3.25953 | -50.35189 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 986429f0-15ff-381a-aa5a-1d475cddf766 | -3.25898 | -50.35534 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f02ba70-4479-338a-a4bb-602f8c21d61e | -3.25784 | -50.34103 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc2b1028-abbd-3ad7-bfb3-3bdf1874ac00 | -3.2573 | -50.34447 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5acd23d7-05ed-30d9-aa84-a3c2510c3348 | -3.25675 | -50.34792 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b45ca380-2f49-3245-9791-93efbf4777cc | -3.25621 | -50.35138 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 4492dfa9-2f58-36a4-91ef-71f93860db4e | -3.25567 | -50.35482 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44e5bbf7-f72d-31e4-ace7-e0338423cc97 | -3.25398 | -50.34396 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57778a72-6556-3679-a5a4-4226cfa41189 | -3.25343 | -50.34741 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 6417dc3d-3565-3a50-ae7e-cb338242aaf5 | -3.25289 | -50.35086 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 3f668f8b-c699-3bf8-9461-4dd708ea0f59 | -3.25235 | -50.35431 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc69044-2475-3e8c-b2e3-432d61f08f60 | -3.2518 | -50.35775 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2bdbc07-7094-3b67-a94d-9ac9f2d8ffbf | -3.25011 | -50.34689 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51ae7916-e41f-339f-ab82-c35b157d20a0 | -3.24957 | -50.35034 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f708839e-eb3b-395e-98f6-20476f14a092 | -3.24848 | -50.35724 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3577d627-0096-3af1-bcf5-a9ad766c828c | -3.03002 | -49.61588 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c17bdaff-3166-3f7b-a6cf-803e3e2d8e81 | -3.00502 | -49.58363 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b28ae595-b1f2-3cf1-9aba-d12b93924512 | -3.00447 | -49.5871 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f30d3b-94fb-3a17-8383-4fcc50010fd9 | -3.00114 | -49.58658 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 790ef030-7c07-3dee-86ff-2bba950ed46d | -3.0006 | -49.59005 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b7dcdf5-a223-371e-bc77-7047e200eec6 | -2.96718 | -49.5422 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d61cfa9-c4cb-3173-aa4b-8e0e04d9d7b9 | -2.96664 | -49.54567 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0129e2ba-dbe4-390c-88ed-139e6bb614ff | -2.891 | -49.46947 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eca79b9-7957-3da8-a047-523c33aa9bbe | -2.87597 | -49.2598 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40c13c0b-b50b-33e6-b0b7-f93e0e2c8e92 | -2.86873 | -49.26227 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05281309-bac2-36b3-8055-f438d974837f | -2.86184 | -49.37218 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ba9c5c7-8a5d-3156-abb1-bde781285068 | -2.86101 | -49.46482 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9098f78-7d84-3fd4-8f9d-8a3949e5a634 | -2.86095 | -49.44342 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aa47cc3-7269-3172-a216-a62960b9e9a4 | -2.8604 | -49.44691 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0215555d-b53a-368a-9282-1158cb903f9f | -2.85707 | -49.44639 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4ff6649c-8786-3057-8816-3dac8e351260 | -2.85652 | -49.44987 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0cd30c5d-990d-347a-bdbe-6f36956ee7c4 | -2.85515 | -49.54578 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a617719d-91b3-3a6c-b3cb-2497f958a467 | -2.85182 | -49.54527 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55cb1335-0d48-33ce-835f-7f34735acd1b | -2.84916 | -49.26295 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0f4dce8-9d75-3a1c-a094-1901773b168a | -2.84582 | -49.26243 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e298e701-3d04-34f6-9f0a-4ec001bc57b0 | -2.83858 | -49.26489 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84b87014-fa73-3548-b4a2-7a4646cefa9b | -2.83137 | -49.74078 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 996a87b6-b5ab-3c06-ae88-a49f6be03ec5 | -2.8103 | -49.31423 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9e85726-1324-3c36-a3b7-64ab04a19473 | -2.80975 | -49.31773 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5075e317-3373-3276-8238-64b239a1342d | -2.80235 | -49.83889 | 2024-10-30 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a3e2886-65f0-3ba1-8296-6a3fa1999b59 | -2.78737 | -49.48196 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58917d7d-1388-3cb1-95b0-a2d90bc091f2 | -2.78071 | -49.48093 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README60.md)
