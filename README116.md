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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8aac577-5999-31cc-be57-c4b5ea59564a | -18.17815 | -56.4376 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 233.5 |
| aa3fc994-6f7a-35fc-b53a-452b5a0f76d0 | -18.17678 | -56.44699 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 59f7626d-cda9-36a7-a9ab-d39c4a44359f | -18.1706 | -56.42682 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 2f2ab017-2888-377c-800b-0a031bc75a44 | -18.16923 | -56.4362 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.9 |
| f730e34e-3706-3f11-b09d-e23a7eba8cd8 | -18.16786 | -56.44559 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| c249dd69-8e2d-3e33-893c-5624f6af6b92 | -18.15894 | -56.44419 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| cfd89138-bfec-35c9-966d-a3cb0f02b0ce | -18.15139 | -56.43341 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| cf3f349b-0e19-38e1-b16b-42ccc6b65dc3 | -18.1157 | -56.42781 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 52634572-6364-3f64-875d-37a284e7fdb9 | -18.11434 | -56.4372 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eb4430f0-1b44-389c-924b-6d946ee9dcbf | -18.10122 | -56.39964 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a1954af7-bb79-3e7e-a4f9-e7d629584923 | -17.72568 | -56.2587 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7325b4c3-88ec-3630-86cc-bca6f18af551 | -17.71885 | -56.3056 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 17774730-2286-3312-b1dc-e91c6e039ef5 | -17.71748 | -56.31497 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bdf70321-3f44-3f54-92ed-a9ff2370af26 | -17.71675 | -56.25731 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 5d43c4b2-1f18-3e20-9b5c-1f1d96ed9352 | -17.70992 | -56.30421 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| f199a952-0cdb-3e98-8226-1686e72e8a30 | -17.70856 | -56.31358 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 99bb16cd-e2a2-37b4-9b82-841442018646 | -17.701 | -56.30282 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| f531b153-5c56-3cde-aa60-38f6f101e2c1 | -17.69963 | -56.31219 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 9f372bd2-6c17-357b-8601-a43be779bb53 | -17.69827 | -56.32156 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 515d85b0-836e-3551-bb7b-a1a9fe77768b | -17.69071 | -56.3108 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 75c8ba42-faa0-3429-9a71-313f427e8ce3 | -17.68935 | -56.32017 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 5eeafb3e-462f-3b5a-84f3-52333b44bcd9 | -17.68179 | -56.30941 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| af9bd6e6-6d20-3311-9f48-2325bd2f1440 | -17.68042 | -56.31878 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 228d2dfa-ce24-33e8-accb-baeddc7689d3 | -17.6715 | -56.31739 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 90012ad8-b3e0-37a6-976e-61833a949e8b | -17.66747 | -56.27249 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| a1644113-3045-3495-9e49-2a2a292f93c3 | -17.66061 | -56.31932 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| ca92878b-524a-363e-8b57-b73687deede6 | -17.65924 | -56.32868 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 164ca620-64d0-304f-96ca-d01addd09682 | -17.65306 | -56.30857 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 6420196a-e7fd-3484-970a-8bfe0ab60b02 | -17.65169 | -56.31793 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| a4c3f79c-dedf-3e91-814b-261b8f345d98 | -17.65032 | -56.32729 | 2024-10-11 05:57:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 73a7720d-7950-38ea-a6de-5afc038c9f53 | -17.16661 | -57.47307 | 2024-10-11 05:57:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3fddb6a0-d578-3964-af00-03b3e64b56e0 | -16.97794 | -57.43955 | 2024-10-11 05:57:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| ec7afa7a-40f9-3537-aebe-efff6eaba37a | -15.97894 | -59.09081 | 2024-10-11 05:57:00 | AQUA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5aef525-6fc7-3155-9315-2b8a1048e613 | -15.96774 | -59.09974 | 2024-10-11 05:57:00 | AQUA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8b75641-07bf-37fe-9475-d31dd87b36ce | -15.69914 | -59.34557 | 2024-10-11 05:57:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec8003e3-8597-3733-a026-c8910b98eb7b | -15.63827 | -59.41402 | 2024-10-11 05:57:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2f356a10-003d-3836-8b11-42b6703f64a9 | -15.43806 | -60.00556 | 2024-10-11 05:57:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ca5381d6-de02-35ad-9dae-bc42f5ac741f | -2.27684 | -66.42993 | 2024-10-11 06:03:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5829b1d6-0a40-3577-a8c6-2e5e476428fd | -2.38466 | -57.16602 | 2024-10-11 06:03:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae3bd3a8-218b-3905-b0f7-c51c3402a91a | -2.38329 | -57.16059 | 2024-10-11 06:03:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ca7cb43-5f3a-37da-aad0-856241e49418 | -2.38234 | -57.16716 | 2024-10-11 06:03:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecadf1c8-1473-3746-805f-cae91eb6131c | -3.63595 | -58.62677 | 2024-10-11 06:03:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1837e4c5-3dd3-3471-b32a-2e39b48fba70 | -3.63513 | -58.63239 | 2024-10-11 06:03:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8571c525-e103-365b-b2cc-38e1a60ed0b3 | -3.53539 | -59.47504 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 244acaec-7e36-33fb-b412-470155ed04b1 | -3.40864 | -59.74822 | 2024-10-11 06:03:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71c87a3d-d344-37f8-8a88-35425624aea3 | -3.40853 | -59.7503 | 2024-10-11 06:03:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af70c7e8-e3aa-3c36-8431-03e40f9ccc74 | -3.5347 | -59.47997 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 597d1b25-f90b-370a-ad5c-07bbdc1b73d4 | -3.47566 | -59.50314 | 2024-10-11 06:03:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ceb75fe-2b95-3697-977e-e5bb54f28df9 | -3.47496 | -59.50793 | 2024-10-11 06:03:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b40a0812-82b4-37e1-8f2a-41eee30a4715 | -3.41475 | -59.74913 | 2024-10-11 06:03:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d5adc65-ab46-3ec7-9691-6d1a044d81c2 | -4.28449 | -60.01512 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cc6eac4-80ad-369a-8d9c-6b4a982596fa | -4.26449 | -59.89372 | 2024-10-11 06:03:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e6bf20e-3052-3321-add7-629d38d042de | -4.26145 | -60.00248 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7790ed06-5bcc-35b8-b32a-61f51c9747ac | -4.25668 | -59.99234 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19fdea62-2d4a-3682-a388-4871e2a09c23 | -4.23225 | -59.85825 | 2024-10-11 06:03:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44c32545-e145-31d0-bfc6-dd3d77cc1f44 | -4.23156 | -59.86295 | 2024-10-11 06:03:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d0a3c8-795a-396b-8217-fa519a2c5e07 | -4.29057 | -60.01601 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dbc7126-6dbe-3697-8743-393351391534 | -4.25602 | -59.99702 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a780e4cf-35e9-31e0-b399-b679abbdb5d4 | -4.25536 | -60.00161 | 2024-10-11 06:03:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebc3b118-635f-3539-b98e-3ea4cee9ca64 | -3.04434 | -61.68036 | 2024-10-11 06:03:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29a6dba4-ad60-3c5d-8751-4c79e1963d10 | -3.04483 | -61.67701 | 2024-10-11 06:03:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5ef0ea2-88f2-3f4a-aa14-68b3d7ee666b | -3.03898 | -61.67957 | 2024-10-11 06:03:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a638a281-ff89-3253-8806-9a8d59f4474d | -2.99805 | -61.41802 | 2024-10-11 06:03:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1efce643-a753-3d7f-8d4b-b663f3e74623 | -8.70241 | -66.99887 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9830202f-bc8b-3ef6-b811-d5f8ec84281b | -8.70191 | -67.00247 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3e68e96-a255-34c3-a257-4971f598cbef | -8.69785 | -67.00186 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 368b0ed4-2b18-353e-be5f-e36903d21ef2 | -8.69731 | -67.00158 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 972b85e2-9f94-3874-ac72-83873227649d | -10.09741 | -67.34802 | 2024-10-11 06:05:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92ece65d-79f7-3f70-861c-800bd9ad7a57 | -10.09327 | -67.1396 | 2024-10-11 06:05:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a6e68846-7207-3805-9d15-d2d5f3b79281 | -10.08918 | -67.13902 | 2024-10-11 06:05:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16ad0da7-f892-383c-baca-e6624f8472d8 | -5.57084 | -60.17049 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fab43fb7-2a01-347b-b31b-3e88f1550571 | -5.57062 | -60.17352 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cb4abab-de62-37ab-9726-1d2fd095f544 | -5.57018 | -60.17517 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccdb839d-77ae-34ca-b8fb-caf8d772b3d1 | -5.33323 | -60.12484 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce35dac1-d59e-3778-9159-7dbce0478fa4 | -5.33257 | -60.12954 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd02aea5-d449-3dd9-a70a-fff90d088470 | -5.3319 | -60.13424 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac3f5980-c3fe-3e47-9a21-bcc08d45e374 | -5.33124 | -60.13894 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d17d376e-b9eb-3fc2-b23b-ebec4e8231fb | -5.33059 | -60.14358 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb3fc48a-40bd-324d-972d-09470cbea036 | -5.32644 | -60.12867 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e384c15-f40f-30c7-a7f3-cb81ee03857d | -5.32512 | -60.13803 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7c83753-3d7d-38ea-9266-eef0d5644ec1 | -5.32447 | -60.1427 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 079ca90d-957e-3db3-bc4c-2b2481a7cde3 | -5.32381 | -60.14738 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e1c7fd8-c954-3ba9-86da-d197c411e2c6 | -6.79452 | -59.63807 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5206a348-676a-3d74-afcd-19a596d7b28d | -6.79329 | -59.64181 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce31ad5d-512e-3aba-acc6-7378cc2f60ca | -6.79256 | -59.64716 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dea4b266-d2e0-3170-8721-ef79a3968bba | -6.55324 | -60.03412 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 883083f8-53b3-35cd-bb44-cd8a56c15179 | -6.55046 | -60.03536 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 702d9c45-21fd-3ba4-bddd-4e128ba3aab0 | -6.54693 | -60.03358 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f25db80f-2a90-3493-ad45-f0a42a7cd8c1 | -6.54443 | -59.76956 | 2024-10-11 06:05:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fdd5538-8d0a-37cf-9584-0a10daea27ae | -6.54415 | -60.03475 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1280deb-732a-356a-98f9-a283b9838c76 | -6.54065 | -60.03283 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66c492b7-aca6-3848-b9a6-edbabe391c2d | -6.53807 | -59.76859 | 2024-10-11 06:05:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8253524-fea6-3fef-9f61-dc326791ba4d | -6.51783 | -60.05959 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2194ebc1-bd51-3a7f-a61b-da838d483b75 | -7.08816 | -59.41305 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21c55af2-1aeb-368c-9e8e-e235734e42fc | -7.08329 | -59.40837 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16caa66d-50b5-3d25-939c-f850b5ee6a65 | -7.08281 | -59.26414 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb9da82e-5109-3549-a3f9-dcdceb482ddd | -7.08252 | -59.41393 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2fe6a42-0df7-31cb-b6d2-5fc0dfb55b4f | -7.0816 | -59.4122 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a423e3e6-1182-3c59-91ac-bd7dc1fb4f6a | -7.07597 | -59.41304 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3edcd9b3-08c9-3229-900a-7c2c5bbb8b55 | -7.0754 | -59.26915 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README117.md)
