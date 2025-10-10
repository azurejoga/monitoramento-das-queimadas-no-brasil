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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70a15729-0932-3545-92fa-1e21086151da | -14.26747 | -45.88425 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90762a33-9be7-395c-be4b-a0a02bbdc2f6 | -13.26693 | -48.02221 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87a15f38-89ef-336e-baaa-4472defcaf5a | -17.08421 | -45.49067 | 2025-10-10 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1be836ab-f3d2-315c-9ce8-e9519115e339 | -16.74437 | -43.98791 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3638434e-fe71-32bb-8fca-9f21ff59a12f | -11.96779 | -45.20613 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f70f197e-90ef-30c4-99b8-f16593bc504a | -11.77395 | -45.04616 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adbf5c60-54ef-358d-9300-dd1da805a449 | -16.1263 | -48.44308 | 2025-10-10 04:02:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 247447bf-db65-38de-9620-b725bd21c419 | -17.93504 | -45.03546 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a2de1ee-7fa8-3fd9-9b05-b3175a5e9c81 | -17.98228 | -44.14259 | 2025-10-10 04:02:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e18d1b09-3c27-35d7-b79c-1d370b59ef5f | -15.4006 | -48.03173 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20fc656e-c51c-3875-996e-25bbb2761cc3 | -16.66943 | -47.60014 | 2025-10-10 04:02:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4741f40c-01d7-3931-9445-b049da9d5d45 | -15.11777 | -48.7139 | 2025-10-10 04:02:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f49f6833-d31e-3bce-b60f-6c0549412f0c | -12.27117 | -47.85193 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0c99a96-be1d-3161-ae91-6461c2093817 | -10.42737 | -44.99739 | 2025-10-10 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94dfd9de-f284-3078-a47d-5c757886593b | -14.98716 | -47.20204 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e6a94918-9b77-3815-afd1-1cc8586938a9 | -14.71284 | -47.44029 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63c1f836-3204-333a-bd19-a2e67f5612b6 | -16.0682 | -47.76737 | 2025-10-10 04:02:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b60ef25-62fd-3b13-9e1a-16dada6d9459 | -14.99193 | -47.19905 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cacec493-866e-326c-a025-81dc2adddd90 | -11.56348 | -41.88852 | 2025-10-10 04:02:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4e722451-7ed2-32f6-b8ec-50b599804790 | -14.57298 | -47.46404 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 24620ea8-336b-3b79-b7b3-ef7c521f0187 | -16.54082 | -48.89252 | 2025-10-10 04:02:00 | NOAA-20 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d874a0d-19a0-3a3b-9cf9-1e3c9a029f8d | -10.65416 | -44.15731 | 2025-10-10 04:02:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 142f3dd6-13f6-33c7-ab62-d6f112856224 | -13.38647 | -44.23329 | 2025-10-10 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc451a4f-058b-3c12-89b4-7cdfba5817f0 | -11.46417 | -41.89432 | 2025-10-10 04:02:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32760f75-87c2-343c-906e-e34be094bd4a | -15.07811 | -46.58807 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b4b5814-5f5d-3e20-a3fe-9ad5b291c5ae | -15.57383 | -44.43034 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cbd864ff-261d-36e7-9e67-aa43c8752bf9 | -12.90728 | -49.10738 | 2025-10-10 04:02:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d2dad6c-45a3-37ff-ab42-048d88267ebe | -15.74602 | -48.99068 | 2025-10-10 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a89940bf-7411-3d5b-b76d-fdde923d5337 | -14.57394 | -47.46269 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3fc41b78-251e-37e3-8024-8922633ff8c9 | -13.17044 | -43.24767 | 2025-10-10 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54535a62-ef90-3af4-a218-0c9b77d5821b | -16.12752 | -48.44213 | 2025-10-10 04:02:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cde4911-fba8-359c-acb9-11c5294e4b01 | -13.0162 | -41.43022 | 2025-10-10 04:02:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 2e13c0bc-6ade-337b-acb6-6940c62df2c5 | -15.00724 | -46.28902 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 00f3604e-3b9e-347a-aec2-4d676caaf22b | -16.11917 | -47.91316 | 2025-10-10 04:02:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4288cd6a-7254-3213-b41b-5a9b03d6b631 | -13.34408 | -47.75555 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 39735ade-8f54-362a-a587-84f511511fb7 | -14.87466 | -48.22774 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 02d891b0-2325-318d-80c7-d85d271c773c | -14.93267 | -46.76699 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f710a413-c952-32ee-ac34-f738660b3f9d | -13.41191 | -47.63029 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48e5b9a5-10df-350c-8e9c-9e3d03660b2d | -10.56844 | -47.005 | 2025-10-10 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0c36746-7d1d-302c-845b-9423a6f3cff0 | -12.956 | -43.9444 | 2025-10-10 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6918a597-4c2e-3e41-bdfd-95b8b360c93c | -13.84387 | -45.86246 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36c7b106-b824-3e87-bd48-082144186acf | -17.99181 | -44.96094 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bae9b1c5-2693-3745-997b-f514d234be58 | -15.00903 | -47.55893 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3d71f45-df95-3fe3-bff6-292489acf882 | -13.02547 | -47.88709 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| feee3ac4-6cd6-31d3-aed7-ec3659c22b31 | -15.78859 | -43.65525 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7edd23bf-fb10-3a5d-bf26-b2a2016e8cd5 | -13.83922 | -45.82118 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4144d828-4eff-3219-acf3-ffbae02e35e3 | -15.42692 | -47.98496 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eec3fd86-39d6-3930-ad67-26ddf1c224f7 | -16.29407 | -47.1576 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bef00f0c-47d1-3954-ba74-7e10a11f6127 | -14.68231 | -48.06429 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ffd188a-f2f1-3655-9451-fd996e3142fe | -11.92953 | -41.53395 | 2025-10-10 04:02:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0562f13d-2862-3f5a-b286-35f6d0c90c3b | -15.73601 | -43.94749 | 2025-10-10 04:02:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d2d3c76-67f7-3d71-9a23-d78810d6f4a3 | -13.83577 | -45.88618 | 2025-10-10 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6dc7155e-e7cb-3fc9-96dc-79a9d400738b | -17.3848 | -46.68519 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 651bd91e-2651-373c-ac5d-fdfc0fb3302f | -14.89833 | -46.8574 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 516f4c6d-7785-35a7-930c-c748c548ef54 | -17.3772 | -46.68359 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f7f4424-7e9c-3d0e-a1f7-c1c878b8cb0c | -17.935 | -45.01436 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 81464bea-3629-3a6d-9bad-1de9b16fcbf8 | -17.94475 | -45.0206 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a960cd0f-5b1d-3daa-9536-2a1b2479de4f | -17.93152 | -45.01365 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| de000e48-aaca-34b0-8831-45248f811267 | -13.2681 | -48.02493 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 108dcf0f-84d7-306b-9b34-92d5a1d8cd7d | -13.23333 | -47.61361 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f391fd6f-718d-3430-b95e-33cd79743632 | -13.36599 | -47.21144 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7054500a-1dd7-34eb-af85-cd7dc46b9133 | -16.27609 | -47.16553 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2e6cae2-8201-34e1-97de-3c1a2d3dca6b | -13.36249 | -47.75342 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6687053b-ef4d-32aa-9098-74aa3d91df03 | -12.47339 | -47.43629 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5970a82-76aa-33b2-bd51-6719a7ab57b7 | -14.86157 | -48.46624 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88ccd9a4-ca92-39a5-bc5d-ea877f139aeb | -10.93621 | -42.85492 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64daf249-807f-3934-9468-518615975ba4 | -15.09105 | -46.60638 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03be0b7e-43ac-33b1-b6ac-37e025da000a | -17.93432 | -45.01838 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 96f619ac-57cb-3650-a4f7-3459c9404f16 | -13.29795 | -47.1292 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a92d924-756e-3889-aef8-b1aa44c1266d | -17.38012 | -46.68929 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca8fb2db-a0ab-3f60-9798-1ffccbf22e5f | -10.86097 | -47.57789 | 2025-10-10 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17634ede-1727-3745-b3a0-4b2a8914c683 | -12.35644 | -38.27829 | 2025-10-10 04:02:00 | NOAA-20 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a66848ad-09a8-3507-adef-5906117bd0e5 | -13.32379 | -47.74348 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cee5a43d-9991-3165-9f55-6f3e4aaf43e9 | -15.73944 | -43.94809 | 2025-10-10 04:02:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e76e2b85-816d-3263-92d8-cde29ef36afd | -16.12938 | -42.72258 | 2025-10-10 04:02:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 2bc584e0-59d8-341f-8319-191e52aa715f | -14.38936 | -46.00174 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a8cb040-c0a6-3602-9d27-e7bd351c02c9 | -17.99669 | -44.9744 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be353d08-9753-398b-b021-71b3c8bbb6af | -15.39483 | -47.30832 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aebbade-503e-352b-b060-56a1c9c374e7 | -11.56015 | -41.88797 | 2025-10-10 04:02:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fe174423-b65b-3b7a-9721-b66126cb60fb | -13.35795 | -47.63232 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cda3775-c998-3d1e-b362-b8e01cb672a3 | -15.40488 | -48.03257 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e9f43c1-cb73-3ee6-8f2b-f62f21cf6433 | -14.89006 | -47.231 | 2025-10-10 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13662a4d-0d05-33f9-a1af-ea5e7cb2a86e | -18.0697 | -44.97506 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc349046-7584-30ae-a7bb-82a74d0021dc | -13.51707 | -48.11862 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 305d0211-ec6c-3f06-a1c5-c62299068a5c | -18.02243 | -45.01317 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 239a7d2a-6a7b-326b-8184-c8e799790e04 | -11.77847 | -45.04244 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2288d65c-5034-332e-97b1-a6f5123893f9 | -14.88174 | -48.23824 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ee8c3a13-9c86-352b-ab22-b6178836d509 | -11.4675 | -41.89487 | 2025-10-10 04:02:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6105dc6c-626d-3576-acd0-3dcaaacc8480 | -14.70873 | -47.43914 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70f41fc4-b021-3fa4-842a-cf38b3c7514d | -12.63502 | -45.03478 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f5c5aa4-85c4-3c13-b474-94fecd19abaf | -13.29687 | -48.49042 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c163f6b-3792-3141-8764-9e93dbfd05f0 | -12.63184 | -45.0531 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf804383-7a5a-3058-898e-95ccbf1189d5 | -16.17487 | -42.86018 | 2025-10-10 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc1a9c66-1d06-31c3-9f1b-864f39e63643 | -13.31841 | -47.9923 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6387585e-bdba-3c71-bc76-b869ab4ac57b | -16.29339 | -47.16133 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d20b91bf-d231-3127-9001-84c9beeea2e1 | -15.08206 | -46.58867 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d56c079c-f94d-3544-bca0-cea7cd371ef5 | -17.96257 | -45.00555 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d32dc41-ce77-3382-bf5c-084f047ab6ea | -15.47466 | -47.98092 | 2025-10-10 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb056317-13e0-3057-911a-67e667a46a9d | -16.12606 | -42.722 | 2025-10-10 04:02:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 07ae3f1e-9fcf-3c19-9ad2-f9fbadc8dc1d | -14.54693 | -47.00005 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
