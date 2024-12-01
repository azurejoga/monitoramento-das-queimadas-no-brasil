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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0941f907-3cee-35db-952c-8fbe59d8c655 | 0.93914 | -50.75381 | 2024-12-01 00:34:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1371e05b-7e00-32cc-be25-c89e39dfed5c | -3.39684 | -45.89563 | 2024-12-01 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 250048b4-9e83-3725-b985-1d192aad9029 | -2.57317 | -51.87215 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b819ea94-8fca-36b5-b89c-a8208b862068 | -3.50844 | -53.86527 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2756b7ec-3d50-3b3b-8f1c-413d80dcfe16 | -3.26282 | -50.20129 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ff77438a-d7f9-3184-ad4b-7f8c7f5247c9 | -1.9461 | -45.84484 | 2024-12-01 00:34:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| d1b4cce5-7527-333a-bbb5-2b4340a61bc5 | -3.38598 | -49.86328 | 2024-12-01 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b5aa7c9f-ef1e-3953-b9c9-96740afc554b | -3.21499 | -45.7713 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4f719e1c-0984-3f3c-b627-4b5618f4a25f | -2.11741 | -46.56115 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 32cbf822-e12d-357f-ae57-4879c90ba611 | -3.35942 | -43.82196 | 2024-12-01 00:34:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 7091deca-cc5e-3913-9708-f320dcb16569 | -3.27479 | -53.63744 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| fbba11ed-89b4-3646-812b-abb09760d12a | -2.97658 | -46.94735 | 2024-12-01 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 39fe72e8-96b5-3bc5-b0e1-4e86c15c7fc7 | -4.10719 | -49.0721 | 2024-12-01 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0ecc1602-5eb0-3572-8f2a-512070029760 | -2.6389 | -46.12748 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 562c63c1-144a-3e04-b1cf-4a2336d9f117 | -3.7151 | -51.07087 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 20d2288b-d35c-3b3f-b4ef-f8876012f2d2 | -3.00143 | -45.42012 | 2024-12-01 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9079c9d2-69eb-384a-a7eb-85aab39f84d6 | -2.12103 | -46.23625 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 177f2df7-64a6-3aa6-b696-9dc0d52e8b1f | -2.13062 | -45.98541 | 2024-12-01 00:34:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76807ded-4790-36e1-a86d-4d38cf4df84b | -3.00928 | -45.14588 | 2024-12-01 00:34:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e420ff0-c58c-3a37-90a9-33b17b2be990 | -3.30847 | -45.78256 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 04842b50-ff50-3fc5-b49a-8bf09ba79d76 | -2.92284 | -51.43562 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8a2e027c-e0e5-3c42-b114-4d6dd05bb486 | -3.12247 | -53.8208 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0fffa86d-b19e-3427-a24e-919fbbfb5733 | -3.20022 | -53.10327 | 2024-12-01 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f31101bc-2d91-3df5-acd0-24b531f5be59 | -2.11299 | -46.24764 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 76ff4bf9-f7b5-3a9d-89ea-e1417ea271a8 | -3.21204 | -53.13097 | 2024-12-01 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| cd2113c1-7ada-3146-b164-e7ddbc72b0bf | -3.32604 | -50.18734 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 46359b8d-7f8d-37c6-96f4-70d6d652a282 | -1.72237 | -45.76139 | 2024-12-01 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4988a624-82d0-3fdd-bb61-d7b9b396eed1 | -1.96913 | -46.467 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7894ec03-18e3-3b6a-afaa-b25dc1e3584f | -1.52235 | -45.90538 | 2024-12-01 00:34:00 | TERRA_M-M | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8950a012-d711-3c0f-ad38-eb7e225b5281 | -3.67417 | -50.24456 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ce402678-fa4f-3b5e-aa47-c1c4d5f80b07 | -3.30683 | -53.86733 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 8d124125-acb7-341b-ae0d-2bfa6ba7ba2e | -3.30792 | -50.0491 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b48448af-ada9-3fb9-9f7b-50ba0328eea2 | -1.27366 | -47.86369 | 2024-12-01 00:34:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| efd586aa-9daf-304a-a33f-1d7e128112df | -3.03153 | -51.53615 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 390cce79-b82d-3567-8e35-58dceb8aa152 | -3.12287 | -51.31594 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| be63ce0f-07c0-3d8d-b431-ce3719efc028 | -3.32155 | -45.67071 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e54b3bca-af33-34be-9f73-fe9975deec85 | -2.83826 | -49.87893 | 2024-12-01 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| cc1fb5e1-2106-3dce-867a-0d2fc0cdce6b | -3.27574 | -50.19954 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 09b0a8ea-8ba0-376b-9594-121135e238a8 | -1.64078 | -45.50109 | 2024-12-01 00:34:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51e32e64-495c-3139-8f51-38d3bfbb1b18 | -1.44809 | -47.12016 | 2024-12-01 00:34:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 128f1f3f-d84e-3b6b-bc54-06121cd8fcaf | -3.26166 | -53.63383 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 49740e25-0ccd-39d0-84b8-25cd5b2f99cf | -3.01587 | -51.78839 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 21159e94-e09b-30f4-a0ca-c80f95ac027c | -2.69768 | -45.42326 | 2024-12-01 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a102a1ee-148a-38ce-880c-f2acf45a7f3c | -4.10152 | -49.07856 | 2024-12-01 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 526b61d7-99d2-315b-9295-2278abf1c2c0 | -1.5237 | -45.915 | 2024-12-01 00:34:00 | TERRA_M-M | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0d401fc9-0849-3345-9034-190cfef89584 | -1.51313 | -45.9067 | 2024-12-01 00:34:00 | TERRA_M-M | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a8f12063-b049-3480-9736-dfa55e38be09 | -2.67573 | -46.60921 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3f64fc1f-4b9e-3ca0-98e5-61184fec4f59 | -3.45719 | -44.921 | 2024-12-01 00:34:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de334282-6a4e-312f-b903-393e3bda1546 | -2.66183 | -51.85483 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 49a31dd6-858d-3841-8dd5-fce76cbcb5f5 | -3.68508 | -44.70342 | 2024-12-01 00:34:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12709df6-bdc1-364a-a9b7-63ed9e40432f | -2.57675 | -51.89881 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 38be4850-516f-343a-a95b-f98e052ef4d0 | -2.80651 | -45.93918 | 2024-12-01 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 08b15db3-ccdd-3f2d-b162-47bc5a577712 | -2.73999 | -51.75685 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 8a87a0d2-5d00-3901-ad6b-1c172303fc7c | -1.27925 | -46.347 | 2024-12-01 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d394db94-217e-3a13-ab7b-9e4d5c316bf1 | -2.92292 | -44.98563 | 2024-12-01 00:34:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cceaca51-48ab-338c-bdac-2c04e888f060 | -2.60692 | -45.43222 | 2024-12-01 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4199b452-067c-3c9d-a7c5-034a4eb5ebd1 | -3.25784 | -53.63935 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| db75ef0d-4db3-35cd-8637-3e2cf3f3a90c | -1.95534 | -45.84357 | 2024-12-01 00:34:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cd1b38cc-f1ab-323d-b71a-79ae8b35b840 | -2.34215 | -45.65182 | 2024-12-01 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 11594a08-791d-36a1-a9ee-31091c2b5cbd | -1.71141 | -46.14494 | 2024-12-01 00:34:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f83f91a2-5641-3d65-a273-9ddb76f397ed | -3.69277 | -51.84166 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 885789e1-c0e2-311f-9af0-9401339468cd | -3.45845 | -44.93019 | 2024-12-01 00:34:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9a4b39e3-7613-35b7-bafd-1ac88b825b46 | -2.84248 | -49.89078 | 2024-12-01 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 43624b89-5f77-362b-8b43-f358947ba573 | -2.12243 | -46.24632 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| eb234b18-1ca9-33d8-b74a-8c8db1b91102 | -3.85054 | -46.53242 | 2024-12-01 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 84c48568-5722-34ea-a509-4c95d0a85ed3 | -2.67947 | -46.14238 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d0131778-cadc-3065-97c9-03634394bdd6 | -2.71115 | -46.19369 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2e538b23-9a3a-3049-82bd-e3078c4d2a67 | -4.07716 | -50.03817 | 2024-12-01 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 324ccfd8-7820-39f1-9647-6caaab6ec582 | -3.54822 | -50.18606 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c4fdb178-fa59-3a6b-a2c5-f8d4892148ea | -3.2947 | -47.03105 | 2024-12-01 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 22c38199-d025-318d-829d-9a86377a0142 | -3.51031 | -53.85798 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 8fa4ee27-135e-318f-a7e0-4249bc9d4def | -3.4501 | -45.68061 | 2024-12-01 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9149deec-9c23-3d1b-b04f-2bb9bb82b732 | -1.25669 | -47.51227 | 2024-12-01 00:34:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa660d68-c7a6-3857-bb05-97619711a010 | -2.11884 | -46.57164 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3db85ab5-dc4e-35c0-9cbb-5bd1c1b8d8a2 | -3.32743 | -50.19267 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| d242f9bf-76f4-31a2-ae38-a57972a43362 | -1.7981 | -46.63033 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a3d8c7e5-956c-38d7-8d3f-2ccddddc3e02 | -2.89698 | -51.56664 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0a75f4f1-f76e-3338-a9ea-d16631d1532c | -2.47706 | -46.57298 | 2024-12-01 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2054fab9-40a7-3729-b9f1-a41a516585a8 | -2.73033 | -49.37325 | 2024-12-01 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1636e02f-7ef8-3eb4-b776-d101c37f3fbb | -3.50516 | -53.8172 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9385330b-d031-33a5-9943-888186fdf4db | -2.71228 | -46.13143 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19a77509-857d-33a1-9068-c414cefba6e9 | -1.12014 | -47.48429 | 2024-12-01 00:34:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3cc56b46-8efb-32f1-a188-340d0f7f9d78 | -3.08692 | -45.5089 | 2024-12-01 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d8a818e1-21c5-3473-a1b3-268fc5d52b79 | -3.12307 | -45.98272 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6722249a-11cc-3e91-9696-7e12659460f7 | -3.37809 | -43.4897 | 2024-12-01 00:34:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0fa410ce-71e4-35d2-88bd-1825ac7cebd0 | -3.02837 | -46.87682 | 2024-12-01 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a5e9ecbd-a44b-340a-866b-477db9e27dbc | -2.46596 | -46.56366 | 2024-12-01 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9c3ce29-1639-3675-bfef-5abe2684b0b4 | -2.54871 | -45.6109 | 2024-12-01 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 078534fa-09bc-3fb2-bc66-7f653709fb40 | -4.18887 | -50.67132 | 2024-12-01 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6b77e264-168e-3443-90b4-397fd7aa4d4d | -1.61276 | -46.23521 | 2024-12-01 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dcacaf94-a403-3ff4-8df1-ff91c6bb7914 | -2.99006 | -51.05575 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a48e5e8a-4a62-3950-9081-5428be6e42cf | -2.08884 | -46.28193 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d6bc6a9-a258-3830-8621-6ba6ad5e4ca7 | -3.79318 | -48.08582 | 2024-12-01 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| aaebfa28-c202-3362-9381-aa447b3e3313 | -2.75035 | -45.94705 | 2024-12-01 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 0887f513-f107-3f7d-a56c-a62fc82a0a39 | -4.19185 | -50.69347 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 191da7cb-a2b3-3abd-9106-c8fb4152e75f | -2.9727 | -48.04319 | 2024-12-01 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4f4e6817-eb37-364a-b278-89513fcfd26d | -2.60562 | -45.4228 | 2024-12-01 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 23304100-af9b-3fb0-8832-b7579a44137e | -1.44658 | -47.10906 | 2024-12-01 00:34:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 172ccd8f-4ca2-3f26-b928-4adeb34b2098 | -2.63014 | -54.20583 | 2024-12-01 00:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 276bcda6-379f-39b7-9341-6918ff2c1092 | -3.03175 | -50.23097 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README7.md)
