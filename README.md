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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c838a6a-aa75-3a91-a5ff-4478948c65bd | -6.9718 | -43.56 | 2024-12-19 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 5228ed32-07b8-3cf3-9957-eeaa53a3d23e | -3.2135 | -46.8063 | 2024-12-19 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 55c83f85-5dd3-3a05-8e94-72d3496bf6ae | -6.972 | -43.5366 | 2024-12-19 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 5fcdbcdd-a64f-3a08-be42-795a0c314867 | -6.9532 | -43.5384 | 2024-12-19 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c4919dab-2c75-3341-be53-229113d2c591 | -5.211 | -43.2833 | 2024-12-19 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 2fec2e3b-0aa8-385d-a1bf-e39275bf2dea | -6.9908 | -43.5349 | 2024-12-19 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| c9aaf111-af03-38bb-bdac-7f8c176d4aab | -1.7518 | -45.8299 | 2024-12-19 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9a4f42ae-b133-3202-a912-b36599886d5f | -3.2136 | -46.7843 | 2024-12-19 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| fdf4e5fb-48c7-37a3-9a85-64811ae96bda | -5.2108 | -43.3067 | 2024-12-19 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bdd9f460-592a-3758-a728-5b1eb03655e9 | -6.9529 | -43.5617 | 2024-12-19 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9a9bdcd9-74be-39ec-9096-236007608f1f | -3.232 | -46.8056 | 2024-12-19 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 3e979867-d455-3d94-b697-9a5f3327eb66 | -3.5968 | -44.5289 | 2024-12-19 00:00:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b20854cd-1dfa-3d9d-8dfb-4c3073101e8b | -6.1229 | -43.9578 | 2024-12-19 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| beacbe96-3870-3414-ba76-81064b34359d | -3.5967 | -44.5517 | 2024-12-19 00:00:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| badfb952-8587-3945-a167-d934fc87f325 | -10.7433 | -37.1027 | 2024-12-19 00:00:00 | GOES-16 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| 40e00c4c-e24d-3f74-b719-876512b12cda | -4.9979 | -44.2001 | 2024-12-19 00:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f3f6b354-848c-3a97-8b77-a0abf328ec60 | -3.2321 | -46.7836 | 2024-12-19 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 69140aae-5cdd-3b37-a1a3-5104684a1893 | -9.6464 | -36.0397 | 2024-12-19 00:00:00 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 50.3 |
| f37161db-9df5-3625-b61b-6166ddf7d233 | -6.9911 | -43.5116 | 2024-12-19 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1b9f7c1e-7aec-3a6b-baac-cfca3839896e | -5.9477 | -39.6665 | 2024-12-19 00:03:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cd688bc0-179f-3e1f-ac2c-be8bd92520bf | -4.785 | -46.389198 | 2024-12-19 00:03:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 073289f5-1e32-352b-8e9e-2b10ddfd3c3a | -4.7948 | -46.3871 | 2024-12-19 00:03:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ecf860c-52a0-3a59-8d0f-ac6373d2b57a | -5.8096 | -39.208199 | 2024-12-19 00:03:00 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 75e86079-4227-3535-bd09-76aca9235384 | -4.8767 | -41.407101 | 2024-12-19 00:03:00 | METOP-B | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 637c0c9f-517f-3b74-a31f-90332ed47fa6 | -4.9308 | -43.956001 | 2024-12-19 00:03:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| daa7e3cd-3d61-3421-8d0b-b559e19fc433 | -6.124 | -43.949001 | 2024-12-19 00:03:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85e90756-9056-3448-a1af-285b041b0f5c | -6.3702 | -35.230499 | 2024-12-19 00:03:00 | METOP-B | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3297583a-12a5-3308-b834-350e6058ea63 | -4.117 | -43.5462 | 2024-12-19 00:03:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d6b0281-9855-34be-95b6-de9124e6bbb2 | -4.4845 | -45.409199 | 2024-12-19 00:03:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cbcb7a11-8b93-325d-ae7e-fc12df91a25c | -4.9192 | -41.322601 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f09a1b3c-95d6-3a45-8139-db2ba09574e3 | -4.4161 | -45.379902 | 2024-12-19 00:03:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61cdcc7d-b5b8-383b-bb95-5774744a7b75 | -4.8633 | -41.393501 | 2024-12-19 00:03:00 | METOP-B | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37107b20-83d2-3c10-a442-8b31cef46a20 | -7.5683 | -35.048199 | 2024-12-19 00:03:00 | METOP-B | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b25b5c6-37c4-31a9-bc74-77115d038403 | -4.8695 | -41.375599 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6a669940-4be5-321a-b117-3d88984d40ac | -6.9883 | -43.5326 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d3843b0d-9a9b-34d8-9081-ae3a33c41fab | -10.2604 | -36.3587 | 2024-12-19 00:03:00 | METOP-B | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34dbf58c-3271-3a8f-8205-45e492f7fecf | -4.9975 | -44.206902 | 2024-12-19 00:03:00 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb841b5-e6cc-3b9d-9d7e-b7b7d299ca6e | -5.9732 | -41.603802 | 2024-12-19 00:03:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 125382ef-7405-38ff-89ca-08910f73d0ec | -6.0698 | -44.6264 | 2024-12-19 00:03:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3da98854-8b43-3178-84f2-787d9a2e8a13 | -4.3983 | -41.432598 | 2024-12-19 00:03:00 | METOP-B | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49e37782-566c-3d16-b947-ca89a7ad9cab | -4.8597 | -41.3778 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 28f6a742-ff2c-3fae-bd30-dd72c517770b | -6.2016 | -39.386398 | 2024-12-19 00:03:00 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8f34c04e-8fec-3567-92d6-b8d8fbb7e535 | -4.1186 | -43.553101 | 2024-12-19 00:03:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a463211f-d4bc-328a-99a5-9d368276821b | -2.5624 | -45.561501 | 2024-12-19 00:03:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cfca863-562d-3adc-9128-5d06b591262d | -10.2636 | -36.371799 | 2024-12-19 00:03:00 | METOP-B | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c4782e5e-851a-3bc4-803b-3a44b5842e94 | -6.9574 | -43.532299 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b281233d-bfdc-39af-9f12-39ce7ba2edfd | -6.1256 | -43.955799 | 2024-12-19 00:03:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe00337-1c07-3cbf-ba51-f3f0b4534eb9 | -4.0073 | -43.744301 | 2024-12-19 00:03:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b31f280-f149-377b-8a6c-1ca3d6739420 | -5.9099 | -46.223202 | 2024-12-19 00:03:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72d4a334-dc94-3c7d-a0b7-05b73e634318 | -7.5639 | -35.030399 | 2024-12-19 00:03:00 | METOP-B | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 961d97bb-ff0e-386c-bd67-45bbcc1fff87 | -6.1225 | -43.942101 | 2024-12-19 00:03:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbec6f03-d1fa-36e6-a83e-ff1a3e82510d | -4.8027 | -44.027599 | 2024-12-19 00:03:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff8c63d4-6357-39e6-9acc-0f240cb797f5 | -5.3861 | -40.665699 | 2024-12-19 00:03:00 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2afd7d26-992b-35d7-b67b-13c50ae0b0fc | -4.1036 | -42.850601 | 2024-12-19 00:03:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0d1d7b-3192-3702-bc3b-9132ce133fce | -3.9466 | -41.484798 | 2024-12-19 00:03:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eed0bbba-e16b-3434-9e47-77d963857b37 | -6.2039 | -39.396099 | 2024-12-19 00:03:00 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c9988c20-1655-318b-924f-be1bc1641136 | -4.8811 | -41.3811 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e0c1b28-1ac9-3fc9-b02b-859014badd1b | -8.0594 | -41.2607 | 2024-12-19 00:03:00 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 76f08232-27a8-3c0e-a00d-015d15464dd3 | -6.966 | -40.633099 | 2024-12-19 00:03:00 | METOP-B | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d69704eb-af7b-38e2-a222-a39b2878a265 | -2.5609 | -45.5546 | 2024-12-19 00:03:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e71067d-6f65-342c-889d-34d43f1148a0 | -6.1338 | -43.9468 | 2024-12-19 00:03:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae0a07cc-6870-3513-bd45-16d1d6e3deea | -6.2061 | -39.405701 | 2024-12-19 00:03:00 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6239abb4-9ca3-3aff-a29c-65c8808e97d4 | -4.7703 | -45.629299 | 2024-12-19 00:03:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e57f40f-2e00-390b-a83f-64f6cd07d72a | -4.8829 | -41.389 | 2024-12-19 00:03:00 | METOP-B | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b905a9d0-11cd-321d-91c3-f267196a5892 | -4.9681 | -43.7103 | 2024-12-19 00:03:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94f61584-d111-353c-94bd-7b78f0a63e6a | -5.2026 | -43.288898 | 2024-12-19 00:03:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5273702-8d68-3f70-932f-3f18f43f3cda | -6.4961 | -39.5881 | 2024-12-19 00:03:00 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 98e48d8e-f677-39b4-b602-1cc4021f7edc | -10.4535 | -36.7682 | 2024-12-19 00:03:00 | METOP-B | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3032dc48-7ec2-3d0a-b9ca-cf76da51fc1c | -4.996 | -44.200001 | 2024-12-19 00:03:00 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35c40bed-c77c-3ebd-8f4a-452466d99ccd | -5.1693 | -37.583801 | 2024-12-19 00:03:00 | METOP-B | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 555bbf07-7b3b-3707-a278-d2ec7f1948d4 | -2.1006 | -46.164501 | 2024-12-19 00:03:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 503b1275-96da-35cd-b944-0f39e79fcdc8 | -4.4177 | -45.387001 | 2024-12-19 00:03:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0649015d-7cc6-3d3d-9ec6-0448c9a6c44a | -10.741 | -37.1007 | 2024-12-19 00:03:00 | METOP-B | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d2604c2d-8b44-34ba-9e49-42b3544ee862 | -2.0991 | -46.157398 | 2024-12-19 00:03:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a11f9eb8-49e0-3731-baab-d49ae3495485 | -4.3964 | -41.424702 | 2024-12-19 00:03:00 | METOP-B | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b16778a-0b67-3142-a527-e1e69b86254b | -6.9718 | -43.550701 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4d239374-9441-3de4-a8d6-00ea7ac8e43b | -2.564 | -45.568501 | 2024-12-19 00:03:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72dad4eb-ea60-354b-b659-d41343700abb | -4.9094 | -41.324799 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1184daab-e940-3103-a08e-fac8f29bbb24 | -6.9785 | -43.534801 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd07d93-81f2-303d-b38e-ed8cf5aecae3 | -5.2155 | -43.300598 | 2024-12-19 00:03:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| baec320a-4cad-362c-a7c2-55a71b681449 | -4.8749 | -41.3992 | 2024-12-19 00:03:00 | METOP-B | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a1e242f8-3a00-30d3-a2ad-c1c29c50c59c | -6.7344 | -35.083099 | 2024-12-19 00:03:00 | METOP-B | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41cd7dca-0d56-31fa-94bf-9fb1d578de26 | -7.0877 | -39.034199 | 2024-12-19 00:03:00 | METOP-B | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3788a055-ae4c-3ba5-aee5-d1fd77320ff4 | -9.9817 | -36.3162 | 2024-12-19 00:03:00 | METOP-B | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c86fdbe-e347-3ac4-a77c-22e77f52370b | -10.2506 | -36.361198 | 2024-12-19 00:03:00 | METOP-B | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 20384336-13eb-3fc4-bd3c-706f81ad5f64 | -4.0089 | -43.751202 | 2024-12-19 00:03:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26d7aafd-ef24-3efe-8f27-3d33eb4395a5 | -9.0486 | -35.4585 | 2024-12-19 00:03:00 | METOP-B | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ce8d491e-4ae0-3b3f-8f58-3eb8fbf276ae | -6.9605 | -43.546001 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71e8734f-beae-3e6a-a755-d773a730bd33 | -5.2041 | -43.295799 | 2024-12-19 00:03:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdb8bdba-f26d-310c-b989-a3d80ede6d83 | -4.8847 | -41.3969 | 2024-12-19 00:03:00 | METOP-B | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e61cf16-7fa2-3132-aa1f-ba898481d310 | -4.8517 | -41.387798 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d381739-3f5d-302b-9aea-eb20e3cf2954 | -6.9703 | -43.5438 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df35c6ec-3238-3571-aa08-06b009ca1b86 | -4.3583 | -48.456501 | 2024-12-19 00:03:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93024143-7b62-3e98-8888-ee493cff0099 | -4.8713 | -41.3834 | 2024-12-19 00:03:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94c0d4fd-b087-358a-9c66-d49a34fc010f | -13.3083 | -52.4007 | 2024-12-19 00:03:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8a0e442-db92-3a2c-84a6-0dd605baf9e0 | -5.9714 | -41.596298 | 2024-12-19 00:03:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d934722-062a-3b62-bbdd-6a2b31bcfa9d | -4.1202 | -43.560001 | 2024-12-19 00:03:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e40611c-0728-3ac9-8534-e10734e2b76c | -5.1724 | -37.596802 | 2024-12-19 00:03:00 | METOP-B | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 82416534-b9fe-39bc-a39d-d2bb3d6c94de | -6.9966 | -43.523602 | 2024-12-19 00:03:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e983d0a-aa6f-3428-84a0-c60c72306da4 | -10.2473 | -36.348 | 2024-12-19 00:03:00 | METOP-B | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
