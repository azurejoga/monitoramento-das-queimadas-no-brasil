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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f8f5226-21e2-3b20-bf9d-725c0fe1b3ca | -17.61959 | -57.55508 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bc363dba-8ce9-32fa-98a8-a7792c285488 | -17.57725 | -57.58104 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 47134e24-a6c5-3743-9d28-4e1aeb4cf482 | -17.06615 | -57.41681 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8178ed94-9837-33a9-a32a-3e12e0198cde | -17.57591 | -57.44217 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d91d8bc6-3d89-3b6c-9ffb-66a8e58aed6d | -17.81117 | -57.54998 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7b9c0e87-05a2-3de0-baf0-5d459000bdbc | -17.23849 | -57.45313 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| b36b154c-194c-3478-b17c-bdead8fba819 | -17.57013 | -57.54959 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3be6e358-9d99-34a9-89b8-0b4e340e654b | -17.56147 | -57.43577 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8bbdf2fa-6275-3023-bf17-45eb42612fd3 | -16.10358 | -60.09718 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21219fa8-f174-3d66-aca9-42229b375ebf | -15.89833 | -59.26692 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9a702b17-0ac1-3189-93d0-6dbb1837beba | -17.55181 | -57.53576 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 02e09b99-8838-3687-a1b1-9b46f5da391c | -15.90911 | -59.26837 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3fd97810-72d8-3096-92d6-0b96b70ab05a | -17.6681 | -57.54997 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8e7366ec-173b-30ec-8783-f88032348b23 | -17.61455 | -57.55393 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 67c74550-f651-3080-947b-67b0ea561257 | -17.62906 | -57.56043 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 28b304c1-4304-3af9-b44b-5ce876ac45c2 | -17.56526 | -57.44296 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1da5348e-cc45-345e-be36-8938fcc68ec8 | -17.55305 | -57.5296 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 0be0213b-acbd-3533-9f28-76e9172e7861 | -17.82793 | -54.54522 | 2024-11-16 04:27:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36bc4cbd-75d1-38f6-ad98-a34e831c2817 | -16.01919 | -59.37136 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a308dde7-ad6e-3aac-957e-d4c0f5143533 | -17.56967 | -57.44711 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 032e68a5-ff9f-3c92-b8e8-a9f9b0c08c04 | -15.91566 | -59.26614 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e609eb35-6871-3cf6-86ab-3beb0da2874b | -17.57973 | -57.58086 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 034fa588-7344-3840-a98f-9a3e39253f78 | -17.2289 | -57.19277 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3439b46a-e766-33c7-99a2-e2c049b3636e | -17.64608 | -57.55462 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| ac38b66e-1121-3eea-8a50-070087967068 | -17.56588 | -57.43993 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3afc10e6-ff18-3a78-a588-f863a95cfb68 | -17.67437 | -57.54498 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4d184fe7-b69c-3380-9e71-f9489d8c6a4c | -17.55933 | -57.5246 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 6fe6bc3d-a38e-34a1-b877-b00278dfe873 | -17.57789 | -57.57795 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| bd12cc41-f1f4-3188-842c-0573dc6faa0f | -17.57801 | -57.48402 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5eaa7fc1-9b3f-32a9-a6fa-56b2ff7e5279 | -17.23406 | -57.44892 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7cd3d12f-ea76-37cc-9dce-7fde1b4a2926 | -17.63474 | -57.55848 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 6bded6d3-52e2-377d-9059-aeb82686a3c4 | -17.55243 | -57.53268 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| cf7eeafd-b9a1-3d42-b0ab-c00ae655e804 | -18.02794 | -57.35002 | 2024-11-16 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2855e671-00f4-313f-aeb9-bebe1aa71a62 | -17.57469 | -57.44822 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1d6ee8ca-4b4f-321b-84b5-6c5163666b5f | -16.09647 | -60.10057 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9768174c-9acc-32cb-95ed-166a76890c8f | -17.62843 | -57.56351 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 50b4ca35-3526-3668-bad6-b7c9e6b14453 | -17.58344 | -57.56231 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f5b0bdc6-4f62-306a-ad2d-138290f7640b | -17.58562 | -57.48973 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c5e415ab-692b-35c7-a593-f74224fba6ed | -15.9041 | -59.26841 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 19125b80-628a-3fef-8812-72e33e7c885d | -16.92399 | -57.54155 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8c7ff93f-f126-3b05-8e90-4be90019b8cd | -16.01514 | -59.37157 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e324818-5793-3bd3-9659-0545a914f29c | -17.64958 | -57.4596 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c35b2a1a-3bf7-3dea-bd37-c383dbff355b | -17.70333 | -54.08726 | 2024-11-16 04:27:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c4a162c-1230-3558-83fd-d12265a3d2a4 | -17.65926 | -57.54154 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 631ddc98-8f78-3df0-aaca-1e47124a824a | -17.68384 | -57.55032 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 87a4ea5d-78e6-35f3-83f4-579a605aa588 | -17.58745 | -57.48935 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ec6ca353-61b4-3573-a345-a3479bc0084e | -17.62086 | -57.54891 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 427dde74-da9c-31bd-9166-901544390928 | -17.24416 | -57.45118 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 37a04bf7-6733-3d22-8b0b-6151177968c7 | -17.57543 | -57.47068 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a202d592-15f7-3ec4-b049-43ab8a0fa9ab | -17.23663 | -57.46235 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a4d85d75-92e0-3e71-8296-895479215799 | -17.63222 | -57.57085 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c3c12f89-ff47-3ccd-a7fa-da530e105b28 | -17.23282 | -57.45508 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 4d06c3c1-8100-31a5-b3ad-2b93cd26679c | -17.58166 | -57.58529 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 3c417bac-20a5-34a1-b5f8-0dc036a47770 | -17.66306 | -57.54882 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 65c589c2-c124-3d9a-8828-47187d99bb0b | -17.5785 | -57.58707 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| f34e5858-35b8-395e-aa53-cee4717c3d8a | -17.63894 | -57.46038 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0f3f00b8-1a30-3931-a920-0d86eaad3df3 | -17.58059 | -57.49739 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ba5079af-554b-3a14-9cea-86300b0c2d47 | -17.56314 | -57.53189 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8005d84d-3d7e-3adb-91f6-43465bf8c3ff | -17.56712 | -57.57881 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cdad1249-a0a0-3e97-a29c-199271bac140 | -17.58991 | -57.57099 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 448d9241-556f-3289-bf5d-a6eeb1545ab5 | -17.58613 | -57.56367 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7be6c8ca-74f0-313a-b3e8-12a852a10eae | -17.5905 | -57.4741 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0fe1d018-4cb6-3890-a72c-b7434e65b22d | -17.59496 | -57.57214 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| df7b237c-5cbb-3b2a-820d-ac142deaa8f1 | -17.6429 | -57.54425 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2d8a190c-d3ed-3e36-b049-68a63d342065 | -17.55685 | -57.5369 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 080c2a95-234d-312f-8122-0a5a5ad381cd | -17.56128 | -57.54112 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7379a399-0340-3c62-9933-b8db0b4adf23 | -17.56517 | -57.57436 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cee52fe9-2f28-3311-944a-0516d7b68902 | -17.57271 | -57.56309 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f860840c-122f-3a36-8248-778368dcbd80 | -17.5729 | -57.55102 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8b844d78-3012-3a15-a6c1-fbc3ed14b424 | -17.64897 | -57.46264 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 01372284-e743-3457-8cf8-5cbeeaf43bc7 | -17.56323 | -57.55772 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7870fed7-0a7b-3dd2-83e5-84a0d59a481b | -17.56649 | -57.43689 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5dd917e2-3a01-3c64-a167-0c2dc686c0e7 | -17.22948 | -57.18782 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e56573cf-c9ec-32cc-b00d-5aa3003eff72 | -19.00642 | -52.39542 | 2024-11-16 04:27:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a2c7fb3-63df-3ea4-a7a7-a8284fe1d603 | -17.57188 | -57.51461 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c0bc3069-b7af-3c36-8672-9d9a1bb732df | -17.55871 | -57.52767 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 758a9c98-14a6-32ea-9543-f87b17cb5d74 | -17.5671 | -57.43387 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 70c18545-d494-3ccb-9bbe-c9db3c07d415 | -16.02019 | -59.37665 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1fd29784-bec0-3d43-b3f1-48fbab43a62d | -16.03704 | -59.40217 | 2024-11-16 04:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1188569-2fe9-3100-a5a9-5def129c0c59 | -17.58877 | -57.47453 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 893d875d-bb97-3a5f-88dd-08c3816101c5 | -17.64642 | -57.44939 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 364230e1-8fb4-33ee-b9e1-c861ab32a451 | -17.80928 | -57.55914 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 512727bb-5a20-3903-ab80-ec4b5df786f2 | -17.66687 | -57.55611 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cb06d953-2013-344e-8298-750b77f7ba0b | -17.59241 | -57.58448 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 5ab44aa3-22c6-3cbe-9e3e-bc07bfba99fe | -17.57023 | -57.57549 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 18abbcef-3e75-3771-953a-065dd8918d73 | -15.9106 | -59.26634 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b3b66b39-9893-3ddb-bc96-ba7666eac765 | -16.01825 | -59.37574 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e928af64-8fc3-3b2d-8255-84a9baab79fb | -17.56074 | -57.57012 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0f55884b-e684-35e4-a7ac-6da5ac4aba21 | -17.55367 | -57.52652 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 304f87ac-157d-385e-9c8c-4370592f308d | -17.68888 | -57.55146 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 88383679-69c5-3e55-907c-80fe26276451 | -17.56375 | -57.52882 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e4ec9a0c-f064-3148-b37e-b18c7b2948d6 | -17.5753 | -57.4452 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7db99a7a-c80c-3af4-b9d8-40214b3bb24e | -17.58927 | -57.57407 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.3 |
| d1082416-f801-31e2-837a-c80730681c0f | -17.64483 | -57.56078 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 2da34aae-a940-34d3-95d7-a5e8adc5d7be | -17.69143 | -57.57806 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 2608348a-4a1f-37e5-bfef-7f422612d443 | -17.64165 | -57.5504 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 168a55f3-d376-354c-91f8-77d58eb37e57 | -17.64228 | -57.54733 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e5ed65bc-c80b-317c-99e9-25de106261ac | -17.23725 | -57.45928 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0cee35ce-06c4-3f87-92ee-239ab2a1e001 | -17.58731 | -57.46378 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 11357194-551f-3a13-a74a-74f93b9b44d1 | -16.03213 | -59.39654 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README40.md)
