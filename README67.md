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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f2010ae-fd9c-3c63-b302-8ef143160d70 | -17.07058 | -56.0009 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 32b31db6-cc68-341e-81b0-6a50c1184b40 | -17.06974 | -56.00562 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e8f9f5ef-2338-385a-a470-83284a7a1cfa | -17.0689 | -56.01036 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 66f544e7-b9d1-37b4-9549-70ca22846575 | -17.06805 | -56.01509 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e103b8cd-6ab9-3e83-afc2-e5fa428392c9 | -17.06767 | -55.99547 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cc561bd3-0f2f-3700-a112-7731ffd9495c | -17.06759 | -56.03948 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9e24e225-1567-3ac5-aa48-611426d2973a | -17.06721 | -56.01982 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 06d28fd5-831a-3e31-ab93-e4516b49ad1c | -17.06683 | -56.00018 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f2eae1eb-3fea-347e-a33d-b69aaaea2648 | -17.06599 | -56.00491 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 095fd7b4-acda-3a4b-89f2-ca78479a2cd4 | -17.06468 | -56.03402 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5e330198-e551-3c64-8adc-e1818f3933fb | -17.06384 | -56.03876 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cccb984f-b960-36e8-b9bc-527b06dbac11 | -17.06008 | -56.03804 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 68c46417-580d-32ea-a89a-4c6b9f70b8d6 | -17.04556 | -56.0108 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 525882b1-e79d-3015-b54a-a3c83a43c19c | -17.04181 | -56.01009 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c646e3b5-afe1-3feb-acc1-fee6fe6d61b9 | -17.02799 | -56.02214 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 828db501-167d-3e20-95ca-8e691ea91a6d | -17.02724 | -56.0242 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8dc9a2bd-9292-3fd8-80f8-d48cf7768aa8 | -17.02714 | -56.02688 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 01dd4e8e-d668-3390-a666-a644a83cfffe | -17.02641 | -56.02896 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 029d30a8-0098-3670-bee1-f5328ce2424d | -17.02424 | -56.02143 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f319b186-12fe-3e6e-98df-8d35a231fabc | -17.02349 | -56.02349 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9bf4a240-eb3d-358e-977e-153d14de374a | -11.9028 | -56.2114 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7f4b9dc5-6994-3746-916b-e92ae3027748 | -11.90212 | -56.2152 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad4dd3c2-26c9-3c14-983e-394e44e4d5bc | -11.89869 | -56.21066 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71906bd0-64b7-3495-b4ad-2a9753c1c62c | -11.89801 | -56.21444 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0d5f4d7-1319-388a-a5a6-5949b086ae88 | -11.89734 | -56.21822 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8135104a-5de2-3fc9-b0f7-f01fec8cda62 | -11.89666 | -56.22202 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4846ba55-68b3-386f-9a91-807a1d550f2b | -11.89457 | -56.20993 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6e0fc57-c245-346a-992b-52a1ac49c19c | -11.8939 | -56.2137 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6ce604c-747f-3db6-ad98-114de0f11e04 | -11.89322 | -56.21748 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fc1d031-f8fd-3b28-8e18-7755b1a319e5 | -11.89255 | -56.22126 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b80b8452-61b8-3366-8684-980ff8387084 | -11.89186 | -56.22509 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ac0883a-4c48-38d2-b52d-ce0ee2f8df7d | -11.89113 | -56.20545 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23915b86-2a1f-3042-88de-f24472fba0cc | -11.89045 | -56.20922 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6d8fc7a-4bc1-35fd-80d3-77586d6825c2 | -11.88911 | -56.21675 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6dd920a-f315-33d9-bb1d-6cb5a204390a | -11.88843 | -56.22052 | 2024-10-13 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac7fd010-9089-35b3-bb7d-99c065450c5f | -17.17478 | -57.46149 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cb88d905-1b74-320b-8938-b9e9ff64a398 | -17.17409 | -57.46529 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f015e897-8dca-3e36-8407-c5127a6c5020 | -17.17339 | -57.46908 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 003ae01f-6ad1-3c19-b952-440e5653bd84 | -17.1727 | -57.47288 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6afc8f78-0a52-3007-8f1d-ac8cae6ff6f3 | -17.17201 | -57.47668 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d13acdc5-a23c-35a3-a97b-d955bc3ccfa9 | -17.16862 | -57.47207 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 77c7945e-91cc-3c66-9c4f-160dbda5b066 | -17.16793 | -57.47587 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4a8bf301-cd18-3911-a5fe-4101c450178c | -17.16723 | -57.47968 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4b76fcc1-9ad4-3bc1-a36a-b1757e20ac7b | -17.13937 | -57.4702 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 33d06b60-927a-371f-a371-30bdc608e5e8 | -17.13529 | -57.46939 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| b063584d-04e1-36dc-bcb0-d01901e74b8b | -17.13459 | -57.47319 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1ff49e1a-5d6e-3eb1-aa12-678aae356773 | -17.1305 | -57.47238 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3605b5f9-1f4e-32ce-bb82-1c688d2191e3 | -17.12164 | -57.47457 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6f9add6f-3d9a-3132-8efd-be9eda22d4bc | -17.11755 | -57.47376 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 418e9dd5-3843-3d1a-a9a6-871e31de7a93 | -17.11684 | -57.47756 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4119561c-3373-36aa-bffd-30f7c88c09cd | -17.11418 | -57.46914 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b1452f0f-f912-3bd8-ba2b-9ea823827b60 | -17.11347 | -57.47295 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c1e61c17-8915-3e43-82bb-5bdf39b9ee4a | -17.11276 | -57.47675 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c672e09a-1332-3f4b-b0b7-5e15419b49b0 | -17.10939 | -57.47214 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 35318261-4643-3d3e-b2de-a47045170dcb | -17.10868 | -57.47594 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5ac0673b-67a6-3190-b25d-6a5450eb9f1a | -17.06866 | -57.4449 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d8016c55-e98f-3b47-ac84-058559b05203 | -17.01493 | -57.43821 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3aceba1d-6084-3986-978c-6366460831c5 | -17.01422 | -57.442 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77d394eb-fdf1-3eb1-9c7a-58b87e0c4af0 | -17.01014 | -57.44119 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 95487b2c-f7b6-3f90-9f32-824c5d618597 | -17.00943 | -57.44498 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 429b674e-0a0d-3aa6-8e43-b5b7dd05e052 | -17.00872 | -57.44879 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4604220b-31d4-33f7-8d9e-89d31e2937c6 | -17.00818 | -57.42901 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4599ad38-df94-34d4-baf2-f37476052a6f | -17.00747 | -57.43281 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| cf1d4582-3e86-3ef3-bc39-2730f0f61d94 | -17.00677 | -57.43659 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 5f831678-4809-33ad-b984-9c59a9fca09b | -17.00606 | -57.44039 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| e449c8d5-ded0-350f-8d21-db3a71a2a358 | -17.00535 | -57.44419 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| eaa953cf-95e8-3e70-a5c7-e3371c4ae32f | -17.00463 | -57.44798 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2150bb5a-5cba-3500-bc9a-031ca503a6ba | -17.0041 | -57.4282 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 671ad522-310d-3266-ac18-0e776cd451e3 | -17.00392 | -57.45179 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2d00e009-44d4-352e-bce9-274287a5ae84 | -17.0034 | -57.432 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e0cfba63-4407-3471-af03-2a029cc26af5 | -17.00321 | -57.45559 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0c1c73de-241b-3d7f-bcfb-108a06d5d437 | -17.00269 | -57.43578 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0c549131-b197-31cd-b5c8-193dd5983e84 | -17.0025 | -57.4594 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8d643b7a-cb45-349f-9893-3d33a8aa2f63 | -17.00197 | -57.43958 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8a86281c-4c2a-3beb-80df-edc75c2b28e5 | -17.00126 | -57.44338 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2818aa0b-d0b4-3fb0-b331-cd9abd5d7cdf | -17.00108 | -57.46701 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dfbbb0a8-5e2d-3d32-b3fc-1e93a719887d | -17.00055 | -57.44718 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f5ac6286-a2da-3955-8334-40d11162276d | -17.00036 | -57.47082 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8ccf5299-a516-3505-8409-6e72fb15db88 | -17.00002 | -57.42741 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3adcafc2-5bca-3207-b0f5-15fe2dd9735f | -16.99984 | -57.45098 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c1606764-7e6e-36ce-a02c-186ceb6fb437 | -16.99965 | -57.47464 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5c0d1d44-5b4e-39cb-932b-25814a8d09cc | -16.99932 | -57.43119 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 52880e66-77a9-386b-80b5-f74a37a9372c | -16.99912 | -57.45479 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| be85bd7f-ece0-3f3d-8e21-42e4c8b2fa51 | -16.99861 | -57.43499 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 671c7644-b4ec-3e7b-813f-91b73c706097 | -16.99841 | -57.45859 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 73bdbdf9-906e-35ab-b68e-39c8c9a0d45b | -16.99789 | -57.43878 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dbb64c18-98b3-3c9e-bf2e-bc723aec7f97 | -16.9977 | -57.46239 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9c0dace4-ab01-37bf-ada9-473e57dce637 | -16.99718 | -57.44257 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0ac8f760-68df-330f-bf63-27a35427d042 | -16.99699 | -57.4662 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ab9fb6e6-796b-3bac-9891-93f8cf79dab9 | -16.99627 | -57.47001 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 810f4c39-a6a3-36cc-bdef-a26e315fefca | -16.99594 | -57.42661 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| edb7ae77-f284-37ed-8f6d-6a4e1589f404 | -16.99556 | -57.47382 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5a102c3e-1c57-36cb-bf4a-87d321939023 | -16.99452 | -57.43419 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8f191851-3693-3842-93e3-7d74215c576c | -16.99381 | -57.43797 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e5db9892-991b-3c14-aeef-d4e42361221c | -16.9931 | -57.44177 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 51dfaff0-ed24-3867-a671-03d3260af3c9 | -16.99239 | -57.44557 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 09ba47c6-43bf-3bdd-822e-a93a2b2ab04f | -16.99003 | -57.48065 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2f3d8865-52f9-34c8-8e6e-c8c0b4e63ec5 | -16.98932 | -57.48446 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 967b2b27-a0aa-36a0-b0b0-38f859fafac2 | -16.98594 | -57.47985 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| ce2fe3c5-dd5b-3854-8f95-0056f33a7143 | -16.9859 | -57.43981 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README68.md)
