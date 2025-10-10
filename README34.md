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
| 4b00ce62-6d8c-338f-b899-507147a025e5 | -5.48841 | -43.07607 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a68aa366-0dd0-3fc7-a18a-4314c5b8b783 | -5.90844 | -42.85299 | 2025-10-10 04:49:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 58625122-c917-33ba-b8fb-fef1ac9b86f6 | -5.25208 | -42.99593 | 2025-10-10 04:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8691e1bc-1373-3f56-9042-39c0be9bd9f5 | -4.83891 | -42.92509 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08a3968f-86c0-3bc4-8b3e-9801eca41d4d | -5.25159 | -42.99945 | 2025-10-10 04:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ea25a9-2186-3f41-8c34-4cea062acf4f | -4.55891 | -46.68675 | 2025-10-10 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b4827a8e-0722-3703-8b86-e2a8d925cac8 | -5.48349 | -43.07176 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ccdbd32a-d0de-3e14-9591-e007a3e8f188 | -4.65093 | -43.19838 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2d3a202-e7e3-3e8c-86b3-53e797ac76f8 | -5.58746 | -42.81063 | 2025-10-10 04:49:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66e33fd0-db07-30a7-87be-6c7e3ee1ea58 | -5.44844 | -43.51337 | 2025-10-10 04:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d8e0abb-8b16-3a66-95e7-0481d83a4d9c | -5.62008 | -41.16864 | 2025-10-10 04:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f34ee875-0836-3da1-b274-31587e53c7e4 | 1.13241 | -51.40865 | 2025-10-10 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2a2579a-d6f2-3ecf-9ba4-03ce0e255930 | -3.39403 | -50.14821 | 2025-10-10 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4363a1c-b050-38da-8974-e2e1fc99afc4 | -5.40632 | -40.98921 | 2025-10-10 04:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8dd688dd-12b8-3e12-9228-426409496aab | -4.55057 | -46.68568 | 2025-10-10 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e84dde4a-1151-31d1-a339-7eea10065f9f | -5.20467 | -44.35841 | 2025-10-10 04:49:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d25a55b-0d1a-33ec-9e37-f760e551d645 | -5.24965 | -42.9971 | 2025-10-10 04:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24b12849-8c1d-3e70-8f3b-1797fca79914 | -2.99926 | -48.73445 | 2025-10-10 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e71f5435-7d82-37aa-96d1-30c095936093 | -5.58698 | -42.8142 | 2025-10-10 04:49:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 969905dd-8fe0-34bb-81cb-f50c89c9f696 | -2.92608 | -48.30238 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| df8967c3-e388-3ed7-8c43-b52bcd9de345 | -2.18908 | -54.4822 | 2025-10-10 04:49:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d108eae5-1088-3324-8455-32e66669f682 | -5.58712 | -42.81199 | 2025-10-10 04:49:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d28af8a-8443-3377-878c-c9a20be9d650 | -5.70111 | -44.21713 | 2025-10-10 04:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7053c5a-c622-3650-98f9-c06edb8f4d84 | -4.94815 | -42.82062 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4c262ad3-948b-3bdb-be85-92ee837c8269 | -4.94901 | -42.82311 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c678dea-5eff-39ad-94c1-74be1f1002cd | -2.688 | -48.38761 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 165508eb-6f02-3c4f-a1a5-d763295dac3d | 0.71141 | -51.37278 | 2025-10-10 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7349c80-eb25-3afc-a5af-1fd32573362c | -5.30786 | -45.40094 | 2025-10-10 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8b1a91d-fb9f-31bc-b691-5e1ddb2c5a60 | -5.40699 | -40.99081 | 2025-10-10 04:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fdd49220-9bed-3500-8049-77586fd7761b | -1.77063 | -52.15314 | 2025-10-10 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39dd62bb-eabc-3279-be8f-72b354f0cc1b | -5.45323 | -43.51734 | 2025-10-10 04:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab962916-c070-3e0a-ba40-b34f7e5fa01b | -1.40796 | -46.70744 | 2025-10-10 04:49:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cba458b-a90e-332e-9eee-fdb1759bfd67 | -3.37986 | -50.28391 | 2025-10-10 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcbcf0b3-5928-36c1-8a12-92ca3f7a5b39 | -3.82884 | -51.31208 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 305b3897-df02-3bfa-ad2b-6b52e4f5f589 | -5.47924 | -45.54493 | 2025-10-10 04:49:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeb1e6ce-96f4-35a6-9295-9852c21d462a | -3.4521 | -52.22142 | 2025-10-10 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3b728d5-7d07-338d-98d7-ca76c6ac0771 | -4.65046 | -43.20159 | 2025-10-10 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78734de3-f53a-3516-8475-4bde8c2764cf | -3.00683 | -49.61077 | 2025-10-10 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb5e1c9f-a119-3ef9-823a-7730368974b8 | 2.1676 | -50.71674 | 2025-10-10 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dbd0bb7-9538-3b02-be26-557837aee8fb | -2.92474 | -48.311 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| be7d70a6-ec9f-34e8-92da-40e412dfb93a | 0.71471 | -51.37227 | 2025-10-10 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ed4f18-e5e9-3619-aa93-681f7d7869f3 | -1.77117 | -52.1497 | 2025-10-10 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd315cab-fe00-3bfe-b684-d952c26befcb | -5.05218 | -45.84859 | 2025-10-10 04:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81b60519-ab8f-35e3-9d8c-1132c1d73436 | -4.55418 | -46.68992 | 2025-10-10 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cca8b5ed-9eed-38e6-8186-f4b95ef70f34 | -4.8634 | -42.78969 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c096cae0-d8ba-3054-a9bb-670a7acba133 | 1.93624 | -50.91082 | 2025-10-10 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 242ce9a9-e851-351b-98b5-346cc34525c0 | -3.75362 | -52.07528 | 2025-10-10 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea08124f-6b19-338a-9e4f-32736bb1c93f | -5.71122 | -44.21875 | 2025-10-10 04:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97e67358-52b9-3151-9254-c379ec83f9b4 | -3.75301 | -44.37871 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 285fa130-b8d1-393d-a9e7-a594abbf1669 | -2.67678 | -48.41189 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91d46c3a-d7cc-399d-8b41-938da5457377 | -2.34571 | -51.97993 | 2025-10-10 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81d1613e-139f-368b-a784-e7d73b290372 | -2.6837 | -48.3913 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52e4f8f1-ecf8-34ee-aec2-a8f79778ce36 | -3.41243 | -52.60291 | 2025-10-10 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c12a405f-8570-39c8-a85f-7f760b5d773a | -2.92541 | -48.30669 | 2025-10-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 601b39ff-1d06-3180-a701-ef9e89c398d3 | -4.95411 | -42.81801 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7296d50d-1fb1-30a2-b4d7-4e0fd7c4fe99 | -3.17404 | -51.25589 | 2025-10-10 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9a096c4-cf82-3c6c-842a-e872bd33de9e | 2.16813 | -50.72016 | 2025-10-10 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b48b800-32dd-39d8-8a1f-3a8d92171162 | -4.95493 | -42.82053 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3cd9c95-ec73-34f3-a4a8-6fb62a763beb | -1.54412 | -55.41158 | 2025-10-10 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4181c7dd-a50f-3101-a4da-4f5aacbd2b22 | -5.49478 | -43.06995 | 2025-10-10 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2cdf268e-4656-3952-95b6-5b7b6cc4ce11 | -4.94949 | -42.8196 | 2025-10-10 04:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 825cc33e-53e3-3afc-810b-4ae1ccd2bb8d | -3.00285 | -48.735 | 2025-10-10 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3efdc548-ad5d-3058-8c07-990c2a5e8a44 | -5.20548 | -44.35276 | 2025-10-10 04:49:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be9d2620-9b7b-340d-a411-271cb84a6447 | -3.38043 | -50.28028 | 2025-10-10 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b944d18-ee45-37d4-ad36-492d870822f4 | -6.82168 | -42.8029 | 2025-10-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d870cc7a-4365-30a2-a4d1-7649a16a92c8 | -12.63398 | -45.06735 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7994e07c-8442-38ea-b338-fd53d1680810 | -6.59526 | -44.80257 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51484e05-a558-3bc0-bf22-a2d9212b7b6f | -7.89625 | -45.49364 | 2025-10-10 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91289a2a-23b4-34fe-af5d-5dbd20143dec | -12.64039 | -45.05851 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f824ad65-e0f3-3cfd-bf87-b24b599e06bf | -8.50454 | -46.09468 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9619366-4add-3906-9122-6dd80534720e | -8.4987 | -46.13729 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 76daef03-b622-3e79-91b5-da5385eb9ce7 | -8.52748 | -46.13189 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bde8ddc7-d9a8-3b67-a087-742bef7abc4f | -11.0927 | -41.05381 | 2025-10-10 04:51:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2b0e915c-37c5-371c-9bd5-e4ad0b2d99fb | -12.22659 | -43.79174 | 2025-10-10 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d1b217f-018f-387a-bdbc-4d8e4bb75088 | -12.27595 | -47.85137 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5df1caa2-2fb3-3dbf-9034-1672375d7147 | -8.04149 | -43.91225 | 2025-10-10 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 377ed5dc-1dca-3b60-a0b0-acb226103245 | -8.20608 | -43.34669 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c1aa7bd0-8e57-31f1-8f36-d7b278b493bb | -5.98287 | -45.92013 | 2025-10-10 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de39cb90-6ff1-35f5-9232-ca4748fe63cd | -7.33551 | -47.81886 | 2025-10-10 04:51:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fbefcae-130c-32b8-be5f-d61b7a911e58 | -5.95772 | -45.67793 | 2025-10-10 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f5a65c8-0b56-3023-b295-5c582b184fc9 | -11.53279 | -47.09979 | 2025-10-10 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c18a8749-7375-3f71-98a0-59ee529d72b6 | -8.50328 | -46.13797 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 6ddb65c9-ed0f-32b9-ae9b-d92c0841ee73 | -7.0206 | -59.45938 | 2025-10-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91b57d51-b73b-3ec7-aaff-324859ffb7a4 | -8.5098 | -46.12452 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3a9dffef-4980-36ca-bc82-f5f4a5091195 | -8.89566 | -46.01136 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db8be4ce-f9ff-3680-9387-5832fd73e3bb | -7.77695 | -44.04987 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 742f86ba-a985-365f-86ca-5401514c2936 | -7.77779 | -44.04353 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48b410c0-995a-3d70-8918-c37f2e374f04 | -12.63321 | -45.07366 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cd2d8b79-5ee2-3077-bc21-4a0a320b164e | -8.53272 | -46.12783 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98ccd314-3116-3007-b0d5-f1f5c7efd468 | -7.79767 | -42.60368 | 2025-10-10 04:51:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c2c94b54-f6ba-366b-85a8-f485f1cb45da | -7.5511 | -44.59967 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ffc4778-b569-3950-a534-03ea7cba2865 | -7.6206 | -46.83352 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f447dcc-c3e2-38a8-a0db-ae6bcc54e489 | -8.5288 | -46.12242 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2198fb64-18d1-32dd-864b-623692bc0448 | -8.20965 | -43.36243 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 800e81a9-f4ef-30f0-9eca-12b31a15868e | -11.12295 | -59.15091 | 2025-10-10 04:51:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4efeb83-ace3-3785-960a-14dc695157eb | -7.11655 | -44.0886 | 2025-10-10 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 494eeb07-8189-34b9-a98e-7b78f6af221c | -12.63633 | -45.0483 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 79550583-f8fa-3545-83f4-081f6f233a1c | -8.20215 | -43.33289 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d8c19305-8a7c-31f2-ae90-d088933f9ee6 | -8.49995 | -46.094 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85747d34-bcc3-36bd-b161-4e86ac3b8e60 | -6.45482 | -44.57357 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README35.md)
