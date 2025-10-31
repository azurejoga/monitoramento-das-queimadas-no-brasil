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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf18cd22-b339-3a32-a425-5c1cb599eb5b | -3.87436 | -42.44323 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 147a9180-3d6a-3237-8bfe-acb5767af3af | -3.92858 | -43.37473 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c18140bc-34ce-324c-a029-198c64fc3c2a | -6.22581 | -42.52762 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 94de84d9-8f6c-3c92-af14-611c52f3364c | -7.31062 | -44.98219 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6b137c20-cab2-3dcf-b138-68c87b729051 | -6.51671 | -40.79783 | 2025-10-31 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b2d10dd-60c9-3ef8-acdb-f34b1265d710 | -7.40327 | -39.82784 | 2025-10-31 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d01a97c8-3aa1-335e-8730-fb0c9ca0a31c | -6.54764 | -44.47252 | 2025-10-31 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1cf41996-c529-37b8-a59f-339fb1d1d3d5 | -5.62664 | -41.53207 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 402d7f7f-ed70-3ca1-9cd7-272d58361183 | -4.47295 | -46.56199 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b35b8b1-7498-36c3-9f93-04b19d0797be | -6.23306 | -42.52514 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f7b1e373-05cf-3085-b11b-88480e85371c | -5.69772 | -43.14859 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 098d941f-15eb-3972-a43a-d05b13e94fff | -3.40785 | -46.90374 | 2025-10-31 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d05a2d36-c804-3ef7-85d4-aa3c0a857b49 | -5.20242 | -45.41859 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76f9f5d7-aca5-3225-87c2-578ddc1f813d | -5.41905 | -44.58505 | 2025-10-31 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 533a359a-353b-3f53-8bdf-ef9d0ae35e02 | -6.44627 | -44.42833 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3141a341-9464-34c7-9583-3c05e56a1f4a | -7.04254 | -41.47348 | 2025-10-31 04:06:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6d74fab3-bf63-3732-8ad9-6c67292866e7 | -5.18032 | -46.15167 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 122a31dd-08c5-3a31-a047-f624bd66eb6b | -2.31772 | -48.5766 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 421911d3-707c-3088-a691-b8d06a31f91d | -6.10251 | -41.74569 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d74cabd1-7baa-3a95-bd1c-8a213d060e16 | -5.12957 | -49.69566 | 2025-10-31 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f318fc1c-efb3-304d-be6f-2f6cb48a56da | -4.86025 | -45.56406 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed30e7e4-1af5-3aaf-addf-a349995c0c0f | -5.92651 | -44.57497 | 2025-10-31 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9b21760-b249-37c1-8188-f566e31c6954 | -3.48277 | -46.01815 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91217adc-bd96-32bf-8ea7-b91afec2970c | -5.85559 | -44.7112 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8052981-8261-3cff-bf8c-98012b9c3414 | -7.3143 | -44.98085 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 76662d31-eee2-317d-b923-39dfd64ab875 | -5.64099 | -45.01667 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcc4dfad-9ead-3174-b7ca-ea66cf671f65 | -5.75031 | -44.52752 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8453f3c0-6fb4-345e-b75f-4abff1b8a23c | -5.27988 | -45.42636 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c451e0bc-32c8-3af4-9516-60e803be735f | -4.90632 | -45.72392 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15d95059-3b55-3afb-9b1f-1f21e509a134 | -7.3479 | -39.3377 | 2025-10-31 04:06:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69b79501-62d8-3c9e-86ea-1489a322e869 | -4.74145 | -45.89725 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2574c8d-9ddf-3f5d-aaf4-071cd3b03d29 | -6.92278 | -42.25019 | 2025-10-31 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f549a991-0fe9-3cf9-8ff4-d2023f03075c | -6.03087 | -46.5565 | 2025-10-31 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07ade2d2-ef49-3cfa-a805-622e32ea0925 | -4.66344 | -45.08954 | 2025-10-31 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a62386f9-a347-3025-bb88-82399fbcf3c0 | -7.04585 | -41.47401 | 2025-10-31 04:06:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 26826031-547c-3cb8-97fa-f9cd2b81e8ff | -3.2987 | -51.92611 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de548f8f-361d-318e-974d-7e7853a39d26 | -3.47809 | -46.02112 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f193d340-e488-3408-aa53-d70c9a541f2d | -5.02032 | -41.04767 | 2025-10-31 04:06:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f68e1d52-39c6-3516-b0df-047675d62076 | -2.31585 | -48.58799 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3af82deb-5fe4-3c5f-ab51-fe3be3ed8ff1 | -3.81665 | -45.05341 | 2025-10-31 04:06:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cae379c8-1a10-34a0-b929-a3dc6e282c26 | -3.45374 | -45.99095 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5094d88f-8208-37bb-8953-a088f41c454d | -7.09328 | -44.37458 | 2025-10-31 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50248600-f449-339a-8d5e-2e4125d1ad6d | -2.45025 | -49.01722 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db934382-87e4-32fb-8b01-6436dfe1d9bc | -4.67151 | -45.80977 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80050243-3494-37cf-8e1a-91b2c67248a2 | -6.08482 | -44.5438 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f64484cb-9e45-3eb6-9220-d2bc0fdc90b7 | -4.53714 | -43.42434 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b7d64b3-1b21-3e60-b18f-19e1ae47e518 | -5.31705 | -44.84166 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4991efd6-abc1-3971-9af0-a356e402f2b8 | -5.33366 | -43.4929 | 2025-10-31 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fe16a10-d47c-3583-8268-049ff9513805 | -6.55271 | -44.02261 | 2025-10-31 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa22f9a3-75a3-391a-86c4-3c5bded1a173 | -3.29951 | -51.92134 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a196561-3883-3b02-8bdb-e3ffab0b762b | -3.93993 | -46.97016 | 2025-10-31 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92cdf035-cab8-3e13-a391-a175579fd69d | -5.6419 | -41.0892 | 2025-10-31 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d179a9f-19fb-32bb-9c64-2bb4d133cf85 | -4.90122 | -42.97487 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 593c6d84-bbe3-39dc-8a92-a6487029f269 | -3.52898 | -47.55271 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c5d54157-af73-365e-beea-c640643b425a | -2.45075 | -49.0142 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2041c242-22e2-341a-9cf1-0b1c91e2ba4e | -6.36758 | -40.96999 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81cf62e8-d695-3de5-8839-f1c61f62085a | -4.83385 | -45.32949 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e975fb2e-d357-34e7-ad49-e431de4e83b8 | -5.03477 | -43.61238 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8c55e656-7e39-33c5-8e21-2b7fde092228 | -4.4211 | -43.37128 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a79ddd3-d2e2-380f-b7ce-d0f87f2a4a95 | -7.58294 | -42.01014 | 2025-10-31 04:06:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54134ff9-245c-3198-93c9-2874a82c6bc9 | -6.92333 | -42.24672 | 2025-10-31 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a980e9b2-bba6-3c30-b7c2-3d7f3ef7b0eb | -5.62024 | -45.98054 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1ee99e6-a1ea-3b08-bc6c-99020747d841 | -5.60817 | -42.79331 | 2025-10-31 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c70a1e1c-1092-341a-8148-3b1a261d86d3 | -7.32016 | -42.48588 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ae8f6a3-a286-3cc8-a921-ffe51b7025e4 | -5.54132 | -48.38241 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 968544c5-db5c-34be-8b8a-0f6b218b189d | -7.44182 | -44.24061 | 2025-10-31 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32f0e9a7-19e1-37a1-8f73-a8795c9025bb | -7.04668 | -44.78778 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 737e4d87-1a08-36be-83f4-76edb12acf7f | -6.47976 | -44.4254 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32b052d-6966-30fa-b7ee-2d232c33f939 | -7.68413 | -40.91257 | 2025-10-31 04:06:00 | NOAA-20 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 65c2951c-13f2-3ca3-96d8-338705a5181d | -6.22972 | -42.5246 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c63664e0-824a-395c-9c87-97101260c1d9 | -2.91937 | -48.72972 | 2025-10-31 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b7eca141-a8c0-3286-9bdb-74e8c3adf3fb | -7.28032 | -41.90477 | 2025-10-31 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60b6820e-2bd7-337f-afa9-25b952f9af51 | -4.56553 | -43.27168 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed67987e-638d-3f07-a8e8-a2cced689db5 | -3.28888 | -51.91009 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e26d9261-b468-3de6-9f60-e32b1df73cb4 | -6.2041 | -42.51334 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3b20c29f-668e-3a2c-9467-6aa160c2ed2c | -6.92891 | -46.01493 | 2025-10-31 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7a0bb6a-f4f3-389e-ab5b-d29331c74786 | -7.84103 | -40.25599 | 2025-10-31 04:06:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 85f12bd3-0122-33ea-bc87-f6bb749a8e98 | -6.012 | -41.97313 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b0abf2a-565f-33bf-9171-cace8161312a | -6.01587 | -41.97018 | 2025-10-31 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42372a6e-7a0a-33ea-a098-8e10fc3f67fd | -6.19961 | -42.51997 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9e85d342-0d18-3b32-94e0-2439e72166ba | -5.32333 | -44.75724 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a2b5027-fecc-3ff0-81c3-7a5660fb8fd3 | -4.3037 | -48.10791 | 2025-10-31 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acf18657-64dc-3e5d-9942-c59f8a81ccbb | -4.86468 | -44.64954 | 2025-10-31 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23b0680b-4987-350b-8c81-2a27e31ea5e4 | -1.05459 | -47.34382 | 2025-10-31 04:06:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afbaa732-233b-3f55-ad08-a10d870a9980 | -2.0999 | -48.05014 | 2025-10-31 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 62e7f5a0-f79c-34ab-b351-424c257dca92 | -1.95455 | -47.8604 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 951871e8-cf1f-3f35-9eb8-da5938cfd612 | -7.16253 | -44.99238 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9364e79f-3c1b-3bc9-8d4a-d682bc636eaa | -6.10747 | -41.71454 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 00688e5c-847d-3d5e-a42b-d827b4aa2927 | -6.01599 | -43.57122 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c10d907e-39f0-325c-8d39-8d7f0b6437ba | -5.85995 | -44.70754 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8715a58-6886-36ec-8cb2-7d0d4e0b0878 | -3.52972 | -47.54813 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 22c73966-1f99-3fd3-b70c-549312be8f3c | -5.69653 | -43.15594 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3e6c0dcf-95e3-3c98-b51f-8ec4597825e7 | -4.67482 | -45.80743 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a31ce9a-4052-3a9f-b3fd-9264fc801be9 | -7.78769 | -41.57448 | 2025-10-31 04:06:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf4c8f74-5bc5-307c-96c5-e3530f89c97f | -5.65047 | -46.40927 | 2025-10-31 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 725f94cf-8e9b-3b89-96e2-95c10ff82d80 | -4.56883 | -45.40474 | 2025-10-31 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 207c5d95-3660-3b16-bc32-b6efecc248a0 | -7.31558 | -44.95274 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d7d2d4b9-9e53-3e6c-8cd5-02e47aaa31d6 | -6.0855 | -44.5467 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02c1479a-b945-31a5-98d4-334c2821631c | -5.70803 | -48.88356 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a6601aae-d09d-366c-9cae-5c8ed7ac8c3d | -7.60358 | -43.55604 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README21.md)
