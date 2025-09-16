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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2543512-6998-35fc-b89d-e22fbc007b15 | -12.10818 | -44.82362 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0c73c94-6c92-3318-821c-18e68c34b746 | -7.67272 | -45.13509 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16b4c42a-b6cb-3065-a2f9-604be045d328 | -7.44509 | -46.16519 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb3b96d5-4b13-3422-bf42-27aae5da893d | -11.91135 | -48.56115 | 2025-09-16 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d43dbc30-1a6a-35eb-aaa9-ab11f72bdee0 | -12.8058 | -47.94252 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64dbb28e-287e-35f1-949f-b2a684a89aed | -12.96741 | -47.9655 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c5431ba-e110-3452-9715-ed85a2f442d1 | -7.71926 | -50.36369 | 2025-09-16 04:29:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69eb61fc-5243-3435-80f4-d3345f0e85b7 | -11.43651 | -46.93132 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0ec77cd-38ef-3005-b114-36f10ad2123c | -10.72341 | -44.74759 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6856eacb-863c-3261-a33c-9bd9cfb84750 | -12.62642 | -45.7518 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b52d41a-4472-313b-8395-48394fb4643f | -8.60822 | -45.73466 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ffecd6b8-0d3d-3037-894c-e21ab2013b60 | -10.95913 | -49.57029 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32365a94-a145-38da-93d9-dfdd1e7ed23c | -7.71234 | -45.30386 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b0e3608-4e13-3b3d-9e15-6525e323fad4 | -10.05809 | -47.17899 | 2025-09-16 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f44cb8d5-c30c-39d1-8639-fa2e51971b3f | -11.1329 | -45.34982 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 442d5abc-d916-324d-8cf0-0443bd03e4d4 | -13.26084 | -46.89169 | 2025-09-16 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a03949a-6b78-3aae-8e55-695c4aa38b5f | -9.09043 | -44.80672 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cb21b7f-eadd-3ff8-b851-386444d3e0dc | -13.00073 | -47.94917 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d3bf80a-0157-3c2a-bd0f-3ab671e36e2e | -12.64771 | -47.95686 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20183ad6-41b2-33d2-a1a1-486119ef9322 | -13.00016 | -47.95271 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24e0b210-f2bc-3a9d-81b4-00f9211dadfa | -12.67106 | -47.93888 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a055bb2-f18f-387c-b9d9-c71f40f450db | -12.0595 | -46.53637 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2d0ddcd-1c6d-3315-a2c3-77d881716261 | -8.76281 | -48.80382 | 2025-09-16 04:29:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f9a635a-4479-34fc-9e5b-e84578bcca11 | -11.42595 | -46.93328 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1258df7c-840a-3672-ad51-1a7ca2c40760 | -13.20028 | -47.30448 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b71feec-e9d3-38c4-bcf1-6fac23696bbe | -7.38824 | -50.0017 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b761efaf-3d21-3c1b-a13f-6ae0c032e62e | -7.67024 | -46.30471 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c04675de-5cb6-396a-9ec6-0731bd540475 | -7.38597 | -49.99236 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76daa315-540e-36c7-9215-2ffd337dc0f7 | -11.13232 | -45.33038 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfcf2294-5ace-3bb7-a015-b9e640ed7b75 | -11.11336 | -45.33904 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5050678-858f-3ebd-b615-bccecf68c825 | -12.95466 | -47.95979 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78f8e072-79ec-3396-ad36-77c57cb7e6c3 | -11.21097 | -49.31631 | 2025-09-16 04:29:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6692b502-f372-3333-bdab-91e3485b51f7 | -9.09098 | -44.83742 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e3b236f-f650-3faa-ae95-b1166a8d0232 | -7.98619 | -45.64887 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ff77cc-fc58-3453-926b-9808ad556337 | -10.16397 | -46.14121 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34829e01-9ba8-3ded-9bc6-998c1ee7070f | -12.11532 | -44.81494 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a70a88c7-1a71-3079-a452-147d679588d9 | -8.11862 | -48.27309 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 133bf534-db08-391a-a4e2-697d8d42dc26 | -11.63427 | -46.58758 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03e29441-3bad-33a1-a42e-973b5e975058 | -10.73571 | -44.76169 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a925dd9-983b-31bb-b148-d148d8676770 | -8.39425 | -47.26078 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e02fc6c-2a27-33d6-b558-87dcac092b61 | -12.65867 | -47.71524 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6011bc9-7925-33fc-8c7b-4c1e1e3e3449 | -10.96261 | -49.57087 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df083877-6557-35cf-a2f4-1789c81d141c | -12.80658 | -47.18643 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1028d174-e2fd-3e98-8327-e028f1a4cf7a | -11.04198 | -48.271 | 2025-09-16 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe2e6ff8-54b6-3972-84d2-17af36bb53c8 | -10.72577 | -44.75595 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 52a4e3b1-58e4-380d-b0cf-4cbf57e0eccb | -12.24889 | -46.75409 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cf58289-7e07-36c9-91a1-bae6b263188a | -12.64427 | -47.99994 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2b760b8-1ce8-3825-b46d-49759e1289d6 | -11.7043 | -46.87959 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0254a2ad-768f-32d9-b2fa-a4234ec23831 | -10.65396 | -46.46593 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25238d30-aa56-3eac-bbea-e8eca943dd16 | -11.27786 | -50.8014 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43cd843c-d268-3517-82d0-b34de9dd7c4f | -8.27933 | -46.96631 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83c60709-3f79-3f77-b665-d81aa54f918a | -9.73675 | -55.37048 | 2025-09-16 04:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4dd35d6-c9f2-307a-aab6-e892f6a2077f | -10.6627 | -48.76284 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00398af9-13f2-3659-af3f-617b37de0835 | -12.11946 | -44.81145 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa119b03-3b16-326c-b9c3-a87d1256e5e9 | -8.61628 | -46.3971 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0d0a92e-4393-36f8-a71c-c7d27f9e035f | -10.71027 | -44.73825 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1ec64101-6274-3bdd-b1b8-d153e87539b4 | -8.12085 | -50.17429 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22bfbdbe-3a2b-381a-99ed-667570dd799f | -8.13618 | -43.64847 | 2025-09-16 04:29:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 077e083c-8fe3-309f-9179-5b81d9195096 | -8.1132 | -48.26538 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| befe69a0-db24-3665-961b-c0597742aeb0 | -12.61107 | -47.95083 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 337d289f-4462-35cc-8a50-1c8263ce9c24 | -12.97407 | -47.96658 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 989f64b1-f82e-358b-924f-fd9ca31ee2c9 | -12.44424 | -49.69839 | 2025-09-16 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1c8a4ec-6d28-3a3d-9b9d-8a9079f5924f | -12.6476 | -48.00048 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 903d2992-219c-399e-b9aa-2fc40802c2bc | -11.43373 | -46.92725 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b04ac64-4da8-320a-bc24-4c7e372b8c52 | -12.61046 | -47.97617 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69e12215-3e78-3d0a-8c47-42b35ebff4ae | -9.0994 | -46.93216 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf277c90-675d-319e-a484-ac9f981fa9f7 | -10.72112 | -44.76313 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d1801c5-7331-3066-85f9-05ecad47a657 | -12.44232 | -49.70982 | 2025-09-16 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee497852-3dca-3738-b77c-b12c6ad80656 | -13.21637 | -47.28898 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8177927d-d527-3421-aee8-80322c74c2d7 | -12.0567 | -46.53226 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d615f9eb-b543-369b-b715-c925f2e2fa17 | -10.71472 | -46.50793 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ea916df9-4224-3d56-aa0a-d863ed0c8141 | -12.11529 | -44.82466 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95fc3378-d84e-3619-bb54-43adccff23ac | -8.00644 | -45.66338 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fdb1e1e6-0b67-30cf-95f6-ce2e6240bd4e | -8.19398 | -43.7606 | 2025-09-16 04:29:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7c79010e-b41d-3bba-8c4a-375d50261b19 | -12.29914 | -46.40761 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f39ddbb7-7e61-320a-bfe5-bd87786475fd | -12.77467 | -47.96646 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bcc18be-1f81-38b3-af57-f43f992fd393 | -12.76689 | -47.97244 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d89efca1-c463-32d1-a7e0-87b326bed92c | -7.6829 | -46.30667 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a2b8d3c-2d79-315e-89c6-cf9661cecef2 | -7.14105 | -47.98931 | 2025-09-16 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 829f3fc4-5cab-373c-92be-c8022ad938ea | -12.61328 | -47.95846 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4269c5b8-99c4-334a-8bc9-2318f956272c | -7.67522 | -46.29479 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9b869d3-09e0-3b24-a48f-f3e1e53b4661 | -11.42317 | -46.92918 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 199d1261-5d3c-3992-ab91-5489cbb96448 | -9.05189 | -47.02132 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb2a4c85-21a6-3ef8-b27c-8416599932f0 | -12.69915 | -47.74004 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e685a2f9-57ae-37e0-b75b-de980df066fd | -12.61209 | -45.75341 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01429c7b-bfdd-304e-a827-61c3039b4729 | -12.79711 | -47.24704 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea974c1e-83c1-3a95-ae9e-32b27d9fd41e | -10.11558 | -45.66424 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9a984f9-41cc-30b6-a480-c08ec1045561 | -7.90072 | -46.23708 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13c1f2e1-fbaf-3fa8-b995-32627c37c9c8 | -12.26783 | -45.29581 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e155fb0-be40-3a80-9909-f219a37e12c2 | -12.66773 | -47.93833 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94178ba8-464c-3616-8040-e173289796ac | -10.79327 | -45.9768 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6478c7fd-c012-3044-a3b7-5332f5361667 | -8.20741 | -45.55201 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea5ddaa1-c662-3732-ab2b-edae4eb57bd7 | -9.45631 | -48.59744 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 585bb9db-5e94-33ba-9d77-6613145b79a6 | -9.00255 | -47.05287 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e1efc0-ec85-37d2-8123-b616903351c3 | -10.89472 | -47.79409 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afe39c81-046b-3670-8ffa-a5e6216c17b0 | -13.01956 | -47.95953 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0168fdfa-fb4d-374c-8377-97ea420fa5b5 | -8.12441 | -48.25901 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7acb0561-88d3-3c61-8524-5c613bac74e7 | -12.68373 | -47.98823 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4102749-8879-3435-a716-e15dca878f28 | -13.02233 | -47.96362 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ea4556c-99ec-346f-b223-c53bc054d126 | -10.79665 | -45.9773 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README40.md)
