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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0754b844-4cef-3bdd-8543-996902565a1b | -12.99716 | -56.91288 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4d11d55-d744-3f28-be1e-022b64205983 | -9.12247 | -65.79203 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c932fac-9fa1-3859-83a1-67b57d6b1889 | -11.87528 | -46.4056 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f36158ca-351c-34b7-bcd8-11f3cc71aea9 | -11.08287 | -44.75482 | 2025-08-29 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a08ca38-6cf5-3138-8518-c93e2cf5ac9a | -13.0077 | -56.91096 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29278bc3-f1fc-3045-904f-df9d083724b4 | -8.95689 | -65.9528 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1ee05cc-7218-37c0-ba6d-c258bd53a183 | -9.88618 | -64.69926 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b914cf08-9686-32f5-b4dc-c5b84e878a00 | -12.32076 | -47.0462 | 2025-08-29 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e48c7321-28bb-3e06-87a6-d39683dfaf22 | -10.62153 | -54.90708 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d47a8f48-5916-361e-ad0f-a6e1b56bcd9e | -10.45115 | -57.96549 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e296cd2-3428-36a3-8a71-230b6ef9db15 | -8.95447 | -65.96378 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 325655af-e62e-32ee-b6e8-44c55c0e7b77 | -9.54316 | -65.69817 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8f77cf6-82e3-3ad3-8b92-6c04cfeba18a | -9.17318 | -65.79092 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bba056a1-5fff-31c3-ade3-d693c956b02e | -12.99273 | -56.89759 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16cfef9c-7b0e-3f53-a8bc-21ec62d931a4 | -11.06764 | -44.77359 | 2025-08-29 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 480d5828-06b4-3ce2-85af-adf5fb6b09e9 | -10.98127 | -46.90131 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 05e6d448-4937-30ea-9a07-6e351e711961 | -11.03235 | -45.07157 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3083a14-98c5-3a60-b3c7-ba46a1416c1e | -8.24947 | -61.50079 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 701e4c7d-63e9-3232-8e12-92d4086176d0 | -12.99606 | -56.89814 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1de4c20b-2814-3758-9044-9784ab24f445 | -9.11566 | -65.7956 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a574814a-b93c-360d-80d3-46f54805f998 | -11.55997 | -46.34907 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8755dc81-809b-3887-81a4-5b32ea11151a | -14.58299 | -54.52352 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec362e72-1de5-3fbc-b85d-8f48c97525a0 | -8.30865 | -61.41519 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 523c9146-c24a-35d4-a707-83ef52e0263d | -13.40404 | -46.9889 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 963b95d4-253a-31e8-abf2-5af88f04eaad | -14.77732 | -59.73487 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c3fe948-78db-3ae1-9f36-f02594b22db6 | -14.33296 | -53.29156 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a36e1711-6146-3db1-b709-de1f0f636415 | -10.47456 | -57.93157 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4279d066-f2c4-3219-9a99-d8e2df895ff0 | -9.77705 | -64.2526 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f0eba817-e66f-3440-a603-f685c151ea61 | -10.97945 | -46.91624 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d4d4e932-41a0-312e-b84f-d95a9c4436ec | -9.66916 | -65.03188 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 77d2bb75-d2ab-3210-bab7-d04f8dbba3de | -9.16537 | -59.57671 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e867ec1-f916-3da1-9f6d-c9558839df6d | -13.19087 | -45.29276 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b4dcd644-0bef-3141-9325-e93545016404 | -12.09123 | -44.72686 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 06fc6232-35fc-3510-84ba-b768728bd160 | -9.16712 | -65.79334 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dcbba87-ebd2-3a37-b0fd-55e43d0c50b8 | -13.00437 | -56.91042 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b36613ce-11b1-3f61-979f-e05a00d0ddaa | -11.55198 | -46.36569 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90a2407f-e89e-3975-a6e5-6fd42da55b7f | -8.17314 | -61.37673 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2849f109-b625-3b2f-874c-4460ec049bc3 | -9.15741 | -60.9293 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97d0bfee-4133-3750-ab83-7f490f728f07 | -8.18135 | -61.37814 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d9fe923-b48a-3465-bb9b-3c03fc5861b6 | -14.34677 | -53.33292 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 889f4846-9e95-31bf-a330-3463bc4b27a6 | -13.02256 | -56.91665 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d73befc6-4dc5-35d4-b8b2-872271c03e99 | -8.25352 | -61.45129 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24411968-3f74-334e-877a-5bdaf196fb5b | -11.88162 | -46.40212 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f19e8b6b-1f1f-3006-b6ae-8edfc8a0626f | -8.17442 | -61.36938 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1dcd3f8c-ae19-3348-aaa7-55e0c6414c4f | -9.12377 | -65.78508 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a6bd77e-ad94-361c-92eb-84a2f3b13a3d | -12.0919 | -44.72927 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 22b47b55-b2d2-3872-a5b5-58f1c94ff14e | -13.40358 | -46.99271 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b6f3bb6-d290-315d-8356-3a3a135f43ce | -9.11368 | -65.74452 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdae95ac-a224-3c77-bf50-d10433e2c460 | -13.0177 | -56.89075 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a477a29-2298-3f00-92ac-9688191cceb1 | -10.44894 | -57.95765 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9348f6eb-a938-3dee-9d7f-3181d23c5989 | -13.40961 | -46.84829 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 726b7bff-c42f-31a4-8f5f-ae908e57c635 | -10.3648 | -57.80653 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8e55828-9dc0-30a7-b8d8-49eb6a038eb0 | -11.45692 | -47.3068 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac380f9e-bb35-3a26-9794-fb7a16b74f64 | -9.13123 | -65.28665 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd614b46-8b68-3004-b126-f0a014958622 | -10.37939 | -57.83106 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9feac17a-d937-3e0c-a630-7807053815f9 | -14.604 | -54.50527 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 746a05cf-cf7a-3a13-a4c5-57ed7f1eca14 | -10.97427 | -46.92872 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e60c0013-d608-3d07-b285-6f52b513d7cb | -14.51616 | -52.99877 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0e95d26-039f-3796-ba92-cb5542c78524 | -9.11881 | -65.7781 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| adae2abe-8b84-3432-940c-fadcbb9fecd7 | -9.23592 | -59.7812 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0df6088-2011-3d7a-83bd-270d7e711114 | -9.11022 | -65.79462 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0189bdb-581a-3d08-a706-8a78a845a6e5 | -15.81788 | -48.16232 | 2025-08-29 05:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30867349-44a3-313d-8b20-4b94f8519b4c | -12.62231 | -57.01502 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5e67db2-b5cf-313b-b8ef-b5aaa31ba091 | -13.66066 | -46.91363 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 180c4b2f-1792-3e08-96fb-c536409c9108 | -15.12607 | -48.11589 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99c7e718-16eb-3736-a7f4-592b2120ada6 | -13.01324 | -56.91914 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2a9b682-7ec3-34f9-9723-e06fefc3cc6d | -9.11294 | -65.78297 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f070c007-8d73-3b7c-a327-92330204f528 | -13.49235 | -46.84423 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 569ef958-3124-3723-b382-e10e8716dcf3 | -12.43077 | -63.91634 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0ebcce47-bee2-3c08-b5e6-238878939953 | -10.93595 | -63.63064 | 2025-08-29 05:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6aa3afc2-0282-3679-a079-0d28f7ee2319 | -13.54631 | -46.88228 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21c5491a-76d9-3414-b689-40b714af362e | -11.57438 | -46.37602 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98cd1211-54d5-3a60-beb4-3bbcd5ff79bc | -12.43979 | -63.91813 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97eb2bba-3ed4-36b0-b372-dce32218a630 | -8.18263 | -61.37078 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74e6c4f7-0a8d-3ca9-a026-5aa2597c441b | -13.00492 | -56.90687 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a754dce-a4c4-36e7-b74f-1fbeb1754c40 | -11.55348 | -46.35362 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee76527-b3d5-3dbf-9f9a-7d10f3510a55 | -12.42625 | -63.91545 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b89fc1b0-f0dc-3136-9503-48f3769185ae | -13.0331 | -56.91471 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ffbe7ca-625f-31b9-98ae-196d2212b511 | -13.01268 | -56.92269 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30aaf9cd-ad22-382f-aa94-f0f6c28f058b | -11.06123 | -44.77285 | 2025-08-29 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cbfa4aea-a69f-3e82-b5c4-0d7b71cad9ed | -13.41871 | -46.97481 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 1598eb52-cb58-38a4-992e-b8f45b266bb0 | -10.97385 | -46.91568 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bec69eb-91ef-339e-a9c2-ccd7dbcd0d59 | -13.41759 | -46.98458 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ed2a1286-b20e-3412-8d0d-2ade9f390e6b | -10.85238 | -60.81442 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a0341aa-785d-319f-b84f-f337d0083788 | -13.41066 | -46.98231 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2ab79be-5d35-3c9a-8709-82632acfe2a2 | -11.88308 | -46.40233 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab42c491-68ba-3e8d-a49e-ad7616cb18d3 | -10.36701 | -57.8143 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63a9a602-e686-351c-897c-1e0a0b4b19c7 | -9.11638 | -65.79454 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e1d7cf3-62b6-3db9-ba79-1a2f01c41a3f | -11.87672 | -46.4058 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| fbda0955-ed02-304c-95b4-e2b6bb9d419f | -12.90641 | -48.14041 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce83c77f-442b-3d68-bd95-215c0f5eba6f | -13.41938 | -46.96898 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7353fabd-5e5f-32ad-acf7-540c3dda9b98 | -14.79441 | -59.71762 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7ee860a-2b3b-3296-8ce1-b3166f37a8b6 | -13.50855 | -46.85639 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ae3db90-f5b1-3ba3-9c0f-88c12638a348 | -7.54097 | -63.84007 | 2025-08-29 05:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f9b5377-a1f3-36c6-91e6-19a07fc7fbf4 | -11.32075 | -55.21495 | 2025-08-29 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17dfcf94-ff98-3d76-9240-f9e999962173 | -13.19201 | -45.28231 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 17b0039a-7a56-3490-93d3-8ac1c0a86cf4 | -8.93491 | -64.16634 | 2025-08-29 05:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64e1e3da-5ce6-3eb3-b7d8-8b2dde23f5bb | -10.9872 | -46.85268 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6193e419-20a6-363f-98d0-0a4f184d0d92 | -12.69203 | -48.19904 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 13afb7cb-2240-30ba-bd91-d7ee41e7c953 | -9.45042 | -51.95003 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README73.md)
