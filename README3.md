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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa8b9744-e035-3285-81bd-a5d3e7b648a1 | -2.2775 | -46.1605 | 2024-11-28 00:03:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82e8109a-f467-3e72-8f91-50edf04883d2 | -8.4532 | -43.278702 | 2024-11-28 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 750af4c1-444d-3563-9da2-6e7023551fbc | -2.4917 | -45.976101 | 2024-11-28 00:03:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d031ced-b1ec-3330-b00c-2ef692a158d1 | -3.4972 | -44.3881 | 2024-11-28 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a6fb755-342f-3123-b9c1-8cfd55f40d99 | -3.613 | -45.7784 | 2024-11-28 00:03:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21f3c533-1da3-3426-a9b1-f4ad332f1a1a | -2.8071 | -46.834801 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 497372aa-a83e-39b4-957f-0154d557dbfe | -6.0452 | -43.962898 | 2024-11-28 00:03:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 339ef898-8732-352b-a911-1715ebdf2baf | -3.6619 | -43.4286 | 2024-11-28 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0df52247-0e5a-3f43-810e-d18a9e5965f0 | -9.5268 | -36.160599 | 2024-11-28 00:03:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 554b92c9-9cf9-3674-962e-f8c40b3f3e48 | -3.6424 | -43.432899 | 2024-11-28 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b77eebdd-4ac9-300f-bdfc-33cffe874996 | -7.2103 | -39.759701 | 2024-11-28 00:03:00 | METOP-C | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bda5cd19-6c05-389a-b83e-d1e2bfa7cbe6 | -3.5737 | -42.396099 | 2024-11-28 00:03:00 | METOP-C | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d479a4e5-8d61-34f6-a810-9a5b183c718e | -3.5083 | -43.430199 | 2024-11-28 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecd51eb7-6ada-3ef1-b9c7-ba6e75d86f64 | -8.4575 | -35.116402 | 2024-11-28 00:03:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bcc42507-c862-3209-8a02-fdd391f58d31 | -5.3417 | -40.6521 | 2024-11-28 00:03:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f3925ff-0efc-328e-ba01-5f30fed02521 | -2.2304 | -47.084301 | 2024-11-28 00:03:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b4c1d0-fba0-3cd3-9b9c-4989774604f8 | -7.6543 | -42.987499 | 2024-11-28 00:03:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e12068fc-4bb6-3e98-b0a2-00eb25ece939 | -4.7489 | -44.443401 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7623da2f-12d1-329d-94a6-b54541c69a95 | -6.8563 | -42.474602 | 2024-11-28 00:03:00 | METOP-C | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5a18b21c-d503-3d61-8e59-eb9ed27ccbcf | -6.1253 | -42.601299 | 2024-11-28 00:03:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b766205-4f05-32d5-9a41-4f60a8fe058f | -3.6401 | -43.422699 | 2024-11-28 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43f23640-9879-3ca2-b9d7-6960de989059 | -4.4875 | -44.603401 | 2024-11-28 00:03:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ddfa4d8-8b7b-3cc8-8712-1dfc103562b4 | -3.6098 | -45.763802 | 2024-11-28 00:03:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7be81afe-a799-39e2-899e-725836fd0060 | -3.274 | -45.496201 | 2024-11-28 00:03:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ebcc61ac-a70e-322a-a9f0-7e7edf0ef0eb | -6.78 | -44.381401 | 2024-11-28 00:03:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e7f697a-b4ae-352b-b44c-fa720853fae2 | -9.067 | -35.3815 | 2024-11-28 00:03:00 | METOP-C | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85d6147e-9ee8-36f0-bab4-f04f207abae3 | -8.973 | -36.131699 | 2024-11-28 00:03:00 | METOP-C | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 604278de-43ed-34d7-a4ab-b9c954e724a2 | -4.6094 | -42.385899 | 2024-11-28 00:03:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 58e2e907-c3eb-38f5-9fe6-3ccb078b2887 | -5.9367 | -39.045399 | 2024-11-28 00:03:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 38fcbe0e-dd43-3725-be6e-e58f5a732f2a | -3.2767 | -44.044601 | 2024-11-28 00:03:00 | METOP-C | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0fbbb94-06ec-3f0c-93d3-a0f44f91c25e | -9.8223 | -36.233601 | 2024-11-28 00:03:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 340afb2d-7ade-3e74-b5dc-f99ec8bfbe19 | -10.05 | -36.505501 | 2024-11-28 00:03:00 | METOP-C | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5fdee76e-6b96-316e-a3d5-f40a84e7952a | -4.6192 | -42.383701 | 2024-11-28 00:03:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 763c6fef-0a46-3e5c-a6cc-044976158af7 | -3.2709 | -45.482498 | 2024-11-28 00:03:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7c420a0-b6cf-3dad-abb0-783b5e889cef | -10.1025 | -36.419899 | 2024-11-28 00:03:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| f89ab381-d924-38b2-8241-4cdb96cd432d | -9.6117 | -36.126099 | 2024-11-28 00:03:00 | METOP-C | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 81cc7dfb-fcea-3886-afcd-c80338a41bb9 | -9.9768 | -36.4562 | 2024-11-28 00:03:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7f2c21b-a219-39f9-87b7-d7f099c7e5b0 | -9.6133 | -36.133202 | 2024-11-28 00:03:00 | METOP-C | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17501f25-c09e-351e-90b1-4c6a9e9f3cb0 | -3.4946 | -44.3764 | 2024-11-28 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dccd5a86-5688-34f5-940f-d4e0a9d22cac | -4.7364 | -44.4333 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20c233d8-85ad-3632-a6aa-6e24fbb327ee | -6.0391 | -41.9328 | 2024-11-28 00:03:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b9b321a-e638-31f2-950d-b13c38f67262 | -2.8353 | -45.3652 | 2024-11-28 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a43ba0d-69bc-36ec-b3df-3b78861d96ee | -2.4646 | -45.174198 | 2024-11-28 00:03:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13a7686b-4c47-3c86-9155-ad3319c84d11 | -10.1009 | -36.412899 | 2024-11-28 00:03:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| d20c10e4-0736-3379-a033-13f9888e4f4a | -4.4903 | -44.615898 | 2024-11-28 00:03:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4952c798-6e60-3d5a-86c1-152147ac089a | -3.6499 | -43.420502 | 2024-11-28 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 051103fe-10de-3d51-9327-0f15b12392a8 | -4.6152 | -42.365601 | 2024-11-28 00:03:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6bdf590-726f-3c43-b69f-94aa61a13712 | -6.0425 | -43.950901 | 2024-11-28 00:03:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd5283d3-ad80-3105-a519-9943c5c44a3e | -5.9401 | -45.358002 | 2024-11-28 00:03:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 778b49ff-455f-32c7-9f7d-f8cdcf0bcf40 | -3.3538 | -50.111599 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d178518-098d-374d-8669-ad51b421e902 | -2.5745 | -45.298199 | 2024-11-28 00:03:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c10a496-b6e1-31da-92e1-5f110174590a | -4.0833 | -46.102798 | 2024-11-28 00:03:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc8c5c0-ca24-352c-a1ce-82b1e5dfeb71 | -1.999 | -47.099201 | 2024-11-28 00:03:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dacc297a-efa0-3fe6-b980-efdb28d9657d | -4.7462 | -44.431099 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1105496-da49-3c5a-afc3-501535edf580 | -3.6163 | -45.7929 | 2024-11-28 00:03:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fda79c38-5099-36a3-88b2-e89f986d4a8f | -5.9369 | -45.343201 | 2024-11-28 00:03:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0042fbc-d3a9-39cd-ac7a-bd3e15d648f3 | -10.1042 | -36.4268 | 2024-11-28 00:03:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 8a27ed7e-0631-35c3-86fb-8b75dc4ee180 | -6.0478 | -43.9748 | 2024-11-28 00:03:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee346319-cc80-3bfc-ba4a-c05d06cb5ba6 | -4.7088 | -44.400799 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 969aae66-1aa6-30bf-a728-d98184b6e466 | -5.1423 | -44.231499 | 2024-11-28 00:03:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0579aa-2c9c-32f0-aff8-d76efa9b1dbf | -10.4471 | -36.889 | 2024-11-28 00:03:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c3749ad-9550-3796-9abf-ac5e75350570 | -3.3189 | -44.186901 | 2024-11-28 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 955ff137-b09d-3b8c-98e0-424667148e5b | -3.1499 | -46.587502 | 2024-11-28 00:03:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15b92fef-4c69-3ffe-b7a2-135458b7e985 | -8.8465 | -35.942299 | 2024-11-28 00:03:00 | METOP-C | SÃO BENEDITO DO SUL | PERNAMBUCO | Brasil | 2612901 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98db69d9-b1bf-36d9-b009-ff6e4a609059 | -7.4745 | -35.108002 | 2024-11-28 00:03:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5ec918d-7943-36f1-abdf-6fe8549559df | -3.6227 | -45.776299 | 2024-11-28 00:03:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f38a520-85b4-3b72-ade4-57c81612ae9f | -6.6182 | -34.979099 | 2024-11-28 00:03:00 | METOP-C | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10d19a9e-7ec6-33ab-8102-a7de0dee6861 | -2.4548 | -45.1763 | 2024-11-28 00:03:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c64702c4-e5c8-3d94-be9a-59fe8ae20b70 | -4.62 | -44.601002 | 2024-11-28 00:03:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de6995a4-291a-3be2-82e8-57c15ab58657 | -6.145 | -44.421101 | 2024-11-28 00:03:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54468284-60c7-3ccc-8cac-09c0832cc421 | -9.793 | -36.195801 | 2024-11-28 00:03:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64a44713-6a08-3df2-b70d-f11d446a922c | -3.5835 | -42.393902 | 2024-11-28 00:03:00 | METOP-C | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9348f212-bb99-3bb4-9978-21dc594573f1 | -3.172 | -45.634602 | 2024-11-28 00:03:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a56c04a-c71f-3413-9b89-a17b207d9fdf | -4.6228 | -44.613602 | 2024-11-28 00:03:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28cb8bb4-4bbf-3f9b-805f-26bee019c835 | -6.0576 | -43.972698 | 2024-11-28 00:03:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f38d5e5-de38-3a8d-bddb-6680aa5363a7 | -3.3217 | -50.058102 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 705c1f34-8c7e-310d-bbe0-4e3f08db594f | -6.0705 | -46.576199 | 2024-11-28 00:03:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9ca534e-139d-3621-a7b0-ae3ed1356ff3 | -5.1631 | -41.277 | 2024-11-28 00:03:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8262f144-3a0e-384d-b8c8-1189fe75ab7f | -4.6172 | -42.374599 | 2024-11-28 00:03:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 10d58121-4f84-384e-88bf-3ef2aaf52ea6 | -5.9272 | -45.345299 | 2024-11-28 00:03:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce760b0-e5cc-3fd2-8fd8-2849c5a58e7f | -6.0431 | -41.950802 | 2024-11-28 00:03:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f27e1388-3db6-313d-bd8d-e78e90f3dfa1 | -6.0509 | -41.939602 | 2024-11-28 00:03:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 351695ff-db46-30c8-9053-ab85a45503d3 | -2.5774 | -45.311199 | 2024-11-28 00:03:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9b2793-70cf-390c-a42e-cdef8d3073e8 | -6.8768 | -38.146999 | 2024-11-28 00:03:00 | METOP-C | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 4bdeef6c-53ba-3e50-b254-f3d74e234680 | -3.2838 | -45.493999 | 2024-11-28 00:03:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 358ab73a-01e3-3164-a324-a1d72d24aa8f | -2.4238 | -45.8563 | 2024-11-28 00:03:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb6f4b6-9cd9-36a4-8a99-f5e3598ce696 | -2.0952 | -46.0779 | 2024-11-28 00:03:00 | METOP-C | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc4109e1-1775-3fcb-8903-af098d14239d | -4.0959 | -43.809101 | 2024-11-28 00:03:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3badd44-39cf-39ea-aa5f-83cc5a38def2 | -6.7702 | -44.3834 | 2024-11-28 00:03:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f39e563-00aa-3533-81f7-0a4460c80eda | -8.9747 | -36.138802 | 2024-11-28 00:03:00 | METOP-C | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9aebd1e-6937-33cc-9306-94f9438e22f8 | -1.9073 | -46.558498 | 2024-11-28 00:03:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad4a971c-4b58-393d-8bb8-66e8850b22b1 | -9.6101 | -36.118999 | 2024-11-28 00:03:00 | METOP-C | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef6f79b0-baa3-339a-9725-c60d5389b205 | -3.4419 | -44.598598 | 2024-11-28 00:03:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b88d74f-09de-3abe-8162-f548287221aa | -3.6596 | -43.4184 | 2024-11-28 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fceb5550-3ddc-39d2-acf4-509fd61dd6f9 | -6.5417 | -44.177399 | 2024-11-28 00:03:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78d3eb20-97dd-33ed-843b-95812033586f | -6.1352 | -44.423199 | 2024-11-28 00:03:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 735e249e-569c-39bb-aabd-b294c8c6079f | -8.396 | -35.073799 | 2024-11-28 00:03:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 65c514f3-6a9a-3498-adcb-2b99bd063514 | -4.7115 | -44.412998 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4678cbb-df18-3fb9-82c8-102a55a01885 | -6.1275 | -42.611099 | 2024-11-28 00:03:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84f07da3-4e2d-3707-acd3-2cd47252865e | -4.0934 | -43.798199 | 2024-11-28 00:03:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
