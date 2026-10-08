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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0031a78-dafb-3d64-8c54-83bd3e20590b | -2.9884 | -51.050598 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51471a2-0fb5-3fee-9214-c4b890ade96f | -7.4682 | -42.8633 | 2026-10-08 00:26:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9fa7bee7-d9eb-3519-a95e-acb0b5ed4ec4 | -6.7113 | -55.043999 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72bd826-0768-35a6-8aab-37ad4acd8625 | -1.3624 | -56.9142 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad0d9cb-a61a-3eca-91cd-a6c165be7b4f | -2.9994 | -53.894699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb536b4-824c-39c8-9734-1c86a91b9d98 | -6.8856 | -43.717098 | 2026-10-08 00:26:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e53617ab-9c04-3b4f-b227-6fa9a42ee28f | -2.8891 | -54.181301 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de4bd60-591d-35d6-afa7-94a6343b438b | -12.1916 | -48.417301 | 2026-10-08 00:26:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 556929e8-7c40-3ee7-900c-050c65132771 | -3.174 | -58.613499 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1cf3372-0726-3414-a08f-ba5033039dc7 | -2.1265 | -56.692799 | 2026-10-08 00:26:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90b32891-41be-3545-b26f-24d1872eeec6 | -2.7954 | -54.086102 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93f12807-d40d-3383-9ff2-79efd4b033e9 | -3.5148 | -54.531101 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d9dc838-fff6-3023-9f66-996bc32ae9d0 | -3.0104 | -54.125198 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ca6e93-ca8a-3ba2-8b39-5b7bc8e79bc7 | -3.0088 | -54.118301 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36cd677-17c9-3daf-927f-ebf5a7a45b5d | -3.1 | -53.747601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03eb63f2-2692-3461-a3b8-61641ee4490c | -3.5425 | -54.653702 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1ab687b-d53f-342a-b83a-77270e85c761 | -6.2038 | -52.841099 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de202eb0-44d5-31f1-81d6-834e5d784eb1 | -6.1707 | -51.931099 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2162d59-ea08-3a94-a8bc-170f317e3ef6 | -2.9794 | -54.124901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da310908-2351-3f99-b375-a0fb16fbc9fd | -6.336 | -43.322899 | 2026-10-08 00:26:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c04e7e58-30c7-3738-97cf-78c97a904f7a | -5.2371 | -56.097599 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce70630-d4b6-39b2-bee0-d9a3fa2337d1 | -4.5908 | -54.914501 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9b34764-1198-33e5-b4d2-08f2a02d1da3 | -1.1032 | -54.171101 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c233e63d-426a-3fc4-93dd-86ffa60f3383 | -13.7061 | -49.088501 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f70aaa22-3d09-3411-83c9-19306af00f38 | -3.0633 | -54.221901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d633ed85-81c5-3012-8724-ae37aca79f01 | -4.0422 | -54.219601 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9883471d-bfe6-36a1-9c82-af026b264493 | -3.2256 | -54.301102 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a58228f-2fee-3202-a82e-4f530ffeee6e | -3.0446 | -54.139301 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de2fe72e-3752-348b-b4a6-8d7e6b1753d5 | -4.1052 | -54.406601 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3a2eed-de48-30ba-94f2-89590ce2d2a9 | -3.0602 | -54.208199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9251455c-acc0-372f-88d5-0ed4e6cb35c7 | -5.9642 | -55.341499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57012e8a-0d4f-30a8-bebe-b15a25f36591 | -2.7725 | -54.076698 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab2a881-ee54-3272-9c70-b86795e226e1 | -6.1614 | -52.655201 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d085ff54-a9db-37ba-bb51-2d7fe84ace68 | -5.9875 | -55.676701 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcead844-4bf7-3bf5-b839-3a0d45425eeb | -2.8428 | -54.068298 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaa7debf-0507-306f-82c0-f016a51a7683 | -2.4898 | -56.109798 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c179cfb-53e7-30cc-8d96-61c6d1dadf9d | -3.0398 | -53.936901 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaca90a8-ed65-394a-85a2-ec8572b062be | -3.5973 | -54.577099 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 314e2c54-f2f8-3a97-8fd8-0842a52cfd5f | -3.3001 | -53.8568 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74b00872-92c5-3155-a553-5b740d0fe900 | -2.7907 | -54.0653 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4ed40c-7d8f-3e98-a032-5f544e9f93d4 | -6.2006 | -52.782001 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa4d65f7-4a93-3e98-bca3-5dbb125ddcfc | -3.1313 | -53.703701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec566531-a120-3cd8-8f36-234ca36c642e | -3.0368 | -54.104801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aeb59d3-4c08-304d-82cb-7a54021437b8 | -2.8741 | -54.206299 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4471cbcb-6de5-3b45-b4f0-281e5b8c637a | -7.3799 | -47.602001 | 2026-10-08 00:26:00 | METOP-B | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c61e3eac-dd28-30b9-98bd-c4deca3e7917 | -4.806 | -54.680199 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a935360e-b387-349c-8881-452a8722a905 | -6.0842 | -53.494202 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d62c27cf-343d-36d2-a475-f925f2a6b395 | -10.9744 | -45.405399 | 2026-10-08 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e50c5ead-e07d-34bd-809e-03831f2d1018 | -3.2695 | -53.994701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a174d8d0-158b-38bc-90ca-26896471fd2c | -4.0538 | -55.321301 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f3534d-d4e7-3cac-a40f-595bb463f403 | -2.4655 | -56.0933 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 636b99d3-89a0-3ff9-a8de-34458b9a92e1 | -6.4787 | -55.2938 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6226447f-56f7-386a-a4f6-ef9d72f551fb | -2.97 | -54.0835 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1041f17e-000d-39d2-8d45-fb14c76e1a35 | -7.383 | -47.614799 | 2026-10-08 00:26:00 | METOP-B | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5218a3d4-1bf9-353f-a767-818d14d7b46e | -6.6814 | -55.094601 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 055ba1f8-44d6-3750-8e2d-e6601cd72985 | -3.5229 | -54.6581 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c58c654-735c-3ef6-b4c9-c3d3f8763c27 | -5.9736 | -55.383499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950c5f50-945e-3fc7-bf0c-9b8bddf88a25 | -1.8071 | -57.1045 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75f69ea1-65d7-376a-bd31-e5ff33fd3281 | -3.0237 | -53.911201 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee6a55d-4182-3c96-898f-59950fa6fd44 | -4.4518 | -47.9263 | 2026-10-08 00:26:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb040a6-2c60-3f84-8b64-5b7c385cd3f0 | -2.4882 | -56.102901 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70f5ee95-e275-3746-b722-d31fff7cc275 | -2.8726 | -54.199402 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347f17e2-2885-3dec-b3b8-bc56ef88bf96 | -6.7398 | -55.125702 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c82bbf1c-b337-3c76-bb20-3a01d677be30 | -2.9661 | -54.156898 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b476c26-78f5-3fbc-8176-dc282249238a | -2.8165 | -54.088699 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06549c7e-2614-3a03-9ef6-ddb67d7f1815 | -3.3681 | -58.192501 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbd8ecc4-acd6-33a9-9770-47ee6f1d8c88 | -3.1036 | -54.2635 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec38ce79-49b2-386c-99bf-91fe18cda16e | -2.9567 | -54.115501 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23dc12cc-1ef3-3126-8512-e35b7d2f998e | -7.885 | -54.997101 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32b24ec0-5d6c-39b1-9b35-7de0d7affb3e | -9.283 | -50.311298 | 2026-10-08 00:26:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f51e55ab-dc8a-34e9-a301-c4c49b4ca134 | -3.0489 | -54.022301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56aeedd8-87b8-3a6f-985b-33e717fb433a | -2.855 | -59.257099 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01140554-1570-36b5-a7ce-e52c85cee025 | -2.5012 | -56.114601 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3574f6-d32a-3e64-83c2-1c7076d7aefd | -2.9288 | -58.297501 | 2026-10-08 00:26:00 | METOP-B | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7833765-850f-3ec2-a05a-2353652bdf0a | -2.9665 | -54.1133 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa8d112-7dc9-3510-bac7-afcfe55ff63c | -1.4769 | -54.546501 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8790cc-0ac5-3612-b24f-6a00f0b2aeb1 | -11.3577 | -51.875 | 2026-10-08 00:26:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22382abe-5d1f-3827-aa82-87dc84a8bf21 | -3.5647 | -59.448601 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ada830d4-3860-38ea-a560-8c4363a669a0 | -2.9732 | -54.097301 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f4d1f18-e686-3cd8-a855-a93b13f9829b | -3.6776 | -57.043098 | 2026-10-08 00:26:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| babb666f-6b13-3eb3-b054-842f14989451 | -3.4126 | -58.900799 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d264d4a-56e1-30b0-b9a9-de1c12403ef6 | -3.0253 | -53.918201 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5dbaf99-217b-314f-b570-3426f4dd50e7 | -7.2017 | -55.118999 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 948cb073-bf80-3dde-81d4-0d5fcc05a092 | -3.1582 | -54.732101 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ace676-e793-3470-907e-079025496656 | -3.9768 | -56.2173 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb32eae-b34c-3f1a-8459-d534168a3ca9 | -1.5064 | -54.813202 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950a3ada-1be0-399e-9a0a-40e2e853ea2c | -6.1298 | -47.929901 | 2026-10-08 00:26:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 125ba17c-3334-3239-b8bf-cb1ab04b890a | -4.3537 | -43.816799 | 2026-10-08 00:26:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e4f542e-9dc9-3e4a-8242-77feb690c5a8 | -4.5841 | -54.930302 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fa93dab-3169-347e-8bcd-89e19c408505 | -9.8223 | -44.7644 | 2026-10-08 00:26:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67dda801-3325-3a3e-987f-1a3e874d8e54 | -3.0162 | -54.196301 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c102cef4-9a63-33f7-a94b-b3f8aa15218d | -3.6647 | -57.077499 | 2026-10-08 00:26:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c1ae646-da67-333d-be9c-3b1ba056ae21 | -6.2235 | -52.791698 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2ec5d16-fd2f-317f-8d35-14833d85204c | -3.7769 | -59.247898 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd22ad5-5c20-32e1-ab48-153ad6a5ce99 | -4.5231 | -54.979801 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 183bb2e9-45cf-342c-b302-2eefeeb3c1db | -2.9551 | -54.108601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca18bbf9-d35c-3022-9f1a-9148151db472 | -5.1138 | -47.123402 | 2026-10-08 00:26:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f525406a-8563-3d80-a9b8-dc30d9a59d39 | -2.8708 | -54.874699 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97276333-91f5-352c-860b-1126707526bc | -2.8934 | -59.199299 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 967051bc-b46a-3836-a4cb-6bc053bc6f37 | -3.0433 | -53.906898 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
