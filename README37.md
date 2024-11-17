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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57af032f-7c9f-3ac1-9af1-634a3f24b262 | 0.52981 | -50.05744 | 2024-11-17 04:27:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6bf245b-6185-30a6-9bf9-ecbe3e404b6b | 0.85186 | -50.13266 | 2024-11-17 04:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42eb0be7-2fb3-32b3-8e33-af6911601805 | 0.14936 | -50.04687 | 2024-11-17 04:27:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13a0222a-e901-3652-9b59-ed584c02670c | 1.5845 | -50.92279 | 2024-11-17 04:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a8fb0c5-74db-34f9-87ba-41a44aa82e81 | 0.00222 | -51.22317 | 2024-11-17 04:27:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae51bf5c-e3e7-3059-b887-d821e1314a3e | 1.58378 | -55.87956 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98a52314-8d73-3d0d-a4a3-c1b1729fab2d | 0.53051 | -50.06187 | 2024-11-17 04:27:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d9b35bd-57d7-3f5f-b07b-d6ac8e754720 | 0.40887 | -50.86857 | 2024-11-17 04:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6450aaca-f0fd-35b3-b131-2bbebf685ed7 | 0.41278 | -50.86795 | 2024-11-17 04:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d396991-9b74-30f3-846e-919f5039b933 | 1.58435 | -55.88332 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19f29b13-e40f-3ef9-a60e-e320ff927bd4 | 0.87315 | -50.88511 | 2024-11-17 04:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3246974a-d8a0-3dd4-a92d-cfed79e7c2b6 | 0.42061 | -50.86673 | 2024-11-17 04:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaab36c0-7322-3ad4-9a98-d1d43d94326d | 0.51773 | -50.74333 | 2024-11-17 04:27:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fbe6242-5624-3e84-a563-0146b5cde317 | 1.5805 | -55.88301 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14e045f4-7a45-31a0-8046-cb3965f508c9 | 1.57762 | -55.87671 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d199e61b-5be7-336e-95dd-7adc284a6a48 | 0.61943 | -51.77175 | 2024-11-17 04:27:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 03070195-86ed-32e0-b63c-296cc187f697 | 0.61355 | -51.77245 | 2024-11-17 04:27:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f593d45f-605f-3c6c-a1b3-d258b0c09d60 | 1.57932 | -55.87551 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 589d9bdf-a127-308f-bcad-3eccc161c40e | 1.57991 | -55.87925 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ee1b866-b531-34b1-88ec-06367ef981f0 | -0.2529 | -48.51906 | 2024-11-17 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d58fec21-6a6e-3413-bfaf-a603b634fbf7 | 0.62 | -51.77549 | 2024-11-17 04:27:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 32.1 |
| c089de6c-d650-3bbd-bb8b-aa5c4111583b | 0.61415 | -51.77619 | 2024-11-17 04:27:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 174d7a51-050f-3520-bdfe-1a4b964f6521 | 0.40496 | -50.86919 | 2024-11-17 04:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3adb5bb0-9a43-3c85-a8b0-2da8770ecc6c | -1.79341 | -48.44601 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ef0bc44-06b1-34e8-94e6-4317345c5d5b | -2.07387 | -48.53746 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eeef56e-39ff-3cf4-90c0-d1ccb2cbd66f | -2.67633 | -46.18606 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03771112-0f03-3125-b0f7-4c2fa73f6df9 | -3.53441 | -50.51793 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32f65fa6-a333-3ce5-9936-d1daa3e524d0 | -2.30148 | -49.12976 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d29b574-dbbc-333f-9f08-b4f65fcb85ef | -2.61796 | -46.255 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b45710e7-bcfe-39a3-bb84-c01ff8fc83a5 | -4.21957 | -47.21915 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92cfec08-529d-3040-974f-dbc9c4758bc4 | -4.37712 | -48.56605 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2260cb6-167d-35e4-b25a-43d9f9ce0344 | -4.2879 | -48.20952 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| acb0a7bd-3597-3b5b-95fb-4610fce5a74f | -1.13292 | -51.69117 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f79e3c0-9db2-3d7f-9dca-d514ccb406de | -3.56303 | -50.24914 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f897310e-939b-3c3f-bb3a-9288dbc54d95 | -0.9082 | -51.74393 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 377f5f21-ec60-338c-b15c-352e0f7eaee3 | -2.92466 | -48.32052 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03d94b81-119d-36b6-b94d-7f916814ff44 | -3.5617 | -50.25737 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b9eec65-19f1-38f6-bb13-17d588444028 | -0.89824 | -51.72766 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f3f241d-db70-3182-b6e1-c594ecbe9a27 | -1.83014 | -46.59806 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7d8e0db-b572-38b0-95cf-cbd6faa566db | -2.67138 | -46.19597 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2591d7d-c1a0-338c-af52-111c89760235 | -6.38652 | -45.68766 | 2024-11-17 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8d3ff56-6030-314e-9e14-6413d1c28e25 | -3.89249 | -49.98155 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7f468e4-7ea6-342e-882a-364d95d32a23 | -4.03268 | -50.88898 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10e1232b-5432-3d97-8242-5a4b98bdae50 | -4.10374 | -46.87656 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b81261b-2a47-38f6-a58a-5c16469a0e1b | -4.1862 | -46.5665 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7a8fcbe-c72a-3600-b42e-ee389f93e99a | -2.60122 | -47.55021 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1183dd4d-3736-399b-9d84-8b4a4c5aa57c | -3.5273 | -50.2528 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| a2627d99-0ed7-3eff-82a8-68bd810f31c7 | -2.09104 | -50.34066 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c962ebe-a9ac-396e-8ff3-95e3e56e1af8 | -3.34883 | -46.42583 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09ec16ca-58b7-35c1-bd9b-0c8589dbe4a1 | -2.23608 | -53.61128 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ab7c6dc-2cb0-3beb-9cba-b250cebc75e6 | -4.41376 | -50.50188 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4d4c26b-a02d-3bfe-81f0-6d102104ebfd | -2.99205 | -52.6015 | 2024-11-17 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bb327e0-9c79-3825-8fe4-65220e0baf95 | -2.68443 | -46.69688 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 123e24b1-7ffd-32ad-8bc5-7c9875e2f454 | -3.53166 | -50.26096 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 519e3efb-092f-35a5-aee4-50ea8ba422a4 | -3.03984 | -47.97841 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9da6c07e-7310-398a-bf0d-3881a73fd1a3 | -4.03392 | -45.47412 | 2024-11-17 04:29:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 583b922c-5213-36fc-abb2-464409e3bdcb | -4.56115 | -48.00741 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5907c19-11d2-399f-8312-3ec72d3e07f4 | -4.2955 | -48.09649 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbae2cbd-547f-3d86-8036-9e1de91d7f61 | -3.52077 | -50.24755 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 55008694-5ba3-3a8d-a0f9-da2843700490 | -2.66589 | -46.20937 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0647f912-1077-3792-8371-17dc50b6bf34 | -0.40231 | -51.62351 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dae5d52-fef5-32b7-8bc4-48a560b6f34e | -3.18125 | -53.24389 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3d028cb-9b46-319b-92e2-b7d978d16c5b | -4.27848 | -48.20446 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62253da6-2edf-39bd-822c-f4207921d618 | -1.63759 | -48.51877 | 2024-11-17 04:29:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ca6d3ad-5faa-30a3-9122-d61ee818adbc | -2.51397 | -46.39833 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 159680b8-1dc9-3b53-b2a0-19cacdd1feea | -2.24177 | -46.83477 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e0ae186-a055-3346-9714-f6cde00caa8a | -1.17484 | -49.46551 | 2024-11-17 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f064494-1cd5-3cbf-8290-9a2a42ec20c4 | -1.70688 | -46.23738 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a75a2d6b-a7f7-3da3-b2a0-593d079529d4 | -4.45775 | -44.06401 | 2024-11-17 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2473d4a8-20d2-3bba-b5e9-75f9a0b84706 | -3.78164 | -46.04421 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e69e25ba-cdd8-3300-b1c8-7e589da1c3e6 | -2.25811 | -53.78989 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94fea0c3-1127-3e26-95ac-4066def9a490 | -2.32598 | -53.57034 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 53ccaffe-1177-3151-baaf-be0be7ca5d6f | -2.71762 | -47.90947 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57cb2dbd-e40d-3661-a9e5-e99026db36ad | -2.1401 | -48.75768 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a17a4ccd-5e09-3603-92ba-108b0d102021 | -2.86722 | -48.7272 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b83b18c-4a48-3066-89be-95f2582309eb | -2.10331 | -48.29831 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35f9ec55-d045-3c26-9cb2-78f76476c225 | -3.95241 | -49.96924 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eabfc7b-f905-3c17-8a3f-b2ca8eb1ba29 | -2.08448 | -50.49348 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40e1765d-b586-3df3-8c10-953f9db29840 | -3.52563 | -45.90274 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d6b4695-dfec-3a83-a6e5-413c1ccc64ed | -1.37546 | -51.09095 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b781e2a-10f4-315f-b8aa-8b715ba71d72 | -2.67852 | -46.82276 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0a952de-0743-378b-8579-a057c3a0b6b0 | -1.91187 | -46.57565 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1f4aefc1-9afd-3821-8f4e-c566d08ae90a | -4.13936 | -44.1875 | 2024-11-17 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e68235b-2f77-3e0a-98d1-a18b6cee4515 | -2.14352 | -48.75822 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6189bed-c931-3e80-a1fb-1410689f74aa | -2.57449 | -54.41216 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec1bb5a-73e0-322d-b219-646c8f9584ea | -2.79888 | -45.98672 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9e5f55b-dc7b-302c-979c-aee392a21e1d | -2.61464 | -46.25449 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17b4a274-dc2d-39c4-9f84-726f62e25f75 | -2.2061 | -49.29118 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ac4ea56-a885-305b-a618-ff23997d233a | -0.94133 | -51.64289 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8f2327c0-f0cf-3ebe-b474-50ad03cf9005 | -3.17529 | -46.60062 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86f9814d-5a03-3c1e-9652-bac014478c54 | -2.17233 | -48.39745 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5bbd35a1-d9fb-359e-881e-049f6abdb5d3 | -0.88649 | -51.80322 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c946a9cb-5934-3804-b923-b3ff130cf4aa | -2.53234 | -46.21685 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fbd6534-afda-3477-bb10-c4d4f926bbfb | -2.13229 | -50.81702 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e912ed4-396a-380e-9e97-a8bf1804b085 | -3.53145 | -50.51311 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c75ddfb8-bc4a-3304-b190-8eaee55db37d | -4.44687 | -45.91247 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 972bb2db-0eb6-3969-abb0-903f1465e4e8 | -3.66114 | -50.20079 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04ae382-c744-304d-9c94-a927a78bd018 | -2.58306 | -47.01877 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63dac1c9-5617-3e48-a323-233ccfaf0b05 | -3.97719 | -46.70786 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa76d855-e431-3ac6-a17f-853952e96c61 | -3.18833 | -46.53894 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
