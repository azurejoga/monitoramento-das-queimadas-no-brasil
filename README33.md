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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2649fc1-2eb8-3f7b-a118-f0eb8b1450af | -15.5613 | -44.522202 | 2026-10-09 00:28:00 | METOP-C | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 771a0440-78cd-39cf-916d-593b598bb459 | -0.6454 | -52.524399 | 2026-10-09 00:28:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f426914d-cec7-335d-bce4-956fcf4c49da | -10.4119 | -47.286598 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 563dec5d-60f0-32a7-94d5-9d04fc54c79d | -6.9059 | -45.885799 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdc8f8a4-11dc-385a-a453-e7e2a39a0cfa | -3.699 | -47.687199 | 2026-10-09 00:28:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b69b9ee6-995e-31d1-8b63-b42399715fd6 | -7.1921 | -55.138199 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fdeb17a-cd06-319f-98d0-a9f4c310d989 | -2.3541 | -48.883099 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfe52431-2c7c-3747-8483-2b480480a15b | -4.1305 | -46.8689 | 2026-10-09 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2be7113b-e13e-38be-af58-c5f35268a1c2 | -9.6072 | -42.143002 | 2026-10-09 00:28:00 | METOP-C | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3491622e-f0cb-38e5-86ad-c949971bf816 | -11.8627 | -43.572601 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c365468-d5cc-328e-8370-a7a56991e7a7 | -7.1852 | -44.275902 | 2026-10-09 00:28:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 63f1483e-1a73-3c8c-8942-76e96cb53dcf | -9.2859 | -47.4464 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95b21379-9d19-3fa1-8565-7a3b09f71ca5 | -5.1035 | -42.6563 | 2026-10-09 00:28:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32d0b992-cb91-36dd-af9a-386da5408219 | -9.8973 | -44.8083 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c1ca5c6-9c6a-3a1c-9210-5ea8fb441432 | -6.1526 | -47.924702 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fc7935f-14ee-3763-8cdf-98233dedd255 | -11.1778 | -45.319 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26e620eb-b8e2-3939-ae65-3a1c27d10baa | -7.4577 | -42.8358 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 14bd2b00-1608-31bb-997d-13a64f4b30ca | -6.156 | -47.939602 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 949e0ae7-b332-3e6b-b7eb-ce925edd45a7 | -9.0156 | -44.382099 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2ded70a8-b90b-3e32-8d5f-fe5e935569ca | -10.7769 | -46.611698 | 2026-10-09 00:28:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b33ac3c6-5522-3af3-8492-55f7b1ff95fe | -8.2141 | -46.839001 | 2026-10-09 00:28:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 188094c2-05b6-374f-99c5-58a8908baea8 | -9.2744 | -47.440899 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08884eb2-0d76-3c80-920d-4ed93914430f | -6.9824 | -47.678799 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61992aa5-9968-39c2-b10f-62987f7e2916 | -5.7538 | -43.8456 | 2026-10-09 00:28:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73ff561d-894d-3b93-988e-39d4f0fa0ec6 | -11.5918 | -43.651001 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6a6fae0-df6c-37b8-996b-c1ceae280b5c | -3.2548 | -50.400799 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea8d273e-2f86-3690-85f8-5cc18790177f | -4.1321 | -46.875801 | 2026-10-09 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| feecd2ac-4e02-395f-bb33-6faf257bc4f4 | -5.1631 | -44.945499 | 2026-10-09 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08b57d1f-6e57-3173-99dc-cdf61f22b724 | -11.056 | -44.057899 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0df390-39ff-365a-99fc-adf4af1ad680 | -7.4132 | -44.771301 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aef75b29-e379-3d99-9795-38cd25b93f32 | -15.7819 | -44.683201 | 2026-10-09 00:28:00 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e71e84a-abd0-3018-aa4f-4502af578542 | -3.5533 | -54.7005 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c966bb7-fc1f-331a-bf11-1a9695790587 | -9.9235 | -44.787701 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a4b39c8-7fcf-329d-8446-1531e7390c52 | -2.4938 | -56.153198 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f457d83d-6d87-320d-af1a-81a54ec0968a | -12.0094 | -43.4482 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f91b2e4-8bcb-334b-8c7b-46771688ef1d | -11.6489 | -43.674999 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8c31355-af36-36a0-888c-d1ac218d0e6c | -11.2092 | -44.865002 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 777c08ee-c68c-35a6-998d-9a2c01a412f2 | -13.4152 | -43.729099 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f724694c-9bd8-3a49-a300-8868b249a189 | -7.41 | -44.757401 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 709ce629-0dec-397e-bfca-a1a7db6604ec | -2.9971 | -54.0835 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c074da2-f43f-35c6-b942-9667924263da | -2.7245 | -54.142799 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b71f23e-ae7d-3c19-b7dc-afb7f2988b67 | -2.5129 | -45.396599 | 2026-10-09 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58f2c134-b378-32ba-8d97-d8dd9439a0ac | -7.5729 | -45.330799 | 2026-10-09 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c45b7dab-c263-3b13-901c-ece8b641a124 | -6.1543 | -47.932098 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bad41636-b541-3ca5-a406-546e319e60d1 | -18.070101 | -41.747601 | 2026-10-09 00:28:00 | METOP-C | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 147300ac-6f55-3b27-907c-71acef02d521 | -4.5222 | -47.049301 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a280ffa2-230f-3668-89b8-d8b4e14ea4ae | -9.0221 | -44.365799 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f05e5c0e-df19-3d44-9a60-d2b2ef4a5d6d | -6.8592 | -48.7836 | 2026-10-09 00:28:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6ace9143-0a96-3f57-8109-8cb83a7b61d9 | -11.0204 | -45.4431 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 674b78b4-bc00-3787-9fb3-457d2795e737 | -7.4018 | -44.766602 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55599d68-712c-37c5-9ab1-370dd8038dcb | -8.9925 | -47.7458 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f9b16cf-e736-3984-821d-a61c0fefba49 | -7.1062 | -41.7439 | 2026-10-09 00:28:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4d9d06bb-902e-3231-b64f-4cfd7795b48c | -14.8774 | -50.306099 | 2026-10-09 00:28:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4a1b80dc-c4a6-32ae-96bd-6e13fa0fd3b5 | 2.4572 | -50.815498 | 2026-10-09 00:28:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 08d6eff5-d936-3641-b585-50e9bc8cae50 | -9.8708 | -44.872601 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7ed8109-3780-344a-9681-547dc5325ce4 | -16.5235 | -42.521702 | 2026-10-09 00:28:00 | METOP-C | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 743016f3-936e-3a6e-b88b-c2441d8c47ca | -4.9039 | -48.776299 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 261a289b-f318-3cdd-b9f6-88ea02c2c1a9 | -9.3005 | -47.419201 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 339d4774-5b96-3d30-bb8d-a03b38f763c3 | -6.9905 | -47.669102 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 780b8159-4fe6-324f-812a-e3428c9921f5 | -5.9969 | -40.987801 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 29c9446d-6b5b-3fad-8598-6080a63f829c | -5.6394 | -45.8041 | 2026-10-09 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eca2333f-1eb5-392f-beba-632c1bda712b | -2.8684 | -54.192799 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9a7b1f-2884-3be4-bca0-9b36006f8f16 | -10.8792 | -49.159 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb3b0d0-91d4-300e-8f7a-5b6161d3b572 | -2.721 | -54.127399 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c90b911-3668-3f6a-9066-54a1e09a2cff | -5.9198 | -51.821098 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c87c57e6-b0bc-30ce-a197-4a0835ad5cf3 | -1.5294 | -54.552101 | 2026-10-09 00:28:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4a0215-18b9-32df-9e77-e0a194598c67 | -5.7442 | -43.275101 | 2026-10-09 00:28:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a18a592c-68b1-3caf-b0f8-afed0fb145e2 | -6.431 | -55.034698 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06766d3-4495-3fcf-b425-ba8ee4be294f | -11.0002 | -47.486698 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc78ed42-5e81-3161-81b3-5928abcb0f06 | -6.9626 | -45.1436 | 2026-10-09 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b18c0c0-4779-3c1f-abe4-96db1a47a0c5 | -5.397 | -45.916199 | 2026-10-09 00:28:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dee153ab-3d0d-3478-8699-c4f2be6be86d | -10.4689 | -47.874298 | 2026-10-09 00:28:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cddd44e6-5f23-3bf5-aa7a-012c17509f67 | -2.3256 | -48.487598 | 2026-10-09 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0766ebd-cdfb-3219-a323-64879423ff81 | -11.2433 | -44.879101 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 036d298e-d917-3f0b-b3e2-80048517f44d | -8.9734 | -45.9133 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9b73d53-2e5b-3032-b8fb-fe01f8062815 | -7.5322 | -45.874599 | 2026-10-09 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85a0d9ea-639a-30df-b206-9e2a0cbb4346 | -14.4426 | -43.939999 | 2026-10-09 00:28:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31501639-2c78-3b3e-a0d4-3e4a1e20c9be | -13.2348 | -43.391899 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df36222f-81bc-310c-bebb-42c534a7439b | -11.6505 | -43.682098 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e699f982-18f2-37bd-92c2-3a2c7317e69b | -10.7377 | -46.620499 | 2026-10-09 00:28:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4693a48-d435-36c2-8b32-3c1702639de6 | -6.8238 | -39.332802 | 2026-10-09 00:28:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fc6c3a38-9fa4-3236-9a44-65846e094c98 | -11.118 | -44.013901 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf9a91b3-4b50-3627-9218-5f2687eaf776 | -5.6918 | -53.489101 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91e44950-a48f-31a1-86d0-2220f4c6e8cd | -3.5848 | -54.567402 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b7337c-fcf5-3209-a743-4ce8f119dc7f | -8.9327 | -45.144798 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af636704-8cb5-30b3-9750-f40c533f644b | -3.0994 | -54.175499 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ede451e-4648-33e4-ab2d-10ef54397e0e | -13.1531 | -54.352299 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 546d9a55-fc10-3112-a086-53d090f78442 | -6.0042 | -40.975101 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 234f07af-43a1-3ba8-ae1b-e2a10d03744c | -11.7629 | -46.794498 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c50e019-9429-3469-95ae-b6bb10c9ce23 | -3.0006 | -54.0989 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b55e7643-02e2-35ff-923a-05f67ebb6f72 | -13.8761 | -43.806 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfefd71d-ae42-3431-9c2a-cffc4942e073 | -11.1845 | -45.3027 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bceda10a-d986-3a61-a39f-3ded08d5b733 | -6.714 | -55.126701 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75ce56b2-a50e-3673-8e0a-33c0670abafa | -11.1794 | -45.326 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 646fc57a-f17e-36bc-8b42-5a27a32c8827 | -14.2582 | -43.671799 | 2026-10-09 00:28:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb94b1b-0e6d-3dd6-af07-47d20ccd8192 | -11.4028 | -46.699299 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec12906b-66b6-3441-92ac-8190049d00db | -6.9534 | -45.283298 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c08362a-31c1-3072-afbe-e46ab79a35f2 | -12.0421 | -43.455601 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab04d393-291a-3a5c-bd0d-4a833cba60d9 | -4.0453 | -46.902302 | 2026-10-09 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78181c69-39de-30a9-b40d-fe99c208fbfe | -9.9039 | -44.792198 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README34.md)
