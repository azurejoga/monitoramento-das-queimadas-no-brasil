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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2bb1af7-0da4-30a7-977b-f303ae394fe5 | -11.7969 | -57.3428 | 2025-06-14 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 02bace04-dbbe-3870-add7-aae947e45a9a | -6.9605 | -42.8816 | 2025-06-14 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 2067721e-3a9c-3cb0-b843-1a04f9c508a6 | -13.887 | -54.6106 | 2025-06-14 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 781178da-5401-3cd1-9245-090bfd7e9f17 | -6.6112 | -43.8941 | 2025-06-14 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9190e2fd-2212-3b4a-86f9-c8ae279f7854 | -12.6236 | -57.8926 | 2025-06-14 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 24643767-5cb5-321b-afaa-d8ca5d25460d | -11.8158 | -57.3413 | 2025-06-14 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 02781977-e5bf-3900-9774-7799ca457299 | -6.9602 | -42.9052 | 2025-06-14 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| a6bb74e4-c260-34e2-915a-8df04bf52e74 | -14.2121 | -57.4098 | 2025-06-14 00:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f2de8b02-1b82-315d-a1d6-418183274b6d | -10.9205 | -54.7795 | 2025-06-14 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| bebbbc3d-f304-366f-88cf-68e20ee322dc | -16.1967 | -46.4589 | 2025-06-14 00:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ff2e812d-1fa6-39a0-98f6-5bcec8e8d419 | -21.452 | -54.5675 | 2025-06-14 00:40:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3d7ea156-15d6-30c7-b64c-f9cba47a677f | -21.4315 | -54.5711 | 2025-06-14 00:40:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 53.4 |
| dfd4c58b-76d6-31c7-99d9-976b498b5063 | -6.9416 | -42.8834 | 2025-06-14 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| c4dd87e3-273a-39ca-acd0-d87057aa6407 | -7.2214 | -43.1153 | 2025-06-14 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 71dbe131-2ced-31f0-86f2-0755916e1f9b | -10.9167 | -56.8336 | 2025-06-14 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c7e63769-d5bd-3d7b-9fff-43c31dc018a7 | -10.9353 | -56.8522 | 2025-06-14 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a54461ad-760a-3117-b40a-7fc47cf3beae | -9.393 | -57.5147 | 2025-06-14 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 78f829e7-0c8a-3e3b-8d0c-915c1941bdcc | -11.011 | -55.0967 | 2025-06-14 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 687c34fa-7163-3704-9e47-87e30d3ea82c | -13.9062 | -54.6084 | 2025-06-14 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f6daaddf-6321-3006-b495-99ecfbffe091 | -7.2403 | -43.1134 | 2025-06-14 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 8f6009ed-9069-3509-a084-079c11925a5f | -10.9355 | -56.8322 | 2025-06-14 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 43a8a63e-ba5e-3a66-9ab7-5c337ca29fe2 | -11.0113 | -55.0764 | 2025-06-14 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c5a5e993-5e34-3ee4-8a8a-7e6a0e43558f | -9.393 | -57.5147 | 2025-06-14 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a89c299d-9b03-30ba-839c-2a325ec3fe30 | -6.9602 | -42.9052 | 2025-06-14 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 802d09ba-d807-32da-ba79-36c006c2ae0e | -10.9353 | -56.8522 | 2025-06-14 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 5661a282-ff1e-32a5-8de7-bc5bf28635b5 | -12.6236 | -57.8926 | 2025-06-14 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 5a050196-0b57-3857-97bc-2957cf909b5e | -7.2403 | -43.1134 | 2025-06-14 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| a14ff4a5-b133-3077-ac9f-e719155b1e61 | -6.9605 | -42.8816 | 2025-06-14 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 2e596f2b-c89e-3a16-ae44-aef4a759c824 | -11.8158 | -57.3413 | 2025-06-14 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fc16eb36-bb39-3cba-9880-363c51a18a36 | -10.9205 | -54.7795 | 2025-06-14 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7b0b119e-f500-358c-a0f9-adcc90b251b4 | -7.2214 | -43.1153 | 2025-06-14 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 9d3a3914-d0aa-3631-b005-eb0e09b8141e | -21.452 | -54.5675 | 2025-06-14 00:50:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e74259c2-f657-35b4-bc40-b462995c6cab | -10.9167 | -56.8336 | 2025-06-14 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 029efacc-029f-3560-8c14-4f851252634c | -13.9062 | -54.6084 | 2025-06-14 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0322a658-2b67-3d90-b513-e6ef39e6904b | -14.2121 | -57.4098 | 2025-06-14 00:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b7f608c2-540e-3a3b-a3e6-6f7c06d69828 | -11.7969 | -57.3428 | 2025-06-14 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| eb0921ab-43dd-3331-9d7a-c2928e6d29ae | -13.887 | -54.6106 | 2025-06-14 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 61d969cf-95b3-3859-a0aa-6e8422139315 | -11.011 | -55.0967 | 2025-06-14 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 76d6e407-6d74-3219-a96a-6bfa21286634 | -16.1967 | -46.4589 | 2025-06-14 00:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| e59a370d-e069-34b9-ada9-7c5fe9c2616d | -11.0113 | -55.0764 | 2025-06-14 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| cac2a86f-00de-3456-9937-4eba118ece52 | -10.9355 | -56.8322 | 2025-06-14 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| b78a80c3-2301-345e-96f0-7f91c31d39ed | -11.4407 | -57.396999 | 2025-06-14 00:51:00 | METOP-B | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a283e04-1fb6-310e-aee8-1f3ff2c287bb | -9.5164 | -61.443001 | 2025-06-14 00:51:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3750479-9aeb-3dd4-b4f3-099dd027da2d | -11.5174 | -54.739498 | 2025-06-14 00:51:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c388a1ad-9177-36f5-b098-a81c3414ca33 | -10.6507 | -55.146198 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53d5e86c-bb5e-3f6b-9223-5b4f042abfa6 | -10.2038 | -52.0695 | 2025-06-14 00:51:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5740c574-fd61-3a70-b93c-2aec2b8227b8 | -9.5142 | -61.432899 | 2025-06-14 00:51:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8642e214-a017-39e0-8422-fa86cc238839 | -11.4391 | -57.3899 | 2025-06-14 00:51:00 | METOP-B | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ffbc01a-81d5-3ea1-8668-4a36f14aff8e | -10.3934 | -54.831902 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8463b70-2cf9-3400-9623-25282a043901 | -17.0163 | -53.878799 | 2025-06-14 00:51:00 | METOP-B | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52f0388a-f8ef-3a80-b41f-24c242e109a9 | -12.2556 | -57.932098 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9852d21d-9b42-3c0d-8b0c-fe41c8f74dd7 | -11.4489 | -57.387699 | 2025-06-14 00:51:00 | METOP-B | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec3c137d-8d7e-349d-adb7-4ae53690de8c | -11.7991 | -56.592899 | 2025-06-14 00:51:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2531f0cd-4415-373f-9eb6-28923789bdf2 | -9.0305 | -57.571899 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f39e35a-1d92-3658-a7f2-9d772dd8d9c1 | -15.8304 | -46.531101 | 2025-06-14 00:51:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e427cf7-49ac-3b50-8ed3-09fda0e82cf8 | -11.916 | -57.313499 | 2025-06-14 00:51:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f45d142a-b189-3dd9-87d9-2dbacca5d43c | -13.5434 | -54.6684 | 2025-06-14 00:51:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d784c13-1341-37cf-a5cd-490f3d2549c5 | -9.7069 | -52.805901 | 2025-06-14 00:51:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb27d76b-8145-3181-a6dc-79561363e6e1 | -10.6377 | -55.134102 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ded5f94f-191a-39c5-a1ac-067de244d558 | -12.3182 | -52.449402 | 2025-06-14 00:51:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fad2997-c451-3ace-9e5e-ece91be19b9a | -12.3203 | -52.458199 | 2025-06-14 00:51:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30662b03-89b3-33c5-808d-0394c09b1c67 | -9.0413 | -48.4851 | 2025-06-14 00:51:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20be9ca8-1736-3956-a96a-0f85af0c017a | -10.5575 | -56.8437 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3a8250-6910-3ae1-b834-5d4ed13ec5dd | -11.4505 | -57.394798 | 2025-06-14 00:51:00 | METOP-B | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 991d837a-8bab-3757-a46b-078dc7cc71f7 | -13.5336 | -54.6707 | 2025-06-14 00:51:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1066a665-ee2b-389b-89f8-0b682ffd90ca | -10.5585 | -54.8321 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4899ebe-ed7b-3959-9b05-655e25d14b58 | -21.0846 | -54.634602 | 2025-06-14 00:51:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 116655de-ce9c-312f-8293-a0db350dc43c | -9.9337 | -57.187801 | 2025-06-14 00:51:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2d49412-b501-3e75-a767-1ce4c7db5f6f | -13.8394 | -57.464699 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33c39a4e-d24c-37ed-8646-36f1cb5cab78 | -9.1033 | -57.901402 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bff838e0-7c8e-33d6-91b7-0845bae45577 | -11.0409 | -55.138901 | 2025-06-14 00:51:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9fe86a3-5ce4-306b-a97e-ee6a7d86702e | -13.532 | -54.663502 | 2025-06-14 00:51:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 442ad735-aa49-37f4-9a88-ec8f4c625f77 | -10.4836 | -53.833099 | 2025-06-14 00:51:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6c2d886-5f7f-3fa6-9588-2ed714541dc6 | -14.307 | -53.446999 | 2025-06-14 00:51:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1885ec8c-ff37-39e7-a544-5f2b7944a837 | -13.846 | -57.447601 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8b1cdd49-7aea-36e7-97b2-54e63c4580ab | -12.2572 | -57.939499 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 874591aa-aee9-33c4-988e-0d57e54c0647 | -10.5002 | -54.351898 | 2025-06-14 00:51:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94e792b4-097d-37f2-a047-2290a8fa7e57 | -13.6669 | -55.171799 | 2025-06-14 00:51:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6fba0694-fe91-359f-8c9d-a7feeec4d9cf | -13.5304 | -54.6563 | 2025-06-14 00:51:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 539a8466-8150-3f56-a6da-048260fb198a | -10.7756 | -53.979698 | 2025-06-14 00:51:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95d513c5-edec-3a22-a0e3-b8a437078433 | -9.9306 | -60.592201 | 2025-06-14 00:51:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e66d94b0-f937-3139-94ef-d34d57d3a5fe | -10.7712 | -54.005299 | 2025-06-14 00:51:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1383fa9d-cc36-39d0-ae64-69d7aa99632e | -12.2539 | -57.924599 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccaeb37f-af1c-39ff-abd6-185ad387f0b0 | -10.5116 | -54.3573 | 2025-06-14 00:51:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebf9eaa-6525-3bf0-9e70-03e70c6952d5 | -9.0207 | -57.5741 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3610fdd1-7f06-33ea-8b91-df5bf075be96 | -11.452 | -57.402 | 2025-06-14 00:51:00 | METOP-B | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01ef7498-a7e4-32e2-a055-57560c443768 | -13.859 | -57.4604 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a4b5ac2-86be-3eb4-9783-6ffb12c31ca3 | -10.0043 | -57.2743 | 2025-06-14 00:51:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01fa3a82-ffe4-3893-a209-90ad09a51cf5 | -9.0316 | -48.487499 | 2025-06-14 00:51:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a769e24d-7697-36b7-91d8-554a488eb87a | -12.1486 | -58.3908 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f817b8b1-bf12-3b39-bb3a-a5e796b228be | -10.5698 | -56.8993 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9f89746-9cb6-3340-8c01-9539fb586f43 | -10.194 | -52.0718 | 2025-06-14 00:51:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62e9383c-62d6-3141-b175-c01773551304 | -15.0252 | -47.934101 | 2025-06-14 00:51:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2f5c81e-1472-30a7-a0e5-5d3a136e70c8 | -18.913601 | -55.203098 | 2025-06-14 00:51:00 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4f13c714-e958-3b84-82c9-debf548ca87c | -9.1017 | -57.894299 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e69f8db3-4176-34bd-b889-76ef053100dd | -9.7048 | -52.796799 | 2025-06-14 00:51:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 667b3673-ffd7-3577-a2f3-d742d9daa687 | -10.6409 | -55.148499 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c13d392c-6ba7-32bc-aaac-36cac1e57a2a | -21.014099 | -48.598999 | 2025-06-14 00:51:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 710917a5-77e9-35b2-a985-856a95324468 | -14.3052 | -53.439301 | 2025-06-14 00:51:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 256d7ef0-0d80-3b11-bcca-3330dd443ddf | -13.7094 | -53.452599 | 2025-06-14 00:51:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
