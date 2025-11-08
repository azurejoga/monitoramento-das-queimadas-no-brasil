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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e6eb015-e733-315f-9dfb-8f834ae94b5d | -3.28745 | -52.08898 | 2025-11-08 04:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bf79b25-de57-34c0-8ac5-1d5c9538e33e | -6.09521 | -41.70802 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e9d26606-664a-303c-bc6f-c3ff7ef43af7 | -2.97641 | -48.70397 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a6e4430-7e9d-3998-94b0-5b55b00032bb | -3.09495 | -50.32812 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efec30d1-f47d-388d-b3a5-11c49c5a2287 | -6.3697 | -42.38434 | 2025-11-08 04:06:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b36c8efe-6746-37ca-b357-318d4892d2b5 | -6.18322 | -41.62628 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c965582a-a7d3-3c4c-9d2e-af04c2aa8292 | -6.00075 | -39.51311 | 2025-11-08 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 139d2fb5-8313-3680-b503-e7f8527588c1 | -6.65369 | -38.84097 | 2025-11-08 04:06:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 50e45601-df15-3a1a-bb64-0044db38fb6f | -3.08941 | -50.3272 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab331afc-205f-3e12-aeb8-02cd0bc91073 | -3.34178 | -50.20495 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8d8d8096-9a50-398c-a507-4fbb2c50809a | -3.55894 | -50.80735 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7084d170-eeaa-3517-8361-9dc15acae57f | -6.85075 | -39.11556 | 2025-11-08 04:06:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0db2137e-6094-3bfb-aa98-439178c52290 | -3.1005 | -50.329 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd8fcfbd-5c90-3a51-8c8d-145e9abd6907 | -5.23035 | -42.79909 | 2025-11-08 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a10cc26-5be0-36f5-99bb-918479f4c94e | -8.03241 | -38.53328 | 2025-11-08 04:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5a8a58dd-2ab5-318d-bdc2-27e54931ede1 | -4.52296 | -45.74165 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9713448-8213-3f3a-bbe3-fc3a1992b881 | -3.09539 | -49.25088 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea9cbe50-0f20-338e-8a00-4e7af7536d86 | -5.60493 | -37.35443 | 2025-11-08 04:06:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3b56efc1-d3cd-3a40-8ebe-e7ccd5e46f62 | -3.65421 | -50.2743 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44f88f1e-c3d8-3327-b6d3-23fbe02d9aa6 | -3.43399 | -51.51918 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31170ea8-7a23-32b3-b09f-a4491e949f04 | -5.23998 | -46.17117 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfb989a3-d892-3f89-a030-1e1bb0b434bb | -8.02818 | -38.53693 | 2025-11-08 04:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f09b059a-1e09-37b1-b465-5db2df8f0355 | -5.23094 | -42.79543 | 2025-11-08 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ec8361e-3a0d-3358-a21f-3ee2eba14995 | -3.09434 | -49.25707 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc0abde1-d604-39aa-9820-804552fddb78 | -5.30369 | -39.80183 | 2025-11-08 04:06:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8e434fa-3b23-3aed-abc7-1f8a1673e6f8 | -4.53228 | -43.76917 | 2025-11-08 04:06:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03b539fa-bce5-31ce-a6fc-5daf351c7d18 | -6.4854 | -48.37058 | 2025-11-08 04:06:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e27f1df3-f54b-3e3b-92f9-8d72722f17c0 | -6.09948 | -41.63789 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 23e848b6-687e-32ca-9982-24375aa5d152 | -5.67845 | -40.85086 | 2025-11-08 04:06:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b88ea09a-b3e9-354f-92e2-6d4869e34ae0 | -3.58129 | -51.24577 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 268e1d3c-9c16-35d9-8e8b-747f31babda8 | -3.45739 | -48.84197 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 144008a6-1fac-39bf-b3ad-8ce85b2be370 | -5.65059 | -43.00388 | 2025-11-08 04:06:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3d227ab-a561-3de6-9648-da277201c684 | -3.72981 | -49.68056 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60956cd0-4c88-3aff-b418-900359118cff | -3.64972 | -49.86573 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37a8bd5d-c7d1-3391-8f42-0e520dadbbad | -4.69209 | -46.40007 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f89633b9-0af9-342d-88d3-78324cdc861c | -3.84049 | -49.82721 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e27a26b-3716-3554-a65e-c2dc6ac9626b | -4.90766 | -45.10652 | 2025-11-08 04:06:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e434fece-b58e-3132-ae1e-fd8f1d3faf06 | -5.6165 | -45.04525 | 2025-11-08 04:06:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70eda911-2805-329c-827e-150ae7de75ec | -3.67752 | -52.09456 | 2025-11-08 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2ad84f0-6db9-3031-a884-6846e51c0ca3 | -3.34284 | -50.20349 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 792f785b-6d6e-3647-b721-8457237424e1 | -4.59146 | -45.99897 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| c3ede53a-fe1c-3ebc-85c2-1922f545e280 | -4.39247 | -45.35519 | 2025-11-08 04:06:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ada2b1bf-e637-3eb5-b74e-3c1cc2868b67 | -4.46838 | -43.21452 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05841796-5408-30e8-9dca-03d7fedb72ec | -4.60821 | -45.56085 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12426b9e-d1d4-3199-a2c8-593560d6cdfc | -3.01422 | -49.44276 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 024ee5ff-93bc-39be-86f3-4268400b6a35 | -5.75961 | -40.78932 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2339a630-28d4-3de6-80db-ee45fd6ebf0a | -3.01997 | -49.44041 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5527d63c-a8e7-397f-93a7-d3bd6350e3fe | -3.25596 | -50.14001 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 928fac31-4cf2-3cd1-bb7e-259901cf8897 | -3.28661 | -52.09382 | 2025-11-08 04:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a3c2b7f-994e-3f71-8504-ae39dbbbbab6 | -4.97756 | -42.68443 | 2025-11-08 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ce50909-e2b4-3c05-ab0e-1df8a2605522 | -5.76568 | -40.79383 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d13f2b6-edf2-3905-a8ee-7b9af9df5a33 | -4.4637 | -43.22161 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c234610-d202-332b-a1c8-9107333480de | -4.6274 | -43.05354 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21d71e05-d18f-315b-b75b-6c7f7b502a89 | -5.61733 | -45.048 | 2025-11-08 04:06:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffe03a5f-ac1c-37e1-86b3-2203e2eec1ef | -3.34704 | -50.17912 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8aa63518-59c3-3b31-9e50-f13f343dcdfa | -3.24444 | -50.14911 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cce0ceff-6f2b-39ae-92e5-2002eb1fbd0a | -6.47467 | -38.65947 | 2025-11-08 04:06:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7d36c934-acdb-3088-8183-3c23e1b46569 | -4.64402 | -46.8779 | 2025-11-08 04:06:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c5fea96-7ad6-306e-bf26-5fe6d27d701c | -4.52195 | -41.92891 | 2025-11-08 04:06:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40797496-f6c8-3035-8b07-9cacb867d67e | -4.68382 | -46.39872 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f3d39b59-636a-3795-99c8-d4191b5291f5 | -4.2867 | -45.89486 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e2e32ac-3293-309e-9915-f424f2243197 | -4.64775 | -47.94888 | 2025-11-08 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f90e8127-123b-317f-b17f-704f7f79b875 | -6.21916 | -41.72044 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bd8b6761-e8bd-3e80-b930-659bff423c4c | -5.94064 | -38.18681 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f522f664-8728-3c27-aba9-b4381542f58e | -2.71205 | -49.54067 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b9e68b22-8a5b-3aae-909d-c8943ce54e1d | -5.65281 | -43.01181 | 2025-11-08 04:06:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41cc1ad8-42fe-3713-938f-46cd7f4d4418 | -3.40383 | -50.27573 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55820065-802e-3b8b-9454-77b628b29068 | -5.72442 | -43.53055 | 2025-11-08 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26f1bbd3-b4a5-3e35-91c9-1e5d0957973e | -4.89535 | -47.96151 | 2025-11-08 04:06:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a52f3677-0a0d-379e-a1f4-582c399f335f | -6.33426 | -42.06998 | 2025-11-08 04:06:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a25ccd86-f51d-33cd-b33a-6f1bd1ac8f58 | -3.15043 | -50.29965 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7581fd6d-48f8-3ec7-b688-a306d1f9cc23 | -6.32271 | -39.70003 | 2025-11-08 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b463c7a-895d-309e-baf0-b747c26bd2e4 | -3.24329 | -50.14886 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39aaaeec-e79d-3dbf-9160-00dc441f0ef8 | -6.97275 | -39.07452 | 2025-11-08 04:06:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad24ac0e-694c-3908-bcd8-32d0a7b9fc33 | -3.36414 | -49.51057 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a035631-da24-33fe-a801-a7af70b63e6d | -3.03024 | -50.27332 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 117af061-d9dc-3782-b257-0046fc521fe8 | -3.32396 | -53.35603 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d557dec-31c4-3c59-8d86-207a95b20277 | -4.68256 | -46.40635 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2133a4c3-2ec7-3570-8b31-5acfc85a05ad | -6.36882 | -41.74462 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 538179ca-0805-3905-88d6-618b2f617cd4 | -3.83465 | -49.82962 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aaf1e124-de8c-35f2-9b4d-59eda307717c | -6.10003 | -41.63442 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8836002-3db6-3841-8749-67aa8243f701 | -6.07674 | -44.04954 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8b5cea5-1576-36b1-8c5d-a250b3e08b42 | -3.95274 | -49.02077 | 2025-11-08 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9b8a47c-6402-3542-bcf2-1a76af8c52ba | -6.00414 | -39.51365 | 2025-11-08 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79c06eb3-0c41-3aec-927f-099a68e43c8f | -6.41294 | -39.59415 | 2025-11-08 04:06:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 37d24efa-a7c9-379d-ac4f-056b9ad91570 | -6.69447 | -40.76972 | 2025-11-08 04:06:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ebdde9a3-0c46-3095-85af-07618e9b6439 | -4.29372 | -45.68982 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 913c3f70-50c0-37a5-94a8-8de66326f8d3 | -3.3416 | -50.2107 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b881cf11-ea23-30c4-bb64-d527fad69bfc | -5.69361 | -40.49165 | 2025-11-08 04:06:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 637925a5-01c9-3db3-ba7b-4ae6c4cb96cb | -5.64941 | -43.01126 | 2025-11-08 04:06:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f63bc054-17ee-3d17-b6b3-81c794b6bb72 | -4.3649 | -45.62025 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 53e5ccc3-c1b7-3bd7-9e26-cac0ad87dca0 | -3.31771 | -49.13301 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef132c22-b4c7-3a5d-9810-31676bacb7b7 | -2.82571 | -49.83249 | 2025-11-08 04:06:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b68db336-6e9a-3750-b298-90358343e880 | -5.33591 | -45.14872 | 2025-11-08 04:06:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73e93f1c-d18b-36ff-8e71-23e9d7a222b3 | -4.83008 | -45.6076 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cabdc4b1-0c3c-30d5-affa-3e26e8e896b5 | -5.73021 | -46.46464 | 2025-11-08 04:06:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbdce8e8-0e4b-32fa-8ccc-de76d2be72a0 | -6.10458 | -41.71302 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0a70158c-d316-3ef5-93dc-e3fd68fcb57c | -5.65 | -43.00756 | 2025-11-08 04:06:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d9e07dd-0af4-3fcf-a3ff-92924e30bb62 | -5.77191 | -40.84077 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6f5cc71c-5d6d-3209-8668-52f90a12f7ab | -5.10186 | -43.99649 | 2025-11-08 04:06:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README15.md)
