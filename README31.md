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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ef22305-2d75-382b-9ba7-9da1089d25f3 | -28.7132 | -55.64339 | 2025-08-31 04:08:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 58aefbd5-b911-3360-9c90-b0392a2099be | -28.71086 | -55.60304 | 2025-08-31 04:08:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| e109d967-c915-3404-9bbe-74037eca19f4 | -28.71165 | -55.59961 | 2025-08-31 04:08:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| a5a8f7d6-6220-3449-9b3c-6f1cef7eb53b | -28.31191 | -55.21389 | 2025-08-31 04:08:00 | NOAA-21 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 4d7ca213-2a1f-3764-8986-ee73899852f1 | -28.71125 | -55.64833 | 2025-08-31 04:08:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 6ec7573b-3913-368a-abb1-a2ca12e38d1f | -28.71235 | -55.64693 | 2025-08-31 04:08:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 830aaea5-55e9-37ac-9173-89b4b1f1afdc | -28.71208 | -55.64478 | 2025-08-31 04:08:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 4dc38de6-11e5-3430-b366-b535109f0eb7 | -28.53068 | -51.04737 | 2025-08-31 04:08:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2f6c9bd3-42c9-3ad2-9a5f-1d1eec7cb6ce | -30.20103 | -53.61865 | 2025-08-31 04:08:00 | NOAA-21 | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| b791ac73-1225-3446-a94a-6558e83f2189 | -28.7129 | -55.64122 | 2025-08-31 04:08:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 707fd50e-b240-3566-8a40-e2a2ae0c1464 | -28.90662 | -51.79464 | 2025-08-31 04:08:00 | NOAA-21 | FAGUNDES VARELA | RIO GRANDE DO SUL | Brasil | 4307864 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3ae9a0f4-1cff-33af-8f83-b531ca7c451e | -28.31269 | -55.21057 | 2025-08-31 04:08:00 | NOAA-21 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| ba628f20-0af1-3cec-bb51-c2fff4ef3788 | -24.99848 | -53.47001 | 2025-08-31 04:08:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6f89bafa-2799-37b9-85c2-a594fae6aec6 | -8.6539 | -61.9457 | 2025-08-31 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| fb5c53b5-cc07-3a0a-8980-1d35b5bddb3a | -6.1665 | -43.3273 | 2025-08-31 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2b21da24-4f18-3b27-b279-29ce92d59ba6 | -9.0614 | -65.4355 | 2025-08-31 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 824e0138-9222-3938-bcab-30f05f170331 | -6.7093 | -51.4165 | 2025-08-31 04:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 93db17ce-9e79-3d7d-ae77-04236f1c9c57 | -8.6538 | -61.9647 | 2025-08-31 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e1099c67-affe-3053-95bb-447c83e4e13e | -10.4605 | -64.5397 | 2025-08-31 04:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| b6218332-7ace-3cbf-983b-728566f3f1d8 | -9.0614 | -65.4355 | 2025-08-31 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a837cc37-8891-3281-8cd0-f1d9c1663929 | -10.4605 | -64.5397 | 2025-08-31 04:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1566e7ed-3b9d-386a-b971-c13006d46353 | -7.0951 | -44.3128 | 2025-08-31 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| f3f444aa-3a83-3f0e-a1e1-32b81ee48e3d | -8.6539 | -61.9457 | 2025-08-31 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 835fa36a-ed2b-3b22-af4f-ebe8f3a39950 | -9.4432 | -60.5692 | 2025-08-31 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bbeb4b74-f236-3fe8-8830-3af5fcc1c530 | -6.7093 | -51.4165 | 2025-08-31 04:20:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a6109c73-7605-3d86-b7a3-fa145418e62d | -6.1665 | -43.3273 | 2025-08-31 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e4c34e48-aaab-30fe-87e5-04183a0a05f9 | -9.4495 | -62.3675 | 2025-08-31 04:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4f98a4fe-f22e-37b1-a54a-1fc8dc7b02b6 | -6.36012 | -43.56132 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26466c1d-0741-3341-9e02-d175672441b6 | -8.4979 | -44.74633 | 2025-08-31 04:27:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cff1b01f-b88c-3e03-bc12-8c7ec56e94fe | -6.77276 | -43.76104 | 2025-08-31 04:27:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f93e4c0-81c9-390e-8be6-b4350784b8dd | -7.21234 | -45.42655 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8715906b-a517-3c6a-bd7a-0047101c69d8 | -4.07397 | -47.95956 | 2025-08-31 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8266b10-7e34-30f8-b633-28a11ddad9cb | -7.19755 | -43.71312 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c444e14e-49be-384e-8359-6df1d3a1ee47 | -7.74344 | -50.26289 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f06fc8e-6a8d-3f5f-a635-dbf94223c079 | -5.82011 | -42.49156 | 2025-08-31 04:27:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 693f8527-4cfe-34ba-891c-4bab19119214 | -6.22018 | -42.77063 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb3a4b0a-2e39-3dd6-87cc-5cba1dca7ea7 | -7.77123 | -45.45485 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da1bd925-ca36-3fcf-aecc-1851fa3832b5 | -7.43817 | -50.25979 | 2025-08-31 04:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccd18319-a2ed-3d95-b3f6-8d38c9c3bfb5 | -7.19673 | -45.43857 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb2940b1-a13a-3f01-90c1-4351c0157817 | -6.95729 | -42.0074 | 2025-08-31 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ca7c25d5-c18c-3bce-8f6e-2ad366dd38a0 | -6.33103 | -42.52822 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f7b5ad1b-7753-3954-acab-7c13a2452a33 | -5.58889 | -46.32468 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21c6291b-1ab4-37aa-8b84-8af312bc6a5f | -6.2384 | -41.82102 | 2025-08-31 04:27:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecd06e0b-595a-30d0-bc0c-bf95cc5b6292 | -7.10633 | -44.31215 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f3e32c80-4e61-3fbd-8104-bd67a3111b04 | -6.64729 | -43.94556 | 2025-08-31 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80b9acd6-ee17-3795-9709-2e5752139671 | -6.98532 | -44.11979 | 2025-08-31 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32cf039f-7ff0-382e-89e0-fc5ab828a28e | -8.88657 | -45.09649 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2020c05-e480-3d8f-9529-ab4581152afb | -7.45924 | -49.59845 | 2025-08-31 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2de48ff7-2ef8-36da-8ee6-cc258f2bde75 | -6.18637 | -44.13021 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ff4f381-519f-3660-b4c5-f2911328f5be | -4.91843 | -42.09011 | 2025-08-31 04:27:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 74552da7-d083-36ce-a1f1-acc5bb06cee3 | -4.41963 | -47.60704 | 2025-08-31 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f3d34d-c59b-3dac-a55f-22337b1b6276 | -7.96129 | -46.38389 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9c7e123-53b3-3e81-b28d-a42d55edcd2f | -6.57475 | -43.68918 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9f27109-7d5b-3171-b947-7e28cb924fa5 | -5.96332 | -44.26459 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf8e7403-10a8-30bf-9f5d-d63e08dd0a11 | -6.50559 | -43.55491 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a002707-ef2a-3f17-ba20-82b84f6746f0 | -6.56653 | -43.6722 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0aef5bde-9f96-3153-bfa7-b32f701c9922 | -6.96299 | -44.31394 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62297997-59f9-378d-9495-29cac19ba8ec | -6.15819 | -44.12989 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 444a42b4-5870-32a4-a61e-0b123efcb6f0 | -6.50861 | -45.42524 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73b2c4b6-3bc2-3c8c-ad5a-d72f5422d509 | -7.71269 | -50.2815 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 798ea010-2b9c-3772-b4da-d32cf189c75d | -7.20119 | -45.43203 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70c0b751-e895-3f53-93ac-23cecc92ca4d | -7.08218 | -44.33154 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1dad8e7c-5a87-3210-832c-04d46d5ef34b | -6.27695 | -43.54226 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1cad107-ab01-38df-b726-9ada45f22192 | -6.16969 | -44.1697 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93fe8582-dff4-3810-9c58-8f1d059db300 | -6.27301 | -43.85121 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ca2d406-1ab9-303a-b4fd-4393ea1c0185 | -6.63721 | -44.25401 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b037e462-2c94-3e52-8e47-220e6ee5151b | -6.48964 | -43.56443 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac199be5-5b24-305b-8f54-3057c86492d0 | -7.32687 | -44.09612 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53f984e7-3c06-39f8-a680-c6365fdd7323 | -8.46086 | -43.62761 | 2025-08-31 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc28c9c7-605b-32a3-8b13-d7e72c5f1bcf | -6.16541 | -43.32545 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 3e555d7b-9126-3aaa-9e9b-450aa8d64eb8 | -5.73487 | -49.14001 | 2025-08-31 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd6af264-950d-3774-8f23-5ad71961f7ef | -6.28402 | -43.54329 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 616aff72-78f2-37b3-a0a0-b94cb29da473 | -8.11959 | -45.00354 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 003e9766-a3e8-3e65-81a4-1f9eb5d9c198 | -6.42751 | -43.96873 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9b381b7-0a45-3040-b710-8ef69637a0f8 | -6.33914 | -53.43718 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11ba37bc-12de-3ec7-9d6a-904320621d81 | -7.58547 | -45.12247 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39c1220f-e140-3b97-a5ae-49b1d133538e | -7.40493 | -49.51764 | 2025-08-31 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b1fd88a-4bd7-3e8d-8422-516cce92ee20 | -7.7276 | -50.26103 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 939e8539-b192-35f1-99aa-2630a7ee97a7 | -3.20948 | -52.24982 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50a03a8e-ba75-3db9-9fa0-4cb8d35724b1 | -6.0996 | -43.33723 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3c40ccd-2558-34e9-8d9b-4b834a115f54 | -6.80677 | -44.31438 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d50b860-f228-388e-8fc4-09f629eebdd3 | -6.3117 | -43.61887 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8b5869c-9b64-3fa5-a8a4-6d682c22183b | -8.83748 | -47.49184 | 2025-08-31 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54ff45cb-376e-304d-9811-313df9e28d3d | -3.59195 | -47.52088 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90e5b4e6-a553-3dc5-b697-6ee446097e3e | -7.33036 | -44.09666 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66c83a95-ad4b-35b6-a8a5-2dbf59dd773a | -7.10173 | -44.31913 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 6c2dbcf3-bcd3-38a7-9053-482ec233b32f | -4.55445 | -50.47688 | 2025-08-31 04:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f067597d-b053-3e6a-bffd-5fe7ba902b34 | -7.95355 | -46.38981 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2d7b3d0-9c92-3eff-9f7c-f882c8db1f3a | -6.94642 | -45.6982 | 2025-08-31 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b7a468e-695b-337e-8267-39a2042d660c | -6.28048 | -43.54279 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcfe72b3-ca2f-3041-90c9-01d5edff18c3 | -5.69847 | -45.95482 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27719557-1fa9-3c2c-b80b-b09b5d0ce3d3 | -6.33036 | -42.5326 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11da1f01-ffaa-30e6-834c-07c4b110f4c4 | -6.24057 | -41.80671 | 2025-08-31 04:27:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0a04af2-af27-39fe-b1b6-eba14db48906 | -3.98484 | -47.88329 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52f3afe9-b36e-3820-a825-ccc2d34c3a6b | -6.33326 | -53.4342 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99c1e74d-8c65-3682-b81c-e6df02868b2e | -7.21618 | -43.63806 | 2025-08-31 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b0b3fd5-59bb-3268-9a83-fdcbd6d429e8 | -6.19279 | -42.75347 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd32f4c7-521d-34c0-b8f6-56b9193b8233 | -6.69593 | -44.05387 | 2025-08-31 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed8c0bc0-9356-345e-97aa-6b0336509d76 | -6.83379 | -43.33627 | 2025-08-31 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd4c3f69-aba1-33e2-8efd-b4e8f81f5a2e | -9.25393 | -47.0657 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README32.md)
