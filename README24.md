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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a2044f6-b1c5-3f1c-ac3f-ce60edf0cbb9 | -14.953 | -47.51706 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3910ef0a-87a2-375e-aa21-7f538e835a9f | -11.08626 | -47.80333 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4115c3f-e3b7-38c2-a0d2-06ed99720ff2 | -14.2949 | -45.8862 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0a60a91-c2a8-3aa2-867e-929a6a272f1b | -13.13102 | -47.89217 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0fb2e48b-3b88-3ef7-b960-1bd7192dd7df | -13.31001 | -47.57789 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 139e529a-6025-31c3-8f17-e49ac4f34ed4 | -14.89689 | -48.29453 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47544dc4-67fc-3381-b8e6-1df328198e4b | -15.31924 | -46.3816 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cda1c49-84d6-37bb-aa46-7aa5708a825b | -14.93985 | -46.8957 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3fe990c7-024c-30ab-8d3e-2a640f084d1d | -10.22685 | -43.02689 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7638a653-5f9f-32f2-8a28-b43d297c2094 | -12.9082 | -46.91383 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4da39735-918f-319c-a41f-aa5dc892fd4d | -13.47394 | -47.2345 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54aaf93d-66c0-39c8-ae1e-2301297776b8 | -11.62774 | -47.98617 | 2025-10-03 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7675f6bc-440b-397e-a813-acd840effaaf | -14.9024 | -46.97101 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efdff356-b119-38d9-8c31-4b1ff280ccd1 | -11.81443 | -45.02525 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c5c6cbe-a8d5-3608-8730-d380afee3c9e | -11.59623 | -47.66629 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c3e3e03-6df4-3ace-b9ee-a5740a9b4603 | -13.31077 | -47.81182 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b4dab32-116c-3b2a-907f-317b250fd0cc | -14.90367 | -46.96465 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8cc542b0-346a-3cc2-a75a-1e5ac4e4f4b3 | -14.89495 | -46.84129 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86c9cd24-847a-363c-9496-cfe30269d9d8 | -12.68099 | -46.85725 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e557ef33-1426-3690-a9f0-0cca7b3df010 | -11.46416 | -44.9606 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf3d5edd-e7e1-3114-801e-fea9b956d8ae | -13.12566 | -47.8587 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e5b057c-4e00-3cea-8eeb-7c79e25a284e | -13.24041 | -47.3505 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef634063-1da9-3664-9da1-b554cda883ff | -11.90156 | -46.31503 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7b4ca49-784e-322c-8f0c-7801b88c7f2c | -9.76711 | -46.22049 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a63d4396-e3d5-32c6-a635-4327e1bb2a86 | -13.74456 | -47.99012 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9d55473-7a37-399a-ad7f-3d71e3cad654 | -14.62579 | -48.23956 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29452a16-cd4e-35db-a1fb-e24f2ee6c386 | -9.90191 | -43.71708 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 7fb0cdb9-7a25-34e2-a9a9-9def98ae5c7f | -15.30473 | -46.28398 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abb62bfb-b5b4-30b7-b795-c53ac353482e | -11.05525 | -47.79818 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2cd2561-d029-3976-b153-adc7b9aa4b8c | -13.5425 | -47.28793 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca52a7ff-3650-3c44-92d9-2b4ed494e4ac | -13.6678 | -47.3059 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e240e11e-3dc7-3911-99fd-e794a5730695 | -12.80975 | -46.86345 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac497bc1-23a5-306d-bec0-b44b390c0596 | -11.91951 | -46.28032 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 74ae0135-765d-3d71-8d24-e401a07a4af1 | -13.55993 | -47.30173 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9aada4c7-0c31-338d-9918-5206e7d77423 | -14.29612 | -45.921 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 212c35c0-c8cb-357d-8b93-3960f491adba | -14.43909 | -46.37665 | 2025-10-03 03:45:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1ce78f4-c145-3981-87ae-4d51745fd5df | -12.1101 | -43.43996 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebcee00e-7e86-38ae-a398-eb505568608c | -11.83572 | -45.04484 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 908e1416-5352-3461-b1c1-d42ef52c22ed | -12.93541 | -48.43567 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b151e238-d4fe-36ef-a009-acb83089c8c2 | -14.87559 | -48.30837 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1b381cb0-f27b-34f9-9f93-cb8843dfd8a2 | -8.79498 | -46.67583 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| baa1929d-f976-395b-a9f4-4c2503ad6e7a | -11.49068 | -45.01457 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02103d44-cf64-38a1-a9b9-4337ba092126 | -14.94493 | -46.89824 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2d1123ab-565f-3218-a544-bbebc077cc9e | -12.74969 | -44.91534 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2dc5987-1ced-3bbf-b956-4da3988a2e95 | -10.76425 | -45.33512 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1867319d-40fd-3970-b5e8-fcc539de319b | -11.47269 | -45.02676 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 025c9f46-eaf0-34ed-9a91-e1bfa3b33f5a | -12.90591 | -46.89634 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d8e9935-3f34-365c-9b42-08a5df8e3615 | -13.24426 | -47.3009 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b77ffd4c-60b5-399a-920b-4989b2b89247 | -12.92894 | -48.4361 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c9e7940-1b81-30f5-ab2a-d6c9bc0847a4 | -11.82448 | -44.91572 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ca29ec4-f0aa-3022-b670-56284d78caff | -9.76306 | -46.22724 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efa2350e-7a8a-3db9-af24-778c753b16a8 | -13.32839 | -47.60571 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e5b85b0-a41e-3387-aa93-68750c10243d | -8.80838 | -46.66944 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c45eb396-3665-388a-9e2c-1b0a8db215dc | -11.1332 | -43.37755 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ea1992d8-7762-3ad0-b36f-3b42baaa2dbf | -12.196 | -47.78771 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6fc42a6a-e5c8-348e-b170-eb6200b4bd72 | -9.94266 | -43.57664 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37277cce-a01b-32f1-b10d-1652dacaf62f | -11.8138 | -45.02863 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63c40481-974a-3946-98ea-728870584c17 | -14.29082 | -45.89434 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a89e0ad-952f-3510-a351-fcff0c048d32 | -14.35698 | -43.85492 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 647eac25-3a20-3b94-8e12-28561bdf8e03 | -14.93857 | -46.90211 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf09d072-df5b-3039-9f53-6f4094de0055 | -14.62945 | -48.13398 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d34ce9d6-e521-37d7-84fd-cd877a1d737f | -13.15971 | -47.90216 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f29e412-19fa-3b54-9ba6-532778bcce33 | -10.88517 | -44.27442 | 2025-10-03 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb3794b1-9977-3ab2-82d6-3ac3ef0f173a | -13.31008 | -47.24841 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4c9c1c08-4843-38b2-a088-c4130a45288c | -11.42944 | -43.49149 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a89d7f2-343b-39a6-9620-12b116b768df | -11.88237 | -45.01899 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41bab802-45c4-3cbd-a0e4-c2ad77c00319 | -10.88715 | -46.72008 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 29f7cf66-58a6-36f4-908f-329524666c0b | -14.74486 | -48.12968 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fcc1024-e3cb-39ac-9508-860a6896b136 | -11.14506 | -47.18364 | 2025-10-03 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa0bfbe3-4fbf-35a4-b0f2-830749f186e8 | -11.86061 | -44.96951 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47683793-2ef9-3164-8aa5-a68d7bfd0941 | -14.21528 | -44.94714 | 2025-10-03 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80bb509c-4801-3226-9200-a523050b9020 | -15.32812 | -46.3909 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bc5101a-8962-31ce-886b-12d219388f4c | -11.23432 | -48.20179 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4129e5dd-a90c-35c8-9eb2-5b9afb6e22a7 | -14.74031 | -48.12241 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a56fce0-fa27-3b2b-b95b-6f1c5072402c | -15.94393 | -43.34443 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58884580-5ef5-393d-8e37-2bf7a7f95291 | -11.9041 | -46.74416 | 2025-10-03 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 253c679c-f67d-3519-a6e5-b50c86331554 | -11.23328 | -48.20691 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 37cab7f7-9d68-37bf-9c5c-cff4af958b19 | -10.82326 | -41.26358 | 2025-10-03 03:45:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 33aa62bd-0551-31f1-bc00-c898eb72e8ce | -11.46914 | -44.96189 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3250c017-f8f6-3a8a-a48c-cb80ca76268c | -13.19927 | -47.88882 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ffb62c6-53f7-372a-ba41-5dbd86617e2c | -11.84687 | -44.96253 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b169f962-8416-3d71-9958-8c50c09baa20 | -12.90404 | -46.93452 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daeb5752-5e31-3c17-bdcd-6599ab7992b5 | -14.38029 | -45.93888 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b24ac6f4-28a9-34a8-aa0d-aa4f9c48a7b9 | -12.64938 | -46.87061 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f08440c-fae6-32c2-ad5e-ef47299dae59 | -11.80811 | -45.03121 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b812cbc-557a-3bc4-a7ae-9d5ceb79ca2c | -14.43539 | -46.11868 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b69d5eec-6163-3308-9f4d-9d3146de090e | -14.6992 | -43.8879 | 2025-10-03 03:45:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 9d4d41f9-07fa-38c0-883f-9ec2b584b316 | -11.91444 | -46.2772 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8ab83df4-844f-3f24-b4e9-0d65e9402111 | -13.12265 | -47.87321 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d62a6cb7-b0c3-3da2-901e-049e39ec31d4 | -11.90431 | -46.30062 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1579ec8-ccb4-3666-86be-efc8aad61c81 | -12.62496 | -46.96535 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 359bccec-119c-39bc-a596-c24994076261 | -11.81239 | -44.89743 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b8ad908-ce38-3f4e-9a95-e7a088221711 | -11.11945 | -47.85888 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62292634-2975-3544-acfe-5e17674390ca | -14.64843 | -48.24853 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 397b293e-f3bf-3911-9e32-b783ca16c563 | -10.24639 | -44.94636 | 2025-10-03 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdd5ca8b-82ef-356c-b9f5-5ad4f22666f5 | -13.12343 | -47.87996 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 01b2be03-4e9f-3408-a566-9bf823ad2a16 | -14.3555 | -46.13594 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5298cc39-9777-3594-8ab8-38ee54325d89 | -14.60086 | -46.70926 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2730fc6-5d4d-3842-a72a-fe06df7999c6 | -15.31291 | -46.27992 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4840f89-a6dd-3eba-92fb-bf7f34b2bef4 | -13.24003 | -47.303 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README25.md)
