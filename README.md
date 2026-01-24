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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85bf5b2a-9620-33e1-90fe-3d8d11eb1321 | -17.7033 | -53.2904 | 2026-01-24 00:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e9261dcb-e0fb-3253-8bab-0e98ac8354c9 | -17.7235 | -53.266 | 2026-01-24 00:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8d23fb4a-6726-3fd1-893e-ee0d67ad5381 | -17.7037 | -53.269 | 2026-01-24 00:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 168.6 |
| bc474c74-930e-3f24-8f28-3adbf71bfda1 | -17.7041 | -53.2475 | 2026-01-24 00:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 285bda70-28ec-390e-9738-bcfda1592c7b | 0.7749 | -60.1826 | 2026-01-24 00:00:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 3d8062d3-f6c9-3491-81a1-62a8b6bc2d59 | 0.7749 | -60.1826 | 2026-01-24 00:10:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 792e5062-06ef-3c0e-a599-6411694f3249 | -9.8572 | -36.084 | 2026-01-24 00:10:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| 31f48616-19b3-3cf2-acc7-19524a611113 | 0.7749 | -60.1826 | 2026-01-24 00:20:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 42e359f2-fde8-379d-8e31-a2cfd1f1ee47 | -17.7235 | -53.266 | 2026-01-24 00:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b3c2f804-37cb-3bbb-9bf6-00e402e80825 | -9.8379 | -36.0874 | 2026-01-24 00:30:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 120.6 |
| d8b8379b-ab1f-3486-bfe5-8c1e03ecd29d | 0.7749 | -60.1826 | 2026-01-24 00:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4b0e4042-6cba-310e-9855-9f33c457bc37 | -17.7033 | -53.2904 | 2026-01-24 00:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c4b9f57b-1b60-3819-b187-1ef0937f42ee | -17.7037 | -53.269 | 2026-01-24 00:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| f3044181-2887-3576-8f2a-068766dbfc91 | -17.7037 | -53.269 | 2026-01-24 00:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 5fbacede-add4-349c-b385-ca15de90ef13 | -17.7033 | -53.2904 | 2026-01-24 00:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c8660647-94b6-3a64-a88a-0f168d12673f | -21.1529 | -48.6612 | 2026-01-24 00:40:00 | GOES-19 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.9 |
| 20ce2f1b-a1eb-3845-94e5-0db6a2e7d5f6 | -17.7235 | -53.266 | 2026-01-24 00:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 58998d0a-ba2f-3ad2-aa14-177317e24fc0 | 0.5562 | -59.841 | 2026-01-24 00:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 6eee0d7e-5e94-3412-8bdf-8ae24f079538 | -17.7033 | -53.2904 | 2026-01-24 00:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 395047cf-d0b1-3c9c-9e51-ae94e1841b92 | 0.5562 | -59.841 | 2026-01-24 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 201ed978-5ae6-3599-9cc1-6b6ddfab0269 | -17.7037 | -53.269 | 2026-01-24 00:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 151.5 |
| a9cb927e-ec94-39e2-945e-870c8adc8736 | -17.7235 | -53.266 | 2026-01-24 00:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7a80c730-a240-3422-85fc-e648960d60df | -17.7037 | -53.269 | 2026-01-24 01:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 4e75d05d-3439-3125-bc9c-dc8e059f55b3 | -17.7235 | -53.266 | 2026-01-24 01:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| dce501a2-f9ff-35b4-a433-1894c666cd62 | -17.7033 | -53.2904 | 2026-01-24 01:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1ed21fd7-b4d4-373f-beb4-ea635373f46b | 0.5562 | -59.841 | 2026-01-24 01:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 77ca952f-866d-3f21-b62b-c5e687ab1148 | -30.06101 | -50.75008 | 2026-01-24 01:02:00 | TERRA_M-M | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 9.0 |
| 43ceb8b5-38a2-3cf8-9351-7b534a526ca4 | -22.1965 | -56.12611 | 2026-01-24 01:04:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 25de0063-ced7-3eb7-ae6c-c3ad8c58f1b3 | -19.55862 | -54.44296 | 2026-01-24 01:04:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 570059f7-dab9-3a1b-9364-2d4334fe57a2 | -19.29518 | -53.17585 | 2026-01-24 01:04:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 5d4b4fa7-ef95-3005-8239-e544d5d7c452 | -19.29879 | -53.18444 | 2026-01-24 01:04:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f403819b-efec-330c-ad25-4b556c2644e6 | -20.32092 | -57.85069 | 2026-01-24 01:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.8 |
| c15d09f6-09c9-32ba-9b4c-e61e154fd9e5 | -19.68362 | -56.86421 | 2026-01-24 01:04:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 424a0a54-fdf9-3e19-b5a1-4c2230d5aef7 | -19.34146 | -54.17309 | 2026-01-24 01:04:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 91fb40fe-5071-3059-a5a3-2a95105f99f5 | -22.0245 | -56.33751 | 2026-01-24 01:04:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 98f69371-5f0e-3848-aaa1-f91c78ab4fca | -20.37775 | -57.8704 | 2026-01-24 01:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| a5853aed-e52f-3499-b238-1de234895cf9 | -20.38888 | -57.87239 | 2026-01-24 01:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 92c30d14-bacb-3e1d-bec7-dd8ec25bee99 | -20.33857 | -57.84789 | 2026-01-24 01:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 5af9253b-c9be-3ff0-9aec-0477364dba62 | -19.67332 | -56.85612 | 2026-01-24 01:04:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 604813fc-56b5-351a-b4b9-43fa89280adc | -20.32975 | -57.84929 | 2026-01-24 01:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 1777cbd0-8f02-3398-bc47-abb37838a9a2 | -19.67631 | -57.19555 | 2026-01-24 01:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| f3928447-0390-32b3-9c46-9d3850430af8 | -19.2963 | -53.16981 | 2026-01-24 01:04:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 08bc01c1-fe41-3f1b-b2d4-2cb8110e11d1 | -19.68225 | -56.85464 | 2026-01-24 01:04:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 08825cf4-3697-367d-8123-96994c32a50e | -19.67469 | -56.86568 | 2026-01-24 01:04:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 65fdf08b-4af9-39a4-b706-d125cd908fe9 | -17.6968 | -53.28384 | 2026-01-24 01:06:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 47fa82a2-903a-335c-b0de-5bf97ea3f29d | -16.44835 | -58.16992 | 2026-01-24 01:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 560a087a-cc98-35c5-9191-bf22045e8d0d | -18.25129 | -51.27985 | 2026-01-24 01:06:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 69efe42e-b80c-3ba3-b2c5-2f95a0900273 | -16.44706 | -58.16073 | 2026-01-24 01:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| d2688cb7-0d00-3e36-bad3-fbb10dd507f5 | -17.69426 | -53.26856 | 2026-01-24 01:06:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 92e5193f-d067-332c-85ca-a8248b422d83 | -17.71919 | -53.27983 | 2026-01-24 01:06:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bfce82bb-371c-35aa-91ef-f53ad3eb44a9 | -17.70547 | -53.26656 | 2026-01-24 01:06:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 34b5e102-fd12-34ea-96c4-73ad660952fc | -18.24919 | -51.27459 | 2026-01-24 01:06:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 5e74833e-1c9f-330b-bd20-6b4afedf0c35 | -17.70802 | -53.28202 | 2026-01-24 01:06:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 9239a862-9a87-37c9-a8df-f165cb62fb3b | -16.3103 | -56.56283 | 2026-01-24 01:06:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 0b4686e9-4be5-39af-b6ae-37010ec0ca8b | -17.7037 | -53.269 | 2026-01-24 01:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| da57bee0-c16c-3d9e-9dc9-e2aa112ae00f | 3.50568 | -60.91688 | 2026-01-24 01:11:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 186bb406-9689-34b2-9e8d-89217d5a1be2 | 0.78469 | -60.18678 | 2026-01-24 01:11:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2f541440-60e6-3b37-a553-f621eedd0215 | 3.98847 | -60.82496 | 2026-01-24 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 474d4fd1-4b67-366c-bd0b-e680cbed6a73 | 1.32345 | -60.42781 | 2026-01-24 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d5682413-328f-3e7f-86e2-9e9820b84b14 | 1.35465 | -60.05945 | 2026-01-24 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc57a6d2-49f5-3141-95d8-3828e6e759d0 | 0.55536 | -59.84108 | 2026-01-24 01:11:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 675f0861-f10a-340c-ab10-d3ebe9da5691 | 2.43271 | -61.14396 | 2026-01-24 01:11:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 916561e8-f7dd-39e0-b257-8275de905d5b | 1.92844 | -61.19368 | 2026-01-24 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 50b8ab04-9435-3b15-9ec1-cd5225724697 | 1.32477 | -60.41812 | 2026-01-24 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.9 |
| e625235a-8f78-339c-a924-d1d812a6fdf0 | 1.3261 | -60.40844 | 2026-01-24 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7b171800-fd7e-30d0-8eab-7f599609c249 | 1.92719 | -61.20284 | 2026-01-24 01:11:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26a1424d-68d8-3a55-b053-ebc70240d9e7 | 0.7754 | -60.1855 | 2026-01-24 01:11:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 27d7b98c-7c0e-35ce-a3ed-00ab6f28324c | 0.55398 | -59.85122 | 2026-01-24 01:11:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 29046b86-9c92-3418-a5b9-935426cc5607 | 0.5562 | -59.841 | 2026-01-24 01:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 769f2f6a-d4d7-3277-b092-6c5c4681d701 | -17.7033 | -53.2904 | 2026-01-24 01:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 01dd0d0f-3632-3d2e-9df6-c657249ca778 | -17.7037 | -53.269 | 2026-01-24 01:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| c2ebe95e-8357-3ad4-9ceb-3faeca66adb8 | -17.7235 | -53.266 | 2026-01-24 01:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 95d93267-fdff-3db7-af14-29bcfd3c14e5 | -17.7235 | -53.266 | 2026-01-24 01:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 19ed3abd-c969-33b0-a385-92b1fcf9c7c9 | -17.7033 | -53.2904 | 2026-01-24 01:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ed38c15c-33be-3389-99be-da9614e6b500 | -17.7037 | -53.269 | 2026-01-24 01:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 8df80fef-52c4-3ca5-874e-7e0c95cb3b8f | -17.7037 | -53.269 | 2026-01-24 01:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| efb2ef17-357e-308b-8077-584ec06519b3 | 3.9865 | -60.8242 | 2026-01-24 02:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4610635a-bc6b-399a-9568-11f1a2d23554 | -17.7037 | -53.269 | 2026-01-24 02:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| b11852fe-e2ae-3337-be95-db8e570a17d5 | -17.7235 | -53.266 | 2026-01-24 02:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2f5aaabd-1da6-3ba7-bcf5-5d260514073e | -17.7033 | -53.2904 | 2026-01-24 02:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d83eaf88-a3ae-3986-aa73-09cfa5c7095a | -17.7037 | -53.269 | 2026-01-24 02:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 182ebc1b-08e0-3b69-81f4-abbee3d2c874 | 4.2454 | -59.9812 | 2026-01-24 02:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 4769afaf-85bd-3cd3-8cc1-182b16ed4fe5 | -17.7037 | -53.269 | 2026-01-24 02:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 13a43b95-da84-3173-a4af-531d32d7f616 | 4.2454 | -59.9812 | 2026-01-24 03:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 56f34558-aba2-3b1f-9547-e4fd41a6d17d | 4.2455 | -59.9621 | 2026-01-24 03:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 3577df69-3422-3ffa-ab49-37d10b1d80f0 | 4.2271 | -59.9817 | 2026-01-24 03:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 45ebd017-308c-3981-a9e3-e37722df2f8e | 4.2271 | -59.9817 | 2026-01-24 03:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bb11099c-32a2-3e5c-9432-705ae9e79803 | 4.2454 | -59.9812 | 2026-01-24 03:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 435d997b-680a-3248-979b-98020b3e5577 | -7.86784 | -39.09358 | 2026-01-24 03:23:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ed1aafe9-bf1c-3794-ae2e-8f4204dcabfc | -8.05436 | -36.1525 | 2026-01-24 03:23:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b24d923-c66c-34ab-8ae7-24c73bca2bbd | -8.38541 | -37.2056 | 2026-01-24 03:23:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 98f49c25-fee8-3a9f-a527-fd1d838a30b4 | -7.70648 | -35.00669 | 2026-01-24 03:23:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25f6898f-1790-34fe-887c-18bd070ec4a2 | -7.27129 | -43.08266 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c7831480-f6a6-3e1a-a303-aea3987d7b73 | -6.31331 | -35.23104 | 2026-01-24 03:23:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 6f1a940f-35eb-3377-9a46-1544502d750e | -6.08742 | -37.3154 | 2026-01-24 03:23:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e8739ba5-f212-3641-86e0-fce844363f32 | -5.84352 | -35.64397 | 2026-01-24 03:23:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| caf888c3-99ff-3de2-96dd-f299397bc29f | -7.25734 | -43.08564 | 2026-01-24 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ec09eb72-a5f2-3906-a7a9-8fa3eeae5087 | -7.50165 | -38.91663 | 2026-01-24 03:23:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0caadac8-f3ff-3568-b687-113e55ab1081 | -7.62224 | -35.09215 | 2026-01-24 03:23:00 | NOAA-21 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c1c52207-9bd8-3819-b628-2e4eaf0a99a7 | -7.97464 | -36.37582 | 2026-01-24 03:23:00 | NOAA-21 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
