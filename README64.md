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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c78dc966-04a8-37bc-9fff-8f6c68542e5d | -12.9736 | -45.1819 | 2025-08-20 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 733ff089-37c3-3986-a425-e3e7808eb1ee | -18.7575 | -45.0866 | 2025-08-20 13:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 103.9 |
| b8868a2f-6bca-368a-9043-2a4bd20015b3 | -11.3087 | -44.9264 | 2025-08-20 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 46e5a63a-dd4b-3f79-b65e-6aa1b74308d9 | -13.1367 | -54.9171 | 2025-08-20 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 5192b0e0-e8a5-36b2-a34d-934a34930a1f | -10.7043 | -48.2226 | 2025-08-20 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a9ced873-7fc1-31da-a33c-d9b7d6037767 | -13.1555 | -54.9357 | 2025-08-20 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| d5c233e0-9fdf-30b1-94a9-90c1ccf6a76a | -8.7945 | -45.4693 | 2025-08-20 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 36fde79c-fc14-35fc-a55b-d3af794a762c | -17.594 | -42.2745 | 2025-08-20 13:40:00 | GOES-19 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.7 |
| 770f3899-f7ba-39e2-8f22-a2248234da70 | -5.9711 | -44.1542 | 2025-08-20 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 226.8 |
| f397869e-4d6c-396e-aca7-720635a311d7 | -13.1558 | -54.9151 | 2025-08-20 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| f72b26a0-955a-31ad-b28d-b353474c2ee8 | -13.5743 | -47.0302 | 2025-08-20 13:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 190febee-1a76-35e8-b65a-f8dd98518090 | -13.1558 | -54.9151 | 2025-08-20 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| e098a0ea-2588-3e49-868a-f3f6d9547792 | -15.0196 | -54.8112 | 2025-08-20 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a47a5e16-d9d8-3b71-b098-e3efcde1cc7b | -13.354 | -54.4006 | 2025-08-20 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 5b5e7b52-b64d-32af-aff3-e7e7f236ad71 | -12.9732 | -45.2051 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 1a69b6bb-f602-32ae-a097-aecb7d28b3fb | -15.0002 | -54.8135 | 2025-08-20 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c272d6a3-e600-3ed4-be29-c3fdbe9e340d | -14.313 | -53.166 | 2025-08-20 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 4afc8fc7-96a7-3089-acb3-9ec99dba2332 | -14.9999 | -54.8343 | 2025-08-20 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 213482d0-b1ac-3e14-a325-339a14452c1f | -11.3087 | -44.9264 | 2025-08-20 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| fc49f2b8-614e-3306-aadb-b4a46d5d01ae | -13.1555 | -54.9357 | 2025-08-20 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 1b50953a-254d-3cfa-8dc8-fe1b29616b16 | -15.0193 | -54.832 | 2025-08-20 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7342d5ab-03ac-3fad-9691-26be16a67ceb | -13.3157 | -54.4047 | 2025-08-20 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2aa72cdb-9ef4-3e3e-97d4-03e7695ea167 | -12.9778 | -56.8614 | 2025-08-20 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 11930279-cf8f-3ea7-81ff-51c77403edcc | -12.9173 | -46.1106 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c470efda-02d5-3de8-981c-87c04a62c6b1 | -13.3537 | -54.4213 | 2025-08-20 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b273bff5-6c10-3f06-a679-30e8768e5682 | -12.9736 | -45.1819 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 0295b1ea-2b41-3933-a95f-fc038a3214c3 | -8.7945 | -45.4693 | 2025-08-20 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 5b7ae067-b18f-38a2-8f30-316e7d66bc98 | -12.898 | -46.1135 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 89a1ec0b-7416-3653-8f30-5743da6c430e | -9.2083 | -59.6161 | 2025-08-20 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 2c48e108-2330-36d9-90c1-3c6d4bf5b8a1 | -13.3346 | -54.4233 | 2025-08-20 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 397.4 |
| aa55cfe8-3500-3802-9f9e-e4722e1bc79f | -10.9919 | -45.613 | 2025-08-20 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 1d1d3521-ad9d-3a2e-b3d0-72afcfade008 | -3.982 | -42.516 | 2025-08-20 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| ffe86be8-0157-36f4-8b3c-6055fc6bdaba | -5.9711 | -44.1542 | 2025-08-20 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 276.5 |
| 99ae70e1-8251-3818-8c81-7268f747046f | -6.9607 | -42.858 | 2025-08-20 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| b8aaba4d-1322-3335-8ae9-3f692e2bbb03 | -5.9713 | -44.1312 | 2025-08-20 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 1dc0b1f1-7f71-3d5f-a2be-7aa5012ed440 | -13.1367 | -54.9171 | 2025-08-20 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| b74ce4f8-1cea-3c17-b86c-29fca95b399e | -12.9925 | -45.202 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 373.4 |
| 7fef2771-6bf7-3acf-8ff7-5cf4af3e2437 | -13.3349 | -54.4027 | 2025-08-20 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 285.9 |
| ac5a5c4e-a9ef-3e48-902f-c3d044eb2501 | -13.0198 | -46.7992 | 2025-08-20 13:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b7c6ca05-b19b-3a15-a00e-3e933f0a47ae | -12.6698 | -44.9525 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| b7fa8dd4-c8f0-358f-9a15-a763dc6c520e | -13.1364 | -54.9376 | 2025-08-20 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 15db8c53-6ecf-3734-9c4d-3f35b442fb09 | -12.8984 | -46.0906 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| c401be9c-c1fe-372d-b2dc-b19c152d7d57 | -12.9921 | -45.2252 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 13ce1095-0dbb-35d1-8b66-58dbf235238a | -9.2082 | -59.6354 | 2025-08-20 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4284caf6-f781-370b-8c20-d481344fc578 | -12.4997 | -44.7937 | 2025-08-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d562fdbd-ae13-3dd5-8282-2f55d0275bb6 | -13.8748 | -45.5411 | 2025-08-20 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f4b5dfbb-d396-31ba-87b7-fb22398e61ae | -13.1044 | -51.9221 | 2025-08-20 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a3003042-716c-3129-8a35-fcd9be3e929a | -10.7043 | -48.2226 | 2025-08-20 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8fec38e1-1337-35d8-87d6-639f441bed68 | -6.9605 | -42.8816 | 2025-08-20 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 398659b4-846d-35c6-8013-e47b62c54d43 | -13.0387 | -46.819 | 2025-08-20 13:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9b8ae5f9-80a6-33f3-9205-18ea814fad2d | -17.594 | -42.2745 | 2025-08-20 13:50:00 | GOES-19 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.8 |
| 5f91211a-5422-3972-b464-e139f5bf1388 | -9.1895 | -59.6364 | 2025-08-20 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 15e28a7a-e11e-3bd9-adee-7ae3e7cd26e2 | -15.0196 | -54.8112 | 2025-08-20 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 08430b25-5f9b-3476-9de4-bcfa68e1fec6 | -3.982 | -42.516 | 2025-08-20 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| ef147b65-f02c-366f-8cc0-536742b73e66 | -12.9732 | -45.2051 | 2025-08-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| a7d96329-8445-3021-bb1b-d1d06459eae5 | -11.011 | -45.6105 | 2025-08-20 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 5d5b639f-cce7-30f6-99d5-6ff20adf235f | -5.9711 | -44.1542 | 2025-08-20 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 260.4 |
| a6cc5cf3-1bfb-36e5-a45a-d2ac4f5eb5dc | -8.8291 | -52.0558 | 2025-08-20 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 527eb180-c5f9-3782-adee-25b1acae8844 | -6.4451 | -45.5072 | 2025-08-20 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3903609b-028d-307f-b264-05bf7ba77ebf | -12.9925 | -45.202 | 2025-08-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 302.3 |
| 243d50f7-2879-3707-afd5-2867e99075ed | -13.1364 | -54.9376 | 2025-08-20 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 52cf9ef8-6c13-3494-aa80-907921ee48b1 | -14.3711 | -51.996 | 2025-08-20 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| e88dfd8f-eaab-3d10-9f5f-e69a887add68 | -13.3349 | -54.4027 | 2025-08-20 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 239.9 |
| 37744c79-4336-39fe-9e30-53c9c70d3385 | -10.9919 | -45.613 | 2025-08-20 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 16dd502f-d2d5-3c43-91aa-63d71b6cbbf7 | -13.3346 | -54.4233 | 2025-08-20 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 306.9 |
| 43edd762-e9cf-3fb3-8d86-62eaee1517d1 | -5.9713 | -44.1312 | 2025-08-20 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| b75d123d-d4e7-3780-93e0-7b9660696567 | -12.9173 | -46.1106 | 2025-08-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 05b97091-44f0-3527-888b-b0ee892b5778 | -12.9778 | -56.8614 | 2025-08-20 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9afc2e82-5d0f-3e0b-9a31-105848358e84 | -13.3157 | -54.4047 | 2025-08-20 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| e4d78a0a-2b1e-3965-8ac9-1223f39715b7 | -6.9419 | -42.8598 | 2025-08-20 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 4506e789-76cc-354b-b33e-c6bee2423446 | -8.7945 | -45.4693 | 2025-08-20 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ffa2403e-fac4-3b45-bf25-482e3536ca84 | -13.3537 | -54.4213 | 2025-08-20 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| a11a9bc5-41d8-3454-afc4-edaf073af573 | -6.9607 | -42.858 | 2025-08-20 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 70e5b314-dfe9-3a1e-b218-383837bc5f23 | -13.1367 | -54.9171 | 2025-08-20 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 0a09ede6-06a8-33a7-9d7d-495f6b9bbe94 | -12.4997 | -44.7937 | 2025-08-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 40fbe15a-212e-38c7-a030-3e5912f3269b | -15.0002 | -54.8135 | 2025-08-20 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7fe6b8d7-6b14-31bb-a3d6-4e652ceafd47 | -13.1555 | -54.9357 | 2025-08-20 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| cf49e9b1-dd8d-378c-a4f5-48abb7920aef | -11.3087 | -44.9264 | 2025-08-20 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 1ce9fb89-4f00-3db1-a843-57ccb9e28a3e | -12.9736 | -45.1819 | 2025-08-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 6a0c486e-c9bf-3aec-a01d-f8af00cadea6 | -12.898 | -46.1135 | 2025-08-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 4d0d36bc-e296-379f-92f6-ee3b192ba5b4 | -13.1558 | -54.9151 | 2025-08-20 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 36104512-dafb-38f0-8bec-76eb183e0bae | -13.354 | -54.4006 | 2025-08-20 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3c18bf74-8160-3463-b998-64a52ce13fb2 | -12.0976 | -44.717 | 2025-08-20 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e3c2d9a5-3fb2-33a2-a299-22e0c359440b | -12.6698 | -44.9525 | 2025-08-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 7c482d86-0df7-3004-918e-ce53e43a93a7 | -13.0387 | -46.819 | 2025-08-20 14:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5d4fb0c2-682e-3423-ab4f-51445802c8ae | -17.594 | -42.2745 | 2025-08-20 14:10:00 | GOES-19 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.7 |
| 0da6effb-d48e-3e53-afcb-849b5cbd0eda | -12.4474 | -47.668 | 2025-08-20 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fad3c737-da90-32e8-8344-5929828448f2 | -13.0198 | -46.7992 | 2025-08-20 14:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9051611e-60a5-3b8c-bace-d89f77e2f765 | -6.4451 | -45.5072 | 2025-08-20 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8562c0be-3afa-3a93-87fc-6b8e2346f3b6 | -13.1367 | -54.9171 | 2025-08-20 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| f8b0d9b7-04ac-3cd7-986a-19d1ed4f9ae5 | -8.7948 | -45.4465 | 2025-08-20 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| db217ef0-8789-343d-be5a-eb1cc85d380c | -13.354 | -54.4006 | 2025-08-20 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 23014c90-4215-30c5-90a8-d4e00dd145e1 | -12.6698 | -44.9525 | 2025-08-20 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| a6f90fa2-7fd4-3998-b863-c6e932dc3e72 | -3.982 | -42.516 | 2025-08-20 14:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 5f469b49-3468-3212-9c7c-e5d4a3567efc | -13.3349 | -54.4027 | 2025-08-20 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 321.2 |
| 59b39229-6eaa-3fa3-9df0-2fadec163082 | -13.0387 | -46.819 | 2025-08-20 14:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| b20e6b0c-e2f4-3438-983d-447ad6cc67f1 | -13.1555 | -54.9357 | 2025-08-20 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 3f4c6502-822a-3557-a16e-aa03ceb246b1 | -13.0391 | -46.7963 | 2025-08-20 14:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| ac032e73-2c96-3cbf-8ec9-d2672a44b7b0 | -13.3157 | -54.4047 | 2025-08-20 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 90f94595-31e3-3065-80be-0fd7edf9d562 | -13.3346 | -54.4233 | 2025-08-20 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 315.8 |


[Clique aqui para ver as próximas entradas](README65.md)
