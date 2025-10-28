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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77cabc75-10b3-318a-84c0-873af8756d93 | -13.631 | -47.03317 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7a73aee1-aaa3-3089-a5ba-49d30b0ef9db | -10.67883 | -47.26524 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0066f92-0811-31a5-b200-220f363dc906 | -9.91236 | -47.68256 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28837db8-9560-3c9a-b938-c42a7f9dd023 | -10.64909 | -47.90646 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 007ecc2a-9d0f-32f5-abe6-52a432e0797c | -9.51837 | -46.11032 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69a6f22c-dbff-397c-abb2-5fc8b9afc788 | -8.32091 | -46.83173 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24631a4b-dae3-3c6a-a3f1-66b6c944bb17 | -9.45463 | -46.86557 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec49eab3-6231-320e-bf3b-89ee4c944a2d | -10.86225 | -50.1327 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 43e41755-7a90-37b4-9036-aea10096ab25 | -13.73954 | -48.40762 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a47a7ee-f27e-350e-afb7-c11c32879efb | -10.60337 | -46.61739 | 2025-10-28 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f4e1d44-de24-3964-8463-25f376aabf72 | -10.32694 | -47.22984 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 972c0138-01aa-395d-bc8e-730f96b573a5 | -10.02406 | -47.16679 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1245ce6d-d44e-3043-aa2b-4b9ee18578bc | -13.55076 | -44.26834 | 2025-10-28 04:44:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38368aea-c1a1-3ecd-8c5f-9e00585c180e | -8.3173 | -46.83112 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4734135-670c-388b-a582-070754536f4e | -13.18814 | -48.44077 | 2025-10-28 04:44:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c997c41b-1e74-3927-bacc-8e579289b46a | -9.2392 | -45.60732 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82ef33b8-2754-3447-89ca-c33bff03ec5d | -14.72671 | -47.36228 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7cde91f-89b0-3c9a-8944-f82485aab752 | -11.91176 | -43.82681 | 2025-10-28 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70352016-cf4a-3c03-ab98-c7b664ee0983 | -10.55847 | -49.78789 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e00b07ec-d6e1-389e-b97f-fcb9fac7a33f | -10.07613 | -50.52803 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c77beed8-ecb2-39e8-b5e3-3af294959f95 | -9.21914 | -46.36946 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3471f8bf-7c7e-3832-971f-6b47e43191ef | -12.55355 | -44.93736 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f648004a-0544-3fea-9b03-460df907ddee | -10.94995 | -50.24786 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| beb0b614-e45b-3b5f-8b94-454db6bd1b45 | -10.68562 | -44.3573 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4029e3f7-6a7b-3db4-900c-f41abf21a0ad | -9.57992 | -46.94783 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee1e7186-6ed8-3cfd-8d67-81dc0deee657 | -13.24278 | -47.06334 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 642a4952-5146-3b08-afcc-b88ebc4ec576 | -10.85759 | -47.90807 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7996f1af-7b7c-338e-8c71-fd084c7fad03 | -7.70985 | -55.50146 | 2025-10-28 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c2d3c05-97b7-3cdb-8cb3-3045e6b7cd06 | -12.70266 | -46.32652 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f2a8f87-f3b2-304d-8ccf-5e83124b60a6 | -9.95273 | -47.09318 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc04be53-93f0-382b-929c-d450c3efe870 | -12.19003 | -43.58774 | 2025-10-28 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9b9040a-0be1-3939-9385-94c3bc88e7c2 | -9.36882 | -49.2668 | 2025-10-28 04:44:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa4c4449-82cb-3719-89f1-d48cfc6b22f6 | -10.52363 | -47.7326 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f8a3873-a0e0-35b8-bc2b-8434c2a560d3 | -14.53357 | -47.97995 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 675e4136-5ea1-3b0c-be5b-f149da60b57f | -9.01417 | -43.97212 | 2025-10-28 04:44:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ae54bb5-affc-3170-a572-78484f498dc9 | -14.73118 | -47.35811 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09903f95-ffd6-3cea-ae4f-e1aa886da6f3 | -10.58038 | -48.00479 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7ccce45-3025-321d-891a-35b0079765c1 | -9.16794 | -44.58575 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd192e2d-1c43-3d3a-b32d-27568e5b9f52 | -9.2211 | -46.35615 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69b6932f-2abd-36d8-954a-6b65bb8882f8 | -11.03442 | -47.85483 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8981d11c-3892-3273-89d4-2b610206e1d9 | -8.66866 | -47.11964 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43a9959f-d6c8-39a0-8a05-2b2969c1932f | -9.2209 | -50.20768 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b84b8ff3-2606-3ab5-be24-69b802366aab | -10.65962 | -45.25207 | 2025-10-28 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| db6a4e5c-4e5c-30de-8ae7-09d6698832cc | -14.76357 | -44.96016 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f2781e6-6663-3e34-99d8-fdd2fec10400 | -13.23388 | -47.07149 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc95aa43-6de8-3228-a10c-c2eb28b4cf34 | -14.54387 | -47.9806 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7abe5139-896a-31f1-a9ca-0893416a29bb | -15.20008 | -47.21006 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eeeff56-d770-3fa1-9926-e9ef0eb7e9da | -11.50669 | -44.00166 | 2025-10-28 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fde1e2a-26c1-365e-b83a-5bf1fde922e2 | -11.02676 | -47.83311 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a18419be-992a-3f3b-a9c0-ebb51c698292 | -10.91169 | -50.25253 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50943cef-1887-3288-8746-c3587658da70 | -10.57738 | -49.79815 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a7f0fca-0e51-3928-8fa3-a25a1de1f3c0 | -10.03253 | -47.15948 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992bee48-79b4-3919-9abb-89c6f662d5ac | -13.9154 | -48.48722 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25866ba5-a327-3980-b5af-cdaf4cd162bd | -11.1062 | -44.01638 | 2025-10-28 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d95ac136-ef59-3d47-aeed-97fe14a9245c | -11.8477 | -43.92593 | 2025-10-28 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4850778f-cc1b-38cb-933a-a4d563922102 | -10.96755 | -47.82134 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2888287f-2f55-3321-947d-8036499aef5b | -10.9271 | -50.0673 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3053f59f-856d-3ba0-9061-ee7d2cc9acc4 | -7.93128 | -55.02064 | 2025-10-28 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58df1d0d-b11c-3c1d-8164-9ab5ac817c25 | -8.66782 | -43.92465 | 2025-10-28 04:44:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed60d5f8-088a-3802-84ed-088290347b1d | -9.54097 | -46.95939 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a55ff339-31b3-3103-9649-56c32a1227bf | -10.96162 | -48.05193 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74b65d52-b8d0-3b0d-8836-d82d34cfcf46 | -10.64315 | -48.01757 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eae12b09-cf88-3148-8ece-f2716563a136 | -12.18739 | -47.01932 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8fa2041-2539-339d-a1fb-184f81b5a6ef | -9.14502 | -51.29841 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ec8676d-2321-325d-bd91-db9fb5534473 | -14.76685 | -44.96963 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c4a1d89-9eb1-364f-a391-fd113e0b0635 | -14.44422 | -49.4405 | 2025-10-28 04:44:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96aa3260-9c9f-361c-813e-ebc04626e028 | -10.98384 | -50.35032 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f93607d2-a5ff-3e72-8218-90982c3d888d | -9.9754 | -47.16543 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e05caa6a-4d84-37fd-a75a-2b2d811bc249 | -8.68862 | -47.05986 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1296fb8c-35d3-3558-82ec-906aceda6832 | -12.38216 | -45.81995 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 252bc3cb-344f-34dc-8bf4-2597abdcb7f9 | -10.97172 | -47.81774 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73031a0c-3ce6-3668-88db-980148af6a46 | -10.55902 | -49.78436 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fde713a6-1297-30e9-91cd-c63bede2ee48 | -12.61913 | -45.08167 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97b158df-95d2-36fd-a649-d11e1910018f | -14.55851 | -47.98277 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46c75124-382e-3bf1-988c-24e896f8942c | -8.64124 | -45.28023 | 2025-10-28 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 374dd262-bd78-3abd-9184-707e07f9cd3c | -8.43849 | -48.69858 | 2025-10-28 04:44:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f0c4141-cdff-31ba-acb7-0b9a29fbe804 | -13.8916 | -48.50099 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a264a84a-e562-30ba-9670-c48bcfaeb95f | -10.58517 | -49.79214 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 3cc572a2-bc12-38c8-a1d4-44930592221b | -13.62649 | -46.46793 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e46ae24-286a-3902-935e-1e706d399acc | -11.03096 | -47.80471 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71338e54-1fdd-3299-8270-2c68abf72106 | -13.39713 | -47.35431 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd62050b-41ad-3280-9381-a92e06360c2f | -12.47469 | -44.49433 | 2025-10-28 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6942599-7bae-37e5-880d-17c3567d8583 | -10.77165 | -44.75777 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79183ba3-9d1c-3576-b595-ab6d845ac1f1 | -12.2172 | -46.49007 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 531bd689-cd06-39c6-b8dd-2910e5709d32 | -9.06337 | -46.94387 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7da1446-239d-35f7-85d5-6482ce51a51a | -14.05883 | -44.4039 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00e85eb2-d8dc-3f8c-ba98-fa288d26d4c5 | -9.14781 | -51.30255 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19a1e281-5b2a-3263-b95c-8751f5eaf17b | -9.55854 | -46.96638 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8172abd-06b7-303c-86b0-ef1c13bc8482 | -16.05013 | -43.53757 | 2025-10-28 04:44:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a74d8c72-20a8-3c8c-8206-688dd9fd736c | -10.95164 | -50.25135 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89e1a6ff-477a-3004-aae9-ea102809f5ac | -13.72499 | -51.45622 | 2025-10-28 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 206d2d9f-668f-3625-a441-49b23f3e949b | -10.7705 | -44.7659 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fc06eef-64cb-3e7a-920c-d0339dc6cbf4 | -10.56682 | -49.8001 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88de9f9a-d7c2-32b8-ba2b-bfab5e3a243a | -10.94833 | -50.27247 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f108b78-ded6-34f2-b2b4-c601b7ab18da | -13.39296 | -48.51514 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfc924c1-f169-3c0a-a464-45d6eae762d1 | -9.36268 | -49.2622 | 2025-10-28 04:44:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7ec5b46-c49d-33dc-8afa-a396dc931789 | -12.25824 | -47.92377 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 213d67ef-8a8e-376f-9edb-d446a4b87ee8 | -11.47361 | -48.71426 | 2025-10-28 04:44:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1e3b614-f45d-3901-87f1-2c0ce3b438c3 | -14.08487 | -44.15833 | 2025-10-28 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44a504ad-70a0-3d9d-8353-abded15cc45d | -14.53229 | -47.98871 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README68.md)
