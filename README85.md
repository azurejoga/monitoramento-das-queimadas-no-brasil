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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00fefe9f-d92f-3148-b4bd-55ffe5084a96 | -4.46268 | -45.89995 | 2024-10-10 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| accd424a-6fe8-3e6e-a4c4-f0ae0933b465 | -4.28282 | -45.47044 | 2024-10-10 04:42:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b190588-3df3-3de8-ae59-e280ce9569ad | -4.28229 | -45.47397 | 2024-10-10 04:42:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb2dbdb3-933b-37ef-be99-930d5758a0d6 | -4.28176 | -45.47749 | 2024-10-10 04:42:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d66518-2d01-3fab-b052-f138ce5b37bc | -4.27879 | -45.46983 | 2024-10-10 04:42:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7ce449a-c4b8-3563-b7e0-9a12bfa5321c | -4.27826 | -45.47335 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 759b58f2-2ae4-3ad4-9fcb-aa0469c001f3 | -4.27475 | -45.46924 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07c644c8-e512-38b9-ac92-6fad5fc00a95 | -3.91089 | -44.86921 | 2024-10-10 04:42:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9276cb5a-d454-3e0a-acbd-b75a1995a18c | -3.91033 | -44.87301 | 2024-10-10 04:42:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6648f57-35f1-334a-b95a-1df21fd61eac | -3.83202 | -45.56303 | 2024-10-10 04:42:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e172a2e-7b32-3f5a-80bc-f670e6a77528 | -3.8315 | -45.56648 | 2024-10-10 04:42:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a7717c-20bd-3ac7-bf4a-b8823cfb7e99 | -3.80937 | -45.49628 | 2024-10-10 04:42:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4f1155e-8f5b-3089-9d91-d4e98ab68b27 | -3.80886 | -45.49974 | 2024-10-10 04:42:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4489abc3-84d4-379b-89ef-3bbb5eb2ef2c | -3.80537 | -45.49569 | 2024-10-10 04:42:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d062d5ed-d009-30ec-b530-7442cf9e3861 | -3.80486 | -45.49914 | 2024-10-10 04:42:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e788714e-045f-38ae-8786-5a346cb24183 | -3.7187 | -44.96449 | 2024-10-10 04:42:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de5c8b4c-474c-39dc-91be-9bbb5c142d5a | -4.9468 | -45.50804 | 2024-10-10 04:42:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1328368-cea7-3e58-b648-af2e9e160046 | -4.92917 | -45.43109 | 2024-10-10 04:42:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de8e0dd8-8cc4-3fa2-bae3-3be9e925e065 | -4.88941 | -45.6982 | 2024-10-10 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 734a6d78-4da7-3889-9812-ae0358cc5141 | -4.88888 | -45.70177 | 2024-10-10 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e987c6ff-7e18-3619-96b1-8af63497d77f | -4.88488 | -45.70111 | 2024-10-10 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8516cdb4-9efb-3f91-b865-7b90a87b8546 | -4.88161 | -45.33519 | 2024-10-10 04:42:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d2046b7-1c57-3501-a7ea-f4a1d8b13217 | -4.86532 | -45.80514 | 2024-10-10 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d3fdd70-66a1-39b4-949e-af6464d305b1 | -4.86482 | -45.80848 | 2024-10-10 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d27d421-cc1a-3877-a0ea-adb008b8338e | -4.83978 | -45.41829 | 2024-10-10 04:42:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a87394ab-135c-3a7b-a48a-0bd686013038 | -4.8357 | -45.41766 | 2024-10-10 04:42:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eddb9e2-3b84-379d-a932-66477caaea84 | -4.73679 | -45.68282 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 186b36f3-f6c7-319c-a0bf-fd83ab5682ab | -4.73452 | -45.68299 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27011e61-7c35-395c-8186-d8341b748e5a | -4.73278 | -45.68227 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1174b30c-fb3b-3567-a9ba-8bf4738a821d | -4.7253 | -45.67764 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94e0cec5-84ed-3a39-b379-97de869feb1b | -4.72129 | -45.67709 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b67b2f97-0467-361a-bc11-d9ced96cb287 | -4.72075 | -45.68065 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffc4d466-824d-385f-8276-99c01cc104cc | -4.6905 | -45.63677 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbd00b6d-9957-3ac8-b3ea-958fcdf000dd | -4.68753 | -45.81865 | 2024-10-10 04:42:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1be49cd-0ccf-31a7-92ed-e46aa6a1247f | -2.07469 | -47.1278 | 2024-10-10 04:42:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3985339a-d919-38ff-9bda-c84661a423ea | -1.40981 | -46.4454 | 2024-10-10 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd723711-ddca-3999-9c79-ca6da4259a6a | -1.3597 | -46.64943 | 2024-10-10 04:42:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a15ef2dd-6426-3fe6-8466-36f62bee8041 | -1.26359 | -46.35213 | 2024-10-10 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c1d62f2-caed-33a4-93cf-863efa729ce6 | -1.26291 | -46.35643 | 2024-10-10 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbd7a324-12cc-3eab-99a9-0fee2f0005c0 | -2.18797 | -46.09362 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c7d2651-8874-3a7d-b240-bbe31fd9c891 | -2.18792 | -46.09609 | 2024-10-10 04:42:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72eb695e-76e0-3e3b-966c-1c505b89962e | -2.18485 | -46.09094 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8988ed4e-7130-30fc-8230-6d0158abcce1 | -2.1842 | -46.09303 | 2024-10-10 04:42:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9698313f-358c-3ace-985f-20e9f8991664 | -2.18404 | -46.06959 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8118609-e9f6-3525-8292-72fdd7a70cfc | -2.18384 | -46.07203 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26a87dee-d0bf-3d33-8e3c-60493e01b567 | -2.18007 | -46.07145 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16192c78-74d8-35f9-8e5e-08a9825420f9 | -2.17321 | -45.94067 | 2024-10-10 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b8de861-5164-3b0e-8e9f-fbedd9c12ae2 | -2.16941 | -45.94007 | 2024-10-10 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08b504d1-4338-31d0-9659-ddbe20eebe52 | -2.16869 | -45.94472 | 2024-10-10 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4406329e-dc04-321c-9e4e-4967c45cb10b | -2.16181 | -45.9389 | 2024-10-10 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c967157-2257-3c8b-84fb-f887a19dace1 | -3.0595 | -45.94452 | 2024-10-10 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93b4668b-f95f-386e-a020-ef53c3b0be3a | -2.58956 | -46.12719 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55506561-6528-31b7-bf4d-91dbf065d86c | -2.53927 | -46.15251 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da7ad75-86c2-3247-bb98-8955d07bdb49 | -2.5355 | -46.15189 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f03a6ac-fe76-3b27-860f-9d48efe63302 | -3.36376 | -46.5065 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4efa69b6-15e2-350b-af18-cff5b2c36a56 | -3.36136 | -46.4972 | 2024-10-10 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56691319-b6ed-3c46-b506-350edd017f0d | -3.30816 | -46.99068 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 824909f6-22b1-3a28-8fa5-5b2b2e7177ed | -3.27579 | -46.34706 | 2024-10-10 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f1f145-ed31-3c7f-aeb7-9d5df9426de8 | -3.04552 | -47.47193 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c7f4f13-bb93-30ea-b11d-4b54a32c7b7d | -3.04198 | -47.47137 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 169c8138-a4d9-3936-8a66-a37a20bc1426 | -2.84056 | -46.70057 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c4c40cd-3191-38bb-a145-1fbed2dac68b | -2.83689 | -46.70001 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8108faf8-1406-3f23-acc0-d477c1b547f9 | -2.71806 | -46.71863 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 966601df-4a04-32f0-a5e5-1994b5bbc2c8 | -2.64576 | -47.36492 | 2024-10-10 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcd74fa3-d91e-34d3-8e4d-208a553f0e8b | -2.40926 | -46.75713 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de2c67a5-3268-3942-911b-44b1880180e7 | -2.4092 | -46.75401 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21d4ca41-0089-3b3f-bd2d-7b76bba17c8e | -2.39332 | -46.7126 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3d95d2f-c1b5-331a-ac0d-6dffb899c7c6 | -2.39034 | -46.70781 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47508ba4-724f-3c60-886c-2280a199026c | -2.36723 | -46.49284 | 2024-10-10 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0fc44fb-74ae-3b88-86f6-c76815686510 | -2.36355 | -46.49223 | 2024-10-10 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fc8cb43-3bda-379e-aeb5-ee9811f23124 | -2.34751 | -46.83942 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22178715-15a5-32e2-92c4-734864c52463 | -2.34324 | -46.84307 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14caed6d-7fee-3674-9e4d-2159f70a899e | -2.3359 | -46.45934 | 2024-10-10 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de7a0006-c132-3d08-9dbc-f8481f61ff7b | -2.3322 | -46.45878 | 2024-10-10 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d095d7c-661b-3d49-b0cd-701b03178f6a | -2.30985 | -46.5532 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c557f1b-c16e-35a9-95e8-f1a339618ac2 | -2.2933 | -46.97531 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2708339-6e21-3bba-b4e2-b39bc12d651a | -2.28971 | -46.97476 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9ebce47a-7f7f-3382-a718-a6ab032478cb | -2.24211 | -46.74809 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f0d3b6-5433-356e-b018-f4de0cd73765 | -2.24146 | -46.75229 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b0b591-c846-34bb-918f-11385f54a9c0 | -2.24043 | -46.73489 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06263133-6875-3253-841e-b6298b191675 | -2.23913 | -46.74333 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4485c91-9677-30ae-920f-d2d330620eba | -2.23745 | -46.7301 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7857b9a7-c003-3509-8a4e-626ab8478a77 | -2.23679 | -46.73434 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7b2a36d-cfcc-3b9c-9753-e08d8527a060 | -2.23614 | -46.73856 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46420362-0867-3f65-b288-5bf44dafead6 | -2.2015 | -46.74614 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15568f2e-6c07-3193-a7dc-c11fa8d657b2 | -2.19851 | -46.74138 | 2024-10-10 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5716246-e011-3036-94b0-8a82535ea70b | -4.47964 | -46.59882 | 2024-10-10 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e604057-ab1d-3ab0-ab68-1eda5a7eb687 | -4.47589 | -46.59818 | 2024-10-10 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d69594e-3c0f-3036-b651-d8b6d8524b08 | -4.47213 | -46.59754 | 2024-10-10 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1f4fe8f-e4bf-33b0-bbf2-3b14f3a6dbe4 | -3.82282 | -47.4958 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb431f73-4545-3be5-b2af-ef14b0d16984 | -3.80917 | -47.4896 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3bfee60a-78e8-3538-815b-59e3788a4d99 | -3.70054 | -47.61011 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6655696a-3886-39f7-a000-781a7b13c194 | -4.35058 | -47.28967 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0049a07e-3d54-37c6-aeed-a65d9752f143 | -4.33764 | -47.25311 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e5a842c-ca51-3967-b3b9-661979ea6307 | -4.33224 | -47.31269 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bf0b9e4-5555-34fa-a9c0-807230c0cb6a | -4.32863 | -47.31212 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f3cfa0c-2657-3568-92a5-49efcbd3cd21 | -4.31949 | -47.70351 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 756bbe17-93eb-350e-aeed-32d1f176dc81 | -4.31886 | -47.70753 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 730ae673-a9ef-346d-8b6c-11589cfec6cc | -4.26022 | -47.19545 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1c904ca-868b-3199-ab98-5a1d3ed5a2e2 | -4.25658 | -47.19491 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README86.md)
