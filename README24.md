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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccfffb46-0a64-345e-8faa-a18a341b08d4 | -7.31043 | -42.46911 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 636e347e-e6ea-307f-8bf2-c9e1e832593b | -5.19609 | -42.90997 | 2025-10-19 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e169558-774e-31ee-8c1d-3547c77b8457 | -7.58478 | -40.94831 | 2025-10-19 04:10:00 | NPP-375D | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f09b3876-7fa0-3ff9-8d78-c255ecc3864a | -5.16427 | -42.91236 | 2025-10-19 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edb1c2f6-3a17-321a-a8bc-89b8c6ad5c9a | -4.33702 | -43.60656 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ac43c9a-7efd-3561-ad85-d39e0acbc9e7 | -2.68966 | -49.54539 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 89c19dc8-eccb-38d1-9a8e-222334e5a78e | -4.24256 | -43.10173 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb2a1663-baa7-38a2-a34f-f3740f926828 | -4.22179 | -50.62937 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4e0b254-9aef-3e19-b3a8-2ec87ccffd72 | -6.25316 | -47.30585 | 2025-10-19 04:10:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2da1f53-0133-3908-a7bf-06c83f5e9012 | -4.12406 | -42.18813 | 2025-10-19 04:10:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d1fa0016-c90f-3194-ab51-63f6b0eb2c8d | -4.27041 | -48.87782 | 2025-10-19 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c7bdb73-9db9-3923-a58b-a438c0e39f15 | -3.80015 | -51.94461 | 2025-10-19 04:10:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ef85cd7-5217-354d-9a83-40f1aa42d3de | -5.17712 | -45.2739 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae15874b-e68b-31d8-b279-f048f5eb9cc9 | -6.96655 | -39.64449 | 2025-10-19 04:10:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5a5c3e3-9a9b-33fa-8de8-affcb6eed995 | -6.32787 | -45.04233 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61799759-5cd9-3145-b669-c9513952b84c | -3.03666 | -47.81143 | 2025-10-19 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e805c4a5-358e-3a1a-ac00-448db754d12c | -2.90736 | -40.40754 | 2025-10-19 04:10:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5cf15d16-3ab1-3d0f-b710-81293d9c2e11 | -3.59178 | -42.83278 | 2025-10-19 04:10:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88fe1464-2baa-391f-be86-a2aa6875435b | -3.39869 | -54.06509 | 2025-10-19 04:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7df9646-9565-377f-b288-fee967f557dd | -4.95927 | -45.0928 | 2025-10-19 04:10:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46474f45-4ff9-36c0-96ac-30494e1b87d9 | -4.77323 | -46.88731 | 2025-10-19 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eb3d004-36d6-353c-ae19-8a04cfbdbcf4 | -7.17998 | -42.52044 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e7bd542-ca0c-397d-bebe-13a70eab46c8 | -4.85632 | -44.59539 | 2025-10-19 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 232d491a-4a67-3743-b7ba-6a784d2f5065 | -6.99487 | -44.87173 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0358db55-d8d0-34b6-998a-aeb661d08c13 | -6.56114 | -45.94739 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1468adf4-7d41-3e8d-b1b9-a968465c1396 | -3.21985 | -50.21693 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b01580c-efe0-3a0f-ad30-8232f5f1c632 | -7.15659 | -42.37597 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94966765-4da5-32fd-a235-4856ee48a72d | -3.89026 | -52.41021 | 2025-10-19 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ee0d5ff-504f-3975-b6d8-6582f74bc43a | -4.22786 | -50.627 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8307bc13-2603-39a3-8fec-3fed3e473e9e | -5.8579 | -43.18222 | 2025-10-19 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f5f1df5-aba2-3898-8f14-4a2c31f8bbfe | -4.44242 | -43.22468 | 2025-10-19 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84d62c54-196b-3965-a5ec-e08c0de55631 | -7.40943 | -44.80008 | 2025-10-19 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 341c2b07-e8ce-3aca-8f06-9c8a2a46f6ab | -5.55686 | -44.9524 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89051b9c-6947-39e3-8764-9c1ceadf4125 | -6.76334 | -41.43927 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 24d8dc66-a3aa-3a03-8e8b-0697c62615c5 | -3.03953 | -51.21328 | 2025-10-19 04:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e35fd96e-456f-3953-af8e-0e485cf0b39f | -2.2573 | -51.91088 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1d4770d-211b-360e-ae53-634884af591e | -4.14492 | -38.23935 | 2025-10-19 04:10:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b20f12f8-3445-33f6-86e9-1aa81310dc67 | -6.33423 | -43.28379 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00773d13-f96f-3e7c-b1f2-834d01e31089 | -4.82949 | -43.01797 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f1e307b-b97d-3291-9bf2-18c19b6b9261 | -7.02231 | -46.80117 | 2025-10-19 04:10:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bdbd9ad-d72b-3b0e-804b-c2d4053148b2 | -5.06802 | -40.47736 | 2025-10-19 04:10:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 692d06f3-1488-331a-b7ba-5b326734b748 | -5.53354 | -46.98989 | 2025-10-19 04:10:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a750c6a8-41c7-3581-b49b-3528507543a4 | -3.55199 | -46.43767 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83263cf8-9992-396d-971c-64842170d38d | -5.3257 | -45.78901 | 2025-10-19 04:10:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3256e42-6a8b-3480-8048-f3df1e4ea0a3 | -4.41564 | -43.97252 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95d83f85-68f2-38b5-af0f-1f07443b1418 | -7.18569 | -39.67086 | 2025-10-19 04:10:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cbf59859-46ce-3258-8b0c-f095a45c54b0 | -7.74323 | -42.51338 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f32c731-b03d-3de9-aad3-6682a372e3b6 | -3.86095 | -49.82114 | 2025-10-19 04:10:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3814dd61-8b04-3366-99d8-32dbd9a1f92b | -7.27582 | -42.30557 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ced45419-5f09-3a7e-ac95-bb3f6e3fd506 | -4.81937 | -38.65815 | 2025-10-19 04:10:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| afbfed71-21f0-3fa3-8dd2-2b90d6e1a14f | -2.70343 | -49.85979 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad822b3-d8b7-3465-98d8-54fc9c85f5c1 | -5.54437 | -41.33981 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9020681d-7105-3577-947b-7451885699b5 | -4.24969 | -48.56919 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbf06d9e-c269-3970-b28d-a9b7fe61b60d | -7.36878 | -41.9523 | 2025-10-19 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4858e42d-d1d3-3f92-b939-0d36430971a2 | -5.10296 | -47.79251 | 2025-10-19 04:10:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e66be03a-8947-30eb-af3f-42fc8f5fb242 | -4.96624 | -45.91008 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 57da15b9-6a6c-352f-bbd7-970ed3b994de | -6.76667 | -41.43979 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 75fae1ab-adad-3e82-9209-9f89e3476997 | -7.16049 | -42.37299 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5ca3366a-99a9-34c7-95ed-cf16cfe1de98 | -3.09109 | -49.22425 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac0b6834-1188-3281-9e97-635a3d8b9040 | -5.93244 | -42.23888 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2773622f-58af-35a4-bf77-86a2e0f4a087 | -5.04244 | -44.35159 | 2025-10-19 04:10:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2988f981-84a9-380f-9261-14d478670f1e | -4.22239 | -50.6259 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6bd7d99-9706-377a-afd3-3bbfc431c2df | -4.48735 | -50.55989 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0de98980-d557-367d-a30c-4b54dbd6019b | -6.59367 | -45.87622 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea16d2c0-5f56-39c2-94e6-60b42565b1af | -5.45869 | -43.29849 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a46fe8cf-874a-37fe-85c3-c9169d68bcad | -5.93076 | -42.24941 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f470da67-2b9b-3ca4-b8b0-85c1faf897cb | -6.37566 | -45.75973 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 922845d4-e69b-3381-849e-1a9e27cd4a86 | -5.36611 | -44.94577 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21c66ad3-44b6-3d58-a5c1-19fde762ad7a | -4.23322 | -44.68627 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69379c54-e4b4-362f-81c2-9f08d63071d0 | -4.91412 | -45.4185 | 2025-10-19 04:10:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d878548-8fc5-3361-ad6e-963365eca4a5 | -6.56749 | -44.42752 | 2025-10-19 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3482e8c6-1ae6-3000-bd20-cd8d00cf1a09 | -6.14637 | -44.288 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cc1aa65-d220-3d07-982f-3d16d84fdc07 | -7.76883 | -42.4815 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 970086b4-c978-3812-a000-ec3867101079 | -5.92844 | -45.44585 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5509b30e-a0e3-350c-ad96-427f496409c7 | -5.30333 | -45.32379 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3c29a97-b0d3-30d4-aec4-2a9041987ca7 | -5.60284 | -42.68068 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 916bc8b4-c7aa-336f-a6ce-ba4b507771e2 | -5.37173 | -42.81798 | 2025-10-19 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed23c7f1-2877-38c0-8c8b-3250426db273 | -5.99419 | -42.79016 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4fe47ce3-68ea-3021-8dc2-5d409194a28c | -5.58144 | -41.3208 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac61880b-fc7a-3f56-859f-17fc3512b3a9 | -6.12772 | -44.22385 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08a1583d-9051-33f4-b03e-5c68e465cdee | -6.14994 | -44.28851 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e30b4852-980c-397a-9e0b-bfe1c80193a4 | -4.00643 | -46.24326 | 2025-10-19 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15fb8784-f325-332d-8278-84164ae62d6d | -5.72026 | -49.09575 | 2025-10-19 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecbde79a-a4c7-397b-b2ae-168350d81508 | -6.72792 | -46.3209 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5cf19e80-1c17-37fa-98fa-10840dffa732 | -7.15993 | -42.3765 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbcebb30-5d7e-3f23-b720-97d319a20284 | -3.3555 | -45.45248 | 2025-10-19 04:10:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 221936fd-fc0a-3f4b-bde6-f76a17b16255 | -5.77731 | -42.72688 | 2025-10-19 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01e060bd-bf70-337a-a15e-251893118e54 | -2.70346 | -49.87302 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab03391e-bb9b-335a-ade7-c48f8782b6f3 | -2.74219 | -49.38965 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8db57a0-a8bf-31c5-bb22-871cdd716ff9 | -7.09445 | -42.20824 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d71614e-bcf7-3385-b40e-084446783e57 | -5.34739 | -42.55641 | 2025-10-19 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 339ba7ff-949f-3c52-8efe-43d048403d91 | -6.89664 | -39.74254 | 2025-10-19 04:10:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8813434e-83b9-3b28-bb7b-f3cb137fca9d | -7.31321 | -42.47316 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ac555f0c-9220-3141-8c1d-6c0c1e26d57b | -6.1255 | -44.21521 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4bd58c2-96a5-3e39-ba4b-5c68671bdb64 | -3.97061 | -47.57887 | 2025-10-19 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2f994b0-593b-3ecc-9434-b7d76d775f05 | -4.05036 | -43.21495 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad8642f8-4fa7-3552-abe7-4d97b16f3b74 | -5.04176 | -44.35574 | 2025-10-19 04:10:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8beb131-bb98-3b49-a63b-cac18fa52724 | -5.21359 | -43.7444 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2374ee01-3fff-3e55-ad1c-5664e85725f9 | -5.77451 | -42.72275 | 2025-10-19 04:10:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c479d823-fddb-3a06-8e5b-f68151cbcc30 | -4.53439 | -44.01091 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
