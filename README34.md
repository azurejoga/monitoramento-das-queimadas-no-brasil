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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0694b645-b071-3495-8c18-9b91afd6e1b8 | -1.11334 | -53.4009 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6d3a82d-6b34-3f71-bb56-d5e0169450ef | -2.70887 | -46.10054 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cf2cfe2-dac7-3376-9797-16098e978045 | -1.60473 | -52.60708 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8aab8da0-1253-315e-ab91-f8b7ce43259e | -1.65929 | -52.70816 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1b3243c-7278-39e9-a994-6492839f5017 | -1.25893 | -53.36387 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 560faae4-723c-3142-9238-86862625f6a5 | -1.19344 | -51.77631 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc33ce33-606f-38d1-9242-5c979dfa84e0 | -3.2283 | -46.4314 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5d43d72-6f0a-363a-b74b-055416b53d2b | -2.70652 | -46.2734 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 51be984c-7208-3449-8547-e01aef40af4b | -2.57036 | -46.56187 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c5460a-3aa3-3c54-8a79-a9544d34a54d | -1.72712 | -52.71597 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4edc0f8f-7ced-3974-9ebd-fe1d87e98545 | -1.74783 | -52.39233 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48aeac4e-4d36-3945-a1f1-30a319410c87 | -1.30921 | -51.75309 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b40d85-12c9-3bb5-9c24-c8fe1fabbb00 | -1.74328 | -52.38464 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b553461-1a09-3dab-ba7b-c2cb56bdc027 | -3.14784 | -44.48478 | 2024-11-23 04:16:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efcc479e-9f08-3317-9a0b-03b9bc076427 | -1.26092 | -53.36398 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0957a2dc-b692-31b8-9640-f66e5d82c118 | -0.25704 | -51.57026 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35d1d7fe-c858-34b4-b51e-78c910ca50d4 | -2.82009 | -45.15862 | 2024-11-23 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dc44fc1-8a21-3a38-9be3-866caf06c912 | -2.20627 | -48.91875 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fdb98dbf-95bb-3e59-a000-02a700e2474a | -0.04458 | -50.81958 | 2024-11-23 04:16:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f45ef763-6d92-377b-971a-68623b690077 | -1.12963 | -53.40754 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 18d58fc6-f93b-3ad8-90f2-185674718227 | -1.74419 | -52.38198 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25af1106-8a14-3e9f-af10-6c914ae356a8 | -2.66729 | -46.16054 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06864e7f-2c96-347c-a3e0-aa4b5fdc49f5 | -3.14122 | -44.48375 | 2024-11-23 04:16:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2418f446-d6c0-3031-affc-5661bac04d4f | -1.60873 | -52.58976 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d46ed63d-cf3e-318e-acf4-0e79ea27cca6 | -2.17075 | -47.94871 | 2024-11-23 04:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2551c4d2-ec06-3fdb-88e3-c9b3261dd089 | -1.20522 | -51.95298 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0384553-0a3b-3751-a90c-acb4495d1e2c | -1.10771 | -53.39991 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8eff262d-9417-39b7-9fcb-025410810770 | -0.27223 | -51.59851 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2395f818-1bbc-35d0-a65f-90a5c7505e46 | -2.7129 | -46.27836 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2d96846e-9e0d-3e75-82b7-cd9bdcf63e5e | -2.53133 | -46.39802 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65cd6595-4877-3372-aaee-ec210e89b67e | -3.17814 | -46.54376 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 386b53cd-47dd-3d22-8fb7-00ef168b0494 | -2.70374 | -46.08804 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bc4343f-7586-3497-af35-f711e74f6f63 | -2.5739 | -46.56244 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f69395b4-54c5-3698-acee-bd71fb95a090 | -2.19278 | -48.21213 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b16c8baf-1eba-3f6f-9844-31b21ffb909c | -2.61647 | -46.20013 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a26c7f7c-3cbb-383b-a60f-f92113b82dcc | -0.91035 | -51.64987 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af59d408-4ebb-3673-a217-7f38cb61aa6b | -1.83393 | -54.52773 | 2024-11-23 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f156477-1e24-3383-a94d-0c9726081c0a | -1.7777 | -53.6125 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95465874-6004-3a61-a634-a4d1f741e43a | -3.17751 | -46.54768 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66598d31-e093-38b0-80a1-1bb2be0c4194 | -3.12412 | -45.91309 | 2024-11-23 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff86dc68-2973-3204-b8c1-f6b63e732e3f | -3.16019 | -45.90738 | 2024-11-23 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbdcff4c-c6b7-3745-9a1c-a6bd718d88ca | -2.68181 | -46.15889 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e9dbc88-1d29-39cc-a7df-b1bd5312af43 | -1.88271 | -47.88618 | 2024-11-23 04:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beefbbc2-4378-392d-bf64-9505e90a1386 | -1.28354 | -54.54468 | 2024-11-23 04:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a2ba70e-1087-36c1-b611-a94223cadeb0 | -2.57476 | -49.09253 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf0b8106-91d8-30bb-975f-c771a982ad8f | -1.63162 | -52.41185 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d12ba950-9d9e-3525-a18a-b3dccc7a7e17 | -2.6874 | -46.25851 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e02ef8eb-cb39-3b5d-974a-fdb5026272c9 | -2.45024 | -46.54459 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1980440c-b491-3da1-9203-c2077234fee6 | -2.728 | -46.09188 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 997f3644-df0f-346b-a351-03731ecd8fcb | -2.70149 | -46.07991 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ac2d322-dfdd-3c15-83c0-eca584e1cea0 | -2.7088 | -46.28168 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 95ad9e59-8ec7-31eb-b832-6e96935f963f | -2.59209 | -46.19622 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fd80bb2-344f-37fb-a5ab-93a33a790da1 | -2.5292 | -47.52096 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f47c312e-1d62-3ff6-9574-ba973886768b | -2.62834 | -46.22527 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80699dbc-05e2-37a2-a926-0723212906a0 | -2.67756 | -46.25293 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e8234d9-0c99-384c-ab6e-aa1c9a30a9a9 | -1.63831 | -52.10114 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11c4278a-eb67-30f6-a2c7-865b6acf3a13 | -2.52907 | -46.38961 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71ac1de1-f968-3cce-8108-6a0d044b5f02 | -3.14453 | -44.48426 | 2024-11-23 04:16:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39a94e27-43f7-3e79-a869-91a02907f588 | -2.60193 | -46.20175 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60e6e2d6-d62b-30a8-b872-22d2a576a35e | -1.79026 | -48.44346 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fea81dd-db4e-384d-b054-98e2070ead8d | -1.93456 | -46.82725 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bfb2933-4a4c-3f32-8844-b88c77161d30 | -2.68104 | -46.25351 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 447dd392-19ab-3bea-850e-b11245eccae6 | -1.22358 | -51.74319 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3537db1a-fc08-3392-9ab4-56e5cefbbc4a | -2.61708 | -46.19627 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9282e58b-822e-347e-a44f-bd8f0263f8b7 | -2.7158 | -46.10165 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef26ee21-8b04-3148-bfc2-b79993d15cca | -1.45492 | -48.20235 | 2024-11-23 04:16:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c49ccdef-303e-3d32-be6b-ea0939f92965 | -2.79187 | -45.95029 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eefe96cb-36ef-30bc-b780-9add36f13063 | -2.61359 | -46.19572 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5d28774-6b5f-34bf-a55a-4c70f6d4215e | -2.82288 | -45.1627 | 2024-11-23 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 270f6739-fdc4-3654-9aff-b731f784e829 | -1.74366 | -52.38514 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf6784d5-99d8-3a5e-ba1a-ff4844f306ee | -1.61588 | -52.60556 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f908b8d6-b67f-3c9b-bab0-71339554a8b8 | -2.38222 | -47.83797 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03a08bfb-1ac9-300f-8b58-b9d1f66f99ae | -2.56462 | -46.55343 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6ac39a9-d23a-30d9-96b2-917767fcd889 | -2.42632 | -46.51216 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29ea5df7-bd15-3690-acaf-9e54396d27c2 | -1.93745 | -49.53268 | 2024-11-23 04:16:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f327df3-dfc7-3ee7-a3f2-37c4c0cbebf9 | -0.95595 | -51.72008 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51636335-e85a-384f-ba42-a95d1f5af982 | -2.92939 | -48.05243 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b81a3efe-830a-3dbe-8dc9-0542325291eb | -3.19034 | -46.55777 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe16cc6c-adfc-3602-8535-5e584bad4db9 | -1.73082 | -52.72689 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 14b6c546-391f-34d9-98b1-93316667b00e | -2.18605 | -45.68152 | 2024-11-23 04:16:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 737987c4-c08c-3d5f-bfd3-b6935a8c0c29 | -1.04462 | -51.74129 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 099662eb-6001-3f49-bd08-762706685f58 | -2.24808 | -49.22122 | 2024-11-23 04:16:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 346024e2-8b70-354f-8d6a-7a933e4a0562 | -2.69014 | -45.66442 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3784d301-62b9-3288-8106-029e408c71ac | -2.45096 | -49.0844 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f07613d-166d-31f5-9edb-4703e451f660 | -0.95044 | -51.72218 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64b3ae3a-0e3f-3868-9238-fcdcc9e1e891 | -1.28918 | -52.26573 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c71327e3-afa2-3748-ab0a-369d46b85c03 | -1.60378 | -52.57993 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4cc163c-8fac-331e-966c-3fd922958f21 | -1.74378 | -52.38147 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 665211bf-933e-3c8b-95fd-db50b950306a | -2.65932 | -46.14355 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff8fd196-e9e3-3de2-b9e0-3965f342ab9e | -2.70668 | -46.24967 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed019345-a769-3c54-8d0f-07eb16771794 | -2.57417 | -49.09622 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f399e7d-8ab3-3e6b-af8f-b866658886e5 | -2.82624 | -45.16323 | 2024-11-23 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 101163bf-04fb-313b-a9e9-521f21025e1e | -2.64194 | -46.14085 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43857b65-ef26-3eb8-bbe8-9030fea27a21 | -1.52578 | -51.62373 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 99683a5d-778f-3e06-badf-0cf33efff5e8 | -1.79483 | -45.71765 | 2024-11-23 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72549883-7556-3732-b751-f0ba10ff35d2 | -2.68467 | -46.16327 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1715856c-b33e-33b4-a250-a841af5c7d9a | -2.45859 | -49.03667 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2718a6b4-cf37-3cde-886a-601d6f2683b6 | -2.26866 | -46.20347 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 446ca0c6-bcc7-3417-be18-7139e4a9e968 | -1.60083 | -52.60534 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 200e5575-72f6-3b73-a6af-1630da5cb9bd | -1.89558 | -46.43328 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README35.md)
