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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55887cd4-0c36-3595-a442-d3d4b404caa2 | -4.91421 | -46.731 | 2025-11-10 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc8b7562-c2dd-3bd6-b909-412392fa36f4 | -4.82917 | -55.9423 | 2025-11-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef89b14b-db60-3424-a141-f0dfbdda3ed6 | -2.90414 | -56.96097 | 2025-11-10 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1defa113-27f3-3763-babb-f5190ba97ec5 | -4.23764 | -55.65657 | 2025-11-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74a31e77-7439-3e3f-aafc-16bb96c9a5b6 | -4.41012 | -54.97959 | 2025-11-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39dbb9c4-8988-349d-acb4-efa6541247b4 | -3.94239 | -51.03664 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6b7e6ba-21f4-3938-8635-c7d74210ef2c | -3.83745 | -51.12706 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9e2e6cb-4d26-321f-a5a2-bc18918f94ed | -10.61561 | -52.18267 | 2025-11-10 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0e1ca512-f128-3a6b-a578-97c1b8ff8dd6 | -5.91379 | -48.32288 | 2025-11-10 05:10:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f495187-c8d5-3c38-99a0-3cf2970233e0 | -2.93192 | -57.7816 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e137c000-2a7c-37ab-9ab7-81f541313eb5 | -4.91585 | -46.73465 | 2025-11-10 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d70d42d-4091-3938-8d14-cb671e4c1c0b | -5.86046 | -61.22373 | 2025-11-10 05:10:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beb8dd9e-9fd6-3320-9fb3-6f5f015cae11 | -11.66222 | -48.46633 | 2025-11-10 05:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1807d091-60e1-3b78-96c1-bb66fdab46a0 | -4.12843 | -52.06473 | 2025-11-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6286011-18e3-3948-9d7f-99d19fa45641 | -4.45683 | -50.48936 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b187fa0e-2a83-311e-9a17-66e15c38a9bc | -5.12558 | -44.73264 | 2025-11-10 05:10:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49768621-b59b-3762-9019-b1ae9a11cd3e | -8.52195 | -55.02724 | 2025-11-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3042bb4a-c435-3dc8-b3b4-23e3c315fa3c | -3.7094 | -52.14952 | 2025-11-10 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9043909-f632-3ee4-a932-2cab3021098f | -5.12636 | -44.7269 | 2025-11-10 05:10:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 807d8a31-e1a9-3712-9b3a-b6e43b327816 | -4.28764 | -50.66193 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70e67a6c-95c7-3ba5-8c93-607f2d9cdc9b | -2.9431 | -57.77604 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 710f3e73-324e-313f-8edc-a1bfeb46c999 | -4.20575 | -50.6345 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 27555368-471a-368b-8a9b-af9d7f0d6a00 | -3.59691 | -55.46755 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3bb2958-83aa-32dc-b406-379dae9bdadf | -6.55681 | -58.48188 | 2025-11-10 05:10:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b73d105a-87f2-3030-849c-f699256e970b | -3.49173 | -55.42247 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06db84b3-02dd-3017-af45-c9f4cfc9e14a | -5.14783 | -50.87234 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d44b6421-d2fb-3962-97ee-2bdcd2f01044 | -7.9329 | -55.01604 | 2025-11-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5113460d-3508-3cc7-8516-cb080f9aff6b | -3.86062 | -51.41338 | 2025-11-10 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31b3b5e9-9f24-3167-b73e-a9d364bc522e | -4.1375 | -50.7701 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c554c1d-bae7-34d4-a5aa-2edd8ccdf2f6 | -4.29192 | -60.95861 | 2025-11-10 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 656e47df-26fe-3242-994d-3aab5448189a | -3.80453 | -51.09128 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c7da409-f80f-360b-80a5-ffb877c865ea | -4.12589 | -53.5005 | 2025-11-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3798f9d4-bf56-38dc-b59f-791b012c1fb9 | -4.2311 | -53.52349 | 2025-11-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55dafb47-363b-3eb3-a3b7-036cadb9ce95 | -4.91932 | -46.73597 | 2025-11-10 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9726acf9-c9c2-3832-bf92-5e622a99f35b | -3.86117 | -51.40971 | 2025-11-10 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14903781-4b07-3508-a911-217960890246 | -3.85654 | -51.41277 | 2025-11-10 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cae656d4-08ea-3eb5-a401-dacd77991618 | -4.91362 | -46.73513 | 2025-11-10 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f5fe643-79e3-3886-bd49-79070618f1d8 | -5.19255 | -46.15134 | 2025-11-10 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76e65d83-5e55-3839-bfd2-c8e2355c25e8 | -4.57898 | -46.66862 | 2025-11-10 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa88ff7a-dc0a-30bf-8e95-5a44517ef6c1 | -6.71658 | -50.98132 | 2025-11-10 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 257e07cb-7da8-316c-a63e-eceafe66fd45 | -3.94296 | -51.03283 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b2cbd31-09e2-3d52-a8f9-aa5086cfe8e5 | -4.2818 | -55.54478 | 2025-11-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3d61ad5-125a-3853-875c-2aa5d94995f1 | -3.59412 | -55.4635 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29d0bb84-961b-3380-ba2e-21712d4330d8 | -4.24098 | -55.65707 | 2025-11-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae233086-dc4e-3686-b38a-72746dd378ba | -3.59636 | -55.47108 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8eba4b67-37ba-3481-99cf-2e26efa0fe35 | -3.34961 | -54.09618 | 2025-11-10 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3e211bc-c8b1-3c90-9666-b92c4c2ac5dd | -4.2952 | -60.95668 | 2025-11-10 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b011f8be-e543-3e7a-8802-9a7f586223df | -4.64866 | -46.34494 | 2025-11-10 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87802a66-b5eb-3f5c-a332-e72bbd88066a | -3.59746 | -55.46402 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4795b36e-63ea-33af-9f86-4544cf96e520 | -3.98401 | -56.2156 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad7adb8c-c104-397b-8541-4b614ce4f334 | -5.9251 | -43.92818 | 2025-11-10 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97179a45-ee73-3a77-bf8c-4df56260baa1 | -3.85851 | -51.04466 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dc6eac4-9753-3013-8626-cd3aa6467783 | -3.50593 | -52.8992 | 2025-11-10 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76164645-6a17-3596-a6bf-498f5d841119 | -3.7764 | -52.26537 | 2025-11-10 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cec05393-24bf-3b2b-85fa-f19605e03725 | -4.45746 | -50.4851 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cc3e445-a35c-333c-81cc-2953aa6ee180 | -3.89597 | -52.19245 | 2025-11-10 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f1068f7-51c9-3f5d-a2ec-4b583600febc | -3.59357 | -55.46703 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cfd202a4-1d98-36c6-814c-4ded12a88f71 | -10.62359 | -52.18797 | 2025-11-10 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 520e35f2-e35d-3923-a47d-91d2f8be5ab9 | -2.94254 | -57.7796 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3c22671-cd1c-3667-8828-1657dbc0ac10 | -4.20697 | -50.62632 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 76e2de62-53d5-33ea-aea0-b26ec5d354d4 | -4.13235 | -52.06534 | 2025-11-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c191a1f6-5182-356b-9fe1-f0e6d56c0147 | -10.61618 | -52.17862 | 2025-11-10 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b48b845b-3cc8-382b-b817-5b575c61ec01 | -2.92856 | -57.78108 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc9c0a87-2a40-3dcc-bc6a-ac7ebd9f42f0 | -5.85666 | -61.22309 | 2025-11-10 05:10:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b1be504-8548-3550-a1f0-029e10f481c3 | -3.49118 | -55.42599 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5da75f7b-2655-311b-abd7-b2b3f9a48bf7 | -3.83778 | -52.10315 | 2025-11-10 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 662bd3a8-c376-3000-87da-703a15572294 | -10.619 | -52.18114 | 2025-11-10 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e922fd6b-7c22-3740-9856-48c9d5db77f4 | -2.92912 | -57.77752 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16f1ad58-9616-3b61-b04f-c29bfc9ba473 | -4.2371 | -55.66007 | 2025-11-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54e8008d-3f83-34e2-9fc1-0777048b51f4 | -4.43494 | -50.60673 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cc51ec6-f918-327e-baab-9dc3fada3c7b | -4.07258 | -50.44104 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cfe5479-281b-3571-b677-a67af6747e4b | -5.19193 | -46.15573 | 2025-11-10 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee4000a5-e008-3109-9df2-93580953b936 | -3.59467 | -55.45998 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e431fccf-a7ea-3f1a-b047-a89b900dad49 | -3.80815 | -51.09555 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 180a6fa7-1cfe-3280-aefd-3e9ecb35b3d5 | -9.1294 | -50.08384 | 2025-11-10 05:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a4bf1aa0-6960-3568-bccf-c522e9efe506 | -2.93639 | -57.77501 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f166565a-9f2b-3bbe-aabd-d11468dc1683 | -7.88785 | -48.38816 | 2025-11-10 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a47fc6c-8c3c-3615-b0bf-1b6a87235628 | -3.21998 | -61.22526 | 2025-11-10 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffe68e06-b2c3-31b7-a4f5-139aa8273e7f | -3.23341 | -58.89646 | 2025-11-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12135342-fa1f-33a0-a05d-1a3eac5a7a88 | -4.06821 | -50.44037 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e34f5ae-1423-3853-832d-88c57430c4eb | -5.12629 | -44.72701 | 2025-11-10 05:10:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 393b64f1-ef68-3cb6-8a92-cdc6749921c9 | -4.20204 | -50.62976 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 33164ba6-bc70-3c1d-a501-22fd8282420d | -3.96018 | -51.00396 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c5720d7-3a42-3814-81cc-477e6864f6d5 | -3.73051 | -53.78621 | 2025-11-10 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad06f188-e597-3497-90a8-a6a198be98d7 | -3.8738 | -50.97249 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49115f7-9a1a-37b9-bca4-2547445810bc | -5.92426 | -43.9347 | 2025-11-10 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 444c8615-20d9-3b76-ab5f-de52731f1416 | -4.20635 | -50.6305 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e2f95685-0881-3343-9668-2428ec0ac123 | -3.68184 | -58.50718 | 2025-11-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8465e2fc-a5ee-3cca-a0c2-62fd2f9afab3 | -5.04924 | -49.56256 | 2025-11-10 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60701ccb-f80f-3274-8625-03ccd28631c5 | -3.70282 | -54.67317 | 2025-11-10 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da680a2-972a-3bcb-a686-0a0d60eb4481 | -5.15214 | -50.87304 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d19e68c5-67d6-33b4-8916-b6555faa6df3 | -3.49452 | -55.4265 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03972a46-ba68-3345-b2eb-6130449515b0 | -3.92228 | -59.12036 | 2025-11-10 05:10:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15107a28-5314-3ebd-b37b-62b7be54a814 | -2.93975 | -57.77552 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dbb5af92-819c-3b76-8527-482d35d1085d | -4.28704 | -50.66603 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00928539-630c-336e-81a4-20327cc608ad | -4.64922 | -46.34088 | 2025-11-10 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c78e0b3-7f77-3f00-bbde-7caa6d3c1c9b | -10.62702 | -52.18642 | 2025-11-10 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ef409a9-d3da-3822-979f-f7da026fc9b6 | -3.68126 | -58.51086 | 2025-11-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad9a950b-4f4d-3c2d-bc12-a938e0839b8a | -4.91641 | -56.92972 | 2025-11-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc596422-3ff0-30b6-902e-f8b6d073340d | -3.84711 | -50.74659 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
