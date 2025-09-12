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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9b15e97-af90-3059-a147-b877ae99f64d | -8.96383 | -46.06126 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b30f343-ac83-397a-9ad7-9a728f5c6955 | -12.09184 | -47.59307 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 17d3f060-da99-312f-a9f2-504c11653f44 | -9.25501 | -57.07365 | 2025-09-12 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76e78db4-7966-3aa5-859b-56b6062171f2 | -9.04341 | -47.11166 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01e9eb07-8f13-3cdf-a372-91a3f607f6ba | -8.19025 | -46.10204 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a49929c-fb4e-334d-974b-8a6f83a4a9c4 | -6.63569 | -49.78219 | 2025-09-12 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b60e390-374b-3057-acd6-d0b4bfed2678 | -11.15315 | -45.2407 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddacb519-0b38-38b8-92ec-97ae0058bb93 | -9.78189 | -47.84868 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60eb0f78-00ab-3b3c-912a-2e4436a0f744 | -11.47618 | -43.67959 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9db35299-e542-37f9-a7af-5cf03e1bbec1 | -9.04784 | -47.04093 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59ab12b4-c8d0-31b3-89ea-ef957dcaee7f | -10.68495 | -48.65649 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ca16fe8-e5f7-32a0-8506-d33e3561a2ae | -5.8284 | -45.27027 | 2025-09-12 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9deda4e8-4f31-3945-a917-54461054550c | -11.31653 | -50.77909 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 814376e5-7b64-3955-aac8-ec954df83aaf | -6.59825 | -41.44654 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52a1fd54-4e87-30d0-883f-464dba8bc88e | -8.36528 | -44.84059 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4401d39c-b107-3d04-bd75-fcdfcfbb2c76 | -5.58072 | -51.32159 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6deefcc2-94c6-3041-a56e-19c942102b9e | -8.87725 | -49.53671 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d2d78ba-2da1-3be2-8e34-7fdf22323681 | -9.71727 | -46.88765 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1b66963-b4d6-3028-b753-c6a12c4d4492 | -11.67714 | -46.6186 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ac6d30a-8e19-3c14-aa05-638f32dc2449 | -10.42537 | -50.61438 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bff3254c-6e17-3114-a9c1-eb64e527699b | -7.73731 | -47.42139 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b99ceb5-7716-33b8-a8d1-db2fe8be05f9 | -10.54823 | -51.53096 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a38ab4ba-f809-31be-84bf-3d7a37f4b91f | -9.05651 | -40.52243 | 2025-09-12 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9a0baf0d-fe2e-36d7-9673-eca294f8ca21 | -9.06201 | -45.71012 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad6ff348-98d9-38f8-b6bd-068b3149ca20 | -9.07534 | -46.95266 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef017ec9-21b6-3089-a986-ad6444a8fb9d | -7.84615 | -45.39098 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab1fe826-948b-3ef3-93e6-f872d46cc713 | -11.68487 | -46.59069 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 153cfdec-145d-31e4-83f2-972ed0c8ad24 | -11.67878 | -46.60796 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2d9912b-a91d-3ccc-a225-1ba1342c1e10 | -5.75728 | -52.37451 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65de33b9-9083-34e1-8dac-fd9a5ce4f642 | -8.42893 | -47.25945 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc5bcc03-184b-3628-851c-0998a8accef3 | -8.26001 | -49.93176 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d51c14e6-464a-3531-8e41-5e50d4d73501 | -8.08054 | -54.74456 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9253eef6-56c4-35a7-abff-80a7b8a239c7 | -9.78198 | -47.38027 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccc9ba35-9d0f-3e53-b7b6-597b0d05963f | -11.73521 | -46.52561 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e64abf7b-73cb-3545-96d6-71da9348ace5 | -11.48666 | -49.26952 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b2258e1-8b9b-3787-997e-ad58d45bc3b0 | -9.71438 | -46.88329 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6aea789-ac4f-363a-8a37-4bbc14eafb86 | -9.89712 | -51.87606 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4a8deef0-d607-358c-8617-6630bc306ca8 | -7.51109 | -55.01829 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2576fa4-b927-37d9-9d3d-30de8efa6c1c | -9.07265 | -47.11992 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 368a1e6e-ff9c-34f9-af96-5502481f275a | -10.55203 | -51.53185 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3537b4c-854e-3cab-a3b1-13128ea654e7 | -7.09347 | -50.7543 | 2025-09-12 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae573030-91ab-3433-9a66-0081166c505a | -11.94438 | -44.30321 | 2025-09-12 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b19d1045-1300-3296-9f19-75b60028174f | -11.23628 | -49.40639 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df67da6e-68b2-32cb-b9fe-7b1c97f225ed | -6.68632 | -44.12148 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed52d711-11cc-3393-bc55-8c72d17bbdb1 | -9.0781 | -46.95666 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d9ca5c1-2718-38c4-ac48-7f191e48b327 | -9.73278 | -48.09535 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe34eec8-ec73-301c-9cfb-3f54a31a46fa | -9.18948 | -45.58636 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab5e942a-a5bd-386e-ae64-9176fcb1a70d | -6.33922 | -43.04662 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 063e8a40-9842-3cc8-95eb-2341b9280195 | -6.55619 | -43.83183 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e766d47-3c11-3210-a5ee-19323a75a1d8 | -6.40262 | -47.33142 | 2025-09-12 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6ac135b-48a3-319a-a9d0-df690f0a8110 | -8.93074 | -51.06918 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cef8a6c-d862-3fb2-9ac5-dc7a912da5d7 | -7.15195 | -39.41977 | 2025-09-12 04:25:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bea691bc-c4d3-3168-a23a-8a9efbda9534 | -7.46979 | -45.29573 | 2025-09-12 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e93e614-166c-32eb-85f7-f6f70f7b90c2 | -7.43988 | -44.98648 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84afde13-61a0-3fcc-a1fd-036ae0e29fdb | -10.70546 | -48.61518 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6baadc9-b0d9-333b-8268-cd10a50b357f | -12.12308 | -44.87231 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb697ff5-c580-375b-8da9-b6fa1af55756 | -11.68097 | -46.57178 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e154b195-f816-3b1d-91d1-5d8c5a070c1f | -8.89674 | -49.92912 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7dec92b3-bef6-355c-b5d0-557e3259fc59 | -6.82445 | -52.79085 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 91a2de4c-1815-3ecf-8ed8-48f7f4d3c923 | -5.64605 | -51.86739 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43bc913f-e816-3b94-8d24-dd1e3917b8db | -6.53951 | -43.70545 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f807dad5-431c-345f-8f0c-19e81b9e6e7f | -8.73314 | -47.11842 | 2025-09-12 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d472c298-e4fe-3687-97e4-e07a633ffa7d | -10.08557 | -47.15733 | 2025-09-12 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d66e9e07-f5b8-34c0-a67d-9db51fc19357 | -10.42463 | -50.59673 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6214a6fc-6ad9-3c3e-827f-1ded3092f1ab | -7.52405 | -44.68789 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc3c994a-660d-3e46-8b73-fe16a3d0a9dd | -9.0119 | -45.79687 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82a0fd37-ea41-3b38-9ef7-0d8b394bc63e | -6.82505 | -45.64806 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e7b7e66-3307-30c4-8c0e-98d6d55d993a | -9.87741 | -46.4723 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81e223e4-2c47-34b5-9f93-194043ca595c | -12.50403 | -44.68887 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 479b2e39-8059-321b-83e9-31320f904d7c | -8.35257 | -47.58895 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13eaf5a4-34c1-3fde-9b65-924add47e69a | -8.05537 | -52.32108 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d518aafd-04ef-3c86-97e2-14540b87c87e | -7.4161 | -50.65568 | 2025-09-12 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec057693-9f94-301a-a38d-ad79f41846dc | -8.5222 | -47.65269 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93d566a2-1af3-3013-8dba-9ab062275b47 | -8.08162 | -42.56648 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7bfe1058-6e85-324b-b580-bedef4bc7314 | -11.12164 | -45.12187 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f20290d-e358-319e-928b-5a176e20d1a9 | -6.41769 | -44.50661 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66378219-2bcd-36b3-9b44-9d44147918c9 | -8.8882 | -49.9362 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ff63427-0277-3d3e-b1f0-11b1060ef0ec | -11.14909 | -45.31365 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ead5910b-a01e-301c-baea-76894d8c9590 | -6.24664 | -44.8005 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84ccc57e-c593-3efd-bdf4-3627242dd297 | -11.68432 | -46.59427 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdfe1e37-8811-3ae6-bf4e-182edf6e3fc1 | -11.53723 | -50.41109 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3186d26e-8d6f-3db7-bf5a-b1dbd5b29180 | -8.0813 | -50.17297 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8372677a-6e37-3457-bc69-5eac49be28f8 | -7.26809 | -44.59969 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de354e74-da40-3087-8e47-d4303699b65e | -9.73924 | -48.3467 | 2025-09-12 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac3fc630-64d8-3562-834a-5021e5bf0546 | -11.68207 | -46.56464 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 788dc728-9f4f-3d41-867c-d198bbd555de | -7.50243 | -44.73761 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b30d3b7e-110f-38b4-80b4-f28ce73f92fa | -7.85285 | -45.39207 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53f52483-d861-3c17-944f-fb831b4ddb32 | -10.69285 | -48.65044 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 610704ba-0384-31ce-b3b3-cd1385ed75ca | -7.73109 | -44.86591 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 616e6409-f2a6-36b5-82bd-1e425b9d7347 | -6.68744 | -44.13743 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b2a6708-8262-318d-ba44-dd48ce8df6fa | -9.99953 | -51.72751 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 432a975a-f9c8-3f07-aa06-48f4b502bcf4 | -11.9989 | -47.77266 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cce46f7e-520b-3efc-a925-8e521e5e04c8 | -11.6971 | -46.59997 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50ea2bdd-5af6-3cdc-86b6-e0ce75edc8cd | -7.91257 | -44.87096 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e039332-7758-3ccd-b415-062a1f971892 | -8.08648 | -50.18745 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ddd23738-c046-352e-bccc-32b50503e6a1 | -11.08723 | -48.44173 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7429fa14-1cbe-3d6f-94c8-c74ab65a2a83 | -12.13135 | -44.84061 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13c47591-a646-3a08-b784-e08eaed151ff | -11.5347 | -50.41161 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 145c4dcc-1aa6-3048-bf4f-0e9e6d72200d | -9.03716 | -45.8047 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09133290-b3e6-3a77-9ca9-0b276c382b92 | -9.9383 | -42.33384 | 2025-09-12 04:25:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README66.md)
