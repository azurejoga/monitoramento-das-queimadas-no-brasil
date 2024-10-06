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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a1f16de-7b47-3777-b978-5eb202bb121f | -10.44343 | -50.67227 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87a4da97-1213-3a6e-86b8-1621e6060e53 | -10.4426 | -50.67918 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f9239e9-b15a-352e-99fd-7bd86482ca54 | -10.44177 | -50.68612 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b08da538-5c02-3151-90cf-fdb1f13d99e1 | -10.44094 | -50.69312 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7bb761a7-caf1-372c-9c59-26f7f60a5af0 | -10.43977 | -50.67029 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9f9f9fd1-5657-3c65-b81a-625a671b9761 | -10.43899 | -50.67721 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5125ceb4-0c0b-3480-b73e-9cc743725c4b | -10.43821 | -50.68414 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ecfa5a2-82c5-35ae-ad7e-79d5100836b7 | -10.43742 | -50.6911 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a782d428-d580-3a69-8dad-0216c237ab90 | -10.43663 | -50.69816 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b70dd8a8-e909-31cf-922c-9f734e7867cb | -10.43624 | -50.6716 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 581e34c5-5d30-3ed7-a009-f0b3cd41650f | -10.43542 | -50.67851 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94d914ee-efd5-3af9-bc50-37c47cd8ea2e | -10.43459 | -50.68545 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 317ad990-cd2e-3a52-98a8-4ccced1f2dd7 | -10.43377 | -50.69234 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 608b9271-8a6e-34be-89c3-fff739501c3d | -10.4318 | -50.67657 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63998df1-c1c2-31ab-a29f-0ee5738c9ab3 | -10.43102 | -50.68352 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b335f6f1-6d8e-3f8d-80b3-da06638dd604 | -10.43025 | -50.69041 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 468f9cbc-b72e-3f98-a23a-7106689514a3 | -10.42948 | -50.69726 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ba555fad-d1af-34ca-bafb-ebbc98b5fe5d | -10.42822 | -50.67796 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad354aac-828b-339f-a677-81c4bd0841bf | -10.4274 | -50.68489 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c0ba3961-c775-3bc1-9d7d-c7a1251dfd83 | -10.42659 | -50.69168 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9b05b6b5-1186-3d46-a9c2-00f6dda9fa5d | -10.42578 | -50.69853 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 19b6b991-fcb4-3deb-a8fa-5dcba56699da | -10.42383 | -50.68291 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 77e1fd70-39e5-3cd0-913e-31ed2e8dbfb8 | -10.42306 | -50.68977 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3a4dff36-b9c1-3885-8888-60ee15f481b3 | -10.42231 | -50.69652 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 456b55eb-8822-310c-9244-b7bf9f805df6 | -10.41862 | -50.69773 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5843144-c781-3c8b-8069-58179855991e | -8.96031 | -52.78768 | 2024-10-06 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836857cb-4da2-3a9e-8ae4-b136ffccfc1f | -8.95407 | -52.78718 | 2024-10-06 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d5b376b-2e76-3829-aa05-c9b00c10dda8 | -10.76356 | -52.47 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba9f4c66-5c01-3716-957a-24b216b71ac1 | -10.76292 | -52.47546 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18d5e1ed-cdf5-322c-a04b-4e82d516baf9 | -10.70325 | -53.03633 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d809724d-04d2-353f-9cb8-f061e92254fe | -10.69958 | -53.03735 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1db9b2dc-3c88-3136-8d5d-8a56819fb684 | -10.69698 | -53.03577 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f414d20c-18da-398c-bb97-35ec43efe64d | -10.69641 | -53.04058 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2d007ca-6b4c-39ce-9efb-dfa68d273145 | -10.69332 | -53.03674 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6efe14e-d49b-3133-8feb-79d9862a0c9e | -8.11526 | -55.30343 | 2024-10-06 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40011e34-d94c-327e-9669-07c542fb010a | -8.11483 | -55.30656 | 2024-10-06 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84c2122f-c8e3-3479-9123-ec2c80955775 | -8.1144 | -55.3097 | 2024-10-06 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43edafe2-70f3-3106-a739-bfae3e35a2a2 | -8.11007 | -55.30265 | 2024-10-06 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6012bbd-6c93-3484-93b7-de40403617f1 | -8.10964 | -55.30578 | 2024-10-06 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a4e35e-3d44-3afb-9502-7a0f57d002d2 | -8.10922 | -55.30891 | 2024-10-06 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a68f2bb-12d4-349c-aa31-f42c9a50b88b | -9.91739 | -57.47841 | 2024-10-06 05:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 727f7c52-ccb0-30cc-a312-8d0b8e4a2ffe | -9.9128 | -57.47778 | 2024-10-06 05:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8275df58-f0b6-3cd9-82e7-410cf3522895 | -9.90821 | -57.47709 | 2024-10-06 05:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ac9a79b-6ff7-3d43-b888-33fde4ea9392 | -9.44154 | -57.82957 | 2024-10-06 05:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a32ea4-159d-309c-b80a-a20b8883f176 | -9.34684 | -58.93985 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6d91ff1-974a-3322-974f-774dbeddd7ac | -9.3463 | -58.94358 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc47d7d-2de2-3413-95a5-83e767913898 | -9.19222 | -58.18054 | 2024-10-06 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c223fca-850e-306c-b00d-2599cb6bfebf | -9.19106 | -58.1889 | 2024-10-06 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc51a5ac-d531-3401-b9b7-9c0d6f8f3800 | -9.12683 | -58.91638 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b9b5a98-9ebd-320d-a94b-1813b79f51b4 | -9.1263 | -58.92004 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5d60aa4-9a4e-3863-96ab-a6fe65056735 | -9.89342 | -59.51015 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 532f6846-fad9-352b-9618-93ba62756fdf | -9.89166 | -59.49388 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210df1ae-7f3e-3b58-830a-019cb4e21e77 | -9.89091 | -59.4991 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e04f967-c28e-318b-b090-f354500adfdf | -9.89017 | -59.5043 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cd2a169-4b02-305b-8e8d-1cd3bddc3d76 | -9.88691 | -59.49851 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78ee6428-bdd7-3e86-986d-c105d8f4bcc1 | -9.88616 | -59.5037 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f2e7a0-bf09-37c2-8cbb-b9e1387412f8 | -9.8829 | -59.49789 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb5cda7-d5c5-38a0-bfe7-4f4340e30401 | -9.88216 | -59.5031 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5e93aa9-375c-304f-b815-368a2d030a35 | -9.87964 | -59.49205 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b92e2d9-5b90-3e00-ac97-b8d5c04b1a86 | -9.8789 | -59.49726 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28df79e8-c53b-3634-b14f-8524dc6047af | -9.82095 | -58.97052 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57438722-0f6e-3794-86d7-e37ffbaf3771 | -9.82042 | -58.97433 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da3a4e84-95ed-3dc7-a79b-230cdf40cea1 | -9.8168 | -58.96996 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f30049be-e0d9-36e7-8ef5-91e613207633 | -9.81628 | -58.97372 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 398d71be-8655-3b0d-9856-e4c0730e55fc | -9.81109 | -58.98065 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c91452da-e95e-3b8b-abf5-7db57e92b4fd | -9.80747 | -58.97627 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34726802-bdb6-3083-a0ab-b7d7bddeaef9 | -9.80695 | -58.98002 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e764b273-c81d-362a-8039-3cb1f1bcafab | -9.80281 | -58.97942 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97b41171-f8d5-30a5-ad85-1ab3d7ed7c7e | -9.80228 | -58.98322 | 2024-10-06 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db5a92a0-1a82-3ef0-bb90-afb38a087506 | -9.774 | -59.39437 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 779cf70e-2f85-30d0-8fcd-2f7b20fff9b3 | -9.76997 | -59.39381 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b900d51a-509c-3916-8a15-d6a3f44a0f6c | -9.76947 | -59.39733 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 242bf87d-ed5a-3268-b36d-5484762aa535 | -9.76643 | -59.38972 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ed2647e-b623-372f-9372-9b2b46785e1d | -9.76594 | -59.39325 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 567e6feb-832b-35f5-892e-176d994d9550 | -9.15736 | -60.66047 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2b7f4d5-ba7f-3bc0-a0ad-90b8ac750cf2 | -9.15365 | -60.65993 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 475e835d-00a1-3e08-898a-b433188d22ad | -9.14995 | -60.65937 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54b76711-2e48-3406-a9dc-6071682f1753 | -9.14625 | -60.65881 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6cdfb7c-b905-32d1-bc46-134a28aa94e9 | -9.1456 | -60.66323 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb21e92a-ca9e-397b-8995-80bc204034b4 | -9.14254 | -60.65824 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d975a8d-dc52-3f6f-af6f-e0cd62692b44 | -9.1419 | -60.66267 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b4dac79-36d4-3b12-8631-7a5239a5d660 | -9.13884 | -60.65768 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 357041d7-b825-35f4-bcb3-8fe32f112a82 | -9.13819 | -60.66211 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53b3300e-e7db-3642-be11-c47df1a3e6eb | -9.13513 | -60.65713 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a8304ab-a8e9-3c2e-91d2-f2a69409441d | -9.13449 | -60.66154 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81775460-ec69-325c-8226-d450c1718159 | -9.13143 | -60.65656 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 896c91ad-8e4c-3cdc-9658-aff5ec17c4f7 | -9.13079 | -60.66099 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 196fc62b-9dfb-3160-83df-eecd78ff4f47 | -9.12772 | -60.65601 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e8d86f-ad2d-37db-bcc5-a675fa390c72 | -9.12709 | -60.66043 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91eb1e8e-2445-3a84-b623-9b1ca9bf42dc | -9.12533 | -60.4021 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0a68e50-d58d-3ae0-9645-f95265f5b90c | -9.1253 | -60.65773 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c58f3c0-d5e6-30ce-81e0-78ba4725bf9e | -9.12464 | -60.66213 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95bb6886-c876-3f82-ab25-fd1e2641a0ce | -9.12402 | -60.65545 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 639ae598-84a1-34ee-8a48-53e9fdbbe681 | -9.12338 | -60.65985 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4574bbac-36b6-365c-9bbe-e44de40d2155 | -9.12224 | -60.39697 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a70c02db-554c-34fb-9afd-97b35e578e9b | -9.1216 | -60.65717 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89733da6-ab9d-3184-844a-3efb2942f10f | -9.12157 | -60.40152 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bfa9718-aa21-34cc-9e78-320a16e65a90 | -9.11782 | -60.40095 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77efee6d-4e60-3e0e-b0a8-4390e6b05b16 | -9.27484 | -60.82397 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b8381f7-37e5-30e5-b5d6-6788ea462bbd | -9.2742 | -60.82833 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README137.md)
