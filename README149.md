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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acb21c59-6b94-3f01-a987-e77fddc249cd | -9.89322 | -44.79774 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2450092a-648c-34a3-bb16-30fe0a9bfc78 | -6.17272 | -52.85903 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9510bc1c-409b-3373-ad22-7447a8fedcb2 | -5.83012 | -52.03223 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d25a7b9-8f8c-38d4-bd4c-e7cba68c1daf | -10.30942 | -46.59455 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f430aad-1353-3f55-8005-8245093f8cd5 | -6.7324 | -48.11462 | 2026-10-09 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 027a2e18-c91d-3e94-9954-031fa2667584 | -4.37007 | -54.75224 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d52887a4-4c1f-3ca1-93db-e90f0085c09d | -7.5071 | -45.76315 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d358a76-c552-3877-a2ac-a594036bf5c9 | -5.09046 | -46.13464 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 338d6595-334a-3903-8612-37c5ad4e1d3a | -3.29052 | -54.08392 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3e500d3-9d68-3f3f-bb5d-7f49e3fb675f | -3.87952 | -55.99126 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75fb1096-f31d-3eeb-a9c5-ac3b98f7addf | -3.05217 | -54.26589 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b51c5fba-cc7f-3200-9fa6-1addf21dfc1f | -6.94338 | -59.09934 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e007e2b-9b2e-3523-95f3-67e0bc105fcb | -3.31031 | -54.70432 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5b2558-32ff-333d-801c-f1f64edc00cd | -11.31667 | -44.82838 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cd2986a-5a1c-34a6-a82b-4268c78234d8 | -3.59126 | -61.6143 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4a28979-25da-3e93-8757-6140a7b6a0be | -11.66039 | -43.68519 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df634bfe-d7ac-342f-b6b6-c728ad343381 | -3.74343 | -55.94812 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc014a3-2bba-3843-be02-0e21f1e3811e | -11.05634 | -44.05698 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe479ead-6168-382a-842d-6d8e0c84e997 | -3.2351 | -53.88892 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a7e765e-e282-3a71-8025-3b9b851431ca | -3.05939 | -53.9314 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e7a15cc-4b48-39b6-9cd6-1dad6f0ec85f | -4.28795 | -60.01439 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a7214e8-ff77-3055-8300-acb013888957 | -9.80131 | -44.76899 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe4d0368-7651-3587-ba70-05dd4c4f8c22 | -3.28538 | -54.00485 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43646ea8-aeb2-3eb2-9550-fa709fc7cd2f | -6.12892 | -55.68177 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 018ba525-1cf4-3625-942b-f3129a57c09d | -11.99053 | -43.4799 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2740622-a8f5-3d5e-a836-08a117db3051 | -3.07974 | -54.27408 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07db8f60-2012-3a4f-b118-3f7d43af6e3a | -5.17076 | -45.60315 | 2026-10-09 05:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5d4cde6-ee0a-303d-83fc-fc9b19b01d15 | -3.00241 | -54.79126 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0ac3808-6637-3c76-acd5-6eb80d3526a4 | -3.31692 | -54.05284 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 106901ef-e3a8-37ab-961a-e90c261a38ff | -4.66219 | -55.94747 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6370511-e558-3f81-9a3f-b60871217ff3 | -2.99747 | -54.06724 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 897261c8-e9bf-3938-a47d-a5e233bfe6e2 | -3.69974 | -53.66763 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99de30a1-96ee-39ed-8ce3-72fb2dd5b7de | -5.0861 | -46.13404 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5b19b08-3b46-38e9-a3d1-1132dcca3fe2 | -11.19813 | -45.32396 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7500e42-19be-3623-9b6e-c18e56b14250 | -2.94847 | -54.19421 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b049a1b7-1fe2-3e90-a905-1be8f64855a5 | -8.23292 | -54.74733 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41319a84-5e24-363c-9b46-23054e61a390 | -3.08226 | -54.28154 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 934dbd6f-41c0-3c47-a913-ebcbe5ee7d25 | -4.58032 | -54.9486 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6bd0585-cb51-306f-ab8e-d54f67c6ac55 | -6.87714 | -45.89541 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c00e46d-83e5-3f0c-a3b5-f8cf84cea399 | -3.09995 | -53.76799 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e2a73b-3d03-3f3b-b763-b10b24d2993f | -6.1101 | -51.73617 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13803a54-5671-3805-b19a-d66ef965a7c0 | -6.49932 | -55.38328 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0f91042-8242-34b3-8fb7-c6ccea5fe992 | -4.45866 | -55.40117 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0517de9-2cdf-3974-b722-076d2f322ec0 | -3.59311 | -61.61308 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 138ddb4d-bc2d-3eca-87a4-bd3ff393ab8c | -3.1153 | -54.1673 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d8f3f061-fc87-3de1-9c65-5223464029f8 | -3.04035 | -54.27205 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31a3b81c-6708-3755-960a-881ccf9296ba | -3.1098 | -53.92785 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ac169a4-8f2f-3038-9c4c-343f17476fe9 | -3.13365 | -54.36625 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb5a682-f815-33fd-be28-25a1f7d21056 | -11.26529 | -46.2687 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa902f18-7c49-3e9c-831b-941a03b1288f | -3.39147 | -57.99278 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7864616-953e-33e1-a0d4-c8fcd8e98693 | -10.0256 | -48.03624 | 2026-10-09 05:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be3bc621-7b19-34f3-b31b-47dea6ec6a17 | -3.48532 | -50.49148 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f0d0ff9-042a-3e8b-b668-8e4da9a15a92 | -6.48857 | -62.85788 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40fc09cb-750e-33db-97b8-ceb79c9ecac6 | -7.47669 | -42.85676 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73328777-1d07-38b1-b590-913599a094bc | -11.06949 | -44.08405 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79a15717-634b-3b8d-abae-627a669eedb4 | -3.294 | -54.08447 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54ab88dc-f340-3fe6-ac36-6925c265f87e | -4.22409 | -59.54461 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f62b1e4-426f-366b-b46f-010030a36b98 | -5.26284 | -47.90839 | 2026-10-09 05:04:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9b21240-4def-348a-96e0-8f01e5d855e6 | -5.57352 | -47.4263 | 2026-10-09 05:04:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23b5469b-0d29-301f-9659-e3f0075d8206 | -3.01722 | -54.08129 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a7736c-5d62-36ce-b9f8-ef1b903a56f8 | -2.73597 | -57.46704 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34cba83f-d289-3de9-8056-dee496f90673 | -3.01445 | -54.12034 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac882519-aa4b-3730-8caf-f340011057e3 | -3.60481 | -61.6354 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22fbbdb4-bc34-3f6e-a3bb-036ec2394837 | -6.62308 | -59.9405 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec0b3609-9617-35a9-8939-caab36fc9418 | -3.73602 | -59.45268 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da479a30-a602-3abe-b10f-83784247a71f | -6.12246 | -55.69813 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f570717-d3dc-3d41-84ab-6fe78ede8ded | -4.39188 | -56.04527 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59d8239a-4221-30ea-989e-c6810b1288c7 | -3.96173 | -51.91486 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d383b3ff-8526-362b-8537-5e9b4a36ed5b | -5.91403 | -53.88103 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11ef1ef5-302a-33ce-997c-a80c1559677c | -12.0363 | -43.44724 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e93ae52a-5a3c-3605-a655-3dedefd11aca | -3.08063 | -53.95429 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56cdfd49-ea07-3662-8f12-8584b5d6502e | -7.7936 | -44.57584 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4368d6-3bb8-3c15-ae64-9705612ab27e | -4.07756 | -59.83482 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8228004e-2151-339d-974e-13f24f356fa8 | -3.71453 | -59.64429 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3344f2e7-44ab-3607-9fc5-efcb81b28c1c | -5.68954 | -53.49531 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d00b5465-d9d8-3f53-920e-6f3f39bbd913 | -5.26209 | -47.91322 | 2026-10-09 05:04:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e582bb85-8809-32a3-91de-65778b3aaaec | -6.39095 | -55.25938 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b4380d3-54e9-3587-95e1-5c19941da971 | -3.26167 | -53.9972 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33a0450a-0cbe-3dc8-a864-8e3dc7e9e825 | -3.10087 | -53.96145 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3211fb7-b369-3322-9b7d-f00909ea0f2a | -3.00385 | -54.0722 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e4e9789-61c6-310f-8369-62d9ccae21f9 | -8.3026 | -45.72436 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 621e0164-ed9c-3e1f-a45a-293745495901 | -6.16994 | -52.85501 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 877a017b-9d47-320e-8b06-bc4ec9b24c08 | -5.96792 | -55.34658 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c344b6d-41ac-3f05-9468-e6c94768d8e3 | -5.6756 | -46.3564 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67c9a2fc-acd2-302d-9aed-5e6bca427ee8 | -5.8246 | -52.04562 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f339a9fa-0c76-32ae-917c-bd4c589d39cf | -8.33184 | -49.12158 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13c762a1-eb9a-3143-88b5-21977f2009c3 | -6.09975 | -55.70022 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43b8317c-ada2-3291-8cb4-9cc80ab895a0 | -3.42928 | -54.54502 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e6510848-7725-3968-b238-86781ffba8c6 | -3.99336 | -56.25751 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c27546b8-89de-3fbd-a82a-ced35a9ed742 | -5.7064 | -53.46128 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd6715a7-128e-37d2-922f-207efc8f3299 | -3.1199 | -53.7981 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ea50b54-4a4a-387e-bdbf-daa147999c04 | -11.19535 | -45.30627 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3c2c345-1416-3dc5-9397-fb5e0429b9fe | -11.45674 | -43.37799 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9174ca7-a96b-3c8e-925a-0f7da5787e84 | -3.71197 | -60.54546 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de05cf98-4f9f-3d75-9d0c-243411c96d7f | -2.87955 | -54.19535 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53215a50-400f-3283-9943-c58da042d32c | -3.35973 | -54.74839 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e4238f1-fe8b-3e97-8840-88f548f1a88e | -3.85651 | -51.93724 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db1d194a-e697-3863-a508-976bec7194e3 | -3.10495 | -53.95818 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c07a912b-608d-35d6-8829-9167f3b546be | -10.74411 | -46.61239 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f14685b0-38ea-39ce-affd-dea1f6dad6f9 | -3.97964 | -56.11582 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README150.md)
