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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 131fb68f-cd1c-305f-a995-975b40cd053e | -13.47138 | -47.23325 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9811db99-d47c-38ae-b5ad-0086ac4a71fe | -11.90688 | -46.31684 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47e30116-364d-3ad9-a150-1a51339feeec | -13.38218 | -47.28214 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e65d51f8-19ba-3f61-9bbc-7c7a25462f8f | -12.68235 | -46.85021 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6c56fe0-1a58-3e46-9cce-dedf8402aa50 | -13.30932 | -47.25217 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c3a80d7-f1e8-3c01-8542-9ed28dc2ce04 | -8.33351 | -46.22365 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5a9f7da-74ec-3ac3-af24-a7db49a68b1d | -15.32767 | -45.05782 | 2025-10-03 03:45:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a496abb-69fb-3c1c-875f-5ebfb6cd977e | -15.92547 | -43.30342 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f754d0f3-4790-3395-a37f-5512ee083b28 | -12.92379 | -46.37514 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecbeaf59-de66-3d8a-8ce4-f4258fba81dd | -11.01709 | -46.54998 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66fbbee7-ce1e-3175-b15b-b0ab6495e374 | -10.8334 | -41.27622 | 2025-10-03 03:45:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cae6c672-91b9-3272-aae8-fcad4702505a | -14.35864 | -43.84581 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6765aed0-5aec-3d30-bc9c-3084b4870139 | -13.74381 | -47.99385 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 497c335b-322a-3625-bf87-8aa3b1309481 | -11.12157 | -43.38975 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1b54bad-657b-377d-9a79-215d9043352e | -9.9484 | -43.73308 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0946d6b3-5dc4-3ff2-b38b-7cbb9aaa3e62 | -15.78335 | -43.69849 | 2025-10-03 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 391b3e14-3107-3df7-9cb9-ef75c252f9d7 | -10.87839 | -47.8255 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de2b0855-31a2-3597-8cea-97a8dfbac542 | -9.9239 | -43.73205 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df5e6cb3-5d40-3e4d-ac19-bd325080c1b8 | -13.19792 | -47.83489 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b07d86d2-0200-3752-8914-7cf145aab57f | -15.60751 | -46.92826 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ee487b1-0920-39bd-93d4-93a47732c03a | -12.60609 | -47.00168 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c93ab4ee-2c33-3f7e-b6ce-8b9f6d69c33f | -14.87839 | -48.33341 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc857828-5307-39aa-81aa-ce3eb8c881cf | -12.38531 | -46.52846 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 956a2850-9964-38d9-9a27-c542373f5039 | -14.41628 | -46.16163 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0760b7d6-e35f-3100-8ee6-501031c4ec49 | -11.34939 | -44.96598 | 2025-10-03 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33288981-abd3-3d83-bebc-ed346945ead3 | -12.38135 | -46.51951 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fafd060-4b1c-3d6a-815c-89a2cb178d3c | -15.34388 | -47.8321 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da456c98-3bc5-39da-b95a-8eb7316113e9 | -11.91377 | -46.28075 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| be194905-57d1-3cf2-9036-0794b3c771fc | -12.64159 | -46.96993 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1b6a3391-f941-3a4a-bcfa-bdacdc31c1b2 | -11.00817 | -46.64309 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0635ee77-88eb-3d2c-91e0-363701bf15cb | -15.66403 | -44.49899 | 2025-10-03 03:45:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 591483c1-edae-3846-a128-b8f67901f6c9 | -8.71553 | -47.13403 | 2025-10-03 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09af93e5-4b17-378b-a29d-ea8923af3627 | -12.61508 | -46.98581 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cffb90d1-324a-35f1-b87d-2e00a9e0397f | -9.77104 | -46.21619 | 2025-10-03 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cd7597e-df02-3098-83ab-800d6459e33b | -11.86829 | -45.03825 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6d5a041-c25b-3ddb-9fd5-f2302be60d81 | -15.11695 | -46.68341 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7abd061-3aaf-3050-b0fa-f6998f802fd5 | -13.57901 | -47.58677 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6b3f211-cc16-3dc3-8e16-8d44c0cd8aaa | -12.86208 | -46.99818 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0216029-932f-3ae3-86c0-2ba5e7fff18f | -10.34815 | -43.73177 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3194932a-50b6-3dc7-9ed2-2c2ccff4681f | -13.47639 | -47.23746 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79bdd2fc-41a4-3cc3-a66e-03e0343184e0 | -10.83876 | -46.59521 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0abc2ec7-65de-3b66-abdb-a6aef71e9f7c | -13.29913 | -47.83912 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0c7327a-ce83-3562-81a0-cd019c618f2e | -14.21427 | -44.95244 | 2025-10-03 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9af509f7-8db7-3948-ae7e-a92a9d8b930c | -9.93528 | -43.58374 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 670cd414-5849-3d68-a1b9-a2c610f3e7f6 | -14.69425 | -45.18313 | 2025-10-03 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9a6f8ba-9be6-3635-bdba-e8439e078bb8 | -10.79979 | -44.242 | 2025-10-03 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c507c0e3-0236-341f-a1be-1e5cdd8242be | -14.29652 | -46.02649 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25b6980a-512c-3222-985a-a91020c3e5ff | -15.22478 | -47.18541 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62799359-d76a-3cb9-8acc-168751d74590 | -13.29254 | -47.18969 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae229766-3890-3941-9898-cdb2e74612ed | -13.26499 | -47.25534 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b1edd272-1b58-38ed-84d5-fcbf37bf4c32 | -13.26279 | -47.24937 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 126eff69-00eb-3805-84e2-8b8893e13fed | -9.91207 | -43.74289 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 30af8259-4a50-3137-9baf-73ef462b3fe9 | -9.7119 | -45.43697 | 2025-10-03 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e387234-9d42-3281-9c26-4372377b5067 | -13.5574 | -47.30161 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 342a98b6-2097-384b-b717-60693d5c6b4e | -8.89794 | -46.60429 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74673f8a-1938-3305-80b3-adbbd96f839e | -10.25216 | -44.94398 | 2025-10-03 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32037b61-44d9-36b6-ad84-c449fd64ffb3 | -14.37773 | -45.93731 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84d38f82-a5ac-36a0-bf5b-fe9c12f2ec5e | -14.57191 | -48.33274 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df1df1ab-714a-3ca8-9506-f16bdcb6d447 | -15.0822 | -42.11751 | 2025-10-03 03:45:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c1261d1d-7b28-3e59-8037-0228a03095f0 | -9.91053 | -43.72405 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| e6c1ab1b-6e1c-3f41-b258-d76eaa341bee | -13.76392 | -48.06553 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2aa3e178-3fc9-300d-9a1b-66ebb2e6e948 | -13.48015 | -47.2478 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15f65b1b-0650-378a-b993-998c80357be3 | -13.26854 | -47.25007 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7fea45bd-a0c2-32ff-8e26-ea15289ab272 | -14.98348 | -46.8583 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d4dc32e-677c-3c39-88f7-f128baa3101c | -11.63105 | -45.06108 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85a0cc96-85bc-329a-85eb-191c3a56708d | -13.97812 | -48.16709 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65ed9086-b539-3e7d-b402-faac369dee4c | -15.91804 | -43.34372 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1b7df1b7-cf9b-3134-bf52-14046992bcd7 | -13.32607 | -47.79641 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8e5f118-9548-3bce-82bd-f111b2249d1a | -13.77884 | -47.55315 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ac767b70-493e-36f8-8126-41ba4e3a7b95 | -14.62411 | -48.24768 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 849ff5bd-5b50-30c2-8205-3d7330881295 | -13.51422 | -47.25335 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fa30af9-11d7-3b98-b2db-f62b1a4f0b33 | -10.86298 | -45.41623 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45393309-24fc-3194-b0ac-a3dba5392c86 | -14.30228 | -46.02438 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ba0f5b0-6ac5-369b-941f-f52a8ebee2d3 | -11.62082 | -45.03238 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 760aa03b-4a56-32ae-98a7-d1e0717bcb1d | -12.75892 | -44.90255 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6d3b471d-50fd-3ec7-b035-3b64234b0778 | -15.1751 | -43.62877 | 2025-10-03 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 02a17b65-d35d-392e-91c5-09d5910e7d35 | -14.58003 | -48.34103 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 868aae54-6739-33b6-8623-4f3688556b67 | -14.93919 | -46.89901 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 362b6c59-acf6-3515-a31e-1e934c1bd412 | -13.79618 | -47.58508 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 57437cb6-6090-3016-859f-f7fab4054de4 | -13.26948 | -47.26248 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e2354aa-f81b-37c1-a897-2e59b23e3556 | -13.34076 | -48.10577 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e871bb1a-85fe-380c-ba73-49b8620604a0 | -14.8685 | -48.31286 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 200c33cc-3338-38f4-a596-d82004616a20 | -13.47894 | -47.23885 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9ff5fcd-c224-3f4a-846f-39fad4140a9a | -14.32192 | -45.87085 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 452bf994-529d-3fab-9f10-ec2d4041e1db | -10.3425 | -43.73605 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce48379e-8a2d-3851-8f0c-321e9098c71f | -11.14519 | -43.41608 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9397081b-4846-3531-930c-3dcfb0f3552e | -11.92644 | -46.27876 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 2568e99a-6d7e-352a-841f-2bdab156f000 | -10.77259 | -46.60246 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a5c2259-d992-3ffe-98fd-69c57f41b2a0 | -14.98416 | -46.85493 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c3fe744-1300-394f-9858-fb4ed7544b91 | -15.65012 | -46.25497 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e92808a-6ec5-38b3-9637-1724595f809f | -12.6142 | -46.96064 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c810342f-3067-3a45-906c-e21aa9b4c161 | -14.88152 | -48.3093 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7457541c-d93b-350d-a864-2b81e2926b0f | -12.6077 | -46.99355 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af2ef5fc-212e-38e6-9ad7-f335f0d8339b | -15.21366 | -47.18438 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ec388fb-a703-3a4a-8827-355cb50d5620 | -13.14325 | -47.89253 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca507a29-d837-30dc-82b0-0730cb65d13e | -14.669 | -48.08964 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bc818390-9ca1-347b-a111-1ed073d0f7b4 | -11.43402 | -43.4923 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc58f4ab-1626-31af-854e-4eddee3d4029 | -10.82168 | -46.59231 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3d562de-083f-3ab7-b865-74c018058bc8 | -13.7648 | -48.06126 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 570bb402-1bb3-3e30-b2f1-3dd1f83f375c | -15.94759 | -46.22547 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README31.md)
