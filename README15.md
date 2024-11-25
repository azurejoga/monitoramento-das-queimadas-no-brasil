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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60f1fa73-c8e9-322e-87b6-fef18b0156e5 | -1.29912 | -51.73191 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8ef29809-bf77-3891-bd88-2bcc0a2ae480 | -0.91734 | -51.65026 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1c56f8b-0b77-34e3-977a-06fd66d1412a | -1.1327 | -48.35472 | 2024-11-25 04:31:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faaa4575-1b1e-3b3a-97d5-3b3f1dc6ec62 | -0.75933 | -51.7431 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d318681f-264f-3d7d-a648-e93015e22361 | -0.75879 | -51.74657 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 068ae0dd-c8d0-318e-b578-784c761e8e18 | 1.85288 | -55.89752 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86c2045a-7c55-3863-b4d5-edc3fc62d7c1 | -0.6235 | -51.70792 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76b0551c-eb19-3602-b8ad-c76fad543003 | -0.27751 | -51.50125 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb0b9b9c-3f92-3667-850f-3563bf32ba84 | -1.30627 | -51.73823 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18f21ce2-cd4f-3ca2-8e38-815f99676de7 | -1.76297 | -46.34473 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1a2cc4b-81a0-3e12-a9f9-599c71541887 | -0.36449 | -51.41096 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ab9dc93-e3fa-3938-89ef-a93134adc5ea | -0.81421 | -51.6158 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df7f57f7-4a08-3ca5-8d2f-81b669cadd55 | -2.11272 | -46.56562 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5d5312b-93cd-3e97-ba10-252a80207566 | 0.66647 | -50.80299 | 2024-11-25 04:31:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bb5d243-520d-35de-8cd1-efadb292c883 | -0.27905 | -51.5172 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e0a969b-001e-33e5-8583-ce91403d76f9 | -1.23233 | -51.79424 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7daf969d-0c14-3e97-9df4-09a95fca0003 | -1.30879 | -51.7407 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d3f5d7ec-aed6-37ba-8296-888aeb333736 | -1.14506 | -47.71073 | 2024-11-25 04:31:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2f2be51-ba89-378d-ae30-b680bef3bc40 | 0.28013 | -49.81139 | 2024-11-25 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e029372-f5ea-3eb0-8865-00eeda434986 | -1.08863 | -53.64292 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cee1d514-3b1f-3dfc-b26e-92ed3b4e86fe | 0.69386 | -51.44017 | 2024-11-25 04:31:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ced20697-84cc-3dc7-be5f-f45882618ee2 | -1.1961 | -51.97048 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23a51563-890e-37d9-89d7-0730459f7936 | -0.94702 | -51.72038 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 865e3c68-2ec2-3af0-9672-cc057782c1d8 | 0.31957 | -51.07623 | 2024-11-25 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e25dc7ff-4f32-320b-a21b-7965f1d2a683 | -0.95069 | -51.64492 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe52fd79-81bb-35c8-8af2-ecb55b06670e | -0.04866 | -50.815 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16716e1b-cc4b-3443-a72b-ac5e9d0b2895 | -1.08796 | -53.64718 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5621959a-74a8-3091-adcf-94f35e35cfe4 | -0.96004 | -51.71536 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe275711-55c3-3e2b-8855-a342447c2d90 | -1.31342 | -51.74458 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7246da49-0a58-39fd-8b12-6a843ab658f2 | -0.73991 | -51.95278 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87806a98-3833-33e0-b629-3c96c26e370b | -1.24828 | -51.745 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f8bfa21-b053-3276-bc5d-9d9ae94c47f6 | -0.23945 | -51.61205 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d862e1ca-28e0-34d3-9fd6-c3cbe42b733d | -1.12308 | -52.11546 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85aee9e0-aaf1-3596-889f-8fe811353046 | -1.13831 | -48.34093 | 2024-11-25 04:31:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bd7afe9-c6ab-39c7-8ef1-ab3c00ea1b76 | -2.11219 | -46.56906 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47eb9dbf-f144-33f4-bd18-addeb45383df | -0.94304 | -51.71976 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 124bfc41-f017-3e9b-9ec6-f3b5ed41592a | -1.23717 | -51.73803 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19981a17-eacb-3b7a-bf5b-c07497887428 | -0.94989 | -51.65 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a1271c8-1587-3050-b39e-34de6ffdccf1 | -1.30714 | -51.75089 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f241243f-1131-3222-ac35-973fe775eb8b | 0.71938 | -50.86355 | 2024-11-25 04:31:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fa04aa1-4c15-32cc-91d2-8179ba0b5e36 | -0.88559 | -51.7215 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4871c36-03e4-32f1-a54e-d551502c787e | -0.9868 | -51.7164 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49999a89-ac79-31a9-b39f-c80744b73321 | -2.22676 | -46.40235 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e51be393-db3a-323f-a9f9-69854ec9946c | -0.27651 | -51.61062 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81d46280-55a8-326e-96c9-c666d50c6890 | -0.96402 | -51.71598 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f91a80e1-c803-3f08-9dbf-bd691ee88d51 | -1.31264 | -51.74967 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c7c56bd-f935-375f-8146-21d046139f4d | -1.19468 | -51.77434 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72f22ad5-2364-3d65-b206-3a8695e42904 | -0.97305 | -51.71032 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bba06d9-c790-3845-bac8-3f890786d31f | -1.11548 | -52.11058 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b4ac2c0-a922-3edf-ab07-5ca18685327c | -1.19069 | -51.77374 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c3df84a-e10e-3dd0-9899-f99e68f15806 | -0.79872 | -52.42298 | 2024-11-25 04:31:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c15ce62b-97ba-32a8-968c-a09781eaa0bd | -0.6658 | -51.66161 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c14e156-75dd-327d-bbf7-84ed432ad6b7 | -0.27706 | -51.60716 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3edb35a3-5f18-3808-b513-b938bba60656 | -1.31193 | -51.74642 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 77c7ac5c-b7cb-3a18-a1b3-18ff3455967f | -0.05628 | -50.81617 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7a8acfb0-f9de-3561-b524-83cbfbaad0be | -0.75639 | -51.73554 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6896d978-f38a-36c2-ac4d-a78c2abff3f9 | -1.19578 | -51.7675 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbb30302-ed05-3ec8-83b7-93acae594013 | -0.35693 | -51.97357 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4f3fadf-11cc-3c76-9005-4c57f47eb62f | -1.29118 | -51.73069 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 886c12ad-4b54-3ed4-8be8-a53866e78f12 | -2.22228 | -46.38744 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90e6fcf4-d9b5-393c-abaf-d0bb8efb4b0d | 1.85234 | -55.89386 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d438308d-7bce-3c30-b4ec-1f8ff7b8aa63 | -0.91419 | -51.64454 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ba03901-92de-3a58-b2ce-f126e1cf3fae | -0.20016 | -51.64044 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afe49227-f368-392d-9ba1-1bdadbb870c2 | -1.19125 | -51.77031 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bf65f05-3576-3d84-b989-287798f583a6 | 1.50866 | -55.67466 | 2024-11-25 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c26ec0e-a322-3cd6-a624-3168e64e1f09 | -0.14521 | -51.29556 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 088a5733-fae5-3800-9e93-a45b0c838df3 | -1.04382 | -51.74271 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14cc4220-c25e-3938-b1fc-d41401fe853c | -1.2896 | -51.74089 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 253d3311-b1aa-3d65-be4f-a9c88ecd3b99 | 0.97298 | -50.1258 | 2024-11-25 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f280c5f-dc48-35aa-a435-db1912e0c0de | -1.24511 | -51.73928 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f161e610-e52b-3f5b-af5c-8b4c6c01ea23 | -1.25496 | -51.78016 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 002d7145-a5b0-3643-b934-66f0325bb18e | -0.96907 | -51.70972 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 740a0b4b-e2f9-343b-afaa-23b739995095 | -1.30961 | -51.73561 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2e9d22b-0e92-3ed2-8e38-240b5f14fd02 | -0.57399 | -51.73582 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c40313-032d-348f-9bf8-a94cbc9d6418 | -1.14848 | -51.69007 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6831fa22-49b3-326c-afc7-0f58d0277673 | -0.66745 | -51.66163 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32e9b819-59b2-309d-bc77-41c130467a59 | -1.25939 | -51.75196 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 602c96af-8b92-3dbd-88d6-92fe343c801a | -1.70115 | -46.23882 | 2024-11-25 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8030e04f-c19d-3870-84fd-963f5fcc7444 | 0.05038 | -51.72399 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76507bb7-e2e4-3ccc-a801-c2a6bbd1dc20 | -1.22725 | -51.80046 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60e24458-7de5-35ff-af09-7ea6ccf74c8c | -1.20306 | -51.74766 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58fb1aa7-c4c7-381b-9390-7df09f74b489 | 0.94669 | -50.73804 | 2024-11-25 04:31:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6c1e4d25-fe45-3cf1-80fd-bd74cc307c08 | -1.23287 | -51.79081 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d4799f87-b493-3ce3-97ed-2c46e905ccc5 | -1.70725 | -46.24332 | 2024-11-25 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d688ad91-0442-3520-ba51-89aff9f403a7 | -0.985 | -51.71214 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92401096-cd02-39c0-bc38-e977c295eb29 | 0.33212 | -49.71857 | 2024-11-25 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a71976c2-5119-30e2-815f-dcc2a1e6b842 | 1.24475 | -50.72641 | 2024-11-25 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9d4b1ba-3ed3-3ac7-9826-9de131d5f2a9 | 1.38324 | -55.89285 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 570229e2-9068-3c0b-bcba-36499b0dbfa8 | -1.60357 | -45.57907 | 2024-11-25 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e69da12-d31d-3434-96b5-cbbf02a852b2 | -1.72102 | -46.22052 | 2024-11-25 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94cbe7df-ba77-37a6-91b5-5ca3f50dcea6 | -0.5784 | -51.70809 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47660e95-9bb6-3c0f-9856-353c7dcd0f8a | -0.05247 | -50.81559 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa67c4e4-1e66-3201-8dd0-e0fc26a5e628 | -1.73956 | -46.29853 | 2024-11-25 04:31:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c2b17a-eed9-3559-8d15-96de5ad71324 | -1.19523 | -51.77091 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98505337-57cc-329e-8349-b673bd9c49df | -0.24744 | -51.61327 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bfb2ca1-005e-3af3-94f5-3961225d3e98 | -0.92759 | -52.64928 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7f08d3e-70dd-30df-9160-806ab327407e | -5.9743 | -46.29731 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44640849-b8dd-3142-8fca-12316f984d0f | -4.26304 | -48.69662 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12092534-96e8-3b02-8dd4-e2f4e2fdffc1 | -4.20378 | -48.11974 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8548524-6677-36f4-849c-d6b62a1e5cb4 | -3.50964 | -53.81725 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
