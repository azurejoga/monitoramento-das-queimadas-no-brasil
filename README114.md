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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 071b429c-2e48-3366-8de7-a3ba55070513 | -3.32739 | -58.1355 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4dcb657-e80a-3b0d-864f-41a6aaa7b2ca | -3.68091 | -60.62846 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9625414-6c8e-3ab6-ae90-75cac974a4a3 | -3.48505 | -59.57986 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e791e671-c970-3101-a63b-898ba7bc2327 | -5.37847 | -55.8976 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee6f03b0-48ab-33b6-baa0-6601116a8ecb | -3.06915 | -61.28925 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84115987-9f5a-33a5-b897-e7d8b7857038 | -6.79461 | -59.95123 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7080628e-f24d-30dc-b111-e624003ac689 | -5.12687 | -60.28089 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab152caf-d4a3-36d2-a400-d70e75e409ee | -5.8701 | -53.64655 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 565f9cfe-31a3-3eb1-84be-2a740bf45f67 | -3.68834 | -60.58101 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bacfc42-2a5a-35f5-9d51-edd493ceaafd | -2.89871 | -60.05516 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a3a4084-1b50-3eeb-8cf5-1a2a92a55d22 | -5.98139 | -57.78126 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8601925-4a4d-3714-8039-f3fddd6178f1 | -6.73866 | -55.07406 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 337827e7-daff-3992-9121-982b6db76680 | -3.40503 | -59.2201 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9dad4bf-6de3-34a1-937e-1ed5faacd940 | -6.61844 | -59.91501 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 0d8cca0d-56c6-34d7-a7c7-91fbb18c0f83 | -6.04304 | -57.82656 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 340ff6df-e692-35ea-b287-bdf1fdbee60a | -7.33352 | -55.60229 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc45021c-0888-357c-a006-a794f6cb2359 | -3.7708 | -61.19221 | 2026-09-22 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7273a788-5a83-3494-ba4b-a71b66751b3a | -7.71411 | -61.23211 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c7fc14bc-877f-3110-a827-28f676a5853a | -3.82457 | -59.33589 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9621652b-e0c6-3c89-94a0-5882d8573962 | -6.22742 | -55.62161 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de9fc889-e87d-32c3-b1bb-b62529cb43e6 | -3.46513 | -59.53607 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d40e6b00-dfbd-345f-8045-25ca50ce2540 | -3.48908 | -59.60295 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 486e192a-f14a-3eb0-b808-6f20f2855ac0 | -3.69083 | -60.56513 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96332e66-e8a5-307c-8c50-59ed096afdd7 | -6.34723 | -57.77778 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caa0b956-0225-3252-9f1e-894b73e383a4 | -6.84108 | -55.53688 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 976319fc-7d92-3fe1-a821-179029495568 | -6.04735 | -57.82714 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| aafe5c27-ff23-3a73-b69c-e11353828b3d | -6.36007 | -58.28191 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c3c82db-c8ec-36a9-8ff6-6cb142c7a4d3 | -6.9218 | -62.90903 | 2026-09-22 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c340515-2c81-3a2e-a92d-d2712937f75c | -6.11172 | -59.89023 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1926e44-d7f6-3bf0-b382-3c07771aa029 | -5.3769 | -55.90818 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e15a7f9-6cc8-3fdd-922f-f9cdc7c5ca74 | -6.15299 | -57.84168 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d5bfd20-dcc9-34b4-9389-d32da2eef55a | -6.05905 | -57.8665 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf6ddf9-81a7-3d3b-ae25-e07608d92e58 | -3.3851 | -59.42633 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ca1c5c0-5627-3b89-8563-c1b4c7ecd7cf | -7.32714 | -55.61057 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1786dfa6-9903-36ff-ad8b-3fbc11064167 | -6.70792 | -58.99969 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f8ce08c-4693-38f6-b55f-3164d7d01d88 | -6.10332 | -56.10915 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3898258c-1064-3891-a5b7-9a700231db78 | -3.07485 | -61.27501 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05d6d6a1-7bea-376b-b569-2eef9cdcd722 | -6.78425 | -63.13706 | 2026-09-22 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbd3d514-74b4-31ae-892b-f810d6212161 | -3.7879 | -60.75248 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1dc80a6-2b3f-326c-bd0d-d8be0118bb04 | -3.97998 | -60.03182 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baad0564-b195-3e28-b8b0-819764c579cb | -2.86794 | -57.79349 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4deed2c1-87b3-3259-8704-6882fe0ad35e | -3.06305 | -54.4038 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cd538ab-2131-3353-a380-d51bd6d149f5 | -7.32833 | -55.60215 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2980e3de-547a-3071-940a-e24daec216e4 | -3.75331 | -59.42033 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e32b034-46c1-3700-a036-3b821e0e0943 | -6.45108 | -59.97246 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c97a76e1-b0cf-3862-80e1-4c11758469d8 | -6.14325 | -59.93708 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 578ce20c-a1ad-34c0-a5b6-4b6498bdb8ff | -6.63078 | -59.93571 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9c463bc5-7522-3bcd-92bc-ab5133cc874f | -3.59964 | -59.44059 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16f8ed9d-d008-343b-902f-fa45330d7e66 | -3.8192 | -58.89238 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 186e3eda-bcf1-3cbc-94dd-7b2ad98cb250 | -3.60687 | -60.56916 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81db5648-d6ea-3466-ab78-a1d33aaa729b | -6.13504 | -59.94047 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 915bca93-3317-36f5-a481-1b9c6038f749 | -3.18991 | -60.43594 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cf14f0a-9fbe-37e9-8e41-a63a7b46605b | -5.45783 | -60.14568 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f22abba-2909-3633-b557-ed6db3f8ca16 | -5.97879 | -57.7842 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a28e42c-47d5-3512-a0b1-cfb8b9d45547 | -6.72776 | -55.07531 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb834884-b44f-3a58-a1c9-40afdf3ed519 | -4.85544 | -56.02642 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6098409-2810-3964-88bd-09bb6bd1ff0b | -2.56975 | -57.50934 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a94252f-0e8d-372b-9490-adbb936098ad | -3.6129 | -60.57754 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c64ab6a-126c-35a7-b04f-cfd61338eb1b | -3.22073 | -53.95126 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87b14918-a8c2-3ded-9881-3f5eb9d6b224 | -3.40276 | -59.58346 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 858cabdc-0f06-3a5a-820b-df0126592387 | -8.25914 | -55.30104 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4effb7f2-525c-3f44-bd07-c8da321574fa | -6.19934 | -57.78025 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86244416-a925-392b-aab4-aad39398b2bb | -3.05074 | -54.41503 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb9ca816-f489-3c36-8fdc-dc2be8c1eb03 | -4.26952 | -55.43864 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0be9cc9f-3f66-3f84-9939-fa11812a56e9 | -6.7109 | -59.00731 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fffb5360-6923-32db-aa56-bc26e10286e4 | -3.06923 | -54.39808 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 131d1bd6-8961-3d23-b4c2-53b6850bdff4 | -4.29696 | -56.26722 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e12e510-ff69-3e09-9b13-20f4191de248 | -6.86445 | -59.92129 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4ab92ba-76c8-3437-9ddc-552694839316 | -3.24053 | -60.80332 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49486fdc-b312-3411-b863-ccf8103d6ea3 | -3.22479 | -61.05275 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d25b890d-87af-3a56-9e60-9ab429ae9ba3 | -7.32791 | -55.60512 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22b408f2-989c-3dfc-84af-8823aca6c952 | -3.0465 | -54.40768 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d5802bb-f65a-3a10-85b4-558e3de872aa | -6.81091 | -55.83023 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9d20d99-62ef-3d93-bc64-db8ead146a2a | -6.09986 | -57.68328 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| beace2fc-6618-3512-877a-e52e80701534 | -5.98079 | -57.78526 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ebe5207-1486-3a51-93ed-99bac48dd27a | -3.06681 | -54.41434 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f77e35d-85c8-3297-9e6e-d81123c2fd5f | -6.08866 | -57.69865 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ea4284f-39c5-3784-bb7e-b94dec6f9736 | -6.00687 | -57.71186 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a7622c8-9b16-3512-bc01-7fefd3f0ec33 | -3.77982 | -60.73523 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a1c39e6-aced-39cb-9472-e790c6c7bd1f | -3.4783 | -59.5743 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9a34802-551e-3de3-b03e-7a23a79c076c | -8.5991 | -54.62922 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71329d91-5021-3f8b-a092-a11847b3bb58 | -6.63148 | -59.9287 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1b334d47-5f09-35cf-83d0-2c46a34f57e9 | -6.75124 | -59.06664 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65f3620e-3921-3001-851a-7a2ebd6e94b2 | -3.75445 | -59.31314 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701f5fe2-bbab-305a-875e-131ba918b5ac | -4.2736 | -55.44502 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0947d7fd-708f-3ec0-afe7-e445bc5cc419 | -6.1005 | -57.67903 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e02f50ca-cc0b-3da3-ab02-2b1d78d05f28 | -2.96112 | -57.62832 | 2026-09-22 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77c589fc-760d-3c9e-b72d-292b92c03d3c | -3.19405 | -60.43185 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd698d0c-2ba6-3790-aed7-fa4a9a3ba28b | -7.90564 | -61.82473 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f36a623-c41b-3493-a47c-440bdf0ce319 | -3.60033 | -59.43608 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6df29c5a-9546-3155-873a-b0a378606b37 | -4.4112 | -55.24477 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3bb7046-aa9f-3a1e-be4b-6aea3e2a3196 | -6.71647 | -58.99742 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2880dac9-05b6-37f2-8df7-e656b3e8fbd0 | -3.46208 | -59.53106 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e387850e-3585-3f8f-8795-90e157fd4f91 | -3.70497 | -60.63618 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e120369-5760-3f40-bdab-c6a0bb77f9bd | -4.325 | -60.88549 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36d369f7-07d0-3743-b0af-6a37023acb7f | -2.86327 | -57.79655 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f0a6487c-6acd-3b73-b189-176961c159e4 | -6.79706 | -58.78712 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e062742d-2836-3c77-83a4-062039c6dd81 | -2.92669 | -57.79485 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d71b2258-3e4d-3997-acf7-bb543b35b332 | -6.10424 | -57.68377 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dc8d752d-2e54-36de-bd8c-22336bc78f41 | -2.87617 | -57.79472 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README115.md)
