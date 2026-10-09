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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdf248b4-53c0-3e90-90c3-b98486ff8e58 | -4.34306 | -55.13048 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59adde0d-4b45-314e-97da-7c221bb0ba17 | -3.02084 | -54.07554 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 927e71eb-d32a-3852-81e8-36918246abaf | -3.36139 | -54.74973 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ee56fd9-d9a8-3cdc-b0f8-038eafabee1b | -3.30997 | -53.71334 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d393b2d7-11a0-3d1d-9222-c979c2088441 | -3.50388 | -59.27668 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fb838d4-d498-339e-b44c-bcbddf565ffb | -3.43317 | -60.21415 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 582e55f6-276a-394a-bda5-f8b848d8a9ab | -3.02283 | -54.04867 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7ea2a7f-5ff1-3112-afb0-b3ce400384ca | -3.09171 | -53.96047 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1515d71-ad14-3340-9a96-868cef7c523f | -9.8919 | -58.12205 | 2026-10-09 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17c14d6c-5641-3262-a1f2-ba69566f16c6 | -2.92748 | -54.11957 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f5871d5-3381-3ec4-b9ee-7bbfc46597a4 | -2.50652 | -56.12096 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26284706-691c-36d7-9c5e-63c8eb89c0dc | -9.29993 | -47.46603 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 849c14ee-49fa-3210-8b10-7d31cce52efd | -2.48919 | -56.16443 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b36bc5bf-75cb-34b4-b8a0-47388e456a6f | -3.35041 | -50.41171 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 460e97cd-314b-3b26-a91a-ad5d26ce6feb | -3.22606 | -54.29155 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0e847d44-d28e-3e42-ae5b-7b67497b989e | -5.09744 | -46.22263 | 2026-10-09 05:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78e244f1-5e13-33d5-9629-5745194bf2db | -2.43254 | -55.99029 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9765c61e-8404-31ef-b8a8-28718f108f2c | -3.01399 | -54.09396 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7d15e00-fbd7-3aa1-970f-45c5d75d4bd2 | -2.96145 | -54.15357 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5176af7e-4344-3ffc-b766-5baf24ca1c7b | -2.68513 | -59.78549 | 2026-10-09 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 038301cc-0747-3ed7-8976-6439563e8ab9 | -3.40554 | -58.91321 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba68708-78f4-384f-baba-88e722b5e5d8 | -2.21909 | -55.45539 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24632e9c-4d00-3940-acdb-02fdf7ac0531 | -2.58394 | -56.14049 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc2280d-f660-3100-8195-0e08fe4ce25a | -10.7359 | -52.03189 | 2026-10-09 05:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 927c69c2-e4a9-341a-96c6-2485f4afceb1 | -3.49755 | -54.61801 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53f90d39-98d7-3770-88c7-e569b72cb07c | -3.73363 | -59.41339 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a64f1853-57a0-333a-b39d-48be77e462b9 | -3.20554 | -58.84594 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33d7cfe5-67e2-3f39-a134-16e732b7ffa8 | -3.03599 | -54.14324 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e04732d2-1f55-34f0-8fa6-676f9c6154b1 | -4.35323 | -55.23148 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42011b49-0426-3821-a951-b9f027268ea0 | -3.57039 | -59.43756 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c0a52e-d670-3f06-baeb-4fb01fb07838 | -2.99231 | -53.9034 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3c39fcf-f55e-388a-9d25-0d6741a95b2d | -3.03796 | -54.10468 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1979e960-0648-3b7c-8356-1a4ed220437a | -2.41426 | -56.53416 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6600992a-f270-30a7-ade9-03cb55866d60 | -3.92943 | -54.57697 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e04af3a-9c88-3ba2-809c-2f840875c34e | -3.57391 | -54.69405 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ec35b150-49ee-3391-a943-1b6c7c7212e8 | -3.24967 | -50.40804 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf385b82-b9dc-3701-bc88-afcece8f8a08 | -3.47563 | -59.58108 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1402bea-5f21-3d28-95ef-e9eb87de6a8b | 1.75157 | -55.56083 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 946b7826-f350-3303-9651-017bcc483db9 | -3.09179 | -59.19732 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5db6e4f5-b7dd-3749-8e43-2c9a4e038e2d | -1.1033 | -54.17297 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca556f16-967b-3a4d-8a17-4e1172a52222 | -4.15801 | -55.13874 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 827a0fef-068c-39ce-b1b2-5caf5de33d6b | -3.0221 | -54.05346 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 921cabc6-61a9-3a22-8d0e-a1bcf6f949e4 | -3.99944 | -56.2497 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab875168-fca4-3b2a-aef1-e84b516af7f8 | -7.22158 | -55.07893 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 45758bdb-4b4c-3deb-bc56-9ad84b1460a7 | -3.17992 | -58.64421 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 161e088b-3f5f-3e45-9756-f9854f09864b | -3.93072 | -56.03833 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0a0ce358-f433-34b1-80b3-bf5227a843c7 | -7.43942 | -63.55815 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d1e59ed4-e8d9-3d85-a944-df91db1274b2 | -2.03978 | -55.58565 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fc702ef-e7be-3c4d-9a53-9e04ff342001 | -3.0173 | -54.11126 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8d40bee-3bcf-33b8-b6b4-30189949ea88 | -8.25468 | -62.93904 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b961f33-b417-3629-b626-98c5f5528140 | -2.50749 | -56.18259 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b92234dd-b3b6-3306-a673-8fe745cc7ebe | -4.4281 | -55.15926 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b2399bf-20b6-30b7-b5e2-feb5bf8b9517 | -4.57394 | -55.9947 | 2026-10-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6a244e2-c576-36bc-8e53-7e3b45ddb880 | -3.02008 | -54.0803 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d43eba3f-a410-3b25-a837-021e3e98040c | -3.40527 | -59.59899 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 944325bb-0aa7-34c9-9a78-6618219d51dd | -4.63656 | -50.95496 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf93db56-0952-3e29-b4fe-2e7ace21c3df | -2.84658 | -54.11893 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d15172e-35fb-31a9-a3e4-d5747b54a7ac | -3.71331 | -59.64777 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d980d18-19e0-3c5f-b9fd-c60b8f2dfe24 | -2.49997 | -58.06829 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb201cdd-2901-3b4b-927f-6cc95ff9187a | -3.54346 | -55.5277 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdfb4126-393d-3c66-b696-b3379763f41e | -3.30125 | -54.00647 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5b0630ed-1874-35dd-bff6-c8ac42e1d0d4 | -0.99626 | -47.65709 | 2026-10-09 05:23:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9cb7db5-53f1-302d-8447-be4d2bdb85a4 | -3.19373 | -50.56659 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a957e17-9c4d-3718-bd00-fd5c47da9bcb | -3.60313 | -54.58498 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2ce686c-e1c8-3df9-8611-98862c2e433d | -3.43905 | -57.9729 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62edb5de-cbcc-3189-8263-57ebf0378ab2 | -3.10246 | -53.94234 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f5aea00a-5e14-3e75-9ca2-54a3712caf52 | -3.98742 | -59.35667 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9f033938-f6d9-3a4c-9120-f77d71cadb03 | -3.16869 | -58.62827 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5bf015bd-36f7-3cdc-8983-52f35e8476c3 | -2.88128 | -60.13575 | 2026-10-09 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 341a09fe-e638-3068-bdc5-9b845e77184d | -3.59218 | -61.63877 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 842ac8d8-ed20-3a93-a6bd-90f9281f3477 | -8.49739 | -54.62294 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b0681c1-7ad5-32b2-9f07-a5c6341d48e3 | -2.33543 | -48.86568 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 346805c9-78be-3e98-b5c3-5cad66f03c10 | -3.56483 | -59.47261 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73e5ca24-8079-3772-9397-c68d70f86a2a | -3.0172 | -57.78279 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cc03856-fd2a-34d1-9116-4a64aabe8db7 | -3.18766 | -58.65954 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f69739c-9e14-3572-b0ee-a2b60adf3f7e | -3.27483 | -53.99748 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c0764ed-c0ff-3e59-8b01-6b5a2eedb07e | -2.908 | -57.20416 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12ae57f5-c9fd-3ed0-8aed-d11925988f78 | -2.584 | -56.14454 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| decfd0f5-1577-3d5b-ad1b-ca25908780c8 | -1.32034 | -55.44017 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46e9c9ef-ff7b-3cb3-b19b-2095c433bf89 | -3.56756 | -54.48866 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80436116-67b5-374a-92ca-624dd4d94ab8 | -3.30915 | -54.03244 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27f64fdf-238b-3c7e-b818-080e4b9977e0 | -3.63489 | -60.61798 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 208d9afc-906a-3595-b997-40093b67c112 | -3.50553 | -59.28765 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6740eb5c-3263-37bf-8d32-05154cd4c2bb | -9.96226 | -59.21075 | 2026-10-09 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bd623b8-3508-3760-88da-e7037adc8174 | -8.84125 | -61.45998 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92394ec8-b182-339a-b78d-a302a0e1f219 | -2.99999 | -54.0577 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28413aea-6418-3717-8f75-7d5af462d181 | -3.1785 | -58.84523 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e3f531-6f90-3fe6-9524-559e765e4583 | -3.73752 | -59.41043 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82bd0335-ff68-346a-a290-0c2a097fa104 | -4.2943 | -48.60513 | 2026-10-09 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd4d122b-3f31-34e4-9709-38ff9df8ad98 | -3.53373 | -59.41022 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 472b6ec6-61f0-38fa-8ff4-2fbbaf13efc4 | -3.98963 | -59.21454 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee6d08df-96c8-3303-aee1-b3851d2272c6 | -2.4328 | -58.01925 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b0d83e-fc70-301e-bcbe-cee7320eb258 | -3.24984 | -54.67105 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38d025ab-48e0-3655-aba4-3c6cd0b93e98 | -3.01849 | -54.0774 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2ecedff-e435-3ac3-80e5-8bc58de75998 | -3.25443 | -50.40095 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fb40359-4f19-3820-bdc9-82aa2ceb2e12 | 1.69464 | -55.61819 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 39ca2189-f060-31ee-b3ca-3409bc048131 | -2.48392 | -56.09108 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7edfef3a-7304-394d-97ff-87b33db184a6 | -2.50273 | -58.07224 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef5d18bc-6263-301f-bce0-f3e586c97e5d | -1.72709 | -56.06554 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74f1183a-a9c8-3c18-83f0-c2b33f7ac578 | -3.22155 | -54.2956 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README189.md)
