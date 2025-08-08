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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d1aa175-a292-38b4-8d3c-6a6018044288 | -8.9213 | -60.7489 | 2025-08-08 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6a143440-15e7-326e-9dec-218509d16ea4 | -6.725 | -43.7915 | 2025-08-08 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 0f96826b-9253-3047-a5f2-e48bbe3d86e7 | -10.625 | -44.7439 | 2025-08-08 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 205fa3e7-3509-36f5-874c-497e909ea29a | -8.9213 | -60.7489 | 2025-08-08 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 89239509-b27a-31e2-8d26-a223337b65d3 | -10.6247 | -44.767 | 2025-08-08 03:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ae9bb13d-36f1-3807-9a58-ec253d2d5b0b | -9.6063 | -40.5902 | 2025-08-08 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 25862a29-e6f0-3f91-b98c-3ef7658f0bac | -9.6254 | -40.5875 | 2025-08-08 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 134.7 |
| 4e26279d-4af9-38a1-a8cf-97258c8355ea | -7.0615 | -59.1779 | 2025-08-08 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| ed0e0884-d43f-39e1-8f27-603e49e1fed2 | -7.0616 | -59.1586 | 2025-08-08 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| f01ebb59-a043-3acc-8f35-d9047ba57db6 | -7.0429 | -59.198 | 2025-08-08 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| e71afa75-ecbd-397f-a9ae-bb32fdce8cb3 | -12.5714 | -47.1584 | 2025-08-08 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8cb1ab6c-ca31-350a-b614-25b10ffe9d6b | -7.0614 | -59.1972 | 2025-08-08 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| fcfe50c6-4653-3b4e-91f8-e8e3ed6ace17 | -7.0801 | -59.1578 | 2025-08-08 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ec077c05-37d1-3e41-a5ea-4e224e6ecc80 | -7.043 | -59.1787 | 2025-08-08 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| c6b82e6b-fa4e-3263-ae57-1eb189715e6c | -9.6254 | -40.5875 | 2025-08-08 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.2 |
| e8eeca97-7571-3b75-b601-496688ebc563 | -10.6247 | -44.767 | 2025-08-08 03:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| fce94c63-e37b-339c-b781-1ff2d2f30161 | -8.9213 | -60.7489 | 2025-08-08 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e366ac21-f779-3f13-80a1-43415cb19b75 | -3.66382 | -41.76276 | 2025-08-08 03:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 53baad00-13e1-3dcb-8bfb-70dc2d6fff44 | -3.66501 | -41.75598 | 2025-08-08 03:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bff88d3e-7608-37c6-b095-8acc89d87f35 | -3.6681 | -41.75774 | 2025-08-08 03:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3c1c1882-7354-3f4e-b298-153c541047fa | -3.65676 | -41.7614 | 2025-08-08 03:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c6226e7-2626-32bc-bd83-c8beadc6fc9c | -5.16253 | -37.9831 | 2025-08-08 03:17:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c5f26871-fd69-31a5-8ea1-7b9524f39461 | -3.59043 | -41.65754 | 2025-08-08 03:17:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a50efc65-0f63-396f-8c20-fd7d77716488 | -3.67203 | -41.75755 | 2025-08-08 03:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05ed3e94-d3da-3e19-9dec-940e4b2f3895 | -5.51416 | -35.58137 | 2025-08-08 03:17:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c9fa27d-24d2-3467-8f82-2742b5058a65 | -5.16191 | -37.98664 | 2025-08-08 03:17:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bbe0ee9a-3e53-3d62-8ed3-d73f8e4b826c | -5.50158 | -35.48606 | 2025-08-08 03:17:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25da938c-5c3b-3f55-9936-51901742058f | -6.2308 | -37.42628 | 2025-08-08 03:17:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbefebf6-a149-3bc2-97fc-ca5b7c2d828d | -3.58342 | -41.6561 | 2025-08-08 03:17:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16713987-924c-3fc9-b2aa-36665d7361f8 | -5.5131 | -35.57849 | 2025-08-08 03:17:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0ce88fb-8139-3377-aeda-d6e45c08db0b | -6.55925 | -39.01395 | 2025-08-08 03:17:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 102a38f0-f605-3f6a-8c6c-2bec4cca4b86 | -8.52621 | -43.30883 | 2025-08-08 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 323a4472-8a18-3b29-a4e2-3bd15693e106 | -6.96112 | -42.86261 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4303b626-1572-344d-9175-1fd098e9988d | -9.61862 | -40.59954 | 2025-08-08 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 267d9a2e-927f-3bb7-8382-34fdc700f8af | -6.96827 | -42.86403 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bf6d38e3-80c0-3b4c-9837-0d27545b10e3 | -9.33357 | -37.98582 | 2025-08-08 03:19:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dc656995-3a16-311c-8418-4c01f793b685 | -9.33413 | -37.98281 | 2025-08-08 03:19:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4c90ba96-ba62-3c97-b06c-e4ec1df0266d | -6.96555 | -42.87793 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| dca8a033-8530-3269-a137-b216aa82848b | -6.96473 | -42.8703 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| d8a98c82-9db4-355c-9683-e40d4b309026 | -8.52282 | -43.31773 | 2025-08-08 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f676eeca-646f-3de0-a3bf-cf099db59a9b | -9.6255 | -40.59618 | 2025-08-08 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 47.8 |
| e9bdcb79-3817-360b-8427-411a899bc97a | -6.97188 | -42.87176 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c3196ce-12bd-3cc5-8855-4551e30bf384 | -6.96342 | -42.87723 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 0c3759ec-f000-3685-8cfd-66244fa19830 | -8.52478 | -43.31595 | 2025-08-08 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2cda4b5c-4c09-3522-a191-83ad526e79db | -6.97055 | -42.8788 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce345891-e8ae-37b9-bf58-95a1bf51cdd5 | -9.62037 | -40.59041 | 2025-08-08 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 25f9122e-5280-39ae-a84d-8ecbfcdb089a | -6.95975 | -42.86956 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 67a022bd-00bb-33ab-9bfb-29f3b8514236 | -9.65561 | -43.84818 | 2025-08-08 03:19:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b7262c8-3223-3d28-b1f5-aea5b40b537a | -6.96691 | -42.87099 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5349778c-38d2-3967-b2da-c8020f0ca6e9 | -7.39628 | -39.67999 | 2025-08-08 03:19:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bdff33ad-57b2-3a9f-bc03-0072cf3ffbc3 | -9.65391 | -43.85634 | 2025-08-08 03:19:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2186b472-8e38-3104-8bb6-9199a72c7754 | -6.96606 | -42.86332 | 2025-08-08 03:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e0a17abe-ed92-35a6-b246-1d9e0fa2df9e | -9.62124 | -40.58585 | 2025-08-08 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b49fa35d-955e-31f6-b979-5aa1c607f5cb | -8.5242 | -43.31059 | 2025-08-08 03:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 334ce236-fcef-3ff6-82d5-9a2b3bf7c208 | -9.61949 | -40.59497 | 2025-08-08 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 47.8 |
| b98127f9-846f-394a-9e14-fa8e3d76a9ee | -7.0615 | -59.1779 | 2025-08-08 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 54512fa7-eb76-3e9e-88d0-3482e0c7fdcc | -7.0616 | -59.1586 | 2025-08-08 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 4fdb22da-c42d-3067-b489-c77c291a3528 | -7.043 | -59.1787 | 2025-08-08 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 77d83898-e506-31c5-8075-5e2a454e4bca | -7.0429 | -59.198 | 2025-08-08 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 138f87a0-5b03-3060-8c03-6929ea43bdbc | -7.0801 | -59.1578 | 2025-08-08 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3b5c07ec-0808-30e8-9d43-bb408877a694 | -8.9213 | -60.7489 | 2025-08-08 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b7e6c283-7939-3e0a-88b5-58e3400324a8 | -10.6247 | -44.767 | 2025-08-08 03:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 83207f00-d823-3743-9131-02a437bbbf57 | -7.0614 | -59.1972 | 2025-08-08 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ead0f4a3-7e9d-38ac-8547-07b3c9ab2b1f | -18.85697 | -45.13398 | 2025-08-08 03:21:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c711545-3318-312c-b301-2deff9656b5c | -18.62042 | -44.26637 | 2025-08-08 03:21:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 800ef9ab-8d70-3be7-8665-02f0f1725d74 | -15.84075 | -41.85267 | 2025-08-08 03:21:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83bc7cea-4fa2-3cd7-aaa5-6c8ca5ba9385 | -19.95475 | -45.18092 | 2025-08-08 03:21:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ff7ed8d-e013-3065-9796-cf3072c79d50 | -17.68569 | -42.40864 | 2025-08-08 03:21:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b964c6f-114a-3ad3-b437-42c5da6dfd36 | -18.76309 | -40.99664 | 2025-08-08 03:21:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b50e37eb-645f-357e-bffc-1e715670be07 | -19.19344 | -45.05381 | 2025-08-08 03:21:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fd3367a-38d7-3001-b3eb-d4e13c1ee940 | -18.22128 | -45.63308 | 2025-08-08 03:21:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0126a7ec-b9a8-3b59-aefa-786a3fc2865b | -17.65764 | -42.51082 | 2025-08-08 03:21:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 297c14dc-3a0f-3ac9-b7a3-8a3f6ec56242 | -19.22572 | -46.58223 | 2025-08-08 03:21:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d1f28b9-324c-36ea-8a6c-418891427ffb | -19.94826 | -45.17922 | 2025-08-08 03:21:00 | NPP-375D | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 233abfde-5be7-3562-930f-2878b75c60dc | -15.83492 | -41.8515 | 2025-08-08 03:21:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84de5d46-d058-34c1-ab74-84ac3ee9cbff | -20.57263 | -41.72226 | 2025-08-08 03:21:00 | NPP-375D | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab1769b7-3812-3b45-86ef-43ecc30f8907 | -18.91329 | -40.61297 | 2025-08-08 03:21:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f0e93cc3-c632-3568-a7a3-196492684573 | -21.00295 | -43.27783 | 2025-08-08 03:21:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 794ae351-aafc-34ef-8a03-a0668ff339de | -17.23015 | -39.28287 | 2025-08-08 03:21:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 532ca070-0435-31c1-9b0b-a5fcb9d42499 | -19.22334 | -46.59182 | 2025-08-08 03:21:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8542b09e-4f13-31bc-889c-a3edfbd34fc7 | -16.88808 | -42.06643 | 2025-08-08 03:21:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d69d3df2-7e1e-3c78-a299-b1b15f3bea10 | -18.22298 | -45.62589 | 2025-08-08 03:21:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abf26381-f3f7-387d-b394-c058fde6abc6 | -16.88231 | -42.06512 | 2025-08-08 03:21:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 29dec42c-6329-377b-bb9c-5f1976a6e0ae | -19.18684 | -45.05239 | 2025-08-08 03:21:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61fd6b19-ce62-3051-b418-0af472d1eea9 | -15.90062 | -40.02806 | 2025-08-08 03:21:00 | NPP-375D | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20939b85-d3e3-3f53-a249-de33fc48c17e | -17.65678 | -42.5148 | 2025-08-08 03:21:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78697958-27d1-330a-b36e-4c9419ea1bf2 | -18.76268 | -40.9967 | 2025-08-08 03:21:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4fe343fa-f77e-33d7-8b31-e89de90e5074 | -19.22882 | -46.58993 | 2025-08-08 03:21:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a30ba9f-8d97-3da3-ac01-74b4f495d2e7 | -22.22332 | -44.73242 | 2025-08-08 03:23:00 | NPP-375D | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 979e4709-e334-3101-9c3c-cc8781e12644 | -22.22225 | -44.73692 | 2025-08-08 03:23:00 | NPP-375D | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| eaf6860d-511e-300d-9af5-ebd495606ad9 | -8.9213 | -60.7489 | 2025-08-08 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1a586d10-2bd7-3a61-ba5d-d73a589a5f32 | -10.6247 | -44.767 | 2025-08-08 03:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7039bd99-95a6-3913-9c42-302deea5a97d | -9.6254 | -40.5875 | 2025-08-08 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 4859f8ac-81f7-3b9e-8733-befc23bf09e6 | -10.6247 | -44.767 | 2025-08-08 03:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ee29bab5-5d69-3247-b533-549e73a96c23 | -7.0615 | -59.1779 | 2025-08-08 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 73efcd70-32ad-376c-aa67-16cd63c224b8 | -8.9213 | -60.7489 | 2025-08-08 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ca6e6f17-a9d0-3f0c-96ad-f3dedf1b9601 | -7.0614 | -59.1972 | 2025-08-08 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 57118861-0176-3187-bede-b4eda2a3bb74 | -7.0801 | -59.1578 | 2025-08-08 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c61f86f5-1992-337e-8af3-803e8ded2602 | -7.0616 | -59.1586 | 2025-08-08 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 79f192cd-591b-348e-889b-28fbf241c360 | -7.043 | -59.1787 | 2025-08-08 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.1 |


[Clique aqui para ver as próximas entradas](README7.md)
