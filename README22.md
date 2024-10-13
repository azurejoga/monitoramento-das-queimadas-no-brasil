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
| 9c0e1949-cf71-3d43-9a8d-c0bbc6e74ac1 | -18.205099 | -56.555099 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d6ddf685-31d2-3b81-93fd-df6b1847ddc9 | -18.2085 | -56.568501 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a522555-7c82-3f82-8d5b-affa8887bb50 | -18.212 | -56.581799 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ba29e5d-e1b0-301d-a9f5-2bdb43e78703 | -18.195499 | -56.557899 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| db7d4754-5f0e-3bdc-ac6b-c48bb6c147e7 | -18.1989 | -56.571301 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b6de37f8-9ecd-39c8-be2d-b7dac1415830 | -18.181601 | -56.8288 | 2024-10-13 01:41:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 352e56aa-d4bd-3083-8b2e-8c50e6ae0895 | -18.1849 | -56.841702 | 2024-10-13 01:41:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6e24716b-b103-3982-bc97-0c8af0dd3078 | -17.7153 | -56.265099 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c2b85868-da34-32af-a9e1-2fd845a44886 | -17.9818 | -57.350399 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cca8e514-3fab-35da-a4cb-cb1321a2c220 | -17.9849 | -57.3624 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ffad594-511a-32ed-b882-0a426e2dff62 | -17.969101 | -57.341 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c12589af-eb61-3119-b971-70689d5fb925 | -17.972099 | -57.353001 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dd62b2a0-3742-3c3c-a079-4641a5ff73fc | -17.975201 | -57.365002 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1f3f8ce4-8189-3114-abd8-695770ab3aef | -17.978201 | -57.376999 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e0680e44-4d41-3eb2-a695-2c62ffbfca16 | -17.9624 | -57.355701 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| de8c7ee8-4c48-33d7-9d65-4e9b959a4e09 | -17.9655 | -57.367699 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e3e13337-4a8d-3fa6-9c44-7a7dbfac5d44 | -17.9685 | -57.3797 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72edd042-38d8-3a96-893c-3a1026248e7a | -17.949699 | -57.346298 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7b783234-58a9-3d99-8477-23d84094911d | -17.9527 | -57.358398 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f520bfb9-ee4a-3bff-a2a9-6916dd8fdc61 | -17.955799 | -57.370399 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 27580d10-b878-3253-a85f-17588b4e12ff | -17.958799 | -57.382401 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d6952aed-0d6b-38cf-b2a6-664d92b71559 | -17.943001 | -57.361099 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 40524c4c-81ef-354b-bf41-53fd02bd5878 | -17.9461 | -57.3731 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1b846982-36d3-3f49-99ea-61e28be627b8 | -17.9491 | -57.385101 | 2024-10-13 01:41:31 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 45be6ce2-cc1e-38d1-a162-13ff1506e0f1 | -17.640301 | -56.255699 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ea44f37-2a1e-3ed0-99b0-68c5d9d89664 | -17.643999 | -56.27 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 94f8ae4f-ed2b-334f-8844-3d70d7219752 | -17.6476 | -56.284199 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c1925604-055a-3a8f-89d1-046eb0966acf | -17.895599 | -57.296501 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 926b86a7-37e4-3163-a48b-896033a49230 | -17.898701 | -57.308601 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 111d6a89-df5f-303e-b054-a20132bd1de9 | -17.9018 | -57.320801 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d5675238-105e-332b-a822-72615db5b177 | -17.8859 | -57.299198 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dde79860-8483-3c80-be45-f0c95390874a | -17.889 | -57.311298 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9bc2a9c8-4a30-3a8b-bd06-e1c41f5422a8 | -17.892099 | -57.323502 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ab14324d-0fe5-33a9-96e1-7b5c6b91a9fb | -17.873199 | -57.2897 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d6325f49-ea91-38ab-9d99-a728841fafd0 | -17.876301 | -57.301899 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| caec1518-ac5b-3add-a101-bde455a9c900 | -17.8794 | -57.313999 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1b431138-43f2-3394-a9a8-52f510cbebc9 | -17.882401 | -57.326199 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 081b42d9-f3d6-390c-a483-a64fe66291b3 | -17.863501 | -57.2924 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 12615c6d-ff94-3290-882c-43e6d84a704c | -17.8666 | -57.3046 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 54dfa610-49a5-36be-80fb-af247e24ed26 | -17.8727 | -57.3288 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c688cf15-7af7-3b07-8dd8-bba39af09dc4 | -17.9048 | -57.332901 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b56bad34-c59f-3cab-9100-cfb1909551b7 | -17.9079 | -57.344898 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f01e8138-8b4d-38f0-b4b0-6065fda61d6f | -17.8951 | -57.335602 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8a82dae1-1c23-3f4b-9110-fe08524b8c78 | -17.898199 | -57.347599 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7840c98c-7c30-3d9a-945c-c8ef30ed3490 | -17.901199 | -57.359699 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1489b868-dd6f-3333-93f1-b337b0f7d498 | -17.8855 | -57.338299 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a87fcfd8-47a9-3acd-b49d-538f9a669661 | -17.8885 | -57.3503 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5ae283be-83ad-36f3-ba28-168ce73b529e | -17.8916 | -57.3624 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 835c9b03-3e5e-3808-81a9-d74927ed6c04 | -17.875799 | -57.3409 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b33a063f-ccf3-3e81-8076-d7d19cb62219 | -17.878799 | -57.353001 | 2024-10-13 01:41:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 130507ec-a722-327b-85e1-6ec4b944c32b | -17.8538 | -57.294998 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ba8ded59-7d53-3a09-9a54-1089c1697762 | -17.856899 | -57.307201 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f9efd3cd-420f-34c1-8163-927655534c25 | -17.844101 | -57.297699 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b9cefdc5-3233-3aa6-ade7-aff4ca016cc5 | -17.8472 | -57.309898 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d0dbc6ab-87ed-370e-a927-37d36a9c347d | -17.8344 | -57.3004 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 91eedc97-0397-3962-a927-63c9fcea9a2c | -17.8375 | -57.312599 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cdebb04c-4c4c-34c1-a0d6-692044bf328e | -17.824699 | -57.303101 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d73e3a6c-c604-3241-8fa8-d40d699f3399 | -17.827801 | -57.3153 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2e7ba2d1-b3cc-3f27-9d6c-13173125ff3c | -17.830799 | -57.3274 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 53e3de71-f7aa-3fc9-abc6-d2df422e5ad1 | -17.8661 | -57.343601 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9897231c-be2c-3654-bab6-6a5fadd2ae8e | -17.869101 | -57.355598 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2f275bdc-b56a-3fa7-a97f-4a1cd6e4f106 | -17.8564 | -57.346298 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8e60c389-34b0-3888-85ae-a4bb47c42c85 | -17.8594 | -57.358299 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4d9b3194-e191-3fd0-b6db-ba7b86f43484 | -17.862499 | -57.370399 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 486a4268-606a-3dda-a0ad-520a98b1c302 | -17.846701 | -57.3489 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87e4a912-e71f-3354-85fb-dc53389d0390 | -17.849701 | -57.361 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e0d3cbfd-19ff-374f-ae17-b4acdb8da487 | -17.8528 | -57.373001 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 747eeb0e-5cc0-30f8-be80-bd04ae180fe7 | -17.84 | -57.363701 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 80d961fa-b72e-38dd-97cc-dd7ce399a5f7 | -17.843 | -57.375702 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b27392f4-5259-30cf-ba46-b1fdac9b08d1 | -17.846001 | -57.387798 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6169a878-de00-3f8e-9740-e853e298e9e7 | -17.830299 | -57.366299 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 750528e9-2452-3bde-b7a7-ea9a8ef3b212 | -17.8333 | -57.378399 | 2024-10-13 01:41:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72214eaf-e2cc-3a82-99d0-79a0aded0143 | -17.836901 | -57.351601 | 2024-10-13 01:41:33 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5c83d45-4bf6-3981-92da-f33dc090966a | -17.8272 | -57.354301 | 2024-10-13 01:41:33 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfdbc15f-67df-3a54-83dd-f39574bb297b | -17.212299 | -57.300598 | 2024-10-13 01:41:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39b9cb96-1497-3033-924f-5984e1e9e9cc | -17.1882 | -57.4519 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5547a4a4-f48d-3db1-bd1d-c44c88260bd6 | -17.191299 | -57.4641 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5d184d6-8225-312b-bc04-0fe485747706 | -17.1723 | -57.430199 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a07c2ed-2418-3ca5-93d1-2d3f37fac8c0 | -17.1754 | -57.442402 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc1aa36f-637d-356e-8948-2211ded29001 | -17.178499 | -57.454601 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b939aed-14e7-36e4-9605-0a8fd0c1ffa1 | -17.181499 | -57.466702 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61712e99-0b8b-34af-8bd4-51d3a9f8e57a | -17.184601 | -57.478901 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84c913f4-2c42-3705-89a2-459f4187cb90 | -17.165701 | -57.445 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c9a5715-8056-37c6-a723-6aaf3cf213c1 | -17.1688 | -57.457199 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a65d466b-b762-3484-97fc-5ea63bbf148c | -17.171801 | -57.469299 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5232d200-c30b-3059-9375-2184f11075e7 | -17.1591 | -57.4599 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c7c0130-9299-33af-b2e1-5fcc40a2a7c3 | -17.1621 | -57.472 | 2024-10-13 01:41:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed9b7ef5-39b6-3052-8c74-c57ffe07d8f3 | -17.127001 | -57.455601 | 2024-10-13 01:41:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2cef071-34bd-358a-9dbc-feec3f69dcd6 | -17.129999 | -57.4678 | 2024-10-13 01:41:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6390d47f-e1fc-3ff7-b69f-73f93dd8cbb0 | -17.107599 | -57.460899 | 2024-10-13 01:41:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c8319e2-17a7-3fad-894e-06d28e6202ee | -17.1106 | -57.473099 | 2024-10-13 01:41:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99cb8cec-12db-3e2c-8684-fa2dfe46ab09 | -17.0979 | -57.4636 | 2024-10-13 01:41:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b403d928-bb36-33fd-a34c-a1a088ec58b3 | -17.100901 | -57.4758 | 2024-10-13 01:41:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 289f746c-8b7b-3190-a48a-07c4eecee61e | -16.9951 | -57.426201 | 2024-10-13 01:41:47 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b047401f-f4a2-33b6-9d67-2566c2128b9d | -16.988501 | -57.441101 | 2024-10-13 01:41:47 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6075a926-137b-3865-b568-dcb52e74b3e7 | -16.9916 | -57.4534 | 2024-10-13 01:41:47 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05febc59-c414-31c7-95f9-18acfe2028fb | -16.994699 | -57.465599 | 2024-10-13 01:41:47 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11730c27-397b-30d5-86aa-4cddd44a002f | -16.985001 | -57.4683 | 2024-10-13 01:41:47 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d139f77d-b57e-3467-bd6a-66baa2e04989 | -16.9753 | -57.470901 | 2024-10-13 01:41:47 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae77b036-0c8f-3219-93c3-6669b61ca09e | -16.978399 | -57.483101 | 2024-10-13 01:41:47 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README23.md)
