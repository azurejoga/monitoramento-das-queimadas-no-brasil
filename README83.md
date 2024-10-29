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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d84f7880-0a4c-3aa5-93d3-99cc28d80f10 | -1.28767 | -54.67052 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0541bda-3e2a-34b7-9881-eb85c0e3abfb | -1.2774 | -54.13285 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e52035-751c-3bd9-a5d8-1a5eb23a40e7 | -1.2656 | -54.68118 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0799603-2e8e-3ebd-92f8-c1da70cb9f84 | -1.25735 | -54.69049 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b845b880-b789-3d03-b398-71627a90010d | -1.24138 | -54.53292 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb88bd2b-1f1c-3edb-9f4c-3f641c08afb4 | -1.21005 | -54.17184 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3778a00f-1c0c-3738-955b-e15c6c6638f4 | -1.20951 | -54.17529 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82464906-6185-37f5-b5c4-5afd5d7f3414 | -1.20844 | -54.52779 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 354ccdbd-fa09-3899-9afb-02104e553f37 | -1.20673 | -54.17131 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7d789b5-7206-380c-a6ce-58e5d9ee6987 | -1.20592 | -54.08991 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f7e399a-871a-3c3e-9f7f-85349f680c23 | -1.20566 | -54.52383 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba9701c4-9c4c-3d7b-98a9-a113b7405cc0 | -1.18133 | -54.1815 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e269674d-fa70-3ff6-a091-33eec4a956f3 | -1.18079 | -54.18494 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a66caec-a808-32c7-b257-5c12eb17022e | -1.17801 | -54.18097 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a04aa7b-fda0-3ba8-b7e3-855810ba7439 | -1.16954 | -54.08789 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 036b0ab4-e09e-35d6-b4d3-8cbf885197d4 | -1.16697 | -54.18631 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16606d6b-9dc7-3da5-9690-7bc11e99df84 | -1.16643 | -54.18976 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2c390fe-fc5a-3f7c-bb61-2c92e39b32c2 | -1.16365 | -54.18579 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26757786-b000-3d8a-8caf-e85ffcb8090b | -1.16311 | -54.18925 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb3293f2-1169-3e0d-8234-f054945559f4 | -2.02509 | -54.92728 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 624431b0-a552-3fd9-a00e-aeefb0d495c1 | -1.96147 | -54.04062 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0c8d550-692c-3cec-88c0-7eca4028d347 | -1.20046 | -53.52241 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7e191da-801c-319a-adf6-aa1c01e888a0 | -1.19991 | -53.52592 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19975fa4-40bf-3c33-8efd-17560c656170 | -1.19656 | -53.52541 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 257ef613-4dce-3413-b430-7cd09b179c5d | -1.1859 | -53.50586 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 000ce36d-267d-32a7-bc1a-9082674ed5cd | -1.18566 | -53.89915 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58be312c-6496-3187-873b-44f65b559970 | -1.18535 | -53.50937 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2be5494-52d0-3316-8722-365c07e60595 | -1.18403 | -53.90952 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c659d04-7b93-3a6d-b625-d699e84567b6 | -1.18255 | -53.50536 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93440964-6358-3e96-85fa-044de7fcaa7e | -1.18179 | -53.66325 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62b9e5ef-cee1-3b2b-8fad-1d0e19590bf2 | -1.18124 | -53.90557 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d16c1441-f4d0-3408-948f-69e8f0ab89d6 | -1.1807 | -53.90901 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ed5f8f0-24a1-3849-9112-49a059ecb510 | -1.1792 | -53.50485 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 339b2205-6637-318e-bafa-586599d8407f | -1.17866 | -53.50833 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74fe072a-1100-309d-bfa8-a4eed61761c3 | -1.17641 | -53.50079 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fc0f604-2386-3127-bcbf-7c99d7a9b920 | -1.17585 | -53.50433 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f66e7768-2b1a-3252-a521-4d75664f0372 | -1.17306 | -53.50027 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a2f30c0-157d-3a92-9bfd-a963cb42e036 | -1.17251 | -53.5038 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 302f52b8-8f5c-3846-8f7d-ec78f96b9c96 | -1.17124 | -53.66514 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd3b3979-c9f4-3baf-8738-351e83cadfae | -1.16971 | -53.49975 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d2aa6f1-e947-3628-ba51-577f3277ea1e | -1.1478 | -53.64008 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c89de5d8-a266-3eb0-bb16-714309988efc | -1.14501 | -53.63607 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c5350b-77b5-39cc-9fda-76bf648ab1bb | -1.14446 | -53.63955 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c0a450b-dae0-3fc5-8a9f-21d17d74e939 | -1.08482 | -53.65537 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a02cf3c-ff35-3f5f-8985-5feb837d0db4 | -1.08427 | -53.65886 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cab3646-ef1e-3e19-87d4-7a20c3427157 | -1.08372 | -53.66235 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7d0be95-42e9-3efb-a97d-d24df3aadf88 | -1.08318 | -53.66581 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be67913-e9ea-3eff-b250-a835dd7ef071 | -1.08263 | -53.66928 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb708b27-224b-3edb-9a2f-c9e4d7d1e55a | -1.08209 | -53.67275 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd6aa8a7-759d-3a05-81fb-a6f24dbb66f7 | -1.08203 | -53.65136 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1a14016-1f70-3bf9-8ce7-3a911a57e247 | -1.08148 | -53.65486 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a600b99-b3d3-3456-bace-cafee09be0fc | -1.08093 | -53.65836 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12b0da1c-462c-3d80-a02a-f6910fb785a0 | -1.08038 | -53.66185 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1983ffa0-5065-33ff-baf4-23987e5d2b2a | -1.07984 | -53.66532 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0b69705-c18d-3fcf-8462-ec01d947c899 | -1.07929 | -53.66878 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae8a7429-6691-3bba-b866-b38d90628162 | -1.07875 | -53.67225 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c04ed2f3-f020-30c6-9521-02147c43c468 | -1.07759 | -53.65784 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86e23926-ebb2-31d8-9a85-6c9945624c99 | -1.07704 | -53.66134 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdd1efba-b8fd-351c-84ca-62753fdb815a | -1.07481 | -53.6538 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e34b71-0b50-3789-bae4-ed8e30dbf3ed | -1.07092 | -53.65676 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 049f0535-a967-3a10-91d6-3545e756f5d7 | -1.06873 | -53.67073 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0d08587-989f-3244-8fdc-b7e010f5a35c | -1.06758 | -53.65625 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5d0f328-68a8-3274-bbd6-b56075dfa22c | -1.06703 | -53.65976 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4b2411f-ffe1-3449-a6c4-c0a8a38a670a | -1.06539 | -53.67021 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca7bdda7-c36a-3d75-a4e4-6e6495479557 | -1.06424 | -53.65574 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acdfd100-fc0f-360c-a6c1-257cccc12554 | -1.0637 | -53.65924 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82095702-b2a5-3b78-85cb-9ca47511a41c | -1.03979 | -53.51573 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef067202-2ca1-35fb-8a34-7ea364c5b690 | -0.9966 | -53.70266 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 927338dd-48dc-32e8-83c5-7d0a5a922e2a | -0.99327 | -53.70214 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0238aed1-ff63-3fd0-a448-9b1f45488dc3 | -0.99048 | -53.69814 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abdeb46e-5ab9-333f-bd07-2fd9185044e1 | -0.98993 | -53.70162 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d05f22e-f727-3a6a-87ae-142f4f227e60 | -0.98939 | -53.7051 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7727c2e2-2cbd-302b-a804-e834b896dd22 | -0.98884 | -53.7086 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 960ab820-55ec-314c-9ea6-2755d8f69409 | -0.98605 | -53.70458 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bf7ae34-f4db-3283-acf4-eb4062647de0 | -0.9855 | -53.70808 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c012440a-37b2-3dc1-a682-a45f7d1f0761 | -0.98495 | -53.71158 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e90b4b71-7add-3daa-ad34-ef28ede32fe9 | -0.98272 | -53.70406 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03f227f7-4081-3835-81ed-320177b778fa | -0.98217 | -53.70756 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cccc5646-46bd-32f6-8086-594402443a2c | -0.98162 | -53.71106 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c31d53f-4b5e-3318-ad90-53bb92f0b4ce | -0.98107 | -53.71455 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 177e60c9-7272-3266-9aa7-798bf275b37c | -0.97884 | -53.70704 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 773a904c-a20e-39d9-8626-48b92c559fab | -0.97828 | -53.71055 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 309c7990-b193-3ce5-b393-eabd3ef210ec | -0.97773 | -53.71406 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 393279ac-7d5d-313c-abeb-765c84949b5f | -0.97605 | -53.70306 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b06c4cc0-55c3-370e-b2db-afa414d1ccc8 | -0.92473 | -53.81252 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71dbd415-de11-37f4-9124-fc5d4cd39519 | -0.92141 | -53.81199 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0be35ec-f36d-3efd-b927-42df56717cf9 | -0.87688 | -53.68692 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54adbada-db09-3544-af87-b222dd8f92ad | -3.58941 | -54.663 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb5fe352-6df5-3c76-8ba9-6ef09eb90edc | -3.58845 | -54.56355 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e65756b-c6d8-3695-96db-d7c76ea758a6 | -3.58791 | -54.56702 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e82a74f-c6c8-334c-8c3c-1277d468948a | -3.58662 | -54.65902 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 691151d4-d45e-3973-88f7-09401866618d | -3.58608 | -54.66248 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37bf6671-4d54-35de-af10-11d615d84363 | -3.58276 | -54.66197 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc0bc7c2-c958-3bfe-b6fe-4efbc8d800b9 | -3.57048 | -54.6778 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56b7c3e5-c3e1-33e7-b837-af03f188d482 | -3.56825 | -54.67036 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00d6ccbe-7ce5-37d1-8b31-9d2e92297c52 | -3.5677 | -54.67382 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9283572-781f-3e77-9cbc-c09bbff324a0 | -3.56716 | -54.67728 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc69cb42-05d9-3265-9269-88ffec64a2cc | -3.56661 | -54.68074 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46f1cb4c-62d8-358b-9d6c-9da935709bb1 | -3.56547 | -54.66639 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0daccd18-f8f8-3fec-aa6e-bf615261b9a2 | -3.56492 | -54.66985 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README84.md)
