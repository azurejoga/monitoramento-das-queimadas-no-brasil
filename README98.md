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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5f549c7-d43f-33f9-a9a9-daa65a112dc6 | -3.34338 | -50.42035 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b23287a-cd32-3b08-8f56-09630cc4a444 | -6.04786 | -53.28376 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d63bf457-3282-3743-bdd3-8122fe7d96cc | -3.24902 | -54.03426 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1c58ac0-ac13-331f-8a0d-7a7f5c65fe76 | -1.15005 | -54.2227 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aadda6b7-e01b-33ef-b191-a6c80d644e3b | -2.8814 | -54.18889 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7c8758e-b695-364b-a05d-eac070233241 | -5.8844 | -57.75107 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec834006-ef91-3586-8612-99bd09424bc0 | -6.45811 | -55.49583 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24ce287a-661e-31b3-b8c6-ea23602b8c2f | -7.53005 | -45.30867 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 02faa0f0-0826-3c8d-9b26-1a704e1bca17 | -5.88808 | -57.75161 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f4bb8cc-edf1-3f54-9cae-9f1588052cf6 | -4.55621 | -54.97874 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0475058d-b5b8-3efa-aae4-49df179629be | -3.90535 | -55.90495 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a97467-0e1c-3cb9-bb27-8c75c20ce933 | -5.06229 | -60.24876 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 349a94ad-808e-3456-bec6-721ceda06e5c | -3.52987 | -59.34603 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b25db0cd-eaa5-3f0a-b1f1-4ea9b052cc13 | -6.93425 | -59.25416 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 262ef44d-24d8-36ab-98ee-ab846bde6d30 | -3.76592 | -57.16456 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2210b59-6fef-3f8c-905f-983bbbfe0074 | -5.18947 | -60.30228 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ed22d0f-50f2-3a00-9d80-08bbfab614ea | -6.48346 | -55.97067 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4166ed8b-1ee0-3956-8180-0c1f3b67ad8f | -3.43235 | -59.35783 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e8e432d-2d18-377e-9409-544c74a2413a | -3.93112 | -54.57571 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53f46da2-4031-316b-a16c-887359a57fa7 | -5.78559 | -53.80763 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47b1b6af-e8b1-3956-9bf8-78edd39cea8e | -4.15486 | -55.13309 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c12bee7-da49-39ca-b7b5-4bb268cc095c | -2.99233 | -54.17453 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7acd720e-330e-348f-bafd-9c91e729d323 | -5.02735 | -50.94633 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d977650b-b294-3c52-94f3-a8cc39c83d26 | -3.26277 | -54.01169 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 484c5ab3-0d65-36df-ba95-16f2546e78f1 | -3.57085 | -54.38276 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| da431efa-5fc3-3e86-aab8-5b2874d28fd1 | -3.77017 | -58.52606 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b074e4ca-95bf-3a56-a401-231365153651 | -2.46023 | -56.0602 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03bda685-ec4f-3a5b-9b3b-ad1ea583f1e3 | -3.01472 | -53.96935 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81cb124b-e5cc-32da-a2e9-9aba0b41e0c6 | -3.8167 | -59.33749 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad3cbb42-8893-3523-8833-2478aade4090 | -3.54767 | -56.84554 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea866d13-d383-3a20-91ca-0644c890b08b | -4.51472 | -54.90087 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bec407d-62ff-344b-b351-2ba5725fa26c | -4.23938 | -48.72645 | 2026-10-10 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 029e6b34-6bde-3604-82fe-0f43a7934250 | -1.10892 | -54.15882 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f804aef0-87c0-30f2-b5e4-7312f7ec378c | -3.05714 | -54.23763 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ef9b0f2-d565-3d7e-bd1a-af0dbdda2313 | -5.18511 | -60.30155 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c49393e-3472-39ac-bf90-4c494fb5e048 | -2.8368 | -49.88098 | 2026-10-10 05:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96424a05-7999-313d-a2ee-51f3b0ec34e9 | -1.50676 | -54.54252 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 994aff36-27c9-3801-b1a5-0984a758df1f | -3.10075 | -50.31895 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cd60a66-1673-3685-9936-c177ced6819c | -2.8384 | -49.88419 | 2026-10-10 05:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54d3f343-0982-347c-b12d-06f511ee0380 | -3.37161 | -57.5336 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76a57ce3-658f-3d74-8ec1-e8e4f5a5666a | -4.79983 | -56.14041 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a3f2a17-eab5-326d-bd90-86bbee5ebd76 | -7.37501 | -55.22469 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2bf1964-1f8c-324f-9534-9a0afbe217fa | -4.19559 | -59.40937 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 086f55b0-f477-39e8-8e78-8cde96f8ace5 | -2.74099 | -54.1097 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9217efac-75d6-3b48-a8e7-c93fa44feda3 | -3.32166 | -59.83809 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9c31236-5ae4-39a2-b1a9-54306e25124f | -5.84441 | -44.92873 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03491adb-6de9-30fa-ac80-1f2c853024c7 | -3.98508 | -59.37128 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ca13299-2646-3c4f-a8d8-08730f51f9fb | -3.27465 | -54.06694 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7523fbb3-8388-307b-9d4c-11771df4efe7 | -4.34099 | -54.79769 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f891ad55-2bc9-34eb-a7ec-193debe8566b | -3.04414 | -54.10474 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 384cab25-4cf5-398b-8b5d-0f6c78c13373 | -5.97 | -55.34167 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 000022b6-e1cd-3fe5-bcf7-685b948c3ea1 | -4.52132 | -54.9883 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8faaac5-5227-3095-8f3e-a37acb353d82 | -7.49731 | -54.99134 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ddeef54-28a3-3df7-941d-07417a0500a0 | -5.09873 | -46.22577 | 2026-10-10 05:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 222f26b8-7389-3bfc-bc20-ce2f75c65561 | -2.56183 | -56.17242 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd9ff924-9dcb-3416-b74c-912fbc8de80e | -3.00634 | -51.009 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dfcb042-e556-3439-96b6-d76a55cc7a4b | -3.90766 | -55.82479 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c031732e-3356-35f2-a584-caf92e1eabb5 | -1.6047 | -55.16132 | 2026-10-10 05:04:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00fb2d27-3faa-3db0-bc8a-a0989a73c39b | -4.92229 | -49.35667 | 2026-10-10 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51fc3c86-9f4c-3f06-9625-4734ca5bd2e5 | -7.53361 | -45.32299 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d333d22-86fa-358a-b137-1cb0b8df67b1 | -5.33244 | -50.95894 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd76d3c2-94ac-38b6-9f3a-184e1f814045 | -9.00939 | -44.37418 | 2026-10-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35573610-5ddf-35b9-ab91-bf481ac865ef | -3.57689 | -54.70885 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a990b9-b3b3-37e4-9bee-cb6222ee944c | -3.42087 | -54.0653 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eacca9e-2866-3330-b255-de835df1fa73 | -6.98898 | -47.72385 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fdeb507-44a7-3a47-b24c-de1055326eea | -1.65126 | -55.19889 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 816baa3c-71b6-3527-8dea-cbf781d00db6 | -3.3141 | -54.67128 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e36ba96-34ad-3dac-a24b-37f6b67a0d55 | -7.01587 | -47.66587 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d8fad68-0227-3551-9152-48a865ac9d0c | -3.2558 | -50.42978 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90270f47-aef5-3d48-8c9c-33e78c67aeb0 | -3.26868 | -54.2536 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b765de82-fad6-34d3-bafe-f43725cba0f6 | -2.51569 | -56.32436 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d93e8f94-d4a7-36e0-b6ea-12e3fb03de1a | -6.32002 | -55.25648 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea306a34-c00a-3834-aefa-62ad7a5528c2 | -2.94701 | -54.11777 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8bab6f4-5b95-39ea-b0e6-cc855d2611cc | -3.0354 | -59.16164 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4e4920f4-3ecb-3533-81c3-8ddf1c626b87 | -6.00492 | -53.49271 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45f34b3a-e6c6-313a-a109-b8d394c860a1 | -3.45888 | -50.59037 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80c986ad-b72c-3543-81eb-cecddefdcb5e | -6.74874 | -52.94633 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 756aaeff-fe8e-3d41-a212-c44d32916b73 | -3.20335 | -50.55355 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28d306f2-5102-33f3-8b45-dbc85285eb6a | -1.8032 | -53.74627 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c76c153d-09cb-301d-a67e-0dbb67b76407 | -3.58911 | -54.71796 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f978922b-9ebf-3f73-a949-04b085fd3389 | -6.45477 | -55.4953 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 573c8518-b75d-33fc-a7f9-d0e4dd7fe90e | -4.61222 | -49.20601 | 2026-10-10 05:04:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 814b8cf3-e860-3a40-affd-bc42a95ae27e | -2.98353 | -54.76334 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c8c6b08-e622-3596-81fb-1e57ac37ff89 | -3.27372 | -54.69378 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1dd51e41-f92f-3ca1-bc68-c448db41fbf4 | -5.18267 | -60.31142 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e314b92f-6117-396e-8359-7b1b1af53fba | -6.04634 | -59.91236 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00ded16c-0ff3-3d14-8073-0ac8543975b4 | -2.80748 | -51.72799 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9597d5c-b742-3f9b-b054-2fdc1133dee4 | -3.03666 | -53.89516 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee36990f-9759-38d1-b519-24f214200799 | -3.89456 | -58.95838 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 459dfbb8-0856-3bef-a200-77f4683b1803 | -5.87231 | -53.5146 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dbecd2a-c60e-36a6-8c90-d870ea8a0113 | -5.07945 | -60.22593 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2864e190-8efd-362b-a86b-2d14305545c9 | -3.13992 | -54.35731 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8ff3d9f-0f7f-3736-9fdd-daf78ebdb7ff | -3.59745 | -54.60088 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 26d942d3-ddee-309a-82b1-42b4b5c07d9f | -3.18013 | -54.74388 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 157a7f1e-3d06-3d7a-aa8d-78571d6e7017 | -3.25412 | -50.41673 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0ae7afd-115a-37dd-857c-95e1fd315ecf | -3.27322 | -50.38956 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6713d1d-2d36-33ea-9c60-3a768e9247d7 | -4.73517 | -55.67116 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 494a25d9-c6ce-38af-a1d3-236fd3fe27e0 | -1.62963 | -54.43146 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d389477-fb2c-3ce9-a9ae-5cbc8f669a75 | -5.92631 | -51.82661 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c80d14b-454d-3b2f-9329-23794edd06e3 | -3.86013 | -56.00988 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README99.md)
