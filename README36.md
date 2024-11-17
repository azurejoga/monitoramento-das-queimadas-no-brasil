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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17ac73e4-6b71-3cf3-8467-0ab6d815adda | -17.6063 | -57.5715 | 2024-11-17 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| b5a5a74b-aa04-3d15-92ed-8a542dcaf8ce | -17.5865 | -57.5739 | 2024-11-17 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 5deb012a-3312-3b01-8a3d-ba7816b70851 | -17.6059 | -57.5921 | 2024-11-17 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 2c9e93d0-849c-38a4-973b-80654bde1678 | 0.6159 | -51.7676 | 2024-11-17 04:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b61e539d-2311-3b79-bce4-e56921a663e9 | -3.5308 | -50.2757 | 2024-11-17 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| f55163be-794d-390d-93fb-b5abc8d40d6d | -17.5862 | -57.5944 | 2024-11-17 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 8132bee6-3a1d-3aec-82a9-eee46a67cc6e | -3.531 | -50.2337 | 2024-11-17 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6672f660-3b7c-3a31-9d0d-e758478bb647 | -3.5309 | -50.2547 | 2024-11-17 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 205.9 |
| cd5112b3-e150-3219-9eab-67fbf4421d41 | -2.6137 | -48.5639 | 2024-11-17 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 5ecad975-7341-3825-a38e-fc81cf53c36b | -3.5494 | -50.254 | 2024-11-17 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| cf9be99f-dba8-3e91-9c72-e93b5071e303 | -17.6008 | -57.60296 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1a5c5753-d512-394f-9c39-41aa9a3c7d0f | -17.58886 | -57.59321 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b5aadeb3-68e4-3fc1-a6d1-55338d1f6e31 | -17.6013 | -57.5699 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| bbe8de69-271b-3f45-bc93-896a5e06fbb9 | -17.59676 | -57.59464 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6d4f7f53-6ef1-3d79-ae82-56efd44f38bb | -23.33711 | -46.77381 | 2024-11-17 04:10:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d11eed03-134b-38fb-b4b2-6bfbb84761d6 | -17.59007 | -57.59292 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| da10e96f-9d20-34e2-b98b-04070328bdba | -17.60492 | -57.5901 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 649ad867-bc6e-34dd-acbf-f08c797e28c8 | -17.59843 | -57.5824 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0c969a18-5103-39bb-87a4-3cf51deef17f | -17.60367 | -57.59042 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 86199d1a-2e05-3871-9aba-2b27e6d32819 | -17.59986 | -57.57615 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e1896917-2c7d-38f5-829b-17f82721367b | -17.61013 | -57.59812 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c5afcad2-4570-3f00-be36-9f64bee7dbb6 | -23.04517 | -49.89647 | 2024-11-17 04:10:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9480586-99cc-3b58-8079-b2d09cb1b93a | -19.48775 | -56.61866 | 2024-11-17 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b78ec80f-9b8d-328d-9267-9642c42eb6b5 | -17.61035 | -57.5922 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| dadbb7d4-089d-3b18-835b-5fcb928121f0 | -17.60511 | -57.58414 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3ec08a60-2352-3484-a671-a5d1ea235e50 | -17.60892 | -57.59847 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 08ff1428-27ba-3cc9-b390-c825b251ef12 | -17.60655 | -57.57787 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b0b846a1-1034-33f4-b288-02e3a0af6c83 | -23.04667 | -49.89454 | 2024-11-17 04:10:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c0d1b221-02fd-3b33-be9a-89a39182148c | -17.59699 | -57.58868 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cec714da-9761-3cb6-b450-417b5ad7cfe7 | -17.60786 | -57.57762 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ec89d5f0-41fd-37a1-811c-c429b4462aed | -16.34962 | -43.69411 | 2024-11-17 04:10:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96d91319-6350-30a0-ad99-d514f0c677b2 | -17.59555 | -57.59495 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| c7745ee9-c2a5-3b29-9b1f-e275219bf497 | -17.59449 | -57.57423 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f47edc5a-406d-3b2d-b2f3-64fb5d57a67f | -22.92118 | -45.41473 | 2024-11-17 04:10:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3a6ccda-9650-3f93-860a-79b6d3a5f857 | -17.60345 | -57.59635 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b2451146-90a4-3111-bbce-6c9be456dbd0 | -17.59411 | -57.60119 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 6718c2b5-a057-3808-a7dc-aca815107f2c | -17.60265 | -57.56968 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| e60aa21a-8b5e-3c86-8266-07d08a9a0fce | -21.93076 | -48.0224 | 2024-11-17 04:10:00 | NPP-375D | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcc3f837-690d-344c-8083-a2fbd6ca93ec | -17.60798 | -57.57163 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d638c293-ac19-3bba-93df-a4f23c5ee120 | -17.58743 | -57.59945 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8d9ebe6c-618e-3fe2-adab-d7c0cc18ebaa | -17.60224 | -57.59669 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 146d339a-ca1d-30a1-a890-6c5922a0f070 | -17.58859 | -57.59916 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d9298ab3-76a1-35ba-a074-0b973eec3b8a | -17.59823 | -57.58839 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| aa61a497-1fbd-331a-a27b-20ba31d00b79 | -17.6116 | -57.59185 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 6903465e-8105-3b4d-9126-b17eb1bffcb0 | -17.60933 | -57.5714 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ac21f651-a113-36dd-9fa5-767c7881faf9 | -17.60118 | -57.57591 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b08f2392-4dd0-35d7-903d-7b47773fa6dc | -17.60639 | -57.58385 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eca8a90f-0f12-3ac9-a7f2-e5dd1deefd05 | -17.59529 | -57.60088 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| f090ecb1-76fe-3a3f-b139-30894d12f07f | -19.48891 | -56.61363 | 2024-11-17 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8e0b4e8b-76eb-3989-8ce8-a40e945ec418 | -17.59971 | -57.58214 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2c81c98d-f715-3273-92fa-6be1b647ea0c | -17.61608 | -57.56713 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 45117075-1873-3730-a5fc-eee0af85ac6e | -17.61747 | -57.5669 | 2024-11-17 04:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8b887bec-4666-3deb-82ec-624ca52a6494 | -26.0072 | -49.76382 | 2024-11-17 04:12:00 | NPP-375D | CAMPO DO TENENTE | PARANÁ | Brasil | 4104105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c38c7512-be84-36ed-a646-1a32128d7e1c | -22.41506 | -54.17643 | 2024-11-17 04:12:00 | NPP-375D | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc22a9f6-f821-3240-8ad6-b1868511f8ed | -22.41438 | -54.17956 | 2024-11-17 04:12:00 | NPP-375D | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a871105d-d5e6-3648-9b0a-0e23d02f472c | -28.95731 | -49.40413 | 2024-11-17 04:12:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dd7bbb9c-fe66-318c-8a93-e610a8d459d9 | -28.95384 | -49.40334 | 2024-11-17 04:12:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ad14880-f438-3592-8d8b-12721a7d3bea | -29.13682 | -51.52094 | 2024-11-17 04:12:00 | NPP-375D | BENTO GONÇALVES | RIO GRANDE DO SUL | Brasil | 4302105 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 30c37e5a-f7e2-3624-ad04-beb3ff3eecee | -28.96002 | -49.40926 | 2024-11-17 04:12:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e77c7939-a3f7-3298-bc2a-40bb12f11ebd | -27.79108 | -53.94465 | 2024-11-17 04:12:00 | NPP-375D | SÃO VALÉRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4319737 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 239b589e-5b87-3832-b927-3f7b4f7a35ee | -29.13582 | -51.52615 | 2024-11-17 04:12:00 | NPP-375D | BENTO GONÇALVES | RIO GRANDE DO SUL | Brasil | 4302105 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 870b10a8-d0cc-3a9c-93f5-1d008a0365b7 | -28.95925 | -49.41362 | 2024-11-17 04:12:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 707bfc23-7146-3400-b4ed-63a02f973af5 | -27.79275 | -53.94239 | 2024-11-17 04:12:00 | NPP-375D | SÃO VALÉRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4319737 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 76f5ce41-70d4-3b18-b5ae-39c09fa8ad9e | -28.57599 | -50.14963 | 2024-11-17 04:12:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7da81be7-ab90-334e-aca4-7933e335d033 | -23.93909 | -54.08576 | 2024-11-17 04:12:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0d88ba99-b1b7-3993-9218-2926f6ce8f08 | -23.9413 | -54.08722 | 2024-11-17 04:12:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 860525be-6b66-311b-a254-748d92f66dbc | -28.57686 | -50.14492 | 2024-11-17 04:12:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4293281d-8e94-3b26-be8a-2a6ec06d95de | -28.96349 | -49.41006 | 2024-11-17 04:12:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fbb36d50-c65e-3031-aad5-2c85effb057b | -22.96194 | -54.43513 | 2024-11-17 04:12:00 | NPP-375D | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4c331bc4-8eda-3f32-a4f9-a703babe4bda | -23.93647 | -54.08598 | 2024-11-17 04:12:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 043abe4f-e1c3-3266-b709-075cb99c6d68 | -27.05615 | -52.62464 | 2024-11-17 04:12:00 | NPP-375D | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 29acfd52-ad3f-382f-88f4-603d9cfb9f04 | -27.79547 | -53.94596 | 2024-11-17 04:12:00 | NPP-375D | SÃO VALÉRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4319737 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b4da177d-d5cb-30de-96ab-5b119e8a44f7 | -28.95848 | -49.41796 | 2024-11-17 04:12:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75779347-6960-3547-98bb-615b0e297e21 | -22.96696 | -54.43639 | 2024-11-17 04:12:00 | NPP-375D | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66be1946-d3f9-3bba-a508-f0ba330c05d5 | -28.96272 | -49.4144 | 2024-11-17 04:12:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 91d66811-ea61-3687-8238-842ee71f96e4 | -29.7451 | -51.93554 | 2024-11-17 04:14:00 | NPP-375D | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 90cb906d-9e49-37c8-a198-834f3a88ba66 | -29.90657 | -54.94374 | 2024-11-17 04:14:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 19eb5a8f-6a02-3a8c-9ae3-119d2f8eb5ca | -29.89991 | -54.93081 | 2024-11-17 04:14:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 8f6cdeef-5912-308e-9029-b48c03ee1484 | -4.5614 | -48.0141 | 2024-11-17 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f7e2839b-01f0-32df-b209-f237a3da4a3c | -4.5616 | -47.9925 | 2024-11-17 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 13036df9-fad9-364b-94d8-729b0834938c | -17.6059 | -57.5921 | 2024-11-17 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |
| decf971f-0181-3030-b400-c3d004e36707 | -3.5308 | -50.2757 | 2024-11-17 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0edc6fa2-18fa-3275-a43f-0f4833ff0304 | -3.5494 | -50.254 | 2024-11-17 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| d19d5839-c147-3980-ae40-1c657e1eb2a3 | -3.531 | -50.2337 | 2024-11-17 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 26e68e39-0f2d-3f38-99d7-303b72d7b571 | -3.5124 | -50.2553 | 2024-11-17 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c9fa23aa-1bd8-3169-bac0-259d25c72c7c | -17.6063 | -57.5715 | 2024-11-17 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| d300da8e-4263-3cb7-abdb-602a4f3e06ac | -3.5125 | -50.2343 | 2024-11-17 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 2c1bcf27-0e65-3322-8403-81ec18dcb490 | 0.6159 | -51.7676 | 2024-11-17 04:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 9b79d930-acc6-3df4-8ffd-9250c7786431 | -2.6322 | -48.5634 | 2024-11-17 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 435dca5a-70ed-3623-858e-d50b7921426e | -8.4336 | -44.2019 | 2024-11-17 04:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 311470fa-023d-3ccd-8191-a9a1854b381d | -17.5862 | -57.5944 | 2024-11-17 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 32b77610-db0b-30d0-a78e-5687d7defd64 | -3.5309 | -50.2547 | 2024-11-17 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 9b817bdc-4bb4-3767-ac05-fe808a8b0d4a | -0.31514 | -48.70113 | 2024-11-17 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eae1116e-6b2a-33ab-9a54-aa11bd9239e1 | 1.57875 | -55.88424 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d018c211-93cd-38fe-82d9-3fe92aef1ff2 | 0.51385 | -50.74393 | 2024-11-17 04:27:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 670c96fd-a360-369b-abfe-2048b057f1e2 | -0.3198 | -48.69411 | 2024-11-17 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f39fd714-8ca3-3458-b76c-6e70eb9507e3 | -0.31574 | -48.69735 | 2024-11-17 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ad2f447-2af3-307c-ad40-d9a6bff9b351 | 0.41592 | -50.86239 | 2024-11-17 04:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f02e1fc-33c4-33c3-af96-984f437b6d76 | 0.61583 | -51.77612 | 2024-11-17 04:27:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 32.1 |
| beb5fe3c-9d8d-3ad2-9cc2-f962d8335b1c | 1.58322 | -55.87581 | 2024-11-17 04:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README37.md)
