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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82bd7f51-941e-3728-bec6-11f02e073b60 | -6.74286 | -43.78542 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de6264e4-6488-38d7-ba1d-968628d1d94b | -7.11314 | -44.77943 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a865613-fdb4-36d1-b864-367de5058156 | -6.5775 | -43.70024 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 716c361c-89bf-3d0a-aead-d26ae1dac26b | -6.75192 | -43.79288 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9fe81c02-be3c-334d-91b6-0987c9a1b4c1 | -4.91346 | -43.19168 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bdb0565-f61f-3a47-aa0f-4ba27e73e41d | -6.36938 | -43.56269 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 180fa2db-51c5-3758-bf7a-1868e91d52b7 | -6.57148 | -43.70517 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9c06d6b-4f5a-3463-81ea-30d261faa251 | -6.49765 | -43.56562 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd0c88ce-715d-3ee9-88c0-1fbdca8b1915 | -6.93636 | -42.02034 | 2025-09-01 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9e2ca323-0b8a-38bf-baac-d1034c6933a0 | -7.06725 | -44.33897 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 07af3f35-ebd5-3105-ae5e-816f452c1e7a | -7.08739 | -44.34626 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| a45ee401-3dcc-392a-8bd7-7e0845768f43 | -6.41873 | -43.96328 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a708a745-67f9-3041-8e4a-7c56886365f2 | -4.91394 | -43.18884 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb5a44e-015b-31b1-bf69-349e12b2a281 | -6.37725 | -43.54684 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 932534dc-4bdd-3136-9ea5-86187168c487 | -6.27696 | -43.53135 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c216b594-275f-389e-a2ff-50a29c83f365 | -5.36096 | -41.14706 | 2025-09-01 03:42:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e3c55c0-8131-34c2-b7b2-caa5a67e38e2 | -7.08851 | -44.33991 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 78d38913-ff2a-3fa8-aded-7e6041f1f775 | -4.73307 | -44.44791 | 2025-09-01 03:42:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2c3d044-dc37-32b8-9ce5-c20d6bae268a | -4.15607 | -46.78257 | 2025-09-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6e7f534-ea40-303f-846f-8d97dbfc8f9b | -6.8069 | -45.68748 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06be0eef-efd1-3324-9f7a-fa63835affc4 | -7.25026 | -44.06696 | 2025-09-01 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb7254db-354e-307a-8a94-775be4e94768 | -7.06669 | -44.34214 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4ef3257e-d190-3880-9e6b-6f4c7a970090 | -6.24519 | -43.38187 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68199f6a-f001-37a8-9acb-6e7e38659ac8 | -4.15338 | -46.786 | 2025-09-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 713c6990-3bd6-3485-bff2-e407115fc76e | -6.45925 | -43.95793 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 367a8112-fe72-308d-9a47-c7fb2ec1ca3d | -6.74635 | -43.79508 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b7c7e931-5e5b-38c5-894f-c6285d55bb2a | -6.35424 | -43.9239 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9a00a74-2782-3ea0-b803-ea375f833125 | -6.3004 | -43.63297 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 077a429f-c91e-36a0-a5d1-0cdf82f4ced3 | -7.07532 | -44.35387 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e41bd80-5db5-3b51-bbb6-10156b0206c8 | -6.81492 | -43.34521 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 35737163-6c34-3043-9999-554ace44aae2 | -7.06956 | -44.35606 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 824a6cd5-e223-3816-9644-0e99edcbd705 | -7.24624 | -44.06004 | 2025-09-01 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c21a842-341c-3945-bbb4-88317362ff56 | -6.64051 | -43.96191 | 2025-09-01 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe90a5b9-b73d-33b5-a609-37311f2769dd | -5.85238 | -42.53466 | 2025-09-01 03:42:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a0e14bb1-bee7-3c4a-9529-bd19604d73e1 | -6.81189 | -45.69235 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5fdc3848-a5b6-3cd7-b1cf-b07dd1397d57 | -7.11618 | -44.76236 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bcc83b3-22a9-33c6-a7fa-d1f1a927fbfd | -6.75244 | -43.78991 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7aa503bc-84ba-3e3d-88f8-2a0cbcc183d1 | -6.41516 | -43.62592 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 158ca19b-0936-36ef-8858-ef403b2f9ba7 | -6.26853 | -43.55051 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19a7b458-9d29-3a10-97b5-d22ef7749a0d | -6.18556 | -43.31488 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86202fee-5678-324f-b30c-6449d04dd102 | -6.28291 | -43.52658 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72a88efd-3f77-395c-abb5-dff7ab0b961f | -6.2415 | -43.3826 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 300969f9-dd43-3dd2-b8b7-35e72692ef83 | -5.31698 | -45.44869 | 2025-09-01 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe8f2ac4-9444-3da8-9876-d0e67deb546c | -7.24117 | -44.05902 | 2025-09-01 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 621182c0-8f9e-30b3-b4c7-e135c7fc9922 | -5.81835 | -43.2275 | 2025-09-01 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb536b91-609f-3035-9103-764590d03c90 | -6.16366 | -44.12658 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 850bb6fc-b2cc-37d9-ab85-b2f6c1700e8b | -6.35441 | -43.56011 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 353b7e67-01b0-36c3-a19a-ae251ddb8f33 | -7.07589 | -44.35062 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 50a766d5-0b72-3de5-9489-0ceeea312050 | -6.571 | -43.70795 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 652ffb76-8bf0-3e47-bc06-1ad7e419c20f | -6.74739 | -43.78913 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 019aa21a-26d0-32d2-ab54-35ce3b9e6b1c | -6.28752 | -43.55969 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c97f48f4-f65a-30b5-9f68-ac0f8991337c | -6.32733 | -43.53873 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 540f40fd-eda9-3d7c-bf96-15e3eb800ef0 | -6.51019 | -43.55227 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44677ee0-f4b0-37a7-aa5f-6968abe65f19 | -6.24091 | -41.80357 | 2025-09-01 03:42:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5a8752a9-29d7-3d47-8f65-a3a66433d6d2 | -6.26562 | -42.61199 | 2025-09-01 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2a03a484-8047-3b4a-8712-bbe4a765dd8b | -6.00576 | -40.22917 | 2025-09-01 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b8b23ec-459f-3a4b-9e5e-139d1e3a6f2f | -6.29932 | -43.55076 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a8db753-b909-375b-b7b1-86b3f0df8972 | -6.75851 | -43.78482 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1f2caa9c-3815-3f3c-bb62-52773ae4147d | -4.91988 | -43.18404 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f72b19f6-9bc3-361d-8fcd-8b06821bd00f | -5.29098 | -45.13765 | 2025-09-01 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 514fba35-e82f-3bce-9a68-45764c48b352 | -7.07015 | -44.35279 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e283041-ee67-3efc-ba4b-0111d12882e3 | -6.1522 | -43.33176 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af570cb2-1dd8-3376-a5e7-2aa841348fca | -6.78255 | -44.62954 | 2025-09-01 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4c999f9-fa9b-3221-88ad-b8bca54994ee | -6.30293 | -43.61866 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0230fe4c-5329-3eda-bbd8-9a993c871535 | -5.1186 | -43.2274 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dabb8ea6-47ad-39a8-8137-afe0c5789a0c | -7.10956 | -44.31152 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 950b8832-18d4-38a6-9c68-c176e20ec3bf | -4.15247 | -46.79134 | 2025-09-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b404d86-1245-3a75-85b7-f7e3d1534656 | -6.28654 | -43.56541 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19c2ab8f-c447-3f83-91bd-a8e880f60c00 | -6.84125 | -43.33827 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 603c9c58-6208-3c10-9c96-bdcfddd566d2 | -6.15417 | -43.34953 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 38bcee25-b8b7-31fd-a73b-cc7c0f15f66f | -6.46387 | -43.96164 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aa0d2c8e-3ba0-31e7-b950-5d66a42eed6f | -7.07647 | -44.34737 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8606cc32-0eb4-30f2-af1a-c2c5b7ca0dbe | -6.52107 | -43.54849 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ed85f0f-1247-36f2-9075-fae3c495f178 | -6.31197 | -43.62597 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a437a509-fa3a-37aa-84de-9b49269b5828 | -7.08106 | -44.35171 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| a81e9e43-77dc-309d-abeb-1c147ecae358 | -6.26739 | -42.61477 | 2025-09-01 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b00b503d-7c87-36cb-b695-97c3404dd94d | -6.16984 | -43.31785 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a6544963-6aa7-3ae5-ab20-16a54ce74c6a | -6.17001 | -44.12087 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b703a36-841c-315b-814d-e7ad7b6cf106 | -6.93698 | -45.56647 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6a69163-2b91-3c00-832c-da6e3ba1e766 | -7.25077 | -44.06403 | 2025-09-01 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a22b58d3-f2b0-359a-82a4-c92fff9fc0d7 | -7.08277 | -44.34208 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3411f817-abcf-3a4a-83ed-eeef2e0b6ecf | -7.08906 | -44.3368 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3d98221e-80c6-3e2b-8ed5-65877591aa89 | -6.97833 | -43.11541 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 183bb868-e921-3a82-b829-59373b65be39 | -6.83242 | -43.33127 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| aed5885e-0121-30dc-a858-a51a524c9a12 | -6.38223 | -43.54768 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd160ff4-4505-33f7-a8df-3aed13dbc3c9 | -6.4563 | -43.95939 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f86a05ed-2613-3e45-9c2b-dfc29517cff9 | -4.12211 | -47.65541 | 2025-09-01 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a558edc-21c1-3f37-871a-4378a21591f7 | -6.45258 | -43.95033 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b14fe5d-a311-36ae-af2a-98fcd14c0abf | -7.07415 | -44.36045 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 286c1913-3d65-32fe-bca3-a694222c9193 | -6.19065 | -43.34415 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be707f29-9da0-3c7b-8010-7ad45a34322f | -6.31146 | -43.62885 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1541f9c2-5405-3677-a906-fb0d2e1de5a7 | -4.64347 | -42.51875 | 2025-09-01 03:42:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 39e1bf4a-bf28-3cd7-98ed-4290bea40ceb | -6.00139 | -43.36417 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5eff5d50-756f-3c05-9cf1-d6fe96e29034 | -6.98312 | -43.11621 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1aaeaf6-1bfb-3c3a-88e0-6d35092f790f | -6.33279 | -43.56618 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 034cde60-ef46-3def-adc7-bc2130da805e | -6.26442 | -43.54451 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9096cf47-c501-36d4-9053-384cbb3f85df | -6.3782 | -43.54131 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a40321d-1752-315b-a7ea-8bb86eaddc17 | -6.1897 | -43.34969 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eff2ba8a-a966-3a4c-b4f1-573b2b00c521 | -6.50815 | -43.56421 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6add069-6002-3e6b-8424-4c92b9b544c2 | -6.8373 | -43.33206 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |


[Clique aqui para ver as próximas entradas](README14.md)
