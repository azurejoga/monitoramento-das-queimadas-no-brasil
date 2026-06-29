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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78c70381-277b-36d5-88d6-c62a4be0ed64 | -11.89282 | -57.1256 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4386bcea-ae72-3b75-8021-76ccdf98aa61 | -15.38269 | -59.47979 | 2026-06-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f54714b-ae62-34a1-99e8-1bd830400619 | -17.70664 | -46.77954 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fb5286b-28a1-3234-88b8-fa1294b1751a | -12.28386 | -57.55017 | 2026-06-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6082c58-8a8e-318f-aa62-03029f616488 | -17.70429 | -46.77905 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92a7da5b-a884-32c3-a776-67ceecb877a0 | -12.54878 | -57.18494 | 2026-06-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a329ac1b-7b78-3089-b4b1-39c24466cc7e | -17.61519 | -46.69502 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bf8a1f5-79f6-3964-b100-33bde163e989 | -16.78695 | -48.76218 | 2026-06-29 04:42:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f35575a-5f45-3bad-85e4-6158a03736f3 | -17.70875 | -46.77608 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9de011cf-224e-3b8f-b2cd-991eed16d81c | -18.803 | -44.55716 | 2026-06-29 04:42:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25ab966a-a5de-30f5-92fb-bcb37f3f2816 | -19.91899 | -42.32371 | 2026-06-29 04:42:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0bfeaecb-93bd-3030-8f12-49c5676d9f92 | -17.61566 | -46.69133 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b16f2d72-f8c7-3e48-b95c-1da2d5f55741 | -18.49191 | -54.09887 | 2026-06-29 04:42:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb61829e-a7c7-3b02-a9c5-466b1ed4fde7 | -14.01312 | -54.48196 | 2026-06-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f2bdd99-5aef-32af-bda4-f010dfb023dd | -15.07744 | -55.81014 | 2026-06-29 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 738fa0ad-cbfc-34da-8d86-f111d61ef4a6 | -18.48445 | -54.10149 | 2026-06-29 04:42:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 402f8dd6-0c9e-3e0c-9e66-0e2463bc00ec | -12.54955 | -57.18064 | 2026-06-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb8212f4-48d6-3a9e-8930-14240a9aab4d | -14.02548 | -54.47515 | 2026-06-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 720e68dc-5aeb-3418-a3be-199f9a7e8cea | -16.78368 | -48.76272 | 2026-06-29 04:42:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b62f4f8-b962-3f75-be68-610992eac420 | -12.54442 | -57.18408 | 2026-06-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e81129a-49b8-38dc-bd7a-85fbe7ee2ea5 | -20.30837 | -42.67375 | 2026-06-29 04:42:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0a45f432-da63-38f1-a460-342f3d9a29da | -18.4885 | -54.09824 | 2026-06-29 04:42:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99f69868-c400-30b2-b3aa-53d9a3de607a | -17.70761 | -46.77223 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02e538fc-8cbd-3e65-a7e6-a992980888d1 | -15.12173 | -46.49001 | 2026-06-29 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13509a65-2e8f-34e7-8e8a-4b4e2dc343af | -17.70264 | -46.77887 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c397142b-f5a8-3c07-b7a9-1f51ca2f0427 | -19.33332 | -45.24781 | 2026-06-29 04:42:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e0ee87-d3e4-37d4-b330-a07c707fc7ac | -17.70921 | -46.7724 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3da0cd68-0842-3c6a-81b2-f55e879a84e6 | -17.70829 | -46.77973 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8046d73-374c-3ce0-a7db-31778a32e014 | -13.94108 | -53.93653 | 2026-06-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dafeee5-1bda-3459-a0a2-8d8c9c63b46f | -17.70712 | -46.77589 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f25a939f-3659-3e49-ab8b-580c371b45fd | -19.81341 | -42.87839 | 2026-06-29 04:42:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1cf24b96-60ae-310b-abde-36e8375b0e98 | -17.61612 | -46.68763 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b47e4381-e0b2-3afd-8edd-da92daf6071a | -12.79261 | -54.88546 | 2026-06-29 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98f281e8-2285-39ae-88a9-b2ed16553f14 | -14.63729 | -54.52736 | 2026-06-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72c99f4b-0a3c-3bd5-a9d5-19b1e5127a30 | -17.70312 | -46.77524 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26205912-c977-3a95-ae9a-8230a20c35f0 | -14.62666 | -54.45932 | 2026-06-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fd487ec-e9a3-3b46-a710-6d0642c651e4 | -18.13075 | -49.09671 | 2026-06-29 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07554160-ddba-3c0e-a00a-eaf1230d72bf | -18.48785 | -54.1021 | 2026-06-29 04:42:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55c738ca-ab9c-349a-86d9-43e9b1a02ed7 | -19.81378 | -42.8747 | 2026-06-29 04:42:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 86318664-9081-31a8-ac28-2a18e5de32d9 | -15.07359 | -55.8095 | 2026-06-29 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b19371b9-5e53-382a-bfe6-ac9be0316e72 | -19.58668 | -50.38283 | 2026-06-29 04:42:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3910407c-4812-3b45-93bc-820db947d163 | -12.28836 | -57.551 | 2026-06-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b54e72d-e9ed-391d-95f1-201fee1d7ed1 | -15.3736 | -59.29523 | 2026-06-29 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 680a5f49-4c89-3b64-88a0-fa5cb8ded6b8 | -17.70474 | -46.77541 | 2026-06-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b3d9737-8a18-3a5b-84f3-9c03800f8362 | -19.5827 | -50.38618 | 2026-06-29 04:42:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 120ba52e-c7ca-3740-99e9-715dccef752d | -14.63025 | -54.45995 | 2026-06-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd6d076-923b-3856-95e5-82352f60e9be | -19.91897 | -42.3231 | 2026-06-29 04:42:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb3c2087-4cf8-338b-b6c9-b9ac9914c4a7 | -18.78231 | -57.36629 | 2026-06-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 43f989ae-ef59-3b44-8982-83d3cacbfd83 | -20.44451 | -53.77433 | 2026-06-29 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2781ad68-e61d-3440-bacb-ab2c3014af34 | -18.78628 | -57.36709 | 2026-06-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 9a227a0e-20f3-3646-8453-c35a56509326 | -20.47007 | -45.89122 | 2026-06-29 04:44:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95ae1da4-bc2c-3cb9-ab36-00b4f89689e8 | -18.78561 | -57.37071 | 2026-06-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 623259d2-31ab-33b8-bda6-b42db3940ae4 | -18.77834 | -57.36548 | 2026-06-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 1fb27ec9-7ce2-3e81-bb3d-1fa302938f20 | -18.77766 | -57.3691 | 2026-06-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5940a157-bd5b-3079-97ac-072925a1eb38 | -6.86676 | -56.57341 | 2026-06-29 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6fbb99fa-c15a-33c6-9982-2f3911a5d1b1 | -7.3087 | -46.29144 | 2026-06-29 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e29511b-b0c8-3c94-8e1e-bb118568f77e | -8.78096 | -46.91835 | 2026-06-29 05:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcb55e1c-3a30-3fb0-b599-bc70161b9b5c | -8.78143 | -46.91488 | 2026-06-29 05:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfc1af01-b2d5-3164-8c30-812bb658af07 | -7.74585 | -44.18502 | 2026-06-29 05:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63dfd4f9-f7a4-39e3-a51d-23316587f56f | -7.30823 | -46.29502 | 2026-06-29 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccc0e3bb-7998-365a-9c8d-7a11a77cc41b | -7.74658 | -44.17941 | 2026-06-29 05:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24e2ef08-8836-35d6-a71e-c794f710a9fb | -13.71089 | -47.85789 | 2026-06-29 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26615c40-bdc1-30cb-91c4-0aee7a914692 | -11.88978 | -57.13084 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be0ba8bc-7373-33d3-aec2-643e51307a98 | -9.31824 | -58.02299 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f71d3931-2f36-3c54-aeb8-ba462417df12 | -11.31666 | -54.46509 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| deda6d45-f62b-37dd-8180-acb6013a4eb2 | -11.89201 | -57.11673 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b3e75fc-feb0-35eb-9551-655a200ad317 | -11.88091 | -57.12215 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54bb7610-e54b-38ae-af70-edac1c380ca9 | -9.32162 | -58.02356 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c54c6910-2849-387e-b5fb-e4d82610057b | -12.51815 | -48.29718 | 2026-06-29 05:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bca05074-07ae-3236-a136-2dc7d046a1f8 | -9.325 | -58.02411 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4ecf08b-8af6-3348-9f15-e225c176d06e | -10.32084 | -50.17725 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b6bf01a6-726f-3007-bcdf-7e81fecdac13 | -10.30172 | -57.12253 | 2026-06-29 05:16:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e16757df-ccae-3f3d-b2e4-8e712c76372d | -9.08912 | -59.40363 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62b3361c-fe98-365c-9b68-ff26dd73391d | -9.08356 | -59.41515 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89f327d7-110d-3b6c-89cc-7d6f6b80c1c6 | -12.23135 | -56.55 | 2026-06-29 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47102bc9-5c3d-3316-85d5-b348f0e16e33 | -14.62883 | -54.4618 | 2026-06-29 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce0b967e-965a-302a-8e85-ecbdfea1fbfa | -9.08556 | -59.40303 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37ad6027-66a0-37b3-826d-68dafa9fce0f | -9.18834 | -58.06905 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2342627-36fe-389a-bf4b-5a891632ead1 | -9.08267 | -59.39842 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89baea5e-6ca9-334f-b0ff-8ad075f1583b | -11.21289 | -54.2985 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e60325-2434-32e0-a1c1-2f105d7ee507 | -12.46337 | -58.49456 | 2026-06-29 05:16:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9e06569-ee22-321a-a40b-e34b1742aede | -11.8859 | -57.13382 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 221f2e06-f9b2-3b83-8b52-77ee21dd6df7 | -13.85927 | -44.75821 | 2026-06-29 05:16:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d430316-873f-3464-a778-a64ad3f46b91 | -9.69187 | -47.69871 | 2026-06-29 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78376514-cd0f-3b58-96df-cad188cc9e80 | -12.51651 | -48.31045 | 2026-06-29 05:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 518926aa-41f8-3af7-911f-76b6c9e9fcd0 | -12.52348 | -48.29781 | 2026-06-29 05:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 752c4cbc-271e-3a27-b295-f33d85797c34 | -10.32575 | -50.17988 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2d720e2b-d70b-3950-b846-d97c6f069c26 | -13.70481 | -47.86148 | 2026-06-29 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e90e6fd-5365-3a2f-9c23-a0394900b17e | -11.3202 | -54.46563 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 396e0b4f-0599-340e-af00-e8f575b653c8 | -9.32779 | -58.02829 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d648673-178e-351e-b0a7-5891b53fa790 | -9.32558 | -58.02049 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c4ad868-e572-3ed0-86c9-9076829de858 | -11.21608 | -53.82971 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a6c1003-17da-3ee9-a392-3857c82ea0c7 | -15.0774 | -55.81012 | 2026-06-29 05:16:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0bcdf62-b132-3407-aa83-e162b7aee1f5 | -11.32315 | -54.4702 | 2026-06-29 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ea307e3-1798-3335-9a69-49a3cdac94b4 | -9.08667 | -59.44066 | 2026-06-29 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb9a6ab3-d9f5-39f4-89d6-2badee5a92d8 | -9.32441 | -58.02774 | 2026-06-29 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e454f4df-edd4-3c1c-a63f-3f7b2f8e1653 | -10.38893 | -56.76619 | 2026-06-29 05:16:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fea2e38e-2582-31af-b141-1d68c69e5f7b | -11.89478 | -57.12079 | 2026-06-29 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64aaed52-3eab-3902-8db4-4e4d3c1d5b47 | -10.32019 | -50.18184 | 2026-06-29 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1633fdcc-e6e9-3e00-aecd-efc3140380b7 | -10.83006 | -49.13291 | 2026-06-29 05:16:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README6.md)
