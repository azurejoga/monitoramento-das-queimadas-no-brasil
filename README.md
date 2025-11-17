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
| e6716e3a-a024-3534-818e-1234c4080c82 | -6.6684 | -42.0553 | 2025-11-17 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| d22acd61-4806-33dc-9d9b-5e37131b691b | -11.849 | -49.2 | 2025-11-17 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| fd886454-873b-3164-ac51-c5211d512599 | -10.6498 | -49.3834 | 2025-11-17 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9c80c38d-6b73-3d72-9a78-76ee5a033ab4 | -5.0399 | -43.6205 | 2025-11-17 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 29a52e2f-7139-3a00-bd56-a93f55c493f9 | -11.8295 | -49.2242 | 2025-11-17 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| fa2c60f7-1119-3ef2-8193-958a13bb2e1f | -11.8486 | -49.2218 | 2025-11-17 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| eb43e0f4-fddc-3c5d-9a97-01284a8cd874 | -10.8749 | -44.6172 | 2025-11-17 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 28cd9144-ef20-3a2a-bac4-9b4bbde3f5dc | -10.669 | -49.3597 | 2025-11-17 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 4acb2d8f-755c-3197-8a6c-8795e375eeec | -6.6875 | -42.0296 | 2025-11-17 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 672.4 |
| 9f6c3d53-4418-3654-9388-cec78bbe59bd | -2.5238 | -47.8332 | 2025-11-17 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 82d9b7c3-0180-339e-ad1c-d46201bef642 | -2.5053 | -47.812 | 2025-11-17 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| f5954f65-3344-3832-9492-0d7299e00e3c | -11.7021 | -48.8474 | 2025-11-17 00:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d506cd2c-9f61-33ed-95d6-2a946d6353c2 | -6.6687 | -42.0314 | 2025-11-17 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 255.3 |
| 6b77f655-5fd2-32f0-a859-661c4ea7ac97 | -11.8299 | -49.2024 | 2025-11-17 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a7c7ba12-eaee-3078-8544-377341e794c8 | -6.7064 | -42.0278 | 2025-11-17 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| a4093ec4-033e-3f4f-8555-8ad80bbe86d2 | -3.2343 | -50.5162 | 2025-11-17 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| efd9a8eb-a999-3bfc-8d2c-4ec3fe470ae0 | -5.0401 | -43.5973 | 2025-11-17 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7d825eaa-9eca-3d58-8d8c-79e23bff0be0 | -7.9714 | -50.0013 | 2025-11-17 00:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c9da9342-31e8-30ac-af0a-b33507700dec | -10.8936 | -44.6378 | 2025-11-17 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 37192ed1-c0ea-3dc3-8c1c-b6f9c8cf7b0a | -11.7017 | -48.8692 | 2025-11-17 00:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 26afc374-8877-3113-9b2a-f475d696b430 | -16.2441 | -46.9561 | 2025-11-17 00:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1a390a60-d878-33a1-bd3e-97496123f309 | -11.7208 | -48.8669 | 2025-11-17 00:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| abb4c0e6-a177-3a15-a318-9828dd2b10cf | -2.5238 | -47.8115 | 2025-11-17 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 97929f7d-9912-33d9-a4be-b423447e0ce8 | -2.5053 | -47.8337 | 2025-11-17 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| d25b9e78-228a-3795-a544-2d48513ad74b | -10.6687 | -49.3813 | 2025-11-17 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 26716533-f34e-32db-9959-ebf1ce78542f | -10.894 | -44.6146 | 2025-11-17 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 0c6001e5-0e3f-3c56-8e95-d37f9bac4522 | -2.694 | -52.0653 | 2025-11-17 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| ad9735c0-2258-39a9-8384-a525a7f1cd89 | -4.9967 | -44.3607 | 2025-11-17 00:00:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7473b26c-47d8-340c-8432-cd229702c5ec | -2.6756 | -52.0657 | 2025-11-17 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d08da4c8-768e-3f11-a02b-45815f3aeeb9 | -6.6873 | -42.0535 | 2025-11-17 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 340.3 |
| 43567940-92ab-337e-b7e3-2616ff733618 | -9.577 | -49.107 | 2025-11-17 00:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| eb19cfaf-9573-3049-9c82-97adc298b326 | -3.2344 | -50.4952 | 2025-11-17 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 921e1869-04f3-3ec1-b48d-cfcd88cd3a84 | -10.8745 | -44.6404 | 2025-11-17 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 0d1f6e4a-0ea3-3145-b61e-8f7228d42c02 | -3.7193 | -45.9215 | 2025-11-17 00:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ba92f045-bab1-3b6c-b48c-49f0405d4d3b | -2.2483 | -53.6216 | 2025-11-17 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 036f6a29-b43a-3e72-80c8-fabb527e0eac | -11.8295 | -49.2242 | 2025-11-17 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 597a5bbf-20b9-3f79-87b6-69ec6b4df2dd | -10.669 | -49.3597 | 2025-11-17 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 13950d8a-0e2f-37c5-a285-4c7b21a8e150 | -2.5053 | -47.8337 | 2025-11-17 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| a36d63f3-51e5-3488-b165-a0fde9c02631 | -2.6756 | -52.0657 | 2025-11-17 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 9a0848a3-ce15-3038-804b-0d6c97f8bb41 | -6.6687 | -42.0314 | 2025-11-17 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 219.6 |
| 8af963f3-34e4-301d-80f8-c6758eb772f7 | -10.8936 | -44.6378 | 2025-11-17 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 68f7bba1-e602-35f1-8c0e-284c8d1f4a5f | -2.5238 | -47.8332 | 2025-11-17 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| f0eb1ef4-20fe-3855-a6c7-e1d739c134fb | -3.2343 | -50.5162 | 2025-11-17 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 10a0d6d1-80ed-381d-8ac6-d18bb7bb49fb | -11.7017 | -48.8692 | 2025-11-17 00:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e7556390-4467-3cda-94a7-5bea8b465afb | -4.9967 | -44.3607 | 2025-11-17 00:10:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c6951673-00be-3ec1-8444-743b867bcfda | -10.8745 | -44.6404 | 2025-11-17 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| cd716489-a2e1-36b5-9c08-9ede96660c74 | -11.7021 | -48.8474 | 2025-11-17 00:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| da89576c-db68-3b6d-bd1c-9ba1bb1dbbae | -8.5418 | -46.0607 | 2025-11-17 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 729620ae-8fcc-3645-9b5c-076b93d1371c | -11.7208 | -48.8669 | 2025-11-17 00:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| aa1a4be1-2d20-31b0-a261-ac41338fae90 | -10.6687 | -49.3813 | 2025-11-17 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2d95ba7e-46d7-3748-b23b-ed11d6c05b14 | -11.8486 | -49.2218 | 2025-11-17 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| d3ec3214-53a0-35ca-a495-f87a2aaf50db | -6.6875 | -42.0296 | 2025-11-17 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 601.5 |
| f25bca21-fba0-3efe-97f5-ca181a9286a7 | -3.2344 | -50.4952 | 2025-11-17 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| a14fd70f-65aa-3001-93e1-a35ba01dceb3 | -4.1596 | -50.2098 | 2025-11-17 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 22f06d5e-e5a7-34d1-8813-580096130e8e | -16.2441 | -46.9561 | 2025-11-17 00:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 721f9483-b5a6-37ea-99ea-6858a6a8a4d6 | -2.694 | -52.0653 | 2025-11-17 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 52de2037-3c5c-314c-8872-4ef432a0acb6 | -4.1781 | -50.2091 | 2025-11-17 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 952f9c0f-8eaf-3587-bbb7-46ac5daefa60 | -2.5238 | -47.8115 | 2025-11-17 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| ca8be45f-928e-365c-9973-4989a9d495d2 | -7.9714 | -50.0013 | 2025-11-17 00:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f0795724-79fd-3f84-9ef1-315a5a577b4f | -11.8299 | -49.2024 | 2025-11-17 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7388b5cd-0bfa-3618-91bb-f715116e34d1 | -6.6873 | -42.0535 | 2025-11-17 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 316.6 |
| aee1c030-ad84-3935-aa01-df5a22148605 | -3.7193 | -45.9215 | 2025-11-17 00:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 145.1 |
| b639f3d2-fa32-3fd0-ae99-072b98ff39fc | -11.849 | -49.2 | 2025-11-17 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| dca2fde1-2f37-3bc9-b885-f3f632b3aad4 | -10.8749 | -44.6172 | 2025-11-17 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 362c0d6c-defe-312f-98ef-a8f819fc1bd5 | -6.6684 | -42.0553 | 2025-11-17 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| c2ef04fc-dab6-3d7f-8e39-97b5b161c966 | -2.5053 | -47.812 | 2025-11-17 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| a2d807a7-d3b0-3cf7-9611-c88136f2ba5f | -10.8749 | -44.6172 | 2025-11-17 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| aebab31f-b472-39ed-b9bd-90c8acf9de42 | -3.2343 | -50.5162 | 2025-11-17 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3fbf3ccb-3584-3c8e-8bbb-409d9b614594 | -10.6687 | -49.3813 | 2025-11-17 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d904b5aa-c577-3f10-aedf-dd4f7cef5aab | -7.9714 | -50.0013 | 2025-11-17 00:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0eaa8dcf-7b12-3c9a-b2df-04e256644592 | -10.8745 | -44.6404 | 2025-11-17 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| dc31de81-ffc7-32d1-85ea-3976e3486f92 | -11.8299 | -49.2024 | 2025-11-17 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b5aed5e8-e013-37f2-9844-661bbfb34b07 | -4.9967 | -44.3607 | 2025-11-17 00:20:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| c194e2a3-904f-3d5f-8dc4-e151ea613e18 | -11.8486 | -49.2218 | 2025-11-17 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 4feacc72-1722-342d-b7e9-7f1665a0ef00 | -2.5053 | -47.8337 | 2025-11-17 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 240b8065-a6e4-3178-85d6-d89e2184b376 | -3.2344 | -50.4952 | 2025-11-17 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 172f8414-25c8-378a-b709-8485243e2363 | -11.7017 | -48.8692 | 2025-11-17 00:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 3507cb8a-b6fe-354d-98f1-26146454cd23 | -6.6878 | -42.0057 | 2025-11-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 7bdf504d-8d78-3806-b1ec-4737c0a04b4d | -2.5238 | -47.8332 | 2025-11-17 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 88d4c807-249c-3e56-8030-1660a784013e | -11.7021 | -48.8474 | 2025-11-17 00:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ccbfb6a2-d820-3e54-839b-bc452e856840 | -2.5238 | -47.8115 | 2025-11-17 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 936122f5-8153-3623-a350-7c225af1c35a | -11.849 | -49.2 | 2025-11-17 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 1f46d2fd-53c3-3dc2-845b-ffde627c68af | -3.7007 | -45.9223 | 2025-11-17 00:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d1cabebb-00d9-3f16-8e92-19f5f8b66900 | -6.7064 | -42.0278 | 2025-11-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| f7ae787a-0e9a-3bd6-b711-a580a3219e5b | -8.5229 | -46.0626 | 2025-11-17 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 7f692529-4977-368f-b6df-11a5b268153d | -6.6873 | -42.0535 | 2025-11-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 278.3 |
| eb161d5c-4d58-3f7c-8684-c6bbf8cc61b0 | -10.669 | -49.3597 | 2025-11-17 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 550ffd7f-02cd-3b86-9f8f-a4d3d87a13d9 | -2.5053 | -47.812 | 2025-11-17 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| ac553ecb-0305-3cc0-aa36-bbea474b8173 | -2.694 | -52.0653 | 2025-11-17 00:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 1220ee2b-61bf-3b29-b3fd-8178ce02a335 | -4.1596 | -50.2098 | 2025-11-17 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f53d0884-c239-3b11-a7d4-501ad41c6fd8 | -11.8295 | -49.2242 | 2025-11-17 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 69aaa7e3-f3c2-3bfb-aa19-cf7fb266ca8e | -8.5226 | -46.0851 | 2025-11-17 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bda407aa-bcca-39f4-876c-1e0d295f7dd1 | -20.3302 | -57.7806 | 2025-11-17 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| d9c2a323-12aa-344b-a69f-d34e9d47c468 | -9.5152 | -40.331 | 2025-11-17 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 8441a586-f6d1-3694-a6bf-8ef9ca6dad19 | -4.7209 | -46.3832 | 2025-11-17 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e2fc1f6c-a42c-3b2b-ade8-8e2392f57331 | -6.6684 | -42.0553 | 2025-11-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 4e4ef02c-1e75-32ca-9490-59b3b356f4da | -4.1781 | -50.2091 | 2025-11-17 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 15400b84-0c18-39dd-8238-16622bf91a12 | -3.7193 | -45.9215 | 2025-11-17 00:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 139.8 |
| e8f01eb2-4cb5-39b9-988a-420cdb935042 | -6.6687 | -42.0314 | 2025-11-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 226.0 |
| 269ed3af-295e-3f8b-9ecc-5b8be6a1a328 | -10.8936 | -44.6378 | 2025-11-17 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |


[Clique aqui para ver as próximas entradas](README2.md)
