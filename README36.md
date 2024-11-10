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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| effeeba0-7d71-3ba9-af92-d7bb8162f8c7 | -2.57486 | -47.34991 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e04e4828-5c0e-33d0-a16d-868b67c4b63f | -3.1531 | -45.94302 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41613a10-5c82-3f08-8030-9c4dc418bbec | -2.99139 | -50.29927 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 895fb058-b09a-34c9-805c-f6acde1c18e0 | -6.23043 | -42.92691 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fec92057-7463-3277-87fc-b81ea19be6cd | -3.21303 | -50.29554 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 84a16943-4b46-36fb-bec1-748f26ad6760 | -2.56338 | -47.34461 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 842031d2-e972-3e61-a7f3-7289ca0a0dd3 | -3.30244 | -50.08031 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6ceef71-c40a-3519-b37d-14380c3a461b | -2.85018 | -51.36206 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a036cf91-48f3-3f30-892a-c0a07ff4e0eb | -4.70544 | -43.86772 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68ccfb01-15ec-3bdb-9619-bf90d4e2e2d4 | -5.51532 | -41.6765 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dacb13ae-1217-3d39-9336-b715fe5ff90d | -2.64868 | -51.87456 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a20f88bf-d2cb-3bf7-91a9-b9b72e9b5828 | -3.95955 | -49.00834 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16b4a2ef-c07b-3d4c-bc31-247de9d99c73 | -3.45495 | -47.66449 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9120025b-97d8-3ccd-a98c-10cb27ac5991 | -2.24527 | -48.37817 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a82a450c-2c2a-3701-8e7f-fd352cc2edee | -3.2645 | -53.70352 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce34c83f-bdef-3ccb-8939-078349cbc5bb | -3.24872 | -50.19785 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34c04bba-8d5c-30ad-af7c-a1701c6099da | -5.23513 | -48.61068 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aaf264c-e298-3c76-a585-e3f4c7f72ea9 | -3.23018 | -50.28186 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b16948c2-930d-3469-a8b9-25587cfba9c2 | -4.05946 | -50.0153 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 045bffa5-2bed-3b8a-ae61-b4e23537ded3 | -0.40833 | -51.48079 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae023cf2-b8b9-3919-8dac-63bc006def3c | -2.08479 | -48.82612 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dea13458-3053-3351-9065-a5ab4da6ac8e | -3.58841 | -47.35365 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 61804c3e-5eca-3972-9dc6-2aa42db88004 | -2.42564 | -51.95963 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e89a6dc5-8e97-3066-b425-e67a34bdbf13 | -4.44033 | -45.91661 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62ed5b1c-bb64-3caf-abc8-2b044fe3e47d | -2.38176 | -46.59661 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c363245-539e-3ba8-9b1c-9a36aad789f6 | -4.85056 | -48.60252 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 55a53ba2-cc80-3ff9-8b57-23d723c3d692 | -4.39528 | -41.9095 | 2024-11-10 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c2c6f2aa-811e-39bc-86a0-4bf921d12606 | -3.04718 | -49.54803 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cd161ed0-03da-32aa-be0d-3df293967cfb | -3.06793 | -48.02771 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c36ed52d-b78a-3167-a436-52870985b9ff | -4.21686 | -45.45391 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 311f4e50-1cea-37e6-b471-9be31463f2c0 | -1.68261 | -50.41178 | 2024-11-10 04:14:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7042778b-5881-30c5-bb68-9a311b4b4fc2 | -4.75371 | -48.92892 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0883c370-48ff-3bf4-8605-e6779c52f014 | -4.12302 | -43.59001 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 16261fa4-46bd-3f86-99d7-80dd04c05f9a | -3.10208 | -49.41607 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2554efab-a1d1-3ccd-afb9-35ef2853a5c8 | -3.86207 | -52.38144 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bc54591-8fbd-3683-b350-a3188f52861c | -2.39614 | -46.78075 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e566a3d6-e486-3f00-8c57-baaf1d2ee39a | -3.76214 | -41.0285 | 2024-11-10 04:14:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8326443d-bd68-3031-9a2f-472f020483f3 | -2.87803 | -49.37544 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b09fbceb-b0b5-39f2-a118-5ee7128d5bde | -2.84348 | -48.67615 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 544c270d-a098-34e9-8c33-387e7279dce9 | -3.59317 | -47.34921 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1f992e73-07c8-3eb8-90d2-a899c330ff80 | -3.9187 | -47.94963 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6435934f-2d7a-3d5d-9513-76bc6c45b662 | -0.85834 | -47.63627 | 2024-11-10 04:14:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5a0e9a4-13c0-3fbb-9c8b-f0a42359e6aa | -2.76394 | -49.35372 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 38763a89-5070-392a-9aec-f4d4e5c3a598 | -2.62348 | -51.29804 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7ecf35b-e939-3989-b539-670d1494bca4 | -3.4889 | -44.55133 | 2024-11-10 04:14:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 264e76c6-8937-3222-97d9-5bd4bab24411 | -2.97586 | -50.30253 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6c3d5b2-3d02-3103-ae92-729c2b07faf6 | -0.85735 | -47.63578 | 2024-11-10 04:14:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c11d8c90-2b0a-35b2-a865-7726740eac34 | -6.2315 | -42.92001 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0140981e-c62f-3ae5-9bcb-e4ef00f2fcf5 | -2.39851 | -46.79105 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f0d2740-2340-3fd5-aa53-af6814f6867d | -2.57457 | -50.6797 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7deb728-dbec-3f57-9287-0be4a7145518 | -1.48147 | -51.74072 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38574bce-0176-3e1e-a78c-2587f03d9ab6 | -3.69754 | -47.64227 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e587460-9f2c-3056-b5dd-ca8270b55280 | -2.65981 | -48.56272 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 837f54bb-ecf5-3beb-85a9-795bf9c98288 | -4.02373 | -48.8967 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8489e26b-1766-3959-9227-ea20a8ca37c6 | -3.41407 | -42.29174 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 351cae42-ee4a-3b77-a61c-92d733627fa4 | -3.21702 | -50.30166 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b690c18a-daa1-3172-9702-b99722d1200d | -3.25368 | -46.46027 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 68cb8418-d995-3765-be4f-0c42aa26d1c3 | -1.51652 | -52.15915 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6e98bbd-815c-35c7-9e6f-a941e43887a7 | -2.36602 | -46.87108 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 942bb48d-0d2e-3b80-bfa9-51be0f5db204 | -0.04144 | -50.77655 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33fa93cd-d7ea-3d55-8314-38866ca529ad | -3.26294 | -53.71269 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e7fcbf6-509f-39c9-b0dc-a0ce033ac54a | -4.11914 | -43.59299 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 080876d2-5208-39f8-b4a2-03cdb3070249 | -2.36128 | -46.80014 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a6bc33f-6de0-3b8a-a15a-3fd3e18e5d0f | -4.68598 | -45.15129 | 2024-11-10 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5a2150d-138d-3b6e-a502-f3b1b6e518c4 | -2.82012 | -46.6468 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd440a98-87a5-3db9-ad8f-b4662c4e823e | -4.4323 | -47.26218 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71e6fcec-8272-38de-8961-06b325cbc5de | -2.86558 | -50.31652 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 92e52648-b7b3-359e-9087-a3476f446a7e | -3.19876 | -48.66438 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2eac83f-8147-3074-8fbd-69222ebbe817 | -2.24414 | -46.36357 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 8b9f7014-f6d6-39cf-aae9-ffd55c575104 | -0.04636 | -50.77648 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5df111f6-ae36-33fd-82aa-8585f707ec04 | -3.96973 | -48.17342 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61f462d1-47b7-30b1-a8c3-a6c3e48ddb45 | -4.06747 | -50.00883 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69f795c1-4c0f-3f19-b63c-32cc563033fb | -2.20275 | -48.36731 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 23a35a3d-c20e-343c-ae0b-33c79e6c9527 | -3.25025 | -45.9919 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3c321d2-41aa-35f9-850b-0aa2f115a326 | -2.72237 | -51.70877 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c1d4b85-c680-360f-9ec1-892021413d5f | -1.34017 | -47.68592 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d2860d3-335a-3b81-9718-1f8f952400a5 | -4.40247 | -41.90703 | 2024-11-10 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 58a45e91-f851-363d-921b-cf0785f4fcb9 | -2.36291 | -46.86544 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31ad0d9b-2f4a-3abe-b13a-392708b89293 | -2.31214 | -47.42719 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aab9a85-4c36-3d27-92a1-d39397e984e9 | -1.94905 | -46.41191 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e355909-5454-3d72-a50b-ae1a4d462ddf | -2.69325 | -49.86832 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c0fe0cc-5284-3966-8543-4c467668b7a9 | -5.69002 | -47.62166 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dba9ba2f-2dfd-316c-8a46-6f38eb903bff | -3.97143 | -48.18906 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30865458-87aa-3bad-8a4b-d634ed49ecc1 | -2.62145 | -46.16871 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6f78e7-4906-3558-a35e-a704f74e8b58 | -4.09034 | -49.12076 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2ccf1e6-164d-399a-912d-b02c7fa9bb6b | -2.52624 | -46.29863 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e42d9fd-7065-3a87-ab71-abd78c83578d | -3.84894 | -43.79829 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6883e3bd-a510-30f6-a0b2-6357cf586e0a | -2.42384 | -46.30794 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 7437971e-d0a9-3157-858d-b3b23c3209f8 | -2.47096 | -50.23962 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b8524bb-4d0c-3d3a-87ff-c995110f14c4 | -2.20143 | -48.37553 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46791561-44dd-3486-90c9-10f7a4860daa | -3.19715 | -46.49562 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f61522f-bc27-3b35-93d6-c745c92e48f1 | -3.9599 | -46.70413 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d053fafb-b6ea-3fac-9c64-67999125bc5e | -3.10053 | -49.42546 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1e25b270-c0bf-376c-a1c4-ea65be632fd3 | -3.22759 | -50.29786 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c208ed06-e3ec-3f49-b393-8791290104c9 | -4.68797 | -45.1165 | 2024-11-10 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0f130b6-e100-3eea-8ecb-7b5227050959 | -2.04813 | -46.0803 | 2024-11-10 04:14:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e29b9212-1a45-33cd-8186-d43e1b7005b4 | -5.5322 | -41.70107 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a186f5c-091f-3464-a177-5bc31ce3d468 | -3.04748 | -51.34141 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31639521-7525-3bf1-a57f-49e1ea877879 | -2.08548 | -48.82169 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 96d648f9-65d7-3d1f-ac8a-b42dce756157 | -3.25953 | -46.28197 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
