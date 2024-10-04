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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9d1e8ac-03a3-3b00-8a11-3d1ec2623e42 | -17.04941 | -56.79103 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c7f74fc6-5168-35c3-af38-030c8df26317 | -17.04858 | -56.79545 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3849ed23-4720-3543-aea2-43378d723b62 | -17.04804 | -56.79278 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 87415ca0-bdcf-3085-8d5a-bdcae44848e1 | -17.04502 | -56.79012 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 68c3f8a2-0b38-32f7-b128-38ad5bb7c360 | -17.0423 | -56.78036 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e5e0e66f-0402-3579-a2db-1d7e3d40ebb4 | -17.04157 | -56.71173 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b03447cb-c1b0-35fc-b2ae-bc70f9c56e78 | -17.04148 | -56.78478 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2728ec80-404a-37d8-b5b5-e87cc7ab6b92 | -17.04075 | -56.71611 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6b23e673-d8e5-3b21-af91-ae8b499e8221 | -17.04065 | -56.7892 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 332a35b3-4ea2-3755-b993-e24dd406bac7 | -17.03804 | -56.70646 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b907fee-95af-3f9e-9691-8569e7c4b03a | -17.03793 | -56.77944 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b8610e72-ab5b-3d48-a6fd-e60111ce7a8d | -17.03722 | -56.71082 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a2c34eed-7d14-3914-ae5a-3fc6ae438323 | -17.0371 | -56.78387 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a9710459-ddd8-3ecf-86d6-f8c45435a1e3 | -17.03639 | -56.7152 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 876bac71-fe46-3843-b49e-ad45931ca39d | -17.03627 | -56.78829 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bacf8b94-828c-3fd1-a995-739f9e48ebe5 | -17.03544 | -56.79271 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f5593d2d-9b9e-3db5-bb77-e8fea23452e6 | -17.03368 | -56.70554 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6d931e57-83a1-3f80-829b-5c0fc7222874 | -17.03355 | -56.77853 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 64ebec1b-490d-3bac-be0e-8898ef0bfd29 | -17.03286 | -56.70992 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 46d45d2f-024d-3f22-8325-cdca5df13f34 | -17.03272 | -56.78296 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f4d01dad-c8c6-36e5-bcf0-804ff43a2681 | -17.03189 | -56.78737 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0519a21a-d60c-3752-b296-045870f01d1c | -17.02834 | -56.78205 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 03db63ab-901e-35cd-92d7-57510d9e9190 | -16.8487 | -57.47558 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a28e74cf-c33d-3e25-a443-306904fb3e4a | -16.84602 | -57.46481 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| b28ffc1c-7762-33ce-9ced-58ecc9d814f8 | -16.84506 | -57.46969 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c542c0e4-f504-32b8-be2c-3e03f51ed708 | -16.84143 | -57.46384 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 997a8c33-c4ef-30d5-b69d-c1fc241fafcb | -16.83951 | -57.47363 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 08dcfa17-3fc6-3965-81a5-9e71e2599df8 | -16.83588 | -57.46777 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| aedbc45a-9781-3607-9a43-259286f03442 | -16.82395 | -57.46206 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 390faf7c-79f1-3c2f-82de-e8a350b39360 | -16.82302 | -57.46697 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f7a8c8d8-0c32-3b58-8421-54023f0f8440 | -16.8221 | -57.46487 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 78259661-6211-3b2f-bbac-476692b54bab | -16.81936 | -57.46108 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 609794d5-ba82-3937-b912-fc6ed4743c93 | -16.79264 | -57.47588 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 076113ee-4b09-3ca0-8bf4-173fbff1d42f | -16.78155 | -57.48379 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 7aa25adb-3779-3b11-9cd7-2087850067b7 | -16.78087 | -57.43757 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 43041126-4475-3d2a-be23-3ec61c9077ce | -16.77993 | -57.44248 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6c4a50c9-3f51-3105-9782-a01d6ccea63e | -16.7787 | -57.49863 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7b9599db-a280-3f72-98cb-2e1db06b5a9f | -16.77695 | -57.48281 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| db80124f-57be-306b-8f7f-9dc65153be73 | -16.77505 | -57.49269 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c1b09adc-22c6-3532-8e2a-64ccfba0b810 | -16.7744 | -57.44641 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5ceb0a60-7f64-3f2d-be56-1b770d8d463a | -16.77155 | -57.46116 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d24e08d0-facc-304b-8824-53580dcbe9d9 | -16.76696 | -57.46017 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2ccf8b4b-b26e-354c-b779-a3d09fabc345 | -16.75759 | -57.48384 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 021609fb-0653-36ef-8b6c-14de645bc26a | -16.75663 | -57.48877 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6cd3497f-f92d-3944-a4ea-f1501b8cd71d | -16.75585 | -57.46808 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2d389de9-f7cf-3333-a853-22db17d7bf5e | -16.75126 | -57.46711 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 361a5434-e406-34a1-b3c5-bc0dc4449338 | -16.7457 | -57.47105 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f86e2525-c857-3716-aea1-414e898beb0b | -16.7411 | -57.47007 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| fc11a1d2-15d1-3f7b-a0cd-0ae178dc28f5 | -16.73842 | -57.45927 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ea82c3be-d226-3a72-9271-6c81e94570dc | -16.7365 | -57.46911 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4974df33-d73e-3366-8a4d-99698c7d5ccf | -16.7319 | -57.46813 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ad14762c-74e0-3a52-a213-b7e4748a7f9d | -16.71253 | -57.46918 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b7c0e3bc-79cc-3fe0-afdc-74bb2966014f | -16.71113 | -57.46229 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cae617f0-094a-391a-be83-b8ea7e0d7328 | -16.71019 | -57.46722 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dbb3c69c-971a-3077-983f-cc41123c606b | -16.70005 | -57.47021 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 48f164ac-851a-37fa-b53c-fa9d90b4e55b | -16.69872 | -57.46628 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9ef49251-0884-3abd-a95f-6b52d5a79096 | -16.69775 | -57.4712 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 444b0b27-bb16-3985-8759-8e82d92fabfa | -16.69178 | -57.46332 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c9dee3f4-214e-3ae2-ab2e-70d0f608c731 | -16.69084 | -57.46826 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9c7fc064-b810-32f2-91f1-b8cd609e9c39 | -16.68718 | -57.46233 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8a1107f4-429c-3f84-b73e-41e174ba99f5 | -16.68624 | -57.46729 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a28d6938-9a89-3bd4-afbb-20a3a5f3b4d1 | -16.68447 | -57.45149 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8ad367e9-9441-3f15-a2f6-c219efb7234c | -16.67337 | -57.4594 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c3c76ccf-c45d-3628-b9ae-95534c360ac8 | -16.66877 | -57.45844 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fb810977-a6d3-36da-983d-bf63c883805f | -16.66687 | -57.46832 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a3622870-8e1f-3bb7-9079-530818d7f3d2 | -15.36345 | -58.15092 | 2024-10-04 04:34:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0f8386-5796-3b01-9d25-e9f4a77e1300 | -15.36239 | -58.15638 | 2024-10-04 04:34:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98e16be5-5f7c-3600-82bb-a0943b324a13 | -15.35845 | -58.15026 | 2024-10-04 04:34:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f8de22b-445a-3605-b0d4-09bc79542f4b | -15.35741 | -58.15562 | 2024-10-04 04:34:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6476cbef-8a5b-3555-87f7-b2af2dcbc465 | -15.35342 | -58.14971 | 2024-10-04 04:34:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70496724-5713-309e-8d48-e5c68f0c17f7 | -15.3524 | -58.15495 | 2024-10-04 04:34:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eca2dc96-f34a-30e7-b03a-fecb56a6219c | -8.87359 | -61.83724 | 2024-10-04 04:34:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 79c048cf-1ddc-34ec-8b57-9e64b31202d2 | -8.8723 | -61.83739 | 2024-10-04 04:34:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| af72127c-ec57-3527-99de-32edbef7bac3 | -3.2899 | -50.4725 | 2024-10-04 04:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 5b2fecdc-9ef4-370f-882c-827c0913dbfe | -3.2899 | -50.4516 | 2024-10-04 04:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 248.4 |
| 259b94ef-f8e8-30e0-9795-531c1f742564 | -3.3083 | -50.4719 | 2024-10-04 04:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 88cf2b6c-90ef-3a54-9257-c1eed0e4fd47 | -3.3084 | -50.451 | 2024-10-04 04:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 301.5 |
| d7e0bd04-2a3a-3ddd-b94c-3bfd7f2a3393 | -3.3085 | -50.43 | 2024-10-04 04:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 35d1e3d3-1dae-3aba-8b4a-f1827d45aa24 | -9.3118 | -50.7991 | 2024-10-04 04:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 98263c7c-10cc-3088-9f38-3558dd3c5421 | -9.3306 | -50.7974 | 2024-10-04 04:35:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| a4304855-cce0-3e74-b11d-5e9586f357f9 | -20.50584 | -42.37622 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d7710e35-0e72-36d7-9912-4dbe31aa9bb9 | -20.50455 | -42.3698 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| c63717f0-912c-3840-b68a-374984de838a | -20.50372 | -42.37807 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 402d815e-feea-3f21-96f8-d91354452a5f | -20.50167 | -42.36755 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4ba35c33-153b-309e-839f-d773b5741c98 | -20.50086 | -42.37491 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 85a57e2e-9db7-3d48-9589-e2d9338d4abc | -20.5 | -42.38278 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| abf1eec4-3db4-38c8-89b2-33c658db9a25 | -20.49952 | -42.36885 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 83269abc-e64b-3ac2-9151-6813baa33d9b | -20.49876 | -42.3764 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 978e9fff-203c-3e3d-ac9c-aa64d3d4f851 | -20.49796 | -42.38428 | 2024-10-04 04:36:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| dc443d82-859d-346b-8447-8c9ed49e6895 | -20.43932 | -42.51933 | 2024-10-04 04:36:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f4b7897-d5c8-345e-b314-67977b05e085 | -20.43432 | -42.51864 | 2024-10-04 04:36:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 188a69db-d1fc-3c1e-aca6-751adf598e4f | -19.89351 | -42.10983 | 2024-10-04 04:36:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 469d5882-bc5d-3565-85c4-c47fb987dc55 | -19.88927 | -42.10126 | 2024-10-04 04:36:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45ed4478-68e6-3f17-acca-6515c1037d3c | -19.88894 | -42.10428 | 2024-10-04 04:36:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| afefc866-1fbe-3014-93ce-2809a67ca264 | -19.88835 | -42.10968 | 2024-10-04 04:36:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 032700c6-d17c-3bff-9ce4-b5416bdf33ef | -19.87237 | -42.34668 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| eae0cb0d-807d-3bc9-b05f-656ea51253f0 | -19.87113 | -42.34668 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e29d7182-0a26-37e8-81e1-81b2518ac3fd | -19.86733 | -42.34614 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 456a6e8f-dc61-38b9-9219-f879766e4c8d | -19.85846 | -42.38006 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 853b09c5-0b21-3cf7-bddb-128232514ffd | -19.85788 | -42.38528 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README132.md)
