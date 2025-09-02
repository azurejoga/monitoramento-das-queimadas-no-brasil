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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a1585b4-b155-3c84-96ad-b9332a2a40a8 | -9.74065 | -48.97253 | 2025-09-02 12:34:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| a84001ee-99c1-3395-b03c-9cba0f8da4db | -6.19669 | -43.33561 | 2025-09-02 12:34:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f6d0978f-40d3-3a4c-971c-98c2641f0eb7 | -8.86129 | -50.58614 | 2025-09-02 12:34:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 75c877a8-edd0-3363-ad42-cea629f0f177 | -8.20918 | -49.5274 | 2025-09-02 12:34:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| c839e5a8-3945-38cd-b806-d61056f884b9 | -15.55499 | -50.39073 | 2025-09-02 12:36:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 78ffd018-5e77-3753-aca4-c7b8c57b476c | -15.23848 | -52.7333 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| fa03ddab-6de1-3fd9-bfb3-d13eb587d65b | -13.55646 | -46.97363 | 2025-09-02 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d931f221-1237-36fd-8c13-edcc319c8a1f | -12.32645 | -45.70422 | 2025-09-02 12:36:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3f1b2b40-9f9e-3cf4-b0ed-7a42adf83ef9 | -11.81496 | -48.35322 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e77b9067-8a91-366b-994e-079fa84388c8 | -12.65949 | -45.30874 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| fecb19ff-2372-3b40-8e1c-45729a35795b | -12.922 | -48.09061 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 07f68a76-0c45-3fa0-97d5-96ac708e0e8f | -10.43704 | -50.52206 | 2025-09-02 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d31bbc02-6e8d-3d6a-99b1-574fe14889c5 | -11.66044 | -52.15901 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 164e772f-5aa3-3173-8b21-d6349275cf27 | -11.82233 | -51.54765 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9f71409e-5339-3fe8-bc75-0abd7db0f353 | -11.67293 | -52.19752 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| abeb13c8-6ddc-3356-80d5-f9688e7e84f3 | -12.57904 | -44.79163 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| f95889d0-6622-3b99-9af8-c767b45c8496 | -13.54284 | -46.98849 | 2025-09-02 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 43.9 |
| a82768c8-c124-3a3e-b958-2d31f84cb658 | -14.99179 | -50.1903 | 2025-09-02 12:36:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 80fdeade-36e2-3bb3-92df-f814cad4edd3 | -12.63453 | -56.99285 | 2025-09-02 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 399b94a2-6a9d-3faa-b75e-1ee33057a35f | -12.03781 | -50.60062 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1232a699-be2e-3484-8f5a-d8aed79c62d6 | -12.78804 | -47.6495 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cb0166a6-ceb5-325f-bab0-be6efd5cb656 | -11.65914 | -52.16799 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ec495d47-da80-3fff-9ca2-df6f445240b4 | -15.24602 | -52.74372 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 787b2c3e-106d-3204-a97e-cff2051d6814 | -12.76958 | -44.78424 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 2ee1d513-cd2d-3e9c-bced-da3cda2520d2 | -11.42619 | -46.81976 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| af55e538-c343-349b-a507-af6c91d0a764 | -16.03244 | -48.0452 | 2025-09-02 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5e4ff043-5212-3448-8720-abef3f0b3c77 | -11.09645 | -44.6559 | 2025-09-02 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| bf124bcd-cd2a-37da-83ee-be4fc577f6f1 | -11.97701 | -45.88941 | 2025-09-02 12:36:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 73ca0074-92c8-39de-b8aa-adb4bc7508de | -11.64768 | -52.18468 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 93956380-b9c9-3e69-9072-41aad7023357 | -10.43834 | -50.51283 | 2025-09-02 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d9b26258-723c-36ca-b882-9a917d3693bc | -11.81603 | -51.52836 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f0e9b39f-05c1-3b20-a2ef-501d7142ac71 | -15.17263 | -52.34813 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 168fd11c-af8b-3f1d-9bba-39b152d0b295 | -14.98093 | -50.19935 | 2025-09-02 12:36:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 70976177-0fd0-31cc-a8d3-aa9756082aec | -11.10996 | -44.65765 | 2025-09-02 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5907b548-402e-37fa-8c14-57db3e37392f | -13.00114 | -48.10554 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 49949a1a-8707-37c9-8678-c10adc725314 | -11.85147 | -51.53351 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 5e1154bb-e656-338d-8c10-29ab9fbdf957 | -13.31953 | -51.77049 | 2025-09-02 12:36:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 99f5a60f-2f5b-3e5b-aae1-8efd3414987c | -15.48401 | -52.94745 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d64de05-675b-3c19-b08c-54ed250668d3 | -11.87175 | -50.60347 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a59a55d1-6148-3a42-8543-c92c46c88c2c | -14.31719 | -53.10115 | 2025-09-02 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2fd576ab-6a7c-3829-a125-63b6e61e015f | -13.35336 | -51.73507 | 2025-09-02 12:36:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 02e1a8d5-c49c-3fc2-a242-a2cf504b3f25 | -12.41557 | -47.78863 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| ddc75757-9f9e-3c9c-bae4-97ae0935aa0d | -14.58314 | -54.53869 | 2025-09-02 12:36:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd5b953c-a5c1-378d-a1cf-2b30b9aefcc4 | -11.9909 | -51.32869 | 2025-09-02 12:36:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b0d146e8-ff98-3831-a2f9-19e86ef1203e | -11.56605 | -47.60476 | 2025-09-02 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fa2b7c38-ceb2-3e29-978f-e8d0ab4e5d30 | -11.82489 | -51.52964 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c2fa840d-192f-3871-b34d-1b4f72c9592f | -11.98544 | -47.10168 | 2025-09-02 12:36:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0dfc12a2-9292-3a85-a040-8737802871c6 | -12.87407 | -48.04463 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5777355e-dfae-3cfa-a19f-c6c7037cb007 | -16.47476 | -49.53672 | 2025-09-02 12:36:00 | TERRA_M-T | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 1197cef8-a680-3076-8599-3d9aa49c0ef8 | -10.84262 | -45.03133 | 2025-09-02 12:36:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6c7073ec-c823-3f13-aaa5-32fdd36b5345 | -12.9204 | -48.10287 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 8f1206c0-44f6-36d5-b5bf-ce068fad5a66 | -15.78032 | -48.15075 | 2025-09-02 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2c82e343-cf27-3501-8141-8915a9787ece | -16.47631 | -49.5247 | 2025-09-02 12:36:00 | TERRA_M-T | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| e13d8f1a-6dce-397f-a247-60c6593ab070 | -15.15361 | -52.35463 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| b15458b6-e848-3f39-a167-7db97e900f2e | -11.65784 | -52.17697 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| afbe91c2-4d91-31a5-8297-1f30a67964eb | -12.58616 | -44.7978 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 03d5f26d-6c0a-3d9a-9bb8-bbe81c8bc878 | -14.71217 | -49.44747 | 2025-09-02 12:36:00 | TERRA_M-T | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4387432-2b43-3f4f-898a-dbb70c4789c3 | -13.72108 | -46.92754 | 2025-09-02 12:36:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| da4e4862-f2a5-3d1e-89d1-f0a55cafdd58 | -11.66538 | -52.18724 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 66c56f3a-fc2e-39a4-8630-033538e90c75 | -15.96666 | -52.21219 | 2025-09-02 12:36:00 | TERRA_M-T | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| dd2a5e39-21b9-3e02-b539-01567c8634ab | -10.8418 | -47.44765 | 2025-09-02 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 14a18062-e1ab-3fa2-b870-babe1d06e761 | -12.76697 | -44.80765 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5e8787f4-5b15-3c66-b0d6-d05204394b49 | -18.04369 | -47.74818 | 2025-09-02 12:36:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 12f3ed4d-91ff-3a3a-ad9f-4a522982dc25 | -11.91436 | -50.62862 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 12b9dae9-c8f6-328e-9519-386412a8df76 | -15.55993 | -48.36905 | 2025-09-02 12:36:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 4102663e-166b-34ea-86af-d12fc4ef0f32 | -10.34341 | -48.13652 | 2025-09-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e5db6c42-4934-3328-88aa-a0cf7bf6a919 | -11.66929 | -52.1603 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e9105b0d-2e04-3534-8b82-c63a55adb885 | -14.27705 | -51.64408 | 2025-09-02 12:36:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f0a54f18-b920-30ab-9718-442e72b7746f | -11.98962 | -51.33776 | 2025-09-02 12:36:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 41659aae-9041-38aa-8439-f70b4824dc68 | -11.85287 | -51.46008 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e512e387-793d-3bc2-856c-3c5c44058c63 | -11.82361 | -51.53865 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e6a95648-10a7-339d-b0d7-b6650324e07f | -10.26894 | -51.12233 | 2025-09-02 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8714a4f1-e300-3e80-9a4b-93e7a9f3071f | -12.21265 | -50.13018 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 771b1e27-ca13-3094-8fbe-6c4b6eff2f25 | -15.23717 | -52.74241 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 72fd4d65-792c-3200-b6f5-e3d8e913f29f | -11.94305 | -50.61985 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9384ed3e-d382-3b73-853d-42e9b7ae9c6b | -11.99979 | -51.32996 | 2025-09-02 12:36:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 280d9bf8-3f21-34ac-9196-9be7d80bf7f9 | -14.5935 | -54.57754 | 2025-09-02 12:36:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a8618bbc-6417-3819-945d-3cd3186a6c2e | -11.92604 | -50.61106 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 9c835c42-ba4c-3e25-8a9e-d7426771fc10 | -14.26905 | -51.17626 | 2025-09-02 12:36:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 689bf421-cd68-3b81-b413-bcefc2193bdb | -11.68178 | -52.19882 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| b403731e-df58-3549-b9de-8236d52a062f | -16.77841 | -49.23158 | 2025-09-02 12:36:00 | TERRA_M-T | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c0fc86d5-32ae-3d0d-8208-41d5a061ee99 | -11.94435 | -50.61043 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 73c4f890-dde1-38a4-bbf2-5182026a426a | -11.07085 | -46.91039 | 2025-09-02 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d477f2eb-3a83-3eb2-b2ed-6607bfdadd74 | -17.27888 | -49.2029 | 2025-09-02 12:36:00 | TERRA_M-T | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 8c06997c-cbeb-3853-99df-a45691213768 | -12.86358 | -48.04226 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| c960013d-4459-3e68-804d-f12ca8469d9e | -10.47341 | -51.62609 | 2025-09-02 12:36:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 55cdda3e-2e24-321a-8f9b-5840d77a8fd8 | -11.43772 | -46.81117 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| e5d9a528-00eb-341e-a385-4c9a9e6e49ee | -11.8625 | -46.71371 | 2025-09-02 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2430801c-51b8-3089-bfc9-ae7013127b84 | -15.1789 | -48.01398 | 2025-09-02 12:36:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 96755ab0-f117-3041-b2ea-67891e25b463 | -13.28828 | -46.82557 | 2025-09-02 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b525f81a-53d0-376f-b4e4-115f854b346b | -12.92698 | -48.09641 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 8e41c622-4e1e-34f9-9f28-7aed2e6ec667 | -14.26001 | -51.17498 | 2025-09-02 12:36:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 89749ae5-e935-3208-8e63-08e9821cbda7 | -15.12281 | -48.10867 | 2025-09-02 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1651b672-ce5c-328f-879e-07cf83457b50 | -10.8423 | -45.0457 | 2025-09-02 12:36:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a56ed1fd-32eb-3b44-8412-075335c1154d | -15.55356 | -50.40125 | 2025-09-02 12:36:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| b7e22af2-bb78-3be8-aef5-d46370af94a6 | -11.86173 | -51.46139 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 42c47f05-5ae8-3db6-8d83-1f68ff1794fa | -13.28064 | -46.8889 | 2025-09-02 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e3575d9b-a41d-383b-8c38-442431911f23 | -14.56352 | -52.99817 | 2025-09-02 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f2c6e13-8e4d-3e6d-a501-ca7df1c160b1 | -11.64899 | -52.1757 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 433fdc37-2a60-3c10-b5e8-ab068bd37154 | -11.37624 | -43.5597 | 2025-09-02 12:36:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.9 |


[Clique aqui para ver as próximas entradas](README92.md)
