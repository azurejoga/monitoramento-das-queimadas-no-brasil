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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 622bc1b7-e33f-3fd0-a1b8-dc7649da2204 | -5.72974 | -43.96595 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dade6d8d-b09d-3e1b-a65a-a7fe27da7dff | -1.39573 | -55.17626 | 2025-09-30 05:06:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d91daaa-b641-36d9-934a-03d8650ce22c | -2.93307 | -51.94693 | 2025-09-30 05:06:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e06ee890-cf8d-3777-807d-ce293101c7af | -6.43454 | -43.0732 | 2025-09-30 05:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 250f5672-9801-3711-ba23-78aadaf41395 | -4.06946 | -49.50843 | 2025-09-30 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dc421cf-4cbb-3191-b591-a2c505bfdfd8 | -3.25755 | -49.12899 | 2025-09-30 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6c69de5-cb03-3637-a746-d4df6fb5df33 | -4.87297 | -48.88651 | 2025-09-30 05:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31b8eb52-a439-3e36-80f4-4f45d36f8032 | -4.37137 | -55.88919 | 2025-09-30 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f52f393f-0602-3efd-b2d2-917238fe7557 | -2.73871 | -48.67546 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e457c5ea-26b3-354d-9555-5b6282b4f05a | -5.69813 | -42.62075 | 2025-09-30 05:06:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d2e719ca-54a9-338b-81d4-5a8de9bb233c | -6.09876 | -42.66431 | 2025-09-30 05:06:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a1a96793-1178-330f-abf1-4c1c7ca49e50 | -3.25684 | -50.11163 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 162b695a-2ff3-3371-bebc-12d00a7fbefc | -6.2911 | -43.92454 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b88b8a5-7c28-3f4f-a48b-6f7e0145293e | -2.25706 | -49.52947 | 2025-09-30 05:06:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23a2bbe7-e8af-38cc-8a26-8f63cdf9358c | -2.30478 | -48.14307 | 2025-09-30 05:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9eafb9ef-4d7a-3cc0-a969-fda08762afb5 | -4.39822 | -44.08818 | 2025-09-30 05:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f8f11db-a8bf-3a0b-bb72-0819c5b91ea0 | -3.28152 | -50.03146 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50114fd9-eec7-302a-b39a-11d363ec5f42 | -5.74491 | -42.68651 | 2025-09-30 05:06:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3b493130-0251-3168-938d-aff78972aa87 | 1.83579 | -60.87017 | 2025-09-30 05:06:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce3d92bb-9ead-35c9-8ac9-5a266ba21a7f | -2.58255 | -48.40548 | 2025-09-30 05:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59754102-7269-3709-8b0b-ac2e6b712817 | -4.88813 | -43.46708 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 635ae219-a9f6-3992-b643-26d6ef0a2bae | -4.39453 | -44.07661 | 2025-09-30 05:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d3d9e3d-24a6-32dd-a721-4aa8139e4cf3 | -3.60744 | -50.20395 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7086ba89-6327-39ba-b188-10ca75ce6a4f | -6.28998 | -43.92158 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0be008db-3238-3a9c-b9f4-f5dd142dc449 | -5.81739 | -42.77839 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34e442bc-d24e-3f43-ab2a-fa37bd8c73d2 | -5.04438 | -45.31564 | 2025-09-30 05:06:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ae12a9-57f9-39d7-a090-f5a7d81e28fe | -5.74747 | -42.66872 | 2025-09-30 05:06:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6c4c46e3-ef1b-3a44-b363-277c40bc3ae2 | -6.20491 | -44.21062 | 2025-09-30 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32e65715-f706-30f0-b725-d786278d40e6 | -3.81218 | -47.57963 | 2025-09-30 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6be5d863-1c0a-3a32-b985-67c5ca97b771 | 0.09275 | -51.08862 | 2025-09-30 05:06:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b64adfb7-9648-3d9a-98b7-23de5614f9eb | -5.74571 | -42.68122 | 2025-09-30 05:06:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f059da3-76c7-34ee-a955-4ccd8b271cf0 | -5.76811 | -43.83093 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aae8697-bb3f-3223-85b9-69e3f0035d47 | -4.29101 | -48.26913 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4220331-d089-3a25-9653-885dae6f07fc | -3.05686 | -48.71222 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de0daa25-736f-3512-a1a7-f11889683876 | -4.58452 | -50.69558 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4549a9-ceb0-3893-b564-0c52011e93e4 | -4.25414 | -48.5573 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6854bdd6-78e3-3111-85ca-ea2e3a7f07af | -4.67345 | -43.25941 | 2025-09-30 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 517cbe6e-6e9d-3a9d-8f0b-a6a87a8071c0 | -3.10095 | -47.01721 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3729685d-76ee-3e9b-a0ac-10735c9aa6b6 | -6.25404 | -43.65403 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36052fa9-10a2-3cc6-b14c-7fa2154d2d3a | -1.59511 | -54.05983 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc6c382a-8ca5-3fcb-bc24-07b67fb7ebac | -4.66533 | -46.46538 | 2025-09-30 05:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aed36f28-d701-30e8-9fda-4a9fc0272e58 | -2.07412 | -56.87554 | 2025-09-30 05:06:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 238ecbb9-052c-39d6-94da-d5c51bb559e6 | -5.76816 | -43.83663 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 788fa84c-9a72-31b2-af76-ec40318a838f | -3.84656 | -52.28195 | 2025-09-30 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9dca73e-cbc1-39e7-9469-7559c87d959e | -4.97899 | -50.64145 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a3517e5-df47-378b-af69-0c18507be4a5 | -3.47802 | -51.59605 | 2025-09-30 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33c9f23e-86f0-33e3-9809-438cfaa2fb66 | -3.25224 | -50.11452 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b6ed2c7-bde1-35e8-98e8-2360ab5bd882 | -3.25574 | -50.11868 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ad0369a-37d0-31af-8c79-bb111045a1dd | -3.50429 | -52.4679 | 2025-09-30 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36511340-46d7-300b-a3d9-af6176585721 | -3.2517 | -50.11805 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4e869d3-f13a-3820-8cff-568b5c8371c4 | -5.28618 | -43.16608 | 2025-09-30 05:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f055d1f3-3f60-3e3e-b722-d84eb7389392 | -3.10117 | -47.01457 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2c97815a-89b2-399d-aba8-0f549372c475 | -3.4923 | -48.93985 | 2025-09-30 05:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f04fa0a8-a92c-3b9e-8e9a-f92ad51c5f35 | -5.48053 | -48.65656 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 066a7252-2e06-3c37-aeb4-9732db6e0059 | -1.29269 | -54.17652 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cf49770-8b65-3b18-8eb5-4a91e95f7d96 | -0.09439 | -51.27382 | 2025-09-30 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac47c062-512d-396b-806b-ca7704954aad | -3.83904 | -51.17595 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f28e8de8-e1bf-3ffc-979b-2fa63c236155 | -4.90028 | -43.47429 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2750fe76-2b52-3354-8e6d-a555bdd93daa | -3.05162 | -48.7095 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a812ef0-a1be-357b-a52e-8501ebcaa0cc | -3.45296 | -53.83064 | 2025-09-30 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14e7673c-376f-3365-bff4-da2c99fa97c2 | -4.86382 | -45.05033 | 2025-09-30 05:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14418e14-bf31-3c59-920d-371f7543f757 | -2.44176 | -47.33139 | 2025-09-30 05:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae2681a8-f6e8-363b-ad0e-da2ba8efc89d | -3.09763 | -47.00505 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 147b46f9-b682-31ec-8e39-f201777cb4c2 | -3.33144 | -50.24783 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fe3ecac-d5a1-3770-b3aa-426090112326 | -0.09736 | -51.27854 | 2025-09-30 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 825f68e1-6e9d-3061-9c6e-1d46ad9df493 | -5.88042 | -48.11523 | 2025-09-30 05:06:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b261f6fc-c09d-3b9c-a07b-5a0cbbb7be9d | -3.4972 | -52.46675 | 2025-09-30 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b17ab0ff-d14e-32d3-8e5f-158ec354d077 | -3.3309 | -50.25134 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7355a44a-41db-3ccc-8716-567ba7314cd9 | -3.0912 | -47.01294 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2317fa3d-3812-3fa8-9498-46e78d43ef15 | -4.2602 | -48.55056 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7283fb0a-9a43-3b2c-a573-6a36be25abdf | -6.25343 | -43.65858 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 608e2c4d-d83e-349b-af97-41fa21693eba | -6.07707 | -42.61622 | 2025-09-30 05:06:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c5d49656-f926-3f45-bbbe-d8c0c214d71b | -2.98903 | -49.27886 | 2025-09-30 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fcec42b-f2f8-3648-b8b0-196b1b2d222d | -5.67202 | -45.29849 | 2025-09-30 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16cd07aa-28b2-32d4-902f-75cffb943c88 | -4.25872 | -48.5579 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e9f4573-457a-3db8-a2c2-98d59487ff7c | -4.25423 | -48.55906 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c545e096-977b-35d5-ad35-04f407bc0f29 | -4.57883 | -50.69105 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6871aa6e-7547-3863-914c-bca2bff330b2 | -3.25519 | -50.1222 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 951d3f16-e52e-35a2-a7ff-60090482afee | -4.66615 | -46.46875 | 2025-09-30 05:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7e5b6f-df5c-3ece-91e2-bb02df184503 | -5.33334 | -43.73133 | 2025-09-30 05:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 89a7f2f8-46f0-340d-bfaf-4ddadba14051 | -5.23247 | -43.69432 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed81df24-91fb-3b6d-92a9-fb85fab94c45 | -4.75437 | -42.59464 | 2025-09-30 05:06:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7b0d1c2-a10e-3d8c-a9b7-3443c1587254 | -2.07352 | -56.87928 | 2025-09-30 05:06:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 273a6880-f96c-391b-85a3-904cd1a8c449 | -1.2916 | -54.18346 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2efee90b-669a-324f-b631-bb5071ceb38c | -4.39957 | -44.07864 | 2025-09-30 05:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecf0f24d-33af-3032-b298-2e33fc13063f | -4.26397 | -48.55393 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76950c5c-1f6c-38fe-81ec-50577bad08d6 | -3.25817 | -49.12484 | 2025-09-30 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb9167a-5220-3de8-b7d9-616b5989f1da | -6.42986 | -43.07479 | 2025-09-30 05:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18ba56a1-84e7-3aec-b5c3-2da819390bae | -3.28117 | -50.03548 | 2025-09-30 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c845ebc1-914d-3d88-8204-5c703ccd0f6d | -5.72907 | -43.97078 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| becaf85d-f3a6-3c46-8cfd-f9be31afd7fc | -4.29402 | -48.26683 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 877c65cc-0f9b-36f1-8452-e40af91355cc | -4.29499 | -48.2746 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eac1c590-3c10-36c5-8c24-22da179b43a0 | -3.03601 | -48.78795 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb90419d-ed51-3e42-a7da-9404d2d5ac5f | -5.27958 | -43.165 | 2025-09-30 05:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3e52703-7102-3daf-8a72-62ad2553c6a0 | -4.0107 | -43.27513 | 2025-09-30 05:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c007be4d-f7d3-317a-8026-8f138f1ef2b7 | -4.51546 | -50.44808 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90f41f80-1848-3061-a5dc-bb62ad20f0fc | -6.25441 | -43.65868 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9eccf5c-7474-3193-8a9b-58395fe84c5a | -4.66489 | -46.46847 | 2025-09-30 05:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67228f6f-0cd4-36c0-9f2d-8264c91e6b90 | -4.89459 | -43.46802 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9d69c0f6-e6a0-3552-9058-bab43d248b60 | -4.5242 | -50.52792 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README83.md)
