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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5addea18-2957-3ab9-8d2f-10dd81a31c9b | -12.26997 | -44.82178 | 2024-10-27 12:34:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a90d0800-e5ce-34d4-875b-c158c0c0d6e4 | -12.14519 | -39.95197 | 2024-10-27 12:34:00 | TERRA_M-T | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| bbffb3fd-c087-3475-9dcd-3d1676fb5637 | -11.99368 | -43.08295 | 2024-10-27 12:34:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 184.5 |
| 0a392f20-916a-39f6-b795-75b21b838b1f | -11.99224 | -43.09368 | 2024-10-27 12:34:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| fe073c48-7502-30e5-b322-3f1c99d7cb10 | -11.95296 | -45.49196 | 2024-10-27 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 14116e7c-9e31-3c36-b440-68e600149f27 | -11.95166 | -45.50097 | 2024-10-27 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 85cde4c7-847e-3a0a-a7ed-d2f60dcd697b | -11.76738 | -43.18135 | 2024-10-27 12:34:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 1e2914ea-793b-3ab9-9083-3fcb735cf7c6 | -11.63196 | -44.9683 | 2024-10-27 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| edbb0d85-cc5d-3417-b57b-54bd4edaff78 | -11.62434 | -44.95788 | 2024-10-27 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 03ca02c6-5e6a-3f4c-8cce-bebe08bc990e | -11.62305 | -44.967 | 2024-10-27 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 3f6f32b7-ebd3-36de-aed4-778d8e7c7ed1 | -11.31254 | -44.16277 | 2024-10-27 12:34:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 767e5524-dd80-391b-a653-cdf03d4d0d48 | -11.31121 | -44.17227 | 2024-10-27 12:34:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8477bdd3-a8a0-34f8-a13c-66150ffcdd03 | -11.25746 | -45.01031 | 2024-10-27 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4c23ac61-e981-3b5e-81f5-2f4037e72752 | -10.92162 | -44.78017 | 2024-10-27 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d237a040-c190-3381-9ecd-d15790ca88ca | -10.92033 | -44.78931 | 2024-10-27 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| e9ffb9dc-d886-3167-8902-e3622f00acdc | -10.78566 | -44.30762 | 2024-10-27 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 579c9080-e37f-3041-a49d-92fd4ff26c67 | -10.78436 | -44.31695 | 2024-10-27 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 71d52b8d-3fa9-359d-ba62-51f1668e2b4c | -10.72086 | -44.2446 | 2024-10-27 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 62caf056-20de-328a-bd5e-87142320be02 | -10.71181 | -44.24335 | 2024-10-27 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e1b080eb-3181-365c-b71d-1dbfbc30ead4 | -10.66644 | -44.50163 | 2024-10-27 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d9ddc511-e330-3088-abc0-4dcb61c8bf92 | -10.59638 | -44.27845 | 2024-10-27 12:34:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 583209b0-77e8-3b57-a372-be311d7abbaf | -10.58243 | -44.0501 | 2024-10-27 12:34:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6d67f329-30d3-3d1d-97b2-62c55b9370fc | -10.5811 | -44.05956 | 2024-10-27 12:34:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cae8dabe-9a5e-32b7-9fb0-c802ed995327 | -10.56884 | -44.27761 | 2024-10-27 12:34:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 08f7e50d-dc4b-37f8-a7e9-2d7dce0733de | -10.53755 | -45.14244 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 55933256-5e45-3d44-9492-387f58c29b7f | -10.50344 | -44.86479 | 2024-10-27 12:34:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1cf21066-9135-39aa-86c8-7ea6d8685d7f | -10.4449 | -44.89331 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d7cc0367-c190-3427-85ad-99808e53a078 | -10.44104 | -44.92034 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 768f4525-9b82-389d-9ddc-ab835b79057f | -10.43975 | -44.92935 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 575b6d30-75bc-366c-af12-6a25d46c7b76 | -10.36124 | -45.08645 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2be71f89-b567-3548-8260-4d59a765fc93 | -10.35995 | -45.09541 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2ee91639-e177-338b-848f-98dc56d1b91c | -10.35237 | -45.08519 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dfc05b7b-3e18-359d-8f87-873b491dc4a7 | -10.35108 | -45.09415 | 2024-10-27 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6887e1c0-dde2-367c-aec6-bfbfb9d4edcc | -9.74382 | -46.28814 | 2024-10-27 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 45e4322b-4628-3b1e-a212-5acddc5423a0 | -8.51488 | -45.86336 | 2024-10-27 12:34:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 66edbd7c-da00-3a36-bf0d-66ec77923a49 | -7.10548 | -45.28502 | 2024-10-27 12:34:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5c79a0b5-bb1b-3a58-9fff-a1d81ddd5a18 | -7.10418 | -45.29396 | 2024-10-27 12:34:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| b2e9ec41-8a8f-389d-864f-c55e8b2e5708 | -6.95517 | -45.49564 | 2024-10-27 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 954033d7-8c54-3da5-b7b7-5a2270161df2 | -6.95385 | -45.50464 | 2024-10-27 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0299b669-9a90-3675-b9b9-f77f515495f9 | -6.61921 | -44.76111 | 2024-10-27 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4b7c4b9a-8cd6-3cee-a8bf-8044c80fdd84 | -6.61164 | -44.75099 | 2024-10-27 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e5498b1c-145c-3828-ac34-40fe93b4dafe | -6.61035 | -44.75985 | 2024-10-27 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| c4fc11bd-f4b4-3df3-b7e7-838bbc66615b | -6.17913 | -45.4387 | 2024-10-27 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 6903c7fa-c044-3ef9-bc68-110dd42f7727 | -5.92109 | -44.61249 | 2024-10-27 12:34:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a27e6ed9-daa5-313b-aeea-8c55c55ebc97 | -5.86165 | -45.90641 | 2024-10-27 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5d7903bb-2744-3eba-90e2-78f2b39c07f0 | -5.86027 | -45.91574 | 2024-10-27 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6b1e5595-f4dc-3ca5-9775-b9a6576b3681 | -5.83999 | -46.24249 | 2024-10-27 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| af00c612-64ec-3711-9e76-0060627766df | -5.76032 | -45.28046 | 2024-10-27 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2735fe03-e0b1-31d0-a7cd-5dae20072a1b | -5.62165 | -44.83186 | 2024-10-27 12:34:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9b18439b-c113-3428-a6bf-dc99dad507ae | -18.54616 | -49.80139 | 2024-10-27 12:36:00 | TERRA_M-T | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| f869e964-7a81-3855-926b-08e89a1d4a1a | -17.71577 | -39.7274 | 2024-10-27 12:36:00 | TERRA_M-T | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| 1e0c2361-2f3f-3f8e-bbeb-28e41d1acab3 | -17.2346 | -46.76303 | 2024-10-27 12:36:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b421e37-f819-393b-be76-caaf4bc4f782 | -17.08553 | -44.8608 | 2024-10-27 12:36:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a583e3d7-8ba0-3bbc-acd7-b3c2e2cf5e95 | -12.869 | -44.6175 | 2024-10-27 12:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6363fa8b-4bdf-3d00-9576-ca19b55e7294 | -12.8883 | -44.6143 | 2024-10-27 12:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 5abaccf5-2f8d-3f67-934b-496d082daaa6 | -13.7523 | -43.0884 | 2024-10-27 12:36:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 714c81d2-7f3c-3f6a-bb62-f28cf22ea1ba | -13.7529 | -43.0642 | 2024-10-27 12:36:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 171.3 |
| fe067818-f75b-3d26-9d0a-ca398cd56eb1 | -12.8883 | -44.6143 | 2024-10-27 12:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 92fbd542-01fe-3b4f-81b0-6cfa74195c10 | -13.7529 | -43.0642 | 2024-10-27 12:46:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 140.9 |
| 9db3787a-57db-3568-866f-1bc9f7a70f34 | -13.7523 | -43.0884 | 2024-10-27 12:46:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 277529ac-cc5e-32fc-9ab4-2569c9eb5f12 | -12.8888 | -44.5909 | 2024-10-27 12:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| d05febd4-7728-3acf-86a8-6449120a7d52 | -13.7523 | -43.0884 | 2024-10-27 12:56:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 104.1 |
| a7bcd934-169a-388b-9aa0-a2bb895bd0d2 | -3.6649 | -42.4148 | 2024-10-27 13:05:26 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| d1752c48-0d29-3651-bb4d-f10bbc352c34 | -12.8883 | -44.6143 | 2024-10-27 13:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 01410618-dd7c-3b5c-b725-b36c7ced5b77 | -12.8888 | -44.5909 | 2024-10-27 13:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 6258db8c-eebd-3cb1-a155-4311a7044cbd | -12.8695 | -44.5941 | 2024-10-27 13:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 0ab53444-6f65-3097-ab42-cdeff08ba5d8 | -2.5312 | -51.1609 | 2024-10-27 13:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 2da04e31-badc-36ce-86e4-feaf77ff2440 | -12.8883 | -44.6143 | 2024-10-27 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 8673ebbc-650a-37d1-b972-b544f2c6a79b | -13.0747 | -42.1261 | 2024-10-27 13:16:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 0b0e0644-018a-3a76-a34d-2157b1cd5bea | -12.8695 | -44.5941 | 2024-10-27 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1258e22a-8927-3368-9757-aaaaf8ca9ec5 | -13.9074 | -43.1072 | 2024-10-27 13:16:23 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 120.6 |
| 8dc4775a-2e4a-388b-b58d-7452caed77b3 | -2.5312 | -51.1609 | 2024-10-27 13:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| c008995d-0208-3a44-842d-d88a32895cfa | -2.9215 | -50.274 | 2024-10-27 13:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 472d092e-f02d-380a-9a15-3c6139081c7a | -3.5564 | -45.098 | 2024-10-27 13:25:25 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| cf914659-737a-38c0-8804-66263ec7b9b1 | -12.976 | -42.2173 | 2024-10-27 13:26:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 109.3 |
| e1ffbee9-0727-3977-8508-4495844debe8 | -12.9565 | -42.2208 | 2024-10-27 13:26:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 2a842edd-16c5-3a3b-a90c-206addb27706 | -12.869 | -44.6175 | 2024-10-27 13:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 702bdd7a-6560-3b64-bc0e-340ad6f5b860 | -13.0747 | -42.1261 | 2024-10-27 13:26:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 16b20ddb-da79-33de-bd98-3e9992befb30 | -2.9215 | -50.274 | 2024-10-27 13:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 275d66da-17cf-3188-9b87-ac47c96d931e | -3.4431 | -45.4184 | 2024-10-27 13:35:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| a2807dd8-c1e1-37e5-9e0a-2b4459ae4dd3 | -3.4617 | -45.4176 | 2024-10-27 13:35:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| b60a3057-b218-334a-a886-3749b04d36c5 | -3.466 | -41.2561 | 2024-10-27 13:35:24 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 118.8 |
| a692d62e-aa04-301d-a2e6-0c4de00ed3f1 | -6.4067 | -38.4547 | 2024-10-27 13:35:41 | GOES-16 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 136.2 |
| eb7afbfc-1342-3df2-9c78-b3c995e29ec1 | -6.9593 | -41.3296 | 2024-10-27 13:35:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 27752708-eafc-3627-b2ea-7a3678a7fee2 | -6.9405 | -41.3315 | 2024-10-27 13:35:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 140.3 |
| 5584e0e0-e57a-3fcc-a003-e7994ba6fb6a | -12.8883 | -44.6143 | 2024-10-27 13:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.3 |
| a36e31c9-b9ef-3f53-aa7f-16456d5f6d60 | -12.8695 | -44.5941 | 2024-10-27 13:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| db1c49db-8a9c-31f2-8cce-ecf0e340d5e1 | -12.869 | -44.6175 | 2024-10-27 13:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e8905ff3-e881-37f8-a154-7712c2c95485 | -12.8888 | -44.5909 | 2024-10-27 13:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 7ee69cf1-6f3e-3066-883d-3867411a278a | -12.9565 | -42.2208 | 2024-10-27 13:36:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 137.4 |
| ae28cbdd-5169-3856-9cb8-e45361b4cb34 | -13.9074 | -43.1072 | 2024-10-27 13:36:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 221.4 |
| 03839cee-5157-3867-93d7-b64aa8a342e3 | -2.9215 | -50.274 | 2024-10-27 13:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| f0839a18-198c-33d8-8b3d-639da4f66860 | -5.2905 | -42.7388 | 2024-10-27 13:45:35 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 1375e6c9-ffbc-39cb-b08f-f8213dc4f6cb | -6.4067 | -38.4547 | 2024-10-27 13:45:41 | GOES-16 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 108.6 |
| fd4f1d7d-9c18-3a91-9e85-c2e9ce1b9bf0 | -6.9593 | -41.3296 | 2024-10-27 13:45:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 580c363f-fb16-3285-9840-179daa4032d6 | -12.9082 | -44.5877 | 2024-10-27 13:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 505f84fc-ccd2-311f-84a4-b969f505d563 | -12.9565 | -42.2208 | 2024-10-27 13:46:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 151.4 |
| edf972e4-e085-36d8-bedd-2678878b8d89 | -12.869 | -44.6175 | 2024-10-27 13:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 1a475208-5199-3f18-920c-d6cf005dc076 | -12.8883 | -44.6143 | 2024-10-27 13:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 266.7 |
| 567bcdea-3d06-3548-9884-7c5b55da7edf | -12.8695 | -44.5941 | 2024-10-27 13:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |


[Clique aqui para ver as próximas entradas](README67.md)
