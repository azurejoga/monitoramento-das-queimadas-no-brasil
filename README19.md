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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd669476-f0ba-3952-a3bb-421c19c5ece4 | 2.51171 | -50.84774 | 2026-09-13 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 172509ba-ecba-3b38-a94d-77293be8bd03 | 2.5133 | -50.85853 | 2026-09-13 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f9885ad-821e-3280-bb98-06b4f6501b3f | 2.51223 | -50.8513 | 2026-09-13 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b92c0327-969e-36b6-aaaa-286414bba878 | 2.51276 | -50.8549 | 2026-09-13 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2155e852-0a8c-339c-bfe9-f851755a4987 | -0.16532 | -50.40838 | 2026-09-13 04:12:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff9f9ea6-4bfb-3b4b-84f2-f03668900bf1 | -3.22955 | -43.04133 | 2026-09-13 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08e918f3-b3cd-31af-8f5d-66e9f83312a8 | -7.38432 | -45.35252 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0274a41-d0b4-3d26-a8f2-1db6dcd94d34 | -2.11477 | -47.11797 | 2026-09-13 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 747ee9d0-d220-3ff6-8b18-bd13debe3067 | -2.82512 | -49.23801 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ad1cc86-5c2e-316d-aba9-8ac8c6bcd5f2 | -7.52348 | -47.33727 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e91e1861-eb98-3ecf-9f05-28c75392d136 | -3.57072 | -53.00452 | 2026-09-13 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b71a019f-39e3-3627-ba9e-5f1c30f21979 | -4.2663 | -46.53733 | 2026-09-13 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7932e9ee-7258-337b-bcf3-28d4dcbc9340 | -7.01454 | -44.62843 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c6e3a949-fb3e-316d-8861-f29d76571c2e | -6.20656 | -45.40152 | 2026-09-13 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a44c451d-4644-33f7-888c-2fc82f17e1e5 | -6.51805 | -42.23352 | 2026-09-13 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0fb4856f-dbd3-3431-b553-051952862d6b | -2.93534 | -45.50709 | 2026-09-13 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cde3094c-4beb-33cd-9885-309a0441ca40 | -6.76719 | -45.45457 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cb66f43-61d4-30c5-9624-6e0a9b4eef1a | -3.04852 | -51.25954 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb8fe59-06a8-3e90-a584-d24902d8cbf7 | -3.33614 | -42.29386 | 2026-09-13 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bd917afd-2d64-3dc8-82b9-bcf68883399c | -4.4577 | -50.16164 | 2026-09-13 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85b8b821-76a9-3d7e-bcb7-8f8fb9671c43 | -7.76883 | -46.68929 | 2026-09-13 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b31ddc95-2e54-33bd-baf2-d9984c23e861 | -4.36946 | -42.99448 | 2026-09-13 04:14:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5e773ca-7993-394c-934f-aa1f49ff2d3a | -6.79209 | -48.65852 | 2026-09-13 04:14:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55fc65df-e4b9-38fd-a81d-2aefaff5fcee | -7.96923 | -43.98959 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 054a6614-ebe7-375e-a244-f39ce6b5a739 | -3.33507 | -42.30074 | 2026-09-13 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1e245b99-3eb5-38c7-944d-caba313cf9e5 | -6.09533 | -49.66348 | 2026-09-13 04:14:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bdc47b7-c009-3066-b422-1c6315468b14 | -3.8784 | -51.19469 | 2026-09-13 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c986d05-5186-376f-a8f9-29e0a229e740 | -5.1305 | -55.96576 | 2026-09-13 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 81365b8e-0f1f-332c-a412-e98494463273 | -7.46521 | -46.1483 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771e6e4c-3679-3671-a873-2fb51e4c0fe5 | -3.04706 | -51.2613 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25db71f8-f4b4-363e-a3da-f44e19cb4ce3 | -5.17943 | -49.3554 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 276575ea-d4e3-31f2-9673-7d56c497c980 | -8.43335 | -46.03675 | 2026-09-13 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e7b8900-1af0-30f3-8c79-ee10c0eecdd4 | -3.04694 | -51.26892 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ae079f0-85ed-3bb3-aaa9-8ea894892ff1 | -2.94358 | -50.40398 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7ed8f61-9780-360d-8bab-71bf03b549fc | -5.64513 | -45.91336 | 2026-09-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a25684b0-ff7b-3ac8-87aa-9ea0a217e32e | -7.77174 | -46.69403 | 2026-09-13 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 72a27c0e-cd4f-3269-8603-7e6bdca34df8 | -7.62535 | -45.98859 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aab77eae-baa9-38a9-8289-0f8488c473e5 | -7.32148 | -45.30491 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7024591-fd36-36e9-b629-01771219f5af | -7.14899 | -44.72002 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 295e50cd-d9e1-3f7d-a6ba-556178f69abd | -7.4701 | -42.11697 | 2026-09-13 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b5e88e7-1b99-3bff-acf6-f0d1ce4b4a01 | -7.57915 | -43.93819 | 2026-09-13 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91e1f589-b8ab-358e-9d0e-f8d8f533298e | -6.23163 | -51.69503 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4676188f-2bbe-3c2f-be6e-47deaa81cfac | -7.46585 | -46.14437 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 02b65f6e-2682-35b1-b465-c5c2f433a6dd | -3.04656 | -51.26443 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 814ef71a-6e88-33b3-abec-7ba4eb8d624a | -6.85785 | -44.86486 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3818b1c-a22a-333d-b1e5-2b7e828e79de | -7.05726 | -42.72659 | 2026-09-13 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 462deea2-310b-3c04-aca5-e85cae077487 | -7.63009 | -45.9814 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 413ce888-39cc-360a-9d19-d28c34ebdb76 | -4.45852 | -50.15675 | 2026-09-13 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5112c907-85f6-3cdf-b5b1-6ab614cbc86a | -5.76766 | -45.09457 | 2026-09-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07778b70-ab94-36c2-a93a-e5c2b2548646 | -3.85107 | -50.61484 | 2026-09-13 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 816a450a-6131-3549-b401-65f160f6a20a | -6.83283 | -43.51462 | 2026-09-13 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a3c37b5-73a5-3632-8efc-c11966609187 | -2.82742 | -49.23273 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50d27487-425b-37ff-86d3-15c3324986df | -3.04747 | -51.26578 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b13d4a04-f861-3e1a-8a2f-0331d1c00d11 | -3.0428 | -51.2618 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acb5fbd5-6630-35fb-8153-c54081525ee3 | -8.98103 | -44.3913 | 2026-09-13 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af27555a-548f-3013-a3ce-051983b5f07a | -7.15234 | -44.72054 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3901423c-ff3c-3843-b4a1-f5ca4e56aca6 | -6.22814 | -51.68518 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c6a2d55-11c2-36ee-8603-ea7dcae72e37 | -3.82693 | -51.88833 | 2026-09-13 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3a1afc5-d6d5-3d05-9ad8-e63e5d35e8e5 | -6.72796 | -45.41368 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfcf2730-300d-37e7-b638-a71cc3d2f5cb | -5.76081 | -45.09353 | 2026-09-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84cc9e87-1ffd-31ec-b88a-ccbb1dd47a07 | -5.49267 | -49.5078 | 2026-09-13 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76120d8b-e1e2-3fa3-a866-f88fbe11e59a | -6.80518 | -44.81517 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 145bc4f6-8719-3d1c-a49c-96965c006b9e | -6.76316 | -45.45772 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f071a60-a00a-3e94-a849-b102b4fc490c | -5.18452 | -49.35191 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcf4c5b3-8ab2-3bd0-9ab5-a28098690910 | -6.65304 | -45.89694 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15500edb-7024-3a3c-8ae0-8d5b40119306 | -3.04289 | -51.25415 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce7d93c2-73cf-3387-b6e1-9a3308b02dd1 | -6.24124 | -51.69983 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f34e202-1d54-3a3e-a271-7dd482f7355a | -2.94537 | -50.39292 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e60be2f9-3fa2-3689-bcfd-ec76b7ad01f2 | -5.02192 | -49.99792 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 310d07f8-70f2-3e03-a55b-c589bee75cb7 | -7.01676 | -44.6361 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ee5166d-202e-3350-9b66-3658095c9552 | -6.52364 | -42.24158 | 2026-09-13 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ae1b9fa-40b1-3a56-a87e-d52f2f01edb6 | -5.48409 | -45.60158 | 2026-09-13 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6f347fe-4e50-3b95-9efd-ef4c50d11555 | -8.97772 | -44.39077 | 2026-09-13 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66f4c8c2-0ac8-39e2-8c6b-9f572e65a466 | -1.87475 | -47.90613 | 2026-09-13 04:14:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 597c0887-4836-3158-a95a-f3578dcffd5b | -6.8339 | -43.50773 | 2026-09-13 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d0c0fa7-b924-3f59-a30c-ec1896ecdb32 | -10.264 | -36.2948 | 2026-09-13 04:14:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 27b9bd0e-6c81-3333-9e5b-7d304704e0d6 | -5.61078 | -44.84705 | 2026-09-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1180d60a-a016-3e83-9e48-7143b9f319c3 | -7.61257 | -43.87946 | 2026-09-13 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d968cf1-bea7-3ef6-89d2-d9ebfa3aae58 | -6.51187 | -47.60268 | 2026-09-13 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad5513bb-e77c-3496-828f-c4837bb49e86 | -6.24175 | -51.69688 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb895d7e-a77e-38eb-9479-1bdb32703233 | -2.53618 | -54.662 | 2026-09-13 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8224eb2d-145f-32ee-9a60-0a2f5fb49ccb | -4.40092 | -42.33663 | 2026-09-13 04:14:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68273fb7-19a8-36e7-a188-7fc02716543c | -7.02068 | -44.63304 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f125bc6e-2eb2-3f8c-a328-e52c165da114 | -2.21579 | -46.00104 | 2026-09-13 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39b52189-2fb5-309c-a33c-36ce581dcc44 | -2.96185 | -50.39884 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c4a28ef-515a-385f-9b65-cfa47353e0ce | -5.13511 | -55.96591 | 2026-09-13 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 72cecb16-04d8-36a8-ac98-179cea3f4714 | -5.2 | -45.26527 | 2026-09-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77e46b36-7e57-33b3-afde-37288c995ba9 | -7.02402 | -44.63358 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 29c356fd-87db-34b8-bce9-efdb8fb34763 | -1.2242 | -54.12404 | 2026-09-13 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dfc17321-07dc-3896-b5fb-16f979f1b5c5 | -2.11806 | -47.12283 | 2026-09-13 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73a0071-5a59-3964-afb0-b8d07074ea79 | -3.87332 | -51.19377 | 2026-09-13 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d118bacf-f30a-375f-b74c-fa1dbebe9b3c | -4.93144 | -47.71 | 2026-09-13 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d44be620-cdea-3429-a6c1-ec5afa505494 | -3.95439 | -47.61473 | 2026-09-13 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c91c97ba-34d4-3223-a507-23b418d179d6 | -6.79642 | -43.02768 | 2026-09-13 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2d9d01a-435e-3fce-9282-89c584e67e43 | -2.1127 | -48.99548 | 2026-09-13 04:14:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9353f264-284a-34db-b116-4a63f828ead2 | -6.23373 | -51.68308 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1f0d4a4-d1ca-35dc-9e1a-7d1e0d5bd902 | -3.78928 | -48.93719 | 2026-09-13 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7af2d3b3-3bf1-3568-957e-028088783c5b | -3.04605 | -51.26759 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abcd10a1-37a4-3d28-9c54-09a2b560d166 | -9.59831 | -40.35441 | 2026-09-13 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 09f6d360-bf40-385c-a3b8-3d12f7b59a04 | -7.52721 | -47.33788 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README20.md)
