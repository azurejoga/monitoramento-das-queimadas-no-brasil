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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc72a7e2-31e7-3d76-abe8-ec8e5ec26f69 | -3.01111 | -59.10744 | 2024-10-09 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2460f0b5-4aca-36d9-92b0-f6f9041a2c41 | -3.01037 | -59.11215 | 2024-10-09 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1af91a89-db32-3a6b-8776-33f17f7861e6 | -2.68756 | -59.57743 | 2024-10-09 05:01:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac29f47-0981-3031-a196-79e8f43f4deb | -2.68676 | -59.58244 | 2024-10-09 05:01:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2704061c-5069-378e-aad3-19b0ef838b42 | -4.52766 | -59.90103 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5330a2b9-d205-3dfe-950f-cbd16922ebac | -4.52749 | -59.90266 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56e3bb82-d281-3389-b99a-ee4ff6121e84 | -4.38058 | -59.94152 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b214979-4de1-3d87-b29d-df3ad954433e | -4.37664 | -59.94087 | 2024-10-09 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d58af8c-928e-39b1-8546-fa405fdc12ba | -4.29612 | -60.01863 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 930588f2-2736-34fe-baca-606ee466ea25 | -4.29531 | -60.02372 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0cc026b-54d2-3dd4-8ca4-96c3d6aaeee8 | -4.29467 | -60.02077 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b1667a55-2fa8-3f31-845f-dc9f6e3f1801 | -4.29297 | -60.01291 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97a2617a-e478-36ba-91cb-df87e7d63c05 | -4.29216 | -60.01798 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8100a055-0a84-3bdd-bfa2-d5fa0b967caf | -4.29071 | -60.02012 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c56d9068-18b4-386c-87f3-9a5e67e1a75f | -4.28901 | -60.01226 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94257ba6-e477-3c01-a959-b9c6e021b124 | -4.2882 | -60.01734 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0dd0af4c-fc60-3745-bcaa-a7c1033f2dc8 | -4.2876 | -60.01442 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5a6c0b9-b0e2-39ac-ac1d-59a7ffaba0a1 | -4.28506 | -60.0116 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe6c28d8-4f00-35ad-ae99-d11125b25e0d | -4.28424 | -60.01669 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c21463b-d04c-304e-8024-fec8b82a4aae | -4.28364 | -60.01377 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bddd8619-a801-3958-a357-2bac3d66c4dd | -4.27401 | -60.00457 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1532a641-dfe9-3640-8c4f-df61126a625f | -4.11334 | -59.87799 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc2c7ea6-a447-35f4-b455-c030fc2f3b55 | -4.10941 | -59.87737 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51197e4d-e064-3eac-b4be-1bb755722286 | -4.10858 | -59.88237 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1ee33c7-02a6-39a8-9854-cc3a18487e63 | -4.10545 | -59.8795 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c374c4-21d3-38d6-8c6c-92a560c07634 | -4.10465 | -59.88453 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30c12565-a2e9-3cfa-b0b9-763650969411 | -4.10465 | -59.88174 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04caf748-ab02-3f00-a521-017fcc04d813 | -4.10381 | -59.88677 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66456fb5-154d-38c9-b63f-b2d9bda6575a | -4.10071 | -59.8839 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c04d4d0d-22a1-31ae-9c2d-4d531c2f9529 | -5.09425 | -60.22276 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b12195d-c578-3f1c-a6b4-9d6f24b8ffef | -5.09342 | -60.22786 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e0785cf-3140-3bd8-bd6c-d974851099e0 | -5.09259 | -60.23298 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0c7c0b9-b6a4-3c7f-868c-0ccb4f6fdd9d | -5.09029 | -60.22209 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8644bf98-b547-312c-b1cf-f6bcb344baef | -5.08633 | -60.22144 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05712823-5e8c-3369-9bb3-1ca4fcbca76b | -5.0855 | -60.22654 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a85a3a6-f7df-32d2-88ae-6bb7a0b8dcd9 | -5.08237 | -60.22078 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce44fa4e-cfd4-3089-81e9-9419849e8dd0 | -5.08153 | -60.22589 | 2024-10-09 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35c19a1c-25e1-3e93-842a-bedf9474f659 | -7.37617 | -59.78183 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f11218a-2d67-3376-a6a7-986dd887a4a3 | -7.36975 | -59.65683 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a98de1a8-2e6e-3a45-be6d-162d212dff28 | -7.2993 | -59.73642 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b240cfe-bfe5-37ff-a889-d55100978171 | -7.29855 | -59.74095 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f01eba5-40fd-3b14-a802-f1bb6bf88590 | -7.29557 | -59.73584 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d5a9432-d9e9-3091-8e0d-cdace65594bf | -7.29482 | -59.74035 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f5a3013-e4cf-3da3-b8c3-c5b58d446f8f | -7.27914 | -59.74238 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c8054e0-33b9-309a-99e7-b7d3778fe2c4 | -7.25027 | -59.6304 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7b951b6-9880-30c1-897b-c75e77a5e30a | -7.24657 | -59.62975 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d96cb936-23c4-3c7c-9a25-826d50d81354 | -7.24582 | -59.6343 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbb7f908-4746-33a6-85ee-b813d3a4b5ff | -7.24286 | -59.62915 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19f462b6-85ee-398d-8c96-ce4f4c458d55 | -7.24211 | -59.63369 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 877c1b88-7167-39dc-80c7-bcb2f5f67d00 | -7.19164 | -59.77681 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3fc92379-1bf7-354c-b522-11f984ae1038 | -7.19088 | -59.78135 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 334936f9-4b9c-3865-b3ab-36df38f98fe0 | -7.18789 | -59.77621 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c274c8d2-60bf-3df9-9bbb-e77191e58b60 | -7.18714 | -59.78074 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 11a5c51b-3ef4-30f6-98f7-868eb67d3258 | -7.17853 | -59.38155 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c62b6ac-6299-3b53-853e-de9ba837866a | -7.17344 | -59.3896 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8291a4b0-6f9c-346f-8fa5-f945616ada37 | -7.16451 | -59.35244 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65019a3a-461b-31ab-8af0-c6562b2f9d33 | -7.1638 | -59.35675 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0e04ac83-7ae8-36fc-966f-b8676eaa3371 | -7.16014 | -59.35616 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 740eb56b-6a45-3710-9bb6-ca0a68c99405 | -7.15943 | -59.3605 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 166349ce-6130-3490-88cf-329b004d4982 | -7.15585 | -59.38218 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57dcb395-9a31-3003-b51e-1f3c58ef4c32 | -7.14675 | -59.30106 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0c12e3d-62a6-3764-b4be-5a4ee83292fd | -7.1431 | -59.30045 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 361071c2-4aa4-3799-8584-5a9664c758f8 | -7.14239 | -59.30473 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee5b01f7-4bd5-3144-8d6a-01741f860fed | -7.13216 | -59.29865 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 271fcf31-13d3-3c91-9730-c7c59cdaade9 | -7.13145 | -59.30293 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61a4bae3-3741-3560-a694-1c03753db0d2 | -7.12851 | -59.29806 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f7603cc-08c2-3b6a-8a76-adfa1997c6d5 | -7.12829 | -59.29975 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c33c6a99-6736-35cd-b9c2-28b5d9bd91b5 | -7.1278 | -59.30233 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe6bb1d4-c274-3787-b935-c27c3340382e | -7.10727 | -59.31387 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5186a531-2bd4-3603-8103-38ff4db08ab8 | -7.06937 | -59.45428 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b35ad1-0683-3234-9e7c-89259fa825d8 | -7.06865 | -59.45868 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d0fd3c1-169c-3400-81d5-f551bfd118dc | -7.06569 | -59.45367 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05123b4a-0ebd-3a83-aa97-dc65e5511426 | -7.03975 | -59.40464 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3926842d-b57d-38aa-9234-69c5626e97dd | -7.03608 | -59.40404 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c90900e4-18a4-309f-ba97-330217020f4e | -7.03392 | -59.41709 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| becd239a-2657-384b-aa36-d9ee6ac19caa | -7.03025 | -59.41648 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dcb4c3b-8f6d-3388-97b7-eed7e68720f1 | -7.02978 | -59.81459 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 499d768a-ac09-352d-9b54-3f47af721402 | -7.02952 | -59.42084 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05cce8e7-afaf-3ae7-92f9-c961c6958086 | -7.02657 | -59.41588 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e761999-930f-34b0-b36f-3dd466b2df46 | -7.02585 | -59.42023 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c01a475c-74d1-3beb-98a8-be4c66525779 | -7.02513 | -59.42458 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0768ee8-ff9e-3a8a-988d-bd355565b188 | -7.02362 | -59.41093 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5df44cb1-4061-3e4e-aef3-f8bc061c16aa | -7.02289 | -59.41528 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99152d79-f9a5-3270-b8b6-c470a05bf663 | -7.02217 | -59.41962 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 070e47e2-a5e5-33e3-9975-3e74e4ba66f0 | -7.02145 | -59.42396 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 025a3245-751c-36cb-b903-ad55d6e4457a | -7.01994 | -59.41034 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdd5e68c-5f5f-3a75-bdab-7770fc011195 | -7.01922 | -59.41468 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b2e1b12-e23b-3078-ad8e-f7b60ee4b12d | -7.01626 | -59.40973 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d84da51-9814-38ce-b2ea-1f3cbafa7eb3 | -7.01554 | -59.41407 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e284442f-0bfd-3c37-a6ab-f8b80181a4db | -7.01259 | -59.40912 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b14fdb2-b333-3e92-8a2e-3ec1d970741b | -6.91689 | -59.79295 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf57d96-2e78-381a-9984-1d32450f0308 | -6.91314 | -59.79226 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 553a8e74-8a3a-3ef0-acd2-6eb1f262b51c | -6.91156 | -59.7547 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63fbf96b-6f51-3d0d-b362-059cb367237c | -6.88533 | -59.75015 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb61cdbd-793f-3d2b-82e1-e1eb6e8e7023 | -6.80828 | -59.14688 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b980016-c7c3-3abb-8137-3aa93a595eaa | -6.80404 | -59.35548 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c82870d8-03b6-3bae-9851-f21d834962e1 | -6.80037 | -59.35486 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e55b0e9-3e1c-3a29-b895-bb06685e9456 | -6.79743 | -59.34988 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a815e4c8-85b0-3643-9099-86380387174d | -6.7967 | -59.35424 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa73a1e2-cdf4-3d51-9c15-4ab88ec81231 | -6.79475 | -59.34707 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README169.md)
