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
| ecbd8de5-a4ac-3272-a0f5-640064b45b55 | -14.4445 | -45.200199 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b9e76f0-b6e4-3b7e-9c44-86a13b68c3f1 | -14.4478 | -45.213501 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30d22415-3b6f-3419-a740-fe4756ad0404 | -14.4512 | -45.226898 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 077817db-c243-3639-857b-16aba15678f2 | -14.4546 | -45.240299 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a49b05b9-9fb6-33d8-a219-5208afdbd947 | -14.4415 | -45.2295 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d51a5c7e-d54c-3d5c-92b4-8eb0c7be1ad7 | -14.4449 | -45.242802 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94734f87-c148-3ecd-ae53-98fecd3864dc | -14.4318 | -45.232101 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5711d0-506f-3927-b280-111bbf7fff2b | -14.4352 | -45.245399 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5675a7ef-4139-3ec9-8e90-4cf208325226 | -14.5582 | -45.653099 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c44407ba-6764-39b6-8716-a7449ab76bba | -14.5613 | -45.6656 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f15b6806-15da-32e7-9242-c09655cff280 | -14.5644 | -45.678001 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 625c00b7-39a7-314f-8074-632e1e7638c2 | -14.5547 | -45.6805 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 890c3bb4-f59d-353e-9e57-588646438b3d | -14.5579 | -45.693001 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 026adbff-9d13-3969-815c-e60963765c74 | -14.561 | -45.705399 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce276bb-f29b-3111-ba6a-19aeb9c87988 | -16.738701 | -55.514301 | 2024-09-26 00:54:28 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbe68a3f-cfaf-3798-b85a-f148a9671be0 | -16.740601 | -55.523899 | 2024-09-26 00:54:28 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e940e500-3f7c-368c-9dee-676e10e94e91 | -15.1776 | -48.806099 | 2024-09-26 00:54:30 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 206e2ac4-efc6-3ba2-ab73-d704de3bef25 | -16.990801 | -57.916901 | 2024-09-26 00:54:32 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbeaae1e-f110-352b-98b4-266315f12211 | -16.9786 | -57.905399 | 2024-09-26 00:54:32 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f0295238-05b0-3eb2-a10f-c7b37f36bb76 | -16.9811 | -57.9189 | 2024-09-26 00:54:32 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abc91de1-949a-3cb5-9985-d8a4735152b2 | -16.9837 | -57.9324 | 2024-09-26 00:54:32 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17f65699-fda9-3343-931c-8b41ce2af02a | -16.9688 | -57.907299 | 2024-09-26 00:54:32 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b7b0847-075d-3fe1-9d35-2469142b4d1d | -16.9713 | -57.920799 | 2024-09-26 00:54:32 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4a7db8b-27f9-314c-891f-a91534dc1ede | -16.841 | -57.7131 | 2024-09-26 00:54:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4ab2a1b-84f7-3523-8d74-a2f4be267e78 | -16.8265 | -57.743099 | 2024-09-26 00:54:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f5eab69-d08e-3471-8f24-88ad1c1c9dcb | -16.828899 | -57.756199 | 2024-09-26 00:54:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7d62d8b-b06a-3b15-9adb-6c34f69ef80f | -16.8167 | -57.745098 | 2024-09-26 00:54:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32fd05fd-d651-3872-9f2a-5fd93d259808 | -16.819099 | -57.758202 | 2024-09-26 00:54:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 204fa67d-9d6d-38b0-b863-cb124343daf5 | -16.809299 | -57.760101 | 2024-09-26 00:54:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a32ee327-239d-305d-9316-7c66fe4938c9 | -16.799601 | -57.7621 | 2024-09-26 00:54:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9641f12b-99d3-3c4b-8572-9e9cac58f57b | -16.802099 | -57.7752 | 2024-09-26 00:54:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b56282ea-01f6-315c-9ca5-81b24621f55f | -16.789801 | -57.764 | 2024-09-26 00:54:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97bce4e1-207e-3048-b9c3-67277d5fb034 | -16.792299 | -57.7771 | 2024-09-26 00:54:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 857195d7-eb8a-3da6-97dd-4d886a534ddb | -14.8436 | -48.880199 | 2024-09-26 00:54:36 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90e60a07-138d-37d9-a1ef-4c5b171fece1 | -14.8281 | -48.858002 | 2024-09-26 00:54:36 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bcae7f24-eaf5-3d0c-9d3e-63f0443044b2 | -14.83 | -48.866199 | 2024-09-26 00:54:36 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f68c1f87-2cbd-3834-9c2b-28e6078abd7e | -15.0297 | -49.904202 | 2024-09-26 00:54:37 | METOP-B | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5624391a-3ed8-3919-85fd-846fd726e041 | -14.7968 | -48.900501 | 2024-09-26 00:54:37 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcfd87c5-87d8-3c4a-ad77-e7987eeaad53 | -14.7812 | -48.8783 | 2024-09-26 00:54:37 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0560c2b2-bc66-3f4f-aa36-806c1bb31ac9 | -15.0314 | -49.911701 | 2024-09-26 00:54:37 | METOP-B | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7e2e61f3-f8b2-3d2a-9ef7-c281bb368637 | -15.0336 | -51.3344 | 2024-09-26 00:54:42 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 98e712e7-0a99-3463-bd24-ac1b02e7f56b | -15.0238 | -51.3367 | 2024-09-26 00:54:42 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9cde6fde-d54b-3e4d-bb68-c893e234ce13 | -15.0254 | -51.3438 | 2024-09-26 00:54:42 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e0f891a9-3e02-3c78-b167-d313368189be | -15.027 | -51.350899 | 2024-09-26 00:54:42 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe639dd-a5d0-302e-be94-e5de8c23ef6a | -14.8737 | -51.080299 | 2024-09-26 00:54:43 | METOP-B | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 774dd924-2394-306e-b8d2-1573d24bc5e0 | -14.0266 | -47.919201 | 2024-09-26 00:54:45 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d976cf8f-70fb-3bb7-ad6f-dc2b302d9459 | -14.8729 | -51.491402 | 2024-09-26 00:54:45 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24eebfc0-281b-3fd5-9bda-6133fbccacac | -14.8744 | -51.498402 | 2024-09-26 00:54:45 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21bf99a5-6075-39ae-82d5-6b2a5a0a7f70 | -14.8631 | -51.493698 | 2024-09-26 00:54:45 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d08efef-d225-3f3a-a641-d7470584d509 | -14.8646 | -51.500702 | 2024-09-26 00:54:45 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c49a077-aaa5-3fb8-93ad-6c02b76bd5ef | -14.5858 | -50.808899 | 2024-09-26 00:54:47 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 43ee5bc4-10b3-36b4-9d97-fcd54659cd44 | -14.5875 | -50.816101 | 2024-09-26 00:54:47 | METOP-B | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b5d1f7d-4199-3bca-a211-b61ab33af49b | -13.8981 | -48.030102 | 2024-09-26 00:54:48 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d8ad1cc-e581-38ef-9764-370567af33b5 | -13.9003 | -48.039299 | 2024-09-26 00:54:48 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a0abc3c7-a098-3113-8e2c-edc7d0b286d4 | -13.8254 | -48.028702 | 2024-09-26 00:54:49 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| faf1c288-3322-364b-8eba-d0e3db444680 | -13.1936 | -45.615501 | 2024-09-26 00:54:50 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7a3b472-0898-3fc2-96a1-ffe84c0b61cd | -13.1969 | -45.628601 | 2024-09-26 00:54:50 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5a223fe-d98c-387f-bad0-b10bd733a134 | -13.2002 | -45.6418 | 2024-09-26 00:54:50 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cd53a9f-1875-3674-805b-0629cd6004f8 | -13.1807 | -45.604801 | 2024-09-26 00:54:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8e2258-24d2-3819-bd32-587bc7b47e1a | -13.1839 | -45.618 | 2024-09-26 00:54:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c920250-4ded-3174-8bb0-95bda6823ec5 | -13.1872 | -45.6311 | 2024-09-26 00:54:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bcb1a619-4763-3743-8dd0-21a971684af1 | -13.1905 | -45.644299 | 2024-09-26 00:54:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92292485-5d10-3755-bb30-1edecbee5013 | -13.3292 | -46.285599 | 2024-09-26 00:54:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba37efb3-dcbc-3e3f-a189-44936b41c000 | -13.3195 | -46.288101 | 2024-09-26 00:54:50 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bdd94039-8962-3d54-ab22-38b049dbe14b | -13.3127 | -46.302502 | 2024-09-26 00:54:50 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 806ea110-bd4e-35c5-81e1-52e314ebf461 | -13.3156 | -46.314301 | 2024-09-26 00:54:50 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64ff3fb6-2ca1-3858-8613-1fc4b4b87371 | -13.7899 | -48.096199 | 2024-09-26 00:54:50 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66780ef7-7717-32b4-99e4-81f013daacc0 | -13.792 | -48.1054 | 2024-09-26 00:54:50 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3432bc30-19ec-3ae2-88bf-82569e5005aa | -13.7942 | -48.114601 | 2024-09-26 00:54:50 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7bd89f27-a702-3f61-9361-64ae144d4303 | -13.7779 | -48.0895 | 2024-09-26 00:54:50 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9211d1f-35a9-33a3-b5f9-0bb099b0e4e3 | -13.7801 | -48.098701 | 2024-09-26 00:54:50 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 702ad411-9138-30e0-87a6-4c3ca8675d9a | -13.3088 | -46.328701 | 2024-09-26 00:54:51 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 84b4b3ef-a06e-3788-b00f-7925e4ccf578 | -13.2962 | -46.319401 | 2024-09-26 00:54:51 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ccd95a8b-c6c5-33bd-8d0b-902c5b352334 | -13.3029 | -46.305 | 2024-09-26 00:54:51 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34a925a6-3d78-3d1b-8f93-ac478c5eb9dc | -13.3059 | -46.316898 | 2024-09-26 00:54:51 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 050dfd8c-28bc-3548-b794-6ce901f235ae | -14.7803 | -53.856098 | 2024-09-26 00:54:55 | METOP-B | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed4a5b6c-d82a-3483-abfa-429776e9dc43 | -14.782 | -53.863701 | 2024-09-26 00:54:55 | METOP-B | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a27d0e88-d70f-3ff4-8167-04ea64e8aab4 | -13.7457 | -51.060501 | 2024-09-26 00:55:02 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0d3660f-2a1c-3614-a844-3aff5e0767cc | -13.7473 | -51.0676 | 2024-09-26 00:55:02 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 371c8dc3-4fb8-3a57-aedc-259ebf2748e9 | -13.7489 | -51.074799 | 2024-09-26 00:55:02 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec86be5-02fa-313d-9e84-767ab6b94294 | -13.7505 | -51.081902 | 2024-09-26 00:55:02 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7dbf5937-1218-3126-97d1-06cf17669b95 | -13.7375 | -51.069901 | 2024-09-26 00:55:02 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19d2d1be-4708-3a95-8abf-28300090d507 | -13.7391 | -51.077099 | 2024-09-26 00:55:02 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a10d9b6-1649-372b-8914-16ffba1f13f4 | -13.7407 | -51.084202 | 2024-09-26 00:55:02 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 790c4e9c-e00e-328e-ac29-bfe2e0737e79 | -13.1377 | -48.525902 | 2024-09-26 00:55:02 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ab55604-ad7c-3741-9af7-9ec18ae7a453 | -13.1399 | -48.534801 | 2024-09-26 00:55:02 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a53d418d-cc31-35da-b83f-a3b5ccad584f | -13.1301 | -48.537201 | 2024-09-26 00:55:02 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa875385-1e97-35cb-9f4a-bdb23cda8b11 | -12.9192 | -47.698502 | 2024-09-26 00:55:02 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e72945b-6a0e-315a-9a2b-504997ae0ede | -11.8343 | -43.800999 | 2024-09-26 00:55:04 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed70d37-e09f-365b-a9b6-29e6a5d147d8 | -11.839 | -43.819199 | 2024-09-26 00:55:04 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39a8326d-9454-30fe-a33b-7f89a9973b6a | -12.2288 | -45.477501 | 2024-09-26 00:55:05 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8623590e-72b5-3a58-a503-0e5fc26c9bc1 | -12.2323 | -45.491402 | 2024-09-26 00:55:05 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e22d89d-e69f-369f-99d7-1a891f1baa25 | -12.2191 | -45.48 | 2024-09-26 00:55:05 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d26073a-6833-3de6-93e7-516d24ae4122 | -12.2226 | -45.4939 | 2024-09-26 00:55:05 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb731ee7-61b7-3601-a62b-709e09a33e56 | -12.2261 | -45.507801 | 2024-09-26 00:55:05 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6bf18fa8-28fb-384f-bb30-a4364e1a7386 | -12.2129 | -45.496399 | 2024-09-26 00:55:05 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1522fac3-6582-366b-8e1e-82e987169257 | -13.643 | -51.4739 | 2024-09-26 00:55:05 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ff3b8a7-e25a-30c5-bbe6-96f9e41ec17c | -13.29 | -51.3251 | 2024-09-26 00:55:10 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08e1d086-44d9-3bbe-a172-d4d0b8bcc159 | -13.2916 | -51.332199 | 2024-09-26 00:55:10 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3996dcf6-9aee-3304-a562-4e471f82cb6a | -13.2932 | -51.339401 | 2024-09-26 00:55:10 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
