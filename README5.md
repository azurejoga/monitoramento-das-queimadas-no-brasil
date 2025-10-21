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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3444d187-afa2-3c37-85a9-241cccbaf8dc | -4.4971 | -46.4618 | 2025-10-21 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| ac889888-7aee-3df1-9143-e160d52aaaf3 | -4.6463 | -46.4095 | 2025-10-21 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2b0dda02-498b-378c-9562-5789f9c9c2fb | -3.4783 | -45.8203 | 2025-10-21 01:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4b1032e4-19a6-3df7-8788-b3f4b7d184f0 | 1.7119 | -55.7051 | 2025-10-21 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| afb4dd58-c392-3342-bda3-e7420e68f559 | -6.1935 | -42.5022 | 2025-10-21 01:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 8df35892-e850-3c35-aea4-e819c9feca35 | -9.0036 | -65.9412 | 2025-10-21 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 14d8b698-d633-3bcf-b2c3-fae74cc266c7 | -4.4969 | -46.4839 | 2025-10-21 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 4d38ca13-fd04-37d0-98ff-b390592cbdb6 | -8.9851 | -65.9232 | 2025-10-21 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 28dfa6e7-e15c-388c-ad68-05b02742d229 | 1.6936 | -55.7251 | 2025-10-21 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0f82e9f0-904c-3f41-be0b-0f53f54c79d9 | -9.0222 | -65.922 | 2025-10-21 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 09c4c0d2-74bf-3fc3-bba1-11fb224603ec | -6.1932 | -42.5259 | 2025-10-21 01:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 645a8819-3345-36c1-a348-0501ebe25e38 | -4.4783 | -46.4849 | 2025-10-21 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 9b7033e7-f097-319a-a368-7c800d316608 | -9.0036 | -65.9226 | 2025-10-21 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 8deacaa9-ed9a-3b71-8e07-9774212120fe | -3.4968 | -45.8195 | 2025-10-21 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 302.1 |
| 80d8d788-2b53-3dbe-9abb-511dd98f850f | 1.7303 | -55.6851 | 2025-10-21 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a2691e61-44f7-3469-b158-23604f88baf4 | -3.497 | -45.7971 | 2025-10-21 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ee594339-045d-36af-a4c1-e7784b6f6f99 | 1.7119 | -55.7248 | 2025-10-21 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 52489c7e-8f5a-36bc-89bd-3dd6d3514c8f | 1.7119 | -55.7248 | 2025-10-21 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 32333add-e586-36cf-be1d-c404d545a608 | -3.4968 | -45.8195 | 2025-10-21 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 306.8 |
| 22ba524d-4bec-343b-ad12-a796b75d8d61 | 1.7302 | -55.7049 | 2025-10-21 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 98179f3f-af96-3b2d-8dd0-acf7b1a56af0 | -3.5154 | -45.8187 | 2025-10-21 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 238.1 |
| cf1d235c-c35e-39e7-aac7-b310e83f7986 | -9.0036 | -65.9412 | 2025-10-21 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8ecffe58-7248-3135-8276-538f4b9370ac | -4.4971 | -46.4618 | 2025-10-21 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6e808832-9555-3fe0-8488-78ad6d35ee21 | -4.4969 | -46.4839 | 2025-10-21 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c53da854-756a-34ad-b70d-12e6056fc306 | -3.4967 | -45.8418 | 2025-10-21 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 177.9 |
| a13ec2e4-1291-38f9-8f16-4f9e0a9284ee | -4.6463 | -46.4095 | 2025-10-21 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d79d482a-fb9a-3323-80cf-b58a039c6534 | -8.9851 | -65.9232 | 2025-10-21 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eb071a9d-98df-3b82-bc85-5e16bf029b37 | -3.4783 | -45.8203 | 2025-10-21 02:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 1978c21b-030c-3cb6-98f1-7a7c3ba284f9 | -3.5153 | -45.8411 | 2025-10-21 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 3fc777d3-5f8c-3299-a1b5-1cb40e5d4444 | -3.497 | -45.7971 | 2025-10-21 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 33f79748-9097-3951-be9d-7dd037fa89d6 | -9.0036 | -65.9226 | 2025-10-21 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 53eee1c3-5ec9-35c6-88b9-ee5490fbc200 | -17.6852 | -52.2398 | 2025-10-21 02:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 6435690d-e1ac-37bb-b19c-f7d39697a147 | 1.7303 | -55.6851 | 2025-10-21 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 842e1584-c447-3f12-9111-8fe1627112d6 | -4.4785 | -46.4628 | 2025-10-21 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c7db235f-0219-3aff-98b0-b8f15e6fb95f | 1.7119 | -55.7051 | 2025-10-21 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7f3578d1-4934-323f-9d98-928f98c50a2c | 1.6936 | -55.7251 | 2025-10-21 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fa0ffff6-d35c-3888-aec5-64037d2c203c | -4.4783 | -46.4849 | 2025-10-21 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 42275982-c501-3f56-86fe-a1ea60472278 | -4.4971 | -46.4618 | 2025-10-21 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 245750a8-39cf-3139-9e8b-8abb7ef70244 | -8.9851 | -65.9232 | 2025-10-21 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a212701a-d365-33f2-9ae3-76ad27cdcfb4 | 1.7303 | -55.6851 | 2025-10-21 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c668d0fe-4d89-3ba3-850e-1b29c18d61f4 | -3.4968 | -45.8195 | 2025-10-21 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 476.0 |
| d8afe3fa-5a7c-36b2-b32b-7a1c057cf8e4 | -9.0036 | -65.9412 | 2025-10-21 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 09404916-4945-3bd8-98cc-b31765bef821 | -4.4785 | -46.4628 | 2025-10-21 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 06bcfd2d-d69c-3745-97c7-5e6c60ffbf4a | 1.7119 | -55.7051 | 2025-10-21 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ba070d11-b77a-3aa5-b8d6-3747eaab43dd | -3.4967 | -45.8418 | 2025-10-21 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 211.7 |
| 11121b47-f23d-3f60-b7d0-61c88544ded3 | 1.7119 | -55.7248 | 2025-10-21 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1c33ab1f-60ed-3e85-8502-8863ee5c7995 | -9.0037 | -65.904 | 2025-10-21 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 2dc2c1a1-a11e-32a1-8053-fe412ccfbf3e | -4.4969 | -46.4839 | 2025-10-21 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 6f17e094-f7d5-385f-b163-17d6e1cb96e3 | -3.5154 | -45.8187 | 2025-10-21 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 37909c38-0692-3956-8353-094a2910a844 | -4.6463 | -46.4095 | 2025-10-21 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 0a4f1e85-6253-374b-a4f3-32b14ea589d1 | -9.0036 | -65.9226 | 2025-10-21 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| f6341f89-fcce-323a-9ae1-d6e4df9a5d4b | -3.5153 | -45.8411 | 2025-10-21 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 6cc6d65a-2702-3bcd-8dfb-547d6a1b52bf | -9.0222 | -65.922 | 2025-10-21 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c6e25332-b386-36f2-aac3-03d1c2a21b14 | 1.7302 | -55.7049 | 2025-10-21 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 99a9d34c-55b0-3bdb-bb3b-4e67f49f0a6d | -4.4783 | -46.4849 | 2025-10-21 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ba00497e-c262-3301-a9d6-a660e705eeec | -4.4783 | -46.4849 | 2025-10-21 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7999eadf-c5fa-3fd5-ab22-35ebcc14ef4a | -9.0222 | -65.922 | 2025-10-21 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 48a135d2-1a33-39c7-8264-856273ac20d3 | -3.4968 | -45.8195 | 2025-10-21 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 315.4 |
| c5c82b83-679e-3543-bd97-9e61f9a31b70 | 1.7119 | -55.7248 | 2025-10-21 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| bea14539-cbf4-3770-af38-6a85845be574 | -4.4971 | -46.4618 | 2025-10-21 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 85d74b03-88a9-3d27-808f-950c0d68cea9 | -9.0036 | -65.9412 | 2025-10-21 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 807689e1-4bef-3077-b0b6-2f431df30be5 | 1.6936 | -55.7251 | 2025-10-21 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ba38530c-c561-3122-81b9-14edc41b2877 | -9.0036 | -65.9226 | 2025-10-21 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| d319f1ac-5517-3823-931a-80ca34440ee9 | -3.4783 | -45.8203 | 2025-10-21 02:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bb2af0c7-4c08-3467-b93d-c7972c15fe63 | 1.7119 | -55.7051 | 2025-10-21 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 82f75b1b-e336-34d0-a415-5c9ddd54544d | -4.4785 | -46.4628 | 2025-10-21 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 80838127-3958-322d-90b3-3b016c2002b3 | -3.4967 | -45.8418 | 2025-10-21 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 38813d5c-2e7a-34dc-97c6-c1dd010f2fcb | -3.5153 | -45.8411 | 2025-10-21 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 7df09fb5-80f3-34c4-b1fa-06238a30e587 | 1.7302 | -55.7246 | 2025-10-21 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1afb02be-3285-30f3-b9b6-4dfcbb6638fa | -3.5154 | -45.8187 | 2025-10-21 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 217.6 |
| 41901cd9-df90-3332-a4e2-f262058cef7f | -10.9393 | -50.3407 | 2025-10-21 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 4e1ee7f1-37fc-313d-84a4-1503ab77b7cb | -8.9851 | -65.9232 | 2025-10-21 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a39e24c3-9375-3a18-bf95-d79b719a1e41 | -4.6463 | -46.4095 | 2025-10-21 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b79c21c4-11c7-30fa-ba0a-e8d555e97590 | -4.4969 | -46.4839 | 2025-10-21 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| dbc54b50-d3d9-33c8-83c4-8ab1e5c7f64b | -9.0037 | -65.904 | 2025-10-21 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bb66a1e9-da31-371b-b5d3-2363a9c68201 | 1.7302 | -55.7049 | 2025-10-21 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e3eeafe2-dc8c-32ef-8857-859edb17c492 | -3.497 | -45.7971 | 2025-10-21 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e41bac2b-f032-3cde-8ade-007d13d0b0c8 | 1.7303 | -55.6851 | 2025-10-21 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a42af537-362f-3808-b243-91e04dce65d6 | -4.4969 | -46.4839 | 2025-10-21 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| e0f4e5a9-b65d-3324-8662-fea7d15af24a | -3.4968 | -45.8195 | 2025-10-21 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 280.6 |
| 1f2ff33b-8192-36f4-9638-3562b0822972 | -3.497 | -45.7971 | 2025-10-21 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d5632316-5598-336b-ab24-fea35111864f | -17.6847 | -52.2615 | 2025-10-21 02:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 096e9abb-d931-3b0d-af85-f7592a033bf3 | -3.4967 | -45.8418 | 2025-10-21 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 182.8 |
| b3a822e8-2ec2-33b7-b71e-678db952353e | -9.0036 | -65.9412 | 2025-10-21 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4aa239fd-482b-3f57-8453-02abd0025306 | -9.0036 | -65.9226 | 2025-10-21 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| e3d715b5-73ec-3395-84ac-b8c249a281ea | -4.4785 | -46.4628 | 2025-10-21 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d4e1d1c4-715d-307f-a03e-8ede43c22eb2 | -3.5153 | -45.8411 | 2025-10-21 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 7c242a06-d593-3757-94f4-5e270751d4d4 | 1.7119 | -55.7248 | 2025-10-21 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e7a7297e-21f5-3775-931c-3c1b0098f915 | -3.5154 | -45.8187 | 2025-10-21 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 193.7 |
| ddb0cf7d-6983-389b-a27f-97ca141793e6 | -8.9851 | -65.9232 | 2025-10-21 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8c3b35b8-b9af-349e-9764-4a76e6f8bafa | 1.7486 | -55.6849 | 2025-10-21 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a2c55a38-e875-3333-b32f-11274188703b | -9.0036 | -65.9226 | 2025-10-21 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 80994eba-d93a-3292-b217-1c13386ebbc1 | -10.9396 | -50.3193 | 2025-10-21 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7e6b6482-e262-3bc6-93cc-295f85c45f25 | 1.7486 | -55.6849 | 2025-10-21 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c7bb8ae3-54d7-38cc-927e-5c0a66e05ec3 | -3.5154 | -45.8187 | 2025-10-21 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 223.7 |
| a7531681-e089-32d3-8f0a-647a81db98d2 | -3.4967 | -45.8418 | 2025-10-21 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 147.8 |
| abf53e26-fd9d-3179-8261-00da39e27b72 | -17.6847 | -52.2615 | 2025-10-21 02:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e4f75e0c-9983-339b-8a41-9980829d10a7 | -9.0036 | -65.9412 | 2025-10-21 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 262bde90-aa99-332e-a7e4-53448936f81a | -3.4968 | -45.8195 | 2025-10-21 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 275.1 |
| 63501c66-7071-3c98-a3a2-24f5d32d7b4c | -9.0222 | -65.922 | 2025-10-21 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |


[Clique aqui para ver as próximas entradas](README6.md)
