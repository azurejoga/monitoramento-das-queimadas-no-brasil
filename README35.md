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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9e7bad1-5bed-385b-a94c-b3b12a13dbf2 | -12.68169 | -48.5846 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e98a75d-76cc-3bec-9b2d-8885c77db769 | -13.1244 | -47.8751 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcf71c83-a808-37a7-9bd1-40a848554d97 | -14.73106 | -48.10866 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3c3263c-d19a-3f96-baad-e12ae41d048f | -13.12639 | -47.86515 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6c7fbb95-f5a4-33ec-adbf-669892beb109 | -13.86201 | -47.93832 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfffff55-52e9-31db-94f8-d203d495eb43 | -8.79578 | -46.67155 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 033cbddf-22ee-3508-a0be-95ac73729942 | -13.77153 | -48.05848 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f33ed54-9366-3527-8495-b7605423ffa5 | -11.44838 | -44.96117 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 350a2618-aa8b-3a1e-81a8-51da3cb9c3f7 | -14.95227 | -47.52072 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45464727-bc6e-3951-93b4-309e77cb15bf | -10.86895 | -46.68394 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a3d42ef3-1fc9-36d8-bdef-117b51f11712 | -13.75787 | -47.9766 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e64ead7-26c9-32c3-a1be-f48e3638da40 | -9.95323 | -43.70652 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a1b99064-bae6-3d9c-9c6a-81b26797432e | -12.62383 | -47.00087 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc9bc11f-c14c-372c-b5e1-c2b07f874150 | -11.85053 | -44.96788 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 953ffd3b-fb5a-39f0-a1c0-6dd57a643309 | -12.38062 | -46.5233 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80c77eab-335a-30b8-b296-ce48a8b4ee62 | -13.12859 | -47.88489 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 46f54e42-6a6c-3052-ad97-30e414db2119 | -13.96238 | -48.10474 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ae55a43-d20e-356e-a90b-6ea5e61a7ead | -9.90166 | -43.71909 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7523ba14-53fd-3537-b4fc-ec64204df978 | -14.66364 | -48.25487 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe39ce55-ae92-34e4-a097-92c3c4f74264 | -14.41107 | -47.87779 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f151e496-b57d-3640-bb5e-74610d7e5954 | -14.93212 | -46.90646 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0e5649b0-946b-3df9-b079-a45cc3821970 | -13.33105 | -47.8019 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3430fa55-451e-3466-b545-f5e62fa28cf4 | -14.59805 | -46.72322 | 2025-10-03 03:45:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84cd2e89-84b5-355e-9ade-82542fbb8c21 | -12.37987 | -46.52712 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ecefe07-11cc-323a-84ee-d57abc7d7752 | -14.29893 | -45.98728 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e525cf6-33a0-37d6-a0d9-a9ff39196d6a | -10.86973 | -46.67986 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 119f2616-94a2-348a-a135-57a4116a41d4 | -13.57334 | -47.5852 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5938a0ec-ae21-37e5-b39c-ca45e69acb0d | -13.7787 | -47.52467 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d4573fd-0201-33ac-b209-c8c1e68c6561 | -14.90618 | -48.33755 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4972c5b3-7eb9-3272-9640-8ae72990900a | -11.01144 | -46.54897 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec55e953-3dbc-3088-914d-0b3b1a01b88a | -15.52744 | -46.81132 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e0c032e-1a34-36ef-b9ac-41fde81c885e | -15.78163 | -42.04873 | 2025-10-03 03:45:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3eab2b16-2e28-3630-8b84-2fb422649cc8 | -11.50664 | -43.50833 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8595701c-975b-33ab-a57a-5a69a4a08333 | -14.65035 | -48.29877 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 277a3969-25c0-3d83-bef6-e52841ae9df5 | -14.60105 | -48.24073 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b6036c5-3360-375b-9a52-993a832b01df | -14.1908 | -46.12074 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1db26fd3-fbd2-3b3f-8fd4-6d10a7bf3aad | -11.83452 | -45.00122 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4dbbb575-dceb-3ef9-a320-894c76e87d8d | -15.70278 | -46.25613 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e311c92a-ed06-33e1-90b4-5b46112551bb | -11.92017 | -46.27686 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 6dbb7604-53b1-3524-a474-888a3ccd3f91 | -15.57606 | -46.94711 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5088f99c-b787-3ec5-9fbc-c34e2c394d9a | -13.27404 | -47.23914 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7df57279-36f4-3f81-b640-a544f5ff19d1 | -12.3697 | -46.52078 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c29eea6-2e52-3d68-82d9-de48ba851784 | -13.13533 | -47.84162 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccd88cf0-a203-379e-89fd-b7da4514d339 | -12.61779 | -46.97205 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 010236a9-547d-3ccc-8959-0b9bd676c176 | -14.19048 | -46.67177 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77d4685f-6991-3f9b-b1e6-ec2ca07ea60c | -14.85811 | -48.28327 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b71d83ba-8fc1-3071-99c4-212d05ab07da | -9.9192 | -43.7588 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 47ace4a2-6bb0-3342-82a1-5b3e266ada25 | -13.4778 | -47.24462 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b79fde35-d333-3c0b-9460-c55bea4ea148 | -13.27209 | -47.26159 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 50423f51-7f56-3476-9254-7478ba8aaabf | -15.50101 | -44.18747 | 2025-10-03 03:45:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc11d0c3-78fb-39d8-939c-df174ab9885d | -13.75214 | -47.98288 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89a38de3-bb14-366c-8f29-d66e83b3f477 | -15.21307 | -47.18732 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b76bcd74-2f0e-30a0-adf7-ac2722f34727 | -14.94733 | -46.8985 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1761e98-0276-34eb-9f4e-9c113b393ceb | -11.86503 | -44.97352 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4eafd60f-d6cf-3ef7-afdf-e2e2bc2a729c | -10.84368 | -46.60021 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75347275-4dc3-395b-9c0c-46d0eb692cfd | -13.12365 | -47.86842 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd26e0c1-bbf9-35fb-93f7-a0dc1952ece7 | -15.52347 | -46.80357 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44709c70-83e9-3986-8ce7-aaac5645b52f | -13.84093 | -47.92879 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 164046ce-b829-3503-8768-b2071281ef9f | -10.90925 | -47.03877 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6e9f2f9-80c1-3808-83b3-366932b4ccf8 | -14.35781 | -43.85037 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06d75646-4a13-3736-8eae-6c98b70e84a7 | -14.28902 | -45.91692 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b6e9d20-36b9-39b7-baa5-70be9437f8f7 | -11.11077 | -43.19116 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75984ecf-3065-357a-9609-5f2354c7d378 | -15.34358 | -46.25985 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 348330be-24ca-3b6f-8199-52b41e9e5e52 | -13.39951 | -47.554 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 321f2a1e-8308-337d-a194-f5fc02376e96 | -13.33518 | -47.21096 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fb95a42-639f-3fb2-a824-61bcc8e39666 | -15.31267 | -46.38761 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f94e07e-8663-3ef2-ba06-de3480787639 | -11.87897 | -45.0095 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38c02b2f-f150-3ad1-bf56-89adcc008987 | -9.92008 | -43.72576 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4ba7eeab-72ed-38a5-8104-571eb006d1d0 | -14.29143 | -45.8913 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5cac4ff6-8208-3870-86db-097a4baa01ec | -13.67981 | -48.03709 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce264149-b6cc-3d3c-bb37-39e1ea2b9f4d | -13.19506 | -47.78876 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d0d7782-039f-3fd3-947a-33e603b3056a | -8.90376 | -46.60564 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad458f04-a6b8-3b8a-a261-591fe71d938c | -12.69105 | -48.54757 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06629b82-8eee-3165-978b-6dc6ebfc11c3 | -11.88059 | -45.02838 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f2a152b-d065-34f9-81de-7160af250a60 | -15.3774 | -48.60115 | 2025-10-03 03:45:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35a8262a-7f64-3d1a-8a49-058802477b2b | -10.88794 | -46.71606 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 22c8365d-d8b3-3a22-a2aa-bd700cf35cdb | -11.8117 | -45.01197 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c70804af-3cd5-34f7-afe7-3b5ea01df8a7 | -12.80954 | -47.01029 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 701945f2-df46-3301-8a26-dd9e7e92eb72 | -14.41999 | -46.08791 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 491b98ec-5743-3ea1-b9a6-7f11b511d779 | -9.94553 | -43.74884 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2b3777b4-01ab-38e3-9bc8-2b531ca2416a | -14.62496 | -48.24355 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1533ee9b-dfe3-394f-a34a-21de23e0436f | -13.96499 | -48.11178 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b5b9b67-123e-3652-81b9-34efb6901860 | -13.23786 | -47.30338 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb373055-ddc2-3b67-90cc-4c97bad2f4f2 | -14.07511 | -45.67983 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6ac4e38-bbc0-329b-90b1-0591f758ea50 | -9.94171 | -43.74276 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff04ef90-785a-3644-9b15-de3b9ee5e1f6 | -9.90744 | -43.71453 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 305377be-5c2c-3e9c-ab66-c9ad0d231f83 | -12.38605 | -46.52465 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee73e230-ab66-3d25-b944-c6b34f16084a | -9.9 | -43.72784 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8c9ef77a-ab2b-30fe-9fb8-ef9393a7ffd8 | -14.3099 | -45.8782 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49cc227a-7ec0-317c-8034-35db6fc56b3b | -11.90972 | -46.74525 | 2025-10-03 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20e78063-12bb-32fa-8c35-1fcb6ece11fa | -15.51602 | -46.81348 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a95c4b96-b1e3-3a94-8f62-922ccb51e299 | -12.86888 | -47.03542 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86c0e778-d75b-3489-a08e-2594a132c4f6 | -9.91914 | -43.73112 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7f984d3b-e7eb-3d80-a561-3e6f2602cbdc | -15.49211 | -45.9305 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35813078-be6a-30cc-bac6-7ba6cfd2c143 | -11.92082 | -46.27346 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 1bca0098-1627-3866-a1b7-49c9f35002d9 | -13.20605 | -47.8856 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73adf962-6e45-3c4a-87a6-f633da9911ad | -9.76384 | -46.22322 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5e8ed55-0921-3fa6-a090-7f461d541f13 | -13.125 | -47.89158 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 38a06713-dcf2-3f07-b6b6-394f03fe0489 | -12.72101 | -48.58192 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 661f8d83-9c69-3869-808b-95862cab94a4 | -14.6894 | -45.18228 | 2025-10-03 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README36.md)
