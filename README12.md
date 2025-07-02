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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bd656f2-d193-379f-9172-b09ab8cff1ff | -16.06687 | -51.56124 | 2025-07-02 04:29:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 573d45db-661b-3429-9962-fbd4ab203c6f | -19.52078 | -43.59376 | 2025-07-02 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08da7fe2-b946-3535-bf51-599d47bf36f7 | -15.93992 | -50.06151 | 2025-07-02 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef14942b-b66b-3494-8c39-041779a071db | -19.2207 | -55.37574 | 2025-07-02 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4539c642-65de-3954-aae3-e697cf0b5e2f | -19.52031 | -43.5975 | 2025-07-02 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f94df34-dffe-3005-bc4e-ab78d6614014 | -19.16132 | -54.83472 | 2025-07-02 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85c4943d-9f8d-3315-9300-3208f3db627f | -18.42733 | -54.55947 | 2025-07-02 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d16ce736-c980-3bf2-9232-980cb31fa8c8 | -19.44061 | -48.54931 | 2025-07-02 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 545e33eb-ff6c-3e41-bb09-0cdb92b3a24e | -18.22847 | -54.4764 | 2025-07-02 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2021b52-e1bc-3160-8320-9a7b86cf2df9 | -18.65673 | -55.74495 | 2025-07-02 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 192bea6a-02ad-346c-9cf0-dcb93b9d5fb6 | -16.60349 | -44.51609 | 2025-07-02 04:29:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4903e307-1097-34f1-b6fa-4ef4f1758159 | -16.6811 | -43.88464 | 2025-07-02 04:29:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d54c706-c6c0-3fb4-81f3-196128dd9936 | -16.77705 | -42.78773 | 2025-07-02 04:29:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e40b08f0-31ef-3698-87b1-c86a66c9fa7e | -16.29126 | -48.01463 | 2025-07-02 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81f66689-77db-3022-a2ea-1adbf15747c8 | -21.50899 | -48.81813 | 2025-07-02 04:29:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3484d5e6-bd81-3b5d-aa15-2486f5590bf4 | -7.8135 | -44.0126 | 2025-07-02 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 63379f90-bd32-385a-bfb4-6dcda748cb6d | -7.7944 | -44.0377 | 2025-07-02 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1b18e08c-3b0f-345d-80b4-0c6b69a99ab4 | -7.7947 | -44.0145 | 2025-07-02 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 5c94a5b6-af87-366c-9137-a6e2102c5a2d | -7.8133 | -44.0358 | 2025-07-02 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| a63b2dca-dee3-32d8-b784-ad5e8c193ac7 | -22.55354 | -44.11362 | 2025-07-02 04:32:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a0b67059-4c25-31c1-9127-93b24268d578 | -20.72873 | -56.65124 | 2025-07-02 04:32:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 87f84cd9-4a4b-3501-8138-b66f920f198f | -21.04689 | -55.99921 | 2025-07-02 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 087ab4a6-ba74-336a-b049-e36da89c7932 | -20.83936 | -55.69334 | 2025-07-02 04:32:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff750fae-b053-3888-97a3-7fad8a230225 | -20.72908 | -56.65317 | 2025-07-02 04:32:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 83449332-9d44-3568-bf8e-4ca9a8ccbf41 | -20.72784 | -56.65563 | 2025-07-02 04:32:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0db76e20-4674-3dab-95b0-01aaafeb602a | -22.54078 | -48.81221 | 2025-07-02 04:32:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0cf3829-fef1-37b7-844c-0a8075be4cfe | -29.80855 | -51.22836 | 2025-07-02 04:34:00 | NOAA-21 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 3ad6b8ed-4bc7-3dc2-8fce-886fbb022b83 | -30.14938 | -52.02651 | 2025-07-02 04:34:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| f2422fc6-a686-3fb6-82b7-864adb1db9c6 | -7.7947 | -44.0145 | 2025-07-02 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 80933b2b-d051-3950-b42b-5ff2ba685f2f | -7.6051 | -45.7464 | 2025-07-02 04:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 46797a92-921f-3811-ae66-503208432880 | -7.8135 | -44.0126 | 2025-07-02 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| a13fea0d-5aa7-3018-94eb-917a59cb7d0d | -7.7944 | -44.0377 | 2025-07-02 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 58b2144a-00c7-3cb6-95c4-3958fe437bd4 | -7.8133 | -44.0358 | 2025-07-02 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 89a43b97-312c-30b5-84a3-4f9b744a4163 | -7.7947 | -44.0145 | 2025-07-02 04:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 4867becd-48d2-3099-9de2-60187a927242 | -7.8133 | -44.0358 | 2025-07-02 04:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e5853215-1b74-3b7c-8696-3d5cd084b413 | -7.8135 | -44.0126 | 2025-07-02 04:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 927ac12e-bafe-349d-a3e1-47e1d7ba2d53 | -7.6051 | -45.7464 | 2025-07-02 04:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ad619096-e0ce-37c3-9054-64482bd670f4 | -6.26943 | -43.68328 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| df19ab9a-6288-3ed2-8558-b392b2c93d85 | -4.53646 | -48.01821 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e0ec947-2c04-3394-bba0-28f65b1d41cb | -6.25024 | -44.83588 | 2025-07-02 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7410383-793a-3b31-a6af-bcde406fb678 | -7.21004 | -43.09502 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a2a732f4-972b-36d7-a91f-d3ce6802103a | -5.28513 | -56.01977 | 2025-07-02 04:51:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2fefecc1-e93a-3242-9974-0e343821f92e | -3.31895 | -48.71193 | 2025-07-02 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43c2510c-2eeb-30b7-80df-1766b3d35793 | -6.9592 | -42.89108 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 07cd91e0-2786-39a8-b9f3-c480eabc8fdd | -5.62639 | -43.65776 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5fc9d44-dea5-3fa3-bd9f-f7471c7f91cd | -5.62413 | -44.26287 | 2025-07-02 04:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa30b494-4a70-31bf-a55f-112c9613317a | -7.2124 | -43.09254 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 12b3aaeb-c8b3-3169-9b03-7f5c9d07bda8 | -7.20595 | -43.0831 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cc477538-db9f-304b-806d-45cb9b7ad06f | -5.91141 | -43.4535 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea85c812-b8b0-3624-bf5c-cb40c0fdb668 | -5.65249 | -46.59452 | 2025-07-02 04:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e75e0340-23f9-344d-976a-65c0ec468e26 | -7.20735 | -43.08807 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3bfb0863-c5de-3be9-9354-a767af692ca7 | -4.37363 | -48.06827 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd2132ba-2268-3ec1-89f3-eb94c86acdf7 | -3.89869 | -49.08549 | 2025-07-02 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be225cb5-47d9-3fe6-9828-c51142729847 | -4.53956 | -48.02357 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d065cb0e-4234-3850-827d-a8184c4cb19a | -5.87952 | -44.79967 | 2025-07-02 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cac20133-7481-3a97-802c-5975e44123ec | -7.1937 | -43.17485 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9a948980-93e0-3d26-991b-71771ce65369 | -6.95357 | -42.89035 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d103875d-81da-3bfd-867b-7a1fce7c5dca | -5.62712 | -43.65675 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db856078-9749-3c06-8151-5690fc1b959f | -6.28946 | -43.68287 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| acfa3d55-aea7-39a3-892e-5da416fd04f3 | -3.32194 | -48.71668 | 2025-07-02 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8781cc7-b154-32f2-a81b-854a9cdfa08f | -5.88237 | -44.79775 | 2025-07-02 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 039a337e-9dfd-3f5c-9dc8-401bbdbc8206 | -3.0822 | -52.42921 | 2025-07-02 04:51:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb990108-0c89-3e80-9ad3-1a8c95d8da26 | -4.10583 | -47.93468 | 2025-07-02 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 734f43c4-5ecb-3d0b-85e3-633d9b6298e3 | -4.31791 | -48.08637 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e508f463-9c03-34bd-b03a-48096cc75f60 | -2.58684 | -51.92297 | 2025-07-02 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89af0474-7be5-3352-a5c1-1c7d8ccd1c66 | -5.62667 | -43.65982 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e0f1949-3d56-3644-bf4d-8fc654827464 | -5.77618 | -43.6208 | 2025-07-02 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 262f07d8-48db-3e83-86a1-7d68cd6c0c6e | -6.66649 | -43.84633 | 2025-07-02 04:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 235c201f-b546-35f7-92fd-dfec31d0e971 | -2.9891 | -47.45057 | 2025-07-02 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6843371-13b7-375f-86c5-6670ef6ececf | -6.66121 | -43.84569 | 2025-07-02 04:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de8b7f1e-287a-36cb-b7e9-da986d70eca1 | -5.78099 | -43.62476 | 2025-07-02 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bc5abf7-f74e-3ee2-a1af-26c84977ce64 | 0.69541 | -51.44723 | 2025-07-02 04:51:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5a629a7-0875-3c55-ac35-72feab22a0fd | -3.21225 | -41.84373 | 2025-07-02 04:51:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bd455c9-8abc-3587-8278-2a499696ad9a | -4.31863 | -48.0817 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adb9a903-390f-37ff-9b05-9040fb29d0d3 | -4.37082 | -48.08686 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5be1efa3-892a-36a3-b689-0d24b30580cf | -5.91095 | -43.45677 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 009e7804-f4f7-301f-ba26-b9759e86763e | -5.62071 | -43.66014 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7722035e-c807-307f-83c0-82518105c45a | -3.03281 | -49.44045 | 2025-07-02 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff7b6af3-e384-3981-b2d0-e86f62c8680e | -7.20283 | -43.07985 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c626e74-847e-3978-981b-a142e753e40d | -7.22168 | -43.09297 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01f006f2-211e-3110-8711-514af10cb755 | -3.70686 | -53.71166 | 2025-07-02 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0be8a7c-f48e-39fd-b4a3-9512ee76ac81 | -5.62186 | -43.6561 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8c7da76-bdeb-35aa-b844-94fff15bc180 | -5.78763 | -43.61588 | 2025-07-02 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1100f5e6-2d34-3b40-9c06-c4db51a41941 | -7.20841 | -43.0806 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3d0f2231-dc49-312c-87c1-a4fdc803c3d9 | -7.21154 | -43.08384 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 43d2f9f6-1737-39a4-b270-b11571f7eb69 | -4.37534 | -48.0828 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e549a3bc-e5e4-3783-afa9-4169f86f61b4 | -6.27471 | -43.6841 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 80ef56d6-21a6-3b26-ac81-758bd768fa9c | -6.6621 | -43.84611 | 2025-07-02 04:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b9d14fc-2dd7-3459-99bf-cf83ddce4289 | -6.29521 | -43.68034 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 02945690-d8a0-3c2c-b6c5-6d195131b64f | -7.21661 | -43.08841 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 998759e5-d5fd-3d20-83d4-9bff061ece37 | -4.1903 | -48.13591 | 2025-07-02 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 408aa5c9-d002-38bf-ace0-0ecb4d3d80a0 | -7.21346 | -43.08509 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 06dc66b4-3e58-332a-be44-b0991ded51b0 | -7.21561 | -43.09585 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c6af6991-304d-3c85-9b50-3804d7d99740 | -4.55785 | -48.00703 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05b2467e-5dc0-30da-9867-c1071e85fd26 | -7.22118 | -43.09668 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f10a36fb-0464-3815-bbe5-52b242574221 | -3.03754 | -49.43326 | 2025-07-02 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f002b5e9-6733-3038-af88-e82ebf8d708d | -7.21054 | -43.09131 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| dc2059a8-eecd-32d5-b865-4bcfdfa9288d | -3.32259 | -48.71248 | 2025-07-02 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a24f262-7ce0-3fb5-b1b4-4d69cf847e06 | -4.37152 | -48.08224 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f2b3d95-b966-3c83-b3de-fce49842b453 | -6.21282 | -44.1957 | 2025-07-02 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README13.md)
