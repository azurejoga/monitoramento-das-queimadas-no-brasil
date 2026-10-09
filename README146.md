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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca896562-0102-34a2-9eae-a3c179451f76 | -3.10116 | -53.76049 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff5e51ae-ffe2-3842-8821-ff9b0037f87f | -6.48872 | -62.85582 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc4e39b8-50af-33d0-89ce-5d9bd1275a64 | -9.87421 | -50.48692 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d979f875-5861-31f3-a0c6-40bda8ca9a94 | -11.23663 | -44.87347 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c632a45-d153-3ae3-a184-25e0b2925703 | -9.90508 | -44.78743 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d81b5af6-4521-3a8f-86ca-9e6e9e69bebd | -9.08296 | -45.10955 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27037d3e-816f-3b58-960a-4eed24dbabf5 | -2.82322 | -57.14106 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 18f3b870-f577-3e64-b93d-a3049e29b752 | -2.546 | -57.38962 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 56d0a5bd-3c0c-30aa-aac7-0cf68015145b | -3.22411 | -53.89104 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d854c4b-45ec-3466-861d-9f35d36c0c1d | -5.69351 | -53.47042 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34a1082b-d803-35be-8627-0b60455eb769 | -4.64023 | -50.95808 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c244e9c3-7aa7-30e6-89e0-439b62124b2b | -3.22004 | -53.89429 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4de5c8dc-edaf-3be8-9bdc-99df20f38857 | -3.16397 | -54.08819 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 171cefd0-f13a-36f1-a3c6-95198547782a | -3.60254 | -54.5867 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7c0a91c-c591-3f07-97cd-967cfd5236c0 | -4.42675 | -55.16047 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32de3e2f-6365-3c32-95e8-a1e5025bdcef | -3.99134 | -59.3566 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2319e0d5-ca55-3d4b-befb-cfdb41ffd206 | -3.9449 | -55.84852 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 074a3811-6d39-397a-8be2-dd7b86cdbdfa | -4.82612 | -45.83273 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 349cdf54-94b9-310c-9778-0cecf2a1a657 | -4.57483 | -54.95994 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a52a2e25-bedd-3f25-aaaa-6cc0918dfd24 | -3.30739 | -53.69283 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c032d5fa-1c22-3821-b657-861933574fce | -5.17465 | -45.60803 | 2026-10-09 05:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcba7ab1-eaba-3543-9767-6b359bd408ae | -3.59598 | -54.67189 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61caf189-8c36-3dad-897b-66548b3fef46 | -4.30289 | -60.95046 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e8f4396-d782-3f06-b1e8-23678a2a65cb | -5.70754 | -53.45419 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1b10953-f4ed-3eac-8d71-b17be152b771 | -10.85968 | -45.54388 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f048eb78-79f0-3d80-9bde-77dc003f5764 | -3.5479 | -54.68625 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ddd0a1a6-2c26-317c-95fb-b580cc3b22c8 | -6.51342 | -51.11792 | 2026-10-09 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b84ebb-b14d-3c41-aba1-5ca3c98f4173 | -10.98258 | -47.79665 | 2026-10-09 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b66f6f6-2838-3e85-9517-ced1ba9832a7 | -3.53557 | -54.67176 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 553de5a8-c136-3cc0-b176-c74d2298f06f | -4.36428 | -55.20167 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8760c7c7-6089-3cdc-ad9e-67a6dc2709ea | -11.99155 | -43.47824 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d7ed62f-a0a2-3cc5-983d-673249874f46 | -6.9372 | -43.66817 | 2026-10-09 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bbf75a8-e1fb-3ebc-bd1d-5cee45d52f88 | -3.67791 | -55.94948 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d962fe4e-d5b0-3ace-985c-dc68a5b89363 | -3.58296 | -55.60399 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebea0f29-a021-3e25-b002-06be6b1a846e | -3.26902 | -54.01784 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db4ecf45-cb91-3e5e-909e-c7a1bcd7f635 | -3.8277 | -55.97316 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec09103e-476b-3442-885d-4824d108c2a0 | -12.01317 | -43.44445 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69b29d58-4ba0-3126-8956-614ed2b748bf | -10.74724 | -46.58897 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56e61750-5f57-3229-b1a2-da3be982e531 | -3.47629 | -59.51327 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5c432b3-bb14-3458-9c97-e3881a3e8d80 | -3.29589 | -53.6986 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 904d0c1e-e30e-347f-ae4e-607f03032ece | -3.07247 | -53.96074 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 226ab6c1-88c4-342c-a0f4-78b17671a210 | -7.47988 | -42.83366 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 192dac08-1544-3d8b-a77d-2e9659c83a0f | -3.36398 | -54.74491 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2e43aad-2f18-360b-9060-103ab97574cf | -3.55211 | -54.6828 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 975c84f2-8377-32e8-8a0d-3b570c909904 | -3.91027 | -55.89653 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 434ba753-cd73-3abf-b071-101da7094a23 | -11.76309 | -44.9554 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80037aea-0624-386f-a67e-b942345c42de | -2.87893 | -54.19925 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fa1c9af-bf48-3d71-afae-79336640e83f | -5.82196 | -52.04518 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6934d80-8c23-3d73-bef7-2e48f3985a7b | -4.55011 | -54.97667 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b485bd05-81c0-38a8-81d4-11f28cd62689 | -8.55717 | -46.90883 | 2026-10-09 05:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4d323ba-cc42-3e5a-bbc4-139104dae30f | -2.52569 | -56.61713 | 2026-10-09 05:04:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa0443a1-5f00-3f8f-98aa-93d865c898b4 | -7.19086 | -52.62543 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e74fa72-7af6-383e-9863-e61f48d8239e | -8.79131 | -47.59141 | 2026-10-09 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2075cfeb-e3bd-31e4-97ea-1a42210d319e | -6.82232 | -39.55227 | 2026-10-09 05:04:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0f09af11-e3f5-3b43-ba40-659643d551dd | -3.85319 | -51.93672 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f473bc2-2f79-3be4-8fff-88b9c1059c39 | -3.27044 | -54.05325 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b6b2f5e-573e-3ec3-9a79-072b244b17f8 | -3.4617 | -59.57086 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fbcba531-4710-347f-9194-14371e553519 | -3.7182 | -54.22806 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd53a9b7-34b7-323d-b679-1367b18b4868 | -2.94005 | -54.15701 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760a9f3a-8745-3060-939d-a3733cb19503 | -2.88509 | -54.1604 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e2fef6b-81e9-3970-81b6-80637d2fa875 | -8.99637 | -45.91285 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72502d9a-5ad2-3c6f-996f-0ca8347b18d2 | -3.07663 | -54.2937 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 821cfb76-0d57-3cd9-b838-8efb25939b21 | -9.87708 | -50.51661 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 214b3f5e-b6cf-35fa-b141-3dfc22373610 | -11.20853 | -47.71757 | 2026-10-09 05:04:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b4dbb4f-76b1-34dd-85ab-72737e7d974a | -11.99732 | -43.479 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e213977d-ca34-3e36-a4a5-6ef2f5a57471 | -5.98385 | -55.36165 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e86bc7b2-ef06-39d1-b0f4-f8eb6ca62d94 | -6.11126 | -52.71378 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad19d37c-10b8-3faa-b282-acaa96f1eb75 | -6.38871 | -55.26617 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a32e4c1-ed55-36f0-b216-39170c2e304d | -3.03909 | -54.27991 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ff179c7-0a62-3497-aafa-257a25e057f1 | -7.07082 | -47.39509 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6cadcda-2169-39fe-865c-d4526f9c940b | -11.46728 | -43.38765 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf0f1980-dd77-3b67-848e-84ebe53632d5 | -3.01282 | -54.03819 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f3b8d5f-fd4f-3a45-867e-1fb1d8ce6b50 | -3.07954 | -54.29815 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5533574c-380c-30e3-9a28-ca64ac2aaf7c | -5.94866 | -55.3517 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5199e6d4-d501-3797-a9c7-ff2f0f1464e1 | -4.62077 | -49.21286 | 2026-10-09 05:04:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ddb6572f-2654-3935-a5bf-53364a3dfb6f | -9.29588 | -47.4281 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d07eac3a-1d38-3bc2-9904-d1ce124b73ea | -3.04225 | -54.26025 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea591b42-a64b-39cc-a8a4-20141d5a6068 | -3.10209 | -53.95382 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56b59c64-2e63-3619-aaef-9abf5a37db48 | -6.20712 | -52.83596 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa48dd1d-b62b-3b52-b5bc-9f20c32099b9 | -3.227 | -54.29988 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c6e2fbad-eedc-3418-abce-3161118a453b | -6.59486 | -60.04617 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c304c1bd-d163-3df4-8466-c2195692e034 | -4.11539 | -59.88074 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae704d38-9df8-38df-82d2-197d6fe86244 | -3.99217 | -59.35154 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d1e7a89b-52c7-3571-953b-8aecc2bc60e5 | -6.39583 | -55.26735 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0856db67-c128-38b1-9f5a-4207c4433fb3 | -3.20145 | -54.36824 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7afb8b6-3d3c-366c-ba8e-ef24d476a5b0 | -3.55704 | -54.68618 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 41d1bbe7-9e39-323b-8163-db386fc3e150 | -8.99792 | -47.73877 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba5658ee-0b10-3e49-8a5d-00019bc4d4eb | -6.5328 | -55.38039 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7adce6b-2f5d-3431-9c95-e88848614068 | -3.59158 | -54.56465 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01fd60de-fefc-3e97-a4b1-f49e0f1d9101 | -9.3483 | -46.578 | 2026-10-09 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dc58308-9060-3c47-848c-cecb297cd068 | -6.436 | -52.67267 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7906ed21-ed12-393b-9b67-5541f38add18 | -2.99441 | -54.08648 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33701e80-4f00-3999-a6e4-a63044945b18 | -3.05742 | -54.21054 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9f71c91-377e-344b-9dc9-65135d4ea17b | -3.00741 | -53.89286 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9de2d8a1-4c70-3563-9afc-23734ba0f724 | -2.98742 | -54.08537 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61999270-4326-3bb0-869e-2d0555f40bff | -3.29866 | -54.01091 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bf8b306-82ae-36ac-bf49-2fb671fc8c5e | -7.53251 | -45.87135 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3a68344-98d1-3963-a481-ce2f19dd982a | -3.17615 | -54.75031 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb23a510-c83f-35e0-b3e3-1f2a229a8383 | -3.97691 | -56.11819 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f2d6297-a774-3d57-b3b2-4c7fe06e379a | -3.73705 | -57.13137 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README147.md)
