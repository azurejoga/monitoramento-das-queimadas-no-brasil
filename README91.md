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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d514837-8c32-3ba2-b62a-d5fa8a1838a8 | -6.37656 | -58.28996 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b6c7478-7e79-3a70-9ef2-413d5bd49389 | -3.45633 | -50.59743 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e6cdd45-fc80-306b-824b-94144ba8978b | -6.01342 | -57.67874 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85a1eb81-7d7f-34c5-a336-edbfe23880c2 | -2.93234 | -57.7952 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c1613c9-f79f-38a6-b64c-337c9e9a0fae | -4.42002 | -55.49924 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30fe271f-bd9a-310b-8089-6870c3da0a38 | -5.98345 | -57.78104 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 951b1f28-6e29-379e-9665-79b7bacdf9cf | -1.2975 | -54.20856 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86ba2257-060f-3980-a9a7-32d7644f1c90 | -8.31521 | -44.74968 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4c0a004a-920d-3478-aca6-e6f17f3dc951 | -3.39623 | -59.52684 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce761dca-0471-3223-852c-dc6f62792ad1 | -13.32796 | -51.28608 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39b471d9-cf24-3f03-8d0e-95dc5bc770ae | -3.06337 | -54.40576 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0f6976e-505a-353b-a7a8-4ccef6550e8b | -2.42023 | -56.44284 | 2026-09-22 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82b4ecae-c19b-3795-aa7f-b1ff0c642c18 | -8.18894 | -54.7781 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8a5c2da-d940-3f21-af10-cbf5fccf5975 | -6.15852 | -57.95554 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1cfebc0-db37-3457-b1ef-0946a37162dd | -6.19306 | -57.78209 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7396b3e5-1f31-35c6-96cf-d34e0ab91189 | -6.73529 | -55.30781 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6383d0b5-deb3-3a45-9087-571188fbcc16 | -6.33754 | -55.2796 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd3e6b43-d8f3-36c0-8005-9ee69286c33b | -6.84602 | -55.26994 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e660b89-6732-3d44-8e82-4a21d737db46 | -3.39096 | -50.43709 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e540e31-1f59-32ed-ad62-a267b62c4005 | -4.53309 | -54.97255 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19871ac2-d278-30fb-897e-04ef3980a815 | -3.40563 | -61.29826 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca951951-d031-3d0c-820c-1ce9877334f1 | -7.87504 | -54.73491 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fc3935c-df90-3b77-ac25-7be609421bd4 | -5.20576 | -56.07287 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25ca7284-d5ba-3151-9de7-5b741dfec752 | -6.52119 | -55.38431 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be7cb3fd-1a63-3b45-aea5-c0cffe763df6 | -6.61922 | -59.92286 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 34b3ddfa-59ee-3442-9fe1-bafb664adcee | -3.19025 | -60.43261 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c23fa4b3-756f-393d-8fc3-cbb5ebf08954 | -2.56559 | -57.5089 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4cec8ed-efce-3e9d-842d-f431c67b45ba | -8.35456 | -50.87399 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0026d554-38e0-3ccb-8064-cfa83020c7b3 | -10.90079 | -54.07026 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be3dc42e-13d8-3903-9a4a-1821289a9fa0 | -8.32219 | -50.83689 | 2026-09-22 05:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e26b852b-eb5c-3973-ba32-2885989263cb | -5.19906 | -56.07176 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2969f67-8479-3958-872a-84889b937de5 | -9.0537 | -48.77683 | 2026-09-22 05:23:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fb6e648-13ed-36a4-a868-91f53b2937eb | -3.51133 | -55.48765 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ccc22e7-7d8a-3a0b-8222-5d9444bfebf4 | -4.5561 | -54.93779 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7aa71f43-aea9-3179-bbe2-5e94cb33e48a | -7.24012 | -55.60704 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb2eebf9-0c72-30c6-b630-d419a79e7ca0 | -2.56406 | -54.73999 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7577c577-3c39-3e55-b51e-a679ae304a41 | -3.05522 | -54.41234 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e206c5-3aab-30e5-ad41-e432628a0aa8 | -5.98441 | -44.72476 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b301b459-9a27-3ab1-b4f0-b6ea9dced18a | -4.29919 | -55.07038 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde8be1a-69af-333d-9157-2f8995cb0695 | -3.58711 | -59.06405 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1281ab88-49fb-3be8-93f5-3d6e112a7fa5 | -6.13909 | -59.94512 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19da57c3-4a6b-3d06-9d9b-2a717e75e2cd | -3.23176 | -53.95028 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 79e87987-9263-30dd-978f-a0f133c9ce89 | -3.77178 | -61.19138 | 2026-09-22 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff4a3a1-d98e-3159-bce1-4973beb1cb39 | -5.92773 | -57.68596 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd96512f-4330-3cac-92c1-955b1e38e150 | -12.56607 | -45.96923 | 2026-09-22 05:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e89397d5-bab4-3252-94a1-d732c8e6a6d4 | -3.06685 | -54.40629 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10949cdc-36f4-342e-8cf3-3ee42f247798 | -7.5859 | -57.70084 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 128225cb-2728-3082-9931-89caddf05737 | -3.47425 | -59.6005 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac338221-0c67-3d2c-ad8c-091980b2de87 | -3.28882 | -57.85502 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| beddaecc-841f-34ae-b9d7-b4c95bfd910a | -6.90079 | -57.60996 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d86087e-c3ca-388d-a87f-d46c1c132e91 | -2.92897 | -57.79467 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 036e2ff9-5710-3450-87ff-d5e8309416a4 | -9.09875 | -65.37439 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4832834-7114-3c8f-b0e6-409f9a036ba0 | -5.75069 | -45.08199 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3c60f7e5-99db-3143-80f0-8a6da926fb8c | -6.72381 | -55.08233 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2774029c-9564-355e-bbd4-e33894b05f3c | -5.98567 | -57.70285 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e601f03d-1f23-3985-bb0b-dc929b54c8e3 | -3.68054 | -60.62197 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 836a5bd9-36db-3b7e-aa04-cf31277cdcb1 | -12.56675 | -45.96324 | 2026-09-22 05:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 04702e8a-9f13-33f7-b6d1-bbf4e7567702 | -3.69094 | -60.58184 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8dc6dae3-4b23-37a1-bf3b-f216f96ebd7b | -1.83103 | -58.47466 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f10a1c9-12ea-3412-a9e9-5623cb6b7fb5 | -2.50727 | -59.52879 | 2026-09-22 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1981e5b3-91d7-30eb-abb5-17fef2cbc0c3 | -3.38137 | -50.44213 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 894bd082-b46a-39c0-88ab-af274b5ae04b | -5.88777 | -52.04607 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fff48c8c-06b2-3310-8e39-e0a87d7efbc7 | -6.31338 | -60.00945 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc26f969-a33a-3906-8bb7-e3f471247d4d | -4.63679 | -55.76644 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49ae9d2b-a0ce-3cfd-a9e8-cb9e288b2c8c | -5.74951 | -45.08203 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bb689014-e202-39a0-ae44-7e2f864f75d0 | -2.85904 | -57.81303 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69f4732a-538d-3e69-b1f7-ba4f6bfc530f | -8.31448 | -44.75678 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5b89598b-5c22-3037-8805-ea2ecabe6dc2 | -6.14198 | -59.94967 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c433f7f-032f-316a-8b37-838799ec63bc | -3.41896 | -61.29764 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a365dfc1-b278-3730-a5d8-d0944fc775bb | -12.02853 | -47.80864 | 2026-09-22 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95988adb-7bca-3583-90e3-d0c10ad88ece | -6.3063 | -60.00825 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1622e32-13be-32d2-9db6-f5d8f19b4f12 | -6.35402 | -57.77184 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f82fa0-e240-3fd9-8ac6-7548bfc53f6e | -3.59845 | -59.44317 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf20f5c6-b111-3c66-953a-7b47792ec963 | -1.61158 | -54.62495 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd55e499-080b-341e-961c-c0f3343c3548 | -9.55133 | -66.04398 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d4c3bb-57d5-3b54-9adc-8e439c43f6e0 | -7.13571 | -48.42847 | 2026-09-22 05:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5019ae80-4f14-350c-8269-77f77fda3741 | -2.41137 | -58.27746 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10ea34c9-9586-3680-9d66-e885be06422d | -5.82404 | -52.11694 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b34bd670-cdc1-385a-b6a5-d14f7be5b736 | -12.95355 | -50.93143 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bcffaa9-3e6c-3942-8bb1-6aa1b9631f6b | -6.79236 | -58.79105 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bdc7d04-8614-34d4-9bb5-f9aa432559bd | -10.15441 | -58.76096 | 2026-09-22 05:23:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5285f4b7-d68f-33d0-92d3-ec610c5f931c | -8.18924 | -54.72734 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 190e0cbd-aa2c-3224-9c96-de909e953586 | -3.29836 | -57.86018 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 746b3d76-380f-3e5d-9590-983b87acb769 | -2.86412 | -57.80287 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 51c07c51-d18c-3e57-b52f-0987c4c191b2 | -3.11852 | -60.68348 | 2026-09-22 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efb4adb8-23da-3c6b-b09d-ce708f992a54 | -6.54884 | -56.03492 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20ad50de-38c1-3ce9-afdd-4b6160da9920 | -6.10108 | -57.63551 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c3be236-4cee-360e-94de-33e097be49e9 | -1.24658 | -54.55068 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2d2cc31-f94c-3aed-97b6-3f40fc8d24f3 | -4.34572 | -55.66387 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 680ae379-d15d-35b7-aae8-7ba521c24458 | -2.50815 | -59.52739 | 2026-09-22 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5145977d-c41e-3c49-9e39-4dd3886d6b6a | -12.87856 | -50.93253 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 4ce6bda4-45bf-3734-840e-00f6ae7113c7 | -8.08253 | -55.33564 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23366585-e5c2-3ae0-b955-3a5615654d2f | -6.46342 | -59.97134 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3c4592f-ccda-3769-8c67-d81b417af949 | -12.02258 | -47.80783 | 2026-09-22 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83f3e2e4-9a3e-3445-9374-c37f7c7b0055 | -6.69419 | -55.3671 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a84d086a-ef06-3ac6-98a2-d88f83f83ad8 | -5.21082 | -56.10619 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3142105a-f484-3e87-b179-c8a7bc5d15de | -3.07212 | -54.39538 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59bd4043-61b3-3e75-845d-7147915616af | -12.91564 | -53.89705 | 2026-09-22 05:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b33e5469-0f97-30d4-998a-a11ce1ad3984 | -3.06805 | -54.39864 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fef52d5-e995-3adb-a4fb-df056ea9c527 | -2.54436 | -58.01414 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README92.md)
