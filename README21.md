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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 443681c8-81fb-375e-92ff-0b5f53520a05 | -11.47837 | -43.24953 | 2025-10-28 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d5636662-52c8-30d7-9eee-da5d3483cdb7 | -5.70559 | -49.19662 | 2025-10-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 36b0aa92-db7f-3bd0-9086-7eff5074eb89 | -10.28943 | -47.19848 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 310bbdfd-1226-341b-98e8-6dbcc3cae992 | -8.52685 | -44.09063 | 2025-10-28 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b0fa6dc-f977-3c2d-868f-f51b8087e1ab | -12.47473 | -44.49859 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21d52b03-6597-30eb-bc72-eae0cae329d9 | -5.30157 | -48.702 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edd25a0c-ec92-3a38-855c-a0f4e2298368 | -9.19003 | -44.6089 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19d958e0-34a4-378c-9d58-47fe9926719e | -6.47086 | -43.18647 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 739113a2-6048-370b-a373-3e1ed3ad6d10 | -7.99382 | -46.19211 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6874ca5a-9fca-37b8-892d-6315c2476302 | -5.65233 | -47.63639 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01b17858-5534-3df0-a37e-537c7bfdc4e1 | -9.89283 | -44.89761 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff264017-95bc-3f28-a800-b641e5b42323 | -9.60601 | -45.19746 | 2025-10-28 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f60a9053-cca6-3160-a69c-09140478bad2 | -10.19321 | -48.07169 | 2025-10-28 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28821f90-73e8-3bbc-aeb3-bda63ab64c48 | -11.28873 | -45.50908 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 24f1bba3-6561-36fe-be3d-5204c54c2bde | -12.20851 | -45.42428 | 2025-10-28 04:14:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efcb9e5b-89d3-378f-a28a-9d048d6af368 | -11.56528 | -43.12445 | 2025-10-28 04:14:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b04953d-d167-3882-ab78-6a4b230273eb | -12.23884 | -46.48912 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 831745f8-16a0-32ec-91fa-b4c84016e9e8 | -10.29169 | -47.22959 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b93c49f4-32fa-3fca-9f40-c3a89304b2a9 | -7.32486 | -47.20308 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7130c3b5-13a9-3933-a655-8129c3366e8b | -7.8363 | -46.4016 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bbdbe2ed-5413-3ecc-bf22-88d56d4ccbca | -7.99736 | -46.1927 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 72577060-7231-36a0-b0a6-5a69511bcf00 | -6.27183 | -43.86531 | 2025-10-28 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e813e91d-0e20-335b-9ec9-25ebc01e08d5 | -6.89512 | -51.72809 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6614b858-3579-3ca8-bb3c-d9304ea4c533 | -10.64955 | -48.01643 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c15acae3-24ad-3db7-9caf-925474f9f480 | -8.4803 | -48.21757 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa114d3d-30fe-33d0-901b-ed2cc403cc0e | -9.15435 | -46.39971 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77700002-bcae-3dd3-80e8-aa824f96ff34 | -11.28143 | -45.51157 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2c67ad10-b3c4-35a0-8d54-b19ede27478d | -7.10432 | -47.2662 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8046c400-4586-3ea3-af0e-6c18b079c4b1 | -8.09037 | -44.41639 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db24f1ea-9fcf-3021-a80c-1bfff3a5b499 | -6.09717 | -44.68047 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2134812f-907f-3f00-a8f0-941cc409cd23 | -6.60785 | -44.64557 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5340348-95c0-366b-af57-b30114b8c9d1 | -10.31103 | -47.15818 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c732d686-8d08-32e1-807e-5700b77791d7 | -7.80765 | -46.48681 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 768167b2-9c68-339f-a55e-459482a9eb84 | -9.51811 | -41.67907 | 2025-10-28 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4afab50b-3681-3eb3-be04-a4fbf773f880 | -10.54529 | -48.01336 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c079d426-07da-39fb-9035-bb438fe7b3b7 | -7.9517 | -45.46992 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 767aafb9-3c5f-3982-ac2a-e94af30a0e94 | -9.19012 | -44.56549 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 992333a1-5a68-3608-adc1-4ff4cf8e354f | -8.56243 | -47.7311 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05b20bd2-1fa8-3b89-a1cd-7cda8b799540 | -5.3081 | -47.87302 | 2025-10-28 04:14:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77d860a3-d659-3d75-9475-c21233e34a3c | -10.99572 | -50.36662 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b7bd33-d48d-3791-8c4f-8722dd1192b2 | -10.22964 | -47.555 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7d4ae7b-8c3d-374e-a8e6-4d2d105a0ca7 | -6.49517 | -42.22329 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cbc1038d-7e13-3523-b497-0f48288badd8 | -7.96026 | -45.52605 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 622fd398-9c33-3656-bd0a-d12d1252cfd8 | -8.64341 | -45.27822 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bc49763c-4926-3442-a42b-9a63b97b2dbd | -7.95238 | -45.50927 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f84ea724-0774-3fa7-89f5-40738e2dca83 | -11.37916 | -48.18806 | 2025-10-28 04:14:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b370c56-c23d-3ce4-9b99-8cdff6a69b1a | -10.39183 | -47.53154 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32177d31-aea2-39c0-be9f-98db76566cb6 | -10.54574 | -45.0518 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38d43650-8cab-365e-bb85-9f04253d62ff | -9.57973 | -46.94788 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbc190e1-0a36-3fd2-b9ea-e69db8bb2876 | -9.25198 | -45.60093 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5374d530-f9cf-34d4-94ea-f8ef4095adad | -12.07788 | -45.64362 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c750038b-c6d7-37c5-b180-fe1a8892f831 | -9.752 | -47.68966 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fce101ce-dbfd-361d-a518-30530663a471 | -9.01867 | -43.97381 | 2025-10-28 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2159cc4d-1c03-34f8-8f5a-42bd90a4570b | -6.63653 | -47.20215 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59594e47-4dbe-34aa-b9b3-646e163edc22 | -6.69659 | -42.04346 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b119c934-7145-3307-a3db-4040b106ecb7 | -7.1345 | -46.99275 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b2eb4d6-6771-3cae-a51d-47063086eaf3 | -10.6918 | -48.02119 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 507d438f-72e2-3f20-b6f0-04cf1ff6008c | -12.70285 | -46.32008 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 31aa92e2-2835-3d53-bc32-d13d855b65b6 | -6.36749 | -48.06456 | 2025-10-28 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb7680bd-426e-3c28-8534-d93cb6001e5b | -7.61109 | -46.47037 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7851580b-8c0d-3666-8c5a-ecdaacd30703 | -9.01432 | -43.97661 | 2025-10-28 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e28f8569-2be0-3777-b4e3-5e6c80f32382 | -7.96327 | -47.24644 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89139854-bcf0-34e2-a18c-f2543028eaf2 | -9.22412 | -45.64276 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c9d8c85-9bbf-3d48-b190-57108a88dc7f | -7.8176 | -46.4712 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c38d1a3-1675-3372-a3a7-3167911fae6f | -5.48502 | -47.74306 | 2025-10-28 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 611edba9-f4eb-333c-b316-d78714c3edcf | -7.76531 | -45.40611 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6cec906-5568-3df0-9156-5976dbac4dbd | -9.70706 | -43.96702 | 2025-10-28 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c4c5a066-acb9-36d3-bbd0-26a3e36de6da | -8.04754 | -41.10587 | 2025-10-28 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a37523e-37df-36d2-bf0d-dcc670a0c1d7 | -5.53255 | -48.98776 | 2025-10-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c987c72-eb17-3aee-b199-94c6ddff19c7 | -7.59096 | -43.57366 | 2025-10-28 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ab2217c-95f8-3a30-a648-310336a4c0e9 | -10.65345 | -44.11644 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8a7597d-79fa-36a1-b0dd-0c1de3ff6f39 | -7.92891 | -49.74328 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26ce4287-0007-35e4-a996-af193ebf15fd | -7.93514 | -49.99262 | 2025-10-28 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91ebdd1f-df06-3a4c-8ff4-a02577dec9a5 | -8.03936 | -45.14341 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8af014c2-633a-3a59-9860-975518410945 | -12.2046 | -46.50709 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5626541-58b3-3634-a530-c14ea7eaf29e | -10.94728 | -50.28036 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f101d68-4987-3058-941f-436aa97b1252 | -11.0621 | -45.22842 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d4decea-81be-3905-8b94-52035bc23f6b | -9.31134 | -41.09579 | 2025-10-28 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dae5e7d6-1a5b-3dfd-8fd9-0c44290890ab | -10.31432 | -48.78543 | 2025-10-28 04:14:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72551fe3-1f07-3e77-91b0-da5fe1d59bc0 | -7.97518 | -46.72508 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deedd83c-ca0f-3569-9e87-12cd1ae78933 | -5.91864 | -45.39879 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4588176-db7e-3e97-8f16-ceebd9a38dde | -10.33312 | -47.77 | 2025-10-28 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f66267b9-f1bd-307e-9d35-1be482b1cb63 | -12.70563 | -46.32445 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a979fa5a-63ec-3dcf-8016-808789db443a | -7.21994 | -40.26619 | 2025-10-28 04:14:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a5b48f4-a1f7-3be6-8fbb-150efe5365ae | -13.08577 | -46.68421 | 2025-10-28 04:14:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eea5259-6b49-3f13-82c8-c8910a615367 | -6.45 | -43.81509 | 2025-10-28 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18999edf-c005-33cb-892c-526bca5e29d8 | -6.59635 | -42.68696 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c7aedc20-05da-358d-8c04-3939b4bd62dd | -11.33536 | -43.18362 | 2025-10-28 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa0c67c2-2a06-35d7-834e-ed39ea9f63e4 | -8.14754 | -47.00008 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 131d8539-3572-3920-b996-8d1b1ff0acd4 | -8.08307 | -45.95713 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 978c332d-85ca-3183-984a-b443d278997f | -11.03554 | -47.85403 | 2025-10-28 04:14:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8cb2ed9d-e946-372e-93c5-b74371e8bdcd | -10.29674 | -47.22168 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f773c6f3-6679-3830-a6b0-a6a1a54456c5 | -8.08593 | -45.96161 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a43d0cc8-c31b-356a-b416-7bd80a824a77 | -7.3671 | -42.43473 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| baa3c63f-d98b-33b5-b5dc-b22c5326c6cd | -7.86147 | -46.39691 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cdf310c7-b77e-3ec5-8916-4e9b1cc1d58b | -7.80902 | -46.47847 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0459d05-5835-3aa8-b2c8-01875e56c14d | -8.26604 | -46.89713 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1326de8-ec97-34a1-8db7-c3a8fe215f43 | -9.79345 | -47.83451 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f244d9be-82f2-3966-82c0-d7eb8f74f821 | -7.26371 | -45.00888 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba73398f-3327-371e-9fa9-d8f2175c6eac | -13.03441 | -42.32529 | 2025-10-28 04:14:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
