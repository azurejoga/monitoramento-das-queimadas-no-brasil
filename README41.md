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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29fc6db6-d186-3284-85ab-f4fb6596e61d | -11.9153 | -46.3781 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6bf524c9-f1a0-39f0-8c6a-239ea1b7c602 | -16.35637 | -49.40108 | 2025-10-04 03:53:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d185144-b915-3d99-b3bd-4f5ca81ffc66 | -13.88724 | -46.51396 | 2025-10-04 03:53:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3f708bfc-abee-3e26-975e-f20e6e88b4eb | -14.70368 | -48.19842 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b29db4d-aba1-369b-8f37-d77b5548d38a | -12.72494 | -48.56295 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b5ea502-6643-3d34-8df0-e5ee4cd79f23 | -13.64314 | -48.67487 | 2025-10-04 03:53:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1635f36f-639f-3914-89e9-09c29c24cc98 | -11.92067 | -46.34966 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef75a0f2-29c2-334e-aa73-1105e5bae4f0 | -16.0069 | -50.92912 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55c87874-37bb-3899-8556-fbf0c9a2531f | -12.36657 | -46.51704 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3feebe82-3d27-3a7b-aecb-ed8aa09a0e93 | -13.50354 | -47.27372 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a234d4b-1ea6-3e38-aef4-30682bdedf00 | -13.38844 | -47.28158 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc9fcbf0-cddb-3fd7-9f65-013bec931140 | -13.13055 | -47.82664 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f28274c-a0ee-3ffe-888b-bb04b8a6d48c | -15.76232 | -47.77222 | 2025-10-04 03:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b87e83ad-82f7-3bd6-869b-090565ce49a5 | -13.21869 | -47.84053 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd43402b-f3fb-3efa-ab86-4d7b2f9f0793 | -14.66306 | -48.31714 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5aedf2f8-20ab-3b9f-af37-554c119d5ded | -11.91546 | -46.74075 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61aa4ddc-a18a-304f-aaf7-5e468f79437b | -17.16143 | -47.02227 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6065354b-e220-304b-bfe1-748c61adf125 | -12.6559 | -46.96891 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6afeab2-432d-3393-aa0e-062d1a1fc1fa | -15.69747 | -46.27215 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdeecca5-ed91-3e50-b92d-e7f6183bf12f | -14.45807 | -46.3413 | 2025-10-04 03:53:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff7154cc-4a70-3a07-8d75-683d54df5f13 | -14.43398 | -46.15857 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 063450ab-c19d-393a-b727-ceda5a8520ac | -16.75761 | -43.96093 | 2025-10-04 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91c4fa9b-5b12-30f3-a5d7-5b18cdbe40fc | -15.60381 | -52.49587 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0bf4394-41c4-3755-9c5e-0463b3b8699f | -13.32064 | -48.12711 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45cca0ca-7ca1-37b0-8f13-ec60436062b5 | -14.94205 | -49.97426 | 2025-10-04 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c7ab851a-7ce8-3245-b042-97b851f6c541 | -11.99693 | -47.19765 | 2025-10-04 03:53:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bebf3104-223c-3af1-899d-d11379731cbe | -16.02045 | -44.28426 | 2025-10-04 03:53:00 | NPP-375D | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 863ee2b8-fa87-3e71-a054-460e59e68d5e | -17.63625 | -44.45652 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5538f2ae-36d3-3eae-9428-0c5220e0d219 | -12.08125 | -45.18367 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbbb7c61-c4a2-377c-ac83-6ba3b163cbd4 | -12.71261 | -48.56574 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcb6055a-2d03-3731-aa80-2fc9c45cbc4c | -17.08272 | -46.25121 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0eae4ce-fd58-3471-b80f-aca10c31a2bb | -12.64072 | -46.99239 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fb29462-67c7-3fbb-9b4b-ae27b4092705 | -13.78094 | -47.81437 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f820eee-2300-3337-b32e-480ea0c34c59 | -13.29489 | -47.59516 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35d992a9-004c-3606-bcf5-afcc3aee9dc2 | -14.459 | -46.33641 | 2025-10-04 03:53:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cec471e-68b6-344c-b08c-88e96ecb7ca7 | -13.2568 | -47.23957 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f1fd3b3-8ce6-37a4-8ad1-d577b57d29e0 | -13.10945 | -47.93301 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 086b471d-8860-3f38-9514-53dbf47d0171 | -11.51189 | -46.7412 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45c44dc4-8a1a-329b-80f1-ccbb9b78ebf7 | -13.1165 | -47.84119 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5e6d6f6-198a-31c2-ad03-e81b71e5e0a4 | -12.02584 | -45.20546 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 0b4936bb-dfd1-32b0-b5a3-9dd8aa4da470 | -14.22633 | -46.0863 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1c57db0-7ed0-380c-98fe-b2f858e1d46d | -13.97403 | -48.18249 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3649333d-103a-3998-8532-254c251e8588 | -11.91843 | -46.36154 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f2e00b14-2b42-3dbb-b393-aae97bc646cc | -14.69894 | -48.19435 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbd22c7f-52e7-3c79-a578-855a01b00dbf | -11.92241 | -46.36782 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d80df1b2-a13e-3da6-aa88-b831da092904 | -13.10119 | -47.88152 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3030e4d-2ae1-377f-9bdc-cb07d556bd80 | -14.19533 | -46.66755 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dffe9f9-0782-33bf-8342-51a44603226f | -11.84865 | -45.04478 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82942a97-fb63-3315-9fbc-845057e2a96a | -13.21118 | -47.82238 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1796461a-85c1-3892-8802-3748202a358e | -14.65353 | -48.30885 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a23c143c-d968-37f0-96fb-ce8e1db6c6f1 | -14.22106 | -46.0631 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6d1a062-bd67-3b05-8cf1-1fed48ff85ec | -12.91677 | -46.79156 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 187fa782-e398-3b1b-bd4d-35340cd21eb6 | -14.24124 | -46.11029 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6498519f-249e-3710-9273-21f02ab102a3 | -11.9208 | -46.40384 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 543367e5-799a-3ef1-9bf7-e6c01c1db829 | -13.1255 | -47.93705 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2f3a52e-c413-30d1-821c-4840f6442fea | -14.93793 | -49.97452 | 2025-10-04 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb67f7f3-7bf4-380a-b716-7134d06b3040 | -15.67691 | -44.51122 | 2025-10-04 03:53:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d84a8e2b-ae7f-3dbb-87d6-a30f2c57af60 | -11.82415 | -45.04944 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fe4b3a9-8a50-39c6-98a9-296d3043184f | -17.028 | -43.43665 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08fa8fb6-48e2-34b9-86d1-72bb5e223348 | -17.96478 | -44.39536 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00d73385-313c-356c-8f29-06f9722f43b8 | -11.85326 | -45.04543 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662614f0-a74d-3f63-8ec7-cdf48e1d1c91 | -13.32567 | -47.57756 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 37cd6d8f-f362-3c4a-9e90-b8b183bed0bb | -13.66194 | -47.29619 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fb67d2f-5306-3e90-a22d-19ee2addb3d3 | -12.8122 | -46.85384 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 465e4344-2397-3b6d-84bf-739e5039ee36 | -14.59919 | -46.72458 | 2025-10-04 03:53:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 676a9e43-f012-3f8b-816a-8b3f9e2c78ab | -14.19942 | -46.0744 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2d867194-83e0-3712-94a6-221056411ead | -14.92924 | -46.90103 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d311db5f-9099-353a-851b-cf72a1d783aa | -14.68333 | -48.27208 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 163b8f6b-ef50-362b-9a3f-2adfeb5a02b2 | -11.69847 | -47.51364 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbd87621-252f-391c-978a-7a50c1264add | -13.3189 | -47.25396 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c1c79b0-40d5-3831-9d35-6ae661eb08db | -11.91204 | -46.74015 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd3c3dd8-139b-3466-aaa9-71b5d21006c4 | -15.60683 | -52.48248 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 03802fdd-0a0c-3ea8-87a2-102884ab1677 | -13.55231 | -47.24834 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96d5966a-e741-3665-97e9-4be2f78c9402 | -11.5658 | -47.6704 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a74648c-0645-3363-b301-deb6b41cf82f | -17.6412 | -44.45193 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bfb92db-c8ee-3b6e-a6bc-6cc50acdc1e2 | -17.15689 | -47.02279 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a98b430c-8fab-3666-a71b-86fc86e0d706 | -14.19969 | -46.06784 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 423b6be6-5712-3489-afe3-bdd8c90523e2 | -14.9126 | -48.28919 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aa5edde-9431-376c-a3c7-1257093c0e6c | -13.10898 | -47.85089 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d5d101d-1802-3b0b-82ad-75811c193a8a | -13.33528 | -47.19817 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f452c83e-1035-389e-bdf6-bfddea8beb0a | -14.92428 | -48.34245 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 75e54fd7-bd9e-357e-9590-7f712898c766 | -17.07965 | -46.24802 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 176a027f-0b2a-3e3e-b5e2-1f7b87ec18b7 | -14.86969 | -48.36365 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a34edeb5-db2f-3ff4-837a-fbc75c515e2c | -14.84418 | -48.28752 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b013dea8-e99d-3919-ac6a-f4950fbdc28e | -13.55783 | -44.09741 | 2025-10-04 03:53:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 027827df-8fa2-366d-a0cf-c893ee762712 | -11.7835 | -46.84077 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0e6a219-3212-3e93-8a77-4f0bb48213db | -13.74226 | -48.09253 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21a22f46-fab2-3888-b3e8-ef3d600f72d0 | -15.37397 | -47.95565 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfbd1e34-437d-3087-b2c5-d69842eeee8c | -13.67221 | -47.29819 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03b0d30e-cb0e-3603-a0ce-78ccf0ceabcf | -13.2695 | -47.20169 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4eea8d0-2609-35ac-903c-0d7b61ff8a0a | -13.12766 | -47.81309 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53c8d43d-efa3-3ab6-8af7-7921c21b5861 | -13.10718 | -47.8504 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a8051814-9803-3c23-865d-a601e3d267ce | -12.92179 | -46.79263 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7dc0d14-8e80-3e64-a146-d263bcf01ab1 | -14.58134 | -52.49334 | 2025-10-04 03:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f82a1d60-83e3-3ee7-88f1-37ca436a91fd | -15.79095 | -46.25975 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6982511f-8978-3734-9d40-cab3d143428c | -16.017 | -50.95256 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e6618dd-705f-3b9a-80e4-e6463c731b10 | -12.04491 | -45.17939 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55f62a2d-9c62-3b77-91d9-5ed31014c244 | -14.87517 | -48.36425 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df46f0d0-730a-3b27-b55a-b8448afb0445 | -15.31 | -46.30857 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 786870a4-da2e-34c7-8d52-070e944dce88 | -14.66067 | -48.3012 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README42.md)
