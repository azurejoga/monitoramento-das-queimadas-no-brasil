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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1e559fc-e0e8-3944-8a55-47e86e944393 | 1.89504 | -55.86837 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0455a99f-168f-39c9-87d1-f107ecea7926 | 1.8945 | -55.86491 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8da658cb-f3e6-3d51-b72d-e4ba12de35c8 | 1.8901 | -55.85852 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a32bf673-438c-3e86-b7a1-c850aa4c58c1 | 1.79565 | -55.88016 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c0058f6-973d-3a4c-b0d0-1ed9b87b7723 | 1.79009 | -55.8881 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f7cd6d6-b725-3bae-ac23-daa2d18f2866 | -1.82669 | -56.73281 | 2024-11-03 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b17c37f-df5b-387e-acd3-c308616a4a65 | -1.80347 | -57.01017 | 2024-11-03 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fa41f26-1e57-3344-baf0-fe88a671d891 | -1.86193 | -56.82685 | 2024-11-03 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40b5fbfc-bb33-31bc-8794-b89124969aa9 | -1.28534 | -57.77346 | 2024-11-03 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76bad214-9866-3631-80d7-c3d394703dc6 | -1.28194 | -57.77291 | 2024-11-03 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2bb0b84-2bfb-3e55-9707-7091d9277cb4 | -2.78505 | -56.72712 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d0e7ab-5940-304e-8692-3c52a37a383e | -2.42505 | -56.95053 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c684ed8-53a5-3dca-8acb-dadd467a4d29 | -2.41354 | -57.02341 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59ba18ca-9271-3532-9e88-ad8c60d140a0 | -2.4102 | -57.02289 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 811b993c-5bce-30ff-9bee-2382e22bbe28 | -2.41015 | -57.5325 | 2024-11-03 05:08:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad69452d-d173-31e2-921c-2800c6cb84da | -2.40966 | -57.02636 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7639e2ae-f5b8-3fb2-b054-1b136c4a2a21 | -2.39753 | -57.08147 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 20d18592-7a76-355b-8978-a63afa0aec43 | -2.39475 | -57.07746 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd90a29a-3d92-3c92-a93a-e8b868be87b1 | -2.3942 | -57.08094 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1709a3e6-a131-30ed-ac24-679a9c3d6b60 | -2.35052 | -57.08134 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7509b47-7a8a-3e47-8650-36bcec3fc23d | -3.36787 | -56.85388 | 2024-11-03 05:08:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d25089f-51ab-326b-ab10-b9dc2aa7619a | -3.27282 | -56.89565 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e92bc23-eabc-34c0-9939-3adab0861a87 | -3.2695 | -56.89513 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032869df-40f0-3d57-8a8d-7487d443e457 | -3.25895 | -56.87579 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b6cd27-2d9d-38a5-8b9d-77c06dac66ab | -3.03922 | -57.04657 | 2024-11-03 05:08:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05eaa77d-d1c2-3c30-9e41-487f8704e3ee | -2.84474 | -56.88509 | 2024-11-03 05:08:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5f2b79f-fa02-306c-91fd-9fe6eb041421 | -2.84365 | -56.89201 | 2024-11-03 05:08:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8b92089-e1a5-363b-8d47-43a640ea10fa | -2.4644 | -57.38556 | 2024-11-03 05:08:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58eeb962-8fac-34cc-b854-88bbbcbe2d86 | -2.41351 | -57.53303 | 2024-11-03 05:08:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fb0aaf3-13b6-3a2c-a85c-88f772a17e54 | -2.40453 | -57.54615 | 2024-11-03 05:08:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 473726eb-72e6-3081-aca9-b9f9bcf56f5e | -2.20956 | -57.11662 | 2024-11-03 05:08:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35c23a3e-0840-3f43-9c3c-5177c9a426c5 | -0.58215 | -62.86021 | 2024-11-03 05:08:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95848307-c583-398f-98c5-d65a1c69d90f | -3.05651 | -59.83004 | 2024-11-03 05:08:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfb37dab-2c13-37b0-be61-adbb4996194d | -2.89727 | -59.17752 | 2024-11-03 05:08:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed2cdeb6-e593-3a80-b9b8-920b69e4c29e | 1.30151 | -59.40607 | 2024-11-03 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca6ad8e6-2ea9-3b9a-a636-41b0a4202831 | 1.30081 | -59.40154 | 2024-11-03 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69b67c66-c9e2-3003-947a-97c9342e62fa | 1.29704 | -59.40212 | 2024-11-03 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed42412a-fe5f-3308-9a71-746ef8277ef7 | 1.21055 | -59.56748 | 2024-11-03 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5947e07e-f7a5-3b21-9610-32f11ce01443 | 0.85319 | -59.77102 | 2024-11-03 05:08:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38f97b5-2f1c-34c7-8307-b82e8f012a62 | 0.85245 | -59.76632 | 2024-11-03 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 245c5761-109b-391d-883b-af20035d3e09 | 0.84862 | -59.76691 | 2024-11-03 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38ddd298-0625-35e3-92cd-e6a77672af5d | 3.44961 | -60.99296 | 2024-11-03 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37482305-4d52-37bf-ad09-c4a70cf1b277 | -0.58301 | -62.85808 | 2024-11-03 05:08:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abbe32dc-7db0-3d16-8d00-66ae6500a4e5 | -0.58291 | -62.85549 | 2024-11-03 05:08:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fedb64c-3b5e-341c-8955-927071bfc115 | -5.12946 | -43.04214 | 2024-11-03 05:08:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bc5d6a7-5c52-30d6-9e01-fa9147db921d | -5.12225 | -43.04086 | 2024-11-03 05:08:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7f1ba57-44e4-3f6a-855b-49e836a8128d | -2.98892 | -45.02099 | 2024-11-03 05:08:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81e313e4-6162-3dda-bf93-07ee4da5c732 | -4.98038 | -45.7317 | 2024-11-03 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60580f41-0c3a-3b65-b166-ff4bf852f0f9 | -4.97417 | -45.73119 | 2024-11-03 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76b052cc-0fab-3e35-bbab-95d71fc7af69 | -4.83726 | -45.99087 | 2024-11-03 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01d2a2ed-7d4c-391b-b0b2-fffba68cf4b9 | -4.83178 | -45.98603 | 2024-11-03 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015fae5e-1f7b-3663-9a9e-1b2d7c7057ea | -4.83121 | -45.9901 | 2024-11-03 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31a8425-c324-3a5f-bb11-4b8928cdf55f | -2.1351 | -46.48269 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1088ad0c-d08f-312a-bbe6-35d22c4652f5 | -2.13454 | -46.48632 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89886115-5ada-3563-aafe-d00c186ea408 | -2.10707 | -46.43966 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45809eb4-9562-3150-a9ed-2db56669ecb5 | -2.10649 | -46.4435 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e2dba09-2133-3dc9-b0b2-6d1e719fa8f7 | -2.0873 | -46.83041 | 2024-11-03 05:08:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df02a702-078e-3a65-b027-22dd184582e4 | -2.08341 | -46.63382 | 2024-11-03 05:08:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d4454e2-fca7-36cb-ac8d-664272d9a382 | -2.08181 | -46.82956 | 2024-11-03 05:08:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 640431ac-4b00-3985-badb-173bff840130 | -2.0784 | -46.6293 | 2024-11-03 05:08:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cb19c19-509a-352a-8617-2883cda3e93c | -2.07784 | -46.63298 | 2024-11-03 05:08:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce81d017-8881-39ea-a428-645a3dfb4d61 | -2.07227 | -46.63219 | 2024-11-03 05:08:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| befa208b-6138-34f7-90ec-91cfcfbbaaea | -2.01198 | -46.43721 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f1179cf-c807-31e3-b59c-4fecd2410a91 | -2.0114 | -46.44098 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34394462-a588-3a8f-a4d5-5742bbc8e2eb | -2.00578 | -46.44008 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8ce9e25-d167-3efd-ad16-fa7fca06e28e | -1.91235 | -47.09073 | 2024-11-03 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18181bbe-48ae-3186-82bf-6fc6ad4717de | -1.90696 | -47.08993 | 2024-11-03 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b06c4b9f-9b33-3bbb-a9bf-1d2aef6c36c2 | -1.90644 | -47.09332 | 2024-11-03 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f0578b5-7754-384a-a6b2-19a83013e3b7 | -1.87597 | -46.40548 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f98f93c5-a956-3a28-85c6-14be69c40c6d | -1.83624 | -46.55603 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cf5de8f-6931-3851-86ba-0c611701d438 | -1.57526 | -46.04161 | 2024-11-03 05:08:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9038c9cd-4920-37aa-a14e-ca4444e83e14 | -1.57468 | -46.04555 | 2024-11-03 05:08:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3a8da48-fc0b-3ef9-9c67-5bb239b28356 | -1.57461 | -46.04337 | 2024-11-03 05:08:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed1074a2-e0d0-3020-b5bf-89915b6984dc | -1.574 | -46.04731 | 2024-11-03 05:08:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36ed9328-8421-3ccd-ae7f-b0bf33792062 | -1.56948 | -46.03853 | 2024-11-03 05:08:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5426d2cc-0545-3615-93b1-f6070d5a24eb | -1.01223 | -46.86873 | 2024-11-03 05:08:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab9f3fdf-8cda-3546-9e41-223096f7f9c4 | -1.0117 | -46.87214 | 2024-11-03 05:08:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94796a1e-9b3f-3874-8cab-d45a5f2ab91f | -3.4501 | -47.48549 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f52c1d-1579-396d-83e0-f3e202107aea | -3.44961 | -47.48879 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a36c6d68-83f2-3f47-b8d3-ca51c1ae3f00 | -3.18831 | -46.25336 | 2024-11-03 05:08:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34f30dd4-1029-3e4d-9ef9-848c0e79d360 | -3.0132 | -46.56013 | 2024-11-03 05:08:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46cb8e3c-167c-38fe-9a73-4cdc2287a8c4 | -3.00808 | -46.55547 | 2024-11-03 05:08:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e76c166-2a0e-3c76-973d-555fabdae680 | -2.89048 | -47.34715 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9054088f-4d46-3ffb-bf04-76782097eed6 | -2.88512 | -47.34624 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9d61870-ba1e-352f-9cc3-4250ee139570 | -2.50476 | -46.70693 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e87330bf-29e7-3df1-aa25-b890c324eab5 | -2.50421 | -46.71061 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 631b4439-f329-3436-8fcc-9debd0399495 | -2.50365 | -46.71427 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 948a8fb2-f464-3289-b5e5-4bf902e3123c | -2.5031 | -46.71792 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a860527-3e10-3132-9d23-72d6c82fb0bd | -2.49809 | -46.71338 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3da41bf-e927-3036-a049-975a96c430a6 | -2.49754 | -46.71704 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b995703c-0fa2-3967-8925-649c0787f32c | -2.49643 | -46.72444 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bb1c90a-9115-3042-a5a3-85a64f179616 | -2.49197 | -46.71619 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5aa4b0f-cb8b-371e-bdd3-2b73233200cf | -2.49086 | -46.72356 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eed03fa-a90f-3b8a-88ed-358760581a80 | -2.48585 | -46.71901 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6965c8c8-c9ab-3017-bf25-b07cb5639884 | -2.4039 | -47.26577 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 716b21f4-024e-3da1-874b-95191e1b01cf | -2.40339 | -47.26914 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ae371c2-f0dc-3cef-ac58-ecc6787b0cb8 | -2.40288 | -47.27254 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a8b02d6-eeb0-372d-9f38-721ee4db7fde | -2.39752 | -47.27171 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ec6326-766a-36f1-9f98-2fe1464407de | -2.39702 | -47.27505 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d03b6bf4-3c10-32ae-9111-9a9540298b0f | -2.39174 | -47.237 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README74.md)
