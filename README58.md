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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8011284-6714-37ac-b68a-068caa0e4e03 | -3.10216 | -53.17097 | 2026-09-21 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8928cb46-862f-364e-ac54-5798b87b8142 | -2.90098 | -59.22356 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 450455bb-487f-3dc2-b936-1090e9df660a | -6.10109 | -57.6885 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b77be405-d253-3e50-9c46-96b44af1f175 | -6.65989 | -50.88951 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab55b60b-55e0-3a24-a659-1625784a16b2 | -3.40663 | -61.30244 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed10122-9f20-3b99-9675-0c250bcafb85 | -6.55557 | -45.57478 | 2026-09-21 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75d8336d-6869-3b03-ace9-fa3e4bc666e8 | -7.18694 | -47.45631 | 2026-09-21 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9722bd84-d86e-3e66-ae37-4706a65ebedc | -3.38637 | -50.44247 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 91bc8e75-73fa-38ae-a49a-b2a7689f69bc | -4.79647 | -48.23362 | 2026-09-21 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9054d6fb-3561-3240-8d96-340305d3311d | -6.73368 | -55.08839 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e00b1a3e-560e-389b-ba49-a3ebcb6827f1 | -8.30834 | -46.86636 | 2026-09-21 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2df25cc-b100-33f9-af7c-2995fa0c03e9 | -1.91111 | -58.26125 | 2026-09-21 05:04:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eaa3b85-9f88-329e-9912-9e23648c1996 | -6.10192 | -55.56705 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acee97bb-e5ea-33cc-812a-87dde7e873d8 | -7.43013 | -44.77279 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 266011dc-56d8-36fa-bf45-52983ad238ad | -5.77236 | -57.59188 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 076213a0-7fab-33ff-923e-7b668b58d0fa | -5.2048 | -56.10367 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a0f81de-ba0c-395d-bb91-ae3484f14bc6 | -5.82976 | -53.52343 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d90c7829-f9bc-39a3-937a-294d2eb168b1 | -7.48768 | -45.47443 | 2026-09-21 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab711a4-64c5-32c6-924f-dd01af99c1c2 | -3.45439 | -50.60626 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c47f46e0-cabb-33b5-a885-3f6fab3bb024 | -6.56475 | -45.55275 | 2026-09-21 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70678103-78eb-3457-8396-f0de7da489c6 | 1.07836 | -60.6762 | 2026-09-21 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea1d7e78-ddc1-351a-8f05-7f9f702a452b | -3.89906 | -60.59163 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24cb198c-d215-3df6-becf-b983c1d626ee | -7.41655 | -44.78051 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 719d9ada-3344-36ed-92f7-723638823e83 | -6.73925 | -55.09642 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f34026d-d6e1-3577-bfc6-b40125771268 | -5.87945 | -53.63219 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dbc32a7-8d96-3f64-85e0-7f5d6310d3fc | -5.42398 | -60.22009 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72a7d40f-5f0b-3984-9b1d-e2dba34263fe | -5.88174 | -53.6403 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faa86f08-a856-3463-a156-49c6d74d46ca | -7.41228 | -44.77172 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f28d481c-3ef1-36b5-a35c-2de136a8f026 | -3.69441 | -60.56576 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1354a01-6de0-3308-9edc-31ec9746fdb7 | -6.14345 | -57.72917 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 911279bb-a173-378f-86a4-448d64bdf0dd | -5.22988 | -49.32193 | 2026-09-21 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b16419d-1fca-31e8-98a6-1d31333ad94b | -3.01161 | -54.17901 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59026d7c-52a3-300d-9bd3-b53a3c8c2f86 | -6.09375 | -56.46782 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fb7ebbf-bb79-3772-bb3b-a8f5157a42ac | -5.21472 | -56.10521 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12ecaf2c-0662-3c34-936e-41ffd72cf3c0 | -7.41096 | -44.78149 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 245a1e94-4e41-3c9c-9bee-f8036d09f2f6 | -6.44064 | -55.64133 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 454a6011-7e71-36ca-8d02-b7e14ae03d52 | -6.09194 | -57.70213 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d369458d-bcfe-3b64-9746-8ea85558bf17 | -3.39191 | -59.52555 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5596c333-16b2-3640-baca-7dcaf9acb271 | -3.07236 | -61.27657 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 84148d77-3b87-3f42-b8b1-32832b24936c | -3.33751 | -57.88279 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e5786fa-355e-3f50-891f-a75133ce7358 | -7.73883 | -49.38923 | 2026-09-21 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcbd0cfe-eafd-3fa2-801b-e29aadefde49 | -5.37357 | -56.04884 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1291fb7a-f2b8-34c3-bed5-b2148df446b3 | -6.1912 | -55.47519 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66d6b2fb-62d7-34bc-8fd9-37b0b737aa06 | -3.0478 | -61.26424 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82cd4038-8111-398f-abad-6bf3414af1f8 | -4.34154 | -46.36678 | 2026-09-21 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea4ddf1b-4101-354e-a07e-f9c84a5da074 | -3.61 | -60.57109 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e199b26c-355a-3461-a3d4-085c743c7539 | -5.92027 | -57.67546 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1130f585-2af5-3569-9b15-277642cf6d11 | -3.38085 | -61.29827 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 379c7bf5-dcdd-372e-8466-4635a20b5f0c | -6.22799 | -56.04644 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e550550-2299-3d39-b0a1-3830ca6ca354 | -2.61127 | -51.72246 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a78b5b46-8a9f-3771-8888-a255dede37aa | -4.07355 | -52.1276 | 2026-09-21 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6730fe8-534f-3cc1-8aec-dbdfdb262a03 | -3.10936 | -61.417 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45bc01cb-5339-3b56-b194-e833f70e06ae | -5.35705 | -56.04626 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13a150e1-db5f-36dc-800e-b1665b84e0c6 | -6.34119 | -55.29596 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 698a0e26-c0a9-374e-8a2f-d41c60a1c673 | -3.1418 | -57.67778 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faefe640-cdfc-3646-827b-e665af5016fe | -6.14481 | -55.70443 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81976537-2ea7-3c85-85f7-3bf53d675a7e | -6.89025 | -55.6586 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a1bb78f-2ef4-312b-9b6e-05693d0dcb61 | -3.96234 | -56.1308 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f12abba4-f299-372a-b1b0-d82de90e2c23 | -6.2511 | -57.78062 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84069431-e1b9-35b5-b082-0d6469756d1a | -6.00141 | -45.24943 | 2026-09-21 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a18f0bb0-1f45-3c47-a770-8f22e8b1cdc3 | -3.33575 | -42.77048 | 2026-09-21 05:04:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55563a99-a68e-3671-adbd-a90e55f575e9 | -8.13389 | -46.82154 | 2026-09-21 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 224efc5b-d8b3-321c-ba05-6ab272a05e04 | -3.68506 | -60.59767 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e71ade96-d24f-3483-a45f-75b3e60b8012 | -3.27364 | -60.88828 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e0152c7-13e6-3cc8-b138-792482caa045 | -5.97682 | -55.36349 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4236648f-0cbb-3011-89e4-c16b23078195 | -6.4915 | -58.38155 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dd56e6a-53e8-3bfb-aeaa-b4ed88f40721 | -5.98169 | -57.77575 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c57473b4-2e2c-32ad-97af-e263e05d4a5a | -3.34629 | -59.85543 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c215e982-6820-3d8f-86ef-7060d0bda5cb | -6.25493 | -55.43548 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a5d2655-3345-3a47-9021-7218d5a3fdea | -3.5865 | -59.06643 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90344ae7-a73c-37c5-a0cf-23f890454f3b | -6.11002 | -55.66725 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b6aaf50-c7ed-3013-8728-08602f90b2ec | -6.91505 | -43.7308 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22caacf5-c0e4-3c0f-8351-f303ff3fb433 | -6.31024 | -60.01906 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 02136fe7-6444-34ac-99a3-a42287ddab1a | -6.13986 | -59.94516 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e29950b-18dd-35fd-af1c-d9106693c54b | -2.91732 | -54.19318 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e2ac577-3fb8-37a8-b9f4-1149c22af22e | -3.01563 | -54.17236 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 271b7252-114f-34fc-bde0-e80d0c89f4ff | -3.24737 | -58.75053 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da23b966-7e03-33a1-8f5a-786b99af9b49 | -5.83561 | -53.54751 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 731e9772-4fbe-33a5-8244-751eeba3fa28 | -5.82012 | -52.11712 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45bdbaa3-e4ef-32c7-98f9-c9201a6e1536 | -6.09743 | -57.62427 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a18778f-49ec-344d-88a5-878a548fbf86 | -6.0132 | -45.25098 | 2026-09-21 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1b8e4347-3034-3e31-9750-d750f6f88ae9 | -6.34065 | -55.29943 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f21fe05-370d-3fe5-bbb4-510d9746f642 | -3.02237 | -51.19638 | 2026-09-21 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1919db95-599d-349b-93f3-ccb22e910969 | -5.85119 | -53.51453 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8756dc77-e97a-3f2f-8a68-1b3fd41ca063 | -5.88479 | -57.72287 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7c310d7-94c6-3b28-bd90-d8851f44a7af | -3.60943 | -60.57471 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8f5a2c0-7247-3c9a-a225-9018f7565088 | -5.21804 | -56.10933 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f87f9e2d-5393-3784-bf82-a80b7fbaa8c3 | -5.99495 | -45.25277 | 2026-09-21 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2defe817-fefc-3a0f-958c-08a093ea2666 | -6.26755 | -55.41969 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce89feae-ada1-3aa4-b91a-52cbc77a50a5 | -6.07589 | -57.62838 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9899761f-128d-3622-b9d2-5cce0bc0a65b | -3.43032 | -59.26505 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 829ad043-398f-34f9-830e-be24e118b9df | -5.83851 | -53.5518 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f79865f-27e1-387c-9a10-10be21c86ec2 | -4.56268 | -54.92248 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ada78aa2-58a1-3458-bbee-dfb43fd97c77 | -5.97628 | -55.36695 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dab96c1b-0a5a-317e-b249-6ce8b5166cb5 | -6.26262 | -55.42958 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac17ea95-f031-36f9-b1a0-238a4ea26406 | -6.73088 | -55.08439 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7361c979-a4ed-32c1-9ffb-3668c2926633 | -7.4871 | -45.4788 | 2026-09-21 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5632ecda-8490-36a1-bca2-7efcce34a549 | -6.75353 | -55.61969 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0021098-6109-3c0e-8837-31af2240e2a0 | -7.30014 | -46.78205 | 2026-09-21 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2763d6ba-0cd2-3580-a19f-18a392898bb1 | -6.14287 | -59.95039 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README59.md)
