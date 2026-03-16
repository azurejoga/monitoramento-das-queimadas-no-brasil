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
| d46a907b-a96f-37d2-a72d-59641df91aaf | 1.98721 | -61.43901 | 2026-03-16 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b165b7be-8de4-39b0-afbe-38a9fe9b02e4 | 1.10893 | -60.39035 | 2026-03-16 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8cca457-a92c-386a-affa-40bddfeaaa2e | 1.64495 | -60.2952 | 2026-03-16 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 748325d6-a2af-3dd7-904e-2446533dc7ea | 2.20551 | -59.80843 | 2026-03-16 05:48:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a613c630-fac9-3284-ac2b-cde1daf22864 | 1.12152 | -59.58376 | 2026-03-16 05:48:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54af0527-e46d-3f87-b018-36747471eab6 | -11.96048 | -58.74956 | 2026-03-16 05:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 065a2299-f064-34b0-9e1d-4c05fa7ecacf | -11.95764 | -58.74601 | 2026-03-16 05:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 680ae6c2-b4fe-3807-ae54-0ea7b53bade1 | -11.95722 | -58.74952 | 2026-03-16 05:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8be7cbae-3d80-3ef1-8340-0871afb95dbb | -11.95506 | -58.74898 | 2026-03-16 05:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36c74efa-a077-3214-b95b-73ef9fbdbc68 | 2.32052 | -60.24074 | 2026-03-16 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba397823-44a5-319d-aceb-d9454e2d7dcd | 0.90666 | -60.29823 | 2026-03-16 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5068e11d-2503-3466-9f23-bdc83f00febb | 2.30824 | -60.24152 | 2026-03-16 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c751ad3f-6aee-31ec-be20-961849fdc76a | 1.11808 | -59.58786 | 2026-03-16 06:18:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67dedab0-06a9-3688-903d-1fda886808ef | 3.13388 | -60.79348 | 2026-03-16 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f59b260-ab7a-3dc4-b852-3b243304fba1 | 1.12448 | -59.58682 | 2026-03-16 06:18:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7b24901-bce2-3943-90bf-c67db520aae6 | 3.13254 | -60.78547 | 2026-03-16 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 484608fa-70e4-35f1-9a6f-f33bd88a844b | 3.12812 | -60.79445 | 2026-03-16 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63f39fd9-d6a8-3652-8a55-8a2033d2859c | 3.13454 | -60.79747 | 2026-03-16 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18358b7a-be3d-3ecb-a15b-2530aa2ef264 | 3.12879 | -60.79844 | 2026-03-16 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca8bf640-bdf0-32ee-bd0e-64fbcf730e80 | 0.90741 | -60.30291 | 2026-03-16 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00f6f92d-28db-3a68-b0aa-c433bdd7f3a2 | 2.25101 | -60.20084 | 2026-03-16 06:18:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b84aa469-0190-32ef-87c7-01c14f76e503 | 2.31385 | -60.24251 | 2026-03-16 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6fce6fa-ba75-3d25-9f69-5dd05eac4c21 | 1.21113 | -60.16577 | 2026-03-16 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f634c598-854e-3708-ab86-b75110b03789 | 2.31434 | -60.24092 | 2026-03-16 06:18:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 682df130-8ad5-3dfe-bca1-a71c1dbf4d01 | 3.1383 | -60.78452 | 2026-03-16 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46786818-49f0-3913-82a3-7af9b371f620 | 3.13521 | -60.80146 | 2026-03-16 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26296ed3-96b5-3eea-82df-a38ab540aea2 | 1.21034 | -60.16087 | 2026-03-16 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b99382fc-5eff-39a4-a769-d0246182ef08 | -10.42396 | -51.04472 | 2026-03-16 12:29:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b99463d5-9ea6-3254-a879-e6604d7fc377 | -23.03489 | -52.67133 | 2026-03-16 12:32:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 6f941014-c699-3c9a-9b35-3e1017b35c30 | -23.02994 | -52.67643 | 2026-03-16 12:32:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |


