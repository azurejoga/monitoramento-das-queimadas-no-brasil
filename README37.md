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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40b58201-f93c-3c16-a3b6-b0b73e84c46b | -12.19293 | -50.5599 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c7354e4-60e0-31e0-8f72-36a35686a763 | -14.20052 | -52.85699 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5d37b81-7643-3404-a29f-0d8ccd03593f | -11.62565 | -54.58643 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73c811bb-28f1-34ba-8330-b012d8144109 | -9.96403 | -53.93139 | 2026-08-29 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae48eec9-af3e-3338-8fbf-2d967120f1a7 | -11.22517 | -54.00491 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d618d02-c5bf-3305-abde-4c1f60e6a779 | -11.03794 | -57.25183 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3067d1ab-a2aa-3142-be1e-129fb66f54c5 | -12.1938 | -50.55499 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b82d7fb0-c3ce-32af-a412-4f97e77b2759 | -15.59107 | -53.07613 | 2026-08-29 04:34:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 851b7791-d707-3271-9e36-371597fec1ff | -11.18192 | -51.28359 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46c6484c-467e-35c8-8ea5-8cb213d1a84a | -10.8824 | -50.49908 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a218de95-1c90-307b-b6e1-209f7546d474 | -11.03726 | -57.2525 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c97998a-9c8f-35b0-a0b6-d0209eb24153 | -17.29029 | -46.03487 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 950e1d69-a13b-324f-a727-2140f321c622 | -11.72226 | -54.53637 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd16b40-f257-3b1e-9a88-156ae13b3ab4 | -11.22879 | -53.98911 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 022b5bfc-ba24-394d-990d-3fbdc566448a | -10.83306 | -50.50895 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4217705c-d9f4-3eec-a07b-5732c2f4c4ef | -14.43178 | -52.58806 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08c9c966-87b3-35b4-883d-a4ae4653a683 | -10.89169 | -50.49853 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b99f5ed-174f-3204-ade0-d0aaea540552 | -11.23315 | -53.98914 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742e4d87-17df-3265-be6d-b625a2c04f4d | -13.31293 | -48.19898 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b293b93-3724-3396-98f5-28a077d15221 | -12.7691 | -44.26267 | 2026-08-29 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2559726-4a99-3c0f-ad28-1600fca855af | -11.02582 | -57.24912 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60b889d4-e0f4-3889-8f48-49f75a65268a | -13.31572 | -48.20342 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e4120b9-df59-36f4-8b58-e93e49e6c565 | -12.76589 | -44.26694 | 2026-08-29 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b12e8a4-451c-31ba-982c-232182751b53 | -11.71777 | -54.53234 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5de96f1f-0073-3da7-a24b-82cb6e03645e | -14.90763 | -43.41399 | 2026-08-29 04:34:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aff15207-6562-3940-a593-44a67e9c3cb9 | -15.3734 | -52.6799 | 2026-08-29 04:34:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29524679-2925-3246-b8ae-66d03b42a363 | -15.64494 | -45.93446 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| eb2c158b-1b52-38a1-9c14-0875ce202283 | -11.48902 | -46.93781 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ce92af8-fc76-3a46-8081-112d39d618fe | -15.65463 | -48.37217 | 2026-08-29 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d454655f-6fe1-3ec5-8ed1-fcee216a65b9 | -15.64326 | -45.92303 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b32ef06b-4b85-38c4-82a7-5005fe6376d2 | -11.60796 | -46.93568 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a86999a-e71f-3e08-82e0-24c604293db8 | -13.6547 | -47.73641 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c7ce579-9165-3434-a86f-50be29799772 | -17.28411 | -46.03004 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d2de531-9ad8-3b2a-9f09-80a77e4541aa | -14.14889 | -52.83968 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ee1811b-81cf-3ac9-8886-403a932517da | -9.96797 | -53.93811 | 2026-08-29 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6cb8f7e8-fd73-36b6-b7e4-045917620c6a | -11.22332 | -53.98716 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45481929-b428-3635-b4d0-1e351d844870 | -11.6855 | -46.73218 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff2d184d-f633-360f-bb4a-3ebfd521ba72 | -11.61175 | -46.73084 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c7d6359-c594-34f9-be1c-c7eac525fc80 | -17.61638 | -51.61557 | 2026-08-29 04:34:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01a5b2b8-1257-34cf-a7cc-eeba6613787c | -13.35641 | -46.9058 | 2026-08-29 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68145d4b-6ec0-3637-bd9d-2cf51b3efa37 | -12.20328 | -50.54656 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b57e2e05-e6c2-3546-8b0c-f93437b0eb0a | -10.75483 | -54.0489 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b02a1ed-633e-3ef4-a37a-4bd7a5e92283 | -13.32845 | -48.19019 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6967673d-386d-3f05-b685-d2bec1ac3935 | -11.0267 | -57.24459 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9215098-cfa0-3a0c-9eae-c5fb0582a114 | -13.31757 | -48.19215 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 278bf7be-4dfe-31fb-bb28-32e895e13a9f | -10.7509 | -54.04228 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69bc4873-5178-33e0-8948-a503a151fc02 | -11.65984 | -46.74256 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3007b0d-2e40-3893-8dd8-60f1d63b142f | -11.23264 | -53.99567 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e169e0be-e3ca-3f47-9102-b43b1f558db2 | -12.42713 | -43.41363 | 2026-08-29 04:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d11b51b-9855-35e5-a226-999d6cd75c51 | -11.03964 | -57.20938 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d907526-b47e-3dd0-9f89-09427533d7d7 | -11.71272 | -54.53132 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75844f96-a2a9-38e1-8cba-986aecddaf20 | -10.54321 | -50.47296 | 2026-08-29 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f20a8b85-744b-344b-945f-75dc99c1993b | -11.71834 | -54.52935 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37bc0124-e374-345a-92f5-ef6f486fe834 | -13.65505 | -47.75532 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80ef0a14-528b-3abe-a8e4-96312adfae50 | -14.90826 | -43.40965 | 2026-08-29 04:34:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a609d287-ea7c-3f62-a202-dd48b8fff34b | -13.3186 | -46.9366 | 2026-08-29 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b4a10ed-0dbd-3e82-8a30-b67850d161c5 | -11.03101 | -57.25496 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 54a939dc-9261-3fe3-9267-6a9e33f59e91 | -17.29086 | -46.03112 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ca027bb-242f-3c49-ab69-4f7a6b4a35d8 | -12.19941 | -50.54586 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b2e3815-a87b-3c5f-8fb6-6252f9bc540a | -11.03595 | -57.22764 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98dfdd67-1304-30ac-bf4d-7c6df8ec48ac | -11.9101 | -55.89538 | 2026-08-29 04:34:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93775a88-b77d-3dc7-adb7-b6aac2703611 | -14.20131 | -52.85272 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d285aaa2-3493-329c-bab8-7f083b913fed | -11.03038 | -57.22578 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2784f40-b73d-30fe-80c6-28cc43e2ccc2 | -13.17255 | -55.66028 | 2026-08-29 04:34:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70f109e4-9d71-3a5c-8545-822980c0dbba | -11.47877 | -46.94721 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6fb5afb-f1c7-32aa-8aa4-b27af61f8174 | -10.75196 | -54.03651 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 706f39d2-3732-3c3a-9044-28fd909fe3e2 | -11.26949 | -54.04404 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a2ad225-74af-394a-84c9-6435312e0fa1 | -11.23601 | -54.0014 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5aca82e2-5ccd-3504-a30a-cb51a12f157d | -15.10643 | -48.15623 | 2026-08-29 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db9ccd7a-b172-34dd-bafd-37fd480e7aeb | -14.76586 | -48.74953 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 561f55b6-118a-3039-888f-c08e7e00fda2 | -13.64736 | -47.73894 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 512f1599-ef2f-30bd-871d-24af290bf87c | -11.04255 | -57.22812 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 349f10fd-2115-3661-b382-7c083b8c330b | -11.1791 | -51.27535 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d8f6f2c-857b-3f4a-b676-7a9a68cefcdd | -10.80616 | -54.0197 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88f77e67-5992-3c1d-afc8-e45c16be76c3 | -14.18516 | -48.75566 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 666b079a-35ce-36ad-bf89-4c5c11165b74 | -17.24453 | -46.92141 | 2026-08-29 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c21fe636-271b-3a91-8aca-ae116378b6e7 | -12.43431 | -42.88781 | 2026-08-29 04:34:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b26e2524-0d19-3fdb-b1fc-709fc3e5bd17 | -14.17186 | -52.84229 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08e38013-d054-3c56-83d0-edffada9e1bd | -14.90124 | -47.74146 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7f7478f5-38bc-342b-a884-a854d1f6b00b | -14.18105 | -48.75893 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 450858c3-3fb5-33e5-9010-da5f2f3294ab | -10.53839 | -50.47736 | 2026-08-29 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 510637e4-d2ff-3219-901e-e7db7abdd5f6 | -11.26454 | -54.04316 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2578a5d4-62df-3a3d-8c75-219af0984ea0 | -11.02576 | -49.68089 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53b0cd81-e730-3083-8698-c8af800b71c2 | -16.47613 | -49.42489 | 2026-08-29 04:34:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ccfe8cd-d6e4-331d-bf97-be21592c2bf3 | -15.66141 | -48.37323 | 2026-08-29 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c81f80e-b4c0-3feb-b9ee-9587d0934f94 | -11.48567 | -46.93726 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0db6a66-2497-378b-b167-651a0492df46 | -18.64859 | -47.2879 | 2026-08-29 04:34:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bb3cb38-d32b-3ab7-b234-c45210268fe3 | -15.64857 | -45.91945 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46f3aa0d-e9f1-37bb-b661-353d19d35df2 | -17.59363 | -51.61107 | 2026-08-29 04:34:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63f8607c-d8b4-3151-a917-fe88bf4c4f5d | -14.40542 | -52.56988 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b91568a9-2269-38f2-b42e-ffd1cad3409f | -18.02768 | -49.20172 | 2026-08-29 04:34:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbb04f8a-ee4d-3512-9191-4db873db69b1 | -14.21148 | -52.84616 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba3a50fe-497d-3b2a-baad-03b637d9fe77 | -17.8537 | -46.47924 | 2026-08-29 04:34:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9302e0b2-2c84-3156-aed2-c7dce1fd37f2 | -15.64913 | -45.91583 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf36fe12-698e-348c-9b4b-32f4049f8cbb | -15.10487 | -48.14463 | 2026-08-29 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfeac289-a7b2-379e-a491-f56d90ab25cc | -11.2256 | -54.00588 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af6a236f-ec26-34e4-9438-65e0e51f40c7 | -14.15983 | -48.77931 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50bca004-9550-31ac-a992-9b7c7dd21398 | -15.36918 | -52.6792 | 2026-08-29 04:34:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 722487f6-3266-3377-83e9-0268dce58b6e | -11.02697 | -57.24078 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20a42155-9a9e-353e-916b-ddc45618b1dd | -11.03825 | -57.21776 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README38.md)
