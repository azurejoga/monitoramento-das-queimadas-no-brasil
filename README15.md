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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e67de3b-a015-35fa-97b9-3f299f269c06 | -3.9792 | -59.327499 | 2026-10-08 00:26:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f178d83-f9db-35c7-b48b-4cc5183b8333 | -4.1067 | -54.413399 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39615c25-94ad-3f93-9c0c-f3e55b290d34 | -6.1133 | -51.726501 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce54eb08-232d-3694-b474-aabd9e39eaf8 | -0.9937 | -53.733898 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b04a2e3-bf59-3ae2-9422-e0854c50a1d6 | 1.6919 | -55.623299 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4610b671-46f2-3b53-9122-8b72daefd753 | 3.1515 | -60.620499 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ddeef0f7-3f04-3ce9-8499-634a6c6141b5 | -2.9685 | -54.076599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b924dca1-7969-311e-b100-0ded3fcbaa1f | -3.1029 | -54.169701 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 146b5156-2648-3d93-a4d6-ea514d344edc | -3.2852 | -54.063801 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82deefbc-9e56-3b0b-b092-132804202f86 | -6.1843 | -53.435299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b96bdb0d-82c1-3b45-be22-19efa9893969 | -1.5208 | -54.5583 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c526d3a-0e46-3c04-bf5e-2cb75a0b0851 | -7.8446 | -49.287498 | 2026-10-08 00:26:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f692d4-d098-3f17-a707-7a595d28f15e | -4.3082 | -50.787102 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 668dd822-39d1-3ff1-b41f-43fea88eafd8 | -3.1934 | -50.555302 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d60094d-2642-30d9-9812-7c414e6c59bd | 2.4388 | -50.830101 | 2026-10-08 00:26:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 10a38c36-e208-3d1e-a296-5218eef6875e | -3.1427 | -53.7085 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f18e39bd-71de-38c1-82b1-73d4a20ae65a | -7.7516 | -54.952801 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8c61ad-1c74-3f1b-8507-8a3dd10ba53d | -3.735 | -51.205601 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b36ae498-d8b5-36ef-a41a-549ed38c5da7 | -3.189 | -50.536201 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e13ff91-9490-3d6f-b101-ebd91f74cbff | -3.2985 | -54.031898 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab7c979-2f00-3574-abaf-0ffb1a65b554 | -3.0453 | -53.8699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26bb579a-df80-35ba-804a-641035bc7e13 | -7.2151 | -55.086498 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6e1b131-8cdd-3c00-af53-702fc63a817f | -7.1785 | -55.153599 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dca70cb-8dd7-304b-8403-2e0d926503ae | -12.2036 | -48.424702 | 2026-10-08 00:26:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 140a9c9d-a9c9-3c1e-9ea4-3fb0811521c4 | -6.5058 | -55.369099 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 355f62d3-f810-319b-ae59-9a6ceae1274c | -3.4249 | -58.586601 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48fe9822-829f-3861-ab7d-0137b6ada69b | -4.2865 | -50.7826 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce8dbd7d-841d-34fe-95f5-8e086a9f6bdd | -5.1199 | -47.106098 | 2026-10-08 00:26:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8312714e-2faa-3b03-99a6-018d45dc4daa | -2.8849 | -54.117001 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 008eb272-0a7b-3eb6-9f49-600ebbb9c504 | -3.266 | -54.024601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 192d6fa2-8e5a-30e3-8a0b-c9393278d01f | -3.2004 | -53.8717 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad89d7bd-3813-3d9f-94e5-60386924546a | -6.0527 | -51.732201 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87c1e244-d33e-3f0b-9753-a16b99062c13 | -5.6894 | -53.481098 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18989969-fe7e-3e70-a56c-c575f71b8cc0 | -2.771 | -54.069698 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2de10d-8480-3a45-81cd-e7d61c04be4d | -1.3773 | -56.888401 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89abde5b-6f13-3cc9-9615-55505886525c | -3.5745 | -59.446499 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce9cbdfa-292b-33d3-b416-ef978187e5a0 | -2.7643 | -54.0858 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feaaef79-792f-32fa-8965-125d4cfdfacf | -1.4692 | -54.649101 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14790df0-0621-34c5-8a9e-f8e99b069f42 | -2.1249 | -56.685699 | 2026-10-08 00:26:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98921448-eb59-3a7e-a868-58f614e1b18d | -6.2219 | -52.784599 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d87271bd-ef61-32db-a016-feb44997a8e1 | -2.4618 | -58.003101 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7482a4a9-3614-3d8d-8c56-49ad168e403d | -3.1076 | -54.1903 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7005594-751b-363c-a70a-7d302e3d029e | -6.2299 | -52.865101 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78c94819-ffb6-32d5-aa55-2edbf562a6ed | -2.566 | -56.1735 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b6ccff-0604-3e35-a568-42928aceda2e | -3.721 | -54.2122 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99477035-4d6d-3b73-b4be-154a5a59f862 | -3.5198 | -54.644501 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a288055-0389-3fd3-85e6-c1dc810fa6b4 | 1.7017 | -55.6255 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef1fde8-3315-3842-826a-c9c82f8fd49c | -3.4224 | -50.432201 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78f6c0e-c288-3eb2-92d7-3ed12e2c6ddb | -3.2523 | -54.646801 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 692145a4-e0f4-3155-b56b-52fd609244e5 | -1.6061 | -55.1628 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a93edbca-26d9-3b53-9880-ea85ec4b7845 | -1.0526 | -53.584301 | 2026-10-08 00:26:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca85424-4856-3f6d-bdfe-54b68df06940 | -3.0037 | -54.141201 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3793b605-7b03-37cb-be7f-90e079b2da6a | -2.8927 | -54.151501 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 602ae0ff-281a-3d1e-910b-88cdeed1ff35 | -7.2068 | -55.095699 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02a65703-97c5-3138-be65-6d95352c0a20 | -7.2249 | -55.084301 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9607c8d-0ba2-3d23-b4aa-cbcf9910ef01 | -3.5265 | -54.6287 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcecb42-cd9a-307d-9b7d-03f7e309b368 | -1.4661 | -54.635399 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2e3e6a-4749-3a00-b937-8af9714d94b4 | -3.1326 | -53.754902 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6df2664-8b19-3391-9e09-dfa012eaf5cb | -5.0497 | -49.766399 | 2026-10-08 00:26:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e208ea3c-163e-3e14-affe-a46e1b496273 | -2.9798 | -54.081299 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8e219bc-44b2-3529-9074-c4a4025a18da | -7.7598 | -54.9436 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d10129ba-b616-3c66-8151-bb3199697b52 | -2.6044 | -57.583 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71122220-de0e-36e4-af98-76f77c61eda6 | -2.9288 | -54.128899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6550bcd8-704e-3df8-88ea-7d4d44c64532 | -7.2084 | -55.102699 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b12ba92f-dd2c-30af-80df-220d34a9466f | -2.48 | -56.112 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9cc7f20-ac71-3c18-bb3f-79cf15d57183 | 1.7708 | -55.547699 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ead62dbf-aeb2-3914-9118-8d98a097c44e | -6.73 | -55.1278 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5262cb16-6ad6-3c68-8db5-b42e22f38e41 | -5.0652 | -56.898102 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 867920a1-8af5-385d-92e9-a4667dbcd1e1 | -3.6729 | -54.2733 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f03511ef-590b-3b26-894b-5cb7da99eb22 | -3.2712 | -51.071098 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 576e1739-489e-339a-bd76-e420840b8935 | -6.8734 | -43.6688 | 2026-10-08 00:26:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e261f5bf-882e-3d1a-ab4e-59ffaa382e37 | 3.6551 | -60.402699 | 2026-10-08 00:26:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3d7191c7-cd90-32ab-9e39-418b3492e608 | -6.5246 | -55.268902 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2358e175-6c66-3d55-b428-39603590e31b | -6.1581 | -52.6409 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5034b8-d8f1-3220-b169-869f84a0b121 | -11.3462 | -51.870098 | 2026-10-08 00:26:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e60abc84-d452-31b4-95f6-f41047ede7a5 | -2.9111 | -54.0966 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6165d7f-839f-3d84-b2b4-5481ac3e093d | -3.0335 | -53.9091 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac3c8a9-2751-3767-969b-3f3039350ccc | -4.5443 | -54.9823 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53cea7a7-684c-36ca-ae5d-dc2770515ebe | -5.7239 | -45.148701 | 2026-10-08 00:26:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dec743aa-1b14-3b25-8de2-d0150c2e8990 | -6.6783 | -55.080601 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 585af63a-c45c-3b6f-9e83-e517ec929957 | -1.5048 | -54.8064 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a55be97a-e3e5-3613-972f-f516d77da8d4 | -5.6993 | -53.478901 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba9ac6b-ded3-31d7-ac6f-1de9b0abca58 | -4.3473 | -43.7906 | 2026-10-08 00:26:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1acce2-02eb-3a2c-a685-52eea5758768 | -19.99 | -49.079201 | 2026-10-08 00:26:00 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d39082dc-9191-3bde-b18b-02673779cf30 | -3.0229 | -54.180302 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7911a0c6-da0d-321c-8b07-605fad5b963b | -6.6799 | -55.087601 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a3b5db-9c22-35d4-a6a9-4ecd4cdc31a4 | -5.2576 | -55.912498 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f51249c2-db6e-3f9c-9e95-4c792a5a8ef5 | -2.7561 | -54.094898 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0a0d216-bc59-395a-8843-40906fb8e4fb | -3.2965 | -54.068501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8bbaf1-eabb-3883-ad2e-3d73743882fb | -3.3048 | -54.059502 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 738ddb32-3cb0-396d-aea0-55bb244a0373 | -3.2742 | -54.015499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b76cf90-4eec-32ea-9ebc-1477176b7925 | -6.0429 | -51.734501 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25073d04-9589-3733-8d4f-23a16b7a97f9 | -1.7212 | -55.444199 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8cc523-2aca-3abe-8a68-9e4b98537ad2 | -3.5734 | -54.653999 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56adcf6f-53de-3acc-b9fd-ae64acdc1456 | -3.8523 | -58.892399 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 805b70a9-2886-3b9b-8fc4-d6c80daad1a2 | -3.2613 | -54.003799 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0d6c5b-04a7-34f8-9ab5-e690fab10aab | -5.1676 | -45.348099 | 2026-10-08 00:26:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2ba713a-fe8d-344c-9c47-efe61f7cf069 | -4.3055 | -54.791599 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b289e0c-6350-32be-b771-7c41ad28bf07 | -3.5244 | -54.664902 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4179037-daaa-38d4-84cc-e1547bf4ce72 | -10.469 | -47.237701 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
