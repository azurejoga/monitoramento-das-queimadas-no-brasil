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

## Dados Diários - Página 399

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebb7ee2f-e0cc-3e78-b17e-df599436bd75 | -3.188 | -58.6241 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 308c05b4-a270-3369-9a2d-911697c0e487 | -3.8749 | -55.9961 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b3562044-29e3-3e8a-9b6c-074ee87598a3 | -5.2352 | -56.109 | 2026-10-08 18:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6f1740ab-10d8-30fa-b1bc-7c45f4b4eef3 | -7.0706 | -52.6764 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 3e53f6c2-d747-3710-9a37-b56a6ef72b3e | -2.5069 | -47.3771 | 2026-10-08 18:50:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8571fd0a-f866-3c5b-b472-7ca2f565064f | -3.2137 | -42.953 | 2026-10-08 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 343.3 |
| 55d6775e-cb8c-3458-920f-eb1e8bff184a | -6.1217 | -53.0584 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2b06b816-15a3-35c2-97ee-3568aed7d90b | -5.3955 | -45.8746 | 2026-10-08 18:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 1eca7e79-045a-3f90-8d72-ff38e0ffc226 | 1.7672 | -55.5463 | 2026-10-08 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 73776d50-aea9-3d7e-a678-43345bd69c64 | -3.2136 | -42.9764 | 2026-10-08 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 270.9 |
| ad04e0d6-cf09-3bbf-8f29-e1429100b879 | -6.2162 | -52.7876 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 92817c21-f3f1-3f9f-9b1b-526784e10383 | -12.2278 | -43.9245 | 2026-10-08 18:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 490804f6-23a8-304f-9785-5f0ded35480c | -2.9979 | -54.7692 | 2026-10-08 18:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 08b9f5b8-9fe5-3bdf-bcb1-204932e19ca2 | -4.0837 | -44.1389 | 2026-10-08 18:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 2e321f58-b824-3698-81c2-d701f8216ccd | -4.0629 | -51.03 | 2026-10-08 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| bf1dafb3-27ff-3d63-b413-7ed8db735332 | -3.5726 | -58.5581 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 037c29fd-bbc1-3815-bfaf-9cea5f25c316 | -3.2717 | -50.3893 | 2026-10-08 18:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fb377c70-f054-3db9-838f-8a1cc9688afc | -5.9586 | -55.3648 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 90852a36-6bae-38b8-af91-f68e483169e6 | -16.3213 | -44.5598 | 2026-10-08 18:50:00 | GOES-19 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 4e6bc94c-d21d-380f-9817-edfd7ae68327 | -6.9331 | -43.6566 | 2026-10-08 18:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| fff7f4c1-408a-3439-9c16-21eb2c45c229 | -6.2155 | -52.8899 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 285.2 |
| 71100285-6c5f-3851-9599-521af4f28d61 | -5.9587 | -55.3448 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 4df0d22f-5ab8-3bc7-a8ce-3c6d577eeb53 | -11.7742 | -43.5245 | 2026-10-08 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| d000b32f-a1dc-3d03-9faa-33a70537953b | -3.1115 | -53.7637 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b2938947-d275-3f3c-9bdd-467c7df62b93 | -1.146 | -54.2199 | 2026-10-08 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 59ad2420-692b-3fb2-bb6d-a790c295b4f4 | -3.1697 | -58.6437 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| d0d4841d-7955-304e-9bec-3c5a1c73ffcb | -3.4095 | -58.0013 | 2026-10-08 18:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 25ed9013-ca4d-30fa-be28-e34e1a46359c | -11.6382 | -43.6166 | 2026-10-08 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| ff607319-ed1a-3bd4-a31a-ad74df855030 | -7.5882 | -42.3925 | 2026-10-08 18:50:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| 7d5b6f97-a044-3a21-914e-d54979fed9e3 | -6.509 | -55.9554 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 10cb8a9c-7dff-39bd-a298-4564e05c2636 | 3.5448 | -51.2772 | 2026-10-08 18:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2a27268e-5d9a-37c7-9b39-b407372c7bf5 | -5.246 | -48.4103 | 2026-10-08 18:50:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f650045b-f10e-3792-9869-7b419ec89da9 | -6.8762 | -43.7083 | 2026-10-08 18:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d69d534a-db7f-3258-b9fb-f30871bf149e | -3.195 | -42.9772 | 2026-10-08 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 73edb0e2-c898-3ccb-8c47-de11e01f7380 | -11.2482 | -46.2604 | 2026-10-08 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| a6dad7b9-f1c5-33a3-8230-37d75873da26 | 1.6938 | -55.6066 | 2026-10-08 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 848ba413-acdb-3dc1-a90d-034207ba9c5e | -6.4905 | -55.9563 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 292.7 |
| 1985eab9-bc41-3195-a170-28338a05b889 | -3.2944 | -54.0207 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ec229657-e037-34e8-9ee8-d3c9454c70ca | -5.9587 | -55.3448 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 38ee9464-5aec-37cc-8763-1ea8015c4af5 | -8.0947 | -39.8753 | 2026-10-08 19:00:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 7188201f-3d04-37f3-9be8-137957d99e00 | -11.7742 | -43.5245 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 468a8bfc-44c6-352c-8515-06874b05448d | -2.5903 | -56.1642 | 2026-10-08 19:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| baf9e828-7d42-384b-bce8-1f1882fac848 | -15.1051 | -43.6409 | 2026-10-08 19:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 295.8 |
| 916287aa-3dd8-3845-a2b3-e9fb2ad4ab2c | -11.734 | -43.6254 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5dd62780-86df-38ad-bae4-e44c7ea23c10 | -3.195 | -42.9772 | 2026-10-08 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4bfa940e-c664-3a1a-8fbe-944ddda63203 | -4.6642 | -56.2083 | 2026-10-08 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| f8fbfcd5-6613-33e2-97fd-22652c4e8316 | -2.8434 | -57.4696 | 2026-10-08 19:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 62291779-d327-3d65-895f-979e5f46dade | -7.5882 | -42.3925 | 2026-10-08 19:00:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 89f29e46-7872-3a50-8131-85e6b9612d60 | 1.8222 | -55.5258 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0638863e-b8b7-344d-bfe7-c5be01654028 | -3.2761 | -54.0011 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a4170889-9d34-30e3-9f34-cab4b97dcdf6 | 1.6938 | -55.6066 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d0ec9877-9f93-3445-8186-678bb5284545 | -7.2184 | -55.1216 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 223053af-7c86-30c0-9579-22a19b77c667 | -7.2371 | -55.1005 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 28421609-6d2f-3781-bf53-38aea664ee82 | -6.1484 | -51.927 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 57371b59-026e-3f64-9a4d-81033c5e8473 | -8.5313 | -46.911 | 2026-10-08 19:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b5964de6-4299-338f-834e-bc5d3d5317dd | -6.2162 | -52.7876 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 1b782fb3-9589-3ea2-a2fc-d26bf84c5721 | -7.4694 | -42.8551 | 2026-10-08 19:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| a72f9a49-278c-3952-8f31-56af1bf571b3 | -3.2956 | -53.6984 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 0c827c08-38ef-32bc-84bb-db3ccb72d840 | -2.1361 | -54.4671 | 2026-10-08 19:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 2736f567-3aa9-3bc8-b187-6cea0d5539f1 | -3.2717 | -50.3893 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 461c6eee-2fd7-3af3-9c01-cac6e32eace4 | -8.9775 | -45.9023 | 2026-10-08 19:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 292.1 |
| 569fc1df-b4b7-3cfa-ab4b-33727c5dc5a5 | -6.4752 | -55.48 | 2026-10-08 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| b60ae87b-78ab-3a92-99cf-7182096aef39 | -6.9328 | -43.6799 | 2026-10-08 19:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5bfe7775-6839-30f6-a807-5090ef7eb912 | -7.5126 | -47.3358 | 2026-10-08 19:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2678ef1b-ba7c-3c20-a908-2b5bdfa16e42 | -7.0706 | -52.6764 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 16278df3-6a86-3521-bee4-3a04719f4fe6 | -5.4956 | -42.8648 | 2026-10-08 19:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 7b3bdb85-a0ca-3416-92ec-d8f5b66058e6 | -6.2542 | -52.6625 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 0eb053b7-a882-3eb2-bf94-cc72a3475e69 | 1.6754 | -55.6266 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9cecacf3-1c51-3702-842d-8b91ea84bdf9 | -3.2945 | -54.0006 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| a720739d-0d9f-399c-b302-54579f3e3e05 | -2.5492 | -58.0373 | 2026-10-08 19:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 220.3 |
| 2f9328f3-a1eb-3cdd-abfa-1c624d4e816b | -5.8615 | -45.9551 | 2026-10-08 19:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4a649288-215f-3002-88de-7b363c2e9184 | -2.8571 | -59.2641 | 2026-10-08 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2638929b-ef49-3c41-b075-20cd1f338c45 | -2.77 | -57.5293 | 2026-10-08 19:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 283b3bff-41ff-32d6-b1af-801af5c83cd9 | -15.1248 | -43.6369 | 2026-10-08 19:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 098bb318-eabd-3f56-b469-501bc0e8d6ac | 1.6937 | -55.6461 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1a6db482-2b7f-3f40-8fc3-daec357a294a | -6.0556 | -43.1493 | 2026-10-08 19:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 3847528f-0eaa-3f2a-b30a-1176062bd5be | -5.8842 | -43.4199 | 2026-10-08 19:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 219.5 |
| e3bcd51f-21a9-3dc0-bc6b-b871b83c2e49 | -3.2137 | -42.953 | 2026-10-08 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 523.0 |
| 6c648375-9386-3a66-b36c-e060d94f7c74 | -13.8655 | -44.14 | 2026-10-08 19:00:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| e609e579-8bff-3b9b-a8ff-7116433cfa5e | -6.2164 | -52.7671 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 07b55cf2-6cd3-3127-ab80-f335c7f93d2e | -3.2957 | -49.1202 | 2026-10-08 19:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b2ad13fd-d59d-316b-a0b8-4932227c9613 | -6.4596 | -55.0415 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| a4118c08-b016-39d4-9ed8-4be3f663ddc7 | -8.2823 | -45.7264 | 2026-10-08 19:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 54948a49-b6ba-392c-917a-1a10cafeaf16 | -5.9586 | -55.3648 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 2cba5282-3135-3e7e-b8ed-318c1f67c218 | -2.9265 | -54.1104 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c4c4af7b-6bbb-3821-863b-91d058c8b1ac | -7.591 | -47.0201 | 2026-10-08 19:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 5dea9d2e-264e-310f-b118-193d04046f1a | -3.1601 | -50.6021 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 94f213b4-fd6c-3e80-9266-7dfccec6fd73 | -13.3476 | -43.8776 | 2026-10-08 19:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 9b473b13-3c53-3250-ada8-b144c352be50 | -7.1998 | -55.1226 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 1e076281-98c5-3c4b-a303-3917aebb514b | -14.0472 | -43.8222 | 2026-10-08 19:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| f6c10704-0d5d-3dd4-a853-9afddbad744b | -6.1617 | -47.9201 | 2026-10-08 19:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b2c23c7a-45f2-3556-89e4-455193dce96b | -3.2532 | -50.4108 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| ed238707-2ebf-38be-b6a5-a43fa3ed62c5 | -6.0609 | -42.608 | 2026-10-08 19:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 13ba5ba0-f245-3783-8449-8cfd7566e17c | -13.8855 | -44.1127 | 2026-10-08 19:00:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| bc3f5de4-0767-3497-a8cf-23a5bdfdc278 | -3.3139 | -59.3898 | 2026-10-08 19:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 141.4 |
| f8fcb2cd-e32a-3cb8-be0a-0e5ea358b1a2 | -3.86 | -44.1274 | 2026-10-08 19:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 358011b8-d7d2-3adf-bc6c-b84006a20f6c | -4.0628 | -51.0508 | 2026-10-08 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a5a4f443-ffee-3b52-a028-14a8bef79d5f | -3.6602 | -54.532 | 2026-10-08 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 01ccfc62-2324-3b02-aabd-7194d2519555 | -2.8346 | -54.1326 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 243.1 |
| f35a7c9b-e673-3830-a78f-812ab393b5b5 | -6.1042 | -55.6964 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |


[Clique aqui para ver as próximas entradas](README400.md)
