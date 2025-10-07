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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0594f9ba-9531-3c9b-83ac-491e1246f1dc | -5.69954 | -42.72277 | 2025-10-07 00:13:00 | TERRA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 3d745bc1-41ee-3b2c-803b-ec4f7fc4c801 | -6.83193 | -45.97586 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8ab1f28d-8ffd-3e15-8082-2d535d2f6019 | -8.74994 | -48.87943 | 2025-10-07 00:13:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fa13a0c2-7a1e-368e-b316-a4622aea5356 | -3.81204 | -43.99213 | 2025-10-07 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09b7b808-86f4-3404-b94b-6cbc8640050f | -3.69596 | -43.68934 | 2025-10-07 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9935417f-0a1c-3b89-9ed3-5b541d65c310 | -7.57204 | -43.97729 | 2025-10-07 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d2b9860e-8a81-3ad1-854f-33e94f75d2ef | -9.69771 | -45.92884 | 2025-10-07 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 14008208-cf98-3a8c-9466-b70057e4747c | -6.29446 | -46.08732 | 2025-10-07 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ccf81e18-b359-3422-bd50-35854c3540df | -5.11318 | -43.20911 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 42116d8f-eba1-3740-92e7-dad66b53bab4 | -5.67646 | -44.26787 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d3a4fdd-8fa6-3d7d-947f-2758219ea6e4 | -4.63928 | -43.18314 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5b8efe67-a22e-34d1-9b4e-0bb34f4e55e2 | -7.00833 | -42.7906 | 2025-10-07 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| a3f35555-a1a3-3943-b3a5-10bb11faeb07 | -8.53615 | -46.26027 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 67bdcdc1-ab56-396b-95ed-333afd4a208f | -5.70777 | -44.83459 | 2025-10-07 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ef9f1011-cc4e-3c45-ae12-0e7d70b358f4 | -5.02014 | -43.66094 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| af821164-d0d6-3b7e-b285-8b3190041e03 | -7.57437 | -46.02018 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7dfaf719-42d9-3048-96fd-418e3b190b0a | -7.26983 | -45.33053 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0c62531-377e-3460-83cf-4fad4eb54522 | -5.853 | -42.83561 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d6215a5c-d279-3275-9d20-cdd0d2cad9bd | -9.2002 | -47.82598 | 2025-10-07 00:13:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 83dbd0b5-33ad-3648-9cc9-e31a884a134e | -3.69468 | -43.68014 | 2025-10-07 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 18fff6ac-790f-3a80-8f01-7148cb933a5d | -6.1018 | -43.09483 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 383c0a8c-f7a8-313c-9df8-a134288df8f0 | -7.68427 | -42.41612 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 537c9746-9a6e-3618-9113-c24ead819c12 | -4.43208 | -38.97168 | 2025-10-07 00:13:00 | TERRA_M-M | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 76e0dd16-bfb4-3ba8-a7cf-50c1567ba2a9 | -5.79921 | -45.22166 | 2025-10-07 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fc053e31-ea70-3f69-91e7-70426ecf9ade | -6.72035 | -42.83789 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e28f1c0b-9afe-33e9-b808-9ebd1f7f975b | -5.49961 | -43.07523 | 2025-10-07 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| def7820c-3257-3b5f-8884-fa593c3992d8 | -10.94412 | -51.1557 | 2025-10-07 00:13:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1c52ae2f-e245-3f71-b306-9135da824643 | -7.7202 | -42.41449 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2c78146e-a602-3454-a72f-87853c11e0ef | -7.48164 | -47.02685 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e348681a-66d4-349c-af71-7f932d0744ba | -8.43181 | -47.64457 | 2025-10-07 00:13:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0afe9b6b-0b68-34ba-bb43-9c7f8a84fc73 | -4.07093 | -43.33969 | 2025-10-07 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4079da5a-caaa-3494-8044-c071125395ab | -6.01489 | -43.13202 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1e67ec14-1219-388e-800a-2fc0bda95562 | -5.1484 | -46.12451 | 2025-10-07 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| abbca56b-e7b8-3a1b-9b13-e80898a6c893 | -5.84384 | -42.83689 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9785a63a-19af-36d9-af28-46c5d7750bcc | -3.81712 | -47.58605 | 2025-10-07 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 210e5e41-a331-3461-a854-7961fa3e29ce | -6.44772 | -44.57653 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 21cfffbb-b62a-3556-816c-a8a0960aa37b | -8.38699 | -41.85605 | 2025-10-07 00:13:00 | TERRA_M-M | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 58884fee-978f-3f21-9972-dbc66ccf9efb | -10.3844 | -50.31931 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f09073f6-ff7e-389c-9be4-04bb546a6b29 | -5.6513 | -45.96174 | 2025-10-07 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c009a9c6-8d00-307f-8963-f4f257746f52 | -7.01606 | -42.7799 | 2025-10-07 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 628e062b-e638-3230-a764-9b4952ec467e | -10.23264 | -48.18857 | 2025-10-07 00:13:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 546909d0-3e15-30b4-b98a-eb70442e14ac | -4.04633 | -42.51661 | 2025-10-07 00:13:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 8b29be13-91cf-3689-b082-3ed6dd837e9c | -5.67523 | -44.25906 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4047aaee-a2d8-353d-ba42-5f74dd0ee3e2 | -8.5348 | -46.25007 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 200e6dfc-6377-356b-a55e-6c61fb53362b | -6.25239 | -43.89913 | 2025-10-07 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 98ea1d91-bdc0-34a6-a724-0f0a947817a4 | -6.65292 | -41.98138 | 2025-10-07 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4f561319-29ce-39ea-829b-c0d32defea85 | -4.68714 | -45.84897 | 2025-10-07 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b94aa8e6-bcdf-3353-9431-35e575c0035d | -6.45896 | -44.59291 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f93f61e9-ec85-3f42-84ce-e98792c3287c | -7.48311 | -47.03776 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 20ef8264-60ab-3bbe-acd2-e81cdb9d339e | -6.24355 | -43.9004 | 2025-10-07 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9329a9b6-6a3a-36ab-9d1e-ebdc7abcaac6 | -4.61705 | -43.15737 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 35a5a3ff-07ce-3482-84a3-611bbeac07eb | -8.57229 | -46.24445 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b20f7df0-11e9-3461-8be0-856d9702c21f | -8.85425 | -46.09956 | 2025-10-07 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 500e949d-c65a-3b5d-9451-dd89fa727b19 | -10.39984 | -50.32388 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 27e019d7-d5b5-302a-8ec9-d793db7f9c95 | -8.69426 | -48.43535 | 2025-10-07 00:13:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a13f3179-6c76-36c2-9c19-cb532d2f06cc | -10.39504 | -50.29674 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 3a316eac-0da2-3095-b996-daa3c57b07fd | -8.17197 | -50.16175 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cb328d27-442b-34d2-8505-a94e3ac5e79a | -8.6593 | -46.27789 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6277dff0-75b7-38c5-94bb-6f19e9f4dd1f | -6.85049 | -47.34491 | 2025-10-07 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 75a9b7ac-52ac-3fce-9ab6-fb16bd8071b9 | -6.45515 | -42.79222 | 2025-10-07 00:13:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2a71dae9-1480-3ce5-8842-3994496214e6 | -7.23134 | -46.46819 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1f982733-bed1-3be4-b42a-f2c6f9801a4f | -6.64346 | -41.98281 | 2025-10-07 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f21e0c50-8527-32a9-816b-d3be120d2b8c | -3.42087 | -43.17337 | 2025-10-07 00:13:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d00d198e-6be5-37ac-aeae-28a8551c996f | -7.46678 | -43.09685 | 2025-10-07 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c092880c-a81b-3a90-987b-aadafd5eda0e | -4.45129 | -44.14183 | 2025-10-07 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 69ce1f22-fb2e-3aa3-8cf9-30d6d86a9979 | -6.56432 | -44.1525 | 2025-10-07 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a90cf2fc-0386-3284-a598-9f7bc7020937 | -6.04351 | -44.1912 | 2025-10-07 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 88338c2e-d938-3840-941f-0b6c08c3f9eb | -4.55082 | -46.67387 | 2025-10-07 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3db2ae18-58bc-3d7d-a136-093e2afef6e4 | -5.03507 | -45.56509 | 2025-10-07 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec298c58-657e-335c-9ebc-9f544dfe4279 | -4.31306 | -48.23543 | 2025-10-07 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5f7a2909-29f4-35f6-8518-64f1d18f35a3 | -4.57882 | -41.30961 | 2025-10-07 00:13:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6abb271d-2b99-3525-adaa-b7f31019b970 | -5.59649 | -44.41991 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 446ee581-74d7-3be9-92cb-926f6780af7e | -8.65265 | -46.29978 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 28d89d5f-e980-3c5c-bb1f-ff94883dc72e | -6.70221 | -46.03508 | 2025-10-07 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fa8c3f3b-8111-391e-81ec-db1c29b998fb | -8.51595 | -46.32503 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 70e51943-0ed3-30e8-945c-8e353cd04d71 | -4.48367 | -44.3091 | 2025-10-07 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1c53fbe-d1ac-3d51-af9d-bfa0417c06d4 | -6.73464 | -48.17582 | 2025-10-07 00:13:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9d2d6f78-eabe-3712-a754-c0b953a51f24 | -9.59268 | -47.85643 | 2025-10-07 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| acffde16-0aaf-39e2-9df7-7447374e4c95 | -8.68426 | -47.07827 | 2025-10-07 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 592797c1-6534-39d7-9d4a-58b2c1bbd6f4 | -6.05098 | -43.51977 | 2025-10-07 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f7920e7e-dda8-3de8-b6f8-5382e7550b7b | -5.87418 | -43.83236 | 2025-10-07 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5bc89672-29e6-3771-83e6-0b80c7ae2c64 | -4.45004 | -44.1329 | 2025-10-07 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff857b31-c7ce-3667-bbb0-e8a6d23b241e | -8.66206 | -46.2984 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a2023b13-534f-3947-9e98-cb40fa686a8b | -6.01279 | -42.46274 | 2025-10-07 00:13:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 90229e9c-b10d-3ab1-bcb4-60fef8ef24f8 | -7.79941 | -44.15779 | 2025-10-07 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bbf45b55-66e3-33a4-91cf-2a7790cf2aae | -7.29864 | -44.79796 | 2025-10-07 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 32c561d4-c60d-3dae-ab87-6c3b87d285ed | -8.74867 | -48.87301 | 2025-10-07 00:13:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 663a3742-e951-34a4-8e07-8d864a783698 | -5.80643 | -46.56413 | 2025-10-07 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2cd3aa44-d72e-3691-9371-51d13ba61cfe | -9.65445 | -43.83631 | 2025-10-07 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4b90a094-ad7f-33b4-abee-a55102d34cfc | -5.64228 | -45.96297 | 2025-10-07 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c446d3fe-7b3e-387c-81c8-d4d11c86438a | -6.45653 | -44.57528 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 83a456c7-883c-3e47-95f1-6a034d1e1a45 | -6.3689 | -46.42991 | 2025-10-07 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| da46def7-569e-343d-9306-88796d9d5b6c | -5.98565 | -43.51693 | 2025-10-07 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2bdf7935-f7cc-3b87-9654-aba3ae368411 | -9.09386 | -47.96582 | 2025-10-07 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b26b8f0f-10c2-393c-8b54-ccfe55c14c6f | -4.49956 | -40.73869 | 2025-10-07 00:13:00 | TERRA_M-M | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1258bc7f-5f95-38c6-b835-7c7fc6d7f751 | -7.46549 | -43.08768 | 2025-10-07 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 61ebf55d-6dfc-35fb-8683-a047129f4aa0 | -6.70486 | -42.85943 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 7df5b1d4-a9ad-316e-a6a7-32b552dbb8a9 | -8.34389 | -49.65005 | 2025-10-07 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 22f9946a-b0f9-3d9a-871f-231308cff64b | -6.09276 | -43.09609 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fb9fb5f2-4845-3e58-9b8f-5440976c3f1c | -10.38673 | -50.32548 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |


[Clique aqui para ver as próximas entradas](README8.md)
