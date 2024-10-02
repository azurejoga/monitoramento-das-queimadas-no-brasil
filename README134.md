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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16d2113c-6220-3784-a354-eee6260e3492 | -8.47446 | -62.72054 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a97afb7-8067-304d-9889-13a42a02497c | -8.47387 | -62.72405 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 199b818d-5513-3073-92c8-c959515b72e1 | -8.47328 | -62.72756 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8648e81d-c70e-34a3-aec3-a8f4b4a570fe | -8.47104 | -62.71635 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13825ee5-ee5e-3a73-b87e-de64966436c9 | -8.47045 | -62.71984 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a18092f-75f1-387a-8698-172c22491b48 | -8.46985 | -62.72335 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bcd43ed-049e-33bd-a33c-e1a383aef87a | -8.46926 | -62.72687 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03ffd7e8-fe62-31cc-aa9c-4e6548b7763a | -8.46702 | -62.71566 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f6d195b-215e-3f17-8cc5-fdb4da77e712 | -8.46643 | -62.71915 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ecb10ed-4369-3cb7-ba9a-606b27014828 | -8.46584 | -62.72266 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c616aed-97f2-37e5-9b07-b152483b760c | -8.4655 | -62.65171 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d90c983d-82f9-37a5-bde3-dd8ce21d23e9 | -8.46301 | -62.715 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd5321cd-026f-3ce3-9d0b-099752ee9112 | -8.46242 | -62.71847 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6af15f23-14f0-3bc4-a95e-2577851886eb | -8.46182 | -62.72198 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 46b24369-42e3-36a6-b7ad-be769025f7c8 | -8.46151 | -62.65102 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0d998b3-7a91-39d0-8a89-50be4d176623 | -8.459 | -62.7143 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a9f31e-2f7c-3b69-985b-b4bb4ec54707 | -8.4584 | -62.7178 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 987775ad-29f9-336d-8217-b06c92aeb628 | -8.45781 | -62.72129 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 94bbaea0-7f22-30ca-90df-e4d8bc426fa8 | -9.27139 | -63.33362 | 2024-10-02 05:10:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8eecf5d-9151-3d44-9e07-02ce88426ef9 | -9.26909 | -63.33381 | 2024-10-02 05:10:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b347ea66-8ab5-39d7-b1cb-6fefad507cda | -9.25333 | -63.63243 | 2024-10-02 05:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1115d923-c007-31ab-8854-2141cf2440d3 | -8.9751 | -63.93588 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edd80745-2f97-3867-a4ae-387b9143b0a2 | -8.91818 | -63.97295 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0d44d2a-6cbe-305e-8ca4-204df5b295eb | -9.77876 | -63.14788 | 2024-10-02 05:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a47d589-7d98-392c-baf5-004d9893baa2 | -9.51251 | -63.19743 | 2024-10-02 05:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fe03db2-76f1-3320-acba-8a764d9729d3 | -9.50845 | -63.19665 | 2024-10-02 05:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e191aaf3-6697-3104-a767-9c003a5458fd | -9.82916 | -64.04929 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bacb9ed-c54c-3955-bf22-8e48232ddd46 | -9.82489 | -64.0485 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4cca555-93b1-3a64-9cea-a65a834bd216 | -9.77584 | -63.93599 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 887199a5-a8d5-307e-8c9f-3a5ebd5691d5 | -9.77514 | -63.93999 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00fde421-ea4f-3d07-8002-b7c81ee18115 | -9.77088 | -63.93927 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91136a19-66ee-3ea0-8ac4-dff0d30a7c2e | -9.73261 | -63.98217 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d77b257-7d05-3b57-92d6-4e066d154f6f | -9.65244 | -63.42277 | 2024-10-02 05:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1a1143d-634a-3e9e-a914-c8e454317648 | -9.64358 | -63.42496 | 2024-10-02 05:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8401b6cf-d522-398f-8cb9-a7db5a3c9325 | -9.56723 | -64.25647 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df9a398d-e2c0-3ac7-a096-f41fbafb6047 | -9.56649 | -64.26067 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 021a0e44-f62d-39b8-ad91-f4813c04d454 | -9.56288 | -64.2557 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26b7aa60-26ac-31fa-a593-ac9325e9fc44 | -9.56213 | -64.2599 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0c78c37-dcfc-3fa6-a755-1ea99fa4d451 | -9.56138 | -64.2641 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34609c28-1a27-38b2-885d-04878a3be37b | -9.55777 | -64.25911 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c7d0e1b-59cd-30fc-806b-35058f3efe68 | -9.55702 | -64.26331 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e1a0dd9-2288-38fc-9f6c-d3accbd69aa6 | -9.55341 | -64.25833 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b59996d-c5dd-3ea7-b0e8-2aa0984d00e7 | -7.29499 | -64.65619 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc46bd2-e690-39ea-aafb-0577f2aed2e4 | -7.29416 | -64.66106 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1232d19-4936-3aae-b574-da1d8e36d643 | -7.29034 | -64.65536 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d8b5fd8-35ac-3435-bd0a-d6b0122b567a | -7.2895 | -64.66026 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 024ff64b-05c7-3d5a-8569-647016a58a3e | -9.30294 | -65.34515 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87c0dee3-ea3d-3ab8-870c-add6584c5a0c | -9.29907 | -65.33955 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31976d84-c6bd-38e4-876d-7218fe16d39f | -9.29814 | -65.34476 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e07ecf0-b82e-3458-8e24-1e96b48648de | -9.29722 | -65.34996 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebec3d3c-ca51-372e-8287-8deeb85dd44b | -9.29339 | -65.34417 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd8b9237-9fad-3a88-a56e-b5e1c17b7570 | -9.1422 | -65.31522 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10071cc7-17f1-3030-ba9b-0815a9220e8f | -9.14087 | -65.317 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fd1d1a4-84e6-3549-a4d1-b85ec3344937 | -8.99363 | -64.41549 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91bc2fd0-e445-3455-8e8c-bbb817216d43 | -8.95499 | -64.36109 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d200a987-5755-3c01-8384-5bbd9aee9afc | -8.95055 | -64.3603 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 203ce45f-94fa-3e90-a0df-985a43e6cf43 | -8.94979 | -64.36469 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db1c548c-a80b-3d3f-9702-b0ccd0fc40a9 | -8.80612 | -64.25407 | 2024-10-02 05:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a505ddfb-c979-32a7-aef7-6b8b00a9d6b6 | -8.80536 | -64.25836 | 2024-10-02 05:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4455329-752b-3db9-8644-d101a08f53bd | -8.8017 | -64.25331 | 2024-10-02 05:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3ef36e4-f14e-31d7-8971-bf481f50c953 | -9.57302 | -64.40282 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 536c0a30-3f6d-3498-b0bb-b7c5508a60a7 | -9.47678 | -64.68616 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d953706-d9e9-3bca-bd79-48ba550ee6ad | -9.38054 | -65.46161 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4fa6002-a00e-3561-9c30-f39f5ed33d5d | -9.37962 | -65.46676 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa93c4d9-d597-30f6-b50b-78173a7bb4e8 | -9.37425 | -65.52419 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2456242-f8ce-3253-b6ad-23d55520b515 | -9.36949 | -65.52329 | 2024-10-02 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963f397e-933b-3a13-acbc-671b1f2c41e0 | -9.8954 | -64.67268 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f59a82e1-f36d-3a15-87a8-d59038296edb | -9.8937 | -64.67051 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd9aa11-0f3e-3162-b44f-51dff7d25d4d | -9.89289 | -64.67494 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eedff112-722b-3dcd-b309-6bcd3e68ddc7 | -9.89094 | -64.67189 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21544008-20c0-3ca0-913e-6a9708a83505 | -9.89017 | -64.67633 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 720c436b-f1d3-3109-a0b5-3c0d408d701a | -9.87815 | -64.69247 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd16f278-a6c0-3bfc-8143-23e1c532e771 | -9.87737 | -64.69695 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36636ba2-5c38-3e34-8503-3a13aace963e | -9.75767 | -65.79247 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e14ad1d0-47c8-3cc8-8f4f-b9ffafaa5f1e | -8.75881 | -68.91111 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ca4c668-dc56-3ec4-bb57-286b1a405cb4 | -8.75796 | -68.91561 | 2024-10-02 05:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23fb0a88-1d30-343c-928e-ccaddbd534a2 | -8.25334 | -71.14697 | 2024-10-02 05:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9f43c8a-4099-3da3-8c0a-41899c273f26 | -9.92153 | -66.8428 | 2024-10-02 05:12:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d111d24-a153-3af9-acb1-d55956ba068d | -9.91638 | -66.84183 | 2024-10-02 05:12:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e53120f-8284-3e48-8559-5db1da565df2 | -9.91209 | -67.30532 | 2024-10-02 05:12:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f633815-a20e-37eb-85d4-59ac99de74a8 | -9.69953 | -66.85036 | 2024-10-02 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3756f929-a66a-3bec-980c-f9ce6e2e4a36 | -9.69896 | -66.85349 | 2024-10-02 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6efea87f-c0d9-3a49-8408-86c2df7707ff | -9.67488 | -66.39283 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e09cbeb1-bb95-3e29-9c8e-e1eb54add184 | -9.66986 | -66.39188 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ddea478-7bc6-3c14-81d9-2c1023e5bb41 | -9.61039 | -67.15945 | 2024-10-02 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 759ae946-9266-32f5-b48a-cb251ee61afc | -9.60978 | -67.16275 | 2024-10-02 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb1c52d-5b58-37af-9f40-e244ba704af5 | -9.237 | -68.77855 | 2024-10-02 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2931a2f7-cace-394a-88bc-a0b0dfc48089 | -10.62792 | -68.67215 | 2024-10-02 05:12:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 729a9ac3-d338-3072-96ba-2b5be169836c | -10.62713 | -68.67624 | 2024-10-02 05:12:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ac3ad84-f03a-3f65-a5d9-473512072f17 | -14.7487 | -48.79481 | 2024-10-02 05:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c5dce22-ae41-3fa1-8694-fc72dc807fc7 | -10.27598 | -68.76527 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a949489e-c3e2-394f-9972-2d9ef5a1309b | -10.27519 | -68.7694 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bb1cfb2-d7f1-364b-a546-4a96fdaa39ab | -10.27097 | -68.76007 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b26393ca-bd34-399d-9bfc-75a1aa6b4858 | -10.27018 | -68.76418 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 027d9a9d-bfd5-3610-9b3a-76534d68e2a8 | -10.26939 | -68.76827 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fca76299-1eba-3c12-bcd4-9eb058009e09 | -10.12364 | -68.40808 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0e31eaf-0f84-3393-964f-6b0064b76487 | -10.11797 | -68.40691 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53afab95-0ca5-3490-983e-9b059e7f1473 | -10.05408 | -68.58486 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e5a18da-479a-32bd-8d5c-91499074214a | -10.05363 | -68.5862 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd0c228b-7cbf-3a8b-97df-fe193f2a8cf6 | -10.0533 | -68.58886 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README135.md)
