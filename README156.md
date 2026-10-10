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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94fa84ec-b5f8-3880-bacd-d59d1ec3728e | -10.9093 | -44.8438 | 2026-10-10 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b0b15845-0b59-39c6-97d3-a02ab86f5f10 | -15.0233 | -41.362 | 2026-10-10 13:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 157.5 |
| c22762f3-57bd-371c-bee6-7d4385206ff1 | -11.1873 | -45.3347 | 2026-10-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 5b073638-279f-3636-921a-221ebeb39c47 | -11.3865 | -50.8891 | 2026-10-10 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 733bc32b-2a10-3ebf-9196-d2c1b9594c9a | -12.1861 | -48.4124 | 2026-10-10 13:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b7fca966-26de-3353-8892-0fa78c300d6b | -11.5793 | -43.6965 | 2026-10-10 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 10813853-81eb-3ac2-bcdc-6e26ca4d3df0 | -11.8307 | -43.5866 | 2026-10-10 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 7fe61b25-7eab-3f1e-9dab-56c11bea535c | -9.9395 | -44.81 | 2026-10-10 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e22cb376-d829-369e-8d79-fd006eafab05 | -11.5985 | -43.6935 | 2026-10-10 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 622d3147-9e68-3189-9721-b7f7db597da2 | -11.8595 | -47.3694 | 2026-10-10 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 91e6a914-315d-3b1e-9cf8-3ec91fc671e0 | -11.0183 | -44.0382 | 2026-10-10 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 0ae5924a-54ca-3c6f-aa36-3100e2a64379 | -11.0937 | -44.0975 | 2026-10-10 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 60e97c9d-2759-3afa-a80a-b3ba60dfd000 | -11.598 | -43.7172 | 2026-10-10 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.9 |
| aa3fe258-7143-3d5a-917e-44960ed029ce | -10.9388 | -45.3687 | 2026-10-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| cbb7f91a-e669-388a-91bd-352ead9de618 | -10.473 | -47.1887 | 2026-10-10 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c8efda02-700c-385f-b9f8-5f636864ae64 | -15.5633 | -48.5041 | 2026-10-10 13:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e3ccdb0d-763e-3af6-9d6c-7bddb923c1f7 | 2.727 | -60.2586 | 2026-10-10 13:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 10a400f5-72fa-37d7-81fc-c1e0b805c9d2 | -12.3708 | -46.5789 | 2026-10-10 13:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 84622164-4589-331d-abb0-f7d78d28e77d | -9.9208 | -44.7893 | 2026-10-10 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 2f28f7fe-fb66-3322-abdb-482ce0532a09 | -11.0379 | -44.012 | 2026-10-10 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 038f2d5e-07d6-349b-be13-eea047642605 | -11.3374 | -46.6322 | 2026-10-10 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 04efc5b2-70c3-3cf3-88c6-97e42437221e | -10.4914 | -47.231 | 2026-10-10 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4a14a869-26ca-3de7-ae44-255b2e9e6681 | -11.8787 | -47.3668 | 2026-10-10 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 78e2c9b7-b187-3dc9-97f6-6104541890a7 | -11.1876 | -45.3117 | 2026-10-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.6 |
| b2e39653-94ae-33c1-8d42-bec5df5a821e | -11.2068 | -45.3091 | 2026-10-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 61298a3b-9876-3881-81ad-c037be717722 | -9.1924 | -49.7678 | 2026-10-10 13:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 491362d7-39a3-32b9-bd1f-e14a2791b4e0 | -15.043 | -41.3576 | 2026-10-10 13:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 145.2 |
| 926d765d-511d-3952-8efd-88799bb2612e | -9.9398 | -44.7869 | 2026-10-10 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 0a9a37fe-b8d0-358b-b706-5506503b7fbc | 3.0551 | -60.5383 | 2026-10-10 13:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bb07746c-0ac7-3aec-99da-47c461f26ae1 | -10.8909 | -44.8001 | 2026-10-10 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9c4b8645-4543-3379-9133-b3f4375cc3e6 | -12.1627 | -45.3547 | 2026-10-10 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 3bb4a500-7665-3af1-b3bc-aaa62b506960 | -10.8905 | -44.8232 | 2026-10-10 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 004c1eb1-3132-3310-8123-ade1d714a7b6 | -12.1729 | -44.7983 | 2026-10-10 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 93b7b3f8-bfc2-3e29-ae45-b3eee4cb34a4 | -11.3875 | -55.1656 | 2026-10-10 13:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 89b50a6a-4589-30a0-9c83-4213b55c8095 | -11.3183 | -46.6347 | 2026-10-10 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 38d91047-a0bc-3027-a7e2-0253d49fe84b | -11.0933 | -44.1209 | 2026-10-10 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 56d1939c-c6f5-35e4-a404-6b45f9e4cf95 | -13.1639 | -54.3385 | 2026-10-10 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 97f74a18-4ad7-37fe-b35e-6b9228c5c3f5 | -12.1733 | -44.775 | 2026-10-10 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 40616cfe-8f36-354e-ba61-3d23d01d2da5 | -11.7772 | -45.4806 | 2026-10-10 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| b85337da-f0d4-3dfb-aa12-1f559c846d9e | -9.1924 | -49.7678 | 2026-10-10 13:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 9f4594b4-1703-342b-b412-1ced2af002ae | -10.473 | -47.1887 | 2026-10-10 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| da1a9fd7-3ca7-3846-8011-067634f6992f | -9.2057 | -45.7869 | 2026-10-10 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0c8bc196-2a35-3186-874f-82fdf3da2522 | -15.043 | -41.3576 | 2026-10-10 13:30:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 166.8 |
| ef92d1cf-ccaa-3976-bdd2-743e3725ecca | -11.3877 | -55.1452 | 2026-10-10 13:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 442c7b7a-3024-3bb4-9f6e-04b1c0f0afbe | -11.0933 | -44.1209 | 2026-10-10 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 47ecedbc-ce4d-342f-b78d-0cc86faa496a | -11.0379 | -44.012 | 2026-10-10 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| c9dcd6d2-6e4f-3730-9980-94343811a0d9 | 2.727 | -60.2586 | 2026-10-10 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 122.1 |
| af9e4ae3-823b-356d-9294-72eccc2eb4c7 | -12.4837 | -51.2959 | 2026-10-10 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 43d803b7-3f89-398e-9dc7-04bdd059e43d | -10.9093 | -44.8438 | 2026-10-10 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 30b79b5f-e69b-3a03-85b2-77f0343d65c5 | -10.9536 | -50.6805 | 2026-10-10 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6913a579-a4b5-3651-a1fd-b157d932020f | -11.5793 | -43.6965 | 2026-10-10 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 6f9c442d-a5bc-39f5-bc0c-7c6343f13c02 | -10.9533 | -50.7018 | 2026-10-10 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 12eb95a7-3545-370f-9813-17c22cf8f6a1 | -11.3688 | -55.1469 | 2026-10-10 13:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b29743ff-558c-366d-b7c5-7d4631569ede | -11.0187 | -44.0148 | 2026-10-10 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 173993a1-eb66-3f83-9db3-1ad6e18e4d7f | -11.2064 | -45.3321 | 2026-10-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 06100ad6-4f93-3cad-88b1-409ab093fa0b | -11.5985 | -43.6935 | 2026-10-10 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 63794d04-7fb0-3e9e-b80d-1b05fdd7808b | -8.9311 | -45.1355 | 2026-10-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 170c8e21-aabe-3293-ae53-db6ff630d9be | -11.8787 | -47.3668 | 2026-10-10 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 4befbb05-1489-3d88-a642-8db587723218 | -12.1733 | -44.775 | 2026-10-10 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| bd7716f1-793e-3632-bd9d-334f6449f817 | -12.1729 | -44.7983 | 2026-10-10 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| bd4ed1a4-c96b-3353-bc49-88496b752f49 | -11.0183 | -44.0382 | 2026-10-10 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| b4ba0166-18f2-3aa7-bd48-711502f2530c | -11.8307 | -43.5866 | 2026-10-10 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 491ee223-6ce0-335b-8a3e-9b577815cefe | -11.8978 | -47.3642 | 2026-10-10 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e9459002-8499-327b-9e08-3735f444babd | -12.0063 | -43.4402 | 2026-10-10 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| e0c95e45-d72d-3fcb-9373-6830b5d1e6cd | -9.9384 | -44.8791 | 2026-10-10 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 307.0 |
| 037230bd-386f-34ab-9a69-aacc0f663598 | -11.3875 | -55.1656 | 2026-10-10 13:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 7e85d0a8-ae85-3162-80a1-d514731400d2 | -10.4914 | -47.231 | 2026-10-10 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b1c4f70d-2a20-3a23-af1c-ecdfecf8f175 | -9.9381 | -44.9022 | 2026-10-10 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| ffe9abe1-bf33-3853-a141-2767e71a256a | -13.1827 | -54.3571 | 2026-10-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| edc6bbf2-6983-32f3-83f3-5ff8c3d1f719 | -12.1861 | -48.4124 | 2026-10-10 13:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e78ef454-5a03-3e06-8431-51a0eb65dc59 | -12.2508 | -44.7397 | 2026-10-10 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| bfad7d05-7c6f-3bad-8cfc-bafd947e762d | -11.8595 | -47.3694 | 2026-10-10 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 6ba1c3d5-f8ca-388e-bdd3-3c0e0a95663c | -10.8905 | -44.8232 | 2026-10-10 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 3eaee558-9569-3944-a977-847774d2b51b | -11.2068 | -45.3091 | 2026-10-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| ac646f7a-13fb-31ba-a4f2-00f5b9e230b7 | -10.9388 | -45.3687 | 2026-10-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 19d9bb43-d016-33c4-936d-ba8702d47741 | -11.1873 | -45.3347 | 2026-10-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| f0c5d99f-6fee-30c6-b6cc-43d07f37f7fa | -11.2853 | -45.1832 | 2026-10-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| b040c737-2462-378b-b857-363239945c64 | -15.0233 | -41.362 | 2026-10-10 13:30:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 141.4 |
| 5c430b76-36ec-336f-8b65-dc34a2ef207d | -8.8899 | -45.3907 | 2026-10-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| bed3454f-c2a5-334b-b434-437e5f0f4881 | -8.255 | -46.4255 | 2026-10-10 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5db3fe0e-900e-3b62-a35d-d4707f4f4048 | -11.0937 | -44.0975 | 2026-10-10 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 2809f55e-f47f-39b9-924c-24c64514619b | -11.1876 | -45.3117 | 2026-10-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 16ec9d47-99e6-3f76-a2d7-a23149d477b8 | -11.3865 | -50.8891 | 2026-10-10 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 9f1cea19-ee24-36e5-af11-db12a2e01b58 | -10.454 | -47.191 | 2026-10-10 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 72f20563-d037-3171-94ab-ebe9829ac356 | -11.2068 | -45.3091 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 80495c78-3ab3-3067-9a3d-bac1597379fc | -11.8787 | -47.3668 | 2026-10-10 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| a5264e59-5042-3a11-beea-66aa76abc1ac | -11.47 | -43.3824 | 2026-10-10 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 5b781af9-aaa2-3170-8ae9-475f7556efe3 | -12.1733 | -44.775 | 2026-10-10 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 244.6 |
| f525e9c9-2439-34ca-9947-8e75a2b22962 | -9.9384 | -44.8791 | 2026-10-10 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 386.6 |
| 7c1226a8-3b8b-30f0-a236-05b77a1077d6 | -11.1876 | -45.3117 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 3b237d1b-15f0-30ab-9cc7-6fe57dcb81f0 | -15.0233 | -41.362 | 2026-10-10 13:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 146.1 |
| 88206575-7431-390c-b233-897d9274dcdf | -10.4914 | -47.231 | 2026-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b38d537d-23c9-346b-9f22-d2729efa5fe4 | -11.8696 | -43.5568 | 2026-10-10 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 7174d515-81c9-385f-b458-55d49c75813c | -15.043 | -41.3576 | 2026-10-10 13:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 141.0 |
| 420fa052-094c-3c12-9a91-b0b701e4ce53 | -12.2508 | -44.7397 | 2026-10-10 13:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 9fa4094d-5215-3e3a-8afc-74ecb1728cd1 | 2.727 | -60.2586 | 2026-10-10 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 298754c4-5b7a-344c-a8fa-9889a5ed9986 | -14.9757 | -41.6952 | 2026-10-10 13:40:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 129.2 |
| e09c890d-acca-322f-ba1e-8524cd4cb474 | -11.0379 | -44.012 | 2026-10-10 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 27513b03-6130-3551-a0c6-d812a05ae1cc | -10.4147 | -47.2846 | 2026-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 0da2b8aa-3de4-3b1f-95b4-c6d1f4426b1a | -12.0063 | -43.4402 | 2026-10-10 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |


[Clique aqui para ver as próximas entradas](README157.md)
