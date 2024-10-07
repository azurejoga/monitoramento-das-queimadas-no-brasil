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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c79f2668-7fa9-3060-9af8-53493b9c51e8 | -17.60594 | -46.94364 | 2024-10-07 05:18:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13f0db00-29ec-36b2-8a28-4b285e57d16d | -16.90967 | -47.15309 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f2f47cc-0df5-3fcd-8157-322405134bba | -16.90523 | -47.15041 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 127f748a-3377-3093-8b31-2ca6ca83d7ab | -16.90192 | -47.15888 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67d69517-77d4-3e85-9da3-e5e5ddc6a696 | -16.88315 | -47.15579 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c99bf1f-d089-3f0f-a9c0-1487d0e9d9cf | -16.88756 | -47.15829 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dbcb16a-b271-3e1a-9776-fae936f0ec85 | -16.14218 | -48.89074 | 2024-10-07 05:18:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 972d0d1d-ed05-3e58-b350-6f63ca75102b | -16.13578 | -48.88993 | 2024-10-07 05:18:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13f34123-417b-38b8-a170-054554015b98 | -16.13471 | -48.90058 | 2024-10-07 05:18:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e58f785-79d7-3fad-a6aa-dd2545b630e9 | -16.08115 | -50.20805 | 2024-10-07 05:18:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 301b9583-3cb9-3c98-ad73-eb5bf4f6abd6 | -16.08071 | -50.21234 | 2024-10-07 05:18:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00af539-7849-348b-840c-33eeed101ba7 | -16.07497 | -50.21006 | 2024-10-07 05:18:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a971454-98e5-3e14-b0e5-f667e9e15390 | -16.07456 | -50.21397 | 2024-10-07 05:18:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcf883ce-815e-306d-a407-4384d9b49399 | -16.07416 | -50.21781 | 2024-10-07 05:18:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4110ba5-814f-3c62-a6a7-e88b5c4e0f89 | -16.91233 | -47.15162 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 158a98f1-0389-3a6c-96ff-8575e8dbbfe3 | -16.90463 | -47.15728 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c8b7bf8e-83de-38d1-8515-a75153eb9ad4 | -16.88248 | -47.16354 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a88a472-5609-37ed-9019-55233fefeb43 | -16.87969 | -47.16551 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fcd6fa91-4556-3fbf-985f-6f00d9d2831b | -16.90257 | -47.15189 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc08686d-9ff3-3e70-94c5-20d9aa057e74 | -16.89031 | -47.15621 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b1c4ef9-a198-39f3-a139-916e74bb187b | -16.88184 | -47.17089 | 2024-10-07 05:18:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a119b748-9446-3991-8acc-e5fc56a2bbd1 | -17.77197 | -53.10102 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2baba69-35e1-3cf1-a389-7322121449c6 | -17.77131 | -53.10693 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfec0d87-ea06-351a-b5ee-50860dcaeb61 | -17.66826 | -53.08227 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23d7cc9d-0a4c-3c83-b818-f34fecd1a5df | -17.13748 | -51.70951 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7b13fd2a-ec64-3e86-8117-34333506afb4 | -17.14212 | -51.71715 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6d5e1950-5c57-34ae-bfb4-bdc33125c9f9 | -17.13128 | -51.71576 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c9f0cc05-a163-3d1c-adb6-b048bb7ed1c3 | -17.10921 | -51.71651 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec00bcfd-b2a7-38a5-a080-515e01e7fc88 | -17.13207 | -51.70872 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fb741139-6de7-3006-9c46-825621b03b66 | -17.11463 | -51.71723 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8c12a03-9ab6-3da8-b5d5-90fc6d193907 | -11.52401 | -65.14423 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff1c93de-9b69-3971-8d27-551533eb176d | -11.51657 | -65.09089 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba3fcaaf-83db-3cdb-b1ee-e5a651e364b3 | -10.8714 | -65.26372 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13830e08-d066-37b1-97c3-33879a218659 | -17.14327 | -51.70694 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d37e3bba-9991-3e04-b72d-bbf5e91f5593 | -17.1371 | -51.71292 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b0f46a78-987f-3e8f-a805-7164bb8224c9 | -17.13671 | -51.71643 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 53ca8de0-54c1-35cf-b04b-14192e3f5891 | -17.11424 | -51.72075 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 08c406c1-bb50-350c-8e51-a995316876f5 | -17.10882 | -51.72002 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6741e7e0-62f8-37be-a4bb-f1827dc3cf24 | -17.13168 | -51.71217 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0cc57855-6756-3b69-8c01-8ff9054af084 | -16.06761 | -50.2233 | 2024-10-07 05:18:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8f41314-8042-30c8-8231-5974ee297a26 | -16.31137 | -51.27505 | 2024-10-07 05:18:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aba85cc-9b77-309a-bd47-88a8f4f9f580 | -16.31095 | -51.2788 | 2024-10-07 05:18:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9db2832a-7c6b-314e-a64a-b424569aad28 | -17.66761 | -53.08808 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a621f9c3-7712-3238-b39d-60635ef2ab83 | -17.66695 | -53.09399 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bfd212a1-5013-3598-bb43-3d95188bd8d7 | -17.66328 | -53.08158 | 2024-10-07 05:18:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc275eb8-5db2-3312-ae25-af4eda042e7a | -9.97798 | -66.75481 | 2024-10-07 05:18:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34f41876-bf36-330e-9c7f-1f2b6cbdff39 | -9.87606 | -66.79854 | 2024-10-07 05:18:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d187e3e-e02d-39f1-92f4-b4c255553e53 | -9.86268 | -67.2826 | 2024-10-07 05:18:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dce278d-8823-3dce-b5c6-edbbcccad038 | -9.86159 | -67.28412 | 2024-10-07 05:18:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5e8f50d-6be4-364c-a98a-d0915d6dd993 | -9.59381 | -66.75505 | 2024-10-07 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31033ccb-bf45-3f21-a87a-64f7abc2774e | -9.58916 | -66.7542 | 2024-10-07 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 361b26d0-a323-384a-a815-17c1ebc8a87b | -9.58829 | -66.75913 | 2024-10-07 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af1f3fdf-43a6-39d2-b705-ae5fdc251d88 | -9.49589 | -67.11127 | 2024-10-07 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 055d6ee7-6974-383f-a659-668818895e0b | -10.86133 | -68.24184 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9bce1420-fd52-3192-a6a9-3041560253df | -10.8296 | -68.35806 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e612b84-22ef-3af6-b52f-99295ae3931b | -10.82907 | -68.36095 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6e9a6a03-b12d-308e-adb4-e58d5c139115 | -10.82346 | -68.36291 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5471de4e-d8af-343e-93a3-459373dbd135 | -10.68079 | -68.86974 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52b250e4-1c23-341e-8e34-cb9ee3caca72 | -10.51483 | -67.88877 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daf4aed5-531f-3c02-81e4-8c81f32bb984 | -10.51472 | -67.89081 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9ebaf46-cd0e-39eb-ab8d-c4c8f30dc225 | -10.50094 | -67.8825 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012dd8d1-ba3c-3349-87bb-8bc2731414b9 | -10.50001 | -67.88599 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1852e0e-996c-3591-a144-21570c58a8cc | -10.49989 | -67.88805 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf0bd660-2316-33bc-b6f4-7996cbcf6a47 | -10.39203 | -67.88908 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e3cc0962-4ed8-3376-94d0-74e4031b8390 | -10.39168 | -67.88766 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78eec176-1398-3060-b093-2cbfcd46975d | -10.39066 | -67.89333 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e2ccedb8-42da-3c3e-9504-00520059ab61 | -10.3404 | -67.97211 | 2024-10-07 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6a43405a-2391-3a8e-913e-9b7fd94f181a | -10.8608 | -68.24476 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30a0b0ed-f260-3047-839d-5a5851933d92 | -10.86026 | -68.24769 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d32c7574-fff2-3136-b2b4-9dee9b2f585b | -10.83013 | -68.35517 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1392992-89a5-30aa-ace1-3ee340b592b6 | -10.82507 | -68.35416 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 630adb25-9d86-3941-9a36-9ded096a0d15 | -10.82454 | -68.35707 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 89767500-2c6c-34e4-ab58-55f307f2e25a | -10.824 | -68.35998 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9571f998-f535-3230-9884-08ec20de9b36 | -10.68018 | -68.87296 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6fb2cb5-c762-3709-a721-1d9927fadafc | -10.92241 | -68.24062 | 2024-10-07 05:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b73e1aae-eafd-3bb6-89e7-bb34060380a7 | -17.61326 | -46.94382 | 2024-10-07 05:18:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 243a4876-e9eb-3d75-a51a-aca03000c873 | -17.61258 | -46.95225 | 2024-10-07 05:18:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e077a52e-04db-3d03-b2ff-dd7947c076cd | -17.61158 | -46.9461 | 2024-10-07 05:18:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 197b295f-f53d-365b-8fd2-928d8e67df80 | -17.61084 | -46.95451 | 2024-10-07 05:18:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fbe2ed1e-b73b-393e-bb61-a5cf4361dd9c | -17.60527 | -46.95197 | 2024-10-07 05:18:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5db35333-8656-35a8-95e7-a38c0b26ae4b | -18.30808 | -47.1373 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd402eb3-584d-3b14-9a2f-5038fae5a59a | -18.30691 | -47.14059 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fe4ff3b-946e-344d-95a7-425b11470543 | -18.30077 | -47.13749 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4bf7147-e9d0-3213-a2bf-e321cf2cb0f3 | -18.30017 | -47.1452 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a8ef6e24-fb73-3f43-ac2a-46f1f08f3e69 | -18.29965 | -47.15195 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0a9ddd3a-573c-37e7-99f0-99e58282b7da | -18.29963 | -47.14024 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e587fa7-f5e7-38db-892a-61fd56447480 | -18.29903 | -47.14754 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f8dd0bc-b01e-3b67-b26e-f133c5c573f6 | -18.29848 | -47.15406 | 2024-10-07 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a1728d92-c411-3913-a7a8-9d10b4c9d682 | -17.64588 | -53.05585 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 01913a1a-120d-3df1-b5a2-1bc617d58102 | -17.14251 | -51.7137 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 286cf11a-cba8-36c1-9ade-7e02b47fc1d3 | -15.01365 | -52.0594 | 2024-10-07 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42caeb7c-2124-300e-b106-0157e68fa509 | -15.0085 | -52.0587 | 2024-10-07 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feb3de7e-f617-31de-8365-32e628eaaadf | -15.8766 | -52.30345 | 2024-10-07 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c68d3a5b-1530-3518-8da5-81735e695755 | -15.87145 | -52.30286 | 2024-10-07 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5172621-ff7b-3d42-9039-4b8a33c5a937 | -15.86628 | -52.30252 | 2024-10-07 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc7cf5a2-ec58-3227-b2d7-35f9cc99f6ca | -17.77803 | -53.76982 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05550e34-f463-38dd-b62f-4479a64c1d4c | -17.7774 | -53.77501 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cbd0683-4d35-3de4-85fa-9f328f168b54 | -17.77265 | -53.77427 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4c238d3-14eb-3523-ba55-67b36ab8f186 | -17.59879 | -52.51241 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7922d22-7732-314e-8201-e200121ebd52 | -17.66225 | -53.04548 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README113.md)
