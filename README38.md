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
| be73d90b-c493-34d7-8956-f50aaac0cbdc | -9.32693 | -62.33632 | 2026-08-17 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5cdcc76e-1441-32f7-9cc7-bde97da39b6f | -12.26332 | -45.88122 | 2026-08-17 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac659580-0239-36bc-9c64-1bd216ecec7d | -11.72755 | -54.60867 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b380dc5-ff7b-34b6-bd99-b2d22b21ba17 | -13.51109 | -46.22728 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5573b37-6a60-34a1-aa78-89ca081d3d64 | -12.75891 | -48.43198 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b865e30a-69ca-3241-b8e1-0c39529af062 | -11.71457 | -54.62232 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25c6655e-1fa4-36ee-9fc7-1c1d02b62ef3 | -8.89902 | -60.5937 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fe3e8d5-db68-393c-88d8-d442eb6f7ad8 | -11.7228 | -54.61577 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56c77922-ec69-3b9a-809d-c12616d03ed8 | -8.50845 | -54.90791 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3378715-ae6f-31e1-ace8-589d9c0dc554 | -9.37503 | -62.36699 | 2026-08-17 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e281453d-f0f0-3664-a9b1-00363d997dfe | -12.67847 | -48.51313 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1e37f46-5303-3559-833d-a0623b07d709 | -8.50618 | -47.22018 | 2026-08-17 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fbfd4d0-9d26-310d-824b-f2a1f06efb69 | -11.13328 | -46.50689 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 865606b9-84a0-342d-8089-e1130eeb3806 | -8.95614 | -60.54562 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c460de77-057e-3933-ade4-c1a95fb1cf39 | -8.98438 | -60.53765 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a14e0773-a239-3867-8c47-6c5a9dd70b11 | -7.78345 | -48.27565 | 2026-08-17 04:57:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 441aa3e5-2754-307e-95bc-7396ed09932e | -6.84372 | -56.43598 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95ad6a49-3e87-3d38-bf6e-2d095e62426a | -11.28209 | -45.82002 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a60b8fc1-9f2e-3061-b463-170029fc7a42 | -11.49217 | -46.61197 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72916abf-9d31-3343-9e00-a0197a5f6eb2 | -11.50278 | -46.59738 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f021336b-b27d-3c5c-9f98-46b99dbc9a21 | -7.36407 | -55.49819 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b11bca69-21f6-3ecd-ad84-50b41f4d4f14 | -10.26209 | -50.41784 | 2026-08-17 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21dfd33d-391d-3483-95ff-130f9ec790b7 | -9.47659 | -51.65778 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cdeb8e0f-1b45-34b4-86c1-a3b97868a8ce | -9.30357 | -56.9229 | 2026-08-17 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42376863-bfdd-3e2e-bfa3-c15c45907c69 | -7.50171 | -60.07653 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d5a4e385-c904-3c12-be96-0aab29d8c71f | -10.5018 | -50.40173 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48a23f14-ed26-30ab-8e25-259139691f1e | -6.83902 | -56.43893 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 737c7b08-55c6-3f7d-9ef3-1a6b6bae1d0e | -7.42156 | -60.01353 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed72096b-841a-3cb7-adbb-e9262109357b | -6.7759 | -59.7611 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0152f761-e6fa-3137-b283-d5a046ad2619 | -8.96653 | -60.5182 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b478c89b-1553-301e-b57f-b97e6a49802f | -14.48103 | -51.99434 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72dde571-7923-3356-aa21-dfbaa0db475a | -12.71165 | -48.4987 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16e6e0f1-89a8-34de-9929-a025e37adebe | -8.52657 | -54.88902 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6446478-7b9c-3a36-9c11-9f0bfae3363f | -6.86085 | -58.9819 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40a335c6-6b4b-35c7-8db2-1652c54feaef | -9.48434 | -51.67332 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70fd9ea3-f619-381b-b9e1-dfe4ff804c81 | -8.96423 | -60.53072 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19cba05f-de85-3424-8756-bddc979a5661 | -6.8224 | -56.44432 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d43dd12e-c51c-3747-8f9f-fafc52ed94d9 | -7.36945 | -55.48942 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dcf60d2-74d2-3a90-9c76-47d7be5f9a2e | -9.37052 | -57.3603 | 2026-08-17 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bbe3bd5-ccf9-3dff-a476-b9e891f6f51f | -11.7269 | -54.61252 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f64150b-7c52-334a-820f-a3982d25af9f | -8.9041 | -60.56536 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00cdd193-ec89-342f-ba90-a4f56a371fa5 | -6.99167 | -59.05113 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45ecb09a-ae7c-35ba-b447-22f9bd44ae60 | -12.69777 | -48.48702 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df27ea96-edd0-3683-8f3c-fb94cecc203c | -10.51012 | -50.00285 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7fb8764-18cf-302f-a6e7-62cbf5698485 | -12.72913 | -48.45868 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d821a8c-6170-374c-b9fd-80c057f18754 | -12.02458 | -46.42744 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be90c237-a623-36f6-a30f-29fafeabf87b | -8.90539 | -60.55896 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ffcf773-1e94-385a-bbaa-20aef241c5ec | -8.41889 | -62.67593 | 2026-08-17 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02838691-e7ef-3a37-8aa0-bfd73353360a | -7.40667 | -60.0079 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d56b7bf-1c03-3e86-a285-8e33ed6b8dd9 | -8.67022 | -54.76543 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaea28b3-4eed-3626-a993-3b626ecfe58b | -8.97745 | -60.51695 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033f9887-141c-33de-bda3-5bd841fc709e | -7.56299 | -60.85702 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c10dea70-95ca-3613-a5f5-d7746f5dc4e1 | -14.44695 | -51.83566 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 173e8ae2-d31a-38f1-a5a8-a4e6b65a9dc2 | -14.31861 | -53.05156 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e50b1f4-275a-3e85-9fc1-79337ba9b641 | -11.82953 | -51.7742 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 79c622c9-0583-3a8a-92f5-69391723dd54 | -11.72126 | -54.6036 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 832ab972-60cc-3517-ab05-60ba505483a8 | -8.89485 | -60.55709 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bfb2bad-0c94-3f7f-8072-ab071585d455 | -8.90412 | -60.59454 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 575182b0-5642-3054-8da8-d92a759d887b | -11.49602 | -46.61559 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ee42623-9127-343e-b9e6-b1298e99d2ec | -13.77925 | -53.80938 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f07cfe6f-8533-3c25-942e-b5460fde10a6 | -8.96366 | -60.53387 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 112689bb-1d55-3f0d-a427-9082834f8bb6 | -11.50011 | -46.5853 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 65bfdfc8-f24d-38a9-9f25-4ae7b34336bd | -11.7178 | -54.603 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78231d21-c70c-33f3-b622-bf228ac576cd | -13.75268 | -53.43305 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 061b202e-e14f-3490-bcbb-8e663af586ad | -10.94652 | -57.15315 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a76e4c5a-b23e-351e-8c7d-6acaac74f8b3 | -7.87852 | -63.75755 | 2026-08-17 04:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1248a0d6-0f34-3ef4-9a5b-d47e6f2ac4a0 | -13.63222 | -56.99345 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 38db904a-62e2-3e03-a10f-d17e1124ac8b | -8.63332 | -54.72076 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67721ca1-91e1-3110-8eb9-3d5112f22490 | -7.37698 | -55.5148 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 968065e4-3136-3a9a-befa-59d3f3283862 | -6.69856 | -56.16399 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7200f819-9681-318f-9e01-872c37bb5446 | -10.92801 | -57.13262 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4e8a083-fee9-3c80-bc30-1164a3b3986e | -11.05302 | -47.22588 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19095396-a5ac-33b9-b0f0-36b7abeb2a97 | -9.47269 | -51.61775 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9b1fb83-37c7-32c3-aa76-3b93cd28ba97 | -14.38426 | -53.14664 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10e5de59-9b2e-3210-b1ba-a6b2809b1da3 | -14.3742 | -51.87299 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fc650c6-93ef-3acd-b8bc-ed4a75830ae7 | -6.98775 | -59.04491 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcc44f3b-e654-3b11-bab8-c659345f1e4c | -12.0015 | -46.4678 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf1ce99a-6318-3784-8ad9-b37b8be62b6b | -11.21637 | -54.0219 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35113801-d23a-3d2c-b8e6-3c571cd0da61 | -8.89371 | -60.59264 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1861aaec-ac70-3711-aee7-4546544c4cf3 | -13.51598 | -46.29366 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8463639c-7afb-3317-a62e-60be2dd7aa24 | -8.63623 | -54.72544 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4569164c-e640-3d0e-bec7-811ed82f719f | -11.69788 | -54.61552 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83ddf6da-05e4-338b-8062-8faa6ede53b8 | -6.64371 | -58.96242 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e36d4d17-ce96-317e-9048-fe19926d4e21 | -15.07674 | -48.71862 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3e10549-936b-3d2d-b594-7d5806eae646 | -8.68241 | -54.75893 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d4f70e5-dc6e-3b5b-a6a7-b40511c054c8 | -6.98181 | -59.02169 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c64d3361-2dcc-3087-943a-02d63e697b91 | -10.8984 | -50.27014 | 2026-08-17 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc4fe224-0aea-3930-9691-5dce264784a7 | -11.32083 | -47.00241 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 561f5e0f-d579-338c-b59d-6522118b8969 | -8.07154 | -48.53731 | 2026-08-17 04:57:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dfd6f4c-68cb-33ae-abdd-7f6116bee639 | -11.20213 | -54.81275 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d29f88e-3e75-337c-8f5a-6376ee5c23b3 | -12.74689 | -59.77883 | 2026-08-17 04:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec4ea484-f2f0-34a1-972f-0dc4b18a4cba | -14.49069 | -51.98472 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99f3b0c5-0ffe-38af-986e-fc4771aab286 | -14.47913 | -45.67856 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a20ea0a9-42b1-3339-88f4-d9bced693c19 | -7.38011 | -55.496 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aa23974-61af-32ac-ad5b-ea6495b68aca | -12.736 | -48.46507 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f496445b-ec5d-3923-af12-eaf91e5c8650 | -11.29957 | -54.8775 | 2026-08-17 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 589456f4-31bc-303e-a38f-b9337ab38a2a | -6.59737 | -58.98479 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d00288d0-8991-3571-b73d-e3311483f13e | -6.83028 | -59.09853 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e597a316-de5f-33d3-a737-890aa1585f80 | -12.74826 | -48.42429 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45e9e986-53a5-3e73-a3df-43ce027f77eb | -11.10386 | -47.27641 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
