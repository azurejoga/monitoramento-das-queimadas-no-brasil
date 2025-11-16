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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 153af5d9-6481-36fd-a0a6-61355213710d | -3.2228 | -52.60197 | 2025-11-16 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a539c6-0837-31cc-a999-99618374cd51 | -4.68675 | -46.51888 | 2025-11-16 05:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1ab3e97-d1d8-3512-a11a-06c6c7eef67d | -7.7159 | -47.29403 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3b3f006-a754-3123-99a9-ea0729eb88fb | -7.21647 | -47.98458 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c2ed044-4d17-3cda-bdc1-7dca4326544c | -4.50147 | -50.79126 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b70e9319-4ecd-3bd5-ab4e-3da2f17c8dd9 | -5.48707 | -46.9148 | 2025-11-16 05:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77e8b227-1c01-351b-bb4b-86b9a5005d64 | -4.67614 | -50.36509 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 786071e6-d5ca-3a38-9b78-b83b00af4ea8 | -7.26644 | -48.02226 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38bb338f-93fb-3556-9d29-8f871723b801 | -4.24434 | -50.05197 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da19203b-57f9-3e10-9b4b-8528ab170ad5 | -1.19561 | -53.72474 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0f58dea-a7b6-3f5b-9d06-bb6f31a136da | -1.85066 | -56.37167 | 2025-11-16 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0edf6916-2228-3b8a-8d7f-014f2133ea97 | -3.54787 | -55.49403 | 2025-11-16 05:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83e995df-d3f9-36d3-8f0c-81bb7f6b0d81 | -2.17537 | -52.08498 | 2025-11-16 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5e98669-6c2a-3e8b-8755-25fe01f8960b | -0.95681 | -52.33802 | 2025-11-16 05:25:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a558bf3a-6c78-328f-9ff3-deae73b5e3a1 | -3.91495 | -54.13387 | 2025-11-16 05:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8672658a-3908-39cd-a49b-04e6d88dc4ca | -3.40077 | -50.1834 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efe118fe-1c0a-344c-9ab9-77103cf561e8 | -3.38518 | -50.13544 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b0846f-d07f-31be-9f5a-cecdeef2a53e | -4.73953 | -46.38636 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5ebfd4ed-766f-3b17-b345-e8476fe598d2 | -2.13775 | -56.68084 | 2025-11-16 05:25:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8ab62746-47d3-314d-8f68-d5458a4b0764 | -4.50052 | -50.79197 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d268297d-d039-3bb4-ad42-de9b2d05733e | -4.50569 | -50.11743 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0f0de08-2bd0-3f0c-b6c0-9153f2014fe5 | -1.3448 | -54.61313 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7cde0d0-781e-398c-bd23-357b4ec17f29 | -2.57749 | -51.87691 | 2025-11-16 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d39c7c5-ae76-38dc-8334-cf5fc55d79aa | -2.86805 | -51.47664 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03bc0a9e-7dc7-3838-9aff-31ad7dddab84 | -2.93478 | -49.35206 | 2025-11-16 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5c10ecf-88ce-3724-ae6f-6c4a0d8cf981 | -3.02115 | -51.6071 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1028a48-3171-35bc-afa3-f9655a4326b2 | -4.05402 | -54.84312 | 2025-11-16 05:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f53c3408-4750-338d-9c08-143338fa5d53 | -3.02362 | -51.62497 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c33813c9-51a4-3a4a-9789-c683455f0a6f | -3.2839 | -53.81933 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ba7f258-9fec-38b2-9fe5-70d0ef00dee5 | -7.71914 | -47.2953 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 695ffe9c-e471-3a56-b954-fd4b9777f446 | -3.85791 | -52.08151 | 2025-11-16 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a634ccc-750a-3bfe-a22e-e7b5fe81f927 | -3.30503 | -50.07617 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e288b6d-cd9d-3c10-8614-3072707b4d44 | -3.33064 | -50.27319 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0084b60e-f441-351c-b3a6-2c6e25917b80 | -10.66921 | -49.3585 | 2025-11-16 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c47a0d2b-ab96-39ee-a9fe-61f261f650e2 | -12.00696 | -49.27521 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 66c630b8-726d-3a91-ae66-29cf75d1a8fe | -11.16662 | -47.45646 | 2025-11-16 05:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0a8bc28-5c40-3bb1-b011-48f59b92e0b9 | -10.93623 | -48.68757 | 2025-11-16 05:27:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e25ed2d-9053-39c1-961d-37a11bb22f8c | -12.00035 | -49.27441 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 168c4c8b-6b9a-30f7-a28d-b860c51367b6 | -9.71274 | -48.90292 | 2025-11-16 05:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 863b486d-1968-3192-8bf3-635ceb5e8f62 | -12.20308 | -49.61804 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dfb71163-12b4-3eef-8b46-153f7f1f77b3 | -10.39053 | -49.05381 | 2025-11-16 05:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cb4a48c-8d6a-3220-9586-085de9feadf6 | -12.39682 | -47.56653 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55e2a41b-905f-33a1-975c-078c40eed972 | -12.39761 | -47.55892 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f828c30-fc83-3a3f-9c54-63367357d429 | -10.93781 | -48.68687 | 2025-11-16 05:27:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cb118ec-2f99-3b23-af84-4cc64f0f5720 | -10.80831 | -47.98759 | 2025-11-16 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eec9e48f-2311-3912-83e2-40040c15f92e | -10.66208 | -49.36317 | 2025-11-16 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dde4fd04-4d08-3cdb-81de-712487637215 | -11.70746 | -48.85614 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6504e5a-3b12-3da4-b766-bffc72763bbd | -12.05854 | -48.21322 | 2025-11-16 05:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06757ae4-8809-3c32-9e14-fd6e97a3671a | -11.71424 | -48.85677 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6033146b-19d7-39e3-b322-5b7591bdd51e | -10.9281 | -48.69799 | 2025-11-16 05:27:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 397cbc22-b060-36f9-8515-9067ea9c5aa8 | -9.83139 | -47.08028 | 2025-11-16 05:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0cd595e5-781e-353a-b11a-85e6ef26b05e | -11.8461 | -56.89707 | 2025-11-16 05:27:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d233cd7-0a23-3c0b-84cf-3040aec16a05 | -12.0053 | -49.27186 | 2025-11-16 05:27:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 45b2b67f-5c1e-377c-aa76-07cc14cc68ad | -11.70535 | -48.87442 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e6b0d139-a39d-3c38-94ff-f5c525d892b6 | -10.66273 | -49.35772 | 2025-11-16 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ad09198-8eb4-3cf5-bba8-7af3ee9879df | -12.40408 | -47.56197 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0d42ca5-e4dc-394a-af81-0e55c925cd8f | -11.8501 | -56.89766 | 2025-11-16 05:27:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c33d9d00-823b-3b31-8ac4-acd08a39c6bc | -12.39677 | -47.56084 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd9f6b6f-c8c0-3093-ac55-9c731019e67a | -11.71455 | -48.86816 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6e438e2-b2c9-34cf-8c34-94dc4e18011f | -12.06557 | -48.21421 | 2025-11-16 05:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64d89244-d437-3c71-9126-7952a255e782 | -12.01127 | -49.27852 | 2025-11-16 05:27:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5727d36c-c99a-3792-bba0-42a0903e1b26 | -11.15917 | -49.44039 | 2025-11-16 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00858901-59a0-3a5d-9853-2b2ba8075b8d | -11.71355 | -48.86279 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08138f84-b31e-360c-a620-b3f4dbe6dd44 | -11.84285 | -47.60102 | 2025-11-16 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb55a521-4ed3-30b7-9ca5-b936d117d763 | -12.06481 | -48.2211 | 2025-11-16 05:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1219fb16-c576-3ee6-a49c-f6408071b90a | -11.71286 | -48.86873 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3467338-a9e1-30a7-97f2-8634f40a669c | -11.71212 | -48.87508 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99f71007-733a-3f6a-94e7-229fe6b6fdff | -9.71932 | -48.9038 | 2025-11-16 05:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9a4dc79-4c96-3662-81a3-5100b2376ec9 | -11.1588 | -49.44637 | 2025-11-16 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46ce3c10-f221-3f40-8935-05f81088ac33 | -9.83872 | -47.08112 | 2025-11-16 05:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d9c4afeb-9a43-3414-b9ae-8f82bd9d40e5 | -10.39029 | -59.18508 | 2025-11-16 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39155e90-e485-3e32-acfc-a70f44db49bd | -11.71963 | -48.86941 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2abb3dc8-0557-3eee-88a4-2d7d090a58d6 | -12.20371 | -49.61242 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2d10755e-a061-344e-8e57-cccece78e968 | -11.85016 | -47.59684 | 2025-11-16 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 888d7275-a172-383a-a338-5c56a7b08330 | -11.7152 | -48.8622 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbef0193-4309-339c-925e-dcb9d3044287 | -11.70908 | -48.85549 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62a9b598-3834-3a8c-a27e-9658659a47a6 | -10.9287 | -48.69308 | 2025-11-16 05:27:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15b35eae-9a69-3514-a75c-dd1c8977488e | -11.6618 | -54.5851 | 2025-11-16 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cdf0bb9-4609-3f9a-9640-2c7baa26ea13 | -11.99805 | -49.27683 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c58cd55-85aa-323e-9abb-184885642692 | -11.72132 | -48.86887 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62d29624-11e8-3387-9d8a-bd0aefdfffad | -9.82289 | -47.08696 | 2025-11-16 05:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f92ed110-621c-3818-925e-647f909d83cb | -12.204 | -49.55123 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb2ebc23-ca35-36e3-b984-bfb1a0a41820 | -11.70776 | -48.86759 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e6ae11f-0234-3006-90d0-63335180b88d | -10.66856 | -49.36397 | 2025-11-16 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9387ed9-966b-3e18-b953-464d93c763c5 | -12.39225 | -48.09394 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f0297de-b9e2-376a-b849-9f2e300cfe72 | -11.84935 | -47.60416 | 2025-11-16 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57ca611a-1719-32c5-a36d-068922077c44 | -9.68538 | -56.09824 | 2025-11-16 05:27:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b923094-3cf6-3e4c-8207-92cf45133203 | -12.1972 | -49.61176 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7875d37d-9e3e-3075-bafd-1ee583fe816d | -11.6598 | -54.58126 | 2025-11-16 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66b6e16d-50b6-3a41-91af-9c35ca7c2606 | -11.15942 | -49.44099 | 2025-11-16 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2451533e-b2bb-3b19-83bd-17b81fa23f8a | -12.39938 | -48.09464 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 178f9fd6-6318-32f6-bd3e-6b2d7e4934da | -11.70606 | -48.86827 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25ca3ae8-8af4-3e9c-ad13-f7a61cf08414 | -11.84205 | -47.6035 | 2025-11-16 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8199ff81-282b-3f14-a598-ed4b84b2002d | -11.16528 | -49.44718 | 2025-11-16 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1e2cd6c-e8fd-3812-8c51-904cc52f1fac | -10.54481 | -47.92687 | 2025-11-16 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 954e9db9-86d7-3db5-a0f9-d91ae438470b | -9.44332 | -59.20559 | 2025-11-16 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd5deb21-cf3a-303a-b17c-ceace16713b8 | -9.83019 | -47.08809 | 2025-11-16 05:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 48bcfc87-6035-3f9d-b235-ce359f220108 | -12.00629 | -49.28096 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 08d44a3a-4479-372e-8b49-0ba1ffa567b0 | -10.53771 | -47.92652 | 2025-11-16 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d3e126d-6b87-3c63-b3d5-38773872af1b | -8.8653 | -50.19371 | 2025-11-16 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README65.md)
