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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2708df1-b89a-3047-9f0c-88727010ad96 | -10.68816 | -56.55952 | 2025-08-19 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98fe6e45-5485-39d8-bc81-c8805196f9f6 | -8.82153 | -52.063 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4ad78f0-45c4-3ab8-86f7-330f7a0aa3a5 | -9.17989 | -59.64287 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0e09cf37-7984-304c-831d-8e9c721a0dcf | -11.86721 | -51.57742 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0808fad4-b978-3bea-87f2-38edd673f817 | -7.14623 | -44.20988 | 2025-08-19 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29006324-7995-35c5-b8e6-a878e4788f96 | -6.63408 | -55.27483 | 2025-08-19 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f72b81af-2c76-3f37-acf7-cc52ca07b771 | -8.81533 | -52.03662 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39f39473-a8d6-3eb9-96ed-e9d8d2f00d48 | -12.64679 | -45.8173 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77b78070-c042-3bf3-98fc-670810117859 | -11.4527 | -47.32174 | 2025-08-19 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc0a5df0-0436-3446-80b7-ebcbeb19011d | -9.51921 | -60.51579 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82f3c8fd-e4da-321d-8248-0638a35856d1 | -6.11523 | -53.87087 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963030ed-4ca4-3fae-b45c-bd5f22ad6b00 | -11.57868 | -44.85316 | 2025-08-19 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e582f459-0a4c-388d-8214-5b108d17a067 | -12.49605 | -45.56775 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89b4f147-69eb-3be3-b222-654dda4fc27f | -9.51287 | -60.5322 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3081f0b-7e02-3c6d-92b5-2ed7e987e573 | -12.73379 | -45.05322 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c10e566-5f77-3087-a147-84cc2539c802 | -12.99404 | -45.18922 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f4f7978-f1fa-3717-8ccb-050a55538836 | -7.13671 | -44.61024 | 2025-08-19 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ea953f6-b941-3f27-a435-d409c9b9470f | -7.14248 | -44.60528 | 2025-08-19 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ccefd5d-8b3e-3199-9279-13c30df065b5 | -9.11523 | -60.3303 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10ae98cb-3c4d-36f5-88f3-260bb38ec6b2 | -10.0834 | -46.36416 | 2025-08-19 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a5a7e03-c008-3cdb-b96d-8bd6ffb24ca8 | -8.40107 | -49.50245 | 2025-08-19 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20e785a1-200b-3596-9cd7-3a1b4359e104 | -7.14325 | -44.59985 | 2025-08-19 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6e82df8-7e53-361c-9194-cfc270115df4 | -11.77113 | -51.74596 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a37f29c-539c-34e8-b0df-7f868f98f744 | -7.78714 | -66.95527 | 2025-08-19 04:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ea876d6-12aa-3cbd-8c76-61e1d3b9406a | -8.82538 | -52.03822 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59a4a06d-7605-3efb-a91c-7925dfdbfe38 | -11.85913 | -51.584 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0e42cee-a470-30de-8652-a7d97ec0fbf4 | -11.35843 | -55.38975 | 2025-08-19 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b15faa74-f188-3e3c-a7be-c086aa62dec7 | -12.04222 | -44.01319 | 2025-08-19 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13d981e2-017c-3089-83c5-8fb09d0a83fd | -7.5891 | -45.4305 | 2025-08-19 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46ae7896-4d78-31d2-bb40-8bb214389f54 | -7.58548 | -45.43155 | 2025-08-19 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9d94f10b-7221-3d94-b59d-d75b2d94e613 | -8.97244 | -60.50296 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d90e10e-a707-3027-8820-bfa0d17b2fe3 | -9.04073 | -50.17785 | 2025-08-19 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d1070f8-f1c7-389f-8f1f-7069a4ca13fa | -6.13457 | -57.93172 | 2025-08-19 04:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69a2230e-4bac-303d-9119-d15a51e7e42a | -7.25483 | -50.17655 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95f8bf62-f121-3221-9b77-8089433864b9 | -7.59932 | -63.4489 | 2025-08-19 04:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce601126-29f3-3b09-913c-1d1b126b37b0 | -12.77693 | -41.24954 | 2025-08-19 04:53:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9f43b157-30f1-302d-8dc6-9ec179703c5c | -12.04183 | -44.01212 | 2025-08-19 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c597ac3-fa34-3dce-b649-8ba6e3cab814 | -7.13825 | -44.59939 | 2025-08-19 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4591187-296c-3ede-8373-cf487fe2018c | -9.34102 | -48.51262 | 2025-08-19 04:53:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33d4ff39-11b5-3ebe-b380-7ac35a34fb99 | -12.9973 | -45.20569 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7855759-fc24-3dae-b6c8-05b1e238cd8f | -8.87947 | -62.39823 | 2025-08-19 04:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80fa8b36-7654-3b38-bdc1-aa075fe514cd | -7.79294 | -66.96409 | 2025-08-19 04:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 242b6268-80b6-357b-9b15-194f6981cf2f | -12.9925 | -45.20185 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9eddc83-a3f5-33cd-ac6a-ee4a531dcd0b | -8.22515 | -47.2904 | 2025-08-19 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e89812de-25ea-38d8-adac-52a7df7280e9 | -11.86317 | -51.5807 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c088b576-ef50-3ed0-8a7b-5c4243e78852 | -12.91975 | -46.10735 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dfd84c1-308e-3fc1-89ac-4da673956257 | -12.99691 | -45.20884 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fe1a7ef-252f-3389-9972-6bfc6c2ce38b | -7.29283 | -43.69 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79e817f0-d59b-3f1f-a67a-774e6dd245f1 | -12.99327 | -45.19554 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 894a0ffe-6e83-37de-b584-d7a94808b894 | -9.51655 | -60.53091 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 760bfb05-e0c3-36e2-a292-3a4bc6f0c7ea | -10.03628 | -59.35945 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59f476a7-cf51-3d10-91d3-47dc2f04cd75 | -7.9298 | -63.29425 | 2025-08-19 04:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57910dc3-8b1a-34af-9800-35d914cc5b27 | -9.18884 | -59.64418 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 892c5364-56f7-3a08-b4e9-a941dbb54569 | -9.24003 | -59.64019 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 861644d6-1d81-3c9b-8260-015886420099 | -9.51379 | -60.52719 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3b912fc-5a9f-3022-a48a-f5aea3c16d7e | -7.30297 | -46.28938 | 2025-08-19 04:53:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6d6e0ea-0706-3423-92b1-5d0500254b08 | -10.5056 | -54.63541 | 2025-08-19 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d1b2cc6-4e91-3b00-b7a0-f701f92902e6 | -9.15128 | -60.82555 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ad74c6f-9b2e-357f-bdc8-320edafeb0cc | -6.13393 | -57.93553 | 2025-08-19 04:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07762939-fbe6-381c-a925-f45cbf3531a9 | -7.25602 | -50.16873 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35464ddb-bcef-3b92-b1c9-e310bf6ec218 | -12.5075 | -45.59894 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae811b4e-f164-3ab4-993e-feedff90e5c0 | -9.17464 | -59.64653 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd5ec306-325d-3063-9081-ec97887e8241 | -8.62285 | -62.61941 | 2025-08-19 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ece1fdd-3bcf-3ace-8534-03c7abce7921 | -8.70401 | -50.6888 | 2025-08-19 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eba1f64-917b-3346-955d-ce203890e56a | -7.14864 | -44.1923 | 2025-08-19 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8f37abb-0faf-3a7a-bf58-7a7ec1e90652 | -9.1791 | -59.64729 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72cdceec-406d-30a7-be0c-6ec79a960428 | -9.71775 | -51.97459 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4a136efb-bacf-3ae1-9a23-027c22c09075 | -10.10996 | -57.76315 | 2025-08-19 04:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa22cb45-e218-3ab3-999b-82d9730e3fd6 | -9.22883 | -59.65186 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5dceb0b-7192-3035-b016-c31e0de16168 | -7.97148 | -55.30363 | 2025-08-19 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a92cc4ae-12c2-384c-b933-6f2c4d34e6a3 | -12.03622 | -44.01605 | 2025-08-19 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0a41cf9-fff9-349a-a695-649b566eb76c | -9.34423 | -48.51825 | 2025-08-19 04:53:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f52f0ffd-4d80-3846-9215-b3a6f0735619 | -9.11792 | -60.32776 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e275967-1835-33c8-aaf6-54afe6982dba | -7.21841 | -49.60455 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a00f2fb-de4a-324c-81dd-41cbe0233402 | -12.63659 | -46.89022 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 199f5769-6406-3bdb-b85e-4f1df28463fc | -9.07519 | -60.42041 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9807b946-66c2-3ff6-9ffc-e7617a86230b | -12.64053 | -46.89572 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11fffe75-39a6-3f57-be35-f9e9b7785200 | -12.63593 | -46.89511 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fea63151-9fda-3183-8bf2-824bb012e26e | -8.71435 | -47.86009 | 2025-08-19 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ffc92c6-88a8-3d35-9a02-fc2fedd5507a | -7.29719 | -43.69738 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b06034a5-720a-3e2c-bb8c-15b08cf406fd | -7.29614 | -43.69168 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c83f6f1-b4ff-391f-bc4c-66175d805615 | -9.0743 | -60.42542 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fbc97b0-7125-3c78-af37-cad70718a83f | -6.11862 | -53.87142 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb5a692e-d0c6-3d38-a4b1-d94bc20b36d3 | -8.40266 | -49.50034 | 2025-08-19 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31e63436-d2ca-3cb8-9756-bd50bcd071af | -12.63203 | -46.88929 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa6b564e-ffc8-3686-a8e3-b96662fe5c17 | -9.51479 | -60.54095 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8430be0b-8e62-37bc-953d-8add5480acbe | -13.00288 | -45.20321 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4299049-7ef6-3c80-b070-ab59741b9ae1 | -12.95785 | -46.15684 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c599bc8-b158-3231-8121-913b417b0e1b | -8.81873 | -52.05897 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d2e3e71-4d48-33d3-9100-fe1a79ef496f | -13.00327 | -45.20005 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93a5c91b-29c5-3b81-8fd3-a563f846c489 | -6.19259 | -53.51938 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeece4b9-95c7-323a-8b25-4a75dd17b5ee | -12.65903 | -45.80926 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 589c455e-4171-345f-8295-067d3acd08dc | -12.63532 | -46.89156 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19d0028a-35bc-3c87-bcb6-4dbcd0b83d83 | -9.71156 | -51.96994 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd3ea44c-e3a4-3ea0-b8e5-a07c2e82458a | -6.63231 | -55.27737 | 2025-08-19 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 025ca8e9-7e51-3675-b08f-7e3abf59e42b | -8.77108 | -50.02225 | 2025-08-19 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c03d12b5-eb23-3b07-b1ee-40e741f29502 | -8.22571 | -47.28649 | 2025-08-19 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6adf1e69-5e16-3980-92d0-3ef6a605d192 | -7.3074 | -46.29 | 2025-08-19 04:53:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2571d90-329d-3d88-b667-446b1365be3d | -13.46856 | -47.05815 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4df7dddd-d72c-3f2a-b0c3-8c1d7f1d924d | -13.15124 | -54.91498 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README41.md)
