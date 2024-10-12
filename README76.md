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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af5111ac-46fa-3bb3-8924-cbd70959138a | -9.57274 | -55.80152 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d18ada87-033b-3e4d-9cdc-025dd139cb3d | -9.57217 | -55.80505 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f3e00614-a773-3879-addf-dec3df91ab2b | -9.56942 | -55.80098 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1199139b-f27a-3258-a93e-518f1ce0afd7 | -10.11126 | -55.1964 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dfa45d6-101b-3964-acfe-77b8a3c24427 | -10.10465 | -55.19534 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef523459-b3dc-346c-9a01-f13cf436f3c2 | -10.10355 | -55.18089 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ff75c85-0743-37bc-808e-fdc6a3e2b329 | -10.10024 | -55.18036 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f2748e7-1f03-3a9f-a8e9-6bd6dfa1c5d6 | -9.70211 | -56.39441 | 2024-10-12 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ced70d6-3f1b-3fdf-aae0-54fff4e0b657 | -9.70152 | -56.39803 | 2024-10-12 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c07e3ac9-5c6c-3077-b916-c1c5d9c2be1d | -9.69875 | -56.39386 | 2024-10-12 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a67eba3-e04f-32ef-a33c-1a69778f21f0 | -10.76245 | -56.23974 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4984df8-b1a1-32dd-aac0-4cb0c33d25cf | -10.68177 | -56.25218 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2706021-bea3-36e2-9923-16141464e679 | -10.63251 | -55.88021 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d85ea94e-9681-3de0-9782-e61e695019d4 | -10.62405 | -55.93306 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09094a31-ee05-3166-a5a2-4b5881ed2be0 | -10.62349 | -55.9366 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32e09a6f-a02a-35d8-8be3-4a101c17f343 | -10.62074 | -55.93252 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9c522c3-2bc7-3ebb-91cd-a90a70cf0b75 | -10.62017 | -55.93606 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 709087fe-1404-3000-8ffb-fba39d9a0f9c | -10.61685 | -55.93553 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9199f482-8c92-3004-8a1c-41c337e2e3df | -10.57277 | -55.89232 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8a893a7-04a4-3bc4-84fc-e3afbb448142 | -10.57221 | -55.89583 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8965aed-9bae-39b8-a4a1-30176637b906 | -10.57165 | -55.89935 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0767a9f0-bfc6-37ed-9106-968f72e5e1a1 | -10.55848 | -55.8539 | 2024-10-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e13c53b-8054-3f76-8a9f-67f9a57835e8 | -10.4885 | -55.60869 | 2024-10-12 04:59:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c80c0351-dab6-3056-9429-57c75e36d759 | -10.48246 | -55.5826 | 2024-10-12 04:59:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afbe744f-d69f-3c5b-829f-e7ba2953b48a | -10.47971 | -55.57857 | 2024-10-12 04:59:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e5281b6-c749-3831-aa67-854043343c79 | -10.47916 | -55.58207 | 2024-10-12 04:59:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a932b9-4821-36be-b65c-1a83bf985233 | -10.47585 | -55.58154 | 2024-10-12 04:59:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1591f303-889a-32c9-a2f9-2b0f3f1b16ce | -11.93909 | -56.96738 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3e1a1e5-8988-3058-b7a2-10174987b781 | -11.93413 | -56.95527 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 752c7ffe-e332-3f8c-bffb-0e4813e241e4 | -11.93354 | -56.95892 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c069fa2-5745-3596-934d-d400bed03938 | -11.93295 | -56.96257 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e068e62-d6e9-37d3-baaa-1a1effc2aee5 | -11.93176 | -56.96991 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94bf234b-fc52-3877-b0bf-7dc6d567a47c | -11.93154 | -56.92859 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 098742ea-513f-3b3e-9fea-9647a49e4339 | -11.93095 | -56.93223 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aeaab7d-9bc0-3d0b-9cae-f22393245ff3 | -11.92818 | -56.92802 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1e9c8b2-2660-367b-9a38-47efaad59c5f | -11.92659 | -56.91654 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549301bf-c7d6-34de-9334-c9f276213d21 | -11.926 | -56.92018 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 017ce207-cbfb-324a-8ca4-adac16a22dce | -11.92382 | -56.91234 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e704d833-ed6b-33f8-afbb-b92409555134 | -11.92323 | -56.91597 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73e01f15-b4a1-3c34-a661-442cb4c038a8 | -11.92264 | -56.91961 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b38a1d0-fcba-3a54-8240-0df3f41cf73a | -11.92045 | -56.91178 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 929b66d7-f82e-3459-aa72-006f4bc45da8 | -11.91987 | -56.91541 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e1a7b92-abd0-3404-b534-f22eccd473ec | -11.91928 | -56.91904 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35985ca5-bb10-3486-8b82-304aa508dc1b | -11.9165 | -56.91486 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf9901fc-028b-3aee-af4e-b905b02353c0 | -11.91591 | -56.9185 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70846833-7755-3aa0-9df2-c9cc04223677 | -11.91314 | -56.9143 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fc53886-253a-360e-a06c-3de50dbeedaa | -11.90984 | -56.195 | 2024-10-12 04:59:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f4d959e-b81a-31b5-93c3-47167106fc08 | -11.85151 | -56.87742 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d388fbb-0a58-363f-a2aa-3a58489ff7ef | -11.84815 | -56.87685 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d24969a-04e0-34ba-90b6-8447978e27fe | -11.76483 | -56.33515 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba83909b-73eb-391d-8cd9-eaf43e677be2 | -11.76426 | -56.3387 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07fdbd1-b3c0-3da7-b872-f9461c5513b3 | -11.76369 | -56.34225 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7acce13b-c43b-330f-bde2-4790398f417d | -11.76312 | -56.34581 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d42e0f5-e686-336c-852a-49cf0262c031 | -11.76265 | -56.32751 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fe50872-7fed-353f-a188-072ebfd2e84a | -11.76208 | -56.33105 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f9d972c-75db-3e7c-89c0-f1b93cd5ad71 | -11.76151 | -56.33461 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33265d6a-2d91-33a4-b73c-d20a9b941654 | -11.76094 | -56.33816 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf25d960-4c8a-37bf-9008-ed758d888f2f | -11.76037 | -56.34171 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fffb7d39-3222-332c-930f-3eada1b839ac | -11.75932 | -56.32697 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c918877c-4b5a-38fe-ae8b-fdcc1aa7a933 | -11.75875 | -56.33051 | 2024-10-12 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62bd0042-9fc4-3138-bca4-cf3e8f78ca2c | -12.62093 | -56.5168 | 2024-10-12 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5800015-ab7c-3ac4-9e72-cf269e47e3e5 | -12.62036 | -56.52037 | 2024-10-12 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a69dfe04-20ee-3f7c-94c0-8915cd55d7f4 | -12.61761 | -56.51625 | 2024-10-12 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7331ff3d-814d-3e9c-a2f3-2bb571dbabcf | -12.61704 | -56.51981 | 2024-10-12 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21c1b880-5775-3fb5-a595-548116924bd5 | -9.39103 | -56.83798 | 2024-10-12 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee723cab-4108-3704-890d-8341cdc3a852 | -9.33995 | -57.60636 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 094b0e96-752c-39a2-95f7-b5e289d99c88 | -10.42703 | -57.23019 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec1a4cf8-9346-361d-9f6a-45b96b5fa4ef | -10.42422 | -57.22582 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c08cbd5e-5e04-3a1c-9674-efe213955a6d | -10.4236 | -57.2296 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b87fdfbd-73bc-3bba-85a9-7c5e58872e15 | -10.42017 | -57.22902 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1e5f216-c754-323d-8391-5f42a62c20cd | -10.31698 | -56.8059 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8503e3e0-02ac-3f74-83c2-39616888bc9e | -10.30483 | -56.77367 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72e2480f-51c4-3a02-834f-6b5684df3015 | -9.95095 | -58.10436 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8526e456-286e-3117-897c-920ecd09874b | -9.94737 | -58.10377 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c32cb16b-b670-3539-ba78-d8c8dee0f15a | -9.94379 | -58.10318 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 680e4a74-7a54-32e4-a14e-a5f96b2347ae | -9.94309 | -58.10731 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0282fe9-2345-30a3-9005-f537f96b8149 | -9.94239 | -58.11145 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b4ea006-1cf5-3149-b09a-dae1123853e3 | -9.9395 | -58.10672 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ca87de-add1-3265-a3d5-788f093378af | -9.93881 | -58.11086 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df176d82-8781-39e3-ac14-2e7c48d28be7 | -9.93592 | -58.10613 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a85aac47-bb7a-3eb3-bd1c-8b483f9afd8b | -9.93522 | -58.11027 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bee287e-d5ad-3b9b-9cb3-515a09e12fa3 | -9.93358 | -58.10693 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49d0dbca-936a-3ff3-bc80-bc3af0d2c63b | -9.93 | -58.10634 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50bce59d-459a-3caa-b45a-36b9f7363a2c | -9.90595 | -57.06429 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5688dd5-7e82-380b-887d-711b110d6d9d | -9.90533 | -57.06807 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99a0f6e3-22f7-3b84-a23b-f79d080c2dfa | -9.90253 | -57.0637 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c32b168e-d8f1-37fa-8981-b24aa53c8bc2 | -9.89848 | -57.0669 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bcb44e8-04de-3c87-a226-e8f028d23b11 | -9.84965 | -57.75404 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53f201af-d68a-3743-8740-82dd7d58bdfa | -9.84678 | -57.74947 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ed65762-d836-362c-a0e3-6226fc4f7852 | -9.78958 | -57.45529 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa22758e-3b3e-3e51-b494-367f88c87558 | -9.78894 | -57.4592 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c80dc96-6095-3070-8665-18c9c4ca8ebe | -9.78546 | -57.45863 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 763a7ffd-ecf3-3eea-a716-cda4a5772a19 | -9.78261 | -57.45416 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c45b9c5-48c6-3570-a163-1790aabb81ed | -9.78197 | -57.45806 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 542b6859-5b92-3015-855a-3ad24767d5ad | -9.76984 | -57.92816 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee14bc3f-bf64-380a-8fa6-7a0231f6d0fa | -9.68551 | -57.20819 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6fe07f2-5d96-3b97-8ff3-6eb7c3f6698a | -9.68238 | -57.22723 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 707eaa05-93db-3194-96f6-10da886ad8e5 | -9.68206 | -57.20758 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7394ad9-bea8-3531-a79b-f803b54c40d2 | -9.68144 | -57.21137 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27902dc6-559f-3c83-be95-c6edb0da43c6 | -9.67956 | -57.22279 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README77.md)
