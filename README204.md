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

## Dados Diários - Página 204

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 187b2bf4-4fea-36c2-b8ec-533952c8d4da | -3.5451 | -54.65795 | 2026-10-08 07:56:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 77c887a1-4aab-33b8-bf62-d8e037faa51b | -3.07964 | -53.94378 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 3042410c-f662-30ab-b361-87f552b20b98 | -3.5842 | -54.65794 | 2026-10-08 07:56:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c49cedca-aadb-3955-b947-49dedb66dc8b | -3.17596 | -58.62935 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 999badc5-3fe9-33c6-a946-8d54c492f102 | -3.26805 | -54.02079 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| fd000d67-32c8-37f3-b14c-96fe13769388 | -3.59131 | -61.63237 | 2026-10-08 07:56:00 | AQUA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3218736-3f60-3866-8c25-63e11555d27d | -3.11579 | -54.17302 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d1d9e692-7686-3fc4-91fb-313b41a3e9a6 | -3.09119 | -53.94111 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| ebf514e4-d153-364f-97a5-7686b6350d67 | -3.01551 | -54.07324 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 81f11dfe-969a-30b0-8e95-950045f37518 | -3.09643 | -53.94613 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 22250be7-a720-39fc-9083-04cca05b32e0 | -3.17858 | -58.62428 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e3f379d9-40b7-3d40-ae82-5b922bd14958 | -4.07181 | -59.82794 | 2026-10-08 07:56:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e998649c-deaf-31d4-b877-92899c3476bd | -3.01019 | -54.10949 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7937337a-a5c9-3ccc-9b40-d77cdd7e45e4 | -3.17372 | -58.64512 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b653bcdb-0712-317a-925c-943236f579c3 | -3.0201 | -54.08194 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 3fb150a2-e41b-32d0-9450-a57675281753 | -3.57721 | -54.66219 | 2026-10-08 07:56:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b371f58c-36e8-3099-bc0b-310b8eaa22ba | -4.05922 | -59.83966 | 2026-10-08 07:56:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 720c1e77-8988-3568-8406-61f694572020 | -7.23373 | -55.08347 | 2026-10-08 07:56:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8055eedd-bad7-3830-9e06-1af38b4ae487 | -3.83544 | -55.97512 | 2026-10-08 07:56:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a892d8b3-5fa6-3d9c-8c87-c924dc55532c | -3.59905 | -54.55676 | 2026-10-08 07:56:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 9619bcbe-4270-3d92-b5eb-dadafbafbe16 | -3.09297 | -59.19394 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 61921fc7-c4b6-3ae8-aa42-c01731683756 | -3.26261 | -54.01534 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 896ca3b1-f270-3f31-b1e6-e977ec920b3c | -6.99277 | -59.10398 | 2026-10-08 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3a6ccd56-e7f5-3f5d-aa0f-6c75d89a9dcc | -2.4953 | -56.05987 | 2026-10-08 07:56:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 338b6e6e-479e-3c33-af6a-766b3f48c347 | -2.15488 | -59.2257 | 2026-10-08 07:56:00 | AQUA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 70617236-995a-3a5b-8403-5226af112e1d | -3.31262 | -54.71111 | 2026-10-08 07:56:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5255289c-2168-3baa-9339-a6b5f654d85c | -3.8491 | -55.96976 | 2026-10-08 07:56:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| c1655e54-d314-3631-a0ce-a79907770c8d | -7.22909 | -55.1201 | 2026-10-08 07:56:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| ea3ca106-0c8c-360d-a3b3-564c0e0e92be | -3.47507 | -59.57617 | 2026-10-08 07:56:00 | AQUA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 82ec0801-76f6-37e4-87c9-453c453a848a | -7.22341 | -55.11166 | 2026-10-08 07:56:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2f79e61f-4214-364a-9d71-e671f214d5a5 | -3.17622 | -58.64004 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 6d930ab7-a093-380d-8849-9826a562a5b1 | -7.00233 | -59.12246 | 2026-10-08 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4bafa119-e0f3-346b-9c65-0c1de691ac26 | -3.0035 | -54.07954 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 4bf1ff01-5bb2-3316-8843-c314bbf633fc | -2.9823 | -54.06857 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 79733fc0-fa3e-38f3-b23a-a1646508e85b | -3.05757 | -53.93661 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f0064767-ee73-3d28-8592-6097261174e2 | -3.30438 | -54.70223 | 2026-10-08 07:56:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 1d530cf2-c430-3e1f-bf4c-99e3dfdbf538 | -2.76187 | -54.09931 | 2026-10-08 07:56:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 656074a1-1fb4-3545-b716-c4690e20264a | -3.84996 | -55.97726 | 2026-10-08 07:56:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 4b243e87-3ae2-37e2-a836-4edd3293fe1d | -3.31733 | -54.67772 | 2026-10-08 07:56:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| acaf6d66-dbb6-3a38-a25d-a9f651e9db31 | -3.08585 | -53.97819 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| a4a9f4e5-5573-3755-9011-4915bec44cb2 | -3.05399 | -53.92793 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 41a83dcb-3a2b-3b6e-b663-25d004d5083e | -3.09323 | -54.27487 | 2026-10-08 07:56:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| b4ccd3a7-fc9c-35b6-8251-ad7dca2de622 | -3.0408 | -53.9341 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 5c093dc8-9603-3844-a40c-4f396756847d | -8.60931 | -67.02495 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| f7cb4882-5730-3309-a135-c5eec5cec882 | -8.62928 | -67.01801 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4387ada4-3511-3d75-b642-2a59c268ee32 | -8.64989 | -67.16955 | 2026-10-08 07:58:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3e6fac9-e89c-3b0e-97c2-0a58de8552d8 | -8.61085 | -67.01515 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 153fbcbf-5ad7-33b2-a5e5-41ebe6e1fa0b | -8.64831 | -67.17952 | 2026-10-08 07:58:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ec74da7d-3129-37c6-8246-e0b8c563b6a3 | -8.53307 | -66.977 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2638a947-e2eb-304a-9a77-40e1606d8dd4 | -7.43834 | -63.54895 | 2026-10-08 07:58:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6d24a5d7-c611-3bde-8dcf-ce2ed501156d | -8.8426 | -64.23391 | 2026-10-08 07:58:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b2388e49-7db7-3166-8455-75eabb48d8e2 | -8.62006 | -67.01658 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 42fd16c7-124f-302d-943a-9551717d4bf0 | -9.05671 | -65.92847 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d51a52e5-36ea-34b3-8796-d334ade84008 | -8.61853 | -67.02638 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 49c8673a-e6b5-3e24-b208-c72fbdba3ec9 | -9.48011 | -64.35387 | 2026-10-08 07:58:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a08a2f29-0bf9-3a33-b371-92ceb6d63c26 | -9.04926 | -65.91817 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c61ecd5c-e65f-3ec1-912a-c26d4c9b0425 | -9.13558 | -65.29567 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94d6d18b-f578-3051-8804-c896a99eec1b | -8.52079 | -66.99514 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 78e05398-0e4e-3726-a8c1-f76d7e0d482a | -9.04787 | -65.92713 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 47aa54ef-8c41-3b9c-b959-41c88d1bfae6 | -9.05969 | -65.48521 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f63a7c3-66f9-3945-a511-c3f848637d1e | -8.62775 | -67.02783 | 2026-10-08 07:58:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 988ffaef-b2ef-3055-8d4d-5ef43012dbfd | -7.42998 | -63.53255 | 2026-10-08 07:58:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 97840fee-d96f-39de-aa45-78ad1ce7cc61 | -8.6291 | -67.0296 | 2026-10-08 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5d7c4ad5-f96a-34f8-9287-fe33588209ae | -8.6107 | -67.0301 | 2026-10-08 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 326ff8cb-6768-3b3b-be2e-f17f7352518b | -8.6292 | -67.0111 | 2026-10-08 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 6630280f-673f-3ed1-b1a4-f5ff58e56152 | -8.6291 | -67.0296 | 2026-10-08 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d676a968-12ac-360a-9980-ecd43246f45e | -8.6107 | -67.0301 | 2026-10-08 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 420ac1ef-9694-376b-9f62-4734ad8feca2 | -8.6292 | -67.0111 | 2026-10-08 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 19c12006-0620-38a3-8a32-5ac745bb0c50 | -8.6107 | -67.0301 | 2026-10-08 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 36a99dfb-0016-3b6e-b111-e83cee02ee92 | -8.6291 | -67.0296 | 2026-10-08 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ced08dee-5bf0-33bc-ac12-c7ca1f7221e8 | -8.6107 | -67.0116 | 2026-10-08 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d5d8aba6-5d20-38d1-b406-d692a02dfea2 | -8.6292 | -67.0111 | 2026-10-08 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e4915699-861a-3270-8fc4-c5e7b22daa77 | -8.6107 | -67.0301 | 2026-10-08 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b72464dc-60eb-330e-9b08-50d4fb620d85 | -8.6292 | -67.0111 | 2026-10-08 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 94c8fdd5-c256-34e3-a0c1-e2489103de47 | -8.6291 | -67.0296 | 2026-10-08 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e8d3d3b3-5916-3887-b3ae-10125c6e8d08 | -8.6292 | -67.0111 | 2026-10-08 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 396bc5f8-5c58-3e68-a825-ab5f6b7ccee6 | -8.6291 | -67.0296 | 2026-10-08 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| ee739aee-c733-378e-b4f3-cb7f45d72e3a | -8.6107 | -67.0301 | 2026-10-08 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1b59177b-9d1b-3118-ae1b-7ebdcd43dfbd | -8.6107 | -67.0116 | 2026-10-08 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 4e9ebf00-d8ec-32e8-8220-68c770788b2b | -8.6291 | -67.0296 | 2026-10-08 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 38d44c48-7fb1-35c9-94da-68e755930686 | -8.6107 | -67.0301 | 2026-10-08 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 35d12cf7-d954-33d5-93e0-92958efd65ee | -8.6292 | -67.0111 | 2026-10-08 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a14fcdc2-789c-3e7b-8c97-8c790201b13d | -8.6291 | -67.0296 | 2026-10-08 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 038f8768-491a-3d46-912a-9ecdfdaa1ee0 | -8.6107 | -67.0301 | 2026-10-08 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 00e62c59-7033-3a0d-9209-dd9113a2f939 | -8.6107 | -67.0116 | 2026-10-08 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| df05b187-cd7c-3f32-ab6f-cd5150e8df1d | -8.6291 | -67.0296 | 2026-10-08 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 04e9387f-7262-3d3f-af33-8a8dfe137c7b | -8.6107 | -67.0301 | 2026-10-08 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| b4c81d96-2c92-3d09-821e-13900e3da917 | -8.6292 | -67.0111 | 2026-10-08 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9e60247c-3f38-33dd-8dbd-5131a480d534 | -8.6107 | -67.0116 | 2026-10-08 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b540437a-162c-3d28-b72f-a4becff77715 | -8.6107 | -67.0301 | 2026-10-08 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e2e4d4b3-62e6-368a-bc14-5644bb3560c2 | -8.6291 | -67.0296 | 2026-10-08 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0ac0970b-b680-348a-b07b-82f9ae4bda16 | -8.6292 | -67.0111 | 2026-10-08 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d0a94adf-86f5-3ef1-b090-ddac03682965 | -8.6292 | -67.0111 | 2026-10-08 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b8e2aa18-4f5c-35a8-9594-0b1ca79625c1 | -8.6107 | -67.0301 | 2026-10-08 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ceadbce8-80fc-3d1c-b387-281567f4361e | -8.6107 | -67.0116 | 2026-10-08 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| bda719fe-37ae-3908-bfa6-9a9bf9bd16f5 | -8.6291 | -67.0296 | 2026-10-08 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 69d7ca9f-60b5-3bc4-afe9-cf4223b9c5ef | -11.3363 | -46.6998 | 2026-10-08 09:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 42d33e90-8436-3485-b76f-5d02c724f22e | -11.3363 | -46.6998 | 2026-10-08 09:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 5c6976b9-b2ad-3bff-8cac-2a119030cc5b | -11.336 | -46.7224 | 2026-10-08 09:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| aca256a6-0b34-37e8-a0ca-b0c5cbd4ce6e | -11.3172 | -46.7024 | 2026-10-08 09:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |


[Clique aqui para ver as próximas entradas](README205.md)
