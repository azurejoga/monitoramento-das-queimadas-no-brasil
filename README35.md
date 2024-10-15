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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d531a6-8fd9-3fa6-a948-ab21a12417aa | -2.58708 | -48.29557 | 2024-10-15 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93cbea76-cf3d-3fb5-9b55-cca6226976c2 | -2.58629 | -47.47645 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d71e0b7f-72be-344f-98f0-d574092d8b3a | -2.51224 | -48.55708 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcedcf53-95a3-3f29-b580-f0f9b51022d2 | -2.50926 | -48.55231 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5a78cd5-e9a6-3352-b33e-633336585310 | -2.50858 | -48.55653 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6d35722-a3c0-35ba-aa29-2571291eca36 | -2.5056 | -48.55175 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d47eb2d1-79b4-38c0-a0be-68c707ef1436 | -2.50493 | -48.55598 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14911e72-da76-36bf-a616-906ab9521b11 | -2.50195 | -48.55118 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21033675-95bd-32be-9a67-f3a9d6f73223 | -2.50128 | -48.5554 | 2024-10-15 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 182bcf2f-3c4f-3db5-91bc-40d660ff31df | -2.46173 | -47.80965 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 807461cf-ab3b-3c19-9e7c-d2383566ce22 | -2.46111 | -47.81355 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e40fd15e-02db-31e0-a535-f9be9e272935 | -2.46089 | -47.81245 | 2024-10-15 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abfe1d01-7fc4-30ed-a01f-ff0ab8104984 | -2.46088 | -48.59676 | 2024-10-15 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d0cfd3b-f591-3dca-b2b6-87a3529a07f0 | -3.8698 | -48.36919 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d2bc103-5aaf-3810-971a-a367571826e8 | -4.66977 | -48.50503 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5c3b824-aae2-36b9-b703-7bdce6e03f37 | -4.6352 | -48.51576 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c1bd466-c5b3-3051-a9c6-8df7797fc45e | -4.57475 | -48.01714 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4482c800-ea21-364a-8c7c-da225f223848 | -4.57127 | -48.01659 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 798221cc-90f3-3d89-a85b-3ae853866bd4 | -4.56778 | -48.01604 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b39158f5-6d23-3503-83e3-9868a4f57ddd | -4.56717 | -48.01988 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 563d17f4-cbed-304e-b611-44f8490667bd | -4.38811 | -47.76321 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 16d20a6c-55a0-3642-aeb7-4e5af8e5bdcc | -4.38465 | -47.76266 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fc4e7c69-3544-3c9d-9522-5c40a59d45fc | -4.37581 | -48.60996 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f805183-7ba2-3d33-a1ce-2ab796f5c083 | -4.37516 | -48.61406 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab89127-d1a8-3aec-9291-8a13f1e906fe | -4.32953 | -48.62336 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9564ee91-39d7-3ab8-82a1-e7d92fb6a709 | -4.32887 | -48.62746 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f44beae2-6c2e-3b45-8110-e5800bb759f6 | -4.32594 | -48.62279 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ba75715-bdd5-3949-b765-4ddf884c31da | -4.32528 | -48.62688 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29c8dbeb-84c9-3c5d-9a93-0264145f49f6 | -4.32462 | -48.63099 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48364638-6929-39bb-afb7-c9e03db61cfc | -4.32396 | -48.63511 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3351d65-cc45-3c5f-9e06-4e07efd297ed | -4.32103 | -48.63042 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b3086ab-abb6-36f6-8d07-eefca60a8921 | -4.32037 | -48.63454 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ac216d1-3b7d-3418-9321-810d9abd4d14 | -4.31744 | -48.62986 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 597d696a-3d52-3744-8a01-3eca2f6106e0 | -4.28806 | -48.62937 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 716f606e-039a-35bd-8512-2339103b5017 | -4.28447 | -48.62878 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dec2f39a-c767-320b-9ed4-a0cab4bc451e | -4.2838 | -48.63289 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5f1b9e7-84cc-31a2-9964-7612e3be8350 | -4.28174 | -48.22703 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e425d86f-e505-3a8b-ad58-d034b614a853 | -4.27971 | -48.59045 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2e5efda-e6a6-3532-af42-9001a1fee49b | -4.27885 | -48.22253 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b40cde05-69e1-3e5c-b3ab-eb2f96652494 | -4.27881 | -48.06667 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99bcbea7-08e9-3da5-a92c-9758fa0c86e5 | -4.27879 | -48.5877 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 376331e4-77b8-36cb-b4a5-f5af49fcaa27 | -4.27814 | -48.59183 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb4dbc32-1b90-3782-835d-0e152efb7186 | -4.2769 | -48.64611 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d59a08f-8c41-3a92-8fe1-e031094440a3 | -4.27533 | -48.22197 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71565f23-7b7f-32cc-9895-46e993cdb4e1 | -4.27532 | -48.0661 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d5592d6-0108-3237-97eb-cb286396d5b5 | -4.27181 | -48.22141 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e12868-df0c-3296-b7b1-c82c6dd597fd | -4.22595 | -47.85474 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2ac67f-9204-3b7e-8b97-47e1de57c984 | -4.22533 | -47.85857 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8133f827-626d-310e-9ee0-507be2424ec3 | -4.22249 | -47.85413 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baef1329-7a57-38f3-bf2b-c65ddb12ba17 | -4.21902 | -47.85352 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c8275a4-899a-35e0-b30c-6b59e8fdd45e | -4.17953 | -48.0319 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e9505a-e7b5-3c1f-948a-ee6d6157cb96 | -4.17539 | -48.03529 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c40a5442-52d9-3dcd-8670-888a1c1c47c3 | -4.0929 | -47.94353 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d394c6-e20e-3e82-a665-c89b389c4fed | -4.06044 | -47.91569 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b07c81fc-9cfd-360f-8656-906021f714e5 | -3.96395 | -47.95951 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32e78b04-b3fc-3e93-b856-1978b4f5f173 | -4.12197 | -48.27542 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ad6efe7-aead-33c0-9b90-7030ceb86850 | -4.12132 | -48.27937 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69a23c11-c10e-3e90-b799-190fbf202993 | -4.12069 | -48.28328 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fefbeb19-3615-343c-80dc-a8695c089dc7 | -4.12038 | -48.26765 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c7e2ddf-bd1d-356f-9ae9-dbf4bf2e4b42 | -4.11973 | -48.26691 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d544467e-1dc9-3c86-8226-a91eec4b8ac9 | -4.11944 | -48.24647 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74df5ef2-3369-37a2-b362-028179715944 | -4.11913 | -48.27562 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce58218c-4a22-311b-a450-68f03f47a3e2 | -4.1185 | -48.27959 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 232608b1-c4a1-389d-9c0c-cca5cfa0fee7 | -4.11843 | -48.27488 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39ab466a-6237-36fd-a4ff-9e536cf05630 | -4.11788 | -48.28352 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f481ccc-1fa1-3776-88ba-f3429823e0f3 | -4.11778 | -48.27884 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12c60cd6-f74e-312a-9fc8-70f3fca8174a | -4.11714 | -48.28277 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8775646-1857-31f3-a303-ab2734c32e0c | -4.11496 | -48.27905 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf416cf7-c33c-34ad-b2f1-f3ce2ae5c0f5 | -4.11433 | -48.28301 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4b379f3-c051-3506-b378-7fccedecb132 | -4.11424 | -48.2783 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ec869c8-d410-3832-93d9-ca1e713ebe60 | -4.11417 | -48.23822 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5708db85-e9c3-324a-8436-55f7806fe213 | -4.11359 | -48.28226 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc0e2739-6435-3a37-96ac-0b132cec35c1 | -4.11142 | -48.2785 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a382b3c-5780-3a31-9eeb-470563423589 | -4.11079 | -48.28248 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83b42e6-89da-34da-915a-224be5be1346 | -4.11064 | -48.23765 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ede7e09-4c3e-3bd4-8142-ac2781a55a4b | -4.10725 | -48.28192 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a05e6f8-ac61-3d5a-a457-6b9341d29b30 | -4.10724 | -48.47801 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e1208e2-ffb8-3c01-87fb-111bce678945 | -4.10367 | -48.47741 | 2024-10-15 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b80d8f8c-3364-3e74-b6e5-3b25ff867f71 | -4.0825 | -48.27781 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59c8d72e-712e-36a8-9e7a-76b3887f0ba3 | -4.0757 | -48.25227 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6ce771e-056d-32ee-b3d4-efaf52227f28 | -4.07152 | -48.25569 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade4e236-530e-3099-b12f-fe784fa9976e | -3.92934 | -48.35265 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dae47085-e934-310f-8078-91a07ea1e0e7 | -3.92869 | -48.3567 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e375c656-1e21-38ab-bd38-1b8815636490 | -3.92643 | -48.34806 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad70829b-3625-3c15-bfb6-21061cb59049 | -3.92578 | -48.35209 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cde6ea96-020f-394b-a25f-ebce0c41cb68 | -3.92513 | -48.35613 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5572672d-fc7a-332a-bc6c-897079158cf3 | -3.92448 | -48.36017 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7008dc3a-b254-3ac8-a961-9fe64d4c7a1d | -3.92287 | -48.34754 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bc5fd63-aae3-3118-b376-ebfeef059cec | -3.92222 | -48.35155 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88079eab-9490-3f8e-b7ca-a9cdd4469fd2 | -3.92157 | -48.35557 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 05c86daa-6ed9-3a28-b66b-2dd6a00db56b | -3.92092 | -48.35959 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 47158264-7e68-3ccb-a86b-b4f425f6749f | -3.92061 | -48.33893 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc93f0b7-09c2-3d10-9e35-7d2e674cc72a | -3.92027 | -48.36362 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7b24a72b-a5bd-34e8-8ddd-0b641e91271d | -3.91996 | -48.34296 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c6c28ee-eb4b-33ae-8bf9-4dac813e0a91 | -3.91736 | -48.35903 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d2dd7f6-74f1-390c-82c2-602c612b83d1 | -3.91706 | -48.33833 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 129d7382-7989-387b-a8c0-6c4fa8785dde | -3.9138 | -48.35846 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e28ca5b-3ca0-3c57-b616-20747d53f0f5 | -3.91351 | -48.33774 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c4b7bd2-e024-36af-9c9c-18a8e2951d6b | -3.91315 | -48.36248 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1286b998-9678-35e0-b442-c9458f1d550d | -3.91024 | -48.35789 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
