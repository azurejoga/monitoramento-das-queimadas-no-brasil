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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c466f6c5-8dc0-3353-8c03-6b17e25f4c32 | -7.10976 | -44.14328 | 2025-09-08 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dd4c0a1-0e00-3745-918f-d270d2cf4140 | -6.00911 | -40.22799 | 2025-09-08 03:38:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dcd9ad5e-500e-31f1-9150-d2b6590b8552 | -11.4128 | -50.374 | 2025-09-08 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| cfb91811-82f1-358a-9a62-ed954ae99833 | -11.2007 | -54.9992 | 2025-09-08 03:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c38a6f00-e2f0-3ad0-a097-0819fb6be28c | -12.6153 | -56.9742 | 2025-09-08 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0d36efdc-ca92-3ebb-bba1-ff0d5e9334cc | -14.5067 | -48.8085 | 2025-09-08 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a11a2271-b93a-32b4-8070-14d7233c030e | -14.2383 | -58.3502 | 2025-09-08 03:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 223.1 |
| 4ec503f9-d5a8-3228-b828-9fbcd1624f01 | -14.2578 | -58.3284 | 2025-09-08 03:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 331a98da-e620-3b9d-8a12-384f0f08033f | -7.4168 | -61.6339 | 2025-09-08 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ced7e1ad-a997-38e9-b281-0a213ba62852 | -14.2575 | -58.3484 | 2025-09-08 03:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 60460a71-9979-3912-90b9-7351e4ec5833 | -7.3983 | -61.6346 | 2025-09-08 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 8c175303-fa14-3282-9ec3-3bd3a6f15c91 | -12.6343 | -56.9725 | 2025-09-08 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3e15cf1d-b2a0-3f26-9e3c-571b4d3dde83 | -14.2386 | -58.3302 | 2025-09-08 03:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| b2c42df5-d012-360f-b741-3a8fe6e6ac9d | -11.4125 | -50.3955 | 2025-09-08 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 5a1a9106-ef4b-3f1a-bf8f-91e42b769337 | -7.3984 | -61.6156 | 2025-09-08 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 27622e3e-d423-3ce7-b797-f46740a33279 | -10.82108 | -47.73764 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66cceeec-a183-364c-9e4b-8bd43e12c385 | -14.49693 | -48.8192 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7efc13c6-0629-3412-9561-49d4eca62c37 | -8.69784 | -45.31071 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f8214272-8faa-34d5-b94c-590cc5cb4815 | -13.74143 | -46.90418 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76d3ea86-65e9-3cd7-8306-35d34741ffdf | -9.72452 | -43.97767 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4b4b8148-8f86-356a-8939-ced0201e3f45 | -9.2018 | -46.04307 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c165b1fc-34f2-3a98-9a4c-e7a204e4313b | -11.01885 | -46.02681 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da03e753-61b7-3572-9b26-b1e561cc45a3 | -10.14322 | -46.22251 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 959d79a2-69eb-38be-81da-3fcfb89fc349 | -11.28647 | -46.46569 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51dd063f-8b72-3378-b71a-939e71fad243 | -11.2769 | -46.4677 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d518f6e8-ef9a-3fa5-8694-2fb16e3f0bd9 | -11.14416 | -45.25771 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59ee15a5-c10d-383c-bec7-7669a8ef399c | -9.20195 | -46.05627 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9d8cf4e-7a3f-354d-9bf2-d4117fc6ec8f | -11.61303 | -47.15017 | 2025-09-08 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 708ede19-cc44-31df-a4be-2c0545336f76 | -9.88219 | -46.53627 | 2025-09-08 03:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e72ef29-4eb8-3fc3-a9f3-063febede306 | -11.24551 | -47.56104 | 2025-09-08 03:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f488ec2e-61b4-39da-b233-33c9e73c51cf | -14.51733 | -48.76375 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca3a81b2-249f-34ca-a8c9-208b8c79385b | -10.28725 | -48.80763 | 2025-09-08 03:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9200469f-1f10-37de-af8a-c5f627708ea7 | -13.71975 | -46.88531 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4895313-a6b4-3061-a018-40c2e314fae4 | -15.18697 | -47.95982 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74d5c242-7068-34d5-99d2-b7fd3366f865 | -16.27846 | -45.68562 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4cb075e-efbb-37ac-b37d-a13fa748d7c0 | -11.60534 | -47.15486 | 2025-09-08 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee2a9f21-112d-3604-9ffa-a9cde19f937a | -11.41072 | -43.58649 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4da1c271-2231-3a0d-876d-38230adaa3cb | -14.60897 | -48.08611 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75e75d75-a3e9-3b31-b97f-fa54271995f5 | -11.01798 | -46.02762 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c8bbac9-0651-3400-b178-bf80cbc22a78 | -16.27949 | -45.68098 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8663ecbd-96a1-3c99-b06b-7bb675660b2c | -10.82081 | -47.74611 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7c290c6-d723-3e4b-8fec-1e7f1f8d22b1 | -14.50845 | -48.80334 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dfec864-6662-3021-a2d9-1d82a6a81608 | -15.09406 | -48.13871 | 2025-09-08 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ec4e5c8-eeec-3498-a622-4c248baa70ae | -14.49973 | -48.80634 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d21e35a0-74bb-316f-9817-da6a97676c23 | -9.32942 | -46.52849 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c43237c-9025-30f8-b927-a406646ca294 | -11.27891 | -46.45781 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9bc4d61d-aa8c-3134-a2c4-bf6e56579cb0 | -15.13629 | -48.06932 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3396525f-927b-3045-9ca5-46b961bd7072 | -11.13792 | -46.34875 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3545681d-bd33-3e8c-8e67-9b433c881503 | -10.78212 | -46.01152 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2f8379d-7926-3b10-adf1-027a5aec8c1b | -14.51897 | -48.78289 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 418545d4-a945-3956-aaec-3295c02c9827 | -15.08816 | -48.13706 | 2025-09-08 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 935eed06-e0b3-37d9-a763-af062da06f56 | -13.81949 | -46.25199 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0c2eea9-e3a9-39ca-b803-afd65ca3c06a | -16.28931 | -45.68805 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 128d59df-672d-35c8-8971-826b0b6a67cf | -9.33046 | -46.52306 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c8ad5fb-62fb-3beb-9862-b1a6bfed05a4 | -15.13635 | -48.06889 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70007db8-9f72-3bf0-897d-fb35c4f09af8 | -11.28086 | -46.44827 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 246f8697-6ddf-306c-8d44-c6333f79cb39 | -10.14717 | -46.20197 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 437f452a-c6bc-3392-8115-3e5612e8060f | -13.82625 | -46.24901 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f82ebc35-8a9e-3508-a280-996c4494496a | -10.79518 | -47.73359 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ff87060-3a47-389d-9277-125a84049855 | -12.41082 | -47.50447 | 2025-09-08 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4b17b3-e83f-3304-870c-11f455392ad6 | -9.20298 | -46.05106 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c8e6e62-97cd-3108-b594-7fa264dee3d3 | -14.29916 | -44.87561 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6952131a-6344-3287-910a-bd4a6988f510 | -15.52888 | -48.18208 | 2025-09-08 03:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66194608-966b-34b2-8807-bd06e1318576 | -13.7167 | -46.89996 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 190aa1c5-b9dd-3688-b966-ceea32428894 | -9.81847 | -47.77087 | 2025-09-08 03:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a8f9533-2b7d-3522-9a15-9e94e099e08f | -13.67285 | -44.22659 | 2025-09-08 03:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69dd8643-6687-3380-9cfd-53a81d8a5260 | -16.28463 | -45.68316 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 696785f1-fe4b-3faf-8451-4a9aca8ed079 | -13.70912 | -46.8749 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8dc84e20-9a2b-39ca-835e-189278e7ba7c | -14.77716 | -48.11417 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44d68dd8-d983-3efe-b6dc-24081cd71fb3 | -13.0007 | -45.20882 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e54cafa-af20-3590-a68c-1b05c14a952a | -13.70991 | -46.87113 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4713011-edf3-382d-9000-fd697020d78e | -11.28129 | -46.45904 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| dbea6573-ef5d-304e-b2ae-9da8cccc7a1e | -14.29307 | -44.87815 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fe2f329-4f6c-349b-8cc8-26e99c666bcb | -12.99994 | -45.21265 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 256149ac-18ab-3e40-9d5a-29b3075d955e | -11.41011 | -43.58966 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5aa2b058-852b-34cc-8a55-e984fe36c214 | -13.64804 | -43.80284 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84737695-2c18-3c2b-b049-0a8f8e60129c | -14.51753 | -48.78953 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cebe679e-b8e8-3dce-986c-3171f7cfa7e2 | -10.18225 | -46.23653 | 2025-09-08 03:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 183b1575-c7e8-3064-a30f-a95db83d36d9 | -8.69729 | -45.31548 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 13907482-c259-362c-95da-43a8efef3731 | -14.79143 | -48.14244 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1e44b24-5d1f-31ff-a161-d3f317059bea | -10.13822 | -46.19617 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af342509-ba43-3bfd-a6a8-a53d8f534018 | -12.16795 | -43.9437 | 2025-09-08 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f851239-99e4-323c-bff8-9a9375048474 | -15.16697 | -47.99041 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85bf6d23-98c7-3c15-9b8a-21792cc5d978 | -14.78939 | -48.14904 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be84596c-3c49-3de1-815a-c9d5b9389a6a | -14.26134 | -44.9451 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4122da9f-010d-3eea-8bcd-719f04ac9936 | -14.50503 | -48.81447 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0d487db-026a-32ac-9b2e-63d915308ca8 | -9.71942 | -43.97792 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a6f656c4-0789-33a9-b950-62abe6fc831d | -15.19214 | -47.96669 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bf3a8c1-0574-3821-b0db-616b021fbaf1 | -15.29035 | -43.38268 | 2025-09-08 03:40:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4323c4fa-fce2-3623-87d0-1997bca9b8bb | -13.64633 | -43.81155 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c57e878b-acd8-3d4c-806b-66b4c2336a56 | -9.19979 | -46.03408 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4430212-21ed-36ed-a12f-d3beb32e9d0e | -15.13515 | -48.07453 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53740775-254c-3f1a-92cb-ba13ef2a117c | -12.81538 | -47.99974 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8126aaa4-81de-33da-9d6e-f99160dd0bac | -10.13937 | -46.22291 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46a452eb-2e49-3db8-ba7c-7b56c2988833 | -15.42188 | -47.68999 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90639e48-0ff4-3b95-b7da-c1697a8a0998 | -9.87663 | -46.53074 | 2025-09-08 03:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4b9f09d-0258-3cc7-836b-b1abc93f8be1 | -14.29245 | -44.8718 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 905d126a-eeed-37ff-9e28-6d296823319a | -9.19873 | -46.03945 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58614b95-b5ed-31ab-ad5d-c23b694e053d | -16.34016 | -45.05473 | 2025-09-08 03:40:00 | NPP-375D | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f2b18ba-c368-341d-9697-8fe88dc3224f | -8.70396 | -45.3116 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README23.md)
