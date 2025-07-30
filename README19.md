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
| d3b110f6-228d-37ae-833f-b430a4f8dd6a | -8.96176 | -46.73533 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71f31875-24b6-3fe1-aa95-8479eb6d6fb4 | -9.75001 | -37.00595 | 2025-07-30 04:27:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6de0eeed-3ae0-3289-a194-6386fbb32620 | -7.77606 | -45.00367 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c5186d5e-5fa0-378b-8cb2-8f63b5462755 | -8.23578 | -44.91623 | 2025-07-30 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f24641-f62a-3679-97fa-004f25d4e04b | -6.49785 | -43.57289 | 2025-07-30 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b26d0f39-8084-3d7a-b6e3-11494385a515 | -7.85601 | -46.72975 | 2025-07-30 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3638f81-30a3-349b-969c-8b164a9fc938 | -6.55285 | -56.18958 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 865d3836-5230-3bdd-afbe-18d7a2a13b98 | -6.29498 | -53.52447 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1305694f-0dc0-3232-9aaf-d08619575900 | -6.02959 | -47.55197 | 2025-07-30 04:27:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1348f03-0b2f-30b1-b296-ccd2cfec6746 | -4.05166 | -47.31552 | 2025-07-30 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baa43d37-1b99-3b6a-802d-a50f301173b8 | -4.28759 | -48.06301 | 2025-07-30 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fa1e776-cb29-3de3-9355-2415072a6779 | -6.71409 | -44.35426 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88cbc386-bf29-36d6-8ff5-3d738e2d3d08 | -9.0526 | -45.07325 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95ecf06d-5e7e-3676-b614-33837bda8019 | -9.47458 | -46.80599 | 2025-07-30 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98365064-69f7-3552-9e5f-13077757be7e | -9.55796 | -40.32257 | 2025-07-30 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3b4d4d83-9519-3d3a-9888-c42b5e849778 | -9.84819 | -44.70404 | 2025-07-30 04:27:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 763403f3-736f-3036-b211-611cfbe0140d | -5.75946 | -43.94393 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa39ed18-f40a-335e-891c-39a5d3ef779f | -2.90917 | -48.24584 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59c335a2-02c6-3b1a-ad3d-8085a5c5ce55 | -6.03355 | -47.54892 | 2025-07-30 04:27:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37ef2c2f-5125-3fe3-9f88-6d6e464f9c30 | -9.14871 | -49.84918 | 2025-07-30 04:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 691168a4-f327-3f3f-aa92-fec7e57c9e1d | -6.02563 | -47.55505 | 2025-07-30 04:27:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0ebb29f-1074-3be3-bdef-a432c77be90c | -7.14281 | -44.35638 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a700ba9e-e262-3fcd-8254-69f6fb189990 | -6.40982 | -53.3726 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3843a5ad-5406-3140-a2e3-4ffd559c37d5 | -7.07107 | -44.95926 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e73c9177-e2f8-31bc-a91f-29c5f3a702a2 | -7.85546 | -46.73322 | 2025-07-30 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd3b28f2-af4a-3a38-87e2-d3088be465e0 | -6.45509 | -53.36043 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82da31ff-8d30-36ce-a931-d375d398f4a5 | -5.40834 | -49.11734 | 2025-07-30 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 752f31d9-636d-3a0f-86d4-9867d3f24dd3 | -6.50324 | -56.19333 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2efd6e14-b10f-38cf-8001-92b20d53cb2f | -8.02527 | -47.68212 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 885b26aa-c83e-3673-a2d6-46d397c38bf9 | -7.77945 | -45.0042 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ca8fbfd-851d-3b47-857d-09bbf9cbec57 | -10.61702 | -45.24312 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0b73d3e7-3139-32e8-a159-0d09d1c8c30f | -7.93948 | -44.08977 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 602a5b9a-3e2e-357c-bf5b-d1ca44083eb0 | -6.91423 | -44.73153 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f87bffb-57b3-3c68-85a7-4bf02c630e0e | -8.95512 | -46.73427 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15e51992-cf13-3e11-87e1-83146e283cec | -6.50257 | -56.19711 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d45a439c-6338-339e-be51-6a0261a65fc9 | -10.47796 | -46.66819 | 2025-07-30 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ae04d07-5b76-3981-934f-cbafcfc234dd | -8.07497 | -42.95195 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d35716bd-ac5e-3888-98c7-05589e12689b | -5.84847 | -44.22076 | 2025-07-30 04:27:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac60edd2-1a96-3a41-bec0-cb789c78736f | -3.27419 | -49.13779 | 2025-07-30 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82c2fd2-5d8b-3ea3-8213-9f0e51c979e0 | -6.39776 | -44.7502 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e065d3fb-ad5d-314d-be6f-09fa56ece63f | -3.8367 | -48.95803 | 2025-07-30 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82c291df-bb34-359f-9aea-647333fbd58e | -6.90063 | -44.7295 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8316047a-fee6-37a9-9430-5e7eda883aea | -4.64999 | -43.12514 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f2b5b57d-6691-3da1-a734-8d009bb4b5c7 | -6.44961 | -53.36448 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78b4c8e2-8e0e-306a-9d3f-14152151811e | -3.95301 | -41.48517 | 2025-07-30 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db076c35-08e4-3332-bee7-a80dae744286 | -8.0302 | -46.91127 | 2025-07-30 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f75da13-2541-3cf9-b8cc-555330b49a75 | -3.82409 | -41.56885 | 2025-07-30 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b4c8e2f6-9d01-327c-a920-94ea4ecf44cb | -7.31085 | -44.69395 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e438fd3c-3ebc-33da-a4c7-185a10d88149 | -5.68853 | -43.67999 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca4d6521-62ae-3b34-82b9-6b4b6a9fff7f | -7.2156 | -43.10712 | 2025-07-30 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 154dc0c1-788c-393d-8860-0cf7cee357ac | -9.86659 | -44.71023 | 2025-07-30 04:27:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 97b0e1c7-2a60-3d23-ba21-46a97d9c5604 | -2.90152 | -48.29425 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 922fa55a-b1b0-34a2-9392-22b0d12e1da4 | -3.51014 | -43.24993 | 2025-07-30 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d60255f-e859-3eee-903b-0ae76e00f123 | -6.40979 | -44.47204 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6c2d4d1-ede9-357b-abb7-62bc2010c7ef | -10.09555 | -46.96998 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e457ddbf-bc67-3e39-bcff-eca7d28196e9 | -7.20416 | -44.09378 | 2025-07-30 04:27:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf83dd7a-fc98-30a2-8c1f-da171eab46fc | -5.76187 | -43.96276 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2185383c-e3c1-33dc-9d8f-53ed985b5017 | -7.28144 | -44.54527 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c837434-a724-3356-845d-25844ac99fb4 | -4.30295 | -48.10096 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15950e97-1f3f-39e3-b0e2-663240e32794 | -6.54667 | -43.34613 | 2025-07-30 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3b01b288-b34b-3300-aaba-30e1c45eb8f2 | -9.04125 | -45.07894 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2928613a-8d64-3bc4-8c69-987d36a335a6 | -8.33594 | -54.7584 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0e5ab3c-e09d-307b-adee-a5ed4cf7558a | -4.58917 | -47.97737 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bc2865d-6466-3d35-934e-e9616c1d8b20 | -6.3941 | -53.36825 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae61b6b8-63de-3159-9430-0edebf8130ea | -8.41815 | -45.68617 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79aff989-2eed-313c-b50a-5fd8b11ea70d | -7.10382 | -44.38099 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e676c5-41d8-3951-ace1-7aeccd809c75 | -9.2719 | -40.55666 | 2025-07-30 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 13cbf6fe-f10b-32e5-bf65-00799ff2fb02 | -2.90497 | -48.24932 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7e91d905-b97a-3d62-8259-9cc085f6aacb | -7.94067 | -44.08185 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99eeaf82-790e-3fab-9bda-67809fd7db10 | -9.22942 | -50.04436 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 967825df-774d-314b-92c5-2d1fea3fd82a | -6.54456 | -56.1893 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8a94774-9527-386e-9a16-0585c7b55481 | -6.48791 | -56.21415 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3452a6ef-8b80-3887-8b1d-f7ed0d563fca | -6.39205 | -53.36446 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 259fa24a-434b-3ddd-99d5-8baf7ea7553b | -8.6422 | -45.5135 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7586f7cf-9372-35c7-aed4-f54bb0eaf5e5 | -2.90853 | -48.24987 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 1327c813-8d89-3858-b2a7-7126489b4963 | -6.52237 | -56.21649 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f266075a-773f-3ddd-bcdd-e1aa1b1702bd | -7.35444 | -43.76743 | 2025-07-30 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f40f9951-f752-393d-b112-f14b0d166225 | -9.39611 | -45.49274 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5e4d7402-74e8-302e-9dd5-ace74a55a4d6 | -8.95624 | -46.74874 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8449b0c2-f90b-3610-81d7-662381790b8a | -7.22971 | -43.08751 | 2025-07-30 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2eef9a46-d42a-3af8-9bab-524a5812f3af | -7.78339 | -45.00108 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02c7933b-e5e3-39a3-a951-adbae62a3b1c | -8.88321 | -47.33859 | 2025-07-30 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ba4aa9d-692d-328d-967e-bcc501ab7a03 | -7.35031 | -43.77085 | 2025-07-30 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33bc2119-8877-3d53-9550-06c0b1a45d5c | -9.04182 | -45.07525 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c52a6e93-1733-358f-9675-55da51e64f1b | -4.65768 | -43.12226 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50f94122-3dc1-334f-b7ff-a92f9aef63ee | -5.83202 | -44.03522 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34b64b99-b873-3b04-9c98-c7fc294bba99 | -6.72075 | -47.20821 | 2025-07-30 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c45f7d8-0ecd-32a3-ba52-5c9c0006c4db | -4.85336 | -42.9943 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfff5907-cae1-32c3-80d7-5ff6853254c1 | -5.76653 | -43.89856 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33f76705-bbe3-314c-a758-93afb59e94c7 | -7.33472 | -44.69767 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a271bef6-69ad-3984-ac4e-d2e5bb54f546 | -6.81286 | -44.64093 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b712d8a1-18d8-3d32-a231-4f05e2b244ef | -8.96066 | -46.7423 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ed5c17b-88d1-3d52-bb31-70104373c702 | -5.75842 | -43.90509 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b434d479-20eb-3689-b2dc-adde6fbaa226 | -9.83326 | -41.49739 | 2025-07-30 04:27:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4b11d679-c09e-3f8a-b7f0-fbc91f08d8bc | -6.89327 | -44.73214 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d411dc56-b1cb-3f41-a57d-de861ab9f856 | -5.76416 | -43.94765 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e55a1a0-1351-390e-b932-c88846078504 | -2.90509 | -48.29483 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b0b9eba-86fb-3149-91a2-a241f59119d4 | -5.75703 | -43.98215 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ef18912-16fd-3bf6-bdc5-3580ebca6e4d | -6.56544 | -56.18412 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1800d16f-38af-3ec5-a509-e3aa611b0218 | -9.59359 | -46.32974 | 2025-07-30 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README20.md)
