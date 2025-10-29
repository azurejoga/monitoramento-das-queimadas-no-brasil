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
| e52e199f-2512-3750-b99d-3fc7a916820f | -6.2939 | -41.8744 | 2025-10-29 00:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 257.4 |
| 864f44a6-c2f3-3adf-927e-bf740373b454 | -3.0507 | -50.2702 | 2025-10-29 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 2af77968-5564-3451-abce-a951c8f97bee | -2.0268 | -46.9299 | 2025-10-29 00:00:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a22c6200-d986-3ef0-9f0a-812d02cd9b64 | -13.2461 | -44.108 | 2025-10-29 00:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| bff0647d-c3e6-33e0-b97c-cde1c86281a6 | -6.3127 | -41.8727 | 2025-10-29 00:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 163.6 |
| e5d3d6d1-510f-32fe-af11-245c62f30491 | -9.8821 | -47.4566 | 2025-10-29 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 2956b6cc-dc78-311f-851c-8d48e40e20ad | -3.6758 | -47.1176 | 2025-10-29 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 239f7595-7ed8-3d00-a359-12252c1b84a8 | -10.6506 | -48.009 | 2025-10-29 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 67078f8e-d78e-3940-add4-ad7c9fed6296 | -2.4264 | -49.2948 | 2025-10-29 00:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 03d988f1-1a97-341f-8d8f-9c1163708e63 | -3.0731 | -45.0501 | 2025-10-29 00:00:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 205.9 |
| fc75c53a-ce9d-3f2c-8a87-b0c60540243d | -13.2073 | -47.0643 | 2025-10-29 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c63b32df-8b5d-3479-8e1e-f486c37aeeee | -3.0732 | -45.0275 | 2025-10-29 00:00:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2c668faf-88f3-3e3c-bc35-427bba878a74 | -12.0036 | -46.7667 | 2025-10-29 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| ba7b129d-67f5-329e-aa0c-ea1d70ef3642 | -3.0545 | -45.0508 | 2025-10-29 00:00:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3186dc34-3ad0-3e9a-b55a-c58ae46a3764 | -6.3125 | -41.8967 | 2025-10-29 00:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| cdbddd53-d62f-3ff4-854d-f3f1646a7209 | -13.6431 | -46.4748 | 2025-10-29 00:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6b44d20a-ce1a-360d-ab54-3d6fea6ee2bf | -10.6509 | -47.9869 | 2025-10-29 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 407256df-6326-36e5-913b-0345411b1a60 | -4.0852 | -46.9458 | 2025-10-29 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 3d31047c-0820-3f10-8f94-206af09fa1e8 | -2.0083 | -46.9304 | 2025-10-29 00:00:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7a84a764-113b-3e96-9fdc-f482ef907938 | -7.8037 | -46.4458 | 2025-10-29 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 5c85c07b-3313-3ce3-9b53-1018bf6fe3cb | -7.8757 | -48.4196 | 2025-10-29 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 59098710-2357-375e-8283-72fa6a8844e7 | -4.4804 | -43.447 | 2025-10-29 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8fb23138-3048-3210-9bcd-9de43d1d4782 | -13.6426 | -46.4976 | 2025-10-29 00:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 154.0 |
| b50ab518-8299-31c3-8c67-c6939ed9a1b7 | -3.3384 | -44.0828 | 2025-10-29 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 78883c27-a57a-36ad-b8e1-95b1998b38dd | -6.2936 | -41.8984 | 2025-10-29 00:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| a6fba927-dc9f-381e-b42d-b07cb9d399eb | -9.8024 | -47.7524 | 2025-10-29 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 79d7ae32-0ec9-3c17-8bce-785b62121821 | -2.7741 | -45.3989 | 2025-10-29 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 000f0847-54e5-3639-89cb-f4d20bf816c2 | -12.0032 | -46.7892 | 2025-10-29 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 019cf387-010b-363a-97f8-9a3e6b6595c3 | -13.6426 | -46.4976 | 2025-10-29 00:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 157.6 |
| f5773663-c926-3914-b46a-b751cd67a841 | -2.4263 | -49.3161 | 2025-10-29 00:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 49ab21fb-1bc1-3389-8a44-dc053fa06299 | -7.8037 | -46.4458 | 2025-10-29 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| fda7acdf-6a66-3dad-906e-228ff1b16e91 | -10.6506 | -48.009 | 2025-10-29 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| ec24c167-a9f9-3c6e-8e6c-714fef1d8faa | -12.0032 | -46.7892 | 2025-10-29 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9826ded7-8af1-3f6b-9cdd-b5907d8a9c25 | -12.0036 | -46.7667 | 2025-10-29 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 339d2d6e-8830-380a-9bee-85077dda95de | -4.2157 | -50.0812 | 2025-10-29 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ec42a8ef-34c1-34ed-8d46-f6f7c2ca2efb | -6.2936 | -41.8984 | 2025-10-29 00:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 770acfba-2799-35fa-9ea8-768f581216f5 | -7.1695 | -42.7198 | 2025-10-29 00:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| d61ea3ce-ade7-30f5-bbe4-55cb60c08595 | -2.0083 | -46.9304 | 2025-10-29 00:10:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 688251a3-68d6-30b3-800d-993ac2bf2e13 | -9.8024 | -47.7524 | 2025-10-29 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 18886947-73c3-32fe-b974-ebe6c8ac5f8d | -3.3573 | -44.0361 | 2025-10-29 00:10:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ed0d5069-7079-365b-9017-be71974a21e8 | -6.2939 | -41.8744 | 2025-10-29 00:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 202.3 |
| 502e8dc4-b04c-3c3d-b777-0fbdc6b15931 | -4.4804 | -43.447 | 2025-10-29 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e2097c87-e8bb-344d-87b0-d480aca3f08a | -6.3127 | -41.8727 | 2025-10-29 00:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 195.1 |
| 0c7e16f8-24e9-39e9-bc9b-4bcbc5798686 | -2.4264 | -49.2948 | 2025-10-29 00:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 43310c56-c939-32fc-9767-4405c6449de6 | -7.8757 | -48.4196 | 2025-10-29 00:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 6a98a3b8-a2ee-3684-8fbb-d200172b50c8 | -3.0731 | -45.0501 | 2025-10-29 00:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 236.8 |
| ea48ab3d-40ea-3dc3-8f7a-9d131ac53703 | -2.7741 | -45.3989 | 2025-10-29 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1fbc8b7c-3bee-321c-9e52-5269e355c4f7 | -4.5188 | -45.9937 | 2025-10-29 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ab0f33e8-5f56-3fbe-97de-982b5be70694 | -3.0545 | -45.0508 | 2025-10-29 00:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 50f81206-8840-3fe0-8f46-f9dfc5aa6c12 | -10.6509 | -47.9869 | 2025-10-29 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 336ef3e7-d867-3cfb-bf7b-e33ffd4d9bb8 | -13.6431 | -46.4748 | 2025-10-29 00:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b035ef6b-ce6f-3438-8b5c-0a24049a8787 | -7.4541 | -49.4018 | 2025-10-29 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7d4a100a-c500-3fe4-ac1e-22f3628f9704 | -6.3125 | -41.8967 | 2025-10-29 00:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 2b43562c-3ea9-369d-909d-7c25f553efc0 | -6.2936 | -41.8984 | 2025-10-29 00:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 2619ff51-0e22-3f0a-8fa9-26529688198b | -10.5467 | -49.9973 | 2025-10-29 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 513476d3-d264-3ba7-b9d7-8f26e9630f94 | -6.2939 | -41.8744 | 2025-10-29 00:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 245.0 |
| 9a02cd46-93c4-32d6-94e4-a475b89efadb | -14.4829 | -45.2485 | 2025-10-29 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ae3cdca0-c36b-3202-a688-922171b4eb1e | -13.2073 | -47.0643 | 2025-10-29 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| a1ed8c02-1538-3008-9d1b-708f3c14cd2f | -2.4263 | -49.3161 | 2025-10-29 00:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 34d31c19-33ee-34dc-ae32-4732edf5756a | -7.4541 | -49.4018 | 2025-10-29 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e6cf208c-c23b-3126-a7a3-dcb18b364bbb | -2.4264 | -49.2948 | 2025-10-29 00:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| aa0fe95b-c348-3fd4-b0f2-c5a4bcf68ebb | -10.2071 | -45.9412 | 2025-10-29 00:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c078a7c4-d4dc-3727-be50-c848b7b3026f | -6.3127 | -41.8727 | 2025-10-29 00:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 140.1 |
| 17c54d76-1fd7-3b0b-9225-fb3039deb720 | -6.3125 | -41.8967 | 2025-10-29 00:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| e3027743-e541-34db-94d7-32b55129baf5 | -10.6506 | -48.009 | 2025-10-29 00:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| abc355e6-0717-337c-ad71-774773a042f9 | -12.0032 | -46.7892 | 2025-10-29 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| c1113e0e-23ec-3939-b398-237bd4722f18 | -12.1958 | -46.717 | 2025-10-29 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b968fa84-e15c-3bba-b3f6-ab1f82c2637b | -12.1766 | -46.7197 | 2025-10-29 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 6d8c81c2-cfa8-3409-84ed-9929cacfc539 | 1.9606 | -50.9653 | 2025-10-29 00:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7ea22cdf-4fc4-3e2e-825a-93be137416ea | -3.0731 | -45.0501 | 2025-10-29 00:20:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| ac962b1a-8fc8-3250-ba1a-f03fa93cd550 | -10.6509 | -47.9869 | 2025-10-29 00:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 869ed516-fef0-3141-a98e-21a3986449aa | -12.0036 | -46.7667 | 2025-10-29 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 162b7b49-b813-310a-97f1-1b890f258053 | -7.8037 | -46.4458 | 2025-10-29 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c7f42fae-27ec-37e1-bdc0-548af2e054c4 | -13.6426 | -46.4976 | 2025-10-29 00:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 155.1 |
| f0d1686d-b843-35b8-b126-80a8d38e5bca | -4.2157 | -50.0812 | 2025-10-29 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5bf50dfc-18dd-383a-835d-9905eab5ef30 | -2.4264 | -49.2948 | 2025-10-29 00:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 527adccf-6da6-3a49-9d0b-d762138b2fa2 | -7.8037 | -46.4458 | 2025-10-29 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| a987366b-c0ef-3e24-bf99-efdec3a35ff2 | -12.0036 | -46.7667 | 2025-10-29 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 615bbcb5-0d7b-3268-baff-6113ecf57e0f | -9.8024 | -47.7524 | 2025-10-29 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 60ed908a-257c-3a02-ac2c-2675df19b511 | -13.2073 | -47.0643 | 2025-10-29 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 166271c2-44c4-3647-ae6e-dfbb26fe5cad | -10.5467 | -49.9973 | 2025-10-29 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9c6db728-6143-3fb1-aad5-bef31a7d5112 | -10.6509 | -47.9869 | 2025-10-29 00:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 8ff2f145-cdbf-3a69-81f3-b2ae60f51082 | -2.4263 | -49.3161 | 2025-10-29 00:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 693a2b22-2ee3-3c5d-ba76-b14c6b90df0c | -10.6506 | -48.009 | 2025-10-29 00:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 9e77bdb2-e04b-39c4-9669-7156d00fb6f5 | -3.0731 | -45.0501 | 2025-10-29 00:30:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 927daa5c-ff59-30db-88c1-3f9cc86b4554 | -7.7048 | -46.8994 | 2025-10-29 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 57875e27-3e23-3195-a280-d4d0d86686d3 | -6.3127 | -41.8727 | 2025-10-29 00:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 23c0a40a-eea6-3ce4-af3b-422e67cabc2c | -12.0032 | -46.7892 | 2025-10-29 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 351a72c1-89ac-3d61-8246-adffa3092376 | -13.6426 | -46.4976 | 2025-10-29 00:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| af608c1d-a9a9-3e92-8c55-70db226e9c6a | -6.2939 | -41.8744 | 2025-10-29 00:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 4948ff5b-a00c-39be-b795-4b9c7d5aaa97 | -12.1958 | -46.717 | 2025-10-29 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f5c9de5e-73db-3876-a872-b848518d7e5c | -4.2157 | -50.0812 | 2025-10-29 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| d88a4ca3-0feb-3de3-9a16-e6e497d07a82 | -4.1972 | -50.0819 | 2025-10-29 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a47a8d4e-616e-36ce-a7b5-4511dad024e9 | -4.2156 | -50.1022 | 2025-10-29 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 438efd4e-f852-3d1b-bfcc-b57c220aedbb | -12.0036 | -46.7667 | 2025-10-29 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 0308a9ce-ac12-3196-81d4-78bf9f207b96 | -4.1972 | -50.0819 | 2025-10-29 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7a675329-7173-379e-b0a8-8f8e2946e61b | -7.8037 | -46.4458 | 2025-10-29 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a996eeab-f39a-3797-a387-1e4ec5db9983 | -2.4263 | -49.3161 | 2025-10-29 00:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c10c993b-f15a-3894-bbf7-8adda1d0fc81 | -13.2073 | -47.0643 | 2025-10-29 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 94a0d3ff-9bb9-33ab-98c9-7239da1e8ccc | -2.4264 | -49.2948 | 2025-10-29 00:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |


[Clique aqui para ver as próximas entradas](README2.md)
