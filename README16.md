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
| af18b23d-40c4-35cd-ab96-2d1e0489741b | -7.52336 | -44.68037 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92507d79-e9f1-381c-81d9-1f970681d232 | -7.29027 | -44.47983 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8600c2b3-bf1d-37ae-a3c3-585347557282 | -6.08997 | -43.26154 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0d7aa7f6-fbb2-3d02-bf56-3d986f5af507 | -6.3149 | -43.43808 | 2025-09-12 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95db32c5-c139-3e04-b5b2-b61ef39904a7 | -6.81375 | -45.6472 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8222780-2f81-36d0-9f6d-2207e17d027e | -8.62467 | -40.19913 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8215541d-fdbd-328e-a4f0-ee3957bf16d4 | -7.55723 | -44.39479 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40fa45d4-1c2a-3349-856b-b02cba030731 | -6.26093 | -43.48515 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1e6c99c-1e0b-32e1-afec-41a0919988fc | -6.67513 | -44.14373 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dd4537c0-cf1f-36fe-b424-02fc62063c86 | -6.44729 | -44.03913 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 592e70c8-eff7-375b-8981-d07af759b8ac | -6.42332 | -44.50689 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 789722b3-bef0-30d2-9822-8f44469b8c65 | -8.18993 | -46.104 | 2025-09-12 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 11b40069-a6f4-3ba5-8c57-940f76a25966 | -6.30045 | -42.22932 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0341efec-f7fa-38d5-b2ac-ad9f7fd661e8 | -6.67303 | -44.14797 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| caa13b01-8fe7-3c96-80fc-10e8f6fc6970 | -6.96413 | -44.83054 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad8cd753-1700-394a-962f-3703daec86e2 | -6.18186 | -42.75043 | 2025-09-12 03:36:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5bead78c-b7f7-36a2-aa88-5089615e577f | -6.41243 | -42.60635 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9df02e83-57ce-3b59-93e1-97264ff3b688 | -6.6849 | -44.1478 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d26433d-c31a-3bb2-8d71-966e74446af5 | -6.41297 | -42.60319 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1826f33-bf72-3968-b313-85c5444b806b | -6.10097 | -45.93637 | 2025-09-12 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e5c18478-cad2-3814-841d-efd7c3de8b3e | -6.17747 | -42.62244 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f04d7013-a5f8-33c6-bf4e-f8f5d6fbd817 | -7.44292 | -44.98742 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ac516cd-a18d-390b-90c7-be80c21ea5a0 | -6.65137 | -44.13662 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c5b3776-ca2e-38ab-8a14-46335b1376ba | -7.29968 | -44.35894 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65d005b2-9ed4-35d0-a2fd-f3dd18bb99d2 | -6.25421 | -43.42775 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7f552d0-d241-3d8c-8641-2642d391a8ca | -5.59884 | -42.91447 | 2025-09-12 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1f5d5041-512c-39ae-bf9d-8ea5f225e5b7 | -6.48194 | -45.15625 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 58b4f7ee-4a0d-3ffa-9a85-3b9abae0c37e | -8.37286 | -44.84841 | 2025-09-12 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 905f75e4-c830-3f85-9861-617caf2a88e3 | -7.29607 | -44.48085 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7085e138-670d-3eca-a5a2-e86aa1838f3e | -6.2495 | -43.42313 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 985f2c60-6149-3358-b445-84c5682e9103 | -6.7085 | -42.04772 | 2025-09-12 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b0ef5b3-6a4c-3b1c-b4e8-47cc9ced94b2 | -6.81685 | -45.6461 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8e2cbcb-e445-359c-9807-7b87464d2671 | -6.47619 | -45.1532 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48b0edcb-69e5-3024-8718-e2b720fb3732 | -6.67378 | -44.15108 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ca4b9eb-f88f-3e53-a2c0-ce65ae6b75ec | -6.15146 | -43.36591 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b64e352-517f-3727-a368-68b2d0a4e919 | -5.96577 | -44.72409 | 2025-09-12 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 90cdf0cb-c373-301b-bfbc-b984ffb7d79f | -7.40769 | -44.36313 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59d09a4e-617a-3917-a03c-dcce29873717 | -8.36779 | -44.84322 | 2025-09-12 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e5902ed-fc6e-3aa7-86a9-26a74e08508c | -6.48778 | -43.87628 | 2025-09-12 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 48139203-a9bb-30bd-9b50-fade32e38af2 | -6.1741 | -43.36606 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13cb1285-7473-341a-b848-0d937b77ae69 | -7.15238 | -44.34841 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f087bf70-8daa-394f-b237-af311c4bad7d | -5.59942 | -42.91107 | 2025-09-12 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 340f755b-ef98-393c-b21f-7c59ad035cf5 | -9.01676 | -40.34487 | 2025-09-12 03:36:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32b7c41e-ce8a-308f-9baa-41ea15c4cbeb | -6.45378 | -44.0692 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59497664-cc76-35ad-96e3-5ece732a6c92 | -6.40425 | -42.596 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78dea8db-a9db-3cf7-816e-4986b5fdb459 | -6.30659 | -42.2242 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a4dce313-a94c-3374-a06b-3f8e27e90653 | -5.94758 | -42.79026 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1b65f4f8-b039-36ae-b59a-5f6a5b437391 | -6.44757 | -41.76328 | 2025-09-12 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0b905730-7598-3360-96ea-68915cb77c96 | -7.18056 | -44.87473 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1baa53ef-803e-3d0d-9701-bbb974856592 | -6.25498 | -43.42427 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 167cda45-16d2-3ad3-b668-2a292d51f4aa | -6.68072 | -44.14555 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dfd9e2ca-7c5b-3665-a519-52adea03e385 | -6.44677 | -44.07543 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9b5c461-516a-3e85-96c1-d34f71d1b5a3 | -6.30202 | -42.22039 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e346aae-57bb-30fb-9653-4f74aee31586 | -6.27438 | -43.66669 | 2025-09-12 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e4c5ece-7fc9-3dbf-998a-4f01180ae796 | -6.4475 | -44.07129 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 227664f0-f999-33d3-a66a-d222a53e22d0 | -6.28037 | -42.40469 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 92dc707c-b008-3b79-aa11-e5500aab2b6a | -6.59515 | -44.31818 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bea69ccc-67d8-3ba5-b538-1259874eb1c1 | -6.18218 | -42.62637 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4c938384-c43c-30d7-aeb7-0b7a14d5f425 | -7.85368 | -44.80733 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1536a8f9-1a28-3566-b575-0203dcda7193 | -4.48827 | -38.42023 | 2025-09-12 03:36:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b24cd0f7-44d2-390d-8f19-f83c17f0f27b | -6.30553 | -42.23026 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| df52f44e-77ba-37b4-ab30-8b03b6e6dc3a | -6.17692 | -42.62564 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ed037c4e-6771-3629-a3ef-25b6088f4287 | -7.44681 | -44.44184 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3218acdd-e696-35d7-a79c-a5c983f3d955 | -6.33908 | -43.05041 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03ec0ac9-45c9-3945-900b-558e0fe85c37 | -6.18244 | -42.74717 | 2025-09-12 03:36:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 85f8f091-3254-3e33-b9b9-d7bde016f527 | -7.17544 | -44.86924 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1cc28de-3686-3fca-b634-b13b6b00413c | -9.739 | -45.42331 | 2025-09-12 03:38:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 245f9eec-f6d1-3593-bf50-d18461d87dd1 | -9.34717 | -46.59137 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f8a0ffb-6321-399d-b877-12080d956eb6 | -15.10784 | -48.02108 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f837e9cc-0686-3cf9-9a85-75f99b6e2d68 | -12.10578 | -44.86522 | 2025-09-12 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 191d1fa0-2a6f-316e-a53e-0b72ca21e2e4 | -11.67778 | -46.67912 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 049a7f21-6b57-31f1-a625-70d003f71954 | -11.67104 | -46.61649 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 37900b01-f0c4-3a55-951c-9f9a5e067e25 | -10.78679 | -47.26494 | 2025-09-12 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6774ea75-4e69-3f36-9fbe-2050b7f5197d | -11.68507 | -46.57807 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 875b853a-91ff-3dca-be67-c397680ef6eb | -11.15513 | -45.29883 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d139da83-dc71-36d8-abfb-3da5ab5a6fdd | -11.93794 | -44.30582 | 2025-09-12 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa75ef7b-81e1-3711-8200-c878b26ac1cd | -11.42959 | -43.54245 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9ff218fb-e238-3434-b240-bdf2e0e6fcba | -14.12957 | -45.37589 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d98806a-1b38-384c-bd50-1cf93f11320d | -8.95143 | -46.09415 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b071a3-d44d-3da9-8d8a-2b78e1da5a96 | -10.85716 | -48.15868 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb1a4168-7133-3303-b6a2-432f2de5c514 | -15.10273 | -48.01418 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6aa03341-cf97-3a77-b090-5e2448bb0fce | -12.01884 | -43.78886 | 2025-09-12 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af761a9b-9ace-34bc-ba63-b02b607780f5 | -10.65625 | -48.65877 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 92ea5a33-5b21-3f44-86ec-864ff0bfa335 | -12.10985 | -44.87351 | 2025-09-12 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f55a5947-d59f-3dea-88b6-c16a5060c9b1 | -11.69748 | -46.51561 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf2eb885-fab2-34c7-a698-e4aa006ac05c | -11.42507 | -43.53845 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f5e3588-3abf-3727-8e1c-f3f7c96d8192 | -9.08087 | -46.95283 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 59278e99-59c8-3d8d-9216-1b1fc611a07d | -9.93791 | -42.33018 | 2025-09-12 03:38:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2097edf6-bb75-33a9-8c71-edd071c28d1c | -15.68996 | -47.01441 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 591df515-a2a9-303c-92f0-461a9efd3be5 | -9.10918 | -47.12249 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| daac4a39-54cc-33f9-a825-aae5cafa83f3 | -12.86181 | -47.95432 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dec194e7-92fc-3ee0-ab86-4431f1dcf5e9 | -12.8332 | -47.96135 | 2025-09-12 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9fc374b6-a1bc-3a1e-97cf-5e4605f38896 | -11.93655 | -44.30616 | 2025-09-12 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2967dce-34e9-3772-ab15-090c835532ca | -15.24619 | -44.03897 | 2025-09-12 03:38:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3d5b1b0-a9e8-3539-b202-a313c901bdbf | -13.89634 | -48.22802 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52fe2daa-1a97-3bde-9091-42d42830170a | -11.67465 | -46.56645 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 171bbb9c-55bb-3c12-9f8a-8a1f0967fb8c | -11.44429 | -39.50832 | 2025-09-12 03:38:00 | NOAA-21 | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a0d18484-dfc7-30a0-a3c0-39d112a59615 | -9.71996 | -48.30395 | 2025-09-12 03:38:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 97aa7d53-77f9-30e0-a12d-e61bb07f4511 | -9.05563 | -47.04634 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ca610d29-32a7-3745-8f87-98a855d3b9a8 | -9.10802 | -47.12846 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README17.md)
