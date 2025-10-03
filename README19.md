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
| f1c175c1-cc5d-350e-9146-a6bbc37b80df | -4.99172 | -38.85862 | 2025-10-03 03:42:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 25b0e093-4dcd-3621-a406-f83e07793348 | -6.80001 | -44.75031 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6c81ca2-04cc-32d2-9d1e-b334185e1fe1 | -5.54401 | -44.648 | 2025-10-03 03:42:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6e0f42ec-3415-35fc-a6b6-e871cc0b9077 | -7.75778 | -42.59348 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 41b993e6-ad43-375d-9b63-6d1923b01edf | -5.78285 | -45.76073 | 2025-10-03 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffe2fbec-eeb2-3373-b8d1-c0f4e28cee4d | -6.86912 | -39.28086 | 2025-10-03 03:42:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e32eb8c6-cc4f-31dc-8f0f-9d8928ac8b67 | -4.66789 | -45.80548 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| eb55a9f6-e768-3f31-b81a-7ec2826ee5d5 | -5.47324 | -44.69387 | 2025-10-03 03:42:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 484d5661-09cc-38c2-afd5-f4bd52c8d587 | -6.04809 | -44.61959 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6cfd3c1a-b86d-3e7e-a73e-e7f885492dfc | -6.05805 | -44.63611 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7db18a27-6a60-33cc-96a5-c4e304a4cd4f | -3.09106 | -47.02462 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6b0c0895-423a-3be1-9e23-7ab84d95ef62 | -5.74165 | -44.26449 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bd8454e-1398-3289-9771-99112e78efc9 | -7.77322 | -42.58626 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 84997428-3acc-3512-a14f-30487f9b3069 | -6.27186 | -44.04887 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bab54d6-084c-37b8-9fe2-d475217da103 | -6.55044 | -43.87909 | 2025-10-03 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd4bff10-a4f4-3f6d-9f67-65023fa53922 | -6.19562 | -44.62819 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b43fe21-3aee-38bf-a660-128a417904e0 | -6.72098 | -45.96809 | 2025-10-03 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 037658b1-0ab5-39c4-a986-f045512b8669 | -5.34784 | -43.759 | 2025-10-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2ab9c7b-f999-33b0-8245-df783e4f4952 | -7.77476 | -42.52345 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fcc0689c-2295-3653-a000-a3b8b4ed4a6a | -6.97318 | -44.39161 | 2025-10-03 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef545c2f-aba4-3d0d-8762-a9221dff5fed | -4.67095 | -45.78837 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 89c24ea3-2658-3dca-9f1c-34a646fb52fb | -6.05293 | -44.62388 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f883c48-83cf-37ce-9f42-a53564882855 | -6.23139 | -44.24598 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de392fff-3c29-3e76-98c8-2dfceade105d | -7.00315 | -47.18066 | 2025-10-03 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70dca510-4231-36f6-bbd0-9f791e4a45e2 | -6.27048 | -44.04965 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a22ec59-f025-30a7-b7af-1a25d52cb792 | -7.7516 | -46.25932 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 02a32425-dd71-32da-9333-9df8746ff0b5 | -4.65985 | -45.79993 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| b2504eb1-7469-3e06-ae8a-dd97472af4bf | -5.40549 | -41.3274 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 81181047-72cb-3c7b-9a9c-35fa3dd0a651 | -7.71573 | -46.19643 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8404e65-f964-39f3-bd68-e60fa96f89ae | -6.6586 | -42.7849 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d4571eb7-900c-3cec-9f78-aab8e0581a4e | -6.24394 | -45.35179 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cc476e13-e1ff-330e-89b3-26695bda49e1 | -7.74314 | -42.59604 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 522c4588-daa4-3a0b-ae44-190ad1784b3a | -7.74571 | -46.25841 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfff4208-d0c4-3f83-b19e-83a0888c9825 | -3.84452 | -41.58782 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d7477a19-d91d-3d10-89eb-e2fd66b9bac5 | -3.09418 | -47.01792 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4587048f-89e4-3052-9e68-53dd8c776fae | -7.75526 | -42.55405 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 78ff9413-d585-3454-9492-c7f58033fbcf | -7.75889 | -46.2526 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 03b1e6e6-5865-3a67-ba79-6733ebd93bf9 | -6.13825 | -39.766 | 2025-10-03 03:42:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| acd66445-9baa-36ea-af6d-a2e4668b53cd | -6.34961 | -43.40648 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe7bdfe5-f2c4-3247-aa68-67170789274d | -6.05167 | -44.63115 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70b39ffd-340e-3e46-af90-ae20dcf7a22e | -4.6538 | -45.79934 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| a19a3068-3a6f-3b3c-84b2-0d5406423d83 | -6.23966 | -44.22847 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cec79f2-695e-3857-a2ea-06bfa4577fbc | -7.78112 | -42.568 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f8dcb13e-64e2-3ab7-95e6-2c8b3d9c5b94 | -5.3165 | -45.28133 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 729e3a41-3fe2-3ab4-98cd-cefdd9ba4284 | -5.40701 | -41.34533 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a3ad37c3-0732-3345-ae46-dc7be4637ecf | -4.5748 | -46.50441 | 2025-10-03 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 215bf273-bcaa-32ff-a036-c1b05b4379fb | -7.74859 | -42.59196 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9f848ad-8ac9-3878-a297-73f9f81d49ce | -7.79519 | -42.54124 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c7aeffc8-3994-3bc3-bbe5-3027ea82db9d | -7.42541 | -40.07382 | 2025-10-03 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b984597-5a49-33d5-b42b-a04cb93414a5 | -6.68198 | -42.81936 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ef800d85-20e3-3536-8b03-904749039d5c | -6.68974 | -42.83123 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 41798314-b17f-366f-893c-ed764888524f | -6.64737 | -43.59315 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11e216ca-9059-3cca-94c9-f050adf2af9b | -8.48465 | -44.59359 | 2025-10-03 03:42:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7303c97f-c10b-327c-ae0f-aa141538c9e6 | -7.71302 | -46.20705 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 75aea4ab-b254-3ede-beaf-b3032be6f15f | -6.37598 | -43.8806 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2ce3c15-7f90-3e20-837d-03f339f53948 | -7.75524 | -46.23969 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 86d1d716-5993-32f4-848d-5281c04cb331 | -7.74654 | -42.57677 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2135be3d-38bc-3fa8-9126-200949d0d236 | -5.39975 | -41.33489 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab848d0b-e6b9-30de-815a-9434c5eaaac5 | -6.65385 | -42.78421 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f74d45ea-58d2-3105-89ab-24588722c2e2 | -6.23606 | -44.2504 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 761ffcc9-4230-3beb-8970-13b0969cc86d | -6.06125 | -44.61839 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad7da7e0-ece4-35a3-81bb-070cc0388cf1 | -6.64293 | -41.27166 | 2025-10-03 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e1447a16-24d2-3bc1-b0f8-4ca7015f9e01 | -7.7508 | -46.26363 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 343d3c25-f4a8-3e76-9bf1-aaf97eaf6e10 | -7.90275 | -43.52972 | 2025-10-03 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 269b50d1-f69a-37b8-83d3-cfa1f67768df | -7.28696 | -45.26175 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6f7d7b3-073e-3b5c-924e-8758b09d6a9e | -6.34925 | -43.43835 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f47dba65-83ed-3fb8-b138-0d43c5d86774 | -6.37652 | -43.87751 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d103d3b-7f37-3e03-b6c5-1779123ef447 | -7.81158 | -37.59066 | 2025-10-03 03:42:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15b2d633-dd1f-350b-8a10-b86dfdb70c1f | -6.68024 | -42.82957 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c4317778-37cb-3bc8-8f38-b3e6f715ea94 | -7.77864 | -42.58225 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 61895e27-07cb-3cf6-a3bf-8561bb96f573 | -7.80218 | -46.01826 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 102fe712-dcac-388b-b514-fb0de9d4ac3a | -7.75588 | -46.23622 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cfdca58e-79ee-3d8c-8e0b-456e668b02bd | -7.74919 | -46.27227 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4bcb07a2-404c-3cb9-b675-b0a3316b1958 | -6.28546 | -44.05594 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06aa3fe5-fdae-3682-8608-a56f1445fedd | -6.27762 | -44.04662 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 232395f3-63a8-3292-9d78-4f438e13c91b | -4.67395 | -45.8061 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e1ece03-741f-3efc-af6b-b6548a526a01 | -4.65832 | -45.80887 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f5494f8b-99ce-325d-9632-8a3d3df065ae | -6.531 | -43.37471 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d27da066-8787-37e0-9cdf-8729a6dd40a7 | -4.66632 | -45.81427 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6734933f-3e54-3d03-90a7-3ab7df9f7770 | -4.66564 | -45.78366 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 685d44ef-cc9e-33e5-a674-70e98ff9cb44 | -5.34731 | -43.76217 | 2025-10-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bc4742c-e9a4-308e-a649-9842c1e8a4fb | -7.75588 | -46.26886 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 1c91690d-ae15-30ba-b0b0-a06e0fca9565 | -6.23197 | -44.2426 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d479b05c-9528-3204-8ff7-46855ecb0b27 | -6.87575 | -44.51388 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9a64b75-9455-310a-a498-1a60f68abcdd | -4.76442 | -45.33125 | 2025-10-03 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2012e47f-5282-38b0-ab3f-424ea250084c | -5.17835 | -45.425 | 2025-10-03 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43defbd7-103b-37f0-8034-606c941e1f77 | -6.09243 | -43.25933 | 2025-10-03 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52b7c34a-3174-3fb5-a3ef-cd5377834e0c | -7.72034 | -46.20025 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 059cdb3f-aba3-3569-9bc5-f4e12a92f2af | -8.6096 | -39.07882 | 2025-10-03 03:42:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b30180e3-35c3-3006-9de8-aca37f27e791 | -6.68797 | -42.8416 | 2025-10-03 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| de5f6ecc-ee54-383c-95d7-668342da81ee | -7.90664 | -43.53612 | 2025-10-03 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c2e449b7-2c0e-3819-9624-8d2fa751bbee | -6.05776 | -44.62827 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a034b8d8-9b05-30bd-9355-9b036b9179c9 | -7.79681 | -42.53189 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 276f32e3-9c03-34ac-a416-d6046a96fda2 | -4.67021 | -45.79253 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 72a03c13-c2f3-3ba5-bdea-1eed3cfc3f3b | -7.79085 | -47.37313 | 2025-10-03 03:42:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0381c3e-ca15-3639-b818-0aa9f32e484e | -5.6356 | -43.90979 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 808c4b6f-9ea7-3a0c-8209-9dcc1c537615 | -4.76426 | -45.33051 | 2025-10-03 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 750ed33e-eeb8-32bd-9fde-bae2a316a96f | -6.04992 | -44.60907 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| b7268b1f-c579-3125-8119-09b68c72c160 | -6.35913 | -44.75698 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7b67fed-2d30-3c59-9e0f-2315e822bdd5 | -6.04983 | -44.64184 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
