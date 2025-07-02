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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09a9e2ae-cbca-3e37-b673-b340d4ed861a | -10.88653 | -56.44736 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 66b925cd-e28e-3990-8912-46acf43b22ca | -9.24505 | -58.74549 | 2025-07-02 04:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 158524f6-8b4e-354e-883b-5f7fd5ffba27 | -11.84024 | -43.80086 | 2025-07-02 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d88fd322-1dda-3211-8079-64cfb75741ab | -10.9292 | -57.12935 | 2025-07-02 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7faf296f-f8d8-3f40-bc54-f64c25b2d9d9 | -10.94611 | -54.37004 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecbce9bf-5bc5-3377-b895-ce4a24562c40 | -9.24213 | -50.04018 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6cb6f50-181a-37cd-8de5-fd775fee0b5f | -11.14556 | -43.33075 | 2025-07-02 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ac61a5d9-f0b8-3df6-89b2-f4ef8e77b4db | -10.87518 | -53.75542 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a469d13-1d61-3196-8362-bce4210bfa62 | -11.58135 | -54.56807 | 2025-07-02 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f6d321f-ad38-3fcc-a0d1-7195b7391d9e | -9.04598 | -63.99036 | 2025-07-02 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 994c5f9c-1db6-31af-9a86-908089ab9000 | -10.86576 | -53.77189 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a0018e2-3c64-3a37-b8e0-46435335ff61 | -9.85477 | -44.70105 | 2025-07-02 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aeabbe4-eb61-303c-841d-91d9984d39f4 | -9.95634 | -54.17277 | 2025-07-02 04:53:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0ab114f-4518-3259-9807-3525bd15c592 | -9.24787 | -58.75378 | 2025-07-02 04:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28234994-59a7-39ea-91d1-51d506893094 | -7.91525 | -61.55762 | 2025-07-02 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6542cc1e-f552-3ee6-b1d9-b03bda1f2df7 | -10.51051 | -49.78964 | 2025-07-02 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db60834d-fc59-38e5-bf85-4dbbcf219903 | -10.30065 | -57.13559 | 2025-07-02 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfbe9035-408b-3555-94b8-78905a5eaec6 | -9.57352 | -49.10689 | 2025-07-02 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b7cb6db-363c-3509-8c7c-976113b120ee | -7.91471 | -61.56061 | 2025-07-02 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a6bd57c-bdfc-3769-b670-57b551facfc8 | -11.13977 | -43.32996 | 2025-07-02 04:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 44b332b6-f5d8-336e-bd54-02ab25c9dd0e | -10.88183 | -53.7565 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37006b2b-b699-3b33-9c88-13243eba3af3 | -11.23729 | -49.48899 | 2025-07-02 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4870d86c-f587-332a-8a32-4f2a0089e645 | -10.88231 | -56.45083 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2730e4e0-b3d6-3f1b-a696-16511790ff34 | -9.24151 | -50.04442 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce6c20f8-093b-3f94-b49b-6f99d2db69f8 | -9.79362 | -47.74561 | 2025-07-02 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9520cbce-b68c-3e25-8173-8e40a4ff17d0 | -9.34371 | -58.84761 | 2025-07-02 04:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ab1e1ae-1fd7-3b78-a832-d32122dc25ee | -11.83976 | -43.80474 | 2025-07-02 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd3c837f-2d08-3c5b-94c3-7fded3645145 | -10.88941 | -56.45205 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 811697cd-a73a-364e-8f58-abc37f70120e | -10.24502 | -47.68002 | 2025-07-02 04:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e0330b3-dcd5-3269-b06b-83285212b663 | -10.04197 | -59.36016 | 2025-07-02 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0147928d-b26f-3250-8bd8-a3322e45b031 | -9.22758 | -50.03798 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8515079-9b8f-3004-893c-8f03057ad09f | -10.81726 | -56.95419 | 2025-07-02 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2317a2a-bbc9-3147-9212-358f0c67e63d | -9.23672 | -50.02635 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c66c0118-01a3-3b84-9f11-2c51e797d30f | -10.99266 | -49.38332 | 2025-07-02 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd3aec17-ec7e-3876-84de-23e9cb3dfadf | -10.51118 | -49.78512 | 2025-07-02 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eae62d49-8aa7-3b07-acc2-ea86c7e2b485 | -9.57272 | -49.10395 | 2025-07-02 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 45ec2227-e573-373e-b41c-b29f6b1df75f | -9.63493 | -61.47137 | 2025-07-02 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b6db8d2-295c-349b-a055-ecc8471e7da3 | -11.23549 | -49.49187 | 2025-07-02 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0505b3af-90ec-3e13-95fb-a1f9f6778fb7 | -9.27652 | -57.82523 | 2025-07-02 04:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70de5379-5270-33a9-a3a2-5ff512646289 | -9.79782 | -47.74627 | 2025-07-02 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9041dfe1-effa-3456-8f68-c6b812bec2c1 | -8.0453 | -55.0815 | 2025-07-02 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4b2baa4-3c5b-33e8-9fdd-3d7b8f97e8f9 | -11.3295 | -51.44367 | 2025-07-02 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 010a712c-136d-3d82-b024-bc32a3a2ebba | -10.8652 | -53.77541 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00aa9760-30db-3f1d-9e59-6ac82718f307 | -9.95968 | -54.17332 | 2025-07-02 04:53:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79bf4826-12b6-3592-9db2-71469549cde0 | -9.23122 | -50.03853 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d05f2c2-8dba-39bd-a1ee-72e891e1f88b | -9.25069 | -58.76208 | 2025-07-02 04:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3518b7d0-4e56-373b-866c-7eb3bbf7ec04 | -9.5742 | -49.10209 | 2025-07-02 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aeb35eba-5fd8-3bec-91dd-9861d118b1b5 | -11.57468 | -54.56697 | 2025-07-02 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfdb4fb7-882c-3926-b2f7-4573cc46f931 | -11.24047 | -49.49434 | 2025-07-02 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f896a64c-f647-346e-b3a7-2d8dc8510496 | -9.24919 | -58.74625 | 2025-07-02 04:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dcdabd0-f092-342f-97ea-4d037547677a | -10.50668 | -53.58436 | 2025-07-02 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a468a8e5-fa74-3d3c-9442-891e1a138f49 | -10.29845 | -57.12613 | 2025-07-02 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e05542dd-6a7d-3c1c-b0a7-612d1d32e585 | -9.2282 | -50.03374 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b42fcde-0812-39b4-948e-59108d17c2da | -9.23849 | -50.03963 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9545e979-c559-371e-b276-5e5c188ff3b3 | -11.32441 | -48.68055 | 2025-07-02 04:53:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe16d7d6-b3a2-323f-b265-014dff392822 | -11.23933 | -49.49244 | 2025-07-02 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1196c1f7-1cda-330c-bdf8-7337b989aaec | -9.23548 | -50.03484 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c3e04cc-b7ab-34df-9f9a-17bdbaddf410 | -9.2555 | -58.75903 | 2025-07-02 04:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5816215-a472-3673-8815-f45100dcd4a2 | -10.68635 | -47.20671 | 2025-07-02 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ad04417-5bd0-384c-b14a-6e79becfde5a | -10.89162 | -56.46075 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44b53d3b-bc3f-35a2-ad72-7b92aead0a04 | -10.30435 | -57.13626 | 2025-07-02 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12718f32-7157-31ee-8ec8-7902f0a1a459 | -9.70588 | -56.18368 | 2025-07-02 04:53:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a672c0f-0d39-3d56-9c3c-5656a7393b75 | -10.86409 | -53.78242 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b20d606-e4ec-39c8-a8d9-a3a2f8d4b6f9 | -10.87574 | -53.75191 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 020af25b-1403-3078-b2cb-96b2ff41d701 | -11.33299 | -51.44421 | 2025-07-02 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ec7f810-49bf-358e-9799-5e7108e2fc12 | -11.24114 | -49.48955 | 2025-07-02 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66851bd5-5ef0-3ba4-9901-ca4e35832845 | -10.89008 | -56.448 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5549d5f9-ee0e-35bf-a734-1b777290b179 | -10.92554 | -57.12868 | 2025-07-02 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b2187cc-50bc-30a2-b628-98cc6ed943a9 | -10.8785 | -53.75595 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d328365-f84c-375c-8c48-2243ccfa9ec3 | -9.79254 | -47.75331 | 2025-07-02 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c78871ef-25ae-3fa7-8f70-70fd4c9c3602 | -11.7489 | -54.72388 | 2025-07-02 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce2ebe92-3bf7-3be7-81d1-62b070fc8ef7 | -9.24853 | -58.75001 | 2025-07-02 04:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d9793c0-92a4-36f3-aab6-af5698caae8a | -10.29621 | -57.13936 | 2025-07-02 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b1971a3-7cab-3375-8020-bbc0ba3b298d | -10.89363 | -56.44865 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| acce54ec-43fc-301c-a88e-db999fb93c65 | -10.86188 | -53.77487 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5dad5bc-26b7-30cb-a6cf-186fd81d1221 | -10.94657 | -55.31496 | 2025-07-02 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 133abb7d-f45f-3f9d-a0bf-1d9327dd8908 | -9.84959 | -44.70026 | 2025-07-02 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2d9b29e-ba8f-3a14-9c5a-058e84a95da3 | -10.88127 | -53.76001 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e818b21-fa1f-39c4-990b-80c69ed44710 | -7.79353 | -44.02712 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d80eb5d-47d8-3512-8530-51f799f0a1df | -8.8999 | -48.33406 | 2025-07-02 04:53:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b378fce4-ae5d-3df4-9288-cb86f358d349 | -7.30821 | -55.30547 | 2025-07-02 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d92fd51-4057-39e3-8888-2ebee8024957 | -7.78432 | -44.01591 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfa5c8fc-2196-331b-953a-48ebd9c15b90 | -7.79487 | -44.01743 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a8803403-093f-396d-9a92-84d6af88e5ba | -6.70973 | -51.4139 | 2025-07-02 04:53:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eec06423-4c41-3aa8-9864-70bcabd2b42e | -7.81462 | -44.03023 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 649b07ed-fba8-358e-befa-c38787291866 | -7.78825 | -44.02634 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60ec135a-0325-3cbf-8d34-083b4f34298f | -7.09314 | -44.38057 | 2025-07-02 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad8436fc-5b5f-3db5-affe-0fdf773e0afe | -7.80869 | -44.02913 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ba4b455f-5131-3b7e-9a11-dcaca9d509b8 | -7.79925 | -44.02467 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72f213e8-afe3-37be-99f5-8b19bfaaefa8 | -7.81968 | -44.02744 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2ae6bc2-e2a9-3c31-9235-30ad323a7313 | -7.08803 | -44.37992 | 2025-07-02 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bdcafa04-417f-3692-b89d-c490b1e26a35 | -6.70636 | -51.41338 | 2025-07-02 04:53:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6178c60-c98a-3957-b417-4e9ec20f71ed | -7.66892 | -44.66093 | 2025-07-02 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbaf9195-cfca-3e1e-a202-04ae5b9a57e9 | -7.8144 | -44.02665 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 057a7043-5689-3fb4-a74c-649cc733b287 | -7.8006 | -44.01495 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 93ec0d3b-9d9f-3c64-9517-82cc3e39565c | -6.89921 | -52.19236 | 2025-07-02 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df15d62c-d85e-3c57-9e7e-544d69687549 | -7.7997 | -44.02143 | 2025-07-02 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e48ae9a3-a9f8-3242-b02a-7e50c533a16d | -7.61199 | -45.73695 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24f384ad-c7bc-31c2-8220-68b7d8e6eb35 | -6.54069 | -55.02946 | 2025-07-02 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c800f657-0022-353d-a56c-da8e572b64bd | -7.60664 | -45.74108 | 2025-07-02 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README15.md)
