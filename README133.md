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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57fa6fe4-9269-3b63-97e3-283c02b86220 | -11.85789 | -59.01171 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82646d4f-e4d9-30bc-b1c9-b9c602740184 | -11.85362 | -59.01126 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8b6cce0-a871-3c23-88fa-aab796b92331 | -11.84479 | -58.89861 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 380465bf-7a0f-3cf3-92c0-b9e312c114e7 | -11.8426 | -58.89787 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86715a1d-6c7b-340e-8840-28e6abe06ee5 | -11.71031 | -58.84004 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5932d01b-0ba5-34a6-bf4f-97256d57eccc | -11.70975 | -58.8441 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9979132-8f91-3ba4-8323-0e9b435b222c | -11.70603 | -58.83929 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c304e92-c224-3bdd-9698-7a81e9e9fb3f | -11.70548 | -58.84332 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b02c2771-6573-38c6-8c59-adb4d15bf44c | -11.7012 | -58.84259 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b1ac7a9-f0a3-3ba5-950e-f01ecba8cd3f | -11.49022 | -59.09943 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ae4e2a-6577-3f71-bffd-d9e6ce22ea55 | -13.14676 | -59.6996 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04bc3138-f7de-3b68-a900-9c10ae011eff | -13.14625 | -59.70345 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bda9cb88-c784-395d-9df6-9c50e784d035 | -13.14313 | -59.69514 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27f2728f-c248-3aca-9603-3edc61acbea7 | -13.14262 | -59.69899 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc1691b8-a32a-3a2d-87c4-e4bc94de0cbe | -13.02856 | -59.87308 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c9ce01-7844-31f1-b282-592d56336603 | -13.02498 | -59.86871 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b59d31-86d8-3e44-90b8-e3148f272fb2 | -12.97438 | -60.0908 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62bedcae-2afe-38e5-a2a8-27e67e4bb02a | -12.97391 | -60.09435 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12ce19ad-f747-3c19-a410-500fa7992b1a | -12.96199 | -60.08968 | 2024-10-06 05:36:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a673fe9b-a273-37e3-9053-6a23cdd20964 | -9.94733 | -60.12949 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff9c5fea-e7fb-3570-ade6-b391add4a5bb | -9.91956 | -59.911 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ef2670e-17e0-3e5a-8667-cad8d05fe8b5 | -9.87661 | -60.31835 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d612dfb2-6fef-3d9c-8173-ef7c0d602d30 | -9.87212 | -60.32246 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd859039-9649-3673-89e8-0fabfcbcec1a | -9.86899 | -60.3172 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0b7ac47-5e08-32e1-9bd7-0c3a12d7e4cf | -9.86831 | -60.3219 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f7ba893-876a-313e-b4fc-cc4cf77f3398 | -9.86788 | -60.29792 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 383c35ba-d964-345d-b48a-bcb8bd71658c | -9.8672 | -60.3026 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c57ec58-6ad7-346e-83d2-0120086e909d | -9.86407 | -60.29733 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfaedbaa-feaf-3249-9df0-0092d8a12199 | -9.86339 | -60.30201 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2be18f51-8825-3ae0-840d-c75457e215aa | -9.86025 | -60.29677 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae45d632-428d-36d5-beb2-eda951c3d4e2 | -9.85958 | -60.30144 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d6a1db2-6954-3673-a1ad-d6114dda011e | -9.8589 | -60.30613 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8e8ef4d-e643-393e-8dca-1ebcc8da70c3 | -9.85823 | -60.31082 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc85d1f5-badf-32e9-848b-b6f7323438f0 | -9.85643 | -60.29622 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63a47e26-99f0-3644-8a0c-c59cbfb90a8f | -9.85576 | -60.30088 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6081152-1962-358e-954e-c2517d199fec | -9.85509 | -60.30557 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a20e7bac-944e-316b-a31e-b5e2d0be9af4 | -9.85441 | -60.31027 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87c0dea6-b268-3324-ab86-9680c2197d86 | -9.85262 | -60.29566 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96ade1cc-6d80-3e55-a3e6-87b71aedd2c8 | -9.85195 | -60.30033 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c38cd6b6-e109-3445-9153-b603a00bb93c | -9.85128 | -60.305 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07c1873e-f6de-35f4-98b4-e2ac6e4f3240 | -9.84948 | -60.2904 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86098625-bd84-3f40-b440-4faac565e34e | -9.8488 | -60.29509 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e623d16-d0f6-3568-baa2-0fe068c0a7e8 | -9.84813 | -60.29979 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb05b5d7-6972-368a-bb8c-8033dfb2d21e | -9.84746 | -60.30446 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d53a82a6-b0f7-3506-92e1-29c0f2fc21cf | -9.84566 | -60.28982 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b44bf7b3-922c-3280-b0fb-a2890a5049a3 | -9.84499 | -60.29453 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f41ebfb6-12e8-33b7-924a-4b89a48d9f56 | -9.84432 | -60.29922 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63331e34-6934-3aac-9893-0410729d817e | -9.84365 | -60.3039 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe8a6dbd-ad46-31c7-a90c-66aeb9f8e196 | -9.84185 | -60.28924 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edcf0127-e4c3-3193-be5f-c9333061dd07 | -9.80013 | -60.47284 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e2f0a0-804f-3839-94f3-9706ee7d301e | -9.79947 | -60.47743 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab914f35-3d2e-3458-a5f8-10ae4ad52fb9 | -9.79635 | -60.47233 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 964c3751-f4cc-3756-a971-994aa883f390 | -10.07625 | -61.11053 | 2024-10-06 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ff5796-f632-32fd-a391-9e2277b3d13e | -10.07195 | -61.11437 | 2024-10-06 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce39bc9d-efe5-3ff6-b072-bb13c4ee2d8a | -12.27735 | -60.47831 | 2024-10-06 05:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211d1d85-c550-3762-b967-ff8114552ffa | -13.4303 | -61.91895 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ca3478b-f195-3af3-8cf9-fc000f6a44f6 | -13.42968 | -61.92324 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e903680-3aab-3391-9ff2-f70697ccbd49 | -13.42665 | -61.9184 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95197773-84a5-3eaf-91f7-41e37dcc921a | -13.42603 | -61.9227 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 768b83e8-6c7e-3d80-85b2-b84c1e2bc3ef | -13.41075 | -61.95115 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2933b678-dee5-39cb-9c8d-849f6a6af82b | -13.41021 | -61.92913 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b19bc2d-4bad-3f8e-9ef7-39bea8ba4c73 | -13.40959 | -61.93342 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eac364cf-f588-3303-bc67-aceff585536f | -13.40773 | -61.94632 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e77b0a-2847-3ac1-b373-6868e19e440a | -13.40711 | -61.95061 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d7ea441-8ac3-3357-9132-3a72078b298d | -13.40285 | -61.95436 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23c040a1-5ad5-3b25-b367-750c6793fdb4 | -13.40045 | -61.94523 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 812d3373-ffea-30e7-9cb8-92b6f579f374 | -13.39922 | -61.95381 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a33114e3-b2de-3418-823a-7e7c7fd6a82b | -13.39681 | -61.94468 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a608b36-4902-3df7-8fe4-224cf49d3922 | -13.39317 | -61.94413 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92c0956a-11aa-3b1b-8b7b-ead71dc62fac | -13.39256 | -61.94842 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad8f83cb-1bdd-3dce-adbf-ba407428b089 | -13.38953 | -61.94358 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb9e324b-742d-32d9-9c90-f9b638bd4917 | -13.38892 | -61.94787 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bcccc34-a9ab-33a4-90ff-cc3a132ed08f | -13.38886 | -61.97415 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5e7557d6-8d34-3d0f-8a5d-e9b348028e49 | -13.3883 | -61.95216 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 499ebb7e-1c20-3b87-b13f-a9c491ba4a84 | -13.38769 | -61.95646 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| fff5c45c-37b0-3c60-8bb8-78e224cb5a7c | -13.38707 | -61.96074 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| aba24f2d-817f-37f2-801e-b6bae0b60d80 | -13.38467 | -61.95161 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1e480f21-aa01-353f-99ed-a6f2de7e347c | -13.38405 | -61.9559 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1d8f129f-dde6-3d04-9b4f-07dfd75964fa | -13.38344 | -61.96018 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d8afedc4-0117-3e0f-84b7-f607449c8070 | -13.38041 | -61.95536 | 2024-10-06 05:36:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75693529-98e8-38ec-b674-082ac206febf | -12.87776 | -60.51495 | 2024-10-06 05:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8af4077d-61d5-3a5e-bb4e-f8d70cd7c662 | -12.87386 | -60.51428 | 2024-10-06 05:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ae9ffab1-3b42-331f-9719-aff1ab9bd16c | -12.68928 | -60.8356 | 2024-10-06 05:36:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50a715c7-9972-36d9-a9f2-c35231bad54e | -12.68861 | -60.84038 | 2024-10-06 05:36:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 453e1db7-7331-32ab-807a-14572f7a5736 | -12.68478 | -60.83982 | 2024-10-06 05:36:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f992ceb-8a6c-301f-956c-ac47ac25032b | -12.5606 | -60.66946 | 2024-10-06 05:36:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53bd70da-6ce5-3b2b-abf8-6d94157102e9 | -12.55603 | -60.67381 | 2024-10-06 05:36:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bfda40c-118d-31b1-b3b2-08105f88f3c0 | -9.69881 | -62.172 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c5bb85d-96e6-30d6-920b-524ea9885609 | -9.69534 | -62.17148 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd78e75a-8442-3f9e-9e91-aa96032ac50f | -11.79455 | -62.95164 | 2024-10-06 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a6a0ca-7b23-3d84-b293-ab5d268b1dd3 | -11.79169 | -62.94735 | 2024-10-06 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6bc34bdc-3698-3750-a5e0-c635aa631832 | -11.79112 | -62.95111 | 2024-10-06 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ffe2d3-9e8f-395f-b749-8a3cc107e1fd | -11.79054 | -62.95488 | 2024-10-06 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36779eaa-5c39-3dcb-aa77-91acfd8c0c64 | -11.78826 | -62.94682 | 2024-10-06 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b9acd31-ad93-36a7-9a37-9205d699e47e | -10.93944 | -62.56535 | 2024-10-06 05:36:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4cdcec1-abc0-37bb-9fc4-eb06bc1d2fc4 | -10.93598 | -62.56481 | 2024-10-06 05:36:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65fdf5ac-4b8f-364d-a8f1-b4958fe6e99b | -11.90934 | -62.09475 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1bcb625e-72b7-3ecb-9926-1533106eb0c3 | -11.42844 | -61.80146 | 2024-10-06 05:36:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d36e25e1-fa02-33ac-93da-ad8bd077ab4b | -11.42485 | -61.80093 | 2024-10-06 05:36:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3528d243-4182-3aaa-8e38-da0ca2b3bc6c | -12.72652 | -62.93823 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README134.md)
