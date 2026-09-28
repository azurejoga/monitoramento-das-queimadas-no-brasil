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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5b761f2-864f-3b06-8bc3-f766b3e32049 | -4.67725 | -43.89576 | 2026-09-28 16:26:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 018f98f4-590d-3ab0-afe5-ae61aa1012ac | -10.97401 | -50.6917 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 607ca42d-6291-30ab-9dd1-d36eb44e9242 | -8.38078 | -45.46413 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4bab3e93-446d-364f-b991-334c8379adef | -4.37109 | -43.06639 | 2026-09-28 16:26:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a5c8881-b567-33fd-bf5f-359f8605afa4 | -9.3438 | -46.53928 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8e8a59e8-e8ad-3321-b73d-b7b67ca86e72 | -9.82773 | -45.26995 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 84d25efb-ecd3-38d7-a2ea-ab94a116fcee | -7.41877 | -55.6334 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 48714ec3-8e3f-33dc-afe5-38d84c9645e0 | -8.96463 | -44.16629 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ffd27d31-6c63-300d-aa3b-e242994068ff | -7.72817 | -44.90979 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99ed2e5b-085d-3de3-b3b0-3eb8093b2c97 | -7.39548 | -38.84758 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 545a7264-9b1a-3132-a4b6-af43ba246666 | -10.93371 | -50.66731 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3b95c33-2eae-3c6c-8c04-e9b4f06277db | -7.18771 | -44.52015 | 2026-09-28 16:26:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9ce885c2-74c0-3ada-b76b-8e65a56c07e7 | -7.08993 | -44.40303 | 2026-09-28 16:26:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b485cff0-102c-3dae-81aa-0f52305abe1c | -7.76166 | -54.78589 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 59bb6e18-4e48-32ad-bac7-ee3e3e8e92b8 | -9.10653 | -49.89654 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b5fb793d-561d-3943-9d93-fc01e7de172d | -9.29872 | -46.44188 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 97f998d0-6ee7-34b0-ab95-a7a5af41db29 | -11.14946 | -50.06085 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| deb068ef-7034-3a95-af1d-c73fa0e143c6 | -3.33895 | -42.00803 | 2026-09-28 16:26:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 794cf9d1-b924-3a2a-9821-1132507cb044 | -11.14373 | -48.3179 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a910c5a9-a1fa-3413-b587-04e911e88137 | -10.45681 | -47.48008 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 17351baf-a844-3602-a52d-b19fc2a34fda | -11.13444 | -51.17163 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 68fbcf5f-3b94-3042-be12-b527aac6dd8d | -10.89216 | -50.67936 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 20b434b1-2ce5-3272-a447-1a43233b4e03 | -3.67564 | -42.67084 | 2026-09-28 16:26:00 | NOAA-20 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b4b1347e-b0a7-3fb9-8365-80681331d25b | -6.73139 | -43.01022 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1cb477e0-e2d6-3e19-8966-4e9542f90811 | -7.33579 | -42.08057 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 03dba0de-a06f-3114-8d54-31f685aebdaf | -9.0459 | -36.90368 | 2026-09-28 16:26:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bb52a6ee-197d-3f40-8287-db39f729dd82 | -10.95202 | -43.88884 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d328c0ca-e77d-33d2-84e3-be6dbe451829 | -8.1916 | -50.15833 | 2026-09-28 16:26:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| edd0af01-e5b3-3e59-9328-e8008f79e01b | -9.78965 | -45.81469 | 2026-09-28 16:26:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c46cbffb-2cc3-3a83-a000-b66003972942 | -8.83898 | -46.59506 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cdaadd16-b625-381a-a484-f8181bb40492 | -6.16268 | -52.81579 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 5b183198-b3ea-3084-8902-eeaaacddfa59 | -10.99541 | -50.69226 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| ded5387e-a6f5-32d5-a0a4-a283d447b7b4 | -3.14323 | -42.96112 | 2026-09-28 16:26:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c738a96d-5a12-3a25-ae7b-2ea502883d8c | -6.21825 | -46.63407 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 82c90715-9b7e-3d03-b187-c9312bfcefcd | -10.30239 | -48.16013 | 2026-09-28 16:26:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a7027c0-92d3-333c-a5e3-f0d03c1ec174 | -10.26153 | -44.62505 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| cdd0c200-c82d-3c13-890b-eb8135211397 | -5.79601 | -46.09151 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 0d7e709e-00ed-3e36-b2ce-4329b0223001 | -3.89032 | -38.73287 | 2026-09-28 16:26:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 122aa571-e0a9-3789-9ef6-c6106fdf5854 | -7.46957 | -45.06277 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 915911ec-7957-3851-ad76-74c784cfb3fd | -11.83227 | -50.6424 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 81a2525c-8d7f-3616-aa1a-d355ee95a5b1 | -10.16704 | -43.90163 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3665ddb5-ba5e-3e95-b24c-21d361d1875e | -10.73679 | -48.766 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 867dbef8-2a67-345e-8f5b-acda5971c840 | -8.16478 | -47.63593 | 2026-09-28 16:26:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7c73a526-f7d0-3afc-a2be-56d526960018 | -7.50177 | -44.56112 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 7e840ee6-cda9-30ba-8e2f-7464751ef523 | -7.26133 | -39.71205 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f5451407-6a40-3939-8a68-4d22c4ccdbfd | -8.66958 | -45.3439 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8b90b0c1-fcd1-3930-9d65-638ac27fb29b | -3.2044 | -42.47646 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9800195e-fa75-320f-975a-6fb5e8563b22 | -8.77356 | -45.82491 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 68defdda-1b82-33c3-8eb7-d1d145d3e37b | -6.76667 | -45.36916 | 2026-09-28 16:26:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 52173ec3-e4a7-3e89-b703-8b24608a6018 | -11.15001 | -48.33072 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7559866-b888-3c35-b7ad-2aac96ea2464 | -7.26335 | -43.36484 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d9e7ce3a-1cba-3477-851a-5995bdd470b9 | -6.35904 | -45.81293 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 9c07cf47-1dcd-3641-9699-a39f44eb9afe | -11.14556 | -50.07033 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 48faf8f9-df4b-3ad4-9b17-ec6f3d9845bf | -7.49434 | -44.5584 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5023e82b-d463-3921-98c8-096c6e6cb57d | -8.73701 | -44.23508 | 2026-09-28 16:26:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6ac87843-bc18-360c-b15f-aa9b714afce9 | -4.95966 | -37.59211 | 2026-09-28 16:26:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d6c49250-cdcd-3514-acc0-8ef2fbd19e9b | -7.38594 | -42.09681 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 91c2f0d3-027d-3e20-a962-3c412ae8506a | -10.90841 | -44.65753 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 53c4b59b-c285-349e-8c82-3aa2d7fce4a4 | -7.71073 | -44.91234 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a84c2fc3-1801-31ca-a12b-1fc907f880a2 | -10.12155 | -50.1922 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6178e54f-a4bc-312a-ba1b-56d24a899ff1 | -7.50154 | -44.56144 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b29cf5b6-705e-3169-8a2d-c1985bb733d5 | -9.11767 | -49.9059 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ea00c855-8925-397c-9c91-b18f5ebbdf44 | -6.3095 | -43.60747 | 2026-09-28 16:26:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 62ebb571-e0a3-3128-91e1-1b71c35fb91c | -10.91063 | -50.65736 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dbdc1bd7-1965-380d-8a5e-50947d7aa645 | -5.73049 | -53.4589 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 16040078-c172-32e9-9089-9047a67ddc95 | -10.21052 | -49.98119 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3d68d28c-d264-3649-a112-c0c75295aa7f | -4.97505 | -49.62275 | 2026-09-28 16:26:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 86a4ebb9-4b5f-38ca-b619-411b4dd44265 | -7.31027 | -44.19308 | 2026-09-28 16:26:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83be8659-2b55-3ff2-853d-f9f47d1163a5 | -3.20494 | -42.47996 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 339d6ee4-dadf-38f8-8f93-a5e87b7abad1 | -10.74443 | -50.90042 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dc57c140-0baf-31ed-889c-3e37f47baa9f | -9.15371 | -46.7527 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e0ec886f-552b-3278-84fd-ff1136248ac4 | -8.36881 | -45.48289 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 68d90702-08fd-3ea6-89af-5be9573f0334 | -10.11654 | -50.19286 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e2e28178-d039-3183-9fe8-143d9625e1b2 | -9.93964 | -50.24381 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 22b855f8-b6f6-3f77-b09c-d0f3d8ec6e31 | -10.35806 | -41.01178 | 2026-09-28 16:26:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 92c05b4f-1296-3b5c-af5b-ca85cb709f8a | -11.17621 | -45.12678 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c9b56fe1-1b8c-39d9-9472-83bcdd01614a | -9.4889 | -46.35775 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d0baa581-de76-30f2-b423-7103a286e32b | -3.34292 | -43.33508 | 2026-09-28 16:26:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 39a65687-46ea-3c22-98e9-5c61414f9d02 | -8.89777 | -37.21361 | 2026-09-28 16:26:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 29204328-b091-3a4d-9501-1adbc7b58f69 | -7.45018 | -44.59191 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8591f27-0cde-3057-9b35-886532530511 | -6.73417 | -43.00626 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 7148db4a-fe20-3908-b3b8-df801d240538 | -8.16957 | -44.44272 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 409760eb-211f-36c8-a839-d8a410b8f37b | -7.64164 | -45.52055 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4cc0ca38-ca04-30f0-af4b-21c15f9e0e94 | -10.99582 | -50.69551 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| cbfff221-099b-301f-a898-7fd0865e9fe1 | -11.75687 | -50.7655 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1b696c94-9004-359e-8774-ae4c5211343a | -11.13488 | -51.17515 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 77bef038-cafd-3050-9441-abceb5145a93 | -3.67178 | -42.66787 | 2026-09-28 16:26:00 | NOAA-20 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b676ea8-5248-302d-ab3c-71c03898b15a | -10.29853 | -48.16464 | 2026-09-28 16:26:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 963ea677-0a4b-3a8a-902c-168937574df5 | -6.36849 | -43.36974 | 2026-09-28 16:26:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70731831-1248-3e94-8d6b-1205a3715a33 | -10.27823 | -49.94828 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ca507e23-547a-36ce-a49a-32a749513b7a | -7.63033 | -45.5183 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d16b744-8ebf-387f-821c-f239ac9cd6b9 | -9.93314 | -50.23285 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b42dc2a4-b6ed-3bb8-a191-b51f40a16c89 | -10.94339 | -50.6595 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7016408e-fb53-33cc-a095-c431893794a4 | -8.71642 | -46.71485 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b6c4dea9-196d-3599-ab28-dc160a8aa3af | -7.23004 | -44.85675 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 86b947ef-8167-35cc-9ce9-18069b9aaa17 | -7.30766 | -44.59803 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f3e61320-0296-3a84-96e3-85aa6d280f68 | -3.97505 | -41.52576 | 2026-09-28 16:26:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 75934e9e-fe23-34a6-8291-1f3185dfe166 | -6.33448 | -38.861 | 2026-09-28 16:26:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 8ae7a636-c50b-3d5c-b04c-9f6c3a7d1349 | -9.32394 | -46.56701 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2db5aef0-ce57-3f57-b639-526cb0b15116 | -4.37971 | -40.60792 | 2026-09-28 16:26:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |


[Clique aqui para ver as próximas entradas](README116.md)
