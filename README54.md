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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3531e0ab-ff2c-3d11-9de1-6ba8a84aeb43 | -11.98058 | -40.84311 | 2024-10-08 04:34:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f6e198ec-4afc-30df-a5a3-02fc08e6267f | -14.12127 | -41.67681 | 2024-10-08 04:34:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1c6934b4-3c12-30bd-91fb-db0115fed8af | -7.327 | -42.00876 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf255c51-0484-39c0-9428-61a5bd1884c5 | -6.82808 | -41.7985 | 2024-10-08 04:34:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 353928a9-7374-3363-829e-a423034c08ba | -6.82675 | -41.79614 | 2024-10-08 04:34:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb60d086-aa28-3c0f-bf38-4a78080d4c3f | -8.80588 | -41.04057 | 2024-10-08 04:34:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 14b2304c-ba44-373b-8fe3-cb76f303f8dd | -8.42467 | -41.95292 | 2024-10-08 04:34:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 590a792c-1b83-3bcf-bd47-756f1e10cdaf | -8.42452 | -41.95115 | 2024-10-08 04:34:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e5729c74-39dd-30b8-a7d8-70d7d3d1bac2 | -8.42026 | -41.9524 | 2024-10-08 04:34:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 72948de2-0651-3545-bd33-db9d906db744 | -8.41529 | -41.95601 | 2024-10-08 04:34:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 533fc0a7-78dd-3dc6-817e-7012f9d28c00 | -14.01583 | -42.47645 | 2024-10-08 04:34:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9e95c7b2-6fa0-329b-a659-f6b1ba355b68 | -7.92825 | -42.45563 | 2024-10-08 04:34:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e303a539-7eb7-34fa-9ec9-95990c0f673d | -7.92405 | -42.45491 | 2024-10-08 04:34:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 79b739f1-7632-34b3-8f24-6dca2f715e3b | -7.78545 | -43.08398 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c12b5753-980c-34e2-a614-87b5a9b1e656 | -7.78494 | -43.0875 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 74214777-88df-31a9-98cc-c3fc3f4b0e01 | -7.78443 | -43.09103 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd953faf-196e-3ffc-b55f-4fb4428b67b9 | -7.78392 | -43.09455 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99cacbd4-a2d2-37da-91bd-570ad0d47e7d | -7.77937 | -43.09758 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f76cb073-c8c5-3eaa-9f76-68a7a519ff86 | -7.77886 | -43.10105 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3be036f7-dc44-3d66-8503-8f645f361320 | -7.77585 | -43.09343 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| eea0ffc9-3fb5-3ac1-a152-586943332a37 | -7.77534 | -43.09698 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34ae6712-05ef-3ad3-8993-eed77320d6ff | -7.73301 | -43.04719 | 2024-10-08 04:34:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 019d65c5-4499-35a3-b2c0-aff974288cd3 | -7.6627 | -42.49557 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 461c4313-49f2-3542-853c-ca45880aef62 | -7.66214 | -42.49941 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a0248f3e-9fcf-3293-913b-7fc790fc4e82 | -7.66159 | -42.50326 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f8556365-ab92-3c60-b860-bb4afaed472b | -7.65962 | -42.48726 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e956c70a-4de7-394a-8cdd-409036134cb3 | -7.65907 | -42.49111 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3bf5c234-e813-3143-813a-1752ae20703d | -7.6574 | -42.50267 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3bf399c8-2395-3f64-9163-9159d31b7e64 | -7.65713 | -42.41508 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14113263-1a2b-37ef-a55f-880548300051 | -7.65629 | -42.51033 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0d50bd50-d1cc-3bba-8ff0-31f83335a13a | -7.65574 | -42.51418 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e25d6d0-f92b-38ff-9d1e-3ab5cd90f4e8 | -7.65544 | -42.48661 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c11731d9-7866-33ba-af90-44ab32fcbe7c | -7.65519 | -42.51801 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1793cef4-ff66-3766-8209-4b86341c651f | -7.65348 | -42.41054 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 04bfbc20-8026-3f47-954f-7f45f17acc23 | -7.65266 | -42.5059 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6a7916d6-4a6b-3202-8284-cfe10cc08591 | -7.65125 | -42.48599 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 083a764b-2775-3cd4-8de8-24e366b5bb48 | -7.65046 | -42.52119 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 08b7ec01-8020-3b48-9cde-30d0012a2c9e | -7.64991 | -42.525 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d1b28c7e-9453-3716-be3f-a62785ffabdc | -7.64574 | -42.52436 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87a248d9-7258-37d8-be00-46d6e87432ce | -7.64519 | -42.52818 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c97b420a-9b75-3fd9-a9f9-800a6b4c9c1a | -7.63608 | -42.412 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcd3dcd7-4ae3-3c29-8817-2ea5e0aba71c | -7.63188 | -42.4113 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76f69fc2-5513-3aed-92fd-1cda633d0c8b | -7.62712 | -42.41459 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1692266f-763a-3037-a022-2e2d1cc52218 | -7.62657 | -42.41855 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 10202b70-31c0-3cc3-a541-1bb97ce1ee0c | -7.62182 | -42.42173 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8457c8eb-88e5-323b-a65c-75eb7307bd05 | -7.62126 | -42.4257 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 66e2f5b7-cb78-31c9-af4d-5c33d7e6617d | -7.62071 | -42.42967 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ccef0fef-2e61-3b88-a19c-3368f7dbfc49 | -7.61542 | -42.43678 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2eb7839e-dba9-3e7d-8d66-9b652a5c99dc | -7.61488 | -42.4406 | 2024-10-08 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b95124b3-ce79-3bee-92d1-9907794b489f | -7.47277 | -42.59283 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9d326b2-d472-388c-8e75-af4aec58d1b5 | -7.14568 | -42.61251 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 34f9e003-0edc-3d56-8251-e5ed59f207fb | -7.14149 | -42.64222 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49e5c567-a5be-33dd-8c27-c829a790dfc8 | -7.13853 | -42.64185 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf0f7a78-77b4-3b62-af4e-c84d30a0e25a | -7.13737 | -42.64164 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9ecc3b8e-e956-3a9c-9da1-c3f4a0e15020 | -7.11689 | -42.64617 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cf21693-e1e8-3dbb-a62e-9abda4f981f0 | -7.10866 | -42.64502 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9f10f66e-7315-333c-b733-bf26d814605b | -6.89403 | -42.83359 | 2024-10-08 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e674c21a-b2f3-30ef-ad5d-93244d3304a7 | -6.89333 | -42.8341 | 2024-10-08 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 598e6ba0-3972-3502-aa8a-567a2d20aa5a | -6.83576 | -42.8035 | 2024-10-08 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e18c5696-be2c-3979-8495-a3f9ee6785b9 | -6.83524 | -42.80708 | 2024-10-08 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4885d78c-10a9-3a59-9001-0ddfc0d7afda | -6.83225 | -42.79919 | 2024-10-08 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9ddb0b73-2595-367e-9f4d-0b35e9e98563 | -6.83173 | -42.80279 | 2024-10-08 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e2a2632a-2dac-3be9-92f4-ec64ef9195fd | -7.30953 | -42.24665 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1b06e42-0664-3c7c-95ee-22b535a76867 | -7.30897 | -42.25071 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5bd06bcc-66c1-31fd-97cc-27291404101f | -7.3084 | -42.25475 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 63edc657-fcf3-360f-8a15-e3ed3f5e7291 | -7.30784 | -42.25872 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e63f462b-3928-34f1-80f2-8550cc8a697d | -7.30585 | -42.24209 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 21be33d1-70de-38d4-991c-4612ebd4f8a9 | -7.30555 | -42.24392 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc463175-6368-3f10-b335-e9bd554a01bb | -7.30191 | -42.2393 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9bb9b869-1e79-33d8-a06d-89ff815aef7c | -7.3016 | -42.24153 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3fbfbbdc-65e5-3865-98c0-3c0d4b7412d9 | -7.30131 | -42.24336 | 2024-10-08 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81dce344-afe3-30f4-887f-af9642a03b0a | -9.52921 | -42.98875 | 2024-10-08 04:34:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 023be700-412c-3af6-8e33-9026003a1d2f | -9.52866 | -42.99259 | 2024-10-08 04:34:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 642cb4de-4df1-395d-af96-7b72a3429b65 | -11.799 | -44.50073 | 2024-10-08 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2cb8e51-c9ec-3eaf-bdb0-3c1f1796a25f | -11.75589 | -44.52493 | 2024-10-08 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb41cadf-3369-3aba-9279-a70d2348d677 | -13.7612 | -44.00354 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fc18c21-45bf-3666-8d09-93d724c16432 | -13.72962 | -43.906 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91c31b54-4910-37d3-988a-2f7637133c30 | -13.72699 | -43.92551 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84de3763-1d45-30a9-bcc6-6121d02ec517 | -13.72645 | -43.92949 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a52b7e2-2c23-3b28-9bf9-24af2b17edfb | -13.68127 | -44.32354 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ea9b1eb-feb9-32e6-8b28-4ac074ec9f53 | -13.5862 | -43.79061 | 2024-10-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6501706b-b4b8-32ac-b640-d7396ff9db8e | -13.58201 | -43.79005 | 2024-10-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57a7f70d-2e82-3861-9f30-8451c1b4c895 | -13.53458 | -44.02365 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7854d4d-2af2-3c0e-8933-ca2128a90fa8 | -13.52131 | -44.40419 | 2024-10-08 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 901fb178-db19-362c-9374-1c92f376aae2 | -13.52083 | -44.40781 | 2024-10-08 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83d480a4-ae64-3c88-9b48-141fd352c01c | -13.49609 | -44.37845 | 2024-10-08 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c20920e5-a66f-3548-9c2d-768bd43e8ab7 | -13.49563 | -44.38193 | 2024-10-08 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84f04ea7-183d-30b6-b54f-e630b64cc792 | -13.4203 | -43.80005 | 2024-10-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8b2c9367-ceac-338a-bd04-12dcab7dbb28 | -13.37805 | -43.76602 | 2024-10-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc33a14b-0d43-3c18-877f-c22d3d852285 | -13.37388 | -43.76542 | 2024-10-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00a709ba-45cf-363d-a4ab-6b6615484f54 | -13.37337 | -43.76931 | 2024-10-08 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e26518b5-c0a5-3853-9951-a92336ca1ded | -13.34452 | -44.70335 | 2024-10-08 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2527c3c-2aea-32aa-883d-3314234d51ea | -12.58145 | -43.36646 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3406565d-4e25-3c52-88ce-c9c6fe447111 | -14.11814 | -44.10065 | 2024-10-08 04:34:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f55356b-03c6-3395-b542-281d556b1e71 | -14.1149 | -44.02972 | 2024-10-08 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c259d8b-7f95-3c80-b458-01824d3ecfd0 | -14.11439 | -44.03359 | 2024-10-08 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 661551e6-d33d-305d-979b-a63dd679db58 | -14.11401 | -44.10007 | 2024-10-08 04:34:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06bb12e9-b5e9-3805-a566-feebc4621394 | -14.02529 | -44.45607 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e138f61d-a0a7-3383-8e72-7f58f45e784a | -13.96211 | -43.97036 | 2024-10-08 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2124a481-9d49-3501-8fdb-d6976f54c8bb | -13.95289 | -44.61759 | 2024-10-08 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README55.md)
