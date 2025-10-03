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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8d93a9a-6be2-311e-9c86-b3923eb5ca14 | -12.7669 | -44.9137 | 2025-10-03 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3f345825-bbe3-3ba8-8ddb-b19aa11e5e4c | -13.1341 | -47.9043 | 2025-10-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2df58b01-c086-3b37-8c48-4522a54313c8 | -9.9186 | -43.6978 | 2025-10-03 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 6455d568-fd54-3240-b644-3d1a7611813d | -7.7944 | -42.5132 | 2025-10-03 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| ccefe8e8-6f48-3cb7-b4c9-4a37c6807f1c | -13.7954 | -47.5812 | 2025-10-03 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f280127a-8638-3182-a6ee-2e0c8fe2adf8 | -10.2781 | -50.3032 | 2025-10-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 60fde6c4-210a-39f8-b540-5ee7a76e9e52 | -13.1345 | -47.882 | 2025-10-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5d2de249-99ef-3e16-99db-1e6f04d51f4f | -8.2105 | -47.0084 | 2025-10-03 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7ca66ed3-b696-355f-968d-98bff855634e | -6.679 | -42.8136 | 2025-10-03 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 4cf780f6-e457-38bd-90ef-45f6391e68da | -7.7743 | -42.6103 | 2025-10-03 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 208.7 |
| 2bce712a-56ec-39d8-b0e7-df0ba8bf254f | -7.2913 | -45.2548 | 2025-10-03 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 22d67fa9-eadd-319d-9e74-aa7f84adbe9d | -15.8097 | -43.7355 | 2025-10-03 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 162.1 |
| cfa05597-ab68-3611-b0e7-278914a65db2 | -13.1353 | -47.8373 | 2025-10-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f31d41d7-1bfb-3d99-bb2d-4ca3d0ec916d | -11.863 | -44.9612 | 2025-10-03 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c0b38d50-5782-3b82-9ad1-e011e36d4aa6 | -14.2939 | -45.9076 | 2025-10-03 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 1e13630d-f96d-37f4-9535-b1bce6dfc0d6 | -12.763 | -50.5352 | 2025-10-03 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 8c9c9723-7d00-3ac2-9e60-ecbf3a2d123d | -12.6127 | -46.9951 | 2025-10-03 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 77ebb0c7-a29b-368c-bedf-563971df1b29 | -11.1275 | -47.8634 | 2025-10-03 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d65e7daf-82c8-3799-80d5-dbe556d50e78 | -13.3611 | -48.1159 | 2025-10-03 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ef7f0b92-0581-3b5d-b528-745363ac1ef9 | -13.1546 | -47.8345 | 2025-10-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 02309983-3736-3802-8d5a-1d5b53fb5c7e | -14.3899 | -45.9601 | 2025-10-03 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 141.6 |
| d55f1bf3-9039-365c-8449-d34db347a61c | -15.7707 | -43.7197 | 2025-10-03 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 177.2 |
| bd1efcf6-521f-3e93-9bc6-fc3ae065c6be | -15.8097 | -43.7355 | 2025-10-03 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 0860fb34-fe6b-3a9c-812d-89f161ed120b | -12.7623 | -50.5782 | 2025-10-03 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ba4fd520-acf9-3db9-b3e0-dbbfd0ae01f2 | -7.7944 | -42.5132 | 2025-10-03 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| db3bda0c-ce9a-3b5c-819a-e4b20e8be91e | -10.2779 | -50.3246 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4b41e776-e85a-391b-af26-5c0158c19bc8 | -9.3547 | -45.951 | 2025-10-03 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 6bb35653-17f8-3a2a-833b-8ed0c1dec490 | -10.019 | -48.4964 | 2025-10-03 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 129b7ae0-ea57-3ecf-9cda-704eb6c32cab | -11.1275 | -47.8634 | 2025-10-03 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 33e17414-fcbd-37e8-8d03-1b5c46a537e0 | -11.8818 | -44.9815 | 2025-10-03 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 226.7 |
| 12edc23f-df3c-3559-a643-aa8e87d2be50 | -6.679 | -42.8136 | 2025-10-03 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| c7865d94-07f5-361f-bf1c-2bd74f46da60 | -10.1281 | -50.233 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f185d082-9c43-386c-9cef-9f001b225753 | -5.7688 | -41.7278 | 2025-10-03 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 187.8 |
| a8ed3b98-9c3e-382a-9464-f08b42d23848 | -6.6792 | -42.79 | 2025-10-03 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| ad5fdd5e-b634-3bc5-8358-5592190d276d | -11.8626 | -44.9844 | 2025-10-03 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c386fa96-3971-32c0-9736-46a4d6f33a8c | -9.1813 | -46.1956 | 2025-10-03 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e3541b58-8964-3577-9844-45cab2a9be21 | -11.9159 | -46.3044 | 2025-10-03 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e65c7d8c-28e5-30d8-9bd7-702d7480095d | -7.7755 | -42.5152 | 2025-10-03 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 500.8 |
| b2aca192-9b54-3778-9017-863655716a6c | -10.0909 | -50.194 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 2660b338-e6ea-328c-a14c-ac35e953e45b | -8.5458 | -47.264 | 2025-10-03 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 57e5fd6a-96b0-318c-84ce-365fbe63bdcd | -18.9673 | -48.4968 | 2025-10-03 14:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 418.5 |
| f4b9cc7b-d8b1-374b-a36b-39ab10e804b6 | -9.9959 | -50.2462 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9da2e68a-813e-3ec2-abc1-8efab4a3ab78 | -7.2913 | -45.2548 | 2025-10-03 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| be5806ef-14ea-303a-a98c-0400f8e0c587 | -14.6497 | -44.7499 | 2025-10-03 14:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 111.7 |
| fa876dda-a44f-3c68-94bc-17b872f74174 | -6.5551 | -43.8758 | 2025-10-03 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4f9e5259-8f3f-34fb-b8b9-0f49e989d884 | -9.8769 | -47.8324 | 2025-10-03 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 2a16ad80-d385-3ce0-978c-19ba6a7d4a47 | -7.7752 | -42.539 | 2025-10-03 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 294.1 |
| 66a8f257-33d1-3343-bc57-4e4bae4287dd | -6.0809 | -42.4881 | 2025-10-03 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 3d840979-12ac-315e-9428-f03c2bbaed25 | -7.2845 | -44.18 | 2025-10-03 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 9fa64d94-b8a4-365d-84fd-f5e1f2c465c6 | -9.3389 | -45.7266 | 2025-10-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 4a43ff0c-e6a2-3270-a032-8fa3c1de2eb6 | -9.3386 | -45.7493 | 2025-10-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3d03867d-f62e-3ff7-9639-3d91152d07ba | -12.7435 | -50.5591 | 2025-10-03 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 286.2 |
| 98ce94f7-717d-30e1-80c6-0816c20d15ad | -6.6976 | -42.8354 | 2025-10-03 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 432480fa-e251-3d72-a006-530b038da212 | -6.3587 | -44.7654 | 2025-10-03 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f665109f-f826-3a5b-9c39-e82d279e38b7 | -10.0717 | -50.2173 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 626a8969-d2c2-35e4-a2d6-7500c4b357c0 | -9.355 | -45.9284 | 2025-10-03 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ecfa2b59-54f0-387c-b620-58763dc1905f | -13.1546 | -47.8345 | 2025-10-03 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 5c386e3a-a36b-3fdf-9213-7890d4c3b635 | -13.3611 | -48.1159 | 2025-10-03 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 24536fdb-8390-31e7-bb2a-d0c6db73856f | -11.9151 | -46.3499 | 2025-10-03 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 18db0df3-78c0-3326-8b05-19993537dd31 | -16.0212 | -50.9425 | 2025-10-03 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| deacc0ef-5795-3388-9776-d440fb24ab0b | -11.0527 | -47.7842 | 2025-10-03 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c6445993-8a3e-39e7-8812-853b0947c7c4 | -10.0145 | -50.2657 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| e5f78293-c82c-3842-8977-7e7657c736e7 | -10.2773 | -50.3673 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ba76e409-e2bc-3fc3-bdec-3da38b43a8c0 | -8.5959 | -44.7833 | 2025-10-03 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9e581932-2176-362f-b9f2-e007c3ba0607 | -14.0032 | -44.961 | 2025-10-03 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 1bd90ffc-13ba-3041-b1fb-2fe778df11d2 | -7.7941 | -42.5369 | 2025-10-03 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 167.9 |
| 2b1d6aa7-9b64-3152-8949-fe70280e3bed | -8.2478 | -47.027 | 2025-10-03 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 52753338-1981-3018-a3ae-c140c8dbbeba | -6.3529 | -43.4516 | 2025-10-03 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 79b25353-4dab-3626-94af-99ccf81fc084 | -9.9186 | -43.6978 | 2025-10-03 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| d2f7314f-cbe7-306d-8517-12513b82e62b | -9.9182 | -43.7212 | 2025-10-03 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 186.4 |
| b8370f44-a35b-3e11-a187-3d77005c3bb4 | -11.1444 | -43.3845 | 2025-10-03 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 101.1 |
| ce64f958-c034-369b-b03a-5031ae301799 | -11.9155 | -46.3272 | 2025-10-03 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 389.4 |
| e0fc40e3-718e-3e6d-bc12-c64a8b7b9efc | -12.7819 | -50.5543 | 2025-10-03 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b2ff3509-0297-332a-af27-14d02156e531 | -13.3422 | -48.0965 | 2025-10-03 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0b059050-a79d-3020-91b7-42c5deaf8e2a | -10.0342 | -50.1997 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| b96491d9-7cf3-3828-afb0-d0ca29d4f066 | -16.0217 | -50.9207 | 2025-10-03 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 99f18ef6-c154-3b62-bada-18b4ff24a037 | -8.5599 | -44.6494 | 2025-10-03 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 1a55d66b-68ae-3383-abcf-76bf6593d500 | -10.2776 | -50.3459 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 434d6c93-3e5d-3cfb-9018-454a2a3a4706 | -12.1088 | -45.1554 | 2025-10-03 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 6f606a27-5de5-3a92-b53f-4bc1dd1d00e7 | -16.023 | -50.8553 | 2025-10-03 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 161.2 |
| bcf8f3bf-2b18-3204-b23b-69ee5c8f0552 | -10.0903 | -50.2368 | 2025-10-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7b70fbf4-5588-3c19-adba-e9a4c920ca0e | -8.1699 | -44.1608 | 2025-10-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 176.3 |
| d39f3669-5904-3f9b-8e0d-6419866febd9 | -8.1702 | -44.1377 | 2025-10-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 53f4eb04-3a82-3d48-966b-f85c16497351 | -6.0806 | -42.5118 | 2025-10-03 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 158.7 |
| d359d9ad-2f58-3375-8185-49bdabb38aac | -6.6978 | -42.8118 | 2025-10-03 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 65f77156-e390-37ed-9fac-d7d5e992f348 | -12.6131 | -46.9725 | 2025-10-03 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 31ce0a6e-6929-385d-a9b9-578206066a1b | -5.7037 | -42.6605 | 2025-10-03 14:10:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 11052948-baa8-30fe-ade6-a478edd5d96e | -10.0187 | -48.5183 | 2025-10-03 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 4462abf8-569f-3c38-8b66-32e8a406073b | -9.062 | -46.6565 | 2025-10-03 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3233794f-e7e9-3f31-8630-07efbafa2d2d | -6.6787 | -42.8372 | 2025-10-03 14:10:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 5aad839f-5f17-30af-a55a-f21d502339d7 | -9.9035 | -45.9553 | 2025-10-03 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7055efe6-36bb-3004-912a-10e826d55a76 | -9.9372 | -43.7187 | 2025-10-03 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| af8815d3-f40a-36a7-b6e6-17958bf76253 | -14.2939 | -45.9076 | 2025-10-03 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| d1693002-4e8a-30bf-940b-099201e361ed | -7.7749 | -42.5628 | 2025-10-03 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 150.5 |
| cc77f311-af34-3cb0-94c0-69928238c15c | -8.1731 | -46.9897 | 2025-10-03 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 09916ee7-6f02-382b-8af2-376d1b84b33b | -12.6127 | -46.9951 | 2025-10-03 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| c396d157-a7ff-3143-85f1-807b43eca2ce | -12.1215 | -43.4453 | 2025-10-03 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 44615346-eb58-3732-bf34-75e38af1d16b | -7.7746 | -42.5865 | 2025-10-03 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 236.8 |
| 59151f3a-8e6d-35db-8600-8624d600182d | -11.1252 | -43.3874 | 2025-10-03 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 7091a0a6-3c62-30ed-98f5-628e7363528c | -9.9369 | -43.7422 | 2025-10-03 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 256.9 |


[Clique aqui para ver as próximas entradas](README153.md)
