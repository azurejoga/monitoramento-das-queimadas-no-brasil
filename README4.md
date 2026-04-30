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
| a538cba0-875c-36fc-8198-1d371595e6bb | -18.08394 | -52.99866 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ea434f2-b7ef-390c-8806-1398fbfe25c4 | -18.04545 | -53.00843 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e70c291-0577-3135-9db7-bbf06f5ee985 | -18.00709 | -48.17541 | 2026-04-30 05:08:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b9a3ea0-d3b8-3661-9127-1856452eab2b | -16.26028 | -60.02943 | 2026-04-30 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbc55194-0e05-3380-a4f0-eb553db68dca | -18.08801 | -52.99924 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05a88d2b-6005-36f5-9e14-8db689b7a3a4 | -18.04592 | -53.00465 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67c3c35d-c31f-3436-b936-5a579b2c2074 | -13.69537 | -55.69323 | 2026-04-30 05:08:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb385fca-3b71-3fbd-96a8-36778452dcd0 | -17.25796 | -47.08198 | 2026-04-30 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 67b04a16-c4fe-363d-82e8-543c136e71a1 | -18.03646 | -53.01231 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3053982-2ce8-3706-9a44-af67934d8ac6 | -12.72186 | -56.56358 | 2026-04-30 05:08:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4428b03-e869-3800-a87a-8726e363499d | -17.99582 | -53.00655 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8d55ab4-8d9e-3ed5-82b4-d10cfa1f5bcf | -16.36027 | -52.42004 | 2026-04-30 05:08:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee063489-916b-3821-95fb-0d376230b11a | -17.98411 | -53.00109 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 835c42fb-1ec0-31b2-88b6-88f1650f8407 | -13.72734 | -57.49007 | 2026-04-30 05:08:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf49326f-30a9-3f39-a46c-7a9a598353a7 | -13.98865 | -56.65583 | 2026-04-30 05:08:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4607ddfe-f2b0-3df9-85db-50cba50c4373 | -18.03999 | -53.01912 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2576ff5-7685-3ca4-b569-fd2b6c48b96a | -18.04606 | -53.00224 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89d6ee85-9159-3f53-a4da-6370582d371d | -18.04045 | -53.01535 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 586da153-33ba-333a-9763-71f245fb3a56 | -18.73193 | -55.25882 | 2026-04-30 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8d8f5489-1df8-3f5a-9370-dd925f78fd75 | -18.04101 | -53.00916 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0c16083-4a1e-398b-82f0-a0cf5e594d5a | -18.04052 | -53.01292 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e4bab45-22a7-35aa-a1d7-aeef40c0b918 | -18.04139 | -53.00782 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2840f6bf-395f-34fa-afe2-e096a8ffb1aa | -18.04408 | -53.01727 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04773168-8d3e-311a-b0fc-0f879b030ded | -18.00037 | -53.00338 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b9719ae-2f8a-32ee-a3c4-19fbf41c0ad7 | -13.72403 | -57.48952 | 2026-04-30 05:08:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2fadc03-20b5-3043-8ec3-e8edbfcf70bd | -18.03191 | -53.01547 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceb283e7-7953-3946-8630-f6f43bbe1e0d | -18.02687 | -53.02238 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd41c908-3300-317a-9984-a4b12594b700 | -13.9881 | -56.65941 | 2026-04-30 05:08:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd679cca-9bc9-3ded-8a78-7ab88925a71c | -18.04092 | -53.01159 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93553801-318c-379e-a1f5-4b8228880ae5 | -13.98478 | -56.65887 | 2026-04-30 05:08:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87251a5e-faf0-345f-bff0-9083f9502297 | -17.98818 | -53.00166 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 564ce31e-6e90-3470-9a62-7a6644118aae | -18.04458 | -53.01352 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2756b6db-71f0-362b-b427-5236a97b8637 | -13.69931 | -55.69005 | 2026-04-30 05:08:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d119105-7974-3e3d-8a97-0d73a79041a2 | -18.05045 | -53.00148 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb504c09-8fe4-30e1-95a0-d41e5315a237 | -16.92322 | -48.2251 | 2026-04-30 05:08:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a3f8959-8885-3089-a914-a5d5fc6bd297 | -16.32393 | -50.04641 | 2026-04-30 05:08:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6419d59-4d87-3cfd-8616-bc084e56b4f2 | -18.03142 | -53.01923 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21183f75-4aaf-398c-8f57-56a565756210 | -18.04185 | -53.00404 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02df8326-5ca9-3ba5-bcac-0154a3e9da80 | -18.04003 | -53.01668 | 2026-04-30 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b98b331b-49f2-3f5d-ac75-e283e4d1e0f2 | -13.50555 | -56.85948 | 2026-04-30 05:08:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 541897d4-b2e4-363b-b053-b4238a4e0979 | -14.21288 | -57.42806 | 2026-04-30 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d30475b-9ac6-358d-bd45-3073af4676a2 | -18.0456 | -53.0013 | 2026-04-30 05:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| aa94dda1-389e-3586-bb30-cf57eeea9094 | -11.0006 | -45.0847 | 2026-04-30 05:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 6aaa7fb2-a290-36c1-b8a8-648fe110085c | -18.0257 | -53.0045 | 2026-04-30 05:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 91d441be-3edb-3257-b0b1-b77d7bbe0f53 | -11.0006 | -45.0847 | 2026-04-30 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 164d3055-12bb-365a-9fac-dc58bf3f8c1d | -18.0456 | -53.0013 | 2026-04-30 05:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 14f45661-de18-376c-ad29-47d989ed00e2 | -18.0654 | -52.9982 | 2026-04-30 05:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 9d564e6e-b0c5-3c02-ace0-fccabbeb6383 | -10.99018 | -45.07164 | 2026-04-30 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 2dcc02dd-1195-3cb9-9afc-40ae2077e8f8 | -10.99058 | -45.07887 | 2026-04-30 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 71f037b8-f5d2-3dbf-ab95-6f5237b7beb6 | -10.98699 | -45.09049 | 2026-04-30 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 79eb4a78-8548-3fae-bc3b-c1961223c358 | -17.25303 | -47.07433 | 2026-04-30 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 46.8 |
| a465145c-edcc-3bbe-ad9a-7b6ad6e291e6 | -12.05103 | -57.41953 | 2026-04-30 05:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9102b2-56fd-33be-bf38-bb68e7a2caf2 | -10.83976 | -68.37564 | 2026-04-30 05:57:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6431f85a-e38f-345a-be8b-22a271aa2631 | -12.05752 | -57.42032 | 2026-04-30 05:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6007d363-7bd1-3896-aacc-1e9e5cd29f9a | -18.0058 | -53.0076 | 2026-04-30 07:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 606648bb-5308-3224-8354-910422df54c0 | -18.0257 | -53.0045 | 2026-04-30 07:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 111a6b5e-648e-30b1-87a5-e35e21e09060 | -18.0257 | -53.0045 | 2026-04-30 07:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e5b1e4f3-6cc0-38da-aede-1cdb2e166491 | -18.0058 | -53.0076 | 2026-04-30 07:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e1da8862-a2a5-3e42-97af-3df391878829 | -9.22611 | -46.66031 | 2026-04-30 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4f961de4-38b7-3226-b976-23493e0e6a86 | -11.27391 | -44.65284 | 2026-04-30 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0ca7a912-b25f-3734-a998-2dadd171cfd9 | -11.28548 | -44.6609 | 2026-04-30 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| abb17d93-e0b2-3580-b749-140a97f40a81 | -10.99777 | -45.08075 | 2026-04-30 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 09832cdd-862b-3d40-9e0c-d48107f94379 | -9.47737 | -46.11189 | 2026-04-30 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| e4c6914a-c064-37c6-83e2-0f7a3ec377da | -9.21338 | -46.65863 | 2026-04-30 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c8c823bc-4a5e-3b01-8cb4-1ce6b1995a64 | -9.47465 | -46.13376 | 2026-04-30 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| b880b0f3-2cdc-31bb-ae73-4c2cc1b8599b | -10.99758 | -45.08616 | 2026-04-30 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5d8dbcce-ac2a-3a24-97a1-51f2f05715f1 | -11.27739 | -44.62221 | 2026-04-30 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3c9fbea0-a15f-3959-875a-92abddb1e56f | -9.22861 | -46.6405 | 2026-04-30 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e1d4cc27-b7e4-356e-8a6b-64cb1cbd893a | -11.28878 | -44.63005 | 2026-04-30 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 6f17cb59-c6da-3927-a92c-2859ac258d8c | -18.00957 | -53.00608 | 2026-04-30 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 90dea403-40a5-3763-9b7c-4f3723c9b036 | -11.60963 | -47.11498 | 2026-04-30 12:21:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 51e8fffb-18b2-3aba-a451-8307aa03b1b7 | -17.25616 | -47.06807 | 2026-04-30 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 1dcd3c3e-9bdf-3050-b26e-dba429912ca3 | -14.71547 | -47.51146 | 2026-04-30 12:21:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 485bc359-bf49-3e44-bc2e-2d7e79dc8ade | -17.2536 | -47.09273 | 2026-04-30 12:21:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 492888b6-9489-3524-b2e0-45580777b47f | -13.30866 | -43.58899 | 2026-04-30 12:21:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| a3bb6e90-5087-3993-b14f-c016ab82edf4 | -14.71395 | -47.51672 | 2026-04-30 12:21:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d7262895-3109-3ea3-bcee-ceb503d2d538 | -11.41508 | -48.42223 | 2026-04-30 12:21:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| a66ff6d7-b2bd-3672-89df-e01ad4912d33 | -12.37836 | -50.02242 | 2026-04-30 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 106b6fa1-6843-3393-9b8f-7ae1f07ccc45 | -11.61204 | -47.09482 | 2026-04-30 12:21:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 27c28030-732a-3830-ad13-bab0725494ee | -12.37674 | -50.03479 | 2026-04-30 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 990dc039-96c6-3a7d-8ec8-960e1208f4d1 | -18.01882 | -53.00738 | 2026-04-30 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9548a913-707c-37df-a57f-f0ff426082d4 | -16.41698 | -54.92231 | 2026-04-30 12:21:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 62546330-0555-3c1c-942a-77ec5e80cb41 | -12.29554 | -57.39197 | 2026-04-30 12:21:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f1621bc6-01be-3f3f-b45a-ecea21b3c7e8 | -13.37718 | -54.26441 | 2026-04-30 12:21:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f04768e0-908b-37bb-92d0-f31a457c656c | -11.40592 | -48.41453 | 2026-04-30 12:21:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| bb886d08-2047-3e2c-9e12-17a4a4f73b50 | -9.4655 | -46.1415 | 2026-04-30 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f576a521-b5c2-3e68-a5ce-abdb4c711a4d | -17.2478 | -47.0825 | 2026-04-30 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2f8d61b2-42ab-3b0a-bfce-e63f582d577b | -12.37 | -50.0242 | 2026-04-30 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 000fd26d-c4ca-3e05-af83-0c00ea8e8d4f | -9.4655 | -46.1415 | 2026-04-30 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3f961b6f-bd7c-32d8-ae6a-a33bad1989e4 | -17.2478 | -47.0825 | 2026-04-30 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0ffbb321-9fb6-3abf-a2f0-9919c75fec86 | -12.37 | -50.0242 | 2026-04-30 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6603b30e-265c-3af4-b38c-cd8a195148e2 | -9.4655 | -46.1415 | 2026-04-30 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e13ac35b-2c32-310e-8a45-e1ee5b991948 | -17.2478 | -47.0825 | 2026-04-30 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0a68b3fa-e647-3721-90dc-1032e87aca5b | -9.4655 | -46.1415 | 2026-04-30 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 635f9e5f-1c28-3bde-a0c4-61e23de03f6e | -17.2677 | -47.0785 | 2026-04-30 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1dbf680a-f8dd-3a56-9096-6c796961dfdb | -12.37 | -50.0242 | 2026-04-30 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| dd441db0-89e0-3a73-82b3-dc811130ffde | -12.37 | -50.0242 | 2026-04-30 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c9a7d2a9-48e5-3029-b424-4421f85f479a | -9.4655 | -46.1415 | 2026-04-30 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 611d07e2-6b7e-36e0-a906-370bc3cc3c08 | -17.2478 | -47.0825 | 2026-04-30 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5337489b-a5e1-3446-89f7-dfad411989f2 | -17.2478 | -47.0825 | 2026-04-30 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 110.2 |


[Clique aqui para ver as próximas entradas](README5.md)
