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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e0a7368-790b-38fc-be4f-ff191cc8dfe4 | -8.0606 | -49.68395 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 94bc3160-315e-3071-85ed-eff8ae95405c | -9.2035 | -59.47701 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 283b1a3f-725d-3b9a-b243-8c077781b279 | -8.87991 | -62.4405 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc01974f-cfab-3d61-b993-8c518ca882ec | -8.12805 | -47.12744 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fbe8e7b-6eed-3a8c-86b8-ef33f865be14 | -9.25301 | -59.64125 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b2cf183-f7de-3789-bd04-25453d183b47 | -13.467 | -46.87687 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49353fbe-16a4-3cdd-bb30-7f08fbe2a985 | -13.51243 | -46.91205 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ae84654-861b-3015-abfa-8151d6bd05f7 | -9.17255 | -60.83357 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a37b8de8-9aec-3b5e-b861-0467ace44b85 | -8.91493 | -62.43564 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4dae53b1-e6fe-3c82-8a0d-b411487bf8e2 | -8.87114 | -62.45047 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 910d1ea1-2536-3d48-a66c-fb9245d69c9b | -9.20286 | -59.48054 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7db22ed3-fdfe-3592-a018-db92e72d40b6 | -9.23709 | -60.92594 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca6eb75d-586a-323e-b49f-e761f4e502d6 | -9.15874 | -59.47561 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3d22949-8691-3a87-8e1b-3fc718215327 | -8.22826 | -61.3864 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 520c18ce-26ff-3c76-b69c-948b4f4e10c8 | -11.4681 | -55.47667 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b45b8031-66b1-3250-94ee-2a3b5b8c42e5 | -9.19846 | -59.50871 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31f25dca-9056-3341-9064-74da5deb944c | -8.10961 | -47.1334 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5bfcb0c8-968b-32b0-b08a-a9cfb7fe537c | -7.66035 | -63.53089 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e958964d-1582-3224-8456-3fcbf5466898 | -9.16897 | -59.48122 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b729f37f-8b67-3231-b3b5-953046293104 | -9.17699 | -59.46815 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec4433aa-d9de-3fed-bea9-256d80e4da5e | -9.19974 | -60.917 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48de27a4-eaa3-3308-b3e5-159468fa2e2e | -8.87399 | -62.44624 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 665bd414-10cb-367e-8d00-4cc38370c110 | -8.89959 | -62.44448 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72433cfc-7856-3841-876f-fd06d4e1c7a0 | -12.95726 | -46.33004 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc3dd458-b17d-33ef-a109-f4228fd6f71c | -10.58724 | -47.14469 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e212920f-8b0b-388a-b897-56f290560ce6 | -9.16806 | -59.45559 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f47fa4d2-a25d-34ec-adcf-c8a26383389f | -9.16378 | -60.83132 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6915989-cbe3-30bd-b3c5-38dc24b2d976 | -11.63864 | -46.21857 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06ca187b-f8c6-3b86-b63a-f8c413b687ea | -9.48925 | -58.93612 | 2025-08-25 04:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5087998-a0fb-33a5-8193-b10173e68411 | -9.15702 | -59.51559 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1de05173-2087-3d2f-87f9-df7393074a32 | -13.49295 | -46.88539 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d9dad0a-7114-379b-8c57-9c8115c0ec8f | -8.06225 | -47.30236 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a131bc47-1083-3598-8f5b-ed55197a9cc6 | -9.15719 | -59.45357 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a940ceae-2ce5-34c0-b966-1c22c129918c | -9.5246 | -60.52106 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eee3031c-95c1-31fd-aab6-55240c9ae654 | -9.17891 | -59.61214 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f184282-3263-3c5a-92c3-5dcf3c7053d5 | -11.18254 | -55.01973 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c2459b6-3619-39cf-b367-2b3ac1e10406 | -13.40015 | -47.5379 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9514beee-d473-3cb9-b783-b3462c577045 | -9.69137 | -48.34165 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f4ff340-f500-325c-b7cf-db1f53069a94 | -13.43485 | -47.02301 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69bb29cc-d90a-363e-8314-24b502386f6f | -9.20222 | -59.48409 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7d5443d-2e4c-3780-9deb-8b01f0fd104d | -9.95834 | -60.19028 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9ce7361-ac76-3b4d-81e0-28ca4d82d948 | -8.6137 | -62.60383 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 462b99ce-96c3-367a-af4d-565084eadeff | -9.2031 | -59.48415 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34011b6a-fbd9-3187-802b-26b7304ee93d | -8.89633 | -62.4262 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c414d9c-e075-3b09-97c0-66f4806d9164 | -12.75236 | -44.41553 | 2025-08-25 04:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f7f5b7c-053e-31ed-9588-177e24ba5771 | -8.89303 | -62.44315 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 957c85b9-0f8e-3b0d-a74a-59451fb7fd5b | -13.39356 | -51.80628 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3839a9c1-a776-33bf-8592-1176cf9d603a | -8.77018 | -49.97255 | 2025-08-25 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51bbfd80-1d69-3497-a09b-84c15fbc16a9 | -9.40134 | -48.25658 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3aea5c8-d994-3ade-9349-f5f1d77988c7 | -9.95978 | -60.18274 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58c2714b-4613-3507-8e5e-f738c16caf55 | -13.1483 | -53.74022 | 2025-08-25 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ecf6573-b315-3d44-8586-4a7ba0c47439 | -13.46496 | -47.00199 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ba345b26-65fb-3267-b175-8b962f24c53a | -11.27661 | -44.98923 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70040ef1-d9bf-3670-a3a3-022e229b4082 | -10.40235 | -57.68336 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a85a515-b86b-3bcf-a98b-75cef84f9868 | -12.74585 | -48.12942 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07235b51-c432-37ae-afb2-039c487b3f6b | -10.2542 | -59.1092 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07fe9b50-d5c0-3997-ab2d-10be1d64a94d | -13.39956 | -47.54197 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54a8b728-f7a0-3b69-b453-bc2da3808938 | -9.20021 | -59.43999 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63c817cf-d600-318f-96f4-175d1348133a | -8.89849 | -62.45013 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ccc3c09-cbf6-3ffe-bf15-7bb9fbc23b5a | -9.20522 | -60.79118 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 231e303c-97b9-3989-82c7-c5ec77b579b2 | -8.12847 | -47.12808 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62aad9c9-7884-3084-8172-1edf98115a59 | -8.75687 | -49.94896 | 2025-08-25 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5959a81f-7ea8-3c6f-a83d-0fa5301dbe0a | -13.61736 | -48.16872 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b70d64c1-65ee-39a8-a2e3-d2db612ea596 | -8.10555 | -62.87406 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25ea4f82-5120-3443-8487-1bda7243a51a | -10.60791 | -54.8888 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0cbc0de-d909-342a-a9c3-b9260cc7e898 | -13.42817 | -46.90911 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 005d6374-ee4d-343b-9282-8462b6111275 | -8.80508 | -48.50637 | 2025-08-25 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cff7190-5a2d-3cac-8aa5-72fcca338137 | -8.12721 | -62.87181 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 977bb813-84e6-30c3-9cca-2186e14bc9b4 | -8.89193 | -62.44879 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4eefc590-2d9f-3294-b3c4-6fb2ab8bac44 | -12.74528 | -48.13335 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce097418-c3f1-3782-a692-b935ff25f343 | -8.86969 | -62.46899 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f04cb68a-31eb-3bda-967f-9e24f966b636 | -6.34212 | -58.18912 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1215c495-c0d5-3e97-a749-84e7c9ebc751 | -8.11743 | -62.88205 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86d9f9c4-88aa-3be0-a930-214205b4ddd8 | -9.15067 | -59.48888 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f195a8c-8f08-373b-bd6c-5b9a187f01b1 | -9.19358 | -59.47494 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f16aa0c-bd46-3834-8d6a-2fc27a3daedd | -10.83449 | -47.51142 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3df37732-8252-33b1-b442-412fcd91cf38 | -13.43194 | -46.90981 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0b34e29-5d1d-3527-9774-b47c712397eb | -6.83306 | -58.95504 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 835da182-454c-3a0f-8336-8c8abe15df84 | -8.87336 | -62.43918 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a75b0dc1-9046-3e67-bfe4-247cbed5453d | -9.1511 | -59.45605 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e587b33-8877-3f7d-b2dc-e3f95e6d9af0 | -8.07825 | -61.54206 | 2025-08-25 04:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 407aaf21-bb6a-3a40-9a21-9518345063bb | -9.13816 | -60.77147 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e9750d0-cfdf-3799-b586-47d3e7050b03 | -11.592 | -46.36452 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c94d7723-66ed-31ba-98a6-05f06c633021 | -9.58039 | -55.36845 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 820f2c08-70dc-395b-b8b7-df3958efa5ea | -9.80581 | -61.20967 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84f1d598-604c-32a8-85bc-b95d94d1c9c9 | -11.09657 | -44.76882 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce999ba8-6233-3957-aeb5-9c48ecb3cd09 | -9.2051 | -59.49924 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1e98e83-c244-317b-883a-96742ce5ff66 | -8.06942 | -49.64965 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e42dcda-7bf9-3be9-9d3b-8f3adcb6ed32 | -13.44197 | -46.92069 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c085d75-70fa-3a24-8d73-33bf2035d4ce | -8.89629 | -62.46141 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3881f840-72a1-3029-a622-2adfaff54e56 | -10.46515 | -48.32002 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 914db5f8-a3de-3d6e-acc5-9311f4fc392a | -11.60124 | -46.34478 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 491c5465-e9f9-3a90-8318-bcf53197fde5 | -13.4425 | -46.89035 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f70d563-d3f9-365f-8514-8213fd9e6359 | -11.2662 | -44.9726 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e5a305-4547-33af-9148-50f4394f4d9a | -12.50066 | -53.8314 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0399ebe-b715-319f-b339-d656a9b7197b | -9.96612 | -60.18 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ff9f291a-02bb-318d-8078-ba8ec20c5d5e | -11.6062 | -46.36499 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bf7912d-b84e-339d-b1c1-1b894455cfb6 | -9.1594 | -59.47206 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 324ec8ea-1013-39b7-8819-73fc023d9164 | -11.86749 | -45.11985 | 2025-08-25 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4adafef6-6e50-3a92-b757-ee753d367b8b | -9.21831 | -59.70582 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README52.md)
