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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b80740f-d5f8-3238-a322-d6e67501afaf | -3.30732 | -49.11091 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf165a08-9b3b-3f66-8e92-1461312dad32 | -3.28905 | -46.5577 | 2024-10-16 01:02:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 05ca2742-a804-3e38-af58-c984f98f4313 | -3.28671 | -46.527 | 2024-10-16 01:02:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7be36e07-b593-30ad-a552-770036e224a8 | -3.28578 | -50.93797 | 2024-10-16 01:02:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c8dec853-0d3b-3206-b7cb-8011576ed6d0 | -3.28501 | -46.51488 | 2024-10-16 01:02:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 195c3656-61cd-3e14-b34a-c6d0ba89358e | -3.28372 | -46.52154 | 2024-10-16 01:02:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ea8e66e1-065c-393a-8132-5d6f5c0aa611 | -3.25625 | -46.89156 | 2024-10-16 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d117b0e7-a843-315c-be96-4238b22de575 | -3.25458 | -46.88012 | 2024-10-16 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4bc88d5d-b0a3-3559-90d1-3be789f85673 | -3.24629 | -46.89318 | 2024-10-16 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bed37490-d26b-3f54-9231-29c20997a965 | -3.24516 | -46.88793 | 2024-10-16 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2a69c9c9-300f-32ef-bf98-3f626f90ebfb | -3.2446 | -46.88164 | 2024-10-16 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8c633a73-25da-3508-876f-e0fa04c05573 | -3.23445 | -50.17867 | 2024-10-16 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db8bad1b-a3b8-3d90-b3ea-16585cf72e7f | -3.21659 | -48.92585 | 2024-10-16 01:02:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 77dbe4a4-4bca-3f82-9a39-188918835bc4 | -3.2153 | -48.91671 | 2024-10-16 01:02:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 763f8960-2866-3d8e-afff-cbe473479aac | -3.20854 | -52.46064 | 2024-10-16 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e7f6144-f15f-3ccc-8822-7d21d759cec4 | -3.16175 | -51.30847 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33845eb0-97fc-33ad-b576-598d9f1d9ba4 | -3.15275 | -53.93668 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4b81a779-0ad5-3a77-86f7-17e2b2888baa | -3.12993 | -54.28597 | 2024-10-16 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 60f1d139-0429-35ce-9c05-f39041f58614 | -3.12453 | -54.24664 | 2024-10-16 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| cdd3d2ff-134e-3d60-a8f3-039c1e036b53 | -3.12275 | -54.23361 | 2024-10-16 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| a781b8aa-13e5-357e-9973-50189c3fb4fe | -3.12095 | -54.22051 | 2024-10-16 01:02:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| a89b2132-b7ea-3eef-a7f4-dfc4c2a5d06c | -3.11729 | -53.7524 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d35c11f1-f7a1-381f-a328-09895a6c8a0c | -3.11565 | -53.74028 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 7292718b-a4c8-3a9b-9a18-181bcc09b89f | -3.11402 | -53.72818 | 2024-10-16 01:02:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7601b3ff-58ee-3bf9-b706-5102676a06f6 | -3.11209 | -54.23504 | 2024-10-16 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f0fa7d60-8a27-3cc2-be29-cdb2fa1e361c | -3.1103 | -54.22187 | 2024-10-16 01:02:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 0dd2b5e1-4761-322f-a5f1-7409c17b66d7 | -3.10852 | -54.20879 | 2024-10-16 01:02:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b8b857e4-cbe9-380f-b72d-d03f9465ce0f | -3.0698 | -51.24411 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d4b497f0-1d19-3626-b4fe-c18b0e1bf0d1 | -3.06854 | -51.23501 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af602d5f-c8c7-3984-babe-6dfbebac1de4 | -3.0668 | -50.49253 | 2024-10-16 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fbb7232b-1938-3856-ba94-8586b320406b | -3.06084 | -51.24537 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6ad33a87-bb9f-3112-bdfb-afb33dcc6fb6 | -3.051 | -53.26224 | 2024-10-16 01:02:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f2c70852-7bca-3642-a62d-dbcf18ffaa94 | -2.97333 | -49.29313 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 93370c62-0d1d-3dfe-a655-fb4e11bd1830 | -2.96619 | -48.0071 | 2024-10-16 01:02:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6dde0d86-5490-3e9e-b4ea-0e688d11e9e2 | -2.96476 | -47.99708 | 2024-10-16 01:02:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6272f24c-3099-3934-b525-e9bb0493cd71 | -2.95682 | -48.00845 | 2024-10-16 01:02:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c097367c-3696-3955-ba6e-ef7b9b302281 | -2.93919 | -54.82246 | 2024-10-16 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ffd43aed-b764-3c4b-a019-7849c26ee4de | -2.89776 | -49.34638 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d7d13d2b-0539-3a63-8c31-4b26fe9cd763 | -2.87189 | -54.17986 | 2024-10-16 01:02:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1e30b918-186d-3110-9de3-8c9ccf3d0887 | -2.86408 | -54.5187 | 2024-10-16 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cea967d8-94a7-3760-a253-8a902d56ad11 | -2.86224 | -54.50514 | 2024-10-16 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5f052e76-a27d-3a64-b422-93e634a7432b | -2.85397 | -49.36809 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d60fefe4-bdb9-3a04-91c2-354b727812f8 | -2.83195 | -49.53503 | 2024-10-16 01:02:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95828e84-49a4-3c92-920f-33decb22ea77 | -2.82557 | -49.55407 | 2024-10-16 01:02:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ca9e0839-d22f-37b9-92e0-03a13ffa9407 | -2.82432 | -49.54518 | 2024-10-16 01:02:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a44087b6-7828-3cff-8f4d-c5bad66b12e9 | -2.61672 | -49.11946 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02f5a12e-2431-3031-977e-76ae5191ecd7 | -2.61545 | -49.11035 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 96e700ba-eb77-3445-acb5-818a70f05de6 | -2.6129 | -49.09213 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 77f5c191-77db-3861-aa10-2da4947c3b6f | -2.61163 | -49.08299 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f4d756f-2938-3fd7-87fc-99301a29269a | -2.60647 | -49.11162 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ea4983b3-7c91-3cdc-a290-19ce1b976aa4 | -2.59749 | -49.1129 | 2024-10-16 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae06e092-7f23-3ccb-a7e9-dfba16adfa87 | -2.53715 | -47.23549 | 2024-10-16 01:02:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| bfbedafc-9331-39ee-9f67-a66acc097cf2 | -2.53558 | -47.22436 | 2024-10-16 01:02:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 6370fafb-07ee-31a4-8bb8-b1488ea8031d | -2.46293 | -48.35687 | 2024-10-16 01:02:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0fc02713-bc6e-3902-9b60-15a5dbaf9ef8 | -2.46155 | -48.34717 | 2024-10-16 01:02:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3fd6f22c-7bca-36be-b533-5ebe4c759803 | -2.4547 | -49.60381 | 2024-10-16 01:02:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7f686aa-583c-3040-a89c-97fe3b33595c | -2.45345 | -49.59491 | 2024-10-16 01:02:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9a061725-df1a-3e99-9d6e-4e6f1f86cea3 | -2.38928 | -53.73152 | 2024-10-16 01:02:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 79164a18-ad11-3a38-b189-f5a2cc7b72ab | -2.38326 | -47.59189 | 2024-10-16 01:02:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d0e812fc-c561-3654-a323-ae4fa668974b | -2.34684 | -47.26372 | 2024-10-16 01:02:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f0e350ff-1ded-3acf-b06d-ff942cbe8c28 | -2.34528 | -47.25262 | 2024-10-16 01:02:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 03b1b9e3-9522-3a60-8676-366165851dce | -2.32938 | -46.48847 | 2024-10-16 01:02:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 642a818b-cc46-337e-bfe9-a653ad40e3cf | -2.25433 | -46.75686 | 2024-10-16 01:02:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9f24a40-1794-3699-9e56-3392cabeeb18 | -2.21288 | -49.59264 | 2024-10-16 01:02:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5983e91e-a6c9-379b-b177-fbbc5ee4bbaa | -2.20605 | -53.66161 | 2024-10-16 01:02:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 96abf66f-24bc-38bf-b99d-e83fdfbadf0a | -2.19235 | -46.74685 | 2024-10-16 01:02:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72113fb3-2d35-3a73-944f-feab9d7b3723 | -17.03 | -57.5 | 2024-10-16 01:03:48 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5fe53108-7a5d-322a-87fb-f68ab51ce229 | -17.0 | -57.48 | 2024-10-16 01:03:48 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| da08bc7a-b63f-3385-8b33-8e206c4f69fd | 1.0016 | -52.2164 | 2024-10-16 01:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7825b278-b91e-3689-b8f6-49ecb6031087 | -3.1098 | -54.2464 | 2024-10-16 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 43ca8233-034f-3efb-a3fe-ea11defc71c7 | -3.1099 | -54.2263 | 2024-10-16 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 64c85de1-8650-39a4-8360-c0dc3ab72796 | -3.1282 | -54.2459 | 2024-10-16 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 49382e0b-f3a4-3dcc-8c26-5d8ef048791e | -3.1283 | -54.2259 | 2024-10-16 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 631084d7-18e3-3f77-8c80-669c1f507d57 | -3.2225 | -48.9306 | 2024-10-16 01:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| de7405e1-de19-3104-94ac-d86c9c433b97 | -3.2226 | -48.9092 | 2024-10-16 01:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5a927fb1-6357-3b14-aba0-50adce3a12ba | -3.3918 | -44.5607 | 2024-10-16 01:05:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| e6d9ff73-dde3-3d92-accd-7675908e5eb3 | -3.4104 | -44.5599 | 2024-10-16 01:05:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 373e6579-8e92-30bf-b701-9a49261a2cb4 | -3.4105 | -44.5371 | 2024-10-16 01:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d81b8d8d-c6f6-3335-9acf-b0724fff1cb7 | -3.5041 | -52.1659 | 2024-10-16 01:05:26 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 444d7d20-f317-309c-abc6-13a7337fc349 | -3.958 | -46.4442 | 2024-10-16 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 28260867-471b-3732-b962-f78872a2d548 | -3.9581 | -46.422 | 2024-10-16 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| ca16c136-8592-3a4a-bd6e-ad3c53e904ad | -9.1543 | -65.3951 | 2024-10-16 01:05:58 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 528947d8-6bf3-3399-b81e-bd71d6c033ee | -9.1728 | -65.3945 | 2024-10-16 01:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 41fe69fd-d3fe-37d8-9da4-b73f060faf5f | -9.1914 | -65.3939 | 2024-10-16 01:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d630daae-81b3-32fa-acc0-12ec3ef5a561 | -9.1727 | -65.4132 | 2024-10-16 01:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b9405b4d-4ffd-3bb1-bbb4-01e3dbceded2 | -9.9588 | -47.3816 | 2024-10-16 01:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| bffa759b-cd0c-3869-a388-d59637eeac97 | -10.822 | -49.256 | 2024-10-16 01:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7a8966e7-e489-3e24-bdcb-0cc5972b51a7 | -10.8224 | -49.2343 | 2024-10-16 01:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e8d0ba2f-2086-3681-866c-807a2e11263b | -11.6915 | -65.2432 | 2024-10-16 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9e6962a9-08cb-3445-866d-945fa9de36a0 | -11.6917 | -65.2243 | 2024-10-16 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 73e8de58-e597-3407-9168-57d0ece6e419 | -11.6918 | -65.2054 | 2024-10-16 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 7ddcb0d6-aa8c-3cf5-a1ae-6c26986acd6a | -11.7103 | -65.2424 | 2024-10-16 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 12c631c4-1cd1-36ea-9d0a-2ad4091cb1df | -11.7104 | -65.2235 | 2024-10-16 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a2abb493-f2fd-3d90-9dfe-79654cd73427 | -12.4925 | -47.2818 | 2024-10-16 01:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| d2163a80-692c-367a-9ed8-d58546c569fe | -12.3793 | -63.7294 | 2024-10-16 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ab83af86-85e8-3b61-9895-15be59ff1b96 | -12.3795 | -63.7103 | 2024-10-16 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 102.3 |
| b0d4e6c2-385d-3c6d-a8a2-7df64a1eddf0 | -12.3983 | -63.7093 | 2024-10-16 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 588506e2-08bd-31d3-94cc-397a2fac378b | -12.9345 | -62.8358 | 2024-10-16 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0406c8be-2056-3a9d-951e-f4bd080778c4 | -12.9538 | -62.7962 | 2024-10-16 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 532c063f-7af6-308a-888f-4f1c20c0abf6 | -16.3031 | -57.0684 | 2024-10-16 01:06:38 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |


[Clique aqui para ver as próximas entradas](README15.md)
