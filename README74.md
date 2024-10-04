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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18fc558e-cec6-303c-9e15-b19a8a0e6441 | -12.27006 | -49.21557 | 2024-10-04 04:10:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 988338af-4b94-309d-894a-c30eae04db09 | -12.26876 | -49.21688 | 2024-10-04 04:10:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d77550f9-597b-394e-9f71-914b34fa54ea | -12.26572 | -49.21473 | 2024-10-04 04:10:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b5c72d-c11f-39cc-a8dc-13f98a799838 | -12.26442 | -49.21603 | 2024-10-04 04:10:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f03ff371-c293-390e-beb8-0be68135ceed | -14.97498 | -49.31017 | 2024-10-04 04:10:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b8e0087-4a06-3b36-81ef-8c36b47bdc52 | -14.97425 | -49.31406 | 2024-10-04 04:10:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 227efa64-5604-3125-9fd6-be1ec0ff151c | -14.97389 | -49.31068 | 2024-10-04 04:10:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a36c59a6-ecdf-3e69-bf4e-00fb6517232b | -14.69593 | -48.7778 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4708056c-acd3-34dd-8999-714a56288fad | -14.69258 | -48.77315 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f23363f-3b7b-3cd6-b90a-60ca3ec4f0a9 | -14.69181 | -48.7774 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6da434e-c10c-32fb-ad12-387ab10c6fb0 | -14.68918 | -48.76879 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e171837-497c-3507-b88e-cf2338ea6490 | -14.68844 | -48.77287 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54faa0d1-bdbf-3e5e-89e9-533eeb9c322d | -14.68791 | -48.75267 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b19be64-8108-3a3a-8c62-ce1bea9f0563 | -14.6865 | -48.76045 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 213febfa-1a25-3acb-81a0-9eb92e0205ba | -14.68577 | -48.76448 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f62f84f-b435-3771-a7bc-36909aea9532 | -14.68506 | -48.76841 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c95c7d6e-9c0b-3e92-b252-5285f91eea19 | -14.68437 | -48.74907 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 926a1ef8-e3cb-32a6-80bb-93080bac636e | -14.68379 | -48.7523 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 593b77e3-be2c-31e1-b46e-af41d9df15a5 | -14.68313 | -48.75592 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 066a1a0c-fda1-34c1-82f7-6c9e4fa62504 | -14.6824 | -48.75997 | 2024-10-04 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e59d9788-0563-304a-a147-f18644029f2a | -14.63205 | -48.71294 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 611205e3-82b3-357e-9ade-abdb74f6f904 | -14.62867 | -48.70845 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae8c77c7-b53d-3ee1-bf6d-7fe64d37ecad | -14.62801 | -48.71216 | 2024-10-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70d41ff5-215d-3502-b299-433b63be1168 | -14.52057 | -49.31089 | 2024-10-04 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5c3a92c9-2265-3c6e-b022-96edaabf9e99 | -14.51317 | -49.27969 | 2024-10-04 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f1a1a7fb-b770-399b-9f9b-dcefebe3a86a | -14.51148 | -49.31301 | 2024-10-04 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51029265-744c-30e5-a7fa-f217550b0a98 | -14.50823 | -49.283 | 2024-10-04 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 506ccf80-f577-3f4c-957a-ae28c8b87767 | -15.89827 | -50.16937 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 441f152d-48d5-3238-ab09-3f12f94eb63e | -15.75631 | -49.93819 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb17e3a6-d63e-3c88-aa30-f80474eb7ee4 | -15.75202 | -49.93739 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dac3421-8555-3118-be4b-12f339c1a0c4 | -11.14404 | -49.61779 | 2024-10-04 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7ebce99-6662-3d9c-82a0-7157f4a89d1f | -11.12223 | -49.60531 | 2024-10-04 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd998afa-e0de-344d-9d92-9c8ed431f6c3 | -11.10065 | -49.62093 | 2024-10-04 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdf770f9-2a2e-37de-bc54-8e16bacbfca3 | -16.09732 | -50.44035 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1fc2ed0-7246-33bd-8ef4-6ecf6596e3c2 | -11.0998 | -49.62571 | 2024-10-04 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0da602c-51e6-3474-a8e1-b924a90462f2 | -11.09609 | -49.62006 | 2024-10-04 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7662240a-b770-3fab-aad4-14291249dbbe | -11.08411 | -49.6081 | 2024-10-04 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c879476d-77bf-3a78-b914-f46649f63d83 | -11.08326 | -49.61283 | 2024-10-04 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daaa8f90-fd63-3243-9a2f-b5d4fdfe0ad2 | -13.62812 | -51.19923 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2870f624-8f74-3a1a-86ba-da8ae639a69c | -13.62535 | -51.18729 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d77fedd6-353e-3c6a-90d7-3112425982d8 | -13.62431 | -51.19279 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c72ab951-790b-3938-ac59-4ef2209e9bfb | -13.62328 | -51.19829 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f9c67bb-718e-3f53-8052-a9ff1e89d9a4 | -13.62224 | -51.20379 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eef3ab59-7126-3859-9dfe-eb55422fa62b | -13.62154 | -51.1809 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89601f74-3c9e-3bca-ac01-4d75f9558dd8 | -13.6212 | -51.2093 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a795be1-b297-32cd-b34f-160d1f516683 | -13.62051 | -51.18635 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5537c6d9-2f4d-3210-b922-3ba21f5e73a9 | -13.62016 | -51.21483 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9338c41-4e5e-38ad-b502-1c6107248415 | -13.61948 | -51.19184 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ca0399fb-d4f8-3c45-ab57-1d170d629813 | -13.61844 | -51.19732 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f45586d8-f65c-369f-92ad-4704ddaa07e9 | -13.6174 | -51.20282 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3cf7cfc-7a55-3da3-99a3-9d807067b276 | -13.61636 | -51.20834 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c6a41f4-b02c-3809-af6c-46bebf786504 | -13.61532 | -51.21386 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03d86127-9bde-33ae-a163-1e9efc3c56db | -13.61428 | -51.21939 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b64ef91-8e27-356f-b2d8-4ea949e620ce | -13.61152 | -51.20738 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27068b48-789d-39b5-9288-1c4dca687ad3 | -13.61048 | -51.21289 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ba75d28-6ad3-3ebf-8728-65245c286b9e | -13.56808 | -51.25047 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eda12e9e-2962-3578-bca4-5710cf50da51 | -13.56428 | -51.24398 | 2024-10-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef2f119e-26bc-359f-a8d9-1447f564387b | -13.14299 | -51.19788 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| d6924597-8cfe-3268-887a-1f9f8efb5226 | -13.11897 | -51.15097 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f46077cb-9562-3cb4-a768-6252b71796fc | -13.11794 | -51.15656 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e15ac59-14b5-373d-a79d-f965601f2003 | -13.11635 | -51.15223 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 73773e90-71e6-3ce0-b9ef-df3a00d9a33b | -13.11527 | -51.15779 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 03e49af6-9ed5-3a73-a74e-17a917c0445f | -13.1142 | -51.16336 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4ff71322-3b16-31fa-b91b-55f9f6e72dfe | -13.1141 | -51.15002 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b4f55c68-0e41-36f9-b5b1-ff1fdae325c3 | -13.11307 | -51.1556 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fa8f72d2-edc9-3a7d-898a-44c4504b595c | -13.11256 | -51.14573 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ffb1705-cf4f-3452-9fa8-0e36809f356f | -13.11203 | -51.16118 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8046f0a0-1b61-3ae9-854e-4e51cbefd50b | -13.11148 | -51.15129 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e5cd8489-c480-30f0-93c3-692c3e5330d7 | -13.1104 | -51.15685 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 199a6da4-2937-338b-ba47-7d7cce430029 | -13.10923 | -51.14907 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b62a8aad-fa73-3fa4-949c-c631d331353b | -13.1082 | -51.15465 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0e425386-0904-3b53-83aa-a344cd54c359 | -13.10717 | -51.17355 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d840977-a64e-3851-9f0c-2b48968cf9a9 | -13.10716 | -51.16022 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1521b59c-9c73-3f5f-b4dc-4ebf399cf791 | -13.10445 | -51.16147 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea6a0e13-9fa2-3e1a-a9f6-37a6f55a40b9 | -13.09463 | -51.1462 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49b79c22-8ee8-36ff-9562-5685bd75b76f | -13.08593 | -51.13875 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f55b4749-7742-3c1f-b83f-68264901eb45 | -13.08488 | -51.14431 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 82689809-3abe-3c61-8389-36aa12b6da6a | -16.11896 | -50.44658 | 2024-10-04 04:10:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be655aba-7fb7-3d22-9b35-aa4c0d4d9618 | -13.08001 | -51.14335 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d60db4b1-064b-385e-b0b6-d789b09b5c56 | -13.07897 | -51.14892 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8c735cf1-10f4-3942-abf2-04c5594ef8dc | -13.07724 | -51.1313 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 029c5a9d-5cca-3556-8599-ac4b235c0c77 | -13.07619 | -51.13685 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8927890f-e283-36cc-94ce-c53c3a6a9a54 | -13.07514 | -51.14241 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41bb908b-6a9b-3b16-bf46-a6d77ddeebf2 | -13.0741 | -51.14797 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6237bef-7c3c-31b8-af07-4f822d967065 | -13.07237 | -51.13034 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d16cc7fb-d934-3733-8eeb-f54f92389b32 | -13.07132 | -51.13589 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7d118979-6db7-3b9e-9024-6aa077d18ed1 | -13.07065 | -51.11277 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 201db0ab-d847-395f-b611-b14113596a89 | -13.07027 | -51.14145 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5826dfb-e348-39c9-9063-1b074e8e6e1e | -13.0696 | -51.1183 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 28e9eec3-1c7b-3d62-9c21-aa0fb0e3dcb5 | -13.06922 | -51.14701 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2fb3a54-2216-31b9-981b-a37197a46649 | -13.06855 | -51.12384 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6db762ba-57da-3286-b83d-30ce933bd679 | -13.06579 | -51.11182 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 464686b2-3b85-3306-b0fb-c8b5d6ab2b5f | -13.06474 | -51.11735 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| aa9d05ff-5443-3dba-b95c-e50712ad5a30 | -13.06369 | -51.12289 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 00b19b2b-8992-3eca-a701-eb0f72a616ba | -13.03724 | -51.12926 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 932e4cc8-be0f-3169-a1c5-075ccbada5f3 | -13.03237 | -51.12831 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1179ce92-c4ba-3693-81be-482d24242c8b | -13.03131 | -51.13388 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5873861e-0793-3b3f-96f2-bb8ff8daee06 | -13.02856 | -51.12186 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b18ec47a-73f8-3ac4-b034-1493cb6d61cc | -13.0275 | -51.12738 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7e233e2d-1f72-3c26-8f61-906cc0aba093 | -13.00422 | -51.11713 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README75.md)
