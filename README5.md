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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d930b1fa-ff89-30ab-b9c1-0eddbce54bf7 | -3.20353 | -39.58826 | 2025-11-22 03:55:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5beaa68-534c-3124-abca-f76e7187651a | -2.58809 | -45.22148 | 2025-11-22 03:55:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ab482c4-b198-3db6-a88e-07110330e218 | -9.96513 | -36.04792 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 30199bc0-43a7-39cf-a64f-525600df0528 | -2.53773 | -45.53813 | 2025-11-22 03:55:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b0b1d9e-63f2-304d-81e2-4d8c8a0a9dc4 | -8.23541 | -39.97828 | 2025-11-22 03:55:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 38616b83-15ee-3275-a200-b289da6e2b5a | -2.89483 | -40.24717 | 2025-11-22 03:55:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd9170ae-5ba0-36ee-97c7-ab7577a29319 | -9.97171 | -36.05327 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 09e280c4-d402-382c-926b-1beac03c2979 | -9.96811 | -36.0527 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 21bc5c7b-c30b-34ef-b08f-35057194a5cc | -3.20695 | -39.58879 | 2025-11-22 03:55:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2e63cf01-d2f7-3fbf-ac99-3a6cea14695d | -9.97233 | -36.04908 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| f0854ee4-2416-38bd-ae20-1e657d0ac73c | -8.20805 | -35.25306 | 2025-11-22 03:55:00 | NOAA-20 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25e9831a-274f-3537-8b48-96e7b18f1781 | -2.45207 | -45.38174 | 2025-11-22 03:55:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad8779ed-4b1f-3dd6-b131-6dc13677984f | -2.45299 | -45.37627 | 2025-11-22 03:55:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286e5f31-2bba-3490-8795-b34ef92099da | -2.88859 | -40.4914 | 2025-11-22 03:55:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f8d05320-8f04-357f-84db-840dae41b8b7 | -10.02488 | -37.32476 | 2025-11-22 03:55:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b15776a2-9543-3e45-aa3c-d11bca450c32 | -8.8304 | -35.2575 | 2025-11-22 03:55:00 | NOAA-20 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19662af2-5745-3a4b-ab85-6158bfd2103c | -8.23876 | -39.97881 | 2025-11-22 03:55:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8d98a61-ad0f-3730-b060-77193ba033a0 | -8.05339 | -37.55831 | 2025-11-22 03:55:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a602e01-9fbc-39a5-9aa2-e81adc0b3686 | -3.02653 | -41.12882 | 2025-11-22 03:55:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b51bd0cf-9e2c-3306-bbc6-eaff7c5d8df3 | -18.75955 | -45.28461 | 2025-11-22 03:57:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c82dcdc-ec73-3a30-bf3f-d9cd8ec2726a | -20.60159 | -45.50245 | 2025-11-22 03:57:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dad7a9e-34d5-3c99-9ba5-5e7cef35ac82 | -20.11899 | -41.74446 | 2025-11-22 03:57:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 32e11491-9c5a-3014-9d45-537a0515d21b | -17.38316 | -42.63332 | 2025-11-22 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f95de279-7e98-340a-b5f6-78bc5231aac6 | -17.06955 | -46.59942 | 2025-11-22 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b646a4ca-9d54-3b7d-9779-60c03249d6b9 | -18.27459 | -43.07814 | 2025-11-22 03:57:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27f6442f-2f17-38e8-9d78-52dd10a23936 | -20.39162 | -46.47038 | 2025-11-22 03:57:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb2c639f-df0f-307a-8006-4b0ba7b1754c | -17.1695 | -47.23446 | 2025-11-22 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77170d31-1bc2-3dec-bb99-917d4d3820e6 | -22.2588 | -42.00241 | 2025-11-22 03:57:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e6e10b16-0a1c-385e-bd19-36c39507f969 | -21.30871 | -48.56022 | 2025-11-22 03:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53650999-218c-3ef9-9fb7-7fdf084f5333 | -21.30833 | -41.89253 | 2025-11-22 03:57:00 | NOAA-20 | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 14f6c9fc-8dea-3fe3-ba63-325f9645a211 | -21.37877 | -41.13548 | 2025-11-22 03:57:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4c6f219a-6182-3fd9-904b-032166935565 | -16.46506 | -46.42601 | 2025-11-22 03:57:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dc09c32-8999-343d-a12b-2b76eb65062a | -20.59907 | -46.35176 | 2025-11-22 03:57:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b133c34-84ef-3335-be10-89ddb7703759 | -17.07368 | -46.60027 | 2025-11-22 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9b29b91-df7c-3ac0-b462-3d2d0cef216c | -20.11568 | -41.74387 | 2025-11-22 03:57:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9861733e-2955-32fb-8685-abe96d122895 | -21.16144 | -48.63631 | 2025-11-22 03:57:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f8c341c1-5c5a-3baf-bee6-9cf04e277638 | -19.31828 | -46.30996 | 2025-11-22 03:57:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 547bb628-208e-3b6d-bec4-b2629e540b52 | -19.64516 | -42.17797 | 2025-11-22 03:57:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c56c78c8-bd37-3819-9521-f4997c152699 | -21.07061 | -43.33294 | 2025-11-22 03:57:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| ce5c469a-95dd-353b-94b5-f4671775e8f2 | -21.81069 | -45.88799 | 2025-11-22 03:57:00 | NOAA-20 | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3775e516-10d0-3bd1-9ff3-cc653e744020 | -18.05409 | -39.59335 | 2025-11-22 03:57:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 98ec686b-f6c6-3006-bdec-8c18e1283880 | -20.81917 | -45.10571 | 2025-11-22 03:57:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f9b6105f-45bf-3030-8f3a-7974a6be4e6c | -20.26655 | -40.39717 | 2025-11-22 03:57:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de4733f4-5e4b-3f94-ad9c-7be08281399c | -21.3053 | -48.55468 | 2025-11-22 03:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cecf1d6-8502-3b0f-858e-504ec4670cd0 | -20.2493 | -49.33973 | 2025-11-22 03:57:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a6e7d9ed-3796-3312-a7fb-39e3008e7d00 | -17.07441 | -46.59635 | 2025-11-22 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bb13b87-5a54-3b67-990d-6874b5b7443c | -20.62732 | -47.44039 | 2025-11-22 03:57:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c5342661-74f3-333f-970d-3ecf019740bb | -20.65808 | -43.44433 | 2025-11-22 03:57:00 | NOAA-20 | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6290bd86-e127-3191-b9ef-caee9834b6e6 | -20.62396 | -47.4356 | 2025-11-22 03:57:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8740802e-32b5-31e6-8c26-866d53ace37d | -18.96916 | -42.36257 | 2025-11-22 03:57:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69afeb33-e481-3067-bc80-a7adf052c500 | -18.7604 | -45.27994 | 2025-11-22 03:57:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7cc897d-ba2d-3828-97d8-1f5fcf03ab48 | -16.46692 | -46.42551 | 2025-11-22 03:57:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44c01fd1-ab69-3e06-8a4e-4276ff94c036 | -19.50069 | -42.08506 | 2025-11-22 03:57:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9646d385-6089-3dd9-82da-1aafea22e847 | -18.97765 | -42.35268 | 2025-11-22 03:57:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 50e24192-16fc-3076-91fc-57a97e71eb89 | -19.62723 | -41.84706 | 2025-11-22 03:57:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 15e96750-6a22-3769-b6c5-6b2aad3e6b70 | -20.94029 | -42.82672 | 2025-11-22 03:57:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ed03b2db-0a14-3c6d-8c84-45024e9ae049 | -20.59819 | -46.35656 | 2025-11-22 03:57:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 687fb28d-af82-3b84-84ff-8a83675980f0 | -20.62655 | -47.44447 | 2025-11-22 03:57:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0a123672-f047-3ff1-8466-5584b4629f00 | -19.85129 | -46.30935 | 2025-11-22 03:57:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acefe469-6d76-39c4-b057-d557be470b17 | -21.36963 | -47.83384 | 2025-11-22 03:57:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61ec72a4-0321-3b34-809d-660377b4c89b | -19.89967 | -40.57908 | 2025-11-22 03:57:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ab53bed2-f36b-33ec-a5eb-17814758c395 | -17.16871 | -47.23864 | 2025-11-22 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97ca1294-5853-3a9d-93d9-b18cd554fd61 | -20.39148 | -46.46958 | 2025-11-22 03:57:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 05cb031e-4ab0-3430-bbf0-b44f37b8831d | -21.16111 | -48.63782 | 2025-11-22 03:57:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f2ad77b9-f35d-3775-a836-45b579422e80 | -21.3044 | -48.55916 | 2025-11-22 03:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d3e3d1-7343-375d-aa10-a1b49c6964b4 | -18.1492 | -45.16901 | 2025-11-22 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38ffc2d7-08c9-352e-9fdf-b241c4f15d13 | -18.51086 | -41.94155 | 2025-11-22 03:57:00 | NOAA-20 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d15f24e0-a09d-390e-9e57-c8531f45a832 | -16.46436 | -46.4299 | 2025-11-22 03:57:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17cae969-2e5f-3a2e-9e8a-759e0cd5d744 | -22.24499 | -43.68105 | 2025-11-22 03:57:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 008766b8-799d-308c-8ea6-e06c9852aabe | -20.65469 | -43.44368 | 2025-11-22 03:57:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 422988d0-4d88-3387-bdad-b7fffbb6f749 | -19.86055 | -47.45735 | 2025-11-22 03:57:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b48327c5-afe8-3989-87d0-4ed3f46920dc | -18.05465 | -39.58957 | 2025-11-22 03:57:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f37c4b5-84b9-30ee-85f9-5b01d1ffd9a0 | -19.91363 | -42.32457 | 2025-11-22 03:57:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 64bf5402-4891-3ca4-b304-7863c191b5f2 | -20.24825 | -49.34502 | 2025-11-22 03:57:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 73d92c0f-2311-38a1-aff8-dfa915de5216 | -18.14652 | -46.73567 | 2025-11-22 03:57:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 812e3ca6-1e49-3a18-bbd0-d0ecbee0e022 | -19.62665 | -41.85072 | 2025-11-22 03:57:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6dacdf82-078e-3811-b428-519e4e6655c9 | -20.25149 | -49.34072 | 2025-11-22 03:57:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 248a5013-2719-3104-b443-a61fb54aff48 | -19.5001 | -42.08871 | 2025-11-22 03:57:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a3c0ded5-4af3-3060-9653-611508fbe980 | -20.00417 | -40.20702 | 2025-11-22 03:57:00 | NOAA-20 | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c54b9d4-9a49-37f0-82b7-0facfd05bf3a | -18.915 | -47.1763 | 2025-11-22 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8853a168-53e8-3b8a-91a6-bbf4abe089a9 | -20.62807 | -47.43635 | 2025-11-22 03:57:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 38664a35-d34d-3f2a-9885-e47bc4e41663 | -17.07027 | -46.5955 | 2025-11-22 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ec432ec-608e-309d-8a6d-cd6a601975df | -19.31758 | -46.31055 | 2025-11-22 03:57:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13d71d28-28be-3a26-84a4-282f5729bb2e | -24.37259 | -49.18665 | 2025-11-22 03:59:00 | NOAA-20 | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 747b1d04-9614-3c3e-80bf-fa71a81732c4 | -24.3683 | -49.18591 | 2025-11-22 03:59:00 | NOAA-20 | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ae4ab9cb-1ee3-3096-808d-0bbe71d0fce9 | -21.87597 | -46.44256 | 2025-11-22 03:59:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2834bc9c-3497-309a-8e0f-ff918501beeb | -22.56541 | -47.01828 | 2025-11-22 03:59:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aa92cc83-7629-3d94-af04-d1b0b99376de | -22.92042 | -48.68117 | 2025-11-22 03:59:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f85bb67f-e9f0-3568-976d-290dec18af92 | -22.24881 | -47.04761 | 2025-11-22 03:59:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cdc0819-ba02-3575-b719-105f7dac5071 | -20.88747 | -52.34544 | 2025-11-22 03:59:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa6c1f07-2b11-35ba-a082-7fe279cad5ef | -22.95752 | -48.69475 | 2025-11-22 03:59:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99566d03-f76b-3864-a226-a22350a7f135 | -22.03468 | -47.19425 | 2025-11-22 03:59:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7e5613c4-5920-3dc7-85dc-036042e9187b | -23.23563 | -51.28976 | 2025-11-22 03:59:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0f3fa639-a483-35fa-b625-ec72185cc364 | -22.11412 | -47.01047 | 2025-11-22 03:59:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3933738-f88f-3681-b85a-67a316a1b1fe | -20.88202 | -52.34381 | 2025-11-22 03:59:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f534052-552b-3739-8771-e2e4775512c1 | -20.8829 | -52.33983 | 2025-11-22 03:59:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aed2cbd0-949c-3b5e-8d69-97f7d89d9357 | -23.23705 | -51.28527 | 2025-11-22 03:59:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| fd33a0bd-553a-35bc-ae14-3a380276a5f8 | -23.23693 | -51.28366 | 2025-11-22 03:59:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9cffe34c-ba8b-3d72-b324-176678475306 | -20.88835 | -52.34145 | 2025-11-22 03:59:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f8bed8f-e5a9-39c0-95a7-adb0d9c4ed83 | -22.51604 | -44.32042 | 2025-11-22 03:59:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
