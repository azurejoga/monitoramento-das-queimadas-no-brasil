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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ef4221f-ca70-36af-a927-784be3697faa | -8.41768 | -48.30418 | 2025-06-22 04:40:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5da24c35-c6b9-3a6e-93ea-29a8f89234f3 | -3.62254 | -47.52284 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 835fbda6-14ff-3bc5-9a58-f7846e64d527 | -7.87548 | -47.8847 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 464c72d3-763f-34ad-9f3a-65c3431dd482 | -8.11531 | -43.14544 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 498163bd-97f9-3a6f-96dd-42023bc10292 | -6.62798 | -47.3527 | 2025-06-22 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d78ab886-7555-3612-914a-565df07e7e0b | -7.87491 | -47.88844 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13ea2a78-4e43-3065-9d81-83966ca56877 | -7.10405 | -43.7198 | 2025-06-22 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 788b4939-e845-39be-9cd8-30ed92f7702e | -8.07692 | -43.15187 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 737abc49-b466-3e2d-ade2-351a1c0e7832 | -5.77093 | -46.57057 | 2025-06-22 04:40:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43764f0d-5b78-3df2-8626-093b7602d5d1 | -8.72753 | -47.15807 | 2025-06-22 04:40:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80ef5336-6775-33be-949e-e1cbc0e6db08 | -8.03575 | -47.63776 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 936c05c7-514f-3df0-93f3-371ea828da57 | -4.54375 | -48.01402 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d027621-8528-36fd-b28a-4e875c9e18db | -3.62591 | -47.52336 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f21f5a07-c0cb-3488-9e53-c373e338d954 | -8.08663 | -43.1487 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f425a780-36c8-33e3-a13b-c27740fd6fc9 | -6.50695 | -43.63252 | 2025-06-22 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e11dc7e-6739-3c59-8245-a07c92df5943 | -7.87835 | -47.88896 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26d0567c-2dad-3e3b-9333-3f6d4899b6b7 | -8.10106 | -43.14803 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 1197fdbc-0c2f-3ef2-a660-96e714b938cf | -7.98606 | -46.21438 | 2025-06-22 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12953336-110b-3b0b-a9c3-e8d5483bcda4 | -7.27273 | -45.3618 | 2025-06-22 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee34d5e1-9315-398e-820c-6fd4df4ecc64 | -4.54319 | -48.01755 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 551198b8-c2d4-3761-8c2c-0cf83cc93e0f | -8.11077 | -43.14478 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d8217e6c-bd5b-36b6-be1c-bfea558ba3cd | -5.41627 | -47.56953 | 2025-06-22 04:40:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85031ba2-7b22-3936-9138-9cc33e10ff3e | -8.08683 | -43.15062 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f133eef9-87d5-3518-94c2-fb37553f4d41 | -8.42505 | -48.30156 | 2025-06-22 04:40:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f1a21be-208f-37e5-91f9-fc9a9911d513 | -4.53425 | -48.00888 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ab6efaa-1a29-33e4-aafc-acb53f3699cb | -8.06923 | -43.10878 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 224de7eb-eedd-3b46-89da-6a1a16533d3a | -8.03516 | -47.6416 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4cb80a0-7de4-3a73-a74a-ff24b7815589 | -8.02763 | -47.64436 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b866122e-4368-375e-98fe-74724fcdab5f | -6.52971 | -55.02129 | 2025-06-22 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b85a355-40d8-30ec-a44d-107b9302ec65 | -7.10464 | -43.71581 | 2025-06-22 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01cdf5da-2987-3d96-8d37-127b1eefbd98 | -6.50441 | -43.63503 | 2025-06-22 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 441cf2e9-311b-32be-81e1-69a448f0eaab | -3.6158 | -47.54375 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7251bf95-3b73-3a6c-8550-3e84bd228c56 | -5.36749 | -47.29786 | 2025-06-22 04:40:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f05add2-3f78-3d1b-bcb9-e74b5228e368 | -5.04042 | -47.65431 | 2025-06-22 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fe69c80-e932-39da-a6ba-e7cc08588b70 | -4.54039 | -48.0135 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf0c09b9-4793-3c78-ab5e-57f8532f1c6b | -7.29292 | -47.83973 | 2025-06-22 04:40:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0e9367f-7159-3474-907d-1ac75b6e762f | -4.54655 | -48.01808 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 706a8faa-0335-3dfd-9ced-d3f38ca6e1c1 | -8.07778 | -43.14922 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7e935240-875d-3f39-a975-fb76cbf777c3 | -5.07188 | -43.72844 | 2025-06-22 04:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ceb9492-fb10-3808-89b7-e4aeb31cdaa4 | -8.00074 | -49.70816 | 2025-06-22 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de8c269d-a240-3061-9598-e34c8ab588f0 | -4.53704 | -48.01297 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e379755-dc7f-38b9-bfc5-78b72b1c342c | -3.61242 | -47.54324 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a10af6e-acd8-3aef-96ce-5c940acf398e | -8.45099 | -47.01124 | 2025-06-22 04:40:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b9ed16a-dd73-3937-9f63-3d6524802f21 | -8.07445 | -43.10477 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78bd84d7-4152-3071-9a66-401058e78349 | -8.41824 | -48.30051 | 2025-06-22 04:40:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b8d7c11-c199-3b4f-8c60-7f4d4c2f5726 | -4.54095 | -48.00996 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed5292f6-492b-39ee-aa58-ec4f9c343a44 | -4.30061 | -48.07418 | 2025-06-22 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73d69947-6dfd-3869-8cc0-29bf1d72eb86 | -6.50266 | -43.63193 | 2025-06-22 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bce1e03-3699-3f2c-8761-711b5c83f66b | -8.08168 | -43.15448 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d55afab2-022f-3540-9630-44c6a7d170e4 | -8.4222 | -48.29736 | 2025-06-22 04:40:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ed438a9-aeff-3047-8b7d-04bf7af5bc8e | -7.06845 | -47.84861 | 2025-06-22 04:40:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a47c1c4-4ddf-3636-a5d7-ba6ab8717946 | -8.42108 | -48.30471 | 2025-06-22 04:40:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4210b448-8de1-34d7-aaff-d66059e62722 | -7.87204 | -47.88417 | 2025-06-22 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a2040e1-3aeb-3a51-b051-56cf26ce3cbe | -9.19059 | -45.33121 | 2025-06-22 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b12f2ccb-2fc3-3331-88af-7d8c4c1657d5 | -7.20085 | -43.57717 | 2025-06-22 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4633080-f4fc-3ec4-8bac-db2c9a83a683 | -3.62536 | -47.52692 | 2025-06-22 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ca44035-43e4-3862-9c4f-87013dd5fcf4 | -8.1056 | -43.14869 | 2025-06-22 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 0b845936-365c-372f-96a2-fea722a52df9 | -4.5443 | -48.01049 | 2025-06-22 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de8a5693-3257-3f94-abcc-719fe23f043f | -5.32493 | -55.94401 | 2025-06-22 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7219df03-ac77-316b-8a43-404f0e63b78f | -13.79531 | -54.29546 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d196b7b-81bd-31eb-b619-412562b0a00f | -11.11066 | -46.66184 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f660e8f-ab1a-31a3-9caf-93f112dc46bf | -12.47377 | -54.4219 | 2025-06-22 04:42:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fb65b0f7-ffad-3cae-8930-53b2105c2382 | -12.57944 | -56.97721 | 2025-06-22 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aabf983-34c1-3e86-ba87-e76f3e145d13 | -11.18355 | -54.40755 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1f43ef0-25fa-3a0d-8b93-34adf418a87e | -11.56886 | -52.09803 | 2025-06-22 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 093408dd-fb75-30a1-a859-15ca680fff3f | -10.89319 | -56.4744 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ad5ecdd-3c04-334e-a475-4f0cb16d4ec7 | -10.85494 | -53.76328 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 881b5f98-244b-31a5-a035-a13014b8701a | -10.52364 | -53.62404 | 2025-06-22 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2907b24f-481a-3815-9efb-e1b643b03427 | -10.89036 | -56.46552 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 598526cd-8714-30b6-a87a-f9d03c9ffac2 | -9.1694 | -61.40537 | 2025-06-22 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bab09854-5970-30c0-929e-22d0c4325852 | -9.47629 | -57.3324 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a3c959e9-e496-3253-806a-eb23e725ad67 | -9.55995 | -50.78146 | 2025-06-22 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15131bf1-c870-3cee-bb90-a44756da81c9 | -13.80322 | -54.29255 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fca467c9-d97d-3375-a99e-d6c7673b45d6 | -8.12034 | -61.41842 | 2025-06-22 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e7bf5f8-9834-3b1e-b5b6-00db79109283 | -11.09671 | -46.67831 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 614c3fbc-0306-38bd-a585-12114ac2b135 | -12.58089 | -56.96906 | 2025-06-22 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f13a1551-8027-3037-975a-5dd6ef89ea91 | -12.60463 | -48.37619 | 2025-06-22 04:42:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4916d53-2638-3225-9e5f-8171b23d91de | -13.27314 | -46.83533 | 2025-06-22 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67d4a608-803c-30bf-983e-2173fc494cfa | -10.16698 | -51.65537 | 2025-06-22 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b867ad4-992e-3dc3-b416-7a8b77fafd61 | -11.10556 | -46.67039 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f244cf7-e345-3515-913c-5a1a0c794cac | -8.98407 | -49.8679 | 2025-06-22 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12646fbb-1460-3630-b9a4-b199eb98b7ca | -9.09858 | -50.02193 | 2025-06-22 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d822f1f-7521-39e8-9ecc-9c869eb66c41 | -9.46512 | -56.06004 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b6f45d97-ec60-3642-8c70-9e88bea2d50b | -10.52435 | -53.61981 | 2025-06-22 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32b52a26-fb06-3648-a412-98dbef1fed57 | -11.78627 | -57.24757 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c627a9d7-ab5a-3879-97cb-86dba79df8d5 | -10.85571 | -53.78108 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d347e1fd-be5a-339f-8404-a09936628aa1 | -9.91605 | -59.91467 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40e3f1a0-72f2-3a48-8dc9-2fe8ec516346 | -12.02852 | -57.08625 | 2025-06-22 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2beaad27-9f94-3002-8cf0-0465249ccf6b | -8.59484 | -51.58524 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8d53c084-c1de-33f5-8947-362109850533 | -11.84128 | -57.76176 | 2025-06-22 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b50d1a26-b166-3154-a563-36f81e16e38b | -14.25999 | -45.49852 | 2025-06-22 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c62c0ab-f308-3017-b64c-0054ac0f0078 | -12.47745 | -54.42256 | 2025-06-22 04:42:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a2fd296b-c075-3597-8092-824cce076563 | -10.85565 | -53.759 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef73a3dc-167e-393d-954f-b9ade39fce7b | -9.16856 | -61.40979 | 2025-06-22 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fb43f413-db92-3110-bc8b-ce4089fed1b3 | -10.74408 | -52.51088 | 2025-06-22 04:42:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26186214-eab5-301e-9319-34c3d97d4e56 | -10.29548 | -60.5517 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fdff29e-dd05-3f44-a057-aa881cdec076 | -10.85857 | -53.76393 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0073ecbe-d542-3ac7-a9d4-f34dec58c90d | -9.6756 | -56.09271 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50da1c50-d211-3310-99fd-9cd206517fff | -12.47301 | -54.42635 | 2025-06-22 04:42:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8c289131-0091-3ac3-86a4-0cea671da25c | -14.03548 | -53.36159 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README9.md)
