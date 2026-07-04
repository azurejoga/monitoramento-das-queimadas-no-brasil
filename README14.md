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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2109a39-86be-3083-8ce3-8e8070531c77 | -8.86042 | -62.2258 | 2026-07-04 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 116381e0-9a09-3ada-8b93-420be6523fa3 | -8.03097 | -46.24209 | 2026-07-04 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9fda7c82-da23-3d4d-a784-0decf606152b | -12.74955 | -44.53926 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b6eafa2a-3ec8-31f6-a159-bf222063fc96 | -8.08503 | -46.70975 | 2026-07-04 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39016fc2-4ef2-3e13-9683-42520c1f5db2 | -10.93332 | -43.05122 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 04b9525f-6fe3-3509-8058-fec0711fd26d | -12.75352 | -44.55567 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c86f29ae-2160-3f2e-9f3c-a5a33ba50ca0 | -11.43896 | -46.56472 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81e68f50-1cbf-3965-b291-f699c58b44d5 | -6.42777 | -43.72172 | 2026-07-04 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55e034c4-0074-3b40-97d8-bb2af32d12c2 | -12.75842 | -44.51766 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02979d40-6c7b-3a76-a833-c99bab00057f | -6.87808 | -43.70293 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 745813b2-81a4-365e-8ae8-9809712a66be | -11.45345 | -46.55112 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b4bbd82-7d21-32c6-8c39-5b516c425f47 | -10.93253 | -43.05766 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8b5817b-5842-3994-bde3-907d238d4d5e | -11.4245 | -46.57832 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b0212851-13ae-31bc-86e8-8a9c49aea6fb | -9.56889 | -49.11155 | 2026-07-04 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7014777e-d922-3da4-ba8f-e523e127ae59 | -5.7939 | -45.06367 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03d38cfb-82ee-3063-b510-6ab4c99263f5 | -10.93854 | -43.05194 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4e1c4c0-2d8b-39c9-bb21-f1b4ca751e41 | -11.46072 | -46.5598 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b3d8698-7844-3290-b18a-22a0c185e46c | -8.035 | -46.24264 | 2026-07-04 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| de5649d6-c772-3f21-ab34-d7895f576516 | -7.00962 | -42.7768 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 38c3c864-f14c-33d1-8694-8d5d1f88a95e | -12.74595 | -44.53807 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d008abb5-d012-318d-ae12-30eae79510dc | -12.76407 | -44.5412 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d4619c52-d376-3695-930d-f0ceb532464a | -10.98359 | -43.70938 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52930549-d172-3903-8d8a-bbc608c717a9 | -10.93451 | -43.04159 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9b5303a6-a1b4-3185-9ec7-705f60d915cc | -8.44479 | -51.56621 | 2026-07-04 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43037851-2347-38b7-9d49-b25867c69c1d | -12.76055 | -44.52964 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| babfb7f9-cac0-3051-ad32-05885346a95c | -10.79017 | -54.10644 | 2026-07-04 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a4d94a-b510-34eb-bd69-c46b84f5bea2 | -10.90469 | -56.85427 | 2026-07-04 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42cdcbcf-468f-33f6-afcc-59a2d2d96c15 | -6.92909 | -43.71601 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c68c592b-71fa-3297-85a4-98a431398a16 | -12.75989 | -44.5351 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ba0d4718-a387-3ea2-9755-741d29e72104 | -6.43241 | -43.72255 | 2026-07-04 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa364fb1-da25-3656-a522-896857360209 | -12.76187 | -44.5291 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 52d946ca-f532-3403-9213-0b00bf4a6c06 | -7.2378 | -47.11208 | 2026-07-04 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87635547-c277-317c-94f1-7754e5077920 | -6.88278 | -43.70372 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1cec36f-7e7b-3f30-ae97-c558c8fd621d | -5.45869 | -47.90375 | 2026-07-04 04:46:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98e0c131-35bf-397d-bca3-fb9f76cd07e8 | -11.45294 | -46.55485 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c951f16-970f-3bf3-b5d1-44712d64e0f1 | -6.93779 | -43.72237 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5626efd0-9497-3f2c-842d-6cc4196e1c13 | -9.8035 | -48.91776 | 2026-07-04 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2df28a68-de1c-3da1-9d2a-2e2cfc74e354 | -5.43281 | -44.6543 | 2026-07-04 04:46:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bc0a565-3849-353a-9583-fd5135f8df19 | -10.9281 | -43.05051 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 56ad397a-d794-3c4e-9b17-83d6fd349cf6 | -9.60012 | -56.92313 | 2026-07-04 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f0cffd4-eda7-3a16-af44-b7795ea8880e | -11.66345 | -50.39346 | 2026-07-04 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed9bcaca-b70c-3c72-a8bd-b8b94a9ca584 | -5.43109 | -44.65068 | 2026-07-04 04:46:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef2b5f58-0d37-3e78-9a92-11cd48569787 | -8.08184 | -46.70412 | 2026-07-04 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2558da4-6503-3b21-9098-4b531420d399 | -12.75976 | -44.54547 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7f127d7d-8dbf-325a-867d-dc3064ee4280 | -9.11565 | -61.4871 | 2026-07-04 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 428734b2-e8e7-3df4-a49b-498142f44b54 | -8.69183 | -54.56543 | 2026-07-04 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddb31df-4f1e-30b8-aadb-3fdaea636247 | -10.12542 | -52.08842 | 2026-07-04 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb92bb0d-0fbe-3461-9164-fbef268f5c54 | -7.73584 | -44.17406 | 2026-07-04 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3bad83e-8c58-3c53-9ba0-480f7c9305e5 | -8.39557 | -44.04386 | 2026-07-04 04:46:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e480580-4e17-36fd-b82e-66bc29b6c496 | -6.4273 | -55.79604 | 2026-07-04 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70800069-661b-3e1d-a27d-7233028da556 | -10.92731 | -43.05694 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2fa4f46-b65f-3866-8e39-eb19eb574211 | -10.90778 | -56.86015 | 2026-07-04 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d3c6dd8-0253-354f-be35-320360227dac | -12.75906 | -44.55091 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 4d247387-7ab0-3104-bbc2-a6f982f6885a | -8.58486 | -47.2441 | 2026-07-04 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73d43829-1203-37c4-af6e-7d43f4d86052 | -10.92288 | -43.0498 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c9c41b75-50e3-3d81-9241-1ac5b5a3dd7d | -10.98321 | -43.71236 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d237e981-0d74-300d-b821-86c9bdddd2cd | -8.45085 | -51.57071 | 2026-07-04 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e70a9598-b690-3dd4-9bda-347658c848bf | -10.78673 | -54.10586 | 2026-07-04 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecb6fdf1-1f28-3ee7-85dd-3f39ffef597c | -4.69737 | -55.98738 | 2026-07-04 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7edec36d-b9fc-3ea9-86b6-7b8560c25b3d | -12.75307 | -44.55082 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ab8d10db-14ed-34c4-ad3f-f3c8ee1d9c8e | -11.42865 | -46.57876 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5d9d69cb-9f2d-3cde-90a2-28bc0eab201f | -11.45722 | -46.58559 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08e4fff7-e6b4-38c5-bc04-eb5e97140bef | -8.72548 | -47.84233 | 2026-07-04 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a716df8a-ce16-3cd7-8395-b0258e00391b | -12.75009 | -44.54416 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 198745b8-8c26-317b-816b-b548f5c70e1e | -7.62687 | -50.0382 | 2026-07-04 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 131a4358-75cc-31ec-a312-18c0d2eb9916 | -7.23331 | -47.11388 | 2026-07-04 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4f322c4e-8b71-301e-8fc1-047b70f32967 | -5.79775 | -43.63699 | 2026-07-04 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdecabe5-c1dc-392b-865d-487ad9ce1d05 | -10.90381 | -56.85947 | 2026-07-04 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41e96791-8a00-31ce-9e54-a1de81a908bc | -10.6239 | -53.89636 | 2026-07-04 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c6f6ce4-4e09-3f94-8e6d-7a5978e8ebf5 | -9.66351 | -56.49481 | 2026-07-04 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d1dcfd3-d4b3-3ccd-9321-5c8951d0e179 | -10.74942 | -48.45 | 2026-07-04 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ada2445-9389-3562-b36d-8fb141f066b7 | -11.45609 | -46.56283 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6fe96ec-d777-35e4-bc24-66070845006c | -8.07861 | -47.37336 | 2026-07-04 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3baa8752-5f58-3db6-af4d-1fd0594214d9 | -5.63994 | -46.68025 | 2026-07-04 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b80af9a-714c-353f-a809-99825652c907 | -12.75372 | -44.54539 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| ac416e4d-8119-3c74-b410-d28eb7d4600b | -10.94417 | -43.04943 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a991d91-a853-3382-b511-afcb5ecd8cd8 | -11.62319 | -50.35371 | 2026-07-04 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bf9d98f-fc86-3758-ab8d-6db11354c3a7 | -12.52779 | -48.28957 | 2026-07-04 04:46:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c95927d9-580b-3fed-a02f-b9d7f8ab55c7 | -12.51349 | -48.25395 | 2026-07-04 04:46:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95097a4b-7855-36ce-9087-669b45e54129 | -8.70631 | -54.58917 | 2026-07-04 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3235938-d4d5-3833-a48f-c33bd98643a0 | -9.02413 | -59.54158 | 2026-07-04 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4615d182-265d-3d16-b7c1-b31566badf2e | -5.4689 | -45.42327 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11c4548e-d1b4-3874-8191-de70bd5b8388 | -9.80704 | -48.91828 | 2026-07-04 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e65dc5e0-5c9a-37b8-a0bc-e2ce9e9c4ba3 | -12.76274 | -44.55215 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2870f4ae-65cd-39a8-9b4b-89ee4d4822d9 | -12.74734 | -44.52718 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3cc2d21a-df98-35af-ab97-08e93e8a7680 | -8.75899 | -47.40399 | 2026-07-04 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b212c4f-a5d2-3f77-b575-6b79af6b6f5d | -10.12102 | -52.09487 | 2026-07-04 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d9edf75-f2ab-3e32-a093-901c708055f4 | -5.52373 | -50.02483 | 2026-07-04 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83819ce7-1bf1-33e4-88be-91e11912b4cd | -7.23403 | -47.11147 | 2026-07-04 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a22e495-2c9a-38ee-be0b-fd5319016b64 | -8.70827 | -54.66644 | 2026-07-04 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef65a79d-093a-3b1d-8317-c9c9d5659e98 | -12.75492 | -44.54483 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 431f607a-04ee-37c0-841b-54db13cabb94 | -7.80712 | -45.22245 | 2026-07-04 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d66d3a01-4027-3470-9a4d-ab7f4a5810d7 | -9.43662 | -40.32013 | 2026-07-04 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c0784d18-75b8-3568-b43f-c89f21fd05c6 | -12.76327 | -44.51831 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f1a29e7-12fb-3531-b50f-29a1cdd826fb | -5.80136 | -43.634 | 2026-07-04 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa0238ad-c953-3a6b-84e4-136e67856fa4 | -11.80958 | -52.52267 | 2026-07-04 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb2568ea-ee7b-3e35-989e-a9a55598780d | -12.75702 | -44.51815 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2737e5c5-d6ad-36e3-aa5f-fb4cd562114b | -11.92279 | -43.38665 | 2026-07-04 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d741149f-86f6-33ae-9b53-7c92aa7f0086 | -9.44249 | -40.32046 | 2026-07-04 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| bd242436-acba-3af8-a8db-0e1119aaacba | -5.93914 | -46.35114 | 2026-07-04 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
