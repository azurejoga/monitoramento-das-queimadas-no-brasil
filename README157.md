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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 394a0018-7b95-3a83-be80-fa0511492e0e | -6.13885 | -53.50836 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6664cc00-3983-3fc7-8ed9-7e47217bb0af | -6.42192 | -55.19789 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2439d2eb-5f38-3129-a810-32be8e683352 | -3.4705 | -60.25627 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da4f52d9-100f-39ee-95da-dbd8080a9c9a | -7.57809 | -45.64825 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 675df8bf-8d6b-37f5-8bfe-f5ceed189715 | -4.35584 | -55.23034 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d47c36-8d56-3219-be73-bfc27e6f92e6 | -12.00644 | -43.4517 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4edfd26-4d50-376d-8a17-0b2efce7f971 | -3.53313 | -59.57908 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 68315e41-9865-3a33-b2df-dadcaeb6311c | -4.96267 | -55.1235 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 515b9591-4d60-3850-b47a-3cf4cef2dc46 | -4.93054 | -55.86627 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9de95cd4-7a3f-30c8-bbd7-7b46c69d9bf9 | -3.2555 | -54.03527 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4b8dda30-e0c2-3a3e-acbb-9189002fbc0b | -3.75064 | -59.47813 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76d3abb7-2572-391a-8d2f-19e86329b0d8 | -6.44096 | -55.0388 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bf5634c-0397-33c2-a585-754c9113eab7 | -9.90551 | -44.78431 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80d946bc-766c-3cff-a678-cacaa2420481 | -3.30781 | -53.71206 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1b202d2-e152-3c6a-80d7-86512e55a5d6 | -2.99322 | -53.84829 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f57d92a6-595f-3ade-861e-a6baa347c528 | -2.94331 | -54.18148 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ef65847-cd8f-3bfd-8843-436a4a240da3 | -3.28129 | -54.0746 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6c87385-49a3-3392-b840-3a7a520da0fa | -6.87986 | -44.81475 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5350442a-bf09-39ce-8db1-556275e3f8bf | -4.14004 | -54.03197 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2b4bdfc-e35c-3f97-bd51-00e4421d98f0 | -2.9245 | -54.07532 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c26a3cd-44a5-3265-8545-7d8b1c794f60 | -4.14634 | -54.03683 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d02bfac5-7c94-3907-8ca5-e84bcaa936ea | -3.54261 | -54.62783 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ea31887-a9c8-3e10-ac4d-50950c3ec926 | -11.99879 | -43.46661 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd0762e1-29a6-38cb-86a8-99aee28c814a | -3.0084 | -54.0887 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e09b86f9-725f-35e3-8c73-17f0ac599354 | -6.92661 | -43.66654 | 2026-10-09 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aa96c79-6906-3b8a-859b-48db20e594b6 | -5.28959 | -60.09074 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d06ffb54-d47c-3914-bdac-ca117fcbb441 | -10.87828 | -44.80511 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f6b3778f-2b1f-3453-8a01-c49f1493c353 | -8.97034 | -45.14963 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50f375ee-9248-348f-bf49-7aad41feb301 | -4.1111 | -54.41061 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08ccb18f-b4fc-3a22-a490-61a7579a5527 | -6.01107 | -40.97355 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 230492cf-5cfe-3342-b358-9514fe4ec879 | -3.56455 | -54.66274 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08fadb4f-34b6-31f9-abf8-3028a20ad38f | -6.49381 | -55.96127 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe5ea599-56d5-350d-a338-e59b2bc2d27c | -11.64152 | -43.69863 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60d93fa7-c3e7-3995-8cbb-6af8f3872345 | -5.31918 | -55.85576 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c018d47b-a8ed-3121-8da2-d59061d86c70 | -3.00458 | -54.11481 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d4cffeb-ce0a-3761-9b4c-51405272fb4d | -3.38285 | -59.42989 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f5b5ba3-c4f6-39ed-a97b-01b5ee65f58e | -3.76971 | -58.84381 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c3f631e-9a01-3e63-b941-5ed243008702 | -9.77873 | -44.7813 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9abd977-22ac-31b5-b2a9-4abbdf1ea243 | -2.99825 | -54.0398 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34a30c66-12fb-3141-9f27-9cea2a2a6e98 | -3.08016 | -54.29422 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e124fa50-2458-3d22-9222-30fc909e47a2 | -3.38768 | -59.43068 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f495cd9-a39d-328d-b0cf-c159129bec28 | -3.01122 | -54.09613 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46520e6f-ab20-3748-aa5f-f7536226caad | -3.74493 | -59.48259 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1b0a4b3-6911-3a05-b606-da58b8257668 | -3.09288 | -53.94456 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7d24fe7-3814-3788-aa39-256c9f292139 | -3.68961 | -51.98563 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b748cc7-41cf-34b1-a737-ec73fa5878a0 | -4.06638 | -51.03619 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62db24d9-995d-39fe-a5bd-4998764df8d9 | -6.10018 | -53.46251 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60102093-0f16-31c7-85ab-5b62435fd580 | -3.20995 | -57.86682 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53adc57a-2ee8-3df6-b63d-998e552c1d2d | -3.10617 | -53.95056 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 691eba40-2a38-3b4e-8b62-0e61cd27ffc5 | -11.31103 | -44.83098 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2583d0cc-0040-33d1-a955-596353d4f596 | -3.03856 | -54.10445 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bba0f172-74e8-34bf-94d7-d6392fd45ad7 | -4.07266 | -59.83398 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8d0bc4a-40d9-355f-86a7-617dcf800e77 | -5.70363 | -53.45031 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00447620-9fe8-3678-bbf8-f238cc2e3432 | -2.99502 | -54.08263 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0127e62-89f2-3ac0-94eb-a9f85976c5da | -10.8424 | -47.93825 | 2026-10-09 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6fde00e-0543-319d-9ce3-71fa75e2ad12 | -6.0973 | -53.50201 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1138065-e797-330a-8f23-94ca30a636a3 | -3.05837 | -53.91571 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0fd00c5-c8ae-3fe0-a944-6c32f93e48fb | -6.76343 | -48.17147 | 2026-10-09 05:04:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df0a5c6-30aa-3618-a397-399d86aae43a | -5.71528 | -53.49173 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 39eea16a-c095-3b61-8433-992e7b1d78f2 | -5.93139 | -51.8232 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd0ec681-a224-31ac-98a2-ed4841652e37 | -6.45526 | -53.69056 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14d32026-d53e-3b59-a517-43e98c7947bf | -3.59532 | -54.67591 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbda0c0d-5d6d-380e-8a79-9bf4bd21499e | -3.39078 | -57.99696 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 989c0d25-1ff0-3762-85cf-a09c860dc4d5 | -4.45378 | -47.92345 | 2026-10-09 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 808945f8-856a-3d39-8ff9-f72ac35b0025 | -12.00686 | -43.44821 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a08ebe7-fe50-3e77-b0cf-bbc9a0ba301c | -11.25591 | -46.26683 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 981c12be-7aed-34df-9330-86f070d39676 | -2.83886 | -57.47174 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 450effea-0296-3bfd-815b-b1851d3c10f6 | -2.94857 | -54.05944 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa673925-acd8-3933-be58-4dd8a3eca5b7 | -3.00429 | -54.092 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83537717-0bd7-3b02-b0ea-e7d949fa8214 | -3.60578 | -54.56684 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39504b05-a0fc-30e7-99a2-ab0742f31571 | -5.71033 | -53.45827 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2656ec9-3aca-3b4b-96ea-2a77c30766b9 | -4.57419 | -55.9912 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a69c76c-58f1-3b34-8010-2656f1e1ad6f | -10.86364 | -45.54206 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3fcd5776-60a8-34c4-8eb7-345ecd8cc53d | -6.15683 | -51.70033 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72093838-c5e8-3f84-ad3d-d9e8b7ac4336 | -4.07817 | -55.38144 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4598f21-4a2d-398b-a95b-203eb4fba229 | -8.9122 | -45.17032 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64ba3bbe-89d3-3f10-9cca-238972913c45 | -6.4952 | -55.95267 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b3c3890-aa80-3847-a730-7affc6ead39e | -6.24317 | -52.83788 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9971a599-c08a-38b4-9b5d-a50a27341de9 | -3.29006 | -53.99786 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2aad1fc-6ab5-3e59-90b9-578f57b12985 | -3.17674 | -58.83838 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ddc4434-4ba0-3159-ae73-4fd633918482 | -5.22834 | -60.23626 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dadd718f-a6d6-3a61-a6ef-9b18b2cf8366 | -3.94737 | -56.02388 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a89b8fb-2504-32a9-ade1-08e0490a9f2a | -5.98745 | -55.3622 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 925c3c02-8ff9-322c-b795-727d45709b76 | -3.17523 | -57.49878 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbdedb8c-1746-3f28-a8fb-8c226ac11898 | -6.21657 | -52.88387 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b799a105-3224-3d82-9ca2-16de154dd005 | -8.65846 | -54.53642 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0317592c-4d3f-3759-962c-11e222934c6f | -5.69573 | -53.47816 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04c87858-b61b-37eb-bbc9-35f3c686cc16 | -6.23705 | -52.87617 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f864392b-9e04-3c5c-9bb2-0c32cdc9df73 | -3.27207 | -54.06526 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57039b8b-32d6-3f3a-8037-97b11d713128 | -3.01534 | -54.09283 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e3380f1-3fa2-3701-9e4a-78a0b405fc88 | -3.07472 | -53.96891 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e470c14-a416-3a30-96cc-ad121ce2b940 | -8.73523 | -45.15937 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 971ab3bb-f8df-3080-99ec-af005bd30bf6 | -3.00551 | -54.08429 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d86f46f7-3b70-3818-b6fb-e32e3ce488ea | -3.06877 | -54.25235 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d86cc066-4cb4-3f11-8e35-9b5d8216e045 | -3.90648 | -55.89592 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5341ec8-1483-3ed8-afe7-b6fa1e542810 | -6.89647 | -55.55636 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f48d229f-2775-30a0-9621-b92bbb90a47b | -8.70259 | -62.41539 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba540eb6-603d-3044-921b-cb16486f0ab2 | -3.00795 | -54.0689 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 874ad162-414a-382f-bc0c-fd447460eb0e | -3.71249 | -60.54239 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f9ee7b-46f4-3884-8c51-4864d74b8fe4 | -11.99051 | -43.48698 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README158.md)
