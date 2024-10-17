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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 425293e4-3975-3ad3-94bc-3b5c5286b737 | -6.68918 | -43.54925 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed1caafe-7c5b-3c3a-bb5f-fb024fa7146f | -6.68544 | -43.54372 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed47d0e7-500b-3dc2-8941-ac91855c0961 | -6.68463 | -43.54838 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09c29251-0f39-38ef-a12d-4075c6927b4e | -6.68382 | -43.55307 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60731b91-8309-35fd-9a4e-d3e474d4998f | -6.46577 | -43.20725 | 2024-10-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| afed425b-54f2-3c68-b1e5-252a682d7ecd | -6.46419 | -43.27122 | 2024-10-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76bd9260-f17d-3759-a115-8817da15acee | -6.4613 | -43.20643 | 2024-10-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c35d2c1-1d39-3a78-b498-cbcc062cb0fc | -18.77848 | -45.60238 | 2024-10-17 03:49:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcf75021-c9d8-38eb-af64-679ec7bfd323 | -18.77422 | -45.60167 | 2024-10-17 03:49:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91c36e1b-cb51-30e3-b9df-e4117185adb0 | -5.72979 | -43.82071 | 2024-10-17 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0983a872-0639-3741-a7d8-d6fcae48af70 | -5.72506 | -43.81995 | 2024-10-17 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c044f111-274a-31f2-aad5-221ebb026ab9 | -5.54315 | -43.91282 | 2024-10-17 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46fa892d-de71-3633-bf41-2adaa7c18240 | -5.53837 | -43.9121 | 2024-10-17 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a525c89-a6ad-30ad-9ba7-f4461456992d | -5.50646 | -43.695 | 2024-10-17 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4abe749-ca9f-3dc5-8f9b-5255a938c030 | -5.50561 | -43.70002 | 2024-10-17 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd95d52b-8983-32a2-8c24-3d432cc0a1da | -5.34511 | -43.48796 | 2024-10-17 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18854a25-afd5-37ba-a859-4db73c24c260 | -5.34047 | -43.48714 | 2024-10-17 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f87e556-2451-3943-91d0-e8489be02828 | -5.97813 | -44.00448 | 2024-10-17 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17975991-ee48-3602-a274-c8a58070c763 | -5.58546 | -44.87905 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d62ffa0-a364-3608-bdbf-3a6184d802c0 | -5.57316 | -44.88934 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2498c382-aa87-3d13-873c-cfa8860a7156 | -5.57164 | -44.88174 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a2973c5-d6d3-34d2-a131-98baa2c7ac9e | -5.57062 | -44.88781 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9f38cbfa-1eff-32ce-9856-02645abbc63d | -5.56913 | -44.88244 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3dcee66f-78be-3078-be68-ddcce6da25ae | -5.56806 | -44.8885 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 95340daa-34d8-3d61-a4d7-6720e2e5483f | -5.58039 | -44.87807 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 112fc2e3-7631-33f7-a89c-b19ffd4ce633 | -5.57985 | -44.8811 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0fb98864-2ca0-3e74-91bb-208c94f19040 | -5.57932 | -44.88416 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd0ad32e-985f-3b0e-9fc8-48c098c502a6 | -5.57878 | -44.88721 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f2bacbcb-946c-3c90-b762-b6aba9d00c4d | -5.57673 | -44.88263 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb3c61ca-7935-34fb-92dd-193916fe56ff | -5.57622 | -44.88567 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 285542f2-57d8-3872-ba23-cf81429e6476 | -5.5757 | -44.88875 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c78a8008-88e6-38b4-9958-9895ceebf55b | -5.57423 | -44.88325 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 832d0a70-ee1c-3768-abc5-3f066d8e4fe3 | -5.5737 | -44.88628 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f4c4f5fd-13cf-316a-8498-a91e0b3d09ba | -5.57262 | -44.8924 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57407c28-d9ab-3708-b655-348439e34c0c | -5.57113 | -44.88477 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6921f620-99bd-3083-a9a1-d936f52d152f | -5.5701 | -44.89088 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 976fe7ed-1618-3ea2-8d33-a0d9753b2828 | -5.56959 | -44.89396 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 51736376-ac85-31f5-8e7d-ff63d9bec11c | -5.56859 | -44.88546 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 40c3057c-fd6d-3ff1-8b01-b062edffe8b9 | -5.56752 | -44.89154 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f9b550b9-1659-3770-a3cf-7b8c236c240a | -5.56601 | -44.88406 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f556d57-7176-3439-8977-c6251b1a41bc | -5.5655 | -44.88705 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 275b63e2-8f2d-390f-9bc4-d0bc01fbebc3 | -5.56499 | -44.89009 | 2024-10-17 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b16b56e7-613a-35f6-b499-62aec3059e78 | -7.29256 | -43.94092 | 2024-10-17 03:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e5e516c-227a-3afc-9a7d-5cc1c167e50a | -7.12241 | -44.07521 | 2024-10-17 03:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef1ea6ef-9409-3aa9-8ed4-9249b038c832 | -7.12067 | -44.07854 | 2024-10-17 03:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03d3d569-a088-3694-9e4a-e60ef7bf0d00 | -7.11773 | -44.07435 | 2024-10-17 03:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2814bc3-4bec-3f70-b1d9-4f19a4972947 | -6.58043 | -44.23085 | 2024-10-17 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d432d80f-e63f-31a3-8e4a-d55223100369 | -6.57568 | -44.22981 | 2024-10-17 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70a1d8df-3b14-30a8-8714-55979e770878 | -18.37985 | -47.41075 | 2024-10-17 03:49:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1138bdd-6a71-3725-8def-a65dfb925d63 | -18.3783 | -47.41129 | 2024-10-17 03:49:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55fb2541-0b55-39e2-8023-1f2165892c9c | -5.98377 | -45.36693 | 2024-10-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b7df26ee-5914-3013-bd85-e6312745d8f1 | -5.98322 | -45.37009 | 2024-10-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b59aa0af-7639-31f4-9146-6876687ec548 | -5.84358 | -46.23925 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a12304d-9cee-3d91-8698-2bd7ed398d01 | -5.78765 | -46.19972 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a35dcba-ab8d-3229-9fb2-3f4cd8983dba | -5.78367 | -46.19602 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6332f76f-d17d-33d9-a58d-126b43d07d82 | -5.75115 | -46.50255 | 2024-10-17 03:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a11bce3-353a-3d43-b086-c4c8a1629cc8 | -5.74547 | -46.50164 | 2024-10-17 03:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bed4096-3a69-33e6-a682-27933e3bf808 | -5.70903 | -45.77837 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c83b6995-60cb-38cb-8d6a-c2bfa21fd914 | -5.98267 | -45.37327 | 2024-10-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 86903900-3ffc-3a36-ba53-2bf9bc0da1d6 | -5.98212 | -45.37646 | 2024-10-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8e54c8c3-fb86-331e-9dd4-de4ae0271ef0 | -5.97798 | -45.36925 | 2024-10-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a50b1843-fc7f-39cd-a4f8-7626a7f5472e | -5.97743 | -45.37244 | 2024-10-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4577d953-ba33-3ced-af2b-f73eb3cf4c54 | -5.97688 | -45.37561 | 2024-10-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c96b982a-766d-35ca-8dfa-dd70c8515279 | -5.85341 | -46.43116 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae179901-2414-38b7-bfd6-5c0837124e1a | -5.85272 | -46.43499 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08819c28-797d-38ce-8595-b55748d32f1a | -5.84912 | -46.24031 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5deeb7e-5543-338f-938a-da915432e7a7 | -5.84861 | -46.45798 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3afa01d1-9ec9-33c6-9aaf-6937554c4f14 | -5.84787 | -46.46214 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4597816b-4ec8-340c-8863-b0cdbc8bed4d | -5.84664 | -46.45517 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4639a40b-3c20-32ec-bfae-3e1045e4e68a | -5.84593 | -46.45935 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b739e361-e50f-3622-b3c8-140fd0b391ea | -5.84421 | -46.23566 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a9fcf8f-e7b9-3530-afb0-7c28c034032e | -5.84371 | -46.45291 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f39c3edd-ee59-391a-8f12-310a3cf46176 | -5.78832 | -46.19598 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b6a116e5-7faf-396a-8c75-a3c806eaccb5 | -5.78272 | -46.19533 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2b4d0207-7e48-3c8d-b058-9650d627283b | -5.70424 | -45.7739 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e497035-26be-3db0-b125-e1c701c6fc5e | -5.70365 | -45.77732 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3097a00d-3b9e-3a18-9d2f-8976d4cf215f | -5.70305 | -45.7808 | 2024-10-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 627fcb7e-373a-3a90-aa92-12376c426600 | -5.2115 | -45.61411 | 2024-10-17 03:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de64c95e-71ee-3620-8db1-d2e4163444e2 | -5.18498 | -46.09763 | 2024-10-17 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f347f18-d1fa-38ed-8b54-eab450243426 | -5.21205 | -45.61084 | 2024-10-17 03:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5159775b-981b-3850-9064-f4f2cc8d4a6a | -5.17942 | -46.09669 | 2024-10-17 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24e2af91-42d8-3f40-a8bf-fe7fa3a8d0b0 | -7.15474 | -45.43293 | 2024-10-17 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6cd04d1-846b-3167-b3f6-b3b118b50fa3 | -7.1542 | -45.43598 | 2024-10-17 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 923f0dbc-b290-3a3f-b55b-49c650698f5b | -4.93747 | -47.0364 | 2024-10-17 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 698e4fda-d083-3627-96b6-500be96a6ae9 | -5.75046 | -46.50642 | 2024-10-17 03:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 50f3be12-6a54-3ac5-ba03-c94bfc770066 | -5.74479 | -46.50549 | 2024-10-17 03:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d42f5411-95ef-3bf3-a77e-d8d0e156cd7a | -4.76216 | -48.00136 | 2024-10-17 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| db3f57b9-5dc5-3364-bd51-a8eb02860884 | -4.76128 | -48.00635 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 184e430b-6744-3b56-a158-32490fb191cd | -4.72214 | -48.30373 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1e2d4cf-df6b-33f3-8913-f8bc6d4b8bfa | -4.71573 | -48.30245 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1f4e334-fdc0-3b8e-825f-2d80b47ed81c | -4.58529 | -48.03035 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdfa12eb-4aac-39bb-b043-a0a24a9b4576 | -4.58268 | -48.03313 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42e5b2ee-6386-3f5f-ad09-3d5ff9780066 | -4.57904 | -48.02873 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93e333e5-d3a8-3b0b-ba9c-101a145390be | -4.57637 | -48.03181 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a858785d-006c-30cf-a3ac-c4ca7bb18069 | -4.57551 | -48.01209 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 25d0d6fc-fd30-3e29-b817-9739b9cd457c | -4.57458 | -48.0172 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 187f1498-a075-3f12-a28d-76ba5ad3d394 | -4.57277 | -48.01488 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0dd41598-c920-39f2-a462-2d07477a670e | -4.57187 | -48.02005 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e32d0640-ca1b-342a-806e-c5023be1c52a | -4.4691 | -48.11902 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 513883f8-79c1-3f69-bbda-100838ace8f4 | -4.46846 | -48.11807 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
