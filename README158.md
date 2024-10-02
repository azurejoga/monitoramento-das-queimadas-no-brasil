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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 495ab753-96e1-3dfc-b1b9-4a6cfa1f71bf | -12.82555 | -62.52708 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11f7286a-595f-3ca6-9a3d-73cb67a1c07b | -12.82384 | -62.55948 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9695a4a7-69ba-3f62-a289-7c6d6b8ecca8 | -12.82011 | -62.5588 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| acf9d0de-fe7f-3795-88c6-4e1c3f5033bc | -12.81639 | -62.55812 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5a1e0a93-05eb-3616-a96b-b96bcc0d7f7c | -12.81066 | -62.52441 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adce1383-0bc0-3dc9-abed-16691dfa9f9c | -12.80693 | -62.52374 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4bc6513-3208-3572-a5cb-8b6a9f7db2c3 | -12.80615 | -62.52826 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 945bed3f-dd7b-3536-8c27-2af247fc352b | -12.80243 | -62.5276 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a2ce5f4-8fab-3de4-a70e-563a423d62c5 | -12.79342 | -62.53529 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9705860c-64e7-39de-994a-1f1cbe863cc4 | -12.79334 | -62.71474 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd8aae9a-c5d6-3015-867f-a5149041d8d6 | -12.77026 | -62.75845 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68741aaf-4851-34a3-8c55-918777101f12 | -12.46938 | -62.68721 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf0a10b4-735b-3389-bf74-c873689941eb | -12.46858 | -62.69185 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74105dc3-4469-3dcd-8a69-b8549652576e | -12.46481 | -62.69117 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebe3582e-2b05-3ab4-a50e-4f981b086de7 | -12.87977 | -62.77585 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82958ffc-7e6b-32e0-ae5b-c2ff1431b2a3 | -12.87624 | -62.52945 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 0cc994a8-8d1c-3928-88c1-07f387502d29 | -12.876 | -62.77518 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96d54a68-811d-3937-8016-eddf7a0b0e20 | -12.87547 | -62.52673 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ce0b4b9-a276-30c4-bb39-a6baae1d5c37 | -12.87545 | -62.53397 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5e55cbe1-bab7-31b7-a3be-c6b4f51af922 | -12.87471 | -62.53126 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2421776f-b52c-3d5c-9a94-2beb21742fe4 | -12.87395 | -62.53579 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| df575e48-7136-3eda-b80b-65753aaac1a2 | -12.87303 | -62.76985 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1565a1dd-4c87-3943-864b-014406d56596 | -12.87252 | -62.52879 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 86b32f9d-f733-3c88-976d-6447dd082ed8 | -12.87223 | -62.7745 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9f92b94-a970-313f-9f88-92d67c430e57 | -12.87175 | -62.52606 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| ea9aace2-082b-3f6d-b3e2-4e7efa5509a5 | -12.87173 | -62.53331 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ff93d96a-d4b4-369d-bed0-1da04f90e71f | -12.87142 | -62.77914 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e4fb640-a3bf-340c-9649-0c6d615b190b | -12.87099 | -62.53059 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| e9336d80-6232-3a36-a706-34e90ac4a496 | -12.87023 | -62.53511 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 018894ca-53d3-3ebb-a390-e433c8c9e92f | -12.87014 | -62.54235 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e7287838-1078-39bc-b80c-618c576042ed | -12.86959 | -62.52361 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ef0722a0-c4ab-372e-8b9e-0a3cc6b34d70 | -12.86946 | -62.53964 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1d203bf5-59ba-3087-8de9-21434772a794 | -12.8688 | -62.52812 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 872a607f-b96d-3630-b6f8-6d2cf3dbcb0a | -12.8687 | -62.54418 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 71b87b87-0358-3a87-822e-eba9a267483e | -12.86845 | -62.77382 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4db912d4-9473-3a43-87ae-69fe12fb14f2 | -12.86803 | -62.52539 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2479431f-9f2e-3662-a51f-b5cd718cc39a | -12.868 | -62.53263 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ff17a36f-1390-384a-9817-a79dc4abd35e | -12.86765 | -62.77848 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f5bd035-6a4c-38c3-ab77-d0251f4f03d9 | -12.86727 | -62.52992 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 47c06915-6648-3bb8-b689-57a1a9532c2c | -12.86684 | -62.78313 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac84f906-86ad-36bf-ad94-accbb23e8f7a | -12.8665 | -62.53445 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| ff788fff-2221-3d66-a0ed-4507916d388a | -12.86642 | -62.54168 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e6045d66-6957-3792-8e68-137a9b0750f5 | -12.86574 | -62.53897 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dddb2f62-c0d9-3487-b8f8-04686975ed21 | -12.86522 | -62.7254 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f1b3616-a25a-35b9-88be-2cdfe1c4fd0a | -12.86497 | -62.54351 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 462f115e-5da4-3299-9352-e871c7d6b6e8 | -12.86431 | -62.52473 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5cabbbdd-0c69-3d51-aac1-87fb7c0531fd | -12.86387 | -62.77779 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6350908f-3a2b-373b-b84a-338fc5b8e142 | -12.86355 | -62.52925 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c36c399-bbe3-3df4-90d1-9554dedf40ac | -12.86306 | -62.78244 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a32e9896-ae2d-3bd1-9efd-d3bd54d606d7 | -12.86278 | -62.53378 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4f2ed2e-d0a1-369a-ac25-1c3f6f21b622 | -12.86202 | -62.5383 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 824dcd4b-b967-371f-8d90-bf378cf23b38 | -12.86125 | -62.54284 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34f46e15-82af-3b05-bc67-6a3a050a9f10 | -12.86059 | -62.52406 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7f3d336e-2026-3dcc-8e27-f819110b96ae | -10.37253 | -64.0829 | 2024-10-02 05:12:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 018ccd42-0f1c-3efc-ac0d-8e5f189e66e8 | -10.37111 | -64.09095 | 2024-10-02 05:12:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cae11a5-8f4c-3456-afb2-0929917c6650 | -10.36687 | -64.09011 | 2024-10-02 05:12:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a5a708d-8368-31bc-bd37-b720e1670f15 | -10.62463 | -64.51899 | 2024-10-02 05:12:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1536744-0c2c-3424-b3a4-a784c982d371 | -10.62385 | -64.5234 | 2024-10-02 05:12:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63d74b6b-8b46-3cb8-8fd2-bac2bfc51c58 | -10.61589 | -64.51759 | 2024-10-02 05:12:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29c37a50-5426-3bcf-9e63-d126fdd007bd | -10.37183 | -64.08686 | 2024-10-02 05:12:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a2faa09-cf57-37b6-a97b-601bb53931ab | -10.36759 | -64.08606 | 2024-10-02 05:12:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd2c610-cb7f-364c-907e-2c342fb78422 | -10.05323 | -64.41062 | 2024-10-02 05:12:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5964b28-90b1-3f06-a2c1-b97ede7b9f68 | -10.26259 | -63.33218 | 2024-10-02 05:12:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c88abad-e5ab-3058-8ffc-f9a1009919e6 | -10.26197 | -63.33575 | 2024-10-02 05:12:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 820ef501-64c6-387f-a288-f8f6b39fc2ef | -12.31956 | -63.71585 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f306626-ac4c-3a88-8ef8-cae89aa3360a | -12.31894 | -63.7194 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b506032-45b3-30b4-8f7a-05f52802a7e1 | -12.31555 | -63.71508 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24cbee84-3890-3080-ba0a-db205e4936fc | -12.31493 | -63.71864 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f8f6a38-ec3a-3464-a950-2b923c659ffa | -11.98225 | -64.74025 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 379225dd-f74e-311d-b271-faf68cece6a9 | -11.75564 | -64.19446 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 212840e0-7783-398c-9f80-c1f85d602399 | -11.73258 | -64.10686 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bf3965b-9a65-39cb-bf4d-05158734c839 | -11.72356 | -64.13293 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57771f74-6d19-3f28-94da-63350c99503e | -11.71025 | -64.13032 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9a1270d-703c-375f-a938-90e465059346 | -11.70223 | -64.05345 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e032ab83-97cc-3b1b-94d4-65a904b211c7 | -11.67747 | -64.04811 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fd67b6d-a061-3b17-b8ad-a039832816ec | -11.67264 | -64.05119 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01d875c9-a05c-326e-9b7b-f9d033c7f7db | -11.66779 | -64.05431 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51d1982c-fe63-367a-be0a-d9e650a82ec5 | -11.66714 | -64.05795 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16ed6f73-66b1-33c2-ae04-f3608a5d4fa7 | -11.66707 | -64.01035 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2cccd31-4ddb-36c8-96f1-7b3a9a8d678e | -11.66688 | -63.98748 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d330f47a-a4d1-3409-b16a-e2ffcacce7be | -11.66299 | -64.00924 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40fcd9f3-efd7-36eb-91d8-e3bfa6e33d56 | -11.65763 | -64.20848 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6ad41c0-3f6c-3a75-b662-542f7389a445 | -11.65757 | -64.06355 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1fbe7fe-d5eb-37ac-9bcc-5c4432f14069 | -11.65676 | -64.02014 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03c90a1a-51c0-3b4f-9cb1-a0c0a72b5d1c | -11.65205 | -64.21552 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be27addf-1e5f-35a2-856c-bb5829afcf44 | -11.62978 | -64.02138 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d16fc79-36d8-3b6c-8656-7b698cca9e9c | -11.62686 | -64.11485 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f70848e-99b5-3c9e-9859-b8775593f4cd | -11.62629 | -64.11589 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e560af2-8a74-3ee8-b164-ca5ac04cfa0d | -11.62563 | -64.02067 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e02cc266-bd44-3204-9db9-82b1db76182c | -11.62496 | -64.0245 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0365ad8d-dc84-3195-a101-55ccbe3cf983 | -11.62268 | -64.1141 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 970a3203-9df0-3b90-b210-1e6da816f0db | -11.61982 | -64.07879 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8c66066-4479-3960-b9a0-bffc7b21d308 | -11.61632 | -64.0742 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf162dd6-837d-3f20-b49d-3cb7773d6b1f | -11.6155 | -63.95629 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 106fbfba-74cb-3f94-b760-8c42167482f1 | -11.61484 | -63.96007 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f1667e9-110a-3599-9ba6-a6dfbdb22f2c | -11.6052 | -64.18684 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e900868-13b3-3dc2-b6cc-ffadc704caed | -11.0032 | -63.92106 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4ad7687-651a-365f-9187-46171cad0aea | -10.99838 | -63.92078 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85fbd11e-5aa3-3251-93d6-4e00a4c3954a | -10.99773 | -63.92455 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a1b5e2c-8037-34c1-9ac1-d843a667c41f | -10.98605 | -63.94237 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README159.md)
