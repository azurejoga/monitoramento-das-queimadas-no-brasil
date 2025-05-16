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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9fe3eea-51db-34fb-8803-7ce95a697374 | -8.43037 | -46.63871 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e9d1cb8-ac7c-3849-9e6a-eab727f82848 | -10.02736 | -48.69966 | 2025-05-16 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4e8583e-87f4-3762-8724-58dd4a451d9f | -10.14255 | -53.64021 | 2025-05-16 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b33a23bd-67aa-3d5f-b2bb-5456546db870 | -6.61893 | -48.00694 | 2025-05-16 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92700400-6110-349a-ac5b-14faa4190e30 | -11.7861 | -47.35196 | 2025-05-16 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cc996a4-d6c0-3057-a8c6-a4bc087f8b2e | -14.17627 | -45.46671 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d18f8dc-666b-363f-ab9d-fc5a88b495ca | -13.28398 | -45.42601 | 2025-05-16 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 429da116-3c21-38ad-9d5b-e2ed326c3b33 | -17.66183 | -46.68355 | 2025-05-16 04:36:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44d925c5-05be-362b-bb9a-ae109023652c | -13.79856 | -53.29974 | 2025-05-16 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3aceb44-4058-3e95-9abc-a0e1db048e8c | -14.01429 | -55.1209 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 193c9653-cb5c-3e69-b5a4-52308d5c71d0 | -13.04901 | -53.71684 | 2025-05-16 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd66220b-0797-3e04-9ae1-a4fa71fc8f18 | -11.41771 | -54.33133 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c35839e5-e41e-38df-8c9b-6e8328c4fcdd | -11.4218 | -54.33205 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e2e0659-2173-39c1-afcd-1418694d3806 | -13.29447 | -47.22964 | 2025-05-16 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca059808-e5bc-3000-85d5-be15eb9e4a36 | -11.55415 | -47.61111 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e3e8958-1a73-3019-9897-d53a3c6546a8 | -10.39059 | -57.54068 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0c7b79f-49d3-3fa4-9a38-d1f9287c14ce | -13.04517 | -53.7161 | 2025-05-16 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80e9bd2b-2038-3100-9bd4-9b74c25dcada | -14.01919 | -55.14116 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 897eed58-5f86-3dc4-a7b4-a56230beebc1 | -11.91807 | -54.40443 | 2025-05-16 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97549f27-f7d6-379f-b5bb-44029f27180b | -12.12221 | -54.66094 | 2025-05-16 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 929cf5bc-dd79-330d-89bc-8609b39e4559 | -14.17421 | -45.48117 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 216e287b-9622-31bc-84a2-9158bc025f2a | -13.57307 | -52.8697 | 2025-05-16 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88d0dbe1-a101-392f-b637-61aed017d5e3 | -13.39237 | -48.44865 | 2025-05-16 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48653018-c74d-32e9-8962-8c655269cc36 | -11.56635 | -47.87724 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f9cdfb9-cde6-35e9-89d8-40308c4e02cf | -11.42653 | -54.3291 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5185e22-d17c-304b-956b-54b65c73d0d3 | -12.12287 | -54.6572 | 2025-05-16 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87308052-e6d3-3150-9c53-b0fff0f1e4eb | -17.24867 | -48.10998 | 2025-05-16 04:36:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4f29f0c-41f3-32be-b0a6-b225e0a74d91 | -12.34682 | -49.95581 | 2025-05-16 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e0dae98-73ae-30db-8f83-5f4476b70c34 | -11.57224 | -47.60648 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d13ee61c-5600-39d8-b4cb-96d98ac17307 | -12.87322 | -55.05747 | 2025-05-16 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa5ffa3a-cc25-35db-aace-3cc266e47510 | -14.17106 | -45.4758 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 151477e3-eb53-3ea2-8000-c6027fb83c4e | -12.26373 | -49.31278 | 2025-05-16 04:36:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a54ddba-4174-36cf-9668-9cde78df87ae | -11.41836 | -54.32761 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef6fa0f7-6c80-3cc5-a08c-970e41aacc31 | -14.1686 | -45.46559 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4f4cf2a-2c1d-3c90-878c-ef3568189725 | -15.78353 | -54.51789 | 2025-05-16 04:36:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32865291-4632-3021-b427-88a8e94ee0cc | -11.61039 | -48.01754 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 956dcd13-521b-31fb-8d2a-217c5e5a39bc | -14.17746 | -45.47356 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dce2c822-8616-34e2-9734-5d4e358221cb | -11.388 | -57.81886 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a766203e-fed0-314d-8a5a-f00655481b2a | -11.628 | -48.47391 | 2025-05-16 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bab28b7-9873-35d5-8f3c-baaf9d583e3a | -15.26307 | -51.46584 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c355afa-bf3a-3b90-b37c-8eb8797a4261 | -11.92214 | -54.40515 | 2025-05-16 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a989d30d-e877-350f-84ac-fde35e21fb03 | -12.86903 | -55.05671 | 2025-05-16 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a08f361-6366-39f0-a0c6-6309fc6f8c3e | -12.36958 | -47.3233 | 2025-05-16 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f2bbb52-fc35-3b32-bc05-1b8d0ada809d | -13.57212 | -52.87179 | 2025-05-16 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 630e9238-6499-3487-8fca-2d78ecef7464 | -16.83302 | -48.81318 | 2025-05-16 04:36:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b87db985-ce74-3c80-a33b-c4a961cd9444 | -14.1768 | -45.47839 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27f9a884-83ee-3b0b-a4b2-76d005facd7a | -13.67182 | -53.94331 | 2025-05-16 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75bc2bce-6cf4-3a61-95a8-fd47e09e1fb1 | -15.00316 | -48.81807 | 2025-05-16 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff80669d-17fe-3d72-9dae-53b4a0e79698 | -13.39966 | -47.50692 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ede8b18-b1b5-374b-8047-bfb01a1a0593 | -13.16366 | -53.27749 | 2025-05-16 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a3c2d03-3de5-326a-98de-c7e9cbd1a8c8 | -17.8838 | -43.99234 | 2025-05-16 04:36:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b0ab49b-bb78-35fb-9497-317e06cbc67a | -17.66494 | -46.68156 | 2025-05-16 04:36:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f74970c-9eb4-364e-b8bb-a18975b4f411 | -11.63619 | -48.02903 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e649ccfe-ff27-32e4-a387-75b6aafb7d9b | -14.01574 | -55.13663 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77f9a7e1-43e1-3bcf-8a17-f541681a26e0 | -13.59112 | -47.38148 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d619e146-1d78-3448-90b4-cd9e0d464c3e | -11.66474 | -54.94697 | 2025-05-16 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a86097a-6ed2-3852-ab6e-f70d2072266a | -11.66403 | -54.95096 | 2025-05-16 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87b3f65e-0413-35f8-b78a-8c74a2d6af20 | -14.87337 | -51.9827 | 2025-05-16 04:36:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 194357a6-14d0-35e0-bfa5-04024d154180 | -11.57735 | -47.61852 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c877d784-d341-36ee-8816-143965d77133 | -14.17998 | -45.48378 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd159a2a-3039-39d0-ad8c-2a0c195faac3 | -14.87402 | -51.97882 | 2025-05-16 04:36:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1d02216-3f23-37a0-b2e7-b34d81c7831f | -14.02331 | -55.14193 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 675594ba-2cdc-3b27-9f32-19deb4409338 | -12.34959 | -49.95994 | 2025-05-16 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f5ce387-24ed-3b12-b99f-661dcf484a5d | -12.45849 | -57.20803 | 2025-05-16 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd1d9362-c05a-3d42-aaf1-11302471652c | -13.30137 | -47.20695 | 2025-05-16 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5076bb8-9837-3566-b566-02328b83e452 | -14.01034 | -53.04232 | 2025-05-16 04:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecbb62d0-c354-36e7-be60-e25e0023d97c | -11.96927 | -63.52084 | 2025-05-16 04:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95436f5d-b3f1-3268-8d3f-47e34c52de37 | -15.26708 | -51.4627 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9092922-5aea-398b-9732-4f6604a73a42 | -13.67507 | -47.96585 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47ad154d-ff6a-3259-a603-37c7f0213c27 | -14.01774 | -55.12539 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b7fe0a0-d2cb-3c87-adb2-224761092c1b | -11.58018 | -47.62273 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f68a3b7-adf9-3214-97b5-97fc408106f4 | -15.07783 | -48.94569 | 2025-05-16 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de3a0616-8797-3187-93e2-cec063b9bd51 | -14.01506 | -55.1404 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cedeeeb0-4a33-38a6-887d-98ea08645b8a | -11.55303 | -47.61843 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29631c65-376e-32f8-aac8-fd91f119c557 | -14.47207 | -56.32111 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f691f9b7-76c3-328e-ad23-4913fbe3a46f | -14.18187 | -45.48231 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7376916-da99-3e06-a141-fb5b7bfb0029 | -11.91742 | -54.40807 | 2025-05-16 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d4e688-d372-37b6-9fab-b09e54127e4c | -11.4231 | -54.32465 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26d50d29-6669-342f-9e41-7269bf0368bc | -13.67344 | -47.16198 | 2025-05-16 04:36:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7a8d83e9-0708-3cb7-9d90-b428d0fa3097 | -12.45364 | -57.20705 | 2025-05-16 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c199620-330e-3b7d-afa5-df7ca2760e73 | -14.33162 | -47.50729 | 2025-05-16 04:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eea5c8c-00fc-3134-aa2f-7f3c76fdbc34 | -15.26585 | -51.47017 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eec34061-2a30-326f-8b3e-47fea2ae9f9b | -14.47123 | -56.32555 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f279bfc9-e0db-33ff-ba3d-2de2abcb57dc | -13.59229 | -47.37348 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f5d37aa-7ab9-3696-9b48-63851099c7bd | -13.96193 | -56.79836 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a12a9dd-baa2-3cfd-93e7-ec2a2e30a7f3 | -11.70591 | -48.3477 | 2025-05-16 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ecd9c53-00ec-3457-a6ca-f3a12ece17eb | -13.61943 | -54.88098 | 2025-05-16 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7db64ee7-a729-3d04-8c09-eaf20fe86114 | -12.29363 | -52.46948 | 2025-05-16 04:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da873163-5f19-3302-9fc3-71582ca1f323 | -11.63087 | -54.94068 | 2025-05-16 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ae0e929-6145-3a1e-8d10-fcec338b4f11 | -11.6605 | -54.94619 | 2025-05-16 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae148e39-8ae9-31cb-8b1a-c4f0a08a4b54 | -14.17735 | -45.48655 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 026efd6b-7bd6-3052-8426-49c9b86f6784 | -11.51613 | -48.58048 | 2025-05-16 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 472c1bd2-085c-3241-9ac3-1433e9d73dea | -12.62445 | -54.87127 | 2025-05-16 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 367ded13-1af9-3e10-900c-7819eac0a3d7 | -11.58096 | -47.87209 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8755b649-16f2-301e-a957-1c347dfc0404 | -11.57508 | -47.61065 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 232794f5-a1a1-3a85-99ef-7adbec29b608 | -14.17232 | -45.48263 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2b10e26-8580-3689-9c16-b9642518ffe7 | -13.96092 | -56.78654 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fa8a72d-0883-35ee-9427-a17c977deb11 | -13.95914 | -56.78798 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 481c0051-1a3e-3773-b3ed-28b0ec986a52 | -12.3429 | -49.95884 | 2025-05-16 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4df3ccd2-6580-3561-8cd9-c06e24bfbbc5 | -14.17175 | -45.47098 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README8.md)
