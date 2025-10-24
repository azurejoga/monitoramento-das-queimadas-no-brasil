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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 145a722a-e718-375f-8254-e4faf3bb8360 | -4.89828 | -43.23405 | 2025-10-24 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b06e794-5587-3f81-9da7-487ce3ec99cb | -2.47126 | -49.23616 | 2025-10-24 03:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83dae2d2-8a9a-32b9-9702-11821c66e5b4 | -11.02744 | -47.90069 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54718606-d913-300c-9119-32e4ca142093 | -9.60339 | -46.90573 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8d78c310-64e0-3cd9-83a4-099d67ef78d2 | -8.87494 | -48.29372 | 2025-10-24 03:49:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2a7084c-000a-3136-b1ea-6ff5e91c9e68 | -16.25219 | -46.78725 | 2025-10-24 03:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e2b47ec-e3f7-3d83-a046-2e0f288449ae | -13.92197 | -50.2592 | 2025-10-24 03:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12f0d3cc-6563-3ead-a838-30ec340c5279 | -9.61124 | -46.86337 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb0d413e-e53a-3a0f-8189-937bc295fc41 | -9.87041 | -47.72859 | 2025-10-24 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddcc5fc1-5233-3a24-814c-142633282759 | -13.18637 | -47.74838 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d894d7db-859a-3802-8f9d-620d0fb07218 | -9.30651 | -45.20449 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a3354d0-7b65-3e3e-980a-3a1abef91054 | -13.36777 | -50.46655 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a00be5ef-dbf5-3a3c-a589-ad4efc147264 | -11.00994 | -47.90103 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 219de564-8740-34bc-89f5-421adfced4d4 | -11.35752 | -45.95784 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c641c37e-b208-3c07-9902-ee651b3adb49 | -3.70223 | -47.65426 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98e45190-5093-3666-a181-273b9b2cbd79 | -4.87832 | -47.53527 | 2025-10-24 03:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 567d4237-79cf-3e5c-8a43-cb32ff8b19c4 | -9.30444 | -45.19583 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c85f4d89-c5e9-3962-9c1f-6645375a7745 | -14.75233 | -46.60509 | 2025-10-24 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9fc62f4-472b-3550-939b-043180992472 | -5.4306 | -40.90274 | 2025-10-24 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43512472-5013-3ecf-bb6a-82079aea79ab | -14.54392 | -48.02605 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4c58f82-6853-3bac-a96b-8d2f15b08111 | -11.35635 | -45.94767 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eb0847cc-5075-3cff-9414-54620b50dfd8 | -3.78563 | -43.9068 | 2025-10-24 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 186cf445-c35a-3b6c-8fa3-731fcb26f597 | -9.86589 | -44.89542 | 2025-10-24 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a52efa55-361d-3af0-86f7-19063e7aa056 | -10.01526 | -47.0789 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 97f48557-f447-37b6-9800-e23a367aa756 | -12.87617 | -48.59526 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 582a2720-18a4-300c-950e-d2d076c500bf | -4.28381 | -40.69766 | 2025-10-24 03:49:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 620a4a3a-cd53-3dfc-8bad-baba8d3ce6cc | -12.27538 | -43.82276 | 2025-10-24 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db86d883-6315-37c1-b623-f3f5d1e3b949 | -14.53767 | -48.02962 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 980cdc8b-9545-3bc4-bcee-33a0dc5d43fd | -9.26511 | -46.45021 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3b21641-aefd-3562-b46e-12e63fdb2591 | -12.0987 | -47.00491 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce8c9bc4-5835-3c93-8816-9b07a642b20a | -10.00998 | -47.1073 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a2010513-072b-3b54-82dc-725704c24a62 | -13.34769 | -47.97245 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7648c098-8c3d-30ef-b365-10884558afa6 | -6.51958 | -37.48344 | 2025-10-24 03:49:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 576decb1-7a83-3206-b47b-fdd4a01edadf | -3.59949 | -48.98814 | 2025-10-24 03:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76566fb5-d13c-39fc-9abb-18890267740f | -12.95565 | -48.50437 | 2025-10-24 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3805d0e7-c022-369b-8968-b2ab26da97ce | -15.60942 | -45.91674 | 2025-10-24 03:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f931b2e0-2605-3005-9a2d-76ece75ce429 | -10.01654 | -47.07201 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 19a79c97-2a4f-3188-9f6a-4dbca2b642af | -11.36946 | -45.93195 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3afa92e6-31fd-3833-b966-cb8fd2e7254e | -13.66931 | -47.95414 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b050d192-8720-3b7f-8bb2-a8cd5b925735 | -13.2112 | -47.735 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bad9cd5-e9e3-302f-aead-6514493699d1 | -4.46366 | -43.23834 | 2025-10-24 03:49:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 098d1ed8-153d-3974-840b-58a73cc2e516 | -3.78651 | -43.90142 | 2025-10-24 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ba6db9bf-f29f-37d2-ac9d-0b8141025db0 | -4.28306 | -40.70226 | 2025-10-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 09e8d7a8-2529-30a7-85d1-be3010a703d5 | -2.47439 | -49.22347 | 2025-10-24 03:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 42a962b6-b9db-3563-925a-58a13969b7b3 | -12.07496 | -46.44341 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c8769c1-fb99-34bd-9818-53a317d62c83 | -16.82254 | -45.70956 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 175afc53-c995-3de4-ba9a-2d774da4bb43 | -12.03278 | -46.9285 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c0e3d92-4de2-3db2-97d6-a3b5e8753455 | -12.07112 | -46.43624 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8252843b-960c-340c-909b-843a88565d3b | -10.40819 | -47.11481 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f878db2-0c86-35b9-91bc-095740f47932 | -15.57023 | -47.71621 | 2025-10-24 03:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 255b18de-e02f-3364-8ba7-c3573518493e | -4.21049 | -48.60452 | 2025-10-24 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 014e9ff7-1a31-32df-bd21-e7dbe749e3d2 | -2.47825 | -49.23721 | 2025-10-24 03:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c798ba88-7731-3d94-887e-10dda38c18b4 | -13.37333 | -46.63948 | 2025-10-24 03:49:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bea16d9b-217b-3ff9-b31b-ab5adccc4e4a | -12.81631 | -48.62929 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6083cb7-61db-32dd-a5ec-ab1bfb27a7af | -10.04354 | -47.07727 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0e4677d-23c1-3835-b0f3-8144b15e5530 | -13.35308 | -47.97356 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9a5404bf-b0a8-3eec-9cb1-0f6c98bf282f | -9.63828 | -46.89774 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7146a718-704e-3e46-a827-12ac9b63b393 | -2.74247 | -48.68505 | 2025-10-24 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38f0f55a-ab07-36f2-8c20-dae453d0dd1b | -11.82245 | -44.1644 | 2025-10-24 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b01d37df-a1ac-3faf-aef7-ef004bc39e6e | -11.79776 | -42.84578 | 2025-10-24 03:49:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6076c0f2-18a9-31ff-9c14-ba14de08d791 | -15.60585 | -45.91087 | 2025-10-24 03:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd857a40-8cfe-3ad6-a398-48bfe0146609 | -11.35653 | -45.96336 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c14e8541-b164-34cb-8a70-20a019cd08d9 | -12.88772 | -43.43169 | 2025-10-24 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0af4fa6-d43f-3fb1-854a-3bd1e9924d91 | -14.52074 | -47.95512 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa665f96-c8c2-336b-a602-e5e176012a2a | -10.0159 | -47.07546 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ce917c20-b158-3863-ba22-49056b4f4107 | -11.36233 | -45.94289 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d51e66a7-0cab-36c4-90e0-e39e21ae3ace | -15.13322 | -47.93612 | 2025-10-24 03:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 038bb250-8253-3b9a-b859-0c6270dbd9cb | -10.01719 | -47.06852 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83460e9c-18fb-3865-a6dc-1262ef0a21f0 | -12.26505 | -47.44652 | 2025-10-24 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03a4deac-0095-3253-9cfd-1e752a172fe0 | -9.6001 | -46.9235 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0162fffc-efc0-381e-8cf9-e9f88562e015 | -15.20999 | -47.96066 | 2025-10-24 03:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 123b668d-4872-3c15-ab8d-4b4d5d25f675 | -14.20529 | -44.59785 | 2025-10-24 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b94f063-63dd-36fe-a3d1-e64ead32eec6 | -10.88339 | -48.05598 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1cfacd9-aa65-305d-8cf8-79f32c717280 | -4.81222 | -42.75589 | 2025-10-24 03:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02f26699-af5a-38d8-9936-87e0fe8349c9 | -4.98857 | -44.14853 | 2025-10-24 03:49:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90126f05-b2e2-3349-a06c-5ce1a179a0a5 | -13.35147 | -47.97263 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ebf032a9-0da2-3771-bfd9-b5be6563009d | -13.77525 | -48.34731 | 2025-10-24 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f847483-8c85-34ee-b551-4c1d8b0a7c46 | -12.84965 | -48.55091 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5e05bfc-4056-3e94-b28c-61b9936b9d00 | -15.83637 | -49.09018 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9832df8c-34eb-3b7f-b8e0-fa5b5325b054 | -8.88006 | -48.29922 | 2025-10-24 03:49:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fec4f71d-2953-3312-b9c6-25ee7f73d5d3 | -10.88707 | -46.04747 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a91f086-2106-35cd-87da-014fc228c6d4 | -9.31244 | -45.2071 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e21441d2-6392-32f7-8c88-f09169bf66f5 | -9.64075 | -46.89699 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc61096a-7c26-37d3-a63e-7e06b73427e1 | -9.26273 | -45.34656 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bacda32a-86ab-3bb7-b56d-6eae63df63eb | -2.42309 | -48.43829 | 2025-10-24 03:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0448b26b-e5c2-3ef5-9aa6-4dfbd60eca8c | -3.02378 | -49.49311 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb9ab813-4c38-3510-8bde-c0a47ab34582 | -12.06505 | -46.41352 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e36f86f7-02ab-3d71-9b86-925728c6b44e | -9.35264 | -46.59308 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7807449-a2b5-3510-802f-0266d46d9ce1 | -4.46445 | -43.23363 | 2025-10-24 03:49:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f275f6f6-8905-3a35-b5ed-72c1d6e4e9ea | -10.04292 | -47.08067 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0943dedb-f0bd-3db4-a549-4e8b7f11c2e5 | -10.01397 | -47.08581 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5d0adb0-4cc8-3a98-9486-846a9598b476 | -10.98094 | -50.35799 | 2025-10-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2850cc9f-f61d-3c87-a463-65062a8c1d5d | -3.21781 | -46.80698 | 2025-10-24 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f34031c-8d9b-316e-b4c5-98d76e8792aa | -13.80647 | -43.89646 | 2025-10-24 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e8536fa-7f86-3851-9c38-78fe60763753 | -9.23986 | -45.59033 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8efc67db-7408-3305-8841-2b51493e18f6 | -3.13199 | -49.52491 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 85dc7dcf-cc3a-3a7c-a871-1abb1821f3d3 | -12.29405 | -45.52741 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bff6704e-9ed8-3021-a4d1-516ab4cb6ec6 | -9.6389 | -46.89434 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b257b1-42bd-3ee5-9e0c-d1308eeff506 | -4.03046 | -45.49944 | 2025-10-24 03:49:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 620e473a-4354-38f5-a516-8720fffc2661 | -15.18845 | -47.08458 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README12.md)
