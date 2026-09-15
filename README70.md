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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c83b43e-a07b-3bc2-9c5f-d297acfeb0f9 | -9.40759 | -50.10178 | 2026-09-15 06:31:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 41c72a2b-1b7e-3137-9ad3-440b773cb5d9 | -12.90733 | -42.76182 | 2026-09-15 06:31:00 | AQUA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a5db2a2b-1de5-3783-8ca0-336c21d41224 | -10.58294 | -47.73606 | 2026-09-15 06:31:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b7346992-6d57-3177-acae-a4016e35c316 | -8.57667 | -44.49505 | 2026-09-15 06:31:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b887155d-dc31-3c0c-ae1b-d72ddd5e6bd0 | -13.56815 | -47.89719 | 2026-09-15 06:31:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dd3ed0f7-e3ce-3560-99a0-16fa5afaf54f | -11.49399 | -45.78929 | 2026-09-15 06:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 02bd9a9b-95c6-3d4b-9105-c0f8954c8081 | -11.49078 | -45.75091 | 2026-09-15 06:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c524a6e4-2942-33bb-aef3-06bf6cb35a29 | -10.86581 | -46.30943 | 2026-09-15 06:31:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 225ae878-5a6a-36eb-bce3-ebcc40547b5b | -14.67605 | -47.99661 | 2026-09-15 06:31:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8f8f275e-716d-3633-93f0-15582b59444d | -14.20595 | -47.41626 | 2026-09-15 06:31:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8107d78d-9466-366b-a2ba-d577bec6c95e | -9.4117 | -50.108 | 2026-09-15 06:31:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 86e53f3b-2500-325e-800a-f38199e19849 | -15.57804 | -48.82361 | 2026-09-15 06:33:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c483d852-ee1c-3d44-affc-83ec407cc9b6 | -18.17022 | -51.76083 | 2026-09-15 06:33:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 15ba8042-0be5-3d7e-9585-33a41bf5081f | -18.16166 | -51.74112 | 2026-09-15 06:33:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 063a860e-3911-3b5b-bdd8-8d20e77479df | -17.98772 | -44.32698 | 2026-09-15 06:33:00 | AQUA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 252c11b4-0460-31cb-b72f-d151d27206cd | -16.97198 | -43.35166 | 2026-09-15 06:33:00 | AQUA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b8c5b740-5029-3b82-9df0-f35dc5270adf | -16.97053 | -43.36212 | 2026-09-15 06:33:00 | AQUA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a2e9a068-ae0d-3546-949d-c02e3b859be5 | -17.97866 | -44.32541 | 2026-09-15 06:33:00 | AQUA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| adc7dc89-50f5-3406-b8d1-d49bc53038be | -17.95211 | -44.25051 | 2026-09-15 06:33:00 | AQUA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7dc28315-9c8c-360e-8b82-56044da255b6 | -18.15858 | -51.75825 | 2026-09-15 06:33:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2b2d9815-45dc-3371-9fd1-85928c7dab6a | -17.95069 | -44.26053 | 2026-09-15 06:33:00 | AQUA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6c5cf7b4-a090-3a56-9e6e-5cc246e00932 | -17.84321 | -44.42949 | 2026-09-15 06:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 92499acc-5d55-3e47-8993-816c08db35b1 | -17.97726 | -44.33519 | 2026-09-15 06:33:00 | AQUA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 6cee6384-3835-3bb3-8f80-59b69cef0fdd | -15.57405 | -48.78672 | 2026-09-15 06:33:00 | AQUA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b6441e5a-cce3-3b68-9e39-6ac35ae3c97a | -15.53588 | -48.82233 | 2026-09-15 06:33:00 | AQUA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9093f598-5326-34bb-89fe-8ae75be2516d | -18.1714 | -51.7466 | 2026-09-15 06:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 54af65bb-709b-39bd-b9a3-b1e7f9952e43 | -14.1666 | -47.3876 | 2026-09-15 06:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8f3541de-e55d-34a2-9a0e-3c1e4ab815e1 | -18.1714 | -51.7466 | 2026-09-15 06:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 579f865b-ff95-3778-99b9-4d54c95dc216 | -11.884 | -43.8142 | 2026-09-15 07:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 288f3277-4e37-3fc8-aa3d-f8941f07e285 | -14.1666 | -47.3876 | 2026-09-15 07:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 8f98b23f-e840-3d67-b059-395593b8087f | -9.3572 | -50.137 | 2026-09-15 07:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f9003866-0d70-3e83-ad19-69f747d2d1bc | -9.3569 | -50.1583 | 2026-09-15 07:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1b6af92e-c08d-357c-b1e2-fe6463c69de7 | -16.1068 | -42.1354 | 2026-09-15 07:10:00 | GOES-19 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| 74782bfb-394d-3bcb-ba5a-dccf14612325 | -18.1714 | -51.7466 | 2026-09-15 07:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 1b30be19-ba06-3e46-869e-537f198b8988 | -11.884 | -43.8142 | 2026-09-15 07:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 5d0925af-8a20-3d7c-b150-eadc1dcc58c6 | -14.1666 | -47.3876 | 2026-09-15 07:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 7522a4c1-ff16-39a3-9e5f-7fdbf2d1aaa8 | -11.884 | -43.8142 | 2026-09-15 07:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 535558a4-44ff-35fb-8d5a-d6a793283125 | -14.1666 | -47.3876 | 2026-09-15 07:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c4c512e5-a331-3e10-9696-427a2f7fe149 | -11.884 | -43.8142 | 2026-09-15 07:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| a85d3c1c-eef2-3419-8796-5cf9ac2eb1e0 | -9.4142 | -50.089 | 2026-09-15 07:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c25a909e-3d38-307f-945d-fe367735d8a2 | -9.3577 | -50.0943 | 2026-09-15 07:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 1f71701a-ee7f-3376-bb75-cfb2368b364a | -9.3569 | -50.1583 | 2026-09-15 07:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| bd1999d3-65c6-327b-a0b9-225ae287e033 | -18.1714 | -51.7466 | 2026-09-15 07:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8b42d807-cf21-3b4b-a0be-e9c4116a8805 | -9.3386 | -50.1174 | 2026-09-15 07:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6892b8ed-d8fb-39c4-933b-db78ffafaafe | -14.1666 | -47.3876 | 2026-09-15 07:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 78ed3ad9-766f-321b-85cd-e3724bafee22 | -9.3572 | -50.137 | 2026-09-15 07:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 256.9 |
| 25126920-0430-3458-83cc-7fb17da1f799 | -9.3384 | -50.1387 | 2026-09-15 07:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 169.1 |
| dadeffe3-9ef0-37ff-bf22-79ffa8a3cf3e | -9.3575 | -50.1156 | 2026-09-15 07:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 8a354661-3f29-3ccf-867e-2bff2628fa25 | -9.3575 | -50.1156 | 2026-09-15 07:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fcb46f9c-675d-3f03-8b23-039e0a70e767 | -9.4139 | -50.1103 | 2026-09-15 07:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c8cdb044-9e1e-37e6-8b0f-1981b44d0b12 | -9.3384 | -50.1387 | 2026-09-15 07:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| be15e0e0-4c7d-3c8d-b5f8-2fc930ad7919 | -14.1666 | -47.3876 | 2026-09-15 07:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d45b8929-780a-39e4-83c6-39592d74abe2 | -9.3572 | -50.137 | 2026-09-15 07:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 057c07b4-c1cd-303e-a549-22b93e73e1af | -11.884 | -43.8142 | 2026-09-15 07:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6b4022f6-03d9-3af1-91ba-4990984b2c05 | -9.3577 | -50.0943 | 2026-09-15 07:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 941e232b-3c38-330a-93d7-b6e41a799dd0 | -14.1666 | -47.3876 | 2026-09-15 07:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 195b44fd-8c61-3e3b-9e98-04b1cc43205e | -9.3569 | -50.1583 | 2026-09-15 07:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 2a86d99c-55bf-3141-92a8-60e5316b2516 | -9.3572 | -50.137 | 2026-09-15 07:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 63ab470f-2cc0-3391-980d-63f62b02d4cb | -9.3575 | -50.1156 | 2026-09-15 07:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| b3d379c5-0bec-39cb-b9b4-3c49389ff181 | -14.1671 | -47.3649 | 2026-09-15 07:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ff3cbaa3-5554-39a9-a1b7-3537eb87c733 | -9.3381 | -50.16 | 2026-09-15 07:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a6634322-70fa-386d-a0e3-bb2f5c010b0c | -9.3384 | -50.1387 | 2026-09-15 07:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| 4ac832ce-7db7-3e46-a52d-b347300450c1 | -9.3577 | -50.0943 | 2026-09-15 07:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1ba536b4-b543-3c65-9e10-170c51d90afa | -9.3384 | -50.1387 | 2026-09-15 08:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| a6f57b29-3195-3d75-84fd-3407b847ed1f | -9.3575 | -50.1156 | 2026-09-15 08:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 4a2ee35a-207e-315a-8cfa-a2e8d5cc4749 | -9.3386 | -50.1174 | 2026-09-15 08:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 99fcc1be-ff9b-3e5d-84b2-b53cd7d7ed8b | -14.1671 | -47.3649 | 2026-09-15 08:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| cdfe8a0a-ca4a-3dd7-8104-7006af5109e2 | -9.3577 | -50.0943 | 2026-09-15 08:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 330af6c8-dfbd-3e9a-9938-f6ef75af2dbb | -9.3572 | -50.137 | 2026-09-15 08:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 925a6349-8309-32e5-b751-db9d266c8687 | -14.1666 | -47.3876 | 2026-09-15 08:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0a03d8e9-9bd2-3e43-8617-cc47a37a9f80 | -11.884 | -43.8142 | 2026-09-15 08:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8a8e43e2-7ac7-3c5f-b89f-4f9885f6bd19 | -3.74816 | -61.7491 | 2026-09-15 08:07:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cf20a0b4-0408-3d23-8d3f-d2471788df04 | -3.73605 | -61.74741 | 2026-09-15 08:07:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 31c0072e-40ad-33d0-80cc-3fd4a26dc1a1 | -9.41122 | -62.70875 | 2026-09-15 08:09:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b8354056-f7d3-32bf-b2c4-86e2f0528438 | -9.3572 | -50.137 | 2026-09-15 08:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 082d9e08-2329-3bdb-b557-42bb3d6286b4 | -9.3575 | -50.1156 | 2026-09-15 08:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 2332d233-1ebd-3d8d-af0d-074239965737 | -11.884 | -43.8142 | 2026-09-15 08:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 35481cd7-dd1a-35f5-8649-5aeb8b202f7d | -14.1671 | -47.3649 | 2026-09-15 08:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 3376421e-efd3-3013-8ca8-34f76de4a3a4 | -14.1666 | -47.3876 | 2026-09-15 08:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 465b821f-5282-3ba4-92b8-0d0bae4aed00 | -9.3577 | -50.0943 | 2026-09-15 08:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 824e5e72-392e-3131-8418-dbb67d2d697c | -9.3386 | -50.1174 | 2026-09-15 08:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| bac42dca-c6d3-3927-be2f-63a9ea387ab0 | -14.1666 | -47.3876 | 2026-09-15 08:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| de4f584a-217a-39dc-8cdf-e2ccf1172d82 | -9.3384 | -50.1387 | 2026-09-15 08:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c8985ba3-e611-3f18-979f-7148ac3941eb | -14.1671 | -47.3649 | 2026-09-15 08:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 47e3bb8b-dab6-35ce-ad62-2adfbc20e3e0 | -9.3575 | -50.1156 | 2026-09-15 08:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 2f3902e1-8afa-3be5-bc8b-3504a54f7120 | -9.3572 | -50.137 | 2026-09-15 08:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 290a893d-30fb-35b5-8265-79788963fe8c | -9.3572 | -50.137 | 2026-09-15 08:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 5d02c0cb-48a8-3530-8ad6-a88b03b51986 | -9.3575 | -50.1156 | 2026-09-15 08:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 636f3052-7ab2-3c0c-9fac-195ea48000de | -11.1699 | -46.3838 | 2026-09-15 09:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d62d21af-1ab2-338a-bb35-39324904e400 | -14.1671 | -47.3649 | 2026-09-15 09:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 3fe38d08-12d6-38d7-8d0e-54e06018a9d2 | -14.1666 | -47.3876 | 2026-09-15 09:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 238.1 |
| da139efc-8db0-3ca7-a2ae-8367ba2ed625 | -7.0 | -44.62 | 2026-09-15 09:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20384acb-b77a-326b-bc74-8b164396a1f5 | -7.0 | -44.67 | 2026-09-15 09:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a52803d-fd5d-3c9a-ae22-948555c1bff1 | -14.1666 | -47.3876 | 2026-09-15 09:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 538a5334-dc91-30b1-a06a-1940e2f5c38c | -7.0166 | -44.6184 | 2026-09-15 09:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 218.6 |
| fb3e95aa-7423-3fea-a67e-b7bc2ac6a407 | -7.0164 | -44.6413 | 2026-09-15 09:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 5fffc2bb-2ae8-39e2-9190-9ce217b73357 | -7.0166 | -44.6184 | 2026-09-15 09:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 21b89a24-321c-33dc-8829-3832f30a7385 | -7.0164 | -44.6413 | 2026-09-15 09:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 300.8 |
| 9aeb9297-b1e6-3188-95ad-01c7751e47cc | -14.1666 | -47.3876 | 2026-09-15 09:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e406c80e-d8f1-3e2c-8e51-c8ce8c948207 | -7.0352 | -44.6396 | 2026-09-15 09:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |


[Clique aqui para ver as próximas entradas](README71.md)
