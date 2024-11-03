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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba7308ca-a926-326a-b626-2776ea3802bb | -6.5115 | -41.4837 | 2024-11-03 00:24:28 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe99012b-a1a9-3ae0-97eb-6f6d18638d5f | -6.5131 | -41.4907 | 2024-11-03 00:24:28 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fc7b23f-bc94-3ee9-867f-fa833ae9c2d8 | -5.6841 | -38.0382 | 2024-11-03 00:24:28 | METOP-C | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| cb96f7e6-3c4f-35bc-bb07-0795cf08a704 | -5.6864 | -38.047901 | 2024-11-03 00:24:28 | METOP-C | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 133d1b8f-8ee5-32f9-ba3c-7bc9e012973c | -6.3332 | -41.560699 | 2024-11-03 00:24:31 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ced41283-b22b-323b-8656-57c1578a6066 | -6.3348 | -41.567699 | 2024-11-03 00:24:31 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 114c21bc-f634-3991-b62a-4b8b4d807711 | -6.3363 | -41.5746 | 2024-11-03 00:24:31 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 133ee407-4cfe-3d9e-84de-21ea974f72af | -6.3169 | -42.028599 | 2024-11-03 00:24:33 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f0de48f-4d5f-3c2f-a3fe-0c91ffde0c5c | -6.3071 | -42.0308 | 2024-11-03 00:24:33 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f87cf818-a30e-3c38-ab99-0c29b1a7895f | -6.3087 | -42.037701 | 2024-11-03 00:24:33 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1cd2186f-aec3-3c1b-875e-8be4e399fc77 | -5.5281 | -39.1675 | 2024-11-03 00:24:35 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4b73b1c5-1fe2-3b0f-8d26-49c344fceb8b | -5.5301 | -39.1759 | 2024-11-03 00:24:35 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2fffeacf-b0d2-3571-984d-8c33ca5bb05b | -6.3983 | -43.835499 | 2024-11-03 00:24:38 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e492c0d3-794f-33c1-9c8d-aacbf812c906 | -6.1103 | -43.974499 | 2024-11-03 00:24:43 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86d22946-18b6-30ba-90f5-9ab60fe5ffda | -5.2804 | -41.246399 | 2024-11-03 00:24:47 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d2f3fcd-9a24-3d07-b516-ebfdf39dcfe8 | -5.2706 | -41.2486 | 2024-11-03 00:24:47 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe0fe63e-3abe-3dab-82ca-3a77c1fcce3e | -5.8045 | -44.125198 | 2024-11-03 00:24:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 928f92ee-12d7-3b1f-ab86-0c496308fa14 | -5.8061 | -44.132401 | 2024-11-03 00:24:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd26bb0f-4813-3282-9106-5921c38a03ec | -5.8077 | -44.139599 | 2024-11-03 00:24:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56177c67-b58a-337b-b4ee-dfe1989210ca | 2.5498 | -51.0981 | 2024-11-03 00:24:51 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 4530f7c7-4471-3786-a535-adadaf58b490 | -5.5436 | -43.928101 | 2024-11-03 00:24:52 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a5009f2-8be9-35a1-bf6e-a4a933eff183 | -6.4385 | -47.8564 | 2024-11-03 00:24:52 | METOP-C | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b7d2fdd-c1e9-380a-b103-b47b8ac64252 | -5.2873 | -43.072601 | 2024-11-03 00:24:53 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adfc92c1-8d5f-3c78-8dfa-8eed237dfe7b | -5.2888 | -43.079498 | 2024-11-03 00:24:53 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e93a90b8-52f1-3db7-a430-4027dbe1e83c | -4.542 | -40.466099 | 2024-11-03 00:24:56 | METOP-C | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dc55c0a3-d53f-3faa-b868-014f0a1bb9c6 | -5.1572 | -44.223301 | 2024-11-03 00:25:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95fbd4cf-c651-3d6a-a5a2-11526b464d8b | -5.1588 | -44.230499 | 2024-11-03 00:25:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39aecc05-afdd-348f-bd5c-8778007ebc25 | -5.9631 | -48.2099 | 2024-11-03 00:25:01 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f9c2a59d-aa69-38f3-bd00-da9f2afed42f | -5.9657 | -48.2216 | 2024-11-03 00:25:01 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 48e350f1-2af2-3a4c-9056-e46664634c19 | -5.9683 | -48.233299 | 2024-11-03 00:25:01 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1456b4-9b6b-3933-8ef5-beb857820316 | -5.5075 | -46.425201 | 2024-11-03 00:25:02 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bc3fbf9-750b-358f-80d4-9f8810c5a784 | -5.4977 | -46.427299 | 2024-11-03 00:25:02 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6dd0eef-cbc5-3b6c-94b4-33b2adc00f2b | -5.5095 | -46.434101 | 2024-11-03 00:25:02 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7e6db93-1e95-3a9a-b6d7-fe224886de3d | -4.6049 | -42.794601 | 2024-11-03 00:25:03 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf245631-a61b-3164-94fd-e187ba2b5372 | -4.6065 | -42.801399 | 2024-11-03 00:25:03 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5f09457-d670-3b66-a2ee-d611a4d21b9f | -5.4236 | -46.509399 | 2024-11-03 00:25:04 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b13ff12-3842-3e4d-b2af-0dfeb15388a7 | -4.5528 | -43.107498 | 2024-11-03 00:25:05 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b1a0977-1100-3061-9677-32ab9bc90621 | -5.3566 | -46.439301 | 2024-11-03 00:25:05 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79d8bb37-36f0-37fe-b3fd-ae1645b0f63a | -5.3586 | -46.4482 | 2024-11-03 00:25:05 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78e5c45b-e031-3fe5-bafd-b9dc4946c2b0 | -4.5512 | -43.1007 | 2024-11-03 00:25:05 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 465b1d73-005c-34f6-a34a-5ac8fbd206de | -5.2079 | -46.141399 | 2024-11-03 00:25:06 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc886418-bec4-3572-9ec8-a280c5a11194 | -5.2098 | -46.150002 | 2024-11-03 00:25:06 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84ec1e9d-b0f6-3e7d-b3c9-492910389726 | -5.1689 | -46.105202 | 2024-11-03 00:25:06 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c48b024-432e-3150-a1f4-f3a3b5bb95b5 | -5.1708 | -46.113701 | 2024-11-03 00:25:06 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0477a4-b7c6-3ae6-917f-9072c1a74942 | -5.1591 | -46.1073 | 2024-11-03 00:25:07 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0c850cd-0c60-38e6-9e8f-682b92f63367 | -5.161 | -46.115799 | 2024-11-03 00:25:07 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6bc422e-9d45-3e9b-a13b-656665026008 | -5.2881 | -47.378399 | 2024-11-03 00:25:09 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9708dd40-89e1-306c-8c19-b0d65b4a670a | -5.2904 | -47.3885 | 2024-11-03 00:25:09 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8184a53f-57d4-3c61-acae-9c7f69b66aeb | -4.4229 | -43.984699 | 2024-11-03 00:25:11 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8a4d455-705c-3f40-ae08-f31b928d5ae6 | -4.4245 | -43.991699 | 2024-11-03 00:25:11 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 256a5836-39f2-35fe-abf4-7f7143dd4a45 | -4.4261 | -43.998699 | 2024-11-03 00:25:11 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95c24e68-ccf5-3163-9f17-fca1e9b67c25 | -1.2755 | -53.4138 | 2024-11-03 00:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ad01fe52-9e4b-3962-ad2e-4d3727135808 | -1.2755 | -53.3936 | 2024-11-03 00:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| dce5a142-619a-3bb2-99c7-660860fcf888 | -1.2756 | -53.3734 | 2024-11-03 00:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 7b8ccbb0-1eda-3c95-b7d8-08a9a598d927 | -1.2572 | -53.3938 | 2024-11-03 00:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2c050c00-20e6-3447-b742-3e6b6309b6f5 | -3.5274 | -40.673 | 2024-11-03 00:25:13 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e1db2fb8-d0bf-3c9e-bec0-b909c9be783f | -3.538 | -40.718498 | 2024-11-03 00:25:13 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| def2bd21-f67b-395c-8e51-8be75dd6da31 | -3.5176 | -40.675201 | 2024-11-03 00:25:13 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e12216f1-f1bc-30f7-93a8-6194132fba84 | -3.496 | -40.759899 | 2024-11-03 00:25:14 | METOP-C | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2464813a-ed5d-39e3-9817-9474bc07d0a6 | -4.7529 | -46.404202 | 2024-11-03 00:25:14 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf84453f-d252-371c-a15c-38b934bf48d0 | -4.6529 | -46.371201 | 2024-11-03 00:25:16 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db67d31b-556c-3f5b-be10-6f6279c4b06e | -4.6549 | -46.379902 | 2024-11-03 00:25:16 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8180378-ffca-3940-a850-c0906af07138 | -4.6237 | -46.561699 | 2024-11-03 00:25:17 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec79c987-bfd4-3c75-af4a-e7a0eb988749 | -4.5686 | -46.453602 | 2024-11-03 00:25:17 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48e6cf65-0a6f-3051-a7c2-1aa4c76e95f4 | -2.1746 | -53.6834 | 2024-11-03 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 7b6e419b-005e-3a2f-81db-ae558c987ea1 | -4.5588 | -46.4557 | 2024-11-03 00:25:18 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2c8932b-a3de-3972-a291-3ab2797ad5f7 | -4.5608 | -46.4645 | 2024-11-03 00:25:18 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| edc8d4de-0bfd-3254-9676-560a9a764b25 | -4.0798 | -44.3797 | 2024-11-03 00:25:18 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a869dc6a-6357-32ed-a2f5-70ab2ce8ff88 | -2.2802 | -48.8082 | 2024-11-03 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 97a49df3-355b-30a8-914d-eb24c32a90f1 | -2.2986 | -48.8291 | 2024-11-03 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 02b8a8a8-55bc-34b5-ae78-84ef8a794c8a | -2.2986 | -48.8078 | 2024-11-03 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 314.7 |
| cce892a4-e970-312d-9938-32baeb854ecd | -2.2987 | -48.7864 | 2024-11-03 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| a5e4d7da-7bef-3221-9bb4-347fa065fc22 | -3.3911 | -41.6441 | 2024-11-03 00:25:19 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0b18597d-996c-35d8-a95f-38e1dac4afa1 | -3.3928 | -41.651199 | 2024-11-03 00:25:19 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87e65b9b-330f-3498-adce-841b318cba57 | -2.6322 | -48.5634 | 2024-11-03 00:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8b85e0a6-aeb2-389c-a722-b6ac3e49d4e9 | -2.6506 | -48.5844 | 2024-11-03 00:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 5352948b-debc-393c-bbf5-013b49ae18fe | -2.6507 | -48.5629 | 2024-11-03 00:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 2b5b12d6-9f8c-397d-bd28-a66db48c483c | -2.7033 | -49.33 | 2024-11-03 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c9fc732b-fc25-3ac9-bb23-9794528c1499 | -2.7218 | -49.3295 | 2024-11-03 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 33aadffc-1f35-3a15-b528-6b29caa59fbe | -2.7219 | -49.3083 | 2024-11-03 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 676172fc-d9a3-370e-a9e0-610883c3c58c | -2.5796 | -53.3927 | 2024-11-03 00:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| a43d4949-3d5d-3549-a3eb-6436ccbb67dd | -2.5797 | -53.3724 | 2024-11-03 00:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c95fd359-d658-3ef5-8885-1026fc1cc454 | -2.6321 | -48.5849 | 2024-11-03 00:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a1f55742-81b8-38f2-99b3-f144d0fd5596 | -4.8648 | -48.707001 | 2024-11-03 00:25:21 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9addcc7-0917-3efd-8dad-13b8bf3b4b83 | -4.8675 | -48.719101 | 2024-11-03 00:25:21 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a3c595-707a-3c06-ae4d-7aa83dc34501 | -4.8702 | -48.7313 | 2024-11-03 00:25:21 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57d8167-edd7-3a2b-9152-8535a36cbe92 | -2.7876 | -51.6099 | 2024-11-03 00:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 78c12546-5f29-339d-8f31-8a5dc947adb6 | -2.7419 | -54.4353 | 2024-11-03 00:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 254.3 |
| 64a830b5-3531-352e-a527-33b659b83b51 | -2.7419 | -54.4153 | 2024-11-03 00:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 212.2 |
| f45c3d09-4be7-3006-a569-048e6c7b9eb3 | -2.7602 | -54.4349 | 2024-11-03 00:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 175.6 |
| a687bb4e-4159-3e46-b4f7-1d122ad68b5a | -2.7603 | -54.4149 | 2024-11-03 00:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 5f680a25-08ea-36b2-b9d5-89070f8e7182 | -3.0365 | -54.2081 | 2024-11-03 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2ac34150-e205-3b86-9c1a-c495c3a0a2e9 | -3.0397 | -53.2603 | 2024-11-03 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b334c781-99ea-3e1d-aa42-d93e49ccae74 | -3.0732 | -45.0275 | 2024-11-03 00:25:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 96d8e3dd-9765-3a3e-bd8e-16c48f0241d7 | -3.055 | -54.1675 | 2024-11-03 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5697fe7d-6bc2-38ff-ad85-58696a0596f9 | -3.055 | -54.1474 | 2024-11-03 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 28681c0b-b782-3250-bd50-c0334c41469c | -4.4195 | -47.256199 | 2024-11-03 00:25:23 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 111966aa-0324-32dc-8792-77fd73e8f8b5 | -4.4217 | -47.2658 | 2024-11-03 00:25:23 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3cc2af-61e7-3f86-be48-ca923b677af9 | -4.4097 | -47.258301 | 2024-11-03 00:25:23 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbe1555b-3409-3c96-beab-4ff9c9af18d2 | -4.2238 | -46.474201 | 2024-11-03 00:25:23 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
