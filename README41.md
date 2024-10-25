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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40f4de8c-6c57-3338-9f2f-33efcbe2f439 | -10.86763 | -44.79166 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5a5d8b8-6ad8-30b7-8baf-d0cc2bec35d6 | -10.86707 | -44.79519 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2f7df68-6a1f-3e35-887b-4a717c057f87 | -10.44248 | -44.89633 | 2024-10-25 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a661bb4-e311-3771-aaf1-ae6a921ed5c4 | -11.31169 | -45.01711 | 2024-10-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4c0f036-397e-38fb-9500-21fdce8d2a06 | -11.31112 | -45.02066 | 2024-10-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2542ed0d-cfad-30ab-be0f-4dc55f8649ca | -11.27345 | -45.0218 | 2024-10-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca59208f-9052-3ae1-ba56-ea9a29bde68d | -11.27288 | -45.02533 | 2024-10-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1f78496-494c-31b0-8009-770bc1f3e874 | -11.26963 | -45.02494 | 2024-10-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d9586d4-cced-34d4-9727-0b3b1e1e4032 | -11.21068 | -44.66757 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c35176a3-90ac-3da4-ad48-5443e92ac5db | -10.97464 | -44.61142 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2f82782-d799-3fe6-8124-bd0656f068bb | -13.09538 | -46.41288 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc6bd780-8103-365f-b752-17e399f884a8 | -13.0932 | -46.40485 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cf7b5c3-d0a4-35b8-9bf6-210e1cbbb269 | -12.46422 | -46.33877 | 2024-10-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2771399f-55bb-345c-8f70-f92b384e950d | -12.46361 | -46.34256 | 2024-10-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fc03045-e26d-36e0-863a-78418efddc17 | -12.90587 | -45.07358 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e740b11-124d-3336-a033-b0ffb99a2bc0 | -12.90531 | -45.07711 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33e905ef-bb2b-3a03-aa85-34e5d9b0d412 | -12.902 | -45.07657 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51df17e7-4cbd-3cca-b2ee-5a13bb9d106e | -12.90144 | -45.0801 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a3a1de-fc73-3122-a8b4-a090f61fd708 | -12.89869 | -45.07602 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 024cec5f-bbd9-3dc1-8561-adbaccdf07ab | -14.48818 | -45.54513 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3691b7d5-b9c5-3e66-bb78-b0cd18b09f50 | -14.48761 | -45.5487 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af7a856c-0be5-34c7-9b42-441205e4272f | -14.48736 | -45.48647 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 547938c1-14ed-35b3-84a8-48b4d8fdccc8 | -14.4868 | -45.49003 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef7f63c0-9dfc-3bd9-bc33-58c00c0a1133 | -14.48623 | -45.49359 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b16b10fe-dffa-3169-a5cb-1dda6350c7df | -14.48348 | -45.48948 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780e4f68-5ddd-39a8-9853-2c957529a901 | -14.48292 | -45.49304 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 762b0afb-4dfa-34b5-87ae-5f5fa28ec55f | -14.48235 | -45.4966 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f5ac869-ba0a-304e-ae66-7322b0f30fb8 | -14.48178 | -45.50016 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69152293-599b-3af6-9ff1-044d591a0f99 | -14.47903 | -45.49605 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10ca53cb-81f4-358f-aab2-84278ac6bc27 | -14.47847 | -45.49961 | 2024-10-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43bba906-ce9c-3466-ad74-9d8e514ef0c4 | -14.16805 | -45.41838 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b61c899c-a67f-3d32-9ee1-4e006bda975a | -9.14306 | -47.10295 | 2024-10-25 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 476eaab3-7b10-3bbd-95bd-fe728a8cfd35 | -9.14963 | -47.10846 | 2024-10-25 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f68a4a58-4e4f-38b0-8cba-646a1d765adc | -9.1467 | -47.10355 | 2024-10-25 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f091e6b8-1035-30eb-b44e-a6d1e46055c7 | -9.14599 | -47.10786 | 2024-10-25 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab59936c-0e4c-330c-9bd2-32b7f552d850 | -9.30325 | -46.17432 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2b33ad8-6c2c-3753-95c3-0ab7400b1fbc | -9.30262 | -46.1782 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62aa6614-d952-350c-8406-0e3ce4272045 | -9.29914 | -46.17763 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08ecbeb9-cc5d-328d-a813-14fcc64d145e | -9.27751 | -46.22235 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f59f623b-8b15-361c-8f7f-7a6a09725cc7 | -9.27404 | -46.22168 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ac87323-8688-32a8-99a0-a713d0c3d4f5 | -9.27121 | -46.21711 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4525c09c-a391-3ff4-835a-011efc90c786 | -9.27056 | -46.22104 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5eaf3034-5ed4-3bae-ac9a-41ead2fc90ea | -9.26708 | -46.22046 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6994e16-9ff2-371f-801c-8356c1698d77 | -9.25097 | -46.627 | 2024-10-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dbb99ce-78e7-34f2-bce8-b37d10171795 | -10.46456 | -47.33636 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34d5ce17-4f7e-3898-a207-6ad2704eeaf0 | -10.46166 | -47.33152 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7db36d6-5bfd-36b5-b59f-b0fecbe042c7 | -10.46093 | -47.33577 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6befb71-acdb-34dd-8d10-4f8ea943715f | -10.4606 | -47.33213 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9ccecd3-f506-3b74-9261-2f6e4bb96c1d | -10.44235 | -47.30735 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ae5e046-6991-3a17-ba52-e2744226e52a | -10.39796 | -46.5882 | 2024-10-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0de2d3cf-4d99-3414-9339-542a1cd9cb74 | -10.39731 | -46.59214 | 2024-10-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74427496-154a-3c57-9b2b-bdbb682c339f | -9.53061 | -46.69218 | 2024-10-25 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de64ed5c-36b5-3525-968d-ed3754b0b1aa | -9.52994 | -46.69626 | 2024-10-25 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d1a5728-baff-3269-9c65-4bb696ac384e | -10.2504 | -46.53215 | 2024-10-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14aa2a8a-30c5-3101-afc8-ec4dc35e622e | -12.33271 | -46.75248 | 2024-10-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5506d527-839f-3ebf-a054-32c69c9055a2 | -12.27137 | -46.78682 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8759a102-41a6-3728-aab0-5068abf96275 | -12.19949 | -46.7265 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31d18e26-1112-3917-a744-bc4d11bfefe2 | -12.19538 | -46.72979 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5fec237-a0f6-39ea-b611-bc046d245999 | -12.18049 | -46.98932 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fdcfa7b-635e-3e5b-b011-97aa94fd3d72 | -12.17983 | -46.99323 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b05f13ab-b004-345e-9f41-be792dbecbd2 | -12.17569 | -46.99646 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec9d4b96-4f7f-3f40-b71f-46e387af81e0 | -12.17417 | -46.98408 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0624e3f0-4022-30ae-ac4d-87a2a2b2615f | -12.17353 | -46.98793 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 414031fa-d633-351e-8c79-639b01f153ff | -12.17005 | -46.98726 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c8e0683-1658-350a-ad05-79f9f172ec1c | -12.15743 | -46.58039 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9d01a18-7ea3-30e4-8fea-179a6544a59c | -12.06548 | -46.89687 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d04f05e3-d051-3f99-bf7b-89cb08a532f2 | -12.05984 | -46.88775 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a1931af-033f-331d-82ea-28be0702e559 | -12.05918 | -46.8917 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 185357ec-119b-3745-949d-7caad46ed783 | -12.05825 | -46.88829 | 2024-10-25 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 895267c0-1aa7-361e-a895-c92258ac5db2 | -11.97265 | -47.25393 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa821492-9251-331b-9f6d-8c5821b841f5 | -11.94121 | -47.48731 | 2024-10-25 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4126c8d8-777a-36d1-92a9-be5451706030 | -11.93542 | -46.58331 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 721ffe8e-f641-3de1-a43d-c311feeffcaf | -11.93327 | -46.5749 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 683680c3-d17d-32fe-8370-960da187e49b | -11.93262 | -46.5788 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 896050e6-e9e2-30b9-906d-f9c0423be856 | -11.93198 | -46.58269 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 561a2463-6d5f-3025-9a59-90066d407ba9 | -11.87754 | -47.71234 | 2024-10-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a2fd788-32c7-30d1-b12f-c788c62474d3 | -11.87681 | -47.71666 | 2024-10-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3416d0f3-0be6-3d9c-b58c-622bf6abcc68 | -11.77707 | -47.07549 | 2024-10-25 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a74526a7-c82f-37f9-b428-5c246726e037 | -11.7764 | -47.07951 | 2024-10-25 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a0c6d1f-dfe3-38d2-925a-5143a0927575 | -11.69979 | -47.12487 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c995fe13-447e-35cf-8c42-d24459b55884 | -11.69626 | -47.12427 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4629a47-1462-3c74-a0eb-9be0743bac2d | -11.69557 | -47.12835 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32c865e6-4898-3b40-8448-596650ff7d5c | -11.69273 | -47.12464 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc98410a-59ac-3fac-bc3f-8a6a093286e1 | -11.69272 | -47.12367 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f387967-fdd3-38a9-bd5c-a26afaacdec3 | -11.69206 | -47.12872 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 950c0743-5d4e-36af-9e82-efc2d65c460f | -11.69203 | -47.12775 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0d1f23b-9dee-3a6b-bc48-c835732b8b6d | -11.6892 | -47.12404 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31bfe3ca-533d-3cb3-91e5-c0976738662f | -11.68918 | -47.12308 | 2024-10-25 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9565ada6-f633-3e15-8d18-85e3add91409 | -11.62633 | -47.57827 | 2024-10-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddf17df0-edd4-390d-9833-4b5695c9ffb2 | -11.62336 | -47.50047 | 2024-10-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6782d114-ecbb-3226-abf7-9572f59ef9db | -11.43134 | -47.68443 | 2024-10-25 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f5e6335-7eb7-38e3-818f-2fed1e8ed312 | -11.34825 | -47.31245 | 2024-10-25 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bbd8326-02f6-36f6-8fb0-5fc1e2aa6203 | -11.27596 | -47.57951 | 2024-10-25 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcaa44d7-abd3-32a8-9965-83e4d14a8e2b | -11.19884 | -47.57123 | 2024-10-25 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93bb157a-ffb0-33b5-8655-345fcb8051f5 | -11.18664 | -47.5116 | 2024-10-25 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8e993f0-ddba-3ef3-a811-26c5931658db | -11.18636 | -47.50854 | 2024-10-25 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2b27295-96e8-3ed8-a3c4-55d8d28aadb4 | -11.18565 | -47.51282 | 2024-10-25 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cf4a2ee-6d1a-325c-8999-25bb0941ce8b | -13.65583 | -46.81127 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 611cc377-ad66-3461-b894-cf29c3f0eebb | -13.56076 | -48.15929 | 2024-10-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a92b8d1-f97b-3552-b365-543bc578fce4 | -13.54104 | -47.3496 | 2024-10-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README42.md)
