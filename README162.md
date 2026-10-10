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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| addc9c7d-de46-3d83-91bd-49aeadeaa851 | -5.7509 | -41.6333 | 2026-10-10 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| c93425ce-8555-3f8b-843f-3b8f1025e40d | -7.4976 | -45.2814 | 2026-10-10 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5f240f35-390b-3ea5-bb22-d5bfcc04255d | -11.987 | -43.4433 | 2026-10-10 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 278.3 |
| f9417fd2-d704-3351-b22e-299b477f253a | -12.8303 | -44.6239 | 2026-10-10 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 455.8 |
| ca113fba-fb8f-3059-afee-729228ffab62 | -11.3633 | -54.0452 | 2026-10-10 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 8ed13114-7865-3876-bcf5-94766158a9fe | -11.0374 | -44.0355 | 2026-10-10 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| c2e2ff4f-7043-3534-ac05-d2ce24ef2512 | -9.9381 | -44.9022 | 2026-10-10 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 295a08af-ad70-3d92-b688-284b3d5ae563 | -12.6873 | -43.0884 | 2026-10-10 14:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 153.6 |
| ae67f46d-e608-3ddf-b7f5-70a0a70691a3 | -12.4837 | -51.2959 | 2026-10-10 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5076a870-8749-3284-9b72-be7911112b34 | -12.211 | -44.8156 | 2026-10-10 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 341.4 |
| a0430ba6-4257-3173-a453-d367268d7009 | -3.1602 | -50.5812 | 2026-10-10 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 5391b3f3-47fd-3889-be8e-8d70209e920e | -4.4976 | -43.6547 | 2026-10-10 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| cb3080b5-6b40-39f0-8d2c-16652d766723 | -11.2083 | -45.217 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 3f64f34c-5158-34c9-8ffa-a88b2dcc0494 | -13.1633 | -54.3798 | 2026-10-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1e6b49c4-a031-3f26-889d-0534048e4087 | -1.6579 | -55.1912 | 2026-10-10 14:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d561508d-c117-3249-8163-ad8dac313a87 | -13.183 | -54.3365 | 2026-10-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 127.9 |
| d0c3bf75-969f-392a-8b64-395ed34dddbf | -5.7507 | -41.6574 | 2026-10-10 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| e7827c65-3071-3709-aece-5f6cf05cb6da | -10.9579 | -45.3661 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| bbd4a15e-5491-3d21-a159-91d48a1075d8 | -17.4775 | -45.0705 | 2026-10-10 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 142.2 |
| e8e7a11d-a1d0-3831-934b-faa3f148946b | -17.4568 | -45.0988 | 2026-10-10 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 08ab6131-f867-3823-91c8-b7601aebf21e | -2.8491 | -49.8763 | 2026-10-10 14:40:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 8a7266b9-5af5-3d10-9b25-c6cf300fc5af | -11.3447 | -54.0264 | 2026-10-10 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d040207e-d043-321e-80ea-fd5e834002db | -11.2064 | -45.3321 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 6309782f-b0b5-3e94-97c5-f138e41a6497 | -11.1876 | -45.3117 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| de033c1c-a864-3274-8e72-8178bf47292e | -1.8986 | -53.9899 | 2026-10-10 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f600bd20-0643-37b7-b954-0d6510e0d71d | -9.1525 | -49.9639 | 2026-10-10 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b3c6ae22-73d6-33bf-aff3-3191cbc6c520 | -11.0379 | -44.012 | 2026-10-10 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 5187bd64-f3db-359f-8104-56713044f64b | -13.3865 | -43.8708 | 2026-10-10 14:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| b1547e30-c5af-3a41-9b12-c2bd5e1c5d9d | -3.3637 | -50.4701 | 2026-10-10 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ec57a354-fd0b-37dd-a6bb-f79470fb881e | -13.1639 | -54.3385 | 2026-10-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 3f6f5297-6d3b-36d0-b107-24aeece1458f | -3.1972 | -50.5592 | 2026-10-10 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c23af62e-1af0-3124-b7bd-e7f9562c113b | -0.9829 | -52.4415 | 2026-10-10 14:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 052a8add-adb0-3ea7-8481-7eb404e8fe25 | -11.8499 | -43.5835 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| aefaed9a-1a7a-376b-9397-615c68fa3207 | -9.5541 | -45.2239 | 2026-10-10 14:40:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 23911949-49a1-3e71-a516-935e2b98a7d5 | -11.4507 | -43.3854 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 9a515cc6-5214-39c0-90b1-e42351810064 | -0.8768 | -48.7246 | 2026-10-10 14:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0fb8d093-9996-39e7-90e1-e326f1cf9a40 | 3.987 | -60.6534 | 2026-10-10 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e3084f0d-7c03-384f-9ea2-414a814fbe1d | -3.1787 | -50.5807 | 2026-10-10 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 75126654-e878-3b6e-a97e-a49b010dd8c3 | -12.4646 | -51.2982 | 2026-10-10 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7c4d01ee-a234-35df-a0fd-e10b2885df11 | -3.5117 | -50.4023 | 2026-10-10 14:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e982984e-99c2-3aaa-a8d2-3eb2c396ef50 | -8.0955 | -45.6094 | 2026-10-10 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 81254842-df9f-353d-841e-2f9e2ce4fc45 | -12.2329 | -44.6728 | 2026-10-10 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 01060000-d62f-3b95-bf63-61959fe1b55f | -10.8909 | -44.8001 | 2026-10-10 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 5197d643-be00-33e4-97fd-739bd6ab9e30 | -11.87 | -43.533 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| ac7f9cdc-0d42-3b7a-83d9-0ab7c51bc3ad | -12.2127 | -44.7224 | 2026-10-10 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| acff85f5-db17-3322-9fe8-43f48a02a172 | -12.1627 | -45.3547 | 2026-10-10 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 006cae10-e883-334e-831b-07559ddd1de8 | -1.3264 | -56.398 | 2026-10-10 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1c11447c-24bf-3d9f-a0cd-24e0949374a0 | -10.9388 | -45.3687 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.6 |
| d29c5260-202a-3deb-86c9-094c3ca6a9ae | -11.8503 | -43.5598 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| db36d236-b4c1-327e-a463-64391fd1d507 | -11.3636 | -54.0246 | 2026-10-10 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e9bee255-c2db-3377-9d7e-6fe40437b9cd | -11.6002 | -43.5989 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 19bf8ac0-fab9-30f1-97ef-d5aa9682e9a1 | -11.3823 | -54.0434 | 2026-10-10 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b9e5262a-a965-3eca-82da-0ea870af6b36 | -2.7613 | -54.0941 | 2026-10-10 14:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9b9216e8-1edc-3837-a92b-f40974455393 | -10.2486 | -49.6851 | 2026-10-10 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| d5e85cc5-c46f-3629-8423-90869077b16f | -9.9384 | -44.8791 | 2026-10-10 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 3325f77a-baf4-308c-9ba4-3e5ec85d7285 | -13.1833 | -54.3158 | 2026-10-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 0bd024b5-2248-3524-aad6-7264ebc23644 | -3.1059 | -50.3105 | 2026-10-10 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 15285321-5f6d-33b0-87ac-6e02388fc04e | -10.9388 | -45.3687 | 2026-10-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 309.0 |
| 7605e591-5b94-354a-b998-85802be768e4 | -13.1644 | -54.2972 | 2026-10-10 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 25a37855-1df3-3898-b8d9-3a742784f5da | -9.1525 | -49.9639 | 2026-10-10 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4dec5741-6fe2-37e9-80a2-b7c8bd4423d3 | -3.1059 | -50.3105 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4497c181-756f-3046-b8ed-43d8d9da463c | 3.9309 | -61.0906 | 2026-10-10 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 37c3b7a3-f249-3c41-8c02-cf973eb0198f | 3.9875 | -60.5014 | 2026-10-10 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2478fe89-3cfb-3772-99ec-3eaaae39a92d | -11.0741 | -44.1237 | 2026-10-10 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 3278a079-de3f-3b4a-9b67-0d8972cf04fa | -15.1088 | -46.9343 | 2026-10-10 14:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 548d0153-c769-392d-92e2-411a04454227 | -12.1733 | -44.775 | 2026-10-10 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 285.1 |
| ae0047c9-3d83-34b8-94a6-49450cde1afd | -3.3923 | -44.4695 | 2026-10-10 14:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| da69229f-a4f2-3195-95ac-21a830c6df1f | -17.4775 | -45.0705 | 2026-10-10 14:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 1b5ed44d-b7b8-346e-bde2-27a555ccfa57 | -12.214 | -44.6524 | 2026-10-10 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 9a9dc983-15e7-33eb-b314-6b8a734bdede | 3.8754 | -61.3187 | 2026-10-10 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 44077ba4-05f1-3d02-ad64-632b92b98a40 | 4.279 | -60.9126 | 2026-10-10 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f38e7c4b-1397-3697-b727-e9ff0c4e9ba3 | -1.6395 | -55.1914 | 2026-10-10 14:50:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| eaaa12aa-ca4b-31af-a3b4-a6d824b7de80 | -2.8712 | -54.192 | 2026-10-10 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f64963c8-af8e-3b16-8d1a-c14114a2d022 | -12.2329 | -44.6728 | 2026-10-10 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0c455718-f662-356e-a46a-ef16959ec0d0 | -1.3264 | -56.398 | 2026-10-10 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 8efd1f03-9075-3a21-a027-555da5175dd1 | -3.1787 | -50.5597 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2be163d0-ee79-3853-8e0a-16674076345f | -15.4029 | -41.8985 | 2026-10-10 14:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.3 |
| ae0273df-1a33-366d-97c2-def7231b3a8d | -12.1541 | -44.778 | 2026-10-10 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9e40865b-463a-39e5-9494-ebf1891a165a | -3.2532 | -50.4108 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 172.0 |
| cb02ba54-f1f4-3179-b099-0ecd013d4e5b | -11.3633 | -54.0452 | 2026-10-10 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 36bbad12-70ee-3e58-9fbd-e57b3bd053f7 | -3.0375 | -53.8865 | 2026-10-10 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 4aca73f8-98ea-3fa8-b024-4d22d14b971b | -3.0008 | -53.8874 | 2026-10-10 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f09efd13-171c-3c59-ad04-957e5132cb87 | -15.0713 | -41.7982 | 2026-10-10 14:50:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 106.6 |
| 68336580-0b95-35f6-b966-24babd0a8a5b | -15.0516 | -41.8024 | 2026-10-10 14:50:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.3 |
| 3d6867ca-837f-3183-800b-6e71313d7ba5 | -11.0933 | -44.1209 | 2026-10-10 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 797.1 |
| b6fc8042-653b-3f23-97a9-cb7e8fbe9714 | -17.4581 | -45.0511 | 2026-10-10 14:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 56724c20-8120-3028-93af-c6c9ff1c05b8 | -3.2533 | -50.3899 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 612284a9-30c3-3185-a2a4-217c641f7a6c | -1.2723 | -55.7494 | 2026-10-10 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 90b51975-4c2d-3967-afad-c3b5065f8195 | -2.7613 | -54.0941 | 2026-10-10 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 86658c3c-4159-354d-8956-2f22c09d21a8 | -10.9197 | -45.3712 | 2026-10-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 0d8cee23-bb76-35e3-b8a1-09b344f39415 | -3.1061 | -50.2686 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| be0cb14c-a211-343b-b993-6ad9676587ed | -1.2175 | -55.6512 | 2026-10-10 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 324ac2c0-2ce9-3d5f-a0fe-5fc3af11bb37 | -3.1973 | -50.5382 | 2026-10-10 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c67d9337-cd52-3352-8c06-a1aaf855259d | -9.1257 | -67.8322 | 2026-10-10 14:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 13b603c5-c352-315a-83a8-348fa493686d | -11.9668 | -43.4939 | 2026-10-10 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| fc6da71f-f4ce-344f-8da1-6414e3c62d0d | -13.1047 | -46.3778 | 2026-10-10 14:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 139.3 |
| ca601a2f-5b20-354e-8851-a989710a9b88 | -11.9476 | -43.497 | 2026-10-10 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 22285efe-e6d1-315a-b982-3eba3df89fcc | 4.2789 | -60.9316 | 2026-10-10 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0b33da51-f3c9-3d32-8b8f-882c07376039 | -3.1285 | -54.1657 | 2026-10-10 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d83669ec-7506-3a5c-b458-60d1992b0fd8 | -1.6395 | -55.2113 | 2026-10-10 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |


[Clique aqui para ver as próximas entradas](README163.md)
