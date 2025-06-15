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
| 2d6c50bd-6b72-33f1-8841-7795d29bbba1 | -10.96195 | -49.56945 | 2025-06-15 05:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59a35e8b-7cbb-3145-8d58-f4e4c4c8ae27 | -12.68599 | -52.39639 | 2025-06-15 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 373ed6ec-e5a6-3a3b-87cb-6a8a795c97af | -11.00692 | -55.07496 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 448e4a31-bf51-3701-9dc8-a90ee2e08ec5 | -11.01122 | -55.07116 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f19f56a6-4472-3bf3-8419-1c4a3d916bc5 | -13.92581 | -54.62515 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 654bb889-2f69-35eb-ae41-4558a248282d | -13.91089 | -54.61772 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 715f3f63-3790-3066-96bb-7a8064d2ef9a | -10.85342 | -53.78994 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84e3c967-e0ed-3e92-8b40-446160039cf7 | -10.62919 | -49.42482 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55bf818e-d180-3168-94fe-4d456d3901f7 | -13.92465 | -54.60432 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 947f9229-7937-3724-b062-cedc58859e3c | -13.91827 | -54.65227 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b29b9ddd-8d8c-3ebe-829b-e337f80301e9 | -10.6638 | -49.36656 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9dfa2710-6eb4-3b7b-be6b-34cc57aabc56 | -10.65937 | -49.35927 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c43b298a-f4e8-30cf-96f2-80d64d3a2205 | -13.89986 | -54.61367 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c8af955-601b-36d6-95c0-30861f99791a | -13.92191 | -54.62461 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| c38e06a0-c8ee-3007-8f8b-3f0e4ef116ee | -12.98108 | -48.64247 | 2025-06-15 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c66088aa-3bf1-3bed-8821-67db8315bd5c | -13.92074 | -54.60379 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f50e113b-3fe2-3a14-a9b7-54d90f4420b5 | -13.94593 | -54.44694 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0e71c12-b7c2-3ba9-af55-3099ed097cbb | -11.00931 | -55.08415 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfe97f84-ca01-35f2-84dd-2881883f04ac | -15.4155 | -47.86446 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 867b39fa-ffdb-38f9-a175-7fdddaa15ae4 | -12.69042 | -52.397 | 2025-06-15 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8270315-a892-392e-8d40-931c59a3892f | -13.92716 | -54.61782 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ea53faa-57f0-387f-aff7-22c3c324e011 | -11.88314 | -54.68299 | 2025-06-15 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac12735c-c212-355d-a86a-1d4fd204fdc9 | -10.9612 | -49.5691 | 2025-06-15 05:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc94026d-cd60-3df5-b67d-b870d9315680 | -12.47468 | -58.4698 | 2025-06-15 05:14:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d85c9e19-cc68-3fd6-b415-02cf20f43052 | -10.09427 | -52.73919 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8846fdc7-e8e5-3475-b3f4-66c57bcbb483 | -13.91299 | -54.60538 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 97f239b3-950b-3a2c-8872-3a7f65fe9b37 | -10.94073 | -56.84325 | 2025-06-15 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89e36b23-2d47-315b-91b0-256243eba1c2 | -10.08954 | -52.7424 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 15a37322-1e41-30f0-9eaa-217d230f26a8 | -14.21903 | -57.40169 | 2025-06-15 05:14:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b9e20e3-ea06-3426-be11-f1409d623da6 | -12.69425 | -52.40208 | 2025-06-15 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 42a5a1c5-ff85-325e-9c9b-62d7368e391b | -10.63402 | -49.42892 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a59e9d70-2726-3044-9453-2c786715da8b | -11.18599 | -44.48294 | 2025-06-15 05:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d229d65-70c7-3784-9064-1f9674fd92f0 | -13.91479 | -54.61835 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c6e68f8-9976-394f-a275-c5f198d27be1 | -10.65893 | -49.36256 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cc3e5f32-69f8-38af-81f6-392d11ac5529 | -13.91801 | -54.62399 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| e684c48b-d985-361f-a30f-a10ce0d26f6f | -15.39736 | -47.87645 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d82cb7b5-82ad-3707-9968-659668c68cf3 | -10.50968 | -53.58119 | 2025-06-15 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7eb12084-6b4c-3119-b7a1-54020e1e069f | -13.90909 | -54.60474 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae13dbd6-3c78-3677-8a83-087eba0475d0 | -14.83438 | -48.43917 | 2025-06-15 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3c2e1d3a-de2e-3321-8876-451821558eb9 | -13.91224 | -54.60769 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 771a8f1d-6f2f-3f0d-89f8-f4d2af79e489 | -10.24251 | -52.23607 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84ea41b9-541e-3e3a-8319-5ef03cb168d3 | -13.91683 | -54.6032 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86e168e0-01b2-3d1c-bdb9-2ed778ab9414 | -10.07648 | -52.74438 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58b62d2b-ec46-33a6-a6ab-0558414761d4 | -10.91068 | -54.75971 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 322c8cfc-4b36-3a32-967e-065f4a70b918 | -11.00995 | -55.07983 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b982843f-f5e5-3df6-af95-7897ee6dfbbb | -10.27943 | -47.61158 | 2025-06-15 05:14:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab35ff7f-5900-3341-95af-b75dc01282fe | -11.57025 | -47.87152 | 2025-06-15 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 053d9580-7d11-3091-9ccf-b4edc3b256ba | -10.65784 | -49.36235 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6d92a5fc-a961-3e63-8b93-21719cce1926 | -10.91684 | -54.76978 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cdedb29-e57d-3d01-b93d-9cc172a58821 | -11.04684 | -62.5843 | 2025-06-15 05:14:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bae48fb-5c84-3d20-b05d-d0dc1426288b | -10.91505 | -54.75582 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88535722-f33e-3c92-9e68-cd56642421f6 | -11.00868 | -55.08846 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98c34451-0596-3ada-91f9-daf2ac8761d3 | -11.18517 | -44.4903 | 2025-06-15 05:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a31cfb4-8c21-3ee5-bf82-f81faaaf8ae3 | -10.65825 | -49.35907 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66baf88f-c6e9-3d74-b297-cf3c91f60b5d | -13.91156 | -54.61274 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7907bc38-acb5-3c88-b4e0-ffd042f66117 | -13.92325 | -54.6173 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| abee4fc4-0027-383d-9fcb-e7b40b042fe0 | -13.92123 | -54.62959 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73b8ecbd-2aec-361c-a8da-3cc29ac79dd2 | -14.83525 | -48.43129 | 2025-06-15 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0cd6e1b-9936-39f3-8eee-51692ad05dc6 | -12.4819 | -58.46733 | 2025-06-15 05:14:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df8df9b6-df3e-30ad-b8fb-46fcc845f647 | -15.39784 | -47.87215 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b77596f8-63fb-3bfb-bdf1-2c1027f128d2 | -15.41448 | -47.87421 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0cb2f79-36b2-301c-a5e3-2335d90d3972 | -15.40351 | -47.87764 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4470abca-f7d7-393b-9721-3d40c9ef6be8 | -16.28887 | -52.93497 | 2025-06-15 05:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3250b15-026c-3c27-ab5e-2b596600ebc6 | -13.91762 | -54.60086 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81cf239d-1e2f-3647-9f9c-338f2d4d6c31 | -10.17555 | -52.61986 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a5ac9e1-d11c-3c07-9a21-d3c702279375 | -15.40726 | -47.88329 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c79a056-6e5e-3e31-a165-dd902b12464a | -10.71665 | -46.55992 | 2025-06-15 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a45defe8-0c48-3ad8-9c8e-70bc4b923bee | -13.91404 | -54.62602 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5f2f9557-d47c-307c-bdd7-940ac04368ca | -13.91864 | -54.6217 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 25009dc4-f852-351d-82da-742066b7c595 | -10.09009 | -52.73861 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03e869af-9794-304e-84a5-fa140e63af0f | -10.66273 | -49.36638 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27504aa5-3930-3752-9eba-a072b45260ba | -15.63891 | -49.37525 | 2025-06-15 05:14:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd4916ce-741e-3b74-9b87-f883aa2655a0 | -13.91936 | -54.61403 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a10b8909-39e6-3e53-8259-7eeb776d25d0 | -10.56846 | -52.01419 | 2025-06-15 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d8a4a0b-5fc1-36cb-9c24-17dc278fef73 | -14.83482 | -48.43514 | 2025-06-15 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68fdc409-fb55-32c3-836a-2e716d1bfd45 | -14.82977 | -48.42622 | 2025-06-15 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35e7fa29-7ec8-36f1-9ada-9a0ad559249b | -10.09497 | -52.73819 | 2025-06-15 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8c657b1-deb0-33a3-a56a-fbf0f29c1c08 | -13.91326 | -54.65904 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64c8525c-b875-3fc3-9f3d-ca8ce68f4c5a | -13.91529 | -54.64406 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fbacd79-3c3e-3540-85ff-c8087763e592 | -19.27327 | -55.1486 | 2025-06-15 05:16:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4965a0b1-2e6a-3304-ad0f-bd7b1b4740f1 | -19.26921 | -55.14795 | 2025-06-15 05:16:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6bd0ae7-3359-3780-8711-c381240d3915 | -19.69665 | -54.61544 | 2025-06-15 05:16:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f91932fb-63ad-33ef-86e5-7a6e615724f1 | -13.9251 | -54.627 | 2025-06-15 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 64fbc229-e6f9-3e91-8dc1-6035da942f85 | -13.9254 | -54.6063 | 2025-06-15 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 2849ddf0-6286-36e9-a19a-8739aae52a89 | -13.9062 | -54.6084 | 2025-06-15 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 68d61aec-99f9-3880-aa89-76d9835b2f79 | -13.9059 | -54.6291 | 2025-06-15 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7d70c880-5535-3049-9a7c-5fc0c9f3fe37 | -13.9251 | -54.627 | 2025-06-15 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c905e5b0-9360-3293-bbda-8771f43c4085 | -13.9254 | -54.6063 | 2025-06-15 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| e152caba-2092-39cf-be9f-8af8e980c121 | -13.9062 | -54.6084 | 2025-06-15 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 0a28303e-eea5-3da5-bbdf-19ec25ae9cdb | -13.9059 | -54.6291 | 2025-06-15 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 65899de2-c316-36f1-bf1f-d6ba6f029647 | -10.07903 | -52.74855 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1186948-ce52-352c-949a-1686d5683d1c | -10.23649 | -52.23219 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e966b0c-5ede-33a6-b03f-3ba7615c72b8 | -10.09021 | -52.73746 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1fbafc2-69bd-3aaa-9947-f7f0e9690913 | -10.08961 | -52.74248 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c2a926b-f477-3f1f-a67b-360b654598ea | -10.09294 | -52.74004 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 524906bf-2cbb-3a99-a52a-450761a2843a | -10.09654 | -52.73818 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b8d5f82-d846-3e0c-9945-8a9f8a12b2d4 | -10.07273 | -52.74766 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64d7911d-c9ba-385d-8ac5-02ac9ff60169 | -10.23577 | -52.23314 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bbb325b-2e11-3984-8eb9-7e49c7e7dfee | -10.0923 | -52.74504 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a703960-2dd0-3e81-bb4a-88d2aac6d684 | -10.23512 | -52.23871 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README15.md)
