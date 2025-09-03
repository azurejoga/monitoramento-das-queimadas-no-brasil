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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 790f43f2-bd05-354e-aac4-ca487057d929 | -6.97797 | -43.27996 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 52e6906f-67b2-3b51-97aa-97f583d22f34 | -7.50188 | -45.33462 | 2025-09-03 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 352f6a8e-1bb9-37fc-9574-f935eb0c4517 | -5.80854 | -43.22166 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a89ae869-1738-314d-b57e-9a190d8fa097 | -9.63619 | -47.04016 | 2025-09-03 03:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 492f66bd-faf0-397b-9e83-a7db5eee4ab1 | -5.95536 | -44.28127 | 2025-09-03 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41ab1117-e582-340f-bcf7-af8101750110 | -6.25706 | -42.59467 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 735114bb-5808-3fb4-b329-cbdca0aa13af | -5.80234 | -43.22064 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9b42790a-8e8f-31c2-88ab-28bf6f1a9700 | -8.87703 | -45.82461 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b18b43bb-ec51-32fd-b2de-0f1f55969d36 | -6.24422 | -42.6132 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ca0efc59-a7ad-396f-81d7-6fd456fa0804 | -7.92463 | -44.94269 | 2025-09-03 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21de7289-5c07-3f6e-8c20-92cc549877aa | -6.73166 | -42.25008 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eddfb530-a783-3bb6-98e1-4466f55bde8d | -3.82021 | -41.06468 | 2025-09-03 03:32:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24567745-0765-3893-a9ad-64c22801a7c1 | -7.49234 | -44.82243 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2ee66c7-f16e-3d01-8271-5da5b0212250 | -6.36143 | -45.65805 | 2025-09-03 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa71dc17-803d-3586-aa03-c886ff7e1f64 | -8.05065 | -45.36304 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a59a571-12f1-3c67-a8dc-84a21a4fda4f | -5.96085 | -44.2765 | 2025-09-03 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e621a2b-8e16-3994-aa0a-d5f31b4388c5 | -6.97933 | -44.36184 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbfadac1-74ec-31d4-8377-278d5d9b6ae9 | -5.80169 | -43.22955 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ffa5846-a8f8-368d-9736-61fabba00484 | -6.98948 | -43.11181 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b89b6e3e-1626-3696-bdf5-3b7f72292a68 | -7.5074 | -45.34278 | 2025-09-03 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe03a5c3-ac2c-3b66-b7c2-cdfffe0c64bd | -7.79899 | -45.45564 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2fdb4857-34c0-3a5a-9ea9-b3f59e3a0f30 | -6.72907 | -42.26025 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7f0b2bea-2deb-3d2f-82cd-007fa4726f6a | -6.98425 | -43.10629 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fd05296-9dfa-3aaa-8caf-40f5a592a013 | -5.8087 | -43.226 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e7489a9d-6655-36fe-843d-0282ed5f5768 | -7.00893 | -43.2474 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfa7c316-317c-3fc8-815d-16a859793205 | -5.61116 | -45.00906 | 2025-09-03 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8f5e1b4-48ec-30be-ac48-60f7550a1f4a | -6.70274 | -44.19244 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67f153f8-e86d-395a-a149-93644ef0cb63 | -6.73038 | -42.25735 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ed1b205-2ed8-38c5-b080-e649038d1fcf | -4.90695 | -43.19131 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd0c72d0-5b43-30f7-b377-4cae545ad650 | -6.36013 | -45.66492 | 2025-09-03 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5438e734-ebd3-3647-8f18-50896d559d79 | -5.9387 | -43.02746 | 2025-09-03 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f17a444-834b-3c19-9a0d-ae7ff54ec5db | -5.79551 | -43.22841 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c490bfcb-de17-3b31-954c-f86c4504d0d0 | -5.80249 | -43.22503 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6167da38-2556-392e-9e93-e96661b015bc | -6.71013 | -44.18858 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b407b285-9d86-3079-9430-531882ae93d1 | -7.00038 | -43.26017 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2501410-c42c-3763-9cce-90cc6e016967 | -9.61699 | -40.61691 | 2025-09-03 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c6f3bb28-f065-33a4-a674-8bdab9f44c32 | -4.45108 | -38.44615 | 2025-09-03 03:32:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4997831e-ddfc-33a4-9a6e-bacda6c75563 | -6.24347 | -42.61752 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37fa1d3a-3b2c-38a7-aba7-cebd69cbc8f3 | -6.70905 | -44.19454 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5d406fa-86b6-3790-afe8-0f5f9c7b9843 | -7.13258 | -44.57536 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e48cd65a-9a33-316d-bde9-dff3dcc1e77f | -6.97527 | -43.27785 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8145fb1d-c1c6-34bc-92a9-a55e485e2f1e | -5.81651 | -43.21796 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 788880dc-96d5-34fe-9d16-a8be9e5cc650 | -7.11349 | -44.7518 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81dc8b21-f896-38f8-8019-8750d76e9e03 | -8.87098 | -45.8237 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3ec2f36-1087-3a23-8527-d4ad81b6dc71 | -5.69554 | -45.94033 | 2025-09-03 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12c9b4f8-b985-3d1e-be77-91ef76bf6eca | -4.90341 | -43.21129 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 90ca1725-938f-32c6-ba29-8b80ed309de9 | -9.19647 | -45.19919 | 2025-09-03 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80c0739a-30aa-3b7c-8eba-e75e3afef7b6 | -6.99955 | -43.26483 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8eaf993e-8eb1-3fb5-9479-94dc191a7278 | -6.70006 | -44.18958 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5ab7a7a-5d14-38ec-ba57-1e6761152d22 | -6.1943 | -43.35303 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f4aabe44-782d-3366-b09b-964271d92a91 | -6.69722 | -44.18605 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b8a1716-6349-315c-be52-1552b8aab049 | -6.27286 | -44.51023 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| acc426cd-57f1-33ae-8f84-c207a13525b3 | -6.47027 | -45.42538 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a5d95da3-8830-3655-ae65-f6576cf244c4 | -5.95984 | -44.28195 | 2025-09-03 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28ff798b-4dca-3fb8-9041-94469c482b7a | -5.50312 | -42.63123 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6776cdf6-1d28-355c-9625-ee1e45c9cfca | -6.47728 | -45.42644 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 43441d8b-a4c5-3c90-9006-597ca34bb52c | -6.21926 | -43.39614 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa369401-6d87-380b-80e8-8d789ccd8015 | -6.97714 | -43.28459 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dec33d6e-6b15-3dcc-bf41-1703560df504 | -8.01549 | -44.11248 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43709e0f-53d3-3def-a938-40ce69cc2300 | -6.45733 | -44.68936 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a071774-4105-30e8-9423-ccdc8bc92c59 | -6.4641 | -44.69016 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a742fa-4c1f-305d-b7f6-3ec191204564 | -6.72981 | -42.25622 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9151ad8b-aa0f-3be3-b12c-1ba25a72f40e | -7.48132 | -44.80819 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b05ccef-62dc-3b2f-a87c-55506635c106 | -7.92901 | -46.5433 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1fc4869-336a-3f8a-8034-bf1fd67ecaef | -6.19688 | -43.3392 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6daf8952-d9f6-32f4-b002-e76f1f95cff6 | -7.93506 | -46.55596 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c81f0429-be38-36be-afdd-00f9a89cae85 | -6.23606 | -42.6249 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9aeb64c5-a9ad-35ac-91a5-fd7ab9d11b38 | -6.99613 | -43.26724 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 086bd1b1-ddc5-3e0d-a778-1bc97153158a | -5.70936 | -43.10577 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09cfd214-4d90-3589-a213-f6c0db86e129 | -6.22799 | -43.37869 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 762e7f89-60fb-3da3-a705-39fe74669982 | -6.72534 | -42.25237 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4fe130ec-22a8-38f9-8f62-083c7bf5ba6f | -6.37311 | -37.37594 | 2025-09-03 03:32:00 | NPP-375D | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 285228e1-a003-3097-878e-cb81724e4a07 | -7.11465 | -44.31146 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23d56e4c-4009-3ad6-bb6b-2572140d2fa3 | -7.11239 | -44.75771 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0ddab79-8eda-301c-ad85-421c5ccb9cb1 | -5.60449 | -45.01607 | 2025-09-03 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e306eeec-c147-3b34-b8e1-e2f4eb7bdd3f | -6.40482 | -43.7556 | 2025-09-03 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 263fca89-31aa-364f-8d6c-4b59faaead5d | -6.22893 | -43.37769 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a27800f-00ed-3420-bb8e-99a1c32d93b3 | -5.52997 | -36.84732 | 2025-09-03 03:32:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| cceb20d3-563f-3468-b449-3dcb79f26e53 | -7.11901 | -44.75912 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71eafdd7-35ed-3cc4-8b1e-a64a6fba70ad | -5.44187 | -42.90064 | 2025-09-03 03:32:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 46ed5295-57b5-3785-9c95-fa1eb2fbbda6 | -7.93625 | -46.54478 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b247bb98-56d9-3bd4-8827-bebbfec9f879 | -5.81558 | -43.2181 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 24411df4-44a1-32a6-a329-f6f8290977fe | -6.23146 | -43.39473 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b30cd463-4e5d-31f2-8484-18982c98fb6e | -5.53283 | -36.85517 | 2025-09-03 03:32:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c324bf1c-44cd-3065-8cad-c2137605c4b4 | -9.16428 | -45.20797 | 2025-09-03 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6a0527-3c1f-3755-9d66-e7e5121b12d3 | -5.49706 | -42.63053 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f85cfccd-dc91-3be4-adaa-68763fc554b3 | -4.89806 | -43.205 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3674fa2-88c6-36bc-8ca6-3f106315f0a2 | -8.05613 | -45.37117 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7074e35d-4310-3a27-b259-0a773ffb41e2 | -6.72596 | -42.24889 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2084af9e-0571-3c32-97ae-b9c1c7d797e6 | -5.4415 | -42.90383 | 2025-09-03 03:32:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d3987ef8-b1eb-3811-945e-364389865fd5 | -6.25244 | -42.60115 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1c35845-191d-3b3d-94d9-e86ce2c7add7 | -8.05829 | -45.36404 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b014c001-5a29-3251-9eb5-57e0b261c924 | -6.79652 | -44.10111 | 2025-09-03 03:32:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e12920f8-4925-35cd-a8a6-08e6b6da216e | -8.88376 | -45.82663 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 921aac3d-610c-300a-935c-d392e54fb7d1 | -5.79535 | -43.22391 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91581f97-1e05-3d44-b938-699d9ffc129a | -5.60307 | -45.0142 | 2025-09-03 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f528e025-bd7d-3303-a30b-570ccc479158 | -6.22275 | -43.37646 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abafa9ef-b077-3684-8983-95cd155cb1a5 | -6.78597 | -44.49132 | 2025-09-03 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43db004f-d9ee-37e1-ad49-e5e411e8b6bf | -6.12209 | -44.13423 | 2025-09-03 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 984d1df4-243f-37fe-b249-5594d5579027 | -6.1976 | -43.33803 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README22.md)
