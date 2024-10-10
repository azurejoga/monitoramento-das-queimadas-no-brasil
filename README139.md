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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 758fff96-26ba-398b-8be1-517eab9c9f25 | -9.07084 | -61.39891 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d4f0b51-6ded-3ccd-81ec-2ab91f1c988e | -9.04148 | -61.62099 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6e59f68-3510-3943-8f7b-7fc7ead39b35 | -9.03855 | -61.61647 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b3e17e0-1e48-3c8a-85fc-054973156455 | -9.03796 | -61.62045 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3c145ec8-5457-3c10-b59b-3d500e1df9cf | -9.03503 | -61.61594 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 293c31cc-8b86-3e82-a4d7-eb7c3d08e36b | -9.03444 | -61.61991 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 014ae984-c70c-32b9-a5de-eee4d36dad43 | -9.03151 | -61.6154 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c72e83b2-c34e-3a02-b642-b4bc02531358 | -9.03092 | -61.61938 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d048c259-17c0-336f-a40f-f9f6b9cf111f | -9.02798 | -61.61487 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b48ff4a-7b86-3687-bea4-1865b99c9114 | -9.02739 | -61.61885 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64bce589-c03b-3f67-ab20-2b2934c8865f | -9.02446 | -61.61434 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f9a8e550-2629-3294-889c-2a40dc86de0d | -9.02388 | -61.61831 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94f460aa-e94d-3412-ba0c-b76995b45dc5 | -9.02328 | -61.6223 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcb489c0-85d5-3aca-a6c6-901772e12a6c | -9.02094 | -61.6138 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 527f70d0-9e78-3223-935e-d031358054d2 | -9.02035 | -61.61778 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af76c5aa-db0f-3ae2-acbd-2bed15445c97 | -9.01977 | -61.62175 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ef06183-3a25-367f-9214-5aaf3cbadf70 | -9.01742 | -61.61325 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24789716-cf09-30c8-a72a-d813f03fa632 | -9.01684 | -61.61723 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a11231a-0a8c-323a-8abd-f5cad6e90226 | -9.01625 | -61.62122 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba05900b-1cfc-38f6-86c9-2ffe8bddc87f | -9.01566 | -61.62518 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f880a0bf-3607-3d23-aee0-469cbc72c938 | -9.0139 | -61.6127 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a05ea53-761d-347c-a6cb-cb4a6be61565 | -9.01332 | -61.61669 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30757555-0d2c-350b-acd2-1f065a997724 | -9.01273 | -61.62067 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25fed24d-1ca8-3489-8992-08b08b3f8638 | -9.0098 | -61.61613 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1280dfc-64a3-3c2a-9849-27e7e2ce5c11 | -9.00805 | -61.5545 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3e865ac-4f86-37cf-a423-6d289db7156d | -9.00746 | -61.55849 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1740ed4e-e703-3c3a-9bd5-377369929b66 | -9.00218 | -61.619 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04a27309-88da-3303-8196-05d97305357b | -9.00159 | -61.62298 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a755c82a-a053-3785-9ab1-45ff6add3f01 | -8.99983 | -61.61052 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda79199-9b0a-3313-8bcd-d8db82f5da19 | -8.99924 | -61.61449 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92f60ed9-067c-34bb-aa24-8f46ba107a11 | -8.99866 | -61.61846 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67ec4a15-0ddd-3d0f-bcf9-8aec2ed56229 | -8.99807 | -61.62243 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcba383e-77b5-3057-9195-6871f5759fd7 | -8.99691 | -61.63036 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeb6663d-fe9d-3276-85a8-a666f4c0c4ca | -8.99572 | -61.61395 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e08ef5a-052c-3c15-8c91-7d2e1afcfa45 | -8.99562 | -61.61112 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7127bc01-b270-3aa7-86f7-81c35f38d079 | -8.99514 | -61.61792 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5851a5c-a9e6-36c0-ae91-4234e7848022 | -8.99501 | -61.61508 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e477575a-7e72-31ea-af25-5050ebcf7a1f | -8.99456 | -61.62188 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c216a0-6032-3e6f-8a09-8a0984bd6dc7 | -8.99441 | -61.61905 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2661c942-6d03-303f-8e6c-e14e2e3bc78a | -8.99397 | -61.62585 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa3c714b-285e-33e9-87d6-03c8968bcaa7 | -8.99381 | -61.623 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6dff524c-8c2b-3f42-bb2f-a61ba4589c0a | -8.99162 | -61.61738 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61d4d7cf-db93-398c-865a-168c9a9886ea | -8.99104 | -61.62135 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 447e1344-6b5d-33b8-b556-6f927bc8bd4a | -8.99089 | -61.61851 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbe947f6-9e66-328b-a646-4e44b719a3b4 | -8.99045 | -61.62531 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4d11f7c-76df-3bd3-a12b-199b7b66bf04 | -8.99029 | -61.62248 | 2024-10-10 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6e645ff-0cf1-3549-8db6-37fd070b55f6 | -12.89806 | -62.18509 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04b792d1-e91c-3874-9f8e-716c55147627 | -12.99365 | -62.74365 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0933c92-0bb9-365e-a9d8-29ccfbbfff6d | -12.99016 | -62.74311 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e65dd87-7b53-3a7f-bb16-22cac9aaa6c6 | -12.98959 | -62.74707 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3869c7ef-b7fa-3e5f-aa7d-179174084ef2 | -12.98668 | -62.74258 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c08c795f-1f2e-374b-a666-5d99912b61b9 | -12.9861 | -62.74653 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68ccecde-cb2e-3ed3-b601-716b5e3a417b | -12.97557 | -62.69635 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe5ac84b-1219-3529-9e86-38caf66bb248 | -12.97513 | -62.79717 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0233c441-23da-396b-b2e9-bf36652d3bbc | -12.97208 | -62.69582 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00283cf7-fd8e-3db8-bcc8-f2c5d9a315bc | -12.9715 | -62.69978 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06eb63da-7244-3b0b-9be4-51a52a02f178 | -12.97093 | -62.70375 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23631b79-905b-3a0c-a30c-cc79ec4f17a4 | -12.96916 | -62.69132 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aa81692-78b5-3b04-9ecb-8827a2a9399e | -12.92584 | -62.73371 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1622100b-0a79-31b5-88c5-db1639019bfa | -12.92294 | -62.72922 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ee019e8-1e59-3c4c-80dd-c9753275c177 | -12.92236 | -62.73317 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a14fcb7-566c-3b33-9f42-ed163fba1eed | -12.92177 | -62.73711 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa772ed8-3ca1-39ad-9c33-73607d07db23 | -12.91946 | -62.72868 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c296c03-fc67-3cea-95cc-cdaa201d3b60 | -12.91887 | -62.73262 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1042529b-6c72-3aca-bf79-086747a6c98f | -12.91771 | -62.74052 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24ec5e85-bb99-34c1-98ac-394e4108457b | -12.91307 | -62.72366 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b6584f1-b1b1-3e47-8be1-029431f52b99 | -12.8887 | -62.79235 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efa5af48-692e-307a-84bc-54dd2172a58b | -12.88407 | -62.79964 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f220959-01fe-3c0c-bec3-ee37053e4a53 | -12.88175 | -62.79126 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c6de8263-9a56-3e75-93a3-7e2180a16747 | -12.88118 | -62.79519 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5850fb8e-d432-3c09-8036-5b82f99a32f4 | -12.8806 | -62.79911 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92f7b01f-eb06-34c5-b6f9-50a8c72f1886 | -12.87945 | -62.80693 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cc877468-4638-31cc-9c9a-5f4c8b0b30d3 | -12.87597 | -62.8064 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 64d801c3-4dc0-33b6-ae2a-33932bd66d8b | -12.87478 | -62.76607 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27ab7971-16be-3b3e-a704-d87a7d25744c | -12.86903 | -62.80532 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86aba573-9fee-3065-8b84-76717795a248 | -12.85746 | -62.81154 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 408453cb-e89d-3317-a8e1-91c4e2fe35e2 | -12.84414 | -62.80546 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7139fec5-fcca-350f-8dff-2e756aa2b0dc | -12.88986 | -62.78449 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1af4cd73-dba0-35ef-ac9e-c79d46a7094b | -12.88928 | -62.78842 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00408716-6e40-3795-9d89-24c0111415fc | -12.88638 | -62.78395 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4baf0bf2-f91d-3655-b3c2-c63b841d3c11 | -12.8858 | -62.78787 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9569b645-e469-391e-a28d-0f56713527d2 | -12.88523 | -62.7918 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc60b021-ef36-3a1a-a4ae-ebcddf6b98b6 | -12.88002 | -62.80303 | 2024-10-10 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f8d36ec0-1c22-3273-b361-c409f66f3d54 | -12.86555 | -62.80479 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9269e7f-d855-326b-b0f0-5ae26d85949b | -12.86151 | -62.80817 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06d1c524-a32e-3186-90f0-120804e3d952 | -12.85803 | -62.80762 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb653376-b320-3a3a-a223-1784d5b15ceb | -12.67841 | -63.07804 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ae7d1c7-7f55-35f1-be05-4d89b78ebdef | -12.67498 | -63.07751 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5eee3ed-660a-3771-b6c3-ac61987e7893 | -12.67441 | -63.08132 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f1199c-73fb-332e-bd1e-285a98da39be | -12.67155 | -63.07697 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bfc09b0c-9b9d-303d-b4a4-04e4564cecc9 | -12.67097 | -63.08079 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4edc2430-8df9-37bf-87ff-cfcd93a3a86f | -12.6704 | -63.08459 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 576eeb84-902a-3f00-8888-827383ecd475 | -12.66812 | -63.07644 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fcfa198b-247c-325a-9991-a08cdf7b8890 | -12.66754 | -63.08025 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b66cfe87-3aa5-3742-b847-69d2a8a4f3cb | -12.66697 | -63.08406 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29b1cdf9-c769-33d8-b847-12710e868788 | -12.66354 | -63.08352 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be9069a7-7ffb-3a26-975d-922a2679d12e | -12.66297 | -63.08733 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd11a3e-08a5-39fe-9a66-cceb227dc078 | -12.66011 | -63.08298 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 148ece48-bca0-3f52-b1b2-72f74ce12f38 | -12.65954 | -63.0868 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a955d5c-d0fe-34be-bc64-7fabf02823b0 | -12.46936 | -62.99985 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README140.md)
