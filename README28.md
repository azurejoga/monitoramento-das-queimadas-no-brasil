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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b8cc6ef-e4ab-36ba-b189-3d9cf9af99d9 | -5.54867 | -42.68112 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d00457b-41cf-3ef7-836f-3cdf60eff956 | -5.55822 | -42.66438 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 56540db2-2a18-348d-bfb0-5cf749ccfd79 | -10.87553 | -51.02839 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 0e9d4e96-2301-39d7-93ed-91f95bbfaf22 | -7.70182 | -42.39466 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e660e95f-03f7-341a-bf74-8762c8912940 | -8.53177 | -46.25456 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 5515114b-e4ba-3e37-a83d-24ebacd0b7d5 | -12.10255 | -43.45311 | 2025-10-07 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2b84b93-1f0d-30d1-b380-8ca91017d6d8 | -8.95969 | -50.79615 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d751b72f-1f99-348f-9184-d2779994e5e7 | -11.81131 | -45.1157 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4422696a-5a72-3cda-aa00-ee10d97a952b | -6.64677 | -41.98472 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4152d96a-cc42-3e6b-8caf-938d03fffcbc | -6.06676 | -43.4789 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e86d1506-70ca-3d5c-9a48-3c4ef17e895f | -7.00613 | -42.78916 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 82f277a5-0cf7-3f15-b278-6534fdebe0ae | -10.87518 | -51.03295 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b34f83cf-02a1-32b2-9ee6-02c94b2447fa | -11.67978 | -46.33953 | 2025-10-07 04:08:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ca92a69-f1a5-39cf-ac19-cf9127b592a3 | -8.65572 | -46.30011 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fd5fb59-502e-30cc-9200-c02d278af15d | -7.67281 | -50.21029 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33329a1a-f0bb-3408-a2bd-05af8b57c3f1 | -10.39858 | -50.30631 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5837ca5-6965-3ba5-93f4-ddaa7698477c | -9.19624 | -47.84676 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6614c56f-4624-3535-9fb0-67a49fef88c5 | -8.17144 | -50.163 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1397ee2d-293a-3021-8b10-0fe734a38ca3 | -11.25832 | -50.27758 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 45446ffa-b786-34d8-a539-fa07d4863821 | -10.39376 | -50.30542 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 454879d4-cea1-3ea4-8702-3347ce737661 | -7.465 | -42.6215 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88337e1c-fede-3713-944d-c9bf2613665d | -6.72214 | -42.8387 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0e3f74ea-9550-3437-9bb1-3ba60f615a33 | -10.26521 | -44.36003 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a1979e1-92f3-3429-94b7-7bfa74b3a823 | -7.80166 | -44.14274 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ecf6a5b-b66b-310d-a0fd-48ec050b9c0c | -10.49563 | -44.4124 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a04fb824-a870-3fc2-8fe1-cd03acab7ef1 | -6.72775 | -42.82505 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 004409d5-7d5b-3fee-919c-ad68bdc2a9ea | -8.53532 | -54.85835 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58cf6427-6c82-3704-950b-148edde68652 | -8.65518 | -46.28043 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76929583-332e-34db-8fe5-b5c27b100b0d | -5.64656 | -45.96211 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7779f34-32bf-3a8e-a1d4-851f021ee2b5 | -5.74041 | -49.13048 | 2025-10-07 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 42fb709b-c8d0-3d58-9736-42d6313e94c3 | -8.53637 | -46.2504 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4f8e1929-40ce-3f50-8760-e7c53db3185f | -10.25256 | -44.37336 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 870e8230-af21-3204-9585-dadf51982af4 | -8.6524 | -46.30194 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddca7bfc-cd6c-3742-a2fd-fdd7bdef93e7 | -7.64779 | -43.89713 | 2025-10-07 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d55e2bda-7723-3f1f-8314-a52cc22e59e3 | -7.46722 | -42.62901 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 187c7d91-083a-3d78-81d7-2c623789b8a7 | -8.53087 | -46.28364 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82235789-0275-3761-881c-5b7c9afb53d8 | -10.74387 | -50.49189 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5e190fe9-0184-36ff-8730-2a27ff1ccbe7 | -7.64902 | -43.8896 | 2025-10-07 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f86fb2e2-ae44-356d-9bdc-17d36dcae747 | -6.81633 | -42.78458 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6bb48673-523f-3424-9423-2fffc6dd01ec | -6.97476 | -41.99812 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cc2a0af-2608-395b-8b62-d86d4715161a | -8.52875 | -46.24918 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 3e442340-ad89-39af-8791-3cf6f178aef1 | -11.49105 | -44.97276 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6d1db99-211e-3340-8e2d-42ed742b238a | -5.40119 | -45.91212 | 2025-10-07 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54cd0680-db4d-3307-b7ce-fa4cc559611c | -10.91615 | -47.11832 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52f90380-1798-3cc3-bd0d-3cd218f90957 | -7.56233 | -42.6514 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 287dc64c-9714-37b6-ab30-3ca21f488d26 | -8.17812 | -50.30051 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8174eb6-e887-34f6-b835-d4ff67f93a63 | -10.45062 | -50.34926 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b3f0b8c-9d82-3211-8577-4a37e9d6d547 | -9.88491 | -45.90542 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91675792-038b-3e31-bde3-7016630b1792 | -8.60975 | -44.9177 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 775b197f-5551-39e8-a8c3-bd41482a7f32 | -6.98375 | -42.86543 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50dfbb24-68e1-3265-9d9e-f9f7f1f4f513 | -11.1191 | -47.22273 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d5e0747-a38d-3089-ac71-8703532d3ed4 | -5.27648 | -43.30148 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ee2a5a7-571b-3748-accf-9ba30d6a55dc | -10.4217 | -50.31609 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7669cd02-aa86-389c-b0fe-4d5cc5106a3a | -5.29987 | -44.55444 | 2025-10-07 04:08:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d8ec997-b2ce-32cb-9a20-b3686a11248b | -6.25053 | -43.27657 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 562a520b-f51d-3baf-9ac5-3b99619ced47 | -6.42221 | -47.8256 | 2025-10-07 04:08:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b4fb427-e36d-3914-94b5-6e3d7be3fbfa | -6.3166 | -41.61436 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bdfe3cce-a470-328c-abb8-07e868d405bc | -11.95554 | -45.48678 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f55b0290-c382-3258-8248-c095f5322c80 | -6.10415 | -43.08957 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3221ef26-7355-3090-b61d-843ab71ef8df | -8.34474 | -49.65422 | 2025-10-07 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b41d335c-4385-3740-938a-62555185d8c7 | -7.68309 | -42.40598 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 14ba67fd-c0f2-38ab-a089-9da43472cb97 | -11.84451 | -44.91589 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 748337e1-5577-37f7-8fe0-5cb08b327999 | -6.13323 | -42.66856 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ae1d6f4e-2896-31aa-9133-104434605feb | -11.71582 | -45.44374 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d1d86cd-10bb-3e60-b37a-8927984d6575 | -5.71634 | -44.83347 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bb67f94f-0dee-31ea-8a13-5959b6db6a62 | -5.33248 | -43.39085 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd366954-385f-37d2-8a6c-199652214689 | -5.25902 | -46.49645 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2ac3f0d-17b3-323d-97df-c2051275c42a | -12.01782 | -47.78812 | 2025-10-07 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ea68b053-55bd-3f61-9ecb-afc9ba276971 | -11.02252 | -51.15691 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67cee34d-9caa-3918-a31b-f805644e8adb | -8.65622 | -46.30254 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 183ddcb4-e387-3438-b8d6-384b2c79dbb3 | -6.38098 | -43.29379 | 2025-10-07 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c388c9d-bc4f-3deb-b819-d0b02cc018b8 | -6.98262 | -42.87251 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bfd2bddf-3f3b-3ff8-b8bc-3e5f5580afa8 | -8.48797 | -46.3055 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ccc43858-068b-3715-81ef-d7b417eeca23 | -6.37758 | -43.29326 | 2025-10-07 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f73800b7-46bd-3d8d-bd49-0a952d9d0d78 | -5.67037 | -44.26099 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cca08271-534e-3d8d-8551-c24caecce2fb | -11.38487 | -43.49129 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e46861c-2644-30cf-a155-6c38fe6d0abd | -11.8491 | -45.05896 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c2d79df-b440-30ae-aa78-6285b0ee4812 | -10.41473 | -45.38217 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4acf532e-34f7-3bd1-a373-674108ea2438 | -7.00382 | -42.84682 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| abf53950-ded8-3473-9eaa-412ed7450362 | -10.09676 | -50.51951 | 2025-10-07 04:08:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb6ecfb2-6ef4-3f32-bdfa-567d888f6869 | -7.7211 | -42.40126 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d88e82db-83ab-3a7a-8dfe-61aae71e5021 | -6.59062 | -44.6299 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fee03259-a80d-379a-9b7f-77bd62c9131c | -8.61485 | -44.93097 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2981721a-b6b8-3d50-86ea-1a7207116144 | -6.66727 | -42.7569 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5b5cb95e-9e3e-34ea-8a8e-a0ab294c2b3d | -6.25451 | -43.27343 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb7ad66c-f195-3488-a14a-8fb1f9562c22 | -11.68612 | -45.27618 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f5ad6aa-ebd5-33a3-abbd-6b4f87da067a | -10.91603 | -47.06494 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5e0fd7b-bd9b-3290-bb64-91f0647d06e4 | -8.62128 | -44.93617 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 274228d7-74df-345b-9d0d-4941343609ee | -11.9428 | -46.4492 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee35a3ca-8c2f-3d6c-9a0f-b9ebb64c8e6d | -5.79939 | -45.21728 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c3340c-a363-3620-bc65-400e37bac72e | -5.68854 | -44.6377 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0249a4e2-3a11-3437-a051-deb46bbe0b66 | -8.26626 | -43.83132 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d4cdd4de-b43d-3747-a857-c9e9878af15f | -12.2207 | -44.24614 | 2025-10-07 04:08:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2fb64ed-41dc-304b-be09-e6a18014bc8d | -10.88445 | -51.03616 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 69e7c54c-65a5-31fa-9a86-ea5a4bcd179a | -5.14951 | -46.12005 | 2025-10-07 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b8adfdd-2a3c-3783-8706-928bf1ef1310 | -6.20518 | -44.09872 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f15d0ca5-f341-3244-9178-bbf3e0023052 | -8.53717 | -46.24561 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 9d1a77ff-9fb4-3eb1-8c1a-fc42c5f5bc75 | -6.67839 | -41.3895 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 976e2cb8-1552-3807-b6fb-ef5718b37448 | -11.79215 | -45.10882 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4677ab81-dd96-3366-9f4a-f0769d6b2be3 | -6.92746 | -45.25664 | 2025-10-07 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README29.md)
