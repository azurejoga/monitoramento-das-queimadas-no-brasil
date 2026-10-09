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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a652e1e9-54ab-36e2-80d0-64186b8dd478 | -3.29737 | -54.00589 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1ad4e4d8-e83f-3a4f-acb5-0f2e1fb38cf1 | -3.39002 | -61.07624 | 2026-10-09 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd323f89-665d-3f32-b221-b2ace8f5d316 | -2.53583 | -56.42582 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a074789c-3b40-3f09-a056-cf6ac08c6243 | -3.89836 | -58.95611 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 805b2d9a-dc2d-34c1-8921-47c5dea51278 | -3.55759 | -59.49665 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad3c4d10-34a8-3bb3-a0c4-9b20cc41eeb5 | -6.84704 | -59.30066 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a6615ce-0c4b-3e0f-a5bb-29e0eec1ed81 | -3.9249 | -56.02951 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c408420-ed8c-3dbc-9a62-abc7e243f718 | -3.10217 | -54.18898 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 502844aa-803f-3e3b-8b72-7a544c133cf8 | -2.78465 | -54.07331 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c90a780b-5384-3477-9cad-15de1c5dc9d0 | -3.69345 | -60.53905 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cd22cb0-40a7-3a8e-803d-aa3b8e6d5979 | -2.82564 | -51.28444 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4b8894fa-7717-3921-bc84-8fcd3348f432 | -3.19538 | -50.55574 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 696db3ec-1ff3-3b64-b58d-7900993a00cf | -2.74534 | -48.42962 | 2026-10-09 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ee4f8c5-002c-3dce-928d-dfd60a62bd3e | -2.99316 | -54.07615 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dbc2504-3c9f-33cb-a563-5fbe0973dc33 | -3.02001 | -54.05584 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1001839e-6087-3e35-9d91-2c2515eee049 | -3.64624 | -60.63522 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cc05d12-432f-379b-b145-d08f7dd72cb6 | -2.62481 | -56.48466 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3993a660-c17a-347b-ba0e-045fb8f614d4 | -3.86309 | -56.0053 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6289e1f-f2d7-3708-856d-1ca0271a5b63 | -3.38499 | -50.2203 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0387cb96-067e-3b9d-9f97-870f368ef16d | -2.57058 | -56.18467 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cab5cf44-1525-3e9a-8b9e-e29b7f7b3a87 | -2.82743 | -54.116 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b55990e2-af1a-3fb5-ab77-c4e9910a4aa2 | -3.07967 | -54.26525 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a0e94b-67d6-384c-8c6b-3d65324502a6 | -3.3054 | -54.05663 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e38e5e8a-e020-3e1a-9f91-fe9b52616360 | -2.74664 | -54.11576 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d92833cc-a13d-319b-bceb-aa6b8c8d392e | -2.55115 | -58.04459 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43fb8135-fe3b-3cae-ba8f-143f1d3c66fe | -3.18875 | -58.65266 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 229b01c7-1963-3581-890e-38959e6de31c | 2.76507 | -60.00228 | 2026-10-09 05:23:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04d1e969-9503-3d1d-bbcc-1460ee28d899 | -2.3949 | -57.89342 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa4a4ee8-bcf2-383d-a116-7dd7b55667a8 | -2.83529 | -54.14128 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5900e3e-516b-3e57-b0ea-fc21e71ff6b3 | -2.79467 | -54.08452 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b50768e2-4fa9-38de-a80d-885acf74f550 | -4.61811 | -49.20987 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c681f49-5967-3f0a-a49f-99bbf3cff069 | -9.25211 | -62.31089 | 2026-10-09 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86c76c40-ca5d-3ef3-8a6b-ed23dd5c6e37 | -3.55205 | -59.44543 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70b968c7-ead1-3005-9d4e-fe5b83c58591 | -1.21018 | -55.69963 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdc7a1c2-4822-329d-aff4-f1025aa2033f | -3.02836 | -54.06425 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95373a4c-551e-39ae-a6bf-2ac02623decf | -2.76241 | -57.69617 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3715a3b5-c629-3e97-8574-5e5ab4fbd762 | -2.56381 | -56.16064 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f57c11-262a-306a-8475-e184a36cbab0 | -3.35862 | -59.50489 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a27b85f8-9915-3801-bf06-2db164d6b5db | -6.91891 | -59.277 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 029e9554-5e75-320d-b531-2cdeea987f1d | -2.51151 | -56.17941 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e172f968-2687-3bcc-b647-7da7acdd6904 | 2.76991 | -60.00981 | 2026-10-09 05:23:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f2282ef-054c-32fb-878a-14340a7388bf | -3.50332 | -59.28016 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0628349-0a23-3618-aa40-a2c6e78e0e9e | -6.92771 | -59.26422 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cadd79c4-0167-3f3a-8afc-517a024b959a | -0.04931 | -50.82629 | 2026-10-09 05:23:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c80aa45-a017-36f3-8aaa-feef9b284a5b | -3.17219 | -58.62889 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dfa781e-b609-31cc-9049-d1918adbb67b | -4.3924 | -56.04593 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aef9c8b8-84bd-3589-abf4-fb798cdcbcc8 | -1.12941 | -57.28077 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 178f0142-9933-3f8d-a801-def6af87d29f | -9.00749 | -45.93842 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b444f1b-0128-372e-b3f3-fc1e4ba4c7d1 | -2.60982 | -57.58711 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d415ac1b-21a0-322a-bb72-ec4f48afc739 | -2.5039 | -56.25059 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 221ca852-3f3f-3d17-9986-2d3b44facc57 | -2.26651 | -48.05816 | 2026-10-09 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa52f64c-0f82-34c4-ba0f-88fa06354f11 | -3.34124 | -50.41171 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63a20808-f02e-3852-a3fe-30628982ccc3 | -3.57532 | -54.68511 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c87a2d68-d7c1-3439-9d9b-e0291a644444 | -3.29915 | -54.04577 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 802452e4-e555-3cf9-bab8-e2fc0b095948 | -2.94488 | -54.18476 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9b427b1-75b8-36fc-a707-866c1b8eb4ab | -3.0231 | -54.06122 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8669256e-2535-3538-b85c-be6282edc3a3 | -3.34963 | -58.19559 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfdb81f5-52d5-3483-8a75-8a01fd5789c3 | -1.2085 | -55.68783 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 892ac1d9-a261-3d97-910d-6d80d13e8fbd | -3.11044 | -54.1691 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c98032c-a66e-3a80-8d69-67e3bb6082c8 | -1.19011 | -55.66941 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe4ca640-fd6c-3811-bcab-4333d65eee61 | -3.55055 | -54.67212 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7aee35f3-e0c3-3e68-a40e-cdbe73f671d7 | -3.85632 | -51.93719 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94a9153a-4460-3601-a07e-66f8ad86e334 | -3.00534 | -54.04873 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95a831d2-1f7f-346b-9e18-e1cb69408512 | 1.21906 | -59.97614 | 2026-10-09 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09b9284c-1cac-3f10-a949-04bb1ae8ab25 | -3.18432 | -58.63785 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 494bc84b-edf8-3e7c-a881-c6ff2b7b8ac4 | -3.02763 | -54.06903 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75b8c1d1-9892-3d2b-ae0a-87d8f22b3b16 | -1.21451 | -55.64988 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 383ed853-d34c-3825-ac21-32ae26e70581 | -3.11039 | -53.78739 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 11782a2e-db05-3dc4-9c99-14d9b7316b0c | -6.45142 | -59.94927 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 404cc1b8-da47-37cb-b30a-65de90200caf | -3.19471 | -60.43491 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03b7c81b-f0b5-3753-9f87-182b46dcf039 | -3.00224 | -54.04336 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2079989b-150f-3a33-8328-5e17ff0d2350 | -6.72858 | -63.05102 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6da1259-37ba-3b9b-be68-3649081e851a | -3.25051 | -54.66662 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c14ff8e7-f519-3f11-8ab9-b9e971ff0da8 | -2.77698 | -54.07215 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d278835e-1fcf-352c-b258-3ca2d5b7fc7a | -3.19622 | -50.55028 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6cfe793-8797-3d9e-bb77-0150fda8f047 | -3.4053 | -59.57728 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a99ff674-92b7-3c0e-8a6a-6097305152c2 | -1.7265 | -56.06923 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b10644f-1df5-36a5-a8d0-5a689340c6bd | -7.57154 | -61.54432 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e8e10dc-26b6-3d02-8dd0-15ad40d1336f | -3.9841 | -59.33475 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1215a314-f57c-3320-8a16-e45e208f9952 | -2.50763 | -56.13654 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 687209b3-4bf6-3211-933e-f5f601e28e15 | -3.71001 | -60.54554 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed1ae25b-0464-305f-9adf-307df79c8cf8 | -2.94355 | -54.11714 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e30a593-a53a-3515-b2aa-6d7ab057c1ef | -3.57616 | -54.68704 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 685e0cde-bea5-3616-ad54-e279a80db55e | -2.82637 | -51.27959 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4403361-90f6-3d35-b039-3dbb035548e4 | -3.04158 | -53.89798 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f29f2c1-9da4-3ac8-a06a-bb9270e7a93b | -3.46385 | -59.2525 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b278ad7f-cf52-393b-b113-5253eab7a6d9 | -3.49897 | -49.93853 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46de06b6-9842-3646-80d0-c2a9d44c5bde | -9.29461 | -60.53031 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ae714b-ad38-3e7f-b8f7-9686cc5d330c | -3.71274 | -59.6513 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c02eec4-971b-3466-8aaf-9d5be6107192 | -3.91171 | -59.10693 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49e15e56-940d-3a2a-9cc3-d60ad50918e4 | -2.83943 | -57.48793 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b54e32-97b8-3f6a-ab96-f95490d803c2 | -4.52368 | -54.8618 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8ce825b-0457-37d5-8f28-f23bf1af8b7c | -3.17602 | -54.74294 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3faaae8c-07c7-3f49-9bd6-2a1c4af85be5 | -2.91595 | -57.47842 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a993b47a-8d79-38f0-8b04-2217443547c8 | -2.47753 | -58.07904 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c878882e-43f8-35ac-abf7-0eef8b36faa2 | -8.9901 | -45.90271 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71e47e4e-299f-36ad-af9d-302eefa8e717 | -11.07189 | -54.51616 | 2026-10-09 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b465102-353c-3486-97fa-06802bd84042 | -10.94899 | -50.69454 | 2026-10-09 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9345537-cfa5-3a09-aef2-0898f89785a7 | -3.72259 | -60.11812 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618a67e3-ee94-35b3-a57b-c74865bcddfa | -3.0081 | -51.01379 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README193.md)
