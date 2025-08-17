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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77f730c1-c535-32f6-bf65-b7ecc9db3908 | -12.6331 | -46.9245 | 2025-08-17 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1b93d7e4-7018-3e20-9cee-1edf248c21f1 | -5.6786 | -43.3659 | 2025-08-17 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e40eec67-5a19-33c6-a619-4ffdb1cce162 | -12.6143 | -46.9047 | 2025-08-17 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b10362a5-cd96-3324-9b81-b0bc415be41d | -14.1902 | -45.3008 | 2025-08-17 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 94bf1774-d95e-34a4-9e70-7276eca9de26 | -14.2046 | -42.0293 | 2025-08-17 13:30:00 | GOES-19 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| b4ba29e1-f1bc-386e-b194-eedbe9fbe361 | -14.1902 | -45.3008 | 2025-08-17 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8877ada3-73c2-324e-94e2-4c60c8091705 | -3.9633 | -42.517 | 2025-08-17 13:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 76c8f26d-ea9b-37ec-8153-ea1448039ea9 | -14.1897 | -45.3241 | 2025-08-17 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 9f58380e-2205-3046-8401-300d99735fae | -15.8602 | -50.204 | 2025-08-17 13:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ad1c1a33-ca0d-3909-98b3-9caa71f5661d | -6.4831 | -45.4591 | 2025-08-17 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e115d9a0-bb56-3fc8-94c5-318ef603f657 | -12.6335 | -46.9019 | 2025-08-17 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 1e5ec2e2-223f-37ea-bf58-a71dff7c9905 | -3.9632 | -42.5406 | 2025-08-17 13:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| e846e4f5-9869-3b21-82b2-a521c70cdf1b | -3.9819 | -42.5396 | 2025-08-17 13:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 158.0 |
| d9a527fc-8eb6-3b74-a8a6-1eecc9e776f3 | -13.8748 | -45.5411 | 2025-08-17 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e3e15a99-0f4d-3ad6-b3c3-2f3d911362db | -5.6784 | -43.3892 | 2025-08-17 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 4de82255-9c5d-3e6a-ab13-88d6f7b0a23f | -14.1702 | -45.3276 | 2025-08-17 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| c61eecde-ca26-3173-8c53-95bca4b817f4 | -12.6143 | -46.9047 | 2025-08-17 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| deebeaf4-7160-3a66-af0c-c74e18b93bed | -17.9137 | -44.4218 | 2025-08-17 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 63d8ff53-726d-3a03-8ef3-a37bbf16f506 | -7.5198 | -44.9836 | 2025-08-17 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2b3eec49-9973-302b-8847-b7f7f19f456c | -3.982 | -42.516 | 2025-08-17 13:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| 1760317c-4054-3bf2-a233-07d9c2aafa4f | -12.6143 | -46.9047 | 2025-08-17 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6b6330ef-185c-35a9-9109-88a7c532a8d4 | -14.2046 | -42.0293 | 2025-08-17 13:40:00 | GOES-19 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 38b01bee-2682-3e7e-b15a-2c12421b3ada | -5.6786 | -43.3659 | 2025-08-17 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b89cde1a-e5a9-3393-9ef9-e6d992f69d05 | -17.9137 | -44.4218 | 2025-08-17 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 2b784a51-e681-3b61-99e2-b209256e98ec | -5.6784 | -43.3892 | 2025-08-17 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 200.2 |
| e9a0c050-4010-379c-9852-07320e81fa3d | -12.6335 | -46.9019 | 2025-08-17 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 24403cc1-7e0e-3eba-b4e5-71029be2508e | -3.982 | -42.516 | 2025-08-17 13:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 176.2 |
| 25a37cec-69d8-3c68-b95c-8bbcc213c285 | -3.9819 | -42.5396 | 2025-08-17 13:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 214.1 |
| 44d82b8a-bc50-3265-ae62-9e42bc075bb0 | -14.1902 | -45.3008 | 2025-08-17 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 614438c5-e23c-3bcc-8782-5cdee689488f | -3.9632 | -42.5406 | 2025-08-17 13:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| cb0e4669-a6f8-371f-b8a7-c63d37b5971b | -14.1702 | -45.3276 | 2025-08-17 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| fa416043-eb5c-32b9-9659-dc0d69c5a0ba | -6.4831 | -45.4591 | 2025-08-17 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| ce3af8e8-e104-3d43-b985-4acfd5a708b6 | -6.5018 | -45.4576 | 2025-08-17 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0cfb6203-19de-3d1b-9a34-58e915f8740c | -14.9819 | -54.7536 | 2025-08-17 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b62a2ed9-f210-3654-b300-b046121b65f1 | -7.5198 | -44.9836 | 2025-08-17 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 590e6356-4eb1-36d3-b0f0-1eead431e72d | -12.6335 | -46.9019 | 2025-08-17 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 169f896b-de5e-3d26-8a1f-4db24d25e1a9 | -7.5198 | -44.9836 | 2025-08-17 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a45e87b7-0030-3aba-844d-0692f79e7dc1 | -14.2046 | -42.0293 | 2025-08-17 13:50:00 | GOES-19 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 147.6 |
| 13911052-b8a2-3763-9bcf-e9e79eadf6dd | -14.1897 | -45.3241 | 2025-08-17 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 2bbe9dee-e655-3477-a00c-59e8dd893344 | -7.1477 | -44.6524 | 2025-08-17 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f200f5b5-ebb5-34b3-b79b-c1bb8bf4b12c | -6.4831 | -45.4591 | 2025-08-17 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 9747a618-daa9-3a85-8b73-575432ccf981 | -7.944 | -63.2037 | 2025-08-17 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3a558490-ed0e-3c49-b32a-f092e9523365 | -15.774 | -47.7933 | 2025-08-17 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 3229e117-1f25-3bb6-b296-c18302796624 | -14.1902 | -45.3008 | 2025-08-17 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 2b03a607-2574-3846-a464-69c4ea698e5a | -12.6143 | -46.9047 | 2025-08-17 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e69cda44-26d5-3423-b588-0a73572bbaa8 | -3.9819 | -42.5396 | 2025-08-17 13:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 197.0 |
| 368e7f44-a237-367d-a62e-d2ac6c598dc9 | -14.1702 | -45.3276 | 2025-08-17 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d2a645f3-9c3b-31a7-8163-986fc6996a9a | -6.0791 | -44.6276 | 2025-08-17 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 72db8514-a23c-30d5-8481-c870b2ea6a96 | -17.9137 | -44.4218 | 2025-08-17 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a5ccf9e0-6367-349b-84de-0cdf00066542 | -5.6971 | -43.3878 | 2025-08-17 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 22a92f19-6ca8-391c-aaf8-bd8a270f2bab | -5.6784 | -43.3892 | 2025-08-17 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 198.0 |
| ce9ae6e6-e5f9-3cf8-a2c0-9ba56f8dc831 | -3.982 | -42.516 | 2025-08-17 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 156.5 |
| 806a9328-0088-3cdb-8cf4-a75cb54de75f | -6.5018 | -45.4576 | 2025-08-17 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f87da43f-0e34-3052-b77d-5bfeef92d7fb | -8.071 | -47.7045 | 2025-08-17 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3c49a91f-4d4f-3820-89d9-03388cb967c8 | -15.774 | -47.7933 | 2025-08-17 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3437b6db-36e1-38df-8166-9755d4463ba2 | -14.1702 | -45.3276 | 2025-08-17 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 8a62f394-4eb1-3048-85b2-5dbf05d81aa3 | -6.5018 | -45.4576 | 2025-08-17 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 3d9660d5-58ab-38bc-833c-1135dac01029 | -5.6784 | -43.3892 | 2025-08-17 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 196.4 |
| e4bdb71c-a4b2-37ac-9e64-0aedede9c2e5 | -6.4831 | -45.4591 | 2025-08-17 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 687bd000-b216-3844-bb87-b80140c72cda | -12.6335 | -46.9019 | 2025-08-17 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 3133405b-69fd-3e0c-99b4-d11822caf3ce | -12.6143 | -46.9047 | 2025-08-17 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| fcbe94db-c158-34c6-bef0-036a545d40f2 | -3.982 | -42.516 | 2025-08-17 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 4f633530-c725-3e71-951f-e15c10c8299e | -10.8253 | -45.3152 | 2025-08-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 1c2c0580-ab6f-3bf8-b3e5-ef1e338f3ce9 | -7.5198 | -44.9836 | 2025-08-17 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| dbc3a8e6-681d-355b-a44e-520f5b3e72d9 | -14.1902 | -45.3008 | 2025-08-17 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 3d4ab9c5-62ba-39bb-b412-253c38f121bd | -14.1897 | -45.3241 | 2025-08-17 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 5dfdfb2c-c665-35b4-a3d5-5a42129e7234 | -7.2036 | -44.6931 | 2025-08-17 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a4886461-e8f3-387f-a257-cc9c4e4b2059 | -10.8436 | -45.3586 | 2025-08-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1ee2c8da-1b1f-361f-a6a3-df6339373a70 | -3.9819 | -42.5396 | 2025-08-17 14:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| db22a158-12d3-3755-803d-991393ea5d05 | -15.774 | -47.7933 | 2025-08-17 14:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c3b38d61-aae5-3888-9cf6-7a4abeb4ba38 | -3.9632 | -42.5406 | 2025-08-17 14:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| e1e00866-5de6-32e4-b5da-a27a3d183482 | -3.9819 | -42.5396 | 2025-08-17 14:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 165.8 |
| 6b810b52-016c-3d76-b509-d5bc377a0c25 | -5.6784 | -43.3892 | 2025-08-17 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 215.6 |
| e98383c3-2dfe-32f2-8cda-212caea3b0d3 | -12.6143 | -46.9047 | 2025-08-17 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 90b17563-9481-3953-9f44-e29e70f9d490 | -17.9137 | -44.4218 | 2025-08-17 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 113.3 |
| aa3a19a8-06bf-3bcd-bc43-a97d085cfad2 | -15.8602 | -50.204 | 2025-08-17 14:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0916b121-aee7-310b-9668-cd3ed5b49e1e | -6.5018 | -45.4576 | 2025-08-17 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 9c006427-fe1a-36e8-bf29-ba31fc1188d5 | -9.8407 | -46.3686 | 2025-08-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| dc4a2b87-18bd-3c0a-bf98-3e33fe0f9b5e | -12.6335 | -46.9019 | 2025-08-17 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 662905da-654f-336a-8870-8c6bd0214e28 | -6.0791 | -44.6276 | 2025-08-17 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 06526d6a-95e3-32ef-b965-0f0488f76203 | -6.4831 | -45.4591 | 2025-08-17 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| a71b22cd-014e-3192-92d4-9460e7891d6c | -3.982 | -42.516 | 2025-08-17 14:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 162.0 |
| 873a9c4c-bbfa-3cf9-bb4a-9043ab7d3680 | -14.1902 | -45.3008 | 2025-08-17 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ff49e59a-9a7a-33d4-ab1d-630df4cac7c1 | -7.1477 | -44.6524 | 2025-08-17 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6209c27c-6b21-3240-b1fc-ad5c3fe6e14e | -15.9229 | -48.1505 | 2025-08-17 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 105faee5-e980-3bd4-b0b1-784b2ba97e70 | -7.4267 | -44.9011 | 2025-08-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 96465564-58dd-3a7d-8745-ff358b07ec83 | -15.9224 | -48.1731 | 2025-08-17 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 97505539-3659-3942-9f79-6042e27b2f63 | -5.6784 | -43.3892 | 2025-08-17 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 437.9 |
| 16ed6668-08e9-31f0-a853-6f0ae42b9deb | -10.8249 | -45.3382 | 2025-08-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f06b0565-de0e-36e2-a46a-5b77e63da5c0 | -6.0791 | -44.6276 | 2025-08-17 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 721a129a-c319-3788-b461-1fb73fbf90fc | -7.427 | -44.8782 | 2025-08-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6f02d060-e1d5-3267-bd45-a606cb3952cf | -5.6786 | -43.3659 | 2025-08-17 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 4331e412-24ef-3854-90b1-f81d3f26f471 | -7.5198 | -44.9836 | 2025-08-17 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 1656c26f-7d9a-3e7d-bc71-73b5de5fce65 | -7.2058 | -46.2307 | 2025-08-17 14:20:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 14f15fd3-72d3-36a8-b3ea-51416cee6b57 | -14.1902 | -45.3008 | 2025-08-17 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d8333072-edb2-3bca-84ce-fedf7f80925c | -8.071 | -47.7045 | 2025-08-17 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a9aab3c9-3fa0-3d6c-b680-d1ee06fcdc52 | -15.774 | -47.7933 | 2025-08-17 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 83881d9a-81d8-36e2-97a7-abfafbe574db | -15.9426 | -48.1471 | 2025-08-17 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 751bf6fc-71d5-3378-8577-c2639604d2d0 | -5.6969 | -43.4111 | 2025-08-17 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5df0535a-ffb9-3d60-8eac-009814c05c97 | -6.0978 | -44.6261 | 2025-08-17 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |


[Clique aqui para ver as próximas entradas](README43.md)
