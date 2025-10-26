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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c984cf6-22ac-30ee-9a54-70f0e2a6c2c0 | -3.10016 | -49.46318 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8fbf15c-cfa2-371f-b5be-4cb9625fdffd | -4.82969 | -50.93223 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05c5a5bf-c99f-313a-b598-e88869638528 | -3.10485 | -49.4669 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0955e5bb-8a8e-3879-bc4a-eb308fcd23b4 | -8.71884 | -48.01012 | 2025-10-26 05:21:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03c18d48-367b-3b9c-aaa1-2f8db6577d88 | -3.10362 | -50.2068 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1db1377b-d872-3895-a697-92d995328c27 | -2.97448 | -49.12257 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e482dbf5-fcdb-3e71-b3f2-ed019c47de7a | -3.11619 | -49.10694 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af2051e7-7411-35e2-9c0f-a32a48b535b7 | -2.48956 | -58.06223 | 2025-10-26 05:21:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 154ef5d2-a1f7-3959-a579-0f0cb81064d5 | -3.23975 | -50.64883 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 149d7fde-1eb9-3aa5-9d55-3765d55b507e | -5.88885 | -49.658 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea071492-a8c9-3151-873f-a5a3fe93ddda | -3.10812 | -49.44449 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 085c9bf4-8b6c-3044-9f72-aafa789e4fd2 | -2.31953 | -48.57929 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5b07915-8d22-35e1-8df2-ac8995c9262d | -3.7954 | -52.01544 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad00214-f511-3fc3-a006-b8f994103eba | -6.78752 | -45.41111 | 2025-10-26 05:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 483abbaf-3abb-3759-bafb-26426ae05797 | -9.43699 | -46.33052 | 2025-10-26 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 542c845a-c484-35a6-8430-200db5c274c6 | -4.73925 | -50.8696 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5a35339-0d2b-3916-95f8-b3b152d73cf3 | -9.05516 | -46.98821 | 2025-10-26 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05bd7c36-83a9-3c11-a705-de6dfea14b56 | -6.80543 | -49.35299 | 2025-10-26 05:21:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8555c660-ac05-30a2-a9e4-e014ce9e8a1d | -2.78551 | -54.42118 | 2025-10-26 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c9b9891-97de-31c5-959e-f86a28b7acb5 | -4.59741 | -49.58999 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7fe6f59-c6d6-3bdf-930c-407e3b69d1a8 | -3.54929 | -54.69193 | 2025-10-26 05:21:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 813101f4-8319-3a12-8b29-315b19bf3255 | -3.92487 | -52.25046 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59be72e3-941f-3bc9-8bec-11ed65190290 | -6.09453 | -47.05621 | 2025-10-26 05:21:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f627766-32c5-3d2d-90d2-272fb35f02a6 | -3.8499 | -51.38319 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bb69e1d-aacb-30ce-bab5-6a64a00b3121 | -4.47695 | -48.67514 | 2025-10-26 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4570cd33-8119-33d2-85e8-5827acfff060 | -4.15083 | -50.77234 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc8402e3-3f62-3689-960a-9dd0d72cba83 | -5.71349 | -49.30845 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ffc9e5a-a6c3-3bd7-be84-32647653e916 | -9.0485 | -46.98717 | 2025-10-26 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d0d68f1-489b-3f00-be85-ed58ae34e85d | -9.4374 | -46.33558 | 2025-10-26 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 707e2c84-0a55-3f15-a910-acf5b7460176 | -2.68809 | -54.77085 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90b1bd22-ff91-338b-9e08-9f395db2e307 | -2.94706 | -51.75922 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4eb86c71-048a-38f8-bf5c-86d5fe1de5bc | -4.20042 | -54.9427 | 2025-10-26 05:21:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bdb1fe8-d018-3a99-acd1-ca023cdd2983 | -3.10836 | -49.44476 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4076834-2476-394b-84ff-385e07afc88d | -3.10623 | -49.45744 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da41ca1e-85ec-3d20-aba3-fbf1239ce771 | -6.39667 | -45.77821 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 500c1715-c1df-3c4c-ba4e-a875e02c4a13 | -3.10764 | -49.44778 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6587f7ac-3970-3611-9fb6-92da433455f5 | -4.26647 | -50.51147 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 274e763a-7a0f-365e-b753-13c6e1a9990d | -2.78888 | -54.41924 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2d33612f-fc54-32ce-a15a-e18133ca0d36 | -3.76235 | -52.26196 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb760aaf-f680-3e52-aef4-950165c2c876 | -9.16051 | -51.30619 | 2025-10-26 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d702f79-a507-30ad-a9ea-f0e50f74bc96 | -3.84525 | -51.38246 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99476c08-4185-3639-b6d2-2f4974502a38 | -6.38965 | -45.77782 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4a90d6a-e620-3c31-b42a-91bbee2f3d67 | -1.281 | -55.77775 | 2025-10-26 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29424dc1-d47d-3276-b689-d0f4aa4365b2 | -3.87209 | -52.18831 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5765871e-3e32-3217-a99b-17e0a74b3c43 | -13.05565 | -50.28829 | 2025-10-26 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3385194-8606-3776-955d-5587f6c92509 | -14.8886 | -52.48189 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 186e93ee-1738-3e55-897e-d5759681b800 | -14.92165 | -52.46409 | 2025-10-26 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52c30d32-769a-3a62-b7b3-7ca5a04b3e36 | -15.1809 | -47.23434 | 2025-10-26 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16e05bfb-5f5a-304e-883b-dbad799bd260 | -11.2482 | -49.86856 | 2025-10-26 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecebe010-7d20-301a-94fd-9b61c3969169 | -21.7596 | -50.052 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 207eb6bd-d86e-304a-9ed0-43cde175cd86 | -11.33522 | -53.93643 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b267a936-b5d8-3397-a741-bd4b61becab9 | -10.21188 | -52.66321 | 2025-10-26 05:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e21f504a-a1d1-33ad-ab8b-eafeaae547a3 | -21.76068 | -50.04659 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 51743665-c83b-3567-90e3-d85f914f36ea | -11.53226 | -47.10111 | 2025-10-26 05:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd058fce-d966-3480-af8f-64132e1e7cb2 | -11.87919 | -56.39996 | 2025-10-26 05:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41330c89-3c4e-378d-8a87-0a726560e2aa | -11.43821 | -54.09126 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90f085f6-46c0-3e3a-8909-ce7d9514ccb5 | -11.32706 | -53.93114 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8951858b-7492-3e3c-b283-c7e8669046b4 | -15.46362 | -50.48065 | 2025-10-26 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f10d369-0e3e-3519-b078-0d93b6ec529a | -9.8625 | -50.54609 | 2025-10-26 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 346e2e04-ba0e-3cdd-a593-ab459863b6ee | -14.50228 | -57.3372 | 2025-10-26 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f14c3c75-2fa5-3177-a568-41a96b5a350e | -10.8347 | -47.62512 | 2025-10-26 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0465e0dd-fb20-3e43-bbeb-09ddfd5780b6 | -11.88229 | -56.40514 | 2025-10-26 05:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83be2561-a3cf-37a9-acaf-30c58a507b26 | -15.18859 | -47.22876 | 2025-10-26 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b78fa24b-10bc-32e5-8262-3210465f754e | -9.63395 | -57.0194 | 2025-10-26 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b4c4401-7340-320e-89a8-c8d67fa7c2be | -11.24794 | -49.86694 | 2025-10-26 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30f2b2c3-bf2e-3f53-8a1d-5e0b03b7b816 | -15.18632 | -47.22808 | 2025-10-26 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b0a6208-0af8-3dc1-ba57-974a8c173540 | -14.83855 | -52.43957 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33367d46-f0c5-31d5-b956-e1eff157710c | -10.40706 | -54.48943 | 2025-10-26 05:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cec62744-a123-3956-8089-1abfe4489ef4 | -10.03303 | -59.58913 | 2025-10-26 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab7d17c6-4107-331d-b6c7-f2c8cd9ba153 | -10.22652 | -49.8477 | 2025-10-26 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79f9e87b-b950-3379-8dc7-7d80297ac681 | -11.24845 | -49.86293 | 2025-10-26 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 407bf6ef-6d71-3558-a602-d86066939bae | -11.81708 | -57.94446 | 2025-10-26 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ff074a-51e0-30af-8b3a-1a84422b1475 | -11.09965 | -54.2417 | 2025-10-26 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 600d619a-cdce-3db2-b9c7-84180db838f8 | -14.83307 | -52.44219 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c3dd03a-a3a1-395f-9f95-13d9e88b8da1 | -13.53357 | -49.55333 | 2025-10-26 05:23:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2129620-9f34-375a-b6aa-a0fb79ce468c | -14.76625 | -46.61425 | 2025-10-26 05:23:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f56f8f55-a5e4-3763-b62c-b8560772e298 | -12.88973 | -54.73186 | 2025-10-26 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 901b574e-c659-3dfd-83c3-56670ded6365 | -10.97172 | -62.42788 | 2025-10-26 05:23:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ab36c7b-152e-3e7e-b277-1ac35551c322 | -11.44016 | -54.08989 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 281da530-c132-3527-a51c-63e622401fb8 | -9.86294 | -50.54276 | 2025-10-26 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaef65be-e52b-396d-be8a-a7ee698b5888 | -15.45776 | -50.4803 | 2025-10-26 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01593170-f289-3247-b2df-c4a11af6b513 | -11.28824 | -54.17923 | 2025-10-26 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e428903-76a4-38f5-8ccc-8a584a6d11f0 | -11.87854 | -56.40456 | 2025-10-26 05:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5512e925-0f32-38da-8e6a-ff1d120cb9fc | -14.73967 | -49.69056 | 2025-10-26 05:23:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd4e1335-540e-3e30-943c-aa1825bb7ed3 | -21.766 | -50.05282 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 612c6159-cdd2-3af6-ad5b-f3b996dc8299 | -21.76694 | -50.04186 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 169dcb5a-9468-31f7-b559-33848cb574e6 | -21.76709 | -50.04741 | 2025-10-26 05:23:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d645a374-3804-3f03-bd95-bc389e0f9939 | -14.43647 | -49.96162 | 2025-10-26 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55e15698-98c4-3f95-ba37-b8af32f796e1 | -11.32648 | -53.93534 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c2e7539-0f8f-3da5-8fdc-d7bec7951035 | -11.21183 | -54.84384 | 2025-10-26 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67bac33a-aea4-3344-a0de-3d2ea5c54174 | -13.91831 | -48.38289 | 2025-10-26 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e721649f-c9c4-349a-960e-92fee7074ff7 | -11.32764 | -53.92693 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08f4c512-3438-35ac-831a-1e278beea92d | -12.00056 | -46.78471 | 2025-10-26 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c18e7e4a-691d-369b-8fda-b6aa879ee5e5 | -11.56241 | -54.52091 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c7559af-4596-36ef-bc06-fd6ecab2d0ed | -14.83712 | -52.45123 | 2025-10-26 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce2d2b0a-157b-3621-b2e0-3794f882750c | -9.44365 | -56.64256 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e3b9b243-f4a8-3397-af06-9517b150afdd | -13.4865 | -56.55897 | 2025-10-26 05:23:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46563d95-8ea9-33ed-beb9-475ddfb5866e | -10.97381 | -52.03098 | 2025-10-26 05:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d50a192-8013-369a-a32a-03b4fe1a7efa | -9.29151 | -57.54978 | 2025-10-26 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b592b9a9-d0b2-3c07-aa50-cc6d03cb1df3 | -12.8586 | -48.65288 | 2025-10-26 05:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README51.md)
