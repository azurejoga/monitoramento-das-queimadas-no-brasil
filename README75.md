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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b438aff-fd44-3305-805e-625b246dcb30 | -14.2373 | -51.9284 | 2026-08-20 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 49269693-a955-30f4-9da9-b49c0ec4c0a4 | -11.4418 | -47.2461 | 2026-08-20 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 92594524-b5b6-311e-8593-1119ade696af | -9.0349 | -45.8509 | 2026-08-20 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6f058502-d084-3a78-b12a-bb8a75a5778f | -6.8991 | -55.7176 | 2026-08-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 70f11ad9-e3b2-38c0-a45f-1baa94e8309d | -6.4392 | -52.7138 | 2026-08-20 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 683.3 |
| ad7a6c10-7075-38ae-b1a4-a4d51b506ff3 | -12.8366 | -48.4346 | 2026-08-20 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f8227232-17cd-3447-938f-aeff5d50e6c9 | -11.3801 | -46.3558 | 2026-08-20 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e50cc428-cea1-30a7-9a1b-49ce4506777d | -10.8265 | -50.2887 | 2026-08-20 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| d115915b-c80a-38c7-b022-e754415d349a | -6.6014 | -58.9844 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9c89b3b2-5943-3455-89c1-4cdbe13246dc | -6.6938 | -58.942 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1ffe8ff9-7b37-301f-ad69-588dd4ea7760 | -11.9099 | -50.1878 | 2026-08-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 806d213d-bad7-30c1-9240-af46fd326f38 | -6.6015 | -58.9651 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0e8e2d21-361a-3e0a-b877-c0c4d586e582 | -9.4256 | -60.4353 | 2026-08-20 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 157.7 |
| a650af78-8f42-3b9d-90fd-028723e1b71c | -13.4117 | -54.3737 | 2026-08-20 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b0424ac6-d052-3d29-8af9-93a45088dcae | -6.7647 | -59.4601 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0eceb1cf-6854-38b9-becf-458f45a66a9d | -5.7903 | -55.7301 | 2026-08-20 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7f509cc9-a412-32ec-bab2-c498e075e8cc | -5.6024 | -45.6815 | 2026-08-20 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f9b28334-e10c-3f62-a773-459510e90381 | -9.2256 | -59.7894 | 2026-08-20 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 54299d2d-cdd6-3405-85cb-5aea5f819a1e | -9.2071 | -59.771 | 2026-08-20 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 167.3 |
| 83b2c072-4d86-3320-a7bf-bacb5a0f6c3f | -10.3898 | -61.1925 | 2026-08-20 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| fec5dc2a-6b23-3bd5-bd34-25a8e80e5cee | -9.2258 | -59.77 | 2026-08-20 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 1ba5ebc1-f343-3977-b58a-9ac5325352a2 | -6.7123 | -58.9412 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| e952d7df-92ef-3445-9897-5a36abcdc9b5 | -8.2968 | -62.889 | 2026-08-20 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 08d3c79b-ef09-364b-9716-a84d3c9a3e3f | -11.8377 | -58.8445 | 2026-08-20 14:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| edf396cc-1b98-3503-a735-749688f7c6de | -6.6929 | -59.0966 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 688d4f29-4a61-3110-b0bd-05dd16075d49 | -6.7114 | -59.0958 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 411c936c-24ec-3fdf-962e-28ec2f79900b | -5.9425 | -52.2066 | 2026-08-20 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7a364e66-d006-320c-8ee1-8314274f05e3 | -7.4444 | -60.0092 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 0febb9e1-6892-385e-b19c-8bac967b21ec | -5.961 | -52.2056 | 2026-08-20 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| cfda29fe-561e-3e72-bbfc-c03e26018401 | -10.4085 | -61.1915 | 2026-08-20 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9daeede6-c457-3ad5-bfd3-88c350fc4a31 | -8.4087 | -62.7145 | 2026-08-20 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| db846b6c-ab32-3720-9576-7e1567aed50b | -11.9102 | -50.1663 | 2026-08-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 474e5653-7f95-3f43-8d61-cd54a20a0a0f | -8.4088 | -62.6956 | 2026-08-20 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.9 |
| b854de30-df70-341e-a484-bb2fc40615dc | -11.3797 | -46.3784 | 2026-08-20 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.7 |
| cb536789-474c-33c9-9bad-2e7d64a2a2fa | -6.4576 | -52.7332 | 2026-08-20 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a40d0fd2-98ba-3b11-b29b-9236c6c03c32 | -8.2967 | -62.9079 | 2026-08-20 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 382bb621-0952-3dcd-9e6f-3a15a547e1c7 | -14.3344 | -53.0372 | 2026-08-20 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5c197683-befc-3a6e-9fbd-f04573b52e34 | -14.447 | -52.0711 | 2026-08-20 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bda72437-63c4-3a31-a585-9bb9d14ac20f | -14.3335 | -51.9371 | 2026-08-20 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 5db3e40c-adc1-3e66-a9b1-55ce48f20dac | -11.4227 | -47.2486 | 2026-08-20 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 3adc1742-2636-345d-bda9-65fac01ec464 | -14.3347 | -53.0162 | 2026-08-20 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 159.7 |
| bfa5c24f-3103-3c96-a2b6-af4b37edad2f | -22.7796 | -47.509 | 2026-08-20 14:30:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.8 |
| 693aaa6a-41c0-3aff-9069-e0badec35d76 | -7.8674 | -63.7705 | 2026-08-20 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 074e2796-b0f9-391d-bb93-7a5e2e7ac7c1 | -7.7702 | -61.1634 | 2026-08-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| f33d59e5-4e65-3371-a87d-8979b2391036 | -12.7981 | -48.4399 | 2026-08-20 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 18fb34f1-aed5-3a00-9bb2-48c583ae6370 | -6.6745 | -59.0973 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 419ae3ee-f426-3131-8651-e22787f93dc1 | -11.2189 | -55.0585 | 2026-08-20 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| c8566230-2cfa-3b5f-b1e3-5d74a725e703 | -6.2353 | -55.4118 | 2026-08-20 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 8cd05e70-e00f-3525-8588-e16c6ed541b0 | -5.8087 | -55.7293 | 2026-08-20 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| d7114cc4-4e4f-3a27-92b8-a2b0e4a7bce6 | -13.3926 | -54.3758 | 2026-08-20 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 76693fc1-df27-3f4c-8a75-83af34f05df6 | -11.1747 | -54.0216 | 2026-08-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| a633b8ea-b3fa-396a-b2fd-6423f67b4dd5 | -10.4084 | -61.2108 | 2026-08-20 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 5ff33f73-ea39-3a15-9990-4c351f40805a | -11.2128 | -53.9976 | 2026-08-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 9768e076-08d6-3969-8a44-47d1c33bfe23 | -5.7904 | -55.7103 | 2026-08-20 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 0fe054b2-ed18-3b14-b4e1-5829d9d50978 | -11.1939 | -53.9993 | 2026-08-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 296.8 |
| 4990c662-983a-3cb8-bbaf-8fffe9f0283f | -15.7151 | -47.8036 | 2026-08-20 14:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 389fb29a-57a7-3a36-ba7f-11a3f5fd3b49 | -8.4088 | -62.6956 | 2026-08-20 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f14c954c-92ce-375e-adfb-2dc5f38a818d | -5.9425 | -52.2066 | 2026-08-20 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7c794b19-7e48-3a46-b7c6-4d5eade0cc36 | -9.2258 | -59.77 | 2026-08-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 14d6da0b-f21d-3e1e-9d5f-9d21b612f678 | -14.2376 | -51.9071 | 2026-08-20 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 2b76d982-35cd-3019-958a-bd964d16e80f | -7.7703 | -61.1443 | 2026-08-20 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 799b5f6e-5000-3618-a3d8-19537a8a746e | -6.7462 | -59.4608 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ad66690e-dad1-3647-a48e-66a728f315e6 | -9.207 | -59.7903 | 2026-08-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 532faeab-ee57-3ed4-95a4-e46e1e632f12 | -10.3897 | -61.2118 | 2026-08-20 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 9327949b-d3fe-341f-9611-654f81c9d944 | -13.7377 | -51.8864 | 2026-08-20 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 3514565b-00be-3600-b302-0f3e5e3eaf5b | -14.3335 | -51.9371 | 2026-08-20 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a312e057-37f8-3a31-9a3e-650200181b26 | -6.6145 | -45.4259 | 2026-08-20 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 8e92dc78-47d3-3d96-bd2b-ecfa5386f75d | -11.2128 | -53.9976 | 2026-08-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 9987e51c-8e23-3ae4-8891-f305d0747f63 | -13.738 | -51.8651 | 2026-08-20 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| f9577fe3-7ddd-3a12-99f6-59214ae40bbe | -6.7647 | -59.4601 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 7bae9020-3644-3785-b6b3-9a81bc2f7e20 | -10.3898 | -61.1925 | 2026-08-20 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| e4f437cc-af22-3116-b50a-ed3e832c006d | -8.3292 | -46.5077 | 2026-08-20 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e242e4cc-d7b0-3acf-b57f-6d359b10b70b | -13.4572 | -51.4324 | 2026-08-20 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e6130d21-e95c-3ce5-aeab-864bbdc09f46 | -14.5465 | -53.0317 | 2026-08-20 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d0ccbe87-6c69-3608-9d76-de676285115e | -9.4257 | -60.416 | 2026-08-20 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a960e34e-879d-355c-baab-29f694e7f7d6 | -15.0164 | -52.6749 | 2026-08-20 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a3dc94e7-7076-3408-8473-7d3e0a02b5c1 | -14.3347 | -53.0162 | 2026-08-20 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 5be14ba9-6869-396e-a206-1fa076b4099a | -10.7883 | -50.3142 | 2026-08-20 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 992caadd-60e8-3698-8b71-41261ec9c3ea | -6.6014 | -58.9844 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 00e721b4-c54c-32f9-8472-ae0df4e24c7b | -6.7114 | -59.0958 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c3b58a7e-bbd7-3515-83dc-b7267fc1be4b | -14.3537 | -53.0348 | 2026-08-20 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| ca1e286f-6271-3b7b-9b3f-7aff653039b6 | -6.6929 | -59.0966 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 7fe28b48-d53e-3b71-bf96-e8a6e33cb1bf | -7.8674 | -63.7705 | 2026-08-20 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e3b3a7c6-f00f-3bb0-a2f9-1e6421b6bab9 | -6.656 | -59.0981 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a6e35a80-6802-3a03-9abf-bbedb76cd8ae | -14.5275 | -53.013 | 2026-08-20 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 131.3 |
| acd5dd18-a0d9-387a-bc5f-cd0e954928aa | -8.9936 | -50.7215 | 2026-08-20 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b92dcad4-2965-3fb9-b868-fd0bc804c753 | -5.8087 | -55.7293 | 2026-08-20 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 6de5c2f9-6962-3562-9d00-2156cc78c70c | -5.7904 | -55.7103 | 2026-08-20 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 775f9546-8c8d-375b-b578-d321c6883966 | -6.6015 | -58.9651 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7feafb55-8317-3bce-bd71-0d477009cbc0 | -8.9748 | -50.7232 | 2026-08-20 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 59a08ec0-96c6-3240-b7b5-84705b2d8cf1 | -10.8075 | -50.2907 | 2026-08-20 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 0f887fcf-9bb8-3ea6-8ff7-5c4f9a431833 | -8.541 | -54.7793 | 2026-08-20 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 215c21e9-de19-324f-bb94-5c044f86d695 | -8.2782 | -62.9086 | 2026-08-20 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| faefe689-a532-3e97-8d39-07bc6b9b9074 | -6.6928 | -59.1159 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2de08bdf-0e27-35c7-941c-785b04f0d0ea | -11.2189 | -55.0585 | 2026-08-20 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 8e7fdf90-b092-3611-9079-752d100dd480 | -11.3797 | -46.3784 | 2026-08-20 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 4d0290ca-84ad-39f8-b0a5-e27621008063 | -9.2256 | -59.7894 | 2026-08-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 17470364-1477-3cc5-8322-9e9a3b0dec52 | -6.583 | -58.9658 | 2026-08-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 167699cd-3982-3598-aacc-b4692081bf84 | -6.2353 | -55.4118 | 2026-08-20 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 9b0a65da-810f-3c91-b335-26589a71f042 | -14.2369 | -51.9498 | 2026-08-20 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |


[Clique aqui para ver as próximas entradas](README76.md)
