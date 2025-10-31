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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dab047c0-bcc3-32b3-9df5-a32b9f8f8d3b | -8.09676 | -45.1719 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 521b0bfe-f3cb-319e-a657-83ddb7645ff9 | -7.80761 | -46.39384 | 2025-10-31 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ecce837-5c7d-3286-aa3f-c5141a515fbf | -7.07137 | -44.93186 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 281fbab0-2317-3078-8db1-35f07c475bf5 | -14.08328 | -44.15736 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a01bf55-541c-3c72-9ae2-495ec8154343 | -7.81356 | -46.39488 | 2025-10-31 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b4342f8-f37f-369c-957f-d9c82d60380d | -9.89422 | -47.45422 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bedacaa-5513-37c1-9ff2-886ab8aa1809 | -6.95736 | -42.53114 | 2025-10-31 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6d474312-3c66-3f3c-ab2f-ba97cdc63ae0 | -9.97939 | -45.16285 | 2025-10-31 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45f0dbb2-66b0-3f9a-b1e1-9f970f47033c | -4.47456 | -46.5676 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44c70462-49a8-382d-89a1-25c0bc7d1a15 | -5.33535 | -43.49184 | 2025-10-31 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c31019bd-20e3-322d-8a29-bd07dd8ee3f4 | -5.85166 | -39.51054 | 2025-10-31 03:47:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| deb8d297-3509-3817-a845-2b8df5a1c94f | -5.87912 | -44.7108 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea4b3d59-a52c-36a8-bed0-1b9b1c6612d6 | -9.52539 | -47.27435 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43edd8ea-480d-3f56-aa92-9569fdb8244b | -7.92083 | -46.79584 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5285e377-f7f4-3db7-a4c9-28b85a7391ab | -4.13149 | -43.98681 | 2025-10-31 03:47:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b33d29c2-f691-3b2c-89fe-fa8929733a7e | -13.81918 | -47.06686 | 2025-10-31 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b7498eb-6f99-338c-b89d-cf75238b5bf3 | -8.09583 | -45.14569 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06ceb947-8bb7-355b-a9c4-181289405584 | -6.57886 | -41.59617 | 2025-10-31 03:47:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09950a0d-8a60-35b5-8748-d241be09aed9 | -7.37404 | -46.22277 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b70420a-95e9-31e2-843e-360470296157 | -10.85651 | -44.90485 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3878a652-7485-3a76-9e16-03721c1065f9 | -7.76536 | -46.47498 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 546cd0a3-8ab1-3022-aa35-5aa1a112eea5 | -13.81363 | -47.06559 | 2025-10-31 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9333810b-111b-3fa7-afce-4e8e3967b62c | -8.89813 | -37.96912 | 2025-10-31 03:47:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48a9e6f6-942b-3cd1-829e-451d867a3a45 | -5.31443 | -44.84151 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59888668-7cfe-38f7-80e9-80339f90f57c | -5.70053 | -43.15693 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c7c599d1-528e-30f7-a0ca-be7ec8069d0a | -8.31947 | -45.37481 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a683a6f4-4fe1-34d4-beb4-e0bc39146532 | -8.39371 | -41.84894 | 2025-10-31 03:47:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 992d9d1a-a2cd-382d-9cd4-dc8a792f7950 | -4.55471 | -45.64882 | 2025-10-31 03:47:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 464bae36-b6f8-3afb-9e1d-d81a8fcd5b33 | -13.88364 | -47.3405 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| da1ba7d0-207a-3eef-84cb-764d4f66b985 | -5.54538 | -38.03655 | 2025-10-31 03:47:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 001e5114-03ae-3773-8471-180f6132d439 | -10.95529 | -44.16838 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 559684bd-119c-3341-a9be-050564f8fc8d | -5.85556 | -39.51116 | 2025-10-31 03:47:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59b3728b-5da1-3f33-8799-ce9df624b722 | -4.57584 | -38.2845 | 2025-10-31 03:47:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a57398ce-3083-3b8e-8764-db824d9a3e2e | -7.08103 | -44.94088 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bf666892-0b68-3a4f-b549-67277f3a8409 | -4.13209 | -43.98337 | 2025-10-31 03:47:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8f2e77b-267d-3455-80ea-a6bc7f3019e8 | -8.06855 | -45.14062 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fe84121-f9d0-37ca-9daa-a2b8152f525e | -5.61675 | -45.97705 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a299c26c-4140-3a73-acb9-5f346e009372 | -8.16788 | -45.48949 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14e57e56-67b4-372f-905c-330f71e931ec | -9.72886 | -48.02658 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 061824e3-034a-31de-b15b-53978b0ee77f | -6.3923 | -39.72861 | 2025-10-31 03:47:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f93d36b-c053-3280-8c6e-d9de6668d11c | -6.03173 | -40.26335 | 2025-10-31 03:47:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dcb483a8-055a-3530-95b8-684b2b4b4923 | -5.84538 | -40.81598 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 227b2a5d-a6e7-33dd-973b-8f1471b0740a | -3.48134 | -45.86972 | 2025-10-31 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a42a734-5b5b-37ea-bbbf-4e63823a70db | -14.12827 | -44.18827 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 811d54cb-1ed6-35be-8629-bc694b47e354 | -9.65726 | -44.54938 | 2025-10-31 03:47:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30835053-ad4f-3a6b-b1fe-8837d3a8da0e | -5.03863 | -43.61883 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 25bea544-5306-3a86-bf1b-13c7e0bc9073 | -5.71004 | -48.88685 | 2025-10-31 03:47:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 87816393-03e5-3232-a301-10c533b1bd6c | -9.73517 | -48.0281 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52be1c66-9cb4-3960-b605-a26a4a43fe22 | -5.61406 | -45.98427 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74035a8f-4f9b-375d-b88d-324f583f5147 | -5.92994 | -43.37207 | 2025-10-31 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98e3b333-23bf-348e-af5b-ad797ca1c55b | -13.88288 | -47.34421 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b281b63b-ceb0-36b6-80ef-df0bf65cc510 | -8.06789 | -45.14426 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69d2299d-468d-339b-bcd1-fea63762e6e1 | -4.47397 | -43.43808 | 2025-10-31 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9062669-a9ab-31de-81b6-e922b73a10e3 | -5.41457 | -41.24404 | 2025-10-31 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4ff1e242-742b-37a5-bd07-a30555281cba | -4.87 | -47.52979 | 2025-10-31 03:47:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df14be4a-93b1-3575-b6f5-e6ea1c330ab6 | -4.46138 | -45.75702 | 2025-10-31 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 437509b5-be54-376d-b8fa-ad9b6ec551f6 | -4.67169 | -46.42344 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46dda6bf-f540-375c-a107-daf70cc38855 | -4.86323 | -44.65009 | 2025-10-31 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2ac33ad-2ef4-335d-806a-f11a392818d0 | -9.91574 | -44.92578 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 172a7ea2-a612-3e22-b12c-1e027b97a9fd | -3.54685 | -46.43052 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fdde423-62ba-3811-8cb5-f6b7b5b8572b | -5.74202 | -45.58495 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de58b1de-96fe-368e-824f-f420372f1529 | -9.03007 | -47.45698 | 2025-10-31 03:47:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b91542e5-659c-3940-bdc2-5daa86bef66b | -10.85594 | -44.90797 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 391a302c-56d3-399a-b2ef-dd2ee825817b | -8.18799 | -45.69408 | 2025-10-31 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 677c02e8-a966-3e62-bde9-67eb7cfcbab8 | -10.53151 | -44.92194 | 2025-10-31 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 259d104c-3e2b-37ee-8333-65e66076e4d2 | -4.90109 | -42.97807 | 2025-10-31 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7141f9e6-5c51-3873-8e1e-bb100e905ccb | -9.27065 | -36.85617 | 2025-10-31 03:47:00 | NPP-375D | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1d4dd534-d517-381a-8ba0-522656855582 | -4.83659 | -45.32691 | 2025-10-31 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99f068ef-31fa-399f-9a88-0afaab23833d | -8.17684 | -45.69117 | 2025-10-31 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04383730-6027-3c75-9cf8-739aeac47745 | -7.04479 | -41.47491 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 059842eb-0c4b-3096-992c-2adc828f45f2 | -6.21847 | -43.94336 | 2025-10-31 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c68561d1-0ae5-3892-ba79-4ddc0a01bb02 | -4.12979 | -43.98632 | 2025-10-31 03:47:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139ccdd2-bc4b-38b7-959c-08e3b58ec6cb | -4.67339 | -46.52621 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c664565e-8210-33a9-8d89-60e539350aac | -14.38643 | -43.71919 | 2025-10-31 03:47:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c68fb54c-3675-315a-9fcc-4ccd6c2bb265 | -6.57147 | -41.58617 | 2025-10-31 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ecf0ec96-33c0-369b-b540-a6ae42f5992d | -4.55169 | -45.63081 | 2025-10-31 03:47:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f57569c2-13cb-3a8f-943a-9c4924bea24e | -5.80503 | -44.42865 | 2025-10-31 03:47:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ce4544f-41dd-39bd-8c8f-30e1916cecd8 | -7.36319 | -44.63509 | 2025-10-31 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5db24a1-c6bd-37a3-a3fd-5f10260f548c | -5.47261 | -44.32132 | 2025-10-31 03:47:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f5cc0de-d95c-3916-a9fc-292756e69d5a | -8.06921 | -45.13701 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52d3547f-c2fc-3695-83ac-63dbbf080d57 | -8.10103 | -45.17957 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c599b87-a0b4-3a41-a94c-fa76150f1357 | -7.04908 | -41.4759 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 199806b0-bf39-3753-99b6-a0cfda8c169d | -7.21985 | -39.95449 | 2025-10-31 03:47:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 046f2eaf-85d6-38d6-8935-131e2870b2d7 | -6.99552 | -41.47221 | 2025-10-31 03:47:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8f86e59c-8f17-3003-9866-1d3e6b3b4db8 | -5.88363 | -43.19598 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| af19fc7f-2ffc-36ac-9c54-77d963b60474 | -9.22088 | -45.58156 | 2025-10-31 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09e394c9-c1e4-3c56-ba0d-95af3c897060 | -6.21791 | -43.94654 | 2025-10-31 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 470fae56-fce9-3c06-bf34-6a661f356a9f | -8.16755 | -45.50127 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e568f49-5ccb-3910-bc42-d9e81cf78751 | -3.54597 | -46.43559 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4815e192-de42-30b5-8ec6-ab40ddf17d47 | -4.99452 | -44.73149 | 2025-10-31 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41c64b93-75b7-3288-be8d-7cadc81e9609 | -8.16719 | -45.49321 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cca24200-6733-3cec-8068-58967462ef32 | -5.42327 | -44.64366 | 2025-10-31 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5894411-1297-3421-b289-5716f38b66ff | -4.77174 | -45.98948 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbdb8b55-1760-374f-9d8d-eab4c168c229 | -4.05445 | -47.50107 | 2025-10-31 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 252fb3b5-2514-347f-b518-6f4e53f7f0f7 | -5.69652 | -43.15052 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 83ffad29-c64b-340d-bcdb-191c04677b55 | -7.22651 | -44.32251 | 2025-10-31 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f83f8c3-47cc-34a5-b983-71ed8878c3eb | -9.72785 | -48.03185 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7e2bba1b-52b9-3a7f-8d15-60f42586ae59 | -3.93836 | -46.97377 | 2025-10-31 03:47:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9775882-35fd-3804-92e6-f58146449f7f | -4.05184 | -47.5072 | 2025-10-31 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 43bd06b3-dec8-38e4-b602-65c1e45d8df8 | -4.3079 | -41.44157 | 2025-10-31 03:47:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
