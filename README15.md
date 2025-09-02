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
| eb9d2c4e-aebe-3f8a-b5cc-c1fea12b4dd5 | -4.47903 | -48.11945 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8ae489a7-3db3-3409-9efb-43d315f361da | -6.25302 | -42.60753 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6cec7bd7-568e-3f6c-9fef-60befa4f0e27 | -5.76279 | -37.92796 | 2025-09-02 03:49:00 | NPP-375D | SEVERIANO MELO | RIO GRANDE DO NORTE | Brasil | 2413607 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4b65645-8219-309c-8e2f-bca994657727 | -7.46801 | -44.81164 | 2025-09-02 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 146139a3-127d-3155-96ce-2e52f24e6fbc | -6.21834 | -43.36989 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e1f211fc-c019-33c0-a9d2-0c067e4f688c | -5.45256 | -42.58174 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6c97c056-c9c1-3e61-abb2-c01d6f4a2225 | -7.47191 | -44.81816 | 2025-09-02 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6c2e863-9d05-3175-b4f7-fb737f11fc97 | -3.22388 | -47.12828 | 2025-09-02 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b13aa3f0-d4b9-37b5-a654-ada550d9e353 | -6.59125 | -43.63041 | 2025-09-02 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c231d6b4-93fb-39a1-bd99-2f6e10145067 | -6.31177 | -43.51147 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d924390-2bc5-348b-9331-43f63f0cf759 | -6.23169 | -42.42198 | 2025-09-02 03:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 25c25810-1058-32c1-afcc-f1b0bd421c95 | -6.19423 | -43.34734 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be7e450d-e58d-30b5-8c2a-4d1bfd58fa2a | -7.14226 | -45.14351 | 2025-09-02 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 405bc552-953f-303b-bf7b-6d0f5497f3a8 | -5.73725 | -45.54315 | 2025-09-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bc631b2-548d-36b4-a845-69845ad24367 | -6.98219 | -44.34364 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2c74855-9bec-3c37-8443-39d93ce77e3a | -5.6998 | -45.95464 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d09148a-eb74-378c-80ce-cddf8c0fa11e | -6.21458 | -43.36462 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58051840-03a5-3aaa-b17f-dfbe7e61e995 | -7.63243 | -42.64851 | 2025-09-02 03:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af3d9032-2224-32e2-b7ae-6c39523df220 | -6.25027 | -42.62395 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3cdb4a7b-282b-3b73-83ff-965d98da64b2 | -7.63599 | -42.65309 | 2025-09-02 03:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b9190998-7e70-339a-8df2-9455db5de1e3 | -6.26923 | -43.29783 | 2025-09-02 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 783b56b6-5c57-3803-a656-852173abebeb | -5.68652 | -45.89908 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 366d3418-9b26-334d-980c-0dfaf927e092 | -6.8745 | -45.85757 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 941254b4-ebb1-3d20-bb97-48dc725b58d8 | -6.131 | -46.32668 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d8c67df-5ca9-3499-ac6e-e32d5d9078ba | -5.87297 | -46.47462 | 2025-09-02 03:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8a1ed50-f7b3-3f79-b0d3-0e75f0d829c8 | -7.41323 | -44.80728 | 2025-09-02 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2a989ac-ce3e-3b79-a27a-88aa28b4e914 | -5.16686 | -37.983 | 2025-09-02 03:49:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9cf1521-0823-3918-816e-18aea1e423e4 | -7.00177 | -43.53334 | 2025-09-02 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24c1e263-b719-344d-8089-6b29a04ea1e7 | -6.32926 | -43.56969 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0baab26-9976-32de-8f34-eb697c60b0b1 | -6.22674 | -41.81543 | 2025-09-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e032c71b-d662-349e-91f2-9f9d56f5b727 | -6.72145 | -42.2631 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b23f0ecd-85c0-3f72-b8df-4e651f57ec2c | -7.11963 | -44.5701 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e16eefc0-c1f1-3d0a-9609-85c6677dd836 | -7.06125 | -44.33788 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9598e877-24bc-30ed-a25b-3b97ba3f452b | -5.69195 | -45.90001 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0604325-e89d-3fdb-9326-7534274e6bdb | -6.17614 | -47.27751 | 2025-09-02 03:49:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| acc62fb4-0bff-392a-80e0-9571d5a086c0 | -5.78352 | -42.59503 | 2025-09-02 03:49:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 69b583ba-977a-3df9-b14f-686fd78eb91d | -6.9611 | -44.35137 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b89bb12e-c350-39fd-872a-0d502cd522d3 | -7.63664 | -42.6493 | 2025-09-02 03:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8cc4ee2a-90f7-3e4e-bcac-08d89b8a82ab | -6.9316 | -45.56344 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 36363362-f177-3842-a109-f74d18a637dc | -6.42243 | -43.95703 | 2025-09-02 03:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bff5a626-454b-34ef-aad7-fcf49e1be34b | -6.97409 | -44.30595 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b250b8a-e5ba-32a1-a82d-be64a39fae7c | -6.70531 | -42.25711 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8519aa68-71f5-31e5-bd1e-f8bc6fbcf40a | -6.99418 | -43.22471 | 2025-09-02 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ffc8fa48-e768-39e6-b940-1250369f0171 | -5.78493 | -42.58675 | 2025-09-02 03:49:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 95ec1239-3456-3e8a-99fc-2d7eb326022a | -7.10969 | -44.75507 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcc31fc4-7d62-30c6-b3c0-a9fb256aa13b | -6.78931 | -44.62428 | 2025-09-02 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a0096ef-016c-3a14-922f-f3ddeb18471b | -6.17538 | -47.28174 | 2025-09-02 03:49:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5653b115-1f48-3d7a-8d8c-9d9014916263 | -6.22881 | -43.39073 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 817efeab-794b-370f-9c65-3624ef1ee3a1 | -5.69981 | -45.95183 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21b49d4b-27e7-3a29-99d9-39156cc2ac9b | -7.64106 | -43.96023 | 2025-09-02 03:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09ad2d48-5ba7-35b6-8814-18a8809f4bf2 | -6.27867 | -43.2877 | 2025-09-02 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 652edad5-7b42-301c-8316-1849330b5b37 | -6.78815 | -44.62151 | 2025-09-02 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 613df9fb-b9a4-311b-8ee4-6445296bcd72 | -4.30961 | -48.0969 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4364941a-cb0e-344b-a921-ad94335b11b5 | -6.27531 | -43.2896 | 2025-09-02 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9dcbd39-b0a5-347e-9e5a-ebfb9fdf1a37 | -7.06508 | -44.34401 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16191070-191a-3bb1-a438-8fcd481cad7b | -6.71658 | -42.26658 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0ecccf8c-628d-313e-a044-55d29068b895 | -7.1136 | -44.76149 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b416fce9-478b-30f1-9935-2b8f5a69815c | -4.47916 | -48.11332 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d99d1f2-8dfa-33a4-ba0a-087b5fb1415d | -6.7921 | -44.62783 | 2025-09-02 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eefb7dc1-80a0-39d1-886b-80a0e1be8657 | -6.88624 | -45.85306 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5f1fdbb-63af-3a7a-a42b-d8411b14568a | -6.28203 | -43.52031 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da1d8ab4-2f18-3371-819e-fc229d1b22e9 | -7.10733 | -44.7589 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e630e44d-d784-3145-b483-496513663082 | -6.79034 | -44.61857 | 2025-09-02 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ce57883-0b66-3851-9f1f-bcd4fb79fff0 | -6.98664 | -44.31842 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9054acff-9159-399a-adb5-b8ecbc4a3673 | -7.47094 | -44.82372 | 2025-09-02 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dcd611b-1ad9-34ef-be40-b8c66e2c06ff | -7.14172 | -45.14653 | 2025-09-02 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e64d62ad-a136-398a-aa3c-a673515e53d9 | -7.06175 | -46.24149 | 2025-09-02 03:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25d5dfca-152e-34ee-ad32-bbe46d31c851 | -7.62757 | -42.65157 | 2025-09-02 03:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6a40c19c-ced9-3a59-80b3-1a203d2d788c | -6.97831 | -44.33771 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53e73b75-7551-3e40-aaa4-430e4e412ecd | -6.27741 | -43.5198 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33be2263-9081-3ddf-85a7-d8ffb0a89e9d | -6.25234 | -42.6116 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7a3d4a84-6287-31f9-bd5c-f10d0446d0b2 | -6.95456 | -44.36035 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29a90e88-3bfb-36e3-b72e-fae1dad9171b | -6.62872 | -43.95562 | 2025-09-02 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7e26f93-ca71-33e0-8526-2150366f0395 | -6.97796 | -44.31186 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bca776c-a693-3a15-8975-ec6d3e9e235d | -6.79426 | -44.62479 | 2025-09-02 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68729edb-7725-3923-9850-70c0f2640a9c | -5.6528 | -42.59609 | 2025-09-02 03:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c9b44575-492c-3d95-83b6-68cd612f3ea4 | -6.59584 | -43.63115 | 2025-09-02 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be25544e-e86c-3219-a0c6-bb9daa452646 | -7.066 | -44.33884 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ac83adc-1ff8-39dd-9a80-b5d32906dbd8 | -5.7806 | -42.58602 | 2025-09-02 03:49:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e41ce925-c886-366f-a27c-e12e508d7b70 | -6.989 | -43.22834 | 2025-09-02 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 624d3e5b-6373-3c93-9fec-a2c3165f22ca | -6.22329 | -41.81102 | 2025-09-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a93e902f-ef04-3e33-b33a-7c95654ba041 | -4.21999 | -47.21291 | 2025-09-02 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa484c41-005a-3433-a1b5-528f3df6b321 | -6.86347 | -45.5547 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f42d4c1-8bab-3f8b-97a5-e9a456b006d9 | -5.78423 | -42.59089 | 2025-09-02 03:49:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 354021b6-b7a3-3787-b1bd-da537db50ca8 | -6.87675 | -45.8448 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 59c38d92-4051-36ce-a1b6-6367d7d0ccd5 | -6.72072 | -42.26748 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0152ec4d-4bdc-3dc3-87e5-7a1d2253abc7 | -5.51093 | -42.63421 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4ea39939-e24a-3800-b3a4-d8c6b96dfc08 | -7.06032 | -44.34309 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7be08fee-c3ea-34c1-88d1-0ef28a86012e | -5.7799 | -42.59013 | 2025-09-02 03:49:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 95d4d5bc-5b17-34ac-bc32-27ebc78045eb | -6.98625 | -43.1125 | 2025-09-02 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73d83c8c-1e0b-3f95-a974-f05c45b7c0aa | -6.21989 | -43.36078 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0dc44191-bf0d-3f49-8fa8-ae9a6997866e | -6.22737 | -41.81173 | 2025-09-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9ee5281d-9ea6-3b3f-b994-0d03ea72b975 | -5.7792 | -42.59425 | 2025-09-02 03:49:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 58bd8785-5dad-393f-84a2-751e630bdde0 | -7.46901 | -44.80598 | 2025-09-02 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d789287-93f3-394d-9b97-870eb3e7d6e5 | -6.9477 | -45.56328 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77b7685c-13f1-3f7e-b95a-b3af8e0829c3 | -6.94575 | -44.35442 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26e53cea-fa04-39d6-b42f-da033d22e011 | -7.06127 | -44.34187 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63cddee9-c3f7-3038-a2bb-80ad373df28d | -6.88737 | -45.84661 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2bd40252-7067-3e98-a0eb-c64db36217e8 | -4.48088 | -48.10911 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efd42cba-5eb1-326f-bf66-86b8ab20a8df | -6.27279 | -43.51926 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README16.md)
