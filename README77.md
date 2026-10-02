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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e2c646f-912c-3534-8007-9d311851d5ee | -7.62881 | -55.07272 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a481b8c-5a97-3688-98d2-742e2edcd618 | -7.57696 | -55.13387 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 934a48c4-0762-3182-90b5-bee9427741e3 | -6.20091 | -52.8059 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cb2d92e-a300-36db-a794-e466b0242c2b | -7.49611 | -54.98396 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac78805e-6548-3cd0-aa9a-c5bf299ad5af | -6.43386 | -55.80283 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eb899ef-62d2-34ac-bf3f-ff3b7f5dd27d | -7.34543 | -55.5808 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 446c0b19-18d5-304d-ad02-9aa749f13e21 | -7.46409 | -54.99524 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b24ed0f-54c0-3a44-811a-ae80cf80f9b2 | -6.84706 | -55.53716 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e321774b-e3f9-3bf5-bc75-f1d987bd170c | -7.83073 | -55.13274 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d91ade1-84a9-3371-b6c4-96c85f67c9df | -10.2658 | -49.65873 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1305e3fe-099c-3828-8431-507c7c784802 | -6.44002 | -55.80546 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eaa50140-e608-3dae-aa2f-cca23c37e55f | -8.30837 | -54.72095 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 115ae6d3-46ec-35a9-bf5f-5ed7593653fa | -7.19225 | -52.609 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a290eaf-965a-3b35-82b9-b9c0b0c3409c | -7.75027 | -49.20753 | 2026-10-02 05:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 414bbba1-323c-38dd-a583-6202c9a97751 | -5.96917 | -55.37281 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7badcbcf-e6d4-32cf-ba38-bbb095b0f3ba | -6.35923 | -55.14298 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94acdce1-b2ed-392b-bfb7-8d6d56a38e03 | -8.08028 | -54.88478 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 584387cb-8726-3267-a588-9e6b0d63a823 | -7.33026 | -55.23343 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 897214df-d81d-33fd-b21a-ba759ca7209a | -7.88049 | -54.71611 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dc89b62-90ce-393d-bfa0-c34342eac75a | -7.4689 | -54.99198 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 199abdfd-2c18-3a60-8bbc-2296f184f6e9 | -6.34863 | -55.32834 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40d8b445-13ff-3897-af9c-bb25e0625874 | -8.1718 | -54.80127 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07514efb-e52c-3fd9-84a4-b3c29cf4c568 | -7.51446 | -47.33354 | 2026-10-02 05:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6707e54f-8ae1-3655-8e75-c008a1eec70a | -5.97268 | -55.37713 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b72b7d6-50ff-3253-a22a-8251281597a1 | -6.24967 | -53.14196 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd63afb3-fadb-3ada-8cfe-a4433d4f626d | -7.81939 | -55.12337 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9965a871-0b59-35c8-817b-f34519ece54f | -6.34508 | -55.32412 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9d1491e-8b68-3ddb-931b-84db28c6064f | -7.39432 | -55.21101 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 91db2b76-d2b8-3d0d-a4b4-15861e5dcfb5 | -7.46041 | -54.99071 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20c51115-353f-3570-a1a2-efb8b0be54e0 | -8.20329 | -54.70757 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fba82f1-7d0f-358e-8f35-d43e73436ce1 | -8.25719 | -54.73502 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16014c5e-0413-365b-9e62-f5fe7d2328be | -8.17615 | -54.8019 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 922642c3-6d9a-3a33-bbec-74be98004d20 | -8.1811 | -54.79841 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6c520b1-b5b6-3272-bf62-fecc654d7577 | -10.81885 | -51.0966 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eab167b-b624-3b88-a240-cb7a6218075a | -6.19199 | -53.17383 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1c7fa5d-017c-33c1-b565-87d9d1841168 | -8.07822 | -54.886 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3dccd68-76d0-358b-8af0-70e479d0f046 | -8.2099 | -55.09544 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30d0f19b-2ca6-307d-9acc-7fdb562565ca | -7.83864 | -55.13783 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88fee602-f2e2-3af4-ac6e-1a785fc84948 | -8.22954 | -55.28695 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22a9def6-f46e-34df-af12-1f881fdeebae | -8.17735 | -54.79364 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ddcd03a-9118-31c7-807f-f3aab64c5a27 | -7.72192 | -54.75839 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95930166-8952-3b90-aa7c-5ff64c738c3b | -7.83182 | -55.12499 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 426b8272-41ec-398e-90d7-0cfbc0acbf05 | -11.30333 | -50.93166 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bc5eec7-be83-367c-ad37-d0fe2bc3e0fa | -8.5421 | -54.55853 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50150329-e4c7-3efe-99de-52636a2210b1 | -8.16865 | -54.79239 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb601d1f-6f12-37d3-aa8f-2b3b7de173f9 | -7.82759 | -55.12437 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 093b875f-b9a1-39d9-8878-c47d36ce78aa | -8.29899 | -54.72398 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69bf0ee3-dbb9-3a33-a303-5252ee598777 | -7.46657 | -55.00799 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21408dec-d7d2-3747-99e2-a642d19a2046 | -7.03585 | -55.63315 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 784894f9-f118-33ab-bb42-81d31ae01094 | -6.24892 | -53.14712 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3486863f-f465-350d-8540-2488406dab01 | -10.83207 | -51.09244 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7beeac68-5c15-397e-8d48-b29fb198af39 | -7.82785 | -55.12457 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e449394a-e04b-38f0-a7d1-370372bb5781 | -6.40769 | -56.39883 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9ab004b-f1bd-32f2-90fe-33f714cc2ec3 | -8.54874 | -54.56634 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5ba5690-62f3-32f1-8df9-eb4959d22fc2 | -7.04495 | -55.62744 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24a2bfb8-c32a-3db5-a6ef-c5b7c0ec8db8 | -7.87945 | -54.71659 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d5ae0d2-8cf1-33ab-a0f3-c3e1ab472c75 | -6.26227 | -55.43412 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4fb5f1c-b0ec-3854-a68d-582c112fb9f0 | -11.30384 | -50.92738 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12d2880b-573d-3509-8cb4-82794c5ebc24 | -7.49728 | -54.97598 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec909a53-0294-3673-8ef4-6935d5bd5d3e | -7.48952 | -54.99929 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab9e475a-9584-3eef-bf1f-4cbeb7bd19b0 | -7.82704 | -55.12825 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba48ded7-62d3-389f-a81a-1ac9fc44e107 | -11.43394 | -50.9763 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ca66596-659b-33ef-8617-73fa7a995ce9 | -8.05834 | -54.84104 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b4f54b1-6cad-3f62-8619-e2366d9c5d98 | -7.04392 | -55.63447 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6648fa5c-cb2d-3712-9a06-f915f9c98b8a | -11.30975 | -50.9282 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8496cbd8-3d17-38ef-9f6d-f235eaa872f8 | -8.24992 | -54.6602 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2fb42bc-2bc1-3563-9e1e-ccc3a1190c7b | -6.44041 | -55.62525 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2634cab0-90c6-32df-b073-72a3d531ea0c | -7.72133 | -54.7625 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afd26437-5ed6-3d7f-94bb-f1babc49e464 | -6.18235 | -52.89944 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| af0f8610-d2f0-32e9-9d0f-a78237b6a006 | -5.98535 | -55.37547 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9d8106-1e91-3e73-a827-00ba25c85dab | -7.74463 | -49.2018 | 2026-10-02 05:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae128f08-1baf-3195-9496-6b5349656bdf | -8.1805 | -54.80252 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab22da5f-2a99-3587-a996-ecc5d6740d72 | -11.30437 | -50.9231 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 371948f9-b04e-3330-90e8-08812bb19e78 | -6.00939 | -53.54288 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 045f3e91-8238-3c37-a274-88c94c44e5c4 | -8.06385 | -54.83356 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc1037eb-10a7-3b3d-92a0-d1aabcad2fbf | -7.63304 | -55.07333 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95fc1b0e-983b-39c3-a0d8-5687b324af52 | -7.51846 | -47.33615 | 2026-10-02 05:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ffb7776-bd90-3a39-a8a7-c4da63b39b90 | -7.48894 | -55.00323 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11714fbd-b613-3803-b6a6-7fee1aea3893 | -7.57159 | -55.02267 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8858f5fa-1610-31e3-9ffb-757e0ac235f9 | -10.26912 | -49.65855 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecb91080-231d-3c49-a7ec-86680c8065c7 | -10.25076 | -49.67735 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a8a92f0-2b43-3462-84b4-472d88fb969e | -6.2548 | -55.48342 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37ed27e2-0aeb-3fbd-9db3-1a4f8987f4f3 | -5.99894 | -53.55015 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8714e6ae-d1ba-3ae0-b611-b240d397920f | -10.25888 | -49.66298 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a577c30-c37f-3b7b-97fb-d19864f19dae | -7.57274 | -55.13328 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4cf6c37-b92c-32c1-996b-bfd07c11e618 | -8.15459 | -54.82827 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96b9fbbd-f9a0-34a0-9347-2a08d1877109 | -8.16745 | -54.80068 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 240c03e6-8efe-32d2-9231-2216725dc844 | -6.39724 | -56.41631 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d85d8d96-f9dd-3500-aef0-7cccdb7b2a81 | -8.53765 | -54.55791 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbe20ed1-a9aa-3106-afd2-0abf089e6c60 | -6.24494 | -53.14129 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4594a1e1-21cb-31f7-b044-abd70b7f9cae | -7.39794 | -55.2155 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 007aa7aa-919a-3eae-867a-ae4354303394 | -7.46947 | -54.98802 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca1c658d-f83d-3a09-9591-dd99f8d24e4d | -7.05761 | -55.62576 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6b1bb0f-ee63-3000-a6b7-60f9d118f533 | -7.39072 | -55.20631 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ad8f890e-571a-38ad-b544-fbecb253c960 | -8.26062 | -55.69117 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 283cf209-c7bd-3341-8e3e-2359605dd648 | -6.19114 | -52.80508 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2733648-3ebf-381c-865b-28b009d55554 | -5.99574 | -53.54016 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5a0ade1-b3a6-368f-9006-747c209cf605 | -7.72252 | -54.75428 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f10968b3-5d1e-3443-9da3-ecb8cc2af8db | -7.56735 | -55.02205 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20cd7627-3b6d-339b-b04b-0dbdd6633f77 | -5.97376 | -55.36977 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README78.md)
