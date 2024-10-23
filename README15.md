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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 150bb0bd-782c-3d1c-9467-af2ec834c801 | -4.65983 | -46.19783 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed304e01-ff82-332c-a92c-5cd92de82ae8 | -4.58735 | -45.78106 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a0664ad-cbf1-33ff-8931-b7eaee465974 | -4.47677 | -45.48004 | 2024-10-23 03:34:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb2549bf-209c-3526-8298-dbb1ee14de31 | -4.47551 | -45.48712 | 2024-10-23 03:34:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1456e571-d861-3c1d-852e-818f77331c68 | -4.14883 | -45.60768 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d85989a-a064-3086-8bca-8db7c576f581 | -4.14778 | -45.61362 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 778428d0-7fa8-36ce-a304-67939c3bc8df | -4.14629 | -45.58307 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4988ba6f-71d6-33c9-b1bf-6087f5b39907 | -4.14524 | -45.58898 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7810d088-5dc0-32fe-92e6-6dce980e0788 | -4.14423 | -45.59473 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 440e2098-3bde-385d-9938-dbcdbd655862 | -4.14321 | -45.60053 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d4484cce-390a-3c93-a829-6996b8d816b0 | -4.14218 | -45.60638 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25b00ccd-4206-3cc8-a712-027e00015015 | -4.14113 | -45.61232 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7351cfb2-a9de-3e28-bd6d-f4fb0c815d41 | -4.14066 | -45.57606 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f537eccf-0e17-3208-8b1e-ca218a8f08e5 | -4.14008 | -45.61827 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 120dc691-c599-3ad7-a241-89e09d34c00e | -4.13962 | -45.5819 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 407ba3a2-5e38-380f-a81d-d84b966fdfca | -4.13904 | -45.62416 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f09ddbfd-d4f7-365b-8819-5a36d894f188 | -4.13858 | -45.58781 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1a7c307b-2202-3761-9127-ddbff28a1383 | -4.138 | -45.63005 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55352b8e-b431-3be5-aead-0f418eff5af2 | -4.13756 | -45.5936 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 226.2 |
| 7e89cf34-cba9-36b0-8968-bf294096caa7 | -4.13696 | -45.63596 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 545d0a62-5194-38f0-962d-5bdb1208ee34 | -4.13653 | -45.5994 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 226.2 |
| 1847f22a-b6c2-3f47-bd1d-59d8f6e7bc72 | -4.1355 | -45.60523 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b46b5033-98ac-32a8-915c-1b72a3d254a7 | -4.13501 | -45.56918 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba8c2a69-7b8b-3aa4-9fac-6440ad515ccb | -4.13446 | -45.61113 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 09011df3-87fb-320c-8194-6acaa705880a | -4.13399 | -45.57494 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 089787b9-eaf7-3c81-8399-9a775469eca5 | -4.13342 | -45.617 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1d58a158-cdeb-3b56-8752-d034014ab574 | -4.13296 | -45.58075 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 166466bc-100a-3c1b-b54b-d2b24c712c2f | -4.13238 | -45.62288 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3e48ce46-e209-39ad-bd5f-5c300de9b1a3 | -4.13192 | -45.58663 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6dd8e80b-5b34-31f8-8ab7-ed3e56dd6efe | -4.13135 | -45.62873 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9db7e7f2-65fe-30bd-9224-7d9ca092013c | -4.13104 | -45.5747 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fb05bf16-b72b-3d92-8b39-3b5451f821ce | -4.1303 | -45.63466 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21dedabf-8ae2-3ae5-af56-4f1bec3867f7 | -4.13005 | -45.58049 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f7e81203-8b5b-3c90-90d0-e3d21190778a | -4.12984 | -45.59833 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 226.2 |
| c5d9059e-2e84-3414-8afb-4e5553f18b5c | -4.12925 | -45.64059 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adb006ed-c828-3e62-ba98-e6784090056f | -4.12904 | -45.5864 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 102.7 |
| e27178ea-ab53-367f-9eca-9cf0f847053a | -4.12882 | -45.6041 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| fad33b12-7a12-3f0c-9634-95b3a7dbca93 | -4.12779 | -45.60994 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 600c9899-0500-390c-ba66-a7f4668cfb84 | -4.12733 | -45.57379 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38ce94f1-1d32-38bb-82f8-d02acd466bc5 | -4.12705 | -45.5981 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 5fac0ec3-fd18-3de2-8be7-aa12dbb33ddc | -4.12674 | -45.61583 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 328dca98-46a6-3e88-8498-d26922d5000d | -4.1263 | -45.57955 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6fe237e8-b85f-32d0-8c9c-44ae5e4c26fc | -4.12605 | -45.60394 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 5c11fcf4-ce96-31f7-a597-bb73129ae79f | -4.12569 | -45.62176 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c9dc79bc-3455-3e32-b4c7-a053ca189376 | -4.12527 | -45.58539 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2ad73619-b228-3fc4-9d29-a749be3450fe | -4.12506 | -45.60978 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4f6bd6e9-012f-3927-bbcc-caf38ca8420a | -4.12467 | -45.62756 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f268389-b4d6-3c04-bdb7-e8e296f80e2d | -4.12439 | -45.57346 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c9ded463-544f-375f-9f8f-584fd160cd4a | -4.12422 | -45.59125 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 19775149-6e1b-3d92-964b-17132de79132 | -4.12405 | -45.61569 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 83c2dd43-e740-37b2-84d4-c52d1bf3c619 | -4.1234 | -45.57922 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b3810f5f-f8bd-3b77-b6f0-15806ce97586 | -4.12318 | -45.59712 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5848dbbd-3be2-3be2-9daa-1595ceca681f | -4.12304 | -45.62165 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae88d9d9-a5f3-3544-a369-1942d61a1048 | -4.1224 | -45.58509 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 102.7 |
| a4f86669-e521-3e63-9d63-cdce318b92b4 | -4.12214 | -45.603 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6d345616-b063-39d7-8eec-042cd304fab3 | -4.12204 | -45.62747 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b65b14c-c228-30e1-a2ed-87318cfd6546 | -4.1214 | -45.59095 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 83663444-e616-394c-8720-a04b54209919 | -4.12109 | -45.60888 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fbc2282d-df72-37fe-b79d-334a1b196a62 | -4.12039 | -45.59685 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3f2c6960-ea41-3282-a5cd-280e383902cd | -4.12005 | -45.61475 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5929b55-9838-3c61-ad6a-5931945b8fb8 | -4.11966 | -45.57828 | 2024-10-23 03:34:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa00046e-3d53-3403-bb62-dfff98c34ee1 | -4.11937 | -45.60279 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 611a22d8-3ec6-3f18-bd36-9d61ce8d80ec | -4.119 | -45.62066 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31ca62cb-ebd0-30db-acf2-8ab7fb4a7dd2 | -4.11861 | -45.58415 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9581ff7-9f35-33f3-9764-ef3793b78c4d | -4.11837 | -45.60868 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1150cf27-1c68-3a9a-b743-146aa3af4b36 | -4.11797 | -45.62648 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d440583a-e0a1-3b4c-bce0-1e14e85fb684 | -4.11757 | -45.59004 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d3a193bf-57e6-3117-aaae-7f1d15867a55 | -4.11737 | -45.61456 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8709b05-46d2-3f98-babb-80c5c6b66812 | -4.11651 | -45.59597 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a7d8a417-7f88-3ad5-946e-c5756fed9d13 | -4.11636 | -45.62044 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92f14cfb-52f7-3111-bf89-a90492f3ebfd | -4.11574 | -45.58385 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dba3584-9d13-30e0-b2ef-aeabd88b7adf | -4.11546 | -45.60187 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9a9092c1-df70-3633-a084-ebd01f0d76d2 | -4.11473 | -45.58976 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44f24b53-87d5-33df-98ab-7197a966f843 | -4.11441 | -45.60776 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d201595c-6f3b-3bf9-abff-7351fb169363 | -4.11371 | -45.59575 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37c6cca9-1457-33b3-a747-5abfcf21aae1 | -4.11337 | -45.61362 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 298dabbb-c8ce-3734-bdae-278727e69b5d | -4.1127 | -45.60164 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cb4b9c4-bccd-34ab-9ae8-1674ba5a7e75 | -4.11169 | -45.60752 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b11b7c5f-eb8a-3b98-8d39-3eab8f2a5021 | -4.00659 | -46.01447 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79aff735-581b-3537-ad84-ce6e85172f57 | -4.00653 | -46.01504 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6584035-4b03-3f1d-a7cf-d68e52fdf122 | -4.00557 | -46.02013 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 800cf59a-071e-323c-b89d-40daeedf2475 | -4.00553 | -46.02073 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 711fc3e6-a136-3eea-bd7c-6f621cdecb87 | -3.99984 | -46.01277 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca576ab4-6062-32e9-b1d4-b098a77aa5f1 | -3.99976 | -46.01334 | 2024-10-23 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14a1b036-db9c-3f8f-8008-9ae59406b357 | -5.76022 | -45.55984 | 2024-10-23 03:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43a8594d-c8c9-3bb4-8e38-860886c8f9c4 | -5.75922 | -45.5654 | 2024-10-23 03:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fb2ff2e-3f9a-3be4-9782-6807b7126d69 | -5.70865 | -45.00031 | 2024-10-23 03:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0af39337-e201-3e5f-9619-0262c1e02319 | -5.7024 | -44.99902 | 2024-10-23 03:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 891d0e54-7ee2-3caa-9dc6-6acf8d69bf17 | -5.3668 | -45.08377 | 2024-10-23 03:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0de89b67-7644-3608-bd1d-054f1dc82f4f | -5.36582 | -45.08917 | 2024-10-23 03:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08fb0453-3989-35ce-95cb-94f1df786b3c | -5.36502 | -45.08144 | 2024-10-23 03:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 448572ff-0aaa-343b-8a52-e285ab6b856d | -5.36406 | -45.0869 | 2024-10-23 03:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 52338bf0-ad0a-3dce-b468-9a29b40075a5 | -5.36046 | -45.08258 | 2024-10-23 03:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 808a624d-e222-3091-bc89-19438e553082 | -3.28795 | -46.08051 | 2024-10-23 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4be83bba-4d3e-353a-a459-8196f9b550bd | -3.28217 | -46.07938 | 2024-10-23 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77b8b458-44cc-382c-aafd-f71e12d11c50 | -3.281 | -46.07937 | 2024-10-23 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eac4b68-dcb4-3e29-aa2f-17d99a1ba4cd | -2.28662 | -46.43652 | 2024-10-23 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c509977e-e8c3-3c95-add2-d6e7575c61be | -2.28549 | -46.44338 | 2024-10-23 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc788a4e-4095-3178-a08f-115d7ff0e846 | -4.76608 | -46.6228 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| adec5926-9298-3e99-980a-95a71c29f735 | -4.76482 | -46.62971 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README16.md)
