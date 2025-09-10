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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3d8a273-b600-32b0-864f-87cf4391a440 | -17.40723 | -49.88855 | 2025-09-10 04:44:00 | NPP-375D | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 491835c3-1cb6-3854-85ba-34dad01a7880 | -15.95627 | -50.23089 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 808e012c-9a6a-3202-ba8c-7a2fe1e05be8 | -13.54117 | -44.13724 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d11c1601-1e8b-3916-bd77-7fc9fa8664ba | -14.3528 | -47.30567 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a84cc919-f44e-3bf6-8211-481e960ed758 | -13.12852 | -54.9212 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f24ebae0-637f-353c-a5e2-fa6c280e00a3 | -15.94988 | -48.10903 | 2025-09-10 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7239a6e8-7261-3349-b94b-af9c3eeb6ced | -19.91783 | -46.15835 | 2025-09-10 04:44:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9900a39-536d-306e-977d-1a63bab0093f | -12.06595 | -51.06379 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ae8e165c-f459-3baa-b778-dda503650526 | -16.67064 | -48.52234 | 2025-09-10 04:44:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9778dcf7-466b-3ef8-b312-14293e7bca17 | -14.89023 | -55.85997 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81be54a3-d917-398e-9aad-dba4dc90b060 | -12.95597 | -54.75624 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6af4ef6d-f4f7-3147-a864-38d7d27106d3 | -11.29667 | -53.95328 | 2025-09-10 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2fe35b0-7ba4-31a2-b395-69036abcfcc1 | -16.8823 | -45.75742 | 2025-09-10 04:44:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e9d4cd7-b4ec-3114-ac14-ca42fea2463f | -12.06816 | -51.07141 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b3e029e0-3a21-3a79-b942-1d47e0b2fa6b | -13.94607 | -48.25731 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54fb5fd5-ebb1-3c4b-9e32-50c999cb1c37 | -17.58192 | -49.81843 | 2025-09-10 04:44:00 | NPP-375D | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e8985ff-c6ce-3c4d-b7d8-2bb4ede3231b | -12.76132 | -53.9945 | 2025-09-10 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| adb0b0d8-3089-3419-8b94-a7fecceef3b1 | -14.37097 | -47.31325 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a96cbccc-b86c-391e-9813-c1c06a4998be | -13.22727 | -51.77458 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de00dc06-d194-3311-b825-35c65ea768cd | -18.4495 | -49.56688 | 2025-09-10 04:44:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eef33206-7490-3315-a65d-e9f191b27a69 | -12.04602 | -51.03872 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 557f3b77-5acc-3eaf-a4c4-c0d8dc6ddcbf | -12.92443 | -54.75999 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9a2b8266-695c-3b31-ac0c-5275779946b9 | -13.14971 | -45.28546 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86712347-f5fc-3d8e-9ce8-bd09f4c7633d | -15.47533 | -49.3761 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1e06e06-b743-3ae2-87fa-954aeb7f3b67 | -15.81441 | -52.22982 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f3342d5-3143-357c-8de2-f2bcad2b4fbb | -16.51588 | -55.13922 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 77997031-220b-3ba7-883b-9b2a59de1a5d | -16.45763 | -50.6703 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7bb62af9-bf97-38eb-8a06-38ea74244a9b | -16.62954 | -51.82619 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c7067bb-8f38-3192-ac9c-d9d18644df93 | -11.6011 | -52.2126 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94930db7-a033-3916-826e-0548b2b37c0a | -14.0561 | -49.68742 | 2025-09-10 04:44:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0cf3e5c7-421a-337b-a488-ea11f594ad97 | -13.12769 | -54.92591 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6d0f26b-caee-3181-be44-08a5a174d329 | -12.55433 | -49.1343 | 2025-09-10 04:44:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e4ad740-6981-325a-bed1-4a3ef262f7d0 | -15.8436 | -52.27222 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baf5f454-b6fe-36a0-94b5-e4b024190bdb | -15.87468 | -52.20712 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc950e33-83a7-360f-97e0-67cb79ec90b3 | -12.69018 | -44.96944 | 2025-09-10 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 893b6372-ad98-3df2-8250-1860e8760da0 | -18.02651 | -47.1481 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 54839542-b844-354e-9026-b071a21baf68 | -15.52567 | -48.37583 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 927d81eb-6b9a-37d4-8709-0e4cece2c6b0 | -14.78169 | -48.22631 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49127ede-aafd-3583-a1a5-cf6f84e30643 | -17.0643 | -49.67332 | 2025-09-10 04:44:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5040176e-e33e-399c-ad63-8680b78a2f24 | -15.01517 | -48.02451 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74702373-995e-30f0-b01c-ffe0a1de8732 | -16.28461 | -45.68627 | 2025-09-10 04:44:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70427b12-e68c-34e4-a999-300c4ea4b7fd | -15.70043 | -49.8966 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b102c1d-1bed-3d62-814b-64e2ea414742 | -16.39031 | -46.87925 | 2025-09-10 04:44:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba483ce5-3a2e-36a5-b33e-acb77b5285b1 | -15.66603 | -48.12228 | 2025-09-10 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd315d0d-dfe4-397c-869d-618efde0dd88 | -15.51162 | -52.76406 | 2025-09-10 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11d8d6a8-de1a-390e-badd-0c38955e1071 | -13.28667 | -51.72563 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5fb282e-d47f-3f4f-964c-0fa9862404b7 | -15.09258 | -50.06894 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f69b1f7-5b53-37a3-b854-aef32b491887 | -17.30301 | -46.75399 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 940e04b7-5bb0-35df-92a9-5524eae36e39 | -18.9579 | -42.39367 | 2025-09-10 04:44:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fca4c93f-6398-304b-99d9-161963dceb4c | -17.20232 | -50.17071 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cea7de8-4888-3d66-bb3e-91117d139c86 | -16.46028 | -51.97555 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff512b32-88c2-3cfc-b96c-3b0eb1e84472 | -14.88932 | -55.86498 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 485787e8-0fba-3c79-a9fd-bc4f004d0c2f | -13.29116 | -51.71903 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3bd1152-23ad-39c0-9be5-a109f3ec1672 | -14.55784 | -52.16676 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aedd0d56-8a2b-3574-bca2-92cceee5822e | -16.34885 | -52.94493 | 2025-09-10 04:44:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dbb0783-7cbf-323a-84ac-dc2eeb2cdaf5 | -16.88282 | -45.75324 | 2025-09-10 04:44:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f2b6a0e-25ff-3859-bd8c-4cb1516de26b | -15.79915 | -52.26077 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63095252-bf25-3801-afeb-9a94098b27f7 | -14.38899 | -47.32178 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4dc59165-5a83-36f5-a42e-c0f2f92fe3f0 | -15.13045 | -52.40141 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed232d7a-285e-3628-9745-10ab661aa786 | -18.34241 | -49.33529 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e36df22-421a-3e07-8405-fcb32c2bdd4e | -13.9705 | -48.23989 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 374f49dd-5a48-3352-8d9c-5d868a341649 | -13.79016 | -46.29172 | 2025-09-10 04:44:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5dc9d2ab-38c5-36a0-a95c-1d78ecf80435 | -11.29006 | -53.9477 | 2025-09-10 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 864712f5-93ad-32f0-95e4-f505dcccd0ce | -15.80425 | -52.25041 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d024f0df-9fbf-3def-8006-1213bfbcfb77 | -15.80976 | -52.25883 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f54bc3b2-70d6-3dd2-8c80-d3ceb1ee9d41 | -12.89916 | -47.97945 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8925ee23-01c5-38c7-b4c3-698f1195f1df | -13.97887 | -48.23262 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5679071-936a-3b57-b932-19c1a312c500 | -15.09376 | -50.08403 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4425dc93-20af-327b-9dd7-aa9619554067 | -15.14008 | -52.38451 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6e00eb5-b53c-3a27-b7d6-85f56b73181c | -14.46269 | -53.27346 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ccf6759-9975-39e4-8d4e-38ea575a72a3 | -13.19322 | -51.77258 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e124d9e0-d9ed-3990-bd99-72c9192b36cb | -14.90695 | -50.11937 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f07d433-b258-3535-9b0c-c09cd2746e60 | -19.63869 | -45.04425 | 2025-09-10 04:44:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06634ea9-bd58-38ad-83a3-e082607060bc | -14.31225 | -44.87587 | 2025-09-10 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e6fa487-5f0a-3329-8da5-b9872f056cf1 | -15.81775 | -52.23038 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ada5ca9f-aab2-35b5-a66a-f7813261a5ab | -13.94015 | -48.25819 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92960f2c-33d7-3bfb-8f56-f5d5df8d3cc5 | -12.9477 | -54.75945 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c16e0eb-2355-3dc5-9490-f87f574faeb9 | -12.94722 | -54.80681 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b99663e-16b5-37dd-8597-78d95e4019bd | -15.13104 | -52.39778 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39485752-aaac-3664-ba7e-496db3dd5318 | -17.33319 | -46.7128 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae677d17-d339-3915-a7ae-5f9e126d3c58 | -12.60348 | -56.9704 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 547330dd-2413-33b4-8bdb-e21d48eb938c | -15.80657 | -52.23599 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34c87f7d-321d-3513-9857-dada46f76580 | -14.92439 | -50.11839 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 619108c5-d2cf-368e-92a3-0ba2630931ed | -12.82706 | -52.93787 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1f40854-ba27-3200-ac78-c2ea2d40b4f0 | -15.25961 | -53.77332 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34a3924b-a3a5-3e54-8c6e-3f871f357fd3 | -16.61982 | -49.75832 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 828ff89e-cde0-3dd8-8d86-a65167d6820e | -15.90355 | -50.18858 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c634ee6-055f-3c4b-8f68-9da22ecfb962 | -15.27633 | -53.78044 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6b4445a-eb70-3d55-9c2d-60d825daa868 | -16.61746 | -49.77406 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac92aca-b94c-3e6f-a878-36a33b7e4e98 | -15.51777 | -52.76893 | 2025-09-10 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ed898d2-7b29-3444-8ec3-ce25b6907731 | -14.29811 | -49.14433 | 2025-09-10 04:44:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3cc58c5-d0d5-33b0-9153-5ddaf4d87f19 | -16.3965 | -46.87627 | 2025-09-10 04:44:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97791baa-2674-3bea-a1e3-dbc0b04f12fa | -18.35247 | -49.34138 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef7b7711-ac57-33b1-b1a9-7efbbfc4abb0 | -16.67704 | -49.39706 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49a4df03-b88d-3e20-b558-4c79d2b52533 | -11.93795 | -51.07927 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f53ad7a-ecad-3a48-90d6-73fdc311538e | -12.3518 | -63.64679 | 2025-09-10 04:44:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3009922a-c6d5-36ef-b284-1e640f911751 | -16.46156 | -50.66717 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f48b02a-4459-35ca-bbb6-05f084df635a | -12.00202 | -50.97725 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8a19864-9214-3df9-86da-27ebaef3538e | -12.9927 | -48.02855 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a9559cb-206e-3a89-96a7-2683739db88b | -13.87684 | -44.45421 | 2025-09-10 04:44:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README77.md)
