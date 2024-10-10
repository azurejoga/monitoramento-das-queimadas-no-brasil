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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b80a1791-da7e-39a8-846f-5a4e0e22199f | -10.37104 | -61.25854 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efb28c9f-6859-3736-9007-645fc4073be4 | -10.36989 | -61.24076 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5e15184-99e8-33c9-a810-83434ad48a3c | -10.36926 | -61.24516 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5868fa90-790f-364a-b16a-fb12667a0423 | -10.36864 | -61.24941 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d662bb2f-488a-3de6-9b77-2cdba104f433 | -10.36803 | -61.25365 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c0a6fc7-8fe3-33f7-bdfd-a71957a924e6 | -10.36741 | -61.25798 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 166155ee-a939-3cf6-b091-c1e4d075cdee | -10.36688 | -61.23578 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23383925-5f0d-3b95-b7ab-f81ab5cd0cfa | -10.36626 | -61.24012 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 030a6a0d-160f-3177-a45e-e7cd74254dbe | -10.36564 | -61.24447 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d8d3023-07db-3a40-8938-bd962b181afa | -10.36502 | -61.24876 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b41fd0-3f90-3581-8f5e-1e1206035efa | -10.3644 | -61.25306 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3eabde0-7871-3812-91a5-e89fac1d477c | -10.36377 | -61.25743 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdecd317-83ee-3e24-8bec-24060e9c9d70 | -10.36325 | -61.23521 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc75e5bd-4c91-345e-848f-9ababb7fedfe | -10.36263 | -61.23951 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4c6ad7a-686b-3b81-90b8-2f0b0a7915c1 | -10.36201 | -61.24381 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 759bb926-cde3-3e60-9b67-5d188857af39 | -10.36139 | -61.24814 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40b7dbca-e693-3cfb-9612-16f96c42da3e | -10.36077 | -61.25247 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f135f39-6224-3861-a67d-797e5a986198 | -9.94845 | -60.13445 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bceeb4ab-d9ae-339a-aa3e-e7db0cd14501 | -9.94774 | -60.13931 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 965af2ef-8311-3451-ad3e-dce6f2a04f96 | -9.94634 | -60.14897 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cbc92b8-581d-35f1-b17f-0d76be5b4197 | -9.93094 | -60.09192 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d5b189f-6d65-3824-b132-6e8c70dabc7b | -9.92719 | -59.83838 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 277da14e-b937-3290-b7d8-00ac6c3d2802 | -9.92484 | -59.94007 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 371856c0-2153-3aee-b6a8-3c0c63dd593a | -9.90349 | -60.30948 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7fd8bcf-3a0d-3f80-aa6c-abe63471c5b5 | -9.90312 | -60.28513 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97a99ea8-1fbd-3388-a13a-61ac6e5d8184 | -9.90198 | -60.21151 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 570efdec-b3af-351a-9482-207734c86df8 | -9.89815 | -60.21093 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14b26491-1745-3baf-b137-edcb71bc6f5e | -9.88922 | -60.27328 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21461bc4-3d32-3136-aabb-ab3d5a5c98df | -9.87205 | -60.11802 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36ffc345-3939-3d36-9278-b778e2489cdd | -9.86502 | -60.11199 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3379ccf-d03a-3264-945f-29805c7565b6 | -9.86338 | -60.31778 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f8ef696d-8c8a-33e4-a65e-89b4af5e3e2d | -9.86325 | -59.83769 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 893437a3-caaa-36a2-a192-7af0ff672655 | -9.86271 | -60.69494 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 750457fa-58fe-37db-89a8-3d40f5355fcd | -9.86271 | -60.32251 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 788ade7c-7864-345c-8d9c-abe36306b0de | -9.85899 | -60.69436 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6e9b4d5-de86-323b-b76d-f240c4eca724 | -9.85676 | -60.12896 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c14d29df-095d-3edb-b519-dbf97ff41807 | -9.85624 | -60.21262 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce1d2a62-c053-3f7e-9627-8b2f096910c4 | -9.85552 | -60.21744 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fe3bbc8-def3-3ef6-9413-eaae3a22ce09 | -9.74609 | -60.40858 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a143543e-a4d8-3d4c-ba72-70b618ca3ea4 | -9.72051 | -60.74473 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84d265bf-eb45-3172-8273-b697fa07cae5 | -10.46303 | -60.10134 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e03dc49c-aedd-33a3-8d63-cca1b86cd1c2 | -10.45912 | -60.10091 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1485b96e-a362-3524-8dd0-3feab8897599 | -10.45842 | -60.10587 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d14f8c3-49ac-37e0-b8a6-d60e9931a210 | -10.432 | -60.9918 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b22a64-869b-315e-b347-73b5318bf7a4 | -10.43135 | -60.99631 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1892c853-d9fa-351a-bd93-91269112dd53 | -10.43072 | -61.00069 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ce7acb2-293d-3058-9cb6-915b2b47496e | -10.42831 | -60.99127 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccfdc012-d591-3ced-9e80-af3fa45d135d | -10.42766 | -60.99579 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffa37fa1-1f0e-39ec-902b-93df537f7894 | -10.42702 | -61.00016 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 507f46dd-eaf5-3da0-bc82-3fc8acdbe676 | -10.4264 | -61.00449 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 674f2a81-242c-3cd9-aa60-e4ad9397a119 | -10.42398 | -60.99511 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a721b138-0e69-3457-9b93-0371322a56a6 | -10.42335 | -60.9995 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890d65ad-46b1-3925-99d0-19193f8f84d1 | -10.42031 | -60.99442 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cafe82a6-714e-3317-a05d-b9f5d36bd00a | -10.18479 | -60.89754 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5496ce14-2f5b-3c04-940a-d788bc312869 | -10.18412 | -60.90201 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dc8be10-42c5-30bb-94a7-343b7eaf4f79 | -10.18379 | -60.89571 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06f68969-e27d-3c08-b1b1-b6df8ee92390 | -10.18316 | -60.9002 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ba4d3de-0035-311c-97c9-a8ef5352b4bc | -10.1811 | -60.89692 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d30955c-e04b-365f-9ac7-00c647983bc4 | -10.18045 | -60.90133 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cee57321-ad9e-320d-a861-60a50ac038ac | -10.18011 | -60.89508 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8652d6ac-e5c3-36a0-823f-6407b16a12b8 | -10.17947 | -60.89956 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f22a032-c5a5-31c6-ba9c-66c126cba13a | -10.17676 | -60.90069 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b8ab76b-2467-3642-8c31-a90b94a48823 | -10.17308 | -60.90005 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67d12497-76da-3ef0-b765-9084e04b3822 | -11.54158 | -60.29449 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7941ba9-15fd-3b0e-b2ad-99c7a25489ec | -11.54088 | -60.29943 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72e66364-053e-3803-b81f-515824ac384b | -11.45417 | -60.43747 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a7cc918-e7dc-3c4d-bc1e-fdb30ddb89af | -11.40584 | -60.40413 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 283789c7-52fd-3c02-8aa3-9e0be162e386 | -11.40197 | -60.40355 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bef13571-1d32-3980-83ea-53bb77b205be | -11.40129 | -60.40837 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2087ca9-0796-3f87-a563-1a2ac13921cf | -11.4006 | -60.41322 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a55d6cb-bfb9-3a44-a270-b5d62263b2d0 | -11.39741 | -60.40785 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ab5e510b-8dc0-3ff6-a6a1-bfe7ff741285 | -11.39672 | -60.41277 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef6462ac-3177-36b8-a466-fc8ace0e28c1 | -11.39604 | -60.41752 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62f70e6e-565d-3b40-973d-f40fad2be6c2 | -11.37198 | -60.58711 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b99d05f3-06d7-3925-a240-0c55c3e49bc9 | -11.35558 | -60.56504 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9b909ed-bc30-3f20-b52c-2927a23c99ff | -11.35175 | -60.56451 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf858911-8fd7-36e5-b6c3-22d8ce591821 | -11.34793 | -60.56391 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e81a289-3353-3de1-af93-f2a296789475 | -11.34724 | -60.56881 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0d98fab-d84d-37ea-a762-d979e08c9dd6 | -11.34341 | -60.56826 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a85acf6-ec20-3b45-bc20-9eeb07cf1439 | -11.311 | -60.54845 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 405f1bf6-22c3-39ea-accb-e63aa2861222 | -11.2838 | -60.33455 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4a1cd54-0827-351e-a0d7-a74c941a0cda | -11.27418 | -60.40292 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b9d34e6-ded0-3617-8468-326c30dcfb44 | -11.27335 | -60.49228 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64a5bbaf-7248-3ed4-b2ee-336f544486d5 | -11.27097 | -60.39772 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61cee7bb-6398-3ebd-9457-3ffe39d4b97c | -11.2703 | -60.40251 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bc6eeb1-2b49-3b87-ae62-50a621b03eea | -11.26951 | -60.49169 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 512a9db9-85d3-3aab-bf0b-99c79b0053cd | -11.26882 | -60.49656 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8bfa891b-37c3-32f3-bd88-bc25c3901289 | -11.26665 | -60.37234 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a9e799-26ec-34aa-a98b-01ef92d93f0d | -11.26646 | -60.4018 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37749849-710c-338f-aa0e-a45e3dfe093a | -11.26637 | -60.48618 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b42bdd9f-499c-36b6-8256-b2487d9599be | -11.26579 | -60.40654 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d3158ab-1082-33ec-8270-6dd0d71dc899 | -11.26567 | -60.49113 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15cdda96-8814-3b94-90ba-aa4fcaf2f029 | -11.26498 | -60.49602 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bbc061e4-0806-3c6f-ad71-228392540616 | -11.26277 | -60.37183 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed76243e-876e-348f-8edc-a67ac6216ff6 | -11.26262 | -60.40108 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8140df8-7327-307b-88fb-831ba9260cf3 | -11.26195 | -60.40582 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9731dc8-a951-34fe-8d69-004b20a0d3a2 | -11.26114 | -60.49549 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42b8276b-8005-389e-ae8a-d8592c6f7396 | -11.26045 | -60.50035 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d432fb8-0877-39a4-835c-eb67108f8cce | -11.2581 | -60.40515 | 2024-10-10 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbd43b04-1577-3acc-ab2a-c7e13d0ba54d | -11.25618 | -60.55822 | 2024-10-10 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README138.md)
