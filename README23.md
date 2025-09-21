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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae6ae2df-e54f-3a8b-87ea-d19199f4799c | -6.3394 | -56.19289 | 2025-09-21 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f471201-d2bf-3520-873a-e6f2374eb753 | -9.77078 | -45.95389 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8639cb73-7b48-3947-bee6-22f15b2b3495 | -10.78615 | -47.33488 | 2025-09-21 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b96d0446-23b6-3c5b-900c-3f525eb7da45 | -10.78331 | -47.33065 | 2025-09-21 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8fb75bb-2568-3794-a12d-a9dba8030265 | -7.94161 | -44.09613 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 86a2af93-733b-3b49-8387-630850ef660a | -7.81037 | -46.18795 | 2025-09-21 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e06b5100-29bd-39ce-8b82-b08a7c85b78f | -6.6756 | -42.43388 | 2025-09-21 04:36:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb8ca30f-5798-3c52-b9e1-c358837b75ac | -7.45962 | -42.63319 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6be8af14-c226-3460-bebe-18a509d07441 | -11.2201 | -49.64325 | 2025-09-21 04:36:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b1a05ca-8728-3715-bb5e-9d1c219cf5e7 | -6.73282 | -43.0246 | 2025-09-21 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6c7b159-1028-3a06-ad8c-1fbc84f40ce5 | -8.94398 | -44.20267 | 2025-09-21 04:36:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 287efe88-f2ef-3c51-a2c0-a2810235adf9 | -7.92283 | -44.11744 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7d4de33-e879-3f54-9690-c0bc206a498c | -10.24092 | -46.49173 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c3042d3-5281-3d2a-847e-158049823b56 | -6.80391 | -43.79918 | 2025-09-21 04:36:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45de6a8f-3336-3fd1-8176-e545be7a2144 | -7.72917 | -44.43511 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33c318b2-f0bc-356e-9785-f4f51770e0ae | -7.99839 | -50.86562 | 2025-09-21 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 524cb043-99f6-3cf1-87da-47fdeb6a39dd | -11.30589 | -47.5165 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e1e22f2-05bb-3040-8eac-03a5c7d56216 | -7.83204 | -45.61571 | 2025-09-21 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0efe2aae-ec96-3280-b13c-9694e9975482 | -7.41692 | -44.54549 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fbd025a-959e-3f17-97b7-11e1aa30ac49 | -10.57109 | -48.59084 | 2025-09-21 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b70525f-ad64-3a04-aa6b-5a1949edc797 | -7.59849 | -45.49339 | 2025-09-21 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ef63b09-732f-36d1-8334-688f74d81dbd | -6.55231 | -43.53549 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61ca4315-701d-3383-b8c3-587a33eead6b | -10.08875 | -46.08827 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4214d523-c1d4-3c18-87ed-2f3fe696e634 | -7.94091 | -44.10086 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1b153b49-577e-385f-abe7-4db358e32e37 | -7.83082 | -45.62373 | 2025-09-21 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90de3d93-db79-364e-8a48-29e0dd3d98cf | -8.28176 | -41.68525 | 2025-09-21 04:36:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c773a8c1-4c04-307e-b368-0f40004c6029 | -12.31815 | -44.84762 | 2025-09-21 04:36:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfda805e-e74a-3ba6-ba4f-967c706142ef | -10.3554 | -47.89387 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a0e6f4d-0e0f-3013-8cb1-15d2cefbfd72 | -6.59384 | -43.57799 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f5366fe-9e06-3ed5-8449-d0d2387b0b0f | -11.48611 | -43.5873 | 2025-09-21 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 504a43c0-0895-35f1-a974-6963f85d6836 | -7.93187 | -44.10917 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67c0d1fd-13f5-352f-bd70-dd148de4be83 | -9.17574 | -44.62489 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5846d81-67fd-3d86-a959-cc78bd1336d2 | -5.64294 | -51.70962 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f43d5008-f8ba-3794-baef-d49d8b9c146e | -7.62057 | -44.43831 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d32d4cd-cab2-3e44-a0d6-4e2274c09daa | -10.02564 | -46.27036 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2863ed7-e7aa-3ec1-94d3-55418153f76b | -7.71921 | -44.454 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e69fcfe4-c639-3f1a-9140-f764e991aae6 | -10.02744 | -46.25854 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6778333c-de55-3ba5-b145-e8d78c76e772 | -7.6199 | -44.44271 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0236e2f4-f8b5-358d-9f99-35cdf4ef34fb | -5.60109 | -51.49366 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8887179-d171-3494-a05e-7bb40ca2aa2b | -5.69591 | -51.75863 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25a64829-5b61-3475-a40c-f3db607946c8 | -6.72879 | -43.02408 | 2025-09-21 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1b96ee3-2238-3c92-a85d-7b03c3f9109e | -12.07212 | -44.83509 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac762cbd-9491-3a20-b0d8-bb6614b3625f | -12.11985 | -44.78523 | 2025-09-21 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82cdfd79-d5ef-35d7-a2dc-d9dc9393122a | -6.95043 | -44.75445 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9105235a-b980-36a2-ba3a-b070094d81c2 | -11.20511 | -42.1949 | 2025-09-21 04:36:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0f2ad445-86a4-333d-bac5-8a903078495b | -11.29158 | -47.40474 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e562cf2-8833-3fe5-8b75-d8ec4af418aa | -7.35886 | -44.56526 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1264b7ef-9dc0-3ca1-9bd6-823921e68ec1 | -6.67203 | -47.73534 | 2025-09-21 04:36:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26032864-0a93-3f05-b726-650a6fe11efb | -7.56297 | -42.21291 | 2025-09-21 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 82d8f368-bcc1-3675-b33e-9be433d41d9b | -8.48552 | -48.26507 | 2025-09-21 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66b18484-ddd3-3abc-a0f5-feb3fbc0a188 | -11.29725 | -47.41328 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1c07b98-28ad-335e-aea1-683b05cd0d8f | -8.48829 | -48.26909 | 2025-09-21 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28d4da0c-1e0c-3e89-9e56-659ea3b410f3 | -9.43067 | -44.72108 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e0d3e2b-e6b0-36a8-bab7-c81b83f64915 | -10.27607 | -46.06773 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba74969-41cd-3035-9689-a0d12e5c0d27 | -7.19227 | -44.45272 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a50f89-23c4-3734-a1c8-e8714b8b90b6 | -6.21656 | -44.70937 | 2025-09-21 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84506c7d-f313-399d-8606-243192f6cc21 | -8.59901 | -45.3488 | 2025-09-21 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e082a31-65e5-3f6e-a4db-1a444dac70ac | -9.63201 | -46.65504 | 2025-09-21 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd69a375-50c8-308d-9a03-7f517c99c897 | -9.17859 | -44.76003 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16e10b74-92b1-397e-a955-fe4d152c349e | -10.32279 | -45.22972 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01778dc1-816e-3db1-bb94-a3a4e8078a73 | -7.83556 | -45.61631 | 2025-09-21 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96b005cd-00a9-3a73-9449-4770869f0f2e | -5.79671 | -50.20024 | 2025-09-21 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eb44822-edce-3432-a746-ba93769811b8 | -12.07706 | -44.80845 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c465a5f-2acc-32ce-8a9d-966c743507dd | -5.58894 | -51.1959 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adee6a0e-22fe-38bd-aa56-08e9b1c9bf48 | -5.56367 | -51.79469 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1864473f-5312-3d35-8c30-e18d2255a006 | -7.71627 | -44.46962 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75e2f89c-e086-393c-ae7b-8128b58fcd4e | -10.0606 | -48.18569 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7631d7bb-5996-3dd1-a34a-61a1c2d7aad8 | -7.18961 | -42.24435 | 2025-09-21 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5cd5cea7-65e6-341f-b9ea-f66061af244e | -4.36983 | -56.03092 | 2025-09-21 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c303714b-4692-3656-bfe4-c11f664f9a7a | -12.07772 | -44.80366 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf3c4df2-671b-3f90-adee-37b43f3d9145 | -10.414 | -47.84827 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d8bef44-2947-38b6-badf-c26709c46bcd | -12.07455 | -44.84556 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c9b702d-e398-3b74-8b31-7bf4ba9f2ee5 | -7.42062 | -44.54608 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9fe6ce2-4de9-3dde-a2b6-061555959380 | -7.9211 | -44.10271 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3dbc8040-4112-3f96-8e45-1beb6b3e5529 | -11.27699 | -47.47795 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41df59ec-b53e-307a-87eb-e37adb9204ac | -10.03798 | -46.26009 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a39928a-6ba0-3e7a-b5f8-5a2752fec063 | -12.09039 | -44.8545 | 2025-09-21 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0eca69b-ff82-3b1a-ad75-6b02ab3721a7 | -7.72537 | -44.4641 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 91b2ab96-5cd3-3d99-bb3e-11cf79225a1b | -10.26725 | -46.05413 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9839caf0-3c10-3a88-a259-6d37fcbad6ee | -10.26665 | -46.05814 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6aef254-8282-3b55-a528-bc6abb608aa4 | -5.62547 | -51.69725 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f0537a0-9eba-3517-a36f-16e6faadb0c8 | -7.47913 | -46.66356 | 2025-09-21 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64adc44f-b83d-3d74-b731-cbadf17c41bc | -12.33475 | -44.09863 | 2025-09-21 04:36:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22c0c305-7c51-3aca-bf15-fd2ff4c273df | -10.28869 | -46.073 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 16bb1ee5-f03a-31aa-aa92-6bcff1544dd7 | -12.08652 | -44.85397 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25c50efe-40ab-3f19-b843-a2a2436692c1 | -10.29518 | -46.10263 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e050a2e9-4364-3db1-a3ea-ade545b70a35 | -11.30189 | -47.49714 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55a3e906-cd53-3ecf-a24f-0fa7c422c258 | -6.02961 | -46.36456 | 2025-09-21 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fd85e30-5f6b-3cf9-be31-91d58a570387 | -5.58966 | -51.19156 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0e6d9b1-b113-3a83-a28c-c3bcf4b6a55c | -9.99883 | -46.23414 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2178b3b-ee99-338b-b929-e85d7df41417 | -7.34991 | -44.59941 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b8be6d0-ab6f-3993-9912-53d90f8ca194 | -9.42957 | -44.70211 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c8e1ed1-bcaa-3889-86df-492da6c0c614 | -7.6103 | -45.48711 | 2025-09-21 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b143f723-d454-371a-81b8-fd7fbf8749f5 | -11.28664 | -47.50596 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ad87423-9b60-3ce5-ab97-7229221c3625 | -10.21988 | -48.06938 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e209d11-1409-386f-9ad9-e3164c655c6e | -10.02273 | -46.26595 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57f20bbc-b6ce-3757-8aea-078d1acf72bb | -10.29402 | -46.08603 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7279f78a-8a26-3d29-ab18-0d07ac571cf3 | -10.33864 | -47.8912 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b339e66a-f3af-3b30-b20e-c77329bd8291 | -12.06964 | -44.82492 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b3c312c-444c-3ec8-8e28-0116928dbdd7 | -6.59557 | -43.59304 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
