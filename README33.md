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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86277267-9f2e-3c46-b515-8b7f2a7031cb | -6.26255 | -43.91194 | 2024-10-14 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adb8e692-a9b3-371b-a76e-1bf378ef5d95 | -6.25935 | -43.90447 | 2024-10-14 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76826829-31a1-3760-8e5d-b1f457b435da | -6.25836 | -43.90976 | 2024-10-14 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bed619e-17b2-3957-bfe7-8b1361a8bf69 | -6.44799 | -44.29172 | 2024-10-14 03:28:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c2fa876-239f-35d7-af21-4386105a7bb6 | -6.44742 | -44.29666 | 2024-10-14 03:28:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 130e74df-2b14-3960-8232-e8dd4a7ad885 | -6.44692 | -44.29747 | 2024-10-14 03:28:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f436bb02-9698-3ed2-a7dd-cf785f564220 | -6.44099 | -44.29513 | 2024-10-14 03:28:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0886a048-938d-320a-9a01-57b93b241c42 | -6.44049 | -44.296 | 2024-10-14 03:28:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad58f0ea-c26e-301a-8069-4e2c59d4fe8f | -6.37099 | -44.09384 | 2024-10-14 03:28:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b70ac47-cb1b-3bd9-a8ab-5b28a427dc1e | -6.17204 | -44.60482 | 2024-10-14 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4e9d074-41a0-3102-b386-555939bcc5bf | -6.16968 | -44.60179 | 2024-10-14 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c5965ea-a7bf-3ec2-bbec-d749efcf087a | -6.16543 | -44.60346 | 2024-10-14 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f942c72-d8bd-3e15-86d3-d3ff0adfa2bc | -5.87101 | -44.04552 | 2024-10-14 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2028d011-29e6-30df-8132-2c52c6f4a160 | -5.87003 | -44.05093 | 2024-10-14 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7340a860-ac3c-3733-9969-07f039ada3ef | -5.58852 | -44.89459 | 2024-10-14 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df2b3564-02a8-3ecd-8083-52135cbada38 | -5.58735 | -44.90096 | 2024-10-14 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 165f5aea-4626-3178-97f7-d91696798f64 | -7.93204 | -44.51982 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a50b98fb-4880-3803-b3be-f83f69cdd899 | -7.92571 | -44.5182 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f00727b-8492-3c00-9141-e0b431d4bc17 | -7.83902 | -44.01035 | 2024-10-14 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fbb48b01-5a8b-322c-b61b-b16d7c9dc8c4 | -7.83548 | -43.99472 | 2024-10-14 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 07865eab-8792-34d5-b38b-230a303aaa4c | -7.83461 | -43.99938 | 2024-10-14 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2656599-f5fd-395b-a9d3-0e939a992be3 | -7.83372 | -44.00418 | 2024-10-14 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da94ca3e-5bed-32d8-afce-28de5e93ace2 | -7.30905 | -44.98445 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d32127e3-bc74-3595-a90a-abbf662d37e1 | -7.27142 | -44.96478 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2425d3e-3c02-3aa9-996a-ce1192704674 | -7.27019 | -44.9712 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d03c4fd4-8c4d-3f5e-b9cc-1290a621303c | -7.26707 | -44.96814 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f2b53ec-76fe-323c-bc5f-5829d7905a33 | -7.26579 | -44.97512 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1d1b198-86dc-3a5b-b479-2810433d569a | -7.2635 | -44.97016 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eed52cdd-d5b6-3514-920a-280e23d6b05e | -7.2604 | -44.96694 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ad8e07e-e985-3184-9b1c-6af6a572bfbf | -7.25912 | -44.97392 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 752344f8-674f-3d63-b5ca-ef26bef2930a | -7.25812 | -44.96222 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7751a4fd-d597-368c-8c7c-f73b5f8b7217 | -7.25681 | -44.96908 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03383b5f-b79d-3a8a-b816-7e112fc675b4 | -7.25376 | -44.9656 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f4620ec-2da4-3b7c-b7b9-bd74582cd133 | -7.25245 | -44.97271 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7c53ad4-1ff3-3b29-a161-63c5ca4552e3 | -7.25243 | -44.92016 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfe1bee3-8bd5-39a9-ab97-e46f8399ab14 | -7.25145 | -44.96107 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72859ea0-f00e-3513-82ba-4e4efd385bfd | -7.25133 | -44.92589 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25a430a5-df72-3004-b1fe-193a43f746b1 | -7.25016 | -44.96778 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ef33d41-1a42-39c8-b1c2-43999bbf5b6c | -7.24709 | -44.96442 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b217336-00f2-3a93-b059-6e6137677ba1 | -9.26411 | -45.23304 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6cd5a7d2-36b8-389a-bba7-82b57fc42a43 | -9.26351 | -45.22783 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 687e31b5-5446-3ac0-91ef-0556f7a65183 | -9.26244 | -45.23329 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5305aef2-96ca-3e13-9087-dad7096b1cc5 | -8.04216 | -44.82605 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bef4332-9a03-355a-86e2-f85a433c5003 | -8.04117 | -44.83135 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c6124a4-f8ea-31c4-b8e6-36f563815b50 | -8.04101 | -44.82661 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0602c1a-a693-3c08-aedc-59f0acbba56c | -8.03997 | -44.83195 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c177dfbe-867e-3bd9-864e-a135cd9df195 | -8.03463 | -44.83023 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e7fcafc-e69c-32e1-9426-3107ef2dd7c3 | -8.03342 | -44.83089 | 2024-10-14 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1cb5a86-b5ca-35b4-b716-8ffd42e7485d | -9.57572 | -44.48268 | 2024-10-14 03:28:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e2affab5-0116-33f0-9c8c-106fc53cb4d5 | -9.57465 | -44.48823 | 2024-10-14 03:28:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 20ed8b1c-ff8d-34c0-a3d9-3f794c88bbfa | -4.63459 | -44.86386 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| add08dd3-9675-3a5e-b448-94434bc0d1c3 | -4.63435 | -44.86349 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c69593cd-9780-367c-9298-0297f445f063 | -4.63341 | -44.87067 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60337f86-4896-370f-bb6b-8a32d72f8369 | -4.63314 | -44.8702 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0758500-1b9b-3c87-aea3-a4f44c5284ad | -4.62773 | -44.86244 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 516a83ef-95c4-31cd-90ba-67dae01ade6b | -4.62748 | -44.86211 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b90c583-d53d-3527-af3f-ac68a4b6a3e8 | -4.62658 | -44.86905 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f97e9d06-6222-38d7-83e4-c146e3d812c5 | -4.6263 | -44.86864 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8fbece3-c7a5-3d09-a05a-ed277282c514 | -4.6208 | -44.86143 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c78d599f-b22e-3c0e-862c-d66743e169fe | -4.62055 | -44.86113 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9152824b-d6e3-3960-adb4-eb4ac1dac72b | -4.6197 | -44.86771 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2871610a-84fd-3362-b517-004d0119d837 | -4.61941 | -44.8674 | 2024-10-14 03:28:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd16df3-e8c6-36ee-ac41-20fa960f4ccd | -5.16273 | -45.39128 | 2024-10-14 03:28:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dce2cac-4c62-36c0-8224-1d9251bdcc15 | -5.15567 | -45.39008 | 2024-10-14 03:28:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90064641-cdcd-39dc-9e0f-342698f0c08c | -9.46303 | -45.80831 | 2024-10-14 03:28:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77d24ac8-7fa5-3d7b-b06e-ebe60e04d3b1 | -9.4603 | -45.81144 | 2024-10-14 03:28:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c055cc60-6dd1-34a0-83c8-1226b1a5bc98 | -9.45441 | -45.8057 | 2024-10-14 03:28:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91586e26-5ce4-31d7-9d79-d3d3a76fca82 | -9.4445 | -45.82058 | 2024-10-14 03:28:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 737847ce-b3b4-3c83-a3a4-2b9823c5c00e | -14.85984 | -40.41955 | 2024-10-14 03:30:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 76f3d407-0f9f-3c28-be64-8143297e2e36 | -15.31462 | -41.89869 | 2024-10-14 03:30:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4d9a89a2-c440-3189-b794-ee917baa3d84 | -15.31433 | -41.90273 | 2024-10-14 03:30:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1a286817-a37e-30b3-ad11-a80eed327d2d | -12.10014 | -43.19028 | 2024-10-14 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22c06289-b233-3038-9f7c-ceeba27cf779 | -12.09867 | -43.19796 | 2024-10-14 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e836d075-998f-379f-83e6-28f3b6298591 | -12.09786 | -43.20217 | 2024-10-14 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed5907b4-c8fc-3451-8def-12f1afe6a44c | -12.09467 | -43.18903 | 2024-10-14 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63ae11ba-8fb7-3d13-a812-58a1e7dc8187 | -12.09397 | -43.19266 | 2024-10-14 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b2a94e19-9a19-3a76-bb39-dfba5b2d62e9 | -11.19343 | -42.66501 | 2024-10-14 03:30:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f1b8cd4-6b11-3c07-943b-c89b5a8bfc32 | -16.04231 | -43.96028 | 2024-10-14 03:30:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b166ac20-06c6-3a74-9edb-841e34af055b | -16.04162 | -43.96362 | 2024-10-14 03:30:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8b17984-52c3-38ab-b56e-b3dab914e7e1 | -11.11198 | -43.33465 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b16c8490-d9bc-306d-bf11-a2215d9d68d8 | -11.11125 | -43.33851 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 63fee0d8-cd8e-3d88-a487-e05e76e41685 | -11.10844 | -43.33469 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| bb2f3d86-0b45-3f54-a121-bbcbe6751041 | -11.10768 | -43.33854 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 89b2de46-e098-36a5-a1c4-0b646980f0a4 | -11.10692 | -43.34241 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 68e74158-6c8b-3ea0-a648-268d2b6aa7f7 | -11.10634 | -43.3335 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 5b1c875e-cefa-3ff2-b72b-db3cda1f63bf | -11.1056 | -43.33735 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d4c2f4c3-c077-3398-8bab-ce0b01819ba5 | -11.10487 | -43.34123 | 2024-10-14 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 388eff4e-32c0-338c-a19f-21137ea16b87 | -11.89289 | -43.89025 | 2024-10-14 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5293cc11-32d7-3174-8d1c-f373a83a37c9 | -11.89265 | -43.89204 | 2024-10-14 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bb5f2624-5d87-3511-aa5c-6648820cd2ae | -11.89207 | -43.89436 | 2024-10-14 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1d7a2dd-c178-3351-bc52-c33911b4bf5b | -11.8863 | -43.89318 | 2024-10-14 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c218a039-363b-344c-ac87-cae5f9431967 | -11.88609 | -43.89497 | 2024-10-14 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ed3fa7f-9130-3fb3-b10d-cf269eb54781 | -11.88032 | -43.8938 | 2024-10-14 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb235729-dae8-3ccd-84d8-6dd9650d910d | -11.10616 | -44.49046 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faaf6a76-9b8e-3584-941f-4c70c2b4f007 | -11.10521 | -44.49519 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2dfa7b2-8a6d-34af-b231-57081338838c | -11.09313 | -44.49069 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed770542-1323-316b-bfb3-a9947c2fa790 | -11.09222 | -44.49536 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38655cd6-6234-31c7-8ad7-74e14ded6efe | -13.70796 | -44.0423 | 2024-10-14 03:30:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b55abcc-bb83-3c06-b03e-c61d3550c413 | -12.42793 | -43.77159 | 2024-10-14 03:30:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 296e23ec-b34b-3eb6-9168-82e6add575f8 | -12.43165 | -43.77245 | 2024-10-14 03:30:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
