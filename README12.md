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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a9f9f2a-6706-33e3-934c-422c39bd8458 | -5.96529 | -44.13948 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 82aae00f-e1d8-3888-8afe-55a76aafb3fe | -3.98148 | -43.24654 | 2025-08-21 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2587231d-bcfc-38da-97a7-9a85a2fc2de9 | -2.3882 | -47.65963 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70fa8822-ee28-370a-ac15-cb520c0836f4 | -4.64458 | -41.41259 | 2025-08-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e019a773-b342-3e44-bde4-2d9d239b8ec8 | -5.11791 | -43.21181 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cc8f61d-6587-379b-bf67-3459215f8f8a | -5.10384 | -43.15958 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38f5e022-985a-374c-be20-f5516a24692d | -3.99321 | -42.50896 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c3be300-254a-3bff-ab3f-b59ab0b038f4 | -5.59703 | -46.29369 | 2025-08-21 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b062876-3550-3b12-a85d-a0d40386183c | -6.06799 | -44.14373 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa346479-039b-37b2-ba7e-248b52707768 | -2.26143 | -47.85221 | 2025-08-21 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09c1c112-1e30-3f17-8e08-f47473b08f5b | -5.78686 | -43.60806 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2d88ecc-3005-3493-b0b3-470bf0c35f8e | -6.0255 | -44.36511 | 2025-08-21 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45a1a456-2533-3a03-b724-3d57d1e6e2f6 | -5.06996 | -37.7155 | 2025-08-21 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 35108df5-c844-3fb5-9a92-ff259962ad9e | -5.7953 | -45.07922 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2846ca3b-59e5-37e9-94b3-55da2460f23f | -3.99491 | -42.51457 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d1f792fe-b62a-3218-8bc7-bc2a38a928ba | -5.13266 | -43.09684 | 2025-08-21 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58050347-bdb6-3145-a90a-fdcd82944869 | -4.86968 | -45.04747 | 2025-08-21 03:47:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee49e1d9-2298-3df7-891e-9b6a98aa9f4b | -5.96062 | -44.13861 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 725b75c0-c9b3-3497-ab53-ce79db0ec251 | -4.65253 | -43.12678 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 04b5843d-4330-3136-be38-d65aef816815 | -5.39016 | -41.23482 | 2025-08-21 03:47:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f702bd44-a94b-38ce-b5fb-9677abf36162 | -3.98586 | -43.24458 | 2025-08-21 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e255ded-787a-32ef-9a7c-452992d83975 | -4.64806 | -43.12606 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 897aff73-cc12-3c78-be9e-a6575b5505f6 | -6.8194 | -39.89653 | 2025-08-21 03:47:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d047899e-7498-376e-bdb1-552882fdf5c6 | -5.96996 | -44.14039 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bb20b1f-e3d7-3f60-a296-08c395a405b7 | -4.94 | -47.46067 | 2025-08-21 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a990335-27b3-3841-a167-f9f4e60a9a8e | -3.03975 | -49.44616 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 522c816d-a369-3382-ac0c-ce07c3735aa2 | -5.98689 | -42.85025 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe3a04e1-8fe3-35eb-b066-76ada612953f | -6.20155 | -43.5726 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1328c0a-9ab9-3c3f-9fb4-8a5584f13e3d | -9.48656 | -47.32885 | 2025-08-21 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18757212-b473-35be-b5b7-f6983810d84b | -12.94543 | -46.23658 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 43c7d1f2-16a4-3537-9c76-840eab21ca55 | -12.95554 | -46.23545 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 39d0f1c3-9d01-3e26-a644-ca74697af180 | -7.23736 | -44.70713 | 2025-08-21 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 57dd326c-de9c-32b6-9059-0cee4bf4481d | -13.15974 | -46.90709 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 666ef46d-9684-334f-a2e3-619f30f6c8c7 | -9.55404 | -48.11928 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b8c9d62-9a5a-3006-92fe-ccafdfdfe481 | -7.95501 | -42.641 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ea29a186-812f-3254-9017-08d56c66e74d | -11.32725 | -47.83616 | 2025-08-21 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 756ce738-78a3-3bcf-934a-0f4ac3b0c1b8 | -11.5933 | -37.93594 | 2025-08-21 03:49:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9166e0be-32aa-39ce-be98-5e7042ae59e0 | -6.77058 | -44.33092 | 2025-08-21 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f01a950e-e4e4-31b9-aed3-e3899fac9469 | -7.21272 | -45.31236 | 2025-08-21 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44b53d69-abc3-3b13-80df-96b3c4b0fa21 | -12.64483 | -46.86865 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dbd025ee-e18b-3f28-93e7-d50d73246d88 | -13.03233 | -45.1837 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1c5fd4fe-239d-3782-a81f-5a3147e0abf8 | -10.71027 | -48.22798 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08dc8136-b8f1-38b5-a8ee-305095fcbaaa | -13.01733 | -45.19016 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39da72ba-3b80-3308-8683-6ca09f0f9a2b | -11.43695 | -47.32191 | 2025-08-21 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7e65bc8-4b95-3409-b9bb-c387308dbec3 | -13.01705 | -45.16672 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f491b46c-0ee6-3a77-8f92-6d250b158774 | -11.08879 | -44.81245 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3aa3dff6-d155-3ae1-a9b5-2c1183234401 | -13.15686 | -46.89508 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a252dc3c-7e7e-3c95-95e8-676ff70a59c9 | -7.99517 | -47.33883 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f30e0f24-a8f8-3851-9cab-8101df3ead3a | -11.17462 | -46.13842 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a46a4936-ed59-3b8e-90ad-1869b940e986 | -9.66524 | -48.38439 | 2025-08-21 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70dab672-bf8e-3e8c-b720-b0b79312f216 | -7.02951 | -44.62767 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e1609e98-d6de-328d-84bf-fcbe4a9ce4de | -12.93809 | -46.19684 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4fd32de-007e-3a7f-a9ae-88735224f832 | -11.29721 | -44.94142 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03c035fc-d10e-3a87-8dcb-185b41d487d2 | -8.27246 | -47.28541 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b4e6645-54eb-3367-a56c-3dfc34c91cc1 | -7.5912 | -44.38227 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd310548-df53-3cb1-a554-d33ad16a38ca | -7.14414 | -44.59296 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f2060cf-7e92-3eea-b89e-99dae7fdb672 | -11.43105 | -47.32416 | 2025-08-21 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd562af6-b1d8-3680-acfe-0deea644c6a0 | -13.27875 | -43.91658 | 2025-08-21 03:49:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b77605d-0b22-3bab-aff8-3b7859f406f1 | -7.15063 | -44.17898 | 2025-08-21 03:49:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b24a2eb3-02b2-3698-90b6-c5a3f2502994 | -9.10583 | -45.18046 | 2025-08-21 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1065e2bf-ea38-3273-b3c9-e9d188e84bc1 | -8.07312 | -43.67722 | 2025-08-21 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7b7ad47-3487-3e11-b8db-266b34056c9f | -8.34989 | -47.50535 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cbf6fd7-95bf-31df-935f-97c699af035e | -9.64108 | -40.60054 | 2025-08-21 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 19060e6e-3f70-3de1-90b8-bf425cff7631 | -13.02373 | -45.20543 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f47511e-0080-3037-bff4-c1d70f37ae34 | -12.64229 | -46.88216 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58ebc3ff-5437-3024-aaf9-85133051bcc1 | -13.01622 | -45.17124 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b388d4b9-ced0-39ff-98ec-33b9b44954c6 | -10.99351 | -45.62819 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8d70254-c2b9-3c3c-8c18-4825c84989c1 | -13.03181 | -45.21164 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 56a74e27-791b-3b70-b5f1-1297637a72be | -6.85931 | -44.41631 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05912854-2aa1-3ce3-bae1-6e21fc0426f6 | -6.58401 | -44.46672 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3abbcc6-8c12-3467-8e29-e0bdb8f3b321 | -13.02178 | -45.19098 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 611b9455-dc0a-3094-8ca8-ee2bb1f4cc06 | -6.49111 | -43.10738 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d87dcb4-c7db-310b-8e37-88c9b03227e3 | -14.53389 | -39.73585 | 2025-08-21 03:49:00 | NOAA-21 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d2a729d-e4f8-32d5-8423-9610957c09fe | -8.16596 | -47.33251 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81e2dba2-15c5-31f5-b251-02745d635fcb | -7.72381 | -46.61602 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3da4c17b-d197-3bbe-8d8c-4e2152ed69cf | -7.02736 | -44.61197 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3e01059-a235-3c48-986f-5a5f485f9a19 | -7.66082 | -45.25227 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92803332-1494-3277-8443-a31cbfdacfc2 | -12.97917 | -45.19699 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3284aab-f0c7-30b1-b904-70c249b1eb07 | -13.38187 | -46.22878 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbbe57f7-782b-3a05-aceb-4ddd5c2a4456 | -6.28665 | -43.8826 | 2025-08-21 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05bd7a3a-6829-3189-879d-225d27964cc9 | -7.95312 | -42.65221 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28f8bab9-1a72-30ab-af0d-8d81e2cb7b7d | -13.5923 | -43.35119 | 2025-08-21 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67c28911-9992-3023-ad35-84b015045acc | -7.03037 | -44.62271 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d7101724-7a55-3dc8-a100-6ed49cf4a606 | -12.08637 | -44.72649 | 2025-08-21 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bde6a2c6-61c4-3dc7-9499-090d91d88198 | -13.32947 | -40.33959 | 2025-08-21 03:49:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6bda7699-83f1-3f9a-8344-0b589c36099c | -13.01983 | -45.17658 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 5f3b9064-dbbd-3caf-92db-7f5300f08c38 | -13.17118 | -46.87397 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32eff4e1-f934-3a5d-a77d-b6190807a1cd | -6.34345 | -43.42626 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e2b8460-44a2-31c2-ad68-3e3c95a23e18 | -13.1995 | -46.88764 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e400c887-28a6-3c38-a46c-b7ee54a0a297 | -7.27234 | -43.68033 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f88eafa-021e-35f0-baba-8aa23d50b643 | -6.62185 | -43.88113 | 2025-08-21 03:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cfa42c62-8a74-336c-a07c-c8dcb02d137a | -12.06252 | -40.00723 | 2025-08-21 03:49:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 421855dc-2eb3-3bf6-b155-ff36388017c4 | -6.42129 | -44.67086 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c511ffa-e9dc-3474-ba6f-9d54a5b9fe1a | -12.98091 | -45.19794 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d579c49c-255f-3be3-a73d-032b0c66ee5b | -11.81858 | -50.6557 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7260df88-1a81-302e-92d8-8b39433ed5e7 | -8.17779 | -47.33102 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8239e2a7-39a3-3faa-b136-491883d9d4ad | -7.02003 | -44.6258 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 91c32ee3-5179-36ed-b67f-343b9b995181 | -6.50246 | -43.44533 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7b6b5d53-61bb-3231-b847-4e5763e2e8ba | -7.64356 | -45.24711 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7f59ee3-7a4c-31bd-a9f5-089a4dd57d05 | -12.08678 | -47.91788 | 2025-08-21 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)
