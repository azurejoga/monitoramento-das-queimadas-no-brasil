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

## Dados Diários - Página 363

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5d96e41-61ea-3896-8667-900bfd833fed | -3.56847 | -54.66695 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| adbcc088-727f-3fc7-b041-6a94929d3415 | -3.25049 | -57.86453 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d7d828e6-1340-3d17-9c74-6bfe7c5bb29c | -7.22792 | -55.16237 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1dc4173a-5197-3b83-965e-8cd3c329557f | -3.46525 | -60.24504 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| f60d9b4c-a675-3758-8c2d-29f99832196e | -3.25864 | -57.87782 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 3bbada92-c400-3233-99f1-cc18db1c34a1 | -2.09076 | -46.57037 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 47a5bcd4-73af-3365-b8c4-aec08f1f937d | -5.94404 | -45.68985 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eba57297-f3a4-3c7d-8b2d-a284eb4b8ff1 | -5.09553 | -46.22075 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.0 |
| c484bcf5-2039-37c4-80e9-a8b569841423 | -6.72692 | -55.10741 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| bd37964f-bbbd-32c5-be2e-41c3b73d832a | -3.51146 | -59.56687 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d372dd35-9975-3d92-b9b1-1b6f90d51f2b | -2.50492 | -56.12317 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| eac8982d-4845-388e-8520-3ef231171a5d | -6.09735 | -53.49584 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8e3c4efb-e163-3c8a-ab15-3f52756a5831 | -2.97884 | -56.83162 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 83bd836a-744a-3ddc-9f18-42d5e81d3285 | -5.35864 | -43.07352 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c45b5445-d699-3bf7-a246-e1de2ac7bc51 | -1.4667 | -54.7622 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0a0dd9a5-c128-3d59-97ee-aca44d5260f7 | -5.43989 | -46.63369 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 424902ff-f137-37a0-9853-fb45087b852d | -7.21944 | -55.10073 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5923df8c-5669-32e0-989f-4f3373ab8521 | -6.41544 | -47.71397 | 2026-10-08 16:39:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6a55c6e7-e33e-3aac-901e-3d5b226eb5a4 | -3.49263 | -57.983 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 293811a1-4d6c-3922-ab6f-dd0c7e1b5054 | -3.46679 | -39.52689 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a74b02a0-67dd-353c-a227-8c993116ba4b | -1.49278 | -54.5468 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2c19c8a7-2bb6-3ba9-a6d5-d873801fe3a1 | -6.15519 | -52.64012 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 00cd6f34-ad34-31cc-8501-6218cb2820a8 | -3.16716 | -50.59642 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9ea6ccdd-9cfa-3253-9fc7-04460e10a883 | -3.02279 | -54.04893 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| bed0d953-22fc-3aca-b7ac-0c7a0e13be2f | -1.53745 | -54.5514 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b8a3521c-8cbf-338e-bfcf-8ae7d6c8c9a7 | -3.51372 | -54.53234 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 83f2a1ed-c77c-3ab1-9d57-ffc3ca0c4085 | -6.20134 | -52.87216 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b5de5928-4b7e-30ec-bbc0-625facd10a26 | -1.47913 | -54.55354 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 32bc6243-7d26-3eef-b639-102b56fe9492 | -3.77495 | -52.62864 | 2026-10-08 16:39:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| d2d6d7e7-f56b-333f-8959-f4512efe195f | -2.5491 | -57.38902 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bd00bae8-03ba-38f2-a399-ee7d6ee13188 | -5.43738 | -45.68297 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e774db9d-7071-35ab-8e3c-53a1ee65c9e4 | -3.29223 | -53.69619 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 85e42642-eb77-3ccb-bc4e-85cb5893e6c1 | -3.30699 | -54.01584 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3bf93ce-bfb4-36c7-8582-c088b5106ce5 | -5.48225 | -44.6052 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6f69078f-08aa-307d-8bac-66e0f891d06c | -6.71036 | -56.14076 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9ef258ae-c7fb-303f-8d75-77cc6c6e9690 | -5.47243 | -45.69043 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| efc67192-75d3-30aa-b912-acafdf18be04 | -3.58204 | -54.31637 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| db52e6c8-b83b-313c-8323-14a5269f3fe9 | -3.07861 | -53.96149 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 0fffa32c-8c3a-3779-b453-8ca01a427e7d | -6.53804 | -56.04469 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5686035-5225-37db-bdc5-66fa06e30eab | -4.08302 | -48.95645 | 2026-10-08 16:39:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b57bc7a6-33c3-303f-ad6e-8bf9da30d83e | -4.97887 | -42.60097 | 2026-10-08 16:39:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 672f9cef-bc27-3ca6-957e-4a54e3016273 | -3.01167 | -54.06334 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0df5a988-8d51-39cb-b359-bf38a32fb389 | -3.08111 | -53.94611 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| eaa2cfd9-b14d-3ab4-9c2b-2f573d6358cf | -6.11478 | -51.73401 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bc69897c-70c1-3443-9cc5-35f37f895d8d | -2.13775 | -54.79542 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 612eed1c-5534-364b-aa60-010710b89005 | -5.99422 | -55.35906 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fa4dbbd-a8e8-31c6-8620-507f428e457f | -7.19662 | -55.13567 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| d97c33cd-7074-3398-8747-697f72eb75b5 | -5.4887 | -45.22381 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| e3bfd749-017a-3c82-b1d9-48d7f2130862 | -3.20347 | -57.8021 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7964ce04-56c2-3c1f-b906-4d08749c0c40 | -2.90162 | -59.22293 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 16515be8-f072-3ab2-b3dd-08b562c6105f | -4.51147 | -43.79934 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f0a1f49f-60ea-37b6-be8a-d5e0eaf1f267 | -2.96814 | -57.56876 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26f6da6d-0107-30c3-9060-8a2264f82e02 | -3.18308 | -58.84087 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ff4fc7a2-dffb-3343-8f81-c747e4e3e5ff | -2.39487 | -57.22565 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 26920d78-9e01-3f3d-83ae-af61c5221991 | -3.29937 | -53.86897 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| df3e136c-3245-34d7-a5c7-bf69b333c9ff | -3.09309 | -57.56705 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e9d3b1b-9234-3756-84ad-d0e7ffb38b76 | -2.99788 | -54.14044 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 78d12413-3bb5-38f9-b065-2bad57256825 | -3.79731 | -41.65281 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 12d6275a-9b00-3087-b0ff-c192aa24e27f | -3.00015 | -57.74264 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6e2780a4-c821-3fab-acc3-300cc8fab608 | -6.25826 | -52.87846 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c893c8d0-dc3c-36d8-bffd-7f1aed6502bc | -3.35469 | -59.50114 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a8fd3c29-b532-34cc-8a6b-78174d0dfc28 | -5.73114 | -45.23227 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c8c7a56-c4b4-34dc-880d-5932f3329d62 | -2.82534 | -57.61293 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b43f562f-a49e-3680-aa77-77ec63aff5e5 | -2.99851 | -49.21879 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 176f749e-b9e2-34c8-b312-a95cfc54b9ba | -2.96647 | -57.76603 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| ee7b5515-726c-3bc4-9eaa-d50d90809ecd | -6.10285 | -53.50034 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4e550829-02d2-38cc-822a-d6d91a2c6f0e | -2.90762 | -57.2021 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bb5e6884-56bd-3873-b4ce-24d04a5e24ae | -3.56802 | -54.49089 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f6213f6c-3aba-36b6-b93f-dbad19f8ef13 | -6.28194 | -53.38315 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f113ba1b-beb3-301f-ab6d-f1b41a0f8928 | -1.88429 | -54.3819 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 20692adb-66ce-33f4-8e61-55813262379e | -3.26266 | -41.85206 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dbb1bcff-7eb9-3cc6-b4b3-4fe105ba4f0a | -2.41718 | -50.49619 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4ae72efb-1577-3f16-904d-fd5e4b0a8dbf | -1.42391 | -55.71584 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5140fcf8-36a2-32bd-bcc8-8747985656ed | -3.07936 | -53.96647 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| e0b713d3-5598-3954-a657-a6d372ac1bd5 | -6.16611 | -52.65257 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 991b6f96-d3d9-3554-a749-85dbf2e3e908 | -3.94458 | -56.02399 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8dbdbb91-57a0-39d1-87a4-a92a239491be | -5.38903 | -44.1833 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 84d3a383-5564-3289-bdaf-5111708b7336 | -3.90313 | -59.44366 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53c78e73-f90c-33ff-b6a2-4225c37326bc | -2.21744 | -56.91529 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e7e8dd29-7ac6-38eb-9163-4f276d0892b5 | -4.96384 | -56.27397 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d86756c8-89b8-3e61-8bc6-6b5d58e276b2 | -4.44994 | -55.86163 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5ab0e1e9-4ecd-35c7-82f4-670259940717 | -5.366 | -43.20237 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 0cc5b7ee-e342-35ef-9e01-cb7a75f06151 | -3.44262 | -45.09626 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| adfaaac6-62d9-3e76-8544-b7868acbeb99 | -2.51305 | -56.17807 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15d18d7c-2910-3d27-be93-d2fa8040ae41 | -4.61355 | -43.4824 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 406e1113-9130-3ade-971e-a2ad7cd145fe | -3.10737 | -50.26839 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3d71e4d1-a800-35b6-8922-04fd55a52b70 | -2.48933 | -56.16755 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 491a5cc9-6f94-360a-aa36-09fb29e3fb5d | -4.08957 | -44.13802 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 56f7ac68-4349-38fe-a8d3-32d1d50b4e1b | -3.61531 | -60.32992 | 2026-10-08 16:39:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 02dd3224-58e4-393c-bda6-7178ab92c5c0 | -3.09096 | -53.93245 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 07962d2f-62bd-34f4-96fc-21fa14bfb053 | -2.98327 | -54.07525 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 40e3f229-27dd-3815-8792-5c8f3d4550b4 | -5.94048 | -44.3273 | 2026-10-08 16:39:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7cba1230-df63-3cce-acb0-75bd858fb9a3 | -5.93358 | -44.2831 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| edaff2de-353e-3d53-906d-4ce0d4711a69 | -2.49773 | -56.6042 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6eea4b93-b2de-3358-9fa5-25a601c9696d | -5.43432 | -46.64162 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3aeb72db-b7b7-3ecb-b7b1-6e78bb1734bb | -5.66687 | -43.62446 | 2026-10-08 16:39:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e8a54fd2-a69c-3685-9b45-b8507fb98000 | -2.50797 | -56.14373 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 01f53373-ec7c-399c-b7f9-2a8de13f814f | -5.92501 | -51.8237 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 188979b3-731b-3823-851c-d43da708b4a9 | -5.09779 | -46.21335 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b9452204-2533-35dc-841b-bfaf57c6bd93 | -3.0905 | -53.94471 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |


[Clique aqui para ver as próximas entradas](README364.md)
