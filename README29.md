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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23c86e34-2d09-35cc-a315-614f0b727b6c | -19.4109 | -46.39822 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04253314-f870-31ce-a326-e0e83cbe7e8e | -15.52185 | -42.65635 | 2026-09-21 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 5b4dd5d2-540d-37fb-bd3f-7f860746e141 | -15.45955 | -48.46841 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7817b444-27af-3c9a-968b-757eec493a04 | -16.01531 | -52.53606 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a5ef923a-af2a-3e07-a2c8-86b502505f7b | -15.96679 | -50.11565 | 2026-09-21 04:04:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90c3e925-b9ac-321b-a9f9-34be3addefbd | -15.45362 | -48.47008 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07909e26-dc3e-363e-ba7d-b22bb29a45c2 | -18.86498 | -42.00497 | 2026-09-21 04:04:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 40c3fa15-1b7a-3d26-8380-da5b773a4e4a | -14.7622 | -48.43539 | 2026-09-21 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 60f070ea-2473-331b-938b-1f1bf5c9c1bb | -15.97059 | -50.11455 | 2026-09-21 04:04:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bf258fb-4486-3dca-9ad6-88a8a53451bd | -14.92824 | -49.89818 | 2026-09-21 04:04:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e06751d3-585a-381d-bedc-2a820e19a71e | -16.03564 | -52.50914 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b9346414-76f7-3153-a5cd-87ddf103fc4c | -19.41335 | -46.40898 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f39829a5-3537-31b0-a20b-19a8b2922848 | -17.22747 | -51.76648 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f73a5d4e-d467-37c7-a2da-0c86a182b1b0 | -18.97934 | -43.75788 | 2026-09-21 04:04:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 199ac24c-8e7a-328f-95e6-d1d449efd32e | -19.11698 | -43.70424 | 2026-09-21 04:04:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08e0e3b3-a2bb-3ce7-8c9b-1c9e1cebe3da | -15.51813 | -42.65567 | 2026-09-21 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 6391ca16-7113-337c-8ce0-4285877772fb | -17.22886 | -51.7602 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0518e7a2-4ca2-3a62-9320-5fc135e80574 | -14.7582 | -48.42727 | 2026-09-21 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a10d08fe-4784-3b9d-8f36-cda2b82a6353 | -15.16902 | -48.16502 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac153ade-c75b-3585-b0e8-e3ceb06617de | -15.44756 | -48.47242 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a18ca423-a5de-3f72-be7c-3e46a58ee94e | -16.31718 | -53.84518 | 2026-09-21 04:04:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 239947bf-94fa-3f37-ac73-710858f2c16f | -16.04899 | -52.51279 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0f4899ce-9dfd-37b0-bd08-1bc6e1c8ca53 | -14.0357 | -52.07611 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e3954f5-24ab-3d70-90a7-6b1f9cbb2cb9 | -14.7955 | -48.52317 | 2026-09-21 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fda5f5c4-12e6-328c-9465-a732ce25637c | -15.52635 | -42.65263 | 2026-09-21 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 68a87814-dd04-3b0f-91f3-e774e2f5a57b | -17.58757 | -43.68708 | 2026-09-21 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86b4278e-9fec-397b-a1f7-bdb6e8fa34df | -16.04473 | -52.53157 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| dff4372c-99f3-3893-ab14-b4025b2f8a67 | -17.59138 | -43.68786 | 2026-09-21 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bec93ac-45ef-3195-aaed-6c0854133732 | -15.97839 | -50.10699 | 2026-09-21 04:04:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aefc4eee-cfee-39c1-88cd-44137fb53b5a | -15.52263 | -42.65193 | 2026-09-21 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 819ee951-c1d5-33f2-81ef-e34f2744ef7c | -18.03403 | -50.93342 | 2026-09-21 04:04:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f7117dc6-a8b7-32c9-877c-c41210053695 | -15.46532 | -48.47771 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec6591ad-a8ef-3b2a-b171-81382ec0fbd6 | -15.45484 | -48.47422 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bfe53546-108e-3abc-9ffd-98b4e75280a9 | -16.68093 | -47.88717 | 2026-09-21 04:04:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 170930f6-7225-345e-a2f9-f91f492dfbe3 | -15.45694 | -48.46414 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f886448-431e-3b92-932f-fe56990acff9 | -15.54964 | -42.62936 | 2026-09-21 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8413ac54-bba9-38ea-a352-429eb311ddac | -16.00997 | -52.52834 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 117b933c-3d9c-3f0a-bd79-c761fd751a4b | -18.03301 | -50.93807 | 2026-09-21 04:04:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2ed7149-e98d-3f36-8a47-c31e8039018f | -14.92202 | -49.89836 | 2026-09-21 04:04:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38e67215-c3d7-3e01-be92-5d4845ecb1be | -16.01666 | -52.53014 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab8a9b22-6e57-3171-b0f3-8c2e5319f329 | -15.44708 | -48.44703 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50864fcd-5202-3c0d-b73b-f152f4c9ead1 | -14.7574 | -48.43119 | 2026-09-21 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4f4671ae-6450-3daf-8689-a930e5fcb0ec | -16.03424 | -52.51533 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 26534348-1960-3f68-a084-30c06257ce2a | -16.04616 | -52.52527 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 4f595677-e546-3fc0-94cd-5609d404b6e6 | -14.05718 | -52.10814 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47c39811-9bcb-3c1a-b62b-394545b6fa61 | -15.45813 | -48.4755 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 072fdf06-64bc-3fff-8b9a-092c773b54aa | -16.02756 | -52.51348 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 691eb7c2-a83c-3b7b-9eb9-d4a0aa215668 | -15.45628 | -48.4673 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7665ab45-75af-368a-a5ad-38b27ee5aae8 | -15.44576 | -48.45354 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52a33998-7e8e-3be0-b8c7-11d5d82c1514 | -17.22273 | -51.76328 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f408c9a5-ab2d-3f1c-bdfc-aa72c167f8e8 | -18.78897 | -46.47016 | 2026-09-21 04:04:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fe3a8f3-50d3-324b-873d-7247164daa29 | -14.76298 | -48.43152 | 2026-09-21 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3aef89a1-1de1-3fd1-be0b-3152300fa33d | -17.22913 | -51.76439 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b0f8e3b-3044-3ae4-8ed2-539fe0f0ec7a | -15.46289 | -48.43555 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04658e02-1369-30ef-b03f-3c7a33766f15 | -15.46337 | -48.47724 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a200c8e-0d30-3c53-9488-510e417d5d12 | -17.23398 | -51.76706 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc4e8db5-2cf0-3a49-9d63-5b7e976a7434 | -15.4641 | -48.47359 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a77a2d96-309e-3732-9991-9fcd76894f8a | -15.45209 | -48.47771 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 703d121d-42ba-3b5c-9e15-64b4bdd7256d | -16.31061 | -53.84382 | 2026-09-21 04:04:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e07a5193-f2e8-33b4-9746-f1d8ddee1e79 | -18.9761 | -43.75505 | 2026-09-21 04:04:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 704dd31f-3c84-39d2-bfb9-21b0e6826ff0 | -15.46606 | -48.47412 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f8293cb-4d98-364d-887e-9de197c978e4 | -15.44643 | -48.45024 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f44169ee-beb6-3e85-a386-8acb232c9aad | -15.96775 | -50.11107 | 2026-09-21 04:04:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aea3e16-92a6-3fd1-91d9-46bfae699144 | -15.86159 | -49.90207 | 2026-09-21 04:04:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f99728-f74a-36c1-bebe-84acbd70d187 | -15.45288 | -48.47376 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02480d7b-d3f6-3896-92a9-1ac6dfc7b69c | -15.16372 | -48.16396 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a292a8cf-aaae-3318-b5b4-ebc466ec6786 | -16.31038 | -53.84174 | 2026-09-21 04:04:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 690ec7ff-ef98-3100-9415-460a16b133b3 | -15.46154 | -48.46896 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3b92b95-789e-3544-a6ad-7101c4a27798 | -15.97158 | -50.10999 | 2026-09-21 04:04:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5a9da15-86a6-3e93-bd0a-47b54d421ac9 | -15.46083 | -48.47234 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 79260f1a-a836-30e2-ab8f-882d064d4602 | -14.7566 | -48.43513 | 2026-09-21 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fd8911a-f559-3f8e-8389-ebba0467c453 | -16.84723 | -49.02869 | 2026-09-21 04:04:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2e35b54-47dd-3550-ae86-2f0933cb5d82 | -16.01446 | -52.53693 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3536a190-b512-35e9-a523-86b868cec4a2 | -19.1133 | -43.70319 | 2026-09-21 04:04:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfdfa7f0-62b3-3f9a-beea-1ceb6ca75ab3 | -16.05007 | -52.53932 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b484cf0e-4630-36b2-8af2-09060b4012fa | -14.05456 | -52.11992 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5aa4f357-d7bc-33b5-be4b-b0fde2ee3736 | -15.1624 | -48.17053 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40bf4bc5-6ab5-3414-a2af-b61ca3973a9a | -19.87274 | -42.63778 | 2026-09-21 04:04:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9c45cac4-a3d3-3f9d-87c6-8a4e6de77ff8 | -18.9765 | -43.75218 | 2026-09-21 04:04:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46bb52eb-c82a-3ef1-a2bb-981b4602ddf8 | -19.41606 | -46.3951 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a6c4b4c-8aac-3ee8-aa1e-526e8543b8e1 | -14.03438 | -52.08202 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06f600cf-0530-36cc-8a50-f50f812ec567 | -19.11585 | -46.67659 | 2026-09-21 04:04:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64f979d3-9bef-392e-b840-d711a99e37e2 | -15.45402 | -48.47817 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8cb2aa83-2005-3852-ae25-80d71ee08f68 | -14.05707 | -52.1079 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cfb98b2-9f27-3981-a47d-f8b7f6b7e373 | -15.46263 | -48.48096 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aaccf528-5eba-393d-88db-f13097b91aca | -14.05587 | -52.11406 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70dc6b2b-81ee-31e8-b6b1-9307e5528d1f | -15.51891 | -42.65125 | 2026-09-21 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 79632388-aa47-3673-87b0-cad2fd73bd24 | -15.46216 | -48.43907 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 608a1999-30bf-3283-a236-77711e6e7da2 | -14.17647 | -51.79143 | 2026-09-21 04:04:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ebe1664-8caa-3e5d-9247-857de293779d | -17.2753 | -44.51409 | 2026-09-21 04:04:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b82797e-bed1-32ba-a6f4-765ad525562f | -16.0476 | -52.51891 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 05b15474-a74b-3701-9e12-9577a3fc292a | -16.31919 | -53.83973 | 2026-09-21 04:04:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92c432cd-5f0c-3beb-ab40-bfd2839cd2a5 | -16.02795 | -52.50806 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abe9221d-375f-3a1d-9b24-d611f80f28ef | -14.05452 | -52.11971 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27b8484d-94e2-3ff8-b62b-ba268243ecb6 | -19.40998 | -46.40295 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a756aef-e6cb-3733-9cec-76095d5d7020 | -18.86846 | -42.0056 | 2026-09-21 04:04:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f7c2fc4f-626d-3730-ad6e-09b1e94fa66e | -15.8624 | -49.89825 | 2026-09-21 04:04:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef77fb56-4e57-3150-94c0-6912bb336e9f | -15.45887 | -48.47178 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 69e6b8cd-fe73-3157-8f48-6616518faf67 | -18.97986 | -43.75581 | 2026-09-21 04:04:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d52488a-019b-32cd-b01b-f92cd8a3cf76 | -15.45735 | -48.47935 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README30.md)
