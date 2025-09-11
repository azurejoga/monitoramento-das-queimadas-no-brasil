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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c62290e-8254-3d9c-8a0e-5a674828ac6a | -12.6829 | -45.2746 | 2025-09-11 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9716b135-893d-3991-b6a4-2afc804a842b | -8.5667 | -45.5842 | 2025-09-11 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| e47f71eb-4776-3d5b-9fa2-49d7f42cfbcd | -6.4927 | -44.4801 | 2025-09-11 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d55acda0-db29-37c1-a1d6-ca731f5d0aaa | -9.0579 | -46.9688 | 2025-09-11 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3b18dd2d-dd7f-31ae-b251-41b808e11019 | -8.9368 | -46.132 | 2025-09-11 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cff7ba99-9063-32bd-902e-6a67e24a9861 | -9.7445 | -47.8468 | 2025-09-11 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 4f13d5b2-8e50-307d-a58e-2a21418a60cf | -13.2027 | -51.7618 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 1d6de24d-fc0c-3d43-9d24-aaa56e31ab1c | -13.2407 | -51.7784 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2ff429bb-9905-3a06-bc0f-13d7d8e7b50a | -6.8525 | -47.8707 | 2025-09-11 13:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 073fb56d-0945-35fb-96f1-99a64496fed6 | -7.8708 | -45.5181 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9f7f455f-72c0-3798-9dce-a75aec141ecc | -8.3302 | -44.9032 | 2025-09-11 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 08e2354c-18b1-3a9d-92cf-c802a0c58bac | -9.0265 | -49.5046 | 2025-09-11 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d60ee82c-ff37-3d06-88b0-9ab7d4727843 | -8.7361 | -47.0904 | 2025-09-11 13:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 73257334-d2e7-362b-8417-72d850fb2aef | -11.7399 | -46.5326 | 2025-09-11 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| cb179510-32e0-30e2-b29c-03e2d268f431 | -8.8755 | -49.5613 | 2025-09-11 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 237c5ce4-5775-37bc-8039-9de2731da572 | -6.2226 | -43.3459 | 2025-09-11 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 67acc01e-7cba-3a68-b009-03861626b748 | -6.4364 | -44.4847 | 2025-09-11 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0bd32cde-63d2-312a-b9ce-73cb5b4bb0a0 | -13.2602 | -51.7548 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 128934b9-5d37-3ca4-90c6-759f0a325cc7 | -14.1492 | -45.4009 | 2025-09-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b7d7c958-7302-381f-96c5-6402e29feeb3 | -11.4285 | -43.5544 | 2025-09-11 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 92f88e1c-1e80-3697-941b-a9294a40a840 | -8.9365 | -46.1545 | 2025-09-11 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| c274f1b6-be0c-393d-99b8-943e4548a31b | -9.039 | -46.9707 | 2025-09-11 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f295034c-8283-3394-8fab-45d94cf3e2e8 | -13.2798 | -51.7312 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 81541a35-400f-3101-ae44-bb23aa2b49b0 | -16.6335 | -49.7683 | 2025-09-11 13:10:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 189.3 |
| c0373460-7f22-3b00-bf47-c401bef9bfd1 | -11.779 | -46.4821 | 2025-09-11 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 3cb29552-35bc-39b4-86c0-c9dd309e9cff | -9.1331 | -46.9831 | 2025-09-11 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8d237913-3cf6-3217-a2e5-e93136589889 | -9.4804 | -46.4321 | 2025-09-11 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 39661bb8-3a7d-3192-8d88-052a378b8c43 | -19.2611 | -48.0221 | 2025-09-11 13:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b2fa871e-4702-3fb2-b6fe-8a0cf403e6f0 | -7.5215 | -48.2753 | 2025-09-11 13:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 11b6f3bd-943c-38db-bf2a-61852ab733f5 | -11.4093 | -43.5573 | 2025-09-11 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 418d15fb-0289-3feb-8202-5ce2cf0eb4b6 | -6.0784 | -44.6961 | 2025-09-11 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9b48cb50-b3fa-3d80-998e-7b0d22fc8f5f | -10.7366 | -46.1011 | 2025-09-11 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| cf12c16d-0b55-3b87-beed-d8417e4d6f72 | -16.633 | -49.7905 | 2025-09-11 13:10:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 60895aef-019d-37b5-a5cf-8252909f6139 | -13.2599 | -51.7761 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 964741e3-4321-3d28-8a66-d7f64aed4e62 | -8.7547 | -47.1107 | 2025-09-11 13:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c7cb2ef2-c1ef-3585-8e2b-79138f969519 | -15.1016 | -50.1468 | 2025-09-11 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 6691f225-ee8b-37dd-be2a-6accb365bf78 | -6.3226 | -53.4553 | 2025-09-11 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| ef3b8f93-1bd3-34a3-a9a1-c3ad13c286da | -15.6732 | -47.0389 | 2025-09-11 13:10:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 316.9 |
| 7b938952-2f22-3645-94dd-6e43ce625410 | -8.1649 | -46.0983 | 2025-09-11 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9c771a7e-835f-3413-b97f-627031a7eb0b | -14.5125 | -53.9367 | 2025-09-11 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| c99bdbc8-0101-31e8-9ce0-80ddd739198e | -11.7786 | -46.5047 | 2025-09-11 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 6e95cbdd-71f7-3827-bb86-818ca2aa8e81 | -10.5674 | -47.2219 | 2025-09-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 5c13d5c7-019d-3985-a5f2-5bd5b345b5cc | -9.1328 | -47.0054 | 2025-09-11 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| cf5070a8-34d9-3bc1-8c53-bb05fdb0a366 | -15.6737 | -47.016 | 2025-09-11 13:10:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 23cf6dae-1f0f-30b6-912e-002c14fb0f68 | -14.5128 | -53.9158 | 2025-09-11 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 1462d2f4-72c5-3d8a-97a5-bf06808ea9bc | -7.852 | -45.5199 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 553ff409-1fe5-338f-b015-1f673912e4d5 | -9.1514 | -47.0257 | 2025-09-11 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b538abc5-8293-36da-bb89-8286ae87e9b4 | -11.7211 | -46.5127 | 2025-09-11 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 46686378-c7f4-3941-8f9c-cb8b181df86e | -6.2228 | -43.3226 | 2025-09-11 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 28a6bc42-7223-3be0-ac81-49eb4c4557f2 | -15.1211 | -50.1438 | 2025-09-11 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3539944c-f91b-3438-bbaa-615c97593283 | -10.5671 | -47.2442 | 2025-09-11 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 0a99b0f6-af10-3f31-a079-c05aa8df2436 | -17.3749 | -52.9341 | 2025-09-11 13:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c60ae9bb-aeeb-35f8-9445-e646eac33570 | -6.4925 | -44.503 | 2025-09-11 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 5e03020d-d3f2-35af-9f6a-09063ecc792c | -11.4281 | -43.578 | 2025-09-11 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 6cf16b55-e5ad-3978-98de-512da5b8d287 | -11.7112 | -48.2757 | 2025-09-11 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e8dc6d65-9f9e-391e-a0b8-04f53148b04a | -9.4801 | -46.4545 | 2025-09-11 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 8cc03ee3-aaa8-357b-b68b-305f995e332d | -11.3584 | -46.5167 | 2025-09-11 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d7dbe9b7-30a7-3dda-ba56-9e5dd909ee8c | -16.6138 | -49.7717 | 2025-09-11 13:10:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c00490af-d441-3f0c-a62c-724c90ff45f1 | -8.7411 | -45.2248 | 2025-09-11 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 225.1 |
| c994a6cb-1a80-3309-8b59-e6a805c49d81 | -13.241 | -51.7571 | 2025-09-11 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9fa4a382-f742-33b6-bb86-61c0e7878ef4 | -9.0942 | -47.076 | 2025-09-11 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 7715a053-8846-3c0d-921c-b079bb1486a2 | -19.2611 | -48.0221 | 2025-09-11 13:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4ca2f4ff-b36a-32ef-a314-d5c952bce96c | -9.4804 | -46.4321 | 2025-09-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c3d2666e-b6f7-3c22-9b91-59b739c1085d | -10.7557 | -46.0987 | 2025-09-11 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3b4b9766-da0a-3bfb-b41d-84c6a57d5f62 | -12.5561 | -49.1535 | 2025-09-11 13:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 3ea1c964-0964-39a0-91cd-4fbb17df022c | -11.779 | -46.4821 | 2025-09-11 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 271.8 |
| b34847f9-35c1-34a2-a146-e5e58bbc0aba | -9.0361 | -45.7603 | 2025-09-11 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f3fb9adc-af23-33c8-ab0b-e5b030923ae5 | -22.6809 | -53.1309 | 2025-09-11 13:20:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 163.6 |
| 460d38ce-cb1d-37a5-886d-4fb00405c33b | -22.6601 | -53.135 | 2025-09-11 13:20:00 | GOES-19 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 152.5 |
| 0644bbee-07f7-3409-8358-2158634d88d5 | -10.203 | -46.213 | 2025-09-11 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 03cfe202-34c1-3472-b4d3-b8a0aa07789a | -11.7316 | -50.6587 | 2025-09-11 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 8f1fdf9b-cd91-3268-818c-cfc834a4a292 | -9.0756 | -47.0558 | 2025-09-11 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 093b9d57-6b90-3b3a-b95b-3d901c21f3dc | -8.9365 | -46.1545 | 2025-09-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 208.3 |
| f13294fa-8330-3eae-9938-b64c6072df99 | -4.553 | -43.7439 | 2025-09-11 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a9011bda-ee44-30c0-9693-b73a75495d50 | -14.5125 | -53.9367 | 2025-09-11 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 83722a33-6ac1-3e22-8fbd-e3b375a194c7 | -8.8755 | -49.5613 | 2025-09-11 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| eaffb7cf-b7b4-3fd4-b24f-cb44ea1ec816 | -9.0358 | -45.783 | 2025-09-11 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 41edce1e-fa57-3594-86d9-c7ba370b66a1 | -6.3226 | -53.4553 | 2025-09-11 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 467bf33c-3fe5-3258-81b1-e0f2675de0fb | -7.5592 | -48.2505 | 2025-09-11 13:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1c386658-0c67-3b4a-a54e-d378fc2e2edd | -11.0997 | -48.4392 | 2025-09-11 13:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c93f6b35-577c-3b44-b765-9c516c08ecb7 | -9.075 | -47.1002 | 2025-09-11 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 1847e3b7-6f52-3361-8e23-9fd60deba81a | -9.4801 | -46.4545 | 2025-09-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 774ab26b-a0dc-3cae-8f0a-f015f91a325a | -16.2934 | -50.068 | 2025-09-11 13:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| d6e3c607-c846-32ee-8615-2cbe5b696b51 | -9.0547 | -45.7809 | 2025-09-11 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d8a880a2-1143-3059-b74d-80f7f41b9753 | -8.5667 | -45.5842 | 2025-09-11 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b49c11b5-a0f9-3206-9c1a-753dca1d9ce8 | -11.7112 | -48.2757 | 2025-09-11 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 31a162e1-ea6c-34f7-903f-f0b21b568448 | -10.1844 | -46.1927 | 2025-09-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c8d643a3-9bca-3ee6-a888-b1fd8d52c86c | -10.8898 | -47.2494 | 2025-09-11 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0d0a48b8-51cf-35ba-a123-9798e1da803b | -6.8525 | -47.8707 | 2025-09-11 13:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 00b51564-947f-39a3-b74a-2bcab94fb44b | -11.1 | -48.4172 | 2025-09-11 13:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 82c3c499-ab98-318d-8158-61672915c856 | -9.7445 | -47.8468 | 2025-09-11 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 222.6 |
| ee322243-b624-3fcd-9a12-216ec2850e5e | -11.7786 | -46.5047 | 2025-09-11 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 352.6 |
| fe7313ec-5faa-3bfa-b027-cad01891cabf | -9.9762 | -50.3121 | 2025-09-11 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a4212ec0-7490-3f4d-a534-50a64fccfe6c | -5.6314 | -51.6444 | 2025-09-11 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4ebeab60-6378-32b0-858a-1db1e33bb0bd | -9.0753 | -47.078 | 2025-09-11 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 2c710bb6-938e-3c1b-8f6b-75cf45e53e8b | -16.6138 | -49.7717 | 2025-09-11 13:20:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 214b8c5f-4793-3c62-bd11-fab05eb89e35 | -6.2226 | -43.3459 | 2025-09-11 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d005f3cd-1698-3f78-8f9c-e1cd946dcaae | -11.7399 | -46.5326 | 2025-09-11 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| b73a2be5-a5b9-3d13-9ad0-faed34c20561 | -10.5674 | -47.2219 | 2025-09-11 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 752347fd-d74b-3608-9544-0d4c3ce8d11e | -15.8006 | -52.2687 | 2025-09-11 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |


[Clique aqui para ver as próximas entradas](README141.md)
