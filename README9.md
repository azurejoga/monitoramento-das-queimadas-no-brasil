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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9df65855-ccdc-32a7-9574-f0730bc106e8 | -17.9026 | -57.5153 | 2025-10-10 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 917977b2-0570-39af-8447-c49e3a086244 | -17.9369 | -45.0388 | 2025-10-10 02:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 121.7 |
| f9b82981-b8d7-3b2d-8443-42b1c34710d4 | -17.9175 | -45.0194 | 2025-10-10 02:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a3fe080a-e8c0-3078-a64c-f97684421364 | -10.1707 | -44.5959 | 2025-10-10 02:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| ea7a7f3e-bce1-3a7e-aecb-153848630da8 | -8.1993 | -43.3424 | 2025-10-10 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| de244fb3-4d52-3512-9e3c-76a91f9c2289 | -14.9367 | -46.782 | 2025-10-10 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 45cf7b93-e10b-3ad5-b5f2-9d25917a19db | -17.9376 | -45.0148 | 2025-10-10 02:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 5ce3d5c9-2b37-3ec8-ba03-997b23926d5c | -17.9026 | -57.5153 | 2025-10-10 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 840bf63b-488e-350e-a3a1-639e2c572ada | -8.5032 | -46.1321 | 2025-10-10 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 87e24ef4-68c2-3902-ae31-e1b0931c5cc9 | -17.9369 | -45.0388 | 2025-10-10 02:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 386fe421-48fd-35e3-b525-85e1b88bbd31 | -17.9376 | -45.0148 | 2025-10-10 02:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 0f4d8b1a-ea16-35bf-8166-b6fc8a269b4a | -8.5029 | -46.1545 | 2025-10-10 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| a5eb07cf-c87a-3b45-97c8-c6312ca86578 | -14.9372 | -46.7591 | 2025-10-10 02:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7753e7d7-ddd8-323d-a8bc-43a9767035f7 | -8.5224 | -46.1076 | 2025-10-10 02:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8bb3d863-2d99-3355-ac8e-860b4d16015e | -8.5221 | -46.1301 | 2025-10-10 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 301.3 |
| 981bcc50-c4e1-34c4-a3ae-6622bdb7aaa5 | -8.5218 | -46.1526 | 2025-10-10 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.8 |
| eec8583e-de4a-32de-a9c3-13f9e71dd3c1 | -17.9175 | -45.0194 | 2025-10-10 02:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| fb7e177d-41ee-32cf-891b-b1aeb4775917 | -8.1993 | -43.3424 | 2025-10-10 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 2edf0005-a038-39f7-9189-5f9291a850c9 | -8.5218 | -46.1526 | 2025-10-10 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 3b81b13a-9a68-3702-9802-5e5183187f5c | -17.9376 | -45.0148 | 2025-10-10 02:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 5788532d-7817-3967-80e5-7ad0231440ff | -14.9861 | -47.2059 | 2025-10-10 02:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1e376530-a5a0-3135-86ec-9891b3f092b8 | -6.5849 | -44.6327 | 2025-10-10 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e21c7f0d-449d-35c6-a8dd-f282cbe9b1c0 | -8.5221 | -46.1301 | 2025-10-10 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 259.9 |
| 1f54af78-8ac9-3089-b57b-9f2109742e1b | -8.5032 | -46.1321 | 2025-10-10 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 315.0 |
| a1ebcf33-4f34-3bab-bcc9-0935c5f42961 | -17.9175 | -45.0194 | 2025-10-10 02:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 77590cbb-8a5d-3255-ba9f-a0a675a63bf6 | -14.9372 | -46.7591 | 2025-10-10 02:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1d8d6dce-b0bf-3038-b27f-3c5a6a820817 | -17.9369 | -45.0388 | 2025-10-10 02:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 5e029331-2b14-3e90-8579-bf519f29486e | -12.6294 | -45.0517 | 2025-10-10 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2833bbc3-8d57-3724-9d9f-5b4a4f36ff4a | -18.6497 | -43.9301 | 2025-10-10 02:50:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 01015088-4fbb-3878-ad82-4584f79d201a | -17.9026 | -57.5153 | 2025-10-10 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| be847979-65b9-3921-87bd-3afb82b4de62 | -10.1707 | -44.5959 | 2025-10-10 02:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9b1ce7b1-ad89-3217-92e6-8f5fda888e89 | -8.5029 | -46.1545 | 2025-10-10 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| b23fd092-dd8c-37c4-a7f8-f48ef77971b6 | -17.9026 | -57.5153 | 2025-10-10 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| c5f5dcbb-767a-3907-a720-0fa57d5a477c | -8.9008 | -46.0007 | 2025-10-10 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c7bbb366-a6c7-3ad2-a771-73f17bf3b64a | -8.5221 | -46.1301 | 2025-10-10 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 224.0 |
| e98cb378-2eac-300f-9107-2b46316dc8ac | -17.9376 | -45.0148 | 2025-10-10 03:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 184.1 |
| dfd1cd96-7dce-34c2-87c3-8de085998312 | -17.8828 | -57.5177 | 2025-10-10 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 3553eb32-6cfe-31e6-9754-bb44a148c0f0 | -13.0122 | -41.4273 | 2025-10-10 03:00:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 49.3 |
| 9213c1fe-170b-36fc-a07a-52fdd8edf047 | -8.5029 | -46.1545 | 2025-10-10 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b5669f1e-3718-3108-b63f-b8c018506899 | -5.4937 | -43.0761 | 2025-10-10 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 1da2b0d3-3694-3f9a-940d-83aa00f58e3e | -10.1707 | -44.5959 | 2025-10-10 03:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5b85f482-c2f7-3485-a4ea-3a431be789b7 | -17.9175 | -45.0194 | 2025-10-10 03:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 5dfae8bd-9935-35eb-8c70-f93d497eaa16 | -14.9372 | -46.7591 | 2025-10-10 03:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b347b526-b032-37d3-9cd9-a34e137e08bf | -14.8869 | -48.2362 | 2025-10-10 03:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7507cc29-c431-391e-bd41-f0d706c64987 | -18.6497 | -43.9301 | 2025-10-10 03:00:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 9ec9d10a-c179-3c29-b99c-73e6f1f2cb96 | -8.5218 | -46.1526 | 2025-10-10 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ad1ab37c-fec7-3004-9db1-1d5505ed8cb9 | -8.5032 | -46.1321 | 2025-10-10 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 6f0b9874-8648-3daa-bc9b-ae63d113a07e | -17.9376 | -45.0148 | 2025-10-10 03:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 8ed7f9c4-a727-3f80-ae0c-fd99413152c1 | -17.9369 | -45.0388 | 2025-10-10 03:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 62952a29-2727-3580-bbb7-2a2c240ee8e3 | -5.4937 | -43.0761 | 2025-10-10 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bd4de314-fc62-3f27-998d-e464d9b41ced | -8.5032 | -46.1321 | 2025-10-10 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 392.9 |
| a87fceec-4955-3ed0-8ea0-cb59bd94a3ae | -8.5218 | -46.1526 | 2025-10-10 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 6ae69085-b286-3898-8dd0-f7c75626dfaa | -18.6497 | -43.9301 | 2025-10-10 03:10:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 144.1 |
| e4b492c5-7914-39ae-b21c-4b1d32f58f32 | -8.5221 | -46.1301 | 2025-10-10 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 304.7 |
| 1a93c4a0-4cbf-3190-9a58-fecfa323aa60 | -5.475 | -43.0774 | 2025-10-10 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 209f147b-8324-3787-8046-8ca18f3d008a | -17.9175 | -45.0194 | 2025-10-10 03:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8070c08e-7d97-327a-8299-1b10488aadd5 | -8.5224 | -46.1076 | 2025-10-10 03:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ded78db6-3d29-373c-bc48-996eba217925 | -17.9026 | -57.5153 | 2025-10-10 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.0 |
| ebd085b8-5c53-353a-b6d2-65e0e46e130e | -8.5029 | -46.1545 | 2025-10-10 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 253.1 |
| 0850d0f0-e927-31e0-98c0-e11974c39d30 | -18.6294 | -43.9351 | 2025-10-10 03:10:00 | GOES-19 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 721697f2-c7ed-351b-9412-d4d3fcf95164 | -14.9861 | -47.2059 | 2025-10-10 03:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 733858e0-29d3-3bc7-a7c8-ffabb4552e5f | -8.5035 | -46.1096 | 2025-10-10 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9b9aa1fa-0d6b-3ca5-b7cb-89fbe1c046d6 | -7.45019 | -37.33347 | 2025-10-10 03:10:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 51e81d1c-590e-320f-b308-b1b130f79c36 | -4.9357 | -38.75591 | 2025-10-10 03:10:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d683f5ed-333c-3ea4-b660-11d217a9b5f3 | -7.66978 | -35.15432 | 2025-10-10 03:10:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0492aad8-ff03-3626-b6ec-f4b94261e907 | -5.4632 | -35.67015 | 2025-10-10 03:10:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39d8924a-dbf7-3cb9-a585-6c4f8db74af7 | -6.48447 | -39.81968 | 2025-10-10 03:10:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d8cfc0f2-fb15-33cc-a718-6860af8c33e7 | -4.93659 | -38.75085 | 2025-10-10 03:10:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6a5cb731-4bbb-3e53-8492-dd06411bbaef | -6.48562 | -39.81361 | 2025-10-10 03:10:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 47f4f992-7193-369f-a4b2-61b868365e7d | -7.21553 | -34.90654 | 2025-10-10 03:10:00 | NOAA-21 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 44fa92cc-febb-3855-8bf0-c8bfff452d03 | -7.66503 | -35.15339 | 2025-10-10 03:10:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 81c7f543-a0cd-329e-842a-e33969fe0502 | -13.01732 | -41.42507 | 2025-10-10 03:13:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| d964b28f-aff5-3a42-9f6b-e13ad1c0fe8c | -11.09283 | -41.05036 | 2025-10-10 03:13:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e3b9be6c-db06-385f-90c5-6ead71f9203b | -11.09165 | -41.05607 | 2025-10-10 03:13:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 21f7e3f4-79db-3086-8c26-51d811cbe753 | -11.09939 | -41.05159 | 2025-10-10 03:13:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| af0fcafe-a733-3f0d-add1-92bb3dfa722f | -11.09265 | -41.05753 | 2025-10-10 03:13:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 830ef8ee-2941-33f3-904d-0693da3aca66 | -11.09379 | -41.05181 | 2025-10-10 03:13:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| d43ab6e9-e034-3b23-a126-979d9b9a4d02 | -11.0982 | -41.05731 | 2025-10-10 03:13:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 21a6c64f-fe39-3344-884a-e24ad629b7bd | -8.82537 | -40.55484 | 2025-10-10 03:13:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 54c3b87d-0f4e-3ba6-91d3-44a77224bb55 | -13.01614 | -41.43069 | 2025-10-10 03:13:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 080b8c35-b5fc-3227-bea9-d68c8d9a5566 | -15.91467 | -43.29358 | 2025-10-10 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c12ed94-738a-362c-bf48-e606a1fcfea4 | -16.17832 | -42.85982 | 2025-10-10 03:15:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68a9f1c6-b845-3bc0-9cbb-7c8e7b8f5ed6 | -15.82521 | -43.78021 | 2025-10-10 03:15:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 607936fb-a005-3e6d-8699-83e38c9efefb | -18.63868 | -43.94233 | 2025-10-10 03:15:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 15fe1ef5-abd9-3882-b058-ff0ae1caa0c8 | -15.81823 | -43.77849 | 2025-10-10 03:15:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| da6c6635-5ace-3222-973b-be81d5b71b93 | -15.33353 | -43.1896 | 2025-10-10 03:15:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a7e7e5e9-3fa3-3f5b-8348-0bc4edaaa5bd | -15.91437 | -43.29794 | 2025-10-10 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03bb3568-28ac-34db-84b4-7d163a20a75a | -15.91289 | -43.3016 | 2025-10-10 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35ccff02-7e86-38a1-9bd6-12a8fb33b5f9 | -16.12872 | -42.72193 | 2025-10-10 03:15:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8a259183-e9da-39b4-9791-97e26892139e | -16.74354 | -43.9828 | 2025-10-10 03:15:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cc6379c-1587-3c77-9f03-692bd659c407 | -16.12601 | -42.72292 | 2025-10-10 03:15:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 4afe90b6-d4ce-3bb5-8471-b147e5c8be69 | -15.33205 | -43.19617 | 2025-10-10 03:15:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d4600736-faec-3f00-9fd5-816830f7cf86 | -17.66412 | -44.45993 | 2025-10-10 03:15:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f580e76b-c2a1-3a17-aed7-19dbd8c7224a | -15.91619 | -43.29003 | 2025-10-10 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c90e76dc-94ab-31a9-a887-f201d37a732f | -15.82833 | -43.77768 | 2025-10-10 03:15:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9dc7fa75-b57e-3dd2-872e-b497dadd1148 | -16.74486 | -43.97716 | 2025-10-10 03:15:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 111a35f0-7ebd-3930-90f0-e41c1cffd838 | -15.82136 | -43.77591 | 2025-10-10 03:15:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 85fa1ff1-bd81-3ffb-8b28-52dc3183b894 | -5.4937 | -43.0761 | 2025-10-10 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 8cec755f-5819-37fc-b571-745c961ba1e5 | -8.5032 | -46.1321 | 2025-10-10 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0ebd7f25-c961-3b82-8aff-08bc9f049410 | -6.5849 | -44.6327 | 2025-10-10 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |


[Clique aqui para ver as próximas entradas](README10.md)
