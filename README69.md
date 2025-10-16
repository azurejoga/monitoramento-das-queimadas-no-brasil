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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45b295f9-c8aa-305b-bc78-752b9b3f65af | -2.43955 | -49.37239 | 2025-10-16 05:06:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5e8f12f-524e-3352-8b96-9cc35a0d4d4b | -2.87392 | -50.74603 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1def4b3f-f9bc-3579-976e-d76f20a1d5b4 | -3.2848 | -50.15106 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14b19ae7-2eeb-3277-8741-cffa410b7a48 | -3.07043 | -49.38543 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2b6e3bb-d7fe-389a-9c80-75ebd71787b8 | 1.8567 | -55.77362 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e48cd7c2-ce9e-3c38-9d7d-f173281b37ab | -3.13523 | -50.2108 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 633b7a19-9015-3d60-be93-e0ca7cb85ee1 | -4.65656 | -44.09376 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbf2ca56-2ad0-31b5-8d6f-6db1df645b69 | 0.99405 | -51.08286 | 2025-10-16 05:06:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efdd670e-40fe-38e2-9cf2-f06025629120 | -4.37225 | -43.38462 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 64b0e377-6808-326b-a8cc-e311466ad31a | -4.36506 | -43.38882 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| f074c749-48d4-3ff5-b9eb-8238d895e9b3 | -3.23646 | -43.45763 | 2025-10-16 05:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 961dc216-8351-363c-b5e4-aa9676e306c0 | -4.36925 | -43.40567 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 101c1e58-8d9e-3ca6-b3a5-631e13608b95 | -3.59596 | -48.87677 | 2025-10-16 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a38d4ed-5da3-378d-959e-7897ad193737 | 1.84851 | -55.69972 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19f8b8bc-49c0-3bf8-9740-9f6dc4125b0e | -3.99534 | -48.33392 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5371ecc7-36c4-3e4b-8085-aed362fa7820 | -3.2167 | -50.21613 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6a77710-bf09-302d-9c98-c92e0bf1d40c | -3.56035 | -53.10129 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 253b7612-1f4e-3bc3-bd29-73aa148a6027 | -3.99854 | -48.34404 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f37db0fc-41b8-3463-988e-2fa82e8ccb99 | 1.83501 | -55.76944 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72e68e32-4238-3d51-bfb8-d1af87d4aac7 | 1.75295 | -55.77847 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9347a21-cfa5-3380-9058-2acbdb57cd35 | -3.02059 | -45.3777 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb97df84-42b2-33b6-b297-54b4c19d66f0 | -4.6634 | -44.09015 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d08071f4-e949-3077-9b06-e0d5b31b4655 | -2.70798 | -49.8608 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee2f88af-6f30-32ea-9c75-ba535bc4b391 | -4.25683 | -48.55254 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e697cb7-f827-3b92-bc46-17ac2f83b233 | -4.83 | -45.6582 | 2025-10-16 05:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b3305cc-36c2-3625-b8d4-f617dd3bded3 | -4.67448 | -44.10147 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f188427-7cc2-3be5-ae84-d927e5c20149 | -4.83056 | -45.65435 | 2025-10-16 05:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7cd8542-c05d-3288-aeac-94d35b44c77a | -3.43519 | -50.25318 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14aa10ee-76ba-31e1-a790-4e9bcc501cb1 | 1.75011 | -55.78268 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8c62381-45f4-3145-b3ea-32ee085b38b9 | -3.01949 | -45.38511 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| edc6275a-7996-35b9-bd67-45ada14a69f9 | -4.35713 | -43.39826 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09f0ec98-2452-3ac3-b9e4-905be9cb9d0f | -3.68167 | -47.63249 | 2025-10-16 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b9c6d75-a731-3ee1-b847-ebd5ef967b76 | 0.87688 | -51.12099 | 2025-10-16 05:06:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0292137f-64e4-3aad-b4e6-981e7b3639c1 | -4.67527 | -44.10488 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e8c9ede3-cce3-37de-8c4f-215987a03820 | -4.67595 | -44.10029 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 59852b8f-1965-33f0-9ae5-4dc93af44c42 | -4.21973 | -48.3634 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b25a670-ea35-3527-89a2-d4400026ef52 | -3.67224 | -50.27427 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4dba972-3d2e-30dd-bf65-99af2243b4dc | -3.49119 | -50.01854 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a75cdaab-7c53-38a1-93d7-62f5bb764515 | -3.4885 | -50.09164 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c1e3613-e748-3d76-8b52-dd863f993700 | -4.39086 | -43.39279 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 88d7c938-d02d-3c31-b940-310ca02aa65f | -4.37646 | -43.40131 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 774b94dd-4f12-3b09-b717-8f5104ba3369 | -4.15481 | -46.7984 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a28cff31-b56a-3982-964e-818b4484f4b8 | -3.68303 | -52.06364 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00bf9a64-d96f-38a2-8b6f-24e7a3e85b9c | -4.01672 | -48.96737 | 2025-10-16 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcaa7d39-2edf-34d8-a07e-c723a02ce881 | -4.39163 | -43.38743 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7267406f-8b60-3fbd-a9ce-3d808d51a702 | 1.89253 | -55.88892 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0069e8a3-4a3c-33fb-a456-e37a05f34242 | -3.86426 | -50.05102 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e35c22c8-f5d4-3d44-b8e6-5be9f2c41137 | 1.82981 | -55.7364 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3e67914-e8d9-3e43-90fb-abf146a18777 | -3.40953 | -51.56892 | 2025-10-16 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec30e010-cf9e-3162-a0c8-7d36f0160461 | 1.06466 | -51.1275 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d00f5a4d-4793-38a1-bd82-134daac33051 | -2.70389 | -49.86018 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3506b7b5-dfd3-334a-99ec-5cf8b62511d8 | -4.38858 | -43.40869 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 629b770a-17c5-3b93-9ad0-13d85a08c7e6 | 1.80379 | -55.8839 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5822944d-525d-3567-a6f0-afeb187dd9bb | -3.55994 | -51.11792 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ea9b00e-e225-3147-a1b2-413b60485ae4 | 1.78881 | -55.74279 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dffb595-faa1-38e4-95c1-01e4c75a08d9 | -3.01557 | -45.3731 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3df2330f-811b-3e9e-b55e-692b216ae13e | -3.28019 | -50.04517 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aae93a33-8daa-30d3-8aa6-4fe4b33685ce | -4.36357 | -43.39928 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 579bed11-604f-3f06-9dc9-a24726177306 | -3.51523 | -50.21522 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fbe22ca-dff0-3638-9325-8c8b81c88d44 | -3.05002 | -47.02197 | 2025-10-16 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ec15e7c-ad69-39cb-bd02-d9668916c9b6 | -2.8684 | -50.73042 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 86f53ce0-6896-3d0a-a514-752ba8cd670f | -4.28299 | -48.62722 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb94ade1-490a-39e7-84b2-80ff611f9cdd | -4.66287 | -44.10307 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| b16927e1-22c3-3c3d-8e74-69b6dc8943da | -3.07316 | -49.50864 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15260158-20f7-397b-9698-822a82c8ab74 | -4.37078 | -43.3949 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d3a44a15-827b-3bd8-8535-5731410018b2 | 1.83491 | -55.72433 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f3d079e-f2de-31dc-89e2-48d0da3cfd9b | -3.85015 | -41.5639 | 2025-10-16 05:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2a910eeb-4327-311c-9f81-94705d61cbfd | -3.20837 | -54.9629 | 2025-10-16 05:06:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f9b9afa-c0cc-3ba9-9793-1ae889ab8d0d | -1.65776 | -55.14053 | 2025-10-16 05:06:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69debd00-ff8a-373e-a958-d932b5dcf2c3 | -3.81577 | -50.93364 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ab9211-66e0-33c1-82ef-28d4c09c4de8 | 1.82186 | -55.75266 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb7219e2-de8e-3dab-a7fa-54d27c426769 | -3.47826 | -53.44979 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fee3f05d-ad5a-319f-99fb-25da657ce8b2 | -3.49065 | -50.02211 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42533da9-b1c8-3a36-9d65-8d8bc977059d | -4.80691 | -43.21078 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1744a562-2b82-324a-8765-dc85886ea806 | -4.12387 | -50.71968 | 2025-10-16 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89efff6d-fac9-3b21-9396-59d2cf243b83 | 1.74786 | -55.79056 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 566272c9-c8f1-338f-9098-44a265daeb28 | -4.65737 | -44.09735 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| edb1b684-0e3f-3284-a011-07b5337e8599 | 1.83212 | -55.75106 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7d36c54-772a-39e4-a2de-d1c84f37ef90 | -3.4821 | -52.86031 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b792d4-48f8-3763-98a2-b6c030678111 | -3.33352 | -50.1041 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5b470c4-3815-352d-956a-c81f3083b1eb | -2.79766 | -48.93945 | 2025-10-16 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 080654dd-5fc8-3047-9f1b-2086328e83ca | -2.87153 | -50.73584 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 824277bd-21b9-3624-8711-c37f0030dbb5 | -1.427 | -55.25285 | 2025-10-16 05:06:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35b5702b-6344-3e9b-830b-ba970bd56a58 | -3.05643 | -52.65282 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd6be696-f536-3c30-8e91-345b8230731a | -1.98697 | -56.91845 | 2025-10-16 05:06:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90e47044-5110-35e3-9f20-e134701369d1 | -4.11133 | -48.01994 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 0042ac0e-1bf5-3d58-8008-420f3c930527 | -1.48864 | -55.44044 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10c83075-d854-3ac9-a80f-29b34e861ea8 | -4.5077 | -45.40235 | 2025-10-16 05:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b560e149-aacd-349d-9e26-ea67302f1b69 | 1.0465 | -51.03723 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a11f7d68-12af-335c-9b77-c3c7d74d386d | -3.53107 | -50.30674 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88748e77-8ad3-305c-bca7-d1755f5f9fba | 1.43022 | -50.84671 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c2f7dd0-799d-39cb-a657-f3fb2237c033 | -3.13122 | -50.21012 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f012ed35-63ad-3e85-b615-890b7d1d6b0d | 1.22081 | -51.03249 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69e83bab-13c1-3ef8-b721-a49cc9a1fe6e | -2.88702 | -50.73821 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88efe4c3-b02a-3e4e-915b-ecb2d84982ca | -4.15644 | -46.79524 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 23d2805a-f74d-3df1-8fd9-0e26a963e9dc | -4.67662 | -44.09576 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7c42f438-3bf8-39f1-8f3e-827a9fecf6c6 | -3.33545 | -53.24736 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c52f670-0a99-321c-8a5a-bbd8269a4df0 | -2.71151 | -49.86499 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d0d7961-abe3-34ff-b0c0-beb8dc5f93a5 | 1.78596 | -55.74699 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4bc1bf4d-1cb2-3a69-b97d-d30f9b229c35 | -2.3824 | -47.71079 | 2025-10-16 05:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README70.md)
