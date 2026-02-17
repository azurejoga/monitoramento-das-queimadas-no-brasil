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
| 1074bb44-b827-3632-bbc9-469840a99c1c | -21.18537 | -48.57922 | 2026-02-17 04:50:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5abbc902-41c6-3f66-ad37-940463d9328f | -21.78099 | -49.82755 | 2026-02-17 04:50:00 | NPP-375D | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75b6393b-94f7-3847-b57e-f4c79b7be52f | -22.78713 | -49.35881 | 2026-02-17 04:50:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 126e6570-d965-3ad8-ad2a-e72c88ce0f6d | -23.56226 | -53.88066 | 2026-02-17 04:50:00 | NPP-375D | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8840c501-ce42-3fc7-8f93-46d6b2faf5b7 | -21.37151 | -49.10313 | 2026-02-17 04:50:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f4ba9f2-6aff-3da2-916f-0f4d1b9aceac | -22.78647 | -49.36369 | 2026-02-17 04:50:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eff03236-20a7-3aed-bc80-5d1f097743ce | -20.78336 | -49.58321 | 2026-02-17 04:50:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ecdfaae1-73f1-34a7-bb1e-6e3191eeff7c | -20.30122 | -49.58294 | 2026-02-17 04:50:00 | NPP-375D | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93a1109e-5374-38e1-9ac7-efaf91e79c60 | -21.78038 | -49.83204 | 2026-02-17 04:50:00 | NPP-375D | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e4976a74-bd55-3547-9f74-99c999856afe | -21.14809 | -48.59393 | 2026-02-17 04:50:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9be6de0e-a939-3a55-858f-98402ed89c3f | -21.47142 | -56.30272 | 2026-02-17 04:50:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d162f663-cdf2-3573-82ac-a654ca38f51e | -20.30483 | -49.5835 | 2026-02-17 04:50:00 | NPP-375D | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b46e105-6e60-39a2-8a55-4837b1c12a16 | -21.70986 | -48.43567 | 2026-02-17 04:50:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19211e02-c049-3e93-aa02-9aeb4274ef03 | -22.79023 | -49.36424 | 2026-02-17 04:50:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41c5fafb-1159-3a1e-9bbf-6c8b0dd0025b | -21.46783 | -56.30199 | 2026-02-17 04:50:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be32391c-a429-3a89-bef3-6bdcf2934ab6 | -21.71378 | -48.43618 | 2026-02-17 04:50:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| beb48e11-bcc6-3ed2-84a3-990bc40e1b75 | -20.51769 | -49.86542 | 2026-02-17 04:50:00 | NPP-375D | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa44de0f-2028-3131-86fb-1d1ed4d569b7 | -20.84288 | -51.73913 | 2026-02-17 04:50:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 11a67be3-5e52-3be4-96c5-47d15613358e | -22.78727 | -49.36025 | 2026-02-17 04:50:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 474297b8-4c29-31df-bdbb-0df4b69da745 | -20.78761 | -49.57937 | 2026-02-17 04:50:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 928463c1-6f48-371f-ad51-ece6bd1f83a8 | -20.78398 | -49.57879 | 2026-02-17 04:50:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aff2cc5c-c705-3721-86a4-d6c7dc1880be | -22.79103 | -49.36081 | 2026-02-17 04:50:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4402f11f-0db5-3bf3-af53-9ef8ddbb1fe2 | -21.18736 | -48.57621 | 2026-02-17 04:50:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1fbc629c-e0de-35eb-ad97-389ca17528a2 | 3.18466 | -60.50764 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5a0556d2-ce68-3945-b485-1357e8784630 | 2.71963 | -60.19078 | 2026-02-17 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c84938bd-8454-3169-a465-2893b70feea6 | 3.1843 | -60.51344 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cbdf3438-9dd9-30c8-98f6-4394a54bd9f3 | 2.67084 | -60.16589 | 2026-02-17 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5571b80e-deb2-349f-bfc1-f1aec4898ada | 2.66514 | -60.15808 | 2026-02-17 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f6cfae0-df84-3927-8514-4e5597c5e7ae | 2.66448 | -60.15382 | 2026-02-17 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f94e048-fe16-3829-9b52-ccb916ba78ec | 2.66646 | -60.16658 | 2026-02-17 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42cb39ad-50ea-3b32-a4f9-392965ad1437 | 3.18149 | -60.51752 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c50bb1b-a5ca-3e74-8acc-d407b49c8f93 | 3.69908 | -60.6575 | 2026-02-17 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0620b8b-80c4-3ce4-828f-2a49d3c67c6a | 4.22027 | -60.89323 | 2026-02-17 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e32f5745-a8aa-301e-bdf2-7133299e7f5f | 3.68704 | -60.92825 | 2026-02-17 05:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4de73b0c-e4e9-327f-82f2-6534f2fea49e | 1.91725 | -60.71724 | 2026-02-17 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2982787-2a90-3448-bf53-00ccffa9b557 | 3.18359 | -60.50886 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca243ec6-b9d1-3bf6-a852-14bf559b622b | 3.68307 | -60.93395 | 2026-02-17 05:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd1f121a-f55d-3a75-a53f-7c6303590948 | 3.17977 | -60.51413 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c57c8c24-c849-364a-899f-d5e6b5fad4e6 | 2.65638 | -60.15946 | 2026-02-17 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b83dc598-55d6-363f-8c27-ad3ca6125510 | 1.91584 | -60.71972 | 2026-02-17 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2871d30c-34ff-3393-bff4-5a78b0c4ac7f | 3.18288 | -60.50431 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12468f23-5f27-3634-bb2c-6a17d9483e5e | 2.95334 | -60.74846 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20f94258-d9c8-3d12-a929-6bdcb42e16ed | 2.94875 | -60.74911 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 407689bc-558e-3412-9f5b-35f5c1d6f9d2 | 3.69519 | -60.66295 | 2026-02-17 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 157b3aba-336d-37ae-89a2-b37146cc5d78 | 3.18081 | -60.51292 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20686af9-2a4a-35bc-abc9-d9dec09e11eb | 3.6959 | -60.66771 | 2026-02-17 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b6e6326-779b-300b-bb4a-e5b110810d30 | 3.70225 | -60.64727 | 2026-02-17 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd01fd6b-0200-3798-9858-0ec2dfa4d752 | 1.45004 | -59.96595 | 2026-02-17 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc8cfae0-8a09-3d6f-ba47-c8f4928799b7 | 2.66076 | -60.15876 | 2026-02-17 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdb3ecb0-b863-30ce-8d40-556e6c3e01bf | 3.18534 | -60.51222 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01991835-b616-3e63-b354-35396c05ddf1 | 2.94947 | -60.7539 | 2026-02-17 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1d77018-bf6b-3172-992d-b2cb4cc27956 | 4.3959 | -60.83121 | 2026-02-17 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2492aeda-1f2d-30d1-b1e1-384e827368ef | 3.69837 | -60.65276 | 2026-02-17 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83fbe822-d1b1-3b3e-af52-e0677b799576 | -15.64633 | -57.51188 | 2026-02-17 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d72ad3-0f2c-3c67-a7b3-8747087f0895 | -15.17379 | -45.64322 | 2026-02-17 05:08:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cffeabeb-108c-39fd-ad85-ba22d0417b54 | -16.4486 | -58.17775 | 2026-02-17 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dbdb29de-8571-39c7-841b-ead5824f7cf0 | -15.17326 | -45.64843 | 2026-02-17 05:08:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66c73341-8546-3784-ab04-a60144c666dd | -16.25027 | -58.71904 | 2026-02-17 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5791bd4b-cc2a-3551-b9b2-2ea476bd4c46 | -16.24637 | -58.72206 | 2026-02-17 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b7da854b-6a66-3dc6-ba74-3559056057ef | -21.71026 | -48.43415 | 2026-02-17 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a36c8cf-5e57-3b60-8c6f-cbf66936bba4 | -20.78584 | -49.58197 | 2026-02-17 05:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7bcfd228-9973-33f2-98ef-6a91c52b1871 | -18.96996 | -52.93134 | 2026-02-17 05:10:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64ba4e2b-c02d-3725-8d4c-b128fafc7bfd | -21.46805 | -56.30284 | 2026-02-17 05:10:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df4a2710-a53b-3590-821e-50de799ab816 | -18.97049 | -52.9272 | 2026-02-17 05:10:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56af4204-f23e-33bf-b514-d23ecba80899 | -18.97471 | -52.92775 | 2026-02-17 05:10:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 484430c5-c0af-3016-b6b4-fb243cf9d7cf | -21.78046 | -49.83298 | 2026-02-17 05:10:00 | NOAA-20 | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0b416a40-3ccf-3d09-b759-03d4dcb162c9 | -20.30371 | -49.58466 | 2026-02-17 05:10:00 | NOAA-20 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe51d991-eb52-39a6-a107-7c03d15a25fe | -18.97418 | -52.93188 | 2026-02-17 05:10:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8af0ffef-8c15-3d32-b959-974359bb3380 | -21.70985 | -48.43855 | 2026-02-17 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e99b67f-934a-3ca6-8351-2ef74c50e367 | -17.95443 | -54.49886 | 2026-02-17 05:10:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f28a4d9e-7500-3872-aa39-81fcb918c79b | -20.78618 | -49.57843 | 2026-02-17 05:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c7efb05-31be-3987-979c-be16323b4971 | -21.47005 | -56.30167 | 2026-02-17 05:10:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92a1bf3c-fb7a-3015-9e0c-d0cd969c2271 | -20.78047 | -49.58124 | 2026-02-17 05:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af5876e0-8bea-3809-bfe6-767cfc4aa8ae | -21.78083 | -49.82936 | 2026-02-17 05:10:00 | NOAA-20 | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 95d8fefd-28b3-393f-8f4a-779fbab0ba7a | -20.30335 | -49.58818 | 2026-02-17 05:10:00 | NOAA-20 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30dc85b4-ac56-37f6-b6ae-6fa9025b9287 | -21.70944 | -48.43717 | 2026-02-17 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5994d2e-3e55-30d6-b990-56230349c7e6 | -21.70981 | -48.43278 | 2026-02-17 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c169ead4-55cb-357f-a3b7-e31491390e57 | 4.39195 | -60.83181 | 2026-02-17 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a6f6c0-0701-3936-aeec-d24340592aac | 3.68742 | -60.92226 | 2026-02-17 05:54:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b062f46-a966-30ec-80e0-babf7ba999b3 | 2.65752 | -60.15893 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8e21fff-9d94-3553-98d4-78fa5e861cb5 | 3.68041 | -60.93102 | 2026-02-17 05:54:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 259e7786-523c-37ab-89e1-fb1c7c068727 | 2.66633 | -60.15751 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db6f7e79-9c86-3d71-956b-4c8ba17411ff | 2.66322 | -60.16553 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bbdcd5d-b5bb-316f-9ed5-61309f3a0fc1 | 2.65745 | -60.15762 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fce0082d-3110-3d82-ba00-12fe154b8e18 | 3.8658 | -60.08101 | 2026-02-17 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5b0ff10-5f50-30f0-95c6-6b391d7b49ec | 2.94684 | -60.75269 | 2026-02-17 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a2931238-00e8-3c08-8cdb-2d12cb0878f5 | 3.18033 | -60.50659 | 2026-02-17 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38e54074-365f-3df9-accc-6e6649c1053c | 2.43043 | -60.23491 | 2026-02-17 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2ba1784-0003-36a8-887f-fd9c9123633d | 1.45046 | -59.96656 | 2026-02-17 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a65dae73-0ec3-34f6-9b13-7a38c29316d0 | 2.67624 | -60.90902 | 2026-02-17 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 499c2751-3bf3-38e5-ae35-fec45b975b7f | 3.86511 | -60.07686 | 2026-02-17 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27d8d20e-50eb-387b-a659-dea97f3ad61d | 3.70844 | -60.63093 | 2026-02-17 05:54:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ce10f76-1609-3416-ada0-773c944b15b1 | 2.66776 | -60.16612 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6771f52e-8fa9-3b6d-9cee-0b4aa425a66e | 1.44661 | -59.96571 | 2026-02-17 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da91fa7d-b0ff-373f-af19-870231b778cb | -15.89511 | -43.4721 | 2026-02-17 05:54:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3dab17f-3f81-3afb-b568-1b7ad7f7357a | 1.45117 | -59.96502 | 2026-02-17 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a447a61-7ef1-33a5-abea-dcd206da280d | 2.68869 | -60.21099 | 2026-02-17 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 397ff76a-7d33-39b1-bf63-3b7d8c01ad1a | -12.45476 | -49.12974 | 2026-02-17 05:54:00 | AQUA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| d7b6b7af-4ebc-3346-86fb-9c3ca9f7cb24 | 3.17739 | -60.5153 | 2026-02-17 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a20078ad-2a6f-3272-a63f-fd570a132f96 | 3.18099 | -60.5106 | 2026-02-17 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README5.md)
