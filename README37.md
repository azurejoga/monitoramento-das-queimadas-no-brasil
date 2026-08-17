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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 198eff84-e60c-3592-825f-301a7cd32972 | -8.06794 | -48.53677 | 2026-08-17 04:57:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95611ed1-3c3b-31b9-b82f-88fd0ad36b81 | -6.96812 | -59.30732 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09151227-8563-35ab-8ab0-8007db90bc72 | -12.71496 | -48.47578 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4088100-4bca-36c6-99f7-d41cb6733880 | -6.71031 | -58.94282 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4ca0fe0f-7b3c-3c88-b40c-6d688a5aa929 | -11.46958 | -46.58889 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04f2a874-7440-301f-ae73-27a7ed7ec402 | -6.60012 | -58.96866 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fa5425c7-4c09-39e5-93cc-3d4035468715 | -9.76099 | -47.23247 | 2026-08-17 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31418431-1d39-3986-8914-981c6f495d4f | -11.22502 | -54.01189 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52d3aa5a-7344-3f74-b0e3-687ab80de427 | -11.45214 | -46.59042 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5962f7f8-1750-3a76-8499-23e8002c705a | -6.84248 | -56.44319 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c54b454-b499-38b0-b7af-12265a931bca | -11.83675 | -51.77172 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 788f992a-ada2-322c-90e5-1d712a69e294 | -14.45368 | -51.83675 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45fef53e-4410-3af5-807b-718958621f24 | -12.71233 | -48.49403 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0022333-d00a-368c-b713-7575e6d3a95e | -6.61179 | -58.97322 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ce066c9-3517-3a45-9c9a-07c49cade4a5 | -12.67401 | -48.51718 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 40504e77-3c8d-3f97-a9a8-adf070c19fdb | -13.65252 | -46.2394 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b85f99c8-15ca-32af-9121-c284301cad31 | -9.48821 | -51.67037 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a2eb2e1-9102-346f-8034-2f95599197fd | -14.49624 | -53.52367 | 2026-08-17 04:57:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07cfbcbf-97d5-3c66-9869-58d90c3770fd | -14.87346 | -46.65173 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efe18487-7ded-335e-bd5d-b44af214e70c | -8.8995 | -60.59047 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b753c33e-ac8a-32fc-b949-b7d5ff04cef5 | -12.0288 | -46.42867 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 451f1cb1-da29-3f8e-91ca-cbf41a969525 | -6.96421 | -59.3008 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54a0099e-d1d5-3e08-a109-4981dcd9ff35 | -11.71023 | -54.60566 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1595fa08-dca1-3495-83de-e812f7a29c6d | -7.40382 | -60.02363 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d13b0df-e216-3800-a716-d89e5e746323 | -7.88423 | -63.75938 | 2026-08-17 04:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3071169a-2ec0-3a32-bd86-eb66e6509d09 | -11.72987 | -54.57338 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da262089-ce31-38df-abdd-fcef0f25b5dc | -6.68715 | -59.07201 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac6ce52d-3d75-3842-acdb-9fcb6ea0a2ae | -15.07607 | -48.71671 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccb39d46-f64a-3da9-b5cf-d79ec582b454 | -11.23183 | -54.01307 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22afab6c-922f-3a5d-bf25-40806fba0d37 | -12.68228 | -48.51368 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 596c7e07-06ab-3dac-acec-6a0a857205f9 | -6.64466 | -58.95698 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 146f4a1b-0cfe-3526-bc06-085d3e373edc | -6.82493 | -56.44771 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e9c8807-8e94-3c6e-a2a4-4f2a53cf6f22 | -6.68512 | -59.07026 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 588a4731-77c5-32ed-9b5c-81f67cda9283 | -12.03718 | -46.49448 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| aa68f2f2-8985-3a2d-9c15-dc94c53b6972 | -11.8795 | -51.95655 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 982c99fd-75ad-3c74-835f-670b644802d0 | -9.47324 | -51.61425 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14d0c4bf-a226-339d-87eb-5bc19179d282 | -15.02798 | -47.03988 | 2026-08-17 04:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61258dcd-f79f-38fa-a748-257434896b3c | -7.38573 | -59.99545 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3236cbb3-3e3a-3c77-8f44-0b427dd185a6 | -9.37193 | -57.35992 | 2026-08-17 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b1eb8fb-36b3-32f3-aba1-f47b186ec91d | -14.47978 | -45.6735 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b94a0aac-7d5d-383f-97c7-28bd84102a09 | -9.48046 | -51.65482 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbefa052-2c91-3fe6-8076-59c283fd1258 | -13.5034 | -46.25145 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a67f4962-c556-307c-a417-ed108a6a5e73 | -8.97458 | -60.53269 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 486cdbb7-7e9d-35fe-9a88-f9c59b9c155d | -6.71703 | -58.9331 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 625664b4-2a13-35e6-9b99-f9f654506255 | -7.81177 | -47.83847 | 2026-08-17 04:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d6252caf-6a8e-3929-a252-27f5ba0abbcb | -9.17787 | -59.67529 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccdbc2ac-55ce-3a24-a4cb-6b4d2b466746 | -10.07402 | -60.50072 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2dbdf15-5464-3b20-9e0c-c5e21a504e22 | -7.59072 | -61.22667 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c0b8c3d-bcc6-3f90-9a93-809e04bb0e27 | -11.84619 | -51.77688 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe66a02-91db-37d3-b854-8e6b6bcd408b | -11.73165 | -54.60543 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e49d62b-ad21-3d7c-a11d-e70356b4ee7a | -6.85883 | -58.96507 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00e102ee-244c-3093-a99b-7255033273c4 | -14.72297 | -52.88803 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d6eb62b-1132-344c-92a4-bef3580f28c9 | -8.50557 | -54.92493 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d48cea2-b45f-3148-b914-68fbcef7e417 | -6.82651 | -56.46284 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbcd2803-8c86-3786-a113-9ec3e3ce2b48 | -12.72841 | -48.46365 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5bfdd494-a7a0-3f73-aaa6-5af695fa8cfc | -12.71273 | -48.51815 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ff11872-6ec1-30ea-9988-f33a5e9f97ef | -6.82469 | -56.45583 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d9ef1cb-41e9-3a48-984f-6bf168399e55 | -6.84884 | -59.10735 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0baedf91-f98d-30dd-935e-66eb44215076 | -11.69853 | -54.61165 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8ae51f-9af0-37bb-adca-c8448851a463 | -13.24897 | -51.68773 | 2026-08-17 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd70d5e3-ba36-321b-8da6-c2f6b9c0da0e | -11.73897 | -54.58287 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbf86bb8-b9bf-3596-86b2-9feab5537053 | -11.45695 | -46.58681 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bd7e3e4-8d08-3992-bedf-b0261bf874e9 | -11.49582 | -46.61655 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 836e9f74-ae57-3e11-bd1d-f4b720bd866f | -12.54818 | -47.85624 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25121881-7615-3c22-a8ff-cd8a6a6d1e1b | -14.18842 | -53.05928 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3031bd44-306c-3b70-a124-3be5d4bb4323 | -8.59894 | -54.69971 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86c582b6-54ba-387f-923c-ffa8e9ef89b8 | -14.38206 | -51.86679 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5334142-3a1b-314f-92f8-81afa0781c3d | -11.31888 | -46.3052 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a19fcd4a-07fd-31a4-889d-1c53c94eb5c8 | -7.37933 | -55.50071 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9613ca84-a22e-3c80-b937-4731b415f4cd | -8.8996 | -60.56123 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce456ab4-6333-391e-bcb4-ae6822521bc1 | -12.03879 | -46.48291 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b46d654-d669-39da-a98e-4581412c7b51 | -11.70763 | -54.62115 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bcfab75-a048-37b6-9bca-ae20baffbe8f | -13.52057 | -46.25875 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 814e54bf-154d-3a61-815c-27bcee1ec757 | -6.62861 | -59.07689 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00543d35-f3e2-39dc-b13a-97d4e75240b5 | -7.29077 | -52.54018 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248f2d0e-d71d-3d5d-acaa-06d9339df09f | -11.2995 | -50.65884 | 2026-08-17 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4067ed24-4684-3898-b83a-5775fbb9ce36 | -14.14618 | -51.74736 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f0d25dc-4f86-3ed0-b85d-10f045c90622 | -10.91559 | -62.76892 | 2026-08-17 04:57:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c272b1d-d799-3d6c-b16a-5a3ea611e12c | -8.90128 | -60.58108 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9abf22f-1097-389f-9959-1f9313a7a467 | -8.97972 | -60.5045 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed66c1bd-69a4-3b19-9e0a-681ed257ef6b | -8.89325 | -60.59585 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8127afea-8e08-3e84-a900-a6a01a981d4d | -8.90598 | -60.55582 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cb1ec7d2-661e-322a-aaf5-78cccc6d28bd | -11.22441 | -54.01561 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8686e997-ff1d-39d6-a29c-4b3c6ee164e2 | -14.37869 | -51.86625 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e540bc51-5d3c-3a1d-a7d1-8102315edcac | -7.42612 | -60.01762 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dfd0fb6-25ce-33b5-98c4-12e2d727980b | -8.97398 | -60.5067 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c45c3696-3ea3-36bf-8b4e-06d71d1ad755 | -8.94525 | -60.51754 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3f873a4-9e15-3041-91eb-6ce83ed3bc3f | -13.63981 | -56.9949 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed29807e-b5a0-350d-8018-3d64582ae84f | -8.64261 | -54.70949 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 136f9ce6-88ff-306f-b3a9-e2a8a22ae54f | -11.71626 | -54.59089 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8aca1e6e-ce05-3bcd-9c10-334fc3bdb703 | -7.38167 | -55.48663 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ee42356-c791-3ae2-a644-f5d8c1e21a42 | -11.21202 | -54.81846 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc172059-1ae1-3ea9-9043-75d5d8686d37 | -6.7752 | -59.46769 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 212fb4c3-4b3a-3135-82ee-a5611f1b166d | -14.30585 | -47.18979 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7e3664a-6062-36ca-8a77-13965fe7390f | -7.39691 | -55.48918 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3b52570-b8d0-35a1-997f-dfd2373856fe | -10.12405 | -52.10208 | 2026-08-17 04:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8d343f2-2183-3781-a5f2-e8b15ec48234 | -12.65698 | -48.50029 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 365bc24c-cffa-3e2e-8a13-1a99f8dfc4a5 | -10.92922 | -57.13454 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 769b9de4-45a7-3ca7-9e05-b669a1c9cc07 | -13.67865 | -46.24792 | 2026-08-17 04:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 505117d7-513b-31a7-a064-a0baee8b7422 | -7.61412 | -60.94587 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README38.md)
