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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ef39878-694e-3942-aca2-5a4fff8375b0 | -12.61975 | -49.071 | 2025-08-03 03:38:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 65f7d8a6-b482-3d63-8b90-410bdc2ffee2 | -13.07771 | -47.43689 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a40168e6-bb21-3550-94f2-a92bfc212468 | -16.83038 | -42.8682 | 2025-08-03 03:38:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba88f75c-b10f-3da6-9504-8dc9655126e0 | -14.17494 | -45.45426 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4641215e-fdd6-3b2c-94f3-8f372f14c12d | -12.66562 | -44.49262 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35f9fd18-0ebf-346c-8a46-7216d9ca444b | -15.59461 | -48.51023 | 2025-08-03 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c22f258-23bf-3227-b91d-ffc3ae0bf107 | -12.66429 | -44.52773 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07ce7649-fe31-3c56-9fde-ce9e7a609a04 | -14.17417 | -45.4571 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91f6aa4e-3b7c-3e0c-96f9-31cc4bf922cb | -14.16216 | -45.43235 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 083cdc2d-0f16-3f26-b7f4-58bd643cf6be | -12.63843 | -44.5189 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d78a21e-aa60-30af-9114-b3c8555db114 | -12.43033 | -47.04065 | 2025-08-03 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0b3d75a-d859-3862-b200-41411868606f | -12.6402 | -44.4913 | 2025-08-03 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e43bb69a-f201-325e-b969-e950f8631cff | -8.0126 | -43.1749 | 2025-08-03 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.1 |
| 729bb358-b4b2-3ca5-857b-46cec510eacd | -7.994 | -43.1534 | 2025-08-03 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 1e886471-752d-3c4a-a985-2966ba2665f0 | -7.9934 | -43.2005 | 2025-08-03 03:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 374a63dd-27dc-3aaa-814c-6cdaa9bdc660 | -8.0129 | -43.1513 | 2025-08-03 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 196.2 |
| 2fe4802e-cdd8-3f09-a072-b803bec9ab1e | -6.6559 | -59.1174 | 2025-08-03 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| bd703763-8864-3026-ab76-03d57c6b955d | -7.9937 | -43.1769 | 2025-08-03 03:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 175.2 |
| 9e732ebc-8e28-3d56-948d-452d197ab9e3 | -12.6595 | -44.4882 | 2025-08-03 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| df89fe73-0f7b-3a8e-8c01-a157272506f7 | -20.79109 | -41.23509 | 2025-08-03 03:40:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 56c80401-ed01-30bb-92f9-3db1afa1bfd1 | -20.6897 | -42.6066 | 2025-08-03 03:40:00 | NOAA-20 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dae314ee-5a41-3629-9307-aee4a8188193 | -22.72429 | -44.74212 | 2025-08-03 03:40:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 64544710-ba4f-30e3-8667-ec68c1de65c4 | -20.32812 | -46.61575 | 2025-08-03 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a9b7bf3-d49b-3be9-81fb-a02129a439ed | -21.03477 | -40.84944 | 2025-08-03 03:40:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 17f73c14-309f-3ff9-964c-cc859113819d | -22.72752 | -46.30601 | 2025-08-03 03:40:00 | NOAA-20 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d543cf14-e68b-378f-9e78-37b5abc64f93 | -20.06994 | -43.74964 | 2025-08-03 03:40:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 44dcf295-95df-3026-9c50-6291506b98c7 | -22.01213 | -47.35425 | 2025-08-03 03:40:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c95246c3-1378-3d08-8fac-af75ae4262db | -20.08067 | -43.9979 | 2025-08-03 03:40:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7a11d0e6-39e7-3a33-b709-b2be4035af5a | -26.5484 | -48.85564 | 2025-08-03 03:40:00 | NOAA-20 | GUARAMIRIM | SANTA CATARINA | Brasil | 4206504 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7e582d19-ea30-34ec-ad9d-4c4e14d6895b | -20.06671 | -43.74286 | 2025-08-03 03:40:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28f17a94-2ee8-3426-87d1-dafe40e9e72e | -20.01807 | -46.43347 | 2025-08-03 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 086f50fe-f6af-3821-8e92-1d0787bfc733 | -21.36189 | -44.90054 | 2025-08-03 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dbdd83ee-63ed-3af7-9f35-0b08f4f91088 | -22.73561 | -42.95797 | 2025-08-03 03:40:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3690349b-ddce-34b4-b3c4-4ae4811ec2c2 | -21.36084 | -44.89736 | 2025-08-03 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8f31e474-0fb9-39c7-8f82-fcdc6e805094 | -20.71652 | -47.29299 | 2025-08-03 03:40:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2b8ffe0-f5b5-36dd-9be3-2795c65a48d8 | -20.06684 | -43.74627 | 2025-08-03 03:40:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fa328174-dd64-3331-b851-b07da03482c4 | -20.07102 | -43.74425 | 2025-08-03 03:40:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d2ea58ba-6e99-33c4-83d2-165653ec2502 | -24.23138 | -48.46691 | 2025-08-03 03:40:00 | NOAA-20 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e24a9c79-1e22-3376-bd84-f20d8c42a82f | -22.72806 | -44.74641 | 2025-08-03 03:40:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 178a1417-9c20-3ce9-9d3b-b84a55fa1e02 | -20.06568 | -43.74801 | 2025-08-03 03:40:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8182e7e3-69fb-392a-97e7-0ce62ef042c9 | -22.78179 | -43.04325 | 2025-08-03 03:40:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f4ecad5-333d-3b0c-887f-810d49a24bf2 | -23.65353 | -48.04793 | 2025-08-03 03:40:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db4dd11d-11f4-380a-bdbd-a380f4e283dc | -27.15716 | -51.21222 | 2025-08-03 03:42:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b19f1c13-277c-383c-86ca-ae5de1bbfbba | -7.994 | -43.1534 | 2025-08-03 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 3be720ad-76fe-36ca-8404-7bbc1a3f7a7b | -7.9937 | -43.1769 | 2025-08-03 03:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 201.9 |
| a9fc5172-00f5-3908-8764-d4c7176d46cb | -7.9934 | -43.2005 | 2025-08-03 03:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 58a422bf-7b35-3e65-9b7a-00238bf16f74 | -12.6595 | -44.4882 | 2025-08-03 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ca62058c-684c-3a6f-9c59-449e6b12504d | -8.0129 | -43.1513 | 2025-08-03 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.0 |
| 6b36edfb-91ca-3041-8e2b-b965d6dc869f | -12.6402 | -44.4913 | 2025-08-03 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 33d78f37-28ff-3032-a3e2-07b806c61204 | -8.0126 | -43.1749 | 2025-08-03 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.7 |
| 2d8692fa-550b-3f33-884c-32875602a017 | -8.0132 | -43.1278 | 2025-08-03 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 02d343f0-a2d1-3f87-8fea-119fbf789b64 | -7.994 | -43.1534 | 2025-08-03 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 1785d127-8e10-3ea4-bb9d-884a02af12bd | -12.6402 | -44.4913 | 2025-08-03 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 516d112a-4e2c-30b3-bbcb-7acef876f780 | -12.6591 | -44.5117 | 2025-08-03 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 54821e70-063d-3f3f-9e14-6f997bd70aa1 | -7.9937 | -43.1769 | 2025-08-03 04:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 299.9 |
| 3c6079f0-7454-3876-a787-b00705644245 | -7.9934 | -43.2005 | 2025-08-03 04:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 3cb4ab44-c8b8-3df7-bd95-4c27e57030a0 | -12.6595 | -44.4882 | 2025-08-03 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 455ad2af-6c61-36ad-a8a2-e2a1cb6cc59a | -8.0129 | -43.1513 | 2025-08-03 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 274.9 |
| 8833ff5e-25ce-31bc-8979-7586b1347a14 | -8.0123 | -43.1984 | 2025-08-03 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 6f1e3986-f129-3700-ae93-23e82c557d0e | -8.0126 | -43.1749 | 2025-08-03 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.1 |
| 8f8a93c6-30dd-3e71-979a-037966ea3b58 | -7.994 | -43.1534 | 2025-08-03 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| 4e1f79c9-4140-362a-8d34-d6bb55e599bf | -6.656 | -59.0981 | 2025-08-03 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8b33d94f-5f23-33fa-a560-1cfbb96fdd8b | -8.0126 | -43.1749 | 2025-08-03 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 267.5 |
| 550ad860-1700-3371-895d-bcc66ee7b428 | -8.0132 | -43.1278 | 2025-08-03 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 76a6a9af-f883-3ea9-911b-c77afe5ed1f3 | -12.6402 | -44.4913 | 2025-08-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d22a2f74-986f-3a09-9d71-f8201d12363d | -6.6559 | -59.1174 | 2025-08-03 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f9bbbffb-a537-3e99-9068-929eda2d05d2 | -12.6591 | -44.5117 | 2025-08-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 6f53da2f-0824-32d4-ba8e-624a590efc33 | -7.9937 | -43.1769 | 2025-08-03 04:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 217.3 |
| 0398e741-f9f1-38f5-86ba-78f4a13b361a | -12.6595 | -44.4882 | 2025-08-03 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6a386d3a-caf5-381e-9bad-e2e0fd846781 | -8.0129 | -43.1513 | 2025-08-03 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 422.4 |
| de604cb5-95fa-3662-94d6-63a006c43b55 | -7.9934 | -43.2005 | 2025-08-03 04:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 40fd8c0f-96e0-3d43-9a99-4592a484f7c4 | -12.6402 | -44.4913 | 2025-08-03 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 21d7bedd-c4cf-323d-92e9-d7583e647b13 | -4.5684 | -44.2036 | 2025-08-03 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2f949143-788c-3bbf-96f8-0392808b2415 | -12.6595 | -44.4882 | 2025-08-03 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e4fba42b-2d80-3572-90a9-620bd7eff0df | -6.6144 | -59.9656 | 2025-08-03 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 15edcb61-390f-39a1-8556-eefc118246ba | -7.9934 | -43.2005 | 2025-08-03 04:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 8ef940d6-e36f-3c31-a41d-5d66ac845df3 | -2.9231 | -48.67385 | 2025-08-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f1b0340-6f5f-3e0f-a947-ea0af20b61fa | -7.1122 | -43.48012 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 674a9925-1d84-3121-accd-1606ca9513a6 | -7.59888 | -44.9887 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c36b3499-886d-3a0f-ac6f-fbb71b0ff4e2 | -7.10054 | -44.96619 | 2025-08-03 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad38f70e-9ed3-3016-9584-22e55b2b4e28 | -6.67721 | -44.36365 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbbdba05-0d10-3558-be6e-9206eb53b187 | -4.85805 | -45.74647 | 2025-08-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e2a4a4-9ab9-33de-9a00-a5183f865ad4 | -7.01248 | -45.55803 | 2025-08-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 397a7817-92c6-3c47-b4e4-67a20f6681e3 | -2.65765 | -42.71741 | 2025-08-03 04:25:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72b222e9-41fb-35b1-bee9-82cc82115aed | -4.02964 | -48.05905 | 2025-08-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a663f79c-c5a1-359b-9d88-7962fcca1494 | -8.03156 | -43.11888 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6527c9ac-2079-3390-9f92-01989500b832 | -8.02983 | -43.11625 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4744b4f1-88e3-3d00-b3a9-409932590355 | -8.00579 | -43.17581 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 03206c62-fde0-35fc-98ec-d36d762a754f | -6.49923 | -42.81736 | 2025-08-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2105f4fb-a1b0-3a98-a6be-44b0f53f75ff | -8.00514 | -43.18023 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 58e75219-7dfe-325b-a9d2-162c4493dfa3 | -8.0322 | -43.11443 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 681d3d50-418c-3741-9a98-b8efe3799deb | -7.12697 | -44.37939 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03bfa413-c815-33da-90a1-2d62d7d117cf | -8.01911 | -43.13729 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f636fd5e-244c-3c19-b656-38de6af5fc85 | -8.00818 | -43.18516 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b485d9ab-79ac-3b5b-bc43-aa3af0e87309 | -8.03962 | -43.11557 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 7af96dc1-711c-3364-9649-9c3cda6dd9ab | -2.91114 | -54.15673 | 2025-08-03 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db571db0-a852-3d2f-8c2d-dd2bbfdbf2e2 | -7.11397 | -44.6741 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8838b2c4-b576-3c03-a06f-ab4604040ae0 | -8.01581 | -43.15935 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5795948e-c7e1-33a3-a967-586fb6a03a4d | -6.95746 | -44.5057 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd618ae2-3713-3271-973f-254508a3e59d | -7.00079 | -42.10231 | 2025-08-03 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |


[Clique aqui para ver as próximas entradas](README13.md)
