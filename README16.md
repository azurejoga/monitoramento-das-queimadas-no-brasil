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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7059a15-0996-31e3-936b-55b90f92ec84 | -13.9254 | -54.6063 | 2025-06-15 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 47809bb4-a7e6-380e-abce-0fe6356040d0 | -13.9062 | -54.6084 | 2025-06-15 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 12895577-7f67-39a6-961b-571b2b67360f | -13.9059 | -54.6291 | 2025-06-15 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 16e010cd-6e05-301a-8f0f-6313c61a62c8 | -13.9059 | -54.6291 | 2025-06-15 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 68a42792-e298-367c-8cd8-96b56e3ca7cd | -13.9062 | -54.6084 | 2025-06-15 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 32020f34-daec-30c1-9e6b-db9f4f926c24 | -13.9251 | -54.627 | 2025-06-15 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 03aab1a3-be59-3284-a95b-8ce9f88fd31f | -13.9254 | -54.6063 | 2025-06-15 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 21979a32-46f1-3a0a-beee-ba66bb7e5b40 | -4.49632 | -43.77374 | 2025-06-15 05:53:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 48c614b6-b1dd-30d2-8e77-36fec7a1f6aa | -13.91169 | -54.63217 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a5c9a706-69de-3bb5-969e-8c350244cbdf | -13.91636 | -54.60402 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 645e3eb8-e046-3391-82d9-94be468eea88 | -13.9153 | -54.62489 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| a3e596c0-1749-301b-9d7c-a6b076bc6d69 | -15.41222 | -47.85899 | 2025-06-15 05:55:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d2eecdda-8f40-3701-9777-1ca53141034b | -13.92488 | -54.61981 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 74e39c3e-5e8b-3f83-8e8b-745625d219fd | -14.83273 | -48.4367 | 2025-06-15 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| eb0a22df-0bbe-3b15-815c-3151b4f2c63b | -13.92012 | -54.59702 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 28484d42-d786-3967-92a4-579cebcca0ff | -8.31126 | -46.20507 | 2025-06-15 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78e8be26-5518-3f32-9ed2-85156d299efd | -10.44954 | -47.94833 | 2025-06-15 05:55:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e3fbb80a-6813-363e-bed2-2ed1f5f976d2 | -11.00837 | -55.06414 | 2025-06-15 05:55:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f3d46f4e-245b-37e1-a013-0bfa407dbc10 | -10.6283 | -49.42284 | 2025-06-15 05:55:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 87475c58-57b9-3029-8582-f27cd8232cc9 | -13.90551 | -54.60229 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 690a5b7b-9133-3da7-88a0-d62a4375ad07 | -10.232 | -52.23465 | 2025-06-15 05:55:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bef49abf-0cae-3a11-8491-1db355265f1e | -10.65527 | -49.36324 | 2025-06-15 05:55:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0ede3f71-032a-3f03-abd9-6228e79b28c5 | -9.42401 | -48.44896 | 2025-06-15 05:55:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e5f8a8f-c76b-3815-a1c5-554fa6e492af | -10.07991 | -52.73941 | 2025-06-15 05:55:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc7aff5b-1e2a-3b67-9f06-848e74db7caf | -12.69185 | -52.39345 | 2025-06-15 05:55:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 53f94286-d685-38e5-b2a6-8fa24c5ab6d4 | -13.91403 | -54.61802 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 90986bba-1898-3085-821a-365e575058e8 | -10.9105 | -54.76325 | 2025-06-15 05:55:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 08209fc8-824c-34ca-8d27-6dbd7c001e66 | -10.27767 | -47.60482 | 2025-06-15 05:55:00 | AQUA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8f0c3b0e-fe51-341c-8af7-78e2df92704b | -10.6566 | -49.35434 | 2025-06-15 05:55:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 54a0645f-7662-3080-a81a-646503c1fe72 | -12.76627 | -44.40504 | 2025-06-15 05:55:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 3e99287e-f4ee-372f-a652-9feb398e7f17 | -9.41516 | -48.44765 | 2025-06-15 05:55:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 18cd5758-87d9-3b26-9d2c-56409d0cbb2f | -7.23867 | -44.153 | 2025-06-15 05:55:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5010e3ad-078a-3223-82b3-7201b8c5023c | -10.09001 | -52.74105 | 2025-06-15 05:55:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 813a7672-0be8-31e3-8889-e3a447a091cc | -11.00548 | -55.08107 | 2025-06-15 05:55:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8da3149d-149a-3124-89e3-ff95642b7d01 | -13.91775 | -54.61074 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 593e3635-3f7d-3d88-91e7-13a46678154e | -9.41649 | -48.43868 | 2025-06-15 05:55:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 62d2cf73-502a-3e9d-8b90-79cda46b51fb | -13.90319 | -54.61621 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| fab95d6a-38a3-386a-8ed2-a13381e09382 | -10.63711 | -49.42416 | 2025-06-15 05:55:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1a90154b-4f16-330b-b090-2536e76cac3c | -10.50818 | -53.57279 | 2025-06-15 05:55:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6ec2e9bb-3e0a-3080-89de-2a08742280f3 | -15.39971 | -47.87892 | 2025-06-15 05:55:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c59a700c-823f-3f6f-a35d-2f7da87e2b38 | -13.90938 | -54.64608 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2f13ab36-947f-32c4-a817-053886ec94d3 | -13.91045 | -54.65291 | 2025-06-15 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dcd60970-61ba-31a9-8666-44993a8654b1 | -13.9251 | -54.627 | 2025-06-15 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 6df80318-a45d-30c0-b330-799c7a6891df | -11.0113 | -55.0764 | 2025-06-15 06:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 616de206-0536-304d-a755-170ff9625596 | -13.9254 | -54.6063 | 2025-06-15 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 4e54c73c-8171-3ce8-8d56-b8bb74fc3e58 | -13.9062 | -54.6084 | 2025-06-15 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| b346e43f-4b88-328b-a274-1feaf310a11a | -13.9059 | -54.6291 | 2025-06-15 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1b2963c9-ddb6-3b61-a249-c7cd80be2f97 | -13.9059 | -54.6291 | 2025-06-15 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4ce87ab4-93c0-3c42-aea0-a668bb970b29 | -13.9062 | -54.6084 | 2025-06-15 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 37eacccf-f538-3f08-9cd4-6445685212a8 | -13.9254 | -54.6063 | 2025-06-15 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| d2104f7d-763a-30f5-8a4c-8d328e19eadd | -13.9251 | -54.627 | 2025-06-15 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| fffc03c1-6657-3481-8e4e-046202340b19 | -13.9062 | -54.6084 | 2025-06-15 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a54d987c-27ab-347a-8c20-90872d8c1f72 | -13.9251 | -54.627 | 2025-06-15 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| eeed1dbd-4cb7-38c7-b133-38b301027a0d | -13.9059 | -54.6291 | 2025-06-15 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 60ec757a-0a96-3d19-b1de-4c034e226acd | -13.9254 | -54.6063 | 2025-06-15 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 148.9 |
| c455a186-5c28-3925-8534-a2d81fe832f5 | -13.9251 | -54.627 | 2025-06-15 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 5cf0960e-8323-3c4c-bd9a-93f8aebb307c | -13.9254 | -54.6063 | 2025-06-15 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 35bd5d42-27d0-3386-8bce-d022f2e8e4fd | -13.9062 | -54.6084 | 2025-06-15 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 124.5 |
| bd648770-ed0d-3370-931f-5fc08adc6bff | -13.9059 | -54.6291 | 2025-06-15 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 87c363a9-89bc-3d26-8300-98454a55284d | -13.9254 | -54.6063 | 2025-06-15 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| c0e75ab5-e8e6-3ba8-b10c-0a60666c588a | -13.9059 | -54.6291 | 2025-06-15 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 1d66d5a4-49c2-33f2-a970-204312acb438 | -13.9251 | -54.627 | 2025-06-15 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5bbc2d2f-984a-3341-a596-6231619ce025 | -13.9062 | -54.6084 | 2025-06-15 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e8981258-f79c-3217-b619-93851f8d086c | -13.9251 | -54.627 | 2025-06-15 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 62872897-c7ad-319a-8a1a-85febf5af88a | -13.9062 | -54.6084 | 2025-06-15 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8fc82386-7645-3c9e-8eef-471227d901ce | -13.9059 | -54.6291 | 2025-06-15 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| d5e8ec72-bef7-3728-86e9-0b8886c73e55 | -13.9254 | -54.6063 | 2025-06-15 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 2248f7e4-543a-3551-90e7-c4b168d8e740 | -13.9254 | -54.6063 | 2025-06-15 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c23f30d2-e2c4-3f9e-8291-1c56e3b99cde | -13.9251 | -54.627 | 2025-06-15 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 03288f12-69e7-3ee9-b332-b5aad1a61169 | -13.9062 | -54.6084 | 2025-06-15 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 218b8298-4828-3078-8f13-7a299d41fc9e | -13.9254 | -54.6063 | 2025-06-15 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9ca33dad-52b9-3134-a83d-90e0e423f072 | -13.9251 | -54.627 | 2025-06-15 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 7d283ac5-0ab9-32a7-9088-2057e76ce9a2 | -13.9062 | -54.6084 | 2025-06-15 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e8a11844-f42b-3981-ab9e-8512bc7f8d33 | -13.9254 | -54.6063 | 2025-06-15 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| b839b166-7f15-3045-991c-cf9f289e434a | -13.9251 | -54.627 | 2025-06-15 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 208b22b5-473b-3544-813c-6dce38a72549 | -13.9251 | -54.627 | 2025-06-15 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 8cc7d343-0745-3e8e-bd06-37000f33e11a | -13.9254 | -54.6063 | 2025-06-15 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| f456b925-5611-3ec1-97ec-d6dc6f4dc1c5 | -13.9251 | -54.627 | 2025-06-15 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 18d585d7-5db6-36ee-8ede-c3638796c1ef | -13.9251 | -54.627 | 2025-06-15 08:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 4bb4dbd6-ca97-397b-8f69-7964f1660fef | -13.9062 | -54.6084 | 2025-06-15 08:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 9cf2819e-64fb-3fb9-a2b0-f57909b3381a | -13.9254 | -54.6063 | 2025-06-15 08:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 25fc077e-d4f7-3538-b877-d1f270ff04f5 | -13.9251 | -54.627 | 2025-06-15 08:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 9a12fba3-4a40-3d19-8a12-d22201b9b0c8 | -13.9254 | -54.6063 | 2025-06-15 08:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 2ae47b24-0893-3ed3-be25-29149ebc67db | -13.9062 | -54.6084 | 2025-06-15 08:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| f58f6aa3-e75a-3eed-99e4-b2f97cb46213 | -13.9062 | -54.6084 | 2025-06-15 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| a2fca136-0011-358e-8cb5-c40e4fc8c987 | -13.9254 | -54.6063 | 2025-06-15 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| c71eed28-29dd-3df5-a85a-8c147317c22a | -13.9251 | -54.627 | 2025-06-15 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| e9721b50-6a2b-3d03-ab46-a3f343487242 | -13.9251 | -54.627 | 2025-06-15 08:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 63276267-1930-36d0-b5ca-7f962f510deb | -13.9254 | -54.6063 | 2025-06-15 08:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ac542790-1d1b-3541-b8c9-18d766f88608 | -13.9059 | -54.6291 | 2025-06-15 08:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| b7c2c627-d79d-3fa3-a685-fc77eea53c8e | -13.9062 | -54.6084 | 2025-06-15 08:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c87477a8-1455-375c-b916-0498d662995b | -13.9062 | -54.6084 | 2025-06-15 09:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c77dc2ac-63fd-38d4-9505-7578d18a4a4c | -13.9254 | -54.6063 | 2025-06-15 09:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| cc8ca72c-4db1-3101-be3a-0596a286bdec | -13.9251 | -54.627 | 2025-06-15 09:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3dcf05de-1065-3c82-86b5-3e95700041ea | -13.9251 | -54.627 | 2025-06-15 09:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 0ed0f8b6-eb0a-3ae7-8b62-bb397d15efca | -13.9254 | -54.6063 | 2025-06-15 09:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 93414c88-6e3e-327b-ae17-8a2c41a57ceb | -13.9062 | -54.6084 | 2025-06-15 09:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 239d6cde-6d33-3617-a90f-3d071ec525fc | -13.9251 | -54.627 | 2025-06-15 11:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| b9ddc61a-27b8-3860-8984-4a335b299596 | -13.9251 | -54.627 | 2025-06-15 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0cfb2522-82a1-37eb-9f0c-6315f1c3e035 | -13.9251 | -54.627 | 2025-06-15 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |


[Clique aqui para ver as próximas entradas](README17.md)
