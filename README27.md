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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1bc0ad0-9a01-325b-b5d5-4747985a607e | -12.95895 | -46.92124 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e73f7567-d3c0-3d66-8965-67df151bfa15 | -10.29213 | -60.54638 | 2025-07-19 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2444254-d78a-3e84-9e56-d8bec6b366cb | -9.43193 | -48.84809 | 2025-07-19 04:57:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6314bfab-61b5-3fe7-9a0d-8d54a4f6a6b1 | -7.3509 | -45.32192 | 2025-07-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c96be08a-c55b-3e64-823b-25607a4d8024 | -12.71409 | -47.79486 | 2025-07-19 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d623bb61-be6c-3c6d-aef8-c5405324a42d | -12.09249 | -44.7366 | 2025-07-19 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a910a172-b5c6-39ab-a284-66f2f93e52ac | -11.83438 | -48.20435 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c4acc8e-6327-3d4b-ae47-f0de09da4342 | -7.48717 | -63.82315 | 2025-07-19 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07e71d42-d571-3093-827c-4e631e07ccab | -10.0931 | -47.24016 | 2025-07-19 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72dd40f1-1996-3f35-9e22-5813b6e3ab74 | -11.73394 | -48.1876 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 574d3657-e058-3432-8094-6b4967bce66c | -11.47902 | -47.32366 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 881070a2-0d3a-3b50-a1a9-54711ab01809 | -7.48355 | -47.50074 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13ceb480-c433-366f-8269-b087f721123d | -11.5693 | -47.09437 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edf45d15-4799-3729-9ad6-d5811d6755a0 | -9.80811 | -47.74619 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6776142b-59f3-3616-ad27-7aec88b6c26a | -9.39406 | -47.95135 | 2025-07-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a12b89-61df-35a9-9cc7-7beff9445e16 | -8.41445 | -46.87492 | 2025-07-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 603fc089-d0fe-3574-9edd-e5ea928c2328 | -12.67637 | -46.83248 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 574f2a88-665b-354d-8eda-3322f2712591 | -12.093 | -44.73235 | 2025-07-19 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0e3530f-7ee7-3886-870e-82e491730e90 | -12.13851 | -50.23755 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0c0d72e-78ca-3438-9767-219338a6f18c | -8.26782 | -46.08441 | 2025-07-19 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eece9ab4-f778-3dea-b05a-0667422c0950 | -7.17647 | -44.1036 | 2025-07-19 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6115828f-76b0-3864-9960-572ca4462578 | -10.61934 | -44.76718 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9d9749dc-cf17-3a2b-a307-33b277b30d06 | -7.48422 | -47.49588 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 689c38ff-f098-3386-ba2b-ae7638c80275 | -8.06872 | -50.11085 | 2025-07-19 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5e3798e-d86a-34f1-9d58-9ece79d6113b | -8.26064 | -55.17836 | 2025-07-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23453b84-cc0b-3082-ad45-10999e8f39ec | -9.80868 | -48.56437 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6fef3135-3fe1-3b0d-a6cb-5d7984d7881b | -11.83909 | -48.20498 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e536cd4-b089-3db9-a76b-2a802da7765e | -12.99372 | -46.9398 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e10be166-42e5-3ec3-abf3-e4779af48f8f | -9.83739 | -48.374 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48719f3a-f9da-3a99-98aa-4078e54dcc73 | -11.45824 | -48.16442 | 2025-07-19 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 452bb7fc-ecd3-3620-9429-fe30ab377737 | -6.76191 | -45.51074 | 2025-07-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a3cc6c0-ee5e-3e39-a52a-e71891f4b8a0 | -12.58078 | -56.97596 | 2025-07-19 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7220417b-cbe8-3fcf-9b3d-ad707c7bdeff | -9.80422 | -48.56382 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 323c9b5c-ea31-3f04-aa6e-a19a6c06675c | -12.06596 | -47.35212 | 2025-07-19 04:57:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f16b57c-217f-3e64-954e-0e6215ecec1c | -9.01756 | -59.76627 | 2025-07-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e98fe8e3-2f9c-32c2-9b91-5e4da9d30c04 | -11.37264 | -54.34402 | 2025-07-19 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2372b9b4-7a31-3c92-85ac-3fae5d5458f0 | -10.63755 | -44.76703 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c9447f7-9e33-32f8-bf33-b4a697a04b90 | -8.64529 | -47.75411 | 2025-07-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ce69062-a946-346d-ba27-f3f9a6a5a039 | -11.95971 | -47.02063 | 2025-07-19 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5de1b65-c75f-341c-9507-499d0fd89359 | -9.80825 | -48.55827 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 92815830-8a60-3b2a-a66b-fa001d241be0 | -12.37747 | -50.33461 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b9928055-693f-3b13-b5e4-34739c7c7cd0 | -8.88659 | -50.15797 | 2025-07-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40436938-bed8-3dae-90eb-a9e783f62195 | -10.67735 | -49.6775 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d931ea05-ad83-3ca8-b677-72c892f0fd83 | -11.82903 | -48.20871 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b920001-7b07-3bcb-9c74-2687073e53b4 | -14.20094 | -45.33981 | 2025-07-19 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6095b161-b066-37bf-8f73-4bd47d88d902 | -8.25926 | -46.06984 | 2025-07-19 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33624749-09ad-37fe-ac3c-98b47cc0ceef | -6.89016 | -45.24329 | 2025-07-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b319e4f5-cc64-3c6a-b911-38330a825dce | -9.8368 | -48.37848 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40e0ee7c-f081-3f91-9443-95771b484cf2 | -8.2623 | -55.16792 | 2025-07-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce953e8c-aff9-353b-9526-e61514c7ba5d | -11.96519 | -47.01825 | 2025-07-19 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 103dec3a-db69-3fa4-86a2-b021da09daaa | -8.01678 | -43.67291 | 2025-07-19 04:57:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 374f8761-4c67-3359-b397-200be028c342 | -9.83987 | -48.37602 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 264eeeb4-d709-3d97-bb39-ad3d4a393b52 | -11.48726 | -47.33018 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 07bf0eb5-0b7e-3d80-a89b-860cca8563f7 | -9.01618 | -59.53719 | 2025-07-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e038593-3edc-3105-8a6c-db83fa652627 | -8.01737 | -43.66852 | 2025-07-19 04:57:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccf8dc52-6558-33b1-a71d-e0787711555f | -8.97515 | -61.51567 | 2025-07-19 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb306665-758a-311e-92c1-20f2ec3dc3e9 | -10.67947 | -56.54844 | 2025-07-19 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 654f6f05-c8ef-3520-ad17-c59d19ee5009 | -7.20854 | -48.22451 | 2025-07-19 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18c07017-3275-3069-94a2-db03dff232ca | -9.80765 | -48.56274 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 64aaceb2-c1b8-3193-825e-83999ba020bf | -8.92375 | -49.84254 | 2025-07-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e82c86eb-4b53-3c63-9714-f53437d31a3b | -11.83373 | -48.20936 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a5e7c02-04cc-3ea5-8fc8-50a9bf0bb6ea | -11.47405 | -47.32301 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 310df384-c919-38b2-9623-e71009b6a5a0 | -7.58304 | -49.4043 | 2025-07-19 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fafbac2-04be-3df5-ae28-e47d23a09d62 | -9.43629 | -48.84865 | 2025-07-19 04:57:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c29ac955-0d81-36c2-b1bf-8ec7cb4a213e | -7.48435 | -47.50377 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65707955-e07b-38f0-9548-8ac6812a95db | -13.61421 | -45.637 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1735f1c5-8ce4-39f2-a701-b8fbeb166676 | -11.89064 | -55.44822 | 2025-07-19 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d05261e-1d8a-3637-896a-8f2c049b41b9 | -13.61232 | -45.63724 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e6aed1f-6767-37dd-93b0-a6208351d73b | -6.75617 | -45.51348 | 2025-07-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f27bfc04-0146-3dff-8b4d-8751d58806c8 | -12.99293 | -46.94616 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc169902-6836-3bff-a707-a512d05412f6 | -10.63808 | -44.76293 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 959a2c93-1ecc-33ed-964d-faca8f71fdef | -9.70525 | -56.09185 | 2025-07-19 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd89508a-f72f-3b29-9915-9be8d6778f71 | -12.37435 | -45.72956 | 2025-07-19 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 710ab213-654f-3204-be04-914a74706320 | -10.56919 | -49.12435 | 2025-07-19 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d77c45f4-f48d-38d1-8882-13ab447f1749 | -12.42353 | -45.36882 | 2025-07-19 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bed0d6d-7912-3191-8af2-6c2cc4c2e0e6 | -12.71594 | -47.79884 | 2025-07-19 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1b3eae5-a302-3ce0-b0b6-bd419a414adf | -9.79975 | -48.56331 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 95f20719-662a-33bb-97db-d2a6a32d92db | -11.46361 | -48.16 | 2025-07-19 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea0905c2-29ae-3f1b-9d70-de97a662885e | -8.30595 | -55.10723 | 2025-07-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| db3cf1dc-2e06-3dc2-90b3-2e110e791b45 | -12.37337 | -50.33403 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1caeccad-d8e0-31f7-b1e9-9b5d8420edf0 | -9.80659 | -47.74553 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c492319-f65a-3ccc-a179-ada98af4bf78 | -7.11508 | -44.38163 | 2025-07-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3927e6b3-88cc-345b-86f8-d0062490776e | -7.48778 | -63.81979 | 2025-07-19 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fb0a374-347f-3c6c-a40d-ba40b9688a73 | -13.04639 | -49.17315 | 2025-07-19 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4027566b-6178-3720-b06b-3205ebc68c36 | -10.62589 | -44.76562 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 55684340-b0b7-3551-bf78-ba1c9cb8d44b | -12.97006 | -46.91703 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be4fb484-4070-33d6-9ed7-277157c4bb16 | -12.42304 | -45.37289 | 2025-07-19 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72dd4fbf-0cea-3189-9337-6c0e1ba4fa3f | -6.78205 | -58.63202 | 2025-07-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae057f0d-222a-39f3-848a-cd7d82fac87d | -9.80994 | -48.55546 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8cf0cffd-5473-3590-b74c-215bf753b1a8 | -10.98467 | -49.39156 | 2025-07-19 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9de2c95b-658a-3808-baff-e38380d16059 | -10.63171 | -45.23574 | 2025-07-19 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81458e4e-acf9-3d25-830a-f1b7fed86d0f | -11.89119 | -55.44471 | 2025-07-19 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8d57eab7-c428-372f-9c11-2802e3da4f2d | -11.57436 | -47.09502 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5803fb68-1a9c-3e75-9701-c98a8a9732a8 | -11.52497 | -48.9564 | 2025-07-19 04:57:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1bc74db-ce3e-3bd6-898a-65a3967a2f20 | -8.97393 | -61.51321 | 2025-07-19 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c32b94b1-7292-3a21-a506-9c6851705303 | -12.03668 | -48.75804 | 2025-07-19 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25625aca-77a6-37ab-b144-4b010b5b0773 | -8.06459 | -50.08468 | 2025-07-19 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ef6f91b-22f6-3136-986d-c83663c7524d | -7.48885 | -47.49657 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 139834c7-aa88-37dd-94d3-eb6a42b090bc | -10.61955 | -44.76894 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1e732028-30cc-3f76-af64-39b90f3f6ad4 | -12.46664 | -46.92792 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
