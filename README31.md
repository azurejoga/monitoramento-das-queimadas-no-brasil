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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33d42038-3e11-3d43-8d16-2f7ce2eefcc2 | -14.43738 | -56.46598 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e6e4093-feba-34bc-9e7e-4518d3d46229 | -11.27085 | -44.96905 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b64dca11-1695-304f-9383-b48172fdbe7b | -15.08266 | -48.66288 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb9f4463-ae39-3c22-aee3-8a43b20b7547 | -16.68072 | -49.16581 | 2025-08-25 04:17:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96e9d41a-b308-363c-81af-965f35635cd7 | -12.75181 | -44.41738 | 2025-08-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c4520c2-45e6-3a37-aba2-bc02f189c581 | -14.2638 | -48.02764 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f26f9a57-4c00-335b-b8f5-5b1c9169b6b3 | -22.17842 | -46.63055 | 2025-08-25 04:17:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d4fcc8b4-4c7e-398a-9d18-e1786736d8a3 | -12.73616 | -48.11916 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 85bcc267-b160-3d04-b717-3fb06630c850 | -15.0759 | -48.72413 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50083663-4a59-33c1-aad8-ed106d7127cf | -9.84168 | -45.96111 | 2025-08-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b93f646d-19ea-3e95-89e3-796df570c6cb | -14.71762 | -55.93121 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85e4d472-fb2d-3fce-953d-635a83681516 | -11.28862 | -44.96464 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddceefc0-0433-3271-8b48-40a4e4e35b8e | -11.6032 | -46.34418 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac11bebd-2747-373a-8ecd-5341596aa15c | -13.28604 | -47.51435 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fed91eb4-b3b7-3ed2-b59a-489f47fc4711 | -14.74148 | -55.93157 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4434ce14-3221-3df9-af9f-1aa8f4cc2daa | -10.0199 | -51.07394 | 2025-08-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ae1a366-4e8e-3502-ad8d-56512a1f70bc | -20.37912 | -46.74445 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 079a0cc1-baf4-3817-8c28-5cf89bb79ca6 | -23.32766 | -47.84522 | 2025-08-25 04:17:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f3bf473b-169f-3454-9dc8-3f5e306a3cc6 | -9.47707 | -57.81842 | 2025-08-25 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 015ba0d2-6ac1-3373-b5b1-65ba3da89f71 | -14.43467 | -56.46695 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3a9fbe6a-5512-368a-b700-6aa7314ac75f | -12.94024 | -46.31358 | 2025-08-25 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da74cf2e-0623-36d9-b28f-0090746ed819 | -13.48497 | -47.01897 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 620ba901-4d01-319c-9e51-7fe41160c95e | -21.63176 | -44.01991 | 2025-08-25 04:17:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a57362c4-943f-3af7-86a0-9d81197420fe | -13.4341 | -47.03079 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2791ad89-e391-35f5-8249-0f06b2b96a81 | -14.92778 | -45.52936 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c049b0ea-a6c6-38fa-8e26-c27ec7f2d490 | -11.27472 | -44.96606 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 797d6880-ecdd-3ba3-8c1e-47c9548e9371 | -20.90895 | -44.07892 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 335684f3-e5b4-3281-8b9f-c4d152bb6f4b | -20.73299 | -49.42691 | 2025-08-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79d39117-2b7c-3134-948d-3f804c6b8d1a | -13.4866 | -46.8817 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04b6fd52-44d8-3f56-b888-ae2662c7575e | -14.11459 | -53.99745 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cad3f57-de2f-3fc9-bd49-1866e2bcb5ae | -11.55295 | -50.52451 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf94b5bc-d556-39bf-b7fb-dfa09e7cb4a2 | -11.19571 | -48.47345 | 2025-08-25 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5477a784-7a38-3418-9484-9537de73c957 | -10.02533 | -51.06999 | 2025-08-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3573fd1-a559-3470-a616-790c99a03978 | -13.47881 | -47.01361 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19409cb5-d2e3-37c2-8ab3-e19f7e000d8c | -21.72889 | -46.81102 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b1d2702-95ec-31aa-82bc-7399dcbd4097 | -13.67031 | -47.97232 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67034546-0f88-3e24-a0bf-6399b2b1791f | -13.46302 | -47.00247 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 39699d92-9a4a-33df-bd74-25661724dd1a | -20.29891 | -47.18387 | 2025-08-25 04:17:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9b3c68c-2692-38fc-8e46-88b5b7eb1668 | -10.81948 | -48.32922 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63ee9099-d502-395f-97c4-8530ae92686d | -22.01749 | -42.09117 | 2025-08-25 04:17:00 | NOAA-21 | SANTA MARIA MADALENA | RIO DE JANEIRO | Brasil | 3304607 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3353f465-ed20-33d2-a9be-d2728ebfa5b1 | -13.61944 | -48.16316 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f418cea-716c-3831-82c3-8f3d6aca4a91 | -13.05539 | -46.31772 | 2025-08-25 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4d7052b-3161-373a-8c8e-1bd9c74d5391 | -20.51251 | -45.9947 | 2025-08-25 04:17:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b82930d-8a54-3757-b023-3cc1e2f1752d | -11.61646 | -46.24249 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd056cf8-70d9-3bc2-9e24-551e3264d41c | -15.06889 | -48.65603 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c2c335-4feb-3533-9000-c887236da8cc | -10.58723 | -47.14598 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7dd4ef2-6d07-31e0-ab07-5f737df47cbb | -10.83502 | -47.51364 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5836a2e3-cfbf-3b65-bd2f-d998c1a6db6e | -11.90529 | -47.12663 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01171d08-cdca-3d96-ab73-019489ead276 | -11.60756 | -46.36029 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c95b2415-e545-3027-a293-c49d3c02df02 | -21.12209 | -48.92108 | 2025-08-25 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1e076bc6-73ea-3f56-b9ff-e7cb9472692b | -13.63168 | -48.15659 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2ca319c-08f5-3471-92d4-237c5b039f69 | -20.51307 | -45.99101 | 2025-08-25 04:17:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21b374ea-648d-3789-9823-1cf1cd787833 | -20.72948 | -49.42623 | 2025-08-25 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88aba832-a905-3341-a652-48c20703f90a | -10.62582 | -51.61572 | 2025-08-25 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66c17b0f-5924-3e75-8b97-b7a6047d8b7d | -10.71417 | -48.30821 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24a94665-da1f-3507-a035-ca72bc2f51b2 | -20.36399 | -46.7757 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51713db1-7f47-360b-a608-424257703cac | -19.93907 | -47.49376 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f38fd2e7-6912-332b-8a45-53b8a9580af0 | -11.93274 | -46.7345 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd50b619-413c-3142-b9a2-b0006504285c | -11.60631 | -46.36782 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dceebc4-6584-3d24-99a9-c8bb51ab2598 | -11.46978 | -55.47716 | 2025-08-25 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73f9f613-2e23-3094-838b-de09f74a9048 | -13.50548 | -46.91635 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aea4a76a-1060-3d0f-a9f8-52347b1357dc | -13.50524 | -46.89652 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d881a4f-06ac-35d9-a893-3addac64b531 | -14.1049 | -53.99242 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 375d49ef-0684-3ba4-8d15-4f2dd4302b15 | -13.62453 | -48.15508 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c04374c8-7790-3b1a-ac02-4ec244b4cf0f | -14.24554 | -58.62264 | 2025-08-25 04:17:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 381c1e16-b0b5-3f61-95b2-ffeda1d9e7e3 | -14.26229 | -48.04156 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 41d34365-3594-3f7d-b271-6c74ee38cc2f | -10.73009 | -47.11407 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9a08e9b-9894-37eb-93f2-2b10b0476c4a | -17.18932 | -46.83554 | 2025-08-25 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fbc1c60-97e5-31cb-92d8-8324d0115290 | -22.88133 | -46.43378 | 2025-08-25 04:17:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1666361c-ca04-3e99-b99e-987fcae5199c | -10.61015 | -55.05923 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 815ef418-2772-374b-a89e-77037194b2ad | -20.295 | -47.18698 | 2025-08-25 04:17:00 | NOAA-21 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3938864a-8535-3471-b707-1dd2cc0e8d79 | -15.30642 | -43.79316 | 2025-08-25 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d02f8c2c-4fd7-3bfc-bd92-de651bfe5a8e | -13.15524 | -53.73879 | 2025-08-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87150282-6ef1-343c-b55f-6d7420c2d100 | -10.77949 | -46.39506 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15f747ac-794a-3458-af08-a2c8fd859181 | -11.15982 | -44.70271 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b95d75a-f6d9-3eb5-b75c-b3d44b1851a0 | -12.74773 | -48.13899 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8144d9b8-6bab-3a37-84e8-22e998a41b24 | -21.2781 | -42.81586 | 2025-08-25 04:17:00 | NOAA-21 | DONA EUSÉBIA | MINAS GERAIS | Brasil | 3122900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4e5eb9e1-803a-395e-9971-af2cc440b091 | -14.2644 | -48.02883 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8d784fa-c0b3-3a71-866c-80d4461370ed | -9.69069 | -48.33596 | 2025-08-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f2c994e2-6831-3078-87ed-3fc36a89e9fe | -12.74564 | -48.12938 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3620f46c-ffda-3381-bbfc-c8bfce20cdc5 | -14.37092 | -53.41928 | 2025-08-25 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45960dc0-8f89-356b-a84e-81a28e96b2a2 | -11.18206 | -55.02222 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c729e5-07ba-375d-8b3d-3a97722925ca | -10.59998 | -44.32507 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7643cf75-196d-345a-8437-26d2eca9754b | -12.75511 | -44.41791 | 2025-08-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21268ff1-59ab-3eee-aba9-a9299aa9cecb | -21.41718 | -47.59786 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b3182dd-5f11-35fb-9c7a-dd2f4a4a67d4 | -11.90414 | -47.12746 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d2ccd9a-bdb8-3f59-bbed-2cf1ba38ea2d | -11.0969 | -44.77887 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2172224-033a-3a9f-b697-d13927b5255f | -15.05616 | -48.51454 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6c1389c-f474-3b9d-8b40-a0337f20189d | -11.28469 | -44.98934 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4ee00cd-3c34-30d5-bf0f-e597450b7cb9 | -9.56288 | -48.17047 | 2025-08-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84756383-5218-326e-82cc-0c9a549978ff | -13.48837 | -47.01978 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 378d26eb-1976-3890-8d83-45d054595050 | -13.45368 | -46.91092 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9b15229-3528-3d0c-87e7-7cb6f03517e1 | -11.60634 | -46.32518 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1f7a272-4355-331f-9abf-53f733a543e0 | -13.44902 | -46.9179 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 167a008c-4dc9-31ae-a21e-099fdec5024f | -14.37416 | -51.93715 | 2025-08-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 93f26a24-54d4-314a-8ae2-526e1607c14e | -22.692 | -47.34824 | 2025-08-25 04:17:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 46d9be44-bc9a-3916-a1b3-5ebdb0ea241d | -11.93464 | -46.72291 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c557ae3b-0c2c-3136-8ff0-e394456b1143 | -11.14544 | -44.79389 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0edfed77-7107-3aa1-95f4-5968fd74d3fd | -20.37854 | -46.74812 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47f9d387-1fdf-3a14-a56a-31dc222f60f0 | -11.64049 | -46.22359 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README32.md)
