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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ff5338d-8149-381e-bcf9-24bfc49e0c56 | -12.3074 | -57.3608 | 2025-12-16 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 679eb5db-9d5c-3e4b-a473-5b9560e8593e | -9.5316 | -36.0053 | 2025-12-16 02:10:00 | GOES-19 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| c23f9dd8-cb27-3454-a81c-04093ce3f4a7 | -12.3072 | -57.3808 | 2025-12-16 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d1d2024d-6f46-3e80-aab1-40a75aa7708c | -12.2885 | -57.3624 | 2025-12-16 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 52dc185e-748c-3325-a293-5d735ce57d8d | -12.2885 | -57.3624 | 2025-12-16 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 243ee604-ffae-3c8d-b096-21d8be191617 | -12.3072 | -57.3808 | 2025-12-16 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 917ce2c7-f72b-3e12-bf54-1f0603241e5f | -12.3074 | -57.3608 | 2025-12-16 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 6b75753e-cb04-3cdf-a597-b842284f8eb5 | -12.2882 | -57.3824 | 2025-12-16 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b6ac87b2-e0d3-325b-8bca-a167bc0d380a | -12.3074 | -57.3608 | 2025-12-16 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| a53f07b3-50a3-33c8-bb8f-98ab4686d666 | -12.3074 | -57.3608 | 2025-12-16 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7827056d-5795-3a93-a19e-7e325f4397cd | -8.0696 | -43.1452 | 2025-12-16 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 3ec916b6-7a2b-3bc2-8cdf-7fc238691c4a | -12.3074 | -57.3608 | 2025-12-16 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 96928b31-f13c-3f67-b97b-5dd7f1a8e5de | -6.5631 | -51.1126 | 2025-12-16 02:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 25dc195c-749d-3211-9d2f-05e9dd0b2d57 | -12.3074 | -57.3608 | 2025-12-16 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4803f3e1-5db2-3b9e-9879-9ec3e3193ed1 | -4.90223 | -37.43679 | 2025-12-16 03:04:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4df07140-356f-3bf6-8e03-ca034e9439db | -5.78428 | -35.36907 | 2025-12-16 03:04:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7ddc00ff-7992-34a4-96ac-aaa96cbba7de | -5.78912 | -35.37392 | 2025-12-16 03:04:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 344bbd8f-bfe8-3a0d-97b5-c93519a45a67 | -4.90316 | -37.43158 | 2025-12-16 03:04:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 005d0516-cf0a-3460-b2d5-4b92936f3ea3 | -5.78365 | -35.37265 | 2025-12-16 03:04:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 794e95b1-ce54-32aa-9283-b27e99bb8c13 | -8.83431 | -35.68173 | 2025-12-16 03:06:00 | NOAA-20 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e5dc5cb7-9a8f-3fc4-8696-5f642944734b | -7.45322 | -35.20817 | 2025-12-16 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b7b65b7d-64a6-34ac-a1a0-48630f47f98e | -7.46033 | -35.19914 | 2025-12-16 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 53e21cae-6ba1-387e-a9ff-51ba245a1bec | -7.45443 | -35.20146 | 2025-12-16 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5ad95fee-8c67-3dc1-a9e8-db25ca5ba416 | -8.83701 | -35.68245 | 2025-12-16 03:06:00 | NOAA-20 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2f0d935d-993b-3ba1-a760-a3b02d6a9720 | -7.45852 | -35.20919 | 2025-12-16 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 24770111-a2d4-3eba-8957-0ce3d5241fce | -7.45564 | -35.19476 | 2025-12-16 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 969e7657-fa72-3fd9-aa90-ca1a83045ee7 | -7.45503 | -35.19812 | 2025-12-16 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ae54f99f-5b4b-3e39-9e62-714fc1aa3c2a | -7.46094 | -35.19576 | 2025-12-16 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 805388b4-8b11-3ece-a738-35c2aae5a79d | -13.25894 | -41.3139 | 2025-12-16 03:08:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1f5f951f-5d4a-38dd-8446-94e319d495d9 | -15.45999 | -39.16172 | 2025-12-16 03:08:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2fc784ce-19fd-32ef-b145-11136b95f719 | -15.46092 | -39.15729 | 2025-12-16 03:08:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a660798b-9edf-31b9-b0e0-52eaed78718f | -9.457 | -35.8825 | 2025-12-16 03:20:00 | GOES-19 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| eb195d6f-d768-3b20-a333-420572e3680f | -3.1267 | -45.4985 | 2025-12-16 03:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8af33b43-0d13-34b7-97b5-e2e1a39cb02b | -3.6543 | -38.74643 | 2025-12-16 03:53:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dc08e670-3623-3ad2-84ac-51c17bf0bdd3 | -1.67365 | -45.80368 | 2025-12-16 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a14fff69-0f8e-3fe4-880a-945fd17b7b4d | -4.24778 | -39.23425 | 2025-12-16 03:53:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee2f68c0-290c-37d3-b3e2-33b86ae2f8c8 | -3.31545 | -40.02708 | 2025-12-16 03:53:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3a2bdce-ce54-389d-872e-81a9bdd9c6ae | -3.24948 | -45.35782 | 2025-12-16 03:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a907840-b82d-3a5c-826f-35572657bd9a | -3.432 | -42.34641 | 2025-12-16 03:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 77d1b6c6-148c-35fa-af79-d9b575f4b005 | -5.78914 | -35.37411 | 2025-12-16 03:53:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6d7cdc2-bca4-317d-9b78-ef1da043ab49 | -4.65894 | -42.39941 | 2025-12-16 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 894ac31b-ba10-36fc-b997-bfc5a262f193 | -3.64733 | -44.2597 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37cb4deb-a851-3b6a-8221-cad62beee23c | -4.2498 | -39.23459 | 2025-12-16 03:53:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 311df51e-bf4c-3f52-8221-d3320d173f39 | -4.40286 | -42.3354 | 2025-12-16 03:53:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 07e69ac6-844a-3672-b318-ec9a40d4fdc3 | -5.02538 | -41.27977 | 2025-12-16 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a2424f4-1938-3adf-b7f7-31425d6938b7 | -5.72515 | -39.07391 | 2025-12-16 03:53:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1cc7da7b-79eb-3277-9daa-5f179e033f01 | -1.92291 | -46.5007 | 2025-12-16 03:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d009457b-6882-32fb-a2f4-9e76e7a53c0a | -3.6541 | -44.2523 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ae4fb50-15fe-3158-b3be-80d385a22292 | -3.6488 | -44.25095 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34eee67c-443e-3b6d-9cd2-43c3fcc9358f | -3.65339 | -44.25668 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 668c24b6-ea7a-3c9f-a4af-5f1c2faf47cb | -3.3551 | -46.86244 | 2025-12-16 03:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c712d24-c700-3b12-af08-c4700c03f071 | -3.64381 | -44.25963 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17e08c94-e5e5-3fd6-aa64-45641f6fbff7 | -4.9048 | -37.43092 | 2025-12-16 03:53:00 | NOAA-21 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c031c2dc-b309-3ddc-8c54-bb9d13835896 | -2.96656 | -41.58336 | 2025-12-16 03:53:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcbfd42b-04dd-3122-8cac-ecde4c07d8a6 | -3.4287 | -41.65297 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| c909be9c-98a5-3c3c-81c1-3a331960cf98 | -4.08008 | -40.27806 | 2025-12-16 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2eeaa26a-a2e8-322f-b0c5-663f4a2fc75b | -3.43281 | -42.34145 | 2025-12-16 03:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b8e5618b-bf67-3ab1-bc5d-c5eda949779d | -5.55779 | -37.75697 | 2025-12-16 03:53:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86d4416c-dff0-3802-bde0-79ee7d350566 | -3.64807 | -44.25532 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0645a86d-77b7-3081-84c5-e69c32346f44 | -3.35568 | -46.85902 | 2025-12-16 03:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e200ccd-05ae-3a30-8e0a-41ac5021cee0 | -2.96279 | -41.58278 | 2025-12-16 03:53:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70a6eb61-b4f3-38f1-b12e-5b118698822d | -1.67143 | -45.80474 | 2025-12-16 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74bcef65-8853-34ad-8c99-2a48f1811c57 | -2.50499 | -48.03769 | 2025-12-16 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 796270aa-930a-3f15-a9d5-44715e87b433 | -2.50434 | -48.0417 | 2025-12-16 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5605a7a-e244-3b8a-9d52-083ad765e3e2 | -3.64523 | -44.25085 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c63bdf27-226e-35df-b9ab-bd4db1e4af0f | -5.1808 | -40.1524 | 2025-12-16 03:53:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e8b0816-71ea-31d8-ac2d-1ebf2944c0e0 | -5.02469 | -41.28396 | 2025-12-16 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 506f13b9-3230-3305-b472-97955bda9496 | -1.60606 | -45.89838 | 2025-12-16 03:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82defb6b-0d9b-30b1-9d8a-2f01b31a2514 | -5.02477 | -40.36049 | 2025-12-16 03:53:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4309be3e-fffb-327e-9d31-2c04465cfaad | -1.61119 | -45.89923 | 2025-12-16 03:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ead28799-f5ac-3d32-afc8-3adecdd766d8 | -1.67242 | -45.79879 | 2025-12-16 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a034715-ad8d-3468-9f37-a1dced006fc5 | -1.66855 | -45.80289 | 2025-12-16 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8627fbc-d2f6-39c1-a60c-69259a91022c | -5.08852 | -37.62685 | 2025-12-16 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c394963b-05ee-3b8e-8884-ec16af0f593d | -3.42487 | -42.46345 | 2025-12-16 03:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db52fe93-fec4-37e4-955f-7970912e4c79 | -1.8488 | -46.39446 | 2025-12-16 03:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d9f8cc92-8d14-312b-940f-509958fc8acb | -5.11471 | -43.28809 | 2025-12-16 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a25466bd-9dc8-3dc4-a276-619ecd3c022f | -3.43405 | -41.64805 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| cc8bccc8-d856-3070-9da9-5c8401e33651 | -4.40749 | -42.33118 | 2025-12-16 03:53:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e832692c-9d92-3231-abdd-7077f3acf3e1 | -4.90534 | -37.42745 | 2025-12-16 03:53:00 | NOAA-21 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7c0d1524-0dcb-3822-a22d-81508936d04a | -1.84933 | -46.39119 | 2025-12-16 03:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c77e0704-143c-3fca-b747-6ee93649d99d | -5.64511 | -38.67666 | 2025-12-16 03:53:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 664eba4b-652f-3d55-b1c5-cd3687b83d19 | -2.39471 | -43.28964 | 2025-12-16 03:53:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 829826a3-86de-30bb-b4b1-53cea3af8951 | -2.50468 | -48.0364 | 2025-12-16 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d677e1e-00d6-3aa3-9289-24e73fe99224 | -5.02177 | -41.27918 | 2025-12-16 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07c3d4f8-08fa-3b44-8140-a13686540e0b | -3.93608 | -47.00337 | 2025-12-16 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d756d7e-8ab5-329c-b8d1-e88ed5475e74 | -3.64896 | -44.25596 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46528665-5189-3080-87ad-f639b9e754c5 | -1.67192 | -45.80176 | 2025-12-16 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a61a0163-f632-362e-8e22-a7d1291c0926 | -3.42942 | -41.64841 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 85fa5c12-8785-3c72-8cb2-be535850b69e | -2.03114 | -45.80873 | 2025-12-16 03:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab5bd979-6da1-3c76-9ffe-c527addc8f14 | -2.03065 | -45.81171 | 2025-12-16 03:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 205811ef-2593-3aeb-8f7a-637544f0b846 | -4.41058 | -42.33666 | 2025-12-16 03:53:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cbacbca6-b025-3f15-b5c4-6f8c027d58b7 | -5.11816 | -43.29234 | 2025-12-16 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28c16af8-fe39-3dc4-9f63-a9f22704da7e | -5.60885 | -35.63278 | 2025-12-16 03:53:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0ffe9b0-a0a8-3cfc-9390-414a1353f7b1 | -3.43318 | -41.649 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 06326ef6-264d-31ff-93a6-fd62deef2ce9 | -3.43246 | -41.65355 | 2025-12-16 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| da823f0e-73cf-3cb2-911d-60ff79c853e6 | -5.32432 | -40.55223 | 2025-12-16 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 11f2241b-1946-3f3f-9dc6-d559ed3bf9ad | -5.33856 | -40.96274 | 2025-12-16 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7cb87e33-dbd4-3f12-af94-c609e671ba3d | -4.90866 | -37.42796 | 2025-12-16 03:53:00 | NOAA-21 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6d731afa-6983-348f-80b7-ef86a2cb6db1 | -5.78618 | -35.36956 | 2025-12-16 03:53:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 393665b6-a193-3df5-bfd0-f9361f1019f8 | -3.64825 | -44.26036 | 2025-12-16 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README5.md)
