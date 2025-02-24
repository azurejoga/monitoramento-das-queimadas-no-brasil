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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 201b06c8-4e68-3e92-b74c-4d354da71350 | -22.90078 | -43.75229 | 2025-02-24 04:29:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ad60d34d-979e-373d-b03d-91e8324cef2e | -21.08741 | -54.18983 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09c8c2f3-0887-3cb9-b18d-c27688e4f459 | -18.96538 | -47.2122 | 2025-02-24 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e8d33d2-f768-3f37-837c-d64c023aa51f | -18.63409 | -48.24427 | 2025-02-24 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 646b3919-7846-3011-b1d2-1c35f2e42c3a | -20.30783 | -46.47054 | 2025-02-24 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a403b258-956a-3463-ace1-6c4ed4b0904a | -21.08671 | -54.18769 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ce6c1f49-02b0-3eef-bc35-cf6933644cab | -21.09121 | -54.19064 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 766fa23a-37f6-30cd-8093-724061330453 | -21.19459 | -44.93493 | 2025-02-24 04:29:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0cd3f8e7-946b-3ba4-9127-802cf5a63952 | -20.00723 | -45.40696 | 2025-02-24 04:29:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0129a054-370b-3db3-8945-fca0405a7616 | -20.55213 | -45.93395 | 2025-02-24 04:29:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8144c238-5c3f-3bd0-a9f2-94d1a8285351 | -20.72034 | -54.60646 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b11744c9-4dc5-314e-8c5d-abc3c451cdb3 | -20.37725 | -45.60518 | 2025-02-24 04:29:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12c67cd2-6ec7-366a-8db8-6c992a246aad | -20.7254 | -49.43471 | 2025-02-24 04:29:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 055eea7b-b14e-3344-8c58-f796086ffdac | -20.5527 | -45.93217 | 2025-02-24 04:29:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2976c752-5188-3bb7-8705-df3be14fe8be | -22.85628 | -42.97997 | 2025-02-24 04:29:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a17ef84c-19b5-3ba2-ad28-52872546ccfa | -21.09051 | -54.18848 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 625c7ed4-9d43-3857-aef1-24b060c9ca39 | -19.7677 | -41.99299 | 2025-02-24 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fcc2e2fd-bcfb-332a-96f1-5a6c035fde69 | -21.298 | -48.61743 | 2025-02-24 04:29:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea20d505-5b3b-30e2-a7f5-2eabfe904733 | -21.30135 | -48.618 | 2025-02-24 04:29:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 28441a27-8083-3c53-81a2-004fa553361b | -21.0865 | -54.19485 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8852521-6ed3-3bdb-8f89-a3783b8bf5ff | -20.29949 | -46.47832 | 2025-02-24 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5810a8fc-187a-3479-a68a-fc98489b3361 | -18.81914 | -43.21094 | 2025-02-24 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f37ab93-939c-32d7-af5c-89464681b2af | -20.41599 | -43.55259 | 2025-02-24 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 194be44d-47d6-3a09-9cde-82a21f71c977 | -20.76462 | -46.76887 | 2025-02-24 04:29:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e616e09d-3a22-3cdf-bde0-a092cfd22bfc | -19.66434 | -46.06779 | 2025-02-24 04:29:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf97471f-d823-3a08-b837-fac7b4692a8f | -20.00661 | -45.41171 | 2025-02-24 04:29:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 94d559d5-d97b-388b-9f76-121b97afa938 | -21.08957 | -54.1935 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffd72096-de68-390f-b1eb-d2a8fcbc7d58 | -22.78438 | -43.75673 | 2025-02-24 04:29:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0bb8c103-5d3a-3ca1-9980-45eea2708f05 | -18.96522 | -47.21318 | 2025-02-24 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73154c09-f835-3c1e-a21e-2de04c7e56bb | -21.08577 | -54.19269 | 2025-02-24 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82213346-8d1c-346a-9904-e91fc0e61b3b | -27.07227 | -49.67253 | 2025-02-24 04:31:00 | NOAA-21 | PRESIDENTE GETÚLIO | SANTA CATARINA | Brasil | 4214003 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| edc93b55-08f8-3545-9eeb-6a9d365751e9 | -28.58763 | -49.44162 | 2025-02-24 04:31:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 124a9a83-edaa-3562-b58d-ad320aabe514 | -24.24213 | -50.73919 | 2025-02-24 04:31:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 73247b8a-bbd8-33b4-9c0c-8795251e46f6 | -23.44375 | -47.41125 | 2025-02-24 04:31:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 64dd4aba-a0e6-3a0a-98eb-17703f4ab867 | -28.67975 | -50.24231 | 2025-02-24 04:31:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ba09df6-d6bc-3007-bf6d-321096e60a59 | -23.98565 | -48.91573 | 2025-02-24 04:31:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a3b2772-5eb9-31e1-86d5-27af8344bbc6 | -28.14813 | -54.7171 | 2025-02-24 04:31:00 | NOAA-21 | CERRO LARGO | RIO GRANDE DO SUL | Brasil | 4305207 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32403f14-9ec4-3c84-b8aa-f12900e9fcdc | -26.20844 | -48.83604 | 2025-02-24 04:31:00 | NOAA-21 | JOINVILLE | SANTA CATARINA | Brasil | 4209102 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1775ac1d-2266-3e99-acca-b6521a8e4091 | -23.59501 | -47.43923 | 2025-02-24 04:31:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b1903b3-a414-39bb-bbc8-140f5d3c8645 | -29.70488 | -56.16193 | 2025-02-24 04:33:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ea4985cf-25bc-3598-9395-b2c15d850011 | -29.70119 | -56.16105 | 2025-02-24 04:33:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 4a032235-6573-3604-934f-758961fc9322 | -30.15051 | -52.0241 | 2025-02-24 04:33:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| c1322072-822b-3e91-b395-ad6072289f5f | -29.70278 | -56.16357 | 2025-02-24 04:33:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| ce6700e0-03b2-33f4-ba87-c69dcf2857e6 | -30.2728 | -51.51805 | 2025-02-24 04:33:00 | NOAA-21 | GUAÍBA | RIO GRANDE DO SUL | Brasil | 4309308 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| fda32909-05df-3fa2-9c3f-23ff4a0a033f | -30.27489 | -51.52144 | 2025-02-24 04:33:00 | NOAA-21 | GUAÍBA | RIO GRANDE DO SUL | Brasil | 4309308 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 039fad27-4bdb-34da-82c2-aca4e0cee14c | -14.9698 | -57.81968 | 2025-02-24 04:53:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67f90ca6-b636-3e2b-b108-8f5e56290880 | -16.68063 | -43.88923 | 2025-02-24 04:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bbe4407-7a2a-3134-a489-6c5fea51bee9 | -16.68117 | -43.884 | 2025-02-24 04:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1e2f881-8d94-3b20-b33c-86830e00f7ad | -20.41678 | -43.556 | 2025-02-24 04:55:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82d40364-49e2-35b9-9df3-b69ec751ef9a | -20.41724 | -43.55077 | 2025-02-24 04:55:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8c4a96e9-a66b-3c3d-a08b-5042ae768683 | -10.60087 | -52.84835 | 2025-02-24 04:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23bcd81e-210d-30b1-a16d-af6853a3a316 | -20.72143 | -54.60521 | 2025-02-24 04:55:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2d4d508-5c13-3d8f-94b8-920976b31048 | -20.30137 | -46.47786 | 2025-02-24 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59323cfb-25f1-3eb9-a8bf-3671b8c9159e | -20.3017 | -46.47459 | 2025-02-24 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8c0792b-94ac-372d-a1e8-7ed0124d923d | -21.29731 | -48.61909 | 2025-02-24 04:55:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 14537d81-2ac7-3cc2-ac25-b895fab47d2a | -19.02299 | -57.62356 | 2025-02-24 04:55:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9385304f-726f-31a6-b1d2-dc25ad84427d | -21.08529 | -54.19205 | 2025-02-24 04:55:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7fec4512-50b2-36fd-9355-dd17bf341a30 | -21.08872 | -54.19261 | 2025-02-24 04:55:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 35dd2b85-4157-3b33-aa23-bd7c5cacb6b2 | -12.3291 | -52.4786 | 2025-02-24 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34f3a2e5-a389-3702-9370-b3fa83192e24 | -20.55046 | -45.93176 | 2025-02-24 04:55:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 173a9af2-eb54-3be4-9b98-bd9a41c18a82 | -20.3075 | -46.4706 | 2025-02-24 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7533d38-9572-3ad6-b0af-cd9c66454da1 | -21.29858 | -48.62049 | 2025-02-24 04:55:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5ac33717-d44f-332d-a37d-d2e5145d36bd | -10.60032 | -52.85191 | 2025-02-24 04:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0e4c8da-4f4c-344e-a350-fe0a3574890c | -29.7033 | -56.16105 | 2025-02-24 04:57:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 0c91eabf-bcff-366b-8292-72a43e7e54dd | -25.19932 | -49.32215 | 2025-02-24 04:57:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8ca0af1-37f6-3930-96de-ec21ab366910 | 3.98677 | -59.87313 | 2025-02-24 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8df0579d-b796-3e76-b4a6-43f160088716 | 2.98552 | -60.86536 | 2025-02-24 05:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50e271a1-51a9-344e-80aa-bdf04c646ba6 | 2.98489 | -60.86279 | 2025-02-24 05:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d46f4f90-ee34-3158-8b98-9de59809b3e3 | 2.72278 | -61.1754 | 2025-02-24 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d8f5c6f-4b25-3ff9-bf31-932796044d1e | -12.02129 | -64.04646 | 2025-02-24 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71d5234f-0dae-3046-8630-570028b8c07b | -14.9683 | -57.81839 | 2025-02-24 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6a9f9c70-32b3-332b-9a15-5800dd0dfa22 | 4.36018 | -60.64406 | 2025-02-24 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c9920db-933e-3189-9124-cee80425805d | 4.35504 | -60.64482 | 2025-02-24 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8df0d7c0-c710-3047-a9e8-7411df7a59e9 | -5.80995 | -35.21009 | 2025-02-24 11:57:00 | TERRA_M-M | NATAL | RIO GRANDE DO NORTE | Brasil | 2408102 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 7d81b01c-a1bf-380c-b6da-17520c606900 | -9.59934 | -36.97657 | 2025-02-24 11:59:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 7d8a53b2-7fc0-3ad9-a4a4-ad37edca9225 | -8.095 | -38.85199 | 2025-02-24 11:59:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d5147f72-9416-3a32-9023-83868ebcc8a0 | -9.42371 | -37.30673 | 2025-02-24 11:59:00 | TERRA_M-M | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 523d68c8-cc61-335c-804c-4dc3d290d49c | -9.55167 | -36.59338 | 2025-02-24 11:59:00 | TERRA_M-M | IGACI | ALAGOAS | Brasil | 2703106 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f39cf925-f65e-32f3-98c4-8f5e72659bb8 | -11.54138 | -38.55654 | 2025-02-24 11:59:00 | TERRA_M-M | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b18cc9c6-bf44-3a13-a33f-12ed50bfc109 | -10.6268 | -38.75522 | 2025-02-24 11:59:00 | TERRA_M-M | BANZAÊ | BAHIA | Brasil | 2902658 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 28444e27-f697-363e-b531-fd52b048c715 | -9.18687 | -37.61353 | 2025-02-24 11:59:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6f77eba5-c495-3a3c-b013-3bb1e2396db2 | -17.62196 | -39.80116 | 2025-02-24 11:59:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b252a5df-2a5b-3486-82cf-d70756511253 | -12.24146 | -38.81773 | 2025-02-24 11:59:00 | TERRA_M-M | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b0816b22-7ede-3c7d-9b69-b186234db6bd | -8.09369 | -38.86097 | 2025-02-24 11:59:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4ebf722c-b051-35aa-972b-0085a17a5d29 | -12.24275 | -38.80874 | 2025-02-24 11:59:00 | TERRA_M-M | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| da7df9f5-be79-3772-8e5a-7d7c5fb5be3b | -8.12249 | -38.66375 | 2025-02-24 11:59:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d935a22c-9875-344b-81c0-5010b234a4c1 | -8.12119 | -38.67266 | 2025-02-24 11:59:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5fdaae44-2138-398d-ab1c-f563ae0fed35 | -8.29949 | -36.58587 | 2025-02-24 11:59:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ded05e34-8939-3691-b37c-bf134a0fb557 | -7.86 | -38.82 | 2025-02-24 12:00:00 | MSG-03 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 363400e0-f59d-36de-9ce3-999ed41f6e5d | -18.64417 | -40.25962 | 2025-02-24 12:01:00 | TERRA_M-T | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |


