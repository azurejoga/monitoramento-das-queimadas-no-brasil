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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0fddf4e-5646-3860-ab13-5128708dc409 | -9.82427 | -65.01525 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cbb67d23-002d-320d-86b1-f948565e3397 | -8.59597 | -66.80791 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8bb2b722-0584-39bb-aab6-99f8df9a3302 | -10.67843 | -69.60031 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7f911c2b-a8f9-3c68-84c0-e42ddf6c7e73 | -2.94228 | -58.32125 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4c538dd-76c8-3f98-a2de-bb17a9288152 | -9.13033 | -68.20679 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0d79bbe8-7c12-3c8d-8519-c24f31a69326 | -9.04489 | -65.43156 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dc237c12-2b3b-36cd-8ece-3ae1fa5d3e8f | -9.8868 | -64.17652 | 2026-10-05 17:37:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4bd31881-abef-36f8-b91e-eb7c38227f5f | 0.30896 | -50.99532 | 2026-10-05 17:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5890f6a4-1917-37ff-a022-b37d1231abca | -2.09759 | -56.62008 | 2026-10-05 17:37:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 075fce54-736f-33d4-8693-f6dabed7bd94 | 1.84722 | -55.80089 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e485221a-d7bf-339a-a2cb-91ad7e17f976 | -10.08878 | -69.18161 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ef68dc3a-0100-3ba6-929a-ac3931b2bdc0 | -9.4861 | -65.63828 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bcdccc35-1b74-3fc4-a7cc-b74df4723807 | -9.88545 | -64.2819 | 2026-10-05 17:37:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a199b89e-879d-3eb7-95b8-df061da1f70b | 3.52243 | -51.50557 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b381ca90-069b-3d6e-8c1b-9e5368d5a803 | -1.64387 | -55.1429 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 934fece7-6b33-3711-b5de-153e7ed7d06f | -1.80815 | -57.0976 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 146721ae-a230-3a5a-aa54-caf34b877cc2 | -9.38299 | -68.29964 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 38a96445-5f84-3e1b-a216-1b57ea1de397 | -9.21491 | -67.3839 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 6a7daafe-2c04-38bc-8a21-86c68a6aed29 | -8.43498 | -54.99087 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b1a24bc4-98c7-3a30-a724-11f6f7b2e9bf | -8.77678 | -69.53402 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75de05a0-f46c-31be-b0dd-638d99c37255 | -6.81263 | -55.29792 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7c3bcd29-4e78-3952-b111-057d30d6a44a | -9.49914 | -69.04942 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41b172b6-465a-3ba4-9325-08da135eed4e | -2.76356 | -57.64733 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d00cad45-e67b-3478-940c-5db1b8276d63 | -8.82092 | -68.65862 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 15c8b362-46d2-3529-8e02-2c2dc44eaede | 3.56615 | -61.34503 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3875b9fc-7e29-3db8-bc65-ae6a73853ca8 | -8.85851 | -66.78502 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| fc8ea117-f90b-3164-bb01-d85bb22dd014 | -10.14731 | -69.02388 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 04aee7ed-12d0-303e-a54b-f3946469dd55 | -8.6601 | -54.54208 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 27357bbb-c876-39d8-9073-ee57f24b071a | -8.89084 | -66.63871 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2e74a6c7-401e-367e-8124-a77063a1ad56 | -9.38389 | -67.69881 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 5d25eced-fb12-3777-962c-0214893cb1b5 | -8.60018 | -67.13268 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d89a0cca-dc05-39e6-80b8-e13582bd8a60 | -2.28747 | -58.09375 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 346621c1-38b2-331e-b05e-65f75c041830 | -9.05522 | -66.09737 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c9ee7370-efb0-3a3b-8b79-32b46ff6f608 | 1.9836 | -60.61897 | 2026-10-05 17:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4ae808ca-73bc-3f2d-bb2d-70f88b724913 | -9.33784 | -68.88873 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 469fcd0c-150a-3255-849a-af685927d02d | -9.19504 | -65.51789 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 739b9915-9f84-36e6-aac6-b9437d7be196 | -1.73242 | -56.071 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 649fe1eb-395a-380d-8c2f-4393b1e30ac1 | -9.01511 | -68.42551 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b58ccbda-db2b-3a90-804c-35059a984559 | -9.36481 | -68.86467 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3b8e60ba-ee9d-37d8-93a9-209315491465 | -1.89962 | -56.25887 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de5ff30e-2251-3f36-991d-eb0c1b9300b3 | -8.64203 | -66.66524 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 806de331-083a-3941-bb45-e7f2771f6a14 | -9.12412 | -68.23898 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e63ddf7-9327-30b9-9653-d10a584c21e4 | -8.87768 | -66.64534 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b6438775-05ea-33ba-95fb-7708b4999dd5 | -8.85601 | -66.79233 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d11ea60b-11d9-301c-a54f-fcccd51f9a55 | -9.03902 | -72.33322 | 2026-10-05 17:37:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ebb4d183-e749-3cb9-8c88-d691d071529f | -10.24063 | -68.2328 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6b437fd-e274-3d41-abfd-0e7f1ebbff96 | -8.8638 | -66.78925 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| bfe39b74-5b4a-393d-bd1e-6063c2472257 | -8.96067 | -69.31002 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1fc706bc-b1cc-38aa-8c28-7036833ed723 | -1.80552 | -53.75262 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 5c8878b4-d2a2-3af5-b2c5-67a81b918f2f | -9.10535 | -64.36752 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e45547cc-d3d7-319c-aec8-9a02eaa3690b | 1.86 | -50.6707 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2328f766-e206-31b8-a3b3-0f2c1e613e77 | -10.39658 | -68.03524 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fbabd416-4f97-32b5-99dd-acf9644c8d83 | -2.32241 | -57.98709 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4c4e2ce2-fd65-39ad-8be2-e90b6f2a9906 | -9.81894 | -68.82112 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 560922f4-dfb0-3f33-92db-3aed126bddd5 | -9.10094 | -65.39953 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 34c3ca08-2c89-3093-878d-c53c29d05f65 | -8.89814 | -69.34831 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2bbce215-8d0d-34f8-bca3-af7a6e230519 | -0.73778 | -57.96918 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 89a0915c-d0ce-38b8-afd3-1fbdac5910e7 | -8.42398 | -54.99788 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 9b8b080a-f08e-38ad-98c6-2f3500d4d45b | -1.99836 | -64.10794 | 2026-10-05 17:37:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7a1068d5-3b43-3703-b981-2328a4429a7a | -1.25022 | -55.72086 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb6d8f91-09e0-3cc5-b417-ec6681828788 | -9.62298 | -65.37094 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8505467-fb5f-3636-a548-3c20b90c4ca1 | -3.10507 | -59.73952 | 2026-10-05 17:37:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e4d3c680-c76c-399e-a49c-06a66c676b45 | -9.33237 | -65.45007 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f41c50e7-5da5-3805-93a2-6dbbbbd36db6 | 1.85084 | -50.6892 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bbde1bd0-00b7-3e1b-b141-7ace9e04fc93 | -9.48167 | -64.6879 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b2e10f8-b1c8-3188-98e3-48f62c154764 | 2.25106 | -50.81947 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd0248ea-0b7e-384a-a603-e2c925a56893 | -10.47234 | -68.16565 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5893cc06-d0a4-3616-a638-f7c42527ffd6 | -9.10838 | -65.3593 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 95e56b52-2c80-39d4-822e-327ad6f05041 | 1.81164 | -55.55673 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a9a59754-90a6-3375-ab99-9902af0dd9db | 2.08803 | -50.73026 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 64e0c165-34cc-3e87-b2c9-88ad35ddc30b | -8.85069 | -66.78809 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 50128321-4a96-33f1-8a7d-9df7c531f385 | -9.68036 | -67.07243 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c9eba13-3a6b-391f-98ba-de890e1e01e7 | 1.84152 | -55.80873 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 009bb4c1-081e-3e60-8120-2812564ca8dc | -10.71799 | -69.40531 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b4334cc1-ed04-3614-982b-25b2c461b8da | -9.53532 | -66.78249 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88c27704-3c23-389a-86a3-19ad7d447c68 | -8.87306 | -66.6459 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d7bd2052-3c47-3292-9f19-2ed91d048a49 | -9.56888 | -66.02032 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d0423d7b-c1f3-3b6f-961d-be6bd0738ee0 | -2.07007 | -56.85767 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2532cf34-3466-3d53-82ff-52445cf2beb6 | -9.22698 | -68.05164 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fcfbac27-7f64-3d2a-bf7e-f99fc7ea26ed | -9.22738 | -68.05462 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8de391c-d627-33e9-9e54-c948fb5da077 | -8.84275 | -69.48249 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 46d08f19-2a7c-33ea-8d48-3fc9b5870653 | -9.1258 | -67.94116 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa86bc83-cc2e-3a7b-b97c-fa33f6245587 | -9.29402 | -67.62998 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f834a7db-aa46-31a8-837f-37b984362817 | -9.26529 | -68.37923 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5e62bce7-d58d-3b4f-bfaf-f51340fb95bc | 3.07399 | -60.58949 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 296d1e6a-edab-399c-b41c-18f74f288f05 | -8.87243 | -66.64116 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| deaaffe6-3a87-3744-af79-1a7ab87bc603 | -9.73912 | -65.08679 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 5af03bf4-d845-34fe-b8ae-bfccd0043322 | -9.15028 | -68.23853 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 34bbe0e6-c27a-31ff-bc96-5cd4b1168ec0 | -7.23486 | -55.19091 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 452271c9-572e-3647-b9dc-0d8f39cc0ab3 | -9.12155 | -67.83472 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a9ac38de-d155-3640-b249-c4012e1f10b3 | -9.53916 | -68.5895 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d7f271af-459a-38b7-9868-acc6be88e31e | -9.11651 | -64.36071 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ce94aa4b-b7ca-3f66-8eb6-59dc6b6ca75c | -9.38963 | -67.70386 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 512c6814-dbc8-33a2-a1b4-dd7ee4de9191 | -8.42793 | -54.99724 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 7bc89357-d5cc-3520-ad61-82fabde746fd | -9.50315 | -67.13291 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6f0733d5-769b-3945-a381-e1a714ec6850 | -9.1364 | -65.90594 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a1f474d9-c228-3dba-826e-d69aed610e03 | -1.48545 | -55.87226 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fe61efdd-1730-32f0-aca7-b1c729c08272 | -9.1099 | -67.82438 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 28d53d78-6a7b-33fd-a4a4-5611ae79adc0 | -8.59544 | -67.13334 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9ef5fb3c-92de-3897-a43d-25baf0f3d23c | -9.34516 | -65.32645 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README153.md)
