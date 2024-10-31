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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff67cf23-63f4-3416-b3ce-cc3a3a1ead3b | -19.50111 | -56.68702 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| aa3bae0a-95fd-314c-8349-b9fcb25d4a97 | -19.49048 | -56.71611 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f66a541d-0abf-36ee-9c7c-3ba8dc2350b8 | -19.48947 | -56.72115 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 730dd893-e0fb-3e29-94f1-b332b16caa43 | -19.54212 | -56.72253 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 5e60c262-57d6-326d-bc18-da4130de1c3c | -19.54176 | -56.71336 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 50ed2b4c-74ba-314e-b325-af4eca2aa119 | -19.5385 | -56.71646 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 28753bae-d8d4-316a-9a1f-2dba0853686e | -19.53291 | -56.72046 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 88bb70f1-cc27-3966-a4c6-42042b4c6a64 | -19.5293 | -56.71438 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 6ff7d603-c914-31dc-a54f-0bbaf76cd8c5 | -19.5257 | -56.70831 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 67075b11-cff1-3933-bfbe-ccca44860bc2 | -19.5067 | -56.68305 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 337892b0-be75-3354-9a9f-1ddc0824465c | -19.5057 | -56.68806 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8f0b3157-c334-33aa-857d-551a28218787 | -19.4981 | -56.70206 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 351ba231-c276-3d5b-884d-be86cea6c1cd | -19.47958 | -56.65081 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7fe7aa36-4dbf-3158-877c-b580eb1791b6 | -19.58847 | -56.62493 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e7fff4b0-92b6-3bb6-8700-da9c8e5496c6 | -19.58491 | -56.61896 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 47d938e2-3d52-3270-b1a4-b85716bad885 | -19.60714 | -56.72284 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| fd3ef7d1-c6d3-377f-96c0-726ed68ba0d3 | -19.59536 | -56.70972 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a1daf58e-2dca-3f15-b174-680953755002 | -19.59177 | -56.70367 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 250514b3-df06-3f49-9e40-f498d641b85f | -19.58416 | -56.71766 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| eb538972-0536-335f-b8f6-d6f4d1a8a976 | -19.60973 | -56.73393 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e307e458-0966-3d74-87f8-cf7f4b7cf076 | -19.60873 | -56.73896 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a71ee646-236e-38ec-9eaa-81bc31340132 | -19.60773 | -56.744 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4538549a-e7ae-3f3b-bc37-fa30bf961fd1 | -19.60672 | -56.74903 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 36d5ca45-88b9-35a5-b0a4-788ebfc54faa | -19.60655 | -56.70178 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f81aa400-a09e-3fdb-a8a4-b67fc1d5d3c7 | -19.60614 | -56.72787 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2d27fe77-b92f-33d6-b780-a39f78d6aefb | -19.60571 | -56.75409 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| a59a5ff4-7273-337d-ad04-11cdc47c91e4 | -19.60513 | -56.73289 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| bcbc2e94-23ba-36a6-a136-4ba3d22d745b | -19.60471 | -56.75912 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| b766d398-57b0-3151-9308-d9b4965c9a90 | -19.60413 | -56.73792 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 59eb0906-bac2-3807-8f4d-0041ee6c41f2 | -19.6037 | -56.76417 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| acd9ce39-a8b8-3a99-a597-44cc7e286b96 | -19.60355 | -56.71679 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1f278fd7-74f1-3e1e-b6b1-ac2554372b77 | -19.60312 | -56.74296 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| aa96a1af-8f18-35c4-bc05-06ef6ae95ace | -19.60254 | -56.7218 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| fa478ce3-6795-3158-bcd8-01212695baeb | -19.60212 | -56.748 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| fd033c4e-640d-38a7-97bf-4b8ce3d0e836 | -19.60196 | -56.70074 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f208ae3b-4834-320d-835f-6ea156472e33 | -19.60154 | -56.72683 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| ccb3f436-0d73-3e93-b1e0-04d7ca8beb03 | -19.60111 | -56.75304 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| a05b2781-7da7-394e-a693-593767353727 | -19.60053 | -56.73185 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| f22fe1a3-2586-3dd3-b397-8f0e53e6e66f | -19.6001 | -56.75808 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 3b5d74db-1296-3842-8990-a103c988f1ed | -19.59953 | -56.73687 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| e3cb63ba-eb04-3d62-8df5-a7921cab76f9 | -19.59909 | -56.76312 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 44f64cca-5a00-3a16-85f0-25b951ab2bea | -19.59852 | -56.74191 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 73f32ef6-7003-3acf-b060-bfabe084d578 | -19.59795 | -56.72077 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 988e6ee1-5193-33bd-befe-4fd98e73b871 | -19.59752 | -56.74695 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e8dd6bc0-d026-39f3-bcbc-f50e8e81eac5 | -19.59694 | -56.72579 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| cb9fbb06-3666-388d-b642-5d5ba3bb579c | -19.59651 | -56.75199 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 849d8521-446d-37f0-a2e2-725c85e4bce0 | -19.59594 | -56.73081 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 7b42607f-16b5-3f01-b4ab-067f19f20699 | -19.5955 | -56.75703 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 93e60e48-ace1-35e3-841e-4d8eb498f7dc | -19.59493 | -56.73584 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| a0aab780-1970-3a7a-b983-86a5c9e23fb3 | -19.59449 | -56.76207 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 6fe38fbe-3c0f-31bd-a436-c51ac7f09edb | -19.59436 | -56.71472 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 78c63865-1f4d-3215-8a48-e970ccf0fd39 | -19.59392 | -56.74087 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bf5dc52a-b0c8-3fb8-8d62-9cb0296e011c | -19.59347 | -56.76713 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 82c7877e-bc92-3cd3-8ead-88b5109697a5 | -19.59291 | -56.74591 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4123eef3-b7aa-3073-8094-2291ce695863 | -19.59234 | -56.72475 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| d55f8708-8f23-3bc2-ae93-094bfad41d64 | -19.5919 | -56.75095 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 30e75476-964e-38c4-a176-3ba11103f780 | -19.59134 | -56.72977 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 7ccfd744-8fa0-3406-8f13-83b08e1382a9 | -19.59089 | -56.756 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| e38701c8-97e4-353c-9f3b-1ebb7b128989 | -19.59033 | -56.7348 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 2272f95b-a578-39af-85fa-cc99d5596f9d | -19.58988 | -56.76104 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| b836af8f-45c1-3db6-9427-493f00efeee1 | -19.58932 | -56.73983 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 9454cb71-41cb-3bb8-84e5-9a52ec07ae0a | -19.58886 | -56.76609 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 0750217d-ff6d-3813-80e9-30cdf689df20 | -19.5883 | -56.74488 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 4c932869-41f1-3da3-8711-a40bcee3a99c | -19.58729 | -56.74992 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| a68d9d2b-ed68-378a-94d3-a6d67db5ec64 | -19.58718 | -56.70263 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6773f191-f5f8-3b91-b3bc-ee27d3c9552d | -19.58674 | -56.72874 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 2f0901bf-c40d-3851-9a04-092ac3f3d2bc | -19.58628 | -56.75496 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 200b9faa-fbc7-3c3b-9f34-3175b8f272d1 | -19.58573 | -56.73376 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 2166796f-1114-3679-bee4-e5a20ed682b7 | -19.58527 | -56.76 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a1e21069-6bf3-37f7-b301-fa37d49f6819 | -19.58517 | -56.71264 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9e56120e-8c65-3a9f-9e7e-89d12dbb74a8 | -19.58471 | -56.7388 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| ff608c83-2b59-38b8-8847-753a1cb692dd | -19.58425 | -56.76506 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 7c65b790-cfce-3a92-bddd-07b20b157af7 | -19.58391 | -56.6239 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 20c2de40-96df-321d-8712-076dc30f3148 | -19.5837 | -56.74384 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 28286e31-7a73-3816-adc4-0dd697d3c94f | -19.58323 | -56.77012 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 01d5a6ce-59c4-3512-be9c-0a3ecf6abe06 | -19.58315 | -56.72268 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 96ee494e-c101-3d85-ac46-fdf456ff98a8 | -19.58269 | -56.74888 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 1e60916a-218a-30f3-9cb8-b7df81d75370 | -19.58214 | -56.7277 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2e9571d0-a334-383f-b7ca-d24b6ddba89e | -19.58113 | -56.73272 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 994db351-1979-3efb-9e4e-1b4b12618f30 | -29.81493 | -51.17825 | 2024-10-31 04:32:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| a3331866-bd5b-3b7d-a7fd-2d898eb92d59 | -26.56208 | -53.56665 | 2024-10-31 04:32:00 | NPP-375D | GUARACIABA | SANTA CATARINA | Brasil | 4206405 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d65a594d-8936-32d0-9c15-81d2effc00cb | -2.5031 | -48.4596 | 2024-10-31 04:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1df6ceba-c857-32f2-b00a-b7b03da4555b | -2.5215 | -48.4806 | 2024-10-31 04:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| dd1a9227-1bda-32bb-9e07-ca210985d1bb | -2.5216 | -48.4591 | 2024-10-31 04:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| d54f0045-e016-3b83-994f-999eea10680a | -2.5401 | -48.4586 | 2024-10-31 04:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e35053e8-7f52-3162-8f81-5f3af63a168c | -2.8431 | -46.6871 | 2024-10-31 04:35:22 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 2a3e0026-ddf4-3ae4-8d7e-dd3afddb5286 | -3.4568 | -50.2992 | 2024-10-31 04:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8683a04e-94c4-39da-a2f5-bbfeb7945260 | -4.8364 | -45.8418 | 2024-10-31 04:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 87705e25-1d32-3905-993a-8134b5b975a2 | -4.8178 | -45.8429 | 2024-10-31 04:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| ced85d64-c222-320a-9acb-775782fde2a9 | -6.1229 | -43.9578 | 2024-10-31 04:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a1de022e-5524-3ad0-9e81-ee26b9eaec6e | -6.1416 | -43.9563 | 2024-10-31 04:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 03c80f0c-c9e2-36da-bff6-448defa3afa2 | -9.7419 | -36.0772 | 2024-10-31 04:36:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| 516e2471-628f-327b-8151-5f7c59f7eec7 | -9.7226 | -36.0805 | 2024-10-31 04:36:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| b679df3e-8cbd-3bfd-ad97-715af6ec7032 | -19.5083 | -56.5989 | 2024-10-31 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 6e8b745b-2f21-3a40-9455-f98e7e7ff7ac | -19.5087 | -56.5779 | 2024-10-31 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| c1ccc8a6-655b-3c07-861c-08522d19da6a | -2.5216 | -48.4591 | 2024-10-31 04:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 91f5381c-f696-3a6a-9f09-07f110bdac98 | -2.8245 | -46.6877 | 2024-10-31 04:45:22 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fb663186-88b5-3cf9-aeb7-ee0dd9d05f9c | -2.8431 | -46.6871 | 2024-10-31 04:45:22 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3b4ec727-807e-35dd-a628-b03db920a20d | -3.4568 | -50.2992 | 2024-10-31 04:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f4381464-af55-36c3-a59e-b94caada6a17 | -4.2749 | -43.4357 | 2024-10-31 04:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |


[Clique aqui para ver as próximas entradas](README30.md)
