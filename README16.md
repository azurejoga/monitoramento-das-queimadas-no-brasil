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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1f9c21c-441f-36e0-8997-05877beef1fc | -6.19995 | -44.33396 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 057bf98e-ef91-3846-bddb-e1165f7555d9 | -5.77922 | -47.2158 | 2025-09-05 04:34:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 009add65-614d-3bf1-bd48-da9c739adb83 | -6.12149 | -44.15366 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9b0db12-ca52-3086-be13-aa835a3784be | -3.48324 | -52.9646 | 2025-09-05 04:34:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee7356af-977b-304f-9988-9bc0e14598e2 | -6.38368 | -43.81468 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f744643f-9c3c-3b61-88cf-3ce3b0a19a75 | -5.93787 | -43.72802 | 2025-09-05 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbaf1c4b-8f88-39b2-af2b-3df528fa9507 | -2.98524 | -49.30303 | 2025-09-05 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7972e3ab-2bef-3348-a6c5-777ae031d153 | -5.60312 | -45.01895 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e62bfd10-cff0-3a62-99af-31b8582d68af | -5.43789 | -42.86067 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e797e660-dbf8-302f-a0ce-be537606d5d7 | -7.34654 | -46.26467 | 2025-09-05 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03fbb935-50bc-3915-b5c9-9e976957e010 | -4.89185 | -41.76031 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e693073e-31ab-329b-8bb5-e1e5bff3c8e4 | -6.40674 | -43.27055 | 2025-09-05 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47166b29-b539-37e1-aa10-cbcc3cb10285 | -6.23073 | -42.61512 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 363c178d-bd2a-33c8-95c2-9efb5e6c8577 | -7.6717 | -46.70071 | 2025-09-05 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99fc7a40-5d9d-3b3b-a21c-769fb90d541c | -6.23182 | -42.44021 | 2025-09-05 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1c54e76-e3ea-3fd4-a755-009765049dd9 | -5.95249 | -46.16941 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24150451-abb2-3205-a169-8d0dfd08493c | -5.26958 | -55.9617 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2e2eda6-047f-390d-b151-ba02fe569525 | -6.20857 | -43.57335 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccd7b7ec-71e7-3ff2-8f07-d074309b8947 | -5.77589 | -47.21528 | 2025-09-05 04:34:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf431d54-d898-35a2-ae00-994ecb54f492 | -5.45718 | -42.82501 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 77851958-5e56-3062-a21c-fabfe8d77892 | -2.42873 | -49.30849 | 2025-09-05 04:34:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2da1958-838d-3b09-af09-b5c6d017fd5c | -3.96712 | -48.13318 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b97c15ba-b1ba-3757-9155-47c238815267 | -7.02077 | -43.24402 | 2025-09-05 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38d6d661-f294-3cb6-9d8a-0835d00acead | -3.23758 | -50.05278 | 2025-09-05 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60b2cfb7-ff6b-3fee-8094-d83fa50928e6 | -3.82795 | -51.19484 | 2025-09-05 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f5c6670-e5a3-3a95-857b-64e30576dc6f | -4.93687 | -55.81652 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7418949-bfd5-3981-8536-3456d9b6b5aa | -5.6557 | -51.26888 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10081275-d9c5-3dee-b0fe-1dbc9d402613 | -5.43187 | -42.85747 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2952395a-58a4-3b40-9f46-ee07f4b94aca | -5.04137 | -56.11279 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef14f992-45e2-3ef9-ba88-974510c62cac | -8.09604 | -42.42883 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0bced834-0a3f-36cd-b32c-fdf27460c804 | -7.90364 | -45.23306 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6093729d-828b-3d73-bcf0-93013bf3584e | -6.68427 | -49.76801 | 2025-09-05 04:34:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 596175bf-f51e-35ee-8c14-cf70079efa41 | -6.88942 | -45.18232 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c02c89be-3896-33fb-aa08-5e8000adfe91 | -6.2888 | -43.50023 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5d4483e-9169-3246-9a19-ff9a909584dc | -4.64421 | -43.124 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b41e2b55-1c17-3756-a6a4-44b0f0335bf8 | -5.68488 | -46.34248 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bf94e25-9cf3-3935-81cd-58acf54f28c6 | -5.10595 | -56.14454 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3beea4d-ff52-39ae-b0a7-235edaff3a24 | -7.07044 | -46.19775 | 2025-09-05 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c904a21-01ca-3968-8b1d-d3fb53e7bafc | -5.54173 | -43.77692 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6f74f02-d0c1-354c-abd4-64e22b91e4b1 | -6.25777 | -43.28124 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d5c5db85-67f6-362b-bec3-d07e03771c73 | -4.20835 | -50.44525 | 2025-09-05 04:34:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02993de3-c947-32a6-a8ba-f6c7270ed481 | -6.22841 | -43.53511 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b12136d-1a7d-366e-93e5-142f64768788 | -6.13794 | -43.3052 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4605126f-1f41-3cad-8137-2da726cff616 | -5.39403 | -45.94345 | 2025-09-05 04:34:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2ba177a-0c6f-3858-a656-df46b1e6e27f | -6.07583 | -43.32066 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7ab8e23-566a-392a-bcfc-4ec91b19eb49 | -6.31348 | -47.762 | 2025-09-05 04:34:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e94fd26-5e7e-3a8b-a820-54664269d1ba | -5.95589 | -46.16993 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0446462e-8f10-3752-aeaf-5a482d950437 | -5.5567 | -46.19833 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d4eb3ea-5677-3976-949a-99d1e8c4493b | -5.4905 | -45.23331 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ac7a9c7-f63c-3f18-a952-d3d7ff04cc84 | -6.21024 | -43.40741 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fccb4480-23f3-3be5-b4ab-546fa89fb764 | -7.88857 | -45.31002 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62bc0468-b8b8-3f95-93d0-51a67b815ab2 | -7.04866 | -42.36473 | 2025-09-05 04:34:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68681d47-83d4-305e-92bb-1ae697450f2a | -6.72628 | -45.92412 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0e91f5d1-80fb-3d23-8748-681c22171f80 | -2.43055 | -48.20129 | 2025-09-05 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 870634a0-3ee0-3a46-ade2-deffd3bfaafa | -7.89169 | -45.23965 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6f6bfc0-052b-360d-9175-926cbe9cdb1a | -7.46436 | -45.20185 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 520d1572-8958-33fb-a42e-2fe86c58cef4 | -7.59656 | -46.21 | 2025-09-05 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0cd5b82-8198-3505-9809-d4cc19ccd5ea | -4.45673 | -41.00922 | 2025-09-05 04:34:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 81fa037d-2a05-3a19-b237-38f7db34a145 | -5.85733 | -45.657 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71117ad3-682e-3ca1-94fe-f29ce14d821d | -5.86913 | -46.03391 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f38533f-eed5-3b03-b15e-002c5d3e19e9 | -4.48635 | -47.67571 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0144cc4-771c-31f5-be5d-4cf25a88e6ea | -6.23331 | -46.25234 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94901397-c4c7-3491-b436-78ae735f4035 | -4.88703 | -41.7636 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eafee1b4-6ff4-3417-9c87-77dff6278ef8 | -4.85515 | -42.54081 | 2025-09-05 04:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 205181a0-bffb-3991-9050-cfb60091938d | -5.70623 | -51.68417 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1c4451b-cc37-312c-bb5f-b421347ba354 | -3.32657 | -54.91286 | 2025-09-05 04:34:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4478a54-aa7a-3b79-ba4a-5ff507d63a5d | -5.90593 | -43.36073 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b42e163-383f-31d9-ab6c-83189fc33d5c | -3.29846 | -43.54328 | 2025-09-05 04:34:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6f37236-c8df-3db4-b3e4-d685c4af7705 | -6.16051 | -43.17838 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21b89144-bae9-317c-a74f-b0d8bbae5e2d | -5.64818 | -43.68596 | 2025-09-05 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 962dbef4-8a1b-3fe6-9cd4-b08aa1b8eb6a | -3.23916 | -50.05185 | 2025-09-05 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7791b674-c69d-3709-8e2f-473aa7bbba7e | -6.30448 | -43.58769 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51bde3e9-1066-31bf-936c-5069f580578d | -6.0018 | -46.68327 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7461ea9d-3f54-3974-a978-865157cefa90 | -5.9073 | -44.16516 | 2025-09-05 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44d07f65-7550-3926-b4d6-cfc821eddef6 | -5.89285 | -43.36855 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eeebc355-955b-36dc-bcce-578eaa1f54a0 | -6.26086 | -53.44231 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d18f7329-ffaf-3d3f-b632-0f7112ab26fe | -5.85675 | -46.11398 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddd5da54-05cc-3f6c-8d99-c649f39c6087 | -5.99205 | -44.73736 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb796183-6ce8-3889-a702-7dd2c2d69f6c | -5.94935 | -43.02364 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 49639b05-bfcb-337a-9aff-0e204665fb17 | -5.7681 | -44.85968 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0b84487-5db6-3c73-99be-fb3f0f4eb42f | -3.67648 | -49.01989 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 841fdbe4-bc17-353d-99c1-ed5eef66989b | -7.36472 | -44.32531 | 2025-09-05 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e336a0b5-d048-38bb-8e9e-2212b56fcfab | -6.21515 | -43.57174 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 130aa600-b2c2-3168-b07b-77785cfb8b75 | -6.74419 | -45.14079 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 781336ea-f9a2-3e12-a57e-a230136bd4af | -2.34737 | -47.58893 | 2025-09-05 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f137b60-f3e0-3217-b7f0-b853a6fa9c73 | -6.26208 | -42.65128 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83b9dadf-835c-3625-a63b-f88d83e19f88 | -7.88505 | -45.28448 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09fa412a-1c19-3ea5-beaa-de0815a7f66c | -6.49571 | -43.73862 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0aee142-8775-38f0-a59d-06bbb7f58133 | -6.4346 | -51.87598 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a45c8f48-1ca8-3e0a-9c61-b436f444d6dc | -5.5537 | -43.77405 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9f8efe4-7ee4-3aae-8e71-01a85b75365f | -5.54541 | -43.07899 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31ccbf66-044e-31e4-b6d9-9e3d56821e2c | -6.01182 | -46.66309 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d49c55f-0266-3514-bac9-77ae6a2729c0 | -5.05738 | -43.86871 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 752a89eb-247c-324f-bc39-e95bd4efdaf2 | -4.17539 | -42.02525 | 2025-09-05 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ad31aea-1141-3484-87f5-c55b05d2423e | -2.95459 | -51.66279 | 2025-09-05 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f456b65b-a8ca-3451-8fbe-741a7f6c401e | -3.22268 | -47.1262 | 2025-09-05 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9abbf06c-4a01-3bbc-b003-f7c891a8fa6e | -5.87628 | -43.16117 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1333b8c7-1c2a-327a-b77d-7c0cfda8e7f9 | -6.8863 | -45.55226 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0a1fe61-362d-3584-ab33-ae3d72f371f3 | -6.67063 | -48.3974 | 2025-09-05 04:34:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fd75b5c-875b-3124-90bf-b26c92799f20 | -6.89652 | -45.18342 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
