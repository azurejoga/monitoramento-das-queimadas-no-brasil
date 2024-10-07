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
| c6f7b64d-baf8-39c8-bb22-7cfd248146ab | -3.74546 | -59.32882 | 2024-10-07 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eced647e-23e0-3808-bd62-1f062f6ae416 | -3.7449 | -59.33249 | 2024-10-07 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c240023-e526-3085-9b6f-8b855411ec12 | -3.74079 | -59.33189 | 2024-10-07 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4591461a-d29d-3490-b473-17e24d687936 | -2.99816 | -61.42587 | 2024-10-07 05:40:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c1f78a3-37dc-3910-b35e-d5ccbc60c226 | -8.60698 | -63.51523 | 2024-10-07 05:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a68bbfc3-feb2-3241-890b-b96f8a74b3b6 | -13.38918 | -61.93284 | 2024-10-07 05:42:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0dad3f50-fb74-3bab-8150-b272035a1f93 | -11.90139 | -63.2412 | 2024-10-07 05:42:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e58a32e3-f12f-31c1-aecf-efff42eadac9 | -11.90078 | -63.24546 | 2024-10-07 05:42:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bcf1d67-b74b-3491-9a1d-fb0cefca8ab7 | -11.89777 | -63.24067 | 2024-10-07 05:42:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d722dde-f01d-3d77-a695-491256a4876e | -11.89716 | -63.24492 | 2024-10-07 05:42:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f41752-2fb8-39ce-baa1-2e182f1855a4 | -12.9948 | -62.72147 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2843888-83a3-3ceb-8da9-5bb1ce657795 | -12.99036 | -62.72559 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a12aa9c5-e6ba-3292-9ffd-0b7f06ac3a8e | -12.9819 | -62.67656 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a85a30-e3ef-3f9b-832e-5964ad60f4f8 | -12.98124 | -62.68125 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e0fe160-6ab0-3623-9869-2ae5aec548af | -12.97745 | -62.68069 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac3de412-5ef8-3f3a-9f22-de96a2c0767f | -12.97301 | -62.68484 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9db6997e-ddc9-3e92-b0fc-17fff457a626 | -12.97235 | -62.68954 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a6d2faf-916a-3c83-b615-bee194c3bca8 | -12.95424 | -62.46608 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ba0e306-c8f6-3258-89d1-8f625c152c05 | -12.9533 | -62.46355 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ac0898ea-e912-3846-88f2-a760f2ba9863 | -12.95041 | -62.46552 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 20a67c91-f507-3215-8658-f44175d3d9fd | -12.86841 | -62.79494 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cbe3e50-0bd4-3142-8ddd-b9959cb07a8f | -12.86608 | -62.67604 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a10080ce-205f-3608-85dd-5cde73fe98cb | -12.86532 | -62.78976 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d21ae720-3b92-31e6-aa3e-ebf832ff7019 | -12.86466 | -62.79438 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08f9d82f-c8ae-3b1a-90b2-b7b689b82e9a | -12.86156 | -62.78921 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 547a1804-94f1-3256-9259-beff96fca17b | -12.82609 | -62.47063 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 434ab689-003b-3d0f-8671-dd1ec833ddcb | -12.82227 | -62.47006 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ad07c4d4-c948-3248-8ba7-dc69de7d2eac | -12.82158 | -62.47485 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 90f19b64-5edd-3bc8-b6b2-614190a0d3df | -12.81844 | -62.46951 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0d4c66ec-55ea-3897-b8b3-e9be9e4f0c39 | -12.74675 | -62.26851 | 2024-10-07 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6c09fb5-5205-3273-915d-9aaefe79bd9e | -12.83404 | -62.90216 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c493859-c730-3a58-aae8-6d89217553cf | -12.83031 | -62.9016 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f32eec8-b584-3b56-8fc1-8fc1e5fb47ff | -12.72155 | -62.90692 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55184671-7253-314d-9ab3-a985e0774764 | -12.72091 | -62.91145 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 288794cc-a59c-31df-ba21-94063f2a6473 | -12.71783 | -62.90637 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16a9a3ed-8f62-3e7e-bd7b-d2a2899a49d9 | -12.71411 | -62.90582 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca406368-61b3-3733-9a5f-9f54c5c4ae55 | -12.71141 | -62.95152 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1d769f8-f56f-344c-96e2-1f4cf961cf0d | -12.71077 | -62.95602 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a5a7175-f1db-34a6-9ece-388e8c413c09 | -12.7077 | -62.95098 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ecd94df-a506-3fcd-9a41-42bacc7874a3 | -12.70706 | -62.95547 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2e8b58a-d7f6-31a6-aba2-a545597c88a6 | -12.70399 | -62.95042 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8cfa1135-1ddf-3a75-b78b-0cad32a6863f | -12.70335 | -62.95493 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 846609c0-6fbf-3b0f-8991-b5b2404c6bc5 | -12.70283 | -62.93185 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ed3bfa1-e8d7-3a85-b986-b3db6da9adf2 | -12.70219 | -62.93636 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19ffb803-6101-3618-9cb9-0e075599d85e | -12.70091 | -62.94537 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4503d2dc-5fb1-3889-b6b3-460612f407e5 | -12.70027 | -62.94988 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 66f1b120-d4da-3774-9f9a-6b54f60b4cf9 | -12.69964 | -62.95437 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 71a92dd7-544f-3356-b85d-2bc46e8fb76f | -12.69911 | -62.9313 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0342d375-b831-334c-afbe-b637dc399c9a | -12.69847 | -62.93581 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cfa70fa4-6041-32a8-9247-d30541a1d19d | -12.6972 | -62.94482 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dd017721-fa09-3ae3-9a83-f6fc52fdf608 | -12.69656 | -62.94933 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d15c4ee4-6040-39e2-8ac4-60089573b76a | -12.68126 | -63.08394 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e223839f-6465-3de7-a83e-e83ccab8a2d6 | -12.67326 | -63.08727 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6987c45e-3ef3-3f1e-b750-8a8d767f517d | -12.66958 | -63.08673 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d846e2b-2193-37fc-979f-791aa394aa4c | -12.62386 | -63.12207 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7eac70ae-ca42-3af4-a4a8-1a61c5450126 | -12.1165 | -63.84836 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2bf8b12-9137-3a7f-b7a7-eb051cab5600 | -12.05376 | -63.78265 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef59cc59-344b-320b-acac-5f5d0b1b98c4 | -12.05023 | -63.78211 | 2024-10-07 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c034b8e-9540-3230-a4aa-3c22ae3b683b | -11.69208 | -64.03156 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0296b879-b1d7-3d77-831d-df8b2e949d4b | -11.69151 | -64.03542 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9ecac06-54ee-3ae8-9547-b7dfaa4e3f49 | -11.68858 | -64.03116 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deb055e5-c933-3f38-90bc-6047fc195a03 | -11.68801 | -64.03502 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe7a0e5a-5369-3351-8182-172c5beb21b0 | -11.67811 | -64.00558 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c234934-f4a0-34ba-ae9d-d8564995bf41 | -11.67755 | -64.00935 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38f04a91-5763-34f7-959e-80b453f86577 | -11.87358 | -63.28046 | 2024-10-07 05:42:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70d0f49d-4e49-3ce5-a5cc-2bf77f4107a1 | -11.96749 | -64.76516 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b2cc4502-5045-3399-9491-cb457f77783c | -11.96726 | -64.76211 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3cc8dd6e-4101-3c3f-9302-0445c222bc9b | -11.96669 | -64.76583 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54dd3b38-1039-3308-8d75-66510ec712a8 | -11.66822 | -65.20715 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae4384ce-c183-3935-aa0a-4592aed3a061 | -11.66766 | -65.21075 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6bc4009-aba4-3370-9e32-5c1b77612cb1 | -11.66096 | -65.2097 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee117549-87a1-3255-9bc8-ddbec20d75b3 | -11.6604 | -65.21331 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b369094f-a77c-3c47-a5fa-cec275df0279 | -11.60182 | -65.00028 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab816e2a-8d48-3587-9fd0-c55e7b229bdb | -11.59845 | -64.99974 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d06444b-6143-3a58-a4f1-0c24672b94b2 | -11.58893 | -65.01688 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 669c9779-5599-35f8-a743-c5664eb142d9 | -11.58612 | -65.01271 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9389fb88-c83d-3eaf-b7fa-791b5f20860e | -11.58556 | -65.01635 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7f4c85e-b12e-356c-8e4a-0c2924e564e9 | -11.5822 | -65.01582 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a21bf9a0-a323-39ac-98c2-f97ccfd4a677 | -11.58164 | -65.01946 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef161304-9013-3d85-9367-15492e443659 | -11.57771 | -65.02258 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e449dece-8eed-3395-b027-85083416aada | -11.57042 | -65.02518 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50777b72-b043-36a8-a278-991789a27be2 | -11.56987 | -65.02881 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 539d526f-1f51-3775-ab5a-764333bf7eb3 | -11.54315 | -65.13605 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b58ce8ef-471e-36b9-8e51-8feff6a5efaa | -11.54259 | -65.13966 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac75e5cb-3e63-3358-ac5f-378d518b2b75 | -11.53979 | -65.13554 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7a20c06-dcec-3e05-910c-4eaad6fef956 | -11.53924 | -65.13914 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98da7260-f29d-3596-b0b5-754a1b11e3cb | -11.53851 | -65.05369 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f17b6e95-4ee5-3924-bd4e-a835c4451852 | -11.53514 | -65.05316 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d70e7bf-1c20-33be-a52b-6161620edbda | -11.53233 | -65.049 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c341ba6d-6d40-3a2b-87d9-82567ed2a863 | -11.53197 | -65.1417 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0440673c-e3b3-3388-b764-a000b047ba4f | -11.53178 | -65.05264 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ee96e51-ccb9-33e4-b56a-1fd223bb853b | -11.52916 | -65.13757 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c0a93ec-179d-35d3-a612-1eb3c6a64f45 | -11.52897 | -65.04848 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a6b055ee-87fb-34fd-b365-5bb262fd52c3 | -11.52861 | -65.14118 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f54dc819-28ce-34c6-a4d4-460e8f04eef8 | -11.52841 | -65.05211 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 618c4f90-1660-3b0b-b5b7-37ff40ce8475 | -11.52525 | -65.14066 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 29d5222e-a282-3849-bcf5-a4f853c08427 | -11.5247 | -65.14427 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9a356f16-045a-31f7-85ca-7835be9e8f1f | -11.51678 | -65.106 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6bdc1f4-02ad-3cde-89eb-da25a5a98845 | -11.51562 | -65.09098 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b25a0bb-73fd-39b8-b45f-1dc7f71ee64c | -11.51397 | -65.10185 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README132.md)
