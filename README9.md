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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4c8111b-0c13-317e-ab4d-7e06c52d2f03 | -9.36343 | -44.72903 | 2026-07-28 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffe7fd4d-40fd-3695-8786-140eeb863091 | -7.73215 | -44.55794 | 2026-07-28 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15ea1aac-1394-3b2d-a8a4-eba6c0791b97 | -4.94695 | -48.24764 | 2026-07-28 03:55:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35d9410e-f8a4-3f95-885e-bb5ef389f60a | -10.26665 | -49.73069 | 2026-07-28 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f7dbff06-b74d-3ad5-8a5b-65ec5597fe48 | -11.77713 | -47.08669 | 2026-07-28 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 89adc92d-0fcc-38c4-b9a9-bccc9d89b7f5 | -5.423 | -43.42677 | 2026-07-28 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7ff1bf8-697d-3f54-9118-9bc03b01a94d | -6.1229 | -43.76605 | 2026-07-28 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2906badb-3c83-3ef2-9cf0-582d85dc5a4d | -7.4631 | -49.73025 | 2026-07-28 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4afbf222-85e1-3d59-99c0-82744c7d1338 | -7.25162 | -43.12971 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9a1fedac-393c-3de5-9b48-825007ca837f | -7.25384 | -43.14023 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93a0ba60-5690-3cdc-bf9b-0cf9e0ac4bf8 | -7.62002 | -38.79724 | 2026-07-28 03:55:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d2c6491b-2e08-352e-a1cf-70a44179025a | -7.46105 | -41.1129 | 2026-07-28 03:55:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 2892ca76-2dee-3c2e-880c-b626ff89d81f | -7.41211 | -46.83499 | 2026-07-28 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e146fc7-e1cf-31f5-b358-c686170646ea | -13.31829 | -40.46134 | 2026-07-28 03:55:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 29cdca7e-5561-339a-963e-3dcba4ffa7c9 | -9.6063 | -47.76638 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d56e4d38-792a-3005-b525-ecb18ec669ea | -6.8727 | -46.00787 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0785854b-bf02-3159-8df9-1186d3e9c1f9 | -5.4905 | -45.12176 | 2026-07-28 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfe4ccec-a780-32e8-969e-bb6fc548d034 | -11.78182 | -47.08762 | 2026-07-28 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2dc96b57-890d-30d5-94b1-80f5510ea203 | -7.83431 | -47.10094 | 2026-07-28 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 261d7e54-03d0-39b8-a356-737942bedc2f | -6.4775 | -42.22969 | 2026-07-28 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 71eef94f-0dab-301d-aa0f-fd5f90d42e99 | -10.93883 | -43.05687 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0eb78a32-c0c2-32e8-832f-9c53f753ccc6 | -10.9322 | -43.05117 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.1 |
| d40c65e1-0c14-3c4d-9728-fd5c66c2021e | -11.78058 | -47.08485 | 2026-07-28 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 56356897-74fd-330c-921d-3f08ef7cf368 | -9.41589 | -40.79385 | 2026-07-28 03:55:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0408bc87-8e6e-3366-9d8f-4c36cc02467a | -11.78277 | -47.08257 | 2026-07-28 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0e25fe0d-cc2f-3cb5-94f3-6af32d0f60a1 | -7.40766 | -46.83111 | 2026-07-28 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85d35f88-df4e-3eda-847b-1ddce4d580a6 | -7.24909 | -43.14452 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ded6aeda-dc3f-313e-b994-7cb0970e365b | -9.60905 | -47.76449 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d55200a-b9da-30c8-aebc-d17327c4df3e | -10.94326 | -43.05307 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 370e738a-c6b7-3e06-8818-539316c3273b | -6.86881 | -46.002 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bdda29ff-64ba-3cce-81a8-b87920b342d3 | -7.25307 | -43.14277 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 90b7b654-220d-356a-b2ec-63f3e2f5cf27 | -7.62278 | -38.80122 | 2026-07-28 03:55:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ecb87f5-f4dd-3586-89ea-bf6c7f50287c | -11.82851 | -38.27053 | 2026-07-28 03:55:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 38dae230-690b-3b56-8e89-ba0771687050 | -9.78106 | -49.1968 | 2026-07-28 03:55:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee359475-644b-3baf-9650-d05435685dbc | -9.60802 | -47.75713 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67dfa8f6-2b2b-32f4-88fd-96fcad7dc693 | -10.7493 | -42.09658 | 2026-07-28 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c9afabd-c557-3e88-9872-4f79e4073a4a | -5.59487 | -44.92253 | 2026-07-28 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d6212b9-7e4f-3ab2-88ac-e5475f3f66c9 | -7.24445 | -43.14643 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8923a497-65c3-320e-9f75-d0e5e70b7dfa | -9.77778 | -49.19302 | 2026-07-28 03:55:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 58526899-d91f-3c04-aad3-f3a2aa6efee5 | -12.21213 | -38.98352 | 2026-07-28 03:55:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 23b2aa37-2c7e-3f15-bb04-196d93eab99a | -6.87009 | -45.99903 | 2026-07-28 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff1d12f0-a61f-3bfb-9b9b-66b2725de3b0 | -8.80352 | -46.71886 | 2026-07-28 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afb4b081-89f1-3b92-a265-c4e84750bda6 | -7.24607 | -43.13651 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63f81ec7-f5f7-3d16-81da-addcd33a3555 | -6.87394 | -46.0049 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 18a9e728-00a0-34c4-9d48-5c07c261ba43 | -7.25078 | -43.13223 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2cbd588e-2382-3bbd-b1c7-91695307f9f5 | -10.75062 | -42.08855 | 2026-07-28 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3b23f187-fa07-3056-9d3c-4410606b4549 | -6.16135 | -44.64582 | 2026-07-28 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 835ae6ed-cfc3-3fad-838c-d926274bad38 | -9.61014 | -47.75832 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baf358a5-1cf4-3ca2-817c-2545761ad8da | -7.00856 | -45.42788 | 2026-07-28 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6dcd9e68-978e-3aa8-8b22-da283cf408ef | -10.26743 | -49.72665 | 2026-07-28 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f10bd5d1-093e-355d-af79-bd1aa1af5418 | -6.87357 | -46.00275 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8721f320-a61b-35ff-8f25-b47301be1dac | -9.9324 | -47.90387 | 2026-07-28 03:55:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64b61d99-6ead-3009-ae95-f988f0b6de1f | -10.37982 | -49.581 | 2026-07-28 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 492c7a6d-a947-33d9-9cb6-d2be5002224f | -11.98335 | -45.54887 | 2026-07-28 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a83d323-47c4-32fb-a454-6261b902c2eb | -6.27809 | -41.77378 | 2026-07-28 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 128bb887-af65-3fff-9de5-7332f64c5bcd | -9.60959 | -47.76144 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96748d4c-005c-359d-a5f6-cee555456157 | -5.82618 | -43.4896 | 2026-07-28 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f9a8cb9-6417-315d-9497-f15a6e56bdaa | -6.87485 | -45.99977 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49d7ba2f-4342-3a30-b5b0-3a2bc512a83a | -6.48569 | -42.22652 | 2026-07-28 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0a9d8208-b458-3e6e-bf68-0b3cceeb46cc | -9.61138 | -47.76744 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b79c9011-5463-3c23-b84e-ff00a9743e94 | -7.24135 | -43.14082 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f5665e67-cc47-3e81-a721-ff5c9208d329 | -10.74996 | -42.09256 | 2026-07-28 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6daba6bd-0510-38c5-94ff-19857d882c1a | -10.94695 | -43.0537 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 38c794da-12d3-366c-bcb3-5ab847678d7c | -6.86917 | -46.00418 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e3453ca2-162e-3845-8969-dd03e2ef1c69 | -9.60743 | -47.76026 | 2026-07-28 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d681a3c1-af26-31e6-894b-146c9e1046a0 | -6.12768 | -43.76286 | 2026-07-28 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4de8c915-6192-3841-b295-68fb254fde61 | -6.87444 | -45.99759 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 36ec193c-6c23-3376-a3e1-8394ca037591 | -6.47675 | -42.23422 | 2026-07-28 03:55:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 95cee7e8-9c89-3845-8c9b-0815fcefa839 | -11.8895 | -43.83111 | 2026-07-28 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d321c7eb-9bac-33c3-99e7-f4b7f6c0cf11 | -7.24917 | -43.14212 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9e7bbdde-b6fa-381e-a011-83e031ce8e6c | -7.67649 | -47.20327 | 2026-07-28 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 701ff48e-a838-32a2-bd44-fefaed297847 | -10.38057 | -49.57705 | 2026-07-28 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 106640a5-21a1-3ed4-93f3-2aef1b137f17 | -8.13799 | -46.77927 | 2026-07-28 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1de44a0f-522d-37a6-9c8f-ddc15058dd57 | -10.94547 | -43.06257 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 9bb8e314-49d6-3dc1-84de-9bf945a06ff5 | -7.83484 | -47.09794 | 2026-07-28 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 601b4e10-4b03-35aa-b0e9-a42951c7c272 | -7.71339 | -46.52786 | 2026-07-28 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e414c3d0-089b-3548-91ee-4fd2d6711c86 | -10.75349 | -42.09315 | 2026-07-28 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22d2ba30-27f7-338e-8ec5-24c21e2780ca | -10.93663 | -43.04736 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f394be0d-e0f6-3343-b6dd-92b9fa7070dc | -11.77808 | -47.08166 | 2026-07-28 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2eae26b-b823-3612-a386-784a70f44384 | -9.34051 | -47.90701 | 2026-07-28 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e00855ab-3dba-38a7-8989-050be4a5c30e | -7.41261 | -46.83216 | 2026-07-28 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2e44406-4fb5-3fa0-a8d0-2ad7669df5d5 | -11.98685 | -45.55365 | 2026-07-28 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10537d7a-b8ac-334a-bede-e86dc0826911 | -9.36761 | -44.72976 | 2026-07-28 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e29bdd1-f8bd-329d-bdca-0954b894fd52 | -9.6615 | -40.60053 | 2026-07-28 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 941bafc3-3a16-390e-ac15-61df423514c9 | -9.33476 | -47.90919 | 2026-07-28 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c8657f6-44e3-35e3-a3d0-15e3e63f6d32 | -6.86794 | -46.00709 | 2026-07-28 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b931301c-1be9-33d8-9c29-d92257f781b4 | -12.39852 | -40.40451 | 2026-07-28 03:55:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4fdde580-8af0-3a8d-a1f9-18b2a0b9021d | -12.49532 | -43.7704 | 2026-07-28 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 441531cf-3e50-3942-b988-a78a0f09c323 | -10.93589 | -43.0518 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9b5ba744-de98-3275-9243-3eb17ccb7fc2 | -10.94178 | -43.06194 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| a4c2d89e-2e8f-3096-a844-e9f074ba4d09 | -9.85576 | -45.55443 | 2026-07-28 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 282bf232-a57e-384b-b584-77d0ea610869 | -7.72209 | -46.50673 | 2026-07-28 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad4538e4-b199-323b-9dfd-47b3c2ab3fbe | -12.03916 | -47.80035 | 2026-07-28 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38bbf1a4-db3e-3f95-b609-1a3735add25a | -12.62446 | -44.62344 | 2026-07-28 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edd4fd8d-04ca-3cf9-8cf9-57deed1f60c7 | -9.33995 | -47.91012 | 2026-07-28 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59bf67cf-df64-3826-99ef-f9d886e63372 | -10.94252 | -43.05751 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 61702a52-05d7-3f35-b4e9-80580128b2f5 | -7.25388 | -43.13784 | 2026-07-28 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 59370231-2cf6-3788-b0f5-790c202ef9e9 | -12.49237 | -43.76509 | 2026-07-28 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c913c3c6-7fc8-3bab-b6c8-78f15c9e86a5 | -7.40717 | -46.83388 | 2026-07-28 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd30721a-2e0f-3d32-9f75-b4bb4b9cab7a | -6.48196 | -42.22586 | 2026-07-28 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |


[Clique aqui para ver as próximas entradas](README10.md)
