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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14a8de52-2a6b-3afa-820a-b18797b0487c | -16.66265 | -46.67431 | 2024-10-06 03:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afd3cb98-3bf4-39e6-87aa-27369f50f11f | -16.6584 | -46.67347 | 2024-10-06 03:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf608878-4a7f-3997-84af-25f879afd21d | -11.36689 | -47.25063 | 2024-10-06 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5d284c31-4115-3e4a-99d4-d5d454c5e267 | -11.31314 | -46.79642 | 2024-10-06 03:55:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a438d206-6d57-3090-ab8d-9b3940b34970 | -11.28355 | -46.79548 | 2024-10-06 03:55:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f85e45ea-c29a-3dcb-aecf-3a1451d33ea2 | -11.27885 | -46.7945 | 2024-10-06 03:55:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cded2d6e-8018-334f-a5c4-8dc924d2f115 | -15.1897 | -47.50387 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70b7e705-ada2-38fd-af23-61e951a77232 | -15.18886 | -47.50823 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c919619-3190-3ce5-b650-cdbd72f858ba | -14.0315 | -47.27634 | 2024-10-06 03:55:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d19cca6-4a1f-3236-ac44-548229b321e0 | -14.03052 | -47.28147 | 2024-10-06 03:55:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c4e79f7e-4774-3832-8610-ea3ee570f308 | -14.03027 | -47.27008 | 2024-10-06 03:55:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bfaf0c1-935b-3707-a5a3-ce68c701ade6 | -14.02857 | -47.27931 | 2024-10-06 03:55:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 249aa2bb-066a-3c4f-86fa-7b10f32e884d | -15.12761 | -47.08464 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bc1bcf5-2e9a-3148-8158-9879b2fff598 | -15.12313 | -47.08369 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a96ed9b-8306-3997-81c4-ceba62c60eda | -15.1178 | -47.08736 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 792e6251-5d49-3bff-b4f5-a4162e383c3d | -15.11242 | -47.09128 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b81979a-d0eb-351f-8c20-45033a6a9156 | -15.44209 | -47.70403 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b82735da-4501-37c0-b344-20ed7417adb8 | -15.44041 | -47.70217 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0512d251-753a-37fd-a089-5fb215c8eda2 | -15.43952 | -47.68134 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94bd6306-bf86-317c-b96c-1087d3504f69 | -15.43951 | -47.70696 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1de09c2c-e825-333b-a6fe-bd44c7890f75 | -15.43857 | -47.68638 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09e55033-3d59-316e-a4f2-c6b0626c7010 | -15.43489 | -47.70589 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad43580a-a38e-33a2-a729-e167adf97ed8 | -15.41633 | -47.702 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1032cd91-34d6-3eaf-aca2-9030f23e101f | -15.41539 | -47.70694 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2cba898-4961-33c8-b3f9-bec56f836e6d | -15.39139 | -47.40924 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 214fcf8e-eb44-3ed6-9e05-56469042aac4 | -15.39128 | -47.41169 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a86e1bae-08f5-334f-98f6-e9c3e39cd8f0 | -15.38576 | -47.41592 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01eb65cc-aafc-3921-a43f-cdf9d4167369 | -15.26787 | -47.49454 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 220e44dc-979c-3487-93a0-1426beca9451 | -15.25959 | -47.48788 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e325a19-30ff-3e06-be80-272c28887bd9 | -15.25875 | -47.49232 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4527905b-c4c6-3828-a6a0-29912f68ac79 | -15.25582 | -47.48257 | 2024-10-06 03:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a733649-1e58-33f4-835e-1f1dcbfbef3d | -15.15899 | -48.0407 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c4e81bc-288e-3efc-9410-07e26cb8e917 | -15.1579 | -48.04621 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f3af9d2-6973-3145-b907-3a275fd84604 | -15.15368 | -48.04857 | 2024-10-06 03:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df4a234d-9932-39c3-b4e9-3789d89ac724 | -14.5533 | -48.81445 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7136593d-d6bf-3f06-8d0b-c0b53dbc9216 | -9.93532 | -47.70321 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d948597e-d944-3297-bcf9-1ffefe8aa3ff | -9.93341 | -47.70353 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8847d28-727d-3b5c-aa51-6e78887e9636 | -9.92889 | -47.69921 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 513bb4db-5973-3fad-a4d2-135ed67cc994 | -9.92833 | -47.7023 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a754dab-1886-309b-906e-894a24622cf6 | -9.69993 | -47.83635 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca4cf301-ac0a-39c4-ba2f-670ff2c5f3da | -9.69836 | -47.81615 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4513f6cf-7e09-37c3-ac47-f8d5bbaffce1 | -9.69778 | -47.81924 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2c0e073f-f82a-31e1-91c5-bf282740137f | -9.69719 | -47.82236 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bc7c4bb9-bec2-37ff-a983-fc57aee5ecb2 | -9.69659 | -47.82553 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ccafde19-9344-35e7-871b-affa7f5df9a6 | -9.69599 | -47.8287 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61d73429-2e6d-3753-89de-51fd66441cf3 | -9.69539 | -47.83192 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0515fc5-c51f-3401-9bfb-f533e6b42367 | -9.69478 | -47.83516 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb9998f5-c489-32d4-94f3-f3bd6b0ffcd0 | -9.69418 | -47.83832 | 2024-10-06 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65809fe-60b3-3b8d-8d43-269a292c3454 | -14.55291 | -48.78936 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57782eb0-d6d7-3003-a08a-6289922f7caa | -10.68721 | -48.72532 | 2024-10-06 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2148c26f-c4a9-37ba-8da2-86b43ba27c7e | -10.68179 | -48.72432 | 2024-10-06 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f01d5653-f2ee-391d-9783-67fe221391cf | -10.59121 | -48.02869 | 2024-10-06 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70a13c06-f7b0-3647-bafc-7b676b810299 | -10.59064 | -48.03174 | 2024-10-06 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2005be5-a4a2-3d36-8bbe-edefc1ee5ea5 | -10.2272 | -48.01418 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cae9726c-2c2e-3eac-83c8-29376e96590a | -10.22319 | -48.00682 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d219b05a-5c0f-3329-bdb3-cf99f1d61c48 | -10.2226 | -48.00997 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4673590d-12f5-3050-bb13-3c30276930f2 | -10.222 | -48.01313 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2fd172a-1e45-3680-9a09-12599dd4efc6 | -10.22141 | -48.01627 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae50d7fc-a97a-354d-ab61-eb890f21df74 | -10.22081 | -48.01942 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b871b957-98b9-31cd-a3ae-3d81624b8592 | -10.22023 | -48.02254 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cb1c308-8bca-38ed-a7c8-94ed03816291 | -10.21759 | -48.00901 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c1672f8b-4c39-3275-b193-a5f290b4d217 | -10.2174 | -48.00894 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 237dfdcb-0816-3cd9-b690-79e842e66838 | -10.21702 | -48.01213 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6ca6384d-054f-3fc9-804a-731067979295 | -10.21681 | -48.01204 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8512a8fe-8981-3bf0-97bc-d0b404c21d3a | -10.21645 | -48.01527 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0aff39cb-8857-35e9-8b1c-d2009f46dec3 | -10.21622 | -48.01518 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6fe7e0c0-8234-3b76-8e07-fd82e3f32e5e | -10.21588 | -48.01844 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9b079617-a74a-3e01-8b92-5823fcda8dff | -10.21562 | -48.01834 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8ae3b5ba-3b2f-3dff-85f1-786843e1621f | -10.21531 | -48.0216 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ca97bed2-a3bb-35b5-82d2-6f5516410cb2 | -10.21503 | -48.02148 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3c0e70c8-3c56-3138-b0f2-5fe9d784b386 | -10.21474 | -48.02472 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5ca6e2d6-4c92-302d-bf5e-d109d7a70d3e | -10.21444 | -48.02461 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 939542e6-7f99-387d-9f5a-5c1726244178 | -10.21417 | -48.02785 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 18cb94e8-0def-3f3e-a35c-cc3fccac8d5e | -10.21385 | -48.02773 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5fd51e22-0c5f-3f22-a98b-694bada8ba48 | -10.21361 | -48.03098 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d5d234a6-f68f-3525-b8b2-9a57a2e1f50a | -10.21326 | -48.03084 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e66ff46a-ffdc-39b6-a969-5571e9fc3036 | -10.21125 | -48.01422 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5e5df85e-a24e-30cc-8551-efbd428dcb06 | -10.21101 | -48.01415 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 466cc825-e85d-38ac-823a-efb0003b7047 | -10.21068 | -48.01738 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8f882721-f8e5-35a9-a051-1d843f12d746 | -10.21042 | -48.0173 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7811aecd-41b8-36ae-8713-f14b2f66c81b | -10.21011 | -48.02052 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0539abc7-252d-347c-81f5-068cf8351027 | -10.20983 | -48.02043 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 078a19b4-3f5d-3aac-b47a-67eaaad30832 | -10.20954 | -48.02364 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 13e6f9f8-c6dd-33d3-b44f-2397dd568441 | -10.20924 | -48.02353 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 038e530c-78b1-346d-bf3d-cd03216e72ec | -10.20898 | -48.02675 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36078cad-acf9-3887-9bce-52b5c74fe4bb | -10.20865 | -48.02663 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c2d2e52-9f50-3192-a4bb-5ad76b10a050 | -10.20841 | -48.02986 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 77a029f5-0d66-3cf6-86f4-babbcb0fe1e7 | -10.20807 | -48.02972 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1bf5a64d-f412-3764-8fd8-b3d6a4b1d6dc | -10.20434 | -48.02258 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| a330fb19-f710-37d4-b2d0-f136b3f65321 | -10.20404 | -48.02249 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 34d6401a-9006-3841-95f1-e71e4a2ce3c5 | -10.20378 | -48.02566 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 1e9742b7-47e8-32de-807c-c30a39a95a38 | -10.20345 | -48.02556 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 50ac7ba4-27cf-339a-a580-8a25ad1c5a0d | -10.20321 | -48.02877 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 76be75d9-aea8-35f0-97c7-8ae65fad59c9 | -10.20287 | -48.02866 | 2024-10-06 03:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| aad1cfe6-6864-3688-82ef-246c02ce1f2e | -11.62361 | -48.32776 | 2024-10-06 03:55:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8df8e3a4-f950-3b22-b4ff-0647a5a4dc57 | -11.62301 | -48.33095 | 2024-10-06 03:55:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44467226-7be3-3baf-b035-74ff51fc359a | -15.05079 | -49.47159 | 2024-10-06 03:55:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3706ef0c-542c-3e3b-8f3b-3897bf44f1d3 | -15.05013 | -49.47488 | 2024-10-06 03:55:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0c4dcb5-eacf-346e-a9c6-3880d125782c | -14.67789 | -48.78263 | 2024-10-06 03:55:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bee39b6e-e2cd-3c65-b230-d15feb163502 | -14.55846 | -48.81508 | 2024-10-06 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README55.md)
