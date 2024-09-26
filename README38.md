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
| 7c6b0e45-856d-374b-a996-5f4e71449cfc | -10.8976 | -57.467701 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22efbabd-9505-3c0c-a41d-94de58677aa6 | -11.5513 | -60.162498 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be3d7983-3aea-3685-a782-bb4d93891a04 | -11.5532 | -60.170601 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c89a0c2-28d8-39c8-a12c-47064ad3d39a | -11.5932 | -60.339401 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab923347-5986-3cd3-86be-9f0e31005252 | -11.5951 | -60.347401 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45a7af65-b1b4-3b74-8bd4-322b0d95f7d5 | -11.597 | -60.355301 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23853f2c-deb3-3efd-a4f6-8c9f76a090e1 | -11.5988 | -60.3633 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e85c5f8-9e59-3a5a-b7a7-348a7a34b763 | -11.6063 | -60.395 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fda3afb2-6bfb-3e55-af2e-69b3bab2b442 | -11.6082 | -60.402901 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35769109-fd19-32a6-a6d9-e1fdc0c0f474 | -10.8821 | -57.446899 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| faf81c8e-867e-32d1-a29f-f44cd779809b | -10.885 | -57.458599 | 2024-09-26 01:49:23 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1dff50-a355-3550-907b-9851f19a49bf | -11.5396 | -60.156799 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 626e3c86-4475-3daa-a10b-5c479a179f62 | -11.5415 | -60.164902 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b265faf-2564-3e39-abbf-c919acf20099 | -11.589 | -60.3657 | 2024-09-26 01:49:23 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e2526575-c046-32ba-9a76-30b34e7a9aaa | -10.8753 | -57.460999 | 2024-09-26 01:49:24 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd541f9d-5e31-3113-810a-73a5ddc03116 | -10.8782 | -57.472599 | 2024-09-26 01:49:24 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f79d348c-3cc2-3cb1-b465-f0d2b8548949 | -11.5298 | -60.1591 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b246aa17-432a-38e4-95ae-c4b233c6cd6b | -11.5317 | -60.167198 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd19139d-0710-366c-8dfc-b0f5c5619a78 | -11.5793 | -60.368 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e41d0735-51bb-31d6-a447-f671448096a2 | -11.5812 | -60.3759 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 326d29e0-1419-3e42-80fa-5c6ee5e9a0e2 | -11.52 | -60.161499 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16606124-e92c-383e-b00d-e9da06ef9e05 | -11.522 | -60.169601 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 808256b9-466f-3cbf-aa31-2897379d678c | -11.5354 | -60.2262 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 990edd65-9aec-3a50-a4f4-2b2cee904cc4 | -11.5695 | -60.370399 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 735099b0-2e45-3bf3-901b-e83c26b68c88 | -11.274 | -59.176899 | 2024-09-26 01:49:24 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce89acac-742c-3b76-91e8-e3ccafa84063 | -11.5275 | -60.236698 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d1278257-4ac7-342e-83a7-8c8e41273784 | -11.2643 | -59.179298 | 2024-09-26 01:49:24 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 065e18fb-69b1-35cc-933d-8a8c21453142 | -11.5177 | -60.238998 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 129de374-05cd-3c6e-9027-d916d87039d2 | -11.5003 | -60.209099 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1df0e4a3-4a27-30e9-9bb7-68b1b3519fbe | -11.5022 | -60.217201 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2f78d17f-083d-3028-b444-39678c0695e8 | -11.5041 | -60.2253 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 939984a1-01a1-30b3-b951-cddb644bcc6c | -11.506 | -60.233299 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 73f20f43-b492-33d3-b1ec-8c972c95ac8b | -11.5379 | -60.411499 | 2024-09-26 01:49:24 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a331299-a8ca-3433-ab5b-d4c4ccef83fc | -11.9911 | -63.0396 | 2024-09-26 01:49:27 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 72b2a073-6f74-3ad8-abc2-c9e6474ca1d3 | -11.3294 | -60.578201 | 2024-09-26 01:49:28 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a01628a2-bc36-3bd5-af19-368aecd58140 | -11.3312 | -60.585999 | 2024-09-26 01:49:28 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9a571d05-f9ee-3b36-a5b7-4e965737ebb4 | -11.2921 | -60.595299 | 2024-09-26 01:49:29 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3f664f1-4661-3494-bf28-e52bd89017ae | -10.3184 | -56.7593 | 2024-09-26 01:49:30 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58436bc1-581f-33fe-8600-63c7fb0a487f | -10.312 | -56.774899 | 2024-09-26 01:49:30 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9a50b6-d0ba-3a27-9882-413685f8b48f | -10.3152 | -56.787998 | 2024-09-26 01:49:30 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff4fdaa4-d80c-3b0a-9766-08211c50a59d | -11.151 | -60.6539 | 2024-09-26 01:49:32 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa6aab16-a015-3ebe-9632-7156b90606de | -11.1528 | -60.661701 | 2024-09-26 01:49:32 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8af4a9a2-b77b-378b-906d-d56aba03b5b1 | -11.1657 | -60.716099 | 2024-09-26 01:49:32 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7ed7397-109e-3f2a-9bf4-ee8fc8930625 | -11.1675 | -60.7239 | 2024-09-26 01:49:32 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a092477-056e-3f44-a4b1-312ed6e7c820 | -11.1577 | -60.7262 | 2024-09-26 01:49:32 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd2a737-1c01-3dc0-a4fc-5d148742e2eb | -10.3061 | -57.248798 | 2024-09-26 01:49:32 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2427c97b-0700-3295-a8c7-7d1278deabcb | -10.3091 | -57.261002 | 2024-09-26 01:49:32 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffb0269c-f9e1-3c67-97b0-46759cde18b1 | -10.2964 | -57.251202 | 2024-09-26 01:49:32 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 928d866e-4ff4-3589-9dca-a2ff1bf05296 | -10.2994 | -57.263401 | 2024-09-26 01:49:32 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e8f52d6-2d72-37e6-9d35-9e75d41154c6 | -10.3025 | -57.2757 | 2024-09-26 01:49:32 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1ebd39e-2ae6-3f77-b622-33587c6af201 | -10.3973 | -58.884102 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7ad2ef4-aa64-3451-97b9-0b69a1d88cb6 | -10.3875 | -58.886501 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccfc5ba9-2000-3351-a349-53c41833898c | -10.3899 | -58.896198 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26a5c1d6-57fa-38cc-817e-08a0ed908516 | -10.3777 | -58.888901 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7767c793-83b9-336a-adfe-95b8b6fedfa4 | -10.3801 | -58.898602 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f64ad539-b871-3e77-9fcb-047dadf26b12 | -10.3824 | -58.908298 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4680335c-cdd6-39b0-bf9e-3361b8d54a1b | -9.9169 | -57.054001 | 2024-09-26 01:49:37 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7cac42f-7052-3638-a3c7-29d83028b93d | -10.368 | -58.8913 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f83e689-c607-3ef9-a5e5-faf13495284d | -10.3704 | -58.901001 | 2024-09-26 01:49:37 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5eeb1cd9-ee02-3270-99e9-b1f1b466d9df | -9.904 | -57.043598 | 2024-09-26 01:49:38 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcc23c22-f2d8-330c-9e4c-28f3fb7ba256 | -9.9072 | -57.0564 | 2024-09-26 01:49:38 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9015b9-4538-31b3-ba80-677aa927f87b | -9.9103 | -57.069199 | 2024-09-26 01:49:38 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20049ef7-807f-3ff5-8fda-86706c961fc2 | -10.3582 | -58.8937 | 2024-09-26 01:49:38 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe7965a-d4ff-3a2e-b93e-24d839c6b12b | -10.3606 | -58.9034 | 2024-09-26 01:49:38 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d91e56bc-c619-3416-b3eb-59c8cccd2cdc | -10.7366 | -60.736301 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec17cfb6-3490-33c4-8872-1d709ac10c11 | -10.7385 | -60.744099 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0245194-a8ea-3da5-acd9-f5b839200573 | -10.7306 | -60.7542 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f266303-7a43-3f43-a86b-550e87b9bee6 | -10.7116 | -60.717499 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f628b25-6612-3cd0-b9c5-e21ab6df76c0 | -10.7135 | -60.7253 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0bc0423-5c36-3d03-a0fd-2081c9efac9c | -10.719 | -60.748699 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 909a7f2b-9777-3e3c-adeb-928a2d46f919 | -10.6975 | -60.745602 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 276515f3-65ca-34eb-a5fc-df92305c614c | -10.6841 | -60.7323 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89a9fb8d-9cc3-3214-85c9-94de312e9480 | -10.6859 | -60.740101 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d543deb-5587-3090-a8c0-dd39e245ad53 | -10.6877 | -60.747898 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| baf2a07b-cad5-34ab-83ff-4fd93011e817 | -10.6896 | -60.755699 | 2024-09-26 01:49:39 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0bda82-7d9a-3a0c-b671-fb80d0c1c068 | -10.678 | -60.750198 | 2024-09-26 01:49:40 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7d8176-0ffe-3db3-bb53-3c6a27a38aa3 | -10.6799 | -60.757999 | 2024-09-26 01:49:40 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7b92900-b5c6-3a98-bad2-08e64aab887a | -10.6701 | -60.760399 | 2024-09-26 01:49:40 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 056f7eac-a7ba-3f2c-8a46-00dcba815e7d | -9.7025 | -57.188801 | 2024-09-26 01:49:41 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e19bf319-979e-3928-a039-3dbc0f312f99 | -9.7056 | -57.201401 | 2024-09-26 01:49:41 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71199e41-f348-35c9-8298-ac7a9b953fc7 | -9.6928 | -57.1912 | 2024-09-26 01:49:42 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cac07194-b6da-3531-8b31-3e3a257b1617 | -9.6959 | -57.2038 | 2024-09-26 01:49:42 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53c04309-1204-32e6-9f50-1ef1b8ed5a87 | -9.7649 | -57.7756 | 2024-09-26 01:49:43 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 928adf40-689c-353b-be66-218b848b51c7 | -9.7677 | -57.787201 | 2024-09-26 01:49:43 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8bf8be5-7c94-3978-9b07-24a0d09e12e9 | -9.6201 | -57.774601 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75cf3d3d-3146-3afc-84c5-28aaff66ef73 | -9.6926 | -58.069698 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e474ffa-c457-3f26-9f14-8008f9e0c021 | -9.6953 | -58.080799 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d41831a4-4d33-399b-b22e-eeec19c072a7 | -9.698 | -58.091801 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0aba466-7798-354f-bb4b-f9cd7fb3f61d | -9.3819 | -56.853901 | 2024-09-26 01:49:45 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c87fa861-7e6f-34b4-9122-a87e6a05b6d0 | -9.3722 | -56.8564 | 2024-09-26 01:49:45 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 990e1311-13fa-3a95-bdb6-ea39734eb596 | -9.4047 | -56.862499 | 2024-09-26 01:49:45 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdecf93a-dd40-39bb-88d5-5972bc502f8f | -9.627 | -57.760601 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d31e2d90-4849-3e71-92b4-500b90a7cbd9 | -9.6299 | -57.772202 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c632a6f3-0ebf-3b02-a261-7f925daccf8e | -9.5619 | -57.538101 | 2024-09-26 01:49:45 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2742c92-d3ae-3a9c-b34b-0d9a07b43b74 | -9.6144 | -57.7514 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f08a648f-9b99-3fda-8a62-8694c6e1957a | -9.6173 | -57.763 | 2024-09-26 01:49:45 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51fa9ea1-b610-3970-b93e-d4d79edc48fd | -11.2659 | -65.2798 | 2024-09-26 01:49:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2331037-d1bd-3a54-9803-ac84cb46f5a0 | -11.2676 | -65.287399 | 2024-09-26 01:49:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb75633-41e0-303a-8599-593182061fb8 | -9.6648 | -58.420799 | 2024-09-26 01:49:47 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0860a36a-d11e-331d-81cc-b531eb011662 | -9.6674 | -58.4314 | 2024-09-26 01:49:47 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README39.md)
