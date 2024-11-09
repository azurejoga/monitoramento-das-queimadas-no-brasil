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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4794777-469f-36c5-b57f-790ef7c1cf96 | -2.83198 | -53.97684 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8ee2d5-65b1-3ea1-ad0b-319a1a5acb36 | -2.73283 | -51.71406 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e59e13b5-9e7f-3e65-bac9-0201e3466d04 | -1.51453 | -52.18098 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cf3e7f6-13e2-347d-b981-ad184cbd0293 | -2.58229 | -49.13269 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 51fc8a5a-4edb-3413-b1cb-108fbf2dd213 | -1.73001 | -53.28352 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1396001e-b560-317f-8af6-e4f2b8dbdd01 | -3.79626 | -50.79731 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 425290e6-d2cf-3cc7-96ca-026509447e59 | -3.77848 | -53.70681 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a20b147c-1d08-3ef7-ab0c-28fd6fcbf27c | -4.72873 | -50.37857 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1fa2798-5813-3155-89ff-317b40cb03e9 | -4.25512 | -47.57729 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae2835ce-841b-3268-b17a-3e33e3f1bb6e | -2.82187 | -50.43803 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8eb08961-20b4-34b8-bfa7-a157ec1d678e | -1.33544 | -52.20292 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1fc0a2a-8518-3f88-991d-54ff037d7588 | -3.28242 | -53.67854 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2387ca5f-a568-3f8d-88bc-d1ce366678c7 | -3.06312 | -53.90648 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc78c924-42cb-35eb-a330-5ad1a8e604f2 | -1.38305 | -51.43855 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39a6825e-92db-3654-8a1c-3f8daafaad7e | -1.38703 | -52.71118 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b030b80-3955-32a1-9ea0-1b47cba7ecbc | -2.9412 | -54.12305 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7a5388a-2374-34af-8ebd-623e1e465e36 | -2.4071 | -55.71213 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3c81113-b37d-31d6-a2f0-589118b92480 | -1.38146 | -52.20676 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f858c99f-6869-3b5c-b592-6186eb1f5dc6 | -1.43364 | -52.17916 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45835a23-931c-3747-9910-96dbd82c438f | -2.87879 | -51.31569 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbdc09f2-8f81-3356-83ba-0a930a68468c | -3.97587 | -48.40155 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b75bf605-b858-3892-a590-ec80103e01d3 | -3.56076 | -52.29119 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e004a80-c58d-39fb-a3ac-0e337ed6418e | -3.41722 | -50.1368 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebaab8be-eca5-3578-aeb5-55b5e2bb5f24 | -1.49657 | -51.60339 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cde5f7d5-babf-3f03-a83d-11e5a5333436 | -3.04642 | -50.37397 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f542d0e-17a0-3094-ac66-e9e407a7f07a | -1.83051 | -53.72059 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b19cc058-99ad-3ec8-8ea5-f81b263e55df | -3.24646 | -51.55259 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9615ab3b-8383-376a-a7f6-3be7821e0cdc | -1.99005 | -52.29382 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9549642d-094a-3615-bd59-3e9bd378bfe7 | -3.77794 | -53.71026 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75ed6989-b9bd-399b-a4a0-74e1cd6f4ee9 | -1.76616 | -45.61071 | 2024-11-09 04:55:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3cb6fbe-d363-3e32-9c8f-c776f1f3feaa | -2.19831 | -48.36877 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49e4877f-009c-3f71-974f-1f12b40e3b4d | -3.13983 | -52.97091 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd45c260-d063-31cd-841b-f64d0bb55a27 | -3.78533 | -52.21694 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ff794af-e57b-322d-bd4f-ddf4a97481ad | -3.05118 | -53.27525 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 550b90f5-81fe-3aef-9fcd-e5a32f2056d1 | -3.00631 | -53.43068 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 614d2e19-73cb-338f-abe9-7ae0bf2ec32c | -0.30429 | -51.72116 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72ed079d-637c-3566-90e2-4e54914c4213 | -3.85013 | -49.89377 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87a9d403-44f6-3dac-a737-8e4f53a45865 | -3.23119 | -50.44653 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9638f60-ad81-3efa-8d13-d6f315a7ec75 | -1.99262 | -52.09005 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43f08af8-d066-3e92-a878-7cff648dc970 | -4.18175 | -50.42398 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b769f2d0-ea9e-3e19-99c5-9839de2c0acf | -3.18464 | -50.43921 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c681766-74d6-3be6-9c18-df952d5c5cac | -2.36698 | -48.5442 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19ace3cd-6e93-37c7-ad98-e686dc340d40 | -4.11428 | -48.49845 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11aef002-d870-3874-9bc4-93956c19d595 | -2.09455 | -49.51776 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be29c5c4-77a8-31cd-bc41-f377b1f934e7 | -1.5232 | -52.64028 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df01b332-0186-38f6-af29-578888624de2 | -2.8182 | -54.08538 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc0769f0-f36f-38a1-ae84-626fb1c95c60 | 0.67919 | -52.16247 | 2024-11-09 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfac86b8-1e15-3925-9d17-a22f73e4df2d | -3.96743 | -48.18019 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 6241307c-3ae5-3d99-9c12-ab7b9ae847d1 | -3.09211 | -51.29044 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9e1985d-2855-38ab-b1b1-e128eea09138 | -2.8609 | -50.31829 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 56d04e88-008e-371f-b46a-f9395cb274af | -3.02907 | -54.3161 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f9fc893-9b78-3208-8f4a-6575e38bea38 | -3.17711 | -53.84988 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be772b76-27ce-3dd4-b1cc-acdcd7b84c45 | -2.6271 | -51.29345 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 011b1407-ffb2-3a34-8cb1-7959c5377d53 | -2.92977 | -49.35904 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f302598b-d8f9-3201-87aa-6b8f46243618 | -4.22274 | -50.64397 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5caa34d-dc25-3ecb-97ee-9fa7766fe9ce | -4.86927 | -45.67392 | 2024-11-09 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 107a2793-6881-3357-8469-4b5e556426fe | -2.62617 | -46.15629 | 2024-11-09 04:55:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 176007f4-7a7c-3ea4-85b8-d79df4875837 | -2.68258 | -46.77243 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72eaf048-83ab-351b-b0f1-fbf8b5eb1425 | -2.12605 | -51.24124 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b31bbc00-fa67-35c8-9d63-b78a43f3c7ec | -5.63062 | -44.83104 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcd28440-b19d-3512-a332-9d341fb3dae7 | -3.59172 | -53.77671 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19522a8a-8920-37f0-9733-f1026bf83848 | -3.51555 | -53.14222 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbc41c0f-25a1-3acd-91b3-5703079a231b | -4.07119 | -47.21331 | 2024-11-09 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25ce3ebb-e9bf-3e3a-b9ea-20c47a058035 | -1.49717 | -52.55154 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd1ba343-ae6a-31e4-ab22-b9704da664f4 | -1.40191 | -52.16353 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8436bc3-2c13-385b-b8ff-ca58b8128aa4 | -2.24462 | -50.71667 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 482f81b7-dafe-3edb-a9b8-6eb4b3bb02b2 | -1.18651 | -53.6625 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfa6d6f4-6e8a-3660-8f03-d471bb12585b | -2.47787 | -54.05434 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fed1e5a4-7f42-38a8-a8f2-6321d2a6deb2 | -3.77543 | -53.81248 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f3def62-0c5b-3b63-b52d-e9a80053d171 | -1.98191 | -52.0271 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f51c1bb-603d-327c-a1cb-bc66042c6c0b | -4.03334 | -47.14356 | 2024-11-09 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d576c645-00a4-3f7b-a91d-bd37155abc11 | -2.12204 | -51.24441 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e13232e6-39ef-3d25-aee9-627df19e0dce | -3.19371 | -54.31981 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83dd7318-ca38-3c52-8b2f-554c3fa01cae | -2.17879 | -48.32763 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3294fbbf-5363-37e6-bccb-e12893062cc9 | -2.18326 | -51.74125 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30dc787e-ad18-36c5-b745-5b3e0ffd1d40 | -3.96498 | -48.16823 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b857d0bc-83e9-3d8a-9e4a-8cb9710026f1 | -3.2225 | -53.28402 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0368f18b-f2ac-3f1d-9fa2-eb2b73f01319 | -3.21769 | -50.19983 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cb210d9-f077-3bb5-9459-e590d1ff0126 | -1.11585 | -53.59785 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a6dbd61-64e9-3baa-859e-fc7ae4115915 | -2.8771 | -49.37435 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea280bae-78d2-37c8-947b-a118c9517aa6 | -2.95076 | -54.46287 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e14351bf-50c4-3319-843e-29cf032799d1 | -1.45817 | -51.49078 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11e5f5aa-10e8-305a-8723-cc597dda8ff4 | -3.53287 | -50.86855 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 854521ec-6aa2-30ac-99f7-e97198975ec6 | -1.62867 | -55.11252 | 2024-11-09 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f451838a-5c69-38df-96c5-eb1aa7bcf6ed | -3.25679 | -53.40959 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5373236-4106-33ff-9791-465079a85873 | -3.27302 | -50.1785 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4993ec6a-2d6f-3e40-8d04-693222fba392 | -2.23796 | -53.66726 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eee49b62-96ba-34dd-a50d-bf3752937ca7 | -2.87524 | -51.47085 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7a476336-f905-3181-991d-ebfbe175ea2c | -3.82953 | -51.91058 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56d6175d-9e48-3b31-a0f4-90ebb3c317a7 | -2.37348 | -46.77587 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3b1d726-fbb9-3a45-9ecf-a850901bc10d | -2.13347 | -48.74129 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 606a55b0-7b6f-3922-8b71-6827f76184e0 | -2.96749 | -53.87051 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff950799-ac6c-3b60-9281-2c3f6770c92b | -4.703 | -46.37992 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0609082f-8ac9-394a-8f70-d456b44345b3 | -2.76608 | -53.21617 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce120ac9-5504-3470-bddf-d191c869c3b6 | -3.82202 | -53.77384 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9ced34e-9388-3dac-b325-ffcd6bf688b7 | -3.66319 | -50.25794 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9acc5c6-5256-3e35-9475-5f01cf65e811 | -3.18424 | -50.58386 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c69b91fc-1195-3600-b3ad-5eab7ddc1c10 | -3.78361 | -47.7387 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53e173d1-2005-3621-90f6-89d991a9cdd9 | -3.04523 | -50.37019 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a2f4056-ced5-352e-bc7d-c36c337b2d94 | -1.23032 | -55.80495 | 2024-11-09 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README89.md)
