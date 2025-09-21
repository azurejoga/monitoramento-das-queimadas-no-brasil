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
| 8db2b050-04b3-3b6c-968f-c2adc0fadb91 | -2.61917 | -46.85731 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 584b84f8-ff18-3172-aa74-c7183342b60c | -3.60076 | -47.51746 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87a25d7b-faef-3241-99b5-ba7924d89c63 | -4.63545 | -45.61167 | 2025-09-21 04:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cffc29b3-854e-3348-b6cc-468883c65efb | -5.40702 | -45.27346 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7614d77b-e243-3137-9e81-a3c4532f83ad | -4.29755 | -48.27002 | 2025-09-21 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf3dbc78-efaa-3a76-a1fe-7aaa2a9e95e6 | -5.43303 | -45.5036 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 751c8506-c930-3115-8afd-8bd1a6646efe | -1.34614 | -47.7461 | 2025-09-21 04:34:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c4bfcd3-3389-3130-934f-cb505746ce50 | -3.60577 | -47.52888 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a1c418-2fe2-3006-906e-3c6c58292d36 | -6.01666 | -44.32988 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1cb226d-0757-3cdb-84f9-127d0ef067cb | -3.59466 | -43.91426 | 2025-09-21 04:34:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7d6db63-b230-3770-bb81-37d6ba39cb27 | -3.60299 | -47.5249 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c42eca34-b3c1-342f-947f-da0819eaac21 | -4.94683 | -49.92565 | 2025-09-21 04:34:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1964c74a-9208-35fd-a589-13377e5dc6fd | -0.94776 | -47.35353 | 2025-09-21 04:34:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 176a55ba-eb44-3835-a2ef-1b3200972ec8 | -1.25895 | -47.11431 | 2025-09-21 04:34:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92e4d9fa-52e4-3b8e-bf01-7d77e8393807 | -2.30264 | -48.1496 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d5646d6-0bb5-312a-af11-80eebfa4bbe9 | -6.01129 | -44.32692 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ed33643-959b-32a6-a91f-446ce70ca230 | -5.61093 | -45.46781 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fc1bc97-b77a-36ca-ac32-5189732b4a8a | -6.31497 | -42.37171 | 2025-09-21 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e402b860-0b53-36f3-afff-92c86fd66dea | -5.12135 | -45.44661 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6d925d5-fd20-3fbc-9eb0-c915f64596ed | -6.01361 | -44.32507 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb2fbd47-a4bf-38d5-bcba-91c9637dbe29 | -3.51336 | -49.93775 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 042aa0ee-fafb-36e7-9270-05014cdce455 | -5.41963 | -43.26227 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51726c06-7981-3497-8ed4-7f9d07951b3c | -5.63309 | -45.95048 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6953cae3-e61a-3c9f-9a0b-fca0a063ebac | -5.47384 | -45.37705 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcc8982f-19b9-3082-b15e-a9be91b5aa28 | -5.27629 | -44.81587 | 2025-09-21 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1c5d470-1e0f-370e-9a10-2caf22fe88c2 | -5.82234 | -43.87646 | 2025-09-21 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c92afe3-c956-306c-a722-9f7775d6d9e3 | -5.42619 | -43.27573 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fe1c88e-1989-3526-a39e-0ff63269f1ce | -5.63593 | -45.95469 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fbab968e-abcb-3ff6-b20e-76c10ec93252 | -4.93617 | -45.08149 | 2025-09-21 04:34:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15cd8fab-0baa-3535-b46f-5064dc0077bf | -6.01063 | -44.33121 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc4bd904-49cf-367e-a9fb-659b1398c230 | -3.60522 | -47.53234 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 953702c8-1064-32a8-a159-e4a8e2d45213 | -3.80486 | -47.57464 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72df45df-dcd5-30ae-add0-0feb103bdefa | -5.34746 | -45.00531 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5684b570-cc42-317f-8a98-53daacd2910e | -1.86306 | -47.98578 | 2025-09-21 04:34:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65b1f483-d18e-3423-981f-34aacc809fce | -5.34214 | -44.89869 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2e58f7b-c7f8-360a-894b-622c6172a5dc | -5.01342 | -45.20836 | 2025-09-21 04:34:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3275716-dd2d-359c-90f6-eb0b1d1a3ef8 | -4.79513 | -47.28334 | 2025-09-21 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a884023f-2c3d-3e37-8f71-92d90d90b954 | -3.36981 | -50.39754 | 2025-09-21 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49251eb6-91f5-3dbe-9cc0-b2fd918514b0 | -5.51939 | -43.86497 | 2025-09-21 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 935321d7-bda1-396a-a3dd-1e95facdaa79 | -3.29841 | -51.60291 | 2025-09-21 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63c1bdf5-be5e-38ee-b80e-a858501395da | -2.89893 | -51.47468 | 2025-09-21 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9c5b3a1-fbbf-32ad-918b-7f72877063f9 | 0.79125 | -51.96918 | 2025-09-21 04:34:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7641712-928a-3808-b1cc-220961c93069 | -4.4614 | -44.13668 | 2025-09-21 04:34:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4704941c-fc63-3e20-ae0f-957665b0f25b | -5.27272 | -44.81534 | 2025-09-21 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a96da92e-c624-3be7-85c9-38f83162f9cb | -5.47553 | -44.41837 | 2025-09-21 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccfe9c94-84b3-3dc4-afe7-3976e8dea259 | -3.35554 | -48.40137 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd3e0d7a-fd38-358b-8ce6-5f75b9b11267 | -3.51241 | -47.20279 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0f729ad-caba-34e8-9100-790371fd9f1f | -2.62576 | -46.83711 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9799c7fe-1785-336b-b862-1fec1ede4645 | -5.89861 | -44.34999 | 2025-09-21 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fe938db-884e-360b-98ce-a38278bf6736 | -4.32803 | -48.39032 | 2025-09-21 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78a03fb9-b177-3dcb-b2ac-429582499386 | -5.81857 | -43.87587 | 2025-09-21 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86eff907-713f-3122-9c12-1068dd5e0e3a | -5.52009 | -43.86043 | 2025-09-21 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4075758e-0e14-31b4-bbd4-c071317fb159 | -5.14794 | -45.70774 | 2025-09-21 04:34:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 664640b7-b639-3820-b2cb-0e43dcaf3f2f | -6.09077 | -41.00057 | 2025-09-21 04:34:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ba6375dc-4096-387c-913a-ebf0aa1ec550 | -5.45096 | -45.50251 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5d52d3f-2cd8-31e3-81e0-82fff85a40ff | -3.37049 | -50.39332 | 2025-09-21 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06338421-2116-32f8-b9b2-f3bcf1308a35 | -3.84521 | -55.60329 | 2025-09-21 04:34:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbd35d09-5cad-36f4-bcbc-90f74375a29c | -5.75825 | -44.19892 | 2025-09-21 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0dffd524-f2b1-388f-ad3e-d58ab877ca36 | -5.28855 | -44.6895 | 2025-09-21 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ade49576-7b39-3a02-a0f4-44fcfcc2b05c | -3.59689 | -47.5204 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c5d08e7-da64-38a1-b0e2-2b234f44bb34 | -2.60774 | -48.13515 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c9c78db-1e50-39f1-8095-2fb426f5b590 | -4.50874 | -43.52052 | 2025-09-21 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49d9b748-a4a8-3ad9-944d-6ab914aa5060 | -3.35667 | -48.39427 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2262abd3-3d82-3fa3-b31a-a7858c42fcff | -5.63024 | -45.94627 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cab86368-fa37-367d-b3ed-337d89e695bc | -3.72149 | -51.32966 | 2025-09-21 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 071c69aa-7d70-3f15-a30e-6fd8ae99047e | -4.63488 | -45.61538 | 2025-09-21 04:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bef6be52-ab7c-3776-8f77-baa97d404167 | -4.97062 | -49.50469 | 2025-09-21 04:34:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9db9a866-0b1b-3f44-a6ca-cf456a2f328f | -4.70992 | -46.47284 | 2025-09-21 04:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33727d64-a178-3cd3-8bd6-5030b5e535cc | -3.17942 | -48.60518 | 2025-09-21 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4723be-cba0-34e3-8e03-aca13ec647ea | -3.3505 | -48.38965 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0b47f5-3bf7-3b7b-a301-457308acc895 | -3.98362 | -51.06319 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 801adea6-e26a-3272-bb5c-a7142288003a | -6.30286 | -42.36312 | 2025-09-21 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c09bfa78-5c19-3b26-9da4-de401dc83c6b | -4.79568 | -47.27988 | 2025-09-21 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19724372-d845-3884-9560-253d74d9dfad | -3.51795 | -47.20723 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66db6431-51e9-3530-ac97-4e8486f1bd66 | -2.74251 | -49.54648 | 2025-09-21 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfe44a43-695e-333f-8567-817e497e82db | -2.26317 | -47.84596 | 2025-09-21 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0252702-94d9-337c-848f-c2a461d9cda1 | -2.30222 | -48.39165 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66b42666-3185-3649-ade1-62095b35159f | -4.79846 | -47.28387 | 2025-09-21 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f97b59c2-b486-373d-bc68-1e2ff08e6501 | -3.53745 | -49.98588 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97f1339d-eed2-3ead-ad90-78b2ac504ed3 | -3.75702 | -54.80851 | 2025-09-21 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf4eff9e-34b5-3294-bfc0-5d104e572e1c | -5.34275 | -44.89471 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24a9ae23-e0ad-3f2e-89d5-a1b35f3af76d | -5.47325 | -45.38089 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60607296-87b9-39df-ae82-94a5f68ba547 | -2.87137 | -45.75713 | 2025-09-21 04:34:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11bdbc03-d2f8-3855-a5ba-27ef97efc039 | -5.00992 | -45.20784 | 2025-09-21 04:34:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23b05211-40f7-3ee8-8a23-60d0a44e27d5 | -3.45502 | -47.6262 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 386411a8-83e1-3d49-ab04-a9c51befb689 | -5.58807 | -43.79453 | 2025-09-21 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d041b5ca-4fbb-31df-956a-f1d52f023f03 | -6.01432 | -44.33173 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f592313d-2498-3723-b50d-b7833814d958 | -3.62738 | -47.52164 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e42c1dc-b1bf-3cd0-957a-c1aba2b1f24c | -4.86004 | -45.89738 | 2025-09-21 04:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4215d60-63dc-3988-8294-183ea82b0330 | -3.51741 | -47.21068 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e8c1862-bbdc-3ac2-8742-300d7747231b | -2.2619 | -47.19365 | 2025-09-21 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a3b2dbd-5726-3314-b375-a3dc353db4f6 | -3.34656 | -48.39267 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b574af-384b-36ed-8096-b1bf66eeba8d | -3.80432 | -47.5781 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3b6a48b-979f-356e-a8de-c63ff3578680 | -5.97961 | -43.80474 | 2025-09-21 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52752206-fbca-3ad2-9002-2de426709cbb | -2.30165 | -48.39525 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16be45ac-67b6-3ef6-8f9d-b4d06c21001e | -6.307 | -42.36401 | 2025-09-21 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 09bc8848-b02c-3203-b595-266ab4e1e800 | -5.44749 | -45.50198 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b516e41-f469-3379-93d1-5feda09bb8d6 | -5.27991 | -44.72163 | 2025-09-21 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e373273-186a-388d-96d3-0b1d39c87fb6 | -5.19444 | -45.48824 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50dbcceb-cc68-3be6-b220-b235dfa3575f | -6.31549 | -42.36812 | 2025-09-21 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
