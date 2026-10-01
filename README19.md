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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17711b34-4a25-356e-8304-4df9e5ab55d9 | -5.18347 | -46.1979 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1224da40-ddff-3a28-8a8d-5eae9fce5f8a | -7.1126 | -43.15144 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9cc68759-a6dd-3ca0-88a7-27fc60a1452b | -7.02421 | -45.27554 | 2026-10-01 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38187c55-11d6-38af-a00d-008c3c3eb94e | -7.32486 | -42.07915 | 2026-10-01 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cac83421-5a25-3bc9-a3c6-8fbeab72ab6d | -5.74769 | -45.16938 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 88232999-8bb3-35f5-a38e-63f25bfd429d | -7.0718 | -42.32198 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c3949496-8cb3-35c7-b1e8-aafcff5eaad7 | -6.18752 | -44.85875 | 2026-10-01 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85958182-ed13-3267-9258-5910ee69208b | -6.8658 | -44.9285 | 2026-10-01 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be51a3d2-a69c-3ae2-9986-5c91278bc645 | -7.1132 | -43.14815 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c304c6da-cd1d-3f51-a586-cd006c66df01 | -7.07787 | -42.31701 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 15b5e670-2022-34f1-9d17-67dc46625424 | -5.18173 | -46.19247 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d9c5627-d48f-3e12-9869-a9b5d3197d69 | -5.72674 | -43.52236 | 2026-10-01 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 014ccc6d-a5b9-3f3c-918f-4a79b7cab66a | -4.12793 | -46.87117 | 2026-10-01 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95930b17-d8c5-378d-8344-6c1ee671c8c4 | -5.76089 | -45.16691 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30da9db2-7241-3ae3-8e4c-4d08da08e0c0 | -6.92608 | -44.56113 | 2026-10-01 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6483cfa-eca8-3fe0-ac73-3463ddeb592e | -4.86451 | -45.84154 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 16f9ed96-e0e6-3326-a6a9-1b9fe16e6ff1 | -7.02946 | -45.28132 | 2026-10-01 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 693df801-114a-3309-a293-c9ff53a7d282 | -4.12619 | -46.87051 | 2026-10-01 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 38021597-fa88-34ae-b1b4-fcd1b326d185 | -7.0739 | -42.31017 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2413db7a-d23d-343b-8833-639882edefae | -1.89941 | -45.82662 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94b7bef7-a859-3d33-bed6-05628aea8e4f | -7.83281 | -40.19285 | 2026-10-01 03:36:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed3b728f-98d0-3c64-811f-c4495c640f9d | -5.74332 | -45.15815 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b147993d-1679-3606-9d06-12f220743d5a | -5.76264 | -45.15705 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 19affc84-e47e-3d35-b4d7-e5bc6d2b5209 | -5.76702 | -45.16833 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c033fe9-5004-336d-aeae-eb84d0243f4d | -5.56857 | -45.07641 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6897bd55-9028-344e-aaa6-4fe814766544 | -7.11731 | -43.15567 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6202c515-38a1-3086-b5e0-8d1e6f3d3f96 | -5.76002 | -45.17183 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d83883e-d058-3e4c-9d17-5f48073162d5 | -5.75034 | -45.15455 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0db7c6c0-c8f9-3c1a-a719-202ed69f1363 | -5.27145 | -46.14969 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12a869f4-0ed3-3c56-b1a6-b593af488bdf | -5.75563 | -45.16064 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1a0d101-e5ec-33bb-bc5f-775dd9840682 | -4.12492 | -46.87763 | 2026-10-01 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0a098cd1-43a8-3a89-8059-672c28610125 | -3.54993 | -41.56914 | 2026-10-01 03:36:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c411ad1a-f3f0-315d-84de-5809ee81e998 | -7.11851 | -43.14909 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| da6a7977-9400-3e5d-a92c-f6296c515be1 | -7.02337 | -45.28014 | 2026-10-01 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 362fd636-9149-35f0-92c3-408b1c69f1b4 | -5.088 | -45.78896 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad807429-ff35-3706-bdd3-550d573c1761 | -5.7635 | -45.15219 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 71cf6365-3aa6-323c-98d7-173404681b7b | -1.9083 | -45.81522 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 958d2688-da45-3418-9600-7f1db44cd5d6 | -7.07733 | -42.32001 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6205bad5-b446-3db8-b01f-1ed0bb0efd6f | -6.18832 | -44.85418 | 2026-10-01 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed758817-3927-3b04-8e26-9dd2dcf810fe | -5.44351 | -43.74463 | 2026-10-01 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b718ee1-f120-3f1f-8a64-4d8b165ed3ad | -5.08892 | -45.78376 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f2a6c162-5fa3-34bc-9a14-7cf8d73f1357 | -5.74244 | -45.16305 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 28ce4aa6-161d-3d40-8a63-4b82b12d92a5 | -5.18062 | -46.19855 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69cb2c3d-3d06-3496-9f97-4c8b0cfda61d | -5.74418 | -45.15334 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 61a7f3c4-7507-3d89-a1c3-f08348cf625f | -1.90863 | -45.82236 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a84655c5-2d44-3ff0-a56c-b505e283e949 | -7.11398 | -43.15146 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a1d6b21a-4945-3f32-aacf-82d8dfcf7b51 | -6.47345 | -46.56448 | 2026-10-01 03:36:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bba6ac97-2e82-3c8e-9fe6-44aec2c6f751 | -3.54943 | -41.57211 | 2026-10-01 03:36:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6105aa77-b633-38a4-8f7f-08b818b4b63a | -3.93538 | -45.42243 | 2026-10-01 03:36:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45932e4a-a9e1-36e4-8558-f2852ff46110 | -4.1267 | -46.87828 | 2026-10-01 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85579dc6-7efc-302f-8318-1323576902d1 | -5.75475 | -45.16557 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ba1cee72-be88-3a9a-b9ce-06f56f727c42 | -7.11814 | -43.15903 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| bc6b6f18-1536-30e9-93d7-e90346aa4396 | -7.0784 | -42.31401 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b8a3552c-723b-3354-b5bd-a0eac5fa447f | -7.11455 | -43.14817 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 82757417-6900-3140-a246-8c84eafabc0a | -1.9097 | -45.81614 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8793d5f4-aef6-322b-a51d-50093c5ce741 | -7.11987 | -43.14912 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f211fc0f-7ecc-3d56-afc0-eaeb64e99985 | -5.75386 | -45.17057 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d8842f3-9796-31a8-941f-96dd572511d5 | -5.7565 | -45.15577 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b04f7499-6790-37d2-a4d5-581c2887193f | -1.90147 | -45.81418 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d552fd26-4e35-3454-a220-ddf8ee98dfb4 | -7.11791 | -43.15237 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 86b125f1-cf08-3ff3-8c6e-300103772ae6 | -3.97569 | -41.51557 | 2026-10-01 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 08b4b4a4-48c0-320b-8c32-093aa78a7f55 | -5.76176 | -45.16201 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aa7fdd09-c306-3806-b9e7-0c13b38b1fa6 | -5.74948 | -45.15938 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 72c69c54-9a5d-36c4-a8b1-d80fbb61f0cc | -1.90931 | -45.80908 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b487b31b-67cc-3a4a-a3f3-31f424dbbc1a | -6.70641 | -45.98567 | 2026-10-01 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24d18af1-18bb-3da9-9fdd-a48afeed5740 | -6.18972 | -44.85702 | 2026-10-01 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b0d1803f-3b3f-36e6-b0a4-639806408e2f | -5.7486 | -45.16431 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2774ee16-b6df-3587-a734-c7a75ca672f6 | -5.42693 | -43.45398 | 2026-10-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d50db96d-c0d4-30bb-88f8-b38138a06d45 | -3.97519 | -41.51849 | 2026-10-01 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5f4e0030-8673-3254-ba17-5f68eceaa1ba | -7.11872 | -43.15571 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a764ac7e-0841-3e03-a222-5eee1a7c4d7e | -6.91951 | -44.56413 | 2026-10-01 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3861e4ba-1aec-3c55-acf8-1d72cb389a1d | -5.75735 | -45.15096 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| eec2fba8-8add-3d2b-a3b7-e2aec2a7861e | -5.44421 | -43.74064 | 2026-10-01 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84e11bad-1e02-3fe3-b7f5-841de111f348 | -7.11341 | -43.15476 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| aecde19e-d339-3449-8c1b-8357d3823995 | -4.85702 | -45.84578 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2666bf2f-891f-33b3-9627-f36f31a5aadc | -6.70786 | -45.98518 | 2026-10-01 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa5b48bd-2dde-3549-b8e7-b997a5848a64 | -5.42759 | -43.45016 | 2026-10-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eab13be3-97d8-3b6b-86ed-d57b305c7ca4 | -5.74206 | -45.05872 | 2026-10-01 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ed141c8-e2cd-3593-9ed5-32804d7cda34 | -7.07543 | -42.30155 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1310b2bb-e0d4-3bac-81ac-0eb03dfd3914 | -5.36484 | -46.22611 | 2026-10-01 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 23c2cf4a-06ae-37f0-b667-c18da725b676 | -6.86498 | -44.93303 | 2026-10-01 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7e1154c-8c51-3710-bb07-ac19fb8ff5e3 | -7.112 | -43.15472 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 89a04bb7-0c33-387a-983a-6555b65d25b8 | -5.17826 | -37.06769 | 2026-10-01 03:36:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd6f2e8a-ef5d-3920-bcdf-24177c8426fd | -4.85805 | -45.84002 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ce879cd-4dba-3fb7-909b-390fa2c539d9 | -5.27583 | -46.15176 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6dbdde8c-68f2-3197-b128-017de61a9e52 | -7.1193 | -43.15241 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 296206df-ed02-3f4f-8c4f-8b00ac78b4c4 | -7.07095 | -42.29759 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 82d4043a-e467-33f2-b789-4f3d4b35b513 | -7.07338 | -42.31306 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fadce57b-8cf2-3f05-8330-96218111f085 | -6.86655 | -44.92436 | 2026-10-01 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c1c91e3-dbcc-324e-9e70-06f4bb4bb54e | -1.90249 | -45.80804 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fc3f5c28-f593-39d4-83a8-7be90b170bd5 | -7.07233 | -42.319 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6e23f168-92c6-39c0-af9a-e855eaeb78b8 | -3.93633 | -45.41705 | 2026-10-01 03:36:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c5bd0d-b0bb-3074-9847-bbb0565aa05b | -7.11671 | -43.15898 | 2026-10-01 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 69c8bfa8-913b-37db-a68d-f3fdde22b946 | -1.90727 | -45.82142 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 569ea093-0858-34fb-be52-f386bac33ad5 | -5.43781 | -43.74374 | 2026-10-01 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61d23fc8-36c1-383e-8912-6b2bbe2110a5 | -7.32143 | -42.08001 | 2026-10-01 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 79fbf5a3-3df9-37d9-a7a1-d23dda57b616 | -5.17687 | -46.1965 | 2026-10-01 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4d74c233-3907-33af-b004-2b221c59fdb8 | -7.0303 | -45.2767 | 2026-10-01 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92a9faac-71ab-3dd8-acc9-9640e8f288d4 | -5.10386 | -45.66282 | 2026-10-01 03:36:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bfe73b27-6e94-3208-b435-d4631af9284b | -7.07335 | -42.85641 | 2026-10-01 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README20.md)
