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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62d7ead1-8ae0-329c-892b-f2c81f710f7c | -13.30332 | -47.47743 | 2025-10-23 04:08:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ee9e17d-1f61-3621-8e0c-735d72b40e5e | -6.90194 | -43.59221 | 2025-10-23 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 647da936-c4c1-3dc0-ae9f-11f2c61484f4 | -12.55081 | -52.22069 | 2025-10-23 04:08:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ffbf38d-1167-3ed5-a4a7-2d66f52389f7 | -11.24706 | -49.87709 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d55193bb-8615-32c6-88a3-6f17e93dcb98 | -10.02526 | -47.06023 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab5b22b9-01d6-3442-b454-56be993d26cc | -7.16145 | -44.9945 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62ff5789-ae3c-3cdf-ae50-f5af4e40f4ae | -9.56163 | -49.63501 | 2025-10-23 04:08:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d32a0d07-c45b-31be-9bfc-49af8a227866 | -7.27317 | -46.16649 | 2025-10-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62bce9e1-4133-393d-a83d-e4129bdbab59 | -12.81943 | -48.63771 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 734d8894-c8c5-3a47-81ec-71a8879c9bfa | -12.67738 | -48.62963 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 861f528c-4520-3542-9bd5-092bbb12ee2d | -6.59613 | -44.3143 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67e99977-88f3-307c-a399-dcfb5e5230d5 | -6.53378 | -44.36209 | 2025-10-23 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fdedca22-917e-3d93-a1c2-d3bc7a62eda5 | -11.14588 | -44.94185 | 2025-10-23 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dd947091-8152-3cfc-b434-94beab03c14c | -6.77723 | -45.44635 | 2025-10-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f716eb01-50f6-3e1f-9716-1858c888b21c | -6.96838 | -44.00886 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2311bb0d-c53e-343d-bf08-eb610597545c | -11.00296 | -47.79799 | 2025-10-23 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eeb50ac-93e7-3240-8ad3-a9889a053dac | -7.03449 | -45.53996 | 2025-10-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f29707ef-0011-3f82-8e66-7e319c7ad5d6 | -11.3569 | -49.79337 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 75412542-945c-361a-9ce3-165332d150e2 | -12.7837 | -48.57382 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a21e11f-d37a-37cf-b0b2-feb242a4c38a | -7.15268 | -42.36389 | 2025-10-23 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39ff6b0f-8414-3389-a9c6-d8505e9b4389 | -6.90928 | -46.1275 | 2025-10-23 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ddee753-ca0c-3271-b684-64cb0cad91a0 | -11.00232 | -47.80167 | 2025-10-23 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69dd5ae4-a724-31a3-9a59-d44ef3325d98 | -11.99212 | -46.78146 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45ebf6fb-597c-3da3-acec-8b4e133de5c5 | -7.51859 | -46.88167 | 2025-10-23 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dabd96a8-aa5d-3f02-bdf4-ddd7782579a8 | -7.79451 | -44.00388 | 2025-10-23 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 328a319d-ac09-32b2-8b5e-6e4ce547d81f | -13.37424 | -46.64439 | 2025-10-23 04:08:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32bb785c-a5f4-3d6f-86e2-d849ed983f51 | -13.33415 | -46.59361 | 2025-10-23 04:08:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0a9af82-1507-3c43-b40d-4566cfb21aaa | -12.82461 | -48.65694 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 317d8da0-fe50-3f43-8ebe-f9dba1338689 | -12.67099 | -48.64108 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52f63079-7afd-3a65-9d7b-e52f81b1bbc0 | -6.79287 | -45.45146 | 2025-10-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 990823dd-921c-3470-a8eb-354aa03c5ff2 | -12.81943 | -48.63772 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 115b1fe8-3862-3459-8368-fd612b3776ea | -6.92586 | -48.26935 | 2025-10-23 04:08:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c88f60cc-d953-3512-994f-a6133954c0e1 | -13.33428 | -46.59183 | 2025-10-23 04:08:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0880fccb-9bf9-3910-9d2e-ba2e7d9de77d | -11.99654 | -46.7749 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc1fa5a6-ca1b-357f-b64d-2ecacba46f30 | -11.34726 | -51.44822 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f324081e-b28e-37e8-8183-097ccb06933c | -12.70115 | -48.836 | 2025-10-23 04:08:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41d7c6d1-7d30-3a22-b1a3-13a965937010 | -5.63624 | -50.03196 | 2025-10-23 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d01c52ef-dd21-3bfd-865d-5227bec8147a | -7.06341 | -44.09512 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e24a87f8-4f60-3a5f-bff9-a9e2d8da8b8d | -6.73466 | -44.1523 | 2025-10-23 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af132da6-51ce-3430-9a91-8ef1ba836110 | -7.51797 | -46.88528 | 2025-10-23 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5140d767-87b5-30d7-b4ab-ccdb279b110c | -9.2404 | -45.59806 | 2025-10-23 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd444a6b-0a5c-3019-996f-053915bfab9b | -13.32539 | -43.10343 | 2025-10-23 04:08:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee102d36-3d71-3ef0-9635-6c7694290ccd | -6.82172 | -41.41777 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4fe70921-52d5-31ec-974c-5f43cbae686c | -10.10282 | -47.74672 | 2025-10-23 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1892769-a52f-3e65-940d-922b1a743cf2 | -7.77924 | -46.32319 | 2025-10-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88a70730-d7cb-3bfa-9b94-472df2cdaeb8 | -7.18805 | -43.86535 | 2025-10-23 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3c4801-4d54-35b0-aeb4-2476a595c225 | -7.63889 | -42.17483 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef6646e2-350c-388a-99a9-ee1f71e3f82b | -6.73116 | -44.15171 | 2025-10-23 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45ba69f3-ce6f-381d-8480-14d828b2d2ed | -7.08223 | -44.65123 | 2025-10-23 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bce84109-c59c-3f18-8444-854a164fbb34 | -13.37558 | -47.26765 | 2025-10-23 04:08:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4d3ad08-2bea-33ef-bf9f-061ed3e4b890 | -13.37178 | -47.91182 | 2025-10-23 04:08:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8141e52f-2542-3826-bcb1-9fb95837d4b2 | -11.99505 | -46.78683 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6c55b08-a075-380d-8356-7de6dade4e7e | -7.68959 | -42.23978 | 2025-10-23 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| efa3fada-19de-3173-a858-f20be47acda6 | -13.4151 | -46.49315 | 2025-10-23 04:08:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2cc1ba9-f152-3f30-9b86-e2655982fc3d | -6.28495 | -47.01125 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77b1533c-a08c-3ca4-8dc4-ecc812bcdc8f | -11.12963 | -48.342 | 2025-10-23 04:08:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9182e415-73ee-3728-b992-98c6991f807b | -7.88964 | -43.54725 | 2025-10-23 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bdd3dade-3f6c-3ceb-8b5c-a9968d04bf09 | -6.47192 | -44.43161 | 2025-10-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67d202db-7ea1-3957-85fb-b582c6b39bbf | -6.77787 | -45.44909 | 2025-10-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6915ec51-3d42-3f74-8090-255941a620ab | -11.36062 | -49.79904 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ae2033b6-03db-3571-8b47-1e3d166d02eb | -12.80601 | -48.64061 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 277ae38c-f956-3ffe-b757-34b94a9ea397 | -12.7741 | -47.38607 | 2025-10-23 04:08:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff34ebbf-5fdb-3d28-ba55-4e3892b2c54e | -6.64664 | -43.60596 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a246e69-f884-3adc-b695-2c42a5d07c44 | -12.13056 | -46.72345 | 2025-10-23 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfa4ae7e-9725-3c60-a239-0295a447d5a0 | -11.07551 | -51.5686 | 2025-10-23 04:08:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e9cb898-bafb-3491-9662-442d99594f7a | -11.24797 | -49.87216 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3823bbc4-2535-3622-8f97-0cb3b1b3e2ef | -7.63119 | -42.20207 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 98be8690-f9a1-3218-a2f0-5b59f895ad18 | -6.3236 | -46.20579 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9883af9f-ef85-3bdb-ba70-eb95857e5315 | -11.14371 | -44.93341 | 2025-10-23 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd624ea5-4ce5-313c-a418-7d2ff804cd3c | -6.59755 | -44.21586 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9ac2680-8f7f-3e79-a793-74b09ce6f9b2 | -17.6167 | -46.614 | 2025-10-23 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 0612f77d-13ba-3e3c-9fcd-51b7f72a0e2b | -17.5967 | -46.6182 | 2025-10-23 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 62420728-ce6a-3371-a85a-640f78d4a234 | 0.3773 | -50.9413 | 2025-10-23 04:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 35.1 |
| e20f27eb-8546-3cbb-992a-a1ecf376fe5d | -9.6295 | -40.3392 | 2025-10-23 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| c280667c-41bc-318a-8fd4-38ab63e6f9ad | -3.0169 | -49.4694 | 2025-10-23 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 16274d83-c48e-3da0-8e87-51c87be6b0ef | -3.0168 | -49.4906 | 2025-10-23 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 85566338-d8fd-33d0-84a5-101a4718eb5e | -17.62066 | -46.62788 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb59eb4f-58b5-391e-9ebd-d0fe80ddc606 | -17.60531 | -46.61259 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fd30f9d1-4582-3f0a-a629-3cb54acafe81 | -17.60737 | -46.60054 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9759795d-cdda-3b05-8ef9-766d8d4a9c7d | -17.6109 | -46.62191 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 17283b95-3c18-3672-ba0b-da28f023a92f | -18.69707 | -47.05283 | 2025-10-23 04:10:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31cb450b-ebf8-344b-aa02-2f8c94fb7f98 | -17.61576 | -46.61453 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cbe9d3a-16f1-3b53-9a1e-152059cc8d17 | -17.59766 | -46.61532 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 921637e2-464a-33bf-bbb5-cd625693e144 | -16.07461 | -51.40627 | 2025-10-23 04:10:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a80d136e-be08-38bd-b7df-1804cc89d76b | -13.58667 | -48.58813 | 2025-10-23 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4855c4fb-88a6-3ece-b654-06e2d04cb388 | -19.15436 | -49.13397 | 2025-10-23 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 821992ac-c1eb-3e96-b0f8-19c0e8dc1bb7 | -20.1767 | -45.52221 | 2025-10-23 04:10:00 | NOAA-21 | JAPARAÍBA | MINAS GERAIS | Brasil | 3135308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbedc862-1231-3de6-b273-504e999d14e7 | -17.79412 | -47.62511 | 2025-10-23 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 842669d7-85ca-32ae-b63e-101a9a1da6f9 | -13.8938 | -48.37481 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ea2ced8-d96c-321c-b27b-2237579e1e6c | -19.77414 | -41.29828 | 2025-10-23 04:10:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dc44e865-da2d-37ed-96af-4705fcf62f09 | -17.6213 | -46.6031 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b660eef-15de-38a1-a0de-e43f887da4db | -17.59907 | -46.62807 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42884ee3-b0e3-394d-aa4c-fc910c7d9e63 | -16.47921 | -46.47422 | 2025-10-23 04:10:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79e2afd0-3e79-3a01-89a0-6aa22a4d0089 | -19.37549 | -45.83939 | 2025-10-23 04:10:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e4630fb-de7d-369a-8d24-5edb42494b97 | -17.61997 | -46.63192 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d3d997a-78b9-33a5-a2f9-f14fde29195b | -17.1497 | -53.31445 | 2025-10-23 04:10:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e29e231-cab7-39ea-b16e-1c76778c3f26 | -17.15039 | -53.3111 | 2025-10-23 04:10:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3fd7e43-60a3-3e60-ba8b-722e265da392 | -17.55603 | -51.0406 | 2025-10-23 04:10:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53c2f934-3806-316c-9bb7-a2d6a4ce3970 | -17.64927 | -46.64981 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7f5c8519-b0c3-3989-b000-edab852aff4d | -17.60252 | -46.60793 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
