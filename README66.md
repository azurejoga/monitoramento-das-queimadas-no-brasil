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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e9de6ba-46d6-3583-bb5a-d1c108dd5701 | -11.80313 | -51.47043 | 2025-08-27 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c578590-606f-3fb5-9cd9-ddc840942965 | -9.19254 | -59.54039 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 889aa1ee-dbf6-3060-be5e-d1dd9c47940e | -9.17799 | -59.4597 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c41d486-b1fd-31fd-a641-39e651506393 | -9.40471 | -60.5284 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1bdf19a2-c7c2-3bc2-be71-8c3c55989cba | -6.93752 | -59.56097 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d62f5f6f-9a2e-31c7-a4ee-cb9c4031fc9e | -6.92322 | -52.82259 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cbda4dc-a4e8-3a36-a467-9154d67a6bbd | -7.4374 | -57.62667 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d501d87d-a275-3184-ba6f-52c996a919b6 | -9.4119 | -60.52595 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efc0784c-3b8a-386e-a651-e3b99acb7fcf | -8.07232 | -61.54825 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17820e80-686c-3f06-bd33-5ac4cc39e2d1 | -9.41965 | -60.51999 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ccc8398-0581-3753-a18f-539473174f78 | -9.1736 | -59.46615 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9123fca4-28b7-3376-9cae-dc36682c5277 | -9.01552 | -65.69312 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6605e0c-1d18-3ea3-a57b-17dbd7a1b144 | -7.35998 | -57.62613 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f03068ad-b3f0-3ea0-8270-17423c5af4aa | -7.34867 | -57.63195 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d9e1958-665c-34eb-945d-b93905e1a784 | -9.64733 | -64.99715 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71b984a6-4e31-3cee-a4b1-3ff08e88d073 | -8.89684 | -60.76844 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89f5c563-5a25-3aff-a132-258bb505a0cf | -8.88959 | -60.77094 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31dc3090-f26c-3e00-92e8-25ac50565a7f | -9.17547 | -59.54126 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff48262c-049e-3b84-9dfe-ee0bc1c2c8df | -8.954 | -65.95017 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f2df9510-4a82-3592-8a45-8878524d3881 | -7.04653 | -59.1922 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97aef80a-c6f3-377f-b77e-72c9262a62d2 | -7.74142 | -50.27982 | 2025-08-27 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16555753-a945-3c3d-bfb9-f8396a0748a7 | -9.28426 | -63.71706 | 2025-08-27 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95afa1f4-43ed-3039-a208-bbe203453b39 | -8.07292 | -61.54447 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 561914d9-d1df-322a-9544-84c29303a751 | -6.6232 | -53.32874 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7719c5-f176-3bae-961d-63ca14fdfa54 | -8.59398 | -63.86671 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11c38ba0-e2f4-3811-92b4-6855adad8d44 | -9.15412 | -59.59134 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c91d07ba-2c53-35e7-bf73-04aec348d8d9 | -6.816 | -58.96782 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef497657-8976-3d08-8b45-16e2cd3ad08c | -6.62638 | -58.54779 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d4f9e39-307e-3f03-ba54-8c8e396464b1 | -9.64439 | -59.63002 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6c864ab6-c6f9-3980-85bf-99481c14a65a | -6.87735 | -59.90017 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd216fe9-9343-3b28-9650-e4896a61afdd | -6.8303 | -58.96297 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 534253d6-b7f9-3e35-a5cb-d3a381ee71fb | -9.01458 | -65.69216 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c7a96bc-b8c8-3647-b56e-47a27ca8b2ba | -9.79548 | -64.26247 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c5e30b7-bbb8-37c5-83e3-13c691bc5024 | -7.2719 | -57.67283 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 126dcf21-482d-3897-9bb0-1134a9b60815 | -8.88474 | -62.477 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f90c8c0c-ab39-38e5-bd60-8069bb5839a9 | -7.47099 | -61.39912 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f2b1f0a-ad06-3ce2-a35d-2309dae9bf32 | -10.10702 | -57.77108 | 2025-08-27 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5548596-8f62-316b-a3f5-df2a1a6334c9 | -6.71542 | -58.56521 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 350e4a36-b978-3550-aa6c-8b1c4b06ea0c | -7.70896 | -61.11763 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54fb5a87-09ab-38c3-8dc5-f2cc31c49b0b | -10.09705 | -62.89705 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0265128c-0079-32da-8df6-bd6e37027e42 | -8.86746 | -62.44944 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 994317f2-c70a-3ab5-a286-daaca581f49b | -6.6325 | -58.42021 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3680cd8-8e2c-3cd0-9eed-1aa9e5929b08 | -7.71177 | -61.12182 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e527ed73-f87f-3fcd-83bf-4e91e356c920 | -9.40108 | -62.49314 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c029975-d886-3751-97b4-459484aea9b3 | -9.16008 | -59.55309 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d933016c-81db-3f68-917d-f35abeb1fc19 | -10.84312 | -54.01326 | 2025-08-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d38e905-c80e-369d-b6f7-5c26ede5258f | -9.19421 | -59.78999 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3129d1dc-1f6c-3d08-85b3-7628b6660580 | -9.58544 | -55.37844 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21039d21-5d56-3921-a51e-1afe2d1ffe35 | -8.53263 | -62.65573 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0765331-627f-3bd4-8384-39a4ad156cd5 | -7.40757 | -64.34684 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdaf9856-2755-3da1-b2f2-d56a267bd633 | -11.81641 | -46.81557 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faba1ce2-1f1c-33e4-8406-01f3d6cd2a0c | -9.32905 | -63.20284 | 2025-08-27 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a56dc0b9-b50a-3c4a-8b52-f5c63aaf2fcc | -11.31985 | -55.21205 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82d05108-0baa-38f1-8b2d-bfcd648c173c | -8.57758 | -62.59868 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0045bb4f-aabe-3ac3-aea4-dcb031c99142 | -9.07061 | -66.06476 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9d5a2e66-b453-3a3a-bcc7-87fb280a6422 | -6.79057 | -59.63024 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eee3ba1e-ad35-3846-8a5a-90a0f5765fea | -7.10331 | -59.21878 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5398a51f-a8cc-387d-be5b-93592a792216 | -9.17374 | -60.80595 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5afbe2c3-127c-36c4-9deb-3aacb8b9b153 | -9.19585 | -59.5409 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95559af5-c3d6-3985-a5bb-3e1fcc298cea | -5.60767 | -60.22485 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63359007-9584-3410-8184-6931c4500728 | -6.79781 | -59.67045 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d291e7a-12a1-311d-b663-1d14b80de234 | -6.25308 | -60.01933 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7940ff2-aafb-3a1f-b297-8256618bc8e5 | -6.79736 | -58.62782 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e214360e-7d3e-3f3b-aec7-ea459d5d5f30 | -9.58796 | -55.3887 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5b3ffb6-c4be-328a-b336-87ff808be73b | -9.15869 | -59.53799 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eca3ce0d-8c93-3fa5-b2c6-33916c615f70 | -7.56206 | -63.86138 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f76f88e-51cc-3834-8a60-fc141e47cffa | -8.95254 | -65.95866 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| ebf61de1-b43d-30fa-9a3d-7453391347ff | -9.56606 | -55.37537 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaf63003-6a37-3ae2-904e-e3bd2bdc579e | -9.20547 | -59.43548 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d43515b-1bbf-362e-9388-299bade01c26 | -9.80414 | -61.20152 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee50adc1-c65a-397d-b65e-4402b7828e3d | -6.36012 | -55.79933 | 2025-08-27 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f48bd6d1-9a24-3051-ab23-e4167034a5ca | -10.24821 | -59.66203 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b7380a7-92ce-3b8a-83a9-e917a8892c6d | -5.52887 | -60.20883 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96350acc-9269-3a75-9e55-df53a25251b3 | -7.34977 | -59.66559 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24faed66-6004-3701-8ca5-536b62fa0fc6 | -10.30926 | -46.80904 | 2025-08-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89721067-4f12-35e1-b8cd-dfa059b8fcc4 | -5.40802 | -60.17542 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e8acd72-d0e7-377d-b69a-79ae340a331f | -9.17216 | -59.54073 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9024e185-aa8e-3e2d-ae89-ae1063dddb68 | -7.3778 | -64.36711 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be51fca4-b5d9-34a2-8c8a-160c80fb5c21 | -8.96472 | -65.9726 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c6e785-e8cb-30bd-9960-217b010bfeb7 | -8.5027 | -69.80213 | 2025-08-27 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c142ee8-e874-3600-8d7a-bad5419c2390 | -8.89246 | -62.47414 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e460553-bd81-3ad4-8f3d-3e6412274d9e | -11.81565 | -46.8224 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 245e7dca-3d01-3f30-a936-4b5c900d3055 | -10.03334 | -59.35877 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93bbc3e4-f69b-3448-89d3-a0ece8259f7d | -6.91447 | -59.36258 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da07939d-caf7-3398-97a9-99f19b94956d | -8.88796 | -60.75974 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2ace867a-e3a4-3797-a832-8f7e6818fb01 | -9.0259 | -65.72758 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7adb4898-8a1d-3784-b19d-761ed1993157 | -10.77472 | -47.04108 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e20d5e20-a233-3b58-8fe0-0459fce9e8ee | -8.93661 | -65.94726 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d57c5e21-5889-3224-b2e3-4b0d09a9d8cf | -6.23699 | -60.01318 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98e4878c-cf99-37c4-a390-fb3d08966c32 | -8.07171 | -61.55207 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 993196ab-3d3c-364f-b3cb-5888305bf4dd | -10.40836 | -57.70552 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8f3037b-679a-396e-aa40-7752afa710f3 | -8.29548 | -46.32679 | 2025-08-27 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04b1e564-245a-3f94-bd27-ce0cbd3cd812 | -11.18845 | -62.646 | 2025-08-27 05:18:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c00ffcb-b5f6-3f89-8e38-fa6e94a04531 | -9.189 | -59.4543 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3f25d8c-1f7a-35ff-821e-04de66600009 | -7.60333 | -61.62538 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e94ae10-24fe-3fe0-9b22-3772971fce24 | -6.93824 | -59.64273 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2928fdb3-8b94-3672-a769-adc1dd30d7be | -8.5618 | -51.35231 | 2025-08-27 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ba0557cc-d780-3684-9783-0b0a90d0cabe | -6.57694 | -59.88444 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b00827bb-06e1-388d-a2a8-259061a024b6 | -8.71895 | -64.02816 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6fbbcba-c4d5-348e-8f1f-9e40e03f9f9d | -9.41854 | -60.52701 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README67.md)
