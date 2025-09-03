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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 050345f5-1239-3c72-a0f3-4be0c3641d3c | -14.99798 | -50.05357 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e458b83-2433-3ad9-82c0-8270de0f47bf | -11.12392 | -44.67307 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 59aec793-11e4-380f-8886-6212fd36515f | -11.86538 | -52.428 | 2025-09-03 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 9f9624fa-66ba-36c4-a017-94101a1825bf | -11.86186 | -51.46322 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 08efeb58-8830-374d-9d5b-b364a9552051 | -11.59543 | -52.06688 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 013b4ead-e5e3-3037-9a2c-020a129329fd | -16.30605 | -52.95998 | 2025-09-03 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0f72ccd3-75fb-3dea-92c8-74cbc8c11700 | -8.87947 | -45.81126 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6fc37945-c019-315f-90ba-731d7018e124 | -15.01727 | -50.06014 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cdce2a43-7723-3f6c-80a2-2d247b64cf40 | -12.49792 | -53.84648 | 2025-09-03 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 548fa97f-38cb-3de4-b133-fe2a5eeed8f4 | -17.25237 | -44.86325 | 2025-09-03 00:50:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f7d57838-9399-3f04-95e3-afb22cdc7616 | -15.74606 | -53.68773 | 2025-09-03 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b44ef007-7b88-3e68-a563-ea6d3c375943 | -7.48786 | -44.8192 | 2025-09-03 00:50:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 1f557981-3ab3-3368-aa8e-d9ab011f0767 | -11.60038 | -52.1027 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 969bed91-b568-324e-9b33-5105aae43285 | -10.45404 | -54.78722 | 2025-09-03 00:50:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 4f6afa4f-b860-3b39-b388-8797871928ac | -12.1697 | -50.13433 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 45219042-ac9d-30f3-9cad-61548dedc6d3 | -11.38173 | -43.5687 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 74bab2fe-c75e-3db0-b66d-0ea291f8c525 | -16.54546 | -55.08337 | 2025-09-03 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 9cff0414-81ba-3f65-b99e-f23082599e37 | -9.95912 | -51.63286 | 2025-09-03 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f265ea6c-2052-3918-a3b7-e319dbcf5c8d | -11.60921 | -52.10142 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7022c1f8-495f-365a-9d80-dcd1efcd8301 | -8.06445 | -45.38223 | 2025-09-03 00:50:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0e9e74b7-4371-3fff-bcbc-0b86a3b8a30e | -14.73658 | -46.9756 | 2025-09-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 02760aa1-21f7-39cb-b96d-a2058b61b4f5 | -12.29747 | -50.0029 | 2025-09-03 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 828fce03-8281-354d-b1c4-21403d05dd84 | -9.75091 | -46.92866 | 2025-09-03 00:50:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 742c3ac3-8c10-3021-b593-62c6cd7c6c41 | -15.01862 | -50.06954 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| ca9b232e-86ba-328a-a2b3-ea4030b31d9f | -12.9277 | -57.0009 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| abc15e92-6d1c-3e32-ba5e-c7d560b022be | -9.13759 | -49.64511 | 2025-09-03 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a767b5ff-f010-380f-96e8-eca0d269691a | -11.0626 | -52.08086 | 2025-09-03 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c3bd5cff-cd9e-387f-a413-6ecae587532f | -10.49476 | -53.65814 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d64467b5-303d-3619-affc-d23903342616 | -15.59882 | -52.67436 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4ca282dd-a6b8-3e85-ac00-bc6681a0e3b2 | -10.05451 | -48.08976 | 2025-09-03 00:50:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 4ccef866-237e-3fa2-98f2-628cde3497d4 | -14.40482 | -51.66757 | 2025-09-03 00:50:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9ac7dc40-eeca-37f3-88e2-d785fd469c76 | -12.91203 | -56.9424 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 8745b342-292f-3610-925f-7171b817d13f | -15.16132 | -52.36118 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd0b0f2c-9029-334e-beb7-60b00a579bca | -13.90779 | -48.10729 | 2025-09-03 00:50:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3964df4f-25f8-331c-8058-05bfea1e0057 | -10.48496 | -50.33918 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| aa705988-c866-3bd3-a4a4-8b31ccdf0b30 | -12.88216 | -48.03505 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 9b5d2bec-ed32-3e2b-8df1-a4d019cea6b0 | -12.93553 | -56.9665 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 3055d174-d598-3f4e-ad8b-74584af8d874 | -8.21349 | -49.56313 | 2025-09-03 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 841d1490-0dae-3ae9-a202-ae93d94bbc38 | -18.02314 | -51.6115 | 2025-09-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 85862346-93ab-32ed-871b-22e09f233c3a | -14.40606 | -51.67666 | 2025-09-03 00:50:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9f0ba662-9bc3-3ab8-8456-8169d69dfb45 | -12.75752 | -47.6819 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9bcdfb02-8188-378a-8770-6614e9bdf775 | -12.64394 | -56.9948 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 83fbf593-f494-32ae-a4ba-f4296c512cf9 | -11.58891 | -52.15007 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 62a24e1d-c6d1-3abe-8c48-00ada865301f | -12.83469 | -48.06643 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1f2e0405-54aa-3590-b1d7-a4177e525695 | -11.02521 | -51.47611 | 2025-09-03 00:50:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 416f5c5b-0bb2-323d-a6bc-794a331f7efa | -16.40133 | -48.1251 | 2025-09-03 00:50:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ec22df94-c7b8-386c-8dc5-fcd8ed7ffcad | -15.03386 | -50.04786 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 78af8dac-b42c-3d1d-9fd8-9e6fcf6ff513 | -17.36191 | -49.188 | 2025-09-03 00:50:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0707bf6c-696b-3f8c-bb22-dac9b71633a2 | -15.71866 | -49.04785 | 2025-09-03 00:50:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec8fe96e-1ee7-3adb-a493-aca6812ce050 | -17.54006 | -46.61137 | 2025-09-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1134dbd0-098c-361b-992d-aec17002af75 | -8.02256 | -44.055 | 2025-09-03 00:50:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3442a3d5-2dd7-3e2d-afea-ede4743ee934 | -11.09169 | -52.03104 | 2025-09-03 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3acd527-af35-345c-bffe-e6c8b787446c | -18.14329 | -51.75299 | 2025-09-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 1d6e7a26-108d-301b-8696-eedd5d537d54 | -12.29891 | -50.01268 | 2025-09-03 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4479a16-7502-38e9-af38-53421a2bcbbc | -11.60285 | -52.12062 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 190.1 |
| a2a1c54c-a743-39d4-8781-dbc62cc48aa4 | -11.61044 | -52.11038 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 74eed873-1842-3cbe-b6b1-122fd4efbeb5 | -15.55148 | -48.32173 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 87c6aee8-6b23-3e8f-8ceb-e62ec08c9258 | -18.02953 | -51.59109 | 2025-09-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8298def8-4bcc-355a-afad-1f44bff0b113 | -12.92001 | -57.0076 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 904f09db-07ef-310c-b28c-c7a0f87f969c | -11.61308 | -52.0643 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 0cd3d4e5-d601-3719-8d88-f8df8b9ae6f0 | -10.45203 | -53.61234 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c5b31646-a204-38a9-b5a3-d7d603a132e4 | -6.97239 | -44.36367 | 2025-09-03 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 74cea6f9-f1a4-35c5-94ba-d14983561900 | -10.0884 | -54.76985 | 2025-09-03 00:50:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 92d1a09e-72fa-3744-ae66-6ef401fcb35b | -15.71665 | -53.64342 | 2025-09-03 00:50:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| afd2dafe-6e84-31a3-b690-52ce764f02aa | -13.00617 | -48.10665 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| dc4d526a-c8cd-3f09-8032-a9cb8930f0ee | -11.92182 | -46.67241 | 2025-09-03 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4ea21003-9ee5-3de1-be87-bbe73a4b2344 | -11.60409 | -52.12958 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 2d538244-ee41-3c9e-97bf-ec834690529a | -12.93925 | -56.97178 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f6f6a0ad-2b73-3e34-a4a4-e6b1ff728c87 | -10.05828 | -48.08321 | 2025-09-03 00:50:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4038f42e-3a83-3517-a31c-17eec04a63cc | -13.29936 | -46.9227 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 30b1f482-3b80-3868-af0b-b0b5eafada60 | -13.70403 | -46.93404 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 76ba55e2-7695-3ebf-9fda-2c14c6add00c | -16.41096 | -48.12353 | 2025-09-03 00:50:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1c95ce1d-9fb0-3a67-8243-02fed8f2afa0 | -12.93937 | -56.99941 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| a588322b-c74a-3952-9218-cad075c4a9de | -11.03356 | -45.0742 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7ded0b6f-966e-37e1-a6a3-8b900d8be285 | -13.28543 | -46.83649 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 4d2ab44f-e377-3214-b63e-a6eabaafc9da | -8.08221 | -47.60715 | 2025-09-03 00:50:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| de8f8eb8-c93c-3f3c-a241-9ce8b7fa61fd | -15.58213 | -48.32857 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8e548666-e145-344b-87fc-951a866c1919 | -12.94525 | -56.94878 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e709c7c2-89cb-3c43-b0d4-c832b3f10f71 | -11.4269 | -55.18454 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cab7fe89-4e8e-3db3-a951-7820eef08ad6 | -12.93524 | -56.93953 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| f2524abb-1132-37da-b44e-e2dcdd7c5a4e | -14.6238 | -48.09622 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2d90c931-b149-3a84-a660-5978ba40ac5d | -15.54424 | -48.36297 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d1667764-b530-3cbb-8616-b67c2ad749bf | -10.48636 | -50.34896 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 4c13b183-746d-3c75-a511-216b0477b3a1 | -9.1408 | -49.66688 | 2025-09-03 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c9207a91-6c3c-3333-8d08-705222c3dfba | -15.54692 | -48.35618 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| d2d73699-7924-32f5-b1dc-601ecb5ca698 | -15.55197 | -48.38894 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 952c8f4c-9faa-3693-a567-d3bb7ede4a16 | -13.285 | -46.84254 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5a0564cb-ae64-3836-872c-20f1d1b0a08f | -11.59791 | -52.08479 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d90b1d98-7274-31a2-9a47-008aaee58911 | -12.94716 | -56.96498 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| adfea69f-3fd1-3285-813e-81df84d19914 | -12.84105 | -48.04006 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| bdbcfe89-0f92-3b94-9e98-ef59f6de334c | -13.6975 | -46.9633 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 58203df5-aec0-3f19-80d0-a758ec45eecd | -11.06136 | -52.07193 | 2025-09-03 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 88f26026-9233-3788-90f5-193cd17b5a04 | -15.17528 | -48.01571 | 2025-09-03 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9af67045-afae-394b-8b1e-86843e9910f9 | -10.45261 | -54.77657 | 2025-09-03 00:50:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ad3f1b07-4ebd-3fc7-adcb-1d0880537e96 | -12.49814 | -47.47753 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6fedbb2e-fe52-3489-b62c-14e32871b8e3 | -9.51774 | -48.89117 | 2025-09-03 00:50:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b2ff7178-002e-3094-915b-47b7e166758f | -6.69602 | -44.17415 | 2025-09-03 00:50:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b043f708-54d9-396e-901b-78ceefbf2613 | -12.93364 | -56.95025 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7920104a-4c1c-36b9-850d-3517aa0657a9 | -10.12984 | -47.4419 | 2025-09-03 00:50:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 618efaf0-e978-3803-888d-d8dbf5864dc8 | -12.99247 | -48.0849 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README13.md)
