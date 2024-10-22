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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08681c63-e751-317c-946a-bbce5fb55c3e | -14.322 | -59.3382 | 2024-10-22 12:36:28 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9bc3671b-d14f-3e75-8aca-8e6da0edb139 | -3.5936 | -41.825 | 2024-10-22 13:05:27 | GOES-16 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 147.6 |
| c935fb19-284c-3790-b5cc-67d8937adda8 | -14.322 | -59.3382 | 2024-10-22 13:26:28 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 13e67081-12ac-3423-b647-02c349b6523c | -4.4207 | -43.9593 | 2024-10-22 13:35:31 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| dba3ed01-5395-3c04-aca3-26528e75b1a7 | -16.5345 | -57.2259 | 2024-10-22 13:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| bada2cad-19eb-3772-af49-a72a90950bca | -17.0184 | -57.5178 | 2024-10-22 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 1a63e033-c6c3-3ba2-b7f3-21985a12b0b9 | -1.5434 | -47.8118 | 2024-10-22 13:45:15 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 4b333f45-5a60-30cb-a8e5-16cee84b19e3 | -1.9793 | -50.8609 | 2024-10-22 13:45:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 4ad88c05-878f-3b96-ac98-37d9ab6c50ce | -1.9793 | -50.84 | 2024-10-22 13:45:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 36ad9ec1-b5da-362b-b332-3dc1016c54f7 | -3.3008 | -44.1533 | 2024-10-22 13:45:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4d000190-93e4-34ec-86a0-44de2e37f0f7 | -3.2251 | -44.3853 | 2024-10-22 13:45:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 9a8d897a-fbc3-3a62-ae48-2d6aeb771d18 | -3.9978 | -45.9979 | 2024-10-22 13:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 38db2d2d-e83d-317d-a6c8-6fe3a527ab25 | -5.2305 | -43.1886 | 2024-10-22 13:45:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 7bb6be36-81b1-37e8-8360-8c6070ba335f | -5.2307 | -43.1652 | 2024-10-22 13:45:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 1a5588d1-fe3e-36b4-bcea-49295c05fd64 | -16.5345 | -57.2259 | 2024-10-22 13:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 2a6ca3c8-bc12-39ba-9bdc-80d1adb0cd6e | -17.0213 | -57.3333 | 2024-10-22 13:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 9bacbbac-42f6-3fab-a872-7788454b30de | -3.0763 | -44.3684 | 2024-10-22 13:55:24 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c3c52253-fbdc-39a7-9b01-dda3ee1f4ad6 | -3.3194 | -44.1525 | 2024-10-22 13:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 108ee3cc-cd07-3bef-87b6-56ccf0a99e69 | -3.3008 | -44.1533 | 2024-10-22 13:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 4aac3115-794e-30ab-91b9-7d87a482ebe2 | -3.3009 | -44.1303 | 2024-10-22 13:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 2ab5d95c-d1d2-3850-87f2-001cb0de6fe0 | -3.5787 | -44.4384 | 2024-10-22 13:55:27 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| cfffb5ee-20a4-3625-a54a-acd1e2a8945a | -4.0163 | -46.0193 | 2024-10-22 13:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 38612dca-8e2e-3cb9-9981-aba30a41ab62 | -3.9978 | -45.9979 | 2024-10-22 13:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| c4c9dc5c-57a2-36cc-94fb-d318e7d18d8d | -5.2307 | -43.1652 | 2024-10-22 13:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 5d361c8a-8d50-36ae-b114-85e9e5ff3fde | -5.2118 | -43.1899 | 2024-10-22 13:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 52c67807-abdd-3c82-ae65-d1f99f10c3c8 | -5.2303 | -43.212 | 2024-10-22 13:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| fbaeeeaf-ee27-3d5b-8a4d-fbc6c43e883d | -5.2305 | -43.1886 | 2024-10-22 13:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 457.4 |
| b73974e5-2351-3076-80f5-e9c6692a7cdc | -6.0597 | -42.7261 | 2024-10-22 13:55:40 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 1fbddf48-61ba-3edf-854f-52c87ef8ad27 | -6.06 | -42.7025 | 2024-10-22 13:55:40 | GOES-16 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| d7cb61ca-7bc3-39bb-80b9-34be3ff914f4 | -6.2968 | -43.4331 | 2024-10-22 13:55:42 | GOES-16 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4e137551-eece-3e7e-89da-dc283e56b805 | -6.9393 | -41.4284 | 2024-10-22 13:55:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| d3c54665-423d-3e2c-8824-47c78eb33abc | -16.5345 | -57.2259 | 2024-10-22 13:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| e01b4a1e-8ed0-3125-9747-828dbc4ecf95 | -16.9995 | -57.4791 | 2024-10-22 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| b62f0cf2-3134-3452-b10e-e8a561a72abb | -17.0184 | -57.5178 | 2024-10-22 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 04865c3c-ae24-3e36-83bb-1b97f4125e04 | -3.2065 | -44.386 | 2024-10-22 14:05:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 441bb263-42d9-3f70-84a9-e5db9f3242f5 | -3.3194 | -44.1525 | 2024-10-22 14:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 57d8df8b-068d-32a1-878e-8002ab4de4e9 | -3.3195 | -44.1295 | 2024-10-22 14:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 285800c0-3f07-390d-8988-20ce3c80ed21 | -3.2251 | -44.3853 | 2024-10-22 14:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 2764395d-37d9-30b1-b646-6d8e65900f64 | -3.3008 | -44.1533 | 2024-10-22 14:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 274.4 |
| fdb5d332-2c65-3646-a4ac-066bfb504f65 | -3.3009 | -44.1303 | 2024-10-22 14:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 4a220f09-a86b-35e6-a123-a69c5d621028 | -4.0163 | -46.0193 | 2024-10-22 14:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 76cad61b-ccd4-3da0-8325-6ee63e7cdebe | -4.9122 | -43.2103 | 2024-10-22 14:05:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| fe0b9d96-eac6-3649-b87c-b05afb7f1bcd | -4.8558 | -43.2373 | 2024-10-22 14:05:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fa14ba89-1eab-3681-b985-22295bb30177 | -4.9309 | -43.2091 | 2024-10-22 14:05:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 26fa4a99-3cf2-30a5-9162-1ae312313e5e | -5.2307 | -43.1652 | 2024-10-22 14:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 01c2be28-84bd-3b37-99d2-8fef7dcecdee | -6.06 | -42.7025 | 2024-10-22 14:05:40 | GOES-16 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| d1c5feb2-1278-39f7-b811-e8b24ca01275 | -6.1843 | -43.4191 | 2024-10-22 14:05:41 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 85840498-b0b0-3c4c-99b0-23ebe4c239cb | -11.9938 | -43.0855 | 2024-10-22 14:06:13 | GOES-16 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 173.5 |
| 20090130-00d4-3176-b190-23e232e938c7 | -11.8727 | -43.3904 | 2024-10-22 14:06:13 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 9d9fb0db-8bad-3e10-8bb4-aa3203c5a212 | -14.322 | -59.3382 | 2024-10-22 14:06:28 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 19470126-6e2b-32e3-b5f2-9691104f95ec | -15.945 | -57.6171 | 2024-10-22 14:06:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6077ea3a-438c-34a0-af6a-f437955a8212 | -16.9211 | -57.4881 | 2024-10-22 14:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 550dc5ce-f789-3a41-b74c-1acd498e8d04 | -2.7589 | -49.286 | 2024-10-22 14:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fa9a695a-2a9b-37a5-9b22-46c640f9fc17 | -3.0577 | -44.3692 | 2024-10-22 14:15:24 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a49727de-f324-3742-ad7a-4910d5f08d60 | -3.1584 | -42.8384 | 2024-10-22 14:15:24 | GOES-16 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e4e7faec-b863-3f3f-bb62-634d89877ccf | -3.3194 | -44.1525 | 2024-10-22 14:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 6bb310c5-079d-3b7f-b1dd-b80a59a89f2f | -3.3195 | -44.1295 | 2024-10-22 14:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ffb58c66-5aed-3485-bcbf-72360a6e5912 | -3.2251 | -44.3853 | 2024-10-22 14:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 4f24ce7e-6061-3ca7-8293-79d9a63e7363 | -3.3008 | -44.1533 | 2024-10-22 14:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 249.0 |
| 2db11565-f591-3b29-9a78-e40fa582fe44 | -3.3009 | -44.1303 | 2024-10-22 14:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 49f25b48-9f65-3dc5-9aa3-6ecc345a7f86 | -4.9122 | -43.2103 | 2024-10-22 14:15:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 210.8 |
| b654dafc-ffbc-300d-8c67-827d7e41bfd6 | -4.9309 | -43.2091 | 2024-10-22 14:15:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 5214e4a2-3c34-356c-9969-a2dc4a5be96a | -5.2307 | -43.1652 | 2024-10-22 14:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 346f9a86-eff2-346d-bfd3-f84f3e401852 | -5.2667 | -41.1657 | 2024-10-22 14:15:36 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| c0c445e9-8f41-388e-86bb-b754de159cea | -5.2118 | -43.1899 | 2024-10-22 14:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 28253635-de2d-34cf-92ac-eeb8e181b923 | -5.212 | -43.1666 | 2024-10-22 14:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c2cb50a9-02cf-394c-aa9e-f6e01c8d19ea | -5.2303 | -43.212 | 2024-10-22 14:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 7bc31edc-21c1-353b-86e5-ad5499f2c89d | -5.2305 | -43.1886 | 2024-10-22 14:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 492.8 |
| d773f7fa-94b4-3721-8a68-9a8ce49ca871 | -6.0597 | -42.7261 | 2024-10-22 14:15:40 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| b0648d9f-f894-338f-b268-8dd52f647be9 | -6.4175 | -42.6482 | 2024-10-22 14:15:42 | GOES-16 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 0e12f34f-dc31-30ec-9dd0-05fc6936ae12 | -6.7238 | -40.4754 | 2024-10-22 14:15:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 61b2b9af-7cd3-3873-ae17-0fe77a561c2b | -6.7241 | -40.4508 | 2024-10-22 14:15:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 7ced9b93-aaf1-3113-b594-8c5480fc3258 | -6.9393 | -41.4284 | 2024-10-22 14:15:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 50652324-a53e-3d12-8e0f-5cb68e6efe17 | -7.2028 | -44.7618 | 2024-10-22 14:15:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7500ebc2-4dbf-3106-85a3-a506ba2e8643 | -11.9938 | -43.0855 | 2024-10-22 14:16:13 | GOES-16 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 146.7 |
| 1dd22a0a-1abf-3a10-9883-9ae6bcf4778a | -16.9714 | -56.7852 | 2024-10-22 14:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 94009e7c-c976-3753-911e-518c0f479397 | -16.9211 | -57.4881 | 2024-10-22 14:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 58bad92d-8994-3ad3-a848-3d38719a67eb | -16.8961 | -57.8378 | 2024-10-22 14:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| ddd79f61-e6b8-3bf5-883e-c85121696c2d | -17.6875 | -57.4181 | 2024-10-22 14:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| f9800cae-83da-3dd6-a999-094d8b55adfa | -17.6674 | -57.4411 | 2024-10-22 14:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| d09ae764-b1c9-385b-ab8b-e8aa019cd197 | -17.6681 | -57.3999 | 2024-10-22 14:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| e0950680-49d0-3fae-9d6e-e562503fb416 | -1.7924 | -52.063 | 2024-10-22 14:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 92e1d4c4-6054-31a3-94d9-dcaee0d5a534 | -3.3194 | -44.1525 | 2024-10-22 14:25:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 181.4 |
| 5856f004-ef84-3d48-b816-8ba0ddf69464 | -3.3195 | -44.1295 | 2024-10-22 14:25:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 88e800d1-9eeb-30a2-9fde-e47e8140c4dd | -3.3009 | -44.1303 | 2024-10-22 14:25:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 170.2 |
| b2479dae-a653-3931-8883-64653dee0645 | -4.2871 | -44.4029 | 2024-10-22 14:25:31 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a957a019-8e2f-3467-9f1d-2b3e3dc1d332 | -4.372 | -45.666 | 2024-10-22 14:25:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 767f52de-3f9a-3fdc-aa97-16d3a12084ee | -4.7457 | -42.964 | 2024-10-22 14:25:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 7a17e4ec-dd19-3f83-9dce-a8317b7ef81f | -4.9122 | -43.2103 | 2024-10-22 14:25:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| cfddaffb-98da-33bc-9af6-31f25ba29ba6 | -5.2307 | -43.1652 | 2024-10-22 14:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 466cea78-3a5b-3bd9-b76f-5bcd5d178e39 | -5.2303 | -43.212 | 2024-10-22 14:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 77af6b28-0865-3626-9049-d59a6dade76e | -6.06 | -42.7025 | 2024-10-22 14:25:40 | GOES-16 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| a9483e35-8766-325f-9231-382e0deea6e2 | -6.0788 | -42.7009 | 2024-10-22 14:25:41 | GOES-16 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| a36fa307-1cd1-3c30-81f5-7877b055fb93 | -6.1843 | -43.4191 | 2024-10-22 14:25:41 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 829d773d-34d6-34c2-8b1c-bc9721cdbb08 | -6.7238 | -40.4754 | 2024-10-22 14:25:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 250.0 |
| 4ab88078-a5df-3e9c-b095-997c3bfafbd3 | -6.7241 | -40.4508 | 2024-10-22 14:25:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 253.0 |
| 7a46ef1a-76ad-38fe-9b7e-d55e29709a7f | -6.9393 | -41.4284 | 2024-10-22 14:25:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| afba6967-7638-3db5-99aa-465475a49a46 | -11.9938 | -43.0855 | 2024-10-22 14:26:13 | GOES-16 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 162.3 |
| 5aad1db4-9ba5-3f4a-b667-94c0d2ca6ca9 | -16.9714 | -56.7852 | 2024-10-22 14:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| c9c82afa-db3a-395a-b721-e6f049acf5d9 | -16.8961 | -57.8378 | 2024-10-22 14:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |


[Clique aqui para ver as próximas entradas](README36.md)
