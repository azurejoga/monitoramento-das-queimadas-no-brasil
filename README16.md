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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c682bc9-2774-31b2-9e6a-63110d35af50 | -3.5231 | -62.7561 | 2024-12-01 01:18:00 | METOP-B | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91d3cf99-0caa-3371-a67b-1bb6a63383cd | -5.4333 | -60.179298 | 2024-12-01 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 332ad4cb-6825-3acb-a881-cf0520ef6085 | 3.2833 | -60.053799 | 2024-12-01 01:18:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| faf4a5c6-87fb-3c85-a99c-f74abd5dae00 | 0.7833 | -60.1096 | 2024-12-01 01:18:00 | METOP-B | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b13ca95e-25ec-3778-8fa0-dd9a5c462542 | -3.1316 | -54.535999 | 2024-12-01 01:18:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af1e62c-20fd-3f62-872d-225c7b3373d5 | -3.5117 | -62.751499 | 2024-12-01 01:18:00 | METOP-B | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 047875db-6786-3e0c-b3af-a1596187b1ab | -3.3009 | -53.8675 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459900b8-70f9-3fd0-9aa8-ee53f8d8262e | -2.1417 | -54.855999 | 2024-12-01 01:18:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc1e4305-7f18-3c44-91dc-371d730d291b | -3.4902 | -53.8027 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bea56e47-7ecf-3c82-90ab-1f4337c945c6 | -2.6433 | -51.836201 | 2024-12-01 01:18:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c94716a-7bc3-3783-94e2-ded5a064d919 | -1.26 | -54.539101 | 2024-12-01 01:18:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601fd780-d69f-3d39-8e6f-b9a6d4f3f065 | 2.7387 | -60.377499 | 2024-12-01 01:18:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 239f7144-6e71-3095-a5a0-10afeca986ca | -2.1456 | -54.872898 | 2024-12-01 01:18:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d92ff8d4-8903-3dd0-97ac-135a48de0ca5 | -3.6701 | -51.7864 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9be935-1449-3b47-81ee-a225916a04c4 | -5.4316 | -60.171799 | 2024-12-01 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f2d918d-f196-3c7d-8f5d-ab81c8a048db | 1.1623 | -55.9669 | 2024-12-01 01:18:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abdb01e2-af5f-3762-9d9f-3e014ca62fe1 | -3.6764 | -51.812401 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7488bdd6-9139-3220-b503-aa89d14a530a | -3.1178 | -54.521 | 2024-12-01 01:18:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83fd7c79-21dc-3e0b-b965-505a699a9d6c | -3.4568 | -50.241402 | 2024-12-01 01:18:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa62236c-d936-341a-a5ae-8125a02f848d | -3.1275 | -54.518799 | 2024-12-01 01:18:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60c9132c-cbd5-32a9-b972-8e0b24c1186b | -2.7966 | -53.0354 | 2024-12-01 01:18:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad7c79cf-c5a0-3829-90ec-f0d9a1f1b5d2 | -3.3237 | -53.361198 | 2024-12-01 01:18:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 837dd304-731f-3722-acd7-40a0a4d0523c | -2.9962 | -51.780399 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bccc563-0ec8-3f09-97f5-681e98dcb6a8 | -2.7393 | -51.727299 | 2024-12-01 01:18:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c96db794-5e8d-3e24-8b94-7e5711fbdced | -2.8063 | -53.0331 | 2024-12-01 01:18:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0129e24d-8fd0-3a9b-9bc2-f0c6526c26f5 | 3.2813 | -60.063 | 2024-12-01 01:18:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a819947e-9efb-3aea-8af1-179e93894b1b | -3.4472 | -50.243698 | 2024-12-01 01:18:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55976a48-cfa1-356b-848b-78009397312e | 0.6483 | -60.526199 | 2024-12-01 01:18:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68e0ba2b-6cf8-3383-8304-e80540de9076 | -3.3061 | -53.846199 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f3fb284-5b54-3b62-869e-5fc0d6c30b4f | -2.1359 | -54.875099 | 2024-12-01 01:18:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f748ab5d-c612-33a3-bf6c-0074e338a84d | 1.1756 | -55.952999 | 2024-12-01 01:18:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c94fb7df-f6d3-3736-aba2-299d5c43831e | -2.64 | -51.865398 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94249a20-c6f4-322f-81d1-dc8100980816 | -3.2964 | -53.848499 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa3e089b-2307-3b60-98f2-a49f4ae26060 | -2.132 | -54.8582 | 2024-12-01 01:18:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b21e2bc-c8cf-3d51-ab31-be2082d25394 | -3.4993 | -53.840698 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1825fa-e170-36cb-8da6-c47bc32e657c | -3.5344 | -62.7607 | 2024-12-01 01:18:00 | METOP-B | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cba1e6ab-3a94-3de2-ade8-7ed53959cb23 | -3.2508 | -53.613098 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58b491e4-96c9-3bb1-9075-243d67bcebbf | -2.6497 | -51.863098 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea71b33-1d82-305c-8bb9-0b0f6f486a4e | -3.1089 | -53.791401 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c33f085-db01-3db6-81c0-44eb7aa694de | -3.2075 | -54.164001 | 2024-12-01 01:18:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 205491b6-d599-39ef-8d12-adb41de3f469 | -3.6861 | -51.810101 | 2024-12-01 01:18:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efee5a8b-385d-35af-b157-541342f0ed8a | -2.6234 | -54.2043 | 2024-12-01 01:18:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4061ad3-4767-3e3b-869c-3bde506132f0 | -4.558 | -45.7008 | 2024-12-01 01:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 6d1835f9-1999-3df3-9e5c-2546c56fdefc | -6.9341 | -43.5634 | 2024-12-01 01:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d45153ba-cbe0-38de-a550-3f08cf068647 | -2.5504 | -45.608 | 2024-12-01 01:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 0ceeba01-3d46-36cf-8709-360b8f7c4f70 | -3.2057 | -53.1341 | 2024-12-01 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6f16635a-82c5-315f-a5ee-efc8ab3a3195 | -3.1456 | -54.5259 | 2024-12-01 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 47e6e3a9-e570-322c-99fe-43a853120d15 | -3.69 | -51.8101 | 2024-12-01 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 76bebb58-231f-399f-b6f0-ea048dc8ed2e | -4.8899 | -41.3143 | 2024-12-01 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| d254d126-322d-356c-a58a-aec760b254b9 | -4.556 | -43.3261 | 2024-12-01 01:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ccd2eee7-3fe5-344b-bdd4-432110778389 | -6.9346 | -43.5168 | 2024-12-01 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 253f4a61-67da-3838-bce1-34ed9f92daa5 | -1.6954 | -46.1426 | 2024-12-01 01:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 242.7 |
| e55c718d-5c7d-3181-b5f4-e7161800d80a | -2.8196 | -53.0629 | 2024-12-01 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 9ce8c4d8-0c00-3554-a2e6-6c7f9525bbf3 | -4.5392 | -45.7243 | 2024-12-01 01:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 20f69755-e482-3cbe-9ac4-8b761a4a205d | -1.6953 | -46.1648 | 2024-12-01 01:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 8f9581bb-3228-34fa-9070-06b5ca5aa084 | -2.6578 | -51.8811 | 2024-12-01 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b341ed90-9a22-3ae3-960b-7a702f09cc2e | -2.6579 | -51.8606 | 2024-12-01 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 56b3bb8f-b872-3594-b374-7cb2883aac30 | -6.9156 | -43.5418 | 2024-12-01 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 72d18329-8b0d-31da-bc1a-1a84ea2456cc | -4.5394 | -45.7019 | 2024-12-01 01:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 1ff1770b-c4c1-3b4b-bfb7-42167d57877b | -10.6674 | -44.4835 | 2024-12-01 01:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e1284a17-175e-3d75-8377-d9340f018633 | -3.2591 | -53.6186 | 2024-12-01 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 6233821e-9b6d-3fb3-a29d-4103ffd42261 | -3.4974 | -53.8339 | 2024-12-01 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| da3f780b-e636-32ee-8165-e379176d25e0 | -3.5158 | -53.8333 | 2024-12-01 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| ef14af3e-020f-3050-96a5-4ccd8507ebca | -4.5563 | -43.2795 | 2024-12-01 01:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c0b3d4ca-0862-3a51-836f-59c359d1bb5a | -3.259 | -53.6388 | 2024-12-01 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| bfdae29b-a06f-3c0e-b626-48a866d53835 | -1.7139 | -46.1422 | 2024-12-01 01:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 200.2 |
| ce372c87-d0dd-3751-a183-6dca6d88e534 | -3.2774 | -53.6383 | 2024-12-01 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| fea17338-0c36-3f8e-82a6-cbefc0f07671 | -4.5562 | -43.3028 | 2024-12-01 01:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 1196c82d-9569-3468-9a0d-30fa1d118991 | -6.9344 | -43.5401 | 2024-12-01 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 311.1 |
| 257362ec-199c-3c29-92b2-7653f4b27fc5 | -1.7139 | -46.1644 | 2024-12-01 01:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| a47c1be6-f776-39e2-9c84-ed4ceca1b090 | -4.5578 | -45.7232 | 2024-12-01 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 9593ea06-90f9-3ba9-9485-bf5dfaf2a21d | -2.7503 | -51.7553 | 2024-12-01 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c07d4716-b14d-316c-80ef-a02c215e6093 | -3.0081 | -51.7897 | 2024-12-01 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d8499ea5-d3ae-3b90-8ab9-eb973b7ed775 | -3.4755 | -50.2566 | 2024-12-01 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| fc786121-bd09-324b-bd63-ef68ae876f05 | -2.8197 | -53.0425 | 2024-12-01 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8c23778c-215d-36c5-8c29-410ee8f95d89 | -3.1273 | -54.5264 | 2024-12-01 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ca89e5c3-eba2-397f-a7fd-4ffc15de30fa | -4.5395 | -45.6794 | 2024-12-01 01:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 33b80e81-f129-3091-ac06-71dafe9c791c | -3.4754 | -50.2776 | 2024-12-01 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 21cb64d8-9413-3658-b868-f1b020309b61 | -3.9939 | -46.6636 | 2024-12-01 01:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 7a662965-8208-3ca8-b720-bba9e05be8d5 | -3.4974 | -53.8339 | 2024-12-01 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 2729f40e-ded8-3778-b672-cc48cee18c0a | -1.6953 | -46.1648 | 2024-12-01 01:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 1249a5f7-de78-3762-9b01-07b7a33420de | -2.8013 | -53.043 | 2024-12-01 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7e0cfabc-88a4-3b5b-bb0f-f560b251d679 | -4.5394 | -45.7019 | 2024-12-01 01:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 5994abcd-d39b-38fa-b02b-5a52a9d6fab5 | -6.9344 | -43.5401 | 2024-12-01 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 209.8 |
| cbf69fad-4ba2-3a2b-8977-ed9a2c27dd0d | -2.5504 | -45.6304 | 2024-12-01 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 22c73c2a-ba8a-396d-8294-807f7b357705 | -2.6578 | -51.8811 | 2024-12-01 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c1c20cd5-8640-3466-aafb-891aabbc9bfc | -3.994 | -46.6415 | 2024-12-01 01:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0824fb35-b719-3f07-a8c2-d54a9c5e99b5 | -1.7139 | -46.1644 | 2024-12-01 01:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 5ad976ae-2f7e-3791-b6f4-629c9c6db0d0 | -1.6954 | -46.1426 | 2024-12-01 01:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 3df80d74-7b71-32ca-ab68-05838bd21e74 | -3.0081 | -51.7897 | 2024-12-01 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2d1eb9b3-e5b2-3984-b10f-9ffa03f58a40 | -3.69 | -51.8101 | 2024-12-01 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 55dd5b4d-9f8b-39c6-802e-5d2c23e71d8c | -4.5562 | -43.3028 | 2024-12-01 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 193.0 |
| c8a49a1c-d2cc-3f6d-84f5-171d5fe01ac4 | -2.5504 | -45.608 | 2024-12-01 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 231.4 |
| 026751b7-aa27-3bee-ad64-0e5916823f45 | -3.4754 | -50.2776 | 2024-12-01 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b9b468e3-134d-3ff0-abac-29704c545096 | -3.2591 | -53.6186 | 2024-12-01 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| fbd5c5f1-d92d-3866-b37a-9c31c8b6062f | -4.5749 | -43.3017 | 2024-12-01 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 29e89c93-a774-32aa-b4b8-6208893d0f57 | -4.558 | -45.7008 | 2024-12-01 01:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| aec2e38f-1318-3b5f-a5f4-a0e44aca5650 | -4.5375 | -43.304 | 2024-12-01 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| fae451d5-8c46-3acc-a730-1f35f7e8a40f | -6.9341 | -43.5634 | 2024-12-01 01:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| cadfbbdc-547b-3a6f-9586-b8dd771d2d64 | -4.5578 | -45.7232 | 2024-12-01 01:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 158.3 |


[Clique aqui para ver as próximas entradas](README17.md)
