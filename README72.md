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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abd377a6-659f-37f0-9453-2b0f4cd1a8bd | -19.64395 | -45.38103 | 2025-10-27 05:40:00 | AQUA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7bcb7e0f-bb63-3f03-94e7-4c9eda1095a6 | -17.32449 | -43.65826 | 2025-10-27 05:40:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8c9ab90-6605-3415-b6bc-cacd3d857c79 | -13.23702 | -47.06301 | 2025-10-27 05:40:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 70cdd072-4214-36f3-9d93-8dea81d12a2f | -12.27965 | -43.75077 | 2025-10-27 05:40:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 249ac92f-2c4b-3634-99c3-64c13c8424c8 | -11.42055 | -46.12199 | 2025-10-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4387a17a-7cbf-3acb-bc68-c848d4719134 | -15.29222 | -42.93284 | 2025-10-27 05:40:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 93168b30-cb6b-3b3e-b3a0-eace8787c4bb | -21.58903 | -43.4946 | 2025-10-27 05:40:00 | AQUA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 015b9dbd-7291-3ab7-bd18-a85441f4d6d8 | -11.42286 | -46.10828 | 2025-10-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 6d25adf5-9d3f-3b43-a761-4003589cf7d5 | -8.96616 | -65.92649 | 2025-10-27 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dacd27c4-580d-3e15-b436-d9f0fba9ce54 | 0.4326 | -50.8163 | 2025-10-27 10:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 120.3 |
| de626aa5-ceeb-3141-91e8-6651fc475365 | 0.4326 | -50.8371 | 2025-10-27 10:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 215.4 |
| dc43cb06-5ba3-3004-865f-3bc132f49b76 | 0.4326 | -50.8163 | 2025-10-27 11:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 954e96ff-4498-3eed-8732-9a3c35f1c851 | -13.3163 | -54.3634 | 2025-10-27 11:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 890c2796-f5ea-392b-b13b-319db9f3abd0 | -13.2589 | -54.3696 | 2025-10-27 11:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| f4782b24-a3ea-3302-9fc0-5f31b5dcad30 | -13.3163 | -54.3634 | 2025-10-27 11:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| ecc62e10-1ffb-3ff3-8918-c59af5f372ef | -13.3163 | -54.3634 | 2025-10-27 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 4f4f3ce8-d067-3db6-be32-87765996740f | -13.3163 | -54.3634 | 2025-10-27 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 151.6 |
| a9c7bbbb-9ca7-30a1-ac52-1abe5270ccf2 | -13.2589 | -54.3696 | 2025-10-27 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| c4c06e0c-22af-3016-a0fc-948fd7bc661a | -13.2589 | -54.3696 | 2025-10-27 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| b3732938-f162-3693-b56d-4bcb28cb532a | -13.2972 | -54.3655 | 2025-10-27 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| bccc6080-1a1a-3273-87f1-227891f2322a | -13.278 | -54.3675 | 2025-10-27 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 27c63d30-b697-3204-bf8b-5db7f84a6d77 | -13.3163 | -54.3634 | 2025-10-27 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| f46f527a-f191-3f6b-99fc-ed3ca5788b8c | -13.2589 | -54.3696 | 2025-10-27 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| f08a1932-ae74-342a-945d-eae588c015bd | -13.3163 | -54.3634 | 2025-10-27 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| f2d88995-01fb-3e35-b09b-4f453f56d7ba | -13.0569 | -45.8599 | 2025-10-27 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c99a9bb4-0454-3f81-8006-f18e63de40d7 | -13.2589 | -54.3696 | 2025-10-27 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| faad61c2-0854-366e-88a4-c7014534b728 | 0.45716 | -50.87135 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ea76503d-a0f2-3b1d-9ed4-005fb32fa2bb | 0.42904 | -51.06844 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dc6b7997-9181-3d31-8574-bd7c9ba7aaa6 | 0.42405 | -50.84628 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 215.4 |
| f02146a5-dee3-3139-9499-c6ad41abd412 | 1.14855 | -51.06137 | 2025-10-27 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 52276fd9-775c-3c21-aa79-a41d5b0f3342 | 0.42279 | -50.83752 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 25e181f1-d115-37c9-ba66-cd124576cd70 | 1.82661 | -50.51633 | 2025-10-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 13.0 |
| dbc4fa97-04da-3223-975a-39474f547bc6 | 1.62359 | -55.716 | 2025-10-27 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 4b902cb8-2060-3a15-8750-9e11f417bd07 | 0.17308 | -50.11922 | 2025-10-27 12:34:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b6ee315e-a448-34fc-a479-71d56a0a56f7 | 0.41524 | -50.8475 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 39e61ee8-2ebf-30b9-b9a0-ffbbcbc07899 | 0.74104 | -50.73282 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ec7d78bf-2aaf-3d34-8586-847827a53263 | 0.30431 | -51.02977 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 17.4 |
| f1463341-0b2a-338c-a707-3080372e4dc7 | 1.1473 | -51.05264 | 2025-10-27 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3a9214dc-2f23-3a17-97ba-544e27f21948 | 0.17438 | -50.12824 | 2025-10-27 12:34:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a4ea717e-8564-3d40-95af-4d6ec580b8a8 | 0.30306 | -51.02104 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ecbf8f9-5b51-3267-801e-d24c2db67929 | 0.42905 | -51.00609 | 2025-10-27 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9e30347e-b832-36d4-850c-4e2a13c96087 | 1.9083 | -50.83494 | 2025-10-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3f0a9996-77c5-34f8-94a4-657fdafa5f51 | -4.44642 | -43.4135 | 2025-10-27 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 82e2a70a-2980-3202-85b9-bd84f510d2df | -4.46037 | -45.45316 | 2025-10-27 12:36:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 6f25989a-2c7d-39fe-9550-4076387da653 | -9.06221 | -45.09661 | 2025-10-27 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 0628385f-c68c-3b61-8707-3ad83aec6d18 | -3.29548 | -43.51757 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| df4748f8-2a4a-3e87-9b0f-427accaf6474 | -8.96345 | -47.19901 | 2025-10-27 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f44e82ce-6429-334b-a1e4-cb6165b53e4d | -7.82528 | -46.49758 | 2025-10-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 6a4de794-4997-3134-b353-f9496f7304b6 | -4.44641 | -43.65676 | 2025-10-27 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 2de53b0a-66b0-3ce6-8cad-424885f3dbf0 | -6.90554 | -46.13282 | 2025-10-27 12:36:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8bfb2e03-c8b6-3d61-bb87-22761639fe17 | -6.66843 | -47.74491 | 2025-10-27 12:36:00 | TERRA_M-T | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 90fae258-219a-3682-8e9e-a79657f6121b | -6.19356 | -42.59765 | 2025-10-27 12:36:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| b0674bf9-4839-3b39-aa48-8021a95d6654 | -9.06096 | -45.09002 | 2025-10-27 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| eae96b12-b816-3cca-8f6c-07c4ff2dee55 | -8.06755 | -46.95086 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| f989a5f9-5177-32d6-a2a5-ab50319b9160 | -3.60928 | -43.55309 | 2025-10-27 12:36:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 43e36924-9da9-3685-8a07-f98e1a92c0a3 | -7.91255 | -45.68909 | 2025-10-27 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| a642e9a9-ead0-3173-8bc7-190113d256e3 | -8.09264 | -47.04596 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 57aef036-383a-36b3-94b3-ce77557d5e79 | -6.87057 | -45.14953 | 2025-10-27 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 05513400-967d-3651-9029-5f9a08e182a3 | -8.03135 | -45.18995 | 2025-10-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d593cbf3-62be-39ac-8acf-af6f5faef4fd | -6.97091 | -47.35701 | 2025-10-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 94139da4-2903-3665-9b04-c0d1b5e0ddd5 | -6.88131 | -43.56244 | 2025-10-27 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| ffd9585d-afb1-35d2-b7bd-8d0a6621ceb9 | -8.11697 | -46.95698 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 282964ef-da18-3376-9f46-66365486b5a2 | -4.44872 | -43.65152 | 2025-10-27 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 0a95f138-9de5-3e98-8e61-11d886b172a8 | -3.70339 | -44.34381 | 2025-10-27 12:36:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 49473bec-3a1b-3c75-b714-d6039f17365d | -4.15889 | -46.79159 | 2025-10-27 12:36:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5910dbcc-c0c3-319b-ab4f-b36c2f389543 | -7.25757 | -44.9667 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 03d476c7-811c-3ff2-914e-b36b8366ce54 | -5.77367 | -42.9688 | 2025-10-27 12:36:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 264e6ef8-c821-3fef-ae7b-428830fff932 | -6.87685 | -45.16802 | 2025-10-27 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 94c394d3-cdc2-38d5-b365-4cea150ed3fb | -8.45415 | -48.20545 | 2025-10-27 12:36:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e2d44874-4732-3f0b-9ab4-79ef67f535b2 | -3.70671 | -44.31857 | 2025-10-27 12:36:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| a53abc4f-d420-3930-ab45-cbd21e9ed984 | -8.02875 | -46.75706 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| dccfda9e-a778-3958-a650-64a9e94e3889 | -8.22831 | -46.92796 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| bf635b46-000b-3f4c-8e9f-eca944a6e87d | -6.8774 | -43.59505 | 2025-10-27 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 2d60d210-5232-3aad-a12b-2f0498e5f092 | -8.09019 | -47.06446 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| cee4788e-afa9-3657-8393-e7a2b99e74fd | -7.52746 | -46.27291 | 2025-10-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 43867d8f-2940-37a4-9e78-bf9214264b9a | -8.53193 | -47.1873 | 2025-10-27 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 77a83227-52a9-3880-ba04-adf8d98f85f3 | -4.39002 | -43.29997 | 2025-10-27 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 430ff39c-acc5-36e9-8189-b14bd2e7be76 | -8.02956 | -46.73202 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 3b48a439-47fc-35e5-94a1-ace024925734 | -3.69997 | -44.33657 | 2025-10-27 12:36:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 504da2eb-9de4-32ba-86c9-934ef5fab652 | -7.82054 | -46.43118 | 2025-10-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 88ff66fe-0871-3402-901f-141e9cd68643 | -6.42721 | -43.15745 | 2025-10-27 12:36:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 7901dd28-8687-3965-acb0-68830cabdefc | -4.40052 | -43.30825 | 2025-10-27 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 66146dc6-1c0d-36c1-a8e6-e75a9a094e56 | -7.34516 | -49.93418 | 2025-10-27 12:36:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fc4f8170-435c-36b6-9cc4-a78ac0920820 | -7.13743 | -47.06048 | 2025-10-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 4300b23f-1304-312d-bec7-ce23b95bc75b | -8.5359 | -47.19365 | 2025-10-27 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| c405126a-2fbd-327e-b582-c4c3eb09000f | -8.03461 | -45.1641 | 2025-10-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 04e3c9fb-9432-3c53-a890-2a7da454ce27 | -8.27281 | -46.87642 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 64563057-2669-3406-9438-0cab70535125 | -8.1073 | -46.96249 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a14b3a9a-a446-3a83-80aa-e39bb8f5f77e | -7.95101 | -47.2369 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c65b4771-02ca-38b1-9e16-d742117e759e | -7.0733 | -44.95131 | 2025-10-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c37f1983-d245-320f-b388-d68d2fe1dde1 | -7.00657 | -46.98433 | 2025-10-27 12:36:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 9575f309-cfc1-3721-b190-961dea74959c | -8.18302 | -47.28482 | 2025-10-27 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a305aadf-0965-3926-8b30-ce6c82c419c4 | -6.43178 | -43.12257 | 2025-10-27 12:36:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 3e208a86-7d6d-348c-b165-bec4ec569871 | -8.70216 | -44.42069 | 2025-10-27 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| f528d5dd-31f7-33cd-84d1-83291ac929bf | -8.48976 | -45.55656 | 2025-10-27 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 0540e349-13e3-3f61-a6b4-7aa7ea33f8db | -6.88409 | -43.58965 | 2025-10-27 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 638.7 |
| 809e0190-c202-34b4-bfca-dd2d70695e71 | -7.76627 | -45.39498 | 2025-10-27 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d165eac7-145a-36d7-a3bc-13c0acaa1eb3 | -6.97305 | -47.34048 | 2025-10-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| a8998486-dfbe-356a-b8f4-e8d021ae113c | -3.34018 | -42.86471 | 2025-10-27 12:36:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| a3eddeaa-4596-3471-a6e8-a88d62683c8e | -8.0311 | -46.73802 | 2025-10-27 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |


[Clique aqui para ver as próximas entradas](README73.md)
