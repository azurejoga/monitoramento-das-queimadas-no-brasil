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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f917732-fbb7-34e1-a122-c3ae1dfd63f3 | 4.92485 | -60.54939 | 2026-03-23 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cc2f705-3dc7-3588-bbfd-4b902232d827 | 2.64976 | -61.28889 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdd9d7d8-4abb-377f-b7fe-010214448c84 | 4.3743 | -60.77157 | 2026-03-23 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a287fcee-0096-3442-bde6-1d0961bc7944 | 4.39583 | -60.76487 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d98a7958-9bda-39fa-bfe2-e329045c54aa | 4.92446 | -60.54795 | 2026-03-23 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cba48423-6652-3e5f-90eb-a71581306e33 | 3.5405 | -61.81506 | 2026-03-23 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9461412d-00c6-31b1-8f4f-2ce28d87fd4c | 4.37376 | -60.77637 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5bd04380-eb5c-388e-b242-42e90560f9f5 | 3.94197 | -60.96199 | 2026-03-23 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f8018e7-a084-3d0e-bf19-7624e890c6e0 | 4.37326 | -60.77338 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e9e1c6d-43cc-37a9-8acb-1e8c4433e80d | 3.51462 | -61.38635 | 2026-03-23 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0167b023-9946-3372-a676-a0c53e93e2f3 | 3.49829 | -61.38031 | 2026-03-23 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82fac45a-bfb8-3aca-9308-1770aae38d13 | 4.37276 | -60.7704 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b9b574b-ea24-3379-9935-f4d6bc35ef76 | 4.2802 | -60.15605 | 2026-03-23 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a16732ee-611f-3b31-808a-9ee6e129a607 | 3.54532 | -61.81426 | 2026-03-23 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c798a644-9be1-31cb-9be9-f62c9b828627 | 4.37795 | -60.77002 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d2ec1cf-4cf5-3f3b-b87b-fedb6e47c119 | 3.23738 | -61.20188 | 2026-03-23 06:05:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8e61490-921b-311a-ad0e-5ae61cfed477 | 4.37743 | -60.76691 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8bfc357-37f8-3b12-8ee9-b1dc67e275e8 | 4.37428 | -60.77942 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2ff331db-2689-3d6d-9ab3-243e5c7f72c8 | 4.27962 | -60.15265 | 2026-03-23 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b9a4a73-f6b4-3419-9498-c9f16f4d90c4 | 4.39082 | -60.76629 | 2026-03-23 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ec6921f-0665-3fd9-8156-0b63c36edd6d | 4.92498 | -60.55095 | 2026-03-23 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e46c230-d693-3d8f-a682-f473ee4d861f | 2.95104 | -60.74445 | 2026-03-23 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebff145f-6976-31f3-ac71-4297a6b49313 | 3.50326 | -61.37949 | 2026-03-23 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 291d0c0c-be5d-33d9-927c-ac1b8064099e | 3.23689 | -61.19892 | 2026-03-23 06:05:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 663c3698-798b-3829-91d3-eb5b0003031a | 2.95051 | -60.74125 | 2026-03-23 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a6f93d8-a0db-33ee-bdb2-8cb8e85238ed | 3.93534 | -60.95374 | 2026-03-23 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fa52253-159c-3dcd-86f9-00a641e2a5bc | 2.65213 | -61.29229 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 204fc6fe-2a09-37b0-b83f-7de4cbc155c5 | 2.64673 | -61.30162 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9dbd2ac-afa2-3241-afe5-34f1755fb72e | 2.65582 | -61.29374 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99df8b9a-4c35-3545-a6c0-91dda5fe5ac9 | 2.64346 | -61.30312 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a810f455-2a4b-3e07-85e3-ef9e55fa3da4 | 0.73606 | -59.60817 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 628fa5e3-4c69-33d3-87bf-3fce98706158 | 2.65165 | -61.28932 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 262668c5-53c3-385e-afbf-334c661e8be7 | 0.99138 | -59.38568 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b8a51bb-dfb9-3e37-b585-f2f29f904edd | 0.98546 | -59.3866 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1805a7b2-641f-3f19-8736-8c5f5622348d | 2.64975 | -61.28872 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf223e7-fb1b-35b5-8e25-2119e179cc54 | 2.63788 | -61.30088 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddaf4142-2e13-311d-a115-60fb43e223b5 | 2.65077 | -61.2947 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca0f0647-818a-3665-aabf-8d6ef31677d7 | 2.64755 | -61.29623 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 731a2af2-c4a1-3191-a180-37a9d111dc8d | 0.98476 | -59.3823 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d5a634f-3fb2-3362-baa8-7d9adf009e85 | 0.73539 | -59.60398 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 588c73c6-95fb-3130-ac25-ccb8b6f76a8a | 2.63837 | -61.30389 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4ba0b4e-fa10-3f03-b81f-fe378087bc54 | 2.12059 | -61.22413 | 2026-03-23 06:08:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 127f421a-33a3-3397-ac8f-50047c7bb007 | 0.7773 | -59.8661 | 2026-03-23 06:08:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77a5aed2-43ac-36c8-9839-73b6b9066750 | 2.65026 | -61.29173 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71218eb3-86c9-3deb-ba24-06808434ff56 | 2.65127 | -61.2977 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4413fcdf-15fc-3420-91e2-34393b9586aa | 2.64724 | -61.30463 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0735f47-1492-3979-9ead-34cb24966199 | 2.64659 | -61.29026 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 122ee448-c3f7-3a11-8206-e0246b3caef6 | 2.65309 | -61.29827 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c717ac99-d9a5-366d-92e5-cdc36dea5e7e | 2.65179 | -61.30071 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30f934b7-17ca-3e10-a487-f36bfad462fe | 0.77794 | -59.87007 | 2026-03-23 06:08:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f64e1911-83aa-3bc7-9426-395ac6c6a97e | 0.98405 | -59.37797 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c63a15ec-f88c-3efd-a5d3-3c28f443f872 | 2.64853 | -61.30227 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ea73578-9f06-347d-a675-560db8d9d57d | 2.64804 | -61.29927 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ebc64c1-e7ef-3ec0-af3f-8a73dedd0c8a | 0.98996 | -59.37699 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 148c98b8-330b-3288-85b8-785e09102a14 | 0.78369 | -59.86916 | 2026-03-23 06:08:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07c53949-da66-3fe6-9183-55c00a34db10 | 2.65531 | -61.29074 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e98537ba-c6b6-38a3-be5d-d04057c84a0a | 2.65359 | -61.30137 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a84cb50f-1142-3598-833e-fd15f2c0e0a3 | 0.99067 | -59.38135 | 2026-03-23 06:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d02ae129-2197-33d5-8995-c198e5a6e0d1 | 2.65261 | -61.29527 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dba3e09d-17c5-3c72-a1f2-a61bdec68964 | 0.72096 | -60.2916 | 2026-03-23 06:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df2c0efe-f560-3a54-af02-b168c44e846a | 2.6523 | -61.30371 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf94178a-17f8-398e-aff7-464213d27a60 | 0.72656 | -60.29074 | 2026-03-23 06:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ab44d03-0cc9-3313-a8a1-0fb20911d0b5 | 2.64622 | -61.29863 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a6f8f07-a6d5-3ae6-9570-37e7a10925f7 | 2.64297 | -61.30011 | 2026-03-23 06:08:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da8e76d2-5ac4-3411-945e-18cf20fd5ab4 | -2.58036 | -51.9287 | 2026-03-23 06:12:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6b2b680f-358f-3b9c-9c47-5c8cc802d7ca | -2.58424 | -51.90431 | 2026-03-23 06:12:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| eff05dd4-290b-3662-adeb-779825c8bf66 | -20.17381 | -46.52334 | 2026-03-23 06:16:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7de6f547-e76e-346a-89aa-074ffea52f8f | -20.18433 | -46.51488 | 2026-03-23 06:16:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9b334e7f-5a37-360c-80ed-6142654f2738 | -20.1829 | -46.52504 | 2026-03-23 06:16:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b2476cd-82f5-3dd2-9be5-8cb45ee33aed | 4.3801 | -60.76931 | 2026-03-23 07:48:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b91e39a0-e6d0-3d51-bcdd-29515cbb5b10 | -5.34359 | -45.12524 | 2026-03-23 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7527a161-cebf-3402-b017-e325e797fc3c | -5.34507 | -45.1144 | 2026-03-23 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 39db70a6-bb58-32bf-84c3-39bc700cfef8 | -12.63865 | -52.13549 | 2026-03-23 12:08:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 96a859a9-5d80-3511-9b0d-d64d3be76b57 | -20.19007 | -46.52193 | 2026-03-23 12:10:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 513e57b9-67e5-3ebd-9820-a49a09dbde53 | -20.18838 | -46.5362 | 2026-03-23 12:10:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c29013ec-15a5-3cbd-8a3c-2b5208e21ba4 | -18.93324 | -46.98029 | 2026-03-23 12:10:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b7f19fe2-4838-3e7a-bcab-74f7a743ed2f | -20.192 | -46.52853 | 2026-03-23 12:10:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 97cc545e-5165-336d-ad1f-22b6493a08fb | -20.17752 | -46.53446 | 2026-03-23 12:10:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8b0ebe92-02bc-32c6-9ecd-cae36723cd00 | -23.03116 | -52.67357 | 2026-03-23 12:12:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 50d2a023-9326-3651-827c-9aa0cf77db18 | 3.913 | -60.9395 | 2026-03-23 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 12ce85cd-59ca-3b6b-8951-1056528107f9 | 3.4747 | -60.7775 | 2026-03-23 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| ffc8cd27-b102-3703-b73b-52c6c2536325 | 3.913 | -60.9584 | 2026-03-23 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 5db0903c-7b9d-3b69-b4f0-b467daa46b1e | 3.9313 | -60.9391 | 2026-03-23 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 6fb665ed-e085-3c99-a074-0dbf3672f334 | 3.9495 | -60.9577 | 2026-03-23 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 540531cd-9571-3b72-a7f8-8c2f779ee232 | 3.4747 | -60.7775 | 2026-03-23 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 2010542f-5015-3856-bfcf-f73e18cbedea | 3.9313 | -60.9581 | 2026-03-23 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 89f6d2fd-1faf-392f-9ae2-cae1605904fa | -12.6425 | -52.1453 | 2026-03-23 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 8ad9fa78-67fc-3617-9952-d9500e66c15b | 3.913 | -60.9584 | 2026-03-23 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 101.1 |
| f0d9011d-29a6-3e98-b8c4-4d4a75f6bac0 | 3.9313 | -60.9391 | 2026-03-23 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| a34a60cc-dc03-3c5f-917e-db0d6cb3c19f | 3.913 | -60.9395 | 2026-03-23 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 100.3 |


