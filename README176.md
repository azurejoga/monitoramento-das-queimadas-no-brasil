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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6446697-1922-3a5b-b30d-49c14c0ca5e9 | -11.0441 | -57.2421 | 2026-08-28 20:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 302.5 |
| 4439b272-02b8-3005-90b3-960aa3a6afb4 | -14.603 | -50.8928 | 2026-08-28 20:00:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 7ca077f3-2e68-389a-a5e7-5bb8aa5b9225 | -17.988 | -50.1725 | 2026-08-28 20:00:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 264b6481-d6d2-3b15-98e9-c3bfb31644e9 | -14.919 | -56.3441 | 2026-08-28 20:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8cf7fa03-fa1f-3158-a1ae-be21b489bea3 | -2.7304 | -47.0424 | 2026-08-28 20:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 77fccdad-43ec-3f7b-aa02-65f68d3334ab | -5.982 | -57.6697 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ce2b5e9c-52d6-35ff-9cd5-456fe3c77752 | -13.471 | -57.0373 | 2026-08-28 20:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ff246802-0a0e-3a28-b671-bc805fee3f7d | -8.0113 | -48.0161 | 2026-08-28 20:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| a2df5227-08f2-3dfb-9047-ec63f9927d95 | -8.5969 | -54.7755 | 2026-08-28 20:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 23acb164-7499-3b99-96f3-d14971c62b63 | 0.1549 | -60.393 | 2026-08-28 20:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 7bc5019d-925c-3799-94b0-c9f59d7f59d7 | -9.8031 | -46.3505 | 2026-08-28 20:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| d37b8b24-4717-3694-a348-482f42dc33a2 | -9.2357 | -68.1441 | 2026-08-28 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 00407e30-c929-32c8-99d3-1a7f949928aa | -7.5332 | -70.0148 | 2026-08-28 20:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7fd3f567-9bfd-3e05-999c-8ac2bbd0eb42 | -6.9272 | -70.0046 | 2026-08-28 20:00:00 | GOES-19 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 73a826ad-acb2-396d-923b-970677f36eae | -21.5147 | -55.42 | 2026-08-28 20:00:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 126.5 |
| c679ead4-6965-385d-a95c-9565b1e9659d | -11.4968 | -45.1071 | 2026-08-28 20:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 39c24894-2acb-327c-b27d-7110e264e81d | -14.9205 | -52.6241 | 2026-08-28 20:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1cdc215e-3ae9-38b0-924d-720c79a0a5c4 | -10.5147 | -59.6379 | 2026-08-28 20:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d8db83ab-9eba-3840-9c68-1d5f565d487c | -14.622 | -50.9117 | 2026-08-28 20:00:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 7914f4e8-49dd-34cf-8959-00f8359bc41e | -13.8752 | -54.1153 | 2026-08-28 20:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 621aaed8-9718-30b0-8c18-04333d1749c8 | -6.1472 | -57.7995 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| a1069767-bec1-3f0e-86c4-971f3303ccca | -11.0247 | -49.6656 | 2026-08-28 20:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 02a1df8d-8037-35fe-a1c3-c8450873d34e | -16.5027 | -54.4363 | 2026-08-28 20:00:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 152ec278-57f0-3b1f-a1ed-3a2e2ffeb775 | -8.5366 | -55.2625 | 2026-08-28 20:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 0a5f8a09-2056-365f-b0b0-647074e25442 | -9.8028 | -46.373 | 2026-08-28 20:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.4 |
| e131069f-8c65-385f-b1a5-36a30a1e90cf | -6.7698 | -55.6844 | 2026-08-28 20:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 6ba89151-4e58-3c93-a022-2b4f6f4ebf73 | -8.5971 | -54.7553 | 2026-08-28 20:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 0bdc09d0-0fd5-3482-b4d8-64d2261d1df2 | -6.8955 | -43.6601 | 2026-08-28 20:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d311fac4-6643-3b8a-93a3-3d47810b0353 | -5.8894 | -57.7708 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 310.6 |
| 39600cf8-2294-34fd-b6e6-28103b8b94d4 | -9.9708 | -53.9419 | 2026-08-28 20:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| a687735d-ccfd-3469-90cc-d6150c437cb0 | -15.577 | -56.2916 | 2026-08-28 20:00:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 88164d4f-ec4b-3cc3-89d4-0ff4eeb81e4b | -12.3611 | -50.5846 | 2026-08-28 20:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 2d445e82-e488-3560-b6a2-e68002c8664f | -12.7603 | -44.2608 | 2026-08-28 20:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 7b03adb7-acdb-3571-9411-8f8db02a9eac | -6.9521 | -58.9506 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 9f8e1d50-68a8-33bf-8d84-a2f7ec84175e | -6.7514 | -55.6654 | 2026-08-28 20:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| d6c653cb-46fe-3ea3-ac84-700283b78e03 | -5.2709 | -45.1173 | 2026-08-28 20:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8468666c-dd86-300c-b34d-6619e853de61 | -9.8737 | -60.3149 | 2026-08-28 20:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| edbcef99-bf95-368f-a4c0-ec38328168b5 | -8.0551 | -45.839 | 2026-08-28 20:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 34bd4c43-bf63-3019-8768-1e2960374d0c | 2.2375 | -50.7723 | 2026-08-28 20:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f0c135ed-8bd3-361e-be46-3bd1c66e35e2 | -3.1815 | -61.1613 | 2026-08-28 20:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 92f680d7-95fa-3f80-a31b-9b4ac4f0545a | 0.1367 | -60.393 | 2026-08-28 20:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 74d901a9-613f-3fc8-8f7c-5e26c0e87d95 | -17.5988 | -51.6465 | 2026-08-28 20:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 119.6 |
| d933deaa-23b1-3325-9c2f-0e7d972cce71 | -6.949 | -59.4719 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 0496616b-3dbc-3bc5-9afa-f6a18373d925 | -15.5576 | -56.2938 | 2026-08-28 20:00:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ae8cc986-74f6-3e23-abd2-753353b1664a | -10.7598 | -54.0179 | 2026-08-28 20:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| be90ab14-2743-3cd3-84cc-878b6727a3ce | -8.0303 | -47.9926 | 2026-08-28 20:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9afc1ff6-0938-3bdd-af70-089c073f9651 | -6.8569 | -59.4564 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 604df9d1-e0e4-3700-9e16-ad7b446483fe | -11.0244 | -49.6872 | 2026-08-28 20:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3f5f6f5a-d937-33df-a7dd-60a6f721d768 | -7.5479 | -61.2866 | 2026-08-28 20:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| ac759a7b-8180-3129-b56b-42c692d7788c | -5.4177 | -43.1986 | 2026-08-28 20:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| b845fb6a-6f34-3c40-b97a-02b02149519c | -7.5333 | -69.9965 | 2026-08-28 20:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 5d8f72f6-738e-3730-830d-e39969493411 | -6.7504 | -58.7268 | 2026-08-28 20:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| a4dd1fd3-a65f-3a4b-ae92-3cd5d130e391 | -5.9079 | -57.7506 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 07f0d362-f890-3270-9f68-3dc3d7391ee0 | -17.9681 | -50.1762 | 2026-08-28 20:00:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| f84d6658-826a-34a3-ab37-5868f393453a | -14.9011 | -52.6267 | 2026-08-28 20:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 8811ab26-2030-313a-99ae-037e523c03ce | -5.399 | -43.1999 | 2026-08-28 20:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| d59348b8-03ea-3dec-aead-ac67c167d04b | -12.3803 | -50.5823 | 2026-08-28 20:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 822f99f7-ed68-3629-bc4d-3639ab359d4b | -14.9389 | -56.3011 | 2026-08-28 20:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 362793c1-409b-326e-a6a3-4e7e2b59db69 | -14.9008 | -52.6479 | 2026-08-28 20:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a80568ac-56b2-38d8-b88d-f377481226ba | -2.5516 | -45.3162 | 2026-08-28 20:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 01fd598b-9761-3300-ac09-165d1309c125 | -6.9489 | -59.4912 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| fe01a2d4-cb77-3636-9d94-f4317fe5374d | -21.5152 | -55.3985 | 2026-08-28 20:00:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 14f55f6c-917d-32ee-b9b3-c51eb93ed2f7 | -11.0254 | -57.2237 | 2026-08-28 20:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 661.6 |
| ad97746d-eacf-32bc-b047-d7fdc347b4f5 | -8.0115 | -47.9943 | 2026-08-28 20:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| ca63ad37-dbfd-3c59-99b5-abc50cef71ad | -10.4795 | -64.4824 | 2026-08-28 20:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 151.5 |
| f41336fe-7054-39ea-a3c9-5386142e6368 | -14.1594 | -53.1429 | 2026-08-28 20:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 42541d5a-f5cd-3a59-9a5a-190a0df2243f | -5.9819 | -57.6892 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b64fa966-681b-32a7-816a-cf9633067aa4 | -14.8817 | -52.6293 | 2026-08-28 20:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| ba501136-31c4-36fc-a126-cb89029e2f4d | -14.9015 | -52.6055 | 2026-08-28 20:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| cb9ffcc0-f486-3cf0-9261-3635f5bf53fb | -10.5711 | -59.6149 | 2026-08-28 20:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 240ea52a-150f-3f6d-b5c3-1c162e1094ae | -14.9 | -56.3257 | 2026-08-28 20:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4ee2c2df-a785-310f-bf72-99fb93f4bdd7 | -9.7838 | -46.3752 | 2026-08-28 20:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2167b1b5-01a7-36a9-8746-923a9c47bebf | -7.5516 | -70.0146 | 2026-08-28 20:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| e38b4ed4-7508-3f6d-9918-b97e40898173 | -3.6216 | -60.528 | 2026-08-28 20:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 26affd35-df1f-359d-a6f3-2523759e01ea | -9.2172 | -68.1445 | 2026-08-28 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 098c768e-260c-3028-9383-669629da7a49 | -6.857 | -59.4371 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 83069697-2719-397e-a905-7a42b73f950f | -6.9272 | -69.9863 | 2026-08-28 20:00:00 | GOES-19 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 4bd1ba74-5da7-30ab-8c6b-71dba99be5b8 | -17.5992 | -51.6247 | 2026-08-28 20:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 236.3 |
| e256345a-dc3c-36c9-89d4-b7a2733ce6a9 | -9.4329 | -51.6926 | 2026-08-28 20:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 0b4f44ae-ce8a-3266-95ba-857c79056c17 | -11.6215 | -54.5742 | 2026-08-28 20:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 3ea31efe-b22f-329f-8ad5-a954b1b49987 | -13.5991 | -45.772 | 2026-08-28 20:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b3f8b9d0-2dd6-37d2-9ecf-dc527b224c07 | -20.9207 | -57.5723 | 2026-08-28 20:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| da40d0f6-e2e6-3e51-9f3c-d7e8d4c696e1 | -12.7797 | -44.2576 | 2026-08-28 20:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 18ccc007-076c-3f09-a9fe-86b145adbd0c | -9.0012 | -57.5585 | 2026-08-28 20:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 5041e9c5-c04e-32e5-8726-2a78f2e7af4d | -14.3569 | -51.6995 | 2026-08-28 20:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| fe3a1fcf-89a3-3cfc-b4a2-adb4d93e5059 | -9.1523 | -49.9853 | 2026-08-28 20:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 9339b227-a141-3cfa-af7f-bf0530d4c308 | -8.6197 | -70.2189 | 2026-08-28 20:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3b4bb98c-4a01-399f-9690-34c9c90d2aeb | -10.0125 | -68.8476 | 2026-08-28 20:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5590370d-5491-3a7a-9ecb-63df639cce40 | -6.8756 | -59.4171 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 921e8b80-b007-3332-a913-4b881c2feadc | -9.02 | -57.5377 | 2026-08-28 20:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7b59d679-4967-3380-9830-c1c902702410 | -6.0004 | -57.6884 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b198f307-ea4f-3331-8ce4-df5e897541c8 | -11.7167 | -54.5244 | 2026-08-28 20:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 64443517-7dae-3e52-98e1-dd55edbbb9e0 | -5.2446 | -43.7457 | 2026-08-28 20:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5c96dc9c-8dd0-3313-b213-77b39309f7e1 | -7.5477 | -61.3247 | 2026-08-28 20:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 195.7 |
| b6fd0dfc-27d6-3e87-add5-6fe9e17fef63 | -9.4327 | -51.7135 | 2026-08-28 20:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| d55f97cb-ec2f-3c6a-83c0-8af8f10a3fd1 | -17.9875 | -50.1948 | 2026-08-28 20:00:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 797e6ba3-a39b-3d86-bd91-c02b0b0aae5e | -6.7832 | -59.4401 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 59e2c0cf-46eb-343b-a768-1ef303f16fbb | -11.6212 | -54.5947 | 2026-08-28 20:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 804b222a-c70e-3dbf-bd53-57e55da21d86 | -9.0014 | -57.5388 | 2026-08-28 20:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e4c3f46a-fa75-3c39-a436-6d0be6324069 | -6.7647 | -59.4601 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |


[Clique aqui para ver as próximas entradas](README177.md)
