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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e929513b-1a08-393a-9702-635d2b7a892a | -6.03037 | -42.63937 | 2026-09-08 05:04:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4a08686f-3495-3bf6-9b8b-b2c4f4b8d487 | -6.55912 | -55.67564 | 2026-09-08 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e76eec5-3d1e-3a81-ba35-e3984d2cffb5 | -3.46068 | -59.51314 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e93f357-d436-3053-91ac-b4fee65f805a | -3.89082 | -55.82115 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d52cdd1-47e0-3fec-bbfb-dd34c65dbf24 | -5.28389 | -60.12015 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6793771-89c5-3b1c-a9fd-86020e72b5a7 | -3.15026 | -60.65974 | 2026-09-08 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 175f175c-1197-37cd-8fb2-c903b5b6f740 | -4.10761 | -49.06206 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b0dd9e4-6202-31b2-9750-d3b4f1290145 | -9.70868 | -43.46174 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2ee929c-1785-3c0a-8a71-da4a320c27a1 | -3.70046 | -58.93976 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d285e8a7-a181-3c80-92f0-77ae0209b269 | -4.08099 | -48.95497 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cf6ca3a-5a3a-3739-a5c9-fb578087e7dc | -3.01753 | -51.34648 | 2026-09-08 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 112a482a-4935-3317-8ce2-10065b9e2d87 | -3.86529 | -48.97599 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0713271a-75a9-3c15-9924-5f23ee675409 | -3.55254 | -48.17484 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b5aa781-1339-3ab4-a8a9-ed7f486ffd99 | -9.29512 | -44.35101 | 2026-09-08 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d407a23-26e0-3ecb-8bdf-194d14a5586d | -9.73781 | -43.5125 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 528d9767-922a-32ca-bed7-6d2701a67c8e | -9.7045 | -43.47286 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f4b34eea-b22f-362b-a0a5-d4bde1fdd5f0 | -3.95771 | -59.35949 | 2026-09-08 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d222cba5-2949-349f-baf7-be073c14d38a | -3.78695 | -55.87744 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 191c35a8-664a-3105-8ea7-cfe0c1e3e8e6 | -4.97808 | -50.64255 | 2026-09-08 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a9577e-94d8-3f8d-9f7f-890e16675527 | -3.77303 | -58.85282 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e497aafe-5ce9-3084-9450-eb7c5963d888 | -3.13576 | -60.63319 | 2026-09-08 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a674e59-3743-3d82-b254-982961dd11fb | -5.30717 | -56.10715 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b06f9415-96f7-3d1d-a5a9-ae0ab02197b7 | -3.71547 | -51.1394 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b31f5158-4ab2-3829-b8c7-53949ca76aad | -5.93944 | -51.70378 | 2026-09-08 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f0edb08-6cb1-39c4-a0db-fbe58558c726 | -5.91574 | -52.48452 | 2026-09-08 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d9c5520-34d4-3478-991f-ce7c34e15c4d | -3.23742 | -50.6066 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d86a39f3-4723-3ec5-a3a6-6ccd5f1507c7 | -7.36809 | -47.01794 | 2026-09-08 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4304943d-58ac-383e-b97e-b74e58ac64ec | -7.78043 | -49.60693 | 2026-09-08 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19e0b80c-e8fc-3c9b-a858-c239a69675e6 | -9.70626 | -43.45853 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efc6ade1-c874-3f7c-af55-bdbe5a7dd809 | -9.7284 | -43.48583 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fcd0825-9169-3198-b042-5feced73ed10 | -9.7133 | -43.42618 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 07af7e8f-a0fa-3c3d-9703-c222ddd39f37 | -9.71829 | -43.4645 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5dcdb1a-514e-3175-a673-9b8874803287 | -3.14036 | -60.63391 | 2026-09-08 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6381cf-190f-376c-a40d-ef030ece2956 | -6.44306 | -58.15302 | 2026-09-08 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e7fba26-7558-321d-832b-92dd88d63769 | -7.37364 | -47.01344 | 2026-09-08 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c35e2e0-637d-39d6-b82c-42be23a020a1 | -9.73969 | -43.49754 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62ed217b-c29a-396b-889f-5c896934c8a9 | -2.89754 | -57.49619 | 2026-09-08 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c688f525-1bbd-3ea0-b397-3885d1cd7869 | -3.3366 | -53.40304 | 2026-09-08 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 559bd3d0-1d96-39bf-979e-132fcf25cbc9 | -3.16013 | -50.8236 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9626d635-0ca4-3c6d-874c-5bc5d89a2a14 | -9.74406 | -43.51343 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fc850ae-5646-3169-ae17-5483cd38a2f1 | -7.66701 | -46.04946 | 2026-09-08 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40d82df8-d600-3db3-818b-2988f7eba916 | -3.54776 | -48.17805 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 655bb29f-3ec3-3995-9af6-f4f4a48abd2c | -4.3463 | -55.21412 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b0ccdb1-e0cb-3e52-951f-bac7ee2124fd | -9.71877 | -43.40871 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5fa20dbe-d7e0-388b-bc57-43514a2c722c | -3.86582 | -48.97258 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 173f5da0-ce07-3387-b534-5bb207e924f6 | -7.37377 | -47.76077 | 2026-09-08 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14204d83-4572-3ffc-985f-89e948e7a645 | -9.76803 | -43.42451 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b29ec885-6afe-3cb1-8378-ad626c803d20 | -5.36745 | -50.56799 | 2026-09-08 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9df9f119-3d9f-3534-b9fc-8a2a1004590d | -4.34573 | -55.21767 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef8f740e-6396-33ca-9766-c55a565420e6 | -5.59242 | -45.37517 | 2026-09-08 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0915d7d-6714-3815-886f-cf8282110d8b | -6.33842 | -43.35347 | 2026-09-08 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8bf6b12-6369-3427-ba47-8114bd2ebd02 | -4.19283 | -59.95256 | 2026-09-08 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdf2c362-846b-3622-ac44-d65c9074a3e8 | -3.62445 | -54.60925 | 2026-09-08 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c30b31a3-2d43-3a36-88f0-d008bfd017ea | -3.79382 | -55.87852 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9efdb473-d9dc-38a1-8713-fc9fb78648cd | -6.75972 | -45.48605 | 2026-09-08 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae3d01f-70fe-3a9f-bcce-c936e60dab07 | -3.69988 | -58.94334 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1aeb0ae6-f5c8-3bfa-bfee-b582aa9a7c51 | -9.74469 | -43.50842 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b462c513-a604-3d1b-a6c1-fe9d7a17e465 | -4.08153 | -48.9515 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4e8f681-9ae7-3152-8460-04bb1444beca | -4.04057 | -50.88332 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32ba408a-5205-3fde-a5b0-f482f44fc0d0 | -4.11095 | -49.06694 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c47d4175-f1d3-398c-bc9c-753685061f44 | -9.70992 | -43.45219 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6395f14-0644-3929-a4d4-79872f3f31d9 | -3.07842 | -57.67126 | 2026-09-08 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73eff869-5f21-309b-b5e6-ca5eac7f5fd3 | -4.34795 | -55.22533 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd53f206-21ae-3b60-8f67-f65f69b00ba2 | -4.53834 | -54.92952 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7627834a-b8e6-35f8-b7cb-5a588c18c3ef | -3.0536 | -59.27362 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68b0b355-a365-365b-8fc3-34359f7d7b03 | -4.93399 | -42.88096 | 2026-09-08 05:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfb359b9-509b-3e58-ba32-e139d09b01d2 | -7.6127 | -47.29331 | 2026-09-08 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5e63e97-cb13-3f7d-9b20-f8c441520d3e | -3.44363 | -53.04788 | 2026-09-08 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a0e3f6-6bcd-34cb-a36f-fff2a9ffb012 | -6.69267 | -47.41764 | 2026-09-08 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f6c603f-9ea1-3e57-a3bd-c88be7dfdc37 | -3.05842 | -59.27049 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f090b11a-6d00-361e-8bd7-83d8bd1969e4 | -4.34295 | -55.21358 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 867a72dc-9a8e-3f70-9ef1-e73350cf1025 | -4.8215 | -55.76995 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6de06762-6136-3ad6-867b-ef7b19ef778b | -4.48471 | -55.50455 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c9f0ce9-05ac-3ff0-8675-16c92772f164 | -2.91397 | -54.11979 | 2026-09-08 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3284c7cc-e0b9-3fbd-9747-f026edf152ec | -9.71459 | -43.41625 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 18c26691-f62c-39c6-ba89-8f96fd913230 | -6.409 | -54.80929 | 2026-09-08 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8d4b999-967a-3e6c-b202-7667139d64b8 | -4.36188 | -47.77482 | 2026-09-08 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d7c88f1-5a2a-31e8-aad9-7b332787c1cb | -4.04181 | -50.87517 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f757eb7-89a2-3cdb-883e-a8fb96933784 | -4.05257 | -50.87675 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0112d91b-f57b-3c71-ae87-85d7d9e04aa2 | -9.70509 | -43.46799 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08fbc469-3c54-3a38-857e-15445dbaf561 | -5.45331 | -60.17759 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20cc080d-c3cc-32d8-af66-28b75462c5de | -5.13878 | -55.95496 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2169485d-6166-3df7-9397-886885ac7677 | -6.76588 | -45.48553 | 2026-09-08 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 993801b4-4916-36a5-a51f-6c8d5ba00a05 | -6.63818 | -59.43941 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5db675de-8913-3452-88c9-d1c6ff6373ee | -5.94356 | -51.70045 | 2026-09-08 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ad7441-6e58-386e-aba2-5b7eca116c27 | -4.07751 | -48.95095 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dcb7eb6-f065-31b7-b2cd-8648c383e4fd | -9.71395 | -43.42118 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8c719f88-5ed4-3874-8062-3bdc9f5557eb | -5.44984 | -60.23744 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84827214-43ec-313c-91c6-220721be2399 | -3.54717 | -48.18185 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 67c4211c-95fc-3508-93f7-ce830a1d1c43 | -4.03761 | -50.87872 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cce3ecda-318f-3f15-83f8-8fb2badf6b9b | -5.94295 | -51.70436 | 2026-09-08 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9872d57-0a89-350e-81a8-b7f99be03c3d | -4.98606 | -50.63939 | 2026-09-08 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d5b491f-0ef3-3fdd-a71a-4fb80ef0c703 | -9.74095 | -43.48744 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f45a0695-759b-36f9-adae-5f270fee298d | -5.36816 | -56.03331 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68f53deb-ef10-32af-b419-5f9245a2b78b | -5.5509 | -60.2421 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ae32d73-1cdf-30e6-a0db-d0c7da0db732 | -4.92841 | -55.82403 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 663d4e14-82f2-3a9f-ae16-8cdb0f303f89 | -5.70264 | -52.30083 | 2026-09-08 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c86adb69-ee0a-34b1-beaa-e24e21d15b26 | -9.71999 | -43.3988 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 763be354-4088-3c86-b054-2963ca9f8246 | -9.72902 | -43.48083 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d57e468-35de-3007-8e85-d3daf10ac25d | -3.70394 | -58.94401 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |


[Clique aqui para ver as próximas entradas](README20.md)
