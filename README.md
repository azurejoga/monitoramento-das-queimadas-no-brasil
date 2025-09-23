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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35b0a7ff-36f5-30a2-9782-d7801fb59062 | -12.7758 | -57.86 | 2025-09-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| ddd5635f-7f86-3688-9c46-66da46fe660f | -12.7755 | -57.8799 | 2025-09-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 1a3b84d9-5c48-3f87-b2c6-a0f31d12991d | -6.2596 | -45.341 | 2025-09-23 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 5b6d4dff-6671-38aa-88b7-a6e6f2471d0a | -7.8887 | -44.0281 | 2025-09-23 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 2836a00e-01fb-3024-9192-28c945cc6e6b | 0.1549 | -60.6772 | 2025-09-23 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 53bb3695-2200-3028-bdd8-dfff152466a6 | -12.7565 | -57.8815 | 2025-09-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 6e08d7be-e477-3e48-8c92-320a3671c286 | -7.8699 | -44.03 | 2025-09-23 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a7825c1d-9b2b-3c7c-8487-924bf8d359e0 | -11.6249 | -52.8416 | 2025-09-23 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 196.9 |
| a4ad73d2-f939-3f04-ad36-44c0bd1475ee | -11.6439 | -52.8397 | 2025-09-23 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e5266e9e-8134-3b24-a727-96ddd81aca1b | -10.9713 | -45.707 | 2025-09-23 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5e7fafdf-451f-3de8-a847-1c2fdd994d17 | -10.9522 | -45.7096 | 2025-09-23 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 6f09aba9-6b27-3b7e-af4e-7f38ab6cc6af | -12.7568 | -57.8616 | 2025-09-23 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 68e0bd88-4200-3456-9437-48e626a07e4e | -7.889 | -44.0049 | 2025-09-23 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 7eeebfbb-a23a-351d-8382-918095dfe3e6 | -11.6247 | -52.8624 | 2025-09-23 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 197.8 |
| a3a75fdc-3c63-3bab-a644-d04afdaf8a0f | -11.6436 | -52.8605 | 2025-09-23 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| e5c1e2ad-0f9e-39c7-a1a6-cd95ead57783 | -13.0235 | -48.7174 | 2025-09-23 00:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b7848fd4-b775-36f9-8ac6-d154c7cb7e83 | -6.2598 | -45.3184 | 2025-09-23 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| cb07c84c-dc93-36da-925f-9c92560d6d7e | -12.7568 | -57.8616 | 2025-09-23 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 26ab5453-42a2-308f-94e4-6fb06992d86e | -10.9713 | -45.707 | 2025-09-23 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 7841b599-31bb-32da-9b2d-786090759d38 | -4.8398 | -42.8875 | 2025-09-23 00:10:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 6d825cbe-1418-3267-b074-9830273fcecd | -9.4579 | -35.8281 | 2025-09-23 00:10:00 | GOES-19 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 1b2be551-7767-347b-992e-b7d319d3c3de | -11.6436 | -52.8605 | 2025-09-23 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 09f0ceaf-2ce0-3c91-9048-18bcbf0d47ab | -10.971 | -45.7298 | 2025-09-23 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 392b8ae4-b461-378f-9710-0ee14bddcbc1 | -7.8887 | -44.0281 | 2025-09-23 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 874fcd12-5f34-3799-8502-1409a31b6492 | -3.6342 | -51.915 | 2025-09-23 00:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b37e4527-5178-354a-b032-9ea3557f7033 | -7.889 | -44.0049 | 2025-09-23 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ad43bb34-101d-3db1-bfcd-a09e65e95b6b | -11.6439 | -52.8397 | 2025-09-23 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| d5b10a22-c8c3-342f-a6f8-8433242abc56 | -8.022 | -45.4581 | 2025-09-23 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| be8e1f52-b466-3f8e-b1e9-6951632eacaa | -3.5161 | -49.4528 | 2025-09-23 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| df1615c5-3bb9-32da-aa54-e024a864feeb | -11.6247 | -52.8624 | 2025-09-23 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 362a8338-e984-3ea8-9b9a-321e401c2f04 | -10.9522 | -45.7096 | 2025-09-23 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f8df72f6-a6a0-37a5-a0a5-4949c5a830f9 | -6.2596 | -45.341 | 2025-09-23 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9b5b0999-f173-3d11-9712-c2a72baf2dfc | -11.6249 | -52.8416 | 2025-09-23 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 4c94eeb3-5fd2-38a8-a286-709e212f8b16 | -12.7758 | -57.86 | 2025-09-23 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b5c8055a-c285-35b2-9684-cdf57698d1d3 | -7.889 | -44.0049 | 2025-09-23 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| c424166a-568c-350d-93c2-c09bfde1b7ad | -10.9522 | -45.7096 | 2025-09-23 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 7efcc20a-e97b-3b86-8750-63db2d739e36 | -3.6342 | -51.915 | 2025-09-23 00:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 63474f66-10b4-3604-83c7-6fcf423f1483 | -10.971 | -45.7298 | 2025-09-23 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c7ec8064-5e1a-3f88-be7a-33935b808fde | -4.8398 | -42.8875 | 2025-09-23 00:20:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d4110061-e90f-3c32-8e15-b1ab41761795 | -6.2596 | -45.341 | 2025-09-23 00:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 42f4f5ff-4454-3b24-88bd-f3d5c12889c7 | -3.5161 | -49.4528 | 2025-09-23 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 16c5eb88-eab7-396f-90b9-3632fc7e63cd | -10.9713 | -45.707 | 2025-09-23 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 578e824e-1164-3e94-acf1-01627fe248be | -11.6439 | -52.8397 | 2025-09-23 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 89195822-7d05-3f42-aa7c-b75d58ac4b46 | -11.6436 | -52.8605 | 2025-09-23 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 618217d5-f158-3ff6-af04-fd1673226624 | -7.8887 | -44.0281 | 2025-09-23 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 7a14fe87-fd70-37a3-8536-f42b140c82e8 | -6.2598 | -45.3184 | 2025-09-23 00:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d5112771-08eb-3241-94eb-eaa75c3a8b05 | -10.9519 | -45.7324 | 2025-09-23 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e6e3c21f-1b88-3616-b6cd-f26161f6015c | -11.6249 | -52.8416 | 2025-09-23 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 5cc6f9c9-4624-3419-8a83-aa60cd693fb1 | -11.6247 | -52.8624 | 2025-09-23 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 81dbccb9-add9-3ecb-8422-f4e811f4d0e4 | -11.9187 | -53.5588 | 2025-09-23 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2384350b-cae4-3049-ad6d-f941a72ed854 | -3.6342 | -51.915 | 2025-09-23 00:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 17c3f8a7-34db-3995-85d6-fa36729d34fa | -8.5179 | -44.9749 | 2025-09-23 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 89905262-76d6-3237-b31e-62a978bb193a | -11.0848 | -50.7729 | 2025-09-23 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 04d97964-6dcf-302e-bfb6-eb5098d563c0 | -6.2411 | -45.3198 | 2025-09-23 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d89b88b7-2140-37db-acdd-c95765a944b3 | -15.9578 | -59.4888 | 2025-09-23 00:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 9c4e5df2-9247-38df-bc25-6bcff6d0c4c5 | -11.6436 | -52.8605 | 2025-09-23 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| cc6a54a2-e8de-3cec-8706-1a0db830df1a | -7.889 | -44.0049 | 2025-09-23 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b629f44a-5b0b-3d41-b064-7fcd8db6a212 | -7.8887 | -44.0281 | 2025-09-23 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| dc7f939b-fc33-397f-aa93-21c6c03b0cbf | -10.9713 | -45.707 | 2025-09-23 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b41505c9-57d1-3a0c-a19f-10649c40a103 | -11.6249 | -52.8416 | 2025-09-23 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 57fe0593-976d-3651-8219-79803c6eeb55 | -11.6247 | -52.8624 | 2025-09-23 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 167.2 |
| f39cfda6-e617-3003-afcb-ab4ec6d90340 | -15.9581 | -59.4688 | 2025-09-23 00:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 139c92e8-b054-368e-8880-e4e1e765e4d8 | -11.6439 | -52.8397 | 2025-09-23 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d001ab8b-773f-3f79-9d20-7568308777a9 | -6.2598 | -45.3184 | 2025-09-23 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 171.8 |
| a23cdb98-d84d-3a9c-8a08-87a74a9b080c | -10.9522 | -45.7096 | 2025-09-23 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1d595bf8-409d-39aa-9256-ddb6e7525ca7 | -13.0235 | -48.7174 | 2025-09-23 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| acd54cfe-47ef-3534-895e-dbbe95fc1ffc | -6.2596 | -45.341 | 2025-09-23 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 221.0 |
| bf90eec0-a751-37d3-826d-2050b73afb32 | -10.971 | -45.7298 | 2025-09-23 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d1a8f8c9-17c2-3422-9a9a-7f3ed859fa95 | -6.2408 | -45.3424 | 2025-09-23 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 419b29ed-e107-303b-a4d8-d27ea9f3b5b3 | -3.5161 | -49.4528 | 2025-09-23 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 177eb7eb-616e-3e67-8b02-8cda19aea459 | -7.889 | -44.0049 | 2025-09-23 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 716cda59-3afe-39bd-9bfc-6fd06d296df5 | -6.2783 | -45.3395 | 2025-09-23 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d24e31c3-831f-3b36-9ac1-5965f349a148 | -10.9522 | -45.7096 | 2025-09-23 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 084714cf-7c9e-3499-a2c0-a7053ef13437 | -11.6436 | -52.8605 | 2025-09-23 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 56be297b-8af3-348a-a36d-9b1d4e8b17d1 | -6.2596 | -45.341 | 2025-09-23 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 251.2 |
| 69a0ded3-7a7f-3d78-9e4a-c9bb451e870b | -6.2411 | -45.3198 | 2025-09-23 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 021cc1f0-6d49-3197-98f2-15b34794e2a6 | -11.6439 | -52.8397 | 2025-09-23 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 367b5d76-672b-3721-8a09-8a791c1c60ef | -10.9713 | -45.707 | 2025-09-23 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fe5b24a5-f236-3b0e-bbdc-87f5ece7eb08 | -11.6247 | -52.8624 | 2025-09-23 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 0e778624-4d39-346d-b8dc-989392fbff8b | -12.006 | -47.7505 | 2025-09-23 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1063677a-67a6-39d9-a249-2aabd78e0481 | -6.2408 | -45.3424 | 2025-09-23 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| f4283856-2b7f-31b8-9f4d-7d5812847adb | -6.2598 | -45.3184 | 2025-09-23 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 67548dad-97ae-319f-9c8b-9f7a59f2a8f7 | -11.6249 | -52.8416 | 2025-09-23 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 3d0e77a4-785f-3ec7-8ad3-38b3b0ef8dba | -3.5162 | -49.4315 | 2025-09-23 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c2d59957-7893-3983-b957-4b6058bc6a0d | -3.6342 | -51.915 | 2025-09-23 00:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8fae2eda-6d6b-3d4f-8558-743bdaa179f8 | -7.8887 | -44.0281 | 2025-09-23 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| c27adb2e-951d-3f10-85d9-73c0a8bbe00b | -24.20937 | -50.418 | 2025-09-23 00:48:00 | TERRA_M-M | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2fbc37b5-6313-3136-b1ae-249410937d88 | -3.5161 | -49.4528 | 2025-09-23 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b46a10ee-a95d-3a80-9d89-84eeb4ff1451 | -6.2408 | -45.3424 | 2025-09-23 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4c8b5535-67fa-3627-9646-fc2e2f8155d4 | -12.8874 | -45.6571 | 2025-09-23 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b53dc260-42ac-3b7e-bbb0-c0fd7742dcfe | -7.889 | -44.0049 | 2025-09-23 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9a633196-8689-3932-8c2f-7dc9cab2ecec | -10.8616 | -45.4248 | 2025-09-23 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c041daf1-7481-3a6c-9af5-c811c4ceb7ac | -11.6439 | -52.8397 | 2025-09-23 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| cca81752-1e00-38e8-b1eb-378278815029 | -8.5179 | -44.9749 | 2025-09-23 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1ad6d605-7adf-38dd-9f93-03d74142ff2d | -13.0043 | -48.72 | 2025-09-23 00:50:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3269d61f-6560-3168-bcfb-373ddec37787 | -15.9578 | -59.4888 | 2025-09-23 00:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 14c80126-6b57-3ee5-8bc0-49d7f0dd01e0 | -11.6249 | -52.8416 | 2025-09-23 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| b69a97a4-fca1-38de-87c5-99ac4da25cef | -15.9581 | -59.4688 | 2025-09-23 00:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6c24a834-a84e-3943-98ff-befde56f8f07 | -6.2596 | -45.341 | 2025-09-23 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| bdc4e088-cb10-3171-b9eb-860b0ee4bff3 | -10.9713 | -45.707 | 2025-09-23 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |


[Clique aqui para ver as próximas entradas](README2.md)
