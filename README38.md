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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf26d7ac-d3e0-3177-a458-fb7a818fb7f2 | -14.004 | -44.0201 | 2024-10-04 01:36:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| def04dea-c941-3dc3-9a28-efaf73afb1f4 | -14.7939 | -48.0275 | 2024-10-04 01:36:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f78ca1bb-fcb8-3a3d-af7a-2f7523eefcd7 | -16.4148 | -57.4028 | 2024-10-04 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 48d37d3a-5982-3715-9c71-cd1cc93a3bd0 | -16.4151 | -57.3823 | 2024-10-04 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 34a71388-998c-34e1-8a32-2252c2d018f1 | -16.573 | -57.2624 | 2024-10-04 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 9bd46b8f-c90d-3885-937a-107703f9934d | -16.5733 | -57.2419 | 2024-10-04 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| eb4c452c-6fe9-3ef6-804c-4f3ab4f7cbd2 | -16.5736 | -57.2215 | 2024-10-04 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 812eac04-6134-3e2e-a47d-a6e0a7439978 | -16.5783 | -58.198 | 2024-10-04 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 00278931-ec37-3f76-9ec2-7d11bf92770f | -16.5925 | -57.2602 | 2024-10-04 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 2546edbb-4505-31d2-a6a3-55168324194b | -16.5928 | -57.2397 | 2024-10-04 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 49ee338a-40fd-3c9c-b04e-0b4fa9a1faa7 | -16.5935 | -57.1988 | 2024-10-04 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 1431f6c1-2080-30e3-848b-ff485e880d9e | -16.5938 | -57.1783 | 2024-10-04 01:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 9027f1fe-053e-30ae-a387-d22554b9c434 | -16.613 | -57.1965 | 2024-10-04 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 01720091-f4aa-3859-b466-89eaafe5e172 | -16.6133 | -57.176 | 2024-10-04 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 8c5be916-9b04-3b78-b0f2-8231dc0a0708 | -16.7606 | -57.7512 | 2024-10-04 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| f9a589b2-b99f-36fc-ac06-f3b7f6cbb5af | -16.9302 | -47.1224 | 2024-10-04 01:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 59421257-4f1e-35f8-b784-aef886707287 | -16.95 | -47.1185 | 2024-10-04 01:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 99597fef-eada-324c-bb16-8785ff62a99e | -16.779 | -57.8306 | 2024-10-04 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 500228d3-a40d-36f4-b5f5-cfe71a625353 | -16.7859 | -57.3811 | 2024-10-04 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| f9e38a98-2343-3007-8f3d-949b24bf14d4 | -16.7985 | -57.8284 | 2024-10-04 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.0 |
| 1dc690a2-e3bb-3846-a365-755fcdfd7ac0 | -16.8055 | -57.3788 | 2024-10-04 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 141d9920-c7ba-371c-b111-07b9c4f5c1c7 | -16.843 | -57.4767 | 2024-10-04 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 61c23be2-7aa5-3993-a188-a9c3ee1bca34 | -16.9087 | -55.843 | 2024-10-04 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| e37cc857-32b1-34b2-b610-bef9d1ea6674 | -16.9091 | -55.8222 | 2024-10-04 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 8084fee5-3a67-39ef-9b02-55227316bbd5 | -16.9283 | -55.8405 | 2024-10-04 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| fbe93380-544a-3541-ab72-4da60d1adedd | -16.9287 | -55.8197 | 2024-10-04 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 49b639d0-a825-353b-b4f3-8dd1ad9b30c4 | -17.0616 | -56.0723 | 2024-10-04 01:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 5bad5ffc-5d4c-3dde-ab79-96cb008436cc | -17.0316 | -56.6956 | 2024-10-04 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| dd21cdb2-1d93-3f7b-8023-cf13ee43295f | -17.0512 | -56.6932 | 2024-10-04 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 90245a67-8832-3c4d-9169-f7b3b2662929 | -17.3643 | -42.6284 | 2024-10-04 01:36:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5622fbc9-0c08-3bab-9b4b-46504b59b048 | -17.3844 | -42.6235 | 2024-10-04 01:36:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ef69d4fe-288e-31ca-966b-144182f6c91b | -17.5339 | -46.7472 | 2024-10-04 01:36:43 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1c363ecf-16e5-38a4-8b2f-c6216c84eae3 | -17.5344 | -46.7239 | 2024-10-04 01:36:43 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 37ff1f9c-df6d-3c97-9c1d-a5fc483b4b9a | -17.7307 | -43.8127 | 2024-10-04 01:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 117.2 |
| b8f35014-fe2f-30ea-9bd3-f8f2e329b6a2 | -17.7313 | -43.7883 | 2024-10-04 01:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 81cc595e-4ec2-3303-be51-a1b04cba0301 | -17.7508 | -43.8079 | 2024-10-04 01:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 930c6c39-024b-3ca9-8650-cc33039ea6ca | -17.7515 | -43.7835 | 2024-10-04 01:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 3927eeb4-a074-3ee1-83e9-c13b3a976da2 | -18.0854 | -42.5976 | 2024-10-04 01:36:46 | GOES-16 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.3 |
| c55cd51d-92f2-374d-bf83-ab7b053d3d6e | -18.8406 | -42.9235 | 2024-10-04 01:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 5241f7a6-6809-3a0d-a73f-10fa5e278920 | -18.8413 | -42.8985 | 2024-10-04 01:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.1 |
| 415ef019-4c36-3e66-8d5e-27a19ba37345 | -18.8609 | -42.9182 | 2024-10-04 01:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| b6211347-a44e-3705-b1d0-fb84de48c589 | -18.8617 | -42.8932 | 2024-10-04 01:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.8 |
| 5d70fcb1-0842-37ff-8a50-f6390add8153 | -18.8613 | -43.5837 | 2024-10-04 01:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.7 |
| e8df88e9-ad66-3d4f-976f-76f8a5f9eebf | -19.2794 | -43.795 | 2024-10-04 01:36:52 | GOES-16 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 3df13613-0530-3186-a83d-7656930bea19 | -19.2801 | -43.7703 | 2024-10-04 01:36:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5d811e12-a763-39ce-bdfe-10f7a26db8c1 | -19.3159 | -42.5976 | 2024-10-04 01:36:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| cb1956af-6e28-3bcd-96a3-813ab2dd0641 | -19.3167 | -42.5724 | 2024-10-04 01:36:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.5 |
| 1db5eaf1-4c96-3dd0-ac7c-f652bd7477f4 | -19.2998 | -43.7897 | 2024-10-04 01:36:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 038d2856-2762-3b81-8a71-2a115eaf74a1 | -19.3005 | -43.765 | 2024-10-04 01:36:52 | GOES-16 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 76116fa8-02cf-3bb8-baa9-a25ab7d01d65 | -19.3363 | -42.592 | 2024-10-04 01:36:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| b1135a07-6032-3ca4-9002-d96b03bd1b6e | -19.3371 | -42.5668 | 2024-10-04 01:36:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| 2f06aca3-7356-36b0-81fb-0a07551eaade | -19.4899 | -42.8746 | 2024-10-04 01:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| 862748fb-82aa-3d3f-9c79-dc8f2462617d | -19.9907 | -48.6913 | 2024-10-04 01:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ddbd5881-2cd2-3a0d-b8a7-ff77f4f2d8d7 | -20.0111 | -48.6869 | 2024-10-04 01:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b4ed3a27-055f-3413-8ae1-7eac84907224 | -20.5176 | -48.7361 | 2024-10-04 01:36:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 7dddeac9-1ff5-397f-89f9-1d76843e516b | -21.3328 | -48.8277 | 2024-10-04 01:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| b968c49e-3fda-3b62-889d-af92d2fd605b | -21.3334 | -48.8044 | 2024-10-04 01:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.1 |
| d2528075-de9d-3a60-9d9a-1527376ec4a4 | -21.3534 | -48.8229 | 2024-10-04 01:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 175.3 |
| c2a1563b-8e87-351a-b437-34baf8edb171 | -21.3541 | -48.7996 | 2024-10-04 01:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 234.2 |
| f2e499c0-d744-3a3f-927f-57708d0f7b82 | -21.7981 | -48.3926 | 2024-10-04 01:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c809aad3-17d8-35cd-aef0-bb566c2293c2 | -21.7988 | -48.3691 | 2024-10-04 01:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 6d999a90-17e0-341b-8c3c-e0f5740686b7 | -21.8079 | -48.7626 | 2024-10-04 01:37:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c6d68fd8-49fa-321b-bb41-59722f155072 | -21.8175 | -48.4346 | 2024-10-04 01:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 146.5 |
| c0c0eba2-af5f-31ff-8403-a293b85eb2c2 | -21.8189 | -48.3876 | 2024-10-04 01:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 10483b04-b8d2-3a5e-ab30-d1f52f2c967b | -21.8196 | -48.3641 | 2024-10-04 01:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 08dc9195-18e8-3513-96e4-ecd861a1e65d | -21.8383 | -48.4296 | 2024-10-04 01:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 47b75f72-4d09-347b-b220-d4550e8d975b | -22.2684 | -51.4941 | 2024-10-04 01:37:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| 99cba3ba-976b-3407-9ea2-c096f62b7a39 | -3.2349 | -50.3695 | 2024-10-04 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c2f7ee3c-6b4b-3fff-8943-50a1262e973b | -3.2534 | -50.3689 | 2024-10-04 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ca8acfda-fde0-329a-baa4-1c2d0303d3be | -3.404 | -42.2858 | 2024-10-04 01:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 5618bcd7-5a8f-387d-a90f-509a8c0084f0 | -3.2899 | -50.4725 | 2024-10-04 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 443c64c7-fd0a-353f-a44e-847be55152cb | -3.2899 | -50.4516 | 2024-10-04 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 3babe3fd-f621-3d88-b151-3b0ff5ca5d02 | -3.3083 | -50.4719 | 2024-10-04 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| c6b1427b-a7fc-36f2-b27e-e7f05efd0feb | -3.3084 | -50.451 | 2024-10-04 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 161.2 |
| c0ca1428-eddf-317c-997f-cdef50947ff4 | -3.4915 | -50.8004 | 2024-10-04 01:45:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5a9736bf-2615-3d89-8e9e-219eaa876237 | -4.5375 | -43.304 | 2024-10-04 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| b7e7d95a-4498-3817-afb2-7c6e33a68237 | -4.6684 | -45.8961 | 2024-10-04 01:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 63d69392-2a1c-33b9-b14c-6f9247087c9b | -4.6686 | -45.8738 | 2024-10-04 01:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 229.9 |
| bbaba50e-930c-3d88-9a7f-36fa8d679972 | -4.687 | -45.8951 | 2024-10-04 01:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 221.1 |
| 20c59904-9420-31bb-bb74-df14ffab8d83 | -4.6872 | -45.8727 | 2024-10-04 01:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 376.8 |
| f2280a25-68d3-37d7-ac3d-871b51b46d2a | -4.6873 | -45.8504 | 2024-10-04 01:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9967f851-990e-3096-aff8-7caabd45d97a | -4.7058 | -45.8717 | 2024-10-04 01:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1452846a-3577-3d3c-aa5a-6bc7a21c9a89 | -5.8214 | -44.1426 | 2024-10-04 01:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 8d3a8526-885e-3534-8b0d-c43fd31ae386 | -5.8216 | -44.1196 | 2024-10-04 01:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e4466c67-5edf-3421-8690-5e28abf2b94c | -7.8164 | -50.543 | 2024-10-04 01:45:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a26c83fc-6afc-3a81-a6d2-ef4f1c6c85c2 | -7.8166 | -50.5219 | 2024-10-04 01:45:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ddc66c15-3717-33e4-a3c7-b6786494c93a | -7.8351 | -50.5416 | 2024-10-04 01:45:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5d61ee25-54c1-39b9-b3f1-423aa9d7b9e0 | -7.8353 | -50.5204 | 2024-10-04 01:45:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e6ffa254-6bd9-3d3f-9058-30dd30132c92 | -8.6448 | -50.0518 | 2024-10-04 01:45:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 4a95a6b0-09cb-3bab-9fb2-db450bb332d8 | -9.1041 | -50.902 | 2024-10-04 01:45:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 54d2bb92-13d2-3a35-80b4-5acdc1ba83d9 | -9.0162 | -67.3904 | 2024-10-04 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0bced79e-1bdb-3204-b02c-41e5254eaf23 | -9.0347 | -67.39 | 2024-10-04 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b359e096-8472-32ec-9ad1-6f2981f46738 | -9.3115 | -50.8203 | 2024-10-04 01:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 964ccf9c-5e8d-3bda-b3a1-d26677195bed | -9.3118 | -50.7991 | 2024-10-04 01:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 293.8 |
| 091cdab2-5ba0-34fc-9d16-9d7f032a504e | -9.312 | -50.7779 | 2024-10-04 01:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 64047b99-ae5b-3eb5-aeb1-b40f53e44ffd | -9.3303 | -50.8186 | 2024-10-04 01:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 8cfba118-9f13-302a-8c29-51a0e24c9cb7 | -9.3306 | -50.7974 | 2024-10-04 01:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| ac185d89-192d-39f4-9415-c47ef6069b34 | -9.871 | -36.3782 | 2024-10-04 01:46:01 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 129.9 |
| a3c3e5d0-3310-332d-a35d-fffbf5430684 | -9.8349 | -46.7726 | 2024-10-04 01:46:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 15a08b80-1806-362e-9315-896bae08ffbe | -9.8353 | -46.7502 | 2024-10-04 01:46:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |


[Clique aqui para ver as próximas entradas](README39.md)
