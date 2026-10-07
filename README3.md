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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab9c9afa-a57e-36a1-87d0-f6186eeb69c0 | -12.1939 | -44.7021 | 2026-10-07 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| a74cca88-1b51-36ac-9f8c-41f78bc391c1 | -2.7612 | -54.1142 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| e9b83345-44fc-3c0c-8fb9-9291ac17e9aa | -5.9835 | -40.9367 | 2026-10-07 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| da5ebaf9-6371-3b13-9fb4-5bffa759adc2 | -3.0001 | -54.1086 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| babb258b-e849-317c-9586-fb8d976c2fd9 | -3.1114 | -53.7839 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 28607f88-8628-3bf9-a3d7-e68283ef2a90 | -1.2922 | -54.5585 | 2026-10-07 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d9568a84-59f7-3c6e-a5cc-1312a9fa9c01 | -12.1742 | -44.7284 | 2026-10-07 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 337a97aa-697b-3046-b606-f5add2aa6772 | -11.7335 | -43.649 | 2026-10-07 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 834c203b-e777-3103-b4e3-46c8fae4e685 | -2.9816 | -54.1291 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5797a0fb-ebb2-34c6-9692-ee2cfb6744f7 | -3.0184 | -54.1282 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 750b591d-a559-33b8-9722-f65a655818e6 | -3.0374 | -53.9268 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 9cd358bd-99b0-3565-bd55-816d46eb7a61 | -5.7376 | -45.1533 | 2026-10-07 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c43a07bd-7529-34ba-bc59-df2121d128dc | -13.5117 | -44.368 | 2026-10-07 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| da44a3bd-c65d-3782-b150-25570512636d | -3.1115 | -53.7637 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| c9c4d448-a5c4-3a64-8f55-f7df76253274 | -2.7613 | -54.0941 | 2026-10-07 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 293.7 |
| 12ecb935-380e-3bed-9927-f9f6fed03476 | -3.055 | -54.1474 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| aaa0e323-dafa-359f-ad6b-0b5a0e63483e | -2.9447 | -54.1702 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a2ca26f0-1900-3446-bea5-5b0b73c190ed | -11.0676 | -45.6485 | 2026-10-07 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2e7ad031-9c56-3e89-b6f0-10a4e1f26186 | -3.0917 | -54.1666 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0e3fc1af-a7e6-3b96-b7f5-1e287911d398 | -3.0375 | -53.8865 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e0cc4bd0-1ea9-3242-ada2-4644de93c43a | -3.4963 | -59.5775 | 2026-10-07 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 072d0e04-424b-3de5-ad44-ff6545aa1ce8 | -3.4577 | -50.089 | 2026-10-07 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 6ba80e85-8b47-3520-8018-904c3c431583 | -5.7189 | -45.1547 | 2026-10-07 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 4b6f5d7c-8014-3de6-a3c6-20a833cdb048 | -3.5515 | -59.4807 | 2026-10-07 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| ca3c4b42-8afa-32c8-afd9-53a7b4d26013 | -2.9264 | -54.1505 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 12c324d2-87e7-36c5-9817-3c52c7b08a61 | -8.7225 | -45.204 | 2026-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| a37945a6-97f2-3351-bde0-291646aacbf3 | -3.1787 | -50.5807 | 2026-10-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 709709d6-c1ea-35c9-a561-d6caa696bd58 | -3.4763 | -50.0673 | 2026-10-07 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 60f5417c-5b6b-32b7-a1c3-fbc29d47fc02 | -5.7374 | -45.176 | 2026-10-07 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e81853ca-69d0-3b1f-b215-3723695f4735 | -5.9647 | -40.9383 | 2026-10-07 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 5ca648c3-a47e-3f17-91d5-a13204f02846 | -11.0867 | -45.6459 | 2026-10-07 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 14c212c8-1bdd-3cdb-9ca0-bd0f5b2a713f | -5.7357 | -43.2682 | 2026-10-07 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| fa1363c7-ef3e-3f1c-9535-191b115b605a | -2.7796 | -54.1138 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| ceaa917f-9b63-3d41-827b-723241881d5a | -2.7874 | -51.6719 | 2026-10-07 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c09f426e-a892-3db9-a06b-841140b51ed9 | -5.7187 | -45.1773 | 2026-10-07 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c24a3a9b-0310-3278-9beb-8d767e829192 | -6.2947 | -43.6427 | 2026-10-07 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e3e2116c-a0ca-3f03-ae00-fd7320758e34 | -9.0612 | -65.4916 | 2026-10-07 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 59f9ebf4-d93c-3766-a6cd-8abd5cb99c18 | -8.2865 | -50.2731 | 2026-10-07 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 5bb6cacd-1f35-3442-9c2e-621ec2dede94 | -3.0373 | -53.9469 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 6a293e5e-2fdb-3970-852e-b639c9b516f1 | -1.801 | -57.1161 | 2026-10-07 00:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 7e995c7f-aaf7-3569-a195-8f3727e8d339 | -8.2868 | -50.2519 | 2026-10-07 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 846ac0dd-340a-34da-a434-3dae15f024ef | -3.0 | -54.1287 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 8e6a7b0c-92b6-3d17-80fd-c23aef2e1b3f | -3.1101 | -54.1661 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 50e16c97-86d9-3cfb-b7f1-5434873961e9 | -8.7036 | -45.2061 | 2026-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 320.7 |
| caf39098-7010-3ed3-b028-3ae2f606adb4 | -3.4762 | -50.0883 | 2026-10-07 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 190.3 |
| b922e5fa-247f-39eb-9355-93c9a12e6271 | -12.1746 | -44.7051 | 2026-10-07 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 0a9ddd12-feb2-34cd-8205-37c933ad6499 | -1.7827 | -57.1164 | 2026-10-07 00:20:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6b008a8c-d380-3fb9-81e5-f7f0904ac865 | -11.0646 | -45.8312 | 2026-10-07 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 7951bd95-759d-391e-be06-63a6f4174efb | -8.2865 | -50.2731 | 2026-10-07 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 0dcfdc09-a35d-3fa2-9290-a21c42dcd1c5 | -3.1787 | -50.5807 | 2026-10-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 34b95aba-0a71-31e5-86f8-aa8786c8de8a | -3.1101 | -54.1661 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| d49b3fdb-e659-3209-97f5-4fafc1e90209 | -3.4577 | -50.089 | 2026-10-07 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 4d878829-c7f4-3a24-ae97-31a7fe7638de | -1.8011 | -57.0967 | 2026-10-07 00:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 68021c48-d506-3116-8186-3ee07c99b88a | -8.7039 | -45.1832 | 2026-10-07 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| fcd02d5e-3ad9-3452-9ded-8c11c3fcd77a | -3.6579 | -60.6412 | 2026-10-07 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ed9b2f76-e518-3358-9c49-a6ca3b0d0149 | -12.1935 | -44.7254 | 2026-10-07 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 257fe4f7-b836-304f-a1df-59851f5f0dc6 | -2.9264 | -54.1706 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 60760ec7-f4eb-336c-9a59-7072f99f263b | -13.5117 | -44.368 | 2026-10-07 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8e1acb85-377d-3fc0-8e81-b5f777303a22 | -3.8997 | -59.339 | 2026-10-07 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 31dbc51a-2d7d-3d4b-94e1-c3b337e4f17d | -9.4621 | -67.0817 | 2026-10-07 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ff68c223-a5d4-3dc2-a0e4-c8bd47a20bcd | -6.2159 | -52.8285 | 2026-10-07 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1c296cd5-fae7-3f17-846d-0d502976cae8 | -12.1939 | -44.7021 | 2026-10-07 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 96073b05-734c-3c54-8258-6f47e8f5283b | -3.8043 | -51.0396 | 2026-10-07 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 737169af-e3e3-31a4-9043-dcb61ab6345a | -3.6762 | -60.6219 | 2026-10-07 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 174584c4-107e-3756-be74-a890498e6711 | -3.8997 | -59.3198 | 2026-10-07 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| d45711bf-740c-37b6-ada3-9329d5d11449 | -3.1972 | -50.5592 | 2026-10-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d75e8987-e5ac-3d65-9691-1b9426f46db6 | -3.0373 | -53.9469 | 2026-10-07 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a840ff98-6ed9-3054-8869-421b03fb81cc | -4.7589 | -55.6516 | 2026-10-07 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4336da75-f88c-340b-8e93-9b17f4f23e22 | -3.5061 | -51.6924 | 2026-10-07 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a8a34c73-50ab-390a-93ca-f70b9670c759 | -2.9448 | -54.1501 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9f817811-3736-3696-8ebd-20d8163d160d | -8.7225 | -45.204 | 2026-10-07 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 97366f2b-6eee-3670-8390-26c9e7829e96 | -3.4762 | -50.0883 | 2026-10-07 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 1b370896-e6d8-3b68-b24e-ca13c85765d9 | -3.0557 | -53.9464 | 2026-10-07 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 68c919c3-9a54-3b0b-80ad-aaf414e6fe26 | -1.801 | -57.1161 | 2026-10-07 00:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 17bc52ab-3eaf-31e0-a552-86de86e274b4 | -3.4963 | -59.5775 | 2026-10-07 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f58865d3-01f6-3292-b930-be31c9857fc7 | -3.8566 | -55.9967 | 2026-10-07 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 8637820b-6615-3c0e-8b31-6a77c488005e | -12.1746 | -44.7051 | 2026-10-07 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 4bb004f5-0e09-3bff-b72e-62d84a2a86ae | -12.1751 | -44.6817 | 2026-10-07 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8a9d96b3-2b8e-3469-9614-3af575f55269 | -2.7797 | -54.0736 | 2026-10-07 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ff794273-0017-3bae-a061-ec83f2898451 | -5.9647 | -40.9383 | 2026-10-07 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| d68d86e0-46cf-3484-a704-6ea46e9527b4 | -3.055 | -54.1474 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| bde25d82-d891-336d-ba6a-9a522aeae50d | -2.9264 | -54.1505 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 058dab92-5af0-394b-88a4-f4a171fce473 | -3.658 | -60.6222 | 2026-10-07 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 1e9684d8-623d-339b-9b25-49c38c8d7720 | -3.0184 | -54.1282 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 66b763b6-de23-3e1c-9d76-a777332a0f7d | -11.7335 | -43.649 | 2026-10-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5ddd7ad6-82ab-3172-9175-945f233a6c47 | -5.7187 | -45.1773 | 2026-10-07 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| d4dccf8c-d0bb-36b9-9df9-512d416be94f | -11.065 | -45.8084 | 2026-10-07 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 10a20651-f087-357e-9373-3ad2532f9faa | -2.9447 | -54.1702 | 2026-10-07 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ecc84087-90c1-3fb9-894e-16a5c979776f | -3.8567 | -55.9769 | 2026-10-07 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e650e220-18d8-3e34-b860-a5f191813de9 | -3.1115 | -53.7637 | 2026-10-07 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| e827f5cd-14dc-3dbc-9a4e-431695b5e435 | -12.1742 | -44.7284 | 2026-10-07 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 26938132-76d2-3184-9560-2f86d0971134 | -3.4763 | -50.0673 | 2026-10-07 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6b9dd521-efa6-30f8-a657-9aae31ac979d | -2.7874 | -51.6719 | 2026-10-07 00:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d8c99f7b-7075-377e-9d55-e18cb1a9ac34 | -2.7613 | -54.074 | 2026-10-07 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| c0d4e9c5-0e8f-33ea-acf4-b4a9a58737b3 | -8.7228 | -45.1812 | 2026-10-07 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1ebd7936-c9db-3bec-ad04-c6e8aae04ad1 | -3.4578 | -50.0679 | 2026-10-07 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b0738ee8-c5a5-39d9-9273-bc96bb632e52 | 4.1498 | -61.2563 | 2026-10-07 00:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 17e80e81-3981-3843-b67b-2f065e7a1d0b | -12.1554 | -44.708 | 2026-10-07 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 5627c393-5421-3c1e-b72d-57ca4e3504d6 | -11.0459 | -45.8109 | 2026-10-07 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d7c4f6c4-51f9-3c36-8ae1-0dd43c741c65 | -5.7376 | -45.1533 | 2026-10-07 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README4.md)
