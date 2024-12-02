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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2be45119-a333-3e53-b99d-a7eed451c6e8 | -4.34812 | -45.75723 | 2024-12-02 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6683a611-f56f-3545-bbdd-994c9046a352 | -5.57962 | -45.14516 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 47c0398b-6380-35cf-b0a8-a77ff5e0bf50 | -6.92125 | -43.53648 | 2024-12-02 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adac5011-2dca-312e-bb60-4959e35027df | -4.57541 | -43.3582 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 08a1ded6-2c39-308b-814b-ca7922c22759 | -2.92102 | -40.44464 | 2024-12-02 04:01:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| b3818e0a-d542-3915-9401-76233cf9ce97 | -3.53848 | -51.02841 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d74c49a7-c19c-346b-8b20-071c8ec85c7a | -3.33786 | -51.5249 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a826127-05dc-3e85-8931-32ec3e8aaca9 | -3.54552 | -51.02459 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0e84427-8a5f-3852-a3dc-be1d3290303f | -2.69027 | -48.85659 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26c3dcb6-2822-3a12-b485-b00ff335b71b | -2.28608 | -45.74834 | 2024-12-02 04:01:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96ad3165-863c-3510-a3d0-de8cb5b39688 | -5.91336 | -45.5813 | 2024-12-02 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fbb6448-54aa-388b-9e36-b2a7258bfa2a | -3.15314 | -51.11615 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fd5f787-6079-354d-81ad-1c25288128aa | -3.75065 | -52.26953 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6651703-948a-3820-b96f-e1494a7d9ff3 | -3.36439 | -53.21436 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 566c18d4-b41d-3d88-99b7-b6095ca98afa | -4.05169 | -46.81534 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e273be8-d5b6-3be0-9825-80be882ab33a | -4.55345 | -45.72071 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e860b9ae-8a0b-3a6e-8ce0-6ed17cf1ded8 | -1.81413 | -46.63781 | 2024-12-02 04:01:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6181ae59-92cd-34a0-9c59-172b9575bf57 | -3.04473 | -49.37932 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0558f6cb-c799-3b58-bc75-cba1f37d0fc6 | -4.01575 | -47.00292 | 2024-12-02 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d103309d-c40e-34ef-a93f-c84a8d6f1c57 | -4.99841 | -41.31888 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a48329c2-3b15-33f8-82b9-4fceb611f3b8 | -3.05495 | -51.06399 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0d4a470-c644-34ac-b4ff-40fb48a448b2 | -3.74397 | -52.2685 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f702c244-041e-3132-99b7-913ee7ebd834 | -4.19259 | -50.68283 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45b4f69d-f6f2-3026-9b1a-6114019cd430 | -6.81863 | -46.7742 | 2024-12-02 04:01:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55d572ff-defd-37ad-a73c-4acb6c93aebf | -3.13285 | -45.98367 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41dbb5b-a8eb-348e-a136-e70b25306451 | -3.48488 | -46.08865 | 2024-12-02 04:01:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9f62ad4-a3fc-3da3-b2b3-4047f0b815c4 | -3.53875 | -51.49542 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c400831-a468-34db-a0bb-6e0d22a3dfcb | -0.92799 | -47.62107 | 2024-12-02 04:01:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 777cf6bf-8713-348b-9f8f-2e20b897e3d6 | -2.74522 | -51.75341 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46900b6d-93ca-3935-839e-583919796fb0 | -3.28343 | -50.55965 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f126a11-5eb2-3714-91a7-9cdb2c6da19d | -3.61709 | -42.74294 | 2024-12-02 04:01:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6150c852-e471-3123-8c0c-2a05ededf165 | -3.54253 | -51.49967 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae792e1a-d8b9-32b1-8e17-17ef3d86c50b | -3.07167 | -50.99068 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba8d4761-9bf2-35cd-86d9-1dc54d8a53eb | -4.90902 | -41.33794 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d939018b-6e86-3689-8d1d-95b60aa35e14 | -4.40872 | -47.57127 | 2024-12-02 04:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc7981e-a275-3b1c-94c6-dfea1aa6b28b | -2.90159 | -51.58122 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 996eb8bd-5594-3e4d-a753-363353e4aef7 | -3.64941 | -51.11886 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d92467c-1341-313b-95e5-491cd96c41ca | -4.47269 | -50.76921 | 2024-12-02 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9daa851a-73bf-3c7d-a75e-fada6494d6ab | -3.19762 | -46.59857 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343ddbfc-484c-39d0-92b6-51db97cbbda7 | -3.38748 | -51.14793 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26b4d09b-a359-3fca-aa61-48048217df55 | -5.5824 | -45.20487 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a4dda02-bac9-3905-95c6-44700a62b39d | -4.55137 | -43.30234 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54c940b7-8b8c-3c1f-9d0d-34ea708db12a | -4.05043 | -46.99819 | 2024-12-02 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9aa079a-9c16-3811-98dd-5823bf441f9a | -3.47487 | -47.68591 | 2024-12-02 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f23f70c3-4dfb-3d3e-b566-a7a0efdf356d | -4.91913 | -41.33957 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e0ff063e-939a-3d38-b3b7-c98970250bd0 | -4.75581 | -41.12708 | 2024-12-02 04:01:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 891607a7-c77a-3e97-bab5-e447c6aaf84e | -3.61775 | -42.73878 | 2024-12-02 04:01:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6242e31-7f20-323c-910e-dbe265f4d8cc | -3.85275 | -46.53837 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7c278779-98e7-34c3-8813-e592821a5b2b | -4.05553 | -46.82105 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 741b276c-54b3-3249-b66b-7587c15b3bfb | -4.92367 | -48.42536 | 2024-12-02 04:01:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d91b81-83e4-3973-adb7-85d4bfa07a32 | -4.90958 | -41.3344 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 200120d2-3f00-3598-a8e9-bebf2191296b | -4.95389 | -42.79922 | 2024-12-02 04:01:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 23830a25-acc9-3330-8596-cf2f7458f0f8 | -4.11126 | -46.76517 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70f45793-41fe-3b63-a314-f3fbf8516bcf | -3.37148 | -53.21548 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f14a37c-b258-34b8-a4b0-eebb2c9f7ca0 | -2.50705 | -46.10434 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 006b6d07-6cbc-30f7-b2a5-74c99644851b | -4.86368 | -41.2646 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f1d63849-b312-3938-8161-e76c9cf65913 | -1.73298 | -52.64234 | 2024-12-02 04:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae465f11-f20e-3b72-9b5e-29fd60825c06 | -3.15662 | -51.11859 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4112076c-8851-3a0c-aba8-2f53c16f1f35 | -1.99468 | -46.45613 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 674bbe3a-3205-3281-b51f-25e82cd7dd48 | -2.47848 | -46.57009 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb58cd6c-d66c-366d-869d-6712bdb2d8d7 | -3.63163 | -40.85951 | 2024-12-02 04:01:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 47c92ed5-f294-3c8e-890a-f7ec79217671 | -6.0855 | -48.05543 | 2024-12-02 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c182deeb-2754-3874-b8b8-2335d76c5a69 | -5.009 | -44.17273 | 2024-12-02 04:01:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 992ec643-b77e-39f4-93aa-c418675780d0 | -3.36798 | -53.2115 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8d6b5aee-b0ff-38b0-b392-a677aa43d713 | -3.78013 | -52.03223 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fc7e9772-ce84-34d8-aed3-451be995b804 | -1.47534 | -47.33939 | 2024-12-02 04:01:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee959ab8-f6b9-3391-81ea-f646605fe710 | -3.28531 | -46.15189 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bdf9d1c-0cc1-31cd-9628-82ba85f5e670 | -5.12866 | -43.20773 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| cf20b301-91e9-31b6-bcca-005b8c86ddca | -3.45536 | -44.92959 | 2024-12-02 04:01:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9049eefe-2611-38a5-9c35-191011a3b998 | -2.48237 | -46.57585 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14ce0334-8d30-37fd-97f9-488a42d3f81a | -4.84615 | -41.3319 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 48abacb9-1f0d-3e45-a505-fce179932b31 | -2.68969 | -48.86015 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 655dcdb2-16c2-3305-8c6f-7ba4c64f9702 | -5.57989 | -45.14537 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6cd31c80-8d3d-3059-b12b-4d2e79fc9a45 | -4.09449 | -44.85456 | 2024-12-02 04:01:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2bcda88-49af-31b3-97cd-b52ab522c843 | -3.10101 | -53.23145 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34ae4306-4099-355f-a627-5ad783ec4b49 | -4.90621 | -41.33386 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8ef41423-c8f0-3976-9206-5a35b08a487a | -1.80988 | -48.77182 | 2024-12-02 04:01:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520984d0-0ea7-3cee-bed6-45a65f040299 | -2.5875 | -46.00917 | 2024-12-02 04:01:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcef5233-494f-3ee8-b3a3-f0b1293defc9 | -5.58049 | -45.1418 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f98f0d8-f1c9-3ecf-b7c1-96d2026aab04 | -5.58739 | -45.1503 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e4158e8a-ed81-34ce-b320-0e3f237cd58e | -4.82952 | -43.65037 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04af4b5b-83a4-30ad-b148-39bcdf7905ae | -4.752 | -38.47231 | 2024-12-02 04:01:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4a8aecd5-7db6-3ae0-a8de-f49e5efab0b6 | -1.9579 | -46.44524 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82acb6ed-26c9-3cc3-9f91-1e97120a2d67 | -5.12569 | -43.20296 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 75bddb75-52f7-3bc1-9b30-e312cba92bab | -6.36764 | -47.35674 | 2024-12-02 04:01:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 573d0799-7b65-3a14-8738-56760231e9cd | -3.29771 | -45.66018 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd84ead5-1461-3143-bee4-054638e7f0e1 | -2.63471 | -46.88019 | 2024-12-02 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4ce8225-9184-3742-b9ca-c21276c10782 | -4.74965 | -43.71637 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cbe93c5-cb8b-36e6-9aa2-2407bababe5e | -2.47459 | -46.56434 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10648ec1-4b04-33d5-805f-061050df3b5d | 0.88801 | -50.95675 | 2024-12-02 04:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52f09f36-c9ed-3825-b096-f4551edb7adc | -5.58647 | -45.20553 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc54e17b-20a9-3233-b2a5-b736306afecd | -3.70706 | -51.8317 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5d7b9dfc-c4fe-3b82-a3aa-4bf8ab47140e | -3.3047 | -46.40762 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| accbb0a1-c3bf-3c06-a220-26462f0a216f | -4.19632 | -50.68494 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f59bef46-0ea6-37c1-9510-0ecd4eaf0cc2 | -2.95541 | -39.96499 | 2024-12-02 04:01:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4073fe3a-8547-31ba-bd1e-6f00db2db197 | -4.90118 | -41.32206 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 186b2776-701e-36ba-ae51-f7e531d42bb6 | -3.13661 | -45.98878 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 446fbc67-edfd-3603-8669-96a7d7c3afa1 | -4.90171 | -41.34039 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e2ad335-47d9-32be-aa86-2080dd5dec4a | -4.56447 | -45.47048 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 142c79fd-e3f1-3b87-b346-fe313508fd72 | -2.79529 | -51.89674 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README25.md)
