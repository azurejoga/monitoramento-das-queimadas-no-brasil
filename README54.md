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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bbe9cf0-1a4b-3fad-86a9-c2bdd804a503 | -13.42109 | -46.97492 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8a9ad92e-c657-3bc3-82ee-da108bf75e81 | -13.56135 | -46.9126 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f0bb0be-1381-3ac7-bbbf-fd32cc1c9a1b | -13.47844 | -46.84528 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ee84fd0-7fe6-3bb8-a146-4f60dfd3e449 | -15.17225 | -52.33618 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81707f81-2d19-3a2e-9b95-23f8d2bc1bb7 | -14.3515 | -51.91261 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ca8fec2-4936-3aed-8680-cfad347a8f9b | -14.36101 | -53.23409 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50d983c3-0738-378a-9946-f54f1656e2a1 | -13.52508 | -46.94835 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68fecb09-cc1b-331e-bbc1-8853b20d7e35 | -17.60675 | -46.68893 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 789f2dc8-d844-38e9-b1da-e505ad87c4e2 | -13.82105 | -52.75682 | 2025-08-29 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 301f8e46-843b-3920-8032-73770424328e | -13.5798 | -46.86518 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fe9433b-54e6-3407-b61d-61423bd945e3 | -13.55554 | -46.92607 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30ea398b-534b-329d-9c52-6769e2260196 | -13.53538 | -46.87404 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ce30550d-0c9d-3474-98ee-2ca2097826ce | -12.93256 | -56.97776 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0434ff12-e00a-38c0-9c87-3abb76f78559 | -13.58365 | -46.86574 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05bf6d4b-85d4-305c-8a20-c89cc63547bb | -13.01842 | -56.91245 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69870f97-2497-3db5-820c-c57bd19a25cd | -13.98103 | -46.32928 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c231baeb-08b2-3d25-8635-3f811ede620d | -13.35301 | -54.39027 | 2025-08-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1cae700-32be-30c8-a1b4-44b98a7a5662 | -13.41085 | -46.96464 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c046020c-19fe-34c9-b710-214b7cfa5a3a | -15.16951 | -52.33199 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33070223-12c4-3b56-9efc-e79bee150701 | -13.53342 | -46.94451 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fad20921-9d89-363c-87a3-971cc61a5e5c | -15.06534 | -48.61959 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a38b2fe-b71e-3c57-9052-fe0fa46e9680 | -14.24567 | -48.06126 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5e9a1a8-ccd8-37ca-88be-08fbbb4d4bc6 | -13.40774 | -46.959 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b39a37a-702e-3bbd-b4ee-5eac4ac151d3 | -13.6295 | -48.17149 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb9e12eb-e267-3c32-b2bd-fb4cbd22e13d | -14.30901 | -51.90193 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb8842d6-15bc-3282-93b6-052e370050b0 | -13.60319 | -48.16055 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8b6a5d6-3c1e-3259-bf9f-d3093a798ee1 | -15.53221 | -54.2691 | 2025-08-29 04:42:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4364e42-6bed-3461-8a50-86aeef6c558a | -15.7904 | -43.34966 | 2025-08-29 04:42:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cdf6e2e-48b2-332f-ae17-8dc1c4ada80d | -13.597 | -46.87 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bba262a-6e3b-35a6-a13a-599c1e6fef59 | -13.40646 | -46.96816 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e92ce771-0908-38e9-a4b3-614f3815e784 | -15.08441 | -48.63358 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c68b7ae9-a8e1-3862-9fb2-c436928490d4 | -13.6722 | -46.92207 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e849fc08-2e75-3108-b5c7-8293a3110d43 | -18.19063 | -45.59827 | 2025-08-29 04:42:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28908059-d278-35fa-99da-9a35650248e0 | -13.45796 | -46.96215 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d1526df-ddb0-3be7-aab1-f987e1807e0e | -17.60627 | -46.69273 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e9d9690-2ec6-383d-98d9-772350424334 | -13.82225 | -52.74945 | 2025-08-29 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87392f1b-70e5-3b40-8887-bb818d4fe5ac | -17.54071 | -46.62495 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 911b689f-9db5-319c-8a8e-d5c56baebe22 | -13.42168 | -46.97073 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1ac749e-b390-321f-ae4c-3db61fa6f414 | -14.59051 | -54.52563 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35713eef-4ee1-3046-a3be-2fdbf8d07a02 | -14.51709 | -52.99512 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83b4d115-80b4-36ac-a2fe-b46c550e8614 | -14.3608 | -52.11161 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e347a5e-047f-3f33-9b09-427a79280941 | -13.51047 | -46.85549 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b67791e0-b7b3-37f1-a49b-10d899f9674c | -15.09428 | -48.51142 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c4e2ec5-7330-3e03-85a1-bf570e1e103f | -17.54728 | -46.60622 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c67ddbd-3227-3be4-965c-2b64026126f8 | -13.57911 | -46.87004 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ca1bc1f-f216-3a9d-b12d-525c9be68d77 | -18.56523 | -44.00294 | 2025-08-29 04:42:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5f03657-244c-3e7b-a3d4-8f330d54e786 | -15.01452 | -48.19582 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e6ef574-50d2-3293-831d-5f6f18b9e8f4 | -13.4282 | -46.95201 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93861855-28f9-3790-af0b-d2fbb7763909 | -13.68177 | -46.90981 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34fc72bc-8083-399d-bf1c-2b6688c1ac12 | -13.54377 | -46.87016 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f3513d1c-a17c-3ed2-9b93-3fab1f36428d | -13.51434 | -46.85585 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32e32a34-6f69-35c8-bab5-29d66303b798 | -12.63564 | -60.25308 | 2025-08-29 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90844638-274a-3f68-8722-7b9c00eb6d9e | -17.54267 | -46.60949 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60354e1c-3114-3245-a4d5-a331dbd5f79c | -15.17399 | -52.32536 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45741160-711d-3711-9fe3-e6380c871b18 | -13.03094 | -56.91491 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f332ea51-63c4-3c7d-a5f7-a056b68fcee7 | -12.99047 | -56.92356 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23d73a65-2b8d-36e0-8943-8d6fd7707877 | -13.66899 | -46.91704 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd0d171a-dd31-3441-8f5f-33fdb8fd3f0d | -13.99704 | -46.33149 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85998aa1-c7d9-3b63-991d-eb85aafa047f | -19.80646 | -45.12497 | 2025-08-29 04:42:00 | NOAA-21 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a31c2291-fb0f-3dc6-8713-4271c72420da | -13.56519 | -46.91313 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfcea976-09ef-3b43-8281-793889284d15 | -14.47053 | -48.37807 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6199eaf2-00a0-3540-ad0d-9f972078d1ff | -14.41215 | -42.8701 | 2025-08-29 04:42:00 | NOAA-21 | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| efe4fe2a-ea30-35f6-b45b-a0547faeeda5 | -14.32769 | -51.93423 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7efdc8f-6832-3bbe-b20e-567c9cec3213 | -13.54557 | -46.88539 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 735ace7e-b0ef-36aa-b5ab-b5f9cb3dd991 | -13.49628 | -46.84448 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9b44d41-ecfa-3770-9fd0-a3ab2e598da0 | -14.78033 | -59.72831 | 2025-08-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e03a41f7-d8e8-3d49-b7f5-19cd8019a4ef | -13.41287 | -46.97799 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8dcddd1b-c8f3-3cbf-9cac-9b0e1b0edf5b | -13.63542 | -48.25857 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0889f935-d396-359a-aa59-02b6c0432a88 | -16.91267 | -49.33966 | 2025-08-29 04:42:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d34803f8-b9fe-3973-91aa-e09f95e2ae45 | -13.00168 | -56.9094 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b6e5a0e-7ee4-3021-be19-bac616bb0063 | -15.07833 | -48.14167 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fde4713e-6033-3f65-9e7a-d7245bc80538 | -13.41789 | -46.97002 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 29b15df7-92ca-3214-b3f5-1f4e17cb76f2 | -13.03235 | -56.88286 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2749d6b7-0703-30c2-8675-0f08ed0082bd | -13.66577 | -46.91201 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70420456-2d94-37d1-9290-adcfaee9c3da | -13.36939 | -46.8682 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53fd7c6c-d9c9-32e3-a187-68aaa463196b | -13.67285 | -46.91746 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f5bba6d8-4ca9-35b2-968c-7e11c65f49ed | -13.67353 | -46.88468 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa5d4b6d-638b-351a-a994-477e64adfbb4 | -16.28504 | -53.61637 | 2025-08-29 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cc4993f-e610-3bb1-8ef1-115b3ac74c56 | -17.75726 | -44.50819 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8455ef-3285-31f1-938b-8f42d20125a7 | -13.41409 | -46.96932 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fb54d89-7b7a-3747-8353-272dcf56d183 | -15.09488 | -48.50711 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d641c3cd-f705-359c-be42-cb6b1020f147 | -13.99259 | -46.33435 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db9343f7-a5a5-3b37-85d1-a6f5525abc28 | -14.40349 | -50.41653 | 2025-08-29 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 577a03a8-11dd-3362-a1ed-01796af767a1 | -15.0741 | -48.11865 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e780bdb-6ce8-35b8-8b44-06cfc58dc10f | -13.53861 | -46.87905 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 57cc1f66-661c-3b77-83d3-cdb571cb13fe | -13.4548 | -46.95696 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeb20274-33ca-32b4-986b-e9b1c5a82159 | -13.67735 | -46.88544 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2614fed-a522-3112-9e2b-bc950793e56f | -16.15714 | -49.64499 | 2025-08-29 04:42:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f7b3c5e-7d96-371b-960d-5a16434e9f2a | -13.43509 | -46.95851 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ce053d21-990a-3267-ac3e-d93e2ef0e5d6 | -13.01354 | -56.91553 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb774f6a-217f-386a-b423-87770dc6d47a | -14.79234 | -59.71856 | 2025-08-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a14bb422-e2c0-31ca-8de8-c7643a59c4dc | -13.9783 | -46.33543 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb87fb00-73f9-3aa8-a76a-731a8fc1bdab | -15.03937 | -48.12708 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 700d038f-b0d1-3550-80d1-54091b13c87c | -13.56054 | -46.86248 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d73839e5-e304-3f8a-85e4-2507893b9ec8 | -13.40325 | -46.96327 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f000b90-ae0c-3cac-8b1b-53b56835fe53 | -13.45549 | -46.95203 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48580b20-f61b-323d-b0e4-571e7df9bb18 | -13.01775 | -56.89214 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bc7bf1c-02f7-3dd8-9adc-4c812721fcf6 | -13.59664 | -48.15517 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 706c32fd-7acf-3a8f-af25-ce13ee272efc | -13.58928 | -48.231 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e396d870-3cce-3742-84bf-7c970ea146cd | -14.60478 | -54.50664 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
