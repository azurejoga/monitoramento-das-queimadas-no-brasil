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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 000209c6-0ba6-3a97-919e-fbca6070f9b7 | -18.02225 | -51.08883 | 2025-08-24 05:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0a55850-3db9-32a9-b7c1-b15c63bc68d2 | -9.17442 | -59.47278 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eedb12c-6113-3570-b408-65198eb2c105 | -9.15519 | -59.50763 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d58159cf-bab9-357a-95b5-2606ec69b8c2 | -14.7912 | -59.62149 | 2025-08-24 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf676cff-1e04-31f4-905b-8b11d9d7c1fa | -9.17058 | -59.58915 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab62224b-d145-3a56-adbb-545f152087cc | -9.01419 | -65.38493 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35f7583d-1ad8-3567-a6a9-24f57ae38e43 | -9.65041 | -59.63507 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a929e9c-dfca-3b12-9efc-9d9a530d5baf | -9.15994 | -59.68124 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a402422f-9885-374f-81de-d99edb3ae57d | -14.79061 | -59.62564 | 2025-08-24 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c15d647-4366-3634-8e7d-8fcad6c8d89d | -8.92447 | -60.7189 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 837d3e09-6c00-3e7a-a4b4-b4fc6d192944 | -11.53666 | -51.86683 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bee7383-5178-376c-890c-a9ee96d050bf | -9.16311 | -59.5013 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b9a847f-c97e-39a8-952b-4ffc96626e9a | -11.73026 | -51.69526 | 2025-08-24 05:25:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1293ace2-75f7-32e3-b564-2cbf9feaa59f | -11.5237 | -50.4867 | 2025-08-24 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 289db9a3-df37-3971-b8f9-e6b846b28edd | -7.72559 | -67.06868 | 2025-08-24 05:25:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f36b73-a83e-365a-982b-5bba49556ded | -9.64814 | -59.6464 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d56183d1-da3c-3719-9f72-f817dd747a11 | -9.80854 | -61.20993 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74e08fe3-ba36-3557-b200-cdcc04aed5b9 | -9.79806 | -61.21184 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af1cd40-6f19-38f1-b259-ce656184817a | -9.1869 | -59.45955 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45205951-4dee-3580-bf49-9144c2db53e0 | -9.34474 | -62.58629 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da35a15b-7b9f-3d98-aa04-ba47ae4a9c67 | -8.91582 | -62.42056 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfaa3446-d962-3c09-b5c6-3593446a1ebc | -9.53132 | -58.87738 | 2025-08-24 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d674a468-0e4e-3a86-884d-63ca69a67744 | -11.1809 | -55.0344 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7e24c94-8ea2-3d54-85c9-e363781e7b8b | -9.51697 | -60.55355 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91b85e68-9b07-3419-881c-bdf31e7d0248 | -9.13707 | -60.77068 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bbd1d73d-34c8-312d-bdd7-3ea233853093 | -16.79879 | -51.35269 | 2025-08-24 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48c1054e-1725-389c-a186-562f3130bbe4 | -23.62858 | -50.5656 | 2025-08-24 05:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0cba8ec5-7090-37f0-b79f-b731eae93f92 | -23.6291 | -50.55825 | 2025-08-24 05:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d7217528-9035-3235-a572-82c7e3857322 | -23.62866 | -50.56691 | 2025-08-24 05:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 61ae8881-7012-30c7-9879-5207d1f237ac | -24.25163 | -50.23604 | 2025-08-24 05:27:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dfac348c-3e0a-3496-8ac5-b688131777ee | -23.62914 | -50.55957 | 2025-08-24 05:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f7d7389e-17d0-3918-9b27-700cb0517657 | -23.84729 | -50.72388 | 2025-08-24 05:27:00 | NOAA-20 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ab78faac-9ec7-31e7-a477-a68ab833e831 | -4.9605 | -55.8226 | 2025-08-24 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 50128900-d7fd-3299-b164-df9aa19eb7ff | -16.7965 | -51.3637 | 2025-08-24 05:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 81e72a21-775b-3d90-b540-bba389482cd4 | -9.1536 | -59.464 | 2025-08-24 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1a491018-3270-3322-8b69-f17415f4eafc | -17.6176 | -44.298 | 2025-08-24 05:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8016dd35-85cc-3315-8c82-376a53d40db9 | -20.3599 | -51.68 | 2025-08-24 05:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 9f7b4fc6-0a58-3550-a93a-f4a7122d9b04 | -9.0231 | -65.7169 | 2025-08-24 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9e286f39-7e5b-3017-a2c3-88b04a37ca5a | -20.3594 | -51.7023 | 2025-08-24 05:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7fb56f9f-157c-3472-a0dc-efee73bef07a | -9.1722 | -59.4629 | 2025-08-24 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0d7ba2f9-3732-3ed3-b467-80f4805d0c86 | -9.1721 | -59.4823 | 2025-08-24 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b4ca173b-fa51-3e0b-ba64-9589e2021aea | -9.1535 | -59.4834 | 2025-08-24 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 83e1cb87-e300-3e7b-819e-446bc8df01dd | -11.5434 | -51.8665 | 2025-08-24 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| fba26de6-366c-3699-a10a-9577eb88cbe5 | -20.3396 | -51.6839 | 2025-08-24 05:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 53b3b87f-1675-3185-8549-058a143521d0 | -9.0232 | -65.6982 | 2025-08-24 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2cce1729-2a54-37dc-90a6-ce1cbcdbd353 | -9.1535 | -59.4834 | 2025-08-24 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 9390ca88-7258-3bd0-aec9-d68a75c7daec | -9.0232 | -65.6982 | 2025-08-24 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b043c92f-3741-388a-a7b0-d097176c2520 | -9.1721 | -59.4823 | 2025-08-24 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b16c7658-21af-3dd2-9819-b79072038700 | -16.7965 | -51.3637 | 2025-08-24 05:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 2b4453a9-caa3-3353-a57e-76d83017c0d3 | -20.3599 | -51.68 | 2025-08-24 05:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 4c830335-4580-318d-a8b1-db91ef5b5cda | -17.6176 | -44.298 | 2025-08-24 05:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2a230b67-8be1-34c6-ae3c-1386aaa71cbf | -16.797 | -51.3419 | 2025-08-24 05:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 42.9 |
| cdcbd7c2-0721-3bf3-805f-44d1477bcec6 | -20.339 | -51.7062 | 2025-08-24 05:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 913f826d-764a-302e-be63-deb48b4fec33 | -9.0231 | -65.7169 | 2025-08-24 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1d31778d-fffa-3750-80d3-194bebe7f5e6 | -9.1536 | -59.464 | 2025-08-24 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0f179b1a-cef1-34cc-a28d-f2cac21d57ed | -20.3594 | -51.7023 | 2025-08-24 05:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 309abe9e-30e1-3da6-807a-3959b94ffe16 | -20.3396 | -51.6839 | 2025-08-24 05:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 8cb5c3f6-b7a5-3f79-82e0-a88333dbac10 | -9.1536 | -59.464 | 2025-08-24 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e1978d8d-946a-3325-b8ef-39d1681401b0 | -9.0232 | -65.6982 | 2025-08-24 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 089b2898-945f-34e6-b047-e11a34aeda5e | -20.3594 | -51.7023 | 2025-08-24 05:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 93.0 |
| bb0edab4-490d-3b29-a847-2ca654578751 | -9.1721 | -59.4823 | 2025-08-24 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3196cd61-c612-3595-a1dd-6c0ba0ff6813 | -16.7965 | -51.3637 | 2025-08-24 05:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 44.3 |
| d5b110f7-a8e2-3d33-b673-a733a09306e9 | -20.3599 | -51.68 | 2025-08-24 05:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 4e85ed6a-7e6b-32b0-9558-0ca2f394d776 | -10.6128 | -44.3284 | 2025-08-24 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 71643a07-75de-3143-be13-e352de7194fe | -9.1722 | -59.4629 | 2025-08-24 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| aa1b53db-bda3-3fb9-b43e-8800b5bb2f4c | -17.6176 | -44.298 | 2025-08-24 05:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 4b289c7e-5b92-3491-95a2-4fa9398ccb77 | -4.9605 | -55.8226 | 2025-08-24 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| aa0429e1-9aab-3e63-af3c-0340e9889bb3 | -9.1535 | -59.4834 | 2025-08-24 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 4e75491c-7987-3694-9d4c-f2f859572e49 | -9.0231 | -65.7169 | 2025-08-24 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| bf93c781-8cb3-3b35-93cd-c42f1b8d8df3 | -16.7965 | -51.3637 | 2025-08-24 06:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| d09e0a24-064c-3753-be49-b5d4c96a1b14 | -20.3594 | -51.7023 | 2025-08-24 06:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8415b66a-1cc0-36f9-a12d-0d56b95fbadb | -9.1535 | -59.4834 | 2025-08-24 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 167044db-c7d1-30f0-b294-dc16fa1aa476 | -9.1536 | -59.464 | 2025-08-24 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 72c0377c-9055-3a6d-a0a3-6f1b7819be1b | -16.797 | -51.3419 | 2025-08-24 06:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| ba9c804c-94e1-323e-b589-cfb0ce6473c6 | -20.3599 | -51.68 | 2025-08-24 06:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 060a0da1-0170-3c0e-b2b0-dc3b3b5ee49d | -9.1721 | -59.4823 | 2025-08-24 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 40d799d0-d6cc-3096-a3ab-5ce4761580d6 | -9.0232 | -65.6982 | 2025-08-24 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6d3c88fc-037f-3f3e-bb0c-da22d0404016 | -9.0231 | -65.7169 | 2025-08-24 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 093bd6dc-a53f-37eb-9b12-957de9855a9f | -17.6176 | -44.298 | 2025-08-24 06:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fc84f0c5-b5f2-3d42-a6c5-4a56cfe4b458 | -9.1722 | -59.4629 | 2025-08-24 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2ea2c2d1-4df3-3a47-95cb-a0a65c0cb0db | -14.8153 | -47.9343 | 2025-08-24 06:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4d21f86c-f87d-34c3-a9f0-34f0c320cb25 | -9.1536 | -59.464 | 2025-08-24 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a210a6d9-6787-33c5-aae4-5e5ba240e3d1 | -9.1535 | -59.4834 | 2025-08-24 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3068ac2e-9455-342e-856a-7d521be0068e | -20.3599 | -51.68 | 2025-08-24 06:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 6eababca-54c0-3acf-8ea0-ea3c999d8a02 | -9.0232 | -65.6982 | 2025-08-24 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 67612de0-e336-3710-b0af-a201d2c0b536 | -17.6176 | -44.298 | 2025-08-24 06:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 65f2d660-d0ad-3aa5-907c-da385575d3b2 | -20.3396 | -51.6839 | 2025-08-24 06:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 87460ddf-d4e0-3141-9d1c-015cda1f6965 | -9.1721 | -59.4823 | 2025-08-24 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0bd59fdb-9c5d-3088-8ab0-a8d970c789ad | -9.0231 | -65.7169 | 2025-08-24 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 37ae474e-e6f6-34cf-9043-88cf69777158 | -20.3594 | -51.7023 | 2025-08-24 06:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 16e3e3ec-9e78-321a-a7ba-fc15c1b19299 | -8.90007 | -62.44747 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4149418-39f5-3a79-8932-a957c0095a8f | -9.19543 | -60.77964 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57197a60-d72a-3d00-8b33-1d5432ff24d2 | -8.92608 | -62.44135 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24bb600b-644b-3865-88cf-b6805626b2db | -9.02633 | -65.70228 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae5fef60-f591-370a-b652-929e50f8ace7 | -9.03413 | -65.72105 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 394f9739-5fda-3d74-9ea4-d48092273a99 | -9.20153 | -60.78711 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1a02c5a5-3107-315c-b9ce-0716e74084f1 | -8.60759 | -62.59429 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0caeb5f2-2f2d-33b1-b73e-be2678e37194 | -8.13671 | -62.85959 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cfeb9419-3a74-3b10-99f0-4d8c2dc70111 | -8.90805 | -62.44369 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31f0231e-f82a-347c-88aa-f743671814b8 | -9.46165 | -63.51124 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README85.md)
