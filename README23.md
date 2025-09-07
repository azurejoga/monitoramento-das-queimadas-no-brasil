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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 630500fb-f388-35ef-9d47-b253cb6da92f | -20.54179 | -46.44843 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d8d0555a-7ac4-3f2a-8165-b15338aeed44 | -20.55089 | -46.44192 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d0b47d85-f648-3cb6-8529-5cde431c9d6c | -16.9743 | -45.8345 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3154035f-85c1-3f10-8f3c-d017c7449bd6 | -21.63265 | -44.01271 | 2025-09-07 03:34:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0d899396-2779-3273-acb2-fb395136dd05 | -20.35401 | -43.88329 | 2025-09-07 03:34:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8825fadb-2671-3177-8cf2-47c3b5c1c999 | -17.67154 | -43.53835 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26f7018d-6937-3e46-9d6d-17e4a31a73b2 | -18.03725 | -47.08964 | 2025-09-07 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08761c57-9af7-3af2-a119-c8cdb0cf8fa6 | -17.52864 | -42.58209 | 2025-09-07 03:34:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 472b46c4-3275-3627-bd42-70606d5c3c5d | -20.40998 | -43.77333 | 2025-09-07 03:34:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ebb14088-39b2-35be-b360-55439b26fa30 | -18.02962 | -47.08685 | 2025-09-07 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa611392-556a-3c6c-a8e6-15b8a3fb959f | -21.2081 | -44.33681 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 321b9739-ed09-302b-9c98-ac7bd800cfac | -19.89624 | -41.44248 | 2025-09-07 03:34:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 59402d9d-a589-3a86-b2c1-be463ebea336 | -19.06518 | -46.77604 | 2025-09-07 03:34:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe5cfbbe-d349-3538-b21e-fcb6c09cfe8f | -17.22731 | -46.70237 | 2025-09-07 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae6f33c5-4de8-3713-b098-5eb3127001f0 | -16.94112 | -45.76086 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20655383-7c55-35a7-9a59-99905a1faf05 | -20.77088 | -44.45966 | 2025-09-07 03:34:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 81bf502b-df87-3af8-9ecd-8c0b9376ceb1 | -20.09939 | -45.31704 | 2025-09-07 03:34:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc5f22e-2313-3139-9f6d-d2d6d211f2e7 | -17.68455 | -43.55172 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60c59970-f400-3976-8415-9cf39bae6cc9 | -19.59703 | -46.11885 | 2025-09-07 03:34:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a90c32f2-8a44-3b4b-82d6-21eba6b403fd | -17.71642 | -44.4889 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d284ea24-0d76-34e8-ad8a-755f2efefea2 | -16.90631 | -45.78043 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1c44856-6db0-38ee-9ad8-5a2849fb3a1b | -20.77026 | -44.46255 | 2025-09-07 03:34:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| af2e6567-aac9-379d-a01a-cc263d00a995 | -21.33974 | -49.12912 | 2025-09-07 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 606d94bb-370c-3ecd-96a5-93726810fafc | -19.07102 | -46.7779 | 2025-09-07 03:34:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2dc08b10-a32c-3983-a457-2945246ad797 | -17.67718 | -43.53627 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dfbdbb3-859a-39ef-b9f8-a2a49fcadefe | -16.90385 | -45.76958 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1941c9be-41f6-3402-915b-6fe12026c40a | -21.4876 | -45.56678 | 2025-09-07 03:34:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 9cc59310-4668-3e8d-bbfb-d1bda8fa4d6f | -18.54214 | -43.82488 | 2025-09-07 03:34:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf54fb1f-e4ab-3a14-883d-5b22d33d1289 | -22.42303 | -47.44064 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 6b118472-f0c7-33d2-98de-04c3062d4b63 | -18.94677 | -43.70156 | 2025-09-07 03:34:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c93855dd-09ee-3b74-b04e-aa99fcc07b22 | -21.42618 | -44.16887 | 2025-09-07 03:34:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bcf4af1d-71e1-34a1-b994-cd95f2968b3a | -19.41222 | -44.31441 | 2025-09-07 03:34:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cba40185-119f-3313-bc73-de6d5f30fdb3 | -22.424 | -47.43639 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5abcb1c7-1281-3668-a990-ed30d0e249ba | -18.37653 | -43.89398 | 2025-09-07 03:34:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f26df0e-c9a1-39f6-98d8-11b23c69b3f7 | -23.42921 | -50.79903 | 2025-09-07 03:36:00 | NOAA-21 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| dc2dc3d5-3b6a-338c-8a29-ce987421ca46 | -12.9482 | -54.7519 | 2025-09-07 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 4015f45e-ed91-3994-8adc-43de402a792f | -13.0542 | -48.0716 | 2025-09-07 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 01010b8e-547e-3970-a260-adfb00a0e9cc | -12.948 | -54.7724 | 2025-09-07 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 292.1 |
| 3257a546-ef3d-35d5-a451-4aadb1c9a381 | -12.9477 | -54.793 | 2025-09-07 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 76536b54-fb8f-339c-b484-e84f879ca21f | -12.8055 | -48.0182 | 2025-09-07 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ca6cb548-1ddf-34ed-a63a-d2840c057101 | -12.9286 | -54.7949 | 2025-09-07 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b811372a-09f7-3d55-bc7f-363829940d86 | -12.9289 | -54.7744 | 2025-09-07 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 3fd8d29d-56ab-394e-bb47-2f7027d30990 | -20.5422 | -46.4408 | 2025-09-07 03:50:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4ec5a446-4fd4-339a-837f-fc77359c7df9 | -12.948 | -54.7724 | 2025-09-07 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 284.5 |
| 508993a1-d975-3bb4-a010-3e980198b9a5 | -12.9477 | -54.793 | 2025-09-07 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 0b5cd5a5-72e0-37ce-9b73-de22535cc1da | -19.8652 | -57.9058 | 2025-09-07 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| d2a5f1e6-bd1d-3547-aefb-00cdcf336774 | -19.8853 | -57.9031 | 2025-09-07 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 5dbde83e-5c41-3f07-9a21-b148c5dd5dbf | -12.9289 | -54.7744 | 2025-09-07 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 229.0 |
| 875e7cf5-a11b-36db-b290-89aa54c1cbd8 | -19.4695 | -47.7691 | 2025-09-07 03:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 8860f2af-3d3c-32bb-bd41-cde2d95668b8 | -5.98874 | -44.14768 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 200c18c9-8884-38ac-81dd-cf83d5bad4fe | -6.23185 | -42.58834 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6d9442a-456c-3f82-ba89-01e72684a774 | -6.19292 | -42.63157 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 45fdde40-82ed-377f-8a81-ac4ad5a986e5 | -5.63385 | -42.624 | 2025-09-07 03:55:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a67692a-08ae-3d9f-942d-4936ccdceb67 | -6.0052 | -44.1549 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02e55240-9e87-3997-a6fc-cadfc288de14 | -5.83383 | -44.12749 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a82441f2-ab87-38b6-b0fc-6b5cbca8fa03 | -2.81604 | -49.19656 | 2025-09-07 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc00aca0-7654-3764-87ea-e1424d71b3fe | -5.98732 | -44.15598 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1f5cd34e-4617-3729-ad11-194052dce962 | -5.42351 | -42.68686 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 192304b7-b1a5-38f9-b4ef-5ee70c2261b1 | -6.20765 | -42.63913 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 09b59042-e8d6-3709-a9b7-4097356deb73 | -5.83518 | -44.11937 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c022680-056e-3ec3-b2c4-1315f0bf5ace | -5.98233 | -44.15929 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6b28a9e-0d5c-34e3-8655-cc4880a1327d | -3.59277 | -47.51016 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 97eda2e8-ed13-3bf8-869b-d5d372109a8c | -5.43771 | -42.81037 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7c37e857-0340-33e9-b61a-4ce658304587 | -5.54945 | -43.05991 | 2025-09-07 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7c3c579-a787-3cbe-86ab-7a78b84f6186 | -3.59646 | -47.52239 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58dd533f-8d83-3bd2-b82b-5a0f2451515f | -4.33702 | -39.35975 | 2025-09-07 03:55:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 490f1949-dd0f-30d2-b88e-18d07105c7a5 | -5.96889 | -43.4146 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 078b712b-c113-3aac-a5f0-fd3d1d117748 | -6.15274 | -43.18184 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a810dc8-39fe-39ad-8018-089a11ef7a4e | -6.1913 | -42.64148 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 85b3e172-af0e-3937-8a57-e2fa34eeb64a | -6.196 | -42.63716 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| abed126a-8a5d-3446-9ebd-7de0cb9dbc07 | -5.75331 | -43.70147 | 2025-09-07 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91e776fa-14ef-391f-bbaa-046f5ac1182d | -5.99161 | -44.15676 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1276d974-d24c-35de-9a97-76712d7f86db | -6.31774 | -42.19891 | 2025-09-07 03:55:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aadf834b-82eb-3289-8d5d-54eaf43ceaf8 | -6.21668 | -42.4626 | 2025-09-07 03:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e34b1530-8a90-38d5-b948-2d1c1c420638 | -6.0002 | -44.15829 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a2f684a-8f06-369a-ac23-1ee67b7f4b29 | -5.75623 | -43.70976 | 2025-09-07 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39a8f97f-0d92-31a0-ba7a-8de0838dd154 | -6.21745 | -42.45789 | 2025-09-07 03:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 676ee686-7e16-3d25-929e-501f9f603fd4 | -2.43215 | -49.30342 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3be5e232-c6d9-3580-b284-d505f40dc043 | -2.82153 | -49.20268 | 2025-09-07 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdd01f0e-c539-372b-909f-8fa4689995fb | -6.22111 | -42.63334 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 64a00176-08fb-31cd-9d81-2e00cc9d507e | -2.42489 | -49.30751 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81d568ef-5722-3e4e-a487-bb5faebd3dbd | -2.42626 | -49.30263 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc629a3e-2c6e-3c76-b0b3-40a1a0b1ca67 | -6.15333 | -43.17836 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f13ea40-6aac-3c68-a686-2d3c18b4051c | -5.98592 | -44.16417 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d087da0d-6d07-3b3e-ad8c-462c54f4f489 | -6.20228 | -42.62314 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aa7f143e-ee34-347f-93bf-7a739fd7378b | -6.20375 | -42.63857 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 21b2987d-a108-3675-a554-53b6a218d09b | -6.18741 | -42.64086 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d06564c-f57d-33fb-b99f-c7f4e6c9efd4 | -5.99022 | -44.16496 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 850cdb10-83f6-3458-94f0-1a0192cd8734 | -5.44103 | -42.80413 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4dfc5999-19ad-3d2c-bbb7-592b44e81ecb | -2.43087 | -49.31421 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 89c5f287-f0f2-3eac-a4a8-2f4bee0a5a72 | -5.45759 | -42.81352 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e630b235-5fdc-37c6-bad1-1f1a2d942305 | -5.97803 | -44.15856 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63faee67-9615-3300-b7ab-b00d55a16ff4 | -5.53615 | -43.09 | 2025-09-07 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f26d96b1-eca9-31cf-9824-65ddcc54f4f4 | -5.32704 | -42.68953 | 2025-09-07 03:55:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 92e94ce2-a86b-3bbb-aa83-1e10a08a100a | -4.25665 | -48.54944 | 2025-09-07 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5f2f6d0-3131-3258-8f31-18cc59fc164a | -5.95895 | -43.81441 | 2025-09-07 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86866832-9210-3230-b78f-79b32b1ec019 | -5.9973 | -44.14933 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0b545f2f-d097-3959-b627-e980175fbff4 | -5.86357 | -42.42199 | 2025-09-07 03:55:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c852875e-8990-30e6-ad5b-67a8d917638f | -5.98444 | -44.14693 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20939c9e-6d15-3898-af88-b4f6243204e2 | -3.88214 | -43.16298 | 2025-09-07 03:55:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README24.md)
