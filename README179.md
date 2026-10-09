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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf84b90c-de01-3fce-adb7-bf5904287ab5 | -1.15118 | -54.21976 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16a6e519-d4cb-3a37-ab7b-50bf7a5de2b9 | -2.56606 | -56.16867 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fde9b22b-25ab-32c9-a1e4-f247f6cefd4d | -3.29309 | -51.57117 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f1777bd-b992-332d-becd-ee67a9591e36 | -11.26089 | -46.27254 | 2026-10-09 05:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eeb7b9ec-33ad-3434-bc09-ba2e49746b23 | -3.03375 | -54.2344 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e56ae832-489b-3bb8-a08b-8b9594ac3ea1 | -3.58268 | -54.31547 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcf1a7a7-9d3e-3934-b8fe-0de78c46e53d | -3.42801 | -54.06758 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a52fdf83-8b43-3ab2-8b8b-121c0c78e6be | -9.69287 | -58.09566 | 2026-10-09 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed736f0c-9791-33d4-a86e-3a386b1b8d1d | -1.69535 | -54.98338 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2079045-75ed-3041-bf58-3b5872762734 | -2.72576 | -58.05832 | 2026-10-09 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beefeb3b-4fe8-365b-9d26-51d25a9d6975 | -8.54417 | -46.90998 | 2026-10-09 05:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8287f7f8-b3a2-3bbb-8a63-68b8ba322397 | -2.57805 | -56.18201 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66f0d6a9-a5b5-3ed0-80aa-59875e98068c | -4.38717 | -55.44873 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e34f9e2f-9ba0-3dc5-b317-a90b410b7d55 | -9.25525 | -60.87984 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31e94c6a-c9d3-3ccf-a9b9-44e9b5a0cbcd | -6.63015 | -59.93869 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96378701-d271-386f-84a2-f60392319028 | -2.47655 | -56.07065 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5519868a-3911-39a5-941f-bc54499707d4 | -3.18348 | -60.39493 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91aef22c-07f5-3848-a214-33c830a601f7 | -3.25418 | -54.02895 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddc6ff0d-8ec2-3625-80b1-c4ab0f794693 | -3.38471 | -50.21847 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30d9f4fc-2c44-323a-9c8f-703c7c4944f7 | -3.16315 | -57.84758 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4ac5ca1-2866-3571-9012-d87ee836001a | -4.57178 | -54.95535 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d77f751f-075c-3f24-b643-89f0965a4b61 | 1.69968 | -55.60624 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ed502c2-9f75-3cbb-b441-6c614ee8892f | -3.22654 | -53.89291 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d02ee1a7-c3d5-3480-a413-6adf598b13d8 | -3.57582 | -54.66395 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 472e2b60-fd7d-3b2b-b216-3663c5e8ed00 | -11.39034 | -46.67358 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3292f172-bb4d-3627-bbc7-3fac70a3e989 | 0.50218 | -50.77712 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4679e1cb-85d9-3c11-b904-9ab16cac5ffd | -3.01897 | -54.04809 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd5f84f4-2386-3ce5-b46e-3dc6bf905c30 | -3.00117 | -54.76492 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9753fb4-c5c0-3ab1-be53-513477c38736 | -1.23713 | -54.2067 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c97c89b-1b5f-3ae6-bd9c-ad0da716cd1c | -3.4018 | -60.84678 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b686478b-2c3e-3b21-b4d7-670a1178d408 | -2.12519 | -56.69765 | 2026-10-09 05:23:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c517c681-a03a-3374-9ead-8b064d146c8b | -3.70196 | -60.55191 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d80e5f5-1c0e-3171-8a0b-097e5784753e | -3.00766 | -54.07084 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c4be043-95f9-322c-903c-6b3c7c2ea278 | -3.02089 | -54.08753 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12dca684-e8ec-3e6b-866d-f7b7cbe6525f | -3.74361 | -58.40885 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2110e9ef-ebed-3003-933e-95ef8586456b | -3.17036 | -57.49987 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b91fb13-d241-3095-9fc2-e464a16e1617 | -3.61399 | -55.46664 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f500759e-c25b-35ba-bc12-f02b53446723 | -2.7399 | -54.13398 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2c043ed-8e0c-38ea-a8b3-e98e95345245 | -3.00247 | -53.91488 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 820edee4-0037-31f3-bd31-9c1d13087562 | -7.08926 | -59.76565 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 002ff63d-d73c-3873-8060-584578427b94 | -2.54595 | -57.38857 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41d76954-5dfe-378a-bba6-c907f23dbbae | -1.36224 | -55.47031 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54d3895e-1f49-3aa4-ac89-d90f81e9f438 | -2.73971 | -54.1099 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd4076b2-6dda-3467-b269-e0abef9a19e1 | -3.00459 | -54.05352 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91a4a89e-320b-32bb-b4e0-ec29c8044dc7 | -4.51993 | -54.86125 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1528bca7-56cd-3d44-a047-38cbc659aa46 | -2.46952 | -56.09274 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b091d533-dc77-3b0b-bdda-f149bedee864 | -3.08231 | -53.94413 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37a4db6b-7a2e-30f5-82c2-f5b6bfba4295 | -6.94297 | -59.10353 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12fd5992-cbb6-3c57-995c-19c4a7ffdebb | -8.84344 | -61.46795 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4762c724-9fee-3088-be43-d36853634d95 | -3.06121 | -53.92609 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9a9dd77-47d8-3db7-8b20-40a09c848845 | -3.63862 | -59.56381 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b959c77-b270-32a0-8257-19e6ac5a5d01 | -3.52948 | -54.65983 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fda60e4-20d2-341e-b733-970737e32f97 | -3.60569 | -61.62395 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8b6a245-9c89-3e62-ba8a-33d540878198 | -4.9373 | -49.21988 | 2026-10-09 05:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 223e1e1f-7588-3632-8e06-8b540e56ddd2 | -2.5695 | -56.16922 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dcaceef-01c2-3020-849e-3ae237ed8a75 | -3.31925 | -54.04393 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbab7d80-28d6-3c0c-943a-d28fa54434bf | -3.70595 | -57.18604 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cceec7e6-3316-3619-af18-b6c7837f3808 | -3.00235 | -54.06782 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b48174e-4dcf-3939-8c0a-d5870a93fca7 | -3.9143 | -58.89853 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1981e091-bfb6-35dd-bcf1-06839126c994 | -2.74906 | -56.61136 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5afe5062-95fe-33a5-a882-2ec368c612e7 | -2.57985 | -56.18975 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0534450-a621-3357-aa2e-a677eeb06f97 | -2.4137 | -56.5378 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8830995d-607c-359f-a7ab-903057b9e3d0 | -1.11077 | -54.17405 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae43ab49-55ed-3817-9835-d218270e7218 | -7.57092 | -61.5481 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17e42165-6e00-3160-93d6-f8d601832324 | -2.99725 | -57.7584 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd21cafc-3645-3bc8-a020-6d4869b63e5e | -3.5983 | -54.66733 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64ee40a3-dcf3-3724-a67b-1cbfd1868f76 | -3.07395 | -53.97272 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17c400bb-943d-344c-b400-25ffb2eced8e | -3.10984 | -54.19772 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f0104b4-50ef-3ea4-a5c6-31ce6a28f666 | -3.05779 | -59.09217 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d0283fc-30ea-3999-ba04-66de5166dc6b | -3.75078 | -59.49864 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a428b63-9222-3014-ab41-b89e10454535 | -3.51611 | -59.22152 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92c3f6f7-a39f-36b3-be9b-064dbc221bcf | -2.99783 | -53.91913 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 21780278-ab46-3850-9e5b-494b5f23b317 | -3.00565 | -54.2396 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c179ffa-00c7-3823-9c36-83d3fb67aaa0 | -6.91946 | -59.27354 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c32576fa-adfb-348a-b750-07963d7115b6 | -1.11007 | -54.17849 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9eeb8eb6-a4de-30d9-b491-8a68422ef76a | -4.20253 | -55.63337 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4be7599-5662-3da4-bf60-ae7ff7a542f2 | -1.47167 | -54.75701 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 674841e2-0643-3fb9-b5d6-5c2903e0d990 | -3.00495 | -54.24426 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81615cd7-2bfd-3dc0-984b-8fc6a2e1c299 | -2.39568 | -51.30722 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15b6838d-a595-3dfa-b0e1-4f97fc2a9803 | -3.30439 | -54.01185 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66fff24c-1ee3-3350-8156-1b4a1e532c6c | -9.25744 | -60.88752 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c492a686-9b61-32e1-afd2-0d5b241fd680 | -1.48472 | -55.86766 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d67df525-158f-38ca-b953-a624d9c0a358 | -8.24555 | -54.72949 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6dd218f-7dc8-32be-ab3e-dc6edb928319 | -3.90321 | -52.15975 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 617e4599-cefc-3ef6-9ebb-f25c0bafe3fa | -3.09844 | -59.19838 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4403eecf-b9b1-342e-8f44-6800fe4771c6 | -2.1128 | -58.13043 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a5b5a76-dbed-38f7-9053-a8a45da8c2c8 | -2.89043 | -54.16413 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d00aa29f-da63-3906-9cd1-444b7e1adaca | -3.16923 | -58.62482 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a4da6598-518a-3962-b854-12d6719e3f4a | -4.10755 | -54.62585 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2174544b-7437-34bc-b02c-d4a2a6acb038 | -4.63499 | -50.96552 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b989a2ae-881e-3abd-ae6c-41e6f8596cab | -3.00434 | -54.11902 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6544b0e-5905-30ee-ad90-0fca7b7176b1 | -2.57367 | -56.14293 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 535939e9-1a6c-3376-a5e6-8eb564ed5e74 | -3.96583 | -60.00098 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2099b47-0041-35a4-881a-9f4e8c2f2d6e | -3.43554 | -54.54074 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d499f7c-a6f5-3edc-a52a-b19bb5aaad27 | -2.49263 | -56.16496 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee51e8e0-f238-3f03-8ceb-0734722091d7 | -3.8676 | -55.83675 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d932f34-763f-3596-bf3f-19ffdb54bc6c | -2.94229 | -54.15079 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a87b1fe1-f334-3c88-8b69-c7b518a0ca29 | -2.63618 | -57.46305 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 104b882d-7624-34f8-b6ad-d95cc5c54950 | -4.10057 | -54.02528 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1632aa27-08da-320e-873f-370e168c3971 | -3.59915 | -61.61866 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README180.md)
