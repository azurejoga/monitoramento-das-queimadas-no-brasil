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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90b3fc53-6306-3d9b-9887-5643af5c67df | -13.8199 | -44.4547 | 2025-11-16 14:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| b2fe1b7a-8bef-3262-b408-58f9d13f1ed4 | -12.4113 | -47.5393 | 2025-11-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 276.6 |
| 3c75598e-5abf-3738-a8a1-3acd2bd78ae0 | -9.0327 | -46.0091 | 2025-11-16 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| da085248-2fd0-3c47-8514-480952864004 | -12.3917 | -47.5643 | 2025-11-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7ccc9d8c-eac8-3a4b-a8fb-5d76b9c0ee06 | -10.1722 | -44.5032 | 2025-11-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 362.9 |
| 800f6f70-3849-351b-bfe3-3edd027f6946 | -12.6672 | -47.167 | 2025-11-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 36f8bebd-6fad-3c10-8507-b13a97d7e005 | -1.9886 | -47.3465 | 2025-11-16 14:20:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 90b2c2d3-01d8-30eb-9412-04d0f6c12f69 | -12.853 | -46.462 | 2025-11-16 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| e0e24297-a7af-33e7-95fd-a413bb744a19 | -9.9969 | -44.7797 | 2025-11-16 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 8ad78ac7-4ea3-34db-bc7d-9a4d1552a23a | -8.6808 | -45.5041 | 2025-11-16 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 54313435-145c-3a59-9c80-46da203cd2d2 | -9.0733 | -47.2334 | 2025-11-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 7547874e-2b32-363e-a29a-c12731012ebd | -7.3698 | -43.3117 | 2025-11-16 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f6c6fef6-73a8-3923-8ab5-e7fcc7352c06 | -4.4246 | -43.4038 | 2025-11-16 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 3a7c73ad-cab1-36eb-8a59-bc0d927eff41 | -12.4117 | -47.5169 | 2025-11-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 05924e8b-44c8-3f27-b5a6-e68b8c6ca68a | -10.1055 | -43.9072 | 2025-11-16 14:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| af3b74d8-9a4e-335a-a44c-19e8e26b8fd5 | -6.2763 | -41.7562 | 2025-11-16 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 1ab57241-b9ef-3927-bcf1-5ed7d6acb8d8 | -12.4109 | -47.5616 | 2025-11-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 17d191c1-cd99-39ed-8aaa-e39bff3bfb0f | -3.8437 | -40.7515 | 2025-11-16 14:30:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 07b256ec-e39a-30ad-9011-8bc3e13b1c50 | -12.4117 | -47.5169 | 2025-11-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a12c4216-d74e-3b84-ad7a-c2636c6e23f4 | -8.6647 | -43.8745 | 2025-11-16 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a77be8d5-c649-3a0e-9601-bfbc5b513229 | -10.1912 | -44.5007 | 2025-11-16 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 5614de36-06a7-371f-aaaf-86ee7ea9bb2c | -12.8663 | -46.7771 | 2025-11-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c386723c-4f62-3963-8653-9b15afbd6aec | -9.6562 | -46.0295 | 2025-11-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| a6247ca9-3c34-3b5c-9918-b8ed9a2a7854 | -13.3825 | -44.0607 | 2025-11-16 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 0b8f6e40-d490-3b67-99a2-cf15165771e6 | -12.439 | -48.1577 | 2025-11-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4a99bea9-7baa-3065-9d21-3a893d90c9b4 | -12.4113 | -47.5393 | 2025-11-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 281.8 |
| 04294d81-0a9b-3923-b54c-3e52c55dec1f | -9.9972 | -44.7566 | 2025-11-16 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 96586fc2-11a2-3fde-84f2-6e43b5f7ec39 | -4.3621 | -44.353 | 2025-11-16 14:30:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| eaee0cfc-e0ee-322a-9755-5636960470e9 | -8.1092 | -46.0363 | 2025-11-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 207.6 |
| fc340380-1202-333b-ac97-795df217a61c | -12.8538 | -46.4164 | 2025-11-16 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1ba26549-b0ba-3f39-9de0-0cf7ba53578e | -8.6814 | -45.4587 | 2025-11-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 04d58139-e205-3954-a0e8-c2a866cb0f2a | -9.8305 | -47.0852 | 2025-11-16 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| f7a9dde7-a505-3c28-b9e4-4ef0debafce1 | -9.0327 | -46.0091 | 2025-11-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 163cd354-2521-3879-991b-54bf9b55acc2 | -9.157 | -45.2015 | 2025-11-16 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 520e0e6f-8b6e-3aa3-bd08-9e875bc5063e | -11.4136 | -43.32 | 2025-11-16 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f896c35d-894f-3d64-9597-29e7e6869f42 | -12.853 | -46.462 | 2025-11-16 14:30:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 92ce2018-4c5a-3cad-9769-a25f11f4bb60 | -1.3376 | -49.1459 | 2025-11-16 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 301a529d-721e-3be2-a943-6556d08c6ba4 | -10.1725 | -44.48 | 2025-11-16 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6be68175-f45a-33a7-8acd-474d9e519841 | -4.1528 | -42.1514 | 2025-11-16 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 52fa1c8b-f2ae-33a4-b859-46439d9ebc22 | -8.6811 | -45.4814 | 2025-11-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 455.5 |
| 1e62ac64-ff6f-3edd-bbd5-bd6fea15255a | -12.8722 | -46.459 | 2025-11-16 14:30:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 78803989-7d86-3e9b-8583-20096754d01c | -8.6623 | -45.4834 | 2025-11-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 82137ec3-c265-3a5e-8910-a1b9b7922ee6 | -10.1234 | -49.159 | 2025-11-16 14:30:00 | GOES-19 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 5ef4dd62-2bed-3fbb-8fa8-cb45d5c7e665 | -13.3631 | -44.0641 | 2025-11-16 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| ca22a463-0386-3b1f-87d0-c2b9debae8b6 | -2.5053 | -47.812 | 2025-11-16 14:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 562cafe6-a63a-3826-a65a-7f08386aa4ef | -4.4549 | -41.7996 | 2025-11-16 14:30:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 98a6bef9-dd7a-3b62-af51-36b72fdc50b9 | -12.6672 | -47.167 | 2025-11-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 29e917e2-8d50-3f59-b06a-877651212006 | -12.8534 | -46.4392 | 2025-11-16 14:30:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 03e55652-f248-3685-945f-5618474ec97d | -1.9886 | -47.3465 | 2025-11-16 14:30:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 91bcf779-827c-35b4-9a9b-f1cdefe77ace | -12.3917 | -47.5643 | 2025-11-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0f5333ab-561d-3362-92ae-ff47722793f4 | -12.6933 | -46.7803 | 2025-11-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 26e03ef1-e40d-3505-9101-a60c90fc929c | -12.8727 | -46.4363 | 2025-11-16 14:30:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e2730978-294d-3da3-8118-3e83fe06f7dd | -14.649 | -46.5807 | 2025-11-16 14:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b284f960-2364-399a-b216-cb9ca99e9b44 | -9.0733 | -47.2334 | 2025-11-16 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7ec7afff-a4f4-3878-a2ce-8d61507f41db | -8.7352 | -45.6796 | 2025-11-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| f9014394-be27-3bc0-9059-c1887dfa83cf | -1.3932 | -49.0387 | 2025-11-16 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5e103c6b-62e7-3b9c-8deb-7e4256f828a4 | -14.6494 | -46.5577 | 2025-11-16 14:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 7723c709-a6d3-3d55-97e1-6ad8309764f9 | -12.3921 | -47.5419 | 2025-11-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 2156e37c-f29c-3cc3-88fc-f8fef2f18d3d | -11.7017 | -48.8692 | 2025-11-16 14:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9a790dfa-c1c2-3313-8462-3196dd8ee42a | -8.0903 | -46.0381 | 2025-11-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 32abc61f-af5d-3e50-9827-82146beaa012 | -12.4347 | -43.1793 | 2025-11-16 14:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 69d4847d-069d-375c-a411-d4286c082e0d | -8.5415 | -46.0832 | 2025-11-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 75c24228-fd72-34a6-b7ea-ea6b239b1fb9 | -9.861 | -47.6137 | 2025-11-16 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2c595047-f832-3c24-bb44-2b6c15820b78 | -8.6808 | -45.5041 | 2025-11-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 20bf6da7-51b8-30c5-bae9-a675132a5197 | -9.7242 | -43.98 | 2025-11-16 14:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 240d420f-56fd-374f-97ab-37f540da9b84 | -12.8722 | -46.459 | 2025-11-16 14:40:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 567cbc72-3d5f-3e7f-afdd-0dad6ba3cc5c | -14.649 | -46.5807 | 2025-11-16 14:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a0b2b23c-3f47-35f5-ac61-57822ccbf355 | -4.6799 | -46.9379 | 2025-11-16 14:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 133979d0-18af-3361-ba28-f1e462b497ca | -12.4113 | -47.5393 | 2025-11-16 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 335.3 |
| 848f9c44-acc3-3dcb-b8a4-841252ed2d9c | -8.0903 | -46.0381 | 2025-11-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9c55ba15-30ae-3626-86f5-e713820dd6d5 | -13.3825 | -44.0607 | 2025-11-16 14:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 4ee1cf7b-8ff7-3303-9802-b62d894c3813 | -8.6808 | -45.5041 | 2025-11-16 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 274.8 |
| 48ec7734-41d9-3f89-b9e7-be789d62521f | -10.0159 | -44.7773 | 2025-11-16 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 482776d9-243a-3d29-bc3e-1dca81217499 | -12.6933 | -46.7803 | 2025-11-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 4e87a76e-1412-3789-891b-aa642ecbcc73 | -10.1531 | -44.5057 | 2025-11-16 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| fe208b43-e33f-35ce-a113-0dcc87ffd04e | -10.1234 | -49.159 | 2025-11-16 14:40:00 | GOES-19 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 54ffa355-93f1-3a2a-9eec-6472d8e11c74 | -3.9895 | -44.2813 | 2025-11-16 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| bbc9c9d7-ddc7-3e2e-9125-013475bdadb8 | -3.6701 | -44.7303 | 2025-11-16 14:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| bc4bb284-949f-32c8-a968-febd32e586b7 | -12.4117 | -47.5169 | 2025-11-16 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 953bf177-1d50-3560-9ae0-162945461894 | -2.4201 | -45.7015 | 2025-11-16 14:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| de840b9e-2aa1-3f7a-bc80-0eab1a222297 | -2.5238 | -47.8115 | 2025-11-16 14:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 6fa564d6-edbc-3143-bcb1-d0cb8d71bd64 | -10.8703 | -44.8953 | 2025-11-16 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 157.4 |
| abc1c64c-32f4-3ec0-942d-47d440860eb9 | -6.5411 | -43.4122 | 2025-11-16 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 97784be5-18ee-3ced-a355-5e09e9606ecb | -9.6495 | -43.8961 | 2025-11-16 14:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 2c59f182-b075-3a40-adc9-8632a91d0e00 | -10.8707 | -44.8722 | 2025-11-16 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 55ffa268-7f18-3a6a-a5d6-afc834813616 | -12.8727 | -46.4363 | 2025-11-16 14:40:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| d351bae3-558d-3877-a1f5-7db8d603a624 | -10.1912 | -44.5007 | 2025-11-16 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| bf9dcfeb-7e6f-3454-8d08-daa47f177daf | -13.3631 | -44.0641 | 2025-11-16 14:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| f3c368dd-84a5-3a07-9f34-b0bc2f183f24 | -8.6814 | -45.4587 | 2025-11-16 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| f0597a1e-5d13-3289-9af2-87ea1588bb56 | -7.3823 | -45.5184 | 2025-11-16 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 698783b8-aa1b-37cd-b1bb-2e31e7d5b81c | -3.8437 | -40.7515 | 2025-11-16 14:40:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 40eb31fa-29fc-3ccd-a932-9e1e393172ab | -4.4549 | -41.7996 | 2025-11-16 14:40:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 6f37942b-043f-3f4a-a2a8-fcd50b04b48f | -3.2304 | -43.3486 | 2025-11-16 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| d3456892-671b-3649-8ef2-4245bdebd013 | -9.8305 | -47.0852 | 2025-11-16 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| f0433b78-6c47-3e6c-8984-8952ac48a7a0 | -12.6929 | -46.8029 | 2025-11-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 05d14b00-e73e-3374-8217-29e863835974 | -12.3921 | -47.5419 | 2025-11-16 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 754a8e40-359e-37c7-bd9c-40853ec06f24 | -12.853 | -46.462 | 2025-11-16 14:40:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 521e064c-c561-3ea9-b378-a867aa97ca91 | -11.7017 | -48.8692 | 2025-11-16 14:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| f20606ee-f1e1-3ff1-8d69-fda50d3201a6 | -11.9179 | -46.1907 | 2025-11-16 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 90d60828-6b31-3307-b200-f573b3291a53 | -5.4751 | -40.9796 | 2025-11-16 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.5 |


[Clique aqui para ver as próximas entradas](README72.md)
