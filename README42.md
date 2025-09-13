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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c142d58-b298-3693-b18c-2da28c0509fe | -5.40754 | -42.83769 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f1486cac-39c7-35b3-8f03-c901dc6e1496 | -3.21603 | -47.12884 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c509c5b7-6af1-300c-8f01-c0a0a051d6ef | -5.89331 | -43.45773 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b1358f6-7212-3937-a8e4-fd905f57343e | -7.56208 | -42.64638 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1886adcf-7c68-3f76-a6ad-906a2d3a8aa0 | -5.19849 | -44.30801 | 2025-09-13 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b71a1fb6-7aaf-3d5c-8821-06b7910d2158 | -5.95712 | -43.21245 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 75dcf3bd-5f9e-3447-a75f-fae8ecb64701 | -5.25043 | -45.57463 | 2025-09-13 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11ca7b99-b187-3738-990f-2eec716376fc | -5.94054 | -43.22867 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5babad57-7b93-3beb-8556-5f998cd6b176 | -6.27202 | -43.34865 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 243ea345-c43d-357a-9bfb-c48b8b98dc13 | -6.03596 | -43.59217 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1d7dd0b-2f1e-3e9c-a06a-7c572fe1e385 | -5.7689 | -46.15521 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d258eab-0ec1-39a4-b0ab-ac7546a2ad83 | -7.31676 | -46.58676 | 2025-09-13 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ffc8b346-759e-38e3-8a10-5b733c8ccdeb | -6.17736 | -43.47871 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2d33cb1-66a9-3bd1-a250-aa47ad9c62ac | -7.45743 | -44.45035 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ddcc5d8-4e9f-3640-b730-d42c0c66aad0 | -4.92382 | -47.86907 | 2025-09-13 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f0e7998-7607-3cb0-9fd5-3584ef549333 | -5.18057 | -40.95231 | 2025-09-13 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9fd135e-cee5-30a9-b23d-57e5b8a1f938 | -6.39415 | -44.37273 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a0d350f-56ce-3b63-abe0-775035535447 | -7.77639 | -43.93565 | 2025-09-13 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 308a213b-4f96-3988-b748-b441672d6d8d | -7.41545 | -44.3539 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bfda603-1d16-3049-a985-44a31a5887db | -7.43002 | -44.39685 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7299ce4-5c4d-3af7-9b27-85e620e8b9a2 | -7.43466 | -44.43456 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43df672c-f1e2-3316-bf2d-cec1f4497db9 | -7.45455 | -44.44585 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daacd480-d968-384b-a00a-9d56c65e551a | -8.16431 | -42.38414 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e8f3c1de-edd1-3272-b397-00cde5b64638 | -2.85717 | -49.50668 | 2025-09-13 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb1b40ae-c8c4-3f99-9a8f-1d1d5db36d57 | -6.16186 | -43.35782 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f726263e-5850-3dd4-85a9-47ab954febb0 | -6.39058 | -44.3722 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c044e987-ce4e-3c93-bc09-c93b1216a1f8 | -7.26535 | -44.42859 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bd0600e-9de7-31f9-980a-5dfedcc6547b | -6.99073 | -43.80433 | 2025-09-13 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 309d25da-dc74-37b9-b4ea-97768e6e7b85 | -6.25044 | -43.13449 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2f2dd7fe-4132-30aa-9278-a0128c73f3c6 | -6.12146 | -42.95796 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c9093f19-aba0-33f9-9ea5-29f2283959ca | -6.29172 | -44.24515 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f0afa51-6576-3a15-a847-560a007accb7 | -6.57645 | -42.94128 | 2025-09-13 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5238aa3c-41da-39d4-b760-38e4078797f2 | -6.17492 | -43.36378 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 322df2d2-7ce2-3916-afef-7597e4e67575 | -2.85246 | -49.50267 | 2025-09-13 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22e3d0c7-cc9b-3c4b-8889-c823fb2e0016 | -8.18732 | -42.43071 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c15d98b-b27a-3e7b-8349-eaa3cf4ba965 | -4.58547 | -37.80775 | 2025-09-13 04:06:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b3ebac82-c8a5-30b6-b03f-0ba780610f99 | -7.39513 | -44.34347 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36a3a023-1e51-3c4e-9de4-71c838877538 | -5.76613 | -43.913 | 2025-09-13 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dddc032b-932a-341d-aa7c-0c58fb313328 | -5.20567 | -44.30919 | 2025-09-13 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff5e03aa-26ad-3bbd-bb92-097f29712b86 | -3.22378 | -47.62695 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 06ac0fa9-0646-323c-ae21-775d56d89718 | -5.93772 | -43.22447 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 586d983c-f4c9-3b13-b2be-655624f1f887 | -3.23736 | -46.78227 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 017fd52a-a727-3da5-a4b7-6eee971b43ad | -5.49354 | -42.15145 | 2025-09-13 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d820355-fef3-397b-be42-79ae35002de1 | -6.83412 | -47.86084 | 2025-09-13 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5489984-2177-3611-b306-8062da628d7d | -6.69503 | -44.1288 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79d538f8-c9f1-3ed9-bc47-bcb90159328d | -2.44042 | -47.32729 | 2025-09-13 04:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba9df8c-4f87-36ee-beb3-9ab580bbcb06 | -5.9674 | -45.85083 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed18ceee-6cca-356d-b774-62099b5ff08d | -5.8028 | -42.47067 | 2025-09-13 04:06:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 658bb020-be8d-3f59-acb3-8e7b1eb18673 | -7.56486 | -42.65043 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd822bba-be5e-300a-8d81-480e8dec65a7 | -6.1092 | -45.9445 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7dfcfae0-9e74-3ed5-9e33-2b2017a64a28 | -7.42673 | -44.41681 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3bc77616-1228-338f-8a03-f8655f6cd0f9 | -6.05877 | -43.56073 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcd185c1-6040-3fb7-8874-8f5149955f28 | -7.41208 | -44.35026 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73735ce8-9adb-30ce-a797-f1e5485c081c | -6.82904 | -47.86731 | 2025-09-13 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0351fb8-7f25-3621-a252-be3aadc8875f | -6.69439 | -44.13269 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf187afd-f503-302d-88cf-2689e1b8eb98 | -6.20337 | -43.44847 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35afd4cd-87eb-3e7d-900a-3f34275a0959 | -2.85195 | -49.50581 | 2025-09-13 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fd96836-40c5-31b8-8de2-4becdbe1fd29 | -7.07859 | -44.12902 | 2025-09-13 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d568c763-eecd-3a29-961a-8962c18c89f5 | -5.08782 | -41.15318 | 2025-09-13 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 05b0b412-10d1-3f7b-8a32-5d71653f62ff | -6.3964 | -45.64113 | 2025-09-13 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77ca9201-2fa8-3ca4-a73b-5388fa2b0703 | -5.67872 | -45.05705 | 2025-09-13 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b979e005-2c1d-3552-a5be-6f057645b625 | -6.43439 | -42.62193 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 237290cd-b28a-303a-aed3-a0238b5909b9 | -6.30777 | -44.2358 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32f39a30-05c4-31cf-90bc-40baf5548d94 | -6.67827 | -44.13856 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6df6cc70-eea1-3a24-a715-f362a0abff88 | -5.99157 | -43.72254 | 2025-09-13 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84509f5b-283f-3dee-ac0f-0a16d457efba | -6.27196 | -43.34911 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2fd3fc6-7fd9-314d-8ae1-7d7b7e272357 | -6.29106 | -44.24918 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac76a662-5aef-3bb4-bdab-af25e8cf2c6d | -5.20208 | -44.3086 | 2025-09-13 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21bb1c88-f228-3ed6-aa22-c7d07b1da8f1 | -6.85854 | -45.63787 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d0affdb-febd-3596-a680-27808b956f03 | -5.20142 | -44.31269 | 2025-09-13 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 885ec013-688a-3a40-b1aa-813305347c8c | -6.67799 | -44.16268 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8aa421f5-e35d-38b7-84bc-e0b8412cfdab | -6.16528 | -43.35837 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d3ea4db-c60e-332d-b5f4-be6d05c39468 | -6.25123 | -43.47925 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1bcd77e0-81b6-38d4-bddb-9990674c701c | -6.29523 | -44.24589 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4fd304d-57a1-3a0a-b731-cfa2eab8243a | -5.99219 | -43.71868 | 2025-09-13 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d07ea39-ae4c-33fd-90e0-4def5f08abac | -8.01036 | -43.81151 | 2025-09-13 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cabb9776-56cd-391d-806a-9c659aa10ced | -5.34571 | -47.29239 | 2025-09-13 04:06:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d09198a8-4d3e-3fe1-8384-c7e947de6213 | -7.4108 | -44.35818 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a15f910-12b2-3933-bbde-fd535718d072 | -7.31433 | -43.92855 | 2025-09-13 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 180256bc-b0fb-3a4c-82d2-c9ab08e967ca | -6.77006 | -41.59989 | 2025-09-13 04:06:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46d9e489-fabb-30be-84f2-2c221d0dccf5 | -6.56101 | -50.87109 | 2025-09-13 04:06:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2609c21d-d57f-3eee-8e0e-876654cec97b | -3.24166 | -46.78297 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a839ed9d-5a3c-3519-96eb-00f889f0208c | -5.85879 | -48.15747 | 2025-09-13 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f68c0994-9bdc-3a95-a785-1053c9ed85d4 | -7.05603 | -44.68638 | 2025-09-13 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 365b4f42-6eea-3cb9-b171-9c66dd416ed8 | -6.20662 | -41.01446 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f3b05a6d-19fe-3af2-b96a-cbe3fde6d3a8 | -5.79946 | -42.47013 | 2025-09-13 04:06:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 615c685b-28bc-3bdb-b3e9-579ce7049049 | -4.94335 | -37.93493 | 2025-09-13 04:06:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0107787-4b89-3eaf-a69e-6e66a041abc9 | -7.77578 | -43.93943 | 2025-09-13 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 369699d1-c386-34aa-9505-b171ab2ec00f | -5.08343 | -41.15956 | 2025-09-13 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1d757c2-c967-386f-8f35-7b3ce0fa346c | -5.91734 | -47.43076 | 2025-09-13 04:06:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f79b5f4-9239-3b9c-ae20-a240033abfa1 | -4.4124 | -47.60983 | 2025-09-13 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ef0425-b9af-37f3-85ac-c8ff96b1c174 | -6.69244 | -44.14455 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a35b7fed-6a61-31da-914b-337f2f8ed09d | -5.73775 | -51.70012 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4366c42d-f2ae-3100-88f9-805f7d7106ee | -5.31525 | -47.87027 | 2025-09-13 04:06:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 759ee570-6048-3561-919a-4dd98eb8df7e | -8.18346 | -42.41221 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10209098-3f2c-337c-9050-bd1f1ff768b3 | -8.17294 | -42.43555 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0814aad1-1eea-3939-a452-0250fa18c4ff | -4.9193 | -47.86843 | 2025-09-13 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d9758937-ba2f-33bb-bd7b-55a34e79ed37 | -7.45936 | -44.43856 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be8e86aa-30d3-37f9-8d15-2265d4a29b92 | -7.07573 | -44.12456 | 2025-09-13 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4bd4d32-45c8-35ce-a6d0-03172e1229db | -6.85914 | -41.48635 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)
