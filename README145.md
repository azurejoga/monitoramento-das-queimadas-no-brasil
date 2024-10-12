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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f37262d-bc5b-37aa-9fa5-5c08aad1a54a | -9.92574 | -59.94191 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 641d20c0-001f-3b5e-9830-fb5dceaceb3f | -9.92077 | -59.91185 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df81f12a-ee02-3f8a-b73f-7c3a4cc330ff | -9.92025 | -59.90862 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7434d2f2-2595-38f0-a3c8-e693a8eca163 | -9.91956 | -59.91392 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4774445f-1c0f-321f-b955-cebc3bdbe7a7 | -9.90625 | -60.30867 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 030cdbdc-683a-3550-b7e8-f374572d0530 | -9.86787 | -59.82858 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 074f9740-1bca-370e-b91c-abf6cb0bb25b | -9.86714 | -59.83406 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abcff510-68fd-34df-b0bd-8d97bd57770d | -9.86459 | -60.1073 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5be8daa9-03da-3c75-9229-923979834e69 | -9.86174 | -60.12822 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65d1124b-9bee-3084-a105-69e6d62a81d8 | -9.86121 | -60.28681 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 429fe92b-0de5-3582-8811-13a45eef6172 | -9.8596 | -60.28403 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3db4f9e4-53cf-3588-8fdf-c120008ca6c6 | -9.85911 | -60.11191 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9dd590e-9ed6-3450-af4d-0b22b85af7c2 | -9.85891 | -60.28907 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df756f16-1672-37f7-be9d-0d689d4eba3b | -9.8584 | -60.11712 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c45122b-6009-36e8-97c9-a4d45c919fda | -9.85808 | -60.32959 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a207ca10-3e86-34fa-b3be-33c9fd271711 | -9.85769 | -60.12234 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec28bd75-d040-31d3-94c8-8694572ad499 | -9.85698 | -60.12755 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16901139-32b1-3c64-8649-f9c6161c6410 | -9.85651 | -60.28614 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| acfcaeb8-5fc9-3400-8af9-5b7c886ed4b6 | -9.85598 | -60.3268 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9261df25-dddf-37bb-9015-e8d5d60c2903 | -9.8549 | -60.28337 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7236bb4f-87a2-34b7-9af4-4c5432efb60c | -9.8542 | -60.28844 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ea85d19-ee7b-3f04-971b-1443ca9e87a2 | -9.85338 | -60.32896 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 285efcbf-c0b6-3121-a31e-5029199c5153 | -9.85129 | -60.32612 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae09c3a-e304-3c75-b675-2792f65faa44 | -9.85019 | -60.2827 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6f08f334-c506-356d-bb1c-108fdf989335 | -9.8495 | -60.28776 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a1c4b82f-e523-383a-ba64-aece5e196b4f | -9.84549 | -60.28202 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8db9ca36-a38e-34ea-aacd-2ce4c0271277 | -9.84479 | -60.28708 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5198fc61-f00e-33d0-9a0d-dc00d0a63461 | -9.84284 | -60.26631 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf5a6ccc-8f2a-35a7-a12a-2c0c0b36f592 | -9.84216 | -60.27127 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 802e72b3-1246-31ba-b0f0-0f45be25b844 | -9.84079 | -60.28135 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7b32ebb-7e0e-311e-bd2a-a9611029597a | -9.84009 | -60.28641 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3539052-435b-38ab-9701-b3fefa255dd4 | -9.75383 | -60.43094 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25ba1c28-7646-325a-a1f8-2ca1e24aeda2 | -12.14944 | -60.74709 | 2024-10-12 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71ce36b0-4953-3203-8d9f-26842c833eba | -12.14471 | -60.7466 | 2024-10-12 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42359b27-bf6c-330f-ad15-01363936824e | -11.21474 | -61.33841 | 2024-10-12 05:48:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f961bee-001e-3901-a031-44b7c086ef7f | -10.95047 | -61.12676 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a97cc58d-2788-366e-9719-845f4541aae6 | -10.94988 | -61.13125 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21375af1-eb1b-33ff-a96d-c93eae62340f | -10.94835 | -61.1079 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 744a3b14-37da-3ccf-a18d-b7cc0450e96a | -10.94721 | -61.10555 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d764e820-1632-346e-bead-f1e8db1ca96d | -10.9466 | -61.10991 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6cd001b-82db-3b97-989f-bca568cc6011 | -10.92982 | -60.82458 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a668bc9-2baa-34ec-a7cf-469ed77e83db | -10.91703 | -60.95432 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d4f9a708-3005-3bc8-a005-01d47b117f5f | -10.91641 | -60.95886 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e251bfc5-5cc3-30a2-8a70-8dab207b9c13 | -10.91242 | -60.95399 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d7f3689a-52cb-3b97-bad7-4ff4d29f90a2 | -10.90183 | -60.89394 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efcba6f3-9e06-3148-ae8c-ec375393ac49 | -10.89725 | -60.89325 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0660521d-0ca3-345c-bf3c-f314eb943214 | -10.81885 | -61.41187 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40b8eca2-7072-3811-b05f-0d7a6ebe9d5d | -10.81826 | -61.41624 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5c1d612-9f4f-3f11-81e4-60328ec62186 | -10.81768 | -61.4206 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25660a6d-4572-33b2-84c6-9830bf664d8a | -10.81326 | -61.42002 | 2024-10-12 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a9ecf69-d976-3d90-a7d2-092159f20bf5 | -11.41288 | -60.45727 | 2024-10-12 05:48:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01af336e-5f15-3114-8ab9-f6c97b7e0c15 | -11.41013 | -60.40439 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b07fe10-e8cb-31de-ae94-f9d4a192e809 | -11.40604 | -60.39852 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd8de0a5-d29c-3b54-83c4-9b4e50b46805 | -11.40405 | -60.41373 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43ec3543-97d4-33ad-ac4b-5f01067e0f3f | -11.40336 | -60.41895 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd578ca0-45d1-3341-8137-27b6f3ce19bc | -11.40127 | -60.39778 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 664d79e0-3811-3525-9b80-bc359faf3aaa | -11.39792 | -60.42347 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86edc1e0-2dc1-3eec-90c7-9f94cf66e858 | -11.30358 | -60.43489 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a214433a-293b-3805-b872-a9bf0a465259 | -11.30292 | -60.43993 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f18c7ea-a4d3-37c8-b248-18be87d38e5e | -11.29885 | -60.43405 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2264d0b-e43b-35ef-becf-a54c61320d68 | -11.29817 | -60.43922 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f19ebcb-a660-3d7f-88c5-4c6d4999179a | -11.29185 | -60.33899 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3de3e3f-6b3a-347a-bc24-2069f97539f9 | -11.28314 | -60.48 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9ccc2ff-d75f-3913-8f2d-334bbf4e81dd | -11.2825 | -60.48492 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb152f78-00a7-3cff-a0d9-45cac523e57c | -11.28053 | -60.49994 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 028387be-c85a-3bd1-ac7d-40f01a5f453c | -11.2799 | -60.50472 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 045f3b07-2896-395d-b0ed-b62c83450dda | -11.27838 | -60.44247 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ef3a37d-39d5-3a8e-aa16-4fb6c589b87d | -11.27837 | -60.47962 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48099de9-4c01-305f-b9b1-3a39453ff985 | -11.27576 | -60.49953 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| aa046b6f-1b42-3300-b1f2-f7288a0d1a7e | -11.27513 | -60.50433 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a19680f6-3956-314a-8ba1-e492f5d5d803 | -11.2737 | -60.47841 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40ec0b00-b859-323c-b4ed-483d6dceff70 | -11.27036 | -60.50402 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bbab4e90-b977-3d94-bd6b-68f108e7761a | -11.26975 | -60.50869 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ce55034e-bac2-325c-872c-d6ea94f959b1 | -11.26753 | -60.41413 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0e1d9e2-61ed-3e32-904d-129f35db61fc | -11.26559 | -60.50362 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22c58cc9-27cb-376e-a972-2588599852df | -11.26497 | -60.50836 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af70dbcd-4835-3683-a76c-0b9397068707 | -11.26394 | -60.36575 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 214441b7-c7ac-37a3-a876-1875ca4f2ca7 | -11.26021 | -60.50798 | 2024-10-12 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0aec3f00-82ba-38b4-ae00-c8ed9a272878 | -11.24491 | -60.55181 | 2024-10-12 05:48:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9533a930-8389-39ac-8bce-f086291fbac7 | -11.17568 | -60.62748 | 2024-10-12 05:48:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2712fb64-4325-30a5-a087-4ebbc64757bf | -11.17502 | -60.63242 | 2024-10-12 05:48:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30829f87-0c7a-35b4-ba14-68c9e5e7a796 | -11.17099 | -60.62691 | 2024-10-12 05:48:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04aeb631-f228-3ffb-9580-c91418cb8bb5 | -13.73632 | -60.60428 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 505002f7-2e49-310a-9744-76459d29c807 | -13.73145 | -60.60366 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6c9bc737-c0c0-3345-9619-5c4ce58312e5 | -13.73077 | -60.60915 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eb722834-ada8-3818-89a4-b8c71039a40b | -13.35043 | -60.58208 | 2024-10-12 05:48:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9899e9a-26af-37b1-92d6-efa8952b659c | -13.34619 | -60.57661 | 2024-10-12 05:48:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00d0b76f-c3f9-3ba1-aab4-5a53b8b420af | -13.34557 | -60.58147 | 2024-10-12 05:48:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44737bd7-d9e9-361a-bc8a-114fa47400d0 | -13.73153 | -60.64272 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49f6cb81-3ff3-3ef9-8852-2d84d70fb1c6 | -13.72804 | -60.63113 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7c2177a0-bdad-3704-8218-37d3e6d6e3ea | -13.72736 | -60.6366 | 2024-10-12 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 31987d65-db12-3c10-b086-2b671270f99b | -7.97804 | -61.21805 | 2024-10-12 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7adcdb59-79d5-34f1-a1b2-528789175778 | -7.92769 | -61.26461 | 2024-10-12 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeccec58-0243-3ba4-ba9a-68c58e1f3809 | -7.92713 | -61.26865 | 2024-10-12 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c83d5d2-ee7f-342f-a029-9fd4fe7543b1 | -7.90565 | -61.51241 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dcaedac-d8be-365d-94c5-4d522683f670 | -7.90332 | -61.46823 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 685bdd1e-4781-3cd9-9d1c-18cce4fc5cda | -7.82783 | -61.60141 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e937d2-f188-37f6-925c-53fb2ffc7bce | -7.82284 | -61.6938 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63d57811-708a-33d4-8ed5-29fa0ea3b378 | -7.81867 | -61.63508 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41a20930-2148-3a17-9466-ebaefd3cb465 | -7.81812 | -61.63889 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README146.md)
