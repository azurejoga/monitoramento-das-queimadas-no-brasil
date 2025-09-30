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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 648b7f78-d5c7-337a-89d7-e28ebde42cb9 | -13.06394 | -47.07597 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93567e09-f4a2-3418-a0b1-9f72bff7ba67 | -11.45968 | -45.01815 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ad6526f-dcca-3f19-8646-ae276060976e | -7.91555 | -48.18205 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06404db2-b20e-3cf8-b341-18e88ec2ff28 | -7.90863 | -44.62522 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9841a69a-0d2e-3c58-9972-cb1070f744c0 | -13.39226 | -53.13119 | 2025-09-30 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9174d12a-cdc6-3497-be8e-62723d8089ee | -10.03932 | -50.1979 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| deaa1e2d-a39b-3340-b35b-81571d7cfbab | -14.19046 | -46.60811 | 2025-09-30 04:40:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 427049d4-e22a-3171-8cd5-25e52d332ad1 | -10.66162 | -48.55315 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21cb2e18-d991-3924-96e1-697f095c8889 | -11.25633 | -47.22464 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05011d0f-6ff5-36dc-9e0c-059fd7e01897 | -11.4586 | -44.99425 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66321940-d08e-32b9-8bd8-f6ea7278af55 | -7.70154 | -41.286 | 2025-09-30 04:40:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d0914a5-a7ec-38c9-87bf-6cbbc291fd45 | -10.66219 | -48.54938 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad128389-2512-3974-aadd-fc60b7b74df8 | -12.38514 | -49.91897 | 2025-09-30 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 800c10fc-4d55-3e21-a912-bca476a23800 | -11.25441 | -47.23764 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7b43813a-e9b5-3186-bba8-49e608d9db7e | -12.41125 | -50.19267 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e49f08e8-6b51-3bbf-9c0a-91d2e85dccef | -8.86496 | -46.6741 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93fb1ffe-0bf7-3ec1-8e57-73f4b1444e8f | -13.82862 | -47.5027 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40a5020d-b20f-34f8-949d-1c915ff85281 | -9.94026 | -47.45927 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 376f275f-c70a-36d4-9ef9-a0b5a7a7c406 | -13.78782 | -47.95338 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e2e4ff7-6fac-3213-bc93-3c8d3ee12653 | -13.81075 | -48.02461 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51e62843-c75b-3620-aadc-24e65c6834ed | -10.0394 | -52.08678 | 2025-09-30 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd4647e8-a0a6-3183-8d39-d1ac4ba48a62 | -10.83673 | -47.9596 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94353240-9208-3692-9a1f-d135ba943e89 | -11.2103 | -47.20884 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5a04d36-1d73-323f-9ef5-e99fc355b167 | -9.31064 | -54.51076 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b14bdde7-f693-30f8-aaf6-af05db691de0 | -9.81826 | -49.09778 | 2025-09-30 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2fd8f87-c998-39dd-925b-d28dbbfa94b7 | -7.81722 | -46.9869 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74bffbaa-f84d-35c1-a449-f10b8aaf0ecb | -14.38916 | -47.13565 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8a94406-8a1f-33ea-bc3a-878f0ac0b736 | -12.85077 | -46.99747 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7b7e39b4-b086-305b-9840-994649b2786b | -13.85364 | -47.95713 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35cb0645-4120-39c5-832c-4d95b5729d16 | -9.96325 | -48.79151 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb2da07f-0272-3d81-b8f6-2f96b32a58da | -13.21985 | -47.31817 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96a2010f-69a2-3cb4-b343-99974d9d202d | -9.04495 | -46.69522 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ee165b4b-9e2d-3a8f-a519-9b5e079c6a01 | -7.76894 | -45.74109 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed32c377-e1c5-378c-87a6-f11f623a965a | -12.41457 | -50.1932 | 2025-09-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ab55af8-3784-37d7-a15f-a0127f6d65df | -11.72358 | -44.43932 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 821d48ef-20e7-3ae2-a6c6-cd679a769f0d | -13.77074 | -48.401 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b188ca5b-f768-35be-a233-0d8e30f9670a | -13.58632 | -48.05147 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78eb9d1d-c576-3a96-8f01-d211fa94ad7e | -10.09862 | -49.06801 | 2025-09-30 04:40:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7abb59a-9635-35f9-a6e4-88ec3de99f3c | -11.16745 | -54.12087 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| d07e3b82-e82e-31ee-b2b6-cc9bdb2958d6 | -10.7994 | -45.35795 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8421c2b9-21ff-333b-a99c-20087e7272e8 | -11.40208 | -44.89847 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd76ea7b-46ff-3e9b-bbc3-e528d61ff92f | -8.26707 | -45.50442 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0521e019-f244-3d68-bf14-c064b920221e | -10.77269 | -45.37238 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aff10cd2-9ebc-348f-9f91-403e4ccb2fdf | -10.89333 | -53.74374 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b14a25b-43b5-3634-a88a-1fe94f1ffe65 | -11.41488 | -55.06535 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c575405a-8a47-3951-9b4b-7821763af26c | -10.44883 | -50.86415 | 2025-09-30 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e504c936-02da-3503-a672-8f4549ee5d30 | -9.5472 | -47.77264 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c0975c0-6744-3832-8bb1-2041c3279a14 | -8.31973 | -50.91802 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34669e1d-a127-3c2a-b961-60c565e2785a | -12.75303 | -46.86674 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc31707a-ff7f-37a8-9fe8-d1a1d4656efd | -11.20177 | -47.21641 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 79c1f5dd-c1ab-3027-bc09-0bc644154f9f | -13.3603 | -46.38465 | 2025-09-30 04:40:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e0129a4-8274-3774-b874-93e5f0f25510 | -12.17917 | -48.35648 | 2025-09-30 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cece7413-fb49-3941-bba4-0c058cc8ea7b | -8.50978 | -54.59945 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 25563bc0-0ab4-33d4-aee1-23b1bd0e2bf4 | -10.02964 | -52.10414 | 2025-09-30 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4045090-d8fd-3e69-94cb-703d964a2df7 | -8.5016 | -47.25237 | 2025-09-30 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83364613-05c6-3b83-b752-490ea840eee8 | -11.93734 | -43.39429 | 2025-09-30 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b6e8087-3382-3cc4-91f7-8bfc0812d0ca | -13.36098 | -46.37962 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47f90df6-520b-38f0-ba44-9c8ee7819d55 | -13.41999 | -48.20018 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3aa3524-bd95-317f-9809-158cc68b0e13 | -13.78539 | -47.97046 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94e33426-a212-3b10-beab-6a068d056156 | -10.87257 | -41.61602 | 2025-09-30 04:40:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c36ec58-2066-3bf0-a218-793bf17631de | -11.43129 | -55.03829 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 065f632c-7ea9-37a5-97d1-0770c45cfa16 | -10.38881 | -48.14849 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7e0ed6d-a8ac-3258-9a26-e1c67afcde5e | -8.47626 | -47.69522 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dadf9da-26fd-3c58-98da-b5aacf860b3d | -13.22922 | -50.92847 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 61777912-8180-36cd-a431-83f9fb27182b | -14.04868 | -44.95482 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2204309a-a029-3a0c-bba7-648ea9ba6fe5 | -11.14183 | -54.11732 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 542f31ac-ed07-3393-8acc-4355a95b15ce | -10.19237 | -52.55404 | 2025-09-30 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb7c1712-fd99-312f-bad9-d6a2a87267ec | -10.33434 | -48.21158 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a4c9217-fbb9-376c-80eb-23690df8fae4 | -9.40778 | -54.69881 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe62431c-3206-3fad-9c6b-f2acdf58a6bd | -11.19504 | -47.23729 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 828a7685-26c1-3297-bf72-241e288529af | -11.41103 | -55.06471 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4442b61-9bcb-3553-b54c-da0909e8722b | -13.57624 | -48.09598 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c428b04-d9ca-3efd-b652-5c1d2a35c02d | -10.39281 | -48.14537 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c6bbf4bf-f7cc-359e-b00e-a811e130fdd7 | -14.01159 | -49.63645 | 2025-09-30 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bf38a84-3339-37c6-b8f6-850fb54ab37a | -11.65716 | -47.48537 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 811104b4-e65a-32a1-8084-4e6597b45128 | -13.60017 | -48.03167 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a79968ee-9454-39e5-a938-1b2c0e02b34c | -9.30469 | -47.37795 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfa1bce7-ba8f-30e9-a734-dc806c01806a | -9.4461 | -50.8989 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 03ea17e4-0aa0-3553-92b3-9101728b333b | -12.85211 | -46.98793 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cd305619-190d-3ba5-ac4c-5a60a0efecdb | -11.24871 | -47.23093 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f7e46678-6425-3161-9171-fdf7c0599262 | -8.88152 | -51.68414 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43dfd9ba-3d55-36b5-9cf9-a3690eb2fb2b | -10.07073 | -50.21721 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 280ca7ed-d8b8-3a4f-b025-632d43ed68ac | -13.80777 | -47.96842 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6951bc35-d0ae-3b9a-b854-a60678506ad5 | -11.89041 | -48.04858 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d95e48bb-8501-350c-98be-e567ca8c4106 | -10.18522 | -44.8979 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb06e968-6894-3c7e-82e6-94821869a3bd | -13.57446 | -48.05751 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f368b10f-1e9f-39ab-8ebe-2a2c21a6b379 | -10.95545 | -46.48058 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 200dac93-53a3-3951-9a9a-1960e1f1dc50 | -11.94568 | -47.89408 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98f70cc8-3abb-3397-94ae-77fdbec1e0ba | -11.89162 | -48.04052 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7382f470-4ee0-378f-b3d3-f6b8f038434d | -8.14862 | -46.38042 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9b017bc5-a8a6-3c9c-b6a9-22ec4d28b15d | -11.88457 | -48.03942 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 358993ce-002b-3966-9253-f82b291b45fa | -9.51482 | -47.69193 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adb6c5dd-a156-3991-927f-9582416d5d10 | -10.88016 | -49.40151 | 2025-09-30 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ab1ac7b-7987-3cb8-b4d7-b2b75714ff61 | -7.91894 | -48.18258 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81e71fef-727b-34e7-9a52-37d6b5d090d3 | -7.52169 | -45.44323 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4e574c0-83c6-3950-b45b-80fc712fa168 | -9.12901 | -47.62886 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df3dea54-4752-3ccd-8440-1ad84429a1fa | -11.70527 | -47.83044 | 2025-09-30 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef475609-79bb-3d0e-a8f7-efeca5df4249 | -10.75957 | -45.37801 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7d7adba-208d-3783-863b-7b7c822622dc | -12.8314 | -46.99887 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3bc29bff-4f2c-3847-8837-955d8d8d6d47 | -13.75608 | -47.9166 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README66.md)
