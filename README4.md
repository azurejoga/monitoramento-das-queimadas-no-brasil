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
| ab1157c8-7866-36ac-96dc-6c49e45aaa46 | -3.20907 | -46.83186 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca2194a0-6468-3e91-b97d-0cb75e36b653 | -5.492 | -45.3845 | 2025-12-15 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d85e936-438e-377a-805f-b118738d0908 | -5.62682 | -35.3417 | 2025-12-15 04:14:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4b597218-9064-34ae-af78-7e5b0b15e4db | -3.21546 | -41.56581 | 2025-12-15 04:14:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fffacbf7-f1ce-3be1-b552-45728d765f57 | -3.71679 | -39.62528 | 2025-12-15 04:14:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 360854cc-cee9-3cfc-ba2a-a77cfd8d9110 | -7.60427 | -38.28674 | 2025-12-15 04:14:00 | NOAA-21 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddcb859a-9937-3366-baad-dc42dfeeaf72 | -3.71676 | -44.5011 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4b8f258-8194-3856-90b5-de9322a82c30 | -5.26701 | -45.85739 | 2025-12-15 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a41c290-9b18-3b3f-b2e5-e246a11d18cc | -1.9067 | -46.59384 | 2025-12-15 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d8cdde0-342c-38af-b8df-697778c50c2e | -3.72762 | -44.49899 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f76c7be-05b9-3f8f-8f86-e0cf5a76ca46 | -2.39375 | -45.77135 | 2025-12-15 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 035fe009-1ce7-3913-a462-12fde08811fb | -8.14222 | -43.55217 | 2025-12-15 04:14:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04f6726d-20d7-310f-a349-bd9219ef54d7 | -4.05181 | -42.78686 | 2025-12-15 04:14:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f0a0f72f-7d19-39b5-bb5d-0fdcf46ea76b | -2.58531 | -45.14005 | 2025-12-15 04:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b0e5347-16e3-3869-81d6-7bffa0463f1d | -3.3052 | -42.53831 | 2025-12-15 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4b7e272-efda-3fdc-972d-f7dac53af91e | -3.05706 | -52.83633 | 2025-12-15 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd07af8-e1ed-302d-8fb9-745c51019fbe | -3.20598 | -46.82644 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc4abd51-900a-327d-91e5-9709465fe5e6 | -1.82054 | -46.29832 | 2025-12-15 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d1e4d37-3241-39d1-96ec-73367019e5c4 | -2.35603 | -45.67894 | 2025-12-15 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f95a3a8-f9a6-3bf9-8fcb-8c77394fc824 | -3.93081 | -47.5605 | 2025-12-15 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30433405-de77-30ec-9060-1fef71a9dffb | -9.11019 | -35.45364 | 2025-12-15 04:14:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7fe05438-c243-3136-b26e-23bd5320ae68 | -7.76754 | -35.10331 | 2025-12-15 04:14:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17cf9baf-cedd-319f-bdd5-58537ac0e9e4 | -3.72019 | -44.50163 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bafbb208-52ef-33f9-ab97-972f7ebf9db1 | -4.69609 | -43.25257 | 2025-12-15 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccc26f04-840d-3bff-8708-cdbaad0f7676 | -3.05731 | -52.83522 | 2025-12-15 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea6d7f97-3acc-379a-8ecc-196bbb27c3aa | -3.05268 | -52.8271 | 2025-12-15 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de56cb90-8dbe-3fd6-8507-6d366bdf7689 | -6.10019 | -40.01525 | 2025-12-15 04:14:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 944949fd-8d60-3973-91fd-a6ec74a85fa1 | -2.7003 | -45.16999 | 2025-12-15 04:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8161a1da-4b9f-3f77-b4b0-09259ceb99ac | -2.39742 | -45.77192 | 2025-12-15 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a2e7614-c25a-3d60-bfff-531383fec3ec | -3.965 | -41.53518 | 2025-12-15 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2461815a-fccf-3664-abb5-2c3716198c5a | -3.65643 | -39.85312 | 2025-12-15 04:14:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 501f0c39-7e48-3ae7-8a40-ecfedc1aa8ad | -6.47796 | -38.8243 | 2025-12-15 04:14:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cde8c75e-208e-3caf-ad4a-88cdff979ba3 | -4.69995 | -43.24963 | 2025-12-15 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a76e2e5c-fd50-3477-b577-a2b62cfd560e | -3.12867 | -41.77316 | 2025-12-15 04:14:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e955bb7d-bb97-31e9-a928-078e284c449a | -3.72303 | -44.50586 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e06f429a-cd0d-351c-8850-dcf462d7321c | -2.50517 | -48.04078 | 2025-12-15 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 023b7737-cb3d-34a9-9475-c25635a656ce | -2.23298 | -45.65153 | 2025-12-15 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be23a4e8-d2c6-3293-bc89-18871ca2d20f | -7.76357 | -35.10236 | 2025-12-15 04:14:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9c1d4fb3-75f4-312e-8744-ab3169a4938f | -3.72195 | -44.49052 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ff67289-6a98-3238-80d4-755b3681eb39 | -4.06671 | -46.59496 | 2025-12-15 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b065bd3-2a1e-3041-9c14-c356142beaa2 | -8.03112 | -43.11166 | 2025-12-15 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52bb498c-c526-30c9-bfe8-408f10d76aa6 | -3.77593 | -47.15793 | 2025-12-15 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e97955-9b56-3a1d-ab54-31e368cb0450 | -6.48031 | -38.82131 | 2025-12-15 04:14:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 104d862c-e1d7-3ea9-886d-30b74078ab06 | -3.92322 | -41.69397 | 2025-12-15 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6200b9a-d8ea-335f-9fda-0c1dc22199b6 | -2.41328 | -48.28447 | 2025-12-15 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f199b6ca-9054-368e-80ea-31e6870b32d9 | -2.83786 | -46.73341 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| abcbe2a8-5332-3ee2-b014-02319cfa0b7b | -3.06287 | -52.83723 | 2025-12-15 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af28f3bb-63d4-36fd-818c-3a26b8755492 | -3.96555 | -41.53167 | 2025-12-15 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5540437b-9b3f-3d67-97ad-675a3640872c | -2.24794 | -45.78999 | 2025-12-15 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2b856e5-f706-3949-b006-717cca39a8d5 | -2.95355 | -41.5219 | 2025-12-15 04:14:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 084e51df-0c38-3091-8798-6ca210b58c4d | -3.71618 | -44.50481 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c170e735-03d4-3753-8a96-3806db2bca56 | -2.22932 | -45.65094 | 2025-12-15 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 159d25e8-577f-3c97-9ec5-f8556981813f | -3.96889 | -41.53219 | 2025-12-15 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 48c2fc21-0d90-3481-92d8-9ebe621d9ed4 | -2.93381 | -41.14778 | 2025-12-15 04:14:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 81f497de-8119-3c07-9ada-a17c36b39cc8 | -3.45306 | -43.63147 | 2025-12-15 04:14:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527c6ab2-ef3f-339f-8f84-53a622b4fd9e | -3.02107 | -45.3418 | 2025-12-15 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd66814f-7e93-33d7-bdb4-7a26cf63e3e9 | -2.76184 | -42.63973 | 2025-12-15 04:14:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2e3c6bf-0edd-3ffb-bbff-3ee2a4f48366 | -2.63645 | -47.29496 | 2025-12-15 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bf2b4999-1774-3e71-a93e-0a673bc5c7ce | -2.22864 | -45.65522 | 2025-12-15 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36cca6c4-eb65-3f0e-a0ff-2157c669b15c | -4.23744 | -46.31269 | 2025-12-15 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74b3b1d6-9fe8-3ed6-ac91-a97a5056768b | -4.09934 | -46.39745 | 2025-12-15 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 980c2dc4-9ed7-35c6-891c-596582346b72 | -9.91879 | -39.0334 | 2025-12-15 04:14:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b447c1a-3bfd-3b6c-b26b-6be2cc853e12 | -8.8004 | -36.95022 | 2025-12-15 04:14:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7624e82-fa86-347e-b075-1d57b41f26cd | -2.28487 | -53.70342 | 2025-12-15 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 804d10ed-84f3-362b-84de-43a61e9f821c | -4.0422 | -41.91226 | 2025-12-15 04:14:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9d140332-56ae-3ff2-800d-0c9c268bb37c | -5.49576 | -42.1637 | 2025-12-15 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a60552ef-bfb8-3be4-be32-8936c025f511 | -6.10959 | -45.84945 | 2025-12-15 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53a53b04-5fa1-3936-a197-b51e334f51eb | -2.63991 | -47.29912 | 2025-12-15 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 734ad753-d536-37f1-bcc0-e1b2b483489f | -12.34072 | -39.57347 | 2025-12-15 04:16:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3dcd16ed-5b9b-37c7-be08-6779817e411a | -11.27749 | -49.46934 | 2025-12-15 04:16:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d066fa41-7558-36e5-b020-bad92a96416c | -12.63611 | -55.78606 | 2025-12-15 04:16:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1d5b125d-0398-3bbf-9201-2ca0857b50af | -10.78252 | -44.47715 | 2025-12-15 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b2502b2-ea32-3e1a-8dd1-ccbe9f1357bf | -11.00143 | -44.34011 | 2025-12-15 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e4b0c36-33af-3b11-9f1a-420da5bb7e0d | -10.76943 | -45.031 | 2025-12-15 04:16:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80506000-0398-3327-9cca-878a8c3f216b | -11.1486 | -43.32592 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e20dba2f-0889-3758-aa1f-a65062ae4476 | -10.42817 | -44.95371 | 2025-12-15 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50f04d08-13ac-3bb6-8d4a-39c04bdf58f7 | -12.63412 | -55.77929 | 2025-12-15 04:16:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7c6cb489-746d-30be-ad0a-2cccf96036d2 | -12.64005 | -55.78058 | 2025-12-15 04:16:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fa8e7762-cc55-35fc-8dc4-493e4877a4cd | -11.1386 | -43.32434 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 533c6a2e-afa5-309e-89d8-562d36db943f | -12.63701 | -55.78151 | 2025-12-15 04:16:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 581af977-2d28-3dac-b9c2-092e65c94675 | -11.00419 | -44.34414 | 2025-12-15 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e930be43-a927-3beb-8656-dad1176154a3 | -12.29597 | -38.08276 | 2025-12-15 04:16:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a1915c3f-938c-30b0-80fe-a31a0c7d2ccd | -12.31391 | -46.03257 | 2025-12-15 04:16:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c518ba88-f157-3964-934c-e6220ca1d207 | -11.14527 | -43.3254 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 901053e4-bc78-366c-8133-2810d6adbc9e | -11.15248 | -43.32289 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8d79dff-18f9-3005-9c3a-89117efbbfe8 | -10.842 | -44.27156 | 2025-12-15 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d282f797-f507-3252-9fd1-d1d6883720d9 | -12.63319 | -55.78385 | 2025-12-15 04:16:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a6c03f7f-e752-340d-a1fb-db37712d47d7 | -14.54114 | -59.54909 | 2025-12-15 04:16:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d8d644e-2cef-3c75-b869-f3febb69fd5b | -11.15193 | -43.32645 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c6024774-63c0-3e17-a574-fe4389ea16ad | -11.14806 | -43.32948 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d121971d-fc05-3fec-9d04-179fdcd681ec | -11.14581 | -43.32184 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 81f06e37-c474-31aa-9060-e4937af0dc04 | -12.31729 | -46.03314 | 2025-12-15 04:16:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc519580-e332-3439-8f34-917d14fb978d | -12.63912 | -55.78508 | 2025-12-15 04:16:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 136be8e5-851e-317f-9b2f-8ac2a1282f49 | -10.80972 | -44.65036 | 2025-12-15 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 438d27f1-6261-3efc-854f-05180df6a204 | -11.14914 | -43.32236 | 2025-12-15 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 89d6a6b3-cce0-3654-90c4-04d3ce1ec3e6 | -16.22851 | -56.33953 | 2025-12-15 04:18:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5bd85bd5-08d2-3acb-a528-4ba8c078e554 | -16.07197 | -56.59343 | 2025-12-15 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec7901d8-3028-3593-9a8c-c3423782480f | -16.22763 | -56.34367 | 2025-12-15 04:18:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b40e6b96-3917-3e18-a5fe-b0cea6b56c55 | -16.07877 | -56.59032 | 2025-12-15 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9efb3e3-1471-3c1c-9ec1-7791aa7eb378 | -12.6301 | -55.7827 | 2025-12-15 04:20:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |


[Clique aqui para ver as próximas entradas](README5.md)
