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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffeceef9-0b60-3b10-854a-8b53369254c0 | -5.83495 | -42.85261 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f11f113d-7a11-3a44-9c37-e1fe45e9f1e2 | -5.82476 | -42.88596 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 537fc675-aac0-31bc-8595-5a7379c23794 | -5.20347 | -45.06878 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d371bb57-d812-3f92-8759-6f3c3c50c33a | -11.47872 | -45.03556 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d01c496-2819-355b-837e-562977bcc04e | -10.57489 | -41.49798 | 2025-10-04 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fc972184-ab9e-3aa0-ba64-cbcea6818648 | -7.77069 | -46.24364 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 456aca70-e071-3ef7-b028-dcfbd0b82fbb | -9.11804 | -40.13509 | 2025-10-04 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cec6a216-733f-36ab-b1c0-946c45c3b606 | -6.67712 | -45.93203 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7500baaf-8b53-3d82-8c58-5f7b43e5d463 | -6.76918 | -42.24334 | 2025-10-04 03:51:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a4ad6447-362e-3728-a278-cfcf661ea679 | -6.66752 | -42.81734 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fbb04294-3ecd-3127-a71b-62951ac5a41a | -7.72724 | -46.24092 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3015574b-04d4-314c-8f2a-5e323e3ecc4d | -10.6071 | -49.14985 | 2025-10-04 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc638691-32e3-3f17-beab-e155fc365fd5 | -5.67196 | -42.72571 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31b3de90-40bc-31f7-b2a4-c94bfa7b56d7 | -4.61601 | -43.14993 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1518af69-d6af-3776-a7e5-9bab41ef41e7 | -6.37349 | -44.3052 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5454e1b1-9ea5-3e45-8ef5-0cfd4f7985c1 | -7.85783 | -48.19791 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aca913d1-90c6-33c3-b0ba-036ed86edbf5 | -5.88686 | -42.91844 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b8809faf-3191-37a9-89aa-567378f5ff5b | -7.78491 | -42.59052 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 273d36dc-4ec6-3c1d-9cb3-c538531245bb | -5.24791 | -42.9679 | 2025-10-04 03:51:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 92b8cb58-7ca2-3a19-9d72-dd1bab5f15c9 | -6.61062 | -44.29257 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70ed7f6b-ad9d-33d0-822b-95a4e6df6a61 | -4.65241 | -45.79808 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dd35abe-2d34-37d7-9bd2-c3686732b628 | -8.91696 | -46.6125 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 773863fd-c3d6-3d14-b99a-0cccaad927e6 | -6.55096 | -43.87299 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c3d6c2a-d21a-39d0-b1f8-c279f7af377b | -6.2453 | -45.35143 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4bec2f7-9e85-33e2-815e-a1004d4b51d0 | -7.72476 | -42.59176 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d75bc9f-e161-35d1-998a-3b2bb42f9174 | -11.7232 | -44.44495 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99b01ff9-2161-3abf-b429-ed803c82faa6 | -11.12395 | -47.84844 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d303321-1e67-3349-aec7-303f46b8b01e | -6.27979 | -45.07922 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca918ebc-7a15-31e1-8abb-516ca1439827 | -5.8443 | -39.25821 | 2025-10-04 03:51:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 870675eb-5d62-34e7-ab8f-d4d9394a7f8b | -8.22925 | -46.80594 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05a97b68-dfe0-3c26-bac8-98085fc3814c | -10.27908 | -44.33968 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72f31417-0d2b-3d3c-9d93-e30cda4733f5 | -6.59069 | -44.62875 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7a423a91-7a07-31a6-ae1d-8d5d254f3478 | -6.66402 | -43.51698 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d47642e1-f5b8-35a7-b54f-3a37e5635775 | -8.92223 | -46.06536 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcafa904-9667-3800-aa71-82849d0272ba | -6.55629 | -44.15609 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca475953-0fd6-3d4d-a236-f36d05e4ebb4 | -11.48044 | -45.02632 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ac9cde9-a47a-339e-b210-cf97551a7378 | -7.76714 | -46.23283 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2aebc1f-e9a5-3964-a876-2c1017fa9e44 | -6.66819 | -42.81332 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c7415e98-6c6a-3e8f-be3b-65539ca1ef1b | -4.95648 | -45.07093 | 2025-10-04 03:51:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bdad4db2-eaab-3058-aef7-d7e84f1455ad | -5.20245 | -45.07481 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc8b69c4-725c-3066-95de-b165f76e27a4 | -6.22249 | -44.27422 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a2e31d0-4613-399c-a012-299ca56b281b | -9.76698 | -46.21538 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0d48be5-fbd7-35c8-adf8-ba247ddd444b | -9.75265 | -43.61735 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a5776af-f5c6-3450-984a-fec63143fe3b | -8.71244 | -47.97955 | 2025-10-04 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e8dced0-2b37-32f8-a48f-475effdc92b4 | -7.75424 | -42.51937 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c25b732a-8379-3432-a977-d6e6eac32c2f | -5.72919 | -42.68205 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2774a1fc-02e4-3d87-b8c6-ab1a8af5e11a | -9.25753 | -45.78268 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66a0c3eb-644f-3b2d-a812-b634fcf1638d | -4.67028 | -45.68596 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 177d4f2b-fe55-3743-8e31-2f41993df774 | -6.36995 | -43.89474 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7182feb5-557a-3c6b-9182-4cd528262b25 | -11.08024 | -47.72541 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d206b1ba-c144-3dfb-ab89-0915c97236f8 | -9.11002 | -44.39831 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53fcc839-a6b4-3fde-8d0f-b9e0e6b3801e | -5.42706 | -47.0997 | 2025-10-04 03:51:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c742e187-c07b-3593-91f2-0b3ca131d4d6 | -6.70888 | -42.79422 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e3ae42bf-a789-335d-994b-ea6a10ba1ffa | -4.21821 | -43.59703 | 2025-10-04 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74dd5a67-a224-37f6-b8cc-3eb53eaf94d2 | -11.49674 | -44.98962 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a457b13f-4c1d-3f01-b555-d85f695ce73f | -7.52392 | -37.99814 | 2025-10-04 03:51:00 | NPP-375D | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 160a5f96-77db-330f-9285-a3ab78a0025e | -8.05918 | -44.803 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 27684756-819b-3d7c-aadd-77a0cc0ee767 | -5.4723 | -42.76286 | 2025-10-04 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6964c600-c4ad-3d65-a891-5e96aeac70ba | -7.73943 | -42.60621 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2d3e02d6-8153-3c23-8d17-7025e7f5777a | -10.273 | -44.34795 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7387155b-6c4a-340c-a28c-a60559d959e0 | -6.24479 | -45.35443 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5d028cb-5ac1-32e3-975b-05f88de09b0b | -7.85773 | -48.20545 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f23c288-f3c5-3cba-8956-84a545c2bb04 | -6.2264 | -42.92953 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad0b40df-4506-35a1-ae69-2e450d4f20f9 | -5.86808 | -43.56294 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d615df76-a567-37a7-981b-db1ef9f69deb | -11.50769 | -45.00731 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fb5bbad-1f59-3ea3-8af8-bd75a8f28634 | -7.77821 | -42.60495 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b91ec899-3255-3593-bc77-32e4b55bbeec | -6.24821 | -44.23742 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8c236e0-7f95-329d-9727-4bbb23fa9b8f | -6.87912 | -47.23193 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7bcf4aa4-3485-3d52-93c7-2585d99013d5 | -10.19132 | -45.48341 | 2025-10-04 03:51:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07d3472c-a653-364a-ac53-045e3c4c6a41 | -7.77251 | -46.26427 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be69570d-6d0a-3f02-9a21-ef6488074b3b | -5.68659 | -42.85302 | 2025-10-04 03:51:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b533d0cc-d5cc-3510-abc4-c8deb417c948 | -8.892 | -45.0264 | 2025-10-04 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d0c524e-350c-3636-ad8c-14063731fbf2 | -11.47027 | -45.03531 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34a4bc4c-7d6b-3f32-95e1-06031388cc04 | -11.00454 | -46.68643 | 2025-10-04 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a007af91-6e05-32e7-bd91-ad00b399fa1c | -11.45454 | -45.13978 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d42ea8ca-55d3-3a78-9c31-c6a59a4d9203 | -4.96161 | -45.07198 | 2025-10-04 03:51:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1d02f051-fa8b-3d95-8592-f2ec9c042dc0 | -9.75408 | -43.60912 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58b640ee-ef00-3bfd-af38-d9efa14d022f | -6.20222 | -44.3362 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20c63499-796f-3eda-ae33-a9191d5104c8 | -7.72256 | -42.57963 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 01a56547-89ca-33a6-973e-b4043a3f6d0b | -5.80217 | -42.72424 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a7272fb-ae41-3629-aefc-ad68d9881d28 | -7.04526 | -43.21942 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aec47714-723e-3c30-9245-19790be51f6f | -5.48423 | -42.7976 | 2025-10-04 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ec8b31ea-7156-3aad-92bb-6e394ee6ab39 | -6.28795 | -39.61211 | 2025-10-04 03:51:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe951772-9339-39a9-9ab1-0e6c0256863f | -5.63436 | -43.2237 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4bd7100-6bd3-35fb-806d-7344a578de28 | -7.04556 | -42.7709 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8e9c574-1630-349b-8ef5-bc56a12b800c | -7.78013 | -42.59352 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d3a2ec82-956a-338e-bef2-d0428090af91 | -6.6697 | -42.81636 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8b69b78b-802c-31a7-b1e6-b65e6ead287b | -11.47568 | -45.03161 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49448bbb-aead-32f1-9ff8-57dfd37b6c01 | -6.69704 | -42.83736 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe578777-cef9-3bc4-aa0d-ff64abab157d | -4.71217 | -46.13049 | 2025-10-04 03:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43a91950-9377-3f0d-b61d-805870c04c65 | -10.32711 | -50.34241 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 84dc2617-4a97-361b-93a6-db4df0fa94f9 | -9.93673 | -50.2379 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dfb593e-3c38-3b14-a769-660acd48bca2 | -4.48532 | -42.86379 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7f43d1ac-d325-3584-9ec1-46cf16a6b894 | -9.12075 | -44.3844 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee7f385b-cea0-34bd-994f-29f6f35ca0de | -5.01634 | -43.65789 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8357d2d0-d357-3421-8598-467861c2c1de | -7.31389 | -42.89198 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d671bf97-b906-3d8c-aa42-69484ac382d4 | -6.45883 | -44.58078 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 85be0130-3814-3269-b937-25e6dbe7a312 | -11.45364 | -45.14459 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63e6d8b8-d28a-3f25-b0be-75331c000119 | -7.78501 | -44.13691 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae9cfe4c-0d00-3084-b692-b73b1d2c7ad3 | -5.66471 | -42.71574 | 2025-10-04 03:51:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |


[Clique aqui para ver as próximas entradas](README27.md)
