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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc5577af-3cf3-37b7-b6fd-086f1fd9a7eb | -3.75938 | -46.95935 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b904c07-a358-30b2-a2b7-82105222575c | -3.67582 | -43.57666 | 2025-11-28 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cc5c4f4-5787-3d38-aa48-f8702e69f04a | -3.0632 | -50.37186 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44d01eab-76ef-3299-bf41-cbdf5dd67dd4 | -4.31782 | -44.055 | 2025-11-28 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceeccd06-1bd6-3971-a79b-d4e03ca09f9e | -3.17305 | -48.60716 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e47433c-f714-3571-9a4f-0cc124b1b1d6 | -2.62125 | -47.36119 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08e062b3-1794-32dd-85a5-9bb3db0cee5d | -2.42722 | -45.75153 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ee99f7a-5c97-3013-8581-d65e1e28d9d1 | -1.34589 | -55.44489 | 2025-11-28 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31efe162-a7dc-3337-acac-98f029fc456b | -2.71351 | -45.21786 | 2025-11-28 04:31:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5596c05e-b89c-372c-93f3-ee6631b56496 | -3.43857 | -52.18 | 2025-11-28 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 575dacc4-844c-3e36-aab6-30eb070be326 | -5.64153 | -44.43916 | 2025-11-28 04:31:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffec481a-e7df-3dfa-a04e-95cbf649e99f | -2.61241 | -47.35278 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a82aa96a-36b5-3b41-91cd-210c7d96f30d | -1.64853 | -52.03999 | 2025-11-28 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 473b78cf-946e-34ca-9735-e35dad8c7ca4 | -3.49131 | -50.48925 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a75aa8b1-27a7-36dd-acb1-f050ace246b5 | -3.95186 | -44.76754 | 2025-11-28 04:31:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd07687e-40b6-3c6c-ae56-2aa5037d2f74 | -5.29182 | -44.96159 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1642b869-8e91-3de8-abfc-11a9145e13d8 | -3.80864 | -45.14391 | 2025-11-28 04:31:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6ce8566-2c5f-3880-a9f4-77386420e791 | -3.5915 | -47.2712 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 340ae220-a3d3-30da-aad6-09ce79c84dd6 | -3.3513 | -45.42658 | 2025-11-28 04:31:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdf7ec73-9803-3586-b660-ce4e2c40ea8b | -5.63478 | -46.3135 | 2025-11-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ab16bd3-9cd9-3c3c-bcee-8dfa8a375eb8 | -6.72683 | -40.82078 | 2025-11-28 04:31:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0c37a009-66e5-3766-be98-638d6a7549a1 | -2.42387 | -45.75101 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91733cdc-e206-3d76-88de-ca2dfb29bc1b | -2.71408 | -45.21419 | 2025-11-28 04:31:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70c749b4-9c04-38b2-894a-28eda8d808f8 | -4.15677 | -46.17758 | 2025-11-28 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bb2cb5e-4d95-3bd0-9cc2-542d26feb1de | -3.56812 | -47.1795 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7515f72a-257f-3dff-a562-b927b10f3e1a | -3.52548 | -53.06842 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 569f92a3-ebe1-3463-8076-3158fb09370b | -2.70206 | -49.55928 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acb940e7-9b62-30a8-b8d4-43c428de42a2 | -5.39488 | -43.10515 | 2025-11-28 04:31:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c26f07d-8eb3-3bf3-9ecc-1ab68f4e9948 | -2.95516 | -49.56199 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bdd69a0-b116-3d13-b80b-61f53f87248d | -12.23607 | -49.3835 | 2025-11-28 04:33:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8efce709-b935-3044-b594-54196f019559 | -9.87962 | -44.1701 | 2025-11-28 04:33:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56b75e1d-6aec-3c77-b165-14cc171d7a40 | -12.23276 | -49.38295 | 2025-11-28 04:33:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28413e03-c3db-3305-b40c-fcce806ed071 | -12.44456 | -57.76449 | 2025-11-28 04:33:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5185c0e8-30dd-3572-b806-56406e669d59 | -12.44904 | -57.76841 | 2025-11-28 04:33:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e38d9d2-722e-330d-9f8a-210c89e0560e | -12.23938 | -49.38403 | 2025-11-28 04:33:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2c151d9-efb1-3be0-ab01-eead3ad49b9c | -7.5829 | -55.49495 | 2025-11-28 04:33:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 972d81a5-2bbb-39b2-9220-1107bf26c357 | -9.93656 | -60.71471 | 2025-11-28 04:33:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfb27e6f-e005-3c99-8532-5839bbf9b2bf | -11.27146 | -53.96268 | 2025-11-28 04:33:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38d9e53a-d2db-3db6-a69a-faf3efe9adf2 | -9.93554 | -60.71981 | 2025-11-28 04:33:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0972200d-e72e-320b-9d6b-b69b8a89d013 | -11.39486 | -49.19567 | 2025-11-28 04:33:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55907835-d3ef-3640-b5ef-bd0bf3c82cf6 | -9.93352 | -60.71733 | 2025-11-28 04:33:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 080b882b-a68c-3827-82d5-773f7e80b050 | -12.4496 | -57.7654 | 2025-11-28 04:33:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af992d22-a6e2-38e1-9832-4c53fc148a45 | -12.44842 | -57.76661 | 2025-11-28 04:33:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4198afb-3855-3a2d-91ad-a1f8a7d986e3 | -12.44399 | -57.76751 | 2025-11-28 04:33:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc883428-ab8f-31f9-9b76-80d857d289a7 | -12.44901 | -57.76361 | 2025-11-28 04:33:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da284e92-fe3c-370d-b185-74cd6908a851 | -9.93985 | -60.71856 | 2025-11-28 04:33:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 494f08b8-58a2-33d7-97fc-28e599811505 | -12.44338 | -57.76574 | 2025-11-28 04:33:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89c9d119-2c88-34ce-9e1d-d61d07a33689 | -11.27207 | -53.95915 | 2025-11-28 04:33:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7bd0af1-8c03-368a-9636-1ced383212e1 | -21.75546 | -49.03128 | 2025-11-28 04:36:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2b17ba3a-0a1b-3747-a988-f83d12dd45b9 | -21.87777 | -44.8697 | 2025-11-28 04:36:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 00a97528-7839-3564-a69b-c94d9f64bc3f | -20.84484 | -46.37407 | 2025-11-28 04:36:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f1f0bef-6e38-3a5c-b94b-647c5eac135d | -16.14406 | -59.96511 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a9ab522-578e-3fb3-b3e2-2d2076af7168 | -15.6047 | -59.94259 | 2025-11-28 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8773b22-0e5b-3993-8fbe-a3e16df400ed | -16.06514 | -59.29525 | 2025-11-28 04:36:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58366795-f9fa-3846-b25a-45bdf2b3f838 | -21.65532 | -48.61756 | 2025-11-28 04:36:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aceb297-9991-3b46-a734-076b005232f8 | -16.14268 | -59.9648 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f3aaa30-b2b9-3cef-b9f9-5ae94fd19311 | -16.06463 | -59.29573 | 2025-11-28 04:36:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 171bd097-1333-364d-8e1b-5ea215dffadb | -16.13727 | -59.96363 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c49689c3-f67b-3183-a96c-e498949792a9 | -20.46514 | -47.47605 | 2025-11-28 04:36:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a31b3d5b-b862-3b86-8ca3-95855229f427 | -16.13865 | -59.96396 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 620df179-4eda-300a-93e9-6b96f0294e3b | -18.15549 | -54.56308 | 2025-11-28 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f4d5de5-b7a1-3a6f-9be7-5a4cb88aa135 | -21.75198 | -49.03074 | 2025-11-28 04:36:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 536d9cad-e073-396a-bac3-1cebf4a37584 | -16.13941 | -59.96036 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95d6432d-81b2-31c0-ad13-add0f8165269 | -20.24798 | -50.67656 | 2025-11-28 04:36:00 | NOAA-21 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f009987b-4c39-386e-86f6-d15ea89eeecf | -18.03824 | -48.92035 | 2025-11-28 04:36:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ebf77625-97cd-3cf9-a64f-4b418d4d9ace | -16.09982 | -59.76263 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4cf591e-9737-370e-b137-65bb95406e2b | -20.63783 | -51.68037 | 2025-11-28 04:36:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dc390a1-24b4-34c8-93a0-20f180d995de | -18.15631 | -54.55842 | 2025-11-28 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9632161-6faa-31ce-b14e-d37060ad1709 | -17.3934 | -49.24315 | 2025-11-28 04:36:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29cbc6c7-319c-34f2-af63-606286ba1983 | -15.60544 | -59.93901 | 2025-11-28 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec80ba35-b5aa-306f-bbe8-d695e43716be | -18.86511 | -52.11852 | 2025-11-28 04:36:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e027d6a-f9ff-3110-b18a-3d6dc87fae59 | -21.68952 | -47.9566 | 2025-11-28 04:36:00 | NOAA-21 | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 78a2410e-a02a-32f8-b3aa-250387bbcd07 | -21.65179 | -48.61698 | 2025-11-28 04:36:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a998145-7898-3649-ac21-b71834cab1c1 | -19.98941 | -49.99183 | 2025-11-28 04:36:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 610768a3-5753-37b3-9fad-dcc414e3ff5d | -16.06013 | -59.29327 | 2025-11-28 04:36:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9eea4f9-d280-3ffd-891f-4bf0cbb842e8 | -16.14015 | -59.95681 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 307d9780-7977-3bb0-9695-b09afc2b3ec0 | -16.14481 | -59.96151 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d66bec84-5bb9-3042-a115-c2057c9d607f | -20.83026 | -47.20466 | 2025-11-28 04:36:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfd3a0b6-1a45-3e49-9e3a-1ed91842cd82 | -16.05959 | -59.29389 | 2025-11-28 04:36:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb54d0f-f012-32d9-b675-c9fc2eeaab0c | -19.98997 | -49.98811 | 2025-11-28 04:36:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 928fa08e-a92c-3530-8239-3632ed540175 | -19.98663 | -49.98755 | 2025-11-28 04:36:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 8cc4991e-dd69-373c-a493-27c363976dd2 | -21.65121 | -48.62119 | 2025-11-28 04:36:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1281ed4-7412-3fb7-b3ce-7e4c6e256abd | -16.14412 | -59.95768 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52ca6dfe-1b7f-3f9d-ac33-f039a25c41b8 | -21.26291 | -50.29885 | 2025-11-28 04:36:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 851121ef-b2d3-327a-96f3-457fb5525ba9 | -16.14341 | -59.96119 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a40ccfee-9153-3b71-9736-5c5d9cb594ca | -21.22957 | -47.04529 | 2025-11-28 04:36:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 422f5199-3113-3018-8f2d-60e96709b880 | -20.46146 | -47.47551 | 2025-11-28 04:36:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ebfe9bf0-d3d6-3c3e-aa65-279e5cdddf95 | -19.9855 | -49.99498 | 2025-11-28 04:36:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 4ac4734c-6a47-30b2-af7c-7190edf55020 | -20.46881 | -47.47655 | 2025-11-28 04:36:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 33af2ca0-019f-32ab-a820-e271bcaeae52 | -16.14554 | -59.95803 | 2025-11-28 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ec80401-85f6-36f7-bfd7-71d81d4e8e55 | -20.47277 | -55.60159 | 2025-11-28 04:36:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61d7ed2d-4fbb-329c-8bec-41f2472e0f8b | -21.33353 | -48.57063 | 2025-11-28 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48b5f6f0-2095-38ed-a2e0-6c84fee3610c | -18.15712 | -54.56103 | 2025-11-28 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9fdce06e-e0f4-344f-9a84-aed526260347 | -19.98884 | -49.99555 | 2025-11-28 04:36:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 3c98480a-a60c-3d82-b913-0e9e9e731c84 | -21.65062 | -48.62538 | 2025-11-28 04:36:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8690ba15-83a6-34a7-8cbe-753fc00f558a | -19.98606 | -49.99127 | 2025-11-28 04:36:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 36967e4a-15f3-399a-8319-4a44e32bb27f | -15.60445 | -59.94087 | 2025-11-28 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc601136-e1aa-309c-bd6a-cc722ed9dee9 | -20.83123 | -47.20646 | 2025-11-28 04:36:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0970672f-3ef2-3ede-8c26-a8526173bea1 | -21.26053 | -50.29861 | 2025-11-28 04:36:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 6372718e-fa3b-37ad-8822-6979e126f717 | -15.60517 | -59.93727 | 2025-11-28 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
