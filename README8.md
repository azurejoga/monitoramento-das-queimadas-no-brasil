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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06fa1fee-cd91-3c46-b0f1-e17e45dac4ab | -9.61067 | -49.01694 | 2025-07-03 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98a2fc73-74da-312e-a262-403f8bb5292d | -6.19835 | -42.64146 | 2025-07-03 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 287a4823-029c-3dc6-b4de-1a0f6f2ca1b1 | -5.87102 | -50.14645 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81b964e7-24c9-3693-ab4d-c6edd1b79a4c | -5.98827 | -43.74088 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 950ce673-2910-316d-8ba7-fd396a61d7ae | -6.37971 | -39.25396 | 2025-07-03 04:08:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a03606de-8e5a-339c-be1b-7389a0aaa6ef | -7.61151 | -45.75177 | 2025-07-03 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 478f24c3-3ccd-3003-9bb6-96088438ba9e | -8.81769 | -43.93019 | 2025-07-03 04:08:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf8787ae-cb6b-3097-8b7b-da72b757b940 | -6.95222 | -42.88868 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 181fbbf1-197a-3c62-81bc-9a693bad89c4 | -5.87052 | -50.14945 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdcd513b-7a88-3252-8b98-c07cd548b60e | -6.2099 | -43.36427 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35ab08b4-e8f9-3e5e-906c-5201684fc22b | -6.96562 | -42.88714 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 6ceb77ca-cff8-31d4-811a-808d5025ce55 | -6.95 | -42.8811 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 81d4f053-ebde-3830-80a8-4eff7636c81d | -6.96731 | -42.87654 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 961517f6-5246-33a8-a751-f216b7d59ed7 | -6.72433 | -43.14078 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4407ee9e-b980-3714-bb96-336bc90fae62 | -6.91299 | -43.05014 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12c62153-acb6-3674-9525-d97453665819 | -10.99776 | -45.19643 | 2025-07-03 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| affb0a2a-eac4-3d1e-8893-3e6c400129ae | -5.90539 | -43.44822 | 2025-07-03 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6668a6f8-1169-3af1-83e5-dec189ef4a48 | -9.51558 | -45.43891 | 2025-07-03 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b03fe8a-e397-3db0-84a8-b4b5306fca31 | -9.24991 | -48.74884 | 2025-07-03 04:08:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 169c9636-9fc5-362b-a48c-012db67e61d7 | -4.53929 | -48.02232 | 2025-07-03 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a78a91ea-f80f-36c8-a23d-5b95ac61d932 | -7.09236 | -44.387 | 2025-07-03 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f47a5e8a-803b-3d7e-8751-ea1b83f29d3b | -9.8112 | -48.3871 | 2025-07-03 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99e3ee5e-cec5-33e2-aca2-5c798c7d09d4 | -11.1461 | -43.33103 | 2025-07-03 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 86dd07f1-dcc5-347f-80b3-e3977ad34ca9 | -7.44705 | -44.4583 | 2025-07-03 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c947442-a5a6-3da8-982e-f6c1ce59a359 | -6.95055 | -42.87756 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 3618638a-4862-3e5b-8aff-847c6248aa37 | -7.57063 | -43.99354 | 2025-07-03 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c67e785d-2e24-3030-8412-ea9eb4948078 | -7.56316 | -43.9962 | 2025-07-03 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11346ce8-2a77-37e3-ae97-466e2ab8fee6 | -7.70875 | -47.38083 | 2025-07-03 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 650da8a1-3ab3-33ff-97ba-93c39ba7c09b | -6.02516 | -49.22551 | 2025-07-03 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1ff0195-be16-311f-96e9-d7c88f378b2f | -6.72539 | -42.12541 | 2025-07-03 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e9b07cd7-c7f3-32d7-9b2b-0b4037f1fef4 | -7.85945 | -47.87865 | 2025-07-03 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17716768-9bb6-3a1e-888b-87f61f017bfe | -7.85452 | -47.88198 | 2025-07-03 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83502c0b-b062-350d-81ff-529fd830473e | -6.95945 | -42.88621 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 4154c5fc-06aa-3feb-99d5-6fb892cc0b48 | -10.64988 | -44.4882 | 2025-07-03 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9f6a5f6a-f6ff-38cc-99fe-46e452c711fc | -5.02464 | -37.04092 | 2025-07-03 04:08:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f62ca957-f116-3fe0-8284-e6dfcc1bb609 | -6.94944 | -42.88463 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 16986e1c-3bc9-354d-81fa-9c7feaef58b2 | -6.1743 | -48.05632 | 2025-07-03 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2b6d4880-7d41-327f-93ac-e1e0d5cf24b5 | -6.7249 | -43.13719 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f04d075-7bbd-3ac4-9b8c-3e3302182fec | -9.79698 | -47.74303 | 2025-07-03 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57fc808b-ae3d-31a2-97fc-247c4875765d | -6.73971 | -38.2012 | 2025-07-03 04:08:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0880fbe4-a10c-344f-bd33-1ed17c8965d2 | -9.24945 | -48.75145 | 2025-07-03 04:08:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 867c8426-4de1-39b8-84f3-b0473bc740e8 | -6.71742 | -43.1839 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5b007e28-5837-3921-88e5-2424299beb51 | -10.08934 | -47.98898 | 2025-07-03 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc3683f5-420c-3456-8bfe-e8a42a77c411 | -7.60853 | -45.74669 | 2025-07-03 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5314a3c-7107-3a85-bb58-736ce3d9caa7 | -7.61227 | -45.74726 | 2025-07-03 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2330e33-2874-32e3-be3c-0812baeece83 | -6.60221 | -43.03708 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad348198-0fb5-3cae-810a-573de64e0131 | -7.05991 | -44.3657 | 2025-07-03 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b9229b1-bff8-3677-9791-57ae5cc6d718 | -6.95389 | -42.87808 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 66633663-ce08-3300-a849-a0909da459f7 | -6.7052 | -43.1525 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6102a804-f1e7-39f4-a53c-f5d4981f8e6e | -6.19779 | -42.64499 | 2025-07-03 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e75bf288-9e6b-3923-9798-7c790af721da | -7.094 | -49.16676 | 2025-07-03 04:08:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 313691f1-aebe-3582-b626-b0c33db9d958 | -6.91578 | -43.05424 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35962b9a-8300-3a24-9886-be1b537c4faa | -9.20546 | -45.33884 | 2025-07-03 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b5cfd29-0a2e-3a6b-9866-4cae535fbf91 | -5.87288 | -50.15085 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53cb424d-bfea-3789-b1b4-435d33146d75 | -6.68855 | -43.15747 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5ec62ef6-b975-3fbd-8326-0496e027b605 | -6.96001 | -42.88268 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 9929cd5c-f32b-3dde-aaf9-3f59e10487e1 | -6.69921 | -43.15551 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d09c1645-7161-333e-aac4-16b2d214230c | -6.93108 | -43.885 | 2025-07-03 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad798c2a-c668-3bde-862d-353df9d16b36 | -5.82011 | -42.62125 | 2025-07-03 04:08:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9df35e0-2cde-3a93-9267-300aa7197074 | -7.2561 | -44.33616 | 2025-07-03 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c521c851-9b15-3ed9-a4f7-f29f81791b99 | -6.17871 | -48.05711 | 2025-07-03 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 528aa8a6-f84c-34d9-8c9f-ffcbe82cf8e7 | -2.90884 | -54.4889 | 2025-07-03 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94f09fc8-c267-3818-b05f-7bed0aea3c32 | -6.29657 | -43.68049 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f2a1d790-e2ec-3ba1-93a3-3a1761e46908 | -5.99293 | -43.73388 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0992a30-db9b-3ad1-9602-7719dcf5ecdf | -5.92169 | -43.47744 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5ee3d1f-dcc3-3883-bbab-8b35823f28bf | -6.02013 | -49.22806 | 2025-07-03 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75e4a3ec-c666-3224-b350-e99541a4cb63 | -7.22451 | -43.05959 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 5ba154d3-a1bc-3eaa-9acc-fc5e29d89013 | -6.61021 | -43.89246 | 2025-07-03 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 436a11c9-1d15-37b5-a688-e9e42ff86714 | -6.96228 | -42.8866 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.5 |
| f82f7eb4-05b1-3fe4-a415-a1ca2d258ee7 | -6.29039 | -43.67607 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2cf3ced1-e3de-3667-9fb0-9260ca7a5ec2 | -6.1794 | -48.05299 | 2025-07-03 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3947a4f2-292f-39ba-87b8-e48ff756e156 | -6.28979 | -43.67982 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| d778aaf3-e057-31c9-8566-3b628b0bd65c | -5.99577 | -43.73818 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b2eba82-f5ff-34d6-acd1-0a6968e14529 | -7.2273 | -43.06367 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8ea3684c-80a5-37b5-9a6d-2ccd4228f268 | -6.95445 | -42.87455 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 82baeecf-18d1-3fbe-9bec-dae230b87029 | -6.92764 | -43.88445 | 2025-07-03 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63382feb-946f-3cb3-a92e-37d1a7072b2f | -9.51917 | -45.43948 | 2025-07-03 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92e8eb92-c7c8-34ae-b187-a4e6ff70988f | -6.96675 | -42.88007 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.0 |
| 06244370-8514-3510-a68c-98ab4541a5cd | -6.95667 | -42.88214 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| d2c840b5-43d2-37ec-8560-6953c3b4690b | -7.19485 | -43.09505 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cfbd7ff9-53d2-39ae-9eeb-613265c5aec3 | -9.87212 | -48.45946 | 2025-07-03 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6289431-fd7c-36aa-bc9d-c2c5c8c272f1 | -6.00042 | -43.73119 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8edd0886-ca02-3d0b-a724-5409f0a367fe | -10.08803 | -47.99649 | 2025-07-03 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe4cc8c0-63eb-31cc-8f03-3343000c1551 | -7.44194 | -44.44548 | 2025-07-03 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8f505ad-b116-3ea2-b6df-e444d4c05124 | -5.99801 | -43.74625 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 306a29aa-3029-3521-aa70-38fa2390675d | -5.92109 | -43.48117 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d486d257-540f-3928-98b6-25482aa1c6f7 | -6.02493 | -49.22884 | 2025-07-03 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91f902a3-148f-32e9-a11b-8f4bade74c16 | -5.72534 | -49.10871 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a7b48e5-d700-3850-8461-bf856730a4fc | -10.08455 | -47.99205 | 2025-07-03 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 720a1ba3-c600-3bb2-a500-45f4d3813fff | -6.58317 | -43.04873 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 235a11db-dce4-34d4-9491-d077d2790763 | -6.95779 | -42.87508 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac38ec71-735b-38b1-a47e-e6ee34de5d3a | -5.99171 | -43.74142 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e2144e1-0a8d-3322-b025-b7b11d62ca91 | -7.616 | -45.74783 | 2025-07-03 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 662a8e13-645b-3057-8f84-0a070bb62c78 | -6.95889 | -42.88975 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 5715d21a-4e0b-3c4a-a277-9b4114d7d3f4 | -6.68798 | -43.16107 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3fb4dcab-e8ff-3134-a492-7177612f4ca6 | -6.7057 | -43.17093 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da675608-fdb0-3b8c-82d9-6bad722884a5 | -7.22673 | -43.06723 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| cb74a482-a634-34fa-9392-3063b3cf1dcb | -4.28503 | -48.19058 | 2025-07-03 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 181f44d2-52b1-3d81-af25-f8186f6eb694 | -9.03902 | -49.71876 | 2025-07-03 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 074fb306-8dd1-3b25-8c17-808bbe3ddaa1 | -5.91282 | -43.44558 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README9.md)
