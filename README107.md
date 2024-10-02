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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38c6e67b-0b3d-35fd-b5c9-fed76c5ab656 | -16.61655 | -55.99242 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77ce9d89-72ca-3a9f-8c82-cfb5e69d42d5 | -16.61558 | -55.93407 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b52dcbca-76dd-3adb-b14e-8649210668bb | -16.61306 | -55.99179 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 54285517-19e8-32d5-9d15-519848487cd4 | -16.61238 | -55.99583 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 1b58df67-9d26-3f11-bfc0-8390db630e61 | -16.61187 | -56.04167 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| be28567a-a790-32a9-a747-3ef3bcdb016c | -16.60929 | -55.92879 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e946075d-2590-3c63-8355-3f38cbf0a04a | -16.60838 | -56.04103 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 43839195-7b63-31f9-b5fd-ca28a132f9ae | -16.60624 | -56.03228 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3f75c39c-9db8-3253-b8bd-029e434b6bea | -16.60327 | -55.98584 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ec2704ae-3f1c-393d-9284-1bc82f40ee95 | -16.60258 | -55.98989 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 01cd3e62-5e06-34cc-94de-d945c3492fdc | -16.60206 | -56.0357 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a71019d5-6a06-3b66-bafd-12c7cfa22606 | -16.60138 | -56.03976 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6d6f5cae-8737-3410-80a4-177d9232b903 | -16.60122 | -55.99798 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 365d87df-ef55-3c36-bbe0-4e0ef7eebd7a | -16.60001 | -56.04788 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 7d3a2c67-bd90-38d6-9ee6-9790abe203b0 | -16.59977 | -55.98522 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5df55fee-144e-3db7-84dd-27293bc1da61 | -16.59841 | -55.99331 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d284da5c-98ab-369e-9450-8d86daa8b816 | -16.59788 | -56.03912 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 41dc1e2f-28e0-3a1c-b144-cd5cf2fd7b7b | -16.59651 | -56.04724 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b98a391b-e0b5-3d65-a146-23e3b1306958 | -16.59301 | -56.04661 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f2832f9a-a14b-3950-81af-c0dc63412c25 | -16.59232 | -56.05067 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b4b3d39c-c002-3d29-869e-0690b7fabf07 | -17.12128 | -56.12589 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 27b04655-385e-3b8e-b58f-93a222eb0ee9 | -17.1206 | -56.12995 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c159b549-f3b1-3216-a3ce-2274ba894703 | -17.11218 | -56.11587 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 99c47f77-45ba-3fe6-96e1-fc9ea9efe532 | -17.11144 | -56.09904 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ded4b6a8-6a93-3aa8-83c6-238116a3a200 | -17.11075 | -56.10308 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cd03e50b-7fea-34cb-ae6f-d4baa59b241f | -17.11007 | -56.10713 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d1c37250-246b-3be3-be6e-e9d1c3fa1c42 | -17.10938 | -56.11119 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a5fb812d-449b-3033-a480-2217d3368c40 | -17.10869 | -56.11523 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 81d43b3b-ba85-3066-8b6a-9086e357e967 | -17.10795 | -56.0984 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 826b3818-58cb-3726-818e-31253dfe91a6 | -17.10726 | -56.10245 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aa924572-b002-3236-adb8-8d810a927113 | -17.10658 | -56.10649 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6db69228-d848-316b-8a37-7c9f8a68e2c9 | -17.10589 | -56.11055 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 89e795f5-1040-38db-b9bf-0f1313967f08 | -17.10377 | -56.10181 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 43c4548b-ecf1-3045-ad42-bc7aa0bbc5f0 | -17.10308 | -56.10586 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8ad10c00-9e5f-3b34-81c6-a54184b5da74 | -17.10028 | -56.10117 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2b14e04b-184f-3e64-a786-ffd7f185d0e4 | -17.09959 | -56.10522 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f8f162e3-6e87-3499-9f40-925914c63d63 | -17.09123 | -56.11204 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fc97ba02-084d-3e30-989d-e17b5de6a52f | -17.08843 | -56.10736 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 07a06e95-43e2-3ca7-abfc-14e24873da68 | -17.08774 | -56.11141 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f1fa0b46-6728-3d4f-997b-2c409f05370e | -17.08424 | -56.11077 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f2ce40d3-dacc-3759-a5d2-4d8544c5a97c | -17.08355 | -56.11482 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1cfec95c-1184-32f8-af3c-3bcf8a0c80fa | -17.08286 | -56.11887 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3f954402-268d-3a6f-ba93-82b2b47fb8cd | -17.08144 | -56.10609 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8472068e-f297-3a5d-965e-a35c94b57bdd | -17.07937 | -56.11823 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2d95c6e3-955d-3160-bf83-1e34eb2918a4 | -17.07865 | -56.1014 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bafcc9fa-10d6-3c2c-8d4c-b9a09f349bbb | -17.07723 | -56.08863 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 28319c3e-61c2-39e1-9109-f36f50d24c5f | -17.07654 | -56.09267 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5785b3b0-8dab-3432-bc71-b450b7b027a0 | -17.07585 | -56.09672 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 36bad4b3-c03f-3e80-a24d-7d341ffe4582 | -17.07444 | -56.08395 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57f1058a-14a1-3d74-9c54-864e2dbda597 | -17.07305 | -56.09204 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 310d1d34-92e4-3b4d-8001-26d7e8e155d1 | -17.07236 | -56.09608 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ab597cfd-32cd-3b5e-a297-b305f163516c | -17.06956 | -56.0914 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2a35d0de-dff3-3579-be5a-316b1bdb9beb | -17.06887 | -56.09544 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 36df4a74-1b26-3cff-bb67-03817cca689a | -17.06677 | -56.08672 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 11c25ffc-8370-30c1-8e48-dc8525dd64c2 | -17.06607 | -56.09076 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| af4302aa-5c30-330c-963f-1b7fc6e3a671 | -17.06328 | -56.08608 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 37bb7755-40e8-3a87-85ca-c8cfe810fb79 | -17.06258 | -56.09012 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 9720a04d-de0e-3e1f-ab56-8d15df171706 | -17.06189 | -56.09417 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| c21af450-f5e2-31f4-a82b-ef6241764560 | -17.05979 | -56.08544 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2c0669c4-d359-3c07-863c-acd8d929b21d | -17.05909 | -56.08949 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 656df89f-4f4a-3bcc-91fc-fc52950fd56b | -17.0584 | -56.09353 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| b42261fc-0014-338c-847e-0fb23e855678 | -17.057 | -56.10162 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f690f94f-cdfa-3153-8559-c34e7c922bd6 | -17.05491 | -56.0929 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 715bdcf7-6476-3525-a735-022a3e3a817f | -17.05421 | -56.09694 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3a895fea-e8b7-3660-ba53-e951dd57eabb | -17.05351 | -56.10099 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 767d1c28-2799-38e4-ab3c-4d35cad1b839 | -17.05302 | -56.09768 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f32d49c7-96b7-32fe-97ec-6c28cc34a16b | -17.05141 | -56.09226 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ebd343d2-e10a-38b8-98f9-e8dcf24d755c | -17.05021 | -56.09299 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| edcb4ef2-4f60-3ad4-8c4f-519a217d0efb | -17.03829 | -56.0783 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f144eb8a-898f-31b7-9b84-07a442720a6d | -16.98325 | -56.12677 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ecde7aa5-4a12-397d-b354-eb748a9a8132 | -16.95037 | -56.1082 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d70174a3-29ad-399a-b0dc-8a4a333be31f | -16.90098 | -56.11712 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 35108504-3630-3169-89f9-48d818190994 | -16.89107 | -55.83784 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 12051b11-8431-36bd-b453-09c7b496bc8f | -16.8904 | -55.84181 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 387e104d-a890-3864-af22-a9b79ee94750 | -16.88516 | -55.93539 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 210df4cb-637b-3588-a5a3-d130ce78fbf5 | -16.88482 | -55.83263 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5d4051e8-a5e7-35fc-b7bb-56ba0a8d2aad | -16.88279 | -55.84453 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3ed151bd-82c3-39ed-9320-be71f6779f1a | -16.88237 | -55.93076 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1fd040b0-5d05-301f-92a3-c88eb5274c41 | -16.88069 | -55.83596 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 5e0b53a9-e363-3d85-a25f-e1b2968d6bc5 | -16.88026 | -55.92213 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 521b48c4-9fbc-3fb0-b3f0-77765f4dda05 | -16.87958 | -55.92613 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 23223e0f-a110-3958-a772-1c6f603af8d4 | -16.8761 | -55.9255 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7c9ab183-00de-36e2-a439-7168f4d6d28a | -16.87542 | -55.9295 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0d960504-cec7-3905-b2b4-1cbef397a315 | -16.87462 | -55.83909 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 30995b59-d18b-3691-a8e9-a023762311a4 | -16.87258 | -55.90427 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 223b87e1-e431-3d97-b9da-843a675e201b | -16.87194 | -55.92887 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 194eb2dc-8a26-3fa3-9118-8151a8ae7991 | -16.87189 | -55.90826 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 730887e6-d377-3523-9ded-61790b9f0ce2 | -16.87182 | -55.8345 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| ec9e8a81-c35d-389c-a0e4-9a8ed552f0d3 | -16.87121 | -55.91225 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 646c7f53-7c2a-38ea-93ae-3e317ba289c9 | -16.87049 | -55.84243 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 3b45f23e-aa0d-3a5c-9a20-d4852d2516e0 | -16.86983 | -55.84641 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 7dd1eeaa-785f-3717-8e43-ab60313b5fd9 | -16.86916 | -55.92424 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5ca6761b-7a20-32ea-810e-7a0ed54f8728 | -16.8691 | -55.90364 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9bfbb92b-002d-33f7-b0f5-d68ff719e087 | -16.86842 | -55.90763 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1e579c51-ebdd-3240-9e48-6e9c8bbdfb64 | -16.86705 | -55.91562 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| dd3a9e10-6a56-389b-a157-afc1765b5d9e | -16.867 | -55.89504 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0be990a4-b1c2-36c9-be47-14c62bc20519 | -16.86568 | -55.92361 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2b93304e-77a0-32fa-b46e-4459c940ec57 | -16.86423 | -55.83721 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7e75aa2f-b523-3479-a898-dae2a21356e1 | -16.86411 | -55.92352 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b92b53cb-eeb2-3d5a-86b2-15529d572040 | -16.86224 | -55.84913 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |


[Clique aqui para ver as próximas entradas](README108.md)
