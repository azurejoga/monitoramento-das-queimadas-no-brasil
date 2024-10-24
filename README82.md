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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46d2d4e0-2019-3e07-8c87-e949ce9c3fc8 | -19.65309 | -56.84384 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c7a8d05a-1eea-3fb8-a6a6-8d32c038cb1a | -19.65279 | -56.7796 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 63b28c46-b8ac-3d8e-8d07-52565264027e | -19.65251 | -56.84752 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d88ac426-133b-32c8-8143-a6358db3407e | -19.65222 | -56.78328 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 26883d73-4096-3005-886d-88878915eecb | -19.65213 | -56.80592 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0fe5c94c-470f-391c-93e8-f1fda1683975 | -19.65165 | -56.78695 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5b1b6428-65c4-35aa-8ba7-a0aff73086cc | -19.65137 | -56.85487 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| cdbb57dc-446d-3de3-a3e3-a33fe2a406c6 | -19.65108 | -56.79063 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 91016ba6-b88b-3d85-bd47-6a8aa3b7886d | -19.6509 | -56.83591 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e8de5321-7736-3dbe-b6b2-f9141c32b7c7 | -19.65051 | -56.79432 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e4f9ffd5-a2e2-3db6-b47a-2eded1406f81 | -19.65032 | -56.83959 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3198e644-f0c0-3928-8783-02d221d2102e | -19.65003 | -56.77534 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 468570e9-6644-3099-bbe8-e7f4ddc225ca | -19.64994 | -56.79799 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c92acbdc-ec09-35db-a3d3-84908d1a9bec | -19.64975 | -56.84327 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e5629291-3a50-3b6d-92a2-34db110fc5a1 | -19.64946 | -56.77903 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 091dc172-854c-30b1-8284-6fa422fc05d2 | -19.64937 | -56.80167 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 99e42a56-ef27-355b-9399-a6d4ccadee34 | -19.64918 | -56.84694 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6461c319-c244-35a2-a776-1a945e50fe7e | -19.64889 | -56.7827 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d0664b01-ca43-336d-9f00-6828cb734cfe | -19.6488 | -56.80534 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8d6e095b-474b-3bae-aab2-3172cb4a3c82 | -19.64861 | -56.85062 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 157b4c4a-371e-37e6-9af5-dd38e7240a1c | -19.64832 | -56.78638 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b743f4a5-14b3-35d8-a15d-4c10f22ee5a1 | -19.64804 | -56.85429 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e484b0d7-3969-3b6e-9522-d59e0b31b6d7 | -19.64775 | -56.79006 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ca31f6d2-8ca7-3da5-a875-e4f8ac288eb4 | -19.64766 | -56.8127 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e03860f9-aca6-3c5e-bb5b-19a50b476d34 | -19.64757 | -56.83533 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 77963f0a-4f3f-35d0-8447-73882af1d356 | -19.64718 | -56.79374 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 76087ce8-6eeb-3be3-8fc1-ce9c8d2039f4 | -19.64699 | -56.83901 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 56b5ee98-90c7-3912-b0e8-a051fba30d41 | -19.6467 | -56.77477 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 870254c4-8ef6-30b2-9f19-610865e0c588 | -19.64642 | -56.84269 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 08246806-612e-3c92-ae51-153d24501f3c | -19.64613 | -56.77839 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 43f547f3-2437-3b59-8559-7b9d67278468 | -19.64604 | -56.80109 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c5bfbb04-f5ee-3fd6-b9d5-3240d31dec98 | -19.64585 | -56.84637 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 5bbd11fa-38aa-3b72-b77a-c5e19ba2e3d7 | -19.64556 | -56.78207 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e3104849-99f3-3983-a980-bd0885c322ca | -19.64547 | -56.80477 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28a54edc-ec9a-3f7d-a968-1288e4a86163 | -19.64528 | -56.85004 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 6f783d73-93b1-38d8-81de-4675599f0f12 | -19.64499 | -56.7858 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 78e32465-6c60-3dc5-8c18-52148dac97f5 | -19.6449 | -56.80844 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6a762b96-be7c-30c5-9d10-9622472a3e73 | -19.64471 | -56.85371 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 616ebfbe-808a-3149-84b1-b0a72808d248 | -19.64433 | -56.81212 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a6c594e5-aa8f-3458-a85f-1270d2cb9f23 | -19.64423 | -56.83476 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 45db12d9-73d0-324b-a779-b5ecd12330d6 | -19.64385 | -56.79316 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b403c2ee-3840-307c-9a2c-12d2b3da2025 | -19.64376 | -56.8158 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c4e6574b-b467-3331-9ca1-e6994a7548d7 | -19.56919 | -56.68628 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 3fdca190-39d3-3354-97a1-5fb30a2646e6 | -19.56862 | -56.68996 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 35b27635-c1cf-3222-8cf2-f6196aa093f1 | -19.56529 | -56.68938 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 742080af-4254-3fb2-ae49-ef3ffb0c4f15 | -19.5587 | -56.66557 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a4eb1412-d745-3fcc-b574-6d0f32c711af | -19.55366 | -56.67604 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b01a508d-f057-3ef4-8511-0f0a3510bf7e | -19.55203 | -56.66442 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c64135d2-e602-3f27-b352-86338b57ef6b | -19.55032 | -56.67547 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4375ee80-1ee2-3734-ad02-283693f49a3b | -19.54805 | -56.69019 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f4558b8d-ad3c-3f34-981c-366061809681 | -19.54593 | -56.6596 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 936b77b2-301b-3153-9125-24793ec0b420 | -19.54528 | -56.68594 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 03568d5d-926a-38a9-a5e1-cae329808581 | -19.54479 | -56.66696 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1b44b4c5-eeea-385b-839b-0ae60248c6cc | -19.54309 | -56.67801 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 4aa668f8-4e25-3042-9b86-0d5ffa171875 | -19.54146 | -56.66639 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b6944859-af92-3085-ab59-44c5554db1eb | -19.54081 | -56.69273 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8a8a82ec-4a02-3f65-9758-8bc7b58030a4 | -19.53861 | -56.68479 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2420606f-f55e-3ba4-9382-67827886ed38 | -19.53755 | -56.66949 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 558a9df4-0096-31b5-840f-bc5474e2d3cb | -19.53479 | -56.66524 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 09b95ab0-b4c2-32b0-a499-3ac9422757fd | -19.53471 | -56.6879 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| cd50d292-120c-3909-94cf-78e3a5775fe0 | -19.53301 | -56.69894 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d3ba963b-7f95-3c6a-b900-23a3c15f961f | -19.51628 | -56.66273 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b1565dee-271c-3d02-ac0f-0fba56b50038 | -19.50627 | -56.66101 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9f5bfb3e-465c-34bb-84a3-7171572a762f | -19.5018 | -56.6678 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 21d6616b-f40d-3683-939b-8361ae745210 | -19.49961 | -56.65987 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 4f7e0e96-ac21-3a76-a474-b4741ae52eaf | -19.56935 | -56.64093 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 02c45b28-e554-363c-a19d-866cbfc89407 | -19.56602 | -56.64036 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 722fab94-0d71-3bb0-a1f9-6adc9f8627d1 | -19.55991 | -56.63552 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 507c25da-b0e8-3536-be6e-7b12d69a4c14 | -19.55707 | -56.65395 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dfc761f2-9847-3cce-9ff5-cdcd83cb8109 | -19.55267 | -56.63806 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e680e5e7-7e9d-3218-9957-ec462da9b873 | -19.50188 | -56.64514 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 460fcc01-c0f2-32f9-a989-17ae2eb39da5 | -19.49741 | -56.65193 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 686a0ba5-0fcb-3d88-b3f7-42c4b0ff1152 | -19.68191 | -56.72416 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6e3aebc2-15b4-301e-aa23-440a2d2907c2 | -19.67801 | -56.72726 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5cf69402-1b71-3197-8c2b-52e429afad79 | -19.67134 | -56.72611 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eeab7caa-e1e7-360e-af5e-f931ffe21b80 | -19.67077 | -56.7298 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f3850097-d9d8-3264-b421-b77ff507028c | -19.66801 | -56.72554 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0aa7adb5-bd99-36f5-b7c9-88204cc6c5f9 | -19.66744 | -56.72922 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f0b1ed81-58b0-335c-809e-9f10b57f11fe | -19.66687 | -56.7329 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4308f70a-6853-3d17-b179-264ba5d34832 | -19.6663 | -56.73658 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4d7f0c29-c047-3aca-8d46-3fcb42383e41 | -19.66354 | -56.73233 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 44cc2b96-37f0-3546-828a-a5e48dc9f0d2 | -19.66297 | -56.73601 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e7d2c769-ac7e-33d7-951b-655550a6902f | -19.66077 | -56.72807 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6d40608c-1425-3ab9-bf70-c79dbee46a57 | -19.6602 | -56.73175 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a3455fdf-4e81-3927-923a-588e4f6e92d9 | -19.65963 | -56.73543 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 04339bd2-566c-3cb3-86ff-b7b91d84edc5 | -19.65687 | -56.73118 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| e4d5f2d3-3db9-352c-b3ab-e13fc2a0c3c7 | -19.6563 | -56.73486 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| b6788108-a4d8-34d6-a404-4fd16d376c8a | -19.65573 | -56.73854 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 7d1cca26-2353-37e6-afcf-e7e09ba8b353 | -19.65353 | -56.7306 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 59689b4e-90fb-309c-ad0b-08d4ad8a5d6d | -19.65297 | -56.73428 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 65835572-c00c-35cb-8e60-367235253e52 | -19.6524 | -56.73796 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 110238a9-2ee1-3d4a-9ac1-fd43ae21f7d5 | -19.64963 | -56.73371 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 129c8a46-a6c6-3e83-ba21-1df1aec234ff | -19.64906 | -56.73739 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 2b9cbafb-5fc7-3c1e-a476-d21d1dd0ae16 | -19.64573 | -56.73681 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 81c12e7e-11b0-3d0f-bdc9-111eef0e6990 | -19.6424 | -56.73624 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 0867dc06-1d5d-3c42-a3d2-9ff08524b459 | -19.6285 | -56.73756 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8b4b1fc0-18a0-32e2-bdde-c5734743f933 | -19.62516 | -56.73698 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2aab6e1a-7bc6-3a59-942d-1b1cd9e105ff | -19.57586 | -56.68742 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 7209aadb-86d4-3471-b9e4-f4f8736805d1 | -19.5731 | -56.68317 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| a15a6c99-5036-3252-bd91-272e2e991808 | -19.57269 | -56.64151 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |


[Clique aqui para ver as próximas entradas](README83.md)
