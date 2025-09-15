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
| 5bd7d53a-a4d3-372a-b5da-ce786aa9474f | 4.31451 | -60.96569 | 2025-09-15 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 643d86d6-ada9-38fb-8e0a-c025cf7183ff | -3.3868 | -50.15025 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21f7d58-0767-3d92-8bdc-cf0aaae2484a | -3.91542 | -47.71258 | 2025-09-15 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 655aeb21-dde8-361a-b37d-92086ab67f6e | -3.22141 | -47.63323 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee5fa212-a0f8-3e73-b299-9da2efe9c866 | -1.95439 | -48.11486 | 2025-09-15 04:46:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70e4efb5-e18b-3dd8-8b95-9e82b9dc5983 | -2.26383 | -47.88164 | 2025-09-15 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6f64b4b-8eda-377c-aa19-c8993818c244 | -3.55385 | -49.04258 | 2025-09-15 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e3f92d3-f029-3790-9d5f-839019d65c08 | -3.72605 | -51.18749 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5995e665-c932-34c8-98f9-9ff35f664960 | -1.22913 | -54.12447 | 2025-09-15 04:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb3a9f99-3de3-305f-909a-7cad1e6434c3 | -3.41944 | -47.60844 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d95f2cf-4e67-369a-b952-8446603ad94a | 4.316 | -60.6542 | 2025-09-15 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e75b3070-9b3e-3043-afbd-2f007f615fb8 | -3.48673 | -52.8097 | 2025-09-15 04:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5c5d90b-e88c-3931-9889-d6cf0c220f43 | -3.8329 | -50.77282 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826ba525-daa7-3555-836e-2bd78ad724ee | -2.79246 | -48.64236 | 2025-09-15 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 895a3cda-dc4e-378d-bdcf-1eaba8d418bd | -4.17574 | -48.56524 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87c03e4d-fcec-3f6e-bee8-f27f452aa18d | -3.38325 | -50.28068 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d798446-ceb3-3fce-8cc2-f1dd75f0a0f1 | -2.9178 | -49.56215 | 2025-09-15 04:46:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbcdf4ba-8607-3583-9b4d-101a33ce8969 | -2.26166 | -47.85019 | 2025-09-15 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 861cb937-729c-32c0-b95e-7b7a7aaf5568 | -2.80949 | -48.62273 | 2025-09-15 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d31f400-4196-3eec-af95-d57ded034f13 | -3.24852 | -50.80902 | 2025-09-15 04:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8d3e543-e0da-325b-a4ea-8dd1b020628a | 4.31584 | -60.65268 | 2025-09-15 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a73ebbee-644d-37dd-9ad2-2c50d4b29007 | -2.26323 | -47.88544 | 2025-09-15 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24471d1e-8a23-3215-88b5-fdf6ada53be4 | -4.17918 | -48.56578 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b7af5b-133a-3c48-8575-06e23a111c58 | -2.81289 | -48.62326 | 2025-09-15 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9a8dae6-0fd4-3980-851c-078b96841220 | -3.3826 | -50.24164 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1a7363e-146d-312d-878b-3cdd942c0e2b | -3.07511 | -48.82277 | 2025-09-15 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1739d28f-6d9c-3f64-9dbb-3206ff236bf6 | -3.89326 | -42.51603 | 2025-09-15 04:46:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e81f03bd-36b4-3c4e-adc2-2a40d13b1205 | -3.35687 | -51.59629 | 2025-09-15 04:46:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 283e80ea-1fc2-3a92-996e-fb6f5287e777 | 4.31666 | -60.65851 | 2025-09-15 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dafd2567-9503-349a-86ae-8e505d4ff2c5 | -2.25878 | -47.84583 | 2025-09-15 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1474a100-c363-351e-9428-089fae8ab47e | -3.52156 | -49.24911 | 2025-09-15 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff53d66a-746f-3625-9475-22bfdff7a6fb | -3.43392 | -47.45583 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b816609-e6d8-36a4-8e2b-7ef67d21f0b0 | -3.21746 | -47.12701 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec2e9c53-4bfd-3342-ae84-c7b63bb06406 | -2.12213 | -56.86428 | 2025-09-15 04:46:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9af2542c-d1b2-3621-bb23-8a0040a52871 | -3.43142 | -47.45801 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecad1712-f521-3f4a-a151-7434357d06c3 | -1.89261 | -54.61799 | 2025-09-15 04:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65df8e7d-e00e-3f7d-ba65-5d51f00096a0 | -3.59723 | -47.51189 | 2025-09-15 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b61697c1-56c5-3205-aaf4-b60f431a77ec | -3.91186 | -47.71206 | 2025-09-15 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a418f5db-cd9e-35fc-a27f-7c9c0b57249d | -4.174 | -48.57644 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4becdf4-9cfd-3c0e-827b-01706cff3371 | -1.89342 | -54.61297 | 2025-09-15 04:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72d41f83-1408-38f7-801a-bb12f6035cf3 | -3.82957 | -50.7723 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b22b3e5-5b05-301e-9b55-69372d79fc44 | -3.22495 | -47.63377 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b7b1d13-f43c-3ea3-88f2-609606afa61d | -3.41994 | -50.11292 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0969de6c-c9ab-36ec-a45d-8a09371ce803 | 4.3094 | -60.97709 | 2025-09-15 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b05ef1a-4053-3c6a-b183-c3d658b2f0b8 | -4.1786 | -48.56952 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 337cf0c6-0bbf-3262-b95b-546bda90c932 | -3.47045 | -50.54189 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 165f0ff6-dc04-37a4-b629-8a26b7651abc | -3.39012 | -50.15077 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b601377f-b69f-32d3-ac3c-6355ae7b4a4e | -3.22109 | -47.12758 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1aef194-e23b-367e-8b70-9442eb6a9648 | -4.17516 | -48.56897 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 48936b89-4cf3-3a33-8c97-946f463b5cc0 | -2.94789 | -49.34842 | 2025-09-15 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a46a9fa-e7f7-384e-bd05-b0d0c94099c2 | -3.41662 | -50.1124 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b48ad8fe-6b7c-30a1-9dfb-a5c188384468 | -3.83012 | -50.76884 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6c13c1f-54b8-3988-98b8-fdb0e0c80f51 | -7.67898 | -44.48542 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2bacdcd-77f9-3a2d-9bd5-0d3aec550077 | -6.43091 | -42.63707 | 2025-09-15 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4a6464b-de0c-3b93-92a9-590955639e41 | -5.93869 | -43.23707 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cdb26520-1912-3529-9cf3-ccdfe7cdf8ae | -6.16506 | -41.20263 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 81727e0d-70ee-3e76-b987-3e406d832698 | -5.74637 | -43.92305 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2724bcbf-7840-30e6-b5cc-582c88fbe69c | -7.38818 | -49.98531 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb7ff508-57d0-39ee-9c8b-4855241e855b | -8.62818 | -45.72892 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2043f490-44f0-3ca3-b87d-e84b0c03c16c | -7.48701 | -44.6849 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb463c94-5b43-3c49-a680-a5b861aa0e03 | -10.73293 | -44.77163 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 445d4a26-c1cb-316d-a69b-0fb4b083dceb | -3.65436 | -54.06237 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| edf6e041-d2ba-33c1-852c-9e354749ae22 | -6.34507 | -43.16329 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 168d6b46-721a-364e-a5b7-4898cf790a79 | -8.91536 | -45.47626 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cdac8cfa-f4c5-3c0c-ba87-07993d2efec3 | -9.004 | -47.05127 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 17aabf7d-188c-35b8-a4c0-ef37cbc75705 | -7.51256 | -44.70863 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5baf56cd-76fb-3dbc-b424-132dacfdcfcc | -8.89153 | -45.45338 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f330a088-7648-316d-96ed-1d069f88d896 | -5.85638 | -48.15706 | 2025-09-15 04:49:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09940d2e-dbc6-3cec-98ad-987ed494e982 | -8.95309 | -46.03854 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5211704-d55f-3e87-aa57-6b80be0af99d | -8.59819 | -46.35472 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4bd768d-5996-36c3-8440-2b536f615df6 | -4.18898 | -50.42506 | 2025-09-15 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f5829f0-0e58-31c8-b791-2a0351bbfbf2 | -8.42116 | -47.22372 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7741102b-0493-3c43-8062-737dfaced430 | -7.70412 | -50.35231 | 2025-09-15 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f656a306-9999-3f69-8b86-712bcb47a14c | -7.69967 | -48.86532 | 2025-09-15 04:49:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77694921-7e18-37af-bd2b-5f1220784705 | -8.62977 | -46.36691 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82feb569-c14b-3bcb-a8f3-b1d2685f984c | -5.95573 | -42.79627 | 2025-09-15 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| da5ae62e-1dbb-371e-b356-27577346c5ce | -8.50281 | -51.16526 | 2025-09-15 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b057142-fe1f-30df-af56-1924126bfc5c | -5.4778 | -44.68848 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83fed087-6cfd-36cf-a898-7140bc492aeb | -10.1617 | -46.14592 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 467ba751-cfb5-373e-bb15-73b222af00bc | -8.60383 | -46.34449 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90883b48-8f60-37c4-9c3a-ddf5351b6b92 | -7.21601 | -44.39957 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 887bc036-f024-352d-ad93-0b762008b75d | -6.98046 | -44.54105 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c243c7c7-a2f2-3719-b1a0-96fbce7be80b | -9.12415 | -46.94529 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d31bb19-4eff-38b6-b0c4-47a889d4ba3f | -7.85851 | -46.12273 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 850e1022-7b45-3b1d-89c5-a31751007009 | -6.76449 | -44.72728 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48a3d592-f011-391e-909c-8bd4eebdae8b | -8.91794 | -45.4896 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 44e68986-9576-312e-9ac9-9ec19f98877e | -6.77329 | -44.72905 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7392a919-76f1-33c0-af98-ffdf9939c994 | -7.51319 | -44.70407 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b78a0def-6bd9-3e86-8b2f-9f909df1495d | -7.86987 | -43.58011 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a01c0775-14d5-3a29-9a86-0877b6a2927a | -7.51425 | -44.36738 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d31b5e01-4c05-33ed-96a7-c25806adb788 | -10.6383 | -44.20821 | 2025-09-15 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f05f694-8727-39ed-98ea-ade0e1f997b3 | -8.96571 | -46.21847 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62102bf8-bd65-3de5-958b-a790b8b558f1 | -3.9631 | -52.19556 | 2025-09-15 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1f2b52-76a7-349f-ac93-c6c9f1e9eca5 | -6.44075 | -44.08566 | 2025-09-15 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c0dd51b-6724-3dc5-a4d0-cfa01f1e1d12 | -8.16673 | -46.78201 | 2025-09-15 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cefdc3a-eb2d-342b-b9da-298f5c0c6876 | -6.13883 | -55.78574 | 2025-09-15 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fb84b0c-1fa6-371e-b8a3-357b9365b11e | -10.74288 | -44.76865 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02b02f32-7dae-34c2-ac29-10cb7df7c60d | -7.36008 | -44.29939 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6bd4972a-216b-3f21-9166-4b815f293989 | -7.87551 | -43.57547 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| af6d4534-1d77-3039-a934-91f62ea31610 | -8.11485 | -50.15974 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README39.md)
