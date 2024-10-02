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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14086a06-da31-33ac-9c22-44302ef52a16 | -14.76175 | -48.79872 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bc05bf13-7ff8-30c2-91d5-91c901f35e46 | -14.75859 | -48.79367 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3006468-526c-3da2-bacf-ef9935b47734 | -14.75798 | -48.79804 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8c4bb58-f5eb-3a93-8246-5539b344e3a6 | -14.75735 | -48.80251 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee65e0c3-efc0-39bc-b18f-64e5fccbf54e | -14.75105 | -48.7923 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47011fe0-56af-30c5-8e19-c94871fb0d30 | -14.75044 | -48.79672 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f358b388-f8ea-3f31-b0bb-35f35574c273 | -14.74788 | -48.7873 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdefdc0b-a394-3adf-8c86-3d571646ae05 | -14.74727 | -48.79169 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 801f5c0a-9bd6-3a11-b16c-d9b8b0bc51e2 | -14.74535 | -48.77767 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2996e0fc-45b4-337d-ad75-3e06f330ae19 | -14.74411 | -48.7866 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea485452-d147-3b6e-9bdd-0f3caa51a62d | -14.74097 | -48.7814 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dce4f69-5aa5-32ad-9aa5-6b74e6db9750 | -14.74035 | -48.78587 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba7d6894-dd30-37e6-a0e5-7ca659a336fe | -14.72647 | -48.77442 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60c62ee2-fc40-355b-8651-4b228c8858a0 | -16.10537 | -50.30373 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66e2ccb4-b153-36d8-acf6-02a00c335ef1 | -16.10504 | -50.30269 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52786593-e186-31b3-80b7-20c3b194d67c | -16.10476 | -50.30793 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 504d17cb-ced2-3116-b302-46fb484a1865 | -16.10445 | -50.30688 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c093e4f-7698-38a8-ad79-b279f56f40cf | -16.10386 | -50.31108 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1f1939a-de5c-3fdd-8ad6-f30bbe569256 | -16.1018 | -50.30333 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bf73017-4aa1-30a5-a5b2-777d954b32e7 | -16.10119 | -50.30753 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f50d74f6-87ae-323f-9d53-7c41e12b4a89 | -16.08746 | -50.30209 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 975b5281-c60b-341d-bec0-485a9e1ad402 | -15.92454 | -50.14875 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ff3734f-51c8-38c4-b214-d439e6c2eef3 | -15.92094 | -50.14837 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f878d1e-1950-3955-a298-a55ef53387ea | -15.92037 | -50.15246 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 790f7741-5ffd-3eb2-a706-76f5dc6593af | -15.91676 | -50.15221 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f079820-53de-3834-b2a6-c9cd0e53b122 | -15.91618 | -50.15636 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b79ff3d-8626-3e76-854e-33a037153678 | -15.91616 | -50.13035 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eec9f5a-5d48-3212-9af2-42e9a1872883 | -15.91389 | -50.15386 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63f5403f-6fad-33e9-8eba-fcce6f6c9abc | -15.91343 | -50.1319 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 565a837a-02b1-3783-8882-c67d972dc762 | -15.91316 | -50.15194 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a954751a-1257-3e80-bf07-e975c9a16ee9 | -15.91259 | -50.12976 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b1f41cd-a7af-33e6-9b4b-e8cc1935e90a | -15.91258 | -50.15606 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87bf8ff7-31ec-3873-8ae7-c77e981ad6e8 | -15.91091 | -50.14925 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9ed67dc-e564-3f7a-8528-f4fe17b1d367 | -15.91031 | -50.15339 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db6a116d-0707-38bc-9c5a-f35e7191102b | -15.91016 | -50.14728 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd80ac08-90de-350f-83e1-10245077e54e | -15.90958 | -50.15142 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 756bf70b-728a-3e72-a664-bd76e606742e | -15.90901 | -50.15548 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ca18880d-9e61-358b-98a9-da798cd822ce | -15.90858 | -50.14015 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ddc5d8b6-5df6-3f3f-bb65-dff076124d85 | -15.90795 | -50.1445 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 33d61b89-81d8-37a9-9e81-71c3eb209346 | -15.90734 | -50.14869 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3f296942-c6ee-331e-88c8-a662ad50e205 | -15.90675 | -50.15277 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4160f299-92a9-35a5-8156-1b7ef584979e | -15.90438 | -50.14393 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7af4766-9384-3bb9-a8de-19e39b4a494c | -15.90377 | -50.14814 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e67ee1cb-1ae5-3dca-b35f-f9fa39e4e02c | -15.90319 | -50.15219 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ebb0d041-61d0-3258-93d4-41452a0ba9dc | -17.16047 | -49.21643 | 2024-10-02 04:49:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a66cfd5-8399-357f-b5da-6fc4dc390c8e | -12.17195 | -50.49122 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 471e9670-312f-3666-94e9-1002b212c23c | -12.16318 | -50.08177 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd0b4349-e845-32cf-aea3-e665cec592c3 | -12.16087 | -50.0735 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2001fceb-a3d3-32ed-a0a4-69ea5727f2fa | -12.1603 | -50.07737 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fde7bd39-0fc0-392b-9878-b4f9bdbd7522 | -12.15624 | -50.05697 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a92650c-41eb-338f-960a-02f2c8cffb2b | -12.15567 | -50.06084 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5aeaa992-41d1-3cbc-9282-b0e897a3f039 | -12.1551 | -50.0647 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4a0f0fde-1353-3048-a2ef-80a1e6ea5cf0 | -12.15335 | -50.05257 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6d89cf77-0714-3969-b26e-9528e5317c3f | -12.15278 | -50.05643 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ce93b1b8-b2d1-3a78-a144-fa9d9eabaf14 | -12.15221 | -50.0603 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2017b5ca-57dc-3cca-9719-e541a815d93c | -12.15046 | -50.04816 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 961f046a-5c59-3f1e-a64e-acd6c228ed31 | -12.14989 | -50.05203 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a7bb2c68-20fd-325e-a983-82c0cf954411 | -12.14933 | -50.0559 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 18f7b798-a7ac-3a75-b16f-1263a200e38c | -12.14876 | -50.05977 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d4f9e55-79f8-3a49-bd4a-59bec89ae9a4 | -12.14644 | -50.05149 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7799defb-5159-39fa-8d07-e41bd2b0c7fa | -12.1453 | -50.05923 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efb7c562-33e0-3dc6-9e8c-2b372d01071e | -12.14411 | -50.04322 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 954792b4-a635-3f64-911f-6e862ee1b96c | -12.14355 | -50.0471 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f5b0fd8-fdfd-3780-91b3-4bc0dfc6ff0f | -12.14066 | -50.04269 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2bb1f067-4609-3955-a10e-b28011c909e0 | -16.1045 | -50.33245 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d79d1865-5434-39b8-bd3e-8fdd52a4cd8e | -12.14009 | -50.04656 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 150a7dc3-3773-3329-878f-b3dcedf3e70e | -12.13374 | -50.04162 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d52e27bf-eb98-325c-a8d1-4eae7bdab220 | -12.13317 | -50.04549 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27931df1-25f9-3d2b-9dca-ccf22b1129e9 | -12.13077 | -50.04545 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c306847-9b7a-3e64-ab9f-cc7f57a515ab | -12.12971 | -50.04495 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0931f302-26ea-3449-a375-161c53962abe | -12.12731 | -50.04492 | 2024-10-02 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00a86dbe-ebd8-37b6-893a-5be1928e93ed | -12.03931 | -49.69165 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c5262c9-25c7-3542-8f0f-298c8ef4a82c | -12.01052 | -50.30839 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9671c22-ade6-39d5-a512-9c83ae8816db | -12.00996 | -50.31218 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95c78beb-d67a-3ab5-8373-0ad587fb1edf | -12.0071 | -50.30785 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0355e8b-c31b-3e35-ba10-81976a9181ea | -11.97255 | -50.18692 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8f2a266-292b-325c-bbd0-977be25a9bf6 | -11.9336 | -50.16529 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68ca0062-8fdb-3b78-82b3-aefc096ccae7 | -11.93017 | -50.16475 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 423effa0-e347-39c8-83bd-c3b516a702df | -11.90555 | -50.16484 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fb0e6cc-4c20-3388-952d-09d77848909d | -11.85684 | -50.65543 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a4a14a6-4a44-32da-b9f5-adeef8acfbb3 | -13.63426 | -50.34139 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0aa2f50f-1482-3bdb-9f37-89ce3dc0cbe6 | -13.63311 | -50.34923 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 539a4c75-cbba-3dec-9513-0f2d86388650 | -13.63136 | -50.33694 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa62b473-9f65-3797-b9ad-444913f711cb | -13.63022 | -50.34478 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 18703a83-babe-34f9-b8af-df8b8661629f | -13.62965 | -50.34869 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e73d18b-7068-3e41-bce1-562af5879f83 | -13.6279 | -50.3364 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ce03788-6ccc-36f8-8e73-fdc8ad2fcba6 | -13.62482 | -51.0932 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16464d4e-6697-3e6c-b247-1c1be7b984e2 | -13.61745 | -51.07307 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5db316a-f891-36c2-bcc3-61b4301e5940 | -13.6169 | -51.07678 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef2b368e-96d9-3586-8676-17422d0fbaaf | -13.61487 | -51.15971 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a3cf326-d11f-3aab-8610-707152b61a34 | -13.61083 | -51.1175 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39f8fe8c-3268-361d-b05a-3c51d42f1d55 | -13.60819 | -51.18129 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77a4ee6c-7e83-38fb-b7f3-bea11d63ccd6 | -13.608 | -51.11327 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8899f8e2-8434-3850-9808-a2549cc020a3 | -13.60764 | -51.18497 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56e31c85-cbc3-3815-9bd5-bccfb519d02e | -13.60745 | -51.11697 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4db0ee0-8666-3a90-951f-18750396e388 | -13.60537 | -51.17707 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eefde902-b534-39c4-b3e3-b7d4dc586488 | -13.60256 | -51.17285 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08327120-277d-3d5c-be50-63b623b03ce5 | -13.60201 | -51.17653 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6da09e5e-320a-3740-81b2-92518b1d0ec5 | -13.60139 | -51.15757 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e152479-3be2-3f0e-9b6f-a92e585c83d3 | -13.59462 | -51.1452 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README98.md)
