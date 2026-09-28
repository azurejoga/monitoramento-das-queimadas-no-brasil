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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06184983-fadd-345e-ab02-935fd5693b7c | -11.3735 | -43.4209 | 2026-09-28 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| cec59965-48fd-3c70-86b0-1fbaf5b355be | -2.7766 | -49.4977 | 2026-09-28 00:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| bf8cd5c4-708d-34c2-a587-920c653d409c | -4.7956 | -49.1211 | 2026-09-28 00:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 29d6d066-9fc3-3513-9f4b-f1d174ff63ed | -3.1655 | -54.0844 | 2026-09-28 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3b7683e8-817e-35de-a3cb-96cba88235c9 | -3.1472 | -54.0648 | 2026-09-28 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| dab7e9f2-1aab-3a39-b3b0-7a5bfda38b49 | -11.0959 | -51.3443 | 2026-09-28 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 57fd5033-7fad-33b6-a9c3-089790802e57 | -11.1775 | -44.7832 | 2026-09-28 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e905d927-ea0b-3d4f-8e34-62517c3f035c | -2.7767 | -49.4765 | 2026-09-28 00:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 0cd234fa-dd9a-3c38-8e22-457b3ba723f3 | -11.0956 | -51.3654 | 2026-09-28 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8f0b1ec6-a9e0-307a-955d-a21b595e82e0 | -11.1771 | -44.8064 | 2026-09-28 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 084cdf26-6ca8-3542-8294-e2eebb2810ee | -11.2158 | -44.7778 | 2026-09-28 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 9cd72589-c982-3b55-a888-e718fc469c2a | -11.1149 | -51.3423 | 2026-09-28 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 72df2e2e-139f-3996-9012-18f4935ca64b | -7.8625 | -61.1978 | 2026-09-28 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| cb8c7cd6-e242-30d8-b60f-b70a304a9828 | -11.0962 | -51.3231 | 2026-09-28 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 63ce91ee-e14c-36e4-be08-2a2a5d1af281 | -3.2137 | -51.0384 | 2026-09-28 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 60efc541-e9b5-3eaa-b621-a4d6aa5d8826 | -11.1966 | -44.7805 | 2026-09-28 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 8bcc1da7-12e0-377c-9544-dcee2f1150d0 | -10.4232 | -53.8219 | 2026-09-28 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c36b3f39-9d64-3ffb-9b3f-65aa9cd53fb5 | -11.4425 | -44.9303 | 2026-09-28 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 0f0fabdc-2582-3ef0-aa8e-1ad7c8440655 | -3.2198 | -54.3238 | 2026-09-28 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ab689ca1-c8a4-339c-b23d-18ad8c47d3f8 | -11.3436 | -54.1086 | 2026-09-28 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| fb0a96fd-2d61-39a0-99c0-2f53ad201ebe | -8.2288 | -45.4829 | 2026-09-28 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f892871a-72cc-3354-978d-edc38a2b8921 | -3.2138 | -51.0176 | 2026-09-28 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 87886b26-3678-3783-9ea7-7ddadf240257 | -3.1471 | -54.1049 | 2026-09-28 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| cd3449a0-82b0-36d3-8a68-5672818e61cc | -7.8626 | -61.1787 | 2026-09-28 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 37320cc8-7ec9-3cd9-b0d4-c441a4111b07 | -3.1471 | -54.0849 | 2026-09-28 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 69797f34-b966-3158-81f2-86e06b78400c | -3.1953 | -51.039 | 2026-09-28 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 8e49a761-340d-3906-94ea-b41c9cfdf87a | -11.6981 | -44.545 | 2026-09-28 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1c74e9e1-aa65-3d6a-9509-8e863275a4a5 | -10.2067 | -49.9898 | 2026-09-28 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e09e0e20-a17b-3c27-979b-6720f4d3b804 | -6.6872 | -45.6456 | 2026-09-28 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 201.9 |
| fe429ebe-0bfe-34d3-9b60-076ebd23a2ef | -10.4043 | -53.8236 | 2026-09-28 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ba549c55-ce88-318f-bc70-d5ee070770a4 | -11.7173 | -44.5422 | 2026-09-28 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3867ddef-3014-3864-90c6-f04d3c371693 | -11.077 | -51.3462 | 2026-09-28 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ded12a2f-47c8-3eff-9e6d-092d9dae3d8f | -11.4616 | -44.9276 | 2026-09-28 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d26bb719-e09f-35e4-838c-620e904b13c9 | -11.6985 | -44.5217 | 2026-09-28 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 504df399-3b1e-342a-a395-cbf3b4afafc8 | -11.4429 | -44.9072 | 2026-09-28 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 4b43a8c3-336d-3207-bd8c-7bb447967456 | -11.1962 | -44.8037 | 2026-09-28 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 1a5f7627-57ad-3271-935b-76ccb4291248 | -6.7026 | -45.9814 | 2026-09-28 00:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2f794167-46b5-39bd-ae40-01606542c214 | -11.2154 | -44.801 | 2026-09-28 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2af8e5cb-9b1a-3924-9abf-89f17c36cdbf | -11.3927 | -43.418 | 2026-09-28 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 7fc92936-94ec-314f-8b63-73fbb5175539 | -1.1241 | -57.2786 | 2026-09-28 00:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 434df655-85a1-38ad-824e-e9d008509a08 | 0.07252 | -51.14276 | 2026-09-28 00:01:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f7e8054f-5aba-35da-9192-e0b3324c5630 | -0.46093 | -52.07809 | 2026-09-28 00:01:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 08419451-cbda-3bb3-8982-5bb61bff68c2 | -0.45965 | -52.06883 | 2026-09-28 00:01:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bb95f13f-2d77-3c33-bc4a-865a63266d35 | 1.26228 | -50.68258 | 2026-09-28 00:01:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 29dd64fd-8c2f-328e-b7b3-f9f3898cbeb2 | -1.23067 | -54.09573 | 2026-09-28 00:01:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a2ca869b-2bac-3a94-81f6-4308a7b21082 | 1.76486 | -50.83687 | 2026-09-28 00:01:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a10eacf-d0dc-3061-930f-145ee35e82cc | 1.67077 | -55.9371 | 2026-09-28 00:01:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c90a9609-028a-30f2-bb50-3703d6d2c05f | 1.76366 | -50.84563 | 2026-09-28 00:01:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3aae5284-4161-3260-ac2d-1d0f4a5fcb23 | 1.67994 | -55.9537 | 2026-09-28 00:01:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3407f279-11ef-38c9-bb60-8cb15fe55c59 | 1.73605 | -50.85072 | 2026-09-28 00:01:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1d3e4109-dea3-3d21-8298-4c87247130e1 | -2.05192 | -56.86827 | 2026-09-28 00:01:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| fb077cb0-d958-376e-83df-2065424aea95 | -1.73954 | -57.18447 | 2026-09-28 00:01:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ae0fabed-f479-32ee-9ea0-6a10a5bee9f2 | -0.53404 | -49.19302 | 2026-09-28 00:01:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b4c7dc00-d7de-3959-b1d8-b809e32f2f03 | 1.66163 | -55.92055 | 2026-09-28 00:01:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4d6804be-bbe7-3695-8fdf-770c94e9bc65 | -1.12661 | -57.28815 | 2026-09-28 00:01:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 34024e22-c0f3-3b75-823d-14cf602854b6 | 1.26348 | -50.67381 | 2026-09-28 00:01:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 170a81e9-82c8-3b19-beff-3e780e74a292 | -1.23235 | -54.10772 | 2026-09-28 00:01:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9459ac22-1045-3457-9035-60940bf5c163 | -0.43649 | -52.03426 | 2026-09-28 00:01:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e86fc66d-fdcd-369c-bb7f-e75bf490b272 | 1.26107 | -50.69135 | 2026-09-28 00:01:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7f25d5b-568f-3471-8a71-cfe33eb8ef97 | -1.74355 | -57.19038 | 2026-09-28 00:01:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 54f31ed4-f379-3cd2-989e-0c3172ce7b2e | 2.38501 | -51.01927 | 2026-09-28 00:01:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d8a51604-e25c-3ad2-817c-a06f7636a9b5 | -2.7582 | -49.4771 | 2026-09-28 00:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 144182c4-6813-3529-867d-28ef4b47a86f | -4.0478 | -54.2194 | 2026-09-28 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4cd9fb37-1eef-30a5-94aa-3be1b23b3d83 | -9.9973 | -50.1393 | 2026-09-28 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 02b5db53-c5d2-30b7-a9f7-3f8beba8446a | -11.0959 | -51.3443 | 2026-09-28 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| ac488418-3946-3c23-bf1f-e03176b1c2c9 | -3.2137 | -51.0384 | 2026-09-28 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 169.8 |
| bc9ab437-9427-3d9c-81e0-df9c72531703 | -11.1149 | -51.3423 | 2026-09-28 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| cebd6364-e091-3190-b974-755beab4415a | -3.1655 | -54.0844 | 2026-09-28 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d5b9cbf2-5948-3dab-b163-bba475c5759e | -2.7767 | -49.4765 | 2026-09-28 00:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 7e49a67d-628f-3f0e-a501-ec74265a9923 | -1.1241 | -57.2786 | 2026-09-28 00:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 18d98da6-d2c0-3203-bde6-bec699b99e9f | -12.8658 | -44.7813 | 2026-09-28 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 0509b437-90a2-3802-a361-eef70a116695 | -8.2288 | -45.4829 | 2026-09-28 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 99c14137-c8b0-3513-9bc9-9a043d0f348a | -11.1152 | -51.3211 | 2026-09-28 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5e1bb8fa-d4cf-32b9-a5b6-211adea3677f | -11.3436 | -54.1086 | 2026-09-28 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8d96c56b-6eda-388f-9c57-0fa1b0737325 | -6.6872 | -45.6456 | 2026-09-28 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 51b76f94-469d-36e2-9617-f1e9fbc380a8 | -2.9081 | -54.1309 | 2026-09-28 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| aebcc9b7-3b7b-35c7-ad7c-0e53c5949990 | -6.7059 | -45.6441 | 2026-09-28 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d1d9beac-cc18-30bd-b3e0-4fbc89069f37 | -10.4232 | -53.8219 | 2026-09-28 00:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 26be8db7-52a0-3c60-bc52-61f98af0033d | -3.1472 | -54.0648 | 2026-09-28 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0782297f-a7e7-34b0-a3ea-5b471562c762 | -11.3735 | -43.4209 | 2026-09-28 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 7548bf7e-0cda-3aca-840a-a000219ced95 | -11.4616 | -44.9276 | 2026-09-28 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 77b6cea4-2905-30dd-a7f1-1337a0dbc5a1 | -3.1953 | -51.039 | 2026-09-28 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 268ca1d1-4a42-377a-bae8-bba003cac20b | -12.155 | -50.352 | 2026-09-28 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 678c7679-6e98-3647-b016-77d1af4a1640 | -11.0962 | -51.3231 | 2026-09-28 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 65cd829d-9ed6-3111-8878-56190afd80a1 | -15.112 | -53.8838 | 2026-09-28 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 428e6a39-6cff-3c9a-a887-c111c056cd32 | -11.6985 | -44.5217 | 2026-09-28 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ec851ef9-fa94-38b6-92bd-548f0bb8650d | -12.8653 | -44.8047 | 2026-09-28 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a881aeb3-4d6e-3b00-b6ed-9ba8c83a38ff | -11.6981 | -44.545 | 2026-09-28 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4a252e61-269e-33f1-889b-b01419c861d7 | -6.687 | -45.6682 | 2026-09-28 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b5cfb3ea-5fa5-3b9c-9745-a07bd22a56c1 | -8.4438 | -44.8683 | 2026-09-28 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0ee6362c-e251-3cf3-8039-252ac9862693 | -3.1471 | -54.0849 | 2026-09-28 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 078f1d5d-e735-364f-b122-2db47f76723c | -2.998 | -54.7492 | 2026-09-28 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 0c21ae8e-515f-3ea9-a389-085b78195993 | -11.4425 | -44.9303 | 2026-09-28 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| ef66c7b2-b109-3edc-af3e-8a2d7444b093 | -7.8626 | -61.1787 | 2026-09-28 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5e258e4b-b830-3e28-b81e-e372a298de9a | -2.7766 | -49.4977 | 2026-09-28 00:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 7e3c9968-7b7c-3e4e-870b-a356a9643618 | -3.2138 | -51.0176 | 2026-09-28 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 585bd885-520c-394a-a601-5dedd03c60c8 | -11.19 | -44.8 | 2026-09-28 00:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb1fe7ef-7ce2-3574-9ebb-e0057fbfaa86 | -11.22 | -44.81 | 2026-09-28 00:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb78b2b5-8354-3587-ab99-e59f2756c135 | -3.1655 | -54.0844 | 2026-09-28 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8f232279-e179-31f3-9dda-387af9bbf7b8 | -11.6981 | -44.545 | 2026-09-28 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |


[Clique aqui para ver as próximas entradas](README2.md)
