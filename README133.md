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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35935d97-91f8-3c48-ae16-d7bc0ab5b33b | -12.29053 | -64.1581 | 2026-10-05 17:34:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1dcc937f-2d5a-3c39-8bf3-c98a9717b400 | -8.36331 | -71.06345 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 83af16fb-a835-3cd6-aab4-44ecebd650f2 | -5.97021 | -55.35637 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 00b34228-b1e5-32c7-ba8d-17a8064eb1b0 | -3.26713 | -58.22311 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d43d4804-60ab-38fc-8047-3a732a099fcd | -8.06148 | -67.2523 | 2026-10-05 17:34:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1d5d3eb-c9e3-338c-8851-d5379a5160a6 | -3.54467 | -58.9368 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8e157bb-66cb-3afe-8977-d461f09b8b0b | -10.78905 | -68.30268 | 2026-10-05 17:34:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35d29866-eaac-306b-926a-7e7faa81fee8 | -3.0668 | -58.40232 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d6c2f738-6d85-3672-b8ea-75ba3d172e0f | -5.96963 | -55.35289 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c1cd343f-00bf-3c45-94ee-b99f74ec46c0 | -3.27714 | -54.18173 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 55845bc2-924c-3e5e-9a86-58b817340efb | -3.58925 | -55.40193 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 62c99d20-3762-3062-9977-8d14af8db415 | -2.48768 | -49.41172 | 2026-10-05 17:34:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d40e1440-0c7d-3a99-8d01-d6714b941046 | -3.21133 | -56.83173 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 2391d626-3a6f-3138-b11e-16b779aa378e | -6.17583 | -55.37262 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b0ae439-df13-3a60-b251-542814634f01 | -10.74663 | -45.30306 | 2026-10-05 17:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81b97a3a-fc0f-385e-a383-51aea082654e | -14.70674 | -58.66714 | 2026-10-05 17:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e9875b5e-ab56-33ba-980b-a83a4428254b | -2.95412 | -54.13695 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6aedc6bf-b3c5-36bf-885f-331319943685 | -11.34676 | -46.65927 | 2026-10-05 17:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9004fc42-72a0-3c42-95d4-ac07ab1d254a | -3.28381 | -54.17398 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 80d82bcf-bd91-3327-b911-bc0b8d6f24b1 | -4.12015 | -54.42255 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cf9b5bbe-10f5-3f58-afe4-bba15668487d | -12.14073 | -63.18148 | 2026-10-05 17:34:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 879c6757-317b-3299-9ab3-3ad7bfa0f3cf | -3.37818 | -58.23899 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dae4a4a3-8eac-3feb-a722-c96fb753b0be | -6.18645 | -55.35122 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 059e5d74-ad2a-391e-9678-f082cf569b8c | -3.64251 | -60.92038 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a3bed168-42a0-3952-ae32-1163c4263a01 | -3.06091 | -54.15976 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e4dbf604-bb02-391b-b3de-f88667ba8ec3 | -3.33016 | -59.47767 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88d969df-e290-33dc-ad14-42839cb67a7e | -3.42077 | -58.56279 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6a5d5329-d0ac-3bc4-8b13-064ba82b618e | -3.32678 | -59.47818 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 52f45257-b5a4-3237-bb95-4e8955ddc187 | -3.92901 | -52.21833 | 2026-10-05 17:34:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aa78305f-de14-3c88-996e-a11a2a4dc8e5 | -3.06764 | -54.17293 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 27f6fc26-1730-3193-9dae-95273d826189 | -6.04915 | -59.94451 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7d89b7c7-3902-35f3-9ab9-2f686e422288 | -7.52874 | -70.38915 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f3bbb024-bfba-38f7-be9d-c32e004da05c | -3.18475 | -58.94295 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72f001f2-95b3-3eb0-8bcd-eb0f140114a4 | -3.82731 | -55.61977 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e9281829-40f2-36ca-b904-e70745c8886a | -3.08874 | -58.39938 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cac8a20-ed69-3d08-b0c8-e22f142ccd08 | -10.95641 | -60.90144 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3b00be0-a6af-3cca-824f-589234e5bc90 | -2.95587 | -57.60918 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 02f1fbaa-71e8-3a2b-9d6b-e92e6b8a8a1e | -3.37916 | -58.19831 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 5bcd47c9-c3fa-3e61-a1c5-04cd80af6865 | -3.0764 | -54.16368 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 84bb1103-23ff-308a-ae23-0e5460d30212 | -3.45287 | -59.63732 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74e0d049-b723-3c3a-b536-8fed247b6139 | -2.78856 | -56.49623 | 2026-10-05 17:34:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 21275238-ca7a-30ea-85f2-975b65cf94d7 | -3.37465 | -58.23954 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bab3b7c0-8729-391c-bb6c-784522647278 | -3.39772 | -59.25626 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 87fab0d5-03fb-3008-a6b1-c97499c46641 | -3.62781 | -58.61256 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f746b31f-f302-3fbd-b7da-fda2f7c96305 | -6.33603 | -55.32615 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 670c46ef-bbca-3219-a222-594791c27f8c | -7.13122 | -71.5312 | 2026-10-05 17:34:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8dd94d50-e2e0-39ec-898b-65003b97fac0 | -6.96434 | -71.49019 | 2026-10-05 17:34:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8836eba0-d17c-3d15-baae-eca4ff9489aa | -2.96064 | -54.1465 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b27ac0df-d59b-36d6-8487-98566ca1abb0 | -3.53347 | -58.72813 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f68062a8-65ba-34ed-9315-ff571cfe70bc | -2.93896 | -54.12991 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f5bab8f6-67c8-32d9-8981-ca5c9ff332b9 | -3.08316 | -58.08721 | 2026-10-05 17:34:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1540c7b1-3d14-331d-b43b-9a968d48b906 | -3.30595 | -59.49968 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b03c3ef-306e-32cc-aa60-9a8cd28c6ff3 | -3.08204 | -58.40799 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6a3e6f0-776f-34dd-8902-7b26733638cf | -6.91557 | -59.26722 | 2026-10-05 17:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b364b3c6-13ad-38fa-8313-dee2e4079c7b | -3.19331 | -54.10372 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cd718ab7-dccc-35dd-8e69-b443c3e98164 | -3.68023 | -60.63263 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d2f871d-79b0-310c-be3b-d6d334984be5 | -5.95987 | -55.35215 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6b9ae869-fef1-3ab0-a646-2d01e64f20ef | -6.04756 | -59.93413 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f4f126e-7618-3cac-ad8d-189a2b7b658a | -3.46216 | -54.59063 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 82b378d6-988c-3b2a-8486-19459bf2a538 | -6.41594 | -67.95857 | 2026-10-05 17:34:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 94bc9f28-0eef-36ea-ba3a-b95ce5c30563 | -8.32817 | -72.11758 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e7085650-cff3-3f07-80b7-df7253ca5c8d | -3.40952 | -58.02192 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c0b7ec6d-9980-3f3a-9617-a9d199cd2b25 | -7.52866 | -70.3899 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 70c908f3-4b70-3ceb-b6f1-ae30c3ac0f26 | -8.27737 | -71.12226 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8e8532fc-91a0-3490-b658-a004436d6f2b | -3.13311 | -53.70652 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2ed4ec8a-1fce-3807-8283-cbcc754a7abd | -2.49014 | -49.40853 | 2026-10-05 17:34:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 31d48dac-23ab-3267-82ec-16ed806a789f | -8.07519 | -71.30447 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 56f84c53-c665-3a1a-8bd3-402d436cc80a | -3.06886 | -54.17453 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 30051956-96f8-3d28-a395-a4fee5b21aa5 | -3.4589 | -60.56165 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91b8158b-4496-3e14-93c9-14ed4b84cd50 | -3.2854 | -54.17551 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e25debdb-4472-32b7-9d73-6bb9066774ea | -5.82207 | -53.85986 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fd9e8ae5-b5de-3563-aefe-88bb87e4d4e5 | -4.78192 | -49.34863 | 2026-10-05 17:34:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6940d5e-2e1a-3fe8-8256-d20171207365 | -10.49476 | -47.23741 | 2026-10-05 17:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d9267e57-4ddd-3ec6-af1d-061cc383c1e6 | -3.69074 | -60.94829 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4d708e4-a33f-3595-94fc-830188b13cfb | -7.80361 | -66.78685 | 2026-10-05 17:34:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| cf83b7d3-3d1f-394f-94dc-c7b1f23c2733 | -3.60328 | -59.06748 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3ec91e42-511a-34b9-b4ff-0fd22f31f626 | -8.03123 | -71.10252 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e6cf6b25-cf01-379a-ac20-3838b583b16f | -3.99886 | -55.67593 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7279fc06-cbbe-36c8-832d-e6d6d5c11258 | -3.93896 | -52.0265 | 2026-10-05 17:34:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 929ce00d-75bd-33e6-b8bb-463422e53d05 | -3.01561 | -57.91407 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f06f0b73-19bd-3b5a-b084-02679d3a575e | -12.02386 | -62.53225 | 2026-10-05 17:34:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cda55bc8-923a-3b9d-bb89-7567af25bceb | -3.63221 | -59.3236 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ac11f2e3-42e6-35fd-8d3f-4407995ae10f | -3.84592 | -55.84282 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c7c30e7c-33e8-3b29-ac6c-21bb9ce9be25 | -3.58675 | -55.40074 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7f531868-491a-3494-8d5b-28e22551b249 | -3.07489 | -54.15451 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ec1291af-e7aa-3918-af0e-f30770ea8b54 | -3.52168 | -54.62491 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 077cefbb-c23b-3ef3-a62e-cd22a26a3258 | -3.64935 | -54.0477 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 74dbc2b5-3596-3526-8cca-ae17d1819e8f | -3.06569 | -58.4185 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cb3a1d7-e541-3b48-8e81-22e7c0b0f259 | -8.07367 | -70.49432 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 166d2699-137f-3361-aac3-96fe2c3de4fb | -3.24539 | -58.54612 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12278f9f-1b03-3905-97cd-7eaee9dc4c51 | -3.49195 | -59.6311 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3bd2e99b-0b62-3525-b801-28549a319512 | -3.67707 | -60.61197 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b8e95dc7-bdf1-3afa-97ce-f873289c1c21 | -3.11864 | -57.66852 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5241bd44-1a1b-372a-a74e-eb3a5de50e5a | -8.35773 | -70.07941 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 98bd9ba9-0e01-3b7c-be96-19175fc7f362 | -3.49693 | -58.32947 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c3393c4c-9f2a-353b-8b90-7c292bbda229 | -6.17867 | -55.71601 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 7766e857-fdea-3791-a56f-a2efe6d8551a | -3.01691 | -57.92229 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 217b950c-566b-3e6b-9fa8-cd75c222c87f | -4.36551 | -55.44321 | 2026-10-05 17:34:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5f7c1013-0789-36c3-8795-f7e8ec2e71a7 | -3.74959 | -59.29011 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| dbbd79f9-5cf2-36e4-9732-7fd776b7739c | -6.83459 | -58.59436 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README134.md)
