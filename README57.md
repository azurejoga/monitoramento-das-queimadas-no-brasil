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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 295c84bd-05b1-36a7-89d3-7e862e8f809e | -14.5378 | -53.14323 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13c64d85-8c82-37af-abf9-af47c4d3cad7 | -14.56587 | -54.54762 | 2025-09-05 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71eb1ce7-0a5d-30b8-941a-9dc052e53eb9 | -15.63236 | -52.8921 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9273572c-7bef-347d-8def-5c7760d00302 | -15.15076 | -52.37518 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 348521ca-8df3-35bd-ab5c-a1ce59d8f0c8 | -15.20201 | -52.37246 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86513fd2-e760-3769-a335-088bc2862778 | -15.57278 | -50.34025 | 2025-09-05 04:59:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21d211a2-e3d1-3695-b78f-9ef8a38157c2 | -15.136 | -52.34459 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37c38d7d-e74f-30b3-a391-a818360f1be3 | -15.21454 | -52.36473 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7db40eb-9534-3bae-b70c-6ecede9d4624 | -14.98492 | -50.06862 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 433cb613-86b8-3088-a775-567b68f78aa9 | -15.18698 | -51.17007 | 2025-09-05 04:59:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2946704f-9f2f-3c27-89d1-c3bb6a0d4292 | -15.70949 | -53.60001 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7651475-348a-3be0-a84a-bb7abf24f3fa | -15.04097 | -50.04283 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dab3316-6c4d-35ce-8092-a576cc1965b6 | -14.98336 | -50.08064 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42da18bc-6e33-36fd-b743-bd9f89840680 | -14.75472 | -47.49369 | 2025-09-05 04:59:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 340d1a7e-e134-348b-8eaa-ee0517540b49 | -15.18016 | -52.39243 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79ce15a5-0049-369a-ab38-931975e4d7db | -14.56415 | -54.53595 | 2025-09-05 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6da3a17-0b56-375c-ba81-facd82db5cc9 | -15.74364 | -53.6137 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f99aee7-7bb2-3205-b369-23632a09b962 | -15.75648 | -53.64803 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13a48f47-991d-3e27-889f-26fc57651579 | -14.97954 | -50.07625 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb8add77-ccfd-386c-ade0-aacc5a3161b6 | -15.22379 | -52.38049 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d878faa0-1658-3eba-bdc8-07018ee2552d | -15.20399 | -52.35819 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed46f515-0f3c-3faa-a950-3d1cba1d359d | -15.54462 | -48.40603 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6a27dec-9fcc-36fa-9bef-d770f3fef5a1 | -15.16308 | -52.39572 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97c9b9af-47b8-3c07-b964-27443089c164 | -14.13294 | -51.71445 | 2025-09-05 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22828293-feb1-3d3f-afab-2154b52eb91b | -14.58845 | -52.18035 | 2025-09-05 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dedf95f-1df8-3091-9319-979951cfd433 | -15.78475 | -48.70659 | 2025-09-05 04:59:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f961ffce-9c80-335b-9990-7b5104f4715c | -15.05685 | -50.07283 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d347cb9-fdab-3285-adfd-d33002e85324 | -15.21256 | -52.37893 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76c9d0be-498e-39eb-8527-fb15e56bb321 | -15.21828 | -52.36529 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 589dc480-b9f2-36da-b8c4-d91f4623a919 | -15.76002 | -53.64853 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcc73099-bd08-350f-b5f9-3f053d53e6a5 | -15.04268 | -50.04616 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66cc1e48-b01f-3d21-8fb5-2a0cf5cb939f | -14.98716 | -50.08503 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fd30bc9-b0da-3f6a-a202-63eb3cce1c9b | -14.75507 | -47.49079 | 2025-09-05 04:59:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44987833-9305-316e-9007-272bd4be3fdd | -14.9844 | -50.07264 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe4d06c6-8f0e-33f5-821c-456d69ca0fa9 | -16.45428 | -45.26233 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b58dd97-9a56-3b5f-b4dd-77cd82f8559e | -15.15936 | -52.39511 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf69dfea-bfb9-39f9-9c84-bdea86be88b8 | -16.46031 | -45.263 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb0202f4-3a3e-3ab5-977e-07d1cc323b18 | -15.74234 | -53.62057 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69dc4072-89c7-3708-af0e-a1530819516d | -15.75649 | -53.67317 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 064c3f67-75ef-3519-a264-229cb6f9a479 | -15.71476 | -53.61344 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72cb512e-6187-3d50-8b85-d1a73c9daa21 | -15.6116 | -52.90665 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5df33382-bef4-33bd-a082-1c8e263fbb08 | -16.29611 | -45.69306 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c279f91d-f341-3ef0-a597-351fca7ea869 | -15.75472 | -53.66035 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8994724-7b3d-359e-bfd4-6e3ba16bd53c | -14.81147 | -48.31831 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b023a085-8cd3-3156-b371-deff7a85ecd5 | -15.61223 | -52.90226 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78f48145-88fd-34cb-930c-e9fed904b550 | -14.13158 | -51.72417 | 2025-09-05 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ae58021-17fe-33c6-85ed-568ade60f64c | -14.57911 | -48.02574 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e91135e-8de0-33b1-a748-2905b59e4c84 | -15.13282 | -52.34002 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ac27e32-df4d-3528-904a-f3bfd43d864b | -15.74351 | -53.61231 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00bdc33f-9a84-3130-a7b4-440891485891 | -15.15209 | -53.51197 | 2025-09-05 04:59:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b20e3e7-49da-3c68-8246-91273b442ad2 | -16.30103 | -45.69163 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 081c7521-3d20-3954-b7aa-8d3561682db1 | -15.75296 | -53.67266 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac43cf68-6007-31f6-a9d6-0f9d184890cc | -15.44543 | -53.00003 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b07a4cc3-1c62-3289-a4d3-8ddea61742a1 | -15.57526 | -50.32088 | 2025-09-05 04:59:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6740974-51cc-3957-a288-93aa16029e11 | -15.04422 | -50.08423 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 607c9cd0-40d2-33af-97ac-f5b916221f21 | -15.71062 | -53.61709 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bc50d85-1168-3478-bece-827bf163e5aa | -16.29657 | -45.68882 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49ed9883-694e-3c8e-b4ba-d570be703fae | -15.20135 | -52.37719 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0484870d-7245-3141-ae28-8b9a8a3bc397 | -14.13677 | -51.71502 | 2025-09-05 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b108fd5e-3f4d-372f-8755-40881843e76c | -15.54815 | -48.4174 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49056856-869f-3eac-ae2a-84ee0ee3c921 | -15.15628 | -52.38995 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f8eace5-8bdd-3ea1-9001-acf3b81a1857 | -15.60858 | -52.9017 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09ca6cdb-129a-38e1-b2b2-6603da51b883 | -15.63231 | -52.89016 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79890005-8b8a-3ed1-ab1e-9da91933dad8 | -14.5636 | -54.53966 | 2025-09-05 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c1abe40-6e7c-3dec-a30c-2e3f2cccdd3f | -14.54137 | -53.14379 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c85cfaab-675e-3d39-8b52-4ea8debe9c24 | -14.81562 | -48.32444 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31226327-4feb-355d-8148-d12c1600bbd0 | -15.0626 | -50.0622 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b4ec3b0d-45d2-384d-8d65-e6581a61b51d | -14.52172 | -53.07669 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e4c20af-d41b-3fa4-880b-e895006d4221 | -15.31567 | -52.7337 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc92f0de-572f-3b16-8afe-96e394f18770 | -15.73833 | -53.62531 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7debd2ff-9ee1-352d-ac36-8eff620d45c2 | -15.15723 | -52.39282 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4197ca2-97d6-3f18-b410-d8bc2265992a | -15.54751 | -48.42257 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 422a6294-5313-39a9-98a2-14b91317bd12 | -14.56643 | -48.08938 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c16e8526-1c34-394b-9c8e-b60d9b134673 | -15.452 | -53.03191 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df9b6f02-af47-392b-b6b7-796c8297870b | -13.94295 | -53.99115 | 2025-09-05 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7443243f-b53a-349e-acb4-af2e468d6717 | -15.32177 | -52.74349 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07408fd3-7a96-32af-9488-e6359d305597 | -15.14855 | -53.51147 | 2025-09-05 04:59:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 893a5f53-08cf-3918-aa59-449eae089a02 | -15.05781 | -50.06531 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fc71bc5-397c-37e5-9923-b0204d4ca5c1 | -15.22754 | -52.38098 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d69ee11f-1912-35c5-bd0c-165fbda3996b | -15.74013 | -53.61304 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52a268b2-07cd-30f3-a672-aa4b698dbdd1 | -16.30061 | -45.69584 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42d7bd89-282f-3a39-9847-1a0d2eed9ae4 | -15.71122 | -53.61295 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3aa1c489-a98e-334f-a499-09a052b46e42 | -14.54259 | -53.05849 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 992e3b39-057f-316d-9acb-1fac730a5124 | -15.22687 | -52.38575 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2888b36-792d-3451-bc6f-54851dbf41b1 | -15.71183 | -53.6088 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2067795-1630-3c8d-a9ac-fb865ce1e7b0 | -15.04671 | -50.08362 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63d56fc5-d979-3e8c-87c9-8eea2af6f291 | -14.48439 | -53.04256 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0c5945a-ff23-39fd-80f4-fbc09cc57071 | -16.45477 | -45.25769 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3004d391-97bd-3539-9941-d86727d4cbf0 | -15.62866 | -52.88955 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c0959da-cca0-3e88-a4fe-1b2c5bd9cbbd | -14.48344 | -54.02484 | 2025-09-05 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6feda6b1-20d6-3e49-9d8c-d99efef0099e | -14.73946 | -47.49129 | 2025-09-05 04:59:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ddb3251-57e2-3ee2-803f-0072005216fc | -15.61588 | -52.90288 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4b9ca75a-2c8e-318a-a859-971d4e7b0169 | -15.53851 | -48.41567 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2d7b7be-e014-31f8-b512-9e1e00064162 | -14.43844 | -52.97947 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ecb36505-99e1-3d66-a8e0-3db8eca887b8 | -13.11001 | -57.12019 | 2025-09-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 339d8d1d-3205-3b80-98ca-bc34abdfbbd6 | -14.97901 | -50.08037 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 603fcbec-5135-3b1e-bf98-788c49a66002 | -15.05319 | -50.10157 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf8f584-4945-3dba-adff-e2ba3780fc11 | -15.72834 | -53.61948 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90eef18d-5261-3105-9fa9-20831ac58281 | -15.1322 | -52.34446 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1beaffab-e031-3354-9047-d40d73f98f46 | -15.71304 | -53.60044 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README58.md)
