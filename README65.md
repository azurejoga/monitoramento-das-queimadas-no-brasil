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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4183a161-a6f2-3e0d-9d72-dad55080c1dd | -11.84429 | -51.52607 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 991abf04-cf72-3a51-95d7-9d4831a2d6b8 | -11.13896 | -46.34335 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 89c9c93e-a1f7-3f90-8838-49e56f776510 | -11.93077 | -50.61315 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd85985d-8d54-322e-bd50-4099f410a411 | -14.72564 | -46.74776 | 2025-09-02 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fe4e1c2-55c7-3c2f-b1ae-f809c5b1245a | -8.9933 | -56.33775 | 2025-09-02 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 122fc30d-80ed-3c31-8836-6e029b974f58 | -11.89681 | -46.67407 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01abbaf4-79ca-39b6-bce1-3427cb8cc9c6 | -10.47331 | -51.62549 | 2025-09-02 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f38c9ed8-3c05-3c73-a150-88b880876299 | -10.83443 | -47.45214 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce46ee2b-92c3-3568-aeec-643484916143 | -12.2114 | -50.1304 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7af8cb32-b601-338b-a1cf-61210796ee3c | -11.05791 | -45.39535 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 463f2e80-807f-3966-a694-f4088ab1ebe7 | -9.50414 | -57.80149 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1a0819c-9201-36c1-b005-54551f698ea2 | -11.66434 | -52.17475 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3a208cd-8cda-3eef-acee-8ad33a38e0bf | -10.05329 | -48.10054 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5525bcd0-2fa3-3a52-8224-657eeeda5ed7 | -10.06037 | -48.12659 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78da6514-2a60-33d8-aaf0-8daf06f687a5 | -11.66834 | -52.17532 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7b63ada3-2432-3a89-b083-09f8a8f8ce04 | -14.59621 | -48.03674 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a76c0ce6-35b4-3afc-b88c-9afce4b41794 | -9.27888 | -48.56281 | 2025-09-02 05:06:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bca38c10-14ea-372f-aeee-8b9249138549 | -13.89252 | -48.11325 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 079f15f5-9a9f-369d-a1c1-5bdfedbb1d09 | -9.83654 | -48.31657 | 2025-09-02 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86cbbdbd-7342-3a05-a1a0-139b65747dcf | -11.10171 | -44.65079 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| b184a82c-7fd1-3f03-86a0-1a45b045f8a0 | -9.32708 | -56.26963 | 2025-09-02 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8045f6d8-03c9-3b0e-be4b-6c84d0770ca9 | -8.97258 | -65.96933 | 2025-09-02 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 511d489c-2800-3d1f-8d7c-c03c2339ad50 | -8.67203 | -62.40221 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c159ae4e-d5f4-34ba-9e54-18aed48647df | -10.83271 | -47.45304 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2535c91b-e4fd-32d3-8c7a-aa311ad9e9a7 | -12.92518 | -56.96691 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b03609ee-2351-34ee-84b7-a4909dbe3ca4 | -7.48129 | -63.8283 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4ed4a12-e0f8-3f8c-a4b8-878e3a21ad43 | -12.99351 | -48.10401 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8132c37-a1aa-3921-a0a8-54d4812afdc6 | -7.54728 | -61.33589 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6946c064-9c7c-317f-9431-ba9a2e6c6fa8 | -12.95172 | -48.08965 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 15f27c85-2b99-3f6f-b885-e0c3b38d86b4 | -11.8198 | -51.54989 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47f3436e-1116-3a7f-a1df-a445b8d12130 | -11.65607 | -57.36338 | 2025-09-02 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7c5eb91b-1d69-31b9-94b5-fc9a01e76ba5 | -12.92842 | -48.1023 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c671e9c4-45fa-3c3b-a8a5-c263f5cceec1 | -8.64745 | -63.27121 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 313b4265-3b47-3481-be6a-f98e20723959 | -14.75158 | -48.15044 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d951e14f-6061-398e-a99d-48c00206fb03 | -14.81817 | -48.35499 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61ccb20-e3f9-3554-85c5-53f3dde6aa29 | -11.01627 | -46.82755 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92607eee-6977-3eb4-9a14-8f52a8073398 | -8.6933 | -62.40587 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c49373d3-54c7-3425-b43f-7a03a147158c | -12.95207 | -48.08673 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e989390-7c5a-35b7-8992-801d3fb6073b | -9.95479 | -66.87448 | 2025-09-02 05:06:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79788eff-eb5e-34d5-ace5-da779176713d | -11.67788 | -52.19456 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 570da347-fed8-3ce9-842b-242773945435 | -10.05885 | -48.09805 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b8cb45f6-4231-3d6b-93b9-064426bd3ec7 | -14.59239 | -48.06921 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35870858-22ea-34a6-94b5-c69d56912799 | -12.98099 | -48.10084 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 997b6fdd-889c-32ae-b6bc-d945c2da4e43 | -7.59318 | -61.63688 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10d2cb56-456a-35b5-9a71-528fe652447c | -12.6277 | -56.9986 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40957198-e135-36ac-8aab-4afddde3c937 | -11.68429 | -52.14874 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a66ebaea-800a-36b4-a615-cb97e5a06062 | -14.59017 | -54.56251 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df59da11-0b1d-39a7-b4b2-f375823713e7 | -11.09181 | -44.62165 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cb8141d6-68aa-3669-92cb-9a4734c3b143 | -9.64469 | -63.11727 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a76d5913-c261-3ebe-9d43-b0cd6cdb1476 | -11.66251 | -52.21718 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 919c9df2-d05a-3e26-a0cf-ed738e479b06 | -14.58716 | -54.5577 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c98daea8-bb7b-3a83-8343-16e8bc51ca38 | -14.79918 | -48.21732 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcb121c1-f91e-3f60-b8fc-472535a82286 | -8.31062 | -55.1015 | 2025-09-02 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18f46f41-9fd8-32ef-a172-a70df3bca0bf | -9.2649 | -59.75654 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89c34762-564d-3681-a987-4fabdaf96dc3 | -9.44678 | -46.77787 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf6a7a82-949a-3340-9cbf-2a2edf36080d | -10.29359 | -47.5116 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef0b1377-14d4-3e47-903b-793db8bef8d0 | -12.61487 | -48.1824 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9a272fa1-cc2e-36c7-b3db-08b0112c9700 | -12.87977 | -48.05301 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 765120da-fc92-3c20-b62b-d8267c62fa90 | -9.73555 | -48.96046 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02ed73d8-301c-31d6-977e-a894f10417a5 | -13.72653 | -46.92837 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f7cf1c3-2c86-3a26-801d-83235f0cbd1e | -12.92804 | -48.10553 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7f5ded0-10b3-3bb9-b9de-1e63e2213929 | -12.48996 | -53.8351 | 2025-09-02 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 367f20d6-bf88-30ad-af9d-99aba587342f | -13.47296 | -46.92712 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c69138ae-3d6e-341d-a110-1326a1a364e5 | -7.56292 | -63.06892 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8af97057-cdcf-3088-bcea-71df78229b26 | -11.07204 | -52.0068 | 2025-09-02 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f5d69dd-3dbd-3c1c-ab68-fabf88ee5fcc | -14.60388 | -48.07195 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba28e906-0ce3-39d9-b49f-4b67b982d8b4 | -14.59277 | -48.06599 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4936487a-1e6a-377b-bec7-0d129830ade2 | -14.59754 | -48.07276 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9a30946-c81e-331d-ba26-83e47d154ddf | -12.79229 | -48.07659 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba9a5912-f8b4-3816-a2c4-2336ff15c487 | -14.78776 | -48.18353 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c98a533-76c2-3ac3-8b4b-8c93acd5c9e7 | -14.58918 | -48.05402 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf35b02a-f914-37b9-9521-4cc376508e50 | -12.92296 | -56.95931 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2c09cc-5c73-34ee-a54d-23e027fb1404 | -11.42462 | -55.19226 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b531e29-e4eb-377d-80e9-0b037d506cff | -10.05962 | -48.09216 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 04416d3c-a028-3988-81f1-077eaa2deed4 | -7.06161 | -62.99291 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff8e3543-5328-3f8e-bfa4-7e3b486c2385 | -12.90364 | -56.95256 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5669362-91d6-366a-9c11-a4ef254beac0 | -15.12545 | -48.11226 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4f75c76-15e7-358c-9480-a3df27b27221 | -9.65477 | -47.04251 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3c53270-71b0-3fb7-884f-683b301bd73d | -12.97811 | -54.76525 | 2025-09-02 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a2bf070-9b15-3b00-9a63-f0bcf8cbf9fd | -11.65092 | -52.18338 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a88ba206-2278-3c2d-b6bf-f3541384106f | -6.92535 | -63.13079 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c3526e6-b03f-3d6a-abbc-b11b00909028 | -10.83318 | -47.44944 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30e0104b-59fd-349e-8ed9-5d3ba43c06d3 | -11.91439 | -46.6748 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24c6756a-e8a8-3af8-bb79-55ee4e9fc6b8 | -14.59255 | -54.57163 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfbbba20-4da4-3543-a200-cbeb64e57123 | -9.32654 | -56.27311 | 2025-09-02 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13451d29-8aac-3bb6-ab41-36dd2341e342 | -11.64529 | -52.04522 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e60fe731-fb6e-3d3e-91b0-5bac4740aa66 | -9.50079 | -57.80097 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66a7d845-2cef-3cb1-adcb-0dad79b7cfae | -8.69203 | -62.40882 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ba0829f-22c4-3aa9-90b8-ccdc8b6b2301 | -14.5984 | -48.07129 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2b216df-7344-301f-8b7f-f2c257d787df | -7.59791 | -61.63388 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea1e36a-e5e1-3549-b2e4-50638b6c6eaa | -9.09294 | -58.88758 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad143ce3-bcae-378d-8b14-0863eea6bb95 | -8.69262 | -62.40995 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2937c3e-6051-3dac-9924-28fa09e678a3 | -9.68617 | -56.73685 | 2025-09-02 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c310591-dfc6-3e04-95a0-ac2333e1b86a | -15.11833 | -48.18189 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15e24626-0440-384e-b713-a7dc8d1b06dd | -8.51158 | -63.9105 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65fe2430-6eed-399b-af54-38f7356b645a | -11.65043 | -52.18688 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d1ba41d9-97c7-394d-b807-e28cc9098624 | -11.66581 | -52.16415 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95e792e9-7811-3c79-afe2-47926e73f5e5 | -11.6659 | -52.19287 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f98bb758-7ee8-34e2-8d05-8e838111bcd7 | -11.86877 | -46.70721 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa33c7f7-46f1-3f91-a610-c3633be2d314 | -12.93845 | -56.99076 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README66.md)
