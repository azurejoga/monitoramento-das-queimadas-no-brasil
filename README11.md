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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f675cee0-33d4-3833-a295-0ae657a7db41 | -2.9816 | -54.1291 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2e345871-5e14-3f49-a6c2-cea2a8c2b5b1 | -3.4762 | -50.0883 | 2026-10-07 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| b8cb764f-686e-3ddb-8520-c67816f58eeb | -11.1234 | -45.7322 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 290.6 |
| e26db4f6-56a1-377e-8c75-abb72c58af4a | -13.5117 | -44.368 | 2026-10-07 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 92601f98-fc8a-365b-894b-8b011d510f9a | -8.2865 | -50.2731 | 2026-10-07 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 81f9e612-ac0d-3c7c-80b0-0d9b90e3b971 | -3.0 | -54.1287 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 98d1d6c4-2c27-33f8-bae7-7bf351cb1cb3 | -8.7228 | -45.1812 | 2026-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 8a31e4ba-c17b-3490-ae00-fc9404a8a71d | -11.2333 | -44.8678 | 2026-10-07 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7d3d7a5d-445b-31e6-83c4-e4694013246e | -11.1047 | -45.7119 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 624.1 |
| fa7f0103-4043-373a-9748-2f03500de9f4 | -5.9647 | -40.9383 | 2026-10-07 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 171.6 |
| 1eb76dca-73c6-3d39-8999-1a066de6dfe1 | -3.6205 | -55.2907 | 2026-10-07 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d8c8d00b-7c04-37ae-9065-de437272b88a | -9.1517 | -65.9554 | 2026-10-07 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3a1c1d79-d4b8-3799-84e7-42525fe75e72 | -2.7612 | -54.1142 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 3838b74d-18a4-3e49-9bb1-22e689b82055 | -12.1939 | -44.7021 | 2026-10-07 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| a327734b-e8c6-3f6d-949b-782a5ebcd038 | -3.5515 | -59.4807 | 2026-10-07 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9f941122-d67d-3834-8478-08dca38b5392 | -7.8234 | -72.7142 | 2026-10-07 00:50:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c8ab763c-6fbe-300c-ac55-278aaff81343 | -11.7143 | -43.652 | 2026-10-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 374760f1-e27c-3c3a-9957-a892a9e36e1e | -2.7613 | -54.0941 | 2026-10-07 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 278.8 |
| 4e6b0a65-e1b2-3661-b140-9413f5ab7a0e | -3.4763 | -50.0673 | 2026-10-07 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 70b19c03-a843-3faa-9c5a-7a61367f723b | -3.4578 | -50.0679 | 2026-10-07 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b980d8fa-35b3-37c3-99df-4b6bfc58cf66 | -8.7225 | -45.204 | 2026-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 214.2 |
| b43dd9a1-1152-33a7-94e8-3a80fcfffae2 | -2.9447 | -54.1702 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4046e345-6f41-3140-b590-6e117b68eab6 | -12.1554 | -44.708 | 2026-10-07 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 89776d42-3878-3d34-8187-c61a7711cccd | -12.1935 | -44.7254 | 2026-10-07 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 73204ddf-54d1-3773-ad01-1f2db7ca5b56 | -3.5061 | -51.6924 | 2026-10-07 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 4b84f288-4514-3adb-8f91-fa8e89ebeec8 | -3.0557 | -53.9464 | 2026-10-07 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c7ba6bf8-f135-30b1-982f-071d3e165882 | -3.1114 | -53.7839 | 2026-10-07 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 7ed21014-b36d-38a3-b749-5d00c5dab908 | -11.065 | -45.8084 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9d5efbc0-0c40-3675-9938-3a9918edc204 | -1.801 | -57.1161 | 2026-10-07 00:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 2498d099-9383-394c-be9b-6202d21140f5 | -2.9264 | -54.1706 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7fbd8cb4-4656-3e2c-a47a-5432500261d7 | -2.7613 | -54.074 | 2026-10-07 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| e4299f5a-80f2-3ec9-85fd-5417a3c36701 | -3.0373 | -53.9469 | 2026-10-07 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c2f26435-7b5b-3c20-9685-f62d410d710c | -12.1742 | -44.7284 | 2026-10-07 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 336.1 |
| 3f25c75f-be24-34fe-bbd1-17944ec24ed8 | -3.4577 | -50.089 | 2026-10-07 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 7bf4dbc1-8ab4-35db-9c28-5aa7b0e1d866 | -11.1238 | -45.7093 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 294.2 |
| bdf83b41-af1b-32cb-8944-89717d551f27 | -3.0917 | -54.1666 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 56c7926d-20bd-31ae-8505-1ad8df7f1a4b | -1.8011 | -57.0967 | 2026-10-07 00:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 44173d3f-3904-3010-bcdd-8c27b4416f95 | -14.2531 | -41.6256 | 2026-10-07 00:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 9e11e31b-4e5d-3ff7-a5ae-d79928524d6b | -8.7033 | -45.2289 | 2026-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 1d44c305-31ff-3278-aa1c-6777051d39ec | -11.0646 | -45.8312 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| fb752e05-b248-3133-b04c-cb0bb7830618 | -8.7039 | -45.1832 | 2026-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 799a9202-c729-3ade-91cb-98822a0c2887 | -3.0558 | -53.9263 | 2026-10-07 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 912c7356-d8b5-377c-b507-d0e3d46658ad | -3.8382 | -55.9972 | 2026-10-07 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| a7fadddc-22ab-39e4-9898-d17137480dd3 | -3.0184 | -54.1282 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c38a3a97-7912-3f66-9375-5afc310a1eb8 | -3.0375 | -53.9066 | 2026-10-07 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 00775025-8ae0-3e1d-a682-fbcd4b00d8ec | -3.8567 | -55.9769 | 2026-10-07 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 51c9e84a-ce42-3659-8d99-b5317ca24ddf | -8.6847 | -45.2081 | 2026-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 49510c52-f1da-3e8e-8d7d-d925915a912a | -5.9649 | -40.914 | 2026-10-07 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| bf66f13e-b8b2-31aa-9606-5ae5cc811eb2 | -3.8566 | -55.9967 | 2026-10-07 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| d289b8e5-ae9e-3c1a-9a3f-50822377d895 | -6.2947 | -43.6427 | 2026-10-07 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d2a20d1e-4905-336e-b95e-31ed0ab5776e | -5.9838 | -40.9123 | 2026-10-07 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| ca6a7d1d-4acf-394e-84d9-9c50cab88846 | -3.0001 | -54.1086 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 27906146-740b-3673-ba74-36acc2c48ecf | -3.8997 | -59.3198 | 2026-10-07 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b505a824-817e-3657-a0c7-a4601046f563 | -12.1746 | -44.7051 | 2026-10-07 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 366.8 |
| 5e7c5945-04a4-3cce-a432-7eaa897db771 | -5.7187 | -45.1773 | 2026-10-07 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 79aad923-0692-397d-b26f-87046b09637b | -9.05031 | -65.92239 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7672801b-f371-3d0e-950f-ddf6be3ae8fa | -9.6186 | -64.18006 | 2026-10-07 00:54:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 63191e47-6578-3fcc-ba17-7df8f49c1571 | -9.23456 | -67.87872 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b35d453b-c12d-3877-9d6d-165588abeac1 | -11.30637 | -61.78302 | 2026-10-07 00:54:00 | TERRA_M-M | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 049eeedf-6986-3563-bf3e-7ed480a0f73e | -9.45126 | -68.41566 | 2026-10-07 00:54:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 26.7 |
| e3df5168-d91f-3b7a-a1c8-0b22c0c83657 | -9.24577 | -67.96071 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dcb5b517-04e8-37b5-95b7-e68c81ad4fc3 | -9.547 | -64.81361 | 2026-10-07 00:54:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 825e1140-745f-3f13-ba5b-18ae6ab49ea0 | -9.11741 | -67.85555 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0c977045-2a15-3b5d-b9a7-b9a75f41645a | -6.77396 | -56.22875 | 2026-10-07 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f6be6af9-f5d0-3f7c-b9ff-b95ca5a3caec | -9.29279 | -63.74512 | 2026-10-07 00:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dcd20ded-6922-32a1-9c5f-4ae3b105c0ec | -8.97633 | -65.43534 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67970abe-13b1-33f8-a94c-cdf6cd1b2763 | -6.76896 | -56.24841 | 2026-10-07 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 6e282d0e-6afc-37e0-b1a5-5a1733bab810 | -8.33358 | -70.80807 | 2026-10-07 00:54:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 19.5 |
| fa85c01b-343e-3026-8893-6a8b21a6318c | -6.77758 | -56.25268 | 2026-10-07 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| e57607b8-6724-3add-a801-c70c16c96ac1 | -8.594 | -67.05003 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 515a8db7-af9e-3ee8-bf3e-c0a6f9e89980 | -8.60435 | -67.04866 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d8b58b67-707d-3fcb-b00d-b2a5d130132c | -9.28323 | -67.89602 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fbff8260-41ea-3f3e-9181-2f4c4fb5a6ae | -9.05172 | -65.93308 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 34a50550-3f95-3473-a102-fe4aa7d55219 | -8.83337 | -62.41879 | 2026-10-07 00:54:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 29e7b645-3978-3438-b776-e1e4a7aa8ed2 | -8.1585 | -64.07554 | 2026-10-07 00:54:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e1a17fa-b369-36b6-a1ac-df4594de787c | -9.30165 | -63.74387 | 2026-10-07 00:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 800efd36-7fbd-3217-933c-5de03b26e746 | -9.0752 | -65.48822 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da28c470-566a-3629-8676-3b39d55e09bc | -9.46675 | -67.08696 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 01d65caf-3e34-33f4-bf63-886b418321c8 | -9.59659 | -64.29223 | 2026-10-07 00:54:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2bdf870f-7729-3d14-98d6-5fd10c909c7d | -9.11373 | -67.82668 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2b4ec320-35fc-3704-acc4-13a65fe7a79c | -9.06981 | -67.74522 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 418a3b7c-4855-38b2-a6d0-f04d326fb06f | -9.4651 | -67.07404 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cfdb7a55-5786-396d-a8ba-2852023a9ca8 | -9.28507 | -67.91068 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| df7a440b-e5b8-3d45-be14-e723f74913a4 | -6.78289 | -56.24643 | 2026-10-07 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 07726f37-2300-34db-aec2-f85d282b3e8e | -9.5483 | -64.8233 | 2026-10-07 00:54:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04ec8942-c8aa-3544-83f4-41780b94b57b | -9.05637 | -65.49079 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a01cceb9-a45f-34c8-92ea-171add27c685 | -9.03609 | -65.74106 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 06bc1a36-2990-303f-a443-4474b94610c1 | -8.97767 | -65.44544 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 340911b0-03f2-3fc1-a282-416b53dc2958 | -8.95568 | -63.36625 | 2026-10-07 00:54:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7765b88b-879d-30eb-a843-4c8827284d77 | -9.46459 | -64.33585 | 2026-10-07 00:54:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 72c0c6c1-9250-3036-8631-6f7fcb1c9553 | -11.94553 | -60.76918 | 2026-10-07 00:54:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12ce1019-9961-3feb-9a60-750c338eff1b | -9.04207 | -65.93443 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c3e74b4f-0e15-352f-9259-12562c872a7f | -8.84637 | -66.78722 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ab94e3a3-70f4-3d12-902a-63a2b4aa0c67 | -9.44926 | -68.39964 | 2026-10-07 00:54:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d211a6b5-2fbd-34a2-a9d9-3d1a5141a38f | -9.138 | -65.41138 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e797ce5b-9053-3ccd-9b78-bcb214248332 | -9.47373 | -62.38437 | 2026-10-07 00:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b3131014-33bf-3798-9cc7-b080a2c17135 | -9.14082 | -65.28831 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 724fc8fb-76a3-36ba-8ae0-a3855f61b5aa | -9.03749 | -65.75156 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f496a4b2-da97-30bb-82dd-f9d6f60c28bd | -8.58922 | -67.31547 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 30bd1ab1-87be-397a-8a1b-7650b06348a8 | -9.16975 | -61.40559 | 2026-10-07 00:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README12.md)
