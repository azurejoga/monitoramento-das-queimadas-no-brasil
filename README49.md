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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28b38067-33e9-360f-8d35-f14ac29ac0cc | -15.56668 | -56.90873 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64f03795-9dea-3fd8-ba66-d7c4cf94d1a9 | -15.56588 | -56.91293 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9985a775-3e3e-301f-93ad-40c1188f1517 | -15.56509 | -56.91706 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f17c3b8b-9aba-3330-958c-b0194ae1191f | -15.56222 | -56.90751 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d05c926-daa9-3a6f-907e-800c5c08591f | -15.56145 | -56.91152 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d8459d3a-0c6b-36a2-8d98-da9d2631dcd8 | -15.55704 | -56.90998 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cc511eb5-c02b-3c06-8cf2-9060868161e4 | -15.5526 | -56.90865 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09b52459-0787-3665-9734-32f2fa5b0189 | -15.54814 | -56.90743 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ecc56e5a-10b3-3124-aa91-05c0083eb33a | -15.54368 | -56.90621 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d1e2bc1-5312-3312-bd5c-0535b95e85c3 | -15.54277 | -56.91095 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82d32c23-32c1-39d8-8e71-96084e0c181f | -15.54185 | -56.9157 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fe335d3-39b4-35d5-98db-a86066538bde | -15.53917 | -56.90524 | 2024-09-30 04:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37a411ae-0230-303a-b46a-d0ff8a9cb9a2 | -15.943 | -57.19235 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99186b10-ac57-35fb-aa98-bf3737bb2d7c | -15.94213 | -57.19685 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3a56305-19ba-3fab-b2c3-607c116807c3 | -15.93846 | -57.19124 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdf9a237-336c-3a7d-bca3-fa1fc696fa28 | -15.93224 | -57.19881 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0e255a4b-b4e2-3d15-b727-8ed91c97dcb8 | -15.92939 | -57.18894 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7349d822-2597-3826-8b13-30686e7fc830 | -15.9286 | -57.19304 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8ee323b-7fed-343f-949c-1399ba90d2e0 | -15.92775 | -57.19741 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92e8526f-fd3a-3230-b44e-21892fa53a1a | -15.92573 | -57.18328 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7965c7b9-910b-35fa-a23f-fe17c7eea81c | -15.92494 | -57.18738 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9756a20-cd2a-37cb-8bca-a60734fa03ae | -15.92122 | -57.18206 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 266a27cc-a1d5-396c-ab84-6051aa9ad705 | -15.92046 | -57.18593 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f673bee4-f360-3a1f-a7a6-84e8bd16a63b | -15.91755 | -57.17941 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fb435497-4854-34cd-bba4-99dbf343ee17 | -15.9168 | -57.18337 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e29fcd2f-0f37-368e-9ada-88257dfd8fb6 | -15.9167 | -57.18082 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4dcaa10c-3cd5-32a4-b384-1f7d99f6a84f | -15.91594 | -57.18473 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ff0d5eb-64ec-34d1-9ecc-7accf616bf8b | -15.91468 | -57.21569 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1481262-dfb5-3308-87e1-b02f26aa40e5 | -15.91231 | -57.20744 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37c4f082-1447-347f-a2ec-014b9f18afe5 | -15.91229 | -57.1821 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4eab8121-747d-3fc9-b4d2-326656216a1c | -15.91221 | -57.17946 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9162a29b-3fb2-3f99-b5ce-133b85103943 | -15.9115 | -57.1863 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 99f695fc-d3e4-30ec-addd-32615ccc2149 | -15.91141 | -57.18357 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e9a6d7be-873f-345c-aba9-aad6d1ae128a | -15.91128 | -57.21294 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f35b3378-862e-303d-8d18-f96950d03da9 | -15.91113 | -57.20946 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bec195f-3698-34fa-ba64-b3b3178c09e6 | -15.91057 | -57.18789 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cea33ee-4b4a-3aac-b0ba-b8c13f73e610 | -15.91013 | -57.21458 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0baa11ef-657e-3ab8-9368-1928e7175d5b | -15.9077 | -57.20663 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31675b7b-3bbb-3a36-8822-27212592b0c3 | -15.90691 | -57.18542 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73e86372-eb0b-36a8-817a-47f41e4e172c | -15.90673 | -57.21184 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e549782-4926-36d9-93af-0c26d7f0dabb | -15.90655 | -57.20852 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14b4100a-35b7-3c98-9b9b-f31cc4b67430 | -15.90603 | -57.19011 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6ba5fdb-d0ea-3bae-a964-507e448686a4 | -15.90596 | -57.18712 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20393932-3c4c-3feb-a243-ed510d519ed6 | -15.90559 | -57.21344 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77475c2e-4ded-317b-84e1-ccf2fb529da0 | -15.9031 | -57.20581 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0127b50-6d26-33f3-b847-f3f0ae018a34 | -15.90298 | -57.20242 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 912cea6d-7f67-39d8-8565-06cfde925915 | -15.90198 | -57.20753 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d72b8206-6250-3687-b8c5-388504e5f9a6 | -15.90144 | -57.18924 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd48f9b0-2ed8-37cd-83b4-f00705d83dee | -15.90051 | -57.19423 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a44e1c21-8926-326b-8020-4af1b3f500f3 | -15.90044 | -57.19102 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b85c0b07-77ae-3a0c-907c-2332df875cc4 | -15.89951 | -57.19953 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b766948b-abfe-3ecf-b5dc-3a76def2b2ea | -15.89944 | -57.19613 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1bf44c84-2338-3913-b324-ce21c11c6335 | -15.89853 | -57.20477 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a64bf887-c027-3797-9831-2a328add6160 | -15.8984 | -57.20147 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64e181db-e86b-3563-8718-eaa5814ddfc6 | -15.89492 | -57.19866 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ce964f88-c29b-3d47-aec5-9309dc9892d7 | -15.89383 | -57.2005 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c8832169-5b11-3b7d-953e-f7b55fd76eda | -15.89035 | -57.19767 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c377096c-8d27-39d5-abb4-d09928923101 | -16.51783 | -57.35524 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2ba40360-9ba3-35dc-9072-7d2bfd50b72e | -16.51781 | -57.35213 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 09c25c9e-83f0-32ee-8368-97b7bb12003d | -16.5169 | -57.36015 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 57c9cdb3-4327-30ee-808c-b63f59dd3340 | -16.51684 | -57.35703 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5d3ac0ac-7776-3d00-ae92-8cc56b7005d2 | -16.51327 | -57.35424 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 699b3409-13ab-3334-9505-ab3be4ffce0a | -16.50869 | -57.35327 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6e44e5e6-829e-3ac3-ae0b-0b70b74279c1 | -16.50412 | -57.3523 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0008654b-8ad3-3c6d-8f4e-bfcbd635a1a8 | -16.50319 | -57.3572 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 12538705-d414-311d-8a4c-d142064c58f6 | -16.50225 | -57.36211 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 23bbfd53-5e26-3ac2-8562-5815417ac383 | -16.49768 | -57.36114 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7a6dc606-b846-3554-9061-64ca38958c5c | -16.49123 | -57.36998 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3ef3b756-f97a-30a2-ae2a-30f480429877 | -16.48665 | -57.36901 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d20ee972-3cb6-3cb1-8ab6-29fe61ceddb9 | -16.48289 | -57.38867 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 89e5a18c-314e-356c-9cf9-db3213f9e5d5 | -16.48194 | -57.39361 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 638c38a4-ef0f-3412-8240-3ed267d66a9e | -16.47897 | -57.43406 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a00510c5-5d53-305d-883d-e54f60ef9c72 | -16.4783 | -57.38769 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a5d16a8d-2bb7-38ee-8f03-78a37c307a40 | -16.47735 | -57.39262 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f263a5e3-4da2-3be2-b43e-627e7d726242 | -16.47438 | -57.43307 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| eb1a58a1-e9a9-35b9-9a33-be3f00312b9e | -16.47372 | -57.3867 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e3dde348-d633-30a4-814d-148d15ca5516 | -16.47277 | -57.39165 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8eff0450-7cd2-3c8e-ad96-277f8ebc4a13 | -16.47197 | -57.37101 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 472ce517-854c-3e28-9110-169abd40a608 | -16.47182 | -57.3966 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 68a7c784-741b-3c29-b387-69c2fced8f60 | -16.46992 | -57.40646 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a72a8d37-bf16-39c0-a048-2a73dfc23997 | -16.46914 | -57.38574 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3af05751-66f2-3fc3-a6d7-99623b4c2091 | -16.46739 | -57.37004 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2c33650d-1004-332b-9920-7966e214ff84 | -16.46343 | -57.41534 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3ac7e0bc-3b01-3d9c-8cb6-1e2b956798ae | -16.46298 | -57.34356 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 58c5389e-d4f2-33e1-ac7f-71dce68335c5 | -16.46203 | -57.34849 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4beff86b-bfb2-3a36-8f6e-990ceced8c96 | -16.46187 | -57.37397 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3c210241-6e29-3ead-b988-07e759c0e5ae | -16.46092 | -57.37889 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5c59aa19-a724-3254-94ff-2623941e31c1 | -16.4598 | -57.40943 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0e39fd81-d786-3454-a3e9-94b45f7a36da | -16.45936 | -57.33769 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 995bdf03-4a32-30c0-8574-60acdae39ac4 | -16.45885 | -57.41435 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7c4b5175-44c5-3373-ba2c-4d5b3b8a154d | -16.45841 | -57.3426 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ce9521be-34e3-3bd6-a4a8-62eb028b34ae | -16.45746 | -57.34751 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2685c75c-628a-3d44-9ef6-0b4ab4b2b9e5 | -16.45479 | -57.3367 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ac8189e3-67af-3b12-bcad-87e89ba90b61 | -16.45384 | -57.34163 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 705e41fb-7a65-31c7-822f-e73abb61b577 | -16.45022 | -57.33575 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7fa95f26-e310-363c-8e89-3002c50654b0 | -16.1305 | -57.52383 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c10b0cdb-b244-3697-8e53-589dd14f021a | -16.12939 | -57.52962 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a252ae37-e866-3783-9ef4-38404ebad687 | -16.12585 | -57.52282 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5098729-073a-3c02-985f-fc9f106423c6 | -16.12121 | -57.52178 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b889fa25-b555-388d-9eed-c014879b9b35 | -16.11657 | -57.52072 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README50.md)
