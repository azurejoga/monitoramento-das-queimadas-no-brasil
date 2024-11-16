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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 933cfd55-3c9b-3aa7-aca4-0f38600e93d1 | -7.58368 | -39.04616 | 2024-11-16 04:01:00 | NOAA-21 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53aaad98-9952-3e67-a1a9-1c8fba23b761 | -2.88316 | -40.38839 | 2024-11-16 04:01:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fabdaaeb-a2d0-3629-af60-a1df1bcc7393 | -3.79188 | -43.90968 | 2024-11-16 04:01:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d5a52a21-ece7-318b-bbfc-40c78518a7e6 | -3.84563 | -46.61533 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ae0362c-0448-3d0d-a2c5-3b64648942e9 | -2.78739 | -48.56355 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 21327dcd-636a-31b7-b058-435c31e69b9b | -2.03027 | -46.37447 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b91f7118-848d-33da-aa48-1a88443354e3 | -3.98109 | -43.72168 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ae9dcca-d275-32ec-8b26-01536e9b22e1 | -3.90534 | -47.1655 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 331a3e09-bd64-35b8-9642-79b6f1a3109b | -3.33174 | -43.82191 | 2024-11-16 04:01:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 029582b1-9f9d-3976-9a67-99acb965785b | -7.68041 | -35.40228 | 2024-11-16 04:01:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 921276a0-0625-35d0-97f2-d12139b9b1be | -3.56106 | -50.23904 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 712a0dfb-7be9-336e-9da8-2eecf34f860f | -3.58583 | -44.85076 | 2024-11-16 04:01:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 321f1af7-3b84-3599-8219-b12be9030b90 | -4.90858 | -44.0336 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60bb8821-7b64-3548-a1f1-cd8d68d9f4c3 | -3.74398 | -50.18693 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 439258e8-5cf6-3c9b-9618-e5bcdbef0c1b | -4.36843 | -45.62341 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd3348bb-3a63-38be-8922-0a88271bb438 | -4.02566 | -49.18838 | 2024-11-16 04:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a21bbed-c8d0-3d61-b370-d025fb5615d1 | -4.22508 | -50.67305 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bd8951f-2543-3a7b-a33e-9efaa291d633 | -2.96477 | -48.04107 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96f478a7-4d83-3813-b231-b7bacdb12282 | -3.0718 | -48.01236 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a3ad6a6-293e-374f-aef8-9c2553621d8a | -3.50336 | -45.44599 | 2024-11-16 04:01:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11d8018b-9ff4-3a6c-b6d1-98ce8474b4ae | -3.98951 | -43.72039 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6e84ae16-548a-3470-a1dc-433fd053b13b | -3.28493 | -45.508 | 2024-11-16 04:01:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5fc315b-d79a-37dc-ad80-97d9eb89a3f4 | -6.99009 | -39.65876 | 2024-11-16 04:01:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1907e967-0da3-3726-b058-85192b6c9a3d | -4.38128 | -48.07315 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07d9bc13-32ad-3db2-8042-173cfe022844 | -4.45246 | -42.92959 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11786f0b-c1e1-3ab3-a140-ab2b5e6b17ff | -2.46911 | -44.83989 | 2024-11-16 04:01:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fbe454f-959e-3627-b040-2cdd5f8d4906 | -6.43964 | -47.85957 | 2024-11-16 04:01:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e5a808d-ba2f-3166-9769-00e3b4e66744 | -4.90942 | -44.03596 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 379753a1-f83b-3b8e-96f8-493e6be82d36 | -3.98566 | -43.71762 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aec697c1-0f04-31e9-81e7-e34c0ad4ee70 | -3.73994 | -45.64919 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f872eafb-c332-3eb8-b5bb-7a9e966719aa | -3.51871 | -44.72037 | 2024-11-16 04:01:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee91f05b-a85a-3e62-99c0-2b89d3f8928b | -4.37772 | -48.56974 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aca91afa-1b23-34bc-b7d6-cb15d4dbabf7 | -3.56628 | -50.24402 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c37337c3-d556-351d-9e41-0d5ffcdf4655 | -5.97526 | -42.16227 | 2024-11-16 04:01:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bf0c566-a4d2-31d1-a07f-5687eabe6e7f | -4.54608 | -42.97794 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6670be53-cc12-35d4-9f18-e1564be57ff3 | -3.79759 | -40.99492 | 2024-11-16 04:01:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7606dbb-e87b-372a-aa91-ed7a0796b0be | -5.30173 | -40.8869 | 2024-11-16 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b0d8599-8881-319f-9d92-7152a4e2e94d | -5.67063 | -35.64211 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 52.7 |
| e8277a9d-9368-3052-9fa7-537babe3c8b3 | -2.97265 | -47.99191 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6eb77281-0410-3ea4-a281-70195c009380 | -7.19283 | -39.75481 | 2024-11-16 04:01:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 53b86047-3317-383c-894a-5a627494808b | -6.94404 | -40.02081 | 2024-11-16 04:01:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7a66b85e-7c01-3270-87ea-05fe07b90fc6 | -2.35684 | -49.11418 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1ddc5323-94fb-3338-b46c-f951c5e86586 | -3.08532 | -47.76711 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d337dc3-63c3-34c5-a24a-61ac68503f55 | -7.92809 | -39.55015 | 2024-11-16 04:01:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d6f70edb-d40c-3e7d-936b-54b49d433dd4 | -4.53828 | -43.564 | 2024-11-16 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 156995b7-4a57-3d54-804f-b9d4768cb9d2 | -6.82461 | -46.77837 | 2024-11-16 04:01:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e552041f-9c5a-376f-94dc-37b9cfa4bdcd | -5.14472 | -37.69907 | 2024-11-16 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 490ddaed-ac4f-3e1e-862f-aa1c3d5aa1e7 | -4.25402 | -45.90277 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bb11888-3ff7-38cb-9e55-22c906357345 | -2.66484 | -46.1807 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5303ac79-15ef-38f9-b3b7-143f6fb1a9d8 | -4.20964 | -45.61729 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23eaa6fe-e628-372d-bbba-40bf17a7a16a | -5.95248 | -44.46461 | 2024-11-16 04:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 78ef0c5e-e60d-3b39-a335-c5e1962166cb | -6.4958 | -41.57804 | 2024-11-16 04:01:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8a79e09-908b-3d7d-9469-1ca8940021b6 | -4.48681 | -48.11904 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00436b99-26bf-3d38-b50e-31be623dec20 | -4.1131 | -44.50929 | 2024-11-16 04:01:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea77734b-faaf-365e-9ea4-14b56f00ea19 | -3.56939 | -50.23739 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bf9448b-6124-345d-a4c8-7b96e19e1af3 | -4.01404 | -46.53846 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd7a0a43-5e6d-3bde-9a51-5b33f3d34519 | -4.22123 | -47.21708 | 2024-11-16 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 940fcd15-761f-393e-881b-62772b7a0f6d | -4.21874 | -46.81178 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ad736ee-9d35-3f16-a22b-1fb7043dbd02 | -2.66865 | -46.18608 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c929ec5a-62d3-3984-b2ba-a9adb05cb9be | -5.15488 | -42.96651 | 2024-11-16 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4841d7e6-e91c-3a9e-9148-7b65fd71a7f1 | -3.50403 | -45.44197 | 2024-11-16 04:01:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69f84a71-ff9a-32b0-b6c9-eb0cc5d7a4fa | -6.81118 | -39.2982 | 2024-11-16 04:01:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0110523-ca1e-3deb-a087-9751cf127e77 | -2.41342 | -47.03272 | 2024-11-16 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bbb5f37-878e-3476-ac06-43250eba69bd | -4.55598 | -48.01581 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 32cbbc37-c8f3-300f-9e6c-2934dc69753b | -2.35511 | -49.11371 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8321b097-643c-33d7-bbb6-94af8f88e136 | -4.7659 | -43.60446 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc403557-78cb-3c54-84d8-c14677f64c19 | -3.97181 | -45.80402 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e00f73f6-335e-3abb-bf93-a97d764885ce | -2.39414 | -46.31073 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d3f3ce6-ad53-3976-8e59-3a5c5614c801 | -3.7386 | -45.65738 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| bcb44fb2-004f-3f1b-aecb-d6d25d4282e7 | -2.14677 | -46.55796 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f283db5-264d-3b5f-8516-8cb82cb16b56 | -3.20861 | -46.68138 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11e7082b-e399-3203-87a6-74abb3f2ba5a | -4.72942 | -48.11548 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a0f77cf-ed35-3d8a-8d65-4eea911106d4 | -5.02082 | -44.44743 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 777ec078-d318-3f13-aebb-b76ba143f1ec | -3.88158 | -44.4959 | 2024-11-16 04:01:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98fd48d7-34ad-3ab0-9233-33cc1faa2467 | -4.22843 | -50.67751 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d564a698-58c5-3314-bf58-570a5e15396a | -3.73794 | -45.66148 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b101f3d7-6c57-3fc2-af4e-9db2425457bf | -4.25334 | -45.90696 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab52d300-89ec-30dc-9348-b9a0b94e6afd | -6.49972 | -41.575 | 2024-11-16 04:01:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5142947e-6f4a-36b3-a2c6-b361471191a3 | -5.95168 | -44.4694 | 2024-11-16 04:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db4abf20-6d36-34e7-b32c-4d366f52c045 | -5.55219 | -44.69458 | 2024-11-16 04:01:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47dc8883-e775-3f15-bb83-5b90a4fd42b1 | -4.66087 | -44.08343 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce7d06ea-a5f8-3c25-9845-1abfb44016a9 | -3.78153 | -50.10688 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a137b41c-2813-3aee-a81e-2472f9bd7e51 | -3.72995 | -45.65599 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 7e5ea13e-0a14-3d9a-8963-fe978047fc27 | -3.62475 | -43.15581 | 2024-11-16 04:01:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 503330a9-5ebf-3d7f-83fa-000d90cdb01e | -3.9181 | -46.52005 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d407e8f2-e7f6-3192-82ad-25e81c7e0535 | -1.97092 | -46.36813 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caec7429-377e-3251-aad9-e66164a8f019 | -3.49868 | -47.21848 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b9f740ce-ea06-3172-8699-bc13aae3d475 | -6.30329 | -39.48367 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ee27c34-bfe3-3ad4-b8ea-ea4949ddc26f | -2.88261 | -40.39189 | 2024-11-16 04:01:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 26f3c952-7d2a-3d11-ad10-7d57aed28c20 | -3.30779 | -43.46777 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d3026e3-fcc0-3149-b3a9-154573012f10 | -2.7462 | -48.56024 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee313a36-65bf-32a1-bb09-cc0b08486579 | -5.90342 | -46.23352 | 2024-11-16 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d35c4714-10ec-3bf4-ae55-0c40219c2ed9 | -4.23029 | -50.67861 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd254ff0-4e0b-3c5b-9112-1425ed719039 | -6.44453 | -47.86395 | 2024-11-16 04:01:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ad4b43c-ddab-3a3b-a68b-7a088f0977a5 | -5.90846 | -46.23011 | 2024-11-16 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a66e063f-12b2-3700-a4aa-dc50fd062325 | -6.05763 | -44.87711 | 2024-11-16 04:01:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afc2ae0b-034e-310d-91cb-e74f58ad4660 | -5.97714 | -45.3698 | 2024-11-16 04:01:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f5c8e6e-7c5d-35ec-a2ee-df76704c0ec9 | -5.67379 | -35.64749 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 52.7 |
| c5d8fcad-88c2-3e7d-aa8e-d2e6c3c722da | -0.78515 | -49.48055 | 2024-11-16 04:01:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d11a768-3321-3fb8-8624-5404df8ddc91 | -5.8827 | -42.54373 | 2024-11-16 04:01:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
