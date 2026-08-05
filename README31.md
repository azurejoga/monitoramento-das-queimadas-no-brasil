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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 053850ad-dd63-32ea-92c3-161d128fd030 | -14.2687 | -45.2636 | 2026-08-05 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 1acc4359-4ba3-3de6-ae63-51a262647be2 | -12.5754 | -46.9329 | 2026-08-05 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8a911b0e-bdb4-3559-8052-db8d94a5cc79 | -14.2682 | -45.287 | 2026-08-05 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 262.9 |
| 7afa06ba-9522-3d90-b51f-4693575b9aa3 | -7.2293 | -45.7801 | 2026-08-05 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 81f71db6-bb84-3599-abe1-a92ef0d2574e | -8.9302 | -45.2041 | 2026-08-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| eb55ba33-ad18-32c0-9ea3-5c259347a02e | -12.5942 | -46.9527 | 2026-08-05 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| a26e5e6a-06ae-3f8e-a4f2-f4e3665ec078 | -12.5951 | -46.9075 | 2026-08-05 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9b0857c3-579d-3387-8896-4d16e0cf0bc8 | -12.575 | -46.9555 | 2026-08-05 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 283ea867-599d-391e-9b7b-8fbfb5c1ef35 | -12.4383 | -50.5324 | 2026-08-05 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6aa2f3ab-c72b-31d5-9f40-b33cfe87dbcf | -10.9192 | -50.4283 | 2026-08-05 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 434f692b-5190-3116-9e6d-275aa07e374d | -12.5947 | -46.9301 | 2026-08-05 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| aa1baae6-0334-3f31-8666-f380d6d548d3 | -12.4386 | -50.5109 | 2026-08-05 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0cc2974e-c64a-3700-a455-960ceb6537e4 | -7.2187 | -43.3499 | 2026-08-05 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 7f5a5b3d-8cd1-3752-9f27-382d17d0409b | -13.2604 | -54.2662 | 2026-08-05 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 9b9b353b-ba1a-3a14-8193-1fe42d023b39 | -12.5938 | -46.9753 | 2026-08-05 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| efd7fc2f-e096-3970-bb91-239434034701 | -13.2413 | -54.2683 | 2026-08-05 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| fd97a3f9-ac13-3037-b2b2-45559ba83c60 | -7.2293 | -45.7801 | 2026-08-05 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 8be46ff8-3031-3ead-b098-52942732e7ae | -10.9192 | -50.4283 | 2026-08-05 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 79e8567e-7e77-3d45-8133-44260fa8da9c | -12.5947 | -46.9301 | 2026-08-05 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 51b72f95-b257-3647-9877-7d9e61488d85 | -12.5942 | -46.9527 | 2026-08-05 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| f55e81bd-a6ec-31e0-90e9-c9814dab0971 | -7.2187 | -43.3499 | 2026-08-05 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 835de4d6-30ec-359d-b059-c8e1911e8878 | -13.2604 | -54.2662 | 2026-08-05 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| fe21b4db-ed90-3ad7-9359-1012b877d1a5 | -14.2687 | -45.2636 | 2026-08-05 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 1996f407-e026-32a2-aabe-fd8577184f0f | -12.4789 | -50.377 | 2026-08-05 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| d16bab69-8f7f-3b9c-bdb5-2cb9cd70f7b7 | -14.2487 | -45.2904 | 2026-08-05 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 124a874a-2f55-3b96-8a13-53cb7459e031 | -12.4598 | -50.3794 | 2026-08-05 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7ab6c1ce-10f8-397b-875c-04da0dfd7834 | -11.2916 | -44.8133 | 2026-08-05 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e8f13092-67fe-3cfc-a662-0f7c3d57acc8 | -14.2682 | -45.287 | 2026-08-05 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 1b34a22f-948f-3d73-9000-6519ca473337 | -12.5938 | -46.9753 | 2026-08-05 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 190.2 |
| a2ad8132-e068-3e8a-bc90-cb6ed32120d1 | -11.3107 | -44.8105 | 2026-08-05 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 7a8fcadf-c3f8-3313-a1f8-d3565edc1d32 | -14.1972 | -54.4102 | 2026-08-05 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2f7e558f-3654-3813-9083-bc29b1d83eb5 | -7.2296 | -45.7575 | 2026-08-05 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 87bcb8e3-38b1-3986-997d-b09ffbe2ac9b | -12.5754 | -46.9329 | 2026-08-05 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0172223c-55fc-3eef-b8df-bf341205f4a0 | -14.3865 | -53.3877 | 2026-08-05 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 460dd531-8621-3530-b898-9c953db0587c | -7.2293 | -45.7801 | 2026-08-05 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 6d16afee-062a-32c7-984a-d6ee8b48b6b8 | -14.2682 | -45.287 | 2026-08-05 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 2e5a3543-2d49-31eb-84d8-f95fa3e4bb65 | -14.2487 | -45.2904 | 2026-08-05 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| deb64cb8-2f87-346e-b869-aa426699d152 | -11.3107 | -44.8105 | 2026-08-05 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 1f552f97-9536-3d11-a941-d963e7fdd2a4 | -7.2187 | -43.3499 | 2026-08-05 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 6fd8ca4f-b958-34a8-a709-5b52a84ee31e | -13.2604 | -54.2662 | 2026-08-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 7dc862ef-0845-3d08-8043-a1785e6d1be3 | -10.9192 | -50.4283 | 2026-08-05 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4be11c95-9b05-33b0-bef4-6a537550c437 | -14.2687 | -45.2636 | 2026-08-05 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 102558fd-0de2-3bb7-bb8d-a278eb7779da | -12.5951 | -46.9075 | 2026-08-05 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 41010acd-e7ca-3215-982c-6e71a153ce42 | -14.1972 | -54.4102 | 2026-08-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d30ef829-f5b4-3b00-9448-4593f4ed7e92 | -8.3494 | -46.394 | 2026-08-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 1ded3842-a753-31b5-abd3-2fdb84082da5 | -6.9879 | -42.1201 | 2026-08-05 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| aced1ce4-7890-3af7-afcf-b126d4f51748 | -13.2604 | -54.2662 | 2026-08-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| d5c02f1e-c908-359c-9c3d-7723f717f656 | -12.5947 | -46.9301 | 2026-08-05 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| fdcfe86e-fe17-32fd-962f-baf9736f9827 | -12.4598 | -50.3794 | 2026-08-05 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| bbe99918-002a-3d3a-9fb6-41a717239d1a | -12.5938 | -46.9753 | 2026-08-05 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.3 |
| d14cf77d-535a-36d4-a013-d37a8bc354bb | -12.5942 | -46.9527 | 2026-08-05 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 1c9aa0e6-0256-3cac-a617-d9d9b2c001f0 | -14.3865 | -53.3877 | 2026-08-05 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 00eaca6a-23d1-370c-a964-b43b93e4f33b | -14.2677 | -45.3103 | 2026-08-05 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f089ce5f-3f0c-36f2-8ef8-76c6c8e3daea | -6.8904 | -42.4152 | 2026-08-05 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| dde94870-4bd4-363d-aae0-ee6cbd88961c | -12.575 | -46.9555 | 2026-08-05 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 30bcae47-f978-3b69-a971-435f4b52edc7 | -6.5514 | -55.1569 | 2026-08-05 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 96611432-74b8-3ff2-b76f-8bce8538f6b1 | -14.2487 | -45.2904 | 2026-08-05 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c961c1a3-a813-38e0-a2b0-2e9f641f03b4 | -7.2293 | -45.7801 | 2026-08-05 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| d293120a-b36d-37e4-9f8e-837b86121867 | -14.2687 | -45.2636 | 2026-08-05 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| aa591ae8-5b01-3dc1-97ac-54b5416a12eb | -10.9192 | -50.4283 | 2026-08-05 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b30d83fb-4449-3f01-b3ae-f6ee5e8d18cf | -8.3494 | -46.394 | 2026-08-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 5e2d6769-17a5-376f-8e71-52f0a4dd6e7e | -14.2682 | -45.287 | 2026-08-05 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 262.5 |
| 9ade790e-0e59-3617-9e8d-18be4f225b7c | -7.2187 | -43.3499 | 2026-08-05 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 54d246dd-5ea6-35df-af04-a10277cff0a8 | -12.5754 | -46.9329 | 2026-08-05 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d9bd7b45-16f4-39e0-b590-6d9f6efccbca | -6.9879 | -42.1201 | 2026-08-05 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| 24937c36-3f3e-3bde-9eaf-877f7eb55d4f | -12.5951 | -46.9075 | 2026-08-05 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 08a70bb3-1963-32e4-9bbf-b3528d5753f6 | -14.4058 | -53.3853 | 2026-08-05 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f8a2a430-d2a3-3299-ab45-b2be2e1343b4 | -7.2187 | -43.3499 | 2026-08-05 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 13d85436-13f9-3927-ae3f-a9110e79cdbf | -14.3865 | -53.3877 | 2026-08-05 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f007d887-b5af-3d05-b583-28ab9a5e416e | -6.5514 | -55.1569 | 2026-08-05 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| fedb9681-d94d-373b-9f7c-7c5d24cc7602 | -7.2296 | -45.7575 | 2026-08-05 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| dd7648ae-81c6-35af-8dc0-88f0e54c3c32 | -14.3579 | -47.5144 | 2026-08-05 14:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 4b4b8595-8c08-33b6-84e8-41f2713fb536 | -10.6184 | -46.3646 | 2026-08-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 87cc7f60-75a1-3061-b388-cb1a4e639229 | -14.1972 | -54.4102 | 2026-08-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 6a967789-6751-3349-bf4d-fd1fe754fed5 | -12.4789 | -50.377 | 2026-08-05 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b0ccc5ad-140b-39ff-8e04-076dfe548939 | -7.2293 | -45.7801 | 2026-08-05 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6769cb74-34b3-33ea-a48a-71025ffce0fa | -12.4386 | -50.5109 | 2026-08-05 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8c02ccb8-56e9-3033-ad53-733baa067e48 | -12.4598 | -50.3794 | 2026-08-05 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 281fab4b-e610-31d0-83a5-f931b094bbd4 | -14.2687 | -45.2636 | 2026-08-05 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a9ff9f8e-7899-30f0-9afe-bc7731734eb1 | -14.2682 | -45.287 | 2026-08-05 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 1133faf7-f6c8-3a2d-9880-eb47a43af934 | -10.6181 | -46.3872 | 2026-08-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 52813b2e-55a1-3cf3-a793-0b80bce49f01 | -10.9192 | -50.4283 | 2026-08-05 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 268.5 |
| e5dd9cfb-9707-3a4e-8856-250588b63602 | -14.2487 | -45.2904 | 2026-08-05 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 39c6fe19-b888-3ebc-b467-1153e9d0c990 | -6.9879 | -42.1201 | 2026-08-05 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 681e019a-5a7c-345a-8018-4095ea75e651 | -14.2487 | -45.2904 | 2026-08-05 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a6dcc2e8-cedf-3d7e-9f68-8fab860d5415 | -14.2682 | -45.287 | 2026-08-05 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 217.7 |
| b30ed246-388d-3599-a6dc-458415dee9df | -11.292 | -44.7901 | 2026-08-05 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 113ce91a-4727-3679-9ecb-a2721dd2367c | -14.3672 | -53.3901 | 2026-08-05 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5c858444-1d0b-37d8-99d5-55f9d0859953 | -12.5947 | -46.9301 | 2026-08-05 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 18b0b079-c84c-35f4-8290-167e03898158 | -7.2296 | -45.7575 | 2026-08-05 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ee981c57-acdb-373e-aff0-ec05ea8f2f1d | -12.4407 | -50.3817 | 2026-08-05 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f00ccc31-fab6-3dfa-bd90-2ed2ec5d945a | -12.4383 | -50.5324 | 2026-08-05 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e65eaebe-e927-3c14-8261-9cd4d29946fa | -7.2293 | -45.7801 | 2026-08-05 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8ef1ce86-c071-39eb-8bd7-8a54d0c4fce2 | -14.3865 | -53.3877 | 2026-08-05 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 44250d49-8ea7-3731-bc01-89e2f29e982e | -6.5514 | -55.1569 | 2026-08-05 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 07bd9583-1664-37da-ad13-9ee613f122f8 | -7.2187 | -43.3499 | 2026-08-05 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| da6f4d20-2554-3a47-9e71-aa6201b6e745 | -12.4403 | -50.4033 | 2026-08-05 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 540a7d67-c3c6-38e1-a473-61e5da1da8ba | -12.4386 | -50.5109 | 2026-08-05 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| f989b78c-6ddb-3479-a928-76b72baa7942 | -10.9192 | -50.4283 | 2026-08-05 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 174.9 |
| c144291d-42b8-3cce-b3c2-275047bc9a03 | -12.5951 | -46.9075 | 2026-08-05 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |


[Clique aqui para ver as próximas entradas](README32.md)
