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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7137d5f-c9cb-3eb0-a9f8-447e69b73509 | -3.07907 | -53.06491 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd74b3c1-9b1e-377b-97bd-3a8ee4525f39 | -3.07851 | -53.06845 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0ab9924-d7e9-355d-a613-ba5ae4dde443 | -4.00769 | -53.7697 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b31b141d-9a11-3b2b-a88f-dd0f4abef9e8 | -3.73726 | -53.73529 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a9454e5-ab52-386f-b38c-5601d2b90a5d | -3.76623 | -52.33571 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd74b65b-9efa-3b7a-bb8f-a5f3eebaaa3e | -3.76569 | -52.33918 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff6ca945-8041-3c9e-a578-0ad8fcdcd71e | -3.76291 | -52.33519 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44009730-5f28-33c4-95e5-4ea3f85d56f0 | -3.76236 | -52.33866 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e0d6454-6c3b-30a4-bf73-24ac60d7ee7f | -3.76052 | -52.26387 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 508a24a7-afa1-3d87-8932-9a1a194c5674 | -3.75755 | -52.41249 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fded647-e352-301f-93e7-19d0aa0c0016 | -3.75719 | -52.26334 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dec7f4c0-7480-3442-933b-6ccebb393117 | -3.75387 | -52.26281 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 748bb111-7c7d-3e74-801b-cb13d82e48cd | -3.72285 | -52.26509 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 044810dd-e0ef-31e8-919d-906a456db7c9 | -6.57998 | -52.92128 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba517c41-3382-3b31-b00b-58ea2b0f73e8 | -6.57944 | -52.92475 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a21a46c-1363-31b8-a3f8-ccd851a33f64 | -6.57556 | -52.9277 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5db5c55a-e935-37a7-8b3d-4c0617f4273f | -6.57278 | -52.9237 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6abe52db-40e7-3352-a2f7-80894f4f856f | -6.56116 | -52.93255 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55eaf9a5-c38a-3c1c-9453-a7e73557ac5d | -6.55783 | -52.93202 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cc48d17-0f07-312a-ab07-93939df57b95 | -6.40478 | -53.67828 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51d575b-05ac-38fc-bd86-d13619036500 | -6.24404 | -53.32973 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47a9448c-fe13-39e4-89c4-b706943b10e3 | -6.23401 | -53.32815 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d24405c1-1000-3c62-ac2b-140c75a3f9be | -6.23345 | -53.33167 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e4209c2-af1b-3dc1-889d-f3f6a06ce3c6 | -6.19511 | -53.27871 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85b24808-e4ce-3d57-bf63-ceded7538081 | -6.19456 | -53.28222 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b227da23-ed9c-3de4-9f73-3c277d8bef96 | -6.19177 | -53.27818 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfddc126-7151-35bc-8b2b-ab4856e93c6c | -6.19122 | -53.28169 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65f820e8-5fc2-32c8-913a-c772dac46fd4 | -6.10911 | -53.22589 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0054607-9439-331b-b8c9-64492e9eb9e5 | -6.10856 | -53.2294 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d089cf46-97d6-34db-8ccf-edd306952236 | -6.10577 | -53.22535 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f7e32e8-1094-3493-92ac-a08fc11238cf | -6.10243 | -53.22481 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 218aa061-63fb-3f38-92c5-8f561a70d91b | -6.10076 | -53.23536 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3de9b79f-5a40-3a12-bf98-243d78865f11 | -6.09742 | -53.23484 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8b7eab4-42c0-3c2b-8c54-93704a25dadf | -6.08669 | -52.83245 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28618e61-53c5-3024-a810-0e38213006fa | -6.08614 | -52.83591 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ae87cf4-c931-379e-8093-62bc5318d247 | -6.08391 | -52.82846 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0d95e70-8a85-3a37-91b7-f1e03c4eb9d8 | -6.08058 | -52.82795 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56f89b16-d82a-3911-b2e0-f56271889e89 | -6.0778 | -52.82397 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecb41aa2-23a2-3d35-943a-78bae158ed28 | -6.07725 | -52.82743 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6748a9c-001f-3af3-af7b-efbdd36e870a | -6.07393 | -52.82691 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e66b5c01-b78e-3685-8e7e-bf50897a2aea | -6.0706 | -52.8264 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44998192-5ac8-3b55-bff4-6eec58822ca2 | -6.07013 | -52.87258 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0545af5d-8998-30e1-ad4c-87aa08b6d8c5 | -6.06958 | -52.87609 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e44c7331-6075-3185-bdb7-563a365d71ea | -6.0668 | -52.87206 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9612db82-5174-3f97-8d89-09af533ac2d1 | -5.87843 | -53.88597 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1b724c3-4482-3ec8-9ba9-67366d20a7bb | -5.87447 | -53.88905 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a02c036-b295-306d-b4ab-bdac6a680a6e | -5.85091 | -53.55386 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90f8e45e-0ec2-375d-8498-a7a404bf04ea | -5.85034 | -53.55741 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9ea526e-8e2c-3e63-9918-163cdb3d073d | -5.84698 | -53.55689 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5772973-fc16-3100-aca7-a2432a4d8a1b | -5.84641 | -53.56045 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e393ad8-e109-38cb-b20c-146b01ab3fd4 | -2.14451 | -53.65551 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59da4886-04c7-3fb7-98da-5f08349d1af7 | -2.14164 | -53.65122 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff6537ce-b94d-3966-b6e4-2c0bb7e1257a | -2.14105 | -53.65498 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2bc696e-d000-3910-86db-c9a628b7b3c8 | -2.13759 | -53.65446 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 169cd41d-bed6-3c49-9a12-40d9155e3a96 | -1.83052 | -53.9553 | 2024-10-03 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d055f4-a5e0-3982-99f1-306c83f99eab | -1.78294 | -53.48483 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ed99243-73d6-3b1f-a711-a0c987523170 | -1.76258 | -54.44955 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 196f366f-caba-36ef-99a0-b3c7ed49cd68 | -1.75964 | -54.4449 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11b75639-f121-3b17-9e08-2d14b6c570a8 | -1.75899 | -54.44898 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0da2891f-3e11-3138-a068-1171336124cd | -1.7554 | -54.44841 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6860df5b-63b5-3931-af67-fc549890937d | -1.75474 | -54.4525 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e14ea334-f08d-33dc-8680-d36a9864400b | -1.7518 | -54.44786 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d8cc20d-b084-3f8e-9fdc-72473fda251f | -1.75115 | -54.45195 | 2024-10-03 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca7af798-42c0-3fca-bcd8-26dac2e73431 | -1.15753 | -54.21914 | 2024-10-03 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73c29467-2246-3019-a502-a859b4ec9fa2 | -1.14046 | -53.64242 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 888e8265-9e68-369d-9427-a8050ab792fa | -1.13818 | -53.63428 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a28d5b15-2914-34dc-bbd8-0feeebf9151d | -1.13757 | -53.63815 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78e7322f-9e08-38a5-98db-52e587ed0e53 | -1.13696 | -53.64199 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb5b020c-21c2-3d79-b69d-0704822853b6 | -1.13469 | -53.63379 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1e92a8f-76f0-317f-a21f-267b9d94780e | -1.13408 | -53.63763 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb929976-8587-36c8-9936-4361a6f3ba7d | -1.1306 | -53.6371 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb66418d-c471-3883-8d85-c9cd8d4b7624 | -1.05061 | -53.52754 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee1a899-1b81-3c2b-a017-1cd40a178c64 | -1.05001 | -53.53135 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32e62acc-428e-3a48-93d8-988e16f93b86 | -1.04774 | -53.52319 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de5cc6f1-3847-3d04-a665-55cea8a6807a | -1.04713 | -53.52702 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35a71c16-479c-3b22-88ee-cfc4cbdf82c5 | -1.04653 | -53.53083 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa43b4a9-e19a-316f-b2df-b1463da8edbe | -1.04487 | -53.51887 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38d7f98b-7efb-3db4-a3c0-a04a4f0687c3 | -1.04426 | -53.52267 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d4d3fb7-d11d-3e80-b0c9-5fbb2528531c | -1.04366 | -53.5265 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd4c37c0-538d-3bbb-b1f5-bff648571955 | -1.04305 | -53.53032 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| faa16033-6c4c-3264-b05c-e341ad520d6c | -1.04259 | -53.5108 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9ae912d-6761-3567-9e96-a427719e5f8b | -1.04199 | -53.51458 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4219678b-4525-3f29-a0ba-ac8bf0343686 | -1.04139 | -53.51838 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d4387d4-e88e-329c-b29f-91217de6a567 | -1.04079 | -53.52217 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b93d80b-1b9d-333a-aa68-11eb6bdd481f | -1.03912 | -53.51027 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf62c5ce-bc80-30f2-8842-402a26ddfaf5 | -1.03852 | -53.51406 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05af35d0-e8fc-3eea-b533-8a9d347137a9 | -1.03791 | -53.51787 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd0b004-17cb-3923-9036-1d0240a50c4b | -1.03731 | -53.52168 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30131721-1f44-3378-8b59-6dff4eafbf95 | -1.02918 | -53.73105 | 2024-10-03 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a5b141c-6352-3744-8c06-19369ece3b57 | -3.50601 | -54.02893 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d1a412a-cb84-3c6f-8272-01066805c96b | -3.50542 | -54.03269 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 159d0518-9b00-36be-892a-07848a0bc4ee | -3.50255 | -54.02837 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d25af16-dd18-3bf8-93e6-d793201fcf3b | -3.46475 | -53.79932 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbd23cec-314e-38b1-a754-4ebf68981c6d | -3.46353 | -53.98349 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac73f653-86b1-3bd5-aba4-f3b6af5b6e10 | -3.46293 | -53.98726 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01ee3cb5-3bcf-3fdf-b750-009d6f2a3e0e | -3.46067 | -53.97915 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47472fc5-e964-3613-949c-bf78542e60a3 | -3.46007 | -53.98293 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17b7860e-0db5-3860-86e4-a01175a608cd | -3.45947 | -53.98671 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 216f76a8-f7ef-386d-9b7f-33beaafa86e3 | -3.45722 | -53.97858 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86328f67-2416-369f-a1dd-2c85e95c5f84 | -3.45661 | -53.98236 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README120.md)
