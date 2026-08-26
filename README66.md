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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52c47f35-036a-3974-91dc-b6b9d92c86c7 | -14.51409 | -59.80663 | 2026-08-26 05:31:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084ce1e1-ff60-334e-882c-0e05b6f6bd70 | -15.60451 | -53.11926 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fac364ed-4eac-364a-a46b-e81973e5fdcc | -14.50681 | -59.80916 | 2026-08-26 05:31:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dd54dbb-7e15-35e9-afad-f883d10ac691 | -19.07212 | -57.39521 | 2026-08-26 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 19b7a814-5e71-32ea-9307-4d3a4314ea9f | -15.59959 | -53.11858 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8bf5f9e0-2350-3217-b3c1-f4b3190e016a | -15.59892 | -53.1242 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a00f1dd-ef8d-3260-849c-5916d224a638 | -16.19632 | -57.75234 | 2026-08-26 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 299fbe32-01d5-3428-9549-a7bf4cb19a1e | -15.67894 | -53.89404 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 916ce194-b6a0-3d0d-b76a-abd914791bba | -15.60384 | -53.12479 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 157f40b0-a1bf-35c3-a8cf-60b0ee622c97 | -16.19938 | -57.75739 | 2026-08-26 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b2727632-3971-35a6-aede-e5300c17b401 | -19.06822 | -57.39464 | 2026-08-26 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f91ad509-34da-316e-9614-436481d32688 | -15.56993 | -53.14695 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bb07f84-3030-3760-ab22-59122a6c8455 | -15.68359 | -53.89481 | 2026-08-26 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a054c675-2e5a-3b8f-8bb9-0cf170c070e4 | -12.6836 | -48.4116 | 2026-08-26 05:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 0944fd33-8baa-310d-875b-aa36536de980 | -13.3031 | -51.4731 | 2026-08-26 05:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 397f7529-c333-310a-ab52-669e003b208d | -13.3034 | -51.4517 | 2026-08-26 05:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 224.3 |
| 74aaaa10-e765-3753-828a-d029470ab094 | -7.5288 | -61.4015 | 2026-08-26 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 009bcca0-50d2-3c5d-ab16-1530e53766bd | -12.055 | -46.0118 | 2026-08-26 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 0916cc7c-f2f0-31cd-bdf8-2779ace4a323 | -10.7784 | -54.0368 | 2026-08-26 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7e9398a2-bf47-375a-914b-736a69684a62 | -12.0166 | -46.0173 | 2026-08-26 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 50b7e21a-9799-351e-b29e-c99b9cbc2a2f | -13.2842 | -51.4541 | 2026-08-26 05:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 0dbb2bc3-273b-3e20-9823-6a920af32ef9 | -6.6409 | -58.5181 | 2026-08-26 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 370dac02-6432-391e-bf50-38193b14dfaf | -12.0546 | -46.0346 | 2026-08-26 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 65bf1a8e-5567-3d8f-ade7-80c664edc4e0 | -9.6024 | -55.1078 | 2026-08-26 05:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 0d9fbbd5-3b88-3d4d-bed1-ac37a6cd7074 | -10.7596 | -54.0384 | 2026-08-26 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 433e38ff-d2fb-3406-9f7d-00b02ded9655 | -12.0358 | -46.0146 | 2026-08-26 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 255.5 |
| 25cb8a0f-0d35-318e-be9d-5300a12cf101 | -6.2676 | -53.3768 | 2026-08-26 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 302e6e11-0ba6-3f98-a435-bb598781f7e0 | -12.0354 | -46.0374 | 2026-08-26 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 7bf38437-e682-31d8-a307-9a45737bb04d | -7.5104 | -61.3832 | 2026-08-26 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| edef4e17-9832-334b-95bd-aa14d7dc1a53 | -7.5289 | -61.3825 | 2026-08-26 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 57ce8d9f-799d-3890-ab7a-f7cbaa3063ab | -6.641 | -58.4987 | 2026-08-26 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| dbe2bdab-3036-3edc-9bba-cbfa1170b809 | -12.0162 | -46.0402 | 2026-08-26 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| cf589172-6ce7-3293-8b48-d10ede8718f2 | -3.1092 | -61.23338 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19a6d887-28bf-39c7-888c-a1120f90ed85 | -3.13512 | -61.18848 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3eca565-c3ac-33c0-914c-8aec2a16e169 | -3.13211 | -61.18356 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94987587-8531-3118-be15-97caca6b5e1f | -3.12336 | -61.19111 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85f75b1b-dd79-3d0a-9999-b5b8e116ad9b | -3.13006 | -61.1966 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 727d1531-0514-3375-9f31-9ea4d9616ef3 | -3.13443 | -61.19282 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4aeb3b87-a059-3a73-96a1-e72d2e2d9de6 | -3.19899 | -61.28006 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5ff2dbc-2038-3a2a-b27d-0912aafb0d07 | -3.11055 | -61.22472 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 664200b5-3db7-37f4-b742-c2412a5dabdc | -3.20448 | -61.14732 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb09294f-5bac-3b97-a60a-3a9260459dba | -3.13796 | -61.18637 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cff0fe7-4887-3ab5-ae69-20b15faf3ce8 | 2.23284 | -60.70448 | 2026-08-26 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 96d815e0-edb5-31b5-9ee8-6f9045284a09 | -3.2161 | -61.24282 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa04e17-e8db-32bf-98c5-022445c4bd95 | -3.21678 | -61.23849 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b817a44-3106-3cf5-9b24-2836660e422a | -3.06862 | -61.07971 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6f50200-e96c-3a0a-9ce0-250430c8f4dc | -3.54202 | -58.6509 | 2026-08-26 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aecd5836-0085-3723-a004-77819aae0803 | -3.07072 | -61.21416 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 277c485f-444d-3ec0-8084-f1a1695bdd41 | -3.21746 | -61.23415 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba733a1f-5514-3402-9aa0-ebb03e5c6040 | -3.54639 | -58.65156 | 2026-08-26 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 684591c7-312c-37ce-beea-f707277e2525 | -3.09551 | -61.20022 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2465449-9d2a-3721-a190-ef00a0067268 | -3.10687 | -61.22415 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 551dd606-d7f6-30b4-bd03-43338eb74441 | -3.49394 | -59.2896 | 2026-08-26 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bc4a81c-a209-3827-a590-7ea9b9a4fc49 | -3.07301 | -61.07584 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fe05195-032f-3516-b6a8-b0674babd453 | -3.10619 | -61.22849 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f59164c-08d3-31eb-8d9f-f0022ea223b2 | -3.0995 | -61.22304 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 468dd4da-5250-3327-8670-d53fa40487cd | -3.10987 | -61.22906 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84337431-fc0e-365b-8c8c-9ee9de352a27 | -3.10251 | -61.22793 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5ce8e91-e22c-3d73-bbe9-d299db437915 | 2.23349 | -60.7085 | 2026-08-26 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0bf6e6ee-15bf-3edb-bd29-dd54a7f5736c | -3.21377 | -61.23358 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe60866e-9a80-358f-94ab-802ca04168d4 | -3.1358 | -61.18412 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad1ae911-333b-36b3-b6ad-7122cd48b66e | -3.09483 | -61.20456 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f8064168-6714-30a4-888a-ed9ba1ab0c8b | -3.49335 | -59.29343 | 2026-08-26 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03e443e3-b875-3306-93f9-541e4f55d7a8 | -3.09618 | -61.19587 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33f05182-ee7a-34da-be1e-b87ab6ec772d | -3.1373 | -61.19072 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6feefbda-9756-3bb6-9847-0c9041f2681b | -3.0693 | -61.07529 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d53ebc27-f5bc-3bda-b86e-bdc0e2938de2 | -3.09249 | -61.19531 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b85f6412-21e4-3d95-b31b-db5701610222 | -3.09883 | -61.22737 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d9767d-aeca-3a37-a35f-889c1b8f9b1f | -3.12705 | -61.19168 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 207c6fe3-5fd6-311f-af89-f42e6af1681b | 1.5243 | -55.94913 | 2026-08-26 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a016259-2635-3522-aa8a-c7767b2c48ea | -3.13143 | -61.18791 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 145f0497-0501-3ac3-a95a-1ca261c16c8f | -3.13074 | -61.19225 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5346f9ef-6d6f-366c-8b20-c4a96b71fec9 | -3.07234 | -61.08026 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c50b7ae0-c086-3a6c-8a42-ea06e69b0e77 | -3.10319 | -61.22359 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9a3bd05-a373-3b18-8879-55e41d578e84 | -3.22347 | -61.24394 | 2026-08-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6681426-cce9-31cd-aa76-b7f76d287d5c | 2.5903 | -60.6954 | 2026-08-26 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c172a9-6080-3615-8128-7ec32f8d0414 | -6.96423 | -62.86578 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c23113b-e5d3-304c-a627-8e994212ef4d | -6.69413 | -58.71824 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3be3e16-f053-3322-bfd6-8d0d6a14bf37 | -8.63495 | -66.53762 | 2026-08-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44b9972a-4bf1-3853-aa40-785e87ff0b5a | -6.99904 | -59.31159 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bdf3d384-2c69-37c9-84df-ae705a8d5fbf | -6.12479 | -57.8153 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc6c5fc7-8d06-3421-82dd-a056297f61ad | -6.62274 | -58.49781 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8f01b421-1f62-3978-b1a6-ddb546a91faa | -6.78286 | -59.74528 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f6851a6-6b34-3e26-b9b4-093b9e96a71c | -6.81147 | -58.61688 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1df4232f-fc7d-3781-8dbd-2dfbceaac217 | -6.99599 | -59.2716 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae0e505-11a2-3824-9f6b-25b55d8956dd | -8.21637 | -55.01206 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb249c92-8cff-3322-a9a3-db119fbbe1e4 | -7.4339 | -59.78005 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3391d34-4cb0-322a-a653-3a5cd6502abf | -6.72691 | -59.45122 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cb6820d-b852-3d73-af9b-d611ec2beb9f | -6.78732 | -59.65546 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 186e97a9-f813-3c9b-9265-b377dc4ffb4b | -7.54077 | -61.35577 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 406b7c8b-1d65-3419-8ac1-737a353e78e4 | -6.15012 | -57.71061 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a041cf45-531d-3c39-9905-9d704a319914 | -8.8216 | -62.33645 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9b8bc98-d089-3c6b-a27a-4c5e555bc589 | -6.81952 | -59.58554 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd4b857e-71ab-3e66-9cf8-a6ba06670f95 | -6.82515 | -58.65234 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26aaee34-20f5-3118-af7a-fe85e77e7caa | -6.22318 | -55.61891 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df2f1d0c-3599-391d-b708-dd45ddbfb672 | -6.1288 | -57.8181 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b07e09c7-e971-34b2-8b07-3b33dcedfe6a | -6.71057 | -59.13089 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7c960d8-490c-3f2d-9ece-894b4cd6f3ac | -6.26265 | -53.38569 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03a6c02c-5cb1-3627-8091-2fca7389ba73 | -7.5178 | -61.37706 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 614aa963-d54c-3bda-90f5-6408b3eb17fd | -6.70238 | -56.34334 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README67.md)
