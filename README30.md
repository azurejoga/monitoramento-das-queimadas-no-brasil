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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1123c21f-b4c7-32d2-9565-50c02d0576a6 | -7.80336 | -44.8975 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53a583ca-575d-3731-93d1-75c27507fece | -3.70663 | -54.1726 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94eef3d3-82f3-32b8-abcf-c916406673f3 | -3.53402 | -42.66739 | 2026-09-18 04:19:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 479da1d2-c03f-3871-9bd1-33758c12f07f | -0.61754 | -48.6016 | 2026-09-18 04:19:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f628f78d-fff1-32e1-85eb-69e87a3faedc | -7.84168 | -44.87168 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 036a98b5-63aa-3a86-99c4-0418fe5efd10 | -1.78872 | -47.83279 | 2026-09-18 04:19:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b342348c-02ad-3ef0-ba9e-d6ea8f355adc | -4.53744 | -54.93084 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75dcd7df-2c93-34e3-a8c9-5ebf98628df0 | -2.95985 | -50.32228 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bba6124-2ce0-3ea7-a30b-06465344554c | -7.15986 | -47.50123 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d07f430-08dc-3172-99ef-1f481a120da2 | -7.86627 | -45.1486 | 2026-09-18 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1546dd54-0fee-3be9-8fd1-90687d8bc08e | -3.37578 | -50.45736 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 955de237-f7d3-387d-89e5-4e06d1c18fd6 | -4.43684 | -55.5233 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57e54952-c656-33d8-bbd5-0f3af4e8b763 | -7.39265 | -44.49888 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76dc43b1-afa5-30b2-b732-1822c243e8a7 | -7.57566 | -46.34824 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb340c7a-1c6b-35ab-8b14-b131a7ea62b4 | -5.73305 | -51.75118 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aa5ebc8-17e0-37d9-b7df-fb8cdbc6855b | -2.96652 | -50.33624 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb8ad1d-8220-3708-9e9a-ad776c9e78ea | -5.65113 | -43.20325 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b5681aa4-8c5a-3657-aca4-9a9b01730d1e | -7.81381 | -44.8956 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4251592a-0953-378c-9af1-18fd6bc5f032 | -3.54384 | -45.31251 | 2026-09-18 04:19:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c0a10ac-cec9-302c-8b87-d877aa82e8ca | -6.37408 | -43.27205 | 2026-09-18 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c09e89da-27ee-371b-881a-fd68fe9f8806 | -2.96353 | -50.32714 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3abaa5bf-a6e3-3d74-acc8-5472d4b10c2e | -3.41008 | -39.28715 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3f38984c-8ec9-361b-894d-a83f5153a1ca | -7.82014 | -44.81133 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e79a305d-256b-301c-8691-3a6cfb773983 | -3.70793 | -54.17682 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 248dd953-e63f-3a1e-822b-dabad93dc4e3 | -7.00182 | -43.6367 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 39b7c642-a6f2-3e8d-b096-b42921f6f7c1 | -7.34658 | -43.89032 | 2026-09-18 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecaf3573-7d94-36ab-a78c-f610eefdeb5e | -5.7559 | -45.09386 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f23c79e9-6836-3ddd-af79-3a692c6bdaef | -4.67982 | -40.1381 | 2026-09-18 04:19:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7ab1be77-f8fe-3d05-86e8-02ebecb148dd | -7.55541 | -45.67849 | 2026-09-18 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f35a61cb-8837-3e37-bc78-fe35831a103c | -7.00463 | -43.6408 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3c3bdce6-a30f-34ab-80a3-017585c2160d | -4.55513 | -42.96593 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad1a26a0-c25d-3dfc-afce-2493882b7f2f | -7.74869 | -44.67945 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37611aeb-f24e-3b61-bec3-0685b7ead4af | -4.37149 | -55.4226 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71ee54a0-32a6-355b-80c7-7de2dd42cd47 | -5.14395 | -47.6038 | 2026-09-18 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 563b98ee-b38a-3070-b8ae-61d97733bda3 | -4.36424 | -47.78255 | 2026-09-18 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 311e8682-1640-362c-b46c-d87528c79ec4 | -6.20771 | -45.33518 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5909676b-ef25-3d36-8bd7-5b73240705ea | -4.56235 | -42.94126 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eec05ae4-a132-3ca1-833a-285923fbe0f7 | -5.2238 | -49.32867 | 2026-09-18 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e035e30-0961-3f49-9c77-598d14d007e0 | -6.34748 | -43.37873 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 72b945d7-33d6-3154-af97-263991c127b9 | -5.14104 | -47.5991 | 2026-09-18 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30985c4f-4fcb-33ed-8d7e-8a0c1d242b7c | -4.37926 | -46.24408 | 2026-09-18 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7676892f-21b2-38ce-b6a8-fa91f076daf6 | -5.57948 | -42.73219 | 2026-09-18 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 76e50d06-174f-3466-8edd-81dee2bc74fd | -7.06096 | -46.22559 | 2026-09-18 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3d6f89dc-7698-35cb-a601-c45c3f651356 | -7.05705 | -46.22861 | 2026-09-18 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d032fb91-08a9-37b4-8cbb-47d998e3c9d3 | -6.03659 | -43.68156 | 2026-09-18 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 532b7018-bb18-3ad1-9161-98f4c074621d | -3.35898 | -50.45034 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5265d46d-5875-3b7d-a460-779e3e5fb996 | -4.59105 | -42.9567 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| cb303d9b-8abe-3794-a156-65ac48bf6850 | -6.77362 | -42.78657 | 2026-09-18 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a19c256-000b-3ce0-a533-878711a1a236 | -1.21318 | -54.22503 | 2026-09-18 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 574b3f1c-7033-3cb2-8cee-b4efac38b61e | -7.0583 | -47.47766 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 281d2dba-a598-3ac7-bc15-d73d42df4ad3 | -6.91366 | -41.72232 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 242f695b-9837-335c-90d0-0732b3817dde | -3.37141 | -50.45667 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3db0c55c-94c4-3795-9a89-df450d7c1053 | -4.58038 | -42.95877 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 09c1c47d-96ec-3950-8f43-4f1b872288a8 | -7.33967 | -44.62224 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a89396f-f0c9-382f-b7f5-1f6e47145a1b | -4.98443 | -37.40166 | 2026-09-18 04:19:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c5375976-3bda-3e83-907f-1452c46deec3 | -2.81901 | -50.46342 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38911dcb-0de2-3e0a-a49e-2740a390c1e8 | -6.30223 | -41.77802 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d2916c46-9759-3a55-a4e4-0e37a2d57b3e | -3.36563 | -50.46445 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35a51e16-bbfb-3bb7-ad67-f8bb98bc5b17 | -6.66585 | -50.92934 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78e86861-1c81-3990-af10-4fc383520fe6 | -5.40436 | -45.83233 | 2026-09-18 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d324c82-0f55-3310-a548-128d6083cb8c | -7.57955 | -44.91524 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85c5eda4-6900-36dc-bfeb-101cbe9ee631 | -2.58614 | -48.43846 | 2026-09-18 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3255746-73f4-3206-a929-f95bfbbc0b9a | -3.41112 | -39.28026 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eed43346-d6f2-314e-bd7b-f00d3590bfcd | -4.53722 | -54.9319 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71ed2caf-6fbb-373e-97a3-0d4deff34121 | -6.18962 | -47.53221 | 2026-09-18 04:19:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 030e7075-2419-393e-a46f-6ad215d15168 | -4.49824 | -45.90903 | 2026-09-18 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 015a8fc9-530c-3694-b8d2-4a5539df4886 | -4.57027 | -42.95721 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f4947321-6a1c-325a-aae6-5dafcc53b3d8 | -3.26628 | -54.26293 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65d3ebc2-e338-39f5-9634-ec4d21f0b9cc | -4.16619 | -54.40966 | 2026-09-18 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3861aabd-2701-32ca-a35f-6426da0fa163 | -7.59748 | -46.31869 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee775a8a-f686-3d20-b442-4ab89e794d45 | -5.88933 | -49.78289 | 2026-09-18 04:19:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c00acbc-2e33-3d7e-9af4-33a6d4888f1b | -4.43273 | -55.52122 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fcc29d9-b323-30cd-ba02-aa084d327d08 | -7.85044 | -44.85883 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32efafe2-d791-3475-89ba-973a69301b0a | -7.30835 | -42.35688 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 874c7757-c7f3-34e6-9535-ee81f3d3662f | -6.27512 | -41.66365 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b2c200cd-6e79-32b6-8e83-922804e72d78 | -7.66831 | -46.0836 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 520aeb94-42ac-3d4b-8276-c96b68bc23b4 | -7.67883 | -46.10329 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fde1ddb-da59-3ad3-8655-82d02676cedf | -6.7741 | -47.86819 | 2026-09-18 04:19:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2ebcc6f-bddc-3b40-9c18-1c5e23e4da18 | -5.63514 | -44.79884 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6492fae-92d3-3f9e-9b21-c6db80bd61d1 | -7.55596 | -45.67501 | 2026-09-18 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82b94531-a430-323a-9b59-9f0365f7d908 | -7.43532 | -44.55182 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48b1ef05-8707-3340-aff4-717a5bfa1937 | -3.21203 | -53.95082 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08853d10-bde3-30d3-91a7-2cdd0351f8f8 | -4.42633 | -49.18702 | 2026-09-18 04:19:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 641fdb86-65ff-3fb6-b2a2-d18e166255a2 | -6.35116 | -39.84545 | 2026-09-18 04:19:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b5f99e00-d4a5-31af-8c64-92edb564265d | -6.94153 | -41.70911 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 389cffa0-1879-300d-826a-54d29451dac5 | -2.64368 | -54.69004 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3151691a-93b5-3cb0-baac-4fe5dc1283bc | -7.79391 | -44.8712 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 091bf04c-abe8-3cd1-811e-8922a6d5f0ca | -3.04046 | -51.37908 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8985f34b-5560-3429-a52e-e14739648e2b | -7.19063 | -44.44199 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1cb7b66-2b4b-3228-9d31-6eec52327cdf | -2.96104 | -52.14463 | 2026-09-18 04:19:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47f83f11-5418-35f2-bc37-200afd359620 | -7.85152 | -44.85189 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f78a17f-65ef-3f03-a427-74acc14a308e | -2.05784 | -52.16874 | 2026-09-18 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd355cef-b129-39d6-8819-3797018c6cd1 | -3.25924 | -54.26997 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe2a2f0d-51ba-3b56-9dea-c7ad1a77f78a | -7.10175 | -43.55953 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 905ca369-0f5e-3375-afd8-0c013302e1c8 | -7.79237 | -44.90288 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c2ffe809-78d7-3fd2-9799-06634a14a61a | -3.47283 | -54.6962 | 2026-09-18 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f171be6-df0b-3135-8b43-e9f2e344d06f | -4.57364 | -42.95774 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a50f0b05-1bc7-3bcf-a5b0-d15b7137d8a1 | -2.82498 | -50.48229 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5c187454-3fe4-3b5f-bbd2-e41998db277e | -4.56125 | -42.94846 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7201f20a-56e4-3935-9753-0d929702a866 | -7.06025 | -42.12986 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README31.md)
