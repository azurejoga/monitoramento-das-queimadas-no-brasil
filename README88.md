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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1733a5b-0db9-3b9f-9b24-c87c0f181f9a | -2.21921 | -51.6719 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c9e078-d0fa-3aaf-a4bc-f156657bbf62 | -3.6845 | -52.09371 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40364a63-bb6f-374f-a3b3-5f1e1b9e514a | -3.68257 | -51.09176 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea4b9d9e-d4f0-398e-a3b2-2f4dfec1bb3d | -3.68248 | -51.08977 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dafbef7e-3f28-32b1-a6de-ea3b490fc554 | -3.6816 | -51.8425 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad82b231-e445-3592-a4b0-b8dc0b434575 | -3.67605 | -51.93071 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 309f1203-cbc9-38a0-bc81-0d311439ebef | -4.67377 | -50.97253 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 949d1f61-d6c7-3c19-9581-753800d6ad98 | -4.67308 | -50.97033 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7974e9aa-e4c8-3930-b89b-f766931930bb | -4.67234 | -50.97517 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78d08150-bffa-3223-8872-174670943666 | -4.66989 | -50.97194 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afb7f782-96dc-36b4-bff1-8a546579d5a1 | -4.6692 | -50.96975 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fcdca6f-b995-3826-99da-6e098931643f | -4.66918 | -50.9768 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f6c9dfb7-a962-3d57-9aca-69952c67faee | -4.66846 | -50.97459 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50ccdc7e-4028-314b-81d4-9defdc115112 | -4.66772 | -50.97943 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59504946-cc0d-337b-b9ad-600dbcd1b323 | -4.66606 | -50.96435 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5bd482a-5403-3c38-827b-6e85e778dc07 | -4.66532 | -50.96917 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 581735a9-b7fb-37be-abc9-a90e282beb7e | -4.66458 | -50.97401 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2681a2a2-2b2c-3a85-aa68-cdb18c5ad498 | -4.65848 | -50.98793 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3e91662-1010-3abe-8f29-51191dc6e97b | -4.64627 | -50.91161 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4649e317-c868-3e5d-8366-67aaa5e816b6 | -4.64165 | -50.91585 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89daa730-ef41-3d14-9db7-5e26bd962ae2 | -4.5722 | -50.95527 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa62175f-294d-3720-8ef5-e5c93a4990da | -4.57056 | -50.95753 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94dfd651-5639-3a2f-b082-79a7bb23ec0d | -4.5405 | -50.97264 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d6ebc84f-a841-3fb6-a289-03d0907ba33e | -4.53974 | -50.97757 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b00626c6-0494-398f-8d67-3afeb6727aad | -4.53663 | -50.972 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08ca19af-8d42-3edf-b6f4-2e1959b0731b | -4.53588 | -50.97691 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d5ae45d-1ba4-3aa4-988c-5899a543f619 | -4.17914 | -51.23606 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c2ce715-8973-3f93-9eec-dd45c921bdc8 | -4.17535 | -51.23549 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a991b7d4-c38b-3a2e-bd60-af369c23a300 | -4.08017 | -51.12331 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b74ce8bd-6b04-37f4-adac-8c8755e25633 | -4.07946 | -51.12796 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6f073b9-d54e-3ffd-9958-c3f8cd608616 | -4.07634 | -51.12283 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10fb0880-64f3-3a59-af5d-a90f216e30d6 | -4.07563 | -51.12749 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 572c9a43-4319-3046-af17-4a04fdfe9396 | -3.95222 | -52.25664 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5616922e-b64e-35a7-a9fd-9f378ec0acf2 | -3.94925 | -52.25207 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a2f1bbc-8f59-3710-a9f8-cf66c511f1e7 | -3.94864 | -52.25613 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f12f367-1405-348e-8b39-0f89db66f140 | -3.94803 | -52.26017 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13fea33e-4dfb-35fc-8f4e-d3856d223904 | -3.94506 | -52.2556 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 169bfbe4-9afb-3ed3-8678-b1e867c20c22 | -3.94445 | -52.25964 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45f56b92-8ba9-321a-a821-31fbe5e1854b | -3.93083 | -51.00745 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6399fc65-d63c-364c-8888-a13e253ba18a | -3.8986 | -51.81827 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b381f33-4e3c-3c4e-b4e8-f0f36a25b043 | -3.89468 | -52.1862 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51088c8c-cc9d-3f18-aea2-f39a10aaab65 | -3.88554 | -52.12573 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a557659c-5a04-3e19-91f0-c0ea9968f5bb | -3.87677 | -52.08644 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a78f8a30-fd84-3463-ad4a-f0fb3e1d0db0 | -3.87615 | -52.09057 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9d8c449-7fc2-3158-a041-57ea6b1d6d54 | -3.87458 | -52.14945 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 485d099b-1ee3-3ae0-8de1-b0ef32417ed4 | -3.8663 | -52.1313 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9d487ad-a451-3e51-b252-64497ae89772 | -3.86568 | -52.13543 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b038f892-793f-3ee1-a633-41c171ff87bc | -3.83043 | -51.36298 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1267e03a-0329-33c1-94d8-e52c30575e04 | -3.82736 | -51.35796 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b96f59f9-9ed7-32bc-85f1-1b25a71936a7 | -3.82667 | -51.36244 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca1774b9-f4e0-3f7c-8cfd-f010cb0e749f | -3.82529 | -52.14737 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e67afa75-a50b-3198-8470-0243e30c8ad6 | -3.82337 | -51.89546 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75d01be4-ade8-3f8a-99f5-a89e232a20a1 | -3.77065 | -52.16846 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2421e3cd-8bd6-31e8-9595-f6372c16d0c9 | -6.39015 | -52.65052 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ae73986-a89f-3e05-a460-bb23a0d797fc | -6.38655 | -52.64998 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e9b24ba-b677-32c9-8191-5775a2e732f3 | -6.14635 | -52.64783 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de25e2a-912f-3e39-aec0-9794ebe3fa7d | -6.14276 | -52.64729 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7bed288-1450-358b-939a-a72fc4dbbc35 | -6.14213 | -52.65141 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81bf61ae-58c6-31e7-b579-3379cef6a18a | -5.89129 | -51.2974 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c57e691d-8d01-37a6-8e46-dcfce182bb6c | -5.88743 | -51.29684 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7792d295-af46-3211-bd15-4b38c96f8b3d | -6.45632 | -52.83635 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58aeed41-3ee4-3b3c-8df0-692860502caf | -6.4537 | -52.83684 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9911a680-d302-34b1-907d-eabd74a575b0 | -0.55276 | -51.84944 | 2024-10-25 05:01:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa6d5be7-9348-35ae-8791-c1ed222e4444 | -0.53034 | -51.87806 | 2024-10-25 05:01:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03132a41-d97f-3ae7-ba37-0633a32fdedc | -0.52974 | -51.88197 | 2024-10-25 05:01:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e09818a8-5558-3e3f-835f-3b080e39a582 | -1.76619 | -52.23486 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08a9f7ef-17b1-35aa-a41a-4eb48ef1bffc | -1.74519 | -52.32263 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d89d039-f847-387f-a5ae-08d348c4a804 | -1.74458 | -52.32648 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b2d8bc1-fdcb-36be-8e75-cf07fdedcd0f | -1.7411 | -52.32594 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf13819c-5cc1-3d64-bdea-27abdaf17e89 | -1.73943 | -52.31386 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc83f6a7-7c84-3234-b174-94e40292e552 | -1.73939 | -52.03841 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdd94b5f-8d1a-32a8-8dc2-65c2eff27702 | -1.73878 | -52.04236 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53260c00-8125-3c92-bf03-aa3c109c8807 | -1.69754 | -52.71405 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 796dda1a-40a9-3a8c-bc1f-b906315faf51 | -1.69744 | -52.71395 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ece8690b-15a9-3bd2-a9d4-b57f0faf7553 | -1.64846 | -52.04156 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4e4f04e-b61c-3e11-8960-29bc89243d41 | -1.64555 | -52.03708 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef9873d1-37eb-34e5-b857-a4cf44560d73 | -1.64493 | -52.04102 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2086484-2463-32ae-a74e-1775aa15677c | -1.60324 | -53.31075 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ed0ab282-2a57-393b-9991-479528d5436e | -1.60044 | -53.30669 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ba98fc0d-45a7-3623-b5b5-4be8ede2507f | -1.59988 | -53.31024 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ba21bff0-ced5-318c-8561-d6ca8f5b33d6 | -1.59932 | -53.3138 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 676b2d7e-7b67-3c6a-97ec-8351930c4157 | -1.59707 | -53.30616 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7f4d66e-b589-3003-982b-587d57520e3c | -1.59651 | -53.30972 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6295d48-2479-3269-9739-24a94fbd5b3f | -1.59371 | -53.30564 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81df1153-d7c5-3cf3-89bc-d89c53009910 | -1.59315 | -53.30921 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e9822f0-8501-38ea-87da-58212d576a7d | -1.59259 | -53.31277 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45e50541-41b6-3db0-927d-4695fad6191c | -1.59035 | -53.30513 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e802e62-de76-367a-a640-7888616ecf23 | -1.58979 | -53.30869 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93d37d6b-0214-3b5c-8044-fe659d317d36 | -1.58923 | -53.31225 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa68db4e-484e-3531-b131-7158d95ae5b0 | -1.58867 | -53.31581 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a68e7070-f716-3169-8980-a1646d90f2d7 | -1.58698 | -53.30462 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5adf606a-d78b-3032-9990-bc66d4c63287 | -1.58642 | -53.30817 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3275db4d-a7d8-3707-80ec-5be527269c43 | -1.58586 | -53.31173 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25732744-bfbf-30d0-9901-a5d271edfeb3 | -1.5853 | -53.31529 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88edc7f2-fa2d-306a-8725-546d996513b6 | -1.58306 | -53.30766 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cffa981-91b6-3a33-badd-82dea5d9637d | -1.5825 | -53.31122 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 313d9244-a093-3d73-999a-5f58558ea2de | -1.58194 | -53.31477 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b2dd042-ecc3-3408-82d6-644f93f0f1fd | -1.57914 | -53.3107 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45d51046-cddb-3f38-b0f7-a2196c97b151 | -1.57858 | -53.31425 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95bd7cb1-3fe5-35fd-94fe-a85f6ab038f7 | -1.57802 | -53.31781 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README89.md)
