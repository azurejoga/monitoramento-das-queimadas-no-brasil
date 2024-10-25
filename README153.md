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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a9677e4-22a3-3f36-bdd5-461281229bd2 | -3.28162 | -50.07277 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d1a01a2-93e6-3523-a127-b689f318f277 | -3.27828 | -50.07328 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6a20170-3df4-30a4-812a-9b8edbb1469b | -3.27493 | -50.07379 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 682a5bf8-be60-31eb-bca7-dc3a4ee18ccc | -3.25632 | -50.15234 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 96a53c14-aae9-3498-9671-29880dd80bd3 | -3.23723 | -50.00725 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bb60b62f-f80a-33c1-9b59-21efd6cae1e9 | -3.23388 | -50.00776 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8360b043-24e7-322d-b996-48125b258c47 | -3.23333 | -50.00422 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d42bbcba-864f-32e3-af9a-4c7f46ecff3d | -3.22998 | -50.00473 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61e26c9a-98d0-3a4f-bce6-66889cdf8d55 | -3.22223 | -50.17202 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 032b2ace-e500-3016-b8a4-51d941cd7130 | -3.22169 | -50.16851 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| abe5e9d9-0da7-36be-8730-fe0e664c0aa6 | -3.2189 | -50.17254 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7d488110-928e-3959-b144-7bcbe49a9c16 | -3.21836 | -50.16902 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5bc9da6d-82ef-3265-9800-df089cbaaa26 | -3.21556 | -50.17305 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6e94361-cc03-31af-90cd-b32fc0b5762a | -3.21502 | -50.16954 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e1b38fa-83bc-32b8-b56f-e9211a5973e5 | -3.21222 | -50.17356 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d417885e-5dff-3fc4-893c-e7a76c22a693 | -3.18319 | -50.20672 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 92248561-f989-3501-88d1-c95cba814e86 | -3.15387 | -49.77188 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c673c28b-403e-3cf5-9bef-6bef7f6b9fa3 | -3.1505 | -49.77241 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 566edaa6-d2d8-3691-9902-8fd9b477a26d | -3.54839 | -50.30331 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 53748e67-df04-3a8d-8000-7bd559ab9b14 | -3.54785 | -50.29982 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6accb2e5-2c65-312f-a169-5f313174b1f2 | -3.48442 | -50.48478 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4b01dae2-7f61-3ccd-8be2-58c59113e5cf | -3.48388 | -50.4813 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c0a5658-7e21-326c-8276-b97f73ddec0e | -3.4811 | -50.48529 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 76be52a4-beec-3df4-8c00-773d9b0088f8 | -3.48057 | -50.48181 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3b904b6-6092-33f6-9c47-e2965122a863 | -3.41449 | -50.62725 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86d2ee58-e541-38d0-ad2e-2427444358d9 | -3.20337 | -50.29333 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d923468-f7bc-3367-996b-f9faf2df8e53 | -3.15129 | -50.46263 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f3504910-8cba-3492-ba0f-69ba70844bcc | -3.15075 | -50.45915 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c0fc483e-256e-3b38-85c7-6a65217d49f2 | -3.15022 | -50.45567 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| be20c7ae-02b6-3e43-abb1-1b853cdb6c6f | -3.1469 | -50.45618 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2d9a79a1-79b9-3329-8688-036bd83c4533 | -3.14637 | -50.4527 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1fc39307-b22c-3aee-b30b-5a20c8a1dfe1 | -3.07311 | -50.50739 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62d3f832-2f62-3e32-809a-8c691918fbab | -3.07204 | -50.50043 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 21656213-7e0f-3ba8-9fe4-b7b61a8adff4 | -3.07151 | -50.49696 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 54006ea5-821c-3e61-9e51-cd1a2b1ed269 | -3.06766 | -50.49399 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7f8b66db-2071-3f21-b5c2-ca12ca599543 | -3.05005 | -50.37903 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e0150de-6aca-3e0d-a3e6-2329287b759b | -2.23564 | -50.36702 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b477d637-9cae-31e0-9f79-91c5e8e37b53 | -2.23531 | -50.02975 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| e8acdb17-ab58-36b4-af47-15e6a3c05302 | -2.23474 | -50.31674 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2060ff6f-d5ac-38a5-989d-b1d2f8b6b0b0 | -2.23419 | -50.31322 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 80557bb2-9da2-3519-b842-a64ff6775f7d | -2.21811 | -50.29765 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4d525dd-4a98-3df0-8adc-5f6c7fafcbf9 | -2.21748 | -50.31578 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 525ad053-2638-3c86-8759-f8521886f0ba | -2.21414 | -50.31629 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a5df1c1-2eda-3671-b600-f44bd09f8b53 | -2.21033 | -50.29161 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 48cd7059-3bac-3687-bdc6-5bcda71c5f04 | -2.17489 | -49.68005 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 6b76efb5-34ac-32e0-8414-582a3915abad | -2.16828 | -50.25839 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dac13b2d-b88e-3bfc-94a7-6b89b208ca55 | -2.1588 | -49.84639 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8c249137-4c8e-34f1-935f-4085fecf52f5 | -2.15073 | -49.97304 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85121166-e3bc-3c1b-b3d9-87389e8473dc | -2.504 | -49.74467 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| cecfb9eb-a831-3b75-bdf7-611d84899393 | -2.50078 | -49.92597 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f7ad690b-d50d-3981-a96a-4f85a2c705d9 | -2.45117 | -50.376 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 20d37493-69db-35e3-a69b-092e2779ef9b | -2.45082 | -49.91528 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7ebba559-aa5f-3474-9469-0d50eba23b27 | -2.45027 | -49.91169 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a38f2181-38bb-311b-9492-c597c0455e21 | -2.44784 | -50.37651 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 31aa11d2-45b8-3c87-a706-6d3d43a33f43 | -2.44745 | -49.9158 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a6124a62-ec4a-36d7-a870-8da96c6bad7c | -2.4244 | -49.72346 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 7a0ce2e5-ce41-30cf-844f-da32d6cc1c44 | -2.42093 | -50.29073 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 56a49299-da1a-3eb6-8759-d814c5096c34 | -2.41534 | -50.29879 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e99f13d1-d34c-3f0c-bd43-ab29d756213f | -2.41496 | -50.40665 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85fe57c6-1c4a-3746-8eb4-2b8e6beab8ae | -2.4118 | -50.18736 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 73b4d9b7-7dbb-372a-90a2-1cbfe0830b9a | -2.40694 | -49.70726 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e5b7ebc4-03de-3192-98e8-3df7c2a1a17f | -2.40086 | -50.42386 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 257c9d79-4825-3649-8a45-c8a4f28c568d | -2.3795 | -49.88927 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d638c7d-b450-32fe-8838-252e64ab3e4c | -2.35029 | -49.85689 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d55200cb-482c-3476-9f87-d47000d9aa08 | -2.34524 | -49.8244 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a129b388-0775-34ec-bbfc-abb34c407fc2 | -2.34186 | -49.82492 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c8f5d2dd-289f-34a3-833d-443885fc093a | -2.27509 | -49.82828 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ee1eb5bb-8294-3bbf-b4e2-e66644572c83 | -2.27171 | -49.8288 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44f42d22-59e5-3cc2-bd1f-9eb45dadef49 | -3.64728 | -49.30854 | 2024-10-25 16:52:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9dd4a385-5528-3a6c-8232-e9c3c6e2826c | -3.58565 | -49.56052 | 2024-10-25 16:52:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| d9be1325-d3d1-3f6b-910b-b8526b8c63f0 | -3.58421 | -49.5612 | 2024-10-25 16:52:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 533b7026-7d55-3c44-999d-262e34ba6e13 | -3.50868 | -49.60971 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 925716b0-d47c-3769-8390-65fa1b610e9a | -3.43141 | -49.13755 | 2024-10-25 16:52:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f62cb39-6613-3a69-8cc2-a400ed86d802 | -3.24253 | -49.59586 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 541e24a0-0218-3d20-b536-d31156175925 | -3.21758 | -49.11683 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85ef82d4-d8ad-3957-8226-e4d014a89cf1 | -3.17144 | -49.60682 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12300c02-c801-3797-8339-9f8ddef3aa69 | -3.13219 | -49.17611 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4545d569-fdec-3781-b0f5-e66de446f3e6 | -3.11544 | -49.52234 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cb2b069-c7b7-3643-af93-92d341a8354e | -2.4804 | -49.09064 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16c50637-aeba-3fb9-8826-a57650ad7e66 | -2.47524 | -49.10314 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d5c61ae-44c2-3e79-8a89-97ebac7e23a1 | -2.47178 | -49.10368 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 7c330600-e039-3102-9b3d-c58b7b57c51b | -2.46832 | -49.10421 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8efc41a1-e430-3d18-82d0-2e0006aa1aaa | -2.46485 | -49.10474 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f8ca8941-a042-3414-a7fd-a255aed9919a | -2.45871 | -49.01965 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a84ace89-8427-35f1-8788-1130edd93644 | -2.42125 | -48.96244 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90c940ae-47e0-3b43-9ed3-8a6e83379503 | -2.41564 | -48.90392 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 48919b5a-ba01-334e-8e24-8904231656f8 | -2.39693 | -49.20848 | 2024-10-25 16:52:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| b3f719a3-7a90-3b0c-adcd-8b0a45c36b58 | -2.39278 | -49.15872 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 386ec9c6-af16-3cc6-ae5e-a12319fc5206 | -2.37596 | -48.9575 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4da2945-ff7b-3e7b-8b0a-f0a066afb210 | -2.36329 | -48.99104 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| de8ea36d-e2d2-3aa0-8654-375a733e8e30 | -2.35981 | -48.99159 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 3556c591-1490-3734-992d-1d0270427f57 | -2.34218 | -49.19757 | 2024-10-25 16:52:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8257267f-fc55-3c7d-bae8-3ad7c1c11ff5 | -2.32974 | -48.91309 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5b866a8c-185e-330f-baa6-f9c05006d7f8 | -2.25066 | -49.14888 | 2024-10-25 16:52:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8b8c3dc-85a8-37dd-a8ba-7124a84f97f5 | -2.25007 | -49.14507 | 2024-10-25 16:52:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e7cd549a-56fa-3f24-8d53-9b7331a4bf2a | -2.2466 | -49.14561 | 2024-10-25 16:52:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f4084ddb-ec42-3290-b103-9af31f450f61 | -2.51227 | -49.4545 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f521d6c6-7af5-3f56-9dd7-b2e1d279ee7e | -2.45439 | -49.62559 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 751f0284-e919-3090-9b14-be5a14bdfbce | -2.45215 | -49.5659 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| dcebc432-2cde-3f39-8a7b-65eb131ee552 | -2.45099 | -49.62611 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README154.md)
