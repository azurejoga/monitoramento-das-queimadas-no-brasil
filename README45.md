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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7945833a-ab4a-33d2-af6a-e8dc0b6b33a8 | -10.24064 | -44.06107 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92eb505b-502a-3bd1-9e52-49a449239096 | -5.34578 | -45.75047 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 447180a2-82b4-3874-ace6-8e3d029ce2fc | -10.18368 | -48.0923 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d4fb9de-1f14-3282-ba36-7899c6bb2cab | -6.58856 | -44.1649 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e0c1d22-2da0-3d88-9eaa-1bf6ced795f5 | -6.89894 | -45.44779 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fade409-1b49-33ae-b9d3-32a818a2b253 | -5.58204 | -44.18132 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86dc239f-a082-357c-8efa-ff30204e5361 | -9.81531 | -47.75279 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9018cb45-4290-35f4-a75e-b872884d174c | -5.15532 | -46.27004 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b67af31-8366-388a-b2a5-09bec6342166 | -8.94696 | -46.57509 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46292014-1255-3c18-82e6-42506f70fb04 | -7.71273 | -47.85864 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdb4e4b4-c46f-33b7-a0e8-d01ca1143611 | -8.17073 | -43.30176 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0535799d-0f5c-3ca3-aae8-213f0e6fd36c | -7.12243 | -44.73067 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4f48823-9da5-3372-b286-0b4b9c3ef441 | -9.67564 | -47.90397 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b40f1d4-6e6e-39c8-b515-a9ce85f5b811 | -10.62172 | -42.30442 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9c4a5e54-aa9a-3295-b6f1-21c8d200a1ab | -5.03647 | -45.13723 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f655f51-f7b6-37b3-b673-e730465391d3 | -5.57615 | -44.18033 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c338b507-25c9-307d-b1e2-009c8a348b7c | -7.6875 | -42.56454 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 35dc64fa-f753-3759-923c-2027ea284020 | -6.3174 | -44.31739 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab537d26-375b-317e-904e-cd1913d3874b | -7.14553 | -46.41493 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99496682-b97e-3caa-bf5f-ca50ffc6e1ae | -6.8872 | -45.45687 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be4c3d38-4c8f-3b64-bec5-c36c94f253f8 | -5.67119 | -51.89743 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 632bd45e-09c3-3a38-a27b-d0d8a4a4aaa0 | -6.52362 | -41.48726 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 36cec0dc-e74b-3ee3-a832-7bd021e36472 | -3.80139 | -51.64392 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c80e7ed-1696-357e-99f4-4835b5a3639c | -4.84794 | -46.72113 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a85e9b50-31a0-30bb-837a-a9faac1f1ce0 | -6.27341 | -44.38378 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9106d63e-6af3-371c-ad14-4104090cc3f7 | -7.39592 | -46.97178 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af8fceda-5703-3b4c-8325-fa829b95078b | -10.8446 | -43.9506 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b353c9c-2ed3-34c0-a2d3-0dc62bfdf9ed | -5.83293 | -40.81739 | 2025-10-18 04:29:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 210042a5-180c-3ad2-8715-70f5a792910e | -7.01491 | -41.82515 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4e92f7a7-3f38-3bee-8c6e-7e8cb25e5b5a | -10.13277 | -44.53444 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| daa1b925-cba7-33d0-af9b-28e9da23a71c | -6.31597 | -44.3141 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7abbe75f-04db-394d-a4f3-2fb958504a64 | -8.38784 | -46.23945 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98fb377b-d051-3e25-a1c3-192690ef3498 | -6.5843 | -47.072 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 087d56da-c2b5-356d-9abe-c07006664b4d | -10.12863 | -44.53789 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 490af5d6-8a62-3283-bcd9-ed11438723ff | -8.16968 | -47.03807 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88fd7b2b-8628-3fb1-b24c-368aa1ac7c73 | -6.06004 | -44.52288 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9530c19-590e-3b4b-889d-9f2ad3aef8be | -8.88148 | -47.96984 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b71da64-ad9c-3d65-a7f1-c58dca9807bd | -10.229 | -49.6847 | 2025-10-18 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b107a27e-ce57-3cbf-a53a-245440beb668 | -8.08915 | -45.44872 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1e0f95b-b245-3392-9f4e-7cc258a334c9 | -7.57921 | -44.98099 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 309e9ff8-09d4-3352-add9-f349216dfed8 | -6.23582 | -44.15613 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9704a28-a1c1-33d8-8ebc-dc7f0ae1d891 | -10.64721 | -45.32442 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32866de1-fd1c-383a-820c-e5cf407c13b7 | -5.24027 | -49.85419 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e297d98d-8606-3853-adcc-eae51ec81efd | -7.21054 | -44.99916 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ede30b36-a254-37c5-a5c7-20027f698206 | -9.19721 | -46.87286 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 340aa318-047b-3f59-ab21-2075cdf66db3 | -4.29261 | -48.26505 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b1d0250f-93a6-31ef-818e-c8142578e691 | -8.83057 | -49.66591 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a71c09f3-819c-370b-95bc-ef08739a628f | -7.36007 | -44.23031 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 005b360f-4267-3016-af69-7bc6abdf74ba | -9.21606 | -46.88304 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b43b4a55-492d-3ae6-b3cc-0be13587818f | -10.09125 | -47.65984 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a0488dc-255a-3f4f-b9fd-48b936fd98af | -10.49773 | -43.42566 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7c5f539-3cb2-334b-aaa2-492a86264cbe | -6.30065 | -44.72344 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afc28353-ea79-3718-9568-90a5c350f238 | -5.20455 | -45.7492 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b7177fc-8aed-374f-a001-9eaea27e05cb | -6.24224 | -44.96635 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc47311d-87bd-36b6-bc19-f96c1b1fbd21 | -10.83743 | -44.39808 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 553e0143-75c9-326d-b771-96ce00b51d90 | -8.22481 | -43.30799 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3d9c8e6-5863-34ef-9a74-f25243d95019 | -10.1121 | -44.55166 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 452969ea-60cf-3c91-b20b-9633290ca781 | -10.7002 | -44.56633 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23e2d9ea-40f6-3dc5-96fc-8cee83a5373b | -10.8047 | -44.01912 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0766907-042e-3456-ac7b-1cab58284728 | -7.01473 | -55.26686 | 2025-10-18 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40e8baa4-ead1-3334-9fd4-01ce1165c5e2 | -6.48738 | -44.55649 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 099c9467-042d-3a6a-8e27-744bc4f56bdf | -6.31538 | -44.31788 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0679f8e-1862-33e6-b32e-83e19d7371c0 | -7.82648 | -44.1231 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b9c1c99-6bd1-30cc-808a-33068b04a596 | -9.24634 | -44.34973 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d02ca44f-65f2-3977-b0ac-9adb03852786 | -5.21736 | -45.51628 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54ef8c23-cddd-3f4e-a2bf-676874364d18 | -6.40475 | -41.47758 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d61fe884-1a2b-3aa3-8a2a-0df0ee53ecdd | -10.85068 | -43.9603 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82f2306e-39e7-35ad-9ad1-514cca90ab93 | -6.20579 | -44.43479 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89dab921-4eb0-37ae-9e08-d5472663d910 | -6.88717 | -45.43513 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb41ae61-f00f-343d-8079-1c81dbed932f | -7.58545 | -44.98571 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 587c7bc0-9321-3bf9-912b-58460f51d73a | -5.92864 | -46.53851 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f080b035-606a-34d9-b5d3-e35981e462bd | -7.67203 | -44.63079 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba4bbc88-5d70-325b-9fd6-29188b2c68c2 | -7.58772 | -44.99358 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b29ff436-7080-32d8-8bd5-c654e124eee6 | -5.11217 | -46.07535 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5de1b92f-51d1-3090-b479-5f7a4dee7610 | -5.25466 | -47.24061 | 2025-10-18 04:29:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f3df82e-9de7-326e-be24-63f75296c258 | -9.04046 | -46.97002 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 909c0af0-be44-3b1c-978f-252562665d5b | -8.09563 | -45.43457 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28dd918e-a210-318c-b964-92226c951b5a | -6.27635 | -44.31926 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 216df58b-328d-3055-9e18-d5ba03171720 | -10.24083 | -44.03521 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e761ab1-ada2-3166-9872-d91dee07105f | -6.38372 | -44.63853 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fc83593-8d52-310e-b797-8a4cc713d31b | -9.61217 | -49.67883 | 2025-10-18 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 168528fc-cca7-33b8-ac49-4668a0e4ecac | -5.60089 | -47.49789 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83f73045-725e-3e3a-bd9d-dbd694f253fc | -10.50438 | -43.45896 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5b341783-fc92-3b8a-8dd8-2be3ee214faa | -7.86669 | -55.37662 | 2025-10-18 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f1c66e9-8d66-38ed-aadb-81a240eb0cc2 | -6.46705 | -44.1386 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1768db20-c4e0-3831-8662-c17002673b75 | -9.7837 | -42.03212 | 2025-10-18 04:29:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 99fa9d16-186f-3552-998b-5a12ef2abccb | -10.63077 | -42.29852 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b4d7195-4c97-38f2-bd89-13d04a41fcca | -10.62535 | -45.23531 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3264588a-28b4-3747-8c5d-7139792d4b61 | -7.12084 | -44.80978 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65930d7e-36d6-388b-9ad5-e8ab45e6d953 | -10.4907 | -43.44761 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 72d59197-29e1-3c24-97c5-6332c491f78b | -5.37736 | -46.004 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a6c7500-50a7-3bb7-b556-0a48e54444f4 | -8.15358 | -46.79975 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8aaedb0a-4659-32ee-ada8-26bbc9a688b7 | -10.24901 | -44.03031 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5b8d9e0-7c16-3ce3-975a-96669bef5dfd | -9.52702 | -47.86563 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee4f0302-ae34-3f84-933f-139751f4ec6f | -6.67694 | -44.59249 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34589599-11cf-3259-94af-fa73c5cd7eb0 | -10.8104 | -43.92797 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc4f13dc-a138-335a-861e-5049414e3dad | -5.93638 | -43.92823 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d0f923f-bddc-333a-8fb7-4533e3fd108b | -10.13569 | -44.53904 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b56dafad-18ae-3025-b5c8-ac5dae8a78cd | -7.14388 | -46.42536 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e8d457a-b8aa-38fc-9000-682efd70b1c3 | -6.11657 | -44.85178 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README46.md)
