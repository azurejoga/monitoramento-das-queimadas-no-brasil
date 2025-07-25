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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 067c9952-6eb9-390f-b19b-bb17127fd8c0 | -6.87738 | -43.10146 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58a8c54e-2283-3b6b-be26-1f1d737e1866 | -9.59269 | -46.33419 | 2025-07-25 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff8f8117-f0fa-3030-9050-03a9574eec90 | -7.84769 | -44.20817 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78479eae-bd79-3d9a-a09b-e16188afddd8 | -7.25427 | -43.06155 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| e31854f8-da13-32b3-a3a2-e56ffb85c17d | -8.21425 | -44.93888 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fe3f046-28f7-37ed-836d-b25d03c4e66e | -9.4269 | -40.34768 | 2025-07-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 00305c50-591c-3941-92df-e11daf858d62 | -8.29002 | -44.98555 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48833222-5daf-3d0f-84ac-a4af230a6790 | -11.78488 | -47.32878 | 2025-07-25 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ea38a27-a6f3-35ae-bc5c-142be1e87b22 | -7.89131 | -43.54087 | 2025-07-25 03:55:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce810e8e-1b02-3ac2-9a92-98802b5dd5c8 | -12.43514 | -45.38377 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f41904be-eff8-32be-aaed-3e3fe9227a16 | -12.04482 | -45.43071 | 2025-07-25 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d0e1b2d-e4a9-330f-8619-9e1e2676bfd0 | -11.44418 | -45.13491 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6164eafb-8e84-341c-9142-3222f95e7917 | -8.20568 | -44.93745 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17576f3e-6284-3c56-bb74-c211f084eb8b | -12.04551 | -45.42688 | 2025-07-25 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 311ca4ba-f007-3c43-91b8-e20b0c1709b1 | -8.76321 | -39.64338 | 2025-07-25 03:55:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b402ddb-36bd-3e5b-b66e-244ffef669f4 | -12.04896 | -45.43149 | 2025-07-25 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 859c4377-48e9-3917-a2a4-384102720b51 | -11.05424 | -44.78282 | 2025-07-25 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 583c43ef-deb8-3462-a5b9-a5a09d9173b7 | -6.88773 | -44.20422 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 515d3c75-40c2-393d-be20-25f31df0e4df | -7.89852 | -42.64348 | 2025-07-25 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fa831112-9c39-3806-8073-31bfd3f3f125 | -7.23675 | -44.79413 | 2025-07-25 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e83ae28-6874-312b-9e6e-3594719bca0d | -10.43028 | -44.17997 | 2025-07-25 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba164a59-f0ec-3fd2-8f20-2c6223115882 | -7.10374 | -43.55527 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5fb594c-7dd0-36ff-820b-3084cc568814 | -7.20927 | -45.33119 | 2025-07-25 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 768e60bf-4d49-3384-96b0-120f37d84670 | -10.61517 | -45.2392 | 2025-07-25 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 84b97983-1024-3a3b-a73e-746fca8cd7ca | -6.88186 | -43.12221 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0ba7fb4-51b7-3d4c-8d87-75f70c3ba3d0 | -7.10544 | -43.54499 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fd08443-67fd-3912-b18b-3213ab8682da | -10.62176 | -44.76526 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ecf3e1d6-d657-3d39-a705-9884aaeee65e | -6.87284 | -43.09843 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eaf98961-1b18-30d5-88b7-df14a51d93f9 | -10.62167 | -44.76517 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6794c962-393c-3fb4-a810-b2f4b4abf5e8 | -10.64331 | -44.76138 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eed692e8-0b53-3b9c-a429-5d21280d07bd | -11.45096 | -45.12064 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f23590da-41a9-3c95-9eab-b7dbdd02a1e4 | -7.56789 | -43.0668 | 2025-07-25 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74fd7736-80d3-3260-a34c-b121c0425dc7 | -12.65883 | -45.04335 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d3d0a04-79dd-3df0-aa1b-4cf3983e4e30 | -9.59177 | -46.33661 | 2025-07-25 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b514eba9-f63d-3cfe-ba46-8a7f57e0c637 | -6.89837 | -44.21756 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 433e8e05-a047-3aed-880c-247a71715f9c | -11.44007 | -45.13418 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9fdcfd9-a5c2-33d6-a527-f53259d0bb37 | -7.88736 | -45.53809 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3aa6c767-6ad3-3325-9f02-c3580bfdecf4 | -9.42747 | -40.34411 | 2025-07-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 646cd91a-2d90-3875-9cf9-2c02fd5cc91a | -5.73381 | -43.96035 | 2025-07-25 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f8672cb-7056-3b49-955e-854d70e93b5f | -11.45982 | -45.11843 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f3e1c47a-187a-369a-a6b1-e4cce68abf10 | -6.56938 | -41.49591 | 2025-07-25 03:55:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07aea1d1-ac7d-3181-b473-72ddf2e6c281 | -7.53533 | -42.42823 | 2025-07-25 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29c8aa11-dc8b-3a7e-8ef0-769833e36b77 | -6.91064 | -42.79354 | 2025-07-25 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf0eb08e-5334-3411-b53d-48c09277201c | -8.93268 | -47.34184 | 2025-07-25 03:55:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43e24c72-a18e-33af-a1f0-2ea9e7793b10 | -7.93953 | -44.08535 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07105cb8-a1e9-381f-b5b2-897d3f05a2b5 | -7.48266 | -49.23045 | 2025-07-25 03:55:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1288c62-1856-3644-8fdc-37e9e1152270 | -8.88999 | -45.57867 | 2025-07-25 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51141aa1-c77a-355d-84c5-aa155694b385 | -10.64266 | -44.76505 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e12cae99-2b35-3ce1-95c6-6fac60e6871a | -7.25812 | -43.06218 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 7d2ef10e-f75f-340c-929d-46b1704bd21a | -6.67652 | -43.96416 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3aba8ce-a75b-307f-9e0a-2e91d4021b8f | -7.4819 | -49.23458 | 2025-07-25 03:55:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f8cc7ae-06a0-369d-9c20-76e9072a7167 | -6.20206 | -44.38569 | 2025-07-25 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3edd6216-6d82-3423-ac70-3c3496e6c7be | -8.07772 | -43.1547 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 45e15c7c-03ff-3e64-b8df-c18873a5bbbf | -12.65947 | -45.03977 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f0f3f3-d383-3367-aeff-28a2c3eb4ae3 | -8.30065 | -44.97483 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac3f19e7-3ed1-35dc-b971-c5e222879b21 | -11.7811 | -47.32266 | 2025-07-25 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b00ad84-f50d-358a-8368-3e07151e9610 | -11.05828 | -44.78352 | 2025-07-25 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf1eb7ba-a6a5-3c4e-9fd8-a8d719a486ad | -7.90645 | -44.08259 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 30f946cf-1992-312e-ba50-53016c4d8f7f | -7.86102 | -48.21576 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c41cc46-7621-30aa-befc-593915817ca1 | -11.78173 | -47.32515 | 2025-07-25 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4323f6b-ad41-33d0-95cf-6e8c5cd82be1 | -7.15316 | -46.09009 | 2025-07-25 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdb355b6-9252-3708-856e-15512fd14181 | -7.53704 | -42.42557 | 2025-07-25 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b131dc63-38bf-3e1a-901d-b2fa5f19ebf2 | -7.85502 | -48.21826 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 520127b6-24aa-3bd0-a8c9-ac7832bd449d | -7.53261 | -42.42949 | 2025-07-25 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 04513e26-a0dd-3ec0-97b4-fd16184ccdde | -8.20141 | -44.9367 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ae03f4d-9ce9-37aa-bc2a-7ca71752cc39 | -9.65673 | -40.59478 | 2025-07-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eda57170-7316-3687-a285-8c6cce87f94d | -12.4317 | -45.37923 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab24cfa2-22f7-3086-815c-7a166e02dd73 | -7.55722 | -44.48827 | 2025-07-25 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dca0815-0405-3594-af55-79d4926b9603 | -7.88391 | -45.54394 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e1de4e89-1829-3650-919a-ee1ab5a0168b | -9.0052 | -45.33717 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65b9deef-8f20-3c0e-8b5f-9f2d11096602 | -7.91047 | -44.08412 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 567d4e69-e632-38d4-aeb6-39c76c8852a7 | -12.25223 | -44.78651 | 2025-07-25 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdd2489f-f310-39a8-9a9b-e8479f7b9d84 | -11.44896 | -45.13191 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f2901bc2-d34d-39ee-9791-44c20077a9d8 | -8.071 | -43.15532 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b65da8b1-160e-35bf-87c0-c77479301781 | -9.5909 | -46.34142 | 2025-07-25 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb8de210-21bc-3f1c-b830-178dfc54818e | -8.89361 | -45.58396 | 2025-07-25 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b81b773-f0f5-3690-8dd1-75eba6a2c70a | -10.74588 | -48.18532 | 2025-07-25 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91b1bab9-c021-33b6-8d69-1992962f2236 | -6.99309 | -47.08435 | 2025-07-25 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28e2bb13-3885-3abf-af4e-dd5fa8cd6edf | -6.8948 | -44.08489 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c13e6c0d-ae6a-3a9b-b8b4-e6ad4163c4b3 | -5.73799 | -43.96098 | 2025-07-25 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02ce9b17-84b7-38a1-ba9c-dc42a5d030ff | -8.51257 | -43.32106 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 739086d2-2b7e-393c-9f97-4a4bfad1a8f8 | -8.8013 | -39.83269 | 2025-07-25 03:55:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 270b9e00-1d0d-3bf0-9989-ba7f03706adc | -6.19783 | -44.38482 | 2025-07-25 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 62704af8-2ac5-31d5-bc4a-1277e26c32fc | -8.33317 | -44.95571 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dd7a6db-7bdf-3982-b4ff-cbf0bd9660e2 | -9.59186 | -46.339 | 2025-07-25 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e58873e3-8ef2-388e-8c06-f2add4da6b06 | -8.07009 | -49.71762 | 2025-07-25 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a54b566-1c18-32e7-ae35-2b67dd30e7ae | -8.29917 | -44.97377 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffa1a329-7251-3cc1-8ddc-f5b794ec1368 | -8.07178 | -43.15055 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 18ccd551-d796-39fc-9753-15c495d614bc | -8.08538 | -43.15593 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 92a2fdb3-9b89-39ef-b9f1-8a01788ee9b0 | -8.50954 | -43.31563 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 18db0ee8-937d-3217-a324-4fcc487a4962 | -6.67591 | -43.96785 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78be595c-e0ac-3687-8024-9f8d0e450445 | -9.02766 | -45.33652 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a3d46f1-7654-3cce-9e65-a73ec63fc693 | -6.8735 | -43.10083 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b545bbc-7ff8-3765-b490-b5753668acd2 | -7.9261 | -44.09052 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 98cc43d0-56a5-3605-b12f-aa6a45d3cc4b | -7.90579 | -44.08699 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e30eaa43-b317-3601-8f56-c9998b678b2c | -6.88376 | -45.25099 | 2025-07-25 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7165a36-1716-3746-8231-42daef9754fc | -7.0919 | -44.87786 | 2025-07-25 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3cb3749e-6cf1-3011-b625-ab8c62ceb755 | -7.89057 | -43.54313 | 2025-07-25 03:55:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9575193-3de4-392e-aa09-d9923079c8a8 | -6.95517 | -44.55582 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 19829fb2-2fef-324a-9709-351796589226 | -9.07821 | -46.63198 | 2025-07-25 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README9.md)
