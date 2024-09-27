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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c2765ce-7a70-3875-ae42-f6683a763c51 | -20.7435 | -42.7607 | 2024-09-27 00:31:23 | METOP-B | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80217d18-5870-3952-bfa7-ab7d89018dc7 | -20.7453 | -42.768799 | 2024-09-27 00:31:23 | METOP-B | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dde29192-37a9-3f20-a314-2f6fd1bc902d | -20.7472 | -42.776798 | 2024-09-27 00:31:23 | METOP-B | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 516294f9-1824-312d-8d8a-72bd46bb8256 | -20.5334 | -41.864201 | 2024-09-27 00:31:23 | METOP-B | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e68be858-7b14-3199-8a59-4783afad7b8c | -20.5354 | -41.873001 | 2024-09-27 00:31:23 | METOP-B | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d8e93e38-755f-3974-8071-a254caa08243 | -20.5257 | -41.875599 | 2024-09-27 00:31:23 | METOP-B | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 962260bb-3e9f-3c64-87f7-9e764128649e | -20.620701 | -42.2784 | 2024-09-27 00:31:23 | METOP-B | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14779ba7-9443-38c4-851a-85987eabf4cc | -21.930599 | -48.541 | 2024-09-27 00:31:24 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 19626905-c6f1-32a9-8c65-735d36160670 | -21.9324 | -48.550201 | 2024-09-27 00:31:24 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21268b0c-665d-3ed1-9e04-2d5eb4cdc0d7 | -20.2955 | -41.131599 | 2024-09-27 00:31:24 | METOP-B | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16ccfa07-94ef-313a-b3b2-92a7258453df | -20.2978 | -41.141102 | 2024-09-27 00:31:24 | METOP-B | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5fb57926-ba8a-3d21-9692-770a17f2457c | -20.273701 | -41.298599 | 2024-09-27 00:31:25 | METOP-B | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9eb27c96-66f2-33bb-a550-91cc621e0090 | -20.275999 | -41.307999 | 2024-09-27 00:31:25 | METOP-B | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ae731b1-e48f-39c4-855a-025d4c178208 | -20.2782 | -41.317299 | 2024-09-27 00:31:25 | METOP-B | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f4e7d49-ef7b-33ad-8c23-74f837aca349 | -20.266199 | -41.3106 | 2024-09-27 00:31:25 | METOP-B | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 56044743-2f0f-3735-9040-9fbf9fc66e5a | -20.429501 | -41.9939 | 2024-09-27 00:31:25 | METOP-B | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e9bbbeb-fe79-3e54-9d35-c542fd17136f | -20.431499 | -42.002499 | 2024-09-27 00:31:25 | METOP-B | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30085590-fd97-3293-a708-a5caffd1e3b9 | -20.433599 | -42.0112 | 2024-09-27 00:31:25 | METOP-B | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ffc8aead-d9b0-3ac4-9104-d2d06d41177c | -20.617599 | -42.8871 | 2024-09-27 00:31:26 | METOP-B | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26d64f43-b0c8-3270-bfcb-080907a16509 | -20.619499 | -42.895 | 2024-09-27 00:31:26 | METOP-B | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 423542a7-e5f6-3672-b37c-5b13cea29a0e | -20.142 | -40.883999 | 2024-09-27 00:31:26 | METOP-B | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26ad4184-c8f7-3744-a137-3c187c2a1c4b | -20.187 | -41.844501 | 2024-09-27 00:31:29 | METOP-B | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb0b68b6-bd3b-375b-a94c-be54d0b0864d | -20.1891 | -41.853298 | 2024-09-27 00:31:29 | METOP-B | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb9c3866-4c65-3d6b-9359-cc69e249a2c2 | -20.3295 | -42.714401 | 2024-09-27 00:31:30 | METOP-B | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 66badb01-4f2a-3546-adec-8d4f83e4ab44 | -20.3314 | -42.7225 | 2024-09-27 00:31:30 | METOP-B | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4b6af51-74f3-323b-a010-b94c45bfb2db | -20.493999 | -43.4744 | 2024-09-27 00:31:30 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0aba71a2-6603-3ba0-aaaf-f8b91323adb7 | -20.4958 | -43.482101 | 2024-09-27 00:31:30 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac68f28b-f7b6-3e4c-a8c3-9f52b37ee17f | -20.2598 | -42.637402 | 2024-09-27 00:31:31 | METOP-B | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 174d722e-d299-3f0a-bcd9-9dc9bfe148ea | -20.2617 | -42.645599 | 2024-09-27 00:31:31 | METOP-B | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 082040d9-379c-3550-91e9-d6a8b939fe91 | -20.556601 | -44.581902 | 2024-09-27 00:31:33 | METOP-B | CARMÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3114501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2f41ea8-e09f-340d-a985-9a3d5473038a | -21.321199 | -48.867599 | 2024-09-27 00:31:35 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 91af7ee6-18e3-3bb4-8e06-4aec587da4e4 | -20.161501 | -43.510502 | 2024-09-27 00:31:35 | METOP-B | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac197f6c-d0cc-3b4d-847e-2ab93e9cd617 | -19.8666 | -42.152302 | 2024-09-27 00:31:35 | METOP-B | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cf9c2c3-13ab-35df-98ba-4103c2aee5d9 | -19.868601 | -42.1609 | 2024-09-27 00:31:35 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e51ac1e-b248-3faf-bf76-e9bc7aabdac6 | -19.8589 | -42.163502 | 2024-09-27 00:31:35 | METOP-B | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09e1e492-cb69-3362-948e-aa135f6dc187 | -19.861 | -42.1721 | 2024-09-27 00:31:35 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7baaa405-a758-3331-a1fe-0a46d176d154 | -20.1499 | -43.505299 | 2024-09-27 00:31:36 | METOP-B | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d303bf03-275c-3429-89d3-4fb184e814b0 | -20.151699 | -43.513 | 2024-09-27 00:31:36 | METOP-B | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d2173af3-b265-3ee0-a228-e8c6d81ca725 | -19.747601 | -42.1745 | 2024-09-27 00:31:37 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d3d2319-044b-3b64-a163-b7fc903e9469 | -19.749701 | -42.183102 | 2024-09-27 00:31:37 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f79da8d9-419d-3fa9-850d-ba3c9e2e2f02 | -19.751699 | -42.191799 | 2024-09-27 00:31:37 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2bd0ac7c-94ac-3005-beb0-32bb5b8ef041 | -19.7379 | -42.177101 | 2024-09-27 00:31:37 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a433f672-9e7f-34fc-aca4-d17733d2d701 | -19.74 | -42.185699 | 2024-09-27 00:31:37 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7f0ff13-f957-3764-8deb-867ce5df228d | -20.424 | -45.246101 | 2024-09-27 00:31:37 | METOP-B | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 62482f80-98de-3174-87f2-e17cbd16bf31 | -20.0889 | -43.827301 | 2024-09-27 00:31:38 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f83cab3-89b7-3b00-992f-9f7db723100c | -20.090599 | -43.8349 | 2024-09-27 00:31:38 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dcbae9f3-7610-3cc3-8bab-d3dff4576e18 | -20.159 | -44.323002 | 2024-09-27 00:31:38 | METOP-B | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bdc0487-f4df-3773-be25-30907ecb1f4d | -19.7141 | -42.3829 | 2024-09-27 00:31:38 | METOP-B | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 545e2021-bc95-3518-9cde-4e6c71eac324 | -20.5378 | -46.355701 | 2024-09-27 00:31:39 | METOP-B | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6758844-5c6a-339e-bf82-1575fc34fd2e | -20.147499 | -44.318001 | 2024-09-27 00:31:39 | METOP-B | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 303cba67-08e2-354d-ad1b-b9ebdcdb45dc | -20.1492 | -44.325401 | 2024-09-27 00:31:39 | METOP-B | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b074836c-dc53-3c68-8201-4ebae1df49ac | -20.150801 | -44.332802 | 2024-09-27 00:31:39 | METOP-B | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 275a6875-d2bb-3e6d-9196-d13823ae6632 | -19.704399 | -42.385502 | 2024-09-27 00:31:39 | METOP-B | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 251fa633-806d-3c84-b627-237c17d5e248 | -21.1035 | -49.111801 | 2024-09-27 00:31:39 | METOP-B | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f8d88eb-5a5a-3ae9-8ae5-7e2a0dedc51b | -21.1054 | -49.121399 | 2024-09-27 00:31:39 | METOP-B | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ade57581-709f-3c44-b43e-a64bbe188c0b | -21.107201 | -49.131001 | 2024-09-27 00:31:39 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e498856-ed99-3922-8e9e-bb7602277ab1 | -21.1091 | -49.140598 | 2024-09-27 00:31:39 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d47b61ee-c715-3733-a708-285e588b3f9d | -21.110901 | -49.1502 | 2024-09-27 00:31:39 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3db9a3f1-3eba-3764-8ce0-334087941450 | -21.0937 | -49.113899 | 2024-09-27 00:31:39 | METOP-B | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41e33e69-82c7-3756-88b6-e85931e1e063 | -21.0956 | -49.123501 | 2024-09-27 00:31:39 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f137f34e-691e-38c0-94cd-8e28256c5ce6 | -21.097401 | -49.133099 | 2024-09-27 00:31:39 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9ae5bd8-151d-35c1-9242-e1230c6a6a8f | -21.0993 | -49.1427 | 2024-09-27 00:31:39 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47d0c961-2985-33f0-b998-5c8a38360d86 | -21.101101 | -49.152302 | 2024-09-27 00:31:39 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfd6fbd8-27df-3bc1-8f10-c3ae582228ab | -20.5214 | -46.375301 | 2024-09-27 00:31:40 | METOP-B | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c3574fb8-ecdf-380b-a32d-346ca50b81f8 | -20.1136 | -44.490002 | 2024-09-27 00:31:40 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90abfd06-e4e9-3028-b72e-a1f2183b21ba | -20.115299 | -44.497398 | 2024-09-27 00:31:40 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 13ec4f12-84c4-3e0e-a99f-c5b31e897742 | -19.9396 | -43.760899 | 2024-09-27 00:31:40 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 575127aa-ef24-346d-91d4-c6cc0ffca23c | -19.941299 | -43.768501 | 2024-09-27 00:31:40 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6bf0b367-499e-3cba-9a84-31e3d1094cde | -19.9447 | -43.783699 | 2024-09-27 00:31:40 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3c1092b-5c60-3241-baad-39b1f1da9223 | -19.9252 | -43.788601 | 2024-09-27 00:31:40 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38669e9e-8973-3e99-bb03-16303bdf1913 | -19.927 | -43.7962 | 2024-09-27 00:31:40 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0c922f5-2820-3e3e-bea8-b379ef83ad54 | -19.9172 | -43.798698 | 2024-09-27 00:31:40 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 668113ba-cb73-3ab2-bb10-99647a026791 | -21.0839 | -49.116001 | 2024-09-27 00:31:40 | METOP-B | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 32e55df5-5511-39de-b825-6fad01dc31c8 | -21.0858 | -49.125599 | 2024-09-27 00:31:40 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d871e4e9-c778-341d-80b3-dc02bdf5404d | -21.087601 | -49.135201 | 2024-09-27 00:31:40 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cca1f68-79e9-3016-870e-c6f2875c2efc | -21.0895 | -49.144798 | 2024-09-27 00:31:40 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d091145f-8f27-3c6f-a98e-37c77007ffb0 | -21.091299 | -49.1544 | 2024-09-27 00:31:40 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61c92b5c-1e46-3985-8ee6-38f141df1716 | -21.077801 | -49.137299 | 2024-09-27 00:31:40 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 935dc288-64cd-39f2-ba53-e69bbf34f20f | -21.0797 | -49.1469 | 2024-09-27 00:31:40 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37eddfc9-6f9b-38aa-940b-74da602a5db6 | -19.647301 | -42.848598 | 2024-09-27 00:31:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d53ed6d-a934-39d8-aa8c-d337ab887ea6 | -19.6492 | -42.856701 | 2024-09-27 00:31:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 747b0d21-5fb8-3a3f-9ba3-9737798e2fba | -19.624201 | -42.794102 | 2024-09-27 00:31:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1b4ef4b8-d0d5-32e2-815a-70b11e590c7b | -19.626101 | -42.802299 | 2024-09-27 00:31:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83d0e7cb-06b5-3f80-bbc1-6fbdf15badb9 | -19.628 | -42.810398 | 2024-09-27 00:31:41 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba444ab8-fdeb-3eb0-a388-fdfc7d6ca9cf | -19.6164 | -42.804901 | 2024-09-27 00:31:42 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3db977e0-fe83-3717-9520-86071f66f451 | -19.618299 | -42.813 | 2024-09-27 00:31:42 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d51cc08f-0b90-30ac-b4c7-a64272411716 | -19.6028 | -42.7911 | 2024-09-27 00:31:42 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 55652f7c-4658-36c7-89be-20fc14d298f2 | -19.6047 | -42.799198 | 2024-09-27 00:31:42 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f5e9e1e-6291-32c8-80c2-6f763951c9c1 | -19.6066 | -42.8074 | 2024-09-27 00:31:42 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bdfd31dc-f086-3550-b5d9-792b9f7ad1de | -19.6085 | -42.815498 | 2024-09-27 00:31:42 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87c1e75d-b03b-3c33-b9f0-ea8f63ae071b | -19.591 | -43.185799 | 2024-09-27 00:31:43 | METOP-B | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b6582593-6714-3787-a460-fcd4fc612e32 | -20.024 | -45.205299 | 2024-09-27 00:31:44 | METOP-B | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb67fa8-a757-36ea-a36f-13701ae9f88c | -20.0142 | -45.207699 | 2024-09-27 00:31:44 | METOP-B | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf01828-0c8e-30f0-a486-8d17404675cf | -19.385 | -42.5672 | 2024-09-27 00:31:44 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b38e9d69-d7eb-37a6-b8f4-551a40362793 | -19.3869 | -42.5755 | 2024-09-27 00:31:44 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5173252b-f136-3a81-a464-dc4c912ce0cf | -19.151199 | -41.369801 | 2024-09-27 00:31:44 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1864aac5-4296-32fa-922a-e931bda7050a | -19.1535 | -41.379299 | 2024-09-27 00:31:44 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 355d1d40-6fd4-3e88-816a-b7c87f967ec8 | -19.1558 | -41.388901 | 2024-09-27 00:31:44 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c9c7833-3413-33cd-aba2-53fc2fa44361 | -19.141399 | -41.372398 | 2024-09-27 00:31:44 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 450dd33e-42fd-3da9-a231-a3138763eb4d | -19.371201 | -42.552898 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README7.md)
