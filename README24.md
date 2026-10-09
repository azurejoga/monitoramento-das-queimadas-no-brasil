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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37484d03-e513-30ee-bf93-9ee369e42909 | -9.1193 | -45.829201 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b7c45cc-fd04-313a-ad8f-2f16ff7fdca2 | -7.0972 | -47.731499 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28d6461b-0251-3074-adb1-d603d7e24b96 | -14.8676 | -50.308102 | 2026-10-09 00:28:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2276744e-ea40-343d-8054-10c885aa7f6d | -7.0501 | -45.434898 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9945c3ac-6e6a-3b0e-8793-8d84256198a1 | -2.8747 | -54.175098 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 197790f9-b4a7-307c-b489-3a8ce32d50a9 | -1.7298 | -52.2374 | 2026-10-09 00:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b2f0eb-6b45-3073-a0d9-bd44c09fb335 | -5.614 | -44.843102 | 2026-10-09 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9a90c0f-c558-31fe-9b54-f7b766ade603 | -12.0013 | -43.502701 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc3160cb-bedb-3424-ad76-2a75acbc15c0 | -6.8879 | -45.897099 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42dff675-3bd1-3613-bf8c-52c2b545befe | -2.9749 | -54.120701 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ffee66b-5d86-3fd9-972e-d2cdd22c9cf0 | -8.9061 | -45.2089 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bda2814f-a11b-3d71-990a-017989942ad4 | -2.9852 | -53.848099 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f93110d-c3e5-356f-8990-ff8646471519 | -13.1668 | -46.876099 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44793262-d530-38dc-8867-a38581c96257 | -11.7888 | -45.609798 | 2026-10-09 00:28:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 768aecc7-93cb-30c2-8662-91dc71739d30 | -8.7336 | -45.175701 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0751ea-1bb4-3e79-b4b9-5e9112032814 | -11.6293 | -43.724201 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc35e8e0-a86e-339b-b16d-262fd4f0b53d | -7.5145 | -47.344299 | 2026-10-09 00:28:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5870e0c-14fe-35c8-886e-6362cdcbd071 | -5.9943 | -40.933601 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 124d3dae-f5ef-3cf9-9ad9-91d32f7b103c | -9.2266 | -45.666302 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1d085c9-5c0a-31bb-ad4c-5909f68685be | -11.7906 | -46.7803 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba7492db-4275-3ccc-b580-3910b30e8fe4 | -6.7229 | -55.168701 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de4e88d5-d038-3d93-81a5-4340784575ec | -6.5056 | -44.371601 | 2026-10-09 00:28:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e230c55-5beb-3d10-882b-62f5d22a2ba8 | -4.2633 | -46.278801 | 2026-10-09 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98f6b8ec-3f50-3ac5-8b26-c6c10bc2e226 | -4.092 | -48.963501 | 2026-10-09 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f929174f-22f3-36f2-b201-813631447001 | -9.086 | -45.138901 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f617a3a-540e-30bf-b88d-283d7a82a1f3 | -8.0338 | -49.407001 | 2026-10-09 00:28:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ced2688d-519a-3490-b2c6-14d5bb2bc648 | -2.9902 | -54.0527 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb7caa89-00e9-3523-a00a-8f284034741f | -4.7964 | -45.770901 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c806a88-6319-3721-8f8c-921bb7f20a0c | -9.6041 | -40.620201 | 2026-10-09 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e29113dc-c58e-3e52-95bd-f40cf651f70f | -6.0627 | -44.108799 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13d02e1c-4191-3966-865e-f02fc401c369 | -16.900299 | -40.8993 | 2026-10-09 00:28:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73f3a8ab-26f8-3332-b268-3a6fcb4e1221 | 0.7765 | -51.975899 | 2026-10-09 00:28:00 | METOP-C | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba0850f-cfab-3adb-8f5a-72019b751baa | -8.9077 | -45.215801 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9d36568d-7065-3824-a8a1-c845f46b2c9b | -11.0738 | -44.090599 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aea29984-f24b-32ba-8cf8-381d4c6ad83b | -4.2905 | -48.6124 | 2026-10-09 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3905a4-ace5-36d0-98c2-24a51f98d0f7 | -6.9384 | -43.659199 | 2026-10-09 00:28:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48acbcbe-9b9a-3db7-b5b6-5e27e24ae5ea | -10.262 | -44.644501 | 2026-10-09 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d994236a-1540-3b1e-9f3c-d02c2b06d881 | -7.0988 | -47.738998 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0a43aa3-7f16-3b37-bad4-39eed7c1ea6f | -9.291 | -47.469299 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1079e7cd-a986-3607-b0ac-79b2267cb6dc | -4.9898 | -44.999599 | 2026-10-09 00:28:00 | METOP-C | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b58b42a2-3b28-3e3d-a6d1-fe3fd8acca57 | -4.0292 | -54.226799 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349ab75c-011a-3bb1-90fa-2736a1814dd8 | -7.5106 | -46.096802 | 2026-10-09 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0daa13-eae8-3c81-8af5-9f32343f8273 | -4.6104 | -49.208401 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8dac6a-c514-3f86-ad54-53bbb78153f2 | -3.5494 | -54.683102 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c70726-4f93-3017-a481-69c294d2f9dc | -5.6379 | -45.797199 | 2026-10-09 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7aff9836-12ea-3bfc-b241-1449dded34c9 | -17.612301 | -42.3176 | 2026-10-09 00:28:00 | METOP-C | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71290236-2e8e-367f-b425-76cc2e168177 | -6.0342 | -44.030701 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ef7d238-30f8-3887-a651-9dcb012370fb | -4.6676 | -48.9604 | 2026-10-09 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9145eb-a40a-36b6-af86-ce1afbce0a86 | -4.9882 | -44.992599 | 2026-10-09 00:28:00 | METOP-C | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 363b0032-0f8f-3d27-a96d-2bf064e390e2 | -7.0874 | -47.7337 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1b862c3-76a4-30e9-b742-c2b2bb238d21 | -4.5387 | -47.030998 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32c86156-736d-3fc0-b60a-a0c7f0cb7866 | -21.0837 | -43.290501 | 2026-10-09 00:28:00 | METOP-C | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40765ed8-5438-3540-b6a5-58d265cefd76 | -5.1039 | -46.212002 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23a1370a-aa6d-3e6a-841b-341764bec7d8 | -10.4555 | -47.860001 | 2026-10-09 00:28:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7ef1e9b-d23e-365d-b8b5-ebfd3088a0d9 | -9.9115 | -44.870499 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89d311a5-5449-3470-ab25-27c1fff940ae | -5.9416 | -55.352798 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa12144-0112-377d-8c98-8afc9d0e58a3 | -12.0274 | -43.481499 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcb41e1e-f2b6-3046-9937-06a19f426e83 | -11.998 | -43.4884 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1df4c073-3b9a-34a5-bd7a-37418997f81e | -5.0957 | -46.2211 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b06d9441-133f-3c8d-a2cd-b278d5828383 | 3.7451 | -51.617001 | 2026-10-09 00:28:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ae507fad-fd88-3db6-96f5-85cc735e06b0 | -9.7784 | -44.784599 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da878b53-96ed-340a-ba0a-258033f9b847 | -4.9419 | -45.7309 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf61a2a-f65d-3033-9b7c-c87cdf145f0e | -8.2046 | -46.431198 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 844b3f33-38f5-34d7-a4b9-7a1865b3ed8e | -9.7588 | -44.789101 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf489b3e-e0db-3833-b84e-3a82103513cf | -2.7405 | -54.123199 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8cdd31b-5788-337c-abb1-43ed79627607 | -13.1919 | -54.345001 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5eddc940-90cd-31f1-9b33-4699fde4cb46 | -18.7869 | -46.475399 | 2026-10-09 00:28:00 | METOP-C | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e4337bc-3d87-3bfe-8c52-cc779d1c019f | -5.4155 | -45.861698 | 2026-10-09 00:28:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 074c2635-a70c-307d-9459-a2849a0bb737 | -11.4688 | -43.386902 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82980456-5a5f-37a5-ac5b-5bbff57b209e | -6.0017 | -40.964802 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bfd1b4b8-1d78-3b1a-96f2-2e21d4cade2e | -7.2213 | -55.132198 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1cc5c1a-1d8e-3c00-9339-164942671558 | -1.0021 | -47.661201 | 2026-10-09 00:28:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3483d6f-351e-366e-af52-9a553725d3f5 | -2.7496 | -49.534 | 2026-10-09 00:28:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 491d4475-1663-3947-912d-fc43ee895c49 | -6.8848 | -43.695099 | 2026-10-09 00:28:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36a9a7f7-ed39-367a-8e56-714df811b157 | -14.9586 | -41.434601 | 2026-10-09 00:28:00 | METOP-C | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5aadb80d-b131-3e07-8ba2-765413ff2973 | -2.7478 | -49.526001 | 2026-10-09 00:28:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45e7989c-9cd5-3d82-b082-01146f7cd1bd | -7.3414 | -45.3111 | 2026-10-09 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb324b79-5cb3-3ac7-aa01-c9f80778177c | -2.9165 | -54.1334 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6858cbf9-381b-3a06-826a-846f7cc9a3f5 | -4.5666 | -54.956299 | 2026-10-09 00:28:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf98489-3895-3bd7-ae03-d18c980d778d | -11.8529 | -43.574902 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87dc3e77-e10d-365f-8b16-926453a0c7cc | -6.979 | -47.663898 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58b507a6-9f60-31af-849a-8ac1041ca84e | -9.0415 | -47.735001 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32482004-8c36-3709-9018-38005fe3a60e | -8.905 | -44.933498 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9722575-76c7-35f8-9acc-de46c2938b35 | -11.2966 | -46.683498 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 850b6d63-66c3-3ef3-b829-d10eabe20c3a | -8.1647 | -48.602402 | 2026-10-09 00:28:00 | METOP-C | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f70057b9-a22c-3756-adef-39947c8a7eb3 | -11.7923 | -46.787998 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0b0cd9f-be2b-365c-adfc-b1b72c38bce7 | -9.6334 | -48.8904 | 2026-10-09 00:28:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d90e58bb-1f92-3aa9-8080-7076db3296ce | -4.5055 | -43.6259 | 2026-10-09 00:28:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8dabc00d-412f-3a19-bc4d-70f2c0438348 | -6.8828 | -45.919899 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d99ca77-2903-3f7b-a893-40500aad68eb | -5.9461 | -55.373901 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8687f0-39f7-3964-8d84-23dd9c36882e | -13.2607 | -44.001801 | 2026-10-09 00:28:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfab5220-f3ca-32cd-89e9-1cb0a3222328 | -7.6957 | -45.461899 | 2026-10-09 00:28:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 362fa8ff-362f-3966-8af2-a631c34633a3 | -18.3297 | -42.386799 | 2026-10-09 00:28:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb9e4866-580f-36de-8a67-e3672ddbd9aa | -9.8607 | -47.489399 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8b86ca3-db67-325f-9563-b7b8f55fd60b | -3.3393 | -50.410599 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5dc4a3-5993-3102-8ba6-7c6ba3e11864 | -4.1487 | -44.352901 | 2026-10-09 00:28:00 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 749200c9-e299-32c8-a3be-8539ab03b5a6 | -3.0803 | -53.953201 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 087e43fb-fd0f-389a-bd15-245df6b38b72 | -5.0569 | -46.1866 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04dca4cc-d302-3ed7-99aa-2d4d4b901cc6 | -4.3246 | -41.237499 | 2026-10-09 00:28:00 | METOP-C | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d39938a7-cee4-3961-b24c-9f46e37f07f3 | -7.2116 | -55.134201 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README25.md)
