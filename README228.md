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

## Dados Diários - Página 228

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ef65716-4b02-3386-a9b3-3d85809a3332 | 1.75795 | -55.57327 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c064b339-8c31-35d6-b848-c29f604484cb | -4.53748 | -55.61049 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 5cfdff54-5a25-3921-9b77-4e6bbad6dc7a | -3.01383 | -54.06355 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6986a93d-22a2-368d-918d-55b3c22beb98 | -3.27918 | -50.43364 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 250e1a2e-16e6-34fc-af23-5532036a67f2 | -3.28308 | -54.05761 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab81ba56-c907-3415-9217-5770eefb4e93 | -3.09566 | -51.38049 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d1d8edde-aa78-37ec-a618-391540dd4cd9 | -2.56467 | -56.16394 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b650620b-a15d-3c6c-86ba-610c2254c26c | -3.30263 | -51.11166 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 90b56bc0-c181-3779-bc78-a5de73ada57e | 1.63852 | -55.78571 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 299a08d8-ffee-333d-a126-0c90dfc743bf | -3.22371 | -54.30261 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 240427be-af44-34e1-b8c4-e4605620dded | -2.97043 | -57.0616 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e49d15f1-3ac1-3447-8798-550029ff70e4 | -3.86897 | -55.99589 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb32ad0a-2795-3bfe-921e-b76ccb193865 | -1.72202 | -50.37152 | 2026-10-07 16:39:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| ff3c800e-cc1c-3773-8bc2-dc266dee21f9 | -3.01696 | -57.73555 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 26fb533f-2b4b-347e-bb2a-46cbb15a1c22 | 3.22761 | -51.30495 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 307a590d-980f-3b5f-a502-a1c92dd48597 | -2.83356 | -54.12885 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5e360c01-2bc3-3d6b-bc71-b58314a769e4 | -0.78051 | -49.27084 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 083cf190-3c3d-306d-a3e7-e3f333248ec2 | -2.91211 | -54.10006 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8055a84e-598c-39e9-a5c7-254ac9473add | -3.84695 | -55.97423 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| e523aacc-2fdf-3df1-8b8d-a4c0ede289b5 | -3.02959 | -53.89528 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4fe602a1-66a9-3f6d-8071-bea73f575bf2 | -3.28942 | -54.02538 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c85a504a-4943-3b78-acf5-51db59468799 | -3.04892 | -54.14956 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7723c14d-05f8-3ecd-b3b0-68de6c60e781 | -1.19625 | -54.20873 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| fde81cc8-4948-3107-9001-f986379aa876 | -3.10469 | -54.18293 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 557c0083-6492-3320-a3d4-91476ca12cc3 | 0.80957 | -51.22582 | 2026-10-07 16:39:00 | NPP-375 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c408073b-499f-3be6-ba56-d80c98445b24 | 1.65103 | -55.8153 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 01742d37-3dff-39f6-9729-cea1fdeb2dbf | -1.28358 | -54.56044 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 894cb285-b29a-3efd-8572-b6aa682e1412 | -1.81915 | -47.8515 | 2026-10-07 16:39:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a654af2f-9f48-3978-95aa-92a79d31ad5c | -1.51972 | -54.51511 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 638df44c-1de1-3a57-a6cd-6bf82fa92fcc | -1.80745 | -57.11831 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c7a39dfe-92cb-30fc-9cdd-93791172c0d1 | -3.03424 | -57.48199 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 326ea92c-fcc9-3d7c-82fc-0e8e34797958 | -4.76698 | -55.72771 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2817d249-a039-38ce-8ade-74c685c16ef7 | -3.9716 | -55.8423 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4517da59-6425-3a9f-abd3-bf258d6ba344 | -3.16137 | -54.7256 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 2679d9b8-0fa0-3a64-9bcb-c3335bbaa1fe | -2.35555 | -48.85496 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 01dda931-68a3-317c-a816-7fe54fcbb5f9 | -2.94927 | -54.1889 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ec9a1c3-e184-3c23-b1a0-68b86b24aa07 | -3.30028 | -53.8756 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 027d4a39-10c9-3283-abd7-8d28c9b26c45 | 2.18744 | -50.97919 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f7a2018-2024-3249-b76a-c4dd3b5d0ac9 | -3.2721 | -50.41483 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b67ec009-7df0-3394-ba11-082acb73301a | -2.75117 | -49.53117 | 2026-10-07 16:39:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b0482567-4123-31d0-a93a-db684e426b3c | 1.47849 | -50.76199 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 92abdb67-bd5e-372b-919d-aa20bff6f232 | -2.8225 | -54.1021 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7b7ae5fd-f3c2-35bf-be8b-f194ae54e78b | -3.99188 | -56.25637 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cd0ee428-c95b-3f9c-8107-a99369bfbb77 | -3.27077 | -54.04898 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cbc2c823-348d-38ce-a696-d9f92595a9b4 | -2.64446 | -56.54615 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f160cfb2-b900-3bb0-bc1f-5800b955be8d | 1.75637 | -55.58739 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 232dd213-5c11-3345-83d8-e1eaa930826a | -3.57817 | -54.66301 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 84ab82ba-a6dd-3145-a71d-cad85f9b96b1 | -3.9516 | -49.01507 | 2026-10-07 16:39:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4bfffc39-912d-3562-85bd-5e88d30ddba1 | -3.02376 | -53.89271 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6836d348-4604-32cb-af08-4d896ed65fa9 | -3.04558 | -53.93018 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 44a7b604-e6a6-3542-bade-bdcd22ae1b7e | -3.00496 | -43.3255 | 2026-10-07 16:39:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 31278860-17cc-39cf-8537-ba27740165b3 | -2.49553 | -56.1162 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a4350742-dd0c-38f2-9873-b7cd8a5d0b3f | 3.212 | -51.29889 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8992ce67-d467-3a92-899e-91d9c0370935 | -3.17865 | -49.45259 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9067ca06-be1f-3c22-8944-79c3948ee068 | -3.05119 | -54.38808 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 01bf3d47-2fb7-3cc4-b61c-09bb8b203c98 | -3.19068 | -50.56511 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9b4a6570-ffc7-3162-b4ce-eff4f6bdcb6b | 2.43906 | -50.83314 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6a1c5233-11bd-34b9-8422-475ed1037dee | -2.93931 | -54.11979 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d28ab22d-3791-3fc4-a52e-de5bc60813ca | -1.55131 | -45.09081 | 2026-10-07 16:39:00 | NPP-375 | APICUM-AÇU | MARANHÃO | Brasil | 2100832 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cbdda44-90d1-3945-a486-a03945b5e1fb | -1.48158 | -54.49462 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4189daea-5942-30b2-aa6d-cbc6226a088c | -2.29942 | -56.77448 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8d1b204-d56f-3687-9dcd-6bb4203077c2 | -3.03963 | -57.49645 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| cd080b28-8cf6-371e-8172-bdeb44838f2c | -2.49438 | -56.11259 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b3368d08-4f21-3e9a-9dfe-00334039c9d1 | -3.35556 | -51.62502 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c878c688-5880-37ba-9803-e288e615951b | -3.65466 | -50.94619 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 3f09289f-4496-3421-b42c-b3ba3f3eba0a | -3.19744 | -50.55204 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| ab76da67-ee0b-301d-b1c7-fd31a5964030 | -3.99747 | -56.25028 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dc34327e-347e-3ced-9d0a-e2d8af7189ee | -3.10858 | -54.1716 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 0cc41a77-464e-34b4-9712-f62b3517d61f | -3.05892 | -44.44617 | 2026-10-07 16:39:00 | NPP-375 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fd329ee1-7425-3fc1-96ba-734953ce068a | -1.38211 | -55.19321 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 26fb1933-be82-3751-9f38-2cc8eddabb01 | -2.49832 | -56.13445 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e126fcd4-2251-36bc-8808-1af5463d50f7 | -1.80023 | -57.11432 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| bd6d1e25-636b-3f44-952c-7de937a50912 | -2.99125 | -54.05994 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c024ed99-3d17-3c3b-971b-d6fd24ff585e | -2.13498 | -54.45866 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 421b36bc-ee78-396c-87e6-808b377c6e24 | -1.28503 | -54.55955 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7772f647-a932-3143-8c32-233c5ac9288a | 1.69754 | -55.63462 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 1625b611-4530-30b1-8c7d-5a7360687938 | -2.68809 | -44.30198 | 2026-10-07 16:39:00 | NPP-375 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| edaf4526-3ef0-3b61-b934-0d42de537c2d | 1.70551 | -55.6206 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d7ee47fb-e6b2-3a7b-9412-323860f32305 | -3.97907 | -56.05526 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5b94ba9b-428d-3ac3-8277-9dca297019bf | -4.53877 | -55.61982 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 771c7df8-a52c-3a7c-95f9-45a5eded839f | -2.52386 | -58.10494 | 2026-10-07 16:39:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3bd8995d-c66b-3c84-b6b4-0883210dab30 | -3.15698 | -43.92063 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 212c34ae-7abc-35cf-8c9e-6307de0b2ca5 | -3.08723 | -54.29276 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e307dbbc-9da3-3c76-8eb9-e1197ec41d7f | -3.1047 | -57.65856 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a953bfbb-6642-3fec-9438-400a6a0c631f | 0.81015 | -51.22202 | 2026-10-07 16:39:00 | NPP-375 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 200a0baa-1bc0-33db-bd45-a489c00e8665 | -3.50439 | -54.64669 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 952c06c2-1e37-3d51-8a6a-dffd03151401 | -3.29634 | -54.03488 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ea75d1f4-01e9-3825-a6c2-7257789452c7 | 3.223 | -51.30783 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 93309218-2074-3e82-be16-227d0622bd07 | -2.26352 | -48.75388 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| dd00a3b4-5fbc-3381-a14c-b256173338ac | -2.77143 | -54.09218 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a6669582-0d2c-3642-8457-cd22b847c3e0 | 1.75811 | -55.57639 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 02f28f97-1b53-3c53-afe7-de58a305ffd5 | 1.76041 | -55.5618 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 96e1ead9-bbec-30f8-a7a7-efaff302cc7b | -3.06949 | -57.75084 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 359aac57-0fa2-3d71-89b4-e65d5911b70f | -4.09834 | -52.07151 | 2026-10-07 16:39:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 768eb60b-1db9-33e3-b30c-159a9432e5b1 | -3.03707 | -57.47879 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 77aced3e-bf68-31bf-9bbe-5c3dc14ec12e | -3.68162 | -55.94719 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d5140c1-9b71-32d4-99a4-a8b7aaf379f7 | -1.88049 | -45.42997 | 2026-10-07 16:39:00 | NPP-375 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 16c98a0f-7d1d-3979-937d-71f6793f4c1b | -2.94032 | -54.16529 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8b2b6aa6-6677-3f43-924d-977b4d702b34 | 2.25403 | -55.98063 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ad17452-0f83-3a0e-9707-d1a7dd8bd349 | -4.34048 | -56.38507 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README229.md)
