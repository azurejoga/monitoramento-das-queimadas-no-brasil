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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c9e3ab-52e5-391f-8950-9a12deaa78f9 | 0.11862 | -49.84776 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67ae428c-0716-3f5d-b50f-f1602ebb482d | -1.68819 | -54.26631 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13df9c1f-7e78-3009-9fa1-6f2eb8b17d6c | -3.97293 | -45.80877 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fffe2bc-08d1-3a17-8b8b-f6c2bb19b751 | -2.13497 | -48.11966 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf47f041-0a1e-35cf-b41f-caeb17f1ab04 | -1.58939 | -50.44008 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea80f3b-9838-3012-bdba-57ba686b253d | -1.63503 | -53.27664 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dbb5db0-e5b3-3e5d-bb2e-d1cb5ec56096 | -3.89465 | -46.47911 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4225ded-6bfb-3758-9b06-20cbaea568c0 | -3.87791 | -45.02411 | 2024-11-16 04:48:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 50c894b9-5993-3ef4-8937-06368fcf52de | -3.99221 | -45.85917 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db25a2d0-3d7c-339a-ba83-a90b301568d5 | -3.98849 | -45.85427 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32058e3b-4938-30c7-a2a8-115cbfc33971 | -0.25619 | -48.5153 | 2024-11-16 04:48:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3ce4f56-92ca-3b26-83de-2c537729e288 | -2.55321 | -46.89663 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42b4e1e9-011b-3507-b561-2a063a9d508d | -2.1798 | -48.55232 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db0a6104-3efd-3453-86d1-dc412c07efc8 | -1.12794 | -47.16729 | 2024-11-16 04:48:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99e05443-8feb-3786-8ed7-a1d79535d91e | -2.35791 | -47.14725 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ad32b9e-cc36-3697-ba2f-edaad1983f6f | -2.15501 | -48.78148 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 093fa06e-4a5c-380e-9a1a-6b981b936c88 | -2.34463 | -47.46612 | 2024-11-16 04:48:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 58f60438-db1a-333e-b06d-d737b9c84ae9 | -2.08533 | -48.94997 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c41d1089-1aaa-3f05-9762-f2bda12b2123 | -2.28283 | -48.46949 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec571da-52b7-37ad-a55e-57f0cc64a6d6 | 0.12255 | -49.82899 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ead451af-eb34-311a-a773-7de8641baa16 | -2.5503 | -46.88912 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbea1cd9-4814-31d7-a408-338322eb7631 | 0.15889 | -51.14031 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93226db6-7519-3021-ae7a-bd9c40239a84 | -2.88216 | -40.39687 | 2024-11-16 04:48:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63fe845b-9b88-3965-a1f9-47e414e1d616 | -4.03266 | -44.10865 | 2024-11-16 04:48:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9afce1ad-33ae-3561-9246-538ff99ec980 | -3.34912 | -46.42692 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1faf630-30d5-34eb-a009-b1ec6de70aeb | -1.68727 | -48.46639 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7173a7b9-903f-3fde-9443-265307a14098 | -0.25329 | -48.51081 | 2024-11-16 04:48:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d089b5e-1329-39f8-8bba-c4d21ed687b2 | -4.22621 | -44.04765 | 2024-11-16 04:48:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bfd4b89-23a2-3dd2-9181-6f94e4539da2 | -2.08328 | -50.49445 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed1a2a68-a921-3ef9-8e4a-225087237555 | -2.175 | -50.47217 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 491ba39f-10b9-3436-a922-9f3594887be0 | -1.13118 | -54.17075 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65601ef3-2b21-33e0-afff-21a64721badc | -2.23057 | -53.61228 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e1aad519-eb5e-3982-afad-9c650d462b4e | -3.79101 | -40.99637 | 2024-11-16 04:48:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0ba55662-539f-383d-9170-4e2c43d15e3c | -2.66735 | -46.18585 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ed0a384-52ee-3686-8d9b-31cd061ef9d3 | -2.11712 | -49.11507 | 2024-11-16 04:48:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ce2350c-94fc-3828-8b53-cb5267d4e71c | -2.74002 | -48.55936 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6fe8ee9-ff20-369a-98cf-6f1aa516c22f | -3.49626 | -47.20651 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef33323b-8253-3d0e-843f-3812a24f0c90 | -2.77124 | -48.57981 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 71588bc5-5e4b-3331-bea0-48c274293b82 | -3.73413 | -45.66035 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ae2659e3-c2b8-3217-8e6e-56edcee06072 | -2.36743 | -48.52791 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82aaccf9-bca1-369a-a20d-2be29787e53c | -2.37442 | -48.55442 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f8b8a06-dc04-3844-802f-6fe253ab26c9 | -2.57513 | -54.42809 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e59ae14-f766-3632-acfc-c112b3042e54 | -4.01609 | -38.25002 | 2024-11-16 04:48:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6640cbac-614c-35ee-b9d0-cc43f162b5f9 | -1.89348 | -47.01034 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dd27ac1-3da5-37e9-8e15-6b4ea2cafd67 | -2.1523 | -48.53967 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceae1cfc-3af8-3bff-8514-8e1a1ad2a701 | -3.19764 | -45.54971 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 9cae03da-770b-39cc-86d7-198964cec9f6 | -3.94338 | -46.70485 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e964b35b-e0b6-3c08-bba7-a9767424de7b | -2.36383 | -48.52736 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c9773b3-7742-399e-a388-3b32653ba6cb | -2.792 | -46.64528 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2ea219f-76b7-38ac-b6ab-a63ad5961c73 | -2.19703 | -46.34613 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b3711e6-5ac2-399b-9927-4dfce02b1c8e | -2.21968 | -47.21412 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b28a4b0e-d931-32c7-8ed3-b3d37f6596ba | -3.20731 | -46.67832 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04a39c16-b599-3b0a-a5c4-c1afebae939a | -2.47605 | -46.36797 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaf7254e-e749-38d3-8570-f1f4863ca6c8 | -2.1319 | -50.81339 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7036dd8-a3d2-35d6-9691-f7ddd9593287 | -2.22998 | -53.61598 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b4fc477-640d-322f-8d29-bb473e54ab5b | -3.96918 | -45.80386 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42b845c5-d32d-366a-a255-de314348f8f7 | 0.69549 | -51.44252 | 2024-11-16 04:48:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39dfaabc-98fc-3333-912d-df12c02eeb75 | -2.39122 | -47.94012 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccbe759f-f723-3340-8d28-f474778d4bcf | -2.29692 | -49.00912 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f34bbc-cfc9-336f-a19a-6d14bd509b8c | -2.5799 | -54.42074 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afeb9a16-6923-3936-9f40-a47f5487b3cc | -2.09029 | -50.33992 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc9a13c-b2d4-3f89-abed-1b9f5468dec9 | -2.1762 | -48.55177 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b25683bc-669c-3eb8-8a0c-fa286508aab9 | -3.74308 | -45.66037 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 294fb2ee-381e-33e3-96ff-1fb955b1304e | -2.8147 | -46.65973 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817a9375-9c60-3b45-b713-f2c566e10e63 | -1.68882 | -54.26236 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bf2871b-372b-34ac-a4e2-0d0e34c02483 | -2.02597 | -53.94747 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f169644-ccf6-3409-b7e1-1d55b448895b | -2.81876 | -46.66035 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4ffc66a-699d-3915-a02d-cb37fbfd0df4 | -2.5555 | -54.03484 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6bf1475f-983a-3529-a16f-5abd0ec8952c | -2.68025 | -46.8278 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2846f181-65e2-31c7-9bd0-f5b99d9bdd9f | -1.94086 | -50.64491 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b8aacb9-b0ba-3830-b952-df7199830eb8 | -2.20449 | -46.04791 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99b67148-5583-3170-ab0b-5128a3a389fe | -2.11102 | -48.27377 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd80a086-61e8-3204-8ac1-14628d964781 | -0.78398 | -49.47979 | 2024-11-16 04:48:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10c9845d-4c23-3620-8d87-e14e9ce2d4c5 | -1.57827 | -50.44555 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19b0c607-5c2d-3c99-81b5-3bb660e6eafa | -3.98767 | -43.71953 | 2024-11-16 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 706d3f4e-a001-3d40-b006-4fb60c5442d3 | -0.81291 | -49.51807 | 2024-11-16 04:48:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0745a59-c3cc-3efb-84cc-d55f962e412c | -2.63916 | -45.97512 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66f936ac-2181-3c1d-b5ca-74490545b675 | -3.78532 | -43.91451 | 2024-11-16 04:48:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57ee2b9b-520f-32bc-ac73-55045aa34095 | -1.21123 | -53.56375 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b2c2689-e4ad-3a35-891a-f10e5f854649 | -1.16044 | -53.50562 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0c25785-00ea-3bd1-a979-fd7a9739d478 | -2.35381 | -48.42326 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 550feecd-a911-33f9-bb57-74e1f4752528 | -3.74362 | -45.65728 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a62f4069-06ae-38ff-ad3b-52bda42f7cae | -0.63919 | -51.72945 | 2024-11-16 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 070d5c1f-6cda-383e-8473-d86219f04476 | -2.22053 | -46.35713 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c332536-3e84-39d7-b467-610d67cc0872 | -2.93705 | -48.3263 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4f9f5d7-bb57-3be8-a2d6-6794da9f2f39 | -2.30942 | -48.46512 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e4a17d1-e951-3012-8146-11351f211f85 | -1.21817 | -53.56075 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e42f12f0-1bb4-38e4-8b0a-7d114bbbddf5 | -3.97687 | -46.70604 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8adbd1b2-ccf7-3f46-a32f-93c1fa7fc7ac | -0.106 | -51.27305 | 2024-11-16 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a262134-9de9-382a-b590-392cd05b582a | -3.28231 | -46.21098 | 2024-11-16 04:48:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 392bf6bb-64c1-3da6-8cae-d8c81fb46371 | -2.15537 | -53.7123 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be5b1375-b81f-363b-aa49-3b579d239fba | -1.85619 | -54.2804 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45fb8bba-6fc3-3576-9932-91e47b0fbdb7 | -2.62913 | -46.18409 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd7f1a08-abaa-3c96-9741-688ed7f9cb5e | -0.78682 | -49.48399 | 2024-11-16 04:48:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdef9567-c77d-3af0-8c54-f58a97bbb53f | -3.1983 | -45.5454 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 2d781204-aae0-3920-af4d-7c67d9316dcb | -1.57937 | -50.43853 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1aeab4e-502c-3d13-b14b-60456a6cc809 | -2.67094 | -46.19025 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cf3b63d-e597-3655-a18e-145b9d9660a6 | -2.08383 | -50.49093 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a20a2d19-845c-3a1f-8362-5a0a82f47ec3 | -2.17999 | -47.95217 | 2024-11-16 04:48:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f33ee75-7f88-3be1-91a2-943a1778bb49 | -2.34846 | -47.46671 | 2024-11-16 04:48:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README44.md)
