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
| 81b0b5dd-fd28-3d39-9d61-bde839e01ada | -6.27225 | -44.54148 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d836c001-f2bc-3d8e-b588-ee0b8569313f | -4.13769 | -46.91814 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a8d94f5-214d-3d80-89a2-14ee42e25cbf | -4.3865 | -47.24323 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db5562b4-8b61-3e88-a9c7-24bc8119b8fb | -2.87889 | -51.30276 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72263740-7435-3716-9246-feef794b57d7 | -5.26074 | -45.45889 | 2024-11-09 04:33:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78b87650-86c5-375f-83ce-478166ec0814 | -4.24057 | -48.54455 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ab7da4e-6c19-36f7-939b-b460787b12f1 | -3.16904 | -48.37325 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afa5a25e-238e-3719-8be2-57fb8ebfea4c | -5.26317 | -37.93834 | 2024-11-09 04:33:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20d64851-120a-3bf0-ba79-a0d77d0b3074 | -3.19949 | -46.52032 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fbda618-9d9f-3346-9ade-3f859156cc09 | -8.85253 | -47.67409 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2350d7c6-8df0-30de-9f89-15dfdd57475c | -3.04702 | -50.36097 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7130ed9d-1cd3-3009-8b80-67394cfdedd6 | -4.18706 | -49.78281 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 745a7b5c-1f3d-3fb9-9328-7461546b3b8f | -3.60213 | -50.24313 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbe41208-8ab2-31ac-9eb1-16f9b130e260 | -3.17366 | -53.85241 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e9aa9706-b4d3-3b79-9717-8b6dc01402a0 | -3.27942 | -53.6794 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1bb99ea0-6e7f-3fe0-a30b-25fe8e230586 | -4.0545 | -48.25716 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7606a175-6422-3943-893e-4bfae1566c5e | -4.44423 | -43.64581 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 787a4d74-7a85-30b6-ab52-cdc9ca7f854b | -2.72298 | -49.29515 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a636810-04bf-3e45-92e1-e57f28e679bd | -5.19646 | -44.9195 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93fc9d63-744a-36c8-80f3-e3ddc35af1ee | -3.81678 | -49.85556 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4a1de267-44d9-3050-b3cd-4b40eb7890cc | -2.99142 | -51.0385 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 413ef70a-c2d3-3f5e-ba0a-92f44e632786 | -3.23479 | -51.18826 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20015f67-267e-37ea-8706-1f71352bcd6b | -4.74019 | -44.10125 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5401976-ef4a-39ba-bea9-13e6bed5a7f4 | -2.83986 | -52.90409 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 782e68c1-301e-3964-82bb-292b98ae83e6 | -4.09886 | -48.32178 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 35c71722-7cfa-3f04-a62b-8fce3e659077 | -6.30845 | -44.79716 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acb9030f-96b1-3b3a-ac50-485e7e395df2 | -4.87284 | -46.09765 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f866b081-2b4c-3aa9-8200-6d5945ff2a8e | -1.83254 | -55.19499 | 2024-11-09 04:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4c60075-b860-317e-8c5d-55fa55353979 | -6.2759 | -44.54202 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f7b574fd-bfe5-3d50-8fbf-36afaac88a3b | -3.24193 | -46.48775 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16959eda-93f3-35bc-adf1-e904a68cb940 | -5.11943 | -50.03555 | 2024-11-09 04:33:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5c2d829-b679-3765-b197-6565d59071c8 | -4.24141 | -48.02057 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cad7fbea-790a-38cd-b638-25294bbe2c41 | -3.11378 | -50.14556 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4378038-53b0-3307-8c0d-d49f184f1e05 | -3.08596 | -50.56767 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f306e358-4a03-3032-be69-ef750f53f92e | -4.11135 | -48.50289 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1cbf20f5-0108-3578-948c-1b8c512d23ab | -3.76751 | -51.76272 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f58ad44b-ada8-3614-b25b-465058172271 | -4.09636 | -48.51135 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b477442-9ddf-3252-abe3-e123056cba5f | -2.85743 | -49.86266 | 2024-11-09 04:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30056094-9f00-3557-bc83-bc58abf05787 | -3.71541 | -49.98721 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d0ae89-c313-3caa-9a8a-1b0ab2f4df89 | -3.2591 | -51.13182 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 50f46a7e-89c1-3146-a0a1-a50de75686d6 | -11.09471 | -43.33919 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| d35d00eb-9c61-316d-a1d7-58e755d914af | -3.74534 | -51.94924 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d8cdd93-1153-3980-9c91-d714b0cf81eb | -6.45036 | -42.75448 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 84c67592-593b-3ff5-b729-783a9d699894 | -4.3845 | -48.58191 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 048541c8-7f2a-3af4-87f2-9415a5b92956 | -5.13949 | -60.36763 | 2024-11-09 04:33:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 930d61e1-117f-31b0-8050-f12420382b92 | -3.35894 | -53.3893 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 940467a8-20e5-3da7-b86f-38ca1d1f8926 | -3.11459 | -50.13718 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf3b6c77-5043-31e2-a563-244cc4fa93d1 | -3.60668 | -51.24489 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ec0f44b-8f60-3db2-962e-801d4d93dd64 | -2.64178 | -49.895 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08393f75-5c28-3e0c-b653-d32f35adb86a | -4.10857 | -48.49884 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c687cfc6-37cf-31e2-8d53-b59696d84c88 | -5.66467 | -46.38361 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7308e7f-6320-3cf8-ad37-2c5ac192e906 | -3.23472 | -50.27109 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 403a67fb-0fc4-3729-b93e-ed93f901fb23 | -3.62042 | -50.19651 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac77f77b-af3b-33ab-b495-336d92357255 | -4.08822 | -48.23807 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de8f51f6-e7e1-3efc-9dd4-1e4c230c2307 | -6.68883 | -48.89973 | 2024-11-09 04:33:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20f3879d-c756-3228-834c-041dc48462a0 | -4.60945 | -45.98032 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb537fd5-badf-3987-b316-c9692f1a430d | -2.88525 | -51.74375 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fb82aee-23c5-3fcb-88b5-02d8e0f71214 | -4.56341 | -50.26497 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9646f93-c406-320e-ab67-df5b88890e64 | -3.94819 | -46.40732 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a74a9165-0f2b-30c0-8e13-74086f84e6d4 | -2.60674 | -51.30317 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ead09c8e-5903-3317-9f50-17906f696687 | -6.99582 | -46.32108 | 2024-11-09 04:33:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f6cc5b3-e199-38af-bb00-51e0bbc369af | -3.52119 | -51.3637 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eca5e93e-df03-38b7-9954-f94b2e5fdc1a | -3.8371 | -50.04239 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 261d0be7-7101-34a1-8989-9c316ecdaa8a | -8.84651 | -47.69118 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f88727cd-bb70-3b77-adde-83df9a80cb28 | -5.25197 | -48.08442 | 2024-11-09 04:33:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f6b6f7b-1328-3ef6-816d-9710f9aa92b5 | -4.08526 | -48.85803 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e382fc-5e14-3901-a992-783fe8a7de7a | -3.18056 | -46.62029 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e8d6a0-9640-3b3b-9dd0-c9fe99fd6afc | -4.60562 | -49.58125 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27ba868d-7b8d-34da-9190-964387356549 | -4.11748 | -48.50742 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 046ae57b-d8c5-38fe-bd5f-aea341f35dc7 | -4.60126 | -46.62662 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc95719c-0ff2-374e-b9fe-01bf2d373419 | -3.59202 | -47.344 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| cd7bed46-8f19-32a0-a7fe-914dbdc2cd3c | -2.63598 | -49.88596 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07b9b03e-3560-337a-ad7a-00fbf8823cb2 | -3.29166 | -53.11452 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d817055b-9109-384c-9465-1c144490432e | -4.43937 | -43.64664 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72aa1731-dd8d-32a5-aca5-a6e863a3b51d | -3.38675 | -52.35629 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 58ccca1d-7131-37c2-9fb4-8520f7339e6f | -4.61228 | -45.98443 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5ada1e6-1df2-3827-ae9f-ab884674ff98 | -3.50409 | -48.23179 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 526742eb-c966-3b7b-b993-d9b7b075e23c | -4.38009 | -48.15542 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0def5f7-a408-31ef-bdbb-1bcc41f417a2 | -5.63374 | -44.82895 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c7ec49c-5e09-3f90-bad7-be32c685a8d6 | -10.51503 | -42.39417 | 2024-11-09 04:33:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe68e1cb-72a5-36d5-8644-aa052e74b547 | -11.08898 | -43.34298 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 122407d4-419b-3e41-ada5-a30c5f5fa625 | -5.5799 | -41.68947 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f02cdd7-8fd9-361d-b46a-ce94ec5bcf17 | -5.67498 | -42.99118 | 2024-11-09 04:33:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 625dabc2-99a2-37be-956f-3a6be816d184 | -4.03686 | -48.28295 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70d801b3-c853-3fda-bcf0-66364a79099a | -3.1445 | -52.97932 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7d5e7ac4-fe85-3752-aa27-79f1ffc55376 | -5.33372 | -44.03819 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc3431ed-b16a-3bd6-a8c2-98628c5a5c76 | -4.23723 | -48.54404 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d136c06-b3c7-3373-87ea-94ec1e2c1842 | -4.50773 | -46.32775 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b301f3f-5a03-3a67-b58f-1d21935e8476 | -3.2523 | -46.44307 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab2c892d-1da5-3f9e-80a8-5790c4a7437e | -5.08045 | -47.9404 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 585973ac-1c40-3ed0-9fba-e7f175ecacd6 | -3.40287 | -51.5966 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94340f7e-fa29-3717-9cc4-28713c09fb78 | -3.02833 | -53.2724 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d34941e6-89dc-3950-b803-609cda5480b7 | -2.85167 | -51.7756 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6b4551a-db18-340a-b270-862a02c4d269 | -3.58109 | -51.20519 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d3240cff-10b4-3a9e-acf4-9feaea36142a | -4.0744 | -54.97089 | 2024-11-09 04:33:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0387b81-9e68-308c-b4f8-b1e78a51f0ed | -5.11416 | -37.56557 | 2024-11-09 04:33:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d315650-15b9-3f87-b290-d1956ae42ede | -3.97752 | -49.88813 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6479a30d-482c-3a58-b251-77b9241fb24f | -2.87774 | -50.41664 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6850f564-3a37-3670-957b-ac14aaf4da09 | -2.73285 | -51.73946 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9d319f5-20cf-35da-9dc7-592d9f205a33 | -3.25066 | -45.92399 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
