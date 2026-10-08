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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76120602-9f97-367a-afd8-19e8cdbdcf43 | -5.1213 | -47.121601 | 2026-10-08 00:48:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9239b4-df73-3564-bb13-b3c2d7f27e32 | -3.0424 | -54.275101 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1018baf-b145-3b8f-a6b7-20f268103b79 | -3.7329 | -51.2094 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dcce189-07b2-3dc8-bd75-2a64afeb1c4a | -3.0422 | -53.957001 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c02ee863-3928-3f92-bb38-6a202399ca9e | -2.152 | -59.2257 | 2026-10-08 00:48:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8f400e8-967a-30a3-80aa-03fa563eabb9 | -5.83 | -53.5387 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe2eecb-fd9a-3512-9ea4-761d824d9ec2 | -18.027599 | -46.2061 | 2026-10-08 00:48:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5442bbfd-8118-3776-97a2-5fc24086e3d2 | -3.173 | -48.6161 | 2026-10-08 00:48:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71c21369-8a66-3331-a478-e832ac59b1fd | -2.9581 | -54.221401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7adc394e-0743-390f-a82f-7fa9827ecc45 | -7.6074 | -46.7715 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d07bc336-d966-3dd0-b294-eb03247ded02 | -7.2539 | -48.067001 | 2026-10-08 00:48:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 901c890a-674c-3899-bc4f-cbb1bbf99c14 | -2.7812 | -54.077801 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9073913-0f41-37f5-9ad7-508ef5449880 | -3.5407 | -51.539799 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee9c6be-bc8c-322b-81e1-b5a037ae4c3b | -11.393 | -46.7033 | 2026-10-08 00:48:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 656a8cea-6b1e-363d-a5d9-e8211d53b51a | -2.4779 | -56.092602 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 509555c2-4119-3e5e-849d-cdea3ec752ee | -2.9964 | -51.057301 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85a39130-7833-3b40-baa6-c95469111aa5 | -1.5124 | -54.5662 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 816149ce-2ed9-3730-ab66-bb1dab662fd7 | -3.5911 | -54.242802 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de70b16d-e55a-3801-a7bb-5bbc77ea2b6a | -16.8944 | -40.885101 | 2026-10-08 00:48:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbbee090-1b0c-3f59-bfcc-475249692ede | -3.6787 | -53.722099 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcb45827-a177-30a0-afd9-9fc6dc0aa2ea | -6.1665 | -52.657299 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0e90926-42b0-3758-9d34-6bb2dab51bdc | -6.7257 | -55.067299 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 927ea475-64ac-31c7-bcb2-ac40cca55a4a | -3.5086 | -54.650799 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64122509-52b2-3eab-9703-3af34787a1e2 | -3.673 | -54.513599 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c65f568-762a-3523-bf7f-b10dac4d6eee | -11.6142 | -43.6763 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc0bd45e-8014-3ccc-be34-ad5e684e686a | -1.5235 | -54.84 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da202279-5376-3ef4-bc8c-34a2cacd9a39 | -3.571 | -54.653999 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7613e62a-2578-3805-9b61-d59713558d59 | -6.2171 | -52.7901 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f867a714-adb9-3683-8f4b-2bd9bf45295f | -3.0533 | -53.915401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 186d01e8-fbf3-3bfe-b4e6-1d469a1a6123 | -3.0602 | -54.263 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 566e0a71-ef36-364f-9f32-4131ab52196e | -3.0256 | -53.929401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72c25b7e-1aa1-3e4d-ba89-cc41d2741d29 | 2.118 | -50.833199 | 2026-10-08 00:48:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 83751d76-dbc7-3ac8-925a-32b8de56444f | -5.6889 | -53.506001 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 951d26d0-f949-320d-b48d-79be4f71c35f | -4.294 | -50.779598 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff60ee6a-d483-36de-8b07-be3623c39cbc | -2.9876 | -54.079399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4b69def-02aa-3d6c-8d20-97f403ddae95 | -6.2158 | -53.286598 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee5a802-15d5-35e8-85ab-161e51455911 | -3.0655 | -54.286098 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 030f220e-aab6-350c-ae64-0749cddc0e73 | -2.8774 | -54.183399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f379a6a-12b4-3f24-ad8c-323db8c7da8d | -2.8659 | -49.556801 | 2026-10-08 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbb2c51b-a042-31f9-9f69-91c045a85692 | -4.2938 | -49.087601 | 2026-10-08 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a529a3a5-10d9-354b-9b1d-79e5ee5f36f7 | -4.1469 | -54.925999 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13736978-8967-3537-b076-1938161a2278 | -6.1953 | -53.1497 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70574ab1-f805-30c0-913a-1bf4388f276c | -7.749 | -54.963501 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c19fb8-10d5-30c4-9724-5e8c68610ca8 | -1.4567 | -54.7729 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6bd966c-de5d-3a1e-90b2-5d83064c13ac | -4.5204 | -54.987 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7afbd4-d969-3611-b8d3-097b468902d5 | -6.2155 | -52.782799 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3599e93-dd94-3ca1-a117-9d6e2fd8071e | -1.5285 | -54.5466 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b888e1-292b-3719-88ef-590272e425b5 | -6.9341 | -43.659801 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76d41fb3-88b0-380a-b510-405b28a5dfea | -3.0354 | -53.9272 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae6bf77-b459-382f-abbc-56e5c48e3a07 | -10.2945 | -47.999001 | 2026-10-08 00:48:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45941c99-f001-3c83-a92d-faa2e7844ab3 | -7.2058 | -45.360298 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01d18132-9953-3f7b-931d-d12a1a242147 | -13.7892 | -52.798801 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8922934-f329-3d0f-a5fe-5f13a0dd2b8e | -2.8526 | -49.5438 | 2026-10-08 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99c0e150-0fac-3583-a5cd-b1249845e674 | -3.0233 | -54.055698 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50b584d4-a6f4-37cb-ba73-33681c3f6a9d | -6.8965 | -43.715698 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7bb2010-f91d-3d0d-ab2c-011f37d7984d | -7.2209 | -55.127102 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b45be7d4-3538-33ef-91c6-757505534441 | -4.3651 | -43.796501 | 2026-10-08 00:48:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92b5d5cd-ec35-3af2-8f6e-c3d8f4dc7180 | -2.8722 | -54.160599 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c535f0b-76ed-3731-beb9-60ebb92b6d80 | -3.1684 | -50.461601 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0de75cb-d353-3f7e-9d74-43570dfe94e5 | -2.8624 | -54.887001 | 2026-10-08 00:48:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe318b06-c88b-3f32-8af3-f7cc8e338a6c | -3.0418 | -53.910099 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4afe43cc-bb47-334a-830d-0c322a9c47fc | -4.9631 | -55.128101 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21fd92fb-e732-302d-8ab2-f817fff12df2 | -9.9001 | -44.808601 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2e52435-c8eb-336d-b039-12e236147cdf | -1.5141 | -54.573898 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba784eed-bb12-3fb1-b221-020ae9b184d0 | -3.5104 | -54.658901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e15a49f-bf35-36e4-ae37-da22e6bbc876 | -7.8831 | -55.014099 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bcc9405-f37b-3ca2-bf8d-17f491c9a262 | 0.943 | -50.2052 | 2026-10-08 00:48:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 696d8771-5d31-32f5-b902-11d2013f673d | -3.475 | -50.092602 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e26c7f8-162a-339b-927c-d8bee2e4be00 | -6.1208 | -51.956299 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ec68f1-5c2c-3400-8690-864763d681ae | -2.8837 | -54.166 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa82dca-69a5-3487-aea1-a0c93ea6a9af | -2.9327 | -54.155102 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b81c672e-fba3-37bf-b4fe-508064903603 | -3.0268 | -54.070702 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347c741e-656b-3135-86a2-527068ba4b0f | -6.1071 | -55.702702 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e67d592-38be-391c-8d87-105318afad55 | -2.8359 | -54.136902 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8e2d74c-11d7-3033-bc33-1991e4d4763a | -6.1366 | -47.9249 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b54341a5-a079-3a16-a059-63dd0c909203 | -7.2098 | -55.1693 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d337f3-673d-3042-bd2c-e1945b26480f | -6.6731 | -55.1078 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01764f6-a849-3857-835e-3b92610f90a7 | -9.8711 | -50.500198 | 2026-10-08 00:48:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03e7b660-ba8a-379c-ac81-4348ed234552 | -2.7795 | -54.070301 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6862d23-a1c6-349f-8c48-6580009c29cf | -5.2389 | -48.4081 | 2026-10-08 00:48:00 | METOP-C | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab65ae5-13ed-370c-bfeb-581d74b58d28 | -13.8088 | -52.794498 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c745b74-be5d-379a-93f6-f9fb064a4e88 | -10.4918 | -47.302101 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abaa597d-042d-310f-bb82-c16de7c181a2 | -3.1667 | -50.454498 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d2c30d0-ee0a-3350-ae96-de2872d10811 | -2.8711 | -54.200699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2d8f8a2-da0a-3c14-be7d-636a1d2b494d | -3.5388 | -50.100899 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23010f6e-7e4a-3ede-8aa3-539837af69c3 | -3.4835 | -54.631001 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8fd4429-367d-3ea4-9c7e-741c0afa61ba | -3.0503 | -53.947399 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77edd704-75d0-31c4-8f11-dd5dac41ad87 | -4.1559 | -55.148602 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cfc29bb-7c5e-30b1-8431-f34e100a3e13 | -6.2433 | -52.8606 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25cac450-b408-3beb-9a3d-49750c1048e5 | -3.423 | -58.602798 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac5f2a7e-7455-3817-beb9-b3d21db4bf28 | -3.5453 | -54.676601 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f28d292e-7f64-357a-a06a-da4baa37f8c6 | -3.2835 | -54.021801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15209a7f-c1d4-3283-bf74-97d3b28ff815 | -5.7587 | -42.0714 | 2026-10-08 00:48:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51f27218-ca5a-3f5d-bf76-13c43cb101f2 | -2.3744 | -56.134998 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02926f54-33fc-342d-b343-e91896a28925 | -2.8942 | -54.076401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6e1d2da-3159-3d2b-922f-2abd5556ed22 | -3.2563 | -54.672798 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8c73e28-14ac-3451-b57b-a102f397258d | -6.1169 | -55.7006 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0c329ea-c308-3637-b05e-104b73cdd4bb | -11.7864 | -46.792301 | 2026-10-08 00:48:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b752fcd-6845-3531-9c5b-48a2c6417ac4 | -11.395 | -46.7117 | 2026-10-08 00:48:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c06eaa6d-a4f8-392c-a4d6-2c8b5c0a9780 | -4.4461 | -54.976299 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README28.md)
