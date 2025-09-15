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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25a06afa-57fb-32ab-be35-ed96e8dc9625 | -15.79018 | -52.20624 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb3b6b6b-2ea4-39fe-88ab-7c3d1bd3ab8d | -12.12346 | -44.84274 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10efc0dd-9770-3a55-a356-81a468af261a | -11.0772 | -49.71535 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cfc91d4-3f9a-348d-902f-fb1caf64ebe4 | -10.75483 | -50.65437 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffafec56-8f64-3d62-8f56-97fdc3468b6a | -11.80402 | -50.49347 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb336741-d9d5-3b56-8ca5-8ab4365dee8a | -11.85407 | -50.50226 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d0f24e7b-b7e3-3ed8-90d2-f1e98cfd4302 | -11.07709 | -49.73866 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d316499-86d7-3353-8e98-8d0c40e7508e | -10.75387 | -50.64151 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ccefc1c6-b96f-39b1-b5c7-a2ad74257651 | -12.96282 | -48.00031 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f462f59-a6e1-354c-848c-b5588f93e8e0 | -13.77337 | -49.34901 | 2025-09-15 04:21:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52591dda-010b-3f2e-9903-75cce22f0f85 | -10.43021 | -44.84525 | 2025-09-15 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43b7875a-e032-3fb4-b531-79c37728b4d5 | -12.77987 | -47.9775 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3f1c7c4f-75dd-3216-850a-d262c4c73dd2 | -9.87837 | -46.45967 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cb087c6-8ce6-38df-b8bc-151e32ccbf0f | -14.50198 | -47.34913 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0347252-8b34-3af0-884c-6da80e770ee6 | -10.75474 | -50.63636 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| bf8f0c33-7212-31ac-bc6a-790a691a3d3c | -12.003 | -46.66908 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1ef9e1c-7497-320d-bbba-8d2e0ca14134 | -13.61131 | -47.63869 | 2025-09-15 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46f574a6-8627-3fb2-9538-ed13103fb1eb | -10.7495 | -44.77916 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c2430da-d305-3326-95aa-bbcd490d34d8 | -11.07336 | -49.73803 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dbd10e0-d637-3e99-ae46-3abcbe317ff8 | -14.43458 | -43.22578 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a1489a4-ce9f-33e0-8895-fe33a02b46e3 | -14.82634 | -51.62904 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8bb9f73a-5d88-3d60-b7e8-71b101f8e505 | -12.08239 | -44.72882 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 503fc016-7ca3-361b-8aaf-4bbf5cb30ec1 | -11.86452 | -50.52153 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 50e022b1-9df7-39e1-9a2e-aa23ad1b8a6c | -10.09772 | -48.3396 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b0e936f-24f0-3c26-b2c1-8bc351758387 | -14.4582 | -55.96606 | 2025-09-15 04:21:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8d45190-ae2f-308b-a7f3-440cd651b749 | -11.79912 | -44.69571 | 2025-09-15 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf844e54-9ceb-3c0d-b5d0-c877c6390419 | -10.78118 | -45.98131 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bacab4ef-c990-3e14-b0a6-3bd8a4276a0b | -11.84784 | -50.44594 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 011f0429-6f04-3cba-b62e-30b81c59d795 | -12.12005 | -44.8201 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22fbdaf4-65e5-35cd-a96b-073ece727225 | -13.18029 | -47.29 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3140331a-4a99-3d4d-88b7-40fbf33218fb | -14.42247 | -43.20377 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7cbd0af-f6dd-3679-babc-af7d32345b5c | -9.12023 | -46.94161 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca40448a-9791-3dcb-9022-ba518a40c14e | -15.66676 | -52.23957 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a8942d2-0eae-348a-ae39-03ff5c0d685b | -16.41111 | -49.07391 | 2025-09-15 04:21:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6f3c143-2750-3947-8106-29b232d5b766 | -12.00193 | -46.65441 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7422500-295b-3cab-83ed-1f00bd31f225 | -8.5045 | -51.16223 | 2025-09-15 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ded0c09-9902-3706-b801-448a9aaa452a | -10.15622 | -46.14487 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 077eb316-c9ed-39b6-981d-9c1ff921ab86 | -14.24815 | -48.83948 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03ffbd9b-dcc7-3cd4-b265-62f21c4b5c32 | -10.74778 | -44.76807 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae8d1b5f-c1cf-3c46-8541-7de05dc7f837 | -10.17274 | -46.14751 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2877f96f-24b7-3685-a806-77d12c187106 | -11.86664 | -50.532 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8508bb68-da54-3939-810b-c0970a9e3c45 | -10.93556 | -45.49094 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a8b9a7d-8234-3aa8-94d7-22e5105b0d74 | -14.50587 | -47.34609 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15db4309-a084-3ff9-a07c-7f50bd3e854a | -11.2705 | -50.8283 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9106f627-1470-3938-8aac-a07152979814 | -11.79932 | -50.49768 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae10f9d2-a19e-3553-92e6-2d7ad754f74f | -10.76364 | -50.65059 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71ffc9a9-f599-339d-a5ae-0cc8457f2f05 | -16.41451 | -49.07455 | 2025-09-15 04:21:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f95fa658-8859-3af2-ad78-1926a661f76a | -12.09173 | -44.87095 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f27d5c4-5ab1-3ed2-98c7-cdb78af3f0e1 | -16.05875 | -49.97876 | 2025-09-15 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a90fa82e-7a47-361f-8fb3-cc0f59c219e2 | -12.60476 | -45.73694 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9bd0153d-2900-3169-87a7-749a49cb2985 | -12.44421 | -44.7435 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a203613a-c88d-3085-936f-59579acc991e | -10.91093 | -45.56226 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a80c35bc-9463-34f0-b1f2-48cf4c46220a | -10.86284 | -45.45797 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d23c889-fc59-3b09-bc7e-e8a4d1795540 | -10.88103 | -45.47159 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a86bd3dd-3514-3312-91e1-28ebaa6e053f | -10.28781 | -45.36963 | 2025-09-15 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5144d47e-ce56-3b43-9648-29fbbad92d1b | -12.00007 | -47.75425 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7752979b-d7a3-3afd-8e34-7fc6d9aaf8be | -11.46307 | -43.56773 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57eda85b-d2e0-3720-8360-94b6595dd69c | -12.77586 | -47.98072 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f30a865f-bece-348e-aca4-b0e7f3c4e521 | -11.43091 | -43.53138 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15b0e5ff-8509-3963-91ce-d9807f568c80 | -11.844 | -50.44526 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fce535b4-5369-3656-8ff3-d8368d7a848f | -10.76003 | -50.65322 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cab03835-c6a5-3e9b-a9d1-e98e4d6b6e97 | -12.98644 | -47.96214 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd26127a-c06e-3f71-908f-2e60a3e3af85 | -12.04516 | -46.53134 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71428de8-9153-3f77-9528-768d36845e81 | -11.87002 | -50.52526 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d6cb9f0c-19a1-3411-b438-b28ebb3ce83f | -13.95432 | -44.88836 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6079440-c4d5-3dfc-b065-113b8adfb3e1 | -12.24876 | -51.06767 | 2025-09-15 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20b3e7d8-5995-3a2a-b59f-fc6521269b11 | -14.28306 | -46.12003 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d67279e6-39fb-3b20-a06b-7cd9cb5e4eb4 | -11.45175 | -43.55853 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48d28360-a619-34e8-b7b6-b9c7a6700669 | -15.78746 | -52.1983 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7466cd73-19f9-364a-991c-ca24d18ea6b9 | -14.2488 | -48.83559 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b4a0b61-7822-37bb-9dfd-507e8b74e0d8 | -13.61305 | -47.62786 | 2025-09-15 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f322782a-3e9d-3613-8af7-87688fd5ab65 | -15.79152 | -52.19877 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 823aed2e-b679-35e8-a46a-453fbb5672fa | -14.94963 | -46.55986 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc444a1d-151b-37b8-b31d-f984672e2994 | -15.79085 | -52.20253 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f27c89dd-567a-3d31-9edf-8ff42fb94510 | -10.75878 | -50.65505 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a473d40-cb84-375e-bbe7-4031d6c06a03 | -12.1693 | -44.10089 | 2025-09-15 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e460d188-dae2-3868-8fef-b55e7b1a062f | -12.0413 | -46.53432 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9594d36-f7af-389e-a728-80c303fce841 | -14.25768 | -43.20774 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2f31f2a8-0d85-35f6-be0e-c5a85a2fd2cd | -10.89804 | -45.44919 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b02a53da-4084-3478-9688-1718f36f55a0 | -11.24482 | -44.76479 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4706a61-71d4-30d9-a880-cef896186f65 | -15.80033 | -52.19587 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ca39e00-753d-3e93-bd4c-6f9405ec1930 | -12.68596 | -47.73568 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b53d909-d8a0-37e0-b6d2-84c05e027300 | -16.88403 | -45.77774 | 2025-09-15 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de14609c-c509-3344-88ab-9c3a2ebb6a76 | -13.19085 | -47.28807 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 62e38c63-24bc-30c9-908d-c60c45147b63 | -14.46407 | -55.9639 | 2025-09-15 04:21:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 311d17b2-9bac-31d8-b0b5-23b2a0bf86ff | -11.07862 | -49.72959 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4490ec44-41ef-3603-a1c5-b6ca708387df | -12.12231 | -44.8278 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e8807e4-a199-34c9-81a5-ca3b24377667 | -15.79157 | -52.22166 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4867ebd8-244c-378a-8e40-57b78ab6e889 | -14.28582 | -46.12411 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99423385-3fe5-3f5f-91a8-a335fad826a0 | -12.76136 | -48.70815 | 2025-09-15 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3690c77-8f81-3e93-8742-b8d3d3852900 | -15.08288 | -52.47806 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 626513f6-1b71-3e92-887e-208d27816527 | -12.00631 | -46.66961 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 01f72b6d-eb0c-3e10-8ce4-40302532f89c | -11.07797 | -49.71084 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bb86f07-f2c7-31e0-9646-ecc5d265008e | -11.43728 | -43.53638 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5f03a6d-86ff-3778-944c-df05e653fed8 | -11.82481 | -50.4419 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 918e9aca-08f6-3055-a27a-db244c48d3e8 | -11.27279 | -50.83078 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 328e895d-eae6-361c-adc0-f8b5ddb5685a | -12.97449 | -47.97156 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| fe6221d4-b981-358a-8c43-caf3c571c663 | -14.83028 | -51.62977 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90062333-5101-312d-b8bc-e1bb42bdda29 | -10.30214 | -45.38624 | 2025-09-15 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb3b1a1e-96f6-3cc4-824a-7ba738adffc8 | -11.46888 | -43.57664 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
