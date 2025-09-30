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
| b5a2063f-96b3-328c-b6fc-4439a5244b8f | -20.99476 | -47.02013 | 2025-09-30 00:28:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52e642b9-d801-38b0-94f8-197e0120d216 | -20.04887 | -41.32473 | 2025-09-30 00:28:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| 5dc29360-5563-381d-80ea-b207a116203d | -22.51078 | -44.60435 | 2025-09-30 00:28:00 | TERRA_M-M | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 9867f826-629c-3608-ba61-6066a14fa845 | -19.85257 | -43.80668 | 2025-09-30 00:28:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| a162d6ce-d103-336b-95e5-adf382d4b795 | -21.46832 | -46.70455 | 2025-09-30 00:28:00 | TERRA_M-M | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8b00f466-fe33-3583-8fd8-f062e96f8e74 | -20.63132 | -46.17559 | 2025-09-30 00:28:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3bc03c04-6071-3580-b898-330df59205a5 | -19.32833 | -43.81314 | 2025-09-30 00:28:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 87eb1307-f30c-3c6c-8426-508806df3d98 | -22.51972 | -44.60294 | 2025-09-30 00:28:00 | TERRA_M-M | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| b5ad7673-ecce-3f3c-a01e-fc11a2c31f8d | -20.68874 | -43.11872 | 2025-09-30 00:28:00 | TERRA_M-M | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| bb23d382-55f8-32ad-bd9d-5ba5807bb662 | -4.354 | -45.5773 | 2025-09-30 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 1e822074-7c04-3973-b782-609329956580 | -21.6839 | -48.0698 | 2025-09-30 00:30:00 | GOES-19 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5719fab9-2663-3c13-9342-527ed24d69e6 | -10.2041 | -44.8915 | 2025-09-30 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 060c11eb-1564-3dcd-9c01-8cb47d5606a3 | -11.7524 | -44.7228 | 2025-09-30 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 35fcb8c9-1f88-3196-bf2d-73f82d03f8b8 | -11.8868 | -48.0323 | 2025-09-30 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| cd7825c4-fb9e-3b26-8134-d96fa75ba2c8 | -12.8643 | -46.8904 | 2025-09-30 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 05f49ed1-a935-3b97-9c59-521f0903b06d | -21.0564 | -45.6881 | 2025-09-30 00:30:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d3389c8e-1bf4-3019-9fca-5756ee789775 | -14.5522 | -48.4684 | 2025-09-30 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ffc938aa-6086-323a-bcbd-3540fc003a86 | -11.2138 | -47.2086 | 2025-09-30 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 05ece30e-16e0-3541-8d79-d8805bfaea32 | -14.7171 | -45.2291 | 2025-09-30 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e616127d-84ef-3202-a981-2e55f34c8729 | -11.1548 | -54.1054 | 2025-09-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| f9476bc7-c9a3-3175-8ac6-0f10b4d8bc94 | -14.6942 | -48.1557 | 2025-09-30 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 35e43b25-c13d-36fa-ad61-a8b978b4606c | -11.1735 | -54.1242 | 2025-09-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0709dddc-98df-3eb2-ab07-e999bc983dbd | -11.7712 | -44.7432 | 2025-09-30 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3f91a1d5-51f1-3606-aa9a-3e5db2bb9b97 | -4.3538 | -45.5997 | 2025-09-30 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 666f847b-b885-37db-b010-7c3266659d0c | -12.8433 | -46.9837 | 2025-09-30 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 172acf9c-a2ed-3765-823e-05b5ab2f6c74 | -12.8429 | -47.0063 | 2025-09-30 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 443c51ab-5524-381a-ab72-fe8a2b519c8e | -10.1851 | -44.8939 | 2025-09-30 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 355.1 |
| 7e8da7cc-f82f-3901-ad1f-c46fda0dad40 | -5.5241 | -43.8878 | 2025-09-30 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ebfaa6c7-80c4-3cb1-9682-59148ee4bca5 | -10.2045 | -44.8684 | 2025-09-30 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| eb461ec4-a8ed-30bd-8318-7e2eaa0a1d57 | -13.0139 | -44.1243 | 2025-09-30 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| cf7b777e-8bc0-3380-b7e8-4a594108e281 | -11.1546 | -54.126 | 2025-09-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 205.0 |
| b06454e1-ba8b-37c0-83e2-3982a4d4b742 | -3.1013 | -47.0082 | 2025-09-30 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f2753451-da0a-333f-9fe3-044c411d3ecf | -14.7137 | -48.1525 | 2025-09-30 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 9d01d757-96e0-380b-867e-9b923a2d77b9 | -5.214 | -45.2341 | 2025-09-30 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 04a0cee1-f15b-32f3-9382-790d6e565457 | -13.0144 | -44.1006 | 2025-09-30 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b7673247-0875-3f0c-b052-516ad18179e9 | -14.7367 | -45.2255 | 2025-09-30 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| fe2fbe6f-c83b-33fb-907c-34e6e91def3b | -20.0491 | -41.3251 | 2025-09-30 00:30:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.7 |
| e08cf41d-6e97-3605-9f38-88d50d36eb5c | -11.7519 | -44.7461 | 2025-09-30 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0f7a30d0-4c63-30c5-bf4f-f6c02e05aac8 | -11.1737 | -54.1037 | 2025-09-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ed579140-0b70-3ce8-9545-c085a9b7c0eb | -5.5243 | -43.8647 | 2025-09-30 00:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e9b32747-9d4c-3b06-9fb9-2528763a22de | -21.0572 | -45.6638 | 2025-09-30 00:30:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3c58d99f-9217-338b-a340-448ea7260f88 | -10.1855 | -44.8709 | 2025-09-30 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 24cacbfa-c0bc-3d2f-bbb0-3200aa1ff095 | -4.3353 | -45.5782 | 2025-09-30 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 4523f8ea-7ef1-359c-8ea5-c1013856511e | -1.2928 | -54.1784 | 2025-09-30 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ba4debb1-9c35-334b-a5bf-e3c6054dc77f | -11.071 | -47.8262 | 2025-09-30 00:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2a3d5b2b-ad0c-3714-adba-bd5064a3e3bf | -11.0714 | -47.804 | 2025-09-30 00:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| c2233a09-4ffc-314a-94f6-ddf1be4db2dd | -12.8638 | -46.913 | 2025-09-30 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 29475d2b-bfe0-3a81-b951-3538b8ec4bc2 | -18.47588 | -44.02209 | 2025-09-30 00:30:00 | TERRA_M-M | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 32.3 |
| cc96f65b-e5d7-382a-84d3-cf97a57175f4 | -17.45822 | -46.21067 | 2025-09-30 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e0759594-3114-3832-87eb-6c423e7cec3e | -15.52743 | -39.89052 | 2025-09-30 00:30:00 | TERRA_M-M | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| f83dce4b-c3a9-3a5a-b9c5-c3db21f76653 | -17.09746 | -48.56781 | 2025-09-30 00:30:00 | TERRA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 15736537-6f4b-37c6-aa12-66b1576c412f | -17.71438 | -46.65825 | 2025-09-30 00:30:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f818ff24-5255-3a47-ba95-5db138816c1e | -17.46576 | -46.20001 | 2025-09-30 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 68c2a728-94d9-3bd7-b96f-b8e087c4b286 | -15.92503 | -48.12593 | 2025-09-30 00:30:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3657380d-4be1-38f3-bb49-88f993793658 | -17.46707 | -46.20928 | 2025-09-30 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8665ae25-4cbf-3352-8023-c2d6afc70c2a | -18.4774 | -44.03209 | 2025-09-30 00:30:00 | TERRA_M-M | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c945d4ea-f27d-3792-941c-e5a22982d3cf | -18.46634 | -40.56701 | 2025-09-30 00:30:00 | TERRA_M-M | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| cd4d56cd-a273-33a0-bd38-77cbc3de74de | -15.53174 | -44.34339 | 2025-09-30 00:30:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c9e5e6d8-80fd-3a7e-8a0b-e2d87813049c | -17.87183 | -49.3943 | 2025-09-30 00:30:00 | TERRA_M-M | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c4175770-e2ff-3fbc-846e-4a946023230f | -18.59809 | -42.75583 | 2025-09-30 00:30:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| d721860c-f024-3e1f-b184-dfd82b21bf98 | -15.41865 | -44.20756 | 2025-09-30 00:30:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b3a9a7e9-be26-3a4f-b912-f75c377b66b3 | -15.91372 | -46.24421 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ad9dbb5c-4ec4-379a-b93c-1aa09f2b5422 | -18.12572 | -42.19244 | 2025-09-30 00:30:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 62f5d456-0121-342b-baf8-9f2cd20d46bb | -16.36931 | -49.12901 | 2025-09-30 00:30:00 | TERRA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 93cfb3c7-fcec-3ece-86ee-0d0e31dcd776 | -15.55108 | -44.34018 | 2025-09-30 00:30:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 07570c9e-7eab-331d-bda2-d96c73d9c5a8 | -17.79729 | -50.11918 | 2025-09-30 00:30:00 | TERRA_M-M | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f0fb387f-111d-3c1d-81f0-5f23f9f0b985 | -15.8547 | -46.22133 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 16535d9f-2be8-3c21-9700-44301c9e7314 | -19.11956 | -44.75338 | 2025-09-30 00:30:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b5e3a414-6c89-3cec-b1d2-6a908353aede | -17.17459 | -42.83097 | 2025-09-30 00:30:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| e1b0f948-a1b6-35c5-8cd6-7b2452a1afc7 | -15.41692 | -44.19627 | 2025-09-30 00:30:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| d14f77b2-cc9a-3d2b-b4ef-ef8554cd1d5b | -18.12656 | -47.79477 | 2025-09-30 00:30:00 | TERRA_M-M | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a29f6350-36fa-3535-8cac-39068c3a7cba | -15.85735 | -46.2401 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 02100403-8ae2-32c2-9e4d-535c1a639a66 | -16.75389 | -51.34937 | 2025-09-30 00:30:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4db3fd2a-6333-30e2-b1f2-8b65c4b81279 | -16.5282 | -49.42965 | 2025-09-30 00:30:00 | TERRA_M-M | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| aa890b83-e5f4-3f09-833e-c462328e6802 | -18.59603 | -42.74306 | 2025-09-30 00:30:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| e178214f-9240-3c3d-8013-6b6897066984 | -17.33703 | -44.00931 | 2025-09-30 00:30:00 | TERRA_M-M | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7e8b06ae-eae1-3788-bc03-6d33c84cb76d | -18.1253 | -47.78525 | 2025-09-30 00:30:00 | TERRA_M-M | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 70e7f412-baa2-3c0e-8db6-48633fbc5b23 | -17.47461 | -46.19862 | 2025-09-30 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0a380a20-85d1-36a5-8365-f914b7d22cfc | -18.11503 | -42.19448 | 2025-09-30 00:30:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f6a6f7f3-cfba-317f-9082-fa4b08138bad | -17.47592 | -46.20789 | 2025-09-30 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 179eff94-49e5-36bc-86fb-44852d43f4d4 | -15.93396 | -48.12466 | 2025-09-30 00:30:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e29116db-38ac-3857-9b68-a890a156fe40 | -15.88304 | -46.22042 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a51c42e8-82c7-3405-866c-e96ff3dc267b | -17.45691 | -46.2014 | 2025-09-30 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 40a9641a-56ee-38ee-abca-5d1fa05bbd98 | -16.73568 | -43.1109 | 2025-09-30 00:30:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d8346c84-f60d-3c83-9b7e-f8f10e19e937 | -15.88169 | -46.21104 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fe724592-efe5-358b-a095-e2a7f9894981 | -15.7771 | -43.67297 | 2025-09-30 00:30:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| f8c393fa-f4f2-3507-a179-0855d7a3ee4e | -17.41395 | -47.1516 | 2025-09-30 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| cd7a00ec-7043-3c6c-81ed-75c7d40e1841 | -17.7131 | -46.64904 | 2025-09-30 00:30:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9227d994-034d-38a2-8972-25bcbb8ee883 | -15.87724 | -46.82933 | 2025-09-30 00:30:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2398b7b1-07ce-396e-81ae-164eae23fb47 | -15.88605 | -46.82795 | 2025-09-30 00:30:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 104965e1-660b-3f35-9eb5-8cd55b95d8a3 | -17.04094 | -43.42147 | 2025-09-30 00:30:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 77c1f96e-1950-35a5-b763-7995bbebca84 | -17.03914 | -43.41005 | 2025-09-30 00:30:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fe67f5bc-34a1-34e1-a488-6a9523f93d05 | -15.92619 | -46.20395 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f99e43d5-589f-3d14-9ac5-0ee6843933a6 | -17.24044 | -44.11081 | 2025-09-30 00:30:00 | TERRA_M-M | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 55c746f6-2587-3b64-8824-783695adbd80 | -16.2837 | -47.84351 | 2025-09-30 00:30:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 88a5fb56-cdd6-30c4-9dfb-f6e91b471859 | -17.17666 | -42.84413 | 2025-09-30 00:30:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d39bf342-7974-3190-9140-1097891590d5 | -16.41987 | -47.96922 | 2025-09-30 00:30:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 46be42fb-bbaa-31ef-909e-8554c493cc93 | -15.93522 | -48.13403 | 2025-09-30 00:30:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2cbee89f-b3dc-31ac-b82e-8434ad99e4bf | -15.68655 | -46.26331 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6d55de4-cfb1-33fc-8555-958d408eb8dd | -15.92629 | -48.1353 | 2025-09-30 00:30:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 33.5 |


[Clique aqui para ver as próximas entradas](README4.md)
