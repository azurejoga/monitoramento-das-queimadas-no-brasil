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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c46ba64a-5272-3307-ad08-e1addab12ed6 | -6.87267 | -39.05429 | 2024-11-16 04:01:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1a6a6b1-ff55-32df-8ef6-9accb584ba32 | -3.19116 | -45.55328 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b993ec9c-43b4-307f-9dad-af19648fd690 | -4.37335 | -45.62014 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 126d5772-3a12-3813-8f7f-db0230d8c75f | -2.54879 | -46.89503 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 76ffc4d0-e83a-3b24-bf2a-11e6fa850c3d | -6.16718 | -41.15735 | 2024-11-16 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d2d4151-f4d1-3b58-a66d-4ef26ab493ba | -3.7527 | -44.37944 | 2024-11-16 04:01:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7087efb-11e7-311b-b4ee-758d62fbe84d | -6.30051 | -39.47968 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6bc8d491-07ca-36a5-9f4a-12ceb3192bd9 | -3.72495 | -45.65942 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb867fb6-b7f7-302f-b43f-a65f5edadc49 | -2.65725 | -46.1986 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36ea574a-0709-3ede-87cd-ab1a7eedfa27 | -5.97183 | -42.16169 | 2024-11-16 04:01:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 809f6495-9a28-371e-a891-05fe20e5a169 | -3.06457 | -45.34964 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 81b44706-1931-3664-a822-cb42585cdf00 | -5.67765 | -35.6481 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 1b79123b-24a2-3c2d-b096-a4796b8f8d99 | -3.78055 | -50.10974 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faa22cb3-4bd9-3bb3-848d-f613b2b3db0f | -7.92755 | -39.55367 | 2024-11-16 04:01:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b6033cd5-bba1-35ae-9644-bec153288649 | -6.11618 | -40.01074 | 2024-11-16 04:01:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2229c1d5-3f66-3687-842d-b10d9f9978ee | -5.84975 | -38.45426 | 2024-11-16 04:01:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ce7bae1-80b6-30b6-8b1b-a5e28ee8be56 | -4.00357 | -44.34056 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 254a226b-e047-3128-a7b5-ca763c645174 | -3.94418 | -46.70894 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06f2e196-219f-3f27-b86e-026ff015a3c1 | -5.6731 | -35.6523 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e17c2b39-a647-3628-95d5-17d0c1a19d12 | -4.38078 | -48.07611 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65974901-9c77-329f-9b25-2dcff6a1fac9 | -3.73361 | -45.66079 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9af84c5c-d02a-31fc-97b2-815d307b32b3 | -2.35944 | -49.12222 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05961e31-20c9-3c52-ad4a-b464abcd9f41 | -3.99944 | -46.19209 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ab27306-82b9-3547-a3b9-25496a2693f6 | -5.41091 | -45.154 | 2024-11-16 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b204e021-8ce4-3aa5-a462-ed967188ff3b | -2.64593 | -48.48124 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 526ceb44-3b77-36b9-adff-509a2226d72c | -2.85938 | -45.24913 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97dd1fe4-06d9-3c12-aa7f-cba9f54cf8d4 | -4.01702 | -44.58303 | 2024-11-16 04:01:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a2d8493-3fa0-3190-b544-cf00bf25e6c5 | -6.43973 | -47.86303 | 2024-11-16 04:01:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70f7e15d-e2a0-317e-aaf4-075eea6f4f19 | -4.55468 | -45.75624 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29d14d12-1cd3-312a-85eb-3a95bce98ed9 | -4.99812 | -44.31721 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7ae48536-8f08-31ff-b803-ca5a46cb7e7e | -4.15116 | -50.76625 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7ab9a7c-650a-3284-9df8-3f92e16db6dd | -7.40401 | -40.38771 | 2024-11-16 04:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0fc8a785-1cf9-3df4-a33e-ab90ac62eaf7 | -4.30028 | -48.0664 | 2024-11-16 04:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c3a7e57-0e5c-34dc-b00b-ded7b6696e7d | -3.50353 | -47.21916 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a38fe31c-b5b6-30da-9482-62df07515bc5 | -3.06521 | -45.34563 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 72d36f2a-37e1-3082-b51a-0e4fd9df3525 | -2.8998 | -45.34524 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 66721d92-7549-335b-b1e2-772a7f375993 | -4.81389 | -43.2218 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f40196f-3475-3f0d-9d26-3f032cb957ee | -5.23724 | -44.91628 | 2024-11-16 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 816e84eb-bf2e-3b72-b073-7ed8b22d04e2 | -6.74862 | -39.02014 | 2024-11-16 04:01:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 311fa1dd-c181-3a99-a02a-2a9e0d57133a | -5.4518 | -44.01694 | 2024-11-16 04:01:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7880b14-1656-313a-be3c-ed9760fa0927 | -5.59013 | -44.58498 | 2024-11-16 04:01:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64b7a3f0-6cd7-3d61-a308-21877a4231cc | 0.79051 | -50.74043 | 2024-11-16 04:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7eabd38b-8269-3d20-81c6-82867bcdf811 | -3.87964 | -45.02328 | 2024-11-16 04:01:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 177832f3-cad3-3458-906a-a25a045d2f92 | -5.67449 | -35.6427 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 3dc45308-a09c-3a4b-bc90-b3507f38d5f4 | -3.98186 | -43.71704 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8084f7c8-4552-3933-a36a-d1ffeac8763a | -7.43727 | -35.15141 | 2024-11-16 04:01:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8de576b9-b467-381a-9a7c-9a8d8fba144e | -4.56149 | -48.01368 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 799920f3-74cb-3bf6-b06c-2c85e16c6bc6 | -6.85983 | -38.89182 | 2024-11-16 04:01:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f9824843-728b-30b7-9357-5c0f6336b8af | -5.15129 | -42.96592 | 2024-11-16 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 102da330-00d9-3f6b-8167-6b55c700277a | -6.0463 | -44.03898 | 2024-11-16 04:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac19b238-ad34-3593-b3e3-3c4b4c3d45e7 | -3.74472 | -50.18255 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb2b5ff4-268e-32bd-aee8-2d93475d7d99 | -3.89689 | -46.47798 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3313301a-4a38-3022-a17d-c3852cb157c2 | -3.99079 | -45.85769 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d8c1f16-1c1d-3038-8ca3-d132373ce65e | -2.2869 | -46.45095 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 568fcb8b-4072-3f12-b964-430ffd1dec97 | -2.95228 | -44.29897 | 2024-11-16 04:01:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94aab0c0-debe-3c3f-b1df-311e190aa5fd | -4.3806 | -45.62944 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a81aa1c-98b1-3ba0-bba7-5ccc8bdf095d | -4.40568 | -43.81172 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e079feb1-71bc-3378-b5ec-ae13cbe94890 | -2.35744 | -49.11049 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 828a6c08-8e7d-37b3-ab23-c7e54cda7131 | -3.41224 | -42.38908 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd78cdbd-2e36-3e09-896c-dc458e4e4fd5 | -6.02591 | -39.53984 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a3a192e7-5859-3c0c-9bc3-d90c7cfdd0cb | -5.23783 | -44.91269 | 2024-11-16 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f4202b3d-270a-3016-8b9e-59dead9da75a | -4.24965 | -45.9021 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d5a2398-677b-3208-9a50-5de16fd76221 | -4.37205 | -45.62806 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dad2ca0c-603c-36a7-95b0-8deb3c7b4006 | -3.9849 | -43.72227 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57f1b6e5-dea0-3cca-8a42-ee6778743086 | -2.21878 | -47.2122 | 2024-11-16 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bb62520-710c-3507-bbfc-bd6a24613dcf | -2.65341 | -46.16466 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9164dcf7-a3ce-3bdf-9ba1-16e35ebf22b3 | -2.77921 | -48.57952 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 45042095-d18c-345f-9aba-31993d500f80 | -3.78808 | -50.10355 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4045eaf0-79d5-3806-8466-0afb3b1c68dc | -2.22007 | -47.21418 | 2024-11-16 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3f1a169-10b0-3668-b9c4-01a79ad638ce | -3.28129 | -45.50323 | 2024-11-16 04:01:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 9d4483dc-371a-3454-a9b4-35254e7eaa16 | -3.24335 | -51.52029 | 2024-11-16 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb8ebacb-ddd6-3092-a5b0-79a653339734 | -3.12303 | -45.74966 | 2024-11-16 04:01:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a93df03a-3bb5-3081-b815-7575256c209a | -7.85933 | -42.08803 | 2024-11-16 04:01:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b89073b-ed7e-382b-91a9-dac0347708b2 | -3.99148 | -45.85352 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a39fc6a2-fc39-3243-b747-d8cbdc4617ce | -2.64647 | -48.47787 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 741d8344-d5fd-3408-bc7b-1ba0629dfa46 | -3.5027 | -42.00488 | 2024-11-16 04:01:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6576d1ea-296a-3aa7-9db0-6889be8ce15a | -3.28255 | -46.20612 | 2024-11-16 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff702fb4-69a5-3336-a4f6-07329dc0bcc7 | -3.59681 | -50.35058 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72e591ab-6370-3514-be5d-49e494b53d06 | -5.15196 | -42.96178 | 2024-11-16 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8c111ae-884d-3e74-8726-b6ce3022db4e | -6.20241 | -35.40175 | 2024-11-16 04:01:00 | NOAA-21 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 068c26d6-2057-3ada-a696-8ab3c84667b0 | -4.35884 | -45.87012 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75941cdc-f305-3356-bd52-f92a1d7848cb | -2.77805 | -48.5864 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 119b6b0d-fa58-3b02-8cb9-c0f18d155337 | -2.66497 | -46.84621 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09d1d540-5bd5-3d5d-9ed1-bd1cde7c15da | -2.79274 | -48.56451 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d02cd49a-db40-3b7f-803a-cb78002ce378 | -3.5193 | -44.71676 | 2024-11-16 04:01:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1d0cb46b-9f70-3bb2-a513-df83fb3a9d69 | -6.64095 | -39.71784 | 2024-11-16 04:01:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 249bdbb6-e86b-336f-abb6-c26a8ad9f928 | -7.40293 | -40.39463 | 2024-11-16 04:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| ed298cb4-adbd-348c-bbab-6f407b76d969 | -4.81453 | -42.91577 | 2024-11-16 04:01:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 807fdf93-abfc-3199-bbd3-2913e595393f | -5.48756 | -43.76944 | 2024-11-16 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb2c0a08-4c7e-34dd-b0a7-88212ff90628 | -3.99517 | -45.85832 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1acb8050-6015-3a70-831b-1ffb2913f7ab | -4.87639 | -45.05114 | 2024-11-16 04:01:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b060104-f3a1-3785-beb0-f7a943342a8b | -3.76189 | -44.39855 | 2024-11-16 04:01:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4036652-f8ae-354a-ad17-8135e6681dea | -6.66371 | -47.87712 | 2024-11-16 04:01:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04839ed2-51a9-3b06-bb7d-6ba11cbc673a | -2.71078 | -47.72809 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6dd54ad-9279-36e1-b940-18fc29ffdd55 | -4.22428 | -50.6776 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd060e51-e6d6-3fce-be69-5d1b05ebf61c | -2.58683 | -47.48236 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5f444ae-37e5-39df-b665-4b24cb7359c0 | -6.54755 | -41.96208 | 2024-11-16 04:01:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0b0cc84f-215e-3ff5-a259-2b8ec86b150e | -3.56551 | -50.24844 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 749d6cad-c863-3a67-934d-2c9ad99975b6 | -3.76901 | -50.78742 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cd14443-fb76-34dd-b592-e5463d5075e9 | -2.21996 | -46.86276 | 2024-11-16 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README19.md)
