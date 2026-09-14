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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 852b41b9-9bb4-3e9d-82be-eae3306518b1 | -10.43671 | -48.65443 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f9a7754-7fa2-34b3-b1dc-2b108a490607 | -8.11675 | -54.80333 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde39a75-6369-39ae-a344-e106fa8d2384 | -6.32369 | -60.01274 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4b822db-3714-39b0-b2e7-c5a7397cc603 | -10.47582 | -51.33051 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98e4ec38-3125-3aa4-8460-3e2f048c3e8e | -7.01896 | -44.63019 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 515e3f53-e865-3860-88f1-d461b3b42ce9 | -10.67122 | -54.15691 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 59f6d23a-7905-3a27-9b9e-d335f30894af | -8.53303 | -54.71513 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c9436da-0057-3b22-a278-071cfb97e552 | -6.10814 | -57.67823 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 45d8d9eb-b830-3a27-8a03-a19fa6e957c0 | -8.53933 | -54.69936 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 840754d8-04b8-30b0-b3cc-377c5bfc518d | -3.39213 | -59.41033 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec1d424f-3e13-306a-90c4-27ac97bb5a1e | -11.25877 | -54.12703 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb54067-5f4c-3f8e-a942-ee76d6487e4d | -9.7984 | -55.30903 | 2026-09-14 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c91f0f3d-2549-3cea-ae14-bc0a29fd531c | -6.33901 | -57.87803 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 634ed96b-b3c7-37ba-9603-ad766ad43f19 | -11.05344 | -49.57068 | 2026-09-14 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9dfa22a-4cd6-3404-b1da-359544d0dfae | -9.71688 | -50.8432 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74359554-0404-3a1a-8383-0e6de66e5f96 | -7.57763 | -57.69535 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c01b29c-189e-35ec-91dc-0922c741329d | -7.01444 | -44.62947 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 202692ea-966c-3542-9383-80c22d9beac6 | -11.24889 | -54.14454 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3220a705-d5b7-38ce-8f7e-53f512a7767b | -6.31726 | -59.98866 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 608421b6-d158-30cb-af0d-528baaf394c9 | -5.12029 | -55.9531 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275c2dbf-21c1-381f-8ccb-a108d49c2ce5 | -9.44202 | -50.12646 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 73a4cca8-8740-3261-9d67-374833234815 | -10.47249 | -51.32998 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cfb5d77-1b4c-31a4-bafb-d1340eb4cc9a | -4.24265 | -53.52213 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a13b6f96-3577-35ff-85a1-57683d79072d | -4.38396 | -55.19947 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 600a9ebc-a42b-3f0d-a20f-f17563baca05 | -4.12124 | -60.68509 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 25a5e46b-df66-3d51-b86e-26f397dcc5d3 | -10.63915 | -50.5616 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e9531ef-4276-3e10-be9b-3ba0a67413b2 | -5.12377 | -55.95712 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce8ffa36-cc09-313f-9f96-1834b7ede528 | -10.53855 | -51.30043 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d903167f-b9aa-3337-b59d-9448dba5ae85 | -5.80358 | -52.11575 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f115190f-d0c2-3645-bf72-498a8764b9be | -10.64368 | -50.57739 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91d05d7d-7d0a-3c35-804c-18b423d5b81e | -6.06742 | -57.86398 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9daedea7-7729-3d9f-a8f6-3e1a4aed1a79 | -9.98999 | -59.86297 | 2026-09-14 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e2171d0-e081-356c-a661-9939eb45720d | -4.22259 | -56.205 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9ea2c1f-e9c2-3eef-a74b-cd28873b5ec5 | -9.44801 | -47.87811 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcbea102-112c-35f5-bea7-767237797579 | -6.87157 | -55.29487 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e931f0e-3def-3f3f-a0dd-e43424272100 | -10.46916 | -51.32944 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4070235e-c184-3e83-af27-a4b4a102d67c | -6.31485 | -59.97216 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b264d6d-8c2d-3478-b2bb-0778a2c70ee9 | -6.28924 | -55.27298 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b4fd32d-75e1-366d-82c4-61d2cdafab79 | -10.10328 | -48.86781 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1192a1c0-9e3b-3fd4-b67c-231d8b9b3c9c | -7.01878 | -44.64228 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b1d78ee-ee17-3e62-b115-dc814438be41 | -9.33072 | -44.37532 | 2026-09-14 04:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a7f110f9-d7fd-3a50-8de1-38b0441e46d5 | -4.98203 | -56.13544 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf9ac9c6-dca0-34b4-9f5c-908d93e0896f | -9.45217 | -47.85273 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2072121-89bf-3491-977b-b36ba0f0120e | -8.48025 | -54.59815 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 089a31eb-091c-39d4-b7c4-709c1a5acfef | -12.17583 | -48.96053 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aded659b-8b3e-32b8-b3d4-55684576a6c3 | -7.53949 | -44.8946 | 2026-09-14 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5385eebb-01fe-3606-8256-3fbc096f8d15 | -9.13745 | -51.57449 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 162d0911-10ea-39f0-938c-e98a9a90323d | -6.29291 | -56.02752 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48b25354-688b-3fa4-b04d-208b4d6cf6e1 | -9.31852 | -44.35645 | 2026-09-14 04:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0df9e42-68b5-3c19-b841-33cb07a401fb | -10.66655 | -54.16384 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3990a689-6002-31b4-a55a-95870be23e69 | -10.48346 | -51.23714 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56c25a57-f6af-3d38-8582-8a9abaf7fd92 | -9.69336 | -54.34267 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a18e1e26-64ca-306a-afd2-5a3eefbf0262 | -9.42896 | -50.12063 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| a03e1ce8-56f7-3606-a11d-2d3f89215a46 | -6.59049 | -58.85795 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c22aa5c4-5123-3580-a371-8f9e2f55fd87 | -6.32313 | -60.0159 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1e0c607-abb0-3f36-93e2-5762b8c65375 | -6.59 | -58.85952 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 622fafb9-4087-3bb6-a716-96f4926f5668 | -11.63144 | -54.59194 | 2026-09-14 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b81ddac8-46b7-371c-b631-6e5992a3b93e | -7.08186 | -41.80052 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 998985ac-39ea-320a-a438-46b0828466d9 | -7.09861 | -41.80184 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 55916965-a952-3e1c-9899-02c43a226a6a | -6.31188 | -59.95886 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71ebaa16-e777-3f56-ae67-d46d6dc4ee4a | -10.95729 | -48.36256 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 526dfeac-edfd-357e-bd22-1f83a8695775 | -9.36873 | -50.14923 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a386f40-41d4-3265-af16-cae336968d0f | -10.65195 | -54.14587 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae2fad6d-7c5a-3183-a274-6c7e6a69a30e | -5.20489 | -49.33052 | 2026-09-14 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9360a04-a90d-3623-b62e-899237049562 | -3.3529 | -59.38612 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 042e5ee2-72c8-3755-b5c9-0632b6496eba | -9.44242 | -50.1264 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1fa6d89c-1189-302d-a44f-dc325ea188cd | -5.90415 | -52.10316 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82d0768-b67d-3225-b02c-79a53be752d2 | -10.10874 | -48.85588 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03c61062-76c5-32fe-a466-268f5b3f75e2 | -10.43245 | -48.65792 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 881e98fd-b8ad-3bac-9be9-06954a326f16 | -11.18273 | -42.8101 | 2026-09-14 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d79c6b8-6946-3652-a4dc-30ee3d877959 | -10.5791 | -51.34334 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c60739f-47ad-303a-a463-ddc46d596645 | -6.85261 | -47.4256 | 2026-09-14 04:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a62361-6ac8-3f32-8597-eed4ce3293bd | -11.37637 | -43.94994 | 2026-09-14 04:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dda313c-61c6-366b-aa4c-d63fc59b2749 | -6.27785 | -59.93189 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4a07f65-af1c-3a0c-a5f5-8e1beac36ee2 | -10.70179 | -47.52551 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47e806db-241c-38f2-92a6-9795e438e572 | -9.00091 | -50.82311 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2947507a-2f90-38ad-97b2-bc7f0a3d6711 | -6.37575 | -55.26509 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49616441-006c-35f3-bf14-1d0e4670b638 | -6.15432 | -57.69349 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0005d39e-3c25-3a67-a9b3-2fda8da02693 | -16.36924 | -46.54789 | 2026-09-14 04:53:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bff09c04-243a-3654-80c1-1d101ac47867 | -11.36935 | -43.96412 | 2026-09-14 04:53:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e7b12e8-a119-3f7e-9d2f-fd7a8a43a2b6 | -10.44283 | -48.66397 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03049313-d091-3db7-a229-6c3d79d224f8 | -9.45199 | -47.85022 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73fd3404-82a6-3f37-af69-f3b1ed6c8988 | -10.68615 | -54.15169 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbac4313-8285-35a2-be4f-3d1945f27529 | -9.44631 | -48.10329 | 2026-09-14 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 730cc69b-fab7-3a4a-961d-d138ce1b31f6 | -6.57795 | -58.84495 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b75a86f9-c742-3532-96c5-c7d58aabca24 | -9.45132 | -47.8549 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14492b9c-2a31-3cb6-b983-27c0fa4cb63a | -11.18817 | -42.81084 | 2026-09-14 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 560f4b07-cc54-3e59-9a1f-6de02a5917d7 | -11.21987 | -46.42289 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca14b1ca-8fb7-3b2d-8eeb-ca26f124e1a2 | -10.68054 | -54.14305 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1467bc3f-846b-3c3a-8fe7-b75701757085 | -6.02262 | -59.94393 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecbe7614-f81e-391e-83f3-1efc2c330170 | -3.37454 | -61.33983 | 2026-09-14 04:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d39cf8fc-f54d-3d77-897f-19299e0f3445 | -5.59307 | -60.18396 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd2573c8-0026-3ff9-8633-ca5831498e47 | -9.5449 | -45.43499 | 2026-09-14 04:53:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cdd2241-a7f8-3671-94e6-2f1974c3edd7 | -11.26278 | -54.12391 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f4a73b1-38de-3293-b1b6-0ab9266b1efc | -3.52855 | -59.07067 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77beb2f2-c441-3481-9ddd-494c854a261c | -5.12086 | -55.94962 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 168a3f0a-9362-3cd2-97d4-1c14e3978cd6 | -6.37354 | -55.25503 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 267d32a7-b0b3-349e-8e40-38618f51dd65 | -6.58709 | -58.84823 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9be736b5-d05f-35a0-a839-4756eb1c890b | -8.11813 | -54.79496 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 489e0b56-3737-38d7-9b34-0949a80827ab | -8.53576 | -54.69876 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README45.md)
