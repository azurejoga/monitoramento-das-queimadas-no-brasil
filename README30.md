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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81ed58cc-ea2e-3661-907b-cdbe43f2c2a7 | -6.34828 | -44.56371 | 2024-10-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c260d837-c2f7-320f-af68-07887ad39947 | -5.34413 | -43.3626 | 2024-10-26 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a31d001f-78b4-33b3-9191-cf888a916825 | -5.93086 | -44.65199 | 2024-10-26 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e028caf5-912c-353f-a937-8002ce740255 | -6.70272 | -43.95513 | 2024-10-26 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0507b6ad-2f24-3e88-af2d-0cbe6a0e8ae9 | -6.69792 | -43.95818 | 2024-10-26 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dff3f34-ed0a-31d6-ae1c-8109c48f54ae | -7.05183 | -44.65902 | 2024-10-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37175d07-13b5-3b10-b925-cb1a80ab17c1 | -6.82059 | -44.46762 | 2024-10-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84d8b681-5a42-3bf4-a6d7-dc3c32c58df2 | -6.81864 | -44.46745 | 2024-10-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ebfecff-325e-3289-8991-23f733568d9b | -6.81792 | -44.4716 | 2024-10-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33abe1ca-b8e8-3f2b-ad17-0a57a8a7cfcb | -6.8156 | -44.47101 | 2024-10-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea61c412-5823-34cb-88aa-c177c5397048 | -6.81363 | -44.47082 | 2024-10-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e467e9f-5fd1-3c27-80fd-05d14969f1a0 | -6.81131 | -44.47024 | 2024-10-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dcb9a9a-6736-36be-9624-c118d16e1112 | -6.71011 | -44.69967 | 2024-10-26 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10965087-3753-3a08-a882-c69e419377e6 | -6.70523 | -44.06607 | 2024-10-26 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| beddf709-195c-3bc9-816f-c68b57152e24 | -6.59763 | -44.18776 | 2024-10-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7128dd8-d165-3c78-bec4-b568f755bb8b | -7.30618 | -44.97024 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3989790c-e848-3c70-bba7-99397d3d2585 | -7.3047 | -44.97877 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 473c7d0b-12bd-3ece-b5ad-a36b325a7b1c | -7.30178 | -44.96943 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4460dc19-3ed3-32b4-b5d7-425a13e3ddcb | -7.30029 | -44.97797 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6dbd8806-b839-3aeb-b6d7-3b3b157180bf | -7.28778 | -44.97158 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19c7fe62-4687-3aa7-bf2f-71342e8da53a | -7.28703 | -44.97589 | 2024-10-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 080b1f82-f19b-3507-8a59-f9390e5f1b44 | -7.02645 | -45.1965 | 2024-10-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4424cc6-7a96-3550-95a8-c79add288927 | -7.02429 | -45.1969 | 2024-10-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0936db52-c7e7-3748-b772-6fac327d3877 | -7.76599 | -45.16642 | 2024-10-26 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 783ab5b4-847f-349f-ba59-b14e7cf3d513 | -9.00663 | -44.31027 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38d67c6f-1c4c-3102-b827-0458e1d16997 | -9.006 | -44.31398 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 79d19a49-f753-3e6b-aeb5-a495773532b9 | -8.79369 | -44.71883 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15417df0-51ea-36b2-8dec-9e312b6b97d1 | -8.793 | -44.72283 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b214674-4e65-3ff7-96c4-4cf37f21efa3 | -8.79231 | -44.72683 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9666525-aab2-3ab4-8695-99812e358f8b | -8.78946 | -44.71811 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 573785c8-1a8c-3e6f-ba8f-e43c22a334c1 | -8.78877 | -44.72211 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18ca2a0e-a7c7-3ed2-af30-964e427e4bda | -8.78808 | -44.72611 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ca7e22e-46e2-3929-a03d-0de03ee9f4e5 | -8.78739 | -44.73012 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f033fb17-2c25-3b4d-afbb-4fd8ddfc4c3d | -8.7867 | -44.73412 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92ff7586-d4b6-3c52-9c9e-533594167293 | -8.786 | -44.73813 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 952e9893-d07b-3c7e-a5ac-71bc904d8d44 | -8.78101 | -44.71661 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12b3ef7a-6dda-3342-aa1f-241c0fe5bed6 | -8.78032 | -44.72061 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cf45e47-3a3c-351e-81aa-66b5e3fce643 | -8.77962 | -44.72461 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 760d5bab-13f5-33cd-a838-6784828b3081 | -8.77609 | -44.71986 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 206d53c6-6c62-3c09-ba35-e5d6fc1b2414 | -8.7754 | -44.72386 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a64c482-d171-3747-9725-17bcb532a71a | -8.7747 | -44.72786 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 333f480d-ef1a-329c-88d8-8367e5817b1f | -8.7641 | -44.71365 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9680137-be38-3530-b25e-6462d0f07cee | -8.7634 | -44.71765 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f90c6b23-fe28-33e7-9b78-d6cdec2de975 | -8.7627 | -44.72165 | 2024-10-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6925dd43-9aee-3d7b-9628-ad9a299bfb7f | -8.6549 | -45.04837 | 2024-10-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31107bf0-6f5b-34ef-b5a2-739bfe94cca1 | -8.63577 | -45.29205 | 2024-10-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f6281ad0-18ee-35dd-80b6-78758aeb9be4 | -8.63541 | -45.29168 | 2024-10-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 814184f1-2829-3e88-b7d0-27b3b8f941dc | -11.51744 | -45.82949 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95de742a-5f1d-3835-a2f6-1b22c15e9b40 | -5.04291 | -45.45292 | 2024-10-26 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ac5853a-3526-3c06-b126-ee492f9bd69c | -5.02932 | -45.1218 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b8ba27-f228-34db-90e1-c15d9e40b4cb | -4.95106 | -45.61492 | 2024-10-26 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f44eab1-d6a9-3f4b-854b-1053ea33661b | -4.94626 | -45.6142 | 2024-10-26 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7c1c3f3-1a22-3b45-a49f-e213bc780f84 | -4.92049 | -45.85533 | 2024-10-26 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab6095a8-6d31-3f41-a5c9-ad65b830e680 | -4.91954 | -45.861 | 2024-10-26 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f9ab90d3-373b-3581-8678-d3d1b9f7c858 | -4.91561 | -45.85455 | 2024-10-26 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6d77a2c5-869b-3705-88b6-2e7d2bff0cf6 | -4.91466 | -45.8602 | 2024-10-26 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a4d0f572-89ef-37a5-857f-e6e5722b2161 | -4.86343 | -45.7792 | 2024-10-26 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3f3a4bb-a402-3662-8b47-4f23c71ef790 | -4.76354 | -45.75971 | 2024-10-26 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fedebe0f-704e-3ace-b272-89717147d532 | -4.74373 | -45.67835 | 2024-10-26 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a9bd7e7-a313-3561-b96e-fb2ac4f0347b | -4.73891 | -45.67745 | 2024-10-26 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05e3f54b-bc31-3865-ade8-148afde11ea6 | -4.69292 | -45.71412 | 2024-10-26 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27b78f1f-b816-3550-a1f0-3f41c099e529 | -4.68134 | -45.8116 | 2024-10-26 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d203a2dc-e7a9-382f-8b3d-e0b251ed2d5c | -4.58276 | -45.84402 | 2024-10-26 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6badd247-f12c-37dd-aa79-5b548f86aae5 | -4.54534 | -46.03534 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b05a0fa-a2fb-3465-9dda-537398ab48d3 | -4.54037 | -46.0345 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed048750-6fd1-339d-a14e-6d95cc37b45b | -4.21674 | -45.82001 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54072b32-e351-3c51-952f-5a88e08a541d | -4.21547 | -45.81655 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f60ce695-0606-338f-a727-ba4eb7eea232 | -4.2118 | -45.81927 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8391b45b-c81a-32f1-9fcb-faf27470adb8 | -4.08305 | -45.56889 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 521466a6-5ccb-358e-8f0a-be07badc029b | -3.99366 | -45.97902 | 2024-10-26 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d95e6e9f-affc-339e-bd34-6b182b2b7e8a | -5.98198 | -45.37001 | 2024-10-26 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2aba5fb3-06fc-32fc-a42d-2e24505e325d | -5.97816 | -45.36445 | 2024-10-26 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7bbaca1b-53dc-3d88-8a9b-0425fde9ee5a | -5.97733 | -45.3693 | 2024-10-26 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 5fecbde2-e8c1-39ce-bbc1-fccdc26ad983 | -5.97651 | -45.37416 | 2024-10-26 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4c45ab17-e028-3dff-a225-6513d43e274c | -5.90931 | -45.51469 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56aa8090-0804-396d-8ff7-f07c99c50be2 | -5.86773 | -46.14605 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8180d209-ebd9-3a98-b9eb-afa36b74bc27 | -5.8443 | -46.24056 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f04c4638-b5fa-38ac-a644-b77f68ac37f4 | -5.77933 | -46.29309 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab470fea-73fe-3996-a449-188cfd3926c3 | -5.75819 | -45.56499 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b29a81f-4ff1-39a3-b4d9-ffde4ddcb669 | -5.75699 | -45.56242 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7e10b64-4f10-392c-b54f-a3cacb6abdcb | -5.75436 | -45.55917 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ceb1f6e-7dc4-3faf-8738-5ac0df09f4c0 | -5.75348 | -45.56419 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46dc3667-dddd-3485-b93b-47c8dae7f7a2 | -5.75227 | -45.56166 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94b89e47-c16d-3caa-b5c1-3d0fc29ad2c2 | -5.64111 | -46.40583 | 2024-10-26 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9c13118-ffd3-3bd0-99fa-5a091899205c | -5.49454 | -46.35891 | 2024-10-26 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3848595b-5186-3292-9e9c-05d51d7ff321 | -5.48956 | -46.35798 | 2024-10-26 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0875d92c-6e22-3bd0-bf7a-deb314168d2f | -5.48908 | -46.36078 | 2024-10-26 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2666f283-020c-3c2e-9030-5ab77400ab82 | -5.35927 | -46.24839 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0f4a2d4-f709-3d61-99b4-805eced23bb5 | -5.35431 | -46.2475 | 2024-10-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aae27dcb-3cdd-375a-a55c-1c0f92b19c51 | -5.20654 | -45.32759 | 2024-10-26 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| edcaed15-3907-34af-bf65-00f5798e7f91 | -5.20573 | -45.33237 | 2024-10-26 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f920c941-0700-32e8-9e58-65d7e55541e2 | -5.11462 | -45.4024 | 2024-10-26 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88dd5e5f-6cda-3a41-aaae-38d2213e2ebf | -5.10989 | -45.4017 | 2024-10-26 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 519ae170-35aa-3b4f-8069-336faa944fc9 | -6.40747 | -45.82381 | 2024-10-26 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71ae23b0-5c9b-3b85-875c-03a2f28b6db4 | -7.94501 | -45.69099 | 2024-10-26 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bd3381b-33af-386e-8946-aa77ac6e48f0 | -7.71606 | -45.70423 | 2024-10-26 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7cdc3f2-e895-3679-abcf-35d557422213 | -7.71519 | -45.70917 | 2024-10-26 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8cfc5199-2ec8-3abb-9284-fd4bacaff6e2 | -7.5634 | -46.79273 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc423796-a37e-3699-8d23-5138c8a00a1d | -7.5629 | -46.79557 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 500c0846-6745-3829-b008-644c7d8995d0 | -7.5624 | -46.79842 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README31.md)
