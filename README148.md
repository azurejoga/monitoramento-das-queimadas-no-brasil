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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e4aa5cd-596d-3708-9894-0c7ff917d64c | -10.65973 | -50.91562 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b88b5573-97fd-30b1-aa27-08306bd4e586 | -10.65916 | -50.91916 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2ec6987-39fe-3eef-9568-8a663ea872dd | -10.65582 | -50.91861 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7f48129-0bfd-346c-99cd-376ddf60b3b1 | -10.65249 | -50.91807 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1887bf5-9d8b-388c-bd41-8065dd72cba6 | -10.65192 | -50.9216 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d842c30-8e1a-3e80-b73d-89fa943975df | -10.64859 | -50.92106 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e6083a3-0a01-3b08-9a89-b55ffd8045dd | -10.64566 | -63.9767 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6be04a01-ff11-32b2-aedf-04bec811ed6c | -10.64525 | -50.92052 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e6b2f9a-e3eb-3561-ac1e-2030da663262 | -10.63709 | -55.89527 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1510feeb-e152-3298-b646-a60f916c38a6 | -10.63358 | -55.89064 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f884c0ac-7e9a-3c16-9cb3-2ce0bcb3ea98 | -10.6329 | -55.89454 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a555994-41bd-3c41-94ce-4d878252e45a | -10.63222 | -55.89844 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c914d94a-4fef-3b34-81a8-bbfb83e9ae63 | -10.63155 | -55.90234 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e1487db-40e6-3968-b974-30032550906f | -10.63087 | -55.9062 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 794d3e18-64fd-3086-8dce-61613a01d37b | -10.63021 | -55.91004 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c75aaec3-d917-3199-93ba-4aa32657cb11 | -10.63009 | -55.88592 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1586409b-d899-3531-bbdf-5c7859a91175 | -10.62954 | -55.91386 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73dd5c95-1688-3e74-95a8-eb63afbbdab8 | -10.62941 | -55.88983 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3345d203-edef-3748-8d78-515d763d173b | -10.62887 | -55.9177 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62e7c33c-4300-32a5-97ed-64d404cdd8f7 | -10.62872 | -55.8938 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0a9eabaf-d5f6-3244-8ee0-74046fc7e274 | -10.6282 | -55.92157 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 485703a0-a412-359f-a4b7-bf0e1256b7b7 | -10.62803 | -55.89773 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85480798-3f8f-3742-b199-bec414bea4c8 | -10.62736 | -55.90162 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2b1147b-d8e9-3dc4-a0ec-c8ce94180f88 | -10.62668 | -55.90548 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c3a5934-a724-350e-bcbf-f112858c7828 | -10.62601 | -55.90931 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7885df9b-1b3a-38d5-b6d9-19bd1806ed0a | -10.6259 | -55.88522 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c54b4417-169c-3de7-9dab-385a3325401f | -10.62534 | -55.91316 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f87b619b-5765-327a-899b-6b201185d68f | -10.62521 | -55.88915 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9eb415bc-496a-3e3e-9d3f-181907565771 | -10.62467 | -55.91701 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd191969-557a-303c-a0c7-b7c6b32a2fb9 | -10.62453 | -55.89309 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9331da5a-f860-3ece-9ef2-f49d84117dce | -10.624 | -55.92085 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 57c31fc7-4c47-3de5-a1e3-23f322d68221 | -10.62384 | -55.897 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 647e1d46-1ee6-33cb-b2dc-35d69f6774ec | -10.62333 | -55.92471 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4031ff13-5630-3d86-b6fb-ab50cf72d942 | -10.62317 | -55.90087 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d9c8e55-9039-3b4e-b0ac-99ca85da747f | -10.62265 | -55.92857 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0cdd08e9-f3d2-3faa-8de1-7464e3d3c7db | -10.6225 | -55.90472 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd3f0326-3bef-3119-a1df-a7482e2dfa7c | -10.62182 | -55.90858 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6bd4085e-8a0b-317a-89d6-475a4279ed0f | -10.62047 | -55.91629 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7751c61-9447-323c-84b4-a40bab31048b | -10.62005 | -53.67467 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e4728e0-e9ec-36d6-9c92-1c14301519b6 | -10.6198 | -55.92012 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| dc53aa3d-b76b-3124-aa2f-57b5cd5f14f1 | -10.61964 | -53.67274 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a54c1204-5822-3a9a-b78a-6be46f3a7d65 | -10.61934 | -53.679 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e57f6f9f-816f-3109-a3bb-cf89998d7c83 | -10.61913 | -55.92396 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 026b89c9-f173-3a2d-91e4-6cac7de3e0ed | -10.61903 | -64.43477 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c72d76e9-f7cf-33f1-94cd-ca2bce01673a | -10.6189 | -53.67707 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11ced27f-5a61-37cf-ae14-fd99545195b9 | -10.61863 | -54.24427 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e4e5483-69eb-3cf2-b2a1-10c0458f824d | -10.6185 | -50.9236 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56ee780c-ba39-3af8-a2c5-231cc65a45a3 | -10.61846 | -55.92782 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f68f2068-a9b3-3d8b-b2f7-deb4b6fb6913 | -10.61775 | -54.60909 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51094a90-6ef8-316d-8afa-d3f9753cedb7 | -10.61692 | -54.61394 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3bec930-a4cb-3ef1-a88b-0ceacf6dc0db | -10.61639 | -53.67405 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03a077f3-08a5-3c5d-a64f-24b040fd95fa | -10.61572 | -50.91952 | 2024-10-09 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c48cd82-6bbe-30fa-add6-7f6e807cf444 | -10.61565 | -54.23883 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6b06ed0-8858-3b22-9354-426bdb76f423 | -10.61562 | -55.91932 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 23d5ea98-dab0-3597-ad31-d01e3eca41b1 | -10.61494 | -55.92319 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 098867d6-52a4-3d61-8e86-6a66759d834d | -10.61486 | -54.24353 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef9c8f22-0d83-397d-8bad-7b2b95e31aef | -10.61425 | -55.92712 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c3b837c-443b-3408-94f2-0c12c2bb99bc | -10.59374 | -64.02757 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c057c8c7-5165-3bce-b1b9-c815091c5610 | -10.5925 | -64.03365 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bc7d2c9-2560-3037-be1b-768dd2e4f5c4 | -10.58686 | -64.02554 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3942c876-3976-3dc2-975a-70c687540d8a | -10.5857 | -64.0312 | 2024-10-09 04:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7482b0c3-dbc6-36ec-b40e-95ae9e9eac48 | -10.57175 | -54.24527 | 2024-10-09 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ac92059-3ed7-30ae-913b-76ed368c5328 | -10.56672 | -56.55625 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d61a4f5-1208-3944-b332-9e95d97c124a | -10.49127 | -51.84974 | 2024-10-09 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f950e40-34d6-31a0-b56c-ee487e1f9dfb | -10.48693 | -54.53338 | 2024-10-09 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1346361-cbf4-37b4-a6a8-32f362817081 | -10.42748 | -60.99294 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99cb9dc0-6f99-395d-92b0-e63a30507b6a | -10.42667 | -60.9971 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d34b0b66-1876-3ebb-ae90-42e26a6e6abe | -10.4258 | -61.00164 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a0dab32e-d75a-3e8c-9c61-f49fbe50185f | -10.42149 | -60.99241 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a977c0f2-039b-39ce-becc-213584b8ba0a | -10.42068 | -60.99659 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f8ad4ebc-76e7-3197-be34-05ec372149e4 | -10.40148 | -55.2612 | 2024-10-09 04:40:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f20af55a-2658-3003-a8a1-9eaa632fece4 | -10.39493 | -61.25719 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 042cedf2-bbc8-3ff9-bd10-9724f972b639 | -10.39419 | -61.26099 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4489be5-f9c3-30fa-b3e9-4d24bbbf3796 | -10.39403 | -55.25624 | 2024-10-09 04:40:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3544f99-b9f6-334d-b6cc-8b0a646122aa | -10.39306 | -61.23478 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3b76def-fdfd-3f89-a54d-648f10b87b68 | -10.39223 | -61.23908 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5be8f653-7e52-33fb-b4b9-90907cdee9cb | -10.39138 | -61.24344 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 095dc8d2-4f92-34b0-9329-dd4473e490fd | -10.39055 | -61.24778 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1000d423-ab11-330e-a877-db43c4b1de9e | -10.38971 | -61.25211 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f482cd02-d347-3f54-8b09-54f162b299bb | -10.38895 | -61.25604 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 182ab22f-9bd2-3f9d-8d92-1e9b94bb47cb | -10.38876 | -61.22499 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ee8b696-7e00-3dab-963a-5756e126b613 | -10.38826 | -61.25961 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1cb8441e-48b1-38f3-a71b-1bca54fd1202 | -10.38793 | -61.22929 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b9297db-e680-35f3-94ef-7dcab860d913 | -10.38755 | -61.26326 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccbad52c-81b4-3b63-a1c2-8f6020f964f3 | -10.38711 | -61.23351 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3455c38a-618b-3d68-92bd-a538448e5cf5 | -10.38677 | -61.26729 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ae39ba4-9fc5-34d7-ac47-c7546ff3e5ce | -10.3863 | -61.23774 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cf90695-ffbe-3c59-90f2-74cfa74dffa8 | -10.38548 | -61.24195 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ace951c-c0e0-3308-9b12-824b55351487 | -10.38466 | -61.24616 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ff197bd-2ef5-3b69-b5a1-c7d474faba5b | -10.38381 | -61.25057 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c8ee317-1e30-30c1-aa4f-cf690f691273 | -10.38297 | -61.25491 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c610b90-61ff-3941-9ab8-3d6b17467072 | -10.38218 | -61.25897 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 240266ad-ac2f-3341-9fb2-cecfdb3b8543 | -10.38196 | -61.22813 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2029c5e-8203-3106-8575-712a03496fe5 | -10.38137 | -61.26313 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6918b571-4bd4-3db7-a497-7a5b0bb20af6 | -10.38115 | -61.23234 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e79644a4-2de5-39d8-b552-e508b2d74ec7 | -10.38035 | -61.23646 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4b65958-f638-3859-8879-595f4ff02459 | -10.37957 | -61.24044 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2029d750-f311-3d5c-ab2d-68a1ac66f4c2 | -10.36145 | -55.86359 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34d8cae5-7f22-3318-891e-1c83a280a940 | -10.35726 | -55.86283 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4211b43d-9d72-336f-a661-2f7aa148cec4 | -10.35657 | -55.86672 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README149.md)
