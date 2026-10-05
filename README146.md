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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61fa429f-34ff-3c56-9351-7da0b043fd06 | -3.08698 | -69.20367 | 2026-10-05 17:37:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ed1892bb-2ad3-3bac-853e-0b64cdace7d8 | -8.87704 | -66.6406 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 47ae8ed7-2db4-3fa7-a9df-b4143d9c3bcf | -2.77953 | -57.65362 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3d7d7cfa-1fa4-381b-b22c-9441977ac81c | -8.32854 | -62.91681 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 139cde06-cac7-3b7b-a906-f306259c2745 | 0.4419 | -60.53341 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 09394ef7-dcb3-343f-bbb2-e9613c8dceb6 | -10.47072 | -68.11066 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b66bb92a-16c7-3088-8310-e3f85b1ba742 | -3.17883 | -60.06319 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23a29fe2-6873-316d-b386-b7a34a8fbc7b | -2.57669 | -57.79145 | 2026-10-05 17:37:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 70663e47-ed7d-3a11-afbd-80af722f21c6 | 4.22882 | -60.40681 | 2026-10-05 17:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 30172e4f-a3f9-3b69-8d24-759898a93d91 | -6.58193 | -55.27774 | 2026-10-05 17:37:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5d9a8434-ed4c-3685-9eb0-df040a648596 | -9.14461 | -65.90062 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 5c9751be-2ea9-3f23-a0d0-808acb330912 | -10.62509 | -68.85593 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f89baee5-e4da-3d18-b43c-36aa19e26b27 | -9.13509 | -67.93393 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5fe34377-e7fc-3e80-be29-9764aceb5a11 | -9.26487 | -68.37605 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 47.0 |
| b0e51f98-fb75-3465-9edb-b9f822258ed3 | -7.22775 | -55.19741 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2b9bbb66-6da4-306a-b023-2cc5a4238d43 | -10.47534 | -69.58309 | 2026-10-05 17:37:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 91cf21a1-1c69-3f6f-a4a8-c6486f5b6a14 | -8.59985 | -70.07906 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d5b43cf-54e4-3f18-97e0-3b30a9981176 | -9.23193 | -67.89687 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0bea6f6b-3d61-3432-937a-0484eec656ce | -9.66929 | -65.0842 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f5ed75d7-00b2-3eba-9f2f-1509c341dda9 | 1.88917 | -55.73167 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de4711de-3534-368d-b522-d83b1628feaa | -8.75121 | -66.91405 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fc1a40c1-4976-3818-86dd-c02585b39b9a | -8.8042 | -69.49148 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0e543c07-b35a-3057-886b-31d723f115cc | -1.69276 | -55.56147 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2d47fc43-a8c7-3c9c-bd1d-d7ef4c2d2cce | 1.61256 | -55.77599 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0d7f2b55-d4ab-3bed-824a-3c4fb753549a | -5.66669 | -49.21852 | 2026-10-05 17:37:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 303fe74d-6281-34cb-ae85-f53afe074449 | -9.22049 | -67.38864 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c6bace78-9a3d-3c99-bf76-5457c6c293ac | -9.00377 | -65.69236 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fe8e7d96-2df5-3799-a9f5-9481fe5b6d57 | -9.03358 | -67.55747 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fc60bd5b-f1c4-3fcc-8adf-f2b18a45882e | -3.62456 | -64.34241 | 2026-10-05 17:37:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 0e4bc7b6-7514-3671-8b33-8973a1708ab0 | -2.76329 | -57.66919 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 7be7d5b4-e2be-3755-b8f9-09065c267e18 | -9.11207 | -65.35477 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| a9662e8b-58c3-3047-9089-1f24608247f2 | -6.4646 | -55.44935 | 2026-10-05 17:37:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 4d3ca798-3fd6-3e24-b25e-5ee905506f47 | -9.17107 | -67.67213 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 371efcd5-a8a1-3d2c-bc79-e911f1710194 | -9.11963 | -65.47527 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 08022f46-2806-34c2-a7c0-b457deef4bf6 | -10.73917 | -69.61766 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 857ac4d1-5962-375b-8d4c-539edaf53476 | -0.73687 | -57.96936 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f447cc68-f1d5-375d-8e1f-5420693ee1e3 | -2.93936 | -58.32575 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 2f958557-ca1f-3148-9d22-288e335d9c0c | -9.33261 | -65.73489 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8d043990-526d-34a7-95e9-892d5bbeff45 | -9.73754 | -65.07511 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6a6ed9b3-78dc-385c-a8b1-54b38eab8c3f | 1.16517 | -50.7435 | 2026-10-05 17:37:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3cf4f632-15d8-3815-8f7c-af71a7ba0a40 | -3.17722 | -60.05272 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bc7d5c18-bb59-34f3-bf78-c717d2dff3f8 | 3.35827 | -51.33949 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fad1045e-0367-36ff-a82f-78e98fcf1898 | 0.81894 | -51.61293 | 2026-10-05 17:37:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5543f057-e8b4-3198-a34d-2a417efae219 | -8.97654 | -68.95184 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d2695d84-363a-3cf7-be46-4f50b30e7dea | -9.30994 | -68.34745 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 637fe541-5641-3980-9b3f-b4f956b2e8a3 | -0.3739 | -52.06782 | 2026-10-05 17:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f6520ece-4263-3eaa-9114-a7943a9bbe5a | 0.64638 | -59.83585 | 2026-10-05 17:37:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f858533f-a820-3fb4-8cbd-1ee03d1b4b41 | -8.68337 | -62.8341 | 2026-10-05 17:37:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f17d80bd-037d-37a8-807b-b8d8266fcb63 | -7.22293 | -55.19279 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d6f52401-08be-3c35-acad-9ba016706d83 | -1.96423 | -55.38622 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d044019-f967-31e1-8fbb-b2ecb0aef8e6 | -8.97373 | -65.44518 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 47300eeb-b05b-3843-bada-4bb4352998ce | -10.64523 | -68.6074 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3491532d-2251-338e-a93d-e7c7ce370104 | -3.51058 | -64.63564 | 2026-10-05 17:37:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd69424b-58d4-33a6-be6f-6b5e8f94a8b3 | -9.1374 | -64.39435 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8699b4fa-1daa-3347-bbd4-0cffa63b3a05 | -8.87526 | -67.00119 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 687f232f-dba8-331e-ab19-d7cb8e4316b6 | -10.04495 | -68.83435 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1024174d-c7e2-3322-a804-7077e78d55ab | -2.64422 | -57.74654 | 2026-10-05 17:37:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d5f2c48-3c3d-358e-beac-caf2f3174c27 | -9.1126 | -65.3587 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6aa309f6-179c-3f0e-89fe-8ed948938058 | -9.3413 | -68.79056 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1e3fcc22-68d1-3667-bda5-4b407ba8335e | -10.804 | -69.56551 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a30884e4-9bd7-3116-a470-2445d66f74d0 | -1.84428 | -64.13786 | 2026-10-05 17:37:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 290.5 |
| 6e974576-7b1c-3f65-b16e-e9da7ebd34e7 | 1.72902 | -55.69135 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5a810a28-7645-3ade-b88e-8f24a1171218 | -7.2204 | -55.17719 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 995af23d-26bc-3d09-a766-70a92e192be6 | 4.20929 | -60.70215 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5c61ea9e-44cf-3def-a7f5-ea2df1cb9443 | -4.02989 | -69.50655 | 2026-10-05 17:37:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6d9d7a6-d0ee-3a44-a38b-73e4f9db5011 | -2.54245 | -58.0302 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b7f300ce-0d44-3910-ab6b-5a0e013fc683 | -2.63667 | -57.72168 | 2026-10-05 17:37:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2749e086-cd45-3485-81b9-07d61328f61c | 1.82701 | -55.54551 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b8e5c4d2-b90e-3f05-a915-0a0baec41169 | -2.57558 | -57.4481 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e9f83ce3-a0df-3cab-bd56-3516b07b1058 | 3.84659 | -59.59829 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3fd6b937-e5d2-3e94-9b2c-b6e8076bccdf | -2.8366 | -67.70663 | 2026-10-05 17:37:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a4b4563d-0e4e-30ad-8c08-b2eba8322ec8 | -8.84698 | -67.00503 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 74bcd831-b282-323e-837e-d9c5c2d3874f | -2.63928 | -57.73863 | 2026-10-05 17:37:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab7b1108-a6f8-373c-bbd8-bba0fd2ce41d | -1.45987 | -55.26315 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 92b696f2-0d64-3328-a54d-8de763fa7d90 | -2.77222 | -57.65473 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8bfbbf57-f78c-311e-80ae-0035f26d9021 | -1.4173 | -55.41148 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea9b101d-2fb7-361d-8962-5e63706cfd5a | -1.35975 | -55.97896 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9fdb3eb9-ba29-3f0c-a42a-672202c0066a | 1.45441 | -55.66263 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| aca3cf0a-6b04-3fcd-93d0-2d0adc405e43 | -10.7176 | -69.63271 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07b311d5-69aa-36f3-97cd-3c5c73bf8e35 | 1.87139 | -55.76085 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8b569d6c-da1c-3647-b5c6-b9898b6254fa | -1.7713 | -55.84188 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3abc1c29-5332-3758-97c1-556bbd7aa4b4 | -9.10281 | -64.37833 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e39582fd-dfb6-325d-9d46-01f15b074b67 | -6.46627 | -55.45959 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c2881356-4d90-3423-af8c-52a41013e622 | -9.35559 | -67.31185 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 532253f5-0f45-3020-897b-33fc493e0439 | -9.12454 | -67.8194 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e317ed21-c828-3833-8ab0-b6364035a06d | -8.96619 | -69.30927 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1e08b839-39cf-332c-b23d-963e79643663 | -9.12485 | -67.94119 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da26cf42-3e35-3a64-aa9a-c689a1a5c4ca | -2.15299 | -56.6673 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d19a9ba-d52a-3547-8fc3-113558759f24 | -9.29166 | -67.53317 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6a4e7faf-7a3d-3faf-92d3-b034e6a8789f | 4.28225 | -60.33345 | 2026-10-05 17:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1f8065f3-425d-35b3-a5de-bc79ca3ce103 | -8.5467 | -69.98355 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9d305d00-6901-3c4b-b5f6-1723df077087 | -3.01066 | -59.19735 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 28d9ba68-83da-38ec-b106-9eaed6d9d645 | -9.3621 | -68.8647 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 788a2667-2119-396f-8126-2f1f4df164e1 | -8.53891 | -54.59296 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e3824d22-6f45-3198-b296-2e9bafbe8486 | -9.04064 | -65.43214 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d350e224-561d-380d-a152-c155aa59d463 | -9.30294 | -67.54298 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d98ccee8-97bd-3563-a89d-40e45dad6114 | -9.21866 | -60.9105 | 2026-10-05 17:37:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11bda48e-872c-3002-b2fa-dd3dd4edf23d | -1.61741 | -55.11688 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 865cf595-628e-3952-9e36-b8e7cb34349d | -2.57919 | -57.14642 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c5a56646-52d0-3b42-8301-2e527b58399d | -2.05449 | -56.88472 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README147.md)
