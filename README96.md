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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 814eead1-ccff-3bd8-aa8b-d6bbeedcf88f | -13.20927 | -48.62704 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bcfc05cd-b21c-3edf-b0f2-2d58b0123c23 | -13.2092 | -48.62026 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f149849-bacf-3751-97de-a76c1a01fa86 | -13.20871 | -48.60331 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9adc86ec-ab2c-3991-864c-e15461a3151c | -13.20864 | -48.63161 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ce1ea52f-5894-3736-9c84-420fff70c067 | -13.20854 | -48.62483 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1edaef85-3ef6-368c-aba4-dfe57dae788f | -13.20815 | -48.60101 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08faf766-df3b-39c2-a1fe-43fd6b105a46 | -13.20806 | -48.60806 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c1e1b2b-b023-37ca-9d1b-92f566648016 | -13.20801 | -48.63618 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| bc03e5c1-2440-3827-a33c-97ea6f7e1187 | -13.20788 | -48.6294 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bb8a6789-c257-3138-acce-fcdd7c7d059a | -13.20741 | -48.61277 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46d59354-c291-36f0-a083-f0e9e8dae30f | -13.20722 | -48.63397 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| efea3fc0-0f64-3610-96ac-c0c4ce3a83d1 | -13.20677 | -48.61055 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db97afec-1f11-300f-a891-f522f43a4d6e | -13.20616 | -48.62185 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72bf12c0-ff41-3743-a0a2-6d7ca7b68e68 | -13.20553 | -48.62643 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 275827e2-edf3-3f5d-9be8-88ad652c6f2f | -13.20546 | -48.61967 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8559a370-9f29-382d-a783-d3b11f23e3a2 | -13.20489 | -48.63102 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f1de879e-bcbb-34c3-ba3e-6ef39372762e | -13.2048 | -48.62422 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3bb434a7-8713-3831-8498-d0b5421816fb | -13.20426 | -48.63561 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 349dadcd-387f-329c-a634-edd88455df35 | -13.20414 | -48.62881 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 35bf137d-d576-361d-900a-6e492f2360a2 | -13.20366 | -48.61224 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5567aa42-06c3-385b-8adc-71ff129d4fa0 | -13.20348 | -48.6334 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fd0403df-cbd8-3dc7-abad-c1b147775eb2 | -13.20303 | -48.61678 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ca47116-caec-33c7-84d8-a7b95e2f7031 | -13.20302 | -48.60997 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 004d6c5d-fed0-3871-b1d6-bf009dce31ee | -13.20241 | -48.6213 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bdb04185-c8e6-39b9-9efb-b201ba371122 | -13.20235 | -48.61464 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f3e541d-113e-36df-a8fe-725f33208212 | -13.20178 | -48.62589 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 76b9da39-40a9-39b0-9927-239f5f3f88a7 | -13.2017 | -48.61914 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f19b5f5-1785-3042-be45-bfa40438d4d7 | -13.20115 | -48.63048 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ca20e085-da90-3339-a87e-bb5a20013cd9 | -13.20105 | -48.62371 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8990b979-8717-3ee6-8c3e-d41531f3ca50 | -13.20039 | -48.62829 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2195e1cb-4395-39e3-8bfc-d12920b31a44 | -13.19991 | -48.61164 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1a0f396-9f98-3cc4-a6e7-c5a1db54d598 | -13.19973 | -48.63285 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f463490a-8509-3844-a11a-407815dcb95d | -13.19928 | -48.61625 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 246547e7-c861-3334-a2fb-895f6ba62447 | -13.1986 | -48.61407 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12bfe18d-73bb-34d3-b516-f39e42729280 | -13.19795 | -48.61865 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 820c10c5-d850-3a4b-9e74-deb0ab21d568 | -13.24007 | -48.59821 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7acc5407-d9fc-3bdc-9333-2ec16f2ecfdc | -14.81013 | -48.75714 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c419b0e-b75c-3b51-953d-8319e99a65fc | -14.80968 | -48.75878 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 06c11719-8337-3d3c-bfc9-fb67a981d6d3 | -14.80944 | -48.76206 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a576afd5-b034-3969-b41e-455b6846c937 | -14.80901 | -48.76372 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68c1f876-8895-34c0-9bf3-82df58a35f90 | -14.80873 | -48.76702 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eef1b6d0-6fed-32d3-8bba-fcff6c576346 | -14.80834 | -48.76871 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d27587b-6fe6-3e1c-ba04-584d2c9418aa | -14.80634 | -48.75655 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb15c2aa-d301-3be8-ae84-340818deaeae | -14.80588 | -48.75819 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6eed4ebb-9cb0-325e-9b72-7818cd91065e | -14.80494 | -48.76651 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9830196-7036-3d40-820b-d5f9b5637630 | -14.80454 | -48.76822 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20f60372-1ed4-38eb-9c5d-7b51ff99951f | -14.80114 | -48.76594 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5726c6a4-597a-3719-b220-c868cd432738 | -14.80075 | -48.76764 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2eb44bf-bd16-33c9-91d9-545e1a171b8d | -14.77769 | -48.76756 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 022f91a0-7355-3965-86d3-471a57e2714b | -14.72711 | -48.76974 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e72c2221-3aae-3b32-a3fb-e062a6143ea6 | -14.72331 | -48.76926 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19067cf1-a9bc-3d6a-82f5-7778369f2e64 | -14.72154 | -48.7538 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f61ea6bc-7350-3bb0-b84f-e3681e24f0b7 | -14.72083 | -48.75908 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88f12095-216f-3548-9424-1d5590c709a0 | -14.71703 | -48.75858 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e46526e-1374-340d-b0e0-cb914d2d0916 | -14.71634 | -48.76374 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 306926d2-1764-3dfd-84b7-a119405a9be0 | -14.7157 | -48.76836 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cfe7e173-c861-36d4-886d-3a2894f5ecbf | -14.71253 | -48.76332 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdff44bd-2205-3b8a-90ab-d69bf2e7fb33 | -14.81628 | -49.0471 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52d2e721-54a4-3699-830e-5a06e0f1405e | -14.81499 | -49.05634 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d29b36f2-0135-3d55-9e6e-5ce4ede7724f | -14.81318 | -49.04194 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97a786fc-11c6-30a9-bf21-240a021309de | -14.81148 | -48.77416 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e002dbac-f572-3331-86a4-b4f5d6b95c47 | -14.81126 | -49.05582 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 238423b5-abc2-338c-909d-f9e22b377a9c | -14.81113 | -48.77744 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 804920ba-38a4-3da5-85b8-04b6ce8d8b85 | -14.8108 | -48.7792 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d963ce3e-10c2-3bc4-924a-026949fb5d1a | -14.81062 | -49.06042 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a5b3c66-36a7-3a21-8048-e007b212643f | -14.80817 | -49.05064 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b123e28-8cb8-3b9b-926f-e9172ed7c86f | -14.80803 | -48.77201 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e645c63d-3a81-3c57-b419-5755f69282ff | -14.80767 | -48.77372 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60dde7cf-180e-380a-b510-aedad7e2a1f7 | -14.80752 | -49.05527 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd9b2ccf-9cb4-3af1-913c-20953abe5abd | -14.80732 | -48.777 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f7b160d-ba98-3f33-9a75-b7b596b07274 | -14.807 | -48.77872 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0f1d540-5c1e-3234-80ef-bf0a2c4d4cb6 | -14.80689 | -49.05984 | 2024-10-02 04:49:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99cfb975-0545-35b6-af2e-565db3a20096 | -14.80659 | -48.78213 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7617d60d-002b-3a9d-84e1-2d35e4f5d5b5 | -14.80351 | -48.77656 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3107dad1-8294-35d2-97be-b2edd48b965b | -14.80319 | -48.77827 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 303d83c4-901e-34fc-8423-39c500d98fd4 | -14.8028 | -48.78164 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 544f04cc-79a7-3624-b253-5be7b8ca07dd | -14.80007 | -48.77271 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c61c172-02d1-3bea-b30a-5cdf7875f95c | -14.79971 | -48.77608 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 971bfe4b-bd8d-3c60-9e30-3e0a1040bf10 | -14.79939 | -48.77783 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98378b21-b48b-395b-abb8-0454457d1117 | -14.79899 | -48.78119 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c8e8e4e-b1d7-35ef-9608-10f4be1c5296 | -14.79871 | -48.78292 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 696582fa-3710-3996-b72c-a1f111cb0829 | -14.79828 | -48.7862 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25254fa7-d8b6-3878-b5b3-5f1f39264801 | -14.79805 | -48.78785 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b92fe8a-5287-3170-8db8-3360f876f767 | -14.79763 | -48.79086 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaa92efc-4269-3b65-b9f6-408879ab1555 | -14.79449 | -48.78566 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04037aa5-4b01-319f-9b51-97afb22a5708 | -14.79072 | -48.78505 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9cd9d27-ab87-37f0-ae30-9171536f7ab0 | -14.78694 | -48.78442 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 27b318cf-4e7f-3e55-840f-ff00d52d8bc2 | -14.78628 | -48.78909 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ee2630c-566f-35ca-b244-fe1282cc738d | -14.78384 | -48.77895 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1d4920e-8327-3d65-b183-ea76c96d6e4d | -14.78317 | -48.78369 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 84a1cd5b-5fea-3a35-8dc0-8f5fb9d1cb27 | -14.78253 | -48.78828 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e72e4b5-2e14-396f-a7d3-c23f2f4b0e59 | -14.7794 | -48.78302 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 98b8accd-c632-3919-a4e2-03be68a653e9 | -14.77877 | -48.78751 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8cdad304-7e40-3073-a1ad-4b12e6a6b62e | -14.77698 | -48.77269 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90f392f5-7f5d-3ce0-abee-92df585044ca | -14.77497 | -48.78702 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e03225cd-383a-3487-a56f-d103aca06022 | -14.77434 | -48.79151 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e1ada9b2-e662-3f69-b145-8f0af157dd77 | -14.76992 | -48.79552 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7794fdcf-cc32-3c7b-a81b-dbc05c8d2db6 | -14.76614 | -48.79495 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f5a1282-ee0e-30a8-a6ae-f3693b499707 | -14.76552 | -48.79932 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21d84fd9-0a66-3aaf-8b96-9f3990e6c278 | -14.76235 | -48.79438 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README97.md)
