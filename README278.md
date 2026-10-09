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

## Dados Diários - Página 278

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14332ed4-86c2-3bc3-9e0f-fdbe60868963 | -8.53078 | -46.88998 | 2026-10-09 16:01:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5d8d484e-999b-3ffa-b015-a08e04ba9498 | -7.48733 | -42.84433 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 04f825d9-2d63-3bed-a672-ba67cb519dee | -9.89317 | -44.79412 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| ecb2939b-a97c-3351-983b-9d5019564b40 | -10.35208 | -46.55497 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bba652fa-7ebc-3394-a659-a28a73830ea4 | -10.28731 | -39.48926 | 2026-10-09 16:01:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 470f0355-07f0-3210-8788-9ad755c81ef2 | -9.34177 | -46.46275 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d6490bcf-de8c-3159-b510-15e92c5ba0e0 | -10.83892 | -47.34333 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 40d69fae-9ad9-3e7d-be38-1f8de8fd83b6 | -5.1542 | -39.5048 | 2026-10-09 16:01:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d1cedeef-f174-347d-99b0-d1d8ff589ffb | -11.06069 | -44.11656 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 0d852856-5709-334f-99d6-6541e7122126 | -11.09357 | -44.04419 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 214f0c52-f8c5-3480-8c2a-12ac838cb99e | -4.57981 | -40.66557 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 2f131ae3-17a2-396e-98fc-085e85dd9fb1 | -5.75922 | -41.64161 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8cbeac0f-5fa4-313f-9ea3-c5d1b1bf9c5f | -9.98853 | -45.93915 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 25614d25-45e0-32f6-b2c6-64902ffad51c | -11.24999 | -46.33371 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 25c35866-838e-36b2-af75-a82019d4b16c | -11.05101 | -44.03647 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 47dbcb0f-1924-3c28-9b2a-64bc716d76f2 | -11.4983 | -47.60642 | 2026-10-09 16:01:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 42ede8a0-2b9e-3701-8ad1-6ced056d9ba7 | -11.11446 | -45.68306 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 01608b6b-1e45-3746-abdf-4ad506766cc5 | -9.85974 | -44.87284 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 32cd46c8-81c2-3ab1-a1bb-05b305dd896b | -7.07345 | -41.60193 | 2026-10-09 16:01:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 77c9c730-52d1-3fb5-b14f-8eee03368650 | -4.7353 | -39.39208 | 2026-10-09 16:01:00 | NPP-375 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8b3882cc-fdb2-36cc-83ed-98fb3133c3d3 | -7.06877 | -41.60265 | 2026-10-09 16:01:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| e06f3b2d-cf49-3c8b-b975-644a574c64b8 | -7.24841 | -43.74077 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56b31fd8-c20d-3318-a6d9-56baf5a76a2e | -7.43176 | -35.08969 | 2026-10-09 16:01:00 | NPP-375 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 325f1e68-58dd-3222-82f6-d044790be36a | -5.62501 | -43.64653 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 155f22b0-c09d-3a23-8982-b69bd57c3871 | -5.51759 | -42.82937 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a14be56e-e9b5-3078-8266-804ebc80a6af | -5.49658 | -40.54863 | 2026-10-09 16:01:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 6696952b-f3ea-39b3-a28d-8bc35340f8cf | -7.47743 | -42.8486 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 388a66be-eb7e-3d73-874f-24077ef5fc07 | -5.53081 | -39.85134 | 2026-10-09 16:01:00 | NPP-375 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9e54c9ae-39f3-3575-859c-946b9aa3974f | -9.84259 | -44.78235 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f5cc9600-a3e3-32cf-a463-f71c92224542 | -10.48606 | -47.3421 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 351a4fc7-b4db-3638-ba83-7d431c0758fb | -7.30214 | -44.01058 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61a485d7-ff68-3544-b0d4-489bafe88f35 | -9.94261 | -43.55044 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6c30ea98-f3de-329d-8f18-cfeb55be2870 | -7.19379 | -44.27785 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6e4765e-4978-30a5-9b3c-8283b5d5160b | -10.47119 | -47.25286 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 6eed5ff4-bf09-383f-b621-1b6f338ddc11 | -6.00369 | -40.95601 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9cec1308-05f6-38ba-95ba-99d9df3c62f8 | -11.28897 | -45.20135 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 443537c5-6d3d-38d5-95f7-4dde53b5ff2d | -10.83966 | -47.35019 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bcf44dbb-b433-37ed-9c8d-458a47fcb780 | -5.12581 | -42.9778 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2a59bff2-45e1-3d0a-9bfb-2dd44b920ce2 | -10.49161 | -47.32766 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e2a7daeb-1ded-39b3-8ae1-8c001589e459 | -7.28833 | -35.87838 | 2026-10-09 16:01:00 | NPP-375 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 62d976ff-6a07-35f6-9bea-250cd354f3bc | -5.75004 | -42.08684 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 4fe44b2f-980b-3c80-8682-131892e2821a | -7.29226 | -44.01631 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| f93f946c-9452-385d-90f5-3cfdeedf3260 | -10.40351 | -42.57577 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5f22074e-a426-38f2-9ceb-8f4ccc63c056 | -9.93041 | -45.73588 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6ce60fb5-b89c-3652-acb5-a6afda00f4e4 | -9.92099 | -44.86877 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a19b2e7a-2907-33ef-81c7-7814d085f903 | -11.15473 | -47.30649 | 2026-10-09 16:01:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d0235e3c-5e78-3c9e-a670-676c9c5fa3a7 | -11.20722 | -44.87769 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b852071a-8355-3a14-9b9f-db1ef9ff2a9b | -9.01492 | -45.12699 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| cf898332-6174-35eb-8e64-c3b435fed25c | -6.96239 | -43.85881 | 2026-10-09 16:01:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4631ba77-c7f1-3359-9241-7f05494415b5 | -11.08202 | -43.99877 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d0be0062-790e-3aee-bb08-74e8c2aee7cb | -8.18721 | -45.80251 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bc537633-ccbd-3808-8d4d-4a2229429a5b | -11.09888 | -45.66303 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c3782ffd-d14c-37dd-92d9-2ae2a0890710 | -9.54815 | -46.84711 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 84a1aff4-9654-354e-ad5c-9e02b17c6dc1 | -5.95236 | -40.94057 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 313.4 |
| 72e49615-9f20-36f7-b058-879665c2b55a | -10.89373 | -45.53323 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3a31431-d4db-3030-8295-f75eddcb3c5e | -6.00774 | -40.98102 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 27f6cc66-5260-3c12-b6ad-7e51c16f498c | -5.8485 | -42.6833 | 2026-10-09 16:01:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3dc39ded-2865-30ec-b54e-5f56fe3e4bcf | -6.94835 | -43.66951 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e0d46fde-e0ff-3a3b-98ad-357489b0832b | -9.93224 | -44.79958 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 92acc792-9ff8-349c-97be-a6406684fb77 | -9.41416 | -45.98198 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6af05758-9ef6-3fed-9fce-ba571c7f5db7 | -6.59287 | -44.29929 | 2026-10-09 16:01:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08f720a2-1e51-3fb6-99bd-66052d6e4f1f | -9.54882 | -45.22648 | 2026-10-09 16:01:00 | NPP-375 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a04dd13a-d8d4-3d3e-a9e9-6626150f3599 | -5.416 | -39.10702 | 2026-10-09 16:01:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2b148e22-d496-3207-8ae0-5a6f17497130 | -9.92676 | -44.80515 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c5d65877-5949-3b90-a384-d8944d1c4af8 | -7.01542 | -45.30958 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| da9d8bb5-9786-3604-a8fc-5c3acf64144b | -8.15353 | -40.50485 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9c077f41-878d-3d8f-847f-f9ab72fbeea1 | -10.50817 | -47.34637 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bfba00ba-5277-377f-ab4c-dfb7cbcf8202 | -10.89492 | -44.8069 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| e338f1a3-2a71-319c-bab6-6c10e7adf532 | -11.06504 | -44.10317 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 8e360fe7-1d27-308c-9e40-e0b88d0f6a72 | -8.84065 | -45.42819 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 090bb502-8f90-3b04-8bd8-0b37441f674c | -9.83703 | -44.7871 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f810c3a3-38a2-3595-a305-db5e1d4ab186 | -6.57772 | -43.05861 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06952fc8-7022-3e86-94e3-bfc18f3fa519 | -8.93006 | -45.14503 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d6e63c77-5a6d-3aae-9aca-0fb7d0d8fd5e | -6.04867 | -42.5846 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 290d4c5f-b2d2-36bb-b40e-fe0361d837a8 | -9.5432 | -46.85242 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 9c0353d6-517a-31f9-a2dc-8435f1fe1704 | -7.82307 | -44.56781 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1be4fc1b-9b60-344d-86fc-92bbe36fce37 | -5.41488 | -39.10455 | 2026-10-09 16:01:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5dbdcef7-455c-3cf6-a6f4-7c3c0653626f | -9.86693 | -44.88119 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| a50401f8-f862-3bed-9608-1cea899736dc | -5.12598 | -42.97393 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 23ef3369-714f-384e-9c10-63b2d844a839 | -11.22185 | -45.31118 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 29def1fc-9d12-3f85-8fe7-e15bc0e4b09a | -9.91364 | -45.70555 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b126d4aa-4bee-3153-9bba-401254645f6f | -9.4865 | -45.55813 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56967690-f48d-3814-9815-0e7a84c46754 | -6.37473 | -38.25998 | 2026-10-09 16:01:00 | NPP-375 | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 88bdddb9-5cc7-3e7c-8fee-cf8780c4099c | -9.52964 | -43.15516 | 2026-10-09 16:01:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1d42e00e-ffb0-3b73-af00-3393affc3017 | -11.22755 | -45.30487 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 567aef79-4293-3880-824c-395363c7ebcb | -6.02185 | -42.44542 | 2026-10-09 16:01:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 88530d2e-192a-32a4-aa7b-d09e25eaf813 | -8.40194 | -36.68137 | 2026-10-09 16:01:00 | NPP-375 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b7a89aaa-e145-3057-ad7f-e2ee6b3e28a4 | -11.07298 | -44.1194 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 400.7 |
| 72728a13-6d94-33d6-945d-34d865fa9147 | -7.39364 | -44.75101 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b83dabec-c6e3-31ef-9a96-a3d0c5cf9ea8 | -11.22058 | -45.30043 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9a5f0f0e-85a8-3a9f-b85c-0e4eda4b53fe | -8.32292 | -44.20255 | 2026-10-09 16:01:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4307271a-1f40-30ba-bf7d-4091ec109789 | -5.52003 | -43.06009 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 129a786d-c4b2-3657-9bd0-15d9b193cfcd | -5.99154 | -41.37706 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 766c1a05-4a34-3782-b47b-c2e8ee119ed3 | -7.04121 | -42.30002 | 2026-10-09 16:01:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f529314c-2b2d-39b6-83f0-02e6af5fb814 | -10.40233 | -42.57444 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8b0be703-e219-34dd-ac77-ef1fc3816fcb | -5.61972 | -43.64725 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec13c31a-e4b6-32c6-89ee-cf29365115fc | -5.36782 | -43.19927 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0da4446-ef68-39e3-bfc2-90c8f848443e | -7.47064 | -42.83702 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| cf7df54d-27da-340c-807f-a05ef5b95a40 | -6.04649 | -35.24633 | 2026-10-09 16:01:00 | NPP-375 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f2fd5f7f-43e9-389a-b168-314dc1ae904d | -7.07183 | -43.50944 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README279.md)
