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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbe63506-0ab8-315e-afc0-1b2994c29219 | -7.92216 | -47.10345 | 2026-10-10 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f30e1426-41c4-3627-9b3d-231bf9f67cf8 | -5.04439 | -49.3497 | 2026-10-10 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b8437518-e37b-33c1-ad9c-2ab4fcf37f37 | -3.22315 | -54.29729 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e32743ea-576e-3ada-84fc-b2514d7850ab | -5.70708 | -41.76398 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c94b4b5-09a4-3f5c-a21f-d61bb19c6a32 | -7.04297 | -47.66066 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d05e1b2e-a7fe-3559-8821-6a9ed353b826 | -9.12383 | -45.82021 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dcb0502a-56cf-33fb-a81a-411bec3ce4c4 | -2.83712 | -49.88344 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7511011b-0259-3079-8488-417d571ebe06 | -3.53669 | -54.74321 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e05f02f4-d9ba-3bdf-9b68-a68967c59210 | -7.84571 | -42.90456 | 2026-10-10 04:08:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bc54471-4f0a-3fec-a53f-0a27c2021e06 | -9.31051 | -46.46597 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed811522-54c9-312d-8fc3-404aa084ee78 | -7.24154 | -55.21394 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4821020d-0ef3-3832-936a-a0df15ed0b13 | -7.24531 | -44.16883 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 571af01c-32d5-3cac-9fb2-bbd6b58b4b6e | -8.26496 | -46.41566 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82cd61fa-7eed-31fa-9c79-e304e0a2d30a | -7.22585 | -55.14597 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3229e9e9-b1a9-3c07-921d-70a906b7ec03 | -5.52975 | -42.72002 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c2dc18ab-24c6-363d-977f-15d52fdad3ea | -3.27584 | -50.38887 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6de0046d-7e3b-3a72-a009-7f6146767207 | -5.81588 | -35.38383 | 2026-10-10 04:08:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2f5c7d8c-f472-3a27-bd12-388b7a11dfe1 | -7.036 | -44.33728 | 2026-10-10 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b3b7be8-17cf-3566-943e-7c847ed4b604 | -7.06432 | -40.95702 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5aa6fb3f-d590-390f-ad2f-8760ae31ea18 | -3.29698 | -50.32883 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c65f379-eafa-3697-b0e0-c49156bf91a5 | -9.32541 | -47.63326 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00b35e0a-6ed6-347f-b790-1741fd649442 | -4.4548 | -47.92078 | 2026-10-10 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 40949a17-8f6f-3c18-b42f-e06e5f7eb3ad | -1.6222 | -54.42745 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f72ebd9-a6bb-3283-a6f7-502cafccb9a2 | -6.32787 | -43.49533 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b27c0b60-dd3f-381d-b985-3019ecd211ec | -5.69607 | -53.47011 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2387f149-f053-3f07-bff3-3af1382044f8 | -5.59718 | -47.28889 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f4a9c41-713d-3ce8-990c-86755a028b9e | -7.21796 | -55.07496 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05380bb8-a92e-3967-b0a6-6d55673d67a7 | -4.13876 | -50.81963 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ae307d6-ac48-3c3c-b844-1e103e87e966 | -8.95565 | -47.37644 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75bce7af-cea7-33ef-821d-c9758307d014 | -6.48839 | -55.31732 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6d347a3-575e-3bad-be1a-3ee173aa2f24 | -7.09661 | -41.75796 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cbf3e604-c95c-34a7-ba50-352ab4c5d3b7 | -6.08124 | -44.00208 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb76c567-2748-3cc8-b1b3-17b88ba57111 | -1.10985 | -54.16548 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d5459965-12be-3a64-b777-4b1586e0a32b | -6.42725 | -55.26447 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fdb9d8fb-d0b0-31da-9d54-f0ecea3725a4 | -4.68056 | -48.51888 | 2026-10-10 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97e65ca5-b18f-355f-bdc6-83b38bc49a82 | -3.19274 | -50.5428 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8912c484-f92c-38f1-8de5-2e3230be017c | -7.2198 | -55.14619 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0476cc4-b677-3424-915b-c705664345eb | -8.18245 | -54.71886 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 011c1fa8-b928-3146-8a7b-c6e421981110 | -7.21201 | -44.35293 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e327097-d075-3d38-958f-fbe36eba8e3a | -5.23236 | -50.67894 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db928135-4dd1-31b1-8f24-fae8f03f057b | -5.68146 | -53.47884 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7049172c-d5ee-3952-895f-ca6f6535e6e5 | -3.12333 | -54.17749 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cbe68c1a-b87a-3765-83d3-a5578d2d6c0f | -4.40902 | -49.77152 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 87e0f760-d827-3553-9761-fe0257e87030 | -5.75209 | -43.27004 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 780bc441-e05e-3c67-b11a-71b50be84c51 | -9.43947 | -44.5949 | 2026-10-10 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53a45b90-0f8e-39ad-832a-5ddb831bbafa | -6.22258 | -52.64489 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cb76ed2-f09f-3edd-aaff-e434df84cf19 | -3.18853 | -49.24872 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e256bb-0b02-39e6-bbf2-0cd0e7e39b26 | -5.95651 | -48.92045 | 2026-10-10 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4d6cc9a-adf0-356b-bc8c-3b27ae72201d | -6.82429 | -39.56009 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 48bbdbb2-5024-3f13-b7ee-c228f201f21b | -3.43631 | -54.54235 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37492f4f-8dc1-3b4c-8ac0-244a938e483b | -6.43367 | -55.03797 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 30cc4183-d290-349a-9b23-65c19de0bcaf | -5.4573 | -44.78101 | 2026-10-10 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d27e690c-b7c1-3427-a3b2-f45d75eba29f | -6.13059 | -44.12789 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb4db7d6-4aae-394d-bca2-c1b5cdf16ec8 | -3.24718 | -54.03012 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0634faa8-3616-3bd9-b090-28ef7aa3eb74 | -9.9358 | -44.89085 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cfece885-fc6b-37d1-8177-0b3b2fc763de | -9.01662 | -44.36418 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ece4e44d-bd7d-3053-ae1e-56fbaccf7efc | -8.92994 | -45.42152 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa3959d3-d814-31a2-8ec7-6a92a4f163f6 | -5.50681 | -40.75756 | 2026-10-10 04:08:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3cd974af-16d6-329d-9474-6282672d1ca8 | -7.05875 | -40.94894 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| adacf774-e545-3d84-8115-34c0de81c88b | -2.40058 | -45.57497 | 2026-10-10 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a9c4bad-c947-3c51-9f1a-93bfd89f7b9b | -5.59765 | -47.28829 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b6b53b0-3ff0-377d-b37a-967a69701159 | -6.93429 | -44.5663 | 2026-10-10 04:08:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c307fad2-b8d4-377e-85db-55b794e610d9 | -3.396 | -50.21693 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f91809a7-de95-3b33-88af-c07887b53da5 | -3.23615 | -50.17795 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f812064-e040-3096-9a83-194ce3ef821a | -9.01246 | -44.36782 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34c107e2-45d9-357d-862e-ff8ad22c345c | -3.4524 | -50.58738 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b430de8d-dd57-3300-8afa-0f18705d57cd | -2.99373 | -53.89777 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e96e469d-e7eb-36b2-93ab-02ca20c92dcb | -4.63678 | -50.96341 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6272e30c-94b2-3305-b782-32b04c51a53d | -6.43913 | -55.27337 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09b19674-35b1-375b-b11f-cf18cc82e59b | -7.48079 | -44.84479 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 000c21e4-c8df-36ef-b3a5-f76692ee92d1 | -3.34524 | -50.41842 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 120adf14-8265-34d2-8408-e3a9e3ff16d4 | -7.7735 | -43.78895 | 2026-10-10 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 66984009-f547-3f44-a1e2-0c132c2d80d9 | -3.24838 | -54.03409 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17ea34a5-bac2-346c-8faf-199c835832ca | -5.76476 | -41.68145 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d3a2712e-3fbc-3b07-85c1-ad5d29d6eb62 | -3.25435 | -50.41745 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a066e8a9-8730-385b-b118-e18c3b015ead | -8.44888 | -47.98534 | 2026-10-10 04:08:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fa0e073-48ea-3db3-8ea1-d0ab08e24e69 | -8.24889 | -46.41776 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e97cd23-1b2a-3d23-a154-e98d03f70575 | -3.12213 | -54.18429 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8e1fb183-e920-3342-ae6a-d10056949727 | -2.93192 | -54.08803 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10e88033-5f3c-3c53-be6b-c5ef06e427f7 | -1.64537 | -54.39944 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc979ba2-78d6-3c4c-8428-c86331b9bc08 | -9.22046 | -45.66521 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73fadc66-77ee-3a9f-a74b-c224f2821332 | -1.95754 | -54.39614 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dee32f14-3d96-316a-9ffd-5a535a5a2546 | -6.45016 | -43.82616 | 2026-10-10 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc7ee64c-53e8-399b-813c-126c8b1858f9 | -3.54368 | -54.74472 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3b504449-5ed8-315e-9cea-cb9205e7e66e | -7.39339 | -44.75651 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e81d23c-9189-3995-97ec-f734c4b1ff08 | -1.63144 | -54.43901 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e71c075c-c6f8-3cce-9e47-db2bfe2a5eda | -2.4294 | -48.20378 | 2026-10-10 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68e263ce-c3c4-3772-8f98-c933b4e499cf | -7.21263 | -44.34906 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63e72296-33bb-3c76-9d50-0f4c43ba44ac | -5.11342 | -46.22256 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 143f0c34-eb85-3c05-89c5-12c3e904a035 | -5.74953 | -45.1263 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d1121199-bced-30c3-a600-19f177be6a72 | -9.17514 | -47.70541 | 2026-10-10 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba9365cb-5150-39ed-8248-fcdecc7e8085 | -6.45259 | -55.283 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3c6b4919-6f4f-3544-a6a5-04eceb0d51bb | -3.17473 | -50.58386 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| facdd8eb-c9fa-325c-bd30-5e0639ec394f | -3.31303 | -54.67973 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b14e8112-bf33-3687-ad4f-d8e16629b588 | -3.22488 | -49.43325 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2164ebb0-916f-31cc-9ba7-75a963dfeca6 | -3.11531 | -53.7939 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 91aedb9f-6cd5-3bee-bc6e-2a5fee0c3ba2 | -7.22804 | -44.16609 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a372a4f3-ff6a-3a33-bd63-213c285d496d | -3.11761 | -54.16988 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 12255392-39a2-3c8b-aaf1-dc61201cdd7c | -3.15707 | -50.58839 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 758a8f32-9c3a-35ba-b90a-38d795e4e77e | -2.93307 | -54.0857 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README35.md)
