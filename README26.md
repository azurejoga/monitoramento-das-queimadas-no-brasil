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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9320307d-4b60-327d-be30-e74477be9397 | -0.42052 | -52.03752 | 2025-10-29 04:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86111f37-89bd-36da-aff5-7c5610b4b4b7 | -4.2051 | -50.09385 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b59e08f-3b95-3bc0-9b3a-f993f3041664 | -3.71509 | -41.57265 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f8db3775-7101-3ab0-8abf-d34cea0885e6 | -4.52623 | -46.04393 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb17e273-ec30-30de-a7e7-73de63a2e9a1 | -4.38869 | -37.86134 | 2025-10-29 04:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20a3d41d-ee7d-3b96-ac28-5a8c1a7ac0e1 | -3.45875 | -43.34969 | 2025-10-29 04:21:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 103918b8-42fa-36c1-92b8-b7a4f03bd72a | -3.69454 | -41.56553 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b4b5cbe-00aa-3f79-a52b-cf0c0cceb0f9 | -3.16725 | -48.6167 | 2025-10-29 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b43b3a7-b746-3c42-99a2-81b1a3b3182b | -4.75479 | -46.97514 | 2025-10-29 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 685eac41-8f96-3c00-a386-177db31b4300 | -4.85871 | -45.77923 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b607077-c1f4-3842-b6c1-1a6566ef656d | -3.71861 | -41.57318 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85a47651-cbc3-3267-b6ed-de5b4f8058e3 | -4.2908 | -44.48769 | 2025-10-29 04:21:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a0a9b7b-3567-3f13-b05e-f7949fb11f5e | -3.178 | -45.65024 | 2025-10-29 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 238ff9d5-3fe3-357e-a899-0f1d0a4b7f88 | -4.21004 | -50.09055 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f84b9e8-35e3-3c68-b752-9e1573c9c3c8 | -5.52747 | -41.70707 | 2025-10-29 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 130be4da-917c-33ce-b833-30722844e544 | -0.43038 | -52.0425 | 2025-10-29 04:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fffb9d4e-03ad-3f73-9ca6-7d4413d9ae9a | -4.67338 | -43.26087 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44103467-cfc6-36a4-b664-34fb46864974 | -2.90893 | -40.34381 | 2025-10-29 04:21:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2f20ddbc-3c7a-37fc-b377-e35d6fa64b7f | -4.0059 | -49.03736 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9276140-b29c-3712-9927-ac97423f1ee4 | 1.83323 | -50.50248 | 2025-10-29 04:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05ce57f3-9117-3b43-bae2-c0552ef572f5 | -3.15138 | -50.46138 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c9db93-d522-3371-977c-311a905b6f93 | -3.04358 | -50.26818 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 431e1ab6-d479-3d0c-835f-3cfa6870f9b1 | -4.47955 | -43.4366 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a7c12bb-07e4-313c-9111-33610f65295f | -4.20281 | -50.08113 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 932459ae-6a03-37e2-a0c9-aec453c459c1 | -3.14472 | -49.2181 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1289948-2c0c-387b-ad86-f74f4bba4b99 | -2.63272 | -47.95777 | 2025-10-29 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1642ad7-c2dd-3c01-b846-a5b4fbbb6186 | -5.56833 | -42.17231 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 02de7078-6817-3ec1-9e7a-9557c623fd0c | -5.00992 | -41.04683 | 2025-10-29 04:21:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15584ab6-7549-3074-b6e3-9d3fd2fda82d | -5.48909 | -42.16893 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e765662b-b963-3f35-96a6-2084ed859eef | -2.42591 | -49.3067 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 258f8bc4-f430-3bc8-b663-f1af44cb1f45 | -4.47845 | -43.44361 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 80d74eca-a954-359b-af45-662c95525e4f | -4.79166 | -43.42756 | 2025-10-29 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2eca9f05-f851-31c4-8399-63772c50b31a | -4.00881 | -49.03595 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c97bacb1-b935-3dac-9c33-cf39d42d1275 | 1.83406 | -50.50776 | 2025-10-29 04:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cdce9269-c796-34ce-b95e-4b0e41934633 | -3.8899 | -40.80191 | 2025-10-29 04:21:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7d65707b-26ad-3a54-897a-55b7aa20f55a | -3.81299 | -48.65724 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 065f822c-df8c-3fd1-9066-219aea8f6da5 | 0.60959 | -51.57832 | 2025-10-29 04:21:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a6559bb-ea88-3c40-98c0-24d108dc8e75 | -3.42393 | -50.11855 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72626a69-3290-3440-8ef1-b25228fa157c | -2.20458 | -51.36889 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd2aeb0-f879-3878-9fdc-4da2582784da | -4.52135 | -47.84136 | 2025-10-29 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 055c693d-8768-3914-a797-ed1b09598f9b | -4.48569 | -43.44116 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 24c75de6-bb02-3363-a697-f45db55a63ae | -3.41031 | -45.4865 | 2025-10-29 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ee2362-ad38-3f3c-ba53-72adc1338568 | -3.40678 | -52.72912 | 2025-10-29 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdb1cba6-5f2f-3eeb-973d-a66a9f7584e7 | -3.878 | -44.72093 | 2025-10-29 04:21:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5d000dde-0e2f-33bc-a7fd-e6b0e6f8e12a | -3.71983 | -41.56533 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 528db1b0-58b4-3c7a-bc6c-86d04fe5b34a | -3.59404 | -47.51817 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d689ad30-74b9-3719-afe2-7e1d875bd4d4 | -4.92494 | -45.66869 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d33ed5e4-da9c-3613-af2c-5824bdc2f867 | -3.59462 | -50.38993 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7a94c25-10e6-3210-afcf-6b294a07447d | -0.43557 | -52.04335 | 2025-10-29 04:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d92c3cb8-45fb-35c5-a23e-55e5e7bb51cc | -5.30501 | -43.67285 | 2025-10-29 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6df9270-9bfd-33d6-b579-d0a4e4b8a0b6 | -4.29078 | -49.65207 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2467c4fd-7f8b-309d-a883-839ecc804111 | -2.99503 | -51.25012 | 2025-10-29 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 751fa7b9-9178-362c-b644-0aa9758e72b8 | 0.155 | -51.10025 | 2025-10-29 04:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0de8538-2796-35c6-b135-2c887e0c3f43 | -5.33041 | -41.2174 | 2025-10-29 04:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e094764-464f-3779-bc4e-f92760e72ca7 | -5.1111 | -44.71319 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2f4395b-f86e-365f-b8cc-bfc42e4b3361 | -4.61272 | -46.59866 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daebc68f-6868-352e-ad7f-471349b54eea | -3.40955 | -46.90229 | 2025-10-29 04:21:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 564d7fc6-ad2e-3f55-b6ac-0b85fc589ce2 | -4.51565 | -46.00097 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8677d1b6-b0db-3041-95cf-c1e788e53773 | -5.56192 | -42.1674 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f0472359-c54f-3191-9442-534839fe492a | -4.37439 | -48.67609 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91f1e1b4-3678-3d07-8c49-e8f2b0967840 | -5.51616 | -41.70948 | 2025-10-29 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37857663-1616-30d7-90e1-c60e97499c31 | -3.04071 | -50.26443 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 925a78d5-6295-3130-86a2-54be130f4a5e | -4.65685 | -42.51952 | 2025-10-29 04:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf6107a6-efdd-3806-bf6c-aa707e299e30 | -3.31367 | -46.53522 | 2025-10-29 04:21:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98224f47-bef4-31f8-af76-637db53e1fe6 | -2.32035 | -44.83104 | 2025-10-29 04:21:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13652cf1-3860-3bcc-84a9-6a425caf77a1 | -2.86392 | -48.67811 | 2025-10-29 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 433c728f-9a81-3f35-a501-e4b0287ab66d | -4.36996 | -48.67853 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1eb839d6-88d2-3ac2-bb72-41f940938d8f | -4.86325 | -45.77256 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f18b349-9e73-3f64-a142-4d0e8f8de2aa | -0.86766 | -47.31086 | 2025-10-29 04:21:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f23f9539-86a4-3ee2-866a-872a08ca5bcb | -3.94964 | -49.0209 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0b7ad93-3934-317c-81b4-8b0b2582e977 | -3.63372 | -44.42685 | 2025-10-29 04:21:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37936647-1a6b-38b8-a19c-f5725f1c92fc | -5.63971 | -41.53575 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37daeac6-475b-31fc-9122-8e1f95111622 | -5.26459 | -42.48903 | 2025-10-29 04:21:00 | NPP-375D | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc480eba-f9d6-395e-86ee-26d118f58e94 | -4.00481 | -49.03528 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85533117-056b-30c4-9ed7-92aea566196f | -3.03891 | -49.51896 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e9dc556-6334-39cf-8432-cb58a5a4f5b5 | -3.7163 | -41.5648 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f1f2024a-201f-3a51-9c82-7246195676eb | -4.72663 | -46.81348 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6591b3bf-8e82-371d-b49e-29521e722c7e | -3.72214 | -41.5737 | 2025-10-29 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 59dd5f20-e4b3-3da2-8442-f096d5b0fc7f | -3.14692 | -50.46064 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a61c3ef8-a031-315b-ba6e-050104fc01ed | -1.49386 | -47.80465 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc42295b-1d69-3046-b573-88de4dbea384 | -4.75416 | -46.97908 | 2025-10-29 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d33d603e-6584-3f42-95bc-c40f3bc72b7d | -5.08576 | -44.80862 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6933bc7e-5a17-3f29-b7c5-7fb4349f2dbf | -4.53023 | -46.04085 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 560641cd-aa08-3a53-9e8f-72b7b2ff581e | -3.57075 | -43.28097 | 2025-10-29 04:21:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60086dc1-b453-30be-8b80-722a983a4eb8 | -4.52208 | -47.83698 | 2025-10-29 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 162b96b9-57e6-3359-bab4-57c1e4c619cb | -3.70803 | -45.38973 | 2025-10-29 04:21:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d2396ed0-6bce-304d-86f8-bdb2e9605a0c | -2.06622 | -48.14901 | 2025-10-29 04:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d67db45-9028-3b24-a1c3-0420ddc24ee3 | -4.08395 | -42.92273 | 2025-10-29 04:21:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58a087ab-5c92-3bf3-a4e3-e5db70890c11 | -2.19976 | -51.3681 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eb64b87-89d4-3a88-8c0f-7c0b7e3b4634 | -4.64476 | -47.95866 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7202b1e1-d478-3112-8f98-32f680ef7bf0 | -4.73794 | -46.74369 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce1b7ae-0d9e-387a-ae10-90bfaf846a32 | -2.02478 | -46.99852 | 2025-10-29 04:21:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fa19124-f93e-37fc-80c6-c0e5fd565ea6 | -4.00398 | -49.04049 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cebb12f3-94c5-3ede-901a-063f0fdf58b7 | -4.67618 | -43.26492 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7afe69fd-3759-38eb-b3e8-2a69a0832082 | -4.70141 | -46.10524 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1350d12-85b9-3683-843f-335191abe9ed | -5.56542 | -42.16792 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e4d65d50-404c-3141-8ea7-4a190ac8b978 | -4.20938 | -50.09454 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ebc61de-7e38-3a92-8c9d-0ea60175803b | -4.22391 | -48.56762 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0837f811-3ddb-3354-b225-01756fd2fea3 | -0.42569 | -52.03849 | 2025-10-29 04:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2a4684b-45a2-352a-a169-41ef1504fc1c | -2.42113 | -49.30981 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README27.md)
