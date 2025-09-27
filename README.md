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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da51b16d-4505-3e2c-b858-c9d282344142 | -22.5799 | -48.575 | 2025-09-27 00:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 165.3 |
| c9a9c761-ef53-3a03-89a0-e4d3cec94d44 | -5.475 | -43.0774 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 691.4 |
| bdb0d45c-fd8b-38cf-8e81-49ac4c062762 | 1.8688 | -50.8421 | 2025-09-27 00:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9c2f28a9-d926-3eef-8268-99bbb1fd79dd | -10.2223 | -50.2448 | 2025-09-27 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 51ceb5e9-45f1-36d9-918f-04958814bc26 | -11.3459 | -44.9904 | 2025-09-27 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d6647633-f735-3675-b120-215dc12ef7bc | -5.4748 | -43.1009 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2589855e-8b8e-3eb1-b034-6f21722ffa97 | -5.0676 | -44.8581 | 2025-09-27 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 767c3943-ee82-3a3e-a27d-a7ee193672b7 | -5.4935 | -43.0995 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 99b8c396-b8ff-3c6a-bff2-5c25aa9e88ce | -7.7192 | -47.296 | 2025-09-27 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4f4680f5-6370-31e0-bda0-73670bf93991 | -5.4562 | -43.0788 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 56537fd6-da53-39dd-936e-218cf2f6f16d | -11.3455 | -45.0135 | 2025-09-27 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 9733948f-23f5-3b04-a3a7-b5674964e17f | -5.0862 | -44.857 | 2025-09-27 00:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| efb24576-746f-32f4-83bd-9e96771a4378 | -5.5056 | -43.866 | 2025-09-27 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 888c9773-cd51-346b-908e-2e6978e181e4 | -10.2409 | -50.2643 | 2025-09-27 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 60786da0-2577-30b6-8f59-e2f2adcc65ce | -5.7961 | -42.8182 | 2025-09-27 00:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 869062fb-6b97-391d-a39f-6d2149e9a100 | -22.6077 | -49.0351 | 2025-09-27 00:00:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c80c4c02-d345-3bf2-989b-17def22329c5 | -5.5243 | -43.8647 | 2025-09-27 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3139aac7-9cc7-33cf-89cf-bea4f1e36d75 | -4.0107 | -46.9712 | 2025-09-27 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 96194a59-918c-3848-b00f-9571c09bc361 | 1.8872 | -50.8417 | 2025-09-27 00:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 781ed196-7f45-39fb-9882-9c9837155f74 | -10.2412 | -50.2429 | 2025-09-27 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 77e712a6-c760-3908-b3f5-9a23bb422f9d | -7.1383 | -45.5174 | 2025-09-27 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| ebf65458-c0ae-3a80-b489-8122216b7bc7 | -5.4752 | -43.054 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 278.6 |
| 87e766df-ba7f-375f-820e-17cf11de1846 | -10.222 | -50.2662 | 2025-09-27 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 91849cd9-12ec-3a8d-aef8-11ded5e36513 | -15.5871 | -42.3997 | 2025-09-27 00:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f94cb13b-47c2-3ed6-ae55-991ba19334ad | -5.4565 | -43.0554 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 3630f3c5-0f5a-3691-b0c0-b904df4d11fb | -5.4937 | -43.0761 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 296.3 |
| e0cbf15f-85df-3f38-ada0-3a44d35132ed | -12.2636 | -44.0599 | 2025-09-27 00:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d8971161-6a49-349c-ac93-4b5ace89a046 | -5.494 | -43.0526 | 2025-09-27 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ab7ab789-63e0-3154-9213-abf15532b798 | -11.365 | -44.9876 | 2025-09-27 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 124cbfef-6ed1-31f2-b1a0-2cfbaf0630ae | -22.5792 | -48.5986 | 2025-09-27 00:00:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| c50f1241-f3d7-329e-a533-eaf390d6d8eb | -11.3646 | -45.0108 | 2025-09-27 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 42f32144-547d-35a1-af1e-16bdba3ce8ba | -22.58903 | -48.57419 | 2025-09-27 00:09:00 | TERRA_M-M | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| 21139a8d-d93f-3fbb-b14e-1b412cf9cb2c | -22.57504 | -48.57592 | 2025-09-27 00:09:00 | TERRA_M-M | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 206.4 |
| f8eebebc-1c7d-3087-af16-f0a2723d18aa | -22.59144 | -48.60043 | 2025-09-27 00:09:00 | TERRA_M-M | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 36925ce2-a374-3c90-a148-bd410dede324 | -19.05943 | -48.14782 | 2025-09-27 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| ad4f09e9-3b4b-3f8e-b5d8-7bf388d3e383 | -22.60138 | -49.03453 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 996e3b35-b141-38dc-9df6-3441340e1fe4 | -17.11049 | -46.8635 | 2025-09-27 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6b4093d5-bceb-366c-83d3-5ce42c64588c | -20.18626 | -43.31417 | 2025-09-27 00:09:00 | TERRA_M-M | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| bb359726-5f11-3171-87ac-3d27689dffd3 | -19.63606 | -45.5764 | 2025-09-27 00:09:00 | TERRA_M-M | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2e0c1628-2c45-3116-a612-5b8fc832b32a | -22.58492 | -49.04346 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a3568a1a-5947-3d70-9c00-85c371c755aa | -22.5774 | -48.60196 | 2025-09-27 00:09:00 | TERRA_M-M | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 171.7 |
| 2a08c61b-e984-3d8b-b7ad-e18c1595f2a8 | -22.84547 | -49.7902 | 2025-09-27 00:09:00 | TERRA_M-M | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.3 |
| 5279054c-2eb3-3bce-a203-427b29484793 | -22.59942 | -49.04179 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 1796bc14-0289-36ca-99e4-eb75d8c066a5 | -20.18493 | -43.30371 | 2025-09-27 00:09:00 | TERRA_M-M | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 484c3282-c00e-39a9-8878-e24bdf955be6 | -19.0573 | -48.12687 | 2025-09-27 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b24f882a-f1b8-3883-8524-e7b89dcacae4 | -22.60386 | -49.06308 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ae6a1b3f-5459-3c15-9c6a-a1a5faf8f37f | -22.5869 | -49.03632 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 1c34b03e-4915-3fdb-8306-f78fe9e3187a | -22.58935 | -49.06498 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 130.6 |
| d774a7db-584b-3fd9-bb7b-053c3977cff1 | -22.60206 | -49.06998 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 111295d5-e1eb-38b2-be64-56b1ef3da9d6 | -19.04531 | -48.13474 | 2025-09-27 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 2e96c566-70de-36ef-9a61-161da7ef2f3e | -19.05818 | -48.13324 | 2025-09-27 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 381120b9-f4f9-3489-b969-5b3dafb7049f | -20.43032 | -43.36801 | 2025-09-27 00:09:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 741f7fbc-473d-30db-b846-db9b520763e0 | -20.30663 | -46.665 | 2025-09-27 00:09:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 85d41a41-a93a-33d3-a5a3-1252628d1e6a | -20.32016 | -47.13288 | 2025-09-27 00:09:00 | TERRA_M-M | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 3cca019a-d5b7-3dc6-93c2-683faa37d8c1 | -22.58757 | -49.07206 | 2025-09-27 00:09:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 37dd4140-0984-395b-a029-36b89d4324b1 | -15.0267 | -47.1307 | 2025-09-27 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 649b10df-8531-381c-8402-3565b096e730 | -10.2412 | -50.2429 | 2025-09-27 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 55165cb7-c7c8-315e-95eb-d5559c158999 | -22.5867 | -49.0402 | 2025-09-27 00:10:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 69059b5a-adc0-36ff-9852-a069ea2e99d5 | -5.4562 | -43.0788 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 24169a10-b54f-3c04-a3da-12525f2d74c7 | -5.5243 | -43.8647 | 2025-09-27 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 64c16f87-96a0-3e86-aa89-c3f847a0d94d | -4.0107 | -46.9712 | 2025-09-27 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 44a16fd4-1af2-3dfb-8877-d8f6ef8263a8 | -5.0676 | -44.8581 | 2025-09-27 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fd34296a-e9e8-3793-8005-a503434d4f06 | -10.222 | -50.2662 | 2025-09-27 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| e253c78c-3ad5-356f-9738-9cd4ec150c4b | -5.4748 | -43.1009 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| c6f303bc-c720-30ef-82c0-f2f7ea426688 | -3.4313 | -44.1247 | 2025-09-27 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 694108dd-e794-3794-83ac-20819bfbd83d | -12.2829 | -44.0568 | 2025-09-27 00:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 7f906534-9501-3f9b-a6ce-f62c98a8db46 | -5.7961 | -42.8182 | 2025-09-27 00:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 68184833-5b1e-3968-932e-eb1a6363517e | -5.4935 | -43.0995 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 42efe8ca-bde6-3ee1-be74-c2c818d317a2 | -5.475 | -43.0774 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 362.0 |
| 357c95ea-80eb-3e3e-8302-0d4caa462a4e | -11.3646 | -45.0108 | 2025-09-27 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| eb5f0b59-31ca-32ad-ae4e-3b0c3a5216a1 | -12.2632 | -44.0834 | 2025-09-27 00:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b2427d61-e317-320e-a0d5-bd1dfaa184c8 | -5.4752 | -43.054 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 7cc574e8-f6c7-341d-8b61-af5c01571f60 | -3.45 | -44.1238 | 2025-09-27 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 622635e0-435e-3b89-b885-bd86cef032e6 | -5.4937 | -43.0761 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 264.0 |
| e688e368-09e2-37f6-a0cc-e49beb9fa3c3 | -5.5056 | -43.866 | 2025-09-27 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 0b983040-a32e-389a-9fd8-fb401cca9425 | -15.0262 | -47.1536 | 2025-09-27 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 95d82e78-1ca4-3bce-9596-c20d80dfdb2b | -12.2641 | -44.0363 | 2025-09-27 00:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6bd90896-fe4d-3b76-93b6-4692b48d5128 | -15.0457 | -47.1502 | 2025-09-27 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f5ef9273-16ce-3b7c-a436-6b3935eb52c9 | -11.3455 | -45.0135 | 2025-09-27 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6f88ec14-6612-367d-b016-99bfa2b1df2a | -22.6077 | -49.0351 | 2025-09-27 00:10:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 101.9 |
| cab8ea32-45fa-3fb2-b7ed-07ec8fc22aec | -8.822 | -46.2564 | 2025-09-27 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3e7670bf-0421-3e2f-8bed-b812d7037efd | -10.2223 | -50.2448 | 2025-09-27 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 38b1d1b4-a924-360b-9d5f-63871f8ce3a6 | -5.4565 | -43.0554 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 8b3f3881-99c4-349b-91a8-629e8e7764c9 | -5.0862 | -44.857 | 2025-09-27 00:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 7b812e01-b9be-32fd-93c9-cc7efde89a9a | -15.0462 | -47.1274 | 2025-09-27 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2646d3e1-6e4c-30a3-b35e-a63bf3d6cf12 | -10.2409 | -50.2643 | 2025-09-27 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 210d5aef-c80e-310b-b001-c0e2e1fed5ee | -12.2636 | -44.0599 | 2025-09-27 00:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 266.7 |
| ac8e7153-6956-3c50-8d53-dcc3829bd4ba | -11.365 | -44.9876 | 2025-09-27 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| dbdb52af-c688-34c8-9849-f9064ee839d2 | -5.494 | -43.0526 | 2025-09-27 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 865350a4-66d8-35fa-accd-718af1bd8349 | -8.66412 | -43.99397 | 2025-09-27 00:11:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e048ae3d-6151-3fd8-a8e7-818478f0c113 | -9.29836 | -49.00801 | 2025-09-27 00:11:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 652246b8-c0ac-38af-9901-8b73c757b54e | -11.6552 | -45.34633 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8722634e-5c49-3fe2-8606-e69f280d7ca6 | -14.05384 | -47.03381 | 2025-09-27 00:11:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0e732edd-8047-3d68-920a-00d11b18a76a | -9.2738 | -46.56599 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 42c0565d-782f-3b25-af35-3fb99d65e611 | -10.23904 | -50.24996 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 21e1459f-8c03-34ad-a499-6c11252d07ba | -8.84407 | -46.23808 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 09426573-1426-307c-8705-9ca05da775a3 | -9.98152 | -43.58745 | 2025-09-27 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d236fc7d-5391-3394-b0ec-af92447ab41c | -9.75072 | -46.1415 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c18178e0-39ac-3c19-8254-01f5f819709a | -11.97249 | -46.60378 | 2025-09-27 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7bceef6c-a03e-343b-b688-6d062a28450b | -15.26823 | -51.48689 | 2025-09-27 00:11:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |


[Clique aqui para ver as próximas entradas](README2.md)
