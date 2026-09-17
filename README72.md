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
| 779d0a01-8fe5-3540-b659-dc385314eb02 | -3.54054 | -59.06407 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08ef9f2e-f076-3698-abec-fbd2beab5c6a | 2.72012 | -60.2941 | 2026-09-17 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30d0deab-21f1-3175-8edf-6319f2b4b954 | -2.96322 | -50.31853 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16c1c0e6-ed11-3177-babe-cc472ff0040a | -2.82146 | -51.34363 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1da04305-36f6-39c2-9df5-ef21c8d54ab9 | 2.71681 | -60.29462 | 2026-09-17 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d3ea431-8491-3aec-82e4-b921313db179 | 0.90943 | -59.62984 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53388e53-67ba-3e29-8b0a-d64e3912d9df | -2.96251 | -50.32329 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e305719e-a2cc-3a82-a6ca-89402779742e | 2.71736 | -60.29806 | 2026-09-17 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cf06890-fd12-3b59-b2a8-37f9efe24d60 | -1.60962 | -55.56276 | 2026-09-17 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f026ac2a-adfc-34b9-859a-28c604fb398c | -3.71055 | -51.11272 | 2026-09-17 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd471336-e273-3920-8549-ec1599de0dc3 | -2.90436 | -54.17809 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51ac54d9-a8a7-315f-933d-8e9bac64161e | -3.75855 | -51.14488 | 2026-09-17 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2b3f63f-00b4-324a-8971-114107fbe875 | 2.20059 | -50.88103 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e8f64a2-0a06-37d5-ae2c-8036be458476 | 2.75684 | -60.89155 | 2026-09-17 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 251ae93c-db56-30fd-b638-4335596e7f22 | 2.71351 | -60.29514 | 2026-09-17 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30110684-4827-3849-b555-e1c71c028cba | -3.33556 | -59.82499 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 113880bf-d8d8-3c98-aa67-cea5fc0e2455 | 1.96244 | -50.97892 | 2026-09-17 05:33:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af96e605-5ee1-3e76-8479-fcf78ebdd821 | -1.197 | -54.21873 | 2026-09-17 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2016829-87d4-3987-9549-a2a656e5e39d | -3.44475 | -50.66509 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6ef0ab2-3add-33e4-813b-7eeb0515a5c7 | -3.75977 | -51.14574 | 2026-09-17 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41d3d05d-0b97-343a-afc1-15443e05149d | -3.45023 | -57.97474 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 50f83fa1-5bd1-3c96-9372-594617b6b5e6 | -3.33783 | -59.83287 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a07be11-fee2-342e-8b11-5300034f5e83 | -4.1347 | -54.41993 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59f9056b-cea9-367f-a718-3dc86a05b2b9 | -3.3944 | -50.45272 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ea9607-3839-3c32-acc8-80398cf7dcbd | -2.89963 | -54.17733 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 09714127-0eb2-3d88-bbb1-b1f68f032e81 | -2.69765 | -57.61232 | 2026-09-17 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eff00c12-1fd2-3512-a6e9-e96809b04dee | -1.14762 | -54.17262 | 2026-09-17 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| add03513-9576-383d-b641-a632d0ff0a01 | -2.9036 | -54.1831 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f519c3ab-4f08-3cb7-bb12-bb3f569296ed | -3.26761 | -54.26371 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3ca2c59-24ef-36b6-80fe-a1a3a4bbdafb | -3.71117 | -51.1085 | 2026-09-17 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9afff96-6741-3837-a7c2-53ccec880a8a | -3.33897 | -59.82552 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca07b06b-1062-3bff-95e4-6a3da75a213f | -2.90909 | -54.17882 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c433a7b-645a-3e0a-8869-f89e3d61a786 | -3.32048 | -57.86566 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db1cefa6-7aa4-364e-b673-f69fcc89339b | 2.20693 | -50.87941 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c8240f3-b205-3713-933b-d0b3686f40d1 | -3.15937 | -58.63449 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 466e5c0f-6c79-3ae5-ba80-deb1454a1026 | -3.28579 | -58.8172 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf5d2aee-a3a1-38a0-aabb-070cc6a7e856 | -3.14672 | -58.64499 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45f8b45e-39b3-37b8-bd6e-e08d64bc5c69 | -3.50601 | -53.20511 | 2026-09-17 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df9a86d0-fe31-3085-9819-f0a9601b5c28 | 2.72066 | -60.29754 | 2026-09-17 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cca6e95-70ca-3746-92d5-ee898a1f01cc | -2.19041 | -56.83965 | 2026-09-17 05:33:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 756c03c4-b666-3471-b8d6-84ab1d67d464 | -3.31606 | -57.86956 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a478211e-4769-351b-aad8-ec279d123794 | -2.96864 | -50.32418 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18b5d333-10e1-3b52-b509-77798a22272e | -2.83367 | -56.72372 | 2026-09-17 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de2c0db4-7193-388e-ac2d-ae51f7834e85 | -1.81405 | -54.93473 | 2026-09-17 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01b012b0-2b76-3558-83e1-94fed595edb1 | -1.18444 | -53.38494 | 2026-09-17 05:33:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9177c7cc-a64f-31cd-819d-bb4dd8cf490a | -3.76506 | -51.14149 | 2026-09-17 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eee68a12-4278-35dc-91f1-b843e3e1ba55 | -3.37411 | -52.7965 | 2026-09-17 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e290c39d-f9c0-3d87-af47-587a383b08ba | -3.48263 | -58.36601 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdcce112-c570-3cd3-aaf8-2552705cb28e | -3.4756 | -54.70966 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 212aba1a-9ad9-39ed-830a-c331fc5c0a9a | -3.84494 | -51.76572 | 2026-09-17 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff5a8e37-c99f-3174-a54d-dc8a1464ecda | 2.75738 | -60.89501 | 2026-09-17 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a322c749-6424-321b-83cc-288b6288d22e | -3.38894 | -50.44741 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d011057d-4038-38df-9193-857ba67aab4c | -3.01746 | -51.34499 | 2026-09-17 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bb204ed-5cbf-37a1-894e-d29af3549837 | -1.61324 | -55.56729 | 2026-09-17 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7491ca39-209c-3318-a6f1-c5b51d7b8408 | 2.21209 | -50.88275 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 846da244-d516-3dc5-a9cd-633ba7d6f35d | -3.44212 | -58.41149 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ba2e4d3-c2b5-3ff0-87cf-30ea329bdb45 | -3.76041 | -51.14149 | 2026-09-17 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2b3064c-3a6f-3415-8a03-158bc54248c3 | 2.7212 | -60.30098 | 2026-09-17 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14971421-ced2-3a2a-bb55-f138116bceba | -3.13057 | -59.02465 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a2e6a4f-ecaa-3dd3-b516-61e42460bde3 | -3.84438 | -51.76945 | 2026-09-17 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 015d34ec-526e-336b-b416-fb92a29366c7 | -1.03698 | -53.73841 | 2026-09-17 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 87979f0b-38e5-3189-a5d0-7e29c60e50f3 | -3.4841 | -54.71569 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5e8be121-f21b-3b1f-85d9-edf139279547 | -3.47934 | -59.48442 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38e66a13-008a-3967-8ce2-43d004fd2663 | -2.96392 | -50.31383 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbcb1058-6014-3bb4-8cdb-e597ebf673f7 | -2.87587 | -51.88012 | 2026-09-17 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cecbe3f-ad81-3d50-a723-c9756273efe3 | -3.54679 | -48.17904 | 2026-09-17 05:33:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 230e383c-42be-3643-8988-d0202a3cd1af | -3.44514 | -57.98302 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5639528f-e466-3292-ae5e-3f5280b609e4 | -3.17758 | -48.58475 | 2026-09-17 05:33:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d52804b0-6a4d-3985-a2f0-dec5c9a50190 | -3.33596 | -54.17174 | 2026-09-17 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04c0ca2f-6620-3403-a588-77f10728ca18 | 0.79016 | -59.20142 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17d992dd-e49c-3a12-b158-b9e9d9e6378d | -2.10471 | -52.04832 | 2026-09-17 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bf53e1a-9bfe-3b1d-9ff3-3fd3f5b2868d | -3.33614 | -59.82131 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4652f6e7-0051-30cf-a371-8d3c4777b1a6 | -3.44808 | -58.42102 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53298940-cfe2-38ac-abcd-6de96e1be99e | -1.61265 | -55.57111 | 2026-09-17 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acb3a085-1356-3d75-8576-cf964d22000a | -3.75917 | -51.14064 | 2026-09-17 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20137aa9-bc58-33d7-88a4-21fa7db95503 | -3.48481 | -54.71099 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 61246571-8cb3-3d9d-b5fc-862e4fd66d2c | -2.90114 | -54.16732 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 916565ac-b9b8-342c-b46d-a4495896d79b | -3.4581 | -59.24349 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d40fc83c-2596-3eaa-aa60-035976de69b3 | -3.45135 | -59.53477 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8eae51f-f1c9-3ff1-af81-75c6da5f2683 | -1.50243 | -54.97187 | 2026-09-17 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc0a8e96-f12d-38cd-a879-814327b48695 | -2.09877 | -52.05095 | 2026-09-17 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6daaa186-2a1d-3a0f-891b-89ef0c9929cb | -3.48941 | -54.7117 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d5f54adf-087a-3683-8ff1-6b48cb02724e | -3.59457 | -59.06429 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57bc2cc7-e1a9-3ed4-97f5-331bfa29c2f4 | -3.48092 | -54.70561 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 81df043b-4835-3d81-9ad3-21ab219e90dd | -3.47099 | -54.70903 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17fc45ff-7c3d-3eeb-aabd-a14f92156e3e | -3.58644 | -58.53944 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a25b83cc-683d-3c40-ba9a-f7eb65b03227 | -2.95708 | -50.31762 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ccc8330-db88-3696-aea5-ad6f6b227db5 | -3.4887 | -54.71639 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ef7ff1d8-e545-3f44-a222-ede8fccadc14 | -3.50557 | -53.20804 | 2026-09-17 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2485539e-796d-3890-83d3-45682e44df14 | -3.60161 | -59.06536 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d2979a1-22bd-3f9a-824f-5de704036e6c | -3.4763 | -54.70498 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9aa5826b-d1a5-3158-b663-9fb7b08b34b7 | -2.90039 | -54.17232 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52e5257c-12b6-3986-ad1d-648a1a93fae1 | 0.91472 | -59.62546 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| decbb7c0-7c39-3794-abc6-5ae79df853a4 | -3.29671 | -57.8712 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 291f8808-7dae-3ccc-b695-87817d580d34 | -3.14251 | -58.6485 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e796fbab-19ad-30dd-8f96-50a67588249f | 1.96303 | -50.98247 | 2026-09-17 05:33:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b26f0648-552c-3b38-b357-ef06d0eef7f1 | -4.10621 | -56.34343 | 2026-09-17 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0856a76f-c7f8-3bfa-becd-301618b66b08 | -3.32254 | -57.85226 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f1a34d9-7a7f-3403-b23d-040cc21b44de | -3.47313 | -54.69476 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0f7a831-945e-30b9-95d8-a5fc2637e942 | -3.40692 | -59.4119 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README73.md)
