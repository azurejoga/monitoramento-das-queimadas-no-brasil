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
| 3f926963-df7d-37e2-b6a2-b50dbde95d31 | -2.6555 | -51.71544 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca67c8ae-6013-394b-9aa6-be08b74e06a7 | -3.99517 | -49.3997 | 2024-11-18 05:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e97ef887-9442-3059-aad5-d2e855d39e42 | -2.6828 | -46.22398 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5745bc86-c142-3f1f-8864-595360fe331e | -1.38319 | -52.71735 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e895382b-865c-3e85-a4e4-9f6a2c362ab3 | -1.62354 | -55.14837 | 2024-11-18 05:03:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6328becc-bf0a-3c03-89fd-e316de39857c | -3.32972 | -50.5008 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8b6521d-659e-3f5d-a4a8-7c290239ab24 | -3.18603 | -53.24249 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9cd76a5-bb35-388b-866a-b1667a6fe37a | -1.22711 | -51.78957 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99f7f75b-d130-3c54-bb38-f1f5283f6ce2 | -3.06711 | -54.39659 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b3cf301-227f-373f-a63b-5c1b2a81641d | -1.70963 | -45.82805 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18d52660-0b8c-30a0-94da-f6a9cbc29173 | -1.27698 | -54.66535 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 826de7a5-07b2-3db6-a13b-8382b9617aab | -1.95027 | -53.33517 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf76b9e8-2a8f-39f9-99de-2a28f1c0aab9 | -3.34368 | -53.28888 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e62c15f-5689-393c-9bd6-c2a5cf31d670 | -1.41251 | -52.06378 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93827633-9495-302a-b006-3bad993586b6 | -2.90955 | -46.86703 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b859cd-03c5-3723-8085-3b87373687bb | -2.6155 | -54.32637 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b5d42b5-e494-3a8d-a2ea-07346cddc2a8 | 0.79689 | -50.22645 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6acbc98d-5e45-3f9f-b525-4d566b9d173e | -1.2904 | -51.65404 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bb97300-b42f-38d7-aadd-a63de3cd742b | -1.7741 | -55.5345 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fed4a7b-99d3-3e0c-90ea-72f0f15a793d | -1.39979 | -55.62114 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35b583ca-2dcc-38f4-93c7-ca8b6e992442 | 2.23723 | -55.83163 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78155bbb-68b3-39cd-bbbe-004fbc0bbc8f | 2.23666 | -55.82795 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a5fd333-f173-3aa3-8539-179beaee771e | -3.52968 | -50.24866 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eda0e123-5aa4-3534-9aff-f09854984cd7 | -3.24455 | -54.50216 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce46727-cb31-3f2b-91e0-611041c3ddac | -1.1855 | -55.73037 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc3849a2-cdaf-3b89-9258-33fea6b8595b | -3.87743 | -52.26807 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef226014-3186-3ec3-a60e-ade16bed99a5 | -1.14277 | -51.69226 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 233f8d64-dccd-3997-bf7c-9cbffa99a79a | -0.16223 | -51.59923 | 2024-11-18 05:03:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a316412b-10bd-37cd-a827-3e849a9fa659 | -3.77233 | -50.15873 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ad37cea-4860-3670-8815-d23772e8070a | -3.20142 | -54.32061 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 522f4379-c1c9-3063-9bc9-be12f477f5b2 | -3.52915 | -50.25213 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 693cc449-95ce-3b31-91ef-9f66f893dd6a | -0.03679 | -50.74873 | 2024-11-18 05:03:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6641a87a-3165-32fd-ae11-dda3406d6893 | -3.66265 | -50.60983 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4240609-0da8-38f6-b106-f59a2d331779 | -2.19692 | -53.67102 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aa06f555-2e86-38d8-8c7f-59fe5e437975 | -0.99334 | -51.77665 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4b2d121-171b-3257-a45d-4614d9ce2230 | -1.33583 | -51.85936 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a779767-5eef-36c7-b87b-7b901acd3d0a | -3.59072 | -53.78055 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c08ec2c-43be-3f2c-b5cc-53be6e785e60 | -1.34462 | -55.47449 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc6e4ef4-ba93-39a4-9909-08058de84f74 | -2.63024 | -54.27513 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a3972e-7699-36ca-ad62-7a8c802feb31 | -3.5669 | -50.25337 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e447da51-57a2-3421-b722-5ae11740ff39 | -1.77396 | -50.74852 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab8f98a7-266a-330c-ae1d-48469abf882c | -3.15858 | -53.23829 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f36ff6f-1544-3b3a-a872-d3d36a43a5fe | -1.39314 | -55.46783 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1668be58-031f-3e37-925e-dd05768ee441 | -4.27062 | -50.67413 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03feab03-988b-3cdc-be37-7874d3921caf | -3.53628 | -50.51398 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e298290-d4b4-3ceb-a853-176e65989a16 | -2.54569 | -53.98584 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3568143f-3562-3b96-87d9-288030b4c838 | -3.56793 | -50.24643 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3583e6b0-ec88-3e55-810d-b73936fb23ed | -2.92949 | -54.66954 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7c91206-ca85-3999-a7f2-8a14be64b42a | -3.06548 | -54.40708 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 833e2a50-5fd0-3bbe-a683-9c12a22bdf40 | -3.40241 | -50.29151 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d3b23c9-228d-32d5-b2b9-bf4c1e4966ae | -2.25816 | -49.04807 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c51dd182-bfdc-361b-83de-6534039b2f38 | -1.62914 | -53.30138 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 586eaa9a-d3dc-3fbe-8d6a-718e266996cc | -2.68084 | -52.43779 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d024781-211b-3ded-a2c0-ada610f3b616 | -2.10923 | -46.42858 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 77296286-e0b1-3289-97e8-96beb5c92be2 | -2.42572 | -54.62671 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 723fe346-21d8-3f72-9cae-605439639f12 | -3.57105 | -45.20846 | 2024-11-18 05:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c99a3982-4224-3a05-91e2-6c14b3bc8438 | -2.73638 | -54.11629 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37ad102a-6cc3-3019-90f0-9aa012ea968c | -2.64428 | -59.7694 | 2024-11-18 05:03:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26dde94c-1217-32fa-a6a2-1e696325082c | -4.95298 | -44.8466 | 2024-11-18 05:03:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 81571665-d1c4-3a4c-902b-9efb2a7b1e6a | -3.06524 | -53.2741 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd7d97b-5fcf-3386-b549-0ead66c95249 | -3.05605 | -54.40205 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 38116704-4d08-3637-91dc-781b9adb2c3c | -2.55183 | -53.99043 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc35d87d-ed46-342c-85b8-1ba4f24aa47e | -2.73543 | -49.49732 | 2024-11-18 05:03:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed6aa05-fade-31e9-909e-a90820bb1039 | -0.97293 | -51.71904 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 178a3a2e-e099-3d9b-9b9f-c8ee6151a255 | -1.3289 | -51.87329 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c37683-3b84-310b-9ae8-a78970d97d64 | -2.97867 | -49.11374 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a149d7d-91aa-320e-a0e4-55960068b91b | 1.0466 | -54.64553 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0888066-05dd-3ad8-bd63-1dfa86f5d14d | -2.10876 | -46.43169 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0e494a9e-4909-3959-9be1-1054a0442854 | -2.65916 | -51.71601 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| eea74046-f0ab-3c19-966d-35622e9a042f | -3.4703 | -49.97554 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fda6128-4c82-3ac8-9a7a-4b5bb586d091 | -2.60858 | -54.26109 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b06295a3-0940-3a99-a815-acbf9a999703 | -1.5962 | -53.06475 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df55a1f3-5d37-3b2a-8db3-c9fb17e73ce6 | -3.1094 | -53.74435 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50c6c2b6-8b35-3209-af3e-8aa941788e61 | -3.48809 | -50.24966 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7955df1e-a259-34ad-8222-962bd1e12de0 | -3.5318 | -50.51669 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ea9e463-03c5-306c-ab8b-db154f5a13a1 | -3.77228 | -52.19811 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e60b613c-11d1-3060-9f58-54ae6d2843f4 | -3.62961 | -50.22288 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15874076-1169-3b74-ae34-8aca21a18ac4 | -3.54055 | -50.45805 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c33b0d8a-36d7-32ae-9a9c-f7dd5090023d | -3.57374 | -50.42785 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f7f8aa6-a5c4-38de-a721-3181f04982a7 | -3.52563 | -50.24802 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b8c7b63-0b54-36ac-a425-30bd7c205ef3 | -1.54801 | -52.0293 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3db42ac-1b75-3ef2-932f-fd14d8869a46 | -2.63904 | -53.97475 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc45946b-1b4b-36bd-a502-360970ddd433 | -2.60643 | -51.79087 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 219e038c-ea12-3acd-b3d1-71034971b9c0 | -3.69102 | -50.11757 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b647c37e-b66b-3bef-9aea-b81301b79dfa | -2.23777 | -53.60772 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f078fdae-7b7f-3845-b825-50ee61fd3bc5 | -2.7111 | -51.8656 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b128f4b-1f06-3df0-97b4-be577ea4648b | -3.52885 | -50.25858 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfe28886-55b9-3f5e-9a1e-6364dafae091 | -3.25021 | -51.51735 | 2024-11-18 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aa3fdfc-8630-3662-a32f-6d382576f813 | -3.79875 | -52.09898 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd89a5a6-1b3c-3c71-af4f-e2b2064aae94 | -2.83185 | -46.66682 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 369bd1d2-6737-3b79-a2a1-5992f0258164 | -3.34368 | -53.31169 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2702ed4b-24c3-33fb-8996-1a14ccd1aab4 | -3.5332 | -50.2527 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6042552-26cf-3596-8abf-a5c78f409227 | -1.67537 | -53.83376 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b93eee8-015b-35ec-ab04-7511a6b37384 | -3.99026 | -49.40312 | 2024-11-18 05:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70a33ce9-fbcc-3fac-9c67-f8f5bf487343 | -1.77085 | -50.7432 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b32b315-cd1e-32e6-99a2-2adead70dafd | -2.17262 | -46.39383 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 215d23bc-dd01-344f-98ca-4629696a04fb | -1.58825 | -50.44004 | 2024-11-18 05:03:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b644f44-53d2-3377-9eb4-2e4570a4701b | 1.56159 | -55.87134 | 2024-11-18 05:03:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ab28c85-5623-3c8a-9b49-c10a8984ae9f | -2.66084 | -51.68109 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4d08a6c-978f-310a-82a2-e43c6e8c8dd3 | -1.13495 | -51.68357 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
