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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73409558-f805-3217-9df2-1190e66c6691 | -9.16775 | -59.45446 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 61b2b436-775d-373d-9881-27ce6e932b5f | -6.60659 | -58.38528 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c46b1676-3a5a-3b9e-affc-9a128ad54717 | -7.2904 | -52.53441 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83eb4589-3e96-3377-bb8b-e6cb42746db5 | -10.89622 | -50.27501 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc73e044-78f2-31aa-87e2-94c2b9eded78 | -6.8864 | -56.43307 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd42768c-155f-3359-94ad-131fe6c17bfd | -6.5339 | -55.17297 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab72751b-5bed-37a9-94db-d4de38fc1636 | -13.45241 | -51.76357 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95696778-72b6-3948-b4c2-50188948ed0d | -6.92037 | -59.35061 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e18e8271-afee-3d57-9a1b-06b00339c836 | -5.74706 | -53.57749 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11b95fe-46b8-3bc8-8954-8f801c642489 | -8.09273 | -51.66602 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e8eb8e9-a725-3256-b43d-c324bc91bc44 | -10.80614 | -50.97888 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb0689d6-a8dc-34b4-b03a-b1dabdc74fb9 | -12.76713 | -48.40522 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad1f454a-9d6c-3a9e-b066-04cfbf14a55a | -6.86357 | -59.42958 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20d60aaf-2e56-35d0-9a2e-d4bbe46f2db3 | -6.25075 | -55.42249 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c476674-7101-3ceb-a35b-fa3170eb1304 | -12.81749 | -48.41576 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 442a38f3-af88-305c-bb56-e1f89d3a6097 | -8.53555 | -55.3283 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 098ccc20-d9e5-30d4-95ac-c11956c56c94 | -6.43061 | -54.94755 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80ef820f-428a-3f93-81f1-5bf069c76035 | -10.51248 | -50.77547 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8de7538e-9125-3684-9c26-d6a63f71baef | -9.17928 | -59.43954 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ca8e6ca-a506-3a5d-9486-fff94d0e8f89 | -6.95088 | -59.30627 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd8f80e1-42be-31ae-aeec-9f6f05a9bfbb | -6.37615 | -54.94313 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a65380bb-c2be-3953-9bbf-a1c900e331f5 | -6.78283 | -58.66581 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 109b6481-212c-3e03-a1d3-32162bd16c35 | -6.6097 | -58.3925 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9af5a35f-1186-37af-acc2-79c84a7c9d62 | -12.76862 | -48.39428 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ab2745b-4d11-3db3-a64c-8f825c7edff3 | -6.87972 | -59.42562 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 911660a1-2715-3b4a-a8ba-e82335199ca9 | -11.17505 | -54.00948 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d744a9a-5fe1-334e-860e-90fffc4226cb | -9.18647 | -59.44927 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a1f1229-9f37-3679-96da-ea08f1d70f5e | -11.2035 | -55.0714 | 2026-08-22 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b9ce212-2343-3f50-8adc-7e0833df61eb | -8.53914 | -54.81677 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95495c96-4e34-321a-ad76-b9723fded1c6 | -12.83197 | -48.46573 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ab3b355-19ba-3f8c-900e-ed0d9ff7644a | -7.54642 | -55.56012 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65dd3d38-4563-369a-83bf-d9ea59580abf | -6.43629 | -54.95628 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e50bc08-1a38-34af-b4bc-b781d6e7a477 | -6.79196 | -58.63849 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7cb8690e-04a4-3f94-82b8-9e63267d296d | -13.47583 | -44.03905 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f67a24e7-0693-3524-99d6-01098d2f61d3 | -6.243 | -55.42532 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1927afac-6a7a-38a8-93af-0231cc84722a | -8.89884 | -60.60085 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10c76d47-c437-32f3-a04b-173a31930a18 | -8.03427 | -54.00499 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a0e0388-4b6b-3f8e-bbe9-73f93f2f8243 | -6.79034 | -59.4261 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f6c16ee7-4628-3e57-95fb-de29f9aeb1ae | -12.81667 | -48.41882 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ed5aa56-be88-3872-8caa-55df25d78206 | -9.45294 | -51.59784 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43376dfb-381c-37fd-b920-d761c3b2a330 | -7.07607 | -44.99985 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7779de11-c618-3f8f-bf21-ac40f7dc2ba7 | -9.17833 | -57.06678 | 2026-08-22 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa0145b-870d-3f59-bbf7-678c41fc7c9e | -11.16341 | -54.01839 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 493752ef-c558-3f78-a6a6-9c628898c1b1 | -7.25981 | -49.9062 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f3fb3b1-3612-3819-aa2e-dab9c80f561f | -10.51286 | -50.82148 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1925217-be27-392a-ba40-a792dd30624a | -9.84265 | -57.71508 | 2026-08-22 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9576bcc8-8d37-3521-a1a2-eb3eab3d9f21 | -8.55359 | -54.85656 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1966f8b-ffb2-3a13-8b14-5326686eb63f | -6.38346 | -54.96395 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c30784c-86de-345d-a7aa-2eed516468af | -8.10946 | -50.04929 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1203b4d2-84e5-3772-970b-89eda22d41f9 | -6.21997 | -55.48464 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e9371f9-559b-3b8c-8e51-f62944611c94 | -6.88049 | -59.42119 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 02f22934-4565-32ef-85c8-cd817b92a361 | -11.16561 | -54.02597 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28bc49b9-bf32-370f-8710-14c6a98d1117 | -6.8998 | -59.00111 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4615f0d6-6449-30a3-a50a-e2a74a0dce30 | -6.1118 | -53.07296 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c34796f4-b981-3c54-8898-3ca2900d336e | -12.26269 | -43.17944 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4f5563b2-7078-37f3-85a1-b2bf0b939c06 | -6.77361 | -58.66835 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a0b446b-e261-3c41-b2e1-bdc11503e9bb | -12.84617 | -48.45623 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b247aa6c-10d8-3354-9050-9b026ccc4de3 | -7.36994 | -55.69164 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ffd810d8-012b-311d-928f-c1a8cd141d34 | -6.86579 | -59.44384 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e702136-b3b0-3adc-a101-533fb099fa98 | -7.34776 | -55.67137 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f881bad-629a-3fa1-b44e-b2aaab7650ed | -6.8038 | -59.42839 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d694e217-e9e7-32e8-91cf-b9313b468992 | -7.4786 | -45.14177 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49ce2059-4ab8-3349-860a-aebd1907b6cf | -6.66893 | -58.75095 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ad0cc78-96fd-3e21-ab10-9c89bfee0a63 | -9.21644 | -60.77501 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7280b31-861d-3f20-9cc4-c0b082ef2582 | -6.79483 | -59.42682 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| c13ee7a9-6829-3a1e-920e-62bb93636d80 | -6.13493 | -59.91669 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a15ef887-4251-32d3-a0a5-39554b13d9bd | -6.75743 | -58.67096 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ce875a28-13c0-3df2-a082-ddfdf5307a3e | -8.09928 | -50.04336 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8e49f7f-da2e-3b8f-b93b-f913e245ecf7 | -8.53615 | -54.83506 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9eb267fa-9fed-3f52-abdf-8a140a76ade9 | -6.93531 | -59.3171 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdba20c5-71b3-3765-a196-ca078549ee8d | -6.789 | -58.63931 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f0500d0-096d-338b-af62-ca3306b236c3 | -9.17493 | -59.46425 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 360c21c8-8bc1-3399-8015-84bf89468255 | -8.6232 | -54.68462 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 999a7f4f-e5ab-3635-85fb-14fc6b2a3c48 | -8.96204 | -49.86986 | 2026-08-22 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a6d1fff-1809-33db-8704-7316af39990a | -8.53047 | -55.32417 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07de68e5-06fd-3697-8809-1ca86298515d | -7.05417 | -56.61133 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0554c81-a58d-307b-9146-8cfda695180a | -6.87135 | -59.447 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 030aa9fb-64e0-33ea-8e17-217d63effafa | -6.78291 | -59.41575 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ccaf33e-d8fc-31d1-930b-9b545da0ba37 | -6.86554 | -59.42759 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be414f72-ed4c-3b3c-93a2-d54dacf506d7 | -6.85234 | -59.44147 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4977cb9-b54a-3d91-ba26-3d05826db223 | -10.7735 | -51.00284 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a13a5df-5eaa-320e-808e-106d1566cde2 | -6.36413 | -62.89869 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4630d10e-12c9-3cca-ae09-6f54ef9f54b9 | -6.69986 | -58.95972 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c2821ea-b02a-3684-aa5c-995b2a0bf464 | -7.82815 | -61.7788 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c17caec-cbcb-3add-b8e2-7de2727a17d1 | -8.15676 | -46.71748 | 2026-08-22 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff0fc35f-3e78-3f61-8698-ed3618da09b3 | -9.28654 | -60.90493 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f75e9726-9043-36ba-99fb-ff37c658a636 | -9.53449 | -63.56402 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b950905-ef39-3d12-88bd-472c77457965 | -7.25918 | -49.91034 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4743c6c-a1e6-3eef-a512-d13f75dbeb3b | -8.49833 | -54.87408 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566fc8d1-9232-3af6-923b-08f08392ff8d | -7.25744 | -49.89747 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6cbc051-4fc6-3311-bbb4-ed65f1ff6bf7 | -6.88567 | -56.43744 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c91208-88b4-3f07-9183-669e4f83e0d6 | -13.25884 | -51.61255 | 2026-08-22 05:04:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba3d7008-434a-3fd3-896e-10cec1f679f6 | -8.5935 | -54.73944 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9433452b-ef50-36cc-b72f-256967efe7f5 | -6.1384 | -59.90487 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5456a69-97c0-3aa3-91c4-11e62d813b94 | -6.79964 | -58.61946 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c3091d3-7c35-3a3c-8b48-69f6b2337eda | -8.64473 | -54.72886 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a7f22fb-6297-32ea-b903-62b0c33f01e5 | -9.58619 | -60.50692 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc40d62d-9a4d-3379-b07a-930f34caadd8 | -6.26417 | -62.53043 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cfdd7ee-b769-3440-a93b-9c790b377512 | -6.22575 | -55.61753 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ab940b58-e5e7-3b53-98b4-9ba5d26d67e5 | -8.10224 | -50.04821 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README42.md)
