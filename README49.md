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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4b18be9-f6f0-3aa9-bd0d-4978f6eea0cf | -3.33905 | -50.81173 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b74cd0a-4d8c-39b0-92ef-a74790ef31f1 | -3.33208 | -50.80306 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd32f30a-2823-3493-8951-8183c6a4500d | -3.33147 | -50.80671 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38659a19-37fe-3be5-95f2-f3baa08fe00b | -3.28411 | -50.951 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07077ae7-8233-37e9-ac05-c10000943d62 | -3.27998 | -50.95034 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fb2b0a5-628f-3ca3-ba28-2030096a2f88 | -3.25945 | -51.24078 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fdbf88d-952c-3904-8ca9-7973cb21e030 | -3.23258 | -50.85126 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 050a3f00-ef6d-3b5a-b551-3dec007596ad | -3.23197 | -50.85498 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b28f9ba-484c-3e3b-9c0e-8119058e3ea1 | -3.16647 | -51.30596 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d84549b-6963-3643-91eb-a418326b618b | -3.16582 | -51.30991 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a14558c2-2485-3277-aadd-77f230249d7d | -2.97482 | -51.36709 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0d9a32da-d178-317d-875e-ecb91a4d6354 | -2.97119 | -51.36243 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 616b785d-48da-3bf7-aeb7-c1e0634edf1a | -2.97055 | -51.3664 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f31bff9d-9d6b-30a6-bef1-4f602276bd50 | -2.96862 | -51.11177 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f357851-f01b-3676-9589-a87279ac7d46 | -2.96757 | -51.35772 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 718d733b-2b97-3f84-8f05-485d1e077d4a | -2.96693 | -51.36169 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2b03448e-8e64-3d92-bdec-418cc4caa839 | -2.96628 | -51.36567 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c9c19fb-4414-3ecd-8df5-d249844a97d1 | -3.55577 | -51.60059 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d93e7961-c38d-3012-9868-70c116b8887d | -3.36666 | -51.51348 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17dc4b67-4e02-3ebd-9061-4f3c8a41a363 | -3.23136 | -51.20007 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99153c35-8a80-3bf3-823d-b464a033dbc3 | -3.17804 | -51.23549 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61167fce-2c0a-3910-971f-9e439cdca705 | -2.97611 | -51.35912 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40848fd8-6f5e-3b13-a4b3-67262e7a3c6c | -2.97184 | -51.35843 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c3acb17-b7d3-3f93-8893-f58fa269b8c4 | -2.64498 | -51.70649 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b506416b-da27-3236-8b4a-f1ee4e35c30e | -2.64477 | -51.70766 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d1a2b82a-88a6-319d-80ee-ddd104cdb6df | -2.64409 | -51.71194 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5edb1f40-09fc-331e-84b9-f75ec0481417 | -2.64037 | -51.70694 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46f163f2-26e4-36fc-a328-a08256e31e3a | -2.6397 | -51.71121 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82970bf2-11a8-3bd2-a5cb-b6c602746c35 | -2.63598 | -51.70621 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2561e414-880f-3c5e-bfd0-9212123903b6 | -2.58364 | -51.92126 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94cbb02a-db34-33fd-b4b1-7a168d04feec | -3.49509 | -50.80334 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21f244f2-8128-39e7-95b7-ed6fcfb13c04 | -3.49015 | -51.58206 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd7feb00-7dcc-31a6-91be-85119ba81114 | -3.44446 | -51.59127 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f91dfefa-1d86-3a62-a30b-280348b2577f | -3.38854 | -51.35295 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5917ba2b-07fc-36cf-8d6c-9e7d6fcf3ddc | -3.33556 | -50.80739 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 425d3b68-21df-3301-9396-476b007eb516 | -3.33496 | -50.81105 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 001d12ce-dc86-34f3-8b97-52a244434241 | -3.28057 | -50.9466 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8934195b-747e-3508-aabb-908c692d03b7 | -3.27938 | -50.95409 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6733b6ec-9829-317f-a709-e5a10cd9a65a | -3.27644 | -50.94591 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e3a2c64-0958-3e03-a3aa-b727553032ad | -3.27584 | -50.94965 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a528c898-477f-39c0-8cee-d401cc321a01 | -3.26757 | -50.94831 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b21289a6-c2f4-321b-bc3c-5283bca86f32 | -3.26343 | -50.94769 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fabbf992-842d-3dc6-8636-ceae678dffa1 | -3.25965 | -51.23974 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba32f16-3ada-3e4b-88d3-4db455652da1 | -3.23669 | -50.85196 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5ac89f5-6c75-33ca-9fd1-d34e69d5ae3a | -3.23319 | -50.84756 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c659a5c-8e38-3ffd-850c-e24b8513f95d | -3.22848 | -50.85056 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdba1933-89b2-3465-9890-538826144f23 | -3.21038 | -51.01226 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9eb20e8-346e-3f20-a5c8-b2fe95496f97 | -2.96991 | -51.37037 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d21cf51-a721-36e2-b5ca-944363602b76 | -2.89791 | -50.70813 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc1fe40c-5351-356a-9907-31c5f54fd015 | -2.89733 | -50.71179 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e06afcd-2910-3d9d-a011-d4a23afd5640 | -2.80637 | -51.60114 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aad89e1-54fd-31cf-bd7f-f09a8ab9c12a | -2.8057 | -51.60527 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b36d57e5-ee8e-3569-8f08-1519f6796e55 | -2.80274 | -51.01106 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9a3b2c4a-0df3-3617-9c1d-ff9de345e4c2 | -2.80212 | -51.01491 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a5e5ed20-220a-32e1-99ab-e0dcb5efd622 | -2.80149 | -51.01881 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| bb1d3eb2-28fc-3bf7-9ac1-04031f0cf87d | -2.79793 | -51.01431 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0a583bf7-5974-3f70-a605-d128d51f4120 | -2.70583 | -51.39178 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ec4cafc-919c-31c9-af62-521dd4a18cc7 | -2.64428 | -51.71075 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4e3f6cbd-ff75-3ef5-93d2-a3182bfe2fdd | -2.64059 | -51.70576 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af3d2ac4-671f-35b8-8e53-14d2897991f4 | -2.63988 | -51.71004 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9fb284ba-43df-337a-8184-f5dffb9c74d8 | -2.6362 | -51.70505 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b67ceb-c53b-3200-9b71-87ee76364aff | -2.63291 | -51.75424 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ff3607c-2f57-3625-965d-56166d9a9353 | -2.60734 | -50.69652 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc0342fa-f9c8-3f60-aa92-406581c7d034 | -2.60674 | -50.7002 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0f9603b-9a96-3ca9-b984-fa319bb76eb0 | -2.58293 | -51.92572 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 336ee9d1-6f0e-3c7a-b314-45bdd174bc76 | -2.55979 | -50.84536 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2727231b-c4a0-3079-9139-53f1990c6c0a | -2.44581 | -50.99496 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a09337b6-0c9c-394a-b242-f5c8de52d958 | -2.25294 | -50.70499 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cda5a9f-44f9-3f4e-bdee-ef76b0c30f34 | -2.24881 | -50.70431 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08619273-3180-342e-8f7d-3bd87284ae81 | -4.06551 | -51.11276 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c1afc83-e353-3254-8af1-123fad23b1d5 | -4.06139 | -51.11205 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fce98e69-0837-307a-9a87-42c180a87d3a | -4.06081 | -51.11559 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a76db72-fce5-3a8d-be98-b54ba3428a9d | -3.92135 | -51.22483 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6995ff99-8cd2-3e25-9ebf-d69ff4c5fbab | -3.84639 | -51.25657 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d5d5eef-fce2-3252-ac70-9d4b50f8f0a2 | -3.80777 | -52.26293 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac49f1b5-151d-35ce-8ca0-535afe69d3eb | -3.80328 | -52.26222 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b57e024e-f1dc-3df0-86b7-85b3e12142d7 | -3.78702 | -51.38103 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8347acbf-e778-361a-b9c8-7eb3fbdb9f80 | -3.68562 | -51.12278 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ec73759-e6cc-30d6-b62a-72c97c18d117 | -3.68462 | -51.07612 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b3e6a32-6ebf-34ac-b52a-af8296edc518 | -3.68047 | -51.07545 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48ce8394-e5f5-390a-b54f-ef211b370c7f | -3.67731 | -51.12144 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b83d8f80-295d-33bf-b23b-da7466d56081 | -3.67254 | -51.12452 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb53e10c-16d3-3430-bff4-b9cbd283ff52 | -4.65558 | -50.94963 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66ccdf7e-a210-393f-a81d-794e12557971 | -4.65499 | -50.95324 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb72e004-a738-35bb-9ac0-938d62ce8668 | -4.65094 | -50.95254 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9c04d18-4647-3951-a335-4a2cd0bcacf9 | -3.85057 | -51.25726 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e01f404e-08af-3dc2-ab93-9040c1a1c983 | -3.84577 | -51.26038 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73056e8-e11a-391b-bd42-66890f219e77 | -3.84015 | -51.2947 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d87d3f85-bc62-31b6-9b6f-e96b4b6fca0a | -3.69099 | -51.11589 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2767f4bf-c57b-325e-8565-90ce23cfdd20 | -3.69039 | -51.11964 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94017317-affa-38f4-b77e-f0f9d40c4b69 | -3.68623 | -51.119 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c1ae04c-63cb-3a02-915b-f064229b8bc6 | -3.68522 | -51.07237 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bbdae26f-9871-3f39-b3e9-3c3bf9159325 | -3.68207 | -51.11834 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02fbfb74-172c-30e9-84f5-67d9ea0d77d9 | -3.68108 | -51.07172 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b8d184a6-6581-3cce-b5a8-3433e3ca5c42 | -3.67693 | -51.07104 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 464125fb-4d28-3a1d-985f-e9f5e4a33731 | -3.67669 | -51.12526 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 564b675a-7f71-339c-bb2b-74587e7893ca | -3.67633 | -51.07476 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62597d63-e6a4-372a-8f2d-0390924ff05b | -3.92197 | -51.22106 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b47e920-cb3d-33bb-ac99-aac73594f7fd | -3.89621 | -52.27171 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80dc41f3-36df-36b2-b891-b6a17707f520 | -3.88407 | -52.12441 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README50.md)
