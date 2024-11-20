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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97d5b14f-e5ef-3e35-a2bb-b7097d011432 | -4.44449 | -49.63054 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c844dac-1ded-3089-bd22-d817df0da81a | -2.86859 | -51.78859 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b73eeac0-dd68-355b-a38c-9b6ef91a90bb | -2.81009 | -54.02057 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7158f8cb-746c-3485-8fcc-6a6ee9b9b89b | -5.98475 | -45.73947 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e5aa8ef-d634-3760-b3eb-ff1a6c740fd1 | -2.69812 | -51.36627 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3e64668-97fe-32a3-9134-29ba533e5cf4 | -8.31836 | -45.10954 | 2024-11-20 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4e78046-148b-3ee6-80a6-c74f44b13f36 | -5.6925 | -45.84671 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca1eaf2a-1bae-3686-a31a-409ecabfb0db | -5.69351 | -47.66379 | 2024-11-20 04:27:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f43661b-00e1-3159-9daf-ecd720791a05 | -4.24454 | -53.66731 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d99e83e-1405-3b68-988d-30fa15271514 | -10.95598 | -44.90793 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d9d3b63-5079-3b88-9c8f-583ce8838d34 | -3.08683 | -54.66308 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f7fc58f-8cb5-3b16-bee4-f15333ea5158 | -4.38952 | -47.75827 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4da3e675-ee3d-3b2c-a288-45b00376bf53 | -6.57474 | -46.75671 | 2024-11-20 04:27:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9371cb-0a7a-36b2-bc59-89a6b1431df6 | -4.94007 | -50.64461 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9aa9d4e1-9200-326e-83d7-cef8cece8b97 | -2.53849 | -54.55528 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05631234-8a39-3c80-986a-a667ec2dd9ae | -5.69966 | -45.84427 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf31423-b6bb-3b20-90ec-bdc2577c865b | -6.23802 | -47.27594 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e86e3fd-1340-3174-aa38-e53c668cdfb2 | -7.17384 | -39.11488 | 2024-11-20 04:27:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ca7f135-bfd2-32e6-a846-46952d287a0d | -5.74027 | -46.41604 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a27c0b1d-64fb-3695-ac69-82326b374716 | -3.24364 | -48.44589 | 2024-11-20 04:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f75419fd-1948-363c-af33-bbf650d1d7e6 | -3.01532 | -51.00673 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2df369ce-2458-3f4a-a0ed-51e3a2bce947 | -9.1755 | -44.72065 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36fdb45d-b9f1-365f-8634-b4d5429a4c3f | -2.58536 | -51.72085 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea988248-9ca4-30a6-ab87-475d9c996926 | -3.18886 | -46.50259 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62983960-f431-3d19-aabb-ade679deb041 | -4.16965 | -46.82052 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b7d4467-d72d-374e-a513-97946107b510 | -2.92563 | -53.07319 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c816c1e7-f1dd-3054-a99c-3f165f507ccc | -6.24028 | -47.30499 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b457cb6-65fb-30b8-8c40-736f5397cc82 | -3.25131 | -46.43056 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ceb903-133f-3e0e-b870-89dc6ee95a70 | -9.19117 | -44.73502 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e839264-5265-3866-b121-6f9eb0c92ea7 | -5.38352 | -45.44971 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df6ce6b9-b8ca-3dea-9e22-232704c7cc8b | -7.00092 | -39.27394 | 2024-11-20 04:27:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb763622-98c0-33fa-a717-8ce3be3003ee | -4.38664 | -47.77655 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6dd74393-0451-3530-8434-fe0b9cf9aaf3 | -6.54429 | -44.18547 | 2024-11-20 04:27:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 405744fc-4cdb-34ba-88b5-12e1e7b30669 | -4.661 | -46.44357 | 2024-11-20 04:27:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a49185c-117a-31a1-aa54-d367b0df169f | -11.1911 | -40.89327 | 2024-11-20 04:27:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4af92a8b-b91f-323f-b398-28befa8cfb6c | -4.12878 | -49.44705 | 2024-11-20 04:27:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14720385-efb9-3230-a702-8aa19e185cd2 | -2.59098 | -51.71333 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b94a2d9-508d-32ae-8abe-1b3879f01501 | -5.20699 | -45.55757 | 2024-11-20 04:27:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38fdc3b0-69a9-3e01-a6af-59ecd3d1d6cb | -10.06982 | -44.02476 | 2024-11-20 04:27:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e71abc1c-4d29-3933-8883-6ed75be4462a | -4.33404 | -50.42529 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e2c42e0-c7fa-350d-aaec-a606c2e016e3 | -9.19174 | -44.73114 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b05a3220-6428-384e-8ec7-09bf42c5ea87 | -5.54356 | -43.90125 | 2024-11-20 04:27:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9af9da2-879b-326f-bf45-fdfeedc787dc | -10.42092 | -44.48974 | 2024-11-20 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d86909c5-c54f-341c-b05e-31d3459ca1ff | -3.77852 | -44.06741 | 2024-11-20 04:27:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0cbef464-0021-33f0-a720-4aa3ec4953f6 | -4.48932 | -46.71427 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36934be8-0676-3db6-8361-720a7abda9f0 | -5.69635 | -45.84377 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a3d7633-64cf-379d-9daf-50b12a7dcd59 | -4.00971 | -43.24921 | 2024-11-20 04:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 793c4876-40c7-32cc-b4c5-24ba6641a36b | -5.3525 | -45.03373 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 460b0439-9b49-31d0-bf3e-a905ae44b094 | -2.53797 | -54.55852 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4055e2dd-4283-3e23-ad11-d3130e4b8ed7 | -6.24189 | -47.27296 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eb19323-21de-3f33-ada2-3475d48acbd5 | -2.58549 | -51.92207 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 112b6248-8e1c-3031-8776-a5c9647918e7 | -6.47947 | -46.07964 | 2024-11-20 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5c2ca09-dd75-30c9-b246-44312243e939 | -3.7262 | -47.37312 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f80ceb12-0302-3084-8466-e3cc50c2ee78 | -4.06692 | -46.84674 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5438defd-740a-3ca4-95fb-f04b760564a3 | -6.00938 | -38.66037 | 2024-11-20 04:27:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 2aa3f5b2-8f90-332b-9ebb-2b4f9e9bc10b | -5.96331 | -48.06488 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3fde926f-019d-3580-a70a-2d81c0bf5b7f | -3.00539 | -51.01637 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb2e3d6d-b8a7-3d10-8e6a-55a2d156f8fd | -5.39364 | -46.1074 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c13037e0-bf47-3fc1-ab27-c9670269fd87 | -5.94916 | -48.06642 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c72cf23-1d04-3809-a12f-cc1049e82602 | -5.97517 | -45.36137 | 2024-11-20 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0c38344-e1aa-3b91-8f7e-4a92eb30d3c1 | -3.62293 | -47.52328 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18f02dfe-8575-32fe-989d-e1961b02c0ba | -3.81745 | -47.80106 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f35a600-6cff-3faa-a333-67f15c73f7f1 | -4.19511 | -46.81015 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d25761ff-05ad-3118-b541-bf2338720f54 | -3.86011 | -44.44449 | 2024-11-20 04:27:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f197da-8c99-3a2b-a3a1-d55ff83cf2cc | -2.5811 | -51.92142 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f32127c-500d-3d90-a1e6-2cf9e1f1f7c3 | -3.72957 | -47.37365 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 782067cd-699b-3879-ad73-89139c9ee9d5 | -5.18325 | -46.1693 | 2024-11-20 04:27:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb5989b3-9be3-31d8-83d0-364a06154d3f | -9.18246 | -44.72173 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05eb2de2-b48e-331a-b03b-feef79a3f5ad | -9.17378 | -44.73227 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28db616c-47d1-3b6b-a583-33bc27162445 | -5.06604 | -44.22588 | 2024-11-20 04:27:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 064ee90c-8f90-3b2b-85b8-d35717e5bb92 | -9.50213 | -43.19123 | 2024-11-20 04:27:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b79891b1-1111-30b6-a480-0ff4141c881d | -5.51145 | -46.44392 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0663e418-d0be-3516-aff5-c2965372af6f | -3.87681 | -46.06247 | 2024-11-20 04:27:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f95844a5-a90a-352c-9ef7-c5d4b6e6da5b | -2.93236 | -53.07158 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acf7efdd-9dbd-3174-bc44-b231861e25cf | -2.92848 | -53.06581 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4de7d812-f3b9-3b49-9f99-3874412b0cb7 | -7.22079 | -45.08672 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2286af9-4568-3afd-b974-f5ca6c80b6a9 | -2.91154 | -53.07047 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 071f0f61-959a-3c49-a1fb-d222ec1909c3 | -2.92802 | -49.43005 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc3a5ace-f2ad-3e2e-ac67-67cf861f3a46 | -3.94686 | -47.004 | 2024-11-20 04:27:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e631e4b-8b78-364c-87b2-5495c6b8ca4c | -6.50961 | -46.03822 | 2024-11-20 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c091bed2-9f99-317a-90b4-62f76b583d0b | -3.88065 | -46.05954 | 2024-11-20 04:27:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dbd10e1-d96c-3934-bcca-898f5653cd1f | -2.95278 | -53.71893 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d727da4-549a-31e6-a77c-18bee900a21c | -5.62488 | -44.83399 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05ec84c3-fd83-3058-abdb-70878b5442ef | -3.13736 | -49.12756 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8f41932-3ae8-3298-bc41-f9c81034c928 | -3.51069 | -53.79597 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8892c92c-c8ee-3870-a992-5face4c82fb4 | -5.54449 | -43.73043 | 2024-11-20 04:27:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 474e5c83-a12f-3aca-9571-16db15379014 | -3.90598 | -45.0881 | 2024-11-20 04:27:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a56e987-b0e7-302e-bae1-a86c47cf119a | -2.89445 | -52.44218 | 2024-11-20 04:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7df863a2-9c57-3830-98bd-d6e0d34b1605 | -2.91745 | -53.07389 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ae62186c-f957-3915-9fcc-960ef32e8a86 | -9.19522 | -44.73167 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae15f24c-e900-3d74-9ce8-c1d6e6474615 | -4.35025 | -45.8837 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c123a58e-068f-3de3-87a9-54238564eefe | -5.69246 | -46.56737 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2486d3f-7955-343f-bd1c-e20848f75432 | -5.44431 | -45.58396 | 2024-11-20 04:27:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19b8b31f-b47a-3005-979d-9f2c3ffdb8b7 | -3.10187 | -53.74557 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2076d65-c8f1-3ee3-bdee-fdae06809aa5 | -9.675 | -46.25249 | 2024-11-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a37f4cd8-01cc-31aa-aa93-1b134d626c46 | -4.08058 | -50.04025 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e43e407-c7b9-3506-94d6-88970e5cf667 | -5.42066 | -44.70288 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6727ee29-65fa-360c-aeb1-2e134e6217df | -6.23038 | -47.00001 | 2024-11-20 04:27:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9bbdd52-34b7-3485-a496-84733d74c1e1 | -4.37391 | -50.73223 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a3f1412-9c5e-3859-9ddb-e0985da95313 | -6.36253 | -55.36477 | 2024-11-20 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README37.md)
