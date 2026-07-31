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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4eb43b1-6b92-32a0-b9af-7229bae9f079 | -4.22012 | -56.04907 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 784e29a0-a461-3b16-bb68-abca291be2b9 | -6.55513 | -41.84425 | 2026-07-31 04:40:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| aa0e2e9a-5cfa-335d-a844-40be4fa43995 | -12.61361 | -44.60118 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa3ffb5d-fd30-3acd-a7bb-4a59b77ac70d | -10.18401 | -46.50142 | 2026-07-31 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| affe4ded-20ab-3341-8f00-7e2fdd6d4c71 | -11.44567 | -50.09694 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f096ee61-f6be-307d-bf38-aa05356e7a05 | -12.33971 | -48.21909 | 2026-07-31 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6e244b5-2709-36c9-8b63-8d707431e6c2 | -5.81113 | -43.63784 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55ec9f94-0ffc-37fe-8df4-e0545d6e16b4 | -12.62005 | -44.59531 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d4c2704-f921-3ee0-94f9-b1783fb77f20 | -12.62438 | -44.63065 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0bfa7b2-05e6-3223-840b-eb7d8bfec3fb | -7.62838 | -49.49942 | 2026-07-31 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ae6856-d3e6-3ddb-8231-35c4fb38c1dc | -12.3438 | -48.21564 | 2026-07-31 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c6a750c-f8bf-3258-88f5-91e8a5a716b4 | -6.12617 | -43.76096 | 2026-07-31 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6866c9e-8d74-347d-8319-8a18a779e132 | -6.18988 | -44.84994 | 2026-07-31 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc500f1c-33f9-39c7-ab47-e817130404d6 | -9.63404 | -40.59775 | 2026-07-31 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5d791a70-f441-3854-97f3-6ac79b2f0a92 | -10.1897 | -46.49944 | 2026-07-31 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc6f19cb-8fb9-30d0-b395-5b6ed9198a28 | -11.47496 | -50.10519 | 2026-07-31 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66b309c4-0b14-3d33-8285-6e2d3a087c17 | -9.003 | -45.18556 | 2026-07-31 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c242f011-7c2f-3505-920c-36afe238b48f | -12.59223 | -44.62828 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48093e54-44cf-3660-adbd-75708b1f2ecb | -5.80634 | -43.6412 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2544f81d-d3d2-3d0f-ac67-18ed17136e7c | -6.46095 | -47.85252 | 2026-07-31 04:40:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e124e2c7-2e02-3a08-8e2e-1178fe9d4148 | -6.56758 | -55.14695 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecf08437-57d8-3f96-8167-0a384977514d | -7.36477 | -43.83442 | 2026-07-31 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f399355c-8093-3269-b650-60554f7c5658 | -12.61569 | -44.62935 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14a9c5f8-7fac-3a4d-bacc-5b94ee538943 | -9.09087 | -47.07046 | 2026-07-31 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e99e15e5-d7c3-347f-b153-52cf1900971b | -11.37334 | -50.56355 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ab789a2-3f62-3021-b1a9-9122c057c7f6 | -12.60537 | -44.64083 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bf2fcdb-9f3a-3ac5-b061-98f641fac2d3 | -10.48545 | -46.31865 | 2026-07-31 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68e5cb07-56a4-3c4b-af91-ee59d00f6b36 | -11.25274 | -40.3443 | 2026-07-31 04:40:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a24be382-ea44-3151-a022-8d90bac1af33 | -12.20213 | -47.97003 | 2026-07-31 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fed00b00-a53d-3843-a8b2-8a5df1442bf7 | -6.29468 | -43.82425 | 2026-07-31 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20148fac-3fc4-379f-8e12-a5202f12714e | -11.8335 | -45.60154 | 2026-07-31 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43704b6d-36f1-36dc-9624-7e7afa6e135e | -12.62873 | -44.63128 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fb3bd62-f6d4-330c-91bd-c7f2cc8c8b3a | -12.45522 | -43.53369 | 2026-07-31 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e86d1fa8-4e2c-396a-937f-d21bec164332 | -5.93469 | -46.35165 | 2026-07-31 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 980e1ad0-75c7-3323-bbc7-7af4150efda7 | -12.61025 | -44.63725 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 365fbefe-7593-3f99-95e0-03a6ce2ffbba | -10.1928 | -46.50447 | 2026-07-31 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5025efcc-0fff-31cf-9fc7-4919a18cc5cf | -6.18668 | -55.52193 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59312bfd-2fe2-31d8-9233-adb67a6122f7 | -6.30221 | -43.65136 | 2026-07-31 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c87e672e-e3ca-3c50-99fd-58ac27874bc2 | -12.61336 | -44.63575 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df62903c-4b86-3d1b-b34e-0ad668bb9d92 | -11.83274 | -45.59859 | 2026-07-31 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1c4c8a19-8941-3511-96e1-afd27c1b776f | -7.87444 | -45.23299 | 2026-07-31 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 907d95f3-9666-38c6-9065-4dbd7453a365 | -6.17597 | -55.53274 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6beeaf65-0769-3e01-b9b7-72d29f554910 | -12.61886 | -44.62785 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89c939d4-95da-348f-857b-e1f4c8378fa4 | -11.37003 | -50.56302 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cbaaffe-f82e-3bf4-9204-1e4f65df8175 | -11.41143 | -46.81849 | 2026-07-31 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7045040-bab5-3f23-a26a-2baeac4a5815 | -5.63887 | -47.10471 | 2026-07-31 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e24153e7-2708-3da4-90d6-560b84e84e96 | -12.61949 | -44.63427 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86c5e0bb-9823-35b1-9298-dac7061d699d | -12.61418 | -44.59694 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f35bca5-9190-3065-b0f9-3cec99088082 | -12.20154 | -47.97408 | 2026-07-31 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bbe4378-e7bd-3558-be2e-83949e93666c | -6.18098 | -55.52938 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abc7050d-564c-3c80-a1f0-13609a742113 | -6.18168 | -55.52528 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d921352-a837-33a2-9560-d9d22cd3f090 | -11.47012 | -50.1585 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 342e4569-7f0f-365a-9d87-c23c8a7c7b9c | -12.6762 | -43.09573 | 2026-07-31 04:40:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4972a5dc-37a5-388f-a65a-97fa544f388c | -7.72923 | -47.25035 | 2026-07-31 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d71dadb9-cb89-32c8-bc1a-e78780b908c9 | -6.56142 | -55.15786 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 302a8d95-b99e-380b-b0a2-4f67850ff799 | -12.58844 | -44.62346 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15aecf25-aa11-3877-bb70-a0421cc1ea27 | -11.74078 | -48.91408 | 2026-07-31 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d06652b9-a357-3d51-9a7e-a58307a2a17b | -12.60318 | -44.6127 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a2ecda8-6d3c-3635-ab66-6dfc19f6b1bb | -6.186 | -55.52597 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b66213b-a5f3-3803-b550-963fa9c74999 | -11.83398 | -45.59794 | 2026-07-31 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 418b2f26-d9db-3c03-b84e-30061b970553 | -12.61514 | -44.59898 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed0ee38e-f6ba-3f7b-83b7-dcf68d2b16e8 | -10.47571 | -46.36002 | 2026-07-31 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 10a1225d-1336-3076-a00a-26d5553e9df1 | -6.55657 | -55.16106 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa8b306a-1733-34b0-98ad-729aa155c362 | -11.47343 | -50.15903 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55427f97-8046-388f-8440-da37149e7f17 | -11.11798 | -49.70884 | 2026-07-31 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02fe9552-fadd-3bbc-a9a3-59ef5e0d026e | -12.6146 | -44.6379 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a744212-264e-33a0-aedf-3f2a82956c4b | -11.83173 | -45.60577 | 2026-07-31 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb8f55e4-351c-3417-8f40-7398fa5f77e7 | -12.61828 | -44.63212 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a55eab29-dd96-3134-9bdc-aa821d0547bf | -6.17736 | -55.52458 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ae002b4-5365-3437-ad6c-235c79c9452f | -9.00349 | -45.18206 | 2026-07-31 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3f616bc-b931-3cf0-9468-4df6196705e2 | -11.31971 | -50.38283 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32b655a9-4436-390c-94a6-0b412c29dbbd | -6.54467 | -55.15517 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a7d37e-2671-3bae-8ed1-5e53aab09e86 | -6.5554 | -56.53678 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56397a00-b1e6-39c0-846d-ba7bf7134aa0 | -12.61394 | -44.63148 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80779b97-257e-329c-b73d-bad3dfc1932d | -12.61514 | -44.63363 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd01b8e7-d3f9-37d6-bebd-4280f59276c5 | -9.56089 | -47.11289 | 2026-07-31 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db192ce6-8436-3f43-a6bb-f759881e94f0 | -8.80332 | -46.73796 | 2026-07-31 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94270f41-35ca-3095-8519-d4a5f4d69603 | -12.61854 | -44.59752 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5af479b9-9dd0-3892-b9e0-e67dea99acde | -11.45839 | -50.10256 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c751b15-7fff-362c-aafd-5e74dab51f50 | -9.63358 | -40.60133 | 2026-07-31 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 72d32592-51cb-348b-a1e3-44a4df630029 | -11.42132 | -50.07865 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a9f299c-3d85-3977-8ac6-14fac89b0129 | -12.10253 | -44.12932 | 2026-07-31 04:40:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c40ffceb-5423-33d0-90f4-f6e64bd5a0f2 | -5.71879 | -48.12496 | 2026-07-31 04:40:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ba2b3fa-6a2b-320b-bbf7-6bc6ff1e73ce | -6.1021 | -49.38622 | 2026-07-31 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1f469a6-91b1-3fd7-a4be-6f06a5fc392f | -10.19148 | -46.50249 | 2026-07-31 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88522014-d080-3caa-bdf6-9bce88d5a010 | -12.60411 | -44.63869 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fff8ed5-7978-3612-8ec5-56cdeaf12a68 | -12.62004 | -44.63 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5249ef82-5cb1-3b79-acbc-0428c27b60e2 | -7.73874 | -55.34159 | 2026-07-31 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d00418d3-8076-32c7-9b33-a8390184d71b | -10.89984 | -45.20029 | 2026-07-31 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccbd89b2-3cae-312d-bbe9-3f074055be5e | -12.85129 | -44.39743 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eba67854-de1e-33d2-9633-24ec30cdb1c9 | -10.47883 | -46.36517 | 2026-07-31 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad00d8f7-2ab7-3dbd-b285-f1f1c76a76f4 | -12.6146 | -44.60324 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10c5cabd-2eeb-3bc1-b29c-82f066a0e6b2 | -5.82113 | -44.13656 | 2026-07-31 04:40:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39bcdf80-7bba-3b45-a35b-de67af38082e | -11.82771 | -45.60518 | 2026-07-31 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dfdfa9b-7cd4-3f30-b18f-4e67bc5b25cf | -12.61797 | -44.60176 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d92325fc-4842-3f7e-a848-45864f7f79f8 | -6.56077 | -55.16169 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89808420-b48d-313f-9226-b37d4eda3538 | -7.73458 | -55.3409 | 2026-07-31 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc4e4fa0-5730-36f4-b4dc-d5a90c3cc2f7 | -6.70766 | -47.42728 | 2026-07-31 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46ac27ea-c273-3585-8e32-1b596eefad03 | -12.60845 | -44.63934 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27c34685-deba-317f-8a98-9cc75deaad6c | -6.17666 | -55.52871 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README9.md)
