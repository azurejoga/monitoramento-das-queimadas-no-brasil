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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ff90dca-a517-3a6b-8f23-bacc50a2f1a4 | -12.48621 | -53.83795 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdc1f7c1-c6f3-38cb-8f0a-41eb21682742 | -14.99899 | -50.06809 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c35e7a6-9cf9-3272-a04f-b380ca27c14f | -12.89184 | -56.93608 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1999d83-1ba0-3f82-b20f-52caa2c76b25 | -11.88608 | -50.60665 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c3138bd-3d3d-32bb-b409-fff7dc9e3fdc | -12.24467 | -50.14395 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3b43cc-e6ce-37a3-ba24-aeb8f6e9a43e | -14.55262 | -48.06885 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f66bc8d-bd87-381f-810f-ad5d1d0497df | -12.50581 | -48.06605 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23ba62ef-1893-3dcd-b944-6a93531c9412 | -11.65473 | -54.53112 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6ce178a-8637-3277-86a4-23b875a4cd51 | -15.30142 | -52.75229 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c63ca8f5-1a6d-3706-8c1e-d314a8a5f22e | -12.60636 | -57.00026 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f2bd2ff-6a7e-3332-9376-734ead5c03f4 | -12.97416 | -54.77042 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a711907b-2713-3b86-ae63-f2ac442e9843 | -11.61688 | -47.77645 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e8bd3025-9b62-3156-9e5a-df7e6b74eade | -11.67287 | -57.34367 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 54151862-a729-3fb9-860b-043894afcd9c | -12.89488 | -56.94104 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8d68315c-e85a-36ee-a65c-e983c74f2056 | -13.44106 | -46.94109 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96b29f02-75d0-3169-8484-fe2cebb65b6a | -12.89791 | -56.94599 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 60f552fd-1cd2-3284-8cd1-ccca4f7bd2de | -8.44342 | -70.13791 | 2025-09-04 05:18:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d07e88b1-46c3-31c6-a613-62e3d12dba51 | -15.30441 | -52.76981 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7980cd9d-73f5-3cbf-b6cb-0c67918ab00d | -14.53561 | -48.07808 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0983937-645a-3ec9-9b1a-86eb646a2167 | -15.60619 | -52.8856 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 323d3c0a-ba4a-362e-b833-eb2911de943d | -12.91455 | -57.00968 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45e9fa46-e3ed-3230-87ea-a9ed225ce211 | -15.98184 | -55.95884 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 05fb4aa1-77d6-3c13-aaf8-939ff12c4ed7 | -12.87392 | -48.0179 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e087f2-c7ee-3143-a7a2-469f11192f4a | -11.73774 | -47.75686 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6bb10499-69e7-3531-bf3e-c00306cac073 | -13.74218 | -46.94753 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f0953e6-59c9-3397-9a87-908b4c25fab7 | -15.47188 | -53.01598 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 512bddd7-f724-3c08-af64-528ca4b145b3 | -15.40826 | -55.94006 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9171ec59-e660-3105-a884-be967f90926d | -15.03258 | -50.08916 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38ecb07e-2e82-3240-9b73-101a1c12e008 | -16.31412 | -52.95469 | 2025-09-04 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27851bf1-5aa8-37cc-8445-de71ba52379f | -12.60938 | -57.00517 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17ab49da-072a-385f-a5db-02873e5ba4c6 | -11.67879 | -57.35291 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8a611d5-e4fd-3ca4-b231-346c9ec97794 | -15.59994 | -52.8961 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff183f54-b299-3249-8544-bd949efd956b | -12.90158 | -56.94655 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b4ba3e5d-ee48-3949-a12d-951c1c9040de | -14.56307 | -48.07228 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e1d3ed4-c4c3-3c8f-ae0d-9b96db12858c | -16.31778 | -52.9663 | 2025-09-04 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53245533-e4a0-3d66-bcd2-be07ba415b2d | -12.8912 | -56.94046 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fdd525d0-a2b0-31b7-a234-8b74de9bacc3 | -11.95362 | -51.34117 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e4c74c34-be41-34bb-92e7-8d68d30e9d73 | -15.78706 | -48.19202 | 2025-09-04 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4229686-0413-3f62-bba6-0df7fc50d26c | -11.60256 | -47.78549 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35219899-f88e-38ac-8b7d-5cf9b69e93f6 | -13.44791 | -46.94347 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c36a2fe-93aa-3cad-8eac-df3ea4d274d7 | -14.29957 | -53.09175 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98fdd08c-2164-3687-b26c-502a94d88f21 | -11.84963 | -51.49353 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02392b26-ca45-31d4-a8a4-955c46c8ed34 | -11.58613 | -52.16226 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cac7014-3006-3849-aad7-b614a3c323d7 | -11.86867 | -51.55051 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57f5e374-4296-3ac8-a1e2-c99e3f9bb91a | -15.04224 | -50.05616 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52364077-5767-3a2e-96f1-843f6f462bfd | -15.00901 | -50.03107 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e7a73ba-9be6-370d-841f-9355dd5c155d | -11.21314 | -55.08619 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f5fcbea-cba0-3e45-927f-fca1d793eaa5 | -12.49837 | -53.84873 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c24acdae-bc84-38d5-a4b9-6a49d728dec2 | -15.54641 | -48.40925 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4774e623-a1c8-350d-bc49-7b1b2690b78c | -12.95997 | -48.06974 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84dc84a1-6f24-3c89-bea7-bc1754c18788 | -11.20156 | -55.02328 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 565beb8f-0719-3f55-a030-c447e0dd35a8 | -11.73837 | -47.75152 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35ff3da2-718f-329c-98bd-870498828283 | -15.04804 | -50.05792 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ca17904-6a80-37fa-9839-7c5772f6ed85 | -13.73623 | -46.91866 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 784a6586-9800-32bd-9b0e-0b3119c98393 | -11.31567 | -55.22497 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d4a77e3-f0a8-3323-8f85-e421f9d3a866 | -11.59924 | -47.75718 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2e24e2a-6c2d-31a2-96fd-15a2ec7e7a4d | -11.19753 | -55.02269 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00cc1d06-f702-3748-bb2c-d3a8c2448c67 | -15.0049 | -50.06879 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dfbf107-5e93-322e-a17e-86f43d788027 | -14.28932 | -53.09558 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cacef0b0-3d59-31cf-846c-3cd9e772abf2 | -12.64718 | -57.00184 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d8f388-0838-31da-ab49-dee20a0d2947 | -14.57649 | -54.56063 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e98adbc-3b1b-3c1f-a701-ffd2448e8da1 | -15.78371 | -48.19188 | 2025-09-04 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7831d27-841d-3585-82c3-e4e7266b17d5 | -12.96887 | -54.77777 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed21efb1-8b96-35d3-b19e-47d64643cada | -12.23284 | -50.14643 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac2e498a-5a54-32dc-b5f0-a7a6cdf43a2c | -11.88135 | -51.53315 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b76003a0-fc07-35b5-8421-c4179d941c5a | -15.06102 | -50.04908 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89b20a70-e892-306b-9d56-5fdb037e6a16 | -14.20086 | -48.09223 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86908023-8cf6-3e7d-9fd8-fcaa531549c9 | -11.63928 | -52.19369 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 139921b0-9304-3fea-b300-4c32d72afa65 | -15.01303 | -50.04916 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49c37abd-9217-3587-88a6-59ea8da2b553 | -14.28919 | -53.09637 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14d29c08-43e0-3765-9628-e86bf6aba14c | -14.56794 | -48.05146 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b424dc4e-4b30-3ec8-9b7e-4e9984da3731 | -15.1706 | -52.35422 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5302ac2f-0fc3-3aae-bb6b-ec39fadca2ea | -12.89733 | -48.03827 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e085d17f-f9bd-3c0f-930d-10262e80b843 | -11.63436 | -52.19309 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee494637-d70c-3680-94ad-87b7d60b8203 | -15.02686 | -48.10623 | 2025-09-04 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00b19103-5dab-3173-a455-45f30d5cfd66 | -13.26679 | -51.84916 | 2025-09-04 05:18:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2db57411-5e8f-3cc1-a538-d0d51d55d9c7 | -12.23758 | -50.15499 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dbc1d9c-787a-3706-9a7b-8262e9678bf6 | -14.53617 | -48.0725 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 217c2712-0fad-3cf6-b48b-f059f33746f2 | -15.40873 | -55.93661 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e683628-8a8b-32ca-aa47-1d77e60fbb7a | -14.90899 | -49.62572 | 2025-09-04 05:18:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dc1aff3-5bf7-3f44-a263-c5c9cf33aed8 | -11.19905 | -55.01188 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43d011fb-51b3-392a-be1f-75b085cb4e2f | -15.18112 | -52.35283 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 790c413f-c340-3c5a-afec-b56cc082caf1 | -15.00259 | -50.03485 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09faf4e8-1f33-3471-a2c9-0f95c3334426 | -13.95465 | -53.97934 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e133a75-496a-3374-b454-927f06415ad4 | -12.98615 | -48.06973 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76b0d400-4c34-3062-8dc4-0d57553cd734 | -12.89855 | -56.94161 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aa44f5fb-020a-3bea-9393-8ed66216e9e4 | -15.2471 | -53.79819 | 2025-09-04 05:18:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 072989c3-9ac8-3ba1-8a11-908e9b7f8351 | -15.15287 | -52.37292 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 913e64f7-7ffd-346b-bd5b-030e05fb8cf0 | -10.14876 | -68.53532 | 2025-09-04 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8422f8f4-8285-311b-8577-3b6bc84dd747 | -13.10037 | -57.11903 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f8716e4-4faa-3df7-b272-cf1b96d36029 | -15.04719 | -50.06552 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d939a998-6a26-38b0-95e7-40d5c6ab7be5 | -13.44222 | -46.92987 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e5df1da-81b9-3fe9-b382-a254e35a9270 | -12.48234 | -53.83288 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6de3e13e-24fb-3a6c-a822-a7b4f4a687af | -12.99811 | -48.08134 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6900138-3397-3c32-8cd0-91d3ceb6cb13 | -14.90243 | -49.62938 | 2025-09-04 05:18:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ebfb3b1-6074-33f4-9bfc-4d4b4fa25aba | -15.41276 | -55.93724 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e8fe052-7be2-301b-8a87-ae222719e6e5 | -12.90094 | -56.95094 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76e664fa-a599-3ecc-ac28-30bd119e68bb | -15.5475 | -48.4145 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfd1f703-f536-36c1-8c30-c8516c1ba761 | -15.03245 | -48.11737 | 2025-09-04 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9f333fb-80eb-375f-868e-cc1b05fd40f5 | -12.46387 | -48.08693 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README88.md)
