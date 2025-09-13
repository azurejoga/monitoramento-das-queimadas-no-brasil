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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b28a5d54-3766-3373-a29f-c2cacc96e5f8 | -16.86906 | -49.34067 | 2025-09-13 04:10:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 886e33cc-be76-38b1-869a-fb9eb16f1e02 | -15.51216 | -47.28979 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6666dee-4c35-35d2-adbf-4b5b2ca8bf6e | -21.06859 | -46.14075 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dac5c0d3-e8a6-3fa9-bd58-5bdac8b07ef6 | -19.98438 | -46.90807 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4699c6c1-6e19-31b7-b2f0-7074ef01869a | -16.40999 | -49.23929 | 2025-09-13 04:10:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26b4c542-45ef-36da-953c-1de1fc7a1458 | -16.50218 | -55.12255 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 1f91964f-99d8-3198-88e2-dbcccabccf00 | -21.61567 | -46.81775 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e208877f-5d4b-34e4-9277-824455b40c16 | -16.49375 | -55.14875 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f535c09-ad29-3de5-a144-93d100bce55a | -18.70872 | -51.78608 | 2025-09-13 04:10:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9340848-287a-3a93-87cc-1337afdd8120 | -15.84449 | -49.93889 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26920f1e-ae3a-3d42-b032-0d0861eed888 | -14.63615 | -52.10292 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a08dfb3d-570d-31cf-aec5-c2b00f331bfa | -17.14594 | -53.89394 | 2025-09-13 04:10:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e4ab6f9-0959-35ce-84ac-27e38be6e18c | -18.18134 | -45.21294 | 2025-09-13 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fe286cc-735c-3b51-ab8a-07c0d75d9e7d | -19.10648 | -43.17048 | 2025-09-13 04:10:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c931880-00f2-3ef4-b7dc-83a74ee977dd | -16.52692 | -51.74524 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0264f7b6-5ff0-303c-be36-884be88c2ef5 | -17.99641 | -46.9407 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40dd4820-739d-374c-afe4-406ec586693f | -17.95469 | -45.26841 | 2025-09-13 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6716c98c-44cb-3386-8a7d-8254363b476a | -18.14734 | -48.46069 | 2025-09-13 04:10:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3683d65-988f-36bf-b330-e609b4d2f85c | -16.50804 | -55.124 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e8aa6dfa-1b5c-3367-be75-52b44424c9b2 | -17.43921 | -49.24545 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 110598fa-f592-322e-a746-e640640b51bd | -22.18397 | -49.6111 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8d15e899-97ab-3a19-8c81-a2e66fedddde | -17.28578 | -46.10418 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1f672251-a3ea-34ba-8ea0-7aa883c7e79d | -16.32852 | -43.75823 | 2025-09-13 04:10:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624c361e-71a8-36a9-bafc-0e16ea6c4204 | -16.84731 | -40.86356 | 2025-09-13 04:10:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 0f4fd042-9dfb-3271-a106-4fe5b3c36987 | -18.79322 | -44.62042 | 2025-09-13 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bb5e053-d7ce-3ae0-8e55-161f02c4b10d | -20.44464 | -46.44715 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 671b63db-f2e4-3d73-b6b1-cb7c9e0fc615 | -16.14413 | -49.91831 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3a39c39-1f95-3041-9a39-300e555bfb96 | -21.61423 | -46.80559 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6e3604e7-feec-3043-a449-eefbb7807054 | -22.18645 | -49.61359 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 68f6d7d9-b41e-3052-b023-6342ee390c76 | -15.16207 | -52.40211 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb788bcc-2615-31e9-8b08-a64aeb21fc07 | -18.85619 | -46.83336 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1616ca9-c264-3b5e-b2f0-80d7bf9286fb | -17.92002 | -44.45211 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f61f0b2d-630d-3007-9e28-d27e683c3816 | -15.16487 | -52.49567 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 744a9ddf-80b9-3ae0-a380-dc73770422d0 | -20.444 | -46.45102 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92eca04e-0dfc-3c2f-84cc-64e81ad71d4e | -16.36913 | -51.53746 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76026781-b0cf-36d0-94fa-13978937662c | -15.60791 | -47.93457 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b5fc402-cf99-3b51-87be-2e7c60275162 | -16.01728 | -47.92667 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b23d20a3-1ae0-3fcd-b1f6-d52b4968d36d | -15.0212 | -50.14493 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61b6f098-4aa2-3dad-ac83-61dfb0ca5fa5 | -18.34856 | -47.0245 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aff6d924-2560-3422-9f9c-f37835effd8b | -17.29569 | -48.74282 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 617100aa-2475-3322-b032-b1a9621002dd | -15.76617 | -53.4921 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da79cb80-09d6-3095-855d-6753db40c96a | -16.40781 | -49.04732 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f5d6b6c-3955-3249-b07d-a2297cf9dd5b | -16.32942 | -51.54002 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2ffda609-367b-3fc5-b5f5-68ec77ba4081 | -19.32975 | -45.11143 | 2025-09-13 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 634c8799-581b-3feb-8caa-670f79a6d958 | -15.37627 | -52.10255 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 449d5251-6bf2-3b53-a3af-849bf93b1c00 | -15.19658 | -56.68427 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 378e7ba9-2ae4-3eb7-9012-d673ed4ece21 | -16.35458 | -51.51115 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd4cdf67-f84b-305e-af40-c3f243f4e93c | -15.2446 | -51.40005 | 2025-09-13 04:10:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17328999-449f-33db-8818-3e35713c6cb5 | -17.27463 | -47.24632 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f29ba05c-7390-3fb7-9518-f9136e2dadb0 | -15.0443 | -50.1681 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35ed937f-cfdf-37a1-9b64-f6b5fae90340 | -21.58579 | -48.41446 | 2025-09-13 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a62ee85-aa2c-3929-9ebb-f60342abf2c3 | -16.4987 | -55.13909 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 35e0db8b-c15c-37a3-b95e-7fad3fae9efa | -21.32097 | -44.99983 | 2025-09-13 04:10:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dfd62272-67a6-3c23-808d-cf40147840cc | -17.28823 | -47.25337 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7918ea3-c260-3e66-b668-b2cb3f1109c7 | -20.59353 | -45.11034 | 2025-09-13 04:10:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 976c537f-6c96-3fd3-99a1-c9b45da56be6 | -18.8572 | -46.83689 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f86869b-7b1d-3ff8-86e1-7521bba0c8b4 | -17.28299 | -46.09978 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5893d178-cc30-3035-ae21-380c20df3d47 | -17.09731 | -48.85576 | 2025-09-13 04:10:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 566879ea-5cc9-378c-b270-8b1800ab9b28 | -16.43584 | -49.05322 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c13e5e82-7ac5-3ccb-b4df-b134db1b0abc | -16.43903 | -45.68797 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90bb0d21-a47c-395e-b974-29c8805425cb | -17.41653 | -49.23359 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddac6f60-6432-3352-b9a8-e0546fe49a31 | -17.99995 | -46.94122 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 165ff19f-b3f8-37eb-8275-c781b9a6f0dd | -16.49365 | -55.13377 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2f4b4194-00e5-38fe-8084-e986390ca9cc | -16.49281 | -55.15307 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fbfe7ece-3736-31fd-81bd-6590cb39ff68 | -18.85271 | -46.83283 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1782b127-116e-3928-80fb-5cc6fb964d5c | -20.10308 | -46.9127 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f51e7f47-3c58-3f3c-8d7a-83c7a7ce4a13 | -16.08661 | -49.95068 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 00aa21da-bb4e-3d3c-9709-80fc36436470 | -15.15959 | -50.13295 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f0532fa-856c-3fda-b223-e6cc8e17a5cc | -16.49468 | -55.14448 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 07dc463a-178a-3468-8207-f0d1001181ba | -21.86913 | -46.50142 | 2025-09-13 04:10:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4f7a7dd5-b1da-300c-82a6-efb9d866211f | -17.14818 | -47.73104 | 2025-09-13 04:10:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c662861f-55d6-3059-8fa6-c62e31357a6a | -22.22508 | -48.60358 | 2025-09-13 04:10:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9b8e353a-0180-3f26-afcd-ed06f4f04fe8 | -17.4113 | -49.26222 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5db89739-2942-3472-be43-e19ab2348b28 | -16.64992 | -49.75488 | 2025-09-13 04:10:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 03256687-a905-3f37-9bb9-59afa1753efc | -17.41659 | -49.25599 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7540526e-41d5-3ea8-8e4f-22f43dd36d4d | -17.42115 | -49.23097 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5ec9d36-4831-3536-9d28-1c8cffb033ca | -18.14064 | -48.45456 | 2025-09-13 04:10:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d920c2f0-5265-3509-8516-e59e84ab1ee8 | -16.49236 | -55.12677 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 76daf741-5c55-3bfd-93d9-b21af5396ae4 | -16.33045 | -51.53469 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80191064-3ce8-3d5f-bbc2-e9848d24fb05 | -21.61551 | -46.79797 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f7d47197-4f0a-3a9b-bdcd-ca4581ba8ec3 | -21.61698 | -46.81 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 73e2eda4-2e11-334a-a540-6dd619ab85b6 | -16.56452 | -49.21986 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 54bd3432-a424-32f3-8ce6-0e8a5a28bec7 | -17.33187 | -46.665 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9958b536-e732-3da8-ab51-ce5297526d91 | -15.58488 | -54.752 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f960fd22-9141-3779-a351-4ea5a3e11cd0 | -19.0852 | -43.12865 | 2025-09-13 04:10:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 17ceff71-f1b2-3f58-9383-146fd8b570d7 | -15.77748 | -52.24731 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 979d1e03-711f-3845-b64d-f65fbc491058 | -19.7348 | -47.91133 | 2025-09-13 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2273441c-8d9a-3bf7-90ed-5d1918712407 | -15.81301 | -52.19729 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9484469f-8d21-3ed8-a95a-3587344c7c62 | -15.12008 | -52.50597 | 2025-09-13 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24fa09e1-8253-3b06-94f2-bce192720621 | -17.76636 | -42.16916 | 2025-09-13 04:10:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5889a13-5614-30a0-877c-3c364eb02a16 | -15.32312 | -52.90297 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae32c26c-91ca-3029-82c5-831b446ef251 | -18.61749 | -43.96759 | 2025-09-13 04:10:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e4338aa-ee3a-3c92-bee2-e4d0f89388db | -16.81605 | -42.21465 | 2025-09-13 04:10:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6073b913-1c49-39db-acb3-1fe515e8e7a8 | -19.25443 | -51.42685 | 2025-09-13 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec442d86-d5a6-3c15-8f3a-3b04da1b71d2 | -17.28104 | -47.25204 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7a7171d-d072-3284-86fb-10d474e7f421 | -16.50104 | -55.11532 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1efb8d39-8688-3941-b964-e31699611b93 | -15.54156 | -47.95361 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 26727286-ef8e-3f30-805f-37a19b9549d3 | -18.13598 | -48.45866 | 2025-09-13 04:10:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4fae0b4-5eba-3f76-ad0e-3d3db2291b9e | -15.07079 | -52.47709 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2f29771-40f3-35bd-970e-9e9f1e124b8f | -17.40495 | -48.21772 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README66.md)
