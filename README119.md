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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7855918f-87df-3111-ac83-503c03460d42 | -18.81735 | -53.76537 | 2024-10-05 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c1e8beb-6d6b-3d9c-b0fa-20623c0a71e4 | -18.81672 | -53.76917 | 2024-10-05 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8992408-6ccd-35b3-9e04-48afad7ed351 | -18.81335 | -53.76855 | 2024-10-05 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b3c07b9-ff8e-306f-85ec-072b9c6c150a | -18.78321 | -52.63423 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 901b1509-bc88-32b6-bc87-d595c4061f46 | -18.50099 | -52.84719 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f6fa502c-8d7a-32eb-9a96-5d4a24575153 | -18.5004 | -52.85085 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1b5909cf-96df-31ea-9cc5-d5e4c990ff58 | -18.49981 | -52.8545 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 15039712-4066-3a8d-9281-5faf29a5b3b6 | -18.49887 | -52.77553 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6f6d18c-d235-32ae-927b-21c75472e3aa | -18.49708 | -52.85026 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 41c489e2-3cdc-3e39-b1c1-17c2729db15e | -18.49649 | -52.85392 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 183b455b-7c1e-35f2-b7b4-4e78bbfeeba5 | -18.4959 | -52.85757 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 8fa3f2a4-a6bf-323f-a93e-7183505ceae5 | -18.49555 | -52.77494 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7825e969-242a-3a2e-a5c6-e0a82fd99bbe | -18.49531 | -52.86122 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e9f8ed9-d4df-3b4c-a9b5-f04513ea4ac5 | -18.49496 | -52.77859 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9a092408-f8e6-3de9-b66a-6bc312270fa0 | -18.49417 | -52.80471 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 041840f8-a990-30b4-9825-376d2a5f33a7 | -18.49317 | -52.85332 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 48a5076d-8343-3f8d-a5f5-33710e25ba61 | -18.49258 | -52.85698 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| df182d36-738a-3603-95ba-d63c08cea473 | -18.49199 | -52.86063 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 29fa4c2a-4923-3a38-a654-46e2286ef528 | -18.49106 | -52.78165 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caa0ffa4-9095-356d-a0bf-51abb39c9573 | -20.47843 | -53.67479 | 2024-10-05 04:40:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db8f6ee-244e-3e2a-b16c-6f8d70ccc3cb | -18.67678 | -57.27721 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 85356d6c-0da3-3350-ade7-07585f990c42 | -12.70412 | -54.11332 | 2024-10-05 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5afb5764-0044-3065-afb5-dbf42267dace | -12.70122 | -54.10838 | 2024-10-05 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 487c8ce0-8dbe-33c8-a9d4-e8e4e9fa0ecf | -12.7005 | -54.11267 | 2024-10-05 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc118ff9-3969-3fa9-b483-5eb090144e4f | -12.69761 | -54.10773 | 2024-10-05 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4679dfd-0f96-382a-86f0-4a2dc6e421c2 | -12.69398 | -54.10711 | 2024-10-05 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2949ca53-cfdc-3728-9712-ace085d455d3 | -12.69108 | -54.1022 | 2024-10-05 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94b9c6e0-66a7-3d44-be17-c495ce09cd85 | -12.69036 | -54.10649 | 2024-10-05 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56bfbb38-db3b-37b4-aa15-c5a320e9a93b | -18.88984 | -54.52787 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 552c7af4-49c0-3b4d-b8eb-62db82a03a15 | -18.88848 | -54.53586 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a33bf5c6-963e-3c52-b9d3-da7d35afb932 | -18.88779 | -54.53994 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59290117-3cdb-3cdb-89d5-5839f858e63d | -18.88571 | -54.53122 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c3d8ab9-cd85-3e67-944d-c63df773582a | -18.88503 | -54.53527 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 605cffec-4251-36e0-9857-823d9b6586b8 | -18.88433 | -54.53935 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65f213c5-0d1c-3aa3-80b9-6e1e96e91fda | -18.88342 | -54.482 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 881245be-eb1d-34c6-9fed-da5f955bab84 | -18.88276 | -54.4859 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d90b6880-02c1-32b5-9b46-5d422c4e2243 | -18.88228 | -54.53053 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e7961a4-a85e-3f98-9cb7-7c2a5a852e60 | -18.88087 | -54.53875 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93ab09a1-6769-3b66-9333-05baf343648c | -18.88064 | -54.47751 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f32bf53e-076a-3322-8652-d47da7e0a44b | -18.87997 | -54.48143 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7747ef0b-e355-36f0-a5c3-44125089d707 | -18.87952 | -54.52583 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d929eae3-0be8-3925-a154-cefb7936ea64 | -18.87814 | -54.53394 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8592a513-1672-3bf5-81ec-cdf2ac95e7fe | -18.87744 | -54.53806 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96602854-ed84-322e-b55c-8ee5c8a39ac8 | -18.8772 | -54.47689 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13808014-0f3c-3952-9fc6-f1ce119c402d | -18.8747 | -54.53321 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5040f20a-d36e-3152-b716-8182bb7cb7c1 | -18.87402 | -54.53725 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b3470e3-16b5-3432-9ee7-1426b8a59468 | -18.87331 | -54.54138 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2ff5f73-3b7e-3d7f-b5de-408518e0b902 | -18.86987 | -54.54067 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32682916-bd96-3043-9736-e3f9d6698801 | -18.86779 | -54.53202 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a76ea2d-fee0-30f9-891a-737fb91566da | -18.86431 | -54.53156 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0759cc3f-7d3d-357d-9a2f-15272217a5d9 | -18.86364 | -54.53553 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86b210af-ed8f-3e03-a732-e5987c9fa87e | -18.86295 | -54.53957 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b05c5f31-1c94-3bb3-ae03-1bd874671d0c | -18.86225 | -54.54363 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abd5b344-d598-3bc7-b211-2d185bfd1450 | -18.86219 | -54.52315 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a517f91d-9ac4-3acf-99f6-0fc18a4780c4 | -18.85892 | -54.46616 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c449e96-82c0-3604-a8d5-1a94c835db48 | -18.8588 | -54.54301 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5785549e-c7d1-3afb-9843-aad5f0d4fd38 | -18.85874 | -54.52256 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8c7a493-0ad8-35e0-b1fd-26056e0c052c | -18.85826 | -54.47016 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45643548-acbb-3d13-8d40-51013c79afc8 | -18.85806 | -54.52652 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e10b385-f3a8-3ec5-9b6c-ffc36154b817 | -18.85528 | -54.52196 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24d1b6eb-2662-3be3-8a9c-5a6245abcdaf | -18.85482 | -54.46947 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3869914-9129-3d3f-ad6d-54da13ef7587 | -18.8546 | -54.52592 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c23b3af-ced7-3ba4-826a-6f726cc65cb2 | -18.85304 | -54.52262 | 2024-10-05 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66db6db9-b2f1-32df-9313-e335dc307ba9 | -18.85205 | -54.4648 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3153cad3-8344-3140-9a3b-3bb4bb91768b | -18.85139 | -54.46874 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f39999b4-1905-313b-b200-e51809ffd20e | -18.85073 | -54.47267 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 451bda14-c7ce-3960-ae03-7aab45607ee5 | -18.84731 | -54.47191 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbd35b77-5814-3529-9bc2-b5420f983d81 | -20.13282 | -54.49199 | 2024-10-05 04:40:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23532257-df4c-3514-946a-cc143d3b5b6f | -12.68897 | -54.66825 | 2024-10-05 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1672eba1-19a8-30ca-b6a1-7387fba32ebe | -12.65959 | -54.70502 | 2024-10-05 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98591af6-75e9-339c-8e61-07ebb77e6644 | -12.65387 | -54.67125 | 2024-10-05 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 688e0490-c6c8-3ad0-8530-83afab9ddf9d | -12.6529 | -54.69917 | 2024-10-05 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf8e7f57-ea77-3e08-91c2-e79a47249d5d | -12.65211 | -54.70372 | 2024-10-05 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 022238cc-8ca3-30d2-97a2-b0dca65c843f | -16.65901 | -55.52163 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4ae551bb-8f6a-3fbb-bc41-55d09349ceba | -16.65871 | -55.54509 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 084db7aa-2a1a-3675-bf25-b0c7d89f718e | -16.65849 | -55.50288 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4c1d24e0-6997-3e6c-88b4-5d2e229a46f5 | -16.65745 | -55.53046 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bdef21f1-cc64-330d-8bb3-e8df1083c8ea | -16.65585 | -55.53961 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 00c7eaa4-fd10-30ba-bea6-07cf0ecd8d98 | -16.65479 | -55.50219 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5eebb438-053f-30a1-b6b4-6e2a37d57baa | -16.65399 | -55.50674 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8f563dc2-78eb-3dd3-9854-30ee5cc8763b | -16.65376 | -55.52976 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bbb5056d-9602-3088-b94d-a26c20ceb947 | -16.65214 | -55.53894 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5ba0c15e-eb18-3cc1-9561-e8b2b322a58f | -16.65082 | -55.52477 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 940b1711-7911-3477-8eae-2d44046cc146 | -16.65003 | -55.52924 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8b99e48c-1cfe-34d3-a9b4-bfeeaafe85d4 | -16.6495 | -55.5106 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c25d1a46-e117-3176-b4dd-b07ff0015a3a | -16.64923 | -55.53378 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 479d9f51-4bdf-3466-a314-2f1cb75923b1 | -16.64789 | -55.51969 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 65d02d5a-ddb1-302b-9e3f-e628407f7901 | -16.64661 | -55.50534 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 084b5b68-fdec-31a5-8d77-42c63f2c8eb6 | -18.67283 | -57.2764 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 4fc4ea66-3283-3839-a444-59c24c0feab5 | -16.6458 | -55.5099 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 05f0b734-8f8a-33e9-9a41-8883d7fbe31a | -16.64339 | -55.52355 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c8ee979d-85e1-3ec0-bb9b-7c9628cbe64b | -16.64292 | -55.50464 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3d0aa7b3-bdae-3eee-9c74-055b002242a7 | -16.64211 | -55.5092 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 20d68052-ef88-3904-9a31-96121d33cb62 | -16.64131 | -55.51375 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9210f696-652c-3d7d-b4a0-2eac0205cddc | -16.6389 | -55.52738 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 527f5d47-0c89-3ef8-80f1-c0b56469b4d6 | -16.63842 | -55.5085 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 396fec9a-64dc-3bd2-b427-671ff55b1bb9 | -16.63761 | -55.51305 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 25baf294-4730-310e-9c4f-80de2d37e933 | -16.636 | -55.52216 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 25dbf87a-5121-3a47-a407-2d19cab29305 | -16.63519 | -55.5267 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 53bb4d50-b44d-3415-b7ac-2b2599e05075 | -16.63473 | -55.50779 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README120.md)
