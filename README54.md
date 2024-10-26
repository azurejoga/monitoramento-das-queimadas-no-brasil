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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85533583-de65-3132-a6b1-ccd287af2c10 | -7.9824 | -49.69163 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6588217-4cd3-3dae-ac56-f9bbd876533a | -7.98155 | -49.69676 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 776e4af6-c78c-33f4-92ea-29b64e0fec30 | -7.97843 | -49.69096 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 381aaa4d-f097-39c3-9ad5-4c527489af5a | -7.97743 | -49.68737 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 163be05c-e1fd-3eee-aa2e-4ceb4dc41e14 | -7.97654 | -49.69249 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9692d9f-fa1c-3495-bf02-76de6ac2cbf1 | -7.97566 | -49.69762 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 08233dc8-4c83-35de-bbbf-bf811b99c238 | -7.97448 | -49.69024 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1129983e-021d-3280-bcfe-6591f041a24f | -7.97362 | -49.69538 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a95f2798-35c9-342e-bb79-7d5f044bac12 | -9.27058 | -49.23452 | 2024-10-26 04:19:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1500a65f-9270-3151-8d40-27b31df82034 | -8.82028 | -49.68609 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 119700cc-ebc2-3ed1-88af-225d6c817bb0 | -8.81945 | -49.69106 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7540f63f-a64a-3a95-b867-4fb2661c5e85 | -8.81637 | -49.68541 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 596e369c-fa7b-38be-9268-cfe6814ceead | -8.81554 | -49.69038 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1aedeb80-03fe-39e4-8289-696f055588af | -8.8147 | -49.69534 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed28f254-7a40-353f-814c-7a791f7a940c | -8.81163 | -49.68968 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eb2c23e-49df-316b-a30b-0f97bcf9ab99 | -8.81079 | -49.69464 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec54ed42-e404-399d-ab2d-8e1e014e8659 | -8.80772 | -49.68897 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b43fd7fc-95fb-3e20-a894-cd3f6cebf062 | -8.60806 | -49.03762 | 2024-10-26 04:19:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a28e9d4-76fe-3871-aa54-9e886f3d4b1a | -8.60428 | -49.03697 | 2024-10-26 04:19:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d9e93e6-6a11-30b7-93e1-1445a80e75b6 | -8.56578 | -49.19767 | 2024-10-26 04:19:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc29eedb-2618-35ab-a302-23fa82df6c9c | -8.5642 | -49.20709 | 2024-10-26 04:19:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fae7e54a-f867-362e-92f5-ecfc1dc4a9e1 | -8.56039 | -49.20646 | 2024-10-26 04:19:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f16c9028-453f-3326-bf3a-d6222493d552 | -8.5458 | -49.55582 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5830f1f8-7fa1-3501-bc25-25116388ad11 | -8.54534 | -49.55749 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c8ca947-00b5-35b8-b7e7-f4f042f07a2b | -8.54498 | -49.5608 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32f95816-83ff-37a9-bc23-8c0cb02cf50c | -8.5419 | -49.55515 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4db50f6-cd62-3ac0-8d50-08744683ced9 | -8.54144 | -49.55682 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3719b18-1aa9-3439-a213-456b309cb01c | -8.54108 | -49.56012 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4a90e66-cc1e-3cad-ab61-9ff28612c9ab | -8.39377 | -50.04737 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c8f7f3e-a98e-35ed-b28b-8d398e9a0456 | -8.39316 | -50.05091 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 773e9b20-64fb-3c9b-bb60-b2a631d62a94 | -9.94503 | -48.95671 | 2024-10-26 04:19:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 185571e1-2082-34b0-ad45-360e9f31a6d9 | -9.78744 | -49.31214 | 2024-10-26 04:19:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d9dbcc1-5149-32e9-9cb6-07ea3a6cd284 | -9.57156 | -49.65392 | 2024-10-26 04:19:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 344d917c-2ac1-3826-8996-3917413ec794 | -9.56571 | -49.61821 | 2024-10-26 04:19:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6572f4a-70fc-301c-9516-4230ed49c4af | -9.51774 | -49.19195 | 2024-10-26 04:19:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8002e430-5640-394f-94bd-77a16fa39174 | -10.61698 | -49.48602 | 2024-10-26 04:19:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d950687-f751-31b4-9bb5-e2a656f3bad1 | -10.61675 | -49.48747 | 2024-10-26 04:19:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d427304f-085c-38c2-a783-378ffcb9e8a1 | -10.19808 | -49.14717 | 2024-10-26 04:19:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3111a1f-2c57-3804-a29d-a961de2db8be | -10.19437 | -49.14653 | 2024-10-26 04:19:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 938f3111-4091-3fbc-8277-6c8fdfc253c0 | -10.17665 | -49.50609 | 2024-10-26 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 257bce68-4f28-3704-9673-3eb50ffef20a | -10.1761 | -49.50434 | 2024-10-26 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0359b188-59e7-3827-985e-59e2c73758d1 | -10.97647 | -49.30142 | 2024-10-26 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c8e2f00-1534-3d55-804a-f40e69dbd834 | -12.4501 | -49.8989 | 2024-10-26 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77b8c238-8b2c-362e-96a2-8c2138ade596 | -0.57714 | -49.5102 | 2024-10-26 04:19:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 711ecb8a-50a5-37d8-a8f2-a1f58b48c517 | -0.57396 | -49.50617 | 2024-10-26 04:19:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21e485d0-6f91-303e-9d53-05534c30f027 | -0.5733 | -49.51041 | 2024-10-26 04:19:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7b58338-aa16-3eb0-9ed4-2e4f8d9007be | -0.57275 | -49.50951 | 2024-10-26 04:19:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35962b99-e4d1-3052-a8aa-98810bccbbd8 | -0.23538 | -48.82307 | 2024-10-26 04:19:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14659685-da0b-370a-a479-a0bf93b99743 | -0.23478 | -48.82692 | 2024-10-26 04:19:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bb5ce1c-509e-3195-88ba-2ed2f53afaae | -6.22539 | -50.87345 | 2024-10-26 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fe36ed3-0ee3-39fe-8bae-ea525659082e | -6.22101 | -50.87256 | 2024-10-26 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e94f477-db5c-3ae2-b1f0-96fb461c070a | -6.20114 | -50.85623 | 2024-10-26 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8cd86f6-d3c7-3a5d-b576-920680ace125 | -6.19675 | -50.8554 | 2024-10-26 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f66d2aaf-8ded-3005-9717-27d9e8dc4796 | -6.19307 | -50.85047 | 2024-10-26 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7888b825-c930-379a-9236-b2a8a7e355a0 | -6.19234 | -50.85471 | 2024-10-26 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af958ff8-7f7f-38e8-88cc-ae09850a76db | -6.18792 | -50.8541 | 2024-10-26 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c37a786c-d491-3195-9390-0cdc00ff68ed | -5.94704 | -50.86681 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14d04e39-d960-3a25-8643-310f97e7aef5 | -5.94185 | -50.87046 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fac01bdc-7a88-3491-b0aa-90da6c2d8124 | -5.57543 | -51.082 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c016d23-cbce-3f0b-a5ec-ff0b7e6888fb | -5.33001 | -50.87435 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb6d2806-d435-35e5-a739-cf9f0e4892a9 | -5.28775 | -50.98667 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ba9cb8a-fd5e-3b65-bec0-8b2f4e2d3e19 | -5.28711 | -50.98455 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e898d3c-cc5f-3540-afbb-1ca4d0a726c7 | -5.28637 | -50.98911 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00bf2fb8-4757-3139-b0fe-0b5615adf1eb | -5.24873 | -50.69182 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c634a412-e282-38a8-86bd-cdfe2c33285f | -5.248 | -50.69613 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f76ce2ba-b804-35ce-8314-c1b86fdef9fa | -5.2443 | -50.69112 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5b2bb5b-862a-3bc6-929f-c480b6a8c22f | -5.06988 | -50.58042 | 2024-10-26 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfe725cb-e8d6-3923-9a99-96624011a5cf | -6.438 | -49.9005 | 2024-10-26 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dfdfb0b-382c-30f6-9af2-9fc3ccba7ae6 | -6.43593 | -49.8969 | 2024-10-26 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78e15fa6-4bdb-3420-8f3f-dd760736c1d9 | -6.43534 | -49.90052 | 2024-10-26 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d8575a4-1c93-3e70-b1c5-9317fda78683 | -6.43389 | -49.89981 | 2024-10-26 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ca7e61-0bd4-3ecd-b1fd-da106a25c1ee | -5.85018 | -50.35329 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77ba473d-c474-3c94-91aa-c9c7efc6e992 | -5.25963 | -49.51984 | 2024-10-26 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adc1b995-f72b-3bae-bf30-f56cce67d0ae | -6.89832 | -50.31774 | 2024-10-26 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16dc618c-f9a7-36d5-8b17-319b03a9fb26 | -6.89412 | -50.31707 | 2024-10-26 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00cabe55-2999-36c4-a949-440cf43856af | -6.84344 | -50.76053 | 2024-10-26 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18541e9f-f847-37ce-9e2c-c24fa0461649 | -6.79726 | -50.8716 | 2024-10-26 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4ae3617-b794-3032-8b72-2183af2878d0 | -9.25722 | -50.68667 | 2024-10-26 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d668fb2-55e4-396c-be01-0c4225b564fd | -9.25657 | -50.69044 | 2024-10-26 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b03d5ed-61e5-3fb6-bc13-aa5456fa7948 | -9.1047 | -50.63792 | 2024-10-26 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f10023c5-5ac1-3fd8-9ef9-49500f63a663 | -9.10407 | -50.64163 | 2024-10-26 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df9b842b-db2d-344f-b367-38405f2e0547 | -9.47696 | -50.81454 | 2024-10-26 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd39640-84ca-3b29-bf4a-6e803d155dde | -9.47631 | -50.81833 | 2024-10-26 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3a2f0f-ac44-31f2-9e94-373dc2e08d47 | -10.47571 | -51.95912 | 2024-10-26 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caa3c5e1-10a1-3e12-8431-0c5abb9b23e5 | -10.35585 | -52.10283 | 2024-10-26 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ca145f5-2f19-3ab1-9e32-ae184763acd3 | 0.31359 | -51.00029 | 2024-10-26 04:19:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90e3d664-4783-3dea-9dd8-6ae0bbe2b9d3 | 0.31299 | -51.0013 | 2024-10-26 04:19:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f048f052-ab4f-3fa8-b19a-91d242cc7a6b | 0.31274 | -50.99471 | 2024-10-26 04:19:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed0367ad-fc97-3811-9149-0dc35e65a6f6 | 0.31209 | -50.99571 | 2024-10-26 04:19:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99ca92a5-c244-3270-9f54-92e5b5e592ed | 0.30865 | -51.00109 | 2024-10-26 04:19:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5433b711-d43f-36cd-ac20-17f86194b413 | 0.06415 | -51.58747 | 2024-10-26 04:19:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46b4530c-ed63-3340-89bd-82cae17d521c | -10.79612 | -53.86465 | 2024-10-26 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09935fe4-8a8b-3c88-bce4-e448dbcc3bcb | -10.79114 | -53.86367 | 2024-10-26 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9c7a51d-aeaf-32e0-bb5a-d9afaa22e90a | -10.78616 | -53.86268 | 2024-10-26 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5d856bd-0c0b-314a-a635-8900eb57a7e8 | -10.78508 | -53.86855 | 2024-10-26 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19195272-5f24-3a17-a90c-91ac7d683469 | -10.78117 | -53.86174 | 2024-10-26 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff9709e8-ab5d-3201-8bce-37dc2edb4a06 | -4.50094 | -54.96188 | 2024-10-26 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77c44af4-0b64-396f-8f22-a1c8d0378bbc | -4.48662 | -55.08284 | 2024-10-26 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b937954-d741-35ab-b2f7-fab067cf742a | -4.48059 | -55.08195 | 2024-10-26 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dbee7e5-2eff-3a0f-9ec1-e5bc22896049 | -4.34558 | -55.35734 | 2024-10-26 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README55.md)
