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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7848585-6e50-3dcd-a4d7-ae0e54029353 | -11.78522 | -44.27654 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eff22152-4fdf-39b8-9d17-1767e3733dc2 | -12.29827 | -52.50758 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de109bcc-bcf1-31d2-9b93-91168dea4292 | -12.2989 | -52.4932 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6e32e6cb-f12b-35bf-849b-19189d194418 | -10.67806 | -57.60743 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d2a3063-660d-3d16-8a1f-7540a76d4493 | -10.65435 | -49.47803 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ae931b-1715-3f28-9144-e92f2923507e | -12.0664 | -47.34619 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8e6869a-8a47-3fd6-bca2-5aaf85aca4ee | -10.6788 | -57.60356 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deff9c0a-2232-363b-8f9e-39bd067e8ca4 | -11.781 | -44.28022 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 73c262c1-707e-3655-8ea0-d6a4f39dd6a8 | -14.05229 | -53.37861 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01de366a-a73e-3b0c-8801-6c229d129dc0 | -7.68401 | -45.64838 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eda916e-9670-333b-a9a0-bf35a64b8e40 | -10.64677 | -49.48075 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bed0c3a8-f5df-3f36-b882-190c58cfd4dc | -10.74138 | -45.15652 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f45483da-83fa-3767-9406-447611f9218d | -10.66191 | -49.47537 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8846a89d-ea87-3e68-ab04-95ff93ce25ce | -10.8246 | -56.95473 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 880e7bff-f19a-3313-925b-0f46507a84e6 | -8.43576 | -46.63877 | 2025-05-23 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e5a8cbc-dcb6-3404-b8d0-738863b83d6b | -12.13328 | -54.6555 | 2025-05-23 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd818ff2-c029-3818-914c-f673518609cb | -12.40025 | -49.98367 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d31082c-6fb0-3aa2-ac2a-eb052c35779f | -12.13247 | -54.65735 | 2025-05-23 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8223ccb0-e564-3660-bbf5-d06825111b2f | -12.8477 | -47.38599 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65064d57-ccd4-3d3b-bb7e-85691869700f | -12.33224 | -49.98409 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a787615-8af2-3473-9299-e3423b9cab7c | -12.28907 | -52.48971 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94866755-cfa3-32b7-949c-b4e07916076d | -12.32745 | -49.99134 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0fff4ff-6a19-3213-afff-56c878ccadbe | -13.59202 | -47.35664 | 2025-05-23 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2a4273b-e21c-3742-a2cd-7d8a322f4f6e | -15.85072 | -46.48709 | 2025-05-23 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb3135ea-ef24-3ce9-a13f-5708094737db | -16.28032 | -58.67175 | 2025-05-23 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 22fd04e8-8740-3493-911e-e115b1825a8c | -14.06969 | -57.10217 | 2025-05-23 04:27:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ad26109-4568-330c-b720-f3662f7cff28 | -20.85386 | -53.74372 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dc4c737-2c85-3251-8a6e-ca3587cd0b7b | -17.75581 | -42.89662 | 2025-05-23 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83a26328-b296-36a0-aff9-2c7d9eb78506 | -16.06499 | -54.72024 | 2025-05-23 04:27:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae86116-d758-314a-9124-fb4edd18ad84 | -16.01911 | -53.20237 | 2025-05-23 04:27:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69714ef6-74fa-32ad-8679-7bd8ca3d8670 | -13.98234 | -56.01839 | 2025-05-23 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5681be14-8ed6-3ae6-9f94-6fe5233b1bd7 | -17.67384 | -47.52792 | 2025-05-23 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0fe2e77-b52d-381b-b85e-2186bc101641 | -18.48329 | -54.65672 | 2025-05-23 04:27:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 161abd28-fc47-3493-8890-3639de20ee80 | -17.08829 | -48.87486 | 2025-05-23 04:27:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d18e9fe-031d-34a5-b4e9-289fd8926969 | -13.85648 | -59.72203 | 2025-05-23 04:27:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdd718f6-1bcc-302e-b902-37b7855be6ee | -14.87068 | -51.97999 | 2025-05-23 04:27:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3243db2-bdb8-35d8-83ac-9edf11591a85 | -16.84992 | -51.397 | 2025-05-23 04:27:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd8400cf-793e-30d0-8967-0057a4eed834 | -19.05231 | -53.45654 | 2025-05-23 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ae5c074-575a-3dfd-80d5-3d414e2fa957 | -20.85585 | -53.75415 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e48572a5-deca-3d9f-9325-727a5e03c138 | -17.66991 | -47.53109 | 2025-05-23 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f16f4744-52f4-388e-80a7-96e4056a5d59 | -17.67327 | -47.53164 | 2025-05-23 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deed0d36-dc51-373d-8cb6-066bb9e0446e | -20.85673 | -53.7493 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14c0b4fd-0c4a-3fae-996a-083ab5716606 | -17.61322 | -54.1753 | 2025-05-23 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5915ea62-2d02-3438-bae6-e65e3cab11a6 | -16.70256 | -48.17571 | 2025-05-23 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9fcedfd-bbc7-3496-8142-b3b55e9d5d9c | -19.79852 | -53.83289 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f228badc-e2c6-3741-a140-6890271735a5 | -20.85298 | -53.74856 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d381b07-63dd-3a0a-99e9-16e8cda5913d | -16.71186 | -43.22697 | 2025-05-23 04:27:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe87f534-bcd8-3a9f-afa6-654480da9a85 | -18.64706 | -48.2163 | 2025-05-23 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fb6bb176-b18c-329b-940a-e7c746cadc7b | -18.65603 | -55.74795 | 2025-05-23 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1e7bc1e6-09e1-389f-9a92-3364b5db014f | -14.0141 | -55.13099 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e3bbc3e-a495-300e-88f4-d0a1fdd94bcd | -19.79382 | -53.83706 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98e905f6-57bb-3747-820c-1127d179ca3a | -13.98445 | -56.00743 | 2025-05-23 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 88edde0a-1606-3df2-8da5-ad820fddd417 | -17.67817 | -46.82288 | 2025-05-23 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44467981-403d-33d0-b888-d570073efff3 | -20.94539 | -56.58688 | 2025-05-23 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d884d3c3-669c-3e39-bf69-f8422190913a | -15.62321 | -57.31062 | 2025-05-23 04:27:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee7681b2-0e51-324f-af6f-60b858ee3d74 | -15.26742 | -51.4843 | 2025-05-23 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a25b604c-3ed8-3e2a-9432-b676075914d6 | -19.11361 | -52.69125 | 2025-05-23 04:27:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4d7d65b-382a-3b96-9fb5-a41cffd02980 | -19.05609 | -53.45729 | 2025-05-23 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f751e89-1f5a-30b2-ac8f-ccb0f160bbb1 | -17.61796 | -54.17228 | 2025-05-23 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf4171a0-457b-37ea-900c-34bcfd844a36 | -20.43026 | -50.13549 | 2025-05-23 04:27:00 | NOAA-20 | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74208b58-52d3-33e1-a97a-aaca5b76fc09 | -19.05987 | -53.45803 | 2025-05-23 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e543a626-5e47-383c-a29d-196c63a8747d | -17.62168 | -50.91397 | 2025-05-23 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8dcc04e-4d89-3629-aa49-4fa8f34a8008 | -20.8521 | -53.75342 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1122cd81-e01b-34cb-9c07-003806d7796c | -14.01866 | -55.13191 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc52d643-8520-34a9-baf4-8f8c045a99b5 | -19.16969 | -47.70003 | 2025-05-23 04:27:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b963435-45a0-3d7d-b471-04335c8d9750 | -20.06427 | -42.24665 | 2025-05-23 04:27:00 | NOAA-20 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 93a8f927-31cc-3890-a3c9-8ec95c303eda | -14.0278 | -55.13366 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40e5039f-6cc2-3c6a-8ef5-ff73941f2324 | -19.06164 | -53.44822 | 2025-05-23 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d085dcf-d33f-3edc-9904-bf599db3c1c6 | -16.0152 | -53.20165 | 2025-05-23 04:27:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c05e331-eaae-35e3-8314-572f814e7cb3 | -19.05785 | -53.4475 | 2025-05-23 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be1203ed-a1a6-319e-985e-7aea2e2cedae | -14.0269 | -55.13841 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9275a104-b66a-3832-b876-f4fa9e22edb4 | -18.35586 | -55.16539 | 2025-05-23 04:27:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3290685d-9ee9-346a-a3a3-cc222036d22b | -18.33904 | -45.59002 | 2025-05-23 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bec6e837-b3a9-3d05-a5e6-ed20d3711214 | -22.58307 | -48.30634 | 2025-05-23 04:27:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18e425eb-161d-3cc7-91cf-4ea0c2694da3 | -19.79174 | -53.83907 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a53f204-3905-3e0f-b997-43db35226ec6 | -19.79471 | -53.83207 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0afe6688-8c26-386d-83fb-3645e15338e7 | -14.06453 | -57.10093 | 2025-05-23 04:27:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08d5e0c4-1229-3120-9e8d-fb405fe60ba8 | -17.7801 | -42.80834 | 2025-05-23 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c66391eb-18f5-3d44-b80d-9e63d4550cd0 | -17.77584 | -42.80772 | 2025-05-23 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58d2b438-2965-315d-a187-2049e605ab8f | -13.98823 | -56.01393 | 2025-05-23 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 37bc113a-fcc2-3c02-91dd-a93c480217ee | -19.79647 | -53.83491 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 63744992-650c-36c5-a2ad-de542f0be9b3 | -15.85015 | -46.4909 | 2025-05-23 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4eaa2073-822a-3e4b-9246-44f4cbee4435 | -22.55755 | -42.21957 | 2025-05-23 04:27:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1bbdd9db-ba78-39e2-9e27-e80962c794ce | -20.85011 | -53.74297 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f921c03b-c9e5-3332-b60b-4d03fd8024e2 | -19.45352 | -45.30602 | 2025-05-23 04:27:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c74e5f40-d789-3abf-a228-f4058f9c8c68 | -13.9786 | -56.0117 | 2025-05-23 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 548e2d12-4edc-3f45-ad37-a2d7d076ae96 | -22.53951 | -48.81234 | 2025-05-23 04:27:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ede21cd-fd36-388b-8165-d852ed7056e2 | -21.63081 | -48.34073 | 2025-05-23 04:27:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91ddde35-165c-3b4c-b5ff-b177ad4ea87a | -13.72161 | -58.67052 | 2025-05-23 04:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f8a4e06-e934-32e1-9ed8-368e081eff36 | -17.91541 | -45.52892 | 2025-05-23 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffdd1dc9-00fd-3647-9833-4612fec281ac | -16.85008 | -51.3957 | 2025-05-23 04:27:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 403c868b-c329-3be0-ae0b-e4f724ccb0fd | -19.73548 | -54.5102 | 2025-05-23 04:27:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43c5bdb0-3529-3651-9630-9825eff465bd | -22.33608 | -46.94006 | 2025-05-23 04:27:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1dcc7f3d-068c-345a-8117-94702c37eb9d | -14.01776 | -55.13666 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7c380d5-97bc-38a4-b2ed-8dc85aee720a | -13.98128 | -56.02393 | 2025-05-23 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ee56925c-c8c9-39a3-af3c-0d0e0583bf12 | -17.30027 | -49.33413 | 2025-05-23 04:27:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 143486bb-aeeb-394b-87ac-a14d3042e6c0 | -14.03236 | -55.13456 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ea06c27-c543-3c9a-b9c6-5956fc2c2d36 | -15.26816 | -51.48001 | 2025-05-23 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa8e0f8e-a7d7-3f4b-b12d-aed94c82df82 | -14.06905 | -57.10538 | 2025-05-23 04:27:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ce6af49-553a-38b7-ae1f-2ab1ca8848db | -15.26889 | -51.47573 | 2025-05-23 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README16.md)
