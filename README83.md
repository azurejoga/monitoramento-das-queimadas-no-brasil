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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5890d21-ed09-3d6a-81b0-2a70415e944c | -3.22236 | -54.30123 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f61475a2-65ea-3588-bae3-e96eb1df8efc | -3.1018 | -54.17848 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f79b35a-8f8e-3c70-a393-93c96b07a8ff | -2.99275 | -51.05433 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 01705c59-9e1f-3bb3-b706-b9266546f811 | -3.48963 | -54.61716 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4040e048-afe0-3a91-af2a-407d92bbfc4b | -4.96182 | -55.82431 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d464f7e-9e6b-318e-a373-6155e3a74373 | -3.02424 | -53.91013 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d99c9fb1-d510-3b43-a4af-95a36ef3378c | -3.23887 | -50.17432 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4852757-b95f-3d09-8d2a-724689d7e43d | -4.77015 | -50.81097 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14757449-4b10-3f06-8426-a5ad0a054f37 | -3.10234 | -54.17497 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e0b55dc-bdb1-397b-ae24-dc9b8f07f82c | -3.2783 | -54.02925 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6adbf217-c638-3f69-93f7-813f65cb88d8 | -4.36012 | -47.77987 | 2026-10-07 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| baf31aff-86df-3e5f-929d-afc8856e2af4 | -2.02816 | -54.32196 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fe75555-0e6a-33f5-95dd-1b5cbcefafde | -3.30093 | -54.03254 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2bce17f-148c-31bb-9761-251e6ed45e5d | -2.76949 | -54.08396 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19aa1015-e647-32e0-8451-8107fbda892c | -1.29375 | -54.5598 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| befc068e-4c54-3c72-9309-aff7725fd4b4 | -1.80104 | -57.10282 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b297390-f781-34f0-b8a5-c007e64a9b65 | -2.89281 | -54.07823 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abbfa7a5-c26f-313c-bd7d-7440aa17a404 | -3.09942 | -53.73537 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db70b82a-171c-3e65-92b7-ef63aa65cd1a | -3.28893 | -54.049 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 13a9b28f-9b63-384a-be7b-143738ca53ce | -3.73156 | -54.65787 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c036466-fcb2-3fca-9f01-c63d74f3285b | -3.10398 | -54.16441 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8d52d01-f41d-32c0-9177-2fee08fa7e8e | -2.37709 | -56.14062 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc3f602-01df-3609-83f5-0d8932cb87a2 | -2.1309 | -54.79974 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 78fff4e2-2a18-3093-8d5e-28a2f87bcb1f | -2.97991 | -54.13094 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e496ab2e-bb80-3d6c-a086-8673658f6054 | -3.01433 | -54.12909 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63de11fd-66dc-394a-b65a-920a9f332c5d | -3.4924 | -54.62114 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2df3a780-7654-3757-bcc4-3091fd266079 | -2.76895 | -54.08747 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3af11298-4915-3296-b3bb-807bba573d2c | -4.41454 | -55.75541 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c26dda5c-f6f7-33aa-9156-dfc6eb942fe1 | -1.32444 | -56.40572 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7f3a09f-cad8-3623-82a0-ae40b75f2144 | -1.4643 | -54.7761 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fb76102-a16a-3707-b1af-2d9541e71d99 | -3.05164 | -53.93253 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4aae3f8-424a-35f3-936e-07e1ff4e91ed | -4.15566 | -55.14841 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ec23a14-fdaf-3fd1-a317-f75d179aaa93 | -4.76149 | -55.66937 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 108cf6d4-253b-3629-ade5-48cb06cf9b95 | -2.99301 | -51.0566 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9acc1930-659e-3e3f-8b77-89fb112687db | -3.07614 | -54.14576 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd5ac74-68cf-3459-a0b1-b3b6187c617a | -3.58808 | -54.31112 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 511fd08c-e082-3087-a8b8-b2823fcea16f | -1.09046 | -54.11599 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70301c78-0852-3879-b243-c38cdd585879 | -6.46656 | -55.45032 | 2026-10-07 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db7e1fc1-375a-3e91-a5da-69221c1f737b | -2.4891 | -49.41423 | 2026-10-07 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c6226d4-09dd-31ad-9294-0b5673bdc183 | -1.52095 | -54.80232 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a23d2ac2-795e-3f94-b454-d9b0a619acdb | -3.28503 | -54.05202 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4ff6957-3e99-383d-8d98-b891dad9022c | -3.18092 | -50.56796 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 84f3c52b-8277-329e-8dc7-8ffc43d08967 | -3.94086 | -51.01593 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 11e3f01c-a01c-38d9-9e18-a4c7093745bc | -6.73044 | -45.80483 | 2026-10-07 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e225145c-3823-33ab-9da0-0594bf91b29b | -2.95676 | -54.17044 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d024e58b-d755-3d42-9196-f315b11c1469 | -6.0044 | -53.50515 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ff685dc-fa0f-3647-bfe3-d071234a3b37 | -3.08452 | -54.15779 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b0231c7-7637-3e25-9b3c-f9706b47e09a | -3.34977 | -45.10271 | 2026-10-07 05:04:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ecddee6-88d1-35b8-b249-2ae3346cfbf2 | -4.28045 | -55.1326 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bfd3e5b-f2b2-3331-a6f7-756d7319aaee | -3.5145 | -54.63165 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ff0cf9-f13c-372d-b681-0499da696937 | -3.55724 | -59.48673 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 473205b3-cf72-3a3b-839d-392a99760189 | -3.99445 | -56.26567 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| db8ff82a-7ba1-30e3-895e-aaa4b09b3591 | -2.88117 | -54.08723 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92afbffc-6242-33ca-9ad7-67dbab7d05e9 | -3.10731 | -53.77325 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83f307e8-3693-36ba-aa7f-eacd02170f3a | -3.50018 | -54.63652 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40d10584-be7c-3019-8884-fa722e6f58f7 | -1.29597 | -54.56715 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b850075-6924-3f1f-9ca9-b8e898e630f3 | -4.23963 | -49.97697 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e61e03c-11dd-3805-a647-2fe705891c9a | -2.7612 | -54.09344 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7580bdf4-faaa-3bb8-8f61-8999df4f48a4 | -2.37764 | -56.13711 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6509d4a3-de53-347a-b0d0-b422251943e5 | -3.80892 | -47.49519 | 2026-10-07 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9cc60bfe-bb1b-3af9-b887-d49473b8cee1 | -3.28174 | -54.07318 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd812f32-d141-335f-ab1e-6c6ebc382be2 | -3.24442 | -53.87125 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11a4143f-ca4d-36fd-9b32-7583b840ae4c | -2.77337 | -54.08096 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2f3373b6-6900-3e39-91fb-62c90ded44bf | -2.47062 | -58.0797 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 122f0a44-a631-363a-8b0a-f3c5872d91ed | -2.41171 | -51.3018 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65ac6a34-b806-3e11-a11c-adb0bd8d3cc9 | -3.27412 | -50.40562 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73d4c973-cdbf-3ce4-854d-f453833ab44d | -3.72896 | -57.14918 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0422c708-3ad5-3865-b6a6-a6dd503e4ea3 | -3.27216 | -54.0247 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7cbd285-6fa0-30ef-91fe-fff698128172 | -3.77838 | -58.52932 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e42ef0a2-cd9b-31ab-b68f-8a0967c6c09c | -3.31939 | -53.85355 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c734aaef-05ff-3ee5-a1b9-e4fb4fa4922b | -2.9241 | -54.14055 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00409873-cf0d-3c79-bd42-e696307d40c1 | -3.10336 | -53.75433 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c824db24-2944-3636-9cdb-6fb25084143e | -2.57464 | -56.16091 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ebd07b1-ba4a-3feb-a9f4-3cf30a6f1918 | -3.03909 | -54.25477 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd6622ec-f192-302a-9be5-39f6d6185eca | -2.95125 | -54.11956 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f64272d-9aff-33bd-9db9-569555ee0e4a | -5.82877 | -53.53452 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ee54404-8bdf-3684-9cac-50940400b536 | -2.32289 | -57.98411 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daafd57d-16b9-3a51-8663-fbfc43700eee | -3.01378 | -54.1326 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db4c0183-deb1-339e-b069-8cb19caac507 | -3.06461 | -54.17634 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ffcd284-2f95-3d44-bf80-653f49d31edd | -1.09762 | -54.11356 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79598cbc-85ad-3d7a-ac7b-550c1577afd1 | -2.88412 | -54.1344 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7dfd64-3d03-37bf-9f48-e1699827b54f | -3.10119 | -54.16036 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db41b02d-b8b1-3994-9458-8194f3c32ef0 | -3.28112 | -50.14075 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 63e949dd-98d3-3ef1-8c85-32bb2c65edb6 | -2.97325 | -54.12989 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7148c69-72b1-3fbd-b51b-2e631ad76ad6 | -4.51958 | -42.89187 | 2026-10-07 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f5b6c00-bf5c-3351-a9cd-ac54a8bfdc32 | -4.77148 | -50.80918 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e09ee24e-d587-3742-bf06-fa9457e891c1 | -3.52612 | -54.6441 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c483fc6a-56e9-3aee-9f73-52c2d187b527 | -3.12578 | -53.69897 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abe6cb09-862c-3254-86ed-340a86598d18 | -3.27999 | -50.42059 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b84eef01-0ea6-3e78-b541-c27ac52eaa66 | -2.90615 | -54.08028 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96efe6a5-a779-3c9a-aefb-ea71bf95e0d3 | -2.91666 | -55.64959 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8ec3a8f-9fe8-3850-8091-943ea59065e6 | -3.10036 | -53.1633 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe266b8-b255-31ff-8de6-1c8cb73e86c3 | -3.09435 | -53.72358 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c88764a-5046-3711-951b-a55f5d450c92 | -3.07378 | -54.24945 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51f7b6fa-7b0b-36ba-b0a5-dbd32a50cbc6 | -2.98346 | -54.04147 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24b9032b-a84c-30bc-9b42-aba63a3cbca9 | -3.07432 | -54.24595 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c8dd7f4-f2ec-320d-b641-3724693eebb0 | -2.75471 | -57.66444 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 503bcea1-c830-3c99-a302-4fcfb791d2c8 | -3.93605 | -52.18331 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25e4d8f5-f74a-3577-9281-91b06b6a79da | -3.11138 | -51.24549 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fd09a9d-df2d-3256-8068-0ece51f97e13 | -3.02759 | -53.91065 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README84.md)
