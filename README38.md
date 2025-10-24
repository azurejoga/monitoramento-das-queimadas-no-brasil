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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60923cd4-c86e-324a-9025-a5824bc2be6c | -3.80128 | -51.75442 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41f20f9f-f0a8-3980-9845-dca4c9a40916 | -4.85304 | -46.72757 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87cacab8-1754-311b-b283-1e2924c5543a | -3.46644 | -53.45798 | 2025-10-24 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8517da2a-82ef-383a-9299-9f88a1938d56 | -8.23866 | -47.17799 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2117779-59db-3b91-97ca-4b0235178c78 | -10.88916 | -46.04914 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44f2a6c1-9a59-3d29-addc-cf4b959daca3 | -6.88185 | -43.61365 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edda6fc0-1004-3f06-9b68-bb31d19f75e6 | -5.65944 | -45.95185 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fe57a9d-de60-3c14-be9b-7a124a14a2bb | -5.48088 | -48.88903 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bbdd4d1-6f06-33eb-a74f-6bc5ebcf5987 | -7.68322 | -48.00177 | 2025-10-24 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6730d557-656d-3681-abd4-df4f38e983c3 | -4.82131 | -48.67546 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac8dd5ff-8775-3b0a-9465-af8570552e88 | -3.11312 | -51.2069 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cf02baa-7018-3502-a7ba-e83045903fc5 | -3.78184 | -43.90397 | 2025-10-24 04:38:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4a2d0ad-e118-3779-85ae-ebc688eb0d47 | -2.73106 | -49.56236 | 2025-10-24 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04a83a3d-c5dd-3489-bd19-96fa7d97858e | -8.19319 | -44.43724 | 2025-10-24 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33e7c393-b187-38ae-94fd-af3cbe3f4f96 | -8.17434 | -47.76661 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a8bc195-7368-35da-bcfa-b098452a6f64 | -8.44757 | -48.7471 | 2025-10-24 04:38:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8000c67a-05e0-394d-be78-518d681b3d76 | -3.84841 | -48.16557 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6964bb29-a545-3e2b-9486-8f917831c57d | -6.2858 | -47.01638 | 2025-10-24 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68339be6-52bb-3d6a-b837-63d64f7ff7ea | -6.89456 | -43.61552 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17554377-ad9a-30cf-a591-25332639a047 | -6.47288 | -44.12762 | 2025-10-24 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fe220de-6ed7-3318-aee0-40d9ba86ed46 | -8.11738 | -47.04454 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc85eb5c-955b-3c9f-bb9f-01eed1de0145 | -3.79685 | -52.42086 | 2025-10-24 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13b742f1-033f-3cf2-b9fd-5c78fb92a833 | -3.02704 | -49.49328 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c7100e-27e1-3fa4-83d8-e035e3ebb78c | -4.53935 | -46.55679 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ac5f758-49d1-3f5c-a93c-2a9c2bf31de5 | -4.66214 | -55.97192 | 2025-10-24 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db847904-d58b-3546-a4da-7e14a5ce8474 | -2.80308 | -51.35577 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de7eb034-0b6f-334d-90c8-4e13949dc3a3 | -4.19806 | -48.36187 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3617da01-6565-3979-9fa6-a71e72775e7c | -10.96239 | -45.07854 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1e81670-2f87-3246-9a8d-422e140f7fd4 | -8.17776 | -47.76714 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8109daa8-07a1-3674-a869-132e59e5ec73 | -6.08881 | -46.23424 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e69eed8f-7b4c-37b4-8dab-04a7fa7cfc5f | -8.31934 | -46.25783 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af24fb74-ca7a-31bb-b61c-585762c8b1cb | -3.82991 | -52.36967 | 2025-10-24 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de063401-8b04-30c2-a305-a1accf58be70 | -6.28002 | -47.01582 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f65f64f4-95dc-31d5-b778-5e4c3b73931a | -4.20521 | -48.35946 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3e3b305-5fb3-34ac-8904-1e52b6ba57bb | -8.46441 | -45.56599 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb9710d-835a-39b2-92fa-c21a5d7b33a9 | -5.10512 | -47.79516 | 2025-10-24 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8779484-7124-37e5-95ea-b46e76d25ac0 | -4.81079 | -50.93393 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 246f5217-e0aa-3432-b7a9-d4fb63374da6 | -5.43253 | -40.88159 | 2025-10-24 04:38:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b47fd53b-62d0-3788-b97f-b0444f440fff | -9.60009 | -46.91634 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca6e5785-4c51-3040-bd77-c8b6a5fd49fa | -6.27984 | -46.1018 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 521b9cb1-6398-3888-a7e7-c6b1cf4c2e94 | -7.13729 | -45.04982 | 2025-10-24 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 460d6221-22e2-3b13-93f2-88f22be71aa9 | -9.59772 | -46.90751 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 37e8d894-cffb-307b-ae04-e9175b3c31ca | -2.79953 | -51.35521 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd5fe5df-2d66-3b39-b4fb-e2d4a4dd6bc7 | -2.79888 | -51.35924 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72c1f393-caa7-3075-a530-755871d9edd7 | -2.73162 | -49.55884 | 2025-10-24 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4b08170-0024-37d0-8782-5436c57b2c23 | -3.81461 | -44.08466 | 2025-10-24 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d54c6743-bfb7-3c61-abd7-99e32b2525d9 | -5.48083 | -48.86782 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7541815c-2b47-378e-b422-3f7f41752865 | -10.42887 | -49.36839 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f95a2af-18ed-3319-a2b0-6e9177124043 | -2.79988 | -54.38542 | 2025-10-24 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e2b379-bab6-319d-a9c0-e5277fb696e9 | -9.25963 | -45.35007 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4545a84-9905-3f1d-b2eb-3059b9578a95 | -9.23327 | -45.61755 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e471486e-f373-3e64-a05d-1732286e8dc5 | -8.24275 | -47.17463 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d8f85c3-3480-3521-9cde-7de7f6eb0428 | -9.78098 | -43.85657 | 2025-10-24 04:38:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 317cfeb7-e736-3769-b7fb-808b10ab974a | -7.83235 | -45.37819 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c70fcb79-212d-3ce3-97f1-8517e11a40f3 | -9.09629 | -46.53401 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 401db11f-aa8c-3132-b007-647226278b40 | -7.85065 | -49.65427 | 2025-10-24 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2bd6e6d-b866-38bc-a388-fe0e3ad1fbce | -7.68472 | -42.24204 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d1dcb936-c954-3e07-82ff-0c4d5c379d92 | -3.13938 | -50.61793 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b64ffe3-a133-31f0-86c3-8e2c830dcc0a | -8.24684 | -47.17125 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c09e768-2e6c-3f29-a4f7-7cdd5d98ae8b | -9.64342 | -46.89728 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5f0b3b0-e3aa-30f4-8b40-38420385476c | -9.50149 | -51.82341 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aee2984-6bc6-3cf9-9f71-a582b2f20c3c | -7.62253 | -41.84655 | 2025-10-24 04:38:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e782154f-07ae-393b-8871-c03fd9de71f5 | -3.92193 | -47.69529 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a658ad9-43a1-3ccc-919c-2e95cb43b4e9 | -9.59886 | -46.92463 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3325f24f-9988-3b03-ba0b-eaafcaf7c026 | -4.28256 | -40.70004 | 2025-10-24 04:38:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ee107b2f-dfd7-38cf-8d4c-c2b376b4d10a | -2.80866 | -49.13422 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51656782-5242-3898-9cbf-ad942ff04feb | -4.96453 | -48.67355 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca7d268a-bfef-37be-9fcb-255b51e73e14 | -8.02492 | -54.88871 | 2025-10-24 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af4533a8-e4b6-3a7e-962d-5417d40334ae | -3.27948 | -50.15485 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92d178aa-d257-37b7-be9d-9a4a0125a926 | -6.55723 | -48.0472 | 2025-10-24 04:38:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3536948a-0fd0-3ea3-8d9a-8d5fb6826d09 | -3.08819 | -49.51395 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 912de527-6a18-329b-a998-0917bc66f1a8 | -8.43799 | -48.69849 | 2025-10-24 04:38:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fee7fa1-86d8-3cca-8af4-e2c286e3bac5 | -5.6588 | -45.95603 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1fe46d1-fd02-34b7-9a81-a2e7951e1db1 | -4.3801 | -43.29775 | 2025-10-24 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a1eaf3-c543-3d3d-b09e-8fb5ec340060 | -5.60521 | -48.66056 | 2025-10-24 04:38:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a30e8372-b359-3fca-806c-877c1fd46051 | -5.01896 | -47.15033 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6cd4883-c451-378d-ae39-801f6edfbc3c | -8.12028 | -47.04908 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 334b98d5-77b2-34d6-9d29-fa1a259c3b6b | -6.77608 | -45.4851 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27ac0238-9272-327f-bfa0-354c0cddb190 | -5.75953 | -46.68829 | 2025-10-24 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7202b99f-dc6f-3c2d-8451-a76c17081116 | -10.56036 | -48.9982 | 2025-10-24 04:38:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd7e75b9-afe4-3954-a308-0d06a9c73906 | -4.18066 | -42.98475 | 2025-10-24 04:38:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e639a66-02af-3820-9d48-341ec1c04755 | -9.85877 | -44.89983 | 2025-10-24 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97697490-5b98-3105-8c0c-23bf6328a303 | -2.8048 | -54.3821 | 2025-10-24 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24bb0450-99d9-347e-ad90-5298b5aacbcd | -4.45738 | -43.2389 | 2025-10-24 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 609358f4-5cbf-3f56-ac8c-4ac4f9a8acd9 | -9.63557 | -46.90052 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17a90efc-b1f5-3b10-ac66-0497ab10a163 | -8.62131 | -44.81104 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c58522fd-1d31-3e32-bdf8-9321240b5887 | -3.84394 | -49.93533 | 2025-10-24 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f006fce2-6ec7-3575-b90f-e8c73fe07b3f | -3.11249 | -51.21084 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a762231f-b56d-3f04-86fe-bc6de219db4f | -9.96832 | -47.73616 | 2025-10-24 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30bb5c48-5f61-3e4e-a052-c8e2cefbf022 | -9.08695 | -47.82176 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f3c3790-b5cf-3631-96ba-74ce5b7f7eb5 | -3.24482 | -48.76189 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c060e3d-6229-3294-b974-4a9a943d6d3d | -9.19168 | -44.53945 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f4dc07e-5a06-392a-a1dd-8850745df7da | -5.59219 | -47.31891 | 2025-10-24 04:38:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1d5f9d6-377f-3472-a8da-0f553f7c44c8 | -9.63321 | -46.89163 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8a5a126-c9fa-3924-be43-43e4d89fe7e5 | -6.90845 | -51.17303 | 2025-10-24 04:38:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6eeb5ff-b1be-357c-b455-c830bee7a910 | -8.31999 | -46.25349 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47a11853-ed5f-3e67-8ac6-4d07457f0f91 | -6.59999 | -48.77087 | 2025-10-24 04:38:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed61d57c-792a-3115-97b6-a8d88c10886f | -4.45796 | -43.23505 | 2025-10-24 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 95f8739a-b7a5-36bc-a3a2-29c5e201a6a3 | -9.86976 | -47.72919 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7790f9c1-72cb-3556-814c-c223b11006b7 | -3.84117 | -52.14033 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README39.md)
