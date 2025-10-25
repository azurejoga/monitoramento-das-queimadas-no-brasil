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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 656bb2d4-010d-39d7-af39-3a4a99150b45 | -6.92608 | -45.16242 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 159e6556-3085-3c68-9e39-ce488dc63416 | -7.42082 | -46.65395 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d05ceb4b-1279-3330-9ebc-91b54ad6e8df | -10.63928 | -48.05841 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47c2aacb-ad11-3515-98bc-90e54829b21c | -10.90161 | -48.0354 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd76c5ef-49c8-363d-a4b2-a1ce4559eebe | -3.61128 | -51.15827 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aa1caeb-0803-3f56-8521-290a713b2955 | -8.56064 | -49.86123 | 2025-10-25 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61f3c2a9-3039-3d49-89a5-38caf9d4328e | -7.48534 | -46.88311 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea582539-8c00-3417-bfa7-2e2e4510cb35 | -10.55651 | -49.77676 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3ce2efb-5c33-3512-9492-ff4809c0b218 | -3.91902 | -47.68645 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15a02c81-316d-38d9-bc90-9b15637780df | -8.1209 | -55.08163 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f514ddfe-6d12-3bac-959e-0888351a049c | -10.84729 | -48.96617 | 2025-10-25 05:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb25e179-be85-3a45-aa7d-86a24ebc15ff | -6.80354 | -45.42795 | 2025-10-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e98cd7ee-1bf1-3c05-8dfd-29998cd0cde2 | -4.83309 | -50.9319 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 564f8ce0-af96-3e25-9ef3-81be0b6295c5 | -9.29291 | -57.54189 | 2025-10-25 05:10:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5007c7ec-74c2-395e-adeb-f4121f4c6e2e | -10.00449 | -47.59196 | 2025-10-25 05:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deb13be5-4696-34e2-9ed4-1c6bbe996efb | -10.74192 | -51.68698 | 2025-10-25 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a36ea23-17b1-309a-9c31-7f89f0f9e459 | -3.7258 | -52.43938 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a02b5e2c-b186-3ec9-8dcb-43ce0d62342a | -4.87554 | -47.53504 | 2025-10-25 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0accbf3-8c5f-3e20-935f-f78e2912fbfe | -9.29015 | -57.5379 | 2025-10-25 05:10:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d740cb6-b7a9-38b0-a0cb-2bca44bd0080 | -7.79018 | -45.3946 | 2025-10-25 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4eb068b1-2518-3203-944d-74252a434d68 | -4.55226 | -46.60365 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2868eea4-b124-3b9f-8354-989a93b5af95 | -3.19368 | -52.21567 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bdce051-6bbc-3832-b6bc-4a4a4038e717 | -4.83443 | -50.93374 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f27fba71-7299-3e65-8e67-a750d82d03ea | -4.83933 | -50.93035 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1507e8bf-9f0f-3dd6-a671-1fdf160414a5 | -7.55568 | -47.1134 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 442841ed-0f7c-3078-8b85-bf91cb672bbb | -7.56148 | -47.11417 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7b62c68-3743-36c2-8969-b35bde6b5306 | -8.63148 | -54.66543 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5ed4e2c-464f-3495-b3d9-b3711c6c7065 | -6.80006 | -51.11062 | 2025-10-25 05:10:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d369c3c1-227f-3fb7-aa7d-e3a16cd1ca59 | -9.44719 | -56.64833 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e898b58c-bc3c-3a7a-aed0-3a7da114d4ae | -4.83812 | -50.9384 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc21d714-e6df-3c73-b1cd-f24530ced35d | -10.87175 | -48.04212 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 76556c4f-bcef-3e6b-9b2c-09ca8eaa17ed | -3.51397 | -51.09972 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a516dd1d-0ae2-3be5-a624-a5042007ca04 | -10.14565 | -52.13319 | 2025-10-25 05:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b451c08-6b2e-37ab-9405-ce7d51f97fc6 | -10.64076 | -45.24431 | 2025-10-25 05:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c2ccec1-f9ce-3259-bdd1-d7f75e1d0ddd | -3.72963 | -52.43993 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 458aa261-71e3-396a-8487-a419ab176c7a | -10.41584 | -44.50203 | 2025-10-25 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ea7d081-6e1a-32eb-b248-7cb3545d7d5c | -9.24456 | -45.61726 | 2025-10-25 05:10:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24898dc0-e0e8-3ede-ac03-85ae267c098e | -8.63108 | -54.89204 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e135e735-9970-31d1-9021-fcdd86f22312 | -4.83738 | -50.93255 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 03a1bef0-6a26-3d87-b699-d1e82998f561 | -5.54258 | -46.52676 | 2025-10-25 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b4799d3-6fd3-3158-b768-f0f81da110ce | -2.69526 | -54.76998 | 2025-10-25 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c76315a7-39e1-307f-8281-6595a6807048 | -10.63947 | -45.23335 | 2025-10-25 05:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1dbeafe-d150-32c2-a7a4-6d034e789fae | -10.66102 | -48.06947 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2529ce8-ecdd-30c0-aa86-a0bcc69550e6 | -7.38076 | -47.04627 | 2025-10-25 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe036a11-4fc4-3eee-8fbb-7c1f225e588d | -9.25512 | -45.5849 | 2025-10-25 05:10:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| df07e10c-7250-368c-af3c-9dce8338dbf1 | -3.43479 | -50.26453 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfc1ded8-9d39-31b8-9242-7495ab08fb91 | -10.64622 | -45.23443 | 2025-10-25 05:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63a594a9-1dce-36f0-9d0f-0c014dbb6102 | -10.41863 | -44.49778 | 2025-10-25 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82e0e5f7-7da6-3a45-a135-362c908bb5c7 | -3.69362 | -51.33532 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54bd49f6-891e-30a2-9477-f6cb6ef777ca | -4.84597 | -50.93382 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6923f585-76fc-3360-8872-67b40ab70510 | -5.69745 | -49.32066 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2815491b-7505-3f46-b255-461680dd70d6 | -3.99152 | -50.51848 | 2025-10-25 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50dd40bc-2354-385f-b311-a73a22be7afa | -10.63819 | -47.92437 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58d0f6d8-2cb3-35f3-bae1-c79de7c3a7b6 | -4.81647 | -45.57717 | 2025-10-25 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fa846f3a-7ef8-3003-a6d3-536359c764d5 | -3.86945 | -51.89032 | 2025-10-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 696821e2-2f3b-3382-8aa8-5388afb08c5e | -4.00355 | -48.3196 | 2025-10-25 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9806b1cc-2c81-3301-b0da-6046f15ee357 | -10.75744 | -47.91659 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e5072d9-bd5e-344a-94c5-6485c6e5c6a9 | -8.01457 | -46.71981 | 2025-10-25 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c19bd39-7c21-3579-af57-fce07306ab27 | -10.00395 | -47.59615 | 2025-10-25 05:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60d0f207-c010-3fb7-8f4e-15431de57d73 | -9.39997 | -59.36426 | 2025-10-25 05:10:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 238989a2-d2cd-3542-b0e6-582db94b746f | -6.79504 | -46.46127 | 2025-10-25 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27f9acc8-3f49-350c-b5d3-7dd7ba1f7f6c | -10.86562 | -48.0448 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33a44c0d-2db2-32d5-8cb7-822b17a34912 | -10.63835 | -48.06594 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68bcb15a-c074-3050-9a17-efcdbdb97aa3 | -8.61086 | -54.95524 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abca4b6d-f04b-36bb-901b-f7598947538e | -4.55763 | -46.68875 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6bbcee56-8ea1-3007-a0b9-3986f78d60f5 | -4.55167 | -46.60777 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 511c0fbc-6532-360a-8b64-b760808404af | -4.83872 | -50.93438 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44849a13-ed0f-3125-b030-09f583886a0f | -6.41446 | -53.66077 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37fb588d-b437-367f-aad5-fcdcccd57294 | -3.43542 | -50.26023 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d146822f-483d-3e8b-a389-62d6756d78a5 | -3.77015 | -51.38464 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db4ee44-61c4-3838-a8cb-bc756fbc2a3a | -8.61265 | -54.65554 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54626335-2fa9-3182-817c-1cffbcf9a420 | -8.86987 | -48.28669 | 2025-10-25 05:10:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bb2cc63-febe-3043-a1ea-3c9bbc9e2dbc | -6.92601 | -45.16216 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e63b1b34-e2ad-30c8-8abd-51f1b8ef9bdb | -3.91939 | -47.689 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e0589f6d-22c7-3340-aead-6810e0b807d6 | -3.92339 | -47.69374 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7b28db3-33ef-3cee-9721-dcf3a7ffa625 | -4.97587 | -48.36131 | 2025-10-25 05:10:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45879170-9606-346b-9d72-a980bf5e4ae7 | -9.74891 | -47.8325 | 2025-10-25 05:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 874359a1-aa86-35aa-a431-6ef05789021d | -8.55197 | -47.38 | 2025-10-25 05:10:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9ea36b4-637b-3112-ab3b-6fdca6078555 | -2.8998 | -53.13479 | 2025-10-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd91990b-a60d-3715-9fbe-f4605fc8a3e9 | -10.66761 | -48.06298 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9a124a3-9123-3df3-af4e-62765d47645c | -4.15852 | -46.78876 | 2025-10-25 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 964e6c58-1ed0-311d-9ce0-f23a21907325 | -6.88846 | -43.61268 | 2025-10-25 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c723472-a837-39ba-958a-9910de4026c2 | -5.82091 | -52.10217 | 2025-10-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a2cb28-35a6-31b9-b165-4f6006ded7d0 | -9.26713 | -59.49171 | 2025-10-25 05:10:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 383476f7-4836-3b79-8d7a-f6197287e407 | -10.87863 | -48.03338 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d856e306-b512-3a1a-b446-beea4c0a929b | -9.32406 | -45.18509 | 2025-10-25 05:10:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20306b63-c340-36a1-a573-ad913a3312c0 | -4.55189 | -46.68809 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b879d4fc-2e75-3beb-b4a2-f41f2fb4cfc4 | -6.24038 | -46.39956 | 2025-10-25 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa4a0c5b-7aed-399a-bd61-48002add4d2c | -6.91882 | -45.16672 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5013d5d8-5d89-3dbb-9b11-43b0202ccc10 | -10.63872 | -45.23964 | 2025-10-25 05:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 468ca1f6-a22e-3d4c-b7f8-63aa6896fbff | -7.99006 | -49.25294 | 2025-10-25 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82174139-a52f-32a2-a0a9-9b7bdd325ce1 | -10.62111 | -52.18545 | 2025-10-25 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 334210ee-6a61-3eb0-bcfa-1dcabcdf7c78 | -8.3329 | -46.18067 | 2025-10-25 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35336636-d5b2-3c99-b230-d0922616047e | -10.90725 | -48.03677 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ad0c3eb-10b4-3cfe-9e96-e5557a65d715 | -5.70873 | -49.31143 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7452c985-561f-312b-93cb-a6b019f91566 | -8.33905 | -46.18206 | 2025-10-25 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bdfd2f1-d013-33f7-bdf8-02eb9ed06356 | -9.96261 | -48.265 | 2025-10-25 05:10:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7245012-a4d2-39ae-9e67-a1346bbb2334 | -6.91819 | -45.17167 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15176a16-fe03-3e76-88b4-49dd41eb51c0 | -9.92952 | -47.99824 | 2025-10-25 05:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae7c90ba-59dc-3ebf-858f-06b2f27826d3 | -9.57858 | -49.6786 | 2025-10-25 05:10:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README54.md)
