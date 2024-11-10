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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06903737-64b8-3b5b-87a5-2d876c624e1a | -3.9955 | -46.3981 | 2024-11-10 13:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| ab5151c1-2098-3500-9a6d-b740914ff71d | -17.6083 | -57.4482 | 2024-11-10 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.7 |
| 619a2ad0-e47e-326f-914b-6642f50411e7 | -2.6388 | -46.7597 | 2024-11-10 13:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 0a67fbf4-441a-3cee-97d3-c26d9ad87c47 | -4.0913 | -49.1323 | 2024-11-10 13:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c26b2e2a-fd73-3bb5-aa04-0dab02561a85 | -8.3778 | -44.1386 | 2024-11-10 13:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 283.4 |
| 647ef1c2-e222-3b55-9f4f-9c136d72d6a6 | -5.561 | -43.9544 | 2024-11-10 13:30:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 95d76eef-c0c1-3e43-a9c2-eff0b8d27031 | -2.0656 | -46.3339 | 2024-11-10 13:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 770d80bc-d36c-3793-b4d0-7066ec1743b6 | -3.9485 | -48.1508 | 2024-11-10 13:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5cacb214-5b16-340c-ae21-fcae2dbcf737 | -17.6273 | -57.487 | 2024-11-10 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.7 |
| dbb82a8c-5bb4-3115-97bd-7a155d346828 | -3.9486 | -48.1291 | 2024-11-10 13:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 764cec9f-8860-3983-b501-3096251113a1 | -4.9108 | -45.8598 | 2024-11-10 13:40:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 6179a6a7-4847-30e3-ae55-8414252dafda | -2.0655 | -46.356 | 2024-11-10 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 53c542ab-3e2e-3155-8374-f256a36b3e77 | -4.0913 | -49.1323 | 2024-11-10 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e2d8f0c7-345d-3e54-81eb-a86084f853e5 | -5.7146 | -43.5261 | 2024-11-10 13:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ff4de66a-7496-3a24-a6a3-33b3619ccb1d | -2.931 | -52.7753 | 2024-11-10 13:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 437a053b-2ecb-31fc-9c80-8d05a74c1651 | -2.0656 | -46.3339 | 2024-11-10 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 6ea5eb8f-57fd-3c6e-bfc0-1497f303845a | -2.4182 | -51.9689 | 2024-11-10 13:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 144f2985-a977-32f6-a79a-404b3f2f43a9 | -2.2502 | -46.5723 | 2024-11-10 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| bdf6a420-cc88-38fb-8b69-1b47ebc846f1 | -4.0915 | -49.111 | 2024-11-10 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 20d7f4ad-cc33-30f0-a3d1-f2c1bd4fb400 | -17.628 | -57.4458 | 2024-11-10 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| ee656940-2152-3924-a2b3-caeba1006f84 | -5.652 | -44.2471 | 2024-11-10 13:40:00 | GOES-16 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5b175994-06be-34e2-b8b3-795d48df20cd | -1.5163 | -52.1901 | 2024-11-10 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 63d95b48-24ff-3635-8cd7-3be5a3e14037 | -17.6069 | -57.5304 | 2024-11-10 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 298.8 |
| e6c9c601-493b-38d7-a2ff-83b8f84837c1 | -23.9095 | -54.0606 | 2024-11-10 13:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| d7a7e1af-9023-340f-a87d-6753570130eb | -2.6388 | -46.7597 | 2024-11-10 13:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 2f0d6cc4-4adb-3e66-b633-7b6fef031122 | -1.5299 | -54.9941 | 2024-11-10 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| a3b7724e-1020-31e4-aa1a-dc13f57431c9 | -2.0842 | -46.3334 | 2024-11-10 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 178e8e52-078b-3b13-be6e-3b515eb01be0 | -2.2095 | -47.733 | 2024-11-10 13:40:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| bd11ba33-6cea-3c20-9471-48026d3fd5f3 | -3.9483 | -48.1724 | 2024-11-10 13:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 5d022d22-e8fa-339c-aebc-efecb58396bf | -3.9669 | -48.1716 | 2024-11-10 13:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b4e51b2d-2e1f-3f19-9ef5-bb695b82e9e5 | -2.4092 | -48.8905 | 2024-11-10 13:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 811b7efc-81cb-3c9f-b8ec-2dae126a2eaa | -3.2721 | -42.5044 | 2024-11-10 13:40:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 406ef54c-d5b3-3731-94fa-49b625abf1ad | -2.4183 | -51.9484 | 2024-11-10 13:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9fb08885-13aa-3564-a19f-289ad067467f | -2.1766 | -46.4196 | 2024-11-10 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0f2d8232-d5e3-3b55-8a8e-34bf442574e6 | -2.0954 | -48.8125 | 2024-11-10 13:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 49892c7f-7e77-3cec-bdf7-cd2df97b5cc5 | -6.2564 | -45.6795 | 2024-11-10 13:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 34e76e48-7b65-3619-bbdc-ee2bb0bac823 | -4.1035 | -43.9539 | 2024-11-10 13:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f9de4219-9f66-3a27-aa12-80017e872481 | -4.1246 | -43.5833 | 2024-11-10 13:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b8657e85-b761-3c73-9823-f361cfa6d1f0 | -5.0605 | -43.3869 | 2024-11-10 13:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0e63dfc8-06c6-355d-bc9d-59deb31861b0 | -2.0664 | -46.0899 | 2024-11-10 13:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8a439486-08bc-3286-b480-6a98cff25ed6 | -5.9788 | -45.3621 | 2024-11-10 13:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c76adb28-610e-3c4d-8c12-af145bbf19b3 | -2.8605 | -51.8349 | 2024-11-10 13:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 76b2a5b2-a278-34e0-8ca6-2649f3a55805 | -2.0953 | -48.8338 | 2024-11-10 13:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 43914ba0-1655-3c1e-8fc8-f664b55d58da | -3.2615 | -41.0005 | 2024-11-10 13:40:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 196.2 |
| 7c111cc4-d0fb-339c-b4b5-8d2612822b03 | -3.8876 | -49.1407 | 2024-11-10 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5abfc373-2a2d-31fb-8a70-2af6b2738c9f | -2.1021 | -46.532 | 2024-11-10 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ed62ecde-9056-3fef-9034-8ed9d43e9e72 | -1.5116 | -54.9944 | 2024-11-10 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| afd0e801-0879-385a-9c5a-1eb2d2922c42 | -4.3979 | -41.8987 | 2024-11-10 13:40:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 029d3101-9a40-3411-936a-8e03e25a144d | -4.0267 | -44.3023 | 2024-11-10 13:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 90a7c44c-fba1-3e43-bf77-d5349d605a45 | -5.66 | -43.344 | 2024-11-10 13:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| de041d49-c739-3e4e-b49b-6061b05f6a74 | -17.6083 | -57.4482 | 2024-11-10 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.9 |
| a3ab596e-e37c-3ce0-9e6a-3cdb696ce081 | -3.9955 | -46.3981 | 2024-11-10 13:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 4024c9e1-0cb9-32d0-bef2-dcb69bf172c2 | -5.5608 | -43.9775 | 2024-11-10 13:40:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 6685d249-2847-35e0-94c5-cc15bf76d27d | -6.2377 | -45.6809 | 2024-11-10 13:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 22151ecd-d685-326d-a8f0-7907ec68715b | -8.4156 | -44.1344 | 2024-11-10 13:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 503e97a8-613e-3604-86c4-7fe432046740 | -4.1099 | -49.1315 | 2024-11-10 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 72133d2d-769a-31ad-a144-40950bf9da67 | -4.4349 | -44.6229 | 2024-11-10 13:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 168.5 |
| f69f2ba2-ec36-368d-aa3e-9bbc226753c2 | -5.4546 | -43.2659 | 2024-11-10 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 69483def-2fad-3a16-830f-4dc00945a5a9 | -1.1672 | -52.0918 | 2024-11-10 13:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 62.8 |
| cbd28f62-5d7d-32f1-b19d-522361f2eb21 | -17.2933 | -57.4857 | 2024-11-10 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 180.1 |
| 1153295b-8831-3ff5-bdd8-bdd8505137e5 | -4.1244 | -43.6064 | 2024-11-10 13:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e2249a63-aad8-328d-9eae-cdee13b37d27 | -2.0478 | -46.0903 | 2024-11-10 13:40:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e0a9e9e5-7edf-3f5c-84ca-271ad22afb4b | -1.3741 | -49.3579 | 2024-11-10 13:40:00 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 87696894-6a49-3fa3-a4cf-aea9c2311fde | -17.5872 | -57.5328 | 2024-11-10 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.7 |
| 0e208ccf-76ba-39ac-ab55-094303fc441d | -6.3689 | -45.6483 | 2024-11-10 13:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f94b4de7-54f3-3e3b-bd7a-5eda10a859de | -2.0841 | -46.3556 | 2024-11-10 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 19fd2b03-828c-30ed-bf50-6fe600e7da1b | -5.455 | -43.2192 | 2024-11-10 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 29ee5ca8-383e-32d4-abd3-1f537ebf020b | -3.9953 | -46.4203 | 2024-11-10 13:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 126.6 |
| e25c28ec-8f29-3abd-965f-53c72f78c92d | -17.6073 | -57.5099 | 2024-11-10 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 367.8 |
| e83f80e1-7876-3347-996c-46ab96b52932 | -3.8413 | -44.1283 | 2024-11-10 13:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 03a4452f-04f5-38f3-a86b-504e1aefe4c3 | -4.1246 | -43.5833 | 2024-11-10 13:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ef4482cd-d078-3288-a2db-9ee932ee6e65 | -17.628 | -57.4458 | 2024-11-10 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.9 |
| ab39757f-d90e-3c5f-a0f4-28039f5bf29f | -3.8413 | -44.1283 | 2024-11-10 13:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 20a05a0c-1b6a-35e7-a788-e4dc5fcb79e3 | -5.4689 | -41.656 | 2024-11-10 13:50:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| e9a0c693-2de2-3f36-9ab1-d6d3a0cde110 | -6.2564 | -45.6795 | 2024-11-10 13:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6f5915ae-e5f5-3c0b-b0f2-6f0cfefd84ea | -2.0656 | -46.3339 | 2024-11-10 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 77c2c822-0051-3026-9e03-446b06a1e838 | -1.3741 | -49.3579 | 2024-11-10 13:50:00 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 732ee653-6c3d-366b-938b-2b0f67957113 | -2.6388 | -46.7597 | 2024-11-10 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| f5e4a849-f05c-3a7a-8b20-b2599cc4c8c2 | -4.1244 | -43.6064 | 2024-11-10 13:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ec38a9ba-9c79-36ec-b7a0-b70e73f4dc2d | -3.9486 | -48.1291 | 2024-11-10 13:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 383871f6-ca6c-3d90-ae4c-be90b8588b52 | -3.686 | -45.2276 | 2024-11-10 13:50:00 | GOES-16 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| bb0156ee-4b3a-3d81-99dd-7e0e600cc8ab | -1.8943 | -48.0 | 2024-11-10 13:50:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| b87d6ea6-705f-33f1-93c5-09fa1b665db2 | -2.0954 | -48.8125 | 2024-11-10 13:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 179.4 |
| ec15f8bd-2dca-347a-8486-1a48b3df5b3c | -4.3228 | -44.6519 | 2024-11-10 13:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1dc5e105-683d-3478-9908-45459f6379e7 | -2.8605 | -51.8349 | 2024-11-10 13:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| da128bdb-5e65-3325-b5f9-9b6f2b5278a2 | -1.4576 | -54.3168 | 2024-11-10 13:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| de7c9728-a4ff-37f7-9347-7cf980a7b97c | -4.2134 | -44.2696 | 2024-11-10 13:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| cdf90ea6-16d6-30f0-9687-518b314dc3d2 | -2.931 | -52.7753 | 2024-11-10 13:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 63441a13-f326-3c13-b5c7-0ac67f71bc59 | -23.9095 | -54.0606 | 2024-11-10 13:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| 3ddaaebf-fbc3-3c25-aa3b-8dadf36c5a62 | -6.3772 | -44.7868 | 2024-11-10 13:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 175e3b39-cdab-363a-a840-2ab0ee26eeb2 | -2.0478 | -46.0903 | 2024-11-10 13:50:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 9ec839c6-e8c0-3acc-8d7f-e9cb4106e4c2 | -4.0913 | -49.1323 | 2024-11-10 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f6e11f2d-00d7-330b-98f4-f422ae751e41 | -3.2615 | -41.0005 | 2024-11-10 13:50:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 121.8 |
| a96e9eae-4247-30cc-a560-bb7fed2e022d | -1.9912 | -46.4241 | 2024-11-10 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 697f917c-9717-3165-bab1-bd71c0a5c36d | -1.1672 | -52.0918 | 2024-11-10 13:50:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8f1c2c26-4cfd-3f9b-b305-ce59f26db473 | -2.1208 | -46.4873 | 2024-11-10 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| a7274ff3-9705-3879-b52c-0eaf85e93739 | -3.9483 | -48.1724 | 2024-11-10 13:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 032eaf20-b919-36a1-b487-17bca7b84c14 | -4.0915 | -49.111 | 2024-11-10 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 3db38010-582c-3126-8c78-f8ee4a5064a1 | -6.2377 | -45.6809 | 2024-11-10 13:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| aaf8426a-bfe7-3925-8b6a-07c7d15167e5 | -5.2994 | -46.2379 | 2024-11-10 13:50:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |


[Clique aqui para ver as próximas entradas](README130.md)
