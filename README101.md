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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d7f78ae-cbe5-3a4b-b111-9170f525ea90 | -16.5779 | -45.11488 | 2025-10-01 04:51:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2235f0a0-666b-378d-800b-1618140228d8 | -9.5158 | -54.74839 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c039b93-16f6-37af-9999-2becdaed2264 | -11.16929 | -47.21423 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 492eb8a8-87de-34eb-b224-ddd9535a66f3 | -13.76822 | -47.9525 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e19d302a-5421-378e-981f-d6c5e4bcc6cf | -14.03397 | -47.99439 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee9500b-32c6-35dd-86a7-9d93d11c4130 | -12.89592 | -47.08367 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1745d6b5-775a-34bb-926c-9da5dc9cc421 | -11.63499 | -47.49127 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b03e01a3-75f3-374a-a4aa-0d3d2b005d76 | -14.084 | -44.09139 | 2025-10-01 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cac195b-7f60-32fc-91fe-c2426849ba90 | -11.16529 | -47.21357 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0b0198d-0f59-30ca-8cb3-75b0253c8abd | -14.50388 | -48.44771 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1858bf1b-62d6-3273-9bd1-424da033eeb2 | -13.33677 | -47.3388 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| adf5a5cf-4a0e-3be1-8319-6dee38644e44 | -12.24431 | -47.81378 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5d9f4fe3-b141-32c1-a12d-2d064062fc6b | -13.06999 | -47.08844 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 632f2965-3ecb-33ab-a2dc-c23895f8b125 | -13.32677 | -47.86296 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b8e74d0-5efb-33da-be43-f68d1b56a906 | -16.08776 | -51.02477 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 824186d3-52b9-3455-9b9e-ecbb6bc829d9 | -12.70001 | -48.56455 | 2025-10-01 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 213e7683-9365-39d1-aeb1-a770b4cf3cd9 | -10.06921 | -50.27538 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0377b20d-55f6-3cad-b793-cf0066dc59f0 | -13.3036 | -47.21114 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71696ec6-ed3f-3ad6-b0e1-84783c1719fd | -14.87872 | -48.32551 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4f1e27f-89d1-31f6-a2f2-50a7c5c993c6 | -9.40681 | -54.70953 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 492ae365-1d72-321b-90ed-3d1d8165c420 | -14.17508 | -46.1157 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 236f0a8f-622c-3d93-a63a-5dcaa829cd90 | -11.80016 | -46.61945 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 3712a307-ed6c-3107-bda1-6db6bd615c82 | -15.50379 | -48.55545 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0be71b7-c83a-3141-8327-de2eaa4b3345 | -14.04812 | -47.98044 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bb983f2-cec7-3dd9-90d1-2c2b83e540a8 | -14.17636 | -46.11331 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f4fe5ad-ea34-364e-b1b2-5866f7f72029 | -13.7803 | -48.0116 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ad612de-c854-3254-b322-a13e5180639a | -15.46323 | -45.8893 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 268d66c0-e631-3f7b-a1bc-7f845be37325 | -14.79961 | -48.32198 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 938a3a19-892e-3e8d-9a7f-2d50abea5ff4 | -14.98616 | -50.76915 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48f5684a-e9c1-346b-a74c-104316c3bd37 | -14.10157 | -49.74576 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17943625-0129-3b0e-bd4f-0924c3137593 | -14.54384 | -48.22079 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8397b291-c66e-38d6-bca3-d1f1bf33f194 | -13.76178 | -47.94024 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2b5522c-ea3d-325b-bea3-5b27819460d2 | -13.77464 | -47.96474 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9e23bf86-1c4c-319c-96b6-407e3deb3624 | -16.19306 | -50.00479 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48a2db4e-493b-352c-bd9f-5958280ace0d | -14.18856 | -46.11784 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c36036d6-ed1f-3eb7-874c-8e92bf88d1f3 | -10.81157 | -45.36037 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47433818-7e74-3218-9fc5-ba8c5a99fd52 | -13.21837 | -50.90118 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3503169-5870-3cf9-9ae5-d8c7b182a508 | -8.98711 | -50.19383 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23532f23-4bfd-322f-8c35-34b69c087b3f | -8.50709 | -54.59938 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38cc399a-3f7f-3fc9-bb98-bcaff8931115 | -13.79032 | -51.21836 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6646107-71a6-3f28-aefc-cbb46a343402 | -11.04849 | -47.82117 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 13ee2783-efee-3bc2-a2a0-8f4c5c480ef7 | -14.04958 | -47.97008 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c042d21e-2e31-3048-b5e9-9a3229ff45e8 | -13.23468 | -47.32908 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a2fc253-d7cf-3f10-9c32-869fbdc08b96 | -14.76781 | -48.09861 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec53577c-16c1-3d41-a155-514f8f96876f | -12.85542 | -46.8721 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 081b3a3b-cb7b-3cf8-9904-08bf80ccecad | -12.85331 | -47.01225 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 772eebce-a5fb-304b-8c44-0278828bd2f5 | -16.0162 | -50.90437 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a100aff-ab9f-3fb8-b720-1637c4907907 | -14.58111 | -46.36537 | 2025-10-01 04:51:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd1a4eb0-cad8-30ec-ab04-f2aeddb62e72 | -14.35527 | -45.91024 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f935e23-fed4-38b3-9cb8-e320e443a0c4 | -10.81217 | -45.3559 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 057f683d-319b-3a0c-a797-ec6bbc2331e4 | -12.84821 | -46.95634 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2e7e798-e7e1-3469-b672-f353c6175de9 | -10.07206 | -50.27961 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd3f715f-baee-3e9e-977b-54474404e11d | -13.17132 | -47.78585 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ac7bc77-122d-39ec-8ffe-5efda94b29ae | -16.3788 | -47.0177 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8782041-f946-3b35-b096-d98bf7c811c1 | -12.84755 | -46.86692 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea85f279-2d6f-3c5d-a5b3-fccb6c43d084 | -13.32759 | -47.82727 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ec80d63-c950-3dd5-872a-6ff595398cea | -14.73102 | -46.82961 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c3352f9-1937-3bf5-af9b-fa0bea10ce28 | -15.76391 | -43.73576 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05083587-e6f6-33a2-bfa8-f46614cbbc6f | -15.94126 | -48.12253 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 204a3bf2-c156-38ba-ab3b-7efa19f36f27 | -12.7709 | -46.89585 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 010309ef-4d99-3533-9349-3793b1d450d3 | -11.0865 | -47.83135 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 20d97fd1-6b87-3c45-b23a-8fae16a12e76 | -10.73291 | -48.17992 | 2025-10-01 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 949302e3-521e-35f7-a155-259c5a8f2170 | -14.51061 | -48.4859 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37ee722f-f7bc-3f2e-9f0e-4cd94f91b12c | -11.79632 | -47.6001 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10c432f1-bf84-3a72-acc2-4c8b876e3a40 | -13.36475 | -48.11055 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aced5e0-dd4b-3999-9490-040575ba1063 | -11.84407 | -44.9759 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7805271e-4244-3640-8550-db960cb9e9d4 | -13.13119 | -47.42321 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18c88dab-60b7-3ef9-b9fb-fd79e170811e | -11.16755 | -54.11651 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad09e9ff-0ffa-3d40-92e1-f554fd425ae9 | -14.59357 | -48.22866 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3ee6ee40-09c9-31fd-9fcd-5590670f55e6 | -15.49109 | -45.91079 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd98b642-8108-3e1e-b802-f49882ea7595 | -13.21273 | -47.33652 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d74d08d-7c72-379a-938e-1ffc4fbbdc1e | -14.96231 | -46.87375 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3772305a-744a-3cf8-a6d2-861806c22f15 | -13.37594 | -47.32852 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc245f33-d40f-3b1b-a5c7-a22b539ee05e | -15.53489 | -42.66164 | 2025-10-01 04:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2cc00831-dc5d-3bc1-b4ce-f38178fdb064 | -10.62494 | -48.59526 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cee63f4d-7fdb-322b-9fd5-5c9e605b1ef6 | -14.7554 | -45.76225 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22fc74e1-3d9e-3eb6-b5f4-c823b8074233 | -13.2955 | -50.66886 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62bbc1fe-39d2-3e3f-8d36-8ccff062bc3c | -11.46222 | -44.97279 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fc2f2ff-7780-375e-977d-9e07b55b4768 | -14.68195 | -46.96662 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbf06ef4-4c5f-3f2b-ae22-a6fa731c04b4 | -11.8501 | -45.00256 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e99e788d-c34a-3788-90d5-2845015f66a8 | -14.44637 | -46.35047 | 2025-10-01 04:51:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b34da66-ce57-3a78-9d08-78bb1b14b1f1 | -14.80023 | -45.80564 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a113a3af-79bf-3a3e-939c-96b125cb34f6 | -15.28002 | -46.41421 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee463129-df9a-36ad-9a0c-f4d2bcc8a4e0 | -11.33621 | -56.20906 | 2025-10-01 04:51:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e3ceed1-0fc7-336c-8a10-e9c996fb1617 | -12.88729 | -45.20217 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe49af68-643a-37db-8e24-7207887b9981 | -11.801 | -47.5956 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff7ffd6a-a4d6-374d-b172-6a6894da0be6 | -15.12764 | -46.4524 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdd0b158-6fe9-388a-9d33-502a68721557 | -10.63993 | -48.53313 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa0ff582-94a3-3667-a1d6-bb89dcba00c3 | -12.4691 | -50.2547 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8da363b1-b37c-3524-b81e-3e312a8dcf03 | -14.52298 | -48.36463 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 004a3826-6ed6-3c43-8ce3-0a56eed176b0 | -14.79218 | -45.79432 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e9391c3b-561c-33be-b646-3d38a74519c0 | -10.63471 | -48.53009 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0db066f-f245-3ccf-9e22-6a016dc925a5 | -10.91081 | -44.32611 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9b040ea-9a2e-3374-bb52-e85cc909dd59 | -14.96286 | -46.86939 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e87a4881-2a0d-3339-8fee-71b00645d0f5 | -11.52401 | -43.5592 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d763a83-c147-38d6-bed9-75dfb8b8db76 | -14.20125 | -46.09798 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bad8968e-daa6-34f1-8d17-7e2d89565faf | -11.63244 | -47.91058 | 2025-10-01 04:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e13e442c-c90e-36ab-8dbb-37b60ffea67d | -15.33992 | -47.9299 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4f93f1b-a88d-369c-8ce3-02d3f7b23d62 | -16.01619 | -50.87976 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6ca08c0-50d0-3a88-b172-7f8330b0539c | -14.1835 | -46.1214 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README102.md)
