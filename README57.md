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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b52a6f8-66c5-326b-9d82-f88c8b56003b | -1.20274 | -51.77898 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fed93f2e-21d1-3f64-8d2d-c1103740fef4 | -2.72395 | -53.19442 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0e0dad0-7364-3fed-bed9-1db4766b75a7 | -3.11324 | -51.32627 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 699041eb-c061-394f-8ac6-923cdce67b1b | -3.62626 | -50.22145 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c85f7b58-3ae1-3c42-8787-8dbc80cd1700 | -4.37561 | -48.08455 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b62487e-21de-3a20-aeca-08938f732c1f | -2.60675 | -47.55814 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5b3a8e6-8a73-3834-a1f7-72f96ec90045 | -3.51276 | -51.66626 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9daefb7-75db-30a3-b441-630bac08978b | -0.89474 | -51.72343 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f121b2b-a37d-39a1-861c-91bbb4cbec3c | -2.70921 | -53.1749 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c79f7e77-202b-3d2a-8237-9368e56aab62 | -2.22749 | -46.81546 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5739f53e-193b-3285-8d32-2e034ee4e856 | -1.99928 | -46.58261 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d821aa95-c3a8-3f8a-9d66-0add47e49168 | -1.69019 | -50.20033 | 2024-11-17 04:29:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef1ca22e-0c3b-3840-9070-08999f213cd2 | -2.33619 | -49.112 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74aba603-c06b-3c62-8aa1-c0554cfa369f | -4.09555 | -47.81333 | 2024-11-17 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f259e33-b512-3a12-9c11-8020d374c659 | -2.10666 | -48.25491 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb38b71-aa5b-309d-b605-88bafa1c2490 | -2.14201 | -49.14444 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 596d6862-706c-38be-b0ec-e0b789cfa8eb | -2.10916 | -46.42361 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18625f04-5e10-3fca-95eb-ed544e8b16d7 | -2.07619 | -48.52295 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45860ae7-2605-33f6-93f0-c186647f48a8 | -3.69053 | -50.10985 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c33426b-1e90-3251-b576-ce3784e0279e | -3.13726 | -44.04237 | 2024-11-17 04:29:00 | NOAA-20 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bf823bb-50cb-32c7-a7c4-498503e620cd | -3.09956 | -45.97869 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e1dae5b-933c-329c-8a71-cbaf67f56319 | -2.60323 | -47.73139 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0c06fcd-bfd8-379e-a18d-86ee6a5d03c3 | -1.29513 | -51.95996 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ed1a7391-d326-3e06-93de-b34f16479791 | -4.0709 | -46.86756 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4443fb37-b914-328d-a0e6-72af7ad7034b | -6.17387 | -41.16801 | 2024-11-17 04:29:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e5621be-6e25-3619-94cc-986ecd5b8146 | -2.70984 | -47.97992 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cebf82f9-a4ad-313c-9738-081158d2eab8 | -1.01587 | -47.75504 | 2024-11-17 04:29:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d6ade6-ad33-344f-9fa5-7bf09678f50b | -1.99705 | -46.57523 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 399c529b-92ca-3efb-bf80-3fd10e3785f7 | -2.59241 | -47.56298 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a70662f2-546b-33fc-8c26-e06abc228f28 | -2.65319 | -46.16078 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3d5bd7-16f6-392c-a0f9-355da8e2a14c | -4.74127 | -48.11398 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a260f7fb-b294-36e0-a2e0-1beff75fed11 | -3.88901 | -46.61988 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a2a0a4d-d151-3ae8-bab7-c8fde0e44179 | -17.6059 | -57.5921 | 2024-11-17 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| db4c5728-cbf7-3d6a-8a57-fa3df7c793e6 | -3.5124 | -50.2553 | 2024-11-17 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 291c5fac-9242-323d-8ac7-523fe82b0f06 | -4.5616 | -47.9925 | 2024-11-17 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 20831eaf-66eb-3404-bc6f-0e304418223f | -3.5494 | -50.254 | 2024-11-17 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ef33b130-5de9-30e4-ba4d-a260e653c065 | -2.5802 | -47.571 | 2024-11-17 04:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 01f73cab-2751-3ece-8b9e-a2e5a88d91d1 | -2.6322 | -48.5634 | 2024-11-17 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a9ea294e-5028-3d1e-afa4-b80687fc8bcf | 0.6159 | -51.7676 | 2024-11-17 04:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 72721784-b694-3bb7-be60-e70f114d6a3f | -3.531 | -50.2337 | 2024-11-17 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 199c1f03-b39c-3521-8c83-54e4151e911c | -17.6256 | -57.5897 | 2024-11-17 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 189dbe38-6ec3-33fd-abd0-d627da672592 | -17.6063 | -57.5715 | 2024-11-17 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 5f5d633d-1127-3f60-9571-9fd12d2a93d4 | -2.6137 | -48.5639 | 2024-11-17 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 13778037-846c-3e91-b8ee-855ac48edb13 | -3.5309 | -50.2547 | 2024-11-17 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 66bfd314-cdd4-30f9-a9ed-895862e48b2d | -3.5678 | -50.2534 | 2024-11-17 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 0b7c0d8d-768e-3e1f-8ca1-1574b09c5dc0 | -4.5614 | -48.0141 | 2024-11-17 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4c0e9fe1-2cdd-35df-a838-8dbfa6ed068d | -17.626 | -57.5692 | 2024-11-17 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 8ae31fab-ec66-3646-b98c-2f9d8be58af7 | -17.5862 | -57.5944 | 2024-11-17 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| dab633a7-7b9e-3811-b1f3-aecf2e565598 | -12.55271 | -57.77607 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6570a320-bc85-32a9-8766-ff39d5748d44 | -11.18064 | -44.62041 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7450f0ea-1290-3f5a-8b72-6c6c45a95fdd | -9.93338 | -49.09911 | 2024-11-17 04:31:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d845b8ea-8a39-3b67-9153-7ae29f32e2b5 | -12.43971 | -43.79885 | 2024-11-17 04:31:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28d43f76-3e19-3b41-8cc9-512815aac547 | -8.44569 | -44.19998 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5da215da-7501-3576-af7a-966950c6cd02 | -11.18448 | -44.62099 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b84f7997-4801-3676-aa59-0241c7273281 | -12.3941 | -57.52352 | 2024-11-17 04:31:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0cd6a511-b203-32a3-b3e5-894829e5dc47 | -12.54769 | -57.77508 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d3541c3-2575-3666-8884-a6c97c3daca7 | -8.13071 | -41.12979 | 2024-11-17 04:31:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| cfb2fb86-5546-3a64-9a4a-2b493c243ffc | -7.08991 | -49.30534 | 2024-11-17 04:31:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a13933b-285a-3e8e-8bf2-eaf1cf392610 | -10.66127 | -44.50011 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f389a358-a7d0-3610-8ca4-bfd4d2a18cad | -12.39055 | -57.51765 | 2024-11-17 04:31:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c513754-267a-3efd-b747-67ee123c171e | -10.95393 | -40.73764 | 2024-11-17 04:31:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 339f34d6-d33b-3e3c-9e0a-0e1d65838c53 | -10.6658 | -44.49583 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f9074a86-5165-3295-853a-78af43f8b33c | -10.54381 | -44.67454 | 2024-11-17 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15f45247-8947-348f-9cd4-0be1e479af28 | -12.56367 | -57.82758 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c340d0cd-5099-34b4-8a8d-ce5f9137ff78 | -10.99654 | -49.35769 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8750ab13-d734-3fea-be53-7d57a39843b5 | -12.44021 | -43.79509 | 2024-11-17 04:31:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4fb34c8-e9ee-3215-bfcd-314a8136257b | -11.85334 | -46.93444 | 2024-11-17 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 078d0ad5-0c97-3384-9517-4b1ee3f64142 | -10.98935 | -49.36013 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 213f3e9f-677b-3173-a79b-b55d43576933 | -10.81591 | -44.92962 | 2024-11-17 04:31:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9db7d3f-9a20-3669-80f3-9a1ca6176f05 | -7.47624 | -47.1811 | 2024-11-17 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cd1586d-5130-3801-9c25-8221a9943d28 | -8.27593 | -45.96765 | 2024-11-17 04:31:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da8d7641-d0a9-3bb1-a1e5-f4ad94d7b0f8 | -8.4412 | -44.20413 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64137673-f22d-3cfe-91fb-15eedcab32b1 | -10.54001 | -44.67398 | 2024-11-17 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 360663bb-0ff2-36a0-b48f-4e16110cf0b3 | -12.27381 | -44.99088 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f991de9-5289-3399-a24c-dd7bd88c9703 | -9.94178 | -48.96069 | 2024-11-17 04:31:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71d99c6b-5c4a-3302-9e62-6c5fa00f813e | -10.8358 | -42.73236 | 2024-11-17 04:31:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c8a2bc17-f9ed-309c-a104-b5cb033cfa14 | -7.09433 | -49.32071 | 2024-11-17 04:31:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8ea7b4cc-6274-3c01-acc9-569dba423ed1 | -8.43672 | -44.20824 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 57d2c8d9-378f-3a58-ac0b-947ca8971d55 | -9.8694 | -47.53048 | 2024-11-17 04:31:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82b41c7a-1513-31c5-b698-2fb54a64fd4b | -12.26997 | -44.99054 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1726114c-9c57-3cb8-86a5-4866f72fc3ed | -7.47291 | -47.18058 | 2024-11-17 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6353eed7-0e62-356d-a307-0bf9955adf05 | -8.2765 | -45.96384 | 2024-11-17 04:31:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2eac767f-9a86-3932-a273-87d9fe31eb5a | -8.44326 | -44.19008 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6977a0f8-4965-377b-89d6-1420a9056a45 | -12.27507 | -44.9889 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39585970-7013-3c27-a1aa-6bba17f91176 | -8.27997 | -45.96438 | 2024-11-17 04:31:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7e3d05e-30ce-31cd-953b-ace3451dd5f8 | -10.37918 | -44.87856 | 2024-11-17 04:31:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 765e7351-6275-30a3-a0e8-b19ec9e4c657 | -7.42338 | -47.8685 | 2024-11-17 04:31:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 781b6eae-1805-300e-9dd8-5befaaddf7db | -12.2668 | -44.98537 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f14a844c-c9a1-32db-9bef-c24f775aff6a | -7.09385 | -49.30229 | 2024-11-17 04:31:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b731980-80a0-3044-9cc3-e0be5fe55014 | -8.445 | -44.20465 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e5ee5a1-2849-3344-bffa-2f625a652207 | -9.85078 | -48.56765 | 2024-11-17 04:31:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5b0607e-d301-30a0-ab40-f99e3dcbff4e | -8.44257 | -44.19476 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 065cd29d-3985-3774-a0ad-8e734b6666e8 | -9.86271 | -47.52944 | 2024-11-17 04:31:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70485a67-4364-3e6a-9ea6-978f5a30449a | -7.13303 | -46.63741 | 2024-11-17 04:31:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2c87ada-7f03-3c0a-8c82-e39d1fe79ddf | -8.43604 | -44.21287 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9eecdf7f-317b-3f96-8081-31115b19b253 | -11.16102 | -45.10462 | 2024-11-17 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98fe282f-3cc3-30ed-933b-48a1a51345ef | -11.56926 | -46.00632 | 2024-11-17 04:31:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c1bd1b6-96d4-33eb-8c07-63fd01db7477 | -12.44156 | -43.79601 | 2024-11-17 04:31:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40f8dabe-7655-3658-84e0-a5e1802cbe68 | -8.4495 | -44.20047 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e840a818-8d75-3ded-a28c-8b1abe5ead81 | -8.43877 | -44.19422 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README58.md)
