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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 230b3fbd-b212-38fe-82ba-14b1128a9f39 | -6.12342 | -42.4494 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ad2248b-bf7c-3b92-a938-9d66da47172a | -10.95969 | -48.04889 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6e61188d-ddaa-3a4c-92c6-7838befb3d13 | -9.1801 | -44.58556 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6d4f785-0434-32dc-8731-37a3302ea832 | -5.85119 | -46.44474 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 160d3842-99ba-337c-be99-264c5b2e9fc0 | -10.0335 | -47.15841 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cf01865-bba7-3adb-861d-5eac1d62ae07 | -9.55438 | -46.92207 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3158ceb-a8d7-33d2-8d0f-75c48ce289dd | -12.53049 | -47.54936 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7b50e86-896f-3168-aefb-34f572f72160 | -5.56987 | -47.50156 | 2025-10-28 04:14:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c870b6bd-b353-3eb2-a39e-bce78479c941 | -9.33788 | -47.83829 | 2025-10-28 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a5a5da4-fde4-3839-9677-f2a5675c151d | -10.84228 | -47.88938 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a065912f-0b42-3184-a8fc-383ff6ad9ed7 | -6.49132 | -42.22625 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c97e5410-2901-3ebc-b276-a159af7ff103 | -6.12976 | -42.69074 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cac0123c-380c-3a08-bb7d-e433572cfc9c | -6.03466 | -46.56166 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8b85253-4bb3-3d9e-8928-e284e27f006a | -8.05176 | -45.153 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86512f4a-1f16-385d-92fd-7daea9d3ca10 | -8.31447 | -47.86312 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58dbddbb-aac7-3f97-8b99-f78a877be854 | -8.29761 | -42.30927 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1a75576-f94b-39fc-bc21-6dddd3d4168e | -7.26748 | -44.96384 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52339681-5243-3dbe-952a-c8bb51f38236 | -10.93145 | -47.60619 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89f64c62-a24d-30eb-a2ff-6cb8c1e36a07 | -7.16064 | -46.99691 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d7e6c60-bdcc-3a66-8d54-1e03014be622 | -9.53942 | -46.9671 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3cb4346-ac3e-39ce-80ee-d189022b8f29 | -8.51637 | -47.19613 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11462909-af6d-3aed-8ebd-412060489b65 | -7.73027 | -44.04877 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7b0de67-847e-305c-b6b7-c60f8fe43847 | -10.76104 | -49.78254 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 05f4c8c4-8e7e-381c-b942-34220263575f | -9.33985 | -50.35292 | 2025-10-28 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1538aca4-6fa1-37f5-a9e6-877fcff20297 | -10.29679 | -47.24379 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7526ece5-f5d5-33d1-ac77-6b98d432daad | -6.30062 | -44.70531 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb2f5787-423d-3ebe-ad0c-273e4e66430e | -10.63237 | -47.98003 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bf8aad7-a4f2-331e-9692-976595689da3 | -10.76035 | -44.75199 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 372f772e-3f47-30a9-b31d-2f3f1f7265a1 | -10.23496 | -52.15051 | 2025-10-28 04:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfe081bb-9f74-33f9-8a5a-abd52bcbf252 | -6.09776 | -44.67682 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aa38b83-5878-339d-a3a2-c04565cee33b | -7.45285 | -47.15742 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c090deb-3dd4-3ae8-adce-ebba2e25b187 | -8.56546 | -47.73639 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac838abe-6fb5-3d77-920e-6e7319231a3b | -6.28507 | -42.87431 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f0aefd6-1a18-328b-86eb-cab4318cfd38 | -10.7884 | -49.25929 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 449469b7-d71b-3091-bd4c-fd57436fe613 | -9.46597 | -46.88718 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 813226c1-df0e-3b3d-9f5e-ed9249fda992 | -7.96386 | -45.46016 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 01a6518d-6259-39ca-8faa-5e5e7865fa25 | -7.13002 | -47.01962 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2d96010-b3dc-3ed5-91fb-1bb032927718 | -7.4482 | -39.2686 | 2025-10-28 04:14:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fa0e0dbe-0d76-316a-9cb7-db2033bab548 | -8.95977 | -42.957 | 2025-10-28 04:14:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| afb6ee31-9cca-308e-b0b6-5ec0397df943 | -8.16454 | -47.01174 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 279839de-6b81-33a7-bc58-3a10f2bf2ff3 | -11.91319 | -43.82488 | 2025-10-28 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a381f0ea-c89d-3c6c-a2e4-8a980a4969f7 | -6.48116 | -46.72635 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10c21397-11a2-35c5-8d91-128403087ca2 | -13.44754 | -44.03938 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24a18e2e-7b03-32b8-a723-d58a742d27d3 | -12.95932 | -44.62137 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb03d591-12b4-3df9-803e-1a9b1b3992a9 | -7.81315 | -46.4532 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3933d28c-4243-3496-9bed-1be9a0093153 | -5.61443 | -45.9823 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d25db0f-4da0-3dbf-a3e4-4fe5000ad98a | -7.90564 | -41.78699 | 2025-10-28 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 08c177c4-44a5-3489-9d7c-cff080e17585 | -8.02725 | -45.17548 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4c154c0-0fc5-303e-8097-24d18d62a380 | -7.8181 | -46.44549 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a825a44-0c81-3280-bb65-0f31af2f522a | -6.10056 | -44.68099 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c30ce5ea-e447-3f90-a31b-d35e3e883e99 | -12.52365 | -49.58778 | 2025-10-28 04:14:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74e4f4e1-f40a-3833-85e1-242f775ae403 | -9.46738 | -46.87871 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da2a1d2a-c094-39b9-8194-cb3e7b47e5fa | -7.27467 | -44.98411 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46b9f488-69f9-36f8-b222-c0dd8e38b7c3 | -13.54118 | -44.13784 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a256f99d-ef99-38fd-94e0-e93911e26a24 | -8.60394 | -45.43572 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eddda67-865c-3972-856c-3f7e429cf59b | -10.62261 | -44.88894 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ba61a01-7137-3f43-85e2-055e24c47b2c | -7.89846 | -45.68812 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65a2fa27-8bc5-3366-8779-bd771fbb9f52 | -12.01137 | -46.78296 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 499a4b5f-b9ef-3e8a-a5f6-400551e636b3 | -7.67705 | -47.42278 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3745584-6e5c-3939-aff9-31181e6ecdc7 | -10.29721 | -49.07375 | 2025-10-28 04:14:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c446352-932b-375c-952f-f32af05ef4d4 | -11.1235 | -44.56609 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfb8ade8-d925-34fa-a0bb-97ad9e67e63a | -12.54077 | -44.92107 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e81c666-350e-3810-8c6c-d4b1864c7c60 | -6.58537 | -42.69231 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c4dfa9bb-8ed5-3c90-803b-974acdaa2871 | -7.92677 | -45.68911 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de297d42-ee19-3078-b65e-d43bd08d0c26 | -9.89064 | -44.88995 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d85134dd-d99e-3483-8143-e59c9ee0f143 | -6.74847 | -46.35093 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb88c028-093b-3b31-a98b-7e5a3c66fc29 | -8.5731 | -47.01549 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9767de1b-053d-3253-bb45-c7cd189503ea | -7.9774 | -46.73425 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68b47ebc-5603-36e3-a465-bfb012117fa7 | -6.10735 | -42.42209 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c8be06e-c385-3e0c-9ba6-2cc2bc90f950 | -12.05234 | -46.46945 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e0f08c8-359a-3902-9576-f4fbaf509b34 | -8.47636 | -48.21693 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0b94cbe8-5273-3956-ba0a-18d228b50f81 | -9.46159 | -46.86905 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8528b695-76a1-3c04-b681-3619aa5b5697 | -6.07189 | -43.18972 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 653c3af4-09f4-3629-a86a-b1ec5f1dec9d | -8.00866 | -42.94893 | 2025-10-28 04:14:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eeb3d573-61ba-3ffc-8d20-4b5e6eb0fdcb | -13.04207 | -45.85246 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b249d6c4-dccb-32fe-b6fe-62a4d73c3b8a | -8.77718 | -42.81754 | 2025-10-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bcca5af4-5a15-3bb2-a522-d07b4deb27f1 | -5.64355 | -47.64025 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86177d4b-5cac-3c7d-aa77-4fdd9bc6b91d | -13.55256 | -44.26336 | 2025-10-28 04:14:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fe1242b-9c13-3fcf-97fb-2f94040d2c9a | -10.92942 | -50.25547 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df71ad46-00e9-3f02-b548-478699986356 | -7.44825 | -41.86465 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 686bb163-ed46-30bc-8f7c-293ac9b58c5c | -12.24342 | -46.5256 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebabea48-7962-3a14-89eb-6d3eaa567e97 | -12.85082 | -44.63989 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf2adee8-c7d9-3a68-8ab2-6e1cf2b943c0 | -7.45585 | -47.16257 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c42c2ac7-fc2d-347c-b598-8aaafad02763 | -6.26833 | -41.82136 | 2025-10-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 325cf72e-e639-30ad-aa81-36b16202a167 | -8.60983 | -47.72926 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b978289-f7a6-3f31-a1fa-f9b9c95a4877 | -8.86523 | -45.40533 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14b0b3f8-226a-3c83-8e61-7288f5ad3596 | -10.94953 | -50.26773 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cda1f9e0-69ac-3cd3-9dd2-d5f34aa0cf9c | -9.55154 | -46.93902 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e11a3b9-e7dd-3f65-8e8d-d9363b26d89d | -6.44714 | -42.35836 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0132e0eb-01fa-3506-85c4-e2570fbc3dc7 | -9.14417 | -51.29914 | 2025-10-28 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61889b76-ab5a-3d6f-9225-3471488746a8 | -7.59814 | -43.59253 | 2025-10-28 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfc5b88d-1eb3-3633-9efd-de57af7e7d4a | -9.96968 | -47.17903 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95ce9536-b8bf-3dc5-89d6-88eec300c70a | -9.97618 | -47.16246 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c8dd15e-4ad0-3f18-8d6e-5a9a9f516f53 | -12.62212 | -44.25307 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8b29ea1-7754-3ecf-aa56-df5f318301eb | -9.28855 | -45.22435 | 2025-10-28 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa921c06-6208-3cba-b323-08215ca3bdd8 | -9.59794 | -46.86016 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eaf6bfe9-ae57-3dd3-bba0-6674f92b0b63 | -10.56503 | -47.89869 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a13fc02d-7d1c-3a13-aa4c-4bbfda219161 | -6.58316 | -44.62668 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dea1c1ac-b7db-3df4-a102-c1e88a25e708 | -7.7603 | -45.39351 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42604b64-4f6c-3bbc-b105-d15b95d6b269 | -12.62167 | -45.07577 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README23.md)
