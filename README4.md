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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a2aed51-709b-383d-8d7c-9936ba38db09 | -2.63946 | -45.67126 | 2025-12-18 04:08:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5fdf08e-356a-37f9-857f-ce3803e31247 | -7.45969 | -35.09174 | 2025-12-18 04:08:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f2a39ac3-d45c-35d5-8afe-bbf999e6253c | -5.4127 | -37.05042 | 2025-12-18 04:08:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 29c85694-a40c-3bd7-bf4a-fd81622c90b3 | -10.07884 | -36.14727 | 2025-12-18 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| dbd4681d-3958-33aa-859d-b93ad71d6075 | -10.08262 | -36.15218 | 2025-12-18 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 09e6a3ef-3cc1-3277-824b-29e6faaedb99 | -2.19998 | -46.61063 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98651492-18ce-316e-be9b-44189cae4f79 | -3.18845 | -50.23325 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75b0b4b2-a9f3-3978-8a6e-11b9e103d882 | -10.08324 | -36.14787 | 2025-12-18 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 19582bd8-91c5-3a35-86b8-30339ff44642 | -2.20686 | -46.59531 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44cab86e-b2ce-3a04-a5e6-f2a11b50a248 | -1.95211 | -48.46228 | 2025-12-18 04:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f84f6d24-9b27-3fbf-83d2-7833929e1739 | -10.62019 | -37.13675 | 2025-12-18 04:08:00 | NOAA-20 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b70b5759-3162-3d13-a749-4f31ae38a47a | -2.79333 | -51.40909 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb85af8a-a812-3ec4-bcac-6dedb8315948 | -2.20064 | -46.60657 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cccc3731-4eee-3ec0-88d0-7c06a06b748d | -2.1158 | -45.35101 | 2025-12-18 04:08:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2b3884a-ab09-3aba-9fed-f003952e5a2e | -8.34386 | -38.91265 | 2025-12-18 04:08:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| feda751a-5193-3e3c-a5ba-d76c5c54d6a8 | -2.25915 | -47.86325 | 2025-12-18 04:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edf20557-885f-3a0c-b891-d7e2a219434b | -2.46464 | -48.11594 | 2025-12-18 04:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3c4943f-ce20-33f7-93dd-927224fafd9f | -3.18512 | -50.23242 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fa61599-7c3f-32ac-9326-3667a6367ada | -8.34447 | -38.90858 | 2025-12-18 04:08:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 758997c8-4725-3954-8a92-d5bdd855d601 | -10.07871 | -36.15044 | 2025-12-18 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 397811c1-07ce-3804-9dcd-82035b50b8fe | -2.63492 | -45.67409 | 2025-12-18 04:08:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53cd4847-2a0f-3155-bf0a-6fc7a6c1e2d6 | -7.78425 | -37.97621 | 2025-12-18 04:08:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82d70b83-b0aa-377a-8bb8-3cef173cfefa | -3.18306 | -50.2323 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d6e00bb-f555-399a-9666-0e21bdcc4ed9 | -2.78747 | -51.40807 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e46fa998-4cbf-38ea-84ed-6921e9ef0e3d | -2.93192 | -48.22651 | 2025-12-18 04:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2d85685-0c2e-3c18-a049-ef15e465e811 | -3.15487 | -48.59914 | 2025-12-18 04:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45d74cbb-8d1e-3217-8875-5a9f7600dd72 | -2.63891 | -45.67473 | 2025-12-18 04:08:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18c31962-aebc-32b6-8262-e06d22564318 | -2.66705 | -46.90139 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20e46477-9d66-3ec8-b78d-19f75949cdf5 | -2.66104 | -46.90219 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67edc256-a072-3dfd-9547-4b69b094c1b6 | -9.02823 | -35.64328 | 2025-12-18 04:08:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 277d3aab-a37c-3082-9b7d-0e8d52306910 | -3.15004 | -48.59835 | 2025-12-18 04:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66259885-d4d1-38c6-b20b-a614d34cd32a | -7.68727 | -38.36207 | 2025-12-18 04:08:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 152df6e0-1c11-3e11-9a96-91e985456841 | -3.78178 | -47.74632 | 2025-12-18 04:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c53304a1-631b-39f8-8d3a-843bb67b118f | -2.0205 | -48.58154 | 2025-12-18 04:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 116db08d-5112-3fad-8844-280b93154eb1 | -2.19636 | -46.60589 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d60a1128-361d-3ed9-9e59-6318a00b3db9 | -4.07518 | -43.69093 | 2025-12-18 04:08:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc198641-8614-3b4f-8b8d-4da397218fc7 | -2.20918 | -46.60802 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 73922437-3213-366c-9b90-db099e548901 | -2.17968 | -45.78663 | 2025-12-18 04:08:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 635c235a-2d32-3538-ac8b-8fa475cdf6fd | -2.17563 | -45.78597 | 2025-12-18 04:08:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 47cfabb1-0c33-3378-ad75-bf97b132836e | -2.32494 | -45.76688 | 2025-12-18 04:08:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec4f48ac-5bce-360b-83ef-0ec45099f5b4 | -1.39996 | -51.74278 | 2025-12-18 04:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 146199fb-919a-3e1c-9e29-ede418cce8bf | -2.63547 | -45.67063 | 2025-12-18 04:08:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba3d7401-24e1-3c5b-9f47-7e58ef529c00 | -9.64942 | -42.9704 | 2025-12-18 04:08:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8820f267-dcfe-3c2d-8877-5d9e2160f809 | -2.66269 | -46.90084 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08ec84f4-5dc9-379b-bd4c-fbdef8db0121 | -2.20557 | -46.60323 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1ca2f9e8-f9dd-34a9-83b4-163c2fcf5b0f | -3.18789 | -50.23667 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42ff0aae-2702-3602-99a0-555be0344a9a | -2.66479 | -46.88827 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cde2209e-fa32-371b-badf-9afbea613ef5 | -2.93109 | -48.23156 | 2025-12-18 04:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf0bcd16-c909-3c01-996f-97ffa49ed1dd | -8.95573 | -35.70671 | 2025-12-18 04:08:00 | NOAA-20 | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fb06d4cd-b008-3316-a4b0-33995203b087 | -3.18454 | -50.23582 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1e35b07-767c-3d1e-9b0b-9a80e4cd0e6e | -2.20852 | -46.61208 | 2025-12-18 04:08:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 50bc15cf-f435-3ea4-b299-21604b5685e3 | -9.11464 | -40.19653 | 2025-12-18 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3cb0e374-c042-34cf-8ab6-d2e0bfaa3284 | -2.20426 | -46.61132 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae6237ae-57de-3175-9c52-841a846fd0d3 | -2.46771 | -48.11984 | 2025-12-18 04:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1095f371-51f5-3bbf-baf5-1cf980e3681c | -3.15151 | -48.59636 | 2025-12-18 04:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea3d58a6-09f4-31dc-9883-801679b5ba35 | -2.66775 | -46.89716 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10195543-8a22-3e9b-8b5f-d0bbcb31a84e | -9.03272 | -35.64385 | 2025-12-18 04:08:00 | NOAA-20 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 11d4703c-e400-30cf-a480-3b4317c9e0b9 | -9.0276 | -35.64779 | 2025-12-18 04:08:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 51d6b753-5e94-3cad-a496-d1ceb20e77ba | -2.2013 | -46.60255 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 92fac9b1-4134-3242-8fa4-b35c6af35879 | -2.4685 | -48.12185 | 2025-12-18 04:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6a40c5c-0c6f-30f3-a5b4-585ef00690da | -5.07972 | -37.64471 | 2025-12-18 04:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ebc59933-07ae-3440-a20c-f4d04d5bd980 | -7.81622 | -35.24402 | 2025-12-18 04:08:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 74a71fec-89b2-3d6a-8504-fbed69b8e4d9 | -10.07929 | -36.14613 | 2025-12-18 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 54319878-5e9f-3c77-8ac4-fd8629704e9b | -10.0831 | -36.15105 | 2025-12-18 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ff7fcdfc-1e23-31d3-aff9-f00e04541db0 | -2.66608 | -46.89841 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9c3d4c50-bee4-3f00-aaf1-a45923b20bab | -2.67531 | -51.68087 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632c128a-49b1-3292-8b22-c028c683e5ed | -2.3709 | -51.92033 | 2025-12-18 04:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5b20421-be37-31e1-9c24-b37bc78c3bcc | -1.62021 | -48.55637 | 2025-12-18 04:08:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2c8b685-1b8d-3583-8a48-22a33064a1e9 | -2.37017 | -51.92152 | 2025-12-18 04:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dc96d5f-d704-35d5-9c48-6c498288332a | -14.39087 | -43.97914 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38bc90d0-c9b5-3ad4-9976-921f31ff0d19 | -10.61214 | -44.65123 | 2025-12-18 04:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa774ecb-b49e-3bf1-9695-ac6a4970b10f | -11.76311 | -43.30777 | 2025-12-18 04:10:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a04c63e-91b4-322d-b9bb-d7cb70c788cb | -15.50598 | -51.85564 | 2025-12-18 04:10:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 589dd699-c5d4-37fd-b741-99159cd194f6 | -14.38595 | -43.96732 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 284045ea-d140-324c-9fba-326bb8f8e98c | -14.38812 | -43.97501 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5822b5fc-be92-3fbd-be40-b37e3c24ca83 | -15.1148 | -52.95996 | 2025-12-18 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9616af02-0cc6-3555-b018-9dc3e2ae1155 | -15.5049 | -51.8612 | 2025-12-18 04:10:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 940754af-3ecd-322c-9d73-a05a5d7b8a43 | -15.11544 | -52.95666 | 2025-12-18 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aa1da74-abcf-30c7-b90f-2b1ac9126c6a | -16.79328 | -40.30871 | 2025-12-18 04:10:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 84cf9225-ed49-30f9-8d24-e9e23b5dcfbb | -11.48749 | -41.50901 | 2025-12-18 04:10:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43ee3ebe-949c-32be-a846-ecd97f0d006f | -14.95359 | -42.77652 | 2025-12-18 04:10:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3af53ea2-0e40-3f77-8b2c-3a0b61c4021d | -15.37049 | -43.17204 | 2025-12-18 04:10:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcd15c6c-9d83-33ca-ace0-babd4044a073 | -15.50973 | -51.86224 | 2025-12-18 04:10:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7620855-86b3-37b9-b159-db993d13dd2f | -14.39419 | -43.9797 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cd7ab7d-5404-3c87-80f3-165435799672 | -12.95197 | -41.02995 | 2025-12-18 04:10:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5a2e0e95-1ef7-3429-b0ab-bdf104b02aa0 | -15.51082 | -51.85667 | 2025-12-18 04:10:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e46b887-60f9-34df-9b6c-386110308b5d | -11.96742 | -44.49783 | 2025-12-18 04:10:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbb28d0c-6243-3702-9023-dde827e9e529 | -13.01579 | -43.97335 | 2025-12-18 04:10:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b76dbd82-8b3a-33a7-a616-f0deaa0de570 | -14.39362 | -43.98326 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fb8101b-9b34-3bd9-9337-611dbef62122 | -15.46139 | -39.1594 | 2025-12-18 04:10:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| afd6b1fa-a5c3-3676-b6f2-5229c752ab60 | -11.76255 | -43.31129 | 2025-12-18 04:10:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 343c139a-613e-36e4-90c6-0c88b4d58b71 | -17.02774 | -41.1731 | 2025-12-18 04:10:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 764a41d1-3e15-3e6c-80e3-8cefb168957d | -14.38926 | -43.96788 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4db68f50-9d67-3696-aea0-389f0913319f | -14.38984 | -43.96432 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 164a6e36-f02d-37ab-874e-2e6642c601be | -14.38755 | -43.97858 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d30bf49d-99c0-3ff1-8c2d-f43e691597e4 | -14.3903 | -43.9827 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2335cecd-edf8-3273-8b32-b53e3b80ff54 | -11.96803 | -44.49415 | 2025-12-18 04:10:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ab0208a-c9b1-3bbf-aaf7-4e7457a928f6 | -12.40392 | -40.41002 | 2025-12-18 04:10:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d54301e-6e20-32bd-8a0e-1ace3a9aa7ff | -14.39258 | -43.96844 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aca5f585-9ae3-3379-8b69-64057e3e8024 | -14.39201 | -43.97201 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
