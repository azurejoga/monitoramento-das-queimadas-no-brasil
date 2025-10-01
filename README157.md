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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c03ead8-ef06-3655-9519-e5ce68381b97 | -10.8421 | -46.6514 | 2025-10-01 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e1351990-b270-3546-a028-9ed5b4cae58e | -7.8882 | -47.281 | 2025-10-01 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 5d065f35-1158-369b-a739-3ac846d5c6d2 | -9.4458 | -47.5923 | 2025-10-01 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1255b7cc-b54a-346b-9d0a-0d74460ebfd7 | -8.483 | -47.7983 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| cc971f49-624c-3853-b5da-fa4d2fac1358 | -13.7868 | -48.03 | 2025-10-01 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 8faed628-959a-3c19-a561-847040a53320 | -15.7707 | -43.7197 | 2025-10-01 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 016248d2-fe21-3bc5-ada9-7874b0fe9092 | -13.3808 | -48.0908 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 129.5 |
| c588b29f-20f0-3cc2-9658-ba7029d44e07 | -6.0602 | -42.6789 | 2025-10-01 13:50:00 | GOES-19 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 7554be45-3a69-33bc-9d26-da7c7271d799 | -5.9366 | -45.905 | 2025-10-01 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 278.3 |
| e1200b05-2a8c-39c0-a313-5697dc47893a | -11.383 | -45.0543 | 2025-10-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e232c9af-8695-388b-825e-59caf6949fa4 | -12.7822 | -50.5328 | 2025-10-01 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 7af0396b-aaae-32ae-970c-ecc91191d77c | -9.9581 | -43.5987 | 2025-10-01 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f9a0d497-3607-339a-8a73-4017dd14ab1f | -8.5267 | -47.2879 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 63846309-a515-3438-8b48-0bdf1b156040 | -7.1815 | -41.6931 | 2025-10-01 13:50:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 2bc57c76-0e3c-35e1-abd7-87ed902d2723 | -12.801 | -50.5519 | 2025-10-01 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 33ba8a6c-f818-3736-ab5e-6c1e0b20e59b | -8.5079 | -47.2897 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 880a8e13-c6af-3fcc-b97f-6de848303b8d | -7.8884 | -47.259 | 2025-10-01 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4d346549-20bd-30df-ab96-dbb16e0d9cfa | -14.8212 | -45.8143 | 2025-10-01 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 54f58a8d-ffe2-35c6-a5f5-25e5f98feec3 | -14.9733 | -46.8896 | 2025-10-01 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 851627a3-0d4e-36b9-af9a-84e86d4e7fed | -8.5218 | -44.6765 | 2025-10-01 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7b9555ae-4830-3800-8176-e67f0827dbb1 | -12.8831 | -46.9101 | 2025-10-01 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| e26946e4-2095-3b1b-b52d-72f68323ca57 | -14.3657 | -47.1291 | 2025-10-01 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 5924920f-72da-3684-81be-81d0b9b4e826 | -6.214 | -44.2272 | 2025-10-01 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c8263835-7282-3718-9cf3-3f81c6de6a7a | -8.8609 | -47.6521 | 2025-10-01 13:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 4619c18c-ea16-3d9b-bba7-b0fbab463134 | -9.9035 | -45.9553 | 2025-10-01 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 0796bdcc-f3a6-372d-9564-bb5d78335cc3 | -11.4592 | -45.0664 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6516445e-10fd-31a8-8c49-ca762503a1b1 | -8.5016 | -47.8184 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b572a595-d86d-354b-b9c1-64f61bbdbb84 | -8.6911 | -47.6906 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 559bd08a-89c3-3b92-81d2-4631f4cd6898 | -5.9555 | -45.8812 | 2025-10-01 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 274.1 |
| f587a3e9-ebd1-34d9-91b3-5b04b1e1a5b0 | -12.8967 | -45.1711 | 2025-10-01 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 083af5f2-fd7d-30b1-a1aa-80e3895e66a9 | -9.9376 | -43.6953 | 2025-10-01 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 282.7 |
| df12979d-40e3-34d1-b664-978bddfe04ad | -12.8014 | -50.5304 | 2025-10-01 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 04bfd0ee-e1f4-36cd-817d-fc8cb0ad39bc | -8.672 | -47.7144 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 13e68118-28f6-3690-ac11-6b9b3ad2efdb | -11.1757 | -47.2134 | 2025-10-01 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| bf7aa2e3-2afc-3860-ac05-a165f137432c | -16.0225 | -50.8771 | 2025-10-01 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 175.2 |
| f08d0405-0143-3da0-ad16-e533b80a105f | -9.938 | -43.6718 | 2025-10-01 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 317.8 |
| 9c2b7be1-ac9f-32b6-87ad-84dcbec8995e | -9.9383 | -43.6483 | 2025-10-01 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 268.6 |
| b13e0355-66b6-3050-8589-64571d75cd8b | -16.0421 | -50.874 | 2025-10-01 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f9ee9c56-15ff-3c89-9e82-6614c624a0b0 | -16.0221 | -50.8989 | 2025-10-01 13:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 145.2 |
| d2d4b1f6-b872-3c46-a3e7-0e79a63b3599 | -11.3296 | -48.3235 | 2025-10-01 13:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 3262f7f0-d370-359f-854b-d08de10ac2e5 | -9.1889 | -48.5166 | 2025-10-01 13:50:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 73bf7afe-8cd3-32c2-980a-928f5b4a709d | -10.8991 | -44.3119 | 2025-10-01 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| fcbf1e87-ec31-36ff-8293-03a3521daae5 | -8.5407 | -44.6745 | 2025-10-01 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 05edc97f-11dd-33bb-b490-d69ace6e60ba | -12.2536 | -47.806 | 2025-10-01 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| fd3cf066-a66a-3cb4-95b2-949fb2b9ef14 | -13.3414 | -48.1411 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 81f20073-960d-39d1-9743-e7f8e02b116e | -10.9182 | -44.3092 | 2025-10-01 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| dfc7e004-fb23-37db-b2c8-867f80d78eb9 | -6.3 | -45.0205 | 2025-10-01 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 9ae47593-40e8-33d2-a236-15583c636e3c | -13.3611 | -48.1159 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 5f9629c4-f9a6-3733-8f62-b0db63f0858a | -13.7691 | -47.9435 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 153.8 |
| dc8080ab-a031-38b5-bf0e-ddc505641656 | -13.7869 | -51.2404 | 2025-10-01 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 2dcf5618-b887-3287-a3c9-7f7c9c27d957 | -14.3714 | -45.9172 | 2025-10-01 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 3d5612aa-17dd-3687-a7e5-ac507b7a850c | -9.4644 | -47.6124 | 2025-10-01 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| b41182a1-7aaf-3bfc-952a-6e349d5665e9 | -7.8218 | -48.2069 | 2025-10-01 13:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| f1ab296f-ba41-3827-a7a3-31f33f93bb89 | -13.327 | -47.876 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| cbbf9e5d-c247-31f4-a3ea-f1eb8d8cbb0b | -12.2816 | -44.1275 | 2025-10-01 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 21cb00c5-7456-3ef3-ae89-493a23b08bde | -11.9411 | -47.0675 | 2025-10-01 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 51c93561-e876-3855-84d0-4fbffa23081b | -5.9557 | -45.8588 | 2025-10-01 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 00f5f486-a2ca-3b46-b82e-6a84b9832869 | -7.5749 | -46.7778 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| e4648744-5e5e-31d2-b6b4-b00ad15aa06c | -15.5379 | -45.2375 | 2025-10-01 13:50:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 16966ca0-8603-3ace-96b0-747ba4f12d14 | -8.5584 | -44.7644 | 2025-10-01 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| ad605276-ad98-3321-81aa-331bcd794215 | -8.2105 | -47.0084 | 2025-10-01 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 81197431-462f-3663-a3d0-fb1508c07de5 | -13.6703 | -48.07 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| aa6bf0aa-c0d8-366c-b177-5665cbe1fbe5 | -7.5561 | -46.7795 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 68646daf-1da6-3f30-9369-d755c781942c | -11.46 | -45.0202 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 8ee9b36c-6094-3133-9aa6-586fb73f2f35 | -6.7356 | -44.5742 | 2025-10-01 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 74df143d-c16f-3421-bf1b-d0a69ff45a2e | -8.5776 | -44.7394 | 2025-10-01 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 5a89f273-1428-3700-8743-74533b6b103a | -6.0999 | -42.4628 | 2025-10-01 13:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 49e2786e-1b13-3cdc-8a85-a738b8f1125a | -8.5773 | -44.7623 | 2025-10-01 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 4ccdae78-dae4-38b0-802c-e860083d1cf6 | -6.0997 | -42.4865 | 2025-10-01 13:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 337866fe-7191-3aac-853d-12c30ec2163d | -13.1747 | -47.7869 | 2025-10-01 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| cfbf3fc3-f3de-34b9-aab3-53868a5d1001 | -11.8438 | -44.964 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 93486d94-65be-33cb-91eb-7dc71396e1b4 | -12.3669 | -50.2187 | 2025-10-01 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| fac0dc1d-1e44-37c5-b6df-cbf00d3c82ba | -15.2742 | -49.2852 | 2025-10-01 13:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 191.8 |
| ebb6b3ec-2b78-3312-a579-c8d9e0dcc29e | -14.9084 | -47.1965 | 2025-10-01 13:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 53c53710-8c26-30f8-afec-1db5d5b01235 | -6.2998 | -45.0433 | 2025-10-01 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 4517fa4f-1949-3d6f-b536-eeb74377d439 | -8.88 | -47.6282 | 2025-10-01 13:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1a2795fa-4eee-34e4-8c4f-bc011132320f | -8.8797 | -47.6502 | 2025-10-01 13:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 359f798e-6982-3ab6-84b5-752b8d265283 | -8.8923 | -46.6519 | 2025-10-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 4af87c89-908a-3524-b8ba-78fba13c6a4c | -13.6896 | -48.0671 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f9507e30-bd53-3f77-91c7-973cff3d5e24 | -14.3514 | -45.9437 | 2025-10-01 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 9f41896e-798f-3dfd-a584-d5926462c11d | -6.0978 | -42.6758 | 2025-10-01 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 24f0ea97-c99d-3532-b447-62eb8ea8e470 | -5.9368 | -45.8825 | 2025-10-01 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 185.7 |
| c5c89e2a-1b24-3258-8745-f9e38fbeac93 | -12.282 | -44.1039 | 2025-10-01 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 15a29ea4-8484-31c4-83e2-2cccee9f35da | -11.7984 | -47.6003 | 2025-10-01 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 20d7c53b-9093-34b2-b196-a3cd703bd3fd | -8.6722 | -47.6924 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 90f39852-5015-3ccd-9d7c-e7f53e7cce00 | -5.9414 | -43.3221 | 2025-10-01 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 973b0bb9-4785-35d2-9d53-84018a98018f | -7.6275 | -45.428 | 2025-10-01 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ccf910a8-0f57-3721-9878-cd8e97d1667a | -9.4455 | -47.6144 | 2025-10-01 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 08df25a2-8e8c-30c9-8427-e889df835e5b | -7.5749 | -46.7778 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 5e3002ea-120e-3995-87c3-788808c39d84 | -5.8064 | -43.728 | 2025-10-01 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| a3fc6f05-5476-3052-818e-6f0fba1afd0d | -10.8421 | -46.6514 | 2025-10-01 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 1172efc3-d3b0-3ff8-b70b-4f335c106a7a | -6.3 | -45.0205 | 2025-10-01 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 337de625-15cd-31c2-8ca9-7223a220b207 | -8.5584 | -44.7644 | 2025-10-01 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 544f0771-9daa-3735-a68b-03279c20856d | -13.3274 | -47.8536 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 5fe059fd-b8b0-34a9-8a42-5497ea223af3 | -8.5079 | -47.2897 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c9c3476a-3649-3fb0-8dd1-d21988598450 | -14.9084 | -47.1965 | 2025-10-01 14:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f2738b41-53d6-3859-845e-197eef7e87c4 | -8.5016 | -47.8184 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 59c114bd-e46c-3710-b378-295828544a68 | -13.3414 | -48.1411 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 280.8 |
| ffdeec89-20b1-3578-aefc-a49a014245d6 | -11.1368 | -49.7823 | 2025-10-01 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1256bea6-8465-3674-b0e2-b26a38c81a64 | -13.3997 | -48.1103 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |


[Clique aqui para ver as próximas entradas](README158.md)
