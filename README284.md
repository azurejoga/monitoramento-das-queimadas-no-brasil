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

## Dados Diários - Página 284

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73d190e1-1d6c-3be4-a8ad-2f58d9cc8bb6 | -8.9501 | -45.1334 | 2026-10-09 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 220ae5b7-79e6-3ea5-a243-9d97c1bdb845 | -8.9308 | -45.1584 | 2026-10-09 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| cde05ac1-3fcd-375b-bab3-f2c672087275 | -1.4118 | -48.9318 | 2026-10-09 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7b9a1216-f26a-3a6c-beaa-b66a46d29345 | -2.3481 | -57.9824 | 2026-10-09 16:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1a226294-5f87-315c-a54a-a3b24413ab1e | -8.9116 | -45.1833 | 2026-10-09 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 3e0a067e-f412-3a4d-9f65-6c68eec97d42 | -3.1697 | -58.6244 | 2026-10-09 16:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 0095071f-e114-301e-a177-d5d231d1c208 | -15.0713 | -41.7982 | 2026-10-09 16:10:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 373.1 |
| e7c900f0-d83d-3acf-90c8-57edcfb8288b | -13.1636 | -54.3591 | 2026-10-09 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 506.7 |
| 1a500f80-8846-38a1-8ee0-0cd765441771 | -12.2316 | -44.7427 | 2026-10-09 16:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 08ad1daf-cba9-3355-9631-ef08a3650488 | -9.9018 | -44.7917 | 2026-10-09 16:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 521.0 |
| 257bd2aa-54e6-35a4-bd6e-ea3d37428e87 | -6.07 | -44.63 | 2026-10-09 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb6fe6a-a252-3820-97c6-f09b6e553b0f | -7.02 | -47.7 | 2026-10-09 16:15:00 | MSG-03 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38ad70e3-1c43-3c49-a645-940e40a9ca0a | -5.06 | -36.95 | 2026-10-09 16:15:00 | MSG-03 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| dfe343f0-e7b3-311c-af75-31015bbb678b | -5.17 | -60.32 | 2026-10-09 16:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f60b8b72-619c-345a-84f5-abbe1d9246ea | -6.99 | -47.69 | 2026-10-09 16:15:00 | MSG-03 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e72965f3-5625-33da-bc0c-33891d966697 | -11.02 | -44.07 | 2026-10-09 16:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5034dbad-047b-305d-a1c6-bd49ff25ba72 | -6.04 | -44.67 | 2026-10-09 16:15:00 | MSG-03 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8905cccb-be11-3735-9949-800ba1e4e319 | -15.38 | -41.97 | 2026-10-09 16:15:00 | MSG-03 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35ae11f1-9d13-364a-82af-6d8c0351dd92 | -11.05 | -44.17 | 2026-10-09 16:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a300ea1-29c1-3845-8c4d-5b0fb76faad4 | -5.09 | -36.95 | 2026-10-09 16:15:00 | MSG-03 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 35d07d48-830f-3d93-85b3-84f2ea0682f5 | -6.07 | -44.67 | 2026-10-09 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4db247f3-aa68-3c1f-8b14-bb16d647f51b | -5.09 | -36.91 | 2026-10-09 16:15:00 | MSG-03 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| e948a5da-82ac-34f7-849e-b9220bffc750 | -12.19 | -44.83 | 2026-10-09 16:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f054de9d-9c6d-363b-b91e-ccbfb90ddbfb | -5.17 | -60.24 | 2026-10-09 16:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3f5a6f-671b-37d4-8232-b5aeaeb94eac | -11.05 | -44.12 | 2026-10-09 16:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c636549a-29e1-3b6f-81c5-5f02528518c2 | -1.4118 | -48.9318 | 2026-10-09 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 18f7a498-868d-3293-b6b5-3bcd2c8a06ad | -13.1636 | -54.3591 | 2026-10-09 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 448.5 |
| ac2e3040-0e31-3454-aed8-5bf5a429495b | -12.2316 | -44.7427 | 2026-10-09 16:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 95f7c8be-980f-3f14-bd0a-bf643709eeee | -8.969 | -45.1313 | 2026-10-09 16:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| ae47bcd5-843e-3166-aaac-e71fb1c68ffe | -2.572 | -56.1646 | 2026-10-09 16:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8c4c1743-55b4-314e-9005-ae53caf8fca9 | -1.5281 | -56.121 | 2026-10-09 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| cb08022d-82ad-364d-afe7-11f0848f2672 | -12.2316 | -44.7427 | 2026-10-09 16:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 76c5a0ce-cbd8-369e-a107-8d7e47ea17cf | -1.4118 | -48.9318 | 2026-10-09 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3255a110-fe4a-3b6f-a1a3-58594215bd28 | -15.0713 | -41.7982 | 2026-10-09 16:30:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 218.7 |
| 8ba3b4d2-3ca8-3c56-b153-b1eaeed6d2e9 | -10.9388 | -45.3687 | 2026-10-09 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 70dcb7b1-8db3-3fe1-9400-17d7f77f24d5 | -1.5281 | -56.121 | 2026-10-09 16:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ba26c9e8-2c84-3c3a-b1d6-07950213d01b | -12.2316 | -44.7427 | 2026-10-09 16:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a5a9d354-7da4-3810-aebe-e8338f49dfdd | -10.9575 | -45.389 | 2026-10-09 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 659ee7a2-7f86-3f72-8c99-8d81b5e79227 | -1.1713 | -49.2969 | 2026-10-09 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 80ca0359-02f9-310c-9790-ff736b8457e4 | -10.9953 | -45.4068 | 2026-10-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 8993766e-1534-3f51-91bd-f16728f5dc4c | -12.1948 | -44.6554 | 2026-10-09 16:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 218fd00a-8551-31ca-a0a3-a5581ae9872e | -1.5281 | -56.121 | 2026-10-09 16:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 44f68e60-a335-3f61-b3a5-e7d49a099ed2 | 1.7488 | -55.5663 | 2026-10-09 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2a221c5b-4709-310f-a060-b8a616407971 | -11.014 | -45.4272 | 2026-10-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 79a3002e-f445-354a-b8fa-9d2c71d6dab2 | -12.2316 | -44.7427 | 2026-10-09 16:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| d9c56348-bec8-3bf4-b7d9-725065c36c97 | -12.2311 | -44.7661 | 2026-10-09 16:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 526.2 |
| 06511cc4-867c-3a64-aaf1-716054a59c4a | 1.7304 | -55.5863 | 2026-10-09 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 5b987b72-b286-3e6f-84c5-bbc7b724a04c | -10.9953 | -45.4068 | 2026-10-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 73e07ba7-ec43-301e-be4c-ab11846767d5 | -12.2316 | -44.7427 | 2026-10-09 17:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| f962af24-9770-36ed-9224-77ab7da2e513 | -12.2311 | -44.7661 | 2026-10-09 17:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 611.7 |
| 0976998a-98ad-3cda-bf8b-ee34bfbb5ab3 | -1.5281 | -56.121 | 2026-10-09 17:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8d111d2e-cdf3-32b6-b4cc-fca7fe5a1e95 | -13.1641 | -54.3178 | 2026-10-09 17:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 30dd2e4b-fa96-34aa-8088-0cf5b006ea82 | -12.2123 | -44.7457 | 2026-10-09 17:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 228.0 |
| 8ac52c26-24de-3872-8b10-076d058cbd88 | -1.5281 | -56.121 | 2026-10-09 17:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| f8d0b477-23a6-3f46-aa73-d44afc5b10f6 | -10.9575 | -45.389 | 2026-10-09 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.1 |
| dd12ea17-2497-3402-ba3a-7e2fd7eda638 | -13.1639 | -54.3385 | 2026-10-09 17:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| a6951d42-03d1-37ae-af93-eea3fd616e3b | -10.9384 | -45.3916 | 2026-10-09 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b197b266-84ac-3fd1-a6e5-c61472601249 | -15.0516 | -41.8024 | 2026-10-09 17:10:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 140.6 |
| b07e3ae0-5e7e-3cff-ace8-ab0462f0322e | -11.2849 | -45.2063 | 2026-10-09 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 56099c53-c099-3c06-ab43-31d03cb4d81b | -5.2 | -60.33 | 2026-10-09 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9b94e2-2e25-3b7d-8d69-4d254738cbe3 | -5.62 | -40.85 | 2026-10-09 17:15:00 | MSG-03 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| baeb4c0a-6744-339c-ab14-3305796db9a3 | -15.08 | -41.79 | 2026-10-09 17:15:00 | MSG-03 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d2a07075-de2f-3a45-a41d-950425d702f2 | -5.62 | -40.8 | 2026-10-09 17:15:00 | MSG-03 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 248af887-4b65-343f-83f4-ef89a800dafa | -15.25 | -42.37 | 2026-10-09 17:15:00 | MSG-03 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b0b36f3-9a46-313c-a9e6-4e7e4daa67f3 | -5.2 | -60.25 | 2026-10-09 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2fbfbe-8334-3486-bef8-0f411e34b8aa | -15.25 | -42.42 | 2026-10-09 17:15:00 | MSG-03 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d66dbe0c-aa02-3633-8b0e-b903f8aea1e2 | -5.11 | -60.23 | 2026-10-09 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7682e9f5-b5ba-303b-bb87-38969cd5e564 | -5.59 | -40.8 | 2026-10-09 17:15:00 | MSG-03 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 42534f15-1a11-35da-a0d5-2cd8bd20af04 | -5.08 | -60.22 | 2026-10-09 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78daf0c2-32b7-31af-b484-785b67c5bcb5 | -15.08 | -41.83 | 2026-10-09 17:15:00 | MSG-03 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04bf3ff4-60af-3970-bea5-2ad9d99bc4ef | -6.46 | -43.45 | 2026-10-09 17:15:00 | MSG-03 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a658ef74-62eb-3b1e-b907-1ca190d7f571 | -5.11 | -60.15 | 2026-10-09 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45f231f4-2a53-3fb4-b2c8-4a473628a95d | -7.52 | -46.12 | 2026-10-09 17:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f32f2acd-693f-3a1e-9208-41b46f2942e5 | -14.45 | -40.74 | 2026-10-09 17:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f07ffc5a-a7cc-3d3a-ab01-cef62847f08f | -14.36 | -55.02 | 2026-10-09 17:15:00 | MSG-03 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 880f36c8-5ba6-38fa-bbae-0cf01c2fec9e | -8.91 | -45.23 | 2026-10-09 17:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5e84bbb-c884-3021-9821-39346e5e4e54 | -15.0516 | -41.8024 | 2026-10-09 17:20:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 190.6 |
| 7dfbfb07-80f3-3970-88cc-7d2823418f6d | -12.2123 | -44.7457 | 2026-10-09 17:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 413.8 |
| 2bfbf82a-5fad-3a9d-b9e6-bb1b6b80e112 | -12.1935 | -44.7254 | 2026-10-09 17:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a4d1b5e6-9017-3c05-8295-1907157dbc8f | -11.2083 | -45.217 | 2026-10-09 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 21ffd509-607b-35bb-b5dd-e3094f6a9a62 | -12.2508 | -44.7397 | 2026-10-09 17:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| d09eda54-fe98-302f-a166-5eb45c64d742 | -3.5893 | -59.0773 | 2026-10-09 17:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7814035a-18d8-31d9-a2cd-40df4c4949fd | -9.1015 | -45.1164 | 2026-10-09 17:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| af9958f9-8b8e-3391-be6a-8d261701acfa | -3.4278 | -58.0203 | 2026-10-09 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 531490a1-4cca-3504-a26a-2653cbe9c795 | -13.1636 | -54.3591 | 2026-10-09 17:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 361.0 |
| 457a9560-709f-3c1a-80dc-debe5d41b32d | 0.5246 | -50.8991 | 2026-10-09 17:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c4268620-f689-339f-ad80-e9507969fc1e | -1.5281 | -56.121 | 2026-10-09 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9db59d48-6ec8-3731-9e2c-087bf58b1d59 | -11.1145 | -44.0009 | 2026-10-09 17:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 255.0 |
| dba2d1ec-4019-3602-b0eb-e19d9f41fe2f | -9.9208 | -44.7893 | 2026-10-09 17:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| addd854a-ac2b-3466-81ff-2998cf7b2347 | -12.2311 | -44.7661 | 2026-10-09 17:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 84c574b3-399f-3243-a551-11860da5ada8 | -13.1641 | -54.3178 | 2026-10-09 17:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 5bdae966-023d-3d2d-a15a-74490bcc79f6 | -12.2316 | -44.7427 | 2026-10-09 17:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 57394f74-2762-35cd-a4c4-6b43af9ce77e | -8.3583 | -44.187 | 2026-10-09 17:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| dfc893c6-baec-3738-b598-48a48a3bc1a2 | -13.1639 | -54.3385 | 2026-10-09 17:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 192.9 |
| 96b8fff0-0db2-38bb-b79d-9066308e133f | -11.075 | -44.0768 | 2026-10-09 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 9b463ce8-9737-3c96-9c4b-7dff1ca1db0b | -1.7369 | -52.2484 | 2026-10-09 17:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| cb318d06-5e90-3820-899d-ef68d8b29427 | -11.014 | -45.4272 | 2026-10-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 79a6f580-8753-3112-a97c-c706232b111d | -9.9018 | -44.7917 | 2026-10-09 17:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 898c6914-e936-3d38-bd5a-15ec3037a06c | -3.5709 | -59.0969 | 2026-10-09 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 855e109b-74e6-3166-a767-eb36f61ef893 | -12.1948 | -44.6554 | 2026-10-09 17:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 245.4 |


[Clique aqui para ver as próximas entradas](README285.md)
