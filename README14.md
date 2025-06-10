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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc943cc3-7d8d-3266-a982-e2c22ec0ce36 | -10.36347 | -57.5046 | 2025-06-10 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ebac41b-4588-3c59-88bd-a8194909d135 | -7.58945 | -63.77613 | 2025-06-10 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51ab4ebf-a329-3b91-89ec-44783d390248 | -10.84708 | -53.76601 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8305f339-38aa-31d6-907f-8d5d039c7ea4 | -10.84169 | -53.76531 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47dd3bcb-9c7d-3e2e-a296-f5df715911c0 | -10.94838 | -55.32944 | 2025-06-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34e61866-2a0d-3997-aadd-3a38f5b4c791 | -10.3687 | -57.49761 | 2025-06-10 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e85e6a6a-7bab-309b-aeb8-d1a39ede657c | -10.86692 | -53.78207 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb884cbf-8b9a-3316-beb0-821a5d22c318 | -2.95352 | -60.01561 | 2025-06-10 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae80c9f-0664-336d-97cb-0926a3326a6d | -10.87779 | -54.31174 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd8055b0-ee1c-3bcd-adb4-e5d9a1cf74e3 | -13.09677 | -52.28665 | 2025-06-10 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 699ee57d-7cb3-366f-b626-612d57bd7fec | -11.33075 | -56.88471 | 2025-06-10 05:29:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7159ded9-23cb-37b2-a473-45a8f21cab0f | -10.04551 | -64.9802 | 2025-06-10 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a3e0cbe-169e-3b8f-9f79-936fe4329cec | -13.79089 | -54.31582 | 2025-06-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ed45934-9e5d-330c-941b-91ed909859ec | -11.58705 | -51.34172 | 2025-06-10 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8cc0897-0af8-39d1-bd60-b6c64e6b0030 | -12.29676 | -50.10928 | 2025-06-10 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9cc7f2d-ca7c-351e-9d1f-5ed5be6366b3 | -12.13143 | -54.65704 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4616d12-7ee4-3b14-962d-e71c00ffb064 | -11.77179 | -54.38139 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12098951-0dfd-380f-9c2a-3f80d1584e83 | -11.59167 | -51.33836 | 2025-06-10 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b456f30-915f-3223-a234-10b9d89b7e5c | -12.71711 | -54.97057 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 222f692b-63fb-3f10-8764-0e82156b1044 | -11.58531 | -51.33759 | 2025-06-10 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2baf4df4-a3a5-3624-8f1e-ca09023a1012 | -11.76815 | -54.36766 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da17aec8-201d-3d4d-9db5-eb82a697c0f6 | -11.76736 | -54.37147 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd53d271-37eb-3cf3-a570-bdc097a07a06 | -12.7226 | -54.96817 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a56a30f-0dfe-3223-a19b-775bdaa448d0 | -12.29007 | -50.1036 | 2025-06-10 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8821008b-1f09-3802-b5c6-897a405ead16 | -13.79132 | -54.31234 | 2025-06-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1537c0a6-1b26-3d8e-81e5-62cb40245c67 | -12.28986 | -50.10847 | 2025-06-10 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54149619-7c62-3bee-bc24-3bb851ba8cdb | -11.76735 | -54.37418 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc4bdb5c-944d-3d9b-9e73-9004a91d1f53 | -11.76779 | -54.36823 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 305e5496-6537-397f-9617-898bb12de0f4 | -11.76775 | -54.37092 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7342cb06-96ed-39d9-a911-48a00af847de | -13.09128 | -52.28668 | 2025-06-10 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 827d1426-db1f-36d6-8147-a979f8829e59 | -11.33037 | -56.88641 | 2025-06-10 05:29:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 150cefb7-50c7-3efc-8b85-bb1772a06291 | -11.76291 | -54.36696 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b67ddfc7-89f9-3139-86de-72055f7cb744 | -12.13061 | -54.66343 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f34933d-96de-3772-9048-c2b15198da81 | -13.58953 | -54.28199 | 2025-06-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0751a522-0426-33f7-b8da-f3bd47bbd056 | -12.29056 | -50.10198 | 2025-06-10 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de534e9c-8098-363a-9639-762ff2e2a0a5 | -11.36684 | -56.5588 | 2025-06-10 05:29:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cecf2cc2-4e7c-38f1-8277-431555022f60 | -13.58912 | -54.28549 | 2025-06-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 012820fb-c26f-3a96-8bc0-d86b95d8e9bf | -12.72221 | -54.97125 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d75dc6d2-40d1-31ba-a248-a79c9a9af7e4 | -11.58764 | -51.33648 | 2025-06-10 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d18f6891-4bac-3f04-89d4-1852ef614b30 | -12.29698 | -50.10437 | 2025-06-10 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1199db17-2df6-338d-809b-d21167ff21df | -13.72118 | -58.6746 | 2025-06-10 05:29:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02cd3510-d80b-3eda-b254-aedfb0334636 | -13.09739 | -52.28745 | 2025-06-10 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86113024-b725-393d-b5a8-53e0bfbb81eb | -12.8803 | -61.64656 | 2025-06-10 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a28006aa-d8a8-3723-8b0b-21964d6a37ca | -12.13102 | -54.66024 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdf2c42f-237a-3218-b9dd-1c1612f8fec6 | -12.72182 | -54.97433 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5cac100c-8997-3458-b4fa-14e5814eb69b | -12.13021 | -54.6666 | 2025-06-10 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6709177c-66f0-3118-b091-a23762448870 | -12.29623 | -50.11084 | 2025-06-10 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7151511c-7f50-3a42-84c9-71625c766f31 | -11.76695 | -54.37745 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df561d7-777a-3646-b367-030251bddfe9 | -12.28933 | -50.11006 | 2025-06-10 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f41f771-5179-3be1-86d1-62e7a672b5e5 | -11.77133 | -54.38191 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64a7bf04-0995-3074-81fd-e63d6afa2fc1 | -12.88373 | -61.64708 | 2025-06-10 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 957a2695-6369-3cf3-a267-4d86fd012e82 | -11.76255 | -54.36753 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64c29353-d13a-33f6-b761-8c30835d1788 | -14.84449 | -52.28389 | 2025-06-10 05:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da58bc23-4068-3c70-9b31-f694b7176d7f | -11.76652 | -54.37799 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 488602cf-b54d-30b0-8106-fa11cd1dae68 | -11.76694 | -54.37473 | 2025-06-10 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15561923-e6ac-3369-86fa-9ee7c970f3fa | -5.2108 | -43.3067 | 2025-06-10 05:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 180cd2f7-2303-3238-b574-9312cbd720ef | -5.2106 | -43.33 | 2025-06-10 05:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3da4485c-762f-3a3f-9527-4e8109ee41e4 | -20.82537 | -54.95705 | 2025-06-10 05:31:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b9501c5-791d-30e8-8e05-01486b30f18d | -20.82241 | -54.9572 | 2025-06-10 05:31:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eea9d9b-29f4-3eeb-b00b-26d05ec294b6 | -6.19351 | -43.32067 | 2025-06-10 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 75dbd621-f17b-37cc-aba6-fafb287a8c25 | -4.30751 | -48.07249 | 2025-06-10 05:55:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 23f276e0-3775-3b2f-a84d-cad00c8f5d09 | -8.95881 | -47.96412 | 2025-06-10 05:55:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2a17eeb5-0781-3a36-9cc8-42140449d949 | -5.64762 | -43.59547 | 2025-06-10 05:55:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5c952ea6-7fec-33ee-ba17-432dcd08f581 | -6.49407 | -42.84705 | 2025-06-10 05:55:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 702e6220-f034-3bd2-a611-4d6e716f4d15 | -9.0073 | -49.57062 | 2025-06-10 05:55:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c1855f8a-93b6-3f7a-98a7-f613c4df29be | -5.77276 | -43.61794 | 2025-06-10 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 11f0011c-5c39-34c9-8c3b-448908c7cf70 | -10.05618 | -48.66524 | 2025-06-10 05:57:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fbfa88e5-ff2e-34e5-9805-171be8ddc760 | -11.76279 | -54.37249 | 2025-06-10 05:57:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 62317092-6ec3-3914-a05e-401c6a350f9b | -10.84424 | -53.76075 | 2025-06-10 05:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3e76e583-0a1a-3511-a44c-4d516eac1673 | -12.29047 | -50.10282 | 2025-06-10 05:57:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 768916ae-3ac1-384a-a5f8-3410d6ad0356 | -12.7203 | -54.95806 | 2025-06-10 05:57:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a2b563c6-4986-3bcf-bedd-f227424d702e | -10.04719 | -48.66393 | 2025-06-10 05:57:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| cdd07515-2017-3350-bca9-94cc4723d6f3 | -9.2053 | -48.85903 | 2025-06-10 05:57:00 | AQUA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f3a440d6-1387-38d6-b991-0ea3c17b41a4 | -14.8417 | -52.27989 | 2025-06-10 05:57:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c36a26a0-01d0-3a55-ab11-46abc9f89e34 | -12.71796 | -54.97189 | 2025-06-10 05:57:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bf9a4672-27ce-3480-947f-158af760fd7a | -5.2108 | -43.3067 | 2025-06-10 06:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 15cc4799-c0b8-3a0e-91ee-0d5415ff31b1 | -5.2108 | -43.3067 | 2025-06-10 06:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 797f4d42-02c7-3585-801e-8c3e313b0856 | -10.2674 | -46.9903 | 2025-06-10 08:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| b5f1c25d-a4fb-328d-8afb-d01782570372 | -10.2677 | -46.968 | 2025-06-10 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e7aa4407-afd1-3a10-bcbc-51aa41b64694 | -11.7754 | -54.3756 | 2025-06-10 11:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 81a625e0-4ff2-3994-84a1-3a3b9356c378 | -11.7754 | -54.3756 | 2025-06-10 11:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 2dee5e27-7fad-334d-bd07-999dc1f510c6 | -11.7754 | -54.3756 | 2025-06-10 11:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 192.2 |
| f2abcc22-ffb6-36fe-b162-7a38d9d377e6 | -5.28335 | -35.81073 | 2025-06-10 11:23:00 | TERRA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 18a79b50-51be-3fc6-aa2c-7d4baf7997d1 | -11.7754 | -54.3756 | 2025-06-10 11:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 183.3 |
| 981292a6-2594-350c-b7ba-72fe85085c9e | -11.7564 | -54.3774 | 2025-06-10 11:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a03c6445-6c17-3fe5-803b-0a4b8a6455c9 | -11.7754 | -54.3756 | 2025-06-10 11:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 8fc7bcdb-9800-3b85-9bfa-a3940ce64d66 | -11.7754 | -54.3756 | 2025-06-10 11:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 1799484f-8b63-3419-a5b7-9b07208b19f6 | -11.7564 | -54.3774 | 2025-06-10 12:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 88b37822-28cd-385e-8ccb-b41759e1ab3f | -11.7754 | -54.3756 | 2025-06-10 12:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 72489e65-b883-38b2-a1a1-4fd86179ada2 | -11.7564 | -54.3774 | 2025-06-10 12:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9f6e8465-c991-3076-a4ab-245b4807d87b | -11.7754 | -54.3756 | 2025-06-10 12:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| c92df806-421e-3bc0-b29c-277ab15755bd | -11.7754 | -54.3756 | 2025-06-10 12:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| e042b012-5b19-394c-ad89-fce349d66c4d | -11.7564 | -54.3774 | 2025-06-10 12:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 9d8c8d26-c8f8-382b-ba0f-255410ef1b61 | -11.7754 | -54.3756 | 2025-06-10 12:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 5d4cbf25-0c40-379c-97fd-f5a8fa96020e | -9.3972 | -48.4305 | 2025-06-10 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9de2c768-5d8f-3949-a7ef-9234101fd96f | -11.7564 | -54.3774 | 2025-06-10 12:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| eefebf91-f635-34fa-8801-cae0eeb3b67f | -8.7993 | -45.1044 | 2025-06-10 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7f087f3d-0b4e-3cba-a9b6-68e92a9d34f0 | -11.7754 | -54.3756 | 2025-06-10 12:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 38c49bdb-8741-343f-a463-13f62c3e9145 | -9.3972 | -48.4305 | 2025-06-10 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3c1e06d5-7b73-3816-9497-5b34760de35a | -11.7754 | -54.3756 | 2025-06-10 12:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |


[Clique aqui para ver as próximas entradas](README15.md)
