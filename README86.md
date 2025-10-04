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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76a4eb5d-feca-3559-be12-f3b7f658d5de | -13.35078 | -47.20655 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 768ff9fc-7c74-34a0-bc8d-ee068ada185d | -11.70146 | -47.50875 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ea6e3ea6-80bd-35d5-a4c5-913422a1da45 | -11.82166 | -45.04731 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b91dd280-6621-37cd-a6c8-21003c53cb47 | -13.27256 | -46.47463 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c476ca5-b64d-3bb9-8279-cd87e0fc686d | -14.70647 | -48.19697 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a507cfcb-f827-394c-97f1-4ccf01a8f75c | -13.99717 | -48.19746 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ef18f8a-fdf8-352e-af8e-57ab46398102 | -11.74098 | -54.72935 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17c53054-b2c1-3998-8801-b53d1c0bf2e0 | -13.34393 | -47.22585 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f61e678-0004-387e-a87f-537911381eba | -12.72368 | -48.56126 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e62f984-5d78-31cc-95c1-df311246e1b9 | -11.88516 | -44.99206 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7665f9eb-b9c5-3a35-aa6d-e8b0145616c2 | -14.24082 | -46.09785 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 3c592d65-95bf-3f48-9a14-830d12d6f731 | -11.96688 | -51.47717 | 2025-10-04 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af318dc7-b9b2-31ce-804c-00fe4f686a59 | -9.90618 | -43.74152 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 443efdd3-5e57-3266-88c5-6cdca055d953 | -12.70705 | -48.56716 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 33f68f10-3a5a-3d2b-9c87-1d80b451e7fa | -12.10799 | -43.44807 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 925366b1-a6d6-3638-93bc-aaa893c37a5b | -12.72506 | -48.5761 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f0242d4-2263-39a3-8777-32e928dadf7f | -9.96247 | -48.77415 | 2025-10-04 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33cf3b6a-2cc8-3f9f-9edf-5419ea4b96d6 | -13.32902 | -48.11073 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2843ad3-46dc-3e5d-9ed5-c6dc3b60b92a | -13.93407 | -48.17071 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6c623eb4-52ca-3d35-b3df-794e0491022d | -13.56198 | -44.09579 | 2025-10-04 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aa00ac1-2cf9-3888-b50d-b3502b39d196 | -14.19893 | -46.06807 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6dbb3bad-c7e8-357d-b934-703283bf5424 | -15.3128 | -46.27978 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2ce2162-3325-34c6-a9cb-a193c26cfb18 | -11.10585 | -47.75019 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bd36872-6235-305f-9b51-5b9ae874a9c4 | -9.4578 | -45.53587 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae414419-29bb-32b0-ba20-d51a53765289 | -8.70821 | -47.98589 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 97c8e030-ef0f-352a-845f-b1d781bed50a | -14.44213 | -46.38605 | 2025-10-04 04:14:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43a83f9c-bbf3-3b1c-abc1-46186c3f814c | -13.31727 | -48.11323 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 930f99e1-b4a2-366f-b21b-50cd1db2396d | -14.9164 | -48.35118 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 166770af-df8a-3e5b-88c7-67f3556e2045 | -11.42675 | -43.48505 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07ab8099-667c-308d-ad50-06f307c6a1a4 | -13.74047 | -48.09604 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1620400a-cb0a-3bcc-bfe6-d17d2b08f29b | -8.89062 | -47.60184 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f854cc6-7c84-37f0-86ee-d5c7dc67da53 | -12.03743 | -45.20671 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 509ab8df-b01d-3312-b564-12df8513d17c | -14.91818 | -46.88078 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43bde9ce-d834-34d9-a1fc-ccdcb9d94eab | -11.96142 | -51.48093 | 2025-10-04 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d8fdc0f-c4e5-35f3-9a8d-c35c91b9a995 | -9.10891 | -44.39797 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f624b70-e0b5-3c0b-a4be-e9f253e214c4 | -13.97206 | -48.12424 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6909e85b-64ac-3c81-a294-ab470f53265b | -10.27907 | -44.34603 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd0c26f5-05c5-3c31-945e-0ec3b988c265 | -11.91181 | -46.38117 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9733f1a-94bf-31f8-9528-a0b70f79c9a0 | -14.89464 | -48.34707 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 357d75ea-e85f-3d8d-a62c-c326c0e5b6ff | -13.17202 | -47.88555 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab8a81eb-3124-324a-9cf2-fb60b94f6174 | -8.52903 | -47.21532 | 2025-10-04 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dac90f8-b3ec-38d5-95e5-779608194ed0 | -13.38491 | -47.28384 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dbc0adb-1fa7-39f4-923d-9063d83e0211 | -13.20975 | -47.82069 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d22ac59f-c537-3ea9-ab2c-9e46f5b9056a | -11.49388 | -44.99267 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16bc1e84-d642-3fc6-b0d4-8d553a477852 | -7.73335 | -46.29866 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce802b83-2983-324c-967e-3f6012e9eabe | -9.91172 | -43.79246 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cbc7ec56-ceb2-3018-a24d-dcf1b5653763 | -14.50138 | -48.42697 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6307d4e5-342d-3536-9459-dfb78169dc1b | -9.95369 | -43.65556 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c4c4186-afda-362c-8467-de15340c6204 | -9.33735 | -45.77954 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| de0369b5-9cb1-3b64-a3ab-d12236274b97 | -14.6028 | -46.72998 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a5c7b1e-37fc-3735-b55a-7b7721e9fc3a | -9.91004 | -43.73856 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1a55f674-61a0-3534-8592-c50d44559b4e | -13.2898 | -47.83729 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 5a59e8e1-d8be-3aa1-8f13-18fd5f4bc273 | -10.86018 | -43.17786 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ee96ccd-47b7-35de-b61c-8f78187e8bb7 | -11.20883 | -54.9896 | 2025-10-04 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 300d03ac-53d1-31cc-873f-b80d538fd54b | -8.61912 | -54.97243 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de8215a2-c020-39a4-a0ec-768ce6f8b9e3 | -14.6288 | -48.23346 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11591ec7-6c51-3fc5-8362-cfcdb34cf6b6 | -12.03467 | -45.20258 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9110c642-71c0-3a45-813f-233068f8823e | -9.93711 | -50.23721 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 465e11a5-a13c-3155-b567-165c71122158 | -14.36209 | -43.83799 | 2025-10-04 04:14:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb254233-b75f-3bcf-9d8f-6f935837849f | -13.69359 | -47.34677 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c983e45-73a9-3d91-8f2e-7d1df86f9425 | -13.73885 | -47.95321 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 799a258c-2641-3aeb-890a-690064d5c9a1 | -11.11285 | -47.89873 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b070431-68d6-34ec-be93-33c5eebba7ea | -13.5641 | -47.29701 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5016642f-2fd7-335c-8441-259ed8ad436d | -8.58191 | -44.79831 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fe6c145a-84c5-343a-9f09-6df80175016b | -12.92084 | -46.91795 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 433c6360-ff1e-358a-8bcd-564fa39b7b40 | -11.88344 | -45.00286 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c228852e-70d3-3a1d-8864-83c56912fdc2 | -11.49891 | -43.50009 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59f42443-9c97-3db3-9429-f5c74182f01a | -11.13485 | -47.86022 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1b75954-5e9f-3dbc-9e1f-e7fd1eecbc37 | -11.92655 | -46.3564 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0bf0d04a-3813-3dc5-b729-2a01606ee70b | -15.31587 | -46.3031 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 995edd2c-a7f5-3dac-8f01-f99f19216a72 | -14.63961 | -48.2381 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71fcb692-ed0a-3d03-97ae-8c1b883f4009 | -11.83172 | -44.92125 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79437880-4c10-31f6-a542-a1011761365f | -13.51828 | -47.2472 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0a74f7e-7fd4-3974-8bb5-f880731740ad | -11.07863 | -47.88892 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6ae75fd-3ee8-39e1-9ca7-89908acb3003 | -13.25857 | -47.23753 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 807650b7-53ac-3d52-968f-502dfbfc6c1b | -12.2144 | -47.78188 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d4751cd-563f-3f7a-bdcd-7f58303419cc | -11.50488 | -45.0092 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb74e61f-f56b-3f30-b3e7-a51a3e3e8699 | -11.92529 | -46.36397 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8ae7680d-ef5d-3e35-9ba7-9bcd94a0e51e | -13.13277 | -47.83092 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d5bdca8-c791-3a30-b001-8d9074f32181 | -11.78732 | -46.81817 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 34c2da55-711d-3dca-93e8-f23bdae9d8bc | -11.44502 | -43.49884 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c98479f-418e-3414-a156-14178af77aab | -8.84214 | -46.84729 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7d5de28-0706-3d9e-8736-d8b71656f187 | -11.11309 | -47.8752 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f44c4a0c-5901-3f61-9691-210a056a4d05 | -13.32757 | -47.79083 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bab2edcb-868b-3374-84ce-50349bd9336d | -13.3318 | -47.58057 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 707f8be6-e32b-3f29-8b83-b3086b437bcd | -14.45624 | -46.34256 | 2025-10-04 04:14:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ebd94a1-48ff-30df-adab-f4844cb54413 | -13.3219 | -47.18515 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58dfbb69-0bb6-3857-8544-d9c2d84fc67d | -11.12811 | -47.19775 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e25ee8-fae2-3e53-a80f-fcb69a0c1a78 | -13.31962 | -47.6096 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2617d829-05fd-329a-8bc4-008b0f49438f | -9.12014 | -40.13199 | 2025-10-04 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c65b646e-ff2b-3b3d-899d-0bafdc5df102 | -11.07261 | -47.72166 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 912edab8-6f80-33af-bd9f-80227b20c77f | -8.89254 | -45.02198 | 2025-10-04 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41af2fd6-d797-3f8f-b9c3-0e0b666c7d08 | -9.90786 | -43.79541 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7251fbbd-eabe-3425-8f01-7a545ea89aff | -8.13344 | -44.08217 | 2025-10-04 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9ddc29c-b2d9-329b-b129-4e09f566d55d | -11.7923 | -47.92303 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00a848b8-580f-3b07-8650-42b234ca5a28 | -10.19145 | -45.48798 | 2025-10-04 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67f44903-ad4e-3818-93dc-08f9af4912cd | -14.98326 | -46.84819 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b3f14fb-d428-3978-8b53-3a0bd7265292 | -13.57741 | -47.28225 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fbcfc71-b6d9-3add-a889-91c1481711e4 | -13.12905 | -47.80907 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1a3c886-26f4-3357-81f8-de18cfefb28b | -11.2481 | -47.7897 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README87.md)
