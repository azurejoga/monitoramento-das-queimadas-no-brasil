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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bb5f175-1981-3d64-a0f1-7c3acc08c4ba | -9.54918 | -50.20746 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fcfa05b-0826-36b2-b1b8-774306608154 | -9.54857 | -50.21157 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69d74b72-95bd-32a7-a5bd-2a17b7c4e0d9 | -9.54499 | -50.21104 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47f79b69-fc3b-36b9-8c4d-c61ae1db0e7e | -9.54202 | -50.20639 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cdc2d94-0f5e-349f-8cd1-96962dea7e26 | -9.54141 | -50.21049 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fe35403-7327-3e47-ba4c-44419925155f | -9.43053 | -50.15259 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c096dcd-00bf-3c97-99c5-6b6f5309b3ce | -9.42993 | -50.15672 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9926f31d-171f-3dac-80a9-6d16fc59e1bc | -9.41359 | -50.03257 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b2d6985-ebe8-3553-8bec-9dcabe7d2ec3 | -9.41297 | -50.03676 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16df35ff-b829-31ca-b673-ddcf88ff0f65 | -9.40936 | -50.03622 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 775c6ea3-9b34-34e4-86d6-00019d46aaaf | -9.39446 | -50.01262 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a6d1969-fc30-3454-909c-78e2d46c1cc2 | -9.39384 | -50.01681 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83f68f7a-31e8-39ad-a786-7914c72609ab | -9.39148 | -50.00789 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3668d6f-400d-3e97-b247-c4a0f403fc8a | -9.39085 | -50.01208 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27ecec35-c011-3bd6-9f39-35f254f192f6 | -9.39023 | -50.01627 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52a45fc9-f0f2-3fe6-9f47-5d07232b58f6 | -9.38961 | -50.02045 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f510101-24a5-3853-8c53-3a28b220ace4 | -9.38787 | -50.00734 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbfba66c-a1f8-3a4f-9e55-fc0af6b654c7 | -9.38538 | -50.0241 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23e556b2-3b77-32e3-a58c-94ec8aa20e56 | -9.38426 | -50.0068 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18264e95-4a71-3032-a0a4-fc305cec5c63 | -9.37705 | -50.00573 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 804cddf5-682e-3d86-a3d2-251cc3a5327a | -9.37643 | -50.00992 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33d5c3a6-eded-3394-9577-1ec5204b6c6f | -10.76095 | -49.85567 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1856c86-1382-353a-b36d-db2345f9fb6f | -10.76031 | -49.86011 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e42900b-df21-3a8e-b42d-ebae7f207d3a | -10.63281 | -49.92178 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 802f56eb-5591-36f4-ab6b-2c4a8ddb1a55 | -10.63257 | -49.19129 | 2024-09-29 04:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d7244b6-5826-3836-9390-d4542b6cc8b6 | -10.63241 | -49.92026 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a16967b9-e2d7-3afc-b2ad-5bb7be17e2d3 | -10.63043 | -49.91248 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68b4a682-3c98-3a93-9de0-a1037c67a3b2 | -10.62978 | -49.91685 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d2d79a8-8c32-303f-ae4f-27cadb9931a3 | -10.62935 | -49.91533 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e9fabd-9e4e-352f-8d73-b57cf97333ed | -10.6274 | -49.90756 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e7f95d8-3827-3eba-914e-d97dea5412bf | -10.62675 | -49.91193 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33522271-b71d-3a5b-a86b-6b25c14cf595 | -10.53219 | -49.4547 | 2024-09-29 04:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fdb51ee-f82f-372b-bd35-262bc348786b | -10.4483 | -49.17638 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c54be4-403a-3e52-bbd5-ea4d74d3ff68 | -10.13574 | -50.00052 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf08567e-2f45-352e-9b85-bc201efe67b6 | -10.13147 | -50.00426 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4ee6c56-f539-3877-9792-3d9ff8f86462 | -10.11629 | -50.00636 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3c74d88-af05-344d-9006-dcea1f436488 | -10.11265 | -50.00581 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4e4e43e-5489-3f44-b750-fce01069b381 | -10.10901 | -50.00527 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4a6936c-41ac-35e6-9913-7137d6705021 | -10.10538 | -50.00471 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d86bd26-0c6a-377e-9903-aa0e84e295ae | -10.10476 | -50.00899 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a74216e-1f60-35e3-8a74-b0e0fb593220 | -10.10174 | -50.00417 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 814d234f-3314-3e78-84fe-0c7a3bf97689 | -10.10112 | -50.00844 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2973afed-edbc-3e0d-981f-1050a2f35548 | -10.1005 | -50.01272 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 304a14b7-f55b-363b-9480-17e50746be5c | -10.09748 | -50.0079 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df872ad9-76c1-308f-82e5-4c6bcbef13ee | -10.09686 | -50.01218 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62deb749-42f4-3ff9-82b7-2f6b3189214c | -10.09323 | -50.01162 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c6a65ba-43e0-3f4d-8b64-e874f3db31ce | -10.1831 | -50.53699 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e20a39-11f1-333f-be5f-6af2e5c450b7 | -10.06069 | -50.31125 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0d97e50-95ed-3261-acdc-33debf8c5c72 | -10.0571 | -50.31071 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9368b40-3173-3256-a93a-e41dd77c8594 | -11.69319 | -49.96921 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3de72086-d585-3672-acab-94a868378c70 | -11.19718 | -49.93569 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bbd81f9-74f9-3096-b35f-ae916572383d | -11.19666 | -49.91288 | 2024-09-29 04:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9768590-875a-3d4c-9cf2-c01a25ddef5b | -11.16045 | -49.73046 | 2024-09-29 04:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 693fbc92-9ccd-3eb6-85a0-4189cf21188e | -11.1424 | -49.72318 | 2024-09-29 04:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 910fc9d4-7f4f-3a44-8337-495a493db1e3 | -11.1042 | -49.58368 | 2024-09-29 04:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 139f2ca0-8a27-3c07-91de-24130700466d | -11.10353 | -49.58831 | 2024-09-29 04:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b859957-3e08-3ed6-bb7b-c726f50d3fe1 | -5.03302 | -49.76919 | 2024-09-29 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f470622-d8af-3833-a4c0-86fa7fbd6871 | -4.98718 | -49.77846 | 2024-09-29 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247eedb0-9d20-366b-b932-efe9a105d352 | -4.94685 | -49.9249 | 2024-09-29 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9578fc58-0070-3098-8901-6bbc91854711 | -4.84831 | -50.93238 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e77ddce-83bc-3503-b62c-afe276b2e0be | -4.8455 | -50.92833 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9933a39-737d-37c0-abb8-f4430c37f242 | -4.84496 | -50.93187 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8520360a-c607-3532-8241-d62d224c65bf | -4.84441 | -50.93541 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f54bda8b-f733-3621-adf1-a36dabe68766 | -4.84215 | -50.92782 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 555f8ae0-961b-3702-8cad-31095744c8c2 | -4.84161 | -50.93135 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9db953dd-4f0f-36ba-acbd-f8afe9f3852d | -4.83989 | -50.92726 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c60a516-571d-3ec7-9a11-8959eac2c0e3 | -4.83934 | -50.93079 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3742d85-af3b-381f-8ef1-9e412b5b3002 | -4.83879 | -50.93433 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73469ca5-5e18-3ba5-831f-6d78153a36f1 | -4.83709 | -50.92323 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7734e8f3-31f0-30c0-91ad-6b283b097e9e | -4.83654 | -50.92675 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7ff9c48-d400-3a98-8c0b-fe0349999e14 | -4.83599 | -50.93027 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc93d1d1-74ba-3fc4-838a-c412a8b3c71f | -4.83544 | -50.93381 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 749f884c-e535-3d53-9e80-24007b306966 | -4.83374 | -50.92271 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25666cd2-a311-3d73-a6b4-c72377ea76e1 | -4.83319 | -50.92624 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee674375-4082-3a4c-b3e5-9bc89badbc05 | -4.83264 | -50.92976 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55b03257-a522-327c-ad95-df33813a1c35 | -4.74014 | -50.42656 | 2024-09-29 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 441c2738-3282-3508-9c15-6a0870ba5588 | -4.39453 | -49.64048 | 2024-09-29 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 046291ca-3a19-38cd-8161-c65d4540e4a0 | -4.39104 | -49.63994 | 2024-09-29 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f663a50-d548-3119-9708-1f3ba8bba609 | -4.27929 | -49.96156 | 2024-09-29 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d891b85-1547-3496-81df-81c7fc3893fa | -4.07189 | -50.42245 | 2024-09-29 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66d6cac1-5b31-38cd-98ee-02b248a68d3c | -5.78704 | -51.03629 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33961f4e-eb6c-31bb-8674-75d5c7156541 | -5.78649 | -51.03979 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a8ff3e4-8cec-375f-85b0-661bac16ed9a | -5.78595 | -51.04326 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b7534d-e30b-3a48-9361-b3928e15c89a | -5.78423 | -51.03223 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8db0f111-849a-3c6e-a88a-fce90524e89b | -5.78367 | -51.03579 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8a569cb-e4c6-30d5-a815-96e8348b98af | -5.78313 | -51.03931 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f12e378-a1b3-35ee-9368-eb725c5962e0 | -5.78259 | -51.04279 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32906d0a-e201-3794-bf94-97f10e0c61c8 | -5.72337 | -51.07003 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 564a2cb4-a39a-3b8a-af0f-f9d3e9da6fd1 | -5.72283 | -51.07355 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d273cb73-7534-3769-934e-978849d0bae7 | -5.72058 | -51.06591 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e02bf59f-8091-32da-9776-3f6834b60b6c | -5.5282 | -50.53777 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70a6b2b6-f03e-3eb7-b9df-07ab34331a2b | -5.49769 | -50.75661 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97bf30bf-1b3e-3826-ac72-5d3b01097944 | -5.43885 | -50.62129 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba188799-12ed-39b4-b4fa-0289cc2ca9a8 | -5.17593 | -49.68301 | 2024-09-29 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d823b730-7b1e-36ed-920a-078a7d202a49 | -4.97699 | -50.86836 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 194837af-8a4b-3f04-af99-e8416614a2e6 | -6.32156 | -49.99704 | 2024-09-29 04:49:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4eb20214-69ee-3c2a-9cef-696c5402e4c5 | -6.32099 | -50.0008 | 2024-09-29 04:49:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94aeb969-9951-336a-b02f-4a65c46268fd | -6.32042 | -50.00455 | 2024-09-29 04:49:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e54ef44b-6024-36df-8ff1-3e873b0ac0e0 | -5.98459 | -49.66735 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a7b8e41-660c-3ef2-bd9b-2b4d1457e7da | -5.98401 | -49.67118 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README47.md)
