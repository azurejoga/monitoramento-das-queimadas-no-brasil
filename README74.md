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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15d010a9-2fc7-388b-8f03-fc5592c68d47 | -3.28816 | -53.85636 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| b758f447-1471-3fad-84ba-0e998f1256db | -2.54896 | -57.40587 | 2026-10-01 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d848d23f-f7d3-3e7f-8aea-aa6a902fa6a8 | -3.8308 | -55.90288 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a69f99a5-9ee6-3529-ae71-386b20a75e10 | -2.88525 | -54.87896 | 2026-10-01 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4079fe01-46fd-3928-be90-a86ba398a658 | -3.25216 | -48.77349 | 2026-10-01 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a3a90bb-391e-3d83-a3e1-ad91547e9a26 | -2.98074 | -51.03024 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca07d840-59c0-3316-a3b2-712ca5743d5a | -3.23023 | -54.31454 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adb37ae8-8ca6-3b75-afa1-3c393ac4c428 | -4.25461 | -50.76192 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91203ceb-490c-3e90-86e9-c03ffab9c9ba | -3.98474 | -56.08435 | 2026-10-01 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6e675d7-4fc5-3cf9-8b37-788b9bd72e33 | -1.63736 | -55.13028 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eca64d59-303b-3a71-b1bc-5c24120590ef | -2.90767 | -51.32499 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 706385b5-e67c-388e-be28-ed2dd7b9f87d | -1.64991 | -55.21479 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2e0d3c4-3deb-3a26-9d60-3c43611f8606 | -3.01252 | -53.87552 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef64fb4d-3841-3196-a3b6-dd400f676e5f | -3.145 | -53.74055 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e640709f-31a8-3bd3-8de7-fc6ab89e5547 | -1.64155 | -55.12677 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a25f8d8-3fd5-308d-bafc-d0df50657b68 | -3.84882 | -55.8083 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38250aab-a881-34cc-bbdf-92d9316deb93 | -3.03846 | -51.45374 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a7c9fc7d-b403-34ac-8a12-af27d1e7579e | -1.46103 | -48.91869 | 2026-10-01 05:16:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e897e7a-9a41-3ce3-99f8-cde57f853462 | -4.12189 | -53.80966 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f3da4a8-650b-3ff2-b002-3b3593400830 | -1.44776 | -54.45771 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 517981b0-9d0e-3963-af1b-4bc848dd8067 | -3.24924 | -50.8076 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fb3bdaa-7ccd-3ef4-bf01-e11dba637f39 | -3.86526 | -55.81902 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c36af45-15d3-35f5-9437-7ccc709392e8 | -3.10648 | -57.91112 | 2026-10-01 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9793baa-e468-3ce8-89d9-e6c3d6fa2c3d | -3.70418 | -59.68154 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9909aef6-7cc6-3cb8-8dba-605104bb2aff | -3.00688 | -54.22807 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33bee7ef-131d-3b08-96d3-785ebf2a6113 | -3.352 | -58.15033 | 2026-10-01 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dd28dc7-a8ca-343d-8821-bc0402fd9274 | -2.95054 | -54.09195 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c417d6b9-d9e7-3b79-9177-78052bd99fc8 | -4.06431 | -51.09746 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c39a32f1-20e5-3a36-8553-095d2e59834e | -3.33089 | -59.3932 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52b9729b-c320-30f8-a35f-ca762ca3f75d | -4.69163 | -55.91119 | 2026-10-01 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 444ef64e-25de-38c9-9c82-734523377632 | -4.28641 | -50.75008 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7202f560-5dce-3966-ad2a-815ad2fbdf50 | -3.80379 | -50.60933 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 634e875b-21b7-3b26-ba9e-5a43568c591a | -1.08331 | -54.10239 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6074f70-92d3-3480-a233-6dd2bf2692ea | -4.27737 | -50.74317 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5738b233-8466-3959-8f5b-c39b392c40a7 | -3.95652 | -48.12883 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d60ff6c5-2506-31b8-a2b9-b83f6730ace3 | -1.32644 | -49.12909 | 2026-10-01 05:16:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f18e06ab-7630-3602-b6e7-bb0e9f6d47fc | -3.18478 | -60.06111 | 2026-10-01 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd30ebd5-afea-3bd3-a325-980229a16f46 | -2.98393 | -51.04102 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eeced102-1e26-3f4e-85be-5b02d17ce332 | -4.6347 | -50.60969 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6bc8fef2-cb71-31e3-8524-6e70689fe7f7 | -1.10737 | -54.1929 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db5ef408-3d79-3c44-bed8-a5c169c45a30 | -4.25616 | -50.7511 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 554babf4-cf3b-3bfd-8769-36623cf42c82 | -1.75772 | -55.6375 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7d61daa-0ead-3ddd-8da6-8ef1f48dddc2 | -3.27093 | -54.27798 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c7d27e6-9102-3625-b065-fe8730f50e16 | -4.04492 | -54.22353 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d041f647-d7a3-31be-9197-1e83f3b7c16b | -3.21352 | -53.94855 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69772a46-0123-32f9-9bf0-5e2986d13411 | -2.88158 | -54.87841 | 2026-10-01 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 809361c3-29ce-3028-90e3-1367165934c1 | -3.83019 | -55.90683 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| befbc219-7700-34eb-9967-c0f62c7877ae | -3.03904 | -57.51415 | 2026-10-01 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ab2620-ff7a-341a-93ef-6466d8bc40e0 | -4.04521 | -51.09324 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8677603-820e-3838-a364-2a93d11b4506 | -2.5535 | -54.62663 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b47f000d-96d3-3898-a623-afb5d8286584 | -2.98227 | -51.02013 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d1fb1f2-0f53-343d-9e80-85882ddf9a80 | -4.15926 | -48.89871 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8a825f-a591-3ff2-9916-7504aef8e3aa | -4.29953 | -50.76321 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cb6c7414-674b-3c72-b236-84411f29934b | -4.25949 | -50.76282 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c9184e42-492e-3c91-b4ba-3e9d2c84636c | -4.04302 | -54.22551 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3738a7d5-1967-3c8b-be24-4149700a7e9e | -3.28891 | -53.85139 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 3968b134-c591-395f-82fa-523ffb6375c5 | -2.97374 | -51.04457 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66ea72b5-00ed-33d9-b612-ff82bc23cc9b | -2.96821 | -60.07552 | 2026-10-01 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdef6944-1162-33f0-9d4b-6aa4aad5c07a | -2.05681 | -56.87368 | 2026-10-01 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4923e00-6544-3250-bf12-e271d0d09a1e | -4.28569 | -50.78933 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b80f08f-970f-3a7d-a634-bfab56031aba | -4.25205 | -50.7448 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2323b879-f994-3879-8a9d-b42467db10af | -3.69001 | -47.12348 | 2026-10-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6816d91-e464-3cef-a876-18e4aace9f0b | -2.97997 | -51.03528 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a25d4796-db02-3982-b313-346ed925a8e4 | -3.15394 | -54.07841 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 418e3f71-0e96-305a-9921-b276871fe20a | -4.24938 | -55.04194 | 2026-10-01 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b693f992-d103-31b5-856d-9c0181426bee | -3.27354 | -54.00505 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 349b35af-f8d0-3126-8d1f-4e9fff6a93b6 | -1.89448 | -52.63858 | 2026-10-01 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e2c47da-5a4e-3eab-b931-d2d805073eea | -4.03892 | -54.23742 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7b535950-03e8-37d2-8fb2-7499acd3cc82 | -3.81931 | -52.39636 | 2026-10-01 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3b08ae6-8f49-33ad-a333-856423a78647 | -2.99412 | -51.03746 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 96aa4e37-daba-3916-85bd-9b55967c8230 | -1.20675 | -49.2852 | 2026-10-01 05:16:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76556e00-7b67-3bf5-9da3-d27477718ad9 | -2.89731 | -54.13233 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54cb8638-9e4a-3344-8713-fb391c38912c | -0.39306 | -51.84641 | 2026-10-01 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3cd57f1f-fa2c-3edd-a2c4-c7df29d5c83f | -3.14744 | -53.75121 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094d184a-3341-3b71-afbb-899555b2ff5e | -4.88915 | -48.37645 | 2026-10-01 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c76670d3-506b-301b-b67c-351975e073cf | -3.49266 | -59.53291 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff467177-3f22-3ac3-80d7-0d49a057cafd | -3.59319 | -54.55364 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96e08995-edd9-367d-bf20-54b0f454d72a | -3.95652 | -48.13007 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 200bb23b-a266-3d85-967e-5deed966c6f0 | -2.98388 | -54.14732 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7ca0761-3e76-3487-a658-ebe91a03892c | -4.46049 | -47.92308 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5a8662e-0e96-3207-954f-6199fa04b244 | -4.27817 | -50.73766 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6e3a0370-8309-3a33-a3c4-4a20e0c97b2c | -3.80456 | -59.30338 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a7b70fe-8c37-3853-953c-5024dd79dc6d | -4.26187 | -50.74625 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8628542d-2630-3877-ac83-bcfc2d100326 | -3.11025 | -50.27456 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3283a144-2a3d-365c-8871-070364f0f3aa | -4.26664 | -59.88928 | 2026-10-01 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc5cf53-712b-3255-85a1-c34b70cf8bea | -4.37928 | -49.73768 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e6a0216-8ab8-3654-aa07-d2e98b789eed | -3.58418 | -53.99787 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87e5a396-fc86-3fa4-8757-352f1bcde06c | -3.01642 | -53.87613 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eab0bd73-f674-3ed9-bc25-a140592e90dc | -3.18613 | -51.24438 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1fe030b-8b02-3a8d-92e4-b82c010c78a5 | -3.19037 | -57.8327 | 2026-10-01 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ba36961-2ed5-3618-b226-9115e720d186 | 1.87766 | -55.64347 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6b227d3-7079-3cd7-b33e-1adc583cbf66 | -3.0916 | -50.26301 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8757db5a-6d19-3e5a-8abb-e928a1bb5369 | -3.71679 | -58.79856 | 2026-10-01 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eef8cad2-6534-300b-9d5c-a4f60fd0884e | -3.01546 | -54.17161 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35d72ce3-0f8c-36c8-a665-0dcef49bfe5d | -4.26845 | -50.77014 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 626aa511-9984-3006-ab2a-6aea79e79098 | -1.91785 | -55.05339 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d557580-46ed-36c5-9e12-0ec67daeae71 | 1.84363 | -55.55958 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf5145cb-cc2f-301f-8f05-22265487a9db | -4.28656 | -48.56066 | 2026-10-01 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5692bef3-d02e-3bb3-9a0b-3cba58682476 | -3.57047 | -51.47691 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 154b469a-6a85-3ca2-84c5-cb48c71a0aae | 1.79229 | -55.63831 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README75.md)
